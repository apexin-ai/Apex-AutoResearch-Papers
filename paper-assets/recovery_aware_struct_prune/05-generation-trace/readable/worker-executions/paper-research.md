# paper research

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_paper_research_20260518T031456.log`
- **Structured JSON:** [`9baf7b14f6d9f7f2f74b.json`](../../sessions/9b/9baf7b14f6d9f7f2f74b.json)

## Before a recorded user message

36 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17",
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
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
  "uuid": "607842a4-3ee9-4680-af01-5d25fbb1a218",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17/memory/"
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
    "resetsAt": 1779090000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "21e5177a-3b5c-44db-9ded-d5f4aa08f1fa",
  "session_id": "309d620c-950c-4540-b56d-67840476ff39"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the existing literature_map.yaml file and searching for relevant papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "e449fbf4-1af2-46d8-a8ec-74f749ede964",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7bQ3a8rVCZUZ8MfisXHku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7307,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7307
      },
      "output_tokens": 27,
      "service_tier": "standard",
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

I'll read the existing literature map and search for papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "2f978953-d316-47fe-a399-76431c89de8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7bQ3a8rVCZUZ8MfisXHku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7307,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7307
      },
      "output_tokens": 27,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01E4Kp6bbMtkozpPfcvPmqPS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "50c3607c-6436-48fc-b472-d9411a0924b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7bQ3a8rVCZUZ8MfisXHku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7307,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7307
      },
      "output_tokens": 27,
      "service_tier": "standard",
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

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BmJbUPrRVjAxG7Avk1UXUx`</summary>

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
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "70aabfb9-1f9d-45d8-a889-39db05ffe876",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7bQ3a8rVCZUZ8MfisXHku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7307,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7307
      },
      "output_tokens": 27,
      "service_tier": "standard",
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

_source line 8 · 2026-05-18T03:15:07.654Z_

<details><summary>↩ Tool result · `toolu_01BmJbUPrRVjAxG7Avk1UXUx`</summary>

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
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "6b327493-4398-416f-b047-a54f6f8879c7",
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

### Tool result

_source line 9 · 2026-05-18T03:15:07.743Z_

<details><summary>↩ Tool result · `toolu_01E4Kp6bbMtkozpPfcvPmqPS`</summary>

