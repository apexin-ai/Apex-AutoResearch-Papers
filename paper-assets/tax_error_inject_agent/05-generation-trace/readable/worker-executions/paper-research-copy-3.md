# paper research

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_paper_research_20260515T033545.log`
- **Structured JSON:** [`b25ba8acbbd4587f8a8a.json`](../../sessions/b2/b25ba8acbbd4587f8a8a.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
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
  "uuid": "c18c851a-7f2c-44e0-8e5c-93af96f25b8a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/memory/"
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
  "uuid": "b2af0dc7-c9d5-4656-a5ea-6fd15535471a",
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to search for two papers, verify their metadata, and append entries to a YAML file. Let me start by searching for both papers and reading the current YAML file in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "b872476f-2915-4206-bf4f-401440ff9c1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G3oMYr68AkfoeKRXzhLLAb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12535,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12535
      },
      "output_tokens": 34,
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

搜索两篇论文并读取现有 YAML 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "e8b83b79-3866-47c0-a2c4-f55150f5f81b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G3oMYr68AkfoeKRXzhLLAb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12535,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12535
      },
      "output_tokens": 34,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Q3bJgfaD2fpYkE6rwQhbuX`</summary>

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
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "8dabeb9a-5ecc-47b5-b7ca-006261f8029a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G3oMYr68AkfoeKRXzhLLAb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12535,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12535
      },
      "output_tokens": 34,
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

_source line 7 · 2026-05-15T03:35:57.455Z_

<details><summary>↩ Tool result · `toolu_01Q3bJgfaD2fpYkE6rwQhbuX`</summary>

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
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "f9987557-8eff-40fc-889b-a038bf7b96a3",
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

<details open><summary>🔧 Tool call — Read · `toolu_012zDfTN1pZeWuzUEEBHPmNA`</summary>

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
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "7a756b0c-38c7-48fd-a6ba-3ff7f7457313",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G3oMYr68AkfoeKRXzhLLAb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12535,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12535
      },
      "output_tokens": 34,
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

_source line 9 · 2026-05-15T03:35:57.713Z_

