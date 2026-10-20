# paper research

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_research_20260515T032801.log`
- **Structured JSON:** [`ce26a5242097bcd6412c.json`](../../sessions/ce/ce26a5242097bcd6412c.json)

## Before a recorded user message

26 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
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
  "uuid": "09772f79-6f0f-4ed1-9efe-f5ecad47be16",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/memory/"
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
    "resetsAt": 1778826600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b8430f82-49d3-4081-8f15-e4a85c70ba36",
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to search for 3 papers, verify their metadata, and update a literature_map.yaml file. Let me start by searching for the papers and reading the existing file in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "4b032cfe-1ff6-4182-a1ae-fe17095341e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176fHqn6Z5vLEZNy1BkKiH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12274,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12274
      },
      "output_tokens": 35,
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

搜索三篇论文并读取现有文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "75114150-ffaf-4437-90f7-71486c19adb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176fHqn6Z5vLEZNy1BkKiH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12274,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12274
      },
      "output_tokens": 35,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019YLr4RfNKqGPzm9xSKkLqq`</summary>

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
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "15daa4a9-1041-4095-b267-cb2e55ad15d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176fHqn6Z5vLEZNy1BkKiH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12274,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12274
      },
      "output_tokens": 35,
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

_source line 7 · 2026-05-15T03:28:11.075Z_

<details><summary>↩ Tool result · `toolu_019YLr4RfNKqGPzm9xSKkLqq`</summary>

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
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "80cb95d6-08d0-4c82-975b-6af2796b635d",
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01Xz3ikmknbPkPXxn8G8JcE9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "d0c65a63-3175-45b9-bf51-31ab8a3e2635",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176fHqn6Z5vLEZNy1BkKiH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12274,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12274
      },
      "output_tokens": 35,
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

_source line 9 · 2026-05-15T03:28:11.531Z_

<details><summary>↩ Tool result · `toolu_01Xz3ikmknbPkPXxn8G8JcE9`</summary>

