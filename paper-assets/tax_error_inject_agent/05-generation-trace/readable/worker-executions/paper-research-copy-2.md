# paper research

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_paper_research_20260515T033017.log`
- **Structured JSON:** [`5cfa815c998e99fa7f58.json`](../../sessions/5c/5cfa815c998e99fa7f58.json)

## Before a recorded user message

31 recorded events

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
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
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
  "uuid": "324e309c-ec46-40ba-a349-fdbb13bfd983",
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
  "uuid": "667bb67f-2f44-4e9a-aedc-0a7fa86f0595",
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to search for 4 papers, verify their metadata, and append them to a literature_map.yaml file. Let me start by reading the existing file and searching for the papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "2ab821f4-9c50-425e-8bcc-d94f930710c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMzX2JACqYhwS1eRjGeks7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12215,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12215
      },
      "output_tokens": 31,
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

先读取现有 literature_map.yaml，同时搜索 4 篇论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "c017f514-4360-47f6-b9de-e6fd92ada106",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMzX2JACqYhwS1eRjGeks7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12215,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12215
      },
      "output_tokens": 31,
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

<details open><summary>🔧 Tool call — Read · `toolu_014wV25x6PLQwehqMDgsBm5h`</summary>

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
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "af2e0874-6f52-4598-a71d-4b54bf82d03e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMzX2JACqYhwS1eRjGeks7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12215,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12215
      },
      "output_tokens": 31,
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

_source line 7 · 2026-05-15T03:30:31.983Z_

<details><summary>↩ Tool result · `toolu_014wV25x6PLQwehqMDgsBm5h`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "5a00ea49-82d9-4153-93b1-fefcefe83def",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
      "content": "# Literature Map: Dose-Response / Threshold Effects in Data Augmentation\n# Updated: 2026-05-15\n\nentries:\n  # === Category: dose-response / threshold ===\n\n  - id: rolnick2017robust\n    title: \"Deep Learning is Robust to Massive Label Noise\"\n    authors: \"Rolnick, Veit, Belongie, Shavit\"\n    year: 2017\n    venue: arXiv 1705.10694\n    category: dose-response\n    role: background\n    key_finding: \"DNNs maintain >90% accuracy on MNIST even when correct labels are diluted 100:1, as long as correct label remains most likely by a small margin.\"\n    relevance: \"Contrasts with our finding: image classification is robust to extreme noise, while embodied planning shows sharp degradation at 25%. Task complexity mediates noise tolerance.\"\n\n  - id: yuan2024early_stopping\n    title: \"Early Stopping Against Label Noise Without Validation Data\"\n    authors: \"Yuan, Feng, Liu\"\n    year: 2024\n    venue: ICLR 2024\n    category: dose-response\n    role: background\n    key_finding: \"Identifies phase transition where DNNs shift from fitting clean to fitting mislabeled examples. Proposes Label Wave to detect this transition during training.\"\n    relevance: \"Supports existence of phase transition in learning dynamics. Our 10-25% threshold may correspond to such a transition point in the SFT regime.\"\n\n  - id: dohmatob2025collapse\n    title: \"Strong Model Collapse\"\n    authors: \"Dohmatob, Feng, Subramonian, Kempe\"\n    year: 2025\n    venue: ICLR 2025\n    category: threshold\n    role: background\n    key_finding: \"Even 0.1% synthetic data can cause model collapse in supervised regression. Past interpolation threshold, larger models become more robust (double-descent).\"\n    relevance: \"Demonstrates extreme sensitivity to data quality in certain regimes. Our 10-25% threshold is analogous—small quality shifts cause nonlinear degradation.\"\n\n  - id: beyond_clean_data2024\n    title: \"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance\"\n    authors: \"Various\"\n    year: 2024\n    venue: ScienceDirect\n    category: dose-response\n    role: background\n    key_finding: \"Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds.\"\n    relevance: \"Methodologically similar—varies noise proportion to find degradation curves. Shows task-specific threshold behavior.\"\n\n  # === Category: error-injection / failure augmentation ===\n\n  - id: wang2024learning_from_failure\n    title: \"Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents\"\n    authors: \"Wang, Li, Han, Zhang, Baldwin\"\n    year: 2024\n    venue: arXiv 2402.11651\n    category: error-injection\n    role: evaluation\n    key_finding: \"Failed trajectories provide valuable signal for LLM agents via contrastive learning. Negative examples improve math, QA, strategic tasks when properly structured.\"\n    relevance: \"Directly related—injects negative trajectories into agent SFT. Key difference: they use contrastive framing, not raw mixing. Our work shows raw mixing has narrow safe window.\"\n\n  - id: song2024eto\n    title: \"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents\"\n    authors: \"Song, Yin, Yue, Huang, Li, Lin\"\n    year: 2024\n    venue: ACL 2024\n    category: error-injection\n    role: evaluation\n    key_finding: \"Iteratively collects failure trajectories, uses DPO-style contrastive learning on success-failure pairs. +8% WebShop, +9.5% ScienceWorld vs SFT.\"\n    relevance: \"Uses failure trajectories via preference optimization (DPO), not direct SFT mixing. Avoids our threshold problem by never training directly on failures.\"\n\n  - id: paladin2025\n    title: \"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases\"\n    authors: \"Vuddanti, Shah et al.\"\n    year: 2025\n    venue: arXiv 2509.25238\n    category: error-injection\n    role: evaluation\n    key_finding: \"Trains on 50K+ recovery-annotated failure trajectories via LoRA. +57pp recovery rate vs vanilla (32.76%→89.68%), +13.6pp vs CRITIC baseline. Taxonomy of 7 error classes. Includes inference-time retrieval.\"\n    relevance: \"Most similar to our approach (taxonomy-guided error injection). Key difference: they pair failures with recovery demos; we inject standalone error trajectories.\"\n\n  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Various\"\n    year: 2025\n    venue: arXiv 2603.21357\n    category: error-injection\n    role: evaluation\n    key_finding: \"Converts failed trajectories to valid training data by relabeling—failure for task A becomes success for task B.\"\n    relevance: \"Avoids noise problem by redefining failure as success for different goals. Contrasts with our direct injection approach.\"\n\n  # === Category: data-mixing ===\n\n  - id: dong2024composition\n    title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n    authors: \"Dong, Yuan et al.\"\n    year: 2024\n    venue: ACL 2024\n    category: data-mixing\n    role: background\n    key_finding: \"Data amount per domain matters more than ratio. Low-data mixing enables cross-domain transfer; high-data mixing causes ability conflicts.\"\n    relevance: \"Documents ability-conflict at high data amounts—analogous to our threshold. Ratio secondary to amount suggests our threshold may be absolute-count driven.\"\n\n  - id: ye2025mixing_laws\n    title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n    authors: \"Ye et al.\"\n    year: 2025\n    venue: ICLR 2025\n    category: data-mixing\n    role: background\n    key_finding: \"Discovers quantitative scaling laws L=f(r) for mixture proportions. Accurately predicts critical proportion avoiding catastrophic forgetting.\"\n    relevance: \"Their 'critical proportion for catastrophic forgetting' is conceptually identical to our threshold—both mark a phase transition in mixing.\"\n\n  - id: li2025mixing_optimization\n    title: \"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICML 2025\n    category: data-mixing\n    role: background\n    key_finding: \"SFT mixing as optimization with scaling-law parameterization. Optimal weights depend on model size and data scale.\"\n    relevance: \"Optimal mixing is model-size dependent—our 7B model may have different threshold than larger models. Finding is scale-specific.\"\n\n  - id: seddik2024synthetic_bound\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Seddik et al.\"\n    year: 2024\n    venue: arXiv 2404.05090\n    category: data-mixing\n    role: background\n    key_finding: \"Theoretical upper bounds on low-quality data proportion before collapse. Real data proportion must remain high.\"\n    relevance: \"Theoretical grounding for hard thresholds in quality mixing. Our empirical 10-25% window is consistent with their predictions.\"\n\n  # === Category: curriculum / quality threshold ===\n\n  - id: curriculum_robust2021\n    title: \"Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction\"\n    authors: \"Zhou, Wang, Bilmes\"\n    year: 2021\n    venue: ICLR 2021\n    category: curriculum\n    role: background\n    key_finding: \"Networks learn simple patterns first, then overfit noisy labels. Loss-based curriculum selection is unstable; errors accumulate multiplicatively.\"\n    relevance: \"Explains WHY threshold exists: once noisy proportion exceeds implicit curriculum capacity, errors accumulate. Our 25% may exceed model's capacity.\"\n\n  - id: agentprm2025\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    year: 2025\n    venue: arXiv 2502.10325\n    category: curriculum\n    role: evaluation\n    key_finding: \"Best-of-N with process reward model achieves 91.0% on ALFWorld (N=16, base policy 88.1%). Shows reward-guided search outperforms SFT alone.\"\n    relevance: \"ALFWorld SOTA reference. Our 65.3% SFT-only baseline is reasonable given AgentPRM uses test-time search.\"\n\n  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Various\"\n    year: 2024\n    venue: NeurIPS 2024\n    category: curriculum\n    role: evaluation\n    key_finding: \"World knowledge models reduce hallucinatory actions in ALFWorld. SFT on expert trajectories prone to overfitting.\"\n    relevance: \"ALFWorld baseline showing SFT quality sensitivity. Hallucination increase from poor training data parallels our error-injection degradation.\"\n\n  # === Category: training-dynamics / memorization ===\n\n  - id: arpit2017memorization\n    title: \"A Closer Look at Memorization in Deep Networks\"\n    authors: \"Arpit, Jastrzębski, Ballas, Krueger, Bengio, Kanwal, Maharaj, Fischer, Courville, Bengio, Lacoste-Julien\"\n    year: 2017\n    venue: ICML 2017\n    category: training-dynamics\n    role: background\n    key_finding: \"DNNs first learn clean patterns (early learning phase), then memorize noise. Training loss/accuracy improve on noisy data but generalization degrades. Dataset-independent capacity concepts are insufficient.\"\n    relevance: \"Directly explains our '50% injection → lowest train loss but worst eval' paradox. Higher injection = more noisy samples to memorize, better train metrics but worse generalization.\"\n\n  - id: liu2020early_learning_reg\n    title: \"Early-Learning Regularization Prevents Memorization of Noisy Labels\"\n    authors: \"Liu, Niles-Weed, Razavian, Fernandez-Granda\"\n    year: 2020\n    venue: NeurIPS 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Formalizes early learning phenomenon: models predict true labels for mislabeled examples early in training, then memorize wrong labels. ELR regularization exploits this window.\"\n    relevance: \"Our error-injected samples may be correctly handled early in training but memorized later, degrading clean-data generalization. Explains why more epochs could worsen the gap.\"\n\n  - id: zhou2023lima\n    title: \"LIMA: Less Is More for Alignment\"\n    authors: \"Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy\"\n    year: 2023\n    venue: NeurIPS 2023\n    category: training-dynamics\n    role: background\n    key_finding: \"Superficial Alignment Hypothesis: LLM knowledge/capability comes from pretraining; SFT only teaches output style/format. Limited SFT data suffices.\"\n    relevance: \"Explains why lower SFT loss ≠ better downstream capability. Error injection improves surface-level fitting (lower loss) but doesn't enhance—and may damage—pretrained planning capability.\"\n\n  - id: luo2023catastrophic_forgetting\n    title: \"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning\"\n    authors: \"Luo, Yang, Meng, Li, Zhou, Zhang\"\n    year: 2023\n    venue: arXiv 2308.08747\n    category: training-dynamics\n    role: background\n    key_finding: \"SFT is off-policy learning prone to overfit training distribution and forget pretraining knowledge. Forgetting severity increases with divergence between fine-tuning and pretraining distributions.\"\n    relevance: \"Error injection increases distributional gap from pretraining data, accelerating catastrophic forgetting. 50% injection → maximal divergence → most forgetting of planning capability.\"\n\n  - id: longpre2020augmentation\n    title: \"How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?\"\n    authors: \"Longpre, Wang, DuBois\"\n    year: 2020\n    venue: Findings of EMNLP 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift.\"\n    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"\n\n  # === Category: training-instability ===\n\n  - id: mccoy2020seeds\n    title: \"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance\"\n    authors: \"McCoy, Min, Linzen\"\n    year: 2020\n    venue: \"BlackboxNLP Workshop at EMNLP 2020\"\n    category: training-instability\n    role: background\n    key_finding: \"Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization.\"\n    relevance: \"与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity\"\n\n  - id: mosbach2021stability\n    title: \"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines\"\n    authors: \"Mosbach, Andriushchenko, Klakow\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    category: training-instability\n    role: background\n    key_finding: \"BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。\"\n    relevance: \"fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training\"\n\n  - id: damour2022underspecification\n    title: \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"\n    authors: \"D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al.\"\n    year: 2022\n    venue: \"Journal of Machine Learning Research, Vol. 23, No. 226\"\n    category: training-instability\n    role: background\n    key_finding: \"ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。\"\n    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"\n",
      "numLines": 246,
      "startLine": 1,
      "totalLines": 246
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BVgf7PQZcW7MzAGk7yP7M2`</summary>

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
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "63a68d13-cc20-4428-b14f-04697dd70b36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMzX2JACqYhwS1eRjGeks7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12215,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12215
      },
      "output_tokens": 31,
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