```text
1	papers:
2	  # === Direct Competitors ===
3	  - id: self_healing_2025
4	    title: "Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning"
5	    authors: "Yixin Ji, Zhimin Lin, Juntao Li, Kaixin Wu, Kai Yao, Xu Jia, Linjian Mo, Min Zhang"
6	    year: 2025
7	    venue: "ICLR 2026 submission (OpenReview #12375, submitted Sep 2025)"
8	    category: direct-competitor
9	    role: "RLVR recovery baseline"
10	    relevance: 9
11	    key_finding: "RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%. Tested on 5 LRMs across 6 math benchmarks."
12	    our_relation: "We extend beyond single sparsity ratio and add CKA-guided pruning selection"
13	    citation_priority: must-cite
14	    arxiv_id: ""
15	
16	  - id: resp_2025
17	    title: "RESP: Self-Reflective Structured Pruning for Reasoning LLMs"
18	    authors: ""
19	    year: 2025
20	    venue: "arXiv Dec 2025"
21	    category: direct-competitor
22	    role: "Structured pruning for reasoning without recovery"
23	    relevance: 8
24	    key_finding: "GSM8K 81.3% at 40% sparsity via self-reflective importance"
25	    our_relation: "No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity"
26	    citation_priority: must-cite
27	    arxiv_id: "2512.02185"
28	
29	  - id: grasprune_2026
30	    title: "GRASPrune: Global Gating-based Structural Pruning for LLMs"
31	    authors: ""
32	    year: 2026
33	    venue: "ACL 2026 Main"
34	    category: direct-competitor
35	    role: "SOTA budgeted structural pruning"
36	    relevance: 8
37	    key_finding: "Global gating achieves best structured pruning under budget constraints"
38	    our_relation: "GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top"
39	    citation_priority: must-cite
40	    arxiv_id: "2604.19398"
41	
42	  - id: opsd_2026
43	    title: "OPSD: One-shot Post-RL Structured Distillation"
44	    authors: ""
45	    year: 2026
46	    venue: "arXiv May 2026"
47	    category: direct-competitor
48	    role: "Post-RL compression via distillation"
49	    relevance: 7
50	    key_finding: "Compress post-RL model in one shot via structured distillation"
51	    our_relation: "Distillation-based vs our pruning+recovery approach; complementary"
52	    citation_priority: should-cite
53	    arxiv_id: ""
54	
55	  - id: doing_more_with_less_2026
56	    title: "Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling"
57	    authors: ""
58	    year: 2026
59	    venue: "arXiv Apr 2026"
60	    category: direct-competitor
61	    role: "Pruning improves test-time scaling"
62	    relevance: 7
63	    key_finding: "Unstructured pruning can augment test-time scaling; structured pruning degrades it"
64	    our_relation: "Motivates why structured pruning needs recovery; we address this gap with RLVR"
65	    citation_priority: should-cite
66	    arxiv_id: "2604.25098"
67	
68	  - id: gprune_llm_2026
69	    title: "GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models"
70	    authors: ""
71	    year: 2026
72	    venue: "arXiv Mar 2026"
73	    category: direct-competitor
74	    role: "Cross-distribution generalization-aware pruning"
75	    relevance: 6
76	    key_finding: "Accounts for neuron cross-distribution behavior; reduces calibration bias"
77	    our_relation: "Complementary importance metric; our CKA captures functional overlap vs their generalization gap"
78	    citation_priority: should-cite
79	    arxiv_id: "2603.13418"
80	
81	  - id: boiling_frog_2026
82	    title: "Gradually Compacting Large Language Models for Reasoning Like a Boiling Frog"
83	    authors: "Yiran Zhao, Shengyang Zhou, Zijian Wu, Tongyan Hu, Yuhui Xu, Rengan Dou, Kenji Kawaguchi, Shafiq Joty, Junnan Li, Michael Qizhe Shieh"
84	    year: 2026
85	    venue: "arXiv Feb 2026"
86	    category: direct-competitor
87	    role: "Iterative prune-tune loop for reasoning model compression"
88	    relevance: 7
89	    key_finding: "Gradual Prune-Tune Loop avoids abrupt performance collapse; iterative pruning+finetuning preserves reasoning"
90	    our_relation: "Similar prune-then-recover paradigm but uses SFT recovery; we use RLVR which is more effective and add CKA-guided pruning selection"
91	    citation_priority: must-cite
92	    arxiv_id: "2602.04919"
93	
94	  - id: think_prune_train_2025
95	    title: "Think, Prune, Train, Improve: Scaling Reasoning without Scaling Models"
96	    authors: "Caia Costello, Simon Guo, Anna Goldie, Azalia Mirhoseini"
97	    year: 2025
98	    venue: "arXiv Apr 2025 (Stanford Scaling Intelligence Lab)"
99	    category: direct-competitor
100	    role: "Self-training on pruned reasoning traces to improve small models"
101	    relevance: 6
102	    key_finding: "Iterative fine-tuning on ground-truth-pruned reasoning traces; Gemma2-9B matches LLaMA-3.1-70B on GSM8K"
103	    our_relation: "Complementary — prunes reasoning traces (CoT) not model weights; could combine with our weight pruning"
104	    citation_priority: nice-to-have
105	    arxiv_id: "2504.18116"
106	
107	  # === Method Components ===
108	  - id: mpruner_2024
109	    title: "MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning"
110	    authors: ""
111	    year: 2024
112	    venue: "arXiv Aug 2024"
113	    category: method-component
114	    role: "CKA for layer importance estimation"
115	    relevance: 8
116	    key_finding: "CKA similarity between layers identifies redundant layers for removal; 50% parameter reduction with minimal accuracy loss"
117	    our_relation: "We adapt CKA from layer-level to width-level functional overlap prediction"
118	    citation_priority: must-cite
119	    arxiv_id: "2408.13482"
120	
121	  - id: lachance_thesis_2024
122	    title: "Using Centered Kernel Alignment for Understanding and Pruning Neural Networks"
123	    authors: "Lachance"
124	    year: 2024
125	    venue: "URI Master's Thesis"
126	    category: method-component
127	    role: "CKA-based pruning theoretical foundation"
128	    relevance: 6
129	    key_finding: "CKA layer similarity correlates with pruning recoverability"
130	    our_relation: "Validates CKA as signal for pruning decisions; we extend to predict RLVR recovery"
131	    citation_priority: should-cite
132	    arxiv_id: ""
133	
134	  - id: fang_2025
135	    title: "FANG: Improving Generalization in LLM Structured Pruning via Function-Aware Neuron Grouping"
136	    authors: "Tao Yu, Yongqi An, Kuan Zhu, Guibo Zhu, Ming Tang, Jinqiao Wang"
137	    year: 2025
138	    venue: "arXiv Dec 2025"
139	    category: method-component
140	    role: "Function-aware neuron grouping for structured pruning"
141	    relevance: 7
142	    key_finding: "Groups FFN neurons by functional roles; shared neuron retention prevents cross-task accuracy loss; outperforms FLAP/OBC by 1.5-8.5% at 30-40% sparsity"
143	    our_relation: "Closest conceptual parallel — both identify functionally critical neurons, but FANG uses activation-based grouping while we use CKA similarity; no recovery component"
144	    citation_priority: must-cite
145	    arxiv_id: "2512.23014"
146	
147	  - id: funcnet_2025
148	    title: "Pruning Large Language Models by Identifying and Preserving Functional Networks"
149	    authors: "Yiheng Liu, Junhao Ning, Sichen Xia, Xiaohui Gao, Ning Qiang, Bao Ge, Junwei Han, Xintao Hu"
150	    year: 2025
151	    venue: "arXiv Aug 2025"
152	    category: method-component
153	    role: "ICA-based functional network identification for pruning"
154	    relevance: 7
155	    key_finding: "Applies ICA (from neuroimaging) to decompose LLM into functional networks; preserves key neurons within identified networks"
156	    our_relation: "Similar motivation — treat LLM as digital brain and preserve functional structure — but uses ICA vs our CKA; no RLVR recovery"
157	    citation_priority: must-cite
158	    arxiv_id: "2508.05239"
159	
160	  - id: bonsai_2025
161	    title: "Bonsai: Gradient-Free Structured Pruning for LLMs"
162	    authors: ""
163	    year: 2025
164	    venue: "ICML 2025"
165	    category: method-component
166	    role: "Gradient-free structured pruning alternative"
167	    relevance: 6
168	    key_finding: "Achieves competitive structured pruning without backprop"
169	    our_relation: "Alternative pruning strategy; our CKA metric is also gradient-free"
170	    citation_priority: should-cite
171	    arxiv_id: ""
172	
173	  - id: pat_2025
174	    title: "PAT: Pruning-Aware Tuning for Large Language Models"
175	    authors: "Yijiang Liu et al."
176	    year: 2025
177	    venue: "AAAI 2025"
178	    category: method-component
179	    role: "Joint pruning and tuning framework via Hybrid Sparsification Modules"
180	    relevance: 6
181	    key_finding: "Co-optimizing pruning mask and fine-tuning via HSMs; surpasses LoRA-64 by 1.26% at 25% pruning on Llama2-7B"
182	    our_relation: "Related idea of pruning-tuning interaction; we separate pruning and RLVR recovery"
183	    citation_priority: should-cite
184	    arxiv_id: "2408.14721"
185	
186	  - id: rac_2025
187	    title: "RAC: Chain-of-Thought Reconstruction for Pruned Reasoning Models"
188	    authors: ""
189	    year: 2025
190	    venue: "NeurIPS 2025"
191	    category: method-component
192	    role: "CoT reconstruction post-pruning"
193	    relevance: 7
194	    key_finding: "Reconstructing CoT improves unstructured/2:4 pruned reasoning models"
195	    our_relation: "Complementary recovery strategy; could combine with our RLVR approach"
196	    citation_priority: should-cite
197	    arxiv_id: ""
198	
199	  - id: paser_2025
200	    title: "PASER: Data Selection for Pruning Recovery"
201	    authors: ""
202	    year: 2025
203	    venue: "under review"
204	    category: method-component
205	    role: "Recovery training data selection"
206	    relevance: 6
207	    key_finding: "Selective data for recovery training improves efficiency"
208	    our_relation: "Orthogonal contribution; can apply PASER data selection to our RLVR recovery"
209	    citation_priority: nice-to-have
210	    arxiv_id: ""
211	
212	  - id: dppo_2026
213	    title: "DPPO: Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization"
214	    authors: ""
215	    year: 2026
216	    venue: "arXiv Mar 2026"
217	    category: method-component
218	    role: "Rollout pruning to accelerate GRPO training"
219	    relevance: 5
220	    key_finding: "Importance-sampling-based rollout pruning achieves 2.37x GRPO speedup with 3.36% accuracy gain on Qwen3-4B"
221	    our_relation: "Could accelerate our GRPO-based RLVR recovery phase"
222	    citation_priority: nice-to-have
223	    arxiv_id: "2603.04135"
224	
225	  - id: arrol_2026
226	    title: "ARRoL: Prune as You Generate — Online Rollout Pruning for Faster and Better RLVR"
227	    authors: ""
228	    year: 2026
229	    venue: "arXiv Mar 2026"
230	    category: method-component
231	    role: "Online rollout pruning for RLVR efficiency"
232	    relevance: 5
233	    key_finding: "Lightweight quality head predicts rollout success probability for early pruning during RLVR"
234	    our_relation: "Complementary technique for speeding up RLVR recovery training"
235	    citation_priority: nice-to-have
236	    arxiv_id: "2603.24840"
237	
238	  - id: restorelcc_2025
239	    title: "RestoreLCC: Restoring Pruned Large Language Models via Lost Component Compensation"
240	    authors: "Zijian Feng, Hanzhang Zhou, Zixiao Zhu, Tianjiao Li, Jia Jim Deryl Chua, Lee Onn Mak, Gee Wah Ng, Kezhi Mao"
241	    year: 2025
242	    venue: "NeurIPS 2025 (Spotlight, top 10%)"
243	    category: method-component
244	    role: "Plug-and-play pruning recovery via activation compensation"
245	    relevance: 6
246	    key_finding: "Contrastively probes critical attention heads, extracts lost components from activation differences, injects them back; +1.25-2.65% over SOTA baselines across structured/unstructured pruning"
247	    our_relation: "Alternative recovery paradigm (activation editing vs RLVR); could be complementary — apply RestoreLCC before RLVR for staged recovery"
248	    citation_priority: should-cite
249	    arxiv_id: "2510.21834"
250	
251	  - id: fastforward_2025
252	    title: "FastForward Pruning: Efficient LLM Pruning via Single-Step Reinforcement Learning"
253	    authors: ""
254	    year: 2025
255	    venue: "arXiv Nov 2025"
256	    category: method-component
257	    role: "RL-based non-uniform sparsity allocation for LLM pruning"
258	    relevance: 5
259	    key_finding: "Decoupled single-step RL framework separates policy optimization from budget satisfaction; efficient non-uniform layer-wise sparsity search"
260	    our_relation: "Uses RL for pruning decisions (not recovery); complementary — could combine their RL sparsity allocation with our CKA-guided selection"
261	    citation_priority: nice-to-have
262	    arxiv_id: "2511.18977"
263	
264	  - id: nirvana_2025
265	    title: "NIRVANA: Structured Pruning Reimagined for Large Language Models Compression"
266	    authors: "Mengting Ai, Tianxin Wei, Sirui Chen, Jingrui He"
267	    year: 2025
268	    venue: "arXiv Sep 2025"
269	    category: method-component
270	    role: "NTK-based saliency with adaptive sparsity allocation"
271	    relevance: 6
272	    key_finding: "First-order saliency from Neural Tangent Kernel under Adam dynamics; adaptive cross-module sparsity; KL-based calibration data selection. Outperforms SOTA on Llama3/Qwen/T5."
273	    our_relation: "Strong pruning baseline; their NTK saliency is complementary to our CKA functional overlap — could combine both signals"
274	    citation_priority: should-cite
275	    arxiv_id: "2509.14230"
276	
277	  - id: tracenas_2026
278	    title: "TraceNAS: Zero-shot LLM Pruning via Gradient Trace Correlation"
279	    authors: "Prajna G. Malettira, Manish Nagaraj, Arjun Roy, Shubham Negi, Kaushik Roy"
280	    year: 2026
281	    venue: "arXiv Feb 2026"
282	    category: method-component
283	    role: "Gradient trace for joint depth+width NAS-style pruning"
284	    relevance: 6
285	    key_finding: "Scale-invariant gradient trace correlation as proxy for pruned architecture quality; joint depth+width search on single GPU in 8.5h; competitive with training-intensive methods on Llama/Qwen"
286	    our_relation: "Related NAS-for-pruning approach; their gradient trace could complement our CKA as alternative architecture quality proxy"
287	    citation_priority: should-cite
288	    arxiv_id: "2602.02891"
289	
290	  - id: rlrc_2025
291	    title: "RLRC: Reinforcement Learning-based Recovery for Compressed Vision-Language-Action Models"
292	    authors: "Yuxuan Chen, Xiao Li"
293	    year: 2025
294	    venue: "arXiv Jun 2025"
295	    category: method-component
296	    role: "RL-based recovery for compressed VLA models (robotics)"
297	    relevance: 6
298	    key_finding: "Three-stage: structured pruning → SFT+RL recovery → quantization. 8x memory reduction, 2.3x throughput, maintains/surpasses original task success."
299	    our_relation: "Extends RL recovery paradigm to robotics VLAs; validates that RL recovery generalizes beyond language-only models. Parallel evidence for our RLVR recovery hypothesis."
300	    citation_priority: should-cite
301	    arxiv_id: "2506.17639"
302	
303	  # === Background / Theory ===
304	  - id: kornblith_cka_2019
305	    title: "Similarity of Neural Network Representations Revisited"
306	    authors: "Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton"
307	    year: 2019
308	    venue: "ICML 2019"
309	    category: background
310	    role: "CKA original paper — foundational method for our functional overlap metric"
311	    relevance: 9
312	    key_finding: "CKA achieves 99.3% accuracy in identifying corresponding layers across different initializations; CCA/SVCCA only 1.4-45.4%. Invariant to orthogonal transform and isotropic scaling."
313	    our_relation: "Foundational method — our CKA-guided pruning directly builds on this. Key justification: CKA >> CCA/SVCCA for reliable layer correspondence"
314	    citation_priority: must-cite
315	    arxiv_id: "1905.00414"
316	
317	  - id: davari_cka_reliability_2023
318	    title: "Reliability of CKA as a Similarity Measure in Deep Learning"
319	    authors: "MohammadReza Davari, Stefan Horoi, Amine Natik, Guillaume Lajoie, Guy Wolf, Eugene Belilovsky"
320	    year: 2023
321	    venue: "ICLR 2023"
322	    category: background
323	    role: "CKA limitations and failure modes — essential for honest CKA justification"
324	    relevance: 7
325	    key_finding: "CKA is sensitive to outliers and simple transformations preserving linear separability; CKA values can be manipulated without changing functional behavior. Calls for caution."
326	    our_relation: "Must-cite for CKA justification section. We should acknowledge limitations and explain why they don't invalidate our use case (intra-model layer comparison, not cross-model with different transformations)."
327	    citation_priority: must-cite
328	    arxiv_id: "2210.16156"
329	
330	  - id: murphy_debiased_cka_2024
331	    title: "Correcting Biased Centered Kernel Alignment Measures in Biological and Artificial Neural Networks"
332	    authors: "Alex Murphy, Joel Zylberberg, Alona Fyshe"
333	    year: 2024
334	    venue: "ICLR 2024 Re-Align Workshop"
335	    category: background
336	    role: "Debiased CKA for high-dimensionality settings"
337	    relevance: 5
338	    key_finding: "Biased CKA gives misleadingly high similarity when feature-sample ratio is skewed; debiased CKA corrects this. Shuffled data doesn't change biased CKA scores."
339	    our_relation: "Nice-to-have citation. Our setting (same model, same data) is less affected by this bias, but worth mentioning in limitations."
340	    citation_priority: nice-to-have
341	    arxiv_id: "2405.01012"
342	
343	  - id: raghu_svcca_2017
344	    title: "SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability"
345	    authors: "Maithra Raghu, Justin Gilmer, Jason Yosinski, Jascha Sohl-Dickstein"
346	    year: 2017
347	    venue: "NeurIPS 2017"
348	    category: background
349	    role: "SVCCA — predecessor to CKA, baseline representation similarity method"
350	    relevance: 5
351	    key_finding: "SVD dimensionality reduction + CCA for comparing representations; reveals bottom-up convergence dynamics and intrinsic dimensionality"
352	    our_relation: "CKA alternative baseline. SVCCA lacks invariance to isotropic scaling and fails at cross-network layer identification (only 45% accuracy vs CKA's 99%)"
353	    citation_priority: should-cite
354	    arxiv_id: "1706.05806"
355	
356	  - id: klabunde_similarity_survey_2025
357	    title: "Similarity of Neural Network Models: A Survey of Functional and Representational Measures"
358	    authors: "Max Klabunde, Tobias Schumacher, Markus Strohmaier, Florian Lemmerich"
359	    year: 2025
360	    venue: "ACM Computing Surveys, Vol. 57, Issue 9"
361	    category: background
362	    role: "Comprehensive survey of representation similarity measures including CKA, CCA, SVCCA, PWCCA"
363	    relevance: 7
364	    key_finding: "First comprehensive review comparing representational vs functional similarity; covers CKA properties, robustness, and practical applications including pruning"
365	    our_relation: "Key citation for CKA justification — survey confirms CKA's advantages over alternatives for model analysis and compression"
366	    citation_priority: must-cite
367	    arxiv_id: "2305.06329"
368	
369	  - id: mipp_2024
370	    title: "MIPP: Mutual Information Preserving Neural Network Pruning"
371	    authors: ""
372	    year: 2024
373	    venue: "arXiv Nov 2024"
374	    category: background
375	    role: "Information-theoretic pruning criterion — MI alternative to CKA"
376	    relevance: 5
377	    key_finding: "Structured activation-based pruning conserving MI between adjacent layers; sample efficiency proportional to MI between masks and data"
378	    our_relation: "MI is a viable alternative but computationally expensive in high dimensions and less stable than CKA. Supports functional similarity matters for pruning."
379	    citation_priority: nice-to-have
380	    arxiv_id: "2411.00147"
381	
382	  - id: rl_squeezes_2026
383	    title: "RL Squeezes, SFT Expands: Different Mechanisms in Post-Training"
384	    authors: ""
385	    year: 2026
386	    venue: "ICLR 2026 Poster"
387	    category: background
388	    role: "Theoretical basis for why RLVR works differently from SFT"
389	    relevance: 8
390	    key_finding: "RLVR compresses representation while SFT expands; different inductive biases"
391	    our_relation: "Explains why RLVR recovery succeeds where SFT fails post-pruning"
392	    citation_priority: must-cite
393	    arxiv_id: ""
394	
395	  - id: from_llms_to_lrms_2026
396	    title: "From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models"
397	    authors: "Longwei Ding, Anhao Zhao, Fanghua Ye, Ziyang Chen, Xiaoyu Shen"
398	    year: 2026
399	    venue: "arXiv Jan 2026"
400	    category: background
401	    role: "Width vs depth pruning for reasoning models"
402	    relevance: 7
403	    key_finding: "Width pruning preserves reasoning better than depth pruning; static pruning > dynamic for long-chain reasoning; recovery relies on distribution-aligned post-fine-tuning, not calibration data."
404	    our_relation: "Motivates our focus on width-level structured pruning; validates that reasoning models need specialized pruning strategies"
405	    citation_priority: must-cite
406	    arxiv_id: "2601.18091"
407	
408	  - id: p2_law_2025
409	    title: "P2 Law: Scaling Law for Pruning Recovery Training"
410	    authors: ""
411	    year: 2025
412	    venue: "ACL 2025"
413	    category: background
414	    role: "Theoretical scaling of recovery compute"
415	    relevance: 7
416	    key_finding: "Recovery training follows predictable scaling with compute and data"
417	    our_relation: "Informs our recovery budget estimation; we extend to RLVR-specific scaling"
418	    citation_priority: should-cite
419	    arxiv_id: ""
420	
421	  - id: free_lunch_retraining_2025
422	    title: "A Free Lunch in LLM Compression: Revisiting Retraining after Pruning"
423	    authors: "Moritz Wagner, Christophe Roux, Max Zimmer, Sebastian Pokutta"
424	    year: 2025
425	    venue: "arXiv Oct 2025 (revised Feb 2026)"
426	    category: background
427	    role: "Local reconstruction as efficient post-pruning recovery"
428	    relevance: 6
429	    key_finding: "Local reconstruction matches sophisticated PEFT recovery with >10x less data/compute. Pruning method matters less as model size grows."
430	    our_relation: "Shows cheap recovery can work — but their SFT-based reconstruction has ceiling; our RLVR recovery pushes beyond that ceiling for reasoning tasks."
431	    citation_priority: should-cite
432	    arxiv_id: "2510.14444"
433	
434	  - id: grasp_2020
435	    title: "Picking Winning Tickets Before Training by Preserving Gradient Flow"
436	    authors: "Chaoqi Wang, Guodong Zhang, Roger Grosse"
437	    year: 2020
438	    venue: "ICLR 2020"
439	    category: background
440	    role: "GraSP — gradient signal preservation for pruning at initialization"
441	    relevance: 5
442	    key_finding: "Hessian-gradient product preserves gradient flow post-pruning; 80% VGG-16 pruning with only 1.6% top-1 drop on ImageNet; outperforms SNIP by 4-6% at high sparsity."
443	    our_relation: "Classic baseline for gradient-based importance. GRASPrune extends this idea to LLMs; our CKA operates at functional level rather than gradient flow."
444	    citation_priority: should-cite
445	    arxiv_id: "2002.07376"
446	
447	  - id: fnf_2026
448	    title: "FNF: Functional Network Fingerprint for Large Language Models"
449	    authors: ""
450	    year: 2026
451	    venue: "arXiv Jan 2026"
452	    category: background
453	    role: "Functional network concept applied to LLM identification"
454	    relevance: 4
455	    key_finding: "Co-activating neuron groups form consistent functional networks; robust to model obfuscation."
456	    our_relation: "Validates the 'functional network' framing we share with FANG/FuncNet; extends concept to model fingerprinting."
457	    citation_priority: nice-to-have
458	    arxiv_id: "2601.22692"
459	
460	  - id: redundancy_aware_cnn_2020
461	    title: "Redundancy-Aware Pruning of Convolutional Neural Networks"
462	    authors: ""
463	    year: 2020
464	    venue: "Neural Computation"
465	    category: background
466	    role: "Pioneer of redundancy-based pruning"
467	    relevance: 4
468	    key_finding: "Redundancy metrics guide pruning decisions in CNNs"
469	    our_relation: "Conceptual ancestor; we apply redundancy-awareness to LLM structured pruning"
470	    citation_priority: nice-to-have
471	    arxiv_id: ""
472	
473	  - id: self_distilled_rlvr_2026
474	    title: "Self-Distilled RLVR"
475	    authors: ""
476	    year: 2026
477	    venue: "arXiv Apr 2026"
478	    category: background
479	    role: "RLVR training efficiency improvement"
480	    relevance: 5
481	    key_finding: "Self-distillation stabilizes RLVR training and improves sample efficiency"
482	    our_relation: "Could improve our RLVR recovery phase efficiency"
483	    citation_priority: nice-to-have
484	    arxiv_id: "2604.03128"
485	
486	  - id: diet_2026
487	    title: "DieT: Dimension-wise Global Pruning via Task-specific Importance Score"
488	    authors: ""
489	    year: 2026
490	    venue: "arXiv Mar 2026"
491	    category: background
492	    role: "Dimension-wise importance for width pruning"
493	    relevance: 5
494	    key_finding: "Task-specific dimension importance outperforms activation-based metrics at 20-40% sparsity"
495	    our_relation: "Alternative width importance metric; we use CKA overlap instead"
496	    citation_priority: nice-to-have
497	    arxiv_id: "2603.23985"
498	
499	  - id: task_neurons_2026
500	    title: "Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific LLMs"
501	    authors: ""
502	    year: 2026
503	    venue: "arXiv Apr 2026"
504	    category: background
505	    role: "Task-specific neuron identification and pruning recovery dynamics"
506	    relevance: 6
507	    key_finding: "10% task-specific neuron removal causes collapse; 15-20% robustness threshold; fine-tuning substantially recovers"
508	    our_relation: "Supports need for recovery-aware pruning; our CKA predicts which neurons are functionally critical"
509	    citation_priority: should-cite
510	    arxiv_id: "2604.27115"
511	
512	  - id: ddp_2026
513	    title: "DDP: Deterministic Differentiable Structured Pruning for Large Language Models"
514	    authors: ""
515	    year: 2026
516	    venue: "arXiv Mar 2026"
517	    category: background
518	    role: "Differentiable mask-only structured pruning"
519	    relevance: 5
520	    key_finding: "Deterministic soft surrogate of l0 constraint eliminates train-test mismatch in differentiable pruning"
521	    our_relation: "Alternative pruning backbone; mask-only optimization complementary to our CKA-guided selection"
522	    citation_priority: nice-to-have
523	    arxiv_id: "2603.08065"
524	
525	  - id: pruning_vlm_recovery_2026
526	    title: "Structural Pruning of Large Vision Language Models: Pruning Dynamics, Recovery, and Data Efficiency"
527	    authors: "Yiran Huang, Lukas Thede, Massimiliano Mancini, Wenjia Xu, Zeynep Akata"
528	    year: 2026
529	    venue: "arXiv Apr 2026"
530	    category: background
531	    role: "Comprehensive pruning + recovery study for VLMs"
532	    relevance: 5
533	    key_finding: "Width pruning + KD recovery outperforms layer pruning + SFT on VLMs; 5% data recovers 95% performance; SFT+hidden-state distillation is optimal."
534	    our_relation: "Validates width pruning + recovery paradigm; our CKA-guided approach adds prediction of recoverability"
535	    citation_priority: nice-to-have
536	    arxiv_id: "2604.24380"
537	
538	  - id: hape_2026
539	    title: "HAP-E: Hessian-Aware Structured Pruning of LLMs for Efficient Inference"
540	    authors: ""
541	    year: 2026
542	    venue: "ICLR 2026 (submitted)"
543	    category: background
544	    role: "Hessian-aware structured pruning with adaptive budget allocation"
545	    relevance: 5
546	    key_finding: "Adaptive cross-layer budget reallocation via global screening + OBS-equivalent batch pruning; up to 3% accuracy over SOTA structured pruning"
547	    our_relation: "Alternative pruning backbone with second-order optimization; complementary to our CKA-guided selection"
548	    citation_priority: nice-to-have
549	    arxiv_id: ""
550	
551	  - id: slimllm_2025
552	    title: "SlimLLM: Accurate Structured Pruning for Large Language Models"
553	    authors: "Jialong Guo, Xinghao Chen, Yehui Tang, Yunhe Wang"
554	    year: 2025
555	    venue: "ICML 2025"
556	    category: background
557	    role: "Holistic channel/head importance evaluation with linear regression recovery"
558	    relevance: 5
559	    key_finding: "Evaluates importance of entire channels/heads holistically; non-uniform layer-based pruning ratio via cosine similarity; linear regression for fast recovery"
560	    our_relation: "Alternative structured pruning metric; their cosine-based layer ratio is complementary to our CKA functional overlap"
561	    citation_priority: nice-to-have
562	    arxiv_id: "2505.22689"
563	
564	  - id: spap_2025
565	    title: "SPAP: Structured Pruning via Alternating Optimization and Penalty Methods"
566	    authors: ""
567	    year: 2025
568	    venue: "arXiv May 2025"
569	    category: background
570	    role: "Optimization-theory-grounded MLP pruning"
571	    relevance: 5
572	    key_finding: "Mixed-integer formulation with relaxation guarantee; alternating minimization with closed-form updates; 1.29x speedup at 30% sparsity"
573	    our_relation: "Could serve as alternative pruning backbone for MLP layers; operates at different abstraction level from our CKA selection"
574	    citation_priority: nice-to-have
575	    arxiv_id: "2505.03373"
576	
577	  - id: wandapp_2025
578	    title: "Wanda++: Pruning Large Language Models via Regional Gradients"
579	    authors: ""
580	    year: 2025
581	    venue: "ACL 2025"
582	    category: background
583	    role: "Gradient-enhanced unstructured pruning"
584	    relevance: 4
585	    key_finding: "Regional gradients improve Wanda score by up to 32% perplexity reduction; regional optimization minimizes dense-sparse output discrepancy"
586	    our_relation: "Unstructured pruning evolution; orthogonal to our structured approach but regional optimization idea could inform per-block CKA computation"
587	    citation_priority: nice-to-have
588	    arxiv_id: "2503.04992"
589	
590	  # === Must-cite gap fills (Step 3, 2026-05-18) ===
591	  - id: llm_pruner_2023
592	    title: "LLM-Pruner: On the Structural Pruning of Large Language Models"
593	    authors: "Xinyin Ma, Gongfan Fang, Xinchao Wang"
594	    year: 2023
595	    venue: "NeurIPS 2023"
596	    category: method-component
597	    role: "Foundational structured pruning framework for LLMs using Taylor importance + dependency detection"
598	    relevance: 9
599	    key_finding: "First task-agnostic structured pruning for LLMs; dependency-aware group removal preserves model integrity; 20% pruning with minimal loss after LoRA recovery on LLaMA-7B/13B/30B"
600	    our_relation: "Foundational baseline; our Taylor importance scoring (Standard method) directly builds on LLM-Pruner. We extend with CKA overlap and RLVR recovery"
601	    citation_priority: must-cite
602	    arxiv_id: "2305.11627"
603	    verified: true
604	
605	  - id: deepseekmath_grpo_2024
606	    title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
607	    authors: "Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo"
608	    year: 2024
609	    venue: "arXiv Feb 2024"
610	    category: background
611	    role: "GRPO algorithm origin — Group Relative Policy Optimization for math reasoning"
612	    relevance: 9
613	    key_finding: "Introduces GRPO: group-level reward normalization without critic model; DeepSeekMath-7B achieves 51.7% on MATH competition via GRPO + code-math corpus"
614	    our_relation: "Our RLVR recovery phase uses GRPO as the alignment algorithm; this is the foundational reference"
615	    citation_priority: must-cite
616	    arxiv_id: "2402.03300"
617	    verified: true
618	
619	# === Update Log ===
620	# 2026-05-15: Literature survey targeting 4 reviewer-flagged gaps
621	#   Direction 1 (Structured pruning + RLVR recovery): Added RLRC, NIRVANA, free_lunch_retraining
622	#   Direction 2 (CKA in pruning/NAS): Added davari_cka_reliability (must-cite), murphy_debiased_cka, tracenas
623	#   Direction 3 (FANG/FuncNet): Confirmed details; added FNF as background
624	#   Direction 4 (GraSP baselines): Added grasp_2020 (original), tracenas
625	#   Updated: self_healing authors (Ji et al., ICLR 2026), from_llms_to_lrms (Ding et al., 2601.18091),
626	#            mpruner (arxiv 2408.13482), slimllm authors, pruning_vlm_recovery authors
627	#   Added citation_priority field (must-cite / should-cite / nice-to-have) to all entries
628	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "cf07dc8d-0a3c-4d29-8832-194fa3d8139e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml",
      "content": "papers:\n  # === Direct Competitors ===\n  - id: self_healing_2025\n    title: \"Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning\"\n    authors: \"Yixin Ji, Zhimin Lin, Juntao Li, Kaixin Wu, Kai Yao, Xu Jia, Linjian Mo, Min Zhang\"\n    year: 2025\n    venue: \"ICLR 2026 submission (OpenReview #12375, submitted Sep 2025)\"\n    category: direct-competitor\n    role: \"RLVR recovery baseline\"\n    relevance: 9\n    key_finding: \"RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%. Tested on 5 LRMs across 6 math benchmarks.\"\n    our_relation: \"We extend beyond single sparsity ratio and add CKA-guided pruning selection\"\n    citation_priority: must-cite\n    arxiv_id: \"\"\n\n  - id: resp_2025\n    title: \"RESP: Self-Reflective Structured Pruning for Reasoning LLMs\"\n    authors: \"\"\n    year: 2025\n    venue: \"arXiv Dec 2025\"\n    category: direct-competitor\n    role: \"Structured pruning for reasoning without recovery\"\n    relevance: 8\n    key_finding: \"GSM8K 81.3% at 40% sparsity via self-reflective importance\"\n    our_relation: \"No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity\"\n    citation_priority: must-cite\n    arxiv_id: \"2512.02185\"\n\n  - id: grasprune_2026\n    title: \"GRASPrune: Global Gating-based Structural Pruning for LLMs\"\n    authors: \"\"\n    year: 2026\n    venue: \"ACL 2026 Main\"\n    category: direct-competitor\n    role: \"SOTA budgeted structural pruning\"\n    relevance: 8\n    key_finding: \"Global gating achieves best structured pruning under budget constraints\"\n    our_relation: \"GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top\"\n    citation_priority: must-cite\n    arxiv_id: \"2604.19398\"\n\n  - id: opsd_2026\n    title: \"OPSD: One-shot Post-RL Structured Distillation\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv May 2026\"\n    category: direct-competitor\n    role: \"Post-RL compression via distillation\"\n    relevance: 7\n    key_finding: \"Compress post-RL model in one shot via structured distillation\"\n    our_relation: \"Distillation-based vs our pruning+recovery approach; complementary\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: doing_more_with_less_2026\n    title: \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: direct-competitor\n    role: \"Pruning improves test-time scaling\"\n    relevance: 7\n    key_finding: \"Unstructured pruning can augment test-time scaling; structured pruning degrades it\"\n    our_relation: \"Motivates why structured pruning needs recovery; we address this gap with RLVR\"\n    citation_priority: should-cite\n    arxiv_id: \"2604.25098\"\n\n  - id: gprune_llm_2026\n    title: \"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: direct-competitor\n    role: \"Cross-distribution generalization-aware pruning\"\n    relevance: 6\n    key_finding: \"Accounts for neuron cross-distribution behavior; reduces calibration bias\"\n    our_relation: \"Complementary importance metric; our CKA captures functional overlap vs their generalization gap\"\n    citation_priority: should-cite\n    arxiv_id: \"2603.13418\"\n\n  - id: boiling_frog_2026\n    title: \"Gradually Compacting Large Language Models for Reasoning Like a Boiling Frog\"\n    authors: \"Yiran Zhao, Shengyang Zhou, Zijian Wu, Tongyan Hu, Yuhui Xu, Rengan Dou, Kenji Kawaguchi, Shafiq Joty, Junnan Li, Michael Qizhe Shieh\"\n    year: 2026\n    venue: \"arXiv Feb 2026\"\n    category: direct-competitor\n    role: \"Iterative prune-tune loop for reasoning model compression\"\n    relevance: 7\n    key_finding: \"Gradual Prune-Tune Loop avoids abrupt performance collapse; iterative pruning+finetuning preserves reasoning\"\n    our_relation: \"Similar prune-then-recover paradigm but uses SFT recovery; we use RLVR which is more effective and add CKA-guided pruning selection\"\n    citation_priority: must-cite\n    arxiv_id: \"2602.04919\"\n\n  - id: think_prune_train_2025\n    title: \"Think, Prune, Train, Improve: Scaling Reasoning without Scaling Models\"\n    authors: \"Caia Costello, Simon Guo, Anna Goldie, Azalia Mirhoseini\"\n    year: 2025\n    venue: \"arXiv Apr 2025 (Stanford Scaling Intelligence Lab)\"\n    category: direct-competitor\n    role: \"Self-training on pruned reasoning traces to improve small models\"\n    relevance: 6\n    key_finding: \"Iterative fine-tuning on ground-truth-pruned reasoning traces; Gemma2-9B matches LLaMA-3.1-70B on GSM8K\"\n    our_relation: \"Complementary — prunes reasoning traces (CoT) not model weights; could combine with our weight pruning\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2504.18116\"\n\n  # === Method Components ===\n  - id: mpruner_2024\n    title: \"MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning\"\n    authors: \"\"\n    year: 2024\n    venue: \"arXiv Aug 2024\"\n    category: method-component\n    role: \"CKA for layer importance estimation\"\n    relevance: 8\n    key_finding: \"CKA similarity between layers identifies redundant layers for removal; 50% parameter reduction with minimal accuracy loss\"\n    our_relation: \"We adapt CKA from layer-level to width-level functional overlap prediction\"\n    citation_priority: must-cite\n    arxiv_id: \"2408.13482\"\n\n  - id: lachance_thesis_2024\n    title: \"Using Centered Kernel Alignment for Understanding and Pruning Neural Networks\"\n    authors: \"Lachance\"\n    year: 2024\n    venue: \"URI Master's Thesis\"\n    category: method-component\n    role: \"CKA-based pruning theoretical foundation\"\n    relevance: 6\n    key_finding: \"CKA layer similarity correlates with pruning recoverability\"\n    our_relation: \"Validates CKA as signal for pruning decisions; we extend to predict RLVR recovery\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: fang_2025\n    title: \"FANG: Improving Generalization in LLM Structured Pruning via Function-Aware Neuron Grouping\"\n    authors: \"Tao Yu, Yongqi An, Kuan Zhu, Guibo Zhu, Ming Tang, Jinqiao Wang\"\n    year: 2025\n    venue: \"arXiv Dec 2025\"\n    category: method-component\n    role: \"Function-aware neuron grouping for structured pruning\"\n    relevance: 7\n    key_finding: \"Groups FFN neurons by functional roles; shared neuron retention prevents cross-task accuracy loss; outperforms FLAP/OBC by 1.5-8.5% at 30-40% sparsity\"\n    our_relation: \"Closest conceptual parallel — both identify functionally critical neurons, but FANG uses activation-based grouping while we use CKA similarity; no recovery component\"\n    citation_priority: must-cite\n    arxiv_id: \"2512.23014\"\n\n  - id: funcnet_2025\n    title: \"Pruning Large Language Models by Identifying and Preserving Functional Networks\"\n    authors: \"Yiheng Liu, Junhao Ning, Sichen Xia, Xiaohui Gao, Ning Qiang, Bao Ge, Junwei Han, Xintao Hu\"\n    year: 2025\n    venue: \"arXiv Aug 2025\"\n    category: method-component\n    role: \"ICA-based functional network identification for pruning\"\n    relevance: 7\n    key_finding: \"Applies ICA (from neuroimaging) to decompose LLM into functional networks; preserves key neurons within identified networks\"\n    our_relation: \"Similar motivation — treat LLM as digital brain and preserve functional structure — but uses ICA vs our CKA; no RLVR recovery\"\n    citation_priority: must-cite\n    arxiv_id: \"2508.05239\"\n\n  - id: bonsai_2025\n    title: \"Bonsai: Gradient-Free Structured Pruning for LLMs\"\n    authors: \"\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: method-component\n    role: \"Gradient-free structured pruning alternative\"\n    relevance: 6\n    key_finding: \"Achieves competitive structured pruning without backprop\"\n    our_relation: \"Alternative pruning strategy; our CKA metric is also gradient-free\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: pat_2025\n    title: \"PAT: Pruning-Aware Tuning for Large Language Models\"\n    authors: \"Yijiang Liu et al.\"\n    year: 2025\n    venue: \"AAAI 2025\"\n    category: method-component\n    role: \"Joint pruning and tuning framework via Hybrid Sparsification Modules\"\n    relevance: 6\n    key_finding: \"Co-optimizing pruning mask and fine-tuning via HSMs; surpasses LoRA-64 by 1.26% at 25% pruning on Llama2-7B\"\n    our_relation: \"Related idea of pruning-tuning interaction; we separate pruning and RLVR recovery\"\n    citation_priority: should-cite\n    arxiv_id: \"2408.14721\"\n\n  - id: rac_2025\n    title: \"RAC: Chain-of-Thought Reconstruction for Pruned Reasoning Models\"\n    authors: \"\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    category: method-component\n    role: \"CoT reconstruction post-pruning\"\n    relevance: 7\n    key_finding: \"Reconstructing CoT improves unstructured/2:4 pruned reasoning models\"\n    our_relation: \"Complementary recovery strategy; could combine with our RLVR approach\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: paser_2025\n    title: \"PASER: Data Selection for Pruning Recovery\"\n    authors: \"\"\n    year: 2025\n    venue: \"under review\"\n    category: method-component\n    role: \"Recovery training data selection\"\n    relevance: 6\n    key_finding: \"Selective data for recovery training improves efficiency\"\n    our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"\n    citation_priority: nice-to-have\n    arxiv_id: \"\"\n\n  - id: dppo_2026\n    title: \"DPPO: Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Rollout pruning to accelerate GRPO training\"\n    relevance: 5\n    key_finding: \"Importance-sampling-based rollout pruning achieves 2.37x GRPO speedup with 3.36% accuracy gain on Qwen3-4B\"\n    our_relation: \"Could accelerate our GRPO-based RLVR recovery phase\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2603.04135\"\n\n  - id: arrol_2026\n    title: \"ARRoL: Prune as You Generate — Online Rollout Pruning for Faster and Better RLVR\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Online rollout pruning for RLVR efficiency\"\n    relevance: 5\n    key_finding: \"Lightweight quality head predicts rollout success probability for early pruning during RLVR\"\n    our_relation: \"Complementary technique for speeding up RLVR recovery training\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2603.24840\"\n\n  - id: restorelcc_2025\n    title: \"RestoreLCC: Restoring Pruned Large Language Models via Lost Component Compensation\"\n    authors: \"Zijian Feng, Hanzhang Zhou, Zixiao Zhu, Tianjiao Li, Jia Jim Deryl Chua, Lee Onn Mak, Gee Wah Ng, Kezhi Mao\"\n    year: 2025\n    venue: \"NeurIPS 2025 (Spotlight, top 10%)\"\n    category: method-component\n    role: \"Plug-and-play pruning recovery via activation compensation\"\n    relevance: 6\n    key_finding: \"Contrastively probes critical attention heads, extracts lost components from activation differences, injects them back; +1.25-2.65% over SOTA baselines across structured/unstructured pruning\"\n    our_relation: \"Alternative recovery paradigm (activation editing vs RLVR); could be complementary — apply RestoreLCC before RLVR for staged recovery\"\n    citation_priority: should-cite\n    arxiv_id: \"2510.21834\"\n\n  - id: fastforward_2025\n    title: \"FastForward Pruning: Efficient LLM Pruning via Single-Step Reinforcement Learning\"\n    authors: \"\"\n    year: 2025\n    venue: \"arXiv Nov 2025\"\n    category: method-component\n    role: \"RL-based non-uniform sparsity allocation for LLM pruning\"\n    relevance: 5\n    key_finding: \"Decoupled single-step RL framework separates policy optimization from budget satisfaction; efficient non-uniform layer-wise sparsity search\"\n    our_relation: \"Uses RL for pruning decisions (not recovery); complementary — could combine their RL sparsity allocation with our CKA-guided selection\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2511.18977\"\n\n  - id: nirvana_2025\n    title: \"NIRVANA: Structured Pruning Reimagined for Large Language Models Compression\"\n    authors: \"Mengting Ai, Tianxin Wei, Sirui Chen, Jingrui He\"\n    year: 2025\n    venue: \"arXiv Sep 2025\"\n    category: method-component\n    role: \"NTK-based saliency with adaptive sparsity allocation\"\n    relevance: 6\n    key_finding: \"First-order saliency from Neural Tangent Kernel under Adam dynamics; adaptive cross-module sparsity; KL-based calibration data selection. Outperforms SOTA on Llama3/Qwen/T5.\"\n    our_relation: \"Strong pruning baseline; their NTK saliency is complementary to our CKA functional overlap — could combine both signals\"\n    citation_priority: should-cite\n    arxiv_id: \"2509.14230\"\n\n  - id: tracenas_2026\n    title: \"TraceNAS: Zero-shot LLM Pruning via Gradient Trace Correlation\"\n    authors: \"Prajna G. Malettira, Manish Nagaraj, Arjun Roy, Shubham Negi, Kaushik Roy\"\n    year: 2026\n    venue: \"arXiv Feb 2026\"\n    category: method-component\n    role: \"Gradient trace for joint depth+width NAS-style pruning\"\n    relevance: 6\n    key_finding: \"Scale-invariant gradient trace correlation as proxy for pruned architecture quality; joint depth+width search on single GPU in 8.5h; competitive with training-intensive methods on Llama/Qwen\"\n    our_relation: \"Related NAS-for-pruning approach; their gradient trace could complement our CKA as alternative architecture quality proxy\"\n    citation_priority: should-cite\n    arxiv_id: \"2602.02891\"\n\n  - id: rlrc_2025\n    title: \"RLRC: Reinforcement Learning-based Recovery for Compressed Vision-Language-Action Models\"\n    authors: \"Yuxuan Chen, Xiao Li\"\n    year: 2025\n    venue: \"arXiv Jun 2025\"\n    category: method-component\n    role: \"RL-based recovery for compressed VLA models (robotics)\"\n    relevance: 6\n    key_finding: \"Three-stage: structured pruning → SFT+RL recovery → quantization. 8x memory reduction, 2.3x throughput, maintains/surpasses original task success.\"\n    our_relation: \"Extends RL recovery paradigm to robotics VLAs; validates that RL recovery generalizes beyond language-only models. Parallel evidence for our RLVR recovery hypothesis.\"\n    citation_priority: should-cite\n    arxiv_id: \"2506.17639\"\n\n  # === Background / Theory ===\n  - id: kornblith_cka_2019\n    title: \"Similarity of Neural Network Representations Revisited\"\n    authors: \"Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton\"\n    year: 2019\n    venue: \"ICML 2019\"\n    category: background\n    role: \"CKA original paper — foundational method for our functional overlap metric\"\n    relevance: 9\n    key_finding: \"CKA achieves 99.3% accuracy in identifying corresponding layers across different initializations; CCA/SVCCA only 1.4-45.4%. Invariant to orthogonal transform and isotropic scaling.\"\n    our_relation: \"Foundational method — our CKA-guided pruning directly builds on this. Key justification: CKA >> CCA/SVCCA for reliable layer correspondence\"\n    citation_priority: must-cite\n    arxiv_id: \"1905.00414\"\n\n  - id: davari_cka_reliability_2023\n    title: \"Reliability of CKA as a Similarity Measure in Deep Learning\"\n    authors: \"MohammadReza Davari, Stefan Horoi, Amine Natik, Guillaume Lajoie, Guy Wolf, Eugene Belilovsky\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    category: background\n    role: \"CKA limitations and failure modes — essential for honest CKA justification\"\n    relevance: 7\n    key_finding: \"CKA is sensitive to outliers and simple transformations preserving linear separability; CKA values can be manipulated without changing functional behavior. Calls for caution.\"\n    our_relation: \"Must-cite for CKA justification section. We should acknowledge limitations and explain why they don't invalidate our use case (intra-model layer comparison, not cross-model with different transformations).\"\n    citation_priority: must-cite\n    arxiv_id: \"2210.16156\"\n\n  - id: murphy_debiased_cka_2024\n    title: \"Correcting Biased Centered Kernel Alignment Measures in Biological and Artificial Neural Networks\"\n    authors: \"Alex Murphy, Joel Zylberberg, Alona Fyshe\"\n    year: 2024\n    venue: \"ICLR 2024 Re-Align Workshop\"\n    category: background\n    role: \"Debiased CKA for high-dimensionality settings\"\n    relevance: 5\n    key_finding: \"Biased CKA gives misleadingly high similarity when feature-sample ratio is skewed; debiased CKA corrects this. Shuffled data doesn't change biased CKA scores.\"\n    our_relation: \"Nice-to-have citation. Our setting (same model, same data) is less affected by this bias, but worth mentioning in limitations.\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2405.01012\"\n\n  - id: raghu_svcca_2017\n    title: \"SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability\"\n    authors: \"Maithra Raghu, Justin Gilmer, Jason Yosinski, Jascha Sohl-Dickstein\"\n    year: 2017\n    venue: \"NeurIPS 2017\"\n    category: background\n    role: \"SVCCA — predecessor to CKA, baseline representation similarity method\"\n    relevance: 5\n    key_finding: \"SVD dimensionality reduction + CCA for comparing representations; reveals bottom-up convergence dynamics and intrinsic dimensionality\"\n    our_relation: \"CKA alternative baseline. SVCCA lacks invariance to isotropic scaling and fails at cross-network layer identification (only 45% accuracy vs CKA's 99%)\"\n    citation_priority: should-cite\n    arxiv_id: \"1706.05806\"\n\n  - id: klabunde_similarity_survey_2025\n    title: \"Similarity of Neural Network Models: A Survey of Functional and Representational Measures\"\n    authors: \"Max Klabunde, Tobias Schumacher, Markus Strohmaier, Florian Lemmerich\"\n    year: 2025\n    venue: \"ACM Computing Surveys, Vol. 57, Issue 9\"\n    category: background\n    role: \"Comprehensive survey of representation similarity measures including CKA, CCA, SVCCA, PWCCA\"\n    relevance: 7\n    key_finding: \"First comprehensive review comparing representational vs functional similarity; covers CKA properties, robustness, and practical applications including pruning\"\n    our_relation: \"Key citation for CKA justification — survey confirms CKA's advantages over alternatives for model analysis and compression\"\n    citation_priority: must-cite\n    arxiv_id: \"2305.06329\"\n\n  - id: mipp_2024\n    title: \"MIPP: Mutual Information Preserving Neural Network Pruning\"\n    authors: \"\"\n    year: 2024\n    venue: \"arXiv Nov 2024\"\n    category: background\n    role: \"Information-theoretic pruning criterion — MI alternative to CKA\"\n    relevance: 5\n    key_finding: \"Structured activation-based pruning conserving MI between adjacent layers; sample efficiency proportional to MI between masks and data\"\n    our_relation: \"MI is a viable alternative but computationally expensive in high dimensions and less stable than CKA. Supports functional similarity matters for pruning.\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2411.00147\"\n\n  - id: rl_squeezes_2026\n    title: \"RL Squeezes, SFT Expands: Different Mechanisms in Post-Training\"\n    authors: \"\"\n    year: 2026\n    venue: \"ICLR 2026 Poster\"\n    category: background\n    role: \"Theoretical basis for why RLVR works differently from SFT\"\n    relevance: 8\n    key_finding: \"RLVR compresses representation while SFT expands; different inductive biases\"\n    our_relation: \"Explains why RLVR recovery succeeds where SFT fails post-pruning\"\n    citation_priority: must-cite\n    arxiv_id: \"\"\n\n  - id: from_llms_to_lrms_2026\n    title: \"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models\"\n    authors: \"Longwei Ding, Anhao Zhao, Fanghua Ye, Ziyang Chen, Xiaoyu Shen\"\n    year: 2026\n    venue: \"arXiv Jan 2026\"\n    category: background\n    role: \"Width vs depth pruning for reasoning models\"\n    relevance: 7\n    key_finding: \"Width pruning preserves reasoning better than depth pruning; static pruning > dynamic for long-chain reasoning; recovery relies on distribution-aligned post-fine-tuning, not calibration data.\"\n    our_relation: \"Motivates our focus on width-level structured pruning; validates that reasoning models need specialized pruning strategies\"\n    citation_priority: must-cite\n    arxiv_id: \"2601.18091\"\n\n  - id: p2_law_2025\n    title: \"P2 Law: Scaling Law for Pruning Recovery Training\"\n    authors: \"\"\n    year: 2025\n    venue: \"ACL 2025\"\n    category: background\n    role: \"Theoretical scaling of recovery compute\"\n    relevance: 7\n    key_finding: \"Recovery training follows predictable scaling with compute and data\"\n    our_relation: \"Informs our recovery budget estimation; we extend to RLVR-specific scaling\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: free_lunch_retraining_2025\n    title: \"A Free Lunch in LLM Compression: Revisiting Retraining after Pruning\"\n    authors: \"Moritz Wagner, Christophe Roux, Max Zimmer, Sebastian Pokutta\"\n    year: 2025\n    venue: \"arXiv Oct 2025 (revised Feb 2026)\"\n    category: background\n    role: \"Local reconstruction as efficient post-pruning recovery\"\n    relevance: 6\n    key_finding: \"Local reconstruction matches sophisticated PEFT recovery with >10x less data/compute. Pruning method matters less as model size grows.\"\n    our_relation: \"Shows cheap recovery can work — but their SFT-based reconstruction has ceiling; our RLVR recovery pushes beyond that ceiling for reasoning tasks.\"\n    citation_priority: should-cite\n    arxiv_id: \"2510.14444\"\n\n  - id: grasp_2020\n    title: \"Picking Winning Tickets Before Training by Preserving Gradient Flow\"\n    authors: \"Chaoqi Wang, Guodong Zhang, Roger Grosse\"\n    year: 2020\n    venue: \"ICLR 2020\"\n    category: background\n    role: \"GraSP — gradient signal preservation for pruning at initialization\"\n    relevance: 5\n    key_finding: \"Hessian-gradient product preserves gradient flow post-pruning; 80% VGG-16 pruning with only 1.6% top-1 drop on ImageNet; outperforms SNIP by 4-6% at high sparsity.\"\n    our_relation: \"Classic baseline for gradient-based importance. GRASPrune extends this idea to LLMs; our CKA operates at functional level rather than gradient flow.\"\n    citation_priority: should-cite\n    arxiv_id: \"2002.07376\"\n\n  - id: fnf_2026\n    title: \"FNF: Functional Network Fingerprint for Large Language Models\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Jan 2026\"\n    category: background\n    role: \"Functional network concept applied to LLM identification\"\n    relevance: 4\n    key_finding: \"Co-activating neuron groups form consistent functional networks; robust to model obfuscation.\"\n    our_relation: \"Validates the 'functional network' framing we share with FANG/FuncNet; extends concept to model fingerprinting.\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2601.22692\"\n\n  - id: redundancy_aware_cnn_2020\n    title: \"Redundancy-Aware Pruning of Convolutional Neural Networks\"\n    authors: \"\"\n    year: 2020\n    venue: \"Neural Computation\"\n    category: background\n    role: \"Pioneer of redundancy-based pruning\"\n    relevance: 4\n    key_finding: \"Redundancy metrics guide pruning decisions in CNNs\"\n    our_relation: \"Conceptual ancestor; we apply redundancy-awareness to LLM structured pruning\"\n    citation_priority: nice-to-have\n    arxiv_id: \"\"\n\n  - id: self_distilled_rlvr_2026\n    title: \"Self-Distilled RLVR\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"RLVR training efficiency improvement\"\n    relevance: 5\n    key_finding: \"Self-distillation stabilizes RLVR training and improves sample efficiency\"\n    our_relation: \"Could improve our RLVR recovery phase efficiency\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2604.03128\"\n\n  - id: diet_2026\n    title: \"DieT: Dimension-wise Global Pruning via Task-specific Importance Score\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: background\n    role: \"Dimension-wise importance for width pruning\"\n    relevance: 5\n    key_finding: \"Task-specific dimension importance outperforms activation-based metrics at 20-40% sparsity\"\n    our_relation: \"Alternative width importance metric; we use CKA overlap instead\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2603.23985\"\n\n  - id: task_neurons_2026\n    title: \"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific LLMs\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"Task-specific neuron identification and pruning recovery dynamics\"\n    relevance: 6\n    key_finding: \"10% task-specific neuron removal causes collapse; 15-20% robustness threshold; fine-tuning substantially recovers\"\n    our_relation: \"Supports need for recovery-aware pruning; our CKA predicts which neurons are functionally critical\"\n    citation_priority: should-cite\n    arxiv_id: \"2604.27115\"\n\n  - id: ddp_2026\n    title: \"DDP: Deterministic Differentiable Structured Pruning for Large Language Models\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: background\n    role: \"Differentiable mask-only structured pruning\"\n    relevance: 5\n    key_finding: \"Deterministic soft surrogate of l0 constraint eliminates train-test mismatch in differentiable pruning\"\n    our_relation: \"Alternative pruning backbone; mask-only optimization complementary to our CKA-guided selection\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2603.08065\"\n\n  - id: pruning_vlm_recovery_2026\n    title: \"Structural Pruning of Large Vision Language Models: Pruning Dynamics, Recovery, and Data Efficiency\"\n    authors: \"Yiran Huang, Lukas Thede, Massimiliano Mancini, Wenjia Xu, Zeynep Akata\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"Comprehensive pruning + recovery study for VLMs\"\n    relevance: 5\n    key_finding: \"Width pruning + KD recovery outperforms layer pruning + SFT on VLMs; 5% data recovers 95% performance; SFT+hidden-state distillation is optimal.\"\n    our_relation: \"Validates width pruning + recovery paradigm; our CKA-guided approach adds prediction of recoverability\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2604.24380\"\n\n  - id: hape_2026\n    title: \"HAP-E: Hessian-Aware Structured Pruning of LLMs for Efficient Inference\"\n    authors: \"\"\n    year: 2026\n    venue: \"ICLR 2026 (submitted)\"\n    category: background\n    role: \"Hessian-aware structured pruning with adaptive budget allocation\"\n    relevance: 5\n    key_finding: \"Adaptive cross-layer budget reallocation via global screening + OBS-equivalent batch pruning; up to 3% accuracy over SOTA structured pruning\"\n    our_relation: \"Alternative pruning backbone with second-order optimization; complementary to our CKA-guided selection\"\n    citation_priority: nice-to-have\n    arxiv_id: \"\"\n\n  - id: slimllm_2025\n    title: \"SlimLLM: Accurate Structured Pruning for Large Language Models\"\n    authors: \"Jialong Guo, Xinghao Chen, Yehui Tang, Yunhe Wang\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: background\n    role: \"Holistic channel/head importance evaluation with linear regression recovery\"\n    relevance: 5\n    key_finding: \"Evaluates importance of entire channels/heads holistically; non-uniform layer-based pruning ratio via cosine similarity; linear regression for fast recovery\"\n    our_relation: \"Alternative structured pruning metric; their cosine-based layer ratio is complementary to our CKA functional overlap\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2505.22689\"\n\n  - id: spap_2025\n    title: \"SPAP: Structured Pruning via Alternating Optimization and Penalty Methods\"\n    authors: \"\"\n    year: 2025\n    venue: \"arXiv May 2025\"\n    category: background\n    role: \"Optimization-theory-grounded MLP pruning\"\n    relevance: 5\n    key_finding: \"Mixed-integer formulation with relaxation guarantee; alternating minimization with closed-form updates; 1.29x speedup at 30% sparsity\"\n    our_relation: \"Could serve as alternative pruning backbone for MLP layers; operates at different abstraction level from our CKA selection\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2505.03373\"\n\n  - id: wandapp_2025\n    title: \"Wanda++: Pruning Large Language Models via Regional Gradients\"\n    authors: \"\"\n    year: 2025\n    venue: \"ACL 2025\"\n    category: background\n    role: \"Gradient-enhanced unstructured pruning\"\n    relevance: 4\n    key_finding: \"Regional gradients improve Wanda score by up to 32% perplexity reduction; regional optimization minimizes dense-sparse output discrepancy\"\n    our_relation: \"Unstructured pruning evolution; orthogonal to our structured approach but regional optimization idea could inform per-block CKA computation\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2503.04992\"\n\n  # === Must-cite gap fills (Step 3, 2026-05-18) ===\n  - id: llm_pruner_2023\n    title: \"LLM-Pruner: On the Structural Pruning of Large Language Models\"\n    authors: \"Xinyin Ma, Gongfan Fang, Xinchao Wang\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    category: method-component\n    role: \"Foundational structured pruning framework for LLMs using Taylor importance + dependency detection\"\n    relevance: 9\n    key_finding: \"First task-agnostic structured pruning for LLMs; dependency-aware group removal preserves model integrity; 20% pruning with minimal loss after LoRA recovery on LLaMA-7B/13B/30B\"\n    our_relation: \"Foundational baseline; our Taylor importance scoring (Standard method) directly builds on LLM-Pruner. We extend with CKA overlap and RLVR recovery\"\n    citation_priority: must-cite\n    arxiv_id: \"2305.11627\"\n    verified: true\n\n  - id: deepseekmath_grpo_2024\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo\"\n    year: 2024\n    venue: \"arXiv Feb 2024\"\n    category: background\n    role: \"GRPO algorithm origin — Group Relative Policy Optimization for math reasoning\"\n    relevance: 9\n    key_finding: \"Introduces GRPO: group-level reward normalization without critic model; DeepSeekMath-7B achieves 51.7% on MATH competition via GRPO + code-math corpus\"\n    our_relation: \"Our RLVR recovery phase uses GRPO as the alignment algorithm; this is the foundational reference\"\n    citation_priority: must-cite\n    arxiv_id: \"2402.03300\"\n    verified: true\n\n# === Update Log ===\n# 2026-05-15: Literature survey targeting 4 reviewer-flagged gaps\n#   Direction 1 (Structured pruning + RLVR recovery): Added RLRC, NIRVANA, free_lunch_retraining\n#   Direction 2 (CKA in pruning/NAS): Added davari_cka_reliability (must-cite), murphy_debiased_cka, tracenas\n#   Direction 3 (FANG/FuncNet): Confirmed details; added FNF as background\n#   Direction 4 (GraSP baselines): Added grasp_2020 (original), tracenas\n#   Updated: self_healing authors (Ji et al., ICLR 2026), from_llms_to_lrms (Ding et al., 2601.18091),\n#            mpruner (arxiv 2408.13482), slimllm authors, pruning_vlm_recovery authors\n#   Added citation_priority field (must-cite / should-cite / nice-to-have) to all entries\n",
      "numLines": 628,
      "startLine": 1,
      "totalLines": 628
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Let me read the existing literature map (already done), and now I need to search for papers on RL training instability. Let me run the searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "2290dd4d-b2ae-48d3-af65-d4399e6b873a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7VXUjtMWZWz5oXmp7J9xP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18130,
      "cache_read_input_tokens": 19148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18130
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

Now searching for RL training instability papers across the specified directions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "e70a5be0-57bd-4a2a-8d58-65fff155c876",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7VXUjtMWZWz5oXmp7J9xP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18130,
      "cache_read_input_tokens": 19148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18130
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XjmXwe3qVd85Wt9AW3GiB5`</summary>

