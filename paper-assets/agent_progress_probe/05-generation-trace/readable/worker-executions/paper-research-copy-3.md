# paper research

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_paper_research_20260514T200749.log`
- **Structured JSON:** [`c08563b66380b87cb5f7.json`](../../sessions/c0/c08563b66380b87cb5f7.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe",
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
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
  "uuid": "7f41534b-505c-4dc2-b8b8-60244cef12d7",
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
  "uuid": "8c9543f6-ae85-4f5c-9377-34b460c2aafe",
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7"
}
```

---

### Assistant

_source line 4_

I'll search for relevant papers on agent self-correction/self-reflection limitations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "55879a2a-09e2-4757-ab06-613611484836",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRPw8zKr3fsK2nid7zutva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11669,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11669
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VWvE4D4H8ZnF7MXCP2uE1z`</summary>

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
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "9944abb8-2d1e-4ec0-9dc0-4b044020abe6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRPw8zKr3fsK2nid7zutva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11669,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11669
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

_source line 6 · 2026-05-14T20:08:00.660Z_

<details><summary>↩ Tool result · `toolu_01VWvE4D4H8ZnF7MXCP2uE1z`</summary>

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
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "1ed44d5e-1493-45fa-a2d5-cd2fb35de6b5",
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

<details open><summary>🔧 Tool call — Read · `toolu_01Ttb2G76mAN619EDR2ru1bt`</summary>

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
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "98cf891e-db8c-455f-a5a6-4a471a7babb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRPw8zKr3fsK2nid7zutva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11669,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11669
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

_source line 8 · 2026-05-14T20:08:01.036Z_

<details><summary>↩ Tool result · `toolu_01Ttb2G76mAN619EDR2ru1bt`</summary>

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
83	  - id: "fan2026agentrm"
84	    title: "Exploring Reasoning Reward Model for Agents"
85	    authors: "Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue"
86	    venue: "arXiv preprint"
87	    year: 2026
88	    arxiv: "2601.22154"
89	    category: "direct-competitor"
90	    verified: true
91	    role: "Agent trajectory 的多维度 reasoning reward model"
92	    key_finding: "Agent-RRM 通过 reasoning trace + critique + overall score 三维结构化反馈评估 agent trajectory，在 12 个 benchmark 上显著提升（GAIA 43.7%, WebWalkerQA 46.2%）"
93	    our_differentiation: "他们用 LLM-based reward model 生成结构化反馈用于 agent 改进，我们用轻量 programmatic LFs + TLM 做 stagnation detection，不依赖大模型推理"
94	
95	  - id: "qiu2026dataprm"
96	    title: "Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis"
97	    authors: "Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen"
98	    venue: "arXiv preprint"
99	    year: 2026
100	    arxiv: "2604.24198"
101	    category: "direct-competitor"
102	    verified: true
103	    role: "Agentic data analysis 场景的 process-level reward model"
104	    key_finding: "传统 PRM 无法检测 silent errors 且误判 exploratory steps；DataPRM 通过 environment-aware probing + ternary reward 策略在 ScienceAgentBench 提升 7.21%"
105	    our_differentiation: "DataPRM 针对数据分析 agent 的 step correctness，我们针对通用 agent 的 stagnation pattern；他们需要 execution state probing，我们用 structural LFs 无需环境交互"
106	
107	  # ============================================================
108	  # CATEGORY: method-component
109	  # ============================================================
110	
111	  - id: "ratner2016dataprogramming"
112	    title: "Data Programming: Creating Large Training Sets, Quickly"
113	    authors: "Alexander Ratner, Christopher De Sa, Sen Wu, Daniel Selsam, Christopher Re"
114	    venue: "NeurIPS 2016"
115	    year: 2016
116	    arxiv: "1605.07723"
117	    category: "method-component"
118	    role: "核心方法论基础：data programming 范式"
119	    key_finding: "用户编写 labeling functions（噪声启发式），generative model 学习 LF 准确率生成概率训练标签"
120	    our_differentiation: "我们扩展 data programming 到时序数据，加入 temporal transition structure"
121	
122	  - id: "ratner2017snorkel"
123	    title: "Snorkel: Rapid Training Data Creation with Weak Supervision"
124	    authors: "Alexander Ratner, Stephen H. Bach, Henry Ehrenberg, Jason Fries, Sen Wu, Christopher Re"
125	    venue: "VLDB 2018"
126	    year: 2018
127	    arxiv: "1711.10160"
128	    category: "method-component"
129	    role: "Data programming 系统实现，label model 基础"
130	    key_finding: "端到端弱监督系统：LFs → generative label model（建模 LF dependency）→ discriminative end model"
131	    our_differentiation: "Snorkel 假设数据点 i.i.d.，我们的 TLM 显式建模相邻 window 间的 label transition"
132	
133	  - id: "fu2020flyingsquid"
134	    title: "Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods"
135	    authors: "Daniel Y. Fu, Mayee F. Chen, Frederic Sala, Sarah M. Hooper, Kayvon Fatahalian, Christopher Re"
136	    venue: "ICML 2020"
137	    year: 2020
138	    arxiv: "2002.11955"
139	    category: "method-component"
140	    role: "快速 label model，triplet method of moments"
141	    key_finding: "用 triplet method 闭式求解 label model 参数，比 SGD 快 170x"
142	    our_differentiation: "FlyingSquid 同样假设 i.i.d.；我们的 TLM 需要不同的参数估计方法来处理时序依赖"
143	
144	  - id: "zhang2021wrench"
145	    title: "WRENCH: A Comprehensive Benchmark for Weak Supervision"
146	    authors: "Jieyu Zhang, Yue Yu, Yinghao Li, Yujing Wang, Yaming Yang, Mao Yang, Alexander Ratner"
147	    venue: "NeurIPS 2021 Datasets and Benchmarks Track"
148	    year: 2021
149	    arxiv: "2109.11377"
150	    category: "method-component"
151	    role: "弱监督评测基准"
152	    key_finding: "22 个真实数据集 + 120+ 方法变体评测，标准化弱监督研究"
153	    our_differentiation: "WRENCH 数据集全是 i.i.d. 分类/序列标注，没有 temporal stagnation detection 任务"
154	
155	  - id: "safranchik2020linkedhmm"
156	    title: "Weakly Supervised Sequence Tagging from Noisy Rules"
157	    authors: "Esteban Safranchik, Shiying Luo, Stephen H. Bach"
158	    venue: "AAAI 2020"
159	    year: 2020
160	    arxiv: null
161	    category: "method-component"
162	    role: "最近的方法论前驱：linked HMM for sequence tagging weak supervision"
163	    key_finding: "将 HMM 引入弱监督序列标注（NER），加入 linking rules 建模 span 结构，比 i.i.d. label model +7 F1"
164	    our_differentiation: "他们是 token-level NER（BIO 约束），我们是 window-level temporal classification；我们建模的是 stagnation temporal dynamics 而非 entity boundary"
165	
166	  - id: "sala2019multiresolution"
167	    title: "Multi-Resolution Weak Supervision for Sequential Data"
168	    authors: "Frederic Sala, Paroma Varma, Jason Fries, Daniel Y. Fu, Stefano Sagawa, Christopher Re"
169	    venue: "NeurIPS 2019"
170	    year: 2019
171	    arxiv: "1910.09505"
172	    category: "method-component"
173	    role: "最近的方法论前驱：multi-resolution WS for sequential data"
174	    key_finding: "处理不同时间分辨率的 LFs（如 frame-level vs span-level），建模 multi-resolution LF correlations"
175	    our_differentiation: "他们关注 resolution mismatch，我们关注 temporal label transitions；互补视角"
176	
177	  - id: "dawid1979em"
178	    title: "Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm"
179	    authors: "A. P. Dawid, A. M. Skene"
180	    venue: "Journal of the Royal Statistical Society, Series C"
181	    year: 1979
182	    arxiv: null
183	    category: "method-component"
184	    role: "Label aggregation 奠基工作"
185	    key_finding: "用 EM 算法估计标注者混淆矩阵，无需 ground truth"
186	    our_differentiation: "经典 i.i.d. 假设；我们的 TLM 可视为 temporal extension of Dawid-Skene for programmatic LFs"
187	
188	  - id: "nguyen2017hmmcrowd"
189	    title: "Aggregating and Predicting Sequence Labels from Crowd Annotations"
190	    authors: "An Thanh Nguyen, Byron C. Wallace, Junyi Jessy Li, Ani Nenkova, Matthew Lease"
191	    venue: "ACL 2017"
192	    year: 2017
193	    arxiv: null
194	    category: "method-component"
195	    role: "HMM + crowdsourcing label aggregation"
196	    key_finding: "HMM-Crowd：扩展 Dawid-Skene 到序列数据，加入 one-step Markov structure over true labels"
197	    our_differentiation: "他们用于 crowdsourcing（人类标注者），我们用于 programmatic LFs（自动化）；他们是 NER/IE，我们是 agent progress monitoring"
198	
199	  # ============================================================
200	  # CATEGORY: evaluation
201	  # ============================================================
202	
203	  - id: "orlanski2026slopcodebench"
204	    title: "SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks"
205	    authors: "Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu, Albert Ge, Dyah Adila, Nicholas Roberts, Frederic Sala, Aws Albarghouthi"
206	    venue: "arXiv preprint"
207	    year: 2026
208	    arxiv: "2603.24755"
209	    category: "evaluation"
210	    role: "Agent degradation 基准——直接支持我们的 problem motivation"
211	    key_finding: "Agent 代码质量在迭代任务中持续退化：比人类代码 2.3x 更冗余、2.0x 更结构侵蚀，75-77% trajectory 呈现退化趋势"
212	    our_differentiation: "SlopCodeBench 量化了 degradation 现象，我们提供了检测方法；他们是 post-hoc 评测，我们是 online monitoring"
213	
214	  - id: "jimenez2024swebench"
215	    title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
216	    authors: "Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan"
217	    venue: "ICLR 2024"
218	    year: 2024
219	    arxiv: "2310.06770"
220	    category: "evaluation"
221	    role: "Agent 数据来源之一"
222	    key_finding: "2294 个真实 GitHub issue 任务，标准化 agent 评测"
223	    our_differentiation: "我们使用 SWE-bench agent trajectories 作为实验数据源之一"
224	
225	  - id: "yang2024sweagent"
226	    title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
227	    authors: "John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press"
228	    venue: "NeurIPS 2024"
229	    year: 2024
230	    arxiv: "2405.15793"
231	    category: "evaluation"
232	    role: "Agent 系统——trajectory 数据来源"
233	    key_finding: "提出 agent-computer interface (ACI)，GPT-4 Turbo 在 SWE-bench 达 12.47% resolve rate"
234	    our_differentiation: "SWE-agent trajectories 是我们分析 stagnation 的数据来源之一"
235	
236	  - id: "wang2025openhands"
237	    title: "OpenHands: An Open Platform for AI Software Developers as Generalist Agents"
238	    authors: "Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al."
239	    venue: "ICLR 2025"
240	    year: 2025
241	    arxiv: "2407.16741"
242	    category: "evaluation"
243	    role: "Agent 平台——主要数据来源"
244	    key_finding: "开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测"
245	    our_differentiation: "OpenHands trajectories 是我们的主要实验数据来源"
246	
247	  # ============================================================
248	  # CATEGORY: background
249	  # ============================================================
250	
251	  - id: "shinn2023reflexion"
252	    title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
253	    authors: "Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao"
254	    venue: "NeurIPS 2023"
255	    year: 2023
256	    arxiv: "2303.11366"
257	    category: "background"
258	    role: "Agent self-reflection 代表工作"
259	    key_finding: "通过 verbal feedback 强化 agent，反思文本存入 episodic memory 用于后续 trial"
260	    our_differentiation: "Reflexion 是 agent 自我改进机制，我们是外部 monitoring；self-reflection 可能失效时我们的 monitor 仍能检测 stagnation"
261	
262	  - id: "zhou2024lats"
263	    title: "Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models"
264	    authors: "Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang"
265	    venue: "ICML 2024"
266	    year: 2024
267	    arxiv: "2310.04406"
268	    category: "background"
269	    role: "Agent planning + self-reflection"
270	    key_finding: "结合 MCTS 与 LM value function 和 self-reflection，支持 backtracking"
271	    our_differentiation: "LATS 通过搜索避免 stagnation，但计算开销大；我们的 monitor 可作为 LATS 的早期终止信号"
272	
273	  - id: "yao2023tot"
274	    title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
275	    authors: "Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan"
276	    venue: "NeurIPS 2023"
277	    year: 2023
278	    arxiv: "2305.10601"
279	    category: "background"
280	    role: "Deliberate reasoning 框架"
281	    key_finding: "将 CoT 泛化为树结构，LM 自我评估中间 thought 并 backtrack"
282	    our_differentiation: "ToT 的自评估是 single-step 的；我们捕捉 multi-step temporal patterns"
283	
284	  - id: "cemri2025multiagentfail"
285	    title: "Why Do Multi-Agent LLM Systems Fail?"
286	    authors: "Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, et al."
287	    venue: "arXiv preprint"
288	    year: 2025
289	    arxiv: "2503.13657"
290	    category: "background"
291	    role: "Agent failure taxonomy——problem motivation"
292	    key_finding: "MAST taxonomy：14 种失败模式，其中 Step Repetition 被识别为具体失败症状"
293	    our_differentiation: "他们提供 taxonomy（what fails），我们提供 detection method（how to detect）"
294	
295	  - id: "zhu2025agentfail"
296	    title: "Where LLM Agents Fail and How They Can Learn From Failures"
297	    authors: "Kunlun Zhu, Zijia Liu, Bingxuan Li, et al."
298	    venue: "arXiv preprint"
299	    year: 2025
300	    arxiv: "2509.25370"
301	    category: "background"
302	    role: "Agent failure 分析 + cascading failure 发现"
303	    key_finding: "Cascading failures（单一 root cause 传播到后续决策）是长 horizon 任务的主要失败模式"
304	    our_differentiation: "Cascading failure 正是我们 temporal model 可以捕捉的 pattern——stagnation 往往是 cascade 的表现"
305	
306	  - id: "george2025cycledetection"
307	    title: "Unsupervised Cycle Detection in Agentic Applications"
308	    authors: "Felix George, Harshit Kumar, Divya Pathak, Kaustabha Ray, Mudit Verma, Pratibha Moogi"
309	    venue: "arXiv preprint (IBM Research)"
310	    year: 2025
311	    arxiv: "2511.10650"
312	    category: "background"
313	    role: "Cycle detection——最相关的 stagnation detection 前驱"
314	    key_finding: "混合方法：call-stack 分析（结构重复）+ embedding 语义相似度确认"
315	    our_differentiation: "他们只检测 exact/near-exact cycles，我们检测更广义的 stagnation（包括非重复性的停滞）；他们是 unsupervised rule-based，我们是 learned temporal model"
316	
317	  - id: "pipis2025reasoningloop"
318	    title: "Wait, Wait, Wait... Why Do Reasoning Models Loop?"
319	    authors: "Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos"
320	    venue: "arXiv preprint"
321	    year: 2025
322	    arxiv: "2512.12895"
323	    category: "background"
324	    role: "Reasoning model looping 分析"
325	    key_finding: "Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测"
326	    our_differentiation: "他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一"
327	
328	  # ============================================================
329	  # CATEGORY: technique
330	  # ============================================================
331	
332	  - id: "cho2014gru"
333	    title: "Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation"
334	    authors: "Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio"
335	    venue: "EMNLP 2014"
336	    year: 2014
337	    arxiv: "1406.1078"
338	    category: "technique"
339	    role: "GRU 原始论文——我们 probe model 的序列编码器"
340	    key_finding: "提出 GRU hidden unit，自适应门控信息流"
341	
342	  - id: "bahdanau2015attention"
343	    title: "Neural Machine Translation by Jointly Learning to Align and Translate"
344	    authors: "Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio"
345	    venue: "ICLR 2015"
346	    year: 2015
347	    arxiv: "1409.0473"
348	    category: "technique"
349	    role: "Attention mechanism——我们 probe model 的 attention 组件"
350	    key_finding: "注意力机制允许 decoder 选择性关注输入序列不同位置"
351	
352	  - id: "khosla2020supcon"
353	    title: "Supervised Contrastive Learning"
354	    authors: "Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, Dilip Krishnan"
355	    venue: "NeurIPS 2020"
356	    year: 2020
357	    arxiv: "2004.11362"
358	    category: "technique"
359	    role: "SupCon loss——我们的辅助训练目标"
360	    key_finding: "扩展自监督对比学习到有监督设置，同类样本拉近、异类推远，提升鲁棒性"
361	
362	  - id: "zhang2025qwen3embedding"
363	    title: "Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models"
364	    authors: "Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou"
365	    venue: "arXiv preprint"
366	    year: 2025
367	    arxiv: "2506.05176"
368	    category: "technique"
369	    role: "Embedding model——我们用于生成 trajectory window embeddings"
370	    key_finding: "基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA"
371	
372	# ============================================================
373	# NOVELTY ANALYSIS SUMMARY
374	# ============================================================
375	#
376	# Key finding: "Temporal Label Model" 作为通用方法论是 NOVEL。
377	#
378	# 最近的前驱工作：
379	# 1. Safranchik AAAI 2020 (linked HMM) — NER-specific，BIO 约束，token-level
380	# 2. Sala NeurIPS 2019 (multi-resolution WS) — 处理分辨率不匹配，不建模 label transition
381	# 3. Nguyen ACL 2017 (HMM-Crowd) — crowdsourcing 场景，不是 programmatic LFs
382	#
383	# 没有人将 data programming + HMM-style temporal transitions 用于：
384	# - 通用序列分类（非 NER）
385	# - Agent trajectory monitoring
386	# - Stagnation detection
387	#
388	# 我们的 TLM 填补的空白：general-purpose temporal extension of
389	# data programming label models for sequential classification tasks.
390	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "bb407ee0-f107-48fb-994d-f91a945cf5e6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
      "content": "# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)\n# Generated: 2026-05-14\n# Paper: Temporal Label Model for Progress Stagnation Detection in LLM Agents\n#\n# Novelty check result: \"temporal label model\" as a general-purpose extension\n# of data programming to sequential data appears NOVEL. Closest works are\n# Safranchik AAAI 2020 (NER-specific linked HMM) and Sala NeurIPS 2019\n# (multi-resolution WS, not temporal transitions).\n\npapers:\n\n  # ============================================================\n  # CATEGORY: direct-competitor\n  # ============================================================\n\n  - id: \"xi2025agentprm\"\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Zhiheng Xi, Chenyang Liao, Guanyu Li, Yajie Yang, Wenxiang Chen, Zhihao Zhang, Binghai Wang, Senjie Jin, Yuhao Zhou, Jian Guan, Wei Wu, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2511.08325\"\n    category: \"direct-competitor\"\n    role: \"主要竞争者：step-level PRM for agent guidance\"\n    key_finding: \"用 promise（长期潜力）和 progress（即时进展）两个维度评估 agent 每步决策，实现 8x 计算效率提升\"\n    our_differentiation: \"我们是 window-level monitoring（不是 step-level guidance），不需要 outcome labels，目标是 stagnation detection 不是 reward shaping\"\n\n  - id: \"choudhury2025prm\"\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Sanjiban Choudhury\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2502.10325\"\n    category: \"direct-competitor\"\n    role: \"PRM 框架综述 + InversePRM 方法\"\n    key_finding: \"提出 AgentPRM（Monte Carlo rollout actor-critic）和 InversePRM（从 demonstrations 学习 process reward），3B 模型超越 GPT-4o\"\n    our_differentiation: \"InversePRM 仍需 demonstration trajectories，我们用 programmatic LFs 替代人工标注；我们关注 monitoring 而非 training signal\"\n\n  - id: \"li2026toolprmbench\"\n    title: \"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents\"\n    authors: \"Dawei Li, Yuguang Yao, Zhen Tan, Huan Liu, Ruocheng Guo\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.12294\"\n    category: \"direct-competitor\"\n    role: \"Tool-use PRM 评测基准\"\n    key_finding: \"大规模 benchmark 评测 PRM 在 tool-use 场景的效果，发现专用 PRM 显著优于通用 PRM\"\n    our_differentiation: \"我们的 TLM 是 unsupervised（不需要 step-level reward labels），且关注 stagnation pattern 而非 step correctness\"\n\n  - id: \"wang2026planrewardbench\"\n    title: \"Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling\"\n    authors: \"Jiaxuan Wang, Yulan Hu, Wenjin Yang, Zheng Pan, Xin Li, Lan-Zhe Guo\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.08178\"\n    category: \"direct-competitor\"\n    role: \"Trajectory-level reward model 评测\"\n    key_finding: \"所有 reward model 类别（generative, discriminative, LLM-as-Judge）在长 horizon trajectory 上性能显著下降\"\n    our_differentiation: \"验证了长 trajectory 评估的难度——我们的 window-level 方法通过局部化避免了这个问题\"\n\n  - id: \"chen2025monitoring\"\n    title: \"Monitoring LLM Agents for Sequentially Contextual Harm\"\n    authors: \"Yueh-Han Chen, Neelay Joshi, Yulin Chen, He He, Rico Angell\"\n    venue: \"ICLR 2025 Workshop on Building Trust in Language Models and Applications\"\n    year: 2025\n    arxiv: null\n    openreview: \"LC0XQ6ufbr\"\n    category: \"direct-competitor\"\n    role: \"Agent monitoring 安全方向\"\n    key_finding: \"将有害任务分解为单独无害的子任务可将 refusal rate 从 50% 降至 10%，现有 monitor 难以检测 sequentially contextual harm\"\n    our_differentiation: \"他们关注 safety monitoring（harmful behavior），我们关注 progress monitoring（stagnation）；互补方向\"\n\n  - id: \"kale2025weaktostrong\"\n    title: \"Reliable Weak-to-Strong Monitoring of LLM Agents\"\n    authors: \"Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team, Christina Q. Knight, Zifan Wang\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2508.19461\"\n    category: \"direct-competitor\"\n    role: \"Weak-to-strong agent monitoring 方法论\"\n    key_finding: \"Monitor scaffolding 比 monitor 能力更重要，弱模型可以可靠监控强模型；targeted human-in-the-loop 提升 TPR ~15%\"\n    our_differentiation: \"他们用 LLM 作为 monitor，我们用 structural LFs + TLM，不依赖另一个 LLM；我们的方法更轻量且可解释\"\n\n  - id: \"fan2026agentrm\"\n    title: \"Exploring Reasoning Reward Model for Agents\"\n    authors: \"Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.22154\"\n    category: \"direct-competitor\"\n    verified: true\n    role: \"Agent trajectory 的多维度 reasoning reward model\"\n    key_finding: \"Agent-RRM 通过 reasoning trace + critique + overall score 三维结构化反馈评估 agent trajectory，在 12 个 benchmark 上显著提升（GAIA 43.7%, WebWalkerQA 46.2%）\"\n    our_differentiation: \"他们用 LLM-based reward model 生成结构化反馈用于 agent 改进，我们用轻量 programmatic LFs + TLM 做 stagnation detection，不依赖大模型推理\"\n\n  - id: \"qiu2026dataprm\"\n    title: \"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis\"\n    authors: \"Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.24198\"\n    category: \"direct-competitor\"\n    verified: true\n    role: \"Agentic data analysis 场景的 process-level reward model\"\n    key_finding: \"传统 PRM 无法检测 silent errors 且误判 exploratory steps；DataPRM 通过 environment-aware probing + ternary reward 策略在 ScienceAgentBench 提升 7.21%\"\n    our_differentiation: \"DataPRM 针对数据分析 agent 的 step correctness，我们针对通用 agent 的 stagnation pattern；他们需要 execution state probing，我们用 structural LFs 无需环境交互\"\n\n  # ============================================================\n  # CATEGORY: method-component\n  # ============================================================\n\n  - id: \"ratner2016dataprogramming\"\n    title: \"Data Programming: Creating Large Training Sets, Quickly\"\n    authors: \"Alexander Ratner, Christopher De Sa, Sen Wu, Daniel Selsam, Christopher Re\"\n    venue: \"NeurIPS 2016\"\n    year: 2016\n    arxiv: \"1605.07723\"\n    category: \"method-component\"\n    role: \"核心方法论基础：data programming 范式\"\n    key_finding: \"用户编写 labeling functions（噪声启发式），generative model 学习 LF 准确率生成概率训练标签\"\n    our_differentiation: \"我们扩展 data programming 到时序数据，加入 temporal transition structure\"\n\n  - id: \"ratner2017snorkel\"\n    title: \"Snorkel: Rapid Training Data Creation with Weak Supervision\"\n    authors: \"Alexander Ratner, Stephen H. Bach, Henry Ehrenberg, Jason Fries, Sen Wu, Christopher Re\"\n    venue: \"VLDB 2018\"\n    year: 2018\n    arxiv: \"1711.10160\"\n    category: \"method-component\"\n    role: \"Data programming 系统实现，label model 基础\"\n    key_finding: \"端到端弱监督系统：LFs → generative label model（建模 LF dependency）→ discriminative end model\"\n    our_differentiation: \"Snorkel 假设数据点 i.i.d.，我们的 TLM 显式建模相邻 window 间的 label transition\"\n\n  - id: \"fu2020flyingsquid\"\n    title: \"Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods\"\n    authors: \"Daniel Y. Fu, Mayee F. Chen, Frederic Sala, Sarah M. Hooper, Kayvon Fatahalian, Christopher Re\"\n    venue: \"ICML 2020\"\n    year: 2020\n    arxiv: \"2002.11955\"\n    category: \"method-component\"\n    role: \"快速 label model，triplet method of moments\"\n    key_finding: \"用 triplet method 闭式求解 label model 参数，比 SGD 快 170x\"\n    our_differentiation: \"FlyingSquid 同样假设 i.i.d.；我们的 TLM 需要不同的参数估计方法来处理时序依赖\"\n\n  - id: \"zhang2021wrench\"\n    title: \"WRENCH: A Comprehensive Benchmark for Weak Supervision\"\n    authors: \"Jieyu Zhang, Yue Yu, Yinghao Li, Yujing Wang, Yaming Yang, Mao Yang, Alexander Ratner\"\n    venue: \"NeurIPS 2021 Datasets and Benchmarks Track\"\n    year: 2021\n    arxiv: \"2109.11377\"\n    category: \"method-component\"\n    role: \"弱监督评测基准\"\n    key_finding: \"22 个真实数据集 + 120+ 方法变体评测，标准化弱监督研究\"\n    our_differentiation: \"WRENCH 数据集全是 i.i.d. 分类/序列标注，没有 temporal stagnation detection 任务\"\n\n  - id: \"safranchik2020linkedhmm\"\n    title: \"Weakly Supervised Sequence Tagging from Noisy Rules\"\n    authors: \"Esteban Safranchik, Shiying Luo, Stephen H. Bach\"\n    venue: \"AAAI 2020\"\n    year: 2020\n    arxiv: null\n    category: \"method-component\"\n    role: \"最近的方法论前驱：linked HMM for sequence tagging weak supervision\"\n    key_finding: \"将 HMM 引入弱监督序列标注（NER），加入 linking rules 建模 span 结构，比 i.i.d. label model +7 F1\"\n    our_differentiation: \"他们是 token-level NER（BIO 约束），我们是 window-level temporal classification；我们建模的是 stagnation temporal dynamics 而非 entity boundary\"\n\n  - id: \"sala2019multiresolution\"\n    title: \"Multi-Resolution Weak Supervision for Sequential Data\"\n    authors: \"Frederic Sala, Paroma Varma, Jason Fries, Daniel Y. Fu, Stefano Sagawa, Christopher Re\"\n    venue: \"NeurIPS 2019\"\n    year: 2019\n    arxiv: \"1910.09505\"\n    category: \"method-component\"\n    role: \"最近的方法论前驱：multi-resolution WS for sequential data\"\n    key_finding: \"处理不同时间分辨率的 LFs（如 frame-level vs span-level），建模 multi-resolution LF correlations\"\n    our_differentiation: \"他们关注 resolution mismatch，我们关注 temporal label transitions；互补视角\"\n\n  - id: \"dawid1979em\"\n    title: \"Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm\"\n    authors: \"A. P. Dawid, A. M. Skene\"\n    venue: \"Journal of the Royal Statistical Society, Series C\"\n    year: 1979\n    arxiv: null\n    category: \"method-component\"\n    role: \"Label aggregation 奠基工作\"\n    key_finding: \"用 EM 算法估计标注者混淆矩阵，无需 ground truth\"\n    our_differentiation: \"经典 i.i.d. 假设；我们的 TLM 可视为 temporal extension of Dawid-Skene for programmatic LFs\"\n\n  - id: \"nguyen2017hmmcrowd\"\n    title: \"Aggregating and Predicting Sequence Labels from Crowd Annotations\"\n    authors: \"An Thanh Nguyen, Byron C. Wallace, Junyi Jessy Li, Ani Nenkova, Matthew Lease\"\n    venue: \"ACL 2017\"\n    year: 2017\n    arxiv: null\n    category: \"method-component\"\n    role: \"HMM + crowdsourcing label aggregation\"\n    key_finding: \"HMM-Crowd：扩展 Dawid-Skene 到序列数据，加入 one-step Markov structure over true labels\"\n    our_differentiation: \"他们用于 crowdsourcing（人类标注者），我们用于 programmatic LFs（自动化）；他们是 NER/IE，我们是 agent progress monitoring\"\n\n  # ============================================================\n  # CATEGORY: evaluation\n  # ============================================================\n\n  - id: \"orlanski2026slopcodebench\"\n    title: \"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks\"\n    authors: \"Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu, Albert Ge, Dyah Adila, Nicholas Roberts, Frederic Sala, Aws Albarghouthi\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.24755\"\n    category: \"evaluation\"\n    role: \"Agent degradation 基准——直接支持我们的 problem motivation\"\n    key_finding: \"Agent 代码质量在迭代任务中持续退化：比人类代码 2.3x 更冗余、2.0x 更结构侵蚀，75-77% trajectory 呈现退化趋势\"\n    our_differentiation: \"SlopCodeBench 量化了 degradation 现象，我们提供了检测方法；他们是 post-hoc 评测，我们是 online monitoring\"\n\n  - id: \"jimenez2024swebench\"\n    title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n    authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2310.06770\"\n    category: \"evaluation\"\n    role: \"Agent 数据来源之一\"\n    key_finding: \"2294 个真实 GitHub issue 任务，标准化 agent 评测\"\n    our_differentiation: \"我们使用 SWE-bench agent trajectories 作为实验数据源之一\"\n\n  - id: \"yang2024sweagent\"\n    title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n    authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv: \"2405.15793\"\n    category: \"evaluation\"\n    role: \"Agent 系统——trajectory 数据来源\"\n    key_finding: \"提出 agent-computer interface (ACI)，GPT-4 Turbo 在 SWE-bench 达 12.47% resolve rate\"\n    our_differentiation: \"SWE-agent trajectories 是我们分析 stagnation 的数据来源之一\"\n\n  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================\n\n  - id: \"shinn2023reflexion\"\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    arxiv: \"2303.11366\"\n    category: \"background\"\n    role: \"Agent self-reflection 代表工作\"\n    key_finding: \"通过 verbal feedback 强化 agent，反思文本存入 episodic memory 用于后续 trial\"\n    our_differentiation: \"Reflexion 是 agent 自我改进机制，我们是外部 monitoring；self-reflection 可能失效时我们的 monitor 仍能检测 stagnation\"\n\n  - id: \"zhou2024lats\"\n    title: \"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\"\n    authors: \"Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang\"\n    venue: \"ICML 2024\"\n    year: 2024\n    arxiv: \"2310.04406\"\n    category: \"background\"\n    role: \"Agent planning + self-reflection\"\n    key_finding: \"结合 MCTS 与 LM value function 和 self-reflection，支持 backtracking\"\n    our_differentiation: \"LATS 通过搜索避免 stagnation，但计算开销大；我们的 monitor 可作为 LATS 的早期终止信号\"\n\n  - id: \"yao2023tot\"\n    title: \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\"\n    authors: \"Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    arxiv: \"2305.10601\"\n    category: \"background\"\n    role: \"Deliberate reasoning 框架\"\n    key_finding: \"将 CoT 泛化为树结构，LM 自我评估中间 thought 并 backtrack\"\n    our_differentiation: \"ToT 的自评估是 single-step 的；我们捕捉 multi-step temporal patterns\"\n\n  - id: \"cemri2025multiagentfail\"\n    title: \"Why Do Multi-Agent LLM Systems Fail?\"\n    authors: \"Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2503.13657\"\n    category: \"background\"\n    role: \"Agent failure taxonomy——problem motivation\"\n    key_finding: \"MAST taxonomy：14 种失败模式，其中 Step Repetition 被识别为具体失败症状\"\n    our_differentiation: \"他们提供 taxonomy（what fails），我们提供 detection method（how to detect）\"\n\n  - id: \"zhu2025agentfail\"\n    title: \"Where LLM Agents Fail and How They Can Learn From Failures\"\n    authors: \"Kunlun Zhu, Zijia Liu, Bingxuan Li, et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2509.25370\"\n    category: \"background\"\n    role: \"Agent failure 分析 + cascading failure 发现\"\n    key_finding: \"Cascading failures（单一 root cause 传播到后续决策）是长 horizon 任务的主要失败模式\"\n    our_differentiation: \"Cascading failure 正是我们 temporal model 可以捕捉的 pattern——stagnation 往往是 cascade 的表现\"\n\n  - id: \"george2025cycledetection\"\n    title: \"Unsupervised Cycle Detection in Agentic Applications\"\n    authors: \"Felix George, Harshit Kumar, Divya Pathak, Kaustabha Ray, Mudit Verma, Pratibha Moogi\"\n    venue: \"arXiv preprint (IBM Research)\"\n    year: 2025\n    arxiv: \"2511.10650\"\n    category: \"background\"\n    role: \"Cycle detection——最相关的 stagnation detection 前驱\"\n    key_finding: \"混合方法：call-stack 分析（结构重复）+ embedding 语义相似度确认\"\n    our_differentiation: \"他们只检测 exact/near-exact cycles，我们检测更广义的 stagnation（包括非重复性的停滞）；他们是 unsupervised rule-based，我们是 learned temporal model\"\n\n  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================\n\n  - id: \"cho2014gru\"\n    title: \"Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation\"\n    authors: \"Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio\"\n    venue: \"EMNLP 2014\"\n    year: 2014\n    arxiv: \"1406.1078\"\n    category: \"technique\"\n    role: \"GRU 原始论文——我们 probe model 的序列编码器\"\n    key_finding: \"提出 GRU hidden unit，自适应门控信息流\"\n\n  - id: \"bahdanau2015attention\"\n    title: \"Neural Machine Translation by Jointly Learning to Align and Translate\"\n    authors: \"Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio\"\n    venue: \"ICLR 2015\"\n    year: 2015\n    arxiv: \"1409.0473\"\n    category: \"technique\"\n    role: \"Attention mechanism——我们 probe model 的 attention 组件\"\n    key_finding: \"注意力机制允许 decoder 选择性关注输入序列不同位置\"\n\n  - id: \"khosla2020supcon\"\n    title: \"Supervised Contrastive Learning\"\n    authors: \"Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, Dilip Krishnan\"\n    venue: \"NeurIPS 2020\"\n    year: 2020\n    arxiv: \"2004.11362\"\n    category: \"technique\"\n    role: \"SupCon loss——我们的辅助训练目标\"\n    key_finding: \"扩展自监督对比学习到有监督设置，同类样本拉近、异类推远，提升鲁棒性\"\n\n  - id: \"zhang2025qwen3embedding\"\n    title: \"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models\"\n    authors: \"Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2506.05176\"\n    category: \"technique\"\n    role: \"Embedding model——我们用于生成 trajectory window embeddings\"\n    key_finding: \"基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA\"\n\n# ============================================================\n# NOVELTY ANALYSIS SUMMARY\n# ============================================================\n#\n# Key finding: \"Temporal Label Model\" 作为通用方法论是 NOVEL。\n#\n# 最近的前驱工作：\n# 1. Safranchik AAAI 2020 (linked HMM) — NER-specific，BIO 约束，token-level\n# 2. Sala NeurIPS 2019 (multi-resolution WS) — 处理分辨率不匹配，不建模 label transition\n# 3. Nguyen ACL 2017 (HMM-Crowd) — crowdsourcing 场景，不是 programmatic LFs\n#\n# 没有人将 data programming + HMM-style temporal transitions 用于：\n# - 通用序列分类（非 NER）\n# - Agent trajectory monitoring\n# - Stagnation detection\n#\n# 我们的 TLM 填补的空白：general-purpose temporal extension of\n# data programming label models for sequential classification tasks.\n",
      "numLines": 390,
      "startLine": 1,
      "totalLines": 390
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
Now I have the literature map and the WebSearch/WebFetch tools loaded. Let me search for relevant papers on agent self-correction limitations and self-reflection failures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "aa6f55e1-0dba-4893-a536-87ae566089ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgwQd4ZJeY9FNVP6ECaf4N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9528,
      "cache_read_input_tokens": 23510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9528
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

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vgj2Jj4w32XL4rZvpwqBws`</summary>

