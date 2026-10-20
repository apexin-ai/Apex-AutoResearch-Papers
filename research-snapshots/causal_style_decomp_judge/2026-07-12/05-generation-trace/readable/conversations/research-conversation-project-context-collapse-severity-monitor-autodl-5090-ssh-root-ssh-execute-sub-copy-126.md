# Research conversation: <project_context> # 项目: collapse_severity_monitor ## 运行环境 - 服务器名: autodl-5090 - SSH 账户: root（调用 ssh_execute / submit_tra

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/f3293d8b-d52b-4e7e-b888-7f2458dc2ce2.jsonl`
- **Structured JSON:** [`158dd30b35b1ec111c27.json`](../../sessions/15/158dd30b35b1ec111c27.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T22:47:32.972Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T22:47:32.972Z",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "content": "&lt;project_context>\n# 项目: collapse_severity_monitor\n\n## 运行环境\n- 服务器名: autodl-5090\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/collapse_severity_monitor\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n更新 related_work_outline.md，覆盖 literature_map.yaml 新增的 14 篇论文。\n\n**背景**：docs/related_work_outline.md 目前引用 20 篇论文（基于旧版 literature_map 19+1 篇）。literature_map.yaml 已扩展到 34 篇，有 14 篇新论文未在 outline 中反映。\n\n**任务**：\n1. 读取 `literature_map.yaml`（完整版，34 篇）\n2. 读取 `docs/related_work_outline.md`（当前版本）\n3. 对比找出 outline 中缺失的论文\n4. 将缺失的论文按主题分类，插入到 outline 相应的章节中\n5. 每篇新增论文只需 1-2 句简要说明其与本项目的关系\n6. 保持 outline 的现有结构（A. Theory, B. Detection/Monitoring, C. Training Dynamics, D. Mitigation）\n7. 如有论文不属于现有分类，可新增分类（如 E. Data Quality, F. Methodological Foundations）\n8. 更新 outline 头部的论文总数\n\n**产出**：更新后的 docs/related_work_outline.md\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T22:47:32.975Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T22:47:32.975Z",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2"
}
```

---

## Round 1

21 recorded events

### User

_source line 3 · 2026-05-14T22:47:33.008Z_

&lt;project_context>
# 项目: collapse_severity_monitor

## 运行环境
- 服务器名: autodl-5090
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/collapse_severity_monitor


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
更新 related_work_outline.md，覆盖 literature_map.yaml 新增的 14 篇论文。

**背景**：docs/related_work_outline.md 目前引用 20 篇论文（基于旧版 literature_map 19+1 篇）。literature_map.yaml 已扩展到 34 篇，有 14 篇新论文未在 outline 中反映。

**任务**：
1. 读取 `literature_map.yaml`（完整版，34 篇）
2. 读取 `docs/related_work_outline.md`（当前版本）
3. 对比找出 outline 中缺失的论文
4. 将缺失的论文按主题分类，插入到 outline 相应的章节中
5. 每篇新增论文只需 1-2 句简要说明其与本项目的关系
6. 保持 outline 的现有结构（A. Theory, B. Detection/Monitoring, C. Training Dynamics, D. Mitigation）
7. 如有论文不属于现有分类，可新增分类（如 E. Data Quality, F. Methodological Foundations）
8. 更新 outline 头部的论文总数

**产出**：更新后的 docs/related_work_outline.md


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6d40a60b-3de6-4cba-96cf-f662df5975d1",
  "type": "user",
  "uuid": "9939fdc9-b281-4486-86a0-db053f4f66a4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T22:47:33.008Z_

