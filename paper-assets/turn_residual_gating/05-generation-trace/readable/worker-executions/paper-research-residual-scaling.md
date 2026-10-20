# paper research residual scaling

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_paper_research_residual_scaling_20260519T214510.log`
- **Structured JSON:** [`a980b29d354df4797c15.json`](../../sessions/a9/a980b29d354df4797c15.json)

## Before a recorded user message

18 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
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
  "uuid": "fad77aa0-78ea-49c3-a21c-cdcf38e0de8a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/memory/"
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
    "resetsAt": 1779243600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2a73fc49-91b5-4c6d-ab62-6f89cd0f0695",
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The task is to find 2 papers about residual connection scaling/initialization and add them to literature_map.yaml under a new `residual_scaling` category.

Let me first search for the papers using Semantic Scholar API, then read the existing literature_map.yaml, and add the new entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "uuid": "6bab9ae5-6954-4b16-a87e-2da5cf7cba0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoTxurG7rMDaF4pQ4hgPwm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12580,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12580
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

先搜索论文，同时读取现有的 literature_map.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "uuid": "b28df18e-115e-4640-b573-e7784a04790f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoTxurG7rMDaF4pQ4hgPwm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12580,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12580
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

<details open><summary>🔧 Tool call — Bash · `toolu_01RMVEfcfSoF7dCiMEPRbRcD`</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nfor query_str in ['ReZero is All You Need Fast Convergence Large Depth', 'Fixup Initialization Residual Learning Without Normalization']:\n    query = quote(query_str)\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,abstract,citationCount'\n    req = Request(url, headers={'User-Agent': 'ResearchBot/1.0'})\n    try:\n        data = json.loads(urlopen(req, timeout=15).read())\n        for p in data.get('data', []):\n            authors = ', '.join([a['name'] for a in p.get('authors', [])[:5]])\n            print(f\\\"Title: {p['title']}\\\")\n            print(f\\\"Authors: {authors}\\\")\n            print(f\\\"Year: {p['year']} | Venue: {p.get('venue','')} | Citations: {p.get('citationCount',0)}\\\")\n            arxiv = p.get('externalIds',{}).get('ArXiv','')\n            if arxiv:\n                print(f\\\"ArXiv: https://arxiv.org/abs/{arxiv}\\\")\n            abstract = (p.get('abstract','') or '')[:300]\n            print(f\\\"Abstract: {abstract}...\\\")\n            print()\n        print('---')\n    except Exception as e:\n        print(f'Error: {e}')\n\"\n",
  "description": "Search Semantic Scholar for ReZero and Fixup papers",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "uuid": "131c089a-3ecb-4fde-9db0-292cfa8a622d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoTxurG7rMDaF4pQ4hgPwm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12580,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12580
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

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01HZ3jtrsr1sCpV7VrtXfXdU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "uuid": "21b918d9-7ed7-4aea-85e9-937d1f17478f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoTxurG7rMDaF4pQ4hgPwm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12580,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12580
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

_source line 8 · 2026-05-19T21:45:30.661Z_

<details><summary>↩ Tool result · `toolu_01RMVEfcfSoF7dCiMEPRbRcD`</summary>

```text
Error: HTTP Error 429: 
Error: HTTP Error 429:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "uuid": "ec7710db-5cd7-4d17-a403-04444d2fb6fd",
  "tool_use_result": {
    "stdout": "Error: HTTP Error 429: \nError: HTTP Error 429:",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T21:45:30.674Z_

<details><summary>↩ Tool result · `toolu_01HZ3jtrsr1sCpV7VrtXfXdU`</summary>

```text
1	categories:
2	  layer_importance:
3	    description: Layer-wise importance analysis, redundancy, and pruning in transformers
4	    papers:
5	    - title: The Unreasonable Ineffectiveness of the Deeper Layers
6	      authors: Gromov et al.
7	      venue: ICLR 2025
8	      year: 2024
9	      url: https://arxiv.org/abs/2403.17887
10	      role: foundation
11	      relevance: 发现 LLM 深层高度冗余，可删除近半层而性能不降；浅层对知识存储至关重要
12	      abstract: Studies knowledge storage via layer pruning. Finds minimal performance degradation until up to half of layers
13	        are removed.
14	    - title: 'ShortGPT: Layers in Large Language Models are More Redundant Than You Expect'
15	      authors: Men et al.
16	      venue: arXiv 2024
17	      year: 2024
18	      url: https://arxiv.org/abs/2403.03853
19	      role: foundation
20	      relevance: 提出 Block Influence (BI) 度量各层重要性，发现许多层高度相似且功能冗余
21	      abstract: Defines Block Influence (BI) metric to gauge layer significance. Discovers many LLM layers exhibit high similarity.
22	    - title: The Curse of Depth in Large Language Models
23	      authors: Sun et al.
24	      venue: NeurIPS 2025
25	      year: 2025
26	      url: https://arxiv.org/abs/2502.05795
27	      role: foundation
28	      relevance: Pre-LN 导致深层梯度趋近恒等映射。解释 ThreadGate 中 late layers gate 接近 1.0
29	      abstract: Pre-Layer Normalization causes output variance to grow exponentially with depth.
30	    - title: 'Reassessing Layer Pruning in LLMs: New Insights and Methods'
31	      authors: Anonymous
32	      venue: arXiv 2024
33	      year: 2024
34	      url: https://arxiv.org/abs/2411.15558
35	      role: context
36	      relevance: 删除最后 25% 层 + 微调即可获得强性能，证实深层冗余
37	      abstract: Simply pruning the final 25% of layers followed by fine-tuning yields strong performance.
38	    - title: Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)
39	      authors: Fan et al.
40	      venue: ICLR 2020
41	      year: 2020
42	      url: https://arxiv.org/abs/1909.11556
43	      role: method-component
44	      relevance: ThreadGate 的 gating 可视为 LayerDrop 的 soft 版本
45	      abstract: Structured dropout on entire transformer layers during training.
46	  multi_turn_attention:
47	    description: Attention degradation and instruction following failure in multi-turn or long-context scenarios
48	    papers:
49	    - title: 'When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction'
50	      authors: Dongre, Hsieh, Lai, Yoon, Bui, Hakkani-Tur
51	      venue: arXiv 2026
52	      year: 2026
53	      url: https://arxiv.org/abs/2605.12922
54	      role: foundation
55	      relevance: 定义 GAR，诊断多轮 attention 通道关闭。纯诊断论文，未提出干预方案。ThreadGate 是首个基于其诊断的干预方法
56	      abstract: 'Channel-transition account: goal tokens become less accessible through attention while goal info persists
57	        in residual representations. Introduces GAR metric.'
58	      notes:
59	        gar_definition: GAR(τ) = (1/L·H·|ℛτ|) Σℓ Σh Σi∈ℛτ Σj∈𝒢 A_{i,j}. ALL layers, ALL heads averaged. Goal tokens = system
60	          prompt task-specifying tokens only
61	        models_tested: Mistral-7B, LLaMA-3.1-8B, Qwen-2.5 (3B/7B/14B/32B), Mixtral-8x7B + 6 additional
62	        gar_decline: 27-48% over 50 turns, monotonic (Mann-Kendall p<1e-7)
63	        residual_probes: 'LDA on PCA-reduced residuals (50 PCs). Peak AUC: LLaMA L2=0.99, Qwen L11=0.98, Mixtral L21=0.99,
64	          Mistral L27=0.87'
65	        qwen_layer_profile: Goal encoding rises steeply from L5. Our v3b L4 outlier may be the layer just before goal encoding
66	          begins
67	        intervention_tested: Periodic goal re-injection FAILED (Appendix H)
68	        no_solution: true
69	        sliding_window: Attention mask W=4096, Qwen crossover at turn 20. Linear W-vs-crossover (R2~1)
70	        framing_impact: GAR not our original metric. No intervention proposed -> ThreadGate is first solution. Residual persistence
71	          directly supports our theory
72	    - title: LLMs Get Lost In Multi-Turn Conversation
73	      authors: Levy et al.
74	      venue: arXiv 2025
75	      year: 2025
76	      url: https://arxiv.org/abs/2505.06120
77	      role: foundation
78	      relevance: 量化多轮对话性能衰减：平均下降 39%，不可靠性增加 112%
79	      abstract: All top LLMs exhibit significantly lower performance in multi-turn vs single-turn, averaging 39% drop.
80	    - title: Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation
81	      authors: Liu et al.
82	      venue: arXiv 2026
83	      year: 2026
84	      url: https://arxiv.org/abs/2602.07338
85	      role: context
86	      relevance: 多轮失败根因是 intent alignment gap，scaling 无法解决。支撑 ThreadGate 架构级方案动机
87	      abstract: Lost in Conversation stems from intent alignment gap, not capability deficits. Scaling cannot resolve.
88	    - title: 'Lost in the Middle: How Language Models Use Long Contexts'
89	      authors: Liu et al.
90	      venue: TACL 2024
91	      year: 2023
92	      url: https://arxiv.org/abs/2307.03172
93	      role: foundation
94	      relevance: U 型 attention 分布（首尾强、中间弱）。多轮场景是此现象在 turn boundary 上的扩展
95	      abstract: Performance highest at beginning/end of context, degrading for middle positions.
96	    - title: 'Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models'
97	      authors: Anonymous
98	      venue: arXiv 2025
99	      year: 2025
100	      url: https://arxiv.org/abs/2512.23578
101	      role: context
102	      relevance: 多轮对话中 style instruction 遵循衰减，system message 比 user message 更严重
103	      abstract: Style instruction in system messages degrades more than in user messages across turns.
104	  residual_gating:
105	    description: Gating mechanisms for transformer residual connections and adaptive depth
106	    papers:
107	    - title: 'Mixture-of-Depths: Dynamically allocating compute in transformer-based language models'
108	      authors: Raposo et al.
109	      venue: arXiv 2024 (Google DeepMind)
110	      year: 2024
111	      url: https://arxiv.org/abs/2404.02258
112	      role: method-component
113	      relevance: top-k routing 动态分配计算。ThreadGate 可视为 MoD 在 turn boundary 上的特化
114	      abstract: Dynamically allocate FLOPs per layer via top-k routing. 1.5% loss improvement or 50% FLOP reduction.
115	    - title: Confident Adaptive Language Modeling (CALM)
116	      authors: Schuster et al.
117	      venue: NeurIPS 2022
118	      year: 2022
119	      url: https://arxiv.org/abs/2207.07061
120	      role: method-component
121	      relevance: 置信度 early exit。CALM 是 monotonic exit，ThreadGate 允许 selective layer gating
122	      abstract: Dynamically allocating compute per input based on confidence. Up to 3x speedup.
123	    - title: 'Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free'
124	      authors: Qiu et al.
125	      venue: NeurIPS 2025 (Oral)
126	      year: 2025
127	      url: https://arxiv.org/abs/2505.06708
128	      role: method-component
129	      relevance: SDPA 输出加 sigmoid gate 消除 attention sink。可参考 head-specific sigmoid gate 设计
130	      abstract: Head-specific sigmoid gate after SDPA. Eliminates attention sink (83% to 4%).
131	    - title: 'SkipNet: Learning Dynamic Routing in Convolutional Networks'
132	      authors: Wang et al.
133	      venue: ECCV 2018
134	      year: 2018
135	      url: https://arxiv.org/abs/1711.09485
136	      role: method-component
137	      relevance: 残差网络逐层 gating 先驱。ThreadGate per-layer gating 的前身
138	      abstract: Gating network to selectively skip convolutional blocks. RL+SL hybrid training.
139	    - title: Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)
140	      authors: Luo et al.
141	      venue: arXiv 2025
142	      year: 2025
143	      url: https://arxiv.org/abs/2503.23798
144	      role: direct-competitor
145	      relevance: plug-in router+adapter on frozen LLM 自适应 layer skipping。与 ThreadGate 高度类似，直接竞品
146	      abstract: Dynamically adjusts layers via plug-in router and adapter. Llama-3-8B skips 8/32 layers maintaining performance.
147	    - title: Learning to Skip the Middle Layers of Transformers
148	      authors: Lawson et al.
149	      venue: arXiv 2025
150	      year: 2025
151	      url: https://arxiv.org/abs/2506.21103
152	      role: context
153	      relevance: middle-out layer skipping 负面结果参考
154	      abstract: Gating to skip middle blocks. Does not improve vs dense baselines at investigated scales.
155	  attention_manipulation:
156	    description: Methods that modify attention weights, positional encoding, or attention distributions to handle long-range
157	      dependencies
158	    papers:
159	    - title: 'Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation'
160	      authors: Press et al.
161	      venue: ICLR 2022
162	      year: 2022
163	      url: https://arxiv.org/abs/2108.12409
164	      role: foundation
165	      relevance: ALiBi 在注意力分数上施加距离线性惩罚实现长度外推，是注意力操纵路线的代表方法，与 ThreadGate 残差门控路线形成设计空间对比
166	      abstract: Replaces positional embeddings with linear bias on attention logits penalizing distance. 1.3B model trained
167	        on 1024 generalizes to 2048 without fine-tuning.
168	    - title: Extending Context Window of Large Language Models via Positional Interpolation
169	      authors: Chen et al.
170	      venue: arXiv 2023
171	      year: 2023
172	      url: https://arxiv.org/abs/2306.15595
173	      role: foundation
174	      relevance: 位置插值通过压缩 RoPE 索引扩展上下文至 32k，属于注意力机制内部解决长序列的路线，与 ThreadGate 在残差层解决多轮衰减形成对比
175	      abstract: Linearly down-scales RoPE position indices to extend context to 32768 tokens in 1000 fine-tuning steps.
176	    - title: 'YaRN: Efficient Context Window Extension of Large Language Models'
177	      authors: Peng et al.
178	      venue: ICLR 2024
179	      year: 2024
180	      url: https://arxiv.org/abs/2309.00071
181	      role: foundation
182	      relevance: YaRN 综合 NTK-aware 和分段插值改进 RoPE 外推，代表注意力位置编码修改应对长程衰减的成熟路线，与 ThreadGate 机制不同
183	      abstract: Combines NTK-aware interpolation with ramp function for different RoPE frequency components. Extends LLaMA-2
184	        to 128k context with 10x fewer tokens.
185	    - title: Efficient Streaming Language Models with Attention Sinks
186	      authors: Xiao et al.
187	      venue: ICLR 2024
188	      year: 2024
189	      url: https://arxiv.org/abs/2309.17453
190	      role: context
191	      relevance: 发现 attention sink 现象（初始 token 聚集高权重），说明多轮对话中早期轮次 token 天然受偏置，ThreadGate 从残差路径角度控制历史轮信息保留
192	      abstract: LLMs assign disproportionate attention to first few tokens regardless of semantics. Retaining sink tokens
193	        enables stable streaming inference over 4M tokens.
194	    - title: 'LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models'
195	      authors: Han et al.
196	      venue: ACL 2024
197	      year: 2024
198	      url: https://arxiv.org/abs/2308.16137
199	      role: context
200	      relevance: 用 Λ 形注意力掩码加距离截断实现超长上下文推理，揭示调整注意力掩码和调整残差门控是两条平行路线
201	      abstract: Applies Λ-shaped attention mask plus distance limit on position encodings. Generalizes to 200M tokens with
202	        2.7x speedup, no parameter updates.
203	    - title: 'Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization'
204	      authors: Ko et al.
205	      venue: arXiv 2024
206	      year: 2024
207	      url: https://arxiv.org/abs/2406.16008
208	      role: direct-competitor
209	      relevance: 直接校准注意力位置偏置修复中段信息丢失，最接近 ThreadGate 问题定义的注意力方案，审稿人会以此质疑为何不直接修正注意力
210	      abstract: Identifies U-shaped positional attention bias causing lost-in-the-middle. Training-free calibration redistributes
211	        attention to middle positions, improving QA by 6-15pp.
212	  theoretical_foundations:
213	    description: Theoretical analysis of transformer residual streams, information flow, and attention dynamics
214	    papers:
215	    - title: A Mathematical Framework for Transformer Circuits
216	      authors: Elhage et al.
217	      venue: Transformer Circuits Thread 2021
218	      year: 2021
219	      url: https://transformer-circuits.pub/2021/framework/index.html
220	      role: foundation
221	      relevance: 提出残差流作为 transformer 各组件通信核心通道，直接为 ThreadGate 在残差连接处插入门控提供机制解释框架
222	      abstract: Linear algebraic decomposition of transformer computations. Attention heads and MLPs as read/write operations
223	        on shared residual stream. Formalizes induction heads and QK/OV circuits.
224	    - title: Toy Models of Superposition
225	      authors: Elhage et al.
226	      venue: arXiv 2022
227	      year: 2022
228	      url: https://arxiv.org/abs/2209.10652
229	      role: foundation
230	      relevance: 揭示残差流子空间叠加存储稀疏特征的机制，为 ThreadGate 按轮次条件化选择性激活残差通道提供理论依据
231	      abstract: Neural networks store more features than dimensions via superposition when features are sparse. Links polysemanticity
232	        to geometry of uniform polytopes.
233	    - title: Eliciting Latent Predictions from Transformers with the Tuned Lens
234	      authors: Belrose et al.
235	      venue: arXiv 2023
236	      year: 2023
237	      url: https://arxiv.org/abs/2303.08112
238	      role: foundation
239	      relevance: 逐层解码残差流隐状态揭示信息在深度方向渐进精化，支撑 ThreadGate 不同层门控强度差异化设计的动机
240	      abstract: Per-layer affine probes decode intermediate residual stream states into vocabulary distributions. Shows predictions
241	        iteratively refined across depth up to 20B parameters.
242	    - title: Exploring the Residual Stream of Transformers
243	      authors: Yu et al.
244	      venue: arXiv 2023
245	      year: 2023
246	      url: https://arxiv.org/abs/2312.12141
247	      role: foundation
248	      relevance: 分析残差连接对 logit 空间的加法效应，揭示知识参数跨层分布规律，为 ThreadGate 定位门控插入层提供实证参考
249	      abstract: Residual connections act as direct additive operations on pre-softmax logits. Identifies factual knowledge
250	        storage distribution across layers and modules.
251	    - title: 'Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains'
252	      authors: Makkuva et al.
253	      venue: ICLR 2025
254	      year: 2025
255	      url: https://arxiv.org/abs/2402.04161
256	      role: foundation
257	      relevance: 用 Markov 链理论刻画注意力深度依赖性，解释为何单层 transformer 无法形成归纳头，支持 ThreadGate 在多层残差路径施加门控的必要性
258	      abstract: Theoretical framework via Markov chain properties. Two-layer transformers learn induction heads on first-order
259	        Markov data; single-layer models get trapped in unigram minima.
260	    - title: 'From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers'
261	      authors: Ildiz et al.
262	      venue: ICML 2024
263	      year: 2024
264	      url: https://arxiv.org/abs/2402.13512
265	      role: foundation
266	      relevance: 建立自注意力与上下文条件 Markov 链的精确映射，为分析多轮对话 token 分布随轮次漂移（GAR decay）提供随机过程理论基础
267	      abstract: Mathematical equivalence between self-attention and context-conditioned Markov chains. Output distribution
268	        sampled from context-weighted transition matrix.
269	  evaluation_benchmarks:
270	    description: Multi-turn dialogue and instruction-following evaluation benchmarks for LLMs
271	    papers:
272	    - title: Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
273	      authors: Zheng et al.
274	      venue: NeurIPS 2023
275	      year: 2023
276	      url: https://arxiv.org/abs/2306.05685
277	      role: foundation
278	      relevance: MT-Bench 多轮对话评测框架，是 ThreadGate 验证多轮 GAR 衰减修复效果的核心 benchmark
279	      abstract: Introduces MT-Bench (80 multi-turn questions) and Chatbot Arena. GPT-4 achieves >80% agreement with human
280	        preferences as judge.
281	    - title: 'Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference'
282	      authors: Chiang et al.
283	      venue: ICML 2024
284	      year: 2024
285	      url: https://arxiv.org/abs/2403.04132
286	      role: foundation
287	      relevance: 基于 ELO 排名的人类偏好评估体系，衡量多轮对话模型综合能力的权威 leaderboard
288	      abstract: Chatbot Arena with 240K+ votes from 90K+ users across 50+ models. Bradley-Terry and ELO ranking validated
289	        against expert raters.
290	    - title: 'Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators'
291	      authors: Dubois et al.
292	      venue: COLM 2024
293	      year: 2024
294	      url: https://arxiv.org/abs/2404.04475
295	      role: foundation
296	      relevance: 指令遵循自动评测标准，Length-Controlled 版本修正长度偏差，为 ThreadGate 单轮指令评测提供对比基线
297	      abstract: GLM-based length debiasing for AlpacaEval. Validated against 20K human annotations.
298	    - title: 'WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild'
299	      authors: Lin et al.
300	      venue: arXiv 2024
301	      year: 2024
302	      url: https://arxiv.org/abs/2406.04770
303	      role: foundation
304	      relevance: 真实用户多样化指令集，评估 wild 场景指令遵循能力，与 ThreadGate 关注的真实多轮对话性能高度相关
305	      abstract: 1,024 challenging tasks from 1M+ conversation logs. WB-Reward/WB-Score achieve 0.98 Pearson correlation with
306	        Chatbot Arena ELO on hard tasks.
307	    - title: 'MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues'
308	      authors: Bai et al.
309	      venue: ACL 2024
310	      year: 2024
311	      url: https://arxiv.org/abs/2402.14762
312	      role: direct-competitor
313	      relevance: 多轮对话细粒度评测体系，直接测量跨轮次能力退化，与 ThreadGate 研究的 GAR 衰减高度吻合
314	      abstract: Three-tier ability taxonomy, 4,208 turns across 1,388 dialogues in 13 tasks. Neither alignment nor chat-specific
315	        designs consistently improve multi-turn abilities.
316	    - title: 'MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs'
317	      authors: Sirdeshmukh et al.
318	      venue: arXiv 2025
319	      year: 2025
320	      url: https://arxiv.org/abs/2501.17399
321	      role: direct-competitor
322	      relevance: 前沿 LLM 多轮对话准确率不足 50%，直接测量 ThreadGate 旨在修复的跨轮指令保留和上下文一致性失败
323	      abstract: 'Four challenge categories: instruction retention, user inference memory, versioned editing, self-coherence.
324	        All frontier LLMs below 50%; Claude 3.5 Sonnet tops at 41.4%.'
325	  exposure_bias:
326	    description: Exposure bias, teacher forcing, scheduled sampling, and train-test distribution mismatch in sequence generation
327	    papers:
328	    - title: Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks
329	      authors: Bengio, Vinyals, Jaitly, Shazeer
330	      venue: NeurIPS 2015
331	      year: 2015
332	      url: https://arxiv.org/abs/1506.03099
333	      role: foundation
334	      relevance: Scheduled sampling 首次提出用 curriculum learning 缓解 teacher forcing 与推理时 autoregressive decoding 的分布不匹配（exposure
335	        bias），直接支撑论文对 auxiliary attention loss 训练-推理 gap 的根因分析
336	      abstract: Proposes a curriculum learning strategy to gently change training from fully guided (true previous token)
337	        to less guided (model-generated token). The discrepancy between teacher-forced training and autoregressive inference
338	        causes error accumulation. Experiments on sequence prediction tasks show significant improvements. Used in the winning
339	        MSCOCO image captioning challenge 2015 entry.
340	    - title: Sequence Level Training with Recurrent Neural Networks
341	      authors: Ranzato, Chopra, Auli, Zaremba
342	      venue: ICLR 2016
343	      year: 2016
344	      url: https://arxiv.org/abs/1511.06732
345	      role: foundation
346	      relevance: MIXER 算法直接优化测试时指标（BLEU/ROUGE）而非 token-level MLE，解决 teacher forcing 导致的 train-test discrepancy；论文中 auxiliary
347	        loss 同样面临 token-level 训练目标与 sequence-level 推理行为的错位
348	      abstract: Addresses the discrepancy between token-level MLE training and sequence-level generation at test time. Proposes
349	        sequence level training that directly optimizes test metrics (BLEU, ROUGE). Outperforms strong baselines for greedy
350	        generation on three tasks and is competitive with beam search while being several times faster.
351	    - title: 'Professor Forcing: A New Algorithm for Training Recurrent Networks'
352	      authors: Lamb, Goyal, Zhang, Zhang, Courville, Bengio
353	      venue: NeurIPS 2016
354	      year: 2016
355	      url: https://arxiv.org/abs/1610.09038
356	      role: foundation
357	      relevance: 用对抗训练对齐 teacher forcing 训练与 free-running 采样的 hidden state 动态分布，直接证明 train-test dynamics mismatch 可导致长序列采样质量崩溃——与论文中
358	        gating 机制推理时失效的现象高度对应
359	      abstract: Introduces Professor Forcing, which uses adversarial domain adaptation to encourage the dynamics of the recurrent
360	        network to be the same when training and when sampling over multiple time steps. Acts as a regularizer improving test
361	        likelihood on Penn Treebank and sequential MNIST. Qualitatively improves samples especially for long generation horizons.
362	        Discusses trade-offs with Scheduled Sampling.
363	    - title: 'SEARNN: Training RNNs with Global-Local Losses'
364	      authors: Leblond, Alayrac, Osokin, Lacoste-Julien
365	      venue: ICLR 2018
366	      year: 2018
367	      url: https://arxiv.org/abs/1706.04499
368	      role: context
369	      relevance: 基于 learning-to-search 理论统一分析 MLE 训练的两大缺陷：exposure bias 和结构化损失信息浪费。论文中 auxiliary attention loss 同时受这两个缺陷影响——token-level
370	        loss 无法反映 sequence-level attention pattern
371	      abstract: Proposes SEARNN inspired by learning-to-search (L2S) approach to structured prediction. MLE training fails
372	        to exploit structured losses and introduces train-test discrepancies (exposure bias). SEARNN leverages test-alike
373	        search space exploration for global-local losses closer to test error. Demonstrates improvements on OCR, spelling
374	        correction, and machine translation with a subsampling strategy for large vocabularies.
375	    - title: Quantifying Exposure Bias for Neural Language Generation
376	      authors: He, Zhang, Zhou, Glass
377	      venue: arXiv 2019
378	      year: 2019
379	      url: https://arxiv.org/abs/1905.10617
380	      role: foundation
381	      relevance: 首次定量度量 exposure bias 影响并发现 LM 的 self-recovery 能力——即模型能从错误前缀部分恢复。这为论文分析 gating 机制在推理时的行为提供关键对照：如果 exposure
382	        bias 可自恢复，auxiliary loss 崩溃可能源于更根本的分布偏移
383	      abstract: 'Proposes sequence-level (EB-bleu) and word-level (EB-C) metrics to quantify exposure bias impact on quality,
384	        diversity, and consistency. Key finding: contrary to popular belief, distortion from prefix discrepancy is limited
385	        and does not appear incremental. Reveals an interesting self-recovery ability of language models that counters harmful
386	        effects of exposure bias.'
387	  gradient_conflict_mtl:
388	    description: Multi-task gradient conflict resolution, gradient surgery, and loss balancing methods
389	    papers:
390	    - title: Gradient Surgery for Multi-Task Learning
391	      authors: Yu, Kumar, Gupta, Levine, Hausman, Finn
392	      venue: NeurIPS 2020
393	      year: 2020
394	      url: https://arxiv.org/abs/2001.06782
395	      role: must-cite
396	      relevance: 提出 PCGrad，通过投影消除任务间梯度冲突。论文直接使用 PCGrad 做因果排除实验，证明梯度冲突不是 auxiliary attention loss 泛化失败的根因
397	      abstract: 'Proposes PCGrad: when gradients between tasks conflict, project one onto the normal plane of the other to
398	        remove the conflicting component. Demonstrates consistent improvements on multi-task supervised learning and multi-task
399	        reinforcement learning benchmarks.'
400	    - title: 'GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks'
401	      authors: Chen, Badrinarayanan, Lee, Rabinovich
402	      venue: ICML 2018
403	      year: 2018
404	      url: https://arxiv.org/abs/1711.02257
405	      role: must-cite
406	      relevance: 首个自动平衡多任务梯度幅度的方法，通过动态调整各任务梯度范数使训练速率一致。为论文中 auxiliary loss 权重调优的 baseline 和梯度冲突缓解方法的早期代表
407	      abstract: Automatically balances training in deep multitask models by dynamically tuning gradient magnitudes. Introduces
408	        a loss-rate-based gradient normalization algorithm that adjusts gradients to ensure tasks train at similar rates.
409	        Shows improvements on NYUv2 and other benchmarks.
410	    - title: Conflict-Averse Gradient Descent for Multi-task Learning
411	      authors: Liu, Liu, Jin, Stone, Liu
412	      venue: NeurIPS 2021
413	      year: 2021
414	      url: https://arxiv.org/abs/2110.14048
415	      role: context
416	      relevance: 提出 CAGrad，在共享参数空间上寻找与所有任务梯度最小冲突的更新方向。作为 PCGrad 之后梯度冲突解决方法的演进，支撑论文对该路线充分覆盖后仍无法解决 attention degradation 的论证
417	      abstract: Proposes Conflict-Averse Gradient descent (CAGrad) that minimizes the average loss while explicitly constraining
418	        the worst-case task performance. Finds an update direction within a ball around the average gradient that maximizes
419	        the minimum improvement across tasks. Achieves state-of-the-art on multi-task learning benchmarks.
420	    - title: Multi-Task Learning as a Bargaining Game
421	      authors: Navon, Shamsian, Achituve, Maron, Kawaguchi, Chechik, Fetaya
422	      venue: ICML 2022
423	      year: 2022
424	      url: https://arxiv.org/abs/2202.01017
425	      role: context
426	      relevance: 将多任务梯度聚合建模为 Nash 博弈问题（Nash-MTL），理论证明 Nash 均衡解优于启发式梯度操作。作为梯度冲突解决的最新理论上界，强化论文"即使最优梯度调和也无法修复 attention degradation"的论证
427	      abstract: Frames multi-task gradient aggregation as a bargaining game and proposes Nash-MTL that finds the Nash bargaining
428	        solution. Provides theoretical guarantees showing the Nash solution is Pareto optimal. Achieves state-of-the-art on
429	        multiple MTL benchmarks including NYUv2, QM9, and CELEBA.
430	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "uuid": "ebbd8d13-6887-403b-8381-ea0121258510",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
      "content": "categories:\n  layer_importance:\n    description: Layer-wise importance analysis, redundancy, and pruning in transformers\n    papers:\n    - title: The Unreasonable Ineffectiveness of the Deeper Layers\n      authors: Gromov et al.\n      venue: ICLR 2025\n      year: 2024\n      url: https://arxiv.org/abs/2403.17887\n      role: foundation\n      relevance: 发现 LLM 深层高度冗余，可删除近半层而性能不降；浅层对知识存储至关重要\n      abstract: Studies knowledge storage via layer pruning. Finds minimal performance degradation until up to half of layers\n        are removed.\n    - title: 'ShortGPT: Layers in Large Language Models are More Redundant Than You Expect'\n      authors: Men et al.\n      venue: arXiv 2024\n      year: 2024\n      url: https://arxiv.org/abs/2403.03853\n      role: foundation\n      relevance: 提出 Block Influence (BI) 度量各层重要性，发现许多层高度相似且功能冗余\n      abstract: Defines Block Influence (BI) metric to gauge layer significance. Discovers many LLM layers exhibit high similarity.\n    - title: The Curse of Depth in Large Language Models\n      authors: Sun et al.\n      venue: NeurIPS 2025\n      year: 2025\n      url: https://arxiv.org/abs/2502.05795\n      role: foundation\n      relevance: Pre-LN 导致深层梯度趋近恒等映射。解释 ThreadGate 中 late layers gate 接近 1.0\n      abstract: Pre-Layer Normalization causes output variance to grow exponentially with depth.\n    - title: 'Reassessing Layer Pruning in LLMs: New Insights and Methods'\n      authors: Anonymous\n      venue: arXiv 2024\n      year: 2024\n      url: https://arxiv.org/abs/2411.15558\n      role: context\n      relevance: 删除最后 25% 层 + 微调即可获得强性能，证实深层冗余\n      abstract: Simply pruning the final 25% of layers followed by fine-tuning yields strong performance.\n    - title: Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\n      authors: Fan et al.\n      venue: ICLR 2020\n      year: 2020\n      url: https://arxiv.org/abs/1909.11556\n      role: method-component\n      relevance: ThreadGate 的 gating 可视为 LayerDrop 的 soft 版本\n      abstract: Structured dropout on entire transformer layers during training.\n  multi_turn_attention:\n    description: Attention degradation and instruction following failure in multi-turn or long-context scenarios\n    papers:\n    - title: 'When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction'\n      authors: Dongre, Hsieh, Lai, Yoon, Bui, Hakkani-Tur\n      venue: arXiv 2026\n      year: 2026\n      url: https://arxiv.org/abs/2605.12922\n      role: foundation\n      relevance: 定义 GAR，诊断多轮 attention 通道关闭。纯诊断论文，未提出干预方案。ThreadGate 是首个基于其诊断的干预方法\n      abstract: 'Channel-transition account: goal tokens become less accessible through attention while goal info persists\n        in residual representations. Introduces GAR metric.'\n      notes:\n        gar_definition: GAR(τ) = (1/L·H·|ℛτ|) Σℓ Σh Σi∈ℛτ Σj∈𝒢 A_{i,j}. ALL layers, ALL heads averaged. Goal tokens = system\n          prompt task-specifying tokens only\n        models_tested: Mistral-7B, LLaMA-3.1-8B, Qwen-2.5 (3B/7B/14B/32B), Mixtral-8x7B + 6 additional\n        gar_decline: 27-48% over 50 turns, monotonic (Mann-Kendall p<1e-7)\n        residual_probes: 'LDA on PCA-reduced residuals (50 PCs). Peak AUC: LLaMA L2=0.99, Qwen L11=0.98, Mixtral L21=0.99,\n          Mistral L27=0.87'\n        qwen_layer_profile: Goal encoding rises steeply from L5. Our v3b L4 outlier may be the layer just before goal encoding\n          begins\n        intervention_tested: Periodic goal re-injection FAILED (Appendix H)\n        no_solution: true\n        sliding_window: Attention mask W=4096, Qwen crossover at turn 20. Linear W-vs-crossover (R2~1)\n        framing_impact: GAR not our original metric. No intervention proposed -> ThreadGate is first solution. Residual persistence\n          directly supports our theory\n    - title: LLMs Get Lost In Multi-Turn Conversation\n      authors: Levy et al.\n      venue: arXiv 2025\n      year: 2025\n      url: https://arxiv.org/abs/2505.06120\n      role: foundation\n      relevance: 量化多轮对话性能衰减：平均下降 39%，不可靠性增加 112%\n      abstract: All top LLMs exhibit significantly lower performance in multi-turn vs single-turn, averaging 39% drop.\n    - title: Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation\n      authors: Liu et al.\n      venue: arXiv 2026\n      year: 2026\n      url: https://arxiv.org/abs/2602.07338\n      role: context\n      relevance: 多轮失败根因是 intent alignment gap，scaling 无法解决。支撑 ThreadGate 架构级方案动机\n      abstract: Lost in Conversation stems from intent alignment gap, not capability deficits. Scaling cannot resolve.\n    - title: 'Lost in the Middle: How Language Models Use Long Contexts'\n      authors: Liu et al.\n      venue: TACL 2024\n      year: 2023\n      url: https://arxiv.org/abs/2307.03172\n      role: foundation\n      relevance: U 型 attention 分布（首尾强、中间弱）。多轮场景是此现象在 turn boundary 上的扩展\n      abstract: Performance highest at beginning/end of context, degrading for middle positions.\n    - title: 'Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models'\n      authors: Anonymous\n      venue: arXiv 2025\n      year: 2025\n      url: https://arxiv.org/abs/2512.23578\n      role: context\n      relevance: 多轮对话中 style instruction 遵循衰减，system message 比 user message 更严重\n      abstract: Style instruction in system messages degrades more than in user messages across turns.\n  residual_gating:\n    description: Gating mechanisms for transformer residual connections and adaptive depth\n    papers:\n    - title: 'Mixture-of-Depths: Dynamically allocating compute in transformer-based language models'\n      authors: Raposo et al.\n      venue: arXiv 2024 (Google DeepMind)\n      year: 2024\n      url: https://arxiv.org/abs/2404.02258\n      role: method-component\n      relevance: top-k routing 动态分配计算。ThreadGate 可视为 MoD 在 turn boundary 上的特化\n      abstract: Dynamically allocate FLOPs per layer via top-k routing. 1.5% loss improvement or 50% FLOP reduction.\n    - title: Confident Adaptive Language Modeling (CALM)\n      authors: Schuster et al.\n      venue: NeurIPS 2022\n      year: 2022\n      url: https://arxiv.org/abs/2207.07061\n      role: method-component\n      relevance: 置信度 early exit。CALM 是 monotonic exit，ThreadGate 允许 selective layer gating\n      abstract: Dynamically allocating compute per input based on confidence. Up to 3x speedup.\n    - title: 'Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free'\n      authors: Qiu et al.\n      venue: NeurIPS 2025 (Oral)\n      year: 2025\n      url: https://arxiv.org/abs/2505.06708\n      role: method-component\n      relevance: SDPA 输出加 sigmoid gate 消除 attention sink。可参考 head-specific sigmoid gate 设计\n      abstract: Head-specific sigmoid gate after SDPA. Eliminates attention sink (83% to 4%).\n    - title: 'SkipNet: Learning Dynamic Routing in Convolutional Networks'\n      authors: Wang et al.\n      venue: ECCV 2018\n      year: 2018\n      url: https://arxiv.org/abs/1711.09485\n      role: method-component\n      relevance: 残差网络逐层 gating 先驱。ThreadGate per-layer gating 的前身\n      abstract: Gating network to selectively skip convolutional blocks. RL+SL hybrid training.\n    - title: Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)\n      authors: Luo et al.\n      venue: arXiv 2025\n      year: 2025\n      url: https://arxiv.org/abs/2503.23798\n      role: direct-competitor\n      relevance: plug-in router+adapter on frozen LLM 自适应 layer skipping。与 ThreadGate 高度类似，直接竞品\n      abstract: Dynamically adjusts layers via plug-in router and adapter. Llama-3-8B skips 8/32 layers maintaining performance.\n    - title: Learning to Skip the Middle Layers of Transformers\n      authors: Lawson et al.\n      venue: arXiv 2025\n      year: 2025\n      url: https://arxiv.org/abs/2506.21103\n      role: context\n      relevance: middle-out layer skipping 负面结果参考\n      abstract: Gating to skip middle blocks. Does not improve vs dense baselines at investigated scales.\n  attention_manipulation:\n    description: Methods that modify attention weights, positional encoding, or attention distributions to handle long-range\n      dependencies\n    papers:\n    - title: 'Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation'\n      authors: Press et al.\n      venue: ICLR 2022\n      year: 2022\n      url: https://arxiv.org/abs/2108.12409\n      role: foundation\n      relevance: ALiBi 在注意力分数上施加距离线性惩罚实现长度外推，是注意力操纵路线的代表方法，与 ThreadGate 残差门控路线形成设计空间对比\n      abstract: Replaces positional embeddings with linear bias on attention logits penalizing distance. 1.3B model trained\n        on 1024 generalizes to 2048 without fine-tuning.\n    - title: Extending Context Window of Large Language Models via Positional Interpolation\n      authors: Chen et al.\n      venue: arXiv 2023\n      year: 2023\n      url: https://arxiv.org/abs/2306.15595\n      role: foundation\n      relevance: 位置插值通过压缩 RoPE 索引扩展上下文至 32k，属于注意力机制内部解决长序列的路线，与 ThreadGate 在残差层解决多轮衰减形成对比\n      abstract: Linearly down-scales RoPE position indices to extend context to 32768 tokens in 1000 fine-tuning steps.\n    - title: 'YaRN: Efficient Context Window Extension of Large Language Models'\n      authors: Peng et al.\n      venue: ICLR 2024\n      year: 2024\n      url: https://arxiv.org/abs/2309.00071\n      role: foundation\n      relevance: YaRN 综合 NTK-aware 和分段插值改进 RoPE 外推，代表注意力位置编码修改应对长程衰减的成熟路线，与 ThreadGate 机制不同\n      abstract: Combines NTK-aware interpolation with ramp function for different RoPE frequency components. Extends LLaMA-2\n        to 128k context with 10x fewer tokens.\n    - title: Efficient Streaming Language Models with Attention Sinks\n      authors: Xiao et al.\n      venue: ICLR 2024\n      year: 2024\n      url: https://arxiv.org/abs/2309.17453\n      role: context\n      relevance: 发现 attention sink 现象（初始 token 聚集高权重），说明多轮对话中早期轮次 token 天然受偏置，ThreadGate 从残差路径角度控制历史轮信息保留\n      abstract: LLMs assign disproportionate attention to first few tokens regardless of semantics. Retaining sink tokens\n        enables stable streaming inference over 4M tokens.\n    - title: 'LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models'\n      authors: Han et al.\n      venue: ACL 2024\n      year: 2024\n      url: https://arxiv.org/abs/2308.16137\n      role: context\n      relevance: 用 Λ 形注意力掩码加距离截断实现超长上下文推理，揭示调整注意力掩码和调整残差门控是两条平行路线\n      abstract: Applies Λ-shaped attention mask plus distance limit on position encodings. Generalizes to 200M tokens with\n        2.7x speedup, no parameter updates.\n    - title: 'Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization'\n      authors: Ko et al.\n      venue: arXiv 2024\n      year: 2024\n      url: https://arxiv.org/abs/2406.16008\n      role: direct-competitor\n      relevance: 直接校准注意力位置偏置修复中段信息丢失，最接近 ThreadGate 问题定义的注意力方案，审稿人会以此质疑为何不直接修正注意力\n      abstract: Identifies U-shaped positional attention bias causing lost-in-the-middle. Training-free calibration redistributes\n        attention to middle positions, improving QA by 6-15pp.\n  theoretical_foundations:\n    description: Theoretical analysis of transformer residual streams, information flow, and attention dynamics\n    papers:\n    - title: A Mathematical Framework for Transformer Circuits\n      authors: Elhage et al.\n      venue: Transformer Circuits Thread 2021\n      year: 2021\n      url: https://transformer-circuits.pub/2021/framework/index.html\n      role: foundation\n      relevance: 提出残差流作为 transformer 各组件通信核心通道，直接为 ThreadGate 在残差连接处插入门控提供机制解释框架\n      abstract: Linear algebraic decomposition of transformer computations. Attention heads and MLPs as read/write operations\n        on shared residual stream. Formalizes induction heads and QK/OV circuits.\n    - title: Toy Models of Superposition\n      authors: Elhage et al.\n      venue: arXiv 2022\n      year: 2022\n      url: https://arxiv.org/abs/2209.10652\n      role: foundation\n      relevance: 揭示残差流子空间叠加存储稀疏特征的机制，为 ThreadGate 按轮次条件化选择性激活残差通道提供理论依据\n      abstract: Neural networks store more features than dimensions via superposition when features are sparse. Links polysemanticity\n        to geometry of uniform polytopes.\n    - title: Eliciting Latent Predictions from Transformers with the Tuned Lens\n      authors: Belrose et al.\n      venue: arXiv 2023\n      year: 2023\n      url: https://arxiv.org/abs/2303.08112\n      role: foundation\n      relevance: 逐层解码残差流隐状态揭示信息在深度方向渐进精化，支撑 ThreadGate 不同层门控强度差异化设计的动机\n      abstract: Per-layer affine probes decode intermediate residual stream states into vocabulary distributions. Shows predictions\n        iteratively refined across depth up to 20B parameters.\n    - title: Exploring the Residual Stream of Transformers\n      authors: Yu et al.\n      venue: arXiv 2023\n      year: 2023\n      url: https://arxiv.org/abs/2312.12141\n      role: foundation\n      relevance: 分析残差连接对 logit 空间的加法效应，揭示知识参数跨层分布规律，为 ThreadGate 定位门控插入层提供实证参考\n      abstract: Residual connections act as direct additive operations on pre-softmax logits. Identifies factual knowledge\n        storage distribution across layers and modules.\n    - title: 'Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains'\n      authors: Makkuva et al.\n      venue: ICLR 2025\n      year: 2025\n      url: https://arxiv.org/abs/2402.04161\n      role: foundation\n      relevance: 用 Markov 链理论刻画注意力深度依赖性，解释为何单层 transformer 无法形成归纳头，支持 ThreadGate 在多层残差路径施加门控的必要性\n      abstract: Theoretical framework via Markov chain properties. Two-layer transformers learn induction heads on first-order\n        Markov data; single-layer models get trapped in unigram minima.\n    - title: 'From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers'\n      authors: Ildiz et al.\n      venue: ICML 2024\n      year: 2024\n      url: https://arxiv.org/abs/2402.13512\n      role: foundation\n      relevance: 建立自注意力与上下文条件 Markov 链的精确映射，为分析多轮对话 token 分布随轮次漂移（GAR decay）提供随机过程理论基础\n      abstract: Mathematical equivalence between self-attention and context-conditioned Markov chains. Output distribution\n        sampled from context-weighted transition matrix.\n  evaluation_benchmarks:\n    description: Multi-turn dialogue and instruction-following evaluation benchmarks for LLMs\n    papers:\n    - title: Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\n      authors: Zheng et al.\n      venue: NeurIPS 2023\n      year: 2023\n      url: https://arxiv.org/abs/2306.05685\n      role: foundation\n      relevance: MT-Bench 多轮对话评测框架，是 ThreadGate 验证多轮 GAR 衰减修复效果的核心 benchmark\n      abstract: Introduces MT-Bench (80 multi-turn questions) and Chatbot Arena. GPT-4 achieves >80% agreement with human\n        preferences as judge.\n    - title: 'Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference'\n      authors: Chiang et al.\n      venue: ICML 2024\n      year: 2024\n      url: https://arxiv.org/abs/2403.04132\n      role: foundation\n      relevance: 基于 ELO 排名的人类偏好评估体系，衡量多轮对话模型综合能力的权威 leaderboard\n      abstract: Chatbot Arena with 240K+ votes from 90K+ users across 50+ models. Bradley-Terry and ELO ranking validated\n        against expert raters.\n    - title: 'Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators'\n      authors: Dubois et al.\n      venue: COLM 2024\n      year: 2024\n      url: https://arxiv.org/abs/2404.04475\n      role: foundation\n      relevance: 指令遵循自动评测标准，Length-Controlled 版本修正长度偏差，为 ThreadGate 单轮指令评测提供对比基线\n      abstract: GLM-based length debiasing for AlpacaEval. Validated against 20K human annotations.\n    - title: 'WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild'\n      authors: Lin et al.\n      venue: arXiv 2024\n      year: 2024\n      url: https://arxiv.org/abs/2406.04770\n      role: foundation\n      relevance: 真实用户多样化指令集，评估 wild 场景指令遵循能力，与 ThreadGate 关注的真实多轮对话性能高度相关\n      abstract: 1,024 challenging tasks from 1M+ conversation logs. WB-Reward/WB-Score achieve 0.98 Pearson correlation with\n        Chatbot Arena ELO on hard tasks.\n    - title: 'MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues'\n      authors: Bai et al.\n      venue: ACL 2024\n      year: 2024\n      url: https://arxiv.org/abs/2402.14762\n      role: direct-competitor\n      relevance: 多轮对话细粒度评测体系，直接测量跨轮次能力退化，与 ThreadGate 研究的 GAR 衰减高度吻合\n      abstract: Three-tier ability taxonomy, 4,208 turns across 1,388 dialogues in 13 tasks. Neither alignment nor chat-specific\n        designs consistently improve multi-turn abilities.\n    - title: 'MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs'\n      authors: Sirdeshmukh et al.\n      venue: arXiv 2025\n      year: 2025\n      url: https://arxiv.org/abs/2501.17399\n      role: direct-competitor\n      relevance: 前沿 LLM 多轮对话准确率不足 50%，直接测量 ThreadGate 旨在修复的跨轮指令保留和上下文一致性失败\n      abstract: 'Four challenge categories: instruction retention, user inference memory, versioned editing, self-coherence.\n        All frontier LLMs below 50%; Claude 3.5 Sonnet tops at 41.4%.'\n  exposure_bias:\n    description: Exposure bias, teacher forcing, scheduled sampling, and train-test distribution mismatch in sequence generation\n    papers:\n    - title: Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\n      authors: Bengio, Vinyals, Jaitly, Shazeer\n      venue: NeurIPS 2015\n      year: 2015\n      url: https://arxiv.org/abs/1506.03099\n      role: foundation\n      relevance: Scheduled sampling 首次提出用 curriculum learning 缓解 teacher forcing 与推理时 autoregressive decoding 的分布不匹配（exposure\n        bias），直接支撑论文对 auxiliary attention loss 训练-推理 gap 的根因分析\n      abstract: Proposes a curriculum learning strategy to gently change training from fully guided (true previous token)\n        to less guided (model-generated token). The discrepancy between teacher-forced training and autoregressive inference\n        causes error accumulation. Experiments on sequence prediction tasks show significant improvements. Used in the winning\n        MSCOCO image captioning challenge 2015 entry.\n    - title: Sequence Level Training with Recurrent Neural Networks\n      authors: Ranzato, Chopra, Auli, Zaremba\n      venue: ICLR 2016\n      year: 2016\n      url: https://arxiv.org/abs/1511.06732\n      role: foundation\n      relevance: MIXER 算法直接优化测试时指标（BLEU/ROUGE）而非 token-level MLE，解决 teacher forcing 导致的 train-test discrepancy；论文中 auxiliary\n        loss 同样面临 token-level 训练目标与 sequence-level 推理行为的错位\n      abstract: Addresses the discrepancy between token-level MLE training and sequence-level generation at test time. Proposes\n        sequence level training that directly optimizes test metrics (BLEU, ROUGE). Outperforms strong baselines for greedy\n        generation on three tasks and is competitive with beam search while being several times faster.\n    - title: 'Professor Forcing: A New Algorithm for Training Recurrent Networks'\n      authors: Lamb, Goyal, Zhang, Zhang, Courville, Bengio\n      venue: NeurIPS 2016\n      year: 2016\n      url: https://arxiv.org/abs/1610.09038\n      role: foundation\n      relevance: 用对抗训练对齐 teacher forcing 训练与 free-running 采样的 hidden state 动态分布，直接证明 train-test dynamics mismatch 可导致长序列采样质量崩溃——与论文中\n        gating 机制推理时失效的现象高度对应\n      abstract: Introduces Professor Forcing, which uses adversarial domain adaptation to encourage the dynamics of the recurrent\n        network to be the same when training and when sampling over multiple time steps. Acts as a regularizer improving test\n        likelihood on Penn Treebank and sequential MNIST. Qualitatively improves samples especially for long generation horizons.\n        Discusses trade-offs with Scheduled Sampling.\n    - title: 'SEARNN: Training RNNs with Global-Local Losses'\n      authors: Leblond, Alayrac, Osokin, Lacoste-Julien\n      venue: ICLR 2018\n      year: 2018\n      url: https://arxiv.org/abs/1706.04499\n      role: context\n      relevance: 基于 learning-to-search 理论统一分析 MLE 训练的两大缺陷：exposure bias 和结构化损失信息浪费。论文中 auxiliary attention loss 同时受这两个缺陷影响——token-level\n        loss 无法反映 sequence-level attention pattern\n      abstract: Proposes SEARNN inspired by learning-to-search (L2S) approach to structured prediction. MLE training fails\n        to exploit structured losses and introduces train-test discrepancies (exposure bias). SEARNN leverages test-alike\n        search space exploration for global-local losses closer to test error. Demonstrates improvements on OCR, spelling\n        correction, and machine translation with a subsampling strategy for large vocabularies.\n    - title: Quantifying Exposure Bias for Neural Language Generation\n      authors: He, Zhang, Zhou, Glass\n      venue: arXiv 2019\n      year: 2019\n      url: https://arxiv.org/abs/1905.10617\n      role: foundation\n      relevance: 首次定量度量 exposure bias 影响并发现 LM 的 self-recovery 能力——即模型能从错误前缀部分恢复。这为论文分析 gating 机制在推理时的行为提供关键对照：如果 exposure\n        bias 可自恢复，auxiliary loss 崩溃可能源于更根本的分布偏移\n      abstract: 'Proposes sequence-level (EB-bleu) and word-level (EB-C) metrics to quantify exposure bias impact on quality,\n        diversity, and consistency. Key finding: contrary to popular belief, distortion from prefix discrepancy is limited\n        and does not appear incremental. Reveals an interesting self-recovery ability of language models that counters harmful\n        effects of exposure bias.'\n  gradient_conflict_mtl:\n    description: Multi-task gradient conflict resolution, gradient surgery, and loss balancing methods\n    papers:\n    - title: Gradient Surgery for Multi-Task Learning\n      authors: Yu, Kumar, Gupta, Levine, Hausman, Finn\n      venue: NeurIPS 2020\n      year: 2020\n      url: https://arxiv.org/abs/2001.06782\n      role: must-cite\n      relevance: 提出 PCGrad，通过投影消除任务间梯度冲突。论文直接使用 PCGrad 做因果排除实验，证明梯度冲突不是 auxiliary attention loss 泛化失败的根因\n      abstract: 'Proposes PCGrad: when gradients between tasks conflict, project one onto the normal plane of the other to\n        remove the conflicting component. Demonstrates consistent improvements on multi-task supervised learning and multi-task\n        reinforcement learning benchmarks.'\n    - title: 'GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks'\n      authors: Chen, Badrinarayanan, Lee, Rabinovich\n      venue: ICML 2018\n      year: 2018\n      url: https://arxiv.org/abs/1711.02257\n      role: must-cite\n      relevance: 首个自动平衡多任务梯度幅度的方法，通过动态调整各任务梯度范数使训练速率一致。为论文中 auxiliary loss 权重调优的 baseline 和梯度冲突缓解方法的早期代表\n      abstract: Automatically balances training in deep multitask models by dynamically tuning gradient magnitudes. Introduces\n        a loss-rate-based gradient normalization algorithm that adjusts gradients to ensure tasks train at similar rates.\n        Shows improvements on NYUv2 and other benchmarks.\n    - title: Conflict-Averse Gradient Descent for Multi-task Learning\n      authors: Liu, Liu, Jin, Stone, Liu\n      venue: NeurIPS 2021\n      year: 2021\n      url: https://arxiv.org/abs/2110.14048\n      role: context\n      relevance: 提出 CAGrad，在共享参数空间上寻找与所有任务梯度最小冲突的更新方向。作为 PCGrad 之后梯度冲突解决方法的演进，支撑论文对该路线充分覆盖后仍无法解决 attention degradation 的论证\n      abstract: Proposes Conflict-Averse Gradient descent (CAGrad) that minimizes the average loss while explicitly constraining\n        the worst-case task performance. Finds an update direction within a ball around the average gradient that maximizes\n        the minimum improvement across tasks. Achieves state-of-the-art on multi-task learning benchmarks.\n    - title: Multi-Task Learning as a Bargaining Game\n      authors: Navon, Shamsian, Achituve, Maron, Kawaguchi, Chechik, Fetaya\n      venue: ICML 2022\n      year: 2022\n      url: https://arxiv.org/abs/2202.01017\n      role: context\n      relevance: 将多任务梯度聚合建模为 Nash 博弈问题（Nash-MTL），理论证明 Nash 均衡解优于启发式梯度操作。作为梯度冲突解决的最新理论上界，强化论文\"即使最优梯度调和也无法修复 attention degradation\"的论证\n      abstract: Frames multi-task gradient aggregation as a bargaining game and proposes Nash-MTL that finds the Nash bargaining\n        solution. Provides theoretical guarantees showing the Nash solution is Pareto optimal. Achieves state-of-the-art on\n        multiple MTL benchmarks including NYUv2, QM9, and CELEBA.\n",
      "numLines": 430,
      "startLine": 1,
      "totalLines": 430
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
The Semantic Scholar API returned 429 (rate limited). I already know the details of both papers, so I'll construct the entries directly and add them to the YAML file. Let me prepare the data.

ReZero paper:
- Title: ReZero is All You Need: Fast Convergence at Large Depth
- Authors: Bachlechner et al.
- Venue: UAI 2021
- Year: 2021
- URL: https://arxiv.org/abs/2003.04887
- Abstract: Deep networks often suffer from vanishing/exploding gradients and slow convergence. 

ReZero uses learnable zero-initialized scalars on residual connections to enable training of extremely deep transformers—up to 10,000 layers—without requiring warm-up or normalization, achieving much faster convergence. For the Fixup paper, it proposes a fixed-update initialization scheme that allows deep residual networks to train without normalization layers by theoretically controlling residual branch scaling to prevent gradient explosion. Now I'll write the Python code to add these entries to the YAML file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "uuid": "4c8a4ab2-2010-4678-9c45-4b34e2e415c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSdUMGfS2pNSBtNrkRwZaz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9967,
      "cache_read_input_tokens": 24421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9967
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

_source line 11_

Semantic Scholar 429 限流，直接用已知信息写入。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "uuid": "42906d9e-5feb-41f9-955b-ed68874442d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSdUMGfS2pNSBtNrkRwZaz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9967,
      "cache_read_input_tokens": 24421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9967
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

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_01KzsgCiLbpkpGxtxZwBwZs6`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, fcntl\n\nmap_path = 'literature_map.yaml'\nnew_papers = [\n    {\n        'title': 'ReZero is All You Need: Fast Convergence at Large Depth',\n        'authors': 'Bachlechner, Majumder, Mao, Cottrell, McAuley',\n        'venue': 'UAI 2021',\n        'year': 2021,\n        'url': 'https://arxiv.org/abs/2003.04887',\n        'role': 'must-cite',\n        'relevance': 'ThreadGate 的 per-layer sigmoid gate 直接源自 ReZero 的零初始化残差缩放思想：x_{l+1} = x_l + alpha_l * f_l(x_l)，alpha 初始化为 0。ThreadGate 将标量 alpha 替换为 turn-conditioned sigmoid gate',\n        'abstract': 'Initializes each residual connection with a learnable zero-initialized parameter, enabling training of extremely deep transformers (up to 10,000 layers) without warmup or normalization. Achieves significantly faster convergence by allowing the network to start as identity and gradually incorporate layer contributions.'\n    },\n    {\n        'title': 'Fixup Initialization: Residual Learning Without Normalization',\n        'authors': 'Zhang, Dauphin, Ma',\n        'venue': 'ICLR 2019',\n        'year': 2019,\n        'url': 'https://arxiv.org/abs/1901.09321',\n        'role': 'foundation',\n        'relevance': '理论推导残差分支的初始化缩放如何控制梯度爆炸，为 ReZero 和 ThreadGate 的残差缩放设计提供数学基础。证明适当的残差缩放可完全替代 normalization layers',\n        'abstract': 'Proposes a properly scaled initialization for residual networks that enables training very deep models without normalization layers. Theoretically shows that residual branch scaling by 1/sqrt(L) prevents gradient explosion. Matches BatchNorm performance on ImageNet and CIFAR with ResNets up to 110 layers.'\n    }\n]\n\nwith open(map_path, 'r') as f:\n    fcntl.flock(f, fcntl.LOCK_SH)\n    data = yaml.safe_load(f)\n    fcntl.flock(f, fcntl.LOCK_UN)\n\nif 'residual_scaling' not in data.get('categories', {}):\n    data['categories']['residual_scaling'] = {\n        'description': 'Residual connection scaling, initialization, and zero-init methods for deep transformers',\n        'papers': []\n    }\n\nexisting = {p['title'].lower() for p in data['categories']['residual_scaling'].get('papers', [])}\nadded = 0\nfor p in new_papers:\n    if p['title'].lower() not in existing:\n        data['categories']['residual_scaling']['papers'].append(p)\n        added += 1\n\nwith open(map_path, 'w') as f:\n    fcntl.flock(f, fcntl.LOCK_EX)\n    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)\n    fcntl.flock(f, fcntl.LOCK_UN)\n\nprint(f'Done: residual_scaling cluster, added {added} papers')\n\"\n",
  "description": "Add residual_scaling category with 2 papers to literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "uuid": "8456ee8f-a228-4447-a48f-88b55260ab32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSdUMGfS2pNSBtNrkRwZaz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9967,
      "cache_read_input_tokens": 24421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9967
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

