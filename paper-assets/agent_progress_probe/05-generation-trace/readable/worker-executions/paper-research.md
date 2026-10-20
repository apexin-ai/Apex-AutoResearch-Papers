# paper research

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_paper_research_20260514T202752.log`
- **Structured JSON:** [`54c638ebba5fb2b95ad0.json`](../../sessions/54/54c638ebba5fb2b95ad0.json)

## Before a recorded user message

30 recorded events

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
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
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
  "uuid": "26dcb6ac-782c-4472-a069-93f0d5cfa986",
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
  "uuid": "313d004f-2a2d-4c61-b1ca-7993d64c73b2",
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79"
}
```

---

### Assistant

_source line 4_

I'll search for the papers and then update the literature map. Let me start by reading the current file and searching for papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "a6aab1b8-9e19-4cd4-9c24-375f29709054",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEtBhLCbyUn98HGiKfJzo6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11688,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11688
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

<details open><summary>🔧 Tool call — Read · `toolu_01XT49LidPLAdfV8Q5uHwwqL`</summary>

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
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "e84ea529-a550-423b-8f24-e8755efb7b66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEtBhLCbyUn98HGiKfJzo6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11688,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11688
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

_source line 6 · 2026-05-14T20:28:03.859Z_

<details><summary>↩ Tool result · `toolu_01XT49LidPLAdfV8Q5uHwwqL`</summary>

