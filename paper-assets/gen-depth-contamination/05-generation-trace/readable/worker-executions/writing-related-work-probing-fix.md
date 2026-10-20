# writing related work probing fix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_writing_related-work-probing-fix_20260514T045514.log`
- **Structured JSON:** [`7e476284cb9f9cfabcf3.json`](../../sessions/7e/7e476284cb9f9cfabcf3.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
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
  "uuid": "b3445d3e-6fa2-45ae-9435-61011eec7a37",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1778745000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d9a195e3-b488-4aea-8877-110c8302999b",
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8"
}
```

---

### Assistant

_source line 4_

Let me start by reading the audit file and the current related work tex file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "fc96d012-f2e6-470b-9f26-adf68a659a47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VucBvKgwadh19qyUv6tnnP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11293,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11293
      },
      "output_tokens": 2,
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

<details open><summary>🔧 Tool call — Read · `toolu_0167uhqfkceTt2Bc13UhuHJ1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/drafts/related_work_audit.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "de0ad87a-707c-4143-9f88-6518adcab67f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VucBvKgwadh19qyUv6tnnP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11293,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11293
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-14T04:55:31.523Z_

<details><summary>↩ Tool result · `toolu_0167uhqfkceTt2Bc13UhuHJ1`</summary>

```text
1	# Related Work 完整性审查
2	
3	审查日期: 2026-05-14
4	审查范围: `related_work.tex` (54行, 5个段落)
5	
6	---
7	
8	## 已覆盖
9	
10	### Model Collapse and Recursive Generation
11	- Shumailov et al. (2024, Nature): line 6, tail-distribution degradation
12	- Alemohammad et al. (2024, ICLR): line 7, self-consuming models, fixed point convergence
13	- Dohmatob et al. (2024, ICML): line 8, scaling laws for tail loss
14	- Schaeffer et al. (2025, ICML): line 9-10, 8-definition taxonomy, K* 与 Family B 对齐
15	- Kazdan et al. (2025, ICML): line 11-12, replace vs accumulate regimes
16	- Shi et al. (2025, NeurIPS Spotlight): line 13, generalization-to-memorization transition
17	- Amin et al. (2025, NeurIPS): line 47, weak signals suffice to escape collapse
18	- Gambetta et al. (2025): line 48, surplexity metric
19	
20	### Binary Synthetic Text Detection
21	- GLTR (Gehrmann et al. 2019): line 18, token-level likelihood visualization
22	- Grover (Zellers et al. 2019): line 19, generator-as-detector
23	- Ippolito et al. (2020): line 19, detection difficulty vs generation quality
24	- DetectGPT (Mitchell et al. 2023): line 20, probability curvature
25	- Binoculars (Hans et al. 2024): line 21, cross-perplexity ratio
26	- DivEye (Basani et al. 2026): line 22, surprisal diversity
27	- Min-K%++ (Zhang et al. 2024): line 22, outlier token likelihoods
28	- CoDeC (Zawalski et al. 2026): line 23, in-context learning contamination detection
29	
30	### Ordinal Classification
31	- CORAL (Cao et al. 2020): line 32-33, rank-consistent ordinal regression
32	
33	### Data Selection and Curation
34	- DSIR (Xie et al. 2023): line 40, importance resampling
35	- D4 (Tirumala et al. 2023): line 41, deduplication + diversification
36	- DoReMi (Xie et al. 2023): line 41, domain weight optimization
37	- Drayson et al. (2025): line 44-46, binary detection + SIR (positioned as special case of our framework)
38	
39	### Watermarking
40	- Kirchenbauer et al. (2023): line 52-53, statistical watermarking
41	
42	---
43	
44	## 需要补充
45	
46	### 1. [高优先] Probing Classifiers 文献 — 支撑 Neural Probe 实验
47	
48	**Gap**: discussion.tex (lines 29-35, 123-129) 和 conclusion.tex (line 45) 大量讨论 frozen-encoder + MLP probe 实验，但 Related Work 中完全没有 probing classifiers 的文献支撑。审稿人会质疑方法选择的依据。
49	
50	**建议**: 在 Ordinal Classification 段落之后新增一个段落，或在 Ordinal Classification 段末追加 2-3 句。
51	
52	**需要引用**:
53	- Alain & Bengio (2017), "Understanding intermediate layers using linear classifier probes" — 提出用线性探针分析网络中间表征，是 frozen-encoder probing 的方法论基础
54	- Conneau et al. (2018), "What you can cram into a single $&!#* vector: Probing sentence embeddings for linguistic properties" (ACL) — 系统研究 sentence embedding 编码了哪些语言学属性
55	- Belinkov (2022), "Probing Classifiers: Promises, Shortcomings, and Advances" (CL) — probing 方法的综述，讨论了 probe 复杂度与结论有效性的权衡
56	
57	**建议文本**:
58	
59	> \paragraph{Probing Classifiers.}
60	> Linear and shallow MLP probes have become a standard tool for analyzing what information is encoded in pretrained representations~\cite{alain2017understanding,conneau2018probing}.
61	> Belinkov~\cite{belinkov2022probing} surveys the methodology and cautions that probe complexity must be controlled to ensure that performance reflects representational content rather than probe capacity.
62	> Our neural probe experiment follows this protocol: a two-layer MLP on frozen Qwen2.5-1.5B embeddings, where the probe's limited capacity ensures that discriminability reflects information present in the representations rather than learned de novo.
63	
64	### 2. [中优先] Fast-DetectGPT — Binary Detection 段落补充
65	
66	**Gap**: DetectGPT 已引用，但其改进版 Fast-DetectGPT 在 2024 年成为 zero-shot 检测的新 SOTA，被广泛引用。
67	
68	**建议**: 在 line 20 (DetectGPT 之后) 追加一句。
69	
70	**需要引用**:
71	- Bao et al. (2024), "Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature" (ICLR 2024)
72	
73	**建议文本**: 在 Mitchell et al. 句后加:
74	
75	> Bao et al.~\cite{bao2024fastdetectgpt} improved efficiency by replacing perturbation sampling with conditional probability curvature, achieving comparable accuracy with orders-of-magnitude speedup.
76	
77	### 3. [中优先] Gerstgrasser et al. (2024) — Model Collapse 理论补充
78	
79	**Gap**: 现有 model collapse 覆盖全面，但缺少 Gerstgrasser et al. 关于 collapse 可避免条件的理论分析。该工作与本文的 data curation 动机直接相关——他们证明保留足够的原始数据可以避免 collapse，本文的 depth-aware filtering 正是实现这一点的工具。
80	
81	**建议**: 在 line 13 (Shi et al.) 之后追加一句。
82	
83	**需要引用**:
84	- Gerstgrasser et al. (2024), "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" (arXiv 2404.01413)
85	
86	**建议文本**:
87	
88	> Gerstgrasser et al.~\cite{gerstgrasser2024inevitable} proved that collapse is avoidable when sufficient original data is retained alongside synthetic samples, a condition that depth-aware curation can enforce by construction.
89	
90	### 4. [低-中优先] Ordinal Classification 补充
91	
92	**Gap**: 仅引用 CORAL 一篇。Ordinal classification 是本文方法的核心组件（OBD head），仅一篇引用显得单薄。
93	
94	**建议**: 在 CORAL 引用后追加 1-2 篇经典方法。
95	
96	**需要引用**:
97	- Frank & Hall (2001), "A Simple Approach to Ordinal Classification" (ECML) — 将 ordinal 问题分解为一系列二分类的开创性工作，与 OBD head 的 boundary detection 思路直接对应
98	- Diaz & Marathe (2019), "Soft Labels for Ordinal Regression" (CVPR) — soft label 方法，与 OBD 的 monotonic probability 设计相关
99	
100	**建议文本**: 在 line 33 CORAL 句后追加:
101	
102	> The idea of decomposing ordinal problems into a series of binary decisions dates to Frank \& Hall~\cite{frank2001ordinal}; our OBD head follows this principle by learning $K\!-\!1$ cumulative boundary classifiers.
103	
104	---
105	
106	## 可选改进
107	
108	### 1. Self-Refinement 文献补充
109	
110	**理由**: Related Work line 27 提到 "beneficial recursive generation (e.g., self-refinement)" 但没有引用。添加一篇可以增强论点。
111	
112	**建议引用**: Madaan et al. (2023), "Self-Refine: Iterative Refinement with Self-Feedback" (NeurIPS 2023)
113	
114	**位置**: line 27, 将 "self-refinement" 处加引用即可。
115	
116	### 2. Trained/Fine-tuned 检测器覆盖
117	
118	**理由**: Binary Detection 段落偏重 zero-shot 和 statistical 方法。如有 fine-tuned detector 的工作（如 OpenAI text classifier, Ghostbuster），可以在 line 19 附近用一句话覆盖 supervised 检测方向，说明本文的 ordinal approach 与之的关系。但这不是必须的，因为本文聚焦 post-hoc 无训练数据场景。
119	
120	### 3. Multi-class AI Text Attribution
121	
122	**理由**: 有一些工作不只做二分类，而是区分不同 LLM 生成的文本（source attribution）。与本文的 ordinal depth 不同但相关。如果空间允许可以提一句以示区分。
123	
124	**建议引用**: Uchendu et al. (2020), "Authorship Attribution for Neural Text Generation" (EMNLP)
125	
126	### 4. Data Contamination (Benchmark) 文献
127	
128	**理由**: CoDeC 已覆盖 benchmark contamination detection，但该方向有更多工作（Golchin & Surdeanu 2024, Oren et al. 2024）。不过本文的 "contamination" 指 recursive generation contamination 而非 benchmark data leakage，过多引用可能造成混淆。现有覆盖已足够。
129	
130	---
131	
132	## 总结
133	
134	| 类别 | 状态 | 行动 |
135	|------|------|------|
136	| Model collapse | ✅ 充分 | 可选补 Gerstgrasser (collapse avoidability) |
137	| Binary detection | ✅ 充分 | 可选补 Fast-DetectGPT |
138	| Ordinal classification | ⚠️ 偏薄 | 建议补 Frank & Hall |
139	| Data selection | ✅ 充分 | 无需补充 |
140	| Watermarking | ✅ 充分 | 无需补充 |
141	| **Probing classifiers** | ❌ **缺失** | **必须补充** — neural probe 实验缺文献支撑 |
142	
143	**最高优先级**: 补充 Probing Classifiers 段落（Alain & Bengio 2017, Conneau et al. 2018, Belinkov 2022），直接支撑 discussion.tex 中的 neural probe 实验设计。
144	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "1d623c7d-d2a7-48ec-9248-f6939d5953e1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/drafts/related_work_audit.md",
      "content": "# Related Work 完整性审查\n\n审查日期: 2026-05-14\n审查范围: `related_work.tex` (54行, 5个段落)\n\n---\n\n## 已覆盖\n\n### Model Collapse and Recursive Generation\n- Shumailov et al. (2024, Nature): line 6, tail-distribution degradation\n- Alemohammad et al. (2024, ICLR): line 7, self-consuming models, fixed point convergence\n- Dohmatob et al. (2024, ICML): line 8, scaling laws for tail loss\n- Schaeffer et al. (2025, ICML): line 9-10, 8-definition taxonomy, K* 与 Family B 对齐\n- Kazdan et al. (2025, ICML): line 11-12, replace vs accumulate regimes\n- Shi et al. (2025, NeurIPS Spotlight): line 13, generalization-to-memorization transition\n- Amin et al. (2025, NeurIPS): line 47, weak signals suffice to escape collapse\n- Gambetta et al. (2025): line 48, surplexity metric\n\n### Binary Synthetic Text Detection\n- GLTR (Gehrmann et al. 2019): line 18, token-level likelihood visualization\n- Grover (Zellers et al. 2019): line 19, generator-as-detector\n- Ippolito et al. (2020): line 19, detection difficulty vs generation quality\n- DetectGPT (Mitchell et al. 2023): line 20, probability curvature\n- Binoculars (Hans et al. 2024): line 21, cross-perplexity ratio\n- DivEye (Basani et al. 2026): line 22, surprisal diversity\n- Min-K%++ (Zhang et al. 2024): line 22, outlier token likelihoods\n- CoDeC (Zawalski et al. 2026): line 23, in-context learning contamination detection\n\n### Ordinal Classification\n- CORAL (Cao et al. 2020): line 32-33, rank-consistent ordinal regression\n\n### Data Selection and Curation\n- DSIR (Xie et al. 2023): line 40, importance resampling\n- D4 (Tirumala et al. 2023): line 41, deduplication + diversification\n- DoReMi (Xie et al. 2023): line 41, domain weight optimization\n- Drayson et al. (2025): line 44-46, binary detection + SIR (positioned as special case of our framework)\n\n### Watermarking\n- Kirchenbauer et al. (2023): line 52-53, statistical watermarking\n\n---\n\n## 需要补充\n\n### 1. [高优先] Probing Classifiers 文献 — 支撑 Neural Probe 实验\n\n**Gap**: discussion.tex (lines 29-35, 123-129) 和 conclusion.tex (line 45) 大量讨论 frozen-encoder + MLP probe 实验，但 Related Work 中完全没有 probing classifiers 的文献支撑。审稿人会质疑方法选择的依据。\n\n**建议**: 在 Ordinal Classification 段落之后新增一个段落，或在 Ordinal Classification 段末追加 2-3 句。\n\n**需要引用**:\n- Alain & Bengio (2017), \"Understanding intermediate layers using linear classifier probes\" — 提出用线性探针分析网络中间表征，是 frozen-encoder probing 的方法论基础\n- Conneau et al. (2018), \"What you can cram into a single $&!#* vector: Probing sentence embeddings for linguistic properties\" (ACL) — 系统研究 sentence embedding 编码了哪些语言学属性\n- Belinkov (2022), \"Probing Classifiers: Promises, Shortcomings, and Advances\" (CL) — probing 方法的综述，讨论了 probe 复杂度与结论有效性的权衡\n\n**建议文本**:\n\n> \\paragraph{Probing Classifiers.}\n> Linear and shallow MLP probes have become a standard tool for analyzing what information is encoded in pretrained representations~\\cite{alain2017understanding,conneau2018probing}.\n> Belinkov~\\cite{belinkov2022probing} surveys the methodology and cautions that probe complexity must be controlled to ensure that performance reflects representational content rather than probe capacity.\n> Our neural probe experiment follows this protocol: a two-layer MLP on frozen Qwen2.5-1.5B embeddings, where the probe's limited capacity ensures that discriminability reflects information present in the representations rather than learned de novo.\n\n### 2. [中优先] Fast-DetectGPT — Binary Detection 段落补充\n\n**Gap**: DetectGPT 已引用，但其改进版 Fast-DetectGPT 在 2024 年成为 zero-shot 检测的新 SOTA，被广泛引用。\n\n**建议**: 在 line 20 (DetectGPT 之后) 追加一句。\n\n**需要引用**:\n- Bao et al. (2024), \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\" (ICLR 2024)\n\n**建议文本**: 在 Mitchell et al. 句后加:\n\n> Bao et al.~\\cite{bao2024fastdetectgpt} improved efficiency by replacing perturbation sampling with conditional probability curvature, achieving comparable accuracy with orders-of-magnitude speedup.\n\n### 3. [中优先] Gerstgrasser et al. (2024) — Model Collapse 理论补充\n\n**Gap**: 现有 model collapse 覆盖全面，但缺少 Gerstgrasser et al. 关于 collapse 可避免条件的理论分析。该工作与本文的 data curation 动机直接相关——他们证明保留足够的原始数据可以避免 collapse，本文的 depth-aware filtering 正是实现这一点的工具。\n\n**建议**: 在 line 13 (Shi et al.) 之后追加一句。\n\n**需要引用**:\n- Gerstgrasser et al. (2024), \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\" (arXiv 2404.01413)\n\n**建议文本**:\n\n> Gerstgrasser et al.~\\cite{gerstgrasser2024inevitable} proved that collapse is avoidable when sufficient original data is retained alongside synthetic samples, a condition that depth-aware curation can enforce by construction.\n\n### 4. [低-中优先] Ordinal Classification 补充\n\n**Gap**: 仅引用 CORAL 一篇。Ordinal classification 是本文方法的核心组件（OBD head），仅一篇引用显得单薄。\n\n**建议**: 在 CORAL 引用后追加 1-2 篇经典方法。\n\n**需要引用**:\n- Frank & Hall (2001), \"A Simple Approach to Ordinal Classification\" (ECML) — 将 ordinal 问题分解为一系列二分类的开创性工作，与 OBD head 的 boundary detection 思路直接对应\n- Diaz & Marathe (2019), \"Soft Labels for Ordinal Regression\" (CVPR) — soft label 方法，与 OBD 的 monotonic probability 设计相关\n\n**建议文本**: 在 line 33 CORAL 句后追加:\n\n> The idea of decomposing ordinal problems into a series of binary decisions dates to Frank \\& Hall~\\cite{frank2001ordinal}; our OBD head follows this principle by learning $K\\!-\\!1$ cumulative boundary classifiers.\n\n---\n\n## 可选改进\n\n### 1. Self-Refinement 文献补充\n\n**理由**: Related Work line 27 提到 \"beneficial recursive generation (e.g., self-refinement)\" 但没有引用。添加一篇可以增强论点。\n\n**建议引用**: Madaan et al. (2023), \"Self-Refine: Iterative Refinement with Self-Feedback\" (NeurIPS 2023)\n\n**位置**: line 27, 将 \"self-refinement\" 处加引用即可。\n\n### 2. Trained/Fine-tuned 检测器覆盖\n\n**理由**: Binary Detection 段落偏重 zero-shot 和 statistical 方法。如有 fine-tuned detector 的工作（如 OpenAI text classifier, Ghostbuster），可以在 line 19 附近用一句话覆盖 supervised 检测方向，说明本文的 ordinal approach 与之的关系。但这不是必须的，因为本文聚焦 post-hoc 无训练数据场景。\n\n### 3. Multi-class AI Text Attribution\n\n**理由**: 有一些工作不只做二分类，而是区分不同 LLM 生成的文本（source attribution）。与本文的 ordinal depth 不同但相关。如果空间允许可以提一句以示区分。\n\n**建议引用**: Uchendu et al. (2020), \"Authorship Attribution for Neural Text Generation\" (EMNLP)\n\n### 4. Data Contamination (Benchmark) 文献\n\n**理由**: CoDeC 已覆盖 benchmark contamination detection，但该方向有更多工作（Golchin & Surdeanu 2024, Oren et al. 2024）。不过本文的 \"contamination\" 指 recursive generation contamination 而非 benchmark data leakage，过多引用可能造成混淆。现有覆盖已足够。\n\n---\n\n## 总结\n\n| 类别 | 状态 | 行动 |\n|------|------|------|\n| Model collapse | ✅ 充分 | 可选补 Gerstgrasser (collapse avoidability) |\n| Binary detection | ✅ 充分 | 可选补 Fast-DetectGPT |\n| Ordinal classification | ⚠️ 偏薄 | 建议补 Frank & Hall |\n| Data selection | ✅ 充分 | 无需补充 |\n| Watermarking | ✅ 充分 | 无需补充 |\n| **Probing classifiers** | ❌ **缺失** | **必须补充** — neural probe 实验缺文献支撑 |\n\n**最高优先级**: 补充 Probing Classifiers 段落（Alain & Bengio 2017, Conneau et al. 2018, Belinkov 2022），直接支撑 discussion.tex 中的 neural probe 实验设计。\n",
      "numLines": 144,
      "startLine": 1,
      "totalLines": 144
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01QtQcwHF8rWo5sRzkY1asin`</summary>

