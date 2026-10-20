# Research conversation: Read the following files and return their full contents: 1. /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/str

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 8
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aa8359aeff3f5958a.jsonl`
- **Structured JSON:** [`5862d0859c53c76b5183.json`](../../sessions/58/5862d0859c53c76b5183.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

8 recorded events

### User

_source line 1 · 2026-05-14T21:14:42.017Z_

Read the following files and return their full contents:
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md

If either file doesn't exist, try reading it via the MCP tool mcp__agent-ml-research__read_project_file with file="literature_map.yaml" or file="paper_framing.md".

Return the full contents of both files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "70785030-78c7-4cc7-bf2d-81f201c46a72",
  "agentId": "aa8359aeff3f5958a",
  "type": "user",
  "uuid": "fcc4b2c6-c5e0-4e10-b7d1-9c4c36064844",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fee328f7-0860-430b-80de-bdcdcefd655f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T21:14:42.024Z_

```json
{
  "parentUuid": "fcc4b2c6-c5e0-4e10-b7d1-9c4c36064844",
  "isSidechain": true,
  "agentId": "aa8359aeff3f5958a",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "4320111d-e162-45a7-b967-76ad80e17afd",
  "timestamp": "2026-05-14T21:14:42.024Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fee328f7-0860-430b-80de-bdcdcefd655f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T21:14:44.308Z_



I'll read both files directly first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4320111d-e162-45a7-b967-76ad80e17afd",
  "isSidechain": true,
  "agentId": "aa8359aeff3f5958a",
  "requestId": "req_011Cb39qm2AhgNufzwN56755",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1bfef17-c3c8-4814-b8fa-6e15c46b8dea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fee328f7-0860-430b-80de-bdcdcefd655f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxkvkaLH37mcsjuUWy5E7x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14182,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14182,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 4 · 2026-05-14T21:14:44.801Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cd448YqRAVaNEgtUNF5PCj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1bfef17-c3c8-4814-b8fa-6e15c46b8dea",
  "isSidechain": true,
  "agentId": "aa8359aeff3f5958a",
  "requestId": "req_011Cb39qm2AhgNufzwN56755",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75bca5fd-d36d-411f-abe0-98bd5bc7c920",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fee328f7-0860-430b-80de-bdcdcefd655f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxkvkaLH37mcsjuUWy5E7x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14182,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14182,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 5 · 2026-05-14T21:14:44.817Z_

<details><summary>↩ Tool result · `toolu_01Cd448YqRAVaNEgtUNF5PCj`</summary>

```text
1	# StructFuse — Related Work Literature Map
2	# 最后更新: 2026-05-12
3	# 说明: 只收录项目文件中已引用的 + 确定存在的知名论文。不确定的信息标注"需验证"。
4	
5	categories:
6	
7	  # ==========================================================================
8	  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem
9	  # ==========================================================================
10	  code_retrieval_bug_fixing:
11	    description: "SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法"
12	    papers:
13	
14	      - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
15	        authors: "Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan"
16	        venue: ICLR
17	        year: 2024
18	        relation: baseline  # StructFuse 的评估基准
19	        summary: "从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。"
20	
21	      - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
22	        authors: "John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press"
23	        venue: NeurIPS
24	        year: 2024
25	        relation: competitor
26	        summary: "基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。"
27	
28	      - title: "AutoCodeRover: Autonomous Program Improvement"
29	        authors: "Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury"
30	        venue: ISSTA
31	        year: 2024
32	        relation: competitor
33	        summary: "结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。"
34	
35	      - title: "Agentless: Demystifying LLM-based Software Engineering Agents"
36	        authors: "Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang"
37	        venue: arXiv
38	        year: 2024
39	        relation: competitor
40	        summary: "无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。"
41	
42	      - title: "SWE-smith: Scaling Data for Software Engineering Agents"
43	        authors: "John Yang, Carlos E. Jimenez, Alexander Wettig, Karthik Narasimhan, Ofir Press"
44	        venue: arXiv
45	        year: 2025
46	        relation: building-block  # StructFuse 用其 repo 做数据提取
47	        summary: "自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。"
48	        note: "需验证 venue（可能已投稿会议）"
49	
50	      - title: "RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems"
51	        authors: "Tianyang Liu, Canwen Xu, Julian McAuley"
52	        venue: ICLR
53	        year: 2024
54	        relation: baseline
55	        summary: "Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务，StructFuse 可用于评估。"
56	        note: "需验证年份和 venue"
57	
58	  # ==========================================================================
59	  # Category 2: Hard Negative Mining in Contrastive Learning
60	  # ==========================================================================
61	  hard_negative_mining:
62	    description: "对比学习中 hard negative 挖掘策略，以及代码领域的对比学习"
63	    papers:
64	
65	      - title: "Dense Passage Retrieval for Open-Domain Question Answering"
66	        authors: "Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih"
67	        venue: EMNLP
68	        year: 2020
69	        relation: background
70	        summary: "DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式，是 StructFuse 对比训练的方法论基础。"
71	
72	      - title: "Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval"
73	        authors: "Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk"
74	        venue: ICLR
75	        year: 2021
76	        relation: background
77	        summary: "ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，是 StructFuse 的 baseline negative 策略之一。"
78	
79	      - title: "SimCLR: A Simple Framework for Contrastive Learning of Visual Representations"
80	        authors: "Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton"
81	        venue: ICML
82	        year: 2020
83	        relation: background
84	        summary: "视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。"
85	
86	      - title: "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"
87	        authors: "Nils Reimers, Iryna Gurevych"
88	        venue: EMNLP
89	        year: 2019
90	        relation: background
91	        summary: "Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。"
92	
93	      - title: "Mining Hard Negatives with Curriculum for Dense Retrieval"
94	        authors: "需验证"
95	        venue: "需验证"
96	        year: "需验证"
97	        relation: background
98	        summary: "课程学习式 hard negative 挖掘，从易到难训练检索器。"
99	        note: "需验证完整信息"
100	
101	  # ==========================================================================
102	  # Category 3: Program Analysis for ML
103	  # ==========================================================================
104	  program_analysis_for_ml:
105	    description: "静态分析辅助 ML，结构信息在代码表示学习中的应用"
106	    papers:
107	
108	      - title: "CodeQL: Semantic Code Analysis Engine"
109	        authors: "GitHub / Semmle"
110	        venue: "Tool (open-source)"
111	        year: 2019
112	        relation: building-block  # StructFuse 核心组件
113	        summary: "基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。"
114	
115	      - title: "code2vec: Learning Distributed Representations of Code"
116	        authors: "Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav"
117	        venue: POPL
118	        year: 2019
119	        relation: background
120	        summary: "用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。"
121	
122	      - title: "code2seq: Generating Sequences from Structured Representations of Code"
123	        authors: "Uri Alon, Shaked Brody, Omer Levy, Eran Yahav"
124	        venue: ICLR
125	        year: 2019
126	        relation: background
127	        summary: "code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。"
128	
129	      - title: "Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree"
130	        authors: "Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin"
131	        venue: SANER
132	        year: 2020
133	        relation: background
134	        summary: "用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。"
135	        note: "需验证作者和 venue"
136	
137	      - title: "GraphCodeBERT: Pre-training Code Representations with Data Flow"
138	        authors: "Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou"
139	        venue: ICLR
140	        year: 2021
141	        relation: background
142	        summary: "在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。"
143	
144	  # ==========================================================================
145	  # Category 4: Code Embeddings / Code Search
146	  # ==========================================================================
147	  code_embeddings_search:
148	    description: "代码嵌入模型和代码搜索方法"
149	    papers:
150	
151	      - title: "CodeSearchNet Challenge: Evaluating the State of Semantic Code Search"
152	        authors: "Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt"
153	        venue: arXiv
154	        year: 2019
155	        relation: background
156	        summary: "代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。"
157	
158	      - title: "CodeBERT: A Pre-Trained Model for Programming and Natural Languages"
159	        authors: "Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou"
160	        venue: EMNLP (Findings)
161	        year: 2020
162	        relation: background
163	        summary: "首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。"
164	
165	      - title: "UniXcoder: Unified Cross-Modal Pre-training for Code Representation"
166	        authors: "Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin"
167	        venue: ACL
168	        year: 2022
169	        relation: background
170	        summary: "统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。"
171	
172	      - title: "StarCoder: May the Source Be with You!"
173	        authors: "Raymond Li, Loubna Ben Allal, et al. (BigCode)"
174	        venue: TMLR
175	        year: 2023
176	        relation: background
177	        summary: "大规模开源代码 LLM，广泛用于代码嵌入的 backbone。"
178	        note: "需验证 venue（可能是 arXiv 或其他）"
179	
180	      - title: "Code Llama: Open Foundation Models for Code"
181	        authors: "Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)"
182	        venue: arXiv
183	        year: 2023
184	        relation: background
185	        summary: "Meta 的代码大模型系列，基于 Llama 2 微调。"
186	
187	      - title: "Qwen2.5-Coder Technical Report"
188	        authors: "Qwen Team (Alibaba)"
189	        venue: arXiv
190	        year: 2024
191	        relation: building-block  # StructFuse 用 Qwen2.5-Coder-3B 做检索器
192	        summary: "Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。"
193	        note: "需验证确切标题和年份"
194	
195	      - title: "Contrastive Learning for Source Code with Structural and Functional Properties"
196	        authors: "Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty"
197	        venue: ACL (Findings)
198	        year: 2022
199	        relation: background
200	        summary: "代码对比学习中利用结构/功能属性构建正负样本对。"
201	        note: "需验证作者和 venue"
202	
203	      - title: "BM25"
204	        authors: "Stephen Robertson, Hugo Zaragoza"
205	        venue: "Foundations and Trends in Information Retrieval"
206	        year: 2009
207	        relation: baseline
208	        summary: "经典稀疏检索方法，StructFuse 的 baseline 之一。Phase 2a 实验发现 BM25 在 bug fixing 定位中可能有误导性（负系数）。"
209	
210	# ==========================================================================
211	# 待补充
212	# ==========================================================================
213	# 以下论文可能相关，待确认后补充：
214	# - FAISS (Johnson et al., 2019) — ANN 检索库，StructFuse 评估可能用到
215	# - Tree-sitter — 增量解析器，与 CodeQL 互补
216	# - Aider / Moatless Tools — SWE-bench 上的其他代码检索方法
217	# - CoSQA (Huang et al., 2021) — 代码搜索 QA 数据集
218	# - DeepSeek-Coder — 另一个可能的 backbone 对比
219	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75bca5fd-d36d-411f-abe0-98bd5bc7c920",
  "isSidechain": true,
  "promptId": "70785030-78c7-4cc7-bf2d-81f201c46a72",
  "agentId": "aa8359aeff3f5958a",
  "type": "user",
  "uuid": "cd83bd87-bb2d-4cb9-a5b6-0df7e5ebdc3c",
  "sourceToolAssistantUUID": "75bca5fd-d36d-411f-abe0-98bd5bc7c920",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fee328f7-0860-430b-80de-bdcdcefd655f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T21:14:45.269Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JUjogQufF4v6FApgEAsdYg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd83bd87-bb2d-4cb9-a5b6-0df7e5ebdc3c",
  "isSidechain": true,
  "agentId": "aa8359aeff3f5958a",
  "requestId": "req_011Cb39qm2AhgNufzwN56755",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae0b1978-6d22-42c2-b7a4-ab2524dcbef4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fee328f7-0860-430b-80de-bdcdcefd655f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxkvkaLH37mcsjuUWy5E7x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14182,
      "cache_read_input_tokens": 0,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14182
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 164,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 14182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14182,
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

_source line 7 · 2026-05-14T21:14:45.275Z_

<details><summary>↩ Tool result · `toolu_01JUjogQufF4v6FApgEAsdYg`</summary>

```text
1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported "harm" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).
10	
11	2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.
12	
13	3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]
14	
15	## Story Spine
16	
17	- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.
18	
19	- **Existing approaches & gaps**:
20	  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies
21	  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal
22	  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
23	  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance
24	  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works
25	
26	- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.
27	
28	- **Headline result template**: "True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective."
29	
30	## Core Insight
31	
32	The effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.
33	
34	## Dual-Pillar Motivation
35	
36	1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.
37	2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.
38	
39	## Formal Definition
40	
41	Given retrieval domain D, structural graph G, similarity function s, query q:
42	**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)
43	
44	The structural graph is externally fixed and does not update with the encoder (drift-immune).
45	
46	## Title Options
47	
48	- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
49	- Alternative: "StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval"
50	- Backup: "Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally"
51	
52	## Venue Fit
53	
54	1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
55	2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
56	3. **Against "incremental" criticism**: Paper corrects a misconception + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.
57	
58	## Anticipated Reviewer Concerns
59	
60	| Concern | Response | Evidence |
61	|---------|----------|----------|
62	| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |
63	| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |
64	| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |
65	| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |
66	| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |
67	| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |
68	| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |
69	| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |
70	| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |
71	| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |
72	| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |
73	| "Complementary signal" overstatement | Temper: "conditionally beneficial" not "always complementary" | Writing discipline |
74	| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |
75	
76	## Evidence Status
77	
78	### Confirmed findings (basis for claims):
79	- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact
80	- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction
81	- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)
82	- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only
83	- plan_006: CodeQL scalability confirmed at 123-repo scale
84	
85	### In progress:
86	- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)
87	- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)
88	- m1_reextract_v2: expanded extraction for higher coverage
89	
90	### Planned (priority order):
91	- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)
92	- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
93	- plan_019: Pool size sensitivity (Dream consensus — external validity)
94	- plan_014: Temperature ablation (Dream reviewer concern)
95	- plan_004: RepoBench-R second benchmark (with multi-seed CIs)
96	- plan_015: Dynamic mining baseline
97	- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)
98	- plan_007/008/009: Additional ablations
99	
100	## Contingency (if full M2 results weaken claims)
101	
102	### All 18 runs confirm pilot pattern: Best case
103	- Full statistical power, paper as framed above
104	- Target: EMNLP Main
105	
106	### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
107	- Drop Claim 2 to analysis observation
108	- Paper becomes: "True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions"
109	- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main
110	
111	### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]
112	- If plan_018 shows BM25 negatives perform ≈ random (not << random), the "correcting misconception" narrative loses empirical anchor
113	- Pivot: from "CoCoHaNeRe was wrong because BM25 proxy" → "systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; prior work's negative finding was likely due to uncontrolled variables (data, training protocol), not BM25 specifically"
114	- Paper becomes less dramatic ("correcting" → "clarifying") but still valid as systematic analysis
115	- Claim 1 reworded: "True embedding-distance mining consistently improves code retrieval" (drop the "correcting misconception" framing, keep the empirical finding)
116	- Impact: weaker narrative hook but core experimental contribution survives
117	
118	### Embedding mining also loses advantage at full scale: Major reassessment needed
119	- Recheck data pipeline for bugs (full-scale data may have distribution differences)
120	- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
121	- Discuss with user before committing direction
122	
123	## Deprecated Claims (with reason)
124	
125	- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
126	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae0b1978-6d22-42c2-b7a4-ab2524dcbef4",
  "isSidechain": true,
  "promptId": "70785030-78c7-4cc7-bf2d-81f201c46a72",
  "agentId": "aa8359aeff3f5958a",
  "type": "user",
  "uuid": "5ee3a110-15a5-4b2b-9203-288da7f881ed",
  "sourceToolAssistantUUID": "ae0b1978-6d22-42c2-b7a4-ab2524dcbef4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fee328f7-0860-430b-80de-bdcdcefd655f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-14T21:17:30.675Z_