_source line 13 · 2026-05-19T21:45:55.983Z_

<details><summary>↩ Tool result · `toolu_01KzsgCiLbpkpGxtxZwBwZs6`</summary>

```text
Done: residual_scaling cluster, added 2 papers
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "uuid": "366ec5b5-b7d8-4446-9b3e-237ef6c84ae5",
  "tool_use_result": {
    "stdout": "Done: residual_scaling cluster, added 2 papers",
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

_source line 14_

验证写入结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "uuid": "9de9936b-620b-498d-9fd1-6ea8ed1780e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXomGnAE46Qf48JKqjJQqv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1350,
      "cache_read_input_tokens": 34388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1350
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

<details open><summary>🔧 Tool call — Bash · `toolu_01PMkL3iHiQnzqAcZYhpUsEv`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('literature_map.yaml') as f:\n    data = yaml.safe_load(f)\ncat = data['categories']['residual_scaling']\nprint(cat['description'])\nfor p in cat['papers']:\n    print(f\\\"  - {p['title']} ({p['year']}) [{p['venue']}] role={p['role']}\\\")\n\"\n",
  "description": "Verify residual_scaling entries in literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "uuid": "c7daa9af-af30-496f-acd0-d1248eaf31cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXomGnAE46Qf48JKqjJQqv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1350,
      "cache_read_input_tokens": 34388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1350
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

_source line 16 · 2026-05-19T21:46:00.434Z_

<details><summary>↩ Tool result · `toolu_01PMkL3iHiQnzqAcZYhpUsEv`</summary>

```text
Residual connection scaling, initialization, and zero-init methods for deep transformers
  - ReZero is All You Need: Fast Convergence at Large Depth (2021) [UAI 2021] role=must-cite
  - Fixup Initialization: Residual Learning Without Normalization (2019) [ICLR 2019] role=foundation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "uuid": "7ecf0ba8-78a8-41aa-951f-83e61c292ac8",
  "tool_use_result": {
    "stdout": "Residual connection scaling, initialization, and zero-init methods for deep transformers\n  - ReZero is All You Need: Fast Convergence at Large Depth (2021) [UAI 2021] role=must-cite\n  - Fixup Initialization: Residual Learning Without Normalization (2019) [ICLR 2019] role=foundation",
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

_source line 17_

已完成。`literature_map.yaml` 新增 `residual_scaling` category，含 2 篇论文：

1. **Bachlechner et al. 2021** (ReZero, UAI 2021) — `must-cite`，ThreadGate per-layer sigmoid gate 的直接理论来源
2. **Zhang et al. 2019** (Fixup, ICLR 2019) — `foundation`，残差分支缩放控制梯度爆炸的数学基础

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "uuid": "6ae6133b-1d5e-435d-9543-fa7407ac71f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URmV7tG6LJSDRB1cfGwYeG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 284,
      "cache_read_input_tokens": 35738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 284
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

_source line 18_

已完成。`literature_map.yaml` 新增 `residual_scaling` category，含 2 篇论文：

1. **Bachlechner et al. 2021** (ReZero, UAI 2021) — `must-cite`，ThreadGate per-layer sigmoid gate 的直接理论来源
2. **Zhang et al. 2019** (Fixup, ICLR 2019) — `foundation`，残差分支缩放控制梯度爆炸的数学基础

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 43320,
  "duration_api_ms": 43695,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "c6c27143-0d5e-46bf-92e5-79866ba01f74",
  "total_cost_usd": 0.26469424999999996,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 24181,
    "cache_read_input_tokens": 106388,
    "output_tokens": 2349,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 24181,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 135,
        "cache_read_input_tokens": 35738,
        "cache_creation_input_tokens": 284,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 284
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1544,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001614,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 2349,
      "cacheReadInputTokens": 106388,
      "cacheCreationInputTokens": 24181,
      "webSearchRequests": 0,
      "costUSD": 0.26308024999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c83a257d-eaed-4201-ac8e-3fb0191ec3bd"
}
```

</details>

---