```text
1	# Literature Map: Dose-Response / Threshold Effects in Data Augmentation
2	# Updated: 2026-05-15
3	
4	entries:
5	  # === Category: dose-response / threshold ===
6	
7	  - id: rolnick2017robust
8	    title: "Deep Learning is Robust to Massive Label Noise"
9	    authors: "Rolnick, Veit, Belongie, Shavit"
10	    year: 2017
11	    venue: arXiv 1705.10694
12	    category: dose-response
13	    role: background
14	    key_finding: "DNNs maintain >90% accuracy on MNIST even when correct labels are diluted 100:1, as long as correct label remains most likely by a small margin."
15	    relevance: "Contrasts with our finding: image classification is robust to extreme noise, while embodied planning shows sharp degradation at 25%. Task complexity mediates noise tolerance."
16	
17	  - id: yuan2024early_stopping
18	    title: "Early Stopping Against Label Noise Without Validation Data"
19	    authors: "Yuan, Feng, Liu"
20	    year: 2024
21	    venue: ICLR 2024
22	    category: dose-response
23	    role: background
24	    key_finding: "Identifies phase transition where DNNs shift from fitting clean to fitting mislabeled examples. Proposes Label Wave to detect this transition during training."
25	    relevance: "Supports existence of phase transition in learning dynamics. Our 10-25% threshold may correspond to such a transition point in the SFT regime."
26	
27	  - id: dohmatob2025collapse
28	    title: "Strong Model Collapse"
29	    authors: "Dohmatob, Feng, Subramonian, Kempe"
30	    year: 2025
31	    venue: ICLR 2025
32	    category: threshold
33	    role: background
34	    key_finding: "Even 0.1% synthetic data can cause model collapse in supervised regression. Past interpolation threshold, larger models become more robust (double-descent)."
35	    relevance: "Demonstrates extreme sensitivity to data quality in certain regimes. Our 10-25% threshold is analogous—small quality shifts cause nonlinear degradation."
36	
37	  - id: beyond_clean_data2024
38	    title: "Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance"
39	    authors: "Various"
40	    year: 2024
41	    venue: ScienceDirect
42	    category: dose-response
43	    role: background
44	    key_finding: "Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds."
45	    relevance: "Methodologically similar—varies noise proportion to find degradation curves. Shows task-specific threshold behavior."
46	
47	  # === Category: error-injection / failure augmentation ===
48	
49	  - id: wang2024learning_from_failure
50	    title: "Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents"
51	    authors: "Wang, Li, Han, Zhang, Baldwin"
52	    year: 2024
53	    venue: arXiv 2402.11651
54	    category: error-injection
55	    role: evaluation
56	    key_finding: "Failed trajectories provide valuable signal for LLM agents via contrastive learning. Negative examples improve math, QA, strategic tasks when properly structured."
57	    relevance: "Directly related—injects negative trajectories into agent SFT. Key difference: they use contrastive framing, not raw mixing. Our work shows raw mixing has narrow safe window."
58	
59	  - id: song2024eto
60	    title: "Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents"
61	    authors: "Song, Yin, Yue, Huang, Li, Lin"
62	    year: 2024
63	    venue: ACL 2024
64	    category: error-injection
65	    role: evaluation
66	    key_finding: "Iteratively collects failure trajectories, uses DPO-style contrastive learning on success-failure pairs. +8% WebShop, +9.5% ScienceWorld vs SFT."
67	    relevance: "Uses failure trajectories via preference optimization (DPO), not direct SFT mixing. Avoids our threshold problem by never training directly on failures."
68	
69	  - id: paladin2025
70	    title: "PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases"
71	    authors: "Vuddanti, Shah et al."
72	    year: 2025
73	    venue: arXiv 2509.25238
74	    category: error-injection
75	    role: evaluation
76	    key_finding: "Trains on 50K+ recovery-annotated failure trajectories via LoRA. +57pp recovery rate vs vanilla (32.76%→89.68%), +13.6pp vs CRITIC baseline. Taxonomy of 7 error classes. Includes inference-time retrieval."
77	    relevance: "Most similar to our approach (taxonomy-guided error injection). Key difference: they pair failures with recovery demos; we inject standalone error trajectories."
78	
79	  - id: agentHER2025
80	    title: "AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling"
81	    authors: "Various"
82	    year: 2025
83	    venue: arXiv 2603.21357
84	    category: error-injection
85	    role: evaluation
86	    key_finding: "Converts failed trajectories to valid training data by relabeling—failure for task A becomes success for task B."
87	    relevance: "Avoids noise problem by redefining failure as success for different goals. Contrasts with our direct injection approach."
88	
89	  # === Category: data-mixing ===
90	
91	  - id: dong2024composition
92	    title: "How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition"
93	    authors: "Dong, Yuan et al."
94	    year: 2024
95	    venue: ACL 2024
96	    category: data-mixing
97	    role: background
98	    key_finding: "Data amount per domain matters more than ratio. Low-data mixing enables cross-domain transfer; high-data mixing causes ability conflicts."
99	    relevance: "Documents ability-conflict at high data amounts—analogous to our threshold. Ratio secondary to amount suggests our threshold may be absolute-count driven."
100	
101	  - id: ye2025mixing_laws
102	    title: "Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance"
103	    authors: "Ye et al."
104	    year: 2025
105	    venue: ICLR 2025
106	    category: data-mixing
107	    role: background
108	    key_finding: "Discovers quantitative scaling laws L=f(r) for mixture proportions. Accurately predicts critical proportion avoiding catastrophic forgetting."
109	    relevance: "Their 'critical proportion for catastrophic forgetting' is conceptually identical to our threshold—both mark a phase transition in mixing."
110	
111	  - id: li2025mixing_optimization
112	    title: "Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models"
113	    authors: "Li et al."
114	    year: 2025
115	    venue: ICML 2025
116	    category: data-mixing
117	    role: background
118	    key_finding: "SFT mixing as optimization with scaling-law parameterization. Optimal weights depend on model size and data scale."
119	    relevance: "Optimal mixing is model-size dependent—our 7B model may have different threshold than larger models. Finding is scale-specific."
120	
121	  - id: seddik2024synthetic_bound
122	    title: "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse"
123	    authors: "Seddik et al."
124	    year: 2024
125	    venue: arXiv 2404.05090
126	    category: data-mixing
127	    role: background
128	    key_finding: "Theoretical upper bounds on low-quality data proportion before collapse. Real data proportion must remain high."
129	    relevance: "Theoretical grounding for hard thresholds in quality mixing. Our empirical 10-25% window is consistent with their predictions."
130	
131	  # === Category: curriculum / quality threshold ===
132	
133	  - id: curriculum_robust2021
134	    title: "Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction"
135	    authors: "Zhou, Wang, Bilmes"
136	    year: 2021
137	    venue: ICLR 2021
138	    category: curriculum
139	    role: background
140	    key_finding: "Networks learn simple patterns first, then overfit noisy labels. Loss-based curriculum selection is unstable; errors accumulate multiplicatively."
141	    relevance: "Explains WHY threshold exists: once noisy proportion exceeds implicit curriculum capacity, errors accumulate. Our 25% may exceed model's capacity."
142	
143	  - id: agentprm2025
144	    title: "Process Reward Models for LLM Agents: Practical Framework and Directions"
145	    authors: "Choudhury"
146	    year: 2025
147	    venue: arXiv 2502.10325
148	    category: curriculum
149	    role: evaluation
150	    key_finding: "Best-of-N with process reward model achieves 91.0% on ALFWorld (N=16, base policy 88.1%). Shows reward-guided search outperforms SFT alone."
151	    relevance: "ALFWorld SOTA reference. Our 65.3% SFT-only baseline is reasonable given AgentPRM uses test-time search."
152	
153	  - id: wkm2024alfworld
154	    title: "Agent Planning with World Knowledge Model"
155	    authors: "Various"
156	    year: 2024
157	    venue: NeurIPS 2024
158	    category: curriculum
159	    role: evaluation
160	    key_finding: "World knowledge models reduce hallucinatory actions in ALFWorld. SFT on expert trajectories prone to overfitting."
161	    relevance: "ALFWorld baseline showing SFT quality sensitivity. Hallucination increase from poor training data parallels our error-injection degradation."
162	
163	  # === Category: training-dynamics / memorization ===
164	
165	  - id: arpit2017memorization
166	    title: "A Closer Look at Memorization in Deep Networks"
167	    authors: "Arpit, Jastrzębski, Ballas, Krueger, Bengio, Kanwal, Maharaj, Fischer, Courville, Bengio, Lacoste-Julien"
168	    year: 2017
169	    venue: ICML 2017
170	    category: training-dynamics
171	    role: background
172	    key_finding: "DNNs first learn clean patterns (early learning phase), then memorize noise. Training loss/accuracy improve on noisy data but generalization degrades. Dataset-independent capacity concepts are insufficient."
173	    relevance: "Directly explains our '50% injection → lowest train loss but worst eval' paradox. Higher injection = more noisy samples to memorize, better train metrics but worse generalization."
174	
175	  - id: liu2020early_learning_reg
176	    title: "Early-Learning Regularization Prevents Memorization of Noisy Labels"
177	    authors: "Liu, Niles-Weed, Razavian, Fernandez-Granda"
178	    year: 2020
179	    venue: NeurIPS 2020
180	    category: training-dynamics
181	    role: background
182	    key_finding: "Formalizes early learning phenomenon: models predict true labels for mislabeled examples early in training, then memorize wrong labels. ELR regularization exploits this window."
183	    relevance: "Our error-injected samples may be correctly handled early in training but memorized later, degrading clean-data generalization. Explains why more epochs could worsen the gap."
184	
185	  - id: zhou2023lima
186	    title: "LIMA: Less Is More for Alignment"
187	    authors: "Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy"
188	    year: 2023
189	    venue: NeurIPS 2023
190	    category: training-dynamics
191	    role: background
192	    key_finding: "Superficial Alignment Hypothesis: LLM knowledge/capability comes from pretraining; SFT only teaches output style/format. Limited SFT data suffices."
193	    relevance: "Explains why lower SFT loss ≠ better downstream capability. Error injection improves surface-level fitting (lower loss) but doesn't enhance—and may damage—pretrained planning capability."
194	
195	  - id: luo2023catastrophic_forgetting
196	    title: "An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning"
197	    authors: "Luo, Yang, Meng, Li, Zhou, Zhang"
198	    year: 2023
199	    venue: arXiv 2308.08747
200	    category: training-dynamics
201	    role: background
202	    key_finding: "SFT is off-policy learning prone to overfit training distribution and forget pretraining knowledge. Forgetting severity increases with divergence between fine-tuning and pretraining distributions."
203	    relevance: "Error injection increases distributional gap from pretraining data, accelerating catastrophic forgetting. 50% injection → maximal divergence → most forgetting of planning capability."
204	
205	  - id: longpre2020augmentation
206	    title: "How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?"
207	    authors: "Longpre, Wang, DuBois"
208	    year: 2020
209	    venue: Findings of EMNLP 2020
210	    category: training-dynamics
211	    role: background
212	    key_finding: "Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift."
213	    relevance: "Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning."
214	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "d46fe3d5-bc8c-49cf-ba7b-2e423dd43351",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
      "content": "# Literature Map: Dose-Response / Threshold Effects in Data Augmentation\n# Updated: 2026-05-15\n\nentries:\n  # === Category: dose-response / threshold ===\n\n  - id: rolnick2017robust\n    title: \"Deep Learning is Robust to Massive Label Noise\"\n    authors: \"Rolnick, Veit, Belongie, Shavit\"\n    year: 2017\n    venue: arXiv 1705.10694\n    category: dose-response\n    role: background\n    key_finding: \"DNNs maintain >90% accuracy on MNIST even when correct labels are diluted 100:1, as long as correct label remains most likely by a small margin.\"\n    relevance: \"Contrasts with our finding: image classification is robust to extreme noise, while embodied planning shows sharp degradation at 25%. Task complexity mediates noise tolerance.\"\n\n  - id: yuan2024early_stopping\n    title: \"Early Stopping Against Label Noise Without Validation Data\"\n    authors: \"Yuan, Feng, Liu\"\n    year: 2024\n    venue: ICLR 2024\n    category: dose-response\n    role: background\n    key_finding: \"Identifies phase transition where DNNs shift from fitting clean to fitting mislabeled examples. Proposes Label Wave to detect this transition during training.\"\n    relevance: \"Supports existence of phase transition in learning dynamics. Our 10-25% threshold may correspond to such a transition point in the SFT regime.\"\n\n  - id: dohmatob2025collapse\n    title: \"Strong Model Collapse\"\n    authors: \"Dohmatob, Feng, Subramonian, Kempe\"\n    year: 2025\n    venue: ICLR 2025\n    category: threshold\n    role: background\n    key_finding: \"Even 0.1% synthetic data can cause model collapse in supervised regression. Past interpolation threshold, larger models become more robust (double-descent).\"\n    relevance: \"Demonstrates extreme sensitivity to data quality in certain regimes. Our 10-25% threshold is analogous—small quality shifts cause nonlinear degradation.\"\n\n  - id: beyond_clean_data2024\n    title: \"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance\"\n    authors: \"Various\"\n    year: 2024\n    venue: ScienceDirect\n    category: dose-response\n    role: background\n    key_finding: \"Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds.\"\n    relevance: \"Methodologically similar—varies noise proportion to find degradation curves. Shows task-specific threshold behavior.\"\n\n  # === Category: error-injection / failure augmentation ===\n\n  - id: wang2024learning_from_failure\n    title: \"Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents\"\n    authors: \"Wang, Li, Han, Zhang, Baldwin\"\n    year: 2024\n    venue: arXiv 2402.11651\n    category: error-injection\n    role: evaluation\n    key_finding: \"Failed trajectories provide valuable signal for LLM agents via contrastive learning. Negative examples improve math, QA, strategic tasks when properly structured.\"\n    relevance: \"Directly related—injects negative trajectories into agent SFT. Key difference: they use contrastive framing, not raw mixing. Our work shows raw mixing has narrow safe window.\"\n\n  - id: song2024eto\n    title: \"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents\"\n    authors: \"Song, Yin, Yue, Huang, Li, Lin\"\n    year: 2024\n    venue: ACL 2024\n    category: error-injection\n    role: evaluation\n    key_finding: \"Iteratively collects failure trajectories, uses DPO-style contrastive learning on success-failure pairs. +8% WebShop, +9.5% ScienceWorld vs SFT.\"\n    relevance: \"Uses failure trajectories via preference optimization (DPO), not direct SFT mixing. Avoids our threshold problem by never training directly on failures.\"\n\n  - id: paladin2025\n    title: \"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases\"\n    authors: \"Vuddanti, Shah et al.\"\n    year: 2025\n    venue: arXiv 2509.25238\n    category: error-injection\n    role: evaluation\n    key_finding: \"Trains on 50K+ recovery-annotated failure trajectories via LoRA. +57pp recovery rate vs vanilla (32.76%→89.68%), +13.6pp vs CRITIC baseline. Taxonomy of 7 error classes. Includes inference-time retrieval.\"\n    relevance: \"Most similar to our approach (taxonomy-guided error injection). Key difference: they pair failures with recovery demos; we inject standalone error trajectories.\"\n\n  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Various\"\n    year: 2025\n    venue: arXiv 2603.21357\n    category: error-injection\n    role: evaluation\n    key_finding: \"Converts failed trajectories to valid training data by relabeling—failure for task A becomes success for task B.\"\n    relevance: \"Avoids noise problem by redefining failure as success for different goals. Contrasts with our direct injection approach.\"\n\n  # === Category: data-mixing ===\n\n  - id: dong2024composition\n    title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n    authors: \"Dong, Yuan et al.\"\n    year: 2024\n    venue: ACL 2024\n    category: data-mixing\n    role: background\n    key_finding: \"Data amount per domain matters more than ratio. Low-data mixing enables cross-domain transfer; high-data mixing causes ability conflicts.\"\n    relevance: \"Documents ability-conflict at high data amounts—analogous to our threshold. Ratio secondary to amount suggests our threshold may be absolute-count driven.\"\n\n  - id: ye2025mixing_laws\n    title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n    authors: \"Ye et al.\"\n    year: 2025\n    venue: ICLR 2025\n    category: data-mixing\n    role: background\n    key_finding: \"Discovers quantitative scaling laws L=f(r) for mixture proportions. Accurately predicts critical proportion avoiding catastrophic forgetting.\"\n    relevance: \"Their 'critical proportion for catastrophic forgetting' is conceptually identical to our threshold—both mark a phase transition in mixing.\"\n\n  - id: li2025mixing_optimization\n    title: \"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICML 2025\n    category: data-mixing\n    role: background\n    key_finding: \"SFT mixing as optimization with scaling-law parameterization. Optimal weights depend on model size and data scale.\"\n    relevance: \"Optimal mixing is model-size dependent—our 7B model may have different threshold than larger models. Finding is scale-specific.\"\n\n  - id: seddik2024synthetic_bound\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Seddik et al.\"\n    year: 2024\n    venue: arXiv 2404.05090\n    category: data-mixing\n    role: background\n    key_finding: \"Theoretical upper bounds on low-quality data proportion before collapse. Real data proportion must remain high.\"\n    relevance: \"Theoretical grounding for hard thresholds in quality mixing. Our empirical 10-25% window is consistent with their predictions.\"\n\n  # === Category: curriculum / quality threshold ===\n\n  - id: curriculum_robust2021\n    title: \"Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction\"\n    authors: \"Zhou, Wang, Bilmes\"\n    year: 2021\n    venue: ICLR 2021\n    category: curriculum\n    role: background\n    key_finding: \"Networks learn simple patterns first, then overfit noisy labels. Loss-based curriculum selection is unstable; errors accumulate multiplicatively.\"\n    relevance: \"Explains WHY threshold exists: once noisy proportion exceeds implicit curriculum capacity, errors accumulate. Our 25% may exceed model's capacity.\"\n\n  - id: agentprm2025\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    year: 2025\n    venue: arXiv 2502.10325\n    category: curriculum\n    role: evaluation\n    key_finding: \"Best-of-N with process reward model achieves 91.0% on ALFWorld (N=16, base policy 88.1%). Shows reward-guided search outperforms SFT alone.\"\n    relevance: \"ALFWorld SOTA reference. Our 65.3% SFT-only baseline is reasonable given AgentPRM uses test-time search.\"\n\n  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Various\"\n    year: 2024\n    venue: NeurIPS 2024\n    category: curriculum\n    role: evaluation\n    key_finding: \"World knowledge models reduce hallucinatory actions in ALFWorld. SFT on expert trajectories prone to overfitting.\"\n    relevance: \"ALFWorld baseline showing SFT quality sensitivity. Hallucination increase from poor training data parallels our error-injection degradation.\"\n\n  # === Category: training-dynamics / memorization ===\n\n  - id: arpit2017memorization\n    title: \"A Closer Look at Memorization in Deep Networks\"\n    authors: \"Arpit, Jastrzębski, Ballas, Krueger, Bengio, Kanwal, Maharaj, Fischer, Courville, Bengio, Lacoste-Julien\"\n    year: 2017\n    venue: ICML 2017\n    category: training-dynamics\n    role: background\n    key_finding: \"DNNs first learn clean patterns (early learning phase), then memorize noise. Training loss/accuracy improve on noisy data but generalization degrades. Dataset-independent capacity concepts are insufficient.\"\n    relevance: \"Directly explains our '50% injection → lowest train loss but worst eval' paradox. Higher injection = more noisy samples to memorize, better train metrics but worse generalization.\"\n\n  - id: liu2020early_learning_reg\n    title: \"Early-Learning Regularization Prevents Memorization of Noisy Labels\"\n    authors: \"Liu, Niles-Weed, Razavian, Fernandez-Granda\"\n    year: 2020\n    venue: NeurIPS 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Formalizes early learning phenomenon: models predict true labels for mislabeled examples early in training, then memorize wrong labels. ELR regularization exploits this window.\"\n    relevance: \"Our error-injected samples may be correctly handled early in training but memorized later, degrading clean-data generalization. Explains why more epochs could worsen the gap.\"\n\n  - id: zhou2023lima\n    title: \"LIMA: Less Is More for Alignment\"\n    authors: \"Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy\"\n    year: 2023\n    venue: NeurIPS 2023\n    category: training-dynamics\n    role: background\n    key_finding: \"Superficial Alignment Hypothesis: LLM knowledge/capability comes from pretraining; SFT only teaches output style/format. Limited SFT data suffices.\"\n    relevance: \"Explains why lower SFT loss ≠ better downstream capability. Error injection improves surface-level fitting (lower loss) but doesn't enhance—and may damage—pretrained planning capability.\"\n\n  - id: luo2023catastrophic_forgetting\n    title: \"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning\"\n    authors: \"Luo, Yang, Meng, Li, Zhou, Zhang\"\n    year: 2023\n    venue: arXiv 2308.08747\n    category: training-dynamics\n    role: background\n    key_finding: \"SFT is off-policy learning prone to overfit training distribution and forget pretraining knowledge. Forgetting severity increases with divergence between fine-tuning and pretraining distributions.\"\n    relevance: \"Error injection increases distributional gap from pretraining data, accelerating catastrophic forgetting. 50% injection → maximal divergence → most forgetting of planning capability.\"\n\n  - id: longpre2020augmentation\n    title: \"How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?\"\n    authors: \"Longpre, Wang, DuBois\"\n    year: 2020\n    venue: Findings of EMNLP 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift.\"\n    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"\n",
      "numLines": 214,
      "startLine": 1,
      "totalLines": 214
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
Now let me search for the three papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "71210af6-3517-4a77-b544-ec8a4cd595b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdjrQqV7LCRV1ZsPNr7zpy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4551,
      "cache_read_input_tokens": 24115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4551
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ac48x3Az1QwDNvoMa4gPjQ`</summary>

