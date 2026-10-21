# paper research

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_paper_research_20260516T083800.log`
- **Structured JSON:** [`6b65a215b3f0b58177b7.json`](../../sessions/6b/6b65a215b3f0b58177b7.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
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
  "uuid": "33cca12d-e5b7-4bf5-91a6-d9bbd0ffc2a9",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/memory/"
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
    "resetsAt": 1778921400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "5a83e523-e8a3-49a6-a1d4-76b92540bff9",
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The task is to supplement the literature_map.yaml with 2-3 papers about contextual sparsity prediction, focusing on PowerInfer and recent 2025-2026 works. Let me start by reading the existing literature_map.yaml to understand the format, then search for the papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "9573e3e1-61a7-4a8c-997e-e5621aae5f01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXcHYa1E6zE4KfNJ51LHNi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11937,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11937
      },
      "output_tokens": 37,
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

Let me first read the existing literature_map.yaml to understand the format, then search for relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "b0fb857d-52db-4ab1-9c4b-b4a092212af4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXcHYa1E6zE4KfNJ51LHNi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11937,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11937
      },
      "output_tokens": 37,
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

<details open><summary>🔧 Tool call — Read · `toolu_01KWQcP8tMbKt7UKDeeRGjUd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "9afba4a0-058c-4900-ac24-1c4084424100",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXcHYa1E6zE4KfNJ51LHNi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11937,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11937
      },
      "output_tokens": 37,
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

_source line 7 · 2026-05-16T08:38:13.776Z_

<details><summary>↩ Tool result · `toolu_01KWQcP8tMbKt7UKDeeRGjUd`</summary>