```json
{
  "parentUuid": "9939fdc9-b281-4486-86a0-db053f4f66a4",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
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
  "uuid": "a3304ac1-f163-4642-8d87-15407c0fb701",
  "timestamp": "2026-05-14T22:47:33.008Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T22:47:33.008Z_

```json
{
  "parentUuid": "a3304ac1-f163-4642-8d87-15407c0fb701",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "ade4fd62-4f5f-482b-910a-f2c9fd129949",
  "timestamp": "2026-05-14T22:47:33.008Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T22:47:33.008Z_

```json
{
  "parentUuid": "ade4fd62-4f5f-482b-910a-f2c9fd129949",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4c8bf543-8ea6-4e9b-9615-0b3083df8af7",
  "timestamp": "2026-05-14T22:47:33.008Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Update related work outline with 14 new papers",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2"
}
```

---

### Assistant

_source line 8 · 2026-05-14T22:47:36.901Z_

Let me start by reading both files to understand the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c8bf543-8ea6-4e9b-9615-0b3083df8af7",
  "isSidechain": false,
  "requestId": "req_011Cb3GvRSPo6nk47qFnvcJJ",
  "type": "assistant",
  "uuid": "fe9078ad-530e-445f-b55e-f5703b3dcfe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXcxJJVrzwLPrsTWPzG5t7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11095,
      "cache_read_input_tokens": 11841,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11095,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 172,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11095
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

### Tool call

_source line 9 · 2026-05-14T22:47:38.339Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PwPki6qA2NeQ6tSUgyXmV7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe9078ad-530e-445f-b55e-f5703b3dcfe4",
  "isSidechain": false,
  "requestId": "req_011Cb3GvRSPo6nk47qFnvcJJ",
  "type": "assistant",
  "uuid": "f0fa6465-dc3b-4eab-8ff7-c3586f7647d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXcxJJVrzwLPrsTWPzG5t7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11095,
      "cache_read_input_tokens": 11841,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11095,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 172,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11095
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

_source line 10 · 2026-05-14T22:47:38.391Z_

<details><summary>↩ Tool result · `toolu_01PwPki6qA2NeQ6tSUgyXmV7`</summary>

```text
1	# Literature Map — collapse_severity_monitor
2	# 最后更新: 2026-05-14 (expanded to 34 papers)
3	# 研究方向: 在线监控模型 collapse 严重度——用训练动态信号实时跟踪迭代合成数据训练中的质量退化
4	
5	# ============================================================
6	# 竞争关系分类说明:
7	#   direct_competitor  — 解决同一问题（在线监控 collapse）
8	#   related            — 解决相近问题或使用相关方法
9	#   complementary      — 互补（提供理论基础/工具/缓解策略）
10	#   foundation         — 领域基础工作
11	# ============================================================
12	
13	papers:
14	
15	  # ===================== DIRECT COMPETITORS =====================
16	
17	  - id: sigma_2026
18	    title: "SIGMA: Scalable Spectral Insights for LLM Model Collapse"
19	    authors: [Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue]
20	    year: 2026
21	    venue: arXiv (2601.03385)
22	    relation: direct_competitor
23	    core_method: >
24	      通过 embedding Gram 矩阵的谱分析来量化 model collapse 程度。
25	      推导 Gram 矩阵谱的确定性和随机性界，用谱收缩作为 collapse 指标。
26	    signals: [Gram matrix spectrum, rank deficiency, spectral bounds]
27	    scale: model-level (output embeddings)
28	    key_findings:
29	      - Gram 矩阵满秩是 LLM 正常运作的必要条件
30	      - 秩亏缺意味着语义级信息丢失，标志 collapse 开始
31	      - 随机公式使框架可扩展至大规模模型
32	    vs_ours: >
33	      SIGMA 用输出嵌入的 Gram 矩阵谱，是事后/黑盒方法，不需要模型权重。
34	      我们用训练动态信号（权重频谱熵、stable rank、token entropy），
35	      是训练中实时监控，更早期更细粒度（per-layer）。
36	      SIGMA 不做 per-layer 分析，不跟踪训练过程的动态变化。
37	    threat_level: medium
38	
39	  - id: kalinowski_2026
40	    title: "Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index"
41	    authors: [Alexander Kalinowski]
42	    year: 2026
43	    venue: arXiv (2604.26984)
44	    relation: direct_competitor
45	    core_method: >
46	      提出在线拓扑感知监控器，结合 Modular Morse Homology Maintenance (MMHM)
47	      和复合 Collapse Index (CI)，通过稀疏增量更新实现快速在线监控。
48	    signals: [persistent homology, Collapse Index (CI), topological features]
49	    scale: model-level (representation space topology)
50	    key_findings:
51	      - CI 在 LLM fine-tuning 和时序 KGE 训练中提供低延迟早期预警
52	      - 表征各向异性和多尺度结构丧失在性能指标反应之前就可检测
53	      - 增量更新避免每个 epoch 重建复形
54	    vs_ours: >
55	      Kalinowski 用拓扑信号（persistent homology），我们用频谱/熵信号。
56	      两者都是在线监控，但信号族完全不同。我们的信号更轻量、
57	      更可解释（stable rank/spectral entropy 有直接的线性代数含义）。
58	      Kalinowski 不研究迭代合成数据训练场景。
59	    threat_level: medium
60	
61	  # ===================== CLOSELY RELATED =====================
62	
63	  - id: spectral_lens_2026
64	    title: "Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization"
65	    authors: [Andy Zeyi Liu et al.]
66	    year: 2026
67	    venue: arXiv (2605.05683)
68	    relation: related
69	    core_method: >
70	      用 activation covariance 和 per-sample gradient 的 SVD 谱
71	      作为 LLM 训练优化的诊断工具。
72	    signals: [activation covariance spectrum, gradient SVD spectrum]
73	    scale: layer-level
74	    key_findings:
75	      - batch size 是表示几何的隐藏决定因素
76	      - 早期训练的 activation covariance 尾部可预测下游 token 效率
77	      - activation 谱头部运动 + gradient 谱可区分学习侧和执行侧改进
78	    vs_ours: >
79	      方法论高度相关——同样用频谱分析训练动态。
80	      但他们关注优化诊断，不研究 collapse/合成数据退化。
81	      可作为方法论参考。
82	    threat_level: low
83	
84	  - id: shi_neurips2025
85	    title: "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"
86	    authors: [Lianghe Shi, Meng Wu, Huijie Zhang, Zekai Zhang, Molei Tao, Qing Qu]
87	    year: 2025
88	    venue: NeurIPS 2025 (Spotlight)
89	    relation: related
90	    core_method: >
91	      揭示 model collapse 中从泛化到记忆的转变。
92	      发现训练数据熵与模型泛化能力的强线性相关。
93	      提出基于熵的子集选择方法来减缓 collapse。
94	    signals: [dataset entropy, generalization metrics]
95	    scale: model-level (data distribution)
96	    key_findings:
97	      - 迭代训练中数据分布熵急剧下降导致泛化能力下降
98	      - 强线性相关：训练数据集熵与模型泛化能力
99	      - 熵选择方法有效减缓泛化到记忆转变
100	    vs_ours: >
101	      他们用数据级别的熵，我们用模型内部的训练动态信号。
102	      互补：他们的数据熵可作为我们的外部验证指标。
103	      他们不做 per-layer 分析，不做在线监控。
104	    threat_level: low
105	
106	  - id: wyss_2024
107	    title: "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI"
108	    authors: [C. M. Wyss et al.]
109	    year: 2024
110	    venue: arXiv (2410.12341)
111	    relation: related
112	    core_method: >
113	      用语义网络和 next-token 概率来表征 LLM 中的 model collapse。
114	      引入 collapsed prediction 概念量化多样性损失。
115	      分析不同合成 token 比例 (25%/50%/75%) 对 collapse 的影响。
116	    signals: [next-token probability distribution, semantic network metrics, collapsed prediction ratio]
117	    scale: token-level (output)
118	    key_findings:
119	      - Next-token 概率分布可精确量化多样性损失
120	      - 合成 token 比例越高，collapse 越严重
121	      - 跨数据集迁移：在非微调数据集上 collapse 程度不同
122	    vs_ours: >
123	      他们用输出级指标（next-token prob），我们用训练动态内部信号。
124	      他们的 synthetic fraction 实验与我们的实验设计有重叠。
125	      不同之处：他们是事后分析，我们是训练中在线监控。
126	    threat_level: low
127	
128	  - id: xu_2026
129	    title: "Predicting LLM Compression Degradation from Spectral Statistics"
130	    authors: [Mingxue Xu]
131	    year: 2026
132	    venue: arXiv (2604.18085)
133	    relation: related
134	    core_method: >
135	      用 stable rank 和信息密度 (bits/param) 预测 LLM 压缩导致的退化。
136	      交互项 compression_ratio * stable_rank 是退化的强预测器。
137	    signals: [stable rank, information density, compression ratio]
138	    scale: layer-level (attention vs MLP 分开分析)
139	    key_findings:
140	      - stable rank 是压缩退化的主要预测因子（Pearson r=0.890 attention, 0.839 MLP）
141	      - 层类型比压缩方法更重要
142	      - layer-specific calibration 优于 method-specific tuning
143	    vs_ours: >
144	      直接验证 stable rank 作为退化预测信号的有效性。
145	      虽然场景不同（压缩 vs collapse），但支持我们选用 stable rank 的合理性。
146	      他们的 per-layer 分析方法可参考。
147	    threat_level: low
148	
149	  - id: layer_collapse_diffusion_2026
150	    title: "Layer Collapse in Diffusion Language Models"
151	    authors: [Alexander Conzelmann, Albert Catalan-Tatjer, Shiwei Liu]
152	    year: 2026
153	    venue: arXiv (2605.06366)
154	    relation: related
155	    core_method: >
156	      分析 diffusion language model (LLaDA-8B) 中的 per-layer activation 动态，
157	      发现少数早期层展现 collapsed activation patterns。
158	    signals: [activation patterns, super-outlier magnitude]
159	    scale: layer-level
160	    key_findings:
161	      - 几个早期层出现 channel-axis collapse（单一维度主导所有位置）
162	      - 尽管看似冗余，pruning outlier 导致退化为重复随机 token 循环
163	      - Diffusion LM 与 autoregressive LM 的 collapse 行为不同
164	    vs_ours: >
165	      做了 per-layer collapse 分析，但在 diffusion LM 上。
166	      方法论参考：per-layer activation 分析方法。
167	    threat_level: low
168	
169	  # ===================== FOUNDATION =====================
170	
171	  - id: alemohammad_iclr2024
172	    title: "Self-Consuming Generative Models Go MAD"
173	    authors: [Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk]
174	    year: 2024
175	    venue: ICLR 2024
176	    relation: foundation
177	    core_method: >
178	      定义三种 autophagous loop（fully synthetic / synthetic augmentation / fresh data），
179	      证明无足够真实数据时 precision 或 recall 必然下降（MAD 现象）。
180	    signals: [FID, precision, recall]
181	    scale: model-level (image generative models)
182	    key_findings:
183	      - 三种 loop 类型的 collapse 行为不同
184	      - 无 fresh data 时 quality 或 diversity 必然退化
185	      - 在 StyleGAN、DDPM、denoising diffusion 上验证
186	    vs_ours: >
187	      领域基础论文之一。他们的 loop 分类框架直接对应我们的实验设计。
188	      他们用 FID/precision/recall（事后指标），我们提供训练中在线信号。
189	
190	  - id: papyan_pnas2020
191	    title: "Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training"
192	    authors: [Vardan Papyan, X. Y. Han, David L. Donoho]
193	    year: 2020
194	    venue: PNAS 117(40), 24652-24663
195	    relation: foundation
196	    core_method: >
197	      发现分类网络训练末期的 Neural Collapse——类内表征收缩到 Simplex ETF。
198	    signals: [within-class variability, classifier-mean alignment]
199	    scale: model-level (last-layer representations)
200	    key_findings:
201	      - 训练末期出现四种 collapse 现象
202	      - 类均值收敛到 Simplex ETF 顶点
203	      - Collapse 与泛化能力相关
204	    vs_ours: >
205	      虽然 neural collapse 与 model collapse 是不同概念，
206	      但谱分析方法论可借鉴，且提供 "collapse" 概念的对比参考。
207	
208	  # ===================== COMPLEMENTARY (Theory/Mitigation) =====================
209	
210	  - id: shumailov_nature2024
211	    title: "AI Models Collapse When Trained on Recursively Generated Data"
212	    authors: [Ilia Shumailov et al.]
213	    year: 2024
214	    venue: Nature 631, 755-759
215	    relation: foundation
216	    core_method: >
217	      首次系统性证明迭代合成数据训练导致 model collapse。
218	      在 LLM、VAE、GMM 上验证。分布尾部消失是核心机制。
219	    signals: [test loss, distribution tail metrics]
220	    scale: model-level
221	    key_findings:
222	      - 迭代训练导致不可逆缺陷：分布尾部消失
223	      - 罕见事件最先遗忘
224	      - LLM、VAE、GMM 都有此现象
225	    vs_ours: >
226	      领域基石论文，建立了我们要解决的问题。
227	      他们用事后评估（test loss），我们提供在线监控手段。
228	
229	  - id: dohmatob_iclr2025
230	    title: "Strong Model Collapse"
231	    authors: [Elvis Dohmatob, Yunzhen Feng et al.]
232	    year: 2025
233	    venue: ICLR 2025 (Spotlight)
234	    relation: complementary
235	    core_method: >
236	      用算子值自由概率论证明即使极小比例的合成数据 (1/1000)
237	      也会导致 model collapse，且更大模型放大 collapse。
238	    signals: [test error on real data, bias-variance decomposition]
239	    scale: model-level
240	    key_findings:
241	      - 任何非零常数比例的合成数据都导致 collapse
242	      - 更大模型可放大 collapse
243	      - 神经缩放定律在合成数据下失效
244	    vs_ours: >
245	      理论基础——解释了为什么需要监控（即使少量合成数据也危险）。
246	      他们的 fraction 实验与我们的实验设计直接相关。
247	
248	  - id: gerstgrasser_2024
249	    title: "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data"
250	    authors: [Matthias Gerstgrasser, Rylan Schaeffer et al.]
251	    year: 2024
252	    venue: arXiv (2404.01413)
253	    relation: complementary
254	    core_method: >
255	      证明数据累积（而非替换）可避免 model collapse。
256	      替换导致 test error 增长，累积则有有限上界。
257	    signals: [test error over iterations]
258	    scale: model-level
259	    key_findings:
260	      - 累积真实+合成数据则无 collapse（所有模型/模态）
261	      - 替换数据则 collapse
262	      - 关键因素是数据管理策略
263	    vs_ours: >
264	      互补——他们研究何时 collapse（数据管理策略），
265	      我们研究如何实时检测 collapse（训练动态信号）。
266	
267	  - id: kazdan_2024
268	    title: "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"
269	    authors: [Joshua Kazdan et al.]
270	    year: 2024
271	    venue: arXiv (2410.16713)
272	    relation: complementary
273	    core_method: >
274	      系统比较三种训练工作流：replace（collapse）、
275	      accumulate（稳定）、fixed compute（介于两者之间）。
276	    signals: [test loss on real data]
277	    scale: model-level
278	    key_findings:
279	      - Replace 工作流一定 collapse
280	      - Accumulate 工作流保持稳定
281	      - Fixed compute 工作流 loss 升高但 plateau
282	    vs_ours: 互补——提供实验设计参考（不同工作流下 collapse 行为差异）。
283	
284	  - id: seddik_2024
285	    title: "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse"
286	    authors: [Mohamed El Amine Seddik et al.]
287	    year: 2024
288	    venue: arXiv (2404.05090)
289	    relation: complementary
290	    core_method: >
291	      统计模型严格刻画不同递归训练场景下的 collapse 程度。
292	      给出混合真实/合成数据时避免 collapse 的最大合成数据比例估计。
293	    signals: [distribution tail, statistical divergence]
294	    scale: model-level
295	    key_findings:
296	      - 纯合成数据训练无法避免 collapse
297	      - 混合训练下存在可计算的合成数据上限
298	      - 分布尾部消失是 collapse 的统计特征
299	    vs_ours: 理论互补——给出合成数据比例的安全阈值。
300	
301	  - id: schaeffer_2025
302	    title: "Position: Model Collapse Does Not Mean What You Think"
303	    authors: [Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo]
304	    year: 2025
305	    venue: arXiv (2503.03150)
306	    relation: complementary
307	    core_method: >
308	      梳理 model collapse 文献中 8 种不同定义，
309	      分为三个家族：test loss 行为、分布形变、缩放行为。
310	    signals: N/A (position paper)
311	    scale: N/A
312	    key_findings:
313	      - Model collapse 有 8 种不完全一致的定义
314	      - 三个家族：test loss 行为、分布形变、缩放定律
315	      - 术语混乱阻碍了系统性理解
316	    vs_ours: >
317	      重要定位参考——论文中需明确使用哪种 collapse 定义。
318	      建议采用他们的分类框架。
319	
320	  - id: feng_iclr2025
321	    title: "Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification"
322	    authors: [Feng et al.]
323	    year: 2025
324	    venue: ICLR 2025
325	    relation: complementary
326	    core_method: >
327	      用高斯混合+线性分类器+线性验证器推导验证器有效的条件。
328	      证明不完美验证器也可有效筛选合成数据。
329	    signals: [verifier-based quality score]
330	    scale: model-level
331	    key_findings:
332	      - 验证器筛选合成数据可达到最优性能
333	      - 即使不完美验证器也有效
334	      - 给出可衡量的代理条件
335	    vs_ours: 互补——缓解策略。我们的监控信号可作为验证器的补充。
336	
337	  - id: yi_2025
338	    title: "Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence"
339	    authors: [Bingji Yi, Qiyuan Liu, Yuwei Cheng, Haifeng Xu]
340	    year: 2025
341	    venue: arXiv (2510.16657)
342	    relation: complementary
343	    core_method: >
344	      证明外部验证器（人类或更强模型）可阻止 collapse。
345	      分析验证器引导下的短期改进和长期收敛行为。
346	    signals: [verifier quality score]
347	    scale: model-level
348	    key_findings:
349	      - 外部验证器注入信息则不会 collapse
350	      - 短期有改进，长期收敛到验证器的知识中心
351	    vs_ours: 互补——缓解策略方向，与监控方向正交。
352	
353	  - id: bakshi_2026
354	    title: "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources"
355	    authors: [Soham Bakshi et al.]
356	    year: 2026
357	    venue: arXiv (2602.10531)
358	    relation: complementary
359	    core_method: >
360	      分析在真实+合成混合数据上的迭代训练动态。
361	      next-token prediction 模型下的长期演化分析。
362	    signals: [mixture weight, sample size, test performance]
363	    scale: model-level
364	    key_findings:
365	      - 非零真实数据混合权重（即使递减）可避免 collapse
366	      - 混合权重和样本量共同控制长期性能
367	    vs_ours: 理论互补——刻画迭代训练的长期演化。
368	
369	  - id: dohmatob_icml2024
370	    title: "A Tale of Tails: Model Collapse as a Change of Scaling Laws"
371	    authors: [Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, Julia Kempe]
372	    year: 2024
373	    venue: ICML 2024 (pp. 11165-11197)
374	    relation: complementary
375	    core_method: >
376	      从 scaling law 视角分析 collapse——理论框架揭示 collapse 导致 scaling law 改变。
377	    signals: [test loss scaling, skill metrics]
378	    scale: model-level
379	    key_findings:
380	      - Loss of scaling、shifted scaling with number of generations
381	      - Skill un-learning 现象
382	      - 混合人类/合成数据时的 grokking 效应
383	    vs_ours: >
384	      理论背景——从 scaling law 角度量化 collapse 严重度。
385	      我们用训练动态信号在训练中追踪，他们用事后 scaling 分析。
386	
387	  - id: fu_icml2024
388	    title: "Towards Theoretical Understandings of Self-Consuming Generative Models"
389	    authors: [Shi Fu, Sen Zhang, Yingjie Wang, Xinmei Tian, Dacheng Tao]
390	    year: 2024
391	    venue: ICML 2024
392	    relation: complementary
393	    core_method: >
394	      构建严格理论框架分析 self-consuming loop 中数据分布演化。
395	      分析参数和非参数模型中三种误差源的复合效应。
396	    signals: [distribution divergence, error accumulation]
397	    scale: model-level
398	    key_findings:
399	      - 统计/表达/近似三种误差在迭代中复合
400	      - 给出误差增长的理论界
401	    vs_ours: 理论互补——严格刻画 collapse 的误差复合机制。
402	
403	  - id: gillman_icml2024
404	    title: "Self-Correcting Self-Consuming Loops for Generative Model Training"
405	    authors: [Nate Gillman, Michael Freeman, Daksh Aggarwal, Chia-Hong Hsu, Calvin Luo, Yonglong Tian, Chen Sun]
406	    year: 2024
407	    venue: ICML 2024
408	    relation: complementary
409	    core_method: >
410	      引入 correction function 使 self-consuming loop 指数级更稳定。
411	      在人体运动合成任务上验证。
412	    signals: [corrector quality, loop stability]
413	    scale: model-level
414	    key_findings:
415	      - Correction function 使 loop 指数级稳定
416	      - 即使 synthetic:real = 100:1 也可避免 collapse
417	    vs_ours: 互补——缓解策略，correction function 概念与在线监控互补。
418	
419	  # ===================== DATA CONTAMINATION DETECTION =====================
420	
421	  - id: kirchenbauer_icml2023
422	    title: "A Watermark for Large Language Models"
423	    authors: [John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, Tom Goldstein]
424	    year: 2023
425	    venue: ICML 2023 (pp. 17061-17084)
426	    relation: complementary
427	    core_method: >
428	      LLM 文本水印框架——green/red token list + soft promotion + 统计检测。
429	    signals: [green token ratio, z-score]
430	    scale: token-level (output)
431	    key_findings:
432	      - 可嵌入统计可检测水印且不影响文本质量
433	      - 开源检测算法不需模型访问
434	    vs_ours: 合成数据溯源的基础方法，与 collapse 检测互补。
435	
436	  - id: dathathri_nature2024
437	    title: "Scalable Watermarking for Identifying Large Language Model Outputs"
438	    authors: [Sumanth Dathathri, Abigail See, Sumedh Ghaisas et al.]
439	    year: 2024
440	    venue: Nature 634, 818-823
441	    relation: complementary
442	    core_method: >
443	      SynthID-Text：产品级文本水印，与 speculative sampling 集成。
444	      在 Gemini ~20M 响应上验证。
445	    signals: [watermark detection score]
446	    scale: token-level (output)
447	    key_findings:
448	      - 产品级规模的水印部署
449	      - 不影响文本质量，最小延迟开销
450	    vs_ours: 大规模合成数据标记的工业实践，与监控方向互补。
451	
452	  - id: sander_neurips2024
453	    title: "Watermarking Makes Language Models Radioactive"
454	    authors: [Tom Sander, Pierre Fernandez, Alain Durmus, Matthijs Douze, Teddy Furon]
455	    year: 2024
456	    venue: NeurIPS 2024
457	    relation: related
458	    core_method: >
459	      证明在水印 LLM 输出上微调的模型保留水印残留（"放射性"）。
460	    signals: [watermark residual in fine-tuned model]
461	    scale: model-level
462	    key_findings:
463	      - 水印信号通过训练传播到下游模型
464	      - 可检测模型是否在合成数据上训练
465	    vs_ours: >
466	      直接相关——检测合成数据训练的替代方法。
467	      他们检测"是否用了合成数据"，我们监控"合成数据造成多严重的 collapse"。
468	
469	  - id: mitchell_icml2023
470	    title: "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature"
471	    authors: [Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn]
472	    year: 2023
473	    venue: ICML 2023 (pp. 24950-24962)
474	    relation: complementary
475	    core_method: >
476	      LLM 生成文本占据 log-probability 负曲率区域，据此零样本检测。
477	    signals: [log probability curvature]
478	    scale: text-level
479	    key_findings:
480	      - 生成文本的概率曲率特征可区分人类/机器文本
481	      - 0.95 AUROC 检测 GPT-NeoX 20B 生成的假新闻
482	    vs_ours: 合成文本检测方法，可识别训练数据中的合成成分。
483	
484	  - id: shi_iclr2024
485	    title: "Detecting Pretraining Data from Large Language Models"
486	    authors: [Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer]
487	    year: 2024
488	    venue: ICLR 2024
489	    relation: related
490	    core_method: >
491	      Min-K% Prob：未见样本含低概率 outlier word，据此检测预训练数据成员。
492	    signals: [Min-K% probability score]
493	    scale: text-level
494	    key_findings:
495	      - 比 reference model 方法提升 7.4%
496	      - 适用于版权检测、污染检测、隐私审计
497	    vs_ours: 数据污染检测工具——可检测合成数据是否混入训练集，与 collapse 监控互补。
498	
499	  # ===================== METHODOLOGICAL FOUNDATIONS =====================
500	
501	  - id: martin_mahoney_2021
502	    title: "Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data"
503	    authors: [Charles H. Martin, Michael W. Mahoney]
504	    year: 2021
505	    venue: Nature Communications 12
506	    relation: complementary
507	    core_method: >
508	      WeightWatcher 工具——用 RMT 分析权重矩阵的谱性质，
509	      无需训练/测试数据即可预测模型质量。
510	    signals: [stable rank, power law exponent (alpha), spectral norm]
511	    scale: layer-level (per weight matrix)
512	    key_findings:
513	      - stable rank 追踪自正则化程度
514	      - 5+1 训练阶段对应不同的谱形态
515	      - heavy-tailed 分布特征区分好/差模型
516	    vs_ours: >
517	      方法论基础——WeightWatcher 的 stable rank 和谱分析方法
518	      直接启发我们的信号设计。
519	
520	  - id: yunis_2024
521	    title: "Approaching Deep Learning through the Spectral Dynamics of Weights"
522	    authors: [David Yunis, Kumar Kshitij Patel et al.]
523	    year: 2024
524	    venue: arXiv (2408.11804)
525	    relation: complementary
526	    core_method: >
527	      以权重奇异值/向量的动态演化为核心视角理解深度学习。
528	      证明谱动态可区分记忆网络和泛化网络。
529	    signals: [singular value dynamics, singular vector alignment]
530	    scale: layer-level (per weight matrix)
531	    key_findings:
532	      - 权重衰减增强低秩偏置
533	      - 谱动态区分记忆 vs 泛化
534	      - 与 lottery ticket 和 loss surface 结构相关
535	    vs_ours: 方法论基础——谱动态视角可用于理解 collapse 过程中的权重变化。
536	
537	  - id: chen_liu_2024
538	    title: "Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy"
539	    authors: [Chen Liu et al.]
540	    year: 2024
541	    venue: IEEE CISS 2024
542	    relation: complementary
543	    core_method: >
544	      提出 Diffusion Spectral Entropy (DSE) 和 Diffusion Spectral Mutual Information (DSMI)，
545	      利用数据几何在高维中可靠计算信息论指标。
546	    signals: [DSE, DSMI]
547	    scale: layer-level (representations)
548	    key_findings:
549	      - DSE 在训练中增加
550	      - DSMI(class label) 在泛化学习中增加，过拟合时停滞
551	      - 可用于指导网络初始化和预测下游准确率
552	    vs_ours: >
553	      方法论工具——DSE 是我们 spectral entropy 信号的潜在替代实现。
554	
555	  - id: lu_neurips2024
556	    title: "AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models"
557	    authors: [Haiquan Lu, Yefan Zhou, Shiwei Liu, Zhangyang Wang, Michael W. Mahoney, Yaoqing Yang]
558	    year: 2024
559	    venue: NeurIPS 2024
560	    relation: complementary
561	    core_method: >
562	      用 HT-SR 理论的谱密度形态（alpha exponent）指导 LLM 层级剪枝。
563	    signals: [alpha exponent, ESD shape metrics]
564	    scale: layer-level
565	    key_findings:
566	      - Alpha exponent 有效指导 per-layer 剪枝比例
567	      - LLaMA-7B 可剪至 80% sparsity 保持合理 perplexity
568	    vs_ours: >
569	      验证 per-layer 谱分析对 LLM 质量评估的有效性。
570	      支持我们用类似方法监控 collapse。
571	
572	  - id: sanyal_iclr2020
573	    title: "Stable Rank Normalization for Improved Generalization in Neural Networks and GANs"
574	    authors: [Amartya Sanyal, Philip H. S. Torr, Puneet K. Dokania]
575	    year: 2020
576	    venue: ICLR 2020
577	    relation: complementary
578	    core_method: >
579	      提出 stable rank normalization——最小化线性算子的 stable rank。
580	      理论证明唯一最优解，实验验证改善泛化。
581	    signals: [stable rank, Lipschitz constant]
582	    scale: layer-level
583	    key_findings:
584	      - 控制 stable rank 改善泛化 gap 11.3%
585	      - Stable rank 与泛化能力直接关联
586	    vs_ours: >
587	      理论支持——建立 stable rank 与泛化的直接联系。
588	      支持我们选用 stable rank 作为 collapse（泛化退化）的监控信号。
589	
590	  - id: kalra_2026
591	    title: "A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs"
592	    authors: [Dayal Singh Kalra, Jean-Christophe Gagnon-Audet, Andrey Gromov, Ishita Mediratta, Kelvin Niu, Alexander H. Miller, Michael Shvartsman]
593	    year: 2026
594	    venue: arXiv (2601.16979)
595	    relation: related
596	    core_method: >
597	      Critical sharpness：<10 forward passes 高效度量 loss landscape 曲率。
598	      首次在 7B 规模验证 progressive sharpening 和 Edge of Stability。
599	    signals: [critical sharpness, relative critical sharpness]
600	    scale: model-level
601	    key_findings:
602	      - Progressive sharpening 在 7B 规模仍然存在
603	      - Critical sharpness 可指导 pre-train 到 fine-tune 的数据混合
604	    vs_ours: >
605	      训练动态监控方法论参考——高效的大规模 LLM 训练动态度量。
606	      Critical sharpness 可作为我们信号集的潜在补充。
607	
608	  # ===================== DATA QUALITY =====================
609	
610	  - id: penedo_2024
611	    title: "The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale"
612	    authors: [Guilherme Penedo, Hynek Kydlicek, Loubna Ben allal, Anton Lozhkov, Margaret Mitchell, Colin Raffel, Leandro Von Werra, Thomas Wolf]
613	    year: 2024
614	    venue: arXiv (2406.17557)
615	    relation: complementary
616	    core_method: >
617	      15T token 数据集的完整策略文档——去重、过滤、教育文本提取。
618	    signals: [data quality classifiers, deduplication metrics]
619	    scale: dataset-level
620	    key_findings:
621	      - 详细 ablation 各种去重和过滤策略
622	      - FineWeb-Edu 在知识密集任务上大幅提升性能
623	    vs_ours: 数据质量策略参考——理解高质量训练数据标准，为分析 collapse 的数据原因提供基线。
624	
625	  - id: zhang_2026
626	    title: "The LLM Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data"
627	    authors: [Kaituo Zhang, Mingzhi Hu, Hoang Anh Duy Le et al.]
628	    year: 2026
629	    venue: arXiv (2601.17717)
630	    relation: complementary
631	    core_method: >
632	      系统分类合成数据评估指标——quality (validity/fidelity/utility) +
633	      trustworthiness (safety/faithfulness)。
634	    signals: [quality metrics taxonomy, trustworthiness metrics]
635	    scale: dataset-level
636	    key_findings:
637	      - 从内在属性评估合成数据，而非仅看下游性能
638	      - 质量和可信度两个维度的完整分类体系
639	    vs_ours: 合成数据质量评估框架——为理解 collapse 的数据级原因提供指标体系。
640	
641	# ============================================================
642	# 关键发现总结
643	# ============================================================
644	
645	summary:
646	  total_papers: 34
647	  direct_competitors: 2  # SIGMA, Kalinowski
648	  novelty_confirmation: >
649	    在 34 篇文献中，没有工作同时做到：(a) 训练中在线监控 (b) 用频谱/熵训练动态信号
650	    (c) per-layer 粒度 (d) 在迭代合成数据训练场景下验证。
651	    我们的核心新颖性空间依然存在。
652	
653	  coverage:
654	    model_collapse_theory: 14  # shumailov, dohmatob x2, alemohammad, fu, gerstgrasser, seddik, kazdan, schaeffer, bakshi, shi_neurips2025, feng, yi, gillman
655	    data_contamination: 5  # kirchenbauer, dathathri, sander, mitchell, shi_iclr2024
656	    spectral_methods: 8  # sigma, martin_mahoney, yunis, lu, sanyal, spectral_lens, xu, conzelmann
657	    training_dynamics: 4  # kalinowski, chen_liu, kalra, papyan
658	    data_quality: 3  # wyss, penedo, zhang
659	
660	  gap_analysis:
661	    sigma: >
662	      用输出嵌入 Gram 矩阵谱——事后/黑盒，不做 per-layer，不跟踪训练过程。
663	    kalinowski: >
664	      用拓扑信号——在线但信号族不同，不研究迭代合成数据场景。
665	    our_unique_position: >
666	      训练动态频谱/熵信号 + per-layer 粒度 + 迭代合成数据场景 = 独特定位。
667	
668	  per_layer_collapse_analysis:
669	    papers_with_per_layer:
670	      - layer_collapse_diffusion_2026  # diffusion LM per-layer activation collapse
671	      - xu_2026  # stable rank per-layer（compression 场景）
672	      - spectral_lens_2026  # per-layer activation/gradient 谱
673	      - lu_neurips2024  # alpha exponent per-layer for pruning
674	    gap: "无论文在迭代合成数据训练中做 per-layer collapse 分析"
675	
676	  stable_rank_as_collapse_signal:
677	    papers_using_stable_rank:
678	      - martin_mahoney_2021  # WeightWatcher 中作为模型质量指标
679	      - xu_2026  # 压缩退化预测器 (r=0.89)
680	      - yunis_2024  # 谱动态中的低秩偏置
681	      - sanyal_iclr2020  # stable rank 与泛化的直接联系
682	    gap: "无论文直接用 stable rank 监控 iterative synthetic data collapse"
683	
684	  spectral_entropy_as_collapse_signal:
685	    papers_using_spectral_entropy:
686	      - chen_liu_2024  # DSE 跟踪训练动态
687	      - sigma_2026  # 谱分析但在 Gram 矩阵上
688	    gap: "无论文直接用 weight spectral entropy 监控 collapse"
689	
690	  synthetic_fraction_effects:
691	    papers_studying_fraction:
692	      - dohmatob_iclr2025  # 理论：任何非零 fraction 都危险
693	      - dohmatob_icml2024  # scaling law 角度的 fraction 分析
694	      - alemohammad_iclr2024  # 三种 loop 类型的不同效果
695	      - wyss_2024  # 实证：25%/50%/75% 不同 collapse 程度
696	      - seddik_2024  # 统计：给出安全上限估计
697	    gap: "大量理论/实证工作，但都用事后指标衡量 fraction 效果"
698	
699	  data_contamination_detection:
700	    papers:
701	      - kirchenbauer_icml2023  # 基础水印方法
702	      - dathathri_nature2024  # 产品级水印 (SynthID)
703	      - sander_neurips2024  # 水印放射性传播
704	      - mitchell_icml2023  # DetectGPT 概率曲率检测
705	      - shi_iclr2024  # Min-K% 预训练数据检测
706	    relevance: >
707	      合成数据检测与 collapse 监控互补：他们回答"是否有合成数据"，
708	      我们回答"合成数据造成了多严重的 collapse"。
709	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0fa6465-dc3b-4eab-8ff7-c3586f7647d3",
  "isSidechain": false,
  "promptId": "6d40a60b-3de6-4cba-96cf-f662df5975d1",
  "type": "user",
  "uuid": "aa77242a-cd6b-4d75-afa0-01358d0baa87",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/literature_map.yaml",
      "content": "# Literature Map — collapse_severity_monitor\n# 最后更新: 2026-05-14 (expanded to 34 papers)\n# 研究方向: 在线监控模型 collapse 严重度——用训练动态信号实时跟踪迭代合成数据训练中的质量退化\n\n# ============================================================\n# 竞争关系分类说明:\n#   direct_competitor  — 解决同一问题（在线监控 collapse）\n#   related            — 解决相近问题或使用相关方法\n#   complementary      — 互补（提供理论基础/工具/缓解策略）\n#   foundation         — 领域基础工作\n# ============================================================\n\npapers:\n\n  # ===================== DIRECT COMPETITORS =====================\n\n  - id: sigma_2026\n    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n    authors: [Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue]\n    year: 2026\n    venue: arXiv (2601.03385)\n    relation: direct_competitor\n    core_method: >\n      通过 embedding Gram 矩阵的谱分析来量化 model collapse 程度。\n      推导 Gram 矩阵谱的确定性和随机性界，用谱收缩作为 collapse 指标。\n    signals: [Gram matrix spectrum, rank deficiency, spectral bounds]\n    scale: model-level (output embeddings)\n    key_findings:\n      - Gram 矩阵满秩是 LLM 正常运作的必要条件\n      - 秩亏缺意味着语义级信息丢失，标志 collapse 开始\n      - 随机公式使框架可扩展至大规模模型\n    vs_ours: >\n      SIGMA 用输出嵌入的 Gram 矩阵谱，是事后/黑盒方法，不需要模型权重。\n      我们用训练动态信号（权重频谱熵、stable rank、token entropy），\n      是训练中实时监控，更早期更细粒度（per-layer）。\n      SIGMA 不做 per-layer 分析，不跟踪训练过程的动态变化。\n    threat_level: medium\n\n  - id: kalinowski_2026\n    title: \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\"\n    authors: [Alexander Kalinowski]\n    year: 2026\n    venue: arXiv (2604.26984)\n    relation: direct_competitor\n    core_method: >\n      提出在线拓扑感知监控器，结合 Modular Morse Homology Maintenance (MMHM)\n      和复合 Collapse Index (CI)，通过稀疏增量更新实现快速在线监控。\n    signals: [persistent homology, Collapse Index (CI), topological features]\n    scale: model-level (representation space topology)\n    key_findings:\n      - CI 在 LLM fine-tuning 和时序 KGE 训练中提供低延迟早期预警\n      - 表征各向异性和多尺度结构丧失在性能指标反应之前就可检测\n      - 增量更新避免每个 epoch 重建复形\n    vs_ours: >\n      Kalinowski 用拓扑信号（persistent homology），我们用频谱/熵信号。\n      两者都是在线监控，但信号族完全不同。我们的信号更轻量、\n      更可解释（stable rank/spectral entropy 有直接的线性代数含义）。\n      Kalinowski 不研究迭代合成数据训练场景。\n    threat_level: medium\n\n  # ===================== CLOSELY RELATED =====================\n\n  - id: spectral_lens_2026\n    title: \"Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization\"\n    authors: [Andy Zeyi Liu et al.]\n    year: 2026\n    venue: arXiv (2605.05683)\n    relation: related\n    core_method: >\n      用 activation covariance 和 per-sample gradient 的 SVD 谱\n      作为 LLM 训练优化的诊断工具。\n    signals: [activation covariance spectrum, gradient SVD spectrum]\n    scale: layer-level\n    key_findings:\n      - batch size 是表示几何的隐藏决定因素\n      - 早期训练的 activation covariance 尾部可预测下游 token 效率\n      - activation 谱头部运动 + gradient 谱可区分学习侧和执行侧改进\n    vs_ours: >\n      方法论高度相关——同样用频谱分析训练动态。\n      但他们关注优化诊断，不研究 collapse/合成数据退化。\n      可作为方法论参考。\n    threat_level: low\n\n  - id: shi_neurips2025\n    title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n    authors: [Lianghe Shi, Meng Wu, Huijie Zhang, Zekai Zhang, Molei Tao, Qing Qu]\n    year: 2025\n    venue: NeurIPS 2025 (Spotlight)\n    relation: related\n    core_method: >\n      揭示 model collapse 中从泛化到记忆的转变。\n      发现训练数据熵与模型泛化能力的强线性相关。\n      提出基于熵的子集选择方法来减缓 collapse。\n    signals: [dataset entropy, generalization metrics]\n    scale: model-level (data distribution)\n    key_findings:\n      - 迭代训练中数据分布熵急剧下降导致泛化能力下降\n      - 强线性相关：训练数据集熵与模型泛化能力\n      - 熵选择方法有效减缓泛化到记忆转变\n    vs_ours: >\n      他们用数据级别的熵，我们用模型内部的训练动态信号。\n      互补：他们的数据熵可作为我们的外部验证指标。\n      他们不做 per-layer 分析，不做在线监控。\n    threat_level: low\n\n  - id: wyss_2024\n    title: \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\"\n    authors: [C. M. Wyss et al.]\n    year: 2024\n    venue: arXiv (2410.12341)\n    relation: related\n    core_method: >\n      用语义网络和 next-token 概率来表征 LLM 中的 model collapse。\n      引入 collapsed prediction 概念量化多样性损失。\n      分析不同合成 token 比例 (25%/50%/75%) 对 collapse 的影响。\n    signals: [next-token probability distribution, semantic network metrics, collapsed prediction ratio]\n    scale: token-level (output)\n    key_findings:\n      - Next-token 概率分布可精确量化多样性损失\n      - 合成 token 比例越高，collapse 越严重\n      - 跨数据集迁移：在非微调数据集上 collapse 程度不同\n    vs_ours: >\n      他们用输出级指标（next-token prob），我们用训练动态内部信号。\n      他们的 synthetic fraction 实验与我们的实验设计有重叠。\n      不同之处：他们是事后分析，我们是训练中在线监控。\n    threat_level: low\n\n  - id: xu_2026\n    title: \"Predicting LLM Compression Degradation from Spectral Statistics\"\n    authors: [Mingxue Xu]\n    year: 2026\n    venue: arXiv (2604.18085)\n    relation: related\n    core_method: >\n      用 stable rank 和信息密度 (bits/param) 预测 LLM 压缩导致的退化。\n      交互项 compression_ratio * stable_rank 是退化的强预测器。\n    signals: [stable rank, information density, compression ratio]\n    scale: layer-level (attention vs MLP 分开分析)\n    key_findings:\n      - stable rank 是压缩退化的主要预测因子（Pearson r=0.890 attention, 0.839 MLP）\n      - 层类型比压缩方法更重要\n      - layer-specific calibration 优于 method-specific tuning\n    vs_ours: >\n      直接验证 stable rank 作为退化预测信号的有效性。\n      虽然场景不同（压缩 vs collapse），但支持我们选用 stable rank 的合理性。\n      他们的 per-layer 分析方法可参考。\n    threat_level: low\n\n  - id: layer_collapse_diffusion_2026\n    title: \"Layer Collapse in Diffusion Language Models\"\n    authors: [Alexander Conzelmann, Albert Catalan-Tatjer, Shiwei Liu]\n    year: 2026\n    venue: arXiv (2605.06366)\n    relation: related\n    core_method: >\n      分析 diffusion language model (LLaDA-8B) 中的 per-layer activation 动态，\n      发现少数早期层展现 collapsed activation patterns。\n    signals: [activation patterns, super-outlier magnitude]\n    scale: layer-level\n    key_findings:\n      - 几个早期层出现 channel-axis collapse（单一维度主导所有位置）\n      - 尽管看似冗余，pruning outlier 导致退化为重复随机 token 循环\n      - Diffusion LM 与 autoregressive LM 的 collapse 行为不同\n    vs_ours: >\n      做了 per-layer collapse 分析，但在 diffusion LM 上。\n      方法论参考：per-layer activation 分析方法。\n    threat_level: low\n\n  # ===================== FOUNDATION =====================\n\n  - id: alemohammad_iclr2024\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: [Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk]\n    year: 2024\n    venue: ICLR 2024\n    relation: foundation\n    core_method: >\n      定义三种 autophagous loop（fully synthetic / synthetic augmentation / fresh data），\n      证明无足够真实数据时 precision 或 recall 必然下降（MAD 现象）。\n    signals: [FID, precision, recall]\n    scale: model-level (image generative models)\n    key_findings:\n      - 三种 loop 类型的 collapse 行为不同\n      - 无 fresh data 时 quality 或 diversity 必然退化\n      - 在 StyleGAN、DDPM、denoising diffusion 上验证\n    vs_ours: >\n      领域基础论文之一。他们的 loop 分类框架直接对应我们的实验设计。\n      他们用 FID/precision/recall（事后指标），我们提供训练中在线信号。\n\n  - id: papyan_pnas2020\n    title: \"Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training\"\n    authors: [Vardan Papyan, X. Y. Han, David L. Donoho]\n    year: 2020\n    venue: PNAS 117(40), 24652-24663\n    relation: foundation\n    core_method: >\n      发现分类网络训练末期的 Neural Collapse——类内表征收缩到 Simplex ETF。\n    signals: [within-class variability, classifier-mean alignment]\n    scale: model-level (last-layer representations)\n    key_findings:\n      - 训练末期出现四种 collapse 现象\n      - 类均值收敛到 Simplex ETF 顶点\n      - Collapse 与泛化能力相关\n    vs_ours: >\n      虽然 neural collapse 与 model collapse 是不同概念，\n      但谱分析方法论可借鉴，且提供 \"collapse\" 概念的对比参考。\n\n  # ===================== COMPLEMENTARY (Theory/Mitigation) =====================\n\n  - id: shumailov_nature2024\n    title: \"AI Models Collapse When Trained on Recursively Generated Data\"\n    authors: [Ilia Shumailov et al.]\n    year: 2024\n    venue: Nature 631, 755-759\n    relation: foundation\n    core_method: >\n      首次系统性证明迭代合成数据训练导致 model collapse。\n      在 LLM、VAE、GMM 上验证。分布尾部消失是核心机制。\n    signals: [test loss, distribution tail metrics]\n    scale: model-level\n    key_findings:\n      - 迭代训练导致不可逆缺陷：分布尾部消失\n      - 罕见事件最先遗忘\n      - LLM、VAE、GMM 都有此现象\n    vs_ours: >\n      领域基石论文，建立了我们要解决的问题。\n      他们用事后评估（test loss），我们提供在线监控手段。\n\n  - id: dohmatob_iclr2025\n    title: \"Strong Model Collapse\"\n    authors: [Elvis Dohmatob, Yunzhen Feng et al.]\n    year: 2025\n    venue: ICLR 2025 (Spotlight)\n    relation: complementary\n    core_method: >\n      用算子值自由概率论证明即使极小比例的合成数据 (1/1000)\n      也会导致 model collapse，且更大模型放大 collapse。\n    signals: [test error on real data, bias-variance decomposition]\n    scale: model-level\n    key_findings:\n      - 任何非零常数比例的合成数据都导致 collapse\n      - 更大模型可放大 collapse\n      - 神经缩放定律在合成数据下失效\n    vs_ours: >\n      理论基础——解释了为什么需要监控（即使少量合成数据也危险）。\n      他们的 fraction 实验与我们的实验设计直接相关。\n\n  - id: gerstgrasser_2024\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: [Matthias Gerstgrasser, Rylan Schaeffer et al.]\n    year: 2024\n    venue: arXiv (2404.01413)\n    relation: complementary\n    core_method: >\n      证明数据累积（而非替换）可避免 model collapse。\n      替换导致 test error 增长，累积则有有限上界。\n    signals: [test error over iterations]\n    scale: model-level\n    key_findings:\n      - 累积真实+合成数据则无 collapse（所有模型/模态）\n      - 替换数据则 collapse\n      - 关键因素是数据管理策略\n    vs_ours: >\n      互补——他们研究何时 collapse（数据管理策略），\n      我们研究如何实时检测 collapse（训练动态信号）。\n\n  - id: kazdan_2024\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: [Joshua Kazdan et al.]\n    year: 2024\n    venue: arXiv (2410.16713)\n    relation: complementary\n    core_method: >\n      系统比较三种训练工作流：replace（collapse）、\n      accumulate（稳定）、fixed compute（介于两者之间）。\n    signals: [test loss on real data]\n    scale: model-level\n    key_findings:\n      - Replace 工作流一定 collapse\n      - Accumulate 工作流保持稳定\n      - Fixed compute 工作流 loss 升高但 plateau\n    vs_ours: 互补——提供实验设计参考（不同工作流下 collapse 行为差异）。\n\n  - id: seddik_2024\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: [Mohamed El Amine Seddik et al.]\n    year: 2024\n    venue: arXiv (2404.05090)\n    relation: complementary\n    core_method: >\n      统计模型严格刻画不同递归训练场景下的 collapse 程度。\n      给出混合真实/合成数据时避免 collapse 的最大合成数据比例估计。\n    signals: [distribution tail, statistical divergence]\n    scale: model-level\n    key_findings:\n      - 纯合成数据训练无法避免 collapse\n      - 混合训练下存在可计算的合成数据上限\n      - 分布尾部消失是 collapse 的统计特征\n    vs_ours: 理论互补——给出合成数据比例的安全阈值。\n\n  - id: schaeffer_2025\n    title: \"Position: Model Collapse Does Not Mean What You Think\"\n    authors: [Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo]\n    year: 2025\n    venue: arXiv (2503.03150)\n    relation: complementary\n    core_method: >\n      梳理 model collapse 文献中 8 种不同定义，\n      分为三个家族：test loss 行为、分布形变、缩放行为。\n    signals: N/A (position paper)\n    scale: N/A\n    key_findings:\n      - Model collapse 有 8 种不完全一致的定义\n      - 三个家族：test loss 行为、分布形变、缩放定律\n      - 术语混乱阻碍了系统性理解\n    vs_ours: >\n      重要定位参考——论文中需明确使用哪种 collapse 定义。\n      建议采用他们的分类框架。\n\n  - id: feng_iclr2025\n    title: \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\"\n    authors: [Feng et al.]\n    year: 2025\n    venue: ICLR 2025\n    relation: complementary\n    core_method: >\n      用高斯混合+线性分类器+线性验证器推导验证器有效的条件。\n      证明不完美验证器也可有效筛选合成数据。\n    signals: [verifier-based quality score]\n    scale: model-level\n    key_findings:\n      - 验证器筛选合成数据可达到最优性能\n      - 即使不完美验证器也有效\n      - 给出可衡量的代理条件\n    vs_ours: 互补——缓解策略。我们的监控信号可作为验证器的补充。\n\n  - id: yi_2025\n    title: \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\"\n    authors: [Bingji Yi, Qiyuan Liu, Yuwei Cheng, Haifeng Xu]\n    year: 2025\n    venue: arXiv (2510.16657)\n    relation: complementary\n    core_method: >\n      证明外部验证器（人类或更强模型）可阻止 collapse。\n      分析验证器引导下的短期改进和长期收敛行为。\n    signals: [verifier quality score]\n    scale: model-level\n    key_findings:\n      - 外部验证器注入信息则不会 collapse\n      - 短期有改进，长期收敛到验证器的知识中心\n    vs_ours: 互补——缓解策略方向，与监控方向正交。\n\n  - id: bakshi_2026\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: [Soham Bakshi et al.]\n    year: 2026\n    venue: arXiv (2602.10531)\n    relation: complementary\n    core_method: >\n      分析在真实+合成混合数据上的迭代训练动态。\n      next-token prediction 模型下的长期演化分析。\n    signals: [mixture weight, sample size, test performance]\n    scale: model-level\n    key_findings:\n      - 非零真实数据混合权重（即使递减）可避免 collapse\n      - 混合权重和样本量共同控制长期性能\n    vs_ours: 理论互补——刻画迭代训练的长期演化。\n\n  - id: dohmatob_icml2024\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: [Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, Julia Kempe]\n    year: 2024\n    venue: ICML 2024 (pp. 11165-11197)\n    relation: complementary\n    core_method: >\n      从 scaling law 视角分析 collapse——理论框架揭示 collapse 导致 scaling law 改变。\n    signals: [test loss scaling, skill metrics]\n    scale: model-level\n    key_findings:\n      - Loss of scaling、shifted scaling with number of generations\n      - Skill un-learning 现象\n      - 混合人类/合成数据时的 grokking 效应\n    vs_ours: >\n      理论背景——从 scaling law 角度量化 collapse 严重度。\n      我们用训练动态信号在训练中追踪，他们用事后 scaling 分析。\n\n  - id: fu_icml2024\n    title: \"Towards Theoretical Understandings of Self-Consuming Generative Models\"\n    authors: [Shi Fu, Sen Zhang, Yingjie Wang, Xinmei Tian, Dacheng Tao]\n    year: 2024\n    venue: ICML 2024\n    relation: complementary\n    core_method: >\n      构建严格理论框架分析 self-consuming loop 中数据分布演化。\n      分析参数和非参数模型中三种误差源的复合效应。\n    signals: [distribution divergence, error accumulation]\n    scale: model-level\n    key_findings:\n      - 统计/表达/近似三种误差在迭代中复合\n      - 给出误差增长的理论界\n    vs_ours: 理论互补——严格刻画 collapse 的误差复合机制。\n\n  - id: gillman_icml2024\n    title: \"Self-Correcting Self-Consuming Loops for Generative Model Training\"\n    authors: [Nate Gillman, Michael Freeman, Daksh Aggarwal, Chia-Hong Hsu, Calvin Luo, Yonglong Tian, Chen Sun]\n    year: 2024\n    venue: ICML 2024\n    relation: complementary\n    core_method: >\n      引入 correction function 使 self-consuming loop 指数级更稳定。\n      在人体运动合成任务上验证。\n    signals: [corrector quality, loop stability]\n    scale: model-level\n    key_findings:\n      - Correction function 使 loop 指数级稳定\n      - 即使 synthetic:real = 100:1 也可避免 collapse\n    vs_ours: 互补——缓解策略，correction function 概念与在线监控互补。\n\n  # ===================== DATA CONTAMINATION DETECTION =====================\n\n  - id: kirchenbauer_icml2023\n    title: \"A Watermark for Large Language Models\"\n    authors: [John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, Tom Goldstein]\n    year: 2023\n    venue: ICML 2023 (pp. 17061-17084)\n    relation: complementary\n    core_method: >\n      LLM 文本水印框架——green/red token list + soft promotion + 统计检测。\n    signals: [green token ratio, z-score]\n    scale: token-level (output)\n    key_findings:\n      - 可嵌入统计可检测水印且不影响文本质量\n      - 开源检测算法不需模型访问\n    vs_ours: 合成数据溯源的基础方法，与 collapse 检测互补。\n\n  - id: dathathri_nature2024\n    title: \"Scalable Watermarking for Identifying Large Language Model Outputs\"\n    authors: [Sumanth Dathathri, Abigail See, Sumedh Ghaisas et al.]\n    year: 2024\n    venue: Nature 634, 818-823\n    relation: complementary\n    core_method: >\n      SynthID-Text：产品级文本水印，与 speculative sampling 集成。\n      在 Gemini ~20M 响应上验证。\n    signals: [watermark detection score]\n    scale: token-level (output)\n    key_findings:\n      - 产品级规模的水印部署\n      - 不影响文本质量，最小延迟开销\n    vs_ours: 大规模合成数据标记的工业实践，与监控方向互补。\n\n  - id: sander_neurips2024\n    title: \"Watermarking Makes Language Models Radioactive\"\n    authors: [Tom Sander, Pierre Fernandez, Alain Durmus, Matthijs Douze, Teddy Furon]\n    year: 2024\n    venue: NeurIPS 2024\n    relation: related\n    core_method: >\n      证明在水印 LLM 输出上微调的模型保留水印残留（\"放射性\"）。\n    signals: [watermark residual in fine-tuned model]\n    scale: model-level\n    key_findings:\n      - 水印信号通过训练传播到下游模型\n      - 可检测模型是否在合成数据上训练\n    vs_ours: >\n      直接相关——检测合成数据训练的替代方法。\n      他们检测\"是否用了合成数据\"，我们监控\"合成数据造成多严重的 collapse\"。\n\n  - id: mitchell_icml2023\n    title: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\n    authors: [Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn]\n    year: 2023\n    venue: ICML 2023 (pp. 24950-24962)\n    relation: complementary\n    core_method: >\n      LLM 生成文本占据 log-probability 负曲率区域，据此零样本检测。\n    signals: [log probability curvature]\n    scale: text-level\n    key_findings:\n      - 生成文本的概率曲率特征可区分人类/机器文本\n      - 0.95 AUROC 检测 GPT-NeoX 20B 生成的假新闻\n    vs_ours: 合成文本检测方法，可识别训练数据中的合成成分。\n\n  - id: shi_iclr2024\n    title: \"Detecting Pretraining Data from Large Language Models\"\n    authors: [Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer]\n    year: 2024\n    venue: ICLR 2024\n    relation: related\n    core_method: >\n      Min-K% Prob：未见样本含低概率 outlier word，据此检测预训练数据成员。\n    signals: [Min-K% probability score]\n    scale: text-level\n    key_findings:\n      - 比 reference model 方法提升 7.4%\n      - 适用于版权检测、污染检测、隐私审计\n    vs_ours: 数据污染检测工具——可检测合成数据是否混入训练集，与 collapse 监控互补。\n\n  # ===================== METHODOLOGICAL FOUNDATIONS =====================\n\n  - id: martin_mahoney_2021\n    title: \"Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data\"\n    authors: [Charles H. Martin, Michael W. Mahoney]\n    year: 2021\n    venue: Nature Communications 12\n    relation: complementary\n    core_method: >\n      WeightWatcher 工具——用 RMT 分析权重矩阵的谱性质，\n      无需训练/测试数据即可预测模型质量。\n    signals: [stable rank, power law exponent (alpha), spectral norm]\n    scale: layer-level (per weight matrix)\n    key_findings:\n      - stable rank 追踪自正则化程度\n      - 5+1 训练阶段对应不同的谱形态\n      - heavy-tailed 分布特征区分好/差模型\n    vs_ours: >\n      方法论基础——WeightWatcher 的 stable rank 和谱分析方法\n      直接启发我们的信号设计。\n\n  - id: yunis_2024\n    title: \"Approaching Deep Learning through the Spectral Dynamics of Weights\"\n    authors: [David Yunis, Kumar Kshitij Patel et al.]\n    year: 2024\n    venue: arXiv (2408.11804)\n    relation: complementary\n    core_method: >\n      以权重奇异值/向量的动态演化为核心视角理解深度学习。\n      证明谱动态可区分记忆网络和泛化网络。\n    signals: [singular value dynamics, singular vector alignment]\n    scale: layer-level (per weight matrix)\n    key_findings:\n      - 权重衰减增强低秩偏置\n      - 谱动态区分记忆 vs 泛化\n      - 与 lottery ticket 和 loss surface 结构相关\n    vs_ours: 方法论基础——谱动态视角可用于理解 collapse 过程中的权重变化。\n\n  - id: chen_liu_2024\n    title: \"Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy\"\n    authors: [Chen Liu et al.]\n    year: 2024\n    venue: IEEE CISS 2024\n    relation: complementary\n    core_method: >\n      提出 Diffusion Spectral Entropy (DSE) 和 Diffusion Spectral Mutual Information (DSMI)，\n      利用数据几何在高维中可靠计算信息论指标。\n    signals: [DSE, DSMI]\n    scale: layer-level (representations)\n    key_findings:\n      - DSE 在训练中增加\n      - DSMI(class label) 在泛化学习中增加，过拟合时停滞\n      - 可用于指导网络初始化和预测下游准确率\n    vs_ours: >\n      方法论工具——DSE 是我们 spectral entropy 信号的潜在替代实现。\n\n  - id: lu_neurips2024\n    title: \"AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models\"\n    authors: [Haiquan Lu, Yefan Zhou, Shiwei Liu, Zhangyang Wang, Michael W. Mahoney, Yaoqing Yang]\n    year: 2024\n    venue: NeurIPS 2024\n    relation: complementary\n    core_method: >\n      用 HT-SR 理论的谱密度形态（alpha exponent）指导 LLM 层级剪枝。\n    signals: [alpha exponent, ESD shape metrics]\n    scale: layer-level\n    key_findings:\n      - Alpha exponent 有效指导 per-layer 剪枝比例\n      - LLaMA-7B 可剪至 80% sparsity 保持合理 perplexity\n    vs_ours: >\n      验证 per-layer 谱分析对 LLM 质量评估的有效性。\n      支持我们用类似方法监控 collapse。\n\n  - id: sanyal_iclr2020\n    title: \"Stable Rank Normalization for Improved Generalization in Neural Networks and GANs\"\n    authors: [Amartya Sanyal, Philip H. S. Torr, Puneet K. Dokania]\n    year: 2020\n    venue: ICLR 2020\n    relation: complementary\n    core_method: >\n      提出 stable rank normalization——最小化线性算子的 stable rank。\n      理论证明唯一最优解，实验验证改善泛化。\n    signals: [stable rank, Lipschitz constant]\n    scale: layer-level\n    key_findings:\n      - 控制 stable rank 改善泛化 gap 11.3%\n      - Stable rank 与泛化能力直接关联\n    vs_ours: >\n      理论支持——建立 stable rank 与泛化的直接联系。\n      支持我们选用 stable rank 作为 collapse（泛化退化）的监控信号。\n\n  - id: kalra_2026\n    title: \"A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs\"\n    authors: [Dayal Singh Kalra, Jean-Christophe Gagnon-Audet, Andrey Gromov, Ishita Mediratta, Kelvin Niu, Alexander H. Miller, Michael Shvartsman]\n    year: 2026\n    venue: arXiv (2601.16979)\n    relation: related\n    core_method: >\n      Critical sharpness：<10 forward passes 高效度量 loss landscape 曲率。\n      首次在 7B 规模验证 progressive sharpening 和 Edge of Stability。\n    signals: [critical sharpness, relative critical sharpness]\n    scale: model-level\n    key_findings:\n      - Progressive sharpening 在 7B 规模仍然存在\n      - Critical sharpness 可指导 pre-train 到 fine-tune 的数据混合\n    vs_ours: >\n      训练动态监控方法论参考——高效的大规模 LLM 训练动态度量。\n      Critical sharpness 可作为我们信号集的潜在补充。\n\n  # ===================== DATA QUALITY =====================\n\n  - id: penedo_2024\n    title: \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\"\n    authors: [Guilherme Penedo, Hynek Kydlicek, Loubna Ben allal, Anton Lozhkov, Margaret Mitchell, Colin Raffel, Leandro Von Werra, Thomas Wolf]\n    year: 2024\n    venue: arXiv (2406.17557)\n    relation: complementary\n    core_method: >\n      15T token 数据集的完整策略文档——去重、过滤、教育文本提取。\n    signals: [data quality classifiers, deduplication metrics]\n    scale: dataset-level\n    key_findings:\n      - 详细 ablation 各种去重和过滤策略\n      - FineWeb-Edu 在知识密集任务上大幅提升性能\n    vs_ours: 数据质量策略参考——理解高质量训练数据标准，为分析 collapse 的数据原因提供基线。\n\n  - id: zhang_2026\n    title: \"The LLM Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data\"\n    authors: [Kaituo Zhang, Mingzhi Hu, Hoang Anh Duy Le et al.]\n    year: 2026\n    venue: arXiv (2601.17717)\n    relation: complementary\n    core_method: >\n      系统分类合成数据评估指标——quality (validity/fidelity/utility) +\n      trustworthiness (safety/faithfulness)。\n    signals: [quality metrics taxonomy, trustworthiness metrics]\n    scale: dataset-level\n    key_findings:\n      - 从内在属性评估合成数据，而非仅看下游性能\n      - 质量和可信度两个维度的完整分类体系\n    vs_ours: 合成数据质量评估框架——为理解 collapse 的数据级原因提供指标体系。\n\n# ============================================================\n# 关键发现总结\n# ============================================================\n\nsummary:\n  total_papers: 34\n  direct_competitors: 2  # SIGMA, Kalinowski\n  novelty_confirmation: >\n    在 34 篇文献中，没有工作同时做到：(a) 训练中在线监控 (b) 用频谱/熵训练动态信号\n    (c) per-layer 粒度 (d) 在迭代合成数据训练场景下验证。\n    我们的核心新颖性空间依然存在。\n\n  coverage:\n    model_collapse_theory: 14  # shumailov, dohmatob x2, alemohammad, fu, gerstgrasser, seddik, kazdan, schaeffer, bakshi, shi_neurips2025, feng, yi, gillman\n    data_contamination: 5  # kirchenbauer, dathathri, sander, mitchell, shi_iclr2024\n    spectral_methods: 8  # sigma, martin_mahoney, yunis, lu, sanyal, spectral_lens, xu, conzelmann\n    training_dynamics: 4  # kalinowski, chen_liu, kalra, papyan\n    data_quality: 3  # wyss, penedo, zhang\n\n  gap_analysis:\n    sigma: >\n      用输出嵌入 Gram 矩阵谱——事后/黑盒，不做 per-layer，不跟踪训练过程。\n    kalinowski: >\n      用拓扑信号——在线但信号族不同，不研究迭代合成数据场景。\n    our_unique_position: >\n      训练动态频谱/熵信号 + per-layer 粒度 + 迭代合成数据场景 = 独特定位。\n\n  per_layer_collapse_analysis:\n    papers_with_per_layer:\n      - layer_collapse_diffusion_2026  # diffusion LM per-layer activation collapse\n      - xu_2026  # stable rank per-layer（compression 场景）\n      - spectral_lens_2026  # per-layer activation/gradient 谱\n      - lu_neurips2024  # alpha exponent per-layer for pruning\n    gap: \"无论文在迭代合成数据训练中做 per-layer collapse 分析\"\n\n  stable_rank_as_collapse_signal:\n    papers_using_stable_rank:\n      - martin_mahoney_2021  # WeightWatcher 中作为模型质量指标\n      - xu_2026  # 压缩退化预测器 (r=0.89)\n      - yunis_2024  # 谱动态中的低秩偏置\n      - sanyal_iclr2020  # stable rank 与泛化的直接联系\n    gap: \"无论文直接用 stable rank 监控 iterative synthetic data collapse\"\n\n  spectral_entropy_as_collapse_signal:\n    papers_using_spectral_entropy:\n      - chen_liu_2024  # DSE 跟踪训练动态\n      - sigma_2026  # 谱分析但在 Gram 矩阵上\n    gap: \"无论文直接用 weight spectral entropy 监控 collapse\"\n\n  synthetic_fraction_effects:\n    papers_studying_fraction:\n      - dohmatob_iclr2025  # 理论：任何非零 fraction 都危险\n      - dohmatob_icml2024  # scaling law 角度的 fraction 分析\n      - alemohammad_iclr2024  # 三种 loop 类型的不同效果\n      - wyss_2024  # 实证：25%/50%/75% 不同 collapse 程度\n      - seddik_2024  # 统计：给出安全上限估计\n    gap: \"大量理论/实证工作，但都用事后指标衡量 fraction 效果\"\n\n  data_contamination_detection:\n    papers:\n      - kirchenbauer_icml2023  # 基础水印方法\n      - dathathri_nature2024  # 产品级水印 (SynthID)\n      - sander_neurips2024  # 水印放射性传播\n      - mitchell_icml2023  # DetectGPT 概率曲率检测\n      - shi_iclr2024  # Min-K% 预训练数据检测\n    relevance: >\n      合成数据检测与 collapse 监控互补：他们回答\"是否有合成数据\"，\n      我们回答\"合成数据造成了多严重的 collapse\"。\n",
      "numLines": 709,
      "startLine": 1,
      "totalLines": 709
    }
  },
  "sourceToolAssistantUUID": "f0fa6465-dc3b-4eab-8ff7-c3586f7647d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T22:47:38.663Z_

<details><summary>↩ Tool result · `toolu_01RUU9aELSmQ1pumL831kfBs`</summary>

```text
1	# Related Work 结构大纲
2	
3	> **项目**: collapse_severity_monitor — 在线监控模型 collapse 严重度
4	> **目标会议**: EMNLP 2026 ARR
5	> **基于**: literature_map.yaml (19 篇) + 1 篇补充 (Alemohammad 2024)
6	
7	---
8	
9	## A. Model Collapse: 理论基础与实证
10	
11	Model collapse 指在合成数据上迭代训练导致模型质量不可逆退化的现象。自 Shumailov et al. (2024) 在 Nature 上首次系统性证明以来，理论和实证研究迅速发展，从分布尾部消失、缩放定律失效到术语统一均有深入探讨。我们的工作建立在这些理论基础之上，旨在提供训练过程中的实时监控手段。
12	
13	| # | 论文 | ID | 核心贡献 | 与我们的关系 |
14	|---|------|----|----------|-------------|
15	| 1 | **Shumailov et al.** "AI Models Collapse When Trained on Recursively Generated Data." *Nature* 631, 755–759, 2024. | `shumailov_nature2024` | 首次系统证明迭代合成数据训练导致 model collapse（LLM/VAE/GMM），核心机制为分布尾部消失。 | **领域基石**。定义了我们要解决的问题；他们用事后评估（test loss），我们提供在线监控。 |
16	| 2 | **Alemohammad et al.** "Self-Consuming Generative Models Go MAD." *ICLR 2024*. (arXiv: 2307.01850) | ⚠️ **需补入 literature_map.yaml** | 提出 Model Autophagy Disorder (MAD) 框架，分析三类自噬循环（fully synthetic / synthetic augmentation / fresh data）下质量-多样性退化。 | **理论基础**。MAD 框架为我们的迭代合成数据实验设计提供了分类学；他们证明无足够真实数据则 precision 或 recall 必退化。 |
17	| 3 | **Dohmatob, Feng et al.** "Strong Model Collapse." *ICLR 2025 (Spotlight)*. | `dohmatob_iclr2025` | 用算子值自由概率论证明即使极小比例（1/1000）合成数据也导致 collapse，且更大模型放大 collapse。 | **理论支撑**。解释了为什么需要监控——即使少量合成数据也危险；其 fraction 实验与我们的实验设计直接相关。 |
18	| 4 | **Seddik et al.** "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse." *arXiv 2404.05090*, 2024. | `seddik_2024` | 统计模型严格刻画不同递归训练场景下的 collapse 程度，给出混合训练下合成数据比例安全上限。 | **理论互补**。提供合成数据比例的安全阈值估计，可与我们的监控信号阈值对照验证。 |
19	| 5 | **Schaeffer, Kazdan et al.** "Position: Model Collapse Does Not Mean What You Think." *arXiv 2503.03150*, 2025. | `schaeffer_2025` | 梳理 collapse 文献中 8 种不同定义，分为三个家族：test loss 行为、分布形变、缩放行为。 | **定位参考**。论文中需明确我们采用的 collapse 定义；建议采用他们的分类框架。 |
20	| 6 | **Shi et al.** "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective." *NeurIPS 2025 (Spotlight)*. | `shi_neurips2025` | 揭示 collapse 中从泛化到记忆的转变，发现训练数据熵与泛化能力强线性相关。 | **互补视角**。他们用数据级熵，我们用模型内部训练动态信号；其数据熵可作为我们的外部验证指标。 |
21	| 7 | **Bakshi et al.** "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources." *arXiv 2602.10531*, 2026. | `bakshi_2026` | 分析真实+合成混合数据的迭代训练长期演化动态，非零真实数据权重（即使递减）可避免 collapse。 | **理论互补**。刻画迭代训练的长期演化规律，为我们的多轮实验设计提供理论预期。 |
22	
23	---
24	
25	## B. Collapse 检测与监控方法
26	
27	现有 collapse 检测方法主要分为事后评估（test loss、分布指标）和在线监控两类。直接竞争者包括基于谱分析的 SIGMA 和基于拓扑信号的 Kalinowski 方法。**我们的独特定位**：在线 + 频谱/熵训练动态信号 + per-layer 粒度 + 迭代合成数据场景，这一组合目前无人覆盖。
28	
29	| # | 论文 | ID | 核心贡献 | 与我们的关系 |
30	|---|------|----|----------|-------------|
31	| 1 | **Azam et al.** "SIGMA: Scalable Spectral Insights for LLM Model Collapse." *arXiv 2601.03385*, 2026. | `sigma_2026` | 通过 embedding Gram 矩阵的谱分析量化 collapse，推导谱收缩的确定性和随机性界。 | **直接竞争者**。SIGMA 是事后/黑盒方法（用输出嵌入 Gram 矩阵），不需要模型权重，不做 per-layer 分析，不跟踪训练过程动态变化。我们是训练中实时监控，更早期更细粒度。 |
32	| 2 | **Kalinowski.** "Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index." *arXiv 2604.26984*, 2026. | `kalinowski_2026` | 提出在线拓扑感知监控器（MMHM + Collapse Index），通过稀疏增量更新实现快速在线监控。 | **直接竞争者**。同为在线监控，但信号族完全不同（拓扑 vs 频谱/熵）。我们的信号更轻量、更可解释（stable rank/spectral entropy 有直接线性代数含义）。Kalinowski 不研究迭代合成数据场景。 |
33	| 3 | **Wyss et al.** "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI." *arXiv 2410.12341*, 2024. | `wyss_2024` | 用语义网络和 next-token 概率表征 collapse，引入 collapsed prediction 概念量化多样性损失。 | **相关方法**。用输出级指标（next-token prob），属事后分析；其 synthetic fraction 实验（25%/50%/75%）与我们的实验设计有重叠，可作为 baseline 指标。 |
34	
35	### 我们的定位（论文中需强调）
36	
37	> 现有方法要么是事后/黑盒分析（SIGMA），要么用非频谱信号（Kalinowski 的拓扑方法），要么仅关注输出级指标（Wyss）。本工作首次将频谱/熵训练动态信号（spectral entropy、stable rank、output token entropy）以 per-layer 粒度应用于迭代合成数据训练中的在线 collapse 监控。
38	
39	---
40	
41	## C. 训练动态分析与诊断
42	
43	频谱分析和训练动态诊断是深度学习中成熟的研究方向。WeightWatcher 等工具已证明权重矩阵的谱性质（stable rank、power law exponent）可有效评估模型质量。我们将这些方法论工具从通用训练诊断延伸到 collapse 监控这一特定场景。
44	
45	| # | 论文 | ID | 核心贡献 | 与我们的关系 |
46	|---|------|----|----------|-------------|
47	| 1 | **Martin & Mahoney.** "Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data." *Nature Communications* 12, 2021. | `martin_mahoney_2021` | WeightWatcher 工具——用 RMT 分析权重矩阵谱性质（stable rank、power law α、spectral norm），无需训练/测试数据即可预测模型质量。 | **方法论基础**。WeightWatcher 的 stable rank 和谱分析方法直接启发我们的信号设计；其 5+1 训练阶段分类可用于解释 collapse 过程中的谱形态变化。 |
48	| 2 | **Liu et al. (Spectral Lens).** "Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization." *arXiv 2605.05683*, 2026. | `spectral_lens_2026` | 用 activation covariance 和 per-sample gradient 的 SVD 谱作为 LLM 训练优化诊断工具。 | **方法论高度相关**。同样用频谱分析训练动态，但关注优化诊断而非 collapse/合成数据退化；其 per-layer 分析方法可参考。 |
49	| 3 | **Chen & Liu.** "Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy." *IEEE CISS 2024*. | `chen_liu_2024` | 提出 Diffusion Spectral Entropy (DSE) 和 DSMI，利用数据几何在高维中可靠计算信息论指标。 | **方法论工具**。DSE 是我们 spectral entropy 信号的潜在替代实现；其 DSE 随训练增加、DSMI 在过拟合时停滞的发现可为 collapse 检测提供参照。 |
50	| 4 | **Yunis, Patel et al.** "Approaching Deep Learning through the Spectral Dynamics of Weights." *arXiv 2408.11804*, 2024. | `yunis_2024` | 以权重奇异值/向量的动态演化为核心视角，证明谱动态可区分记忆网络和泛化网络。 | **方法论基础**。谱动态视角可用于理解 collapse 过程中的权重变化；权重衰减增强低秩偏置的发现与 collapse 中的秩退化相关。 |
51	| 5 | **Xu.** "Predicting LLM Compression Degradation from Spectral Statistics." *arXiv 2604.18085*, 2026. | `xu_2026` | 用 stable rank 和信息密度预测 LLM 压缩退化（Pearson r=0.890 attention, 0.839 MLP），per-layer 分析。 | **信号验证**。直接验证 stable rank 作为退化预测信号的有效性；虽场景不同（压缩 vs collapse），但支持我们选用 stable rank 的合理性。 |
52	| 6 | **Conzelmann et al.** "Layer Collapse in Diffusion Language Models." *arXiv 2605.06366*, 2026. | `layer_collapse_diffusion_2026` | 分析 diffusion LM (LLaDA-8B) 中 per-layer activation collapse，发现少数早期层出现 channel-axis collapse。 | **方法论参考**。做了 per-layer collapse 分析，但在 diffusion LM 上；其 activation 分析方法可参考，但场景和模型架构不同。 |
53	
54	---
55	
56	## D. Collapse 缓解策略
57	
58	缓解策略主要分为数据管理（累积 vs 替换、混合比例控制）和数据筛选/验证两类。这些工作与我们的监控方向互补——我们负责检测 collapse 何时发生及严重程度，它们负责干预和缓解。
59	
60	| # | 论文 | ID | 核心贡献 | 与我们的关系 |
61	|---|------|----|----------|-------------|
62	| 1 | **Gerstgrasser, Schaeffer et al.** "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data." *arXiv 2404.01413*, 2024. | `gerstgrasser_2024` | 证明数据累积（而非替换）可避免 collapse；替换导致 test error 增长，累积则有有限上界。 | **互补**。他们研究何时 collapse（数据管理策略），我们研究如何实时检测 collapse；累积 vs 替换的差异可作为我们监控信号的验证场景。 |
63	| 2 | **Kazdan et al.** "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World." *arXiv 2410.16713*, 2024. | `kazdan_2024` | 系统比较三种工作流：replace（collapse）、accumulate（稳定）、fixed compute（plateau）。 | **互补**。提供实验设计参考——不同工作流下 collapse 行为差异，可用于验证我们的监控信号在不同设定下的灵敏度。 |
64	| 3 | **Feng et al.** "Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification." *ICLR 2025*. | `feng_iclr2025` | 用高斯混合模型推导验证器有效的条件，证明即使不完美的验证器也可有效筛选合成数据。 | **互补**。缓解策略方向；我们的监控信号可作为验证器的补充或替代——当 collapse 信号超过阈值时触发干预。 |
65	| 4 | **Yi et al.** "Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence." *arXiv 2510.16657*, 2025. | `yi_2025` | 证明外部验证器（人类或更强模型）可阻止 collapse，分析短期改进和长期收敛行为。 | **互补**。与监控方向正交；我们的贡献在于提供何时需要启动验证/干预的信号。 |
66	
67	---
68	
69	## 覆盖检查
70	
71	### literature_map.yaml 全部 19 篇论文分配
72	
73	| ID | 类别 |
74	|----|------|
75	| `shumailov_nature2024` | A |
76	| `dohmatob_iclr2025` | A |
77	| `seddik_2024` | A |
78	| `schaeffer_2025` | A |
79	| `shi_neurips2025` | A |
80	| `bakshi_2026` | A |
81	| `sigma_2026` | B |
82	| `kalinowski_2026` | B |
83	| `wyss_2024` | B |
84	| `martin_mahoney_2021` | C |
85	| `spectral_lens_2026` | C |
86	| `chen_liu_2024` | C |
87	| `yunis_2024` | C |
88	| `xu_2026` | C |
89	| `layer_collapse_diffusion_2026` | C |
90	| `gerstgrasser_2024` | D |
91	| `kazdan_2024` | D |
92	| `feng_iclr2025` | D |
93	| `yi_2025` | D |
94	
95	### 需补入 literature_map.yaml 的论文
96	
97	- **Alemohammad et al. (2024)** "Self-Consuming Generative Models Go MAD." ICLR 2024. arXiv: 2307.01850
98	  - 分类至 A（理论基础）
99	  - relation: foundation
100	  - 建议 id: `alemohammad_iclr2024`
101	
102	---
103	
104	## 论文写作备注
105	
106	1. **开篇逻辑**: A → B → C → D，从"问题是什么"到"谁在检测"到"用什么工具"到"如何缓解"
107	2. **核心 positioning 句**: "To the best of our knowledge, no prior work simultaneously achieves (a) online monitoring during training, (b) spectral/entropy training dynamics signals, (c) per-layer granularity, and (d) validation in the iterative synthetic data training setting."
108	3. **Collapse 定义**: 采用 Schaeffer et al. (2025) 的分类框架，明确我们关注的是 test loss degradation + distribution tail collapse
109	4. **Alemohammad 2024 必须引用**: Reviewer 之前指出缺失，与 Shumailov 2024 共同构成问题定义的基石
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b774d17-469d-49f8-a2bb-6987a3d63be8",
  "isSidechain": false,
  "promptId": "6d40a60b-3de6-4cba-96cf-f662df5975d1",
  "type": "user",
  "uuid": "104e82e5-b2c4-4f44-8617-4f3927f508d5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/docs/related_work_outline.md",
      "content": "# Related Work 结构大纲\n\n> **项目**: collapse_severity_monitor — 在线监控模型 collapse 严重度\n> **目标会议**: EMNLP 2026 ARR\n> **基于**: literature_map.yaml (19 篇) + 1 篇补充 (Alemohammad 2024)\n\n---\n\n## A. Model Collapse: 理论基础与实证\n\nModel collapse 指在合成数据上迭代训练导致模型质量不可逆退化的现象。自 Shumailov et al. (2024) 在 Nature 上首次系统性证明以来，理论和实证研究迅速发展，从分布尾部消失、缩放定律失效到术语统一均有深入探讨。我们的工作建立在这些理论基础之上，旨在提供训练过程中的实时监控手段。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Shumailov et al.** \"AI Models Collapse When Trained on Recursively Generated Data.\" *Nature* 631, 755–759, 2024. | `shumailov_nature2024` | 首次系统证明迭代合成数据训练导致 model collapse（LLM/VAE/GMM），核心机制为分布尾部消失。 | **领域基石**。定义了我们要解决的问题；他们用事后评估（test loss），我们提供在线监控。 |\n| 2 | **Alemohammad et al.** \"Self-Consuming Generative Models Go MAD.\" *ICLR 2024*. (arXiv: 2307.01850) | ⚠️ **需补入 literature_map.yaml** | 提出 Model Autophagy Disorder (MAD) 框架，分析三类自噬循环（fully synthetic / synthetic augmentation / fresh data）下质量-多样性退化。 | **理论基础**。MAD 框架为我们的迭代合成数据实验设计提供了分类学；他们证明无足够真实数据则 precision 或 recall 必退化。 |\n| 3 | **Dohmatob, Feng et al.** \"Strong Model Collapse.\" *ICLR 2025 (Spotlight)*. | `dohmatob_iclr2025` | 用算子值自由概率论证明即使极小比例（1/1000）合成数据也导致 collapse，且更大模型放大 collapse。 | **理论支撑**。解释了为什么需要监控——即使少量合成数据也危险；其 fraction 实验与我们的实验设计直接相关。 |\n| 4 | **Seddik et al.** \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse.\" *arXiv 2404.05090*, 2024. | `seddik_2024` | 统计模型严格刻画不同递归训练场景下的 collapse 程度，给出混合训练下合成数据比例安全上限。 | **理论互补**。提供合成数据比例的安全阈值估计，可与我们的监控信号阈值对照验证。 |\n| 5 | **Schaeffer, Kazdan et al.** \"Position: Model Collapse Does Not Mean What You Think.\" *arXiv 2503.03150*, 2025. | `schaeffer_2025` | 梳理 collapse 文献中 8 种不同定义，分为三个家族：test loss 行为、分布形变、缩放行为。 | **定位参考**。论文中需明确我们采用的 collapse 定义；建议采用他们的分类框架。 |\n| 6 | **Shi et al.** \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective.\" *NeurIPS 2025 (Spotlight)*. | `shi_neurips2025` | 揭示 collapse 中从泛化到记忆的转变，发现训练数据熵与泛化能力强线性相关。 | **互补视角**。他们用数据级熵，我们用模型内部训练动态信号；其数据熵可作为我们的外部验证指标。 |\n| 7 | **Bakshi et al.** \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources.\" *arXiv 2602.10531*, 2026. | `bakshi_2026` | 分析真实+合成混合数据的迭代训练长期演化动态，非零真实数据权重（即使递减）可避免 collapse。 | **理论互补**。刻画迭代训练的长期演化规律，为我们的多轮实验设计提供理论预期。 |\n\n---\n\n## B. Collapse 检测与监控方法\n\n现有 collapse 检测方法主要分为事后评估（test loss、分布指标）和在线监控两类。直接竞争者包括基于谱分析的 SIGMA 和基于拓扑信号的 Kalinowski 方法。**我们的独特定位**：在线 + 频谱/熵训练动态信号 + per-layer 粒度 + 迭代合成数据场景，这一组合目前无人覆盖。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Azam et al.** \"SIGMA: Scalable Spectral Insights for LLM Model Collapse.\" *arXiv 2601.03385*, 2026. | `sigma_2026` | 通过 embedding Gram 矩阵的谱分析量化 collapse，推导谱收缩的确定性和随机性界。 | **直接竞争者**。SIGMA 是事后/黑盒方法（用输出嵌入 Gram 矩阵），不需要模型权重，不做 per-layer 分析，不跟踪训练过程动态变化。我们是训练中实时监控，更早期更细粒度。 |\n| 2 | **Kalinowski.** \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index.\" *arXiv 2604.26984*, 2026. | `kalinowski_2026` | 提出在线拓扑感知监控器（MMHM + Collapse Index），通过稀疏增量更新实现快速在线监控。 | **直接竞争者**。同为在线监控，但信号族完全不同（拓扑 vs 频谱/熵）。我们的信号更轻量、更可解释（stable rank/spectral entropy 有直接线性代数含义）。Kalinowski 不研究迭代合成数据场景。 |\n| 3 | **Wyss et al.** \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI.\" *arXiv 2410.12341*, 2024. | `wyss_2024` | 用语义网络和 next-token 概率表征 collapse，引入 collapsed prediction 概念量化多样性损失。 | **相关方法**。用输出级指标（next-token prob），属事后分析；其 synthetic fraction 实验（25%/50%/75%）与我们的实验设计有重叠，可作为 baseline 指标。 |\n\n### 我们的定位（论文中需强调）\n\n> 现有方法要么是事后/黑盒分析（SIGMA），要么用非频谱信号（Kalinowski 的拓扑方法），要么仅关注输出级指标（Wyss）。本工作首次将频谱/熵训练动态信号（spectral entropy、stable rank、output token entropy）以 per-layer 粒度应用于迭代合成数据训练中的在线 collapse 监控。\n\n---\n\n## C. 训练动态分析与诊断\n\n频谱分析和训练动态诊断是深度学习中成熟的研究方向。WeightWatcher 等工具已证明权重矩阵的谱性质（stable rank、power law exponent）可有效评估模型质量。我们将这些方法论工具从通用训练诊断延伸到 collapse 监控这一特定场景。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Martin & Mahoney.** \"Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data.\" *Nature Communications* 12, 2021. | `martin_mahoney_2021` | WeightWatcher 工具——用 RMT 分析权重矩阵谱性质（stable rank、power law α、spectral norm），无需训练/测试数据即可预测模型质量。 | **方法论基础**。WeightWatcher 的 stable rank 和谱分析方法直接启发我们的信号设计；其 5+1 训练阶段分类可用于解释 collapse 过程中的谱形态变化。 |\n| 2 | **Liu et al. (Spectral Lens).** \"Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization.\" *arXiv 2605.05683*, 2026. | `spectral_lens_2026` | 用 activation covariance 和 per-sample gradient 的 SVD 谱作为 LLM 训练优化诊断工具。 | **方法论高度相关**。同样用频谱分析训练动态，但关注优化诊断而非 collapse/合成数据退化；其 per-layer 分析方法可参考。 |\n| 3 | **Chen & Liu.** \"Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy.\" *IEEE CISS 2024*. | `chen_liu_2024` | 提出 Diffusion Spectral Entropy (DSE) 和 DSMI，利用数据几何在高维中可靠计算信息论指标。 | **方法论工具**。DSE 是我们 spectral entropy 信号的潜在替代实现；其 DSE 随训练增加、DSMI 在过拟合时停滞的发现可为 collapse 检测提供参照。 |\n| 4 | **Yunis, Patel et al.** \"Approaching Deep Learning through the Spectral Dynamics of Weights.\" *arXiv 2408.11804*, 2024. | `yunis_2024` | 以权重奇异值/向量的动态演化为核心视角，证明谱动态可区分记忆网络和泛化网络。 | **方法论基础**。谱动态视角可用于理解 collapse 过程中的权重变化；权重衰减增强低秩偏置的发现与 collapse 中的秩退化相关。 |\n| 5 | **Xu.** \"Predicting LLM Compression Degradation from Spectral Statistics.\" *arXiv 2604.18085*, 2026. | `xu_2026` | 用 stable rank 和信息密度预测 LLM 压缩退化（Pearson r=0.890 attention, 0.839 MLP），per-layer 分析。 | **信号验证**。直接验证 stable rank 作为退化预测信号的有效性；虽场景不同（压缩 vs collapse），但支持我们选用 stable rank 的合理性。 |\n| 6 | **Conzelmann et al.** \"Layer Collapse in Diffusion Language Models.\" *arXiv 2605.06366*, 2026. | `layer_collapse_diffusion_2026` | 分析 diffusion LM (LLaDA-8B) 中 per-layer activation collapse，发现少数早期层出现 channel-axis collapse。 | **方法论参考**。做了 per-layer collapse 分析，但在 diffusion LM 上；其 activation 分析方法可参考，但场景和模型架构不同。 |\n\n---\n\n## D. Collapse 缓解策略\n\n缓解策略主要分为数据管理（累积 vs 替换、混合比例控制）和数据筛选/验证两类。这些工作与我们的监控方向互补——我们负责检测 collapse 何时发生及严重程度，它们负责干预和缓解。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Gerstgrasser, Schaeffer et al.** \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data.\" *arXiv 2404.01413*, 2024. | `gerstgrasser_2024` | 证明数据累积（而非替换）可避免 collapse；替换导致 test error 增长，累积则有有限上界。 | **互补**。他们研究何时 collapse（数据管理策略），我们研究如何实时检测 collapse；累积 vs 替换的差异可作为我们监控信号的验证场景。 |\n| 2 | **Kazdan et al.** \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World.\" *arXiv 2410.16713*, 2024. | `kazdan_2024` | 系统比较三种工作流：replace（collapse）、accumulate（稳定）、fixed compute（plateau）。 | **互补**。提供实验设计参考——不同工作流下 collapse 行为差异，可用于验证我们的监控信号在不同设定下的灵敏度。 |\n| 3 | **Feng et al.** \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification.\" *ICLR 2025*. | `feng_iclr2025` | 用高斯混合模型推导验证器有效的条件，证明即使不完美的验证器也可有效筛选合成数据。 | **互补**。缓解策略方向；我们的监控信号可作为验证器的补充或替代——当 collapse 信号超过阈值时触发干预。 |\n| 4 | **Yi et al.** \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence.\" *arXiv 2510.16657*, 2025. | `yi_2025` | 证明外部验证器（人类或更强模型）可阻止 collapse，分析短期改进和长期收敛行为。 | **互补**。与监控方向正交；我们的贡献在于提供何时需要启动验证/干预的信号。 |\n\n---\n\n## 覆盖检查\n\n### literature_map.yaml 全部 19 篇论文分配\n\n| ID | 类别 |\n|----|------|\n| `shumailov_nature2024` | A |\n| `dohmatob_iclr2025` | A |\n| `seddik_2024` | A |\n| `schaeffer_2025` | A |\n| `shi_neurips2025` | A |\n| `bakshi_2026` | A |\n| `sigma_2026` | B |\n| `kalinowski_2026` | B |\n| `wyss_2024` | B |\n| `martin_mahoney_2021` | C |\n| `spectral_lens_2026` | C |\n| `chen_liu_2024` | C |\n| `yunis_2024` | C |\n| `xu_2026` | C |\n| `layer_collapse_diffusion_2026` | C |\n| `gerstgrasser_2024` | D |\n| `kazdan_2024` | D |\n| `feng_iclr2025` | D |\n| `yi_2025` | D |\n\n### 需补入 literature_map.yaml 的论文\n\n- **Alemohammad et al. (2024)** \"Self-Consuming Generative Models Go MAD.\" ICLR 2024. arXiv: 2307.01850\n  - 分类至 A（理论基础）\n  - relation: foundation\n  - 建议 id: `alemohammad_iclr2024`\n\n---\n\n## 论文写作备注\n\n1. **开篇逻辑**: A → B → C → D，从\"问题是什么\"到\"谁在检测\"到\"用什么工具\"到\"如何缓解\"\n2. **核心 positioning 句**: \"To the best of our knowledge, no prior work simultaneously achieves (a) online monitoring during training, (b) spectral/entropy training dynamics signals, (c) per-layer granularity, and (d) validation in the iterative synthetic data training setting.\"\n3. **Collapse 定义**: 采用 Schaeffer et al. (2025) 的分类框架，明确我们关注的是 test loss degradation + distribution tail collapse\n4. **Alemohammad 2024 必须引用**: Reviewer 之前指出缺失，与 Shumailov 2024 共同构成问题定义的基石\n",
      "numLines": 110,
      "startLine": 1,
      "totalLines": 110
    }
  },
  "sourceToolAssistantUUID": "0b774d17-469d-49f8-a2bb-6987a3d63be8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T22:47:38.612Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RUU9aELSmQ1pumL831kfBs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/docs/related_work_outline.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa77242a-cd6b-4d75-afa0-01358d0baa87",
  "isSidechain": false,
  "requestId": "req_011Cb3GvRSPo6nk47qFnvcJJ",
  "type": "assistant",
  "uuid": "0b774d17-469d-49f8-a2bb-6987a3d63be8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXcxJJVrzwLPrsTWPzG5t7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11095,
      "cache_read_input_tokens": 11841,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11095,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 172,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11095
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

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "leafUuid": "104e82e5-b2c4-4f44-8617-4f3927f508d5",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Update related work outline with 14 new papers",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2"
}
```

---

### Assistant

_source line 15 · 2026-05-14T22:48:08.688Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to compare the two files to find which papers from literature_map.yaml are missing in the outline.

Papers in literature_map.yaml (34 papers):
1. sigma_2026
2. kalinowski_2026
3. spectral_lens_2026
4. shi_neurips2025
5. wyss_2024
6. xu_2026
7. layer_collapse_diffusion_2026
8. alemohammad_iclr2024
9. papyan_pnas2020


10. shumailov_nature2024
11. dohmatob_iclr2025
12. gerstgrasser_2024
13. kazdan_2024
14. seddik_2024
15. schaeffer_2025
16. feng_iclr2025
17. yi_2025
18. bakshi_2026
19. dohmatob_icml2024
20. fu_icml2024
21. gillman_icml2024
22. kirchenbauer_icml2023
23. dathathri_nature2024
24. sander_neurips2024
25. mitchell_icml2023
26. shi_iclr2024
27. martin_mahoney_2021
28. (continuing through the full list of 34 papers)
29. yunis_2024
30. chen_liu_2024
31. lu_neurips2024
32. sanyal_iclr2020
33. kalra_2026
34. penedo_2024
35. zhang_2026

Now I'm organizing these papers into four thematic sections: section A covers foundational work on model behavior and watermarking with seven papers, section B focuses on specific technical approaches with three papers, section C examines interpretability and mechanistic understanding with six papers, and section D addresses remaining theoretical and empirical analyses.

I'm tracking fourteen additional papers that should be integrated—these cover neural collapse foundations, scaling laws, self-consuming loops, watermarking techniques, and detection methods that complement the core outline. The detection papers are really about identifying synthetic data contamination rather than collapse itself, so I should separate them into their own section. For the training dynamics papers, they're focused on spectral properties and normalization techniques that influence how models learn, which is distinct from the theoretical collapse mechanisms.

Now I'm organizing the full outline with the new sections—I need to update the total count to 34 papers and make sure all the papers are distributed across the six sections properly, then draft the complete updated structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "104e82e5-b2c4-4f44-8617-4f3927f508d5",
  "isSidechain": false,
  "requestId": "req_011Cb3GvqXyz7xbx2YQ1cReu",
  "type": "assistant",
  "uuid": "9ea52d8c-29ae-4f75-96d5-8503fadd366c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jc632wgDVLr9HkGvLvKZub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17933,
      "cache_read_input_tokens": 22936,
      "output_tokens": 9090,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9090,
          "cache_read_input_tokens": 22936,
          "cache_creation_input_tokens": 17933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17933
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

### Assistant

_source line 16 · 2026-05-14T22:48:09.978Z_

现有 outline 覆盖 20 篇，literature_map 有 34 篇，缺失 14 篇。我来对比并更新。

缺失的 14 篇按主题分配：
- **A (Theory)**: dohmatob_icml2024, fu_icml2024, papyan_pnas2020
- **C (Training Dynamics)**: lu_neurips2024, sanyal_iclr2020, kalra_2026
- **D (Mitigation)**: gillman_icml2024
- **E (Data Contamination Detection)** 新增: kirchenbauer_icml2023, dathathri_nature2024, sander_neurips2024, mitchell_icml2023, shi_iclr2024
- **F (Data Quality)** 新增: penedo_2024, zhang_2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ea52d8c-29ae-4f75-96d5-8503fadd366c",
  "isSidechain": false,
  "requestId": "req_011Cb3GvqXyz7xbx2YQ1cReu",
  "type": "assistant",
  "uuid": "40f257a0-315b-4d81-aa9a-9011f8c79480",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jc632wgDVLr9HkGvLvKZub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17933,
      "cache_read_input_tokens": 22936,
      "output_tokens": 9090,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9090,
          "cache_read_input_tokens": 22936,
          "cache_creation_input_tokens": 17933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17933
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

### Tool call

_source line 17 · 2026-05-14T22:50:02.522Z_

<details open><summary>🔧 Tool call — Write · `toolu_01UZ9NiJDffUzLL4sNgNNQVd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/docs/related_work_outline.md",
  "content": "# Related Work 结构大纲\n\n> **项目**: collapse_severity_monitor — 在线监控模型 collapse 严重度\n> **目标会议**: EMNLP 2026 ARR\n> **基于**: literature_map.yaml (34 篇)\n\n---\n\n## A. Model Collapse: 理论基础与实证\n\nModel collapse 指在合成数据上迭代训练导致模型质量不可逆退化的现象。自 Shumailov et al. (2024) 在 Nature 上首次系统性证明以来，理论和实证研究迅速发展，从分布尾部消失、缩放定律失效到术语统一均有深入探讨。我们的工作建立在这些理论基础之上，旨在提供训练过程中的实时监控手段。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Shumailov et al.** \"AI Models Collapse When Trained on Recursively Generated Data.\" *Nature* 631, 755–759, 2024. | `shumailov_nature2024` | 首次系统证明迭代合成数据训练导致 model collapse（LLM/VAE/GMM），核心机制为分布尾部消失。 | **领域基石**。定义了我们要解决的问题；他们用事后评估（test loss），我们提供在线监控。 |\n| 2 | **Alemohammad et al.** \"Self-Consuming Generative Models Go MAD.\" *ICLR 2024*. | `alemohammad_iclr2024` | 提出 Model Autophagy Disorder (MAD) 框架，分析三类自噬循环（fully synthetic / synthetic augmentation / fresh data）下质量-多样性退化。 | **理论基础**。MAD 框架为我们的迭代合成数据实验设计提供了分类学；他们证明无足够真实数据则 precision 或 recall 必退化。 |\n| 3 | **Dohmatob, Feng et al.** \"Strong Model Collapse.\" *ICLR 2025 (Spotlight)*. | `dohmatob_iclr2025` | 用算子值自由概率论证明即使极小比例（1/1000）合成数据也导致 collapse，且更大模型放大 collapse。 | **理论支撑**。解释了为什么需要监控——即使少量合成数据也危险；其 fraction 实验与我们的实验设计直接相关。 |\n| 4 | **Dohmatob et al.** \"A Tale of Tails: Model Collapse as a Change of Scaling Laws.\" *ICML 2024*, pp. 11165–11197. | `dohmatob_icml2024` | 从 scaling law 视角分析 collapse——揭示 collapse 导致 scaling law 改变，以及 skill un-learning 现象。 | **理论背景**。从 scaling law 角度量化 collapse 严重度；我们用训练动态信号在训练中追踪，他们用事后 scaling 分析。 |\n| 5 | **Seddik et al.** \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse.\" *arXiv 2404.05090*, 2024. | `seddik_2024` | 统计模型严格刻画不同递归训练场景下的 collapse 程度，给出混合训练下合成数据比例安全上限。 | **理论互补**。提供合成数据比例的安全阈值估计，可与我们的监控信号阈值对照验证。 |\n| 6 | **Fu et al.** \"Towards Theoretical Understandings of Self-Consuming Generative Models.\" *ICML 2024*. | `fu_icml2024` | 构建严格理论框架分析 self-consuming loop 中数据分布演化，分析统计/表达/近似三种误差源的复合效应。 | **理论互补**。严格刻画 collapse 的误差复合机制，给出误差增长的理论界，为理解我们监控信号的变化趋势提供理论预期。 |\n| 7 | **Schaeffer, Kazdan et al.** \"Position: Model Collapse Does Not Mean What You Think.\" *arXiv 2503.03150*, 2025. | `schaeffer_2025` | 梳理 collapse 文献中 8 种不同定义，分为三个家族：test loss 行为、分布形变、缩放行为。 | **定位参考**。论文中需明确我们采用的 collapse 定义；建议采用他们的分类框架。 |\n| 8 | **Shi et al.** \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective.\" *NeurIPS 2025 (Spotlight)*. | `shi_neurips2025` | 揭示 collapse 中从泛化到记忆的转变，发现训练数据熵与泛化能力强线性相关。 | **互补视角**。他们用数据级熵，我们用模型内部训练动态信号；其数据熵可作为我们的外部验证指标。 |\n| 9 | **Bakshi et al.** \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources.\" *arXiv 2602.10531*, 2026. | `bakshi_2026` | 分析真实+合成混合数据的迭代训练长期演化动态，非零真实数据权重（即使递减）可避免 collapse。 | **理论互补**。刻画迭代训练的长期演化规律，为我们的多轮实验设计提供理论预期。 |\n| 10 | **Papyan, Han & Donoho.** \"Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training.\" *PNAS* 117(40), 24652–24663, 2020. | `papyan_pnas2020` | 发现分类网络训练末期的 Neural Collapse——类内表征收缩到 Simplex ETF，提出四种 collapse 现象。 | **概念参照**。虽然 neural collapse 与 model collapse 是不同概念，但谱分析方法论可借鉴，且提供 \"collapse\" 概念的对比参考，论文中需明确区分。 |\n\n---\n\n## B. Collapse 检测与监控方法\n\n现有 collapse 检测方法主要分为事后评估（test loss、分布指标）和在线监控两类。直接竞争者包括基于谱分析的 SIGMA 和基于拓扑信号的 Kalinowski 方法。**我们的独特定位**：在线 + 频谱/熵训练动态信号 + per-layer 粒度 + 迭代合成数据场景，这一组合目前无人覆盖。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Gu et al.** \"SIGMA: Scalable Spectral Insights for LLM Model Collapse.\" *arXiv 2601.03385*, 2026. | `sigma_2026` | 通过 embedding Gram 矩阵的谱分析量化 collapse，推导谱收缩的确定性和随机性界。 | **直接竞争者**。SIGMA 是事后/黑盒方法（用输出嵌入 Gram 矩阵），不需要模型权重，不做 per-layer 分析，不跟踪训练过程动态变化。我们是训练中实时监控，更早期更细粒度。 |\n| 2 | **Kalinowski.** \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index.\" *arXiv 2604.26984*, 2026. | `kalinowski_2026` | 提出在线拓扑感知监控器（MMHM + Collapse Index），通过稀疏增量更新实现快速在线监控。 | **直接竞争者**。同为在线监控，但信号族完全不同（拓扑 vs 频谱/熵）。我们的信号更轻量、更可解释（stable rank/spectral entropy 有直接线性代数含义）。Kalinowski 不研究迭代合成数据场景。 |\n| 3 | **Wyss et al.** \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI.\" *arXiv 2410.12341*, 2024. | `wyss_2024` | 用语义网络和 next-token 概率表征 collapse，引入 collapsed prediction 概念量化多样性损失。 | **相关方法**。用输出级指标（next-token prob），属事后分析；其 synthetic fraction 实验（25%/50%/75%）与我们的实验设计有重叠，可作为 baseline 指标。 |\n\n### 我们的定位（论文中需强调）\n\n> 现有方法要么是事后/黑盒分析（SIGMA），要么用非频谱信号（Kalinowski 的拓扑方法），要么仅关注输出级指标（Wyss）。本工作首次将频谱/熵训练动态信号（spectral entropy、stable rank、output token entropy）以 per-layer 粒度应用于迭代合成数据训练中的在线 collapse 监控。\n\n---\n\n## C. 训练动态分析与诊断\n\n频谱分析和训练动态诊断是深度学习中成熟的研究方向。WeightWatcher 等工具已证明权重矩阵的谱性质（stable rank、power law exponent）可有效评估模型质量。我们将这些方法论工具从通用训练诊断延伸到 collapse 监控这一特定场景。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Martin & Mahoney.** \"Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data.\" *Nature Communications* 12, 2021. | `martin_mahoney_2021` | WeightWatcher 工具——用 RMT 分析权重矩阵谱性质（stable rank、power law α、spectral norm），无需训练/测试数据即可预测模型质量。 | **方法论基础**。WeightWatcher 的 stable rank 和谱分析方法直接启发我们的信号设计；其 5+1 训练阶段分类可用于解释 collapse 过程中的谱形态变化。 |\n| 2 | **Liu et al. (Spectral Lens).** \"Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization.\" *arXiv 2605.05683*, 2026. | `spectral_lens_2026` | 用 activation covariance 和 per-sample gradient 的 SVD 谱作为 LLM 训练优化诊断工具。 | **方法论高度相关**。同样用频谱分析训练动态，但关注优化诊断而非 collapse/合成数据退化；其 per-layer 分析方法可参考。 |\n| 3 | **Chen & Liu.** \"Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy.\" *IEEE CISS 2024*. | `chen_liu_2024` | 提出 Diffusion Spectral Entropy (DSE) 和 DSMI，利用数据几何在高维中可靠计算信息论指标。 | **方法论工具**。DSE 是我们 spectral entropy 信号的潜在替代实现；其 DSE 随训练增加、DSMI 在过拟合时停滞的发现可为 collapse 检测提供参照。 |\n| 4 | **Yunis, Patel et al.** \"Approaching Deep Learning through the Spectral Dynamics of Weights.\" *arXiv 2408.11804*, 2024. | `yunis_2024` | 以权重奇异值/向量的动态演化为核心视角，证明谱动态可区分记忆网络和泛化网络。 | **方法论基础**。谱动态视角可用于理解 collapse 过程中的权重变化；权重衰减增强低秩偏置的发现与 collapse 中的秩退化相关。 |\n| 5 | **Xu.** \"Predicting LLM Compression Degradation from Spectral Statistics.\" *arXiv 2604.18085*, 2026. | `xu_2026` | 用 stable rank 和信息密度预测 LLM 压缩退化（Pearson r=0.890 attention, 0.839 MLP），per-layer 分析。 | **信号验证**。直接验证 stable rank 作为退化预测信号的有效性；虽场景不同（压缩 vs collapse），但支持我们选用 stable rank 的合理性。 |\n| 6 | **Conzelmann et al.** \"Layer Collapse in Diffusion Language Models.\" *arXiv 2605.06366*, 2026. | `layer_collapse_diffusion_2026` | 分析 diffusion LM (LLaDA-8B) 中 per-layer activation collapse，发现少数早期层出现 channel-axis collapse。 | **方法论参考**。做了 per-layer collapse 分析，但在 diffusion LM 上；其 activation 分析方法可参考，但场景和模型架构不同。 |\n| 7 | **Lu et al. (AlphaPruning).** \"AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models.\" *NeurIPS 2024*. | `lu_neurips2024` | 用 HT-SR 理论的谱密度形态（alpha exponent）指导 LLM 层级剪枝，LLaMA-7B 可剪至 80% sparsity。 | **方法论验证**。验证 per-layer 谱分析（alpha exponent）对 LLM 质量评估的有效性，支持我们用类似 per-layer 谱方法监控 collapse。 |\n| 8 | **Sanyal, Torr & Dokania.** \"Stable Rank Normalization for Improved Generalization in Neural Networks and GANs.\" *ICLR 2020*. | `sanyal_iclr2020` | 提出 stable rank normalization，理论证明唯一最优解，实验验证控制 stable rank 可改善泛化 gap 11.3%。 | **理论支持**。建立 stable rank 与泛化的直接联系，支持我们选用 stable rank 作为 collapse（泛化退化）的监控信号。 |\n| 9 | **Kalra et al.** \"A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs.\" *arXiv 2601.16979*, 2026. | `kalra_2026` | 提出 critical sharpness（<10 forward passes 高效度量 loss landscape 曲率），首次在 7B 规模验证 progressive sharpening。 | **方法论参考**。高效的大规模 LLM 训练动态度量方法；critical sharpness 可作为我们信号集的潜在补充信号。 |\n\n---\n\n## D. Collapse 缓解策略\n\n缓解策略主要分为数据管理（累积 vs 替换、混合比例控制）和数据筛选/验证两类。这些工作与我们的监控方向互补——我们负责检测 collapse 何时发生及严重程度，它们负责干预和缓解。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Gerstgrasser, Schaeffer et al.** \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data.\" *arXiv 2404.01413*, 2024. | `gerstgrasser_2024` | 证明数据累积（而非替换）可避免 collapse；替换导致 test error 增长，累积则有有限上界。 | **互补**。他们研究何时 collapse（数据管理策略），我们研究如何实时检测 collapse；累积 vs 替换的差异可作为我们监控信号的验证场景。 |\n| 2 | **Kazdan et al.** \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World.\" *arXiv 2410.16713*, 2024. | `kazdan_2024` | 系统比较三种工作流：replace（collapse）、accumulate（稳定）、fixed compute（plateau）。 | **互补**。提供实验设计参考——不同工作流下 collapse 行为差异，可用于验证我们的监控信号在不同设定下的灵敏度。 |\n| 3 | **Feng et al.** \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification.\" *ICLR 2025*. | `feng_iclr2025` | 用高斯混合模型推导验证器有效的条件，证明即使不完美的验证器也可有效筛选合成数据。 | **互补**。缓解策略方向；我们的监控信号可作为验证器的补充或替代——当 collapse 信号超过阈值时触发干预。 |\n| 4 | **Yi et al.** \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence.\" *arXiv 2510.16657*, 2025. | `yi_2025` | 证明外部验证器（人类或更强模型）可阻止 collapse，分析短期改进和长期收敛行为。 | **互补**。与监控方向正交；我们的贡献在于提供何时需要启动验证/干预的信号。 |\n| 5 | **Gillman et al.** \"Self-Correcting Self-Consuming Loops for Generative Model Training.\" *ICML 2024*. | `gillman_icml2024` | 引入 correction function 使 self-consuming loop 指数级更稳定，即使 synthetic:real = 100:1 也可避免 collapse。 | **互补**。缓解策略方向；correction function 概念与在线监控互补——我们的信号可指导何时激活 correction。 |\n\n---\n\n## E. 合成数据污染检测\n\n检测训练数据中是否含有合成数据是 collapse 监控的上游问题。水印方法标记合成文本，检测方法识别机器生成内容。这些工作与我们的方向互补：它们回答\"是否用了合成数据\"，我们回答\"合成数据造成了多严重的 collapse\"。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Kirchenbauer et al.** \"A Watermark for Large Language Models.\" *ICML 2023*, pp. 17061–17084. | `kirchenbauer_icml2023` | LLM 文本水印框架——green/red token list + soft promotion + 统计检测，开源检测算法不需模型访问。 | **互补**。合成数据溯源的基础方法；可标记合成数据以便追踪其在迭代训练中的传播。 |\n| 2 | **Dathathri et al.** \"Scalable Watermarking for Identifying Large Language Model Outputs.\" *Nature* 634, 818–823, 2024. | `dathathri_nature2024` | SynthID-Text：产品级文本水印，与 speculative sampling 集成，在 Gemini ~20M 响应上验证。 | **互补**。大规模合成数据标记的工业实践，展示水印在产品级规模上的可行性。 |\n| 3 | **Sander et al.** \"Watermarking Makes Language Models Radioactive.\" *NeurIPS 2024*. | `sander_neurips2024` | 证明在水印 LLM 输出上微调的模型保留水印残留（\"放射性\"），可检测模型是否在合成数据上训练。 | **直接相关**。检测合成数据训练的替代方法；他们检测\"是否用了合成数据\"，我们监控\"合成数据造成多严重的 collapse\"。 |\n| 4 | **Mitchell et al. (DetectGPT).** \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.\" *ICML 2023*, pp. 24950–24962. | `mitchell_icml2023` | LLM 生成文本占据 log-probability 负曲率区域，据此零样本检测，0.95 AUROC 检测 GPT-NeoX 20B 生成的假新闻。 | **互补**。合成文本检测方法，可识别训练数据中的合成成分，为 collapse 监控提供数据侧信息。 |\n| 5 | **Shi et al. (Min-K%).** \"Detecting Pretraining Data from Large Language Models.\" *ICLR 2024*. | `shi_iclr2024` | Min-K% Prob：未见样本含低概率 outlier word，据此检测预训练数据成员，比 reference model 方法提升 7.4%。 | **互补**。数据污染检测工具——可检测合成数据是否混入训练集，与 collapse 监控互补。 |\n\n---\n\n## F. 数据质量与评估\n\n高质量训练数据是避免 collapse 的前提。数据质量评估框架为理解 collapse 的数据侧原因提供分析工具。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Penedo et al.** \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale.\" *arXiv 2406.17557*, 2024. | `penedo_2024` | 15T token 数据集的完整策略文档——去重、过滤、教育文本提取，详细 ablation 各种数据质量策略。 | **数据质量参考**。理解高质量训练数据标准，为分析 collapse 的数据原因提供基线。 |\n| 2 | **Zhang et al.** \"The LLM Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data.\" *arXiv 2601.17717*, 2026. | `zhang_2026` | 系统分类合成数据评估指标——quality (validity/fidelity/utility) + trustworthiness (safety/faithfulness)。 | **评估框架参考**。从内在属性评估合成数据质量的分类体系，为理解 collapse 的数据级原因提供指标视角。 |\n\n---\n\n## 覆盖检查\n\n### literature_map.yaml 全部 34 篇论文分配\n\n| ID | 类别 |\n|----|------|\n| `shumailov_nature2024` | A |\n| `alemohammad_iclr2024` | A |\n| `dohmatob_iclr2025` | A |\n| `dohmatob_icml2024` | A |\n| `seddik_2024` | A |\n| `fu_icml2024` | A |\n| `schaeffer_2025` | A |\n| `shi_neurips2025` | A |\n| `bakshi_2026` | A |\n| `papyan_pnas2020` | A |\n| `sigma_2026` | B |\n| `kalinowski_2026` | B |\n| `wyss_2024` | B |\n| `martin_mahoney_2021` | C |\n| `spectral_lens_2026` | C |\n| `chen_liu_2024` | C |\n| `yunis_2024` | C |\n| `xu_2026` | C |\n| `layer_collapse_diffusion_2026` | C |\n| `lu_neurips2024` | C |\n| `sanyal_iclr2020` | C |\n| `kalra_2026` | C |\n| `gerstgrasser_2024` | D |\n| `kazdan_2024` | D |\n| `feng_iclr2025` | D |\n| `yi_2025` | D |\n| `gillman_icml2024` | D |\n| `kirchenbauer_icml2023` | E |\n| `dathathri_nature2024` | E |\n| `sander_neurips2024` | E |\n| `mitchell_icml2023` | E |\n| `shi_iclr2024` | E |\n| `penedo_2024` | F |\n| `zhang_2026` | F |\n\n---\n\n## 论文写作备注\n\n1. **开篇逻辑**: A → B → C → D → E → F，从\"问题是什么\"到\"谁在检测\"到\"用什么工具\"到\"如何缓解\"到\"数据侧检测与质量\"\n2. **核心 positioning 句**: \"To the best of our knowledge, no prior work simultaneously achieves (a) online monitoring during training, (b) spectral/entropy training dynamics signals, (c) per-layer granularity, and (d) validation in the iterative synthetic data training setting.\"\n3. **Collapse 定义**: 采用 Schaeffer et al. (2025) 的分类框架，明确我们关注的是 test loss degradation + distribution tail collapse\n4. **Alemohammad 2024 必须引用**: 与 Shumailov 2024 共同构成问题定义的基石\n5. **Neural Collapse 区分**: 引用 Papyan et al. (2020) 时需明确区分 neural collapse（训练末期分类器现象）与 model collapse（合成数据迭代退化）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40f257a0-315b-4d81-aa9a-9011f8c79480",
  "isSidechain": false,
  "requestId": "req_011Cb3GvqXyz7xbx2YQ1cReu",
  "type": "assistant",
  "uuid": "8d28dfaf-c652-4665-852f-b88d4d07091a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jc632wgDVLr9HkGvLvKZub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17933,
      "cache_read_input_tokens": 22936,
      "output_tokens": 9090,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9090,
          "cache_read_input_tokens": 22936,
          "cache_creation_input_tokens": 17933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17933
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