```text
1	# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)
2	# Generated: 2026-05-14
3	# Paper: Structural Signal Analysis for Progress Stagnation Detection in LLM Agents
4	#
5	# D039 Pivot: Empirical analysis paper. Central finding: stagnation signals are
6	# fundamentally structural (30 features → 0.995 in-domain, 0.967 cross-agent F1),
7	# decisively surpassing NL embeddings (0.906/0.751) and LLM-as-judge (+24.3pp).
8	# TLM is a well-motivated negative finding (3 implementations all fail to beat MV).
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
47	    our_differentiation: "我们的 empirical analysis 揭示 structural features 足以检测 stagnation（0.995 F1），无需 step-level reward labels；关注 stagnation pattern 而非 step correctness"
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
81	    our_differentiation: "他们用 LLM 作为 monitor，我们发现 30 个 structural features 即可达 0.967 跨域 F1，不依赖另一个 LLM；更轻量（<5ms）且可解释"
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
93	    our_differentiation: "他们用 LLM-based reward model 生成结构化反馈用于 agent 改进，我们的 empirical analysis 表明轻量 structural features 即可高精度检测 stagnation（0.995 F1），不依赖大模型推理"
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
120	    our_differentiation: "我们在 agent trajectory 上应用 data programming，发现 structural features 主导检测能力；同时揭示 LFs 的时序动态和 temporal label model 的负面结果"
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
131	    our_differentiation: "Snorkel 假设数据点 i.i.d.，我们发现 agent trajectory 上 LFs 展现系统性时序动态（violating i.i.d.），但 temporal label model 未能超越 MV（negative finding）"
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
142	    our_differentiation: "FlyingSquid 同样假设 i.i.d.；我们的 empirical analysis 揭示 i.i.d. violation 虽系统性存在，但 temporal correction 在低冲突 regime 下无收益（negative finding）"
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
186	    our_differentiation: "经典 i.i.d. 假设；我们测试了 temporal extension（HMM-TLM, lag-aware HMM）但发现在 3-LF 低冲突 regime 下未超越 MV——约束未来 temporal label model 研究"
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
315	    our_differentiation: "他们只检测 exact/near-exact cycles，我们检测更广义的 stagnation（包括非重复性的停滞）；我们的 empirical analysis 表明 30 个 structural features（含但不限于 cycle 特征）即可达 0.995 F1"
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
328	  - id: "huang2024selfcorrect"
329	    title: "Large Language Models Cannot Self-Correct Reasoning Yet"
330	    authors: "Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou"
331	    venue: "ICLR 2024"
332	    year: 2024
333	    arxiv: "2310.01798"
334	    category: "background"
335	    verified: true
336	    role: "Self-correction 失败的关键证据——支持 external monitoring 必要性"
337	    key_finding: "LLM 在无外部反馈时无法自我纠错推理错误，intrinsic self-correction 甚至导致性能下降"
338	    our_differentiation: "直接支持我们的核心论点：agent 不能可靠地自我检测 stagnation，需要外部 monitor；我们的 structural features 提供了轻量（<5ms）且高精度（0.995 F1）的外部检测方案"
339	
340	  - id: "kamoi2024selfcorrection"
341	    title: "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs"
342	    authors: "Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang"
343	    venue: "TACL 2024"
344	    year: 2024
345	    arxiv: "2406.01297"
346	    category: "background"
347	    verified: true
348	    role: "Self-correction 条件的系统性综述——外部反馈是成功的必要条件"
349	    key_finding: "无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效"
350	    our_differentiation: "综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解"
351	
352	  # ============================================================
353	  # CATEGORY: technique
354	  # ============================================================
355	
356	  - id: "cho2014gru"
357	    title: "Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation"
358	    authors: "Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio"
359	    venue: "EMNLP 2014"
360	    year: 2014
361	    arxiv: "1406.1078"
362	    category: "technique"
363	    role: "GRU 原始论文——我们 probe model 的序列编码器"
364	    key_finding: "提出 GRU hidden unit，自适应门控信息流"
365	
366	  - id: "bahdanau2015attention"
367	    title: "Neural Machine Translation by Jointly Learning to Align and Translate"
368	    authors: "Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio"
369	    venue: "ICLR 2015"
370	    year: 2015
371	    arxiv: "1409.0473"
372	    category: "technique"
373	    role: "Attention mechanism——我们 probe model 的 attention 组件"
374	    key_finding: "注意力机制允许 decoder 选择性关注输入序列不同位置"
375	
376	  - id: "khosla2020supcon"
377	    title: "Supervised Contrastive Learning"
378	    authors: "Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, Dilip Krishnan"
379	    venue: "NeurIPS 2020"
380	    year: 2020
381	    arxiv: "2004.11362"
382	    category: "technique"
383	    role: "SupCon loss——我们的辅助训练目标"
384	    key_finding: "扩展自监督对比学习到有监督设置，同类样本拉近、异类推远，提升鲁棒性"
385	
386	  - id: "zhang2025qwen3embedding"
387	    title: "Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models"
388	    authors: "Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou"
389	    venue: "arXiv preprint"
390	    year: 2025
391	    arxiv: "2506.05176"
392	    category: "technique"
393	    role: "Embedding model——我们用于生成 trajectory window embeddings"
394	    key_finding: "基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA"
395	
396	# ============================================================
397	# NOVELTY ANALYSIS SUMMARY (D039 Pivot — Empirical Analysis)
398	# ============================================================
399	#
400	# Primary novelty: 首次系统性实证分析 agent stagnation 检测中 structural vs
401	# semantic signal 的有效性。30 个结构特征达 0.995 in-domain / 0.967 cross-agent F1，
402	# 全面优于 NL embedding (0.906/0.751) 和 LLM-as-judge (+24.3pp)。
403	#
404	# 三层贡献：
405	# 1. Structural Signal Discovery (primary) — 改变社区对 agent monitoring 方法选型认知
406	# 2. LF Temporal Dynamics Analysis — 量化 LFs 时序角色 + agent-specific 迁移分析
407	# 3. TLM Negative Finding — 3 种实现 (TWV/HMM/lag-aware HMM) 均未超越 MV
408	#
409	# 方法论前驱（TLM negative finding 的参照）：
410	# 1. Safranchik AAAI 2020 (linked HMM) — NER-specific，BIO 约束，token-level
411	# 2. Sala NeurIPS 2019 (multi-resolution WS) — 处理分辨率不匹配，不建模 label transition
412	# 3. Nguyen ACL 2017 (HMM-Crowd) — crowdsourcing 场景，不是 programmatic LFs
413	#
414	# 核心差异化：不是 "method paper proposing TLM"，而是 "empirical study revealing
415	# structural signals dominate stagnation detection, with temporal modeling as
416	# well-motivated negative finding".
417	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "8c0dedf8-da0b-4d28-969c-a7893186ac36",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
      "content": "# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)\n# Generated: 2026-05-14\n# Paper: Structural Signal Analysis for Progress Stagnation Detection in LLM Agents\n#\n# D039 Pivot: Empirical analysis paper. Central finding: stagnation signals are\n# fundamentally structural (30 features → 0.995 in-domain, 0.967 cross-agent F1),\n# decisively surpassing NL embeddings (0.906/0.751) and LLM-as-judge (+24.3pp).\n# TLM is a well-motivated negative finding (3 implementations all fail to beat MV).\n\npapers:\n\n  # ============================================================\n  # CATEGORY: direct-competitor\n  # ============================================================\n\n  - id: \"xi2025agentprm\"\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Zhiheng Xi, Chenyang Liao, Guanyu Li, Yajie Yang, Wenxiang Chen, Zhihao Zhang, Binghai Wang, Senjie Jin, Yuhao Zhou, Jian Guan, Wei Wu, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2511.08325\"\n    category: \"direct-competitor\"\n    role: \"主要竞争者：step-level PRM for agent guidance\"\n    key_finding: \"用 promise（长期潜力）和 progress（即时进展）两个维度评估 agent 每步决策，实现 8x 计算效率提升\"\n    our_differentiation: \"我们是 window-level monitoring（不是 step-level guidance），不需要 outcome labels，目标是 stagnation detection 不是 reward shaping\"\n\n  - id: \"choudhury2025prm\"\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Sanjiban Choudhury\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2502.10325\"\n    category: \"direct-competitor\"\n    role: \"PRM 框架综述 + InversePRM 方法\"\n    key_finding: \"提出 AgentPRM（Monte Carlo rollout actor-critic）和 InversePRM（从 demonstrations 学习 process reward），3B 模型超越 GPT-4o\"\n    our_differentiation: \"InversePRM 仍需 demonstration trajectories，我们用 programmatic LFs 替代人工标注；我们关注 monitoring 而非 training signal\"\n\n  - id: \"li2026toolprmbench\"\n    title: \"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents\"\n    authors: \"Dawei Li, Yuguang Yao, Zhen Tan, Huan Liu, Ruocheng Guo\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.12294\"\n    category: \"direct-competitor\"\n    role: \"Tool-use PRM 评测基准\"\n    key_finding: \"大规模 benchmark 评测 PRM 在 tool-use 场景的效果，发现专用 PRM 显著优于通用 PRM\"\n    our_differentiation: \"我们的 empirical analysis 揭示 structural features 足以检测 stagnation（0.995 F1），无需 step-level reward labels；关注 stagnation pattern 而非 step correctness\"\n\n  - id: \"wang2026planrewardbench\"\n    title: \"Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling\"\n    authors: \"Jiaxuan Wang, Yulan Hu, Wenjin Yang, Zheng Pan, Xin Li, Lan-Zhe Guo\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.08178\"\n    category: \"direct-competitor\"\n    role: \"Trajectory-level reward model 评测\"\n    key_finding: \"所有 reward model 类别（generative, discriminative, LLM-as-Judge）在长 horizon trajectory 上性能显著下降\"\n    our_differentiation: \"验证了长 trajectory 评估的难度——我们的 window-level 方法通过局部化避免了这个问题\"\n\n  - id: \"chen2025monitoring\"\n    title: \"Monitoring LLM Agents for Sequentially Contextual Harm\"\n    authors: \"Yueh-Han Chen, Neelay Joshi, Yulin Chen, He He, Rico Angell\"\n    venue: \"ICLR 2025 Workshop on Building Trust in Language Models and Applications\"\n    year: 2025\n    arxiv: null\n    openreview: \"LC0XQ6ufbr\"\n    category: \"direct-competitor\"\n    role: \"Agent monitoring 安全方向\"\n    key_finding: \"将有害任务分解为单独无害的子任务可将 refusal rate 从 50% 降至 10%，现有 monitor 难以检测 sequentially contextual harm\"\n    our_differentiation: \"他们关注 safety monitoring（harmful behavior），我们关注 progress monitoring（stagnation）；互补方向\"\n\n  - id: \"kale2025weaktostrong\"\n    title: \"Reliable Weak-to-Strong Monitoring of LLM Agents\"\n    authors: \"Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team, Christina Q. Knight, Zifan Wang\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2508.19461\"\n    category: \"direct-competitor\"\n    role: \"Weak-to-strong agent monitoring 方法论\"\n    key_finding: \"Monitor scaffolding 比 monitor 能力更重要，弱模型可以可靠监控强模型；targeted human-in-the-loop 提升 TPR ~15%\"\n    our_differentiation: \"他们用 LLM 作为 monitor，我们发现 30 个 structural features 即可达 0.967 跨域 F1，不依赖另一个 LLM；更轻量（<5ms）且可解释\"\n\n  - id: \"fan2026agentrm\"\n    title: \"Exploring Reasoning Reward Model for Agents\"\n    authors: \"Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.22154\"\n    category: \"direct-competitor\"\n    verified: true\n    role: \"Agent trajectory 的多维度 reasoning reward model\"\n    key_finding: \"Agent-RRM 通过 reasoning trace + critique + overall score 三维结构化反馈评估 agent trajectory，在 12 个 benchmark 上显著提升（GAIA 43.7%, WebWalkerQA 46.2%）\"\n    our_differentiation: \"他们用 LLM-based reward model 生成结构化反馈用于 agent 改进，我们的 empirical analysis 表明轻量 structural features 即可高精度检测 stagnation（0.995 F1），不依赖大模型推理\"\n\n  - id: \"qiu2026dataprm\"\n    title: \"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis\"\n    authors: \"Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.24198\"\n    category: \"direct-competitor\"\n    verified: true\n    role: \"Agentic data analysis 场景的 process-level reward model\"\n    key_finding: \"传统 PRM 无法检测 silent errors 且误判 exploratory steps；DataPRM 通过 environment-aware probing + ternary reward 策略在 ScienceAgentBench 提升 7.21%\"\n    our_differentiation: \"DataPRM 针对数据分析 agent 的 step correctness，我们针对通用 agent 的 stagnation pattern；他们需要 execution state probing，我们用 structural LFs 无需环境交互\"\n\n  # ============================================================\n  # CATEGORY: method-component\n  # ============================================================\n\n  - id: \"ratner2016dataprogramming\"\n    title: \"Data Programming: Creating Large Training Sets, Quickly\"\n    authors: \"Alexander Ratner, Christopher De Sa, Sen Wu, Daniel Selsam, Christopher Re\"\n    venue: \"NeurIPS 2016\"\n    year: 2016\n    arxiv: \"1605.07723\"\n    category: \"method-component\"\n    role: \"核心方法论基础：data programming 范式\"\n    key_finding: \"用户编写 labeling functions（噪声启发式），generative model 学习 LF 准确率生成概率训练标签\"\n    our_differentiation: \"我们在 agent trajectory 上应用 data programming，发现 structural features 主导检测能力；同时揭示 LFs 的时序动态和 temporal label model 的负面结果\"\n\n  - id: \"ratner2017snorkel\"\n    title: \"Snorkel: Rapid Training Data Creation with Weak Supervision\"\n    authors: \"Alexander Ratner, Stephen H. Bach, Henry Ehrenberg, Jason Fries, Sen Wu, Christopher Re\"\n    venue: \"VLDB 2018\"\n    year: 2018\n    arxiv: \"1711.10160\"\n    category: \"method-component\"\n    role: \"Data programming 系统实现，label model 基础\"\n    key_finding: \"端到端弱监督系统：LFs → generative label model（建模 LF dependency）→ discriminative end model\"\n    our_differentiation: \"Snorkel 假设数据点 i.i.d.，我们发现 agent trajectory 上 LFs 展现系统性时序动态（violating i.i.d.），但 temporal label model 未能超越 MV（negative finding）\"\n\n  - id: \"fu2020flyingsquid\"\n    title: \"Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods\"\n    authors: \"Daniel Y. Fu, Mayee F. Chen, Frederic Sala, Sarah M. Hooper, Kayvon Fatahalian, Christopher Re\"\n    venue: \"ICML 2020\"\n    year: 2020\n    arxiv: \"2002.11955\"\n    category: \"method-component\"\n    role: \"快速 label model，triplet method of moments\"\n    key_finding: \"用 triplet method 闭式求解 label model 参数，比 SGD 快 170x\"\n    our_differentiation: \"FlyingSquid 同样假设 i.i.d.；我们的 empirical analysis 揭示 i.i.d. violation 虽系统性存在，但 temporal correction 在低冲突 regime 下无收益（negative finding）\"\n\n  - id: \"zhang2021wrench\"\n    title: \"WRENCH: A Comprehensive Benchmark for Weak Supervision\"\n    authors: \"Jieyu Zhang, Yue Yu, Yinghao Li, Yujing Wang, Yaming Yang, Mao Yang, Alexander Ratner\"\n    venue: \"NeurIPS 2021 Datasets and Benchmarks Track\"\n    year: 2021\n    arxiv: \"2109.11377\"\n    category: \"method-component\"\n    role: \"弱监督评测基准\"\n    key_finding: \"22 个真实数据集 + 120+ 方法变体评测，标准化弱监督研究\"\n    our_differentiation: \"WRENCH 数据集全是 i.i.d. 分类/序列标注，没有 temporal stagnation detection 任务\"\n\n  - id: \"safranchik2020linkedhmm\"\n    title: \"Weakly Supervised Sequence Tagging from Noisy Rules\"\n    authors: \"Esteban Safranchik, Shiying Luo, Stephen H. Bach\"\n    venue: \"AAAI 2020\"\n    year: 2020\n    arxiv: null\n    category: \"method-component\"\n    role: \"最近的方法论前驱：linked HMM for sequence tagging weak supervision\"\n    key_finding: \"将 HMM 引入弱监督序列标注（NER），加入 linking rules 建模 span 结构，比 i.i.d. label model +7 F1\"\n    our_differentiation: \"他们是 token-level NER（BIO 约束），我们是 window-level temporal classification；我们建模的是 stagnation temporal dynamics 而非 entity boundary\"\n\n  - id: \"sala2019multiresolution\"\n    title: \"Multi-Resolution Weak Supervision for Sequential Data\"\n    authors: \"Frederic Sala, Paroma Varma, Jason Fries, Daniel Y. Fu, Stefano Sagawa, Christopher Re\"\n    venue: \"NeurIPS 2019\"\n    year: 2019\n    arxiv: \"1910.09505\"\n    category: \"method-component\"\n    role: \"最近的方法论前驱：multi-resolution WS for sequential data\"\n    key_finding: \"处理不同时间分辨率的 LFs（如 frame-level vs span-level），建模 multi-resolution LF correlations\"\n    our_differentiation: \"他们关注 resolution mismatch，我们关注 temporal label transitions；互补视角\"\n\n  - id: \"dawid1979em\"\n    title: \"Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm\"\n    authors: \"A. P. Dawid, A. M. Skene\"\n    venue: \"Journal of the Royal Statistical Society, Series C\"\n    year: 1979\n    arxiv: null\n    category: \"method-component\"\n    role: \"Label aggregation 奠基工作\"\n    key_finding: \"用 EM 算法估计标注者混淆矩阵，无需 ground truth\"\n    our_differentiation: \"经典 i.i.d. 假设；我们测试了 temporal extension（HMM-TLM, lag-aware HMM）但发现在 3-LF 低冲突 regime 下未超越 MV——约束未来 temporal label model 研究\"\n\n  - id: \"nguyen2017hmmcrowd\"\n    title: \"Aggregating and Predicting Sequence Labels from Crowd Annotations\"\n    authors: \"An Thanh Nguyen, Byron C. Wallace, Junyi Jessy Li, Ani Nenkova, Matthew Lease\"\n    venue: \"ACL 2017\"\n    year: 2017\n    arxiv: null\n    category: \"method-component\"\n    role: \"HMM + crowdsourcing label aggregation\"\n    key_finding: \"HMM-Crowd：扩展 Dawid-Skene 到序列数据，加入 one-step Markov structure over true labels\"\n    our_differentiation: \"他们用于 crowdsourcing（人类标注者），我们用于 programmatic LFs（自动化）；他们是 NER/IE，我们是 agent progress monitoring\"\n\n  # ============================================================\n  # CATEGORY: evaluation\n  # ============================================================\n\n  - id: \"orlanski2026slopcodebench\"\n    title: \"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks\"\n    authors: \"Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu, Albert Ge, Dyah Adila, Nicholas Roberts, Frederic Sala, Aws Albarghouthi\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.24755\"\n    category: \"evaluation\"\n    role: \"Agent degradation 基准——直接支持我们的 problem motivation\"\n    key_finding: \"Agent 代码质量在迭代任务中持续退化：比人类代码 2.3x 更冗余、2.0x 更结构侵蚀，75-77% trajectory 呈现退化趋势\"\n    our_differentiation: \"SlopCodeBench 量化了 degradation 现象，我们提供了检测方法；他们是 post-hoc 评测，我们是 online monitoring\"\n\n  - id: \"jimenez2024swebench\"\n    title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n    authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2310.06770\"\n    category: \"evaluation\"\n    role: \"Agent 数据来源之一\"\n    key_finding: \"2294 个真实 GitHub issue 任务，标准化 agent 评测\"\n    our_differentiation: \"我们使用 SWE-bench agent trajectories 作为实验数据源之一\"\n\n  - id: \"yang2024sweagent\"\n    title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n    authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv: \"2405.15793\"\n    category: \"evaluation\"\n    role: \"Agent 系统——trajectory 数据来源\"\n    key_finding: \"提出 agent-computer interface (ACI)，GPT-4 Turbo 在 SWE-bench 达 12.47% resolve rate\"\n    our_differentiation: \"SWE-agent trajectories 是我们分析 stagnation 的数据来源之一\"\n\n  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================\n\n  - id: \"shinn2023reflexion\"\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    arxiv: \"2303.11366\"\n    category: \"background\"\n    role: \"Agent self-reflection 代表工作\"\n    key_finding: \"通过 verbal feedback 强化 agent，反思文本存入 episodic memory 用于后续 trial\"\n    our_differentiation: \"Reflexion 是 agent 自我改进机制，我们是外部 monitoring；self-reflection 可能失效时我们的 monitor 仍能检测 stagnation\"\n\n  - id: \"zhou2024lats\"\n    title: \"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\"\n    authors: \"Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang\"\n    venue: \"ICML 2024\"\n    year: 2024\n    arxiv: \"2310.04406\"\n    category: \"background\"\n    role: \"Agent planning + self-reflection\"\n    key_finding: \"结合 MCTS 与 LM value function 和 self-reflection，支持 backtracking\"\n    our_differentiation: \"LATS 通过搜索避免 stagnation，但计算开销大；我们的 monitor 可作为 LATS 的早期终止信号\"\n\n  - id: \"yao2023tot\"\n    title: \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\"\n    authors: \"Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    arxiv: \"2305.10601\"\n    category: \"background\"\n    role: \"Deliberate reasoning 框架\"\n    key_finding: \"将 CoT 泛化为树结构，LM 自我评估中间 thought 并 backtrack\"\n    our_differentiation: \"ToT 的自评估是 single-step 的；我们捕捉 multi-step temporal patterns\"\n\n  - id: \"cemri2025multiagentfail\"\n    title: \"Why Do Multi-Agent LLM Systems Fail?\"\n    authors: \"Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2503.13657\"\n    category: \"background\"\n    role: \"Agent failure taxonomy——problem motivation\"\n    key_finding: \"MAST taxonomy：14 种失败模式，其中 Step Repetition 被识别为具体失败症状\"\n    our_differentiation: \"他们提供 taxonomy（what fails），我们提供 detection method（how to detect）\"\n\n  - id: \"zhu2025agentfail\"\n    title: \"Where LLM Agents Fail and How They Can Learn From Failures\"\n    authors: \"Kunlun Zhu, Zijia Liu, Bingxuan Li, et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2509.25370\"\n    category: \"background\"\n    role: \"Agent failure 分析 + cascading failure 发现\"\n    key_finding: \"Cascading failures（单一 root cause 传播到后续决策）是长 horizon 任务的主要失败模式\"\n    our_differentiation: \"Cascading failure 正是我们 temporal model 可以捕捉的 pattern——stagnation 往往是 cascade 的表现\"\n\n  - id: \"george2025cycledetection\"\n    title: \"Unsupervised Cycle Detection in Agentic Applications\"\n    authors: \"Felix George, Harshit Kumar, Divya Pathak, Kaustabha Ray, Mudit Verma, Pratibha Moogi\"\n    venue: \"arXiv preprint (IBM Research)\"\n    year: 2025\n    arxiv: \"2511.10650\"\n    category: \"background\"\n    role: \"Cycle detection——最相关的 stagnation detection 前驱\"\n    key_finding: \"混合方法：call-stack 分析（结构重复）+ embedding 语义相似度确认\"\n    our_differentiation: \"他们只检测 exact/near-exact cycles，我们检测更广义的 stagnation（包括非重复性的停滞）；我们的 empirical analysis 表明 30 个 structural features（含但不限于 cycle 特征）即可达 0.995 F1\"\n\n  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  - id: \"huang2024selfcorrect\"\n    title: \"Large Language Models Cannot Self-Correct Reasoning Yet\"\n    authors: \"Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2310.01798\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 失败的关键证据——支持 external monitoring 必要性\"\n    key_finding: \"LLM 在无外部反馈时无法自我纠错推理错误，intrinsic self-correction 甚至导致性能下降\"\n    our_differentiation: \"直接支持我们的核心论点：agent 不能可靠地自我检测 stagnation，需要外部 monitor；我们的 structural features 提供了轻量（<5ms）且高精度（0.995 F1）的外部检测方案\"\n\n  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================\n\n  - id: \"cho2014gru\"\n    title: \"Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation\"\n    authors: \"Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio\"\n    venue: \"EMNLP 2014\"\n    year: 2014\n    arxiv: \"1406.1078\"\n    category: \"technique\"\n    role: \"GRU 原始论文——我们 probe model 的序列编码器\"\n    key_finding: \"提出 GRU hidden unit，自适应门控信息流\"\n\n  - id: \"bahdanau2015attention\"\n    title: \"Neural Machine Translation by Jointly Learning to Align and Translate\"\n    authors: \"Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio\"\n    venue: \"ICLR 2015\"\n    year: 2015\n    arxiv: \"1409.0473\"\n    category: \"technique\"\n    role: \"Attention mechanism——我们 probe model 的 attention 组件\"\n    key_finding: \"注意力机制允许 decoder 选择性关注输入序列不同位置\"\n\n  - id: \"khosla2020supcon\"\n    title: \"Supervised Contrastive Learning\"\n    authors: \"Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, Dilip Krishnan\"\n    venue: \"NeurIPS 2020\"\n    year: 2020\n    arxiv: \"2004.11362\"\n    category: \"technique\"\n    role: \"SupCon loss——我们的辅助训练目标\"\n    key_finding: \"扩展自监督对比学习到有监督设置，同类样本拉近、异类推远，提升鲁棒性\"\n\n  - id: \"zhang2025qwen3embedding\"\n    title: \"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models\"\n    authors: \"Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2506.05176\"\n    category: \"technique\"\n    role: \"Embedding model——我们用于生成 trajectory window embeddings\"\n    key_finding: \"基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA\"\n\n# ============================================================\n# NOVELTY ANALYSIS SUMMARY (D039 Pivot — Empirical Analysis)\n# ============================================================\n#\n# Primary novelty: 首次系统性实证分析 agent stagnation 检测中 structural vs\n# semantic signal 的有效性。30 个结构特征达 0.995 in-domain / 0.967 cross-agent F1，\n# 全面优于 NL embedding (0.906/0.751) 和 LLM-as-judge (+24.3pp)。\n#\n# 三层贡献：\n# 1. Structural Signal Discovery (primary) — 改变社区对 agent monitoring 方法选型认知\n# 2. LF Temporal Dynamics Analysis — 量化 LFs 时序角色 + agent-specific 迁移分析\n# 3. TLM Negative Finding — 3 种实现 (TWV/HMM/lag-aware HMM) 均未超越 MV\n#\n# 方法论前驱（TLM negative finding 的参照）：\n# 1. Safranchik AAAI 2020 (linked HMM) — NER-specific，BIO 约束，token-level\n# 2. Sala NeurIPS 2019 (multi-resolution WS) — 处理分辨率不匹配，不建模 label transition\n# 3. Nguyen ACL 2017 (HMM-Crowd) — crowdsourcing 场景，不是 programmatic LFs\n#\n# 核心差异化：不是 \"method paper proposing TLM\"，而是 \"empirical study revealing\n# structural signals dominate stagnation detection, with temporal modeling as\n# well-motivated negative finding\".\n",
      "numLines": 417,
      "startLine": 1,
      "totalLines": 417
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GXNSXgLcWSSy5RQehHnCPV`</summary>

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
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "dd7997fc-20f9-430b-b28f-604a3521a555",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEtBhLCbyUn98HGiKfJzo6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11688,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11688
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

