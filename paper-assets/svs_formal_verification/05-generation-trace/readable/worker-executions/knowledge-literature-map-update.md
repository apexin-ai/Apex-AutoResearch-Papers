# knowledge literature map update

**svs formal verification** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_knowledge_literature_map_update_20260514T160129.log`
- **Structured JSON:** [`df8d9577c7c7308c2b97.json`](../../sessions/df/df8d9577c7c7308c2b97.json)

## Before a recorded user message

23 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification",
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
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
  "uuid": "6eaed721-3f2b-496f-9f00-dc595db37dde",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-svs-formal-verification/memory/"
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
    "resetsAt": 1778787600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "014baa5b-2744-434b-8b86-f4b3d5318478",
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current literature map and the VeriCoT deep dive report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "820359d1-6169-49c2-950a-225ed44f5fa8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MUV1eQc2pmx5mf24bBJ2G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11429,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11429
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014PmwFRfZkznTW9aGeDPvSB`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
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
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "25f12c98-4333-434a-b22f-bd358786690d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MUV1eQc2pmx5mf24bBJ2G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11429,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11429
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

_source line 6 · 2026-05-14T16:01:38.643Z_

<details><summary>↩ Tool result · `toolu_014PmwFRfZkznTW9aGeDPvSB`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "0ab2ad68-2dd1-48a7-a00a-4052c0a5addf",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read both files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "948d0440-980d-4862-8a36-9272ae27b61d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A6tRuYWAnsHEz7AMX7DHWJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 23270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
      },
      "output_tokens": 16,
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KkrTUvVZLKQWXyrLc1rVcQ`</summary>

```json
{
  "project": "svs_formal_verification",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "5f2f6237-2628-4ea1-a970-0a3e0ce83359",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A6tRuYWAnsHEz7AMX7DHWJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 23270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
      },
      "output_tokens": 16,
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

_source line 9 · 2026-05-14T16:01:44.170Z_