```json
{
  "query": "LLM agent self-correction limitations failure 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "a7bf0578-3410-4944-9f82-d3a88e948b5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgwQd4ZJeY9FNVP6ECaf4N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9528,
      "cache_read_input_tokens": 23510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9528
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BqquPNaebWyvhD3v47DMMg`</summary>

```json
{
  "query": "\"self-reflection\" LLM agent fails limitations external verification 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "d3e0527c-0282-4da2-9b00-7ed92d9aae57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgwQd4ZJeY9FNVP6ECaf4N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9528,
      "cache_read_input_tokens": 23510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9528
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

_source line 12 · 2026-05-14T20:08:13.117Z_

<details><summary>↩ Tool result · `toolu_01BqquPNaebWyvhD3v47DMMg`</summary>

```text
Web search results for query: ""self-reflection" LLM agent fails limitations external verification 2024 2025"

Links: [{"title":"Large Language Models Cannot Self-Correct Reasoning Yet | OpenReview","url":"https://openreview.net/forum?id=IkmD3fKBPQ"},{"title":"Self-Reflection in LLM Agents: Effects on Problem-Solving Performance","url":"https://arxiv.org/pdf/2405.06682"},{"title":"[2310.01798] Large Language Models Cannot Self-Correct Reasoning Yet","url":"https://arxiv.org/abs/2310.01798"},{"title":"Reflect, Retry, Reward: Self-Improving LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2505.24726v1"},{"title":"Better Ways to Build Self-Improving AI Agents – Yohei Nakajima","url":"https://yoheinakajima.com/better-ways-to-build-self-improving-ai-agents/"},{"title":"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs","url":"https://arxiv.org/html/2510.16062v1"},{"title":"Self-reflection enhances large language models towards substantial academic response | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-025-00045-3"},{"title":"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs","url":"https://arxiv.org/html/2512.20845"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"Large Language Models Can Self-Correct with Key Condition Verification - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.714/"}]