```text
1	# Literature Map: KL Distillation for Sparse SwiGLU Activation Prediction
2	# Last updated: 2026-05-15
3	# Survey scope: 2023-2026, 4 directions
4	
5	# =============================================================================
6	# Direction 1: KL distillation for structured/activation sparsity
7	# Finding: NO prior work uses KL to train an activation sparsity PREDICTOR.
8	# Existing predictors use BCE (DejaVu, ShadowLLM). SPON uses KL but for
9	# learnable bias correction, not predictor training. This is our novelty.
10	# =============================================================================
11	
12	- title: "Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models"
13	  authors: [Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, Tengfei Ma]
14	  venue: ICML 2026
15	  year: 2026
16	  arxiv_id: "2512.12744"
17	  category: direct-competitor
18	  role: "最接近的KL蒸馏用于稀疏性的工作——但SPON训练的是可学习bias项而非predictor"
19	  key_finding: "SPON注入input-independent learnable activation vectors作为sparse computation的anchor，用KL散度(dense vs sparse logits)做distribution matching训练，训练后吸收进bias项，零推理开销"
20	  relevance_to_us: "SPON证明KL divergence比BCE/MSE更适合sparsity场景的distribution matching。但SPON是全局bias correction而非per-token predictor——我们的predictor方案能实现input-dependent的sparsity pattern，比SPON更灵活。SPON在50-60% sparsity下测试，与我们目标一致"
21	
22	- title: "Compact Language Models via Pruning and Knowledge Distillation"
23	  authors: [Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz, Pavlo Molchanov]
24	  venue: NeurIPS 2024
25	  year: 2024
26	  arxiv_id: "2407.14679"
27	  category: method-component
28	  role: "KL蒸馏用于结构化剪枝后恢复——验证logit-only KL优于intermediate matching"
29	  key_finding: "Minitron用logit-only forward KL divergence做structured pruning后的distillation recovery，发现仅用KL loss（不用CE或intermediate matching）效果最好，学生模型继承了teacher的inter-token关系和confidence calibration"
30	  relevance_to_us: "支持我们的核心假设：KL divergence保留output distribution比逐元素BCE更优。Minitron的发现（logit-only KL最优）为我们predictor的KL训练目标提供了理论支撑"
31	
32	- title: "Instruction-Following Pruning for Large Language Models"
33	  authors: [Bairu Hou, Qibin Chen, Jianyu Wang, Guoli Yin, Chong Wang, Nan Du, Ruoming Pang, Shiyu Chang, Tao Lei]
34	  venue: ICML 2025
35	  year: 2025
36	  arxiv_id: "2501.02086"
37	  category: method-component
38	  role: "训练sparse mask predictor的范式——input-dependent mask selection"
39	  key_finding: "训练一个sparse mask predictor以instruction为输入动态选择最相关参数子集，联合优化mask predictor和LLM"
40	  relevance_to_us: "架构上与我们类似（训练predictor生成mask），但目标是instruction-aware weight pruning而非activation sparsity。可参考其predictor-LLM联合优化策略"
41	
42	# =============================================================================
43	# Direction 2: Output distribution preservation in pruning/sparsity
44	# =============================================================================
45	
46	- title: "Distilling to Hybrid Attention Models via KL-Guided Layer Selection"
47	  authors: []
48	  venue: arXiv
49	  year: 2025
50	  arxiv_id: "2512.20569"
51	  category: method-component
52	  role: "KL散度引导layer selection——用distribution差异决定哪些层需要保留"
53	  key_finding: "用KL divergence作为指标选择哪些attention层替换为hybrid attention，通过最小化output distribution变化来指导架构决策"
54	  relevance_to_us: "方法论启示：KL divergence不仅可作为训练loss，还可作为layer-wise重要性指标。我们可用per-layer KL分析哪些层的sparsity对output distribution影响最大"
55	
56	# =============================================================================
57	# Direction 3: SPON和类似的learnable bias correction for sparsity
58	# =============================================================================
59	
60	- title: "Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity"
61	  authors: [Aayush Gautam, Mukul Gagrani, Junyoung Park, Mingu Lee, Chiris Lott, Narasimha Reddy]
62	  venue: arXiv
63	  year: 2026
64	  arxiv_id: "2602.00397"
65	  category: direct-competitor
66	  role: "Predictor + error compensation双组件架构——与SPON的bias correction思路互补"
67	  key_finding: "组合三个组件：(1) lightweight expert predictor选择high-importance neurons，(2) error compensation network修正sparsity误差，(3) layer-wise sparsity scheduler分配计算。50% FFN sparsity下达到1.45x prefill加速"
68	  relevance_to_us: "与我们的方案最可比：都用predictor做activation sparsity。我们的差异在于用KL loss训练predictor而非BCE，且不需要额外的error compensation网络（KL loss本身应该能减少distribution shift）"
69	
70	- title: "Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models"
71	  authors: [Tai An, Ruwu Cai, Yanzhe Zhang, Yang Liu, Hao Chen, Pengcheng Xie, Sheng Chang, Yiwu Yao, Gongyi Wang]
72	  venue: arXiv
73	  year: 2025
74	  arxiv_id: "2508.02128"
75	  category: background
76	  role: "N:M structured activation sparsity——hardware-friendly的sparsity pattern"
77	  key_finding: "Training-free的top-k策略在linear projection层内确定N:M activation masks，在2:4/4:8/8:16多种ratio下有效，可与W8A8量化组合"
78	  relevance_to_us: "如果我们的predictor输出改为N:M structured pattern而非unstructured binary mask，可获得更好的hardware加速。值得作为future work"
79	
80	# =============================================================================
81	# Direction 4: Predictor-based activation sparsity (TEAL, DejaVu, PowerInfer等)
82	# =============================================================================
83	
84	- title: "Training-Free Activation Sparsity in Large Language Models"
85	  authors: [James Liu, Pragaash Ponnusamy, Tianle Cai, Han Guo, Yoon Kim, Ben Athiwaratkun]
86	  venue: ICLR 2025 (Spotlight)
87	  year: 2025
88	  arxiv_id: "2408.14690"
89	  category: direct-competitor
90	  role: "TEAL——我们的主要baseline，training-free magnitude pruning"
91	  key_finding: "对所有hidden states施加magnitude-based sparsity（不需训练），在40-50% sparsity下性能降低很小，Llama-2/3和Mistral 7B-70B上验证。50% sparsity下1.8x decoding加速"
92	  relevance_to_us: "TEAL用BCE度量sparsity mask质量（二元对错），我们的核心论点是：BCE只看neuron是否激活的对错，忽略了错误预测对output distribution的差异化影响。KL loss应该能让predictor学到'哪些neuron的错误预测对output影响更大'"
93	
94	- title: "Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time"
95	  authors: [Zichang Liu, Jue Wang, Tri Dao, Tianyi Zhou, Binhang Yuan, Zhao Song, Anshumali Shrivastava, Ce Zhang, Yuandong Tian, Christopher Re, Beidi Chen]
96	  venue: ICML 2023
97	  year: 2023
98	  arxiv_id: "2310.17157"
99	  category: direct-competitor
100	  role: "Predictor-based contextual sparsity的开创性工作——我们的直接对比对象"
101	  key_finding: "用两层MLP predictor预测每层的contextual sparsity pattern（哪些attention heads和MLP neurons可跳过），在OPT-175B上实现2x加速。Predictor用BCE训练"
102	  relevance_to_us: "DejaVu是predictor-based sparsity的baseline。其predictor用BCE训练——我们改用KL loss训练类似的predictor。关键差异：DejaVu在per-neuron level用BCE，我们在output distribution level用KL"
103	
104	- title: "ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models"
105	  authors: [Yash Akhauri, Ahmed F AbouElhamayed, Jordan Dotzel, Zhiru Zhang, Alexander M Rush, Safeen Huda, Mohamed S Abdelfattah]
106	  venue: EMNLP 2024
107	  year: 2024
108	  arxiv_id: "2406.16635"
109	  category: direct-competitor
110	  role: "DejaVu的改进——更好的predictor架构和sparsity pattern enforcement"
111	  key_finding: "Shadow predictor超越magnitude-based pruning，context-dependent评估attention head和neuron重要性。比DejaVu端到端精度提升15%，速度提升20%"
112	  relevance_to_us: "ShadowLLM改进了predictor架构但仍用BCE-style loss。我们的改进方向正交：不改predictor架构，改训练loss（BCE→KL）。两种改进可能互补"
113	
114	- title: "SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference"
115	  authors: [Jiho Shin, Hoeseok Yang, Youngmin Yi]
116	  venue: DATE 2025
117	  year: 2025
118	  arxiv_id: "2411.12692"
119	  category: background
120	  role: "Training-free sign-bit predictor——极低开销的sparsity预测"
121	  key_finding: "仅比较input和weight的sign bits预测activation sparsity，无需训练。仅适用于ReLU-based LLMs，不适用SwiGLU"
122	  relevance_to_us: "不适用于SwiGLU模型（我们的目标），但其sign-bit方法的简洁性值得参考。SwiGLU缺乏天然sparsity证明trained predictor的必要性"
123	
124	- title: "SVD Contextual Sparsity Predictors for Fast LLM Inference"
125	  authors: [Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, C.C. Korikov]
126	  venue: arXiv
127	  year: 2026
128	  arxiv_id: "2603.14110"
129	  category: direct-competitor
130	  role: "Training-free SVD-based sparsity predictor——用gate projection矩阵的SVD做预测"
131	  key_finding: "对ReGLU FFN的gate projection矩阵做truncation-aware SVD构建sparse pattern predictor，90% FFN sparsity下1.8x decoding加速，benchmark降低<1%"
132	  relevance_to_us: "虽然是training-free competitor，但focus在ReGLU（不是SwiGLU）且需要90%天然稀疏性。我们的方法在SwiGLU的50%目标sparsity下工作，使用场景不同"
133	
134	- title: "CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models"
135	  authors: [Donghyun Lee, Je-Yong Lee, Genghan Zhang, Mo Tiwari, Azalia Mirhoseini]
136	  venue: arXiv
137	  year: 2024
138	  arxiv_id: "2404.08763"
139	  category: direct-competitor
140	  role: "Contextual thresholding——不训练predictor，用统计threshold做sparsity"
141	  key_finding: "为每个MLP层计算SiLU(x)激活的percentile threshold做sparsification，50% sparsity下性能降低1-2%，无需fine-tuning。Mistral-7B和Llama2-7B上验证"
142	  relevance_to_us: "CATS直接在SwiGLU/SiLU模型上工作，是我们的直接competitor。但CATS是固定threshold不考虑input context，我们的trained predictor是input-dependent的，理论上更优"
143	
144	- title: "R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference"
145	  authors: [Zhenyu Zhang, Zechun Liu, Yuandong Tian, Harshit Khaitan, Zhangyang Wang, Steven Li]
146	  venue: ICLR 2025
147	  year: 2025
148	  arxiv_id: "2504.19449"
149	  category: background
150	  role: "Training-free rank-aware方法——利用input channel sparsity和SVD"
151	  key_finding: "用SVD分解将input channel sparsity映射到output，无需预测active channels。50% model-level sparsity下43%端到端加速"
152	  relevance_to_us: "Training-free baseline。如果R-Sparse在SwiGLU模型上效果很好，我们需要证明trained KL predictor的额外训练成本是值得的"
153	
154	- title: "Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking"
155	  authors: [Marco Federici, Davide Belli, Mart van Baalen, Amir Jalalirad, Andrii Skliar, Bence Major, Markus Nagel, Paul Whatmough]
156	  venue: MLSys 2025
157	  year: 2024
158	  arxiv_id: "2412.01380"
159	  category: direct-competitor
160	  role: "Predictor-free dynamic pruning for SwiGLU——直接针对SwiGLU的magnitude pruning"
161	  key_finding: "Predictor-free方案动态剪枝SwiGLU MLP层，配合LoRA adapter恢复精度。Phi-3-Medium上46%内存减少+40%吞吐提升"
162	  relevance_to_us: "直接针对SwiGLU的competitor。DIP证明SwiGLU的sparsity pattern难以预测（所以放弃predictor），我们的KL-trained predictor需要证明能克服这个挑战"
163	
164	# =============================================================================
165	# 补充：Activation function替换和sparsity增强
166	# =============================================================================
167	
168	- title: "ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models"
169	  authors: [Iman Mirzadeh, Keivan Alizadeh, Sachin Mehta, Carlo C Del Mundo, Oncel Tuzel, Golnoosh Samei, Mohammad Rastegari, Mehrdad Farajtabar]
170	  venue: ICLR 2024
171	  year: 2024
172	  arxiv_id: "2310.04564"
173	  category: background
174	  role: "ReLU替换SiLU获得天然sparsity——替代路线"
175	  key_finding: "用ReLU替换SiLU/GELU后continual pretraining，获得天然高稀疏性（>90%），推理计算减少3x"
176	  relevance_to_us: "替代路线：修改activation function vs 训练predictor。我们的定位：不需要修改pretrained模型架构，作为plug-in predictor在现有SwiGLU模型上工作"
177	
178	- title: "Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters"
179	  authors: [Yixin Song, Haotong Xie, Zhengyan Zhang, Bo Wen, Li Ma, Zeyu Mi, Haibo Chen]
180	  venue: arXiv
181	  year: 2024
182	  arxiv_id: "2406.05955"
183	  category: background
184	  role: "dReLU获得90%+ sparsity——activation function工程的极致"
185	  key_finding: "提出dReLU使LLM达到近90% sparsity同时保持SOTA性能，2-5x decoding加速"
186	  relevance_to_us: "与ReLU Strikes Back同一思路但更极端。我们不改activation function，这是差异化定位"
187	
188	- title: "ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models"
189	  authors: [Chenyang Song, Xu Han, Zhengyan Zhang, Shengding Hu, Xiyu Shi, Kuai Li, Chen Chen, Zhiyuan Liu, Guangli Li, Tao Yang, Maosong Sun]
190	  venue: COLING 2025
191	  year: 2025
192	  arxiv_id: "2402.13516"
193	  category: background
194	  role: "Progressive sparsification——渐进式增加sparsity regularization"
195	  key_finding: "三步法：ReLU替换→progressive sparsity regularization（沿sine curve增强）→threshold shifting(FATReLU)。LLaMA2-7B达89.32% sparsity"
196	  relevance_to_us: "ProSparse的progressive training策略可参考：我们的KL predictor训练也可渐进式增加sparsity目标（已在Lagrangian约束中实现）"
197	
198	- title: "Sparsing Law: Towards Large Language Models with Greater Activation Sparsity"
199	  authors: [Yuqi Luo, Chenyang Song, Xu Han, Yingfa Chen, Chaojun Xiao, Xiaojun Meng, Liqun Deng, Jiansheng Wei, Zhiyuan Liu, Maosong Sun]
200	  venue: arXiv
201	  year: 2024
202	  arxiv_id: "2411.02335"
203	  category: background
204	  role: "Activation sparsity的scaling law——理论基础"
205	  key_finding: "SiLU/SwiGLU的activation ratio随训练递增（变密），ReLU递减（变稀）。Sparsity对parameter scale不敏感，与width-depth ratio线性相关"
206	  relevance_to_us: "理论支撑：SiLU/SwiGLU模型天然不够稀疏（随训练变密），因此需要外部predictor/pruning来获得稀疏性——这是我们工作的motivation之一"
207	
208	- title: "A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering"
209	  authors: [Nobel Dhar, Bobin Deng, Md Romyull Islam, Xinyue Zhang, Kazi Fahim Ahmad Nasif, Kun Suo]
210	  venue: Euro-Par 2025
211	  year: 2025
212	  arxiv_id: "2507.14179"
213	  category: background
214	  role: "Clustering-based sparsity prediction——用聚类简化prediction"
215	  key_finding: "将activation patterns聚类为representative clusters，预测cluster assignment而非individual neuron states，减少prediction开销。Mistral-7B上79.34%聚类精度"
216	  relevance_to_us: "降低predictor复杂度的思路。如果我们的per-neuron KL predictor开销太大，可考虑cluster-level prediction"
217	
218	# =============================================================================
219	# 竞争格局总结
220	# =============================================================================
221	#
222	# 我们的独特定位:
223	# 1. 唯一使用KL divergence训练activation sparsity predictor的工作
224	#    - DejaVu/ShadowLLM用BCE训练predictor
225	#    - SPON用KL但训练bias correction而非predictor
226	#    - TEAL/CATS/R-Sparse/SparseInfer/SVD-CSP是training-free
227	# 2. 专注SwiGLU模型的50% sparsity目标
228	#    - ReLU/dReLU方案需要替换activation function
229	#    - 很多training-free方案在SwiGLU上效果不佳(DIP论文证实)
230	# 3. 通过保留output distribution(而非逐neuron匹配)来指导sparsity
231	#    - Minitron/SPON已证明KL loss优于MSE/BCE做distribution matching
232	#    - 我们将此insight应用到predictor训练
233	#
234	# 主要related work定位:
235	# - vs TEAL: trained predictor(input-dependent) vs fixed magnitude threshold
236	# - vs DejaVu/ShadowLLM: KL loss vs BCE loss训练predictor
237	# - vs SPON: predictor vs learnable bias; 都用KL但目标不同
238	# - vs DIP: trained predictor vs predictor-free pruning
239	# - vs ReLU/TurboSparse/ProSparse: 不改activation function
240	# - vs Fast Forward: KL loss vs BCE+error compensation
241	# - vs CATS: input-dependent predictor vs fixed percentile threshold
242	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "b9f6b671-293f-4b6a-9fc7-97042419fd80",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml",
      "content": "# Literature Map: KL Distillation for Sparse SwiGLU Activation Prediction\n# Last updated: 2026-05-15\n# Survey scope: 2023-2026, 4 directions\n\n# =============================================================================\n# Direction 1: KL distillation for structured/activation sparsity\n# Finding: NO prior work uses KL to train an activation sparsity PREDICTOR.\n# Existing predictors use BCE (DejaVu, ShadowLLM). SPON uses KL but for\n# learnable bias correction, not predictor training. This is our novelty.\n# =============================================================================\n\n- title: \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\"\n  authors: [Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, Tengfei Ma]\n  venue: ICML 2026\n  year: 2026\n  arxiv_id: \"2512.12744\"\n  category: direct-competitor\n  role: \"最接近的KL蒸馏用于稀疏性的工作——但SPON训练的是可学习bias项而非predictor\"\n  key_finding: \"SPON注入input-independent learnable activation vectors作为sparse computation的anchor，用KL散度(dense vs sparse logits)做distribution matching训练，训练后吸收进bias项，零推理开销\"\n  relevance_to_us: \"SPON证明KL divergence比BCE/MSE更适合sparsity场景的distribution matching。但SPON是全局bias correction而非per-token predictor——我们的predictor方案能实现input-dependent的sparsity pattern，比SPON更灵活。SPON在50-60% sparsity下测试，与我们目标一致\"\n\n- title: \"Compact Language Models via Pruning and Knowledge Distillation\"\n  authors: [Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz, Pavlo Molchanov]\n  venue: NeurIPS 2024\n  year: 2024\n  arxiv_id: \"2407.14679\"\n  category: method-component\n  role: \"KL蒸馏用于结构化剪枝后恢复——验证logit-only KL优于intermediate matching\"\n  key_finding: \"Minitron用logit-only forward KL divergence做structured pruning后的distillation recovery，发现仅用KL loss（不用CE或intermediate matching）效果最好，学生模型继承了teacher的inter-token关系和confidence calibration\"\n  relevance_to_us: \"支持我们的核心假设：KL divergence保留output distribution比逐元素BCE更优。Minitron的发现（logit-only KL最优）为我们predictor的KL训练目标提供了理论支撑\"\n\n- title: \"Instruction-Following Pruning for Large Language Models\"\n  authors: [Bairu Hou, Qibin Chen, Jianyu Wang, Guoli Yin, Chong Wang, Nan Du, Ruoming Pang, Shiyu Chang, Tao Lei]\n  venue: ICML 2025\n  year: 2025\n  arxiv_id: \"2501.02086\"\n  category: method-component\n  role: \"训练sparse mask predictor的范式——input-dependent mask selection\"\n  key_finding: \"训练一个sparse mask predictor以instruction为输入动态选择最相关参数子集，联合优化mask predictor和LLM\"\n  relevance_to_us: \"架构上与我们类似（训练predictor生成mask），但目标是instruction-aware weight pruning而非activation sparsity。可参考其predictor-LLM联合优化策略\"\n\n# =============================================================================\n# Direction 2: Output distribution preservation in pruning/sparsity\n# =============================================================================\n\n- title: \"Distilling to Hybrid Attention Models via KL-Guided Layer Selection\"\n  authors: []\n  venue: arXiv\n  year: 2025\n  arxiv_id: \"2512.20569\"\n  category: method-component\n  role: \"KL散度引导layer selection——用distribution差异决定哪些层需要保留\"\n  key_finding: \"用KL divergence作为指标选择哪些attention层替换为hybrid attention，通过最小化output distribution变化来指导架构决策\"\n  relevance_to_us: \"方法论启示：KL divergence不仅可作为训练loss，还可作为layer-wise重要性指标。我们可用per-layer KL分析哪些层的sparsity对output distribution影响最大\"\n\n# =============================================================================\n# Direction 3: SPON和类似的learnable bias correction for sparsity\n# =============================================================================\n\n- title: \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\"\n  authors: [Aayush Gautam, Mukul Gagrani, Junyoung Park, Mingu Lee, Chiris Lott, Narasimha Reddy]\n  venue: arXiv\n  year: 2026\n  arxiv_id: \"2602.00397\"\n  category: direct-competitor\n  role: \"Predictor + error compensation双组件架构——与SPON的bias correction思路互补\"\n  key_finding: \"组合三个组件：(1) lightweight expert predictor选择high-importance neurons，(2) error compensation network修正sparsity误差，(3) layer-wise sparsity scheduler分配计算。50% FFN sparsity下达到1.45x prefill加速\"\n  relevance_to_us: \"与我们的方案最可比：都用predictor做activation sparsity。我们的差异在于用KL loss训练predictor而非BCE，且不需要额外的error compensation网络（KL loss本身应该能减少distribution shift）\"\n\n- title: \"Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models\"\n  authors: [Tai An, Ruwu Cai, Yanzhe Zhang, Yang Liu, Hao Chen, Pengcheng Xie, Sheng Chang, Yiwu Yao, Gongyi Wang]\n  venue: arXiv\n  year: 2025\n  arxiv_id: \"2508.02128\"\n  category: background\n  role: \"N:M structured activation sparsity——hardware-friendly的sparsity pattern\"\n  key_finding: \"Training-free的top-k策略在linear projection层内确定N:M activation masks，在2:4/4:8/8:16多种ratio下有效，可与W8A8量化组合\"\n  relevance_to_us: \"如果我们的predictor输出改为N:M structured pattern而非unstructured binary mask，可获得更好的hardware加速。值得作为future work\"\n\n# =============================================================================\n# Direction 4: Predictor-based activation sparsity (TEAL, DejaVu, PowerInfer等)\n# =============================================================================\n\n- title: \"Training-Free Activation Sparsity in Large Language Models\"\n  authors: [James Liu, Pragaash Ponnusamy, Tianle Cai, Han Guo, Yoon Kim, Ben Athiwaratkun]\n  venue: ICLR 2025 (Spotlight)\n  year: 2025\n  arxiv_id: \"2408.14690\"\n  category: direct-competitor\n  role: \"TEAL——我们的主要baseline，training-free magnitude pruning\"\n  key_finding: \"对所有hidden states施加magnitude-based sparsity（不需训练），在40-50% sparsity下性能降低很小，Llama-2/3和Mistral 7B-70B上验证。50% sparsity下1.8x decoding加速\"\n  relevance_to_us: \"TEAL用BCE度量sparsity mask质量（二元对错），我们的核心论点是：BCE只看neuron是否激活的对错，忽略了错误预测对output distribution的差异化影响。KL loss应该能让predictor学到'哪些neuron的错误预测对output影响更大'\"\n\n- title: \"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\"\n  authors: [Zichang Liu, Jue Wang, Tri Dao, Tianyi Zhou, Binhang Yuan, Zhao Song, Anshumali Shrivastava, Ce Zhang, Yuandong Tian, Christopher Re, Beidi Chen]\n  venue: ICML 2023\n  year: 2023\n  arxiv_id: \"2310.17157\"\n  category: direct-competitor\n  role: \"Predictor-based contextual sparsity的开创性工作——我们的直接对比对象\"\n  key_finding: \"用两层MLP predictor预测每层的contextual sparsity pattern（哪些attention heads和MLP neurons可跳过），在OPT-175B上实现2x加速。Predictor用BCE训练\"\n  relevance_to_us: \"DejaVu是predictor-based sparsity的baseline。其predictor用BCE训练——我们改用KL loss训练类似的predictor。关键差异：DejaVu在per-neuron level用BCE，我们在output distribution level用KL\"\n\n- title: \"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\"\n  authors: [Yash Akhauri, Ahmed F AbouElhamayed, Jordan Dotzel, Zhiru Zhang, Alexander M Rush, Safeen Huda, Mohamed S Abdelfattah]\n  venue: EMNLP 2024\n  year: 2024\n  arxiv_id: \"2406.16635\"\n  category: direct-competitor\n  role: \"DejaVu的改进——更好的predictor架构和sparsity pattern enforcement\"\n  key_finding: \"Shadow predictor超越magnitude-based pruning，context-dependent评估attention head和neuron重要性。比DejaVu端到端精度提升15%，速度提升20%\"\n  relevance_to_us: \"ShadowLLM改进了predictor架构但仍用BCE-style loss。我们的改进方向正交：不改predictor架构，改训练loss（BCE→KL）。两种改进可能互补\"\n\n- title: \"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference\"\n  authors: [Jiho Shin, Hoeseok Yang, Youngmin Yi]\n  venue: DATE 2025\n  year: 2025\n  arxiv_id: \"2411.12692\"\n  category: background\n  role: \"Training-free sign-bit predictor——极低开销的sparsity预测\"\n  key_finding: \"仅比较input和weight的sign bits预测activation sparsity，无需训练。仅适用于ReLU-based LLMs，不适用SwiGLU\"\n  relevance_to_us: \"不适用于SwiGLU模型（我们的目标），但其sign-bit方法的简洁性值得参考。SwiGLU缺乏天然sparsity证明trained predictor的必要性\"\n\n- title: \"SVD Contextual Sparsity Predictors for Fast LLM Inference\"\n  authors: [Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, C.C. Korikov]\n  venue: arXiv\n  year: 2026\n  arxiv_id: \"2603.14110\"\n  category: direct-competitor\n  role: \"Training-free SVD-based sparsity predictor——用gate projection矩阵的SVD做预测\"\n  key_finding: \"对ReGLU FFN的gate projection矩阵做truncation-aware SVD构建sparse pattern predictor，90% FFN sparsity下1.8x decoding加速，benchmark降低<1%\"\n  relevance_to_us: \"虽然是training-free competitor，但focus在ReGLU（不是SwiGLU）且需要90%天然稀疏性。我们的方法在SwiGLU的50%目标sparsity下工作，使用场景不同\"\n\n- title: \"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\"\n  authors: [Donghyun Lee, Je-Yong Lee, Genghan Zhang, Mo Tiwari, Azalia Mirhoseini]\n  venue: arXiv\n  year: 2024\n  arxiv_id: \"2404.08763\"\n  category: direct-competitor\n  role: \"Contextual thresholding——不训练predictor，用统计threshold做sparsity\"\n  key_finding: \"为每个MLP层计算SiLU(x)激活的percentile threshold做sparsification，50% sparsity下性能降低1-2%，无需fine-tuning。Mistral-7B和Llama2-7B上验证\"\n  relevance_to_us: \"CATS直接在SwiGLU/SiLU模型上工作，是我们的直接competitor。但CATS是固定threshold不考虑input context，我们的trained predictor是input-dependent的，理论上更优\"\n\n- title: \"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\"\n  authors: [Zhenyu Zhang, Zechun Liu, Yuandong Tian, Harshit Khaitan, Zhangyang Wang, Steven Li]\n  venue: ICLR 2025\n  year: 2025\n  arxiv_id: \"2504.19449\"\n  category: background\n  role: \"Training-free rank-aware方法——利用input channel sparsity和SVD\"\n  key_finding: \"用SVD分解将input channel sparsity映射到output，无需预测active channels。50% model-level sparsity下43%端到端加速\"\n  relevance_to_us: \"Training-free baseline。如果R-Sparse在SwiGLU模型上效果很好，我们需要证明trained KL predictor的额外训练成本是值得的\"\n\n- title: \"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\"\n  authors: [Marco Federici, Davide Belli, Mart van Baalen, Amir Jalalirad, Andrii Skliar, Bence Major, Markus Nagel, Paul Whatmough]\n  venue: MLSys 2025\n  year: 2024\n  arxiv_id: \"2412.01380\"\n  category: direct-competitor\n  role: \"Predictor-free dynamic pruning for SwiGLU——直接针对SwiGLU的magnitude pruning\"\n  key_finding: \"Predictor-free方案动态剪枝SwiGLU MLP层，配合LoRA adapter恢复精度。Phi-3-Medium上46%内存减少+40%吞吐提升\"\n  relevance_to_us: \"直接针对SwiGLU的competitor。DIP证明SwiGLU的sparsity pattern难以预测（所以放弃predictor），我们的KL-trained predictor需要证明能克服这个挑战\"\n\n# =============================================================================\n# 补充：Activation function替换和sparsity增强\n# =============================================================================\n\n- title: \"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\"\n  authors: [Iman Mirzadeh, Keivan Alizadeh, Sachin Mehta, Carlo C Del Mundo, Oncel Tuzel, Golnoosh Samei, Mohammad Rastegari, Mehrdad Farajtabar]\n  venue: ICLR 2024\n  year: 2024\n  arxiv_id: \"2310.04564\"\n  category: background\n  role: \"ReLU替换SiLU获得天然sparsity——替代路线\"\n  key_finding: \"用ReLU替换SiLU/GELU后continual pretraining，获得天然高稀疏性（>90%），推理计算减少3x\"\n  relevance_to_us: \"替代路线：修改activation function vs 训练predictor。我们的定位：不需要修改pretrained模型架构，作为plug-in predictor在现有SwiGLU模型上工作\"\n\n- title: \"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\"\n  authors: [Yixin Song, Haotong Xie, Zhengyan Zhang, Bo Wen, Li Ma, Zeyu Mi, Haibo Chen]\n  venue: arXiv\n  year: 2024\n  arxiv_id: \"2406.05955\"\n  category: background\n  role: \"dReLU获得90%+ sparsity——activation function工程的极致\"\n  key_finding: \"提出dReLU使LLM达到近90% sparsity同时保持SOTA性能，2-5x decoding加速\"\n  relevance_to_us: \"与ReLU Strikes Back同一思路但更极端。我们不改activation function，这是差异化定位\"\n\n- title: \"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\"\n  authors: [Chenyang Song, Xu Han, Zhengyan Zhang, Shengding Hu, Xiyu Shi, Kuai Li, Chen Chen, Zhiyuan Liu, Guangli Li, Tao Yang, Maosong Sun]\n  venue: COLING 2025\n  year: 2025\n  arxiv_id: \"2402.13516\"\n  category: background\n  role: \"Progressive sparsification——渐进式增加sparsity regularization\"\n  key_finding: \"三步法：ReLU替换→progressive sparsity regularization（沿sine curve增强）→threshold shifting(FATReLU)。LLaMA2-7B达89.32% sparsity\"\n  relevance_to_us: \"ProSparse的progressive training策略可参考：我们的KL predictor训练也可渐进式增加sparsity目标（已在Lagrangian约束中实现）\"\n\n- title: \"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\"\n  authors: [Yuqi Luo, Chenyang Song, Xu Han, Yingfa Chen, Chaojun Xiao, Xiaojun Meng, Liqun Deng, Jiansheng Wei, Zhiyuan Liu, Maosong Sun]\n  venue: arXiv\n  year: 2024\n  arxiv_id: \"2411.02335\"\n  category: background\n  role: \"Activation sparsity的scaling law——理论基础\"\n  key_finding: \"SiLU/SwiGLU的activation ratio随训练递增（变密），ReLU递减（变稀）。Sparsity对parameter scale不敏感，与width-depth ratio线性相关\"\n  relevance_to_us: \"理论支撑：SiLU/SwiGLU模型天然不够稀疏（随训练变密），因此需要外部predictor/pruning来获得稀疏性——这是我们工作的motivation之一\"\n\n- title: \"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering\"\n  authors: [Nobel Dhar, Bobin Deng, Md Romyull Islam, Xinyue Zhang, Kazi Fahim Ahmad Nasif, Kun Suo]\n  venue: Euro-Par 2025\n  year: 2025\n  arxiv_id: \"2507.14179\"\n  category: background\n  role: \"Clustering-based sparsity prediction——用聚类简化prediction\"\n  key_finding: \"将activation patterns聚类为representative clusters，预测cluster assignment而非individual neuron states，减少prediction开销。Mistral-7B上79.34%聚类精度\"\n  relevance_to_us: \"降低predictor复杂度的思路。如果我们的per-neuron KL predictor开销太大，可考虑cluster-level prediction\"\n\n# =============================================================================\n# 竞争格局总结\n# =============================================================================\n#\n# 我们的独特定位:\n# 1. 唯一使用KL divergence训练activation sparsity predictor的工作\n#    - DejaVu/ShadowLLM用BCE训练predictor\n#    - SPON用KL但训练bias correction而非predictor\n#    - TEAL/CATS/R-Sparse/SparseInfer/SVD-CSP是training-free\n# 2. 专注SwiGLU模型的50% sparsity目标\n#    - ReLU/dReLU方案需要替换activation function\n#    - 很多training-free方案在SwiGLU上效果不佳(DIP论文证实)\n# 3. 通过保留output distribution(而非逐neuron匹配)来指导sparsity\n#    - Minitron/SPON已证明KL loss优于MSE/BCE做distribution matching\n#    - 我们将此insight应用到predictor训练\n#\n# 主要related work定位:\n# - vs TEAL: trained predictor(input-dependent) vs fixed magnitude threshold\n# - vs DejaVu/ShadowLLM: KL loss vs BCE loss训练predictor\n# - vs SPON: predictor vs learnable bias; 都用KL但目标不同\n# - vs DIP: trained predictor vs predictor-free pruning\n# - vs ReLU/TurboSparse/ProSparse: 不改activation function\n# - vs Fast Forward: KL loss vs BCE+error compensation\n# - vs CATS: input-dependent predictor vs fixed percentile threshold\n",
      "numLines": 242,
      "startLine": 1,
      "totalLines": 242
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JzuVakz7L13zneEavbbbyF`</summary>

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
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "087e5d56-0247-4af9-85da-9f13d11cece2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXcHYa1E6zE4KfNJ51LHNi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11937,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11937
      },
      "output_tokens": 37,
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