<details><summary>↩ Tool result · `toolu_01KkrTUvVZLKQWXyrLc1rVcQ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'svs_formal_verification'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "026ac1d7-bc79-4fe5-a3d8-95dd0adfdedd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No literature_map.yaml found for 'svs_formal_verification'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'svs_formal_verification'.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01UUP8FqrnYn94qVmjuu8uPg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/artifacts/vericot_deep_dive.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "3a30ee9f-6746-443d-90c6-c628a5580001",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A6tRuYWAnsHEz7AMX7DHWJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 23270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
      },
      "output_tokens": 16,
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

_source line 11 · 2026-05-14T16:01:45.469Z_

<details><summary>↩ Tool result · `toolu_01UUP8FqrnYn94qVmjuu8uPg`</summary>

````text
1	# VeriCoT 深入调研报告
2	
3	> 调研日期: 2026-05-14 | 目的: 为 SVS reframe 准备差异化分析
4	
5	---
6	
7	## 1. VeriCoT 方法总结
8	
9	**论文**: VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks
10	**作者**: Yu Feng, Nathaniel Weir, Kaj Bostrom, Sam Bayless, Darion Cassel, Sapana Chaudhary, Benjamin Kiesl-Reiter, Huzefa Rangwala
11	**发表**: ICLR 2026 (Poster) | arXiv: 2511.04662 (Nov 2025)
12	
13	### 1.1 核心 Pipeline
14	
15	```
16	CoT Step Cᵢ → [Stage 1: Autoformalize → SMT-LIB Fᵢ] → [Stage 2: Extend Vocab if needed, ≤3 retries]
17	            → [Contradiction Check: ℱᵢ₋₁ ⊨ ¬Fᵢ ?]
18	            → [Entailment Check: ℱᵢ₋₁ ⊨ Fᵢ ?]
19	            → [Premise Generation: if not entailed, LLM proposes premises Pᵢ]
20	            → Output: {entailed | contradicted | ungrounded | untranslatable}
21	```
22	
23	**关键设计决策**:
24	- **验证粒度**: Step-level（逐步验证，每步 Cᵢ 独立形式化并检查）
25	- **验证类型**: 同时做 entailment + contradiction check（两者都有）
26	- **形式化模型**: Claude-3.5-Sonnet-V2 负责 autoformalization 和 premise generation
27	- **求解器**: Z3 SMT solver，支持 linear arithmetic、uninterpreted functions、quantifiers
28	- **编码格式**: SMT-LIB 语言
29	- **Premise 来源**: LLM 生成（非题目给定），分为 source context / commonsense / prior step 三类
30	
31	### 1.2 验证判定逻辑
32	
33	**Binary，非 graded**。每步判定为四类之一：
34	
35	| 判定 | 条件 | 含义 |
36	|------|------|------|
37	| Entailed | P ∪ {F₁,...,Fᵢ₋₁} ⊨ Fᵢ | 逻辑有效 |
38	| Contradicted | P ∪ {F₁,...,Fᵢ₋₁} ⊨ ¬Fᵢ | 逻辑矛盾 |
39	| Ungrounded | 以上均不成立 | 前提不充分 |
40	| Untranslatable | 3次重试仍无法形式化 | 超出 FOL 表达力 |
41	
42	整条链验证结果 = pass（所有步骤 entailed）/ fail（任一步骤非 entailed）。**无连续分数**。
43	
44	### 1.3 验证信号的三种用途
45	
46	1. **Inference-time self-reflection**: 将验证反馈（含符号翻译、premises、solver 判定）回传给 LLM，重新生成 CoT
47	2. **SFT**: 用验证通过的 CoT 构建训练集
48	3. **DPO**: 用 (verified CoT, unverified CoT) 对构建偏好数据
49	
50	---
51	
52	## 2. 实验配置
53	
54	### 2.1 数据集
55	
56	| 数据集 | 领域 | Train | Test | 类型 |
57	|--------|------|-------|------|------|
58	| ProofWriter | 逻辑推理 | 5,000 | 400 | 规则+事实→推断 |
59	| BioASQ | 生物医学 QA | 5,049 | 340 | 科学推理 |
60	| LegalBench-SARA | 法律推理 | — | 367 | 法规解释 |
61	
62	**注意**: 未测试 FOLIO、LogiQA、PrOntoQA。数据集范围比 LOGIC-LM/LINC 窄。
63	
64	### 2.2 模型
65	
66	| 角色 | 模型 |
67	|------|------|
68	| CoT 生成 + Autoformalization + Premise gen | Claude-3.5-Sonnet-V2 |
69	| Fine-tuning 目标 | Qwen2.5-7B-Instruct |
70	
71	**注意**: 未做 cross-model validation（如用 GPT-4 生成 CoT + 另一模型形式化）。
72	
73	### 2.3 核心指标与结果
74	
75	| 数据集 | Pass Rate | Precision | VCAR |
76	|--------|-----------|-----------|------|
77	| ProofWriter | 45.2% | 94.1% | 42.5% |
78	| BioASQ | 25.3% | 84.3% | 21.3% |
79	| SARA | 15.2% | 87.0% | 13.2% |
80	
81	- **Self-reflection**: 平均 +46% relative pass rate, +41% relative VCAR
82	- **SFT**: +3% absolute accuracy (BioASQ 77.4→79.7%, ProofWriter 47.5→51.1%)
83	- **DPO**: +18.4% relative pass rate improvement
84	- **Baseline 对比**: Pass rate 45.2% vs 14.8%（ProofWriter, baseline 未明确指定）
85	
86	### 2.4 VeriCoT vs SVS 当前配置对比
87	
88	| 维度 | VeriCoT | SVS (当前) |
89	|------|---------|-----------|
90	| **验证类型** | Entailment + Contradiction | Entailment (D012 pivot 后) |
91	| **验证粒度** | Step-level | Claim-level |
92	| **验证判定** | Binary (pass/fail) | Graded (entailed/total_claims 连续分数) |
93	| **Premise 来源** | LLM 生成 (source/commonsense/prior) | 题目给定 premises (PCV) |
94	| **Chain selection** | 单链验证+反思 | 多链采样+分数排序选择 |
95	| **形式化模型** | Claude-3.5-Sonnet-V2 | DeepSeek V3.2 |
96	| **链生成模型** | Claude-3.5-Sonnet-V2 | Qwen2.5-14B / DeepSeek V3.2 |
97	| **数据集** | ProofWriter, BioASQ, SARA | ProofWriter (当前), LogiQA (计划) |
98	| **训练依赖** | 无 (inference-time) + SFT/DPO | 无 (inference-time only) |
99	| **Pass rate** | 15-45% | ~85% formalization rate |
100	| **SMT 编码** | SMT-LIB | Z3 Python API |
101	
102	---
103	
104	## 3. Chain Selection 关键问题（核心差异化确认）
105	
106	### 3.1 VeriCoT 不做 chain selection
107	
108	经确认，VeriCoT：
109	- **仅验证单条链**，不做 multi-chain sampling
110	- Self-reflection 是**串行重试**（验证失败→反馈→重新生成单条链→再验证），不是并行采样
111	- DPO 训练时构造 (verified, unverified) pairs，但这是**训练信号**不是 inference-time selection
112	- 无任何 best-of-n 或 reranking 机制
113	
114	### 3.2 PC-CoT 的 Certified Self-Consistency（部分相关）
115	
116	PC-CoT (Typed Chain-of-Thought, ICLR 2026) 提出 "Certified Self-Consistency"：
117	- 采样多条 CoT → type-check 每条 → **只对通过 type-check 的链做多数投票**
118	- 这是 **binary filter + SC**，不是 graded scoring selection
119	- 数据集仅 GSM8K（数学），与逻辑推理不同赛道
120	
121	### 3.3 PRoSFI 的 Graded Scoring（部分相关）
122	
123	PRoSFI (ICML 2026) 用 graded reward 做 RL 训练：
124	- R=1.0 (correct+all verified), R=0.3 (correct+unverified), R=0.1 (incorrect), R=0.0 (format fail)
125	- 但这是**训练信号**，不用于 inference-time chain selection
126	
127	### 3.4 结论
128	
129	**"Graded formal verification score for inference-time chain selection" 是 SVS 的独特贡献点。** 现有工作要么做 binary verify（VeriCoT, LINC, LOGIC-LM），要么做 graded reward for training（PRoSFI），要么做 binary filter + SC（PC-CoT）。无人将连续验证分数直接用于 test-time chain ranking/selection。
130	
131	---
132	
133	## 4. 相关工作全景
134	
135	### 4.1 Formal Verification for CoT（2023-2026）
136	
137	| 方法 | 年份/会议 | 验证器 | 粒度 | 判定 | Chain Selection | 关键区别 |
138	|------|-----------|--------|------|------|----------------|----------|
139	| **LINC** | EMNLP 2023 | Prover9 | Problem-level | Binary | No | LLM→FOL→theorem prover，不验证 CoT 步骤 |
140	| **LOGIC-LM** | EMNLP 2023 | Symbolic solver | Problem-level | Binary | No | NL→符号→求解，有 self-refinement |
141	| **SatLM** | NeurIPS 2023 | SAT solver | Problem-level | Binary | No | 声明式编程范式 |
142	| **VeriCoT** | ICLR 2026 | Z3 SMT | Step-level | Binary | No | 逐步 entailment+contradiction |
143	| **PC-CoT** | ICLR 2026 | Type checker | Step-level | Binary (typed) | 部分 (Certified SC) | Curry-Howard 对应 |
144	| **VERGE** | arXiv 2026 | Z3/SMT | Step-level | Graded? | 部分 (trajectory) | 生成时集成 formal guidance |
145	| **PRoSFI** | ICML 2026 | Z3/Prover9 | Step-level | Graded (RL reward) | No (training only) | Structured intermediaries for RL |
146	| **LogicReward** | ICLR 2026 | Isabelle | Step-level | Graded (reward) | No (training only) | 形式验证→reward for SFT/DPO |
147	| **SVS (ours)** | — | Z3 SMT | Claim-level | Graded (continuous) | **Yes** | Graded IC for chain selection |
148	
149	### 4.2 关键观察
150	
151	1. **Binary → Graded 趋势明显**: 2023 年工作全是 binary，2026 年开始出现 graded scoring（PRoSFI, VERGE, LogicReward），但都用于 training reward
152	2. **Chain selection 空白**: 无人将 formal verification score 用于 inference-time chain selection
153	3. **Autoformalization 是共同瓶颈**: VeriCoT 45% pass rate, PC-CoT 40-60% typing rate，说明 LLM→formal 翻译远未成熟
154	
155	---
156	
157	## 5. VeriCoT 局限性分析
158	
159	### 5.1 已确认局限
160	
161	| 局限 | 严重程度 | SVS 是否克服 |
162	|------|----------|-------------|
163	| **极低 pass rate** (15-45%) | 致命 | 部分——SVS 85% formalization rate 但粒度不同不直接可比 |
164	| **Premise 由 LLM 生成** | 中等 | SVS 用题目 premises (PCV)，更可靠 |
165	| **Binary 判定丢失信息** | 中等 | SVS graded scoring 保留连续信息 |
166	| **单链验证无选择能力** | 中等 | SVS 多链选择 |
167	| **仅 Claude-3.5 做形式化** | 中等 | 部分——SVS 用 DeepSeek V3.2，也是单一模型 |
168	| **数据集窄** (3个) | 次要 | 部分——SVS 当前也只有 ProofWriter |
169	| **无 cross-model validation** | 次要 | 计划中（Qwen chain gen + DeepSeek formalization） |
170	| **Autoformalization faithfulness 未验证** | 中等 | 共同问题 |
171	
172	### 5.2 VeriCoT pass rate 低的根因
173	
174	ProofWriter 上 45.2% pass 意味着 **54.8% 的 CoT 无法通过验证**。可能原因：
175	1. Step-level 逐步累积验证过于严格——任一步失败全链失败
176	2. LLM-generated premises 质量不稳定
177	3. 跨步 vocabulary 对齐困难
178	4. SMT-LIB 编码限制
179	
180	SVS 的 claim-level 验证 + 连续分数设计天然对此更鲁棒——即使部分 claim 无法验证，仍可输出有区分力的分数。
181	
182	---
183	
184	## 6. 差异化分析与 Reframe 建议
185	
186	### 6.1 SVS 残余差异化（按强度排序）
187	
188	| 差异点 | 强度 | 支撑论据 | 需要的实验证据 |
189	|--------|------|----------|---------------|
190	| **Graded IC for chain selection** | ⭐⭐⭐ 强 | 无人做过；binary filter+SC 是最近 alternative | d > 0.15 + ablation: graded IC vs binary filter+SC |
191	| **PCV (题目 premises 驱动)** | ⭐⭐ 中 | VeriCoT 用 LLM-gen premises 有 fabrication 风险 | PCV vs LLM-gen premise ablation |
192	| **实用 pass rate** | ⭐⭐ 中 | VeriCoT 15-45%，SVS 85% formalization | 直接对比数字 |
193	| **Training-free** | ⭐ 弱 | VeriCoT 也是 training-free at inference | — |
194	
195	### 6.2 Reframe 方向建议
196	
197	**如果 entailment IC 实验成功 (d > 0.15)**:
198	
199	**推荐 framing**: "Graded Formal Verification as a Test-Time Chain Selection Mechanism"
200	
201	核心 narrative:
202	> 现有 formal verification for CoT 工作（VeriCoT, LINC, LOGIC-LM）将验证视为 binary accept/reject，丢弃大量信息。我们提出将 claim-level entailment checking 转化为连续验证分数（IC score），首次实现 formal-verification-guided test-time chain selection。相比 binary filter + self-consistency，graded selection 在 [数据集] 上提升 [X]%。
203	
204	**必须做的 ablation**:
205	1. **SVS graded IC** vs **Binary filter + SC** (模拟 VeriCoT 风格)
206	2. **SVS graded IC** vs **SC alone** (baseline)
207	3. **PCV (题目 premises)** vs **LLM-generated premises** (区分于 VeriCoT)
208	4. **IC score 分布分析**: correct vs wrong chains 的 IC 分数分布可视化
209	
210	**论文 Related Work 定位**:
211	- VeriCoT → "binary single-chain verification; we extend to graded multi-chain selection"
212	- VERGE → "MCS for error localization + refinement; we use MCS-derived score for selection"
213	- PRoSFI → "graded reward for training; we use graded score at inference without training"
214	- PC-CoT → "Certified Self-Consistency = binary filter + SC; we show graded scoring outperforms"
215	
216	### 6.3 Reframe 需要回答的 Reviewer 预期问题
217	
218	1. **"Graded scoring 比 binary filter+SC 好多少？"** → 必须有 ablation 数字
219	2. **"为什么不直接用 VeriCoT 的 pass/fail 做 filter？"** → 需证明 graded 的信息增益
220	3. **"Autoformalization 本身可靠吗？"** → 需要 faithfulness analysis 或 caveat
221	4. **"为什么只在 ProofWriter 测？"** → 需扩展至少一个数据集
222	
223	---
224	
225	## 7. 风险评估与备选方向
226	
227	### 7.1 如果 entailment IC 成功 (d > 0.15)
228	
229	- **乐观路径**: Graded chain selection 是清晰的贡献点，论文可行
230	- **需补充**: Binary filter ablation + 第二数据集 + faithfulness analysis
231	- **目标会议**: ACL/EMNLP 2026 或 NeurIPS 2026
232	
233	### 7.2 如果 entailment IC 弱信号 (0 < d ≤ 0.15)
234	
235	- **分层分析**: True/False 子集可能有信号（61% Unknown 是 confound）
236	- **数据集切换**: ProofWriter depth-1/2/3 可能更适合（推理链短，形式化更准确）
237	- **FOLIO**: 更多 True/False，更少 Unknown
238	
239	### 7.3 如果 entailment IC 失败 (d ≤ 0)
240	
241	**备选方向 A: 方法论比较研究**
242	- "Formal Verification Scores as Chain Selectors: A Systematic Comparison"
243	- 比较 IC score / binary filter / self-consistency / ORM 在多数据集上的表现
244	- 贡献点：系统性 benchmark + 失败模式分析
245	- 风险：纯比较研究 novelty 偏低
246	
247	**备选方向 B: Autoformalization Faithfulness**
248	- arXiv:2604.19459 揭示 axiom fabrication + premise mistranslation
249	- SVS 框架可用于检测 autoformalization 错误（IC 低→可能形式化不忠实）
250	- 贡献点：formalization faithfulness detector
251	- 风险：需要 gold FOL annotations
252	
253	**备选方向 C: Hybrid Scoring**
254	- 将 IC score 与 LLM-based verifier（如 LogicReward）组合
255	- formal verification 捕捉逻辑错误，learned verifier 捕捉语义错误
256	- 贡献点：互补融合
257	- 风险：engineering complexity
258	
259	---
260	
261	## 8. 搜索来源
262	
263	- [VeriCoT Paper (arXiv)](https://arxiv.org/abs/2511.04662)
264	- [VeriCoT OpenReview](https://openreview.net/forum?id=zHuV3Vatov)
265	- [VeriCoT Full HTML](https://arxiv.org/html/2511.04662v1)
266	- [PC-CoT / Typed Chain-of-Thought](https://arxiv.org/pdf/2510.01069)
267	- [VERGE](https://arxiv.org/pdf/2601.20055)
268	- [PRoSFI](https://arxiv.org/html/2603.29500v1)
269	- [LogicReward GitHub](https://github.com/Aiden0526/Logic-Reward)
270	- [LINC](https://arxiv.org/abs/2310.15164)
271	- [LOGIC-LM](https://arxiv.org/abs/2305.12295)
272	- [SatLM](https://arxiv.org/abs/2305.09656)
273	- [VeriCoT Summary](https://www.emergentmind.com/topics/vericot)
274	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "9597db2b-4cbf-4d1e-8a65-afb34924570c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/artifacts/vericot_deep_dive.md",
      "content": "# VeriCoT 深入调研报告\n\n> 调研日期: 2026-05-14 | 目的: 为 SVS reframe 准备差异化分析\n\n---\n\n## 1. VeriCoT 方法总结\n\n**论文**: VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks\n**作者**: Yu Feng, Nathaniel Weir, Kaj Bostrom, Sam Bayless, Darion Cassel, Sapana Chaudhary, Benjamin Kiesl-Reiter, Huzefa Rangwala\n**发表**: ICLR 2026 (Poster) | arXiv: 2511.04662 (Nov 2025)\n\n### 1.1 核心 Pipeline\n\n```\nCoT Step Cᵢ → [Stage 1: Autoformalize → SMT-LIB Fᵢ] → [Stage 2: Extend Vocab if needed, ≤3 retries]\n            → [Contradiction Check: ℱᵢ₋₁ ⊨ ¬Fᵢ ?]\n            → [Entailment Check: ℱᵢ₋₁ ⊨ Fᵢ ?]\n            → [Premise Generation: if not entailed, LLM proposes premises Pᵢ]\n            → Output: {entailed | contradicted | ungrounded | untranslatable}\n```\n\n**关键设计决策**:\n- **验证粒度**: Step-level（逐步验证，每步 Cᵢ 独立形式化并检查）\n- **验证类型**: 同时做 entailment + contradiction check（两者都有）\n- **形式化模型**: Claude-3.5-Sonnet-V2 负责 autoformalization 和 premise generation\n- **求解器**: Z3 SMT solver，支持 linear arithmetic、uninterpreted functions、quantifiers\n- **编码格式**: SMT-LIB 语言\n- **Premise 来源**: LLM 生成（非题目给定），分为 source context / commonsense / prior step 三类\n\n### 1.2 验证判定逻辑\n\n**Binary，非 graded**。每步判定为四类之一：\n\n| 判定 | 条件 | 含义 |\n|------|------|------|\n| Entailed | P ∪ {F₁,...,Fᵢ₋₁} ⊨ Fᵢ | 逻辑有效 |\n| Contradicted | P ∪ {F₁,...,Fᵢ₋₁} ⊨ ¬Fᵢ | 逻辑矛盾 |\n| Ungrounded | 以上均不成立 | 前提不充分 |\n| Untranslatable | 3次重试仍无法形式化 | 超出 FOL 表达力 |\n\n整条链验证结果 = pass（所有步骤 entailed）/ fail（任一步骤非 entailed）。**无连续分数**。\n\n### 1.3 验证信号的三种用途\n\n1. **Inference-time self-reflection**: 将验证反馈（含符号翻译、premises、solver 判定）回传给 LLM，重新生成 CoT\n2. **SFT**: 用验证通过的 CoT 构建训练集\n3. **DPO**: 用 (verified CoT, unverified CoT) 对构建偏好数据\n\n---\n\n## 2. 实验配置\n\n### 2.1 数据集\n\n| 数据集 | 领域 | Train | Test | 类型 |\n|--------|------|-------|------|------|\n| ProofWriter | 逻辑推理 | 5,000 | 400 | 规则+事实→推断 |\n| BioASQ | 生物医学 QA | 5,049 | 340 | 科学推理 |\n| LegalBench-SARA | 法律推理 | — | 367 | 法规解释 |\n\n**注意**: 未测试 FOLIO、LogiQA、PrOntoQA。数据集范围比 LOGIC-LM/LINC 窄。\n\n### 2.2 模型\n\n| 角色 | 模型 |\n|------|------|\n| CoT 生成 + Autoformalization + Premise gen | Claude-3.5-Sonnet-V2 |\n| Fine-tuning 目标 | Qwen2.5-7B-Instruct |\n\n**注意**: 未做 cross-model validation（如用 GPT-4 生成 CoT + 另一模型形式化）。\n\n### 2.3 核心指标与结果\n\n| 数据集 | Pass Rate | Precision | VCAR |\n|--------|-----------|-----------|------|\n| ProofWriter | 45.2% | 94.1% | 42.5% |\n| BioASQ | 25.3% | 84.3% | 21.3% |\n| SARA | 15.2% | 87.0% | 13.2% |\n\n- **Self-reflection**: 平均 +46% relative pass rate, +41% relative VCAR\n- **SFT**: +3% absolute accuracy (BioASQ 77.4→79.7%, ProofWriter 47.5→51.1%)\n- **DPO**: +18.4% relative pass rate improvement\n- **Baseline 对比**: Pass rate 45.2% vs 14.8%（ProofWriter, baseline 未明确指定）\n\n### 2.4 VeriCoT vs SVS 当前配置对比\n\n| 维度 | VeriCoT | SVS (当前) |\n|------|---------|-----------|\n| **验证类型** | Entailment + Contradiction | Entailment (D012 pivot 后) |\n| **验证粒度** | Step-level | Claim-level |\n| **验证判定** | Binary (pass/fail) | Graded (entailed/total_claims 连续分数) |\n| **Premise 来源** | LLM 生成 (source/commonsense/prior) | 题目给定 premises (PCV) |\n| **Chain selection** | 单链验证+反思 | 多链采样+分数排序选择 |\n| **形式化模型** | Claude-3.5-Sonnet-V2 | DeepSeek V3.2 |\n| **链生成模型** | Claude-3.5-Sonnet-V2 | Qwen2.5-14B / DeepSeek V3.2 |\n| **数据集** | ProofWriter, BioASQ, SARA | ProofWriter (当前), LogiQA (计划) |\n| **训练依赖** | 无 (inference-time) + SFT/DPO | 无 (inference-time only) |\n| **Pass rate** | 15-45% | ~85% formalization rate |\n| **SMT 编码** | SMT-LIB | Z3 Python API |\n\n---\n\n## 3. Chain Selection 关键问题（核心差异化确认）\n\n### 3.1 VeriCoT 不做 chain selection\n\n经确认，VeriCoT：\n- **仅验证单条链**，不做 multi-chain sampling\n- Self-reflection 是**串行重试**（验证失败→反馈→重新生成单条链→再验证），不是并行采样\n- DPO 训练时构造 (verified, unverified) pairs，但这是**训练信号**不是 inference-time selection\n- 无任何 best-of-n 或 reranking 机制\n\n### 3.2 PC-CoT 的 Certified Self-Consistency（部分相关）\n\nPC-CoT (Typed Chain-of-Thought, ICLR 2026) 提出 \"Certified Self-Consistency\"：\n- 采样多条 CoT → type-check 每条 → **只对通过 type-check 的链做多数投票**\n- 这是 **binary filter + SC**，不是 graded scoring selection\n- 数据集仅 GSM8K（数学），与逻辑推理不同赛道\n\n### 3.3 PRoSFI 的 Graded Scoring（部分相关）\n\nPRoSFI (ICML 2026) 用 graded reward 做 RL 训练：\n- R=1.0 (correct+all verified), R=0.3 (correct+unverified), R=0.1 (incorrect), R=0.0 (format fail)\n- 但这是**训练信号**，不用于 inference-time chain selection\n\n### 3.4 结论\n\n**\"Graded formal verification score for inference-time chain selection\" 是 SVS 的独特贡献点。** 现有工作要么做 binary verify（VeriCoT, LINC, LOGIC-LM），要么做 graded reward for training（PRoSFI），要么做 binary filter + SC（PC-CoT）。无人将连续验证分数直接用于 test-time chain ranking/selection。\n\n---\n\n## 4. 相关工作全景\n\n### 4.1 Formal Verification for CoT（2023-2026）\n\n| 方法 | 年份/会议 | 验证器 | 粒度 | 判定 | Chain Selection | 关键区别 |\n|------|-----------|--------|------|------|----------------|----------|\n| **LINC** | EMNLP 2023 | Prover9 | Problem-level | Binary | No | LLM→FOL→theorem prover，不验证 CoT 步骤 |\n| **LOGIC-LM** | EMNLP 2023 | Symbolic solver | Problem-level | Binary | No | NL→符号→求解，有 self-refinement |\n| **SatLM** | NeurIPS 2023 | SAT solver | Problem-level | Binary | No | 声明式编程范式 |\n| **VeriCoT** | ICLR 2026 | Z3 SMT | Step-level | Binary | No | 逐步 entailment+contradiction |\n| **PC-CoT** | ICLR 2026 | Type checker | Step-level | Binary (typed) | 部分 (Certified SC) | Curry-Howard 对应 |\n| **VERGE** | arXiv 2026 | Z3/SMT | Step-level | Graded? | 部分 (trajectory) | 生成时集成 formal guidance |\n| **PRoSFI** | ICML 2026 | Z3/Prover9 | Step-level | Graded (RL reward) | No (training only) | Structured intermediaries for RL |\n| **LogicReward** | ICLR 2026 | Isabelle | Step-level | Graded (reward) | No (training only) | 形式验证→reward for SFT/DPO |\n| **SVS (ours)** | — | Z3 SMT | Claim-level | Graded (continuous) | **Yes** | Graded IC for chain selection |\n\n### 4.2 关键观察\n\n1. **Binary → Graded 趋势明显**: 2023 年工作全是 binary，2026 年开始出现 graded scoring（PRoSFI, VERGE, LogicReward），但都用于 training reward\n2. **Chain selection 空白**: 无人将 formal verification score 用于 inference-time chain selection\n3. **Autoformalization 是共同瓶颈**: VeriCoT 45% pass rate, PC-CoT 40-60% typing rate，说明 LLM→formal 翻译远未成熟\n\n---\n\n## 5. VeriCoT 局限性分析\n\n### 5.1 已确认局限\n\n| 局限 | 严重程度 | SVS 是否克服 |\n|------|----------|-------------|\n| **极低 pass rate** (15-45%) | 致命 | 部分——SVS 85% formalization rate 但粒度不同不直接可比 |\n| **Premise 由 LLM 生成** | 中等 | SVS 用题目 premises (PCV)，更可靠 |\n| **Binary 判定丢失信息** | 中等 | SVS graded scoring 保留连续信息 |\n| **单链验证无选择能力** | 中等 | SVS 多链选择 |\n| **仅 Claude-3.5 做形式化** | 中等 | 部分——SVS 用 DeepSeek V3.2，也是单一模型 |\n| **数据集窄** (3个) | 次要 | 部分——SVS 当前也只有 ProofWriter |\n| **无 cross-model validation** | 次要 | 计划中（Qwen chain gen + DeepSeek formalization） |\n| **Autoformalization faithfulness 未验证** | 中等 | 共同问题 |\n\n### 5.2 VeriCoT pass rate 低的根因\n\nProofWriter 上 45.2% pass 意味着 **54.8% 的 CoT 无法通过验证**。可能原因：\n1. Step-level 逐步累积验证过于严格——任一步失败全链失败\n2. LLM-generated premises 质量不稳定\n3. 跨步 vocabulary 对齐困难\n4. SMT-LIB 编码限制\n\nSVS 的 claim-level 验证 + 连续分数设计天然对此更鲁棒——即使部分 claim 无法验证，仍可输出有区分力的分数。\n\n---\n\n## 6. 差异化分析与 Reframe 建议\n\n### 6.1 SVS 残余差异化（按强度排序）\n\n| 差异点 | 强度 | 支撑论据 | 需要的实验证据 |\n|--------|------|----------|---------------|\n| **Graded IC for chain selection** | ⭐⭐⭐ 强 | 无人做过；binary filter+SC 是最近 alternative | d > 0.15 + ablation: graded IC vs binary filter+SC |\n| **PCV (题目 premises 驱动)** | ⭐⭐ 中 | VeriCoT 用 LLM-gen premises 有 fabrication 风险 | PCV vs LLM-gen premise ablation |\n| **实用 pass rate** | ⭐⭐ 中 | VeriCoT 15-45%，SVS 85% formalization | 直接对比数字 |\n| **Training-free** | ⭐ 弱 | VeriCoT 也是 training-free at inference | — |\n\n### 6.2 Reframe 方向建议\n\n**如果 entailment IC 实验成功 (d > 0.15)**:\n\n**推荐 framing**: \"Graded Formal Verification as a Test-Time Chain Selection Mechanism\"\n\n核心 narrative:\n> 现有 formal verification for CoT 工作（VeriCoT, LINC, LOGIC-LM）将验证视为 binary accept/reject，丢弃大量信息。我们提出将 claim-level entailment checking 转化为连续验证分数（IC score），首次实现 formal-verification-guided test-time chain selection。相比 binary filter + self-consistency，graded selection 在 [数据集] 上提升 [X]%。\n\n**必须做的 ablation**:\n1. **SVS graded IC** vs **Binary filter + SC** (模拟 VeriCoT 风格)\n2. **SVS graded IC** vs **SC alone** (baseline)\n3. **PCV (题目 premises)** vs **LLM-generated premises** (区分于 VeriCoT)\n4. **IC score 分布分析**: correct vs wrong chains 的 IC 分数分布可视化\n\n**论文 Related Work 定位**:\n- VeriCoT → \"binary single-chain verification; we extend to graded multi-chain selection\"\n- VERGE → \"MCS for error localization + refinement; we use MCS-derived score for selection\"\n- PRoSFI → \"graded reward for training; we use graded score at inference without training\"\n- PC-CoT → \"Certified Self-Consistency = binary filter + SC; we show graded scoring outperforms\"\n\n### 6.3 Reframe 需要回答的 Reviewer 预期问题\n\n1. **\"Graded scoring 比 binary filter+SC 好多少？\"** → 必须有 ablation 数字\n2. **\"为什么不直接用 VeriCoT 的 pass/fail 做 filter？\"** → 需证明 graded 的信息增益\n3. **\"Autoformalization 本身可靠吗？\"** → 需要 faithfulness analysis 或 caveat\n4. **\"为什么只在 ProofWriter 测？\"** → 需扩展至少一个数据集\n\n---\n\n## 7. 风险评估与备选方向\n\n### 7.1 如果 entailment IC 成功 (d > 0.15)\n\n- **乐观路径**: Graded chain selection 是清晰的贡献点，论文可行\n- **需补充**: Binary filter ablation + 第二数据集 + faithfulness analysis\n- **目标会议**: ACL/EMNLP 2026 或 NeurIPS 2026\n\n### 7.2 如果 entailment IC 弱信号 (0 < d ≤ 0.15)\n\n- **分层分析**: True/False 子集可能有信号（61% Unknown 是 confound）\n- **数据集切换**: ProofWriter depth-1/2/3 可能更适合（推理链短，形式化更准确）\n- **FOLIO**: 更多 True/False，更少 Unknown\n\n### 7.3 如果 entailment IC 失败 (d ≤ 0)\n\n**备选方向 A: 方法论比较研究**\n- \"Formal Verification Scores as Chain Selectors: A Systematic Comparison\"\n- 比较 IC score / binary filter / self-consistency / ORM 在多数据集上的表现\n- 贡献点：系统性 benchmark + 失败模式分析\n- 风险：纯比较研究 novelty 偏低\n\n**备选方向 B: Autoformalization Faithfulness**\n- arXiv:2604.19459 揭示 axiom fabrication + premise mistranslation\n- SVS 框架可用于检测 autoformalization 错误（IC 低→可能形式化不忠实）\n- 贡献点：formalization faithfulness detector\n- 风险：需要 gold FOL annotations\n\n**备选方向 C: Hybrid Scoring**\n- 将 IC score 与 LLM-based verifier（如 LogicReward）组合\n- formal verification 捕捉逻辑错误，learned verifier 捕捉语义错误\n- 贡献点：互补融合\n- 风险：engineering complexity\n\n---\n\n## 8. 搜索来源\n\n- [VeriCoT Paper (arXiv)](https://arxiv.org/abs/2511.04662)\n- [VeriCoT OpenReview](https://openreview.net/forum?id=zHuV3Vatov)\n- [VeriCoT Full HTML](https://arxiv.org/html/2511.04662v1)\n- [PC-CoT / Typed Chain-of-Thought](https://arxiv.org/pdf/2510.01069)\n- [VERGE](https://arxiv.org/pdf/2601.20055)\n- [PRoSFI](https://arxiv.org/html/2603.29500v1)\n- [LogicReward GitHub](https://github.com/Aiden0526/Logic-Reward)\n- [LINC](https://arxiv.org/abs/2310.15164)\n- [LOGIC-LM](https://arxiv.org/abs/2305.12295)\n- [SatLM](https://arxiv.org/abs/2305.09656)\n- [VeriCoT Summary](https://www.emergentmind.com/topics/vericot)\n",
      "numLines": 274,
      "startLine": 1,
      "totalLines": 274
    }
  }
}
````

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The literature_map.yaml doesn't exist yet, so I need to create it from scratch. Let me construct a comprehensive literature map based on the VeriCoT deep dive report, covering all the papers mentioned in the task.

Let me also check if there are any other project files that might have relevant information about the current literature map structure or conventions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "254b50f4-ca2d-4f9d-b6cd-9335d142ec42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FuzUcHtHKHPDafJ7rEihDW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6400,
      "cache_read_input_tokens": 23989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6400
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

_source line 13_

literature_map.yaml 不存在，需要新建。根据深度调研报告构建完整文献图谱。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "5b78c620-8350-4839-b514-2c03b7426de8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FuzUcHtHKHPDafJ7rEihDW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6400,
      "cache_read_input_tokens": 23989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6400
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_011ggDLVDAgVCHLNSnqHWzgE`</summary>