```json
{
  "pattern": "paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "caddf4b1-cf2b-40af-9d64-c9327072be66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VucBvKgwadh19qyUv6tnnP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11293,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11293
      },
      "output_tokens": 2,
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

_source line 8 · 2026-05-14T04:55:32.556Z_

<details><summary>↩ Tool result · `toolu_01QtQcwHF8rWo5sRzkY1asin`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "8582c5b3-b54d-431d-811f-d34495b95698",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 16,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_012VcftRadY3AeiZzxQCpZoZ`</summary>

```json
{
  "pattern": "paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "61e7eab7-b3f0-4b74-9eeb-2ec9b36e1bf4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VucBvKgwadh19qyUv6tnnP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11293,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11293
      },
      "output_tokens": 2,
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

_source line 10 · 2026-05-14T04:55:32.793Z_

<details><summary>↩ Tool result · `toolu_012VcftRadY3AeiZzxQCpZoZ`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "d82f4628-f843-467c-a4a5-7c5929e0cb37",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 10,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
The paper files are not in the expected location. Let me search more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "7b320302-4490-4e7e-8c3c-3f644a16870a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWK3V9EVPb7hWTZJNKqpyG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3532,
      "cache_read_input_tokens": 23134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3532
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

_source line 12_

Paper files not found in `paper/` directory. Let me search for them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "60e1806c-c355-47e6-a8e6-2e417a64d64a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWK3V9EVPb7hWTZJNKqpyG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3532,
      "cache_read_input_tokens": 23134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3532
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

<details open><summary>🔧 Tool call — Glob · `toolu_013K3FydMDBcmPqNBZnbusER`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "af3a5b2a-6e7c-440d-9864-2f21c9c16c0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWK3V9EVPb7hWTZJNKqpyG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3532,
      "cache_read_input_tokens": 23134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3532
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

_source line 14 · 2026-05-14T04:55:42.549Z_

<details><summary>↩ Tool result · `toolu_013K3FydMDBcmPqNBZnbusER`</summary>

```text
artifacts/dream_reports/dream_20260512T200328/best/paper.tex
artifacts/dream_reports/dream_20260512T200328/median/paper.tex
artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
artifacts/dream_reports/dream_20260513T080728/best/paper.tex
artifacts/dream_reports/dream_20260513T080728/median/paper.tex
artifacts/dream_reports/dream_20260513T080728/worst/paper.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_c1.tex
docs/paper/method.tex
docs/paper/appendix.tex
docs/paper/main.tex
docs/paper/experiments_c1.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "a985b823-a966-406b-b72b-1b3e8445c0ec",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260512T200328/best/paper.tex",
      "artifacts/dream_reports/dream_20260512T200328/median/paper.tex",
      "artifacts/dream_reports/dream_20260512T200328/worst/paper.tex",
      "artifacts/dream_reports/dream_20260513T080728/best/paper.tex",
      "artifacts/dream_reports/dream_20260513T080728/median/paper.tex",
      "artifacts/dream_reports/dream_20260513T080728/worst/paper.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/experiments_c1.tex",
      "docs/paper/method.tex",
      "docs/paper/appendix.tex",
      "docs/paper/main.tex",
      "docs/paper/experiments_c1.tex",
      "docs/paper/related_work.tex",
      "docs/paper/introduction.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/discussion.tex"
    ],
    "durationMs": 10,
    "numFiles": 16,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_017jATQap927PRPJ2TcqEgNm`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "9c92da37-439c-47d2-b98c-50e95cbce5da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWK3V9EVPb7hWTZJNKqpyG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3532,
      "cache_read_input_tokens": 23134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3532
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

_source line 16 · 2026-05-14T04:55:42.773Z_

<details><summary>↩ Tool result · `toolu_017jATQap927PRPJ2TcqEgNm`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "7fc47e63-0a1c-4f5a-b447-fb9bd320d265",
  "tool_use_result": {
    "filenames": [
      "docs/paper/references.bib"
    ],
    "durationMs": 7,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 17_

Found them in `docs/paper/`. Let me read the related work and references files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "dd2b8875-ec38-4d2d-97d7-40fd8cf3c725",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNNNPYRvHX6pb3JvMCyC8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 26666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 516
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

<details open><summary>🔧 Tool call — Read · `toolu_01WAcQd4UjSkhc9apNCjY6wA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "dff170bb-997f-4ba7-9c1f-af043ee2092f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNNNPYRvHX6pb3JvMCyC8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 26666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 516
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