```json
{
  "query": "McCoy et al 2020 \"BERTs of a feather do not generalize together\" paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "17772f65-28dc-472c-9dce-a39086ee0aa0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdjrQqV7LCRV1ZsPNr7zpy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4551,
      "cache_read_input_tokens": 24115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4551
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0163nMgQyEXYbmJ6aJXNcy7a`</summary>

```json
{
  "query": "Mosbach et al 2021 \"On the Stability of Fine-Tuning BERT\" paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "1d098796-638c-43b1-b0be-1bc01030c5c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdjrQqV7LCRV1ZsPNr7zpy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4551,
      "cache_read_input_tokens": 24115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4551
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_019anyBUvibUm4biawjHoMop`</summary>

```json
{
  "query": "D'Amour et al 2022 \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "f9ae4fb2-983d-4d44-bec6-3f90e14b415d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdjrQqV7LCRV1ZsPNr7zpy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4551,
      "cache_read_input_tokens": 24115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4551
      },
      "output_tokens": 18,
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

_source line 14 · 2026-05-15T03:28:19.754Z_

<details><summary>↩ Tool result · `toolu_01Ac48x3Az1QwDNvoMa4gPjQ`</summary>

```text
Web search results for query: "McCoy et al 2020 "BERTs of a feather do not generalize together" paper"

Links: [{"title":"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance - ACL Anthology","url":"https://aclanthology.org/2020.blackboxnlp-1.21/"},{"title":"[1911.02969] BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance","url":"https://arxiv.org/abs/1911.02969"},{"title":"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance | Request PDF","url":"https://www.researchgate.net/publication/347236013_BERTs_of_a_feather_do_not_generalize_together_Large_variability_in_generalization_across_models_with_similar_test_set_performance"},{"title":"[PDF] BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BERTs-of-a-feather-do-not-generalize-together:-in-McCoy-Min/48689c4bb52a45c0bc97d1421d72d11bab6c346b"},{"title":"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance","url":"https://zenodo.org/records/4110593"},{"title":"Paper page - BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance","url":"https://huggingface.co/papers/1911.02969"},{"title":"dblp: BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance.","url":"https://dblp.org/rec/journals/corr/abs-1911-02969.html"},{"title":"Exploring Generalization Ability of Pretrained Language Models on Arithmetic and Logical Reasoning | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-030-88480-2_61"},{"title":"BERTs of a feather do not generalize together","url":"https://tallinzen.net/media/papers/mccoy_min_linzen_2020_blackboxnlp.pdf"},{"title":"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv191102969M/abstract"}]