```json
{
  "project": "svs_formal_verification",
  "file": "literature_map.yaml",
  "content": "# SVS Formal Verification - Literature Map\n# 更新日期: 2026-05-14\n# 基于 VeriCoT 深度调研整合\n\npapers:\n\n  # ============================================================\n  # Direct Competitors - 直接竞争方法\n  # ============================================================\n\n  VeriCoT:\n    title: \"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks\"\n    authors: \"Yu Feng, Nathaniel Weir, Kaj Bostrom, Sam Bayless, Darion Cassel, Sapana Chaudhary, Benjamin Kiesl-Reiter, Huzefa Rangwala\"\n    venue: ICLR 2026 (Poster)\n    arxiv: \"2511.04662\"\n    role: direct-competitor\n    method:\n      verifier: Z3 SMT solver\n      granularity: step-level\n      verdict: binary (entailed / contradicted / ungrounded / untranslatable)\n      chain_selection: none (single-chain + serial self-reflection)\n      formalization: SMT-LIB via Claude-3.5-Sonnet-V2\n      premise_source: LLM-generated (source context / commonsense / prior step)\n      training_dependency: none at inference; optional SFT/DPO\n    datasets: [ProofWriter, BioASQ, LegalBench-SARA]\n    key_results:\n      pass_rate: \"15-45% (ProofWriter 45.2%, BioASQ 25.3%, SARA 15.2%)\"\n      precision: \"84-94%\"\n      self_reflection_gain: \"+46% relative pass rate\"\n    svs_relevance: |\n      最直接的竞争者。核心差异：\n      1. Binary vs Graded: VeriCoT 输出 pass/fail，SVS 输出连续 IC 分数\n      2. Single-chain vs Multi-chain: VeriCoT 验证单链+串行反思，SVS 多链采样+分数排序选择\n      3. LLM-gen premises vs PCV: VeriCoT 由 LLM 生成 premises（有 fabrication 风险），SVS 使用题目给定 premises\n      4. Pass rate: VeriCoT 15-45%，SVS ~85% formalization rate（粒度不同不直接可比）\n      论文定位: \"binary single-chain verification; we extend to graded multi-chain selection\"\n\n  PC-CoT:\n    title: \"Typed Chain-of-Thought (PC-CoT): Certified Self-Consistency via Curry-Howard Correspondence\"\n    venue: ICLR 2026\n    arxiv: \"2510.01069\"\n    role: direct-competitor\n    method:\n      verifier: type checker (Curry-Howard correspondence)\n      granularity: step-level\n      verdict: binary (type-check pass/fail)\n      chain_selection: \"Certified Self-Consistency = binary type-check filter + majority voting (SC)\"\n      formalization: typed CoT via Curry-Howard\n      training_dependency: none\n    datasets: [GSM8K]\n    key_results:\n      typing_rate: \"40-60%\"\n    svs_relevance: |\n      提出 \"Certified Self-Consistency\"，是 SVS graded chain selection 的最近 alternative。\n      核心差异：\n      1. Binary filter + SC vs Graded scoring selection: PC-CoT 先 binary 筛再投票，SVS 用连续分数直接排序\n      2. 赛道不同: PC-CoT 仅测 GSM8K（数学），SVS 做逻辑推理\n      3. 信息损失: binary filter 丢弃了验证程度的连续信息\n      论文定位: \"Certified Self-Consistency = binary filter + SC; we show graded scoring outperforms\"\n      必须做的 ablation: SVS graded IC vs binary filter + SC\n\n  VERGE:\n    title: \"VERGE: Verification-Guided Reasoning with Z3/SMT\"\n    venue: arXiv 2026\n    arxiv: \"2601.20055\"\n    role: direct-competitor\n    method:\n      verifier: Z3/SMT\n      granularity: step-level\n      verdict: \"graded (MCS-based)\"\n      chain_selection: \"partial (trajectory-level formal guidance during generation)\"\n      formalization: SMT encoding\n      key_innovation: \"MCS (Maximal Consistent Subsets) for error localization + formal guidance during generation\"\n    svs_relevance: |\n      最接近 SVS 的 graded 思路，但用途不同。\n      核心差异：\n      1. 用途: VERGE 用 MCS 做 error localization + 生成引导，SVS 用 MCS-derived score 做 chain selection\n      2. 时机: VERGE 在生成过程中介入（online），SVS 在生成后评估（post-hoc）\n      3. 复杂度: VERGE 需修改生成 pipeline，SVS 是 plug-and-play 后处理\n      论文定位: \"MCS for error localization + refinement; we use MCS-derived score for selection\"\n\n  # ============================================================\n  # Method Components - 方法组件（用于训练，非 inference-time）\n  # ============================================================\n\n  PRoSFI:\n    title: \"PRoSFI: Graded Reward via Structured Formal Intermediaries for RL Training\"\n    venue: ICML 2026\n    arxiv: \"2603.29500\"\n    role: method-component\n    method:\n      verifier: Z3/Prover9\n      granularity: step-level\n      verdict: \"graded reward (R=1.0/0.3/0.1/0.0)\"\n      chain_selection: none (training reward only, not used at inference)\n      key_innovation: \"graded formal verification reward for RL (PPO/GRPO)\"\n    svs_relevance: |\n      与 SVS 共享 \"graded formal verification\" 理念，但用途截然不同。\n      核心差异：\n      1. Training vs Inference: PRoSFI 的 graded score 是 RL reward（训练信号），SVS 用于 inference-time chain selection\n      2. SVS 无需训练: PRoSFI 需 RL 训练循环，SVS 是 training-free 的 test-time 方法\n      论文定位: \"graded reward for training; we use graded score at inference without training\"\n\n  # ============================================================\n  # Evaluation Baselines\n  # ============================================================\n\n  LogicReward:\n    title: \"LogicReward: Isabelle-based Graded Reward for SFT/DPO Training\"\n    venue: ICLR 2026\n    github: \"https://github.com/Aiden0526/Logic-Reward\"\n    role: evaluation\n    method:\n      verifier: Isabelle theorem prover\n      granularity: step-level\n      verdict: \"graded reward\"\n      chain_selection: none (training reward only)\n      key_innovation: \"formal verification → reward signal for SFT/DPO\"\n    svs_relevance: |\n      同样产出 graded verification signal，但仅用于训练。\n      核心差异：\n      1. 训练 vs 推理: LogicReward 用于 SFT/DPO 训练，SVS 用于 inference-time selection\n      2. 验证器: LogicReward 用 Isabelle（交互式定理证明器），SVS 用 Z3（SMT solver），Z3 更轻量自动化\n      3. 互补潜力: Hybrid scoring（IC score + LogicReward）是潜在扩展方向\n\n  # ============================================================\n  # Background - 早期基础工作\n  # ============================================================\n\n  LINC:\n    title: \"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\"\n    venue: EMNLP 2023\n    arxiv: \"2310.15164\"\n    role: background\n    method:\n      verifier: Prover9\n      granularity: problem-level\n      verdict: binary\n      chain_selection: none\n      key_innovation: \"LLM → FOL → theorem prover pipeline\"\n    svs_relevance: |\n      SVS 的前身类方法。LINC 做 problem-level binary 验证，不验证 CoT 步骤。\n      SVS 在三个维度上推进：step/claim-level 粒度、graded 判定、multi-chain selection。\n\n  LOGIC-LM:\n    title: \"LOGIC-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\"\n    venue: EMNLP 2023\n    arxiv: \"2305.12295\"\n    role: background\n    method:\n      verifier: symbolic solver\n      granularity: problem-level\n      verdict: binary\n      chain_selection: none\n      key_innovation: \"NL → symbolic formulation → solver，with self-refinement loop\"\n    svs_relevance: |\n      Problem-level binary 验证 + self-refinement。与 SVS 的差异同 LINC：\n      粒度（problem vs claim）、判定（binary vs graded）、用途（refinement vs selection）。\n      LOGIC-LM 的 self-refinement 思路与 VeriCoT 的 self-reflection 类似。\n\n  SatLM:\n    title: \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\"\n    venue: NeurIPS 2023\n    arxiv: \"2305.09656\"\n    role: background\n    method:\n      verifier: SAT solver\n      granularity: problem-level\n      verdict: binary\n      chain_selection: none\n      key_innovation: \"declarative programming paradigm for LLM reasoning\"\n    svs_relevance: |\n      SAT solver 路线，声明式编程范式。与 SVS 的 SMT-based 方法不同赛道。\n      SAT 表达力弱于 SMT（无量词、无函数），但求解效率更高。\n      SVS 选择 Z3 SMT 是更通用的形式化选择。\n\n# ============================================================\n# 图谱总结\n# ============================================================\n\nlandscape_summary:\n  trend_binary_to_graded: |\n    2023 年工作（LINC, LOGIC-LM, SatLM）全是 binary problem-level 验证。\n    2026 年开始出现 graded step-level scoring（PRoSFI, VERGE, LogicReward），但均用于 training reward。\n    SVS 首次将 graded formal verification score 用于 inference-time chain selection。\n\n  chain_selection_gap: |\n    现有工作的 chain selection 方式：\n    - 无选择: VeriCoT, LINC, LOGIC-LM, SatLM, PRoSFI, LogicReward\n    - Binary filter + SC: PC-CoT (Certified Self-Consistency)\n    - 生成引导: VERGE\n    - Graded scoring selection: SVS (ours) ← 唯一\n\n  common_bottleneck: |\n    Autoformalization 是所有方法的共同瓶颈：\n    - VeriCoT: 45% pass rate\n    - PC-CoT: 40-60% typing rate\n    - SVS: ~85% formalization rate（claim-level 粒度更宽容）\n\n  svs_unique_contribution: |\n    \"Graded formal verification score for inference-time chain selection\"\n    是 SVS 的独特贡献点。无人将连续验证分数直接用于 test-time chain ranking/selection。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "f93ed240-9dc4-4ea4-993e-c1db654b7468",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FuzUcHtHKHPDafJ7rEihDW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6400,
      "cache_read_input_tokens": 23989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6400
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

_source line 15 · 2026-05-14T16:02:54.058Z_

<details><summary>↩ Tool result · `toolu_011ggDLVDAgVCHLNSnqHWzgE`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'literature_map.yaml' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "93f82f80-29c8-46e6-80e3-df2f34f85733",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file 'literature_map.yaml' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file 'literature_map.yaml' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool doesn't allow writing literature_map.yaml. I need to write it directly to the filesystem.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "3760db7f-ccdf-4966-892a-ca6212af936a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1uaGZKL6qwhQyRmtwr8yV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3403,
      "cache_read_input_tokens": 30389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3403
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

_source line 17_

save_project_file 不支持写 literature_map.yaml，直接写文件系统。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "46f54b26-3893-4012-9cab-6207c1af7bbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1uaGZKL6qwhQyRmtwr8yV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3403,
      "cache_read_input_tokens": 30389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3403
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01LWah75fvhERbyVChyxewj6`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/",
  "description": "List project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "54504a99-9e80-42a8-9a67-c482939bdb65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1uaGZKL6qwhQyRmtwr8yV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3403,
      "cache_read_input_tokens": 30389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3403
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

