# paper research

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_research_20260514T194953.log`
- **Structured JSON:** [`4689975ca6bd1f1abb44.json`](../../sessions/46/4689975ca6bd1f1abb44.json)

## Before a recorded user message

28 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe",
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
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
  "uuid": "c63ebbad-7fa3-4ad9-ae76-6e249abd55d7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-agent-progress-probe/memory/"
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
    "resetsAt": 1778800200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9f4c7d2b-563b-459e-bf1a-9b08896aa289",
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2"
}
```

---

### Assistant

_source line 4_

I'll search for relevant Process Reward Model papers to add to the literature map. Let me start by loading the necessary tools and reading the current file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "be471821-b5ac-4fff-931e-d0472845c97f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rLFJazAdT53nK7qDr9Snh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11727,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11727
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WXcPmcCG16Q2YmPWJfoA6p`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "14ed4edb-4dd0-4b93-a32d-9457c9d3e6ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rLFJazAdT53nK7qDr9Snh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11727,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11727
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

_source line 6 · 2026-05-14T19:50:03.535Z_

<details><summary>↩ Tool result · `toolu_01WXcPmcCG16Q2YmPWJfoA6p`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

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
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "0cb92684-8b9c-46a5-a5eb-3693cd0f3b62",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 50
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01QwJQN3xKYSiCpMz8Q4svtD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "cfc29a81-6e48-45b9-8084-62e01902ea42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rLFJazAdT53nK7qDr9Snh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11727,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11727
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

_source line 8 · 2026-05-14T19:50:03.550Z_

<details><summary>↩ Tool result · `toolu_01QwJQN3xKYSiCpMz8Q4svtD`</summary>

```text
1	# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)
2	# Generated: 2026-05-14
3	# Paper: Temporal Label Model for Progress Stagnation Detection in LLM Agents
4	#
5	# Novelty check result: "temporal label model" as a general-purpose extension
6	# of data programming to sequential data appears NOVEL. Closest works are
7	# Safranchik AAAI 2020 (NER-specific linked HMM) and Sala NeurIPS 2019
8	# (multi-resolution WS, not temporal transitions).
9	
10	papers:
11	
12	  # ============================================================
13	  # CATEGORY: direct-competitor
14	  # ============================================================
15	
16	  - id: "xi2025agentprm"
17	    title: "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress"
18	    authors: "Zhiheng Xi, Chenyang Liao, Guanyu Li, Yajie Yang, Wenxiang Chen, Zhihao Zhang, Binghai Wang, Senjie Jin, Yuhao Zhou, Jian Guan, Wei Wu, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang"
19	    venue: "arXiv preprint"
20	    year: 2025
21	    arxiv: "2511.08325"
22	    category: "direct-competitor"
23	    role: "主要竞争者：step-level PRM for agent guidance"
24	    key_finding: "用 promise（长期潜力）和 progress（即时进展）两个维度评估 agent 每步决策，实现 8x 计算效率提升"
25	    our_differentiation: "我们是 window-level monitoring（不是 step-level guidance），不需要 outcome labels，目标是 stagnation detection 不是 reward shaping"
26	
27	  - id: "choudhury2025prm"
28	    title: "Process Reward Models for LLM Agents: Practical Framework and Directions"
29	    authors: "Sanjiban Choudhury"
30	    venue: "arXiv preprint"
31	    year: 2025
32	    arxiv: "2502.10325"
33	    category: "direct-competitor"
34	    role: "PRM 框架综述 + InversePRM 方法"
35	    key_finding: "提出 AgentPRM（Monte Carlo rollout actor-critic）和 InversePRM（从 demonstrations 学习 process reward），3B 模型超越 GPT-4o"
36	    our_differentiation: "InversePRM 仍需 demonstration trajectories，我们用 programmatic LFs 替代人工标注；我们关注 monitoring 而非 training signal"
37	
38	  - id: "li2026toolprmbench"
39	    title: "ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents"
40	    authors: "Dawei Li, Yuguang Yao, Zhen Tan, Huan Liu, Ruocheng Guo"
41	    venue: "arXiv preprint"
42	    year: 2026
43	    arxiv: "2601.12294"
44	    category: "direct-competitor"
45	    role: "Tool-use PRM 评测基准"
46	    key_finding: "大规模 benchmark 评测 PRM 在 tool-use 场景的效果，发现专用 PRM 显著优于通用 PRM"
47	    our_differentiation: "我们的 TLM 是 unsupervised（不需要 step-level reward labels），且关注 stagnation pattern 而非 step correctness"
48	
49	  - id: "wang2026planrewardbench"
50	    title: "Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling"
51	    authors: "Jiaxuan Wang, Yulan Hu, Wenjin Yang, Zheng Pan, Xin Li, Lan-Zhe Guo"
52	    venue: "arXiv preprint"
53	    year: 2026
54	    arxiv: "2604.08178"
55	    category: "direct-competitor"
56	    role: "Trajectory-level reward model 评测"
57	    key_finding: "所有 reward model 类别（generative, discriminative, LLM-as-Judge）在长 horizon trajectory 上性能显著下降"
58	    our_differentiation: "验证了长 trajectory 评估的难度——我们的 window-level 方法通过局部化避免了这个问题"
59	
60	  - id: "chen2025monitoring"
61	    title: "Monitoring LLM Agents for Sequentially Contextual Harm"
62	    authors: "Yueh-Han Chen, Neelay Joshi, Yulin Chen, He He, Rico Angell"
63	    venue: "ICLR 2025 Workshop on Building Trust in Language Models and Applications"
64	    year: 2025
65	    arxiv: null
66	    openreview: "LC0XQ6ufbr"
67	    category: "direct-competitor"
68	    role: "Agent monitoring 安全方向"
69	    key_finding: "将有害任务分解为单独无害的子任务可将 refusal rate 从 50% 降至 10%，现有 monitor 难以检测 sequentially contextual harm"
70	    our_differentiation: "他们关注 safety monitoring（harmful behavior），我们关注 progress monitoring（stagnation）；互补方向"
71	
72	  - id: "kale2025weaktostrong"
73	    title: "Reliable Weak-to-Strong Monitoring of LLM Agents"
74	    authors: "Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team, Christina Q. Knight, Zifan Wang"
75	    venue: "arXiv preprint"
76	    year: 2025
77	    arxiv: "2508.19461"
78	    category: "direct-competitor"
79	    role: "Weak-to-strong agent monitoring 方法论"
80	    key_finding: "Monitor scaffolding 比 monitor 能力更重要，弱模型可以可靠监控强模型；targeted human-in-the-loop 提升 TPR ~15%"
81	    our_differentiation: "他们用 LLM 作为 monitor，我们用 structural LFs + TLM，不依赖另一个 LLM；我们的方法更轻量且可解释"
82	
83	  # ============================================================
84	  # CATEGORY: method-component
85	  # ============================================================
86	
87	  - id: "ratner2016dataprogramming"
88	    title: "Data Programming: Creating Large Training Sets, Quickly"
89	    authors: "Alexander Ratner, Christopher De Sa, Sen Wu, Daniel Selsam, Christopher Re"
90	    venue: "NeurIPS 2016"
91	    year: 2016
92	    arxiv: "1605.07723"
93	    category: "method-component"
94	    role: "核心方法论基础：data programming 范式"
95	    key_finding: "用户编写 labeling functions（噪声启发式），generative model 学习 LF 准确率生成概率训练标签"
96	    our_differentiation: "我们扩展 data programming 到时序数据，加入 temporal transition structure"
97	
98	  - id: "ratner2017snorkel"
99	    title: "Snorkel: Rapid Training Data Creation with Weak Supervision"
100	    authors: "Alexander Ratner, Stephen H. Bach, Henry Ehrenberg, Jason Fries, Sen Wu, Christopher Re"
101	    venue: "VLDB 2018"
102	    year: 2018
103	    arxiv: "1711.10160"
104	    category: "method-component"
105	    role: "Data programming 系统实现，label model 基础"
106	    key_finding: "端到端弱监督系统：LFs → generative label model（建模 LF dependency）→ discriminative end model"
107	    our_differentiation: "Snorkel 假设数据点 i.i.d.，我们的 TLM 显式建模相邻 window 间的 label transition"
108	
109	  - id: "fu2020flyingsquid"
110	    title: "Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods"
111	    authors: "Daniel Y. Fu, Mayee F. Chen, Frederic Sala, Sarah M. Hooper, Kayvon Fatahalian, Christopher Re"
112	    venue: "ICML 2020"
113	    year: 2020
114	    arxiv: "2002.11955"
115	    category: "method-component"
116	    role: "快速 label model，triplet method of moments"
117	    key_finding: "用 triplet method 闭式求解 label model 参数，比 SGD 快 170x"
118	    our_differentiation: "FlyingSquid 同样假设 i.i.d.；我们的 TLM 需要不同的参数估计方法来处理时序依赖"
119	
120	  - id: "zhang2021wrench"
121	    title: "WRENCH: A Comprehensive Benchmark for Weak Supervision"
122	    authors: "Jieyu Zhang, Yue Yu, Yinghao Li, Yujing Wang, Yaming Yang, Mao Yang, Alexander Ratner"
123	    venue: "NeurIPS 2021 Datasets and Benchmarks Track"
124	    year: 2021
125	    arxiv: "2109.11377"
126	    category: "method-component"
127	    role: "弱监督评测基准"
128	    key_finding: "22 个真实数据集 + 120+ 方法变体评测，标准化弱监督研究"
129	    our_differentiation: "WRENCH 数据集全是 i.i.d. 分类/序列标注，没有 temporal stagnation detection 任务"
130	
131	  - id: "safranchik2020linkedhmm"
132	    title: "Weakly Supervised Sequence Tagging from Noisy Rules"
133	    authors: "Esteban Safranchik, Shiying Luo, Stephen H. Bach"
134	    venue: "AAAI 2020"
135	    year: 2020
136	    arxiv: null
137	    category: "method-component"
138	    role: "最近的方法论前驱：linked HMM for sequence tagging weak supervision"
139	    key_finding: "将 HMM 引入弱监督序列标注（NER），加入 linking rules 建模 span 结构，比 i.i.d. label model +7 F1"
140	    our_differentiation: "他们是 token-level NER（BIO 约束），我们是 window-level temporal classification；我们建模的是 stagnation temporal dynamics 而非 entity boundary"
141	
142	  - id: "sala2019multiresolution"
143	    title: "Multi-Resolution Weak Supervision for Sequential Data"
144	    authors: "Frederic Sala, Paroma Varma, Jason Fries, Daniel Y. Fu, Stefano Sagawa, Christopher Re"
145	    venue: "NeurIPS 2019"
146	    year: 2019
147	    arxiv: "1910.09505"
148	    category: "method-component"
149	    role: "最近的方法论前驱：multi-resolution WS for sequential data"
150	    key_finding: "处理不同时间分辨率的 LFs（如 frame-level vs span-level），建模 multi-resolution LF correlations"
151	    our_differentiation: "他们关注 resolution mismatch，我们关注 temporal label transitions；互补视角"
152	
153	  - id: "dawid1979em"
154	    title: "Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm"
155	    authors: "A. P. Dawid, A. M. Skene"
156	    venue: "Journal of the Royal Statistical Society, Series C"
157	    year: 1979
158	    arxiv: null
159	    category: "method-component"
160	    role: "Label aggregation 奠基工作"
161	    key_finding: "用 EM 算法估计标注者混淆矩阵，无需 ground truth"
162	    our_differentiation: "经典 i.i.d. 假设；我们的 TLM 可视为 temporal extension of Dawid-Skene for programmatic LFs"
163	
164	  - id: "nguyen2017hmmcrowd"
165	    title: "Aggregating and Predicting Sequence Labels from Crowd Annotations"
166	    authors: "An Thanh Nguyen, Byron C. Wallace, Junyi Jessy Li, Ani Nenkova, Matthew Lease"
167	    venue: "ACL 2017"
168	    year: 2017
169	    arxiv: null
170	    category: "method-component"
171	    role: "HMM + crowdsourcing label aggregation"
172	    key_finding: "HMM-Crowd：扩展 Dawid-Skene 到序列数据，加入 one-step Markov structure over true labels"
173	    our_differentiation: "他们用于 crowdsourcing（人类标注者），我们用于 programmatic LFs（自动化）；他们是 NER/IE，我们是 agent progress monitoring"
174	
175	  # ============================================================
176	  # CATEGORY: evaluation
177	  # ============================================================
178	
179	  - id: "orlanski2026slopcodebench"
180	    title: "SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks"
181	    authors: "Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu, Albert Ge, Dyah Adila, Nicholas Roberts, Frederic Sala, Aws Albarghouthi"
182	    venue: "arXiv preprint"
183	    year: 2026
184	    arxiv: "2603.24755"
185	    category: "evaluation"
186	    role: "Agent degradation 基准——直接支持我们的 problem motivation"
187	    key_finding: "Agent 代码质量在迭代任务中持续退化：比人类代码 2.3x 更冗余、2.0x 更结构侵蚀，75-77% trajectory 呈现退化趋势"
188	    our_differentiation: "SlopCodeBench 量化了 degradation 现象，我们提供了检测方法；他们是 post-hoc 评测，我们是 online monitoring"
189	
190	  - id: "jimenez2024swebench"
191	    title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
192	    authors: "Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan"
193	    venue: "ICLR 2024"
194	    year: 2024
195	    arxiv: "2310.06770"
196	    category: "evaluation"
197	    role: "Agent 数据来源之一"
198	    key_finding: "2294 个真实 GitHub issue 任务，标准化 agent 评测"
199	    our_differentiation: "我们使用 SWE-bench agent trajectories 作为实验数据源之一"
200	
201	  - id: "yang2024sweagent"
202	    title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
203	    authors: "John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press"
204	    venue: "NeurIPS 2024"
205	    year: 2024
206	    arxiv: "2405.15793"
207	    category: "evaluation"
208	    role: "Agent 系统——trajectory 数据来源"
209	    key_finding: "提出 agent-computer interface (ACI)，GPT-4 Turbo 在 SWE-bench 达 12.47% resolve rate"
210	    our_differentiation: "SWE-agent trajectories 是我们分析 stagnation 的数据来源之一"
211	
212	  - id: "wang2025openhands"
213	    title: "OpenHands: An Open Platform for AI Software Developers as Generalist Agents"
214	    authors: "Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al."
215	    venue: "ICLR 2025"
216	    year: 2025
217	    arxiv: "2407.16741"
218	    category: "evaluation"
219	    role: "Agent 平台——主要数据来源"
220	    key_finding: "开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测"
221	    our_differentiation: "OpenHands trajectories 是我们的主要实验数据来源"
222	
223	  # ============================================================
224	  # CATEGORY: background
225	  # ============================================================
226	
227	  - id: "shinn2023reflexion"
228	    title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
229	    authors: "Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao"
230	    venue: "NeurIPS 2023"
231	    year: 2023
232	    arxiv: "2303.11366"
233	    category: "background"
234	    role: "Agent self-reflection 代表工作"
235	    key_finding: "通过 verbal feedback 强化 agent，反思文本存入 episodic memory 用于后续 trial"
236	    our_differentiation: "Reflexion 是 agent 自我改进机制，我们是外部 monitoring；self-reflection 可能失效时我们的 monitor 仍能检测 stagnation"
237	
238	  - id: "zhou2024lats"
239	    title: "Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models"
240	    authors: "Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang"
241	    venue: "ICML 2024"
242	    year: 2024
243	    arxiv: "2310.04406"
244	    category: "background"
245	    role: "Agent planning + self-reflection"
246	    key_finding: "结合 MCTS 与 LM value function 和 self-reflection，支持 backtracking"
247	    our_differentiation: "LATS 通过搜索避免 stagnation，但计算开销大；我们的 monitor 可作为 LATS 的早期终止信号"
248	
249	  - id: "yao2023tot"
250	    title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
251	    authors: "Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan"
252	    venue: "NeurIPS 2023"
253	    year: 2023
254	    arxiv: "2305.10601"
255	    category: "background"
256	    role: "Deliberate reasoning 框架"
257	    key_finding: "将 CoT 泛化为树结构，LM 自我评估中间 thought 并 backtrack"
258	    our_differentiation: "ToT 的自评估是 single-step 的；我们捕捉 multi-step temporal patterns"
259	
260	  - id: "cemri2025multiagentfail"
261	    title: "Why Do Multi-Agent LLM Systems Fail?"
262	    authors: "Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, et al."
263	    venue: "arXiv preprint"
264	    year: 2025
265	    arxiv: "2503.13657"
266	    category: "background"
267	    role: "Agent failure taxonomy——problem motivation"
268	    key_finding: "MAST taxonomy：14 种失败模式，其中 Step Repetition 被识别为具体失败症状"
269	    our_differentiation: "他们提供 taxonomy（what fails），我们提供 detection method（how to detect）"
270	
271	  - id: "zhu2025agentfail"
272	    title: "Where LLM Agents Fail and How They Can Learn From Failures"
273	    authors: "Kunlun Zhu, Zijia Liu, Bingxuan Li, et al."
274	    venue: "arXiv preprint"
275	    year: 2025
276	    arxiv: "2509.25370"
277	    category: "background"
278	    role: "Agent failure 分析 + cascading failure 发现"
279	    key_finding: "Cascading failures（单一 root cause 传播到后续决策）是长 horizon 任务的主要失败模式"
280	    our_differentiation: "Cascading failure 正是我们 temporal model 可以捕捉的 pattern——stagnation 往往是 cascade 的表现"
281	
282	  - id: "george2025cycledetection"
283	    title: "Unsupervised Cycle Detection in Agentic Applications"
284	    authors: "Felix George, Harshit Kumar, Divya Pathak, Kaustabha Ray, Mudit Verma, Pratibha Moogi"
285	    venue: "arXiv preprint (IBM Research)"
286	    year: 2025
287	    arxiv: "2511.10650"
288	    category: "background"
289	    role: "Cycle detection——最相关的 stagnation detection 前驱"
290	    key_finding: "混合方法：call-stack 分析（结构重复）+ embedding 语义相似度确认"
291	    our_differentiation: "他们只检测 exact/near-exact cycles，我们检测更广义的 stagnation（包括非重复性的停滞）；他们是 unsupervised rule-based，我们是 learned temporal model"
292	
293	  - id: "pipis2025reasoningloop"
294	    title: "Wait, Wait, Wait... Why Do Reasoning Models Loop?"
295	    authors: "Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos"
296	    venue: "arXiv preprint"
297	    year: 2025
298	    arxiv: "2512.12895"
299	    category: "background"
300	    role: "Reasoning model looping 分析"
301	    key_finding: "Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测"
302	    our_differentiation: "他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一"
303	
304	  # ============================================================
305	  # CATEGORY: technique
306	  # ============================================================
307	
308	  - id: "cho2014gru"
309	    title: "Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation"
310	    authors: "Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio"
311	    venue: "EMNLP 2014"
312	    year: 2014
313	    arxiv: "1406.1078"
314	    category: "technique"
315	    role: "GRU 原始论文——我们 probe model 的序列编码器"
316	    key_finding: "提出 GRU hidden unit，自适应门控信息流"
317	
318	  - id: "bahdanau2015attention"
319	    title: "Neural Machine Translation by Jointly Learning to Align and Translate"
320	    authors: "Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio"
321	    venue: "ICLR 2015"
322	    year: 2015
323	    arxiv: "1409.0473"
324	    category: "technique"
325	    role: "Attention mechanism——我们 probe model 的 attention 组件"
326	    key_finding: "注意力机制允许 decoder 选择性关注输入序列不同位置"
327	
328	  - id: "khosla2020supcon"
329	    title: "Supervised Contrastive Learning"
330	    authors: "Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, Dilip Krishnan"
331	    venue: "NeurIPS 2020"
332	    year: 2020
333	    arxiv: "2004.11362"
334	    category: "technique"
335	    role: "SupCon loss——我们的辅助训练目标"
336	    key_finding: "扩展自监督对比学习到有监督设置，同类样本拉近、异类推远，提升鲁棒性"
337	
338	  - id: "zhang2025qwen3embedding"
339	    title: "Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models"
340	    authors: "Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou"
341	    venue: "arXiv preprint"
342	    year: 2025
343	    arxiv: "2506.05176"
344	    category: "technique"
345	    role: "Embedding model——我们用于生成 trajectory window embeddings"
346	    key_finding: "基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA"
347	
348	# ============================================================
349	# NOVELTY ANALYSIS SUMMARY
350	# ============================================================
351	#
352	# Key finding: "Temporal Label Model" 作为通用方法论是 NOVEL。
353	#
354	# 最近的前驱工作：
355	# 1. Safranchik AAAI 2020 (linked HMM) — NER-specific，BIO 约束，token-level
356	# 2. Sala NeurIPS 2019 (multi-resolution WS) — 处理分辨率不匹配，不建模 label transition
357	# 3. Nguyen ACL 2017 (HMM-Crowd) — crowdsourcing 场景，不是 programmatic LFs
358	#
359	# 没有人将 data programming + HMM-style temporal transitions 用于：
360	# - 通用序列分类（非 NER）
361	# - Agent trajectory monitoring
362	# - Stagnation detection
363	#
364	# 我们的 TLM 填补的空白：general-purpose temporal extension of
365	# data programming label models for sequential classification tasks.
366	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "51d9db2d-5aef-4e4d-8a14-3b82232b4686",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
      "content": "# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)\n# Generated: 2026-05-14\n# Paper: Temporal Label Model for Progress Stagnation Detection in LLM Agents\n#\n# Novelty check result: \"temporal label model\" as a general-purpose extension\n# of data programming to sequential data appears NOVEL. Closest works are\n# Safranchik AAAI 2020 (NER-specific linked HMM) and Sala NeurIPS 2019\n# (multi-resolution WS, not temporal transitions).\n\npapers:\n\n  # ============================================================\n  # CATEGORY: direct-competitor\n  # ============================================================\n\n  - id: \"xi2025agentprm\"\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Zhiheng Xi, Chenyang Liao, Guanyu Li, Yajie Yang, Wenxiang Chen, Zhihao Zhang, Binghai Wang, Senjie Jin, Yuhao Zhou, Jian Guan, Wei Wu, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2511.08325\"\n    category: \"direct-competitor\"\n    role: \"主要竞争者：step-level PRM for agent guidance\"\n    key_finding: \"用 promise（长期潜力）和 progress（即时进展）两个维度评估 agent 每步决策，实现 8x 计算效率提升\"\n    our_differentiation: \"我们是 window-level monitoring（不是 step-level guidance），不需要 outcome labels，目标是 stagnation detection 不是 reward shaping\"\n\n  - id: \"choudhury2025prm\"\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Sanjiban Choudhury\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2502.10325\"\n    category: \"direct-competitor\"\n    role: \"PRM 框架综述 + InversePRM 方法\"\n    key_finding: \"提出 AgentPRM（Monte Carlo rollout actor-critic）和 InversePRM（从 demonstrations 学习 process reward），3B 模型超越 GPT-4o\"\n    our_differentiation: \"InversePRM 仍需 demonstration trajectories，我们用 programmatic LFs 替代人工标注；我们关注 monitoring 而非 training signal\"\n\n  - id: \"li2026toolprmbench\"\n    title: \"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents\"\n    authors: \"Dawei Li, Yuguang Yao, Zhen Tan, Huan Liu, Ruocheng Guo\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.12294\"\n    category: \"direct-competitor\"\n    role: \"Tool-use PRM 评测基准\"\n    key_finding: \"大规模 benchmark 评测 PRM 在 tool-use 场景的效果，发现专用 PRM 显著优于通用 PRM\"\n    our_differentiation: \"我们的 TLM 是 unsupervised（不需要 step-level reward labels），且关注 stagnation pattern 而非 step correctness\"\n\n  - id: \"wang2026planrewardbench\"\n    title: \"Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling\"\n    authors: \"Jiaxuan Wang, Yulan Hu, Wenjin Yang, Zheng Pan, Xin Li, Lan-Zhe Guo\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.08178\"\n    category: \"direct-competitor\"\n    role: \"Trajectory-level reward model 评测\"\n    key_finding: \"所有 reward model 类别（generative, discriminative, LLM-as-Judge）在长 horizon trajectory 上性能显著下降\"\n    our_differentiation: \"验证了长 trajectory 评估的难度——我们的 window-level 方法通过局部化避免了这个问题\"\n\n  - id: \"chen2025monitoring\"\n    title: \"Monitoring LLM Agents for Sequentially Contextual Harm\"\n    authors: \"Yueh-Han Chen, Neelay Joshi, Yulin Chen, He He, Rico Angell\"\n    venue: \"ICLR 2025 Workshop on Building Trust in Language Models and Applications\"\n    year: 2025\n    arxiv: null\n    openreview: \"LC0XQ6ufbr\"\n    category: \"direct-competitor\"\n    role: \"Agent monitoring 安全方向\"\n    key_finding: \"将有害任务分解为单独无害的子任务可将 refusal rate 从 50% 降至 10%，现有 monitor 难以检测 sequentially contextual harm\"\n    our_differentiation: \"他们关注 safety monitoring（harmful behavior），我们关注 progress monitoring（stagnation）；互补方向\"\n\n  - id: \"kale2025weaktostrong\"\n    title: \"Reliable Weak-to-Strong Monitoring of LLM Agents\"\n    authors: \"Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team, Christina Q. Knight, Zifan Wang\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2508.19461\"\n    category: \"direct-competitor\"\n    role: \"Weak-to-strong agent monitoring 方法论\"\n    key_finding: \"Monitor scaffolding 比 monitor 能力更重要，弱模型可以可靠监控强模型；targeted human-in-the-loop 提升 TPR ~15%\"\n    our_differentiation: \"他们用 LLM 作为 monitor，我们用 structural LFs + TLM，不依赖另一个 LLM；我们的方法更轻量且可解释\"\n\n  # ============================================================\n  # CATEGORY: method-component\n  # ============================================================\n\n  - id: \"ratner2016dataprogramming\"\n    title: \"Data Programming: Creating Large Training Sets, Quickly\"\n    authors: \"Alexander Ratner, Christopher De Sa, Sen Wu, Daniel Selsam, Christopher Re\"\n    venue: \"NeurIPS 2016\"\n    year: 2016\n    arxiv: \"1605.07723\"\n    category: \"method-component\"\n    role: \"核心方法论基础：data programming 范式\"\n    key_finding: \"用户编写 labeling functions（噪声启发式），generative model 学习 LF 准确率生成概率训练标签\"\n    our_differentiation: \"我们扩展 data programming 到时序数据，加入 temporal transition structure\"\n\n  - id: \"ratner2017snorkel\"\n    title: \"Snorkel: Rapid Training Data Creation with Weak Supervision\"\n    authors: \"Alexander Ratner, Stephen H. Bach, Henry Ehrenberg, Jason Fries, Sen Wu, Christopher Re\"\n    venue: \"VLDB 2018\"\n    year: 2018\n    arxiv: \"1711.10160\"\n    category: \"method-component\"\n    role: \"Data programming 系统实现，label model 基础\"\n    key_finding: \"端到端弱监督系统：LFs → generative label model（建模 LF dependency）→ discriminative end model\"\n    our_differentiation: \"Snorkel 假设数据点 i.i.d.，我们的 TLM 显式建模相邻 window 间的 label transition\"\n\n  - id: \"fu2020flyingsquid\"\n    title: \"Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods\"\n    authors: \"Daniel Y. Fu, Mayee F. Chen, Frederic Sala, Sarah M. Hooper, Kayvon Fatahalian, Christopher Re\"\n    venue: \"ICML 2020\"\n    year: 2020\n    arxiv: \"2002.11955\"\n    category: \"method-component\"\n    role: \"快速 label model，triplet method of moments\"\n    key_finding: \"用 triplet method 闭式求解 label model 参数，比 SGD 快 170x\"\n    our_differentiation: \"FlyingSquid 同样假设 i.i.d.；我们的 TLM 需要不同的参数估计方法来处理时序依赖\"\n\n  - id: \"zhang2021wrench\"\n    title: \"WRENCH: A Comprehensive Benchmark for Weak Supervision\"\n    authors: \"Jieyu Zhang, Yue Yu, Yinghao Li, Yujing Wang, Yaming Yang, Mao Yang, Alexander Ratner\"\n    venue: \"NeurIPS 2021 Datasets and Benchmarks Track\"\n    year: 2021\n    arxiv: \"2109.11377\"\n    category: \"method-component\"\n    role: \"弱监督评测基准\"\n    key_finding: \"22 个真实数据集 + 120+ 方法变体评测，标准化弱监督研究\"\n    our_differentiation: \"WRENCH 数据集全是 i.i.d. 分类/序列标注，没有 temporal stagnation detection 任务\"\n\n  - id: \"safranchik2020linkedhmm\"\n    title: \"Weakly Supervised Sequence Tagging from Noisy Rules\"\n    authors: \"Esteban Safranchik, Shiying Luo, Stephen H. Bach\"\n    venue: \"AAAI 2020\"\n    year: 2020\n    arxiv: null\n    category: \"method-component\"\n    role: \"最近的方法论前驱：linked HMM for sequence tagging weak supervision\"\n    key_finding: \"将 HMM 引入弱监督序列标注（NER），加入 linking rules 建模 span 结构，比 i.i.d. label model +7 F1\"\n    our_differentiation: \"他们是 token-level NER（BIO 约束），我们是 window-level temporal classification；我们建模的是 stagnation temporal dynamics 而非 entity boundary\"\n\n  - id: \"sala2019multiresolution\"\n    title: \"Multi-Resolution Weak Supervision for Sequential Data\"\n    authors: \"Frederic Sala, Paroma Varma, Jason Fries, Daniel Y. Fu, Stefano Sagawa, Christopher Re\"\n    venue: \"NeurIPS 2019\"\n    year: 2019\n    arxiv: \"1910.09505\"\n    category: \"method-component\"\n    role: \"最近的方法论前驱：multi-resolution WS for sequential data\"\n    key_finding: \"处理不同时间分辨率的 LFs（如 frame-level vs span-level），建模 multi-resolution LF correlations\"\n    our_differentiation: \"他们关注 resolution mismatch，我们关注 temporal label transitions；互补视角\"\n\n  - id: \"dawid1979em\"\n    title: \"Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm\"\n    authors: \"A. P. Dawid, A. M. Skene\"\n    venue: \"Journal of the Royal Statistical Society, Series C\"\n    year: 1979\n    arxiv: null\n    category: \"method-component\"\n    role: \"Label aggregation 奠基工作\"\n    key_finding: \"用 EM 算法估计标注者混淆矩阵，无需 ground truth\"\n    our_differentiation: \"经典 i.i.d. 假设；我们的 TLM 可视为 temporal extension of Dawid-Skene for programmatic LFs\"\n\n  - id: \"nguyen2017hmmcrowd\"\n    title: \"Aggregating and Predicting Sequence Labels from Crowd Annotations\"\n    authors: \"An Thanh Nguyen, Byron C. Wallace, Junyi Jessy Li, Ani Nenkova, Matthew Lease\"\n    venue: \"ACL 2017\"\n    year: 2017\n    arxiv: null\n    category: \"method-component\"\n    role: \"HMM + crowdsourcing label aggregation\"\n    key_finding: \"HMM-Crowd：扩展 Dawid-Skene 到序列数据，加入 one-step Markov structure over true labels\"\n    our_differentiation: \"他们用于 crowdsourcing（人类标注者），我们用于 programmatic LFs（自动化）；他们是 NER/IE，我们是 agent progress monitoring\"\n\n  # ============================================================\n  # CATEGORY: evaluation\n  # ============================================================\n\n  - id: \"orlanski2026slopcodebench\"\n    title: \"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks\"\n    authors: \"Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu, Albert Ge, Dyah Adila, Nicholas Roberts, Frederic Sala, Aws Albarghouthi\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.24755\"\n    category: \"evaluation\"\n    role: \"Agent degradation 基准——直接支持我们的 problem motivation\"\n    key_finding: \"Agent 代码质量在迭代任务中持续退化：比人类代码 2.3x 更冗余、2.0x 更结构侵蚀，75-77% trajectory 呈现退化趋势\"\n    our_differentiation: \"SlopCodeBench 量化了 degradation 现象，我们提供了检测方法；他们是 post-hoc 评测，我们是 online monitoring\"\n\n  - id: \"jimenez2024swebench\"\n    title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n    authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2310.06770\"\n    category: \"evaluation\"\n    role: \"Agent 数据来源之一\"\n    key_finding: \"2294 个真实 GitHub issue 任务，标准化 agent 评测\"\n    our_differentiation: \"我们使用 SWE-bench agent trajectories 作为实验数据源之一\"\n\n  - id: \"yang2024sweagent\"\n    title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n    authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv: \"2405.15793\"\n    category: \"evaluation\"\n    role: \"Agent 系统——trajectory 数据来源\"\n    key_finding: \"提出 agent-computer interface (ACI)，GPT-4 Turbo 在 SWE-bench 达 12.47% resolve rate\"\n    our_differentiation: \"SWE-agent trajectories 是我们分析 stagnation 的数据来源之一\"\n\n  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================\n\n  - id: \"shinn2023reflexion\"\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    arxiv: \"2303.11366\"\n    category: \"background\"\n    role: \"Agent self-reflection 代表工作\"\n    key_finding: \"通过 verbal feedback 强化 agent，反思文本存入 episodic memory 用于后续 trial\"\n    our_differentiation: \"Reflexion 是 agent 自我改进机制，我们是外部 monitoring；self-reflection 可能失效时我们的 monitor 仍能检测 stagnation\"\n\n  - id: \"zhou2024lats\"\n    title: \"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\"\n    authors: \"Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang\"\n    venue: \"ICML 2024\"\n    year: 2024\n    arxiv: \"2310.04406\"\n    category: \"background\"\n    role: \"Agent planning + self-reflection\"\n    key_finding: \"结合 MCTS 与 LM value function 和 self-reflection，支持 backtracking\"\n    our_differentiation: \"LATS 通过搜索避免 stagnation，但计算开销大；我们的 monitor 可作为 LATS 的早期终止信号\"\n\n  - id: \"yao2023tot\"\n    title: \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\"\n    authors: \"Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    arxiv: \"2305.10601\"\n    category: \"background\"\n    role: \"Deliberate reasoning 框架\"\n    key_finding: \"将 CoT 泛化为树结构，LM 自我评估中间 thought 并 backtrack\"\n    our_differentiation: \"ToT 的自评估是 single-step 的；我们捕捉 multi-step temporal patterns\"\n\n  - id: \"cemri2025multiagentfail\"\n    title: \"Why Do Multi-Agent LLM Systems Fail?\"\n    authors: \"Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2503.13657\"\n    category: \"background\"\n    role: \"Agent failure taxonomy——problem motivation\"\n    key_finding: \"MAST taxonomy：14 种失败模式，其中 Step Repetition 被识别为具体失败症状\"\n    our_differentiation: \"他们提供 taxonomy（what fails），我们提供 detection method（how to detect）\"\n\n  - id: \"zhu2025agentfail\"\n    title: \"Where LLM Agents Fail and How They Can Learn From Failures\"\n    authors: \"Kunlun Zhu, Zijia Liu, Bingxuan Li, et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2509.25370\"\n    category: \"background\"\n    role: \"Agent failure 分析 + cascading failure 发现\"\n    key_finding: \"Cascading failures（单一 root cause 传播到后续决策）是长 horizon 任务的主要失败模式\"\n    our_differentiation: \"Cascading failure 正是我们 temporal model 可以捕捉的 pattern——stagnation 往往是 cascade 的表现\"\n\n  - id: \"george2025cycledetection\"\n    title: \"Unsupervised Cycle Detection in Agentic Applications\"\n    authors: \"Felix George, Harshit Kumar, Divya Pathak, Kaustabha Ray, Mudit Verma, Pratibha Moogi\"\n    venue: \"arXiv preprint (IBM Research)\"\n    year: 2025\n    arxiv: \"2511.10650\"\n    category: \"background\"\n    role: \"Cycle detection——最相关的 stagnation detection 前驱\"\n    key_finding: \"混合方法：call-stack 分析（结构重复）+ embedding 语义相似度确认\"\n    our_differentiation: \"他们只检测 exact/near-exact cycles，我们检测更广义的 stagnation（包括非重复性的停滞）；他们是 unsupervised rule-based，我们是 learned temporal model\"\n\n  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================\n\n  - id: \"cho2014gru\"\n    title: \"Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation\"\n    authors: \"Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio\"\n    venue: \"EMNLP 2014\"\n    year: 2014\n    arxiv: \"1406.1078\"\n    category: \"technique\"\n    role: \"GRU 原始论文——我们 probe model 的序列编码器\"\n    key_finding: \"提出 GRU hidden unit，自适应门控信息流\"\n\n  - id: \"bahdanau2015attention\"\n    title: \"Neural Machine Translation by Jointly Learning to Align and Translate\"\n    authors: \"Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio\"\n    venue: \"ICLR 2015\"\n    year: 2015\n    arxiv: \"1409.0473\"\n    category: \"technique\"\n    role: \"Attention mechanism——我们 probe model 的 attention 组件\"\n    key_finding: \"注意力机制允许 decoder 选择性关注输入序列不同位置\"\n\n  - id: \"khosla2020supcon\"\n    title: \"Supervised Contrastive Learning\"\n    authors: \"Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, Dilip Krishnan\"\n    venue: \"NeurIPS 2020\"\n    year: 2020\n    arxiv: \"2004.11362\"\n    category: \"technique\"\n    role: \"SupCon loss——我们的辅助训练目标\"\n    key_finding: \"扩展自监督对比学习到有监督设置，同类样本拉近、异类推远，提升鲁棒性\"\n\n  - id: \"zhang2025qwen3embedding\"\n    title: \"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models\"\n    authors: \"Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2506.05176\"\n    category: \"technique\"\n    role: \"Embedding model——我们用于生成 trajectory window embeddings\"\n    key_finding: \"基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA\"\n\n# ============================================================\n# NOVELTY ANALYSIS SUMMARY\n# ============================================================\n#\n# Key finding: \"Temporal Label Model\" 作为通用方法论是 NOVEL。\n#\n# 最近的前驱工作：\n# 1. Safranchik AAAI 2020 (linked HMM) — NER-specific，BIO 约束，token-level\n# 2. Sala NeurIPS 2019 (multi-resolution WS) — 处理分辨率不匹配，不建模 label transition\n# 3. Nguyen ACL 2017 (HMM-Crowd) — crowdsourcing 场景，不是 programmatic LFs\n#\n# 没有人将 data programming + HMM-style temporal transitions 用于：\n# - 通用序列分类（非 NER）\n# - Agent trajectory monitoring\n# - Stagnation detection\n#\n# 我们的 TLM 填补的空白：general-purpose temporal extension of\n# data programming label models for sequential classification tasks.\n",
      "numLines": 366,
      "startLine": 1,
      "totalLines": 366
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
Now I need to search for relevant PRM papers. Let me search for papers in the directions specified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "0cfbab78-f759-4406-84a6-bae6332436ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzcFugsxnr5AW1mc5a746Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8891,
      "cache_read_input_tokens": 23568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8891
      },
      "output_tokens": 25,
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