I've found substantial research on this topic. Here are the key findings:

## LLM Self-Reflection Limitations and the Need for External Verification

### Core Finding: Self-Correction Without External Feedback Fails

LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction. This has been well-documented in recent research from 2023-2025.

### Specific Limitations Identified

Recent work has shown that the effectiveness of self-reflection depends strongly on context, with challenges including the inability to reliably identify self-errors without ground-truth oracles, diminishing returns from repeated reflection, and risks of performance deterioration for easier prompts or high-performing base models.

Additionally, LLMs cannot reliably correct their own reasoning without external feedback, and self-correction can flip correct answers to incorrect ones.

### Single-Agent Reflexion Problems

Research on the Reflexion framework revealed critical issues: the single agent design of Reflexion leads to systematic shortcomings, where the same model generates actions, evaluates its own behavior, and produces reflections, which often results in repeated reasoning errors, confirmation bias, and limited corrective feedback.

### When External Verification Works

Self-reflection is most effective when initial accuracy is low, question difficulty is high, and external verification is available. Furthermore, external correction methods generally achieve higher average gains than intrinsic methods.

The research clearly demonstrates that while self-reflection can be useful in specific contexts, successful LLM agents require external verification mechanisms rather than relying solely on internal self-assessment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "dadfad10-bf37-4c9d-a7e3-fb82e1a473fc",
  "tool_use_result": {
    "query": "\"self-reflection\" LLM agent fails limitations external verification 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QPSSGSHJfpqzEHF54EhVE7",
        "content": [
          {
            "title": "Large Language Models Cannot Self-Correct Reasoning Yet | OpenReview",
            "url": "https://openreview.net/forum?id=IkmD3fKBPQ"
          },
          {
            "title": "Self-Reflection in LLM Agents: Effects on Problem-Solving Performance",
            "url": "https://arxiv.org/pdf/2405.06682"
          },
          {
            "title": "[2310.01798] Large Language Models Cannot Self-Correct Reasoning Yet",
            "url": "https://arxiv.org/abs/2310.01798"
          },
          {
            "title": "Reflect, Retry, Reward: Self-Improving LLMs via Reinforcement Learning",
            "url": "https://arxiv.org/html/2505.24726v1"
          },
          {
            "title": "Better Ways to Build Self-Improving AI Agents – Yohei Nakajima",
            "url": "https://yoheinakajima.com/better-ways-to-build-self-improving-ai-agents/"
          },
          {
            "title": "Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs",
            "url": "https://arxiv.org/html/2510.16062v1"
          },
          {
            "title": "Self-reflection enhances large language models towards substantial academic response | npj Artificial Intelligence",
            "url": "https://www.nature.com/articles/s44387-025-00045-3"
          },
          {
            "title": "MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs",
            "url": "https://arxiv.org/html/2512.20845"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"
          },
          {
            "title": "Large Language Models Can Self-Correct with Key Condition Verification - ACL Anthology",
            "url": "https://aclanthology.org/2024.emnlp-main.714/"
          }
        ]
      },
      "I've found substantial research on this topic. Here are the key findings:\n\n## LLM Self-Reflection Limitations and the Need for External Verification\n\n### Core Finding: Self-Correction Without External Feedback Fails\n\nLLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction. This has been well-documented in recent research from 2023-2025.\n\n### Specific Limitations Identified\n\nRecent work has shown that the effectiveness of self-reflection depends strongly on context, with challenges including the inability to reliably identify self-errors without ground-truth oracles, diminishing returns from repeated reflection, and risks of performance deterioration for easier prompts or high-performing base models.\n\nAdditionally, LLMs cannot reliably correct their own reasoning without external feedback, and self-correction can flip correct answers to incorrect ones.\n\n### Single-Agent Reflexion Problems\n\nResearch on the Reflexion framework revealed critical issues: the single agent design of Reflexion leads to systematic shortcomings, where the same model generates actions, evaluates its own behavior, and produces reflections, which often results in repeated reasoning errors, confirmation bias, and limited corrective feedback.\n\n### When External Verification Works\n\nSelf-reflection is most effective when initial accuracy is low, question difficulty is high, and external verification is available. Furthermore, external correction methods generally achieve higher average gains than intrinsic methods.\n\nThe research clearly demonstrates that while self-reflection can be useful in specific contexts, successful LLM agents require external verification mechanisms rather than relying solely on internal self-assessment."
    ],
    "durationSeconds": 7.632786207999998
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T20:08:14.931Z_

