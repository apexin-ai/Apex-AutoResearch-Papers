# Research conversation: <project_context> # 项目: collapse_severity_monitor ## 运行环境 - 服务器名: autodl-5090 - SSH 账户: root（调用 ssh_execute / submit_tra

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/94a01d86-ec14-4786-834e-1e6883edfb12.jsonl`
- **Structured JSON:** [`13fd48e55c3486555bca.json`](../../sessions/13/13fd48e55c3486555bca.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T22:41:58.699Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T22:41:58.699Z",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "content": "&lt;project_context>\n# 项目: collapse_severity_monitor\n\n## 运行环境\n- 服务器名: autodl-5090\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/collapse_severity_monitor\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n检查当前项目的文献和论文准备状态。\n\n**任务**：\n1. 读取 `literature_map.yaml`，统计总论文数量、各 category 数量\n2. 读取 `artifacts/references.bib`，统计 BibTeX 条目数\n3. 读取 `docs/related_work_outline.md`，检查引用数量是否 ≥20\n4. 读取 `artifacts/figure_design.md`，确认图表设计方案\n5. 读取 `artifacts/annotated_bibliography.md`，确认标注状况\n\n**产出**：简要状态报告（每项一行），包括具体数量。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T22:41:58.703Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T22:41:58.703Z",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-14T22:41:58.738Z_

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
检查当前项目的文献和论文准备状态。

**任务**：
1. 读取 `literature_map.yaml`，统计总论文数量、各 category 数量
2. 读取 `artifacts/references.bib`，统计 BibTeX 条目数
3. 读取 `docs/related_work_outline.md`，检查引用数量是否 ≥20
4. 读取 `artifacts/figure_design.md`，确认图表设计方案
5. 读取 `artifacts/annotated_bibliography.md`，确认标注状况

**产出**：简要状态报告（每项一行），包括具体数量。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "985e4d4c-de63-470a-9f8d-580809be0b1f",
  "type": "user",
  "uuid": "91e67413-6464-4f53-9d65-d3c299add09b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T22:41:58.738Z_

```json
{
  "parentUuid": "91e67413-6464-4f53-9d65-d3c299add09b",
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
  "uuid": "63a37354-e102-4993-98e4-a899bda37050",
  "timestamp": "2026-05-14T22:41:58.738Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T22:41:58.738Z_

```json
{
  "parentUuid": "63a37354-e102-4993-98e4-a899bda37050",
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
  "uuid": "e78c4078-a716-4a04-8ca5-24a5caee5f88",
  "timestamp": "2026-05-14T22:41:58.738Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T22:41:58.738Z_

```json
{
  "parentUuid": "e78c4078-a716-4a04-8ca5-24a5caee5f88",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0c739089-6416-4dd2-88f7-1dcf7064e062",
  "timestamp": "2026-05-14T22:41:58.738Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
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
  "aiTitle": "Check literature and paper preparation status",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12"
}
```

---

### Assistant

_source line 8 · 2026-05-14T22:42:03.609Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read all the requested files in parallel to gather the information needed for the status report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c739089-6416-4dd2-88f7-1dcf7064e062",
  "isSidechain": false,
  "requestId": "req_011Cb3GVnD7VUQqXo5vcooxc",
  "type": "assistant",
  "uuid": "061d709b-d637-48cb-b136-3ff12f7722d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVtC9qKfmcxd2antjmGysX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10922,
      "cache_read_input_tokens": 11841,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10922,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 119,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10922,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10922
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

_source line 9 · 2026-05-14T22:42:04.131Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NVtJ2GCufmgspEoR22tW5o`</summary>

```json
{
  "pattern": "**/{literature_map.yaml,references.bib,related_work_outline.md,figure_design.md,annotated_bibliography.md}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "061d709b-d637-48cb-b136-3ff12f7722d3",
  "isSidechain": false,
  "requestId": "req_011Cb3GVnD7VUQqXo5vcooxc",
  "type": "assistant",
  "uuid": "f72951a2-d783-4796-bf83-a06712e9cb8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVtC9qKfmcxd2antjmGysX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10922,
      "cache_read_input_tokens": 11841,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10922,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 119,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10922,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10922
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

_source line 10 · 2026-05-14T22:42:04.145Z_

<details><summary>↩ Tool result · `toolu_01NVtJ2GCufmgspEoR22tW5o`</summary>

```text
artifacts/_project/report/literature_map.yaml
artifacts/literature_map.yaml
docs/related_work_outline.md
artifacts/_project/intermediate/related_work_outline.md
artifacts/_project/paper/references.bib
artifacts/references.bib
artifacts/_project/report/figure_design.md
artifacts/figure_design.md
artifacts/_project/paper/annotated_bibliography.md
artifacts/annotated_bibliography.md
literature_map.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f72951a2-d783-4796-bf83-a06712e9cb8f",
  "isSidechain": false,
  "promptId": "985e4d4c-de63-470a-9f8d-580809be0b1f",
  "type": "user",
  "uuid": "bbc930b5-1a5f-4ad5-a6ab-116ca3b9a7e8",
  "toolUseResult": {
    "filenames": [
      "artifacts/_project/report/literature_map.yaml",
      "artifacts/literature_map.yaml",
      "docs/related_work_outline.md",
      "artifacts/_project/intermediate/related_work_outline.md",
      "artifacts/_project/paper/references.bib",
      "artifacts/references.bib",
      "artifacts/_project/report/figure_design.md",
      "artifacts/figure_design.md",
      "artifacts/_project/paper/annotated_bibliography.md",
      "artifacts/annotated_bibliography.md",
      "literature_map.yaml"
    ],
    "durationMs": 6,
    "numFiles": 11,
    "truncated": false
  },
  "sourceToolAssistantUUID": "f72951a2-d783-4796-bf83-a06712e9cb8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T22:42:07.543Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y5dEhybXE2QbjSn7BwUUnc`</summary>

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
  "parentUuid": "bbc930b5-1a5f-4ad5-a6ab-116ca3b9a7e8",
  "isSidechain": false,
  "requestId": "req_011Cb3GWBP8qSjoabQ1rozXo",
  "type": "assistant",
  "uuid": "58a6484d-ee17-4d5d-a802-8bad846e730d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5tctSX7vDf1AdBwGUC2Hr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 22763,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 367,
          "cache_read_input_tokens": 22763,
          "cache_creation_input_tokens": 240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 240
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

_source line 12 · 2026-05-14T22:42:07.551Z_

<details><summary>↩ Tool result · `toolu_01Y5dEhybXE2QbjSn7BwUUnc`</summary>

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
19	    authors: [Azam et al.]
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
  "parentUuid": "58a6484d-ee17-4d5d-a802-8bad846e730d",
  "isSidechain": false,
  "promptId": "985e4d4c-de63-470a-9f8d-580809be0b1f",
  "type": "user",
  "uuid": "e800f1c9-60b2-42eb-8635-815ace8fdf49",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/literature_map.yaml",
      "content": "# Literature Map — collapse_severity_monitor\n# 最后更新: 2026-05-14 (expanded to 34 papers)\n# 研究方向: 在线监控模型 collapse 严重度——用训练动态信号实时跟踪迭代合成数据训练中的质量退化\n\n# ============================================================\n# 竞争关系分类说明:\n#   direct_competitor  — 解决同一问题（在线监控 collapse）\n#   related            — 解决相近问题或使用相关方法\n#   complementary      — 互补（提供理论基础/工具/缓解策略）\n#   foundation         — 领域基础工作\n# ============================================================\n\npapers:\n\n  # ===================== DIRECT COMPETITORS =====================\n\n  - id: sigma_2026\n    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n    authors: [Azam et al.]\n    year: 2026\n    venue: arXiv (2601.03385)\n    relation: direct_competitor\n    core_method: >\n      通过 embedding Gram 矩阵的谱分析来量化 model collapse 程度。\n      推导 Gram 矩阵谱的确定性和随机性界，用谱收缩作为 collapse 指标。\n    signals: [Gram matrix spectrum, rank deficiency, spectral bounds]\n    scale: model-level (output embeddings)\n    key_findings:\n      - Gram 矩阵满秩是 LLM 正常运作的必要条件\n      - 秩亏缺意味着语义级信息丢失，标志 collapse 开始\n      - 随机公式使框架可扩展至大规模模型\n    vs_ours: >\n      SIGMA 用输出嵌入的 Gram 矩阵谱，是事后/黑盒方法，不需要模型权重。\n      我们用训练动态信号（权重频谱熵、stable rank、token entropy），\n      是训练中实时监控，更早期更细粒度（per-layer）。\n      SIGMA 不做 per-layer 分析，不跟踪训练过程的动态变化。\n    threat_level: medium\n\n  - id: kalinowski_2026\n    title: \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\"\n    authors: [Alexander Kalinowski]\n    year: 2026\n    venue: arXiv (2604.26984)\n    relation: direct_competitor\n    core_method: >\n      提出在线拓扑感知监控器，结合 Modular Morse Homology Maintenance (MMHM)\n      和复合 Collapse Index (CI)，通过稀疏增量更新实现快速在线监控。\n    signals: [persistent homology, Collapse Index (CI), topological features]\n    scale: model-level (representation space topology)\n    key_findings:\n      - CI 在 LLM fine-tuning 和时序 KGE 训练中提供低延迟早期预警\n      - 表征各向异性和多尺度结构丧失在性能指标反应之前就可检测\n      - 增量更新避免每个 epoch 重建复形\n    vs_ours: >\n      Kalinowski 用拓扑信号（persistent homology），我们用频谱/熵信号。\n      两者都是在线监控，但信号族完全不同。我们的信号更轻量、\n      更可解释（stable rank/spectral entropy 有直接的线性代数含义）。\n      Kalinowski 不研究迭代合成数据训练场景。\n    threat_level: medium\n\n  # ===================== CLOSELY RELATED =====================\n\n  - id: spectral_lens_2026\n    title: \"Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization\"\n    authors: [Andy Zeyi Liu et al.]\n    year: 2026\n    venue: arXiv (2605.05683)\n    relation: related\n    core_method: >\n      用 activation covariance 和 per-sample gradient 的 SVD 谱\n      作为 LLM 训练优化的诊断工具。\n    signals: [activation covariance spectrum, gradient SVD spectrum]\n    scale: layer-level\n    key_findings:\n      - batch size 是表示几何的隐藏决定因素\n      - 早期训练的 activation covariance 尾部可预测下游 token 效率\n      - activation 谱头部运动 + gradient 谱可区分学习侧和执行侧改进\n    vs_ours: >\n      方法论高度相关——同样用频谱分析训练动态。\n      但他们关注优化诊断，不研究 collapse/合成数据退化。\n      可作为方法论参考。\n    threat_level: low\n\n  - id: shi_neurips2025\n    title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n    authors: [Lianghe Shi, Meng Wu, Huijie Zhang, Zekai Zhang, Molei Tao, Qing Qu]\n    year: 2025\n    venue: NeurIPS 2025 (Spotlight)\n    relation: related\n    core_method: >\n      揭示 model collapse 中从泛化到记忆的转变。\n      发现训练数据熵与模型泛化能力的强线性相关。\n      提出基于熵的子集选择方法来减缓 collapse。\n    signals: [dataset entropy, generalization metrics]\n    scale: model-level (data distribution)\n    key_findings:\n      - 迭代训练中数据分布熵急剧下降导致泛化能力下降\n      - 强线性相关：训练数据集熵与模型泛化能力\n      - 熵选择方法有效减缓泛化到记忆转变\n    vs_ours: >\n      他们用数据级别的熵，我们用模型内部的训练动态信号。\n      互补：他们的数据熵可作为我们的外部验证指标。\n      他们不做 per-layer 分析，不做在线监控。\n    threat_level: low\n\n  - id: wyss_2024\n    title: \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\"\n    authors: [C. M. Wyss et al.]\n    year: 2024\n    venue: arXiv (2410.12341)\n    relation: related\n    core_method: >\n      用语义网络和 next-token 概率来表征 LLM 中的 model collapse。\n      引入 collapsed prediction 概念量化多样性损失。\n      分析不同合成 token 比例 (25%/50%/75%) 对 collapse 的影响。\n    signals: [next-token probability distribution, semantic network metrics, collapsed prediction ratio]\n    scale: token-level (output)\n    key_findings:\n      - Next-token 概率分布可精确量化多样性损失\n      - 合成 token 比例越高，collapse 越严重\n      - 跨数据集迁移：在非微调数据集上 collapse 程度不同\n    vs_ours: >\n      他们用输出级指标（next-token prob），我们用训练动态内部信号。\n      他们的 synthetic fraction 实验与我们的实验设计有重叠。\n      不同之处：他们是事后分析，我们是训练中在线监控。\n    threat_level: low\n\n  - id: xu_2026\n    title: \"Predicting LLM Compression Degradation from Spectral Statistics\"\n    authors: [Mingxue Xu]\n    year: 2026\n    venue: arXiv (2604.18085)\n    relation: related\n    core_method: >\n      用 stable rank 和信息密度 (bits/param) 预测 LLM 压缩导致的退化。\n      交互项 compression_ratio * stable_rank 是退化的强预测器。\n    signals: [stable rank, information density, compression ratio]\n    scale: layer-level (attention vs MLP 分开分析)\n    key_findings:\n      - stable rank 是压缩退化的主要预测因子（Pearson r=0.890 attention, 0.839 MLP）\n      - 层类型比压缩方法更重要\n      - layer-specific calibration 优于 method-specific tuning\n    vs_ours: >\n      直接验证 stable rank 作为退化预测信号的有效性。\n      虽然场景不同（压缩 vs collapse），但支持我们选用 stable rank 的合理性。\n      他们的 per-layer 分析方法可参考。\n    threat_level: low\n\n  - id: layer_collapse_diffusion_2026\n    title: \"Layer Collapse in Diffusion Language Models\"\n    authors: [Alexander Conzelmann, Albert Catalan-Tatjer, Shiwei Liu]\n    year: 2026\n    venue: arXiv (2605.06366)\n    relation: related\n    core_method: >\n      分析 diffusion language model (LLaDA-8B) 中的 per-layer activation 动态，\n      发现少数早期层展现 collapsed activation patterns。\n    signals: [activation patterns, super-outlier magnitude]\n    scale: layer-level\n    key_findings:\n      - 几个早期层出现 channel-axis collapse（单一维度主导所有位置）\n      - 尽管看似冗余，pruning outlier 导致退化为重复随机 token 循环\n      - Diffusion LM 与 autoregressive LM 的 collapse 行为不同\n    vs_ours: >\n      做了 per-layer collapse 分析，但在 diffusion LM 上。\n      方法论参考：per-layer activation 分析方法。\n    threat_level: low\n\n  # ===================== FOUNDATION =====================\n\n  - id: alemohammad_iclr2024\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: [Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk]\n    year: 2024\n    venue: ICLR 2024\n    relation: foundation\n    core_method: >\n      定义三种 autophagous loop（fully synthetic / synthetic augmentation / fresh data），\n      证明无足够真实数据时 precision 或 recall 必然下降（MAD 现象）。\n    signals: [FID, precision, recall]\n    scale: model-level (image generative models)\n    key_findings:\n      - 三种 loop 类型的 collapse 行为不同\n      - 无 fresh data 时 quality 或 diversity 必然退化\n      - 在 StyleGAN、DDPM、denoising diffusion 上验证\n    vs_ours: >\n      领域基础论文之一。他们的 loop 分类框架直接对应我们的实验设计。\n      他们用 FID/precision/recall（事后指标），我们提供训练中在线信号。\n\n  - id: papyan_pnas2020\n    title: \"Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training\"\n    authors: [Vardan Papyan, X. Y. Han, David L. Donoho]\n    year: 2020\n    venue: PNAS 117(40), 24652-24663\n    relation: foundation\n    core_method: >\n      发现分类网络训练末期的 Neural Collapse——类内表征收缩到 Simplex ETF。\n    signals: [within-class variability, classifier-mean alignment]\n    scale: model-level (last-layer representations)\n    key_findings:\n      - 训练末期出现四种 collapse 现象\n      - 类均值收敛到 Simplex ETF 顶点\n      - Collapse 与泛化能力相关\n    vs_ours: >\n      虽然 neural collapse 与 model collapse 是不同概念，\n      但谱分析方法论可借鉴，且提供 \"collapse\" 概念的对比参考。\n\n  # ===================== COMPLEMENTARY (Theory/Mitigation) =====================\n\n  - id: shumailov_nature2024\n    title: \"AI Models Collapse When Trained on Recursively Generated Data\"\n    authors: [Ilia Shumailov et al.]\n    year: 2024\n    venue: Nature 631, 755-759\n    relation: foundation\n    core_method: >\n      首次系统性证明迭代合成数据训练导致 model collapse。\n      在 LLM、VAE、GMM 上验证。分布尾部消失是核心机制。\n    signals: [test loss, distribution tail metrics]\n    scale: model-level\n    key_findings:\n      - 迭代训练导致不可逆缺陷：分布尾部消失\n      - 罕见事件最先遗忘\n      - LLM、VAE、GMM 都有此现象\n    vs_ours: >\n      领域基石论文，建立了我们要解决的问题。\n      他们用事后评估（test loss），我们提供在线监控手段。\n\n  - id: dohmatob_iclr2025\n    title: \"Strong Model Collapse\"\n    authors: [Elvis Dohmatob, Yunzhen Feng et al.]\n    year: 2025\n    venue: ICLR 2025 (Spotlight)\n    relation: complementary\n    core_method: >\n      用算子值自由概率论证明即使极小比例的合成数据 (1/1000)\n      也会导致 model collapse，且更大模型放大 collapse。\n    signals: [test error on real data, bias-variance decomposition]\n    scale: model-level\n    key_findings:\n      - 任何非零常数比例的合成数据都导致 collapse\n      - 更大模型可放大 collapse\n      - 神经缩放定律在合成数据下失效\n    vs_ours: >\n      理论基础——解释了为什么需要监控（即使少量合成数据也危险）。\n      他们的 fraction 实验与我们的实验设计直接相关。\n\n  - id: gerstgrasser_2024\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: [Matthias Gerstgrasser, Rylan Schaeffer et al.]\n    year: 2024\n    venue: arXiv (2404.01413)\n    relation: complementary\n    core_method: >\n      证明数据累积（而非替换）可避免 model collapse。\n      替换导致 test error 增长，累积则有有限上界。\n    signals: [test error over iterations]\n    scale: model-level\n    key_findings:\n      - 累积真实+合成数据则无 collapse（所有模型/模态）\n      - 替换数据则 collapse\n      - 关键因素是数据管理策略\n    vs_ours: >\n      互补——他们研究何时 collapse（数据管理策略），\n      我们研究如何实时检测 collapse（训练动态信号）。\n\n  - id: kazdan_2024\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: [Joshua Kazdan et al.]\n    year: 2024\n    venue: arXiv (2410.16713)\n    relation: complementary\n    core_method: >\n      系统比较三种训练工作流：replace（collapse）、\n      accumulate（稳定）、fixed compute（介于两者之间）。\n    signals: [test loss on real data]\n    scale: model-level\n    key_findings:\n      - Replace 工作流一定 collapse\n      - Accumulate 工作流保持稳定\n      - Fixed compute 工作流 loss 升高但 plateau\n    vs_ours: 互补——提供实验设计参考（不同工作流下 collapse 行为差异）。\n\n  - id: seddik_2024\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: [Mohamed El Amine Seddik et al.]\n    year: 2024\n    venue: arXiv (2404.05090)\n    relation: complementary\n    core_method: >\n      统计模型严格刻画不同递归训练场景下的 collapse 程度。\n      给出混合真实/合成数据时避免 collapse 的最大合成数据比例估计。\n    signals: [distribution tail, statistical divergence]\n    scale: model-level\n    key_findings:\n      - 纯合成数据训练无法避免 collapse\n      - 混合训练下存在可计算的合成数据上限\n      - 分布尾部消失是 collapse 的统计特征\n    vs_ours: 理论互补——给出合成数据比例的安全阈值。\n\n  - id: schaeffer_2025\n    title: \"Position: Model Collapse Does Not Mean What You Think\"\n    authors: [Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo]\n    year: 2025\n    venue: arXiv (2503.03150)\n    relation: complementary\n    core_method: >\n      梳理 model collapse 文献中 8 种不同定义，\n      分为三个家族：test loss 行为、分布形变、缩放行为。\n    signals: N/A (position paper)\n    scale: N/A\n    key_findings:\n      - Model collapse 有 8 种不完全一致的定义\n      - 三个家族：test loss 行为、分布形变、缩放定律\n      - 术语混乱阻碍了系统性理解\n    vs_ours: >\n      重要定位参考——论文中需明确使用哪种 collapse 定义。\n      建议采用他们的分类框架。\n\n  - id: feng_iclr2025\n    title: \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\"\n    authors: [Feng et al.]\n    year: 2025\n    venue: ICLR 2025\n    relation: complementary\n    core_method: >\n      用高斯混合+线性分类器+线性验证器推导验证器有效的条件。\n      证明不完美验证器也可有效筛选合成数据。\n    signals: [verifier-based quality score]\n    scale: model-level\n    key_findings:\n      - 验证器筛选合成数据可达到最优性能\n      - 即使不完美验证器也有效\n      - 给出可衡量的代理条件\n    vs_ours: 互补——缓解策略。我们的监控信号可作为验证器的补充。\n\n  - id: yi_2025\n    title: \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\"\n    authors: [Bingji Yi, Qiyuan Liu, Yuwei Cheng, Haifeng Xu]\n    year: 2025\n    venue: arXiv (2510.16657)\n    relation: complementary\n    core_method: >\n      证明外部验证器（人类或更强模型）可阻止 collapse。\n      分析验证器引导下的短期改进和长期收敛行为。\n    signals: [verifier quality score]\n    scale: model-level\n    key_findings:\n      - 外部验证器注入信息则不会 collapse\n      - 短期有改进，长期收敛到验证器的知识中心\n    vs_ours: 互补——缓解策略方向，与监控方向正交。\n\n  - id: bakshi_2026\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: [Soham Bakshi et al.]\n    year: 2026\n    venue: arXiv (2602.10531)\n    relation: complementary\n    core_method: >\n      分析在真实+合成混合数据上的迭代训练动态。\n      next-token prediction 模型下的长期演化分析。\n    signals: [mixture weight, sample size, test performance]\n    scale: model-level\n    key_findings:\n      - 非零真实数据混合权重（即使递减）可避免 collapse\n      - 混合权重和样本量共同控制长期性能\n    vs_ours: 理论互补——刻画迭代训练的长期演化。\n\n  - id: dohmatob_icml2024\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: [Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, Julia Kempe]\n    year: 2024\n    venue: ICML 2024 (pp. 11165-11197)\n    relation: complementary\n    core_method: >\n      从 scaling law 视角分析 collapse——理论框架揭示 collapse 导致 scaling law 改变。\n    signals: [test loss scaling, skill metrics]\n    scale: model-level\n    key_findings:\n      - Loss of scaling、shifted scaling with number of generations\n      - Skill un-learning 现象\n      - 混合人类/合成数据时的 grokking 效应\n    vs_ours: >\n      理论背景——从 scaling law 角度量化 collapse 严重度。\n      我们用训练动态信号在训练中追踪，他们用事后 scaling 分析。\n\n  - id: fu_icml2024\n    title: \"Towards Theoretical Understandings of Self-Consuming Generative Models\"\n    authors: [Shi Fu, Sen Zhang, Yingjie Wang, Xinmei Tian, Dacheng Tao]\n    year: 2024\n    venue: ICML 2024\n    relation: complementary\n    core_method: >\n      构建严格理论框架分析 self-consuming loop 中数据分布演化。\n      分析参数和非参数模型中三种误差源的复合效应。\n    signals: [distribution divergence, error accumulation]\n    scale: model-level\n    key_findings:\n      - 统计/表达/近似三种误差在迭代中复合\n      - 给出误差增长的理论界\n    vs_ours: 理论互补——严格刻画 collapse 的误差复合机制。\n\n  - id: gillman_icml2024\n    title: \"Self-Correcting Self-Consuming Loops for Generative Model Training\"\n    authors: [Nate Gillman, Michael Freeman, Daksh Aggarwal, Chia-Hong Hsu, Calvin Luo, Yonglong Tian, Chen Sun]\n    year: 2024\n    venue: ICML 2024\n    relation: complementary\n    core_method: >\n      引入 correction function 使 self-consuming loop 指数级更稳定。\n      在人体运动合成任务上验证。\n    signals: [corrector quality, loop stability]\n    scale: model-level\n    key_findings:\n      - Correction function 使 loop 指数级稳定\n      - 即使 synthetic:real = 100:1 也可避免 collapse\n    vs_ours: 互补——缓解策略，correction function 概念与在线监控互补。\n\n  # ===================== DATA CONTAMINATION DETECTION =====================\n\n  - id: kirchenbauer_icml2023\n    title: \"A Watermark for Large Language Models\"\n    authors: [John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, Tom Goldstein]\n    year: 2023\n    venue: ICML 2023 (pp. 17061-17084)\n    relation: complementary\n    core_method: >\n      LLM 文本水印框架——green/red token list + soft promotion + 统计检测。\n    signals: [green token ratio, z-score]\n    scale: token-level (output)\n    key_findings:\n      - 可嵌入统计可检测水印且不影响文本质量\n      - 开源检测算法不需模型访问\n    vs_ours: 合成数据溯源的基础方法，与 collapse 检测互补。\n\n  - id: dathathri_nature2024\n    title: \"Scalable Watermarking for Identifying Large Language Model Outputs\"\n    authors: [Sumanth Dathathri, Abigail See, Sumedh Ghaisas et al.]\n    year: 2024\n    venue: Nature 634, 818-823\n    relation: complementary\n    core_method: >\n      SynthID-Text：产品级文本水印，与 speculative sampling 集成。\n      在 Gemini ~20M 响应上验证。\n    signals: [watermark detection score]\n    scale: token-level (output)\n    key_findings:\n      - 产品级规模的水印部署\n      - 不影响文本质量，最小延迟开销\n    vs_ours: 大规模合成数据标记的工业实践，与监控方向互补。\n\n  - id: sander_neurips2024\n    title: \"Watermarking Makes Language Models Radioactive\"\n    authors: [Tom Sander, Pierre Fernandez, Alain Durmus, Matthijs Douze, Teddy Furon]\n    year: 2024\n    venue: NeurIPS 2024\n    relation: related\n    core_method: >\n      证明在水印 LLM 输出上微调的模型保留水印残留（\"放射性\"）。\n    signals: [watermark residual in fine-tuned model]\n    scale: model-level\n    key_findings:\n      - 水印信号通过训练传播到下游模型\n      - 可检测模型是否在合成数据上训练\n    vs_ours: >\n      直接相关——检测合成数据训练的替代方法。\n      他们检测\"是否用了合成数据\"，我们监控\"合成数据造成多严重的 collapse\"。\n\n  - id: mitchell_icml2023\n    title: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\n    authors: [Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn]\n    year: 2023\n    venue: ICML 2023 (pp. 24950-24962)\n    relation: complementary\n    core_method: >\n      LLM 生成文本占据 log-probability 负曲率区域，据此零样本检测。\n    signals: [log probability curvature]\n    scale: text-level\n    key_findings:\n      - 生成文本的概率曲率特征可区分人类/机器文本\n      - 0.95 AUROC 检测 GPT-NeoX 20B 生成的假新闻\n    vs_ours: 合成文本检测方法，可识别训练数据中的合成成分。\n\n  - id: shi_iclr2024\n    title: \"Detecting Pretraining Data from Large Language Models\"\n    authors: [Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer]\n    year: 2024\n    venue: ICLR 2024\n    relation: related\n    core_method: >\n      Min-K% Prob：未见样本含低概率 outlier word，据此检测预训练数据成员。\n    signals: [Min-K% probability score]\n    scale: text-level\n    key_findings:\n      - 比 reference model 方法提升 7.4%\n      - 适用于版权检测、污染检测、隐私审计\n    vs_ours: 数据污染检测工具——可检测合成数据是否混入训练集，与 collapse 监控互补。\n\n  # ===================== METHODOLOGICAL FOUNDATIONS =====================\n\n  - id: martin_mahoney_2021\n    title: \"Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data\"\n    authors: [Charles H. Martin, Michael W. Mahoney]\n    year: 2021\n    venue: Nature Communications 12\n    relation: complementary\n    core_method: >\n      WeightWatcher 工具——用 RMT 分析权重矩阵的谱性质，\n      无需训练/测试数据即可预测模型质量。\n    signals: [stable rank, power law exponent (alpha), spectral norm]\n    scale: layer-level (per weight matrix)\n    key_findings:\n      - stable rank 追踪自正则化程度\n      - 5+1 训练阶段对应不同的谱形态\n      - heavy-tailed 分布特征区分好/差模型\n    vs_ours: >\n      方法论基础——WeightWatcher 的 stable rank 和谱分析方法\n      直接启发我们的信号设计。\n\n  - id: yunis_2024\n    title: \"Approaching Deep Learning through the Spectral Dynamics of Weights\"\n    authors: [David Yunis, Kumar Kshitij Patel et al.]\n    year: 2024\n    venue: arXiv (2408.11804)\n    relation: complementary\n    core_method: >\n      以权重奇异值/向量的动态演化为核心视角理解深度学习。\n      证明谱动态可区分记忆网络和泛化网络。\n    signals: [singular value dynamics, singular vector alignment]\n    scale: layer-level (per weight matrix)\n    key_findings:\n      - 权重衰减增强低秩偏置\n      - 谱动态区分记忆 vs 泛化\n      - 与 lottery ticket 和 loss surface 结构相关\n    vs_ours: 方法论基础——谱动态视角可用于理解 collapse 过程中的权重变化。\n\n  - id: chen_liu_2024\n    title: \"Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy\"\n    authors: [Chen Liu et al.]\n    year: 2024\n    venue: IEEE CISS 2024\n    relation: complementary\n    core_method: >\n      提出 Diffusion Spectral Entropy (DSE) 和 Diffusion Spectral Mutual Information (DSMI)，\n      利用数据几何在高维中可靠计算信息论指标。\n    signals: [DSE, DSMI]\n    scale: layer-level (representations)\n    key_findings:\n      - DSE 在训练中增加\n      - DSMI(class label) 在泛化学习中增加，过拟合时停滞\n      - 可用于指导网络初始化和预测下游准确率\n    vs_ours: >\n      方法论工具——DSE 是我们 spectral entropy 信号的潜在替代实现。\n\n  - id: lu_neurips2024\n    title: \"AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models\"\n    authors: [Haiquan Lu, Yefan Zhou, Shiwei Liu, Zhangyang Wang, Michael W. Mahoney, Yaoqing Yang]\n    year: 2024\n    venue: NeurIPS 2024\n    relation: complementary\n    core_method: >\n      用 HT-SR 理论的谱密度形态（alpha exponent）指导 LLM 层级剪枝。\n    signals: [alpha exponent, ESD shape metrics]\n    scale: layer-level\n    key_findings:\n      - Alpha exponent 有效指导 per-layer 剪枝比例\n      - LLaMA-7B 可剪至 80% sparsity 保持合理 perplexity\n    vs_ours: >\n      验证 per-layer 谱分析对 LLM 质量评估的有效性。\n      支持我们用类似方法监控 collapse。\n\n  - id: sanyal_iclr2020\n    title: \"Stable Rank Normalization for Improved Generalization in Neural Networks and GANs\"\n    authors: [Amartya Sanyal, Philip H. S. Torr, Puneet K. Dokania]\n    year: 2020\n    venue: ICLR 2020\n    relation: complementary\n    core_method: >\n      提出 stable rank normalization——最小化线性算子的 stable rank。\n      理论证明唯一最优解，实验验证改善泛化。\n    signals: [stable rank, Lipschitz constant]\n    scale: layer-level\n    key_findings:\n      - 控制 stable rank 改善泛化 gap 11.3%\n      - Stable rank 与泛化能力直接关联\n    vs_ours: >\n      理论支持——建立 stable rank 与泛化的直接联系。\n      支持我们选用 stable rank 作为 collapse（泛化退化）的监控信号。\n\n  - id: kalra_2026\n    title: \"A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs\"\n    authors: [Dayal Singh Kalra, Jean-Christophe Gagnon-Audet, Andrey Gromov, Ishita Mediratta, Kelvin Niu, Alexander H. Miller, Michael Shvartsman]\n    year: 2026\n    venue: arXiv (2601.16979)\n    relation: related\n    core_method: >\n      Critical sharpness：<10 forward passes 高效度量 loss landscape 曲率。\n      首次在 7B 规模验证 progressive sharpening 和 Edge of Stability。\n    signals: [critical sharpness, relative critical sharpness]\n    scale: model-level\n    key_findings:\n      - Progressive sharpening 在 7B 规模仍然存在\n      - Critical sharpness 可指导 pre-train 到 fine-tune 的数据混合\n    vs_ours: >\n      训练动态监控方法论参考——高效的大规模 LLM 训练动态度量。\n      Critical sharpness 可作为我们信号集的潜在补充。\n\n  # ===================== DATA QUALITY =====================\n\n  - id: penedo_2024\n    title: \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\"\n    authors: [Guilherme Penedo, Hynek Kydlicek, Loubna Ben allal, Anton Lozhkov, Margaret Mitchell, Colin Raffel, Leandro Von Werra, Thomas Wolf]\n    year: 2024\n    venue: arXiv (2406.17557)\n    relation: complementary\n    core_method: >\n      15T token 数据集的完整策略文档——去重、过滤、教育文本提取。\n    signals: [data quality classifiers, deduplication metrics]\n    scale: dataset-level\n    key_findings:\n      - 详细 ablation 各种去重和过滤策略\n      - FineWeb-Edu 在知识密集任务上大幅提升性能\n    vs_ours: 数据质量策略参考——理解高质量训练数据标准，为分析 collapse 的数据原因提供基线。\n\n  - id: zhang_2026\n    title: \"The LLM Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data\"\n    authors: [Kaituo Zhang, Mingzhi Hu, Hoang Anh Duy Le et al.]\n    year: 2026\n    venue: arXiv (2601.17717)\n    relation: complementary\n    core_method: >\n      系统分类合成数据评估指标——quality (validity/fidelity/utility) +\n      trustworthiness (safety/faithfulness)。\n    signals: [quality metrics taxonomy, trustworthiness metrics]\n    scale: dataset-level\n    key_findings:\n      - 从内在属性评估合成数据，而非仅看下游性能\n      - 质量和可信度两个维度的完整分类体系\n    vs_ours: 合成数据质量评估框架——为理解 collapse 的数据级原因提供指标体系。\n\n# ============================================================\n# 关键发现总结\n# ============================================================\n\nsummary:\n  total_papers: 34\n  direct_competitors: 2  # SIGMA, Kalinowski\n  novelty_confirmation: >\n    在 34 篇文献中，没有工作同时做到：(a) 训练中在线监控 (b) 用频谱/熵训练动态信号\n    (c) per-layer 粒度 (d) 在迭代合成数据训练场景下验证。\n    我们的核心新颖性空间依然存在。\n\n  coverage:\n    model_collapse_theory: 14  # shumailov, dohmatob x2, alemohammad, fu, gerstgrasser, seddik, kazdan, schaeffer, bakshi, shi_neurips2025, feng, yi, gillman\n    data_contamination: 5  # kirchenbauer, dathathri, sander, mitchell, shi_iclr2024\n    spectral_methods: 8  # sigma, martin_mahoney, yunis, lu, sanyal, spectral_lens, xu, conzelmann\n    training_dynamics: 4  # kalinowski, chen_liu, kalra, papyan\n    data_quality: 3  # wyss, penedo, zhang\n\n  gap_analysis:\n    sigma: >\n      用输出嵌入 Gram 矩阵谱——事后/黑盒，不做 per-layer，不跟踪训练过程。\n    kalinowski: >\n      用拓扑信号——在线但信号族不同，不研究迭代合成数据场景。\n    our_unique_position: >\n      训练动态频谱/熵信号 + per-layer 粒度 + 迭代合成数据场景 = 独特定位。\n\n  per_layer_collapse_analysis:\n    papers_with_per_layer:\n      - layer_collapse_diffusion_2026  # diffusion LM per-layer activation collapse\n      - xu_2026  # stable rank per-layer（compression 场景）\n      - spectral_lens_2026  # per-layer activation/gradient 谱\n      - lu_neurips2024  # alpha exponent per-layer for pruning\n    gap: \"无论文在迭代合成数据训练中做 per-layer collapse 分析\"\n\n  stable_rank_as_collapse_signal:\n    papers_using_stable_rank:\n      - martin_mahoney_2021  # WeightWatcher 中作为模型质量指标\n      - xu_2026  # 压缩退化预测器 (r=0.89)\n      - yunis_2024  # 谱动态中的低秩偏置\n      - sanyal_iclr2020  # stable rank 与泛化的直接联系\n    gap: \"无论文直接用 stable rank 监控 iterative synthetic data collapse\"\n\n  spectral_entropy_as_collapse_signal:\n    papers_using_spectral_entropy:\n      - chen_liu_2024  # DSE 跟踪训练动态\n      - sigma_2026  # 谱分析但在 Gram 矩阵上\n    gap: \"无论文直接用 weight spectral entropy 监控 collapse\"\n\n  synthetic_fraction_effects:\n    papers_studying_fraction:\n      - dohmatob_iclr2025  # 理论：任何非零 fraction 都危险\n      - dohmatob_icml2024  # scaling law 角度的 fraction 分析\n      - alemohammad_iclr2024  # 三种 loop 类型的不同效果\n      - wyss_2024  # 实证：25%/50%/75% 不同 collapse 程度\n      - seddik_2024  # 统计：给出安全上限估计\n    gap: \"大量理论/实证工作，但都用事后指标衡量 fraction 效果\"\n\n  data_contamination_detection:\n    papers:\n      - kirchenbauer_icml2023  # 基础水印方法\n      - dathathri_nature2024  # 产品级水印 (SynthID)\n      - sander_neurips2024  # 水印放射性传播\n      - mitchell_icml2023  # DetectGPT 概率曲率检测\n      - shi_iclr2024  # Min-K% 预训练数据检测\n    relevance: >\n      合成数据检测与 collapse 监控互补：他们回答\"是否有合成数据\"，\n      我们回答\"合成数据造成了多严重的 collapse\"。\n",
      "numLines": 709,
      "startLine": 1,
      "totalLines": 709
    }
  },
  "sourceToolAssistantUUID": "58a6484d-ee17-4d5d-a802-8bad846e730d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T22:42:07.924Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SDjeHburHBkzfU1CbKQ74c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e800f1c9-60b2-42eb-8635-815ace8fdf49",
  "isSidechain": false,
  "requestId": "req_011Cb3GWBP8qSjoabQ1rozXo",
  "type": "assistant",
  "uuid": "6b385fc9-27e7-4b3e-984d-d9a8f61c0ddd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5tctSX7vDf1AdBwGUC2Hr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 22763,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 367,
          "cache_read_input_tokens": 22763,
          "cache_creation_input_tokens": 240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 240
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