I found the paper successfully! Here's what I found about the McCoy et al. 2020 paper "BERTs of a feather do not generalize together":

## Paper Details

The paper was authored by R. Thomas McCoy, Junghyun Min, and Tal Linzen, and titled "BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance." It was published in the Proceedings of the Third BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP (November 2020).

## Research Question and Findings

The paper asks: "If the same neural network architecture is trained multiple times on the same dataset, will it make similar linguistic generalizations across runs?" To study this, the authors fine-tuned 100 instances of BERT on the Multi-genre Natural Language Inference (MNLI) dataset and evaluated them on the HANS dataset, which evaluates syntactic generalization in natural language inference.

## Key Results

On the MNLI development set, the behavior of all instances was remarkably consistent, with accuracy ranging between 83.6% and 84.8%. In stark contrast, the same models varied widely in their generalization performance. For example, on the simple case of subject-object swap (e.g., determining that "the doctor visited the lawyer" does not entail "the lawyer visited the doctor"), accuracy ranged from 0.0% to 66.2%.

## Interpretation

The variation is likely due to the presence of many local minima in the loss surface that are equally attractive to a low-bias learner such as a neural network; decreasing the variability may therefore require models with stronger inductive biases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "cde049e2-a421-4ef5-873c-f7918e7c228f",
  "tool_use_result": {
    "query": "McCoy et al 2020 \"BERTs of a feather do not generalize together\" paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VWTPfyjsZRp8sWESWPLTXa",
        "content": [
          {
            "title": "BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance - ACL Anthology",
            "url": "https://aclanthology.org/2020.blackboxnlp-1.21/"
          },
          {
            "title": "[1911.02969] BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance",
            "url": "https://arxiv.org/abs/1911.02969"
          },
          {
            "title": "BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance | Request PDF",
            "url": "https://www.researchgate.net/publication/347236013_BERTs_of_a_feather_do_not_generalize_together_Large_variability_in_generalization_across_models_with_similar_test_set_performance"
          },
          {
            "title": "[PDF] BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/BERTs-of-a-feather-do-not-generalize-together:-in-McCoy-Min/48689c4bb52a45c0bc97d1421d72d11bab6c346b"
          },
          {
            "title": "BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance",
            "url": "https://zenodo.org/records/4110593"
          },
          {
            "title": "Paper page - BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance",
            "url": "https://huggingface.co/papers/1911.02969"
          },
          {
            "title": "dblp: BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance.",
            "url": "https://dblp.org/rec/journals/corr/abs-1911-02969.html"
          },
          {
            "title": "Exploring Generalization Ability of Pretrained Language Models on Arithmetic and Logical Reasoning | SpringerLink",
            "url": "https://link.springer.com/chapter/10.1007/978-3-030-88480-2_61"
          },
          {
            "title": "BERTs of a feather do not generalize together",
            "url": "https://tallinzen.net/media/papers/mccoy_min_linzen_2020_blackboxnlp.pdf"
          },
          {
            "title": "BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2019arXiv191102969M/abstract"
          }
        ]
      },
      "I found the paper successfully! Here's what I found about the McCoy et al. 2020 paper \"BERTs of a feather do not generalize together\":\n\n## Paper Details\n\nThe paper was authored by R. Thomas McCoy, Junghyun Min, and Tal Linzen, and titled \"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance.\" It was published in the Proceedings of the Third BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP (November 2020).\n\n## Research Question and Findings\n\nThe paper asks: \"If the same neural network architecture is trained multiple times on the same dataset, will it make similar linguistic generalizations across runs?\" To study this, the authors fine-tuned 100 instances of BERT on the Multi-genre Natural Language Inference (MNLI) dataset and evaluated them on the HANS dataset, which evaluates syntactic generalization in natural language inference.\n\n## Key Results\n\nOn the MNLI development set, the behavior of all instances was remarkably consistent, with accuracy ranging between 83.6% and 84.8%. In stark contrast, the same models varied widely in their generalization performance. For example, on the simple case of subject-object swap (e.g., determining that \"the doctor visited the lawyer\" does not entail \"the lawyer visited the doctor\"), accuracy ranged from 0.0% to 66.2%.\n\n## Interpretation\n\nThe variation is likely due to the presence of many local minima in the loss surface that are equally attractive to a low-bias learner such as a neural network; decreasing the variability may therefore require models with stronger inductive biases."
    ],
    "durationSeconds": 4.837388356000002
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T03:28:20.805Z_

<details><summary>↩ Tool result · `toolu_0163nMgQyEXYbmJ6aJXNcy7a`</summary>

```text
Web search results for query: "Mosbach et al 2021 "On the Stability of Fine-Tuning BERT" paper"

Links: [{"title":"[PDF] On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-the-Stability-of-Fine-tuning-BERT:-Explanations,-Mosbach-Andriushchenko/8b9d77d5e52a70af37451d3db3d32781b83ea054"},{"title":"[2006.04884] On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines","url":"https://arxiv.org/abs/2006.04884"},{"title":"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines - researchr publication","url":"https://researchr.org/publication/MosbachAK21"},{"title":"dblp: On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines.","url":"https://dblp.org/rec/conf/iclr/MosbachAK21.html"},{"title":"[2021] On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines · Issue #134 · cfiken/paper-reading","url":"https://github.com/cfiken/paper-reading/issues/134"},{"title":"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines","url":"https://infoscience.epfl.ch/entities/publication/c6ba6881-3085-479a-8265-e5446e0831b2"},{"title":"On the Stability of Fine-tuning BERT - Marius Mosbach","url":"https://iclr.cc/virtual/2021/poster/2558"},{"title":"What Exactly Happens When We Fine-Tune Large Language Models?","url":"https://mlfrontiers.substack.com/p/what-exactly-happens-when-we-fine"},{"title":"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines | OpenReview","url":"https://openreview.net/forum?id=nzpLWnVAyah"},{"title":"[2006.04884v1] On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines","url":"https://arxiv.org/abs/2006.04884v1"}]

I found the paper! Here are the key results from my search:

## Paper Details

The paper "On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines" was authored by Marius Mosbach, Maksym Andriushchenko, and Dietrich Klakow, and was presented at the 9th International Conference on Learning Representations (ICLR 2021) in May 2021.

## Main Findings

The paper addresses the problem that fine-tuning is an unstable process: training the same model with multiple random seeds can result in a large variance of the task performance.

The authors show that two previously hypothesized reasons for instability—catastrophic forgetting and small size of fine-tuning datasets—fail to explain the fine-tuning instability, and instead demonstrate that the observed instability is caused by optimization difficulties that lead to vanishing gradients.

Additionally, they show that the remaining variance can be attributed to differences in generalization, and they present a simple but strong baseline that makes fine-tuning BERT-based models significantly more stable than previously proposed approaches.

## Paper Links

The paper is available on:
- arXiv (arxiv.org/abs/2006.04884)
- With code available at https://github.com/uds-lsv/bert-stable-fine-tuning


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "370e901e-002a-43d4-9c56-99a9d203fbad",
  "tool_use_result": {
    "query": "Mosbach et al 2021 \"On the Stability of Fine-Tuning BERT\" paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DgRWTmqJWKVFA9j6JKmYTz",
        "content": [
          {
            "title": "[PDF] On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/On-the-Stability-of-Fine-tuning-BERT:-Explanations,-Mosbach-Andriushchenko/8b9d77d5e52a70af37451d3db3d32781b83ea054"
          },
          {
            "title": "[2006.04884] On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines",
            "url": "https://arxiv.org/abs/2006.04884"
          },
          {
            "title": "On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines - researchr publication",
            "url": "https://researchr.org/publication/MosbachAK21"
          },
          {
            "title": "dblp: On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines.",
            "url": "https://dblp.org/rec/conf/iclr/MosbachAK21.html"
          },
          {
            "title": "[2021] On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines · Issue #134 · cfiken/paper-reading",
            "url": "https://github.com/cfiken/paper-reading/issues/134"
          },
          {
            "title": "On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines",
            "url": "https://infoscience.epfl.ch/entities/publication/c6ba6881-3085-479a-8265-e5446e0831b2"
          },
          {
            "title": "On the Stability of Fine-tuning BERT - Marius Mosbach",
            "url": "https://iclr.cc/virtual/2021/poster/2558"
          },
          {
            "title": "What Exactly Happens When We Fine-Tune Large Language Models?",
            "url": "https://mlfrontiers.substack.com/p/what-exactly-happens-when-we-fine"
          },
          {
            "title": "On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines | OpenReview",
            "url": "https://openreview.net/forum?id=nzpLWnVAyah"
          },
          {
            "title": "[2006.04884v1] On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines",
            "url": "https://arxiv.org/abs/2006.04884v1"
          }
        ]
      },
      "I found the paper! Here are the key results from my search:\n\n## Paper Details\n\nThe paper \"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines\" was authored by Marius Mosbach, Maksym Andriushchenko, and Dietrich Klakow, and was presented at the 9th International Conference on Learning Representations (ICLR 2021) in May 2021.\n\n## Main Findings\n\nThe paper addresses the problem that fine-tuning is an unstable process: training the same model with multiple random seeds can result in a large variance of the task performance.\n\nThe authors show that two previously hypothesized reasons for instability—catastrophic forgetting and small size of fine-tuning datasets—fail to explain the fine-tuning instability, and instead demonstrate that the observed instability is caused by optimization difficulties that lead to vanishing gradients.\n\nAdditionally, they show that the remaining variance can be attributed to differences in generalization, and they present a simple but strong baseline that makes fine-tuning BERT-based models significantly more stable than previously proposed approaches.\n\n## Paper Links\n\nThe paper is available on:\n- arXiv (arxiv.org/abs/2006.04884)\n- With code available at https://github.com/uds-lsv/bert-stable-fine-tuning"
    ],
    "durationSeconds": 4.8433003900000005
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T03:28:26.058Z_

<details><summary>↩ Tool result · `toolu_019anyBUvibUm4biawjHoMop`</summary>

```text
Web search results for query: "D'Amour et al 2022 "Underspecification Presents Challenges for Credibility in Modern Machine Learning""