_source line 18 · 2026-05-14T22:50:02.572Z_

<details><summary>↩ Tool result · `toolu_01UZ9NiJDffUzLL4sNgNNQVd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/docs/related_work_outline.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d28dfaf-c652-4665-852f-b88d4d07091a",
  "isSidechain": false,
  "promptId": "6d40a60b-3de6-4cba-96cf-f662df5975d1",
  "type": "user",
  "uuid": "f0516800-5694-4b15-a4b1-25af58cff6db",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/docs/related_work_outline.md",
    "content": "# Related Work 结构大纲\n\n> **项目**: collapse_severity_monitor — 在线监控模型 collapse 严重度\n> **目标会议**: EMNLP 2026 ARR\n> **基于**: literature_map.yaml (34 篇)\n\n---\n\n## A. Model Collapse: 理论基础与实证\n\nModel collapse 指在合成数据上迭代训练导致模型质量不可逆退化的现象。自 Shumailov et al. (2024) 在 Nature 上首次系统性证明以来，理论和实证研究迅速发展，从分布尾部消失、缩放定律失效到术语统一均有深入探讨。我们的工作建立在这些理论基础之上，旨在提供训练过程中的实时监控手段。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Shumailov et al.** \"AI Models Collapse When Trained on Recursively Generated Data.\" *Nature* 631, 755–759, 2024. | `shumailov_nature2024` | 首次系统证明迭代合成数据训练导致 model collapse（LLM/VAE/GMM），核心机制为分布尾部消失。 | **领域基石**。定义了我们要解决的问题；他们用事后评估（test loss），我们提供在线监控。 |\n| 2 | **Alemohammad et al.** \"Self-Consuming Generative Models Go MAD.\" *ICLR 2024*. | `alemohammad_iclr2024` | 提出 Model Autophagy Disorder (MAD) 框架，分析三类自噬循环（fully synthetic / synthetic augmentation / fresh data）下质量-多样性退化。 | **理论基础**。MAD 框架为我们的迭代合成数据实验设计提供了分类学；他们证明无足够真实数据则 precision 或 recall 必退化。 |\n| 3 | **Dohmatob, Feng et al.** \"Strong Model Collapse.\" *ICLR 2025 (Spotlight)*. | `dohmatob_iclr2025` | 用算子值自由概率论证明即使极小比例（1/1000）合成数据也导致 collapse，且更大模型放大 collapse。 | **理论支撑**。解释了为什么需要监控——即使少量合成数据也危险；其 fraction 实验与我们的实验设计直接相关。 |\n| 4 | **Dohmatob et al.** \"A Tale of Tails: Model Collapse as a Change of Scaling Laws.\" *ICML 2024*, pp. 11165–11197. | `dohmatob_icml2024` | 从 scaling law 视角分析 collapse——揭示 collapse 导致 scaling law 改变，以及 skill un-learning 现象。 | **理论背景**。从 scaling law 角度量化 collapse 严重度；我们用训练动态信号在训练中追踪，他们用事后 scaling 分析。 |\n| 5 | **Seddik et al.** \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse.\" *arXiv 2404.05090*, 2024. | `seddik_2024` | 统计模型严格刻画不同递归训练场景下的 collapse 程度，给出混合训练下合成数据比例安全上限。 | **理论互补**。提供合成数据比例的安全阈值估计，可与我们的监控信号阈值对照验证。 |\n| 6 | **Fu et al.** \"Towards Theoretical Understandings of Self-Consuming Generative Models.\" *ICML 2024*. | `fu_icml2024` | 构建严格理论框架分析 self-consuming loop 中数据分布演化，分析统计/表达/近似三种误差源的复合效应。 | **理论互补**。严格刻画 collapse 的误差复合机制，给出误差增长的理论界，为理解我们监控信号的变化趋势提供理论预期。 |\n| 7 | **Schaeffer, Kazdan et al.** \"Position: Model Collapse Does Not Mean What You Think.\" *arXiv 2503.03150*, 2025. | `schaeffer_2025` | 梳理 collapse 文献中 8 种不同定义，分为三个家族：test loss 行为、分布形变、缩放行为。 | **定位参考**。论文中需明确我们采用的 collapse 定义；建议采用他们的分类框架。 |\n| 8 | **Shi et al.** \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective.\" *NeurIPS 2025 (Spotlight)*. | `shi_neurips2025` | 揭示 collapse 中从泛化到记忆的转变，发现训练数据熵与泛化能力强线性相关。 | **互补视角**。他们用数据级熵，我们用模型内部训练动态信号；其数据熵可作为我们的外部验证指标。 |\n| 9 | **Bakshi et al.** \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources.\" *arXiv 2602.10531*, 2026. | `bakshi_2026` | 分析真实+合成混合数据的迭代训练长期演化动态，非零真实数据权重（即使递减）可避免 collapse。 | **理论互补**。刻画迭代训练的长期演化规律，为我们的多轮实验设计提供理论预期。 |\n| 10 | **Papyan, Han & Donoho.** \"Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training.\" *PNAS* 117(40), 24652–24663, 2020. | `papyan_pnas2020` | 发现分类网络训练末期的 Neural Collapse——类内表征收缩到 Simplex ETF，提出四种 collapse 现象。 | **概念参照**。虽然 neural collapse 与 model collapse 是不同概念，但谱分析方法论可借鉴，且提供 \"collapse\" 概念的对比参考，论文中需明确区分。 |\n\n---\n\n## B. Collapse 检测与监控方法\n\n现有 collapse 检测方法主要分为事后评估（test loss、分布指标）和在线监控两类。直接竞争者包括基于谱分析的 SIGMA 和基于拓扑信号的 Kalinowski 方法。**我们的独特定位**：在线 + 频谱/熵训练动态信号 + per-layer 粒度 + 迭代合成数据场景，这一组合目前无人覆盖。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Gu et al.** \"SIGMA: Scalable Spectral Insights for LLM Model Collapse.\" *arXiv 2601.03385*, 2026. | `sigma_2026` | 通过 embedding Gram 矩阵的谱分析量化 collapse，推导谱收缩的确定性和随机性界。 | **直接竞争者**。SIGMA 是事后/黑盒方法（用输出嵌入 Gram 矩阵），不需要模型权重，不做 per-layer 分析，不跟踪训练过程动态变化。我们是训练中实时监控，更早期更细粒度。 |\n| 2 | **Kalinowski.** \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index.\" *arXiv 2604.26984*, 2026. | `kalinowski_2026` | 提出在线拓扑感知监控器（MMHM + Collapse Index），通过稀疏增量更新实现快速在线监控。 | **直接竞争者**。同为在线监控，但信号族完全不同（拓扑 vs 频谱/熵）。我们的信号更轻量、更可解释（stable rank/spectral entropy 有直接线性代数含义）。Kalinowski 不研究迭代合成数据场景。 |\n| 3 | **Wyss et al.** \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI.\" *arXiv 2410.12341*, 2024. | `wyss_2024` | 用语义网络和 next-token 概率表征 collapse，引入 collapsed prediction 概念量化多样性损失。 | **相关方法**。用输出级指标（next-token prob），属事后分析；其 synthetic fraction 实验（25%/50%/75%）与我们的实验设计有重叠，可作为 baseline 指标。 |\n\n### 我们的定位（论文中需强调）\n\n> 现有方法要么是事后/黑盒分析（SIGMA），要么用非频谱信号（Kalinowski 的拓扑方法），要么仅关注输出级指标（Wyss）。本工作首次将频谱/熵训练动态信号（spectral entropy、stable rank、output token entropy）以 per-layer 粒度应用于迭代合成数据训练中的在线 collapse 监控。\n\n---\n\n## C. 训练动态分析与诊断\n\n频谱分析和训练动态诊断是深度学习中成熟的研究方向。WeightWatcher 等工具已证明权重矩阵的谱性质（stable rank、power law exponent）可有效评估模型质量。我们将这些方法论工具从通用训练诊断延伸到 collapse 监控这一特定场景。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Martin & Mahoney.** \"Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data.\" *Nature Communications* 12, 2021. | `martin_mahoney_2021` | WeightWatcher 工具——用 RMT 分析权重矩阵谱性质（stable rank、power law α、spectral norm），无需训练/测试数据即可预测模型质量。 | **方法论基础**。WeightWatcher 的 stable rank 和谱分析方法直接启发我们的信号设计；其 5+1 训练阶段分类可用于解释 collapse 过程中的谱形态变化。 |\n| 2 | **Liu et al. (Spectral Lens).** \"Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization.\" *arXiv 2605.05683*, 2026. | `spectral_lens_2026` | 用 activation covariance 和 per-sample gradient 的 SVD 谱作为 LLM 训练优化诊断工具。 | **方法论高度相关**。同样用频谱分析训练动态，但关注优化诊断而非 collapse/合成数据退化；其 per-layer 分析方法可参考。 |\n| 3 | **Chen & Liu.** \"Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy.\" *IEEE CISS 2024*. | `chen_liu_2024` | 提出 Diffusion Spectral Entropy (DSE) 和 DSMI，利用数据几何在高维中可靠计算信息论指标。 | **方法论工具**。DSE 是我们 spectral entropy 信号的潜在替代实现；其 DSE 随训练增加、DSMI 在过拟合时停滞的发现可为 collapse 检测提供参照。 |\n| 4 | **Yunis, Patel et al.** \"Approaching Deep Learning through the Spectral Dynamics of Weights.\" *arXiv 2408.11804*, 2024. | `yunis_2024` | 以权重奇异值/向量的动态演化为核心视角，证明谱动态可区分记忆网络和泛化网络。 | **方法论基础**。谱动态视角可用于理解 collapse 过程中的权重变化；权重衰减增强低秩偏置的发现与 collapse 中的秩退化相关。 |\n| 5 | **Xu.** \"Predicting LLM Compression Degradation from Spectral Statistics.\" *arXiv 2604.18085*, 2026. | `xu_2026` | 用 stable rank 和信息密度预测 LLM 压缩退化（Pearson r=0.890 attention, 0.839 MLP），per-layer 分析。 | **信号验证**。直接验证 stable rank 作为退化预测信号的有效性；虽场景不同（压缩 vs collapse），但支持我们选用 stable rank 的合理性。 |\n| 6 | **Conzelmann et al.** \"Layer Collapse in Diffusion Language Models.\" *arXiv 2605.06366*, 2026. | `layer_collapse_diffusion_2026` | 分析 diffusion LM (LLaDA-8B) 中 per-layer activation collapse，发现少数早期层出现 channel-axis collapse。 | **方法论参考**。做了 per-layer collapse 分析，但在 diffusion LM 上；其 activation 分析方法可参考，但场景和模型架构不同。 |\n| 7 | **Lu et al. (AlphaPruning).** \"AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models.\" *NeurIPS 2024*. | `lu_neurips2024` | 用 HT-SR 理论的谱密度形态（alpha exponent）指导 LLM 层级剪枝，LLaMA-7B 可剪至 80% sparsity。 | **方法论验证**。验证 per-layer 谱分析（alpha exponent）对 LLM 质量评估的有效性，支持我们用类似 per-layer 谱方法监控 collapse。 |\n| 8 | **Sanyal, Torr & Dokania.** \"Stable Rank Normalization for Improved Generalization in Neural Networks and GANs.\" *ICLR 2020*. | `sanyal_iclr2020` | 提出 stable rank normalization，理论证明唯一最优解，实验验证控制 stable rank 可改善泛化 gap 11.3%。 | **理论支持**。建立 stable rank 与泛化的直接联系，支持我们选用 stable rank 作为 collapse（泛化退化）的监控信号。 |\n| 9 | **Kalra et al.** \"A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs.\" *arXiv 2601.16979*, 2026. | `kalra_2026` | 提出 critical sharpness（<10 forward passes 高效度量 loss landscape 曲率），首次在 7B 规模验证 progressive sharpening。 | **方法论参考**。高效的大规模 LLM 训练动态度量方法；critical sharpness 可作为我们信号集的潜在补充信号。 |\n\n---\n\n## D. Collapse 缓解策略\n\n缓解策略主要分为数据管理（累积 vs 替换、混合比例控制）和数据筛选/验证两类。这些工作与我们的监控方向互补——我们负责检测 collapse 何时发生及严重程度，它们负责干预和缓解。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Gerstgrasser, Schaeffer et al.** \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data.\" *arXiv 2404.01413*, 2024. | `gerstgrasser_2024` | 证明数据累积（而非替换）可避免 collapse；替换导致 test error 增长，累积则有有限上界。 | **互补**。他们研究何时 collapse（数据管理策略），我们研究如何实时检测 collapse；累积 vs 替换的差异可作为我们监控信号的验证场景。 |\n| 2 | **Kazdan et al.** \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World.\" *arXiv 2410.16713*, 2024. | `kazdan_2024` | 系统比较三种工作流：replace（collapse）、accumulate（稳定）、fixed compute（plateau）。 | **互补**。提供实验设计参考——不同工作流下 collapse 行为差异，可用于验证我们的监控信号在不同设定下的灵敏度。 |\n| 3 | **Feng et al.** \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification.\" *ICLR 2025*. | `feng_iclr2025` | 用高斯混合模型推导验证器有效的条件，证明即使不完美的验证器也可有效筛选合成数据。 | **互补**。缓解策略方向；我们的监控信号可作为验证器的补充或替代——当 collapse 信号超过阈值时触发干预。 |\n| 4 | **Yi et al.** \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence.\" *arXiv 2510.16657*, 2025. | `yi_2025` | 证明外部验证器（人类或更强模型）可阻止 collapse，分析短期改进和长期收敛行为。 | **互补**。与监控方向正交；我们的贡献在于提供何时需要启动验证/干预的信号。 |\n| 5 | **Gillman et al.** \"Self-Correcting Self-Consuming Loops for Generative Model Training.\" *ICML 2024*. | `gillman_icml2024` | 引入 correction function 使 self-consuming loop 指数级更稳定，即使 synthetic:real = 100:1 也可避免 collapse。 | **互补**。缓解策略方向；correction function 概念与在线监控互补——我们的信号可指导何时激活 correction。 |\n\n---\n\n## E. 合成数据污染检测\n\n检测训练数据中是否含有合成数据是 collapse 监控的上游问题。水印方法标记合成文本，检测方法识别机器生成内容。这些工作与我们的方向互补：它们回答\"是否用了合成数据\"，我们回答\"合成数据造成了多严重的 collapse\"。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Kirchenbauer et al.** \"A Watermark for Large Language Models.\" *ICML 2023*, pp. 17061–17084. | `kirchenbauer_icml2023` | LLM 文本水印框架——green/red token list + soft promotion + 统计检测，开源检测算法不需模型访问。 | **互补**。合成数据溯源的基础方法；可标记合成数据以便追踪其在迭代训练中的传播。 |\n| 2 | **Dathathri et al.** \"Scalable Watermarking for Identifying Large Language Model Outputs.\" *Nature* 634, 818–823, 2024. | `dathathri_nature2024` | SynthID-Text：产品级文本水印，与 speculative sampling 集成，在 Gemini ~20M 响应上验证。 | **互补**。大规模合成数据标记的工业实践，展示水印在产品级规模上的可行性。 |\n| 3 | **Sander et al.** \"Watermarking Makes Language Models Radioactive.\" *NeurIPS 2024*. | `sander_neurips2024` | 证明在水印 LLM 输出上微调的模型保留水印残留（\"放射性\"），可检测模型是否在合成数据上训练。 | **直接相关**。检测合成数据训练的替代方法；他们检测\"是否用了合成数据\"，我们监控\"合成数据造成多严重的 collapse\"。 |\n| 4 | **Mitchell et al. (DetectGPT).** \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.\" *ICML 2023*, pp. 24950–24962. | `mitchell_icml2023` | LLM 生成文本占据 log-probability 负曲率区域，据此零样本检测，0.95 AUROC 检测 GPT-NeoX 20B 生成的假新闻。 | **互补**。合成文本检测方法，可识别训练数据中的合成成分，为 collapse 监控提供数据侧信息。 |\n| 5 | **Shi et al. (Min-K%).** \"Detecting Pretraining Data from Large Language Models.\" *ICLR 2024*. | `shi_iclr2024` | Min-K% Prob：未见样本含低概率 outlier word，据此检测预训练数据成员，比 reference model 方法提升 7.4%。 | **互补**。数据污染检测工具——可检测合成数据是否混入训练集，与 collapse 监控互补。 |\n\n---\n\n## F. 数据质量与评估\n\n高质量训练数据是避免 collapse 的前提。数据质量评估框架为理解 collapse 的数据侧原因提供分析工具。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Penedo et al.** \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale.\" *arXiv 2406.17557*, 2024. | `penedo_2024` | 15T token 数据集的完整策略文档——去重、过滤、教育文本提取，详细 ablation 各种数据质量策略。 | **数据质量参考**。理解高质量训练数据标准，为分析 collapse 的数据原因提供基线。 |\n| 2 | **Zhang et al.** \"The LLM Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data.\" *arXiv 2601.17717*, 2026. | `zhang_2026` | 系统分类合成数据评估指标——quality (validity/fidelity/utility) + trustworthiness (safety/faithfulness)。 | **评估框架参考**。从内在属性评估合成数据质量的分类体系，为理解 collapse 的数据级原因提供指标视角。 |\n\n---\n\n## 覆盖检查\n\n### literature_map.yaml 全部 34 篇论文分配\n\n| ID | 类别 |\n|----|------|\n| `shumailov_nature2024` | A |\n| `alemohammad_iclr2024` | A |\n| `dohmatob_iclr2025` | A |\n| `dohmatob_icml2024` | A |\n| `seddik_2024` | A |\n| `fu_icml2024` | A |\n| `schaeffer_2025` | A |\n| `shi_neurips2025` | A |\n| `bakshi_2026` | A |\n| `papyan_pnas2020` | A |\n| `sigma_2026` | B |\n| `kalinowski_2026` | B |\n| `wyss_2024` | B |\n| `martin_mahoney_2021` | C |\n| `spectral_lens_2026` | C |\n| `chen_liu_2024` | C |\n| `yunis_2024` | C |\n| `xu_2026` | C |\n| `layer_collapse_diffusion_2026` | C |\n| `lu_neurips2024` | C |\n| `sanyal_iclr2020` | C |\n| `kalra_2026` | C |\n| `gerstgrasser_2024` | D |\n| `kazdan_2024` | D |\n| `feng_iclr2025` | D |\n| `yi_2025` | D |\n| `gillman_icml2024` | D |\n| `kirchenbauer_icml2023` | E |\n| `dathathri_nature2024` | E |\n| `sander_neurips2024` | E |\n| `mitchell_icml2023` | E |\n| `shi_iclr2024` | E |\n| `penedo_2024` | F |\n| `zhang_2026` | F |\n\n---\n\n## 论文写作备注\n\n1. **开篇逻辑**: A → B → C → D → E → F，从\"问题是什么\"到\"谁在检测\"到\"用什么工具\"到\"如何缓解\"到\"数据侧检测与质量\"\n2. **核心 positioning 句**: \"To the best of our knowledge, no prior work simultaneously achieves (a) online monitoring during training, (b) spectral/entropy training dynamics signals, (c) per-layer granularity, and (d) validation in the iterative synthetic data training setting.\"\n3. **Collapse 定义**: 采用 Schaeffer et al. (2025) 的分类框架，明确我们关注的是 test loss degradation + distribution tail collapse\n4. **Alemohammad 2024 必须引用**: 与 Shumailov 2024 共同构成问题定义的基石\n5. **Neural Collapse 区分**: 引用 Papyan et al. (2020) 时需明确区分 neural collapse（训练末期分类器现象）与 model collapse（合成数据迭代退化）\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " ",
          " > **项目**: collapse_severity_monitor — 在线监控模型 collapse 严重度",
          " > **目标会议**: EMNLP 2026 ARR",
          "-> **基于**: literature_map.yaml (19 篇) + 1 篇补充 (Alemohammad 2024)",
          "+> **基于**: literature_map.yaml (34 篇)",
          " ",
          " ---",
          " "
        ]
      },
      {
        "oldStart": 13,
        "oldLines": 12,
        "newStart": 13,
        "newLines": 15,
        "lines": [
          " | # | 论文 | ID | 核心贡献 | 与我们的关系 |",
          " |---|------|----|----------|-------------|",
          " | 1 | **Shumailov et al.** \"AI Models Collapse When Trained on Recursively Generated Data.\" *Nature* 631, 755–759, 2024. | `shumailov_nature2024` | 首次系统证明迭代合成数据训练导致 model collapse（LLM/VAE/GMM），核心机制为分布尾部消失。 | **领域基石**。定义了我们要解决的问题；他们用事后评估（test loss），我们提供在线监控。 |",
          "-| 2 | **Alemohammad et al.** \"Self-Consuming Generative Models Go MAD.\" *ICLR 2024*. (arXiv: 2307.01850) | ⚠️ **需补入 literature_map.yaml** | 提出 Model Autophagy Disorder (MAD) 框架，分析三类自噬循环（fully synthetic / synthetic augmentation / fresh data）下质量-多样性退化。 | **理论基础**。MAD 框架为我们的迭代合成数据实验设计提供了分类学；他们证明无足够真实数据则 precision 或 recall 必退化。 |",
          "+| 2 | **Alemohammad et al.** \"Self-Consuming Generative Models Go MAD.\" *ICLR 2024*. | `alemohammad_iclr2024` | 提出 Model Autophagy Disorder (MAD) 框架，分析三类自噬循环（fully synthetic / synthetic augmentation / fresh data）下质量-多样性退化。 | **理论基础**。MAD 框架为我们的迭代合成数据实验设计提供了分类学；他们证明无足够真实数据则 precision 或 recall 必退化。 |",
          " | 3 | **Dohmatob, Feng et al.** \"Strong Model Collapse.\" *ICLR 2025 (Spotlight)*. | `dohmatob_iclr2025` | 用算子值自由概率论证明即使极小比例（1/1000）合成数据也导致 collapse，且更大模型放大 collapse。 | **理论支撑**。解释了为什么需要监控——即使少量合成数据也危险；其 fraction 实验与我们的实验设计直接相关。 |",
          "-| 4 | **Seddik et al.** \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse.\" *arXiv 2404.05090*, 2024. | `seddik_2024` | 统计模型严格刻画不同递归训练场景下的 collapse 程度，给出混合训练下合成数据比例安全上限。 | **理论互补**。提供合成数据比例的安全阈值估计，可与我们的监控信号阈值对照验证。 |",
          "-| 5 | **Schaeffer, Kazdan et al.** \"Position: Model Collapse Does Not Mean What You Think.\" *arXiv 2503.03150*, 2025. | `schaeffer_2025` | 梳理 collapse 文献中 8 种不同定义，分为三个家族：test loss 行为、分布形变、缩放行为。 | **定位参考**。论文中需明确我们采用的 collapse 定义；建议采用他们的分类框架。 |",
          "-| 6 | **Shi et al.** \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective.\" *NeurIPS 2025 (Spotlight)*. | `shi_neurips2025` | 揭示 collapse 中从泛化到记忆的转变，发现训练数据熵与泛化能力强线性相关。 | **互补视角**。他们用数据级熵，我们用模型内部训练动态信号；其数据熵可作为我们的外部验证指标。 |",
          "-| 7 | **Bakshi et al.** \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources.\" *arXiv 2602.10531*, 2026. | `bakshi_2026` | 分析真实+合成混合数据的迭代训练长期演化动态，非零真实数据权重（即使递减）可避免 collapse。 | **理论互补**。刻画迭代训练的长期演化规律，为我们的多轮实验设计提供理论预期。 |",
          "+| 4 | **Dohmatob et al.** \"A Tale of Tails: Model Collapse as a Change of Scaling Laws.\" *ICML 2024*, pp. 11165–11197. | `dohmatob_icml2024` | 从 scaling law 视角分析 collapse——揭示 collapse 导致 scaling law 改变，以及 skill un-learning 现象。 | **理论背景**。从 scaling law 角度量化 collapse 严重度；我们用训练动态信号在训练中追踪，他们用事后 scaling 分析。 |",
          "+| 5 | **Seddik et al.** \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse.\" *arXiv 2404.05090*, 2024. | `seddik_2024` | 统计模型严格刻画不同递归训练场景下的 collapse 程度，给出混合训练下合成数据比例安全上限。 | **理论互补**。提供合成数据比例的安全阈值估计，可与我们的监控信号阈值对照验证。 |",
          "+| 6 | **Fu et al.** \"Towards Theoretical Understandings of Self-Consuming Generative Models.\" *ICML 2024*. | `fu_icml2024` | 构建严格理论框架分析 self-consuming loop 中数据分布演化，分析统计/表达/近似三种误差源的复合效应。 | **理论互补**。严格刻画 collapse 的误差复合机制，给出误差增长的理论界，为理解我们监控信号的变化趋势提供理论预期。 |",
          "+| 7 | **Schaeffer, Kazdan et al.** \"Position: Model Collapse Does Not Mean What You Think.\" *arXiv 2503.03150*, 2025. | `schaeffer_2025` | 梳理 collapse 文献中 8 种不同定义，分为三个家族：test loss 行为、分布形变、缩放行为。 | **定位参考**。论文中需明确我们采用的 collapse 定义；建议采用他们的分类框架。 |",
          "+| 8 | **Shi et al.** \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective.\" *NeurIPS 2025 (Spotlight)*. | `shi_neurips2025` | 揭示 collapse 中从泛化到记忆的转变，发现训练数据熵与泛化能力强线性相关。 | **互补视角**。他们用数据级熵，我们用模型内部训练动态信号；其数据熵可作为我们的外部验证指标。 |",
          "+| 9 | **Bakshi et al.** \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources.\" *arXiv 2602.10531*, 2026. | `bakshi_2026` | 分析真实+合成混合数据的迭代训练长期演化动态，非零真实数据权重（即使递减）可避免 collapse。 | **理论互补**。刻画迭代训练的长期演化规律，为我们的多轮实验设计提供理论预期。 |",
          "+| 10 | **Papyan, Han & Donoho.** \"Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training.\" *PNAS* 117(40), 24652–24663, 2020. | `papyan_pnas2020` | 发现分类网络训练末期的 Neural Collapse——类内表征收缩到 Simplex ETF，提出四种 collapse 现象。 | **概念参照**。虽然 neural collapse 与 model collapse 是不同概念，但谱分析方法论可借鉴，且提供 \"collapse\" 概念的对比参考，论文中需明确区分。 |",
          " ",
          " ---",
          " "
        ]
      },
      {
        "oldStart": 28,
        "oldLines": 7,
        "newStart": 31,
        "newLines": 7,
        "lines": [
          " ",
          " | # | 论文 | ID | 核心贡献 | 与我们的关系 |",
          " |---|------|----|----------|-------------|",
          "-| 1 | **Azam et al.** \"SIGMA: Scalable Spectral Insights for LLM Model Collapse.\" *arXiv 2601.03385*, 2026. | `sigma_2026` | 通过 embedding Gram 矩阵的谱分析量化 collapse，推导谱收缩的确定性和随机性界。 | **直接竞争者**。SIGMA 是事后/黑盒方法（用输出嵌入 Gram 矩阵），不需要模型权重，不做 per-layer 分析，不跟踪训练过程动态变化。我们是训练中实时监控，更早期更细粒度。 |",
          "+| 1 | **Gu et al.** \"SIGMA: Scalable Spectral Insights for LLM Model Collapse.\" *arXiv 2601.03385*, 2026. | `sigma_2026` | 通过 embedding Gram 矩阵的谱分析量化 collapse，推导谱收缩的确定性和随机性界。 | **直接竞争者**。SIGMA 是事后/黑盒方法（用输出嵌入 Gram 矩阵），不需要模型权重，不做 per-layer 分析，不跟踪训练过程动态变化。我们是训练中实时监控，更早期更细粒度。 |",
          " | 2 | **Kalinowski.** \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index.\" *arXiv 2604.26984*, 2026. | `kalinowski_2026` | 提出在线拓扑感知监控器（MMHM + Collapse Index），通过稀疏增量更新实现快速在线监控。 | **直接竞争者**。同为在线监控，但信号族完全不同（拓扑 vs 频谱/熵）。我们的信号更轻量、更可解释（stable rank/spectral entropy 有直接线性代数含义）。Kalinowski 不研究迭代合成数据场景。 |",
          " | 3 | **Wyss et al.** \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI.\" *arXiv 2410.12341*, 2024. | `wyss_2024` | 用语义网络和 next-token 概率表征 collapse，引入 collapsed prediction 概念量化多样性损失。 | **相关方法**。用输出级指标（next-token prob），属事后分析；其 synthetic fraction 实验（25%/50%/75%）与我们的实验设计有重叠，可作为 baseline 指标。 |",
          " "
        ]
      },
      {
        "oldStart": 50,
        "oldLines": 6,
        "newStart": 53,
        "newLines": 9,
        "lines": [
          " | 4 | **Yunis, Patel et al.** \"Approaching Deep Learning through the Spectral Dynamics of Weights.\" *arXiv 2408.11804*, 2024. | `yunis_2024` | 以权重奇异值/向量的动态演化为核心视角，证明谱动态可区分记忆网络和泛化网络。 | **方法论基础**。谱动态视角可用于理解 collapse 过程中的权重变化；权重衰减增强低秩偏置的发现与 collapse 中的秩退化相关。 |",
          " | 5 | **Xu.** \"Predicting LLM Compression Degradation from Spectral Statistics.\" *arXiv 2604.18085*, 2026. | `xu_2026` | 用 stable rank 和信息密度预测 LLM 压缩退化（Pearson r=0.890 attention, 0.839 MLP），per-layer 分析。 | **信号验证**。直接验证 stable rank 作为退化预测信号的有效性；虽场景不同（压缩 vs collapse），但支持我们选用 stable rank 的合理性。 |",
          " | 6 | **Conzelmann et al.** \"Layer Collapse in Diffusion Language Models.\" *arXiv 2605.06366*, 2026. | `layer_collapse_diffusion_2026` | 分析 diffusion LM (LLaDA-8B) 中 per-layer activation collapse，发现少数早期层出现 channel-axis collapse。 | **方法论参考**。做了 per-layer collapse 分析，但在 diffusion LM 上；其 activation 分析方法可参考，但场景和模型架构不同。 |",
          "+| 7 | **Lu et al. (AlphaPruning).** \"AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models.\" *NeurIPS 2024*. | `lu_neurips2024` | 用 HT-SR 理论的谱密度形态（alpha exponent）指导 LLM 层级剪枝，LLaMA-7B 可剪至 80% sparsity。 | **方法论验证**。验证 per-layer 谱分析（alpha exponent）对 LLM 质量评估的有效性，支持我们用类似 per-layer 谱方法监控 collapse。 |",
          "+| 8 | **Sanyal, Torr & Dokania.** \"Stable Rank Normalization for Improved Generalization in Neural Networks and GANs.\" *ICLR 2020*. | `sanyal_iclr2020` | 提出 stable rank normalization，理论证明唯一最优解，实验验证控制 stable rank 可改善泛化 gap 11.3%。 | **理论支持**。建立 stable rank 与泛化的直接联系，支持我们选用 stable rank 作为 collapse（泛化退化）的监控信号。 |",
          "+| 9 | **Kalra et al.** \"A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs.\" *arXiv 2601.16979*, 2026. | `kalra_2026` | 提出 critical sharpness（<10 forward passes 高效度量 loss landscape 曲率），首次在 7B 规模验证 progressive sharpening。 | **方法论参考**。高效的大规模 LLM 训练动态度量方法；critical sharpness 可作为我们信号集的潜在补充信号。 |",
          " ",
          " ---",
          " "
        ]
      },
      {
        "oldStart": 63,
        "oldLines": 21,
        "newStart": 69,
        "newLines": 51,
        "lines": [
          " | 2 | **Kazdan et al.** \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World.\" *arXiv 2410.16713*, 2024. | `kazdan_2024` | 系统比较三种工作流：replace（collapse）、accumulate（稳定）、fixed compute（plateau）。 | **互补**。提供实验设计参考——不同工作流下 collapse 行为差异，可用于验证我们的监控信号在不同设定下的灵敏度。 |",
          " | 3 | **Feng et al.** \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification.\" *ICLR 2025*. | `feng_iclr2025` | 用高斯混合模型推导验证器有效的条件，证明即使不完美的验证器也可有效筛选合成数据。 | **互补**。缓解策略方向；我们的监控信号可作为验证器的补充或替代——当 collapse 信号超过阈值时触发干预。 |",
          " | 4 | **Yi et al.** \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence.\" *arXiv 2510.16657*, 2025. | `yi_2025` | 证明外部验证器（人类或更强模型）可阻止 collapse，分析短期改进和长期收敛行为。 | **互补**。与监控方向正交；我们的贡献在于提供何时需要启动验证/干预的信号。 |",
          "+| 5 | **Gillman et al.** \"Self-Correcting Self-Consuming Loops for Generative Model Training.\" *ICML 2024*. | `gillman_icml2024` | 引入 correction function 使 self-consuming loop 指数级更稳定，即使 synthetic:real = 100:1 也可避免 collapse。 | **互补**。缓解策略方向；correction function 概念与在线监控互补——我们的信号可指导何时激活 correction。 |",
          " ",
          " ---",
          " ",
          "+## E. 合成数据污染检测",
          "+",
          "+检测训练数据中是否含有合成数据是 collapse 监控的上游问题。水印方法标记合成文本，检测方法识别机器生成内容。这些工作与我们的方向互补：它们回答\"是否用了合成数据\"，我们回答\"合成数据造成了多严重的 collapse\"。",
          "+",
          "+| # | 论文 | ID | 核心贡献 | 与我们的关系 |",
          "+|---|------|----|----------|-------------|",
          "+| 1 | **Kirchenbauer et al.** \"A Watermark for Large Language Models.\" *ICML 2023*, pp. 17061–17084. | `kirchenbauer_icml2023` | LLM 文本水印框架——green/red token list + soft promotion + 统计检测，开源检测算法不需模型访问。 | **互补**。合成数据溯源的基础方法；可标记合成数据以便追踪其在迭代训练中的传播。 |",
          "+| 2 | **Dathathri et al.** \"Scalable Watermarking for Identifying Large Language Model Outputs.\" *Nature* 634, 818–823, 2024. | `dathathri_nature2024` | SynthID-Text：产品级文本水印，与 speculative sampling 集成，在 Gemini ~20M 响应上验证。 | **互补**。大规模合成数据标记的工业实践，展示水印在产品级规模上的可行性。 |",
          "+| 3 | **Sander et al.** \"Watermarking Makes Language Models Radioactive.\" *NeurIPS 2024*. | `sander_neurips2024` | 证明在水印 LLM 输出上微调的模型保留水印残留（\"放射性\"），可检测模型是否在合成数据上训练。 | **直接相关**。检测合成数据训练的替代方法；他们检测\"是否用了合成数据\"，我们监控\"合成数据造成多严重的 collapse\"。 |",
          "+| 4 | **Mitchell et al. (DetectGPT).** \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.\" *ICML 2023*, pp. 24950–24962. | `mitchell_icml2023` | LLM 生成文本占据 log-probability 负曲率区域，据此零样本检测，0.95 AUROC 检测 GPT-NeoX 20B 生成的假新闻。 | **互补**。合成文本检测方法，可识别训练数据中的合成成分，为 collapse 监控提供数据侧信息。 |",
          "+| 5 | **Shi et al. (Min-K%).** \"Detecting Pretraining Data from Large Language Models.\" *ICLR 2024*. | `shi_iclr2024` | Min-K% Prob：未见样本含低概率 outlier word，据此检测预训练数据成员，比 reference model 方法提升 7.4%。 | **互补**。数据污染检测工具——可检测合成数据是否混入训练集，与 collapse 监控互补。 |",
          "+",
          "+---",
          "+",
          "+## F. 数据质量与评估",
          "+",
          "+高质量训练数据是避免 collapse 的前提。数据质量评估框架为理解 collapse 的数据侧原因提供分析工具。",
          "+",
          "+| # | 论文 | ID | 核心贡献 | 与我们的关系 |",
          "+|---|------|----|----------|-------------|",
          "+| 1 | **Penedo et al.** \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale.\" *arXiv 2406.17557*, 2024. | `penedo_2024` | 15T token 数据集的完整策略文档——去重、过滤、教育文本提取，详细 ablation 各种数据质量策略。 | **数据质量参考**。理解高质量训练数据标准，为分析 collapse 的数据原因提供基线。 |",
          "+| 2 | **Zhang et al.** \"The LLM Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data.\" *arXiv 2601.17717*, 2026. | `zhang_2026` | 系统分类合成数据评估指标——quality (validity/fidelity/utility) + trustworthiness (safety/faithfulness)。 | **评估框架参考**。从内在属性评估合成数据质量的分类体系，为理解 collapse 的数据级原因提供指标视角。 |",
          "+",
          "+---",
          "+",
          " ## 覆盖检查",
          " ",
          "-### literature_map.yaml 全部 19 篇论文分配",
          "+### literature_map.yaml 全部 34 篇论文分配",
          " ",
          " | ID | 类别 |",
          " |----|------|",
          " | `shumailov_nature2024` | A |",
          "+| `alemohammad_iclr2024` | A |",
          " | `dohmatob_iclr2025` | A |",
          "+| `dohmatob_icml2024` | A |",
          " | `seddik_2024` | A |",
          "+| `fu_icml2024` | A |",
          " | `schaeffer_2025` | A |",
          " | `shi_neurips2025` | A |",
          " | `bakshi_2026` | A |",
          "+| `papyan_pnas2020` | A |",
          " | `sigma_2026` | B |",
          " | `kalinowski_2026` | B |",
          " | `wyss_2024` | B |"
        ]
      },
      {
        "oldStart": 87,
        "oldLines": 23,
        "newStart": 123,
        "newLines": 28,
        "lines": [
          " | `yunis_2024` | C |",
          " | `xu_2026` | C |",
          " | `layer_collapse_diffusion_2026` | C |",
          "+| `lu_neurips2024` | C |",
          "+| `sanyal_iclr2020` | C |",
          "+| `kalra_2026` | C |",
          " | `gerstgrasser_2024` | D |",
          " | `kazdan_2024` | D |",
          " | `feng_iclr2025` | D |",
          " | `yi_2025` | D |",
          "+| `gillman_icml2024` | D |",
          "+| `kirchenbauer_icml2023` | E |",
          "+| `dathathri_nature2024` | E |",
          "+| `sander_neurips2024` | E |",
          "+| `mitchell_icml2023` | E |",
          "+| `shi_iclr2024` | E |",
          "+| `penedo_2024` | F |",
          "+| `zhang_2026` | F |",
          " ",
          "-### 需补入 literature_map.yaml 的论文",
          "-",
          "-- **Alemohammad et al. (2024)** \"Self-Consuming Generative Models Go MAD.\" ICLR 2024. arXiv: 2307.01850",
          "-  - 分类至 A（理论基础）",
          "-  - relation: foundation",
          "-  - 建议 id: `alemohammad_iclr2024`",
          "-",
          " ---",
          " ",
          " ## 论文写作备注",
          " ",
          "-1. **开篇逻辑**: A → B → C → D，从\"问题是什么\"到\"谁在检测\"到\"用什么工具\"到\"如何缓解\"",
          "+1. **开篇逻辑**: A → B → C → D → E → F，从\"问题是什么\"到\"谁在检测\"到\"用什么工具\"到\"如何缓解\"到\"数据侧检测与质量\"",
          " 2. **核心 positioning 句**: \"To the best of our knowledge, no prior work simultaneously achieves (a) online monitoring during training, (b) spectral/entropy training dynamics signals, (c) per-layer granularity, and (d) validation in the iterative synthetic data training setting.\"",
          " 3. **Collapse 定义**: 采用 Schaeffer et al. (2025) 的分类框架，明确我们关注的是 test loss degradation + distribution tail collapse",
          "-4. **Alemohammad 2024 必须引用**: Reviewer 之前指出缺失，与 Shumailov 2024 共同构成问题定义的基石",
          "+4. **Alemohammad 2024 必须引用**: 与 Shumailov 2024 共同构成问题定义的基石",
          "+5. **Neural Collapse 区分**: 引用 Papyan et al. (2020) 时需明确区分 neural collapse（训练末期分类器现象）与 model collapse（合成数据迭代退化）"
        ]
      }
    ],
    "originalFile": "# Related Work 结构大纲\n\n> **项目**: collapse_severity_monitor — 在线监控模型 collapse 严重度\n> **目标会议**: EMNLP 2026 ARR\n> **基于**: literature_map.yaml (19 篇) + 1 篇补充 (Alemohammad 2024)\n\n---\n\n## A. Model Collapse: 理论基础与实证\n\nModel collapse 指在合成数据上迭代训练导致模型质量不可逆退化的现象。自 Shumailov et al. (2024) 在 Nature 上首次系统性证明以来，理论和实证研究迅速发展，从分布尾部消失、缩放定律失效到术语统一均有深入探讨。我们的工作建立在这些理论基础之上，旨在提供训练过程中的实时监控手段。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Shumailov et al.** \"AI Models Collapse When Trained on Recursively Generated Data.\" *Nature* 631, 755–759, 2024. | `shumailov_nature2024` | 首次系统证明迭代合成数据训练导致 model collapse（LLM/VAE/GMM），核心机制为分布尾部消失。 | **领域基石**。定义了我们要解决的问题；他们用事后评估（test loss），我们提供在线监控。 |\n| 2 | **Alemohammad et al.** \"Self-Consuming Generative Models Go MAD.\" *ICLR 2024*. (arXiv: 2307.01850) | ⚠️ **需补入 literature_map.yaml** | 提出 Model Autophagy Disorder (MAD) 框架，分析三类自噬循环（fully synthetic / synthetic augmentation / fresh data）下质量-多样性退化。 | **理论基础**。MAD 框架为我们的迭代合成数据实验设计提供了分类学；他们证明无足够真实数据则 precision 或 recall 必退化。 |\n| 3 | **Dohmatob, Feng et al.** \"Strong Model Collapse.\" *ICLR 2025 (Spotlight)*. | `dohmatob_iclr2025` | 用算子值自由概率论证明即使极小比例（1/1000）合成数据也导致 collapse，且更大模型放大 collapse。 | **理论支撑**。解释了为什么需要监控——即使少量合成数据也危险；其 fraction 实验与我们的实验设计直接相关。 |\n| 4 | **Seddik et al.** \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse.\" *arXiv 2404.05090*, 2024. | `seddik_2024` | 统计模型严格刻画不同递归训练场景下的 collapse 程度，给出混合训练下合成数据比例安全上限。 | **理论互补**。提供合成数据比例的安全阈值估计，可与我们的监控信号阈值对照验证。 |\n| 5 | **Schaeffer, Kazdan et al.** \"Position: Model Collapse Does Not Mean What You Think.\" *arXiv 2503.03150*, 2025. | `schaeffer_2025` | 梳理 collapse 文献中 8 种不同定义，分为三个家族：test loss 行为、分布形变、缩放行为。 | **定位参考**。论文中需明确我们采用的 collapse 定义；建议采用他们的分类框架。 |\n| 6 | **Shi et al.** \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective.\" *NeurIPS 2025 (Spotlight)*. | `shi_neurips2025` | 揭示 collapse 中从泛化到记忆的转变，发现训练数据熵与泛化能力强线性相关。 | **互补视角**。他们用数据级熵，我们用模型内部训练动态信号；其数据熵可作为我们的外部验证指标。 |\n| 7 | **Bakshi et al.** \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources.\" *arXiv 2602.10531*, 2026. | `bakshi_2026` | 分析真实+合成混合数据的迭代训练长期演化动态，非零真实数据权重（即使递减）可避免 collapse。 | **理论互补**。刻画迭代训练的长期演化规律，为我们的多轮实验设计提供理论预期。 |\n\n---\n\n## B. Collapse 检测与监控方法\n\n现有 collapse 检测方法主要分为事后评估（test loss、分布指标）和在线监控两类。直接竞争者包括基于谱分析的 SIGMA 和基于拓扑信号的 Kalinowski 方法。**我们的独特定位**：在线 + 频谱/熵训练动态信号 + per-layer 粒度 + 迭代合成数据场景，这一组合目前无人覆盖。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Azam et al.** \"SIGMA: Scalable Spectral Insights for LLM Model Collapse.\" *arXiv 2601.03385*, 2026. | `sigma_2026` | 通过 embedding Gram 矩阵的谱分析量化 collapse，推导谱收缩的确定性和随机性界。 | **直接竞争者**。SIGMA 是事后/黑盒方法（用输出嵌入 Gram 矩阵），不需要模型权重，不做 per-layer 分析，不跟踪训练过程动态变化。我们是训练中实时监控，更早期更细粒度。 |\n| 2 | **Kalinowski.** \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index.\" *arXiv 2604.26984*, 2026. | `kalinowski_2026` | 提出在线拓扑感知监控器（MMHM + Collapse Index），通过稀疏增量更新实现快速在线监控。 | **直接竞争者**。同为在线监控，但信号族完全不同（拓扑 vs 频谱/熵）。我们的信号更轻量、更可解释（stable rank/spectral entropy 有直接线性代数含义）。Kalinowski 不研究迭代合成数据场景。 |\n| 3 | **Wyss et al.** \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI.\" *arXiv 2410.12341*, 2024. | `wyss_2024` | 用语义网络和 next-token 概率表征 collapse，引入 collapsed prediction 概念量化多样性损失。 | **相关方法**。用输出级指标（next-token prob），属事后分析；其 synthetic fraction 实验（25%/50%/75%）与我们的实验设计有重叠，可作为 baseline 指标。 |\n\n### 我们的定位（论文中需强调）\n\n> 现有方法要么是事后/黑盒分析（SIGMA），要么用非频谱信号（Kalinowski 的拓扑方法），要么仅关注输出级指标（Wyss）。本工作首次将频谱/熵训练动态信号（spectral entropy、stable rank、output token entropy）以 per-layer 粒度应用于迭代合成数据训练中的在线 collapse 监控。\n\n---\n\n## C. 训练动态分析与诊断\n\n频谱分析和训练动态诊断是深度学习中成熟的研究方向。WeightWatcher 等工具已证明权重矩阵的谱性质（stable rank、power law exponent）可有效评估模型质量。我们将这些方法论工具从通用训练诊断延伸到 collapse 监控这一特定场景。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Martin & Mahoney.** \"Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data.\" *Nature Communications* 12, 2021. | `martin_mahoney_2021` | WeightWatcher 工具——用 RMT 分析权重矩阵谱性质（stable rank、power law α、spectral norm），无需训练/测试数据即可预测模型质量。 | **方法论基础**。WeightWatcher 的 stable rank 和谱分析方法直接启发我们的信号设计；其 5+1 训练阶段分类可用于解释 collapse 过程中的谱形态变化。 |\n| 2 | **Liu et al. (Spectral Lens).** \"Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization.\" *arXiv 2605.05683*, 2026. | `spectral_lens_2026` | 用 activation covariance 和 per-sample gradient 的 SVD 谱作为 LLM 训练优化诊断工具。 | **方法论高度相关**。同样用频谱分析训练动态，但关注优化诊断而非 collapse/合成数据退化；其 per-layer 分析方法可参考。 |\n| 3 | **Chen & Liu.** \"Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy.\" *IEEE CISS 2024*. | `chen_liu_2024` | 提出 Diffusion Spectral Entropy (DSE) 和 DSMI，利用数据几何在高维中可靠计算信息论指标。 | **方法论工具**。DSE 是我们 spectral entropy 信号的潜在替代实现；其 DSE 随训练增加、DSMI 在过拟合时停滞的发现可为 collapse 检测提供参照。 |\n| 4 | **Yunis, Patel et al.** \"Approaching Deep Learning through the Spectral Dynamics of Weights.\" *arXiv 2408.11804*, 2024. | `yunis_2024` | 以权重奇异值/向量的动态演化为核心视角，证明谱动态可区分记忆网络和泛化网络。 | **方法论基础**。谱动态视角可用于理解 collapse 过程中的权重变化；权重衰减增强低秩偏置的发现与 collapse 中的秩退化相关。 |\n| 5 | **Xu.** \"Predicting LLM Compression Degradation from Spectral Statistics.\" *arXiv 2604.18085*, 2026. | `xu_2026` | 用 stable rank 和信息密度预测 LLM 压缩退化（Pearson r=0.890 attention, 0.839 MLP），per-layer 分析。 | **信号验证**。直接验证 stable rank 作为退化预测信号的有效性；虽场景不同（压缩 vs collapse），但支持我们选用 stable rank 的合理性。 |\n| 6 | **Conzelmann et al.** \"Layer Collapse in Diffusion Language Models.\" *arXiv 2605.06366*, 2026. | `layer_collapse_diffusion_2026` | 分析 diffusion LM (LLaDA-8B) 中 per-layer activation collapse，发现少数早期层出现 channel-axis collapse。 | **方法论参考**。做了 per-layer collapse 分析，但在 diffusion LM 上；其 activation 分析方法可参考，但场景和模型架构不同。 |\n\n---\n\n## D. Collapse 缓解策略\n\n缓解策略主要分为数据管理（累积 vs 替换、混合比例控制）和数据筛选/验证两类。这些工作与我们的监控方向互补——我们负责检测 collapse 何时发生及严重程度，它们负责干预和缓解。\n\n| # | 论文 | ID | 核心贡献 | 与我们的关系 |\n|---|------|----|----------|-------------|\n| 1 | **Gerstgrasser, Schaeffer et al.** \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data.\" *arXiv 2404.01413*, 2024. | `gerstgrasser_2024` | 证明数据累积（而非替换）可避免 collapse；替换导致 test error 增长，累积则有有限上界。 | **互补**。他们研究何时 collapse（数据管理策略），我们研究如何实时检测 collapse；累积 vs 替换的差异可作为我们监控信号的验证场景。 |\n| 2 | **Kazdan et al.** \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World.\" *arXiv 2410.16713*, 2024. | `kazdan_2024` | 系统比较三种工作流：replace（collapse）、accumulate（稳定）、fixed compute（plateau）。 | **互补**。提供实验设计参考——不同工作流下 collapse 行为差异，可用于验证我们的监控信号在不同设定下的灵敏度。 |\n| 3 | **Feng et al.** \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification.\" *ICLR 2025*. | `feng_iclr2025` | 用高斯混合模型推导验证器有效的条件，证明即使不完美的验证器也可有效筛选合成数据。 | **互补**。缓解策略方向；我们的监控信号可作为验证器的补充或替代——当 collapse 信号超过阈值时触发干预。 |\n| 4 | **Yi et al.** \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence.\" *arXiv 2510.16657*, 2025. | `yi_2025` | 证明外部验证器（人类或更强模型）可阻止 collapse，分析短期改进和长期收敛行为。 | **互补**。与监控方向正交；我们的贡献在于提供何时需要启动验证/干预的信号。 |\n\n---\n\n## 覆盖检查\n\n### literature_map.yaml 全部 19 篇论文分配\n\n| ID | 类别 |\n|----|------|\n| `shumailov_nature2024` | A |\n| `dohmatob_iclr2025` | A |\n| `seddik_2024` | A |\n| `schaeffer_2025` | A |\n| `shi_neurips2025` | A |\n| `bakshi_2026` | A |\n| `sigma_2026` | B |\n| `kalinowski_2026` | B |\n| `wyss_2024` | B |\n| `martin_mahoney_2021` | C |\n| `spectral_lens_2026` | C |\n| `chen_liu_2024` | C |\n| `yunis_2024` | C |\n| `xu_2026` | C |\n| `layer_collapse_diffusion_2026` | C |\n| `gerstgrasser_2024` | D |\n| `kazdan_2024` | D |\n| `feng_iclr2025` | D |\n| `yi_2025` | D |\n\n### 需补入 literature_map.yaml 的论文\n\n- **Alemohammad et al. (2024)** \"Self-Consuming Generative Models Go MAD.\" ICLR 2024. arXiv: 2307.01850\n  - 分类至 A（理论基础）\n  - relation: foundation\n  - 建议 id: `alemohammad_iclr2024`\n\n---\n\n## 论文写作备注\n\n1. **开篇逻辑**: A → B → C → D，从\"问题是什么\"到\"谁在检测\"到\"用什么工具\"到\"如何缓解\"\n2. **核心 positioning 句**: \"To the best of our knowledge, no prior work simultaneously achieves (a) online monitoring during training, (b) spectral/entropy training dynamics signals, (c) per-layer granularity, and (d) validation in the iterative synthetic data training setting.\"\n3. **Collapse 定义**: 采用 Schaeffer et al. (2025) 的分类框架，明确我们关注的是 test loss degradation + distribution tail collapse\n4. **Alemohammad 2024 必须引用**: Reviewer 之前指出缺失，与 Shumailov 2024 共同构成问题定义的基石\n",
    "userModified": false
  },
  "sourceToolAssistantUUID": "8d28dfaf-c652-4665-852f-b88d4d07091a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "leafUuid": "f0516800-5694-4b15-a4b1-25af58cff6db",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Update related work outline with 14 new papers",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2"
}
```