<details><summary>↩ Tool result · `toolu_012zDfTN1pZeWuzUEEBHPmNA`</summary>

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
215	  # === Category: training-instability ===
216	
217	  - id: mccoy2020seeds
218	    title: "BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance"
219	    authors: "McCoy, Min, Linzen"
220	    year: 2020
221	    venue: "BlackboxNLP Workshop at EMNLP 2020"
222	    category: training-instability
223	    role: background
224	    key_finding: "Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization."
225	    relevance: "与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity"
226	
227	  - id: mosbach2021stability
228	    title: "On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines"
229	    authors: "Mosbach, Andriushchenko, Klakow"
230	    year: 2021
231	    venue: "ICLR 2021"
232	    category: training-instability
233	    role: background
234	    key_finding: "BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。"
235	    relevance: "fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training"
236	
237	  - id: damour2022underspecification
238	    title: "Underspecification Presents Challenges for Credibility in Modern Machine Learning"
239	    authors: "D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al."
240	    year: 2022
241	    venue: "Journal of Machine Learning Research, Vol. 23, No. 226"
242	    category: training-instability
243	    role: background
244	    key_finding: "ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。"
245	    relevance: "我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现"
246	
247	  # === Category: alfworld-methods ===
248	
249	  - id: shridhar2021alfworld
250	    title: "ALFWorld: Aligning Text and Embodied Environments for Interactive Learning"
251	    authors: "Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht"
252	    year: 2021
253	    venue: "ICLR 2021"
254	    arxiv: "2010.03768"
255	    category: alfworld-methods
256	    role: evaluation
257	    key_finding: "Aligns TextWorld text-based environment with ALFRED embodied benchmark, enabling abstract policy learning that transfers to visual grounding."
258	    relevance: "我们的实验环境；134 tasks across 6 task types benchmark"
259	
260	  - id: yao2023react
261	    title: "ReAct: Synergizing Reasoning and Acting in Language Models"
262	    authors: "Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao"
263	    year: 2023
264	    venue: "ICLR 2023"
265	    arxiv: "2210.03629"
266	    category: alfworld-methods
267	    role: evaluation
268	    key_finding: "Interleaved reasoning traces and actions enable LLMs to ground decisions, achieving 75% on ALFWorld (single-trial)."
269	    relevance: "我们使用的 prompting paradigm（ReAct format）"
270	
271	  - id: shinn2023reflexion
272	    title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
273	    authors: "Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao"
274	    year: 2023
275	    venue: "NeurIPS 2023"
276	    arxiv: "2303.11366"
277	    category: alfworld-methods
278	    role: evaluation
279	    key_finding: "Verbal self-reflection in episodic memory achieves 97% on ALFWorld (12 trials, 130/134 tasks solved) without weight updates."
280	    relevance: "Inference-time reflection 成功 where training-time injection 失败——对比 key point"
281	
282	  - id: kim2025coex
283	    title: "CoEx -- Co-evolving World-model and Exploration"
284	    authors: "Kim, Hwang"
285	    year: 2025
286	    venue: "Findings of EMNLP 2025"
287	    arxiv: "2507.22281"
288	    category: alfworld-methods
289	    role: evaluation
290	    key_finding: "Hierarchical state abstraction with dynamically updated neurosymbolic world model achieves 93.28% on ALFWorld."
291	    relevance: "ALFWorld SOTA 参考；co-evolving world model 对比我们的 static SFT 方法"
292	
293	  # === Category: error-injection (补充) ===
294	
295	  - id: eef2025
296	    title: "Exploring Expert Failures Improves LLM Agent Tuning"
297	    authors: "Lan, Bai, Cheng, Wang et al."
298	    year: 2025
299	    venue: "arXiv 2504.13145"
300	    category: error-injection
301	    role: evaluation
302	    key_finding: "从失败 expert trajectories 中提取有益 actions（plans、key actions），用于引导 agent exploration，WebShop SOTA 0.81，SciWorld 81/100。"
303	    relevance: "从失败中提取正向信号（非注入负信号），成功 on WebShop。与我们的直接注入形成对比——方向相反的 failure utilization。"
304	
305	  - id: agentdebug2025
306	    title: "Where LLM Agents Fail and How They can Learn From Failures"
307	    authors: "Zhu, Liu, Li, Tian et al."
308	    year: 2025
309	    venue: "arXiv 2509.25370"
310	    category: error-injection
311	    role: evaluation
312	    key_finding: "5-dimension AgentErrorTaxonomy（memory, reflection, planning, action, system-level）+ AgentErrorBench 标注数据集 + AgentDebug 纠错框架，跨 ALFWorld/GAIA/WebShop 提升 24% all-correct accuracy。"
313	    relevance: "ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。"
314	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "e72a451a-b9ed-4a6c-bc7a-448d6952c02f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
      "content": "# Literature Map: Dose-Response / Threshold Effects in Data Augmentation\n# Updated: 2026-05-15\n\nentries:\n  # === Category: dose-response / threshold ===\n\n  - id: rolnick2017robust\n    title: \"Deep Learning is Robust to Massive Label Noise\"\n    authors: \"Rolnick, Veit, Belongie, Shavit\"\n    year: 2017\n    venue: arXiv 1705.10694\n    category: dose-response\n    role: background\n    key_finding: \"DNNs maintain >90% accuracy on MNIST even when correct labels are diluted 100:1, as long as correct label remains most likely by a small margin.\"\n    relevance: \"Contrasts with our finding: image classification is robust to extreme noise, while embodied planning shows sharp degradation at 25%. Task complexity mediates noise tolerance.\"\n\n  - id: yuan2024early_stopping\n    title: \"Early Stopping Against Label Noise Without Validation Data\"\n    authors: \"Yuan, Feng, Liu\"\n    year: 2024\n    venue: ICLR 2024\n    category: dose-response\n    role: background\n    key_finding: \"Identifies phase transition where DNNs shift from fitting clean to fitting mislabeled examples. Proposes Label Wave to detect this transition during training.\"\n    relevance: \"Supports existence of phase transition in learning dynamics. Our 10-25% threshold may correspond to such a transition point in the SFT regime.\"\n\n  - id: dohmatob2025collapse\n    title: \"Strong Model Collapse\"\n    authors: \"Dohmatob, Feng, Subramonian, Kempe\"\n    year: 2025\n    venue: ICLR 2025\n    category: threshold\n    role: background\n    key_finding: \"Even 0.1% synthetic data can cause model collapse in supervised regression. Past interpolation threshold, larger models become more robust (double-descent).\"\n    relevance: \"Demonstrates extreme sensitivity to data quality in certain regimes. Our 10-25% threshold is analogous—small quality shifts cause nonlinear degradation.\"\n\n  - id: beyond_clean_data2024\n    title: \"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance\"\n    authors: \"Various\"\n    year: 2024\n    venue: ScienceDirect\n    category: dose-response\n    role: background\n    key_finding: \"Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds.\"\n    relevance: \"Methodologically similar—varies noise proportion to find degradation curves. Shows task-specific threshold behavior.\"\n\n  # === Category: error-injection / failure augmentation ===\n\n  - id: wang2024learning_from_failure\n    title: \"Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents\"\n    authors: \"Wang, Li, Han, Zhang, Baldwin\"\n    year: 2024\n    venue: arXiv 2402.11651\n    category: error-injection\n    role: evaluation\n    key_finding: \"Failed trajectories provide valuable signal for LLM agents via contrastive learning. Negative examples improve math, QA, strategic tasks when properly structured.\"\n    relevance: \"Directly related—injects negative trajectories into agent SFT. Key difference: they use contrastive framing, not raw mixing. Our work shows raw mixing has narrow safe window.\"\n\n  - id: song2024eto\n    title: \"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents\"\n    authors: \"Song, Yin, Yue, Huang, Li, Lin\"\n    year: 2024\n    venue: ACL 2024\n    category: error-injection\n    role: evaluation\n    key_finding: \"Iteratively collects failure trajectories, uses DPO-style contrastive learning on success-failure pairs. +8% WebShop, +9.5% ScienceWorld vs SFT.\"\n    relevance: \"Uses failure trajectories via preference optimization (DPO), not direct SFT mixing. Avoids our threshold problem by never training directly on failures.\"\n\n  - id: paladin2025\n    title: \"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases\"\n    authors: \"Vuddanti, Shah et al.\"\n    year: 2025\n    venue: arXiv 2509.25238\n    category: error-injection\n    role: evaluation\n    key_finding: \"Trains on 50K+ recovery-annotated failure trajectories via LoRA. +57pp recovery rate vs vanilla (32.76%→89.68%), +13.6pp vs CRITIC baseline. Taxonomy of 7 error classes. Includes inference-time retrieval.\"\n    relevance: \"Most similar to our approach (taxonomy-guided error injection). Key difference: they pair failures with recovery demos; we inject standalone error trajectories.\"\n\n  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Various\"\n    year: 2025\n    venue: arXiv 2603.21357\n    category: error-injection\n    role: evaluation\n    key_finding: \"Converts failed trajectories to valid training data by relabeling—failure for task A becomes success for task B.\"\n    relevance: \"Avoids noise problem by redefining failure as success for different goals. Contrasts with our direct injection approach.\"\n\n  # === Category: data-mixing ===\n\n  - id: dong2024composition\n    title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n    authors: \"Dong, Yuan et al.\"\n    year: 2024\n    venue: ACL 2024\n    category: data-mixing\n    role: background\n    key_finding: \"Data amount per domain matters more than ratio. Low-data mixing enables cross-domain transfer; high-data mixing causes ability conflicts.\"\n    relevance: \"Documents ability-conflict at high data amounts—analogous to our threshold. Ratio secondary to amount suggests our threshold may be absolute-count driven.\"\n\n  - id: ye2025mixing_laws\n    title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n    authors: \"Ye et al.\"\n    year: 2025\n    venue: ICLR 2025\n    category: data-mixing\n    role: background\n    key_finding: \"Discovers quantitative scaling laws L=f(r) for mixture proportions. Accurately predicts critical proportion avoiding catastrophic forgetting.\"\n    relevance: \"Their 'critical proportion for catastrophic forgetting' is conceptually identical to our threshold—both mark a phase transition in mixing.\"\n\n  - id: li2025mixing_optimization\n    title: \"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICML 2025\n    category: data-mixing\n    role: background\n    key_finding: \"SFT mixing as optimization with scaling-law parameterization. Optimal weights depend on model size and data scale.\"\n    relevance: \"Optimal mixing is model-size dependent—our 7B model may have different threshold than larger models. Finding is scale-specific.\"\n\n  - id: seddik2024synthetic_bound\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Seddik et al.\"\n    year: 2024\n    venue: arXiv 2404.05090\n    category: data-mixing\n    role: background\n    key_finding: \"Theoretical upper bounds on low-quality data proportion before collapse. Real data proportion must remain high.\"\n    relevance: \"Theoretical grounding for hard thresholds in quality mixing. Our empirical 10-25% window is consistent with their predictions.\"\n\n  # === Category: curriculum / quality threshold ===\n\n  - id: curriculum_robust2021\n    title: \"Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction\"\n    authors: \"Zhou, Wang, Bilmes\"\n    year: 2021\n    venue: ICLR 2021\n    category: curriculum\n    role: background\n    key_finding: \"Networks learn simple patterns first, then overfit noisy labels. Loss-based curriculum selection is unstable; errors accumulate multiplicatively.\"\n    relevance: \"Explains WHY threshold exists: once noisy proportion exceeds implicit curriculum capacity, errors accumulate. Our 25% may exceed model's capacity.\"\n\n  - id: agentprm2025\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    year: 2025\n    venue: arXiv 2502.10325\n    category: curriculum\n    role: evaluation\n    key_finding: \"Best-of-N with process reward model achieves 91.0% on ALFWorld (N=16, base policy 88.1%). Shows reward-guided search outperforms SFT alone.\"\n    relevance: \"ALFWorld SOTA reference. Our 65.3% SFT-only baseline is reasonable given AgentPRM uses test-time search.\"\n\n  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Various\"\n    year: 2024\n    venue: NeurIPS 2024\n    category: curriculum\n    role: evaluation\n    key_finding: \"World knowledge models reduce hallucinatory actions in ALFWorld. SFT on expert trajectories prone to overfitting.\"\n    relevance: \"ALFWorld baseline showing SFT quality sensitivity. Hallucination increase from poor training data parallels our error-injection degradation.\"\n\n  # === Category: training-dynamics / memorization ===\n\n  - id: arpit2017memorization\n    title: \"A Closer Look at Memorization in Deep Networks\"\n    authors: \"Arpit, Jastrzębski, Ballas, Krueger, Bengio, Kanwal, Maharaj, Fischer, Courville, Bengio, Lacoste-Julien\"\n    year: 2017\n    venue: ICML 2017\n    category: training-dynamics\n    role: background\n    key_finding: \"DNNs first learn clean patterns (early learning phase), then memorize noise. Training loss/accuracy improve on noisy data but generalization degrades. Dataset-independent capacity concepts are insufficient.\"\n    relevance: \"Directly explains our '50% injection → lowest train loss but worst eval' paradox. Higher injection = more noisy samples to memorize, better train metrics but worse generalization.\"\n\n  - id: liu2020early_learning_reg\n    title: \"Early-Learning Regularization Prevents Memorization of Noisy Labels\"\n    authors: \"Liu, Niles-Weed, Razavian, Fernandez-Granda\"\n    year: 2020\n    venue: NeurIPS 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Formalizes early learning phenomenon: models predict true labels for mislabeled examples early in training, then memorize wrong labels. ELR regularization exploits this window.\"\n    relevance: \"Our error-injected samples may be correctly handled early in training but memorized later, degrading clean-data generalization. Explains why more epochs could worsen the gap.\"\n\n  - id: zhou2023lima\n    title: \"LIMA: Less Is More for Alignment\"\n    authors: \"Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy\"\n    year: 2023\n    venue: NeurIPS 2023\n    category: training-dynamics\n    role: background\n    key_finding: \"Superficial Alignment Hypothesis: LLM knowledge/capability comes from pretraining; SFT only teaches output style/format. Limited SFT data suffices.\"\n    relevance: \"Explains why lower SFT loss ≠ better downstream capability. Error injection improves surface-level fitting (lower loss) but doesn't enhance—and may damage—pretrained planning capability.\"\n\n  - id: luo2023catastrophic_forgetting\n    title: \"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning\"\n    authors: \"Luo, Yang, Meng, Li, Zhou, Zhang\"\n    year: 2023\n    venue: arXiv 2308.08747\n    category: training-dynamics\n    role: background\n    key_finding: \"SFT is off-policy learning prone to overfit training distribution and forget pretraining knowledge. Forgetting severity increases with divergence between fine-tuning and pretraining distributions.\"\n    relevance: \"Error injection increases distributional gap from pretraining data, accelerating catastrophic forgetting. 50% injection → maximal divergence → most forgetting of planning capability.\"\n\n  - id: longpre2020augmentation\n    title: \"How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?\"\n    authors: \"Longpre, Wang, DuBois\"\n    year: 2020\n    venue: Findings of EMNLP 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift.\"\n    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"\n\n  # === Category: training-instability ===\n\n  - id: mccoy2020seeds\n    title: \"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance\"\n    authors: \"McCoy, Min, Linzen\"\n    year: 2020\n    venue: \"BlackboxNLP Workshop at EMNLP 2020\"\n    category: training-instability\n    role: background\n    key_finding: \"Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization.\"\n    relevance: \"与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity\"\n\n  - id: mosbach2021stability\n    title: \"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines\"\n    authors: \"Mosbach, Andriushchenko, Klakow\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    category: training-instability\n    role: background\n    key_finding: \"BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。\"\n    relevance: \"fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training\"\n\n  - id: damour2022underspecification\n    title: \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"\n    authors: \"D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al.\"\n    year: 2022\n    venue: \"Journal of Machine Learning Research, Vol. 23, No. 226\"\n    category: training-instability\n    role: background\n    key_finding: \"ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。\"\n    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"\n\n  # === Category: alfworld-methods ===\n\n  - id: shridhar2021alfworld\n    title: \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\"\n    authors: \"Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    arxiv: \"2010.03768\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Aligns TextWorld text-based environment with ALFRED embodied benchmark, enabling abstract policy learning that transfers to visual grounding.\"\n    relevance: \"我们的实验环境；134 tasks across 6 task types benchmark\"\n\n  - id: yao2023react\n    title: \"ReAct: Synergizing Reasoning and Acting in Language Models\"\n    authors: \"Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.03629\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Interleaved reasoning traces and actions enable LLMs to ground decisions, achieving 75% on ALFWorld (single-trial).\"\n    relevance: \"我们使用的 prompting paradigm（ReAct format）\"\n\n  - id: shinn2023reflexion\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2303.11366\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Verbal self-reflection in episodic memory achieves 97% on ALFWorld (12 trials, 130/134 tasks solved) without weight updates.\"\n    relevance: \"Inference-time reflection 成功 where training-time injection 失败——对比 key point\"\n\n  - id: kim2025coex\n    title: \"CoEx -- Co-evolving World-model and Exploration\"\n    authors: \"Kim, Hwang\"\n    year: 2025\n    venue: \"Findings of EMNLP 2025\"\n    arxiv: \"2507.22281\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Hierarchical state abstraction with dynamically updated neurosymbolic world model achieves 93.28% on ALFWorld.\"\n    relevance: \"ALFWorld SOTA 参考；co-evolving world model 对比我们的 static SFT 方法\"\n\n  # === Category: error-injection (补充) ===\n\n  - id: eef2025\n    title: \"Exploring Expert Failures Improves LLM Agent Tuning\"\n    authors: \"Lan, Bai, Cheng, Wang et al.\"\n    year: 2025\n    venue: \"arXiv 2504.13145\"\n    category: error-injection\n    role: evaluation\n    key_finding: \"从失败 expert trajectories 中提取有益 actions（plans、key actions），用于引导 agent exploration，WebShop SOTA 0.81，SciWorld 81/100。\"\n    relevance: \"从失败中提取正向信号（非注入负信号），成功 on WebShop。与我们的直接注入形成对比——方向相反的 failure utilization。\"\n\n  - id: agentdebug2025\n    title: \"Where LLM Agents Fail and How They can Learn From Failures\"\n    authors: \"Zhu, Liu, Li, Tian et al.\"\n    year: 2025\n    venue: \"arXiv 2509.25370\"\n    category: error-injection\n    role: evaluation\n    key_finding: \"5-dimension AgentErrorTaxonomy（memory, reflection, planning, action, system-level）+ AgentErrorBench 标注数据集 + AgentDebug 纠错框架，跨 ALFWorld/GAIA/WebShop 提升 24% all-correct accuracy。\"\n    relevance: \"ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。\"\n",
      "numLines": 314,
      "startLine": 1,
      "totalLines": 314
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K9KxQo9YzymHAehmudeWYS`</summary>

```json
{
  "query": "Bengio Curriculum Learning ICML 2009"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "cdf5553a-513e-41f0-b608-c6e877155052",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbxY1SocGU8ACsCEYFscnq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6508,
      "cache_read_input_tokens": 23982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6508
      },
      "output_tokens": 42,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KhdhiRTB7Y7YaN4q6siGix`</summary>

```json
{
  "query": "Madry adversarial training PGD ICLR 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "56b1bc55-c826-4667-bc94-2941a3ce4916",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbxY1SocGU8ACsCEYFscnq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6508,
      "cache_read_input_tokens": 23982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6508
      },
      "output_tokens": 42,
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