Links: [{"title":"Underspecification Presents Challenges for Credibility in Modern Machine Learning","url":"https://www.jmlr.org/papers/v23/20-1335.html"},{"title":"Underspecification presents challenges for credibility in modern machine learning | The Journal of Machine Learning Research","url":"https://dl.acm.org/doi/10.5555/3586589.3586815"},{"title":"(PDF) Underspecification Presents Challenges for Credibility in Modern Machine Learning","url":"https://www.researchgate.net/publication/364089505_Underspecification_Presents_Challenges_for_Credibility_in_Modern_Machine_Learning"},{"title":"Underspecification presents challenges for credibility in ...","url":"https://dl.acm.org/doi/pdf/10.5555/3586589.3586815"},{"title":"[2011.03395] Underspecification Presents Challenges for Credibility in Modern Machine Learning","url":"https://arxiv.org/abs/2011.03395"},{"title":"[PDF] Underspecification Presents Challenges for Credibility in Modern Machine Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Underspecification-Presents-Challenges-for-in-D'Amour-Heller/71a85e735a3686bef8cce3725ae5ba82e2cabb1b"},{"title":"How Underspecification Presents Challenges for Machine Learning","url":"https://research.google/blog/how-underspecification-presents-challenges-for-machine-learning/?m=1"},{"title":"Underspecification Presents Challenges for Credibility in Modern Machine Learning. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/11392e00397b9939b73ae7159630384bc"},{"title":"Underspecification Presents Challenges for Credibility in Modern Machine Learning","url":"https://research.google/pubs/underspecification-presents-challenges-for-credibility-in-modern-machine-learning/"},{"title":"Underspecification Presents Challenges for Credibility in Modern Machine Learning - Paper Detail","url":"https://deeplearn.org/arxiv/168762/underspecification-presents-challenges-for-credibility-in-modern-machine-learning"}]

I found the paper you were looking for. Here's a summary of the search results:

## Paper Details

The paper "Underspecification Presents Challenges for Credibility in Modern Machine Learning" was published in the Journal of Machine Learning Research, Volume 23, Issue 226, pages 1-61 in 2022.

## Main Concept

An ML pipeline is underspecified when it can return many distinct predictors with equivalently strong test performance. The paper identifies underspecification in ML pipelines as a key reason why machine learning systems often exhibit unexpectedly poor behavior when deployed in real-world domains.

## Key Findings

Predictors returned by underspecified pipelines are often treated as equivalent based on their training domain performance, but can behave very differently in deployment domains, with this ambiguity leading to instability and poor model behavior in practice.

## Applications Studied

The authors provide evidence that underspecification has substantive implications for practical ML pipelines, using examples from computer vision, medical imaging, natural language processing, clinical risk prediction based on electronic health records, and medical genomics.

The paper is available through multiple sources including the Journal of Machine Learning Research website and arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "0fd63f16-4bbe-4691-a5fe-e11868668f0e",
  "tool_use_result": {
    "query": "D'Amour et al 2022 \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CsM27nBSJjhXAqMNZ7Q65H",
        "content": [
          {
            "title": "Underspecification Presents Challenges for Credibility in Modern Machine Learning",
            "url": "https://www.jmlr.org/papers/v23/20-1335.html"
          },
          {
            "title": "Underspecification presents challenges for credibility in modern machine learning | The Journal of Machine Learning Research",
            "url": "https://dl.acm.org/doi/10.5555/3586589.3586815"
          },
          {
            "title": "(PDF) Underspecification Presents Challenges for Credibility in Modern Machine Learning",
            "url": "https://www.researchgate.net/publication/364089505_Underspecification_Presents_Challenges_for_Credibility_in_Modern_Machine_Learning"
          },
          {
            "title": "Underspecification presents challenges for credibility in ...",
            "url": "https://dl.acm.org/doi/pdf/10.5555/3586589.3586815"
          },
          {
            "title": "[2011.03395] Underspecification Presents Challenges for Credibility in Modern Machine Learning",
            "url": "https://arxiv.org/abs/2011.03395"
          },
          {
            "title": "[PDF] Underspecification Presents Challenges for Credibility in Modern Machine Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Underspecification-Presents-Challenges-for-in-D'Amour-Heller/71a85e735a3686bef8cce3725ae5ba82e2cabb1b"
          },
          {
            "title": "How Underspecification Presents Challenges for Machine Learning",
            "url": "https://research.google/blog/how-underspecification-presents-challenges-for-machine-learning/?m=1"
          },
          {
            "title": "Underspecification Presents Challenges for Credibility in Modern Machine Learning. | BibSonomy",
            "url": "https://www.bibsonomy.org/bibtex/11392e00397b9939b73ae7159630384bc"
          },
          {
            "title": "Underspecification Presents Challenges for Credibility in Modern Machine Learning",
            "url": "https://research.google/pubs/underspecification-presents-challenges-for-credibility-in-modern-machine-learning/"
          },
          {
            "title": "Underspecification Presents Challenges for Credibility in Modern Machine Learning - Paper Detail",
            "url": "https://deeplearn.org/arxiv/168762/underspecification-presents-challenges-for-credibility-in-modern-machine-learning"
          }
        ]
      },
      "I found the paper you were looking for. Here's a summary of the search results:\n\n## Paper Details\n\nThe paper \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\" was published in the Journal of Machine Learning Research, Volume 23, Issue 226, pages 1-61 in 2022.\n\n## Main Concept\n\nAn ML pipeline is underspecified when it can return many distinct predictors with equivalently strong test performance. The paper identifies underspecification in ML pipelines as a key reason why machine learning systems often exhibit unexpectedly poor behavior when deployed in real-world domains.\n\n## Key Findings\n\nPredictors returned by underspecified pipelines are often treated as equivalent based on their training domain performance, but can behave very differently in deployment domains, with this ambiguity leading to instability and poor model behavior in practice.\n\n## Applications Studied\n\nThe authors provide evidence that underspecification has substantive implications for practical ML pipelines, using examples from computer vision, medical imaging, natural language processing, clinical risk prediction based on electronic health records, and medical genomics.\n\nThe paper is available through multiple sources including the Journal of Machine Learning Research website and arXiv."
    ],
    "durationSeconds": 9.683987725
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the basic information for all three papers. Now I need to get the complete author lists. Let me search for more details on each paper, especially the full author lists.

For McCoy et al.: Authors are R. Thomas McCoy, Junghyun Min, and Tal Linzen. Venue: BlackboxNLP 2020 (Workshop at EMNLP). arXiv: 1911.02969

For Mosbach et al.: Authors are Marius Mosbach, Maksym Andriushchenko, and Dietrich Klakow. Venue: ICLR 2021. arXiv: 2006.04884
 
Now I need to track down the complete author list for D'Amour et al., which was published in JMLR 2022.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "50c9220e-e136-4fb1-be9a-a60e8148f383",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnZsGHdUicH1DqKvW2cxUi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3255,
      "cache_read_input_tokens": 28666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3255
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

_source line 18_