Here are the full contents of both files:

---

**File 1: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml`**

```yaml
# StructFuse — Related Work Literature Map
# 最后更新: 2026-05-12
# 说明: 只收录项目文件中已引用的 + 确定存在的知名论文。不确定的信息标注"需验证"。

categories:

  # ==========================================================================
  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem
  # ==========================================================================
  code_retrieval_bug_fixing:
    description: "SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法"
    papers:

      - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
        authors: "Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan"
        venue: ICLR
        year: 2024
        relation: baseline  # StructFuse 的评估基准
        summary: "从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。"

      - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
        authors: "John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press"
        venue: NeurIPS
        year: 2024
        relation: competitor
        summary: "基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。"

      - title: "AutoCodeRover: Autonomous Program Improvement"
        authors: "Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury"
        venue: ISSTA
        year: 2024
        relation: competitor
        summary: "结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。"

      - title: "Agentless: Demystifying LLM-based Software Engineering Agents"
        authors: "Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang"
        venue: arXiv
        year: 2024
        relation: competitor
        summary: "无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。"

      - title: "SWE-smith: Scaling Data for Software Engineering Agents"
        authors: "John Yang, Carlos E. Jimenez, Alexander Wettig, Karthik Narasimhan, Ofir Press"
        venue: arXiv
        year: 2025
        relation: building-block  # StructFuse 用其 repo 做数据提取
        summary: "自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。"
        note: "需验证 venue（可能已投稿会议）"

      - title: "RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems"
        authors: "Tianyang Liu, Canwen Xu, Julian McAuley"
        venue: ICLR
        year: 2024
        relation: baseline
        summary: "Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务，StructFuse 可用于评估。"
        note: "需验证年份和 venue"

  # ==========================================================================
  # Category 2: Hard Negative Mining in Contrastive Learning
  # ==========================================================================
  hard_negative_mining:
    description: "对比学习中 hard negative 挖掘策略，以及代码领域的对比学习"
    papers:

      - title: "Dense Passage Retrieval for Open-Domain Question Answering"
        authors: "Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih"
        venue: EMNLP
        year: 2020
        relation: background
        summary: "DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式，是 StructFuse 对比训练的方法论基础。"

      - title: "Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval"
        authors: "Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk"
        venue: ICLR
        year: 2021
        relation: background
        summary: "ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，是 StructFuse 的 baseline negative 策略之一。"

      - title: "SimCLR: A Simple Framework for Contrastive Learning of Visual Representations"
        authors: "Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton"
        venue: ICML
        year: 2020
        relation: background
        summary: "视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。"

      - title: "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"
        authors: "Nils Reimers, Iryna Gurevych"
        venue: EMNLP
        year: 2019
        relation: background
        summary: "Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。"

      - title: "Mining Hard Negatives with Curriculum for Dense Retrieval"
        authors: "需验证"
        venue: "需验证"
        year: "需验证"
        relation: background
        summary: "课程学习式 hard negative 挖掘，从易到难训练检索器。"
        note: "需验证完整信息"

  # ==========================================================================
  # Category 3: Program Analysis for ML
  # ==========================================================================
  program_analysis_for_ml:
    description: "静态分析辅助 ML，结构信息在代码表示学习中的应用"
    papers:

      - title: "CodeQL: Semantic Code Analysis Engine"
        authors: "GitHub / Semmle"
        venue: "Tool (open-source)"
        year: 2019
        relation: building-block  # StructFuse 核心组件
        summary: "基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。"

      - title: "code2vec: Learning Distributed Representations of Code"
        authors: "Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav"
        venue: POPL
        year: 2019
        relation: background
        summary: "用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。"

      - title: "code2seq: Generating Sequences from Structured Representations of Code"
        authors: "Uri Alon, Shaked Brody, Omer Levy, Eran Yahav"
        venue: ICLR
        year: 2019
        relation: background
        summary: "code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。"

      - title: "Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree"
        authors: "Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin"
        venue: SANER
        year: 2020
        relation: background
        summary: "用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。"
        note: "需验证作者和 venue"

      - title: "GraphCodeBERT: Pre-training Code Representations with Data Flow"
        authors: "Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou"
        venue: ICLR
        year: 2021
        relation: background
        summary: "在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。"

  # ==========================================================================
  # Category 4: Code Embeddings / Code Search
  # ==========================================================================
  code_embeddings_search:
    description: "代码嵌入模型和代码搜索方法"
    papers:

      - title: "CodeSearchNet Challenge: Evaluating the State of Semantic Code Search"
        authors: "Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt"
        venue: arXiv
        year: 2019
        relation: background
        summary: "代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。"

      - title: "CodeBERT: A Pre-Trained Model for Programming and Natural Languages"
        authors: "Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou"
        venue: EMNLP (Findings)
        year: 2020
        relation: background
        summary: "首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。"

      - title: "UniXcoder: Unified Cross-Modal Pre-training for Code Representation"
        authors: "Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin"
        venue: ACL
        year: 2022
        relation: background
        summary: "统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。"

      - title: "StarCoder: May the Source Be with You!"
        authors: "Raymond Li, Loubna Ben Allal, et al. (BigCode)"
        venue: TMLR
        year: 2023
        relation: background
        summary: "大规模开源代码 LLM，广泛用于代码嵌入的 backbone。"
        note: "需验证 venue（可能是 arXiv 或其他）"

      - title: "Code Llama: Open Foundation Models for Code"
        authors: "Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)"
        venue: arXiv
        year: 2023
        relation: background
        summary: "Meta 的代码大模型系列，基于 Llama 2 微调。"

      - title: "Qwen2.5-Coder Technical Report"
        authors: "Qwen Team (Alibaba)"
        venue: arXiv
        year: 2024
        relation: building-block  # StructFuse 用 Qwen2.5-Coder-3B 做检索器
        summary: "Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。"
        note: "需验证确切标题和年份"

      - title: "Contrastive Learning for Source Code with Structural and Functional Properties"
        authors: "Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty"
        venue: ACL (Findings)
        year: 2022
        relation: background
        summary: "代码对比学习中利用结构/功能属性构建正负样本对。"
        note: "需验证作者和 venue"

      - title: "BM25"
        authors: "Stephen Robertson, Hugo Zaragoza"
        venue: "Foundations and Trends in Information Retrieval"
        year: 2009
        relation: baseline
        summary: "经典稀疏检索方法，StructFuse 的 baseline 之一。Phase 2a 实验发现 BM25 在 bug fixing 定位中可能有误导性（负系数）。"