<details><summary>↩ Tool result · `toolu_01Vgj2Jj4w32XL4rZvpwqBws`</summary>

```text
Web search results for query: "LLM agent self-correction limitations failure 2024 2025"

Links: [{"title":"Large Language Models Cannot Self-Correct Reasoning Yet | OpenReview","url":"https://openreview.net/forum?id=IkmD3fKBPQ"},{"title":"[2310.01798] Large Language Models Cannot Self-Correct Reasoning Yet","url":"https://arxiv.org/abs/2310.01798"},{"title":"Limits of Self-Correction in LLMs: An Information-Theoretic Analysis of Correlated Errors[v2] | Preprints.org","url":"https://www.preprints.org/manuscript/202601.0892"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes"},{"title":"Experience-based Knowledge Correction for Robust Planning in Minecraft","url":"https://arxiv.org/html/2505.24157v2"},{"title":"Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=7K1kXowjK1"},{"title":"Large Language Models Can Self-Correct with Key Condition Verification - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.714/"},{"title":"NeurIPS Poster Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs","url":"https://neurips.cc/virtual/2025/poster/121806"},{"title":"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs","url":"https://arxiv.org/html/2510.16062v1"},{"title":"WHERE LLM AGENTS FAIL AND HOW THEY CAN LEARN FROM FAILURES","url":"https://arxiv.org/pdf/2509.25370"}]

Based on the search results, here's a comprehensive overview of LLM agent self-correction limitations and failures from recent research (2024-2025):

## Key Limitations and Failures

### Intrinsic Self-Correction Challenges

LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction. There is still no consensus on the question of when LLMs can correct their own mistakes, as recent studies report negative results.

### Correlated Error Problem

When both generator and evaluator components share failure modes, self-evaluation may provide weak evidence of correctness, and repeated self-critique may amplify confidence without adding information.

### Self-Correction Blind Spot

Recent research has identified a significant limitation: LLMs can correct errors by fixing external ones but fail to activate this capability for identical internal errors—a limitation termed the Self-Correction Blind Spot. However, appending a simple "Wait" prompt cuts blind spots by 89.3%, revealing latent capabilities.

### Agents and Planning Knowledge

In complex planning tasks, LLMs cannot robustly correct their flawed knowledge, even when prompted to self-correct with failure feedback, often repeating the same errors. For complex tasks like planning, LLMs struggle to identify and correct their own errors without external feedback.

### Error Propagation in Agent Trajectories

Error propagation is identified as the central bottleneck to building robust LLM agents, with agents frequently exhibiting errors ranging from misinterpreting instructions and misusing tools to breaking down in long-horizon reasoning.

## Conditions for Success

Despite these limitations, self-correction methods can improve accuracy, especially for complex reasoning tasks, and a simple yet effective prompting method enhances LLM performance in identifying and correcting inaccurate answers without external feedback by masking a key condition in the question, adding the current response to construct a verification question, and predicting the condition to verify the response.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "d7893082-f06e-4525-b461-d24cd3d30dc4",
  "tool_use_result": {
    "query": "LLM agent self-correction limitations failure 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_013XUn6gPAbXftr75jvtyZNa",
        "content": [
          {
            "title": "Large Language Models Cannot Self-Correct Reasoning Yet | OpenReview",
            "url": "https://openreview.net/forum?id=IkmD3fKBPQ"
          },
          {
            "title": "[2310.01798] Large Language Models Cannot Self-Correct Reasoning Yet",
            "url": "https://arxiv.org/abs/2310.01798"
          },
          {
            "title": "Limits of Self-Correction in LLMs: An Information-Theoretic Analysis of Correlated Errors[v2] | Preprints.org",
            "url": "https://www.preprints.org/manuscript/202601.0892"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes"
          },
          {
            "title": "Experience-based Knowledge Correction for Robust Planning in Minecraft",
            "url": "https://arxiv.org/html/2505.24157v2"
          },
          {
            "title": "Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=7K1kXowjK1"
          },
          {
            "title": "Large Language Models Can Self-Correct with Key Condition Verification - ACL Anthology",
            "url": "https://aclanthology.org/2024.emnlp-main.714/"
          },
          {
            "title": "NeurIPS Poster Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs",
            "url": "https://neurips.cc/virtual/2025/poster/121806"
          },
          {
            "title": "Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs",
            "url": "https://arxiv.org/html/2510.16062v1"
          },
          {
            "title": "WHERE LLM AGENTS FAIL AND HOW THEY CAN LEARN FROM FAILURES",
            "url": "https://arxiv.org/pdf/2509.25370"
          }
        ]
      },
      "Based on the search results, here's a comprehensive overview of LLM agent self-correction limitations and failures from recent research (2024-2025):\n\n## Key Limitations and Failures\n\n### Intrinsic Self-Correction Challenges\n\nLLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction. There is still no consensus on the question of when LLMs can correct their own mistakes, as recent studies report negative results.\n\n### Correlated Error Problem\n\nWhen both generator and evaluator components share failure modes, self-evaluation may provide weak evidence of correctness, and repeated self-critique may amplify confidence without adding information.\n\n### Self-Correction Blind Spot\n\nRecent research has identified a significant limitation: LLMs can correct errors by fixing external ones but fail to activate this capability for identical internal errors—a limitation termed the Self-Correction Blind Spot. However, appending a simple \"Wait\" prompt cuts blind spots by 89.3%, revealing latent capabilities.\n\n### Agents and Planning Knowledge\n\nIn complex planning tasks, LLMs cannot robustly correct their flawed knowledge, even when prompted to self-correct with failure feedback, often repeating the same errors. For complex tasks like planning, LLMs struggle to identify and correct their own errors without external feedback.\n\n### Error Propagation in Agent Trajectories\n\nError propagation is identified as the central bottleneck to building robust LLM agents, with agents frequently exhibiting errors ranging from misinterpreting instructions and misusing tools to breaking down in long-horizon reasoning.\n\n## Conditions for Success\n\nDespite these limitations, self-correction methods can improve accuracy, especially for complex reasoning tasks, and a simple yet effective prompting method enhances LLM performance in identifying and correcting inaccurate answers without external feedback by masking a key condition in the question, adding the current response to construct a verification question, and predicting the condition to verify the response."
    ],
    "durationSeconds": 9.909879245000003
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Good results. Two strong candidates:

1. **Huang et al. 2024 "Large Language Models Cannot Self-Correct Reasoning Yet"** (arxiv 2310.01798) - ICLR 2024. This is the seminal paper showing LLMs can't self-correct without external feedback.

2. **"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs"** (TACL) - This is a survey paper. Let me get the arxiv ID.


3. **"Self-Reflection in LLM Agents: Effects on Problem-Solving Performance"** (arxiv 2405.06682) - This looks directly relevant too. Now I'm pulling together the details on these top candidates to verify the arxiv IDs and publication info.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "fbc37f63-82cf-4ef0-9263-f0373086b954",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApLYN4uFrq9Aokpi36gEji",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 912,
      "cache_creation_input_tokens": 1198,
      "cache_read_input_tokens": 33038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1198
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_0151q5eUUH4dDmMQq4Gmw3sr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2310.01798",
  "prompt": "Extract: title, authors, venue/conference, year, arxiv ID, key findings about self-correction limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "85b03e73-2dbb-479e-9c41-92c3ce981c30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApLYN4uFrq9Aokpi36gEji",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 912,
      "cache_creation_input_tokens": 1198,
      "cache_read_input_tokens": 33038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1198
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MQnZ8GmqEXwp8j7nTeQaPt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2405.06682",
  "prompt": "Extract: title, authors, venue/conference, year, arxiv ID, key findings about self-reflection limitations in agents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "26947819-7aed-4507-83bc-55ee8391e159",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApLYN4uFrq9Aokpi36gEji",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 912,
      "cache_creation_input_tokens": 1198,
      "cache_read_input_tokens": 33038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1198
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

_source line 17 · 2026-05-14T20:08:25.896Z_

<details><summary>↩ Tool result · `toolu_01MQnZ8GmqEXwp8j7nTeQaPt`</summary>

```text
# Research Paper Summary

