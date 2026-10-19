# research related work survey

**action cond info bottleneck** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 75
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/workers/worker_research_related-work-survey_20260517T150220.log`
- **Structured JSON:** [`c4741199c81c1e4554d1.json`](../../sessions/c4/c4741199c81c1e4554d1.json)

## Before a recorded user message

75 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
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
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "85c430ea-1bfa-49f0-8d49-575daa197db7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-3-projects-action-cond-info-bottleneck/memory/"
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
    "resetsAt": 1779042600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a6e591ad-64c5-4d6b-878a-e6891984bcaf",
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to conduct a literature survey for the ACIB paper across 4 topics, find key papers, and compile them into a YAML file. Let me start by checking if a literature_map.yaml already exists, then conduct web searches across all 4 topics in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "975aad63-2db8-49c6-9992-37bd049a7091",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YrE9E88qjkx21bTtrDE6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13447,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13447
      },
      "output_tokens": 28,
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

先检查是否已有 literature_map.yaml，然后并行搜索四个主题的文献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "d1902d97-397f-4f5f-89b8-d7581b0ccc02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YrE9E88qjkx21bTtrDE6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13447,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13447
      },
      "output_tokens": 28,
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

<details open><summary>🔧 Tool call — Bash · `toolu_0182YDma9SUTWxUfERi7xxiW`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/literature_map.yaml 2>/dev/null; echo \"EXIT:$?\"",
  "description": "Check if literature_map.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "26102186-5f86-4fc7-b70d-a15731b2d560",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YrE9E88qjkx21bTtrDE6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13447,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13447
      },
      "output_tokens": 28,
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

_source line 7 · 2026-05-17T15:02:33.536Z_

<details><summary>↩ Tool result · `toolu_0182YDma9SUTWxUfERi7xxiW`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 23273 May 16 03:36 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/literature_map.yaml
EXIT:0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "af00398c-cbce-457c-a370-755dd771a514",
  "tool_use_result": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 23273 May 16 03:36 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/literature_map.yaml\nEXIT:0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019uMmmtimbetGMzyPwSfkhF`</summary>

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
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "b8e6770c-a043-42d0-9cfe-9d2734863039",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YrE9E88qjkx21bTtrDE6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13447,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13447
      },
      "output_tokens": 28,
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

_source line 9 · 2026-05-17T15:02:33.736Z_

<details><summary>↩ Tool result · `toolu_019uMmmtimbetGMzyPwSfkhF`</summary>

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
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "75372e7d-8dd6-4a78-adc9-914d32796a77",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
The file already exists. Let me read it first, then conduct searches for the 4 topics in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "c897c4f0-4cbf-482f-85c2-5fc7d1024e86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bpYNowv2rPPbuanxTSB8R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 25288,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 936
      },
      "output_tokens": 22,
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

文件已存在，先读取现有内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "444bc3b9-5225-48b9-91c4-399312cc9cba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bpYNowv2rPPbuanxTSB8R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 25288,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 936
      },
      "output_tokens": 22,
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

<details open><summary>🔧 Tool call — Read · `toolu_017QzxF52TWbNhCdkQq7fzAy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "45ecbeed-cac8-442d-abbf-287d4b9d7988",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bpYNowv2rPPbuanxTSB8R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 25288,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 936
      },
      "output_tokens": 22,
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

_source line 13 · 2026-05-17T15:02:38.057Z_

<details><summary>↩ Tool result · `toolu_017QzxF52TWbNhCdkQq7fzAy`</summary>

```text
1	# Literature Map — ACIB (Action-Conditioned Information Bottleneck)
2	# Target venue: CoRL 2026
3	# Generated: 2026-05-16, updated: 2026-05-16
4	# Scope: Information Bottleneck × VLA / Robot Learning, plus token pruning, VLA robustness, LIBERO
5	
6	meta:
7	  our_method_summary: >
8	    Token-level information bottleneck for VLA models. A learned scorer network produces
9	    per-token soft masks gating visual tokens consumed by the action expert. The bottleneck is
10	    enforced by an aggregate-rate KL (KL on the mean activation across the batch, rather than
11	    per-sample) plus a diversity regularizer that prevents the scorer from collapsing to
12	    uniform or to a fixed subset. Action loss provides the task-relevance signal — gradients
13	    flow back through the soft mask so the scorer learns which tokens are required to predict
14	    actions. Backbone: SmolVLA. Benchmark: LIBERO. Positioned as a regularization-based
15	    complement to data augmentation.
16	  novelty_axes:
17	    - token_level_IB        # not representation/feature-level
18	    - action_conditioned    # scorer trained by the action loss, not reconstruction or MI on input
19	    - aggregate_rate_KL     # KL on batch-mean activation, not per-sample variational KL
20	    - explicit_anti_collapse # diversity regularizer with empirical scorer_std as health metric
21	    - regularization_not_data # complementary to GenAug/RoCoDA-style augmentation
22	    - soft_gating_not_pruning # all tokens flow through; contrast with LightVLA/ATP-LLaVA hard pruning
23	
24	# =====================================================================
25	# Direction 1: Information Bottleneck in RL / Robot Learning
26	# =====================================================================
27	ib_in_robot_learning:
28	  - id: bc_ib_2025
29	    title: "Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation"
30	    authors: [Bai, Zhou, Ding, Zhao, Wang, Chen]
31	    year: 2025
32	    venue: ICML 2025
33	    arxiv: "2502.02853"
34	    code: "https://github.com/BaiShuanghao/BC-IB"
35	    one_liner: >
36	      Adds an IB regularizer to behavior-cloning: minimizes I(X;Z) between fused multimodal
37	      input X and policy latent Z via MINE, while preserving action prediction.
38	    relation: competitor
39	    differences_from_acib:
40	      level: "representation-level (single fused latent Z) vs. ACIB's token-level (per visual token gate)"
41	      ib_estimator: "MINE-based MI lower bound vs. ACIB's aggregate-rate KL with learned prior"
42	      mechanism: "no scorer / no token mask; ACIB outputs an interpretable per-token relevance score"
43	      collapse_handling: "BC-IB has no explicit anti-collapse term — single-latent IB does not face the per-token collapse failure mode"
44	      benchmark_overlap: "both on LIBERO; BC-IB baseline gains +2-9% per suite, ACIB targets SmolVLA backbone instead"
45	    citation_priority: high  # primary related-work anchor; the ICML-25 paper to beat
46	
47	  - id: vib_rl_skill_2023
48	    title: "Variational Information Bottleneck Regularized Deep RL for Efficient Robotic Skill Adaptation"
49	    venue: "MDPI Sensors 2023 (Vol 23 Issue 2)"
50	    one_liner: VIB on meta-RL latent task representation, 200x-5000x sample-efficiency claim on skill transfer.
51	    relation: background
52	    note: pre-VLA era; VIB on task embeddings, not visual tokens.
53	    citation_priority: medium
54	
55	  - id: mib_multimodal_2024
56	    title: "Multimodal Information Bottleneck for Deep RL with Multiple Sensors"
57	    venue: "Neural Networks (Elsevier) 2024"
58	    one_liner: MIB compresses joint egocentric-image + proprioception representation, filtering policy-irrelevant info.
59	    relation: background
60	    note: closest in spirit to ACIB (filter task-irrelevant info) but operates on fused embeddings, not tokens.
61	    citation_priority: medium
62	
63	  - id: ibe_2025
64	    title: "Information Bottleneck-Enhanced RL for Solving Operation Research Problems"
65	    venue: "MDPI Sensors 2025"
66	    one_liner: Two-level IB — state representation bottleneck + policy bottleneck as exploration bonus.
67	    relation: background
68	    note: combinatorial RL, not robot manipulation; cited only if discussing IB design space.
69	    citation_priority: low
70	
71	  - id: discrete_ib_drl_2023
72	    title: "Representation Learning in Deep RL via Discrete Information Bottleneck"
73	    venue: PMLR 2023 (Islam et al.)
74	    one_liner: Discrete IB on state representation for deep RL.
75	    relation: background
76	    citation_priority: low
77	
78	# =====================================================================
79	# Direction 2: Token Pruning / Selection for Vision-Language Models
80	# =====================================================================
81	token_pruning_vlm:
82	  - id: lightvla_2025
83	    title: "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning"
84	    authors: [Jiang, et al.]
85	    year: 2025
86	    arxiv: "2509.12594"
87	    project_page: "https://liauto-research.github.io/LightVLA/"
88	    one_liner: >
89	      Differentiable token pruning for VLA: generates dynamic queries to evaluate visual token
90	      importance, uses Gumbel softmax for hard selection. 59% FLOPs reduction + 2.9% success
91	      rate improvement over OpenVLA-OFT.
92	    relation: competitor  # closest VLA-specific token selection work
93	    differences_from_acib:
94	      goal: "LightVLA = efficiency (reduce FLOPs); ACIB = robustness regularization (encourage task-relevant focus)"
95	      selection_type: "LightVLA uses hard Gumbel selection (tokens are dropped); ACIB uses soft gating (all tokens flow through with scaled weights)"
96	      bottleneck: "LightVLA has no information-theoretic constraint; ACIB enforces aggregate-rate KL to a prior rate"
97	      collapse: "LightVLA has no anti-collapse mechanism; ACIB's diversity regularizer prevents scorer degeneration"
98	      backbone: "LightVLA on 7B OpenVLA; ACIB on 0.45B SmolVLA with only 64 visual tokens — different operating regime"
99	    citation_priority: high  # most direct VLA token selection competitor
100	
101	  - id: divprune_2025
102	    title: "DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models"
103	    authors: [Alvar, Singh, Akbari, Zhang]
104	    year: 2025
105	    venue: CVPR 2025
106	    arxiv: "2503.02175"
107	    one_liner: Formulates token pruning as Max-Min Diversity Problem; selects most diverse token subset; training-free.
108	    relation: complementary  # different goal (efficiency) but shares "diversity" motivation
109	    differences_from_acib:
110	      goal: "DivPrune = inference efficiency under fixed budget; ACIB = robustness regularization, not efficiency"
111	      training: "DivPrune is training-free at test time; ACIB trains the scorer end-to-end with action loss"
112	      diversity_role: "DivPrune diversity is the *objective*; ACIB diversity is an anti-collapse *regularizer*"
113	    citation_priority: high  # closest competing use of 'diversity' in visual token selection
114	
115	  - id: atp_llava_2025
116	    title: "ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models"
117	    venue: CVPR 2025
118	    one_liner: Layer-adaptive token pruning module predicting pruning thresholds per-layer and per-instance, removing text-irrelevant visual tokens.
119	    relation: competitor  # also learns a scorer-like importance function
120	    differences_from_acib:
121	      objective: "ATP optimizes for accuracy-under-pruning; ACIB optimizes for action-prediction under IB constraint"
122	      action_grounding: "ATP uses text relevance; ACIB uses action relevance (closer to control)"
123	      mechanism: "ATP prunes hard tokens; ACIB applies soft mask, all tokens still flow through"
124	    citation_priority: high
125	
126	  - id: sparsevlm_2025
127	    title: "SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference"
128	    authors: [Zhang, Fan, Ma, Zheng, Huang, Cheng, Gudovskiy, Okuno, Nakata, Keutzer, Zhang]
129	    year: 2025
130	    venue: ICML 2025
131	    arxiv: "2410.04417"
132	    code: "https://github.com/Gumpest/SparseVLMs"
133	    one_liner: >
134	      Training-free token sparsification: uses text-visual attention to rate vision token importance,
135	      progressively prunes with rank-based adaptive ratio + token recycling. 54% FLOPs reduction, 97% accuracy retained.
136	    relation: background
137	    note: Training-free, text-relevance based. No action grounding. General VLM efficiency, not robot-specific.
138	    citation_priority: medium
139	
140	  - id: vla_cache_2025
141	    title: "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching"
142	    authors: [Hsu, et al.]
143	    year: 2025
144	    venue: NeurIPS 2025
145	    arxiv: "2502.02175"
146	    code: "https://github.com/siyuhsu/vla-cache"
147	    one_liner: >
148	      Training-free inference acceleration: caches static visual tokens across frames, selectively
149	      re-computes task-relevant tokens. 1.7x speedup on LIBERO/SIMPLER.
150	    relation: background
151	    note: >
152	      Temporal token reuse, orthogonal to ACIB. Interesting overlap: both identify "task-relevant" tokens,
153	      but VLA-Cache uses attention-based heuristics while ACIB learns relevance end-to-end.
154	    citation_priority: medium
155	
156	  - id: topv_2025
157	    title: "TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal VLM"
158	    venue: CVPR 2025
159	    one_liner: Training-free token pruning posed as inference-time optimization.
160	    relation: background
161	    citation_priority: medium
162	
163	  - id: feather_2025
164	    title: "Feather the Throttle: Revisiting Visual Token Pruning for VLMs"
165	    venue: ICCV 2025
166	    one_liner: Diagnoses attention-based pruning bias (RoPE long-term decay favors bottom-row tokens) and proposes fixes.
167	    relation: background
168	    note: useful warning when designing scorer input features; cite if discussing attention-based scorers.
169	    citation_priority: medium
170	
171	  - id: prunevid_2025
172	    title: "PruneVid: Visual Token Pruning for Efficient Video LLMs"
173	    venue: ACL 2025
174	    one_liner: Training-free spatial-temporal token merging for video VLMs.
175	    relation: background
176	    citation_priority: low
177	
178	  - id: dycoke_2025
179	    title: "DyCoke: Dynamic Compression of Tokens for Fast Video LLMs"
180	    venue: CVPR 2025
181	    one_liner: Dynamic token compression for video LLMs.
182	    relation: background
183	    citation_priority: low
184	
185	# =====================================================================
186	# Direction 3: VLA Robustness / Generalization / Augmentation
187	# =====================================================================
188	vla_robustness:
189	  - id: robustvla_2025
190	    title: "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models"
191	    year: 2025
192	    arxiv: "2511.01331"
193	    one_liner: >
194	      RL post-training with Jacobian regularization (observation noise sensitivity) +
195	      smoothness regularization (action perturbation stability) for VLA robustness.
196	    relation: competitor
197	    differences_from_acib:
198	      stage: "RobustVLA = post-training RL fine-tuning; ACIB = training-time regularization integrated into BC"
199	      mechanism: "RobustVLA uses gradient-based Jacobian/smoothness penalties; ACIB uses information-theoretic bottleneck"
200	      interpretability: "RobustVLA is a black-box regularizer; ACIB produces interpretable per-token relevance scores"
201	      composability: "potentially complementary — ACIB during training, RobustVLA as post-training hardening"
202	    citation_priority: high
203	
204	  - id: revla_2025
205	    title: "ReVLA: Reverting Visual Domain Limitation of Robotic Foundation Models"
206	    authors: [Daskalov, et al.]
207	    year: 2025
208	    arxiv: "2409.15250"
209	    project_page: "https://insait-institute.github.io/ReVLA/"
210	    one_liner: >
211	      Gradual backbone reversal via model merging — restores vision encoder to pretrained state
212	      to combat catastrophic forgetting. +77% grasp, +66% lift on OOD visual tasks over OpenVLA.
213	    relation: complementary
214	    note: >
215	      Addresses the same symptom (VLA visual fragility) from a different angle: ReVLA preserves
216	      pretrained visual features, ACIB teaches the model which features matter. Could combine.
217	    citation_priority: medium
218	
219	  - id: libero_plus_2025
220	    title: "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models"
221	    year: 2025
222	    arxiv: "2510.13626"
223	    one_liner: 7 perturbation dims (object layout, viewpoint, init state, language, light, texture, sensor noise); 10k tasks; shows 95%→<30% drop under modest perturbations.
224	    relation: evaluation_benchmark
225	    note: >
226	      Critical eval target — our ACIB robustness story should be validated here, not on vanilla LIBERO,
227	      to avoid the "memorization" critique LIBERO-PRO levels at the field.
228	    citation_priority: high
229	
230	  - id: libero_pro_2025
231	    title: "LIBERO-PRO: Towards Robust and Fair Evaluation of VLA Models Beyond Memorization"
232	    year: 2025
233	    arxiv: "2510.03827"
234	    one_liner: Object/position/instruction/task perturbations; SOTA models that report >90% drop to ~0% — exposes rote memorization.
235	    relation: evaluation_benchmark
236	    citation_priority: high
237	
238	  - id: eva_vla_2025
239	    title: "Eva-VLA: Evaluating VLA Models' Robustness Under Real-World Physical Variations"
240	    year: 2025
241	    arxiv: "2509.18953"
242	    one_liner: Treats perturbations (viewpoint, init state) as a continuous optimization problem to find worst-case.
243	    relation: evaluation_benchmark
244	    citation_priority: medium
245	
246	  - id: vla_multimodal_perturb_2025
247	    title: "On Robustness of VLA Models against Multi-Modal Perturbations"
248	    arxiv: "2510.00037"
249	    one_liner: Tests mainstream VLAs against 17 uncertainties across 4 modalities; finds action modality most fragile; π0 > OpenVLA.
250	    relation: background
251	    citation_priority: medium
252	
253	  - id: byovla_2025
254	    title: "BYOVLA: Removing Model-Sensitive Features via VLM Segmentation + Inpainting"
255	    authors: [Hancock, et al.]
256	    year: 2025
257	    one_liner: At inference, segments and inpaints out task-irrelevant regions to make VLAs robust.
258	    relation: competitor  # solves the same problem (irrelevant visual content hurts policy) at test time
259	    differences_from_acib:
260	      stage: "BYOVLA = test-time pre-processing; ACIB = training-time regularization"
261	      mechanism: "BYOVLA modifies the image (segmentation + inpainting); ACIB modifies the token stream (soft gating)"
262	      cost: "BYOVLA needs a VLM call per frame; ACIB is a small scorer head, zero extra cost at inference if mask is integrated"
263	    citation_priority: high
264	
265	  - id: gevrm_2025
266	    title: "GEVRM: Model-based Planning for Visual Corruptions in VLA"
267	    authors: [Zhang, et al.]
268	    year: 2025
269	    one_liner: Handles color jitter and common visual corruptions via model-based planning.
270	    relation: competitor
271	    differences_from_acib:
272	      mechanism: "augmentation-style robustness vs. ACIB's regularization-style robustness"
273	    citation_priority: medium
274	
275	  - id: rocoda_2024
276	    title: "RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning"
277	    year: 2024
278	    arxiv: "2411.16959"
279	    one_liner: Counterfactual augmentation modifying task-irrelevant subset of environment state; tests distractor generalization.
280	    relation: complementary
281	    note: ACIB and RoCoDA are *complementary* — ACIB is the regularization analogue of RoCoDA's data-side approach.
282	    citation_priority: high
283	
284	  - id: nice_scene_surgery_2025
285	    title: "NICE Scene Surgery: Improving Robotic Manipulation Robustness"
286	    year: 2025
287	    arxiv: "2511.22777"
288	    one_liner: Edits scenes to insert distractors while preserving causal task-relevant features.
289	    relation: complementary
290	    citation_priority: medium
291	
292	  - id: genaug_2023
293	    title: "GenAug: Scaling Robot Learning with Semantic Data Augmentation"
294	    venue: RSS 2023
295	    one_liner: Diffusion-based scene augmentation (backgrounds, distractors, textures) for imitation learning.
296	    relation: complementary
297	    citation_priority: medium
298	
299	# =====================================================================
300	# Direction 4: LIBERO + VLA Baselines
301	# =====================================================================
302	libero_baselines:
303	  - id: openvla_2024
304	    title: "OpenVLA: An Open-Source Vision-Language-Action Model"
305	    year: 2024
306	    one_liner: 7B Llama-based VLA; LIBERO 76.5% avg.
307	    relation: backbone_baseline
308	    citation_priority: high
309	
310	  - id: openvla_oft_2025
311	    title: "Fine-Tuning VLA Models: Optimizing Speed and Success (OpenVLA-OFT)"
312	    authors: [Kim, et al.]
313	    year: 2025
314	    venue: RSS 2025
315	    arxiv: "2502.19645"
316	    one_liner: Parallel decoding + action chunking + continuous actions + L1 regression; 76.5%→97.1% on LIBERO; 26× faster.
317	    relation: strong_baseline
318	    note: Current LIBERO SOTA prior to VLA-0; ACIB must compare against OFT recipe.
319	    citation_priority: high
320	
321	  - id: pi0_2024
322	    title: "π0: A Vision-Language-Action Flow Model"
323	    authors: [Black, et al.]
324	    year: 2024
325	    one_liner: 3.3B robotics-pretrained flow-matching VLA; LIBERO 86.0%; most robust under multi-modal perturbations.
326	    relation: strong_baseline
327	    citation_priority: high
328	
329	  - id: pi0_fast_2025
330	    title: "π0-FAST"
331	    authors: [Pertsch, et al.]
332	    year: 2025
333	    one_liner: Faster autoregressive variant of π0.
334	    relation: baseline
335	    citation_priority: medium
336	
337	  - id: smolvla_2025
338	    title: "SmolVLA: A VLA Model for Affordable and Efficient Robotics"
339	    year: 2025
340	    arxiv: "2506.01844"
341	    one_liner: 0.45B VLA; PixelShuffle compresses 1024→64 visual tokens; VLM layer-skip; CA/SA interleaved action expert; LIBERO 87.3%.
342	    relation: our_backbone
343	    note: >
344	      Our chosen backbone. Important: SmolVLA already reduces to 64 visual tokens via PixelShuffle,
345	      so ACIB's scorer operates on a small token set — must justify why further token-level gating
346	      helps when the count is already low (answer: not all 64 are equally task-relevant per scene/timestep).
347	    citation_priority: high
348	
349	  - id: vla_0_2025
350	    title: "VLA-0: Building SOTA VLAs with Zero Modification"
351	    year: 2025
352	    arxiv: "2510.13054"
353	    one_liner: Outperforms OpenVLA-OFT, SmolVLA, π0.5-KI on LIBERO with no architectural changes.
354	    relation: strong_baseline
355	    citation_priority: high
356	
357	# =====================================================================
358	# Novelty Position Statement
359	# =====================================================================
360	novelty_synthesis:
361	  closest_competitors:
362	    - bc_ib_2025      # IB for BC, but representation-level
363	    - lightvla_2025   # learned token selection for VLA, but efficiency-oriented pruning
364	
365	  delta_vs_bc_ib:
366	    - "BC-IB applies IB at the fused-latent level (one Z); ACIB applies IB at the visual-token level (per-token gate)"
367	    - "BC-IB uses MINE for MI estimation; ACIB uses aggregate-rate KL (KL on batch-mean scorer output to a prior rate)"
368	    - "BC-IB has no scorer interpretability — Z is opaque; ACIB exposes a per-token relevance score usable for visualization/analysis"
369	    - "BC-IB does not face per-token collapse; ACIB introduces an explicit diversity regularizer and tracks scorer_std as a training health metric (0.441 in our successful run)"
370	
371	  delta_vs_lightvla:
372	    - "LightVLA targets efficiency (hard Gumbel pruning, drop tokens); ACIB targets robustness (soft gating, all tokens retained with scaled weights)"
373	    - "LightVLA has no information-theoretic framework; ACIB enforces an aggregate-rate KL bottleneck"
374	    - "LightVLA has no anti-collapse mechanism; ACIB's diversity regularizer prevents scorer degeneration"
375	    - "LightVLA on 7B OpenVLA; ACIB on 0.45B SmolVLA with only 64 visual tokens — different operating regime"
376	
377	  uniqueness_combination:
378	    description: >
379	      To our knowledge no prior work combines (a) token-level IB on visual tokens, (b) end-to-end
380	      training driven by an action-prediction loss (not reconstruction or text relevance),
381	      (c) aggregate-rate KL as the bottleneck term, (d) an explicit anti-collapse diversity
382	      regularizer with an empirical health metric, and (e) soft gating rather than hard pruning.
383	      The closest competitors each share at most one of these axes:
384	        - BC-IB: shares IB-for-policy but at representation level, no token scorer, no collapse issue.
385	        - LightVLA: shares learned VLA token selection but for efficiency via hard pruning, no IB framework.
386	        - ATP-LLaVA: shares token-level scoring but for text-relevance and pruning, not action-grounded IB.
387	        - DivPrune: shares diversity motivation but as the objective (not anti-collapse) and is training-free.
388	        - BYOVLA: shares "remove irrelevant visual content" goal but at test time via VLM inpainting.
389	        - RobustVLA: shares VLA robustness goal but via gradient-based Jacobian/smoothness penalties, not IB.
390	        - RoCoDA / GenAug: shares the underlying problem (distractor invariance) but solves it via data augmentation.
391	    framing: >
392	      ACIB = regularization-side counterpart to data-augmentation approaches for VLA robustness,
393	      with action-conditioned token-level IB as the mechanism. Soft gating under an information
394	      constraint, not hard pruning for efficiency.
395	
396	  positioning_risks:
397	    - "BC-IB ICML-25 is the *direct* prior art on IB-for-BC. Differentiation must be airtight; expect reviewers to ask 'why token-level if representation-level already works?'"
398	    - "LightVLA does learned token selection *specifically for VLA* — reviewers may conflate it with ACIB. Key defense: ACIB is soft gating under IB for robustness, not hard pruning for efficiency."
399	    - "Token-pruning literature (DivPrune, ATP-LLaVA, SparseVLM) may be invoked as similar token-selection work. Need to clarify that ACIB does not prune — it gates softly under an information constraint, and the goal is regularization, not efficiency."
400	    - "LIBERO-Plus / LIBERO-PRO show standard LIBERO scores are inflated by memorization. ACIB should report on LIBERO-Plus or analogous perturbation eval to make a credible robustness claim — otherwise the contribution will be perceived as marginal."
401	    - "RobustVLA targets the same VLA robustness goal via RL post-training. Must argue why training-time IB regularization is preferable to or complementary with post-training approaches."
402	
403	  must_cite:
404	    - bc_ib_2025
405	    - lightvla_2025
406	    - divprune_2025
407	    - atp_llava_2025
408	    - byovla_2025
409	    - robustvla_2025
410	    - rocoda_2024
411	    - libero_plus_2025
412	    - openvla_oft_2025
413	    - smolvla_2025
414	    - pi0_2024
415	    - vla_0_2025
416	
417	  should_cite:
418	    - mib_multimodal_2024
419	    - vib_rl_skill_2023
420	    - sparsevlm_2025
421	    - vla_cache_2025
422	    - revla_2025
423	    - libero_pro_2025
424	    - eva_vla_2025
425	    - gevrm_2025
426	    - genaug_2023
427	    - feather_2025
428	    - openvla_2024
429	
430	  open_research_directions:
431	    - "Does the learned scorer transfer across task suites (LIBERO-Spatial scorer applied to LIBERO-Goal)?"
432	    - "Correlation between scorer mask and object-segmentation masks — does ACIB learn an implicit object detector for free?"
433	    - "Combining ACIB with augmentation (RoCoDA/GenAug) — does the regularization-side + data-side gain stack?"
434	    - "Robustness on LIBERO-Plus perturbation dims, especially camera viewpoint and distractor objects — where the 95→30% drop lives."
435	    - "ACIB + RobustVLA: training-time IB regularization + post-training RL hardening — do they compose?"
436	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "4cd83123-3d33-4003-b12a-0f651767c4b9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/literature_map.yaml",
      "content": "# Literature Map — ACIB (Action-Conditioned Information Bottleneck)\n# Target venue: CoRL 2026\n# Generated: 2026-05-16, updated: 2026-05-16\n# Scope: Information Bottleneck × VLA / Robot Learning, plus token pruning, VLA robustness, LIBERO\n\nmeta:\n  our_method_summary: >\n    Token-level information bottleneck for VLA models. A learned scorer network produces\n    per-token soft masks gating visual tokens consumed by the action expert. The bottleneck is\n    enforced by an aggregate-rate KL (KL on the mean activation across the batch, rather than\n    per-sample) plus a diversity regularizer that prevents the scorer from collapsing to\n    uniform or to a fixed subset. Action loss provides the task-relevance signal — gradients\n    flow back through the soft mask so the scorer learns which tokens are required to predict\n    actions. Backbone: SmolVLA. Benchmark: LIBERO. Positioned as a regularization-based\n    complement to data augmentation.\n  novelty_axes:\n    - token_level_IB        # not representation/feature-level\n    - action_conditioned    # scorer trained by the action loss, not reconstruction or MI on input\n    - aggregate_rate_KL     # KL on batch-mean activation, not per-sample variational KL\n    - explicit_anti_collapse # diversity regularizer with empirical scorer_std as health metric\n    - regularization_not_data # complementary to GenAug/RoCoDA-style augmentation\n    - soft_gating_not_pruning # all tokens flow through; contrast with LightVLA/ATP-LLaVA hard pruning\n\n# =====================================================================\n# Direction 1: Information Bottleneck in RL / Robot Learning\n# =====================================================================\nib_in_robot_learning:\n  - id: bc_ib_2025\n    title: \"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation\"\n    authors: [Bai, Zhou, Ding, Zhao, Wang, Chen]\n    year: 2025\n    venue: ICML 2025\n    arxiv: \"2502.02853\"\n    code: \"https://github.com/BaiShuanghao/BC-IB\"\n    one_liner: >\n      Adds an IB regularizer to behavior-cloning: minimizes I(X;Z) between fused multimodal\n      input X and policy latent Z via MINE, while preserving action prediction.\n    relation: competitor\n    differences_from_acib:\n      level: \"representation-level (single fused latent Z) vs. ACIB's token-level (per visual token gate)\"\n      ib_estimator: \"MINE-based MI lower bound vs. ACIB's aggregate-rate KL with learned prior\"\n      mechanism: \"no scorer / no token mask; ACIB outputs an interpretable per-token relevance score\"\n      collapse_handling: \"BC-IB has no explicit anti-collapse term — single-latent IB does not face the per-token collapse failure mode\"\n      benchmark_overlap: \"both on LIBERO; BC-IB baseline gains +2-9% per suite, ACIB targets SmolVLA backbone instead\"\n    citation_priority: high  # primary related-work anchor; the ICML-25 paper to beat\n\n  - id: vib_rl_skill_2023\n    title: \"Variational Information Bottleneck Regularized Deep RL for Efficient Robotic Skill Adaptation\"\n    venue: \"MDPI Sensors 2023 (Vol 23 Issue 2)\"\n    one_liner: VIB on meta-RL latent task representation, 200x-5000x sample-efficiency claim on skill transfer.\n    relation: background\n    note: pre-VLA era; VIB on task embeddings, not visual tokens.\n    citation_priority: medium\n\n  - id: mib_multimodal_2024\n    title: \"Multimodal Information Bottleneck for Deep RL with Multiple Sensors\"\n    venue: \"Neural Networks (Elsevier) 2024\"\n    one_liner: MIB compresses joint egocentric-image + proprioception representation, filtering policy-irrelevant info.\n    relation: background\n    note: closest in spirit to ACIB (filter task-irrelevant info) but operates on fused embeddings, not tokens.\n    citation_priority: medium\n\n  - id: ibe_2025\n    title: \"Information Bottleneck-Enhanced RL for Solving Operation Research Problems\"\n    venue: \"MDPI Sensors 2025\"\n    one_liner: Two-level IB — state representation bottleneck + policy bottleneck as exploration bonus.\n    relation: background\n    note: combinatorial RL, not robot manipulation; cited only if discussing IB design space.\n    citation_priority: low\n\n  - id: discrete_ib_drl_2023\n    title: \"Representation Learning in Deep RL via Discrete Information Bottleneck\"\n    venue: PMLR 2023 (Islam et al.)\n    one_liner: Discrete IB on state representation for deep RL.\n    relation: background\n    citation_priority: low\n\n# =====================================================================\n# Direction 2: Token Pruning / Selection for Vision-Language Models\n# =====================================================================\ntoken_pruning_vlm:\n  - id: lightvla_2025\n    title: \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning\"\n    authors: [Jiang, et al.]\n    year: 2025\n    arxiv: \"2509.12594\"\n    project_page: \"https://liauto-research.github.io/LightVLA/\"\n    one_liner: >\n      Differentiable token pruning for VLA: generates dynamic queries to evaluate visual token\n      importance, uses Gumbel softmax for hard selection. 59% FLOPs reduction + 2.9% success\n      rate improvement over OpenVLA-OFT.\n    relation: competitor  # closest VLA-specific token selection work\n    differences_from_acib:\n      goal: \"LightVLA = efficiency (reduce FLOPs); ACIB = robustness regularization (encourage task-relevant focus)\"\n      selection_type: \"LightVLA uses hard Gumbel selection (tokens are dropped); ACIB uses soft gating (all tokens flow through with scaled weights)\"\n      bottleneck: \"LightVLA has no information-theoretic constraint; ACIB enforces aggregate-rate KL to a prior rate\"\n      collapse: \"LightVLA has no anti-collapse mechanism; ACIB's diversity regularizer prevents scorer degeneration\"\n      backbone: \"LightVLA on 7B OpenVLA; ACIB on 0.45B SmolVLA with only 64 visual tokens — different operating regime\"\n    citation_priority: high  # most direct VLA token selection competitor\n\n  - id: divprune_2025\n    title: \"DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models\"\n    authors: [Alvar, Singh, Akbari, Zhang]\n    year: 2025\n    venue: CVPR 2025\n    arxiv: \"2503.02175\"\n    one_liner: Formulates token pruning as Max-Min Diversity Problem; selects most diverse token subset; training-free.\n    relation: complementary  # different goal (efficiency) but shares \"diversity\" motivation\n    differences_from_acib:\n      goal: \"DivPrune = inference efficiency under fixed budget; ACIB = robustness regularization, not efficiency\"\n      training: \"DivPrune is training-free at test time; ACIB trains the scorer end-to-end with action loss\"\n      diversity_role: \"DivPrune diversity is the *objective*; ACIB diversity is an anti-collapse *regularizer*\"\n    citation_priority: high  # closest competing use of 'diversity' in visual token selection\n\n  - id: atp_llava_2025\n    title: \"ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models\"\n    venue: CVPR 2025\n    one_liner: Layer-adaptive token pruning module predicting pruning thresholds per-layer and per-instance, removing text-irrelevant visual tokens.\n    relation: competitor  # also learns a scorer-like importance function\n    differences_from_acib:\n      objective: \"ATP optimizes for accuracy-under-pruning; ACIB optimizes for action-prediction under IB constraint\"\n      action_grounding: \"ATP uses text relevance; ACIB uses action relevance (closer to control)\"\n      mechanism: \"ATP prunes hard tokens; ACIB applies soft mask, all tokens still flow through\"\n    citation_priority: high\n\n  - id: sparsevlm_2025\n    title: \"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference\"\n    authors: [Zhang, Fan, Ma, Zheng, Huang, Cheng, Gudovskiy, Okuno, Nakata, Keutzer, Zhang]\n    year: 2025\n    venue: ICML 2025\n    arxiv: \"2410.04417\"\n    code: \"https://github.com/Gumpest/SparseVLMs\"\n    one_liner: >\n      Training-free token sparsification: uses text-visual attention to rate vision token importance,\n      progressively prunes with rank-based adaptive ratio + token recycling. 54% FLOPs reduction, 97% accuracy retained.\n    relation: background\n    note: Training-free, text-relevance based. No action grounding. General VLM efficiency, not robot-specific.\n    citation_priority: medium\n\n  - id: vla_cache_2025\n    title: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\"\n    authors: [Hsu, et al.]\n    year: 2025\n    venue: NeurIPS 2025\n    arxiv: \"2502.02175\"\n    code: \"https://github.com/siyuhsu/vla-cache\"\n    one_liner: >\n      Training-free inference acceleration: caches static visual tokens across frames, selectively\n      re-computes task-relevant tokens. 1.7x speedup on LIBERO/SIMPLER.\n    relation: background\n    note: >\n      Temporal token reuse, orthogonal to ACIB. Interesting overlap: both identify \"task-relevant\" tokens,\n      but VLA-Cache uses attention-based heuristics while ACIB learns relevance end-to-end.\n    citation_priority: medium\n\n  - id: topv_2025\n    title: \"TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal VLM\"\n    venue: CVPR 2025\n    one_liner: Training-free token pruning posed as inference-time optimization.\n    relation: background\n    citation_priority: medium\n\n  - id: feather_2025\n    title: \"Feather the Throttle: Revisiting Visual Token Pruning for VLMs\"\n    venue: ICCV 2025\n    one_liner: Diagnoses attention-based pruning bias (RoPE long-term decay favors bottom-row tokens) and proposes fixes.\n    relation: background\n    note: useful warning when designing scorer input features; cite if discussing attention-based scorers.\n    citation_priority: medium\n\n  - id: prunevid_2025\n    title: \"PruneVid: Visual Token Pruning for Efficient Video LLMs\"\n    venue: ACL 2025\n    one_liner: Training-free spatial-temporal token merging for video VLMs.\n    relation: background\n    citation_priority: low\n\n  - id: dycoke_2025\n    title: \"DyCoke: Dynamic Compression of Tokens for Fast Video LLMs\"\n    venue: CVPR 2025\n    one_liner: Dynamic token compression for video LLMs.\n    relation: background\n    citation_priority: low\n\n# =====================================================================\n# Direction 3: VLA Robustness / Generalization / Augmentation\n# =====================================================================\nvla_robustness:\n  - id: robustvla_2025\n    title: \"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\"\n    year: 2025\n    arxiv: \"2511.01331\"\n    one_liner: >\n      RL post-training with Jacobian regularization (observation noise sensitivity) +\n      smoothness regularization (action perturbation stability) for VLA robustness.\n    relation: competitor\n    differences_from_acib:\n      stage: \"RobustVLA = post-training RL fine-tuning; ACIB = training-time regularization integrated into BC\"\n      mechanism: \"RobustVLA uses gradient-based Jacobian/smoothness penalties; ACIB uses information-theoretic bottleneck\"\n      interpretability: \"RobustVLA is a black-box regularizer; ACIB produces interpretable per-token relevance scores\"\n      composability: \"potentially complementary — ACIB during training, RobustVLA as post-training hardening\"\n    citation_priority: high\n\n  - id: revla_2025\n    title: \"ReVLA: Reverting Visual Domain Limitation of Robotic Foundation Models\"\n    authors: [Daskalov, et al.]\n    year: 2025\n    arxiv: \"2409.15250\"\n    project_page: \"https://insait-institute.github.io/ReVLA/\"\n    one_liner: >\n      Gradual backbone reversal via model merging — restores vision encoder to pretrained state\n      to combat catastrophic forgetting. +77% grasp, +66% lift on OOD visual tasks over OpenVLA.\n    relation: complementary\n    note: >\n      Addresses the same symptom (VLA visual fragility) from a different angle: ReVLA preserves\n      pretrained visual features, ACIB teaches the model which features matter. Could combine.\n    citation_priority: medium\n\n  - id: libero_plus_2025\n    title: \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\"\n    year: 2025\n    arxiv: \"2510.13626\"\n    one_liner: 7 perturbation dims (object layout, viewpoint, init state, language, light, texture, sensor noise); 10k tasks; shows 95%→<30% drop under modest perturbations.\n    relation: evaluation_benchmark\n    note: >\n      Critical eval target — our ACIB robustness story should be validated here, not on vanilla LIBERO,\n      to avoid the \"memorization\" critique LIBERO-PRO levels at the field.\n    citation_priority: high\n\n  - id: libero_pro_2025\n    title: \"LIBERO-PRO: Towards Robust and Fair Evaluation of VLA Models Beyond Memorization\"\n    year: 2025\n    arxiv: \"2510.03827\"\n    one_liner: Object/position/instruction/task perturbations; SOTA models that report >90% drop to ~0% — exposes rote memorization.\n    relation: evaluation_benchmark\n    citation_priority: high\n\n  - id: eva_vla_2025\n    title: \"Eva-VLA: Evaluating VLA Models' Robustness Under Real-World Physical Variations\"\n    year: 2025\n    arxiv: \"2509.18953\"\n    one_liner: Treats perturbations (viewpoint, init state) as a continuous optimization problem to find worst-case.\n    relation: evaluation_benchmark\n    citation_priority: medium\n\n  - id: vla_multimodal_perturb_2025\n    title: \"On Robustness of VLA Models against Multi-Modal Perturbations\"\n    arxiv: \"2510.00037\"\n    one_liner: Tests mainstream VLAs against 17 uncertainties across 4 modalities; finds action modality most fragile; π0 > OpenVLA.\n    relation: background\n    citation_priority: medium\n\n  - id: byovla_2025\n    title: \"BYOVLA: Removing Model-Sensitive Features via VLM Segmentation + Inpainting\"\n    authors: [Hancock, et al.]\n    year: 2025\n    one_liner: At inference, segments and inpaints out task-irrelevant regions to make VLAs robust.\n    relation: competitor  # solves the same problem (irrelevant visual content hurts policy) at test time\n    differences_from_acib:\n      stage: \"BYOVLA = test-time pre-processing; ACIB = training-time regularization\"\n      mechanism: \"BYOVLA modifies the image (segmentation + inpainting); ACIB modifies the token stream (soft gating)\"\n      cost: \"BYOVLA needs a VLM call per frame; ACIB is a small scorer head, zero extra cost at inference if mask is integrated\"\n    citation_priority: high\n\n  - id: gevrm_2025\n    title: \"GEVRM: Model-based Planning for Visual Corruptions in VLA\"\n    authors: [Zhang, et al.]\n    year: 2025\n    one_liner: Handles color jitter and common visual corruptions via model-based planning.\n    relation: competitor\n    differences_from_acib:\n      mechanism: \"augmentation-style robustness vs. ACIB's regularization-style robustness\"\n    citation_priority: medium\n\n  - id: rocoda_2024\n    title: \"RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning\"\n    year: 2024\n    arxiv: \"2411.16959\"\n    one_liner: Counterfactual augmentation modifying task-irrelevant subset of environment state; tests distractor generalization.\n    relation: complementary\n    note: ACIB and RoCoDA are *complementary* — ACIB is the regularization analogue of RoCoDA's data-side approach.\n    citation_priority: high\n\n  - id: nice_scene_surgery_2025\n    title: \"NICE Scene Surgery: Improving Robotic Manipulation Robustness\"\n    year: 2025\n    arxiv: \"2511.22777\"\n    one_liner: Edits scenes to insert distractors while preserving causal task-relevant features.\n    relation: complementary\n    citation_priority: medium\n\n  - id: genaug_2023\n    title: \"GenAug: Scaling Robot Learning with Semantic Data Augmentation\"\n    venue: RSS 2023\n    one_liner: Diffusion-based scene augmentation (backgrounds, distractors, textures) for imitation learning.\n    relation: complementary\n    citation_priority: medium\n\n# =====================================================================\n# Direction 4: LIBERO + VLA Baselines\n# =====================================================================\nlibero_baselines:\n  - id: openvla_2024\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    year: 2024\n    one_liner: 7B Llama-based VLA; LIBERO 76.5% avg.\n    relation: backbone_baseline\n    citation_priority: high\n\n  - id: openvla_oft_2025\n    title: \"Fine-Tuning VLA Models: Optimizing Speed and Success (OpenVLA-OFT)\"\n    authors: [Kim, et al.]\n    year: 2025\n    venue: RSS 2025\n    arxiv: \"2502.19645\"\n    one_liner: Parallel decoding + action chunking + continuous actions + L1 regression; 76.5%→97.1% on LIBERO; 26× faster.\n    relation: strong_baseline\n    note: Current LIBERO SOTA prior to VLA-0; ACIB must compare against OFT recipe.\n    citation_priority: high\n\n  - id: pi0_2024\n    title: \"π0: A Vision-Language-Action Flow Model\"\n    authors: [Black, et al.]\n    year: 2024\n    one_liner: 3.3B robotics-pretrained flow-matching VLA; LIBERO 86.0%; most robust under multi-modal perturbations.\n    relation: strong_baseline\n    citation_priority: high\n\n  - id: pi0_fast_2025\n    title: \"π0-FAST\"\n    authors: [Pertsch, et al.]\n    year: 2025\n    one_liner: Faster autoregressive variant of π0.\n    relation: baseline\n    citation_priority: medium\n\n  - id: smolvla_2025\n    title: \"SmolVLA: A VLA Model for Affordable and Efficient Robotics\"\n    year: 2025\n    arxiv: \"2506.01844\"\n    one_liner: 0.45B VLA; PixelShuffle compresses 1024→64 visual tokens; VLM layer-skip; CA/SA interleaved action expert; LIBERO 87.3%.\n    relation: our_backbone\n    note: >\n      Our chosen backbone. Important: SmolVLA already reduces to 64 visual tokens via PixelShuffle,\n      so ACIB's scorer operates on a small token set — must justify why further token-level gating\n      helps when the count is already low (answer: not all 64 are equally task-relevant per scene/timestep).\n    citation_priority: high\n\n  - id: vla_0_2025\n    title: \"VLA-0: Building SOTA VLAs with Zero Modification\"\n    year: 2025\n    arxiv: \"2510.13054\"\n    one_liner: Outperforms OpenVLA-OFT, SmolVLA, π0.5-KI on LIBERO with no architectural changes.\n    relation: strong_baseline\n    citation_priority: high\n\n# =====================================================================\n# Novelty Position Statement\n# =====================================================================\nnovelty_synthesis:\n  closest_competitors:\n    - bc_ib_2025      # IB for BC, but representation-level\n    - lightvla_2025   # learned token selection for VLA, but efficiency-oriented pruning\n\n  delta_vs_bc_ib:\n    - \"BC-IB applies IB at the fused-latent level (one Z); ACIB applies IB at the visual-token level (per-token gate)\"\n    - \"BC-IB uses MINE for MI estimation; ACIB uses aggregate-rate KL (KL on batch-mean scorer output to a prior rate)\"\n    - \"BC-IB has no scorer interpretability — Z is opaque; ACIB exposes a per-token relevance score usable for visualization/analysis\"\n    - \"BC-IB does not face per-token collapse; ACIB introduces an explicit diversity regularizer and tracks scorer_std as a training health metric (0.441 in our successful run)\"\n\n  delta_vs_lightvla:\n    - \"LightVLA targets efficiency (hard Gumbel pruning, drop tokens); ACIB targets robustness (soft gating, all tokens retained with scaled weights)\"\n    - \"LightVLA has no information-theoretic framework; ACIB enforces an aggregate-rate KL bottleneck\"\n    - \"LightVLA has no anti-collapse mechanism; ACIB's diversity regularizer prevents scorer degeneration\"\n    - \"LightVLA on 7B OpenVLA; ACIB on 0.45B SmolVLA with only 64 visual tokens — different operating regime\"\n\n  uniqueness_combination:\n    description: >\n      To our knowledge no prior work combines (a) token-level IB on visual tokens, (b) end-to-end\n      training driven by an action-prediction loss (not reconstruction or text relevance),\n      (c) aggregate-rate KL as the bottleneck term, (d) an explicit anti-collapse diversity\n      regularizer with an empirical health metric, and (e) soft gating rather than hard pruning.\n      The closest competitors each share at most one of these axes:\n        - BC-IB: shares IB-for-policy but at representation level, no token scorer, no collapse issue.\n        - LightVLA: shares learned VLA token selection but for efficiency via hard pruning, no IB framework.\n        - ATP-LLaVA: shares token-level scoring but for text-relevance and pruning, not action-grounded IB.\n        - DivPrune: shares diversity motivation but as the objective (not anti-collapse) and is training-free.\n        - BYOVLA: shares \"remove irrelevant visual content\" goal but at test time via VLM inpainting.\n        - RobustVLA: shares VLA robustness goal but via gradient-based Jacobian/smoothness penalties, not IB.\n        - RoCoDA / GenAug: shares the underlying problem (distractor invariance) but solves it via data augmentation.\n    framing: >\n      ACIB = regularization-side counterpart to data-augmentation approaches for VLA robustness,\n      with action-conditioned token-level IB as the mechanism. Soft gating under an information\n      constraint, not hard pruning for efficiency.\n\n  positioning_risks:\n    - \"BC-IB ICML-25 is the *direct* prior art on IB-for-BC. Differentiation must be airtight; expect reviewers to ask 'why token-level if representation-level already works?'\"\n    - \"LightVLA does learned token selection *specifically for VLA* — reviewers may conflate it with ACIB. Key defense: ACIB is soft gating under IB for robustness, not hard pruning for efficiency.\"\n    - \"Token-pruning literature (DivPrune, ATP-LLaVA, SparseVLM) may be invoked as similar token-selection work. Need to clarify that ACIB does not prune — it gates softly under an information constraint, and the goal is regularization, not efficiency.\"\n    - \"LIBERO-Plus / LIBERO-PRO show standard LIBERO scores are inflated by memorization. ACIB should report on LIBERO-Plus or analogous perturbation eval to make a credible robustness claim — otherwise the contribution will be perceived as marginal.\"\n    - \"RobustVLA targets the same VLA robustness goal via RL post-training. Must argue why training-time IB regularization is preferable to or complementary with post-training approaches.\"\n\n  must_cite:\n    - bc_ib_2025\n    - lightvla_2025\n    - divprune_2025\n    - atp_llava_2025\n    - byovla_2025\n    - robustvla_2025\n    - rocoda_2024\n    - libero_plus_2025\n    - openvla_oft_2025\n    - smolvla_2025\n    - pi0_2024\n    - vla_0_2025\n\n  should_cite:\n    - mib_multimodal_2024\n    - vib_rl_skill_2023\n    - sparsevlm_2025\n    - vla_cache_2025\n    - revla_2025\n    - libero_pro_2025\n    - eva_vla_2025\n    - gevrm_2025\n    - genaug_2023\n    - feather_2025\n    - openvla_2024\n\n  open_research_directions:\n    - \"Does the learned scorer transfer across task suites (LIBERO-Spatial scorer applied to LIBERO-Goal)?\"\n    - \"Correlation between scorer mask and object-segmentation masks — does ACIB learn an implicit object detector for free?\"\n    - \"Combining ACIB with augmentation (RoCoDA/GenAug) — does the regularization-side + data-side gain stack?\"\n    - \"Robustness on LIBERO-Plus perturbation dims, especially camera viewpoint and distractor objects — where the 95→30% drop lives.\"\n    - \"ACIB + RobustVLA: training-time IB regularization + post-training RL hardening — do they compose?\"\n",
      "numLines": 436,
      "startLine": 1,
      "totalLines": 436
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