# ==========================================================================
# 待补充
# ==========================================================================
# 以下论文可能相关，待确认后补充：
# - FAISS (Johnson et al., 2019) — ANN 检索库，StructFuse 评估可能用到
# - Tree-sitter — 增量解析器，与 CodeQL 互补
# - Aider / Moatless Tools — SWE-bench 上的其他代码检索方法
# - CoSQA (Huang et al., 2021) — 代码搜索 QA 数据集
# - DeepSeek-Coder — 另一个可能的 backbone 对比
```

---

**File 2: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md`**

```markdown
# Paper Framing — StructFuse

## Target Venue
- Primary: EMNLP 2026 Main
- Deadline: ARR May 25, 2026

## Core Claims (3)

1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported "harm" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).

2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.

3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]

## Story Spine

- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.

- **Existing approaches & gaps**:
  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies
  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal
  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance
  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works

- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.

- **Headline result template**: "True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective."

## Core Insight

The effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.

## Dual-Pillar Motivation

1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.
2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.

## Formal Definition

Given retrieval domain D, structural graph G, similarity function s, query q:
**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)

The structural graph is externally fixed and does not update with the encoder (drift-immune).

## Title Options

- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
- Alternative: "StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval"
- Backup: "Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally"

## Venue Fit

1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
3. **Against "incremental" criticism**: Paper corrects a misconception + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.

## Anticipated Reviewer Concerns

| Concern | Response | Evidence |
|---------|----------|----------|
| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |
| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |
| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |
| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |
| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |
| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |
| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |
| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |
| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |
| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |
| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |
| "Complementary signal" overstatement | Temper: "conditionally beneficial" not "always complementary" | Writing discipline |
| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |

## Evidence Status

### Confirmed findings (basis for claims):
- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact
- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction
- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)
- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only
- plan_006: CodeQL scalability confirmed at 123-repo scale

### In progress:
- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)
- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)
- m1_reextract_v2: expanded extraction for higher coverage

### Planned (priority order):
- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)
- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
- plan_019: Pool size sensitivity (Dream consensus — external validity)
- plan_014: Temperature ablation (Dream reviewer concern)
- plan_004: RepoBench-R second benchmark (with multi-seed CIs)
- plan_015: Dynamic mining baseline
- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)
- plan_007/008/009: Additional ablations

## Contingency (if full M2 results weaken claims)

### All 18 runs confirm pilot pattern: Best case
- Full statistical power, paper as framed above
- Target: EMNLP Main

### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
- Drop Claim 2 to analysis observation
- Paper becomes: "True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions"
- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main

### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]
- If plan_018 shows BM25 negatives perform ≈ random (not << random), the "correcting misconception" narrative loses empirical anchor
- Pivot: from "CoCoHaNeRe was wrong because BM25 proxy" → "systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; prior work's negative finding was likely due to uncontrolled variables (data, training protocol), not BM25 specifically"
- Paper becomes less dramatic ("correcting" → "clarifying") but still valid as systematic analysis
- Claim 1 reworded: "True embedding-distance mining consistently improves code retrieval" (drop the "correcting misconception" framing, keep the empirical finding)
- Impact: weaker narrative hook but core experimental contribution survives

### Embedding mining also loses advantage at full scale: Major reassessment needed
- Recheck data pipeline for bugs (full-scale data may have distribution differences)
- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
- Discuss with user before committing direction

## Deprecated Claims (with reason)

- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
```

Both files were read directly from disk. The `literature_map.yaml` contains 4 categories of related work (Code Retrieval/Bug Fixing, Hard Negative Mining, Program Analysis for ML, Code Embeddings/Search) with 22 papers total. The `paper_framing.md` lays out the StructFuse paper targeting EMNLP 2026 Main (ARR May 25, 2026 deadline), with 3 core claims centered on hard negative mining strategies for contrastive code retrieval, contingency plans, and a detailed reviewer concern matrix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ee3a110-15a5-4b2b-9203-288da7f881ed",
  "isSidechain": true,
  "agentId": "aa8359aeff3f5958a",
  "requestId": "req_011Cb39r2ETrC79y84wCn9RN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cdc09408-0921-44e7-a9fa-5a2050cc2d81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fee328f7-0860-430b-80de-bdcdcefd655f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3Y7G7BbJxsLYjtMpLdgmR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8389,
      "cache_read_input_tokens": 14182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8389,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