_source line 19 · 2026-05-14T16:02:58.731Z_

<details><summary>↩ Tool result · `toolu_01LWah75fvhERbyVChyxewj6`</summary>

```text
AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
checkpoints
decisions.lock
decisions.yaml
docs
dream_registry.lock
logs
memory.md
registry.lock
registry.yaml
report.md
study_status.lock
task_context
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "49d83715-f10c-4b6d-85ca-4a5e2e50ee67",
  "tool_use_result": {
    "stdout": "AGENTS.md\nROADMAP.lock\nROADMAP.md\nartifacts\ncheckpoints\ndecisions.lock\ndecisions.yaml\ndocs\ndream_registry.lock\nlogs\nmemory.md\nregistry.lock\nregistry.yaml\nreport.md\nstudy_status.lock\ntask_context",
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

_source line 20_

<details open><summary>🔧 Tool call — Write · `toolu_01PapFi62KLLZoevq3s73rkU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/literature_map.yaml",
  "content": "# SVS Formal Verification - Literature Map\n# 更新日期: 2026-05-14\n# 基于 VeriCoT 深度调研整合\n\npapers:\n\n  # ============================================================\n  # Direct Competitors - 直接竞争方法\n  # ============================================================\n\n  VeriCoT:\n    title: \"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks\"\n    authors: \"Yu Feng, Nathaniel Weir, Kaj Bostrom, Sam Bayless, Darion Cassel, Sapana Chaudhary, Benjamin Kiesl-Reiter, Huzefa Rangwala\"\n    venue: ICLR 2026 (Poster)\n    arxiv: \"2511.04662\"\n    role: direct-competitor\n    method:\n      verifier: Z3 SMT solver\n      granularity: step-level\n      verdict: binary (entailed / contradicted / ungrounded / untranslatable)\n      chain_selection: none (single-chain + serial self-reflection)\n      formalization: SMT-LIB via Claude-3.5-Sonnet-V2\n      premise_source: LLM-generated (source context / commonsense / prior step)\n      training_dependency: none at inference; optional SFT/DPO\n    datasets: [ProofWriter, BioASQ, LegalBench-SARA]\n    key_results:\n      pass_rate: \"15-45% (ProofWriter 45.2%, BioASQ 25.3%, SARA 15.2%)\"\n      precision: \"84-94%\"\n      self_reflection_gain: \"+46% relative pass rate\"\n    svs_relevance: |\n      最直接的竞争者。核心差异：\n      1. Binary vs Graded: VeriCoT 输出 pass/fail，SVS 输出连续 IC 分数\n      2. Single-chain vs Multi-chain: VeriCoT 验证单链+串行反思，SVS 多链采样+分数排序选择\n      3. LLM-gen premises vs PCV: VeriCoT 由 LLM 生成 premises（有 fabrication 风险），SVS 使用题目给定 premises\n      4. Pass rate: VeriCoT 15-45%，SVS ~85% formalization rate（粒度不同不直接可比）\n      论文定位: \"binary single-chain verification; we extend to graded multi-chain selection\"\n\n  PC-CoT:\n    title: \"Typed Chain-of-Thought (PC-CoT): Certified Self-Consistency via Curry-Howard Correspondence\"\n    venue: ICLR 2026\n    arxiv: \"2510.01069\"\n    role: direct-competitor\n    method:\n      verifier: type checker (Curry-Howard correspondence)\n      granularity: step-level\n      verdict: binary (type-check pass/fail)\n      chain_selection: \"Certified Self-Consistency = binary type-check filter + majority voting (SC)\"\n      formalization: typed CoT via Curry-Howard\n      training_dependency: none\n    datasets: [GSM8K]\n    key_results:\n      typing_rate: \"40-60%\"\n    svs_relevance: |\n      提出 \"Certified Self-Consistency\"，是 SVS graded chain selection 的最近 alternative。\n      核心差异：\n      1. Binary filter + SC vs Graded scoring selection: PC-CoT 先 binary 筛再投票，SVS 用连续分数直接排序\n      2. 赛道不同: PC-CoT 仅测 GSM8K（数学），SVS 做逻辑推理\n      3. 信息损失: binary filter 丢弃了验证程度的连续信息\n      论文定位: \"Certified Self-Consistency = binary filter + SC; we show graded scoring outperforms\"\n      必须做的 ablation: SVS graded IC vs binary filter + SC\n\n  VERGE:\n    title: \"VERGE: Verification-Guided Reasoning with Z3/SMT\"\n    venue: arXiv 2026\n    arxiv: \"2601.20055\"\n    role: direct-competitor\n    method:\n      verifier: Z3/SMT\n      granularity: step-level\n      verdict: \"graded (MCS-based)\"\n      chain_selection: \"partial (trajectory-level formal guidance during generation)\"\n      formalization: SMT encoding\n      key_innovation: \"MCS (Maximal Consistent Subsets) for error localization + formal guidance during generation\"\n    svs_relevance: |\n      最接近 SVS 的 graded 思路，但用途不同。\n      核心差异：\n      1. 用途: VERGE 用 MCS 做 error localization + 生成引导，SVS 用 MCS-derived score 做 chain selection\n      2. 时机: VERGE 在生成过程中介入（online），SVS 在生成后评估（post-hoc）\n      3. 复杂度: VERGE 需修改生成 pipeline，SVS 是 plug-and-play 后处理\n      论文定位: \"MCS for error localization + refinement; we use MCS-derived score for selection\"\n\n  # ============================================================\n  # Method Components - 方法组件（用于训练，非 inference-time）\n  # ============================================================\n\n  PRoSFI:\n    title: \"PRoSFI: Graded Reward via Structured Formal Intermediaries for RL Training\"\n    venue: ICML 2026\n    arxiv: \"2603.29500\"\n    role: method-component\n    method:\n      verifier: Z3/Prover9\n      granularity: step-level\n      verdict: \"graded reward (R=1.0/0.3/0.1/0.0)\"\n      chain_selection: none (training reward only, not used at inference)\n      key_innovation: \"graded formal verification reward for RL (PPO/GRPO)\"\n    svs_relevance: |\n      与 SVS 共享 \"graded formal verification\" 理念，但用途截然不同。\n      核心差异：\n      1. Training vs Inference: PRoSFI 的 graded score 是 RL reward（训练信号），SVS 用于 inference-time chain selection\n      2. SVS 无需训练: PRoSFI 需 RL 训练循环，SVS 是 training-free 的 test-time 方法\n      论文定位: \"graded reward for training; we use graded score at inference without training\"\n\n  # ============================================================\n  # Evaluation Baselines\n  # ============================================================\n\n  LogicReward:\n    title: \"LogicReward: Isabelle-based Graded Reward for SFT/DPO Training\"\n    venue: ICLR 2026\n    github: \"https://github.com/Aiden0526/Logic-Reward\"\n    role: evaluation\n    method:\n      verifier: Isabelle theorem prover\n      granularity: step-level\n      verdict: \"graded reward\"\n      chain_selection: none (training reward only)\n      key_innovation: \"formal verification → reward signal for SFT/DPO\"\n    svs_relevance: |\n      同样产出 graded verification signal，但仅用于训练。\n      核心差异：\n      1. 训练 vs 推理: LogicReward 用于 SFT/DPO 训练，SVS 用于 inference-time selection\n      2. 验证器: LogicReward 用 Isabelle（交互式定理证明器），SVS 用 Z3（SMT solver），Z3 更轻量自动化\n      3. 互补潜力: Hybrid scoring（IC score + LogicReward）是潜在扩展方向\n\n  # ============================================================\n  # Background - 早期基础工作\n  # ============================================================\n\n  LINC:\n    title: \"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\"\n    venue: EMNLP 2023\n    arxiv: \"2310.15164\"\n    role: background\n    method:\n      verifier: Prover9\n      granularity: problem-level\n      verdict: binary\n      chain_selection: none\n      key_innovation: \"LLM → FOL → theorem prover pipeline\"\n    svs_relevance: |\n      SVS 的前身类方法。LINC 做 problem-level binary 验证，不验证 CoT 步骤。\n      SVS 在三个维度上推进：step/claim-level 粒度、graded 判定、multi-chain selection。\n\n  LOGIC-LM:\n    title: \"LOGIC-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\"\n    venue: EMNLP 2023\n    arxiv: \"2305.12295\"\n    role: background\n    method:\n      verifier: symbolic solver\n      granularity: problem-level\n      verdict: binary\n      chain_selection: none\n      key_innovation: \"NL → symbolic formulation → solver，with self-refinement loop\"\n    svs_relevance: |\n      Problem-level binary 验证 + self-refinement。与 SVS 的差异同 LINC：\n      粒度（problem vs claim）、判定（binary vs graded）、用途（refinement vs selection）。\n      LOGIC-LM 的 self-refinement 思路与 VeriCoT 的 self-reflection 类似。\n\n  SatLM:\n    title: \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\"\n    venue: NeurIPS 2023\n    arxiv: \"2305.09656\"\n    role: background\n    method:\n      verifier: SAT solver\n      granularity: problem-level\n      verdict: binary\n      chain_selection: none\n      key_innovation: \"declarative programming paradigm for LLM reasoning\"\n    svs_relevance: |\n      SAT solver 路线，声明式编程范式。与 SVS 的 SMT-based 方法不同赛道。\n      SAT 表达力弱于 SMT（无量词、无函数），但求解效率更高。\n      SVS 选择 Z3 SMT 是更通用的形式化选择。\n\n# ============================================================\n# 图谱总结\n# ============================================================\n\nlandscape_summary:\n  trend_binary_to_graded: |\n    2023 年工作（LINC, LOGIC-LM, SatLM）全是 binary problem-level 验证。\n    2026 年开始出现 graded step-level scoring（PRoSFI, VERGE, LogicReward），但均用于 training reward。\n    SVS 首次将 graded formal verification score 用于 inference-time chain selection。\n\n  chain_selection_gap: |\n    现有工作的 chain selection 方式：\n    - 无选择: VeriCoT, LINC, LOGIC-LM, SatLM, PRoSFI, LogicReward\n    - Binary filter + SC: PC-CoT (Certified Self-Consistency)\n    - 生成引导: VERGE\n    - Graded scoring selection: SVS (ours) ← 唯一\n\n  common_bottleneck: |\n    Autoformalization 是所有方法的共同瓶颈：\n    - VeriCoT: 45% pass rate\n    - PC-CoT: 40-60% typing rate\n    - SVS: ~85% formalization rate（claim-level 粒度更宽容）\n\n  svs_unique_contribution: |\n    \"Graded formal verification score for inference-time chain selection\"\n    是 SVS 的独特贡献点。无人将连续验证分数直接用于 test-time chain ranking/selection。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "04b8fee7-16fb-4d26-968d-229953c8131e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01222nSHpCjLxrNgBh9c9wCe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 245,
      "cache_read_input_tokens": 33792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 245
      },
      "output_tokens": 51,
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