_source line 14 · 2026-05-14T22:42:09.509Z_

<details><summary>↩ Tool result · `toolu_017CRiPnTNntFzQ4ChZKPEdP`</summary>

```text
1	# Annotated Bibliography — collapse_severity_monitor
2	
3	**Last updated:** 2026-05-14  
4	**Total papers:** 33  
5	**Research focus:** Training dynamic signals (spectral/output/downstream) as online monitors of model collapse severity in iterative synthetic data training.
6	
7	---
8	
9	## 1. Model Collapse Theory (14 papers)
10	
11	### Foundation & Mechanism
12	
13	| Key | Paper | Role |
14	|-----|-------|------|
15	| `shumailov2024curse` | Shumailov et al. "AI Models Collapse When Trained on Recursively Generated Data" (Nature 2024) | **foundation** |
16	
17	首次系统性证明迭代合成数据训练导致 model collapse——分布尾部不可逆消失。在 LLM、VAE、GMM 上验证。**领域基石论文，定义了我们要解决的问题。**
18	
19	| Key | Paper | Role |
20	|-----|-------|------|
21	| `alemohammad2024mad` | Alemohammad et al. "Self-Consuming Generative Models Go MAD" (ICLR 2024) | **foundation** |
22	
23	定义三种 autophagous loop（fully synthetic / synthetic augmentation / fresh data）并证明无足够真实数据时 precision 或 recall 必然下降（MAD 现象）。**提供了我们实验设计中不同 synthetic fraction 设置的理论基础。**
24	
25	| Key | Paper | Role |
26	|-----|-------|------|
27	| `dohmatob2025strong` | Dohmatob et al. "Strong Model Collapse" (ICLR 2025 Spotlight) | **background** |
28	
29	用算子值自由概率论证明即使极小比例合成数据 (1/1000) 也导致 collapse，且更大模型放大 collapse。**理论依据——解释了为什么需要监控（即使少量合成数据也危险）。**
30	
31	| Key | Paper | Role |
32	|-----|-------|------|
33	| `dohmatob2024tails` | Dohmatob et al. "A Tale of Tails: Model Collapse as a Change of Scaling Laws" (ICML 2024) | **background** |
34	
35	从 scaling law 视角分析 collapse——发现 loss of scaling、shifted scaling、skill un-learning 等衰退现象。**为理解 collapse 的定量行为提供 scaling law 框架。**
36	
37	### Theoretical Frameworks
38	
39	| Key | Paper | Role |
40	|-----|-------|------|
41	| `fu2024selfconsuming` | Fu et al. "Towards Theoretical Understandings of Self-Consuming Generative Models" (ICML 2024) | **background** |
42	
43	构建严格理论框架分析 self-consuming loop 中数据分布的演化，包括参数和非参数模型。**三种误差源（统计/表达/近似）在迭代中的复合效应分析。**
44	
45	| Key | Paper | Role |
46	|-----|-------|------|
47	| `seddik2024bad` | Seddik et al. "How Bad is Training on Synthetic Data?" (arXiv 2024) | **background** |
48	
49	统计模型刻画不同递归训练场景的 collapse 程度，给出混合训练时合成数据安全上限估计。**为我们的 synthetic fraction 实验提供理论预期。**
50	
51	| Key | Paper | Role |
52	|-----|-------|------|
53	| `bakshi2026improvement` | Bakshi et al. "From Collapse to Improvement" (arXiv 2026) | **background** |
54	
55	分析真实+合成混合数据上 next-token prediction 模型的长期演化——非零真实数据权重可避免 collapse。**刻画迭代训练的长期演化理论。**
56	
57	### Empirical Studies & Taxonomies
58	
59	| Key | Paper | Role |
60	|-----|-------|------|
61	| `gerstgrasser2024inevitable` | Gerstgrasser et al. "Is Model Collapse Inevitable?" (arXiv 2024) | **complementary** |
62	
63	证明数据累积（而非替换）可避免 collapse。**互补——研究何时 collapse（数据管理策略），我们研究如何检测 collapse。**
64	
65	| Key | Paper | Role |
66	|-----|-------|------|
67	| `kazdan2024collapse` | Kazdan et al. "Collapse or Thrive?" (arXiv 2024) | **complementary** |
68	
69	系统比较 replace/accumulate/fixed-compute 三种工作流的 collapse 行为。**提供实验设计参考。**
70	
71	| Key | Paper | Role |
72	|-----|-------|------|
73	| `schaeffer2025position` | Schaeffer et al. "Position: Model Collapse Does Not Mean What You Think" (arXiv 2025) | **background** |
74	
75	梳理文献中 8 种 collapse 定义，分为 test-loss/分布形变/缩放定律三个家族。**论文定位参考——需明确使用哪种 collapse 定义。**
76	
77	| Key | Paper | Role |
78	|-----|-------|------|
79	| `shi2025closerlook` | Shi et al. "A Closer Look at Model Collapse" (NeurIPS 2025 Spotlight) | **complementary** |
80	
81	揭示 collapse 中泛化→记忆的转变，发现数据熵与泛化强线性相关。**数据级熵可作为我们训练动态信号的外部验证指标。**
82	
83	### Mitigation Strategies
84	
85	| Key | Paper | Role |
86	|-----|-------|------|
87	| `feng2025verification` | Feng et al. "Beyond Model Collapse: Verification" (ICLR 2025) | **complementary** |
88	
89	验证器筛选合成数据可达最优性能，即使不完美验证器也有效。**缓解策略——我们的监控信号可作为验证器的补充。**
90	
91	| Key | Paper | Role |
92	|-----|-------|------|
93	| `yi2025escaping` | Yi et al. "Escaping Model Collapse via Synthetic Data Verification" (arXiv 2025) | **complementary** |
94	
95	证明外部验证器注入信息则不会 collapse。**缓解策略方向，与监控方向正交。**
96	
97	| Key | Paper | Role |
98	|-----|-------|------|
99	| `gillman2024selfcorrecting` | Gillman et al. "Self-Correcting Self-Consuming Loops" (ICML 2024) | **complementary** |
100	
101	引入 correction function 使 self-consuming loop 指数级更稳定，即使 synthetic:real = 100:1 也可避免 collapse。**缓解策略，correction function 概念与我们的在线监控互补。**
102	
103	---
104	
105	## 2. Data Contamination Detection (5 papers)
106	
107	| Key | Paper | Role |
108	|-----|-------|------|
109	| `kirchenbauer2023watermark` | Kirchenbauer et al. "A Watermark for Large Language Models" (ICML 2023) | **background** |
110	
111	提出 LLM 文本水印框架——通过 green/red token list 在采样时嵌入统计水印。**合成数据溯源的基础方法，与 collapse 检测互补。**
112	
113	| Key | Paper | Role |
114	|-----|-------|------|
115	| `dathathri2024synthid` | Dathathri et al. "Scalable Watermarking for Identifying LLM Outputs" (Nature 2024) | **background** |
116	
117	SynthID-Text：产品级文本水印方案，与 speculative sampling 集成，在 Gemini 20M 响应上验证。**大规模合成数据标记的工业实践。**
118	
119	| Key | Paper | Role |
120	|-----|-------|------|
121	| `sander2024radioactive` | Sander et al. "Watermarking Makes Language Models Radioactive" (NeurIPS 2024) | **complementary** |
122	
123	证明在水印 LLM 输出上微调的模型保留水印残留（"放射性"），可检测是否使用了合成训练数据。**直接相关——检测模型是否在合成数据上训练，与我们的 collapse 监控互补。**
124	
125	| Key | Paper | Role |
126	|-----|-------|------|
127	| `mitchell2023detectgpt` | Mitchell et al. "DetectGPT" (ICML 2023) | **background** |
128	
129	LLM 生成文本占据 log-probability 负曲率区域，据此零样本检测机器文本。**合成文本检测方法，可用于识别训练数据中的合成成分。**
130	
131	| Key | Paper | Role |
132	|-----|-------|------|
133	| `shi2024detecting` | Shi et al. "Detecting Pretraining Data from LLMs" (ICLR 2024) | **complementary** |
134	
135	Min-K% Prob：未见样本含低概率 outlier word，据此检测预训练数据成员。**数据污染检测工具——可检测合成数据是否混入训练集。**
136	
137	---
138	
139	## 3. Spectral Methods in NLP/LLM (7 papers)
140	
141	| Key | Paper | Role |
142	|-----|-------|------|
143	| `azam2026sigma` | Gu et al. "SIGMA: Scalable Spectral Insights for LLM Model Collapse" (arXiv 2026) | **direct competitor** |
144	
145	通过 embedding Gram 矩阵的谱分析量化 collapse——推导确定性和随机性界。**事后/黑盒方法，不做 per-layer，不跟踪训练过程。我们用训练动态信号，更早期更细粒度。**
146	
147	| Key | Paper | Role |
148	|-----|-------|------|
149	| `martin2021weightwatcher` | Martin & Mahoney "Predicting Trends in Neural Network Quality" (Nature Communications 2021) | **method component** |
150	
151	WeightWatcher 工具——用 RMT 分析权重谱性质（stable rank, power law alpha, spectral norm）预测模型质量。**方法论基础——直接启发我们的 stable rank 和谱分析信号设计。**
152	
153	| Key | Paper | Role |
154	|-----|-------|------|
155	| `yunis2024spectral` | Yunis et al. "Approaching Deep Learning through the Spectral Dynamics of Weights" (arXiv 2024) | **method component** |
156	
157	以权重奇异值/向量动态演化为视角理解深度学习——谱动态可区分记忆 vs 泛化。**方法论基础——谱动态视角用于理解 collapse 中的权重变化。**
158	
159	| Key | Paper | Role |
160	|-----|-------|------|
161	| `lu2024alphapruning` | Lu et al. "AlphaPruning" (NeurIPS 2024) | **method component** |
162	
163	用 heavy-tailed self-regularization 理论的谱密度形态 (alpha exponent) 指导 LLM 层级剪枝。**验证了 per-layer 谱分析对 LLM 质量评估的有效性，支持我们用类似方法监控 collapse。**
164	
165	| Key | Paper | Role |
166	|-----|-------|------|
167	| `sanyal2020stablerank` | Sanyal et al. "Stable Rank Normalization" (ICLR 2020) | **method component** |
168	
169	提出 stable rank normalization 方法，证明控制 stable rank 可改善泛化（11.3% generalization gap 改善）。**理论支持——stable rank 与泛化能力的直接联系。**
170	
171	| Key | Paper | Role |
172	|-----|-------|------|
173	| `liu2026spectrallens` | Liu et al. "Spectral Lens" (arXiv 2026) | **complementary** |
174	
175	用 activation covariance 和 per-sample gradient 的 SVD 谱诊断 LLM 训练优化。**方法论高度相关——同样用频谱分析训练动态，但不研究 collapse。**
176	
177	| Key | Paper | Role |
178	|-----|-------|------|
179	| `xu2026compression` | Xu "Predicting LLM Compression Degradation from Spectral Statistics" (arXiv 2026) | **complementary** |
180	
181	stable rank 是压缩退化的主要预测因子 (r=0.890)，per-layer 分析优于全局。**直接验证 stable rank 作为退化预测信号的有效性。**
182	
183	---
184	
185	## 4. Training Dynamics Monitoring (4 papers)
186	
187	| Key | Paper | Role |
188	|-----|-------|------|
189	| `kalinowski2026monitoring` | Kalinowski "Monitoring Neural Training with Topology" (arXiv 2026) | **direct competitor** |
190	
191	在线拓扑监控器——persistent homology + Collapse Index 提供低延迟早期预警。**在线监控但信号族不同（拓扑 vs 频谱/熵），不研究迭代合成数据场景。**
192	
193	| Key | Paper | Role |
194	|-----|-------|------|
195	| `chen2024dse` | Liu et al. "Diffusion Spectral Entropy for Neural Network Representations" (IEEE CISS 2024) | **method component** |
196	
197	提出 DSE 和 DSMI——利用数据几何在高维中计算信息论指标，DSE 在训练中增加。**我们 spectral entropy 信号的潜在替代实现。**
198	
199	| Key | Paper | Role |
200	|-----|-------|------|
201	| `kalra2026curvature` | Kalra et al. "Scalable Loss Landscape Curvature for LLM Training Dynamics" (arXiv 2026) | **complementary** |
202	
203	Critical sharpness：<10 forward passes 捕获 Hessian sharpness，首次在 7B 规模验证 progressive sharpening/Edge of Stability。**训练动态监控方法论参考——高效的大规模 LLM 训练动态度量。**
204	
205	| Key | Paper | Role |
206	|-----|-------|------|
207	| `conzelmann2026layercollapse` | Conzelmann et al. "Layer Collapse in Diffusion Language Models" (arXiv 2026) | **complementary** |
208	
209	分析 diffusion LM 中 per-layer activation collapse——少数层的 channel-axis collapse 对整体生成至关重要。**per-layer collapse 分析方法论参考。**
210	
211	---
212	
213	## 5. Data Quality & Model Degradation (3 papers)
214	
215	| Key | Paper | Role |
216	|-----|-------|------|
217	| `wyss2024surprise` | Wyss et al. "Learning by Surprise: Surplexity" (arXiv 2024) | **complementary** |
218	
219	用语义网络和 next-token 概率量化 LLM collapse 中的多样性损失。**输出级 collapse 量化方法——合成比例实验设计与我们重叠。**
220	
221	| Key | Paper | Role |
222	|-----|-------|------|
223	| `penedo2024fineweb` | Penedo et al. "The FineWeb Datasets" (arXiv 2024) | **background** |
224	
225	15T token 数据集，详细文档化去重、过滤等数据策略。**数据质量策略参考——理解高质量训练数据的标准。**
226	
227	| Key | Paper | Role |
228	|-----|-------|------|
229	| `zhang2026auditor` | Zhang et al. "The LLM Data Auditor" (arXiv 2026) | **background** |
230	
231	系统分类合成数据评估指标——quality (validity/fidelity/utility) + trustworthiness (safety/faithfulness)。**合成数据质量评估框架，为理解 collapse 的数据级原因提供指标体系。**
232	
233	---
234	
235	## 6. Foundational (1 paper)
236	
237	| Key | Paper | Role |
238	|-----|-------|------|
239	| `papyan2020neuralcollapse` | Papyan et al. "Prevalence of Neural Collapse" (PNAS 2020) | **foundation** |
240	
241	发现分类网络训练末期的 Neural Collapse 现象——类内表征收缩到 Simplex ETF。**虽然与 model collapse 不同，但提供了"collapse"概念的对比参考，且其谱分析方法论可借鉴。**
242	
243	---
244	
245	## Summary Statistics
246	
247	| Category | Count | Direct Competitors | Background | Method Component | Complementary |
248	|----------|-------|-------------------|------------|-----------------|---------------|
249	| Model Collapse Theory | 14 | 0 | 7 | 0 | 5 |
250	| Data Contamination | 5 | 0 | 3 | 0 | 2 |
251	| Spectral Methods | 7 | 1 | 0 | 4 | 2 |
252	| Training Dynamics | 4 | 1 | 0 | 1 | 2 |
253	| Data Quality | 3 | 0 | 2 | 0 | 1 |
254	| Foundational | 1 | 0 | 0 | 0 | 0 |
255	| **Total** | **33** | **2** | **12** | **5** | **12** |
256	
257	Foundation papers: 2 (shumailov2024curse, papyan2020neuralcollapse)
258	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d32e62b-0c70-4fa1-823d-829af339ad12",
  "isSidechain": false,
  "promptId": "985e4d4c-de63-470a-9f8d-580809be0b1f",
  "type": "user",
  "uuid": "80214af7-5275-48da-843c-245e7129bacf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/annotated_bibliography.md",
      "content": "# Annotated Bibliography — collapse_severity_monitor\n\n**Last updated:** 2026-05-14  \n**Total papers:** 33  \n**Research focus:** Training dynamic signals (spectral/output/downstream) as online monitors of model collapse severity in iterative synthetic data training.\n\n---\n\n## 1. Model Collapse Theory (14 papers)\n\n### Foundation & Mechanism\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `shumailov2024curse` | Shumailov et al. \"AI Models Collapse When Trained on Recursively Generated Data\" (Nature 2024) | **foundation** |\n\n首次系统性证明迭代合成数据训练导致 model collapse——分布尾部不可逆消失。在 LLM、VAE、GMM 上验证。**领域基石论文，定义了我们要解决的问题。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `alemohammad2024mad` | Alemohammad et al. \"Self-Consuming Generative Models Go MAD\" (ICLR 2024) | **foundation** |\n\n定义三种 autophagous loop（fully synthetic / synthetic augmentation / fresh data）并证明无足够真实数据时 precision 或 recall 必然下降（MAD 现象）。**提供了我们实验设计中不同 synthetic fraction 设置的理论基础。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `dohmatob2025strong` | Dohmatob et al. \"Strong Model Collapse\" (ICLR 2025 Spotlight) | **background** |\n\n用算子值自由概率论证明即使极小比例合成数据 (1/1000) 也导致 collapse，且更大模型放大 collapse。**理论依据——解释了为什么需要监控（即使少量合成数据也危险）。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `dohmatob2024tails` | Dohmatob et al. \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\" (ICML 2024) | **background** |\n\n从 scaling law 视角分析 collapse——发现 loss of scaling、shifted scaling、skill un-learning 等衰退现象。**为理解 collapse 的定量行为提供 scaling law 框架。**\n\n### Theoretical Frameworks\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `fu2024selfconsuming` | Fu et al. \"Towards Theoretical Understandings of Self-Consuming Generative Models\" (ICML 2024) | **background** |\n\n构建严格理论框架分析 self-consuming loop 中数据分布的演化，包括参数和非参数模型。**三种误差源（统计/表达/近似）在迭代中的复合效应分析。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `seddik2024bad` | Seddik et al. \"How Bad is Training on Synthetic Data?\" (arXiv 2024) | **background** |\n\n统计模型刻画不同递归训练场景的 collapse 程度，给出混合训练时合成数据安全上限估计。**为我们的 synthetic fraction 实验提供理论预期。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `bakshi2026improvement` | Bakshi et al. \"From Collapse to Improvement\" (arXiv 2026) | **background** |\n\n分析真实+合成混合数据上 next-token prediction 模型的长期演化——非零真实数据权重可避免 collapse。**刻画迭代训练的长期演化理论。**\n\n### Empirical Studies & Taxonomies\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `gerstgrasser2024inevitable` | Gerstgrasser et al. \"Is Model Collapse Inevitable?\" (arXiv 2024) | **complementary** |\n\n证明数据累积（而非替换）可避免 collapse。**互补——研究何时 collapse（数据管理策略），我们研究如何检测 collapse。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `kazdan2024collapse` | Kazdan et al. \"Collapse or Thrive?\" (arXiv 2024) | **complementary** |\n\n系统比较 replace/accumulate/fixed-compute 三种工作流的 collapse 行为。**提供实验设计参考。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `schaeffer2025position` | Schaeffer et al. \"Position: Model Collapse Does Not Mean What You Think\" (arXiv 2025) | **background** |\n\n梳理文献中 8 种 collapse 定义，分为 test-loss/分布形变/缩放定律三个家族。**论文定位参考——需明确使用哪种 collapse 定义。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `shi2025closerlook` | Shi et al. \"A Closer Look at Model Collapse\" (NeurIPS 2025 Spotlight) | **complementary** |\n\n揭示 collapse 中泛化→记忆的转变，发现数据熵与泛化强线性相关。**数据级熵可作为我们训练动态信号的外部验证指标。**\n\n### Mitigation Strategies\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `feng2025verification` | Feng et al. \"Beyond Model Collapse: Verification\" (ICLR 2025) | **complementary** |\n\n验证器筛选合成数据可达最优性能，即使不完美验证器也有效。**缓解策略——我们的监控信号可作为验证器的补充。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `yi2025escaping` | Yi et al. \"Escaping Model Collapse via Synthetic Data Verification\" (arXiv 2025) | **complementary** |\n\n证明外部验证器注入信息则不会 collapse。**缓解策略方向，与监控方向正交。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `gillman2024selfcorrecting` | Gillman et al. \"Self-Correcting Self-Consuming Loops\" (ICML 2024) | **complementary** |\n\n引入 correction function 使 self-consuming loop 指数级更稳定，即使 synthetic:real = 100:1 也可避免 collapse。**缓解策略，correction function 概念与我们的在线监控互补。**\n\n---\n\n## 2. Data Contamination Detection (5 papers)\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `kirchenbauer2023watermark` | Kirchenbauer et al. \"A Watermark for Large Language Models\" (ICML 2023) | **background** |\n\n提出 LLM 文本水印框架——通过 green/red token list 在采样时嵌入统计水印。**合成数据溯源的基础方法，与 collapse 检测互补。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `dathathri2024synthid` | Dathathri et al. \"Scalable Watermarking for Identifying LLM Outputs\" (Nature 2024) | **background** |\n\nSynthID-Text：产品级文本水印方案，与 speculative sampling 集成，在 Gemini 20M 响应上验证。**大规模合成数据标记的工业实践。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `sander2024radioactive` | Sander et al. \"Watermarking Makes Language Models Radioactive\" (NeurIPS 2024) | **complementary** |\n\n证明在水印 LLM 输出上微调的模型保留水印残留（\"放射性\"），可检测是否使用了合成训练数据。**直接相关——检测模型是否在合成数据上训练，与我们的 collapse 监控互补。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `mitchell2023detectgpt` | Mitchell et al. \"DetectGPT\" (ICML 2023) | **background** |\n\nLLM 生成文本占据 log-probability 负曲率区域，据此零样本检测机器文本。**合成文本检测方法，可用于识别训练数据中的合成成分。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `shi2024detecting` | Shi et al. \"Detecting Pretraining Data from LLMs\" (ICLR 2024) | **complementary** |\n\nMin-K% Prob：未见样本含低概率 outlier word，据此检测预训练数据成员。**数据污染检测工具——可检测合成数据是否混入训练集。**\n\n---\n\n## 3. Spectral Methods in NLP/LLM (7 papers)\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `azam2026sigma` | Gu et al. \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\" (arXiv 2026) | **direct competitor** |\n\n通过 embedding Gram 矩阵的谱分析量化 collapse——推导确定性和随机性界。**事后/黑盒方法，不做 per-layer，不跟踪训练过程。我们用训练动态信号，更早期更细粒度。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `martin2021weightwatcher` | Martin & Mahoney \"Predicting Trends in Neural Network Quality\" (Nature Communications 2021) | **method component** |\n\nWeightWatcher 工具——用 RMT 分析权重谱性质（stable rank, power law alpha, spectral norm）预测模型质量。**方法论基础——直接启发我们的 stable rank 和谱分析信号设计。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `yunis2024spectral` | Yunis et al. \"Approaching Deep Learning through the Spectral Dynamics of Weights\" (arXiv 2024) | **method component** |\n\n以权重奇异值/向量动态演化为视角理解深度学习——谱动态可区分记忆 vs 泛化。**方法论基础——谱动态视角用于理解 collapse 中的权重变化。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `lu2024alphapruning` | Lu et al. \"AlphaPruning\" (NeurIPS 2024) | **method component** |\n\n用 heavy-tailed self-regularization 理论的谱密度形态 (alpha exponent) 指导 LLM 层级剪枝。**验证了 per-layer 谱分析对 LLM 质量评估的有效性，支持我们用类似方法监控 collapse。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `sanyal2020stablerank` | Sanyal et al. \"Stable Rank Normalization\" (ICLR 2020) | **method component** |\n\n提出 stable rank normalization 方法，证明控制 stable rank 可改善泛化（11.3% generalization gap 改善）。**理论支持——stable rank 与泛化能力的直接联系。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `liu2026spectrallens` | Liu et al. \"Spectral Lens\" (arXiv 2026) | **complementary** |\n\n用 activation covariance 和 per-sample gradient 的 SVD 谱诊断 LLM 训练优化。**方法论高度相关——同样用频谱分析训练动态，但不研究 collapse。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `xu2026compression` | Xu \"Predicting LLM Compression Degradation from Spectral Statistics\" (arXiv 2026) | **complementary** |\n\nstable rank 是压缩退化的主要预测因子 (r=0.890)，per-layer 分析优于全局。**直接验证 stable rank 作为退化预测信号的有效性。**\n\n---\n\n## 4. Training Dynamics Monitoring (4 papers)\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `kalinowski2026monitoring` | Kalinowski \"Monitoring Neural Training with Topology\" (arXiv 2026) | **direct competitor** |\n\n在线拓扑监控器——persistent homology + Collapse Index 提供低延迟早期预警。**在线监控但信号族不同（拓扑 vs 频谱/熵），不研究迭代合成数据场景。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `chen2024dse` | Liu et al. \"Diffusion Spectral Entropy for Neural Network Representations\" (IEEE CISS 2024) | **method component** |\n\n提出 DSE 和 DSMI——利用数据几何在高维中计算信息论指标，DSE 在训练中增加。**我们 spectral entropy 信号的潜在替代实现。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `kalra2026curvature` | Kalra et al. \"Scalable Loss Landscape Curvature for LLM Training Dynamics\" (arXiv 2026) | **complementary** |\n\nCritical sharpness：<10 forward passes 捕获 Hessian sharpness，首次在 7B 规模验证 progressive sharpening/Edge of Stability。**训练动态监控方法论参考——高效的大规模 LLM 训练动态度量。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `conzelmann2026layercollapse` | Conzelmann et al. \"Layer Collapse in Diffusion Language Models\" (arXiv 2026) | **complementary** |\n\n分析 diffusion LM 中 per-layer activation collapse——少数层的 channel-axis collapse 对整体生成至关重要。**per-layer collapse 分析方法论参考。**\n\n---\n\n## 5. Data Quality & Model Degradation (3 papers)\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `wyss2024surprise` | Wyss et al. \"Learning by Surprise: Surplexity\" (arXiv 2024) | **complementary** |\n\n用语义网络和 next-token 概率量化 LLM collapse 中的多样性损失。**输出级 collapse 量化方法——合成比例实验设计与我们重叠。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `penedo2024fineweb` | Penedo et al. \"The FineWeb Datasets\" (arXiv 2024) | **background** |\n\n15T token 数据集，详细文档化去重、过滤等数据策略。**数据质量策略参考——理解高质量训练数据的标准。**\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `zhang2026auditor` | Zhang et al. \"The LLM Data Auditor\" (arXiv 2026) | **background** |\n\n系统分类合成数据评估指标——quality (validity/fidelity/utility) + trustworthiness (safety/faithfulness)。**合成数据质量评估框架，为理解 collapse 的数据级原因提供指标体系。**\n\n---\n\n## 6. Foundational (1 paper)\n\n| Key | Paper | Role |\n|-----|-------|------|\n| `papyan2020neuralcollapse` | Papyan et al. \"Prevalence of Neural Collapse\" (PNAS 2020) | **foundation** |\n\n发现分类网络训练末期的 Neural Collapse 现象——类内表征收缩到 Simplex ETF。**虽然与 model collapse 不同，但提供了\"collapse\"概念的对比参考，且其谱分析方法论可借鉴。**\n\n---\n\n## Summary Statistics\n\n| Category | Count | Direct Competitors | Background | Method Component | Complementary |\n|----------|-------|-------------------|------------|-----------------|---------------|\n| Model Collapse Theory | 14 | 0 | 7 | 0 | 5 |\n| Data Contamination | 5 | 0 | 3 | 0 | 2 |\n| Spectral Methods | 7 | 1 | 0 | 4 | 2 |\n| Training Dynamics | 4 | 1 | 0 | 1 | 2 |\n| Data Quality | 3 | 0 | 2 | 0 | 1 |\n| Foundational | 1 | 0 | 0 | 0 | 0 |\n| **Total** | **33** | **2** | **12** | **5** | **12** |\n\nFoundation papers: 2 (shumailov2024curse, papyan2020neuralcollapse)\n",
      "numLines": 258,
      "startLine": 1,
      "totalLines": 258
    }
  },
  "sourceToolAssistantUUID": "8d32e62b-0c70-4fa1-823d-829af339ad12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T22:42:07.940Z_

<details><summary>↩ Tool result · `toolu_01SDjeHburHBkzfU1CbKQ74c`</summary>

```text
1	% ============================================================
2	% References for collapse_severity_monitor
3	% 33 papers, organized by topic
4	% Last updated: 2026-05-14
5	% ============================================================
6	
7	% ===================== 1. MODEL COLLAPSE THEORY =====================
8	
9	@article{shumailov2024curse,
10	  author    = {Ilia Shumailov and Zakhar Shumaylov and Yiren Zhao and Nicolas Papernot and Ross Anderson and Yarin Gal},
11	  title     = {{AI} Models Collapse When Trained on Recursively Generated Data},
12	  journal   = {Nature},
13	  volume    = {631},
14	  pages     = {755--759},
15	  year      = {2024},
16	  doi       = {10.1038/s41586-024-07566-y},
17	}
18	
19	@inproceedings{dohmatob2025strong,
20	  author    = {Elvis Dohmatob and Yunzhen Feng and Pu Yang and Francois Charton and Julia Kempe},
21	  title     = {Strong Model Collapse},
22	  booktitle = {International Conference on Learning Representations (ICLR)},
23	  year      = {2025},
24	  note      = {Spotlight},
25	}
26	
27	@inproceedings{alemohammad2024mad,
28	  author    = {Sina Alemohammad and Josue Casco-Rodriguez and Lorenzo Luzi and Ahmed Imtiaz Humayun and Hossein Babaei and Daniel LeJeune and Ali Siahkoohi and Richard G. Baraniuk},
29	  title     = {Self-Consuming Generative Models Go {MAD}},
30	  booktitle = {International Conference on Learning Representations (ICLR)},
31	  year      = {2024},
32	}
33	
34	@inproceedings{dohmatob2024tails,
35	  author    = {Elvis Dohmatob and Yunzhen Feng and Pu Yang and Francois Charton and Julia Kempe},
36	  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},
37	  booktitle = {International Conference on Machine Learning (ICML)},
38	  pages     = {11165--11197},
39	  year      = {2024},
40	}
41	
42	@inproceedings{fu2024selfconsuming,
43	  author    = {Shi Fu and Sen Zhang and Yingjie Wang and Xinmei Tian and Dacheng Tao},
44	  title     = {Towards Theoretical Understandings of Self-Consuming Generative Models},
45	  booktitle = {International Conference on Machine Learning (ICML)},
46	  year      = {2024},
47	}
48	
49	@article{gerstgrasser2024inevitable,
50	  author    = {Matthias Gerstgrasser and Rylan Schaeffer and Apratim Dey and Rafael Rafailov and Henry Sleight and John Hughes and Tomasz Korbak and Rajashree Agrawal and Dhruv Pai and Andrey Gromov and Daniel A. Roberts and Diyi Yang and David L. Donoho and Sanmi Koyejo},
51	  title     = {Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},
52	  journal   = {arXiv preprint arXiv:2404.01413},
53	  year      = {2024},
54	}
55	
56	@article{seddik2024bad,
57	  author    = {Mohamed El Amine Seddik and Suei-Hai Chen and Soufiane Hayou and Pierre Youssef and Merouane Debbah},
58	  title     = {How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse},
59	  journal   = {arXiv preprint arXiv:2404.05090},
60	  year      = {2024},
61	}
62	
63	@article{kazdan2024collapse,
64	  author    = {Joshua Kazdan and Rylan Schaeffer and Apratim Dey and Matthias Gerstgrasser and Rafael Rafailov and David L. Donoho and Sanmi Koyejo},
65	  title     = {Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
66	  journal   = {arXiv preprint arXiv:2410.16713},
67	  year      = {2024},
68	}
69	
70	@article{schaeffer2025position,
71	  author    = {Rylan Schaeffer and Joshua Kazdan and Alvan Caleb Arulandu and Sanmi Koyejo},
72	  title     = {Position: Model Collapse Does Not Mean What You Think},
73	  journal   = {arXiv preprint arXiv:2503.03150},
74	  year      = {2025},
75	}
76	
77	@article{bakshi2026improvement,
78	  author    = {Soham Bakshi and others},
79	  title     = {From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources},
80	  journal   = {arXiv preprint arXiv:2602.10531},
81	  year      = {2026},
82	}
83	
84	@inproceedings{shi2025closerlook,
85	  author    = {Lianghe Shi and Meng Wu and Huijie Zhang and Zekai Zhang and Molei Tao and Qing Qu},
86	  title     = {A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
87	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
88	  year      = {2025},
89	  note      = {Spotlight},
90	}
91	
92	@inproceedings{feng2025verification,
93	  author    = {Yunzhen Feng and Elvis Dohmatob and Pu Yang and Francois Charton and Julia Kempe},
94	  title     = {Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification},
95	  booktitle = {International Conference on Learning Representations (ICLR)},
96	  year      = {2025},
97	}
98	
99	@article{yi2025escaping,
100	  author    = {Bingji Yi and Qiyuan Liu and Yuwei Cheng and Haifeng Xu},
101	  title     = {Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence},
102	  journal   = {arXiv preprint arXiv:2510.16657},
103	  year      = {2025},
104	}
105	
106	@inproceedings{gillman2024selfcorrecting,
107	  author    = {Nate Gillman and Michael Freeman and Daksh Aggarwal and Chia-Hong Hsu and Calvin Luo and Yonglong Tian and Chen Sun},
108	  title     = {Self-Correcting Self-Consuming Loops for Generative Model Training},
109	  booktitle = {International Conference on Machine Learning (ICML)},
110	  year      = {2024},
111	}
112	
113	% ===================== 2. DATA CONTAMINATION DETECTION =====================
114	
115	@inproceedings{sander2024radioactive,
116	  author    = {Tom Sander and Pierre Fernandez and Alain Durmus and Matthijs Douze and Teddy Furon},
117	  title     = {Watermarking Makes Language Models Radioactive},
118	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
119	  year      = {2024},
120	}
121	
122	@article{dathathri2024synthid,
123	  author    = {Sumanth Dathathri and Abigail See and Sumedh Ghaisas and Po-Sen Huang and Rob McAdam and Johannes Welbl and Vandana Bachani and Alex Kaskasoli and Robert Stanforth and Tatiana Matejovicova and Jamie Hayes and Nidhi Vyas and Majd Al Merey and Jonah Brown-Cohen and Rudy Bunel and Borja Balle and Ander Steiner and Cem Anil and Pushmeet Kohli},
124	  title     = {Scalable Watermarking for Identifying Large Language Model Outputs},
125	  journal   = {Nature},
126	  volume    = {634},
127	  pages     = {818--823},
128	  year      = {2024},
129	  doi       = {10.1038/s41586-024-08025-4},
130	}
131	
132	@inproceedings{kirchenbauer2023watermark,
133	  author    = {John Kirchenbauer and Jonas Geiping and Yuxin Wen and Jonathan Katz and Ian Miers and Tom Goldstein},
134	  title     = {A Watermark for Large Language Models},
135	  booktitle = {International Conference on Machine Learning (ICML)},
136	  pages     = {17061--17084},
137	  year      = {2023},
138	}
139	
140	@inproceedings{mitchell2023detectgpt,
141	  author    = {Eric Mitchell and Yoonho Lee and Alexander Khazatsky and Christopher D. Manning and Chelsea Finn},
142	  title     = {{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
143	  booktitle = {International Conference on Machine Learning (ICML)},
144	  pages     = {24950--24962},
145	  year      = {2023},
146	}
147	
148	@inproceedings{shi2024detecting,
149	  author    = {Weijia Shi and Anirudh Ajith and Mengzhou Xia and Yangsibo Huang and Daogao Liu and Terra Blevins and Danqi Chen and Luke Zettlemoyer},
150	  title     = {Detecting Pretraining Data from Large Language Models},
151	  booktitle = {International Conference on Learning Representations (ICLR)},
152	  year      = {2024},
153	}
154	
155	% ===================== 3. SPECTRAL METHODS IN NLP/LLM =====================
156	
157	@article{martin2021weightwatcher,
158	  author    = {Charles H. Martin and Michael W. Mahoney},
159	  title     = {Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data},
160	  journal   = {Nature Communications},
161	  volume    = {12},
162	  number    = {1},
163	  pages     = {4118},
164	  year      = {2021},
165	  doi       = {10.1038/s41467-021-24025-8},
166	}
167	
168	@article{yunis2024spectral,
169	  author    = {David Yunis and Kumar Kshitij Patel and Samuel Denton and Sasha Beliy and Guillermo {del Rio} and Gintare Karolina Dziugaite and Daniel M. Roy},
170	  title     = {Approaching Deep Learning through the Spectral Dynamics of Weights},
171	  journal   = {arXiv preprint arXiv:2408.11804},
172	  year      = {2024},
173	}
174	
175	@inproceedings{lu2024alphapruning,
176	  author    = {Haiquan Lu and Yefan Zhou and Shiwei Liu and Zhangyang Wang and Michael W. Mahoney and Yaoqing Yang},
177	  title     = {{AlphaPruning}: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models},
178	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
179	  year      = {2024},
180	}
181	
182	@inproceedings{sanyal2020stablerank,
183	  author    = {Amartya Sanyal and Philip H. S. Torr and Puneet K. Dokania},
184	  title     = {Stable Rank Normalization for Improved Generalization in Neural Networks and {GAN}s},
185	  booktitle = {International Conference on Learning Representations (ICLR)},
186	  year      = {2020},
187	}
188	
189	@article{azam2026sigma,
190	  author    = {Yi Gu and Lingyou Pang and Xiangkun Ye and Tianyu Wang and Jianyu Lin and Carey E. Priebe and Alexander Aue},
191	  title     = {{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},
192	  journal   = {arXiv preprint arXiv:2601.03385},
193	  year      = {2026},
194	}
195	
196	@article{liu2026spectrallens,
197	  author    = {Andy Zeyi Liu and others},
198	  title     = {Spectral Lens: Activation and Gradient Spectra as Diagnostics of {LLM} Optimization},
199	  journal   = {arXiv preprint arXiv:2605.05683},
200	  year      = {2026},
201	}
202	
203	@article{xu2026compression,
204	  author    = {Mingxue Xu},
205	  title     = {Predicting {LLM} Compression Degradation from Spectral Statistics},
206	  journal   = {arXiv preprint arXiv:2604.18085},
207	  year      = {2026},
208	}
209	
210	@article{conzelmann2026layercollapse,
211	  author    = {Alexander Conzelmann and Albert Catalan-Tatjer and Shiwei Liu},
212	  title     = {Layer Collapse in Diffusion Language Models},
213	  journal   = {arXiv preprint arXiv:2605.06366},
214	  year      = {2026},
215	}
216	
217	% ===================== 4. TRAINING DYNAMICS MONITORING =====================
218	
219	@inproceedings{chen2024dse,
220	  author    = {Chen Liu and Xiuyuan Cheng and Yao Xie},
221	  title     = {Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy},
222	  booktitle = {IEEE Conference on Information Sciences and Systems (CISS)},
223	  year      = {2024},
224	}
225	
226	@article{kalra2026curvature,
227	  author    = {Dayal Singh Kalra and Jean-Christophe Gagnon-Audet and Andrey Gromov and Ishita Mediratta and Kelvin Niu and Alexander H. Miller and Michael Shvartsman},
228	  title     = {A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of {LLM}s},
229	  journal   = {arXiv preprint arXiv:2601.16979},
230	  year      = {2026},
231	}
232	
233	@article{kalinowski2026monitoring,
234	  author    = {Alexander Kalinowski},
235	  title     = {Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index},
236	  journal   = {arXiv preprint arXiv:2604.26984},
237	  year      = {2026},
238	}
239	
240	% ===================== 5. DATA QUALITY & MODEL DEGRADATION =====================
241	
242	@article{wyss2024surprise,
243	  author    = {C. M. Wyss and others},
244	  title     = {Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},
245	  journal   = {arXiv preprint arXiv:2410.12341},
246	  year      = {2024},
247	}
248	
249	@article{penedo2024fineweb,
250	  author    = {Guilherme Penedo and Hynek Kydl{\'\i}{\v{c}}ek and Loubna {Ben allal} and Anton Lozhkov and Margaret Mitchell and Colin Raffel and Leandro {Von Werra} and Thomas Wolf},
251	  title     = {The {FineWeb} Datasets: Decanting the Web for the Finest Text Data at Scale},
252	  journal   = {arXiv preprint arXiv:2406.17557},
253	  year      = {2024},
254	}
255	
256	@article{zhang2026auditor,
257	  author    = {Kaituo Zhang and Mingzhi Hu and Hoang Anh Duy Le and Fariha Kabir Torsha and Zhimeng Jiang and Minh Khai Bui and Chia-Yuan Chang and Yu-Neng Chuang and Zhen Xiong and Ying Lin and Guanchu Wang and Na Zou},
258	  title     = {The {LLM} Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data},
259	  journal   = {arXiv preprint arXiv:2601.17717},
260	  year      = {2026},
261	}
262	
263	% ===================== 6. FOUNDATIONAL =====================
264	
265	@article{papyan2020neuralcollapse,
266	  author    = {Vardan Papyan and X. Y. Han and David L. Donoho},
267	  title     = {Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training},
268	  journal   = {Proceedings of the National Academy of Sciences (PNAS)},
269	  volume    = {117},
270	  number    = {40},
271	  pages     = {24652--24663},
272	  year      = {2020},
273	  doi       = {10.1073/pnas.2015509117},
274	}
275	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b385fc9-27e7-4b3e-984d-d9a8f61c0ddd",
  "isSidechain": false,
  "promptId": "985e4d4c-de63-470a-9f8d-580809be0b1f",
  "type": "user",
  "uuid": "469e6f28-b41a-455a-9f98-2c0a53a65926",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/references.bib",
      "content": "% ============================================================\n% References for collapse_severity_monitor\n% 33 papers, organized by topic\n% Last updated: 2026-05-14\n% ============================================================\n\n% ===================== 1. MODEL COLLAPSE THEORY =====================\n\n@article{shumailov2024curse,\n  author    = {Ilia Shumailov and Zakhar Shumaylov and Yiren Zhao and Nicolas Papernot and Ross Anderson and Yarin Gal},\n  title     = {{AI} Models Collapse When Trained on Recursively Generated Data},\n  journal   = {Nature},\n  volume    = {631},\n  pages     = {755--759},\n  year      = {2024},\n  doi       = {10.1038/s41586-024-07566-y},\n}\n\n@inproceedings{dohmatob2025strong,\n  author    = {Elvis Dohmatob and Yunzhen Feng and Pu Yang and Francois Charton and Julia Kempe},\n  title     = {Strong Model Collapse},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n  note      = {Spotlight},\n}\n\n@inproceedings{alemohammad2024mad,\n  author    = {Sina Alemohammad and Josue Casco-Rodriguez and Lorenzo Luzi and Ahmed Imtiaz Humayun and Hossein Babaei and Daniel LeJeune and Ali Siahkoohi and Richard G. Baraniuk},\n  title     = {Self-Consuming Generative Models Go {MAD}},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n}\n\n@inproceedings{dohmatob2024tails,\n  author    = {Elvis Dohmatob and Yunzhen Feng and Pu Yang and Francois Charton and Julia Kempe},\n  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  pages     = {11165--11197},\n  year      = {2024},\n}\n\n@inproceedings{fu2024selfconsuming,\n  author    = {Shi Fu and Sen Zhang and Yingjie Wang and Xinmei Tian and Dacheng Tao},\n  title     = {Towards Theoretical Understandings of Self-Consuming Generative Models},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2024},\n}\n\n@article{gerstgrasser2024inevitable,\n  author    = {Matthias Gerstgrasser and Rylan Schaeffer and Apratim Dey and Rafael Rafailov and Henry Sleight and John Hughes and Tomasz Korbak and Rajashree Agrawal and Dhruv Pai and Andrey Gromov and Daniel A. Roberts and Diyi Yang and David L. Donoho and Sanmi Koyejo},\n  title     = {Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},\n  journal   = {arXiv preprint arXiv:2404.01413},\n  year      = {2024},\n}\n\n@article{seddik2024bad,\n  author    = {Mohamed El Amine Seddik and Suei-Hai Chen and Soufiane Hayou and Pierre Youssef and Merouane Debbah},\n  title     = {How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse},\n  journal   = {arXiv preprint arXiv:2404.05090},\n  year      = {2024},\n}\n\n@article{kazdan2024collapse,\n  author    = {Joshua Kazdan and Rylan Schaeffer and Apratim Dey and Matthias Gerstgrasser and Rafael Rafailov and David L. Donoho and Sanmi Koyejo},\n  title     = {Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\n  journal   = {arXiv preprint arXiv:2410.16713},\n  year      = {2024},\n}\n\n@article{schaeffer2025position,\n  author    = {Rylan Schaeffer and Joshua Kazdan and Alvan Caleb Arulandu and Sanmi Koyejo},\n  title     = {Position: Model Collapse Does Not Mean What You Think},\n  journal   = {arXiv preprint arXiv:2503.03150},\n  year      = {2025},\n}\n\n@article{bakshi2026improvement,\n  author    = {Soham Bakshi and others},\n  title     = {From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources},\n  journal   = {arXiv preprint arXiv:2602.10531},\n  year      = {2026},\n}\n\n@inproceedings{shi2025closerlook,\n  author    = {Lianghe Shi and Meng Wu and Huijie Zhang and Zekai Zhang and Molei Tao and Qing Qu},\n  title     = {A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2025},\n  note      = {Spotlight},\n}\n\n@inproceedings{feng2025verification,\n  author    = {Yunzhen Feng and Elvis Dohmatob and Pu Yang and Francois Charton and Julia Kempe},\n  title     = {Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n}\n\n@article{yi2025escaping,\n  author    = {Bingji Yi and Qiyuan Liu and Yuwei Cheng and Haifeng Xu},\n  title     = {Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence},\n  journal   = {arXiv preprint arXiv:2510.16657},\n  year      = {2025},\n}\n\n@inproceedings{gillman2024selfcorrecting,\n  author    = {Nate Gillman and Michael Freeman and Daksh Aggarwal and Chia-Hong Hsu and Calvin Luo and Yonglong Tian and Chen Sun},\n  title     = {Self-Correcting Self-Consuming Loops for Generative Model Training},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2024},\n}\n\n% ===================== 2. DATA CONTAMINATION DETECTION =====================\n\n@inproceedings{sander2024radioactive,\n  author    = {Tom Sander and Pierre Fernandez and Alain Durmus and Matthijs Douze and Teddy Furon},\n  title     = {Watermarking Makes Language Models Radioactive},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2024},\n}\n\n@article{dathathri2024synthid,\n  author    = {Sumanth Dathathri and Abigail See and Sumedh Ghaisas and Po-Sen Huang and Rob McAdam and Johannes Welbl and Vandana Bachani and Alex Kaskasoli and Robert Stanforth and Tatiana Matejovicova and Jamie Hayes and Nidhi Vyas and Majd Al Merey and Jonah Brown-Cohen and Rudy Bunel and Borja Balle and Ander Steiner and Cem Anil and Pushmeet Kohli},\n  title     = {Scalable Watermarking for Identifying Large Language Model Outputs},\n  journal   = {Nature},\n  volume    = {634},\n  pages     = {818--823},\n  year      = {2024},\n  doi       = {10.1038/s41586-024-08025-4},\n}\n\n@inproceedings{kirchenbauer2023watermark,\n  author    = {John Kirchenbauer and Jonas Geiping and Yuxin Wen and Jonathan Katz and Ian Miers and Tom Goldstein},\n  title     = {A Watermark for Large Language Models},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  pages     = {17061--17084},\n  year      = {2023},\n}\n\n@inproceedings{mitchell2023detectgpt,\n  author    = {Eric Mitchell and Yoonho Lee and Alexander Khazatsky and Christopher D. Manning and Chelsea Finn},\n  title     = {{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  pages     = {24950--24962},\n  year      = {2023},\n}\n\n@inproceedings{shi2024detecting,\n  author    = {Weijia Shi and Anirudh Ajith and Mengzhou Xia and Yangsibo Huang and Daogao Liu and Terra Blevins and Danqi Chen and Luke Zettlemoyer},\n  title     = {Detecting Pretraining Data from Large Language Models},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n}\n\n% ===================== 3. SPECTRAL METHODS IN NLP/LLM =====================\n\n@article{martin2021weightwatcher,\n  author    = {Charles H. Martin and Michael W. Mahoney},\n  title     = {Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data},\n  journal   = {Nature Communications},\n  volume    = {12},\n  number    = {1},\n  pages     = {4118},\n  year      = {2021},\n  doi       = {10.1038/s41467-021-24025-8},\n}\n\n@article{yunis2024spectral,\n  author    = {David Yunis and Kumar Kshitij Patel and Samuel Denton and Sasha Beliy and Guillermo {del Rio} and Gintare Karolina Dziugaite and Daniel M. Roy},\n  title     = {Approaching Deep Learning through the Spectral Dynamics of Weights},\n  journal   = {arXiv preprint arXiv:2408.11804},\n  year      = {2024},\n}\n\n@inproceedings{lu2024alphapruning,\n  author    = {Haiquan Lu and Yefan Zhou and Shiwei Liu and Zhangyang Wang and Michael W. Mahoney and Yaoqing Yang},\n  title     = {{AlphaPruning}: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2024},\n}\n\n@inproceedings{sanyal2020stablerank,\n  author    = {Amartya Sanyal and Philip H. S. Torr and Puneet K. Dokania},\n  title     = {Stable Rank Normalization for Improved Generalization in Neural Networks and {GAN}s},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2020},\n}\n\n@article{azam2026sigma,\n  author    = {Yi Gu and Lingyou Pang and Xiangkun Ye and Tianyu Wang and Jianyu Lin and Carey E. Priebe and Alexander Aue},\n  title     = {{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},\n  journal   = {arXiv preprint arXiv:2601.03385},\n  year      = {2026},\n}\n\n@article{liu2026spectrallens,\n  author    = {Andy Zeyi Liu and others},\n  title     = {Spectral Lens: Activation and Gradient Spectra as Diagnostics of {LLM} Optimization},\n  journal   = {arXiv preprint arXiv:2605.05683},\n  year      = {2026},\n}\n\n@article{xu2026compression,\n  author    = {Mingxue Xu},\n  title     = {Predicting {LLM} Compression Degradation from Spectral Statistics},\n  journal   = {arXiv preprint arXiv:2604.18085},\n  year      = {2026},\n}\n\n@article{conzelmann2026layercollapse,\n  author    = {Alexander Conzelmann and Albert Catalan-Tatjer and Shiwei Liu},\n  title     = {Layer Collapse in Diffusion Language Models},\n  journal   = {arXiv preprint arXiv:2605.06366},\n  year      = {2026},\n}\n\n% ===================== 4. TRAINING DYNAMICS MONITORING =====================\n\n@inproceedings{chen2024dse,\n  author    = {Chen Liu and Xiuyuan Cheng and Yao Xie},\n  title     = {Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy},\n  booktitle = {IEEE Conference on Information Sciences and Systems (CISS)},\n  year      = {2024},\n}\n\n@article{kalra2026curvature,\n  author    = {Dayal Singh Kalra and Jean-Christophe Gagnon-Audet and Andrey Gromov and Ishita Mediratta and Kelvin Niu and Alexander H. Miller and Michael Shvartsman},\n  title     = {A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of {LLM}s},\n  journal   = {arXiv preprint arXiv:2601.16979},\n  year      = {2026},\n}\n\n@article{kalinowski2026monitoring,\n  author    = {Alexander Kalinowski},\n  title     = {Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index},\n  journal   = {arXiv preprint arXiv:2604.26984},\n  year      = {2026},\n}\n\n% ===================== 5. DATA QUALITY & MODEL DEGRADATION =====================\n\n@article{wyss2024surprise,\n  author    = {C. M. Wyss and others},\n  title     = {Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},\n  journal   = {arXiv preprint arXiv:2410.12341},\n  year      = {2024},\n}\n\n@article{penedo2024fineweb,\n  author    = {Guilherme Penedo and Hynek Kydl{\\'\\i}{\\v{c}}ek and Loubna {Ben allal} and Anton Lozhkov and Margaret Mitchell and Colin Raffel and Leandro {Von Werra} and Thomas Wolf},\n  title     = {The {FineWeb} Datasets: Decanting the Web for the Finest Text Data at Scale},\n  journal   = {arXiv preprint arXiv:2406.17557},\n  year      = {2024},\n}\n\n@article{zhang2026auditor,\n  author    = {Kaituo Zhang and Mingzhi Hu and Hoang Anh Duy Le and Fariha Kabir Torsha and Zhimeng Jiang and Minh Khai Bui and Chia-Yuan Chang and Yu-Neng Chuang and Zhen Xiong and Ying Lin and Guanchu Wang and Na Zou},\n  title     = {The {LLM} Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data},\n  journal   = {arXiv preprint arXiv:2601.17717},\n  year      = {2026},\n}\n\n% ===================== 6. FOUNDATIONAL =====================\n\n@article{papyan2020neuralcollapse,\n  author    = {Vardan Papyan and X. Y. Han and David L. Donoho},\n  title     = {Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training},\n  journal   = {Proceedings of the National Academy of Sciences (PNAS)},\n  volume    = {117},\n  number    = {40},\n  pages     = {24652--24663},\n  year      = {2020},\n  doi       = {10.1073/pnas.2015509117},\n}\n",
      "numLines": 275,
      "startLine": 1,
      "totalLines": 275
    }
  },
  "sourceToolAssistantUUID": "6b385fc9-27e7-4b3e-984d-d9a8f61c0ddd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T22:42:08.396Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Mt4H53Qi7qK6UnkehY7qHH`</summary>

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
  "parentUuid": "469e6f28-b41a-455a-9f98-2c0a53a65926",
  "isSidechain": false,
  "requestId": "req_011Cb3GWBP8qSjoabQ1rozXo",
  "type": "assistant",
  "uuid": "52c1ddf5-ca75-479f-a754-884b8f5cdc89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5tctSX7vDf1AdBwGUC2Hr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 22763,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 367,
          "cache_read_input_tokens": 22763,
          "cache_creation_input_tokens": 240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 240
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

_source line 17 · 2026-05-14T22:42:08.411Z_

<details><summary>↩ Tool result · `toolu_01Mt4H53Qi7qK6UnkehY7qHH`</summary>

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
  "parentUuid": "52c1ddf5-ca75-479f-a754-884b8f5cdc89",
  "isSidechain": false,
  "promptId": "985e4d4c-de63-470a-9f8d-580809be0b1f",
  "type": "user",
  "uuid": "e30521b4-0bb3-4cca-a4dc-47f8142427c3",
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
  "sourceToolAssistantUUID": "52c1ddf5-ca75-479f-a754-884b8f5cdc89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T22:42:08.854Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ChSK5tVdM9oGEwvAM4e84n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/figure_design.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e30521b4-0bb3-4cca-a4dc-47f8142427c3",
  "isSidechain": false,
  "requestId": "req_011Cb3GWBP8qSjoabQ1rozXo",
  "type": "assistant",
  "uuid": "1e7e61ef-9192-4569-b5ce-91881efaf975",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5tctSX7vDf1AdBwGUC2Hr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 22763,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 367,
          "cache_read_input_tokens": 22763,
          "cache_creation_input_tokens": 240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 240
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

_source line 19 · 2026-05-14T22:42:08.863Z_

<details><summary>↩ Tool result · `toolu_01ChSK5tVdM9oGEwvAM4e84n`</summary>

````text
1	# Figure Design Specification — collapse_severity_monitor
2	
3	NeurIPS 2026 (D&B / Main). All figures target single-column width (5.5") unless noted.
4	
5	---
6	
7	## Unified Style Spec
8	
9	### Color Palette (colorblind-friendly, 6-fraction sequential)
10	
11	```python
12	FRAC_COLORS = {
13	    0.00: "#4477AA",  # blue   — clean baseline
14	    0.10: "#66CCEE",  # cyan
15	    0.25: "#228833",  # green
16	    0.50: "#CCBB44",  # yellow
17	    0.75: "#EE6677",  # pink-red
18	    1.00: "#AA3377",  # purple-red — full synthetic
19	}
20	FRAC_LABELS = {
21	    0.00: "0% (clean)",
22	    0.10: "10%",
23	    0.25: "25%",
24	    0.50: "50%",
25	    0.75: "75%",
26	    1.00: "100%",
27	}
28	```
29	
30	Source: Paul Tol's colorblind-safe qualitative palette. Monotonic warm shift from blue (clean) to red (collapsed) encodes severity intuitively.
31	
32	### Typography
33	
34	| Element | Font Size | Weight |
35	|---------|-----------|--------|
36	| Axis labels | 9pt | Normal |
37	| Tick labels | 8pt | Normal |
38	| Legend entries | 8pt | Normal |
39	| Subplot titles (a), (b)... | 10pt | Bold |
40	| Figure title (if any) | — | Omit (use caption) |
41	
42	```python
43	RCPARAMS = {
44	    "font.family": "serif",
45	    "font.serif": ["Times New Roman", "DejaVu Serif"],
46	    "mathtext.fontset": "stix",
47	    "font.size": 8,
48	    "axes.labelsize": 9,
49	    "axes.titlesize": 10,
50	    "legend.fontsize": 8,
51	    "xtick.labelsize": 8,
52	    "ytick.labelsize": 8,
53	    "axes.linewidth": 0.8,
54	    "lines.linewidth": 1.5,
55	    "lines.markersize": 5,
56	    "savefig.dpi": 300,
57	    "savefig.bbox": "tight",
58	    "savefig.pad_inches": 0.02,
59	    "figure.constrained_layout.use": True,
60	}
61	```
62	
63	### Lines, Markers, Error Bands
64	
65	| Element | Spec |
66	|---------|------|
67	| Line width | 1.5pt |
68	| Marker | `o` (circle), size=5, edgecolor=white, edgewidth=0.5 |
69	| Error band | `fill_between`, alpha=0.15, same color as line |
70	| Error bar (if used) | capsize=2, linewidth=0.8 |
71	| Grid | `ax.grid(True, alpha=0.15, linewidth=0.4)` |
72	
73	---
74	
75	## Figure 1: Severity Curves (Signal × Generation × Fraction)
76	
77	### Layout
78	
79	2×2 subplot grid. Each subplot = one signal.
80	
81	```
82	(a) Stable Rank          (b) Spectral Entropy
83	(c) Token Entropy        (d) Perplexity
84	```
85	
86	`figsize=(5.5, 4.5)` — single-column, compact.
87	
88	### Wireframe
89	
90	```
91	  ┌─────────────────┬─────────────────┐
92	  │ (a) Stable Rank │(b) Spectral Ent.│
93	  │                 │                 │
94	  │  ╱── 100%       │       ╱── 100%  │
95	  │ ╱─── 75%        │     ╱─── 75%    │
96	  │ ─── 50%         │     ─── 50%     │
97	  │ ─── 25%         │     ─── 25%     │
98	  │ ─── 10%         │     ─── 10%     │
99	  │ ─── 0%          │     ─── 0%      │
100	  │   0  1  2  3  4 │   0  1  2  3  4 │
101	  │    Generation    │    Generation   │
102	  ├─────────────────┼─────────────────┤
103	  │(c) Token Entropy│ (d) Perplexity  │
104	  │                 │                 │
105	  │ ─── 0%          │            100% │
106	  │ ─── 10%         │ (log)   ╱── 75% │
107	  │ ─── 25%         │        ╱       │
108	  │     ╲── 50%     │       ╱── 50%   │
109	  │      ╲── 75%    │      ── 25%     │
110	  │       ╲── 100%  │      ── 10%     │
111	  │   0  1  2  3  4 │   0  1  2  3  4 │
112	  │    Generation    │    Generation   │
113	  └─────────────────┴─────────────────┘
114	  Shared legend at bottom (horizontal, 6 entries)
115	```
116	
117	### Axes
118	
119	| Subplot | Y-axis | Scale | Expected Range |
120	|---------|--------|-------|----------------|
121	| (a) Stable Rank | Stable Rank | linear | 20–200 |
122	| (b) Spectral Entropy | Spectral Entropy | linear | 0.69–0.92 |
123	| (c) Token Entropy | Token Entropy (nats) | linear | 0.5–2.5 |
124	| (d) Perplexity | Perplexity | **log** | 13–1000 |
125	
126	X-axis: Generation (0–4), integer ticks. All subplots share X-axis label.
127	
128	**PPL uses log scale** because range spans 13.5–960 (71×). Linear scale would compress 0–50% fractions into an indistinguishable band at the bottom.
129	
130	### Data Requirements
131	
132	| Field | Source |
133	|-------|--------|
134	| `stable_rank`, `spectral_entropy`, `token_entropy`, `perplexity` | End-of-generation records from `signals_{frac}pct_gen{g}_seed{s}.jsonl` |
135	| Aggregation | Mean ± std across 5 seeds (WikiText) or 3 seeds (PubMed) |
136	| Filter | `is_generation_end == True` or last record per generation |
137	
138	### Implementation
139	
140	```python
141	fig, axes = plt.subplots(2, 2, figsize=(5.5, 4.5))
142	signals = ["stable_rank", "spectral_entropy", "token_entropy", "perplexity"]
143	log_signals = {"perplexity"}
144	labels = ["(a)", "(b)", "(c)", "(d)"]
145	
146	for ax, sig, label in zip(axes.flat, signals, labels):
147	    for frac in [0.0, 0.10, 0.25, 0.50, 0.75, 1.00]:
148	        gens = np.arange(5)
149	        mean = df_agg.loc[(frac, slice(None)), sig].groupby("gen").mean().values
150	        std  = df_agg.loc[(frac, slice(None)), sig].groupby("gen").std().values
151	        ax.plot(gens, mean, marker="o", color=FRAC_COLORS[frac])
152	        ax.fill_between(gens, mean - std, mean + std, alpha=0.15,
153	                        color=FRAC_COLORS[frac])
154	    if sig in log_signals:
155	        ax.set_yscale("log")
156	    ax.set_title(label, loc="left", fontweight="bold")
157	    ax.set_ylabel(sig.replace("_", " ").title())
158	    ax.set_xticks(range(5))
159	
160	# Shared x-label and legend
161	for ax in axes[1]:
162	    ax.set_xlabel("Generation")
163	handles = [mpl.lines.Line2D([], [], color=c, marker="o", label=FRAC_LABELS[f])
164	           for f, c in FRAC_COLORS.items()]
165	fig.legend(handles=handles, loc="lower center", ncol=6,
166	           bbox_to_anchor=(0.5, -0.04), frameon=False)
167	fig.savefig("fig1_severity_curves.pdf")
168	```
169	
170	### Trade-offs
171	
172	| Option | Pros | Cons | Decision |
173	|--------|------|------|----------|
174	| 2×2 grid | Compact, single-column | Smaller per-subplot | **Chosen** — NeurIPS space constraint |
175	| 4×1 vertical | Larger per-subplot | Half page, poor space use | Reject |
176	| Inset for PPL linear | Shows low-fraction detail | Cluttered | Optional: add if reviewer requests |
177	| Normalized Y (% change from gen0) | Cross-signal comparable | Loses absolute values | **Appendix version** |
178	
179	---
180	
181	## Figure 2: ROC/AUC Curves (Collapse Detection)
182	
183	### Layout
184	
185	1×2 subplots: within-domain (WikiText) + cross-domain (PubMed).
186	
187	`figsize=(5.5, 2.8)`
188	
189	### Wireframe
190	
191	```
192	  ┌───────────────────┬───────────────────┐
193	  │(a) Within-Domain  │(b) Cross-Domain   │
194	  │   (WikiText)      │ (Train:WT→Test:PM)│
195	  │                   │                   │
196	  │  ╱── SR (0.97)    │  ╱── SR (0.94)    │
197	  │ ╱── PPL (0.93)    │ ╱── PPL (0.91)    │
198	  │╱── TE (0.91)      │╱── TE (0.88)      │
199	  │╱── SE (0.85)      │╱── SE (0.82)      │
200	  │ ⋰ diagonal        │ ⋰ diagonal        │
201	  │  0    FPR    1    │  0    FPR    1    │
202	  └───────────────────┴───────────────────┘
203	```
204	
205	### Statistical Methodology (Dream Review Constraint)
206	
207	**Clustered bootstrap** (required): one observation = one (fraction × seed) pair. Do NOT pool individual generation records — generations within the same run are serially dependent.
208	
209	Procedure:
210	1. For each (fraction, seed) pair → compute aggregate signal value (mean of end-of-gen values across 5 generations)
211	2. Binary label: contamination ≥ threshold → positive
212	3. Three thresholds → three ROC curves per subplot: `≥25%`, `≥50%`, `≥75%`
213	4. Bootstrap: resample (fraction × seed) clusters 1000×, compute ROC per resample
214	5. Report: mean ROC curve + 95% CI band (2.5th/97.5th percentile of TPR at each FPR)
215	
216	**Number of observations**: WikiText = 6 fractions × 5 seeds = 30; PubMed = 6 fractions × 3 seeds = 18.
217	
218	### Axes
219	
220	- X: False Positive Rate [0, 1]
221	- Y: True Positive Rate [0, 1]
222	- Diagonal dashed line (chance, gray, linewidth=0.8)
223	
224	### Signal Colors for ROC (distinct from fraction colors)
225	
226	```python
227	SIGNAL_COLORS = {
228	    "stable_rank":      "#E69F00",  # orange
229	    "perplexity":       "#56B4E9",  # sky blue
230	    "token_entropy":    "#009E73",  # green
231	    "spectral_entropy": "#CC79A7",  # pink
232	}
233	```
234	
235	### Implementation
236	
237	```python
238	from sklearn.metrics import roc_curve, auc
239	
240	fig, (ax_wd, ax_cd) = plt.subplots(1, 2, figsize=(5.5, 2.8))
241	
242	for ax, domain_data, title in [(ax_wd, wiki_data, "(a) Within-Domain"),
243	                                (ax_cd, pubmed_data, "(b) Cross-Domain")]:
244	    threshold = 0.75  # primary threshold shown; others as thinner lines
245	    for sig_name, color in SIGNAL_COLORS.items():
246	        # Clustered: one value per (frac, seed)
247	        y_true = (fracs >= threshold).astype(int)  # shape: (n_clusters,)
248	        y_score = cluster_means[sig_name]
249	        fpr, tpr, _ = roc_curve(y_true, y_score)
250	        auc_val = auc(fpr, tpr)
251	        ax.plot(fpr, tpr, color=color, label=f"{sig_name} (AUC={auc_val:.2f})")
252	        # Bootstrap CI
253	        tpr_boots = bootstrap_roc(y_true, y_score, n=1000)
254	        ax.fill_between(fpr_grid, tpr_boots_lo, tpr_boots_hi, alpha=0.1, color=color)
255	    ax.plot([0, 1], [0, 1], "--", color="gray", linewidth=0.8)
256	    ax.set_xlabel("False Positive Rate")
257	    ax.set_ylabel("True Positive Rate")
258	    ax.set_title(title, loc="left", fontweight="bold")
259	    ax.set_aspect("equal")
260	    ax.legend(fontsize=7, loc="lower right")
261	```
262	
263	### Trade-offs
264	
265	| Option | Pros | Cons | Decision |
266	|--------|------|------|----------|
267	| Multiple thresholds on same plot | Shows threshold sensitivity | Cluttered with 4 signals × 3 thresholds | **Primary: ≥75% only. ≥25%/≥50% in appendix** |
268	| Single combined plot | Less space | Can't compare domains | Reject |
269	| AUC bar chart instead of ROC | Simpler | Loses operating-point info | **Supplementary figure** |
270	
271	---
272	
273	## Figure 3: Seed Variance Visualization
274	
275	### Recommended: Option C (strip plot with mean + individual seeds)
276	
277	Heatmap (Option A) is compact but hides distribution shape. Swarm plot (B) gets noisy at 30 points per cell. **Strip plot with jittered points + mean line** strikes the best balance: shows individual seed values, enables visual assessment of spread, and is compact enough for single-column.
278	
279	### Layout
280	
281	1×4 horizontal subplots (one per signal). `figsize=(5.5, 2.0)`
282	
283	### Wireframe
284	
285	```
286	  ┌──────────┬──────────┬──────────┬──────────┐
287	  │(a) SR    │(b) PPL   │(c) TE    │(d) SE    │
288	  │          │          │          │          │
289	  │ · · ─ ·  │ · · ─ ·  │ · · ─ ·  │ · · ─ ·  │  ← gen4
290	  │ · ─ · ·  │ · ─ · ·  │ · ─ · ·  │ · ─ · ·  │  ← gen2
291	  │ · ─ ·    │ · ─ ·    │ · ─ ·    │ · ─ ·    │  ← gen0
292	  │   Fraction →        │          │          │
293	  └──────────┴──────────┴──────────┴──────────┘
294	  Legend: · = individual seed, ─ = mean
295	```
296	
297	Each subplot: X = fraction (6 categories), Y = normalized signal value (z-score or fold-change from 0% mean). Rows of dots at each fraction represent individual seed values; horizontal bar = mean.
298	
299	### Alternative: Coefficient of Variation Heatmap
300	
301	If reviewer prefers quantitative summary over raw points:
302	
303	```
304	  ┌─────────────────────────────────────┐
305	  │  Coefficient of Variation (%)       │
306	  │        gen0  gen1  gen2  gen3  gen4  │
307	  │  0%  │ 1.5│ 1.8│ 2.0│ 2.2│ 2.0│   │
308	  │ 10%  │ 1.8│ 2.5│ 3.0│ 3.5│ 3.2│   │
309	  │ 25%  │ 2.0│ 3.0│ 4.0│ 4.5│ 4.2│   │
310	  │ 50%  │ 2.5│ 5.0│ 7.0│ 7.5│ 6.8│   │
311	  │ 75%  │ 3.0│ 6.0│ 8.5│ 9.0│ 8.5│   │
312	  │100%  │ 3.5│ 6.5│ 8.0│ 8.0│ 7.5│   │
313	  └─────────────────────────────────────┘
314	  Colormap: sequential white→deep blue (low CV = consistent)
315	```
316	
317	`figsize=(3.5, 2.0)`, `cmap="Blues"`, `vmin=0, vmax=12`, annotation with `fmt=".1f"`.
318	
319	### Data Requirements
320	
321	| Field | Source |
322	|-------|--------|
323	| End-of-gen signal values | Per-seed `signals_{frac}pct_gen{g}_seed{s}.jsonl` |
324	| Required: ≥3 seeds per (fraction, generation) | plan_001: 5 seeds (WikiText) |
325	| Aggregation | None — plot raw per-seed values |
326	
327	### Implementation (strip plot version)
328	
329	```python
330	fig, axes = plt.subplots(1, 4, figsize=(5.5, 2.0), sharey=False)
331	signals = ["stable_rank", "perplexity", "token_entropy", "spectral_entropy"]
332	labels = ["(a) SR", "(b) PPL", "(c) TE", "(d) SE"]
333	
334	for ax, sig, label in zip(axes, signals, labels):
335	    for i, frac in enumerate(fracs_sorted):
336	        seed_vals = df_seeds.loc[frac, sig].values  # shape: (n_seeds,)
337	        jitter = np.random.uniform(-0.15, 0.15, len(seed_vals))
338	        ax.scatter(i + jitter, seed_vals, s=12, alpha=0.6,
339	                   color=FRAC_COLORS[frac], zorder=3)
340	        ax.hlines(seed_vals.mean(), i - 0.2, i + 0.2,
341	                  color=FRAC_COLORS[frac], linewidth=2, zorder=4)
342	    ax.set_xticks(range(len(fracs_sorted)))
343	    ax.set_xticklabels(["0", "10", "25", "50", "75", "100"], fontsize=7)
344	    ax.set_title(label, loc="left", fontweight="bold", fontsize=9)
345	    if sig == "perplexity":
346	        ax.set_yscale("log")
347	axes[0].set_ylabel("Signal Value")
348	fig.supxlabel("Synthetic Fraction (%)", fontsize=9)
349	```
350	
351	---
352	
353	## Figure 4: Per-Layer Collapse Heatmap (Supplementary → Main if space)
354	
355	### Layout
356	
357	Single heatmap. `figsize=(5.5, 3.5)`
358	
359	### Wireframe
360	
361	```
362	  ┌──────────────────────────────────────┐
363	  │  Stable Rank Fold Change (vs 0%)     │
364	  │                                      │
365	  │  Layer 27 ┃░░░░░░░░▓▓▓▓████████████│
366	  │  Layer 24 ┃░░░░░░░░▓▓▓▓████████████│
367	  │  ...      ┃                         │
368	  │  Layer 14 ┃░░░▓▓▓▓████████████████ │ ← core-mid peak
369	  │  Layer 10 ┃░░░▓▓▓▓████████████████ │
370	  │  ...      ┃                         │
371	  │  Layer 3  ┃░░░░░░░▓▓▓████████████  │
372	  │  Layer 0  ┃░░░░░░░░▓▓▓▓███████████ │
373	  │           ┗━━━━━━━━━━━━━━━━━━━━━━━━│
374	  │            gen0 gen1 gen2 gen3 gen4  │
375	  │         100% synthetic fraction     │
376	  └──────────────────────────────────────┘
377	  Colorbar: fold-change 1× (white) → 10× (dark red)
378	```
379	
380	### Axes
381	
382	- X: Generation (0–4)
383	- Y: Layer index (0–27, bottom to top)
384	- Color: Stable rank fold-change vs 0% baseline at same generation
385	- Colormap: `"Reds"`, vmin=1, vmax=12, log-normalized (`LogNorm`)
386	- Annotate layer groups with brackets on right margin: "embed-adj", "lower-mid", "core-mid", "upper-mid", "head-adj"
387	
388	### Data Requirements
389	
390	- Per-layer SVD: `layer_signals_{frac}pct_gen{g}_seed{s}.jsonl` (from plan_006)
391	- Fields: `layer_idx`, `stable_rank`, `spectral_entropy`, `sv_ratio_1_2`
392	- Two fractions needed: 0% (baseline) and 100% (collapsed). Optional: 50% as secondary panel.
393	
394	### Implementation
395	
396	```python
397	from matplotlib.colors import LogNorm
398	
399	fig, ax = plt.subplots(figsize=(5.5, 3.5))
400	
401	# sr_matrix shape: (28 layers, 5 gens), values = fold-change
402	sr_fold = sr_100pct / sr_0pct  # element-wise
403	im = ax.imshow(sr_fold, aspect="auto", cmap="Reds",
404	               norm=LogNorm(vmin=1, vmax=12), origin="lower",
405	               interpolation="nearest")
406	
407	ax.set_xticks(range(5))
408	ax.set_xticklabels([f"Gen {i}" for i in range(5)])
409	ax.set_ylabel("Layer Index")
410	ax.set_yticks(range(0, 28, 4))
411	
412	# Layer group annotations
413	groups = [(0, 3, "Embed\nadj."), (4, 7, "Lower\nmid"),
414	          (8, 14, "Core\nmid"), (15, 21, "Upper\nmid"), (22, 27, "Head\nadj.")]
415	for lo, hi, name in groups:
416	    ax.annotate(name, xy=(5.3, (lo + hi) / 2), fontsize=6,
417	                ha="left", va="center", annotation_clip=False)
418	    ax.add_patch(plt.Rectangle((-0.5, lo - 0.5), 5, hi - lo + 1,
419	                               fill=False, edgecolor="gray", linewidth=0.4))
420	
421	cbar = fig.colorbar(im, ax=ax, label="SR Fold Change vs Clean", shrink=0.8)
422	```
423	
424	---
425	
426	## Figure 5: Within-Generation Early Warning
427	
428	### Layout
429	
430	Single plot or 1×2 (one per scale). `figsize=(5.5, 2.8)`
431	
432	### Wireframe
433	
434	```
435	  ┌──────────────────────────────────────┐
436	  │  Stable Rank Deviation (%) vs 0%     │
437	  │                                      │
438	  │ 40% ─── ────── ──── ────── 100%      │
439	  │ 30% ─── ────── ──── ──               │
440	  │ 20% ─── ────── ─             75%     │
441	  │ 15%·················threshold·····   │
442	  │ 10% ─── ────                  50%    │
443	  │  5% ─── ──                    25%    │
444	  │  0%                            10%   │
445	  │     50  100  200  500  1540          │
446	  │            Training Step             │
447	  └──────────────────────────────────────┘
448	  Horizontal dashed line at 15% = optimal detection threshold
449	```
450	
451	### Axes
452	
453	- X: Training step (50, 100, 200, 500, 1000, 1540). Log or linear — **linear recommended** (steps are unevenly sampled but conceptually progressive).
454	- Y: Signal deviation % = |sig_frac - sig_0pct| / sig_0pct × 100
455	- Horizontal dashed line at 15% = optimal threshold from ROC analysis
456	
457	### Data Requirements
458	
459	- Within-generation signal values at specific steps
460	- Computed as: `deviation = abs(sig[frac, step] - sig[0%, step]) / sig[0%, step] * 100`
461	- Primary signal: stable_rank (best early indicator)
462	- Need 0% baseline at matched steps
463	
464	### Implementation
465	
466	```python
467	fig, ax = plt.subplots(figsize=(5.5, 2.8))
468	steps = [50, 100, 200, 500, 1000, 1540]
469	
470	for frac in [0.10, 0.25, 0.50, 0.75, 1.00]:
471	    devs_mean = [compute_deviation(frac, step, "stable_rank").mean() for step in steps]
472	    devs_std  = [compute_deviation(frac, step, "stable_rank").std() for step in steps]
473	    ax.plot(steps, devs_mean, marker="o", color=FRAC_COLORS[frac],
474	            label=FRAC_LABELS[frac])
475	    ax.fill_between(steps, np.array(devs_mean) - devs_std,
476	                     np.array(devs_mean) + devs_std, alpha=0.15,
477	                     color=FRAC_COLORS[frac])
478	
479	ax.axhline(15, linestyle="--", color="gray", linewidth=0.8, label="Threshold (15%)")
480	ax.set_xlabel("Training Step")
481	ax.set_ylabel("Stable Rank Deviation (%)")
482	ax.legend(fontsize=7, loc="upper left")
483	```
484	
485	---
486	
487	## Table 1: Signal Taxonomy (Main Text Table)
488	
489	Not a figure, but integral to Claim 3. Rendered as LaTeX `\begin{table}`.
490	
491	```
492	| Signal          | Family   | 0–10% | 10–25% | 25–50% | 50–75% | 75–100% | Best Use         |
493	|-----------------|----------|-------|--------|--------|--------|---------|------------------|
494	| Stable Rank     | Spectral | ★     | ★★     | ★★★    | ★★★    | sat.    | Early warning    |
495	| Spectral Ent.   | Spectral | ·     | ★      | ★★     | ★★★    | sat.    | Moderate sev.    |
496	| Perplexity      | Output   | ★     | ★★     | ★★★    | ★★★    | ★★★     | Universal meter  |
497	| Token Entropy   | Output   | ·     | ★      | ★★     | ★★★    | ★★★     | Severe collapse  |
498	| Gradient Norm   | Gradient | ·     | ·      | ★      | ★★ ↑   | ★ ↓     | NOT recommended  |
499	| HellaSwag       | Downstream| ·    | ·      | ·      | ★      | ★       | NOT recommended  |
500	```
501	
502	★ = informative (effect size d > 1). sat. = saturated. ↑↓ = non-monotonic.
503	
504	---
505	
506	## Data Pipeline Design
507	
508	### Step 1: Raw JSONL → Tidy DataFrame
509	
510	```python
511	import pandas as pd
512	import json
513	from pathlib import Path
514	
515	def load_signals_to_df(base_dir: str) -> pd.DataFrame:
516	    """Load all signals JSONL files into a single tidy DataFrame.
517	
518	    Expected file naming: signals_{frac}pct_gen{g}_seed{s}.jsonl
519	    Returns DataFrame with columns:
520	        fraction, generation, seed, step, stable_rank, spectral_entropy,
521	        token_entropy, perplexity, training_loss, gradient_norm,
522	        sv_ratio_1_2, top_singular_values
523	    """
524	    records = []
525	    for path in Path(base_dir).glob("signals_*pct_gen*_seed*.jsonl"):
526	        parts = path.stem.split("_")
527	        frac = int(parts[1].replace("pct", "")) / 100
528	        gen = int(parts[2].replace("gen", ""))
529	        seed = int(parts[3].replace("seed", ""))
530	        with open(path) as f:
531	            for line in f:
532	                r = json.loads(line)
533	                r["fraction"] = frac
534	                r["generation"] = gen
535	                r["seed"] = seed
536	                svs = r.get("top_singular_values", [])
537	                r["sv_ratio_1_2"] = svs[0] / svs[1] if len(svs) >= 2 and svs[1] > 0 else 0.0
538	                records.append(r)
539	    df = pd.DataFrame(records)
540	    return df
541	```
542	
543	### Step 2: End-of-Generation Aggregation (for Figures 1, 3)
544	
545	```python
546	def aggregate_end_of_gen(df: pd.DataFrame) -> pd.DataFrame:
547	    """Extract end-of-generation records, aggregate across seeds.
548	
549	    Returns DataFrame indexed by (fraction, generation) with columns:
550	        {signal}_mean, {signal}_std for each signal.
551	    """
552	    # Take last record per (fraction, generation, seed)
553	    eog = df.sort_values("step").groupby(["fraction", "generation", "seed"]).last().reset_index()
554	
555	    signals = ["stable_rank", "spectral_entropy", "token_entropy", "perplexity"]
556	    agg_dict = {s: ["mean", "std"] for s in signals}
557	    result = eog.groupby(["fraction", "generation"]).agg(agg_dict)
558	    result.columns = [f"{s}_{stat}" for s, stat in result.columns]
559	    return result
560	```
561	
562	### Step 3: Clustered Bootstrap for ROC (Figure 2)
563	
564	```python
565	def clustered_bootstrap_roc(df_eog: pd.DataFrame, signal: str,
566	                            threshold: float, n_boot: int = 1000):
567	    """Compute ROC with clustered bootstrap CIs.
568	
569	    One cluster = one (fraction, seed) pair.
570	    Binary label: fraction >= threshold → positive.
571	    """
572	    clusters = df_eog.groupby(["fraction", "seed"])[signal].mean().reset_index()
573	    clusters["label"] = (clusters["fraction"] >= threshold).astype(int)
574	
575	    fpr_grid = np.linspace(0, 1, 100)
576	    tpr_boots = []
577	
578	    for _ in range(n_boot):
579	        idx = np.random.choice(len(clusters), len(clusters), replace=True)
580	        boot = clusters.iloc[idx]
581	        if boot["label"].nunique() < 2:
582	            continue
583	        fpr, tpr, _ = roc_curve(boot["label"], boot[signal])
584	        tpr_interp = np.interp(fpr_grid, fpr, tpr)
585	        tpr_boots.append(tpr_interp)
586	
587	    tpr_boots = np.array(tpr_boots)
588	    return fpr_grid, np.mean(tpr_boots, axis=0), np.percentile(tpr_boots, [2.5, 97.5], axis=0)
589	```
590	
591	### Step 4: Within-Gen Deviation (Figure 5)
592	
593	```python
594	def compute_early_warning_deviation(df: pd.DataFrame, signal: str = "stable_rank"):
595	    """Compute signal deviation vs 0% baseline at each step.
596	
597	    Returns DataFrame with columns: fraction, step, deviation_pct, seed.
598	    """
599	    baseline = df[df["fraction"] == 0.0].groupby(["generation", "step", "seed"])[signal].mean()
600	    # Use gen=1 for early warning (first collapsing generation)
601	    df_gen1 = df[df["generation"] == 1]
602	    bl_gen1 = df_gen1[df_gen1["fraction"] == 0.0].set_index("step")[signal]
603	
604	    results = []
605	    for frac in [0.10, 0.25, 0.50, 0.75, 1.00]:
606	        for seed in df_gen1["seed"].unique():
607	            frac_data = df_gen1[(df_gen1["fraction"] == frac) & (df_gen1["seed"] == seed)]
608	            bl_seed = df_gen1[(df_gen1["fraction"] == 0.0) & (df_gen1["seed"] == seed)]
609	            for _, row in frac_data.iterrows():
610	                bl_val = bl_seed[bl_seed["step"] == row["step"]][signal].values
611	                if len(bl_val) > 0 and bl_val[0] > 0:
612	                    dev = abs(row[signal] - bl_val[0]) / bl_val[0] * 100
613	                    results.append({"fraction": frac, "step": row["step"],
614	                                    "seed": seed, "deviation_pct": dev})
615	    return pd.DataFrame(results)
616	```
617	
618	### Step 5: Per-Layer Fold Change (Figure 4)
619	
620	```python
621	def compute_layer_fold_change(base_dir: str):
622	    """Compute per-layer stable_rank fold change (100% / 0%).
623	
624	    Returns: np.ndarray of shape (n_layers, n_gens).
625	    """
626	    def load_layer_signals(frac_str):
627	        matrix = {}  # {(layer, gen): [values across seeds]}
628	        for path in Path(base_dir).glob(f"layer_signals_{frac_str}_gen*_seed*.jsonl"):
629	            gen = int(path.stem.split("_")[3].replace("gen", ""))
630	            with open(path) as f:
631	                for line in f:
632	                    r = json.loads(line)
633	                    key = (r["layer_idx"], gen)
634	                    matrix.setdefault(key, []).append(r["stable_rank"])
635	        return {k: np.mean(v) for k, v in matrix.items()}
636	
637	    sr_0   = load_layer_signals("0pct")
638	    sr_100 = load_layer_signals("100pct")
639	
640	    n_layers, n_gens = 28, 5
641	    fold = np.ones((n_layers, n_gens))
642	    for layer in range(n_layers):
643	        for gen in range(n_gens):
644	            bl = sr_0.get((layer, gen), 1)
645	            col = sr_100.get((layer, gen), 1)
646	            fold[layer, gen] = col / bl if bl > 0 else 1
647	    return fold
648	```
649	
650	---
651	
652	## Figure Priority for Main Text
653	
654	| Priority | Figure | Supports | Space |
655	|----------|--------|----------|-------|
656	| 1 (必须) | Fig 1: Severity Curves | Claim 1 | ~1/3 page |
657	| 2 (必须) | Fig 2: ROC Curves | Claim 2 + reviewer concern | ~1/4 page |
658	| 3 (必须) | Fig 3: Seed Variance | Reviewer concern (reproducibility) | ~1/6 page |
659	| 4 (强推) | Fig 4: Layer Heatmap | Claim 3 (depth) | ~1/3 page |
660	| 5 (强推) | Fig 5: Early Warning | Claim 2 (practitioner value) | ~1/4 page |
661	| — | Table 1: Signal Taxonomy | Claim 3 (summary) | ~1/6 page |
662	
663	Total main-text figures: 5 figures + 1 table ≈ 1.5 pages of visual content. NeurIPS allows 8 pages + unlimited appendix; this is a reasonable allocation for an analysis paper.
664	
665	### Appendix Figures
666	
667	- Fig A1: Severity curves with normalized Y-axis (% change from gen0)
668	- Fig A2: ROC curves at ≥25% and ≥50% thresholds
669	- Fig A3: QLoRA vs Full FT comparison (Table 5 as bar chart)
670	- Fig A4: Self-recovery PPL trajectories (zoom on 25%/50%/75%)
671	- Fig A5: AUC bar chart by signal × training progress %
672	- Fig A6: Per-layer spectral_entropy and sv_ratio heatmaps
673	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "1e7e61ef-9192-4569-b5ce-91881efaf975",
  "isSidechain": false,
  "promptId": "985e4d4c-de63-470a-9f8d-580809be0b1f",
  "type": "user",
  "uuid": "e90c5c7d-bf69-4da0-b453-ea2a91c881f2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/figure_design.md",
      "content": "# Figure Design Specification — collapse_severity_monitor\n\nNeurIPS 2026 (D&B / Main). All figures target single-column width (5.5\") unless noted.\n\n---\n\n## Unified Style Spec\n\n### Color Palette (colorblind-friendly, 6-fraction sequential)\n\n```python\nFRAC_COLORS = {\n    0.00: \"#4477AA\",  # blue   — clean baseline\n    0.10: \"#66CCEE\",  # cyan\n    0.25: \"#228833\",  # green\n    0.50: \"#CCBB44\",  # yellow\n    0.75: \"#EE6677\",  # pink-red\n    1.00: \"#AA3377\",  # purple-red — full synthetic\n}\nFRAC_LABELS = {\n    0.00: \"0% (clean)\",\n    0.10: \"10%\",\n    0.25: \"25%\",\n    0.50: \"50%\",\n    0.75: \"75%\",\n    1.00: \"100%\",\n}\n```\n\nSource: Paul Tol's colorblind-safe qualitative palette. Monotonic warm shift from blue (clean) to red (collapsed) encodes severity intuitively.\n\n### Typography\n\n| Element | Font Size | Weight |\n|---------|-----------|--------|\n| Axis labels | 9pt | Normal |\n| Tick labels | 8pt | Normal |\n| Legend entries | 8pt | Normal |\n| Subplot titles (a), (b)... | 10pt | Bold |\n| Figure title (if any) | — | Omit (use caption) |\n\n```python\nRCPARAMS = {\n    \"font.family\": \"serif\",\n    \"font.serif\": [\"Times New Roman\", \"DejaVu Serif\"],\n    \"mathtext.fontset\": \"stix\",\n    \"font.size\": 8,\n    \"axes.labelsize\": 9,\n    \"axes.titlesize\": 10,\n    \"legend.fontsize\": 8,\n    \"xtick.labelsize\": 8,\n    \"ytick.labelsize\": 8,\n    \"axes.linewidth\": 0.8,\n    \"lines.linewidth\": 1.5,\n    \"lines.markersize\": 5,\n    \"savefig.dpi\": 300,\n    \"savefig.bbox\": \"tight\",\n    \"savefig.pad_inches\": 0.02,\n    \"figure.constrained_layout.use\": True,\n}\n```\n\n### Lines, Markers, Error Bands\n\n| Element | Spec |\n|---------|------|\n| Line width | 1.5pt |\n| Marker | `o` (circle), size=5, edgecolor=white, edgewidth=0.5 |\n| Error band | `fill_between`, alpha=0.15, same color as line |\n| Error bar (if used) | capsize=2, linewidth=0.8 |\n| Grid | `ax.grid(True, alpha=0.15, linewidth=0.4)` |\n\n---\n\n## Figure 1: Severity Curves (Signal × Generation × Fraction)\n\n### Layout\n\n2×2 subplot grid. Each subplot = one signal.\n\n```\n(a) Stable Rank          (b) Spectral Entropy\n(c) Token Entropy        (d) Perplexity\n```\n\n`figsize=(5.5, 4.5)` — single-column, compact.\n\n### Wireframe\n\n```\n  ┌─────────────────┬─────────────────┐\n  │ (a) Stable Rank │(b) Spectral Ent.│\n  │                 │                 │\n  │  ╱── 100%       │       ╱── 100%  │\n  │ ╱─── 75%        │     ╱─── 75%    │\n  │ ─── 50%         │     ─── 50%     │\n  │ ─── 25%         │     ─── 25%     │\n  │ ─── 10%         │     ─── 10%     │\n  │ ─── 0%          │     ─── 0%      │\n  │   0  1  2  3  4 │   0  1  2  3  4 │\n  │    Generation    │    Generation   │\n  ├─────────────────┼─────────────────┤\n  │(c) Token Entropy│ (d) Perplexity  │\n  │                 │                 │\n  │ ─── 0%          │            100% │\n  │ ─── 10%         │ (log)   ╱── 75% │\n  │ ─── 25%         │        ╱       │\n  │     ╲── 50%     │       ╱── 50%   │\n  │      ╲── 75%    │      ── 25%     │\n  │       ╲── 100%  │      ── 10%     │\n  │   0  1  2  3  4 │   0  1  2  3  4 │\n  │    Generation    │    Generation   │\n  └─────────────────┴─────────────────┘\n  Shared legend at bottom (horizontal, 6 entries)\n```\n\n### Axes\n\n| Subplot | Y-axis | Scale | Expected Range |\n|---------|--------|-------|----------------|\n| (a) Stable Rank | Stable Rank | linear | 20–200 |\n| (b) Spectral Entropy | Spectral Entropy | linear | 0.69–0.92 |\n| (c) Token Entropy | Token Entropy (nats) | linear | 0.5–2.5 |\n| (d) Perplexity | Perplexity | **log** | 13–1000 |\n\nX-axis: Generation (0–4), integer ticks. All subplots share X-axis label.\n\n**PPL uses log scale** because range spans 13.5–960 (71×). Linear scale would compress 0–50% fractions into an indistinguishable band at the bottom.\n\n### Data Requirements\n\n| Field | Source |\n|-------|--------|\n| `stable_rank`, `spectral_entropy`, `token_entropy`, `perplexity` | End-of-generation records from `signals_{frac}pct_gen{g}_seed{s}.jsonl` |\n| Aggregation | Mean ± std across 5 seeds (WikiText) or 3 seeds (PubMed) |\n| Filter | `is_generation_end == True` or last record per generation |\n\n### Implementation\n\n```python\nfig, axes = plt.subplots(2, 2, figsize=(5.5, 4.5))\nsignals = [\"stable_rank\", \"spectral_entropy\", \"token_entropy\", \"perplexity\"]\nlog_signals = {\"perplexity\"}\nlabels = [\"(a)\", \"(b)\", \"(c)\", \"(d)\"]\n\nfor ax, sig, label in zip(axes.flat, signals, labels):\n    for frac in [0.0, 0.10, 0.25, 0.50, 0.75, 1.00]:\n        gens = np.arange(5)\n        mean = df_agg.loc[(frac, slice(None)), sig].groupby(\"gen\").mean().values\n        std  = df_agg.loc[(frac, slice(None)), sig].groupby(\"gen\").std().values\n        ax.plot(gens, mean, marker=\"o\", color=FRAC_COLORS[frac])\n        ax.fill_between(gens, mean - std, mean + std, alpha=0.15,\n                        color=FRAC_COLORS[frac])\n    if sig in log_signals:\n        ax.set_yscale(\"log\")\n    ax.set_title(label, loc=\"left\", fontweight=\"bold\")\n    ax.set_ylabel(sig.replace(\"_\", \" \").title())\n    ax.set_xticks(range(5))\n\n# Shared x-label and legend\nfor ax in axes[1]:\n    ax.set_xlabel(\"Generation\")\nhandles = [mpl.lines.Line2D([], [], color=c, marker=\"o\", label=FRAC_LABELS[f])\n           for f, c in FRAC_COLORS.items()]\nfig.legend(handles=handles, loc=\"lower center\", ncol=6,\n           bbox_to_anchor=(0.5, -0.04), frameon=False)\nfig.savefig(\"fig1_severity_curves.pdf\")\n```\n\n### Trade-offs\n\n| Option | Pros | Cons | Decision |\n|--------|------|------|----------|\n| 2×2 grid | Compact, single-column | Smaller per-subplot | **Chosen** — NeurIPS space constraint |\n| 4×1 vertical | Larger per-subplot | Half page, poor space use | Reject |\n| Inset for PPL linear | Shows low-fraction detail | Cluttered | Optional: add if reviewer requests |\n| Normalized Y (% change from gen0) | Cross-signal comparable | Loses absolute values | **Appendix version** |\n\n---\n\n## Figure 2: ROC/AUC Curves (Collapse Detection)\n\n### Layout\n\n1×2 subplots: within-domain (WikiText) + cross-domain (PubMed).\n\n`figsize=(5.5, 2.8)`\n\n### Wireframe\n\n```\n  ┌───────────────────┬───────────────────┐\n  │(a) Within-Domain  │(b) Cross-Domain   │\n  │   (WikiText)      │ (Train:WT→Test:PM)│\n  │                   │                   │\n  │  ╱── SR (0.97)    │  ╱── SR (0.94)    │\n  │ ╱── PPL (0.93)    │ ╱── PPL (0.91)    │\n  │╱── TE (0.91)      │╱── TE (0.88)      │\n  │╱── SE (0.85)      │╱── SE (0.82)      │\n  │ ⋰ diagonal        │ ⋰ diagonal        │\n  │  0    FPR    1    │  0    FPR    1    │\n  └───────────────────┴───────────────────┘\n```\n\n### Statistical Methodology (Dream Review Constraint)\n\n**Clustered bootstrap** (required): one observation = one (fraction × seed) pair. Do NOT pool individual generation records — generations within the same run are serially dependent.\n\nProcedure:\n1. For each (fraction, seed) pair → compute aggregate signal value (mean of end-of-gen values across 5 generations)\n2. Binary label: contamination ≥ threshold → positive\n3. Three thresholds → three ROC curves per subplot: `≥25%`, `≥50%`, `≥75%`\n4. Bootstrap: resample (fraction × seed) clusters 1000×, compute ROC per resample\n5. Report: mean ROC curve + 95% CI band (2.5th/97.5th percentile of TPR at each FPR)\n\n**Number of observations**: WikiText = 6 fractions × 5 seeds = 30; PubMed = 6 fractions × 3 seeds = 18.\n\n### Axes\n\n- X: False Positive Rate [0, 1]\n- Y: True Positive Rate [0, 1]\n- Diagonal dashed line (chance, gray, linewidth=0.8)\n\n### Signal Colors for ROC (distinct from fraction colors)\n\n```python\nSIGNAL_COLORS = {\n    \"stable_rank\":      \"#E69F00\",  # orange\n    \"perplexity\":       \"#56B4E9\",  # sky blue\n    \"token_entropy\":    \"#009E73\",  # green\n    \"spectral_entropy\": \"#CC79A7\",  # pink\n}\n```\n\n### Implementation\n\n```python\nfrom sklearn.metrics import roc_curve, auc\n\nfig, (ax_wd, ax_cd) = plt.subplots(1, 2, figsize=(5.5, 2.8))\n\nfor ax, domain_data, title in [(ax_wd, wiki_data, \"(a) Within-Domain\"),\n                                (ax_cd, pubmed_data, \"(b) Cross-Domain\")]:\n    threshold = 0.75  # primary threshold shown; others as thinner lines\n    for sig_name, color in SIGNAL_COLORS.items():\n        # Clustered: one value per (frac, seed)\n        y_true = (fracs >= threshold).astype(int)  # shape: (n_clusters,)\n        y_score = cluster_means[sig_name]\n        fpr, tpr, _ = roc_curve(y_true, y_score)\n        auc_val = auc(fpr, tpr)\n        ax.plot(fpr, tpr, color=color, label=f\"{sig_name} (AUC={auc_val:.2f})\")\n        # Bootstrap CI\n        tpr_boots = bootstrap_roc(y_true, y_score, n=1000)\n        ax.fill_between(fpr_grid, tpr_boots_lo, tpr_boots_hi, alpha=0.1, color=color)\n    ax.plot([0, 1], [0, 1], \"--\", color=\"gray\", linewidth=0.8)\n    ax.set_xlabel(\"False Positive Rate\")\n    ax.set_ylabel(\"True Positive Rate\")\n    ax.set_title(title, loc=\"left\", fontweight=\"bold\")\n    ax.set_aspect(\"equal\")\n    ax.legend(fontsize=7, loc=\"lower right\")\n```\n\n### Trade-offs\n\n| Option | Pros | Cons | Decision |\n|--------|------|------|----------|\n| Multiple thresholds on same plot | Shows threshold sensitivity | Cluttered with 4 signals × 3 thresholds | **Primary: ≥75% only. ≥25%/≥50% in appendix** |\n| Single combined plot | Less space | Can't compare domains | Reject |\n| AUC bar chart instead of ROC | Simpler | Loses operating-point info | **Supplementary figure** |\n\n---\n\n## Figure 3: Seed Variance Visualization\n\n### Recommended: Option C (strip plot with mean + individual seeds)\n\nHeatmap (Option A) is compact but hides distribution shape. Swarm plot (B) gets noisy at 30 points per cell. **Strip plot with jittered points + mean line** strikes the best balance: shows individual seed values, enables visual assessment of spread, and is compact enough for single-column.\n\n### Layout\n\n1×4 horizontal subplots (one per signal). `figsize=(5.5, 2.0)`\n\n### Wireframe\n\n```\n  ┌──────────┬──────────┬──────────┬──────────┐\n  │(a) SR    │(b) PPL   │(c) TE    │(d) SE    │\n  │          │          │          │          │\n  │ · · ─ ·  │ · · ─ ·  │ · · ─ ·  │ · · ─ ·  │  ← gen4\n  │ · ─ · ·  │ · ─ · ·  │ · ─ · ·  │ · ─ · ·  │  ← gen2\n  │ · ─ ·    │ · ─ ·    │ · ─ ·    │ · ─ ·    │  ← gen0\n  │   Fraction →        │          │          │\n  └──────────┴──────────┴──────────┴──────────┘\n  Legend: · = individual seed, ─ = mean\n```\n\nEach subplot: X = fraction (6 categories), Y = normalized signal value (z-score or fold-change from 0% mean). Rows of dots at each fraction represent individual seed values; horizontal bar = mean.\n\n### Alternative: Coefficient of Variation Heatmap\n\nIf reviewer prefers quantitative summary over raw points:\n\n```\n  ┌─────────────────────────────────────┐\n  │  Coefficient of Variation (%)       │\n  │        gen0  gen1  gen2  gen3  gen4  │\n  │  0%  │ 1.5│ 1.8│ 2.0│ 2.2│ 2.0│   │\n  │ 10%  │ 1.8│ 2.5│ 3.0│ 3.5│ 3.2│   │\n  │ 25%  │ 2.0│ 3.0│ 4.0│ 4.5│ 4.2│   │\n  │ 50%  │ 2.5│ 5.0│ 7.0│ 7.5│ 6.8│   │\n  │ 75%  │ 3.0│ 6.0│ 8.5│ 9.0│ 8.5│   │\n  │100%  │ 3.5│ 6.5│ 8.0│ 8.0│ 7.5│   │\n  └─────────────────────────────────────┘\n  Colormap: sequential white→deep blue (low CV = consistent)\n```\n\n`figsize=(3.5, 2.0)`, `cmap=\"Blues\"`, `vmin=0, vmax=12`, annotation with `fmt=\".1f\"`.\n\n### Data Requirements\n\n| Field | Source |\n|-------|--------|\n| End-of-gen signal values | Per-seed `signals_{frac}pct_gen{g}_seed{s}.jsonl` |\n| Required: ≥3 seeds per (fraction, generation) | plan_001: 5 seeds (WikiText) |\n| Aggregation | None — plot raw per-seed values |\n\n### Implementation (strip plot version)\n\n```python\nfig, axes = plt.subplots(1, 4, figsize=(5.5, 2.0), sharey=False)\nsignals = [\"stable_rank\", \"perplexity\", \"token_entropy\", \"spectral_entropy\"]\nlabels = [\"(a) SR\", \"(b) PPL\", \"(c) TE\", \"(d) SE\"]\n\nfor ax, sig, label in zip(axes, signals, labels):\n    for i, frac in enumerate(fracs_sorted):\n        seed_vals = df_seeds.loc[frac, sig].values  # shape: (n_seeds,)\n        jitter = np.random.uniform(-0.15, 0.15, len(seed_vals))\n        ax.scatter(i + jitter, seed_vals, s=12, alpha=0.6,\n                   color=FRAC_COLORS[frac], zorder=3)\n        ax.hlines(seed_vals.mean(), i - 0.2, i + 0.2,\n                  color=FRAC_COLORS[frac], linewidth=2, zorder=4)\n    ax.set_xticks(range(len(fracs_sorted)))\n    ax.set_xticklabels([\"0\", \"10\", \"25\", \"50\", \"75\", \"100\"], fontsize=7)\n    ax.set_title(label, loc=\"left\", fontweight=\"bold\", fontsize=9)\n    if sig == \"perplexity\":\n        ax.set_yscale(\"log\")\naxes[0].set_ylabel(\"Signal Value\")\nfig.supxlabel(\"Synthetic Fraction (%)\", fontsize=9)\n```\n\n---\n\n## Figure 4: Per-Layer Collapse Heatmap (Supplementary → Main if space)\n\n### Layout\n\nSingle heatmap. `figsize=(5.5, 3.5)`\n\n### Wireframe\n\n```\n  ┌──────────────────────────────────────┐\n  │  Stable Rank Fold Change (vs 0%)     │\n  │                                      │\n  │  Layer 27 ┃░░░░░░░░▓▓▓▓████████████│\n  │  Layer 24 ┃░░░░░░░░▓▓▓▓████████████│\n  │  ...      ┃                         │\n  │  Layer 14 ┃░░░▓▓▓▓████████████████ │ ← core-mid peak\n  │  Layer 10 ┃░░░▓▓▓▓████████████████ │\n  │  ...      ┃                         │\n  │  Layer 3  ┃░░░░░░░▓▓▓████████████  │\n  │  Layer 0  ┃░░░░░░░░▓▓▓▓███████████ │\n  │           ┗━━━━━━━━━━━━━━━━━━━━━━━━│\n  │            gen0 gen1 gen2 gen3 gen4  │\n  │         100% synthetic fraction     │\n  └──────────────────────────────────────┘\n  Colorbar: fold-change 1× (white) → 10× (dark red)\n```\n\n### Axes\n\n- X: Generation (0–4)\n- Y: Layer index (0–27, bottom to top)\n- Color: Stable rank fold-change vs 0% baseline at same generation\n- Colormap: `\"Reds\"`, vmin=1, vmax=12, log-normalized (`LogNorm`)\n- Annotate layer groups with brackets on right margin: \"embed-adj\", \"lower-mid\", \"core-mid\", \"upper-mid\", \"head-adj\"\n\n### Data Requirements\n\n- Per-layer SVD: `layer_signals_{frac}pct_gen{g}_seed{s}.jsonl` (from plan_006)\n- Fields: `layer_idx`, `stable_rank`, `spectral_entropy`, `sv_ratio_1_2`\n- Two fractions needed: 0% (baseline) and 100% (collapsed). Optional: 50% as secondary panel.\n\n### Implementation\n\n```python\nfrom matplotlib.colors import LogNorm\n\nfig, ax = plt.subplots(figsize=(5.5, 3.5))\n\n# sr_matrix shape: (28 layers, 5 gens), values = fold-change\nsr_fold = sr_100pct / sr_0pct  # element-wise\nim = ax.imshow(sr_fold, aspect=\"auto\", cmap=\"Reds\",\n               norm=LogNorm(vmin=1, vmax=12), origin=\"lower\",\n               interpolation=\"nearest\")\n\nax.set_xticks(range(5))\nax.set_xticklabels([f\"Gen {i}\" for i in range(5)])\nax.set_ylabel(\"Layer Index\")\nax.set_yticks(range(0, 28, 4))\n\n# Layer group annotations\ngroups = [(0, 3, \"Embed\\nadj.\"), (4, 7, \"Lower\\nmid\"),\n          (8, 14, \"Core\\nmid\"), (15, 21, \"Upper\\nmid\"), (22, 27, \"Head\\nadj.\")]\nfor lo, hi, name in groups:\n    ax.annotate(name, xy=(5.3, (lo + hi) / 2), fontsize=6,\n                ha=\"left\", va=\"center\", annotation_clip=False)\n    ax.add_patch(plt.Rectangle((-0.5, lo - 0.5), 5, hi - lo + 1,\n                               fill=False, edgecolor=\"gray\", linewidth=0.4))\n\ncbar = fig.colorbar(im, ax=ax, label=\"SR Fold Change vs Clean\", shrink=0.8)\n```\n\n---\n\n## Figure 5: Within-Generation Early Warning\n\n### Layout\n\nSingle plot or 1×2 (one per scale). `figsize=(5.5, 2.8)`\n\n### Wireframe\n\n```\n  ┌──────────────────────────────────────┐\n  │  Stable Rank Deviation (%) vs 0%     │\n  │                                      │\n  │ 40% ─── ────── ──── ────── 100%      │\n  │ 30% ─── ────── ──── ──               │\n  │ 20% ─── ────── ─             75%     │\n  │ 15%·················threshold·····   │\n  │ 10% ─── ────                  50%    │\n  │  5% ─── ──                    25%    │\n  │  0%                            10%   │\n  │     50  100  200  500  1540          │\n  │            Training Step             │\n  └──────────────────────────────────────┘\n  Horizontal dashed line at 15% = optimal detection threshold\n```\n\n### Axes\n\n- X: Training step (50, 100, 200, 500, 1000, 1540). Log or linear — **linear recommended** (steps are unevenly sampled but conceptually progressive).\n- Y: Signal deviation % = |sig_frac - sig_0pct| / sig_0pct × 100\n- Horizontal dashed line at 15% = optimal threshold from ROC analysis\n\n### Data Requirements\n\n- Within-generation signal values at specific steps\n- Computed as: `deviation = abs(sig[frac, step] - sig[0%, step]) / sig[0%, step] * 100`\n- Primary signal: stable_rank (best early indicator)\n- Need 0% baseline at matched steps\n\n### Implementation\n\n```python\nfig, ax = plt.subplots(figsize=(5.5, 2.8))\nsteps = [50, 100, 200, 500, 1000, 1540]\n\nfor frac in [0.10, 0.25, 0.50, 0.75, 1.00]:\n    devs_mean = [compute_deviation(frac, step, \"stable_rank\").mean() for step in steps]\n    devs_std  = [compute_deviation(frac, step, \"stable_rank\").std() for step in steps]\n    ax.plot(steps, devs_mean, marker=\"o\", color=FRAC_COLORS[frac],\n            label=FRAC_LABELS[frac])\n    ax.fill_between(steps, np.array(devs_mean) - devs_std,\n                     np.array(devs_mean) + devs_std, alpha=0.15,\n                     color=FRAC_COLORS[frac])\n\nax.axhline(15, linestyle=\"--\", color=\"gray\", linewidth=0.8, label=\"Threshold (15%)\")\nax.set_xlabel(\"Training Step\")\nax.set_ylabel(\"Stable Rank Deviation (%)\")\nax.legend(fontsize=7, loc=\"upper left\")\n```\n\n---\n\n## Table 1: Signal Taxonomy (Main Text Table)\n\nNot a figure, but integral to Claim 3. Rendered as LaTeX `\\begin{table}`.\n\n```\n| Signal          | Family   | 0–10% | 10–25% | 25–50% | 50–75% | 75–100% | Best Use         |\n|-----------------|----------|-------|--------|--------|--------|---------|------------------|\n| Stable Rank     | Spectral | ★     | ★★     | ★★★    | ★★★    | sat.    | Early warning    |\n| Spectral Ent.   | Spectral | ·     | ★      | ★★     | ★★★    | sat.    | Moderate sev.    |\n| Perplexity      | Output   | ★     | ★★     | ★★★    | ★★★    | ★★★     | Universal meter  |\n| Token Entropy   | Output   | ·     | ★      | ★★     | ★★★    | ★★★     | Severe collapse  |\n| Gradient Norm   | Gradient | ·     | ·      | ★      | ★★ ↑   | ★ ↓     | NOT recommended  |\n| HellaSwag       | Downstream| ·    | ·      | ·      | ★      | ★       | NOT recommended  |\n```\n\n★ = informative (effect size d > 1). sat. = saturated. ↑↓ = non-monotonic.\n\n---\n\n## Data Pipeline Design\n\n### Step 1: Raw JSONL → Tidy DataFrame\n\n```python\nimport pandas as pd\nimport json\nfrom pathlib import Path\n\ndef load_signals_to_df(base_dir: str) -> pd.DataFrame:\n    \"\"\"Load all signals JSONL files into a single tidy DataFrame.\n\n    Expected file naming: signals_{frac}pct_gen{g}_seed{s}.jsonl\n    Returns DataFrame with columns:\n        fraction, generation, seed, step, stable_rank, spectral_entropy,\n        token_entropy, perplexity, training_loss, gradient_norm,\n        sv_ratio_1_2, top_singular_values\n    \"\"\"\n    records = []\n    for path in Path(base_dir).glob(\"signals_*pct_gen*_seed*.jsonl\"):\n        parts = path.stem.split(\"_\")\n        frac = int(parts[1].replace(\"pct\", \"\")) / 100\n        gen = int(parts[2].replace(\"gen\", \"\"))\n        seed = int(parts[3].replace(\"seed\", \"\"))\n        with open(path) as f:\n            for line in f:\n                r = json.loads(line)\n                r[\"fraction\"] = frac\n                r[\"generation\"] = gen\n                r[\"seed\"] = seed\n                svs = r.get(\"top_singular_values\", [])\n                r[\"sv_ratio_1_2\"] = svs[0] / svs[1] if len(svs) >= 2 and svs[1] > 0 else 0.0\n                records.append(r)\n    df = pd.DataFrame(records)\n    return df\n```\n\n### Step 2: End-of-Generation Aggregation (for Figures 1, 3)\n\n```python\ndef aggregate_end_of_gen(df: pd.DataFrame) -> pd.DataFrame:\n    \"\"\"Extract end-of-generation records, aggregate across seeds.\n\n    Returns DataFrame indexed by (fraction, generation) with columns:\n        {signal}_mean, {signal}_std for each signal.\n    \"\"\"\n    # Take last record per (fraction, generation, seed)\n    eog = df.sort_values(\"step\").groupby([\"fraction\", \"generation\", \"seed\"]).last().reset_index()\n\n    signals = [\"stable_rank\", \"spectral_entropy\", \"token_entropy\", \"perplexity\"]\n    agg_dict = {s: [\"mean\", \"std\"] for s in signals}\n    result = eog.groupby([\"fraction\", \"generation\"]).agg(agg_dict)\n    result.columns = [f\"{s}_{stat}\" for s, stat in result.columns]\n    return result\n```\n\n### Step 3: Clustered Bootstrap for ROC (Figure 2)\n\n```python\ndef clustered_bootstrap_roc(df_eog: pd.DataFrame, signal: str,\n                            threshold: float, n_boot: int = 1000):\n    \"\"\"Compute ROC with clustered bootstrap CIs.\n\n    One cluster = one (fraction, seed) pair.\n    Binary label: fraction >= threshold → positive.\n    \"\"\"\n    clusters = df_eog.groupby([\"fraction\", \"seed\"])[signal].mean().reset_index()\n    clusters[\"label\"] = (clusters[\"fraction\"] >= threshold).astype(int)\n\n    fpr_grid = np.linspace(0, 1, 100)\n    tpr_boots = []\n\n    for _ in range(n_boot):\n        idx = np.random.choice(len(clusters), len(clusters), replace=True)\n        boot = clusters.iloc[idx]\n        if boot[\"label\"].nunique() < 2:\n            continue\n        fpr, tpr, _ = roc_curve(boot[\"label\"], boot[signal])\n        tpr_interp = np.interp(fpr_grid, fpr, tpr)\n        tpr_boots.append(tpr_interp)\n\n    tpr_boots = np.array(tpr_boots)\n    return fpr_grid, np.mean(tpr_boots, axis=0), np.percentile(tpr_boots, [2.5, 97.5], axis=0)\n```\n\n### Step 4: Within-Gen Deviation (Figure 5)\n\n```python\ndef compute_early_warning_deviation(df: pd.DataFrame, signal: str = \"stable_rank\"):\n    \"\"\"Compute signal deviation vs 0% baseline at each step.\n\n    Returns DataFrame with columns: fraction, step, deviation_pct, seed.\n    \"\"\"\n    baseline = df[df[\"fraction\"] == 0.0].groupby([\"generation\", \"step\", \"seed\"])[signal].mean()\n    # Use gen=1 for early warning (first collapsing generation)\n    df_gen1 = df[df[\"generation\"] == 1]\n    bl_gen1 = df_gen1[df_gen1[\"fraction\"] == 0.0].set_index(\"step\")[signal]\n\n    results = []\n    for frac in [0.10, 0.25, 0.50, 0.75, 1.00]:\n        for seed in df_gen1[\"seed\"].unique():\n            frac_data = df_gen1[(df_gen1[\"fraction\"] == frac) & (df_gen1[\"seed\"] == seed)]\n            bl_seed = df_gen1[(df_gen1[\"fraction\"] == 0.0) & (df_gen1[\"seed\"] == seed)]\n            for _, row in frac_data.iterrows():\n                bl_val = bl_seed[bl_seed[\"step\"] == row[\"step\"]][signal].values\n                if len(bl_val) > 0 and bl_val[0] > 0:\n                    dev = abs(row[signal] - bl_val[0]) / bl_val[0] * 100\n                    results.append({\"fraction\": frac, \"step\": row[\"step\"],\n                                    \"seed\": seed, \"deviation_pct\": dev})\n    return pd.DataFrame(results)\n```\n\n### Step 5: Per-Layer Fold Change (Figure 4)\n\n```python\ndef compute_layer_fold_change(base_dir: str):\n    \"\"\"Compute per-layer stable_rank fold change (100% / 0%).\n\n    Returns: np.ndarray of shape (n_layers, n_gens).\n    \"\"\"\n    def load_layer_signals(frac_str):\n        matrix = {}  # {(layer, gen): [values across seeds]}\n        for path in Path(base_dir).glob(f\"layer_signals_{frac_str}_gen*_seed*.jsonl\"):\n            gen = int(path.stem.split(\"_\")[3].replace(\"gen\", \"\"))\n            with open(path) as f:\n                for line in f:\n                    r = json.loads(line)\n                    key = (r[\"layer_idx\"], gen)\n                    matrix.setdefault(key, []).append(r[\"stable_rank\"])\n        return {k: np.mean(v) for k, v in matrix.items()}\n\n    sr_0   = load_layer_signals(\"0pct\")\n    sr_100 = load_layer_signals(\"100pct\")\n\n    n_layers, n_gens = 28, 5\n    fold = np.ones((n_layers, n_gens))\n    for layer in range(n_layers):\n        for gen in range(n_gens):\n            bl = sr_0.get((layer, gen), 1)\n            col = sr_100.get((layer, gen), 1)\n            fold[layer, gen] = col / bl if bl > 0 else 1\n    return fold\n```\n\n---\n\n## Figure Priority for Main Text\n\n| Priority | Figure | Supports | Space |\n|----------|--------|----------|-------|\n| 1 (必须) | Fig 1: Severity Curves | Claim 1 | ~1/3 page |\n| 2 (必须) | Fig 2: ROC Curves | Claim 2 + reviewer concern | ~1/4 page |\n| 3 (必须) | Fig 3: Seed Variance | Reviewer concern (reproducibility) | ~1/6 page |\n| 4 (强推) | Fig 4: Layer Heatmap | Claim 3 (depth) | ~1/3 page |\n| 5 (强推) | Fig 5: Early Warning | Claim 2 (practitioner value) | ~1/4 page |\n| — | Table 1: Signal Taxonomy | Claim 3 (summary) | ~1/6 page |\n\nTotal main-text figures: 5 figures + 1 table ≈ 1.5 pages of visual content. NeurIPS allows 8 pages + unlimited appendix; this is a reasonable allocation for an analysis paper.\n\n### Appendix Figures\n\n- Fig A1: Severity curves with normalized Y-axis (% change from gen0)\n- Fig A2: ROC curves at ≥25% and ≥50% thresholds\n- Fig A3: QLoRA vs Full FT comparison (Table 5 as bar chart)\n- Fig A4: Self-recovery PPL trajectories (zoom on 25%/50%/75%)\n- Fig A5: AUC bar chart by signal × training progress %\n- Fig A6: Per-layer spectral_entropy and sv_ratio heatmaps\n",
      "numLines": 673,
      "startLine": 1,
      "totalLines": 673
    }
  },
  "sourceToolAssistantUUID": "1e7e61ef-9192-4569-b5ce-91881efaf975",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 20 · 2026-05-14T22:42:09.485Z_

<details open><summary>🔧 Tool call — Read · `toolu_017CRiPnTNntFzQ4ChZKPEdP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/annotated_bibliography.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e90c5c7d-bf69-4da0-b453-ea2a91c881f2",
  "isSidechain": false,
  "requestId": "req_011Cb3GWBP8qSjoabQ1rozXo",
  "type": "assistant",
  "uuid": "8d32e62b-0c70-4fa1-823d-829af339ad12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5tctSX7vDf1AdBwGUC2Hr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 22763,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 367,
          "cache_read_input_tokens": 22763,
          "cache_creation_input_tokens": 240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 240
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

_source line 21_

```json
{
  "type": "last-prompt",
  "leafUuid": "80214af7-5275-48da-843c-245e7129bacf",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Check literature and paper preparation status",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12"
}
```

---

### Assistant

_source line 23 · 2026-05-14T22:42:39.997Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now compile the status report based on what I've read.

1. `literature_map.yaml`: 34 papers total. Categories: direct_competitor (2), related (7), foundation (3), complementary (22). Let me recount by looking at the `relation` field values.

Actually the summary section says:
- total_papers: 34
- direct_competitors: 2 (SIGMA, Kalinowski)
- coverage breakdown: model_collapse_theory: 14, data_contamination: 5, spectral_methods: 8, training_dynamics: 4, data_quality: 3


2. `references.bib`: Now I'm counting the bibliography entries and I can see there are at least 16 entries starting from shumailov2024curse through to d, which appears to be cut off mid-entry.

Continuing through the rest of the file, I'm seeing entries like athathri2024synthid, kirchenbauer2023watermark, mitchell2023detectgpt, and others, bringing the total to 34 entries. But there's a discrepancy—the file header claims 33 papers, so I need to recount to verify the actual number. Let me recount the actual @ entries.

Looking at the file: I count 34 entries across six sections. But the header says 33, so there's a small discrepancy there.

Now I'm checking the related work outline. It has 20 papers cited across four sections, which matches what the header claims—it was based on an earlier version of the literature map with 19 papers plus one supplementary addition. The current literature map has grown to 34, but the outline still covers the 20 it needs.

For the figure design document, I see 5 main figures plus a table and 6 appendix figures with complete specifications.

The annotated bibliography lists 33 papers across 6 categories with role tags and annotations for each.

There's a small inconsistency across the files: the literature map shows 34 papers, but the references file header says 33 even though it actually contains 34 entries. The annotated bibliography also says 33. This might be a stale comment in one of the headers, or there's a one-paper discrepancy I need to track down. The literature_map has 34 papers total, the bibliography file contains 34 entries despite its header claiming 33, and the related_work_outline meets the requirement with 20 citations. There's a discrepancy in the annotated bibliography where the header says 33 but the actual count is closer to 34.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80214af7-5275-48da-843c-245e7129bacf",
  "isSidechain": false,
  "requestId": "req_011Cb3GWacPCYDcpaChRTvvy",
  "type": "assistant",
  "uuid": "fb83c72d-7564-4ff1-8ec1-fd9d04bc3ae1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9nSqyGvjwwfxDx4x8uneh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39016,
      "cache_read_input_tokens": 23003,
      "output_tokens": 1898,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39016,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1898,
          "cache_read_input_tokens": 23003,
          "cache_creation_input_tokens": 39016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39016
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

_source line 24 · 2026-05-14T22:42:47.409Z_

| 项目 | 状态 | 详情 |
|------|------|------|
| `literature_map.yaml` | 34 篇 | direct_competitor: 2, related: 7, foundation: 3, complementary: 22。覆盖 5 个子领域（theory 14, contamination 5, spectral 8, dynamics 4, data quality 3） |
| `artifacts/references.bib` | 34 条 BibTeX | 文件头注释写 33 篇（过期），实际 `@` 条目 34 个，与 literature_map 一致 |
| `docs/related_work_outline.md` | 20 篇引用 | 4 个分节（A–D），20 篇 ≥ 20 ✓。但基于旧版 literature_map（19+1），未覆盖后续新增的 14 篇 |
| `artifacts/figure_design.md` | 完整 | 5 主图 + 1 表 + 6 附录图，含 wireframe、实现代码、色板、数据管线（5 步），统计方法（clustered bootstrap） |
| `artifacts/annotated_bibliography.md` | 33 篇（头注） | 6 分类，每篇标注 role（foundation/background/method component/complementary/direct competitor），实际条目约 34 |

**问题**：`references.bib` 和 `annotated_bibliography.md` 头部计数均写 33，实际为 34，需同步更新。`related_work_outline.md` 滞后于 literature_map 14 篇（从 20→34 的扩充未反映到 outline）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb83c72d-7564-4ff1-8ec1-fd9d04bc3ae1",
  "isSidechain": false,
  "requestId": "req_011Cb3GWacPCYDcpaChRTvvy",
  "type": "assistant",
  "uuid": "5c906783-780c-49c0-90fb-f51940bfcacf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9nSqyGvjwwfxDx4x8uneh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39016,
      "cache_read_input_tokens": 23003,
      "output_tokens": 1898,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39016,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1898,
          "cache_read_input_tokens": 23003,
          "cache_creation_input_tokens": 39016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39016
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

_source line 25_

```json
{
  "type": "last-prompt",
  "leafUuid": "5c906783-780c-49c0-90fb-f51940bfcacf",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Check literature and paper preparation status",
  "sessionId": "94a01d86-ec14-4786-834e-1e6883edfb12"
}
```

---