_source line 9 · 2026-05-16T08:38:14.007Z_

<details><summary>↩ Tool result · `toolu_01JzuVakz7L13zneEavbbbyF`</summary>

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
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "663ef1b5-da3c-4dc7-b250-6713a550be0d",
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
Good, I have the current literature_map.yaml and the WebSearch tool. Now let me search for the papers. I'll run three searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "7de3cca5-9838-4774-9016-758f90d22033",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WR9KRF2BwBYu2eE3sf4HXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7125,
      "cache_read_input_tokens": 23778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7125
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

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XMnUPe1aMurJ97Tn7Pvc5N`</summary>

```json
{
  "query": "PowerInfer activation sparsity GPU-CPU hybrid inference LLM arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "c7913cb4-44b6-44c0-9b2e-901a303e9e2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WR9KRF2BwBYu2eE3sf4HXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7125,
      "cache_read_input_tokens": 23778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7125
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N4uGTrcfChM32AyBMdJWjj`</summary>

```json
{
  "query": "contextual sparsity prediction LLM 2025 2026 arxiv learned predictor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "47f0a2b3-0a22-46af-a19b-bd7cf9c6394a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WR9KRF2BwBYu2eE3sf4HXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7125,
      "cache_read_input_tokens": 23778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7125
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EUVXATv93AVteoLsFyTb6C`</summary>

```json
{
  "query": "learned activation sparsity predictor neural network 2025 2026 efficient inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "8cf48687-7329-4060-9db9-93dd28a8a968",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WR9KRF2BwBYu2eE3sf4HXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7125,
      "cache_read_input_tokens": 23778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7125
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

_source line 14 · 2026-05-16T08:38:25.293Z_

<details><summary>↩ Tool result · `toolu_01XMnUPe1aMurJ97Tn7Pvc5N`</summary>

```text
Web search results for query: "PowerInfer activation sparsity GPU-CPU hybrid inference LLM arxiv"

Links: [{"title":"[2312.12456] PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://arxiv.org/abs/2312.12456"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://arxiv.org/html/2312.12456v2"},{"title":"[2312.12456] PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://ar5iv.labs.arxiv.org/html/2312.12456"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU | Proceedings of the ACM SIGOPS 30th Symposium on Operating Systems Principles","url":"https://dl.acm.org/doi/10.1145/3694715.3695964"},{"title":"PowerInfer: Fast LLM Inference on Consumer GPUs","url":"https://www.emergentmind.com/papers/2312.12456"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://gonzoml.substack.com/p/powerinfer-fast-large-language-model"},{"title":"Paper page - PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://huggingface.co/papers/2312.12456"},{"title":"Efficient LLM Inference with Activation Checkpointing and Hybrid Caching","url":"https://arxiv.org/html/2501.01792v1"},{"title":"HGCA: Hybrid GPU-CPU Attention for Long Context LLM Inference","url":"https://arxiv.org/html/2507.03153v1"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231212456S/abstract"}]

I found comprehensive information about PowerInfer on arXiv. Here are the key findings:

## PowerInfer Overview

PowerInfer is a high-speed Large Language Model (LLM) inference engine on a personal computer (PC) equipped with a single consumer-grade GPU.

## Core Design Principle

The design exploits the high locality inherent in LLM inference, characterized by a power-law distribution in neuron activation, where a small subset of neurons (hot neurons) are consistently activated across inputs, while the majority (cold neurons) vary based on specific inputs.

## GPU-CPU Hybrid Architecture

PowerInfer designs a GPU-CPU hybrid inference engine where hot-activated neurons are preloaded onto the GPU for fast access, while cold-activated neurons are computed on the CPU, thus significantly reducing GPU memory demands and CPU-GPU data transfers.

## Key Optimizations

PowerInfer integrates adaptive predictors and neuron-aware sparse operators, optimizing the efficiency of neuron activation and computational sparsity. It introduces an adaptive method for constructing smaller predictors for layers with higher activation sparsity and skewness, which reduces predictor size while maintaining accuracy and frees up GPU memory for LLM inferences.

## Performance Results

PowerInfer significantly outperforms llama.cpp by up to 11.69x while retaining model accuracy across various LLMs on a single NVIDIA RTX 4090 GPU.

**arXiv paper:** https://arxiv.org/abs/2312.12456


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "eaee1308-c08b-4094-a64d-6497eacb9b93",
  "tool_use_result": {
    "query": "PowerInfer activation sparsity GPU-CPU hybrid inference LLM arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H4oF6iBg5eamnQGeTUXsHH",
        "content": [
          {
            "title": "[2312.12456] PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU",
            "url": "https://arxiv.org/abs/2312.12456"
          },
          {
            "title": "PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU",
            "url": "https://arxiv.org/html/2312.12456v2"
          },
          {
            "title": "[2312.12456] PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU",
            "url": "https://ar5iv.labs.arxiv.org/html/2312.12456"
          },
          {
            "title": "PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU | Proceedings of the ACM SIGOPS 30th Symposium on Operating Systems Principles",
            "url": "https://dl.acm.org/doi/10.1145/3694715.3695964"
          },
          {
            "title": "PowerInfer: Fast LLM Inference on Consumer GPUs",
            "url": "https://www.emergentmind.com/papers/2312.12456"
          },
          {
            "title": "PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU",
            "url": "https://gonzoml.substack.com/p/powerinfer-fast-large-language-model"
          },
          {
            "title": "Paper page - PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU",
            "url": "https://huggingface.co/papers/2312.12456"
          },
          {
            "title": "Efficient LLM Inference with Activation Checkpointing and Hybrid Caching",
            "url": "https://arxiv.org/html/2501.01792v1"
          },
          {
            "title": "HGCA: Hybrid GPU-CPU Attention for Long Context LLM Inference",
            "url": "https://arxiv.org/html/2507.03153v1"
          },
          {
            "title": "PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2023arXiv231212456S/abstract"
          }
        ]
      },
      "I found comprehensive information about PowerInfer on arXiv. Here are the key findings:\n\n## PowerInfer Overview\n\nPowerInfer is a high-speed Large Language Model (LLM) inference engine on a personal computer (PC) equipped with a single consumer-grade GPU.\n\n## Core Design Principle\n\nThe design exploits the high locality inherent in LLM inference, characterized by a power-law distribution in neuron activation, where a small subset of neurons (hot neurons) are consistently activated across inputs, while the majority (cold neurons) vary based on specific inputs.\n\n## GPU-CPU Hybrid Architecture\n\nPowerInfer designs a GPU-CPU hybrid inference engine where hot-activated neurons are preloaded onto the GPU for fast access, while cold-activated neurons are computed on the CPU, thus significantly reducing GPU memory demands and CPU-GPU data transfers.\n\n## Key Optimizations\n\nPowerInfer integrates adaptive predictors and neuron-aware sparse operators, optimizing the efficiency of neuron activation and computational sparsity. It introduces an adaptive method for constructing smaller predictors for layers with higher activation sparsity and skewness, which reduces predictor size while maintaining accuracy and frees up GPU memory for LLM inferences.\n\n## Performance Results\n\nPowerInfer significantly outperforms llama.cpp by up to 11.69x while retaining model accuracy across various LLMs on a single NVIDIA RTX 4090 GPU.\n\n**arXiv paper:** https://arxiv.org/abs/2312.12456"
    ],
    "durationSeconds": 6.119862428
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T08:38:28.237Z_

<details><summary>↩ Tool result · `toolu_01N4uGTrcfChM32AyBMdJWjj`</summary>

```text
Web search results for query: "contextual sparsity prediction LLM 2025 2026 arxiv learned predictor"

Links: [{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/html/2603.14110"},{"title":"[2406.16635] ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/abs/2406.16635"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/shadowllm-predictor-based-contextual-sparsity-large-language"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/html/2406.16635v2"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/pdf/2310.17157"},{"title":"[2310.17157] Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://ar5iv.labs.arxiv.org/html/2310.17157"},{"title":"SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://arxiv.org/html/2506.16500v1"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models | Space Frontiers","url":"https://spacefrontiers.org/r/10.48550/arxiv.2406.16635"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering","url":"https://arxiv.org/html/2507.14179v1"},{"title":"TokenButler: Token Importance is Predictable","url":"https://arxiv.org/html/2503.07518v1"}]

Based on the search results, here are the key findings about contextual sparsity prediction in LLMs from recent 2025-2026 arxiv papers:

## Recent Research on Contextual Sparsity Predictors for LLMs

**SVD Contextual Sparsity Predictors (March 2026)**

A recent framework presents a fast, training-free method for building sparse pattern predictors using truncation-aware singular value decomposition (SVD) of the gate projection matrix, along with a threshold calibration algorithm, and inference executors supporting conditional computation on CUDA and CANN devices. This approach demonstrates up to a 1.8x reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores on tasks involving complex math and code generation.

Key advantages of this SVD-based approach include: SVD predictors directly leverage the LLM's internal weight structure, while trained predictors may suffer from out-of-distribution sensitivity due to their data-dependent nature.

**Learned Sparsity Predictors**

A prevalent approach for leveraging contextual sparsity involves employing lightweight, learnable sparsity predictors that generate input-specific sparse activation patterns prior to FFN forward passes. Some approaches employ learned low-rank predictors, though this raises concerns about generalization across different datasets and tasks.

**Token Importance Prediction (March 2025)**

TokenButler is a high-granularity, query-aware predictor that learns to identify critical tokens by training a light-weight predictor with less than 1.2% parameter overhead.

**Activation Pattern Clustering (July 2025)**

A clustering-based activation pattern compression framework enables efficient prediction and utilization of activation sparsity.

These recent approaches represent significant advances in making contextual sparsity prediction more efficient and practical for LLM inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "50d8bc4c-a875-467b-b35f-66fc0b80380d",
  "tool_use_result": {
    "query": "contextual sparsity prediction LLM 2025 2026 arxiv learned predictor",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WG8xrWvirCDSPtk82TSHZq",
        "content": [
          {
            "title": "SVD Contextual Sparsity Predictors for Fast LLM Inference",
            "url": "https://arxiv.org/html/2603.14110"
          },
          {
            "title": "[2406.16635] ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models",
            "url": "https://arxiv.org/abs/2406.16635"
          },
          {
            "title": "ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/shadowllm-predictor-based-contextual-sparsity-large-language"
          },
          {
            "title": "ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models",
            "url": "https://arxiv.org/html/2406.16635v2"
          },
          {
            "title": "Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time",
            "url": "https://arxiv.org/pdf/2310.17157"
          },
          {
            "title": "[2310.17157] Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time",
            "url": "https://ar5iv.labs.arxiv.org/html/2310.17157"
          },
          {
            "title": "SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity",
            "url": "https://arxiv.org/html/2506.16500v1"
          },
          {
            "title": "ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models | Space Frontiers",
            "url": "https://spacefrontiers.org/r/10.48550/arxiv.2406.16635"
          },
          {
            "title": "A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering",
            "url": "https://arxiv.org/html/2507.14179v1"
          },
          {
            "title": "TokenButler: Token Importance is Predictable",
            "url": "https://arxiv.org/html/2503.07518v1"
          }
        ]
      },
      "Based on the search results, here are the key findings about contextual sparsity prediction in LLMs from recent 2025-2026 arxiv papers:\n\n## Recent Research on Contextual Sparsity Predictors for LLMs\n\n**SVD Contextual Sparsity Predictors (March 2026)**\n\nA recent framework presents a fast, training-free method for building sparse pattern predictors using truncation-aware singular value decomposition (SVD) of the gate projection matrix, along with a threshold calibration algorithm, and inference executors supporting conditional computation on CUDA and CANN devices. This approach demonstrates up to a 1.8x reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores on tasks involving complex math and code generation.\n\nKey advantages of this SVD-based approach include: SVD predictors directly leverage the LLM's internal weight structure, while trained predictors may suffer from out-of-distribution sensitivity due to their data-dependent nature.\n\n**Learned Sparsity Predictors**\n\nA prevalent approach for leveraging contextual sparsity involves employing lightweight, learnable sparsity predictors that generate input-specific sparse activation patterns prior to FFN forward passes. Some approaches employ learned low-rank predictors, though this raises concerns about generalization across different datasets and tasks.\n\n**Token Importance Prediction (March 2025)**\n\nTokenButler is a high-granularity, query-aware predictor that learns to identify critical tokens by training a light-weight predictor with less than 1.2% parameter overhead.\n\n**Activation Pattern Clustering (July 2025)**\n\nA clustering-based activation pattern compression framework enables efficient prediction and utilization of activation sparsity.\n\nThese recent approaches represent significant advances in making contextual sparsity prediction more efficient and practical for LLM inference."
    ],
    "durationSeconds": 8.328603124
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T08:38:30.311Z_

<details><summary>↩ Tool result · `toolu_01EUVXATv93AVteoLsFyTb6C`</summary>

```text
Web search results for query: "learned activation sparsity predictor neural network 2025 2026 efficient inference"

Links: [{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering","url":"https://arxiv.org/html/2507.14179v1"},{"title":"Inducing and exploiting activation sparsity for fast neural network inference | Proceedings of the 37th International Conference on Machine Learning","url":"https://dl.acm.org/doi/abs/10.5555/3524938.3525451"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://arxiv.org/html/2411.12692v2"},{"title":"Accelerating LLM Inference Using Sparsity Kira Selby, Varun Khare NimbleEdge","url":"https://www.nimbleedge.com/sparsity-white-paper.pdf"},{"title":"TensorDash: Exploiting Sparsity to Accelerate Deep Neural Network Training","url":"https://www.cs.toronto.edu/ecosystem/papers/MICRO_21/TensorDash.pdf"},{"title":"Inducing and Exploiting Activation Sparsity for Fast Neural Network Inference","url":"http://proceedings.mlr.press/v119/kurtz20a/kurtz20a.pdf"},{"title":"Inducing and Exploiting Activation Sparsity for Fast Inference on Deep Neural Networks","url":"https://proceedings.mlr.press/v119/kurtz20a.html"},{"title":"Activation Sparsity","url":"https://www.aussieai.com/research/activation-sparsity"},{"title":"Exploring the benefit of activation sparsity in pre-training | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3694553"},{"title":"Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models","url":"https://arxiv.org/html/2508.02128v1"}]

I found several recent and relevant papers on activation sparsity prediction for neural networks. Here are the key findings:

## Recent Developments in Activation Sparsity Prediction (2025-2026)

### Clustering-Based Approach
To enable efficient prediction and utilization of activation sparsity, researchers propose a clustering-based activation pattern compression framework. Instead of treating each neuron independently, similar activation patterns are grouped into a small set of representative clusters. This method achieves up to 79.34% clustering precision while maintaining minimal degradation in perplexity (PPL) scores.

### Training-Free Prediction Method
A recent approach predicts sparsity dynamically and approximately without the need for training, and the proposed predictor not only eliminates the need for additional training but also reduces memory and computational overhead. This contrasts with earlier methods that required training separate neural networks.

### N:M Sparsity for LLM Prefill
Amber Pruner is a training-free N:M activation sparsity method designed specifically for the prefill stage, targeting the acceleration of linear projection layers in LLMs, and demonstrates that it can effectively sparsify and accelerate more than 55% of linear computations without requiring model retraining.

### Advanced Training Approaches
Recent work observed that 60% sparsity was still far below the >95% sparsity demonstrated in OPT, and proposed a multi-phase training programme incorporating auxiliary losses that help promote sparse activations, with results on Llama2 showing sparsities of almost 90%, with no appreciable drop in accuracy.

These approaches represent significant progress in making efficient inference with activation sparsity more practical and scalable for large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "e2b38e4c-ed15-4570-b109-5d1be84b4551",
  "tool_use_result": {
    "query": "learned activation sparsity predictor neural network 2025 2026 efficient inference",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H9MSUMrvpFiBgPRm2MkzbB",
        "content": [
          {
            "title": "A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering",
            "url": "https://arxiv.org/html/2507.14179v1"
          },
          {
            "title": "Inducing and exploiting activation sparsity for fast neural network inference | Proceedings of the 37th International Conference on Machine Learning",
            "url": "https://dl.acm.org/doi/abs/10.5555/3524938.3525451"
          },
          {
            "title": "SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference",
            "url": "https://arxiv.org/html/2411.12692v2"
          },
          {
            "title": "Accelerating LLM Inference Using Sparsity Kira Selby, Varun Khare NimbleEdge",
            "url": "https://www.nimbleedge.com/sparsity-white-paper.pdf"
          },
          {
            "title": "TensorDash: Exploiting Sparsity to Accelerate Deep Neural Network Training",
            "url": "https://www.cs.toronto.edu/ecosystem/papers/MICRO_21/TensorDash.pdf"
          },
          {
            "title": "Inducing and Exploiting Activation Sparsity for Fast Neural Network Inference",
            "url": "http://proceedings.mlr.press/v119/kurtz20a/kurtz20a.pdf"
          },
          {
            "title": "Inducing and Exploiting Activation Sparsity for Fast Inference on Deep Neural Networks",
            "url": "https://proceedings.mlr.press/v119/kurtz20a.html"
          },
          {
            "title": "Activation Sparsity",
            "url": "https://www.aussieai.com/research/activation-sparsity"
          },
          {
            "title": "Exploring the benefit of activation sparsity in pre-training | Proceedings of the 41st International Conference on Machine Learning",
            "url": "https://dl.acm.org/doi/10.5555/3692070.3694553"
          },
          {
            "title": "Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models",
            "url": "https://arxiv.org/html/2508.02128v1"
          }
        ]
      },
      "I found several recent and relevant papers on activation sparsity prediction for neural networks. Here are the key findings:\n\n## Recent Developments in Activation Sparsity Prediction (2025-2026)\n\n### Clustering-Based Approach\nTo enable efficient prediction and utilization of activation sparsity, researchers propose a clustering-based activation pattern compression framework. Instead of treating each neuron independently, similar activation patterns are grouped into a small set of representative clusters. This method achieves up to 79.34% clustering precision while maintaining minimal degradation in perplexity (PPL) scores.\n\n### Training-Free Prediction Method\nA recent approach predicts sparsity dynamically and approximately without the need for training, and the proposed predictor not only eliminates the need for additional training but also reduces memory and computational overhead. This contrasts with earlier methods that required training separate neural networks.\n\n### N:M Sparsity for LLM Prefill\nAmber Pruner is a training-free N:M activation sparsity method designed specifically for the prefill stage, targeting the acceleration of linear projection layers in LLMs, and demonstrates that it can effectively sparsify and accelerate more than 55% of linear computations without requiring model retraining.\n\n### Advanced Training Approaches\nRecent work observed that 60% sparsity was still far below the >95% sparsity demonstrated in OPT, and proposed a multi-phase training programme incorporating auxiliary losses that help promote sparse activations, with results on Llama2 showing sparsities of almost 90%, with no appreciable drop in accuracy.\n\nThese approaches represent significant progress in making efficient inference with activation sparsity more practical and scalable for large language models."
    ],
    "durationSeconds": 10.332939929
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Good, I found PowerInfer (2312.12456). Now let me search for more details about TokenButler and any other recent 2025-2026 works that might be relevant. Let me also look for PowerInfer-2 or newer variants.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "8b490e75-d354-493c-9c5a-0aae4c1d8051",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012sc2YUG2ooB1wQEm1B2nfD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3043,
      "cache_read_input_tokens": 30903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3043
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

Found PowerInfer. Let me get more details on TokenButler and search for any other recent contextual sparsity works we might have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "b15e2548-f9e4-47f5-b2b0-8ae49dac2ea2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012sc2YUG2ooB1wQEm1B2nfD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3043,
      "cache_read_input_tokens": 30903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3043
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S2zHZcFfLJTvT7vg3zy7A3`</summary>

```json
{
  "query": "TokenButler token importance predictor LLM arxiv 2025 query-aware sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "cb4502ff-5305-4c92-a359-51a38d9c0c34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012sc2YUG2ooB1wQEm1B2nfD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3043,
      "cache_read_input_tokens": 30903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3043
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_011puc5HCs9pjd1oV517M4yp`</summary>

```json
{
  "query": "PowerInfer-2 arxiv 2024 2025 smartphone inference sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "5b17235e-5695-4ccf-bebd-ad67f267ee5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012sc2YUG2ooB1wQEm1B2nfD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3043,
      "cache_read_input_tokens": 30903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3043
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

_source line 21 · 2026-05-16T08:38:43.089Z_

<details><summary>↩ Tool result · `toolu_01S2zHZcFfLJTvT7vg3zy7A3`</summary>

```text
Web search results for query: "TokenButler token importance predictor LLM arxiv 2025 query-aware sparsity"

Links: [{"title":"TokenButler: Token Importance is Predictable","url":"https://arxiv.org/html/2503.07518v1"},{"title":"[2503.07518] TokenButler: Token Importance is Predictable","url":"https://arxiv.org/abs/2503.07518"},{"title":"[Literature Review] TokenButler: Token Importance is Predictable","url":"https://www.themoonlight.io/en/review/tokenbutler-token-importance-is-predictable"},{"title":"[2503.07518v1] TokenButler: Token Importance is Predictable","url":"https://arxiv.org/abs/2503.07518v1"},{"title":"arXiv:2506.17121v1 [cs.CL] 20 Jun 2025","url":"https://arxiv.org/pdf/2506.17121"},{"title":"Your LLM Knows the Future: Uncovering Its Multi-Token Prediction Potential","url":"https://arxiv.org/html/2507.11851v1"},{"title":"SlimInfer: Accelerating Long-Context LLM Inference via Dynamic Token Pruning","url":"https://arxiv.org/html/2508.06447v1"},{"title":"FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference Guangda Liu1","url":"https://arxiv.org/pdf/2505.13109"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00397"},{"title":"Query-Aware Token Selection","url":"https://www.emergentmind.com/topics/query-aware-token-selection"}]

Based on the search results, here's information about TokenButler:

## TokenButler: Token Importance is Predictable

TokenButler is a high-granularity, query-aware predictor that learns to identify critical tokens in Large Language Models. By training a light-weight predictor with less than 1.2% parameter overhead, TokenButler prioritizes tokens based on their contextual, predicted importance.

### Key Problem

LLMs rely on the Key-Value (KV) Cache to store token history, enabling efficient decoding of tokens. As the KV-Cache grows, it becomes a major memory and computation bottleneck, especially because prior research has shown that only a small subset of tokens contribute meaningfully to each decoding step. A key challenge in finding these critical tokens is that they are dynamic, and heavily input query-dependent.

### Approach and Results

A key highlight is the stark difference between TokenButler's high-granularity, query-aware approach and existing token-eviction or page-level compression strategies. TokenButler introduces a light predictor that tracks each head's token preference, preserving the tokens that actually matter. This results in up-to 8% gains in perplexity and downstream accuracy.

### Performance at Scale

Even at a very aggressive sparsity of 70%, TokenButler is able to preserve accuracy within 1%, and with a 2% increase in perplexity at 50% sparsity.

The paper was published on arXiv in March 2025 (arxiv: 2503.07518).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "d1d5869c-f07b-4722-8dda-bc4018a6d943",
  "tool_use_result": {
    "query": "TokenButler token importance predictor LLM arxiv 2025 query-aware sparsity",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F8N7h14QCrTfN34szg3yu3",
        "content": [
          {
            "title": "TokenButler: Token Importance is Predictable",
            "url": "https://arxiv.org/html/2503.07518v1"
          },
          {
            "title": "[2503.07518] TokenButler: Token Importance is Predictable",
            "url": "https://arxiv.org/abs/2503.07518"
          },
          {
            "title": "[Literature Review] TokenButler: Token Importance is Predictable",
            "url": "https://www.themoonlight.io/en/review/tokenbutler-token-importance-is-predictable"
          },
          {
            "title": "[2503.07518v1] TokenButler: Token Importance is Predictable",
            "url": "https://arxiv.org/abs/2503.07518v1"
          },
          {
            "title": "arXiv:2506.17121v1 [cs.CL] 20 Jun 2025",
            "url": "https://arxiv.org/pdf/2506.17121"
          },
          {
            "title": "Your LLM Knows the Future: Uncovering Its Multi-Token Prediction Potential",
            "url": "https://arxiv.org/html/2507.11851v1"
          },
          {
            "title": "SlimInfer: Accelerating Long-Context LLM Inference via Dynamic Token Pruning",
            "url": "https://arxiv.org/html/2508.06447v1"
          },
          {
            "title": "FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference Guangda Liu1",
            "url": "https://arxiv.org/pdf/2505.13109"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2602.00397"
          },
          {
            "title": "Query-Aware Token Selection",
            "url": "https://www.emergentmind.com/topics/query-aware-token-selection"
          }
        ]
      },
      "Based on the search results, here's information about TokenButler:\n\n## TokenButler: Token Importance is Predictable\n\nTokenButler is a high-granularity, query-aware predictor that learns to identify critical tokens in Large Language Models. By training a light-weight predictor with less than 1.2% parameter overhead, TokenButler prioritizes tokens based on their contextual, predicted importance.\n\n### Key Problem\n\nLLMs rely on the Key-Value (KV) Cache to store token history, enabling efficient decoding of tokens. As the KV-Cache grows, it becomes a major memory and computation bottleneck, especially because prior research has shown that only a small subset of tokens contribute meaningfully to each decoding step. A key challenge in finding these critical tokens is that they are dynamic, and heavily input query-dependent.\n\n### Approach and Results\n\nA key highlight is the stark difference between TokenButler's high-granularity, query-aware approach and existing token-eviction or page-level compression strategies. TokenButler introduces a light predictor that tracks each head's token preference, preserving the tokens that actually matter. This results in up-to 8% gains in perplexity and downstream accuracy.\n\n### Performance at Scale\n\nEven at a very aggressive sparsity of 70%, TokenButler is able to preserve accuracy within 1%, and with a 2% increase in perplexity at 50% sparsity.\n\nThe paper was published on arXiv in March 2025 (arxiv: 2503.07518)."
    ],
    "durationSeconds": 7.904066060000004
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T08:38:44.579Z_

<details><summary>↩ Tool result · `toolu_011puc5HCs9pjd1oV517M4yp`</summary>

```text
Web search results for query: "PowerInfer-2 arxiv 2024 2025 smartphone inference sparsity"

Links: [{"title":"[2406.06282] PowerInfer-2: Fast Large Language Model Inference on a Smartphone","url":"https://arxiv.org/abs/2406.06282"},{"title":"PowerInfer-2: Fast Large Language Model Inference on a Smartphone","url":"https://arxiv.org/html/2406.06282v3"},{"title":"[Quick Review] PowerInfer-2: Fast Large Language Model Inference on a Smartphone","url":"https://liner.com/review/powerinfer2-fast-large-language-model-inference-on-smartphone"},{"title":"PowerInfer-2: Fast Large Language Model Inference on a Smartphone - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2406.06282"},{"title":"PowerInfer-2: Fast Large Language Model Inference on a Smartphone | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/powerinfer-2-fast-large-language-model-inference"},{"title":"[PDF] PowerInfer-2: Fast Large Language Model Inference on a Smartphone | Semantic Scholar","url":"https://www.semanticscholar.org/paper/PowerInfer-2:-Fast-Large-Language-Model-Inference-a-Xue-Song/0afae4fd689b99b76b46daee66f1be9c743518b6"},{"title":"[2406.06282v2] PowerInfer-2: Fast Large Language Model Inference on a Smartphone","url":"https://arxiv.org/abs/2406.06282v2"},{"title":"GitHub - SJTU-IPADS/PowerInfer: High-speed Large Language Model Serving for Local Deployment","url":"https://github.com/SJTU-IPADS/PowerInfer"},{"title":"[2406.06282v1] PowerInfer-2: Fast Large Language Model Inference on a Smartphone","url":"https://arxiv.org/abs/2406.06282v1"},{"title":"Ripple: Accelerating LLM Inference on Smartphones with Correlation-Aware Neuron Management","url":"https://arxiv.org/html/2410.19274v1"}]

I've found comprehensive information about PowerInfer-2 from the search results. Here's a summary of the key findings:

## PowerInfer-2: Fast Large Language Model Inference on a Smartphone

PowerInfer-2 is a smartphone-based framework that enables fast inference for LLMs exceeding the memory capacity.

### Core Design Approach

The key insight is decomposing matrix operations into neuron clusters as the basic processing unit, which enables flexible scheduling and efficient I/O-computation pipelining. Neuron clusters with dense activations are processed on NPU, while sparse clusters use CPU.

### Sparsity-Aware Techniques

PowerInfer-2's Sparsity-Aware Adaptation simultaneously assigns neuron clusters of different sizes to NPUs for efficient dense matrix operations and CPUs for flexible sparse computations. The framework redistributes the ratio of neuron clusters between NPU and CPU to dynamically adapt to changes in sparsity patterns across different batch sizes.

### Performance Results

PowerInfer-2 achieves up to a 27.8x speed increase compared to state-of-the-art frameworks, and is the first system to serve a 47B LLM on a smartphone, achieving 11.68 tokens/s. These performance improvements preserve model quality with negligible accuracy degradation.

### Impact on Model Performance

Models like TurboSparse-Mixtral-47B benefit from high sparsity, while models with lower sparsity, such as Llama-13B, exhibit slower performance, indicating that the effectiveness of PowerInfer-2's sparse computation mechanisms is directly tied to the inherent sparsity of the LLM.

The paper was first submitted in June 2024 with updates through December 2024, making it a recent contribution to on-device LLM inference optimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "6094438c-9d1e-42c3-bbaa-ab55207ae44f",
  "tool_use_result": {
    "query": "PowerInfer-2 arxiv 2024 2025 smartphone inference sparsity",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G4i7vaeaVr7ADQbFYY7RGx",
        "content": [
          {
            "title": "[2406.06282] PowerInfer-2: Fast Large Language Model Inference on a Smartphone",
            "url": "https://arxiv.org/abs/2406.06282"
          },
          {
            "title": "PowerInfer-2: Fast Large Language Model Inference on a Smartphone",
            "url": "https://arxiv.org/html/2406.06282v3"
          },
          {
            "title": "[Quick Review] PowerInfer-2: Fast Large Language Model Inference on a Smartphone",
            "url": "https://liner.com/review/powerinfer2-fast-large-language-model-inference-on-smartphone"
          },
          {
            "title": "PowerInfer-2: Fast Large Language Model Inference on a Smartphone - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2406.06282"
          },
          {
            "title": "PowerInfer-2: Fast Large Language Model Inference on a Smartphone | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/powerinfer-2-fast-large-language-model-inference"
          },
          {
            "title": "[PDF] PowerInfer-2: Fast Large Language Model Inference on a Smartphone | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/PowerInfer-2:-Fast-Large-Language-Model-Inference-a-Xue-Song/0afae4fd689b99b76b46daee66f1be9c743518b6"
          },
          {
            "title": "[2406.06282v2] PowerInfer-2: Fast Large Language Model Inference on a Smartphone",
            "url": "https://arxiv.org/abs/2406.06282v2"
          },
          {
            "title": "GitHub - SJTU-IPADS/PowerInfer: High-speed Large Language Model Serving for Local Deployment",
            "url": "https://github.com/SJTU-IPADS/PowerInfer"
          },
          {
            "title": "[2406.06282v1] PowerInfer-2: Fast Large Language Model Inference on a Smartphone",
            "url": "https://arxiv.org/abs/2406.06282v1"
          },
          {
            "title": "Ripple: Accelerating LLM Inference on Smartphones with Correlation-Aware Neuron Management",
            "url": "https://arxiv.org/html/2410.19274v1"
          }
        ]
      },
      "I've found comprehensive information about PowerInfer-2 from the search results. Here's a summary of the key findings:\n\n## PowerInfer-2: Fast Large Language Model Inference on a Smartphone\n\nPowerInfer-2 is a smartphone-based framework that enables fast inference for LLMs exceeding the memory capacity.\n\n### Core Design Approach\n\nThe key insight is decomposing matrix operations into neuron clusters as the basic processing unit, which enables flexible scheduling and efficient I/O-computation pipelining. Neuron clusters with dense activations are processed on NPU, while sparse clusters use CPU.\n\n### Sparsity-Aware Techniques\n\nPowerInfer-2's Sparsity-Aware Adaptation simultaneously assigns neuron clusters of different sizes to NPUs for efficient dense matrix operations and CPUs for flexible sparse computations. The framework redistributes the ratio of neuron clusters between NPU and CPU to dynamically adapt to changes in sparsity patterns across different batch sizes.\n\n### Performance Results\n\nPowerInfer-2 achieves up to a 27.8x speed increase compared to state-of-the-art frameworks, and is the first system to serve a 47B LLM on a smartphone, achieving 11.68 tokens/s. These performance improvements preserve model quality with negligible accuracy degradation.\n\n### Impact on Model Performance\n\nModels like TurboSparse-Mixtral-47B benefit from high sparsity, while models with lower sparsity, such as Llama-13B, exhibit slower performance, indicating that the effectiveness of PowerInfer-2's sparse computation mechanisms is directly tied to the inherent sparsity of the LLM.\n\nThe paper was first submitted in June 2024 with updates through December 2024, making it a recent contribution to on-device LLM inference optimization."
    ],
    "durationSeconds": 8.815892910000002
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have enough information to select 2-3 papers. Let me evaluate the candidates:

1. **PowerInfer** (2312.12456) - SOSP 2024. This is a seminal work on exploiting activation sparsity for GPU-CPU hybrid inference. It uses adaptive predictors, exploits power-law distribution in neuron activation. Very relevant to our work as it's a system that relies on sparsity prediction for efficient inference. Category: background/method-component.

2. **TokenButler** (2503.07518) - March 2025. Query-aware predictor for token importance. 

TokenButler focuses on KV cache sparsity at the token level rather than neuron-level activation sparsity, so it's less directly aligned with our approach.

3. **PowerInfer-2** (2406.06282) - 2024. Extends PowerInfer to smartphones with neuron cluster decomposition, which is less central to the prediction mechanism itself.

For our project on KL distillation for sparse SwiGLU activation prediction, PowerInfer stands out as the most essential reference—it pioneered using sparsity predictors for efficient inference by leveraging the power-law distribution of neuron activations.

Let me search for more recent work from 2025-2026 that specifically addresses learned neuron-level sparsity predictors, and I should also check SparseLoRA (2506.16500) for contextual sparsity insights and Ripple (2410.19274) for its correlation-aware neuron management approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "3ed2ebae-7576-419a-8233-8ddb261a83c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYQxucdDbB4jxfBa6qLSFN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2085,
      "cache_read_input_tokens": 33946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2085
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

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WH6t7G1qkRNSwSsq4MDBs6`</summary>

```json
{
  "query": "\"Ripple\" neuron management LLM sparsity predictor correlation arxiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "5b255e40-e915-4119-a3c2-08afe5076200",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYQxucdDbB4jxfBa6qLSFN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2085,
      "cache_read_input_tokens": 33946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2085
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_013igS7C9BLyNkk5S3xjF7JN`</summary>

```json
{
  "query": "MoE activation sparsity prediction routing 2025 2026 FFN expert selection learned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "16fc4371-e4fe-44b8-8806-fd7e21e21508",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYQxucdDbB4jxfBa6qLSFN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2085,
      "cache_read_input_tokens": 33946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2085
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

_source line 26 · 2026-05-16T08:39:05.925Z_

<details><summary>↩ Tool result · `toolu_01WH6t7G1qkRNSwSsq4MDBs6`</summary>

```text
Web search results for query: ""Ripple" neuron management LLM sparsity predictor correlation arxiv 2024"

Links: [{"title":"Ripple: Accelerating LLM Inference on Smartphones with Correlation-Aware Neuron Management","url":"https://arxiv.org/html/2410.19274v1"},{"title":"Ripple: Accelerating LLM Inference on Smartphones with Correlation-Aware Neuron Management | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/ripple-accelerating-llm-inference-smartphones-correlation-aware"},{"title":"(PDF) Ripple: Accelerating LLM Inference on Smartphones with Correlation-Aware Neuron Management","url":"https://www.researchgate.net/publication/385291661_Ripple_Accelerating_LLM_Inference_on_Smartphones_with_Correlation-Aware_Neuron_Management"},{"title":"Ripple: Accelerating LLM Inference on Smartphones with Correlation-Aware Neuron Management | PromptLayer","url":"https://www.promptlayer.com/research-papers/ripple-bringing-powerful-llms-to-your-smartphone"},{"title":"[PDF] Ripple: Accelerating LLM Inference on Smartphones with Correlation-Aware Neuron Management | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Ripple:-Accelerating-LLM-Inference-on-Smartphones-Wang-Fan/42c05ce4147844ffe66ede596f1461cdde45f565"},{"title":"[2410.19274] Neuralink: Fast LLM Inference on Smartphones with Neuron Co-Activation Linking","url":"https://arxiv.org/abs/2410.19274"},{"title":"Small Language Models: Survey, Measurements, and Insights","url":"https://arxiv.org/html/2409.15790v3"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/html/2406.16635v1"},{"title":"VLM in a flash: I/O-Efficient Sparsification of Vision-Language Model via Neuron Chunking","url":"https://arxiv.org/html/2511.18692v1"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/html/2505.14884v1"}]

Based on the search results, I found relevant information about Ripple and its relationship to neuron management, LLM sparsity, and predictor correlations:

## Overview

Ripple is a novel approach that accelerates LLM inference on smartphones by optimizing neuron placement in flash memory, leveraging the concept of Neuron Co-Activation, where neurons frequently activated together are linked to facilitate continuous read access and optimize data transfer efficiency.

## Key Findings

**Sparsity-Based Approach**: Deja Vu pioneered a predictor-based approach for sparsity-based LLM inference, greatly reducing inference latency, and Ripple builds upon this foundational work by extending the sparsity concept with correlation-aware optimizations.

**Correlation-Aware Neuron Management**: Ripple employs correlation-aware neuron management to identify and selectively process the most important neurons, skipping the inactive ones.

**Architecture and Solution**: Ripple's approach incorporates a two-stage solution: an offline stage that reorganizes neuron placement based on co-activation patterns, and an online stage that employs tailored data access and caching strategies to align well with hardware characteristics.

**Performance**: Evaluations conducted on a variety of smartphones and LLMs demonstrate that Ripple achieves up to 5.93 × improvements in I/O latency compared to the state-of-the-art.

**Research Contribution**: As the first solution to optimize storage placement under sparsity, Ripple explores a new optimization space at the intersection of sparsity-driven algorithm and storage-level system co-design in LLM inference.

The paper was published on arXiv in October 2024 (arXiv:2410.19274).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "67dd1feb-c48b-4d95-958f-5aee77182168",
  "tool_use_result": {
    "query": "\"Ripple\" neuron management LLM sparsity predictor correlation arxiv 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AzrV2xSE9uwrvWgJKFBrxw",
        "content": [
          {
            "title": "Ripple: Accelerating LLM Inference on Smartphones with Correlation-Aware Neuron Management",
            "url": "https://arxiv.org/html/2410.19274v1"
          },
          {
            "title": "Ripple: Accelerating LLM Inference on Smartphones with Correlation-Aware Neuron Management | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/ripple-accelerating-llm-inference-smartphones-correlation-aware"
          },
          {
            "title": "(PDF) Ripple: Accelerating LLM Inference on Smartphones with Correlation-Aware Neuron Management",
            "url": "https://www.researchgate.net/publication/385291661_Ripple_Accelerating_LLM_Inference_on_Smartphones_with_Correlation-Aware_Neuron_Management"
          },
          {
            "title": "Ripple: Accelerating LLM Inference on Smartphones with Correlation-Aware Neuron Management | PromptLayer",
            "url": "https://www.promptlayer.com/research-papers/ripple-bringing-powerful-llms-to-your-smartphone"
          },
          {
            "title": "[PDF] Ripple: Accelerating LLM Inference on Smartphones with Correlation-Aware Neuron Management | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Ripple:-Accelerating-LLM-Inference-on-Smartphones-Wang-Fan/42c05ce4147844ffe66ede596f1461cdde45f565"
          },
          {
            "title": "[2410.19274] Neuralink: Fast LLM Inference on Smartphones with Neuron Co-Activation Linking",
            "url": "https://arxiv.org/abs/2410.19274"
          },
          {
            "title": "Small Language Models: Survey, Measurements, and Insights",
            "url": "https://arxiv.org/html/2409.15790v3"
          },
          {
            "title": "ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models",
            "url": "https://arxiv.org/html/2406.16635v1"
          },
          {
            "title": "VLM in a flash: I/O-Efficient Sparsification of Vision-Language Model via Neuron Chunking",
            "url": "https://arxiv.org/html/2511.18692v1"
          },
          {
            "title": "Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity",
            "url": "https://arxiv.org/html/2505.14884v1"
          }
        ]
      },
      "Based on the search results, I found relevant information about Ripple and its relationship to neuron management, LLM sparsity, and predictor correlations:\n\n## Overview\n\nRipple is a novel approach that accelerates LLM inference on smartphones by optimizing neuron placement in flash memory, leveraging the concept of Neuron Co-Activation, where neurons frequently activated together are linked to facilitate continuous read access and optimize data transfer efficiency.\n\n## Key Findings\n\n**Sparsity-Based Approach**: Deja Vu pioneered a predictor-based approach for sparsity-based LLM inference, greatly reducing inference latency, and Ripple builds upon this foundational work by extending the sparsity concept with correlation-aware optimizations.\n\n**Correlation-Aware Neuron Management**: Ripple employs correlation-aware neuron management to identify and selectively process the most important neurons, skipping the inactive ones.\n\n**Architecture and Solution**: Ripple's approach incorporates a two-stage solution: an offline stage that reorganizes neuron placement based on co-activation patterns, and an online stage that employs tailored data access and caching strategies to align well with hardware characteristics.\n\n**Performance**: Evaluations conducted on a variety of smartphones and LLMs demonstrate that Ripple achieves up to 5.93 × improvements in I/O latency compared to the state-of-the-art.\n\n**Research Contribution**: As the first solution to optimize storage placement under sparsity, Ripple explores a new optimization space at the intersection of sparsity-driven algorithm and storage-level system co-design in LLM inference.\n\nThe paper was published on arXiv in October 2024 (arXiv:2410.19274)."
    ],
    "durationSeconds": 7.779072841999994
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T08:39:06.805Z_

<details><summary>↩ Tool result · `toolu_013igS7C9BLyNkk5S3xjF7JN`</summary>

```text
Web search results for query: "MoE activation sparsity prediction routing 2025 2026 FFN expert selection learned"

Links: [{"title":"Exploiting Activation Sparsity with Dense to Dynamic-k ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf"},{"title":"Read-ME: Refactorizing LLMs as Router-Decoupled ...","url":"https://utns.cs.utexas.edu/assets/papers/neurips24-readme.pdf"},{"title":"Mixture of Experts Explained","url":"https://huggingface.co/blog/moe"},{"title":"Refactorizing LLMs as Router-Decoupled Mixture of ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d298cf34e4539f9134db7f38b42f69fe-Paper-Conference.pdf"},{"title":"What is mixture of experts? | IBM","url":"https://www.ibm.com/think/topics/mixture-of-experts"},{"title":"Analytical FFN-to-MoE Restructuring via Activation Pattern Analysis","url":"https://arxiv.org/html/2502.04416"},{"title":"Sparse Mixture-of-Experts (MoE) Models","url":"https://www.emergentmind.com/topics/sparse-mixture-of-experts-moe-models"},{"title":"The Sparse MoE Approach","url":"https://apxml.com/courses/mixture-of-experts/chapter-1-moe-foundations-sparse-models/sparse-moe-paradigm"},{"title":"Exploiting Transformer Activation Sparsity with Dynamic Inference","url":"https://neurips2023-enlsp.github.io/papers/paper_37.pdf"},{"title":"Mixture of Experts (MoE) Explained: How Sparse Activation","url":"https://gurusup.com/blog/mixture-of-experts-moe-explained"}]

I found relevant research results on MoE activation sparsity, prediction routing, and FFN expert selection. Here's a summary of recent developments:

## Key Research Directions

**Activation Sparsity and Router-Based Expert Selection:**

Recent work converts FFN layers to MoE layers with routers that predict the contribution of each expert using regression-based formulations that directly predict the ℓ2-norm of the output of each expert.

**Analytical FFN-to-MoE Restructuring (2025):**

Recent analytical frameworks analyze neuron activation patterns to distinguish frequently active neurons from sparsely active ones, partitioning neurons into always-active shared experts and conditionally activated routed experts, then construct a router analytically from representative neuron statistics.

**Router Prediction and Dynamic Routing:**

Researchers propose novel learning objectives for training routers that enable them to accurately predict the relative contribution of each expert, while introducing Dynamic-k routing that allows models to adapt the amount of compute to the difficulty of the input.

**Pre-Gating and Router Decoupling:**

Recent work refactorizes pre-trained dense LLMs into specialized experts through activation sparsity and proposes decoupling the router from the MoE backbone, allowing pre-gating of all requests before inference and applying lookahead scheduling based on expert assignments.

**Load Balancing and Expert Utilization:**

Methods like SEER-MoE prune experts using heavy-hitter statistics and entropy-regularized fine-tuning, while SiDA-MoE exploits router predictability by prefetching likely-to-be-activated experts based on predicted routing patterns.

These developments show active research into improving MoE efficiency through better activation sparsity exploitation, learned routing mechanisms, and system-level optimizations for expert selection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "fc75e45c-2f4f-4a03-89a4-166eee6289b4",
  "tool_use_result": {
    "query": "MoE activation sparsity prediction routing 2025 2026 FFN expert selection learned",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F644ZuM8kEuQZw6geV3sRn",
        "content": [
          {
            "title": "Exploiting Activation Sparsity with Dense to Dynamic-k ...",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf"
          },
          {
            "title": "Read-ME: Refactorizing LLMs as Router-Decoupled ...",
            "url": "https://utns.cs.utexas.edu/assets/papers/neurips24-readme.pdf"
          },
          {
            "title": "Mixture of Experts Explained",
            "url": "https://huggingface.co/blog/moe"
          },
          {
            "title": "Refactorizing LLMs as Router-Decoupled Mixture of ...",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/d298cf34e4539f9134db7f38b42f69fe-Paper-Conference.pdf"
          },
          {
            "title": "What is mixture of experts? | IBM",
            "url": "https://www.ibm.com/think/topics/mixture-of-experts"
          },
          {
            "title": "Analytical FFN-to-MoE Restructuring via Activation Pattern Analysis",
            "url": "https://arxiv.org/html/2502.04416"
          },
          {
            "title": "Sparse Mixture-of-Experts (MoE) Models",
            "url": "https://www.emergentmind.com/topics/sparse-mixture-of-experts-moe-models"
          },
          {
            "title": "The Sparse MoE Approach",
            "url": "https://apxml.com/courses/mixture-of-experts/chapter-1-moe-foundations-sparse-models/sparse-moe-paradigm"
          },
          {
            "title": "Exploiting Transformer Activation Sparsity with Dynamic Inference",
            "url": "https://neurips2023-enlsp.github.io/papers/paper_37.pdf"
          },
          {
            "title": "Mixture of Experts (MoE) Explained: How Sparse Activation",
            "url": "https://gurusup.com/blog/mixture-of-experts-moe-explained"
          }
        ]
      },
      "I found relevant research results on MoE activation sparsity, prediction routing, and FFN expert selection. Here's a summary of recent developments:\n\n## Key Research Directions\n\n**Activation Sparsity and Router-Based Expert Selection:**\n\nRecent work converts FFN layers to MoE layers with routers that predict the contribution of each expert using regression-based formulations that directly predict the ℓ2-norm of the output of each expert.\n\n**Analytical FFN-to-MoE Restructuring (2025):**\n\nRecent analytical frameworks analyze neuron activation patterns to distinguish frequently active neurons from sparsely active ones, partitioning neurons into always-active shared experts and conditionally activated routed experts, then construct a router analytically from representative neuron statistics.\n\n**Router Prediction and Dynamic Routing:**\n\nResearchers propose novel learning objectives for training routers that enable them to accurately predict the relative contribution of each expert, while introducing Dynamic-k routing that allows models to adapt the amount of compute to the difficulty of the input.\n\n**Pre-Gating and Router Decoupling:**\n\nRecent work refactorizes pre-trained dense LLMs into specialized experts through activation sparsity and proposes decoupling the router from the MoE backbone, allowing pre-gating of all requests before inference and applying lookahead scheduling based on expert assignments.\n\n**Load Balancing and Expert Utilization:**\n\nMethods like SEER-MoE prune experts using heavy-hitter statistics and entropy-regularized fine-tuning, while SiDA-MoE exploits router predictability by prefetching likely-to-be-activated experts based on predicted routing patterns.\n\nThese developments show active research into improving MoE efficiency through better activation sparsity exploitation, learned routing mechanisms, and system-level optimizations for expert selection."
    ],
    "durationSeconds": 8.551978196000004
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Let me also check one more interesting paper - "Polar Sparsity" that appeared in the earlier search results. That's from May 2025 and seems to be about scalable contextual sparsity with high throughput batched inference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "737ecbc7-3789-43e4-8147-70b1e23043dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHTqYz8pVHR1TA9Ci4jRP8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2763,
      "cache_read_input_tokens": 36031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2763
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

_source line 29_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WyppNaUMSHu4WaUkuyCyTx`</summary>

```json
{
  "query": "\"Polar Sparsity\" batched LLM inference contextual sparsity 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "037f8236-08f0-4345-9259-9a8f4d2263ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHTqYz8pVHR1TA9Ci4jRP8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2763,
      "cache_read_input_tokens": 36031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2763
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

_source line 30 · 2026-05-16T08:39:17.042Z_

<details><summary>↩ Tool result · `toolu_01WyppNaUMSHu4WaUkuyCyTx`</summary>

```text
Web search results for query: ""Polar Sparsity" batched LLM inference contextual sparsity 2025 arxiv"

Links: [{"title":"[2505.14884] Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/abs/2505.14884"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/html/2505.14884v1"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing ...","url":"https://arxiv.org/pdf/2505.14884"},{"title":"Paper page - Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://huggingface.co/papers/2505.14884"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=21275&show=1000"},{"title":"Computer Science May 2025","url":"https://www.arxiv.org/list/cs/2025-05?skip=7125&show=1000"},{"title":"NeurIPS Poster Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/117070"},{"title":"ENABLING DYNAMIC SPARSITY IN QUANTIZED LLM INFERENCE","url":"https://arxiv.org/pdf/2511.04477"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/html/2603.14110"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity | OpenReview","url":"https://openreview.net/forum?id=cg2S1qqNSq"}]

Based on the search results, I found comprehensive information about "Polar Sparsity" on arXiv.

## Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity

Accelerating large language model (LLM) inference is critical for real-world deployments requiring high throughput and low latency. Contextual sparsity, where each token dynamically activates only a small subset of the model parameters, shows promise but does not scale to large batch sizes due to union of active neurons quickly approaching dense computation.

### Key Innovation

Polar Sparsity highlights a key shift in sparsity importance from MLP to Attention layers as batch size and sequence length scale. While MLP layers become more compute-efficient under batching, their sparsity vanishes. In contrast, attention becomes increasingly more expensive at scale, while their head sparsity remains stable and batch-invariant.

### Technical Approach & Results

The approach develops Selective Head Attention with hardware-efficient, sparsity-aware GPU kernels, delivering up to 2.2× end-to-end speedups for models like OPT, LLaMA-2 & 3, Qwen, Mistral across various batch sizes and sequence lengths without compromising accuracy.

### Significance

This is the first work to demonstrate that contextual sparsity can scale effectively to large batch sizes, delivering substantial inference acceleration with minimal changes, making Polar Sparsity practical for large-scale, high-throughput LLM deployment systems.

**Paper Details:** The paper (arXiv:2505.14884) was published on May 20, 2025, by authors Susav Shrestha, Brad Settlemyer, Nikoli Dryden, and Narasimha Reddy. The code is available at GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "c74c7bd6-e0f4-4285-a1a9-d192563f439a",
  "tool_use_result": {
    "query": "\"Polar Sparsity\" batched LLM inference contextual sparsity 2025 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WM2AGRVri1b5Kw3SbzAs4A",
        "content": [
          {
            "title": "[2505.14884] Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity",
            "url": "https://arxiv.org/abs/2505.14884"
          },
          {
            "title": "Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity",
            "url": "https://arxiv.org/html/2505.14884v1"
          },
          {
            "title": "Polar Sparsity: High Throughput Batched LLM Inferencing ...",
            "url": "https://arxiv.org/pdf/2505.14884"
          },
          {
            "title": "Paper page - Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity",
            "url": "https://huggingface.co/papers/2505.14884"
          },
          {
            "title": "Artificial Intelligence 2025",
            "url": "https://arxiv.org/list/cs.AI/2025?skip=21275&show=1000"
          },
          {
            "title": "Computer Science May 2025",
            "url": "https://www.arxiv.org/list/cs/2025-05?skip=7125&show=1000"
          },
          {
            "title": "NeurIPS Poster Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/117070"
          },
          {
            "title": "ENABLING DYNAMIC SPARSITY IN QUANTIZED LLM INFERENCE",
            "url": "https://arxiv.org/pdf/2511.04477"
          },
          {
            "title": "SVD Contextual Sparsity Predictors for Fast LLM Inference",
            "url": "https://arxiv.org/html/2603.14110"
          },
          {
            "title": "Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity | OpenReview",
            "url": "https://openreview.net/forum?id=cg2S1qqNSq"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about \"Polar Sparsity\" on arXiv.\n\n## Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity\n\nAccelerating large language model (LLM) inference is critical for real-world deployments requiring high throughput and low latency. Contextual sparsity, where each token dynamically activates only a small subset of the model parameters, shows promise but does not scale to large batch sizes due to union of active neurons quickly approaching dense computation.\n\n### Key Innovation\n\nPolar Sparsity highlights a key shift in sparsity importance from MLP to Attention layers as batch size and sequence length scale. While MLP layers become more compute-efficient under batching, their sparsity vanishes. In contrast, attention becomes increasingly more expensive at scale, while their head sparsity remains stable and batch-invariant.\n\n### Technical Approach & Results\n\nThe approach develops Selective Head Attention with hardware-efficient, sparsity-aware GPU kernels, delivering up to 2.2× end-to-end speedups for models like OPT, LLaMA-2 & 3, Qwen, Mistral across various batch sizes and sequence lengths without compromising accuracy.\n\n### Significance\n\nThis is the first work to demonstrate that contextual sparsity can scale effectively to large batch sizes, delivering substantial inference acceleration with minimal changes, making Polar Sparsity practical for large-scale, high-throughput LLM deployment systems.\n\n**Paper Details:** The paper (arXiv:2505.14884) was published on May 20, 2025, by authors Susav Shrestha, Brad Settlemyer, Nikoli Dryden, and Narasimha Reddy. The code is available at GitHub."
    ],
    "durationSeconds": 5.201173767999993
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Now I have good candidates. Let me select the best 2-3 papers:

1. **PowerInfer** (2312.12456) - SOSP 2024. This is definitely needed - it's the pioneering GPU-CPU hybrid inference system exploiting activation sparsity with adaptive predictors. It establishes the power-law distribution of neuron activation and uses predictors for efficient inference. Very relevant as a foundational work.

2. **Polar Sparsity** (2505.14884) - NeurIPS 2025. This is interesting and recent (May 2025). It reveals that MLP contextual sparsity doesn't scale to large batches (union of active neurons approaches dense), but attention head sparsity is batch-invariant. 

This directly challenges the scalability of our approach at large batch sizes, making it essential for understanding the limitations of MLP neuron sparsity prediction. **TokenButler** (2503.07518) focuses on KV cache token-level sparsity rather than neuron-level activation sparsity, so it's less directly relevant. Given the focus on contextual sparsity prediction, PowerInfer and Polar Sparsity are the strongest choices—one establishes the foundational approach while the other reveals critical scalability constraints we need to address. Now I'm gathering the specific details for both papers—pulling the arxiv IDs, author names, and venue information. For PowerInfer, I need to confirm the exact author list from SJTU IPADS, and I've got Polar Sparsity pinned down with its NeurIPS 2025 acceptance and the arxiv identifier. I'm placing PowerInfer in Direction 4 since it deals with predictor-based activation sparsity, while Polar Sparsity fits better with contextual sparsity scalability. Now I'm formatting the entries with their metadata—titles, authors, venues, and key findings about how PowerInfer leverages the power-law distribution of neuron activations to enable efficient GPU-CPU hybrid inference. 终激活，大量cold neurons input-dependent），将hot neurons预加载至GPU、cold neurons在CPU计算，配合adaptive sparsity predictor，单RTX 4090上比llama.cpp快11.69x。PowerInfer的核心假设（neuron activation有power-law locality）直接支持我们predictor的设计：hot neurons无需预测（始终激活），predictor重点预测cold neurons的contextual activation。其adaptive predictor用较小网络预测高稀疏层的思路可参考。

对于Polar Sparsity这篇2025年的工作，它首次揭示了MLP contextual sparsity在batch场景下的扩展性问题——随着batch size增加，不同token的active neuron取并集会趋近dense计算，导致sparsity增益消失，而attention head sparsity则保持batch-invariant的特性。这对我们的工作很重要，因为它表明MLP neuron-level contextual sparsity主要适用于特定场景。

我们需要在论文中明确讨论这一适用范围的限制。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "c51d3208-d95c-49ce-8e53-389af7876185",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qZNvmpCZ1X2zTzTfwGJMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 38794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1133
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

_source line 32_

I have enough information. Let me add PowerInfer and Polar Sparsity — both highly relevant and not in the existing list.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "1524bff8-5ba5-4b02-b171-c129bf8a38f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qZNvmpCZ1X2zTzTfwGJMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 38794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1133
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

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_0134EMqhAP4LwhZ1xHLirJra`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml",
  "old_string": "- title: \"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering\"\n  authors: [Nobel Dhar, Bobin Deng, Md Romyull Islam, Xinyue Zhang, Kazi Fahim Ahmad Nasif, Kun Suo]\n  venue: Euro-Par 2025\n  year: 2025\n  arxiv_id: \"2507.14179\"\n  category: background\n  role: \"Clustering-based sparsity prediction——用聚类简化prediction\"\n  key_finding: \"将activation patterns聚类为representative clusters，预测cluster assignment而非individual neuron states，减少prediction开销。Mistral-7B上79.34%聚类精度\"\n  relevance_to_us: \"降低predictor复杂度的思路。如果我们的per-neuron KL predictor开销太大，可考虑cluster-level prediction\"\n\n# =============================================================================\n# 竞争格局总结",
  "new_string": "- title: \"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering\"\n  authors: [Nobel Dhar, Bobin Deng, Md Romyull Islam, Xinyue Zhang, Kazi Fahim Ahmad Nasif, Kun Suo]\n  venue: Euro-Par 2025\n  year: 2025\n  arxiv_id: \"2507.14179\"\n  category: background\n  role: \"Clustering-based sparsity prediction——用聚类简化prediction\"\n  key_finding: \"将activation patterns聚类为representative clusters，预测cluster assignment而非individual neuron states，减少prediction开销。Mistral-7B上79.34%聚类精度\"\n  relevance_to_us: \"降低predictor复杂度的思路。如果我们的per-neuron KL predictor开销太大，可考虑cluster-level prediction\"\n\n- title: \"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU\"\n  authors: [Yixin Song, Zeyu Mi, Haotong Xie, Haibo Chen]\n  venue: SOSP 2024\n  year: 2024\n  arxiv_id: \"2312.12456\"\n  category: background\n  role: \"GPU-CPU混合推理利用activation sparsity的开创性系统工作——建立neuron activation power-law分布\"\n  key_finding: \"利用LLM neuron activation的power-law分布（少量hot neurons跨input始终激活，大量cold neurons input-dependent），将hot neurons预加载至GPU、cold neurons在CPU计算，配合adaptive sparsity predictor，单RTX 4090上比llama.cpp快11.69x\"\n  relevance_to_us: \"PowerInfer的核心假设（neuron activation有power-law locality）直接支持我们predictor的设计：hot neurons无需预测（始终激活），predictor重点预测cold neurons的contextual activation。其adaptive predictor用较小网络预测高稀疏层的思路可参考\"\n\n- title: \"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity\"\n  authors: [Susav Shrestha, Brad Settlemyer, Nikoli Dryden, Narasimha Reddy]\n  venue: NeurIPS 2025\n  year: 2025\n  arxiv_id: \"2505.14884\"\n  category: background\n  role: \"揭示MLP contextual sparsity在batch场景下不可扩展——attention head sparsity更稳定\"\n  key_finding: \"首次揭示MLP contextual sparsity的扩展性瓶颈：随batch size增加，batch内不同token的active neuron取并集趋近dense计算，MLP sparsity增益消失。相反attention head sparsity是batch-invariant的。提出Selective Head Attention实现2.2x加速\"\n  relevance_to_us: \"对我们工作的重要约束和定位信息：MLP neuron-level contextual sparsity（我们的方法）主要适用于decoding（batch=1）场景。在大batch prefill中需要不同策略。论文中应明确讨论这一适用范围\"\n\n# =============================================================================\n# 竞争格局总结"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "2b59c1db-9de7-434a-b5ad-4935239813bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qZNvmpCZ1X2zTzTfwGJMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 38794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1133
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

_source line 34 · 2026-05-16T08:40:11.275Z_

<details><summary>↩ Tool result · `toolu_0134EMqhAP4LwhZ1xHLirJra`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "933f1ea9-5f22-42ed-bbc1-ab06d3daf69a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml",
    "oldString": "- title: \"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering\"\n  authors: [Nobel Dhar, Bobin Deng, Md Romyull Islam, Xinyue Zhang, Kazi Fahim Ahmad Nasif, Kun Suo]\n  venue: Euro-Par 2025\n  year: 2025\n  arxiv_id: \"2507.14179\"\n  category: background\n  role: \"Clustering-based sparsity prediction——用聚类简化prediction\"\n  key_finding: \"将activation patterns聚类为representative clusters，预测cluster assignment而非individual neuron states，减少prediction开销。Mistral-7B上79.34%聚类精度\"\n  relevance_to_us: \"降低predictor复杂度的思路。如果我们的per-neuron KL predictor开销太大，可考虑cluster-level prediction\"\n\n# =============================================================================\n# 竞争格局总结",
    "newString": "- title: \"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering\"\n  authors: [Nobel Dhar, Bobin Deng, Md Romyull Islam, Xinyue Zhang, Kazi Fahim Ahmad Nasif, Kun Suo]\n  venue: Euro-Par 2025\n  year: 2025\n  arxiv_id: \"2507.14179\"\n  category: background\n  role: \"Clustering-based sparsity prediction——用聚类简化prediction\"\n  key_finding: \"将activation patterns聚类为representative clusters，预测cluster assignment而非individual neuron states，减少prediction开销。Mistral-7B上79.34%聚类精度\"\n  relevance_to_us: \"降低predictor复杂度的思路。如果我们的per-neuron KL predictor开销太大，可考虑cluster-level prediction\"\n\n- title: \"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU\"\n  authors: [Yixin Song, Zeyu Mi, Haotong Xie, Haibo Chen]\n  venue: SOSP 2024\n  year: 2024\n  arxiv_id: \"2312.12456\"\n  category: background\n  role: \"GPU-CPU混合推理利用activation sparsity的开创性系统工作——建立neuron activation power-law分布\"\n  key_finding: \"利用LLM neuron activation的power-law分布（少量hot neurons跨input始终激活，大量cold neurons input-dependent），将hot neurons预加载至GPU、cold neurons在CPU计算，配合adaptive sparsity predictor，单RTX 4090上比llama.cpp快11.69x\"\n  relevance_to_us: \"PowerInfer的核心假设（neuron activation有power-law locality）直接支持我们predictor的设计：hot neurons无需预测（始终激活），predictor重点预测cold neurons的contextual activation。其adaptive predictor用较小网络预测高稀疏层的思路可参考\"\n\n- title: \"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity\"\n  authors: [Susav Shrestha, Brad Settlemyer, Nikoli Dryden, Narasimha Reddy]\n  venue: NeurIPS 2025\n  year: 2025\n  arxiv_id: \"2505.14884\"\n  category: background\n  role: \"揭示MLP contextual sparsity在batch场景下不可扩展——attention head sparsity更稳定\"\n  key_finding: \"首次揭示MLP contextual sparsity的扩展性瓶颈：随batch size增加，batch内不同token的active neuron取并集趋近dense计算，MLP sparsity增益消失。相反attention head sparsity是batch-invariant的。提出Selective Head Attention实现2.2x加速\"\n  relevance_to_us: \"对我们工作的重要约束和定位信息：MLP neuron-level contextual sparsity（我们的方法）主要适用于decoding（batch=1）场景。在大batch prefill中需要不同策略。论文中应明确讨论这一适用范围\"\n\n# =============================================================================\n# 竞争格局总结",
    "originalFile": "# Literature Map: KL Distillation for Sparse SwiGLU Activation Prediction\n# Last updated: 2026-05-15\n# Survey scope: 2023-2026, 4 directions\n\n# =============================================================================\n# Direction 1: KL distillation for structured/activation sparsity\n# Finding: NO prior work uses KL to train an activation sparsity PREDICTOR.\n# Existing predictors use BCE (DejaVu, ShadowLLM). SPON uses KL but for\n# learnable bias correction, not predictor training. This is our novelty.\n# =============================================================================\n\n- title: \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\"\n  authors: [Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, Tengfei Ma]\n  venue: ICML 2026\n  year: 2026\n  arxiv_id: \"2512.12744\"\n  category: direct-competitor\n  role: \"最接近的KL蒸馏用于稀疏性的工作——但SPON训练的是可学习bias项而非predictor\"\n  key_finding: \"SPON注入input-independent learnable activation vectors作为sparse computation的anchor，用KL散度(dense vs sparse logits)做distribution matching训练，训练后吸收进bias项，零推理开销\"\n  relevance_to_us: \"SPON证明KL divergence比BCE/MSE更适合sparsity场景的distribution matching。但SPON是全局bias correction而非per-token predictor——我们的predictor方案能实现input-dependent的sparsity pattern，比SPON更灵活。SPON在50-60% sparsity下测试，与我们目标一致\"\n\n- title: \"Compact Language Models via Pruning and Knowledge Distillation\"\n  authors: [Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz, Pavlo Molchanov]\n  venue: NeurIPS 2024\n  year: 2024\n  arxiv_id: \"2407.14679\"\n  category: method-component\n  role: \"KL蒸馏用于结构化剪枝后恢复——验证logit-only KL优于intermediate matching\"\n  key_finding: \"Minitron用logit-only forward KL divergence做structured pruning后的distillation recovery，发现仅用KL loss（不用CE或intermediate matching）效果最好，学生模型继承了teacher的inter-token关系和confidence calibration\"\n  relevance_to_us: \"支持我们的核心假设：KL divergence保留output distribution比逐元素BCE更优。Minitron的发现（logit-only KL最优）为我们predictor的KL训练目标提供了理论支撑\"\n\n- title: \"Instruction-Following Pruning for Large Language Models\"\n  authors: [Bairu Hou, Qibin Chen, Jianyu Wang, Guoli Yin, Chong Wang, Nan Du, Ruoming Pang, Shiyu Chang, Tao Lei]\n  venue: ICML 2025\n  year: 2025\n  arxiv_id: \"2501.02086\"\n  category: method-component\n  role: \"训练sparse mask predictor的范式——input-dependent mask selection\"\n  key_finding: \"训练一个sparse mask predictor以instruction为输入动态选择最相关参数子集，联合优化mask predictor和LLM\"\n  relevance_to_us: \"架构上与我们类似（训练predictor生成mask），但目标是instruction-aware weight pruning而非activation sparsity。可参考其predictor-LLM联合优化策略\"\n\n# =============================================================================\n# Direction 2: Output distribution preservation in pruning/sparsity\n# =============================================================================\n\n- title: \"Distilling to Hybrid Attention Models via KL-Guided Layer Selection\"\n  authors: []\n  venue: arXiv\n  year: 2025\n  arxiv_id: \"2512.20569\"\n  category: method-component\n  role: \"KL散度引导layer selection——用distribution差异决定哪些层需要保留\"\n  key_finding: \"用KL divergence作为指标选择哪些attention层替换为hybrid attention，通过最小化output distribution变化来指导架构决策\"\n  relevance_to_us: \"方法论启示：KL divergence不仅可作为训练loss，还可作为layer-wise重要性指标。我们可用per-layer KL分析哪些层的sparsity对output distribution影响最大\"\n\n# =============================================================================\n# Direction 3: SPON和类似的learnable bias correction for sparsity\n# =============================================================================\n\n- title: \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\"\n  authors: [Aayush Gautam, Mukul Gagrani, Junyoung Park, Mingu Lee, Chiris Lott, Narasimha Reddy]\n  venue: arXiv\n  year: 2026\n  arxiv_id: \"2602.00397\"\n  category: direct-competitor\n  role: \"Predictor + error compensation双组件架构——与SPON的bias correction思路互补\"\n  key_finding: \"组合三个组件：(1) lightweight expert predictor选择high-importance neurons，(2) error compensation network修正sparsity误差，(3) layer-wise sparsity scheduler分配计算。50% FFN sparsity下达到1.45x prefill加速\"\n  relevance_to_us: \"与我们的方案最可比：都用predictor做activation sparsity。我们的差异在于用KL loss训练predictor而非BCE，且不需要额外的error compensation网络（KL loss本身应该能减少distribution shift）\"\n\n- title: \"Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models\"\n  authors: [Tai An, Ruwu Cai, Yanzhe Zhang, Yang Liu, Hao Chen, Pengcheng Xie, Sheng Chang, Yiwu Yao, Gongyi Wang]\n  venue: arXiv\n  year: 2025\n  arxiv_id: \"2508.02128\"\n  category: background\n  role: \"N:M structured activation sparsity——hardware-friendly的sparsity pattern\"\n  key_finding: \"Training-free的top-k策略在linear projection层内确定N:M activation masks，在2:4/4:8/8:16多种ratio下有效，可与W8A8量化组合\"\n  relevance_to_us: \"如果我们的predictor输出改为N:M structured pattern而非unstructured binary mask，可获得更好的hardware加速。值得作为future work\"\n\n# =============================================================================\n# Direction 4: Predictor-based activation sparsity (TEAL, DejaVu, PowerInfer等)\n# =============================================================================\n\n- title: \"Training-Free Activation Sparsity in Large Language Models\"\n  authors: [James Liu, Pragaash Ponnusamy, Tianle Cai, Han Guo, Yoon Kim, Ben Athiwaratkun]\n  venue: ICLR 2025 (Spotlight)\n  year: 2025\n  arxiv_id: \"2408.14690\"\n  category: direct-competitor\n  role: \"TEAL——我们的主要baseline，training-free magnitude pruning\"\n  key_finding: \"对所有hidden states施加magnitude-based sparsity（不需训练），在40-50% sparsity下性能降低很小，Llama-2/3和Mistral 7B-70B上验证。50% sparsity下1.8x decoding加速\"\n  relevance_to_us: \"TEAL用BCE度量sparsity mask质量（二元对错），我们的核心论点是：BCE只看neuron是否激活的对错，忽略了错误预测对output distribution的差异化影响。KL loss应该能让predictor学到'哪些neuron的错误预测对output影响更大'\"\n\n- title: \"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\"\n  authors: [Zichang Liu, Jue Wang, Tri Dao, Tianyi Zhou, Binhang Yuan, Zhao Song, Anshumali Shrivastava, Ce Zhang, Yuandong Tian, Christopher Re, Beidi Chen]\n  venue: ICML 2023\n  year: 2023\n  arxiv_id: \"2310.17157\"\n  category: direct-competitor\n  role: \"Predictor-based contextual sparsity的开创性工作——我们的直接对比对象\"\n  key_finding: \"用两层MLP predictor预测每层的contextual sparsity pattern（哪些attention heads和MLP neurons可跳过），在OPT-175B上实现2x加速。Predictor用BCE训练\"\n  relevance_to_us: \"DejaVu是predictor-based sparsity的baseline。其predictor用BCE训练——我们改用KL loss训练类似的predictor。关键差异：DejaVu在per-neuron level用BCE，我们在output distribution level用KL\"\n\n- title: \"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\"\n  authors: [Yash Akhauri, Ahmed F AbouElhamayed, Jordan Dotzel, Zhiru Zhang, Alexander M Rush, Safeen Huda, Mohamed S Abdelfattah]\n  venue: EMNLP 2024\n  year: 2024\n  arxiv_id: \"2406.16635\"\n  category: direct-competitor\n  role: \"DejaVu的改进——更好的predictor架构和sparsity pattern enforcement\"\n  key_finding: \"Shadow predictor超越magnitude-based pruning，context-dependent评估attention head和neuron重要性。比DejaVu端到端精度提升15%，速度提升20%\"\n  relevance_to_us: \"ShadowLLM改进了predictor架构但仍用BCE-style loss。我们的改进方向正交：不改predictor架构，改训练loss（BCE→KL）。两种改进可能互补\"\n\n- title: \"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference\"\n  authors: [Jiho Shin, Hoeseok Yang, Youngmin Yi]\n  venue: DATE 2025\n  year: 2025\n  arxiv_id: \"2411.12692\"\n  category: background\n  role: \"Training-free sign-bit predictor——极低开销的sparsity预测\"\n  key_finding: \"仅比较input和weight的sign bits预测activation sparsity，无需训练。仅适用于ReLU-based LLMs，不适用SwiGLU\"\n  relevance_to_us: \"不适用于SwiGLU模型（我们的目标），但其sign-bit方法的简洁性值得参考。SwiGLU缺乏天然sparsity证明trained predictor的必要性\"\n\n- title: \"SVD Contextual Sparsity Predictors for Fast LLM Inference\"\n  authors: [Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, C.C. Korikov]\n  venue: arXiv\n  year: 2026\n  arxiv_id: \"2603.14110\"\n  category: direct-competitor\n  role: \"Training-free SVD-based sparsity predictor——用gate projection矩阵的SVD做预测\"\n  key_finding: \"对ReGLU FFN的gate projection矩阵做truncation-aware SVD构建sparse pattern predictor，90% FFN sparsity下1.8x decoding加速，benchmark降低<1%\"\n  relevance_to_us: \"虽然是training-free competitor，但focus在ReGLU（不是SwiGLU）且需要90%天然稀疏性。我们的方法在SwiGLU的50%目标sparsity下工作，使用场景不同\"\n\n- title: \"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\"\n  authors: [Donghyun Lee, Je-Yong Lee, Genghan Zhang, Mo Tiwari, Azalia Mirhoseini]\n  venue: arXiv\n  year: 2024\n  arxiv_id: \"2404.08763\"\n  category: direct-competitor\n  role: \"Contextual thresholding——不训练predictor，用统计threshold做sparsity\"\n  key_finding: \"为每个MLP层计算SiLU(x)激活的percentile threshold做sparsification，50% sparsity下性能降低1-2%，无需fine-tuning。Mistral-7B和Llama2-7B上验证\"\n  relevance_to_us: \"CATS直接在SwiGLU/SiLU模型上工作，是我们的直接competitor。但CATS是固定threshold不考虑input context，我们的trained predictor是input-dependent的，理论上更优\"\n\n- title: \"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\"\n  authors: [Zhenyu Zhang, Zechun Liu, Yuandong Tian, Harshit Khaitan, Zhangyang Wang, Steven Li]\n  venue: ICLR 2025\n  year: 2025\n  arxiv_id: \"2504.19449\"\n  category: background\n  role: \"Training-free rank-aware方法——利用input channel sparsity和SVD\"\n  key_finding: \"用SVD分解将input channel sparsity映射到output，无需预测active channels。50% model-level sparsity下43%端到端加速\"\n  relevance_to_us: \"Training-free baseline。如果R-Sparse在SwiGLU模型上效果很好，我们需要证明trained KL predictor的额外训练成本是值得的\"\n\n- title: \"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\"\n  authors: [Marco Federici, Davide Belli, Mart van Baalen, Amir Jalalirad, Andrii Skliar, Bence Major, Markus Nagel, Paul Whatmough]\n  venue: MLSys 2025\n  year: 2024\n  arxiv_id: \"2412.01380\"\n  category: direct-competitor\n  role: \"Predictor-free dynamic pruning for SwiGLU——直接针对SwiGLU的magnitude pruning\"\n  key_finding: \"Predictor-free方案动态剪枝SwiGLU MLP层，配合LoRA adapter恢复精度。Phi-3-Medium上46%内存减少+40%吞吐提升\"\n  relevance_to_us: \"直接针对SwiGLU的competitor。DIP证明SwiGLU的sparsity pattern难以预测（所以放弃predictor），我们的KL-trained predictor需要证明能克服这个挑战\"\n\n# =============================================================================\n# 补充：Activation function替换和sparsity增强\n# =============================================================================\n\n- title: \"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\"\n  authors: [Iman Mirzadeh, Keivan Alizadeh, Sachin Mehta, Carlo C Del Mundo, Oncel Tuzel, Golnoosh Samei, Mohammad Rastegari, Mehrdad Farajtabar]\n  venue: ICLR 2024\n  year: 2024\n  arxiv_id: \"2310.04564\"\n  category: background\n  role: \"ReLU替换SiLU获得天然sparsity——替代路线\"\n  key_finding: \"用ReLU替换SiLU/GELU后continual pretraining，获得天然高稀疏性（>90%），推理计算减少3x\"\n  relevance_to_us: \"替代路线：修改activation function vs 训练predictor。我们的定位：不需要修改pretrained模型架构，作为plug-in predictor在现有SwiGLU模型上工作\"\n\n- title: \"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\"\n  authors: [Yixin Song, Haotong Xie, Zhengyan Zhang, Bo Wen, Li Ma, Zeyu Mi, Haibo Chen]\n  venue: arXiv\n  year: 2024\n  arxiv_id: \"2406.05955\"\n  category: background\n  role: \"dReLU获得90%+ sparsity——activation function工程的极致\"\n  key_finding: \"提出dReLU使LLM达到近90% sparsity同时保持SOTA性能，2-5x decoding加速\"\n  relevance_to_us: \"与ReLU Strikes Back同一思路但更极端。我们不改activation function，这是差异化定位\"\n\n- title: \"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\"\n  authors: [Chenyang Song, Xu Han, Zhengyan Zhang, Shengding Hu, Xiyu Shi, Kuai Li, Chen Chen, Zhiyuan Liu, Guangli Li, Tao Yang, Maosong Sun]\n  venue: COLING 2025\n  year: 2025\n  arxiv_id: \"2402.13516\"\n  category: background\n  role: \"Progressive sparsification——渐进式增加sparsity regularization\"\n  key_finding: \"三步法：ReLU替换→progressive sparsity regularization（沿sine curve增强）→threshold shifting(FATReLU)。LLaMA2-7B达89.32% sparsity\"\n  relevance_to_us: \"ProSparse的progressive training策略可参考：我们的KL predictor训练也可渐进式增加sparsity目标（已在Lagrangian约束中实现）\"\n\n- title: \"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\"\n  authors: [Yuqi Luo, Chenyang Song, Xu Han, Yingfa Chen, Chaojun Xiao, Xiaojun Meng, Liqun Deng, Jiansheng Wei, Zhiyuan Liu, Maosong Sun]\n  venue: arXiv\n  year: 2024\n  arxiv_id: \"2411.02335\"\n  category: background\n  role: \"Activation sparsity的scaling law——理论基础\"\n  key_finding: \"SiLU/SwiGLU的activation ratio随训练递增（变密），ReLU递减（变稀）。Sparsity对parameter scale不敏感，与width-depth ratio线性相关\"\n  relevance_to_us: \"理论支撑：SiLU/SwiGLU模型天然不够稀疏（随训练变密），因此需要外部predictor/pruning来获得稀疏性——这是我们工作的motivation之一\"\n\n- title: \"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering\"\n  authors: [Nobel Dhar, Bobin Deng, Md Romyull Islam, Xinyue Zhang, Kazi Fahim Ahmad Nasif, Kun Suo]\n  venue: Euro-Par 2025\n  year: 2025\n  arxiv_id: \"2507.14179\"\n  category: background\n  role: \"Clustering-based sparsity prediction——用聚类简化prediction\"\n  key_finding: \"将activation patterns聚类为representative clusters，预测cluster assignment而非individual neuron states，减少prediction开销。Mistral-7B上79.34%聚类精度\"\n  relevance_to_us: \"降低predictor复杂度的思路。如果我们的per-neuron KL predictor开销太大，可考虑cluster-level prediction\"\n\n# =============================================================================\n# 竞争格局总结\n# =============================================================================\n#\n# 我们的独特定位:\n# 1. 唯一使用KL divergence训练activation sparsity predictor的工作\n#    - DejaVu/ShadowLLM用BCE训练predictor\n#    - SPON用KL但训练bias correction而非predictor\n#    - TEAL/CATS/R-Sparse/SparseInfer/SVD-CSP是training-free\n# 2. 专注SwiGLU模型的50% sparsity目标\n#    - ReLU/dReLU方案需要替换activation function\n#    - 很多training-free方案在SwiGLU上效果不佳(DIP论文证实)\n# 3. 通过保留output distribution(而非逐neuron匹配)来指导sparsity\n#    - Minitron/SPON已证明KL loss优于MSE/BCE做distribution matching\n#    - 我们将此insight应用到predictor训练\n#\n# 主要related work定位:\n# - vs TEAL: trained predictor(input-dependent) vs fixed magnitude threshold\n# - vs DejaVu/ShadowLLM: KL loss vs BCE loss训练predictor\n# - vs SPON: predictor vs learnable bias; 都用KL但目标不同\n# - vs DIP: trained predictor vs predictor-free pruning\n# - vs ReLU/TurboSparse/ProSparse: 不改activation function\n# - vs Fast Forward: KL loss vs BCE+error compensation\n# - vs CATS: input-dependent predictor vs fixed percentile threshold\n",
    "structuredPatch": [
      {
        "oldStart": 215,
        "oldLines": 6,
        "newStart": 215,
        "newLines": 26,
        "lines": [
          "   key_finding: \"将activation patterns聚类为representative clusters，预测cluster assignment而非individual neuron states，减少prediction开销。Mistral-7B上79.34%聚类精度\"",
          "   relevance_to_us: \"降低predictor复杂度的思路。如果我们的per-neuron KL predictor开销太大，可考虑cluster-level prediction\"",
          " ",
          "+- title: \"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU\"",
          "+  authors: [Yixin Song, Zeyu Mi, Haotong Xie, Haibo Chen]",
          "+  venue: SOSP 2024",
          "+  year: 2024",
          "+  arxiv_id: \"2312.12456\"",
          "+  category: background",
          "+  role: \"GPU-CPU混合推理利用activation sparsity的开创性系统工作——建立neuron activation power-law分布\"",
          "+  key_finding: \"利用LLM neuron activation的power-law分布（少量hot neurons跨input始终激活，大量cold neurons input-dependent），将hot neurons预加载至GPU、cold neurons在CPU计算，配合adaptive sparsity predictor，单RTX 4090上比llama.cpp快11.69x\"",
          "+  relevance_to_us: \"PowerInfer的核心假设（neuron activation有power-law locality）直接支持我们predictor的设计：hot neurons无需预测（始终激活），predictor重点预测cold neurons的contextual activation。其adaptive predictor用较小网络预测高稀疏层的思路可参考\"",
          "+",
          "+- title: \"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity\"",
          "+  authors: [Susav Shrestha, Brad Settlemyer, Nikoli Dryden, Narasimha Reddy]",
          "+  venue: NeurIPS 2025",
          "+  year: 2025",
          "+  arxiv_id: \"2505.14884\"",
          "+  category: background",
          "+  role: \"揭示MLP contextual sparsity在batch场景下不可扩展——attention head sparsity更稳定\"",
          "+  key_finding: \"首次揭示MLP contextual sparsity的扩展性瓶颈：随batch size增加，batch内不同token的active neuron取并集趋近dense计算，MLP sparsity增益消失。相反attention head sparsity是batch-invariant的。提出Selective Head Attention实现2.2x加速\"",
          "+  relevance_to_us: \"对我们工作的重要约束和定位信息：MLP neuron-level contextual sparsity（我们的方法）主要适用于decoding（batch=1）场景。在大batch prefill中需要不同策略。论文中应明确讨论这一适用范围\"",
          "+",
          " # =============================================================================",
          " # 竞争格局总结",
          " # ============================================================================="
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

已追加 2 篇论文到 literature_map.yaml：

1. **PowerInfer** (SOSP 2024, 2312.12456) — GPU-CPU 混合推理利用 activation sparsity 的开创工作。建立 neuron activation power-law 分布假设，adaptive predictor 为高稀疏层构建更小预测网络。
2. **Polar Sparsity** (NeurIPS 2025, 2505.14884) — 揭示 MLP contextual sparsity 在 batch 场景下的扩展性瓶颈（active neuron 并集趋近 dense），attention head sparsity 是 batch-invariant 的。对我们工作的适用范围定位有直接意义。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "uuid": "e36160c1-645f-4d15-851e-72e554ecdcba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VDqjW5caXT41yEnkXpJAXk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3036,
      "cache_read_input_tokens": 39927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3036
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

已追加 2 篇论文到 literature_map.yaml：

1. **PowerInfer** (SOSP 2024, 2312.12456) — GPU-CPU 混合推理利用 activation sparsity 的开创工作。建立 neuron activation power-law 分布假设，adaptive predictor 为高稀疏层构建更小预测网络。
2. **Polar Sparsity** (NeurIPS 2025, 2505.14884) — 揭示 MLP contextual sparsity 在 batch 场景下的扩展性瓶颈（active neuron 并集趋近 dense），attention head sparsity 是 batch-invariant 的。对我们工作的适用范围定位有直接意义。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 131387,
  "duration_api_ms": 163043,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "b325a5d3-04ce-492e-afa9-91ad76803d9d",
  "total_cost_usd": 0.6799545,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 31122,
    "cache_read_input_tokens": 215220,
    "output_tokens": 4636,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 31122,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 206,
        "cache_read_input_tokens": 39927,
        "cache_creation_input_tokens": 3036,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3036
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 159857,
      "outputTokens": 4405,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 8,
      "costUSD": 0.261882,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 4636,
      "cacheReadInputTokens": 215220,
      "cacheCreationInputTokens": 31122,
      "webSearchRequests": 0,
      "costUSD": 0.4180725,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e5d142da-d6a0-40ec-a5d7-10a73d37bf32"
}
```

</details>

---