Now let me search for relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "4680d160-1d63-43d9-ab95-ee0947dfe736",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzcFugsxnr5AW1mc5a746Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8891,
      "cache_read_input_tokens": 23568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8891
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_012X7rXzHrmNBqN9wv7E8pmQ`</summary>

```json
{
  "query": "process reward model LLM agent step-level supervision 2024 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "1c458a2f-e494-43d5-886b-1fed6aab706e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzcFugsxnr5AW1mc5a746Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8891,
      "cache_read_input_tokens": 23568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8891
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LTtE4RJgpSdUY1HK2WHAvE`</summary>

```json
{
  "query": "CodeRL process reward model code generation agent 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "84117ebf-030f-4194-b188-dc4c4a535c5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzcFugsxnr5AW1mc5a746Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8891,
      "cache_read_input_tokens": 23568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8891
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KnXwSXefeRKAaLs5LFY6wz`</summary>

```json
{
  "query": "process supervision outcome supervision agent training reward model 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "257c201e-02c0-4257-804b-f6328fc81c20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzcFugsxnr5AW1mc5a746Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8891,
      "cache_read_input_tokens": 23568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8891
      },
      "output_tokens": 25,
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

_source line 14 · 2026-05-14T19:50:15.036Z_

<details><summary>↩ Tool result · `toolu_012X7rXzHrmNBqN9wv7E8pmQ`</summary>

```text
Web search results for query: "process reward model LLM agent step-level supervision 2024 2025 2026 arXiv"

Links: [{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Proceedings of the ACM Web Conference 2026","url":"https://dl.acm.org/doi/10.1145/3774904.3792551"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/html/2502.10325v1"},{"title":"[2510.08049] A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/abs/2510.08049"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress","url":"https://arxiv.org/html/2511.08325v1"},{"title":"Principle Process Reward For Search Agents | OpenReview","url":"https://openreview.net/forum?id=zN1aqLhkGm"},{"title":"GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub","url":"https://github.com/bobxwu/learning-from-rewards-llm-papers"},{"title":"[2511.08325] AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress","url":"https://arxiv.org/abs/2511.08325"},{"title":"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis","url":"https://arxiv.org/html/2604.24198v1"},{"title":"Process Reward Models Meet Planning: Generating Precise and Scalable Datasets for Step-Level Rewards","url":"https://arxiv.org/html/2604.17957"}]

I've successfully performed a web search on process reward models for LLM agents with step-level supervision from 2024-2026 on arXiv. Here are the key findings:

## Recent Research on Process Reward Models for LLM Agents

### Main Papers Found:

1. **AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress**
   - A process supervision model designed for LLM agents in multi-step decision-making tasks that captures both the probability of each step achieving the goal (promise) and the interdependence between sequential steps (progress)
   - Small 3B models trained with AgentPRM outperform strong GPT-4o baselines on the ALFWorld benchmark

2. **Survey on Process Reward Models** (arXiv 2510.08049)
   - PRMs address the gap by evaluating and guiding reasoning at the step or trajectory level, providing a systematic overview through how to generate process data, build PRMs, and use PRMs for test-time scaling and reinforcement learning
   - Applications span math, code, text, multimodal reasoning, robotics, and agents

3. **Process Reward Models for Agent Applications**
   - PRMs have shown success in mathematical reasoning and code generation, providing step-level supervision and fine-grained verification during both training and inference time

4. **Comprehensive Resources**
   - Notable recent work includes papers on AdaptiveStep, VersaPRM, and various agent-focused PRM studies from 2025

The search results reveal an active research area with multiple approaches to applying process-level supervision to LLM agents across 2024-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "352f6623-eaa7-4807-9ed2-3e31e8dd7d15",
  "tool_use_result": {
    "query": "process reward model LLM agent step-level supervision 2024 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KCnJKhqtgUkGu32Drz85F2",
        "content": [
          {
            "title": "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Proceedings of the ACM Web Conference 2026",
            "url": "https://dl.acm.org/doi/10.1145/3774904.3792551"
          },
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          },
          {
            "title": "Process Reward Models for LLM Agents: Practical Framework and Directions",
            "url": "https://arxiv.org/html/2502.10325v1"
          },
          {
            "title": "[2510.08049] A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/abs/2510.08049"
          },
          {
            "title": "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress",
            "url": "https://arxiv.org/html/2511.08325v1"
          },
          {
            "title": "Principle Process Reward For Search Agents | OpenReview",
            "url": "https://openreview.net/forum?id=zN1aqLhkGm"
          },
          {
            "title": "GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub",
            "url": "https://github.com/bobxwu/learning-from-rewards-llm-papers"
          },
          {
            "title": "[2511.08325] AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress",
            "url": "https://arxiv.org/abs/2511.08325"
          },
          {
            "title": "Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis",
            "url": "https://arxiv.org/html/2604.24198v1"
          },
          {
            "title": "Process Reward Models Meet Planning: Generating Precise and Scalable Datasets for Step-Level Rewards",
            "url": "https://arxiv.org/html/2604.17957"
          }
        ]
      },
      "I've successfully performed a web search on process reward models for LLM agents with step-level supervision from 2024-2026 on arXiv. Here are the key findings:\n\n## Recent Research on Process Reward Models for LLM Agents\n\n### Main Papers Found:\n\n1. **AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress**\n   - A process supervision model designed for LLM agents in multi-step decision-making tasks that captures both the probability of each step achieving the goal (promise) and the interdependence between sequential steps (progress)\n   - Small 3B models trained with AgentPRM outperform strong GPT-4o baselines on the ALFWorld benchmark\n\n2. **Survey on Process Reward Models** (arXiv 2510.08049)\n   - PRMs address the gap by evaluating and guiding reasoning at the step or trajectory level, providing a systematic overview through how to generate process data, build PRMs, and use PRMs for test-time scaling and reinforcement learning\n   - Applications span math, code, text, multimodal reasoning, robotics, and agents\n\n3. **Process Reward Models for Agent Applications**\n   - PRMs have shown success in mathematical reasoning and code generation, providing step-level supervision and fine-grained verification during both training and inference time\n\n4. **Comprehensive Resources**\n   - Notable recent work includes papers on AdaptiveStep, VersaPRM, and various agent-focused PRM studies from 2025\n\nThe search results reveal an active research area with multiple approaches to applying process-level supervision to LLM agents across 2024-2026."
    ],
    "durationSeconds": 7.361266717999999
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T19:50:15.659Z_

<details><summary>↩ Tool result · `toolu_01LTtE4RJgpSdUY1HK2WHAvE`</summary>

```text
Web search results for query: "CodeRL process reward model code generation agent 2024 2025 arXiv"

Links: [{"title":"[2510.18471] CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment","url":"https://arxiv.org/abs/2510.18471"},{"title":"Preprint, September 2025 CODERL+: Improving Code Generation via Reinforce-","url":"https://www.arxiv.org/pdf/2510.18471"},{"title":"CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment","url":"https://arxiv.org/html/2510.18471v1"},{"title":"CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment | Request PDF","url":"https://www.researchgate.net/publication/396747277_CodeRL_Improving_Code_Generation_via_Reinforcement_with_Execution_Semantics_Alignment"},{"title":"Autonomous Code Generation with Reinforcement- ...","url":"https://www.ijrai.org/index.php/ijrai/article/download/95/92"},{"title":"[2502.10325] Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/abs/2502.10325"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub","url":"https://github.com/bobxwu/learning-from-rewards-llm-papers"},{"title":"Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/html/2502.10325v1"},{"title":"GitHub - salesforce/CodeRL: This is the official code for the paper CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning (NeurIPS22). · GitHub","url":"https://github.com/salesforce/CodeRL"}]

Based on the search results, I found several highly relevant papers on CodeRL and process reward models for code generation. Here's what I discovered:

## CodeRL+: Recent Development (2025)

CodeRL+, proposed in a recent arXiv paper, integrates execution semantics alignment into the RLVR (Reinforcement Learning with Verifiable Rewards) training pipeline for code generation. CodeRL+ enables the model to infer variable-level execution trajectory, providing a direct learning signal of execution semantics. Extensive experiments demonstrate that CodeRL+ outperforms post-training baselines (including RLVR and Distillation), achieving a 4.6% average relative improvement in pass@1.

## Process Reward Models in Code Generation

CodePRM (Li et al., 2025b) addresses the sparse reward problem through process reward models that provide dense feedback. The search results also reference recent work on process reward models more broadly.

## Agent Process Reward Models (2025)

Agent Process Reward Models (AgentPRM) is a simple and scalable framework for training LLM agents to continually improve through interactions, following a lightweight actor-critic paradigm using Monte Carlo rollouts to compute reward targets and optimize policies.

## Historical Context

Early explorations such as CodeRL (Le et al., 2022) employ actor-critic frameworks to leverage unit test feedback for code generation.

The search revealed active research in combining reinforcement learning with code generation, with recent focus on improving reward signals through process-level feedback and execution semantics alignment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "ba42eb1d-c57d-4b33-b4e7-873ee424a093",
  "tool_use_result": {
    "query": "CodeRL process reward model code generation agent 2024 2025 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_014BhqEb8hwJzESB9VcG9kiF",
        "content": [
          {
            "title": "[2510.18471] CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment",
            "url": "https://arxiv.org/abs/2510.18471"
          },
          {
            "title": "Preprint, September 2025 CODERL+: Improving Code Generation via Reinforce-",
            "url": "https://www.arxiv.org/pdf/2510.18471"
          },
          {
            "title": "CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment",
            "url": "https://arxiv.org/html/2510.18471v1"
          },
          {
            "title": "CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment | Request PDF",
            "url": "https://www.researchgate.net/publication/396747277_CodeRL_Improving_Code_Generation_via_Reinforcement_with_Execution_Semantics_Alignment"
          },
          {
            "title": "Autonomous Code Generation with Reinforcement- ...",
            "url": "https://www.ijrai.org/index.php/ijrai/article/download/95/92"
          },
          {
            "title": "[2502.10325] Process Reward Models for LLM Agents: Practical Framework and Directions",
            "url": "https://arxiv.org/abs/2502.10325"
          },
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          },
          {
            "title": "GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub",
            "url": "https://github.com/bobxwu/learning-from-rewards-llm-papers"
          },
          {
            "title": "Process Reward Models for LLM Agents: Practical Framework and Directions",
            "url": "https://arxiv.org/html/2502.10325v1"
          },
          {
            "title": "GitHub - salesforce/CodeRL: This is the official code for the paper CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning (NeurIPS22). · GitHub",
            "url": "https://github.com/salesforce/CodeRL"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers on CodeRL and process reward models for code generation. Here's what I discovered:\n\n## CodeRL+: Recent Development (2025)\n\nCodeRL+, proposed in a recent arXiv paper, integrates execution semantics alignment into the RLVR (Reinforcement Learning with Verifiable Rewards) training pipeline for code generation. CodeRL+ enables the model to infer variable-level execution trajectory, providing a direct learning signal of execution semantics. Extensive experiments demonstrate that CodeRL+ outperforms post-training baselines (including RLVR and Distillation), achieving a 4.6% average relative improvement in pass@1.\n\n## Process Reward Models in Code Generation\n\nCodePRM (Li et al., 2025b) addresses the sparse reward problem through process reward models that provide dense feedback. The search results also reference recent work on process reward models more broadly.\n\n## Agent Process Reward Models (2025)\n\nAgent Process Reward Models (AgentPRM) is a simple and scalable framework for training LLM agents to continually improve through interactions, following a lightweight actor-critic paradigm using Monte Carlo rollouts to compute reward targets and optimize policies.\n\n## Historical Context\n\nEarly explorations such as CodeRL (Le et al., 2022) employ actor-critic frameworks to leverage unit test feedback for code generation.\n\nThe search revealed active research in combining reinforcement learning with code generation, with recent focus on improving reward signals through process-level feedback and execution semantics alignment."
    ],
    "durationSeconds": 7.004405180999998
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T19:50:16.871Z_

<details><summary>↩ Tool result · `toolu_01KnXwSXefeRKAaLs5LFY6wz`</summary>

```text
Web search results for query: "process supervision outcome supervision agent training reward model 2025 2026 arXiv"

Links: [{"title":"Process-Based Supervision in AI: Guiding Learning Step-by-Step | by Ursina Sanderink | Medium","url":"https://medium.com/@sanderink.ursina/process-based-supervision-in-ai-guiding-learning-step-by-step-ddad77b17cfc"},{"title":"[2510.08049] A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/abs/2510.08049"},{"title":"[2305.20050] Let's Verify Step by Step","url":"https://arxiv.org/abs/2305.20050"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Internalizing Outcome Supervision into Process Supervision: A New Paradigm for Reasoning Reinforcement Learning","url":"https://arxiv.org/html/2605.05226"},{"title":"Exploring Reasoning Reward Model for Agents","url":"https://arxiv.org/html/2601.22154v2"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Proceedings of the ACM Web Conference 2026","url":"https://dl.acm.org/doi/10.1145/3774904.3792551"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/pdf/2502.10325"},{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=h3LlJ6Bh4S"}]

Based on the web search results, here's what I found about process supervision, outcome supervision, agent training, and reward models from 2025-2026 arXiv papers:

## Recent Key Research Areas

**Process vs. Outcome Supervision:**
Research compares outcome supervision (which provides feedback for a final result) with process supervision (which provides feedback for each intermediate reasoning step), finding that process supervision significantly outperforms outcome supervision for training models to solve problems.

**Bi-directional Reward Models (BiRM):**
One issue with standard process reward models was that they looked only at the past. In 2025, researchers proposed BiRM (Bi-directional Reward Model), which evaluates not just the backward correctness of steps already taken, but also predicts the "distance" to the goal or the probability of future success from that point.

**Agent Process Reward Models:**
PRMs provide fine-grained supervision at each step. By evaluating intermediate actions rather than relying on sparse outcome rewards, PRMs improve sample efficiency. While PRMs have been explored in multi-step reasoning tasks, they are underexplored in agentic settings where actions impact an external environment.

**Survey on Process Reward Models:**
A comprehensive survey titled "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models" was published on arXiv with versions from October 2025 through April 2026.

**Recent Benchmarks and Applications:**
ToolComp: A Multi-Tool Reasoning & Process Supervision Benchmark (arXiv 2501.01290) provides a benchmark dataset with step-by-step annotations for multi-tool reasoning tasks, showing benefits of process supervision in complex tool-use scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "e87da8fe-5052-4ae8-8054-a3e5107548f6",
  "tool_use_result": {
    "query": "process supervision outcome supervision agent training reward model 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CgmSi3j3KY5RfX4gYHbRMT",
        "content": [
          {
            "title": "Process-Based Supervision in AI: Guiding Learning Step-by-Step | by Ursina Sanderink | Medium",
            "url": "https://medium.com/@sanderink.ursina/process-based-supervision-in-ai-guiding-learning-step-by-step-ddad77b17cfc"
          },
          {
            "title": "[2510.08049] A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/abs/2510.08049"
          },
          {
            "title": "[2305.20050] Let's Verify Step by Step",
            "url": "https://arxiv.org/abs/2305.20050"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "Internalizing Outcome Supervision into Process Supervision: A New Paradigm for Reasoning Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.05226"
          },
          {
            "title": "Exploring Reasoning Reward Model for Agents",
            "url": "https://arxiv.org/html/2601.22154v2"
          },
          {
            "title": "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Proceedings of the ACM Web Conference 2026",
            "url": "https://dl.acm.org/doi/10.1145/3774904.3792551"
          },
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          },
          {
            "title": "Process Reward Models for LLM Agents: Practical Framework and Directions",
            "url": "https://arxiv.org/pdf/2502.10325"
          },
          {
            "title": "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=h3LlJ6Bh4S"
          }
        ]
      },
      "Based on the web search results, here's what I found about process supervision, outcome supervision, agent training, and reward models from 2025-2026 arXiv papers:\n\n## Recent Key Research Areas\n\n**Process vs. Outcome Supervision:**\nResearch compares outcome supervision (which provides feedback for a final result) with process supervision (which provides feedback for each intermediate reasoning step), finding that process supervision significantly outperforms outcome supervision for training models to solve problems.\n\n**Bi-directional Reward Models (BiRM):**\nOne issue with standard process reward models was that they looked only at the past. In 2025, researchers proposed BiRM (Bi-directional Reward Model), which evaluates not just the backward correctness of steps already taken, but also predicts the \"distance\" to the goal or the probability of future success from that point.\n\n**Agent Process Reward Models:**\nPRMs provide fine-grained supervision at each step. By evaluating intermediate actions rather than relying on sparse outcome rewards, PRMs improve sample efficiency. While PRMs have been explored in multi-step reasoning tasks, they are underexplored in agentic settings where actions impact an external environment.\n\n**Survey on Process Reward Models:**\nA comprehensive survey titled \"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models\" was published on arXiv with versions from October 2025 through April 2026.\n\n**Recent Benchmarks and Applications:**\nToolComp: A Multi-Tool Reasoning & Process Supervision Benchmark (arXiv 2501.01290) provides a benchmark dataset with step-by-step annotations for multi-tool reasoning tasks, showing benefits of process supervision in complex tool-use scenarios."
    ],
    "durationSeconds": 7.756866381
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Good, I found several interesting candidates. Let me look more carefully at:

1. "Exploring Reasoning Reward Model for Agents" (2601.22154) - seems very relevant
2. "Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis" (2604.24198) - recent and relevant
3. The PRM survey (2510.08049) - comprehensive survey
4. "CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment" (2510.18471)

Let me fetch details on the most promising candidates.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "b8ce3fa3-a3f3-4f10-b694-f8b6ff13acf4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rei5e8bbsDkarqx2wdMk9u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3152,
      "cache_read_input_tokens": 32459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3152
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

Found several candidates. Let me verify the most promising ones.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "423cde83-4b19-4a58-9a78-f46297b93f14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rei5e8bbsDkarqx2wdMk9u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3152,
      "cache_read_input_tokens": 32459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3152
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Vdgu2z5pwzV2mot6me4H4U`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.22154",
  "prompt": "Extract the full title, all authors, year, arxiv ID, and the abstract. Return them clearly labeled."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "0ea43889-503e-4740-ac62-58e2b9e54378",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rei5e8bbsDkarqx2wdMk9u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3152,
      "cache_read_input_tokens": 32459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3152
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MwdUvjtYfrTrMBqvsjMtwp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.24198",
  "prompt": "Extract the full title, all authors, year, arxiv ID, and the abstract. Return them clearly labeled."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "99035432-2990-4083-b58c-f0364e5c405f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rei5e8bbsDkarqx2wdMk9u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3152,
      "cache_read_input_tokens": 32459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3152
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

_source line 21 · 2026-05-14T19:50:29.753Z_

<details><summary>↩ Tool result · `toolu_01MwdUvjtYfrTrMBqvsjMtwp`</summary>

```text
# Research Paper Details

**Full Title:**
"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis"

**Authors:**
Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen

**Year:**
2026

**arXiv ID:**
2604.24198

**Abstract:**
Process Reward Models have shown promise in enhancing LLM reasoning for mathematics, yet their effectiveness in dynamic data analysis remains under-investigated. This research identifies that conventional PRMs fail at detecting silent errors and misidentify exploratory steps. The authors propose DataPRM, an environment-aware generative model that actively probes execution states and employs a ternary reward strategy. Built on over 8K training instances, DataPRM achieves "7.21% improvement on ScienceAgentBench and 11.28% on DABStep" through Best-of-N inference, demonstrating robust generalization across scaling approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "47fcca31-e3b1-4d36-9c69-5e9478339a81",
  "tool_use_result": {
    "bytes": 49123,
    "code": 200,
    "codeText": "OK",
    "result": "# Research Paper Details\n\n**Full Title:**\n\"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis\"\n\n**Authors:**\nZhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen\n\n**Year:**\n2026\n\n**arXiv ID:**\n2604.24198\n\n**Abstract:**\nProcess Reward Models have shown promise in enhancing LLM reasoning for mathematics, yet their effectiveness in dynamic data analysis remains under-investigated. This research identifies that conventional PRMs fail at detecting silent errors and misidentify exploratory steps. The authors propose DataPRM, an environment-aware generative model that actively probes execution states and employs a ternary reward strategy. Built on over 8K training instances, DataPRM achieves \"7.21% improvement on ScienceAgentBench and 11.28% on DABStep\" through Best-of-N inference, demonstrating robust generalization across scaling approaches.",
    "durationMs": 4582,
    "url": "https://arxiv.org/abs/2604.24198"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T19:50:30.334Z_

<details><summary>↩ Tool result · `toolu_01Vdgu2z5pwzV2mot6me4H4U`</summary>

```text
# Paper Details

**Full Title:**
Exploring Reasoning Reward Model for Agents

**Authors:**
Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue

**Year:**
2026

**arXiv ID:**
2601.22154

**Abstract:**
The paper introduces Agent-RRM, a multi-faceted reward model generating structured feedback for agent trajectories through "an explicit reasoning trace, a focused critique that provides refinement guidance by highlighting reasoning flaws, and an overall score that evaluates process performance." The authors investigate three integration strategies—Reagent-C, Reagent-R, and Reagent-U—with Reagent-U demonstrating substantial improvements across 12 benchmarks, achieving 43.7% on GAIA and 46.2% on WebWalkerQA.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "5bf1bf0e-f78a-49e0-b864-f9bd96a2fa0c",
  "tool_use_result": {
    "bytes": 47104,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Details\n\n**Full Title:**\nExploring Reasoning Reward Model for Agents\n\n**Authors:**\nKaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue\n\n**Year:**\n2026\n\n**arXiv ID:**\n2601.22154\n\n**Abstract:**\nThe paper introduces Agent-RRM, a multi-faceted reward model generating structured feedback for agent trajectories through \"an explicit reasoning trace, a focused critique that provides refinement guidance by highlighting reasoning flaws, and an overall score that evaluates process performance.\" The authors investigate three integration strategies—Reagent-C, Reagent-R, and Reagent-U—with Reagent-U demonstrating substantial improvements across 12 benchmarks, achieving 43.7% on GAIA and 46.2% on WebWalkerQA.",
    "durationMs": 5388,
    "url": "https://arxiv.org/abs/2601.22154"
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Both papers look very relevant:

1. **Agent-RRM** (2601.22154, 2026) - A reasoning reward model for agents that provides structured feedback for agent trajectories including reasoning trace, critique, and overall score. This is relevant as it's about reward models for agents with process-level feedback.

2. **DataPRM** (2604.24198, 2026) - Process-level reward modeling for agentic data analysis. This is directly about PRMs for agents, identifying failures of conventional PRMs and proposing environment-aware approach.

Both are direct competitors to the project's work. Let me pick these two. They are:


- Not in the existing list
- Have arxiv IDs
- Are recent (2026)
- Are highly relevant to process reward models for agents

Now I need to add them to the YAML file. Looking at the structure, I should append after the `kale2025weaktostrong` entry at line 81 in the direct-competitor section.

Wait, let me reconsider the task instructions. It says to add them after `wang2026planrewardbench` in the direct-competitor section, but that's not the last entry—there are `chen2025monitoring` and `kale2025weaktostrong` after it. The instruction might mean to place them right after `wang2026planrewardbench`, between it and `chen2025monitoring`. Let me re-read the Chinese more carefully to clarify whether it means immediately after that entry or at the end of the section.

Actually, I think the safest interpretation is to add them at the true end of the direct-competitor section, after `kale2025weaktostrong`, since that's what "section 的末尾" literally means. The parenthetical about `wang2026planrewardbench` might just be an imprecise reference point.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "e39ccc13-bb08-436d-b08a-33b34668b6dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0117MeZw2Y2b9w7LNmGBF8SA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 273,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 35611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 730
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

_source line 24_

Both papers are highly relevant. Let me add them to the literature map after the last entry in the direct-competitor section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "0e067718-9f0f-4ea7-b46b-826d2fff2371",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0117MeZw2Y2b9w7LNmGBF8SA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 273,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 35611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 730
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

<details open><summary>🔧 Tool call — Edit · `toolu_01WpHxK2NApZquWjKYKXXLQJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
  "old_string": "    our_differentiation: \"他们用 LLM 作为 monitor，我们用 structural LFs + TLM，不依赖另一个 LLM；我们的方法更轻量且可解释\"\n\n  # ============================================================\n  # CATEGORY: method-component",
  "new_string": "    our_differentiation: \"他们用 LLM 作为 monitor，我们用 structural LFs + TLM，不依赖另一个 LLM；我们的方法更轻量且可解释\"\n\n  - id: \"fan2026agentrm\"\n    title: \"Exploring Reasoning Reward Model for Agents\"\n    authors: \"Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.22154\"\n    category: \"direct-competitor\"\n    verified: true\n    role: \"Agent trajectory 的多维度 reasoning reward model\"\n    key_finding: \"Agent-RRM 通过 reasoning trace + critique + overall score 三维结构化反馈评估 agent trajectory，在 12 个 benchmark 上显著提升（GAIA 43.7%, WebWalkerQA 46.2%）\"\n    our_differentiation: \"他们用 LLM-based reward model 生成结构化反馈用于 agent 改进，我们用轻量 programmatic LFs + TLM 做 stagnation detection，不依赖大模型推理\"\n\n  - id: \"qiu2026dataprm\"\n    title: \"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis\"\n    authors: \"Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.24198\"\n    category: \"direct-competitor\"\n    verified: true\n    role: \"Agentic data analysis 场景的 process-level reward model\"\n    key_finding: \"传统 PRM 无法检测 silent errors 且误判 exploratory steps；DataPRM 通过 environment-aware probing + ternary reward 策略在 ScienceAgentBench 提升 7.21%\"\n    our_differentiation: \"DataPRM 针对数据分析 agent 的 step correctness，我们针对通用 agent 的 stagnation pattern；他们需要 execution state probing，我们用 structural LFs 无需环境交互\"\n\n  # ============================================================\n  # CATEGORY: method-component"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "42bbdc55-1c45-4b6a-a25d-d6f2e618a5bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0117MeZw2Y2b9w7LNmGBF8SA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 273,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 35611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 730
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

_source line 26 · 2026-05-14T19:51:02.678Z_

<details><summary>↩ Tool result · `toolu_01WpHxK2NApZquWjKYKXXLQJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "6fcbf8d1-9a76-4c0b-80ae-954464fb8812",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
    "oldString": "    our_differentiation: \"他们用 LLM 作为 monitor，我们用 structural LFs + TLM，不依赖另一个 LLM；我们的方法更轻量且可解释\"\n\n  # ============================================================\n  # CATEGORY: method-component",
    "newString": "    our_differentiation: \"他们用 LLM 作为 monitor，我们用 structural LFs + TLM，不依赖另一个 LLM；我们的方法更轻量且可解释\"\n\n  - id: \"fan2026agentrm\"\n    title: \"Exploring Reasoning Reward Model for Agents\"\n    authors: \"Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.22154\"\n    category: \"direct-competitor\"\n    verified: true\n    role: \"Agent trajectory 的多维度 reasoning reward model\"\n    key_finding: \"Agent-RRM 通过 reasoning trace + critique + overall score 三维结构化反馈评估 agent trajectory，在 12 个 benchmark 上显著提升（GAIA 43.7%, WebWalkerQA 46.2%）\"\n    our_differentiation: \"他们用 LLM-based reward model 生成结构化反馈用于 agent 改进，我们用轻量 programmatic LFs + TLM 做 stagnation detection，不依赖大模型推理\"\n\n  - id: \"qiu2026dataprm\"\n    title: \"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis\"\n    authors: \"Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.24198\"\n    category: \"direct-competitor\"\n    verified: true\n    role: \"Agentic data analysis 场景的 process-level reward model\"\n    key_finding: \"传统 PRM 无法检测 silent errors 且误判 exploratory steps；DataPRM 通过 environment-aware probing + ternary reward 策略在 ScienceAgentBench 提升 7.21%\"\n    our_differentiation: \"DataPRM 针对数据分析 agent 的 step correctness，我们针对通用 agent 的 stagnation pattern；他们需要 execution state probing，我们用 structural LFs 无需环境交互\"\n\n  # ============================================================\n  # CATEGORY: method-component",
    "originalFile": "# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)\n# Generated: 2026-05-14\n# Paper: Temporal Label Model for Progress Stagnation Detection in LLM Agents\n#\n# Novelty check result: \"temporal label model\" as a general-purpose extension\n# of data programming to sequential data appears NOVEL. Closest works are\n# Safranchik AAAI 2020 (NER-specific linked HMM) and Sala NeurIPS 2019\n# (multi-resolution WS, not temporal transitions).\n\npapers:\n\n  # ============================================================\n  # CATEGORY: direct-competitor\n  # ============================================================\n\n  - id: \"xi2025agentprm\"\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Zhiheng Xi, Chenyang Liao, Guanyu Li, Yajie Yang, Wenxiang Chen, Zhihao Zhang, Binghai Wang, Senjie Jin, Yuhao Zhou, Jian Guan, Wei Wu, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2511.08325\"\n    category: \"direct-competitor\"\n    role: \"主要竞争者：step-level PRM for agent guidance\"\n    key_finding: \"用 promise（长期潜力）和 progress（即时进展）两个维度评估 agent 每步决策，实现 8x 计算效率提升\"\n    our_differentiation: \"我们是 window-level monitoring（不是 step-level guidance），不需要 outcome labels，目标是 stagnation detection 不是 reward shaping\"\n\n  - id: \"choudhury2025prm\"\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Sanjiban Choudhury\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2502.10325\"\n    category: \"direct-competitor\"\n    role: \"PRM 框架综述 + InversePRM 方法\"\n    key_finding: \"提出 AgentPRM（Monte Carlo rollout actor-critic）和 InversePRM（从 demonstrations 学习 process reward），3B 模型超越 GPT-4o\"\n    our_differentiation: \"InversePRM 仍需 demonstration trajectories，我们用 programmatic LFs 替代人工标注；我们关注 monitoring 而非 training signal\"\n\n  - id: \"li2026toolprmbench\"\n    title: \"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents\"\n    authors: \"Dawei Li, Yuguang Yao, Zhen Tan, Huan Liu, Ruocheng Guo\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.12294\"\n    category: \"direct-competitor\"\n    role: \"Tool-use PRM 评测基准\"\n    key_finding: \"大规模 benchmark 评测 PRM 在 tool-use 场景的效果，发现专用 PRM 显著优于通用 PRM\"\n    our_differentiation: \"我们的 TLM 是 unsupervised（不需要 step-level reward labels），且关注 stagnation pattern 而非 step correctness\"\n\n  - id: \"wang2026planrewardbench\"\n    title: \"Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling\"\n    authors: \"Jiaxuan Wang, Yulan Hu, Wenjin Yang, Zheng Pan, Xin Li, Lan-Zhe Guo\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.08178\"\n    category: \"direct-competitor\"\n    role: \"Trajectory-level reward model 评测\"\n    key_finding: \"所有 reward model 类别（generative, discriminative, LLM-as-Judge）在长 horizon trajectory 上性能显著下降\"\n    our_differentiation: \"验证了长 trajectory 评估的难度——我们的 window-level 方法通过局部化避免了这个问题\"\n\n  - id: \"chen2025monitoring\"\n    title: \"Monitoring LLM Agents for Sequentially Contextual Harm\"\n    authors: \"Yueh-Han Chen, Neelay Joshi, Yulin Chen, He He, Rico Angell\"\n    venue: \"ICLR 2025 Workshop on Building Trust in Language Models and Applications\"\n    year: 2025\n    arxiv: null\n    openreview: \"LC0XQ6ufbr\"\n    category: \"direct-competitor\"\n    role: \"Agent monitoring 安全方向\"\n    key_finding: \"将有害任务分解为单独无害的子任务可将 refusal rate 从 50% 降至 10%，现有 monitor 难以检测 sequentially contextual harm\"\n    our_differentiation: \"他们关注 safety monitoring（harmful behavior），我们关注 progress monitoring（stagnation）；互补方向\"\n\n  - id: \"kale2025weaktostrong\"\n    title: \"Reliable Weak-to-Strong Monitoring of LLM Agents\"\n    authors: \"Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team, Christina Q. Knight, Zifan Wang\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2508.19461\"\n    category: \"direct-competitor\"\n    role: \"Weak-to-strong agent monitoring 方法论\"\n    key_finding: \"Monitor scaffolding 比 monitor 能力更重要，弱模型可以可靠监控强模型；targeted human-in-the-loop 提升 TPR ~15%\"\n    our_differentiation: \"他们用 LLM 作为 monitor，我们用 structural LFs + TLM，不依赖另一个 LLM；我们的方法更轻量且可解释\"\n\n  # ============================================================\n  # CATEGORY: method-component\n  # ============================================================\n\n  - id: \"ratner2016dataprogramming\"\n    title: \"Data Programming: Creating Large Training Sets, Quickly\"\n    authors: \"Alexander Ratner, Christopher De Sa, Sen Wu, Daniel Selsam, Christopher Re\"\n    venue: \"NeurIPS 2016\"\n    year: 2016\n    arxiv: \"1605.07723\"\n    category: \"method-component\"\n    role: \"核心方法论基础：data programming 范式\"\n    key_finding: \"用户编写 labeling functions（噪声启发式），generative model 学习 LF 准确率生成概率训练标签\"\n    our_differentiation: \"我们扩展 data programming 到时序数据，加入 temporal transition structure\"\n\n  - id: \"ratner2017snorkel\"\n    title: \"Snorkel: Rapid Training Data Creation with Weak Supervision\"\n    authors: \"Alexander Ratner, Stephen H. Bach, Henry Ehrenberg, Jason Fries, Sen Wu, Christopher Re\"\n    venue: \"VLDB 2018\"\n    year: 2018\n    arxiv: \"1711.10160\"\n    category: \"method-component\"\n    role: \"Data programming 系统实现，label model 基础\"\n    key_finding: \"端到端弱监督系统：LFs → generative label model（建模 LF dependency）→ discriminative end model\"\n    our_differentiation: \"Snorkel 假设数据点 i.i.d.，我们的 TLM 显式建模相邻 window 间的 label transition\"\n\n  - id: \"fu2020flyingsquid\"\n    title: \"Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods\"\n    authors: \"Daniel Y. Fu, Mayee F. Chen, Frederic Sala, Sarah M. Hooper, Kayvon Fatahalian, Christopher Re\"\n    venue: \"ICML 2020\"\n    year: 2020\n    arxiv: \"2002.11955\"\n    category: \"method-component\"\n    role: \"快速 label model，triplet method of moments\"\n    key_finding: \"用 triplet method 闭式求解 label model 参数，比 SGD 快 170x\"\n    our_differentiation: \"FlyingSquid 同样假设 i.i.d.；我们的 TLM 需要不同的参数估计方法来处理时序依赖\"\n\n  - id: \"zhang2021wrench\"\n    title: \"WRENCH: A Comprehensive Benchmark for Weak Supervision\"\n    authors: \"Jieyu Zhang, Yue Yu, Yinghao Li, Yujing Wang, Yaming Yang, Mao Yang, Alexander Ratner\"\n    venue: \"NeurIPS 2021 Datasets and Benchmarks Track\"\n    year: 2021\n    arxiv: \"2109.11377\"\n    category: \"method-component\"\n    role: \"弱监督评测基准\"\n    key_finding: \"22 个真实数据集 + 120+ 方法变体评测，标准化弱监督研究\"\n    our_differentiation: \"WRENCH 数据集全是 i.i.d. 分类/序列标注，没有 temporal stagnation detection 任务\"\n\n  - id: \"safranchik2020linkedhmm\"\n    title: \"Weakly Supervised Sequence Tagging from Noisy Rules\"\n    authors: \"Esteban Safranchik, Shiying Luo, Stephen H. Bach\"\n    venue: \"AAAI 2020\"\n    year: 2020\n    arxiv: null\n    category: \"method-component\"\n    role: \"最近的方法论前驱：linked HMM for sequence tagging weak supervision\"\n    key_finding: \"将 HMM 引入弱监督序列标注（NER），加入 linking rules 建模 span 结构，比 i.i.d. label model +7 F1\"\n    our_differentiation: \"他们是 token-level NER（BIO 约束），我们是 window-level temporal classification；我们建模的是 stagnation temporal dynamics 而非 entity boundary\"\n\n  - id: \"sala2019multiresolution\"\n    title: \"Multi-Resolution Weak Supervision for Sequential Data\"\n    authors: \"Frederic Sala, Paroma Varma, Jason Fries, Daniel Y. Fu, Stefano Sagawa, Christopher Re\"\n    venue: \"NeurIPS 2019\"\n    year: 2019\n    arxiv: \"1910.09505\"\n    category: \"method-component\"\n    role: \"最近的方法论前驱：multi-resolution WS for sequential data\"\n    key_finding: \"处理不同时间分辨率的 LFs（如 frame-level vs span-level），建模 multi-resolution LF correlations\"\n    our_differentiation: \"他们关注 resolution mismatch，我们关注 temporal label transitions；互补视角\"\n\n  - id: \"dawid1979em\"\n    title: \"Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm\"\n    authors: \"A. P. Dawid, A. M. Skene\"\n    venue: \"Journal of the Royal Statistical Society, Series C\"\n    year: 1979\n    arxiv: null\n    category: \"method-component\"\n    role: \"Label aggregation 奠基工作\"\n    key_finding: \"用 EM 算法估计标注者混淆矩阵，无需 ground truth\"\n    our_differentiation: \"经典 i.i.d. 假设；我们的 TLM 可视为 temporal extension of Dawid-Skene for programmatic LFs\"\n\n  - id: \"nguyen2017hmmcrowd\"\n    title: \"Aggregating and Predicting Sequence Labels from Crowd Annotations\"\n    authors: \"An Thanh Nguyen, Byron C. Wallace, Junyi Jessy Li, Ani Nenkova, Matthew Lease\"\n    venue: \"ACL 2017\"\n    year: 2017\n    arxiv: null\n    category: \"method-component\"\n    role: \"HMM + crowdsourcing label aggregation\"\n    key_finding: \"HMM-Crowd：扩展 Dawid-Skene 到序列数据，加入 one-step Markov structure over true labels\"\n    our_differentiation: \"他们用于 crowdsourcing（人类标注者），我们用于 programmatic LFs（自动化）；他们是 NER/IE，我们是 agent progress monitoring\"\n\n  # ============================================================\n  # CATEGORY: evaluation\n  # ============================================================\n\n  - id: \"orlanski2026slopcodebench\"\n    title: \"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks\"\n    authors: \"Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu, Albert Ge, Dyah Adila, Nicholas Roberts, Frederic Sala, Aws Albarghouthi\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.24755\"\n    category: \"evaluation\"\n    role: \"Agent degradation 基准——直接支持我们的 problem motivation\"\n    key_finding: \"Agent 代码质量在迭代任务中持续退化：比人类代码 2.3x 更冗余、2.0x 更结构侵蚀，75-77% trajectory 呈现退化趋势\"\n    our_differentiation: \"SlopCodeBench 量化了 degradation 现象，我们提供了检测方法；他们是 post-hoc 评测，我们是 online monitoring\"\n\n  - id: \"jimenez2024swebench\"\n    title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n    authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2310.06770\"\n    category: \"evaluation\"\n    role: \"Agent 数据来源之一\"\n    key_finding: \"2294 个真实 GitHub issue 任务，标准化 agent 评测\"\n    our_differentiation: \"我们使用 SWE-bench agent trajectories 作为实验数据源之一\"\n\n  - id: \"yang2024sweagent\"\n    title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n    authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv: \"2405.15793\"\n    category: \"evaluation\"\n    role: \"Agent 系统——trajectory 数据来源\"\n    key_finding: \"提出 agent-computer interface (ACI)，GPT-4 Turbo 在 SWE-bench 达 12.47% resolve rate\"\n    our_differentiation: \"SWE-agent trajectories 是我们分析 stagnation 的数据来源之一\"\n\n  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================\n\n  - id: \"shinn2023reflexion\"\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    arxiv: \"2303.11366\"\n    category: \"background\"\n    role: \"Agent self-reflection 代表工作\"\n    key_finding: \"通过 verbal feedback 强化 agent，反思文本存入 episodic memory 用于后续 trial\"\n    our_differentiation: \"Reflexion 是 agent 自我改进机制，我们是外部 monitoring；self-reflection 可能失效时我们的 monitor 仍能检测 stagnation\"\n\n  - id: \"zhou2024lats\"\n    title: \"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\"\n    authors: \"Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang\"\n    venue: \"ICML 2024\"\n    year: 2024\n    arxiv: \"2310.04406\"\n    category: \"background\"\n    role: \"Agent planning + self-reflection\"\n    key_finding: \"结合 MCTS 与 LM value function 和 self-reflection，支持 backtracking\"\n    our_differentiation: \"LATS 通过搜索避免 stagnation，但计算开销大；我们的 monitor 可作为 LATS 的早期终止信号\"\n\n  - id: \"yao2023tot\"\n    title: \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\"\n    authors: \"Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    arxiv: \"2305.10601\"\n    category: \"background\"\n    role: \"Deliberate reasoning 框架\"\n    key_finding: \"将 CoT 泛化为树结构，LM 自我评估中间 thought 并 backtrack\"\n    our_differentiation: \"ToT 的自评估是 single-step 的；我们捕捉 multi-step temporal patterns\"\n\n  - id: \"cemri2025multiagentfail\"\n    title: \"Why Do Multi-Agent LLM Systems Fail?\"\n    authors: \"Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2503.13657\"\n    category: \"background\"\n    role: \"Agent failure taxonomy——problem motivation\"\n    key_finding: \"MAST taxonomy：14 种失败模式，其中 Step Repetition 被识别为具体失败症状\"\n    our_differentiation: \"他们提供 taxonomy（what fails），我们提供 detection method（how to detect）\"\n\n  - id: \"zhu2025agentfail\"\n    title: \"Where LLM Agents Fail and How They Can Learn From Failures\"\n    authors: \"Kunlun Zhu, Zijia Liu, Bingxuan Li, et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2509.25370\"\n    category: \"background\"\n    role: \"Agent failure 分析 + cascading failure 发现\"\n    key_finding: \"Cascading failures（单一 root cause 传播到后续决策）是长 horizon 任务的主要失败模式\"\n    our_differentiation: \"Cascading failure 正是我们 temporal model 可以捕捉的 pattern——stagnation 往往是 cascade 的表现\"\n\n  - id: \"george2025cycledetection\"\n    title: \"Unsupervised Cycle Detection in Agentic Applications\"\n    authors: \"Felix George, Harshit Kumar, Divya Pathak, Kaustabha Ray, Mudit Verma, Pratibha Moogi\"\n    venue: \"arXiv preprint (IBM Research)\"\n    year: 2025\n    arxiv: \"2511.10650\"\n    category: \"background\"\n    role: \"Cycle detection——最相关的 stagnation detection 前驱\"\n    key_finding: \"混合方法：call-stack 分析（结构重复）+ embedding 语义相似度确认\"\n    our_differentiation: \"他们只检测 exact/near-exact cycles，我们检测更广义的 stagnation（包括非重复性的停滞）；他们是 unsupervised rule-based，我们是 learned temporal model\"\n\n  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================\n\n  - id: \"cho2014gru\"\n    title: \"Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation\"\n    authors: \"Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio\"\n    venue: \"EMNLP 2014\"\n    year: 2014\n    arxiv: \"1406.1078\"\n    category: \"technique\"\n    role: \"GRU 原始论文——我们 probe model 的序列编码器\"\n    key_finding: \"提出 GRU hidden unit，自适应门控信息流\"\n\n  - id: \"bahdanau2015attention\"\n    title: \"Neural Machine Translation by Jointly Learning to Align and Translate\"\n    authors: \"Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio\"\n    venue: \"ICLR 2015\"\n    year: 2015\n    arxiv: \"1409.0473\"\n    category: \"technique\"\n    role: \"Attention mechanism——我们 probe model 的 attention 组件\"\n    key_finding: \"注意力机制允许 decoder 选择性关注输入序列不同位置\"\n\n  - id: \"khosla2020supcon\"\n    title: \"Supervised Contrastive Learning\"\n    authors: \"Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, Dilip Krishnan\"\n    venue: \"NeurIPS 2020\"\n    year: 2020\n    arxiv: \"2004.11362\"\n    category: \"technique\"\n    role: \"SupCon loss——我们的辅助训练目标\"\n    key_finding: \"扩展自监督对比学习到有监督设置，同类样本拉近、异类推远，提升鲁棒性\"\n\n  - id: \"zhang2025qwen3embedding\"\n    title: \"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models\"\n    authors: \"Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2506.05176\"\n    category: \"technique\"\n    role: \"Embedding model——我们用于生成 trajectory window embeddings\"\n    key_finding: \"基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA\"\n\n# ============================================================\n# NOVELTY ANALYSIS SUMMARY\n# ============================================================\n#\n# Key finding: \"Temporal Label Model\" 作为通用方法论是 NOVEL。\n#\n# 最近的前驱工作：\n# 1. Safranchik AAAI 2020 (linked HMM) — NER-specific，BIO 约束，token-level\n# 2. Sala NeurIPS 2019 (multi-resolution WS) — 处理分辨率不匹配，不建模 label transition\n# 3. Nguyen ACL 2017 (HMM-Crowd) — crowdsourcing 场景，不是 programmatic LFs\n#\n# 没有人将 data programming + HMM-style temporal transitions 用于：\n# - 通用序列分类（非 NER）\n# - Agent trajectory monitoring\n# - Stagnation detection\n#\n# 我们的 TLM 填补的空白：general-purpose temporal extension of\n# data programming label models for sequential classification tasks.\n",
    "structuredPatch": [
      {
        "oldStart": 80,
        "oldLines": 6,
        "newStart": 80,
        "newLines": 30,
        "lines": [
          "     key_finding: \"Monitor scaffolding 比 monitor 能力更重要，弱模型可以可靠监控强模型；targeted human-in-the-loop 提升 TPR ~15%\"",
          "     our_differentiation: \"他们用 LLM 作为 monitor，我们用 structural LFs + TLM，不依赖另一个 LLM；我们的方法更轻量且可解释\"",
          " ",
          "+  - id: \"fan2026agentrm\"",
          "+    title: \"Exploring Reasoning Reward Model for Agents\"",
          "+    authors: \"Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2026",
          "+    arxiv: \"2601.22154\"",
          "+    category: \"direct-competitor\"",
          "+    verified: true",
          "+    role: \"Agent trajectory 的多维度 reasoning reward model\"",
          "+    key_finding: \"Agent-RRM 通过 reasoning trace + critique + overall score 三维结构化反馈评估 agent trajectory，在 12 个 benchmark 上显著提升（GAIA 43.7%, WebWalkerQA 46.2%）\"",
          "+    our_differentiation: \"他们用 LLM-based reward model 生成结构化反馈用于 agent 改进，我们用轻量 programmatic LFs + TLM 做 stagnation detection，不依赖大模型推理\"",
          "+",
          "+  - id: \"qiu2026dataprm\"",
          "+    title: \"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis\"",
          "+    authors: \"Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2026",
          "+    arxiv: \"2604.24198\"",
          "+    category: \"direct-competitor\"",
          "+    verified: true",
          "+    role: \"Agentic data analysis 场景的 process-level reward model\"",
          "+    key_finding: \"传统 PRM 无法检测 silent errors 且误判 exploratory steps；DataPRM 通过 environment-aware probing + ternary reward 策略在 ScienceAgentBench 提升 7.21%\"",
          "+    our_differentiation: \"DataPRM 针对数据分析 agent 的 step correctness，我们针对通用 agent 的 stagnation pattern；他们需要 execution state probing，我们用 structural LFs 无需环境交互\"",
          "+",
          "   # ============================================================",
          "   # CATEGORY: method-component",
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

_source line 27_

添加了 2 篇论文：

1. **fan2026agentrm** — *Exploring Reasoning Reward Model for Agents* (2601.22154)：多维度 reasoning reward model，通过结构化反馈（reasoning trace + critique + score）评估 agent trajectory，12 个 benchmark 上验证。

2. **qiu2026dataprm** — *Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis* (2604.24198)：发现传统 PRM 无法检测 silent errors 且误判 exploratory steps，提出 environment-aware DataPRM + ternary reward 策略。

两篇均为 2026 年，有 arxiv ID，已标注 `verified: true`，已有条目未修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "uuid": "d58f36af-7a0a-49d9-bf73-2352cd22f1a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yQdZszFuPZaaajxhWWR7p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 36341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1899
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

_source line 28_

添加了 2 篇论文：

1. **fan2026agentrm** — *Exploring Reasoning Reward Model for Agents* (2601.22154)：多维度 reasoning reward model，通过结构化反馈（reasoning trace + critique + score）评估 agent trajectory，12 个 benchmark 上验证。

2. **qiu2026dataprm** — *Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis* (2604.24198)：发现传统 PRM 无法检测 silent errors 且误判 exploratory steps，提出 environment-aware DataPRM + ternary reward 策略。

两篇均为 2026 年，有 arxiv ID，已标注 `verified: true`，已有条目未修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 68592,
  "duration_api_ms": 88083,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "79e35447-8682-417b-a19b-40a09b0015c2",
  "total_cost_usd": 0.41076775,
  "usage": {
    "input_tokens": 280,
    "cache_creation_input_tokens": 26399,
    "cache_read_input_tokens": 139820,
    "output_tokens": 2530,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26399,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 209,
        "cache_read_input_tokens": 36341,
        "cache_creation_input_tokens": 1899,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1899
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 70774,
      "outputTokens": 2088,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 3,
      "costUSD": 0.111214,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 280,
      "outputTokens": 2530,
      "cacheReadInputTokens": 139820,
      "cacheCreationInputTokens": 26399,
      "webSearchRequests": 0,
      "costUSD": 0.29955374999999995,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "80ac5f4d-18d4-446e-b856-2606b6297105"
}
```

</details>

---