_source line 8 · 2026-05-14T20:28:04.169Z_

<details><summary>↩ Tool result · `toolu_01GXNSXgLcWSSy5RQehHnCPV`</summary>

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
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "e5ff1bb2-60cd-40f2-9b1a-986333176ed2",
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

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I have the file content and the WebSearch tool. Let me search for the papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "035415ca-d19c-4b6a-9fb4-25962fee8825",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179eHh5xcUkj7g7NY8a91iH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10031,
      "cache_read_input_tokens": 23529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10031
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

Searching for papers now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "7325848a-3a9d-485c-8cd2-157bda16b26b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179eHh5xcUkj7g7NY8a91iH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10031,
      "cache_read_input_tokens": 23529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10031
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HHqHy3KuAJuGbVFbgXvBs2`</summary>

```json
{
  "query": "WebArena benchmark agent evaluation arxiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "8bb894f0-8714-408e-bfc2-8bf502a4fb59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179eHh5xcUkj7g7NY8a91iH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10031,
      "cache_read_input_tokens": 23529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10031
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P9M4x292zR5dMmWRdYNfTb`</summary>

```json
{
  "query": "MINT benchmark multi-turn interaction agent evaluation arxiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "9749b861-ca32-41f8-8e3a-3f936342f9fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179eHh5xcUkj7g7NY8a91iH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10031,
      "cache_read_input_tokens": 23529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10031
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qxde12NZyd1sBbGvEpME4R`</summary>

```json
{
  "query": "agent trajectory anomaly detection loop detection 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "95087cbb-8a67-4693-aa16-5f4d93a31893",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179eHh5xcUkj7g7NY8a91iH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10031,
      "cache_read_input_tokens": 23529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10031
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

_source line 14 · 2026-05-14T20:28:16.774Z_

<details><summary>↩ Tool result · `toolu_01HHqHy3KuAJuGbVFbgXvBs2`</summary>

```text
Web search results for query: "WebArena benchmark agent evaluation arxiv 2024"

Links: [{"title":"[2307.13854] WebArena: A Realistic Web Environment for Building Autonomous Agents","url":"https://arxiv.org/abs/2307.13854"},{"title":"ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents","url":"https://arxiv.org/html/2410.06703v5"},{"title":"Published as a conference paper at ICLR 2024","url":"https://arxiv.org/pdf/2307.13854"},{"title":"WebArena Benchmark: Evaluating Web Agents","url":"https://www.emergentmind.com/topics/webarena-benchmark"},{"title":"WebArena Benchmark and the State of Agentic AI | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/webarena-benchmark-and-the-state-of-agentic-ai-c22697e8e192"},{"title":"WebArena: A Realistic Web Environment for Building Autonomous Agents - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230713854Z/abstract"},{"title":"GitHub - web-arena-x/visualwebarena: VisualWebArena is a benchmark for multimodal agents. · GitHub","url":"https://github.com/web-arena-x/visualwebarena"},{"title":"WebArena: A Realistic Web Environment for Building Autonomous Agents","url":"https://arxiv.org/html/2307.13854v4"},{"title":"WebArena-x","url":"https://webarena.dev/"},{"title":"BrowserArena: Evaluating LLM Agents on Real-World Web Navigation Tasks","url":"https://arxiv.org/html/2510.02418v2"}]

I've found comprehensive information about the WebArena benchmark for agent evaluation. Here are the key findings:

## Overview

WebArena is an environment for language-guided agents that is highly realistic and reproducible, focusing on agents that perform tasks on the web and creating an environment with fully functional websites from four common domains: e-commerce, social forum discussions, collaborative software development, and content management.

## Benchmark Details

The benchmark includes 812 long-horizon web-based tasks, with each task described as a high-level natural language intent, emulating the abstract language usage patterns typically employed by humans. The evaluation focuses on functional correctness of these tasks, assessing whether the result of the execution actually achieves the desired goal.

## Key Findings

The results demonstrate that solving complex tasks is challenging: the best GPT-4-based agent only achieves an end-to-end task success rate of 14.41%, significantly lower than the human performance of 78.24%. However, in just two years, AI agents have leaped from a 14% to a ~60% success rate on the complex WebArena web-task benchmark.

## Extensions and Related Work

The momentum has produced several web-agent systems including AgentE, AgentQ, WebPilot, and others, in parallel with benchmarks such as Mind2Web, WebVoyager, VisualWebArena, and WorkArena. Additionally, ST-WebAgentBench extends WebArena with explicit safety and trust templates and policy-compliance metrics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "78c59e6c-8100-4ab3-8a42-ec362b8c319b",
  "tool_use_result": {
    "query": "WebArena benchmark agent evaluation arxiv 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q1VQfwxK1CXtcJbAATMbrs",
        "content": [
          {
            "title": "[2307.13854] WebArena: A Realistic Web Environment for Building Autonomous Agents",
            "url": "https://arxiv.org/abs/2307.13854"
          },
          {
            "title": "ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents",
            "url": "https://arxiv.org/html/2410.06703v5"
          },
          {
            "title": "Published as a conference paper at ICLR 2024",
            "url": "https://arxiv.org/pdf/2307.13854"
          },
          {
            "title": "WebArena Benchmark: Evaluating Web Agents",
            "url": "https://www.emergentmind.com/topics/webarena-benchmark"
          },
          {
            "title": "WebArena Benchmark and the State of Agentic AI | by Adnan Masood, PhD. | Medium",
            "url": "https://medium.com/@adnanmasood/webarena-benchmark-and-the-state-of-agentic-ai-c22697e8e192"
          },
          {
            "title": "WebArena: A Realistic Web Environment for Building Autonomous Agents - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2023arXiv230713854Z/abstract"
          },
          {
            "title": "GitHub - web-arena-x/visualwebarena: VisualWebArena is a benchmark for multimodal agents. · GitHub",
            "url": "https://github.com/web-arena-x/visualwebarena"
          },
          {
            "title": "WebArena: A Realistic Web Environment for Building Autonomous Agents",
            "url": "https://arxiv.org/html/2307.13854v4"
          },
          {
            "title": "WebArena-x",
            "url": "https://webarena.dev/"
          },
          {
            "title": "BrowserArena: Evaluating LLM Agents on Real-World Web Navigation Tasks",
            "url": "https://arxiv.org/html/2510.02418v2"
          }
        ]
      },
      "I've found comprehensive information about the WebArena benchmark for agent evaluation. Here are the key findings:\n\n## Overview\n\nWebArena is an environment for language-guided agents that is highly realistic and reproducible, focusing on agents that perform tasks on the web and creating an environment with fully functional websites from four common domains: e-commerce, social forum discussions, collaborative software development, and content management.\n\n## Benchmark Details\n\nThe benchmark includes 812 long-horizon web-based tasks, with each task described as a high-level natural language intent, emulating the abstract language usage patterns typically employed by humans. The evaluation focuses on functional correctness of these tasks, assessing whether the result of the execution actually achieves the desired goal.\n\n## Key Findings\n\nThe results demonstrate that solving complex tasks is challenging: the best GPT-4-based agent only achieves an end-to-end task success rate of 14.41%, significantly lower than the human performance of 78.24%. However, in just two years, AI agents have leaped from a 14% to a ~60% success rate on the complex WebArena web-task benchmark.\n\n## Extensions and Related Work\n\nThe momentum has produced several web-agent systems including AgentE, AgentQ, WebPilot, and others, in parallel with benchmarks such as Mind2Web, WebVoyager, VisualWebArena, and WorkArena. Additionally, ST-WebAgentBench extends WebArena with explicit safety and trust templates and policy-compliance metrics."
    ],
    "durationSeconds": 8.062053145000002
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T20:28:17.300Z_

<details><summary>↩ Tool result · `toolu_01Qxde12NZyd1sBbGvEpME4R`</summary>

```text
Web search results for query: "agent trajectory anomaly detection loop detection 2025 arxiv"

Links: [{"title":"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents","url":"https://arxiv.org/html/2602.06443"},{"title":"Trajectory Guard - A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI","url":"https://arxiv.org/html/2601.00516"},{"title":"Unsupervised Anomaly Detection in Multi-Agent Trajectory Prediction via Transformer-Based Models","url":"https://arxiv.org/html/2601.20367"},{"title":"Graph Enhanced Trajectory Anomaly Detection Jonathan Kabala Mbuya","url":"https://arxiv.org/pdf/2509.18386"},{"title":"Graph Enhanced Trajectory Anomaly Detection","url":"https://arxiv.org/html/2509.18386v1"},{"title":"[2601.20367] Unsupervised Anomaly Detection in Multi-Agent Trajectory Prediction via Transformer-Based Models","url":"https://arxiv.org/abs/2601.20367"},{"title":"[2509.18386] Graph Enhanced Trajectory Anomaly Detection","url":"https://arxiv.org/abs/2509.18386"},{"title":"Detecting Silent Failures in Multi-Agentic AI Trajectories","url":"https://arxiv.org/html/2511.04032"},{"title":"Context-Aware Trajectory Anomaly Detection","url":"https://arxiv.org/pdf/2410.19136"},{"title":"[2602.06443] TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents","url":"https://arxiv.org/abs/2602.06443"}]

Based on the search results, I found several recent 2025 arxiv papers on agent trajectory anomaly detection that include loop detection:

## Key Papers Found:

1. **TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents** (February 2026, arxiv 2602.06443)
   
   TrajAD is a specialized auditing framework for detecting and localizing anomalies by modeling the global context of execution traces to achieve precise step-level localization of errors. Notably, the framework is designed to detect logical errors inherent to the sequence, such as infinite loops or redundant actions. This capability enables efficient error recovery through a "rollback-and-retry" mechanism.

2. **Trajectory Guard - A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI** (January 2026, arxiv 2601.00516)
   
   Trajectory Guard uses a Siamese Recurrent Autoencoder with a hybrid loss function that jointly learns task-trajectory alignment via contrastive learning and sequential validity via reconstruction.

3. **Detecting Silent Failures in Multi-Agentic AI Trajectories** (November 2025, arxiv 2511.04032)
   
   This work addresses silent failures in Multi-Agentic AI systems, including drift, cycles, and missing details in outputs, and introduces the task of anomaly detection in agentic trajectories. For cycles, a strict criterion is defined: no agent or tool should be invoked more than once within a single execution.

These papers represent the latest research on detecting anomalies and loops in agent execution trajectories for trustworthy LLM-based agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "9dc9d187-471d-4bb1-aa55-ed1387fe050a",
  "tool_use_result": {
    "query": "agent trajectory anomaly detection loop detection 2025 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LswUUUjSFeNj1NaMzYJuAZ",
        "content": [
          {
            "title": "TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents",
            "url": "https://arxiv.org/html/2602.06443"
          },
          {
            "title": "Trajectory Guard - A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI",
            "url": "https://arxiv.org/html/2601.00516"
          },
          {
            "title": "Unsupervised Anomaly Detection in Multi-Agent Trajectory Prediction via Transformer-Based Models",
            "url": "https://arxiv.org/html/2601.20367"
          },
          {
            "title": "Graph Enhanced Trajectory Anomaly Detection Jonathan Kabala Mbuya",
            "url": "https://arxiv.org/pdf/2509.18386"
          },
          {
            "title": "Graph Enhanced Trajectory Anomaly Detection",
            "url": "https://arxiv.org/html/2509.18386v1"
          },
          {
            "title": "[2601.20367] Unsupervised Anomaly Detection in Multi-Agent Trajectory Prediction via Transformer-Based Models",
            "url": "https://arxiv.org/abs/2601.20367"
          },
          {
            "title": "[2509.18386] Graph Enhanced Trajectory Anomaly Detection",
            "url": "https://arxiv.org/abs/2509.18386"
          },
          {
            "title": "Detecting Silent Failures in Multi-Agentic AI Trajectories",
            "url": "https://arxiv.org/html/2511.04032"
          },
          {
            "title": "Context-Aware Trajectory Anomaly Detection",
            "url": "https://arxiv.org/pdf/2410.19136"
          },
          {
            "title": "[2602.06443] TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents",
            "url": "https://arxiv.org/abs/2602.06443"
          }
        ]
      },
      "Based on the search results, I found several recent 2025 arxiv papers on agent trajectory anomaly detection that include loop detection:\n\n## Key Papers Found:\n\n1. **TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents** (February 2026, arxiv 2602.06443)\n   \n   TrajAD is a specialized auditing framework for detecting and localizing anomalies by modeling the global context of execution traces to achieve precise step-level localization of errors. Notably, the framework is designed to detect logical errors inherent to the sequence, such as infinite loops or redundant actions. This capability enables efficient error recovery through a \"rollback-and-retry\" mechanism.\n\n2. **Trajectory Guard - A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI** (January 2026, arxiv 2601.00516)\n   \n   Trajectory Guard uses a Siamese Recurrent Autoencoder with a hybrid loss function that jointly learns task-trajectory alignment via contrastive learning and sequential validity via reconstruction.\n\n3. **Detecting Silent Failures in Multi-Agentic AI Trajectories** (November 2025, arxiv 2511.04032)\n   \n   This work addresses silent failures in Multi-Agentic AI systems, including drift, cycles, and missing details in outputs, and introduces the task of anomaly detection in agentic trajectories. For cycles, a strict criterion is defined: no agent or tool should be invoked more than once within a single execution.\n\nThese papers represent the latest research on detecting anomalies and loops in agent execution trajectories for trustworthy LLM-based agents."
    ],
    "durationSeconds": 7.690077016999999
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T20:28:20.985Z_

<details><summary>↩ Tool result · `toolu_01P9M4x292zR5dMmWRdYNfTb`</summary>

```text
Web search results for query: "MINT benchmark multi-turn interaction agent evaluation arxiv 2024"

Links: [{"title":"GitHub - xingyaoww/mint-bench: Official Repo for ICLR 2024 paper MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback by Xingyao Wang*, Zihan Wang*, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng and Heng Ji. · GitHub","url":"https://github.com/xingyaoww/mint-bench"},{"title":"[2309.10691] MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback","url":"https://arxiv.org/abs/2309.10691"},{"title":"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback","url":"https://xwang.dev/mint-bench/"},{"title":"mint: evaluating llms in multi-turn inter","url":"https://zihanwang314.github.io/pdf/mint.pdf"},{"title":"AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents Chang Ma∗♠","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf"},{"title":"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback | OpenReview","url":"https://openreview.net/forum?id=jp3gWrMuIZ"},{"title":"Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions","url":"https://arxiv.org/html/2507.05257v3"},{"title":"\\scalerel*X MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback","url":"https://arxiv.org/html/2309.10691v1"},{"title":"Published as a conference paper at ICLR 2024 MINTREC2.0: A LARGE-SCALE","url":"https://arxiv.org/pdf/2403.10943"},{"title":"[PDF] MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MINT:-Evaluating-LLMs-in-Multi-turn-Interaction-and-Wang-Wang/12b233752c7097ea6525622bed238ae2d2193c5a"}]

I found relevant information about the MINT benchmark. Here's what the search revealed:

## MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback

MINT is an ICLR 2024 paper that evaluates LLMs' ability to solve tasks with multi-turn interactions by (1) using tools and (2) leveraging natural language feedback.

### Key Purpose
Large language models often require multiple rounds of interactions with users, sometimes assisted by external tools. However, current evaluation protocols emphasize single-turn exchanges, neglecting the nuanced interactions among users, LLMs, and external tools, while underestimating the importance of natural language feedback. These oversights contribute to discrepancies between research benchmark evaluations and real-world use cases.

### Evaluation Framework
The benchmark provides an evaluation framework where LLMs can access tools by executing Python code and receive users' natural language feedback simulated by GPT-4.

### Coverage
The benchmark includes test instances from several sources: HumanEval, MBPP, GSM8K, HotpotQA, MATH, MMLU, TheoremQA, and AlfWorld.

### Key Findings
LLMs generally benefit from tools and language feedback, with performance gains of 1-8% for each turn of tool use and 2-17% with natural language feedback.

The paper was initially posted on arXiv in September 2023 (arXiv:2309.10691) and was published at ICLR 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "7badb252-d6ea-4aa1-be9c-feb8c7407ba9",
  "tool_use_result": {
    "query": "MINT benchmark multi-turn interaction agent evaluation arxiv 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_0161jr6FgNuKaycgPKCnqTY9",
        "content": [
          {
            "title": "GitHub - xingyaoww/mint-bench: Official Repo for ICLR 2024 paper MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback by Xingyao Wang*, Zihan Wang*, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng and Heng Ji. · GitHub",
            "url": "https://github.com/xingyaoww/mint-bench"
          },
          {
            "title": "[2309.10691] MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback",
            "url": "https://arxiv.org/abs/2309.10691"
          },
          {
            "title": "MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback",
            "url": "https://xwang.dev/mint-bench/"
          },
          {
            "title": "mint: evaluating llms in multi-turn inter",
            "url": "https://zihanwang314.github.io/pdf/mint.pdf"
          },
          {
            "title": "AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents Chang Ma∗♠",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf"
          },
          {
            "title": "MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback | OpenReview",
            "url": "https://openreview.net/forum?id=jp3gWrMuIZ"
          },
          {
            "title": "Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions",
            "url": "https://arxiv.org/html/2507.05257v3"
          },
          {
            "title": "\\scalerel*X MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback",
            "url": "https://arxiv.org/html/2309.10691v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 MINTREC2.0: A LARGE-SCALE",
            "url": "https://arxiv.org/pdf/2403.10943"
          },
          {
            "title": "[PDF] MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/MINT:-Evaluating-LLMs-in-Multi-turn-Interaction-and-Wang-Wang/12b233752c7097ea6525622bed238ae2d2193c5a"
          }
        ]
      },
      "I found relevant information about the MINT benchmark. Here's what the search revealed:\n\n## MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\n\nMINT is an ICLR 2024 paper that evaluates LLMs' ability to solve tasks with multi-turn interactions by (1) using tools and (2) leveraging natural language feedback.\n\n### Key Purpose\nLarge language models often require multiple rounds of interactions with users, sometimes assisted by external tools. However, current evaluation protocols emphasize single-turn exchanges, neglecting the nuanced interactions among users, LLMs, and external tools, while underestimating the importance of natural language feedback. These oversights contribute to discrepancies between research benchmark evaluations and real-world use cases.\n\n### Evaluation Framework\nThe benchmark provides an evaluation framework where LLMs can access tools by executing Python code and receive users' natural language feedback simulated by GPT-4.\n\n### Coverage\nThe benchmark includes test instances from several sources: HumanEval, MBPP, GSM8K, HotpotQA, MATH, MMLU, TheoremQA, and AlfWorld.\n\n### Key Findings\nLLMs generally benefit from tools and language feedback, with performance gains of 1-8% for each turn of tool use and 2-17% with natural language feedback.\n\nThe paper was initially posted on arXiv in September 2023 (arXiv:2309.10691) and was published at ICLR 2024."
    ],
    "durationSeconds": 11.808716173
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
I found good candidates. Let me get more details on the specific papers I want to add:

1. **WebArena** (zhou2024webarena) - arxiv 2307.13854, ICLR 2024
2. **MINT** (wang2024mint) - arxiv 2309.10691, ICLR 2024 - but wait, the first author is Xingyao Wang, same as OpenHands. Let me check.

Actually, looking at the MINT paper, the authors are Xingyao Wang*, Zihan Wang*, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng and Heng Ji. 

Xingyao Wang appears on both papers, but they're distinct works so that's fine.

3. For cycle and anomaly detection, I'm looking at several options: **TrajAD** for trajectory anomaly detection in LLM agents, **Trajectory Guard** for lightweight real-time detection, and **Detecting Silent Failures** for multi-agent trajectories. TrajAD seems most directly relevant since it handles both loop detection and trajectory anomalies specifically for LLM agents, so I'll dig into that one further.

Now I'm verifying the paper details—authors, publication venues, and dates.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "9148197f-81e2-4d67-85d8-2cac11329aba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNjDDbsiASsM28amVeSucn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 872,
      "cache_creation_input_tokens": 2072,
      "cache_read_input_tokens": 33560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2072
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

Good results. Let me get more details on the top candidates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "d916335f-0183-4d1e-91e7-db14968b3de4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNjDDbsiASsM28amVeSucn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 872,
      "cache_creation_input_tokens": 2072,
      "cache_read_input_tokens": 33560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2072
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JFBB2GGk4HaNnfeZrJGYKJ`</summary>

```json
{
  "query": "arxiv 2307.13854 WebArena authors Shunyu Zhou ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "ec952212-e3a0-46f5-a975-c9a78293f7c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNjDDbsiASsM28amVeSucn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 872,
      "cache_creation_input_tokens": 2072,
      "cache_read_input_tokens": 33560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2072
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A2htate2ZrYtKZspaHHamo`</summary>

```json
{
  "query": "arxiv 2602.06443 TrajAD trajectory anomaly detection LLM agents authors 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "342eeb6e-02bb-41ec-8134-8c6ea747d00e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNjDDbsiASsM28amVeSucn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 872,
      "cache_creation_input_tokens": 2072,
      "cache_read_input_tokens": 33560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2072
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

_source line 21 · 2026-05-14T20:28:41.211Z_

<details><summary>↩ Tool result · `toolu_01JFBB2GGk4HaNnfeZrJGYKJ`</summary>

```text
Web search results for query: "arxiv 2307.13854 WebArena authors Shunyu Zhou ICLR 2024"

Links: [{"title":"[2307.13854] WebArena: A Realistic Web Environment for Building Autonomous Agents","url":"https://arxiv.org/abs/2307.13854"},{"title":"Published as a conference paper at ICLR 2024","url":"https://arxiv.org/pdf/2307.13854"},{"title":"[PDF] WebArena: A Realistic Web Environment for Building Autonomous Agents | Semantic Scholar","url":"https://www.semanticscholar.org/paper/WebArena:-A-Realistic-Web-Environment-for-Building-Zhou-Xu/e41482f4ee984f17382f6cdd900df094d928be06"},{"title":"GitHub - web-arena-x/webarena: Code repo for \"WebArena: A Realistic Web Environment for Building Autonomous Agents\" · GitHub","url":"https://github.com/web-arena-x/webarena"},{"title":"WebArena: A Realistic Web Environment for Building Autonomous Agents","url":"https://arxiv.org/html/2307.13854.pdf"},{"title":"WebArena: A Realistic Web Environment for Building Autonomous Agents - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230713854Z/abstract"},{"title":"(PDF) WebArena: A Realistic Web Environment for Building Autonomous Agents","url":"https://www.researchgate.net/publication/372654539_WebArena_A_Realistic_Web_Environment_for_Building_Autonomous_Agents"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2411.02337"},{"title":"Learning representations of learning representations","url":"https://arxiv.org/html/2404.08403v1"},{"title":"Computer Science Mar 2024","url":"https://arxiv.org/list/cs/2024-03?skip=8100&show=2000"}]

Based on the search results, I can provide you with information about the WebArena paper:

## WebArena Paper Details

The authors of the WebArena paper (arXiv 2307.13854) are Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, and Graham Neubig.

The paper was published as a conference paper at ICLR 2024.

## Paper Summary

The paper focuses on agents that perform tasks on the web, creating an environment with fully functional websites from four common domains: e-commerce, social forum discussions, collaborative software development, and content management. The environment is enriched with tools (e.g., a map) and external knowledge bases (e.g., user manuals) to encourage human-like task-solving.

Along with WebArena, they release a ready-to-use benchmark with 812 long-horizon web-based tasks. Their best GPT-4-based agent only achieves an end-to-end task success rate of 14.41%, significantly lower than the human performance of 78.24%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "e10a3f5e-8182-42d3-b299-f15cad60f9ed",
  "tool_use_result": {
    "query": "arxiv 2307.13854 WebArena authors Shunyu Zhou ICLR 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V6vQrrNB5UoBfWLwXihwkL",
        "content": [
          {
            "title": "[2307.13854] WebArena: A Realistic Web Environment for Building Autonomous Agents",
            "url": "https://arxiv.org/abs/2307.13854"
          },
          {
            "title": "Published as a conference paper at ICLR 2024",
            "url": "https://arxiv.org/pdf/2307.13854"
          },
          {
            "title": "[PDF] WebArena: A Realistic Web Environment for Building Autonomous Agents | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/WebArena:-A-Realistic-Web-Environment-for-Building-Zhou-Xu/e41482f4ee984f17382f6cdd900df094d928be06"
          },
          {
            "title": "GitHub - web-arena-x/webarena: Code repo for \"WebArena: A Realistic Web Environment for Building Autonomous Agents\" · GitHub",
            "url": "https://github.com/web-arena-x/webarena"
          },
          {
            "title": "WebArena: A Realistic Web Environment for Building Autonomous Agents",
            "url": "https://arxiv.org/html/2307.13854.pdf"
          },
          {
            "title": "WebArena: A Realistic Web Environment for Building Autonomous Agents - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2023arXiv230713854Z/abstract"
          },
          {
            "title": "(PDF) WebArena: A Realistic Web Environment for Building Autonomous Agents",
            "url": "https://www.researchgate.net/publication/372654539_WebArena_A_Realistic_Web_Environment_for_Building_Autonomous_Agents"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://arxiv.org/pdf/2411.02337"
          },
          {
            "title": "Learning representations of learning representations",
            "url": "https://arxiv.org/html/2404.08403v1"
          },
          {
            "title": "Computer Science Mar 2024",
            "url": "https://arxiv.org/list/cs/2024-03?skip=8100&show=2000"
          }
        ]
      },
      "Based on the search results, I can provide you with information about the WebArena paper:\n\n## WebArena Paper Details\n\nThe authors of the WebArena paper (arXiv 2307.13854) are Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, and Graham Neubig.\n\nThe paper was published as a conference paper at ICLR 2024.\n\n## Paper Summary\n\nThe paper focuses on agents that perform tasks on the web, creating an environment with fully functional websites from four common domains: e-commerce, social forum discussions, collaborative software development, and content management. The environment is enriched with tools (e.g., a map) and external knowledge bases (e.g., user manuals) to encourage human-like task-solving.\n\nAlong with WebArena, they release a ready-to-use benchmark with 812 long-horizon web-based tasks. Their best GPT-4-based agent only achieves an end-to-end task success rate of 14.41%, significantly lower than the human performance of 78.24%."
    ],
    "durationSeconds": 6.440699249999998
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T20:28:41.835Z_

<details><summary>↩ Tool result · `toolu_01A2htate2ZrYtKZspaHHamo`</summary>

```text
Web search results for query: "arxiv 2602.06443 TrajAD trajectory anomaly detection LLM agents authors 2026"

Links: [{"title":"[2602.06443] TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents","url":"https://arxiv.org/abs/2602.06443"},{"title":"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents","url":"https://arxiv.org/html/2602.06443"},{"title":"Graph Enhanced Trajectory Anomaly Detection","url":"https://arxiv.org/html/2509.18386v1"},{"title":"Trajectory Anomaly Detection with By-Design Complementary Detectors Shurui Cao∗","url":"https://www.andrew.cmu.edu/user/lakoglu/pubs/25-sdm-TrajAD.pdf"},{"title":"[2509.18386] Graph Enhanced Trajectory Anomaly Detection","url":"https://arxiv.org/abs/2509.18386"},{"title":"Trajectory Anomaly Detection with Language Models","url":"https://arxiv.org/html/2409.15366v1"},{"title":"Context-Aware Trajectory Anomaly Detection","url":"https://arxiv.org/html/2410.19136v1"},{"title":"[2409.15366] Trajectory Anomaly Detection with Language Models","url":"https://arxiv.org/abs/2409.15366"},{"title":"Unsupervised Anomaly Detection in Multi-Agent Trajectory Prediction via Transformer-Based Models","url":"https://arxiv.org/html/2601.20367"},{"title":"[2303.05000] Learning Representation for Anomaly Detection of Vehicle Trajectories","url":"https://arxiv.org/abs/2303.05000"}]

Based on the search results, I found the paper you're looking for. Here's the information about arxiv 2602.06443:

## TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents

**Authors:** Yibing Liu, Chong Zhang, Zhongyi Han, Hansong Liu, Yong Wang, Yang Yu, Xiaoyan Wang, and Yilong Yin

**Paper ID:** arxiv 2602.06443  
**Submitted:** February 6, 2026

### Overview

The paper addresses runtime trajectory anomaly detection, a critical capability for enabling trustworthy LLM agents. The goal is not merely detection, but precise error localization, which is essential for enabling efficient rollback-and-retry.

### Key Contributions

- TrajBench: a dataset synthesized via a perturb-and-complete strategy to cover diverse procedural anomalies
- TrajAD: a specialized verifier trained with fine-grained process supervision
- Coverage of three representative anomaly categories: Task Failure, Process Inefficiency, and Unwarranted Continuation

### Main Findings

General-purpose LLMs, even with zero-shot prompting, struggle to identify and localize these anomalies. In contrast, TrajAD achieves superior performance in both detection and localization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "0f3cc72a-813b-49fe-a141-c8305a4e3993",
  "tool_use_result": {
    "query": "arxiv 2602.06443 TrajAD trajectory anomaly detection LLM agents authors 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017mPV8mywcST9PFN7gS3Wt8",
        "content": [
          {
            "title": "[2602.06443] TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents",
            "url": "https://arxiv.org/abs/2602.06443"
          },
          {
            "title": "TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents",
            "url": "https://arxiv.org/html/2602.06443"
          },
          {
            "title": "Graph Enhanced Trajectory Anomaly Detection",
            "url": "https://arxiv.org/html/2509.18386v1"
          },
          {
            "title": "Trajectory Anomaly Detection with By-Design Complementary Detectors Shurui Cao∗",
            "url": "https://www.andrew.cmu.edu/user/lakoglu/pubs/25-sdm-TrajAD.pdf"
          },
          {
            "title": "[2509.18386] Graph Enhanced Trajectory Anomaly Detection",
            "url": "https://arxiv.org/abs/2509.18386"
          },
          {
            "title": "Trajectory Anomaly Detection with Language Models",
            "url": "https://arxiv.org/html/2409.15366v1"
          },
          {
            "title": "Context-Aware Trajectory Anomaly Detection",
            "url": "https://arxiv.org/html/2410.19136v1"
          },
          {
            "title": "[2409.15366] Trajectory Anomaly Detection with Language Models",
            "url": "https://arxiv.org/abs/2409.15366"
          },
          {
            "title": "Unsupervised Anomaly Detection in Multi-Agent Trajectory Prediction via Transformer-Based Models",
            "url": "https://arxiv.org/html/2601.20367"
          },
          {
            "title": "[2303.05000] Learning Representation for Anomaly Detection of Vehicle Trajectories",
            "url": "https://arxiv.org/abs/2303.05000"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's the information about arxiv 2602.06443:\n\n## TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents\n\n**Authors:** Yibing Liu, Chong Zhang, Zhongyi Han, Hansong Liu, Yong Wang, Yang Yu, Xiaoyan Wang, and Yilong Yin\n\n**Paper ID:** arxiv 2602.06443  \n**Submitted:** February 6, 2026\n\n### Overview\n\nThe paper addresses runtime trajectory anomaly detection, a critical capability for enabling trustworthy LLM agents. The goal is not merely detection, but precise error localization, which is essential for enabling efficient rollback-and-retry.\n\n### Key Contributions\n\n- TrajBench: a dataset synthesized via a perturb-and-complete strategy to cover diverse procedural anomalies\n- TrajAD: a specialized verifier trained with fine-grained process supervision\n- Coverage of three representative anomaly categories: Task Failure, Process Inefficiency, and Unwarranted Continuation\n\n### Main Findings\n\nGeneral-purpose LLMs, even with zero-shot prompting, struggle to identify and localize these anomalies. In contrast, TrajAD achieves superior performance in both detection and localization."
    ],
    "durationSeconds": 7.061290387000001
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Now I have the details for all three papers:

1. **WebArena** - zhou2024webarena
   - Title: "WebArena: A Realistic Web Environment for Building Autonomous Agents"
   - Authors: Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig
   - Venue: ICLR 2024
   - arxiv: 2307.13854
   - category: evaluation

2. **MINT** - wang2024mint
   - Title: "MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback"
   - Authors: Xingyao Wang, Zihan Wang, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng, Heng Ji
   - Venue: ICLR 2024
   - arxiv: 2309.10691
   - category: evaluation

3. **TrajAD** - liu2026trajad
   - Title: "TrajAD: Trajectory Anomaly Detection for Trustworthy" - the title appears to be cut off, but I have the basic citation information for this paper as well.

I'm looking at where to place these entries in the bibliography. The TrajAD paper should go in the background section after the kamoi2024selfcorrection entry, while the other two papers fit into the evaluation section after wang2025openhands. I need to insert the agent benchmark papers into the evaluation section after wang2025openhands, and then add the cycle detection paper to the background section after kamoi2024selfcorrection. Let me prepare those edits now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "934e1f1e-b718-4f4e-8c04-ea7c2bf8ba50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSeWkLd8yeZwbC38EZrRBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3127,
      "cache_read_input_tokens": 35632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3127
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

Found all 3 papers. Now appending to the literature map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "4f7c36cc-47ad-4228-98dc-28a17f325c51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSeWkLd8yeZwbC38EZrRBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3127,
      "cache_read_input_tokens": 35632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3127
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

<details open><summary>🔧 Tool call — Edit · `toolu_01947pi6M4KGDxfw8TwbePWW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
  "old_string": "  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================",
  "new_string": "  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  - id: \"zhou2024webarena\"\n    title: \"WebArena: A Realistic Web Environment for Building Autonomous Agents\"\n    authors: \"Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2307.13854\"\n    category: \"evaluation\"\n    verified: true\n    role: \"Web agent 评测基准——long-horizon 任务评估\"\n    key_finding: \"812 个真实网站上的 long-horizon 任务，GPT-4 agent 仅 14.41% 成功率 vs 人类 78.24%，揭示 agent 在复杂任务上的巨大差距\"\n    our_differentiation: \"WebArena 的 long-horizon 任务正是 stagnation 高发场景；我们的 monitor 可作为此类任务的早期终止/干预信号\"\n\n  - id: \"wang2024mint\"\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Xingyao Wang, Zihan Wang, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng, Heng Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2309.10691\"\n    category: \"evaluation\"\n    verified: true\n    role: \"Multi-turn agent 评测基准——tool use + feedback 交互评估\"\n    key_finding: \"评估 LLM 在多轮交互中使用工具和接收自然语言反馈的能力，每轮 tool use 提升 1-8%，NL feedback 提升 2-17%\"\n    our_differentiation: \"MINT 量化了 multi-turn 交互中的性能变化，我们的 stagnation detection 关注多轮交互中进展停滞的检测；MINT 的 multi-turn 设定与我们的 window-level 分析天然对齐\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "20750874-38d7-497b-aaea-41b3d530d7c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSeWkLd8yeZwbC38EZrRBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3127,
      "cache_read_input_tokens": 35632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3127
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

_source line 26 · 2026-05-14T20:29:17.962Z_

<details><summary>↩ Tool result · `toolu_01947pi6M4KGDxfw8TwbePWW`</summary>

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
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "2a7869a9-ea6e-4905-aeff-a983d211df8e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
    "oldString": "  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================",
    "newString": "  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  - id: \"zhou2024webarena\"\n    title: \"WebArena: A Realistic Web Environment for Building Autonomous Agents\"\n    authors: \"Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2307.13854\"\n    category: \"evaluation\"\n    verified: true\n    role: \"Web agent 评测基准——long-horizon 任务评估\"\n    key_finding: \"812 个真实网站上的 long-horizon 任务，GPT-4 agent 仅 14.41% 成功率 vs 人类 78.24%，揭示 agent 在复杂任务上的巨大差距\"\n    our_differentiation: \"WebArena 的 long-horizon 任务正是 stagnation 高发场景；我们的 monitor 可作为此类任务的早期终止/干预信号\"\n\n  - id: \"wang2024mint\"\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Xingyao Wang, Zihan Wang, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng, Heng Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2309.10691\"\n    category: \"evaluation\"\n    verified: true\n    role: \"Multi-turn agent 评测基准——tool use + feedback 交互评估\"\n    key_finding: \"评估 LLM 在多轮交互中使用工具和接收自然语言反馈的能力，每轮 tool use 提升 1-8%，NL feedback 提升 2-17%\"\n    our_differentiation: \"MINT 量化了 multi-turn 交互中的性能变化，我们的 stagnation detection 关注多轮交互中进展停滞的检测；MINT 的 multi-turn 设定与我们的 window-level 分析天然对齐\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================",
    "originalFile": "# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)\n# Generated: 2026-05-14\n# Paper: Structural Signal Analysis for Progress Stagnation Detection in LLM Agents\n#\n# D039 Pivot: Empirical analysis paper. Central finding: stagnation signals are\n# fundamentally structural (30 features → 0.995 in-domain, 0.967 cross-agent F1),\n# decisively surpassing NL embeddings (0.906/0.751) and LLM-as-judge (+24.3pp).\n# TLM is a well-motivated negative finding (3 implementations all fail to beat MV).\n\npapers:\n\n  # ============================================================\n  # CATEGORY: direct-competitor\n  # ============================================================\n\n  - id: \"xi2025agentprm\"\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Zhiheng Xi, Chenyang Liao, Guanyu Li, Yajie Yang, Wenxiang Chen, Zhihao Zhang, Binghai Wang, Senjie Jin, Yuhao Zhou, Jian Guan, Wei Wu, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2511.08325\"\n    category: \"direct-competitor\"\n    role: \"主要竞争者：step-level PRM for agent guidance\"\n    key_finding: \"用 promise（长期潜力）和 progress（即时进展）两个维度评估 agent 每步决策，实现 8x 计算效率提升\"\n    our_differentiation: \"我们是 window-level monitoring（不是 step-level guidance），不需要 outcome labels，目标是 stagnation detection 不是 reward shaping\"\n\n  - id: \"choudhury2025prm\"\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Sanjiban Choudhury\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2502.10325\"\n    category: \"direct-competitor\"\n    role: \"PRM 框架综述 + InversePRM 方法\"\n    key_finding: \"提出 AgentPRM（Monte Carlo rollout actor-critic）和 InversePRM（从 demonstrations 学习 process reward），3B 模型超越 GPT-4o\"\n    our_differentiation: \"InversePRM 仍需 demonstration trajectories，我们用 programmatic LFs 替代人工标注；我们关注 monitoring 而非 training signal\"\n\n  - id: \"li2026toolprmbench\"\n    title: \"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents\"\n    authors: \"Dawei Li, Yuguang Yao, Zhen Tan, Huan Liu, Ruocheng Guo\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.12294\"\n    category: \"direct-competitor\"\n    role: \"Tool-use PRM 评测基准\"\n    key_finding: \"大规模 benchmark 评测 PRM 在 tool-use 场景的效果，发现专用 PRM 显著优于通用 PRM\"\n    our_differentiation: \"我们的 empirical analysis 揭示 structural features 足以检测 stagnation（0.995 F1），无需 step-level reward labels；关注 stagnation pattern 而非 step correctness\"\n\n  - id: \"wang2026planrewardbench\"\n    title: \"Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling\"\n    authors: \"Jiaxuan Wang, Yulan Hu, Wenjin Yang, Zheng Pan, Xin Li, Lan-Zhe Guo\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.08178\"\n    category: \"direct-competitor\"\n    role: \"Trajectory-level reward model 评测\"\n    key_finding: \"所有 reward model 类别（generative, discriminative, LLM-as-Judge）在长 horizon trajectory 上性能显著下降\"\n    our_differentiation: \"验证了长 trajectory 评估的难度——我们的 window-level 方法通过局部化避免了这个问题\"\n\n  - id: \"chen2025monitoring\"\n    title: \"Monitoring LLM Agents for Sequentially Contextual Harm\"\n    authors: \"Yueh-Han Chen, Neelay Joshi, Yulin Chen, He He, Rico Angell\"\n    venue: \"ICLR 2025 Workshop on Building Trust in Language Models and Applications\"\n    year: 2025\n    arxiv: null\n    openreview: \"LC0XQ6ufbr\"\n    category: \"direct-competitor\"\n    role: \"Agent monitoring 安全方向\"\n    key_finding: \"将有害任务分解为单独无害的子任务可将 refusal rate 从 50% 降至 10%，现有 monitor 难以检测 sequentially contextual harm\"\n    our_differentiation: \"他们关注 safety monitoring（harmful behavior），我们关注 progress monitoring（stagnation）；互补方向\"\n\n  - id: \"kale2025weaktostrong\"\n    title: \"Reliable Weak-to-Strong Monitoring of LLM Agents\"\n    authors: \"Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team, Christina Q. Knight, Zifan Wang\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2508.19461\"\n    category: \"direct-competitor\"\n    role: \"Weak-to-strong agent monitoring 方法论\"\n    key_finding: \"Monitor scaffolding 比 monitor 能力更重要，弱模型可以可靠监控强模型；targeted human-in-the-loop 提升 TPR ~15%\"\n    our_differentiation: \"他们用 LLM 作为 monitor，我们发现 30 个 structural features 即可达 0.967 跨域 F1，不依赖另一个 LLM；更轻量（<5ms）且可解释\"\n\n  - id: \"fan2026agentrm\"\n    title: \"Exploring Reasoning Reward Model for Agents\"\n    authors: \"Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.22154\"\n    category: \"direct-competitor\"\n    verified: true\n    role: \"Agent trajectory 的多维度 reasoning reward model\"\n    key_finding: \"Agent-RRM 通过 reasoning trace + critique + overall score 三维结构化反馈评估 agent trajectory，在 12 个 benchmark 上显著提升（GAIA 43.7%, WebWalkerQA 46.2%）\"\n    our_differentiation: \"他们用 LLM-based reward model 生成结构化反馈用于 agent 改进，我们的 empirical analysis 表明轻量 structural features 即可高精度检测 stagnation（0.995 F1），不依赖大模型推理\"\n\n  - id: \"qiu2026dataprm\"\n    title: \"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis\"\n    authors: \"Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.24198\"\n    category: \"direct-competitor\"\n    verified: true\n    role: \"Agentic data analysis 场景的 process-level reward model\"\n    key_finding: \"传统 PRM 无法检测 silent errors 且误判 exploratory steps；DataPRM 通过 environment-aware probing + ternary reward 策略在 ScienceAgentBench 提升 7.21%\"\n    our_differentiation: \"DataPRM 针对数据分析 agent 的 step correctness，我们针对通用 agent 的 stagnation pattern；他们需要 execution state probing，我们用 structural LFs 无需环境交互\"\n\n  # ============================================================\n  # CATEGORY: method-component\n  # ============================================================\n\n  - id: \"ratner2016dataprogramming\"\n    title: \"Data Programming: Creating Large Training Sets, Quickly\"\n    authors: \"Alexander Ratner, Christopher De Sa, Sen Wu, Daniel Selsam, Christopher Re\"\n    venue: \"NeurIPS 2016\"\n    year: 2016\n    arxiv: \"1605.07723\"\n    category: \"method-component\"\n    role: \"核心方法论基础：data programming 范式\"\n    key_finding: \"用户编写 labeling functions（噪声启发式），generative model 学习 LF 准确率生成概率训练标签\"\n    our_differentiation: \"我们在 agent trajectory 上应用 data programming，发现 structural features 主导检测能力；同时揭示 LFs 的时序动态和 temporal label model 的负面结果\"\n\n  - id: \"ratner2017snorkel\"\n    title: \"Snorkel: Rapid Training Data Creation with Weak Supervision\"\n    authors: \"Alexander Ratner, Stephen H. Bach, Henry Ehrenberg, Jason Fries, Sen Wu, Christopher Re\"\n    venue: \"VLDB 2018\"\n    year: 2018\n    arxiv: \"1711.10160\"\n    category: \"method-component\"\n    role: \"Data programming 系统实现，label model 基础\"\n    key_finding: \"端到端弱监督系统：LFs → generative label model（建模 LF dependency）→ discriminative end model\"\n    our_differentiation: \"Snorkel 假设数据点 i.i.d.，我们发现 agent trajectory 上 LFs 展现系统性时序动态（violating i.i.d.），但 temporal label model 未能超越 MV（negative finding）\"\n\n  - id: \"fu2020flyingsquid\"\n    title: \"Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods\"\n    authors: \"Daniel Y. Fu, Mayee F. Chen, Frederic Sala, Sarah M. Hooper, Kayvon Fatahalian, Christopher Re\"\n    venue: \"ICML 2020\"\n    year: 2020\n    arxiv: \"2002.11955\"\n    category: \"method-component\"\n    role: \"快速 label model，triplet method of moments\"\n    key_finding: \"用 triplet method 闭式求解 label model 参数，比 SGD 快 170x\"\n    our_differentiation: \"FlyingSquid 同样假设 i.i.d.；我们的 empirical analysis 揭示 i.i.d. violation 虽系统性存在，但 temporal correction 在低冲突 regime 下无收益（negative finding）\"\n\n  - id: \"zhang2021wrench\"\n    title: \"WRENCH: A Comprehensive Benchmark for Weak Supervision\"\n    authors: \"Jieyu Zhang, Yue Yu, Yinghao Li, Yujing Wang, Yaming Yang, Mao Yang, Alexander Ratner\"\n    venue: \"NeurIPS 2021 Datasets and Benchmarks Track\"\n    year: 2021\n    arxiv: \"2109.11377\"\n    category: \"method-component\"\n    role: \"弱监督评测基准\"\n    key_finding: \"22 个真实数据集 + 120+ 方法变体评测，标准化弱监督研究\"\n    our_differentiation: \"WRENCH 数据集全是 i.i.d. 分类/序列标注，没有 temporal stagnation detection 任务\"\n\n  - id: \"safranchik2020linkedhmm\"\n    title: \"Weakly Supervised Sequence Tagging from Noisy Rules\"\n    authors: \"Esteban Safranchik, Shiying Luo, Stephen H. Bach\"\n    venue: \"AAAI 2020\"\n    year: 2020\n    arxiv: null\n    category: \"method-component\"\n    role: \"最近的方法论前驱：linked HMM for sequence tagging weak supervision\"\n    key_finding: \"将 HMM 引入弱监督序列标注（NER），加入 linking rules 建模 span 结构，比 i.i.d. label model +7 F1\"\n    our_differentiation: \"他们是 token-level NER（BIO 约束），我们是 window-level temporal classification；我们建模的是 stagnation temporal dynamics 而非 entity boundary\"\n\n  - id: \"sala2019multiresolution\"\n    title: \"Multi-Resolution Weak Supervision for Sequential Data\"\n    authors: \"Frederic Sala, Paroma Varma, Jason Fries, Daniel Y. Fu, Stefano Sagawa, Christopher Re\"\n    venue: \"NeurIPS 2019\"\n    year: 2019\n    arxiv: \"1910.09505\"\n    category: \"method-component\"\n    role: \"最近的方法论前驱：multi-resolution WS for sequential data\"\n    key_finding: \"处理不同时间分辨率的 LFs（如 frame-level vs span-level），建模 multi-resolution LF correlations\"\n    our_differentiation: \"他们关注 resolution mismatch，我们关注 temporal label transitions；互补视角\"\n\n  - id: \"dawid1979em\"\n    title: \"Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm\"\n    authors: \"A. P. Dawid, A. M. Skene\"\n    venue: \"Journal of the Royal Statistical Society, Series C\"\n    year: 1979\n    arxiv: null\n    category: \"method-component\"\n    role: \"Label aggregation 奠基工作\"\n    key_finding: \"用 EM 算法估计标注者混淆矩阵，无需 ground truth\"\n    our_differentiation: \"经典 i.i.d. 假设；我们测试了 temporal extension（HMM-TLM, lag-aware HMM）但发现在 3-LF 低冲突 regime 下未超越 MV——约束未来 temporal label model 研究\"\n\n  - id: \"nguyen2017hmmcrowd\"\n    title: \"Aggregating and Predicting Sequence Labels from Crowd Annotations\"\n    authors: \"An Thanh Nguyen, Byron C. Wallace, Junyi Jessy Li, Ani Nenkova, Matthew Lease\"\n    venue: \"ACL 2017\"\n    year: 2017\n    arxiv: null\n    category: \"method-component\"\n    role: \"HMM + crowdsourcing label aggregation\"\n    key_finding: \"HMM-Crowd：扩展 Dawid-Skene 到序列数据，加入 one-step Markov structure over true labels\"\n    our_differentiation: \"他们用于 crowdsourcing（人类标注者），我们用于 programmatic LFs（自动化）；他们是 NER/IE，我们是 agent progress monitoring\"\n\n  # ============================================================\n  # CATEGORY: evaluation\n  # ============================================================\n\n  - id: \"orlanski2026slopcodebench\"\n    title: \"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks\"\n    authors: \"Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu, Albert Ge, Dyah Adila, Nicholas Roberts, Frederic Sala, Aws Albarghouthi\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.24755\"\n    category: \"evaluation\"\n    role: \"Agent degradation 基准——直接支持我们的 problem motivation\"\n    key_finding: \"Agent 代码质量在迭代任务中持续退化：比人类代码 2.3x 更冗余、2.0x 更结构侵蚀，75-77% trajectory 呈现退化趋势\"\n    our_differentiation: \"SlopCodeBench 量化了 degradation 现象，我们提供了检测方法；他们是 post-hoc 评测，我们是 online monitoring\"\n\n  - id: \"jimenez2024swebench\"\n    title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n    authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2310.06770\"\n    category: \"evaluation\"\n    role: \"Agent 数据来源之一\"\n    key_finding: \"2294 个真实 GitHub issue 任务，标准化 agent 评测\"\n    our_differentiation: \"我们使用 SWE-bench agent trajectories 作为实验数据源之一\"\n\n  - id: \"yang2024sweagent\"\n    title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n    authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv: \"2405.15793\"\n    category: \"evaluation\"\n    role: \"Agent 系统——trajectory 数据来源\"\n    key_finding: \"提出 agent-computer interface (ACI)，GPT-4 Turbo 在 SWE-bench 达 12.47% resolve rate\"\n    our_differentiation: \"SWE-agent trajectories 是我们分析 stagnation 的数据来源之一\"\n\n  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================\n\n  - id: \"shinn2023reflexion\"\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    arxiv: \"2303.11366\"\n    category: \"background\"\n    role: \"Agent self-reflection 代表工作\"\n    key_finding: \"通过 verbal feedback 强化 agent，反思文本存入 episodic memory 用于后续 trial\"\n    our_differentiation: \"Reflexion 是 agent 自我改进机制，我们是外部 monitoring；self-reflection 可能失效时我们的 monitor 仍能检测 stagnation\"\n\n  - id: \"zhou2024lats\"\n    title: \"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\"\n    authors: \"Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang\"\n    venue: \"ICML 2024\"\n    year: 2024\n    arxiv: \"2310.04406\"\n    category: \"background\"\n    role: \"Agent planning + self-reflection\"\n    key_finding: \"结合 MCTS 与 LM value function 和 self-reflection，支持 backtracking\"\n    our_differentiation: \"LATS 通过搜索避免 stagnation，但计算开销大；我们的 monitor 可作为 LATS 的早期终止信号\"\n\n  - id: \"yao2023tot\"\n    title: \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\"\n    authors: \"Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    arxiv: \"2305.10601\"\n    category: \"background\"\n    role: \"Deliberate reasoning 框架\"\n    key_finding: \"将 CoT 泛化为树结构，LM 自我评估中间 thought 并 backtrack\"\n    our_differentiation: \"ToT 的自评估是 single-step 的；我们捕捉 multi-step temporal patterns\"\n\n  - id: \"cemri2025multiagentfail\"\n    title: \"Why Do Multi-Agent LLM Systems Fail?\"\n    authors: \"Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2503.13657\"\n    category: \"background\"\n    role: \"Agent failure taxonomy——problem motivation\"\n    key_finding: \"MAST taxonomy：14 种失败模式，其中 Step Repetition 被识别为具体失败症状\"\n    our_differentiation: \"他们提供 taxonomy（what fails），我们提供 detection method（how to detect）\"\n\n  - id: \"zhu2025agentfail\"\n    title: \"Where LLM Agents Fail and How They Can Learn From Failures\"\n    authors: \"Kunlun Zhu, Zijia Liu, Bingxuan Li, et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2509.25370\"\n    category: \"background\"\n    role: \"Agent failure 分析 + cascading failure 发现\"\n    key_finding: \"Cascading failures（单一 root cause 传播到后续决策）是长 horizon 任务的主要失败模式\"\n    our_differentiation: \"Cascading failure 正是我们 temporal model 可以捕捉的 pattern——stagnation 往往是 cascade 的表现\"\n\n  - id: \"george2025cycledetection\"\n    title: \"Unsupervised Cycle Detection in Agentic Applications\"\n    authors: \"Felix George, Harshit Kumar, Divya Pathak, Kaustabha Ray, Mudit Verma, Pratibha Moogi\"\n    venue: \"arXiv preprint (IBM Research)\"\n    year: 2025\n    arxiv: \"2511.10650\"\n    category: \"background\"\n    role: \"Cycle detection——最相关的 stagnation detection 前驱\"\n    key_finding: \"混合方法：call-stack 分析（结构重复）+ embedding 语义相似度确认\"\n    our_differentiation: \"他们只检测 exact/near-exact cycles，我们检测更广义的 stagnation（包括非重复性的停滞）；我们的 empirical analysis 表明 30 个 structural features（含但不限于 cycle 特征）即可达 0.995 F1\"\n\n  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  - id: \"huang2024selfcorrect\"\n    title: \"Large Language Models Cannot Self-Correct Reasoning Yet\"\n    authors: \"Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2310.01798\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 失败的关键证据——支持 external monitoring 必要性\"\n    key_finding: \"LLM 在无外部反馈时无法自我纠错推理错误，intrinsic self-correction 甚至导致性能下降\"\n    our_differentiation: \"直接支持我们的核心论点：agent 不能可靠地自我检测 stagnation，需要外部 monitor；我们的 structural features 提供了轻量（<5ms）且高精度（0.995 F1）的外部检测方案\"\n\n  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================\n\n  - id: \"cho2014gru\"\n    title: \"Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation\"\n    authors: \"Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio\"\n    venue: \"EMNLP 2014\"\n    year: 2014\n    arxiv: \"1406.1078\"\n    category: \"technique\"\n    role: \"GRU 原始论文——我们 probe model 的序列编码器\"\n    key_finding: \"提出 GRU hidden unit，自适应门控信息流\"\n\n  - id: \"bahdanau2015attention\"\n    title: \"Neural Machine Translation by Jointly Learning to Align and Translate\"\n    authors: \"Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio\"\n    venue: \"ICLR 2015\"\n    year: 2015\n    arxiv: \"1409.0473\"\n    category: \"technique\"\n    role: \"Attention mechanism——我们 probe model 的 attention 组件\"\n    key_finding: \"注意力机制允许 decoder 选择性关注输入序列不同位置\"\n\n  - id: \"khosla2020supcon\"\n    title: \"Supervised Contrastive Learning\"\n    authors: \"Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, Dilip Krishnan\"\n    venue: \"NeurIPS 2020\"\n    year: 2020\n    arxiv: \"2004.11362\"\n    category: \"technique\"\n    role: \"SupCon loss——我们的辅助训练目标\"\n    key_finding: \"扩展自监督对比学习到有监督设置，同类样本拉近、异类推远，提升鲁棒性\"\n\n  - id: \"zhang2025qwen3embedding\"\n    title: \"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models\"\n    authors: \"Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2506.05176\"\n    category: \"technique\"\n    role: \"Embedding model——我们用于生成 trajectory window embeddings\"\n    key_finding: \"基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA\"\n\n# ============================================================\n# NOVELTY ANALYSIS SUMMARY (D039 Pivot — Empirical Analysis)\n# ============================================================\n#\n# Primary novelty: 首次系统性实证分析 agent stagnation 检测中 structural vs\n# semantic signal 的有效性。30 个结构特征达 0.995 in-domain / 0.967 cross-agent F1，\n# 全面优于 NL embedding (0.906/0.751) 和 LLM-as-judge (+24.3pp)。\n#\n# 三层贡献：\n# 1. Structural Signal Discovery (primary) — 改变社区对 agent monitoring 方法选型认知\n# 2. LF Temporal Dynamics Analysis — 量化 LFs 时序角色 + agent-specific 迁移分析\n# 3. TLM Negative Finding — 3 种实现 (TWV/HMM/lag-aware HMM) 均未超越 MV\n#\n# 方法论前驱（TLM negative finding 的参照）：\n# 1. Safranchik AAAI 2020 (linked HMM) — NER-specific，BIO 约束，token-level\n# 2. Sala NeurIPS 2019 (multi-resolution WS) — 处理分辨率不匹配，不建模 label transition\n# 3. Nguyen ACL 2017 (HMM-Crowd) — crowdsourcing 场景，不是 programmatic LFs\n#\n# 核心差异化：不是 \"method paper proposing TLM\"，而是 \"empirical study revealing\n# structural signals dominate stagnation detection, with temporal modeling as\n# well-motivated negative finding\".\n",
    "structuredPatch": [
      {
        "oldStart": 244,
        "oldLines": 6,
        "newStart": 244,
        "newLines": 30,
        "lines": [
          "     key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"",
          "     our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"",
          " ",
          "+  - id: \"zhou2024webarena\"",
          "+    title: \"WebArena: A Realistic Web Environment for Building Autonomous Agents\"",
          "+    authors: \"Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig\"",
          "+    venue: \"ICLR 2024\"",
          "+    year: 2024",
          "+    arxiv: \"2307.13854\"",
          "+    category: \"evaluation\"",
          "+    verified: true",
          "+    role: \"Web agent 评测基准——long-horizon 任务评估\"",
          "+    key_finding: \"812 个真实网站上的 long-horizon 任务，GPT-4 agent 仅 14.41% 成功率 vs 人类 78.24%，揭示 agent 在复杂任务上的巨大差距\"",
          "+    our_differentiation: \"WebArena 的 long-horizon 任务正是 stagnation 高发场景；我们的 monitor 可作为此类任务的早期终止/干预信号\"",
          "+",
          "+  - id: \"wang2024mint\"",
          "+    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"",
          "+    authors: \"Xingyao Wang, Zihan Wang, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng, Heng Ji\"",
          "+    venue: \"ICLR 2024\"",
          "+    year: 2024",
          "+    arxiv: \"2309.10691\"",
          "+    category: \"evaluation\"",
          "+    verified: true",
          "+    role: \"Multi-turn agent 评测基准——tool use + feedback 交互评估\"",
          "+    key_finding: \"评估 LLM 在多轮交互中使用工具和接收自然语言反馈的能力，每轮 tool use 提升 1-8%，NL feedback 提升 2-17%\"",
          "+    our_differentiation: \"MINT 量化了 multi-turn 交互中的性能变化，我们的 stagnation detection 关注多轮交互中进展停滞的检测；MINT 的 multi-turn 设定与我们的 window-level 分析天然对齐\"",
          "+",
          "   # ============================================================",
          "   # CATEGORY: background",
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

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_015NdSVKHHprsbo7FaU3SChf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
  "old_string": "  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================",
  "new_string": "  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\"\n\n  - id: \"liu2026trajad\"\n    title: \"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents\"\n    authors: \"Yibing Liu, Chong Zhang, Zhongyi Han, Hansong Liu, Yong Wang, Yang Yu, Xiaoyan Wang, Yilong Yin\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.06443\"\n    category: \"background\"\n    verified: true\n    role: \"Agent trajectory 异常检测——stagnation detection 的直接前驱\"\n    key_finding: \"TrajAD 通过 fine-grained process supervision 训练 verifier 检测 agent trajectory 中的异常（task failure, process inefficiency, unwarranted continuation），通用 LLM zero-shot 表现差\"\n    our_differentiation: \"TrajAD 需要训练专用 verifier + 合成数据（perturb-and-complete），我们用 30 个 structural features 无需训练即达 0.995 F1；他们覆盖多种异常类型，我们专注 stagnation pattern 的深度分析\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "219e1620-2cc8-4df0-af4b-31d0564e6eda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GovC2kmYAgFvubuuXGaFU3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2010,
      "cache_read_input_tokens": 38759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2010
      },
      "output_tokens": 46,
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

_source line 28 · 2026-05-14T20:29:36.906Z_

<details><summary>↩ Tool result · `toolu_015NdSVKHHprsbo7FaU3SChf`</summary>

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
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "024e07ea-8f21-4502-a4a7-fc9917e40e72",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
    "oldString": "  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================",
    "newString": "  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\"\n\n  - id: \"liu2026trajad\"\n    title: \"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents\"\n    authors: \"Yibing Liu, Chong Zhang, Zhongyi Han, Hansong Liu, Yong Wang, Yang Yu, Xiaoyan Wang, Yilong Yin\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.06443\"\n    category: \"background\"\n    verified: true\n    role: \"Agent trajectory 异常检测——stagnation detection 的直接前驱\"\n    key_finding: \"TrajAD 通过 fine-grained process supervision 训练 verifier 检测 agent trajectory 中的异常（task failure, process inefficiency, unwarranted continuation），通用 LLM zero-shot 表现差\"\n    our_differentiation: \"TrajAD 需要训练专用 verifier + 合成数据（perturb-and-complete），我们用 30 个 structural features 无需训练即达 0.995 F1；他们覆盖多种异常类型，我们专注 stagnation pattern 的深度分析\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================",
    "originalFile": "# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)\n# Generated: 2026-05-14\n# Paper: Structural Signal Analysis for Progress Stagnation Detection in LLM Agents\n#\n# D039 Pivot: Empirical analysis paper. Central finding: stagnation signals are\n# fundamentally structural (30 features → 0.995 in-domain, 0.967 cross-agent F1),\n# decisively surpassing NL embeddings (0.906/0.751) and LLM-as-judge (+24.3pp).\n# TLM is a well-motivated negative finding (3 implementations all fail to beat MV).\n\npapers:\n\n  # ============================================================\n  # CATEGORY: direct-competitor\n  # ============================================================\n\n  - id: \"xi2025agentprm\"\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Zhiheng Xi, Chenyang Liao, Guanyu Li, Yajie Yang, Wenxiang Chen, Zhihao Zhang, Binghai Wang, Senjie Jin, Yuhao Zhou, Jian Guan, Wei Wu, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2511.08325\"\n    category: \"direct-competitor\"\n    role: \"主要竞争者：step-level PRM for agent guidance\"\n    key_finding: \"用 promise（长期潜力）和 progress（即时进展）两个维度评估 agent 每步决策，实现 8x 计算效率提升\"\n    our_differentiation: \"我们是 window-level monitoring（不是 step-level guidance），不需要 outcome labels，目标是 stagnation detection 不是 reward shaping\"\n\n  - id: \"choudhury2025prm\"\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Sanjiban Choudhury\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2502.10325\"\n    category: \"direct-competitor\"\n    role: \"PRM 框架综述 + InversePRM 方法\"\n    key_finding: \"提出 AgentPRM（Monte Carlo rollout actor-critic）和 InversePRM（从 demonstrations 学习 process reward），3B 模型超越 GPT-4o\"\n    our_differentiation: \"InversePRM 仍需 demonstration trajectories，我们用 programmatic LFs 替代人工标注；我们关注 monitoring 而非 training signal\"\n\n  - id: \"li2026toolprmbench\"\n    title: \"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents\"\n    authors: \"Dawei Li, Yuguang Yao, Zhen Tan, Huan Liu, Ruocheng Guo\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.12294\"\n    category: \"direct-competitor\"\n    role: \"Tool-use PRM 评测基准\"\n    key_finding: \"大规模 benchmark 评测 PRM 在 tool-use 场景的效果，发现专用 PRM 显著优于通用 PRM\"\n    our_differentiation: \"我们的 empirical analysis 揭示 structural features 足以检测 stagnation（0.995 F1），无需 step-level reward labels；关注 stagnation pattern 而非 step correctness\"\n\n  - id: \"wang2026planrewardbench\"\n    title: \"Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling\"\n    authors: \"Jiaxuan Wang, Yulan Hu, Wenjin Yang, Zheng Pan, Xin Li, Lan-Zhe Guo\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.08178\"\n    category: \"direct-competitor\"\n    role: \"Trajectory-level reward model 评测\"\n    key_finding: \"所有 reward model 类别（generative, discriminative, LLM-as-Judge）在长 horizon trajectory 上性能显著下降\"\n    our_differentiation: \"验证了长 trajectory 评估的难度——我们的 window-level 方法通过局部化避免了这个问题\"\n\n  - id: \"chen2025monitoring\"\n    title: \"Monitoring LLM Agents for Sequentially Contextual Harm\"\n    authors: \"Yueh-Han Chen, Neelay Joshi, Yulin Chen, He He, Rico Angell\"\n    venue: \"ICLR 2025 Workshop on Building Trust in Language Models and Applications\"\n    year: 2025\n    arxiv: null\n    openreview: \"LC0XQ6ufbr\"\n    category: \"direct-competitor\"\n    role: \"Agent monitoring 安全方向\"\n    key_finding: \"将有害任务分解为单独无害的子任务可将 refusal rate 从 50% 降至 10%，现有 monitor 难以检测 sequentially contextual harm\"\n    our_differentiation: \"他们关注 safety monitoring（harmful behavior），我们关注 progress monitoring（stagnation）；互补方向\"\n\n  - id: \"kale2025weaktostrong\"\n    title: \"Reliable Weak-to-Strong Monitoring of LLM Agents\"\n    authors: \"Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team, Christina Q. Knight, Zifan Wang\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2508.19461\"\n    category: \"direct-competitor\"\n    role: \"Weak-to-strong agent monitoring 方法论\"\n    key_finding: \"Monitor scaffolding 比 monitor 能力更重要，弱模型可以可靠监控强模型；targeted human-in-the-loop 提升 TPR ~15%\"\n    our_differentiation: \"他们用 LLM 作为 monitor，我们发现 30 个 structural features 即可达 0.967 跨域 F1，不依赖另一个 LLM；更轻量（<5ms）且可解释\"\n\n  - id: \"fan2026agentrm\"\n    title: \"Exploring Reasoning Reward Model for Agents\"\n    authors: \"Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.22154\"\n    category: \"direct-competitor\"\n    verified: true\n    role: \"Agent trajectory 的多维度 reasoning reward model\"\n    key_finding: \"Agent-RRM 通过 reasoning trace + critique + overall score 三维结构化反馈评估 agent trajectory，在 12 个 benchmark 上显著提升（GAIA 43.7%, WebWalkerQA 46.2%）\"\n    our_differentiation: \"他们用 LLM-based reward model 生成结构化反馈用于 agent 改进，我们的 empirical analysis 表明轻量 structural features 即可高精度检测 stagnation（0.995 F1），不依赖大模型推理\"\n\n  - id: \"qiu2026dataprm\"\n    title: \"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis\"\n    authors: \"Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.24198\"\n    category: \"direct-competitor\"\n    verified: true\n    role: \"Agentic data analysis 场景的 process-level reward model\"\n    key_finding: \"传统 PRM 无法检测 silent errors 且误判 exploratory steps；DataPRM 通过 environment-aware probing + ternary reward 策略在 ScienceAgentBench 提升 7.21%\"\n    our_differentiation: \"DataPRM 针对数据分析 agent 的 step correctness，我们针对通用 agent 的 stagnation pattern；他们需要 execution state probing，我们用 structural LFs 无需环境交互\"\n\n  # ============================================================\n  # CATEGORY: method-component\n  # ============================================================\n\n  - id: \"ratner2016dataprogramming\"\n    title: \"Data Programming: Creating Large Training Sets, Quickly\"\n    authors: \"Alexander Ratner, Christopher De Sa, Sen Wu, Daniel Selsam, Christopher Re\"\n    venue: \"NeurIPS 2016\"\n    year: 2016\n    arxiv: \"1605.07723\"\n    category: \"method-component\"\n    role: \"核心方法论基础：data programming 范式\"\n    key_finding: \"用户编写 labeling functions（噪声启发式），generative model 学习 LF 准确率生成概率训练标签\"\n    our_differentiation: \"我们在 agent trajectory 上应用 data programming，发现 structural features 主导检测能力；同时揭示 LFs 的时序动态和 temporal label model 的负面结果\"\n\n  - id: \"ratner2017snorkel\"\n    title: \"Snorkel: Rapid Training Data Creation with Weak Supervision\"\n    authors: \"Alexander Ratner, Stephen H. Bach, Henry Ehrenberg, Jason Fries, Sen Wu, Christopher Re\"\n    venue: \"VLDB 2018\"\n    year: 2018\n    arxiv: \"1711.10160\"\n    category: \"method-component\"\n    role: \"Data programming 系统实现，label model 基础\"\n    key_finding: \"端到端弱监督系统：LFs → generative label model（建模 LF dependency）→ discriminative end model\"\n    our_differentiation: \"Snorkel 假设数据点 i.i.d.，我们发现 agent trajectory 上 LFs 展现系统性时序动态（violating i.i.d.），但 temporal label model 未能超越 MV（negative finding）\"\n\n  - id: \"fu2020flyingsquid\"\n    title: \"Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods\"\n    authors: \"Daniel Y. Fu, Mayee F. Chen, Frederic Sala, Sarah M. Hooper, Kayvon Fatahalian, Christopher Re\"\n    venue: \"ICML 2020\"\n    year: 2020\n    arxiv: \"2002.11955\"\n    category: \"method-component\"\n    role: \"快速 label model，triplet method of moments\"\n    key_finding: \"用 triplet method 闭式求解 label model 参数，比 SGD 快 170x\"\n    our_differentiation: \"FlyingSquid 同样假设 i.i.d.；我们的 empirical analysis 揭示 i.i.d. violation 虽系统性存在，但 temporal correction 在低冲突 regime 下无收益（negative finding）\"\n\n  - id: \"zhang2021wrench\"\n    title: \"WRENCH: A Comprehensive Benchmark for Weak Supervision\"\n    authors: \"Jieyu Zhang, Yue Yu, Yinghao Li, Yujing Wang, Yaming Yang, Mao Yang, Alexander Ratner\"\n    venue: \"NeurIPS 2021 Datasets and Benchmarks Track\"\n    year: 2021\n    arxiv: \"2109.11377\"\n    category: \"method-component\"\n    role: \"弱监督评测基准\"\n    key_finding: \"22 个真实数据集 + 120+ 方法变体评测，标准化弱监督研究\"\n    our_differentiation: \"WRENCH 数据集全是 i.i.d. 分类/序列标注，没有 temporal stagnation detection 任务\"\n\n  - id: \"safranchik2020linkedhmm\"\n    title: \"Weakly Supervised Sequence Tagging from Noisy Rules\"\n    authors: \"Esteban Safranchik, Shiying Luo, Stephen H. Bach\"\n    venue: \"AAAI 2020\"\n    year: 2020\n    arxiv: null\n    category: \"method-component\"\n    role: \"最近的方法论前驱：linked HMM for sequence tagging weak supervision\"\n    key_finding: \"将 HMM 引入弱监督序列标注（NER），加入 linking rules 建模 span 结构，比 i.i.d. label model +7 F1\"\n    our_differentiation: \"他们是 token-level NER（BIO 约束），我们是 window-level temporal classification；我们建模的是 stagnation temporal dynamics 而非 entity boundary\"\n\n  - id: \"sala2019multiresolution\"\n    title: \"Multi-Resolution Weak Supervision for Sequential Data\"\n    authors: \"Frederic Sala, Paroma Varma, Jason Fries, Daniel Y. Fu, Stefano Sagawa, Christopher Re\"\n    venue: \"NeurIPS 2019\"\n    year: 2019\n    arxiv: \"1910.09505\"\n    category: \"method-component\"\n    role: \"最近的方法论前驱：multi-resolution WS for sequential data\"\n    key_finding: \"处理不同时间分辨率的 LFs（如 frame-level vs span-level），建模 multi-resolution LF correlations\"\n    our_differentiation: \"他们关注 resolution mismatch，我们关注 temporal label transitions；互补视角\"\n\n  - id: \"dawid1979em\"\n    title: \"Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm\"\n    authors: \"A. P. Dawid, A. M. Skene\"\n    venue: \"Journal of the Royal Statistical Society, Series C\"\n    year: 1979\n    arxiv: null\n    category: \"method-component\"\n    role: \"Label aggregation 奠基工作\"\n    key_finding: \"用 EM 算法估计标注者混淆矩阵，无需 ground truth\"\n    our_differentiation: \"经典 i.i.d. 假设；我们测试了 temporal extension（HMM-TLM, lag-aware HMM）但发现在 3-LF 低冲突 regime 下未超越 MV——约束未来 temporal label model 研究\"\n\n  - id: \"nguyen2017hmmcrowd\"\n    title: \"Aggregating and Predicting Sequence Labels from Crowd Annotations\"\n    authors: \"An Thanh Nguyen, Byron C. Wallace, Junyi Jessy Li, Ani Nenkova, Matthew Lease\"\n    venue: \"ACL 2017\"\n    year: 2017\n    arxiv: null\n    category: \"method-component\"\n    role: \"HMM + crowdsourcing label aggregation\"\n    key_finding: \"HMM-Crowd：扩展 Dawid-Skene 到序列数据，加入 one-step Markov structure over true labels\"\n    our_differentiation: \"他们用于 crowdsourcing（人类标注者），我们用于 programmatic LFs（自动化）；他们是 NER/IE，我们是 agent progress monitoring\"\n\n  # ============================================================\n  # CATEGORY: evaluation\n  # ============================================================\n\n  - id: \"orlanski2026slopcodebench\"\n    title: \"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks\"\n    authors: \"Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu, Albert Ge, Dyah Adila, Nicholas Roberts, Frederic Sala, Aws Albarghouthi\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.24755\"\n    category: \"evaluation\"\n    role: \"Agent degradation 基准——直接支持我们的 problem motivation\"\n    key_finding: \"Agent 代码质量在迭代任务中持续退化：比人类代码 2.3x 更冗余、2.0x 更结构侵蚀，75-77% trajectory 呈现退化趋势\"\n    our_differentiation: \"SlopCodeBench 量化了 degradation 现象，我们提供了检测方法；他们是 post-hoc 评测，我们是 online monitoring\"\n\n  - id: \"jimenez2024swebench\"\n    title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n    authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2310.06770\"\n    category: \"evaluation\"\n    role: \"Agent 数据来源之一\"\n    key_finding: \"2294 个真实 GitHub issue 任务，标准化 agent 评测\"\n    our_differentiation: \"我们使用 SWE-bench agent trajectories 作为实验数据源之一\"\n\n  - id: \"yang2024sweagent\"\n    title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n    authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv: \"2405.15793\"\n    category: \"evaluation\"\n    role: \"Agent 系统——trajectory 数据来源\"\n    key_finding: \"提出 agent-computer interface (ACI)，GPT-4 Turbo 在 SWE-bench 达 12.47% resolve rate\"\n    our_differentiation: \"SWE-agent trajectories 是我们分析 stagnation 的数据来源之一\"\n\n  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  - id: \"zhou2024webarena\"\n    title: \"WebArena: A Realistic Web Environment for Building Autonomous Agents\"\n    authors: \"Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2307.13854\"\n    category: \"evaluation\"\n    verified: true\n    role: \"Web agent 评测基准——long-horizon 任务评估\"\n    key_finding: \"812 个真实网站上的 long-horizon 任务，GPT-4 agent 仅 14.41% 成功率 vs 人类 78.24%，揭示 agent 在复杂任务上的巨大差距\"\n    our_differentiation: \"WebArena 的 long-horizon 任务正是 stagnation 高发场景；我们的 monitor 可作为此类任务的早期终止/干预信号\"\n\n  - id: \"wang2024mint\"\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Xingyao Wang, Zihan Wang, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng, Heng Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2309.10691\"\n    category: \"evaluation\"\n    verified: true\n    role: \"Multi-turn agent 评测基准——tool use + feedback 交互评估\"\n    key_finding: \"评估 LLM 在多轮交互中使用工具和接收自然语言反馈的能力，每轮 tool use 提升 1-8%，NL feedback 提升 2-17%\"\n    our_differentiation: \"MINT 量化了 multi-turn 交互中的性能变化，我们的 stagnation detection 关注多轮交互中进展停滞的检测；MINT 的 multi-turn 设定与我们的 window-level 分析天然对齐\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================\n\n  - id: \"shinn2023reflexion\"\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    arxiv: \"2303.11366\"\n    category: \"background\"\n    role: \"Agent self-reflection 代表工作\"\n    key_finding: \"通过 verbal feedback 强化 agent，反思文本存入 episodic memory 用于后续 trial\"\n    our_differentiation: \"Reflexion 是 agent 自我改进机制，我们是外部 monitoring；self-reflection 可能失效时我们的 monitor 仍能检测 stagnation\"\n\n  - id: \"zhou2024lats\"\n    title: \"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\"\n    authors: \"Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang\"\n    venue: \"ICML 2024\"\n    year: 2024\n    arxiv: \"2310.04406\"\n    category: \"background\"\n    role: \"Agent planning + self-reflection\"\n    key_finding: \"结合 MCTS 与 LM value function 和 self-reflection，支持 backtracking\"\n    our_differentiation: \"LATS 通过搜索避免 stagnation，但计算开销大；我们的 monitor 可作为 LATS 的早期终止信号\"\n\n  - id: \"yao2023tot\"\n    title: \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\"\n    authors: \"Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    arxiv: \"2305.10601\"\n    category: \"background\"\n    role: \"Deliberate reasoning 框架\"\n    key_finding: \"将 CoT 泛化为树结构，LM 自我评估中间 thought 并 backtrack\"\n    our_differentiation: \"ToT 的自评估是 single-step 的；我们捕捉 multi-step temporal patterns\"\n\n  - id: \"cemri2025multiagentfail\"\n    title: \"Why Do Multi-Agent LLM Systems Fail?\"\n    authors: \"Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2503.13657\"\n    category: \"background\"\n    role: \"Agent failure taxonomy——problem motivation\"\n    key_finding: \"MAST taxonomy：14 种失败模式，其中 Step Repetition 被识别为具体失败症状\"\n    our_differentiation: \"他们提供 taxonomy（what fails），我们提供 detection method（how to detect）\"\n\n  - id: \"zhu2025agentfail\"\n    title: \"Where LLM Agents Fail and How They Can Learn From Failures\"\n    authors: \"Kunlun Zhu, Zijia Liu, Bingxuan Li, et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2509.25370\"\n    category: \"background\"\n    role: \"Agent failure 分析 + cascading failure 发现\"\n    key_finding: \"Cascading failures（单一 root cause 传播到后续决策）是长 horizon 任务的主要失败模式\"\n    our_differentiation: \"Cascading failure 正是我们 temporal model 可以捕捉的 pattern——stagnation 往往是 cascade 的表现\"\n\n  - id: \"george2025cycledetection\"\n    title: \"Unsupervised Cycle Detection in Agentic Applications\"\n    authors: \"Felix George, Harshit Kumar, Divya Pathak, Kaustabha Ray, Mudit Verma, Pratibha Moogi\"\n    venue: \"arXiv preprint (IBM Research)\"\n    year: 2025\n    arxiv: \"2511.10650\"\n    category: \"background\"\n    role: \"Cycle detection——最相关的 stagnation detection 前驱\"\n    key_finding: \"混合方法：call-stack 分析（结构重复）+ embedding 语义相似度确认\"\n    our_differentiation: \"他们只检测 exact/near-exact cycles，我们检测更广义的 stagnation（包括非重复性的停滞）；我们的 empirical analysis 表明 30 个 structural features（含但不限于 cycle 特征）即可达 0.995 F1\"\n\n  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  - id: \"huang2024selfcorrect\"\n    title: \"Large Language Models Cannot Self-Correct Reasoning Yet\"\n    authors: \"Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2310.01798\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 失败的关键证据——支持 external monitoring 必要性\"\n    key_finding: \"LLM 在无外部反馈时无法自我纠错推理错误，intrinsic self-correction 甚至导致性能下降\"\n    our_differentiation: \"直接支持我们的核心论点：agent 不能可靠地自我检测 stagnation，需要外部 monitor；我们的 structural features 提供了轻量（<5ms）且高精度（0.995 F1）的外部检测方案\"\n\n  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================\n\n  - id: \"cho2014gru\"\n    title: \"Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation\"\n    authors: \"Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio\"\n    venue: \"EMNLP 2014\"\n    year: 2014\n    arxiv: \"1406.1078\"\n    category: \"technique\"\n    role: \"GRU 原始论文——我们 probe model 的序列编码器\"\n    key_finding: \"提出 GRU hidden unit，自适应门控信息流\"\n\n  - id: \"bahdanau2015attention\"\n    title: \"Neural Machine Translation by Jointly Learning to Align and Translate\"\n    authors: \"Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio\"\n    venue: \"ICLR 2015\"\n    year: 2015\n    arxiv: \"1409.0473\"\n    category: \"technique\"\n    role: \"Attention mechanism——我们 probe model 的 attention 组件\"\n    key_finding: \"注意力机制允许 decoder 选择性关注输入序列不同位置\"\n\n  - id: \"khosla2020supcon\"\n    title: \"Supervised Contrastive Learning\"\n    authors: \"Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, Dilip Krishnan\"\n    venue: \"NeurIPS 2020\"\n    year: 2020\n    arxiv: \"2004.11362\"\n    category: \"technique\"\n    role: \"SupCon loss——我们的辅助训练目标\"\n    key_finding: \"扩展自监督对比学习到有监督设置，同类样本拉近、异类推远，提升鲁棒性\"\n\n  - id: \"zhang2025qwen3embedding\"\n    title: \"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models\"\n    authors: \"Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2506.05176\"\n    category: \"technique\"\n    role: \"Embedding model——我们用于生成 trajectory window embeddings\"\n    key_finding: \"基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA\"\n\n# ============================================================\n# NOVELTY ANALYSIS SUMMARY (D039 Pivot — Empirical Analysis)\n# ============================================================\n#\n# Primary novelty: 首次系统性实证分析 agent stagnation 检测中 structural vs\n# semantic signal 的有效性。30 个结构特征达 0.995 in-domain / 0.967 cross-agent F1，\n# 全面优于 NL embedding (0.906/0.751) 和 LLM-as-judge (+24.3pp)。\n#\n# 三层贡献：\n# 1. Structural Signal Discovery (primary) — 改变社区对 agent monitoring 方法选型认知\n# 2. LF Temporal Dynamics Analysis — 量化 LFs 时序角色 + agent-specific 迁移分析\n# 3. TLM Negative Finding — 3 种实现 (TWV/HMM/lag-aware HMM) 均未超越 MV\n#\n# 方法论前驱（TLM negative finding 的参照）：\n# 1. Safranchik AAAI 2020 (linked HMM) — NER-specific，BIO 约束，token-level\n# 2. Sala NeurIPS 2019 (multi-resolution WS) — 处理分辨率不匹配，不建模 label transition\n# 3. Nguyen ACL 2017 (HMM-Crowd) — crowdsourcing 场景，不是 programmatic LFs\n#\n# 核心差异化：不是 \"method paper proposing TLM\"，而是 \"empirical study revealing\n# structural signals dominate stagnation detection, with temporal modeling as\n# well-motivated negative finding\".\n",
    "structuredPatch": [
      {
        "oldStart": 373,
        "oldLines": 6,
        "newStart": 373,
        "newLines": 18,
        "lines": [
          "     key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"",
          "     our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\"",
          " ",
          "+  - id: \"liu2026trajad\"",
          "+    title: \"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents\"",
          "+    authors: \"Yibing Liu, Chong Zhang, Zhongyi Han, Hansong Liu, Yong Wang, Yang Yu, Xiaoyan Wang, Yilong Yin\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2026",
          "+    arxiv: \"2602.06443\"",
          "+    category: \"background\"",
          "+    verified: true",
          "+    role: \"Agent trajectory 异常检测——stagnation detection 的直接前驱\"",
          "+    key_finding: \"TrajAD 通过 fine-grained process supervision 训练 verifier 检测 agent trajectory 中的异常（task failure, process inefficiency, unwarranted continuation），通用 LLM zero-shot 表现差\"",
          "+    our_differentiation: \"TrajAD 需要训练专用 verifier + 合成数据（perturb-and-complete），我们用 30 个 structural features 无需训练即达 0.995 F1；他们覆盖多种异常类型，我们专注 stagnation pattern 的深度分析\"",
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

_source line 29_

已添加 3 篇论文：

- **evaluation**: `zhou2024webarena` (WebArena, ICLR 2024, arxiv 2307.13854), `wang2024mint` (MINT, ICLR 2024, arxiv 2309.10691)
- **background**: `liu2026trajad` (TrajAD, arXiv 2026, arxiv 2602.06443)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "uuid": "8258df14-50a1-4136-8736-d0defbe97b73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2MbHBhKqewMvwqwZEgL9L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 40769,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1075
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

_source line 30_

已添加 3 篇论文：

- **evaluation**: `zhou2024webarena` (WebArena, ICLR 2024, arxiv 2307.13854), `wang2024mint` (MINT, ICLR 2024, arxiv 2309.10691)
- **background**: `liu2026trajad` (TrajAD, arXiv 2026, arxiv 2602.06443)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 100572,
  "duration_api_ms": 124876,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "b70e06a0-6988-409b-be37-d7c666188d79",
  "total_cost_usd": 0.52894275,
  "usage": {
    "input_tokens": 880,
    "cache_creation_input_tokens": 30003,
    "cache_read_input_tokens": 184090,
    "output_tokens": 3948,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 30003,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 110,
        "cache_read_input_tokens": 40769,
        "cache_creation_input_tokens": 1075,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1075
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 83809,
      "outputTokens": 2494,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 5,
      "costUSD": 0.146279,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 880,
      "outputTokens": 3948,
      "cacheReadInputTokens": 184090,
      "cacheCreationInputTokens": 30003,
      "webSearchRequests": 0,
      "costUSD": 0.38266375,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a82168e1-ddfa-497f-bd0b-b6cd10c161d3"
}
```

</details>

---