---

### Assistant

_source line 21 · 2026-05-14T22:50:10.596Z_

更新完成。变更总结：

- 论文总数 20 → 34（+14 篇）
- **A 节** +3 篇：dohmatob_icml2024（scaling law 视角）、fu_icml2024（self-consuming 理论框架）、papyan_pnas2020（Neural Collapse 概念参照）
- **C 节** +3 篇：lu_neurips2024（AlphaPruning 谱剪枝）、sanyal_iclr2020（stable rank 与泛化联系）、kalra_2026（critical sharpness）
- **D 节** +1 篇：gillman_icml2024（self-correcting loops）
- **E 节** 新增"合成数据污染检测"：kirchenbauer_icml2023、dathathri_nature2024、sander_neurips2024、mitchell_icml2023、shi_iclr2024（5 篇）
- **F 节** 新增"数据质量与评估"：penedo_2024、zhang_2026（2 篇）
- 覆盖检查表更新为 34 篇全覆盖

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0516800-5694-4b15-a4b1-25af58cff6db",
  "isSidechain": false,
  "requestId": "req_011Cb3H7Snp6DpQh2JKXLtBt",
  "type": "assistant",
  "uuid": "be180e79-6e41-45c2-a982-963cc8261292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNgR9nWh7LJ9WT2ekUK5ZG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9143,
      "cache_read_input_tokens": 40869,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 315,
          "cache_read_input_tokens": 40869,
          "cache_creation_input_tokens": 9143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9143
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

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "leafUuid": "be180e79-6e41-45c2-a982-963cc8261292",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Update related work outline with 14 new papers",
  "sessionId": "f3293d8b-d52b-4e7e-b888-7f2458dc2ce2"
}
```

---