_source line 9 · 2026-05-15T03:30:33.331Z_

<details><summary>↩ Tool result · `toolu_01BVgf7PQZcW7MzAGk7yP7M2`</summary>

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
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "9f08b893-cb58-442f-ac5b-0e306f96fc9c",
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

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the existing literature_map.yaml and the WebSearch tool. Now let me search for all 4 papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "aa918c97-44bc-40ce-83da-8c8caeea8106",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6vbEkHPvYN2yV8tKyYnaA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5258,
      "cache_read_input_tokens": 24056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5258
      },
      "output_tokens": 17,
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

搜索 4 篇论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "b1b254bc-5b70-4a53-9dc5-aaf380a8b2b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6vbEkHPvYN2yV8tKyYnaA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5258,
      "cache_read_input_tokens": 24056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5258
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ge4YxNfFTbLL3qRSeoThdS`</summary>

```json
{
  "query": "ALFWorld Shridhar 2021 \"ALFWorld\" ICLR embodied planning benchmark paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "6af5eb43-beaf-48ef-b8cc-c36ec21a9383",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6vbEkHPvYN2yV8tKyYnaA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5258,
      "cache_read_input_tokens": 24056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5258
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XrZDVPQcK2ckQRiz7GxHu4`</summary>

```json
{
  "query": "ReAct Yao 2023 \"Synergizing Reasoning and Acting in Language Models\" ICLR paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "c31c227b-6547-41a3-8847-f3226dbee637",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6vbEkHPvYN2yV8tKyYnaA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5258,
      "cache_read_input_tokens": 24056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5258
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_015rQQfvMzG96MDGZBnpVHPT`</summary>

```json
{
  "query": "Reflexion Shinn 2023 \"Language Agents with Verbal Reinforcement Learning\" NeurIPS paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "1623def8-6d91-4c20-9ced-2c17ad302535",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6vbEkHPvYN2yV8tKyYnaA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5258,
      "cache_read_input_tokens": 24056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5258
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GPDR1uQrFhL8nwiiRUSmYj`</summary>

```json
{
  "query": "CoEx ALFWorld 93.28 collaborative exploration SOTA paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "41fa0078-c217-4ddf-ae18-388fd6f689bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6vbEkHPvYN2yV8tKyYnaA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5258,
      "cache_read_input_tokens": 24056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5258
      },
      "output_tokens": 17,
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

_source line 16 · 2026-05-15T03:30:43.566Z_

<details><summary>↩ Tool result · `toolu_01Ge4YxNfFTbLL3qRSeoThdS`</summary>

```text
Web search results for query: "ALFWorld Shridhar 2021 "ALFWorld" ICLR embodied planning benchmark paper"

Links: [{"title":"GitHub - alfworld/alfworld: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning · GitHub","url":"https://github.com/alfworld/alfworld"},{"title":"ALFWorld","url":"https://alfworld.github.io/"},{"title":"[PDF] ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ALFWorld:-Aligning-Text-and-Embodied-Environments-Shridhar-Yuan/398a0625e8707a0b41ac58eaec51e8feb87dd7cb"},{"title":"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | OpenReview","url":"https://openreview.net/forum?id=0IOX0YcCdTn"},{"title":"[2010.03768] ALFWorld: Aligning Text and Embodied Environments for Interactive Learning","url":"https://arxiv.org/abs/2010.03768"},{"title":"Published as a conference paper at ICLR 2021","url":"https://openreview.net/pdf?id=0IOX0YcCdTn"},{"title":"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning","url":"https://papertalk.org/papertalks/28910"},{"title":"[PDF] ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ALFRED:-A-Benchmark-for-Interpreting-Grounded-for-Shridhar-Thomason/f4cf4246f3882aa6337e9c05d5675a3b8463a32e"},{"title":"[Paper Note] ALFWorld: Aligning Text and Embodied Environments for Interactive Learning, Mohit Shridhar+, ICLR'21, 2020.10 · Issue #3452 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/3452"},{"title":"ICLR Poster ALFWorld: Aligning Text and Embodied Environments for Interactive Learning","url":"https://iclr.cc/virtual/2021/poster/2973"}]

I found information about the ALFWorld paper! Here are the key details:

**Paper Citation:**
ALFWorld: Aligning Text and Embodied Environments for Interactive Learning by Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté, Yonatan Bisk, Adam Trischler, and Matthew Hausknecht, published in the Proceedings of the International Conference on Learning Representations (ICLR) in 2021.

**Paper Details:**
- ArXiv URL: https://arxiv.org/abs/2010.03768
- OpenReview: https://openreview.net/forum?id=0IOX0YcCdTn

**Key Contribution:**
ALFWorld is a simulator that enables agents to learn abstract, text-based policies in TextWorld and then execute goals from the ALFRED benchmark in a rich visual environment. ALFWorld enables the creation of a new BUTLER agent whose abstract knowledge, learned in TextWorld, corresponds directly to concrete, visually grounded actions.

**Purpose:**
Embodied agents require the same abilities as humans do for reasoning abstractly and executing concretely, but existing work does not yet provide the infrastructure necessary for both reasoning abstractly and executing concretely, which is what ALFWorld addresses.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "94075937-06ca-4885-a6d5-1cce38ecabd3",
  "tool_use_result": {
    "query": "ALFWorld Shridhar 2021 \"ALFWorld\" ICLR embodied planning benchmark paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q4D2SUBBRcgVbw3H6bnojP",
        "content": [
          {
            "title": "GitHub - alfworld/alfworld: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning · GitHub",
            "url": "https://github.com/alfworld/alfworld"
          },
          {
            "title": "ALFWorld",
            "url": "https://alfworld.github.io/"
          },
          {
            "title": "[PDF] ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/ALFWorld:-Aligning-Text-and-Embodied-Environments-Shridhar-Yuan/398a0625e8707a0b41ac58eaec51e8feb87dd7cb"
          },
          {
            "title": "ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | OpenReview",
            "url": "https://openreview.net/forum?id=0IOX0YcCdTn"
          },
          {
            "title": "[2010.03768] ALFWorld: Aligning Text and Embodied Environments for Interactive Learning",
            "url": "https://arxiv.org/abs/2010.03768"
          },
          {
            "title": "Published as a conference paper at ICLR 2021",
            "url": "https://openreview.net/pdf?id=0IOX0YcCdTn"
          },
          {
            "title": "ALFWorld: Aligning Text and Embodied Environments for Interactive Learning",
            "url": "https://papertalk.org/papertalks/28910"
          },
          {
            "title": "[PDF] ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/ALFRED:-A-Benchmark-for-Interpreting-Grounded-for-Shridhar-Thomason/f4cf4246f3882aa6337e9c05d5675a3b8463a32e"
          },
          {
            "title": "[Paper Note] ALFWorld: Aligning Text and Embodied Environments for Interactive Learning, Mohit Shridhar+, ICLR'21, 2020.10 · Issue #3452 · AkihikoWatanabe/paper_notes",
            "url": "https://github.com/AkihikoWatanabe/paper_notes/issues/3452"
          },
          {
            "title": "ICLR Poster ALFWorld: Aligning Text and Embodied Environments for Interactive Learning",
            "url": "https://iclr.cc/virtual/2021/poster/2973"
          }
        ]
      },
      "I found information about the ALFWorld paper! Here are the key details:\n\n**Paper Citation:**\nALFWorld: Aligning Text and Embodied Environments for Interactive Learning by Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté, Yonatan Bisk, Adam Trischler, and Matthew Hausknecht, published in the Proceedings of the International Conference on Learning Representations (ICLR) in 2021.\n\n**Paper Details:**\n- ArXiv URL: https://arxiv.org/abs/2010.03768\n- OpenReview: https://openreview.net/forum?id=0IOX0YcCdTn\n\n**Key Contribution:**\nALFWorld is a simulator that enables agents to learn abstract, text-based policies in TextWorld and then execute goals from the ALFRED benchmark in a rich visual environment. ALFWorld enables the creation of a new BUTLER agent whose abstract knowledge, learned in TextWorld, corresponds directly to concrete, visually grounded actions.\n\n**Purpose:**\nEmbodied agents require the same abilities as humans do for reasoning abstractly and executing concretely, but existing work does not yet provide the infrastructure necessary for both reasoning abstractly and executing concretely, which is what ALFWorld addresses."
    ],
    "durationSeconds": 5.083090610000001
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T03:30:45.316Z_

<details><summary>↩ Tool result · `toolu_01XrZDVPQcK2ckQRiz7GxHu4`</summary>

```text
Web search results for query: "ReAct Yao 2023 "Synergizing Reasoning and Acting in Language Models" ICLR paper"

Links: [{"title":"[2210.03629] ReAct: Synergizing Reasoning and Acting in Language Models","url":"https://arxiv.org/abs/2210.03629"},{"title":"GitHub - ysymyth/ReAct: [ICLR 2023] ReAct: Synergizing Reasoning and Acting in Language Models · GitHub","url":"https://github.com/ysymyth/ReAct"},{"title":"ReAct: Synergizing Reasoning and Acting in Language ...","url":"https://arxiv.org/pdf/2210.03629"},{"title":"REACT: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS - Princeton University","url":"https://collaborate.princeton.edu/en/publications/react-synergizing-reasoning-and-acting-in-language-models/"},{"title":"Synergizing reasoning and acting in language models","url":"https://openreview.net/pdf?id=WE_vluYUL-X"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models | OpenReview","url":"https://openreview.net/forum?id=WE_vluYUL-X"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models","url":"https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/"},{"title":"[PDF] ReAct: Synergizing Reasoning and Acting in Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ReAct:-Synergizing-Reasoning-and-Acting-in-Language-Yao-Zhao/99832586d55f540f603637e458a292406a0ed75d"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10451467-react-synergizing-reasoning-acting-language-models"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models","url":"https://react-lm.github.io/"}]

I found the paper you're looking for. Here are the key details:

**Paper Information:**

The paper "ReAct: Synergizing Reasoning and Acting in Language Models" was authored by Yao, Shunyu; Zhao, Jeffrey; Yu, Dian; Du, Nan; Shafran, Izhak; Narasimhan, Karthik; and Cao, Yuan, and was published at the International Conference on Learning Representations (ICLR) in 2023.

**Paper Abstract:**

While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. The paper explores the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments.

**Key Results:**

On question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces.

**Available Resources:**

- The paper can be found on arXiv at arxiv.org/abs/2210.03629
- Code is available on GitHub for the ICLR 2023 paper ReAct
- A project page with additional resources is available at react-lm.github.io


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "e085f7fe-617c-4e7d-826d-db20f0f02bf9",
  "tool_use_result": {
    "query": "ReAct Yao 2023 \"Synergizing Reasoning and Acting in Language Models\" ICLR paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VRyfVgVo48PBKBenRSqK4k",
        "content": [
          {
            "title": "[2210.03629] ReAct: Synergizing Reasoning and Acting in Language Models",
            "url": "https://arxiv.org/abs/2210.03629"
          },
          {
            "title": "GitHub - ysymyth/ReAct: [ICLR 2023] ReAct: Synergizing Reasoning and Acting in Language Models · GitHub",
            "url": "https://github.com/ysymyth/ReAct"
          },
          {
            "title": "ReAct: Synergizing Reasoning and Acting in Language ...",
            "url": "https://arxiv.org/pdf/2210.03629"
          },
          {
            "title": "REACT: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS - Princeton University",
            "url": "https://collaborate.princeton.edu/en/publications/react-synergizing-reasoning-and-acting-in-language-models/"
          },
          {
            "title": "Synergizing reasoning and acting in language models",
            "url": "https://openreview.net/pdf?id=WE_vluYUL-X"
          },
          {
            "title": "ReAct: Synergizing Reasoning and Acting in Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=WE_vluYUL-X"
          },
          {
            "title": "ReAct: Synergizing Reasoning and Acting in Language Models",
            "url": "https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/"
          },
          {
            "title": "[PDF] ReAct: Synergizing Reasoning and Acting in Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/ReAct:-Synergizing-Reasoning-and-Acting-in-Language-Yao-Zhao/99832586d55f540f603637e458a292406a0ed75d"
          },
          {
            "title": "ReAct: Synergizing Reasoning and Acting in Language Models | NSF Public Access Repository",
            "url": "https://par.nsf.gov/biblio/10451467-react-synergizing-reasoning-acting-language-models"
          },
          {
            "title": "ReAct: Synergizing Reasoning and Acting in Language Models",
            "url": "https://react-lm.github.io/"
          }
        ]
      },
      "I found the paper you're looking for. Here are the key details:\n\n**Paper Information:**\n\nThe paper \"ReAct: Synergizing Reasoning and Acting in Language Models\" was authored by Yao, Shunyu; Zhao, Jeffrey; Yu, Dian; Du, Nan; Shafran, Izhak; Narasimhan, Karthik; and Cao, Yuan, and was published at the International Conference on Learning Representations (ICLR) in 2023.\n\n**Paper Abstract:**\n\nWhile large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. The paper explores the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments.\n\n**Key Results:**\n\nOn question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces.\n\n**Available Resources:**\n\n- The paper can be found on arXiv at arxiv.org/abs/2210.03629\n- Code is available on GitHub for the ICLR 2023 paper ReAct\n- A project page with additional resources is available at react-lm.github.io"
    ],
    "durationSeconds": 6.060597267000001
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T03:30:47.381Z_

<details><summary>↩ Tool result · `toolu_01GPDR1uQrFhL8nwiiRUSmYj`</summary>

```text
Web search results for query: "CoEx ALFWorld 93.28 collaborative exploration SOTA paper"

Links: [{"title":"CoEx – Co-evolving World-model and Exploration Minsoo Kim","url":"https://arxiv.org/pdf/2507.22281"},{"title":"[2507.22281] CoEx -- Co-evolving World-model and Exploration","url":"https://arxiv.org/abs/2507.22281"},{"title":"CoEx – Co-evolving World-model and Exploration - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.1179/"},{"title":"Results on the six tasks of the ALFWorld benchmark, using success rate... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Results-on-the-six-tasks-of-the-ALFWorld-benchmark-using-success-rate-as-evaluation_tbl1_394121762"},{"title":"ALFWorld","url":"https://alfworld.github.io/"},{"title":"AI2-THOR Publications","url":"https://ai2thor.allenai.org/publications/"},{"title":"Collaborative Research and Scholarly Experiences | The College | Brown University","url":"https://college.brown.edu/design-your-education/explore-open-curriculum/course-selection/curricular-programs/coex"},{"title":"[2311.16714] Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld","url":"https://arxiv.org/abs/2311.16714"},{"title":"GitHub - alfworld/alfworld: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning · GitHub","url":"https://github.com/alfworld/alfworld"},{"title":"coex","url":"https://coexcollaborative.com/"}]

Based on the search results, I found relevant information about CoEx and its performance on ALFWorld with the 93.28% score:

CoEx demonstrates strong performance across all task types, achieving the highest total success rate of 93.28%, over state-of-the-art baselines.

CoEx is a hierarchical agent architecture in which hierarchical state abstraction allows LLM planning to co-evolve with a dynamically updated model of the world. It plans and interacts with the world by using LLM reasoning to orchestrate dynamic plans consisting of subgoals, and its learning mechanism continuously incorporates these subgoal experiences into a persistent world model in the form of a neurosymbolic belief state, comprising textual inferences and code-based symbolic memory.

ALFWorld tasks require a mixture of planning and exploration, as the tasks require locating objects whose locations are at first unknown, then carrying out further tasks involving them. Through its co-evolution of planning and world model adaptation, CoEx achieves superior performance compared to less dynamic methods for world model adaptation.

The paper was published on arXiv on July 29, 2025, by Minsoo Kim and co-authors, and evaluates the CoEx agent across diverse scenarios including ALFWorld, PDDL, and Jericho environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "46fe5db7-ca89-42b2-8a00-9fac99b50b12",
  "tool_use_result": {
    "query": "CoEx ALFWorld 93.28 collaborative exploration SOTA paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_012YNcnKazMnj3Z1jtRCM5Hz",
        "content": [
          {
            "title": "CoEx – Co-evolving World-model and Exploration Minsoo Kim",
            "url": "https://arxiv.org/pdf/2507.22281"
          },
          {
            "title": "[2507.22281] CoEx -- Co-evolving World-model and Exploration",
            "url": "https://arxiv.org/abs/2507.22281"
          },
          {
            "title": "CoEx – Co-evolving World-model and Exploration - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-emnlp.1179/"
          },
          {
            "title": "Results on the six tasks of the ALFWorld benchmark, using success rate... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Results-on-the-six-tasks-of-the-ALFWorld-benchmark-using-success-rate-as-evaluation_tbl1_394121762"
          },
          {
            "title": "ALFWorld",
            "url": "https://alfworld.github.io/"
          },
          {
            "title": "AI2-THOR Publications",
            "url": "https://ai2thor.allenai.org/publications/"
          },
          {
            "title": "Collaborative Research and Scholarly Experiences | The College | Brown University",
            "url": "https://college.brown.edu/design-your-education/explore-open-curriculum/course-selection/curricular-programs/coex"
          },
          {
            "title": "[2311.16714] Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld",
            "url": "https://arxiv.org/abs/2311.16714"
          },
          {
            "title": "GitHub - alfworld/alfworld: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning · GitHub",
            "url": "https://github.com/alfworld/alfworld"
          },
          {
            "title": "coex",
            "url": "https://coexcollaborative.com/"
          }
        ]
      },
      "Based on the search results, I found relevant information about CoEx and its performance on ALFWorld with the 93.28% score:\n\nCoEx demonstrates strong performance across all task types, achieving the highest total success rate of 93.28%, over state-of-the-art baselines.\n\nCoEx is a hierarchical agent architecture in which hierarchical state abstraction allows LLM planning to co-evolve with a dynamically updated model of the world. It plans and interacts with the world by using LLM reasoning to orchestrate dynamic plans consisting of subgoals, and its learning mechanism continuously incorporates these subgoal experiences into a persistent world model in the form of a neurosymbolic belief state, comprising textual inferences and code-based symbolic memory.\n\nALFWorld tasks require a mixture of planning and exploration, as the tasks require locating objects whose locations are at first unknown, then carrying out further tasks involving them. Through its co-evolution of planning and world model adaptation, CoEx achieves superior performance compared to less dynamic methods for world model adaptation.\n\nThe paper was published on arXiv on July 29, 2025, by Minsoo Kim and co-authors, and evaluates the CoEx agent across diverse scenarios including ALFWorld, PDDL, and Jericho environments."
    ],
    "durationSeconds": 7.068639605
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T03:30:47.658Z_

<details><summary>↩ Tool result · `toolu_015rQQfvMzG96MDGZBnpVHPT`</summary>

```text
Web search results for query: "Reflexion Shinn 2023 "Language Agents with Verbal Reinforcement Learning" NeurIPS paper"

Links: [{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub","url":"https://github.com/noahshinn/reflexion"},{"title":"[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366"},{"title":"NeurIPS Poster Reflexion: language agents with verbal reinforcement learning","url":"https://neurips.cc/virtual/2023/poster/70114"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf"},{"title":"Reflexion: language agents with verbal reinforcement learning | OpenReview","url":"https://openreview.net/forum?id=vAElhFcKW6"},{"title":"Reflexion: language agents with verbal reinforcement learning","url":"https://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://openreview.net/pdf?id=vAElhFcKW6"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning - Princeton University","url":"https://collaborate.princeton.edu/en/publications/reflexion-language-agents-with-verbal-reinforcement-learning-2/"},{"title":"[PDF] Reflexion: language agents with verbal reinforcement learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Reflexion:-language-agents-with-verbal-learning-Shinn-Cassano/0671fd553dd670a4e820553a974bc48040ba0819"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://github.com/noahshinn/reflexion/tree/main"}]

I found the paper you're looking for. Here are the search results for the Reflexion paper by Shinn et al. (2023):

## Paper Overview

This is the code, demos, and log files for "Reflexion: Language Agents with Verbal Reinforcement Learning" by Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao.

## Key Contribution

The paper proposes Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials.

## Motivation

Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning.

## Publication

The paper was published at the 37th Conference on Neural Information Processing Systems (NeurIPS 2023).

## Available Resources

- **arXiv**: Available at https://arxiv.org/abs/2303.11366 (arXiv:2303.11366)
- **GitHub Repository**: https://github.com/noahshinn/reflexion
- **NeurIPS Poster**: https://neurips.cc/virtual/2023/poster/70114
- **OpenReview**: https://openreview.net/forum?id=vAElhFcKW6
- **Official Paper PDF**: https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "a0d34639-74f1-4192-8ada-ffa1810368b8",
  "tool_use_result": {
    "query": "Reflexion Shinn 2023 \"Language Agents with Verbal Reinforcement Learning\" NeurIPS paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BGp4soycbDMJsZYGgwSpXk",
        "content": [
          {
            "title": "GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub",
            "url": "https://github.com/noahshinn/reflexion"
          },
          {
            "title": "[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://arxiv.org/abs/2303.11366"
          },
          {
            "title": "NeurIPS Poster Reflexion: language agents with verbal reinforcement learning",
            "url": "https://neurips.cc/virtual/2023/poster/70114"
          },
          {
            "title": "Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf"
          },
          {
            "title": "Reflexion: language agents with verbal reinforcement learning | OpenReview",
            "url": "https://openreview.net/forum?id=vAElhFcKW6"
          },
          {
            "title": "Reflexion: language agents with verbal reinforcement learning",
            "url": "https://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html"
          },
          {
            "title": "Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn",
            "url": "https://openreview.net/pdf?id=vAElhFcKW6"
          },
          {
            "title": "Reflexion: Language Agents with Verbal Reinforcement Learning - Princeton University",
            "url": "https://collaborate.princeton.edu/en/publications/reflexion-language-agents-with-verbal-reinforcement-learning-2/"
          },
          {
            "title": "[PDF] Reflexion: language agents with verbal reinforcement learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Reflexion:-language-agents-with-verbal-learning-Shinn-Cassano/0671fd553dd670a4e820553a974bc48040ba0819"
          },
          {
            "title": "GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://github.com/noahshinn/reflexion/tree/main"
          }
        ]
      },
      "I found the paper you're looking for. Here are the search results for the Reflexion paper by Shinn et al. (2023):\n\n## Paper Overview\n\nThis is the code, demos, and log files for \"Reflexion: Language Agents with Verbal Reinforcement Learning\" by Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao.\n\n## Key Contribution\n\nThe paper proposes Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials.\n\n## Motivation\n\nLarge language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning.\n\n## Publication\n\nThe paper was published at the 37th Conference on Neural Information Processing Systems (NeurIPS 2023).\n\n## Available Resources\n\n- **arXiv**: Available at https://arxiv.org/abs/2303.11366 (arXiv:2303.11366)\n- **GitHub Repository**: https://github.com/noahshinn/reflexion\n- **NeurIPS Poster**: https://neurips.cc/virtual/2023/poster/70114\n- **OpenReview**: https://openreview.net/forum?id=vAElhFcKW6\n- **Official Paper PDF**: https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf"
    ],
    "durationSeconds": 7.713131592999998
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Good, I found all 4 papers. Let me now get more detailed metadata for each. I need to verify:
1. ALFWorld - authors are Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté, Yonatan Bisk, Adam Trischler, Matthew Hausknecht. ICLR 2021. arXiv 2010.03768.
2. ReAct - authors are Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao. 
3. Reflexion - authors are Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao. NeurIPS 2023. arXiv 2303.11366.
4. CoEx - "CoEx – Co-evolving World-model and Exploration" by Minsoo Kim et al. arXiv 2507.22281. Published at EMNLP 2025. I've got the complete publication details now - ReAct appeared at ICLR 2023 with arXiv 2210.03629.

Let me verify the CoEx author list and venue details through the ACL Anthology.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "1624e474-b585-4264-9d39-60076fadaa7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5LtskiHRkSjS8ZE4YCq1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 3331,
      "cache_read_input_tokens": 29314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3331
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

_source line 21_

找到了所有 4 篇。CoEx 需要确认作者和 venue 细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "9d1a1456-7d79-41ad-9abd-ac77b38b303b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5LtskiHRkSjS8ZE4YCq1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 3331,
      "cache_read_input_tokens": 29314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3331
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

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VnW4QB8ztQ3qr6YswPvjzd`</summary>

```json
{
  "query": "CoEx \"Co-evolving World-model and Exploration\" Minsoo Kim authors EMNLP 2025 findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "56b5e8e8-bc63-4b0e-b4b8-f6fd30df1ef5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5LtskiHRkSjS8ZE4YCq1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 3331,
      "cache_read_input_tokens": 29314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3331
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PzvfHQx2y2r2ntuhBFmEqC`</summary>

```json
{
  "query": "Reflexion ALFWorld success rate 97% multi-trial results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "103d2720-93bd-4ac2-a98d-e845248fb1cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5LtskiHRkSjS8ZE4YCq1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 3331,
      "cache_read_input_tokens": 29314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3331
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

_source line 24 · 2026-05-15T03:31:03.802Z_

<details><summary>↩ Tool result · `toolu_01PzvfHQx2y2r2ntuhBFmEqC`</summary>

```text
Web search results for query: "Reflexion ALFWorld success rate 97% multi-trial results"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2511.14584v1"},{"title":"GitHub - qpiai/reflexgrad","url":"https://github.com/qpiai/reflexgrad"},{"title":"2023 ReflexionAnAutonomousAgentwithD - GM-RKB","url":"http://www.gabormelli.com/RKB/2023_ReflexionAnAutonomousAgentwithD"},{"title":"(PDF) Reflexion: an autonomous agent with dynamic memory and self-reflection","url":"https://www.researchgate.net/publication/369414009_Reflexion_an_autonomous_agent_with_dynamic_memory_and_self-reflection"},{"title":"Reflexion: an autonomous agent with dynamic memory and self-reflection – Digital Habitats","url":"https://digitalhabitats.global/blogs/digital-thoughts/reflexion-an-autonomous-agent-with-dynamic-memory-and-self-reflection"},{"title":"Code Driven Planning with Domain-Adaptive Critic","url":"https://arxiv.org/html/2509.19077"},{"title":"Towards Autonomous Agents: Adaptive-planning, Reasoning, and Acting in Language Models","url":"https://arxiv.org/html/2408.06458"},{"title":"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection","url":"https://arxiv.org/html/2505.15182v2"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://arxiv.org/pdf/2303.11366"},{"title":"Reflexion: Agents in Action - Unalarming","url":"https://unalarming.com/reflexion-agents-in-action"}]

Based on the search results, I found the information you're looking for:

When combined with the ReAct problem-solving technique, self-reflection guides the Reflexion agent to achieve a 97% success discovery rate on the AlfWorld benchmark in just 12 autonomous trials. This represents the multi-trial results for the Reflexion system.

More specifically, the agent used ReAct to solve 97% of the given environments in 12 trials, failing to solve only 4 out of 134 tasks. 

It's important to note that this 97% success discovery rate on the AlfWorld benchmark outperforms the base ReAct agent with an accuracy of 75%, demonstrating the effectiveness of adding the Reflexion approach with self-reflection capabilities.

This 97% success rate represents a significant improvement in the agent's performance across multiple trials, showing how the Reflexion framework enables learning and adaptation through self-reflection over the course of several task attempts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "6bd566d3-a699-4cc2-bb72-435deed7fa03",
  "tool_use_result": {
    "query": "Reflexion ALFWorld success rate 97% multi-trial results",
    "results": [
      {
        "tool_use_id": "srvtoolu_019FJ7Y7uu35TEbjmq5FJVTP",
        "content": [
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2511.14584v1"
          },
          {
            "title": "GitHub - qpiai/reflexgrad",
            "url": "https://github.com/qpiai/reflexgrad"
          },
          {
            "title": "2023 ReflexionAnAutonomousAgentwithD - GM-RKB",
            "url": "http://www.gabormelli.com/RKB/2023_ReflexionAnAutonomousAgentwithD"
          },
          {
            "title": "(PDF) Reflexion: an autonomous agent with dynamic memory and self-reflection",
            "url": "https://www.researchgate.net/publication/369414009_Reflexion_an_autonomous_agent_with_dynamic_memory_and_self-reflection"
          },
          {
            "title": "Reflexion: an autonomous agent with dynamic memory and self-reflection – Digital Habitats",
            "url": "https://digitalhabitats.global/blogs/digital-thoughts/reflexion-an-autonomous-agent-with-dynamic-memory-and-self-reflection"
          },
          {
            "title": "Code Driven Planning with Domain-Adaptive Critic",
            "url": "https://arxiv.org/html/2509.19077"
          },
          {
            "title": "Towards Autonomous Agents: Adaptive-planning, Reasoning, and Acting in Language Models",
            "url": "https://arxiv.org/html/2408.06458"
          },
          {
            "title": "ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection",
            "url": "https://arxiv.org/html/2505.15182v2"
          },
          {
            "title": "Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn",
            "url": "https://arxiv.org/pdf/2303.11366"
          },
          {
            "title": "Reflexion: Agents in Action - Unalarming",
            "url": "https://unalarming.com/reflexion-agents-in-action"
          }
        ]
      },
      "Based on the search results, I found the information you're looking for:\n\nWhen combined with the ReAct problem-solving technique, self-reflection guides the Reflexion agent to achieve a 97% success discovery rate on the AlfWorld benchmark in just 12 autonomous trials. This represents the multi-trial results for the Reflexion system.\n\nMore specifically, the agent used ReAct to solve 97% of the given environments in 12 trials, failing to solve only 4 out of 134 tasks. \n\nIt's important to note that this 97% success discovery rate on the AlfWorld benchmark outperforms the base ReAct agent with an accuracy of 75%, demonstrating the effectiveness of adding the Reflexion approach with self-reflection capabilities.\n\nThis 97% success rate represents a significant improvement in the agent's performance across multiple trials, showing how the Reflexion framework enables learning and adaptation through self-reflection over the course of several task attempts."
    ],
    "durationSeconds": 5.730228507
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T03:31:04.399Z_

<details><summary>↩ Tool result · `toolu_01VnW4QB8ztQ3qr6YswPvjzd`</summary>

```text
Web search results for query: "CoEx "Co-evolving World-model and Exploration" Minsoo Kim authors EMNLP 2025 findings"

Links: [{"title":"CoEx – Co-evolving World-model and Exploration - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.1179/"},{"title":"[2507.22281] CoEx -- Co-evolving World-model and Exploration","url":"https://arxiv.org/abs/2507.22281"},{"title":"CoEx – Co-evolving World-model and Exploration Minsoo Kim","url":"https://arxiv.org/pdf/2507.22281"},{"title":"dblp: Minsoo Kim (disambiguation)","url":"https://dblp.org/pid/78/661.html"},{"title":"dblp: Seung-won Hwang","url":"https://dblp.uni-trier.de/pid/h/SeungwonHwang.html"},{"title":"CoEx – Co-evolving World-model and Exploration","url":"https://aclanthology.org/2025.findings-emnlp.1179.pdf"},{"title":"Awesome-World-Models/README.md at main · leofan90/Awesome-World-Models","url":"https://github.com/leofan90/Awesome-World-Models/blob/main/README.md"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"Beyond Task-Oriented and Chitchat Dialogues: Proactive and Transition-Aware Conversational Agents - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.672/"}]

Based on the search results, here is information about the CoEx paper from EMNLP 2025:

## Paper Overview

CoEx – Co-evolving World-model and Exploration was authored by Minsoo Kim and Seung-won Hwang and published in 2025 in the Findings of the Association for Computational Linguistics: EMNLP 2025 conference in Suzhou, China.

## Key Problem and Solution

The paper addresses how planning in modern LLM agents relies on the LLM as an internal world model acquired during pretraining. However, existing agent designs fail to effectively assimilate new observations into dynamic updates of the world model, and this reliance on the LLM's static internal world model is progressively prone to misalignment with the underlying true state of the world, leading to the generation of divergent and erroneous plans.

The authors introduce a hierarchical agent architecture, CoEx, in which hierarchical state abstraction allows LLM planning to co-evolve with a dynamically updated model of the world.

## Experimental Findings

The paper evaluates the agent across a diverse set of agent scenarios involving rich environments and complex tasks including ALFWorld, PDDL, and Jericho, and experiments show that CoEx outperforms existing agent paradigms in planning and exploration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "717d861b-f36b-4238-b040-bfea82a96f66",
  "tool_use_result": {
    "query": "CoEx \"Co-evolving World-model and Exploration\" Minsoo Kim authors EMNLP 2025 findings",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BTf93gKno3yTNFtDjuiBSH",
        "content": [
          {
            "title": "CoEx – Co-evolving World-model and Exploration - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-emnlp.1179/"
          },
          {
            "title": "[2507.22281] CoEx -- Co-evolving World-model and Exploration",
            "url": "https://arxiv.org/abs/2507.22281"
          },
          {
            "title": "CoEx – Co-evolving World-model and Exploration Minsoo Kim",
            "url": "https://arxiv.org/pdf/2507.22281"
          },
          {
            "title": "dblp: Minsoo Kim (disambiguation)",
            "url": "https://dblp.org/pid/78/661.html"
          },
          {
            "title": "dblp: Seung-won Hwang",
            "url": "https://dblp.uni-trier.de/pid/h/SeungwonHwang.html"
          },
          {
            "title": "CoEx – Co-evolving World-model and Exploration",
            "url": "https://aclanthology.org/2025.findings-emnlp.1179.pdf"
          },
          {
            "title": "Awesome-World-Models/README.md at main · leofan90/Awesome-World-Models",
            "url": "https://github.com/leofan90/Awesome-World-Models/blob/main/README.md"
          },
          {
            "title": "Accepted Main Conference Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/main_papers/"
          },
          {
            "title": "GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub",
            "url": "https://github.com/LMD0311/Awesome-World-Model"
          },
          {
            "title": "Beyond Task-Oriented and Chitchat Dialogues: Proactive and Transition-Aware Conversational Agents - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.672/"
          }
        ]
      },
      "Based on the search results, here is information about the CoEx paper from EMNLP 2025:\n\n## Paper Overview\n\nCoEx – Co-evolving World-model and Exploration was authored by Minsoo Kim and Seung-won Hwang and published in 2025 in the Findings of the Association for Computational Linguistics: EMNLP 2025 conference in Suzhou, China.\n\n## Key Problem and Solution\n\nThe paper addresses how planning in modern LLM agents relies on the LLM as an internal world model acquired during pretraining. However, existing agent designs fail to effectively assimilate new observations into dynamic updates of the world model, and this reliance on the LLM's static internal world model is progressively prone to misalignment with the underlying true state of the world, leading to the generation of divergent and erroneous plans.\n\nThe authors introduce a hierarchical agent architecture, CoEx, in which hierarchical state abstraction allows LLM planning to co-evolve with a dynamically updated model of the world.\n\n## Experimental Findings\n\nThe paper evaluates the agent across a diverse set of agent scenarios involving rich environments and complex tasks including ALFWorld, PDDL, and Jericho, and experiments show that CoEx outperforms existing agent paradigms in planning and exploration."
    ],
    "durationSeconds": 6.920225980000003
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the entries:

1. **ALFWorld**:
   - Title: "ALFWorld: Aligning Text and Embodied Environments for Interactive Learning"
   - Authors: Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht
   - Year: 2021
   - Venue: ICLR 2021
   - arXiv: 2010.03768

2. **ReAct**:
   - Title: "ReAct: Synergizing Reasoning and Acting in Language Models"
   - Authors: Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao
   - Year: 2023
   - Venue: ICLR 2023
   - arXiv: 2210.03629

3. **Reflexion**:
   - Title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
   - Authors: Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao
   - Year: 2023
   - Venue: NeurIPS 2023
   - arXiv: 2303.11366

4. **CoEx**:
   - Title: "CoEx – Co-evolving World-" (title appears to be cut off)
   - Authors: Kim, Hwang
   - Year: 2025
   - Venue: Findings of EMNLP 2025
   - arXiv: 2507.22281

Now I'm adding these entries to the literature_map.yaml file, appending after line 246.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "f13f973f-7ac2-4fd1-bc8d-655d50d7f51b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015v6a4kTL8VCrVY5SEwFmmJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 719,
      "cache_creation_input_tokens": 2225,
      "cache_read_input_tokens": 32645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2225
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

_source line 27_

所有 4 篇元数据已验证。追加到 literature_map.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "11fab326-7841-4375-b8a1-4a26a3e5cfc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015v6a4kTL8VCrVY5SEwFmmJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 719,
      "cache_creation_input_tokens": 2225,
      "cache_read_input_tokens": 32645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2225
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

<details open><summary>🔧 Tool call — Edit · `toolu_01WrYfT92WfukoNDe7JAFT7c`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
  "old_string": "    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"",
  "new_string": "    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"\n\n  # === Category: alfworld-methods ===\n\n  - id: shridhar2021alfworld\n    title: \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\"\n    authors: \"Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    arxiv: \"2010.03768\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Aligns TextWorld text-based environment with ALFRED embodied benchmark, enabling abstract policy learning that transfers to visual grounding.\"\n    relevance: \"我们的实验环境；134 tasks across 6 task types benchmark\"\n\n  - id: yao2023react\n    title: \"ReAct: Synergizing Reasoning and Acting in Language Models\"\n    authors: \"Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.03629\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Interleaved reasoning traces and actions enable LLMs to ground decisions, achieving 75% on ALFWorld (single-trial).\"\n    relevance: \"我们使用的 prompting paradigm（ReAct format）\"\n\n  - id: shinn2023reflexion\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2303.11366\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Verbal self-reflection in episodic memory achieves 97% on ALFWorld (12 trials, 130/134 tasks solved) without weight updates.\"\n    relevance: \"Inference-time reflection 成功 where training-time injection 失败——对比 key point\"\n\n  - id: kim2025coex\n    title: \"CoEx -- Co-evolving World-model and Exploration\"\n    authors: \"Kim, Hwang\"\n    year: 2025\n    venue: \"Findings of EMNLP 2025\"\n    arxiv: \"2507.22281\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Hierarchical state abstraction with dynamically updated neurosymbolic world model achieves 93.28% on ALFWorld.\"\n    relevance: \"ALFWorld SOTA 参考；co-evolving world model 对比我们的 static SFT 方法\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "ffdd7091-63a3-4823-bc47-308095d6db74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015v6a4kTL8VCrVY5SEwFmmJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 719,
      "cache_creation_input_tokens": 2225,
      "cache_read_input_tokens": 32645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2225
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

_source line 29 · 2026-05-15T03:31:28.447Z_

<details><summary>↩ Tool result · `toolu_01WrYfT92WfukoNDe7JAFT7c`</summary>

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
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "b47199a7-8d95-47e3-901d-a18258384b64",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
    "oldString": "    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"",
    "newString": "    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"\n\n  # === Category: alfworld-methods ===\n\n  - id: shridhar2021alfworld\n    title: \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\"\n    authors: \"Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    arxiv: \"2010.03768\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Aligns TextWorld text-based environment with ALFRED embodied benchmark, enabling abstract policy learning that transfers to visual grounding.\"\n    relevance: \"我们的实验环境；134 tasks across 6 task types benchmark\"\n\n  - id: yao2023react\n    title: \"ReAct: Synergizing Reasoning and Acting in Language Models\"\n    authors: \"Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.03629\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Interleaved reasoning traces and actions enable LLMs to ground decisions, achieving 75% on ALFWorld (single-trial).\"\n    relevance: \"我们使用的 prompting paradigm（ReAct format）\"\n\n  - id: shinn2023reflexion\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2303.11366\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Verbal self-reflection in episodic memory achieves 97% on ALFWorld (12 trials, 130/134 tasks solved) without weight updates.\"\n    relevance: \"Inference-time reflection 成功 where training-time injection 失败——对比 key point\"\n\n  - id: kim2025coex\n    title: \"CoEx -- Co-evolving World-model and Exploration\"\n    authors: \"Kim, Hwang\"\n    year: 2025\n    venue: \"Findings of EMNLP 2025\"\n    arxiv: \"2507.22281\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Hierarchical state abstraction with dynamically updated neurosymbolic world model achieves 93.28% on ALFWorld.\"\n    relevance: \"ALFWorld SOTA 参考；co-evolving world model 对比我们的 static SFT 方法\"",
    "originalFile": "# Literature Map: Dose-Response / Threshold Effects in Data Augmentation\n# Updated: 2026-05-15\n\nentries:\n  # === Category: dose-response / threshold ===\n\n  - id: rolnick2017robust\n    title: \"Deep Learning is Robust to Massive Label Noise\"\n    authors: \"Rolnick, Veit, Belongie, Shavit\"\n    year: 2017\n    venue: arXiv 1705.10694\n    category: dose-response\n    role: background\n    key_finding: \"DNNs maintain >90% accuracy on MNIST even when correct labels are diluted 100:1, as long as correct label remains most likely by a small margin.\"\n    relevance: \"Contrasts with our finding: image classification is robust to extreme noise, while embodied planning shows sharp degradation at 25%. Task complexity mediates noise tolerance.\"\n\n  - id: yuan2024early_stopping\n    title: \"Early Stopping Against Label Noise Without Validation Data\"\n    authors: \"Yuan, Feng, Liu\"\n    year: 2024\n    venue: ICLR 2024\n    category: dose-response\n    role: background\n    key_finding: \"Identifies phase transition where DNNs shift from fitting clean to fitting mislabeled examples. Proposes Label Wave to detect this transition during training.\"\n    relevance: \"Supports existence of phase transition in learning dynamics. Our 10-25% threshold may correspond to such a transition point in the SFT regime.\"\n\n  - id: dohmatob2025collapse\n    title: \"Strong Model Collapse\"\n    authors: \"Dohmatob, Feng, Subramonian, Kempe\"\n    year: 2025\n    venue: ICLR 2025\n    category: threshold\n    role: background\n    key_finding: \"Even 0.1% synthetic data can cause model collapse in supervised regression. Past interpolation threshold, larger models become more robust (double-descent).\"\n    relevance: \"Demonstrates extreme sensitivity to data quality in certain regimes. Our 10-25% threshold is analogous—small quality shifts cause nonlinear degradation.\"\n\n  - id: beyond_clean_data2024\n    title: \"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance\"\n    authors: \"Various\"\n    year: 2024\n    venue: ScienceDirect\n    category: dose-response\n    role: background\n    key_finding: \"Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds.\"\n    relevance: \"Methodologically similar—varies noise proportion to find degradation curves. Shows task-specific threshold behavior.\"\n\n  # === Category: error-injection / failure augmentation ===\n\n  - id: wang2024learning_from_failure\n    title: \"Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents\"\n    authors: \"Wang, Li, Han, Zhang, Baldwin\"\n    year: 2024\n    venue: arXiv 2402.11651\n    category: error-injection\n    role: evaluation\n    key_finding: \"Failed trajectories provide valuable signal for LLM agents via contrastive learning. Negative examples improve math, QA, strategic tasks when properly structured.\"\n    relevance: \"Directly related—injects negative trajectories into agent SFT. Key difference: they use contrastive framing, not raw mixing. Our work shows raw mixing has narrow safe window.\"\n\n  - id: song2024eto\n    title: \"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents\"\n    authors: \"Song, Yin, Yue, Huang, Li, Lin\"\n    year: 2024\n    venue: ACL 2024\n    category: error-injection\n    role: evaluation\n    key_finding: \"Iteratively collects failure trajectories, uses DPO-style contrastive learning on success-failure pairs. +8% WebShop, +9.5% ScienceWorld vs SFT.\"\n    relevance: \"Uses failure trajectories via preference optimization (DPO), not direct SFT mixing. Avoids our threshold problem by never training directly on failures.\"\n\n  - id: paladin2025\n    title: \"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases\"\n    authors: \"Vuddanti, Shah et al.\"\n    year: 2025\n    venue: arXiv 2509.25238\n    category: error-injection\n    role: evaluation\n    key_finding: \"Trains on 50K+ recovery-annotated failure trajectories via LoRA. +57pp recovery rate vs vanilla (32.76%→89.68%), +13.6pp vs CRITIC baseline. Taxonomy of 7 error classes. Includes inference-time retrieval.\"\n    relevance: \"Most similar to our approach (taxonomy-guided error injection). Key difference: they pair failures with recovery demos; we inject standalone error trajectories.\"\n\n  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Various\"\n    year: 2025\n    venue: arXiv 2603.21357\n    category: error-injection\n    role: evaluation\n    key_finding: \"Converts failed trajectories to valid training data by relabeling—failure for task A becomes success for task B.\"\n    relevance: \"Avoids noise problem by redefining failure as success for different goals. Contrasts with our direct injection approach.\"\n\n  # === Category: data-mixing ===\n\n  - id: dong2024composition\n    title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n    authors: \"Dong, Yuan et al.\"\n    year: 2024\n    venue: ACL 2024\n    category: data-mixing\n    role: background\n    key_finding: \"Data amount per domain matters more than ratio. Low-data mixing enables cross-domain transfer; high-data mixing causes ability conflicts.\"\n    relevance: \"Documents ability-conflict at high data amounts—analogous to our threshold. Ratio secondary to amount suggests our threshold may be absolute-count driven.\"\n\n  - id: ye2025mixing_laws\n    title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n    authors: \"Ye et al.\"\n    year: 2025\n    venue: ICLR 2025\n    category: data-mixing\n    role: background\n    key_finding: \"Discovers quantitative scaling laws L=f(r) for mixture proportions. Accurately predicts critical proportion avoiding catastrophic forgetting.\"\n    relevance: \"Their 'critical proportion for catastrophic forgetting' is conceptually identical to our threshold—both mark a phase transition in mixing.\"\n\n  - id: li2025mixing_optimization\n    title: \"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICML 2025\n    category: data-mixing\n    role: background\n    key_finding: \"SFT mixing as optimization with scaling-law parameterization. Optimal weights depend on model size and data scale.\"\n    relevance: \"Optimal mixing is model-size dependent—our 7B model may have different threshold than larger models. Finding is scale-specific.\"\n\n  - id: seddik2024synthetic_bound\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Seddik et al.\"\n    year: 2024\n    venue: arXiv 2404.05090\n    category: data-mixing\n    role: background\n    key_finding: \"Theoretical upper bounds on low-quality data proportion before collapse. Real data proportion must remain high.\"\n    relevance: \"Theoretical grounding for hard thresholds in quality mixing. Our empirical 10-25% window is consistent with their predictions.\"\n\n  # === Category: curriculum / quality threshold ===\n\n  - id: curriculum_robust2021\n    title: \"Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction\"\n    authors: \"Zhou, Wang, Bilmes\"\n    year: 2021\n    venue: ICLR 2021\n    category: curriculum\n    role: background\n    key_finding: \"Networks learn simple patterns first, then overfit noisy labels. Loss-based curriculum selection is unstable; errors accumulate multiplicatively.\"\n    relevance: \"Explains WHY threshold exists: once noisy proportion exceeds implicit curriculum capacity, errors accumulate. Our 25% may exceed model's capacity.\"\n\n  - id: agentprm2025\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    year: 2025\n    venue: arXiv 2502.10325\n    category: curriculum\n    role: evaluation\n    key_finding: \"Best-of-N with process reward model achieves 91.0% on ALFWorld (N=16, base policy 88.1%). Shows reward-guided search outperforms SFT alone.\"\n    relevance: \"ALFWorld SOTA reference. Our 65.3% SFT-only baseline is reasonable given AgentPRM uses test-time search.\"\n\n  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Various\"\n    year: 2024\n    venue: NeurIPS 2024\n    category: curriculum\n    role: evaluation\n    key_finding: \"World knowledge models reduce hallucinatory actions in ALFWorld. SFT on expert trajectories prone to overfitting.\"\n    relevance: \"ALFWorld baseline showing SFT quality sensitivity. Hallucination increase from poor training data parallels our error-injection degradation.\"\n\n  # === Category: training-dynamics / memorization ===\n\n  - id: arpit2017memorization\n    title: \"A Closer Look at Memorization in Deep Networks\"\n    authors: \"Arpit, Jastrzębski, Ballas, Krueger, Bengio, Kanwal, Maharaj, Fischer, Courville, Bengio, Lacoste-Julien\"\n    year: 2017\n    venue: ICML 2017\n    category: training-dynamics\n    role: background\n    key_finding: \"DNNs first learn clean patterns (early learning phase), then memorize noise. Training loss/accuracy improve on noisy data but generalization degrades. Dataset-independent capacity concepts are insufficient.\"\n    relevance: \"Directly explains our '50% injection → lowest train loss but worst eval' paradox. Higher injection = more noisy samples to memorize, better train metrics but worse generalization.\"\n\n  - id: liu2020early_learning_reg\n    title: \"Early-Learning Regularization Prevents Memorization of Noisy Labels\"\n    authors: \"Liu, Niles-Weed, Razavian, Fernandez-Granda\"\n    year: 2020\n    venue: NeurIPS 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Formalizes early learning phenomenon: models predict true labels for mislabeled examples early in training, then memorize wrong labels. ELR regularization exploits this window.\"\n    relevance: \"Our error-injected samples may be correctly handled early in training but memorized later, degrading clean-data generalization. Explains why more epochs could worsen the gap.\"\n\n  - id: zhou2023lima\n    title: \"LIMA: Less Is More for Alignment\"\n    authors: \"Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy\"\n    year: 2023\n    venue: NeurIPS 2023\n    category: training-dynamics\n    role: background\n    key_finding: \"Superficial Alignment Hypothesis: LLM knowledge/capability comes from pretraining; SFT only teaches output style/format. Limited SFT data suffices.\"\n    relevance: \"Explains why lower SFT loss ≠ better downstream capability. Error injection improves surface-level fitting (lower loss) but doesn't enhance—and may damage—pretrained planning capability.\"\n\n  - id: luo2023catastrophic_forgetting\n    title: \"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning\"\n    authors: \"Luo, Yang, Meng, Li, Zhou, Zhang\"\n    year: 2023\n    venue: arXiv 2308.08747\n    category: training-dynamics\n    role: background\n    key_finding: \"SFT is off-policy learning prone to overfit training distribution and forget pretraining knowledge. Forgetting severity increases with divergence between fine-tuning and pretraining distributions.\"\n    relevance: \"Error injection increases distributional gap from pretraining data, accelerating catastrophic forgetting. 50% injection → maximal divergence → most forgetting of planning capability.\"\n\n  - id: longpre2020augmentation\n    title: \"How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?\"\n    authors: \"Longpre, Wang, DuBois\"\n    year: 2020\n    venue: Findings of EMNLP 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift.\"\n    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"\n\n  # === Category: training-instability ===\n\n  - id: mccoy2020seeds\n    title: \"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance\"\n    authors: \"McCoy, Min, Linzen\"\n    year: 2020\n    venue: \"BlackboxNLP Workshop at EMNLP 2020\"\n    category: training-instability\n    role: background\n    key_finding: \"Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization.\"\n    relevance: \"与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity\"\n\n  - id: mosbach2021stability\n    title: \"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines\"\n    authors: \"Mosbach, Andriushchenko, Klakow\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    category: training-instability\n    role: background\n    key_finding: \"BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。\"\n    relevance: \"fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training\"\n\n  - id: damour2022underspecification\n    title: \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"\n    authors: \"D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al.\"\n    year: 2022\n    venue: \"Journal of Machine Learning Research, Vol. 23, No. 226\"\n    category: training-instability\n    role: background\n    key_finding: \"ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。\"\n    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"\n",
    "structuredPatch": [
      {
        "oldStart": 243,
        "oldLines": 3,
        "newStart": 243,
        "newLines": 49,
        "lines": [
          "     role: background",
          "     key_finding: \"ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。\"",
          "     relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"",
          "+",
          "+  # === Category: alfworld-methods ===",
          "+",
          "+  - id: shridhar2021alfworld",
          "+    title: \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\"",
          "+    authors: \"Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht\"",
          "+    year: 2021",
          "+    venue: \"ICLR 2021\"",
          "+    arxiv: \"2010.03768\"",
          "+    category: alfworld-methods",
          "+    role: evaluation",
          "+    key_finding: \"Aligns TextWorld text-based environment with ALFRED embodied benchmark, enabling abstract policy learning that transfers to visual grounding.\"",
          "+    relevance: \"我们的实验环境；134 tasks across 6 task types benchmark\"",
          "+",
          "+  - id: yao2023react",
          "+    title: \"ReAct: Synergizing Reasoning and Acting in Language Models\"",
          "+    authors: \"Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao\"",
          "+    year: 2023",
          "+    venue: \"ICLR 2023\"",
          "+    arxiv: \"2210.03629\"",
          "+    category: alfworld-methods",
          "+    role: evaluation",
          "+    key_finding: \"Interleaved reasoning traces and actions enable LLMs to ground decisions, achieving 75% on ALFWorld (single-trial).\"",
          "+    relevance: \"我们使用的 prompting paradigm（ReAct format）\"",
          "+",
          "+  - id: shinn2023reflexion",
          "+    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"",
          "+    authors: \"Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao\"",
          "+    year: 2023",
          "+    venue: \"NeurIPS 2023\"",
          "+    arxiv: \"2303.11366\"",
          "+    category: alfworld-methods",
          "+    role: evaluation",
          "+    key_finding: \"Verbal self-reflection in episodic memory achieves 97% on ALFWorld (12 trials, 130/134 tasks solved) without weight updates.\"",
          "+    relevance: \"Inference-time reflection 成功 where training-time injection 失败——对比 key point\"",
          "+",
          "+  - id: kim2025coex",
          "+    title: \"CoEx -- Co-evolving World-model and Exploration\"",
          "+    authors: \"Kim, Hwang\"",
          "+    year: 2025",
          "+    venue: \"Findings of EMNLP 2025\"",
          "+    arxiv: \"2507.22281\"",
          "+    category: alfworld-methods",
          "+    role: evaluation",
          "+    key_finding: \"Hierarchical state abstraction with dynamically updated neurosymbolic world model achieves 93.28% on ALFWorld.\"",
          "+    relevance: \"ALFWorld SOTA 参考；co-evolving world model 对比我们的 static SFT 方法\""
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

_source line 30_

4 篇已追加到 `literature_map.yaml` 的 `alfworld-methods` category：

| ID | 标题 | 作者 | Venue | arXiv |
|---|---|---|---|---|
| `shridhar2021alfworld` | ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht | ICLR 2021 | 2010.03768 |
| `yao2023react` | ReAct: Synergizing Reasoning and Acting in Language Models | Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao | ICLR 2023 | 2210.03629 |
| `shinn2023reflexion` | Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao | NeurIPS 2023 | 2303.11366 |
| `kim2025coex` | CoEx -- Co-evolving World-model and Exploration | Kim, Hwang | Findings of EMNLP 2025 | 2507.22281 |

CoEx 确认只有 2 位作者（Minsoo Kim, Seung-won Hwang），venue 为 Findings of EMNLP 2025，93.28% 数字与 ACL Anthology 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "uuid": "39cd1127-6073-43b9-b7d8-11c0da89d493",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JALezRddDqQra9rWjT6JaZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2138,
      "cache_read_input_tokens": 34870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2138
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

_source line 31_

4 篇已追加到 `literature_map.yaml` 的 `alfworld-methods` category：

| ID | 标题 | 作者 | Venue | arXiv |
|---|---|---|---|---|
| `shridhar2021alfworld` | ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht | ICLR 2021 | 2010.03768 |
| `yao2023react` | ReAct: Synergizing Reasoning and Acting in Language Models | Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao | ICLR 2023 | 2210.03629 |
| `shinn2023reflexion` | Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao | NeurIPS 2023 | 2303.11366 |
| `kim2025coex` | CoEx -- Co-evolving World-model and Exploration | Kim, Hwang | Findings of EMNLP 2025 | 2507.22281 |

CoEx 确认只有 2 位作者（Minsoo Kim, Seung-won Hwang），venue 为 Findings of EMNLP 2025，93.28% 数字与 ACL Anthology 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 67216,
  "duration_api_ms": 93396,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "97540337-c952-4edc-a06f-8b1888495ca2",
  "total_cost_usd": 0.48194675,
  "usage": {
    "input_tokens": 1505,
    "cache_creation_input_tokens": 25167,
    "cache_read_input_tokens": 132726,
    "output_tokens": 2751,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25167,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 382,
        "cache_read_input_tokens": 34870,
        "cache_creation_input_tokens": 2138,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2138
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 108435,
      "outputTokens": 2711,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 6,
      "costUSD": 0.18198999999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1505,
      "outputTokens": 2751,
      "cacheReadInputTokens": 132726,
      "cacheCreationInputTokens": 25167,
      "webSearchRequests": 0,
      "costUSD": 0.29995675,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "215ad61e-81e3-4794-8c52-225f7877defa"
}
```

</details>

---