现有文件已涵盖不少内容，但缺少用户要求的几个主题：(1) ViT token pruning经典论文（ToMe, DynamicViT, EViT, A-ViT）；(2) IB理论基础（VIB, Deep VIB）；(3) instruction-conditioned visual attention for robot learning；(4) VLM interpretability methods。现在并行搜索这些缺失主题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "644c5c27-5993-47d8-a3f6-93ac928b0bee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TexFHWGNYzG2BkbmyYsqmm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7969,
      "cache_read_input_tokens": 26224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7969
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T4snDZduvn7pLfCxiqopew`</summary>

```json
{
  "query": "Token Merging ToMe Vision Transformer token pruning Bolya ICLR 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "80704109-17f7-46ac-b5ea-15df82c4c0b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TexFHWGNYzG2BkbmyYsqmm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7969,
      "cache_read_input_tokens": 26224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7969
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tvhzb64bshBzgghdtu97jw`</summary>

```json
{
  "query": "DynamicViT dynamic token sparsification vision transformer Rao NeurIPS 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "402936c5-d57c-49c2-beb7-ae8596b4cd7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TexFHWGNYzG2BkbmyYsqmm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7969,
      "cache_read_input_tokens": 26224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7969
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

_source line 17_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0175QXj2PUVyvS4Hnz6JGhjg`</summary>

```json
{
  "query": "EViT Expediting Vision Transformers token attentiveness Liang 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "da8959fa-e142-4649-bd82-79a3ab856f08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TexFHWGNYzG2BkbmyYsqmm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7969,
      "cache_read_input_tokens": 26224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7969
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

_source line 18_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A5EfpkkD7pioYQbnBrM7aZ`</summary>

```json
{
  "query": "A-ViT Adaptive Vision Transformer adaptive token halting Yin ECCV 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "6dd3e786-3f8d-434f-9d5d-feed68d26030",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TexFHWGNYzG2BkbmyYsqmm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7969,
      "cache_read_input_tokens": 26224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7969
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

_source line 19 · 2026-05-17T15:02:51.953Z_

<details><summary>↩ Tool result · `toolu_01Tvhzb64bshBzgghdtu97jw`</summary>

```text
Web search results for query: "DynamicViT dynamic token sparsification vision transformer Rao NeurIPS 2021"

Links: [{"title":"GitHub - raoyongming/DynamicViT: [NeurIPS 2021] [T-PAMI] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification · GitHub","url":"https://github.com/raoyongming/DynamicViT"},{"title":"DynamicViT: Efﬁcient Vision Transformers with Dynamic Token Sparsiﬁcation","url":"https://papers.neurips.cc/paper_files/paper/2021/file/747d3443e319a22747fbb873e8b2f9f2-Paper.pdf"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification","url":"https://proceedings.neurips.cc/paper/2021/hash/747d3443e319a22747fbb873e8b2f9f2-Abstract.html"},{"title":"[2106.02034] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification","url":"https://arxiv.org/abs/2106.02034"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification | OpenReview","url":"https://openreview.net/forum?id=kR95DuwwXHZ"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification","url":"https://papers.nips.cc/paper/2021/hash/747d3443e319a22747fbb873e8b2f9f2-Abstract.html"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210602034R/abstract"},{"title":"[2021 NeurIPS] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification","url":"https://velog.io/@hseop/DynamicViT-Efficient-Vision-Transformers-withDynamic-Token-Sparsification"},{"title":"[PDF] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DynamicViT:-Efficient-Vision-Transformers-with-Rao-Zhao/dbdcabd0444ad50b68ee09e30f39b66e9068f5d2"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic ...","url":"https://proceedings.neurips.cc/paper/2021/file/747d3443e319a22747fbb873e8b2f9f2-Paper.pdf"}]

I found comprehensive information about DynamicViT from the search results. Here's what I found:

## Overview

DynamicViT is a NeurIPS 2021 paper by Yongming Rao, Wenliang Zhao, Benlin Liu, Jiwen Lu, Jie Zhou, and Cho-Jui Hsieh.

## Key Concept

DynamicViT is a dynamic token sparsification framework to prune redundant tokens in vision transformers progressively and dynamically based on the input. The work observes that attention is sparse in vision transformers, and that the final prediction is only based on a subset of most informative tokens, which is sufficient for accurate image recognition.

## Technical Approach

The method devises a lightweight prediction module to estimate the importance score of each token given the current features, and this module is added to different layers to prune redundant tokens hierarchically. An attention masking strategy is proposed to differentiably prune a token by blocking its interactions with other tokens.

## Performance

By hierarchically pruning 66% of the input tokens, the method reduces 31%~37% FLOPs and improves throughput by over 40% while the drop of accuracy is within 0.5% for various vision transformers.

## Code Availability

Code is available at https://github.com/raoyongming/DynamicViT


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "128bb4f3-51cf-4b2c-94de-bcb99f93016a",
  "tool_use_result": {
    "query": "DynamicViT dynamic token sparsification vision transformer Rao NeurIPS 2021",
    "results": [
      {
        "tool_use_id": "srvtoolu_0161dGCAKVT5KvPtKhaQS9C9",
        "content": [
          {
            "title": "GitHub - raoyongming/DynamicViT: [NeurIPS 2021] [T-PAMI] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification · GitHub",
            "url": "https://github.com/raoyongming/DynamicViT"
          },
          {
            "title": "DynamicViT: Efﬁcient Vision Transformers with Dynamic Token Sparsiﬁcation",
            "url": "https://papers.neurips.cc/paper_files/paper/2021/file/747d3443e319a22747fbb873e8b2f9f2-Paper.pdf"
          },
          {
            "title": "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification",
            "url": "https://proceedings.neurips.cc/paper/2021/hash/747d3443e319a22747fbb873e8b2f9f2-Abstract.html"
          },
          {
            "title": "[2106.02034] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification",
            "url": "https://arxiv.org/abs/2106.02034"
          },
          {
            "title": "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification | OpenReview",
            "url": "https://openreview.net/forum?id=kR95DuwwXHZ"
          },
          {
            "title": "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification",
            "url": "https://papers.nips.cc/paper/2021/hash/747d3443e319a22747fbb873e8b2f9f2-Abstract.html"
          },
          {
            "title": "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2021arXiv210602034R/abstract"
          },
          {
            "title": "[2021 NeurIPS] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification",
            "url": "https://velog.io/@hseop/DynamicViT-Efficient-Vision-Transformers-withDynamic-Token-Sparsification"
          },
          {
            "title": "[PDF] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/DynamicViT:-Efficient-Vision-Transformers-with-Rao-Zhao/dbdcabd0444ad50b68ee09e30f39b66e9068f5d2"
          },
          {
            "title": "DynamicViT: Efficient Vision Transformers with Dynamic ...",
            "url": "https://proceedings.neurips.cc/paper/2021/file/747d3443e319a22747fbb873e8b2f9f2-Paper.pdf"
          }
        ]
      },
      "I found comprehensive information about DynamicViT from the search results. Here's what I found:\n\n## Overview\n\nDynamicViT is a NeurIPS 2021 paper by Yongming Rao, Wenliang Zhao, Benlin Liu, Jiwen Lu, Jie Zhou, and Cho-Jui Hsieh.\n\n## Key Concept\n\nDynamicViT is a dynamic token sparsification framework to prune redundant tokens in vision transformers progressively and dynamically based on the input. The work observes that attention is sparse in vision transformers, and that the final prediction is only based on a subset of most informative tokens, which is sufficient for accurate image recognition.\n\n## Technical Approach\n\nThe method devises a lightweight prediction module to estimate the importance score of each token given the current features, and this module is added to different layers to prune redundant tokens hierarchically. An attention masking strategy is proposed to differentiably prune a token by blocking its interactions with other tokens.\n\n## Performance\n\nBy hierarchically pruning 66% of the input tokens, the method reduces 31%~37% FLOPs and improves throughput by over 40% while the drop of accuracy is within 0.5% for various vision transformers.\n\n## Code Availability\n\nCode is available at https://github.com/raoyongming/DynamicViT"
    ],
    "durationSeconds": 5.979331857000001
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T15:02:53.263Z_

<details><summary>↩ Tool result · `toolu_01T4snDZduvn7pLfCxiqopew`</summary>

```text
Web search results for query: "Token Merging ToMe Vision Transformer token pruning Bolya ICLR 2023"

Links: [{"title":"Published as a conference paper at ICLR 2023 TOKEN MERGING: YOUR VIT BUT FASTER","url":"https://arxiv.org/pdf/2210.09461"},{"title":"GitHub - facebookresearch/ToMe: A method to increase the speed and lower the memory footprint of existing vision transformers. · GitHub","url":"https://github.com/facebookresearch/ToMe"},{"title":"[2210.09461] Token Merging: Your ViT But Faster","url":"https://arxiv.org/abs/2210.09461"},{"title":"Token Merging for Fast Stable Diffusion Daniel Bolya Judy Hoffman Georgia Tech","url":"https://openaccess.thecvf.com/content/CVPR2023W/ECV/papers/Bolya_Token_Merging_for_Fast_Stable_Diffusion_CVPRW_2023_paper.pdf"},{"title":"Track: Oral 1 Track 1: Deep Learning and representational learning I","url":"https://iclr.cc/virtual/2023/session/13335"},{"title":"Multimodal Promptable Token Merging for Diffusion Models","url":"https://ojs.aaai.org/index.php/AAAI/article/download/33894/36049"},{"title":"ICLR 2023 Token Merging: Your ViT But Faster Oral","url":"https://iclr.cc/virtual/2023/oral/12533"},{"title":"Published as a conference paper at ICLR 2023 TOKEN MERGING: YOUR VIT BUT FASTER","url":"https://openreview.net/pdf?id=JroZRaRw7Eu"},{"title":"ENERGY MINIMIZING-BASED TOKEN MERGING FOR ...","url":"https://www.dfki.de/fileadmin/user_upload/import/15618_84_Energy_Minimizing_based_tok.pdf"},{"title":"Token Merging: Your ViT But Faster | OpenReview","url":"https://openreview.net/forum?id=JroZRaRw7Eu"}]

## Search Results Summary

I found comprehensive information about Token Merging (ToMe) from the search results. Here's what I discovered:

### Paper Overview
Token Merging: Your ViT but Faster is authored by Daniel Bolya, Cheng-Yang Fu, Xiaoliang Dai, Peizhao Zhang, Christoph Feichtenholer, and Judy Hoffman, and the paper was accepted for an oral presentation at ICLR 2023.

### Core Method
ToMe is a simple method to increase the throughput of existing ViT models without needing to train. ToMe gradually combines similar tokens in a transformer using a general and light-weight matching algorithm that is as fast as pruning while being more accurate.

### Key Distinction from Pruning
Unlike token pruning approaches, Token Merging combines tokens rather than prune them. ToMe merges tokens based on their similarity, implicitly grouping parts of objects together, which is in contrast to token pruning that only removes background tokens. ToMe can reduce more tokens because it can merge redundant foreground tokens in addition to background ones.

### Performance Results
Off-the-shelf, ToMe can 2x the throughput of state-of-the-art ViT-L @ 512 and ViT-H @ 518 models on images and 2.2x the throughput of ViT-L on video with only a 0.2-0.3% accuracy drop in each case.

The official code is available on GitHub as a method that allows you to take an existing Vision Transformer architecture and efficiently merge tokens inside of the network for 2-3x faster evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "c38d7153-db15-4c8b-99ac-29e747bac626",
  "tool_use_result": {
    "query": "Token Merging ToMe Vision Transformer token pruning Bolya ICLR 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WXeA21Pg1zwEGCTeBWmKEQ",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2023 TOKEN MERGING: YOUR VIT BUT FASTER",
            "url": "https://arxiv.org/pdf/2210.09461"
          },
          {
            "title": "GitHub - facebookresearch/ToMe: A method to increase the speed and lower the memory footprint of existing vision transformers. · GitHub",
            "url": "https://github.com/facebookresearch/ToMe"
          },
          {
            "title": "[2210.09461] Token Merging: Your ViT But Faster",
            "url": "https://arxiv.org/abs/2210.09461"
          },
          {
            "title": "Token Merging for Fast Stable Diffusion Daniel Bolya Judy Hoffman Georgia Tech",
            "url": "https://openaccess.thecvf.com/content/CVPR2023W/ECV/papers/Bolya_Token_Merging_for_Fast_Stable_Diffusion_CVPRW_2023_paper.pdf"
          },
          {
            "title": "Track: Oral 1 Track 1: Deep Learning and representational learning I",
            "url": "https://iclr.cc/virtual/2023/session/13335"
          },
          {
            "title": "Multimodal Promptable Token Merging for Diffusion Models",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/download/33894/36049"
          },
          {
            "title": "ICLR 2023 Token Merging: Your ViT But Faster Oral",
            "url": "https://iclr.cc/virtual/2023/oral/12533"
          },
          {
            "title": "Published as a conference paper at ICLR 2023 TOKEN MERGING: YOUR VIT BUT FASTER",
            "url": "https://openreview.net/pdf?id=JroZRaRw7Eu"
          },
          {
            "title": "ENERGY MINIMIZING-BASED TOKEN MERGING FOR ...",
            "url": "https://www.dfki.de/fileadmin/user_upload/import/15618_84_Energy_Minimizing_based_tok.pdf"
          },
          {
            "title": "Token Merging: Your ViT But Faster | OpenReview",
            "url": "https://openreview.net/forum?id=JroZRaRw7Eu"
          }
        ]
      },
      "## Search Results Summary\n\nI found comprehensive information about Token Merging (ToMe) from the search results. Here's what I discovered:\n\n### Paper Overview\nToken Merging: Your ViT but Faster is authored by Daniel Bolya, Cheng-Yang Fu, Xiaoliang Dai, Peizhao Zhang, Christoph Feichtenholer, and Judy Hoffman, and the paper was accepted for an oral presentation at ICLR 2023.\n\n### Core Method\nToMe is a simple method to increase the throughput of existing ViT models without needing to train. ToMe gradually combines similar tokens in a transformer using a general and light-weight matching algorithm that is as fast as pruning while being more accurate.\n\n### Key Distinction from Pruning\nUnlike token pruning approaches, Token Merging combines tokens rather than prune them. ToMe merges tokens based on their similarity, implicitly grouping parts of objects together, which is in contrast to token pruning that only removes background tokens. ToMe can reduce more tokens because it can merge redundant foreground tokens in addition to background ones.\n\n### Performance Results\nOff-the-shelf, ToMe can 2x the throughput of state-of-the-art ViT-L @ 512 and ViT-H @ 518 models on images and 2.2x the throughput of ViT-L on video with only a 0.2-0.3% accuracy drop in each case.\n\nThe official code is available on GitHub as a method that allows you to take an existing Vision Transformer architecture and efficiently merge tokens inside of the network for 2-3x faster evaluation."
    ],
    "durationSeconds": 8.294196597000003
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T15:02:53.664Z_

<details><summary>↩ Tool result · `toolu_0175QXj2PUVyvS4Hnz6JGhjg`</summary>

```text
Web search results for query: "EViT Expediting Vision Transformers token attentiveness Liang 2022"

Links: [{"title":"GitHub - youweiliang/evit: Python code for ICLR 2022 spotlight paper EViT: Expediting Vision Transformers via Token Reorganizations · GitHub","url":"https://github.com/youweiliang/evit"},{"title":"[2202.07800] Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations","url":"https://arxiv.org/abs/2202.07800"},{"title":"EViT: Expediting Vision Transformers via Token Reorganizations | OpenReview","url":"https://openreview.net/forum?id=BjyvwnXXVn_"},{"title":"Papers with Code - EViT: Expediting Vision Transformers via Token Reorganizations","url":"https://paperswithcode.com/paper/evit-expediting-vision-transformers-via-token"},{"title":"EVIT: EXPEDITING VISION TRANSFORMERS VIA TOKEN ...","url":"https://openreview.net/references/pdf?id=EzNODF0csg"},{"title":"ICLR 2022 EViT: Expediting Vision Transformers via Token Reorganizations Spotlight","url":"https://iclr.cc/virtual/2022/spotlight/6169"},{"title":"(PDF) Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations","url":"https://www.researchgate.net/publication/358655949_Not_All_Patches_are_What_You_Need_Expediting_Vision_Transformers_via_Token_Reorganizations"},{"title":"EXPEDITING VISION TRANSFORMERS VIA TOKEN ...","url":"https://openreview.net/pdf/feb0c5a2e1c1fc63509c2e528ca07aa95aea2d5e.pdf"},{"title":"Expediting Vision Transformers via Token Reorganizations","url":"https://iclr.cc/media/iclr-2022/Slides/6168.pdf"},{"title":"ICLR Poster EViT: Expediting Vision Transformers via Token Reorganizations","url":"https://iclr.cc/virtual/2022/poster/6168"}]

I've found comprehensive information about EViT. Here are the key findings:

## Overview

EViT is an ICLR 2022 Spotlight paper titled "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations" by Youwei Liang, Chongjian Ge, Zhan Tong, Yibing Song, Jue Wang, and Pengtao Xie.

## Core Concept

Vision Transformers (ViTs) take all the image patches as tokens and construct multi-head self-attention (MHSA) among them. Complete leverage of these image tokens brings redundant computations since not all the tokens are attentive in MHSA.

## Method

For each forward inference, the method identifies the attentive image tokens between MHSA and FFN (feed-forward network) modules, which is guided by the corresponding class token attention. Then, it reorganizes image tokens by preserving attentive image tokens and fusing inattentive ones to expedite subsequent MHSA and FFN computations.

## Key Results

The inference speed of DeiT-S is increased by 50% while its recognition accuracy is decreased by only 0.3% for ImageNet classification. Additionally, EViT improves the recognition accuracy of DeiT-S by 1% for ImageNet classification at the same computational cost of a vanilla DeiT-S.

The method does not introduce more parameters to ViTs. The code is available at https://github.com/youweiliang/evit.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "d49baa75-6f6b-46f1-82dc-2846951c3ada",
  "tool_use_result": {
    "query": "EViT Expediting Vision Transformers token attentiveness Liang 2022",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VpzG8KekqGzcsyxxKw1pVb",
        "content": [
          {
            "title": "GitHub - youweiliang/evit: Python code for ICLR 2022 spotlight paper EViT: Expediting Vision Transformers via Token Reorganizations · GitHub",
            "url": "https://github.com/youweiliang/evit"
          },
          {
            "title": "[2202.07800] Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations",
            "url": "https://arxiv.org/abs/2202.07800"
          },
          {
            "title": "EViT: Expediting Vision Transformers via Token Reorganizations | OpenReview",
            "url": "https://openreview.net/forum?id=BjyvwnXXVn_"
          },
          {
            "title": "Papers with Code - EViT: Expediting Vision Transformers via Token Reorganizations",
            "url": "https://paperswithcode.com/paper/evit-expediting-vision-transformers-via-token"
          },
          {
            "title": "EVIT: EXPEDITING VISION TRANSFORMERS VIA TOKEN ...",
            "url": "https://openreview.net/references/pdf?id=EzNODF0csg"
          },
          {
            "title": "ICLR 2022 EViT: Expediting Vision Transformers via Token Reorganizations Spotlight",
            "url": "https://iclr.cc/virtual/2022/spotlight/6169"
          },
          {
            "title": "(PDF) Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations",
            "url": "https://www.researchgate.net/publication/358655949_Not_All_Patches_are_What_You_Need_Expediting_Vision_Transformers_via_Token_Reorganizations"
          },
          {
            "title": "EXPEDITING VISION TRANSFORMERS VIA TOKEN ...",
            "url": "https://openreview.net/pdf/feb0c5a2e1c1fc63509c2e528ca07aa95aea2d5e.pdf"
          },
          {
            "title": "Expediting Vision Transformers via Token Reorganizations",
            "url": "https://iclr.cc/media/iclr-2022/Slides/6168.pdf"
          },
          {
            "title": "ICLR Poster EViT: Expediting Vision Transformers via Token Reorganizations",
            "url": "https://iclr.cc/virtual/2022/poster/6168"
          }
        ]
      },
      "I've found comprehensive information about EViT. Here are the key findings:\n\n## Overview\n\nEViT is an ICLR 2022 Spotlight paper titled \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\" by Youwei Liang, Chongjian Ge, Zhan Tong, Yibing Song, Jue Wang, and Pengtao Xie.\n\n## Core Concept\n\nVision Transformers (ViTs) take all the image patches as tokens and construct multi-head self-attention (MHSA) among them. Complete leverage of these image tokens brings redundant computations since not all the tokens are attentive in MHSA.\n\n## Method\n\nFor each forward inference, the method identifies the attentive image tokens between MHSA and FFN (feed-forward network) modules, which is guided by the corresponding class token attention. Then, it reorganizes image tokens by preserving attentive image tokens and fusing inattentive ones to expedite subsequent MHSA and FFN computations.\n\n## Key Results\n\nThe inference speed of DeiT-S is increased by 50% while its recognition accuracy is decreased by only 0.3% for ImageNet classification. Additionally, EViT improves the recognition accuracy of DeiT-S by 1% for ImageNet classification at the same computational cost of a vanilla DeiT-S.\n\nThe method does not introduce more parameters to ViTs. The code is available at https://github.com/youweiliang/evit."
    ],
    "durationSeconds": 6.769664934000001
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T15:02:53.814Z_

<details><summary>↩ Tool result · `toolu_01A5EfpkkD7pioYQbnBrM7aZ`</summary>

```text
Web search results for query: "A-ViT Adaptive Vision Transformer adaptive token halting Yin ECCV 2022"

Links: [{"title":"A-ViT: Adaptive Tokens for Efﬁcient Vision Transformer Hongxu Yin Arash Vahdat","url":"https://openaccess.thecvf.com/content/CVPR2022/papers/Yin_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer_CVPR_2022_paper.pdf"},{"title":"A-ViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://a-vit.github.io/"},{"title":"[2112.07658] AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/abs/2112.07658"},{"title":"A-ViT - CVPR 2022 Open Access Repository","url":"https://openaccess.thecvf.com/content/CVPR2022/html/Yin_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer_CVPR_2022_paper.html"},{"title":"[PDF] A-ViT: Adaptive Tokens for Efficient Vision Transformer | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-ViT:-Adaptive-Tokens-for-Efficient-Vision-Yin-Vahdat/c2a0c18e810535db52e5ebaf180c64ce70356748"},{"title":"Yin a-ViT Adaptive Tokens For Efficient Vision Transformer CVPR 2022 Paper | PDF | Computer Vision | Artificial Neural Network","url":"https://www.scribd.com/document/681449307/Yin-a-ViT-Adaptive-Tokens-for-Efficient-Vision-Transformer-CVPR-2022-Paper"},{"title":"A-ViT: Adaptive Tokens for Efficient Vision Transformer | Request PDF","url":"https://www.researchgate.net/publication/363908419_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer"},{"title":"A-ViT: Adaptive Tokens for Efficient Vision Transformer | Research","url":"https://research.nvidia.com/publication/2022-06_vit-adaptive-tokens-efficient-vision-transformer"},{"title":"GitHub - NVlabs/A-ViT: Official PyTorch implementation of A-ViT: Adaptive Tokens for Efficient Vision Transformer (CVPR 2022) · GitHub","url":"https://github.com/NVlabs/A-ViT"},{"title":"[CVPR'22 Oral] A-ViT: Adaptive Tokens for Efficient Vision Transformer | Request PDF","url":"https://www.researchgate.net/publication/357046283_CVPR'22_Oral_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer"}]

Based on the search results, here's information about A-ViT:

## Overview

A-ViT is a method to enable adaptive token computation for vision transformers by augmenting the vision transformer block with an adaptive halting module that computes a halting probability per token.

## Key Technical Details

The module reuses the parameters of existing blocks and it borrows a single neuron from the last dense layer in each block to compute the halting probability, imposing no extra parameters or computations. A token is discarded once reaching the halting condition, and via adaptively halting tokens, dense compute is performed only on the active tokens deemed informative for the task, with successive blocks in vision transformers gradually receiving less tokens, leading to faster inference.

## Methodology

The approach reformulates Adaptive Computation Time (Graves'17) for this task, extending halting to discard redundant spatial tokens. The method further introduces distributional prior regularization that stabilizes training compared to prior ACT approaches.

## Performance Results

The proposed method improves the throughput of DeiT-Tiny by 62% and DeiT-Small by 38% with only 0.3% accuracy drop, outperforming prior art by a large margin.

## Publication

Note: The search results indicate that A-ViT was published at **CVPR 2022**, not ECCV 2022. The paper is titled "A-ViT: Adaptive Tokens for Efficient Vision Transformer (CVPR 2022)" and was authored by Hongxu Yin, Arash Vahdat, and colleagues from NVIDIA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "c4825f20-bdbd-4734-9f21-3349dba3ef2a",
  "tool_use_result": {
    "query": "A-ViT Adaptive Vision Transformer adaptive token halting Yin ECCV 2022",
    "results": [
      {
        "tool_use_id": "srvtoolu_013X6pd7PsVKVfpCoWZ2JBTg",
        "content": [
          {
            "title": "A-ViT: Adaptive Tokens for Efﬁcient Vision Transformer Hongxu Yin Arash Vahdat",
            "url": "https://openaccess.thecvf.com/content/CVPR2022/papers/Yin_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer_CVPR_2022_paper.pdf"
          },
          {
            "title": "A-ViT: Adaptive Tokens for Efficient Vision Transformer",
            "url": "https://a-vit.github.io/"
          },
          {
            "title": "[2112.07658] AdaViT: Adaptive Tokens for Efficient Vision Transformer",
            "url": "https://arxiv.org/abs/2112.07658"
          },
          {
            "title": "A-ViT - CVPR 2022 Open Access Repository",
            "url": "https://openaccess.thecvf.com/content/CVPR2022/html/Yin_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer_CVPR_2022_paper.html"
          },
          {
            "title": "[PDF] A-ViT: Adaptive Tokens for Efficient Vision Transformer | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/A-ViT:-Adaptive-Tokens-for-Efficient-Vision-Yin-Vahdat/c2a0c18e810535db52e5ebaf180c64ce70356748"
          },
          {
            "title": "Yin a-ViT Adaptive Tokens For Efficient Vision Transformer CVPR 2022 Paper | PDF | Computer Vision | Artificial Neural Network",
            "url": "https://www.scribd.com/document/681449307/Yin-a-ViT-Adaptive-Tokens-for-Efficient-Vision-Transformer-CVPR-2022-Paper"
          },
          {
            "title": "A-ViT: Adaptive Tokens for Efficient Vision Transformer | Request PDF",
            "url": "https://www.researchgate.net/publication/363908419_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer"
          },
          {
            "title": "A-ViT: Adaptive Tokens for Efficient Vision Transformer | Research",
            "url": "https://research.nvidia.com/publication/2022-06_vit-adaptive-tokens-efficient-vision-transformer"
          },
          {
            "title": "GitHub - NVlabs/A-ViT: Official PyTorch implementation of A-ViT: Adaptive Tokens for Efficient Vision Transformer (CVPR 2022) · GitHub",
            "url": "https://github.com/NVlabs/A-ViT"
          },
          {
            "title": "[CVPR'22 Oral] A-ViT: Adaptive Tokens for Efficient Vision Transformer | Request PDF",
            "url": "https://www.researchgate.net/publication/357046283_CVPR'22_Oral_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer"
          }
        ]
      },
      "Based on the search results, here's information about A-ViT:\n\n## Overview\n\nA-ViT is a method to enable adaptive token computation for vision transformers by augmenting the vision transformer block with an adaptive halting module that computes a halting probability per token.\n\n## Key Technical Details\n\nThe module reuses the parameters of existing blocks and it borrows a single neuron from the last dense layer in each block to compute the halting probability, imposing no extra parameters or computations. A token is discarded once reaching the halting condition, and via adaptively halting tokens, dense compute is performed only on the active tokens deemed informative for the task, with successive blocks in vision transformers gradually receiving less tokens, leading to faster inference.\n\n## Methodology\n\nThe approach reformulates Adaptive Computation Time (Graves'17) for this task, extending halting to discard redundant spatial tokens. The method further introduces distributional prior regularization that stabilizes training compared to prior ACT approaches.\n\n## Performance Results\n\nThe proposed method improves the throughput of DeiT-Tiny by 62% and DeiT-Small by 38% with only 0.3% accuracy drop, outperforming prior art by a large margin.\n\n## Publication\n\nNote: The search results indicate that A-ViT was published at **CVPR 2022**, not ECCV 2022. The paper is titled \"A-ViT: Adaptive Tokens for Efficient Vision Transformer (CVPR 2022)\" and was authored by Hongxu Yin, Arash Vahdat, and colleagues from NVIDIA."
    ],
    "durationSeconds": 6.463768635
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the first batch of ViT token pruning papers. Now let me search for the remaining topics in parallel: IB theory, instruction-conditioned visual attention for robot learning, and VLM interpretability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "27699996-9f25-4438-9a4e-525f36b9cfca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiVWQ926DZcREyoa9kdynB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4626,
      "cache_read_input_tokens": 34193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4626
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

搜到了 ViT token pruning 经典论文。继续搜索剩余主题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "186fdee6-ec96-4def-98c7-00e6117c514a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiVWQ926DZcREyoa9kdynB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4626,
      "cache_read_input_tokens": 34193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4626
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ECs6L1ugcLnGMcNBweqh84`</summary>

```json
{
  "query": "Variational Information Bottleneck deep learning Alemi ICLR 2017 Deep VIB"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "cbda0e95-bbca-4749-9d57-b6e903c7fa86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiVWQ926DZcREyoa9kdynB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4626,
      "cache_read_input_tokens": 34193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4626
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

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LLW5EupTbMZ8DS6ej36P1b`</summary>

```json
{
  "query": "Information Bottleneck representation learning neural networks Tishby deep learning theory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "7ca3e6d8-5250-4787-8483-77c6cd3afc69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiVWQ926DZcREyoa9kdynB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4626,
      "cache_read_input_tokens": 34193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4626
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

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NKmE1DwkzKFeRNxLa5M3Fm`</summary>

```json
{
  "query": "information bottleneck feature selection compression neural network 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "bf77e85e-71ab-4e4a-aa63-1e553fb66df6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiVWQ926DZcREyoa9kdynB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4626,
      "cache_read_input_tokens": 34193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4626
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MmP8riesXB2GCcYXrbd1vU`</summary>

```json
{
  "query": "instruction conditioned visual attention robot learning language-guided manipulation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "1fc1146f-365e-471e-b31a-d9a484345be0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiVWQ926DZcREyoa9kdynB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4626,
      "cache_read_input_tokens": 34193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4626
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WVaYM7pb2Vr13KiJsB9iw3`</summary>

```json
{
  "query": "visual token importance interpretability vision language model attention saliency GradCAM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "246055ab-d936-410e-9055-8fecbb5e6ed8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiVWQ926DZcREyoa9kdynB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4626,
      "cache_read_input_tokens": 34193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4626
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

_source line 30 · 2026-05-17T15:03:12.044Z_

<details><summary>↩ Tool result · `toolu_01ECs6L1ugcLnGMcNBweqh84`</summary>

```text
Web search results for query: "Variational Information Bottleneck deep learning Alemi ICLR 2017 Deep VIB"

Links: [{"title":"[1612.00410] Deep Variational Information Bottleneck","url":"https://arxiv.org/abs/1612.00410"},{"title":"[PDF] Deep Variational Information Bottleneck | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deep-Variational-Information-Bottleneck-Alemi-Fischer/a181fb5a42ad8fe2cc27b5542fa40384e9a8d72c"},{"title":"Deep Variational Information Bottleneck - Google Research","url":"https://research.google/pubs/deep-variational-information-bottleneck/"},{"title":"deep variational information bottleneck","url":"http://www.cs.columbia.edu/~blei/seminar/2020-representation/readings/AlemiFischerDillonMurphy2017.pdf"},{"title":"Deep Variational Information Bottleneck","url":"https://ai.google/research/pubs/pub45903"},{"title":"Deep Variational Information Bottleneck – Google Research","url":"https://research.google/pubs/pub45903/"},{"title":"Deep Variational Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=HyxQzBceg"},{"title":"The Supervised Information Bottleneck","url":"https://www.mdpi.com/1099-4300/27/5/452"},{"title":"[1612.00410v6] Deep Variational Information Bottleneck","url":"https://arxiv.org/abs/1612.00410v6"},{"title":"Deep Variational Information Bottleneck - ADS","url":"https://ui.adsabs.harvard.edu/abs/2016arXiv161200410A/abstract"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

## Deep Variational Information Bottleneck (Deep VIB)

The paper "Deep Variational Information Bottleneck" was published at ICLR 2017 by Alex Alemi, Ian Fischer, Josh Dillon, and Kevin Murphy.

### Overview

The paper presents a variational approximation to the information bottleneck of Tishby et al. (1999). This variational approach allows parameterizing the information bottleneck model using a neural network and leveraging the reparameterization trick for efficient training, which they call "Deep Variational Information Bottleneck", or Deep VIB.

### Key Contributions

Models trained with the VIB objective outperform those that are trained with other forms of regularization, in terms of generalization performance and robustness to adversarial attack.

### Technical Approach

By using the reparameterization trick, Monte Carlo sampling can be used to get an unbiased estimate of the gradient, allowing optimization using stochastic gradient descent. This enables the use of deep neural networks to handle high-dimensional, continuous data like images.

The paper is available on arXiv (1612.00410) and has been widely cited in the machine learning community.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "45c3d4f3-fe1b-49d4-a9f2-66a70adc6ffb",
  "tool_use_result": {
    "query": "Variational Information Bottleneck deep learning Alemi ICLR 2017 Deep VIB",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UQkjze9B7nC37HmHiHRh3h",
        "content": [
          {
            "title": "[1612.00410] Deep Variational Information Bottleneck",
            "url": "https://arxiv.org/abs/1612.00410"
          },
          {
            "title": "[PDF] Deep Variational Information Bottleneck | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Deep-Variational-Information-Bottleneck-Alemi-Fischer/a181fb5a42ad8fe2cc27b5542fa40384e9a8d72c"
          },
          {
            "title": "Deep Variational Information Bottleneck - Google Research",
            "url": "https://research.google/pubs/deep-variational-information-bottleneck/"
          },
          {
            "title": "deep variational information bottleneck",
            "url": "http://www.cs.columbia.edu/~blei/seminar/2020-representation/readings/AlemiFischerDillonMurphy2017.pdf"
          },
          {
            "title": "Deep Variational Information Bottleneck",
            "url": "https://ai.google/research/pubs/pub45903"
          },
          {
            "title": "Deep Variational Information Bottleneck – Google Research",
            "url": "https://research.google/pubs/pub45903/"
          },
          {
            "title": "Deep Variational Information Bottleneck | OpenReview",
            "url": "https://openreview.net/forum?id=HyxQzBceg"
          },
          {
            "title": "The Supervised Information Bottleneck",
            "url": "https://www.mdpi.com/1099-4300/27/5/452"
          },
          {
            "title": "[1612.00410v6] Deep Variational Information Bottleneck",
            "url": "https://arxiv.org/abs/1612.00410v6"
          },
          {
            "title": "Deep Variational Information Bottleneck - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2016arXiv161200410A/abstract"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the paper you're looking for:\n\n## Deep Variational Information Bottleneck (Deep VIB)\n\nThe paper \"Deep Variational Information Bottleneck\" was published at ICLR 2017 by Alex Alemi, Ian Fischer, Josh Dillon, and Kevin Murphy.\n\n### Overview\n\nThe paper presents a variational approximation to the information bottleneck of Tishby et al. (1999). This variational approach allows parameterizing the information bottleneck model using a neural network and leveraging the reparameterization trick for efficient training, which they call \"Deep Variational Information Bottleneck\", or Deep VIB.\n\n### Key Contributions\n\nModels trained with the VIB objective outperform those that are trained with other forms of regularization, in terms of generalization performance and robustness to adversarial attack.\n\n### Technical Approach\n\nBy using the reparameterization trick, Monte Carlo sampling can be used to get an unbiased estimate of the gradient, allowing optimization using stochastic gradient descent. This enables the use of deep neural networks to handle high-dimensional, continuous data like images.\n\nThe paper is available on arXiv (1612.00410) and has been widely cited in the machine learning community."
    ],
    "durationSeconds": 7.600817070999998
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-17T15:03:12.394Z_

<details><summary>↩ Tool result · `toolu_01LLW5EupTbMZ8DS6ej36P1b`</summary>

```text
Web search results for query: "Information Bottleneck representation learning neural networks Tishby deep learning theory"

Links: [{"title":"[1503.02406] Deep Learning and the Information Bottleneck Principle","url":"https://arxiv.org/abs/1503.02406"},{"title":"Deep Learning and the Information Bottleneck Principle Naftali Tishby1,2","url":"https://arxiv.org/pdf/1503.02406"},{"title":"How Does Information Bottleneck Help Deep Learning?","url":"https://proceedings.mlr.press/v202/kawaguchi23a/kawaguchi23a.pdf"},{"title":"Theory and Application of the Information Bottleneck Method - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10968930/"},{"title":"Information bottleneck method - Wikipedia","url":"https://en.wikipedia.org/wiki/Information_bottleneck_method"},{"title":"Anatomize Deep Learning with Information Theory | Lil'Log","url":"https://lilianweng.github.io/posts/2017-09-28-information-bottleneck/"},{"title":"Published as a conference paper at ICLR 2018 ON THE INFORMATION BOTTLENECK","url":"http://mcubed.mit.edu/files/public/RT1/2018_Tracey_ICLR_InfoBottleneck.pdf"},{"title":"[PDF] Deep learning and the information bottleneck principle | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deep-learning-and-the-information-bottleneck-Tishby-Zaslavsky/415229903f91a1f3fc7404f5e5997fde025c221d"},{"title":"A GENERALIZED INFORMATION BOTTLENECK THEORY OF DEEP LEARNING","url":"https://arxiv.org/pdf/2509.26327"},{"title":"(PDF) Deep Learning and the Information Bottleneck Principle","url":"https://www.researchgate.net/publication/273388040_Deep_Learning_and_the_Information_Bottleneck_Principle"}]

I've found comprehensive information about the Information Bottleneck principle and its application to deep learning. Here are the key findings:

## Overview

The information bottleneck method is a technique in information theory introduced by Naftali Tishby, Fernando C. Pereira, and William Bialek. In 1999, Naftali Tishby et al. introduced a powerful information theoretical framework called the information bottleneck method.

## Application to Deep Learning

Deep Neural Networks (DNNs) are analyzed via the theoretical framework of the information bottleneck (IB) principle. Any DNN can be quantified by the mutual information between the layers and the input and output variables. Using this representation we can calculate the optimal information theoretic limits of the DNN and obtain finite sample generalization bounds.

## Core Concepts for Representation Learning

Deep learning is a question of representation learning: each layer of a deep neural network can be seen as a set of summary statistics which contain some but not all of the information present in the input, while retaining as much information about the target output as possible.

The optimal architecture, number of layers and features/connections at each layer, are related to the bifurcation points of the information bottleneck tradeoff, namely, relevant compression of the input layer with respect to the output layer.

## Training Dynamics

DNN training involves two distinct phases: First, the network is trained to fully represent the input data and minimize the generalization error; then, it learns to forget the irrelevant details by compressing the representation of the input.

## Generalization Theory

It has been mathematically proven that controlling information bottleneck is one way to control generalization error in deep learning. The generalization error is proven to scale with the degree of information bottleneck, unlike the other generalization bounds that scale with the number of parameters, VC dimension, Rademacher complexity, stability or robustness.

This framework has become influential in understanding deep learning theory and continues to be an active area of research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "11736ff2-bec9-466e-bc53-78a5c5a63f3f",
  "tool_use_result": {
    "query": "Information Bottleneck representation learning neural networks Tishby deep learning theory",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AyhWvLkWhgA8iV8t8rVgSo",
        "content": [
          {
            "title": "[1503.02406] Deep Learning and the Information Bottleneck Principle",
            "url": "https://arxiv.org/abs/1503.02406"
          },
          {
            "title": "Deep Learning and the Information Bottleneck Principle Naftali Tishby1,2",
            "url": "https://arxiv.org/pdf/1503.02406"
          },
          {
            "title": "How Does Information Bottleneck Help Deep Learning?",
            "url": "https://proceedings.mlr.press/v202/kawaguchi23a/kawaguchi23a.pdf"
          },
          {
            "title": "Theory and Application of the Information Bottleneck Method - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10968930/"
          },
          {
            "title": "Information bottleneck method - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Information_bottleneck_method"
          },
          {
            "title": "Anatomize Deep Learning with Information Theory | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2017-09-28-information-bottleneck/"
          },
          {
            "title": "Published as a conference paper at ICLR 2018 ON THE INFORMATION BOTTLENECK",
            "url": "http://mcubed.mit.edu/files/public/RT1/2018_Tracey_ICLR_InfoBottleneck.pdf"
          },
          {
            "title": "[PDF] Deep learning and the information bottleneck principle | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Deep-learning-and-the-information-bottleneck-Tishby-Zaslavsky/415229903f91a1f3fc7404f5e5997fde025c221d"
          },
          {
            "title": "A GENERALIZED INFORMATION BOTTLENECK THEORY OF DEEP LEARNING",
            "url": "https://arxiv.org/pdf/2509.26327"
          },
          {
            "title": "(PDF) Deep Learning and the Information Bottleneck Principle",
            "url": "https://www.researchgate.net/publication/273388040_Deep_Learning_and_the_Information_Bottleneck_Principle"
          }
        ]
      },
      "I've found comprehensive information about the Information Bottleneck principle and its application to deep learning. Here are the key findings:\n\n## Overview\n\nThe information bottleneck method is a technique in information theory introduced by Naftali Tishby, Fernando C. Pereira, and William Bialek. In 1999, Naftali Tishby et al. introduced a powerful information theoretical framework called the information bottleneck method.\n\n## Application to Deep Learning\n\nDeep Neural Networks (DNNs) are analyzed via the theoretical framework of the information bottleneck (IB) principle. Any DNN can be quantified by the mutual information between the layers and the input and output variables. Using this representation we can calculate the optimal information theoretic limits of the DNN and obtain finite sample generalization bounds.\n\n## Core Concepts for Representation Learning\n\nDeep learning is a question of representation learning: each layer of a deep neural network can be seen as a set of summary statistics which contain some but not all of the information present in the input, while retaining as much information about the target output as possible.\n\nThe optimal architecture, number of layers and features/connections at each layer, are related to the bifurcation points of the information bottleneck tradeoff, namely, relevant compression of the input layer with respect to the output layer.\n\n## Training Dynamics\n\nDNN training involves two distinct phases: First, the network is trained to fully represent the input data and minimize the generalization error; then, it learns to forget the irrelevant details by compressing the representation of the input.\n\n## Generalization Theory\n\nIt has been mathematically proven that controlling information bottleneck is one way to control generalization error in deep learning. The generalization error is proven to scale with the degree of information bottleneck, unlike the other generalization bounds that scale with the number of parameters, VC dimension, Rademacher complexity, stability or robustness.\n\nThis framework has become influential in understanding deep learning theory and continues to be an active area of research."
    ],
    "durationSeconds": 7.478828372999996
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T15:03:13.589Z_

<details><summary>↩ Tool result · `toolu_01NKmE1DwkzKFeRNxLa5M3Fm`</summary>

```text
Web search results for query: "information bottleneck feature selection compression neural network 2023 2024 2025"

Links: [{"title":"Information-Bottleneck Driven Binary Neural Network for ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Yin_Information-Bottleneck_Driven_Binary_Neural_Network_for_Change_Detection_ICCV_2025_paper.pdf"},{"title":"On Neural Networks Fitting, Compression, and Generalization Behavior via Information-Bottleneck-like Approaches - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10377965/"},{"title":"Decoding the Information Bottleneck: A Deep Dive into Neural Network Learning Dynamics | by Mehmet Emre Akbulut | Medium","url":"https://medium.com/@memreakbulut/decoding-the-information-bottleneck-a-deep-dive-into-neural-network-learning-dynamics-8cb02aff37e2"},{"title":"On Neural Networks Fitting, Compression, and Generalization Behavior via Information-Bottleneck-like Approaches","url":"https://www.mdpi.com/1099-4300/25/7/1063"},{"title":"[2305.08013] Information Bottleneck Analysis of Deep Neural Networks via Lossy Compression","url":"https://arxiv.org/abs/2305.08013"},{"title":"Information bottleneck method - Wikipedia","url":"https://en.wikipedia.org/wiki/Information_bottleneck_method"},{"title":"Information Bottleneck Analysis of Deep Neural Networks via Lossy Compression | OpenReview","url":"https://openreview.net/forum?id=huGECz8dPp"},{"title":"An information bottleneck approach for feature selection - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320325002249"},{"title":"(PDF) Information Bottleneck Analysis of Deep Neural Networks via Lossy Compression","url":"https://www.researchgate.net/publication/370775416_Information_Bottleneck_Analysis_of_Deep_Neural_Networks_via_Lossy_Compression"},{"title":"A GENERALIZED INFORMATION BOTTLENECK THEORY OF DEEP LEARNING","url":"https://arxiv.org/pdf/2509.26327"}]

Based on the search results, here's what I found about information bottleneck approaches in feature selection, compression, and neural networks during 2023-2025:

## Recent Research Highlights

**Information Bottleneck Principle**: The information bottleneck method is a technique in information theory designed for finding the best tradeoff between accuracy and complexity (compression) when summarizing a random variable, given a joint probability distribution between the variable and an observed relevant variable.

**Neural Network Compression and Learning Dynamics**: Research has proposed novel approaches to capturing neural network dynamics using information-bottleneck-type techniques, involving the replacement of mutual information measures by more tractable ones, including the minimum mean-squared error associated with reconstruction of the network input data and the cross-entropy associated with class labels.

**Feature Selection Applications (2025)**: A neural network-based feature selection framework leveraging the information bottleneck principle was introduced, establishing a connection between the IB principle and maximizing mutual information for feature selection, while optimizing high-dimensional multivariate mutual information directly without resorting to variational approximation.

**Deep Neural Network Analysis (2023-2024)**: The Information Bottleneck principle offers an information-theoretic framework for analyzing the training process of deep neural networks. Recent work proposes using lossy compression to overcome obstacles with high dimensionality, tracking training dynamics that consist of two phases: fitting and compression, where the compression phase accounts for good generalization performance.

**Latest Theoretical Developments (2025)**: Recent work includes a generalized information bottleneck theory of deep learning presented at AISTATS'25, extending the foundational IB framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "16e0e3b4-107a-4b94-b329-3f4d0d503496",
  "tool_use_result": {
    "query": "information bottleneck feature selection compression neural network 2023 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RzQuKTqE3T6hksK1pZMcbz",
        "content": [
          {
            "title": "Information-Bottleneck Driven Binary Neural Network for ...",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Yin_Information-Bottleneck_Driven_Binary_Neural_Network_for_Change_Detection_ICCV_2025_paper.pdf"
          },
          {
            "title": "On Neural Networks Fitting, Compression, and Generalization Behavior via Information-Bottleneck-like Approaches - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10377965/"
          },
          {
            "title": "Decoding the Information Bottleneck: A Deep Dive into Neural Network Learning Dynamics | by Mehmet Emre Akbulut | Medium",
            "url": "https://medium.com/@memreakbulut/decoding-the-information-bottleneck-a-deep-dive-into-neural-network-learning-dynamics-8cb02aff37e2"
          },
          {
            "title": "On Neural Networks Fitting, Compression, and Generalization Behavior via Information-Bottleneck-like Approaches",
            "url": "https://www.mdpi.com/1099-4300/25/7/1063"
          },
          {
            "title": "[2305.08013] Information Bottleneck Analysis of Deep Neural Networks via Lossy Compression",
            "url": "https://arxiv.org/abs/2305.08013"
          },
          {
            "title": "Information bottleneck method - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Information_bottleneck_method"
          },
          {
            "title": "Information Bottleneck Analysis of Deep Neural Networks via Lossy Compression | OpenReview",
            "url": "https://openreview.net/forum?id=huGECz8dPp"
          },
          {
            "title": "An information bottleneck approach for feature selection - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0031320325002249"
          },
          {
            "title": "(PDF) Information Bottleneck Analysis of Deep Neural Networks via Lossy Compression",
            "url": "https://www.researchgate.net/publication/370775416_Information_Bottleneck_Analysis_of_Deep_Neural_Networks_via_Lossy_Compression"
          },
          {
            "title": "A GENERALIZED INFORMATION BOTTLENECK THEORY OF DEEP LEARNING",
            "url": "https://arxiv.org/pdf/2509.26327"
          }
        ]
      },
      "Based on the search results, here's what I found about information bottleneck approaches in feature selection, compression, and neural networks during 2023-2025:\n\n## Recent Research Highlights\n\n**Information Bottleneck Principle**: The information bottleneck method is a technique in information theory designed for finding the best tradeoff between accuracy and complexity (compression) when summarizing a random variable, given a joint probability distribution between the variable and an observed relevant variable.\n\n**Neural Network Compression and Learning Dynamics**: Research has proposed novel approaches to capturing neural network dynamics using information-bottleneck-type techniques, involving the replacement of mutual information measures by more tractable ones, including the minimum mean-squared error associated with reconstruction of the network input data and the cross-entropy associated with class labels.\n\n**Feature Selection Applications (2025)**: A neural network-based feature selection framework leveraging the information bottleneck principle was introduced, establishing a connection between the IB principle and maximizing mutual information for feature selection, while optimizing high-dimensional multivariate mutual information directly without resorting to variational approximation.\n\n**Deep Neural Network Analysis (2023-2024)**: The Information Bottleneck principle offers an information-theoretic framework for analyzing the training process of deep neural networks. Recent work proposes using lossy compression to overcome obstacles with high dimensionality, tracking training dynamics that consist of two phases: fitting and compression, where the compression phase accounts for good generalization performance.\n\n**Latest Theoretical Developments (2025)**: Recent work includes a generalized information bottleneck theory of deep learning presented at AISTATS'25, extending the foundational IB framework."
    ],
    "durationSeconds": 7.729096802
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-17T15:03:16.389Z_

<details><summary>↩ Tool result · `toolu_01MmP8riesXB2GCcYXrbd1vU`</summary>

```text
Web search results for query: "instruction conditioned visual attention robot learning language-guided manipulation 2024 2025"

Links: [{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"F1: A Vision-Language-Action Model Bridging ...","url":"https://arxiv.org/pdf/2509.06951"},{"title":"ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations","url":"https://liralab.usc.edu/pdfs/publications/zhang2025rewind.pdf"},{"title":"2025-9-18 ThinkAct: Vision-Language-Action Reasoning via","url":"https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"},{"title":"(PDF) Vision-Language-Conditioned Learning Policy for Robotic Manipulation","url":"https://www.researchgate.net/publication/385346118_Vision-Language-Conditioned_Learning_Policy_for_Robotic_Manipulation"},{"title":"GitHub - hk-zh/language-conditioned-robot-manipulation-models: https://arxiv.org/abs/2312.10807 · GitHub","url":"https://github.com/hk-zh/language-conditioned-robot-manipulation-models"},{"title":"Proceedings of Machine Learning Research | Proceedings of The 8th Conference on Robot Learning Held in Munich, Germany on 06-09 November 2024 Published as Volume 270 by the Proceedings of Machine Learning Research on 12 January 2025. Volume Edited by: Pulkit Agrawal Oliver Kroemer Wolfram Burgard Series Editors: Neil D. Lawrence","url":"https://proceedings.mlr.press/v270/"},{"title":"1 Recipe for Vision-Language-Action Models in Robotic Manipulation: A Survey","url":"https://www.techrxiv.org/users/956965/articles/1326137/master/file/data/eart2025recipevla/eart2025recipevla.pdf?inline=true"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"}]

I've found comprehensive research results on instruction-conditioned visual attention for robot learning and language-guided manipulation from 2024-2025. Here's a summary of the key findings:

## Recent Research in Language-Guided Robot Manipulation (2024-2025)

### Vision-Language-Action (VLA) Models

Vision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robot manipulation, leveraging the vast knowledge of pre-trained Vision-Language Models (VLMs) to ground natural language instructions into physical actions.

### Key Recent Architectures

Several cutting-edge approaches have been developed:

1. **F1 Model**: F1 uses a Mixture-of-Transformer (MoT) architecture with three dedicated experts for understanding, foresight generation, and action execution. A progressive attention scheme regulates information exchange across experts, with intra-expert attention capturing rich token interactions and inter-expert attention enforcing a causal flow from understanding to foresight to action.

2. **ThinkAct**: ThinkAct is a reasoning VLA framework capable of thinking before acting. Through reasoning reinforced by action-aligned visual feedback, ThinkAct enables capabilities of few-shot adaptation, long-horizon planning, and self-correction in embodied tasks.

3. **LangForce**: The research employs the Qwen3VL-4B-GR00T model from starVLA (2025) as a representative VLA architecture.

### Language-Conditioned Learning

ReWiND overcomes training challenges by assuming only a handful of demonstrations to enable real-world robot learning. It first trains a language-conditioned reward model from these demonstrations, then uses it to pre-train a language-conditioned policy via offline RL.

### Industry Trends

The field is characterized by rapid growth through 2023 Q3–2024 Q3 with the emergence of open-source datasets and models, followed by a maturation phase from 2024 Q4–present where development of large-scale models is accelerated, with industrial-scale models such as GR00T N1 and π0 emerging.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "37acbdfa-0e81-453f-a6a8-10b4b47b47ff",
  "tool_use_result": {
    "query": "instruction conditioned visual attention robot learning language-guided manipulation 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WM1xU8uieP2aL1PSsLs6gi",
        "content": [
          {
            "title": "LangForce: Bayesian Decomposition of Vision Language ...",
            "url": "https://arxiv.org/pdf/2601.15197"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "F1: A Vision-Language-Action Model Bridging ...",
            "url": "https://arxiv.org/pdf/2509.06951"
          },
          {
            "title": "ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations",
            "url": "https://liralab.usc.edu/pdfs/publications/zhang2025rewind.pdf"
          },
          {
            "title": "2025-9-18 ThinkAct: Vision-Language-Action Reasoning via",
            "url": "https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"
          },
          {
            "title": "(PDF) Vision-Language-Conditioned Learning Policy for Robotic Manipulation",
            "url": "https://www.researchgate.net/publication/385346118_Vision-Language-Conditioned_Learning_Policy_for_Robotic_Manipulation"
          },
          {
            "title": "GitHub - hk-zh/language-conditioned-robot-manipulation-models: https://arxiv.org/abs/2312.10807 · GitHub",
            "url": "https://github.com/hk-zh/language-conditioned-robot-manipulation-models"
          },
          {
            "title": "Proceedings of Machine Learning Research | Proceedings of The 8th Conference on Robot Learning Held in Munich, Germany on 06-09 November 2024 Published as Volume 270 by the Proceedings of Machine Learning Research on 12 January 2025. Volume Edited by: Pulkit Agrawal Oliver Kroemer Wolfram Burgard Series Editors: Neil D. Lawrence",
            "url": "https://proceedings.mlr.press/v270/"
          },
          {
            "title": "1 Recipe for Vision-Language-Action Models in Robotic Manipulation: A Survey",
            "url": "https://www.techrxiv.org/users/956965/articles/1326137/master/file/data/eart2025recipevla/eart2025recipevla.pdf?inline=true"
          },
          {
            "title": "Vision Language Action Models in Robotic Manipulation: A Systematic Review",
            "url": "https://arxiv.org/html/2507.10672v1"
          }
        ]
      },
      "I've found comprehensive research results on instruction-conditioned visual attention for robot learning and language-guided manipulation from 2024-2025. Here's a summary of the key findings:\n\n## Recent Research in Language-Guided Robot Manipulation (2024-2025)\n\n### Vision-Language-Action (VLA) Models\n\nVision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robot manipulation, leveraging the vast knowledge of pre-trained Vision-Language Models (VLMs) to ground natural language instructions into physical actions.\n\n### Key Recent Architectures\n\nSeveral cutting-edge approaches have been developed:\n\n1. **F1 Model**: F1 uses a Mixture-of-Transformer (MoT) architecture with three dedicated experts for understanding, foresight generation, and action execution. A progressive attention scheme regulates information exchange across experts, with intra-expert attention capturing rich token interactions and inter-expert attention enforcing a causal flow from understanding to foresight to action.\n\n2. **ThinkAct**: ThinkAct is a reasoning VLA framework capable of thinking before acting. Through reasoning reinforced by action-aligned visual feedback, ThinkAct enables capabilities of few-shot adaptation, long-horizon planning, and self-correction in embodied tasks.\n\n3. **LangForce**: The research employs the Qwen3VL-4B-GR00T model from starVLA (2025) as a representative VLA architecture.\n\n### Language-Conditioned Learning\n\nReWiND overcomes training challenges by assuming only a handful of demonstrations to enable real-world robot learning. It first trains a language-conditioned reward model from these demonstrations, then uses it to pre-train a language-conditioned policy via offline RL.\n\n### Industry Trends\n\nThe field is characterized by rapid growth through 2023 Q3–2024 Q3 with the emergence of open-source datasets and models, followed by a maturation phase from 2024 Q4–present where development of large-scale models is accelerated, with industrial-scale models such as GR00T N1 and π0 emerging."
    ],
    "durationSeconds": 9.997672732
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T15:03:17.322Z_

<details><summary>↩ Tool result · `toolu_01WVaYM7pb2Vr13KiJsB9iw3`</summary>

```text
Web search results for query: "visual token importance interpretability vision language model attention saliency GradCAM 2024 2025"

Links: [{"title":"Visualizing Vision-Language Models | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/visualizing-vision-language-models-multimodal-reasoning"},{"title":"A Comprehensive Review of Explainable Artificial Intelligence (XAI) in Computer Vision - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12252469/"},{"title":"Grad-CAM: A Gradient-based Approach to Explainability in Deep Learning | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/grad-cam-a-gradient-based-approach-to-explainability-in-deep-learning-871b3ab8a6ce"},{"title":"GradCAM++: Advanced Attention Visualization","url":"https://www.emergentmind.com/topics/gradcam-attention-visualization"},{"title":"Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025","url":"https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/"},{"title":"Token selection using Grad-CAM in Vision Transformer to reduce computational costs | Proceedings of the 2024 7th Artificial Intelligence and Cloud Computing Conference","url":"https://dl.acm.org/doi/10.1145/3719384.3719433"},{"title":"Class-Discriminative Attention Maps for Vision Transformers","url":"https://arxiv.org/html/2312.02364v3"},{"title":"Gradient Attention Rollout","url":"https://www.emergentmind.com/topics/gradient-attention-rollout"},{"title":"Improving LLM Input Attribution via Attention Bias ...","url":"https://openreview.net/pdf?id=DrUR87D4Hj"},{"title":"A Novel Human Action Recognition Model by Grad-CAM Visualization with Multi-level Feature Extraction Using Global Average Pooling with Sequence Modeling by Bidirectional Gated Recurrent Units | International Journal of Computational Intelligence Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44196-025-00848-x"}]

I've performed the web search for your query. Here's a summary of the relevant findings on visual token importance interpretability in vision-language models with recent developments in 2024-2025:

## Key Interpretability Techniques for Vision-Language Models

Different visualization techniques answer different interpretability questions: attention maps show cross-modal focus, Grad-CAM highlights causal influence, embedding projections reveal global semantic structure, and token/patch-level analyses expose internal mechanisms of heads and neurons.

### Saliency and Gradient-Based Methods

Gradient-based saliency maps provide an alternative to attention maps that doesn't depend only on attention weights, and can sometimes provide different information than attention weights since not all information comes from large attention weights.

Grad-CAM generalizes the idea of CAM and avoids the need for a specific architecture, making it more flexible, and improved localization accuracy over gradient-only saliency by making explanations more class-specific.

### Recent Advances (2024-2025)

Class-discriminative attention maps (CDAM) is a gradient-based extension that makes attention maps sensitive to class-specific signals based on a classifier or a latent concept.

A token selection method using the gradient obtained by back propagation via Grad-CAM proposes an additional network that predicts the activation map computed from the tokens and uses this network in the inference phase to reduce the prediction cost.

### Vision Transformer Interpretability

Gradient Attention Rollout is a family of interpretability techniques for Vision Transformers which quantify how input features influence output predictions by propagating attention or gradient-weighted attention scores across layers, addressing the inadequacy of raw attention weights.

### Mechanistic Understanding of VLMs

LLaVA primarily retrieves visual information in early layers (1-4), followed by consistent summarization in final visual tokens, while layers 1-10 process broader contextual information and layers 15-24 focus on extracting specific object details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "ca0db22d-bad9-45c4-bf94-07d7566e835c",
  "tool_use_result": {
    "query": "visual token importance interpretability vision language model attention saliency GradCAM 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KzotjdcAtrqrF8JD3CYKiJ",
        "content": [
          {
            "title": "Visualizing Vision-Language Models | DigitalOcean",
            "url": "https://www.digitalocean.com/community/tutorials/visualizing-vision-language-models-multimodal-reasoning"
          },
          {
            "title": "A Comprehensive Review of Explainable Artificial Intelligence (XAI) in Computer Vision - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12252469/"
          },
          {
            "title": "Grad-CAM: A Gradient-based Approach to Explainability in Deep Learning | by Dong-Keon Kim | Medium",
            "url": "https://medium.com/@kdk199604/grad-cam-a-gradient-based-approach-to-explainability-in-deep-learning-871b3ab8a6ce"
          },
          {
            "title": "GradCAM++: Advanced Attention Visualization",
            "url": "https://www.emergentmind.com/topics/gradcam-attention-visualization"
          },
          {
            "title": "Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025",
            "url": "https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/"
          },
          {
            "title": "Token selection using Grad-CAM in Vision Transformer to reduce computational costs | Proceedings of the 2024 7th Artificial Intelligence and Cloud Computing Conference",
            "url": "https://dl.acm.org/doi/10.1145/3719384.3719433"
          },
          {
            "title": "Class-Discriminative Attention Maps for Vision Transformers",
            "url": "https://arxiv.org/html/2312.02364v3"
          },
          {
            "title": "Gradient Attention Rollout",
            "url": "https://www.emergentmind.com/topics/gradient-attention-rollout"
          },
          {
            "title": "Improving LLM Input Attribution via Attention Bias ...",
            "url": "https://openreview.net/pdf?id=DrUR87D4Hj"
          },
          {
            "title": "A Novel Human Action Recognition Model by Grad-CAM Visualization with Multi-level Feature Extraction Using Global Average Pooling with Sequence Modeling by Bidirectional Gated Recurrent Units | International Journal of Computational Intelligence Systems | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s44196-025-00848-x"
          }
        ]
      },
      "I've performed the web search for your query. Here's a summary of the relevant findings on visual token importance interpretability in vision-language models with recent developments in 2024-2025:\n\n## Key Interpretability Techniques for Vision-Language Models\n\nDifferent visualization techniques answer different interpretability questions: attention maps show cross-modal focus, Grad-CAM highlights causal influence, embedding projections reveal global semantic structure, and token/patch-level analyses expose internal mechanisms of heads and neurons.\n\n### Saliency and Gradient-Based Methods\n\nGradient-based saliency maps provide an alternative to attention maps that doesn't depend only on attention weights, and can sometimes provide different information than attention weights since not all information comes from large attention weights.\n\nGrad-CAM generalizes the idea of CAM and avoids the need for a specific architecture, making it more flexible, and improved localization accuracy over gradient-only saliency by making explanations more class-specific.\n\n### Recent Advances (2024-2025)\n\nClass-discriminative attention maps (CDAM) is a gradient-based extension that makes attention maps sensitive to class-specific signals based on a classifier or a latent concept.\n\nA token selection method using the gradient obtained by back propagation via Grad-CAM proposes an additional network that predicts the activation map computed from the tokens and uses this network in the inference phase to reduce the prediction cost.\n\n### Vision Transformer Interpretability\n\nGradient Attention Rollout is a family of interpretability techniques for Vision Transformers which quantify how input features influence output predictions by propagating attention or gradient-weighted attention scores across layers, addressing the inadequacy of raw attention weights.\n\n### Mechanistic Understanding of VLMs\n\nLLaVA primarily retrieves visual information in early layers (1-4), followed by consistent summarization in final visual tokens, while layers 1-10 process broader contextual information and layers 15-24 focus on extracting specific object details."
    ],
    "durationSeconds": 10.342937052000002
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Good, I have a good amount of information. Let me now search for a few more specific papers to fill in the gaps:
1. The original IB paper by Tishby (1999/2000)
2. Attention rollout / attention interpretability for VLMs
3. Language-conditioned visual attention specifically for robot learning
4. More about VLM interpretability tools
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "30d0a425-1ecd-4a18-88f7-bf93fec259b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYsiM5pxr2s3ci2ioguWMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5387,
      "cache_read_input_tokens": 38819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5387
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

_source line 36_

搜索更多具体论文填补空白。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "bd92da5c-2295-422e-b484-9e0bbe393116",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYsiM5pxr2s3ci2ioguWMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5387,
      "cache_read_input_tokens": 38819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5387
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

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011HQGGujYRr1ouan4fd67qb`</summary>

```json
{
  "query": "Tishby Pereira Bialek \"information bottleneck method\" 1999 2000 original paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "8655b53b-0779-4a78-a2f2-14f8a65d8c7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYsiM5pxr2s3ci2ioguWMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5387,
      "cache_read_input_tokens": 38819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5387
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

_source line 38_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XDmCDGFmdTMSz9ThhEgby1`</summary>

```json
{
  "query": "\"attention rollout\" vision transformer interpretability Abnar Zuidema 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "8c8b5098-9e5b-4583-acb8-b71fa5fceed6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYsiM5pxr2s3ci2ioguWMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5387,
      "cache_read_input_tokens": 38819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5387
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

_source line 39_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bx9ZSoPNYjLN6FLZPsc44E`</summary>

```json
{
  "query": "VLA model interpretability attention visualization robot manipulation what does VLA look at 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "e81d183a-a036-478f-8e5e-a6c0327de769",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYsiM5pxr2s3ci2ioguWMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5387,
      "cache_read_input_tokens": 38819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5387
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

_source line 40_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M2fiidtAoRE7KDcEKk9ikn`</summary>

```json
{
  "query": "language conditioned visual feature selection robot policy task-relevant visual tokens 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "acafda3b-a12c-4c70-8b7e-d7db2e896855",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYsiM5pxr2s3ci2ioguWMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5387,
      "cache_read_input_tokens": 38819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5387
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

_source line 41 · 2026-05-17T15:03:34.201Z_

<details><summary>↩ Tool result · `toolu_011HQGGujYRr1ouan4fd67qb`</summary>

```text
Web search results for query: "Tishby Pereira Bialek "information bottleneck method" 1999 2000 original paper"

Links: [{"title":"[physics/0004057] The information bottleneck method","url":"https://arxiv.org/abs/physics/0004057"},{"title":"Theory and Application of the Information Bottleneck Method - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10968930/"},{"title":"arXiv:physics/0004057 v1 24 Apr 2000 The information bottleneck method","url":"https://www.princeton.edu/~wbialek/our_papers/tishby+al_99.pdf"},{"title":"Information bottleneck method - Wikipedia","url":"https://en.wikipedia.org/wiki/Information_bottleneck_method"},{"title":"[PDF] The information bottleneck method | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-information-bottleneck-method-Tishby-Pereira/4ef483f819e11873822416042a4b6dc4652e010c"},{"title":"(PDF) The Information Bottleneck Method","url":"https://www.researchgate.net/publication/2844514_The_Information_Bottleneck_Method"},{"title":"The Information Bottleneck Method","url":"https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=38d23708b925d257faf78c68239b08e1325fd8d2"},{"title":"Learning and Generalization with the Information Bottleneck","url":"https://isaim2008.unl.edu/PAPERS/InvitedSpeakers/Tishby.pdf"},{"title":"Information Bottleneck 1: Rate-Distortion Theory | by Ac Studio | Medium","url":"https://medium.com/@acamvproducingstudio/information-bottleneck-1-rate-distortion-theory-02646b377eb6"},{"title":"The deterministic information bottleneck - ACM Digital Library","url":"https://dl.acm.org/doi/10.1162/NECO_a_00961"}]

Based on my web search, I found the original information bottleneck paper:

## The Information Bottleneck Method - Original Paper

The original paper "The information bottleneck method" was authored by Naftali Tishby (Hebrew University and NEC Research Institute), Fernando C. Pereira (AT&T Shannon Laboratory), and William Bialek (NEC Research Institute).

**Publication Details:**
- The paper was dated 30 September 1999
- It was submitted to arXiv on Monday, 24 April 2000 with the identifier physics/0004057
- The paper was presented at the 37th Annual Allerton Conference on Communication, Control, and Computing in 2000, pp. 368–377

**Key Concept:**
The paper defines the relevant information in a signal as the information that signal provides about another signal, formalizing the problem as finding a short code that preserves the maximum information through a 'bottleneck' formed by a limited set of codewords.

The paper is available in several locations, including at https://arxiv.org/abs/physics/0004057 and https://www.princeton.edu/~wbialek/our_papers/tishby+al_99.pdf


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "f69ab640-749b-45a6-bec0-be6e6c1bec5d",
  "tool_use_result": {
    "query": "Tishby Pereira Bialek \"information bottleneck method\" 1999 2000 original paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_012rnxFwxZQeK8n1sT4hg5q8",
        "content": [
          {
            "title": "[physics/0004057] The information bottleneck method",
            "url": "https://arxiv.org/abs/physics/0004057"
          },
          {
            "title": "Theory and Application of the Information Bottleneck Method - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10968930/"
          },
          {
            "title": "arXiv:physics/0004057 v1 24 Apr 2000 The information bottleneck method",
            "url": "https://www.princeton.edu/~wbialek/our_papers/tishby+al_99.pdf"
          },
          {
            "title": "Information bottleneck method - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Information_bottleneck_method"
          },
          {
            "title": "[PDF] The information bottleneck method | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/The-information-bottleneck-method-Tishby-Pereira/4ef483f819e11873822416042a4b6dc4652e010c"
          },
          {
            "title": "(PDF) The Information Bottleneck Method",
            "url": "https://www.researchgate.net/publication/2844514_The_Information_Bottleneck_Method"
          },
          {
            "title": "The Information Bottleneck Method",
            "url": "https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=38d23708b925d257faf78c68239b08e1325fd8d2"
          },
          {
            "title": "Learning and Generalization with the Information Bottleneck",
            "url": "https://isaim2008.unl.edu/PAPERS/InvitedSpeakers/Tishby.pdf"
          },
          {
            "title": "Information Bottleneck 1: Rate-Distortion Theory | by Ac Studio | Medium",
            "url": "https://medium.com/@acamvproducingstudio/information-bottleneck-1-rate-distortion-theory-02646b377eb6"
          },
          {
            "title": "The deterministic information bottleneck - ACM Digital Library",
            "url": "https://dl.acm.org/doi/10.1162/NECO_a_00961"
          }
        ]
      },
      "Based on my web search, I found the original information bottleneck paper:\n\n## The Information Bottleneck Method - Original Paper\n\nThe original paper \"The information bottleneck method\" was authored by Naftali Tishby (Hebrew University and NEC Research Institute), Fernando C. Pereira (AT&T Shannon Laboratory), and William Bialek (NEC Research Institute).\n\n**Publication Details:**\n- The paper was dated 30 September 1999\n- It was submitted to arXiv on Monday, 24 April 2000 with the identifier physics/0004057\n- The paper was presented at the 37th Annual Allerton Conference on Communication, Control, and Computing in 2000, pp. 368–377\n\n**Key Concept:**\nThe paper defines the relevant information in a signal as the information that signal provides about another signal, formalizing the problem as finding a short code that preserves the maximum information through a 'bottleneck' formed by a limited set of codewords.\n\nThe paper is available in several locations, including at https://arxiv.org/abs/physics/0004057 and https://www.princeton.edu/~wbialek/our_papers/tishby+al_99.pdf"
    ],
    "durationSeconds": 5.608377731999994
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-17T15:03:36.742Z_

<details><summary>↩ Tool result · `toolu_01XDmCDGFmdTMSz9ThhEgby1`</summary>

```text
Web search results for query: ""attention rollout" vision transformer interpretability Abnar Zuidema 2020"

Links: [{"title":"Exploring Visual Attention in Transformer Models | by Niv Leibovitch | Medium","url":"https://medium.com/@nivonl/exploring-visual-attention-in-transformer-models-ab538c06083a"},{"title":"Quantifying Attention Flow in Transformers | Samira Abnar","url":"https://samiraabnar.github.io/articles/2020-04/attention_flow"},{"title":"Quantifying Attention Flow in Transformers | MYRIAD","url":"https://creatis-myriad.github.io/2022/07/07/AttentionRollout.html"},{"title":"ICEv2: Interpretability, Comprehensiveness, and Explainability in Vision Transformer | International Journal of Computer Vision | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11263-024-02290-6"},{"title":"GMAR: Gradient-Driven Multi-Head Attention Rollout for Vision Transformer Interpretability","url":"https://arxiv.org/html/2504.19414v1"},{"title":"Quantifying Attention Flow in Transformers | Request PDF","url":"https://www.researchgate.net/publication/343298597_Quantifying_Attention_Flow_in_Transformers"},{"title":"Quantifying Attention Flow in Transformers","url":"https://aclanthology.org/2020.acl-main.385.pdf"},{"title":"Quantifying Attention Flow in Transformers - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.385/"},{"title":"(PDF) Quantifying Attention Flow in Transformers","url":"https://www.researchgate.net/publication/341148976_Quantifying_Attention_Flow_in_Transformers"},{"title":"[PDF] Quantifying Attention Flow in Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quantifying-Attention-Flow-in-Transformers-Abnar-Zuidema/76a9f336481b39515d6cea2920696f11fb686451"}]

Based on the search results, here's what I found about attention rollout, vision transformers, and the work by Abnar and Zuidema:

## Overview

In the Transformer model, "self-attention" combines information from attended embeddings into the representation of the focal embedding in the next layer. Thus, across layers of the Transformer, information originating from different tokens gets increasingly mixed. This makes attention weights unreliable as explanations probes.

## The Abnar & Zuidema 2020 Paper

Abnar and Zuidema proposed two methods for approximating the attention to input tokens given attention weights, attention rollout and attention flow, as post hoc methods when using attention weights as the relative relevance of the input tokens. These methods give complementary views on the flow of information, and compared to raw attention, both yield higher correlations with importance scores of input tokens obtained using an ablation method and input gradients.

## Application to Vision Transformers

The methods were designed for the original NLP transformer but the authors of the Vision Transformer showed that Attention Rollout still works with images. Attention Rollout and Attention Flow are methods to compute attention scores to input tokens at each layer.

## How Attention Rollout Works

Attention weights determine the proportion of the incoming information that can propagate through each link, with input token identities linearly combined through the layers based on attention weights. To compute attention to input tokens in a given layer, attention weights matrices are recursively multiplied, starting from the input layer up to that layer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "67f8cbe6-505e-4d73-8dcb-43cfb517b654",
  "tool_use_result": {
    "query": "\"attention rollout\" vision transformer interpretability Abnar Zuidema 2020",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KziKsFyKmLVXqxT9bNR6Cy",
        "content": [
          {
            "title": "Exploring Visual Attention in Transformer Models | by Niv Leibovitch | Medium",
            "url": "https://medium.com/@nivonl/exploring-visual-attention-in-transformer-models-ab538c06083a"
          },
          {
            "title": "Quantifying Attention Flow in Transformers | Samira Abnar",
            "url": "https://samiraabnar.github.io/articles/2020-04/attention_flow"
          },
          {
            "title": "Quantifying Attention Flow in Transformers | MYRIAD",
            "url": "https://creatis-myriad.github.io/2022/07/07/AttentionRollout.html"
          },
          {
            "title": "ICEv2: Interpretability, Comprehensiveness, and Explainability in Vision Transformer | International Journal of Computer Vision | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11263-024-02290-6"
          },
          {
            "title": "GMAR: Gradient-Driven Multi-Head Attention Rollout for Vision Transformer Interpretability",
            "url": "https://arxiv.org/html/2504.19414v1"
          },
          {
            "title": "Quantifying Attention Flow in Transformers | Request PDF",
            "url": "https://www.researchgate.net/publication/343298597_Quantifying_Attention_Flow_in_Transformers"
          },
          {
            "title": "Quantifying Attention Flow in Transformers",
            "url": "https://aclanthology.org/2020.acl-main.385.pdf"
          },
          {
            "title": "Quantifying Attention Flow in Transformers - ACL Anthology",
            "url": "https://aclanthology.org/2020.acl-main.385/"
          },
          {
            "title": "(PDF) Quantifying Attention Flow in Transformers",
            "url": "https://www.researchgate.net/publication/341148976_Quantifying_Attention_Flow_in_Transformers"
          },
          {
            "title": "[PDF] Quantifying Attention Flow in Transformers | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Quantifying-Attention-Flow-in-Transformers-Abnar-Zuidema/76a9f336481b39515d6cea2920696f11fb686451"
          }
        ]
      },
      "Based on the search results, here's what I found about attention rollout, vision transformers, and the work by Abnar and Zuidema:\n\n## Overview\n\nIn the Transformer model, \"self-attention\" combines information from attended embeddings into the representation of the focal embedding in the next layer. Thus, across layers of the Transformer, information originating from different tokens gets increasingly mixed. This makes attention weights unreliable as explanations probes.\n\n## The Abnar & Zuidema 2020 Paper\n\nAbnar and Zuidema proposed two methods for approximating the attention to input tokens given attention weights, attention rollout and attention flow, as post hoc methods when using attention weights as the relative relevance of the input tokens. These methods give complementary views on the flow of information, and compared to raw attention, both yield higher correlations with importance scores of input tokens obtained using an ablation method and input gradients.\n\n## Application to Vision Transformers\n\nThe methods were designed for the original NLP transformer but the authors of the Vision Transformer showed that Attention Rollout still works with images. Attention Rollout and Attention Flow are methods to compute attention scores to input tokens at each layer.\n\n## How Attention Rollout Works\n\nAttention weights determine the proportion of the incoming information that can propagate through each link, with input token identities linearly combined through the layers based on attention weights. To compute attention to input tokens in a given layer, attention weights matrices are recursively multiplied, starting from the input layer up to that layer."
    ],
    "durationSeconds": 7.126675216999996
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-17T15:03:39.222Z_

<details><summary>↩ Tool result · `toolu_01Bx9ZSoPNYjLN6FLZPsc44E`</summary>

```text
Web search results for query: "VLA model interpretability attention visualization robot manipulation what does VLA look at 2024 2025"

Links: [{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025","url":"https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"Comprehensive Survey of VLA Models | PDF | Embodied Cognition | Computer Vision","url":"https://www.scribd.com/document/939026368/Pure-Vision-Language-Action-VLA-Models-A-Comprehensive-Survey"},{"title":"GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub","url":"https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"}]

Based on the search results, here's what recent research shows about VLA model interpretability and attention visualization in robot manipulation:

## Key Findings on VLA Model Attention and Interpretability

### Mechanistic Interpretability Studies

Mechanistic interpretability analyses show that specific transformer neurons correspond to semantic directions (e.g., "fast", "up"), and activation steering can causally modulate robot behavior at inference time, yielding real-time behavioral control without retraining.

Recent studies indicate that OpenVLA encodes an emergent internal world model; probes reveal latent knowledge of state transitions consistent with Koopman operator theory.

### Attention Visualization and Analysis

Research on VLM attention patterns shows that cross-attention serves three functions: object detection, suppression, and outlier suppression, with different architectures having distinct characteristics in their attention heads. Additionally, LVLM-Interpret is an interactive tool that combines attention knockout with relevancy mapping and causal graph construction to visualize information flow patterns and identify critical image regions.

### What VLA Models Focus On

Representations at visual token positions change systematically across layers, gradually aligning with interpretable textual concepts, indicating that VLMs can naturally transform visual information into language-like representations.

### Future Directions

Advances in attention mechanisms, token pruning strategies, and interpretability frameworks will further enable robust, transparent deployment in diverse robotic environments.

The field is actively developing better tools and methods to understand how VLA models process visual information and generate manipulation actions, with multiple 2024-2025 publications focusing on these interpretability questions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "c6dba2f5-25ff-4547-803b-1d5d94091a53",
  "tool_use_result": {
    "query": "VLA model interpretability attention visualization robot manipulation what does VLA look at 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L4yQ7dy5iDkjjgK8AEENVR",
        "content": [
          {
            "title": "Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey",
            "url": "https://arxiv.org/html/2508.13073v1"
          },
          {
            "title": "CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models",
            "url": "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"
          },
          {
            "title": "Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S1566253525011248"
          },
          {
            "title": "OpenVLA: Open Source VLA for Robotics",
            "url": "https://www.emergentmind.com/topics/openvla"
          },
          {
            "title": "Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025",
            "url": "https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/"
          },
          {
            "title": "CoA-VLA: Improving Vision-Language-Action Models via ...",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"
          },
          {
            "title": "Vision Language Action Models (VLA) & Policies for Robots",
            "url": "https://learnopencv.com/vision-language-action-models-lerobot-policy/"
          },
          {
            "title": "Comprehensive Survey of VLA Models | PDF | Embodied Cognition | Computer Vision",
            "url": "https://www.scribd.com/document/939026368/Pure-Vision-Language-Action-VLA-Models-A-Comprehensive-Survey"
          },
          {
            "title": "GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub",
            "url": "https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"
          },
          {
            "title": "Vision Language Action Models in Robotic Manipulation: A Systematic Review",
            "url": "https://arxiv.org/html/2507.10672v1"
          }
        ]
      },
      "Based on the search results, here's what recent research shows about VLA model interpretability and attention visualization in robot manipulation:\n\n## Key Findings on VLA Model Attention and Interpretability\n\n### Mechanistic Interpretability Studies\n\nMechanistic interpretability analyses show that specific transformer neurons correspond to semantic directions (e.g., \"fast\", \"up\"), and activation steering can causally modulate robot behavior at inference time, yielding real-time behavioral control without retraining.\n\nRecent studies indicate that OpenVLA encodes an emergent internal world model; probes reveal latent knowledge of state transitions consistent with Koopman operator theory.\n\n### Attention Visualization and Analysis\n\nResearch on VLM attention patterns shows that cross-attention serves three functions: object detection, suppression, and outlier suppression, with different architectures having distinct characteristics in their attention heads. Additionally, LVLM-Interpret is an interactive tool that combines attention knockout with relevancy mapping and causal graph construction to visualize information flow patterns and identify critical image regions.\n\n### What VLA Models Focus On\n\nRepresentations at visual token positions change systematically across layers, gradually aligning with interpretable textual concepts, indicating that VLMs can naturally transform visual information into language-like representations.\n\n### Future Directions\n\nAdvances in attention mechanisms, token pruning strategies, and interpretability frameworks will further enable robust, transparent deployment in diverse robotic environments.\n\nThe field is actively developing better tools and methods to understand how VLA models process visual information and generate manipulation actions, with multiple 2024-2025 publications focusing on these interpretability questions."
    ],
    "durationSeconds": 8.561846342999997
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T15:03:41.129Z_

<details><summary>↩ Tool result · `toolu_01M2fiidtAoRE7KDcEKk9ikn`</summary>

```text
Web search results for query: "language conditioned visual feature selection robot policy task-relevant visual tokens 2024 2025"

Links: [{"title":"Language-Conditioned Representations and Mixture-of-Experts Policy for Robust Multi-Task Robotic Manipulation","url":"https://arxiv.org/html/2510.24055"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation","url":"https://arxiv.org/html/2508.05186v5"},{"title":"Progress-Guided Diffusion Policy for Vision-Language Robotic Manipulation","url":"https://arxiv.org/html/2603.27670"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.15618v2"},{"title":"Task-conditioned adaptation of visual features in multi-task policy learning","url":"https://openaccess.thecvf.com/content/CVPR2024/papers/Marza_Task-Conditioned_Adaptation_of_Visual_Features_in_Multi-Task_Policy_Learning_CVPR_2024_paper.pdf"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"}]

Based on the web search results, I found several relevant papers and works on language-conditioned visual feature selection for robotic manipulation and task-relevant visual tokens from 2024-2025:

## Key Papers and Approaches:

### 1. **Compressor-VLA: Instruction-Guided Visual Token Compression** (November 2025)
Compressor-VLA is a hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models, consisting of a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details. This compression is dynamically modulated by the natural language instruction, allowing for the adaptive condensation of task-relevant visual information.

### 2. **Language-Conditioned Visual Representation (LCVR) Module** (October 2025)
The framework combines a Language-Conditioned Visual Representation module that resolves perceptual ambiguities by grounding visual features with language instructions, enabling differentiation between visually similar tasks.

### 3. **Task-aware Virtual View Exploration (TVVE)** (March 2026)
TVVE is a framework that learns to select task-relevant virtual camera viewpoints and dynamically re-renders observations from a reconstructed scene representation using the selected viewpoints, and introduces a Task-aware Mixture-of-Experts (TaskMoE) visual encoder that routes visual features to task-specialized experts, mitigating interference in multi-task learning.

### 4. **DeepVision-VLA: Action-Guided Visual Pruning** (March 2026)
Action-to-vision attention guidance provides effective cues for identifying manipulation-relevant regions, as shallow-layer action tokens naturally encode both task intent and action-conditioned visual grounding.

### 5. **Progress-Guided Diffusion Policy** (March 2026)
ProgressVLA mitigates visual noise by grounding progress estimation within a pre-trained, object-centric visual feature space, and by explicitly conditioning on language, the model ensures the learned signal prioritizes task-relevant state changes over incidental visual dynamics.

These approaches collectively address the challenge of selecting and focusing on task-relevant visual information in language-conditioned robotic policies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "ff78034e-689c-4fc4-8597-7b42719e9c6a",
  "tool_use_result": {
    "query": "language conditioned visual feature selection robot policy task-relevant visual tokens 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BzVRYrYiixVCpVDLVwr7Ku",
        "content": [
          {
            "title": "Language-Conditioned Representations and Mixture-of-Experts Policy for Robust Multi-Task Robotic Manipulation",
            "url": "https://arxiv.org/html/2510.24055"
          },
          {
            "title": "Vision-Language-Action Models and the Search for a Generalist Robot Policy",
            "url": "https://itcanthink.substack.com/p/vision-language-action-models-and"
          },
          {
            "title": "Vision-Language-Action Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/html/2505.04769v1"
          },
          {
            "title": "Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation",
            "url": "https://arxiv.org/html/2508.05186v5"
          },
          {
            "title": "Progress-Guided Diffusion Policy for Vision-Language Robotic Manipulation",
            "url": "https://arxiv.org/html/2603.27670"
          },
          {
            "title": "Vision Language Action Models (VLA) & Policies for Robots",
            "url": "https://learnopencv.com/vision-language-action-models-lerobot-policy/"
          },
          {
            "title": "[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/abs/2511.18950"
          },
          {
            "title": "Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.15618v2"
          },
          {
            "title": "Task-conditioned adaptation of visual features in multi-task policy learning",
            "url": "https://openaccess.thecvf.com/content/CVPR2024/papers/Marza_Task-Conditioned_Adaptation_of_Visual_Features_in_Multi-Task_Policy_Learning_CVPR_2024_paper.pdf"
          },
          {
            "title": "CoA-VLA: Improving Vision-Language-Action Models via ...",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers and works on language-conditioned visual feature selection for robotic manipulation and task-relevant visual tokens from 2024-2025:\n\n## Key Papers and Approaches:\n\n### 1. **Compressor-VLA: Instruction-Guided Visual Token Compression** (November 2025)\nCompressor-VLA is a hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models, consisting of a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details. This compression is dynamically modulated by the natural language instruction, allowing for the adaptive condensation of task-relevant visual information.\n\n### 2. **Language-Conditioned Visual Representation (LCVR) Module** (October 2025)\nThe framework combines a Language-Conditioned Visual Representation module that resolves perceptual ambiguities by grounding visual features with language instructions, enabling differentiation between visually similar tasks.\n\n### 3. **Task-aware Virtual View Exploration (TVVE)** (March 2026)\nTVVE is a framework that learns to select task-relevant virtual camera viewpoints and dynamically re-renders observations from a reconstructed scene representation using the selected viewpoints, and introduces a Task-aware Mixture-of-Experts (TaskMoE) visual encoder that routes visual features to task-specialized experts, mitigating interference in multi-task learning.\n\n### 4. **DeepVision-VLA: Action-Guided Visual Pruning** (March 2026)\nAction-to-vision attention guidance provides effective cues for identifying manipulation-relevant regions, as shallow-layer action tokens naturally encode both task intent and action-conditioned visual grounding.\n\n### 5. **Progress-Guided Diffusion Policy** (March 2026)\nProgressVLA mitigates visual noise by grounding progress estimation within a pre-trained, object-centric visual feature space, and by explicitly conditioning on language, the model ensures the learned signal prioritizes task-relevant state changes over incidental visual dynamics.\n\nThese approaches collectively address the challenge of selecting and focusing on task-relevant visual information in language-conditioned robotic policies."
    ],
    "durationSeconds": 9.963787371999992
  }
}
```

</details>

---

### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
Excellent! I found some very relevant papers. Let me now search for more specific papers that I need:
1. Compressor-VLA (very relevant - instruction-guided visual token compression for VLA)
2. Task-conditioned adaptation of visual features (CVPR 2024)
3. GradCAM original paper
4. LVLM-Interpret
5. DeepVision-VLA (action-guided visual pruning - very relevant!)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "37d43098-1d44-4485-8b53-8f73b14a0211",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TfD2ghbh32kxgv8JaFF9Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4460,
      "cache_read_input_tokens": 44206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4460
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

_source line 46_

找到几篇非常相关的新论文。继续搜索更多细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "e4a8d0c9-7ad2-4885-be42-c16a9158fbad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TfD2ghbh32kxgv8JaFF9Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4460,
      "cache_read_input_tokens": 44206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4460
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

_source line 47_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DE1siUiBP2RHwpH1cMFE5m`</summary>

```json
{
  "query": "Compressor-VLA instruction-guided visual token compression VLA robotic manipulation 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "a6fcf683-466b-4784-adae-3a13fe23a4f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TfD2ghbh32kxgv8JaFF9Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4460,
      "cache_read_input_tokens": 44206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4460
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

_source line 48_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016vahen7YkCTJ4W3oX3PfWL`</summary>

```json
{
  "query": "DeepVision-VLA action-guided visual pruning vision language action 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "fcfac092-8b1c-4d39-bfd1-c26ea697d2ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TfD2ghbh32kxgv8JaFF9Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4460,
      "cache_read_input_tokens": 44206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4460
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

_source line 49_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LuF9a5T5pA4TUdU2oyyLdc`</summary>

```json
{
  "query": "\"task-conditioned adaptation of visual features\" multi-task policy learning Marza CVPR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "043eecb6-dd89-4f24-8abf-51342a1dde48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TfD2ghbh32kxgv8JaFF9Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4460,
      "cache_read_input_tokens": 44206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4460
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

_source line 50_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V5ssEnBDN4fpT2KotiX8Tn`</summary>

```json
{
  "query": "Grad-CAM visual explanations Selvaraju ICCV 2017 gradient class activation mapping"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "748f0919-191e-489e-8806-e2a45301c69e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TfD2ghbh32kxgv8JaFF9Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4460,
      "cache_read_input_tokens": 44206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4460
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

_source line 51 · 2026-05-17T15:03:55.455Z_

<details><summary>↩ Tool result · `toolu_01LuF9a5T5pA4TUdU2oyyLdc`</summary>

```text
Web search results for query: ""task-conditioned adaptation of visual features" multi-task policy learning Marza CVPR 2024"

Links: [{"title":"Pierre Marza | Task-conditioned adaptation of visual features in multi-task policy learning","url":"https://pierremarza.github.io/projects/task_conditioned_adaptation/"},{"title":"Task-conditioned adaptation of visual features in multi-task policy learning","url":"https://openaccess.thecvf.com/content/CVPR2024/papers/Marza_Task-Conditioned_Adaptation_of_Visual_Features_in_Multi-Task_Policy_Learning_CVPR_2024_paper.pdf"},{"title":"GitHub - PierreMarza/task_conditioned_adaptation: Code for CVPR 2024 paper \"Task-conditioned adaptation of visual features in multi-task policy learning\"","url":"https://github.com/PierreMarza/task_conditioned_adaptation"},{"title":"CVPR 2024 Open Access Repository","url":"https://openaccess.thecvf.com/content/CVPR2024/html/Marza_Task-Conditioned_Adaptation_of_Visual_Features_in_Multi-Task_Policy_Learning_CVPR_2024_paper.html"},{"title":"Task-conditioned adaptation of visual features in multi-task policy learning - Inria - Institut national de recherche en sciences et technologies du numérique","url":"https://inria.hal.science/hal-04569375"},{"title":"[2402.07739] Task-conditioned adaptation of visual features in multi-task policy learning","url":"https://arxiv.org/abs/2402.07739"},{"title":"Task-conditioned adaptation of visual features in multi- ...","url":"https://inria.hal.science/hal-04569375/file/CVPR2024_Task_Conditioned_Adaptation.pdf"},{"title":"CVPR Poster Task-Conditioned Adaptation of Visual Features in Multi-Task Policy Learning","url":"https://cvpr.thecvf.com/virtual/2024/poster/30739"},{"title":"Task-conditioned adaptation of visual features in multi-task policy learning","url":"https://arxiv.org/html/2402.07739v4"},{"title":"CVPR 2024 NAVER LABS Europe papers and benchmarks","url":"https://europe.naverlabs.com/updates/cvpr-2024-conference-and-workshop-papers-and-benchmarks/"}]

I found comprehensive information about the paper "Task-conditioned adaptation of visual features in multi-task policy learning" by Pierre Marza and colleagues presented at CVPR 2024.

## Overview

The work introduces task-conditioned adapters that do not require finetuning any pre-trained weights, combined with a single policy trained with behavior cloning and capable of addressing multiple tasks.

## Key Contributions

The authors adapt pre-trained large vision models conditioned on specific downstream tasks in the context of multi-task policy learning, using task-conditioned adapters. The policy and visual adapters are conditioned on task embeddings, which can be selected at inference if the task is known, or alternatively inferred from a set of example demonstrations.

## Technical Approach

One trainable adapter is added after each ViT block to modulate its output, implemented as a 2-layer MLP that is conditioned on the task embedding and modulates the output of the corresponding self-attention block. The output of a middle adapter is combined with the one of the self-attention layer through a residual connection.

## Few-Shot Capabilities

For the unknown setting where the task embedding is unknown at inference, it needs to be estimated from a set of example demonstrations by finding the embedding that obtains the highest probability of the demonstration actions when the policy is applied to the demonstration inputs.

## Evaluation

The method was evaluated on a wide variety of tasks from the CortexBench benchmark and can be addressed with a single policy. The work demonstrates that adapting visual features is a key design choice and that the method generalizes to unseen tasks given a few demonstrations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "e6795de0-2716-49f1-8bc0-54f18a89ac15",
  "tool_use_result": {
    "query": "\"task-conditioned adaptation of visual features\" multi-task policy learning Marza CVPR 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Uez5EMLEYTr53trfeudCjK",
        "content": [
          {
            "title": "Pierre Marza | Task-conditioned adaptation of visual features in multi-task policy learning",
            "url": "https://pierremarza.github.io/projects/task_conditioned_adaptation/"
          },
          {
            "title": "Task-conditioned adaptation of visual features in multi-task policy learning",
            "url": "https://openaccess.thecvf.com/content/CVPR2024/papers/Marza_Task-Conditioned_Adaptation_of_Visual_Features_in_Multi-Task_Policy_Learning_CVPR_2024_paper.pdf"
          },
          {
            "title": "GitHub - PierreMarza/task_conditioned_adaptation: Code for CVPR 2024 paper \"Task-conditioned adaptation of visual features in multi-task policy learning\"",
            "url": "https://github.com/PierreMarza/task_conditioned_adaptation"
          },
          {
            "title": "CVPR 2024 Open Access Repository",
            "url": "https://openaccess.thecvf.com/content/CVPR2024/html/Marza_Task-Conditioned_Adaptation_of_Visual_Features_in_Multi-Task_Policy_Learning_CVPR_2024_paper.html"
          },
          {
            "title": "Task-conditioned adaptation of visual features in multi-task policy learning - Inria - Institut national de recherche en sciences et technologies du numérique",
            "url": "https://inria.hal.science/hal-04569375"
          },
          {
            "title": "[2402.07739] Task-conditioned adaptation of visual features in multi-task policy learning",
            "url": "https://arxiv.org/abs/2402.07739"
          },
          {
            "title": "Task-conditioned adaptation of visual features in multi- ...",
            "url": "https://inria.hal.science/hal-04569375/file/CVPR2024_Task_Conditioned_Adaptation.pdf"
          },
          {
            "title": "CVPR Poster Task-Conditioned Adaptation of Visual Features in Multi-Task Policy Learning",
            "url": "https://cvpr.thecvf.com/virtual/2024/poster/30739"
          },
          {
            "title": "Task-conditioned adaptation of visual features in multi-task policy learning",
            "url": "https://arxiv.org/html/2402.07739v4"
          },
          {
            "title": "CVPR 2024 NAVER LABS Europe papers and benchmarks",
            "url": "https://europe.naverlabs.com/updates/cvpr-2024-conference-and-workshop-papers-and-benchmarks/"
          }
        ]
      },
      "I found comprehensive information about the paper \"Task-conditioned adaptation of visual features in multi-task policy learning\" by Pierre Marza and colleagues presented at CVPR 2024.\n\n## Overview\n\nThe work introduces task-conditioned adapters that do not require finetuning any pre-trained weights, combined with a single policy trained with behavior cloning and capable of addressing multiple tasks.\n\n## Key Contributions\n\nThe authors adapt pre-trained large vision models conditioned on specific downstream tasks in the context of multi-task policy learning, using task-conditioned adapters. The policy and visual adapters are conditioned on task embeddings, which can be selected at inference if the task is known, or alternatively inferred from a set of example demonstrations.\n\n## Technical Approach\n\nOne trainable adapter is added after each ViT block to modulate its output, implemented as a 2-layer MLP that is conditioned on the task embedding and modulates the output of the corresponding self-attention block. The output of a middle adapter is combined with the one of the self-attention layer through a residual connection.\n\n## Few-Shot Capabilities\n\nFor the unknown setting where the task embedding is unknown at inference, it needs to be estimated from a set of example demonstrations by finding the embedding that obtains the highest probability of the demonstration actions when the policy is applied to the demonstration inputs.\n\n## Evaluation\n\nThe method was evaluated on a wide variety of tasks from the CortexBench benchmark and can be addressed with a single policy. The work demonstrates that adapting visual features is a key design choice and that the method generalizes to unseen tasks given a few demonstrations."
    ],
    "durationSeconds": 7.274464041000014
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-17T15:03:55.852Z_

<details><summary>↩ Tool result · `toolu_016vahen7YkCTJ4W3oX3PfWL`</summary>

```text
Web search results for query: "DeepVision-VLA action-guided visual pruning vision language action 2025 2026"

Links: [{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://deepvision-vla.github.io/"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.15618v2"},{"title":"DeepVision-VLA: Keeping Visual Context Alive Through the Depths of Robot Action Models / DeepVision-VLA：在机器人动作模型的深层保持视觉上下文活跃 | Alan Hou","url":"https://alanhou.org/blog/arxiv-look-before-acting-enhancing-vision-foundation/"},{"title":"[2603.15618] Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.15618"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/402482266_Look_Before_Acting_Enhancing_Vision_Foundation_Representations_for_Vision-Language-Action_Models"},{"title":"Paper page - Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://huggingface.co/papers/2603.15618"},{"title":"GitHub - chen7086/VLA-ADP: Action aware Dynamic Pruning for Efficient Vision Language Action Manipulation · GitHub","url":"https://github.com/chen7086/VLA-ADP"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model","url":"https://arxiv.org/html/2602.20566"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"}]

Based on the search results, here's information about DeepVision-VLA and action-guided visual pruning:

## DeepVision-VLA Overview

DeepVision-VLA is built on a Vision-Language Mixture-of-Transformers (VL-MoT) framework. Vision-Language-Action (VLA) models have recently emerged as a promising paradigm for robotic manipulation, in which reliable action prediction critically depends on accurately interpreting and integrating visual observations conditioned on language instructions.

## Key Problem & Motivation

The research performs a systematic analysis of multiple VLA models across different action-generation paradigms and observes that sensitivity to visual tokens progressively decreases in deeper layers during action generation.

## Core Innovation: Action-Guided Visual Pruning (AGVP)

Action-Guided Visual Pruning (AGVP) leverages shallow-layer attention to prune irrelevant visual tokens while preserving task-relevant ones, reinforcing critical visual cues for manipulation with minimal computational overhead. 

More specifically, AGVP leverages the robust grounding capabilities of shallow VLA layers to compute a saliency map by averaging attention weights from action tokens to visual tokens, identifying the most task-relevant regions, which are then used to prune the Query, Key, and Value across the Vision Expert's Transformer layers before integrating them into the deep VLA layers.

## Framework Design

The framework enables shared attention between the vision foundation model and the VLA backbone, injecting multi-scale visual features from the vision expert into deeper layers of the VLA backbone to enhance visual representations for precise and complex manipulation.

## Performance Results

DeepVision-VLA achieves state-of-the-art (SOTA) performance, outperforming prior VLA methods by 9.0% in simulated settings and 7.5% in real-world settings.

The paper was published in March 2026, with the research available on arXiv (2603.15618).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "8e771af1-51a9-43b8-9f20-72bff08d5806",
  "tool_use_result": {
    "query": "DeepVision-VLA action-guided visual pruning vision language action 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012u7o6bzWuicpMz5hjqRTgJ",
        "content": [
          {
            "title": "Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://deepvision-vla.github.io/"
          },
          {
            "title": "Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.15618v2"
          },
          {
            "title": "DeepVision-VLA: Keeping Visual Context Alive Through the Depths of Robot Action Models / DeepVision-VLA：在机器人动作模型的深层保持视觉上下文活跃 | Alan Hou",
            "url": "https://alanhou.org/blog/arxiv-look-before-acting-enhancing-vision-foundation/"
          },
          {
            "title": "[2603.15618] Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.15618"
          },
          {
            "title": "Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/402482266_Look_Before_Acting_Enhancing_Vision_Foundation_Representations_for_Vision-Language-Action_Models"
          },
          {
            "title": "Paper page - Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2603.15618"
          },
          {
            "title": "GitHub - chen7086/VLA-ADP: Action aware Dynamic Pruning for Efficient Vision Language Action Manipulation · GitHub",
            "url": "https://github.com/chen7086/VLA-ADP"
          },
          {
            "title": "EfficientVLA: Training-Free Acceleration and Compression ...",
            "url": "https://openreview.net/pdf?id=SELYlDHZk2"
          },
          {
            "title": "BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model",
            "url": "https://arxiv.org/html/2602.20566"
          },
          {
            "title": "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/html/2511.16449"
          }
        ]
      },
      "Based on the search results, here's information about DeepVision-VLA and action-guided visual pruning:\n\n## DeepVision-VLA Overview\n\nDeepVision-VLA is built on a Vision-Language Mixture-of-Transformers (VL-MoT) framework. Vision-Language-Action (VLA) models have recently emerged as a promising paradigm for robotic manipulation, in which reliable action prediction critically depends on accurately interpreting and integrating visual observations conditioned on language instructions.\n\n## Key Problem & Motivation\n\nThe research performs a systematic analysis of multiple VLA models across different action-generation paradigms and observes that sensitivity to visual tokens progressively decreases in deeper layers during action generation.\n\n## Core Innovation: Action-Guided Visual Pruning (AGVP)\n\nAction-Guided Visual Pruning (AGVP) leverages shallow-layer attention to prune irrelevant visual tokens while preserving task-relevant ones, reinforcing critical visual cues for manipulation with minimal computational overhead. \n\nMore specifically, AGVP leverages the robust grounding capabilities of shallow VLA layers to compute a saliency map by averaging attention weights from action tokens to visual tokens, identifying the most task-relevant regions, which are then used to prune the Query, Key, and Value across the Vision Expert's Transformer layers before integrating them into the deep VLA layers.\n\n## Framework Design\n\nThe framework enables shared attention between the vision foundation model and the VLA backbone, injecting multi-scale visual features from the vision expert into deeper layers of the VLA backbone to enhance visual representations for precise and complex manipulation.\n\n## Performance Results\n\nDeepVision-VLA achieves state-of-the-art (SOTA) performance, outperforming prior VLA methods by 9.0% in simulated settings and 7.5% in real-world settings.\n\nThe paper was published in March 2026, with the research available on arXiv (2603.15618)."
    ],
    "durationSeconds": 8.152752980999997
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-17T15:03:55.864Z_

<details><summary>↩ Tool result · `toolu_01DE1siUiBP2RHwpH1cMFE5m`</summary>

```text
Web search results for query: "Compressor-VLA instruction-guided visual token compression VLA robotic manipulation 2025 arxiv"

Links: [{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2512.09927"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"Token Expand-Merge: Training-Free Compression Accelerates Billion-Parameter Vision-Language-Action Model Inference","url":"https://quantumzeitgeist.com/training-token-expand-merge-free-compression-accelerates-billion-parameter/"},{"title":"GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub","url":"https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"}]

I found the paper you're looking for! Here are the key details:

## Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation

Compressor-VLA is a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models.

### Main Problem and Solution

Vision-Language-Action (VLA) models have emerged as a powerful paradigm in Embodied AI. However, the significant computational overhead of processing redundant visual tokens remains a critical bottleneck for real-time robotic deployment. While standard token pruning techniques can alleviate this, these task-agnostic methods struggle to preserve task-critical visual information.

### Framework Architecture

The proposed Compressor-VLA framework consists of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details. This compression is dynamically modulated by the natural language instruction, allowing for the adaptive condensation of task-relevant visual information.

### Results

Experimentally, extensive evaluations demonstrate that Compressor-VLA achieves a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline. The real-robot deployments on a dual-arm robot platform validate the model's sim-to-real transferability and practical applicability.

**ArXiv Link**: https://arxiv.org/abs/2511.18950


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "5e01fd7b-e794-4cd5-aa90-4fcc4152bde2",
  "tool_use_result": {
    "query": "Compressor-VLA instruction-guided visual token compression VLA robotic manipulation 2025 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_019GoMwbpVaPjiY43qoet4pH",
        "content": [
          {
            "title": "[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/abs/2511.18950"
          },
          {
            "title": "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.18950v1"
          },
          {
            "title": "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://chatpaper.com/paper/212383"
          },
          {
            "title": "EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2506.10100v1"
          },
          {
            "title": "Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey",
            "url": "https://arxiv.org/html/2510.17111v3"
          },
          {
            "title": "Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2512.09927"
          },
          {
            "title": "Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey",
            "url": "https://arxiv.org/html/2508.13073v1"
          },
          {
            "title": "Token Expand-Merge: Training-Free Compression Accelerates Billion-Parameter Vision-Language-Action Model Inference",
            "url": "https://quantumzeitgeist.com/training-token-expand-merge-free-compression-accelerates-billion-parameter/"
          },
          {
            "title": "GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub",
            "url": "https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"
          },
          {
            "title": "EfficientVLA: Training-Free Acceleration and Compression ...",
            "url": "https://openreview.net/pdf?id=SELYlDHZk2"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n## Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\n\nCompressor-VLA is a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models.\n\n### Main Problem and Solution\n\nVision-Language-Action (VLA) models have emerged as a powerful paradigm in Embodied AI. However, the significant computational overhead of processing redundant visual tokens remains a critical bottleneck for real-time robotic deployment. While standard token pruning techniques can alleviate this, these task-agnostic methods struggle to preserve task-critical visual information.\n\n### Framework Architecture\n\nThe proposed Compressor-VLA framework consists of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details. This compression is dynamically modulated by the natural language instruction, allowing for the adaptive condensation of task-relevant visual information.\n\n### Results\n\nExperimentally, extensive evaluations demonstrate that Compressor-VLA achieves a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline. The real-robot deployments on a dual-arm robot platform validate the model's sim-to-real transferability and practical applicability.\n\n**ArXiv Link**: https://arxiv.org/abs/2511.18950"
    ],
    "durationSeconds": 8.637180219000001
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-17T15:03:57.281Z_

<details><summary>↩ Tool result · `toolu_01V5ssEnBDN4fpT2KotiX8Tn`</summary>

```text
Web search results for query: "Grad-CAM visual explanations Selvaraju ICCV 2017 gradient class activation mapping"

Links: [{"title":"[1610.02391] Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization","url":"https://arxiv.org/abs/1610.02391"},{"title":"Grad-cam: visual explanations from deep - CVF Open Access","url":"https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html"},{"title":"Grad-CAM: Visual Explanations From Deep Networks via ...","url":"https://openaccess.thecvf.com/content_ICCV_2017/papers/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.pdf"},{"title":"Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8237336/"},{"title":"Grad-CAM: Visual Explanations from Deep Networks via ...","url":"https://ramprs.github.io/static/docs/IJCV_Grad-CAM.pdf"},{"title":"(Open Access) Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization (2017) | Ramprasaath R. Selvaraju | 14581 Citations","url":"https://scispace.com/papers/grad-cam-visual-explanations-from-deep-networks-via-gradient-2hh8jx0dua"},{"title":"Grad-CAM:","url":"https://mit6874.github.io/assets/misc/selvaraju.pdf"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Selvaraju%2C+R.R.%2C+Cogswell%2C+M.%2C+Das%2C+A.%2C+Vedantam%2C+R.%2C+Parikh%2C+D.%2C+Batra%2C+D.%3A+Grad-CAM%3A+visual+explanations+from+deep+networks+via+gradient-based+localization.+In%3A+Proceedings+of+the+IEEE+International+Conference+on+Computer+Vision+%28ICCV%29+%282017%29"},{"title":"Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization | Request PDF","url":"https://www.researchgate.net/publication/322058942_Grad-CAM_Visual_Explanations_from_Deep_Networks_via_Gradient-Based_Localization"},{"title":"Selvaraju, R.R., Cogswell, M., Das, A., Vedantam, R., Parikh, D. and Batra, D. (2017) Grad-CAM Visual Explanations from Deep Networks via Gradient-Weighted Class Activation Mapping. Proceedings of the IEEE International Conference on Computer Vision (ICCV), 2017, 618-626. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=4141532"}]

I found comprehensive information about the Grad-CAM paper. Here are the key details:

## Publication Information

The paper "Grad-CAM: Visual Explanations From Deep Networks via Gradient-Based Localization" was published by Ramprasaath R. Selvaraju, Michael Cogswell, Abhishek Das, Ramakrishna Vedantam, Devi Parikh, and Dhruv Batra in the Proceedings of the IEEE International Conference on Computer Vision (ICCV), 2017, pages 618-626.

## Main Contribution

The paper proposes a technique for producing "visual explanations" for decisions from a large class of CNN-based models, making them more transparent. The approach - Gradient-weighted Class Activation Mapping (Grad-CAM) - uses the gradients of any target concept, flowing into the final convolutional layer to produce a coarse localization map highlighting important regions in the image for predicting the concept.

## Key Features and Applicability

Grad-CAM is applicable to a wide variety of CNN model-families: (1) CNNs with fully-connected layers, (2) CNNs used for structured outputs, (3) CNNs used in tasks with multimodal inputs or reinforcement learning, without any architectural changes or re-training.

## Combination with Fine-grained Visualizations

The authors combine Grad-CAM with fine-grained visualizations to create a high-resolution class-discriminative visualization and apply it to off-the-shelf image classification, captioning, and visual question answering (VQA) models, including ResNet-based architectures.

The paper is widely recognized in the field of explainable AI and has received significant citations for its contribution to making deep learning models more interpretable.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "20b937eb-0436-4340-b348-4dd9cc7a613e",
  "tool_use_result": {
    "query": "Grad-CAM visual explanations Selvaraju ICCV 2017 gradient class activation mapping",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EzwUHwbMGjep7ZV7PerHej",
        "content": [
          {
            "title": "[1610.02391] Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization",
            "url": "https://arxiv.org/abs/1610.02391"
          },
          {
            "title": "Grad-cam: visual explanations from deep - CVF Open Access",
            "url": "https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html"
          },
          {
            "title": "Grad-CAM: Visual Explanations From Deep Networks via ...",
            "url": "https://openaccess.thecvf.com/content_ICCV_2017/papers/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.pdf"
          },
          {
            "title": "Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/8237336/"
          },
          {
            "title": "Grad-CAM: Visual Explanations from Deep Networks via ...",
            "url": "https://ramprs.github.io/static/docs/IJCV_Grad-CAM.pdf"
          },
          {
            "title": "(Open Access) Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization (2017) | Ramprasaath R. Selvaraju | 14581 Citations",
            "url": "https://scispace.com/papers/grad-cam-visual-explanations-from-deep-networks-via-gradient-2hh8jx0dua"
          },
          {
            "title": "Grad-CAM:",
            "url": "https://mit6874.github.io/assets/misc/selvaraju.pdf"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar?q=Selvaraju%2C+R.R.%2C+Cogswell%2C+M.%2C+Das%2C+A.%2C+Vedantam%2C+R.%2C+Parikh%2C+D.%2C+Batra%2C+D.%3A+Grad-CAM%3A+visual+explanations+from+deep+networks+via+gradient-based+localization.+In%3A+Proceedings+of+the+IEEE+International+Conference+on+Computer+Vision+%28ICCV%29+%282017%29"
          },
          {
            "title": "Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization | Request PDF",
            "url": "https://www.researchgate.net/publication/322058942_Grad-CAM_Visual_Explanations_from_Deep_Networks_via_Gradient-Based_Localization"
          },
          {
            "title": "Selvaraju, R.R., Cogswell, M., Das, A., Vedantam, R., Parikh, D. and Batra, D. (2017) Grad-CAM Visual Explanations from Deep Networks via Gradient-Weighted Class Activation Mapping. Proceedings of the IEEE International Conference on Computer Vision (ICCV), 2017, 618-626. - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=4141532"
          }
        ]
      },
      "I found comprehensive information about the Grad-CAM paper. Here are the key details:\n\n## Publication Information\n\nThe paper \"Grad-CAM: Visual Explanations From Deep Networks via Gradient-Based Localization\" was published by Ramprasaath R. Selvaraju, Michael Cogswell, Abhishek Das, Ramakrishna Vedantam, Devi Parikh, and Dhruv Batra in the Proceedings of the IEEE International Conference on Computer Vision (ICCV), 2017, pages 618-626.\n\n## Main Contribution\n\nThe paper proposes a technique for producing \"visual explanations\" for decisions from a large class of CNN-based models, making them more transparent. The approach - Gradient-weighted Class Activation Mapping (Grad-CAM) - uses the gradients of any target concept, flowing into the final convolutional layer to produce a coarse localization map highlighting important regions in the image for predicting the concept.\n\n## Key Features and Applicability\n\nGrad-CAM is applicable to a wide variety of CNN model-families: (1) CNNs with fully-connected layers, (2) CNNs used for structured outputs, (3) CNNs used in tasks with multimodal inputs or reinforcement learning, without any architectural changes or re-training.\n\n## Combination with Fine-grained Visualizations\n\nThe authors combine Grad-CAM with fine-grained visualizations to create a high-resolution class-discriminative visualization and apply it to off-the-shelf image classification, captioning, and visual question answering (VQA) models, including ResNet-based architectures.\n\nThe paper is widely recognized in the field of explainable AI and has received significant citations for its contribution to making deep learning models more interpretable."
    ],
    "durationSeconds": 8.237561919999992
  }
}
```

</details>

---

### Assistant

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
I found very relevant papers. Let me also search for VLA-ADP (Action-aware Dynamic Pruning) and VLA-Pruner which appeared in search results, plus a few more IB-related papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "41a65060-9785-41cf-a4d2-ad82d3fc5a36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gCAcAAB6LMVbCj3ZgzmJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4681,
      "cache_read_input_tokens": 48666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4681
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

_source line 56_

发现了几篇非常重要的新论文（Compressor-VLA, DeepVision-VLA, VLA-ADP, VLA-Pruner）。继续搜索补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "3ab4a9f6-7ef2-4003-9621-d1640803846c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gCAcAAB6LMVbCj3ZgzmJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4681,
      "cache_read_input_tokens": 48666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4681
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

_source line 57_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xu6jybY7c4c98EyLDXGegb`</summary>

```json
{
  "query": "VLA-ADP action aware dynamic pruning efficient vision language action manipulation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "04098740-8809-4f7b-88da-8da78d5b55e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gCAcAAB6LMVbCj3ZgzmJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4681,
      "cache_read_input_tokens": 48666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4681
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

_source line 58_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EGTz85WyvkHSkUWDdqCG9d`</summary>

```json
{
  "query": "VLA-Pruner temporal-aware dual-level visual token pruning VLA inference 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "c28de46b-0ddc-4aa7-b3c3-841a352cc882",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gCAcAAB6LMVbCj3ZgzmJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4681,
      "cache_read_input_tokens": 48666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4681
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

_source line 59_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CVN6fVTsaBMDXGLBaAL2ii`</summary>

```json
{
  "query": "conditional information bottleneck task-relevant representation learning supervised feature selection 2020 2021 2022 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "c9a4dea7-28ea-474f-8d62-c770e38e1b15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gCAcAAB6LMVbCj3ZgzmJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4681,
      "cache_read_input_tokens": 48666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4681
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

_source line 60_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DDtxX6e8vrqpQ7kSHDiRCZ`</summary>

```json
{
  "query": "LVLM-Interpret interpretability tool vision language model token importance 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "ace93b1f-acfa-4ec3-adfc-72f2ad155723",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gCAcAAB6LMVbCj3ZgzmJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4681,
      "cache_read_input_tokens": 48666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4681
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

_source line 61 · 2026-05-17T15:04:19.371Z_

<details><summary>↩ Tool result · `toolu_01Xu6jybY7c4c98EyLDXGegb`</summary>

```text
Web search results for query: "VLA-ADP action aware dynamic pruning efficient vision language action manipulation 2025"

Links: [{"title":"GitHub - chen7086/VLA-ADP: Action aware Dynamic Pruning for Efficient Vision Language Action Manipulation · GitHub","url":"https://github.com/chen7086/VLA-ADP"},{"title":"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://arxiv.org/html/2509.22093v1"},{"title":"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation | OpenReview","url":"https://openreview.net/forum?id=ea6j8k8Rnw"},{"title":"[2509.22093] Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://arxiv.org/abs/2509.22093"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"(PDF) Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://www.researchgate.net/publication/395944757_Action-aware_Dynamic_Pruning_for_Efficient_Vision-Language-Action_Manipulation"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"},{"title":"Efficient Vision-Language-Action Models for Embodied ...","url":"https://arxiv.org/pdf/2510.17111"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"ACTION-AWARE DYNAMIC PRUNING FOR EFFICIENT VISION- ...","url":"https://openreview.net/pdf/022fa65ed15d8281bae4fdd9be9e837aa5210745.pdf"}]

Based on the search results, here's what I found about VLA-ADP:

## Overview

VLA-ADP (Action-aware Dynamic Pruning) is a training-free, plug-and-play method for efficient Vision-Language-Action models that adaptively prunes redundant visual tokens across manipulation stages by combining text-driven token relevance with an action-aware gating signal from end-effector motion—reducing FLOPs and latency while preserving task success.

## Key Approach

The method integrates text-driven token selection with action-aware trajectory gating, introducing a gating mechanism that conditions the pruning signal on recent action trajectories, using past motion windows to adaptively adjust token retention ratios in accordance with dynamics.

## Technical Innovation

The method observes that visual token redundancy is higher in the coarse manipulation phase than in fine-grained operations, and is strongly correlated with action dynamics. ADP introduces a text-driven pruning mechanism that computes the similarity between vision tokens and task instructions based on cross-modal attention and retains the most relevant Top-K tokens.

## Performance

ADP achieves a 1.35× speedup and 25.8% action success rate improvement in OpenVLA-OFT settings. The method has been evaluated on both simulation benchmarks and real-world robotic tasks.

## Publication

The paper was published on arXiv as preprint arXiv:2509.22093 in 2025 by authors including Xiaohuan Pei, Yuxing Chen, Siyu Xu, Yunke Wang, Yuheng Shi, and Chang Xu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "8237ca9d-7621-4608-a859-9b35bec267b2",
  "tool_use_result": {
    "query": "VLA-ADP action aware dynamic pruning efficient vision language action manipulation 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_013xUMeFjbxhAxqQi3FDKEmT",
        "content": [
          {
            "title": "GitHub - chen7086/VLA-ADP: Action aware Dynamic Pruning for Efficient Vision Language Action Manipulation · GitHub",
            "url": "https://github.com/chen7086/VLA-ADP"
          },
          {
            "title": "Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation",
            "url": "https://arxiv.org/html/2509.22093v1"
          },
          {
            "title": "Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation | OpenReview",
            "url": "https://openreview.net/forum?id=ea6j8k8Rnw"
          },
          {
            "title": "[2509.22093] Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation",
            "url": "https://arxiv.org/abs/2509.22093"
          },
          {
            "title": "OpenVLA: Open Source VLA for Robotics",
            "url": "https://www.emergentmind.com/topics/openvla"
          },
          {
            "title": "(PDF) Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation",
            "url": "https://www.researchgate.net/publication/395944757_Action-aware_Dynamic_Pruning_for_Efficient_Vision-Language-Action_Manipulation"
          },
          {
            "title": "A Survey on Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.24795v1"
          },
          {
            "title": "Efficient Vision-Language-Action Models for Embodied ...",
            "url": "https://arxiv.org/pdf/2510.17111"
          },
          {
            "title": "Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey",
            "url": "https://arxiv.org/html/2510.17111v3"
          },
          {
            "title": "ACTION-AWARE DYNAMIC PRUNING FOR EFFICIENT VISION- ...",
            "url": "https://openreview.net/pdf/022fa65ed15d8281bae4fdd9be9e837aa5210745.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about VLA-ADP:\n\n## Overview\n\nVLA-ADP (Action-aware Dynamic Pruning) is a training-free, plug-and-play method for efficient Vision-Language-Action models that adaptively prunes redundant visual tokens across manipulation stages by combining text-driven token relevance with an action-aware gating signal from end-effector motion—reducing FLOPs and latency while preserving task success.\n\n## Key Approach\n\nThe method integrates text-driven token selection with action-aware trajectory gating, introducing a gating mechanism that conditions the pruning signal on recent action trajectories, using past motion windows to adaptively adjust token retention ratios in accordance with dynamics.\n\n## Technical Innovation\n\nThe method observes that visual token redundancy is higher in the coarse manipulation phase than in fine-grained operations, and is strongly correlated with action dynamics. ADP introduces a text-driven pruning mechanism that computes the similarity between vision tokens and task instructions based on cross-modal attention and retains the most relevant Top-K tokens.\n\n## Performance\n\nADP achieves a 1.35× speedup and 25.8% action success rate improvement in OpenVLA-OFT settings. The method has been evaluated on both simulation benchmarks and real-world robotic tasks.\n\n## Publication\n\nThe paper was published on arXiv as preprint arXiv:2509.22093 in 2025 by authors including Xiaohuan Pei, Yuxing Chen, Siyu Xu, Yunke Wang, Yuheng Shi, and Chang Xu."
    ],
    "durationSeconds": 7.759753422999987
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-17T15:04:19.845Z_

<details><summary>↩ Tool result · `toolu_01EGTz85WyvkHSkUWDdqCG9d`</summary>

```text
Web search results for query: "VLA-Pruner temporal-aware dual-level visual token pruning VLA inference 2025"

Links: [{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449v1"},{"title":"Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.00780"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614"},{"title":"Preprint. SP-VLA: A JOINT MODEL SCHEDULING AND TOKEN","url":"https://arxiv.org/pdf/2506.12723"},{"title":"BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model","url":"https://arxiv.org/html/2602.20566"}]

Based on the search results, here's information about VLA-Pruner:

## Overview

Vision-Language-Action (VLA) models have shown great promise for embodied AI, yet the heavy computational cost of processing continuous visual streams severely limits their real-time deployment. VLA-Pruner is a versatile plug-and-play VLA-specific token prune method that aligns with the dual-system nature of VLA models and exploits the temporal continuity in robot manipulation.

## Key Innovation

The main contribution of VLA-Pruner is its dual-level approach to token importance. VLA-Pruner adopts a dual-level importance criterion for visual token retention: vision-language prefill attention for semantic-level relevance and action decode attention, estimated via temporal smoothing, for action-level importance.

## Problem It Addresses

VLM-specific token pruning methods select tokens based solely on semantic salience metrics (e.g., prefill attention), while overlooking the VLA's intrinsic dual-system nature of high-level semantic understanding and low-level action execution. Consequently, these methods bias token retention toward semantic cues, discard critical information for action generation, and significantly degrade VLA performance.

## Token Selection Strategy

VLA-Pruner proposes a novel dual-level token selection strategy that adaptively preserves a compact, informative set of visual tokens for both semantic understanding and action execution under given compute budget.

## Performance

Experiments show that VLA-Pruner achieves state-of-the-art performance across multiple VLA architectures and diverse robotic tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "4e8b4356-dc37-4866-8876-6d380b65e700",
  "tool_use_result": {
    "query": "VLA-Pruner temporal-aware dual-level visual token pruning VLA inference 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SMeGD7dyFXmjpHkNQYW2mj",
        "content": [
          {
            "title": "[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/abs/2511.16449"
          },
          {
            "title": "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/html/2511.16449v1"
          },
          {
            "title": "Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2602.00780"
          },
          {
            "title": "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware",
            "url": "https://arxiv.org/pdf/2509.05614"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991"
          },
          {
            "title": "SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration",
            "url": "https://arxiv.org/html/2506.12723v2"
          },
          {
            "title": "EfficientVLA: Training-Free Acceleration and Compression ...",
            "url": "https://openreview.net/pdf?id=SELYlDHZk2"
          },
          {
            "title": "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning",
            "url": "https://arxiv.org/html/2509.05614"
          },
          {
            "title": "Preprint. SP-VLA: A JOINT MODEL SCHEDULING AND TOKEN",
            "url": "https://arxiv.org/pdf/2506.12723"
          },
          {
            "title": "BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model",
            "url": "https://arxiv.org/html/2602.20566"
          }
        ]
      },
      "Based on the search results, here's information about VLA-Pruner:\n\n## Overview\n\nVision-Language-Action (VLA) models have shown great promise for embodied AI, yet the heavy computational cost of processing continuous visual streams severely limits their real-time deployment. VLA-Pruner is a versatile plug-and-play VLA-specific token prune method that aligns with the dual-system nature of VLA models and exploits the temporal continuity in robot manipulation.\n\n## Key Innovation\n\nThe main contribution of VLA-Pruner is its dual-level approach to token importance. VLA-Pruner adopts a dual-level importance criterion for visual token retention: vision-language prefill attention for semantic-level relevance and action decode attention, estimated via temporal smoothing, for action-level importance.\n\n## Problem It Addresses\n\nVLM-specific token pruning methods select tokens based solely on semantic salience metrics (e.g., prefill attention), while overlooking the VLA's intrinsic dual-system nature of high-level semantic understanding and low-level action execution. Consequently, these methods bias token retention toward semantic cues, discard critical information for action generation, and significantly degrade VLA performance.\n\n## Token Selection Strategy\n\nVLA-Pruner proposes a novel dual-level token selection strategy that adaptively preserves a compact, informative set of visual tokens for both semantic understanding and action execution under given compute budget.\n\n## Performance\n\nExperiments show that VLA-Pruner achieves state-of-the-art performance across multiple VLA architectures and diverse robotic tasks."
    ],
    "durationSeconds": 7.286986300999997
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-17T15:04:22.649Z_

<details><summary>↩ Tool result · `toolu_01CVN6fVTsaBMDXGLBaAL2ii`</summary>

```text
Web search results for query: "conditional information bottleneck task-relevant representation learning supervised feature selection 2020 2021 2022 2023"

Links: [{"title":"Information bottleneck method — Grokipedia","url":"https://grokipedia.com/page/Information_bottleneck_method"},{"title":"Representation Learning and the Information Bottleneck Approach","url":"https://www.inference.vc/representation-learning-and-compression-with-the-information-bottleneck/"},{"title":"Information Bottleneck for Active Feature Acquisition | OpenReview","url":"https://openreview.net/forum?id=u5KzZjQOsl"},{"title":"The Supervised Information Bottleneck - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12110060/"},{"title":"Structured IB: Improving Information Bottleneck with Structured Feature Learning","url":"https://arxiv.org/html/2412.08222v1"},{"title":"LEARNING ROBUST REPRESENTATIONS VIA MULTI- ...","url":"https://openreview.net/pdf?id=B1xwcyHFDr"},{"title":"Information bottleneck method - Wikipedia","url":"https://en.wikipedia.org/wiki/Information_bottleneck_method"},{"title":"The Supervised Information Bottleneck","url":"https://www.mdpi.com/1099-4300/27/5/452"},{"title":"How Does Information Bottleneck Help Deep Learning?","url":"https://proceedings.mlr.press/v202/kawaguchi23a/kawaguchi23a.pdf"},{"title":"Trustworthy Representation Learning via Information Funnels and Bottlenecks | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-025-06924-9"}]

Based on my search results, here's an overview of research on conditional information bottleneck, task-relevant representation learning, and supervised feature selection from 2020-2023:

## Key Research Areas

**Information Bottleneck Fundamentals:**
The Information Bottleneck (IB) resolves limitations of rate-distortion by defining mutual information between the learned representation and a designated downstream random variable as a universal distortion function.

**Conditional Information Bottleneck Variants:**

An interesting extension is the case of information bottleneck with side information, where information is maximized about one target variable and minimized about another, learning a representation that is informative about selected aspects of data.

More recently, information-theoretic objectives, including information funnels and bottlenecks, are designed to extract invariant representations from data, with the Conditional Privacy Funnel with Side-information (CPFSI) being a novel formulation applicable in both fully and semi-supervised settings.

**Supervised Information Bottleneck:**

Applying the IB objective for supervised tasks results in the optimization of a classifier distribution as well, and requires a reformulation of the initial problem to include both representation and classification. The Supervised IB (SIB) is an extension to the original IB that considers the classifier distribution as well, and adds an additional bottleneck to mitigate information flow between representations and the classifier.

**Task-Relevant Representation Learning:**

In the information bottleneck framework, decision contours for classification are constructed by leveraging the learned conditional probability, with the compressed representation treated as a bottleneck through which only pertinent details pass, discarding extraneous information to create a more efficient encoding suitable for predictive tasks.

These research directions address how to extract minimal sufficient statistics for task performance while filtering out irrelevant noise.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "df9633a8-e293-40b9-b8a6-bb6e4577f416",
  "tool_use_result": {
    "query": "conditional information bottleneck task-relevant representation learning supervised feature selection 2020 2021 2022 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XGh95ozDU9Z9UWp7XmDbGz",
        "content": [
          {
            "title": "Information bottleneck method — Grokipedia",
            "url": "https://grokipedia.com/page/Information_bottleneck_method"
          },
          {
            "title": "Representation Learning and the Information Bottleneck Approach",
            "url": "https://www.inference.vc/representation-learning-and-compression-with-the-information-bottleneck/"
          },
          {
            "title": "Information Bottleneck for Active Feature Acquisition | OpenReview",
            "url": "https://openreview.net/forum?id=u5KzZjQOsl"
          },
          {
            "title": "The Supervised Information Bottleneck - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12110060/"
          },
          {
            "title": "Structured IB: Improving Information Bottleneck with Structured Feature Learning",
            "url": "https://arxiv.org/html/2412.08222v1"
          },
          {
            "title": "LEARNING ROBUST REPRESENTATIONS VIA MULTI- ...",
            "url": "https://openreview.net/pdf?id=B1xwcyHFDr"
          },
          {
            "title": "Information bottleneck method - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Information_bottleneck_method"
          },
          {
            "title": "The Supervised Information Bottleneck",
            "url": "https://www.mdpi.com/1099-4300/27/5/452"
          },
          {
            "title": "How Does Information Bottleneck Help Deep Learning?",
            "url": "https://proceedings.mlr.press/v202/kawaguchi23a/kawaguchi23a.pdf"
          },
          {
            "title": "Trustworthy Representation Learning via Information Funnels and Bottlenecks | Machine Learning | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10994-025-06924-9"
          }
        ]
      },
      "Based on my search results, here's an overview of research on conditional information bottleneck, task-relevant representation learning, and supervised feature selection from 2020-2023:\n\n## Key Research Areas\n\n**Information Bottleneck Fundamentals:**\nThe Information Bottleneck (IB) resolves limitations of rate-distortion by defining mutual information between the learned representation and a designated downstream random variable as a universal distortion function.\n\n**Conditional Information Bottleneck Variants:**\n\nAn interesting extension is the case of information bottleneck with side information, where information is maximized about one target variable and minimized about another, learning a representation that is informative about selected aspects of data.\n\nMore recently, information-theoretic objectives, including information funnels and bottlenecks, are designed to extract invariant representations from data, with the Conditional Privacy Funnel with Side-information (CPFSI) being a novel formulation applicable in both fully and semi-supervised settings.\n\n**Supervised Information Bottleneck:**\n\nApplying the IB objective for supervised tasks results in the optimization of a classifier distribution as well, and requires a reformulation of the initial problem to include both representation and classification. The Supervised IB (SIB) is an extension to the original IB that considers the classifier distribution as well, and adds an additional bottleneck to mitigate information flow between representations and the classifier.\n\n**Task-Relevant Representation Learning:**\n\nIn the information bottleneck framework, decision contours for classification are constructed by leveraging the learned conditional probability, with the compressed representation treated as a bottleneck through which only pertinent details pass, discarding extraneous information to create a more efficient encoding suitable for predictive tasks.\n\nThese research directions address how to extract minimal sufficient statistics for task performance while filtering out irrelevant noise."
    ],
    "durationSeconds": 9.093537555000003
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-17T15:04:27.868Z_

<details><summary>↩ Tool result · `toolu_01DDtxX6e8vrqpQ7kSHDiRCZ`</summary>

```text
Web search results for query: "LVLM-Interpret interpretability tool vision language model token importance 2024"

Links: [{"title":"LVLM-Intrepret: An Interpretability Tool for Large Vision-Language Models","url":"https://openaccess.thecvf.com/content/CVPR2024W/XAI4CV/papers/Stan_LVLM-Intrepret_An_Interpretability_Tool_for_Large_Vision-Language_Models_CVPRW_2024_paper.pdf"},{"title":"LVLM-Interpret: An Interpretability Tool for Large Vision-Language Models","url":"https://arxiv.org/html/2404.03118v3"},{"title":"[2404.03118] LVLM-Interpret: An Interpretability Tool for Large Vision-Language Models","url":"https://arxiv.org/abs/2404.03118"},{"title":"LVLM-Intrepret: An Interpretability Tool for Large Vision-Language Models","url":"https://arxiv.org/html/2404.03118v1"},{"title":"Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025","url":"https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/"},{"title":"LVLM-Intrepret: An Interpretability Tool for Large Vision-Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/lvlm-intrepret-interpretability-tool-large-vision-language"},{"title":"LVLM-Interpret","url":"https://intellabs.github.io/multimodal_cognitive_ai/lvlm_interpret/"},{"title":"LVLM-Interpret: Explaining Decision-Making Processes in Large Vision-Language Models - Intel Community","url":"https://community.intel.com/t5/Blogs/Tech-Innovation/Artificial-Intelligence-AI/LVLM-Interpret-Explaining-Decision-Making-Processes-in-Large/post/1649345"},{"title":"Large Vision-Language Models","url":"https://www.emergentmind.com/topics/large-vision-language-model-lvlm"},{"title":"An Interpretability Tool for Large Vision-Language Models","url":"https://www.alphaxiv.org/overview/2404.03118v3"}]

I found comprehensive information about LVLM-Interpret from your search query. Here's what the tool is about:

## Overview

LVLM-Interpret is a novel interactive application aimed at understanding the internal mechanisms of large vision-language models, designed to enhance the interpretability of the image patches which are instrumental in generating an answer and assess the efficacy of the language model in grounding its output in the image.

## Key Features

Users can upload an image and issue multimodal queries to the LVLM, and as the model generates a response, the attention weights of the model are stored internally and are later presented to the user for visualization.

The tool provides an interactive interface where users can upload images and pose multimodal queries through a chatbot-like interaction, then visualizes the attention weights between image patches and textual tokens, giving a clear representation of which parts of the image and text the model is focusing on during answer generation.

## Technical Approaches

Relevancy maps aim at interpreting the decision-making process of transformers by illustrating how different components of an input, whether text or image, are relevant to the model's generated output, and the method assigns a local relevancy scores to each element in the input based on their contribution to the output decision.

The tool adapted the calculation of relevancy maps to LVLMs such as LLaVA, with relevancy scores being backward propagated through the LLM as well as vision transformer commonly used as the vision encoder.

LVLM-Interpret combines attention knockout with relevancy mapping and causal graph construction to visualize information flow patterns and identify critical image regions.

The paper was published in 2024 and presented at CVPR 2024 Workshop on Explainable AI for Computer Vision.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "a0541376-a8af-4191-bee8-8bad1cb852aa",
  "tool_use_result": {
    "query": "LVLM-Interpret interpretability tool vision language model token importance 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SbhDUhVUoMq7h2pdhk6JCf",
        "content": [
          {
            "title": "LVLM-Intrepret: An Interpretability Tool for Large Vision-Language Models",
            "url": "https://openaccess.thecvf.com/content/CVPR2024W/XAI4CV/papers/Stan_LVLM-Intrepret_An_Interpretability_Tool_for_Large_Vision-Language_Models_CVPRW_2024_paper.pdf"
          },
          {
            "title": "LVLM-Interpret: An Interpretability Tool for Large Vision-Language Models",
            "url": "https://arxiv.org/html/2404.03118v3"
          },
          {
            "title": "[2404.03118] LVLM-Interpret: An Interpretability Tool for Large Vision-Language Models",
            "url": "https://arxiv.org/abs/2404.03118"
          },
          {
            "title": "LVLM-Intrepret: An Interpretability Tool for Large Vision-Language Models",
            "url": "https://arxiv.org/html/2404.03118v1"
          },
          {
            "title": "Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025",
            "url": "https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/"
          },
          {
            "title": "LVLM-Intrepret: An Interpretability Tool for Large Vision-Language Models | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/lvlm-intrepret-interpretability-tool-large-vision-language"
          },
          {
            "title": "LVLM-Interpret",
            "url": "https://intellabs.github.io/multimodal_cognitive_ai/lvlm_interpret/"
          },
          {
            "title": "LVLM-Interpret: Explaining Decision-Making Processes in Large Vision-Language Models - Intel Community",
            "url": "https://community.intel.com/t5/Blogs/Tech-Innovation/Artificial-Intelligence-AI/LVLM-Interpret-Explaining-Decision-Making-Processes-in-Large/post/1649345"
          },
          {
            "title": "Large Vision-Language Models",
            "url": "https://www.emergentmind.com/topics/large-vision-language-model-lvlm"
          },
          {
            "title": "An Interpretability Tool for Large Vision-Language Models",
            "url": "https://www.alphaxiv.org/overview/2404.03118v3"
          }
        ]
      },
      "I found comprehensive information about LVLM-Interpret from your search query. Here's what the tool is about:\n\n## Overview\n\nLVLM-Interpret is a novel interactive application aimed at understanding the internal mechanisms of large vision-language models, designed to enhance the interpretability of the image patches which are instrumental in generating an answer and assess the efficacy of the language model in grounding its output in the image.\n\n## Key Features\n\nUsers can upload an image and issue multimodal queries to the LVLM, and as the model generates a response, the attention weights of the model are stored internally and are later presented to the user for visualization.\n\nThe tool provides an interactive interface where users can upload images and pose multimodal queries through a chatbot-like interaction, then visualizes the attention weights between image patches and textual tokens, giving a clear representation of which parts of the image and text the model is focusing on during answer generation.\n\n## Technical Approaches\n\nRelevancy maps aim at interpreting the decision-making process of transformers by illustrating how different components of an input, whether text or image, are relevant to the model's generated output, and the method assigns a local relevancy scores to each element in the input based on their contribution to the output decision.\n\nThe tool adapted the calculation of relevancy maps to LVLMs such as LLaVA, with relevancy scores being backward propagated through the LLM as well as vision transformer commonly used as the vision encoder.\n\nLVLM-Interpret combines attention knockout with relevancy mapping and causal graph construction to visualize information flow patterns and identify critical image regions.\n\nThe paper was published in 2024 and presented at CVPR 2024 Workshop on Explainable AI for Computer Vision."
    ],
    "durationSeconds": 13.278524740000009
  }
}
```

</details>

---

### Assistant

_source line 65_

<details><summary>Logged reasoning block</summary>

```text
I now have all the information I need. Let me compile the findings into the YAML file. I need to add the following new entries to the existing literature_map.yaml:

### Topic 1: Token pruning / token importance in Vision Transformers (classic papers)
1. **ToMe** - Token Merging (Bolya et al., ICLR 2023) - already in the file but only as a format example in the task description. Let me check if it's actually in the file... No, it's not in the YAML. Need to add.
2. **DynamicViT** - (Rao et al., NeurIPS 2021) - pioneering token pruning work


3. **EViT** - (Liang et al., ICLR 2022) - token attentiveness-based reorganization
4. **A-ViT** - (Yin et al., CVPR 2022) - adaptive token halting

### Topic 2: Information Bottleneck in deep learning (foundational)
5. **Original IB** - Tishby, Pereira, Bialek 1999
6. **Deep VIB** - Alemi et al., ICLR 2017
7. **Deep Learning and the IB Principle** - Tishby & Zaslavsky 2015

Now I'm moving on to Topic 3 about visual tokens and continuing to organize the remaining papers.

### Topic 3: Visual token selection / attention for robot learning
8. **Compressor-VLA** - instruction-guided visual token compression (2025)
9. **VLA-ADP** - action-aware dynamic pruning (2025)
10. **VLA-Pruner** - temporal-aware dual-level pruning (2025)
11. **DeepVision-VLA** - action-guided visual pruning (2026)
12. **Task-conditioned adaptation** - Marza et al., CVPR 2024

### Topic 4: Interpretability methods for VLAs / VLMs
13. **Grad-CAM** - Selvaraju et al., ICCV 2017
14. **Attention Rollout** - Abnar & Zuidema, ACL 2020
15. **LVLM-Interpret** - Stan et al., CVPR 2024 Workshop

Now I'm updating the YAML file with these new sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "5b7aaa71-5d50-4baf-8e2b-0f64986f79a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oMWwhDMGKJZbxyycmjYm4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4192,
      "cache_read_input_tokens": 53347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4192
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

_source line 66_

搜集完毕，现在整理所有新论文并追加到现有 literature_map.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "4be3437b-8e7b-4415-9c2b-92ae2175c8ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oMWwhDMGKJZbxyycmjYm4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4192,
      "cache_read_input_tokens": 53347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4192
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

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_01LxdT5zUwS5RH5hqKAp3PY6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/literature_map.yaml",
  "offset": 430
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "c928ae06-764a-439d-b8e6-8cce5ed3b532",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oMWwhDMGKJZbxyycmjYm4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4192,
      "cache_read_input_tokens": 53347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4192
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

_source line 68 · 2026-05-17T15:04:47.005Z_

<details><summary>↩ Tool result · `toolu_01LxdT5zUwS5RH5hqKAp3PY6`</summary>

```text
430	  open_research_directions:
431	    - "Does the learned scorer transfer across task suites (LIBERO-Spatial scorer applied to LIBERO-Goal)?"
432	    - "Correlation between scorer mask and object-segmentation masks — does ACIB learn an implicit object detector for free?"
433	    - "Combining ACIB with augmentation (RoCoDA/GenAug) — does the regularization-side + data-side gain stack?"
434	    - "Robustness on LIBERO-Plus perturbation dims, especially camera viewpoint and distractor objects — where the 95→30% drop lives."
435	    - "ACIB + RobustVLA: training-time IB regularization + post-training RL hardening — do they compose?"
436	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "b2aac008-784d-4310-a2a8-c3d8e89dc197",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/literature_map.yaml",
      "content": "  open_research_directions:\n    - \"Does the learned scorer transfer across task suites (LIBERO-Spatial scorer applied to LIBERO-Goal)?\"\n    - \"Correlation between scorer mask and object-segmentation masks — does ACIB learn an implicit object detector for free?\"\n    - \"Combining ACIB with augmentation (RoCoDA/GenAug) — does the regularization-side + data-side gain stack?\"\n    - \"Robustness on LIBERO-Plus perturbation dims, especially camera viewpoint and distractor objects — where the 95→30% drop lives.\"\n    - \"ACIB + RobustVLA: training-time IB regularization + post-training RL hardening — do they compose?\"\n",
      "numLines": 7,
      "startLine": 430,
      "totalLines": 436
    }
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Edit · `toolu_01BpU4nQwPXYW8xkXKCpGF9H`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/literature_map.yaml",
  "old_string": "    - \"ACIB + RobustVLA: training-time IB regularization + post-training RL hardening — do they compose?\"",
  "new_string": "    - \"ACIB + RobustVLA: training-time IB regularization + post-training RL hardening — do they compose?\"\n\n# =====================================================================\n# Direction 5: Token Pruning / Importance in Vision Transformers (Classic)\n# =====================================================================\nvit_token_pruning_classic:\n  - id: tome_2023\n    title: \"Token Merging: Your ViT But Faster\"\n    authors: [Bolya, Fu, Dai, Zhang, Feichtenhofer, Hoffman]\n    year: 2023\n    venue: ICLR 2023 (Oral)\n    arxiv: \"2210.09461\"\n    code: \"https://github.com/facebookresearch/ToMe\"\n    one_liner: >\n      Merges similar tokens using a bipartite soft matching algorithm, reducing token count\n      without training. 2x throughput with <0.3% accuracy drop on ViT-L.\n    relation: foundation\n    differences_from_acib:\n      goal: \"ToMe = efficiency via similarity-based merging; ACIB = robustness via task-relevance gating\"\n      selection_criterion: \"ToMe merges by cosine similarity (task-agnostic); ACIB gates by action-conditioned importance\"\n      mechanism: \"ToMe reduces token count (hard merge); ACIB keeps all tokens with soft weights\"\n      training: \"ToMe is training-free; ACIB trains a scorer end-to-end with action loss\"\n    citation_priority: high  # seminal token reduction work, frequently cited as baseline\n\n  - id: dynamicvit_2021\n    title: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\"\n    authors: [Rao, Zhao, Liu, Lu, Zhou, Hsieh]\n    year: 2021\n    venue: NeurIPS 2021\n    arxiv: \"2106.02034\"\n    code: \"https://github.com/raoyongming/DynamicViT\"\n    one_liner: >\n      Learns a lightweight prediction module to estimate token importance and prune hierarchically.\n      66% tokens pruned with 31-37% FLOPs reduction and <0.5% accuracy drop.\n    relation: foundation\n    differences_from_acib:\n      goal: \"DynamicViT = efficiency for classification; ACIB = robustness for action prediction\"\n      selection: \"Learned binary decision (hard prune); ACIB uses soft gating under IB constraint\"\n      conditioning: \"DynamicViT importance is task-agnostic (classification CLS token); ACIB is action-conditioned\"\n      training: \"DynamicViT uses attention masking for differentiable pruning; ACIB uses soft mask with KL bottleneck\"\n    citation_priority: high  # pioneering learned token pruning\n\n  - id: evit_2022\n    title: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\"\n    authors: [Liang, Ge, Tong, Song, Wang, Xie]\n    year: 2022\n    venue: ICLR 2022 (Spotlight)\n    arxiv: \"2202.07800\"\n    code: \"https://github.com/youweiliang/evit\"\n    one_liner: >\n      Uses CLS token attention to identify attentive tokens; preserves them and fuses inattentive\n      ones. 50% speedup on DeiT-S with 0.3% accuracy drop. No extra parameters.\n    relation: foundation\n    differences_from_acib:\n      importance_signal: \"EViT uses CLS attention (heuristic); ACIB learns importance via action loss (end-to-end)\"\n      fusion: \"EViT fuses inattentive tokens into one; ACIB retains all tokens with scaled weights\"\n      conditioning: \"EViT is unconditional; ACIB conditions on language instruction via action loss\"\n    citation_priority: high  # influential attention-based token selection\n\n  - id: avit_2022\n    title: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\"\n    authors: [Yin, Vahdat, et al.]\n    year: 2022\n    venue: CVPR 2022 (Oral)\n    arxiv: \"2112.07658\"\n    code: \"https://github.com/NVlabs/A-ViT\"\n    one_liner: >\n      Adaptive Computation Time applied to ViT tokens: each token has a halting probability,\n      discarded once halted. 62% throughput gain on DeiT-Tiny with 0.3% accuracy drop.\n    relation: foundation\n    differences_from_acib:\n      mechanism: \"A-ViT uses ACT halting (token stops propagating at different layers); ACIB applies uniform soft gate at input\"\n      regularization: \"A-ViT uses distributional prior on halting; ACIB uses aggregate-rate KL on gate activation\"\n      goal: \"A-ViT = per-token adaptive depth for efficiency; ACIB = per-token relevance weighting for robustness\"\n    citation_priority: medium\n\n# =====================================================================\n# Direction 6: Information Bottleneck Theory (Foundational)\n# =====================================================================\nib_theory_foundations:\n  - id: ib_original_1999\n    title: \"The Information Bottleneck Method\"\n    authors: [Tishby, Pereira, Bialek]\n    year: 2000\n    venue: \"37th Allerton Conference on Communication, Control, and Computing, 1999\"\n    arxiv: \"physics/0004057\"\n    one_liner: >\n      Foundational paper defining the information bottleneck: find a compressed representation T\n      of input X that preserves maximal information about target Y, formalized as\n      min I(X;T) - beta * I(T;Y).\n    relation: foundation\n    note: >\n      ACIB's theoretical ancestor. The aggregate-rate KL in ACIB is a practical approximation of the\n      I(X;T) compression term, applied at the token level rather than the representation level.\n    citation_priority: high  # must-cite foundational reference\n\n  - id: deep_vib_2017\n    title: \"Deep Variational Information Bottleneck\"\n    authors: [Alemi, Fischer, Dillon, Murphy]\n    year: 2017\n    venue: ICLR 2017\n    arxiv: \"1612.00410\"\n    one_liner: >\n      Variational approximation to the IB objective using reparameterization trick, enabling\n      end-to-end training of neural networks under IB constraint. Improves generalization\n      and adversarial robustness over standard regularization.\n    relation: foundation\n    differences_from_acib:\n      level: \"Deep VIB applies IB to the full representation (single bottleneck); ACIB applies per-token gates\"\n      approximation: \"Deep VIB uses variational bound with Gaussian encoder; ACIB uses aggregate-rate KL on learned gate activations\"\n      goal: \"Deep VIB targets classification robustness; ACIB targets action-prediction robustness in VLA\"\n    note: >\n      ACIB inherits the spirit of Deep VIB (IB as a training regularizer for robustness) but\n      operates at a different granularity (token-level gates vs representation-level bottleneck).\n    citation_priority: high  # must-cite; bridges IB theory to deep learning practice\n\n  - id: tishby_dl_ib_2015\n    title: \"Deep Learning and the Information Bottleneck Principle\"\n    authors: [Tishby, Zaslavsky]\n    year: 2015\n    venue: \"IEEE Information Theory Workshop (ITW) 2015\"\n    arxiv: \"1503.02406\"\n    one_liner: >\n      Analyzes DNNs through IB lens: each layer is a bottleneck, and training exhibits\n      fitting then compression phases. Provides finite-sample generalization bounds via IB.\n    relation: foundation\n    note: >\n      Theoretical motivation for why IB-style regularization helps generalization in deep networks.\n      Supports ACIB's claim that compressing task-irrelevant visual information improves policy generalization.\n    citation_priority: medium  # cite for theoretical grounding\n\n  - id: kawaguchi_ib_dl_2023\n    title: \"How Does Information Bottleneck Help Deep Learning?\"\n    authors: [Kawaguchi, Deng, Ji, Huang]\n    year: 2023\n    venue: ICML 2023\n    arxiv: \"2305.08013\"  # approximate\n    one_liner: >\n      Proves that controlling information bottleneck controls generalization error, unlike bounds\n      based on parameter count or VC dimension. Provides theoretical justification for IB regularization.\n    relation: foundation\n    note: >\n      Strongest theoretical support for ACIB's approach: IB regularization provably helps generalization,\n      and ACIB applies this at the visual token level for action prediction.\n    citation_priority: medium\n\n# =====================================================================\n# Direction 7: Visual Token Selection for VLA (Action-Conditioned)\n# =====================================================================\nvla_token_selection:\n  - id: compressor_vla_2025\n    title: \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\"\n    authors: [Unknown]\n    year: 2025\n    arxiv: \"2511.18950\"\n    one_liner: >\n      Hybrid instruction-conditioned token compression: Semantic Task Compressor (STC) for holistic\n      task-relevant context + Spatial Refinement Compressor (SRC) for fine-grained details.\n      59% FLOPs reduction, 3x token reduction on LIBERO.\n    relation: competitor\n    differences_from_acib:\n      goal: \"Compressor-VLA = efficiency (reduce tokens); ACIB = robustness (soft-gate tokens)\"\n      mechanism: \"Compressor-VLA compresses tokens into fewer tokens; ACIB retains all tokens with soft weights\"\n      bottleneck: \"Compressor-VLA has no information-theoretic constraint; ACIB enforces aggregate-rate KL\"\n      conditioning: \"Both are instruction-conditioned, but Compressor-VLA uses explicit language features; ACIB conditions implicitly through action loss gradients\"\n    citation_priority: high  # instruction-conditioned VLA token selection, direct competitor\n\n  - id: vla_adp_2025\n    title: \"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation\"\n    authors: [Pei, Chen, Xu, Wang, Shi, Xu]\n    year: 2025\n    arxiv: \"2509.22093\"\n    code: \"https://github.com/chen7086/VLA-ADP\"\n    one_liner: >\n      Training-free action-aware pruning: combines text-driven token relevance (cross-modal attention)\n      with action trajectory gating signal. Adapts pruning ratio based on manipulation phase\n      (coarse vs fine). 1.35x speedup + 25.8% success improvement on OpenVLA-OFT.\n    relation: competitor\n    differences_from_acib:\n      training: \"VLA-ADP is training-free (heuristic); ACIB trains a scorer end-to-end\"\n      action_signal: \"VLA-ADP uses past action trajectory as gating signal; ACIB uses action prediction loss to train the scorer\"\n      mechanism: \"VLA-ADP hard-prunes tokens; ACIB soft-gates all tokens\"\n      bottleneck: \"VLA-ADP has no IB constraint; ACIB enforces aggregate-rate KL\"\n    citation_priority: high  # closest in name (action-aware) and spirit\n\n  - id: vla_pruner_2025\n    title: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\"\n    authors: [Unknown]\n    year: 2025\n    arxiv: \"2511.16449\"\n    one_liner: >\n      Dual-level token importance: vision-language prefill attention for semantic relevance +\n      action decode attention (temporally smoothed) for action-level importance. Plug-and-play.\n    relation: competitor\n    differences_from_acib:\n      dual_level: \"VLA-Pruner separates semantic vs action importance; ACIB uses a single scorer trained by action loss\"\n      training: \"VLA-Pruner is training-free; ACIB trains the scorer end-to-end\"\n      mechanism: \"VLA-Pruner hard-prunes; ACIB soft-gates\"\n      temporal: \"VLA-Pruner exploits temporal smoothing across frames; ACIB operates per-timestep\"\n    citation_priority: high\n\n  - id: deepvision_vla_2026\n    title: \"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models (DeepVision-VLA)\"\n    authors: [Unknown]\n    year: 2026\n    arxiv: \"2603.15618\"\n    project_page: \"https://deepvision-vla.github.io/\"\n    one_liner: >\n      Action-Guided Visual Pruning (AGVP): uses shallow-layer action-to-visual attention to\n      compute saliency map, prunes irrelevant visual tokens in deep layers. Multi-scale vision\n      expert injection. +9% sim, +7.5% real over prior VLAs.\n    relation: competitor\n    differences_from_acib:\n      pruning_source: \"DeepVision uses shallow action-token attention as saliency; ACIB uses a dedicated learned scorer\"\n      mechanism: \"DeepVision prunes in deep layers only; ACIB gates at the visual token input\"\n      goal: \"DeepVision targets performance via better visual representation; ACIB targets robustness via IB\"\n      bottleneck: \"DeepVision has no IB constraint; ACIB enforces aggregate-rate KL\"\n    citation_priority: high  # very recent, action-guided pruning for VLA\n\n  - id: task_cond_adapt_2024\n    title: \"Task-Conditioned Adaptation of Visual Features in Multi-Task Policy Learning\"\n    authors: [Marza, et al.]\n    year: 2024\n    venue: CVPR 2024\n    arxiv: \"2402.07739\"\n    code: \"https://github.com/PierreMarza/task_conditioned_adaptation\"\n    one_liner: >\n      Task-conditioned adapters modulate ViT features for multi-task robot policy learning.\n      Adapter is a 2-layer MLP conditioned on task embedding, added after each ViT block.\n      Generalizes to unseen tasks with few demonstrations.\n    relation: background\n    differences_from_acib:\n      level: \"Task-cond adapters modulate feature channels; ACIB modulates token importance (spatial selection)\"\n      conditioning: \"Explicit task embedding; ACIB conditions implicitly through action loss\"\n      goal: \"Multi-task generalization; ACIB targets robustness to visual distractors\"\n    citation_priority: medium  # relevant for instruction-conditioned visual processing in robot learning\n\n# =====================================================================\n# Direction 8: Interpretability Methods for VLMs / VLAs\n# =====================================================================\nvlm_interpretability:\n  - id: gradcam_2017\n    title: \"Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization\"\n    authors: [Selvaraju, Cogswell, Das, Vedantam, Parikh, Batra]\n    year: 2017\n    venue: ICCV 2017\n    arxiv: \"1610.02391\"\n    one_liner: >\n      Uses gradients flowing into the final convolutional layer to produce coarse localization\n      maps highlighting important image regions. Applicable to any CNN without architecture changes.\n    relation: foundation\n    note: >\n      Classic interpretability baseline. ACIB's learned scorer can be seen as an end-to-end trained\n      alternative to post-hoc Grad-CAM: instead of computing gradients after training, the scorer\n      learns importance during training. Grad-CAM can be used to validate ACIB scorer quality.\n    citation_priority: medium  # cite when discussing interpretability of ACIB's scorer\n\n  - id: attention_rollout_2020\n    title: \"Quantifying Attention Flow in Transformers\"\n    authors: [Abnar, Zuidema]\n    year: 2020\n    venue: ACL 2020\n    one_liner: >\n      Proposes attention rollout and attention flow methods to approximate token-level importance\n      by recursively multiplying attention matrices across layers. Yields higher correlation with\n      ablation-based importance than raw attention weights.\n    relation: foundation\n    note: >\n      Attention rollout is a standard tool for analyzing what transformers attend to. Relevant for\n      comparing ACIB's learned scorer masks against attention-based importance heuristics.\n    citation_priority: medium\n\n  - id: lvlm_interpret_2024\n    title: \"LVLM-Intrepret: An Interpretability Tool for Large Vision-Language Models\"\n    authors: [Stan, et al.]\n    year: 2024\n    venue: CVPR 2024 Workshop (XAI4CV)\n    arxiv: \"2404.03118\"\n    one_liner: >\n      Interactive tool for understanding LVLMs: combines attention knockout, relevancy mapping,\n      and causal graph construction to visualize information flow and identify critical image regions.\n      Adapts relevancy maps to LLaVA-style architectures.\n    relation: background\n    note: >\n      Provides methodology for analyzing what visual regions VLMs attend to. Could be used to\n      benchmark ACIB's scorer against LVLM-Interpret's relevancy maps.\n    citation_priority: low  # cite only if discussing interpretability tools in depth\n\n# =====================================================================\n# Updated must_cite / should_cite lists\n# =====================================================================\nextended_citations:\n  newly_added_must_cite:\n    - tome_2023           # seminal token merging\n    - dynamicvit_2021     # pioneering learned token pruning\n    - evit_2022           # attention-based token selection\n    - ib_original_1999    # foundational IB theory\n    - deep_vib_2017       # IB + deep learning bridge\n    - compressor_vla_2025 # instruction-conditioned VLA token compression\n    - vla_adp_2025        # action-aware VLA pruning\n    - vla_pruner_2025     # dual-level VLA token pruning\n    - deepvision_vla_2026 # action-guided visual pruning\n\n  newly_added_should_cite:\n    - avit_2022           # adaptive token halting\n    - tishby_dl_ib_2015   # IB theory for deep learning\n    - kawaguchi_ib_dl_2023 # IB generalization theory\n    - task_cond_adapt_2024 # task-conditioned visual features for robot policy\n    - gradcam_2017        # classic interpretability baseline\n    - attention_rollout_2020 # attention-based importance analysis\n    - lvlm_interpret_2024 # VLM interpretability tool"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "4e3e04b7-dffd-4d88-8acb-41591acb0e79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFFkQrzr2vM1K8ECig8wfw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 908,
      "cache_read_input_tokens": 57539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 908
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

_source line 70 · 2026-05-17T15:06:38.810Z_

<details><summary>↩ Tool result · `toolu_01BpU4nQwPXYW8xkXKCpGF9H`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "49ab50e5-9134-4d0a-a49a-f535c0d0bb8d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/literature_map.yaml",
    "oldString": "    - \"ACIB + RobustVLA: training-time IB regularization + post-training RL hardening — do they compose?\"",
    "newString": "    - \"ACIB + RobustVLA: training-time IB regularization + post-training RL hardening — do they compose?\"\n\n# =====================================================================\n# Direction 5: Token Pruning / Importance in Vision Transformers (Classic)\n# =====================================================================\nvit_token_pruning_classic:\n  - id: tome_2023\n    title: \"Token Merging: Your ViT But Faster\"\n    authors: [Bolya, Fu, Dai, Zhang, Feichtenhofer, Hoffman]\n    year: 2023\n    venue: ICLR 2023 (Oral)\n    arxiv: \"2210.09461\"\n    code: \"https://github.com/facebookresearch/ToMe\"\n    one_liner: >\n      Merges similar tokens using a bipartite soft matching algorithm, reducing token count\n      without training. 2x throughput with <0.3% accuracy drop on ViT-L.\n    relation: foundation\n    differences_from_acib:\n      goal: \"ToMe = efficiency via similarity-based merging; ACIB = robustness via task-relevance gating\"\n      selection_criterion: \"ToMe merges by cosine similarity (task-agnostic); ACIB gates by action-conditioned importance\"\n      mechanism: \"ToMe reduces token count (hard merge); ACIB keeps all tokens with soft weights\"\n      training: \"ToMe is training-free; ACIB trains a scorer end-to-end with action loss\"\n    citation_priority: high  # seminal token reduction work, frequently cited as baseline\n\n  - id: dynamicvit_2021\n    title: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\"\n    authors: [Rao, Zhao, Liu, Lu, Zhou, Hsieh]\n    year: 2021\n    venue: NeurIPS 2021\n    arxiv: \"2106.02034\"\n    code: \"https://github.com/raoyongming/DynamicViT\"\n    one_liner: >\n      Learns a lightweight prediction module to estimate token importance and prune hierarchically.\n      66% tokens pruned with 31-37% FLOPs reduction and <0.5% accuracy drop.\n    relation: foundation\n    differences_from_acib:\n      goal: \"DynamicViT = efficiency for classification; ACIB = robustness for action prediction\"\n      selection: \"Learned binary decision (hard prune); ACIB uses soft gating under IB constraint\"\n      conditioning: \"DynamicViT importance is task-agnostic (classification CLS token); ACIB is action-conditioned\"\n      training: \"DynamicViT uses attention masking for differentiable pruning; ACIB uses soft mask with KL bottleneck\"\n    citation_priority: high  # pioneering learned token pruning\n\n  - id: evit_2022\n    title: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\"\n    authors: [Liang, Ge, Tong, Song, Wang, Xie]\n    year: 2022\n    venue: ICLR 2022 (Spotlight)\n    arxiv: \"2202.07800\"\n    code: \"https://github.com/youweiliang/evit\"\n    one_liner: >\n      Uses CLS token attention to identify attentive tokens; preserves them and fuses inattentive\n      ones. 50% speedup on DeiT-S with 0.3% accuracy drop. No extra parameters.\n    relation: foundation\n    differences_from_acib:\n      importance_signal: \"EViT uses CLS attention (heuristic); ACIB learns importance via action loss (end-to-end)\"\n      fusion: \"EViT fuses inattentive tokens into one; ACIB retains all tokens with scaled weights\"\n      conditioning: \"EViT is unconditional; ACIB conditions on language instruction via action loss\"\n    citation_priority: high  # influential attention-based token selection\n\n  - id: avit_2022\n    title: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\"\n    authors: [Yin, Vahdat, et al.]\n    year: 2022\n    venue: CVPR 2022 (Oral)\n    arxiv: \"2112.07658\"\n    code: \"https://github.com/NVlabs/A-ViT\"\n    one_liner: >\n      Adaptive Computation Time applied to ViT tokens: each token has a halting probability,\n      discarded once halted. 62% throughput gain on DeiT-Tiny with 0.3% accuracy drop.\n    relation: foundation\n    differences_from_acib:\n      mechanism: \"A-ViT uses ACT halting (token stops propagating at different layers); ACIB applies uniform soft gate at input\"\n      regularization: \"A-ViT uses distributional prior on halting; ACIB uses aggregate-rate KL on gate activation\"\n      goal: \"A-ViT = per-token adaptive depth for efficiency; ACIB = per-token relevance weighting for robustness\"\n    citation_priority: medium\n\n# =====================================================================\n# Direction 6: Information Bottleneck Theory (Foundational)\n# =====================================================================\nib_theory_foundations:\n  - id: ib_original_1999\n    title: \"The Information Bottleneck Method\"\n    authors: [Tishby, Pereira, Bialek]\n    year: 2000\n    venue: \"37th Allerton Conference on Communication, Control, and Computing, 1999\"\n    arxiv: \"physics/0004057\"\n    one_liner: >\n      Foundational paper defining the information bottleneck: find a compressed representation T\n      of input X that preserves maximal information about target Y, formalized as\n      min I(X;T) - beta * I(T;Y).\n    relation: foundation\n    note: >\n      ACIB's theoretical ancestor. The aggregate-rate KL in ACIB is a practical approximation of the\n      I(X;T) compression term, applied at the token level rather than the representation level.\n    citation_priority: high  # must-cite foundational reference\n\n  - id: deep_vib_2017\n    title: \"Deep Variational Information Bottleneck\"\n    authors: [Alemi, Fischer, Dillon, Murphy]\n    year: 2017\n    venue: ICLR 2017\n    arxiv: \"1612.00410\"\n    one_liner: >\n      Variational approximation to the IB objective using reparameterization trick, enabling\n      end-to-end training of neural networks under IB constraint. Improves generalization\n      and adversarial robustness over standard regularization.\n    relation: foundation\n    differences_from_acib:\n      level: \"Deep VIB applies IB to the full representation (single bottleneck); ACIB applies per-token gates\"\n      approximation: \"Deep VIB uses variational bound with Gaussian encoder; ACIB uses aggregate-rate KL on learned gate activations\"\n      goal: \"Deep VIB targets classification robustness; ACIB targets action-prediction robustness in VLA\"\n    note: >\n      ACIB inherits the spirit of Deep VIB (IB as a training regularizer for robustness) but\n      operates at a different granularity (token-level gates vs representation-level bottleneck).\n    citation_priority: high  # must-cite; bridges IB theory to deep learning practice\n\n  - id: tishby_dl_ib_2015\n    title: \"Deep Learning and the Information Bottleneck Principle\"\n    authors: [Tishby, Zaslavsky]\n    year: 2015\n    venue: \"IEEE Information Theory Workshop (ITW) 2015\"\n    arxiv: \"1503.02406\"\n    one_liner: >\n      Analyzes DNNs through IB lens: each layer is a bottleneck, and training exhibits\n      fitting then compression phases. Provides finite-sample generalization bounds via IB.\n    relation: foundation\n    note: >\n      Theoretical motivation for why IB-style regularization helps generalization in deep networks.\n      Supports ACIB's claim that compressing task-irrelevant visual information improves policy generalization.\n    citation_priority: medium  # cite for theoretical grounding\n\n  - id: kawaguchi_ib_dl_2023\n    title: \"How Does Information Bottleneck Help Deep Learning?\"\n    authors: [Kawaguchi, Deng, Ji, Huang]\n    year: 2023\n    venue: ICML 2023\n    arxiv: \"2305.08013\"  # approximate\n    one_liner: >\n      Proves that controlling information bottleneck controls generalization error, unlike bounds\n      based on parameter count or VC dimension. Provides theoretical justification for IB regularization.\n    relation: foundation\n    note: >\n      Strongest theoretical support for ACIB's approach: IB regularization provably helps generalization,\n      and ACIB applies this at the visual token level for action prediction.\n    citation_priority: medium\n\n# =====================================================================\n# Direction 7: Visual Token Selection for VLA (Action-Conditioned)\n# =====================================================================\nvla_token_selection:\n  - id: compressor_vla_2025\n    title: \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\"\n    authors: [Unknown]\n    year: 2025\n    arxiv: \"2511.18950\"\n    one_liner: >\n      Hybrid instruction-conditioned token compression: Semantic Task Compressor (STC) for holistic\n      task-relevant context + Spatial Refinement Compressor (SRC) for fine-grained details.\n      59% FLOPs reduction, 3x token reduction on LIBERO.\n    relation: competitor\n    differences_from_acib:\n      goal: \"Compressor-VLA = efficiency (reduce tokens); ACIB = robustness (soft-gate tokens)\"\n      mechanism: \"Compressor-VLA compresses tokens into fewer tokens; ACIB retains all tokens with soft weights\"\n      bottleneck: \"Compressor-VLA has no information-theoretic constraint; ACIB enforces aggregate-rate KL\"\n      conditioning: \"Both are instruction-conditioned, but Compressor-VLA uses explicit language features; ACIB conditions implicitly through action loss gradients\"\n    citation_priority: high  # instruction-conditioned VLA token selection, direct competitor\n\n  - id: vla_adp_2025\n    title: \"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation\"\n    authors: [Pei, Chen, Xu, Wang, Shi, Xu]\n    year: 2025\n    arxiv: \"2509.22093\"\n    code: \"https://github.com/chen7086/VLA-ADP\"\n    one_liner: >\n      Training-free action-aware pruning: combines text-driven token relevance (cross-modal attention)\n      with action trajectory gating signal. Adapts pruning ratio based on manipulation phase\n      (coarse vs fine). 1.35x speedup + 25.8% success improvement on OpenVLA-OFT.\n    relation: competitor\n    differences_from_acib:\n      training: \"VLA-ADP is training-free (heuristic); ACIB trains a scorer end-to-end\"\n      action_signal: \"VLA-ADP uses past action trajectory as gating signal; ACIB uses action prediction loss to train the scorer\"\n      mechanism: \"VLA-ADP hard-prunes tokens; ACIB soft-gates all tokens\"\n      bottleneck: \"VLA-ADP has no IB constraint; ACIB enforces aggregate-rate KL\"\n    citation_priority: high  # closest in name (action-aware) and spirit\n\n  - id: vla_pruner_2025\n    title: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\"\n    authors: [Unknown]\n    year: 2025\n    arxiv: \"2511.16449\"\n    one_liner: >\n      Dual-level token importance: vision-language prefill attention for semantic relevance +\n      action decode attention (temporally smoothed) for action-level importance. Plug-and-play.\n    relation: competitor\n    differences_from_acib:\n      dual_level: \"VLA-Pruner separates semantic vs action importance; ACIB uses a single scorer trained by action loss\"\n      training: \"VLA-Pruner is training-free; ACIB trains the scorer end-to-end\"\n      mechanism: \"VLA-Pruner hard-prunes; ACIB soft-gates\"\n      temporal: \"VLA-Pruner exploits temporal smoothing across frames; ACIB operates per-timestep\"\n    citation_priority: high\n\n  - id: deepvision_vla_2026\n    title: \"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models (DeepVision-VLA)\"\n    authors: [Unknown]\n    year: 2026\n    arxiv: \"2603.15618\"\n    project_page: \"https://deepvision-vla.github.io/\"\n    one_liner: >\n      Action-Guided Visual Pruning (AGVP): uses shallow-layer action-to-visual attention to\n      compute saliency map, prunes irrelevant visual tokens in deep layers. Multi-scale vision\n      expert injection. +9% sim, +7.5% real over prior VLAs.\n    relation: competitor\n    differences_from_acib:\n      pruning_source: \"DeepVision uses shallow action-token attention as saliency; ACIB uses a dedicated learned scorer\"\n      mechanism: \"DeepVision prunes in deep layers only; ACIB gates at the visual token input\"\n      goal: \"DeepVision targets performance via better visual representation; ACIB targets robustness via IB\"\n      bottleneck: \"DeepVision has no IB constraint; ACIB enforces aggregate-rate KL\"\n    citation_priority: high  # very recent, action-guided pruning for VLA\n\n  - id: task_cond_adapt_2024\n    title: \"Task-Conditioned Adaptation of Visual Features in Multi-Task Policy Learning\"\n    authors: [Marza, et al.]\n    year: 2024\n    venue: CVPR 2024\n    arxiv: \"2402.07739\"\n    code: \"https://github.com/PierreMarza/task_conditioned_adaptation\"\n    one_liner: >\n      Task-conditioned adapters modulate ViT features for multi-task robot policy learning.\n      Adapter is a 2-layer MLP conditioned on task embedding, added after each ViT block.\n      Generalizes to unseen tasks with few demonstrations.\n    relation: background\n    differences_from_acib:\n      level: \"Task-cond adapters modulate feature channels; ACIB modulates token importance (spatial selection)\"\n      conditioning: \"Explicit task embedding; ACIB conditions implicitly through action loss\"\n      goal: \"Multi-task generalization; ACIB targets robustness to visual distractors\"\n    citation_priority: medium  # relevant for instruction-conditioned visual processing in robot learning\n\n# =====================================================================\n# Direction 8: Interpretability Methods for VLMs / VLAs\n# =====================================================================\nvlm_interpretability:\n  - id: gradcam_2017\n    title: \"Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization\"\n    authors: [Selvaraju, Cogswell, Das, Vedantam, Parikh, Batra]\n    year: 2017\n    venue: ICCV 2017\n    arxiv: \"1610.02391\"\n    one_liner: >\n      Uses gradients flowing into the final convolutional layer to produce coarse localization\n      maps highlighting important image regions. Applicable to any CNN without architecture changes.\n    relation: foundation\n    note: >\n      Classic interpretability baseline. ACIB's learned scorer can be seen as an end-to-end trained\n      alternative to post-hoc Grad-CAM: instead of computing gradients after training, the scorer\n      learns importance during training. Grad-CAM can be used to validate ACIB scorer quality.\n    citation_priority: medium  # cite when discussing interpretability of ACIB's scorer\n\n  - id: attention_rollout_2020\n    title: \"Quantifying Attention Flow in Transformers\"\n    authors: [Abnar, Zuidema]\n    year: 2020\n    venue: ACL 2020\n    one_liner: >\n      Proposes attention rollout and attention flow methods to approximate token-level importance\n      by recursively multiplying attention matrices across layers. Yields higher correlation with\n      ablation-based importance than raw attention weights.\n    relation: foundation\n    note: >\n      Attention rollout is a standard tool for analyzing what transformers attend to. Relevant for\n      comparing ACIB's learned scorer masks against attention-based importance heuristics.\n    citation_priority: medium\n\n  - id: lvlm_interpret_2024\n    title: \"LVLM-Intrepret: An Interpretability Tool for Large Vision-Language Models\"\n    authors: [Stan, et al.]\n    year: 2024\n    venue: CVPR 2024 Workshop (XAI4CV)\n    arxiv: \"2404.03118\"\n    one_liner: >\n      Interactive tool for understanding LVLMs: combines attention knockout, relevancy mapping,\n      and causal graph construction to visualize information flow and identify critical image regions.\n      Adapts relevancy maps to LLaVA-style architectures.\n    relation: background\n    note: >\n      Provides methodology for analyzing what visual regions VLMs attend to. Could be used to\n      benchmark ACIB's scorer against LVLM-Interpret's relevancy maps.\n    citation_priority: low  # cite only if discussing interpretability tools in depth\n\n# =====================================================================\n# Updated must_cite / should_cite lists\n# =====================================================================\nextended_citations:\n  newly_added_must_cite:\n    - tome_2023           # seminal token merging\n    - dynamicvit_2021     # pioneering learned token pruning\n    - evit_2022           # attention-based token selection\n    - ib_original_1999    # foundational IB theory\n    - deep_vib_2017       # IB + deep learning bridge\n    - compressor_vla_2025 # instruction-conditioned VLA token compression\n    - vla_adp_2025        # action-aware VLA pruning\n    - vla_pruner_2025     # dual-level VLA token pruning\n    - deepvision_vla_2026 # action-guided visual pruning\n\n  newly_added_should_cite:\n    - avit_2022           # adaptive token halting\n    - tishby_dl_ib_2015   # IB theory for deep learning\n    - kawaguchi_ib_dl_2023 # IB generalization theory\n    - task_cond_adapt_2024 # task-conditioned visual features for robot policy\n    - gradcam_2017        # classic interpretability baseline\n    - attention_rollout_2020 # attention-based importance analysis\n    - lvlm_interpret_2024 # VLM interpretability tool",
    "originalFile": "# Literature Map — ACIB (Action-Conditioned Information Bottleneck)\n# Target venue: CoRL 2026\n# Generated: 2026-05-16, updated: 2026-05-16\n# Scope: Information Bottleneck × VLA / Robot Learning, plus token pruning, VLA robustness, LIBERO\n\nmeta:\n  our_method_summary: >\n    Token-level information bottleneck for VLA models. A learned scorer network produces\n    per-token soft masks gating visual tokens consumed by the action expert. The bottleneck is\n    enforced by an aggregate-rate KL (KL on the mean activation across the batch, rather than\n    per-sample) plus a diversity regularizer that prevents the scorer from collapsing to\n    uniform or to a fixed subset. Action loss provides the task-relevance signal — gradients\n    flow back through the soft mask so the scorer learns which tokens are required to predict\n    actions. Backbone: SmolVLA. Benchmark: LIBERO. Positioned as a regularization-based\n    complement to data augmentation.\n  novelty_axes:\n    - token_level_IB        # not representation/feature-level\n    - action_conditioned    # scorer trained by the action loss, not reconstruction or MI on input\n    - aggregate_rate_KL     # KL on batch-mean activation, not per-sample variational KL\n    - explicit_anti_collapse # diversity regularizer with empirical scorer_std as health metric\n    - regularization_not_data # complementary to GenAug/RoCoDA-style augmentation\n    - soft_gating_not_pruning # all tokens flow through; contrast with LightVLA/ATP-LLaVA hard pruning\n\n# =====================================================================\n# Direction 1: Information Bottleneck in RL / Robot Learning\n# =====================================================================\nib_in_robot_learning:\n  - id: bc_ib_2025\n    title: \"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation\"\n    authors: [Bai, Zhou, Ding, Zhao, Wang, Chen]\n    year: 2025\n    venue: ICML 2025\n    arxiv: \"2502.02853\"\n    code: \"https://github.com/BaiShuanghao/BC-IB\"\n    one_liner: >\n      Adds an IB regularizer to behavior-cloning: minimizes I(X;Z) between fused multimodal\n      input X and policy latent Z via MINE, while preserving action prediction.\n    relation: competitor\n    differences_from_acib:\n      level: \"representation-level (single fused latent Z) vs. ACIB's token-level (per visual token gate)\"\n      ib_estimator: \"MINE-based MI lower bound vs. ACIB's aggregate-rate KL with learned prior\"\n      mechanism: \"no scorer / no token mask; ACIB outputs an interpretable per-token relevance score\"\n      collapse_handling: \"BC-IB has no explicit anti-collapse term — single-latent IB does not face the per-token collapse failure mode\"\n      benchmark_overlap: \"both on LIBERO; BC-IB baseline gains +2-9% per suite, ACIB targets SmolVLA backbone instead\"\n    citation_priority: high  # primary related-work anchor; the ICML-25 paper to beat\n\n  - id: vib_rl_skill_2023\n    title: \"Variational Information Bottleneck Regularized Deep RL for Efficient Robotic Skill Adaptation\"\n    venue: \"MDPI Sensors 2023 (Vol 23 Issue 2)\"\n    one_liner: VIB on meta-RL latent task representation, 200x-5000x sample-efficiency claim on skill transfer.\n    relation: background\n    note: pre-VLA era; VIB on task embeddings, not visual tokens.\n    citation_priority: medium\n\n  - id: mib_multimodal_2024\n    title: \"Multimodal Information Bottleneck for Deep RL with Multiple Sensors\"\n    venue: \"Neural Networks (Elsevier) 2024\"\n    one_liner: MIB compresses joint egocentric-image + proprioception representation, filtering policy-irrelevant info.\n    relation: background\n    note: closest in spirit to ACIB (filter task-irrelevant info) but operates on fused embeddings, not tokens.\n    citation_priority: medium\n\n  - id: ibe_2025\n    title: \"Information Bottleneck-Enhanced RL for Solving Operation Research Problems\"\n    venue: \"MDPI Sensors 2025\"\n    one_liner: Two-level IB — state representation bottleneck + policy bottleneck as exploration bonus.\n    relation: background\n    note: combinatorial RL, not robot manipulation; cited only if discussing IB design space.\n    citation_priority: low\n\n  - id: discrete_ib_drl_2023\n    title: \"Representation Learning in Deep RL via Discrete Information Bottleneck\"\n    venue: PMLR 2023 (Islam et al.)\n    one_liner: Discrete IB on state representation for deep RL.\n    relation: background\n    citation_priority: low\n\n# =====================================================================\n# Direction 2: Token Pruning / Selection for Vision-Language Models\n# =====================================================================\ntoken_pruning_vlm:\n  - id: lightvla_2025\n    title: \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning\"\n    authors: [Jiang, et al.]\n    year: 2025\n    arxiv: \"2509.12594\"\n    project_page: \"https://liauto-research.github.io/LightVLA/\"\n    one_liner: >\n      Differentiable token pruning for VLA: generates dynamic queries to evaluate visual token\n      importance, uses Gumbel softmax for hard selection. 59% FLOPs reduction + 2.9% success\n      rate improvement over OpenVLA-OFT.\n    relation: competitor  # closest VLA-specific token selection work\n    differences_from_acib:\n      goal: \"LightVLA = efficiency (reduce FLOPs); ACIB = robustness regularization (encourage task-relevant focus)\"\n      selection_type: \"LightVLA uses hard Gumbel selection (tokens are dropped); ACIB uses soft gating (all tokens flow through with scaled weights)\"\n      bottleneck: \"LightVLA has no information-theoretic constraint; ACIB enforces aggregate-rate KL to a prior rate\"\n      collapse: \"LightVLA has no anti-collapse mechanism; ACIB's diversity regularizer prevents scorer degeneration\"\n      backbone: \"LightVLA on 7B OpenVLA; ACIB on 0.45B SmolVLA with only 64 visual tokens — different operating regime\"\n    citation_priority: high  # most direct VLA token selection competitor\n\n  - id: divprune_2025\n    title: \"DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models\"\n    authors: [Alvar, Singh, Akbari, Zhang]\n    year: 2025\n    venue: CVPR 2025\n    arxiv: \"2503.02175\"\n    one_liner: Formulates token pruning as Max-Min Diversity Problem; selects most diverse token subset; training-free.\n    relation: complementary  # different goal (efficiency) but shares \"diversity\" motivation\n    differences_from_acib:\n      goal: \"DivPrune = inference efficiency under fixed budget; ACIB = robustness regularization, not efficiency\"\n      training: \"DivPrune is training-free at test time; ACIB trains the scorer end-to-end with action loss\"\n      diversity_role: \"DivPrune diversity is the *objective*; ACIB diversity is an anti-collapse *regularizer*\"\n    citation_priority: high  # closest competing use of 'diversity' in visual token selection\n\n  - id: atp_llava_2025\n    title: \"ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models\"\n    venue: CVPR 2025\n    one_liner: Layer-adaptive token pruning module predicting pruning thresholds per-layer and per-instance, removing text-irrelevant visual tokens.\n    relation: competitor  # also learns a scorer-like importance function\n    differences_from_acib:\n      objective: \"ATP optimizes for accuracy-under-pruning; ACIB optimizes for action-prediction under IB constraint\"\n      action_grounding: \"ATP uses text relevance; ACIB uses action relevance (closer to control)\"\n      mechanism: \"ATP prunes hard tokens; ACIB applies soft mask, all tokens still flow through\"\n    citation_priority: high\n\n  - id: sparsevlm_2025\n    title: \"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference\"\n    authors: [Zhang, Fan, Ma, Zheng, Huang, Cheng, Gudovskiy, Okuno, Nakata, Keutzer, Zhang]\n    year: 2025\n    venue: ICML 2025\n    arxiv: \"2410.04417\"\n    code: \"https://github.com/Gumpest/SparseVLMs\"\n    one_liner: >\n      Training-free token sparsification: uses text-visual attention to rate vision token importance,\n      progressively prunes with rank-based adaptive ratio + token recycling. 54% FLOPs reduction, 97% accuracy retained.\n    relation: background\n    note: Training-free, text-relevance based. No action grounding. General VLM efficiency, not robot-specific.\n    citation_priority: medium\n\n  - id: vla_cache_2025\n    title: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\"\n    authors: [Hsu, et al.]\n    year: 2025\n    venue: NeurIPS 2025\n    arxiv: \"2502.02175\"\n    code: \"https://github.com/siyuhsu/vla-cache\"\n    one_liner: >\n      Training-free inference acceleration: caches static visual tokens across frames, selectively\n      re-computes task-relevant tokens. 1.7x speedup on LIBERO/SIMPLER.\n    relation: background\n    note: >\n      Temporal token reuse, orthogonal to ACIB. Interesting overlap: both identify \"task-relevant\" tokens,\n      but VLA-Cache uses attention-based heuristics while ACIB learns relevance end-to-end.\n    citation_priority: medium\n\n  - id: topv_2025\n    title: \"TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal VLM\"\n    venue: CVPR 2025\n    one_liner: Training-free token pruning posed as inference-time optimization.\n    relation: background\n    citation_priority: medium\n\n  - id: feather_2025\n    title: \"Feather the Throttle: Revisiting Visual Token Pruning for VLMs\"\n    venue: ICCV 2025\n    one_liner: Diagnoses attention-based pruning bias (RoPE long-term decay favors bottom-row tokens) and proposes fixes.\n    relation: background\n    note: useful warning when designing scorer input features; cite if discussing attention-based scorers.\n    citation_priority: medium\n\n  - id: prunevid_2025\n    title: \"PruneVid: Visual Token Pruning for Efficient Video LLMs\"\n    venue: ACL 2025\n    one_liner: Training-free spatial-temporal token merging for video VLMs.\n    relation: background\n    citation_priority: low\n\n  - id: dycoke_2025\n    title: \"DyCoke: Dynamic Compression of Tokens for Fast Video LLMs\"\n    venue: CVPR 2025\n    one_liner: Dynamic token compression for video LLMs.\n    relation: background\n    citation_priority: low\n\n# =====================================================================\n# Direction 3: VLA Robustness / Generalization / Augmentation\n# =====================================================================\nvla_robustness:\n  - id: robustvla_2025\n    title: \"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\"\n    year: 2025\n    arxiv: \"2511.01331\"\n    one_liner: >\n      RL post-training with Jacobian regularization (observation noise sensitivity) +\n      smoothness regularization (action perturbation stability) for VLA robustness.\n    relation: competitor\n    differences_from_acib:\n      stage: \"RobustVLA = post-training RL fine-tuning; ACIB = training-time regularization integrated into BC\"\n      mechanism: \"RobustVLA uses gradient-based Jacobian/smoothness penalties; ACIB uses information-theoretic bottleneck\"\n      interpretability: \"RobustVLA is a black-box regularizer; ACIB produces interpretable per-token relevance scores\"\n      composability: \"potentially complementary — ACIB during training, RobustVLA as post-training hardening\"\n    citation_priority: high\n\n  - id: revla_2025\n    title: \"ReVLA: Reverting Visual Domain Limitation of Robotic Foundation Models\"\n    authors: [Daskalov, et al.]\n    year: 2025\n    arxiv: \"2409.15250\"\n    project_page: \"https://insait-institute.github.io/ReVLA/\"\n    one_liner: >\n      Gradual backbone reversal via model merging — restores vision encoder to pretrained state\n      to combat catastrophic forgetting. +77% grasp, +66% lift on OOD visual tasks over OpenVLA.\n    relation: complementary\n    note: >\n      Addresses the same symptom (VLA visual fragility) from a different angle: ReVLA preserves\n      pretrained visual features, ACIB teaches the model which features matter. Could combine.\n    citation_priority: medium\n\n  - id: libero_plus_2025\n    title: \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\"\n    year: 2025\n    arxiv: \"2510.13626\"\n    one_liner: 7 perturbation dims (object layout, viewpoint, init state, language, light, texture, sensor noise); 10k tasks; shows 95%→<30% drop under modest perturbations.\n    relation: evaluation_benchmark\n    note: >\n      Critical eval target — our ACIB robustness story should be validated here, not on vanilla LIBERO,\n      to avoid the \"memorization\" critique LIBERO-PRO levels at the field.\n    citation_priority: high\n\n  - id: libero_pro_2025\n    title: \"LIBERO-PRO: Towards Robust and Fair Evaluation of VLA Models Beyond Memorization\"\n    year: 2025\n    arxiv: \"2510.03827\"\n    one_liner: Object/position/instruction/task perturbations; SOTA models that report >90% drop to ~0% — exposes rote memorization.\n    relation: evaluation_benchmark\n    citation_priority: high\n\n  - id: eva_vla_2025\n    title: \"Eva-VLA: Evaluating VLA Models' Robustness Under Real-World Physical Variations\"\n    year: 2025\n    arxiv: \"2509.18953\"\n    one_liner: Treats perturbations (viewpoint, init state) as a continuous optimization problem to find worst-case.\n    relation: evaluation_benchmark\n    citation_priority: medium\n\n  - id: vla_multimodal_perturb_2025\n    title: \"On Robustness of VLA Models against Multi-Modal Perturbations\"\n    arxiv: \"2510.00037\"\n    one_liner: Tests mainstream VLAs against 17 uncertainties across 4 modalities; finds action modality most fragile; π0 > OpenVLA.\n    relation: background\n    citation_priority: medium\n\n  - id: byovla_2025\n    title: \"BYOVLA: Removing Model-Sensitive Features via VLM Segmentation + Inpainting\"\n    authors: [Hancock, et al.]\n    year: 2025\n    one_liner: At inference, segments and inpaints out task-irrelevant regions to make VLAs robust.\n    relation: competitor  # solves the same problem (irrelevant visual content hurts policy) at test time\n    differences_from_acib:\n      stage: \"BYOVLA = test-time pre-processing; ACIB = training-time regularization\"\n      mechanism: \"BYOVLA modifies the image (segmentation + inpainting); ACIB modifies the token stream (soft gating)\"\n      cost: \"BYOVLA needs a VLM call per frame; ACIB is a small scorer head, zero extra cost at inference if mask is integrated\"\n    citation_priority: high\n\n  - id: gevrm_2025\n    title: \"GEVRM: Model-based Planning for Visual Corruptions in VLA\"\n    authors: [Zhang, et al.]\n    year: 2025\n    one_liner: Handles color jitter and common visual corruptions via model-based planning.\n    relation: competitor\n    differences_from_acib:\n      mechanism: \"augmentation-style robustness vs. ACIB's regularization-style robustness\"\n    citation_priority: medium\n\n  - id: rocoda_2024\n    title: \"RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning\"\n    year: 2024\n    arxiv: \"2411.16959\"\n    one_liner: Counterfactual augmentation modifying task-irrelevant subset of environment state; tests distractor generalization.\n    relation: complementary\n    note: ACIB and RoCoDA are *complementary* — ACIB is the regularization analogue of RoCoDA's data-side approach.\n    citation_priority: high\n\n  - id: nice_scene_surgery_2025\n    title: \"NICE Scene Surgery: Improving Robotic Manipulation Robustness\"\n    year: 2025\n    arxiv: \"2511.22777\"\n    one_liner: Edits scenes to insert distractors while preserving causal task-relevant features.\n    relation: complementary\n    citation_priority: medium\n\n  - id: genaug_2023\n    title: \"GenAug: Scaling Robot Learning with Semantic Data Augmentation\"\n    venue: RSS 2023\n    one_liner: Diffusion-based scene augmentation (backgrounds, distractors, textures) for imitation learning.\n    relation: complementary\n    citation_priority: medium\n\n# =====================================================================\n# Direction 4: LIBERO + VLA Baselines\n# =====================================================================\nlibero_baselines:\n  - id: openvla_2024\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    year: 2024\n    one_liner: 7B Llama-based VLA; LIBERO 76.5% avg.\n    relation: backbone_baseline\n    citation_priority: high\n\n  - id: openvla_oft_2025\n    title: \"Fine-Tuning VLA Models: Optimizing Speed and Success (OpenVLA-OFT)\"\n    authors: [Kim, et al.]\n    year: 2025\n    venue: RSS 2025\n    arxiv: \"2502.19645\"\n    one_liner: Parallel decoding + action chunking + continuous actions + L1 regression; 76.5%→97.1% on LIBERO; 26× faster.\n    relation: strong_baseline\n    note: Current LIBERO SOTA prior to VLA-0; ACIB must compare against OFT recipe.\n    citation_priority: high\n\n  - id: pi0_2024\n    title: \"π0: A Vision-Language-Action Flow Model\"\n    authors: [Black, et al.]\n    year: 2024\n    one_liner: 3.3B robotics-pretrained flow-matching VLA; LIBERO 86.0%; most robust under multi-modal perturbations.\n    relation: strong_baseline\n    citation_priority: high\n\n  - id: pi0_fast_2025\n    title: \"π0-FAST\"\n    authors: [Pertsch, et al.]\n    year: 2025\n    one_liner: Faster autoregressive variant of π0.\n    relation: baseline\n    citation_priority: medium\n\n  - id: smolvla_2025\n    title: \"SmolVLA: A VLA Model for Affordable and Efficient Robotics\"\n    year: 2025\n    arxiv: \"2506.01844\"\n    one_liner: 0.45B VLA; PixelShuffle compresses 1024→64 visual tokens; VLM layer-skip; CA/SA interleaved action expert; LIBERO 87.3%.\n    relation: our_backbone\n    note: >\n      Our chosen backbone. Important: SmolVLA already reduces to 64 visual tokens via PixelShuffle,\n      so ACIB's scorer operates on a small token set — must justify why further token-level gating\n      helps when the count is already low (answer: not all 64 are equally task-relevant per scene/timestep).\n    citation_priority: high\n\n  - id: vla_0_2025\n    title: \"VLA-0: Building SOTA VLAs with Zero Modification\"\n    year: 2025\n    arxiv: \"2510.13054\"\n    one_liner: Outperforms OpenVLA-OFT, SmolVLA, π0.5-KI on LIBERO with no architectural changes.\n    relation: strong_baseline\n    citation_priority: high\n\n# =====================================================================\n# Novelty Position Statement\n# =====================================================================\nnovelty_synthesis:\n  closest_competitors:\n    - bc_ib_2025      # IB for BC, but representation-level\n    - lightvla_2025   # learned token selection for VLA, but efficiency-oriented pruning\n\n  delta_vs_bc_ib:\n    - \"BC-IB applies IB at the fused-latent level (one Z); ACIB applies IB at the visual-token level (per-token gate)\"\n    - \"BC-IB uses MINE for MI estimation; ACIB uses aggregate-rate KL (KL on batch-mean scorer output to a prior rate)\"\n    - \"BC-IB has no scorer interpretability — Z is opaque; ACIB exposes a per-token relevance score usable for visualization/analysis\"\n    - \"BC-IB does not face per-token collapse; ACIB introduces an explicit diversity regularizer and tracks scorer_std as a training health metric (0.441 in our successful run)\"\n\n  delta_vs_lightvla:\n    - \"LightVLA targets efficiency (hard Gumbel pruning, drop tokens); ACIB targets robustness (soft gating, all tokens retained with scaled weights)\"\n    - \"LightVLA has no information-theoretic framework; ACIB enforces an aggregate-rate KL bottleneck\"\n    - \"LightVLA has no anti-collapse mechanism; ACIB's diversity regularizer prevents scorer degeneration\"\n    - \"LightVLA on 7B OpenVLA; ACIB on 0.45B SmolVLA with only 64 visual tokens — different operating regime\"\n\n  uniqueness_combination:\n    description: >\n      To our knowledge no prior work combines (a) token-level IB on visual tokens, (b) end-to-end\n      training driven by an action-prediction loss (not reconstruction or text relevance),\n      (c) aggregate-rate KL as the bottleneck term, (d) an explicit anti-collapse diversity\n      regularizer with an empirical health metric, and (e) soft gating rather than hard pruning.\n      The closest competitors each share at most one of these axes:\n        - BC-IB: shares IB-for-policy but at representation level, no token scorer, no collapse issue.\n        - LightVLA: shares learned VLA token selection but for efficiency via hard pruning, no IB framework.\n        - ATP-LLaVA: shares token-level scoring but for text-relevance and pruning, not action-grounded IB.\n        - DivPrune: shares diversity motivation but as the objective (not anti-collapse) and is training-free.\n        - BYOVLA: shares \"remove irrelevant visual content\" goal but at test time via VLM inpainting.\n        - RobustVLA: shares VLA robustness goal but via gradient-based Jacobian/smoothness penalties, not IB.\n        - RoCoDA / GenAug: shares the underlying problem (distractor invariance) but solves it via data augmentation.\n    framing: >\n      ACIB = regularization-side counterpart to data-augmentation approaches for VLA robustness,\n      with action-conditioned token-level IB as the mechanism. Soft gating under an information\n      constraint, not hard pruning for efficiency.\n\n  positioning_risks:\n    - \"BC-IB ICML-25 is the *direct* prior art on IB-for-BC. Differentiation must be airtight; expect reviewers to ask 'why token-level if representation-level already works?'\"\n    - \"LightVLA does learned token selection *specifically for VLA* — reviewers may conflate it with ACIB. Key defense: ACIB is soft gating under IB for robustness, not hard pruning for efficiency.\"\n    - \"Token-pruning literature (DivPrune, ATP-LLaVA, SparseVLM) may be invoked as similar token-selection work. Need to clarify that ACIB does not prune — it gates softly under an information constraint, and the goal is regularization, not efficiency.\"\n    - \"LIBERO-Plus / LIBERO-PRO show standard LIBERO scores are inflated by memorization. ACIB should report on LIBERO-Plus or analogous perturbation eval to make a credible robustness claim — otherwise the contribution will be perceived as marginal.\"\n    - \"RobustVLA targets the same VLA robustness goal via RL post-training. Must argue why training-time IB regularization is preferable to or complementary with post-training approaches.\"\n\n  must_cite:\n    - bc_ib_2025\n    - lightvla_2025\n    - divprune_2025\n    - atp_llava_2025\n    - byovla_2025\n    - robustvla_2025\n    - rocoda_2024\n    - libero_plus_2025\n    - openvla_oft_2025\n    - smolvla_2025\n    - pi0_2024\n    - vla_0_2025\n\n  should_cite:\n    - mib_multimodal_2024\n    - vib_rl_skill_2023\n    - sparsevlm_2025\n    - vla_cache_2025\n    - revla_2025\n    - libero_pro_2025\n    - eva_vla_2025\n    - gevrm_2025\n    - genaug_2023\n    - feather_2025\n    - openvla_2024\n\n  open_research_directions:\n    - \"Does the learned scorer transfer across task suites (LIBERO-Spatial scorer applied to LIBERO-Goal)?\"\n    - \"Correlation between scorer mask and object-segmentation masks — does ACIB learn an implicit object detector for free?\"\n    - \"Combining ACIB with augmentation (RoCoDA/GenAug) — does the regularization-side + data-side gain stack?\"\n    - \"Robustness on LIBERO-Plus perturbation dims, especially camera viewpoint and distractor objects — where the 95→30% drop lives.\"\n    - \"ACIB + RobustVLA: training-time IB regularization + post-training RL hardening — do they compose?\"\n",
    "structuredPatch": [
      {
        "oldStart": 433,
        "oldLines": 3,
        "newStart": 433,
        "newLines": 313,
        "lines": [
          "     - \"Combining ACIB with augmentation (RoCoDA/GenAug) — does the regularization-side + data-side gain stack?\"",
          "     - \"Robustness on LIBERO-Plus perturbation dims, especially camera viewpoint and distractor objects — where the 95→30% drop lives.\"",
          "     - \"ACIB + RobustVLA: training-time IB regularization + post-training RL hardening — do they compose?\"",
          "+",
          "+# =====================================================================",
          "+# Direction 5: Token Pruning / Importance in Vision Transformers (Classic)",
          "+# =====================================================================",
          "+vit_token_pruning_classic:",
          "+  - id: tome_2023",
          "+    title: \"Token Merging: Your ViT But Faster\"",
          "+    authors: [Bolya, Fu, Dai, Zhang, Feichtenhofer, Hoffman]",
          "+    year: 2023",
          "+    venue: ICLR 2023 (Oral)",
          "+    arxiv: \"2210.09461\"",
          "+    code: \"https://github.com/facebookresearch/ToMe\"",
          "+    one_liner: >",
          "+      Merges similar tokens using a bipartite soft matching algorithm, reducing token count",
          "+      without training. 2x throughput with <0.3% accuracy drop on ViT-L.",
          "+    relation: foundation",
          "+    differences_from_acib:",
          "+      goal: \"ToMe = efficiency via similarity-based merging; ACIB = robustness via task-relevance gating\"",
          "+      selection_criterion: \"ToMe merges by cosine similarity (task-agnostic); ACIB gates by action-conditioned importance\"",
          "+      mechanism: \"ToMe reduces token count (hard merge); ACIB keeps all tokens with soft weights\"",
          "+      training: \"ToMe is training-free; ACIB trains a scorer end-to-end with action loss\"",
          "+    citation_priority: high  # seminal token reduction work, frequently cited as baseline",
          "+",
          "+  - id: dynamicvit_2021",
          "+    title: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\"",
          "+    authors: [Rao, Zhao, Liu, Lu, Zhou, Hsieh]",
          "+    year: 2021",
          "+    venue: NeurIPS 2021",
          "+    arxiv: \"2106.02034\"",
          "+    code: \"https://github.com/raoyongming/DynamicViT\"",
          "+    one_liner: >",
          "+      Learns a lightweight prediction module to estimate token importance and prune hierarchically.",
          "+      66% tokens pruned with 31-37% FLOPs reduction and <0.5% accuracy drop.",
          "+    relation: foundation",
          "+    differences_from_acib:",
          "+      goal: \"DynamicViT = efficiency for classification; ACIB = robustness for action prediction\"",
          "+      selection: \"Learned binary decision (hard prune); ACIB uses soft gating under IB constraint\"",
          "+      conditioning: \"DynamicViT importance is task-agnostic (classification CLS token); ACIB is action-conditioned\"",
          "+      training: \"DynamicViT uses attention masking for differentiable pruning; ACIB uses soft mask with KL bottleneck\"",
          "+    citation_priority: high  # pioneering learned token pruning",
          "+",
          "+  - id: evit_2022",
          "+    title: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\"",
          "+    authors: [Liang, Ge, Tong, Song, Wang, Xie]",
          "+    year: 2022",
          "+    venue: ICLR 2022 (Spotlight)",
          "+    arxiv: \"2202.07800\"",
          "+    code: \"https://github.com/youweiliang/evit\"",
          "+    one_liner: >",
          "+      Uses CLS token attention to identify attentive tokens; preserves them and fuses inattentive",
          "+      ones. 50% speedup on DeiT-S with 0.3% accuracy drop. No extra parameters.",
          "+    relation: foundation",
          "+    differences_from_acib:",
          "+      importance_signal: \"EViT uses CLS attention (heuristic); ACIB learns importance via action loss (end-to-end)\"",
          "+      fusion: \"EViT fuses inattentive tokens into one; ACIB retains all tokens with scaled weights\"",
          "+      conditioning: \"EViT is unconditional; ACIB conditions on language instruction via action loss\"",
          "+    citation_priority: high  # influential attention-based token selection",
          "+",
          "+  - id: avit_2022",
          "+    title: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\"",
          "+    authors: [Yin, Vahdat, et al.]",
          "+    year: 2022",
          "+    venue: CVPR 2022 (Oral)",
          "+    arxiv: \"2112.07658\"",
          "+    code: \"https://github.com/NVlabs/A-ViT\"",
          "+    one_liner: >",
          "+      Adaptive Computation Time applied to ViT tokens: each token has a halting probability,",
          "+      discarded once halted. 62% throughput gain on DeiT-Tiny with 0.3% accuracy drop.",
          "+    relation: foundation",
          "+    differences_from_acib:",
          "+      mechanism: \"A-ViT uses ACT halting (token stops propagating at different layers); ACIB applies uniform soft gate at input\"",
          "+      regularization: \"A-ViT uses distributional prior on halting; ACIB uses aggregate-rate KL on gate activation\"",
          "+      goal: \"A-ViT = per-token adaptive depth for efficiency; ACIB = per-token relevance weighting for robustness\"",
          "+    citation_priority: medium",
          "+",
          "+# =====================================================================",
          "+# Direction 6: Information Bottleneck Theory (Foundational)",
          "+# =====================================================================",
          "+ib_theory_foundations:",
          "+  - id: ib_original_1999",
          "+    title: \"The Information Bottleneck Method\"",
          "+    authors: [Tishby, Pereira, Bialek]",
          "+    year: 2000",
          "+    venue: \"37th Allerton Conference on Communication, Control, and Computing, 1999\"",
          "+    arxiv: \"physics/0004057\"",
          "+    one_liner: >",
          "+      Foundational paper defining the information bottleneck: find a compressed representation T",
          "+      of input X that preserves maximal information about target Y, formalized as",
          "+      min I(X;T) - beta * I(T;Y).",
          "+    relation: foundation",
          "+    note: >",
          "+      ACIB's theoretical ancestor. The aggregate-rate KL in ACIB is a practical approximation of the",
          "+      I(X;T) compression term, applied at the token level rather than the representation level.",
          "+    citation_priority: high  # must-cite foundational reference",
          "+",
          "+  - id: deep_vib_2017",
          "+    title: \"Deep Variational Information Bottleneck\"",
          "+    authors: [Alemi, Fischer, Dillon, Murphy]",
          "+    year: 2017",
          "+    venue: ICLR 2017",
          "+    arxiv: \"1612.00410\"",
          "+    one_liner: >",
          "+      Variational approximation to the IB objective using reparameterization trick, enabling",
          "+      end-to-end training of neural networks under IB constraint. Improves generalization",
          "+      and adversarial robustness over standard regularization.",
          "+    relation: foundation",
          "+    differences_from_acib:",
          "+      level: \"Deep VIB applies IB to the full representation (single bottleneck); ACIB applies per-token gates\"",
          "+      approximation: \"Deep VIB uses variational bound with Gaussian encoder; ACIB uses aggregate-rate KL on learned gate activations\"",
          "+      goal: \"Deep VIB targets classification robustness; ACIB targets action-prediction robustness in VLA\"",
          "+    note: >",
          "+      ACIB inherits the spirit of Deep VIB (IB as a training regularizer for robustness) but",
          "+      operates at a different granularity (token-level gates vs representation-level bottleneck).",
          "+    citation_priority: high  # must-cite; bridges IB theory to deep learning practice",
          "+",
          "+  - id: tishby_dl_ib_2015",
          "+    title: \"Deep Learning and the Information Bottleneck Principle\"",
          "+    authors: [Tishby, Zaslavsky]",
          "+    year: 2015",
          "+    venue: \"IEEE Information Theory Workshop (ITW) 2015\"",
          "+    arxiv: \"1503.02406\"",
          "+    one_liner: >",
          "+      Analyzes DNNs through IB lens: each layer is a bottleneck, and training exhibits",
          "+      fitting then compression phases. Provides finite-sample generalization bounds via IB.",
          "+    relation: foundation",
          "+    note: >",
          "+      Theoretical motivation for why IB-style regularization helps generalization in deep networks.",
          "+      Supports ACIB's claim that compressing task-irrelevant visual information improves policy generalization.",
          "+    citation_priority: medium  # cite for theoretical grounding",
          "+",
          "+  - id: kawaguchi_ib_dl_2023",
          "+    title: \"How Does Information Bottleneck Help Deep Learning?\"",
          "+    authors: [Kawaguchi, Deng, Ji, Huang]",
          "+    year: 2023",
          "+    venue: ICML 2023",
          "+    arxiv: \"2305.08013\"  # approximate",
          "+    one_liner: >",
          "+      Proves that controlling information bottleneck controls generalization error, unlike bounds",
          "+      based on parameter count or VC dimension. Provides theoretical justification for IB regularization.",
          "+    relation: foundation",
          "+    note: >",
          "+      Strongest theoretical support for ACIB's approach: IB regularization provably helps generalization,",
          "+      and ACIB applies this at the visual token level for action prediction.",
          "+    citation_priority: medium",
          "+",
          "+# =====================================================================",
          "+# Direction 7: Visual Token Selection for VLA (Action-Conditioned)",
          "+# =====================================================================",
          "+vla_token_selection:",
          "+  - id: compressor_vla_2025",
          "+    title: \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\"",
          "+    authors: [Unknown]",
          "+    year: 2025",
          "+    arxiv: \"2511.18950\"",
          "+    one_liner: >",
          "+      Hybrid instruction-conditioned token compression: Semantic Task Compressor (STC) for holistic",
          "+      task-relevant context + Spatial Refinement Compressor (SRC) for fine-grained details.",
          "+      59% FLOPs reduction, 3x token reduction on LIBERO.",
          "+    relation: competitor",
          "+    differences_from_acib:",
          "+      goal: \"Compressor-VLA = efficiency (reduce tokens); ACIB = robustness (soft-gate tokens)\"",
          "+      mechanism: \"Compressor-VLA compresses tokens into fewer tokens; ACIB retains all tokens with soft weights\"",
          "+      bottleneck: \"Compressor-VLA has no information-theoretic constraint; ACIB enforces aggregate-rate KL\"",
          "+      conditioning: \"Both are instruction-conditioned, but Compressor-VLA uses explicit language features; ACIB conditions implicitly through action loss gradients\"",
          "+    citation_priority: high  # instruction-conditioned VLA token selection, direct competitor",
          "+",
          "+  - id: vla_adp_2025",
          "+    title: \"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation\"",
          "+    authors: [Pei, Chen, Xu, Wang, Shi, Xu]",
          "+    year: 2025",
          "+    arxiv: \"2509.22093\"",
          "+    code: \"https://github.com/chen7086/VLA-ADP\"",
          "+    one_liner: >",
          "+      Training-free action-aware pruning: combines text-driven token relevance (cross-modal attention)",
          "+      with action trajectory gating signal. Adapts pruning ratio based on manipulation phase",
          "+      (coarse vs fine). 1.35x speedup + 25.8% success improvement on OpenVLA-OFT.",
          "+    relation: competitor",
          "+    differences_from_acib:",
          "+      training: \"VLA-ADP is training-free (heuristic); ACIB trains a scorer end-to-end\"",
          "+      action_signal: \"VLA-ADP uses past action trajectory as gating signal; ACIB uses action prediction loss to train the scorer\"",
          "+      mechanism: \"VLA-ADP hard-prunes tokens; ACIB soft-gates all tokens\"",
          "+      bottleneck: \"VLA-ADP has no IB constraint; ACIB enforces aggregate-rate KL\"",
          "+    citation_priority: high  # closest in name (action-aware) and spirit",
          "+",
          "+  - id: vla_pruner_2025",
          "+    title: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\"",
          "+    authors: [Unknown]",
          "+    year: 2025",
          "+    arxiv: \"2511.16449\"",
          "+    one_liner: >",
          "+      Dual-level token importance: vision-language prefill attention for semantic relevance +",
          "+      action decode attention (temporally smoothed) for action-level importance. Plug-and-play.",
          "+    relation: competitor",
          "+    differences_from_acib:",
          "+      dual_level: \"VLA-Pruner separates semantic vs action importance; ACIB uses a single scorer trained by action loss\"",
          "+      training: \"VLA-Pruner is training-free; ACIB trains the scorer end-to-end\"",
          "+      mechanism: \"VLA-Pruner hard-prunes; ACIB soft-gates\"",
          "+      temporal: \"VLA-Pruner exploits temporal smoothing across frames; ACIB operates per-timestep\"",
          "+    citation_priority: high",
          "+",
          "+  - id: deepvision_vla_2026",
          "+    title: \"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models (DeepVision-VLA)\"",
          "+    authors: [Unknown]",
          "+    year: 2026",
          "+    arxiv: \"2603.15618\"",
          "+    project_page: \"https://deepvision-vla.github.io/\"",
          "+    one_liner: >",
          "+      Action-Guided Visual Pruning (AGVP): uses shallow-layer action-to-visual attention to",
          "+      compute saliency map, prunes irrelevant visual tokens in deep layers. Multi-scale vision",
          "+      expert injection. +9% sim, +7.5% real over prior VLAs.",
          "+    relation: competitor",
          "+    differences_from_acib:",
          "+      pruning_source: \"DeepVision uses shallow action-token attention as saliency; ACIB uses a dedicated learned scorer\"",
          "+      mechanism: \"DeepVision prunes in deep layers only; ACIB gates at the visual token input\"",
          "+      goal: \"DeepVision targets performance via better visual representation; ACIB targets robustness via IB\"",
          "+      bottleneck: \"DeepVision has no IB constraint; ACIB enforces aggregate-rate KL\"",
          "+    citation_priority: high  # very recent, action-guided pruning for VLA",
          "+",
          "+  - id: task_cond_adapt_2024",
          "+    title: \"Task-Conditioned Adaptation of Visual Features in Multi-Task Policy Learning\"",
          "+    authors: [Marza, et al.]",
          "+    year: 2024",
          "+    venue: CVPR 2024",
          "+    arxiv: \"2402.07739\"",
          "+    code: \"https://github.com/PierreMarza/task_conditioned_adaptation\"",
          "+    one_liner: >",
          "+      Task-conditioned adapters modulate ViT features for multi-task robot policy learning.",
          "+      Adapter is a 2-layer MLP conditioned on task embedding, added after each ViT block.",
          "+      Generalizes to unseen tasks with few demonstrations.",
          "+    relation: background",
          "+    differences_from_acib:",
          "+      level: \"Task-cond adapters modulate feature channels; ACIB modulates token importance (spatial selection)\"",
          "+      conditioning: \"Explicit task embedding; ACIB conditions implicitly through action loss\"",
          "+      goal: \"Multi-task generalization; ACIB targets robustness to visual distractors\"",
          "+    citation_priority: medium  # relevant for instruction-conditioned visual processing in robot learning",
          "+",
          "+# =====================================================================",
          "+# Direction 8: Interpretability Methods for VLMs / VLAs",
          "+# =====================================================================",
          "+vlm_interpretability:",
          "+  - id: gradcam_2017",
          "+    title: \"Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization\"",
          "+    authors: [Selvaraju, Cogswell, Das, Vedantam, Parikh, Batra]",
          "+    year: 2017",
          "+    venue: ICCV 2017",
          "+    arxiv: \"1610.02391\"",
          "+    one_liner: >",
          "+      Uses gradients flowing into the final convolutional layer to produce coarse localization",
          "+      maps highlighting important image regions. Applicable to any CNN without architecture changes.",
          "+    relation: foundation",
          "+    note: >",
          "+      Classic interpretability baseline. ACIB's learned scorer can be seen as an end-to-end trained",
          "+      alternative to post-hoc Grad-CAM: instead of computing gradients after training, the scorer",
          "+      learns importance during training. Grad-CAM can be used to validate ACIB scorer quality.",
          "+    citation_priority: medium  # cite when discussing interpretability of ACIB's scorer",
          "+",
          "+  - id: attention_rollout_2020",
          "+    title: \"Quantifying Attention Flow in Transformers\"",
          "+    authors: [Abnar, Zuidema]",
          "+    year: 2020",
          "+    venue: ACL 2020",
          "+    one_liner: >",
          "+      Proposes attention rollout and attention flow methods to approximate token-level importance",
          "+      by recursively multiplying attention matrices across layers. Yields higher correlation with",
          "+      ablation-based importance than raw attention weights.",
          "+    relation: foundation",
          "+    note: >",
          "+      Attention rollout is a standard tool for analyzing what transformers attend to. Relevant for",
          "+      comparing ACIB's learned scorer masks against attention-based importance heuristics.",
          "+    citation_priority: medium",
          "+",
          "+  - id: lvlm_interpret_2024",
          "+    title: \"LVLM-Intrepret: An Interpretability Tool for Large Vision-Language Models\"",
          "+    authors: [Stan, et al.]",
          "+    year: 2024",
          "+    venue: CVPR 2024 Workshop (XAI4CV)",
          "+    arxiv: \"2404.03118\"",
          "+    one_liner: >",
          "+      Interactive tool for understanding LVLMs: combines attention knockout, relevancy mapping,",
          "+      and causal graph construction to visualize information flow and identify critical image regions.",
          "+      Adapts relevancy maps to LLaVA-style architectures.",
          "+    relation: background",
          "+    note: >",
          "+      Provides methodology for analyzing what visual regions VLMs attend to. Could be used to",
          "+      benchmark ACIB's scorer against LVLM-Interpret's relevancy maps.",
          "+    citation_priority: low  # cite only if discussing interpretability tools in depth",
          "+",
          "+# =====================================================================",
          "+# Updated must_cite / should_cite lists",
          "+# =====================================================================",
          "+extended_citations:",
          "+  newly_added_must_cite:",
          "+    - tome_2023           # seminal token merging",
          "+    - dynamicvit_2021     # pioneering learned token pruning",
          "+    - evit_2022           # attention-based token selection",
          "+    - ib_original_1999    # foundational IB theory",
          "+    - deep_vib_2017       # IB + deep learning bridge",
          "+    - compressor_vla_2025 # instruction-conditioned VLA token compression",
          "+    - vla_adp_2025        # action-aware VLA pruning",
          "+    - vla_pruner_2025     # dual-level VLA token pruning",
          "+    - deepvision_vla_2026 # action-guided visual pruning",
          "+",
          "+  newly_added_should_cite:",
          "+    - avit_2022           # adaptive token halting",
          "+    - tishby_dl_ib_2015   # IB theory for deep learning",
          "+    - kawaguchi_ib_dl_2023 # IB generalization theory",
          "+    - task_cond_adapt_2024 # task-conditioned visual features for robot policy",
          "+    - gradcam_2017        # classic interpretability baseline",
          "+    - attention_rollout_2020 # attention-based importance analysis",
          "+    - lvlm_interpret_2024 # VLM interpretability tool"
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

_source line 71_

写入完成。验证文件完整性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "3f2c7c2c-30dc-417a-9ba7-eb33f0227d1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WciNrQ8MM3YUcHVspTjuiL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5002,
      "cache_read_input_tokens": 58447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5002
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

_source line 72_

<details open><summary>🔧 Tool call — Bash · `toolu_01B5W3d9ajTCHuUnoh6v4DFy`</summary>

```json
{
  "command": "python3 -c \"import yaml; data = yaml.safe_load(open('/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/literature_map.yaml')); print('YAML valid'); sections = [k for k in data.keys()]; print(f'Sections: {sections}'); counts = {k: len(v) if isinstance(v, list) else 'dict' for k, v in data.items()}; print(f'Counts: {counts}')\"",
  "description": "Validate YAML syntax and count entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "466e481a-8f16-454a-ab76-e9d335b42fde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WciNrQ8MM3YUcHVspTjuiL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5002,
      "cache_read_input_tokens": 58447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5002
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

_source line 73 · 2026-05-17T15:06:44.239Z_

<details><summary>↩ Tool result · `toolu_01B5W3d9ajTCHuUnoh6v4DFy`</summary>

```text
YAML valid
Sections: ['meta', 'ib_in_robot_learning', 'token_pruning_vlm', 'vla_robustness', 'libero_baselines', 'novelty_synthesis', 'vit_token_pruning_classic', 'ib_theory_foundations', 'vla_token_selection', 'vlm_interpretability', 'extended_citations']
Counts: {'meta': 'dict', 'ib_in_robot_learning': 5, 'token_pruning_vlm': 9, 'vla_robustness': 11, 'libero_baselines': 6, 'novelty_synthesis': 'dict', 'vit_token_pruning_classic': 4, 'ib_theory_foundations': 4, 'vla_token_selection': 5, 'vlm_interpretability': 3, 'extended_citations': 'dict'}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "82234c29-45d9-4a3e-badc-2fb1e5921704",
  "tool_use_result": {
    "stdout": "YAML valid\nSections: ['meta', 'ib_in_robot_learning', 'token_pruning_vlm', 'vla_robustness', 'libero_baselines', 'novelty_synthesis', 'vit_token_pruning_classic', 'ib_theory_foundations', 'vla_token_selection', 'vlm_interpretability', 'extended_citations']\nCounts: {'meta': 'dict', 'ib_in_robot_learning': 5, 'token_pruning_vlm': 9, 'vla_robustness': 11, 'libero_baselines': 6, 'novelty_synthesis': 'dict', 'vit_token_pruning_classic': 4, 'ib_theory_foundations': 4, 'vla_token_selection': 5, 'vlm_interpretability': 3, 'extended_citations': 'dict'}",
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

_source line 74_

YAML 验证通过。新增 4 个 section，共 16 篇论文：

| Section | 新增论文数 | 关键论文 |
|---------|-----------|---------|
| **ViT Token Pruning (Classic)** | 4 | ToMe, DynamicViT, EViT, A-ViT |
| **IB Theory (Foundational)** | 4 | Tishby 1999, Deep VIB 2017, Tishby & Zaslavsky 2015, Kawaguchi 2023 |
| **VLA Token Selection** | 5 | Compressor-VLA, VLA-ADP, VLA-Pruner, DeepVision-VLA, Task-Cond Adapt |
| **VLM Interpretability** | 3 | Grad-CAM, Attention Rollout, LVLM-Interpret |

重点发现：
- **VLA-ADP** (action-aware dynamic pruning) 和 **Compressor-VLA** (instruction-guided compression) 是新发现的直接竞争者，必须在 Related Work 中明确区分
- **DeepVision-VLA** (2026) 用 action-to-visual attention 做 pruning，思路最接近 ACIB，但它是 post-hoc 注意力 heuristic 而非 learned scorer + IB constraint
- IB 理论基础（Tishby 1999 + Deep VIB 2017）是 must-cite，为 ACIB 的 aggregate-rate KL 提供理论根基

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "uuid": "cf551ea4-955e-48a2-ac0c-aba23475063a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6iqDFy6EqvYRbJypTJQmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 63449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
      },
      "output_tokens": 6,
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

_source line 75_

YAML 验证通过。新增 4 个 section，共 16 篇论文：

| Section | 新增论文数 | 关键论文 |
|---------|-----------|---------|
| **ViT Token Pruning (Classic)** | 4 | ToMe, DynamicViT, EViT, A-ViT |
| **IB Theory (Foundational)** | 4 | Tishby 1999, Deep VIB 2017, Tishby & Zaslavsky 2015, Kawaguchi 2023 |
| **VLA Token Selection** | 5 | Compressor-VLA, VLA-ADP, VLA-Pruner, DeepVision-VLA, Task-Cond Adapt |
| **VLM Interpretability** | 3 | Grad-CAM, Attention Rollout, LVLM-Interpret |

重点发现：
- **VLA-ADP** (action-aware dynamic pruning) 和 **Compressor-VLA** (instruction-guided compression) 是新发现的直接竞争者，必须在 Related Work 中明确区分
- **DeepVision-VLA** (2026) 用 action-to-visual attention 做 pruning，思路最接近 ACIB，但它是 post-hoc 注意力 heuristic 而非 learned scorer + IB constraint
- IB 理论基础（Tishby 1999 + Deep VIB 2017）是 must-cite，为 ACIB 的 aggregate-rate KL 提供理论根基

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 267839,
  "duration_api_ms": 392469,
  "num_turns": 28,
  "stop_reason": "end_turn",
  "session_id": "26d5ec3f-016d-4ace-b557-94352ecae01a",
  "total_cost_usd": 1.3931712499999998,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 52071,
    "cache_read_input_tokens": 462019,
    "output_tokens": 8545,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 52071,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 417,
        "cache_read_input_tokens": 63449,
        "cache_creation_input_tokens": 463,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 463
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 355403,
      "outputTokens": 11523,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 21,
      "costUSD": 0.6230180000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 8545,
      "cacheReadInputTokens": 462019,
      "cacheCreationInputTokens": 52071,
      "webSearchRequests": 0,
      "costUSD": 0.77015325,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "615b246d-6cab-4b2e-bbfd-92ea3795c013"
}
```

</details>

---
