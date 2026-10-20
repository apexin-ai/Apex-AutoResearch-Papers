# Research conversation: Find and read the file `related_work_audit.md` in the gen-depth-contamination project artifacts. Try these paths: 1. /ho

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a57f8c15b4346ee2a.jsonl`
- **Structured JSON:** [`9254e52c9bc22643ff83.json`](../../sessions/92/9254e52c9bc22643ff83.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

7 recorded events

### User

_source line 1 · 2026-05-14T04:55:54.364Z_

Find and read the file `related_work_audit.md` in the gen-depth-contamination project artifacts. Try these paths:
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/drafts/related_work_audit.md
2. Search for it with glob pattern **/related_work_audit.md under /home/ubuntu/.agent-ml-research-idea_gen_0509_7/

Return the full contents of the file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ff4326eb-858e-4d8f-8394-35754b67796b",
  "agentId": "a57f8c15b4346ee2a",
  "type": "user",
  "uuid": "cce7433c-e456-4dec-a569-e2cd48bae41e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/agent_2bb8bf55",
  "sessionId": "2345b0b3-4f5a-4de3-8cea-15ee8dd4dc18",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-14T04:55:56.531Z_

I'll search for the `related_work_audit.md` file using the paths you specified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cce7433c-e456-4dec-a569-e2cd48bae41e",
  "isSidechain": true,
  "agentId": "a57f8c15b4346ee2a",
  "requestId": "req_011Cb1sChA6uFW2A6rdACYF2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e4a7262b-8f32-4158-b344-2d515c402a0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/agent_2bb8bf55",
  "sessionId": "2345b0b3-4f5a-4de3-8cea-15ee8dd4dc18",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WUZ7iYKRngMApjBmSh8AjQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32149,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32149,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T04:55:56.784Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P3PXvbtW2CUECbxoCjrMYo`</summary>

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
  "parentUuid": "e4a7262b-8f32-4158-b344-2d515c402a0e",
  "isSidechain": true,
  "agentId": "a57f8c15b4346ee2a",
  "requestId": "req_011Cb1sChA6uFW2A6rdACYF2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "01cd9806-b6e6-4009-85af-2e33691cd535",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/agent_2bb8bf55",
  "sessionId": "2345b0b3-4f5a-4de3-8cea-15ee8dd4dc18",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WUZ7iYKRngMApjBmSh8AjQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32149,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32149,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T04:55:56.811Z_