_source line 12 · 2026-05-15T03:36:10.996Z_

<details><summary>↩ Tool result · `toolu_01K9KxQo9YzymHAehmudeWYS`</summary>

```text
Web search results for query: "Bengio Curriculum Learning ICML 2009"

Links: [{"title":"Curriculum learning | Proceedings of the 26th Annual International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.1145/1553374.1553380"},{"title":"Curriculum Learning Yoshua Bengio1 Yoshua.Bengio@umontreal.ca","url":"https://ronan.collobert.com/pub/2009_curriculum_icml.pdf"},{"title":"Curriculum learning","url":"https://bibbase.org/network/publication/bengio-louradour-collobert-weston-curriculumlearning-2009"},{"title":"[PDF] Curriculum learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Curriculum-learning-Bengio-Louradour/8de174ab5419b9d3127695405efd079808e956e8"},{"title":"Bengio, 2009 Curriculum Learning.pdf","url":"https://www.scribd.com/document/425393423/Bengio-2009-Curriculum-Learning-pdf"},{"title":"(PDF) Curriculum learning","url":"https://www.academia.edu/58928901/Curriculum_learning"},{"title":"Under review as a conference paper at ICLR 2020 CURRICULUM LEARNING","url":"https://openreview.net/pdf?id=BklTQCEtwH"},{"title":"dblp: Curriculum learning.","url":"https://dblp.org/rec/conf/icml/BengioLCW09.html"},{"title":"Curriculum Learning: A Survey","url":"https://arxiv.org/pdf/2101.10382"},{"title":"Curriculum learning (2009) | Yoshua Bengio | 6391 Citations","url":"https://scispace.com/papers/curriculum-learning-a335v5etyf"}]

I found comprehensive information about Bengio's Curriculum Learning paper from ICML 2009. Here are the key findings:

## Publication Details

The paper "Curriculum learning" was authored by Yoshua Bengio, Jérôme Louradour, Ronan Collobert, and Jason Weston at ICML 2009, pages 41-48.

## Main Concept

Humans and animals learn much better when the examples are not randomly presented but organized in a meaningful order which illustrates gradually more concepts, and gradually more complex ones. The authors formalize such training strategies in the context of machine learning, and call them "curriculum learning".

## Key Hypothesis and Findings

The paper explores curriculum learning in the context of training with non-convex training criteria for deep neural networks and shows that significant improvements in generalization can be achieved. 

The authors hypothesize that curriculum learning has both an effect on the speed of convergence of the training process to a minimum and, in the case of non-convex criteria, on the quality of the local minima obtained: curriculum learning can be seen as a particular form of continuation method (a general strategy for global optimization of non-convex functions).

## Impact

The paper proposed curriculum learning as a method to gradually increase the complexity of the data samples used during the training process, which is the most natural way to perform curriculum learning as it represents the most direct way of imitating how humans learn.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "ca668907-f55c-4521-b370-5438a511ca00",
  "tool_use_result": {
    "query": "Bengio Curriculum Learning ICML 2009",
    "results": [
      {
        "tool_use_id": "srvtoolu_019APTVLxkpf9iJv3jBGkcjw",
        "content": [
          {
            "title": "Curriculum learning | Proceedings of the 26th Annual International Conference on Machine Learning",
            "url": "https://dl.acm.org/doi/10.1145/1553374.1553380"
          },
          {
            "title": "Curriculum Learning Yoshua Bengio1 Yoshua.Bengio@umontreal.ca",
            "url": "https://ronan.collobert.com/pub/2009_curriculum_icml.pdf"
          },
          {
            "title": "Curriculum learning",
            "url": "https://bibbase.org/network/publication/bengio-louradour-collobert-weston-curriculumlearning-2009"
          },
          {
            "title": "[PDF] Curriculum learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Curriculum-learning-Bengio-Louradour/8de174ab5419b9d3127695405efd079808e956e8"
          },
          {
            "title": "Bengio, 2009 Curriculum Learning.pdf",
            "url": "https://www.scribd.com/document/425393423/Bengio-2009-Curriculum-Learning-pdf"
          },
          {
            "title": "(PDF) Curriculum learning",
            "url": "https://www.academia.edu/58928901/Curriculum_learning"
          },
          {
            "title": "Under review as a conference paper at ICLR 2020 CURRICULUM LEARNING",
            "url": "https://openreview.net/pdf?id=BklTQCEtwH"
          },
          {
            "title": "dblp: Curriculum learning.",
            "url": "https://dblp.org/rec/conf/icml/BengioLCW09.html"
          },
          {
            "title": "Curriculum Learning: A Survey",
            "url": "https://arxiv.org/pdf/2101.10382"
          },
          {
            "title": "Curriculum learning (2009) | Yoshua Bengio | 6391 Citations",
            "url": "https://scispace.com/papers/curriculum-learning-a335v5etyf"
          }
        ]
      },
      "I found comprehensive information about Bengio's Curriculum Learning paper from ICML 2009. Here are the key findings:\n\n## Publication Details\n\nThe paper \"Curriculum learning\" was authored by Yoshua Bengio, Jérôme Louradour, Ronan Collobert, and Jason Weston at ICML 2009, pages 41-48.\n\n## Main Concept\n\nHumans and animals learn much better when the examples are not randomly presented but organized in a meaningful order which illustrates gradually more concepts, and gradually more complex ones. The authors formalize such training strategies in the context of machine learning, and call them \"curriculum learning\".\n\n## Key Hypothesis and Findings\n\nThe paper explores curriculum learning in the context of training with non-convex training criteria for deep neural networks and shows that significant improvements in generalization can be achieved. \n\nThe authors hypothesize that curriculum learning has both an effect on the speed of convergence of the training process to a minimum and, in the case of non-convex criteria, on the quality of the local minima obtained: curriculum learning can be seen as a particular form of continuation method (a general strategy for global optimization of non-convex functions).\n\n## Impact\n\nThe paper proposed curriculum learning as a method to gradually increase the complexity of the data samples used during the training process, which is the most natural way to perform curriculum learning as it represents the most direct way of imitating how humans learn."
    ],
    "durationSeconds": 6.002448966
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T03:36:11.132Z_

<details><summary>↩ Tool result · `toolu_01KhdhiRTB7Y7YaN4q6siGix`</summary>

```text
Web search results for query: "Madry adversarial training PGD ICLR 2018"