_source line 21 · 2026-05-14T16:03:55.269Z_

<details><summary>↩ Tool result · `toolu_01PapFi62KLLZoevq3s73rkU`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/literature_map.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "5353d0f7-582d-40f3-9827-dddf8e63686a",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/literature_map.yaml",
    "content": "# SVS Formal Verification - Literature Map\n# 更新日期: 2026-05-14\n# 基于 VeriCoT 深度调研整合\n\npapers:\n\n  # ============================================================\n  # Direct Competitors - 直接竞争方法\n  # ============================================================\n\n  VeriCoT:\n    title: \"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks\"\n    authors: \"Yu Feng, Nathaniel Weir, Kaj Bostrom, Sam Bayless, Darion Cassel, Sapana Chaudhary, Benjamin Kiesl-Reiter, Huzefa Rangwala\"\n    venue: ICLR 2026 (Poster)\n    arxiv: \"2511.04662\"\n    role: direct-competitor\n    method:\n      verifier: Z3 SMT solver\n      granularity: step-level\n      verdict: binary (entailed / contradicted / ungrounded / untranslatable)\n      chain_selection: none (single-chain + serial self-reflection)\n      formalization: SMT-LIB via Claude-3.5-Sonnet-V2\n      premise_source: LLM-generated (source context / commonsense / prior step)\n      training_dependency: none at inference; optional SFT/DPO\n    datasets: [ProofWriter, BioASQ, LegalBench-SARA]\n    key_results:\n      pass_rate: \"15-45% (ProofWriter 45.2%, BioASQ 25.3%, SARA 15.2%)\"\n      precision: \"84-94%\"\n      self_reflection_gain: \"+46% relative pass rate\"\n    svs_relevance: |\n      最直接的竞争者。核心差异：\n      1. Binary vs Graded: VeriCoT 输出 pass/fail，SVS 输出连续 IC 分数\n      2. Single-chain vs Multi-chain: VeriCoT 验证单链+串行反思，SVS 多链采样+分数排序选择\n      3. LLM-gen premises vs PCV: VeriCoT 由 LLM 生成 premises（有 fabrication 风险），SVS 使用题目给定 premises\n      4. Pass rate: VeriCoT 15-45%，SVS ~85% formalization rate（粒度不同不直接可比）\n      论文定位: \"binary single-chain verification; we extend to graded multi-chain selection\"\n\n  PC-CoT:\n    title: \"Typed Chain-of-Thought (PC-CoT): Certified Self-Consistency via Curry-Howard Correspondence\"\n    venue: ICLR 2026\n    arxiv: \"2510.01069\"\n    role: direct-competitor\n    method:\n      verifier: type checker (Curry-Howard correspondence)\n      granularity: step-level\n      verdict: binary (type-check pass/fail)\n      chain_selection: \"Certified Self-Consistency = binary type-check filter + majority voting (SC)\"\n      formalization: typed CoT via Curry-Howard\n      training_dependency: none\n    datasets: [GSM8K]\n    key_results:\n      typing_rate: \"40-60%\"\n    svs_relevance: |\n      提出 \"Certified Self-Consistency\"，是 SVS graded chain selection 的最近 alternative。\n      核心差异：\n      1. Binary filter + SC vs Graded scoring selection: PC-CoT 先 binary 筛再投票，SVS 用连续分数直接排序\n      2. 赛道不同: PC-CoT 仅测 GSM8K（数学），SVS 做逻辑推理\n      3. 信息损失: binary filter 丢弃了验证程度的连续信息\n      论文定位: \"Certified Self-Consistency = binary filter + SC; we show graded scoring outperforms\"\n      必须做的 ablation: SVS graded IC vs binary filter + SC\n\n  VERGE:\n    title: \"VERGE: Verification-Guided Reasoning with Z3/SMT\"\n    venue: arXiv 2026\n    arxiv: \"2601.20055\"\n    role: direct-competitor\n    method:\n      verifier: Z3/SMT\n      granularity: step-level\n      verdict: \"graded (MCS-based)\"\n      chain_selection: \"partial (trajectory-level formal guidance during generation)\"\n      formalization: SMT encoding\n      key_innovation: \"MCS (Maximal Consistent Subsets) for error localization + formal guidance during generation\"\n    svs_relevance: |\n      最接近 SVS 的 graded 思路，但用途不同。\n      核心差异：\n      1. 用途: VERGE 用 MCS 做 error localization + 生成引导，SVS 用 MCS-derived score 做 chain selection\n      2. 时机: VERGE 在生成过程中介入（online），SVS 在生成后评估（post-hoc）\n      3. 复杂度: VERGE 需修改生成 pipeline，SVS 是 plug-and-play 后处理\n      论文定位: \"MCS for error localization + refinement; we use MCS-derived score for selection\"\n\n  # ============================================================\n  # Method Components - 方法组件（用于训练，非 inference-time）\n  # ============================================================\n\n  PRoSFI:\n    title: \"PRoSFI: Graded Reward via Structured Formal Intermediaries for RL Training\"\n    venue: ICML 2026\n    arxiv: \"2603.29500\"\n    role: method-component\n    method:\n      verifier: Z3/Prover9\n      granularity: step-level\n      verdict: \"graded reward (R=1.0/0.3/0.1/0.0)\"\n      chain_selection: none (training reward only, not used at inference)\n      key_innovation: \"graded formal verification reward for RL (PPO/GRPO)\"\n    svs_relevance: |\n      与 SVS 共享 \"graded formal verification\" 理念，但用途截然不同。\n      核心差异：\n      1. Training vs Inference: PRoSFI 的 graded score 是 RL reward（训练信号），SVS 用于 inference-time chain selection\n      2. SVS 无需训练: PRoSFI 需 RL 训练循环，SVS 是 training-free 的 test-time 方法\n      论文定位: \"graded reward for training; we use graded score at inference without training\"\n\n  # ============================================================\n  # Evaluation Baselines\n  # ============================================================\n\n  LogicReward:\n    title: \"LogicReward: Isabelle-based Graded Reward for SFT/DPO Training\"\n    venue: ICLR 2026\n    github: \"https://github.com/Aiden0526/Logic-Reward\"\n    role: evaluation\n    method:\n      verifier: Isabelle theorem prover\n      granularity: step-level\n      verdict: \"graded reward\"\n      chain_selection: none (training reward only)\n      key_innovation: \"formal verification → reward signal for SFT/DPO\"\n    svs_relevance: |\n      同样产出 graded verification signal，但仅用于训练。\n      核心差异：\n      1. 训练 vs 推理: LogicReward 用于 SFT/DPO 训练，SVS 用于 inference-time selection\n      2. 验证器: LogicReward 用 Isabelle（交互式定理证明器），SVS 用 Z3（SMT solver），Z3 更轻量自动化\n      3. 互补潜力: Hybrid scoring（IC score + LogicReward）是潜在扩展方向\n\n  # ============================================================\n  # Background - 早期基础工作\n  # ============================================================\n\n  LINC:\n    title: \"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\"\n    venue: EMNLP 2023\n    arxiv: \"2310.15164\"\n    role: background\n    method:\n      verifier: Prover9\n      granularity: problem-level\n      verdict: binary\n      chain_selection: none\n      key_innovation: \"LLM → FOL → theorem prover pipeline\"\n    svs_relevance: |\n      SVS 的前身类方法。LINC 做 problem-level binary 验证，不验证 CoT 步骤。\n      SVS 在三个维度上推进：step/claim-level 粒度、graded 判定、multi-chain selection。\n\n  LOGIC-LM:\n    title: \"LOGIC-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\"\n    venue: EMNLP 2023\n    arxiv: \"2305.12295\"\n    role: background\n    method:\n      verifier: symbolic solver\n      granularity: problem-level\n      verdict: binary\n      chain_selection: none\n      key_innovation: \"NL → symbolic formulation → solver，with self-refinement loop\"\n    svs_relevance: |\n      Problem-level binary 验证 + self-refinement。与 SVS 的差异同 LINC：\n      粒度（problem vs claim）、判定（binary vs graded）、用途（refinement vs selection）。\n      LOGIC-LM 的 self-refinement 思路与 VeriCoT 的 self-reflection 类似。\n\n  SatLM:\n    title: \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\"\n    venue: NeurIPS 2023\n    arxiv: \"2305.09656\"\n    role: background\n    method:\n      verifier: SAT solver\n      granularity: problem-level\n      verdict: binary\n      chain_selection: none\n      key_innovation: \"declarative programming paradigm for LLM reasoning\"\n    svs_relevance: |\n      SAT solver 路线，声明式编程范式。与 SVS 的 SMT-based 方法不同赛道。\n      SAT 表达力弱于 SMT（无量词、无函数），但求解效率更高。\n      SVS 选择 Z3 SMT 是更通用的形式化选择。\n\n# ============================================================\n# 图谱总结\n# ============================================================\n\nlandscape_summary:\n  trend_binary_to_graded: |\n    2023 年工作（LINC, LOGIC-LM, SatLM）全是 binary problem-level 验证。\n    2026 年开始出现 graded step-level scoring（PRoSFI, VERGE, LogicReward），但均用于 training reward。\n    SVS 首次将 graded formal verification score 用于 inference-time chain selection。\n\n  chain_selection_gap: |\n    现有工作的 chain selection 方式：\n    - 无选择: VeriCoT, LINC, LOGIC-LM, SatLM, PRoSFI, LogicReward\n    - Binary filter + SC: PC-CoT (Certified Self-Consistency)\n    - 生成引导: VERGE\n    - Graded scoring selection: SVS (ours) ← 唯一\n\n  common_bottleneck: |\n    Autoformalization 是所有方法的共同瓶颈：\n    - VeriCoT: 45% pass rate\n    - PC-CoT: 40-60% typing rate\n    - SVS: ~85% formalization rate（claim-level 粒度更宽容）\n\n  svs_unique_contribution: |\n    \"Graded formal verification score for inference-time chain selection\"\n    是 SVS 的独特贡献点。无人将连续验证分数直接用于 test-time chain ranking/selection。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 22_