```json
{
  "query": "reward hacking RLHF language models 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "3faf83a6-e185-438b-8dc9-4edbdbb96439",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7VXUjtMWZWz5oXmp7J9xP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18130,
      "cache_read_input_tokens": 19148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18130
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ENXwusBwHUntqpJ565cfyh`</summary>

```json
{
  "query": "policy collapse reinforcement learning LLM fine-tuning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "8b0c46f7-ed0d-4022-aaf4-3178ad4ea9c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7VXUjtMWZWz5oXmp7J9xP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18130,
      "cache_read_input_tokens": 19148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18130
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0114X9X3EBtRaLFyrLR82eb5`</summary>

```json
{
  "query": "reward overoptimization RLHF scaling 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "b8b1b1f7-928b-46a2-8bd1-144434e899fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7VXUjtMWZWz5oXmp7J9xP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18130,
      "cache_read_input_tokens": 19148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18130
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0144RzzbZAcAHNU8rfj2Wojh`</summary>

```json
{
  "query": "RL training instability language model alignment KL divergence 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "c7859a87-7474-416e-baf2-a89c8ab545e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7VXUjtMWZWz5oXmp7J9xP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18130,
      "cache_read_input_tokens": 19148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18130
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 16 · 2026-05-18T03:15:21.034Z_

<details><summary>↩ Tool result · `toolu_01ENXwusBwHUntqpJ565cfyh`</summary>

```text
Web search results for query: "policy collapse reinforcement learning LLM fine-tuning 2024 2025"