Links: [{"title":"Workshop track - ICLR 2018 ATTACKING THE MADRY DEFENSE MODEL WITH","url":"https://openreview.net/pdf?id=Sy8WeUJPf"},{"title":"Towards deep learning models resistant to adversarial attacks","url":"https://dspace.mit.edu/handle/1721.1/137496"},{"title":"[1706.06083] Towards Deep Learning Models Resistant to Adversarial Attacks","url":"https://arxiv.org/abs/1706.06083"},{"title":"I-PGD-AT: EFFICIENT ADVERSARIAL TRAINING VIA","url":"https://openreview.net/pdf?id=TEt7PsVZux6"},{"title":"Published as a conference paper at ICLR 2018","url":"https://openreview.net/pdf?id=rJzIBfZAb"},{"title":"Towards Deep Learning Models Resistant to Adversarial Attacks | OpenReview","url":"https://openreview.net/forum?id=rJzIBfZAb"},{"title":"Curriculum Adversarial Training Qi-Zhi Cai1∗, Chang Liu2 and Dawn Song2","url":"https://www.ijcai.org/proceedings/2018/0520.pdf"},{"title":"IMPROVING THE GENERALIZATION OF ADVERSARIAL ...","url":"https://openreview.net/pdf?id=SyfIfnC5Ym"},{"title":"On the Convergence and Robustness of Adversarial Training","url":"http://proceedings.mlr.press/v97/wang19i/wang19i.pdf"},{"title":"Under review as a conference paper at ICLR 2023","url":"https://openreview.net/pdf?id=a60Jo7_RUd2"}]