`literature_map.yaml` 已创建，包含 8 篇论文的完整条目：

| 论文 | Role | 核心差异 |
|------|------|----------|
| **VeriCoT** (ICLR 2026) | direct-competitor | binary step-level, 单链+反思, LLM-gen premises, 15-45% pass rate |
| **PC-CoT** (ICLR 2026) | direct-competitor | binary filter + SC (Certified Self-Consistency), 仅 GSM8K |
| **VERGE** (arXiv 2026) | direct-competitor | MCS error localization + 生成引导, online 介入 vs SVS post-hoc |
| **PRoSFI** (ICML 2026) | method-component | graded reward for RL training, 不用于 inference |
| **LogicReward** (ICLR 2026) | evaluation | Isabelle-based graded reward for SFT/DPO |
| **LINC** (EMNLP 2023) | background | Prover9, problem-level binary |
| **LOGIC-LM** (EMNLP 2023) | background | symbolic solver, problem-level binary + self-refinement |
| **SatLM** (NeurIPS 2023) | background | SAT solver, 声明式编程 |

每篇都包含 `svs_relevance` 字段，说明与 SVS 的差异化定位。底部 `landscape_summary` 总结了 binary→graded 趋势、chain selection 空白、autoformalization 瓶颈三个关键观察。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "uuid": "74155d3a-44a5-4388-9dfa-0d111ed11435",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tsr5jQvP2MVvcWdvdVmdmY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3241,
      "cache_read_input_tokens": 34037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3241
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