<details><summary>↩ Tool result · `toolu_01P3PXvbtW2CUECbxoCjrMYo`</summary>

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
  "parentUuid": "01cd9806-b6e6-4009-85af-2e33691cd535",
  "isSidechain": true,
  "promptId": "ff4326eb-858e-4d8f-8394-35754b67796b",
  "agentId": "a57f8c15b4346ee2a",
  "type": "user",
  "uuid": "a9ec8af9-75e3-4333-b70c-306763e70767",
  "sourceToolAssistantUUID": "01cd9806-b6e6-4009-85af-2e33691cd535",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/agent_2bb8bf55",
  "sessionId": "2345b0b3-4f5a-4de3-8cea-15ee8dd4dc18",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T04:55:56.970Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TsnJY1W1FsAuuR8xQ5DPpr`</summary>

```json
{
  "pattern": "**/related_work_audit.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9ec8af9-75e3-4333-b70c-306763e70767",
  "isSidechain": true,
  "agentId": "a57f8c15b4346ee2a",
  "requestId": "req_011Cb1sChA6uFW2A6rdACYF2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "42996048-8188-46a4-adb1-db7f397e51fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/agent_2bb8bf55",
  "sessionId": "2345b0b3-4f5a-4de3-8cea-15ee8dd4dc18",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WUZ7iYKRngMApjBmSh8AjQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32149,
      "cache_read_input_tokens": 0,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 32149
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 194,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 32149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 32149,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T04:55:56.997Z_

<details><summary>↩ Tool result · `toolu_01TsnJY1W1FsAuuR8xQ5DPpr`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/drafts/related_work_audit.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42996048-8188-46a4-adb1-db7f397e51fc",
  "isSidechain": true,
  "promptId": "ff4326eb-858e-4d8f-8394-35754b67796b",
  "agentId": "a57f8c15b4346ee2a",
  "type": "user",
  "uuid": "c26ac2a3-f66e-49bb-9a49-4f235e18f7ed",
  "sourceToolAssistantUUID": "42996048-8188-46a4-adb1-db7f397e51fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/agent_2bb8bf55",
  "sessionId": "2345b0b3-4f5a-4de3-8cea-15ee8dd4dc18",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-14T04:56:28.130Z_

Perfect! I found the file at the first path. Here is the full contents of `related_work_audit.md`:

---

## Related Work 完整性审查

**审查日期**: 2026-05-14
**审查范围**: `related_work.tex` (54行, 5个段落)

### 已覆盖

**Model Collapse and Recursive Generation**
- Shumailov et al. (2024, Nature): line 6, tail-distribution degradation
- Alemohammad et al. (2024, ICLR): line 7, self-consuming models, fixed point convergence
- Dohmatob et al. (2024, ICML): line 8, scaling laws for tail loss
- Schaeffer et al. (2025, ICML): line 9-10, 8-definition taxonomy, K* 与 Family B 对齐
- Kazdan et al. (2025, ICML): line 11-12, replace vs accumulate regimes
- Shi et al. (2025, NeurIPS Spotlight): line 13, generalization-to-memorization transition
- Amin et al. (2025, NeurIPS): line 47, weak signals suffice to escape collapse
- Gambetta et al. (2025): line 48, surplexity metric

**Binary Synthetic Text Detection**
- GLTR (Gehrmann et al. 2019): line 18, token-level likelihood visualization
- Grover (Zellers et al. 2019): line 19, generator-as-detector
- Ippolito et al. (2020): line 19, detection difficulty vs generation quality
- DetectGPT (Mitchell et al. 2023): line 20, probability curvature
- Binoculars (Hans et al. 2024): line 21, cross-perplexity ratio
- DivEye (Basani et al. 2026): line 22, surprisal diversity
- Min-K%++ (Zhang et al. 2024): line 22, outlier token likelihoods
- CoDeC (Zawalski et al. 2026): line 23, in-context learning contamination detection

**Ordinal Classification**
- CORAL (Cao et al. 2020): line 32-33, rank-consistent ordinal regression

**Data Selection and Curation**
- DSIR (Xie et al. 2023): line 40, importance resampling
- D4 (Tirumala et al. 2023): line 41, deduplication + diversification
- DoReMi (Xie et al. 2023): line 41, domain weight optimization
- Drayson et al. (2025): line 44-46, binary detection + SIR (positioned as special case of our framework)

**Watermarking**
- Kirchenbauer et al. (2023): line 52-53, statistical watermarking

### 需要补充

#### 1. [高优先] Probing Classifiers 文献 — 支撑 Neural Probe 实验

**Gap**: discussion.tex (lines 29-35, 123-129) 和 conclusion.tex (line 45) 大量讨论 frozen-encoder + MLP probe 实验，但 Related Work 中完全没有 probing classifiers 的文献支撑。审稿人会质疑方法选择的依据。

**建议**: 在 Ordinal Classification 段落之后新增一个段落，或在 Ordinal Classification 段末追加 2-3 句。

**需要引用**:
- Alain & Bengio (2017), "Understanding intermediate layers using linear classifier probes" — 提出用线性探针分析网络中间表征，是 frozen-encoder probing 的方法论基础
- Conneau et al. (2018), "What you can cram into a single $&!#* vector: Probing sentence embeddings for linguistic properties" (ACL) — 系统研究 sentence embedding 编码了哪些语言学属性
- Belinkov (2022), "Probing Classifiers: Promises, Shortcomings, and Advances" (CL) — probing 方法的综述，讨论了 probe 复杂度与结论有效性的权衡

**建议文本**:

> \paragraph{Probing Classifiers.}
> Linear and shallow MLP probes have become a standard tool for analyzing what information is encoded in pretrained representations~\cite{alain2017understanding,conneau2018probing}.
> Belinkov~\cite{belinkov2022probing} surveys the methodology and cautions that probe complexity must be controlled to ensure that performance reflects representational content rather than probe capacity.
> Our neural probe experiment follows this protocol: a two-layer MLP on frozen Qwen2.5-1.5B embeddings, where the probe's limited capacity ensures that discriminability reflects information present in the representations rather than learned de novo.

#### 2. [中优先] Fast-DetectGPT — Binary Detection 段落补充

**Gap**: DetectGPT 已引用，但其改进版 Fast-DetectGPT 在 2024 年成为 zero-shot 检测的新 SOTA，被广泛引用。

**建议**: 在 line 20 (DetectGPT 之后) 追加一句。

**需要引用**:
- Bao et al. (2024), "Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature" (ICLR 2024)

**建议文本**: 在 Mitchell et al. 句后加:

> Bao et al.~\cite{bao2024fastdetectgpt} improved efficiency by replacing perturbation sampling with conditional probability curvature, achieving comparable accuracy with orders-of-magnitude speedup.

#### 3. [中优先] Gerstgrasser et al. (2024) — Model Collapse 理论补充

**Gap**: 现有 model collapse 覆盖全面，但缺少 Gerstgrasser et al. 关于 collapse 可避免条件的理论分析。该工作与本文的 data curation 动机直接相关——他们证明保留足够的原始数据可以避免 collapse，本文的 depth-aware filtering 正是实现这一点的工具。

**建议**: 在 line 13 (Shi et al.) 之后追加一句。

**需要引用**:
- Gerstgrasser et al. (2024), "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" (arXiv 2404.01413)

**建议文本**:

> Gerstgrasser et al.~\cite{gerstgrasser2024inevitable} proved that collapse is avoidable when sufficient original data is retained alongside synthetic samples, a condition that depth-aware curation can enforce by construction.

#### 4. [低-中优先] Ordinal Classification 补充

**Gap**: 仅引用 CORAL 一篇。Ordinal classification 是本文方法的核心组件（OBD head），仅一篇引用显得单薄。

**建议**: 在 CORAL 引用后追加 1-2 篇经典方法。

**需要引用**:
- Frank & Hall (2001), "A Simple Approach to Ordinal Classification" (ECML) — 将 ordinal 问题分解为一系列二分类的开创性工作，与 OBD head 的 boundary detection 思路直接对应
- Diaz & Marathe (2019), "Soft Labels for Ordinal Regression" (CVPR) — soft label 方法，与 OBD 的 monotonic probability 设计相关

**建议文本**: 在 line 33 CORAL 句后追加:

> The idea of decomposing ordinal problems into a series of binary decisions dates to Frank \& Hall~\cite{frank2001ordinal}; our OBD head follows this principle by learning $K\!-\!1$ cumulative boundary classifiers.

### 可选改进

#### 1. Self-Refinement 文献补充

**理由**: Related Work line 27 提到 "beneficial recursive generation (e.g., self-refinement)" 但没有引用。添加一篇可以增强论点。

**建议引用**: Madaan et al. (2023), "Self-Refine: Iterative Refinement with Self-Feedback" (NeurIPS 2023)

**位置**: line 27, 将 "self-refinement" 处加引用即可。

#### 2. Trained/Fine-tuned 检测器覆盖

**理由**: Binary Detection 段落偏重 zero-shot 和 statistical 方法。如有 fine-tuned detector 的工作（如 OpenAI text classifier, Ghostbuster），可以在 line 19 附近用一句话覆盖 supervised 检测方向，说明本文的 ordinal approach 与之的关系。但这不是必须的，因为本文聚焦 post-hoc 无训练数据场景。

#### 3. Multi-class AI Text Attribution

**理由**: 有一些工作不只做二分类，而是区分不同 LLM 生成的文本（source attribution）。与本文的 ordinal depth 不同但相关。如果空间允许可以提一句以示区分。

**建议引用**: Uchendu et al. (2020), "Authorship Attribution for Neural Text Generation" (EMNLP)

#### 4. Data Contamination (Benchmark) 文献

**理由**: CoDeC 已覆盖 benchmark contamination detection，但该方向有更多工作（Golchin & Surdeanu 2024, Oren et al. 2024）。不过本文的 "contamination" 指 recursive generation contamination 而非 benchmark data leakage，过多引用可能造成混淆。现有覆盖已足够。

### 总结

| 类别 | 状态 | 行动 |
|------|------|------|
| Model collapse | ✅ 充分 | 可选补 Gerstgrasser (collapse avoidability) |
| Binary detection | ✅ 充分 | 可选补 Fast-DetectGPT |
| Ordinal classification | ⚠️ 偏薄 | 建议补 Frank & Hall |
| Data selection | ✅ 充分 | 无需补充 |
| Watermarking | ✅ 充分 | 无需补充 |
| **Probing classifiers** | ❌ **缺失** | **必须补充** — neural probe 实验缺文献支撑 |

**最高优先级**: 补充 Probing Classifiers 段落（Alain & Bengio 2017, Conneau et al. 2018, Belinkov 2022），直接支撑 discussion.tex 中的 neural probe 实验设计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c26ac2a3-f66e-49bb-9a49-4f235e18f7ed",
  "isSidechain": true,
  "agentId": "a57f8c15b4346ee2a",
  "requestId": "req_011Cb1sCtG6MY1ttVvUtB9dP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f7786a6b-f1e7-47d4-8064-b06cd1506898",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/agent_2bb8bf55",
  "sessionId": "2345b0b3-4f5a-4de3-8cea-15ee8dd4dc18",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019wETCnYDso2LbyTr4hzE67",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4293,
      "cache_read_input_tokens": 32149,
      "output_tokens": 2857,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4293
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2857,
          "cache_read_input_tokens": 32149,
          "cache_creation_input_tokens": 4293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4293,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