Based on the search results, I found relevant information about the Madry adversarial training work with PGD and ICLR 2018:

The paper "Towards deep learning models resistant to adversarial attacks" by Madry, Makelov, Schmidt, Tsipras, and Vladu was published at ICLR 2018.

The work studies adversarial robustness of neural networks through the lens of robust optimization, and enables identification of methods for both training and attacking neural networks that are reliable and universal.

Projected Gradient Descent Adversarial Training (PGD-AT) by Madry et al., 2018 approximately solves the inner maximization problem by multiple steps of projected gradient descent and achieves empirical robustness.

The Projected Gradient Descent (PGD) adversary was introduced by Madry et al. (2018) without random start, which is a stronger iterative variant of FGSM.

PGD-AT (Madry et al., 2018), as the most popular adversarial training method, brings consistent improvements on robustness against various attacks and inspires several adversarial training methods.

This seminal work established PGD-based adversarial training as a fundamental approach for improving neural network robustness against adversarial examples, and it has become highly influential in the adversarial machine learning community.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "3bee7202-2d2f-4465-a133-5fd6b598e195",
  "tool_use_result": {
    "query": "Madry adversarial training PGD ICLR 2018",
    "results": [
      {
        "tool_use_id": "srvtoolu_011EKK97fFuWTkaZwg2YyBAe",
        "content": [
          {
            "title": "Workshop track - ICLR 2018 ATTACKING THE MADRY DEFENSE MODEL WITH",
            "url": "https://openreview.net/pdf?id=Sy8WeUJPf"
          },
          {
            "title": "Towards deep learning models resistant to adversarial attacks",
            "url": "https://dspace.mit.edu/handle/1721.1/137496"
          },
          {
            "title": "[1706.06083] Towards Deep Learning Models Resistant to Adversarial Attacks",
            "url": "https://arxiv.org/abs/1706.06083"
          },
          {
            "title": "I-PGD-AT: EFFICIENT ADVERSARIAL TRAINING VIA",
            "url": "https://openreview.net/pdf?id=TEt7PsVZux6"
          },
          {
            "title": "Published as a conference paper at ICLR 2018",
            "url": "https://openreview.net/pdf?id=rJzIBfZAb"
          },
          {
            "title": "Towards Deep Learning Models Resistant to Adversarial Attacks | OpenReview",
            "url": "https://openreview.net/forum?id=rJzIBfZAb"
          },
          {
            "title": "Curriculum Adversarial Training Qi-Zhi Cai1∗, Chang Liu2 and Dawn Song2",
            "url": "https://www.ijcai.org/proceedings/2018/0520.pdf"
          },
          {
            "title": "IMPROVING THE GENERALIZATION OF ADVERSARIAL ...",
            "url": "https://openreview.net/pdf?id=SyfIfnC5Ym"
          },
          {
            "title": "On the Convergence and Robustness of Adversarial Training",
            "url": "http://proceedings.mlr.press/v97/wang19i/wang19i.pdf"
          },
          {
            "title": "Under review as a conference paper at ICLR 2023",
            "url": "https://openreview.net/pdf?id=a60Jo7_RUd2"
          }
        ]
      },
      "Based on the search results, I found relevant information about the Madry adversarial training work with PGD and ICLR 2018:\n\nThe paper \"Towards deep learning models resistant to adversarial attacks\" by Madry, Makelov, Schmidt, Tsipras, and Vladu was published at ICLR 2018.\n\nThe work studies adversarial robustness of neural networks through the lens of robust optimization, and enables identification of methods for both training and attacking neural networks that are reliable and universal.\n\nProjected Gradient Descent Adversarial Training (PGD-AT) by Madry et al., 2018 approximately solves the inner maximization problem by multiple steps of projected gradient descent and achieves empirical robustness.\n\nThe Projected Gradient Descent (PGD) adversary was introduced by Madry et al. (2018) without random start, which is a stronger iterative variant of FGSM.\n\nPGD-AT (Madry et al., 2018), as the most popular adversarial training method, brings consistent improvements on robustness against various attacks and inspires several adversarial training methods.\n\nThis seminal work established PGD-based adversarial training as a fundamental approach for improving neural network robustness against adversarial examples, and it has become highly influential in the adversarial machine learning community."
    ],
    "durationSeconds": 5.8425834699999974
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
I have the information I need:

1. **Bengio et al. (2009)**: "Curriculum Learning" by Yoshua Bengio, Jérôme Louradour, Ronan Collobert, and Jason Weston. ICML 2009.

2. **Madry et al. (2018)**: "Towards Deep Learning Models Resistant to Adversarial Attacks" by Aleksander Madry, Aleksandar Makelov, Ludwig Schmidt, Dimitris Tsipras, and Adrian Vladu. ICLR 2018.

Now I need to append to the YAML file. 

The file ends at line 314, so I'll add these two entries after the last existing entry while preserving the indentation pattern—each entry should be indented with 2 spaces under the `entries:` section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "4fc79550-6a23-4645-9177-a15e96f32ab8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YRSPHjrRYpHf7CpCN9pvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1786,
      "cache_read_input_tokens": 30490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1786
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

_source line 15_

两篇论文元数据已验证。追加到 YAML。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "1b4743d3-322d-4acb-86a2-5ba9cc32735d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YRSPHjrRYpHf7CpCN9pvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1786,
      "cache_read_input_tokens": 30490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1786
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

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_01Qto8DNuP95LyQuqbWFCoUT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
  "old_string": "    relevance: \"ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。\"",
  "new_string": "    relevance: \"ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。\"\n\n  # === Category: data-mixing / curriculum (补充) ===\n\n  - id: bengio2009curriculum\n    title: \"Curriculum Learning\"\n    authors: \"Bengio, Louradour, Collobert, Weston\"\n    year: 2009\n    venue: \"ICML 2009\"\n    category: curriculum\n    role: background\n    key_finding: \"按难度递增顺序呈现训练样本可加速收敛并改善非凸优化的局部最优质量；curriculum 本质是一种 continuation method。\"\n    relevance: \"Curriculum learning 中 difficult example proportion 的 threshold 概念与我们的 dose-response 阈值平行——训练数据中困难/噪声样本超过阈值后性能崩溃\"\n\n  - id: madry2018adversarial\n    title: \"Towards Deep Learning Models Resistant to Adversarial Attacks\"\n    authors: \"Madry, Makelov, Schmidt, Tsipras, Vladu\"\n    year: 2018\n    venue: \"ICLR 2018\"\n    category: data-mixing\n    role: background\n    key_finding: \"基于 PGD 的 adversarial training 通过 robust optimization 框架显著提升对抗鲁棒性，但以 clean accuracy 下降为代价。\"\n    relevance: \"Adversarial training 的 accuracy-robustness tradeoff 是 dose-response 型——增加 adversarial perturbation 强度提升鲁棒性但降低 clean accuracy，与我们的 injection ratio vs clean eval tradeoff 结构相似\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "3924c07f-6f1d-45ca-a126-9a015aadf7cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YRSPHjrRYpHf7CpCN9pvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1786,
      "cache_read_input_tokens": 30490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1786
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

_source line 17 · 2026-05-15T03:36:31.429Z_

<details><summary>↩ Tool result · `toolu_01Qto8DNuP95LyQuqbWFCoUT`</summary>

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
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "998f6d46-f6db-472f-a1d7-96a18536ef77",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
    "oldString": "    relevance: \"ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。\"",
    "newString": "    relevance: \"ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。\"\n\n  # === Category: data-mixing / curriculum (补充) ===\n\n  - id: bengio2009curriculum\n    title: \"Curriculum Learning\"\n    authors: \"Bengio, Louradour, Collobert, Weston\"\n    year: 2009\n    venue: \"ICML 2009\"\n    category: curriculum\n    role: background\n    key_finding: \"按难度递增顺序呈现训练样本可加速收敛并改善非凸优化的局部最优质量；curriculum 本质是一种 continuation method。\"\n    relevance: \"Curriculum learning 中 difficult example proportion 的 threshold 概念与我们的 dose-response 阈值平行——训练数据中困难/噪声样本超过阈值后性能崩溃\"\n\n  - id: madry2018adversarial\n    title: \"Towards Deep Learning Models Resistant to Adversarial Attacks\"\n    authors: \"Madry, Makelov, Schmidt, Tsipras, Vladu\"\n    year: 2018\n    venue: \"ICLR 2018\"\n    category: data-mixing\n    role: background\n    key_finding: \"基于 PGD 的 adversarial training 通过 robust optimization 框架显著提升对抗鲁棒性，但以 clean accuracy 下降为代价。\"\n    relevance: \"Adversarial training 的 accuracy-robustness tradeoff 是 dose-response 型——增加 adversarial perturbation 强度提升鲁棒性但降低 clean accuracy，与我们的 injection ratio vs clean eval tradeoff 结构相似\"",
    "originalFile": "# Literature Map: Dose-Response / Threshold Effects in Data Augmentation\n# Updated: 2026-05-15\n\nentries:\n  # === Category: dose-response / threshold ===\n\n  - id: rolnick2017robust\n    title: \"Deep Learning is Robust to Massive Label Noise\"\n    authors: \"Rolnick, Veit, Belongie, Shavit\"\n    year: 2017\n    venue: arXiv 1705.10694\n    category: dose-response\n    role: background\n    key_finding: \"DNNs maintain >90% accuracy on MNIST even when correct labels are diluted 100:1, as long as correct label remains most likely by a small margin.\"\n    relevance: \"Contrasts with our finding: image classification is robust to extreme noise, while embodied planning shows sharp degradation at 25%. Task complexity mediates noise tolerance.\"\n\n  - id: yuan2024early_stopping\n    title: \"Early Stopping Against Label Noise Without Validation Data\"\n    authors: \"Yuan, Feng, Liu\"\n    year: 2024\n    venue: ICLR 2024\n    category: dose-response\n    role: background\n    key_finding: \"Identifies phase transition where DNNs shift from fitting clean to fitting mislabeled examples. Proposes Label Wave to detect this transition during training.\"\n    relevance: \"Supports existence of phase transition in learning dynamics. Our 10-25% threshold may correspond to such a transition point in the SFT regime.\"\n\n  - id: dohmatob2025collapse\n    title: \"Strong Model Collapse\"\n    authors: \"Dohmatob, Feng, Subramonian, Kempe\"\n    year: 2025\n    venue: ICLR 2025\n    category: threshold\n    role: background\n    key_finding: \"Even 0.1% synthetic data can cause model collapse in supervised regression. Past interpolation threshold, larger models become more robust (double-descent).\"\n    relevance: \"Demonstrates extreme sensitivity to data quality in certain regimes. Our 10-25% threshold is analogous—small quality shifts cause nonlinear degradation.\"\n\n  - id: beyond_clean_data2024\n    title: \"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance\"\n    authors: \"Various\"\n    year: 2024\n    venue: ScienceDirect\n    category: dose-response\n    role: background\n    key_finding: \"Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds.\"\n    relevance: \"Methodologically similar—varies noise proportion to find degradation curves. Shows task-specific threshold behavior.\"\n\n  # === Category: error-injection / failure augmentation ===\n\n  - id: wang2024learning_from_failure\n    title: \"Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents\"\n    authors: \"Wang, Li, Han, Zhang, Baldwin\"\n    year: 2024\n    venue: arXiv 2402.11651\n    category: error-injection\n    role: evaluation\n    key_finding: \"Failed trajectories provide valuable signal for LLM agents via contrastive learning. Negative examples improve math, QA, strategic tasks when properly structured.\"\n    relevance: \"Directly related—injects negative trajectories into agent SFT. Key difference: they use contrastive framing, not raw mixing. Our work shows raw mixing has narrow safe window.\"\n\n  - id: song2024eto\n    title: \"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents\"\n    authors: \"Song, Yin, Yue, Huang, Li, Lin\"\n    year: 2024\n    venue: ACL 2024\n    category: error-injection\n    role: evaluation\n    key_finding: \"Iteratively collects failure trajectories, uses DPO-style contrastive learning on success-failure pairs. +8% WebShop, +9.5% ScienceWorld vs SFT.\"\n    relevance: \"Uses failure trajectories via preference optimization (DPO), not direct SFT mixing. Avoids our threshold problem by never training directly on failures.\"\n\n  - id: paladin2025\n    title: \"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases\"\n    authors: \"Vuddanti, Shah et al.\"\n    year: 2025\n    venue: arXiv 2509.25238\n    category: error-injection\n    role: evaluation\n    key_finding: \"Trains on 50K+ recovery-annotated failure trajectories via LoRA. +57pp recovery rate vs vanilla (32.76%→89.68%), +13.6pp vs CRITIC baseline. Taxonomy of 7 error classes. Includes inference-time retrieval.\"\n    relevance: \"Most similar to our approach (taxonomy-guided error injection). Key difference: they pair failures with recovery demos; we inject standalone error trajectories.\"\n\n  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Various\"\n    year: 2025\n    venue: arXiv 2603.21357\n    category: error-injection\n    role: evaluation\n    key_finding: \"Converts failed trajectories to valid training data by relabeling—failure for task A becomes success for task B.\"\n    relevance: \"Avoids noise problem by redefining failure as success for different goals. Contrasts with our direct injection approach.\"\n\n  # === Category: data-mixing ===\n\n  - id: dong2024composition\n    title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n    authors: \"Dong, Yuan et al.\"\n    year: 2024\n    venue: ACL 2024\n    category: data-mixing\n    role: background\n    key_finding: \"Data amount per domain matters more than ratio. Low-data mixing enables cross-domain transfer; high-data mixing causes ability conflicts.\"\n    relevance: \"Documents ability-conflict at high data amounts—analogous to our threshold. Ratio secondary to amount suggests our threshold may be absolute-count driven.\"\n\n  - id: ye2025mixing_laws\n    title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n    authors: \"Ye et al.\"\n    year: 2025\n    venue: ICLR 2025\n    category: data-mixing\n    role: background\n    key_finding: \"Discovers quantitative scaling laws L=f(r) for mixture proportions. Accurately predicts critical proportion avoiding catastrophic forgetting.\"\n    relevance: \"Their 'critical proportion for catastrophic forgetting' is conceptually identical to our threshold—both mark a phase transition in mixing.\"\n\n  - id: li2025mixing_optimization\n    title: \"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICML 2025\n    category: data-mixing\n    role: background\n    key_finding: \"SFT mixing as optimization with scaling-law parameterization. Optimal weights depend on model size and data scale.\"\n    relevance: \"Optimal mixing is model-size dependent—our 7B model may have different threshold than larger models. Finding is scale-specific.\"\n\n  - id: seddik2024synthetic_bound\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Seddik et al.\"\n    year: 2024\n    venue: arXiv 2404.05090\n    category: data-mixing\n    role: background\n    key_finding: \"Theoretical upper bounds on low-quality data proportion before collapse. Real data proportion must remain high.\"\n    relevance: \"Theoretical grounding for hard thresholds in quality mixing. Our empirical 10-25% window is consistent with their predictions.\"\n\n  # === Category: curriculum / quality threshold ===\n\n  - id: curriculum_robust2021\n    title: \"Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction\"\n    authors: \"Zhou, Wang, Bilmes\"\n    year: 2021\n    venue: ICLR 2021\n    category: curriculum\n    role: background\n    key_finding: \"Networks learn simple patterns first, then overfit noisy labels. Loss-based curriculum selection is unstable; errors accumulate multiplicatively.\"\n    relevance: \"Explains WHY threshold exists: once noisy proportion exceeds implicit curriculum capacity, errors accumulate. Our 25% may exceed model's capacity.\"\n\n  - id: agentprm2025\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    year: 2025\n    venue: arXiv 2502.10325\n    category: curriculum\n    role: evaluation\n    key_finding: \"Best-of-N with process reward model achieves 91.0% on ALFWorld (N=16, base policy 88.1%). Shows reward-guided search outperforms SFT alone.\"\n    relevance: \"ALFWorld SOTA reference. Our 65.3% SFT-only baseline is reasonable given AgentPRM uses test-time search.\"\n\n  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Various\"\n    year: 2024\n    venue: NeurIPS 2024\n    category: curriculum\n    role: evaluation\n    key_finding: \"World knowledge models reduce hallucinatory actions in ALFWorld. SFT on expert trajectories prone to overfitting.\"\n    relevance: \"ALFWorld baseline showing SFT quality sensitivity. Hallucination increase from poor training data parallels our error-injection degradation.\"\n\n  # === Category: training-dynamics / memorization ===\n\n  - id: arpit2017memorization\n    title: \"A Closer Look at Memorization in Deep Networks\"\n    authors: \"Arpit, Jastrzębski, Ballas, Krueger, Bengio, Kanwal, Maharaj, Fischer, Courville, Bengio, Lacoste-Julien\"\n    year: 2017\n    venue: ICML 2017\n    category: training-dynamics\n    role: background\n    key_finding: \"DNNs first learn clean patterns (early learning phase), then memorize noise. Training loss/accuracy improve on noisy data but generalization degrades. Dataset-independent capacity concepts are insufficient.\"\n    relevance: \"Directly explains our '50% injection → lowest train loss but worst eval' paradox. Higher injection = more noisy samples to memorize, better train metrics but worse generalization.\"\n\n  - id: liu2020early_learning_reg\n    title: \"Early-Learning Regularization Prevents Memorization of Noisy Labels\"\n    authors: \"Liu, Niles-Weed, Razavian, Fernandez-Granda\"\n    year: 2020\n    venue: NeurIPS 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Formalizes early learning phenomenon: models predict true labels for mislabeled examples early in training, then memorize wrong labels. ELR regularization exploits this window.\"\n    relevance: \"Our error-injected samples may be correctly handled early in training but memorized later, degrading clean-data generalization. Explains why more epochs could worsen the gap.\"\n\n  - id: zhou2023lima\n    title: \"LIMA: Less Is More for Alignment\"\n    authors: \"Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy\"\n    year: 2023\n    venue: NeurIPS 2023\n    category: training-dynamics\n    role: background\n    key_finding: \"Superficial Alignment Hypothesis: LLM knowledge/capability comes from pretraining; SFT only teaches output style/format. Limited SFT data suffices.\"\n    relevance: \"Explains why lower SFT loss ≠ better downstream capability. Error injection improves surface-level fitting (lower loss) but doesn't enhance—and may damage—pretrained planning capability.\"\n\n  - id: luo2023catastrophic_forgetting\n    title: \"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning\"\n    authors: \"Luo, Yang, Meng, Li, Zhou, Zhang\"\n    year: 2023\n    venue: arXiv 2308.08747\n    category: training-dynamics\n    role: background\n    key_finding: \"SFT is off-policy learning prone to overfit training distribution and forget pretraining knowledge. Forgetting severity increases with divergence between fine-tuning and pretraining distributions.\"\n    relevance: \"Error injection increases distributional gap from pretraining data, accelerating catastrophic forgetting. 50% injection → maximal divergence → most forgetting of planning capability.\"\n\n  - id: longpre2020augmentation\n    title: \"How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?\"\n    authors: \"Longpre, Wang, DuBois\"\n    year: 2020\n    venue: Findings of EMNLP 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift.\"\n    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"\n\n  # === Category: training-instability ===\n\n  - id: mccoy2020seeds\n    title: \"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance\"\n    authors: \"McCoy, Min, Linzen\"\n    year: 2020\n    venue: \"BlackboxNLP Workshop at EMNLP 2020\"\n    category: training-instability\n    role: background\n    key_finding: \"Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization.\"\n    relevance: \"与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity\"\n\n  - id: mosbach2021stability\n    title: \"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines\"\n    authors: \"Mosbach, Andriushchenko, Klakow\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    category: training-instability\n    role: background\n    key_finding: \"BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。\"\n    relevance: \"fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training\"\n\n  - id: damour2022underspecification\n    title: \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"\n    authors: \"D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al.\"\n    year: 2022\n    venue: \"Journal of Machine Learning Research, Vol. 23, No. 226\"\n    category: training-instability\n    role: background\n    key_finding: \"ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。\"\n    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"\n\n  # === Category: alfworld-methods ===\n\n  - id: shridhar2021alfworld\n    title: \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\"\n    authors: \"Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    arxiv: \"2010.03768\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Aligns TextWorld text-based environment with ALFRED embodied benchmark, enabling abstract policy learning that transfers to visual grounding.\"\n    relevance: \"我们的实验环境；134 tasks across 6 task types benchmark\"\n\n  - id: yao2023react\n    title: \"ReAct: Synergizing Reasoning and Acting in Language Models\"\n    authors: \"Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.03629\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Interleaved reasoning traces and actions enable LLMs to ground decisions, achieving 75% on ALFWorld (single-trial).\"\n    relevance: \"我们使用的 prompting paradigm（ReAct format）\"\n\n  - id: shinn2023reflexion\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2303.11366\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Verbal self-reflection in episodic memory achieves 97% on ALFWorld (12 trials, 130/134 tasks solved) without weight updates.\"\n    relevance: \"Inference-time reflection 成功 where training-time injection 失败——对比 key point\"\n\n  - id: kim2025coex\n    title: \"CoEx -- Co-evolving World-model and Exploration\"\n    authors: \"Kim, Hwang\"\n    year: 2025\n    venue: \"Findings of EMNLP 2025\"\n    arxiv: \"2507.22281\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Hierarchical state abstraction with dynamically updated neurosymbolic world model achieves 93.28% on ALFWorld.\"\n    relevance: \"ALFWorld SOTA 参考；co-evolving world model 对比我们的 static SFT 方法\"\n\n  # === Category: error-injection (补充) ===\n\n  - id: eef2025\n    title: \"Exploring Expert Failures Improves LLM Agent Tuning\"\n    authors: \"Lan, Bai, Cheng, Wang et al.\"\n    year: 2025\n    venue: \"arXiv 2504.13145\"\n    category: error-injection\n    role: evaluation\n    key_finding: \"从失败 expert trajectories 中提取有益 actions（plans、key actions），用于引导 agent exploration，WebShop SOTA 0.81，SciWorld 81/100。\"\n    relevance: \"从失败中提取正向信号（非注入负信号），成功 on WebShop。与我们的直接注入形成对比——方向相反的 failure utilization。\"\n\n  - id: agentdebug2025\n    title: \"Where LLM Agents Fail and How They can Learn From Failures\"\n    authors: \"Zhu, Liu, Li, Tian et al.\"\n    year: 2025\n    venue: \"arXiv 2509.25370\"\n    category: error-injection\n    role: evaluation\n    key_finding: \"5-dimension AgentErrorTaxonomy（memory, reflection, planning, action, system-level）+ AgentErrorBench 标注数据集 + AgentDebug 纠错框架，跨 ALFWorld/GAIA/WebShop 提升 24% all-correct accuracy。\"\n    relevance: \"ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。\"\n",
    "structuredPatch": [
      {
        "oldStart": 311,
        "oldLines": 3,
        "newStart": 311,
        "newLines": 25,
        "lines": [
          "     role: evaluation",
          "     key_finding: \"5-dimension AgentErrorTaxonomy（memory, reflection, planning, action, system-level）+ AgentErrorBench 标注数据集 + AgentDebug 纠错框架，跨 ALFWorld/GAIA/WebShop 提升 24% all-correct accuracy。\"",
          "     relevance: \"ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。\"",
          "+",
          "+  # === Category: data-mixing / curriculum (补充) ===",
          "+",
          "+  - id: bengio2009curriculum",
          "+    title: \"Curriculum Learning\"",
          "+    authors: \"Bengio, Louradour, Collobert, Weston\"",
          "+    year: 2009",
          "+    venue: \"ICML 2009\"",
          "+    category: curriculum",
          "+    role: background",
          "+    key_finding: \"按难度递增顺序呈现训练样本可加速收敛并改善非凸优化的局部最优质量；curriculum 本质是一种 continuation method。\"",
          "+    relevance: \"Curriculum learning 中 difficult example proportion 的 threshold 概念与我们的 dose-response 阈值平行——训练数据中困难/噪声样本超过阈值后性能崩溃\"",
          "+",
          "+  - id: madry2018adversarial",
          "+    title: \"Towards Deep Learning Models Resistant to Adversarial Attacks\"",
          "+    authors: \"Madry, Makelov, Schmidt, Tsipras, Vladu\"",
          "+    year: 2018",
          "+    venue: \"ICLR 2018\"",
          "+    category: data-mixing",
          "+    role: background",
          "+    key_finding: \"基于 PGD 的 adversarial training 通过 robust optimization 框架显著提升对抗鲁棒性，但以 clean accuracy 下降为代价。\"",
          "+    relevance: \"Adversarial training 的 accuracy-robustness tradeoff 是 dose-response 型——增加 adversarial perturbation 强度提升鲁棒性但降低 clean accuracy，与我们的 injection ratio vs clean eval tradeoff 结构相似\""
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

_source line 18_

已追加 2 条条目：

- **bengio2009curriculum** — Bengio, Louradour, Collobert, Weston. "Curriculum Learning". ICML 2009.
- **madry2018adversarial** — Madry, Makelov, Schmidt, Tsipras, Vladu. "Towards Deep Learning Models Resistant to Adversarial Attacks". ICLR 2018.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "uuid": "f64aa74e-2fb4-4ae2-990a-0a0fd6c430da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kStKrab7YZUjNACGWuc8i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 960,
      "cache_read_input_tokens": 32276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 960
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

已追加 2 条条目：

- **bengio2009curriculum** — Bengio, Louradour, Collobert, Weston. "Curriculum Learning". ICML 2009.
- **madry2018adversarial** — Madry, Makelov, Schmidt, Tsipras, Vladu. "Towards Deep Learning Models Resistant to Adversarial Attacks". ICLR 2018.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 41965,
  "duration_api_ms": 49077,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "e3447104-8fab-470c-8d0a-f3330aadb4ed",
  "total_cost_usd": 0.28444175,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 21789,
    "cache_read_input_tokens": 98195,
    "output_tokens": 1334,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21789,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 108,
        "cache_read_input_tokens": 32276,
        "cache_creation_input_tokens": 960,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 960
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 41143,
      "outputTokens": 927,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 2,
      "costUSD": 0.065778,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 1334,
      "cacheReadInputTokens": 98195,
      "cacheCreationInputTokens": 21789,
      "webSearchRequests": 0,
      "costUSD": 0.21866375,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8202f240-f8c7-4dbe-9f26-abb87a71dfd1"
}
```

</details>

---