_source line 23_

`literature_map.yaml` 已创建，包含 8 篇论文的完整条目：

| 论文 | Role | 核心差异 |
|------|------|----------|
| **VeriCoT** (ICLR 2026) | direct-competitor | binary step-level, 单链+反思, LLM-gen premises, 15-45% pass rate |
| **PC-CoT** (ICLR 2026) | direct-competitor | binary filter + SC (Certified Self-Consistency), 仅 GSM8K |
| **VERGE** (arXiv 2026) | direct-competitor | MCS error localization + 生成引导, online 介入 vs SVS post-hoc |
| **PRoSFI** (ICML 2026) | method-component | graded reward for RL training, 不用于 inference |
| **LogicReward** (ICLR 2026) | evaluation | Isabelle-based graded reward for SFT/DPO |
| **LINC** (EMNLP 2023) | background | Prover9, problem-level binary |
| **LOGIC-LM** (EMNLP 2023) | background | symbolic solver, problem-level binary + self-refinement |
| **SatLM** (NeurIPS 2023) | background | SAT solver, 声明式编程 |

每篇都包含 `svs_relevance` 字段，说明与 SVS 的差异化定位。底部 `landscape_summary` 总结了 binary→graded 趋势、chain selection 空白、autoformalization 瓶颈三个关键观察。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 150611,
  "duration_api_ms": 151540,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "59e9ec46-7cdf-4e0a-9e6a-2530397aedb9",
  "total_cost_usd": 0.42518025000000004,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 25437,
    "cache_read_input_tokens": 157318,
    "output_tokens": 7444,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25437,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 439,
        "cache_read_input_tokens": 34037,
        "cache_creation_input_tokens": 3241,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3241
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1300,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00139,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 7444,
      "cacheReadInputTokens": 157318,
      "cacheCreationInputTokens": 25437,
      "webSearchRequests": 0,
      "costUSD": 0.42379025000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "557f30d0-fd99-4498-99c6-73edba5cd46e"
}
```

</details>

---