_source line 19 · 2026-05-14T04:55:45.751Z_

<details><summary>↩ Tool result · `toolu_01WAcQd4UjSkhc9apNCjY6wA`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model Collapse and Recursive Generation.}
5	Training on model-generated data can cause progressive distribution shift known as \emph{model collapse}.
6	Shumailov et al.~\cite{shumailov2024collapse} showed that iteratively training language models on their own outputs leads to irreversible tail-distribution degradation, with minority modes vanishing across generations.
7	Alemohammad et al.~\cite{alemohammad2024selfconsuming} formalized this for self-consuming generative models, proving convergence to a fixed point under mild regularity conditions.
8	Dohmatob et al.~\cite{dohmatob2024model} derived scaling laws for collapse, demonstrating that tail probability mass is lost at rates predictable from model and data scale.
9	Schaeffer et al.~\cite{schaeffer2025position} organized the fragmented literature into a taxonomy of eight definitions across three families.
10	Our $\Kstar$ aligns with their Family~B (distributional deformation), specifically D4 (collapsing variance) and D6 (mode entanglement)---the features that degrade most rapidly in our experiments are precisely variance-based surprisal measures.
11	Kazdan et al.~\cite{kazdan2025collapse} distinguished \emph{replace} and \emph{accumulate} regimes: in the replace regime each generation completely supplants its predecessor, producing faster collapse.
12	Our prompt-chain protocol operates in the replace regime, so $\Kempirical = 2$ is a conservative lower bound; the accumulate regime would yield slower degradation and higher $\Kstar$.
13	Shi et al.~\cite{shi2025generalization} identified a generalization-to-memorization transition in recursively trained models, providing cross-modal evidence that information loss is progressive.
14	These works characterize the macro dynamics of collapse but do not provide tools for per-text generational depth estimation.
15	
16	\paragraph{Binary Synthetic Text Detection.}
17	Distinguishing machine-generated from human-written text is a well-studied binary classification problem.
18	Early statistical approaches such as GLTR~\cite{gehrmann2019gltr} visualized per-token likelihood ranks to help human annotators spot generated text, establishing that token-level distributional cues are informative for detection.
19	Zellers et al.~\cite{zellers2019grover} demonstrated that the generating model itself is an effective detector, while Ippolito et al.~\cite{ippolito2020detection} analyzed how detection difficulty scales with generation quality.
20	Recent zero-shot methods have narrowed the gap: Mitchell et al.~\cite{mitchell2023detectgpt} introduced DetectGPT, which uses probability curvature to detect machine-generated text without access to the generating model.
21	Hans et al.~\cite{hans2024binoculars} proposed Binoculars, which computes the cross-perplexity ratio between two closely related language models to achieve near-perfect detection without any training data.
22	DivEye~\cite{basani2026diveye} uses surprisal diversity features to detect synthetic text without generator-specific training data, and Min-K\%++~\cite{zhang2024minkpp} adapts membership inference techniques to flag model-generated passages via outlier token likelihoods.
23	CoDeC~\cite{zawalski2026codec} frames contamination detection as in-context learning, calibrating thresholds from few-shot exemplars.
24	
25	All these methods produce binary outputs and do not distinguish generational depth.
26	The connection to membership inference is instructive: Min-K\%++ and related approaches test whether a text appeared in training data---a related but distinct question from how many recursive generation steps it has undergone.
27	A further limitation is that binary detectors cannot separate beneficial recursive generation (e.g., self-refinement, where a model iteratively improves its own output) from harmful recursive contamination, creating systematic false positives when applied to curated synthetic data.
28	Binary features are designed for the human-vs.-synthetic boundary and are not expected to capture fine-grained depth differences, as the distributional shift between adjacent generations is orders of magnitude smaller than the shift between human and first-generation text.
29	
30	\paragraph{Ordinal Classification.}
31	Ordinal regression methods exploit the natural ordering among class labels to improve generalization over nominal classifiers.
32	Cao et al.~\cite{cao2020coral} introduced CORAL, which enforces rank consistency through weight sharing in the output layer, guaranteeing that predicted cumulative probabilities are monotonically non-increasing.
33	Ordinal approaches have been applied in NLP tasks such as sentiment intensity prediction and essay scoring, where adjacent categories share more semantic overlap than distant ones.
34	Generational depth exhibits the same ordinal structure: text at depth~$k$ is distributionally closer to depth~$k\!\pm\!1$ than to depth~$k\!\pm\!3$, because each recursive generation step introduces an incremental distributional shift rather than a discontinuous one.
35	Despite this natural fit, ordinal classification has not been applied to synthetic text depth estimation.
36	Our Ordinal Boundary Detection (OBD) head leverages this ordered structure, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.
37	
38	\paragraph{Data Selection and Curation.}
39	Principled data selection methods improve training corpus quality through distribution matching and deduplication.
40	DSIR~\cite{xie2023dsir} selects pretraining data by importance resampling against a target distribution.
41	D4~\cite{tirumala2023d4} combines deduplication with diversification to reduce redundancy, and DoReMi~\cite{xie2023doremi} learns domain weights via a proxy model to optimize downstream performance.
42	These methods operate on distributional properties of the corpus but do not estimate whether individual documents have undergone recursive generation.
43	
44	The closest prior work is Drayson et al.~\cite{drayson2025}, who combined binary machine-generated text detection with stratified importance resampling (SIR) to filter synthetic content and prevent model collapse.
45	Their approach is a special case of our graduated filtering framework: when $\Kstar = 1$, ordinal depth estimation reduces to binary classification, and depth-aware curation degenerates to their SIR-based scheme.
46	We generalize this binary formulation to ordinal depth estimation, enabling finer-grained curation that preserves mildly contaminated text (depth~1, retaining most original signal) while removing deeply corrupted text (depth~$\geq 3$).
47	Amin et al.~\cite{amin2025escaping} demonstrated that even weak quality signals suffice to escape model collapse when applied iteratively, suggesting that approximate depth estimates beyond $\Kempirical$ may remain practically useful.
48	Gambetta et al.~\cite{gambetta2025surplexity} proposed surplexity as a text quality metric correlated with generative degradation, though without explicit depth calibration.
49	
50	\paragraph{Watermarking and Provenance.}
51	An alternative approach embeds identifiers at generation time.
52	Kirchenbauer et al.~\cite{kirchenbauer2023watermark} proposed statistical watermarking for LLM outputs by partitioning the vocabulary into green and red token lists conditioned on preceding context.
53	Watermarking is complementary to depth estimation: it requires control over the generation process and cooperation from providers, whereas our method operates post-hoc on unwatermarked text.
54	The two approaches address different threat models---watermarking assumes a cooperative generator, while depth estimation targets uncontrolled settings where provenance metadata is unavailable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "b304e9a5-480d-4bca-939e-7ab17139f1ce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Model Collapse and Recursive Generation.}\nTraining on model-generated data can cause progressive distribution shift known as \\emph{model collapse}.\nShumailov et al.~\\cite{shumailov2024collapse} showed that iteratively training language models on their own outputs leads to irreversible tail-distribution degradation, with minority modes vanishing across generations.\nAlemohammad et al.~\\cite{alemohammad2024selfconsuming} formalized this for self-consuming generative models, proving convergence to a fixed point under mild regularity conditions.\nDohmatob et al.~\\cite{dohmatob2024model} derived scaling laws for collapse, demonstrating that tail probability mass is lost at rates predictable from model and data scale.\nSchaeffer et al.~\\cite{schaeffer2025position} organized the fragmented literature into a taxonomy of eight definitions across three families.\nOur $\\Kstar$ aligns with their Family~B (distributional deformation), specifically D4 (collapsing variance) and D6 (mode entanglement)---the features that degrade most rapidly in our experiments are precisely variance-based surprisal measures.\nKazdan et al.~\\cite{kazdan2025collapse} distinguished \\emph{replace} and \\emph{accumulate} regimes: in the replace regime each generation completely supplants its predecessor, producing faster collapse.\nOur prompt-chain protocol operates in the replace regime, so $\\Kempirical = 2$ is a conservative lower bound; the accumulate regime would yield slower degradation and higher $\\Kstar$.\nShi et al.~\\cite{shi2025generalization} identified a generalization-to-memorization transition in recursively trained models, providing cross-modal evidence that information loss is progressive.\nThese works characterize the macro dynamics of collapse but do not provide tools for per-text generational depth estimation.\n\n\\paragraph{Binary Synthetic Text Detection.}\nDistinguishing machine-generated from human-written text is a well-studied binary classification problem.\nEarly statistical approaches such as GLTR~\\cite{gehrmann2019gltr} visualized per-token likelihood ranks to help human annotators spot generated text, establishing that token-level distributional cues are informative for detection.\nZellers et al.~\\cite{zellers2019grover} demonstrated that the generating model itself is an effective detector, while Ippolito et al.~\\cite{ippolito2020detection} analyzed how detection difficulty scales with generation quality.\nRecent zero-shot methods have narrowed the gap: Mitchell et al.~\\cite{mitchell2023detectgpt} introduced DetectGPT, which uses probability curvature to detect machine-generated text without access to the generating model.\nHans et al.~\\cite{hans2024binoculars} proposed Binoculars, which computes the cross-perplexity ratio between two closely related language models to achieve near-perfect detection without any training data.\nDivEye~\\cite{basani2026diveye} uses surprisal diversity features to detect synthetic text without generator-specific training data, and Min-K\\%++~\\cite{zhang2024minkpp} adapts membership inference techniques to flag model-generated passages via outlier token likelihoods.\nCoDeC~\\cite{zawalski2026codec} frames contamination detection as in-context learning, calibrating thresholds from few-shot exemplars.\n\nAll these methods produce binary outputs and do not distinguish generational depth.\nThe connection to membership inference is instructive: Min-K\\%++ and related approaches test whether a text appeared in training data---a related but distinct question from how many recursive generation steps it has undergone.\nA further limitation is that binary detectors cannot separate beneficial recursive generation (e.g., self-refinement, where a model iteratively improves its own output) from harmful recursive contamination, creating systematic false positives when applied to curated synthetic data.\nBinary features are designed for the human-vs.-synthetic boundary and are not expected to capture fine-grained depth differences, as the distributional shift between adjacent generations is orders of magnitude smaller than the shift between human and first-generation text.\n\n\\paragraph{Ordinal Classification.}\nOrdinal regression methods exploit the natural ordering among class labels to improve generalization over nominal classifiers.\nCao et al.~\\cite{cao2020coral} introduced CORAL, which enforces rank consistency through weight sharing in the output layer, guaranteeing that predicted cumulative probabilities are monotonically non-increasing.\nOrdinal approaches have been applied in NLP tasks such as sentiment intensity prediction and essay scoring, where adjacent categories share more semantic overlap than distant ones.\nGenerational depth exhibits the same ordinal structure: text at depth~$k$ is distributionally closer to depth~$k\\!\\pm\\!1$ than to depth~$k\\!\\pm\\!3$, because each recursive generation step introduces an incremental distributional shift rather than a discontinuous one.\nDespite this natural fit, ordinal classification has not been applied to synthetic text depth estimation.\nOur Ordinal Boundary Detection (OBD) head leverages this ordered structure, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.\n\n\\paragraph{Data Selection and Curation.}\nPrincipled data selection methods improve training corpus quality through distribution matching and deduplication.\nDSIR~\\cite{xie2023dsir} selects pretraining data by importance resampling against a target distribution.\nD4~\\cite{tirumala2023d4} combines deduplication with diversification to reduce redundancy, and DoReMi~\\cite{xie2023doremi} learns domain weights via a proxy model to optimize downstream performance.\nThese methods operate on distributional properties of the corpus but do not estimate whether individual documents have undergone recursive generation.\n\nThe closest prior work is Drayson et al.~\\cite{drayson2025}, who combined binary machine-generated text detection with stratified importance resampling (SIR) to filter synthetic content and prevent model collapse.\nTheir approach is a special case of our graduated filtering framework: when $\\Kstar = 1$, ordinal depth estimation reduces to binary classification, and depth-aware curation degenerates to their SIR-based scheme.\nWe generalize this binary formulation to ordinal depth estimation, enabling finer-grained curation that preserves mildly contaminated text (depth~1, retaining most original signal) while removing deeply corrupted text (depth~$\\geq 3$).\nAmin et al.~\\cite{amin2025escaping} demonstrated that even weak quality signals suffice to escape model collapse when applied iteratively, suggesting that approximate depth estimates beyond $\\Kempirical$ may remain practically useful.\nGambetta et al.~\\cite{gambetta2025surplexity} proposed surplexity as a text quality metric correlated with generative degradation, though without explicit depth calibration.\n\n\\paragraph{Watermarking and Provenance.}\nAn alternative approach embeds identifiers at generation time.\nKirchenbauer et al.~\\cite{kirchenbauer2023watermark} proposed statistical watermarking for LLM outputs by partitioning the vocabulary into green and red token lists conditioned on preceding context.\nWatermarking is complementary to depth estimation: it requires control over the generation process and cooperation from providers, whereas our method operates post-hoc on unwatermarked text.\nThe two approaches address different threat models---watermarking assumes a cooperative generator, while depth estimation targets uncontrolled settings where provenance metadata is unavailable.",
      "numLines": 54,
      "startLine": 1,
      "totalLines": 54
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01V4jq2LRrj4qgak7dDcraiV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "f38c1ec2-2daa-49d3-88de-a0c1a621be48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNNNPYRvHX6pb3JvMCyC8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 26666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 516
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