D'Amour et al. 有很多作者，需要确认完整列表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "73de5c63-943a-4314-8007-d254d8685913",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnZsGHdUicH1DqKvW2cxUi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3255,
      "cache_read_input_tokens": 28666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3255
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F9ce75RKF8spD3wRioTzna`</summary>

```json
{
  "query": "D'Amour et al 2022 underspecification JMLR full author list all authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "355bb467-135a-42cb-be71-88c5df286e4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnZsGHdUicH1DqKvW2cxUi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3255,
      "cache_read_input_tokens": 28666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3255
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

_source line 20 · 2026-05-15T03:28:41.197Z_

<details><summary>↩ Tool result · `toolu_01F9ce75RKF8spD3wRioTzna`</summary>

```text
Web search results for query: "D'Amour et al 2022 underspecification JMLR full author list all authors"

Links: [{"title":"Underspecification Presents Challenges for Credibility in Modern Machine Learning","url":"https://www.jmlr.org/papers/v23/20-1335.html"},{"title":"Underspecification Presents Challenges for Credibility in Modern Machine Learning. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/11392e00397b9939b73ae7159630384bc"},{"title":"Underspecification Presents Challenges for Credibility in ...","url":"https://www.jmlr.org/papers/volume23/20-1335/20-1335.pdf"},{"title":"[2011.03395] Underspecification Presents Challenges for Credibility in Modern Machine Learning","url":"https://arxiv.org/abs/2011.03395"},{"title":"Underspecification presents challenges for credibility in modern machine learning | The Journal of Machine Learning Research","url":"https://dl.acm.org/doi/10.5555/3586589.3586815"},{"title":"[PDF] Underspecification Presents Challenges for Credibility in Modern Machine Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Underspecification-Presents-Challenges-for-in-D'Amour-Heller/71a85e735a3686bef8cce3725ae5ba82e2cabb1b"},{"title":"(PDF) Underspecification Presents Challenges for Credibility in Modern Machine Learning","url":"https://www.researchgate.net/publication/345555232_Underspecification_Presents_Challenges_for_Credibility_in_Modern_Machine_Learning"},{"title":"JMLR: Vol 23, No 1 - ACM Digital Library","url":"https://dl.acm.org/toc/jmlr/2022/23/1?useYearTocUrl=false&id=31"},{"title":"Journal of Machine Learning Research (JMLR) - Serial Profile - zbMATH Open","url":"https://zbmath.org/serials/?q=se:2913"},{"title":"JMLR Template - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/jmlr-template/zqvxjzpbgxvb"}]

Based on the search results, here is the complete author list for the D'Amour et al. 2022 paper published in JMLR:

Alexander D'Amour, Katherine Heller, Dan Moldovan, Ben Adlam, Babak Alipanahi, Alex Beutel, Christina Chen, Jonathan Deaton, Jacob Eisenstein, Matthew D. Hoffman, Farhad Hormozdiari, Neil Houlsby, Shaobo Hou, Ghassen Jerfel, Alan Karthikesalingam, Mario Lucic, Yian Ma, Cory McLean, Diana Mincu, Akinori Mitani, Andrea Montanari, Zachary Nado, Vivek Natarajan, Christopher Nielson, Thomas F. Osborne, Rajiv Raman, Kim Ramasamy, Rory Sayres, Jessica Schrouff, Martin Seneviratne, Shannon Sequeira, Harini Suresh, Victor Veitch, Max Vladymyrov, Xuezhi Wang, Kellie Webster, Steve Yadlowsky, Taedong Yun, Xiaohua Zhai, D. Sculley

The paper, titled "Underspecification Presents Challenges for Credibility in Modern Machine Learning," was published in the Journal of Machine Learning Research, Volume 23, Issue 226, in 2022.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "fbcf5e13-0f57-47aa-b889-7769fc83e7db",
  "tool_use_result": {
    "query": "D'Amour et al 2022 underspecification JMLR full author list all authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VX2gQB77YovyPLR9zKg4Ci",
        "content": [
          {
            "title": "Underspecification Presents Challenges for Credibility in Modern Machine Learning",
            "url": "https://www.jmlr.org/papers/v23/20-1335.html"
          },
          {
            "title": "Underspecification Presents Challenges for Credibility in Modern Machine Learning. | BibSonomy",
            "url": "https://www.bibsonomy.org/bibtex/11392e00397b9939b73ae7159630384bc"
          },
          {
            "title": "Underspecification Presents Challenges for Credibility in ...",
            "url": "https://www.jmlr.org/papers/volume23/20-1335/20-1335.pdf"
          },
          {
            "title": "[2011.03395] Underspecification Presents Challenges for Credibility in Modern Machine Learning",
            "url": "https://arxiv.org/abs/2011.03395"
          },
          {
            "title": "Underspecification presents challenges for credibility in modern machine learning | The Journal of Machine Learning Research",
            "url": "https://dl.acm.org/doi/10.5555/3586589.3586815"
          },
          {
            "title": "[PDF] Underspecification Presents Challenges for Credibility in Modern Machine Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Underspecification-Presents-Challenges-for-in-D'Amour-Heller/71a85e735a3686bef8cce3725ae5ba82e2cabb1b"
          },
          {
            "title": "(PDF) Underspecification Presents Challenges for Credibility in Modern Machine Learning",
            "url": "https://www.researchgate.net/publication/345555232_Underspecification_Presents_Challenges_for_Credibility_in_Modern_Machine_Learning"
          },
          {
            "title": "JMLR: Vol 23, No 1 - ACM Digital Library",
            "url": "https://dl.acm.org/toc/jmlr/2022/23/1?useYearTocUrl=false&id=31"
          },
          {
            "title": "Journal of Machine Learning Research (JMLR) - Serial Profile - zbMATH Open",
            "url": "https://zbmath.org/serials/?q=se:2913"
          },
          {
            "title": "JMLR Template - Overleaf, Online LaTeX Editor",
            "url": "https://www.overleaf.com/latex/templates/jmlr-template/zqvxjzpbgxvb"
          }
        ]
      },
      "Based on the search results, here is the complete author list for the D'Amour et al. 2022 paper published in JMLR:\n\nAlexander D'Amour, Katherine Heller, Dan Moldovan, Ben Adlam, Babak Alipanahi, Alex Beutel, Christina Chen, Jonathan Deaton, Jacob Eisenstein, Matthew D. Hoffman, Farhad Hormozdiari, Neil Houlsby, Shaobo Hou, Ghassen Jerfel, Alan Karthikesalingam, Mario Lucic, Yian Ma, Cory McLean, Diana Mincu, Akinori Mitani, Andrea Montanari, Zachary Nado, Vivek Natarajan, Christopher Nielson, Thomas F. Osborne, Rajiv Raman, Kim Ramasamy, Rory Sayres, Jessica Schrouff, Martin Seneviratne, Shannon Sequeira, Harini Suresh, Victor Veitch, Max Vladymyrov, Xuezhi Wang, Kellie Webster, Steve Yadlowsky, Taedong Yun, Xiaohua Zhai, D. Sculley\n\nThe paper, titled \"Underspecification Presents Challenges for Credibility in Modern Machine Learning,\" was published in the Journal of Machine Learning Research, Volume 23, Issue 226, in 2022."
    ],
    "durationSeconds": 6.477169136999997
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the entries:

1. **McCoy et al. (2020)**
   - Title: "BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance"
   - Authors: R. Thomas McCoy, Junghyun Min, Tal Linzen
   - Year: 2020
   - Venue: Proceedings of the Third BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP (at EMNLP 2020)
   - arXiv: 1911.02969
   
2. **Mosbach et al. (2021)**
   - Title: "On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines"
   - Authors: Marius Mosbach, Maksym Andriushchenko, Dietrich Klakow
   - Year: 2021
   - Venue: ICLR 2021
   - arXiv: 2006.04884

3. **D'Amour et al. (2022)**
   - Title: "Underspecification Presents Challenges for Credibility in Modern Machine Learning"
   - Authors: Alexander D'Amour, Katherine Heller, Dan Moldovan, Ben Adlam, Babak Alipanahi, Alex Beutel, Christina Chen, Jonathan De

, Jacob Eisenstein, Matthew D. Hoffman, Farhad Hormozdiari, Neil Houlsby, Shaobo Hou, Ghassen Jerfel, Alan Karthikesalingam, Mario Lucic, Yian Ma, Cory McLean, Diana Mincu, Akinori Mitani, Andrea Montanari, Zachary Nado, Vivek Natarajan, Christopher Nielson, Thomas F. Osborne, Rajiv Raman, Kim Ramasamy, Rory Sayres, Jessica Schrouff, Martin Seneviratne, Shannon Sequeira, Harini Suresh, Victor Veitch, Max Vladymyrov, Xuezhi Wang, Kellie Webster, Steve Yadlowsky, Taedong Yun, Xiaohua Zhai, D. Sculley
   - Year: 2022
   - Venue: Journal of Machine Learning Research (JMLR)
   - Volume: 23, Issue: 226
   - arXiv: 2011.03395

Now I'm updating the literature_map.yaml file to include this paper in the appropriate section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "876b93f3-e3a9-4682-aa96-9562beb04a43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kMpkcN2xBwW6acvVGQV4S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 31921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1269
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

_source line 22_

三篇论文元数据已验证。现在更新 literature_map.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "1b1235ef-b2f7-4aef-916d-7be2ff75a2de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kMpkcN2xBwW6acvVGQV4S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 31921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1269
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

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_01AtMvXPEoFJZ8aqmWSZ9gut`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
  "old_string": "    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"",
  "new_string": "    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"\n\n  # === Category: training-instability ===\n\n  - id: mccoy2020seeds\n    title: \"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance\"\n    authors: \"McCoy, Min, Linzen\"\n    year: 2020\n    venue: \"BlackboxNLP Workshop at EMNLP 2020\"\n    category: training-instability\n    role: background\n    key_finding: \"Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization.\"\n    relevance: \"与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity\"\n\n  - id: mosbach2021stability\n    title: \"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines\"\n    authors: \"Mosbach, Andriushchenko, Klakow\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    category: training-instability\n    role: background\n    key_finding: \"BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。\"\n    relevance: \"fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training\"\n\n  - id: damour2022underspecification\n    title: \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"\n    authors: \"D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al.\"\n    year: 2022\n    venue: \"Journal of Machine Learning Research, Vol. 23, No. 226\"\n    category: training-instability\n    role: background\n    key_finding: \"ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。\"\n    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "d034be00-06f4-43c6-ba70-f488fef40117",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kMpkcN2xBwW6acvVGQV4S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 31921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1269
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

_source line 24 · 2026-05-15T03:29:08.172Z_

<details><summary>↩ Tool result · `toolu_01AtMvXPEoFJZ8aqmWSZ9gut`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "2714af24-d2fa-418f-a5e9-28f21a214cb9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
    "oldString": "    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"",
    "newString": "    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"\n\n  # === Category: training-instability ===\n\n  - id: mccoy2020seeds\n    title: \"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance\"\n    authors: \"McCoy, Min, Linzen\"\n    year: 2020\n    venue: \"BlackboxNLP Workshop at EMNLP 2020\"\n    category: training-instability\n    role: background\n    key_finding: \"Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization.\"\n    relevance: \"与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity\"\n\n  - id: mosbach2021stability\n    title: \"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines\"\n    authors: \"Mosbach, Andriushchenko, Klakow\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    category: training-instability\n    role: background\n    key_finding: \"BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。\"\n    relevance: \"fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training\"\n\n  - id: damour2022underspecification\n    title: \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"\n    authors: \"D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al.\"\n    year: 2022\n    venue: \"Journal of Machine Learning Research, Vol. 23, No. 226\"\n    category: training-instability\n    role: background\n    key_finding: \"ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。\"\n    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"",
    "originalFile": "# Literature Map: Dose-Response / Threshold Effects in Data Augmentation\n# Updated: 2026-05-15\n\nentries:\n  # === Category: dose-response / threshold ===\n\n  - id: rolnick2017robust\n    title: \"Deep Learning is Robust to Massive Label Noise\"\n    authors: \"Rolnick, Veit, Belongie, Shavit\"\n    year: 2017\n    venue: arXiv 1705.10694\n    category: dose-response\n    role: background\n    key_finding: \"DNNs maintain >90% accuracy on MNIST even when correct labels are diluted 100:1, as long as correct label remains most likely by a small margin.\"\n    relevance: \"Contrasts with our finding: image classification is robust to extreme noise, while embodied planning shows sharp degradation at 25%. Task complexity mediates noise tolerance.\"\n\n  - id: yuan2024early_stopping\n    title: \"Early Stopping Against Label Noise Without Validation Data\"\n    authors: \"Yuan, Feng, Liu\"\n    year: 2024\n    venue: ICLR 2024\n    category: dose-response\n    role: background\n    key_finding: \"Identifies phase transition where DNNs shift from fitting clean to fitting mislabeled examples. Proposes Label Wave to detect this transition during training.\"\n    relevance: \"Supports existence of phase transition in learning dynamics. Our 10-25% threshold may correspond to such a transition point in the SFT regime.\"\n\n  - id: dohmatob2025collapse\n    title: \"Strong Model Collapse\"\n    authors: \"Dohmatob, Feng, Subramonian, Kempe\"\n    year: 2025\n    venue: ICLR 2025\n    category: threshold\n    role: background\n    key_finding: \"Even 0.1% synthetic data can cause model collapse in supervised regression. Past interpolation threshold, larger models become more robust (double-descent).\"\n    relevance: \"Demonstrates extreme sensitivity to data quality in certain regimes. Our 10-25% threshold is analogous—small quality shifts cause nonlinear degradation.\"\n\n  - id: beyond_clean_data2024\n    title: \"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance\"\n    authors: \"Various\"\n    year: 2024\n    venue: ScienceDirect\n    category: dose-response\n    role: background\n    key_finding: \"Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds.\"\n    relevance: \"Methodologically similar—varies noise proportion to find degradation curves. Shows task-specific threshold behavior.\"\n\n  # === Category: error-injection / failure augmentation ===\n\n  - id: wang2024learning_from_failure\n    title: \"Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents\"\n    authors: \"Wang, Li, Han, Zhang, Baldwin\"\n    year: 2024\n    venue: arXiv 2402.11651\n    category: error-injection\n    role: evaluation\n    key_finding: \"Failed trajectories provide valuable signal for LLM agents via contrastive learning. Negative examples improve math, QA, strategic tasks when properly structured.\"\n    relevance: \"Directly related—injects negative trajectories into agent SFT. Key difference: they use contrastive framing, not raw mixing. Our work shows raw mixing has narrow safe window.\"\n\n  - id: song2024eto\n    title: \"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents\"\n    authors: \"Song, Yin, Yue, Huang, Li, Lin\"\n    year: 2024\n    venue: ACL 2024\n    category: error-injection\n    role: evaluation\n    key_finding: \"Iteratively collects failure trajectories, uses DPO-style contrastive learning on success-failure pairs. +8% WebShop, +9.5% ScienceWorld vs SFT.\"\n    relevance: \"Uses failure trajectories via preference optimization (DPO), not direct SFT mixing. Avoids our threshold problem by never training directly on failures.\"\n\n  - id: paladin2025\n    title: \"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases\"\n    authors: \"Vuddanti, Shah et al.\"\n    year: 2025\n    venue: arXiv 2509.25238\n    category: error-injection\n    role: evaluation\n    key_finding: \"Trains on 50K+ recovery-annotated failure trajectories via LoRA. +57pp recovery rate vs vanilla (32.76%→89.68%), +13.6pp vs CRITIC baseline. Taxonomy of 7 error classes. Includes inference-time retrieval.\"\n    relevance: \"Most similar to our approach (taxonomy-guided error injection). Key difference: they pair failures with recovery demos; we inject standalone error trajectories.\"\n\n  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Various\"\n    year: 2025\n    venue: arXiv 2603.21357\n    category: error-injection\n    role: evaluation\n    key_finding: \"Converts failed trajectories to valid training data by relabeling—failure for task A becomes success for task B.\"\n    relevance: \"Avoids noise problem by redefining failure as success for different goals. Contrasts with our direct injection approach.\"\n\n  # === Category: data-mixing ===\n\n  - id: dong2024composition\n    title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n    authors: \"Dong, Yuan et al.\"\n    year: 2024\n    venue: ACL 2024\n    category: data-mixing\n    role: background\n    key_finding: \"Data amount per domain matters more than ratio. Low-data mixing enables cross-domain transfer; high-data mixing causes ability conflicts.\"\n    relevance: \"Documents ability-conflict at high data amounts—analogous to our threshold. Ratio secondary to amount suggests our threshold may be absolute-count driven.\"\n\n  - id: ye2025mixing_laws\n    title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n    authors: \"Ye et al.\"\n    year: 2025\n    venue: ICLR 2025\n    category: data-mixing\n    role: background\n    key_finding: \"Discovers quantitative scaling laws L=f(r) for mixture proportions. Accurately predicts critical proportion avoiding catastrophic forgetting.\"\n    relevance: \"Their 'critical proportion for catastrophic forgetting' is conceptually identical to our threshold—both mark a phase transition in mixing.\"\n\n  - id: li2025mixing_optimization\n    title: \"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICML 2025\n    category: data-mixing\n    role: background\n    key_finding: \"SFT mixing as optimization with scaling-law parameterization. Optimal weights depend on model size and data scale.\"\n    relevance: \"Optimal mixing is model-size dependent—our 7B model may have different threshold than larger models. Finding is scale-specific.\"\n\n  - id: seddik2024synthetic_bound\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Seddik et al.\"\n    year: 2024\n    venue: arXiv 2404.05090\n    category: data-mixing\n    role: background\n    key_finding: \"Theoretical upper bounds on low-quality data proportion before collapse. Real data proportion must remain high.\"\n    relevance: \"Theoretical grounding for hard thresholds in quality mixing. Our empirical 10-25% window is consistent with their predictions.\"\n\n  # === Category: curriculum / quality threshold ===\n\n  - id: curriculum_robust2021\n    title: \"Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction\"\n    authors: \"Zhou, Wang, Bilmes\"\n    year: 2021\n    venue: ICLR 2021\n    category: curriculum\n    role: background\n    key_finding: \"Networks learn simple patterns first, then overfit noisy labels. Loss-based curriculum selection is unstable; errors accumulate multiplicatively.\"\n    relevance: \"Explains WHY threshold exists: once noisy proportion exceeds implicit curriculum capacity, errors accumulate. Our 25% may exceed model's capacity.\"\n\n  - id: agentprm2025\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    year: 2025\n    venue: arXiv 2502.10325\n    category: curriculum\n    role: evaluation\n    key_finding: \"Best-of-N with process reward model achieves 91.0% on ALFWorld (N=16, base policy 88.1%). Shows reward-guided search outperforms SFT alone.\"\n    relevance: \"ALFWorld SOTA reference. Our 65.3% SFT-only baseline is reasonable given AgentPRM uses test-time search.\"\n\n  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Various\"\n    year: 2024\n    venue: NeurIPS 2024\n    category: curriculum\n    role: evaluation\n    key_finding: \"World knowledge models reduce hallucinatory actions in ALFWorld. SFT on expert trajectories prone to overfitting.\"\n    relevance: \"ALFWorld baseline showing SFT quality sensitivity. Hallucination increase from poor training data parallels our error-injection degradation.\"\n\n  # === Category: training-dynamics / memorization ===\n\n  - id: arpit2017memorization\n    title: \"A Closer Look at Memorization in Deep Networks\"\n    authors: \"Arpit, Jastrzębski, Ballas, Krueger, Bengio, Kanwal, Maharaj, Fischer, Courville, Bengio, Lacoste-Julien\"\n    year: 2017\n    venue: ICML 2017\n    category: training-dynamics\n    role: background\n    key_finding: \"DNNs first learn clean patterns (early learning phase), then memorize noise. Training loss/accuracy improve on noisy data but generalization degrades. Dataset-independent capacity concepts are insufficient.\"\n    relevance: \"Directly explains our '50% injection → lowest train loss but worst eval' paradox. Higher injection = more noisy samples to memorize, better train metrics but worse generalization.\"\n\n  - id: liu2020early_learning_reg\n    title: \"Early-Learning Regularization Prevents Memorization of Noisy Labels\"\n    authors: \"Liu, Niles-Weed, Razavian, Fernandez-Granda\"\n    year: 2020\n    venue: NeurIPS 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Formalizes early learning phenomenon: models predict true labels for mislabeled examples early in training, then memorize wrong labels. ELR regularization exploits this window.\"\n    relevance: \"Our error-injected samples may be correctly handled early in training but memorized later, degrading clean-data generalization. Explains why more epochs could worsen the gap.\"\n\n  - id: zhou2023lima\n    title: \"LIMA: Less Is More for Alignment\"\n    authors: \"Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy\"\n    year: 2023\n    venue: NeurIPS 2023\n    category: training-dynamics\n    role: background\n    key_finding: \"Superficial Alignment Hypothesis: LLM knowledge/capability comes from pretraining; SFT only teaches output style/format. Limited SFT data suffices.\"\n    relevance: \"Explains why lower SFT loss ≠ better downstream capability. Error injection improves surface-level fitting (lower loss) but doesn't enhance—and may damage—pretrained planning capability.\"\n\n  - id: luo2023catastrophic_forgetting\n    title: \"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning\"\n    authors: \"Luo, Yang, Meng, Li, Zhou, Zhang\"\n    year: 2023\n    venue: arXiv 2308.08747\n    category: training-dynamics\n    role: background\n    key_finding: \"SFT is off-policy learning prone to overfit training distribution and forget pretraining knowledge. Forgetting severity increases with divergence between fine-tuning and pretraining distributions.\"\n    relevance: \"Error injection increases distributional gap from pretraining data, accelerating catastrophic forgetting. 50% injection → maximal divergence → most forgetting of planning capability.\"\n\n  - id: longpre2020augmentation\n    title: \"How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?\"\n    authors: \"Longpre, Wang, DuBois\"\n    year: 2020\n    venue: Findings of EMNLP 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift.\"\n    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"\n",
    "structuredPatch": [
      {
        "oldStart": 211,
        "oldLines": 3,
        "newStart": 211,
        "newLines": 35,
        "lines": [
          "     role: background",
          "     key_finding: \"Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift.\"",
          "     relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"",
          "+",
          "+  # === Category: training-instability ===",
          "+",
          "+  - id: mccoy2020seeds",
          "+    title: \"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance\"",
          "+    authors: \"McCoy, Min, Linzen\"",
          "+    year: 2020",
          "+    venue: \"BlackboxNLP Workshop at EMNLP 2020\"",
          "+    category: training-instability",
          "+    role: background",
          "+    key_finding: \"Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization.\"",
          "+    relevance: \"与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity\"",
          "+",
          "+  - id: mosbach2021stability",
          "+    title: \"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines\"",
          "+    authors: \"Mosbach, Andriushchenko, Klakow\"",
          "+    year: 2021",
          "+    venue: \"ICLR 2021\"",
          "+    category: training-instability",
          "+    role: background",
          "+    key_finding: \"BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。\"",
          "+    relevance: \"fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training\"",
          "+",
          "+  - id: damour2022underspecification",
          "+    title: \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"",
          "+    authors: \"D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al.\"",
          "+    year: 2022",
          "+    venue: \"Journal of Machine Learning Research, Vol. 23, No. 226\"",
          "+    category: training-instability",
          "+    role: background",
          "+    key_finding: \"ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。\"",
          "+    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\""
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

已完成。三篇论文元数据均经 WebSearch 验证后追加到 `literature_map.yaml` 末尾：

| ID | 标题 | 作者 | 年份 | Venue |
|---|---|---|---|---|
| `mccoy2020seeds` | BERTs of a feather do not generalize together… | McCoy, Min, Linzen | 2020 | BlackboxNLP@EMNLP 2020 |
| `mosbach2021stability` | On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines | Mosbach, Andriushchenko, Klakow | 2021 | ICLR 2021 |
| `damour2022underspecification` | Underspecification Presents Challenges for Credibility in Modern Machine Learning | D'Amour, Heller, Moldovan, Adlam et al. (40+ authors) | 2022 | JMLR Vol.23 No.226 |

arXiv IDs: `1911.02969` / `2006.04884` / `2011.03395`。

Sources:
- [McCoy et al. - ACL Anthology](https://aclanthology.org/2020.blackboxnlp-1.21/)
- [Mosbach et al. - arXiv](https://arxiv.org/abs/2006.04884)
- [D'Amour et al. - JMLR](https://www.jmlr.org/papers/v23/20-1335.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "uuid": "57e0c3c1-87f3-40e9-b630-bb479e647d4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014K2sefYTjVKw7P8ARJChQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 33190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1668
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

_source line 26_

已完成。三篇论文元数据均经 WebSearch 验证后追加到 `literature_map.yaml` 末尾：

| ID | 标题 | 作者 | 年份 | Venue |
|---|---|---|---|---|
| `mccoy2020seeds` | BERTs of a feather do not generalize together… | McCoy, Min, Linzen | 2020 | BlackboxNLP@EMNLP 2020 |
| `mosbach2021stability` | On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines | Mosbach, Andriushchenko, Klakow | 2021 | ICLR 2021 |
| `damour2022underspecification` | Underspecification Presents Challenges for Credibility in Modern Machine Learning | D'Amour, Heller, Moldovan, Adlam et al. (40+ authors) | 2022 | JMLR Vol.23 No.226 |

arXiv IDs: `1911.02969` / `2006.04884` / `2011.03395`。

Sources:
- [McCoy et al. - ACL Anthology](https://aclanthology.org/2020.blackboxnlp-1.21/)
- [Mosbach et al. - arXiv](https://arxiv.org/abs/2006.04884)
- [D'Amour et al. - JMLR](https://www.jmlr.org/papers/v23/20-1335.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 68743,
  "duration_api_ms": 79444,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "c33bc0db-c545-42d5-a3c1-6a8356ea9646",
  "total_cost_usd": 0.38812875,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 23017,
    "cache_read_input_tokens": 129733,
    "output_tokens": 2634,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 23017,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 401,
        "cache_read_input_tokens": 33190,
        "cache_creation_input_tokens": 1668,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1668
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 64201,
      "outputTokens": 1863,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 4,
      "costUSD": 0.113516,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 2634,
      "cacheReadInputTokens": 129733,
      "cacheCreationInputTokens": 23017,
      "webSearchRequests": 0,
      "costUSD": 0.27461274999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "93268bce-d719-40dc-ab28-49a50971639b"
}
```

</details>

---