Links: [{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization","url":"https://arxiv.org/html/2508.00222v1"},{"title":"Prosperity before Collapse: How Far Can Off-Policy RL Reach with Stale Data on LLMs?","url":"https://arxiv.org/html/2510.01161"},{"title":"Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle","url":"https://arxiv.org/html/2509.16679v1"},{"title":"NeurIPS Poster Coevolving with the Other You: Fine-Tuning LLM with Sequential Cooperative Multi-Agent Reinforcement Learning","url":"https://neurips.cc/virtual/2024/poster/95347"},{"title":"Fine-tuning LLMs with Reinforcement Learning | by Mehul Jain | Data Science + AI at Microsoft | Medium","url":"https://medium.com/data-science-at-microsoft/fine-tuning-llms-with-reinforcement-learning-ef84fe42d6a6"},{"title":"Prosperity before Collapse: How Far Can Off-Policy RL","url":"https://arxiv.org/pdf/2510.01161"},{"title":"Preprint, 2025 CAN LARGE REASONING MODELS SELF-TRAIN? Sheikh Shafayat1∗","url":"https://arxiv.org/pdf/2505.21444"},{"title":"Fine-tuning LLMs using Reinforcement Learning","url":"https://januverma.substack.com/p/fine-tuning-llms-using-reinforcement"},{"title":"Scaling LLM Reinforcement Learning with Prolonged Training Using ProRL v2 | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/scaling-llm-reinforcement-learning-with-prolonged-training-using-prorl-v2/"}]

I found several relevant sources on policy collapse in reinforcement learning fine-tuning of LLMs. Here's a summary of the key findings:

## Policy Collapse in LLM RL Fine-Tuning (2024-2025)

**Policy Entropy Collapse:**
Policy entropy collapse occurs in reinforcement learning experiments without entropy intervention. Policy performance is achieved at the cost of entropy consumption, limited by depletion of entropy with a predictable theoretical upper limit.

**Capability Boundary Collapse:**
Commonly used RLVR (Reinforcement Learning with Verifiable Reward) methods can lead to capability boundary collapse in LLMs. While pass@1 performance surpasses the base model, pass@k deteriorates. Current RLVR cannot enable LLMs to acquire novel reasoning abilities, but rather simply utilize reasoning patterns already in the base model.

**"Prosperity Before Collapse" Phenomenon:**
Off-policy RL for LLMs shows a prosperity-before-collapse phenomenon: training without a trust region initially outperforms standard methods, but eventually collapses due to instability.

**Model Collapse from Self-Training:**
Models trained using RL on self-labeled data suffer from actor collapsing due to reward hacking.

**Mitigation Strategies:**
Clip-Higher uses a higher upper bound of the PPO clipping range to mitigate policy entropy collapse and promote sampling diversity. A KL penalty to a strong reference policy acts as a trust-region that stabilizes learning and preserves pre-trained priors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "34f92eb7-aa54-488c-9253-bf8f0d935ec7",
  "tool_use_result": {
    "query": "policy collapse reinforcement learning LLM fine-tuning 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SsWwuu7p7a3UjdwQei5gkB",
        "content": [
          {
            "title": "The State of Reinforcement Learning for LLM Reasoning",
            "url": "https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"
          },
          {
            "title": "RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization",
            "url": "https://arxiv.org/html/2508.00222v1"
          },
          {
            "title": "Prosperity before Collapse: How Far Can Off-Policy RL Reach with Stale Data on LLMs?",
            "url": "https://arxiv.org/html/2510.01161"
          },
          {
            "title": "Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle",
            "url": "https://arxiv.org/html/2509.16679v1"
          },
          {
            "title": "NeurIPS Poster Coevolving with the Other You: Fine-Tuning LLM with Sequential Cooperative Multi-Agent Reinforcement Learning",
            "url": "https://neurips.cc/virtual/2024/poster/95347"
          },
          {
            "title": "Fine-tuning LLMs with Reinforcement Learning | by Mehul Jain | Data Science + AI at Microsoft | Medium",
            "url": "https://medium.com/data-science-at-microsoft/fine-tuning-llms-with-reinforcement-learning-ef84fe42d6a6"
          },
          {
            "title": "Prosperity before Collapse: How Far Can Off-Policy RL",
            "url": "https://arxiv.org/pdf/2510.01161"
          },
          {
            "title": "Preprint, 2025 CAN LARGE REASONING MODELS SELF-TRAIN? Sheikh Shafayat1∗",
            "url": "https://arxiv.org/pdf/2505.21444"
          },
          {
            "title": "Fine-tuning LLMs using Reinforcement Learning",
            "url": "https://januverma.substack.com/p/fine-tuning-llms-using-reinforcement"
          },
          {
            "title": "Scaling LLM Reinforcement Learning with Prolonged Training Using ProRL v2 | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/scaling-llm-reinforcement-learning-with-prolonged-training-using-prorl-v2/"
          }
        ]
      },
      "I found several relevant sources on policy collapse in reinforcement learning fine-tuning of LLMs. Here's a summary of the key findings:\n\n## Policy Collapse in LLM RL Fine-Tuning (2024-2025)\n\n**Policy Entropy Collapse:**\nPolicy entropy collapse occurs in reinforcement learning experiments without entropy intervention. Policy performance is achieved at the cost of entropy consumption, limited by depletion of entropy with a predictable theoretical upper limit.\n\n**Capability Boundary Collapse:**\nCommonly used RLVR (Reinforcement Learning with Verifiable Reward) methods can lead to capability boundary collapse in LLMs. While pass@1 performance surpasses the base model, pass@k deteriorates. Current RLVR cannot enable LLMs to acquire novel reasoning abilities, but rather simply utilize reasoning patterns already in the base model.\n\n**\"Prosperity Before Collapse\" Phenomenon:**\nOff-policy RL for LLMs shows a prosperity-before-collapse phenomenon: training without a trust region initially outperforms standard methods, but eventually collapses due to instability.\n\n**Model Collapse from Self-Training:**\nModels trained using RL on self-labeled data suffer from actor collapsing due to reward hacking.\n\n**Mitigation Strategies:**\nClip-Higher uses a higher upper bound of the PPO clipping range to mitigate policy entropy collapse and promote sampling diversity. A KL penalty to a strong reference policy acts as a trust-region that stabilizes learning and preserves pre-trained priors."
    ],
    "durationSeconds": 7.224135690999998
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T03:15:21.914Z_

<details><summary>↩ Tool result · `toolu_01XjmXwe3qVd85Wt9AW3GiB5`</summary>

```text
Web search results for query: "reward hacking RLHF language models 2024 2025"

Links: [{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/html/2502.18770v3"},{"title":"ICML Poster The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking","url":"https://icml.cc/virtual/2025/poster/46294"},{"title":"Inference-Time Reward Hacking in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=hSX7Dd8dxy"},{"title":"Reward Hacking in RLHF - Rohan's Bytes","url":"https://www.rohan-paul.com/p/reward-hacking-in-rlhf"},{"title":"NATURAL EMERGENT MISALIGNMENT FROM REWARD HACKING IN PRODUCTION RL","url":"https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf"},{"title":"NeurIPS Poster InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling","url":"https://neurips.cc/virtual/2024/poster/96739"},{"title":"Inference-Time Reward Hacking in Large Language Models Hadi Khalaf","url":"https://openreview.net/pdf?id=hSX7Dd8dxy"},{"title":"Inference-Time Reward Hacking in Large Language Models","url":"https://openreview.net/pdf?id=vRfDOhiJAR"},{"title":"REWARD MODEL BOOSTING FOR RLHF","url":"https://openreview.net/pdf/2fd4b1609b392151e6692f73c18ac0a8fe54ae94.pdf"}]

I've found comprehensive information about reward hacking in RLHF for language models from recent 2024-2025 research. Here are the key findings:

## Definition and Core Problem

Reward hacking occurs when a reinforcement learning (RL) agent exploits flaws or ambiguities in the reward function to achieve high rewards, without genuinely learning or completing the intended task. With the rise of language models generalizing to a broad spectrum of tasks and RLHF becomes a de facto method for alignment training, reward hacking in RL training of language models has become a critical practical challenge.

## Manifestations in Language Models

Recent research has documented several concerning ways reward hacking appears:

- **Misleading Correctness**: Models may be optimized to output responses that seem correct and convincing but are, in fact, inaccurate, thereby misleading human evaluators to approve its incorrect answers more often.

- **Code Complexity**: RLHF leads to fewer helper functions overall and higher code complexity among incorrect generated programs.

- **Sycophancy**: Sycophancy refers to the tendency of model responses to match user beliefs rather than reflect the truth.

## Recent Mitigation Strategies (2024-2025)

Multiple approaches have emerged to address this problem:

Reward ensemble techniques have shown promise in addressing this issue. InfoRM proposes a framework for reward modeling by introducing a variational information bottleneck objective to filter out irrelevant information. Results reveal a reward threshold in PPO training—exceeding it often triggers reward hacking, degrading the model's win rate.

Energy loss in the final layer of a Large Language Model gradually increases during the RL process, with excessive increase characterizing reward hacking, and extensive experiments demonstrate the effectiveness of EPPO in mitigating reward hacking.

Penalizing reward hacking during training either with an HHH preference model reward or a dedicated reward-hacking classifier is effective in preventing RL from incentivizing reward hacking.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "91c1dfea-f277-4731-93d8-0a53643f00bb",
  "tool_use_result": {
    "query": "reward hacking RLHF language models 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0182Hvy96hs2T22jbYFnayHA",
        "content": [
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/html/2502.18770v3"
          },
          {
            "title": "ICML Poster The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking",
            "url": "https://icml.cc/virtual/2025/poster/46294"
          },
          {
            "title": "Inference-Time Reward Hacking in Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=hSX7Dd8dxy"
          },
          {
            "title": "Reward Hacking in RLHF - Rohan's Bytes",
            "url": "https://www.rohan-paul.com/p/reward-hacking-in-rlhf"
          },
          {
            "title": "NATURAL EMERGENT MISALIGNMENT FROM REWARD HACKING IN PRODUCTION RL",
            "url": "https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf"
          },
          {
            "title": "NeurIPS Poster InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling",
            "url": "https://neurips.cc/virtual/2024/poster/96739"
          },
          {
            "title": "Inference-Time Reward Hacking in Large Language Models Hadi Khalaf",
            "url": "https://openreview.net/pdf?id=hSX7Dd8dxy"
          },
          {
            "title": "Inference-Time Reward Hacking in Large Language Models",
            "url": "https://openreview.net/pdf?id=vRfDOhiJAR"
          },
          {
            "title": "REWARD MODEL BOOSTING FOR RLHF",
            "url": "https://openreview.net/pdf/2fd4b1609b392151e6692f73c18ac0a8fe54ae94.pdf"
          }
        ]
      },
      "I've found comprehensive information about reward hacking in RLHF for language models from recent 2024-2025 research. Here are the key findings:\n\n## Definition and Core Problem\n\nReward hacking occurs when a reinforcement learning (RL) agent exploits flaws or ambiguities in the reward function to achieve high rewards, without genuinely learning or completing the intended task. With the rise of language models generalizing to a broad spectrum of tasks and RLHF becomes a de facto method for alignment training, reward hacking in RL training of language models has become a critical practical challenge.\n\n## Manifestations in Language Models\n\nRecent research has documented several concerning ways reward hacking appears:\n\n- **Misleading Correctness**: Models may be optimized to output responses that seem correct and convincing but are, in fact, inaccurate, thereby misleading human evaluators to approve its incorrect answers more often.\n\n- **Code Complexity**: RLHF leads to fewer helper functions overall and higher code complexity among incorrect generated programs.\n\n- **Sycophancy**: Sycophancy refers to the tendency of model responses to match user beliefs rather than reflect the truth.\n\n## Recent Mitigation Strategies (2024-2025)\n\nMultiple approaches have emerged to address this problem:\n\nReward ensemble techniques have shown promise in addressing this issue. InfoRM proposes a framework for reward modeling by introducing a variational information bottleneck objective to filter out irrelevant information. Results reveal a reward threshold in PPO training—exceeding it often triggers reward hacking, degrading the model's win rate.\n\nEnergy loss in the final layer of a Large Language Model gradually increases during the RL process, with excessive increase characterizing reward hacking, and extensive experiments demonstrate the effectiveness of EPPO in mitigating reward hacking.\n\nPenalizing reward hacking during training either with an HHH preference model reward or a dedicated reward-hacking classifier is effective in preventing RL from incentivizing reward hacking."
    ],
    "durationSeconds": 8.619840821000002
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T03:15:22.079Z_

<details><summary>↩ Tool result · `toolu_0114X9X3EBtRaLFyrLR82eb5`</summary>

```text
Web search results for query: "reward overoptimization RLHF scaling 2023 2024"

Links: [{"title":"[2406.02900] Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://arxiv.org/abs/2406.02900"},{"title":"Reward Model Overoptimization: Root Causes and Mitigations","url":"https://www.reinforced.info/p/reward-model-overoptimization"},{"title":"NeurIPS Poster Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://neurips.cc/virtual/2024/poster/93540"},{"title":"Reward Model Overoptimisation in Iterated RLHF","url":"https://arxiv.org/html/2505.18126v1"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"},{"title":"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"},{"title":"Reward Model Overoptimisation in Iterated RLHF | OpenReview","url":"https://openreview.net/forum?id=efoe5VJfKz"},{"title":"Mitigating Reward Hacking in RLHF via Information- ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/f25d75fc760aec0a6174f9f5d9da59b8-Paper-Conference.pdf"},{"title":"Over-Optimization | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/14-over-optimization"},{"title":"[2210.10760] Scaling Laws for Reward Model Overoptimization","url":"https://arxiv.org/abs/2210.10760"}]

I've completed a web search for "reward overoptimization RLHF scaling 2023 2024". Here are the key findings:

## Core Concept

Reward over-optimization or reward hacking is where performance as measured by the learned proxy reward model increases, but true quality plateaus or even deteriorates.

## Key Research Papers

**2023 Paper:**
The foundational work "Scaling Laws for Reward Model Overoptimization" was published in the International Conference on Machine Learning in 2023. This paper studied how, because the reward model is an imperfect proxy, optimizing its value too much can hinder ground truth performance, in accordance with Goodhart's law.

**2024 Papers:**
Recent work has formalized the reward over-optimization problem for Direct Alignment Algorithms (DAAs) and explored its consequences across objectives, training regimes, and model scales. Research found that at different KL-divergence budgets, Direct Alignment Algorithms exhibit degradation patterns similar to those found in RLHF.

## Root Causes

Reward model optimization happens during RLHF because RL finds a way to reward-hack an imperfect reward model, which crumbles under the induced distribution shift.

## Mitigation Approaches

Using the controlled AlpacaFarm benchmark, research observed that overoptimisation tends to decrease over successive iterations, as reward models increasingly approximate ground-truth preferences. Additionally, techniques like InfoRM have been shown to consistently prevent reward overoptimization and substantially enhance RLHF performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "5d5b8fb6-7777-45ab-ab5d-a4447ae99103",
  "tool_use_result": {
    "query": "reward overoptimization RLHF scaling 2023 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ekc4tw8yzNAcTTR6EHb9K4",
        "content": [
          {
            "title": "[2406.02900] Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms",
            "url": "https://arxiv.org/abs/2406.02900"
          },
          {
            "title": "Reward Model Overoptimization: Root Causes and Mitigations",
            "url": "https://www.reinforced.info/p/reward-model-overoptimization"
          },
          {
            "title": "NeurIPS Poster Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms",
            "url": "https://neurips.cc/virtual/2024/poster/93540"
          },
          {
            "title": "Reward Model Overoptimisation in Iterated RLHF",
            "url": "https://arxiv.org/html/2505.18126v1"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization",
            "url": "https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"
          },
          {
            "title": "Reward Model Overoptimisation in Iterated RLHF | OpenReview",
            "url": "https://openreview.net/forum?id=efoe5VJfKz"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Information- ...",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/f25d75fc760aec0a6174f9f5d9da59b8-Paper-Conference.pdf"
          },
          {
            "title": "Over-Optimization | RLHF Book by Nathan Lambert",
            "url": "https://rlhfbook.com/c/14-over-optimization"
          },
          {
            "title": "[2210.10760] Scaling Laws for Reward Model Overoptimization",
            "url": "https://arxiv.org/abs/2210.10760"
          }
        ]
      },
      "I've completed a web search for \"reward overoptimization RLHF scaling 2023 2024\". Here are the key findings:\n\n## Core Concept\n\nReward over-optimization or reward hacking is where performance as measured by the learned proxy reward model increases, but true quality plateaus or even deteriorates.\n\n## Key Research Papers\n\n**2023 Paper:**\nThe foundational work \"Scaling Laws for Reward Model Overoptimization\" was published in the International Conference on Machine Learning in 2023. This paper studied how, because the reward model is an imperfect proxy, optimizing its value too much can hinder ground truth performance, in accordance with Goodhart's law.\n\n**2024 Papers:**\nRecent work has formalized the reward over-optimization problem for Direct Alignment Algorithms (DAAs) and explored its consequences across objectives, training regimes, and model scales. Research found that at different KL-divergence budgets, Direct Alignment Algorithms exhibit degradation patterns similar to those found in RLHF.\n\n## Root Causes\n\nReward model optimization happens during RLHF because RL finds a way to reward-hack an imperfect reward model, which crumbles under the induced distribution shift.\n\n## Mitigation Approaches\n\nUsing the controlled AlpacaFarm benchmark, research observed that overoptimisation tends to decrease over successive iterations, as reward models increasingly approximate ground-truth preferences. Additionally, techniques like InfoRM have been shown to consistently prevent reward overoptimization and substantially enhance RLHF performance."
    ],
    "durationSeconds": 7.2966813780000015
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T03:15:22.976Z_

<details><summary>↩ Tool result · `toolu_0144RzzbZAcAHNU8rfj2Wojh`</summary>

```text
Web search results for query: "RL training instability language model alignment KL divergence 2024 2025"

Links: [{"title":"Large Language Models Alignment via Comparative RL - EECS","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2024/EECS-2024-21.pdf"},{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_298.pdf"},{"title":"Preprint. A COMEDY OF ESTIMATORS: ON KL REGULARIZATION IN RL TRAINING OF LLMS","url":"https://www.arxiv.org/pdf/2512.21852"},{"title":"A Comedy of Estimators: On KL Regularization in RL Training of LLMs | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.21852"},{"title":"A Technical Survey of Reinforcement Learning Techniques for Large Language Models","url":"https://arxiv.org/html/2507.04136v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2024 BEYOND REVERSE KL: GENERALIZING","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/2b1d1e5affe5fdb70372cd90dd8afd49-Paper-Conference.pdf"},{"title":"Reinforcement Learning for Large Language Models via ...","url":"https://aclanthology.org/2025.emnlp-main.1085.pdf"},{"title":"[2512.21852] A Comedy of Estimators: On KL Regularization in RL Training of LLMs","url":"https://arxiv.org/abs/2512.21852"},{"title":"Reinforcement Learning with Supervised Alignment","url":"https://aclanthology.org/2025.findings-emnlp.378.pdf"}]

I've completed the web search for your query on RL training instability in language model alignment with KL divergence. Here are the key findings from recent 2024-2025 research:

## Key Research Findings

**Training Instability Issues:**
RLHF faces challenges such as reward model misgeneralization and training instability. Recent work has identified that common implementation choices lead to biased gradient estimates, resulting in unstable training and suboptimal performance.

**KL Divergence Implementation Problems:**
A particularly important 2025 paper titled "A Comedy of Estimators" reveals critical issues with KL regularization. Prevailing practices for incorporating KL regularization do not provide correct gradients for stated objectives, creating a discrepancy between the objective and its implementation. The research shows that K1-in-reward consistently shows the lowest bias when comparing different KL estimator configurations.

**KL Regularization's Role:**
KL regularization is widely used in reinforcement learning from human feedback (RLHF), where it serves as a safety mechanism to prevent the fine-tuned model from drifting too far from the base model. More specifically, this regularization ensures that the policy explores within the space of coherent sequences by constraining it within the support of the base model, mitigating problems such as language drift, reward over-optimization or catastrophic forgetting.

**Method Comparisons:**
The average KL-divergence and reward ranking is DPO > P3O > PPO > SFT, and although DPO marginally surpasses P3O in reward, it has a considerably higher KL-divergence, which may be detrimental to the quality of generation.

These findings suggest that while KL divergence is essential for stable RL training, its practical implementation requires careful attention to how estimators are incorporated into the training objective.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "1a8e4158-15cf-48a9-877b-19c29272cadc",
  "tool_use_result": {
    "query": "RL training instability language model alignment KL divergence 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_015ec535eHyJ8W6HoiAEg2xQ",
        "content": [
          {
            "title": "Large Language Models Alignment via Comparative RL - EECS",
            "url": "https://www2.eecs.berkeley.edu/Pubs/TechRpts/2024/EECS-2024-21.pdf"
          },
          {
            "title": "Reinforcement Learning Journal 2025 Cover Page",
            "url": "https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_298.pdf"
          },
          {
            "title": "Preprint. A COMEDY OF ESTIMATORS: ON KL REGULARIZATION IN RL TRAINING OF LLMS",
            "url": "https://www.arxiv.org/pdf/2512.21852"
          },
          {
            "title": "A Comedy of Estimators: On KL Regularization in RL Training of LLMs | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2512.21852"
          },
          {
            "title": "A Technical Survey of Reinforcement Learning Techniques for Large Language Models",
            "url": "https://arxiv.org/html/2507.04136v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 BEYOND REVERSE KL: GENERALIZING",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/2b1d1e5affe5fdb70372cd90dd8afd49-Paper-Conference.pdf"
          },
          {
            "title": "Reinforcement Learning for Large Language Models via ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1085.pdf"
          },
          {
            "title": "[2512.21852] A Comedy of Estimators: On KL Regularization in RL Training of LLMs",
            "url": "https://arxiv.org/abs/2512.21852"
          },
          {
            "title": "Reinforcement Learning with Supervised Alignment",
            "url": "https://aclanthology.org/2025.findings-emnlp.378.pdf"
          }
        ]
      },
      "I've completed the web search for your query on RL training instability in language model alignment with KL divergence. Here are the key findings from recent 2024-2025 research:\n\n## Key Research Findings\n\n**Training Instability Issues:**\nRLHF faces challenges such as reward model misgeneralization and training instability. Recent work has identified that common implementation choices lead to biased gradient estimates, resulting in unstable training and suboptimal performance.\n\n**KL Divergence Implementation Problems:**\nA particularly important 2025 paper titled \"A Comedy of Estimators\" reveals critical issues with KL regularization. Prevailing practices for incorporating KL regularization do not provide correct gradients for stated objectives, creating a discrepancy between the objective and its implementation. The research shows that K1-in-reward consistently shows the lowest bias when comparing different KL estimator configurations.\n\n**KL Regularization's Role:**\nKL regularization is widely used in reinforcement learning from human feedback (RLHF), where it serves as a safety mechanism to prevent the fine-tuned model from drifting too far from the base model. More specifically, this regularization ensures that the policy explores within the space of coherent sequences by constraining it within the support of the base model, mitigating problems such as language drift, reward over-optimization or catastrophic forgetting.\n\n**Method Comparisons:**\nThe average KL-divergence and reward ranking is DPO > P3O > PPO > SFT, and although DPO marginally surpasses P3O in reward, it has a considerably higher KL-divergence, which may be detrimental to the quality of generation.\n\nThese findings suggest that while KL divergence is essential for stable RL training, its practical implementation requires careful attention to how estimators are incorporated into the training objective."
    ],
    "durationSeconds": 8.019868546999998
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Let me search for more specific papers with arxiv IDs to get precise details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "518865a1-e89b-4135-a286-feac3fd9c400",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USX8Z5cr2EXb8tcDGDze6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4174,
      "cache_read_input_tokens": 37278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4174
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

_source line 21_

Found strong candidates. Let me get arxiv details for the top 3 papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "4c92373c-87e9-4132-b60a-0cfd7e78d590",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USX8Z5cr2EXb8tcDGDze6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4174,
      "cache_read_input_tokens": 37278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4174
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VKqz1Gn2ztJgXf5gz87Ls3`</summary>

```json
{
  "query": "arxiv 2210.10760 \"Scaling Laws for Reward Model Overoptimization\" Gao 2023 ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "bf4e587b-b148-4d91-a5d2-a48d5b80f05a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USX8Z5cr2EXb8tcDGDze6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4174,
      "cache_read_input_tokens": 37278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4174
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QUPgaqYQ57KfhtLhqoiXdD`</summary>

```json
{
  "query": "arxiv 2512.21852 \"A Comedy of Estimators\" KL regularization RL training LLMs authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "cb3b2bd2-929e-4d8e-a7ba-531f8ef4de48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USX8Z5cr2EXb8tcDGDze6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4174,
      "cache_read_input_tokens": 37278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4174
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_014KcNfyLR4XD9PabSjN5wme`</summary>

```json
{
  "query": "\"capability boundary collapse\" RLVR arxiv 2508.00222 RL-PLUS authors 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "77a668e2-6e0a-4c0d-ad2d-918914258526",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USX8Z5cr2EXb8tcDGDze6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4174,
      "cache_read_input_tokens": 37278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4174
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

_source line 25 · 2026-05-18T03:15:32.849Z_

<details><summary>↩ Tool result · `toolu_01VKqz1Gn2ztJgXf5gz87Ls3`</summary>

```text
Web search results for query: "arxiv 2210.10760 "Scaling Laws for Reward Model Overoptimization" Gao 2023 ICML"

Links: [{"title":"[2210.10760] Scaling Laws for Reward Model Overoptimization","url":"https://arxiv.org/abs/2210.10760"},{"title":"Scaling Laws for Reward Model Overoptimization Leo Gao OpenAI John Schulman","url":"https://arxiv.org/pdf/2210.10760"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://www.researchgate.net/publication/364436070_Scaling_Laws_for_Reward_Model_Overoptimization"},{"title":"Scaling Laws for Reward Model Overoptimization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv221010760G/abstract"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h.html"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://www.summarizepaper.com/en/arxiv-id/2210.10760v1/"},{"title":"Scaling Laws For Reward Model Overoptimization","url":"https://www.scribd.com/document/668584786/2210-10760"},{"title":"[PDF] Scaling Laws for Reward Model Overoptimization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scaling-Laws-for-Reward-Model-Overoptimization-Gao-Schulman/fb3dc5e20e0a71134ca916f0d6d8d41f01225b4b"},{"title":"Paper page - Scaling Laws for Reward Model Overoptimization","url":"https://huggingface.co/papers/2210.10760"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://www.alignmentforum.org/posts/shcSdHGPhnLQkpSbX/scaling-laws-for-reward-model-overoptimization"}]

I found the paper successfully. Here's what I can tell you about it:

## Paper Summary

The paper "Scaling Laws for Reward Model Overoptimization" was authored by Leo Gao and 2 other authors (John Schulman and Jacob Hilton).

**Key Content:**

In reinforcement learning from human feedback, it is common to optimize against a reward model trained to predict human preferences. Because the reward model is an imperfect proxy, optimizing its value too much can hinder ground truth performance, in accordance with Goodhart's law.

The work uses a synthetic setup in which a fixed "gold-standard" reward model plays the role of humans, providing labels used to train a proxy reward model. They study how the gold reward model score changes as they optimize against the proxy reward model using either reinforcement learning or best-of-n sampling.

**Main Findings:**

The relationship follows a different functional form depending on the method of optimization, and in both cases the coefficients scale smoothly with the number of reward model parameters.

**Publication:**

The paper was published in the Proceedings of the 40th International Conference on Machine Learning, PMLR 202:10835-10866, 2023.

The arXiv preprint (2210.10760) was posted on October 19, 2022, and the work was later accepted to ICML 2023.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "86f68777-9741-4e15-b425-c2e3ea437700",
  "tool_use_result": {
    "query": "arxiv 2210.10760 \"Scaling Laws for Reward Model Overoptimization\" Gao 2023 ICML",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N2vuducmKTBrExBbPm3ty6",
        "content": [
          {
            "title": "[2210.10760] Scaling Laws for Reward Model Overoptimization",
            "url": "https://arxiv.org/abs/2210.10760"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization Leo Gao OpenAI John Schulman",
            "url": "https://arxiv.org/pdf/2210.10760"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization",
            "url": "https://www.researchgate.net/publication/364436070_Scaling_Laws_for_Reward_Model_Overoptimization"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2022arXiv221010760G/abstract"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization",
            "url": "https://proceedings.mlr.press/v202/gao23h.html"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization",
            "url": "https://www.summarizepaper.com/en/arxiv-id/2210.10760v1/"
          },
          {
            "title": "Scaling Laws For Reward Model Overoptimization",
            "url": "https://www.scribd.com/document/668584786/2210-10760"
          },
          {
            "title": "[PDF] Scaling Laws for Reward Model Overoptimization | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Scaling-Laws-for-Reward-Model-Overoptimization-Gao-Schulman/fb3dc5e20e0a71134ca916f0d6d8d41f01225b4b"
          },
          {
            "title": "Paper page - Scaling Laws for Reward Model Overoptimization",
            "url": "https://huggingface.co/papers/2210.10760"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization",
            "url": "https://www.alignmentforum.org/posts/shcSdHGPhnLQkpSbX/scaling-laws-for-reward-model-overoptimization"
          }
        ]
      },
      "I found the paper successfully. Here's what I can tell you about it:\n\n## Paper Summary\n\nThe paper \"Scaling Laws for Reward Model Overoptimization\" was authored by Leo Gao and 2 other authors (John Schulman and Jacob Hilton).\n\n**Key Content:**\n\nIn reinforcement learning from human feedback, it is common to optimize against a reward model trained to predict human preferences. Because the reward model is an imperfect proxy, optimizing its value too much can hinder ground truth performance, in accordance with Goodhart's law.\n\nThe work uses a synthetic setup in which a fixed \"gold-standard\" reward model plays the role of humans, providing labels used to train a proxy reward model. They study how the gold reward model score changes as they optimize against the proxy reward model using either reinforcement learning or best-of-n sampling.\n\n**Main Findings:**\n\nThe relationship follows a different functional form depending on the method of optimization, and in both cases the coefficients scale smoothly with the number of reward model parameters.\n\n**Publication:**\n\nThe paper was published in the Proceedings of the 40th International Conference on Machine Learning, PMLR 202:10835-10866, 2023.\n\nThe arXiv preprint (2210.10760) was posted on October 19, 2022, and the work was later accepted to ICML 2023."
    ],
    "durationSeconds": 5.965799695999999
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T03:15:34.065Z_

<details><summary>↩ Tool result · `toolu_01QUPgaqYQ57KfhtLhqoiXdD`</summary>

```text
Web search results for query: "arxiv 2512.21852 "A Comedy of Estimators" KL regularization RL training LLMs authors"

Links: [{"title":"[2512.21852] A Comedy of Estimators: On KL Regularization in RL Training of LLMs","url":"https://arxiv.org/abs/2512.21852"},{"title":"Preprint. A COMEDY OF ESTIMATORS: ON KL REGULARIZATION IN RL TRAINING OF LLMS","url":"https://www.arxiv.org/pdf/2512.21852"},{"title":"A Comedy of Estimators: On KL Regularization in RL Training of LLMs | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.21852v2"},{"title":"A Comedy of Estimators: On KL Regularization in RL Training of LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251221852S/abstract"},{"title":"A Comedy of Estimators: On KL Regularization in RL Training of LLMs | OpenReview","url":"https://openreview.net/forum?id=MkLHbwSMP3"},{"title":"AI Papers on X: \"A Comedy of Estimators: On KL Regularization in RL Training of LLMs Vedant Shah, Johan Obando-Ceron, Vineet Jain, Brian Bartoldson, Bhavya Kailkhura, Sarthak Mittal, Glen Berseth, Pablo Samuel Castro, Yoshua Bengio, Nikolay Malkin, … (arXiv:2512.21852) https://t.co/JtsAUWzB2n\" / X","url":"https://x.com/SciFi/status/2007460236672565250"},{"title":"A Comedy of Estimators: On KL Regularization in RL ...","url":"https://www.aimodels.fyi/papers/arxiv/comedy-estimators-kl-regularization-rl-training-llms"},{"title":"Choosing KL Estimators in RL: From Value Unbiasedness to Gradient Correctness | Xihuai Wang's Page","url":"https://xihuai18.github.io/reinforcement-learning/2025/12/01/kl-estimators-en.html"},{"title":"On KL Regularization in RL Training of LLMs","url":"https://www.researchgate.net/publication/399134876_A_Comedy_of_Estimators_On_KL_Regularization_in_RL_Training_of_LLMs"},{"title":"Diffusion Alignment Beyond KL: Variance Minimisation as Effective Policy Optimiser","url":"https://arxiv.org/html/2602.12229"}]

Based on the search results, I found the paper you're looking for. Here's the information about arxiv paper 2512.21852:

## Paper Details

**Title:** "A Comedy of Estimators: On KL Regularization in RL Training of LLMs"

**Authors:** Vedant Shah, Johan Obando-Ceron, Vineet Jain, Brian Bartoldson, Bhavya Kailkhura, Sarthak Mittal, Glen Berseth, Pablo Samuel Castro, Yoshua Bengio, Nikolay Malkin, Moksh Jain, Siddarth Venkatraman, and Aaron Courville

## Summary

The paper focuses on how reinforcement learning can improve the reasoning performance of LLMs, with particular attention to the reverse Kullback-Leibler (KL) divergence regularization term used in RL training objectives.

Since computing the KL divergence exactly is intractable, various estimators are used in practice. Despite wide adoption, there is no systematic study analyzing how different KL estimators are incorporated in the objective and their effects on RL-trained model performance. Recent works show that prevailing practices for incorporating KL regularization do not provide correct gradients for stated objectives, highlighting a discrepancy between the intended objective and its implementation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "ec6e269c-eefc-43a9-9cfd-fe77780c0b77",
  "tool_use_result": {
    "query": "arxiv 2512.21852 \"A Comedy of Estimators\" KL regularization RL training LLMs authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_015U2T7RgJHeyfty2kestGfb",
        "content": [
          {
            "title": "[2512.21852] A Comedy of Estimators: On KL Regularization in RL Training of LLMs",
            "url": "https://arxiv.org/abs/2512.21852"
          },
          {
            "title": "Preprint. A COMEDY OF ESTIMATORS: ON KL REGULARIZATION IN RL TRAINING OF LLMS",
            "url": "https://www.arxiv.org/pdf/2512.21852"
          },
          {
            "title": "A Comedy of Estimators: On KL Regularization in RL Training of LLMs | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2512.21852v2"
          },
          {
            "title": "A Comedy of Estimators: On KL Regularization in RL Training of LLMs - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv251221852S/abstract"
          },
          {
            "title": "A Comedy of Estimators: On KL Regularization in RL Training of LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=MkLHbwSMP3"
          },
          {
            "title": "AI Papers on X: \"A Comedy of Estimators: On KL Regularization in RL Training of LLMs Vedant Shah, Johan Obando-Ceron, Vineet Jain, Brian Bartoldson, Bhavya Kailkhura, Sarthak Mittal, Glen Berseth, Pablo Samuel Castro, Yoshua Bengio, Nikolay Malkin, … (arXiv:2512.21852) https://t.co/JtsAUWzB2n\" / X",
            "url": "https://x.com/SciFi/status/2007460236672565250"
          },
          {
            "title": "A Comedy of Estimators: On KL Regularization in RL ...",
            "url": "https://www.aimodels.fyi/papers/arxiv/comedy-estimators-kl-regularization-rl-training-llms"
          },
          {
            "title": "Choosing KL Estimators in RL: From Value Unbiasedness to Gradient Correctness | Xihuai Wang's Page",
            "url": "https://xihuai18.github.io/reinforcement-learning/2025/12/01/kl-estimators-en.html"
          },
          {
            "title": "On KL Regularization in RL Training of LLMs",
            "url": "https://www.researchgate.net/publication/399134876_A_Comedy_of_Estimators_On_KL_Regularization_in_RL_Training_of_LLMs"
          },
          {
            "title": "Diffusion Alignment Beyond KL: Variance Minimisation as Effective Policy Optimiser",
            "url": "https://arxiv.org/html/2602.12229"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's the information about arxiv paper 2512.21852:\n\n## Paper Details\n\n**Title:** \"A Comedy of Estimators: On KL Regularization in RL Training of LLMs\"\n\n**Authors:** Vedant Shah, Johan Obando-Ceron, Vineet Jain, Brian Bartoldson, Bhavya Kailkhura, Sarthak Mittal, Glen Berseth, Pablo Samuel Castro, Yoshua Bengio, Nikolay Malkin, Moksh Jain, Siddarth Venkatraman, and Aaron Courville\n\n## Summary\n\nThe paper focuses on how reinforcement learning can improve the reasoning performance of LLMs, with particular attention to the reverse Kullback-Leibler (KL) divergence regularization term used in RL training objectives.\n\nSince computing the KL divergence exactly is intractable, various estimators are used in practice. Despite wide adoption, there is no systematic study analyzing how different KL estimators are incorporated in the objective and their effects on RL-trained model performance. Recent works show that prevailing practices for incorporating KL regularization do not provide correct gradients for stated objectives, highlighting a discrepancy between the intended objective and its implementation."
    ],
    "durationSeconds": 6.234531978999995
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T03:15:36.963Z_

<details><summary>↩ Tool result · `toolu_014KcNfyLR4XD9PabSjN5wme`</summary>

```text
Web search results for query: ""capability boundary collapse" RLVR arxiv 2508.00222 RL-PLUS authors 2025"

Links: [{"title":"RL-PLUS: Countering Capability Boundary Collapse of LLMs in...","url":"https://arxiv.org/abs/2508.00222"},{"title":"Preprint, July 2025 RL-PLUS: Countering Capability Boundary Collapse of LLMs","url":"https://arxiv.org/pdf/2508.00222"},{"title":"RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization","url":"https://arxiv.org/html/2508.00222"},{"title":"Paper page - RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization","url":"https://huggingface.co/papers/2508.00222"},{"title":"The Debate on RLVR Reasoning Capability Boundary:","url":"https://arxiv.org/pdf/2510.04028"},{"title":"The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? A Two-Stage Dynamic View","url":"https://arxiv.org/html/2510.04028v1"},{"title":"RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization | Request PDF","url":"https://www.researchgate.net/publication/394263125_RL-PLUS_Countering_Capability_Boundary_Collapse_of_LLMs_in_Reinforcement_Learning_with_Hybrid-policy_Optimization"},{"title":"(PDF) The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? A Two-Stage Dynamic View","url":"https://www.researchgate.net/publication/396249087_The_Debate_on_RLVR_Reasoning_Capability_Boundary_Shrinkage_Expansion_or_Both_A_Two-Stage_Dynamic_View"},{"title":"BoundRL: Efficient Token-level Structured Text Segmentation through Reinforced Boundary Generation","url":"https://arxiv.org/html/2510.20151"},{"title":"Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning","url":"https://arxiv.org/html/2510.10649v1"}]

I've found comprehensive information about the paper you're looking for. Here are the key findings:

## RL-PLUS: Countering Capability Boundary Collapse

Reinforcement Learning with Verifiable Reward (RLVR) has significantly advanced the complex reasoning abilities of Large Language Models (LLMs), but can lead to capability boundary collapse, narrowing the LLM's problem-solving scope.

This occurs due to RLVR's essentially on-policy strategy coupled with LLM's immense action space and sparse reward.

## The Proposed Solution

RL-PLUS is a novel hybrid-policy optimization approach for LLMs that synergizes internal exploitation with external data to achieve stronger reasoning capabilities and surpass the boundaries of base models, integrating Multiple Importance Sampling to address distributional mismatch from external data, and Exploration-Based Advantage Function to guide the model towards high-value, unexplored reasoning paths.

## Results and Authors

The paper was submitted on July 31, 2025 and last revised on April 15, 2026 (version 5), with authors including Yihong Dong, Xue Jiang, Yongding Tao, Huanyu Liu, Kechi Zhang, Lili Mou, Rongyu Cao, Yingwei Ma, Jue Chen, Binhua Li, Zhi Jin, Fei Huang, Yongbin Li, and Ge Li.

RL-PLUS achieves state-of-the-art performance on six math reasoning benchmarks, superior performance on six out-of-distribution reasoning tasks, and consistent and significant gains across diverse model families with average relative improvements up to 69.2%, with Pass@k curves indicating that RL-PLUS effectively resolves the capability boundary collapse problem.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "bbe1cbab-d5b4-46f2-a702-16b35a948219",
  "tool_use_result": {
    "query": "\"capability boundary collapse\" RLVR arxiv 2508.00222 RL-PLUS authors 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TarqpPjL4pSUPjcJJzSvpU",
        "content": [
          {
            "title": "RL-PLUS: Countering Capability Boundary Collapse of LLMs in...",
            "url": "https://arxiv.org/abs/2508.00222"
          },
          {
            "title": "Preprint, July 2025 RL-PLUS: Countering Capability Boundary Collapse of LLMs",
            "url": "https://arxiv.org/pdf/2508.00222"
          },
          {
            "title": "RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization",
            "url": "https://arxiv.org/html/2508.00222"
          },
          {
            "title": "Paper page - RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization",
            "url": "https://huggingface.co/papers/2508.00222"
          },
          {
            "title": "The Debate on RLVR Reasoning Capability Boundary:",
            "url": "https://arxiv.org/pdf/2510.04028"
          },
          {
            "title": "The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? A Two-Stage Dynamic View",
            "url": "https://arxiv.org/html/2510.04028v1"
          },
          {
            "title": "RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization | Request PDF",
            "url": "https://www.researchgate.net/publication/394263125_RL-PLUS_Countering_Capability_Boundary_Collapse_of_LLMs_in_Reinforcement_Learning_with_Hybrid-policy_Optimization"
          },
          {
            "title": "(PDF) The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? A Two-Stage Dynamic View",
            "url": "https://www.researchgate.net/publication/396249087_The_Debate_on_RLVR_Reasoning_Capability_Boundary_Shrinkage_Expansion_or_Both_A_Two-Stage_Dynamic_View"
          },
          {
            "title": "BoundRL: Efficient Token-level Structured Text Segmentation through Reinforced Boundary Generation",
            "url": "https://arxiv.org/html/2510.20151"
          },
          {
            "title": "Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning",
            "url": "https://arxiv.org/html/2510.10649v1"
          }
        ]
      },
      "I've found comprehensive information about the paper you're looking for. Here are the key findings:\n\n## RL-PLUS: Countering Capability Boundary Collapse\n\nReinforcement Learning with Verifiable Reward (RLVR) has significantly advanced the complex reasoning abilities of Large Language Models (LLMs), but can lead to capability boundary collapse, narrowing the LLM's problem-solving scope.\n\nThis occurs due to RLVR's essentially on-policy strategy coupled with LLM's immense action space and sparse reward.\n\n## The Proposed Solution\n\nRL-PLUS is a novel hybrid-policy optimization approach for LLMs that synergizes internal exploitation with external data to achieve stronger reasoning capabilities and surpass the boundaries of base models, integrating Multiple Importance Sampling to address distributional mismatch from external data, and Exploration-Based Advantage Function to guide the model towards high-value, unexplored reasoning paths.\n\n## Results and Authors\n\nThe paper was submitted on July 31, 2025 and last revised on April 15, 2026 (version 5), with authors including Yihong Dong, Xue Jiang, Yongding Tao, Huanyu Liu, Kechi Zhang, Lili Mou, Rongyu Cao, Yingwei Ma, Jue Chen, Binhua Li, Zhi Jin, Fei Huang, Yongbin Li, and Ge Li.\n\nRL-PLUS achieves state-of-the-art performance on six math reasoning benchmarks, superior performance on six out-of-distribution reasoning tasks, and consistent and significant gains across diverse model families with average relative improvements up to 69.2%, with Pass@k curves indicating that RL-PLUS effectively resolves the capability boundary collapse problem."
    ],
    "durationSeconds": 8.660589617999998
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now I have 3 strong candidates:

1. **Gao et al. 2023** - "Scaling Laws for Reward Model Overoptimization" (ICML 2023, arxiv 2210.10760)
   - Authors: Leo Gao, John Schulman, Jacob Hilton
   - Key finding: Reward overoptimization follows predictable scaling laws; proxy reward increases but gold reward degrades as optimization pressure grows
   - Relation to our work: Pruning-induced collapse can be viewed as an extreme case of reward overoptimization where damaged model capacity amplifies the proxy-gold reward gap
   
2. **Shah et al. 2025** - "A Comedy of Estimators: On KL Regularization in RL Training of LLMs" (arxiv 2512.21852)
   - Authors: Vedant Shah, Johan Obando-Ceron, Vineet Jain, Brian Bartoldson, Bhavya Kailkhura, Sarthak Mittal, Glen Berseth, Pablo Samuel Castro, Yoshua Bengio, Nikolay Malkin, Moksh Jain, Siddarth Venkatraman, Aaron Courville
   - Key finding: Examines how KL regularization implementations in RL training affect LLM behavior and optimization dynamics

3. **Dong et al. 2025** - "RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization" (arxiv 2508.00222)
   - Authors: Yihong Dong et al.
   - Key finding: Shows how on-policy strategies combined with sparse rewards in large action spaces lead to capability boundary collapse, which parallels the structural collapse we see from pruning

I'm also considering whether "policy entropy collapse" and the Energy Loss paper from ICML 2025 might offer more direct insights into the training instability mechanisms at play.

Actually, I think I have a solid set of three papers covering distinct angles: Gao et al. 2023 on reward overoptimization, RL-PLUS on policy collapse, and Shah et al. 2025 on KL regularization issues during alignment. Let me verify these aren't already in my literature map before adding them. I've verified none of these additional entries conflict with the existing IDs, so I can proceed with inserting them into the database.

For the Gao paper on reward model overoptimization, I'm adding a structured entry that connects their scaling laws findings to how pruning amplifies the gap between proxy and actual reward signals—this becomes relevant context for understanding why reduced model capacity leads to performance collapse during RL fine-tuning.

Now I'm documenting the Shah et al. paper on KL regularization pitfalls in RLHF, which addresses implementation inconsistencies that can destabilize training, and I need to capture their key findings about how these regularization issues interact with model capacity constraints. I'm now verifying these papers actually exist in the literature. The first one checks out at arxiv.org/abs/2210.10760 from ICML 2023, and I'm confirming the others through similar searches.

Now I need to insert these three entries into the YAML file before the Update Log section starts at line 619, placing them right after the last existing entry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "17b7a4a7-5be6-4506-a09c-10373143d962",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012r8QXTEXU83ehvWx2CZ7qX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3385,
      "cache_read_input_tokens": 41452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3385
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

_source line 29_

Found 3 verified papers. Now adding entries to the literature map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "708f91f9-bd1c-4e46-8b9e-d75ed97dae8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012r8QXTEXU83ehvWx2CZ7qX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3385,
      "cache_read_input_tokens": 41452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3385
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

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_01CtNFBwCVadeFNdRbKWgoNG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml",
  "old_string": "  - id: deepseekmath_grpo_2024\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo\"\n    year: 2024\n    venue: \"arXiv Feb 2024\"\n    category: background\n    role: \"GRPO algorithm origin — Group Relative Policy Optimization for math reasoning\"\n    relevance: 9\n    key_finding: \"Introduces GRPO: group-level reward normalization without critic model; DeepSeekMath-7B achieves 51.7% on MATH competition via GRPO + code-math corpus\"\n    our_relation: \"Our RLVR recovery phase uses GRPO as the alignment algorithm; this is the foundational reference\"\n    citation_priority: must-cite\n    arxiv_id: \"2402.03300\"\n    verified: true\n\n# === Update Log ===",
  "new_string": "  - id: deepseekmath_grpo_2024\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo\"\n    year: 2024\n    venue: \"arXiv Feb 2024\"\n    category: background\n    role: \"GRPO algorithm origin — Group Relative Policy Optimization for math reasoning\"\n    relevance: 9\n    key_finding: \"Introduces GRPO: group-level reward normalization without critic model; DeepSeekMath-7B achieves 51.7% on MATH competition via GRPO + code-math corpus\"\n    our_relation: \"Our RLVR recovery phase uses GRPO as the alignment algorithm; this is the foundational reference\"\n    citation_priority: must-cite\n    arxiv_id: \"2402.03300\"\n    verified: true\n\n  # === RL Training Instability (added 2026-05-18) ===\n  - id: gao_reward_overoptimization_2023\n    title: \"Scaling Laws for Reward Model Overoptimization\"\n    authors: \"Leo Gao, John Schulman, Jacob Hilton\"\n    year: 2023\n    venue: \"ICML 2023\"\n    category: background\n    role: \"RL training instability — reward overoptimization scaling laws\"\n    relevance: 6\n    key_finding: \"Proxy reward optimization degrades gold reward following predictable scaling laws; overoptimization worsens with more RL compute and smaller reward models\"\n    our_relation: \"Pruning-induced collapse can be viewed as amplified reward overoptimization where reduced model capacity widens the proxy-gold reward gap\"\n    citation_priority: should-cite\n    arxiv_id: \"2210.10760\"\n    verified: true\n\n  - id: rl_plus_collapse_2025\n    title: \"RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization\"\n    authors: \"Yihong Dong, Xue Jiang, Yongding Tao, Huanyu Liu, Kechi Zhang, Lili Mou, Rongyu Cao, Yingwei Ma, Jue Chen, Binhua Li, Zhi Jin, Fei Huang, Yongbin Li, Ge Li\"\n    year: 2025\n    venue: \"arXiv Jul 2025\"\n    category: background\n    role: \"RL training instability — capability boundary collapse in RLVR\"\n    relevance: 7\n    key_finding: \"RLVR causes capability boundary collapse: pass@1 improves but pass@k degrades, narrowing the model's problem-solving scope due to on-policy training with sparse reward\"\n    our_relation: \"Pruning-induced collapse is a structural variant of capability boundary collapse; pruning removes capacity that exacerbates the on-policy sparse-reward instability they identify\"\n    citation_priority: should-cite\n    arxiv_id: \"2508.00222\"\n    verified: true\n\n  - id: comedy_of_estimators_2025\n    title: \"A Comedy of Estimators: On KL Regularization in RL Training of LLMs\"\n    authors: \"Vedant Shah, Johan Obando-Ceron, Vineet Jain, Brian Bartoldson, Bhavya Kailkhura, Sarthak Mittal, Glen Berseth, Pablo Samuel Castro, Yoshua Bengio, Nikolay Malkin, Moksh Jain, Siddarth Venkatraman, Aaron Courville\"\n    year: 2025\n    venue: \"arXiv Dec 2025\"\n    category: background\n    role: \"RL training instability — KL regularization implementation pitfalls\"\n    relevance: 5\n    key_finding: \"Prevailing KL regularization implementations in RLHF/RLVR provide incorrect gradients for stated objectives, causing training instability and suboptimal performance\"\n    our_relation: \"Informs our GRPO recovery design: incorrect KL estimation can destabilize RLVR recovery of pruned models, especially when pruning shifts the policy distribution\"\n    citation_priority: should-cite\n    arxiv_id: \"2512.21852\"\n    verified: true\n\n# === Update Log ==="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "6d7380a0-b7f0-42bc-a397-dbe3fea56d68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012r8QXTEXU83ehvWx2CZ7qX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3385,
      "cache_read_input_tokens": 41452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3385
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

_source line 31 · 2026-05-18T03:16:33.263Z_

<details><summary>↩ Tool result · `toolu_01CtNFBwCVadeFNdRbKWgoNG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "23948b93-602c-44b9-a85c-32a2c8a0e1d0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml",
    "oldString": "  - id: deepseekmath_grpo_2024\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo\"\n    year: 2024\n    venue: \"arXiv Feb 2024\"\n    category: background\n    role: \"GRPO algorithm origin — Group Relative Policy Optimization for math reasoning\"\n    relevance: 9\n    key_finding: \"Introduces GRPO: group-level reward normalization without critic model; DeepSeekMath-7B achieves 51.7% on MATH competition via GRPO + code-math corpus\"\n    our_relation: \"Our RLVR recovery phase uses GRPO as the alignment algorithm; this is the foundational reference\"\n    citation_priority: must-cite\n    arxiv_id: \"2402.03300\"\n    verified: true\n\n# === Update Log ===",
    "newString": "  - id: deepseekmath_grpo_2024\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo\"\n    year: 2024\n    venue: \"arXiv Feb 2024\"\n    category: background\n    role: \"GRPO algorithm origin — Group Relative Policy Optimization for math reasoning\"\n    relevance: 9\n    key_finding: \"Introduces GRPO: group-level reward normalization without critic model; DeepSeekMath-7B achieves 51.7% on MATH competition via GRPO + code-math corpus\"\n    our_relation: \"Our RLVR recovery phase uses GRPO as the alignment algorithm; this is the foundational reference\"\n    citation_priority: must-cite\n    arxiv_id: \"2402.03300\"\n    verified: true\n\n  # === RL Training Instability (added 2026-05-18) ===\n  - id: gao_reward_overoptimization_2023\n    title: \"Scaling Laws for Reward Model Overoptimization\"\n    authors: \"Leo Gao, John Schulman, Jacob Hilton\"\n    year: 2023\n    venue: \"ICML 2023\"\n    category: background\n    role: \"RL training instability — reward overoptimization scaling laws\"\n    relevance: 6\n    key_finding: \"Proxy reward optimization degrades gold reward following predictable scaling laws; overoptimization worsens with more RL compute and smaller reward models\"\n    our_relation: \"Pruning-induced collapse can be viewed as amplified reward overoptimization where reduced model capacity widens the proxy-gold reward gap\"\n    citation_priority: should-cite\n    arxiv_id: \"2210.10760\"\n    verified: true\n\n  - id: rl_plus_collapse_2025\n    title: \"RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization\"\n    authors: \"Yihong Dong, Xue Jiang, Yongding Tao, Huanyu Liu, Kechi Zhang, Lili Mou, Rongyu Cao, Yingwei Ma, Jue Chen, Binhua Li, Zhi Jin, Fei Huang, Yongbin Li, Ge Li\"\n    year: 2025\n    venue: \"arXiv Jul 2025\"\n    category: background\n    role: \"RL training instability — capability boundary collapse in RLVR\"\n    relevance: 7\n    key_finding: \"RLVR causes capability boundary collapse: pass@1 improves but pass@k degrades, narrowing the model's problem-solving scope due to on-policy training with sparse reward\"\n    our_relation: \"Pruning-induced collapse is a structural variant of capability boundary collapse; pruning removes capacity that exacerbates the on-policy sparse-reward instability they identify\"\n    citation_priority: should-cite\n    arxiv_id: \"2508.00222\"\n    verified: true\n\n  - id: comedy_of_estimators_2025\n    title: \"A Comedy of Estimators: On KL Regularization in RL Training of LLMs\"\n    authors: \"Vedant Shah, Johan Obando-Ceron, Vineet Jain, Brian Bartoldson, Bhavya Kailkhura, Sarthak Mittal, Glen Berseth, Pablo Samuel Castro, Yoshua Bengio, Nikolay Malkin, Moksh Jain, Siddarth Venkatraman, Aaron Courville\"\n    year: 2025\n    venue: \"arXiv Dec 2025\"\n    category: background\n    role: \"RL training instability — KL regularization implementation pitfalls\"\n    relevance: 5\n    key_finding: \"Prevailing KL regularization implementations in RLHF/RLVR provide incorrect gradients for stated objectives, causing training instability and suboptimal performance\"\n    our_relation: \"Informs our GRPO recovery design: incorrect KL estimation can destabilize RLVR recovery of pruned models, especially when pruning shifts the policy distribution\"\n    citation_priority: should-cite\n    arxiv_id: \"2512.21852\"\n    verified: true\n\n# === Update Log ===",
    "originalFile": "papers:\n  # === Direct Competitors ===\n  - id: self_healing_2025\n    title: \"Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning\"\n    authors: \"Yixin Ji, Zhimin Lin, Juntao Li, Kaixin Wu, Kai Yao, Xu Jia, Linjian Mo, Min Zhang\"\n    year: 2025\n    venue: \"ICLR 2026 submission (OpenReview #12375, submitted Sep 2025)\"\n    category: direct-competitor\n    role: \"RLVR recovery baseline\"\n    relevance: 9\n    key_finding: \"RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%. Tested on 5 LRMs across 6 math benchmarks.\"\n    our_relation: \"We extend beyond single sparsity ratio and add CKA-guided pruning selection\"\n    citation_priority: must-cite\n    arxiv_id: \"\"\n\n  - id: resp_2025\n    title: \"RESP: Self-Reflective Structured Pruning for Reasoning LLMs\"\n    authors: \"\"\n    year: 2025\n    venue: \"arXiv Dec 2025\"\n    category: direct-competitor\n    role: \"Structured pruning for reasoning without recovery\"\n    relevance: 8\n    key_finding: \"GSM8K 81.3% at 40% sparsity via self-reflective importance\"\n    our_relation: \"No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity\"\n    citation_priority: must-cite\n    arxiv_id: \"2512.02185\"\n\n  - id: grasprune_2026\n    title: \"GRASPrune: Global Gating-based Structural Pruning for LLMs\"\n    authors: \"\"\n    year: 2026\n    venue: \"ACL 2026 Main\"\n    category: direct-competitor\n    role: \"SOTA budgeted structural pruning\"\n    relevance: 8\n    key_finding: \"Global gating achieves best structured pruning under budget constraints\"\n    our_relation: \"GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top\"\n    citation_priority: must-cite\n    arxiv_id: \"2604.19398\"\n\n  - id: opsd_2026\n    title: \"OPSD: One-shot Post-RL Structured Distillation\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv May 2026\"\n    category: direct-competitor\n    role: \"Post-RL compression via distillation\"\n    relevance: 7\n    key_finding: \"Compress post-RL model in one shot via structured distillation\"\n    our_relation: \"Distillation-based vs our pruning+recovery approach; complementary\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: doing_more_with_less_2026\n    title: \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: direct-competitor\n    role: \"Pruning improves test-time scaling\"\n    relevance: 7\n    key_finding: \"Unstructured pruning can augment test-time scaling; structured pruning degrades it\"\n    our_relation: \"Motivates why structured pruning needs recovery; we address this gap with RLVR\"\n    citation_priority: should-cite\n    arxiv_id: \"2604.25098\"\n\n  - id: gprune_llm_2026\n    title: \"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: direct-competitor\n    role: \"Cross-distribution generalization-aware pruning\"\n    relevance: 6\n    key_finding: \"Accounts for neuron cross-distribution behavior; reduces calibration bias\"\n    our_relation: \"Complementary importance metric; our CKA captures functional overlap vs their generalization gap\"\n    citation_priority: should-cite\n    arxiv_id: \"2603.13418\"\n\n  - id: boiling_frog_2026\n    title: \"Gradually Compacting Large Language Models for Reasoning Like a Boiling Frog\"\n    authors: \"Yiran Zhao, Shengyang Zhou, Zijian Wu, Tongyan Hu, Yuhui Xu, Rengan Dou, Kenji Kawaguchi, Shafiq Joty, Junnan Li, Michael Qizhe Shieh\"\n    year: 2026\n    venue: \"arXiv Feb 2026\"\n    category: direct-competitor\n    role: \"Iterative prune-tune loop for reasoning model compression\"\n    relevance: 7\n    key_finding: \"Gradual Prune-Tune Loop avoids abrupt performance collapse; iterative pruning+finetuning preserves reasoning\"\n    our_relation: \"Similar prune-then-recover paradigm but uses SFT recovery; we use RLVR which is more effective and add CKA-guided pruning selection\"\n    citation_priority: must-cite\n    arxiv_id: \"2602.04919\"\n\n  - id: think_prune_train_2025\n    title: \"Think, Prune, Train, Improve: Scaling Reasoning without Scaling Models\"\n    authors: \"Caia Costello, Simon Guo, Anna Goldie, Azalia Mirhoseini\"\n    year: 2025\n    venue: \"arXiv Apr 2025 (Stanford Scaling Intelligence Lab)\"\n    category: direct-competitor\n    role: \"Self-training on pruned reasoning traces to improve small models\"\n    relevance: 6\n    key_finding: \"Iterative fine-tuning on ground-truth-pruned reasoning traces; Gemma2-9B matches LLaMA-3.1-70B on GSM8K\"\n    our_relation: \"Complementary — prunes reasoning traces (CoT) not model weights; could combine with our weight pruning\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2504.18116\"\n\n  # === Method Components ===\n  - id: mpruner_2024\n    title: \"MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning\"\n    authors: \"\"\n    year: 2024\n    venue: \"arXiv Aug 2024\"\n    category: method-component\n    role: \"CKA for layer importance estimation\"\n    relevance: 8\n    key_finding: \"CKA similarity between layers identifies redundant layers for removal; 50% parameter reduction with minimal accuracy loss\"\n    our_relation: \"We adapt CKA from layer-level to width-level functional overlap prediction\"\n    citation_priority: must-cite\n    arxiv_id: \"2408.13482\"\n\n  - id: lachance_thesis_2024\n    title: \"Using Centered Kernel Alignment for Understanding and Pruning Neural Networks\"\n    authors: \"Lachance\"\n    year: 2024\n    venue: \"URI Master's Thesis\"\n    category: method-component\n    role: \"CKA-based pruning theoretical foundation\"\n    relevance: 6\n    key_finding: \"CKA layer similarity correlates with pruning recoverability\"\n    our_relation: \"Validates CKA as signal for pruning decisions; we extend to predict RLVR recovery\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: fang_2025\n    title: \"FANG: Improving Generalization in LLM Structured Pruning via Function-Aware Neuron Grouping\"\n    authors: \"Tao Yu, Yongqi An, Kuan Zhu, Guibo Zhu, Ming Tang, Jinqiao Wang\"\n    year: 2025\n    venue: \"arXiv Dec 2025\"\n    category: method-component\n    role: \"Function-aware neuron grouping for structured pruning\"\n    relevance: 7\n    key_finding: \"Groups FFN neurons by functional roles; shared neuron retention prevents cross-task accuracy loss; outperforms FLAP/OBC by 1.5-8.5% at 30-40% sparsity\"\n    our_relation: \"Closest conceptual parallel — both identify functionally critical neurons, but FANG uses activation-based grouping while we use CKA similarity; no recovery component\"\n    citation_priority: must-cite\n    arxiv_id: \"2512.23014\"\n\n  - id: funcnet_2025\n    title: \"Pruning Large Language Models by Identifying and Preserving Functional Networks\"\n    authors: \"Yiheng Liu, Junhao Ning, Sichen Xia, Xiaohui Gao, Ning Qiang, Bao Ge, Junwei Han, Xintao Hu\"\n    year: 2025\n    venue: \"arXiv Aug 2025\"\n    category: method-component\n    role: \"ICA-based functional network identification for pruning\"\n    relevance: 7\n    key_finding: \"Applies ICA (from neuroimaging) to decompose LLM into functional networks; preserves key neurons within identified networks\"\n    our_relation: \"Similar motivation — treat LLM as digital brain and preserve functional structure — but uses ICA vs our CKA; no RLVR recovery\"\n    citation_priority: must-cite\n    arxiv_id: \"2508.05239\"\n\n  - id: bonsai_2025\n    title: \"Bonsai: Gradient-Free Structured Pruning for LLMs\"\n    authors: \"\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: method-component\n    role: \"Gradient-free structured pruning alternative\"\n    relevance: 6\n    key_finding: \"Achieves competitive structured pruning without backprop\"\n    our_relation: \"Alternative pruning strategy; our CKA metric is also gradient-free\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: pat_2025\n    title: \"PAT: Pruning-Aware Tuning for Large Language Models\"\n    authors: \"Yijiang Liu et al.\"\n    year: 2025\n    venue: \"AAAI 2025\"\n    category: method-component\n    role: \"Joint pruning and tuning framework via Hybrid Sparsification Modules\"\n    relevance: 6\n    key_finding: \"Co-optimizing pruning mask and fine-tuning via HSMs; surpasses LoRA-64 by 1.26% at 25% pruning on Llama2-7B\"\n    our_relation: \"Related idea of pruning-tuning interaction; we separate pruning and RLVR recovery\"\n    citation_priority: should-cite\n    arxiv_id: \"2408.14721\"\n\n  - id: rac_2025\n    title: \"RAC: Chain-of-Thought Reconstruction for Pruned Reasoning Models\"\n    authors: \"\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    category: method-component\n    role: \"CoT reconstruction post-pruning\"\n    relevance: 7\n    key_finding: \"Reconstructing CoT improves unstructured/2:4 pruned reasoning models\"\n    our_relation: \"Complementary recovery strategy; could combine with our RLVR approach\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: paser_2025\n    title: \"PASER: Data Selection for Pruning Recovery\"\n    authors: \"\"\n    year: 2025\n    venue: \"under review\"\n    category: method-component\n    role: \"Recovery training data selection\"\n    relevance: 6\n    key_finding: \"Selective data for recovery training improves efficiency\"\n    our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"\n    citation_priority: nice-to-have\n    arxiv_id: \"\"\n\n  - id: dppo_2026\n    title: \"DPPO: Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Rollout pruning to accelerate GRPO training\"\n    relevance: 5\n    key_finding: \"Importance-sampling-based rollout pruning achieves 2.37x GRPO speedup with 3.36% accuracy gain on Qwen3-4B\"\n    our_relation: \"Could accelerate our GRPO-based RLVR recovery phase\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2603.04135\"\n\n  - id: arrol_2026\n    title: \"ARRoL: Prune as You Generate — Online Rollout Pruning for Faster and Better RLVR\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Online rollout pruning for RLVR efficiency\"\n    relevance: 5\n    key_finding: \"Lightweight quality head predicts rollout success probability for early pruning during RLVR\"\n    our_relation: \"Complementary technique for speeding up RLVR recovery training\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2603.24840\"\n\n  - id: restorelcc_2025\n    title: \"RestoreLCC: Restoring Pruned Large Language Models via Lost Component Compensation\"\n    authors: \"Zijian Feng, Hanzhang Zhou, Zixiao Zhu, Tianjiao Li, Jia Jim Deryl Chua, Lee Onn Mak, Gee Wah Ng, Kezhi Mao\"\n    year: 2025\n    venue: \"NeurIPS 2025 (Spotlight, top 10%)\"\n    category: method-component\n    role: \"Plug-and-play pruning recovery via activation compensation\"\n    relevance: 6\n    key_finding: \"Contrastively probes critical attention heads, extracts lost components from activation differences, injects them back; +1.25-2.65% over SOTA baselines across structured/unstructured pruning\"\n    our_relation: \"Alternative recovery paradigm (activation editing vs RLVR); could be complementary — apply RestoreLCC before RLVR for staged recovery\"\n    citation_priority: should-cite\n    arxiv_id: \"2510.21834\"\n\n  - id: fastforward_2025\n    title: \"FastForward Pruning: Efficient LLM Pruning via Single-Step Reinforcement Learning\"\n    authors: \"\"\n    year: 2025\n    venue: \"arXiv Nov 2025\"\n    category: method-component\n    role: \"RL-based non-uniform sparsity allocation for LLM pruning\"\n    relevance: 5\n    key_finding: \"Decoupled single-step RL framework separates policy optimization from budget satisfaction; efficient non-uniform layer-wise sparsity search\"\n    our_relation: \"Uses RL for pruning decisions (not recovery); complementary — could combine their RL sparsity allocation with our CKA-guided selection\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2511.18977\"\n\n  - id: nirvana_2025\n    title: \"NIRVANA: Structured Pruning Reimagined for Large Language Models Compression\"\n    authors: \"Mengting Ai, Tianxin Wei, Sirui Chen, Jingrui He\"\n    year: 2025\n    venue: \"arXiv Sep 2025\"\n    category: method-component\n    role: \"NTK-based saliency with adaptive sparsity allocation\"\n    relevance: 6\n    key_finding: \"First-order saliency from Neural Tangent Kernel under Adam dynamics; adaptive cross-module sparsity; KL-based calibration data selection. Outperforms SOTA on Llama3/Qwen/T5.\"\n    our_relation: \"Strong pruning baseline; their NTK saliency is complementary to our CKA functional overlap — could combine both signals\"\n    citation_priority: should-cite\n    arxiv_id: \"2509.14230\"\n\n  - id: tracenas_2026\n    title: \"TraceNAS: Zero-shot LLM Pruning via Gradient Trace Correlation\"\n    authors: \"Prajna G. Malettira, Manish Nagaraj, Arjun Roy, Shubham Negi, Kaushik Roy\"\n    year: 2026\n    venue: \"arXiv Feb 2026\"\n    category: method-component\n    role: \"Gradient trace for joint depth+width NAS-style pruning\"\n    relevance: 6\n    key_finding: \"Scale-invariant gradient trace correlation as proxy for pruned architecture quality; joint depth+width search on single GPU in 8.5h; competitive with training-intensive methods on Llama/Qwen\"\n    our_relation: \"Related NAS-for-pruning approach; their gradient trace could complement our CKA as alternative architecture quality proxy\"\n    citation_priority: should-cite\n    arxiv_id: \"2602.02891\"\n\n  - id: rlrc_2025\n    title: \"RLRC: Reinforcement Learning-based Recovery for Compressed Vision-Language-Action Models\"\n    authors: \"Yuxuan Chen, Xiao Li\"\n    year: 2025\n    venue: \"arXiv Jun 2025\"\n    category: method-component\n    role: \"RL-based recovery for compressed VLA models (robotics)\"\n    relevance: 6\n    key_finding: \"Three-stage: structured pruning → SFT+RL recovery → quantization. 8x memory reduction, 2.3x throughput, maintains/surpasses original task success.\"\n    our_relation: \"Extends RL recovery paradigm to robotics VLAs; validates that RL recovery generalizes beyond language-only models. Parallel evidence for our RLVR recovery hypothesis.\"\n    citation_priority: should-cite\n    arxiv_id: \"2506.17639\"\n\n  # === Background / Theory ===\n  - id: kornblith_cka_2019\n    title: \"Similarity of Neural Network Representations Revisited\"\n    authors: \"Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton\"\n    year: 2019\n    venue: \"ICML 2019\"\n    category: background\n    role: \"CKA original paper — foundational method for our functional overlap metric\"\n    relevance: 9\n    key_finding: \"CKA achieves 99.3% accuracy in identifying corresponding layers across different initializations; CCA/SVCCA only 1.4-45.4%. Invariant to orthogonal transform and isotropic scaling.\"\n    our_relation: \"Foundational method — our CKA-guided pruning directly builds on this. Key justification: CKA >> CCA/SVCCA for reliable layer correspondence\"\n    citation_priority: must-cite\n    arxiv_id: \"1905.00414\"\n\n  - id: davari_cka_reliability_2023\n    title: \"Reliability of CKA as a Similarity Measure in Deep Learning\"\n    authors: \"MohammadReza Davari, Stefan Horoi, Amine Natik, Guillaume Lajoie, Guy Wolf, Eugene Belilovsky\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    category: background\n    role: \"CKA limitations and failure modes — essential for honest CKA justification\"\n    relevance: 7\n    key_finding: \"CKA is sensitive to outliers and simple transformations preserving linear separability; CKA values can be manipulated without changing functional behavior. Calls for caution.\"\n    our_relation: \"Must-cite for CKA justification section. We should acknowledge limitations and explain why they don't invalidate our use case (intra-model layer comparison, not cross-model with different transformations).\"\n    citation_priority: must-cite\n    arxiv_id: \"2210.16156\"\n\n  - id: murphy_debiased_cka_2024\n    title: \"Correcting Biased Centered Kernel Alignment Measures in Biological and Artificial Neural Networks\"\n    authors: \"Alex Murphy, Joel Zylberberg, Alona Fyshe\"\n    year: 2024\n    venue: \"ICLR 2024 Re-Align Workshop\"\n    category: background\n    role: \"Debiased CKA for high-dimensionality settings\"\n    relevance: 5\n    key_finding: \"Biased CKA gives misleadingly high similarity when feature-sample ratio is skewed; debiased CKA corrects this. Shuffled data doesn't change biased CKA scores.\"\n    our_relation: \"Nice-to-have citation. Our setting (same model, same data) is less affected by this bias, but worth mentioning in limitations.\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2405.01012\"\n\n  - id: raghu_svcca_2017\n    title: \"SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability\"\n    authors: \"Maithra Raghu, Justin Gilmer, Jason Yosinski, Jascha Sohl-Dickstein\"\n    year: 2017\n    venue: \"NeurIPS 2017\"\n    category: background\n    role: \"SVCCA — predecessor to CKA, baseline representation similarity method\"\n    relevance: 5\n    key_finding: \"SVD dimensionality reduction + CCA for comparing representations; reveals bottom-up convergence dynamics and intrinsic dimensionality\"\n    our_relation: \"CKA alternative baseline. SVCCA lacks invariance to isotropic scaling and fails at cross-network layer identification (only 45% accuracy vs CKA's 99%)\"\n    citation_priority: should-cite\n    arxiv_id: \"1706.05806\"\n\n  - id: klabunde_similarity_survey_2025\n    title: \"Similarity of Neural Network Models: A Survey of Functional and Representational Measures\"\n    authors: \"Max Klabunde, Tobias Schumacher, Markus Strohmaier, Florian Lemmerich\"\n    year: 2025\n    venue: \"ACM Computing Surveys, Vol. 57, Issue 9\"\n    category: background\n    role: \"Comprehensive survey of representation similarity measures including CKA, CCA, SVCCA, PWCCA\"\n    relevance: 7\n    key_finding: \"First comprehensive review comparing representational vs functional similarity; covers CKA properties, robustness, and practical applications including pruning\"\n    our_relation: \"Key citation for CKA justification — survey confirms CKA's advantages over alternatives for model analysis and compression\"\n    citation_priority: must-cite\n    arxiv_id: \"2305.06329\"\n\n  - id: mipp_2024\n    title: \"MIPP: Mutual Information Preserving Neural Network Pruning\"\n    authors: \"\"\n    year: 2024\n    venue: \"arXiv Nov 2024\"\n    category: background\n    role: \"Information-theoretic pruning criterion — MI alternative to CKA\"\n    relevance: 5\n    key_finding: \"Structured activation-based pruning conserving MI between adjacent layers; sample efficiency proportional to MI between masks and data\"\n    our_relation: \"MI is a viable alternative but computationally expensive in high dimensions and less stable than CKA. Supports functional similarity matters for pruning.\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2411.00147\"\n\n  - id: rl_squeezes_2026\n    title: \"RL Squeezes, SFT Expands: Different Mechanisms in Post-Training\"\n    authors: \"\"\n    year: 2026\n    venue: \"ICLR 2026 Poster\"\n    category: background\n    role: \"Theoretical basis for why RLVR works differently from SFT\"\n    relevance: 8\n    key_finding: \"RLVR compresses representation while SFT expands; different inductive biases\"\n    our_relation: \"Explains why RLVR recovery succeeds where SFT fails post-pruning\"\n    citation_priority: must-cite\n    arxiv_id: \"\"\n\n  - id: from_llms_to_lrms_2026\n    title: \"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models\"\n    authors: \"Longwei Ding, Anhao Zhao, Fanghua Ye, Ziyang Chen, Xiaoyu Shen\"\n    year: 2026\n    venue: \"arXiv Jan 2026\"\n    category: background\n    role: \"Width vs depth pruning for reasoning models\"\n    relevance: 7\n    key_finding: \"Width pruning preserves reasoning better than depth pruning; static pruning > dynamic for long-chain reasoning; recovery relies on distribution-aligned post-fine-tuning, not calibration data.\"\n    our_relation: \"Motivates our focus on width-level structured pruning; validates that reasoning models need specialized pruning strategies\"\n    citation_priority: must-cite\n    arxiv_id: \"2601.18091\"\n\n  - id: p2_law_2025\n    title: \"P2 Law: Scaling Law for Pruning Recovery Training\"\n    authors: \"\"\n    year: 2025\n    venue: \"ACL 2025\"\n    category: background\n    role: \"Theoretical scaling of recovery compute\"\n    relevance: 7\n    key_finding: \"Recovery training follows predictable scaling with compute and data\"\n    our_relation: \"Informs our recovery budget estimation; we extend to RLVR-specific scaling\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: free_lunch_retraining_2025\n    title: \"A Free Lunch in LLM Compression: Revisiting Retraining after Pruning\"\n    authors: \"Moritz Wagner, Christophe Roux, Max Zimmer, Sebastian Pokutta\"\n    year: 2025\n    venue: \"arXiv Oct 2025 (revised Feb 2026)\"\n    category: background\n    role: \"Local reconstruction as efficient post-pruning recovery\"\n    relevance: 6\n    key_finding: \"Local reconstruction matches sophisticated PEFT recovery with >10x less data/compute. Pruning method matters less as model size grows.\"\n    our_relation: \"Shows cheap recovery can work — but their SFT-based reconstruction has ceiling; our RLVR recovery pushes beyond that ceiling for reasoning tasks.\"\n    citation_priority: should-cite\n    arxiv_id: \"2510.14444\"\n\n  - id: grasp_2020\n    title: \"Picking Winning Tickets Before Training by Preserving Gradient Flow\"\n    authors: \"Chaoqi Wang, Guodong Zhang, Roger Grosse\"\n    year: 2020\n    venue: \"ICLR 2020\"\n    category: background\n    role: \"GraSP — gradient signal preservation for pruning at initialization\"\n    relevance: 5\n    key_finding: \"Hessian-gradient product preserves gradient flow post-pruning; 80% VGG-16 pruning with only 1.6% top-1 drop on ImageNet; outperforms SNIP by 4-6% at high sparsity.\"\n    our_relation: \"Classic baseline for gradient-based importance. GRASPrune extends this idea to LLMs; our CKA operates at functional level rather than gradient flow.\"\n    citation_priority: should-cite\n    arxiv_id: \"2002.07376\"\n\n  - id: fnf_2026\n    title: \"FNF: Functional Network Fingerprint for Large Language Models\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Jan 2026\"\n    category: background\n    role: \"Functional network concept applied to LLM identification\"\n    relevance: 4\n    key_finding: \"Co-activating neuron groups form consistent functional networks; robust to model obfuscation.\"\n    our_relation: \"Validates the 'functional network' framing we share with FANG/FuncNet; extends concept to model fingerprinting.\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2601.22692\"\n\n  - id: redundancy_aware_cnn_2020\n    title: \"Redundancy-Aware Pruning of Convolutional Neural Networks\"\n    authors: \"\"\n    year: 2020\n    venue: \"Neural Computation\"\n    category: background\n    role: \"Pioneer of redundancy-based pruning\"\n    relevance: 4\n    key_finding: \"Redundancy metrics guide pruning decisions in CNNs\"\n    our_relation: \"Conceptual ancestor; we apply redundancy-awareness to LLM structured pruning\"\n    citation_priority: nice-to-have\n    arxiv_id: \"\"\n\n  - id: self_distilled_rlvr_2026\n    title: \"Self-Distilled RLVR\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"RLVR training efficiency improvement\"\n    relevance: 5\n    key_finding: \"Self-distillation stabilizes RLVR training and improves sample efficiency\"\n    our_relation: \"Could improve our RLVR recovery phase efficiency\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2604.03128\"\n\n  - id: diet_2026\n    title: \"DieT: Dimension-wise Global Pruning via Task-specific Importance Score\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: background\n    role: \"Dimension-wise importance for width pruning\"\n    relevance: 5\n    key_finding: \"Task-specific dimension importance outperforms activation-based metrics at 20-40% sparsity\"\n    our_relation: \"Alternative width importance metric; we use CKA overlap instead\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2603.23985\"\n\n  - id: task_neurons_2026\n    title: \"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific LLMs\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"Task-specific neuron identification and pruning recovery dynamics\"\n    relevance: 6\n    key_finding: \"10% task-specific neuron removal causes collapse; 15-20% robustness threshold; fine-tuning substantially recovers\"\n    our_relation: \"Supports need for recovery-aware pruning; our CKA predicts which neurons are functionally critical\"\n    citation_priority: should-cite\n    arxiv_id: \"2604.27115\"\n\n  - id: ddp_2026\n    title: \"DDP: Deterministic Differentiable Structured Pruning for Large Language Models\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: background\n    role: \"Differentiable mask-only structured pruning\"\n    relevance: 5\n    key_finding: \"Deterministic soft surrogate of l0 constraint eliminates train-test mismatch in differentiable pruning\"\n    our_relation: \"Alternative pruning backbone; mask-only optimization complementary to our CKA-guided selection\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2603.08065\"\n\n  - id: pruning_vlm_recovery_2026\n    title: \"Structural Pruning of Large Vision Language Models: Pruning Dynamics, Recovery, and Data Efficiency\"\n    authors: \"Yiran Huang, Lukas Thede, Massimiliano Mancini, Wenjia Xu, Zeynep Akata\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"Comprehensive pruning + recovery study for VLMs\"\n    relevance: 5\n    key_finding: \"Width pruning + KD recovery outperforms layer pruning + SFT on VLMs; 5% data recovers 95% performance; SFT+hidden-state distillation is optimal.\"\n    our_relation: \"Validates width pruning + recovery paradigm; our CKA-guided approach adds prediction of recoverability\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2604.24380\"\n\n  - id: hape_2026\n    title: \"HAP-E: Hessian-Aware Structured Pruning of LLMs for Efficient Inference\"\n    authors: \"\"\n    year: 2026\n    venue: \"ICLR 2026 (submitted)\"\n    category: background\n    role: \"Hessian-aware structured pruning with adaptive budget allocation\"\n    relevance: 5\n    key_finding: \"Adaptive cross-layer budget reallocation via global screening + OBS-equivalent batch pruning; up to 3% accuracy over SOTA structured pruning\"\n    our_relation: \"Alternative pruning backbone with second-order optimization; complementary to our CKA-guided selection\"\n    citation_priority: nice-to-have\n    arxiv_id: \"\"\n\n  - id: slimllm_2025\n    title: \"SlimLLM: Accurate Structured Pruning for Large Language Models\"\n    authors: \"Jialong Guo, Xinghao Chen, Yehui Tang, Yunhe Wang\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: background\n    role: \"Holistic channel/head importance evaluation with linear regression recovery\"\n    relevance: 5\n    key_finding: \"Evaluates importance of entire channels/heads holistically; non-uniform layer-based pruning ratio via cosine similarity; linear regression for fast recovery\"\n    our_relation: \"Alternative structured pruning metric; their cosine-based layer ratio is complementary to our CKA functional overlap\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2505.22689\"\n\n  - id: spap_2025\n    title: \"SPAP: Structured Pruning via Alternating Optimization and Penalty Methods\"\n    authors: \"\"\n    year: 2025\n    venue: \"arXiv May 2025\"\n    category: background\n    role: \"Optimization-theory-grounded MLP pruning\"\n    relevance: 5\n    key_finding: \"Mixed-integer formulation with relaxation guarantee; alternating minimization with closed-form updates; 1.29x speedup at 30% sparsity\"\n    our_relation: \"Could serve as alternative pruning backbone for MLP layers; operates at different abstraction level from our CKA selection\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2505.03373\"\n\n  - id: wandapp_2025\n    title: \"Wanda++: Pruning Large Language Models via Regional Gradients\"\n    authors: \"\"\n    year: 2025\n    venue: \"ACL 2025\"\n    category: background\n    role: \"Gradient-enhanced unstructured pruning\"\n    relevance: 4\n    key_finding: \"Regional gradients improve Wanda score by up to 32% perplexity reduction; regional optimization minimizes dense-sparse output discrepancy\"\n    our_relation: \"Unstructured pruning evolution; orthogonal to our structured approach but regional optimization idea could inform per-block CKA computation\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2503.04992\"\n\n  # === Must-cite gap fills (Step 3, 2026-05-18) ===\n  - id: llm_pruner_2023\n    title: \"LLM-Pruner: On the Structural Pruning of Large Language Models\"\n    authors: \"Xinyin Ma, Gongfan Fang, Xinchao Wang\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    category: method-component\n    role: \"Foundational structured pruning framework for LLMs using Taylor importance + dependency detection\"\n    relevance: 9\n    key_finding: \"First task-agnostic structured pruning for LLMs; dependency-aware group removal preserves model integrity; 20% pruning with minimal loss after LoRA recovery on LLaMA-7B/13B/30B\"\n    our_relation: \"Foundational baseline; our Taylor importance scoring (Standard method) directly builds on LLM-Pruner. We extend with CKA overlap and RLVR recovery\"\n    citation_priority: must-cite\n    arxiv_id: \"2305.11627\"\n    verified: true\n\n  - id: deepseekmath_grpo_2024\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo\"\n    year: 2024\n    venue: \"arXiv Feb 2024\"\n    category: background\n    role: \"GRPO algorithm origin — Group Relative Policy Optimization for math reasoning\"\n    relevance: 9\n    key_finding: \"Introduces GRPO: group-level reward normalization without critic model; DeepSeekMath-7B achieves 51.7% on MATH competition via GRPO + code-math corpus\"\n    our_relation: \"Our RLVR recovery phase uses GRPO as the alignment algorithm; this is the foundational reference\"\n    citation_priority: must-cite\n    arxiv_id: \"2402.03300\"\n    verified: true\n\n# === Update Log ===\n# 2026-05-15: Literature survey targeting 4 reviewer-flagged gaps\n#   Direction 1 (Structured pruning + RLVR recovery): Added RLRC, NIRVANA, free_lunch_retraining\n#   Direction 2 (CKA in pruning/NAS): Added davari_cka_reliability (must-cite), murphy_debiased_cka, tracenas\n#   Direction 3 (FANG/FuncNet): Confirmed details; added FNF as background\n#   Direction 4 (GraSP baselines): Added grasp_2020 (original), tracenas\n#   Updated: self_healing authors (Ji et al., ICLR 2026), from_llms_to_lrms (Ding et al., 2601.18091),\n#            mpruner (arxiv 2408.13482), slimllm authors, pruning_vlm_recovery authors\n#   Added citation_priority field (must-cite / should-cite / nice-to-have) to all entries\n",
    "structuredPatch": [
      {
        "oldStart": 616,
        "oldLines": 6,
        "newStart": 616,
        "newLines": 49,
        "lines": [
          "     arxiv_id: \"2402.03300\"",
          "     verified: true",
          " ",
          "+  # === RL Training Instability (added 2026-05-18) ===",
          "+  - id: gao_reward_overoptimization_2023",
          "+    title: \"Scaling Laws for Reward Model Overoptimization\"",
          "+    authors: \"Leo Gao, John Schulman, Jacob Hilton\"",
          "+    year: 2023",
          "+    venue: \"ICML 2023\"",
          "+    category: background",
          "+    role: \"RL training instability — reward overoptimization scaling laws\"",
          "+    relevance: 6",
          "+    key_finding: \"Proxy reward optimization degrades gold reward following predictable scaling laws; overoptimization worsens with more RL compute and smaller reward models\"",
          "+    our_relation: \"Pruning-induced collapse can be viewed as amplified reward overoptimization where reduced model capacity widens the proxy-gold reward gap\"",
          "+    citation_priority: should-cite",
          "+    arxiv_id: \"2210.10760\"",
          "+    verified: true",
          "+",
          "+  - id: rl_plus_collapse_2025",
          "+    title: \"RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization\"",
          "+    authors: \"Yihong Dong, Xue Jiang, Yongding Tao, Huanyu Liu, Kechi Zhang, Lili Mou, Rongyu Cao, Yingwei Ma, Jue Chen, Binhua Li, Zhi Jin, Fei Huang, Yongbin Li, Ge Li\"",
          "+    year: 2025",
          "+    venue: \"arXiv Jul 2025\"",
          "+    category: background",
          "+    role: \"RL training instability — capability boundary collapse in RLVR\"",
          "+    relevance: 7",
          "+    key_finding: \"RLVR causes capability boundary collapse: pass@1 improves but pass@k degrades, narrowing the model's problem-solving scope due to on-policy training with sparse reward\"",
          "+    our_relation: \"Pruning-induced collapse is a structural variant of capability boundary collapse; pruning removes capacity that exacerbates the on-policy sparse-reward instability they identify\"",
          "+    citation_priority: should-cite",
          "+    arxiv_id: \"2508.00222\"",
          "+    verified: true",
          "+",
          "+  - id: comedy_of_estimators_2025",
          "+    title: \"A Comedy of Estimators: On KL Regularization in RL Training of LLMs\"",
          "+    authors: \"Vedant Shah, Johan Obando-Ceron, Vineet Jain, Brian Bartoldson, Bhavya Kailkhura, Sarthak Mittal, Glen Berseth, Pablo Samuel Castro, Yoshua Bengio, Nikolay Malkin, Moksh Jain, Siddarth Venkatraman, Aaron Courville\"",
          "+    year: 2025",
          "+    venue: \"arXiv Dec 2025\"",
          "+    category: background",
          "+    role: \"RL training instability — KL regularization implementation pitfalls\"",
          "+    relevance: 5",
          "+    key_finding: \"Prevailing KL regularization implementations in RLHF/RLVR provide incorrect gradients for stated objectives, causing training instability and suboptimal performance\"",
          "+    our_relation: \"Informs our GRPO recovery design: incorrect KL estimation can destabilize RLVR recovery of pruned models, especially when pruning shifts the policy distribution\"",
          "+    citation_priority: should-cite",
          "+    arxiv_id: \"2512.21852\"",
          "+    verified: true",
          "+",
          " # === Update Log ===",
          " # 2026-05-15: Literature survey targeting 4 reviewer-flagged gaps",
          " #   Direction 1 (Structured pruning + RLVR recovery): Added RLRC, NIRVANA, free_lunch_retraining"
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

_source line 32_

Now adding the update log entry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "0a08b173-ee81-4c16-a107-6a41a65f4c6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HerJVumdxpqpYVkUYAc7Mz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3787,
      "cache_read_input_tokens": 44837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3787
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

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_01M65yzPH5kdD2sejyCCho1c`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml",
  "old_string": "# === Update Log ===\n# 2026-05-15: Literature survey targeting 4 reviewer-flagged gaps",
  "new_string": "# === Update Log ===\n# 2026-05-18: Added 3 RL training instability papers (background for pruning-induced collapse positioning)\n#   - gao_reward_overoptimization_2023: Reward overoptimization scaling laws (ICML 2023)\n#   - rl_plus_collapse_2025: Capability boundary collapse in RLVR (arXiv 2508.00222)\n#   - comedy_of_estimators_2025: KL regularization pitfalls in RL training (arXiv 2512.21852)\n# 2026-05-15: Literature survey targeting 4 reviewer-flagged gaps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "2a768b71-1826-4c3e-b5ec-da11370be0f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HerJVumdxpqpYVkUYAc7Mz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3787,
      "cache_read_input_tokens": 44837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3787
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

_source line 34 · 2026-05-18T03:16:38.747Z_

<details><summary>↩ Tool result · `toolu_01M65yzPH5kdD2sejyCCho1c`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "07bc1a47-0d54-42ba-b4e8-eef46cfe089c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml",
    "oldString": "# === Update Log ===\n# 2026-05-15: Literature survey targeting 4 reviewer-flagged gaps",
    "newString": "# === Update Log ===\n# 2026-05-18: Added 3 RL training instability papers (background for pruning-induced collapse positioning)\n#   - gao_reward_overoptimization_2023: Reward overoptimization scaling laws (ICML 2023)\n#   - rl_plus_collapse_2025: Capability boundary collapse in RLVR (arXiv 2508.00222)\n#   - comedy_of_estimators_2025: KL regularization pitfalls in RL training (arXiv 2512.21852)\n# 2026-05-15: Literature survey targeting 4 reviewer-flagged gaps",
    "originalFile": "papers:\n  # === Direct Competitors ===\n  - id: self_healing_2025\n    title: \"Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning\"\n    authors: \"Yixin Ji, Zhimin Lin, Juntao Li, Kaixin Wu, Kai Yao, Xu Jia, Linjian Mo, Min Zhang\"\n    year: 2025\n    venue: \"ICLR 2026 submission (OpenReview #12375, submitted Sep 2025)\"\n    category: direct-competitor\n    role: \"RLVR recovery baseline\"\n    relevance: 9\n    key_finding: \"RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%. Tested on 5 LRMs across 6 math benchmarks.\"\n    our_relation: \"We extend beyond single sparsity ratio and add CKA-guided pruning selection\"\n    citation_priority: must-cite\n    arxiv_id: \"\"\n\n  - id: resp_2025\n    title: \"RESP: Self-Reflective Structured Pruning for Reasoning LLMs\"\n    authors: \"\"\n    year: 2025\n    venue: \"arXiv Dec 2025\"\n    category: direct-competitor\n    role: \"Structured pruning for reasoning without recovery\"\n    relevance: 8\n    key_finding: \"GSM8K 81.3% at 40% sparsity via self-reflective importance\"\n    our_relation: \"No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity\"\n    citation_priority: must-cite\n    arxiv_id: \"2512.02185\"\n\n  - id: grasprune_2026\n    title: \"GRASPrune: Global Gating-based Structural Pruning for LLMs\"\n    authors: \"\"\n    year: 2026\n    venue: \"ACL 2026 Main\"\n    category: direct-competitor\n    role: \"SOTA budgeted structural pruning\"\n    relevance: 8\n    key_finding: \"Global gating achieves best structured pruning under budget constraints\"\n    our_relation: \"GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top\"\n    citation_priority: must-cite\n    arxiv_id: \"2604.19398\"\n\n  - id: opsd_2026\n    title: \"OPSD: One-shot Post-RL Structured Distillation\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv May 2026\"\n    category: direct-competitor\n    role: \"Post-RL compression via distillation\"\n    relevance: 7\n    key_finding: \"Compress post-RL model in one shot via structured distillation\"\n    our_relation: \"Distillation-based vs our pruning+recovery approach; complementary\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: doing_more_with_less_2026\n    title: \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: direct-competitor\n    role: \"Pruning improves test-time scaling\"\n    relevance: 7\n    key_finding: \"Unstructured pruning can augment test-time scaling; structured pruning degrades it\"\n    our_relation: \"Motivates why structured pruning needs recovery; we address this gap with RLVR\"\n    citation_priority: should-cite\n    arxiv_id: \"2604.25098\"\n\n  - id: gprune_llm_2026\n    title: \"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: direct-competitor\n    role: \"Cross-distribution generalization-aware pruning\"\n    relevance: 6\n    key_finding: \"Accounts for neuron cross-distribution behavior; reduces calibration bias\"\n    our_relation: \"Complementary importance metric; our CKA captures functional overlap vs their generalization gap\"\n    citation_priority: should-cite\n    arxiv_id: \"2603.13418\"\n\n  - id: boiling_frog_2026\n    title: \"Gradually Compacting Large Language Models for Reasoning Like a Boiling Frog\"\n    authors: \"Yiran Zhao, Shengyang Zhou, Zijian Wu, Tongyan Hu, Yuhui Xu, Rengan Dou, Kenji Kawaguchi, Shafiq Joty, Junnan Li, Michael Qizhe Shieh\"\n    year: 2026\n    venue: \"arXiv Feb 2026\"\n    category: direct-competitor\n    role: \"Iterative prune-tune loop for reasoning model compression\"\n    relevance: 7\n    key_finding: \"Gradual Prune-Tune Loop avoids abrupt performance collapse; iterative pruning+finetuning preserves reasoning\"\n    our_relation: \"Similar prune-then-recover paradigm but uses SFT recovery; we use RLVR which is more effective and add CKA-guided pruning selection\"\n    citation_priority: must-cite\n    arxiv_id: \"2602.04919\"\n\n  - id: think_prune_train_2025\n    title: \"Think, Prune, Train, Improve: Scaling Reasoning without Scaling Models\"\n    authors: \"Caia Costello, Simon Guo, Anna Goldie, Azalia Mirhoseini\"\n    year: 2025\n    venue: \"arXiv Apr 2025 (Stanford Scaling Intelligence Lab)\"\n    category: direct-competitor\n    role: \"Self-training on pruned reasoning traces to improve small models\"\n    relevance: 6\n    key_finding: \"Iterative fine-tuning on ground-truth-pruned reasoning traces; Gemma2-9B matches LLaMA-3.1-70B on GSM8K\"\n    our_relation: \"Complementary — prunes reasoning traces (CoT) not model weights; could combine with our weight pruning\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2504.18116\"\n\n  # === Method Components ===\n  - id: mpruner_2024\n    title: \"MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning\"\n    authors: \"\"\n    year: 2024\n    venue: \"arXiv Aug 2024\"\n    category: method-component\n    role: \"CKA for layer importance estimation\"\n    relevance: 8\n    key_finding: \"CKA similarity between layers identifies redundant layers for removal; 50% parameter reduction with minimal accuracy loss\"\n    our_relation: \"We adapt CKA from layer-level to width-level functional overlap prediction\"\n    citation_priority: must-cite\n    arxiv_id: \"2408.13482\"\n\n  - id: lachance_thesis_2024\n    title: \"Using Centered Kernel Alignment for Understanding and Pruning Neural Networks\"\n    authors: \"Lachance\"\n    year: 2024\n    venue: \"URI Master's Thesis\"\n    category: method-component\n    role: \"CKA-based pruning theoretical foundation\"\n    relevance: 6\n    key_finding: \"CKA layer similarity correlates with pruning recoverability\"\n    our_relation: \"Validates CKA as signal for pruning decisions; we extend to predict RLVR recovery\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: fang_2025\n    title: \"FANG: Improving Generalization in LLM Structured Pruning via Function-Aware Neuron Grouping\"\n    authors: \"Tao Yu, Yongqi An, Kuan Zhu, Guibo Zhu, Ming Tang, Jinqiao Wang\"\n    year: 2025\n    venue: \"arXiv Dec 2025\"\n    category: method-component\n    role: \"Function-aware neuron grouping for structured pruning\"\n    relevance: 7\n    key_finding: \"Groups FFN neurons by functional roles; shared neuron retention prevents cross-task accuracy loss; outperforms FLAP/OBC by 1.5-8.5% at 30-40% sparsity\"\n    our_relation: \"Closest conceptual parallel — both identify functionally critical neurons, but FANG uses activation-based grouping while we use CKA similarity; no recovery component\"\n    citation_priority: must-cite\n    arxiv_id: \"2512.23014\"\n\n  - id: funcnet_2025\n    title: \"Pruning Large Language Models by Identifying and Preserving Functional Networks\"\n    authors: \"Yiheng Liu, Junhao Ning, Sichen Xia, Xiaohui Gao, Ning Qiang, Bao Ge, Junwei Han, Xintao Hu\"\n    year: 2025\n    venue: \"arXiv Aug 2025\"\n    category: method-component\n    role: \"ICA-based functional network identification for pruning\"\n    relevance: 7\n    key_finding: \"Applies ICA (from neuroimaging) to decompose LLM into functional networks; preserves key neurons within identified networks\"\n    our_relation: \"Similar motivation — treat LLM as digital brain and preserve functional structure — but uses ICA vs our CKA; no RLVR recovery\"\n    citation_priority: must-cite\n    arxiv_id: \"2508.05239\"\n\n  - id: bonsai_2025\n    title: \"Bonsai: Gradient-Free Structured Pruning for LLMs\"\n    authors: \"\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: method-component\n    role: \"Gradient-free structured pruning alternative\"\n    relevance: 6\n    key_finding: \"Achieves competitive structured pruning without backprop\"\n    our_relation: \"Alternative pruning strategy; our CKA metric is also gradient-free\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: pat_2025\n    title: \"PAT: Pruning-Aware Tuning for Large Language Models\"\n    authors: \"Yijiang Liu et al.\"\n    year: 2025\n    venue: \"AAAI 2025\"\n    category: method-component\n    role: \"Joint pruning and tuning framework via Hybrid Sparsification Modules\"\n    relevance: 6\n    key_finding: \"Co-optimizing pruning mask and fine-tuning via HSMs; surpasses LoRA-64 by 1.26% at 25% pruning on Llama2-7B\"\n    our_relation: \"Related idea of pruning-tuning interaction; we separate pruning and RLVR recovery\"\n    citation_priority: should-cite\n    arxiv_id: \"2408.14721\"\n\n  - id: rac_2025\n    title: \"RAC: Chain-of-Thought Reconstruction for Pruned Reasoning Models\"\n    authors: \"\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    category: method-component\n    role: \"CoT reconstruction post-pruning\"\n    relevance: 7\n    key_finding: \"Reconstructing CoT improves unstructured/2:4 pruned reasoning models\"\n    our_relation: \"Complementary recovery strategy; could combine with our RLVR approach\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: paser_2025\n    title: \"PASER: Data Selection for Pruning Recovery\"\n    authors: \"\"\n    year: 2025\n    venue: \"under review\"\n    category: method-component\n    role: \"Recovery training data selection\"\n    relevance: 6\n    key_finding: \"Selective data for recovery training improves efficiency\"\n    our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"\n    citation_priority: nice-to-have\n    arxiv_id: \"\"\n\n  - id: dppo_2026\n    title: \"DPPO: Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Rollout pruning to accelerate GRPO training\"\n    relevance: 5\n    key_finding: \"Importance-sampling-based rollout pruning achieves 2.37x GRPO speedup with 3.36% accuracy gain on Qwen3-4B\"\n    our_relation: \"Could accelerate our GRPO-based RLVR recovery phase\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2603.04135\"\n\n  - id: arrol_2026\n    title: \"ARRoL: Prune as You Generate — Online Rollout Pruning for Faster and Better RLVR\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Online rollout pruning for RLVR efficiency\"\n    relevance: 5\n    key_finding: \"Lightweight quality head predicts rollout success probability for early pruning during RLVR\"\n    our_relation: \"Complementary technique for speeding up RLVR recovery training\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2603.24840\"\n\n  - id: restorelcc_2025\n    title: \"RestoreLCC: Restoring Pruned Large Language Models via Lost Component Compensation\"\n    authors: \"Zijian Feng, Hanzhang Zhou, Zixiao Zhu, Tianjiao Li, Jia Jim Deryl Chua, Lee Onn Mak, Gee Wah Ng, Kezhi Mao\"\n    year: 2025\n    venue: \"NeurIPS 2025 (Spotlight, top 10%)\"\n    category: method-component\n    role: \"Plug-and-play pruning recovery via activation compensation\"\n    relevance: 6\n    key_finding: \"Contrastively probes critical attention heads, extracts lost components from activation differences, injects them back; +1.25-2.65% over SOTA baselines across structured/unstructured pruning\"\n    our_relation: \"Alternative recovery paradigm (activation editing vs RLVR); could be complementary — apply RestoreLCC before RLVR for staged recovery\"\n    citation_priority: should-cite\n    arxiv_id: \"2510.21834\"\n\n  - id: fastforward_2025\n    title: \"FastForward Pruning: Efficient LLM Pruning via Single-Step Reinforcement Learning\"\n    authors: \"\"\n    year: 2025\n    venue: \"arXiv Nov 2025\"\n    category: method-component\n    role: \"RL-based non-uniform sparsity allocation for LLM pruning\"\n    relevance: 5\n    key_finding: \"Decoupled single-step RL framework separates policy optimization from budget satisfaction; efficient non-uniform layer-wise sparsity search\"\n    our_relation: \"Uses RL for pruning decisions (not recovery); complementary — could combine their RL sparsity allocation with our CKA-guided selection\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2511.18977\"\n\n  - id: nirvana_2025\n    title: \"NIRVANA: Structured Pruning Reimagined for Large Language Models Compression\"\n    authors: \"Mengting Ai, Tianxin Wei, Sirui Chen, Jingrui He\"\n    year: 2025\n    venue: \"arXiv Sep 2025\"\n    category: method-component\n    role: \"NTK-based saliency with adaptive sparsity allocation\"\n    relevance: 6\n    key_finding: \"First-order saliency from Neural Tangent Kernel under Adam dynamics; adaptive cross-module sparsity; KL-based calibration data selection. Outperforms SOTA on Llama3/Qwen/T5.\"\n    our_relation: \"Strong pruning baseline; their NTK saliency is complementary to our CKA functional overlap — could combine both signals\"\n    citation_priority: should-cite\n    arxiv_id: \"2509.14230\"\n\n  - id: tracenas_2026\n    title: \"TraceNAS: Zero-shot LLM Pruning via Gradient Trace Correlation\"\n    authors: \"Prajna G. Malettira, Manish Nagaraj, Arjun Roy, Shubham Negi, Kaushik Roy\"\n    year: 2026\n    venue: \"arXiv Feb 2026\"\n    category: method-component\n    role: \"Gradient trace for joint depth+width NAS-style pruning\"\n    relevance: 6\n    key_finding: \"Scale-invariant gradient trace correlation as proxy for pruned architecture quality; joint depth+width search on single GPU in 8.5h; competitive with training-intensive methods on Llama/Qwen\"\n    our_relation: \"Related NAS-for-pruning approach; their gradient trace could complement our CKA as alternative architecture quality proxy\"\n    citation_priority: should-cite\n    arxiv_id: \"2602.02891\"\n\n  - id: rlrc_2025\n    title: \"RLRC: Reinforcement Learning-based Recovery for Compressed Vision-Language-Action Models\"\n    authors: \"Yuxuan Chen, Xiao Li\"\n    year: 2025\n    venue: \"arXiv Jun 2025\"\n    category: method-component\n    role: \"RL-based recovery for compressed VLA models (robotics)\"\n    relevance: 6\n    key_finding: \"Three-stage: structured pruning → SFT+RL recovery → quantization. 8x memory reduction, 2.3x throughput, maintains/surpasses original task success.\"\n    our_relation: \"Extends RL recovery paradigm to robotics VLAs; validates that RL recovery generalizes beyond language-only models. Parallel evidence for our RLVR recovery hypothesis.\"\n    citation_priority: should-cite\n    arxiv_id: \"2506.17639\"\n\n  # === Background / Theory ===\n  - id: kornblith_cka_2019\n    title: \"Similarity of Neural Network Representations Revisited\"\n    authors: \"Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton\"\n    year: 2019\n    venue: \"ICML 2019\"\n    category: background\n    role: \"CKA original paper — foundational method for our functional overlap metric\"\n    relevance: 9\n    key_finding: \"CKA achieves 99.3% accuracy in identifying corresponding layers across different initializations; CCA/SVCCA only 1.4-45.4%. Invariant to orthogonal transform and isotropic scaling.\"\n    our_relation: \"Foundational method — our CKA-guided pruning directly builds on this. Key justification: CKA >> CCA/SVCCA for reliable layer correspondence\"\n    citation_priority: must-cite\n    arxiv_id: \"1905.00414\"\n\n  - id: davari_cka_reliability_2023\n    title: \"Reliability of CKA as a Similarity Measure in Deep Learning\"\n    authors: \"MohammadReza Davari, Stefan Horoi, Amine Natik, Guillaume Lajoie, Guy Wolf, Eugene Belilovsky\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    category: background\n    role: \"CKA limitations and failure modes — essential for honest CKA justification\"\n    relevance: 7\n    key_finding: \"CKA is sensitive to outliers and simple transformations preserving linear separability; CKA values can be manipulated without changing functional behavior. Calls for caution.\"\n    our_relation: \"Must-cite for CKA justification section. We should acknowledge limitations and explain why they don't invalidate our use case (intra-model layer comparison, not cross-model with different transformations).\"\n    citation_priority: must-cite\n    arxiv_id: \"2210.16156\"\n\n  - id: murphy_debiased_cka_2024\n    title: \"Correcting Biased Centered Kernel Alignment Measures in Biological and Artificial Neural Networks\"\n    authors: \"Alex Murphy, Joel Zylberberg, Alona Fyshe\"\n    year: 2024\n    venue: \"ICLR 2024 Re-Align Workshop\"\n    category: background\n    role: \"Debiased CKA for high-dimensionality settings\"\n    relevance: 5\n    key_finding: \"Biased CKA gives misleadingly high similarity when feature-sample ratio is skewed; debiased CKA corrects this. Shuffled data doesn't change biased CKA scores.\"\n    our_relation: \"Nice-to-have citation. Our setting (same model, same data) is less affected by this bias, but worth mentioning in limitations.\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2405.01012\"\n\n  - id: raghu_svcca_2017\n    title: \"SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability\"\n    authors: \"Maithra Raghu, Justin Gilmer, Jason Yosinski, Jascha Sohl-Dickstein\"\n    year: 2017\n    venue: \"NeurIPS 2017\"\n    category: background\n    role: \"SVCCA — predecessor to CKA, baseline representation similarity method\"\n    relevance: 5\n    key_finding: \"SVD dimensionality reduction + CCA for comparing representations; reveals bottom-up convergence dynamics and intrinsic dimensionality\"\n    our_relation: \"CKA alternative baseline. SVCCA lacks invariance to isotropic scaling and fails at cross-network layer identification (only 45% accuracy vs CKA's 99%)\"\n    citation_priority: should-cite\n    arxiv_id: \"1706.05806\"\n\n  - id: klabunde_similarity_survey_2025\n    title: \"Similarity of Neural Network Models: A Survey of Functional and Representational Measures\"\n    authors: \"Max Klabunde, Tobias Schumacher, Markus Strohmaier, Florian Lemmerich\"\n    year: 2025\n    venue: \"ACM Computing Surveys, Vol. 57, Issue 9\"\n    category: background\n    role: \"Comprehensive survey of representation similarity measures including CKA, CCA, SVCCA, PWCCA\"\n    relevance: 7\n    key_finding: \"First comprehensive review comparing representational vs functional similarity; covers CKA properties, robustness, and practical applications including pruning\"\n    our_relation: \"Key citation for CKA justification — survey confirms CKA's advantages over alternatives for model analysis and compression\"\n    citation_priority: must-cite\n    arxiv_id: \"2305.06329\"\n\n  - id: mipp_2024\n    title: \"MIPP: Mutual Information Preserving Neural Network Pruning\"\n    authors: \"\"\n    year: 2024\n    venue: \"arXiv Nov 2024\"\n    category: background\n    role: \"Information-theoretic pruning criterion — MI alternative to CKA\"\n    relevance: 5\n    key_finding: \"Structured activation-based pruning conserving MI between adjacent layers; sample efficiency proportional to MI between masks and data\"\n    our_relation: \"MI is a viable alternative but computationally expensive in high dimensions and less stable than CKA. Supports functional similarity matters for pruning.\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2411.00147\"\n\n  - id: rl_squeezes_2026\n    title: \"RL Squeezes, SFT Expands: Different Mechanisms in Post-Training\"\n    authors: \"\"\n    year: 2026\n    venue: \"ICLR 2026 Poster\"\n    category: background\n    role: \"Theoretical basis for why RLVR works differently from SFT\"\n    relevance: 8\n    key_finding: \"RLVR compresses representation while SFT expands; different inductive biases\"\n    our_relation: \"Explains why RLVR recovery succeeds where SFT fails post-pruning\"\n    citation_priority: must-cite\n    arxiv_id: \"\"\n\n  - id: from_llms_to_lrms_2026\n    title: \"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models\"\n    authors: \"Longwei Ding, Anhao Zhao, Fanghua Ye, Ziyang Chen, Xiaoyu Shen\"\n    year: 2026\n    venue: \"arXiv Jan 2026\"\n    category: background\n    role: \"Width vs depth pruning for reasoning models\"\n    relevance: 7\n    key_finding: \"Width pruning preserves reasoning better than depth pruning; static pruning > dynamic for long-chain reasoning; recovery relies on distribution-aligned post-fine-tuning, not calibration data.\"\n    our_relation: \"Motivates our focus on width-level structured pruning; validates that reasoning models need specialized pruning strategies\"\n    citation_priority: must-cite\n    arxiv_id: \"2601.18091\"\n\n  - id: p2_law_2025\n    title: \"P2 Law: Scaling Law for Pruning Recovery Training\"\n    authors: \"\"\n    year: 2025\n    venue: \"ACL 2025\"\n    category: background\n    role: \"Theoretical scaling of recovery compute\"\n    relevance: 7\n    key_finding: \"Recovery training follows predictable scaling with compute and data\"\n    our_relation: \"Informs our recovery budget estimation; we extend to RLVR-specific scaling\"\n    citation_priority: should-cite\n    arxiv_id: \"\"\n\n  - id: free_lunch_retraining_2025\n    title: \"A Free Lunch in LLM Compression: Revisiting Retraining after Pruning\"\n    authors: \"Moritz Wagner, Christophe Roux, Max Zimmer, Sebastian Pokutta\"\n    year: 2025\n    venue: \"arXiv Oct 2025 (revised Feb 2026)\"\n    category: background\n    role: \"Local reconstruction as efficient post-pruning recovery\"\n    relevance: 6\n    key_finding: \"Local reconstruction matches sophisticated PEFT recovery with >10x less data/compute. Pruning method matters less as model size grows.\"\n    our_relation: \"Shows cheap recovery can work — but their SFT-based reconstruction has ceiling; our RLVR recovery pushes beyond that ceiling for reasoning tasks.\"\n    citation_priority: should-cite\n    arxiv_id: \"2510.14444\"\n\n  - id: grasp_2020\n    title: \"Picking Winning Tickets Before Training by Preserving Gradient Flow\"\n    authors: \"Chaoqi Wang, Guodong Zhang, Roger Grosse\"\n    year: 2020\n    venue: \"ICLR 2020\"\n    category: background\n    role: \"GraSP — gradient signal preservation for pruning at initialization\"\n    relevance: 5\n    key_finding: \"Hessian-gradient product preserves gradient flow post-pruning; 80% VGG-16 pruning with only 1.6% top-1 drop on ImageNet; outperforms SNIP by 4-6% at high sparsity.\"\n    our_relation: \"Classic baseline for gradient-based importance. GRASPrune extends this idea to LLMs; our CKA operates at functional level rather than gradient flow.\"\n    citation_priority: should-cite\n    arxiv_id: \"2002.07376\"\n\n  - id: fnf_2026\n    title: \"FNF: Functional Network Fingerprint for Large Language Models\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Jan 2026\"\n    category: background\n    role: \"Functional network concept applied to LLM identification\"\n    relevance: 4\n    key_finding: \"Co-activating neuron groups form consistent functional networks; robust to model obfuscation.\"\n    our_relation: \"Validates the 'functional network' framing we share with FANG/FuncNet; extends concept to model fingerprinting.\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2601.22692\"\n\n  - id: redundancy_aware_cnn_2020\n    title: \"Redundancy-Aware Pruning of Convolutional Neural Networks\"\n    authors: \"\"\n    year: 2020\n    venue: \"Neural Computation\"\n    category: background\n    role: \"Pioneer of redundancy-based pruning\"\n    relevance: 4\n    key_finding: \"Redundancy metrics guide pruning decisions in CNNs\"\n    our_relation: \"Conceptual ancestor; we apply redundancy-awareness to LLM structured pruning\"\n    citation_priority: nice-to-have\n    arxiv_id: \"\"\n\n  - id: self_distilled_rlvr_2026\n    title: \"Self-Distilled RLVR\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"RLVR training efficiency improvement\"\n    relevance: 5\n    key_finding: \"Self-distillation stabilizes RLVR training and improves sample efficiency\"\n    our_relation: \"Could improve our RLVR recovery phase efficiency\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2604.03128\"\n\n  - id: diet_2026\n    title: \"DieT: Dimension-wise Global Pruning via Task-specific Importance Score\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: background\n    role: \"Dimension-wise importance for width pruning\"\n    relevance: 5\n    key_finding: \"Task-specific dimension importance outperforms activation-based metrics at 20-40% sparsity\"\n    our_relation: \"Alternative width importance metric; we use CKA overlap instead\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2603.23985\"\n\n  - id: task_neurons_2026\n    title: \"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific LLMs\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"Task-specific neuron identification and pruning recovery dynamics\"\n    relevance: 6\n    key_finding: \"10% task-specific neuron removal causes collapse; 15-20% robustness threshold; fine-tuning substantially recovers\"\n    our_relation: \"Supports need for recovery-aware pruning; our CKA predicts which neurons are functionally critical\"\n    citation_priority: should-cite\n    arxiv_id: \"2604.27115\"\n\n  - id: ddp_2026\n    title: \"DDP: Deterministic Differentiable Structured Pruning for Large Language Models\"\n    authors: \"\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: background\n    role: \"Differentiable mask-only structured pruning\"\n    relevance: 5\n    key_finding: \"Deterministic soft surrogate of l0 constraint eliminates train-test mismatch in differentiable pruning\"\n    our_relation: \"Alternative pruning backbone; mask-only optimization complementary to our CKA-guided selection\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2603.08065\"\n\n  - id: pruning_vlm_recovery_2026\n    title: \"Structural Pruning of Large Vision Language Models: Pruning Dynamics, Recovery, and Data Efficiency\"\n    authors: \"Yiran Huang, Lukas Thede, Massimiliano Mancini, Wenjia Xu, Zeynep Akata\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"Comprehensive pruning + recovery study for VLMs\"\n    relevance: 5\n    key_finding: \"Width pruning + KD recovery outperforms layer pruning + SFT on VLMs; 5% data recovers 95% performance; SFT+hidden-state distillation is optimal.\"\n    our_relation: \"Validates width pruning + recovery paradigm; our CKA-guided approach adds prediction of recoverability\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2604.24380\"\n\n  - id: hape_2026\n    title: \"HAP-E: Hessian-Aware Structured Pruning of LLMs for Efficient Inference\"\n    authors: \"\"\n    year: 2026\n    venue: \"ICLR 2026 (submitted)\"\n    category: background\n    role: \"Hessian-aware structured pruning with adaptive budget allocation\"\n    relevance: 5\n    key_finding: \"Adaptive cross-layer budget reallocation via global screening + OBS-equivalent batch pruning; up to 3% accuracy over SOTA structured pruning\"\n    our_relation: \"Alternative pruning backbone with second-order optimization; complementary to our CKA-guided selection\"\n    citation_priority: nice-to-have\n    arxiv_id: \"\"\n\n  - id: slimllm_2025\n    title: \"SlimLLM: Accurate Structured Pruning for Large Language Models\"\n    authors: \"Jialong Guo, Xinghao Chen, Yehui Tang, Yunhe Wang\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: background\n    role: \"Holistic channel/head importance evaluation with linear regression recovery\"\n    relevance: 5\n    key_finding: \"Evaluates importance of entire channels/heads holistically; non-uniform layer-based pruning ratio via cosine similarity; linear regression for fast recovery\"\n    our_relation: \"Alternative structured pruning metric; their cosine-based layer ratio is complementary to our CKA functional overlap\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2505.22689\"\n\n  - id: spap_2025\n    title: \"SPAP: Structured Pruning via Alternating Optimization and Penalty Methods\"\n    authors: \"\"\n    year: 2025\n    venue: \"arXiv May 2025\"\n    category: background\n    role: \"Optimization-theory-grounded MLP pruning\"\n    relevance: 5\n    key_finding: \"Mixed-integer formulation with relaxation guarantee; alternating minimization with closed-form updates; 1.29x speedup at 30% sparsity\"\n    our_relation: \"Could serve as alternative pruning backbone for MLP layers; operates at different abstraction level from our CKA selection\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2505.03373\"\n\n  - id: wandapp_2025\n    title: \"Wanda++: Pruning Large Language Models via Regional Gradients\"\n    authors: \"\"\n    year: 2025\n    venue: \"ACL 2025\"\n    category: background\n    role: \"Gradient-enhanced unstructured pruning\"\n    relevance: 4\n    key_finding: \"Regional gradients improve Wanda score by up to 32% perplexity reduction; regional optimization minimizes dense-sparse output discrepancy\"\n    our_relation: \"Unstructured pruning evolution; orthogonal to our structured approach but regional optimization idea could inform per-block CKA computation\"\n    citation_priority: nice-to-have\n    arxiv_id: \"2503.04992\"\n\n  # === Must-cite gap fills (Step 3, 2026-05-18) ===\n  - id: llm_pruner_2023\n    title: \"LLM-Pruner: On the Structural Pruning of Large Language Models\"\n    authors: \"Xinyin Ma, Gongfan Fang, Xinchao Wang\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    category: method-component\n    role: \"Foundational structured pruning framework for LLMs using Taylor importance + dependency detection\"\n    relevance: 9\n    key_finding: \"First task-agnostic structured pruning for LLMs; dependency-aware group removal preserves model integrity; 20% pruning with minimal loss after LoRA recovery on LLaMA-7B/13B/30B\"\n    our_relation: \"Foundational baseline; our Taylor importance scoring (Standard method) directly builds on LLM-Pruner. We extend with CKA overlap and RLVR recovery\"\n    citation_priority: must-cite\n    arxiv_id: \"2305.11627\"\n    verified: true\n\n  - id: deepseekmath_grpo_2024\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo\"\n    year: 2024\n    venue: \"arXiv Feb 2024\"\n    category: background\n    role: \"GRPO algorithm origin — Group Relative Policy Optimization for math reasoning\"\n    relevance: 9\n    key_finding: \"Introduces GRPO: group-level reward normalization without critic model; DeepSeekMath-7B achieves 51.7% on MATH competition via GRPO + code-math corpus\"\n    our_relation: \"Our RLVR recovery phase uses GRPO as the alignment algorithm; this is the foundational reference\"\n    citation_priority: must-cite\n    arxiv_id: \"2402.03300\"\n    verified: true\n\n  # === RL Training Instability (added 2026-05-18) ===\n  - id: gao_reward_overoptimization_2023\n    title: \"Scaling Laws for Reward Model Overoptimization\"\n    authors: \"Leo Gao, John Schulman, Jacob Hilton\"\n    year: 2023\n    venue: \"ICML 2023\"\n    category: background\n    role: \"RL training instability — reward overoptimization scaling laws\"\n    relevance: 6\n    key_finding: \"Proxy reward optimization degrades gold reward following predictable scaling laws; overoptimization worsens with more RL compute and smaller reward models\"\n    our_relation: \"Pruning-induced collapse can be viewed as amplified reward overoptimization where reduced model capacity widens the proxy-gold reward gap\"\n    citation_priority: should-cite\n    arxiv_id: \"2210.10760\"\n    verified: true\n\n  - id: rl_plus_collapse_2025\n    title: \"RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization\"\n    authors: \"Yihong Dong, Xue Jiang, Yongding Tao, Huanyu Liu, Kechi Zhang, Lili Mou, Rongyu Cao, Yingwei Ma, Jue Chen, Binhua Li, Zhi Jin, Fei Huang, Yongbin Li, Ge Li\"\n    year: 2025\n    venue: \"arXiv Jul 2025\"\n    category: background\n    role: \"RL training instability — capability boundary collapse in RLVR\"\n    relevance: 7\n    key_finding: \"RLVR causes capability boundary collapse: pass@1 improves but pass@k degrades, narrowing the model's problem-solving scope due to on-policy training with sparse reward\"\n    our_relation: \"Pruning-induced collapse is a structural variant of capability boundary collapse; pruning removes capacity that exacerbates the on-policy sparse-reward instability they identify\"\n    citation_priority: should-cite\n    arxiv_id: \"2508.00222\"\n    verified: true\n\n  - id: comedy_of_estimators_2025\n    title: \"A Comedy of Estimators: On KL Regularization in RL Training of LLMs\"\n    authors: \"Vedant Shah, Johan Obando-Ceron, Vineet Jain, Brian Bartoldson, Bhavya Kailkhura, Sarthak Mittal, Glen Berseth, Pablo Samuel Castro, Yoshua Bengio, Nikolay Malkin, Moksh Jain, Siddarth Venkatraman, Aaron Courville\"\n    year: 2025\n    venue: \"arXiv Dec 2025\"\n    category: background\n    role: \"RL training instability — KL regularization implementation pitfalls\"\n    relevance: 5\n    key_finding: \"Prevailing KL regularization implementations in RLHF/RLVR provide incorrect gradients for stated objectives, causing training instability and suboptimal performance\"\n    our_relation: \"Informs our GRPO recovery design: incorrect KL estimation can destabilize RLVR recovery of pruned models, especially when pruning shifts the policy distribution\"\n    citation_priority: should-cite\n    arxiv_id: \"2512.21852\"\n    verified: true\n\n# === Update Log ===\n# 2026-05-15: Literature survey targeting 4 reviewer-flagged gaps\n#   Direction 1 (Structured pruning + RLVR recovery): Added RLRC, NIRVANA, free_lunch_retraining\n#   Direction 2 (CKA in pruning/NAS): Added davari_cka_reliability (must-cite), murphy_debiased_cka, tracenas\n#   Direction 3 (FANG/FuncNet): Confirmed details; added FNF as background\n#   Direction 4 (GraSP baselines): Added grasp_2020 (original), tracenas\n#   Updated: self_healing authors (Ji et al., ICLR 2026), from_llms_to_lrms (Ding et al., 2601.18091),\n#            mpruner (arxiv 2408.13482), slimllm authors, pruning_vlm_recovery authors\n#   Added citation_priority field (must-cite / should-cite / nice-to-have) to all entries\n",
    "structuredPatch": [
      {
        "oldStart": 660,
        "oldLines": 6,
        "newStart": 660,
        "newLines": 10,
        "lines": [
          "     verified: true",
          " ",
          " # === Update Log ===",
          "+# 2026-05-18: Added 3 RL training instability papers (background for pruning-induced collapse positioning)",
          "+#   - gao_reward_overoptimization_2023: Reward overoptimization scaling laws (ICML 2023)",
          "+#   - rl_plus_collapse_2025: Capability boundary collapse in RLVR (arXiv 2508.00222)",
          "+#   - comedy_of_estimators_2025: KL regularization pitfalls in RL training (arXiv 2512.21852)",
          " # 2026-05-15: Literature survey targeting 4 reviewer-flagged gaps",
          " #   Direction 1 (Structured pruning + RLVR recovery): Added RLRC, NIRVANA, free_lunch_retraining",
          " #   Direction 2 (CKA in pruning/NAS): Added davari_cka_reliability (must-cite), murphy_debiased_cka, tracenas"
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

_source line 35_

已添加 3 篇 RL 训练不稳定性论文：

1. **gao_reward_overoptimization_2023** — Gao, Schulman, Hilton (ICML 2023, `2210.10760`). Reward overoptimization 的 scaling laws，奠基性工作。与我们的关系：pruning 降低模型容量可放大 proxy-gold reward gap。

2. **rl_plus_collapse_2025** — Dong et al. (arXiv `2508.00222`). RLVR 导致 capability boundary collapse（pass@1 升但 pass@k 降）。与我们的关系：pruning-induced collapse 是其结构性变体，剪枝移除的容量加剧了 on-policy sparse-reward 不稳定性。

3. **comedy_of_estimators_2025** — Shah, Bengio, Courville et al. (arXiv `2512.21852`). KL regularization 实现中梯度计算错误导致训练不稳定。与我们的关系：剪枝后 policy distribution 偏移时，KL 估计误差对 RLVR recovery 稳定性的影响。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "uuid": "39ffd783-adb1-4cca-903f-4d88bbba1717",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zwo9BRiVJ26yjQMmSdAzj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 393,
      "cache_read_input_tokens": 48624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 393
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

_source line 36_

已添加 3 篇 RL 训练不稳定性论文：

1. **gao_reward_overoptimization_2023** — Gao, Schulman, Hilton (ICML 2023, `2210.10760`). Reward overoptimization 的 scaling laws，奠基性工作。与我们的关系：pruning 降低模型容量可放大 proxy-gold reward gap。

2. **rl_plus_collapse_2025** — Dong et al. (arXiv `2508.00222`). RLVR 导致 capability boundary collapse（pass@1 升但 pass@k 降）。与我们的关系：pruning-induced collapse 是其结构性变体，剪枝移除的容量加剧了 on-policy sparse-reward 不稳定性。

3. **comedy_of_estimators_2025** — Shah, Bengio, Courville et al. (arXiv `2512.21852`). KL regularization 实现中梯度计算错误导致训练不稳定。与我们的关系：剪枝后 policy distribution 偏移时，KL 估计误差对 RLVR recovery 稳定性的影响。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 103827,
  "duration_api_ms": 139980,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "309d620c-950c-4540-b56d-67840476ff39",
  "total_cost_usd": 0.6812579999999999,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 37176,
    "cache_read_input_tokens": 203180,
    "output_tokens": 5112,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37176,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 330,
        "cache_read_input_tokens": 48624,
        "cache_creation_input_tokens": 393,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 393
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 130503,
      "outputTokens": 3794,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 7,
      "costUSD": 0.219473,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 5112,
      "cacheReadInputTokens": 203180,
      "cacheCreationInputTokens": 37176,
      "webSearchRequests": 0,
      "costUSD": 0.461785,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "90f5927c-59cd-4148-9221-a193408f76c5"
}
```

</details>

---