_source line 21 · 2026-05-14T04:55:46.171Z_

<details><summary>↩ Tool result · `toolu_01V4jq2LRrj4qgak7dDcraiV`</summary>

```text
1	% === References for gen-depth-contamination ===
2	% Source: literature_map.yaml — verified 2026-05-14
3	
4	% === Must-Cite ===
5	
6	@inproceedings{drayson2025,
7	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
8	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
9	  booktitle={Proceedings of EMNLP},
10	  year={2025},
11	  url={https://arxiv.org/abs/2502.15654}
12	}
13	
14	@inproceedings{schaeffer2025position,
15	  title={Position: Model Collapse Does Not Mean What You Think},
16	  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},
17	  booktitle={Proceedings of ICML},
18	  year={2025},
19	  url={https://arxiv.org/abs/2503.03150}
20	}
21	
22	@inproceedings{kazdan2025collapse,
23	  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
24	  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},
25	  booktitle={Proceedings of ICML},
26	  year={2025},
27	  url={https://arxiv.org/abs/2410.16713}
28	}
29	
30	@inproceedings{shi2025generalization,
31	  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
32	  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
33	  booktitle={Advances in NeurIPS},
34	  year={2025},
35	  note={Spotlight},
36	  url={https://arxiv.org/abs/2509.16499}
37	}
38	
39	@inproceedings{mitchell2023detectgpt,
40	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
41	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
42	  booktitle={Proceedings of ICML},
43	  year={2023}
44	}
45	
46	% === Should-Cite ===
47	
48	@article{basani2026diveye,
49	  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},
50	  author={Basani, Advik Raj and Chen, Pin-Yu},
51	  journal={Transactions on Machine Learning Research},
52	  year={2026},
53	  url={https://arxiv.org/abs/2509.18880}
54	}
55	
56	@inproceedings{amin2025escaping,
57	  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},
58	  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},
59	  booktitle={Advances in NeurIPS},
60	  year={2025},
61	  url={https://arxiv.org/abs/2502.08924}
62	}
63	
64	@inproceedings{zawalski2026codec,
65	  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},
66	  author={Zawalski, Micha{\l} and Boubdir, Meriem and Ba{\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},
67	  booktitle={Proceedings of ICLR},
68	  year={2026},
69	  url={https://arxiv.org/abs/2510.27055}
70	}
71	
72	@article{gambetta2025surplexity,
73	  title={Learning by Surprise: Surplexity for Mitigating Model Collapse},
74	  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},
75	  journal={arXiv preprint arXiv:2410.12341},
76	  year={2025},
77	  url={https://arxiv.org/abs/2410.12341}
78	}
79	
80	@inproceedings{zhang2024minkpp,
81	  title={Min-{K}\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
82	  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},
83	  booktitle={Proceedings of EMNLP},
84	  year={2024}
85	}
86	
87	@article{shumailov2024collapse,
88	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
89	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
90	  journal={Nature},
91	  year={2024}
92	}
93	
94	@inproceedings{alemohammad2024selfconsuming,
95	  title={Self-Consuming Generative Models Go {MAD}},
96	  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luber, Lorenzo and Babaei, Ahmed Imtiaz and Letizia, Daniel and Bastani, Osbert and Baraniuk, Richard},
97	  booktitle={Proceedings of ICLR},
98	  year={2024}
99	}
100	
101	@inproceedings{dohmatob2024model,
102	  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},
103	  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},
104	  booktitle={Proceedings of ICML},
105	  year={2024}
106	}
107	
108	@inproceedings{xie2023dsir,
109	  title={Data Selection with Importance Resampling},
110	  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
111	  booktitle={Proceedings of ICML},
112	  year={2023}
113	}
114	
115	@inproceedings{tirumala2023d4,
116	  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},
117	  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},
118	  booktitle={Advances in NeurIPS},
119	  year={2023}
120	}
121	
122	@inproceedings{xie2023doremi,
123	  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},
124	  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},
125	  booktitle={Advances in NeurIPS},
126	  year={2023}
127	}
128	
129	@inproceedings{kirchenbauer2023watermark,
130	  title={A Watermark for Large Language Models},
131	  author={Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
132	  booktitle={Proceedings of ICML},
133	  year={2023}
134	}
135	
136	@inproceedings{gehrmann2019gltr,
137	  title={{GLTR}: Statistical Detection and Visualization of Generated Text},
138	  author={Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
139	  booktitle={Proceedings of ACL: System Demonstrations},
140	  year={2019}
141	}
142	
143	@inproceedings{hans2024binoculars,
144	  title={Spotting {LLMs} With Binoculars},
145	  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
146	  booktitle={Proceedings of ICML},
147	  year={2024}
148	}
149	
150	@article{cao2020coral,
151	  title={Rank consistent ordinal regression for neural networks with application to age estimation},
152	  author={Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
153	  journal={Pattern Recognition Letters},
154	  volume={140},
155	  pages={325--331},
156	  year={2020}
157	}
158	
159	@inproceedings{zellers2019grover,
160	  title={Defending Against Neural Fake News},
161	  author={Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
162	  booktitle={Advances in NeurIPS},
163	  year={2019}
164	}
165	
166	@inproceedings{ippolito2020detection,
167	  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},
168	  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},
169	  booktitle={Proceedings of ACL},
170	  year={2020}
171	}
172	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "fdf9a7b4-d128-40da-b39b-fdd0b3b75ee0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
      "content": "% === References for gen-depth-contamination ===\n% Source: literature_map.yaml — verified 2026-05-14\n\n% === Must-Cite ===\n\n@inproceedings{drayson2025,\n  title={Machine-Generated Text Detection Prevents Language Model Collapse},\n  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  booktitle={Proceedings of EMNLP},\n  year={2025},\n  url={https://arxiv.org/abs/2502.15654}\n}\n\n@inproceedings{schaeffer2025position,\n  title={Position: Model Collapse Does Not Mean What You Think},\n  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2503.03150}\n}\n\n@inproceedings{kazdan2025collapse,\n  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\n  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2410.16713}\n}\n\n@inproceedings{shi2025generalization,\n  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},\n  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  booktitle={Advances in NeurIPS},\n  year={2025},\n  note={Spotlight},\n  url={https://arxiv.org/abs/2509.16499}\n}\n\n@inproceedings{mitchell2023detectgpt,\n  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\n  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n% === Should-Cite ===\n\n@article{basani2026diveye,\n  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},\n  author={Basani, Advik Raj and Chen, Pin-Yu},\n  journal={Transactions on Machine Learning Research},\n  year={2026},\n  url={https://arxiv.org/abs/2509.18880}\n}\n\n@inproceedings{amin2025escaping,\n  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},\n  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},\n  booktitle={Advances in NeurIPS},\n  year={2025},\n  url={https://arxiv.org/abs/2502.08924}\n}\n\n@inproceedings{zawalski2026codec,\n  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},\n  author={Zawalski, Micha{\\l} and Boubdir, Meriem and Ba{\\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},\n  booktitle={Proceedings of ICLR},\n  year={2026},\n  url={https://arxiv.org/abs/2510.27055}\n}\n\n@article{gambetta2025surplexity,\n  title={Learning by Surprise: Surplexity for Mitigating Model Collapse},\n  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},\n  journal={arXiv preprint arXiv:2410.12341},\n  year={2025},\n  url={https://arxiv.org/abs/2410.12341}\n}\n\n@inproceedings{zhang2024minkpp,\n  title={Min-{K}\\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},\n  booktitle={Proceedings of EMNLP},\n  year={2024}\n}\n\n@article{shumailov2024collapse,\n  title={{AI} Models Collapse When Trained on Recursively Generated Data},\n  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal={Nature},\n  year={2024}\n}\n\n@inproceedings{alemohammad2024selfconsuming,\n  title={Self-Consuming Generative Models Go {MAD}},\n  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luber, Lorenzo and Babaei, Ahmed Imtiaz and Letizia, Daniel and Bastani, Osbert and Baraniuk, Richard},\n  booktitle={Proceedings of ICLR},\n  year={2024}\n}\n\n@inproceedings{dohmatob2024model,\n  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n@inproceedings{xie2023dsir,\n  title={Data Selection with Importance Resampling},\n  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n@inproceedings{tirumala2023d4,\n  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},\n  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},\n  booktitle={Advances in NeurIPS},\n  year={2023}\n}\n\n@inproceedings{xie2023doremi,\n  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},\n  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},\n  booktitle={Advances in NeurIPS},\n  year={2023}\n}\n\n@inproceedings{kirchenbauer2023watermark,\n  title={A Watermark for Large Language Models},\n  author={Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n@inproceedings{gehrmann2019gltr,\n  title={{GLTR}: Statistical Detection and Visualization of Generated Text},\n  author={Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  booktitle={Proceedings of ACL: System Demonstrations},\n  year={2019}\n}\n\n@inproceedings{hans2024binoculars,\n  title={Spotting {LLMs} With Binoculars},\n  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n@article{cao2020coral,\n  title={Rank consistent ordinal regression for neural networks with application to age estimation},\n  author={Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  journal={Pattern Recognition Letters},\n  volume={140},\n  pages={325--331},\n  year={2020}\n}\n\n@inproceedings{zellers2019grover,\n  title={Defending Against Neural Fake News},\n  author={Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},\n  booktitle={Advances in NeurIPS},\n  year={2019}\n}\n\n@inproceedings{ippolito2020detection,\n  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},\n  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},\n  booktitle={Proceedings of ACL},\n  year={2020}\n}\n",
      "numLines": 172,
      "startLine": 1,
      "totalLines": 172
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context. Let me:

1. Add a new "Probing Classifiers" paragraph after the "Ordinal Classification" paragraph
2. Add Frank & Hall to the Ordinal Classification paragraph
3. Add the needed bib entries to references.bib

Let me make the edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "aa7e10d7-8a1f-44bd-83a2-24903145fd1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToaqqCCCbiymouV35U76qN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5054,
      "cache_read_input_tokens": 27182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5054
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

_source line 23_

Now I have the full picture. Let me make all three edits: (1) add probing classifiers paragraph, (2) supplement ordinal classification with Frank & Hall, (3) add bib entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "937a1b67-0e9f-4038-92ba-68ea68810354",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToaqqCCCbiymouV35U76qN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5054,
      "cache_read_input_tokens": 27182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5054
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Wps1A6JNCtzLkVF1PjUKwr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
  "old_string": "Our Ordinal Boundary Detection (OBD) head leverages this ordered structure, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.\n\n\\paragraph{Data Selection and Curation.}",
  "new_string": "The idea of decomposing ordinal problems into a series of binary decisions dates to Frank \\& Hall~\\cite{frank2001ordinal}; our Ordinal Boundary Detection (OBD) head follows this principle by learning $K\\!-\\!1$ cumulative boundary classifiers, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.\n\n\\paragraph{Probing Classifiers.}\nLinear and shallow MLP probes have become a standard tool for analyzing what information is encoded in pretrained representations~\\cite{alain2017understanding,conneau2018probing}.\nBelinkov~\\cite{belinkov2022probing} surveys the methodology and cautions that probe complexity must be controlled to ensure that performance reflects representational content rather than probe capacity.\nOur neural probe experiment follows this protocol: a two-layer MLP on frozen Qwen2.5-1.5B embeddings, where the probe's limited capacity ensures that discriminability reflects depth information already present in the representations rather than learned de novo.\n\n\\paragraph{Data Selection and Curation.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "96a5ea0b-57f7-4a0d-a64f-2ad033cb0e67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToaqqCCCbiymouV35U76qN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5054,
      "cache_read_input_tokens": 27182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5054
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

_source line 25 · 2026-05-14T04:56:02.445Z_

<details><summary>↩ Tool result · `toolu_01Wps1A6JNCtzLkVF1PjUKwr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "0cc9de39-6074-4ae0-bc5a-cfa0a1cf8213",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
    "oldString": "Our Ordinal Boundary Detection (OBD) head leverages this ordered structure, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.\n\n\\paragraph{Data Selection and Curation.}",
    "newString": "The idea of decomposing ordinal problems into a series of binary decisions dates to Frank \\& Hall~\\cite{frank2001ordinal}; our Ordinal Boundary Detection (OBD) head follows this principle by learning $K\\!-\\!1$ cumulative boundary classifiers, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.\n\n\\paragraph{Probing Classifiers.}\nLinear and shallow MLP probes have become a standard tool for analyzing what information is encoded in pretrained representations~\\cite{alain2017understanding,conneau2018probing}.\nBelinkov~\\cite{belinkov2022probing} surveys the methodology and cautions that probe complexity must be controlled to ensure that performance reflects representational content rather than probe capacity.\nOur neural probe experiment follows this protocol: a two-layer MLP on frozen Qwen2.5-1.5B embeddings, where the probe's limited capacity ensures that discriminability reflects depth information already present in the representations rather than learned de novo.\n\n\\paragraph{Data Selection and Curation.}",
    "originalFile": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Model Collapse and Recursive Generation.}\nTraining on model-generated data can cause progressive distribution shift known as \\emph{model collapse}.\nShumailov et al.~\\cite{shumailov2024collapse} showed that iteratively training language models on their own outputs leads to irreversible tail-distribution degradation, with minority modes vanishing across generations.\nAlemohammad et al.~\\cite{alemohammad2024selfconsuming} formalized this for self-consuming generative models, proving convergence to a fixed point under mild regularity conditions.\nDohmatob et al.~\\cite{dohmatob2024model} derived scaling laws for collapse, demonstrating that tail probability mass is lost at rates predictable from model and data scale.\nSchaeffer et al.~\\cite{schaeffer2025position} organized the fragmented literature into a taxonomy of eight definitions across three families.\nOur $\\Kstar$ aligns with their Family~B (distributional deformation), specifically D4 (collapsing variance) and D6 (mode entanglement)---the features that degrade most rapidly in our experiments are precisely variance-based surprisal measures.\nKazdan et al.~\\cite{kazdan2025collapse} distinguished \\emph{replace} and \\emph{accumulate} regimes: in the replace regime each generation completely supplants its predecessor, producing faster collapse.\nOur prompt-chain protocol operates in the replace regime, so $\\Kempirical = 2$ is a conservative lower bound; the accumulate regime would yield slower degradation and higher $\\Kstar$.\nShi et al.~\\cite{shi2025generalization} identified a generalization-to-memorization transition in recursively trained models, providing cross-modal evidence that information loss is progressive.\nThese works characterize the macro dynamics of collapse but do not provide tools for per-text generational depth estimation.\n\n\\paragraph{Binary Synthetic Text Detection.}\nDistinguishing machine-generated from human-written text is a well-studied binary classification problem.\nEarly statistical approaches such as GLTR~\\cite{gehrmann2019gltr} visualized per-token likelihood ranks to help human annotators spot generated text, establishing that token-level distributional cues are informative for detection.\nZellers et al.~\\cite{zellers2019grover} demonstrated that the generating model itself is an effective detector, while Ippolito et al.~\\cite{ippolito2020detection} analyzed how detection difficulty scales with generation quality.\nRecent zero-shot methods have narrowed the gap: Mitchell et al.~\\cite{mitchell2023detectgpt} introduced DetectGPT, which uses probability curvature to detect machine-generated text without access to the generating model.\nHans et al.~\\cite{hans2024binoculars} proposed Binoculars, which computes the cross-perplexity ratio between two closely related language models to achieve near-perfect detection without any training data.\nDivEye~\\cite{basani2026diveye} uses surprisal diversity features to detect synthetic text without generator-specific training data, and Min-K\\%++~\\cite{zhang2024minkpp} adapts membership inference techniques to flag model-generated passages via outlier token likelihoods.\nCoDeC~\\cite{zawalski2026codec} frames contamination detection as in-context learning, calibrating thresholds from few-shot exemplars.\n\nAll these methods produce binary outputs and do not distinguish generational depth.\nThe connection to membership inference is instructive: Min-K\\%++ and related approaches test whether a text appeared in training data---a related but distinct question from how many recursive generation steps it has undergone.\nA further limitation is that binary detectors cannot separate beneficial recursive generation (e.g., self-refinement, where a model iteratively improves its own output) from harmful recursive contamination, creating systematic false positives when applied to curated synthetic data.\nBinary features are designed for the human-vs.-synthetic boundary and are not expected to capture fine-grained depth differences, as the distributional shift between adjacent generations is orders of magnitude smaller than the shift between human and first-generation text.\n\n\\paragraph{Ordinal Classification.}\nOrdinal regression methods exploit the natural ordering among class labels to improve generalization over nominal classifiers.\nCao et al.~\\cite{cao2020coral} introduced CORAL, which enforces rank consistency through weight sharing in the output layer, guaranteeing that predicted cumulative probabilities are monotonically non-increasing.\nOrdinal approaches have been applied in NLP tasks such as sentiment intensity prediction and essay scoring, where adjacent categories share more semantic overlap than distant ones.\nGenerational depth exhibits the same ordinal structure: text at depth~$k$ is distributionally closer to depth~$k\\!\\pm\\!1$ than to depth~$k\\!\\pm\\!3$, because each recursive generation step introduces an incremental distributional shift rather than a discontinuous one.\nDespite this natural fit, ordinal classification has not been applied to synthetic text depth estimation.\nOur Ordinal Boundary Detection (OBD) head leverages this ordered structure, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.\n\n\\paragraph{Data Selection and Curation.}\nPrincipled data selection methods improve training corpus quality through distribution matching and deduplication.\nDSIR~\\cite{xie2023dsir} selects pretraining data by importance resampling against a target distribution.\nD4~\\cite{tirumala2023d4} combines deduplication with diversification to reduce redundancy, and DoReMi~\\cite{xie2023doremi} learns domain weights via a proxy model to optimize downstream performance.\nThese methods operate on distributional properties of the corpus but do not estimate whether individual documents have undergone recursive generation.\n\nThe closest prior work is Drayson et al.~\\cite{drayson2025}, who combined binary machine-generated text detection with stratified importance resampling (SIR) to filter synthetic content and prevent model collapse.\nTheir approach is a special case of our graduated filtering framework: when $\\Kstar = 1$, ordinal depth estimation reduces to binary classification, and depth-aware curation degenerates to their SIR-based scheme.\nWe generalize this binary formulation to ordinal depth estimation, enabling finer-grained curation that preserves mildly contaminated text (depth~1, retaining most original signal) while removing deeply corrupted text (depth~$\\geq 3$).\nAmin et al.~\\cite{amin2025escaping} demonstrated that even weak quality signals suffice to escape model collapse when applied iteratively, suggesting that approximate depth estimates beyond $\\Kempirical$ may remain practically useful.\nGambetta et al.~\\cite{gambetta2025surplexity} proposed surplexity as a text quality metric correlated with generative degradation, though without explicit depth calibration.\n\n\\paragraph{Watermarking and Provenance.}\nAn alternative approach embeds identifiers at generation time.\nKirchenbauer et al.~\\cite{kirchenbauer2023watermark} proposed statistical watermarking for LLM outputs by partitioning the vocabulary into green and red token lists conditioned on preceding context.\nWatermarking is complementary to depth estimation: it requires control over the generation process and cooperation from providers, whereas our method operates post-hoc on unwatermarked text.\nThe two approaches address different threat models---watermarking assumes a cooperative generator, while depth estimation targets uncontrolled settings where provenance metadata is unavailable.",
    "structuredPatch": [
      {
        "oldStart": 33,
        "oldLines": 8,
        "newStart": 33,
        "newLines": 13,
        "lines": [
          " Ordinal approaches have been applied in NLP tasks such as sentiment intensity prediction and essay scoring, where adjacent categories share more semantic overlap than distant ones.",
          " Generational depth exhibits the same ordinal structure: text at depth~$k$ is distributionally closer to depth~$k\\!\\pm\\!1$ than to depth~$k\\!\\pm\\!3$, because each recursive generation step introduces an incremental distributional shift rather than a discontinuous one.",
          " Despite this natural fit, ordinal classification has not been applied to synthetic text depth estimation.",
          "-Our Ordinal Boundary Detection (OBD) head leverages this ordered structure, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.",
          "+The idea of decomposing ordinal problems into a series of binary decisions dates to Frank \\& Hall~\\cite{frank2001ordinal}; our Ordinal Boundary Detection (OBD) head follows this principle by learning $K\\!-\\!1$ cumulative boundary classifiers, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.",
          " ",
          "+\\paragraph{Probing Classifiers.}",
          "+Linear and shallow MLP probes have become a standard tool for analyzing what information is encoded in pretrained representations~\\cite{alain2017understanding,conneau2018probing}.",
          "+Belinkov~\\cite{belinkov2022probing} surveys the methodology and cautions that probe complexity must be controlled to ensure that performance reflects representational content rather than probe capacity.",
          "+Our neural probe experiment follows this protocol: a two-layer MLP on frozen Qwen2.5-1.5B embeddings, where the probe's limited capacity ensures that discriminability reflects depth information already present in the representations rather than learned de novo.",
          "+",
          " \\paragraph{Data Selection and Curation.}",
          " Principled data selection methods improve training corpus quality through distribution matching and deduplication.",
          " DSIR~\\cite{xie2023dsir} selects pretraining data by importance resampling against a target distribution."
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

_source line 26_

Now add the bib entries for all four new references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "43100271-5fce-4090-a5d6-ae1782ef8a6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fnu6xczkcC31NQtz7zaVr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 621,
      "cache_read_input_tokens": 32236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 621
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

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_015Lg51NQGVpDCFT454rbMRq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
  "old_string": "@inproceedings{ippolito2020detection,\n  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},\n  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},\n  booktitle={Proceedings of ACL},\n  year={2020}\n}",
  "new_string": "@inproceedings{ippolito2020detection,\n  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},\n  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},\n  booktitle={Proceedings of ACL},\n  year={2020}\n}\n\n% === Probing Classifiers ===\n\n@article{alain2017understanding,\n  title={Understanding Intermediate Layers Using Linear Classifier Probes},\n  author={Alain, Guillaume and Bengio, Yoshua},\n  journal={arXiv preprint arXiv:1610.01644},\n  year={2017}\n}\n\n@inproceedings{conneau2018probing,\n  title={What You Can Cram into a Single \\$\\&!\\#* Vector: Probing Sentence Embeddings for Linguistic Properties},\n  author={Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo{\\\"\\i}c and Baroni, Marco},\n  booktitle={Proceedings of ACL},\n  year={2018}\n}\n\n@article{belinkov2022probing,\n  title={Probing Classifiers: Promises, Shortcomings, and Advances},\n  author={Belinkov, Yonatan},\n  journal={Computational Linguistics},\n  volume={48},\n  number={1},\n  pages={207--219},\n  year={2022}\n}\n\n% === Ordinal Classification (additional) ===\n\n@inproceedings{frank2001ordinal,\n  title={A Simple Approach to Ordinal Classification},\n  author={Frank, Eibe and Hall, Mark},\n  booktitle={Proceedings of ECML},\n  pages={145--156},\n  year={2001}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "1df8ff94-2fda-4e8a-91a5-8a779134850e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fnu6xczkcC31NQtz7zaVr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 621,
      "cache_read_input_tokens": 32236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 621
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

_source line 28 · 2026-05-14T04:56:13.003Z_

<details><summary>↩ Tool result · `toolu_015Lg51NQGVpDCFT454rbMRq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "aaaf13cc-246d-43f9-a622-bb17901557ce",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
    "oldString": "@inproceedings{ippolito2020detection,\n  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},\n  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},\n  booktitle={Proceedings of ACL},\n  year={2020}\n}",
    "newString": "@inproceedings{ippolito2020detection,\n  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},\n  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},\n  booktitle={Proceedings of ACL},\n  year={2020}\n}\n\n% === Probing Classifiers ===\n\n@article{alain2017understanding,\n  title={Understanding Intermediate Layers Using Linear Classifier Probes},\n  author={Alain, Guillaume and Bengio, Yoshua},\n  journal={arXiv preprint arXiv:1610.01644},\n  year={2017}\n}\n\n@inproceedings{conneau2018probing,\n  title={What You Can Cram into a Single \\$\\&!\\#* Vector: Probing Sentence Embeddings for Linguistic Properties},\n  author={Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo{\\\"\\i}c and Baroni, Marco},\n  booktitle={Proceedings of ACL},\n  year={2018}\n}\n\n@article{belinkov2022probing,\n  title={Probing Classifiers: Promises, Shortcomings, and Advances},\n  author={Belinkov, Yonatan},\n  journal={Computational Linguistics},\n  volume={48},\n  number={1},\n  pages={207--219},\n  year={2022}\n}\n\n% === Ordinal Classification (additional) ===\n\n@inproceedings{frank2001ordinal,\n  title={A Simple Approach to Ordinal Classification},\n  author={Frank, Eibe and Hall, Mark},\n  booktitle={Proceedings of ECML},\n  pages={145--156},\n  year={2001}\n}",
    "originalFile": "% === References for gen-depth-contamination ===\n% Source: literature_map.yaml — verified 2026-05-14\n\n% === Must-Cite ===\n\n@inproceedings{drayson2025,\n  title={Machine-Generated Text Detection Prevents Language Model Collapse},\n  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  booktitle={Proceedings of EMNLP},\n  year={2025},\n  url={https://arxiv.org/abs/2502.15654}\n}\n\n@inproceedings{schaeffer2025position,\n  title={Position: Model Collapse Does Not Mean What You Think},\n  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2503.03150}\n}\n\n@inproceedings{kazdan2025collapse,\n  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\n  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2410.16713}\n}\n\n@inproceedings{shi2025generalization,\n  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},\n  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  booktitle={Advances in NeurIPS},\n  year={2025},\n  note={Spotlight},\n  url={https://arxiv.org/abs/2509.16499}\n}\n\n@inproceedings{mitchell2023detectgpt,\n  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\n  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n% === Should-Cite ===\n\n@article{basani2026diveye,\n  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},\n  author={Basani, Advik Raj and Chen, Pin-Yu},\n  journal={Transactions on Machine Learning Research},\n  year={2026},\n  url={https://arxiv.org/abs/2509.18880}\n}\n\n@inproceedings{amin2025escaping,\n  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},\n  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},\n  booktitle={Advances in NeurIPS},\n  year={2025},\n  url={https://arxiv.org/abs/2502.08924}\n}\n\n@inproceedings{zawalski2026codec,\n  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},\n  author={Zawalski, Micha{\\l} and Boubdir, Meriem and Ba{\\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},\n  booktitle={Proceedings of ICLR},\n  year={2026},\n  url={https://arxiv.org/abs/2510.27055}\n}\n\n@article{gambetta2025surplexity,\n  title={Learning by Surprise: Surplexity for Mitigating Model Collapse},\n  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},\n  journal={arXiv preprint arXiv:2410.12341},\n  year={2025},\n  url={https://arxiv.org/abs/2410.12341}\n}\n\n@inproceedings{zhang2024minkpp,\n  title={Min-{K}\\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},\n  booktitle={Proceedings of EMNLP},\n  year={2024}\n}\n\n@article{shumailov2024collapse,\n  title={{AI} Models Collapse When Trained on Recursively Generated Data},\n  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal={Nature},\n  year={2024}\n}\n\n@inproceedings{alemohammad2024selfconsuming,\n  title={Self-Consuming Generative Models Go {MAD}},\n  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luber, Lorenzo and Babaei, Ahmed Imtiaz and Letizia, Daniel and Bastani, Osbert and Baraniuk, Richard},\n  booktitle={Proceedings of ICLR},\n  year={2024}\n}\n\n@inproceedings{dohmatob2024model,\n  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n@inproceedings{xie2023dsir,\n  title={Data Selection with Importance Resampling},\n  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n@inproceedings{tirumala2023d4,\n  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},\n  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},\n  booktitle={Advances in NeurIPS},\n  year={2023}\n}\n\n@inproceedings{xie2023doremi,\n  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},\n  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},\n  booktitle={Advances in NeurIPS},\n  year={2023}\n}\n\n@inproceedings{kirchenbauer2023watermark,\n  title={A Watermark for Large Language Models},\n  author={Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n@inproceedings{gehrmann2019gltr,\n  title={{GLTR}: Statistical Detection and Visualization of Generated Text},\n  author={Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  booktitle={Proceedings of ACL: System Demonstrations},\n  year={2019}\n}\n\n@inproceedings{hans2024binoculars,\n  title={Spotting {LLMs} With Binoculars},\n  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n@article{cao2020coral,\n  title={Rank consistent ordinal regression for neural networks with application to age estimation},\n  author={Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  journal={Pattern Recognition Letters},\n  volume={140},\n  pages={325--331},\n  year={2020}\n}\n\n@inproceedings{zellers2019grover,\n  title={Defending Against Neural Fake News},\n  author={Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},\n  booktitle={Advances in NeurIPS},\n  year={2019}\n}\n\n@inproceedings{ippolito2020detection,\n  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},\n  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},\n  booktitle={Proceedings of ACL},\n  year={2020}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 169,
        "oldLines": 3,
        "newStart": 169,
        "newLines": 39,
        "lines": [
          "   booktitle={Proceedings of ACL},",
          "   year={2020}",
          " }",
          "+",
          "+% === Probing Classifiers ===",
          "+",
          "+@article{alain2017understanding,",
          "+  title={Understanding Intermediate Layers Using Linear Classifier Probes},",
          "+  author={Alain, Guillaume and Bengio, Yoshua},",
          "+  journal={arXiv preprint arXiv:1610.01644},",
          "+  year={2017}",
          "+}",
          "+",
          "+@inproceedings{conneau2018probing,",
          "+  title={What You Can Cram into a Single \\$\\&!\\#* Vector: Probing Sentence Embeddings for Linguistic Properties},",
          "+  author={Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo{\\\"\\i}c and Baroni, Marco},",
          "+  booktitle={Proceedings of ACL},",
          "+  year={2018}",
          "+}",
          "+",
          "+@article{belinkov2022probing,",
          "+  title={Probing Classifiers: Promises, Shortcomings, and Advances},",
          "+  author={Belinkov, Yonatan},",
          "+  journal={Computational Linguistics},",
          "+  volume={48},",
          "+  number={1},",
          "+  pages={207--219},",
          "+  year={2022}",
          "+}",
          "+",
          "+% === Ordinal Classification (additional) ===",
          "+",
          "+@inproceedings{frank2001ordinal,",
          "+  title={A Simple Approach to Ordinal Classification},",
          "+  author={Frank, Eibe and Hall, Mark},",
          "+  booktitle={Proceedings of ECML},",
          "+  pages={145--156},",
          "+  year={2001}",
          "+}"
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

修改完成。摘要：

**related_work.tex**:
- **Ordinal Classification 段落**：将原来独立引用 CORAL 的结尾句改写，加入 Frank & Hall (2001) 作为 ordinal-to-binary decomposition 的开创性工作，并将 OBD head 的设计与之关联
- **新增 Probing Classifiers 段落**（3 句，位于 Ordinal Classification 和 Data Selection 之间）：引用 Alain & Bengio (2017)、Conneau et al. (2018)、Belinkov (2022)，说明 neural probe 实验遵循该范式，probe 的有限容量确保可区分性来自表征本身而非 probe 学到的新信息

**references.bib**：新增 4 条 bib entry — `alain2017understanding`、`conneau2018probing`、`belinkov2022probing`、`frank2001ordinal`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "uuid": "411de4ec-4d61-4844-8433-a513e3f1f1d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R87reBPGXRxHSMq1vZoXVe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 763,
      "cache_read_input_tokens": 32857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 763
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

修改完成。摘要：

**related_work.tex**:
- **Ordinal Classification 段落**：将原来独立引用 CORAL 的结尾句改写，加入 Frank & Hall (2001) 作为 ordinal-to-binary decomposition 的开创性工作，并将 OBD head 的设计与之关联
- **新增 Probing Classifiers 段落**（3 句，位于 Ordinal Classification 和 Data Selection 之间）：引用 Alain & Bengio (2017)、Conneau et al. (2018)、Belinkov (2022)，说明 neural probe 实验遵循该范式，probe 的有限容量确保可区分性来自表征本身而非 probe 学到的新信息

**references.bib**：新增 4 条 bib entry — `alain2017understanding`、`conneau2018probing`、`belinkov2022probing`、`frank2001ordinal`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 53433,
  "duration_api_ms": 54265,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "f20a9cc0-7216-48a9-baa4-62da05b14ca8",
  "total_cost_usd": 0.26910775000000003,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 21779,
    "cache_read_input_tokens": 153916,
    "output_tokens": 2190,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21779,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 268,
        "cache_read_input_tokens": 32857,
        "cache_creation_input_tokens": 763,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 763
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1161,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001246,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 2190,
      "cacheReadInputTokens": 153916,
      "cacheCreationInputTokens": 21779,
      "webSearchRequests": 0,
      "costUSD": 0.26786175,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c43dc5d8-17fb-4052-8bc3-63c7dc0fae44"
}
```

</details>

---