**Title:** Self-Reflection in LLM Agents: Effects on Problem-Solving Performance

**Authors:** Matthew Renze, Erhan Guven

**Venue/Conference:** 2nd International Conference on Foundation and Large Language Models (FLLM 2024)

**Year:** 2024

**arXiv ID:** 2405.06682

## Key Findings

The research demonstrated that "LLM agents are able to significantly improve their problem-solving performance through self-reflection (p < 0.001)." The study evaluated nine popular LLMs using multiple-choice questions, then employed eight distinct self-reflection approaches on incorrect responses.

**Important Note on Limitations:** The provided abstract does not explicitly detail limitations of self-reflection in agents. The paper focuses on positive outcomes—showing statistically significant performance improvements—and mentions comparing different reflection types, but the full limitations discussion appears to be contained within the complete paper rather than the abstract provided.

The researchers made all code and data publicly available on GitHub to support reproducibility.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "0d61db37-b769-4149-a3e2-e8edc5c9d549",
  "tool_use_result": {
    "bytes": 46896,
    "code": 200,
    "codeText": "OK",
    "result": "# Research Paper Summary\n\n**Title:** Self-Reflection in LLM Agents: Effects on Problem-Solving Performance\n\n**Authors:** Matthew Renze, Erhan Guven\n\n**Venue/Conference:** 2nd International Conference on Foundation and Large Language Models (FLLM 2024)\n\n**Year:** 2024\n\n**arXiv ID:** 2405.06682\n\n## Key Findings\n\nThe research demonstrated that \"LLM agents are able to significantly improve their problem-solving performance through self-reflection (p < 0.001).\" The study evaluated nine popular LLMs using multiple-choice questions, then employed eight distinct self-reflection approaches on incorrect responses.\n\n**Important Note on Limitations:** The provided abstract does not explicitly detail limitations of self-reflection in agents. The paper focuses on positive outcomes—showing statistically significant performance improvements—and mentions comparing different reflection types, but the full limitations discussion appears to be contained within the complete paper rather than the abstract provided.\n\nThe researchers made all code and data publicly available on GitHub to support reproducibility.",
    "durationMs": 3638,
    "url": "https://arxiv.org/abs/2405.06682"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T20:08:26.142Z_

<details><summary>↩ Tool result · `toolu_0151q5eUUH4dDmMQq4Gmw3sr`</summary>

```text
# Paper Summary

**Title:** Large Language Models Cannot Self-Correct Reasoning Yet

**Authors:** Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou

**Venue/Conference:** ICLR 2024

**Year:** 2023 (submitted October 3, 2023; revised March 14, 2024)

**arXiv ID:** 2310.01798

## Key Findings on Self-Correction Limitations

The research reveals that "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction." 

The study focuses on *intrinsic self-correction*—where models attempt to correct themselves based solely on their own capabilities rather than receiving external guidance. The central conclusion is that this approach has significant limitations for reasoning tasks. Rather than improving accuracy, self-correction attempts can paradoxically worsen results, highlighting that current large language models lack the capacity for effective autonomous error detection and correction in logical reasoning contexts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "2fd1689b-58d3-4603-959d-1e037bce0d60",
  "tool_use_result": {
    "bytes": 46272,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** Large Language Models Cannot Self-Correct Reasoning Yet\n\n**Authors:** Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou\n\n**Venue/Conference:** ICLR 2024\n\n**Year:** 2023 (submitted October 3, 2023; revised March 14, 2024)\n\n**arXiv ID:** 2310.01798\n\n## Key Findings on Self-Correction Limitations\n\nThe research reveals that \"LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction.\" \n\nThe study focuses on *intrinsic self-correction*—where models attempt to correct themselves based solely on their own capabilities rather than receiving external guidance. The central conclusion is that this approach has significant limitations for reasoning tasks. Rather than improving accuracy, self-correction attempts can paradoxically worsen results, highlighting that current large language models lack the capacity for effective autonomous error detection and correction in logical reasoning contexts.",
    "durationMs": 4221,
    "url": "https://arxiv.org/abs/2310.01798"
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
The Huang et al. 2024 paper is the classic one about self-correction limitations. It's ICLR 2024. This is a great fit.

The Renze paper seems more positive about self-reflection, so it's less ideal for our "external monitoring > self-reflection" framing.

Let me look for the TACL survey paper on self-correction, and also the "Self-Correction Blind Spot" paper or other papers that more directly support external monitoring.

Let me search for the TACL survey "When Can LLMs Actually Correct Their Own Mistakes?"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "e88dab40-7712-4211-99d1-9be6a476a176",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fQeiNFYCYLTM4XejqEfPz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 262,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 34236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1585
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Nu4oQzVXBH76DkCVxRzxav`</summary>

```json
{
  "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes",
  "prompt": "Extract: title, all authors, venue, year, arxiv ID if available, key findings about when self-correction works vs fails"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "83aef618-ca87-4816-a57f-a8836b311adb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fQeiNFYCYLTM4XejqEfPz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 262,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 34236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1585
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

_source line 21_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018a24BRfZoiRbDGsWZ893ky`</summary>

```json
{
  "query": "arxiv \"When Can LLMs Actually Correct Their Own Mistakes\" survey self-correction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "19601a5d-3c44-430b-90a9-c848ef50e998",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fQeiNFYCYLTM4XejqEfPz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 262,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 34236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1585
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

_source line 22 · 2026-05-14T20:08:33.431Z_

<details><summary>↩ Tool result · reported error · `toolu_01Nu4oQzVXBH76DkCVxRzxav`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "b4712a8d-07f7-45cf-a927-7e65533a239e",
  "tool_use_result": "Error: Request failed with status code 403"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T20:08:40.557Z_

<details><summary>↩ Tool result · `toolu_018a24BRfZoiRbDGsWZ893ky`</summary>

```text
Web search results for query: "arxiv "When Can LLMs Actually Correct Their Own Mistakes" survey self-correction"

Links: [{"title":"[2406.01297] When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://arxiv.org/abs/2406.01297"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://arxiv.org/html/2406.01297v1"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes"},{"title":"[2406.01297v3] When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://arxiv.org/abs/2406.01297v3"},{"title":"[2406.01297v2] When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://arxiv.org/abs/2406.01297v2"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A ...","url":"https://aclanthology.org/2024.tacl-1.78.pdf"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | alphaXiv","url":"https://www.alphaxiv.org/abs/2406.01297"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs - ACL Anthology","url":"https://aclanthology.org/2024.tacl-1.78/"},{"title":"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs","url":"https://arxiv.org/html/2510.16062"}]

I found the paper you're looking for! Here are the key results:

## Paper Summary

The paper is titled "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs" by Ryo Kamoi and colleagues.

## Main Findings

Self-correction is an approach to improving responses from large language models (LLMs) by refining the responses using LLMs during inference. However, there is still no consensus on the question of when LLMs can correct their own mistakes, as recent studies also report negative results.

Prior studies often do not define their research questions in detail and involve impractical frameworks or unfair evaluations that over-evaluate self-correction. To address this, the authors categorize research questions in self-correction research and provide a checklist for designing appropriate experiments.

## Key Conclusions

The critical survey shows that (1) no prior work demonstrates successful self-correction with feedback from prompted LLMs, except for studies in tasks that are exceptionally suited for self-correction, (2) self-correction works well in tasks that can use reliable external feedback, and (3) large-scale fine-tuning enables self-correction.

## Publication Details

The paper was submitted in June 2024, revised in August 2024, and published as version 3 in December 2024. It also appears to have been published in the Transactions of the Association for Computational Linguistics (TACL) in 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "55fd79a4-4602-415f-8a88-d5beed5f8c62",
  "tool_use_result": {
    "query": "arxiv \"When Can LLMs Actually Correct Their Own Mistakes\" survey self-correction",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CjXVNqYBisfvTWaGuTnd2H",
        "content": [
          {
            "title": "[2406.01297] When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://arxiv.org/abs/2406.01297"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://arxiv.org/html/2406.01297v1"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes"
          },
          {
            "title": "[2406.01297v3] When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://arxiv.org/abs/2406.01297v3"
          },
          {
            "title": "[2406.01297v2] When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://arxiv.org/abs/2406.01297v2"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A ...",
            "url": "https://aclanthology.org/2024.tacl-1.78.pdf"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2406.01297"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2024.tacl-1.78/"
          },
          {
            "title": "Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs",
            "url": "https://arxiv.org/html/2510.16062"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key results:\n\n## Paper Summary\n\nThe paper is titled \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\" by Ryo Kamoi and colleagues.\n\n## Main Findings\n\nSelf-correction is an approach to improving responses from large language models (LLMs) by refining the responses using LLMs during inference. However, there is still no consensus on the question of when LLMs can correct their own mistakes, as recent studies also report negative results.\n\nPrior studies often do not define their research questions in detail and involve impractical frameworks or unfair evaluations that over-evaluate self-correction. To address this, the authors categorize research questions in self-correction research and provide a checklist for designing appropriate experiments.\n\n## Key Conclusions\n\nThe critical survey shows that (1) no prior work demonstrates successful self-correction with feedback from prompted LLMs, except for studies in tasks that are exceptionally suited for self-correction, (2) self-correction works well in tasks that can use reliable external feedback, and (3) large-scale fine-tuning enables self-correction.\n\n## Publication Details\n\nThe paper was submitted in June 2024, revised in August 2024, and published as version 3 in December 2024. It also appears to have been published in the Transactions of the Association for Computational Linguistics (TACL) in 2024."
    ],
    "durationSeconds": 7.151403134
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ay8EkE1PbEmSQa9toL4z2T`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.01297",
  "prompt": "Extract: exact title, all authors, arxiv ID, venue/conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "2135c853-92bb-4de1-a520-0e04a87412a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEL9KS8MhapHRRoc3iSQsn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1646,
      "cache_read_input_tokens": 35821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1646
      },
      "output_tokens": 59,
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

_source line 25 · 2026-05-14T20:08:45.875Z_

<details><summary>↩ Tool result · `toolu_01Ay8EkE1PbEmSQa9toL4z2T`</summary>

```text
# Paper Information

**Title:** "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs"

**Authors:** 
- Ryo Kamoi
- Yusen Zhang
- Nan Zhang
- Jiawei Han
- Rui Zhang

**arXiv ID:** 2406.01297

**Venue:** Transactions of the Association for Computational Linguistics (TACL 2024)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "49853785-ea22-4e96-b790-52c49733ddf7",
  "tool_use_result": {
    "bytes": 48751,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Information\n\n**Title:** \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n\n**Authors:** \n- Ryo Kamoi\n- Yusen Zhang\n- Nan Zhang\n- Jiawei Han\n- Rui Zhang\n\n**arXiv ID:** 2406.01297\n\n**Venue:** Transactions of the Association for Computational Linguistics (TACL 2024)",
    "durationMs": 2017,
    "url": "https://arxiv.org/abs/2406.01297"
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I have two strong candidates:

1. **Huang et al. "Large Language Models Cannot Self-Correct Reasoning Yet"** (ICLR 2024, arxiv 2310.01798)
   - Key finding: LLMs can't self-correct without external feedback, performance degrades
   - Perfect for our "external monitoring > self-reflection" framing

2. **Kamoi et al. "When Can LLMs Actually Correct Their Own Mistakes?"** (TACL 2024, arxiv 2406.01297)
   - Key finding: No successful self-correction with prompted LLM feedback; only works with reliable external feedback or large-scale fine-tuning
   - Also perfect for our framing

Both papers strongly reinforce the external monitoring narrative. The Huang et al. paper is the foundational 2023 work published at ICLR 2024, while Kamoi et al. provides a comprehensive 2024 synthesis of the landscape. I'm leaning toward using both, though I should consider whether there's something even more recent from 2025 that might be worth exploring.

Actually, these two are the most impactful and directly aligned with our framing, so I'll go with them. Now I'm adding these references to the literature map in the background section, placing them after the last existing entry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "ec9719f4-ee1d-4e03-9b68-316b48cd8da6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwhFPMuQDXqgB12RRkrqKS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 37467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 318
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

Found two strong papers that directly support our "external monitoring > self-reflection" framing. Adding them now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "9c3fb158-3f11-4eb5-9107-429024a0c84f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwhFPMuQDXqgB12RRkrqKS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 37467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 318
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

<details open><summary>🔧 Tool call — Edit · `toolu_01B8FazdZgoUzh9nKjSbuper`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
  "old_string": "  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  # ============================================================\n  # CATEGORY: technique",
  "new_string": "  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  - id: \"huang2024selfcorrect\"\n    title: \"Large Language Models Cannot Self-Correct Reasoning Yet\"\n    authors: \"Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2310.01798\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 失败的关键证据——支持 external monitoring 必要性\"\n    key_finding: \"LLM 在无外部反馈时无法自我纠错推理错误，intrinsic self-correction 甚至导致性能下降\"\n    our_differentiation: \"直接支持我们的核心论点：agent 不能可靠地自我检测 stagnation，需要外部 monitor（即我们的 TLM）\"\n\n  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 TLM 正是提供这种外部 stagnation 信号的轻量方案\"\n\n  # ============================================================\n  # CATEGORY: technique"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "53c30ed0-232c-4fbb-ad0d-13168e731bde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwhFPMuQDXqgB12RRkrqKS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 37467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 318
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

_source line 29 · 2026-05-14T20:09:15.867Z_

<details><summary>↩ Tool result · `toolu_01B8FazdZgoUzh9nKjSbuper`</summary>

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
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "4366de56-9c70-4d0f-a1e1-d102a79946f3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
    "oldString": "  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  # ============================================================\n  # CATEGORY: technique",
    "newString": "  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  - id: \"huang2024selfcorrect\"\n    title: \"Large Language Models Cannot Self-Correct Reasoning Yet\"\n    authors: \"Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2310.01798\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 失败的关键证据——支持 external monitoring 必要性\"\n    key_finding: \"LLM 在无外部反馈时无法自我纠错推理错误，intrinsic self-correction 甚至导致性能下降\"\n    our_differentiation: \"直接支持我们的核心论点：agent 不能可靠地自我检测 stagnation，需要外部 monitor（即我们的 TLM）\"\n\n  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 TLM 正是提供这种外部 stagnation 信号的轻量方案\"\n\n  # ============================================================\n  # CATEGORY: technique",
    "originalFile": "# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)\n# Generated: 2026-05-14\n# Paper: Temporal Label Model for Progress Stagnation Detection in LLM Agents\n#\n# Novelty check result: \"temporal label model\" as a general-purpose extension\n# of data programming to sequential data appears NOVEL. Closest works are\n# Safranchik AAAI 2020 (NER-specific linked HMM) and Sala NeurIPS 2019\n# (multi-resolution WS, not temporal transitions).\n\npapers:\n\n  # ============================================================\n  # CATEGORY: direct-competitor\n  # ============================================================\n\n  - id: \"xi2025agentprm\"\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Zhiheng Xi, Chenyang Liao, Guanyu Li, Yajie Yang, Wenxiang Chen, Zhihao Zhang, Binghai Wang, Senjie Jin, Yuhao Zhou, Jian Guan, Wei Wu, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2511.08325\"\n    category: \"direct-competitor\"\n    role: \"主要竞争者：step-level PRM for agent guidance\"\n    key_finding: \"用 promise（长期潜力）和 progress（即时进展）两个维度评估 agent 每步决策，实现 8x 计算效率提升\"\n    our_differentiation: \"我们是 window-level monitoring（不是 step-level guidance），不需要 outcome labels，目标是 stagnation detection 不是 reward shaping\"\n\n  - id: \"choudhury2025prm\"\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Sanjiban Choudhury\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2502.10325\"\n    category: \"direct-competitor\"\n    role: \"PRM 框架综述 + InversePRM 方法\"\n    key_finding: \"提出 AgentPRM（Monte Carlo rollout actor-critic）和 InversePRM（从 demonstrations 学习 process reward），3B 模型超越 GPT-4o\"\n    our_differentiation: \"InversePRM 仍需 demonstration trajectories，我们用 programmatic LFs 替代人工标注；我们关注 monitoring 而非 training signal\"\n\n  - id: \"li2026toolprmbench\"\n    title: \"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents\"\n    authors: \"Dawei Li, Yuguang Yao, Zhen Tan, Huan Liu, Ruocheng Guo\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.12294\"\n    category: \"direct-competitor\"\n    role: \"Tool-use PRM 评测基准\"\n    key_finding: \"大规模 benchmark 评测 PRM 在 tool-use 场景的效果，发现专用 PRM 显著优于通用 PRM\"\n    our_differentiation: \"我们的 TLM 是 unsupervised（不需要 step-level reward labels），且关注 stagnation pattern 而非 step correctness\"\n\n  - id: \"wang2026planrewardbench\"\n    title: \"Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling\"\n    authors: \"Jiaxuan Wang, Yulan Hu, Wenjin Yang, Zheng Pan, Xin Li, Lan-Zhe Guo\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.08178\"\n    category: \"direct-competitor\"\n    role: \"Trajectory-level reward model 评测\"\n    key_finding: \"所有 reward model 类别（generative, discriminative, LLM-as-Judge）在长 horizon trajectory 上性能显著下降\"\n    our_differentiation: \"验证了长 trajectory 评估的难度——我们的 window-level 方法通过局部化避免了这个问题\"\n\n  - id: \"chen2025monitoring\"\n    title: \"Monitoring LLM Agents for Sequentially Contextual Harm\"\n    authors: \"Yueh-Han Chen, Neelay Joshi, Yulin Chen, He He, Rico Angell\"\n    venue: \"ICLR 2025 Workshop on Building Trust in Language Models and Applications\"\n    year: 2025\n    arxiv: null\n    openreview: \"LC0XQ6ufbr\"\n    category: \"direct-competitor\"\n    role: \"Agent monitoring 安全方向\"\n    key_finding: \"将有害任务分解为单独无害的子任务可将 refusal rate 从 50% 降至 10%，现有 monitor 难以检测 sequentially contextual harm\"\n    our_differentiation: \"他们关注 safety monitoring（harmful behavior），我们关注 progress monitoring（stagnation）；互补方向\"\n\n  - id: \"kale2025weaktostrong\"\n    title: \"Reliable Weak-to-Strong Monitoring of LLM Agents\"\n    authors: \"Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team, Christina Q. Knight, Zifan Wang\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2508.19461\"\n    category: \"direct-competitor\"\n    role: \"Weak-to-strong agent monitoring 方法论\"\n    key_finding: \"Monitor scaffolding 比 monitor 能力更重要，弱模型可以可靠监控强模型；targeted human-in-the-loop 提升 TPR ~15%\"\n    our_differentiation: \"他们用 LLM 作为 monitor，我们用 structural LFs + TLM，不依赖另一个 LLM；我们的方法更轻量且可解释\"\n\n  - id: \"fan2026agentrm\"\n    title: \"Exploring Reasoning Reward Model for Agents\"\n    authors: \"Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.22154\"\n    category: \"direct-competitor\"\n    verified: true\n    role: \"Agent trajectory 的多维度 reasoning reward model\"\n    key_finding: \"Agent-RRM 通过 reasoning trace + critique + overall score 三维结构化反馈评估 agent trajectory，在 12 个 benchmark 上显著提升（GAIA 43.7%, WebWalkerQA 46.2%）\"\n    our_differentiation: \"他们用 LLM-based reward model 生成结构化反馈用于 agent 改进，我们用轻量 programmatic LFs + TLM 做 stagnation detection，不依赖大模型推理\"\n\n  - id: \"qiu2026dataprm\"\n    title: \"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis\"\n    authors: \"Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.24198\"\n    category: \"direct-competitor\"\n    verified: true\n    role: \"Agentic data analysis 场景的 process-level reward model\"\n    key_finding: \"传统 PRM 无法检测 silent errors 且误判 exploratory steps；DataPRM 通过 environment-aware probing + ternary reward 策略在 ScienceAgentBench 提升 7.21%\"\n    our_differentiation: \"DataPRM 针对数据分析 agent 的 step correctness，我们针对通用 agent 的 stagnation pattern；他们需要 execution state probing，我们用 structural LFs 无需环境交互\"\n\n  # ============================================================\n  # CATEGORY: method-component\n  # ============================================================\n\n  - id: \"ratner2016dataprogramming\"\n    title: \"Data Programming: Creating Large Training Sets, Quickly\"\n    authors: \"Alexander Ratner, Christopher De Sa, Sen Wu, Daniel Selsam, Christopher Re\"\n    venue: \"NeurIPS 2016\"\n    year: 2016\n    arxiv: \"1605.07723\"\n    category: \"method-component\"\n    role: \"核心方法论基础：data programming 范式\"\n    key_finding: \"用户编写 labeling functions（噪声启发式），generative model 学习 LF 准确率生成概率训练标签\"\n    our_differentiation: \"我们扩展 data programming 到时序数据，加入 temporal transition structure\"\n\n  - id: \"ratner2017snorkel\"\n    title: \"Snorkel: Rapid Training Data Creation with Weak Supervision\"\n    authors: \"Alexander Ratner, Stephen H. Bach, Henry Ehrenberg, Jason Fries, Sen Wu, Christopher Re\"\n    venue: \"VLDB 2018\"\n    year: 2018\n    arxiv: \"1711.10160\"\n    category: \"method-component\"\n    role: \"Data programming 系统实现，label model 基础\"\n    key_finding: \"端到端弱监督系统：LFs → generative label model（建模 LF dependency）→ discriminative end model\"\n    our_differentiation: \"Snorkel 假设数据点 i.i.d.，我们的 TLM 显式建模相邻 window 间的 label transition\"\n\n  - id: \"fu2020flyingsquid\"\n    title: \"Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods\"\n    authors: \"Daniel Y. Fu, Mayee F. Chen, Frederic Sala, Sarah M. Hooper, Kayvon Fatahalian, Christopher Re\"\n    venue: \"ICML 2020\"\n    year: 2020\n    arxiv: \"2002.11955\"\n    category: \"method-component\"\n    role: \"快速 label model，triplet method of moments\"\n    key_finding: \"用 triplet method 闭式求解 label model 参数，比 SGD 快 170x\"\n    our_differentiation: \"FlyingSquid 同样假设 i.i.d.；我们的 TLM 需要不同的参数估计方法来处理时序依赖\"\n\n  - id: \"zhang2021wrench\"\n    title: \"WRENCH: A Comprehensive Benchmark for Weak Supervision\"\n    authors: \"Jieyu Zhang, Yue Yu, Yinghao Li, Yujing Wang, Yaming Yang, Mao Yang, Alexander Ratner\"\n    venue: \"NeurIPS 2021 Datasets and Benchmarks Track\"\n    year: 2021\n    arxiv: \"2109.11377\"\n    category: \"method-component\"\n    role: \"弱监督评测基准\"\n    key_finding: \"22 个真实数据集 + 120+ 方法变体评测，标准化弱监督研究\"\n    our_differentiation: \"WRENCH 数据集全是 i.i.d. 分类/序列标注，没有 temporal stagnation detection 任务\"\n\n  - id: \"safranchik2020linkedhmm\"\n    title: \"Weakly Supervised Sequence Tagging from Noisy Rules\"\n    authors: \"Esteban Safranchik, Shiying Luo, Stephen H. Bach\"\n    venue: \"AAAI 2020\"\n    year: 2020\n    arxiv: null\n    category: \"method-component\"\n    role: \"最近的方法论前驱：linked HMM for sequence tagging weak supervision\"\n    key_finding: \"将 HMM 引入弱监督序列标注（NER），加入 linking rules 建模 span 结构，比 i.i.d. label model +7 F1\"\n    our_differentiation: \"他们是 token-level NER（BIO 约束），我们是 window-level temporal classification；我们建模的是 stagnation temporal dynamics 而非 entity boundary\"\n\n  - id: \"sala2019multiresolution\"\n    title: \"Multi-Resolution Weak Supervision for Sequential Data\"\n    authors: \"Frederic Sala, Paroma Varma, Jason Fries, Daniel Y. Fu, Stefano Sagawa, Christopher Re\"\n    venue: \"NeurIPS 2019\"\n    year: 2019\n    arxiv: \"1910.09505\"\n    category: \"method-component\"\n    role: \"最近的方法论前驱：multi-resolution WS for sequential data\"\n    key_finding: \"处理不同时间分辨率的 LFs（如 frame-level vs span-level），建模 multi-resolution LF correlations\"\n    our_differentiation: \"他们关注 resolution mismatch，我们关注 temporal label transitions；互补视角\"\n\n  - id: \"dawid1979em\"\n    title: \"Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm\"\n    authors: \"A. P. Dawid, A. M. Skene\"\n    venue: \"Journal of the Royal Statistical Society, Series C\"\n    year: 1979\n    arxiv: null\n    category: \"method-component\"\n    role: \"Label aggregation 奠基工作\"\n    key_finding: \"用 EM 算法估计标注者混淆矩阵，无需 ground truth\"\n    our_differentiation: \"经典 i.i.d. 假设；我们的 TLM 可视为 temporal extension of Dawid-Skene for programmatic LFs\"\n\n  - id: \"nguyen2017hmmcrowd\"\n    title: \"Aggregating and Predicting Sequence Labels from Crowd Annotations\"\n    authors: \"An Thanh Nguyen, Byron C. Wallace, Junyi Jessy Li, Ani Nenkova, Matthew Lease\"\n    venue: \"ACL 2017\"\n    year: 2017\n    arxiv: null\n    category: \"method-component\"\n    role: \"HMM + crowdsourcing label aggregation\"\n    key_finding: \"HMM-Crowd：扩展 Dawid-Skene 到序列数据，加入 one-step Markov structure over true labels\"\n    our_differentiation: \"他们用于 crowdsourcing（人类标注者），我们用于 programmatic LFs（自动化）；他们是 NER/IE，我们是 agent progress monitoring\"\n\n  # ============================================================\n  # CATEGORY: evaluation\n  # ============================================================\n\n  - id: \"orlanski2026slopcodebench\"\n    title: \"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks\"\n    authors: \"Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu, Albert Ge, Dyah Adila, Nicholas Roberts, Frederic Sala, Aws Albarghouthi\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.24755\"\n    category: \"evaluation\"\n    role: \"Agent degradation 基准——直接支持我们的 problem motivation\"\n    key_finding: \"Agent 代码质量在迭代任务中持续退化：比人类代码 2.3x 更冗余、2.0x 更结构侵蚀，75-77% trajectory 呈现退化趋势\"\n    our_differentiation: \"SlopCodeBench 量化了 degradation 现象，我们提供了检测方法；他们是 post-hoc 评测，我们是 online monitoring\"\n\n  - id: \"jimenez2024swebench\"\n    title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n    authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2310.06770\"\n    category: \"evaluation\"\n    role: \"Agent 数据来源之一\"\n    key_finding: \"2294 个真实 GitHub issue 任务，标准化 agent 评测\"\n    our_differentiation: \"我们使用 SWE-bench agent trajectories 作为实验数据源之一\"\n\n  - id: \"yang2024sweagent\"\n    title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n    authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv: \"2405.15793\"\n    category: \"evaluation\"\n    role: \"Agent 系统——trajectory 数据来源\"\n    key_finding: \"提出 agent-computer interface (ACI)，GPT-4 Turbo 在 SWE-bench 达 12.47% resolve rate\"\n    our_differentiation: \"SWE-agent trajectories 是我们分析 stagnation 的数据来源之一\"\n\n  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================\n\n  - id: \"shinn2023reflexion\"\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    arxiv: \"2303.11366\"\n    category: \"background\"\n    role: \"Agent self-reflection 代表工作\"\n    key_finding: \"通过 verbal feedback 强化 agent，反思文本存入 episodic memory 用于后续 trial\"\n    our_differentiation: \"Reflexion 是 agent 自我改进机制，我们是外部 monitoring；self-reflection 可能失效时我们的 monitor 仍能检测 stagnation\"\n\n  - id: \"zhou2024lats\"\n    title: \"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\"\n    authors: \"Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang\"\n    venue: \"ICML 2024\"\n    year: 2024\n    arxiv: \"2310.04406\"\n    category: \"background\"\n    role: \"Agent planning + self-reflection\"\n    key_finding: \"结合 MCTS 与 LM value function 和 self-reflection，支持 backtracking\"\n    our_differentiation: \"LATS 通过搜索避免 stagnation，但计算开销大；我们的 monitor 可作为 LATS 的早期终止信号\"\n\n  - id: \"yao2023tot\"\n    title: \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\"\n    authors: \"Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    arxiv: \"2305.10601\"\n    category: \"background\"\n    role: \"Deliberate reasoning 框架\"\n    key_finding: \"将 CoT 泛化为树结构，LM 自我评估中间 thought 并 backtrack\"\n    our_differentiation: \"ToT 的自评估是 single-step 的；我们捕捉 multi-step temporal patterns\"\n\n  - id: \"cemri2025multiagentfail\"\n    title: \"Why Do Multi-Agent LLM Systems Fail?\"\n    authors: \"Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2503.13657\"\n    category: \"background\"\n    role: \"Agent failure taxonomy——problem motivation\"\n    key_finding: \"MAST taxonomy：14 种失败模式，其中 Step Repetition 被识别为具体失败症状\"\n    our_differentiation: \"他们提供 taxonomy（what fails），我们提供 detection method（how to detect）\"\n\n  - id: \"zhu2025agentfail\"\n    title: \"Where LLM Agents Fail and How They Can Learn From Failures\"\n    authors: \"Kunlun Zhu, Zijia Liu, Bingxuan Li, et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2509.25370\"\n    category: \"background\"\n    role: \"Agent failure 分析 + cascading failure 发现\"\n    key_finding: \"Cascading failures（单一 root cause 传播到后续决策）是长 horizon 任务的主要失败模式\"\n    our_differentiation: \"Cascading failure 正是我们 temporal model 可以捕捉的 pattern——stagnation 往往是 cascade 的表现\"\n\n  - id: \"george2025cycledetection\"\n    title: \"Unsupervised Cycle Detection in Agentic Applications\"\n    authors: \"Felix George, Harshit Kumar, Divya Pathak, Kaustabha Ray, Mudit Verma, Pratibha Moogi\"\n    venue: \"arXiv preprint (IBM Research)\"\n    year: 2025\n    arxiv: \"2511.10650\"\n    category: \"background\"\n    role: \"Cycle detection——最相关的 stagnation detection 前驱\"\n    key_finding: \"混合方法：call-stack 分析（结构重复）+ embedding 语义相似度确认\"\n    our_differentiation: \"他们只检测 exact/near-exact cycles，我们检测更广义的 stagnation（包括非重复性的停滞）；他们是 unsupervised rule-based，我们是 learned temporal model\"\n\n  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================\n\n  - id: \"cho2014gru\"\n    title: \"Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation\"\n    authors: \"Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio\"\n    venue: \"EMNLP 2014\"\n    year: 2014\n    arxiv: \"1406.1078\"\n    category: \"technique\"\n    role: \"GRU 原始论文——我们 probe model 的序列编码器\"\n    key_finding: \"提出 GRU hidden unit，自适应门控信息流\"\n\n  - id: \"bahdanau2015attention\"\n    title: \"Neural Machine Translation by Jointly Learning to Align and Translate\"\n    authors: \"Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio\"\n    venue: \"ICLR 2015\"\n    year: 2015\n    arxiv: \"1409.0473\"\n    category: \"technique\"\n    role: \"Attention mechanism——我们 probe model 的 attention 组件\"\n    key_finding: \"注意力机制允许 decoder 选择性关注输入序列不同位置\"\n\n  - id: \"khosla2020supcon\"\n    title: \"Supervised Contrastive Learning\"\n    authors: \"Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, Dilip Krishnan\"\n    venue: \"NeurIPS 2020\"\n    year: 2020\n    arxiv: \"2004.11362\"\n    category: \"technique\"\n    role: \"SupCon loss——我们的辅助训练目标\"\n    key_finding: \"扩展自监督对比学习到有监督设置，同类样本拉近、异类推远，提升鲁棒性\"\n\n  - id: \"zhang2025qwen3embedding\"\n    title: \"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models\"\n    authors: \"Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2506.05176\"\n    category: \"technique\"\n    role: \"Embedding model——我们用于生成 trajectory window embeddings\"\n    key_finding: \"基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA\"\n\n# ============================================================\n# NOVELTY ANALYSIS SUMMARY\n# ============================================================\n#\n# Key finding: \"Temporal Label Model\" 作为通用方法论是 NOVEL。\n#\n# 最近的前驱工作：\n# 1. Safranchik AAAI 2020 (linked HMM) — NER-specific，BIO 约束，token-level\n# 2. Sala NeurIPS 2019 (multi-resolution WS) — 处理分辨率不匹配，不建模 label transition\n# 3. Nguyen ACL 2017 (HMM-Crowd) — crowdsourcing 场景，不是 programmatic LFs\n#\n# 没有人将 data programming + HMM-style temporal transitions 用于：\n# - 通用序列分类（非 NER）\n# - Agent trajectory monitoring\n# - Stagnation detection\n#\n# 我们的 TLM 填补的空白：general-purpose temporal extension of\n# data programming label models for sequential classification tasks.\n",
    "structuredPatch": [
      {
        "oldStart": 325,
        "oldLines": 6,
        "newStart": 325,
        "newLines": 30,
        "lines": [
          "     key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"",
          "     our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"",
          " ",
          "+  - id: \"huang2024selfcorrect\"",
          "+    title: \"Large Language Models Cannot Self-Correct Reasoning Yet\"",
          "+    authors: \"Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou\"",
          "+    venue: \"ICLR 2024\"",
          "+    year: 2024",
          "+    arxiv: \"2310.01798\"",
          "+    category: \"background\"",
          "+    verified: true",
          "+    role: \"Self-correction 失败的关键证据——支持 external monitoring 必要性\"",
          "+    key_finding: \"LLM 在无外部反馈时无法自我纠错推理错误，intrinsic self-correction 甚至导致性能下降\"",
          "+    our_differentiation: \"直接支持我们的核心论点：agent 不能可靠地自我检测 stagnation，需要外部 monitor（即我们的 TLM）\"",
          "+",
          "+  - id: \"kamoi2024selfcorrection\"",
          "+    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"",
          "+    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"",
          "+    venue: \"TACL 2024\"",
          "+    year: 2024",
          "+    arxiv: \"2406.01297\"",
          "+    category: \"background\"",
          "+    verified: true",
          "+    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"",
          "+    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"",
          "+    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 TLM 正是提供这种外部 stagnation 信号的轻量方案\"",
          "+",
          "   # ============================================================",
          "   # CATEGORY: technique",
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

_source line 30_

已添加 2 篇论文到 `background` 类别末尾：

1. **huang2024selfcorrect** — "Large Language Models Cannot Self-Correct Reasoning Yet" (ICLR 2024, `2310.01798`)  
   核心证据：LLM 无外部反馈时 intrinsic self-correction 失败甚至降低性能。

2. **kamoi2024selfcorrection** — "When Can LLMs Actually Correct Their Own Mistakes?" (TACL 2024, `2406.01297`)  
   系统性综述确认：prompted self-correction 无一成功，self-correction 仅在有可靠外部反馈时有效。

两篇都直接支持我们的 "external monitoring > self-reflection" 论点——agent 不能可靠自检 stagnation，需要外部 monitor（即 TLM）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "uuid": "6a8c3dbe-db7d-4287-86e5-3569986fb01a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6SZgsvXqAvruFspUdMs9d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1670,
      "cache_read_input_tokens": 37785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1670
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

已添加 2 篇论文到 `background` 类别末尾：

1. **huang2024selfcorrect** — "Large Language Models Cannot Self-Correct Reasoning Yet" (ICLR 2024, `2310.01798`)  
   核心证据：LLM 无外部反馈时 intrinsic self-correction 失败甚至降低性能。

2. **kamoi2024selfcorrection** — "When Can LLMs Actually Correct Their Own Mistakes?" (TACL 2024, `2406.01297`)  
   系统性综述确认：prompted self-correction 无一成功，self-correction 仅在有可靠外部反馈时有效。

两篇都直接支持我们的 "external monitoring > self-reflection" 论点——agent 不能可靠自检 stagnation，需要外部 monitor（即 TLM）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 83480,
  "duration_api_ms": 96244,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "50ee3d9f-e490-4eb3-8df5-4bf7efb336e7",
  "total_cost_usd": 0.4717255,
  "usage": {
    "input_tokens": 1182,
    "cache_creation_input_tokens": 27614,
    "cache_read_input_tokens": 213698,
    "output_tokens": 3017,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 27614,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 241,
        "cache_read_input_tokens": 37785,
        "cache_creation_input_tokens": 1670,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1670
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 69499,
      "outputTokens": 2291,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 3,
      "costUSD": 0.11095400000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1182,
      "outputTokens": 3017,
      "cacheReadInputTokens": 213698,
      "cacheCreationInputTokens": 27614,
      "webSearchRequests": 0,
      "costUSD": 0.36077149999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "900872bd-24cc-4d10-bb46-e09ce275ce4d"
}
```

</details>

---
