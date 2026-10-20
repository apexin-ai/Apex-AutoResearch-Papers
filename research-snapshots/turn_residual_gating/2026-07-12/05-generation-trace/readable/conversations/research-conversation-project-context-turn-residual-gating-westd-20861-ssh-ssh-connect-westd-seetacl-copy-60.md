# Research conversation: <project_context> # 项目: turn_residual_gating ## 运行环境 - 服务器名: westd-20861 - SSH 连接命令: ssh connect.westd.seetacloud.com # 

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 103
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-1/79c91556-39c7-41c3-af87-6b5fcf7be31a.jsonl`
- **Structured JSON:** [`6a690b6bc2a6580a5143.json`](../../sessions/6a/6a690b6bc2a6580a5143.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T04:50:31.020Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T04:50:31.020Z",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "content": "&lt;project_context>\n# 项目: turn_residual_gating\n\n## 运行环境\n- 服务器名: westd-20861\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/turn_residual_gating\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：文献图谱填充 (literature_map.yaml)\n\n### 目标\nliterature_map.yaml 当前为空。参考论文 references.bib 和 paper_framing.md 中的 key references，添加 ≥5 篇核心相关论文。\n\n### 步骤\n\n1. 读取 paper_framing.md 了解核心研究方向和关键引用：\n   `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper_framing.md`\n\n2. 读取 references.bib 了解已引用的论文列表：\n   `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib`\n\n3. 从以下 4 个方向各选至少 1 篇核心论文，WebSearch 获取 Semantic Scholar paper ID 或 arXiv ID：\n\n   **a. Exposure bias 相关** — 如 Bengio et al. 2015 (scheduled sampling), Ranzato et al. 2016, He et al. 2019\n   **b. GAR/grounding/attention 相关** — 如 Dongre et al. 2026 (goal attention ratio)\n   **c. Multi-turn dialogue 注意力机制** — 如 Liu et al. 2023 (lost in the middle)\n   **d. Scheduled sampling / curriculum learning** — 如 Lamb et al. 2016, Leblond et al. 2018\n\n4. 用 WebSearch 确认每篇论文的：\n   - 完整 title, authors, year, venue\n   - Semantic Scholar paper ID 或 arXiv ID\n   - 与本项目的关系 (role: direct-competitor / method-component / theoretical-foundation / benchmark)\n\n5. 将每篇论文通过合适的方式添加到 literature_map.yaml\n\n### 产出\n报告：添加了哪些论文，每篇的 role 和与项目的关联说明\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T04:50:31.023Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T04:50:31.023Z",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

## Round 1

101 recorded events

### User

_source line 3 · 2026-05-22T04:50:31.061Z_

&lt;project_context>
# 项目: turn_residual_gating

## 运行环境
- 服务器名: westd-20861
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/turn_residual_gating


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：文献图谱填充 (literature_map.yaml)

### 目标
literature_map.yaml 当前为空。参考论文 references.bib 和 paper_framing.md 中的 key references，添加 ≥5 篇核心相关论文。

### 步骤

1. 读取 paper_framing.md 了解核心研究方向和关键引用：
   `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper_framing.md`

2. 读取 references.bib 了解已引用的论文列表：
   `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib`

3. 从以下 4 个方向各选至少 1 篇核心论文，WebSearch 获取 Semantic Scholar paper ID 或 arXiv ID：

   **a. Exposure bias 相关** — 如 Bengio et al. 2015 (scheduled sampling), Ranzato et al. 2016, He et al. 2019
   **b. GAR/grounding/attention 相关** — 如 Dongre et al. 2026 (goal attention ratio)
   **c. Multi-turn dialogue 注意力机制** — 如 Liu et al. 2023 (lost in the middle)
   **d. Scheduled sampling / curriculum learning** — 如 Lamb et al. 2016, Leblond et al. 2018

4. 用 WebSearch 确认每篇论文的：
   - 完整 title, authors, year, venue
   - Semantic Scholar paper ID 或 arXiv ID
   - 与本项目的关系 (role: direct-competitor / method-component / theoretical-foundation / benchmark)

5. 将每篇论文通过合适的方式添加到 literature_map.yaml

### 产出
报告：添加了哪些论文，每篇的 role 和与项目的关联说明


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "8697c930-cf2e-4d0a-a4fe-4c5ff53013cc",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T04:50:31.061Z_

```json
{
  "parentUuid": "8697c930-cf2e-4d0a-a4fe-4c5ff53013cc",
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
  "uuid": "43e2b084-cf03-4a5c-b1bf-a3360bb19301",
  "timestamp": "2026-05-22T04:50:31.061Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T04:50:31.061Z_

```json
{
  "parentUuid": "43e2b084-cf03-4a5c-b1bf-a3360bb19301",
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
  "uuid": "936f8baf-8a3b-43aa-ac3c-e3f54c4bf159",
  "timestamp": "2026-05-22T04:50:31.061Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T04:50:31.061Z_

```json
{
  "parentUuid": "936f8baf-8a3b-43aa-ac3c-e3f54c4bf159",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b8474d72-e0fc-4420-901e-628c36f7dd67",
  "timestamp": "2026-05-22T04:50:31.061Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Fill literature map with core related papers",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Assistant

_source line 8 · 2026-05-22T04:50:40.852Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the paper_framing.md and references.bib to understand the project's research direction and existing citations, then I'll fill in the literature_map.yaml.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8474d72-e0fc-4420-901e-628c36f7dd67",
  "isSidechain": false,
  "requestId": "req_011CbH1GBbhYPQeTE9RQr6Lv",
  "type": "assistant",
  "uuid": "5d1b89d0-4ed2-4f12-aa64-10777bdcf612",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmWWfxM4eAa5ZC9jYVbr6P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12874,
      "cache_read_input_tokens": 11841,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12874,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 307,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12874
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

_source line 9 · 2026-05-22T04:50:41.285Z_

I'll read the paper framing and references to understand the research direction, then populate the literature map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d1b89d0-4ed2-4f12-aa64-10777bdcf612",
  "isSidechain": false,
  "requestId": "req_011CbH1GBbhYPQeTE9RQr6Lv",
  "type": "assistant",
  "uuid": "315c4dda-dee1-4305-a8cf-966ef0db5a53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmWWfxM4eAa5ZC9jYVbr6P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12874,
      "cache_read_input_tokens": 11841,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12874,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 307,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12874
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

_source line 10 · 2026-05-22T04:50:42.413Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Lqj11sZEYjZX54tUkmhw5D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "315c4dda-dee1-4305-a8cf-966ef0db5a53",
  "isSidechain": false,
  "requestId": "req_011CbH1GBbhYPQeTE9RQr6Lv",
  "type": "assistant",
  "uuid": "42b334b3-e951-42c3-bcaf-ac6735e96d8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmWWfxM4eAa5ZC9jYVbr6P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12874,
      "cache_read_input_tokens": 11841,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12874,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 307,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12874
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

_source line 11 · 2026-05-22T04:50:42.431Z_

<details><summary>↩ Tool result · `toolu_01Lqj11sZEYjZX54tUkmhw5D`</summary>

```text
1	# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering
2	
3	> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（30x 断层的定量证据）。这个 insight 为 auxiliary attention loss 在 teacher-forcing 下的 exposure bias 脆弱性提供首个实证刻画。
4	> Novelty 排序: (1) exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画 (30x gap) > (2) PCGrad 因果排除梯度方向冲突 + "观察→假设→排除→指向真因" 完整因果链 (D028) > (3) principled intervention + systematic ablation 的 negative result
5	> **⚠️ Dream review D024: "Cannot" overclaims, novelty "first measurement" 过高, 缺 gradient surgery baseline (PCGrad). 标题改 "Fails to", novelty 降级 "first empirical characterization"**
6	> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)
7	> 最后更新: 2026-05-20 (M017 修正: PPL -46% 为跨协议伪影, IID PPL 无差异; selective dissociation 撤回; D033 跨变体确认)
8	> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）
9	
10	---
11	
12	## 1. Title Candidates
13	
14	- **T1 (推荐)**: Why Lightweight Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis
15	- **T2**: The Distribution Shift Trap: Why Training-Time Attention Steering Fails at Inference
16	- **T3**: Residual Gating Fails to Recover Goal Attention in Multi-Turn Dialogue
17	- **T4**: Lightweight Gating Struggles with Multi-Turn Attention Degradation: Evidence from Exposure Bias
18	
19	推荐 T1: "Fails to Fix" 替代 "Cannot Fix"（审稿共识：证据仅支持 tested conditions 下的失败，非绝对否定）。"Lightweight Gating" 覆盖标量+uniform gate。
20	
21	---
22	
23	## 2. Story Arc
24	
25	Multi-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Attention Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), and this improvement transfers perfectly when evaluated on same-distribution text at inference (GAR-ours = 0.49). However, on model-generated text, GAR-ours collapses to 0.016—a 30× gap driven by text distribution shift. Our central finding is that attention patterns learned under teacher-forced contexts (gold text) do not generalize to autoregressive generation contexts (model-generated text), the classic exposure bias phenomenon. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Notably, this 30× gap is specific to GAR-ours (last-token attention to goals); GAR-Dongre (all-token attention) shows uniformly low values regardless of text distribution, revealing that exposure bias selectively disrupts summary-position attention patterns. Combined with Dongre et al.'s independent failure of goal re-injection, our results provide the first empirical characterization of how text distribution shift (exposure bias) selectively destroys attention patterns learned through auxiliary losses, and identify the specific mechanisms through which this vulnerability manifests.
26	
27	---
28	
29	## 3. Core Claims
30	
31	| # | Claim | 支撑 | 状态 |
32	|---|-------|------|------|
33	| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | ✅ 已验证 |
34	| C2 | Residual gating 训练时在 same-distribution text 上有效优化 GAR-ours (0.48→0.49 泛化成功)，但在 model-generated text 上完全失败 (GAR-ours=0.016, 30x text distribution shift gap)。GAR-Dongre 在两种分布上均低（~0.01-0.016），无 gap——说明分布偏移选择性影响 summary-position attention pattern。 | v7 训练曲线 + 4-way eval + v7 直接 eval + Reviewer 独立验证 (D024) | ✅ 已验证（precision upgrade） |
35	| C3 | 失败机制的因果分析: (1) Distribution shift 是主因（D028 PCGrad 因果排除梯度方向冲突）; (2) NTP 幅度主导 gate 学习 → NF1 反向 turn conditioning; (3) NF3 gate 干预强度不足 2-7%。PCGrad ablation: 消除方向冲突后 cos_sim 围绕 0 震荡(range -0.151 to +0.091)，但 L_GAR 坍塌轨迹不变且无延迟 → 方向冲突非因果因素。**推理端确认（IID same-protocol）**: v9 GAR-ours=0.0151 vs v7=0.0157 (差<0.1pp), **v9 IID PPL=2.780 vs v7=2.784 (差0.004，无改善)**——PCGrad 消除方向冲突后所有可观测指标均 ≈ v7，方向冲突因 NTP 幅度主导而完全 inconsequential | D014 gate-profile + 梯度冲突量化 + **D028 PCGrad 因果排除** + v9 推理 eval + **M017 PPL 修正** | ✅ **End-to-end 完成**: 训练端 + 推理端均确认梯度方向冲突对 GAR 和 PPL 均无因果影响 |
36	| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。IID: GAR 差异<0.6pp, PPL 均 ~2.78。**Model-gen (D033): v9 PCGrad=0.0151, UG=0.0149, LoRA-only=0.0245 均接近 baseline 0.0122——30x gap 在所有训练变体上普遍存在，排除 gating mechanism / turn-conditioning / gradient conflict 作为因果因素** | D021 四路 eval + D033 model-gen eval | ✅ **双重验证**: IID (D021) + model-gen (D033)。model-gen regime 进一步确认 gating 零增量且 GAR collapse 是训练-推理分布偏移的普遍现象 |
37	| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Phase 1 ✅ (GAR decay 90.1%, D042), Phase 2 训练中 | ⏳ Phase 1 done, Phase 2 running |
38	
39	---
40	
41	## 4. Negative Findings (NF)
42	
43	| # | Finding | 证据 | 叙事角色 |
44	|---|---------|------|----------|
45	| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |
46	| NF2 | 30x text distribution shift gap (GAR-ours): ultrachat 文本 0.49 vs 模型生成文本 0.016。Same-distribution 泛化成功（训练 0.48 → ultrachat eval 0.49），cross-distribution 泛化失败。**D033 跨变体确认**: v9 PCGrad (0.0151), UG (0.0149), LoRA-only (0.0245) model-gen GAR 均接近 baseline (0.0122)——gap 独立于训练策略，是 exposure bias 的普遍表现。GAR-Dongre 在两种分布上均低（~0.01-0.019），无 gap——分布偏移选择性影响 summary-position (last token) attention pattern | D015 + 4-way eval + v7 direct eval + D024 + **D033 cross-variant model-gen** | 核心 negative finding。精确定位为 TEXT DISTRIBUTION SHIFT（exposure bias）。D033 确认跨所有训练变体的普遍性。 |
47	| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |
48	| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |
49	
50	---
51	
52	## 5. Key Selling Points
53	
54	**SP1 (核心卖点): Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画。** 30x training-inference GAR-ours gap 提供了 teacher-forcing distribution shift 如何摧毁 auxiliary attention loss 泛化性的实证证据。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。虽然 exposure bias 概念本身已知 (Bengio et al. 2015)，且 sequence generation 中有量化先例 (Ranzato et al. 2016, Wiseman & Rush 2016)，但此前无人刻画其对 auxiliary attention loss 的具体影响。我们的 30x gap 测量展示了这种脆弱性在 attention steering 场景下的严重程度。**注意：(1) claim scope 严格限于 lightweight residual gating + GAR auxiliary loss 的实测范围，不泛化到所有 attention steering 方法。(2) 30x gap 在 GAR-ours（last token only, summary-position attention）上测得（IID 0.50 vs model-gen 0.016）；GAR-Dongre（all response tokens）在两种分布上均低（~0.01-0.019），无 gap——表明 exposure bias 选择性影响 summary-position attention pattern，这一差异本身有分析价值。**
55	
56	**SP2: NTP-GAR 梯度动力学 + PCGrad 因果排除（gradient conflict is inconsequential）。** 观察到 67-79% 的层 NTP-GAR 梯度方向冲突（cos_sim<0）+ NTP 幅度 3-15x 压制 GAR（mag_ratio 7.5→14.7x）。**PCGrad 消融（D028）因果排除方向冲突**：投影后 cos_sim 围绕 0 震荡（range -0.151 to +0.091），L_GAR 坍塌轨迹不变。**推理端确认（IID same-protocol）**: v9 IID PPL = 2.780 vs v7 = 2.784（差 0.004，无改善）; v9 GAR-ours = 0.0151 vs v7 = 0.0157（差 <0.1pp）——**PCGrad 消除方向冲突后所有可观测指标均无变化**（GAR、PPL、NTP 均 ≈ v7）。方向冲突虽然可测量存在于 v7 中，但对训练和推理结果无任何因果影响——10-40× NTP 幅度主导使方向冲突完全无关紧要（inconsequential）。**⚠️ M017: 此前 "PPL -46%" 和 "selective dissociation" 论述为跨协议对比伪影（model-gen PPL 1.50 vs IID PPL 2.78），已撤回。** **精确 claim scope**: gradient direction conflict is **neither necessary nor sufficient** for the 30x GAR gap; exposure bias alone is sufficient。NOT necessary: 移除冲突→gap仍在; NOT sufficient: v7有冲突但L_GAR训练时收敛; Exposure bias is sufficient: 训练≠推理分布→GAR泛化失败。**Gate 行为额外 insight**: v9 gate dynamic range 比 v7 更宽 (L15 range 0.33 vs v7 0.21)——PCGrad 给 gate 更大自由度，但 gate 用该自由度更激进地优化 NTP 而非 GAR，说明优化景观固有偏好语言建模目标。
57	
58	**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融严格隔离贡献: TG (learned gate + GAR loss) / UG (uniform gate + GAR loss) / LoRA-only (gate=1.0 fixed + GAR loss, 无 gating 机制) / Base。注意：三个 fine-tuned 变体均使用 GAR loss，消融测试的是 gating 机制的增量贡献，而非 GAR loss 本身的效果。
59	
60	**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。
61	
62	**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。
63	
64	---
65	
66	## 6. Anticipated Reviewer Concerns
67	
68	| # | 严重度 | 预期质疑 | 回应策略 |
69	|---|--------|----------|----------|
70	| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |
71	| W2 | **严重** | "你只是没调对参数" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |
72	| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |
73	| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |
74	| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（30x 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |
75	| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |
76	| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 "we extend Dongre"，而是 "Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations"。核心叙事是 mechanism discovery，非 follow-up work。 |
77	| W6 | **严重** | 引用不足（Dream review: 11篇远不够）| 目标 25-30 篇。必须覆盖: attention sinks (Xiao et al. 2024), Found-in-the-Middle (Ko et al. 2024), gated attention (Qiu et al. 2025), transformer circuits (Elhage et al. 2021), FlexiDepth (Luo et al. 2025), multi-turn eval (MT-Bench-101, MultiChallenge), exposure bias mitigation (Professor Forcing, SEARNN) 等。Paper Agent 写作时负责扩充。|
78	| W7 | **严重** | 单 seed 无方差估计 | 所有实验 seed=42，TG-LoRA 差异 ±0.001 在噪声层。回应: held-out eval 50 conversations 提供 paired bootstrap CI，若 CI 包含 0 则统计支持 "zero benefit"。必要时追加 2 个 seed 的训练。|
79	| W8 | **中等** | 缺 exposure-bias mitigation 实验 | 测试 scheduled sampling / model-generated context 训练能否缩小 30x gap。加入 experiment_plan (P1)。如果实验表明 mitigation 确实缩小 gap，论文从 "negative result" 升级为 "negative result + constructive direction"。|
80	| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 exposure bias 的定量测量（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |
81	| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 "we extend Dongre"，而是 "Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations"。核心叙事是 mechanism discovery，非 follow-up work。 |
82	| R3 | 低 | 30x gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |
83	| R4 | ~~低~~ **已核实** | Code-paper 公式语义相反 | **已确认不一致（plan_017 DONE）**。代码正确实现 ReZero-style: `x_{l+1} = x_l + g_l · f_l(x_l)`（gate 缩放子层输出，g→0=层 no-op）。Dream paper.tex 错误写为 `x_{l+1} = g_l · x_l + f_l(x_l)`（gate 缩放残差流，g→0=破坏 skip connection）。**实验数据不受影响**（所有实验用同一份代码）。**Paper Agent 写作时必须**: (1) Method section 用正确公式 `x + g·f(x)`; (2) 机制叙事修正: g→0 = 子层输出被抑制（层变 no-op），NTP 推 g→1 是为保留层计算能力，不是保留 skip connection; (3) NF3 "gate attenuation 2-7%" 指子层贡献缩放，表述正确但需明确。|
84	
85	---
86	
87	## 7. Dongre et al. 关系定位
88	
89	| 维度 | Dongre et al. | 本文 |
90	|------|---------------|------|
91	| 核心问题 | "发生了什么" + "为什么" | "怎么干预" + "为什么干预失败" |
92	| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |
93	| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 30x 泛化 gap + turn conditioning 反转 |
94	| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |
95	| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |
96	
97	**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。
98	
99	共同推论: 两种独立干预路线均失败 → lightweight residual gating with auxiliary attention loss 在 teacher-forcing 下面临严重泛化障碍 → 需要 inference-time 干预或 exposure bias mitigation。（注意：scope 限于 lightweight gating，不泛化到所有 attention steering 方法。）
100	
101	---
102	
103	## 8. GAR 定义策略
104	
105	| 用途 | 定义 | Goal tokens | Response tokens | 理由 |
106	|------|------|------------|----------------|------|
107	| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |
108	| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |
109	| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |
110	
111	**D024 精确化**: GAR-ours 在 same-distribution (ultrachat) text 上 ≈0.49（泛化成功），在 model-generated text 上 ≈0.016（30x gap）。GAR-Dongre 在两种分布上均低 (~0.01-0.016, 无 gap)。30x gap 是 text distribution shift 现象，特定于 summary-position attention (GAR-ours)。
112	
113	---
114	
115	## 9. 论文结构草案
116	
117	1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示
118	2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表
119	3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention
120	4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据
121	5. **Method**: ThreadGate 架构（⚠️ 非简单标量 gate：per-layer 2 层 MLP + turn embedding，接收 hidden_state + turn_distance/turn_index，输出 per-token per-layer sigmoid gate 值。公式 g_l = σ(W_2·ReLU(W_1·[proj(x_l); emb(t_d, t_i)] + b_1) + b_2)。Uniform Gate = 同架构但用 constant_vector 替代 turn embedding，仍然 per-layer content-dependent）+ MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置
122	6. **Experiments**: 四路消融 (TG/UG/LoRA-only/Base) with GAR + PPL dual metrics + 跨模型验证 (Llama-3.1-8B)
123	7. **Analysis**: §6.1 NTP-GAR 梯度冲突观察 → §6.2 Gate turn conditioning (Wilcoxon) → §6.3 **PCGrad 因果排除方向冲突** → §6.4 Distribution shift (exposure bias) 作为主因 → §6.5 attention 可视化 + 训练动力学
124	8. **Discussion**: 为什么 lightweight residual gating 不够 → exposure bias 对 auxiliary attention loss 的具体影响机制 → 潜在解决方向 (inference-time intervention / exposure bias mitigation for auxiliary losses / decoupled pathway / GAR-aware decoding) → **scope 声明: claim 限于 lightweight gating，不泛化到所有 attention steering**
125	9. **Conclusion**: negative result 总结 + 对社区的 actionable 建议
126	
127	### 贡献列表（按 novelty 排序）
128	
129	1. **Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画**: 实证展示 teacher-forcing distribution shift 如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（30x training-inference GAR-ours gap），为 teacher-forcing 下的 attention steering 方法提供具体风险标杆
130	2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）
131	3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline
132	4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性
133	
134	---
135	
136	## 10. 竞争力评估
137	
138	### Dream Review 结果 (2026-05-19, dream_20260519T135115)
139	- **Best case**: 3.0 (Weak Reject / Findings-level)。主要扣分: claim 过度泛化 (W1), 引用不足 (W6), 单 seed (W7)。
140	- **Median case**: 3.0 (Weak Reject)。同上 + distribution shift insight incremental (W5)。
141	- **Worst case**: 未完成 review（crash），但 imagined experiments 显示最坏情况下 Llama-3 不复现 dramatic pattern。
142	
143	### 修正后预期
144	- **收窄 claim + 扩充引用 + code 验证后**: best 预期 3.5 (Weak Accept / Borderline Conference)。移除两个 Major weakness (W1 overclaim + W6 thin refs)。
145	- **加 bootstrap CI + Llama-3 数据后**: median 预期 3.0-3.5。
146	- **冲 Main 条件**: 上述修正 + exposure-bias mitigation 实验 (W8) + 25-30 references。
147	- **核心差异化**: 不是 "gating 失败了"（弱），而是 "exposure bias 在 auxiliary attention loss 上的首个定量测量 + 失败机制 taxonomy"。
148	- **关键风险**: W5（exposure bias 已知）需要精确定位增量；W7（单 seed）需 bootstrap CI 或追加 seed。
149	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42b334b3-e951-42c3-bcaf-ac6735e96d8c",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "7b00a40e-6fed-4770-914c-235b0e2e3796",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper_framing.md",
      "content": "# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering\n\n> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（30x 断层的定量证据）。这个 insight 为 auxiliary attention loss 在 teacher-forcing 下的 exposure bias 脆弱性提供首个实证刻画。\n> Novelty 排序: (1) exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画 (30x gap) > (2) PCGrad 因果排除梯度方向冲突 + \"观察→假设→排除→指向真因\" 完整因果链 (D028) > (3) principled intervention + systematic ablation 的 negative result\n> **⚠️ Dream review D024: \"Cannot\" overclaims, novelty \"first measurement\" 过高, 缺 gradient surgery baseline (PCGrad). 标题改 \"Fails to\", novelty 降级 \"first empirical characterization\"**\n> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)\n> 最后更新: 2026-05-20 (M017 修正: PPL -46% 为跨协议伪影, IID PPL 无差异; selective dissociation 撤回; D033 跨变体确认)\n> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）\n\n---\n\n## 1. Title Candidates\n\n- **T1 (推荐)**: Why Lightweight Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\n- **T2**: The Distribution Shift Trap: Why Training-Time Attention Steering Fails at Inference\n- **T3**: Residual Gating Fails to Recover Goal Attention in Multi-Turn Dialogue\n- **T4**: Lightweight Gating Struggles with Multi-Turn Attention Degradation: Evidence from Exposure Bias\n\n推荐 T1: \"Fails to Fix\" 替代 \"Cannot Fix\"（审稿共识：证据仅支持 tested conditions 下的失败，非绝对否定）。\"Lightweight Gating\" 覆盖标量+uniform gate。\n\n---\n\n## 2. Story Arc\n\nMulti-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Attention Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), and this improvement transfers perfectly when evaluated on same-distribution text at inference (GAR-ours = 0.49). However, on model-generated text, GAR-ours collapses to 0.016—a 30× gap driven by text distribution shift. Our central finding is that attention patterns learned under teacher-forced contexts (gold text) do not generalize to autoregressive generation contexts (model-generated text), the classic exposure bias phenomenon. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Notably, this 30× gap is specific to GAR-ours (last-token attention to goals); GAR-Dongre (all-token attention) shows uniformly low values regardless of text distribution, revealing that exposure bias selectively disrupts summary-position attention patterns. Combined with Dongre et al.'s independent failure of goal re-injection, our results provide the first empirical characterization of how text distribution shift (exposure bias) selectively destroys attention patterns learned through auxiliary losses, and identify the specific mechanisms through which this vulnerability manifests.\n\n---\n\n## 3. Core Claims\n\n| # | Claim | 支撑 | 状态 |\n|---|-------|------|------|\n| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | ✅ 已验证 |\n| C2 | Residual gating 训练时在 same-distribution text 上有效优化 GAR-ours (0.48→0.49 泛化成功)，但在 model-generated text 上完全失败 (GAR-ours=0.016, 30x text distribution shift gap)。GAR-Dongre 在两种分布上均低（~0.01-0.016），无 gap——说明分布偏移选择性影响 summary-position attention pattern。 | v7 训练曲线 + 4-way eval + v7 直接 eval + Reviewer 独立验证 (D024) | ✅ 已验证（precision upgrade） |\n| C3 | 失败机制的因果分析: (1) Distribution shift 是主因（D028 PCGrad 因果排除梯度方向冲突）; (2) NTP 幅度主导 gate 学习 → NF1 反向 turn conditioning; (3) NF3 gate 干预强度不足 2-7%。PCGrad ablation: 消除方向冲突后 cos_sim 围绕 0 震荡(range -0.151 to +0.091)，但 L_GAR 坍塌轨迹不变且无延迟 → 方向冲突非因果因素。**推理端确认（IID same-protocol）**: v9 GAR-ours=0.0151 vs v7=0.0157 (差<0.1pp), **v9 IID PPL=2.780 vs v7=2.784 (差0.004，无改善)**——PCGrad 消除方向冲突后所有可观测指标均 ≈ v7，方向冲突因 NTP 幅度主导而完全 inconsequential | D014 gate-profile + 梯度冲突量化 + **D028 PCGrad 因果排除** + v9 推理 eval + **M017 PPL 修正** | ✅ **End-to-end 完成**: 训练端 + 推理端均确认梯度方向冲突对 GAR 和 PPL 均无因果影响 |\n| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。IID: GAR 差异<0.6pp, PPL 均 ~2.78。**Model-gen (D033): v9 PCGrad=0.0151, UG=0.0149, LoRA-only=0.0245 均接近 baseline 0.0122——30x gap 在所有训练变体上普遍存在，排除 gating mechanism / turn-conditioning / gradient conflict 作为因果因素** | D021 四路 eval + D033 model-gen eval | ✅ **双重验证**: IID (D021) + model-gen (D033)。model-gen regime 进一步确认 gating 零增量且 GAR collapse 是训练-推理分布偏移的普遍现象 |\n| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Phase 1 ✅ (GAR decay 90.1%, D042), Phase 2 训练中 | ⏳ Phase 1 done, Phase 2 running |\n\n---\n\n## 4. Negative Findings (NF)\n\n| # | Finding | 证据 | 叙事角色 |\n|---|---------|------|----------|\n| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |\n| NF2 | 30x text distribution shift gap (GAR-ours): ultrachat 文本 0.49 vs 模型生成文本 0.016。Same-distribution 泛化成功（训练 0.48 → ultrachat eval 0.49），cross-distribution 泛化失败。**D033 跨变体确认**: v9 PCGrad (0.0151), UG (0.0149), LoRA-only (0.0245) model-gen GAR 均接近 baseline (0.0122)——gap 独立于训练策略，是 exposure bias 的普遍表现。GAR-Dongre 在两种分布上均低（~0.01-0.019），无 gap——分布偏移选择性影响 summary-position (last token) attention pattern | D015 + 4-way eval + v7 direct eval + D024 + **D033 cross-variant model-gen** | 核心 negative finding。精确定位为 TEXT DISTRIBUTION SHIFT（exposure bias）。D033 确认跨所有训练变体的普遍性。 |\n| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |\n| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |\n\n---\n\n## 5. Key Selling Points\n\n**SP1 (核心卖点): Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画。** 30x training-inference GAR-ours gap 提供了 teacher-forcing distribution shift 如何摧毁 auxiliary attention loss 泛化性的实证证据。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。虽然 exposure bias 概念本身已知 (Bengio et al. 2015)，且 sequence generation 中有量化先例 (Ranzato et al. 2016, Wiseman & Rush 2016)，但此前无人刻画其对 auxiliary attention loss 的具体影响。我们的 30x gap 测量展示了这种脆弱性在 attention steering 场景下的严重程度。**注意：(1) claim scope 严格限于 lightweight residual gating + GAR auxiliary loss 的实测范围，不泛化到所有 attention steering 方法。(2) 30x gap 在 GAR-ours（last token only, summary-position attention）上测得（IID 0.50 vs model-gen 0.016）；GAR-Dongre（all response tokens）在两种分布上均低（~0.01-0.019），无 gap——表明 exposure bias 选择性影响 summary-position attention pattern，这一差异本身有分析价值。**\n\n**SP2: NTP-GAR 梯度动力学 + PCGrad 因果排除（gradient conflict is inconsequential）。** 观察到 67-79% 的层 NTP-GAR 梯度方向冲突（cos_sim<0）+ NTP 幅度 3-15x 压制 GAR（mag_ratio 7.5→14.7x）。**PCGrad 消融（D028）因果排除方向冲突**：投影后 cos_sim 围绕 0 震荡（range -0.151 to +0.091），L_GAR 坍塌轨迹不变。**推理端确认（IID same-protocol）**: v9 IID PPL = 2.780 vs v7 = 2.784（差 0.004，无改善）; v9 GAR-ours = 0.0151 vs v7 = 0.0157（差 <0.1pp）——**PCGrad 消除方向冲突后所有可观测指标均无变化**（GAR、PPL、NTP 均 ≈ v7）。方向冲突虽然可测量存在于 v7 中，但对训练和推理结果无任何因果影响——10-40× NTP 幅度主导使方向冲突完全无关紧要（inconsequential）。**⚠️ M017: 此前 \"PPL -46%\" 和 \"selective dissociation\" 论述为跨协议对比伪影（model-gen PPL 1.50 vs IID PPL 2.78），已撤回。** **精确 claim scope**: gradient direction conflict is **neither necessary nor sufficient** for the 30x GAR gap; exposure bias alone is sufficient。NOT necessary: 移除冲突→gap仍在; NOT sufficient: v7有冲突但L_GAR训练时收敛; Exposure bias is sufficient: 训练≠推理分布→GAR泛化失败。**Gate 行为额外 insight**: v9 gate dynamic range 比 v7 更宽 (L15 range 0.33 vs v7 0.21)——PCGrad 给 gate 更大自由度，但 gate 用该自由度更激进地优化 NTP 而非 GAR，说明优化景观固有偏好语言建模目标。\n\n**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融严格隔离贡献: TG (learned gate + GAR loss) / UG (uniform gate + GAR loss) / LoRA-only (gate=1.0 fixed + GAR loss, 无 gating 机制) / Base。注意：三个 fine-tuned 变体均使用 GAR loss，消融测试的是 gating 机制的增量贡献，而非 GAR loss 本身的效果。\n\n**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。\n\n**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。\n\n---\n\n## 6. Anticipated Reviewer Concerns\n\n| # | 严重度 | 预期质疑 | 回应策略 |\n|---|--------|----------|----------|\n| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |\n| W2 | **严重** | \"你只是没调对参数\" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |\n| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |\n| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |\n| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（30x 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| W6 | **严重** | 引用不足（Dream review: 11篇远不够）| 目标 25-30 篇。必须覆盖: attention sinks (Xiao et al. 2024), Found-in-the-Middle (Ko et al. 2024), gated attention (Qiu et al. 2025), transformer circuits (Elhage et al. 2021), FlexiDepth (Luo et al. 2025), multi-turn eval (MT-Bench-101, MultiChallenge), exposure bias mitigation (Professor Forcing, SEARNN) 等。Paper Agent 写作时负责扩充。|\n| W7 | **严重** | 单 seed 无方差估计 | 所有实验 seed=42，TG-LoRA 差异 ±0.001 在噪声层。回应: held-out eval 50 conversations 提供 paired bootstrap CI，若 CI 包含 0 则统计支持 \"zero benefit\"。必要时追加 2 个 seed 的训练。|\n| W8 | **中等** | 缺 exposure-bias mitigation 实验 | 测试 scheduled sampling / model-generated context 训练能否缩小 30x gap。加入 experiment_plan (P1)。如果实验表明 mitigation 确实缩小 gap，论文从 \"negative result\" 升级为 \"negative result + constructive direction\"。|\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 exposure bias 的定量测量（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| R3 | 低 | 30x gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |\n| R4 | ~~低~~ **已核实** | Code-paper 公式语义相反 | **已确认不一致（plan_017 DONE）**。代码正确实现 ReZero-style: `x_{l+1} = x_l + g_l · f_l(x_l)`（gate 缩放子层输出，g→0=层 no-op）。Dream paper.tex 错误写为 `x_{l+1} = g_l · x_l + f_l(x_l)`（gate 缩放残差流，g→0=破坏 skip connection）。**实验数据不受影响**（所有实验用同一份代码）。**Paper Agent 写作时必须**: (1) Method section 用正确公式 `x + g·f(x)`; (2) 机制叙事修正: g→0 = 子层输出被抑制（层变 no-op），NTP 推 g→1 是为保留层计算能力，不是保留 skip connection; (3) NF3 \"gate attenuation 2-7%\" 指子层贡献缩放，表述正确但需明确。|\n\n---\n\n## 7. Dongre et al. 关系定位\n\n| 维度 | Dongre et al. | 本文 |\n|------|---------------|------|\n| 核心问题 | \"发生了什么\" + \"为什么\" | \"怎么干预\" + \"为什么干预失败\" |\n| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |\n| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 30x 泛化 gap + turn conditioning 反转 |\n| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |\n| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |\n\n**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。\n\n共同推论: 两种独立干预路线均失败 → lightweight residual gating with auxiliary attention loss 在 teacher-forcing 下面临严重泛化障碍 → 需要 inference-time 干预或 exposure bias mitigation。（注意：scope 限于 lightweight gating，不泛化到所有 attention steering 方法。）\n\n---\n\n## 8. GAR 定义策略\n\n| 用途 | 定义 | Goal tokens | Response tokens | 理由 |\n|------|------|------------|----------------|------|\n| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |\n| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |\n| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |\n\n**D024 精确化**: GAR-ours 在 same-distribution (ultrachat) text 上 ≈0.49（泛化成功），在 model-generated text 上 ≈0.016（30x gap）。GAR-Dongre 在两种分布上均低 (~0.01-0.016, 无 gap)。30x gap 是 text distribution shift 现象，特定于 summary-position attention (GAR-ours)。\n\n---\n\n## 9. 论文结构草案\n\n1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示\n2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表\n3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention\n4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据\n5. **Method**: ThreadGate 架构（⚠️ 非简单标量 gate：per-layer 2 层 MLP + turn embedding，接收 hidden_state + turn_distance/turn_index，输出 per-token per-layer sigmoid gate 值。公式 g_l = σ(W_2·ReLU(W_1·[proj(x_l); emb(t_d, t_i)] + b_1) + b_2)。Uniform Gate = 同架构但用 constant_vector 替代 turn embedding，仍然 per-layer content-dependent）+ MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置\n6. **Experiments**: 四路消融 (TG/UG/LoRA-only/Base) with GAR + PPL dual metrics + 跨模型验证 (Llama-3.1-8B)\n7. **Analysis**: §6.1 NTP-GAR 梯度冲突观察 → §6.2 Gate turn conditioning (Wilcoxon) → §6.3 **PCGrad 因果排除方向冲突** → §6.4 Distribution shift (exposure bias) 作为主因 → §6.5 attention 可视化 + 训练动力学\n8. **Discussion**: 为什么 lightweight residual gating 不够 → exposure bias 对 auxiliary attention loss 的具体影响机制 → 潜在解决方向 (inference-time intervention / exposure bias mitigation for auxiliary losses / decoupled pathway / GAR-aware decoding) → **scope 声明: claim 限于 lightweight gating，不泛化到所有 attention steering**\n9. **Conclusion**: negative result 总结 + 对社区的 actionable 建议\n\n### 贡献列表（按 novelty 排序）\n\n1. **Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画**: 实证展示 teacher-forcing distribution shift 如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（30x training-inference GAR-ours gap），为 teacher-forcing 下的 attention steering 方法提供具体风险标杆\n2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）\n3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline\n4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性\n\n---\n\n## 10. 竞争力评估\n\n### Dream Review 结果 (2026-05-19, dream_20260519T135115)\n- **Best case**: 3.0 (Weak Reject / Findings-level)。主要扣分: claim 过度泛化 (W1), 引用不足 (W6), 单 seed (W7)。\n- **Median case**: 3.0 (Weak Reject)。同上 + distribution shift insight incremental (W5)。\n- **Worst case**: 未完成 review（crash），但 imagined experiments 显示最坏情况下 Llama-3 不复现 dramatic pattern。\n\n### 修正后预期\n- **收窄 claim + 扩充引用 + code 验证后**: best 预期 3.5 (Weak Accept / Borderline Conference)。移除两个 Major weakness (W1 overclaim + W6 thin refs)。\n- **加 bootstrap CI + Llama-3 数据后**: median 预期 3.0-3.5。\n- **冲 Main 条件**: 上述修正 + exposure-bias mitigation 实验 (W8) + 25-30 references。\n- **核心差异化**: 不是 \"gating 失败了\"（弱），而是 \"exposure bias 在 auxiliary attention loss 上的首个定量测量 + 失败机制 taxonomy\"。\n- **关键风险**: W5（exposure bias 已知）需要精确定位增量；W7（单 seed）需 bootstrap CI 或追加 seed。\n",
      "numLines": 149,
      "startLine": 1,
      "totalLines": 149
    }
  },
  "sourceToolAssistantUUID": "42b334b3-e951-42c3-bcaf-ac6735e96d8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T04:50:42.519Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MSCrcL5ahCGLJdGYACKT9h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b00a40e-6fed-4770-914c-235b0e2e3796",
  "isSidechain": false,
  "requestId": "req_011CbH1GBbhYPQeTE9RQr6Lv",
  "type": "assistant",
  "uuid": "ac3d96f0-da3f-41a4-9b1b-bbf6b5c75a54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmWWfxM4eAa5ZC9jYVbr6P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12874,
      "cache_read_input_tokens": 11841,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12874,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 307,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12874
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

_source line 13 · 2026-05-22T04:50:42.536Z_

<details><summary>↩ Tool result · `toolu_01MSCrcL5ahCGLJdGYACKT9h`</summary>

```text
1	% ============================================================
2	% Layer Importance
3	% ============================================================
4	
5	@inproceedings{gromov2024deeper,
6	  author    = {Gromov and others},
7	  title     = {{The Unreasonable Ineffectiveness of the Deeper Layers}},
8	  booktitle = {International Conference on Learning Representations},
9	  year      = {2024},
10	  url       = {https://arxiv.org/abs/2403.17887}
11	}
12	
13	@article{men2024shortgpt,
14	  author  = {Men and others},
15	  title   = {{ShortGPT: Layers in Large Language Models are More Redundant Than You Expect}},
16	  journal = {arXiv preprint arXiv:2403.03853},
17	  year    = {2024},
18	  url     = {https://arxiv.org/abs/2403.03853}
19	}
20	
21	@inproceedings{sun2025curse,
22	  author    = {Sun and others},
23	  title     = {{The Curse of Depth in Large Language Models}},
24	  booktitle = {Advances in Neural Information Processing Systems},
25	  year      = {2025},
26	  url       = {https://arxiv.org/abs/2502.05795}
27	}
28	
29	@article{lu2024reassessing,
30	  author  = {Lu, Yao and others},
31	  title   = {{Reassessing Layer Pruning in LLMs: New Insights and Methods}},
32	  journal = {arXiv preprint arXiv:2411.15558},
33	  year    = {2024},
34	  url     = {https://arxiv.org/abs/2411.15558}
35	}
36	
37	@inproceedings{fan2020layerdrop,
38	  author    = {Fan and others},
39	  title     = {{Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)}},
40	  booktitle = {International Conference on Learning Representations},
41	  year      = {2020},
42	  url       = {https://arxiv.org/abs/1909.11556}
43	}
44	
45	% ============================================================
46	% Multi-Turn Attention
47	% ============================================================
48	
49	@article{dongre2026attention,
50	  author  = {Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur},
51	  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},
52	  journal = {arXiv preprint arXiv:2605.12922},
53	  year    = {2026},
54	  url     = {https://arxiv.org/abs/2605.12922}
55	}
56	
57	@article{laban2025lost,
58	  author  = {Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer},
59	  title   = {{LLMs Get Lost In Multi-Turn Conversation}},
60	  journal = {arXiv preprint arXiv:2505.06120},
61	  year    = {2025},
62	  url     = {https://arxiv.org/abs/2505.06120}
63	}
64	
65	@article{liu2026intent,
66	  author  = {Liu and others},
67	  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},
68	  journal = {arXiv preprint arXiv:2602.07338},
69	  year    = {2026},
70	  url     = {https://arxiv.org/abs/2602.07338}
71	}
72	
73	@article{liu2023lost,
74	  author  = {Liu and others},
75	  title   = {{Lost in the Middle: How Language Models Use Long Contexts}},
76	  journal = {Transactions of the Association for Computational Linguistics},
77	  year    = {2023},
78	  url     = {https://arxiv.org/abs/2307.03172}
79	}
80	
81	@article{lin2025style,
82	  author  = {Lin, Yu-Xiang and others},
83	  title   = {{Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models}},
84	  journal = {arXiv preprint arXiv:2512.23578},
85	  year    = {2025},
86	  url     = {https://arxiv.org/abs/2512.23578}
87	}
88	
89	% ============================================================
90	% Residual Gating
91	% ============================================================
92	
93	@article{raposo2024mixture,
94	  author  = {Raposo and others},
95	  title   = {{Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models}},
96	  journal = {arXiv preprint arXiv:2404.02258},
97	  year    = {2024},
98	  url     = {https://arxiv.org/abs/2404.02258}
99	}
100	
101	@inproceedings{schuster2022calm,
102	  author    = {Schuster and others},
103	  title     = {{Confident Adaptive Language Modeling}},
104	  booktitle = {Advances in Neural Information Processing Systems},
105	  year      = {2022},
106	  url       = {https://arxiv.org/abs/2207.07061}
107	}
108	
109	@inproceedings{qiu2025gated,
110	  author    = {Qiu and others},
111	  title     = {{Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free}},
112	  booktitle = {Advances in Neural Information Processing Systems},
113	  year      = {2025},
114	  url       = {https://arxiv.org/abs/2505.06708}
115	}
116	
117	@inproceedings{wang2018skipnet,
118	  author    = {Wang and others},
119	  title     = {{SkipNet: Learning Dynamic Routing in Convolutional Networks}},
120	  booktitle = {European Conference on Computer Vision},
121	  year      = {2018},
122	  url       = {https://arxiv.org/abs/1711.09485}
123	}
124	
125	@article{luo2025flexidepth,
126	  author  = {Luo and others},
127	  title   = {{Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)}},
128	  journal = {arXiv preprint arXiv:2503.23798},
129	  year    = {2025},
130	  url     = {https://arxiv.org/abs/2503.23798}
131	}
132	
133	@article{lawson2025skip,
134	  author  = {Lawson and others},
135	  title   = {{Learning to Skip the Middle Layers of Transformers}},
136	  journal = {arXiv preprint arXiv:2506.21103},
137	  year    = {2025},
138	  url     = {https://arxiv.org/abs/2506.21103}
139	}
140	
141	% ============================================================
142	% Attention Manipulation
143	% ============================================================
144	
145	@inproceedings{press2022alibi,
146	  author    = {Press and others},
147	  title     = {{Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation}},
148	  booktitle = {International Conference on Learning Representations},
149	  year      = {2022},
150	  url       = {https://arxiv.org/abs/2108.12409}
151	}
152	
153	@article{chen2023positional,
154	  author  = {Chen and others},
155	  title   = {{Extending Context Window of Large Language Models via Positional Interpolation}},
156	  journal = {arXiv preprint arXiv:2306.15595},
157	  year    = {2023},
158	  url     = {https://arxiv.org/abs/2306.15595}
159	}
160	
161	@inproceedings{peng2024yarn,
162	  author    = {Peng and others},
163	  title     = {{YaRN: Efficient Context Window Extension of Large Language Models}},
164	  booktitle = {International Conference on Learning Representations},
165	  year      = {2024},
166	  url       = {https://arxiv.org/abs/2309.00071}
167	}
168	
169	@inproceedings{xiao2024streaming,
170	  author    = {Xiao and others},
171	  title     = {{Efficient Streaming Language Models with Attention Sinks}},
172	  booktitle = {International Conference on Learning Representations},
173	  year      = {2024},
174	  url       = {https://arxiv.org/abs/2309.17453}
175	}
176	
177	@inproceedings{han2024lminfinite,
178	  author    = {Han and others},
179	  title     = {{LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models}},
180	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
181	  year      = {2024},
182	  url       = {https://arxiv.org/abs/2308.16137}
183	}
184	
185	@article{hsieh2024found,
186	  author  = {Hsieh, Cheng-Yu and others},
187	  title   = {{Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization}},
188	  journal = {arXiv preprint arXiv:2406.16008},
189	  year    = {2024},
190	  url     = {https://arxiv.org/abs/2406.16008}
191	}
192	
193	% ============================================================
194	% Theoretical Foundations
195	% ============================================================
196	
197	@article{elhage2021framework,
198	  author  = {Elhage and others},
199	  title   = {{A Mathematical Framework for Transformer Circuits}},
200	  journal = {Anthropic Blog},
201	  year    = {2021},
202	  url     = {https://transformer-circuits.pub/2021/framework/index.html}
203	}
204	
205	@article{elhage2022superposition,
206	  author  = {Elhage and others},
207	  title   = {{Toy Models of Superposition}},
208	  journal = {arXiv preprint arXiv:2209.10652},
209	  year    = {2022},
210	  url     = {https://arxiv.org/abs/2209.10652}
211	}
212	
213	@article{belrose2023tuned,
214	  author  = {Belrose and others},
215	  title   = {{Eliciting Latent Predictions from Transformers with the Tuned Lens}},
216	  journal = {arXiv preprint arXiv:2303.08112},
217	  year    = {2023},
218	  url     = {https://arxiv.org/abs/2303.08112}
219	}
220	
221	@article{yu2023residual,
222	  author  = {Yu and others},
223	  title   = {{Exploring the Residual Stream of Transformers}},
224	  journal = {arXiv preprint arXiv:2312.12141},
225	  year    = {2023},
226	  url     = {https://arxiv.org/abs/2312.12141}
227	}
228	
229	@inproceedings{makkuva2025markov,
230	  author    = {Makkuva and others},
231	  title     = {{Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains}},
232	  booktitle = {International Conference on Learning Representations},
233	  year      = {2025},
234	  url       = {https://arxiv.org/abs/2402.04161}
235	}
236	
237	@inproceedings{ildiz2024markov,
238	  author    = {Ildiz and others},
239	  title     = {{From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers}},
240	  booktitle = {International Conference on Machine Learning},
241	  year      = {2024},
242	  url       = {https://arxiv.org/abs/2402.13512}
243	}
244	
245	% ============================================================
246	% Evaluation Benchmarks
247	% ============================================================
248	
249	@inproceedings{zheng2023mtbench,
250	  author    = {Zheng and others},
251	  title     = {{Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena}},
252	  booktitle = {Advances in Neural Information Processing Systems},
253	  year      = {2023},
254	  url       = {https://arxiv.org/abs/2306.05685}
255	}
256	
257	@inproceedings{chiang2024arena,
258	  author    = {Chiang and others},
259	  title     = {{Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference}},
260	  booktitle = {International Conference on Machine Learning},
261	  year      = {2024},
262	  url       = {https://arxiv.org/abs/2403.04132}
263	}
264	
265	@inproceedings{dubois2024alpacaeval,
266	  author    = {Dubois and others},
267	  title     = {{Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators}},
268	  booktitle = {Conference on Language Modeling},
269	  year      = {2024},
270	  url       = {https://arxiv.org/abs/2404.04475}
271	}
272	
273	@article{lin2024wildbench,
274	  author  = {Lin and others},
275	  title   = {{WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild}},
276	  journal = {arXiv preprint arXiv:2406.04770},
277	  year    = {2024},
278	  url     = {https://arxiv.org/abs/2406.04770}
279	}
280	
281	@inproceedings{bai2024mtbench101,
282	  author    = {Bai and others},
283	  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},
284	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
285	  year      = {2024},
286	  url       = {https://arxiv.org/abs/2402.14762}
287	}
288	
289	@article{sirdeshmukh2025multichallenge,
290	  author  = {Sirdeshmukh and others},
291	  title   = {{MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs}},
292	  journal = {arXiv preprint arXiv:2501.17399},
293	  year    = {2025},
294	  url     = {https://arxiv.org/abs/2501.17399}
295	}
296	
297	% ============================================================
298	% Exposure Bias
299	% ============================================================
300	
301	@inproceedings{bengio2015scheduled,
302	  author    = {Bengio and Vinyals and Jaitly and Shazeer},
303	  title     = {{Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks}},
304	  booktitle = {Advances in Neural Information Processing Systems},
305	  year      = {2015},
306	  url       = {https://arxiv.org/abs/1506.03099}
307	}
308	
309	@inproceedings{ranzato2016sequence,
310	  author    = {Ranzato and Chopra and Auli and Zaremba},
311	  title     = {{Sequence Level Training with Recurrent Neural Networks}},
312	  booktitle = {International Conference on Learning Representations},
313	  year      = {2016},
314	  url       = {https://arxiv.org/abs/1511.06732}
315	}
316	
317	@inproceedings{lamb2016professor,
318	  author    = {Lamb and Goyal and Zhang and Zhang and Courville and Bengio},
319	  title     = {{Professor Forcing: A New Algorithm for Training Recurrent Networks}},
320	  booktitle = {Advances in Neural Information Processing Systems},
321	  year      = {2016},
322	  url       = {https://arxiv.org/abs/1610.09038}
323	}
324	
325	@inproceedings{leblond2018searnn,
326	  author    = {Leblond and Alayrac and Osokin and Lacoste-Julien},
327	  title     = {{SEARNN: Training RNNs with Global-Local Losses}},
328	  booktitle = {International Conference on Learning Representations},
329	  year      = {2018},
330	  url       = {https://arxiv.org/abs/1706.04499}
331	}
332	
333	@article{he2019exposure,
334	  author  = {He and Zhang and Zhou and Glass},
335	  title   = {{Quantifying Exposure Bias for Neural Language Generation}},
336	  journal = {arXiv preprint arXiv:1905.10617},
337	  year    = {2019},
338	  url     = {https://arxiv.org/abs/1905.10617}
339	}
340	
341	% ============================================================
342	% Gradient Conflict / Multi-Task Learning
343	% ============================================================
344	
345	@inproceedings{yu2020pcgrad,
346	  author    = {Yu and Kumar and Gupta and Levine and Hausman and Finn},
347	  title     = {{Gradient Surgery for Multi-Task Learning}},
348	  booktitle = {Advances in Neural Information Processing Systems},
349	  year      = {2020},
350	  url       = {https://arxiv.org/abs/2001.06782}
351	}
352	
353	@inproceedings{chen2018gradnorm,
354	  author    = {Chen and Badrinarayanan and Lee and Rabinovich},
355	  title     = {{GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks}},
356	  booktitle = {International Conference on Machine Learning},
357	  year      = {2018},
358	  url       = {https://arxiv.org/abs/1711.02257}
359	}
360	
361	@inproceedings{liu2021cagrad,
362	  author    = {Liu and Liu and Jin and Stone and Liu},
363	  title     = {{Conflict-Averse Gradient Descent for Multi-task Learning}},
364	  booktitle = {Advances in Neural Information Processing Systems},
365	  year      = {2021},
366	  url       = {https://arxiv.org/abs/2110.14048}
367	}
368	
369	@inproceedings{navon2022nash,
370	  author    = {Navon and Shamsian and Achituve and Maron and Kawaguchi and Chechik and Fetaya},
371	  title     = {{Multi-Task Learning as a Bargaining Game}},
372	  booktitle = {International Conference on Machine Learning},
373	  year      = {2022},
374	  url       = {https://arxiv.org/abs/2202.01017}
375	}
376	
377	% ============================================================
378	% Residual Scaling
379	% ============================================================
380	
381	@inproceedings{bachlechner2021rezero,
382	  author    = {Bachlechner and Majumder and Mao and Cottrell and McAuley},
383	  title     = {{ReZero is All You Need: Fast Convergence at Large Depth}},
384	  booktitle = {Uncertainty in Artificial Intelligence},
385	  year      = {2021},
386	  url       = {https://arxiv.org/abs/2003.04887}
387	}
388	
389	@inproceedings{zhang2019fixup,
390	  author    = {Zhang and Dauphin and Ma},
391	  title     = {{Fixup Initialization: Residual Learning Without Normalization}},
392	  booktitle = {International Conference on Learning Representations},
393	  year      = {2019},
394	  url       = {https://arxiv.org/abs/1901.09321}
395	}
396	
397	@article{grattafiori2024llama3,
398	  author  = {Grattafiori and others},
399	  title   = {{The Llama 3 Herd of Models}},
400	  journal = {arXiv preprint arXiv:2407.21783},
401	  year    = {2024},
402	  url     = {https://arxiv.org/abs/2407.21783}
403	}
404	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac3d96f0-da3f-41a4-9b1b-bbf6b5c75a54",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "ebf3b8a7-2130-4a56-8ca8-93d2f2d4fa0d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib",
      "content": "% ============================================================\n% Layer Importance\n% ============================================================\n\n@inproceedings{gromov2024deeper,\n  author    = {Gromov and others},\n  title     = {{The Unreasonable Ineffectiveness of the Deeper Layers}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.17887}\n}\n\n@article{men2024shortgpt,\n  author  = {Men and others},\n  title   = {{ShortGPT: Layers in Large Language Models are More Redundant Than You Expect}},\n  journal = {arXiv preprint arXiv:2403.03853},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2403.03853}\n}\n\n@inproceedings{sun2025curse,\n  author    = {Sun and others},\n  title     = {{The Curse of Depth in Large Language Models}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.05795}\n}\n\n@article{lu2024reassessing,\n  author  = {Lu, Yao and others},\n  title   = {{Reassessing Layer Pruning in LLMs: New Insights and Methods}},\n  journal = {arXiv preprint arXiv:2411.15558},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2411.15558}\n}\n\n@inproceedings{fan2020layerdrop,\n  author    = {Fan and others},\n  title     = {{Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2020},\n  url       = {https://arxiv.org/abs/1909.11556}\n}\n\n% ============================================================\n% Multi-Turn Attention\n% ============================================================\n\n@article{dongre2026attention,\n  author  = {Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur},\n  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},\n  journal = {arXiv preprint arXiv:2605.12922},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2605.12922}\n}\n\n@article{laban2025lost,\n  author  = {Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer},\n  title   = {{LLMs Get Lost In Multi-Turn Conversation}},\n  journal = {arXiv preprint arXiv:2505.06120},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2505.06120}\n}\n\n@article{liu2026intent,\n  author  = {Liu and others},\n  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},\n  journal = {arXiv preprint arXiv:2602.07338},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2602.07338}\n}\n\n@article{liu2023lost,\n  author  = {Liu and others},\n  title   = {{Lost in the Middle: How Language Models Use Long Contexts}},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2307.03172}\n}\n\n@article{lin2025style,\n  author  = {Lin, Yu-Xiang and others},\n  title   = {{Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models}},\n  journal = {arXiv preprint arXiv:2512.23578},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2512.23578}\n}\n\n% ============================================================\n% Residual Gating\n% ============================================================\n\n@article{raposo2024mixture,\n  author  = {Raposo and others},\n  title   = {{Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models}},\n  journal = {arXiv preprint arXiv:2404.02258},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2404.02258}\n}\n\n@inproceedings{schuster2022calm,\n  author    = {Schuster and others},\n  title     = {{Confident Adaptive Language Modeling}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2207.07061}\n}\n\n@inproceedings{qiu2025gated,\n  author    = {Qiu and others},\n  title     = {{Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2505.06708}\n}\n\n@inproceedings{wang2018skipnet,\n  author    = {Wang and others},\n  title     = {{SkipNet: Learning Dynamic Routing in Convolutional Networks}},\n  booktitle = {European Conference on Computer Vision},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1711.09485}\n}\n\n@article{luo2025flexidepth,\n  author  = {Luo and others},\n  title   = {{Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)}},\n  journal = {arXiv preprint arXiv:2503.23798},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2503.23798}\n}\n\n@article{lawson2025skip,\n  author  = {Lawson and others},\n  title   = {{Learning to Skip the Middle Layers of Transformers}},\n  journal = {arXiv preprint arXiv:2506.21103},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2506.21103}\n}\n\n% ============================================================\n% Attention Manipulation\n% ============================================================\n\n@inproceedings{press2022alibi,\n  author    = {Press and others},\n  title     = {{Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2108.12409}\n}\n\n@article{chen2023positional,\n  author  = {Chen and others},\n  title   = {{Extending Context Window of Large Language Models via Positional Interpolation}},\n  journal = {arXiv preprint arXiv:2306.15595},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2306.15595}\n}\n\n@inproceedings{peng2024yarn,\n  author    = {Peng and others},\n  title     = {{YaRN: Efficient Context Window Extension of Large Language Models}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2309.00071}\n}\n\n@inproceedings{xiao2024streaming,\n  author    = {Xiao and others},\n  title     = {{Efficient Streaming Language Models with Attention Sinks}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2309.17453}\n}\n\n@inproceedings{han2024lminfinite,\n  author    = {Han and others},\n  title     = {{LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2308.16137}\n}\n\n@article{hsieh2024found,\n  author  = {Hsieh, Cheng-Yu and others},\n  title   = {{Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization}},\n  journal = {arXiv preprint arXiv:2406.16008},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2406.16008}\n}\n\n% ============================================================\n% Theoretical Foundations\n% ============================================================\n\n@article{elhage2021framework,\n  author  = {Elhage and others},\n  title   = {{A Mathematical Framework for Transformer Circuits}},\n  journal = {Anthropic Blog},\n  year    = {2021},\n  url     = {https://transformer-circuits.pub/2021/framework/index.html}\n}\n\n@article{elhage2022superposition,\n  author  = {Elhage and others},\n  title   = {{Toy Models of Superposition}},\n  journal = {arXiv preprint arXiv:2209.10652},\n  year    = {2022},\n  url     = {https://arxiv.org/abs/2209.10652}\n}\n\n@article{belrose2023tuned,\n  author  = {Belrose and others},\n  title   = {{Eliciting Latent Predictions from Transformers with the Tuned Lens}},\n  journal = {arXiv preprint arXiv:2303.08112},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2303.08112}\n}\n\n@article{yu2023residual,\n  author  = {Yu and others},\n  title   = {{Exploring the Residual Stream of Transformers}},\n  journal = {arXiv preprint arXiv:2312.12141},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2312.12141}\n}\n\n@inproceedings{makkuva2025markov,\n  author    = {Makkuva and others},\n  title     = {{Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2402.04161}\n}\n\n@inproceedings{ildiz2024markov,\n  author    = {Ildiz and others},\n  title     = {{From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.13512}\n}\n\n% ============================================================\n% Evaluation Benchmarks\n% ============================================================\n\n@inproceedings{zheng2023mtbench,\n  author    = {Zheng and others},\n  title     = {{Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{chiang2024arena,\n  author    = {Chiang and others},\n  title     = {{Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.04132}\n}\n\n@inproceedings{dubois2024alpacaeval,\n  author    = {Dubois and others},\n  title     = {{Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators}},\n  booktitle = {Conference on Language Modeling},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2404.04475}\n}\n\n@article{lin2024wildbench,\n  author  = {Lin and others},\n  title   = {{WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild}},\n  journal = {arXiv preprint arXiv:2406.04770},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2406.04770}\n}\n\n@inproceedings{bai2024mtbench101,\n  author    = {Bai and others},\n  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.14762}\n}\n\n@article{sirdeshmukh2025multichallenge,\n  author  = {Sirdeshmukh and others},\n  title   = {{MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs}},\n  journal = {arXiv preprint arXiv:2501.17399},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2501.17399}\n}\n\n% ============================================================\n% Exposure Bias\n% ============================================================\n\n@inproceedings{bengio2015scheduled,\n  author    = {Bengio and Vinyals and Jaitly and Shazeer},\n  title     = {{Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2015},\n  url       = {https://arxiv.org/abs/1506.03099}\n}\n\n@inproceedings{ranzato2016sequence,\n  author    = {Ranzato and Chopra and Auli and Zaremba},\n  title     = {{Sequence Level Training with Recurrent Neural Networks}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1511.06732}\n}\n\n@inproceedings{lamb2016professor,\n  author    = {Lamb and Goyal and Zhang and Zhang and Courville and Bengio},\n  title     = {{Professor Forcing: A New Algorithm for Training Recurrent Networks}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1610.09038}\n}\n\n@inproceedings{leblond2018searnn,\n  author    = {Leblond and Alayrac and Osokin and Lacoste-Julien},\n  title     = {{SEARNN: Training RNNs with Global-Local Losses}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1706.04499}\n}\n\n@article{he2019exposure,\n  author  = {He and Zhang and Zhou and Glass},\n  title   = {{Quantifying Exposure Bias for Neural Language Generation}},\n  journal = {arXiv preprint arXiv:1905.10617},\n  year    = {2019},\n  url     = {https://arxiv.org/abs/1905.10617}\n}\n\n% ============================================================\n% Gradient Conflict / Multi-Task Learning\n% ============================================================\n\n@inproceedings{yu2020pcgrad,\n  author    = {Yu and Kumar and Gupta and Levine and Hausman and Finn},\n  title     = {{Gradient Surgery for Multi-Task Learning}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2020},\n  url       = {https://arxiv.org/abs/2001.06782}\n}\n\n@inproceedings{chen2018gradnorm,\n  author    = {Chen and Badrinarayanan and Lee and Rabinovich},\n  title     = {{GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1711.02257}\n}\n\n@inproceedings{liu2021cagrad,\n  author    = {Liu and Liu and Jin and Stone and Liu},\n  title     = {{Conflict-Averse Gradient Descent for Multi-task Learning}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2110.14048}\n}\n\n@inproceedings{navon2022nash,\n  author    = {Navon and Shamsian and Achituve and Maron and Kawaguchi and Chechik and Fetaya},\n  title     = {{Multi-Task Learning as a Bargaining Game}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2202.01017}\n}\n\n% ============================================================\n% Residual Scaling\n% ============================================================\n\n@inproceedings{bachlechner2021rezero,\n  author    = {Bachlechner and Majumder and Mao and Cottrell and McAuley},\n  title     = {{ReZero is All You Need: Fast Convergence at Large Depth}},\n  booktitle = {Uncertainty in Artificial Intelligence},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2003.04887}\n}\n\n@inproceedings{zhang2019fixup,\n  author    = {Zhang and Dauphin and Ma},\n  title     = {{Fixup Initialization: Residual Learning Without Normalization}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1901.09321}\n}\n\n@article{grattafiori2024llama3,\n  author  = {Grattafiori and others},\n  title   = {{The Llama 3 Herd of Models}},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2407.21783}\n}\n",
      "numLines": 404,
      "startLine": 1,
      "totalLines": 404
    }
  },
  "sourceToolAssistantUUID": "ac3d96f0-da3f-41a4-9b1b-bbf6b5c75a54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-22T04:50:42.696Z_

<details open><summary>🔧 Tool call — Read · `toolu_016HSdC7QqUZRQsqsc59ieLd`</summary>

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
  "parentUuid": "ebf3b8a7-2130-4a56-8ca8-93d2f2d4fa0d",
  "isSidechain": false,
  "requestId": "req_011CbH1GBbhYPQeTE9RQr6Lv",
  "type": "assistant",
  "uuid": "adb39f79-617e-44d3-a8a0-eebeec1457b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmWWfxM4eAa5ZC9jYVbr6P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12874,
      "cache_read_input_tokens": 11841,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12874,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 307,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12874
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

_source line 15_

```json
{
  "type": "last-prompt",
  "leafUuid": "adb39f79-617e-44d3-a8a0-eebeec1457b9",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Fill literature map with core related papers",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Tool result

_source line 17 · 2026-05-22T04:50:43.021Z_

<details><summary>↩ Tool result · `toolu_016HSdC7QqUZRQsqsc59ieLd`</summary>

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
430	  residual_scaling:
431	    description: Residual connection scaling, initialization, and zero-init methods for deep transformers
432	    papers:
433	    - title: 'ReZero is All You Need: Fast Convergence at Large Depth'
434	      authors: Bachlechner, Majumder, Mao, Cottrell, McAuley
435	      venue: UAI 2021
436	      year: 2021
437	      url: https://arxiv.org/abs/2003.04887
438	      role: must-cite
439	      relevance: ThreadGate 的 per-layer sigmoid gate 直接源自 ReZero 的零初始化残差缩放思想：x_{l+1} = x_l + alpha_l * f_l(x_l)，alpha 初始化为
440	        0。ThreadGate 将标量 alpha 替换为 turn-conditioned sigmoid gate
441	      abstract: Initializes each residual connection with a learnable zero-initialized parameter, enabling training of extremely
442	        deep transformers (up to 10,000 layers) without warmup or normalization. Achieves significantly faster convergence
443	        by allowing the network to start as identity and gradually incorporate layer contributions.
444	    - title: 'Fixup Initialization: Residual Learning Without Normalization'
445	      authors: Zhang, Dauphin, Ma
446	      venue: ICLR 2019
447	      year: 2019
448	      url: https://arxiv.org/abs/1901.09321
449	      role: foundation
450	      relevance: 理论推导残差分支的初始化缩放如何控制梯度爆炸，为 ReZero 和 ThreadGate 的残差缩放设计提供数学基础。证明适当的残差缩放可完全替代 normalization layers
451	      abstract: Proposes a properly scaled initialization for residual networks that enables training very deep models without
452	        normalization layers. Theoretically shows that residual branch scaling by 1/sqrt(L) prevents gradient explosion. Matches
453	        BatchNorm performance on ImageNet and CIFAR with ResNets up to 110 layers.
454	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adb39f79-617e-44d3-a8a0-eebeec1457b9",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "5e05c331-706e-4b38-8b1f-cc3b31423f39",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
      "content": "categories:\n  layer_importance:\n    description: Layer-wise importance analysis, redundancy, and pruning in transformers\n    papers:\n    - title: The Unreasonable Ineffectiveness of the Deeper Layers\n      authors: Gromov et al.\n      venue: ICLR 2025\n      year: 2024\n      url: https://arxiv.org/abs/2403.17887\n      role: foundation\n      relevance: 发现 LLM 深层高度冗余，可删除近半层而性能不降；浅层对知识存储至关重要\n      abstract: Studies knowledge storage via layer pruning. Finds minimal performance degradation until up to half of layers\n        are removed.\n    - title: 'ShortGPT: Layers in Large Language Models are More Redundant Than You Expect'\n      authors: Men et al.\n      venue: arXiv 2024\n      year: 2024\n      url: https://arxiv.org/abs/2403.03853\n      role: foundation\n      relevance: 提出 Block Influence (BI) 度量各层重要性，发现许多层高度相似且功能冗余\n      abstract: Defines Block Influence (BI) metric to gauge layer significance. Discovers many LLM layers exhibit high similarity.\n    - title: The Curse of Depth in Large Language Models\n      authors: Sun et al.\n      venue: NeurIPS 2025\n      year: 2025\n      url: https://arxiv.org/abs/2502.05795\n      role: foundation\n      relevance: Pre-LN 导致深层梯度趋近恒等映射。解释 ThreadGate 中 late layers gate 接近 1.0\n      abstract: Pre-Layer Normalization causes output variance to grow exponentially with depth.\n    - title: 'Reassessing Layer Pruning in LLMs: New Insights and Methods'\n      authors: Anonymous\n      venue: arXiv 2024\n      year: 2024\n      url: https://arxiv.org/abs/2411.15558\n      role: context\n      relevance: 删除最后 25% 层 + 微调即可获得强性能，证实深层冗余\n      abstract: Simply pruning the final 25% of layers followed by fine-tuning yields strong performance.\n    - title: Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\n      authors: Fan et al.\n      venue: ICLR 2020\n      year: 2020\n      url: https://arxiv.org/abs/1909.11556\n      role: method-component\n      relevance: ThreadGate 的 gating 可视为 LayerDrop 的 soft 版本\n      abstract: Structured dropout on entire transformer layers during training.\n  multi_turn_attention:\n    description: Attention degradation and instruction following failure in multi-turn or long-context scenarios\n    papers:\n    - title: 'When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction'\n      authors: Dongre, Hsieh, Lai, Yoon, Bui, Hakkani-Tur\n      venue: arXiv 2026\n      year: 2026\n      url: https://arxiv.org/abs/2605.12922\n      role: foundation\n      relevance: 定义 GAR，诊断多轮 attention 通道关闭。纯诊断论文，未提出干预方案。ThreadGate 是首个基于其诊断的干预方法\n      abstract: 'Channel-transition account: goal tokens become less accessible through attention while goal info persists\n        in residual representations. Introduces GAR metric.'\n      notes:\n        gar_definition: GAR(τ) = (1/L·H·|ℛτ|) Σℓ Σh Σi∈ℛτ Σj∈𝒢 A_{i,j}. ALL layers, ALL heads averaged. Goal tokens = system\n          prompt task-specifying tokens only\n        models_tested: Mistral-7B, LLaMA-3.1-8B, Qwen-2.5 (3B/7B/14B/32B), Mixtral-8x7B + 6 additional\n        gar_decline: 27-48% over 50 turns, monotonic (Mann-Kendall p<1e-7)\n        residual_probes: 'LDA on PCA-reduced residuals (50 PCs). Peak AUC: LLaMA L2=0.99, Qwen L11=0.98, Mixtral L21=0.99,\n          Mistral L27=0.87'\n        qwen_layer_profile: Goal encoding rises steeply from L5. Our v3b L4 outlier may be the layer just before goal encoding\n          begins\n        intervention_tested: Periodic goal re-injection FAILED (Appendix H)\n        no_solution: true\n        sliding_window: Attention mask W=4096, Qwen crossover at turn 20. Linear W-vs-crossover (R2~1)\n        framing_impact: GAR not our original metric. No intervention proposed -> ThreadGate is first solution. Residual persistence\n          directly supports our theory\n    - title: LLMs Get Lost In Multi-Turn Conversation\n      authors: Levy et al.\n      venue: arXiv 2025\n      year: 2025\n      url: https://arxiv.org/abs/2505.06120\n      role: foundation\n      relevance: 量化多轮对话性能衰减：平均下降 39%，不可靠性增加 112%\n      abstract: All top LLMs exhibit significantly lower performance in multi-turn vs single-turn, averaging 39% drop.\n    - title: Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation\n      authors: Liu et al.\n      venue: arXiv 2026\n      year: 2026\n      url: https://arxiv.org/abs/2602.07338\n      role: context\n      relevance: 多轮失败根因是 intent alignment gap，scaling 无法解决。支撑 ThreadGate 架构级方案动机\n      abstract: Lost in Conversation stems from intent alignment gap, not capability deficits. Scaling cannot resolve.\n    - title: 'Lost in the Middle: How Language Models Use Long Contexts'\n      authors: Liu et al.\n      venue: TACL 2024\n      year: 2023\n      url: https://arxiv.org/abs/2307.03172\n      role: foundation\n      relevance: U 型 attention 分布（首尾强、中间弱）。多轮场景是此现象在 turn boundary 上的扩展\n      abstract: Performance highest at beginning/end of context, degrading for middle positions.\n    - title: 'Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models'\n      authors: Anonymous\n      venue: arXiv 2025\n      year: 2025\n      url: https://arxiv.org/abs/2512.23578\n      role: context\n      relevance: 多轮对话中 style instruction 遵循衰减，system message 比 user message 更严重\n      abstract: Style instruction in system messages degrades more than in user messages across turns.\n  residual_gating:\n    description: Gating mechanisms for transformer residual connections and adaptive depth\n    papers:\n    - title: 'Mixture-of-Depths: Dynamically allocating compute in transformer-based language models'\n      authors: Raposo et al.\n      venue: arXiv 2024 (Google DeepMind)\n      year: 2024\n      url: https://arxiv.org/abs/2404.02258\n      role: method-component\n      relevance: top-k routing 动态分配计算。ThreadGate 可视为 MoD 在 turn boundary 上的特化\n      abstract: Dynamically allocate FLOPs per layer via top-k routing. 1.5% loss improvement or 50% FLOP reduction.\n    - title: Confident Adaptive Language Modeling (CALM)\n      authors: Schuster et al.\n      venue: NeurIPS 2022\n      year: 2022\n      url: https://arxiv.org/abs/2207.07061\n      role: method-component\n      relevance: 置信度 early exit。CALM 是 monotonic exit，ThreadGate 允许 selective layer gating\n      abstract: Dynamically allocating compute per input based on confidence. Up to 3x speedup.\n    - title: 'Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free'\n      authors: Qiu et al.\n      venue: NeurIPS 2025 (Oral)\n      year: 2025\n      url: https://arxiv.org/abs/2505.06708\n      role: method-component\n      relevance: SDPA 输出加 sigmoid gate 消除 attention sink。可参考 head-specific sigmoid gate 设计\n      abstract: Head-specific sigmoid gate after SDPA. Eliminates attention sink (83% to 4%).\n    - title: 'SkipNet: Learning Dynamic Routing in Convolutional Networks'\n      authors: Wang et al.\n      venue: ECCV 2018\n      year: 2018\n      url: https://arxiv.org/abs/1711.09485\n      role: method-component\n      relevance: 残差网络逐层 gating 先驱。ThreadGate per-layer gating 的前身\n      abstract: Gating network to selectively skip convolutional blocks. RL+SL hybrid training.\n    - title: Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)\n      authors: Luo et al.\n      venue: arXiv 2025\n      year: 2025\n      url: https://arxiv.org/abs/2503.23798\n      role: direct-competitor\n      relevance: plug-in router+adapter on frozen LLM 自适应 layer skipping。与 ThreadGate 高度类似，直接竞品\n      abstract: Dynamically adjusts layers via plug-in router and adapter. Llama-3-8B skips 8/32 layers maintaining performance.\n    - title: Learning to Skip the Middle Layers of Transformers\n      authors: Lawson et al.\n      venue: arXiv 2025\n      year: 2025\n      url: https://arxiv.org/abs/2506.21103\n      role: context\n      relevance: middle-out layer skipping 负面结果参考\n      abstract: Gating to skip middle blocks. Does not improve vs dense baselines at investigated scales.\n  attention_manipulation:\n    description: Methods that modify attention weights, positional encoding, or attention distributions to handle long-range\n      dependencies\n    papers:\n    - title: 'Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation'\n      authors: Press et al.\n      venue: ICLR 2022\n      year: 2022\n      url: https://arxiv.org/abs/2108.12409\n      role: foundation\n      relevance: ALiBi 在注意力分数上施加距离线性惩罚实现长度外推，是注意力操纵路线的代表方法，与 ThreadGate 残差门控路线形成设计空间对比\n      abstract: Replaces positional embeddings with linear bias on attention logits penalizing distance. 1.3B model trained\n        on 1024 generalizes to 2048 without fine-tuning.\n    - title: Extending Context Window of Large Language Models via Positional Interpolation\n      authors: Chen et al.\n      venue: arXiv 2023\n      year: 2023\n      url: https://arxiv.org/abs/2306.15595\n      role: foundation\n      relevance: 位置插值通过压缩 RoPE 索引扩展上下文至 32k，属于注意力机制内部解决长序列的路线，与 ThreadGate 在残差层解决多轮衰减形成对比\n      abstract: Linearly down-scales RoPE position indices to extend context to 32768 tokens in 1000 fine-tuning steps.\n    - title: 'YaRN: Efficient Context Window Extension of Large Language Models'\n      authors: Peng et al.\n      venue: ICLR 2024\n      year: 2024\n      url: https://arxiv.org/abs/2309.00071\n      role: foundation\n      relevance: YaRN 综合 NTK-aware 和分段插值改进 RoPE 外推，代表注意力位置编码修改应对长程衰减的成熟路线，与 ThreadGate 机制不同\n      abstract: Combines NTK-aware interpolation with ramp function for different RoPE frequency components. Extends LLaMA-2\n        to 128k context with 10x fewer tokens.\n    - title: Efficient Streaming Language Models with Attention Sinks\n      authors: Xiao et al.\n      venue: ICLR 2024\n      year: 2024\n      url: https://arxiv.org/abs/2309.17453\n      role: context\n      relevance: 发现 attention sink 现象（初始 token 聚集高权重），说明多轮对话中早期轮次 token 天然受偏置，ThreadGate 从残差路径角度控制历史轮信息保留\n      abstract: LLMs assign disproportionate attention to first few tokens regardless of semantics. Retaining sink tokens\n        enables stable streaming inference over 4M tokens.\n    - title: 'LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models'\n      authors: Han et al.\n      venue: ACL 2024\n      year: 2024\n      url: https://arxiv.org/abs/2308.16137\n      role: context\n      relevance: 用 Λ 形注意力掩码加距离截断实现超长上下文推理，揭示调整注意力掩码和调整残差门控是两条平行路线\n      abstract: Applies Λ-shaped attention mask plus distance limit on position encodings. Generalizes to 200M tokens with\n        2.7x speedup, no parameter updates.\n    - title: 'Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization'\n      authors: Ko et al.\n      venue: arXiv 2024\n      year: 2024\n      url: https://arxiv.org/abs/2406.16008\n      role: direct-competitor\n      relevance: 直接校准注意力位置偏置修复中段信息丢失，最接近 ThreadGate 问题定义的注意力方案，审稿人会以此质疑为何不直接修正注意力\n      abstract: Identifies U-shaped positional attention bias causing lost-in-the-middle. Training-free calibration redistributes\n        attention to middle positions, improving QA by 6-15pp.\n  theoretical_foundations:\n    description: Theoretical analysis of transformer residual streams, information flow, and attention dynamics\n    papers:\n    - title: A Mathematical Framework for Transformer Circuits\n      authors: Elhage et al.\n      venue: Transformer Circuits Thread 2021\n      year: 2021\n      url: https://transformer-circuits.pub/2021/framework/index.html\n      role: foundation\n      relevance: 提出残差流作为 transformer 各组件通信核心通道，直接为 ThreadGate 在残差连接处插入门控提供机制解释框架\n      abstract: Linear algebraic decomposition of transformer computations. Attention heads and MLPs as read/write operations\n        on shared residual stream. Formalizes induction heads and QK/OV circuits.\n    - title: Toy Models of Superposition\n      authors: Elhage et al.\n      venue: arXiv 2022\n      year: 2022\n      url: https://arxiv.org/abs/2209.10652\n      role: foundation\n      relevance: 揭示残差流子空间叠加存储稀疏特征的机制，为 ThreadGate 按轮次条件化选择性激活残差通道提供理论依据\n      abstract: Neural networks store more features than dimensions via superposition when features are sparse. Links polysemanticity\n        to geometry of uniform polytopes.\n    - title: Eliciting Latent Predictions from Transformers with the Tuned Lens\n      authors: Belrose et al.\n      venue: arXiv 2023\n      year: 2023\n      url: https://arxiv.org/abs/2303.08112\n      role: foundation\n      relevance: 逐层解码残差流隐状态揭示信息在深度方向渐进精化，支撑 ThreadGate 不同层门控强度差异化设计的动机\n      abstract: Per-layer affine probes decode intermediate residual stream states into vocabulary distributions. Shows predictions\n        iteratively refined across depth up to 20B parameters.\n    - title: Exploring the Residual Stream of Transformers\n      authors: Yu et al.\n      venue: arXiv 2023\n      year: 2023\n      url: https://arxiv.org/abs/2312.12141\n      role: foundation\n      relevance: 分析残差连接对 logit 空间的加法效应，揭示知识参数跨层分布规律，为 ThreadGate 定位门控插入层提供实证参考\n      abstract: Residual connections act as direct additive operations on pre-softmax logits. Identifies factual knowledge\n        storage distribution across layers and modules.\n    - title: 'Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains'\n      authors: Makkuva et al.\n      venue: ICLR 2025\n      year: 2025\n      url: https://arxiv.org/abs/2402.04161\n      role: foundation\n      relevance: 用 Markov 链理论刻画注意力深度依赖性，解释为何单层 transformer 无法形成归纳头，支持 ThreadGate 在多层残差路径施加门控的必要性\n      abstract: Theoretical framework via Markov chain properties. Two-layer transformers learn induction heads on first-order\n        Markov data; single-layer models get trapped in unigram minima.\n    - title: 'From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers'\n      authors: Ildiz et al.\n      venue: ICML 2024\n      year: 2024\n      url: https://arxiv.org/abs/2402.13512\n      role: foundation\n      relevance: 建立自注意力与上下文条件 Markov 链的精确映射，为分析多轮对话 token 分布随轮次漂移（GAR decay）提供随机过程理论基础\n      abstract: Mathematical equivalence between self-attention and context-conditioned Markov chains. Output distribution\n        sampled from context-weighted transition matrix.\n  evaluation_benchmarks:\n    description: Multi-turn dialogue and instruction-following evaluation benchmarks for LLMs\n    papers:\n    - title: Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\n      authors: Zheng et al.\n      venue: NeurIPS 2023\n      year: 2023\n      url: https://arxiv.org/abs/2306.05685\n      role: foundation\n      relevance: MT-Bench 多轮对话评测框架，是 ThreadGate 验证多轮 GAR 衰减修复效果的核心 benchmark\n      abstract: Introduces MT-Bench (80 multi-turn questions) and Chatbot Arena. GPT-4 achieves >80% agreement with human\n        preferences as judge.\n    - title: 'Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference'\n      authors: Chiang et al.\n      venue: ICML 2024\n      year: 2024\n      url: https://arxiv.org/abs/2403.04132\n      role: foundation\n      relevance: 基于 ELO 排名的人类偏好评估体系，衡量多轮对话模型综合能力的权威 leaderboard\n      abstract: Chatbot Arena with 240K+ votes from 90K+ users across 50+ models. Bradley-Terry and ELO ranking validated\n        against expert raters.\n    - title: 'Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators'\n      authors: Dubois et al.\n      venue: COLM 2024\n      year: 2024\n      url: https://arxiv.org/abs/2404.04475\n      role: foundation\n      relevance: 指令遵循自动评测标准，Length-Controlled 版本修正长度偏差，为 ThreadGate 单轮指令评测提供对比基线\n      abstract: GLM-based length debiasing for AlpacaEval. Validated against 20K human annotations.\n    - title: 'WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild'\n      authors: Lin et al.\n      venue: arXiv 2024\n      year: 2024\n      url: https://arxiv.org/abs/2406.04770\n      role: foundation\n      relevance: 真实用户多样化指令集，评估 wild 场景指令遵循能力，与 ThreadGate 关注的真实多轮对话性能高度相关\n      abstract: 1,024 challenging tasks from 1M+ conversation logs. WB-Reward/WB-Score achieve 0.98 Pearson correlation with\n        Chatbot Arena ELO on hard tasks.\n    - title: 'MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues'\n      authors: Bai et al.\n      venue: ACL 2024\n      year: 2024\n      url: https://arxiv.org/abs/2402.14762\n      role: direct-competitor\n      relevance: 多轮对话细粒度评测体系，直接测量跨轮次能力退化，与 ThreadGate 研究的 GAR 衰减高度吻合\n      abstract: Three-tier ability taxonomy, 4,208 turns across 1,388 dialogues in 13 tasks. Neither alignment nor chat-specific\n        designs consistently improve multi-turn abilities.\n    - title: 'MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs'\n      authors: Sirdeshmukh et al.\n      venue: arXiv 2025\n      year: 2025\n      url: https://arxiv.org/abs/2501.17399\n      role: direct-competitor\n      relevance: 前沿 LLM 多轮对话准确率不足 50%，直接测量 ThreadGate 旨在修复的跨轮指令保留和上下文一致性失败\n      abstract: 'Four challenge categories: instruction retention, user inference memory, versioned editing, self-coherence.\n        All frontier LLMs below 50%; Claude 3.5 Sonnet tops at 41.4%.'\n  exposure_bias:\n    description: Exposure bias, teacher forcing, scheduled sampling, and train-test distribution mismatch in sequence generation\n    papers:\n    - title: Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\n      authors: Bengio, Vinyals, Jaitly, Shazeer\n      venue: NeurIPS 2015\n      year: 2015\n      url: https://arxiv.org/abs/1506.03099\n      role: foundation\n      relevance: Scheduled sampling 首次提出用 curriculum learning 缓解 teacher forcing 与推理时 autoregressive decoding 的分布不匹配（exposure\n        bias），直接支撑论文对 auxiliary attention loss 训练-推理 gap 的根因分析\n      abstract: Proposes a curriculum learning strategy to gently change training from fully guided (true previous token)\n        to less guided (model-generated token). The discrepancy between teacher-forced training and autoregressive inference\n        causes error accumulation. Experiments on sequence prediction tasks show significant improvements. Used in the winning\n        MSCOCO image captioning challenge 2015 entry.\n    - title: Sequence Level Training with Recurrent Neural Networks\n      authors: Ranzato, Chopra, Auli, Zaremba\n      venue: ICLR 2016\n      year: 2016\n      url: https://arxiv.org/abs/1511.06732\n      role: foundation\n      relevance: MIXER 算法直接优化测试时指标（BLEU/ROUGE）而非 token-level MLE，解决 teacher forcing 导致的 train-test discrepancy；论文中 auxiliary\n        loss 同样面临 token-level 训练目标与 sequence-level 推理行为的错位\n      abstract: Addresses the discrepancy between token-level MLE training and sequence-level generation at test time. Proposes\n        sequence level training that directly optimizes test metrics (BLEU, ROUGE). Outperforms strong baselines for greedy\n        generation on three tasks and is competitive with beam search while being several times faster.\n    - title: 'Professor Forcing: A New Algorithm for Training Recurrent Networks'\n      authors: Lamb, Goyal, Zhang, Zhang, Courville, Bengio\n      venue: NeurIPS 2016\n      year: 2016\n      url: https://arxiv.org/abs/1610.09038\n      role: foundation\n      relevance: 用对抗训练对齐 teacher forcing 训练与 free-running 采样的 hidden state 动态分布，直接证明 train-test dynamics mismatch 可导致长序列采样质量崩溃——与论文中\n        gating 机制推理时失效的现象高度对应\n      abstract: Introduces Professor Forcing, which uses adversarial domain adaptation to encourage the dynamics of the recurrent\n        network to be the same when training and when sampling over multiple time steps. Acts as a regularizer improving test\n        likelihood on Penn Treebank and sequential MNIST. Qualitatively improves samples especially for long generation horizons.\n        Discusses trade-offs with Scheduled Sampling.\n    - title: 'SEARNN: Training RNNs with Global-Local Losses'\n      authors: Leblond, Alayrac, Osokin, Lacoste-Julien\n      venue: ICLR 2018\n      year: 2018\n      url: https://arxiv.org/abs/1706.04499\n      role: context\n      relevance: 基于 learning-to-search 理论统一分析 MLE 训练的两大缺陷：exposure bias 和结构化损失信息浪费。论文中 auxiliary attention loss 同时受这两个缺陷影响——token-level\n        loss 无法反映 sequence-level attention pattern\n      abstract: Proposes SEARNN inspired by learning-to-search (L2S) approach to structured prediction. MLE training fails\n        to exploit structured losses and introduces train-test discrepancies (exposure bias). SEARNN leverages test-alike\n        search space exploration for global-local losses closer to test error. Demonstrates improvements on OCR, spelling\n        correction, and machine translation with a subsampling strategy for large vocabularies.\n    - title: Quantifying Exposure Bias for Neural Language Generation\n      authors: He, Zhang, Zhou, Glass\n      venue: arXiv 2019\n      year: 2019\n      url: https://arxiv.org/abs/1905.10617\n      role: foundation\n      relevance: 首次定量度量 exposure bias 影响并发现 LM 的 self-recovery 能力——即模型能从错误前缀部分恢复。这为论文分析 gating 机制在推理时的行为提供关键对照：如果 exposure\n        bias 可自恢复，auxiliary loss 崩溃可能源于更根本的分布偏移\n      abstract: 'Proposes sequence-level (EB-bleu) and word-level (EB-C) metrics to quantify exposure bias impact on quality,\n        diversity, and consistency. Key finding: contrary to popular belief, distortion from prefix discrepancy is limited\n        and does not appear incremental. Reveals an interesting self-recovery ability of language models that counters harmful\n        effects of exposure bias.'\n  gradient_conflict_mtl:\n    description: Multi-task gradient conflict resolution, gradient surgery, and loss balancing methods\n    papers:\n    - title: Gradient Surgery for Multi-Task Learning\n      authors: Yu, Kumar, Gupta, Levine, Hausman, Finn\n      venue: NeurIPS 2020\n      year: 2020\n      url: https://arxiv.org/abs/2001.06782\n      role: must-cite\n      relevance: 提出 PCGrad，通过投影消除任务间梯度冲突。论文直接使用 PCGrad 做因果排除实验，证明梯度冲突不是 auxiliary attention loss 泛化失败的根因\n      abstract: 'Proposes PCGrad: when gradients between tasks conflict, project one onto the normal plane of the other to\n        remove the conflicting component. Demonstrates consistent improvements on multi-task supervised learning and multi-task\n        reinforcement learning benchmarks.'\n    - title: 'GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks'\n      authors: Chen, Badrinarayanan, Lee, Rabinovich\n      venue: ICML 2018\n      year: 2018\n      url: https://arxiv.org/abs/1711.02257\n      role: must-cite\n      relevance: 首个自动平衡多任务梯度幅度的方法，通过动态调整各任务梯度范数使训练速率一致。为论文中 auxiliary loss 权重调优的 baseline 和梯度冲突缓解方法的早期代表\n      abstract: Automatically balances training in deep multitask models by dynamically tuning gradient magnitudes. Introduces\n        a loss-rate-based gradient normalization algorithm that adjusts gradients to ensure tasks train at similar rates.\n        Shows improvements on NYUv2 and other benchmarks.\n    - title: Conflict-Averse Gradient Descent for Multi-task Learning\n      authors: Liu, Liu, Jin, Stone, Liu\n      venue: NeurIPS 2021\n      year: 2021\n      url: https://arxiv.org/abs/2110.14048\n      role: context\n      relevance: 提出 CAGrad，在共享参数空间上寻找与所有任务梯度最小冲突的更新方向。作为 PCGrad 之后梯度冲突解决方法的演进，支撑论文对该路线充分覆盖后仍无法解决 attention degradation 的论证\n      abstract: Proposes Conflict-Averse Gradient descent (CAGrad) that minimizes the average loss while explicitly constraining\n        the worst-case task performance. Finds an update direction within a ball around the average gradient that maximizes\n        the minimum improvement across tasks. Achieves state-of-the-art on multi-task learning benchmarks.\n    - title: Multi-Task Learning as a Bargaining Game\n      authors: Navon, Shamsian, Achituve, Maron, Kawaguchi, Chechik, Fetaya\n      venue: ICML 2022\n      year: 2022\n      url: https://arxiv.org/abs/2202.01017\n      role: context\n      relevance: 将多任务梯度聚合建模为 Nash 博弈问题（Nash-MTL），理论证明 Nash 均衡解优于启发式梯度操作。作为梯度冲突解决的最新理论上界，强化论文\"即使最优梯度调和也无法修复 attention degradation\"的论证\n      abstract: Frames multi-task gradient aggregation as a bargaining game and proposes Nash-MTL that finds the Nash bargaining\n        solution. Provides theoretical guarantees showing the Nash solution is Pareto optimal. Achieves state-of-the-art on\n        multiple MTL benchmarks including NYUv2, QM9, and CELEBA.\n  residual_scaling:\n    description: Residual connection scaling, initialization, and zero-init methods for deep transformers\n    papers:\n    - title: 'ReZero is All You Need: Fast Convergence at Large Depth'\n      authors: Bachlechner, Majumder, Mao, Cottrell, McAuley\n      venue: UAI 2021\n      year: 2021\n      url: https://arxiv.org/abs/2003.04887\n      role: must-cite\n      relevance: ThreadGate 的 per-layer sigmoid gate 直接源自 ReZero 的零初始化残差缩放思想：x_{l+1} = x_l + alpha_l * f_l(x_l)，alpha 初始化为\n        0。ThreadGate 将标量 alpha 替换为 turn-conditioned sigmoid gate\n      abstract: Initializes each residual connection with a learnable zero-initialized parameter, enabling training of extremely\n        deep transformers (up to 10,000 layers) without warmup or normalization. Achieves significantly faster convergence\n        by allowing the network to start as identity and gradually incorporate layer contributions.\n    - title: 'Fixup Initialization: Residual Learning Without Normalization'\n      authors: Zhang, Dauphin, Ma\n      venue: ICLR 2019\n      year: 2019\n      url: https://arxiv.org/abs/1901.09321\n      role: foundation\n      relevance: 理论推导残差分支的初始化缩放如何控制梯度爆炸，为 ReZero 和 ThreadGate 的残差缩放设计提供数学基础。证明适当的残差缩放可完全替代 normalization layers\n      abstract: Proposes a properly scaled initialization for residual networks that enables training very deep models without\n        normalization layers. Theoretically shows that residual branch scaling by 1/sqrt(L) prevents gradient explosion. Matches\n        BatchNorm performance on ImageNet and CIFAR with ResNets up to 110 layers.\n",
      "numLines": 454,
      "startLine": 1,
      "totalLines": 454
    }
  },
  "sourceToolAssistantUUID": "adb39f79-617e-44d3-a8a0-eebeec1457b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "leafUuid": "5e05c331-706e-4b38-8b1f-cc3b31423f39",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Fill literature map with core related papers",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Assistant

_source line 20 · 2026-05-22T04:51:19.716Z_

<details><summary>Logged reasoning block</summary>

```text
The literature_map.yaml already has substantial content - it's not empty. It already has papers organized into categories: layer_importance, multi_turn_attention, residual_gating, attention_manipulation, theoretical_foundations, evaluation_benchmarks, exposure_bias, gradient_conflict_mtl, and residual_scaling.

Wait, let me re-read the task. It says "literature_map.yaml 当前为空" but clearly it's not empty - it has extensive content. Let me check if there's some other file or if the task is outdated.


Looking at what's already there, I can see the file has papers across multiple directions. Exposure bias already has several entries like Bengio 2015, Ranzato 2016, and others. Multi-turn attention has Dongre 2026, Laban 2025, Liu 2026, and more. I need to check what's still missing across the four required directions before adding new papers. Looking through paper_framing.md to see what references might be missing from the literature map, I'm checking each mention against what's already documented. It turns out all the key papers cited—from attention sinks and found-in-the-middle techniques to gated attention and transformer circuits—are already mapped in the YAML file, so there's nothing new to add here.

But I should dig deeper into what might actually be missing. Wiseman & Rush 2016 comes up in the exposure bias section of paper_framing.md but isn't in the literature map yet, and there are curriculum learning and scheduled sampling papers referenced in the bibliography that could be relevant to the research direction. I see the literature_map.yaml actually has entries already, so the task description saying it's empty seems inaccurate. But looking at what's referenced in paper_framing.md, there are papers mentioned that aren't captured yet—like Wiseman & Rush 2016 on sequence-to-sequence generation with exposure bias solutions. I should identify papers across the four directions that would strengthen the map, focusing on ones that are cited in the framing document but missing from the current literature map. I'm realizing I should cross-reference the papers mentioned in the framing document against what's already in the literature map, then use web search to identify and verify a few key papers that would fill gaps in the narrative.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e05c331-706e-4b38-8b1f-cc3b31423f39",
  "isSidechain": false,
  "requestId": "req_011CbH1H5g31exeE76kwY84L",
  "type": "assistant",
  "uuid": "70e67250-adde-4892-b8a4-6c59145fb85c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013swLohEDVYa7rYTQbdQGJB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24381,
      "cache_read_input_tokens": 24715,
      "output_tokens": 1776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24381,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1776,
          "cache_read_input_tokens": 24715,
          "cache_creation_input_tokens": 24381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24381
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

_source line 21 · 2026-05-22T04:51:20.569Z_

The literature_map.yaml already has substantial content across 8 categories. I'll identify gaps based on the paper_framing.md narrative and add papers that are referenced but missing, plus new highly relevant ones. Let me search for key papers mentioned in the framing that aren't yet in the map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70e67250-adde-4892-b8a4-6c59145fb85c",
  "isSidechain": false,
  "requestId": "req_011CbH1H5g31exeE76kwY84L",
  "type": "assistant",
  "uuid": "e0d26743-c440-4cfe-a289-5b3dbe436f58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013swLohEDVYa7rYTQbdQGJB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24381,
      "cache_read_input_tokens": 24715,
      "output_tokens": 1776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24381,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1776,
          "cache_read_input_tokens": 24715,
          "cache_creation_input_tokens": 24381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24381
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

_source line 22 · 2026-05-22T04:51:20.851Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Uh6PwZwAu3CrdqmaG7UMW1`</summary>

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
  "parentUuid": "e0d26743-c440-4cfe-a289-5b3dbe436f58",
  "isSidechain": false,
  "requestId": "req_011CbH1H5g31exeE76kwY84L",
  "type": "assistant",
  "uuid": "3c6a24a9-30f2-4819-b46c-a598682d550a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013swLohEDVYa7rYTQbdQGJB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24381,
      "cache_read_input_tokens": 24715,
      "output_tokens": 1776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24381,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1776,
          "cache_read_input_tokens": 24715,
          "cache_creation_input_tokens": 24381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24381
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

_source line 23 · 2026-05-22T04:51:20.855Z_

<details><summary>↩ Tool result · `toolu_01Uh6PwZwAu3CrdqmaG7UMW1`</summary>

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
  "parentUuid": "3c6a24a9-30f2-4819-b46c-a598682d550a",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "9daaba03-598b-495e-95a1-0b8a6fffaed6",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "3c6a24a9-30f2-4819-b46c-a598682d550a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-22T04:51:34.526Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me identify what's missing. Looking at the paper_framing.md:

1. **Wiseman & Rush 2016** - mentioned in SP1: "sequence generation 中有量化先例 (Ranzato et al. 2016, Wiseman & Rush 2016)" - NOT in literature_map or references.bib
2. **Zhang et al. 2019** - "Bridging the Gap between Training and Inference for Neural Machine Translation" - a key exposure bias mitigation paper for transformers, not in the map


3. **Arora et al. 2022** - a more recent exposure bias analysis that could strengthen the exposure bias direction, and I should check if there's transformer-specific scheduled sampling work beyond what's already covered with Bengio 2015.

For the four required directions, exposure bias already has solid coverage with five papers, but adding Wiseman & Rush and a transformer-era paper would fill gaps. The GAR/grounding/attention direction has Dongre, though I should verify if additional grounding work is needed.

Multi-turn dialogue attention mechanisms could benefit from something beyond Liu 2023, and scheduled sampling needs Zhang et al. 2019 on bridging training-inference gaps for neural machine translation. Let me search for these specific papers and any recent LLM exposure bias work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9daaba03-598b-495e-95a1-0b8a6fffaed6",
  "isSidechain": false,
  "requestId": "req_011CbH1KrmUdGMNdqbbcjox6",
  "type": "assistant",
  "uuid": "4648b85d-e04f-4935-bcdb-09a1ab67f71b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019T27pLLhe35oSs5RDmmcz3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2299,
      "cache_read_input_tokens": 49096,
      "output_tokens": 729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2299,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 729,
          "cache_read_input_tokens": 49096,
          "cache_creation_input_tokens": 2299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2299
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

_source line 25 · 2026-05-22T04:51:34.537Z_

Let me search for papers referenced in paper_framing.md but missing from the literature map, plus additional relevant ones.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4648b85d-e04f-4935-bcdb-09a1ab67f71b",
  "isSidechain": false,
  "requestId": "req_011CbH1KrmUdGMNdqbbcjox6",
  "type": "assistant",
  "uuid": "638728ca-9209-4d2c-af24-704e594ddf32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019T27pLLhe35oSs5RDmmcz3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2299,
      "cache_read_input_tokens": 49096,
      "output_tokens": 729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2299,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 729,
          "cache_read_input_tokens": 49096,
          "cache_creation_input_tokens": 2299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2299
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

_source line 26 · 2026-05-22T04:51:34.589Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QrpjMbdHF9R65DVd6c9cqB`</summary>

```json
{
  "query": "Wiseman Rush 2016 \"Sequence-to-Sequence Generation\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "638728ca-9209-4d2c-af24-704e594ddf32",
  "isSidechain": false,
  "requestId": "req_011CbH1KrmUdGMNdqbbcjox6",
  "type": "assistant",
  "uuid": "8e22f827-7d2a-4099-8f72-53871f145384",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019T27pLLhe35oSs5RDmmcz3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2299,
      "cache_read_input_tokens": 49096,
      "output_tokens": 729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2299,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 729,
          "cache_read_input_tokens": 49096,
          "cache_creation_input_tokens": 2299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2299
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

_source line 27 · 2026-05-22T04:51:34.823Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016k258otDPTAxuij6vydgn9`</summary>

```json
{
  "query": "Zhang et al 2019 \"Bridging the Gap between Training and Inference\" neural machine translation exposure bias arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e22f827-7d2a-4099-8f72-53871f145384",
  "isSidechain": false,
  "requestId": "req_011CbH1KrmUdGMNdqbbcjox6",
  "type": "assistant",
  "uuid": "4bcba544-1ea3-40f9-ae87-29a542b061b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019T27pLLhe35oSs5RDmmcz3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2299,
      "cache_read_input_tokens": 49096,
      "output_tokens": 729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2299,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 729,
          "cache_read_input_tokens": 49096,
          "cache_creation_input_tokens": 2299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2299
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

_source line 28 · 2026-05-22T04:51:34.931Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NF8fNhEsbra5L3xzDAq3Ns`</summary>

```json
{
  "query": "Arora et al 2022 \"Exposure Bias versus Self-Recovery\" language generation arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bcba544-1ea3-40f9-ae87-29a542b061b2",
  "isSidechain": false,
  "requestId": "req_011CbH1KrmUdGMNdqbbcjox6",
  "type": "assistant",
  "uuid": "800de696-7cd3-4841-8fbf-1497a5eb46f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019T27pLLhe35oSs5RDmmcz3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2299,
      "cache_read_input_tokens": 49096,
      "output_tokens": 729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2299,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 729,
          "cache_read_input_tokens": 49096,
          "cache_creation_input_tokens": 2299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2299
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

_source line 29 · 2026-05-22T04:51:39.114Z_

<details><summary>↩ Tool result · `toolu_01QrpjMbdHF9R65DVd6c9cqB`</summary>

```text
Web search results for query: "Wiseman Rush 2016 "Sequence-to-Sequence Generation" arxiv"

Links: [{"title":"[1701.06549] Learning to Decode for Future Success","url":"https://ar5iv.labs.arxiv.org/html/1701.06549"},{"title":"Sequence-to-Sequence Learning as Beam-Search Optimization - ACL Anthology","url":"https://aclanthology.org/D16-1137/"},{"title":"arXiv:1901.06283v1 [cs.CL] 18 Jan 2019","url":"https://arxiv.org/pdf/1901.06283"},{"title":"[1606.02960] Sequence-to-Sequence Learning as Beam-Search Optimization","url":"https://arxiv.org/abs/1606.02960"},{"title":"Sequence-to-Sequence Learning as Beam-Search Optimization","url":"https://www.researchgate.net/publication/311990355_Sequence-to-Sequence_Learning_as_Beam-Search_Optimization"},{"title":"[PDF] Sequence-to-Sequence Learning as Beam-Search Optimization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sequence-to-Sequence-Learning-as-Beam-Search-Wiseman-Rush/5507dc32b368c8afd3b9507e9b5888da7bd7d7cd"},{"title":"Seq2seq Dependency Parsing","url":"https://aclanthology.org/C18-1271.pdf"},{"title":"Sequence-to-Sequence Learning as Beam-Search ...","url":"https://aclanthology.org/D16-1137.pdf"},{"title":"Sequence-to-Sequence Learning as Beam-Search Optimization | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/1606.02960"}]

Based on the search results, I found the paper you're looking for:

"Sequence-to-Sequence Learning as Beam-Search Optimization" by Sam Wiseman and Alexander M. Rush, published in 2016 in the Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing.

The arXiv identifier for this paper is arXiv:1606.02960.

The work introduces a model and beam-search training scheme that extends seq2seq to learn global sequence scores, avoiding classical biases associated with local training and unifying the training loss with test-time usage. The system outperforms attention-based seq2seq baselines on three sequence-to-sequence tasks: word ordering, parsing, and machine translation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e22f827-7d2a-4099-8f72-53871f145384",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "9bdaade0-5951-4f1c-8830-27db7e98f441",
  "toolUseResult": {
    "query": "Wiseman Rush 2016 \"Sequence-to-Sequence Generation\" arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NGiKJ3XkiZxX1Bup9rCaVE",
        "content": [
          {
            "title": "[1701.06549] Learning to Decode for Future Success",
            "url": "https://ar5iv.labs.arxiv.org/html/1701.06549"
          },
          {
            "title": "Sequence-to-Sequence Learning as Beam-Search Optimization - ACL Anthology",
            "url": "https://aclanthology.org/D16-1137/"
          },
          {
            "title": "arXiv:1901.06283v1 [cs.CL] 18 Jan 2019",
            "url": "https://arxiv.org/pdf/1901.06283"
          },
          {
            "title": "[1606.02960] Sequence-to-Sequence Learning as Beam-Search Optimization",
            "url": "https://arxiv.org/abs/1606.02960"
          },
          {
            "title": "Sequence-to-Sequence Learning as Beam-Search Optimization",
            "url": "https://www.researchgate.net/publication/311990355_Sequence-to-Sequence_Learning_as_Beam-Search_Optimization"
          },
          {
            "title": "[PDF] Sequence-to-Sequence Learning as Beam-Search Optimization | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Sequence-to-Sequence-Learning-as-Beam-Search-Wiseman-Rush/5507dc32b368c8afd3b9507e9b5888da7bd7d7cd"
          },
          {
            "title": "Seq2seq Dependency Parsing",
            "url": "https://aclanthology.org/C18-1271.pdf"
          },
          {
            "title": "Sequence-to-Sequence Learning as Beam-Search ...",
            "url": "https://aclanthology.org/D16-1137.pdf"
          },
          {
            "title": "Sequence-to-Sequence Learning as Beam-Search Optimization | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/1606.02960"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"Sequence-to-Sequence Learning as Beam-Search Optimization\" by Sam Wiseman and Alexander M. Rush, published in 2016 in the Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing.\n\nThe arXiv identifier for this paper is arXiv:1606.02960.\n\nThe work introduces a model and beam-search training scheme that extends seq2seq to learn global sequence scores, avoiding classical biases associated with local training and unifying the training loss with test-time usage. The system outperforms attention-based seq2seq baselines on three sequence-to-sequence tasks: word ordering, parsing, and machine translation."
    ],
    "durationSeconds": 4.518839637000012
  },
  "sourceToolAssistantUUID": "8e22f827-7d2a-4099-8f72-53871f145384",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T04:51:42.927Z_

<details><summary>↩ Tool result · `toolu_01NF8fNhEsbra5L3xzDAq3Ns`</summary>

```text
Web search results for query: "Arora et al 2022 "Exposure Bias versus Self-Recovery" language generation arxiv"

Links: [{"title":"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation? | Request PDF","url":"https://www.researchgate.net/publication/357121582_Exposure_Bias_versus_Self-Recovery_Are_Distortions_Really_Incremental_for_Autoregressive_Text_Generation"},{"title":"[PDF] Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Exposure-Bias-versus-Self-Recovery:-Are-Distortions-He-Zhang/cb51b53d5d26537ed6d458f83b81afe0f2efa289"},{"title":"Mitigating the Learning Bias towards Repetition by Self-Contrastive Training for Open-Ended Generation","url":"https://arxiv.org/html/2307.01542"},{"title":"Exposure Bias versus Self-Recovery:","url":"https://arxiv.org/pdf/1905.10617"},{"title":"(PDF) Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation","url":"https://www.researchgate.net/publication/359729383_Why_Exposure_Bias_Matters_An_Imitation_Learning_Perspective_of_Error_Accumulation_in_Language_Generation"},{"title":"[1905.10617] Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?","url":"https://arxiv.org/abs/1905.10617"},{"title":"[1905.10617v4] Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/abs/1905.10617v4"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of Error   Accumulation in Language Generation","url":"https://arxiv.org/pdf/2204.01171"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of...","url":"https://arxiv.org/abs/2204.01171"},{"title":"Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/pdf/1905.10617v4"}]

I found information about papers related to your query. There appear to be two related papers that may match what you're looking for:

1. **"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?"** - by Tianxing He and others. This paper addresses exposure bias as a central problem for auto-regressive language models, where teacher forcing causes test-time generation to be incrementally distorted due to training-generation discrepancy. The authors identify the self-recovery ability of MLE-trained language models and propose sequence-level (EB-bleu) and word-level (EB-C) metrics to quantify the impact of exposure bias. This paper has arXiv ID 1905.10617.

2. **"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation"** - by Kushal Arora, Layla El Asri, Hareesh Bahuleyan, and Jackie Chi Kit Cheung, published in Findings of the Association for Computational Linguistics: ACL 2022, pages 700–710. This paper is related to the Arora et al. 2022 citation you mentioned.

Both papers examine exposure bias and self-recovery in language generation, which aligns with your query terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "800de696-7cd3-4841-8fbf-1497a5eb46f1",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "e1b1614d-010a-4a60-aa15-0930c5a782b3",
  "toolUseResult": {
    "query": "Arora et al 2022 \"Exposure Bias versus Self-Recovery\" language generation arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_017YqRcV8q3B3sz6HaBp8qrd",
        "content": [
          {
            "title": "Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation? | Request PDF",
            "url": "https://www.researchgate.net/publication/357121582_Exposure_Bias_versus_Self-Recovery_Are_Distortions_Really_Incremental_for_Autoregressive_Text_Generation"
          },
          {
            "title": "[PDF] Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation? | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Exposure-Bias-versus-Self-Recovery:-Are-Distortions-He-Zhang/cb51b53d5d26537ed6d458f83b81afe0f2efa289"
          },
          {
            "title": "Mitigating the Learning Bias towards Repetition by Self-Contrastive Training for Open-Ended Generation",
            "url": "https://arxiv.org/html/2307.01542"
          },
          {
            "title": "Exposure Bias versus Self-Recovery:",
            "url": "https://arxiv.org/pdf/1905.10617"
          },
          {
            "title": "(PDF) Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation",
            "url": "https://www.researchgate.net/publication/359729383_Why_Exposure_Bias_Matters_An_Imitation_Learning_Perspective_of_Error_Accumulation_in_Language_Generation"
          },
          {
            "title": "[1905.10617] Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?",
            "url": "https://arxiv.org/abs/1905.10617"
          },
          {
            "title": "[1905.10617v4] Quantifying Exposure Bias for Neural Language Generation",
            "url": "https://arxiv.org/abs/1905.10617v4"
          },
          {
            "title": "Why Exposure Bias Matters: An Imitation Learning Perspective of Error   Accumulation in Language Generation",
            "url": "https://arxiv.org/pdf/2204.01171"
          },
          {
            "title": "Why Exposure Bias Matters: An Imitation Learning Perspective of...",
            "url": "https://arxiv.org/abs/2204.01171"
          },
          {
            "title": "Quantifying Exposure Bias for Neural Language Generation",
            "url": "https://arxiv.org/pdf/1905.10617v4"
          }
        ]
      },
      "I found information about papers related to your query. There appear to be two related papers that may match what you're looking for:\n\n1. **\"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?\"** - by Tianxing He and others. This paper addresses exposure bias as a central problem for auto-regressive language models, where teacher forcing causes test-time generation to be incrementally distorted due to training-generation discrepancy. The authors identify the self-recovery ability of MLE-trained language models and propose sequence-level (EB-bleu) and word-level (EB-C) metrics to quantify the impact of exposure bias. This paper has arXiv ID 1905.10617.\n\n2. **\"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation\"** - by Kushal Arora, Layla El Asri, Hareesh Bahuleyan, and Jackie Chi Kit Cheung, published in Findings of the Association for Computational Linguistics: ACL 2022, pages 700–710. This paper is related to the Arora et al. 2022 citation you mentioned.\n\nBoth papers examine exposure bias and self-recovery in language generation, which aligns with your query terms."
    ],
    "durationSeconds": 7.992223836000004
  },
  "sourceToolAssistantUUID": "800de696-7cd3-4841-8fbf-1497a5eb46f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "leafUuid": "e1b1614d-010a-4a60-aa15-0930c5a782b3",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Fill literature map with core related papers",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Tool result

_source line 33 · 2026-05-22T04:51:46.366Z_

<details><summary>↩ Tool result · `toolu_016k258otDPTAxuij6vydgn9`</summary>

```text
Web search results for query: "Zhang et al 2019 "Bridging the Gap between Training and Inference" neural machine translation exposure bias arxiv"

Links: [{"title":"Bridging the Gap between Learning and Inference for Diffusion-Based Molecule Generation","url":"https://arxiv.org/html/2411.05472v1"},{"title":"Bridging the Gap between Training and Inference for Neural Machine Translation | Request PDF","url":"https://www.researchgate.net/publication/335778783_Bridging_the_Gap_between_Training_and_Inference_for_Neural_Machine_Translation"},{"title":"(PDF) Bridging the Data Gap between Training and Inference for Unsupervised Neural Machine Translation","url":"https://www.researchgate.net/publication/361063097_Bridging_the_Data_Gap_between_Training_and_Inference_for_Unsupervised_Neural_Machine_Translation"},{"title":"[1906.02448] Bridging the Gap between Training and Inference for Neural Machine Translation","url":"https://arxiv.org/abs/1906.02448"},{"title":"Bridging the Gap between Training and Inference for Neural Machine Translation - ACL Anthology","url":"https://aclanthology.org/P19-1426/"},{"title":"On Exposure Bias, Hallucination and Domain Shift in Neural Machine   Translation","url":"https://arxiv.org/pdf/2005.03642"},{"title":"Bridging the Gap between Training and Inference for Neural Machine   Translation","url":"https://arxiv.org/pdf/1906.02448"},{"title":"Bridging the Gap between Training and Inference for ...","url":"https://aclanthology.org/P19-1426.pdf"}]

Based on the search results, I found the paper you're looking for:

**"Bridging the Gap between Training and Inference for Neural Machine Translation"** by Wen Zhang, Yang Feng, Fandong Meng, Di You, and Qun Liu (2019).

The paper was published in the Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, pages 4334–4343, Florence, Italy.

The paper addresses exposure bias in neural machine translation. At training time ground truth words are used as context while at inference the entire sequence is generated by the model, resulting in predicted words drawn from different distributions—a discrepancy called exposure bias.

The authors address these issues by sampling context words not only from the ground truth sequence but also from the predicted sequence by the model during training, where the predicted sequence is selected with a sentence-level optimum. Their approach achieved significant improvements on Chinese->English and WMT'14 English->German translation tasks.

The paper is available on arXiv (1906.02448) and through the ACL Anthology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bcba544-1ea3-40f9-ae87-29a542b061b2",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "121b19cb-2031-450a-8979-08482c64bf09",
  "toolUseResult": {
    "query": "Zhang et al 2019 \"Bridging the Gap between Training and Inference\" neural machine translation exposure bias arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LdmutM22EtmN26JhPRmBmd",
        "content": [
          {
            "title": "Bridging the Gap between Learning and Inference for Diffusion-Based Molecule Generation",
            "url": "https://arxiv.org/html/2411.05472v1"
          },
          {
            "title": "Bridging the Gap between Training and Inference for Neural Machine Translation | Request PDF",
            "url": "https://www.researchgate.net/publication/335778783_Bridging_the_Gap_between_Training_and_Inference_for_Neural_Machine_Translation"
          },
          {
            "title": "(PDF) Bridging the Data Gap between Training and Inference for Unsupervised Neural Machine Translation",
            "url": "https://www.researchgate.net/publication/361063097_Bridging_the_Data_Gap_between_Training_and_Inference_for_Unsupervised_Neural_Machine_Translation"
          },
          {
            "title": "[1906.02448] Bridging the Gap between Training and Inference for Neural Machine Translation",
            "url": "https://arxiv.org/abs/1906.02448"
          },
          {
            "title": "Bridging the Gap between Training and Inference for Neural Machine Translation - ACL Anthology",
            "url": "https://aclanthology.org/P19-1426/"
          },
          {
            "title": "On Exposure Bias, Hallucination and Domain Shift in Neural Machine   Translation",
            "url": "https://arxiv.org/pdf/2005.03642"
          },
          {
            "title": "Bridging the Gap between Training and Inference for Neural Machine   Translation",
            "url": "https://arxiv.org/pdf/1906.02448"
          },
          {
            "title": "Bridging the Gap between Training and Inference for ...",
            "url": "https://aclanthology.org/P19-1426.pdf"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**\"Bridging the Gap between Training and Inference for Neural Machine Translation\"** by Wen Zhang, Yang Feng, Fandong Meng, Di You, and Qun Liu (2019).\n\nThe paper was published in the Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, pages 4334–4343, Florence, Italy.\n\nThe paper addresses exposure bias in neural machine translation. At training time ground truth words are used as context while at inference the entire sequence is generated by the model, resulting in predicted words drawn from different distributions—a discrepancy called exposure bias.\n\nThe authors address these issues by sampling context words not only from the ground truth sequence but also from the predicted sequence by the model during training, where the predicted sequence is selected with a sentence-level optimum. Their approach achieved significant improvements on Chinese->English and WMT'14 English->German translation tasks.\n\nThe paper is available on arXiv (1906.02448) and through the ACL Anthology."
    ],
    "durationSeconds": 11.538816680000004
  },
  "sourceToolAssistantUUID": "4bcba544-1ea3-40f9-ae87-29a542b061b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-22T04:51:46.372Z_

```json
{
  "parentUuid": "121b19cb-2031-450a-8979-08482c64bf09",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3a324639-29d3-4daf-b987-a0389a04a50d",
  "timestamp": "2026-05-22T04:51:46.372Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 35 · 2026-05-22T04:51:52.665Z_

<details><summary>Logged reasoning block</summary>

```text
Good. I found several papers. Let me now search for more:

1. Wiseman & Rush 2016 - "Sequence-to-Sequence Learning as Beam-Search Optimization" - arXiv:1606.02960, EMNLP 2016
2. Zhang et al. 2019 - "Bridging the Gap between Training and Inference for Neural Machine Translation" - arXiv:1906.02448, ACL 2019
3. Arora et al. 2022 - "Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation" - arXiv:2204.01171, ACL Findings 2022


4. I should look for papers covering grounding and attention mechanisms, recent work on multi-turn dialogue systems, and curriculum learning approaches for transformers to round out the coverage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a324639-29d3-4daf-b987-a0389a04a50d",
  "isSidechain": false,
  "requestId": "req_011CbH1MjZwi9TbAU6Cv9WEw",
  "type": "assistant",
  "uuid": "1da49c09-f922-4927-b5ab-742f091cfeb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Ut494tgUjuYkoA9PP7zVD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 952,
      "cache_creation_input_tokens": 2224,
      "cache_read_input_tokens": 51395,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 952,
          "output_tokens": 390,
          "cache_read_input_tokens": 51395,
          "cache_creation_input_tokens": 2224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2224
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

_source line 36 · 2026-05-22T04:51:52.803Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017rJ967LXBZf6kwiSsBfPEd`</summary>

```json
{
  "query": "Arora 2022 \"Why Exposure Bias Matters\" imitation learning error accumulation arxiv 2204.01171"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1da49c09-f922-4927-b5ab-742f091cfeb0",
  "isSidechain": false,
  "requestId": "req_011CbH1MjZwi9TbAU6Cv9WEw",
  "type": "assistant",
  "uuid": "a973071e-e409-45f6-87c3-d8180aed3fe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Ut494tgUjuYkoA9PP7zVD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 952,
      "cache_creation_input_tokens": 2224,
      "cache_read_input_tokens": 51395,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 952,
          "output_tokens": 390,
          "cache_read_input_tokens": 51395,
          "cache_creation_input_tokens": 2224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2224
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

_source line 37 · 2026-05-22T04:51:52.882Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MG18F9StoKEAeSVXrTBh41`</summary>

```json
{
  "query": "scheduled sampling transformer \"curriculum learning\" exposure bias mitigation 2020 2021 2022 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a973071e-e409-45f6-87c3-d8180aed3fe1",
  "isSidechain": false,
  "requestId": "req_011CbH1MjZwi9TbAU6Cv9WEw",
  "type": "assistant",
  "uuid": "13c071ac-63b9-4f41-bb1d-c24e559e1127",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Ut494tgUjuYkoA9PP7zVD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 952,
      "cache_creation_input_tokens": 2224,
      "cache_read_input_tokens": 51395,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 952,
          "output_tokens": 390,
          "cache_read_input_tokens": 51395,
          "cache_creation_input_tokens": 2224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2224
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

_source line 38 · 2026-05-22T04:51:57.374Z_

<details><summary>↩ Tool result · `toolu_017rJ967LXBZf6kwiSsBfPEd`</summary>

```text
Web search results for query: "Arora 2022 "Why Exposure Bias Matters" imitation learning error accumulation arxiv 2204.01171"

Links: [{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of...","url":"https://arxiv.org/abs/2204.01171"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation - ACL Anthology","url":"https://aclanthology.org/2022.findings-acl.58/"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation | Request PDF","url":"https://www.researchgate.net/publication/361063299_Why_Exposure_Bias_Matters_An_Imitation_Learning_Perspective_of_Error_Accumulation_in_Language_Generation"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation - Publication | RBC Borealis","url":"https://rbcborealis.com/publications/why-exposure-bias-matters-imitation-learning-perspective-error-accumulation-language-generation/"},{"title":"(PDF) Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation","url":"https://www.researchgate.net/publication/359729383_Why_Exposure_Bias_Matters_An_Imitation_Learning_Perspective_of_Error_Accumulation_in_Language_Generation"},{"title":"[PDF] Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Why-Exposure-Bias-Matters:-An-Imitation-Learning-of-Arora-Asri/0e3d6a7c9c04cf3ba9c902724548846a5ade04b4"},{"title":"dblp: Hareesh Bahuleyan","url":"https://dblp.org/pid/203/9500.html"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of Error","url":"https://arxiv.org/pdf/2204.01171"}]

I found the paper you're looking for. Here's what I found:

The paper is titled "Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation" by Kushal Arora, Layla El Asri, Hareesh Bahuleyan, and Jackie Chi Kit Cheung, with arXiv identifier 2204.01171.

The paper shows that exposure bias leads to an accumulation of errors, analyzes why perplexity fails to capture this accumulation, and empirically shows that this accumulation results in poor generation quality. The hypothesis being verified is that the brittleness of generation models is caused by the training and generation procedure mismatch, also referred to as exposure bias.

The paper was published in the Findings of the Association for Computational Linguistics: ACL 2022.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a973071e-e409-45f6-87c3-d8180aed3fe1",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "ed5787f0-8a61-46c6-a419-fa8c2ae603bf",
  "toolUseResult": {
    "query": "Arora 2022 \"Why Exposure Bias Matters\" imitation learning error accumulation arxiv 2204.01171",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DKbxahWFP5AoUf1NCy2QxP",
        "content": [
          {
            "title": "Why Exposure Bias Matters: An Imitation Learning Perspective of...",
            "url": "https://arxiv.org/abs/2204.01171"
          },
          {
            "title": "Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation - ACL Anthology",
            "url": "https://aclanthology.org/2022.findings-acl.58/"
          },
          {
            "title": "Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation | Request PDF",
            "url": "https://www.researchgate.net/publication/361063299_Why_Exposure_Bias_Matters_An_Imitation_Learning_Perspective_of_Error_Accumulation_in_Language_Generation"
          },
          {
            "title": "Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation - Publication | RBC Borealis",
            "url": "https://rbcborealis.com/publications/why-exposure-bias-matters-imitation-learning-perspective-error-accumulation-language-generation/"
          },
          {
            "title": "(PDF) Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation",
            "url": "https://www.researchgate.net/publication/359729383_Why_Exposure_Bias_Matters_An_Imitation_Learning_Perspective_of_Error_Accumulation_in_Language_Generation"
          },
          {
            "title": "[PDF] Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Why-Exposure-Bias-Matters:-An-Imitation-Learning-of-Arora-Asri/0e3d6a7c9c04cf3ba9c902724548846a5ade04b4"
          },
          {
            "title": "dblp: Hareesh Bahuleyan",
            "url": "https://dblp.org/pid/203/9500.html"
          },
          {
            "title": "Why Exposure Bias Matters: An Imitation Learning Perspective of Error",
            "url": "https://arxiv.org/pdf/2204.01171"
          }
        ]
      },
      "I found the paper you're looking for. Here's what I found:\n\nThe paper is titled \"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation\" by Kushal Arora, Layla El Asri, Hareesh Bahuleyan, and Jackie Chi Kit Cheung, with arXiv identifier 2204.01171.\n\nThe paper shows that exposure bias leads to an accumulation of errors, analyzes why perplexity fails to capture this accumulation, and empirically shows that this accumulation results in poor generation quality. The hypothesis being verified is that the brittleness of generation models is caused by the training and generation procedure mismatch, also referred to as exposure bias.\n\nThe paper was published in the Findings of the Association for Computational Linguistics: ACL 2022."
    ],
    "durationSeconds": 4.565294520000011
  },
  "sourceToolAssistantUUID": "a973071e-e409-45f6-87c3-d8180aed3fe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-22T04:52:01.424Z_

<details><summary>↩ Tool result · `toolu_01MG18F9StoKEAeSVXrTBh41`</summary>

```text
Web search results for query: "scheduled sampling transformer "curriculum learning" exposure bias mitigation 2020 2021 2022 arxiv"

Links: [{"title":"Scheduled Sampling in Sequence Prediction","url":"https://www.emergentmind.com/topics/scheduled-sampling"},{"title":"[PDF] Scheduled Sampling for Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scheduled-Sampling-for-Transformers-Mihaylova-Martins/6b6befbff611ddc98ef268b3c51353593bb07e77"},{"title":"[1906.07651v1] Scheduled Sampling for Transformers","url":"https://arxiv.org/abs/1906.07651v1"},{"title":"[1906.07651] Scheduled Sampling for Transformers","url":"https://arxiv.org/abs/1906.07651"},{"title":"[2108.12963] Scheduled Sampling Based on Decoding Steps for Neural Machine Translation","url":"https://arxiv.org/abs/2108.12963"},{"title":"[2210.08959] Flipped Classroom: Effective Teaching for Time Series Forecasting","url":"https://arxiv.org/abs/2210.08959"},{"title":"Dynamic Scheduled Sampling with Imitation Loss for Neural Text   Generation","url":"https://arxiv.org/pdf/2301.13753"},{"title":"[2107.10427v1] Confidence-Aware Scheduled Sampling for Neural Machine Translation","url":"https://arxiv.org/abs/2107.10427v1"}]

I found several relevant research papers on scheduled sampling, transformers, curriculum learning, and exposure bias mitigation. Here are the key findings:

## Core Research Papers

**Scheduled Sampling for Transformers (2019)**
Scheduled sampling is a technique for avoiding exposure bias in sequence-to-sequence generation, consisting of feeding the model a mix of teacher forced embeddings and model predictions from the previous step in training time. The paper proposes structural changes to allow scheduled sampling to be applied to Transformer architecture via a two-pass decoding strategy.

**Recent Variants (2021-2022)**

Scheduled sampling is widely used to mitigate the exposure bias problem for neural machine translation by replacing ground-truth tokens with predicted tokens to bridge the gap between training and inference. 

Two notable 2021 papers on arXiv include:

1. **Scheduled Sampling Based on Decoding Steps** (August 2021, arXiv 2108.12963): This proposes scheduled sampling methods based on decoding steps, increasing the selection chance of predicted tokens with decoding step growth to more realistically simulate the inference scene during training.

2. **Confidence-Aware Scheduled Sampling** (July 2021, arXiv 2107.10427): This designs fine-grained schedule strategies by quantifying real-time model competence through prediction confidence, exposing the model to predicted tokens for high-confidence positions while using ground-truth tokens for low-confidence positions.

**2022-2023 Extensions**

Scheduled sampling is a curriculum learning strategy that gradually exposes the model to its own predictions during training to mitigate exposure bias. A 2023 paper (arXiv 2301.13753) explores dynamic scheduled sampling with imitation loss for neural text generation.

These papers address the fundamental mismatch between training (using ground-truth tokens) and inference (using model-generated tokens) through curriculum learning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13c071ac-63b9-4f41-bb1d-c24e559e1127",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "623787cc-30bd-42fe-9541-bf7516ccd28c",
  "toolUseResult": {
    "query": "scheduled sampling transformer \"curriculum learning\" exposure bias mitigation 2020 2021 2022 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EHeUB86hJQYen3uinDUKfK",
        "content": [
          {
            "title": "Scheduled Sampling in Sequence Prediction",
            "url": "https://www.emergentmind.com/topics/scheduled-sampling"
          },
          {
            "title": "[PDF] Scheduled Sampling for Transformers | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Scheduled-Sampling-for-Transformers-Mihaylova-Martins/6b6befbff611ddc98ef268b3c51353593bb07e77"
          },
          {
            "title": "[1906.07651v1] Scheduled Sampling for Transformers",
            "url": "https://arxiv.org/abs/1906.07651v1"
          },
          {
            "title": "[1906.07651] Scheduled Sampling for Transformers",
            "url": "https://arxiv.org/abs/1906.07651"
          },
          {
            "title": "[2108.12963] Scheduled Sampling Based on Decoding Steps for Neural Machine Translation",
            "url": "https://arxiv.org/abs/2108.12963"
          },
          {
            "title": "[2210.08959] Flipped Classroom: Effective Teaching for Time Series Forecasting",
            "url": "https://arxiv.org/abs/2210.08959"
          },
          {
            "title": "Dynamic Scheduled Sampling with Imitation Loss for Neural Text   Generation",
            "url": "https://arxiv.org/pdf/2301.13753"
          },
          {
            "title": "[2107.10427v1] Confidence-Aware Scheduled Sampling for Neural Machine Translation",
            "url": "https://arxiv.org/abs/2107.10427v1"
          }
        ]
      },
      "I found several relevant research papers on scheduled sampling, transformers, curriculum learning, and exposure bias mitigation. Here are the key findings:\n\n## Core Research Papers\n\n**Scheduled Sampling for Transformers (2019)**\nScheduled sampling is a technique for avoiding exposure bias in sequence-to-sequence generation, consisting of feeding the model a mix of teacher forced embeddings and model predictions from the previous step in training time. The paper proposes structural changes to allow scheduled sampling to be applied to Transformer architecture via a two-pass decoding strategy.\n\n**Recent Variants (2021-2022)**\n\nScheduled sampling is widely used to mitigate the exposure bias problem for neural machine translation by replacing ground-truth tokens with predicted tokens to bridge the gap between training and inference. \n\nTwo notable 2021 papers on arXiv include:\n\n1. **Scheduled Sampling Based on Decoding Steps** (August 2021, arXiv 2108.12963): This proposes scheduled sampling methods based on decoding steps, increasing the selection chance of predicted tokens with decoding step growth to more realistically simulate the inference scene during training.\n\n2. **Confidence-Aware Scheduled Sampling** (July 2021, arXiv 2107.10427): This designs fine-grained schedule strategies by quantifying real-time model competence through prediction confidence, exposing the model to predicted tokens for high-confidence positions while using ground-truth tokens for low-confidence positions.\n\n**2022-2023 Extensions**\n\nScheduled sampling is a curriculum learning strategy that gradually exposes the model to its own predictions during training to mitigate exposure bias. A 2023 paper (arXiv 2301.13753) explores dynamic scheduled sampling with imitation loss for neural text generation.\n\nThese papers address the fundamental mismatch between training (using ground-truth tokens) and inference (using model-generated tokens) through curriculum learning approaches."
    ],
    "durationSeconds": 8.538356329000003
  },
  "sourceToolAssistantUUID": "13c071ac-63b9-4f41-bb1d-c24e559e1127",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-22T04:52:16.048Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I found:
1. Wiseman & Rush 2016 - "Sequence-to-Sequence Learning as Beam-Search Optimization" - arXiv:1606.02960, EMNLP 2016
2. Zhang et al. 2019 - "Bridging the Gap between Training and Inference for Neural Machine Translation" - arXiv:1906.02448, ACL 2019
3. Arora et al. 2022 - "Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation" - arXiv:2204.01171, ACL Findings 2022


4. Mihaylova & Martins 2019 - "Scheduled Sampling for Transformers" - arXiv:1906.07651

Now I need to find papers covering the other directions—something on grounding and attention mechanisms, plus multi-turn dialogue attention. Let me look for work on instruction-following or goal-conditioned generation that isn't already represented in my map.

Checking my coverage: exposure bias is handled, scheduled sampling is covered, but I'm missing something on how system prompts and initial instructions persist (or fail to persist) through long conversations. That seems like a natural fit for the grounding direction. I should also consider papers on attention regularization or auxiliary losses in transformers that might strengthen the framework.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "623787cc-30bd-42fe-9541-bf7516ccd28c",
  "isSidechain": false,
  "requestId": "req_011CbH1Nr2Ar9zHTe2rmaRWw",
  "type": "assistant",
  "uuid": "0df15935-67ab-4690-85f3-665ebb56806e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPuw4DwgQcELBSrmY7Jbi1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3000,
      "cache_read_input_tokens": 53619,
      "output_tokens": 753,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3000,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 753,
          "cache_read_input_tokens": 53619,
          "cache_creation_input_tokens": 3000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3000
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

_source line 41 · 2026-05-22T04:52:16.117Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JwuNTKRfS1R2MokiiHq25M`</summary>

```json
{
  "query": "auxiliary attention loss supervision transformer training \"attention regularization\" 2023 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0df15935-67ab-4690-85f3-665ebb56806e",
  "isSidechain": false,
  "requestId": "req_011CbH1Nr2Ar9zHTe2rmaRWw",
  "type": "assistant",
  "uuid": "e4300eed-497b-4a22-849a-35193cbfbfed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPuw4DwgQcELBSrmY7Jbi1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3000,
      "cache_read_input_tokens": 53619,
      "output_tokens": 753,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3000,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 753,
          "cache_read_input_tokens": 53619,
          "cache_creation_input_tokens": 3000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3000
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

_source line 42 · 2026-05-22T04:52:16.525Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0149Fu9EU58y13KJ3h2ocEpS`</summary>

```json
{
  "query": "Mihaylova Martins 2019 \"Scheduled Sampling for Transformers\" arxiv 1906.07651 venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4300eed-497b-4a22-849a-35193cbfbfed",
  "isSidechain": false,
  "requestId": "req_011CbH1Nr2Ar9zHTe2rmaRWw",
  "type": "assistant",
  "uuid": "489cd79d-50af-492f-8614-3ed8c472262f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPuw4DwgQcELBSrmY7Jbi1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3000,
      "cache_read_input_tokens": 53619,
      "output_tokens": 753,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3000,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 753,
          "cache_read_input_tokens": 53619,
          "cache_creation_input_tokens": 3000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3000
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

_source line 43_

```json
{
  "type": "last-prompt",
  "leafUuid": "489cd79d-50af-492f-8614-3ed8c472262f",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Fill literature map with core related papers",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Tool result

_source line 45 · 2026-05-22T04:52:19.963Z_

<details><summary>↩ Tool result · `toolu_0149Fu9EU58y13KJ3h2ocEpS`</summary>

```text
Web search results for query: "Mihaylova Martins 2019 "Scheduled Sampling for Transformers" arxiv 1906.07651 venue"

Links: [{"title":"[1906.07651] Scheduled Sampling for Transformers","url":"https://arxiv.org/abs/1906.07651"},{"title":"[1906.07651v1] Scheduled Sampling for Transformers","url":"https://arxiv.org/abs/1906.07651v1"},{"title":"[1906.07651] Scheduled Sampling for Transformers - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/1906.07651"},{"title":"Scheduled Sampling for Transformers - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190607651M/abstract"},{"title":"[1906.07651] Scheduled Sampling for Transformers","url":"https://www.arxiv-vanity.com/papers/1906.07651/"},{"title":"[PDF] Scheduled Sampling for Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scheduled-Sampling-for-Transformers-Mihaylova-Martins/6b6befbff611ddc98ef268b3c51353593bb07e77"},{"title":"Scheduled Sampling for Transformers | alphaXiv","url":"https://www.alphaxiv.org/overview/1906.07651v1"},{"title":"Scheduled Sampling for Transformers | Request PDF","url":"https://www.researchgate.net/publication/333866142_Scheduled_Sampling_for_Transformers"},{"title":"Scheduled Sampling for Transformers Tsvetomila Mihaylova","url":"https://arxiv.org/pdf/1906.07651"}]

Based on the search results, I found information about the paper. The paper "Scheduled Sampling for Transformers" was authored by Tsvetomila Mihaylova and André F. T. Martins and submitted on June 18, 2019 (arXiv ID: 1906.07651).

Regarding the venue, the paper was published at the ACL 2019 Student Research Workshop.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "489cd79d-50af-492f-8614-3ed8c472262f",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "0b000aa4-661b-452d-b375-4a9d95f79897",
  "toolUseResult": {
    "query": "Mihaylova Martins 2019 \"Scheduled Sampling for Transformers\" arxiv 1906.07651 venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FzCBzLscuYwLdoxVGTZAqZ",
        "content": [
          {
            "title": "[1906.07651] Scheduled Sampling for Transformers",
            "url": "https://arxiv.org/abs/1906.07651"
          },
          {
            "title": "[1906.07651v1] Scheduled Sampling for Transformers",
            "url": "https://arxiv.org/abs/1906.07651v1"
          },
          {
            "title": "[1906.07651] Scheduled Sampling for Transformers - ar5iv",
            "url": "https://ar5iv.labs.arxiv.org/html/1906.07651"
          },
          {
            "title": "Scheduled Sampling for Transformers - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2019arXiv190607651M/abstract"
          },
          {
            "title": "[1906.07651] Scheduled Sampling for Transformers",
            "url": "https://www.arxiv-vanity.com/papers/1906.07651/"
          },
          {
            "title": "[PDF] Scheduled Sampling for Transformers | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Scheduled-Sampling-for-Transformers-Mihaylova-Martins/6b6befbff611ddc98ef268b3c51353593bb07e77"
          },
          {
            "title": "Scheduled Sampling for Transformers | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/1906.07651v1"
          },
          {
            "title": "Scheduled Sampling for Transformers | Request PDF",
            "url": "https://www.researchgate.net/publication/333866142_Scheduled_Sampling_for_Transformers"
          },
          {
            "title": "Scheduled Sampling for Transformers Tsvetomila Mihaylova",
            "url": "https://arxiv.org/pdf/1906.07651"
          }
        ]
      },
      "Based on the search results, I found information about the paper. The paper \"Scheduled Sampling for Transformers\" was authored by Tsvetomila Mihaylova and André F. T. Martins and submitted on June 18, 2019 (arXiv ID: 1906.07651).\n\nRegarding the venue, the paper was published at the ACL 2019 Student Research Workshop."
    ],
    "durationSeconds": 3.4349636019999887
  },
  "sourceToolAssistantUUID": "489cd79d-50af-492f-8614-3ed8c472262f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-22T04:52:23.195Z_

<details><summary>↩ Tool result · `toolu_01JwuNTKRfS1R2MokiiHq25M`</summary>

```text
Web search results for query: "auxiliary attention loss supervision transformer training "attention regularization" 2023 2024 arxiv"

Links: [{"title":"Guiding Attention for Self-Supervised Learning with Transformers","url":"https://arxiv.org/pdf/2010.02399"},{"title":"Spatial Entropy as an Inductive Bias for Vision Transformers","url":"https://arxiv.org/pdf/2206.04636"},{"title":"Value Residual Learning For Alleviating Attention Concentration In Transformers","url":"https://arxiv.org/html/2410.17897v1"},{"title":"Crisp Attention: Regularizing Transformers via Structured Sparsity","url":"https://arxiv.org/html/2508.06016v1"},{"title":"Adaptive Attention Link-based Regularization for Vision Transformers","url":"https://arxiv.org/pdf/2211.13852"},{"title":"[2504.12088] AttentionDrop: A Novel Regularization Method for Transformer Models","url":"https://arxiv.org/abs/2504.12088"}]

I found several relevant papers on arXiv related to attention regularization and auxiliary losses in transformer training. Here are the key results:

## Papers Found:

1. **"Guiding Attention for Self-Supervised Learning with Transformers"** (2020, arXiv:2010.02399)
   - Proposes an auxiliary loss function to guide attention heads to conform to linguistic patterns, demonstrating that this method results in faster convergence and better downstream task performance.

2. **"Spatial Entropy as an Inductive Bias for Vision Transformers"** (2022, arXiv:2206.04636)
   - Uses an auxiliary self-supervised task jointly with standard supervised training to introduce local bias and encourage spatial clustering as a form of training regularization.

3. **"Value Residual Learning For Alleviating Attention Concentration In Transformers"** (October 2024, arXiv:2410.17897)
   - Addresses attention concentration issues and mentions solutions like adding extra regularizers to alleviate over-smoothing in transformers.

4. **"Crisp Attention: Regularizing Transformers via Structured Sparsity"** (August 2025, arXiv:2508.06016)
   - Demonstrates that structured sparsity in the attention mechanism can act as a regularizer, leading to significant accuracy improvements.

5. **"Adaptive Attention Link-based Regularization for Vision Transformers"** (2022, arXiv:2211.13852)
   - Proposes a regularization method through trainable attention links between ViT attention maps and CNN activation maps.

6. **"AttentionDrop: A Novel Regularization Method for Transformer Models"** (April 2024, arXiv:2504.12088)
   - Proposes stochastic regularization techniques operating on self-attention distributions, including hard attention masking and blurred attention smoothing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4300eed-497b-4a22-849a-35193cbfbfed",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "c9bc4096-8cc2-4cf7-bd99-251a99dccbff",
  "toolUseResult": {
    "query": "auxiliary attention loss supervision transformer training \"attention regularization\" 2023 2024 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MBYN3jFh2Gx6HiEVG3iXNg",
        "content": [
          {
            "title": "Guiding Attention for Self-Supervised Learning with Transformers",
            "url": "https://arxiv.org/pdf/2010.02399"
          },
          {
            "title": "Spatial Entropy as an Inductive Bias for Vision Transformers",
            "url": "https://arxiv.org/pdf/2206.04636"
          },
          {
            "title": "Value Residual Learning For Alleviating Attention Concentration In Transformers",
            "url": "https://arxiv.org/html/2410.17897v1"
          },
          {
            "title": "Crisp Attention: Regularizing Transformers via Structured Sparsity",
            "url": "https://arxiv.org/html/2508.06016v1"
          },
          {
            "title": "Adaptive Attention Link-based Regularization for Vision Transformers",
            "url": "https://arxiv.org/pdf/2211.13852"
          },
          {
            "title": "[2504.12088] AttentionDrop: A Novel Regularization Method for Transformer Models",
            "url": "https://arxiv.org/abs/2504.12088"
          }
        ]
      },
      "I found several relevant papers on arXiv related to attention regularization and auxiliary losses in transformer training. Here are the key results:\n\n## Papers Found:\n\n1. **\"Guiding Attention for Self-Supervised Learning with Transformers\"** (2020, arXiv:2010.02399)\n   - Proposes an auxiliary loss function to guide attention heads to conform to linguistic patterns, demonstrating that this method results in faster convergence and better downstream task performance.\n\n2. **\"Spatial Entropy as an Inductive Bias for Vision Transformers\"** (2022, arXiv:2206.04636)\n   - Uses an auxiliary self-supervised task jointly with standard supervised training to introduce local bias and encourage spatial clustering as a form of training regularization.\n\n3. **\"Value Residual Learning For Alleviating Attention Concentration In Transformers\"** (October 2024, arXiv:2410.17897)\n   - Addresses attention concentration issues and mentions solutions like adding extra regularizers to alleviate over-smoothing in transformers.\n\n4. **\"Crisp Attention: Regularizing Transformers via Structured Sparsity\"** (August 2025, arXiv:2508.06016)\n   - Demonstrates that structured sparsity in the attention mechanism can act as a regularizer, leading to significant accuracy improvements.\n\n5. **\"Adaptive Attention Link-based Regularization for Vision Transformers\"** (2022, arXiv:2211.13852)\n   - Proposes a regularization method through trainable attention links between ViT attention maps and CNN activation maps.\n\n6. **\"AttentionDrop: A Novel Regularization Method for Transformer Models\"** (April 2024, arXiv:2504.12088)\n   - Proposes stochastic regularization techniques operating on self-attention distributions, including hard attention masking and blurred attention smoothing."
    ],
    "durationSeconds": 7.073938902000009
  },
  "sourceToolAssistantUUID": "e4300eed-497b-4a22-849a-35193cbfbfed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-22T04:52:37.870Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me search for one more paper in the GAR/grounding/attention direction. Let me look for something about instruction-following attention patterns or goal-conditioned attention in multi-turn dialogue that isn't already in the literature map.

Actually, thinking more carefully about what papers would be most relevant and valuable to add:

1. **Wiseman & Rush 2016** - "Sequence-to-Sequence Learning as Beam-Search Optimization" - explicitly mentioned in paper_framing.md SP1. Role: foundation (exposure bias)
2. **Zhang et al. 

2019** - "Bridging the Gap between Training and Inference for Neural Machine Translation" - addresses exposure bias mitigation in NMT, directly relevant to the paper's discussion of mitigation approaches. Role: method-component (exposure bias mitigation)
3. **Arora et al. 2022** - "Why Exposure Bias Matters: An Imitation Learning Perspective" - provides the most recent theoretical analysis showing how exposure bias causes error accumulation. Role: theoretical-foundation
4. **Mihaylova & Martins 2019** - "Scheduled Sampling for Transformers" - applies scheduled sampling to transformer models. Role: method-component (scheduled sampling in transformers)
5. For the fifth paper, I'm looking for something in the attention/grounding direction since the core contribution involves using attention patterns as auxiliary training signals. I'm considering papers on attention distillation or attention supervision—something that frames attention as a training signal itself, which would highlight the gap between using GAR during training versus its failure to transfer at inference time.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9bc4096-8cc2-4cf7-bd99-251a99dccbff",
  "isSidechain": false,
  "requestId": "req_011CbH1QT1NWoD5YTTpNzXoM",
  "type": "assistant",
  "uuid": "0d5fae50-1433-4613-acbf-f13afdbf8a8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157yhf9C7QiWn3cVjZozeHC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 596,
      "cache_creation_input_tokens": 1516,
      "cache_read_input_tokens": 56619,
      "output_tokens": 586,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1516,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 596,
          "output_tokens": 586,
          "cache_read_input_tokens": 56619,
          "cache_creation_input_tokens": 1516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1516
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

_source line 48 · 2026-05-22T04:52:38.033Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GeYr8WQpAa1C2S4eiEVJHk`</summary>

```json
{
  "query": "attention supervision auxiliary loss language model \"attention guidance\" transformer training generalization 2022 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d5fae50-1433-4613-acbf-f13afdbf8a8e",
  "isSidechain": false,
  "requestId": "req_011CbH1QT1NWoD5YTTpNzXoM",
  "type": "assistant",
  "uuid": "fb4e3b09-5c3a-4192-a2e5-21e00378934a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157yhf9C7QiWn3cVjZozeHC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 596,
      "cache_creation_input_tokens": 1516,
      "cache_read_input_tokens": 56619,
      "output_tokens": 586,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1516,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 596,
          "output_tokens": 586,
          "cache_read_input_tokens": 56619,
          "cache_creation_input_tokens": 1516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1516
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

_source line 49 · 2026-05-22T04:52:44.623Z_

<details><summary>↩ Tool result · `toolu_01GeYr8WQpAa1C2S4eiEVJHk`</summary>

```text
Web search results for query: "attention supervision auxiliary loss language model "attention guidance" transformer training generalization 2022 2023 2024"

Links: [{"title":"Guiding Attention for Self-Supervised Learning with Transformers","url":"https://arxiv.org/pdf/2010.02399"},{"title":"On the Surprising Effectiveness of Attention Transfer for Vision Transformers","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/ceb45c48e29e7f49b0b47edb98e43691-Paper-Conference.pdf"},{"title":"Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/html/2507.19595v1"},{"title":"Supervised Visual Attention for Simultaneous Multimodal Machine   Translation","url":"https://arxiv.org/pdf/2201.09324"},{"title":"Beyond Self-learned Attention: Mitigating Attention Bias in   Transformer-based Models Using Attention Guidance","url":"https://arxiv.org/pdf/2402.16790"},{"title":"Learning to Look: Cognitive Attention Alignment with Vision-Language Models","url":"https://arxiv.org/pdf/2509.21247"},{"title":"Structural Guidance for Transformer Language Models","url":"https://arxiv.org/pdf/2108.00104"}]

I've completed a web search for your query about attention supervision, auxiliary losses, language models, attention guidance, and transformer training generalization. Here's a summary of the relevant research findings:

## Key Research Areas Found

**Attention Guidance for Transformers:**

One approach proposes a computationally efficient auxiliary loss function to guide attention heads to conform to linguistic patterns. This method results in faster convergence of models as well as better performance on downstream tasks.

**Attention Supervision for Improved Generalization:**

Transformer networks feature a self-attention mechanism that learns the weight and interdependence of attention among tokens within an input sequence, using attention weights to capture inter-relationships and long-range dependencies. Recent work has explored attention guiding mechanisms followed by fine-tuning, where PLMs undergo fine-tuning to achieve optimal performance for specific downstream tasks.

**Auxiliary Loss for Attention Alignment:**

Concept-based supervision and explanation regularization techniques encourage models to align their attention with ground-truth annotations through auxiliary losses, and auxiliary losses can align model attention with reference maps to steer networks toward more reliable decision-making.

**Structural Guidance in Language Models:**

Generative structural supervisions can induce more robust and humanlike linguistic generalization in Transformer language models without the need for data intensive pre-training.

The search results include papers from 2020-2024 covering these topics across vision transformers, language models, and multimodal applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb4e3b09-5c3a-4192-a2e5-21e00378934a",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "1b4a5224-6cc5-4858-979e-5a0392149c2a",
  "toolUseResult": {
    "query": "attention supervision auxiliary loss language model \"attention guidance\" transformer training generalization 2022 2023 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Wxz343J4ZxToKakDQmo2BP",
        "content": [
          {
            "title": "Guiding Attention for Self-Supervised Learning with Transformers",
            "url": "https://arxiv.org/pdf/2010.02399"
          },
          {
            "title": "On the Surprising Effectiveness of Attention Transfer for Vision Transformers",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/ceb45c48e29e7f49b0b47edb98e43691-Paper-Conference.pdf"
          },
          {
            "title": "Efficient Attention Mechanisms for Large Language Models: A Survey",
            "url": "https://arxiv.org/html/2507.19595v1"
          },
          {
            "title": "Supervised Visual Attention for Simultaneous Multimodal Machine   Translation",
            "url": "https://arxiv.org/pdf/2201.09324"
          },
          {
            "title": "Beyond Self-learned Attention: Mitigating Attention Bias in   Transformer-based Models Using Attention Guidance",
            "url": "https://arxiv.org/pdf/2402.16790"
          },
          {
            "title": "Learning to Look: Cognitive Attention Alignment with Vision-Language Models",
            "url": "https://arxiv.org/pdf/2509.21247"
          },
          {
            "title": "Structural Guidance for Transformer Language Models",
            "url": "https://arxiv.org/pdf/2108.00104"
          }
        ]
      },
      "I've completed a web search for your query about attention supervision, auxiliary losses, language models, attention guidance, and transformer training generalization. Here's a summary of the relevant research findings:\n\n## Key Research Areas Found\n\n**Attention Guidance for Transformers:**\n\nOne approach proposes a computationally efficient auxiliary loss function to guide attention heads to conform to linguistic patterns. This method results in faster convergence of models as well as better performance on downstream tasks.\n\n**Attention Supervision for Improved Generalization:**\n\nTransformer networks feature a self-attention mechanism that learns the weight and interdependence of attention among tokens within an input sequence, using attention weights to capture inter-relationships and long-range dependencies. Recent work has explored attention guiding mechanisms followed by fine-tuning, where PLMs undergo fine-tuning to achieve optimal performance for specific downstream tasks.\n\n**Auxiliary Loss for Attention Alignment:**\n\nConcept-based supervision and explanation regularization techniques encourage models to align their attention with ground-truth annotations through auxiliary losses, and auxiliary losses can align model attention with reference maps to steer networks toward more reliable decision-making.\n\n**Structural Guidance in Language Models:**\n\nGenerative structural supervisions can induce more robust and humanlike linguistic generalization in Transformer language models without the need for data intensive pre-training.\n\nThe search results include papers from 2020-2024 covering these topics across vision transformers, language models, and multimodal applications."
    ],
    "durationSeconds": 6.5866789960000025
  },
  "sourceToolAssistantUUID": "fb4e3b09-5c3a-4192-a2e5-21e00378934a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-22T04:53:25.996Z_

<details><summary>Logged reasoning block</summary>

```text
The paper "Beyond Self-learned Attention: Mitigating Attention Bias in Transformer-based Models Using Attention Guidance" (arXiv:2402.16790) seems highly relevant - it's about using attention guidance to mitigate attention bias in transformers. Let me search for more details.

Actually, let me also check the "Structural Guidance for Transformer Language Models" paper (arXiv:2108.00104) which seems relevant to using auxiliary signals to guide attention in LMs.

But wait - I think I have enough papers now. Let me also consider what would be most impactful for the literature map. The task requires papers from 4 directions:


- Exposure bias: I'll use Wiseman & Rush 2016 plus Arora et al. 2022
- GAR/grounding/attention: The attention guidance paper could work, though I might need something more specific
- Multi-turn dialogue attention: Already well covered in the map
- Scheduled sampling and curriculum learning: Zhang et al. 2019 and Mihaylova & Martins 2019 should fill this out

Looking at what the task actually requires across these four directions, I need to make sure I'm hitting all of them. For direction b on attention guidance, that 2402.16790 paper about mitigating attention bias through attention guidance seems like it could be exactly what I need—it's directly about using attention mechanisms to guide model behavior, which is essentially what our paper explores with the GAR loss. Let me pull up the details on that one.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b4a5224-6cc5-4858-979e-5a0392149c2a",
  "isSidechain": false,
  "requestId": "req_011CbH1S2dyL6FmGUqkRoUsR",
  "type": "assistant",
  "uuid": "863b7379-e02a-4634-b0ce-93e2fda3a28e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkdiNkXSHLjAgHf3KYbHDk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1857,
      "cache_read_input_tokens": 58135,
      "output_tokens": 598,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1857,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 598,
          "cache_read_input_tokens": 58135,
          "cache_creation_input_tokens": 1857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1857
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

_source line 51 · 2026-05-22T04:53:26.002Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KtezG4HDTrSopvMPHxg5Fr`</summary>

```json
{
  "query": "\"Beyond Self-learned Attention\" \"Mitigating Attention Bias\" transformer attention guidance arxiv 2402.16790"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "863b7379-e02a-4634-b0ce-93e2fda3a28e",
  "isSidechain": false,
  "requestId": "req_011CbH1S2dyL6FmGUqkRoUsR",
  "type": "assistant",
  "uuid": "d99df3e5-2cdf-40d9-ae3d-34ad724b40ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkdiNkXSHLjAgHf3KYbHDk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1857,
      "cache_read_input_tokens": 58135,
      "output_tokens": 598,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1857,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 598,
          "cache_read_input_tokens": 58135,
          "cache_creation_input_tokens": 1857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1857
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

_source line 52 · 2026-05-22T04:53:32.111Z_

<details><summary>↩ Tool result · `toolu_01KtezG4HDTrSopvMPHxg5Fr`</summary>

```text
Web search results for query: ""Beyond Self-learned Attention" "Mitigating Attention Bias" transformer attention guidance arxiv 2402.16790"

Links: [{"title":"[2402.16790] Beyond Self-learned Attention: Mitigating Attention Bias in Transformer-based Models Using Attention Guidance","url":"https://arxiv.org/abs/2402.16790"},{"title":"Beyond Self-learned Attention: Mitigating Attention Bias in Transformer-based Models Using Attention Guidance","url":"https://arxiv.org/html/2402.16790v1"},{"title":"Beyond Self-learned Attention: Mitigating Attention Bias in   Transformer-based Models Using Attention Guidance","url":"https://arxiv.org/pdf/2402.16790"},{"title":"An Attentive Inductive Bias for Sequential Recommendation Beyond the Self-Attention","url":"https://arxiv.org/html/2312.10325v1"},{"title":"Prior Knowledge-Guided Attention in Self-Supervised Vision Transformers","url":"https://arxiv.org/pdf/2209.03745"},{"title":"On the Emergence of Position Bias in Transformers","url":"https://arxiv.org/pdf/2502.01951"}]

I found the paper you're looking for. The paper "Beyond Self-learned Attention: Mitigating Attention Bias in Transformer-based Models Using Attention Guidance" addresses how transformer-based models for source code are limited by their dependence on automatic self-attention weight learning, and how these models overemphasize delimiters added by tokenizers (e.g., [CLS], [SEP]), which may lead to overlooking essential information in the original input source code.

The authors introduce SyntaGuid, a novel approach that utilizes the observation that attention weights tend to be biased towards specific source code syntax tokens and abstract syntax tree (AST) elements in fine-tuned language models when they make correct predictions, and facilitates the guidance of attention-weight learning to improve model performance on various software engineering tasks.

Experimental results show that SyntaGuid can improve overall performance up to 3.25% and fix up to 28.3% wrong predictions.

The paper was submitted on February 26, 2024, and is authored by Jiri Gesi (Amazon) and Iftelhar Ahmed (University of California, Irvine).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d99df3e5-2cdf-40d9-ae3d-34ad724b40ec",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "be1da830-4c0c-44d4-acc4-1c1520e5a08a",
  "toolUseResult": {
    "query": "\"Beyond Self-learned Attention\" \"Mitigating Attention Bias\" transformer attention guidance arxiv 2402.16790",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HRc4KPmktt7EFjTNvBX6z6",
        "content": [
          {
            "title": "[2402.16790] Beyond Self-learned Attention: Mitigating Attention Bias in Transformer-based Models Using Attention Guidance",
            "url": "https://arxiv.org/abs/2402.16790"
          },
          {
            "title": "Beyond Self-learned Attention: Mitigating Attention Bias in Transformer-based Models Using Attention Guidance",
            "url": "https://arxiv.org/html/2402.16790v1"
          },
          {
            "title": "Beyond Self-learned Attention: Mitigating Attention Bias in   Transformer-based Models Using Attention Guidance",
            "url": "https://arxiv.org/pdf/2402.16790"
          },
          {
            "title": "An Attentive Inductive Bias for Sequential Recommendation Beyond the Self-Attention",
            "url": "https://arxiv.org/html/2312.10325v1"
          },
          {
            "title": "Prior Knowledge-Guided Attention in Self-Supervised Vision Transformers",
            "url": "https://arxiv.org/pdf/2209.03745"
          },
          {
            "title": "On the Emergence of Position Bias in Transformers",
            "url": "https://arxiv.org/pdf/2502.01951"
          }
        ]
      },
      "I found the paper you're looking for. The paper \"Beyond Self-learned Attention: Mitigating Attention Bias in Transformer-based Models Using Attention Guidance\" addresses how transformer-based models for source code are limited by their dependence on automatic self-attention weight learning, and how these models overemphasize delimiters added by tokenizers (e.g., [CLS], [SEP]), which may lead to overlooking essential information in the original input source code.\n\nThe authors introduce SyntaGuid, a novel approach that utilizes the observation that attention weights tend to be biased towards specific source code syntax tokens and abstract syntax tree (AST) elements in fine-tuned language models when they make correct predictions, and facilitates the guidance of attention-weight learning to improve model performance on various software engineering tasks.\n\nExperimental results show that SyntaGuid can improve overall performance up to 3.25% and fix up to 28.3% wrong predictions.\n\nThe paper was submitted on February 26, 2024, and is authored by Jiri Gesi (Amazon) and Iftelhar Ahmed (University of California, Irvine)."
    ],
    "durationSeconds": 6.104094897000003
  },
  "sourceToolAssistantUUID": "d99df3e5-2cdf-40d9-ae3d-34ad724b40ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 53_

```json
{
  "type": "last-prompt",
  "leafUuid": "be1da830-4c0c-44d4-acc4-1c1520e5a08a",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Fill literature map with core related papers",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Assistant

_source line 55 · 2026-05-22T04:54:03.368Z_

<details><summary>Logged reasoning block</summary>

```text
This paper is about code models, not language models for dialogue. It's not the best fit. Let me think of a better paper for direction b (GAR/grounding/attention).

Actually, I think the most relevant paper for direction b would be something about:
1. Attention supervision/distillation in NLG that fails or doesn't generalize
2. Goal-conditioned generation
3. System prompt attention patterns

Let me look for a paper on attention alignment or attention loss in dialogue/language models that more directly relates to the GAR concept.

Actually, you know what - I think I already have enough relevant papers. The task says "从以下 4 个方向各选至少 1 篇核心论文". Let me see:


- a. Exposure bias: Wiseman & Rush 2016 (explicit mention in paper_framing SP1) + Arora et al. 2022
- b. GAR/grounding/attention: Dongre et al. is already in the map! The task says "如 Dongre et al. 2026 (goal attention ratio)" - but this is already there. Maybe I need to find something NEW that's not in the map yet.
- c. Multi-turn dialogue attention: Liu et al. 2023 (lost in the middle) is already there
- d. Scheduled sampling / curriculum learning: Bengio 2015 is already there. Add Zhang 2019 + Mihaylova 2019.

Actually, looking at the task more carefully—I need at least one paper from each of the four directions, and I should be adding at least five papers total that aren't already in the literature map. Let me focus on papers that are genuinely missing. Wiseman & Rush 2016 on sequence-to-sequence beam search optimization covers the exposure bias direction and isn't in the map yet, so that's a solid first choice. Zhang et al. 2019 looks promising for bridging the gap between training and inference...

Now I'm looking at papers that specifically address exposure bias and scheduled sampling approaches. Arora et al. 2022 provides recent theoretical grounding on why exposure bias causes error accumulation, which would strengthen the conceptual foundation. Mihaylova & Martins 2019 extends scheduled sampling specifically to transformers, filling a gap in how these mitigation techniques apply to modern architectures. For the fifth paper, I should find something that covers direction b or c to ensure I have representation across all four directions. I'm reconsidering the angle here—the key insight is that auxiliary attention losses fail to generalize from teacher-forced to model-generated sequences, so I should look for papers that either demonstrate this problem in other contexts or use attention supervision as a training objective. A strong addition would be something recent about multi-turn dialogue attention degradation or how attention mechanisms break down over conversation turns, rather than retreading older foundational work like Bahdanau's alignment paper. I'm searching for a strong paper on how system prompts and instructions influence attention patterns in multi-turn LLM conversations, which would directly address the goal-conditioning aspect of GAR degradation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be1da830-4c0c-44d4-acc4-1c1520e5a08a",
  "isSidechain": false,
  "requestId": "req_011CbH1VXhnu5RAoPEpzhkmx",
  "type": "assistant",
  "uuid": "37cee431-37d6-4498-8be9-16126533dba8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KU4ZWEgyGsGPijtvkDQ7fv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1192,
      "cache_read_input_tokens": 59992,
      "output_tokens": 1467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1192,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1467,
          "cache_read_input_tokens": 59992,
          "cache_creation_input_tokens": 1192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1192
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

_source line 56 · 2026-05-22T04:54:03.465Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016zhk7W8rGaRSW2w1qFNnE9`</summary>

```json
{
  "query": "system prompt instruction attention degradation multi-turn LLM 2024 2025 arxiv attention allocation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37cee431-37d6-4498-8be9-16126533dba8",
  "isSidechain": false,
  "requestId": "req_011CbH1VXhnu5RAoPEpzhkmx",
  "type": "assistant",
  "uuid": "65b0bb53-a8db-4440-ae96-e1b8cb896da9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KU4ZWEgyGsGPijtvkDQ7fv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1192,
      "cache_read_input_tokens": 59992,
      "output_tokens": 1467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1192,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1467,
          "cache_read_input_tokens": 59992,
          "cache_creation_input_tokens": 1192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1192
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

_source line 57 · 2026-05-22T04:54:10.881Z_

<details><summary>↩ Tool result · `toolu_016zhk7W8rGaRSW2w1qFNnE9`</summary>

```text
Web search results for query: "system prompt instruction attention degradation multi-turn LLM 2024 2025 arxiv attention allocation"

Links: [{"title":"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/html/2605.12922"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"},{"title":"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs","url":"https://arxiv.org/html/2402.10962v3"},{"title":"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://arxiv.org/pdf/2512.06869"},{"title":"RelayAttention for Efficient Large Language Model Serving with Long   System Prompts","url":"https://arxiv.org/pdf/2402.14808"},{"title":"Modeling and Predicting Multi-Turn Answer Instability in Large Language Models","url":"https://arxiv.org/pdf/2511.10688"},{"title":"Context Branching for LLM Conversations: A Version Control Approach to Exploratory Programming","url":"https://arxiv.org/pdf/2512.13914"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/pdf/2602.07338"}]

I found several highly relevant papers on this topic. Here are the key findings:

## Main Research Areas

**Attention Degradation in Multi-Turn LLMs:**

Large language models deployed in multi-turn settings must remain consistent with instructions delivered in the system prompt, where persona, formatting requirements, safety policies, and reference facts are typically specified once and expected to govern model output for the remainder of the session. However, while LLMs comply with such instructions reliably in single-turn evaluations, compliance degrades in multi-turn deployments.

**Key Papers and Findings:**

1. **"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction"** - This recent paper examines how LLMs lose track of system prompts in multi-turn interactions.

2. **Instruction Drift and Attention Control** - Research has shown that chatbots initially follow system prompts well but fail after extended conversations, and proposes split-softmax, a training-free method that amplifies the model's attention to the system prompt at inference time.

3. **KV Cache Compression Issues** - System prompts define an LLM's behavior, persona, and safety guardrails, and because they are present across long interactions and reused for multiple queries, their KV cache entries are natural targets for compression.

4. **Performance Degradation Magnitude** - Recent studies demonstrate an average 39% performance drop when instructions are delivered across multiple turns.

The research indicates that attention allocation to system prompts is a critical factor in multi-turn LLM reliability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65b0bb53-a8db-4440-ae96-e1b8cb896da9",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "0e9dd352-b733-429d-bb8f-02e52a32db11",
  "toolUseResult": {
    "query": "system prompt instruction attention degradation multi-turn LLM 2024 2025 arxiv attention allocation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VEpHjtJoTXGFK7RBTnsinJ",
        "content": [
          {
            "title": "When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction",
            "url": "https://arxiv.org/html/2605.12922"
          },
          {
            "title": "Preprint THE PITFALLS OF KV CACHE COMPRESSION",
            "url": "https://arxiv.org/pdf/2510.00231"
          },
          {
            "title": "Measuring and Controlling Instruction (In)Stability in Language Model Dialogs",
            "url": "https://arxiv.org/html/2402.10962v3"
          },
          {
            "title": "Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs",
            "url": "https://arxiv.org/pdf/2512.06869"
          },
          {
            "title": "RelayAttention for Efficient Large Language Model Serving with Long   System Prompts",
            "url": "https://arxiv.org/pdf/2402.14808"
          },
          {
            "title": "Modeling and Predicting Multi-Turn Answer Instability in Large Language Models",
            "url": "https://arxiv.org/pdf/2511.10688"
          },
          {
            "title": "Context Branching for LLM Conversations: A Version Control Approach to Exploratory Programming",
            "url": "https://arxiv.org/pdf/2512.13914"
          },
          {
            "title": "Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation",
            "url": "https://arxiv.org/pdf/2602.07338"
          }
        ]
      },
      "I found several highly relevant papers on this topic. Here are the key findings:\n\n## Main Research Areas\n\n**Attention Degradation in Multi-Turn LLMs:**\n\nLarge language models deployed in multi-turn settings must remain consistent with instructions delivered in the system prompt, where persona, formatting requirements, safety policies, and reference facts are typically specified once and expected to govern model output for the remainder of the session. However, while LLMs comply with such instructions reliably in single-turn evaluations, compliance degrades in multi-turn deployments.\n\n**Key Papers and Findings:**\n\n1. **\"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\"** - This recent paper examines how LLMs lose track of system prompts in multi-turn interactions.\n\n2. **Instruction Drift and Attention Control** - Research has shown that chatbots initially follow system prompts well but fail after extended conversations, and proposes split-softmax, a training-free method that amplifies the model's attention to the system prompt at inference time.\n\n3. **KV Cache Compression Issues** - System prompts define an LLM's behavior, persona, and safety guardrails, and because they are present across long interactions and reused for multiple queries, their KV cache entries are natural targets for compression.\n\n4. **Performance Degradation Magnitude** - Recent studies demonstrate an average 39% performance drop when instructions are delivered across multiple turns.\n\nThe research indicates that attention allocation to system prompts is a critical factor in multi-turn LLM reliability."
    ],
    "durationSeconds": 7.4080794579999925
  },
  "sourceToolAssistantUUID": "65b0bb53-a8db-4440-ae96-e1b8cb896da9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-22T04:54:16.344Z_

<details><summary>Logged reasoning block</summary>

```text
The paper "Measuring and Controlling Instruction (In)Stability in Language Model Dialogs" (arXiv:2402.10962) seems very relevant - it's about instruction compliance degradation in multi-turn settings and proposes methods to control it. Let me search for more details about this paper.

Also, "Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs" (arXiv:2512.06869) seems relevant - it's about role-aware attention for conversational LLMs.

Let me get details on the first one, as it seems most directly relevant to our paper's problem (attention to system prompt degrades over turns = GAR degradation).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e9dd352-b733-429d-bb8f-02e52a32db11",
  "isSidechain": false,
  "requestId": "req_011CbH1YPZUd9GqQZ52sfaVF",
  "type": "assistant",
  "uuid": "0d17ee5b-d8df-4882-855c-79c1dbe4fb4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TqAgCR7NNLphbxcXuhUEaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2199,
      "cache_read_input_tokens": 61184,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2199,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 253,
          "cache_read_input_tokens": 61184,
          "cache_creation_input_tokens": 2199,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2199
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

_source line 59 · 2026-05-22T04:54:16.895Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011XDqWL3SzM8P1CEn2jo398`</summary>

```json
{
  "query": "\"Measuring and Controlling Instruction Instability\" language model dialogs arxiv 2402.10962 authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d17ee5b-d8df-4882-855c-79c1dbe4fb4a",
  "isSidechain": false,
  "requestId": "req_011CbH1YPZUd9GqQZ52sfaVF",
  "type": "assistant",
  "uuid": "bec0ed05-0894-4fb0-a67d-1fc859f9ba4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TqAgCR7NNLphbxcXuhUEaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2199,
      "cache_read_input_tokens": 61184,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2199,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 253,
          "cache_read_input_tokens": 61184,
          "cache_creation_input_tokens": 2199,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2199
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

_source line 60 · 2026-05-22T04:54:22.696Z_

<details><summary>↩ Tool result · `toolu_011XDqWL3SzM8P1CEn2jo398`</summary>

```text
Web search results for query: ""Measuring and Controlling Instruction Instability" language model dialogs arxiv 2402.10962 authors venue"

Links: [{"title":"[Literature Review] Measuring and Controlling Instruction (In)Stability in Language Model Dialogs","url":"https://www.themoonlight.io/en/review/measuring-and-controlling-instruction-instability-in-language-model-dialogs"},{"title":"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs (arXiv:2402.10962v4) - ScienceStack","url":"https://www.sciencestack.ai/paper/2402.10962"},{"title":"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs - AI Research Paper Analysis | ArxivLens - Arxivlens","url":"https://arxivlens.com/paperview/details/measuring-and-controlling-instruction-instability-in-language-model-dialogs-7499-1350985"},{"title":"[2402.10962] Measuring and Controlling Instruction (In)Stability in Language Model Dialogs","url":"https://arxiv.org/abs/2402.10962"},{"title":"[2402.10962v4] Measuring and Controlling Instruction (In)Stability in Language Model Dialogs","url":"https://arxiv.org/abs/2402.10962v4"},{"title":"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs | alphaXiv","url":"https://www.alphaxiv.org/abs/2402.10962"},{"title":"VCG Harvard | Measuring and Controlling Instruction (In)Stability in Language Model Dialogs","url":"https://vcg.seas.harvard.edu/publications/https-arxiv-org-pdf-2402-10962"},{"title":"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs","url":"https://arxiv.org/html/2402.10962v3"},{"title":"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/measuring-controlling-instruction-instability-language-model-dialogs"},{"title":"arXiv:2402.10962v4 [cs.CL] 25 Jul 2024","url":"https://arxiv.org/pdf/2402.10962"}]

Based on the search results, here's the information about this paper:

## Paper Details

**Title:** Measuring and Controlling Instruction (In)Stability in Language Model Dialogs

**ArXiv ID:** 2402.10962

**Authors:** Kenneth Li, Tianle Liu, Naomi Bashkansky, David Bau, Fernanda Viégas, Hanspeter Pfister, Martin Wattenberg

**Venue:** Published as a conference paper at COLM 2024

**Submission Date:** Submitted on 13 Feb 2024 (v1), last revised 25 Jul 2024 (this version, v4)

## Summary

The paper proposes a quantitative benchmark to evaluate instruction stability via self-chats between two instructed chatbots, and testing popular models like LLaMA2-chat-70B and GPT-3.5 reveals significant instruction drift within eight rounds of conversations. An empirical and theoretical analysis suggests the transformer attention mechanism plays a role due to attention decay, and the authors propose a lightweight method called split-softmax to combat this issue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bec0ed05-0894-4fb0-a67d-1fc859f9ba4e",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "801514f1-e91a-42b7-8e5b-8fd4e8f505fd",
  "toolUseResult": {
    "query": "\"Measuring and Controlling Instruction Instability\" language model dialogs arxiv 2402.10962 authors venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_018hmeXrMhFpRW5CfuqKancT",
        "content": [
          {
            "title": "[Literature Review] Measuring and Controlling Instruction (In)Stability in Language Model Dialogs",
            "url": "https://www.themoonlight.io/en/review/measuring-and-controlling-instruction-instability-in-language-model-dialogs"
          },
          {
            "title": "Measuring and Controlling Instruction (In)Stability in Language Model Dialogs (arXiv:2402.10962v4) - ScienceStack",
            "url": "https://www.sciencestack.ai/paper/2402.10962"
          },
          {
            "title": "Measuring and Controlling Instruction (In)Stability in Language Model Dialogs - AI Research Paper Analysis | ArxivLens - Arxivlens",
            "url": "https://arxivlens.com/paperview/details/measuring-and-controlling-instruction-instability-in-language-model-dialogs-7499-1350985"
          },
          {
            "title": "[2402.10962] Measuring and Controlling Instruction (In)Stability in Language Model Dialogs",
            "url": "https://arxiv.org/abs/2402.10962"
          },
          {
            "title": "[2402.10962v4] Measuring and Controlling Instruction (In)Stability in Language Model Dialogs",
            "url": "https://arxiv.org/abs/2402.10962v4"
          },
          {
            "title": "Measuring and Controlling Instruction (In)Stability in Language Model Dialogs | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2402.10962"
          },
          {
            "title": "VCG Harvard | Measuring and Controlling Instruction (In)Stability in Language Model Dialogs",
            "url": "https://vcg.seas.harvard.edu/publications/https-arxiv-org-pdf-2402-10962"
          },
          {
            "title": "Measuring and Controlling Instruction (In)Stability in Language Model Dialogs",
            "url": "https://arxiv.org/html/2402.10962v3"
          },
          {
            "title": "Measuring and Controlling Instruction (In)Stability in Language Model Dialogs | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/measuring-controlling-instruction-instability-language-model-dialogs"
          },
          {
            "title": "arXiv:2402.10962v4 [cs.CL] 25 Jul 2024",
            "url": "https://arxiv.org/pdf/2402.10962"
          }
        ]
      },
      "Based on the search results, here's the information about this paper:\n\n## Paper Details\n\n**Title:** Measuring and Controlling Instruction (In)Stability in Language Model Dialogs\n\n**ArXiv ID:** 2402.10962\n\n**Authors:** Kenneth Li, Tianle Liu, Naomi Bashkansky, David Bau, Fernanda Viégas, Hanspeter Pfister, Martin Wattenberg\n\n**Venue:** Published as a conference paper at COLM 2024\n\n**Submission Date:** Submitted on 13 Feb 2024 (v1), last revised 25 Jul 2024 (this version, v4)\n\n## Summary\n\nThe paper proposes a quantitative benchmark to evaluate instruction stability via self-chats between two instructed chatbots, and testing popular models like LLaMA2-chat-70B and GPT-3.5 reveals significant instruction drift within eight rounds of conversations. An empirical and theoretical analysis suggests the transformer attention mechanism plays a role due to attention decay, and the authors propose a lightweight method called split-softmax to combat this issue."
    ],
    "durationSeconds": 5.797178736000002
  },
  "sourceToolAssistantUUID": "bec0ed05-0894-4fb0-a67d-1fc859f9ba4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-22T04:54:48.287Z_

<details><summary>Logged reasoning block</summary>

```text
This paper is highly relevant! It:
1. Quantifies instruction instability in multi-turn dialogues
2. Identifies attention decay as a mechanism
3. Proposes split-softmax as inference-time mitigation

This maps directly to our paper's problem (GAR degradation = attention to goal instructions declining over turns) and the proposed future direction (inference-time attention intervention). This is perfect for direction b/c.

Now I have 5 strong papers to add:

1. **Wiseman & Rush 2016** - "Sequence-to-Sequence Learning as Beam-Search Optimization" (EMNLP 2016, arXiv:1606.02960)
   - Role: foundation
   - Direction: a (exposure bias)
   - Relevance: Explicitly cited in paper_framing SP1 as a key reference for quantifying train-test discrepancy. Proposes beam-aware training that unifies training and test-time objectives.

2. **Zhang et al. 2019** - "Bridging the Gap between Training and Inference for Neural Machine Translation" (ACL 2019, arXiv:1906.02448)
   - Role: method-component
   - Direction: d (scheduled sampling / curriculum learning)
   - Relevance: Key exposure bias mitigation for NMT that samples context from both ground truth and model predictions during training to reduce the train-test mismatch.

3. **Arora et al. 2022** - "Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation" (ACL Findings 2022, arXiv:2204.01171)
   - Role: theoretical-foundation
   - Direction: a (exposure bias)
   - Relevance: Recent theoretical work proving exposure bias causes compounding errors in text generation through an imitation learning lens, directly supporting our paper's central argument.

4. **Mihaylova & Martins 2019** - "Scheduled Sampling for Transformers" (ACL SRW 2019, arXiv:1906.07651)
   - Role: method-component
   - Direction: d (scheduled sampling / curriculum learning)
   - Relevance: Applies scheduled sampling to Transformers, extending the foundational approach to modern architectures.

5. **Li et al. 2024** - "Measuring and Controlling Instruction (In)Stability in Language Model Dialogs" (COLM 2024, arXiv:2402.10962)
   - Role: direct-competitor
   - Direction: b/c (GAR/grounding + multi-turn attention)
   - Relevance: Directly addresses the same multi-turn degradation problem we're tackling, identifies attention decay as the mechanism, and proposes an inference-time fix using split-softmax.

Now I'm updating the literature_map.yaml file with these entries...

Updating literature_map.yaml...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "801514f1-e91a-42b7-8e5b-8fd4e8f505fd",
  "isSidechain": false,
  "requestId": "req_011CbH1ZFv8Vj7TCd8YpaNAd",
  "type": "assistant",
  "uuid": "9eb65614-bdd7-44f1-a6c7-4c49f2f376c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ium1G3ht7N2ut5TvDopjm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 63383,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 63383,
          "cache_creation_input_tokens": 1129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1129
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

_source line 62 · 2026-05-22T04:54:48.289Z_

I have 5 papers to add. Let me now update the literature_map.yaml with these entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9eb65614-bdd7-44f1-a6c7-4c49f2f376c2",
  "isSidechain": false,
  "requestId": "req_011CbH1ZFv8Vj7TCd8YpaNAd",
  "type": "assistant",
  "uuid": "c22877b2-3714-4d37-b5af-5a1e9c8c4f77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ium1G3ht7N2ut5TvDopjm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 63383,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 63383,
          "cache_creation_input_tokens": 1129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1129
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

_source line 63 · 2026-05-22T04:54:49.369Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M17iUEVYR4j5szTaonLzhu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
  "offset": 325,
  "limit": 70
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c22877b2-3714-4d37-b5af-5a1e9c8c4f77",
  "isSidechain": false,
  "requestId": "req_011CbH1ZFv8Vj7TCd8YpaNAd",
  "type": "assistant",
  "uuid": "756984cc-3643-48c4-b209-d77f05af8ffd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ium1G3ht7N2ut5TvDopjm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 63383,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 63383,
          "cache_creation_input_tokens": 1129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1129
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

_source line 64 · 2026-05-22T04:54:49.381Z_

<details><summary>↩ Tool result · `toolu_01M17iUEVYR4j5szTaonLzhu`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "756984cc-3643-48c4-b209-d77f05af8ffd",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "616b58bb-a2bc-439d-a770-a0b276f0748c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
      "content": "  exposure_bias:\n    description: Exposure bias, teacher forcing, scheduled sampling, and train-test distribution mismatch in sequence generation\n    papers:\n    - title: Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\n      authors: Bengio, Vinyals, Jaitly, Shazeer\n      venue: NeurIPS 2015\n      year: 2015\n      url: https://arxiv.org/abs/1506.03099\n      role: foundation\n      relevance: Scheduled sampling 首次提出用 curriculum learning 缓解 teacher forcing 与推理时 autoregressive decoding 的分布不匹配（exposure\n        bias），直接支撑论文对 auxiliary attention loss 训练-推理 gap 的根因分析\n      abstract: Proposes a curriculum learning strategy to gently change training from fully guided (true previous token)\n        to less guided (model-generated token). The discrepancy between teacher-forced training and autoregressive inference\n        causes error accumulation. Experiments on sequence prediction tasks show significant improvements. Used in the winning\n        MSCOCO image captioning challenge 2015 entry.\n    - title: Sequence Level Training with Recurrent Neural Networks\n      authors: Ranzato, Chopra, Auli, Zaremba\n      venue: ICLR 2016\n      year: 2016\n      url: https://arxiv.org/abs/1511.06732\n      role: foundation\n      relevance: MIXER 算法直接优化测试时指标（BLEU/ROUGE）而非 token-level MLE，解决 teacher forcing 导致的 train-test discrepancy；论文中 auxiliary\n        loss 同样面临 token-level 训练目标与 sequence-level 推理行为的错位\n      abstract: Addresses the discrepancy between token-level MLE training and sequence-level generation at test time. Proposes\n        sequence level training that directly optimizes test metrics (BLEU, ROUGE). Outperforms strong baselines for greedy\n        generation on three tasks and is competitive with beam search while being several times faster.\n    - title: 'Professor Forcing: A New Algorithm for Training Recurrent Networks'\n      authors: Lamb, Goyal, Zhang, Zhang, Courville, Bengio\n      venue: NeurIPS 2016\n      year: 2016\n      url: https://arxiv.org/abs/1610.09038\n      role: foundation\n      relevance: 用对抗训练对齐 teacher forcing 训练与 free-running 采样的 hidden state 动态分布，直接证明 train-test dynamics mismatch 可导致长序列采样质量崩溃——与论文中\n        gating 机制推理时失效的现象高度对应\n      abstract: Introduces Professor Forcing, which uses adversarial domain adaptation to encourage the dynamics of the recurrent\n        network to be the same when training and when sampling over multiple time steps. Acts as a regularizer improving test\n        likelihood on Penn Treebank and sequential MNIST. Qualitatively improves samples especially for long generation horizons.\n        Discusses trade-offs with Scheduled Sampling.\n    - title: 'SEARNN: Training RNNs with Global-Local Losses'\n      authors: Leblond, Alayrac, Osokin, Lacoste-Julien\n      venue: ICLR 2018\n      year: 2018\n      url: https://arxiv.org/abs/1706.04499\n      role: context\n      relevance: 基于 learning-to-search 理论统一分析 MLE 训练的两大缺陷：exposure bias 和结构化损失信息浪费。论文中 auxiliary attention loss 同时受这两个缺陷影响——token-level\n        loss 无法反映 sequence-level attention pattern\n      abstract: Proposes SEARNN inspired by learning-to-search (L2S) approach to structured prediction. MLE training fails\n        to exploit structured losses and introduces train-test discrepancies (exposure bias). SEARNN leverages test-alike\n        search space exploration for global-local losses closer to test error. Demonstrates improvements on OCR, spelling\n        correction, and machine translation with a subsampling strategy for large vocabularies.\n    - title: Quantifying Exposure Bias for Neural Language Generation\n      authors: He, Zhang, Zhou, Glass\n      venue: arXiv 2019\n      year: 2019\n      url: https://arxiv.org/abs/1905.10617\n      role: foundation\n      relevance: 首次定量度量 exposure bias 影响并发现 LM 的 self-recovery 能力——即模型能从错误前缀部分恢复。这为论文分析 gating 机制在推理时的行为提供关键对照：如果 exposure\n        bias 可自恢复，auxiliary loss 崩溃可能源于更根本的分布偏移\n      abstract: 'Proposes sequence-level (EB-bleu) and word-level (EB-C) metrics to quantify exposure bias impact on quality,\n        diversity, and consistency. Key finding: contrary to popular belief, distortion from prefix discrepancy is limited\n        and does not appear incremental. Reveals an interesting self-recovery ability of language models that counters harmful\n        effects of exposure bias.'\n  gradient_conflict_mtl:\n    description: Multi-task gradient conflict resolution, gradient surgery, and loss balancing methods\n    papers:\n    - title: Gradient Surgery for Multi-Task Learning\n      authors: Yu, Kumar, Gupta, Levine, Hausman, Finn\n      venue: NeurIPS 2020\n      year: 2020\n      url: https://arxiv.org/abs/2001.06782",
      "numLines": 70,
      "startLine": 325,
      "totalLines": 454
    }
  },
  "sourceToolAssistantUUID": "756984cc-3643-48c4-b209-d77f05af8ffd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 65 · 2026-05-22T04:54:49.434Z_

```json
{
  "parentUuid": "616b58bb-a2bc-439d-a770-a0b276f0748c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1588c27e-b4dd-4cf3-8ea8-57c75291f763",
  "timestamp": "2026-05-22T04:54:49.434Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "last-prompt",
  "leafUuid": "1588c27e-b4dd-4cf3-8ea8-57c75291f763",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Fill literature map with core related papers",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Assistant

_source line 68 · 2026-05-22T04:54:57.478Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to add 5 papers to the literature_map.yaml. Let me add them in the appropriate sections:

1. **Wiseman & Rush 2016** → exposure_bias section (after He et al. 2019)
2. **Zhang et al. 2019** → exposure_bias section (as exposure bias mitigation for transformers)
3. **Arora et al. 2022** → exposure_bias section (recent theoretical contribution)
4. **Mihaylova & Martins 2019** → exposure_bias section (scheduled sampling for transformers)


5. **Li et al. 2024** → multi_turn_attention section

I'll insert papers 1-4 into the exposure_bias section before the gradient_conflict_mtl section, and then locate where the multi_turn_attention section ends to add paper 5 there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1588c27e-b4dd-4cf3-8ea8-57c75291f763",
  "isSidechain": false,
  "requestId": "req_011CbH1bEFikdS2i9mU1YuGE",
  "type": "assistant",
  "uuid": "fc74d52c-1f41-4fb8-b0c7-d900318e5277",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGZ8npXtP3MEKAURJYKRAo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2706,
      "cache_read_input_tokens": 64512,
      "output_tokens": 1633,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2706,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1633,
          "cache_read_input_tokens": 64512,
          "cache_creation_input_tokens": 2706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2706
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

_source line 69 · 2026-05-22T04:54:57.656Z_

Now I'll add the 5 papers. First, adding 3 to the exposure_bias section (after He et al. 2019).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc74d52c-1f41-4fb8-b0c7-d900318e5277",
  "isSidechain": false,
  "requestId": "req_011CbH1bEFikdS2i9mU1YuGE",
  "type": "assistant",
  "uuid": "d48c7ab8-f54c-450b-9e5a-26cffce979d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGZ8npXtP3MEKAURJYKRAo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2706,
      "cache_read_input_tokens": 64512,
      "output_tokens": 1633,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2706,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1633,
          "cache_read_input_tokens": 64512,
          "cache_creation_input_tokens": 2706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2706
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

_source line 70 · 2026-05-22T04:55:16.643Z_

<details open><summary>🔧 Tool call — Edit · `toolu_018A8GbxcS46NzU5AWY2CohY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
  "old_string": "      abstract: 'Proposes sequence-level (EB-bleu) and word-level (EB-C) metrics to quantify exposure bias impact on quality,\n        diversity, and consistency. Key finding: contrary to popular belief, distortion from prefix discrepancy is limited\n        and does not appear incremental. Reveals an interesting self-recovery ability of language models that counters harmful\n        effects of exposure bias.'\n  gradient_conflict_mtl:",
  "new_string": "      abstract: 'Proposes sequence-level (EB-bleu) and word-level (EB-C) metrics to quantify exposure bias impact on quality,\n        diversity, and consistency. Key finding: contrary to popular belief, distortion from prefix discrepancy is limited\n        and does not appear incremental. Reveals an interesting self-recovery ability of language models that counters harmful\n        effects of exposure bias.'\n    - title: Sequence-to-Sequence Learning as Beam-Search Optimization\n      authors: Wiseman, Rush\n      venue: EMNLP 2016\n      year: 2016\n      url: https://arxiv.org/abs/1606.02960\n      role: foundation\n      relevance: 提出 beam-aware 训练将训练目标与测试时解码统一，量化 teacher forcing 的 train-test discrepancy 对序列生成质量的影响。paper_framing SP1 明确引用为\n        exposure bias 在 sequence generation 中的量化先例\n      abstract: Proposes a model and beam-search training scheme that extends seq2seq to learn global sequence scores, avoiding\n        local training biases and unifying training loss with test-time usage. Outperforms attention-based seq2seq on word ordering,\n        parsing, and machine translation.\n    - title: 'Bridging the Gap between Training and Inference for Neural Machine Translation'\n      authors: Zhang, Feng, Meng, You, Liu\n      venue: ACL 2019\n      year: 2019\n      url: https://arxiv.org/abs/1906.02448\n      role: method-component\n      relevance: 在训练时混合 ground truth 和 model-generated tokens 作为上下文，用 sentence-level optimum 选择预测序列。直接对应论文 W8 中讨论的\n        exposure bias mitigation 实验方向——若应用于 auxiliary attention loss 可能缩小 30x gap\n      abstract: Addresses exposure bias in NMT by sampling context words from both ground truth and model predictions during\n        training, selecting predicted sequences with sentence-level optimum. Achieves significant improvements on Chinese-English\n        and WMT14 English-German translation.\n    - title: Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation\n      authors: Arora, El Asri, Bahuleyan, Cheung\n      venue: ACL Findings 2022\n      year: 2022\n      url: https://arxiv.org/abs/2204.01171\n      role: theoretical-foundation\n      relevance: 用 imitation learning 框架证明 exposure bias 导致 compounding error accumulation，且 perplexity 无法捕捉此累积效应。直接支撑论文核心论证：auxiliary\n        attention loss 的 PPL 正常但 GAR 崩溃，因为 perplexity 掩盖了分布偏移对 attention pattern 的破坏\n      abstract: Shows that exposure bias leads to accumulation of errors in autoregressive generation. Analyzes why perplexity\n        fails to capture this accumulation. Empirically demonstrates that compounding errors from train-test mismatch degrade\n        generation quality even when perplexity appears normal.\n    - title: Scheduled Sampling for Transformers\n      authors: Mihaylova, Martins\n      venue: ACL SRW 2019\n      year: 2019\n      url: https://arxiv.org/abs/1906.07651\n      role: method-component\n      relevance: 将 Bengio 2015 的 scheduled sampling 扩展到 transformer 架构，通过 two-pass decoding 策略解决 transformer 非自回归 decoder 的适配问题。直接相关于论文\n        Discussion 中讨论的 scheduled sampling 应用于 auxiliary attention loss 的未来方向\n      abstract: Extends scheduled sampling to Transformer architecture via two-pass decoding strategy. Proposes structural changes\n        to allow mixing of teacher-forced embeddings and model predictions during transformer training for exposure bias mitigation.\n  gradient_conflict_mtl:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d48c7ab8-f54c-450b-9e5a-26cffce979d6",
  "isSidechain": false,
  "requestId": "req_011CbH1bEFikdS2i9mU1YuGE",
  "type": "assistant",
  "uuid": "8e79287d-db66-412d-b3e4-99dccbe757d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGZ8npXtP3MEKAURJYKRAo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2706,
      "cache_read_input_tokens": 64512,
      "output_tokens": 1633,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2706,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1633,
          "cache_read_input_tokens": 64512,
          "cache_creation_input_tokens": 2706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2706
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

_source line 71 · 2026-05-22T04:55:16.678Z_

<details><summary>↩ Tool result · `toolu_018A8GbxcS46NzU5AWY2CohY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e79287d-db66-412d-b3e4-99dccbe757d4",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "86e08201-ea04-4f1b-9293-8058402d1fc7",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
    "oldString": "      abstract: 'Proposes sequence-level (EB-bleu) and word-level (EB-C) metrics to quantify exposure bias impact on quality,\n        diversity, and consistency. Key finding: contrary to popular belief, distortion from prefix discrepancy is limited\n        and does not appear incremental. Reveals an interesting self-recovery ability of language models that counters harmful\n        effects of exposure bias.'\n  gradient_conflict_mtl:",
    "newString": "      abstract: 'Proposes sequence-level (EB-bleu) and word-level (EB-C) metrics to quantify exposure bias impact on quality,\n        diversity, and consistency. Key finding: contrary to popular belief, distortion from prefix discrepancy is limited\n        and does not appear incremental. Reveals an interesting self-recovery ability of language models that counters harmful\n        effects of exposure bias.'\n    - title: Sequence-to-Sequence Learning as Beam-Search Optimization\n      authors: Wiseman, Rush\n      venue: EMNLP 2016\n      year: 2016\n      url: https://arxiv.org/abs/1606.02960\n      role: foundation\n      relevance: 提出 beam-aware 训练将训练目标与测试时解码统一，量化 teacher forcing 的 train-test discrepancy 对序列生成质量的影响。paper_framing SP1 明确引用为\n        exposure bias 在 sequence generation 中的量化先例\n      abstract: Proposes a model and beam-search training scheme that extends seq2seq to learn global sequence scores, avoiding\n        local training biases and unifying training loss with test-time usage. Outperforms attention-based seq2seq on word ordering,\n        parsing, and machine translation.\n    - title: 'Bridging the Gap between Training and Inference for Neural Machine Translation'\n      authors: Zhang, Feng, Meng, You, Liu\n      venue: ACL 2019\n      year: 2019\n      url: https://arxiv.org/abs/1906.02448\n      role: method-component\n      relevance: 在训练时混合 ground truth 和 model-generated tokens 作为上下文，用 sentence-level optimum 选择预测序列。直接对应论文 W8 中讨论的\n        exposure bias mitigation 实验方向——若应用于 auxiliary attention loss 可能缩小 30x gap\n      abstract: Addresses exposure bias in NMT by sampling context words from both ground truth and model predictions during\n        training, selecting predicted sequences with sentence-level optimum. Achieves significant improvements on Chinese-English\n        and WMT14 English-German translation.\n    - title: Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation\n      authors: Arora, El Asri, Bahuleyan, Cheung\n      venue: ACL Findings 2022\n      year: 2022\n      url: https://arxiv.org/abs/2204.01171\n      role: theoretical-foundation\n      relevance: 用 imitation learning 框架证明 exposure bias 导致 compounding error accumulation，且 perplexity 无法捕捉此累积效应。直接支撑论文核心论证：auxiliary\n        attention loss 的 PPL 正常但 GAR 崩溃，因为 perplexity 掩盖了分布偏移对 attention pattern 的破坏\n      abstract: Shows that exposure bias leads to accumulation of errors in autoregressive generation. Analyzes why perplexity\n        fails to capture this accumulation. Empirically demonstrates that compounding errors from train-test mismatch degrade\n        generation quality even when perplexity appears normal.\n    - title: Scheduled Sampling for Transformers\n      authors: Mihaylova, Martins\n      venue: ACL SRW 2019\n      year: 2019\n      url: https://arxiv.org/abs/1906.07651\n      role: method-component\n      relevance: 将 Bengio 2015 的 scheduled sampling 扩展到 transformer 架构，通过 two-pass decoding 策略解决 transformer 非自回归 decoder 的适配问题。直接相关于论文\n        Discussion 中讨论的 scheduled sampling 应用于 auxiliary attention loss 的未来方向\n      abstract: Extends scheduled sampling to Transformer architecture via two-pass decoding strategy. Proposes structural changes\n        to allow mixing of teacher-forced embeddings and model predictions during transformer training for exposure bias mitigation.\n  gradient_conflict_mtl:",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 384,
        "oldLines": 6,
        "newStart": 384,
        "newLines": 49,
        "lines": [
          "         diversity, and consistency. Key finding: contrary to popular belief, distortion from prefix discrepancy is limited",
          "         and does not appear incremental. Reveals an interesting self-recovery ability of language models that counters harmful",
          "         effects of exposure bias.'",
          "+    - title: Sequence-to-Sequence Learning as Beam-Search Optimization",
          "+      authors: Wiseman, Rush",
          "+      venue: EMNLP 2016",
          "+      year: 2016",
          "+      url: https://arxiv.org/abs/1606.02960",
          "+      role: foundation",
          "+      relevance: 提出 beam-aware 训练将训练目标与测试时解码统一，量化 teacher forcing 的 train-test discrepancy 对序列生成质量的影响。paper_framing SP1 明确引用为",
          "+        exposure bias 在 sequence generation 中的量化先例",
          "+      abstract: Proposes a model and beam-search training scheme that extends seq2seq to learn global sequence scores, avoiding",
          "+        local training biases and unifying training loss with test-time usage. Outperforms attention-based seq2seq on word ordering,",
          "+        parsing, and machine translation.",
          "+    - title: 'Bridging the Gap between Training and Inference for Neural Machine Translation'",
          "+      authors: Zhang, Feng, Meng, You, Liu",
          "+      venue: ACL 2019",
          "+      year: 2019",
          "+      url: https://arxiv.org/abs/1906.02448",
          "+      role: method-component",
          "+      relevance: 在训练时混合 ground truth 和 model-generated tokens 作为上下文，用 sentence-level optimum 选择预测序列。直接对应论文 W8 中讨论的",
          "+        exposure bias mitigation 实验方向——若应用于 auxiliary attention loss 可能缩小 30x gap",
          "+      abstract: Addresses exposure bias in NMT by sampling context words from both ground truth and model predictions during",
          "+        training, selecting predicted sequences with sentence-level optimum. Achieves significant improvements on Chinese-English",
          "+        and WMT14 English-German translation.",
          "+    - title: Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation",
          "+      authors: Arora, El Asri, Bahuleyan, Cheung",
          "+      venue: ACL Findings 2022",
          "+      year: 2022",
          "+      url: https://arxiv.org/abs/2204.01171",
          "+      role: theoretical-foundation",
          "+      relevance: 用 imitation learning 框架证明 exposure bias 导致 compounding error accumulation，且 perplexity 无法捕捉此累积效应。直接支撑论文核心论证：auxiliary",
          "+        attention loss 的 PPL 正常但 GAR 崩溃，因为 perplexity 掩盖了分布偏移对 attention pattern 的破坏",
          "+      abstract: Shows that exposure bias leads to accumulation of errors in autoregressive generation. Analyzes why perplexity",
          "+        fails to capture this accumulation. Empirically demonstrates that compounding errors from train-test mismatch degrade",
          "+        generation quality even when perplexity appears normal.",
          "+    - title: Scheduled Sampling for Transformers",
          "+      authors: Mihaylova, Martins",
          "+      venue: ACL SRW 2019",
          "+      year: 2019",
          "+      url: https://arxiv.org/abs/1906.07651",
          "+      role: method-component",
          "+      relevance: 将 Bengio 2015 的 scheduled sampling 扩展到 transformer 架构，通过 two-pass decoding 策略解决 transformer 非自回归 decoder 的适配问题。直接相关于论文",
          "+        Discussion 中讨论的 scheduled sampling 应用于 auxiliary attention loss 的未来方向",
          "+      abstract: Extends scheduled sampling to Transformer architecture via two-pass decoding strategy. Proposes structural changes",
          "+        to allow mixing of teacher-forced embeddings and model predictions during transformer training for exposure bias mitigation.",
          "   gradient_conflict_mtl:",
          "     description: Multi-task gradient conflict resolution, gradient surgery, and loss balancing methods",
          "     papers:"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "8e79287d-db66-412d-b3e4-99dccbe757d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-22T04:55:19.781Z_

Now adding paper 5 (Li et al. 2024) to the multi_turn_attention section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86e08201-ea04-4f1b-9293-8058402d1fc7",
  "isSidechain": false,
  "requestId": "req_011CbH1dF1fcPTVWUgK5SyH8",
  "type": "assistant",
  "uuid": "99e33679-5d7f-4108-b01d-f711175d06e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tQZ2Y5wFE2AMRCS1UTzr8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1705,
      "cache_read_input_tokens": 67218,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1705,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 67218,
          "cache_creation_input_tokens": 1705,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1705
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

_source line 73 · 2026-05-22T04:55:20.611Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AUXkLwVKBCkDfY1fDP3rRg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
  "offset": 95,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99e33679-5d7f-4108-b01d-f711175d06e3",
  "isSidechain": false,
  "requestId": "req_011CbH1dF1fcPTVWUgK5SyH8",
  "type": "assistant",
  "uuid": "76c19d4d-6d27-4b20-8e9e-1d0e984f0db8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tQZ2Y5wFE2AMRCS1UTzr8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1705,
      "cache_read_input_tokens": 67218,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1705,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 67218,
          "cache_creation_input_tokens": 1705,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1705
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

_source line 74 · 2026-05-22T04:55:20.617Z_

<details><summary>↩ Tool result · `toolu_01AUXkLwVKBCkDfY1fDP3rRg`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76c19d4d-6d27-4b20-8e9e-1d0e984f0db8",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "820ad179-43d8-401a-84d4-525c0a2bf6d0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
      "content": "      abstract: Performance highest at beginning/end of context, degrading for middle positions.\n    - title: 'Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models'\n      authors: Anonymous\n      venue: arXiv 2025\n      year: 2025\n      url: https://arxiv.org/abs/2512.23578\n      role: context\n      relevance: 多轮对话中 style instruction 遵循衰减，system message 比 user message 更严重\n      abstract: Style instruction in system messages degrades more than in user messages across turns.\n  residual_gating:\n    description: Gating mechanisms for transformer residual connections and adaptive depth\n    papers:\n    - title: 'Mixture-of-Depths: Dynamically allocating compute in transformer-based language models'\n      authors: Raposo et al.\n      venue: arXiv 2024 (Google DeepMind)",
      "numLines": 15,
      "startLine": 95,
      "totalLines": 497
    }
  },
  "sourceToolAssistantUUID": "76c19d4d-6d27-4b20-8e9e-1d0e984f0db8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-22T04:55:31.495Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01LyYdhgRYvATePtQqQikEvF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
  "old_string": "      abstract: Style instruction in system messages degrades more than in user messages across turns.\n  residual_gating:",
  "new_string": "      abstract: Style instruction in system messages degrades more than in user messages across turns.\n    - title: Measuring and Controlling Instruction (In)Stability in Language Model Dialogs\n      authors: Li, Liu, Bashkansky, Bau, Viégas, Pfister, Wattenberg\n      venue: COLM 2024\n      year: 2024\n      url: https://arxiv.org/abs/2402.10962\n      role: direct-competitor\n      relevance: 定量测量多轮对话中 instruction compliance 衰减（同 GAR decay），识别 transformer attention decay 为机制，提出 split-softmax\n        推理时修复。最直接的对比工作——同一问题（attention 到 system prompt 随轮次衰减），但从推理端而非训练端干预\n      abstract: Quantifies instruction drift in multi-turn LLM dialogs via self-chat benchmark. LLaMA2-70B and GPT-3.5 show\n        significant instruction instability within 8 turns. Identifies attention decay as mechanism and proposes split-softmax,\n        a training-free inference-time method that amplifies attention to system prompt tokens.\n  residual_gating:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "820ad179-43d8-401a-84d4-525c0a2bf6d0",
  "isSidechain": false,
  "requestId": "req_011CbH1dXy8xjbuQYWTTNjux",
  "type": "assistant",
  "uuid": "54e15c6f-d5db-44fc-93fd-39e18dd2d8ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TogEe3EBKKLhTqYoJjhdcZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 419,
      "cache_read_input_tokens": 68923,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 419,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 68923,
          "cache_creation_input_tokens": 419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 419
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

_source line 76 · 2026-05-22T04:55:31.511Z_

<details><summary>↩ Tool result · `toolu_01LyYdhgRYvATePtQqQikEvF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54e15c6f-d5db-44fc-93fd-39e18dd2d8ac",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "ac8fd298-b6ba-411d-8fac-e7ed51131857",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
    "oldString": "      abstract: Style instruction in system messages degrades more than in user messages across turns.\n  residual_gating:",
    "newString": "      abstract: Style instruction in system messages degrades more than in user messages across turns.\n    - title: Measuring and Controlling Instruction (In)Stability in Language Model Dialogs\n      authors: Li, Liu, Bashkansky, Bau, Viégas, Pfister, Wattenberg\n      venue: COLM 2024\n      year: 2024\n      url: https://arxiv.org/abs/2402.10962\n      role: direct-competitor\n      relevance: 定量测量多轮对话中 instruction compliance 衰减（同 GAR decay），识别 transformer attention decay 为机制，提出 split-softmax\n        推理时修复。最直接的对比工作——同一问题（attention 到 system prompt 随轮次衰减），但从推理端而非训练端干预\n      abstract: Quantifies instruction drift in multi-turn LLM dialogs via self-chat benchmark. LLaMA2-70B and GPT-3.5 show\n        significant instruction instability within 8 turns. Identifies attention decay as mechanism and proposes split-softmax,\n        a training-free inference-time method that amplifies attention to system prompt tokens.\n  residual_gating:",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 101,
        "oldLines": 6,
        "newStart": 101,
        "newLines": 17,
        "lines": [
          "       role: context",
          "       relevance: 多轮对话中 style instruction 遵循衰减，system message 比 user message 更严重",
          "       abstract: Style instruction in system messages degrades more than in user messages across turns.",
          "+    - title: Measuring and Controlling Instruction (In)Stability in Language Model Dialogs",
          "+      authors: Li, Liu, Bashkansky, Bau, Viégas, Pfister, Wattenberg",
          "+      venue: COLM 2024",
          "+      year: 2024",
          "+      url: https://arxiv.org/abs/2402.10962",
          "+      role: direct-competitor",
          "+      relevance: 定量测量多轮对话中 instruction compliance 衰减（同 GAR decay），识别 transformer attention decay 为机制，提出 split-softmax",
          "+        推理时修复。最直接的对比工作——同一问题（attention 到 system prompt 随轮次衰减），但从推理端而非训练端干预",
          "+      abstract: Quantifies instruction drift in multi-turn LLM dialogs via self-chat benchmark. LLaMA2-70B and GPT-3.5 show",
          "+        significant instruction instability within 8 turns. Identifies attention decay as mechanism and proposes split-softmax,",
          "+        a training-free inference-time method that amplifies attention to system prompt tokens.",
          "   residual_gating:",
          "     description: Gating mechanisms for transformer residual connections and adaptive depth",
          "     papers:"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "54e15c6f-d5db-44fc-93fd-39e18dd2d8ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-22T04:55:35.820Z_

Now let me also add these papers to references.bib since they should be citable.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac8fd298-b6ba-411d-8fac-e7ed51131857",
  "isSidechain": false,
  "requestId": "req_011CbH1eLDV1fnsRXguxLbM9",
  "type": "assistant",
  "uuid": "17199292-9d86-4407-ab8f-3ba5d302c3c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0151u5tAaux1ZDojwJbjs6GY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 69342,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 523,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 69342,
          "cache_creation_input_tokens": 523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 523
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

_source line 78 · 2026-05-22T04:55:36.462Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Lc4jR8q9dmARu37zVsTXfH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib",
  "offset": 297,
  "limit": 45
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17199292-9d86-4407-ab8f-3ba5d302c3c9",
  "isSidechain": false,
  "requestId": "req_011CbH1eLDV1fnsRXguxLbM9",
  "type": "assistant",
  "uuid": "7d960f3d-e58d-4dc0-bd35-6fa18f283382",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0151u5tAaux1ZDojwJbjs6GY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 69342,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 523,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 69342,
          "cache_creation_input_tokens": 523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 523
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

_source line 79 · 2026-05-22T04:55:36.479Z_

<details><summary>↩ Tool result · `toolu_01Lc4jR8q9dmARu37zVsTXfH`</summary>

```text
297	% ============================================================
298	% Exposure Bias
299	% ============================================================
300	
301	@inproceedings{bengio2015scheduled,
302	  author    = {Bengio and Vinyals and Jaitly and Shazeer},
303	  title     = {{Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks}},
304	  booktitle = {Advances in Neural Information Processing Systems},
305	  year      = {2015},
306	  url       = {https://arxiv.org/abs/1506.03099}
307	}
308	
309	@inproceedings{ranzato2016sequence,
310	  author    = {Ranzato and Chopra and Auli and Zaremba},
311	  title     = {{Sequence Level Training with Recurrent Neural Networks}},
312	  booktitle = {International Conference on Learning Representations},
313	  year      = {2016},
314	  url       = {https://arxiv.org/abs/1511.06732}
315	}
316	
317	@inproceedings{lamb2016professor,
318	  author    = {Lamb and Goyal and Zhang and Zhang and Courville and Bengio},
319	  title     = {{Professor Forcing: A New Algorithm for Training Recurrent Networks}},
320	  booktitle = {Advances in Neural Information Processing Systems},
321	  year      = {2016},
322	  url       = {https://arxiv.org/abs/1610.09038}
323	}
324	
325	@inproceedings{leblond2018searnn,
326	  author    = {Leblond and Alayrac and Osokin and Lacoste-Julien},
327	  title     = {{SEARNN: Training RNNs with Global-Local Losses}},
328	  booktitle = {International Conference on Learning Representations},
329	  year      = {2018},
330	  url       = {https://arxiv.org/abs/1706.04499}
331	}
332	
333	@article{he2019exposure,
334	  author  = {He and Zhang and Zhou and Glass},
335	  title   = {{Quantifying Exposure Bias for Neural Language Generation}},
336	  journal = {arXiv preprint arXiv:1905.10617},
337	  year    = {2019},
338	  url     = {https://arxiv.org/abs/1905.10617}
339	}
340	
341	% ============================================================
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d960f3d-e58d-4dc0-bd35-6fa18f283382",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "95cc6552-fbbc-46bd-ac61-6c224b9d10a3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib",
      "content": "% ============================================================\n% Exposure Bias\n% ============================================================\n\n@inproceedings{bengio2015scheduled,\n  author    = {Bengio and Vinyals and Jaitly and Shazeer},\n  title     = {{Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2015},\n  url       = {https://arxiv.org/abs/1506.03099}\n}\n\n@inproceedings{ranzato2016sequence,\n  author    = {Ranzato and Chopra and Auli and Zaremba},\n  title     = {{Sequence Level Training with Recurrent Neural Networks}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1511.06732}\n}\n\n@inproceedings{lamb2016professor,\n  author    = {Lamb and Goyal and Zhang and Zhang and Courville and Bengio},\n  title     = {{Professor Forcing: A New Algorithm for Training Recurrent Networks}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1610.09038}\n}\n\n@inproceedings{leblond2018searnn,\n  author    = {Leblond and Alayrac and Osokin and Lacoste-Julien},\n  title     = {{SEARNN: Training RNNs with Global-Local Losses}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1706.04499}\n}\n\n@article{he2019exposure,\n  author  = {He and Zhang and Zhou and Glass},\n  title   = {{Quantifying Exposure Bias for Neural Language Generation}},\n  journal = {arXiv preprint arXiv:1905.10617},\n  year    = {2019},\n  url     = {https://arxiv.org/abs/1905.10617}\n}\n\n% ============================================================",
      "numLines": 45,
      "startLine": 297,
      "totalLines": 404
    }
  },
  "sourceToolAssistantUUID": "7d960f3d-e58d-4dc0-bd35-6fa18f283382",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 80_

```json
{
  "type": "last-prompt",
  "leafUuid": "95cc6552-fbbc-46bd-ac61-6c224b9d10a3",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "Fill literature map with core related papers",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Tool call

_source line 82 · 2026-05-22T04:55:46.280Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01LU2N5r8BUoj8mJxKKQB3Vs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib",
  "old_string": "@article{he2019exposure,\n  author  = {He and Zhang and Zhou and Glass},\n  title   = {{Quantifying Exposure Bias for Neural Language Generation}},\n  journal = {arXiv preprint arXiv:1905.10617},\n  year    = {2019},\n  url     = {https://arxiv.org/abs/1905.10617}\n}\n\n% ============================================================\n% Gradient Conflict / Multi-Task Learning",
  "new_string": "@article{he2019exposure,\n  author  = {He and Zhang and Zhou and Glass},\n  title   = {{Quantifying Exposure Bias for Neural Language Generation}},\n  journal = {arXiv preprint arXiv:1905.10617},\n  year    = {2019},\n  url     = {https://arxiv.org/abs/1905.10617}\n}\n\n@inproceedings{wiseman2016sequence,\n  author    = {Wiseman and Rush},\n  title     = {{Sequence-to-Sequence Learning as Beam-Search Optimization}},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1606.02960}\n}\n\n@inproceedings{zhang2019bridging,\n  author    = {Zhang and Feng and Meng and You and Liu},\n  title     = {{Bridging the Gap between Training and Inference for Neural Machine Translation}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1906.02448}\n}\n\n@inproceedings{arora2022exposure,\n  author    = {Arora and El Asri and Bahuleyan and Cheung},\n  title     = {{Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation}},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2204.01171}\n}\n\n@inproceedings{mihaylova2019scheduled,\n  author    = {Mihaylova and Martins},\n  title     = {{Scheduled Sampling for Transformers}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics: Student Research Workshop},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1906.07651}\n}\n\n% ============================================================\n% Instruction Stability\n% ============================================================\n\n@inproceedings{li2024measuring,\n  author    = {Li and Liu and Bashkansky and Bau and Vi\\'{e}gas and Pfister and Wattenberg},\n  title     = {{Measuring and Controlling Instruction (In)Stability in Language Model Dialogs}},\n  booktitle = {Conference on Language Modeling},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.10962}\n}\n\n% ============================================================\n% Gradient Conflict / Multi-Task Learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95cc6552-fbbc-46bd-ac61-6c224b9d10a3",
  "isSidechain": false,
  "requestId": "req_011CbH1ehf5PdFjLVhoGdQtP",
  "type": "assistant",
  "uuid": "dcfe86e6-da3b-4e8d-9892-8078904305bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoVPMPXMFjGgsB7RkERt7X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 793,
      "cache_read_input_tokens": 69865,
      "output_tokens": 917,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 793,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 917,
          "cache_read_input_tokens": 69865,
          "cache_creation_input_tokens": 793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 793
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

_source line 83 · 2026-05-22T04:55:46.301Z_

<details><summary>↩ Tool result · `toolu_01LU2N5r8BUoj8mJxKKQB3Vs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcfe86e6-da3b-4e8d-9892-8078904305bd",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "9ca2fcb8-3567-4398-9a0f-d8285c41d439",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib",
    "oldString": "@article{he2019exposure,\n  author  = {He and Zhang and Zhou and Glass},\n  title   = {{Quantifying Exposure Bias for Neural Language Generation}},\n  journal = {arXiv preprint arXiv:1905.10617},\n  year    = {2019},\n  url     = {https://arxiv.org/abs/1905.10617}\n}\n\n% ============================================================\n% Gradient Conflict / Multi-Task Learning",
    "newString": "@article{he2019exposure,\n  author  = {He and Zhang and Zhou and Glass},\n  title   = {{Quantifying Exposure Bias for Neural Language Generation}},\n  journal = {arXiv preprint arXiv:1905.10617},\n  year    = {2019},\n  url     = {https://arxiv.org/abs/1905.10617}\n}\n\n@inproceedings{wiseman2016sequence,\n  author    = {Wiseman and Rush},\n  title     = {{Sequence-to-Sequence Learning as Beam-Search Optimization}},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1606.02960}\n}\n\n@inproceedings{zhang2019bridging,\n  author    = {Zhang and Feng and Meng and You and Liu},\n  title     = {{Bridging the Gap between Training and Inference for Neural Machine Translation}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1906.02448}\n}\n\n@inproceedings{arora2022exposure,\n  author    = {Arora and El Asri and Bahuleyan and Cheung},\n  title     = {{Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation}},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2204.01171}\n}\n\n@inproceedings{mihaylova2019scheduled,\n  author    = {Mihaylova and Martins},\n  title     = {{Scheduled Sampling for Transformers}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics: Student Research Workshop},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1906.07651}\n}\n\n% ============================================================\n% Instruction Stability\n% ============================================================\n\n@inproceedings{li2024measuring,\n  author    = {Li and Liu and Bashkansky and Bau and Vi\\'{e}gas and Pfister and Wattenberg},\n  title     = {{Measuring and Controlling Instruction (In)Stability in Language Model Dialogs}},\n  booktitle = {Conference on Language Modeling},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.10962}\n}\n\n% ============================================================\n% Gradient Conflict / Multi-Task Learning",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 338,
        "oldLines": 7,
        "newStart": 338,
        "newLines": 51,
        "lines": [
          "   url     = {https://arxiv.org/abs/1905.10617}",
          " }",
          " ",
          "+@inproceedings{wiseman2016sequence,",
          "+  author    = {Wiseman and Rush},",
          "+  title     = {{Sequence-to-Sequence Learning as Beam-Search Optimization}},",
          "+  booktitle = {Conference on Empirical Methods in Natural Language Processing},",
          "+  year      = {2016},",
          "+  url       = {https://arxiv.org/abs/1606.02960}",
          "+}",
          "+",
          "+@inproceedings{zhang2019bridging,",
          "+  author    = {Zhang and Feng and Meng and You and Liu},",
          "+  title     = {{Bridging the Gap between Training and Inference for Neural Machine Translation}},",
          "+  booktitle = {Annual Meeting of the Association for Computational Linguistics},",
          "+  year      = {2019},",
          "+  url       = {https://arxiv.org/abs/1906.02448}",
          "+}",
          "+",
          "+@inproceedings{arora2022exposure,",
          "+  author    = {Arora and El Asri and Bahuleyan and Cheung},",
          "+  title     = {{Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation}},",
          "+  booktitle = {Findings of the Association for Computational Linguistics: ACL},",
          "+  year      = {2022},",
          "+  url       = {https://arxiv.org/abs/2204.01171}",
          "+}",
          "+",
          "+@inproceedings{mihaylova2019scheduled,",
          "+  author    = {Mihaylova and Martins},",
          "+  title     = {{Scheduled Sampling for Transformers}},",
          "+  booktitle = {Annual Meeting of the Association for Computational Linguistics: Student Research Workshop},",
          "+  year      = {2019},",
          "+  url       = {https://arxiv.org/abs/1906.07651}",
          "+}",
          "+",
          " % ============================================================",
          "+% Instruction Stability",
          "+% ============================================================",
          "+",
          "+@inproceedings{li2024measuring,",
          "+  author    = {Li and Liu and Bashkansky and Bau and Vi\\'{e}gas and Pfister and Wattenberg},",
          "+  title     = {{Measuring and Controlling Instruction (In)Stability in Language Model Dialogs}},",
          "+  booktitle = {Conference on Language Modeling},",
          "+  year      = {2024},",
          "+  url       = {https://arxiv.org/abs/2402.10962}",
          "+}",
          "+",
          "+% ============================================================",
          " % Gradient Conflict / Multi-Task Learning",
          " % ============================================================",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "dcfe86e6-da3b-4e8d-9892-8078904305bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 84 · 2026-05-22T04:55:50.409Z_

Let me verify the literature_map.yaml is valid YAML.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ca2fcb8-3567-4398-9a0f-d8285c41d439",
  "isSidechain": false,
  "requestId": "req_011CbH1fRNpQjkeci9dNcWev",
  "type": "assistant",
  "uuid": "48ca0c1c-d98d-4cc2-8a42-666907992e27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFKw7xjiN25c7krAQ6ukx4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 971,
      "cache_read_input_tokens": 70658,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 70658,
          "cache_creation_input_tokens": 971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 971
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

_source line 85 · 2026-05-22T04:55:51.175Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VshLnBF7VkLa4n4erAQoZk`</summary>

```json
{
  "command": "python3 -c \"import yaml; yaml.safe_load(open('literature_map.yaml')); print('YAML valid')\"",
  "description": "Validate literature_map.yaml syntax"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48ca0c1c-d98d-4cc2-8a42-666907992e27",
  "isSidechain": false,
  "requestId": "req_011CbH1fRNpQjkeci9dNcWev",
  "type": "assistant",
  "uuid": "fecd6d79-0ca7-4b16-ad17-0ff21011b62b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFKw7xjiN25c7krAQ6ukx4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 971,
      "cache_read_input_tokens": 70658,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 70658,
          "cache_creation_input_tokens": 971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 971
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

_source line 86 · 2026-05-22T04:55:51.764Z_

<details><summary>↩ Tool result · reported error · `toolu_01VshLnBF7VkLa4n4erAQoZk`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 1, in &lt;module>
    import yaml; yaml.safe_load(open('literature_map.yaml')); print('YAML valid')
                 ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/yaml/__init__.py", line 125, in safe_load
    return load(stream, SafeLoader)
  File "/usr/lib/python3/dist-packages/yaml/__init__.py", line 81, in load
    return loader.get_single_data()
           ~~~~~~~~~~~~~~~~~~~~~~^^
  File "/usr/lib/python3/dist-packages/yaml/constructor.py", line 49, in get_single_data
    node = self.get_single_node()
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 36, in get_single_node
    document = self.compose_document()
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 55, in compose_document
    node = self.compose_node(None, None)
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 84, in compose_node
    node = self.compose_mapping_node(anchor)
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 133, in compose_mapping_node
    item_value = self.compose_node(node, item_key)
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 84, in compose_node
    node = self.compose_mapping_node(anchor)
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 133, in compose_mapping_node
    item_value = self.compose_node(node, item_key)
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 84, in compose_node
    node = self.compose_mapping_node(anchor)
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 133, in compose_mapping_node
    item_value = self.compose_node(node, item_key)
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 82, in compose_node
    node = self.compose_sequence_node(anchor)
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 111, in compose_sequence_node
    node.value.append(self.compose_node(node, index))
                      ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 84, in compose_node
    node = self.compose_mapping_node(anchor)
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 127, in compose_mapping_node
    while not self.check_event(MappingEndEvent):
              ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/yaml/parser.py", line 98, in check_event
    self.current_event = self.state()
                         ~~~~~~~~~~^^
  File "/usr/lib/python3/dist-packages/yaml/parser.py", line 428, in parse_block_mapping_key
    if self.check_token(KeyToken):
       ~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/yaml/scanner.py", line 116, in check_token
    self.fetch_more_tokens()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "/usr/lib/python3/dist-packages/yaml/scanner.py", line 223, in fetch_more_tokens
    return self.fetch_value()
           ~~~~~~~~~~~~~~~~^^
  File "/usr/lib/python3/dist-packages/yaml/scanner.py", line 577, in fetch_value
    raise ScannerError(None, None,
            "mapping values are not allowed here",
            self.get_mark())
yaml.scanner.ScannerError: mapping values are not allowed here
  in "literature_map.yaml", line 420, column 39
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fecd6d79-0ca7-4b16-ad17-0ff21011b62b",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "b3dd5e57-6e3c-4a5f-8aaf-6d31a4991b49",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 1, in &lt;module>\n    import yaml; yaml.safe_load(open('literature_map.yaml')); print('YAML valid')\n                 ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3/dist-packages/yaml/__init__.py\", line 125, in safe_load\n    return load(stream, SafeLoader)\n  File \"/usr/lib/python3/dist-packages/yaml/__init__.py\", line 81, in load\n    return loader.get_single_data()\n           ~~~~~~~~~~~~~~~~~~~~~~^^\n  File \"/usr/lib/python3/dist-packages/yaml/constructor.py\", line 49, in get_single_data\n    node = self.get_single_node()\n  File \"/usr/lib/python3/dist-packages/yaml/composer.py\", line 36, in get_single_node\n    document = self.compose_document()\n  File \"/usr/lib/python3/dist-packages/yaml/composer.py\", line 55, in compose_document\n    node = self.compose_node(None, None)\n  File \"/usr/lib/python3/dist-packages/yaml/composer.py\", line 84, in compose_node\n    node = self.compose_mapping_node(anchor)\n  File \"/usr/lib/python3/dist-packages/yaml/composer.py\", line 133, in compose_mapping_node\n    item_value = self.compose_node(node, item_key)\n  File \"/usr/lib/python3/dist-packages/yaml/composer.py\", line 84, in compose_node\n    node = self.compose_mapping_node(anchor)\n  File \"/usr/lib/python3/dist-packages/yaml/composer.py\", line 133, in compose_mapping_node\n    item_value = self.compose_node(node, item_key)\n  File \"/usr/lib/python3/dist-packages/yaml/composer.py\", line 84, in compose_node\n    node = self.compose_mapping_node(anchor)\n  File \"/usr/lib/python3/dist-packages/yaml/composer.py\", line 133, in compose_mapping_node\n    item_value = self.compose_node(node, item_key)\n  File \"/usr/lib/python3/dist-packages/yaml/composer.py\", line 82, in compose_node\n    node = self.compose_sequence_node(anchor)\n  File \"/usr/lib/python3/dist-packages/yaml/composer.py\", line 111, in compose_sequence_node\n    node.value.append(self.compose_node(node, index))\n                      ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^\n  File \"/usr/lib/python3/dist-packages/yaml/composer.py\", line 84, in compose_node\n    node = self.compose_mapping_node(anchor)\n  File \"/usr/lib/python3/dist-packages/yaml/composer.py\", line 127, in compose_mapping_node\n    while not self.check_event(MappingEndEvent):\n              ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3/dist-packages/yaml/parser.py\", line 98, in check_event\n    self.current_event = self.state()\n                         ~~~~~~~~~~^^\n  File \"/usr/lib/python3/dist-packages/yaml/parser.py\", line 428, in parse_block_mapping_key\n    if self.check_token(KeyToken):\n       ~~~~~~~~~~~~~~~~^^^^^^^^^^\n  File \"/usr/lib/python3/dist-packages/yaml/scanner.py\", line 116, in check_token\n    self.fetch_more_tokens()\n    ~~~~~~~~~~~~~~~~~~~~~~^^\n  File \"/usr/lib/python3/dist-packages/yaml/scanner.py\", line 223, in fetch_more_tokens\n    return self.fetch_value()\n           ~~~~~~~~~~~~~~~~^^\n  File \"/usr/lib/python3/dist-packages/yaml/scanner.py\", line 577, in fetch_value\n    raise ScannerError(None, None,\n            \"mapping values are not allowed here\",\n            self.get_mark())\nyaml.scanner.ScannerError: mapping values are not allowed here\n  in \"literature_map.yaml\", line 420, column 39",
  "sourceToolAssistantUUID": "fecd6d79-0ca7-4b16-ad17-0ff21011b62b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 87 · 2026-05-22T04:55:51.766Z_

```json
{
  "parentUuid": "b3dd5e57-6e3c-4a5f-8aaf-6d31a4991b49",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "980a6e5f-fd1a-4a6a-91b6-551f38500dce",
  "timestamp": "2026-05-22T04:55:51.766Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 88 · 2026-05-22T04:55:54.958Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QEJByoToSvGDqpj7GBwrLA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
  "offset": 415,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "980a6e5f-fd1a-4a6a-91b6-551f38500dce",
  "isSidechain": false,
  "requestId": "req_011CbH1fpjznZRfFJDrKkRGP",
  "type": "assistant",
  "uuid": "6e774e21-8d1e-4313-bc63-a072d8eca167",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qfR8q1tzWqmqYJMSfsjme",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 71629,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1275,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 71629,
          "cache_creation_input_tokens": 1275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1275
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

_source line 89 · 2026-05-22T04:55:54.967Z_

<details><summary>↩ Tool result · `toolu_01QEJByoToSvGDqpj7GBwrLA`</summary>

```text
415	      relevance: 在训练时混合 ground truth 和 model-generated tokens 作为上下文，用 sentence-level optimum 选择预测序列。直接对应论文 W8 中讨论的
416	        exposure bias mitigation 实验方向——若应用于 auxiliary attention loss 可能缩小 30x gap
417	      abstract: Addresses exposure bias in NMT by sampling context words from both ground truth and model predictions during
418	        training, selecting predicted sequences with sentence-level optimum. Achieves significant improvements on Chinese-English
419	        and WMT14 English-German translation.
420	    - title: Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation
421	      authors: Arora, El Asri, Bahuleyan, Cheung
422	      venue: ACL Findings 2022
423	      year: 2022
424	      url: https://arxiv.org/abs/2204.01171
425	      role: theoretical-foundation
426	      relevance: 用 imitation learning 框架证明 exposure bias 导致 compounding error accumulation，且 perplexity 无法捕捉此累积效应。直接支撑论文核心论证：auxiliary
427	        attention loss 的 PPL 正常但 GAR 崩溃，因为 perplexity 掩盖了分布偏移对 attention pattern 的破坏
428	      abstract: Shows that exposure bias leads to accumulation of errors in autoregressive generation. Analyzes why perplexity
429	        fails to capture this accumulation. Empirically demonstrates that compounding errors from train-test mismatch degrade
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e774e21-8d1e-4313-bc63-a072d8eca167",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "ed437593-4107-4d48-bf0a-fcbc036c3bd9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
      "content": "      relevance: 在训练时混合 ground truth 和 model-generated tokens 作为上下文，用 sentence-level optimum 选择预测序列。直接对应论文 W8 中讨论的\n        exposure bias mitigation 实验方向——若应用于 auxiliary attention loss 可能缩小 30x gap\n      abstract: Addresses exposure bias in NMT by sampling context words from both ground truth and model predictions during\n        training, selecting predicted sequences with sentence-level optimum. Achieves significant improvements on Chinese-English\n        and WMT14 English-German translation.\n    - title: Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation\n      authors: Arora, El Asri, Bahuleyan, Cheung\n      venue: ACL Findings 2022\n      year: 2022\n      url: https://arxiv.org/abs/2204.01171\n      role: theoretical-foundation\n      relevance: 用 imitation learning 框架证明 exposure bias 导致 compounding error accumulation，且 perplexity 无法捕捉此累积效应。直接支撑论文核心论证：auxiliary\n        attention loss 的 PPL 正常但 GAR 崩溃，因为 perplexity 掩盖了分布偏移对 attention pattern 的破坏\n      abstract: Shows that exposure bias leads to accumulation of errors in autoregressive generation. Analyzes why perplexity\n        fails to capture this accumulation. Empirically demonstrates that compounding errors from train-test mismatch degrade",
      "numLines": 15,
      "startLine": 415,
      "totalLines": 508
    }
  },
  "sourceToolAssistantUUID": "6e774e21-8d1e-4313-bc63-a072d8eca167",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 90 · 2026-05-22T04:55:59.416Z_

<details><summary>Logged reasoning block</summary>

```text
The issue is that `title: Why Exposure Bias Matters: An Imitation Learning Perspective...` has a colon in the title value, which YAML interprets as a mapping separator. I need to quote the title. Let me fix this.

Line 420 has `- title: Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation` - the colon after "Matters" is causing issues. I need to quote the title.

Let me also check if there are other similar issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed437593-4107-4d48-bf0a-fcbc036c3bd9",
  "isSidechain": false,
  "requestId": "req_011CbH1g54xgiPKERdDjpHuZ",
  "type": "assistant",
  "uuid": "a997aaad-4a28-4ba6-b968-88b6040ed72f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bo1Fe4EjN9mnSVciH8aYU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 72904,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 358,
          "cache_read_input_tokens": 72904,
          "cache_creation_input_tokens": 567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 567
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

_source line 91 · 2026-05-22T04:55:59.921Z_

The colon in the title is causing YAML parsing issues. Let me fix the unquoted titles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a997aaad-4a28-4ba6-b968-88b6040ed72f",
  "isSidechain": false,
  "requestId": "req_011CbH1g54xgiPKERdDjpHuZ",
  "type": "assistant",
  "uuid": "3b073c1b-96bd-4a16-b36e-45b71f6509f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bo1Fe4EjN9mnSVciH8aYU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 72904,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 358,
          "cache_read_input_tokens": 72904,
          "cache_creation_input_tokens": 567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 567
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

_source line 92 · 2026-05-22T04:56:01.342Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01MW6CMKw9GwhuZgwgqfcZD7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
  "old_string": "    - title: Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation",
  "new_string": "    - title: 'Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b073c1b-96bd-4a16-b36e-45b71f6509f8",
  "isSidechain": false,
  "requestId": "req_011CbH1g54xgiPKERdDjpHuZ",
  "type": "assistant",
  "uuid": "9c6f47e1-1bd1-402d-89e5-d559d030f6c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bo1Fe4EjN9mnSVciH8aYU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 72904,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 358,
          "cache_read_input_tokens": 72904,
          "cache_creation_input_tokens": 567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 567
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

_source line 93 · 2026-05-22T04:56:01.367Z_

<details><summary>↩ Tool result · `toolu_01MW6CMKw9GwhuZgwgqfcZD7`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c6f47e1-1bd1-402d-89e5-d559d030f6c6",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "37c6121a-b757-4437-8472-2f9f03c23d3b",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
    "oldString": "    - title: Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation",
    "newString": "    - title: 'Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation'",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 417,
        "oldLines": 7,
        "newStart": 417,
        "newLines": 7,
        "lines": [
          "       abstract: Addresses exposure bias in NMT by sampling context words from both ground truth and model predictions during",
          "         training, selecting predicted sequences with sentence-level optimum. Achieves significant improvements on Chinese-English",
          "         and WMT14 English-German translation.",
          "-    - title: Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation",
          "+    - title: 'Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation'",
          "       authors: Arora, El Asri, Bahuleyan, Cheung",
          "       venue: ACL Findings 2022",
          "       year: 2022"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "9c6f47e1-1bd1-402d-89e5-d559d030f6c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 94_

```json
{
  "type": "last-prompt",
  "leafUuid": "37c6121a-b757-4437-8472-2f9f03c23d3b",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Runtime record

_source line 95_

```json
{
  "type": "ai-title",
  "aiTitle": "Fill literature map with core related papers",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Tool call

_source line 96 · 2026-05-22T04:56:06.847Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QkVJdmc9E9XsT5U5wuw8bL`</summary>

```json
{
  "command": "python3 -c \"import yaml; yaml.safe_load(open('literature_map.yaml')); print('YAML valid')\"",
  "description": "Validate literature_map.yaml syntax"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37c6121a-b757-4437-8472-2f9f03c23d3b",
  "isSidechain": false,
  "requestId": "req_011CbH1gYWDZCEAKbBmH5rzK",
  "type": "assistant",
  "uuid": "0ec43411-00ad-4e41-ab4b-9090f67d173d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDA7P6i4b98yX3Qs7BMzs2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 411,
      "cache_read_input_tokens": 73471,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 411,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 73471,
          "cache_creation_input_tokens": 411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 411
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

_source line 97 · 2026-05-22T04:56:07.017Z_

<details><summary>↩ Tool result · `toolu_01QkVJdmc9E9XsT5U5wuw8bL`</summary>

```text
YAML valid
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ec43411-00ad-4e41-ab4b-9090f67d173d",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "18c0df26-6bc3-4be2-8d6d-699ff3446f19",
  "toolUseResult": {
    "stdout": "YAML valid",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0ec43411-00ad-4e41-ab4b-9090f67d173d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 98 · 2026-05-22T04:56:10.080Z_

YAML is valid. Let me verify the added entries look correct.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18c0df26-6bc3-4be2-8d6d-699ff3446f19",
  "isSidechain": false,
  "requestId": "req_011CbH1gwybTRr3j4b3td6Cf",
  "type": "assistant",
  "uuid": "ecdab55a-9c68-4ff9-a7a7-a630ca8e0132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dmy1pLy7wBKJikREJM5j3K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 121,
      "cache_read_input_tokens": 73882,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 277,
          "cache_read_input_tokens": 73882,
          "cache_creation_input_tokens": 121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 121
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

_source line 99 · 2026-05-22T04:56:12.837Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01L5dn5gn3749jzeGeToBDmZ`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\ndata = yaml.safe_load(open('literature_map.yaml'))\n# Count papers in exposure_bias\neb = data['categories']['exposure_bias']['papers']\nprint(f'exposure_bias: {len(eb)} papers')\nfor p in eb:\n    print(f'  - {p[\\\"year\\\"]} {p[\\\"authors\\\"]}: {p[\\\"title\\\"][:60]}')\n\n# Count papers in multi_turn_attention\nmt = data['categories']['multi_turn_attention']['papers']\nprint(f'\\nmulti_turn_attention: {len(mt)} papers')\nfor p in mt:\n    print(f'  - {p[\\\"year\\\"]} {p[\\\"authors\\\"]}: {p[\\\"title\\\"][:60]}')\n\"",
  "description": "List papers in updated categories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecdab55a-9c68-4ff9-a7a7-a630ca8e0132",
  "isSidechain": false,
  "requestId": "req_011CbH1gwybTRr3j4b3td6Cf",
  "type": "assistant",
  "uuid": "50440ed9-6eab-4d95-87ff-4816396a71b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dmy1pLy7wBKJikREJM5j3K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 121,
      "cache_read_input_tokens": 73882,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 277,
          "cache_read_input_tokens": 73882,
          "cache_creation_input_tokens": 121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 121
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

_source line 100 · 2026-05-22T04:56:12.992Z_

<details><summary>↩ Tool result · `toolu_01L5dn5gn3749jzeGeToBDmZ`</summary>

```text
exposure_bias: 9 papers
  - 2015 Bengio, Vinyals, Jaitly, Shazeer: Scheduled Sampling for Sequence Prediction with Recurrent Ne
  - 2016 Ranzato, Chopra, Auli, Zaremba: Sequence Level Training with Recurrent Neural Networks
  - 2016 Lamb, Goyal, Zhang, Zhang, Courville, Bengio: Professor Forcing: A New Algorithm for Training Recurrent Ne
  - 2018 Leblond, Alayrac, Osokin, Lacoste-Julien: SEARNN: Training RNNs with Global-Local Losses
  - 2019 He, Zhang, Zhou, Glass: Quantifying Exposure Bias for Neural Language Generation
  - 2016 Wiseman, Rush: Sequence-to-Sequence Learning as Beam-Search Optimization
  - 2019 Zhang, Feng, Meng, You, Liu: Bridging the Gap between Training and Inference for Neural M
  - 2022 Arora, El Asri, Bahuleyan, Cheung: Why Exposure Bias Matters: An Imitation Learning Perspective
  - 2019 Mihaylova, Martins: Scheduled Sampling for Transformers

multi_turn_attention: 6 papers
  - 2026 Dongre, Hsieh, Lai, Yoon, Bui, Hakkani-Tur: When Attention Closes: How LLMs Lose the Thread in Multi-Tur
  - 2025 Levy et al.: LLMs Get Lost In Multi-Turn Conversation
  - 2026 Liu et al.: Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conver
  - 2023 Liu et al.: Lost in the Middle: How Language Models Use Long Contexts
  - 2025 Anonymous: Style Amnesia: Investigating Speaking Style Degradation and 
  - 2024 Li, Liu, Bashkansky, Bau, Viégas, Pfister, Wattenberg: Measuring and Controlling Instruction (In)Stability in Langu
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50440ed9-6eab-4d95-87ff-4816396a71b6",
  "isSidechain": false,
  "promptId": "e109313b-1278-4670-ab8e-60aef5944391",
  "type": "user",
  "uuid": "e5747cea-cc4f-4273-a829-2f2aa8a3b0af",
  "toolUseResult": {
    "stdout": "exposure_bias: 9 papers\n  - 2015 Bengio, Vinyals, Jaitly, Shazeer: Scheduled Sampling for Sequence Prediction with Recurrent Ne\n  - 2016 Ranzato, Chopra, Auli, Zaremba: Sequence Level Training with Recurrent Neural Networks\n  - 2016 Lamb, Goyal, Zhang, Zhang, Courville, Bengio: Professor Forcing: A New Algorithm for Training Recurrent Ne\n  - 2018 Leblond, Alayrac, Osokin, Lacoste-Julien: SEARNN: Training RNNs with Global-Local Losses\n  - 2019 He, Zhang, Zhou, Glass: Quantifying Exposure Bias for Neural Language Generation\n  - 2016 Wiseman, Rush: Sequence-to-Sequence Learning as Beam-Search Optimization\n  - 2019 Zhang, Feng, Meng, You, Liu: Bridging the Gap between Training and Inference for Neural M\n  - 2022 Arora, El Asri, Bahuleyan, Cheung: Why Exposure Bias Matters: An Imitation Learning Perspective\n  - 2019 Mihaylova, Martins: Scheduled Sampling for Transformers\n\nmulti_turn_attention: 6 papers\n  - 2026 Dongre, Hsieh, Lai, Yoon, Bui, Hakkani-Tur: When Attention Closes: How LLMs Lose the Thread in Multi-Tur\n  - 2025 Levy et al.: LLMs Get Lost In Multi-Turn Conversation\n  - 2026 Liu et al.: Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conver\n  - 2023 Liu et al.: Lost in the Middle: How Language Models Use Long Contexts\n  - 2025 Anonymous: Style Amnesia: Investigating Speaking Style Degradation and \n  - 2024 Li, Liu, Bashkansky, Bau, Viégas, Pfister, Wattenberg: Measuring and Controlling Instruction (In)Stability in Langu",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "50440ed9-6eab-4d95-87ff-4816396a71b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 101 · 2026-05-22T04:56:25.126Z_

All 5 papers added successfully. Here's the summary:

---

**添加了 5 篇论文，覆盖 4 个方向：**

| # | 论文 | 方向 | Role | 关联 |
|---|------|------|------|------|
| 1 | Wiseman & Rush 2016, "Sequence-to-Sequence Learning as Beam-Search Optimization" (EMNLP) | a. Exposure bias | foundation | paper_framing SP1 明确引用为 exposure bias 量化先例 |
| 2 | Zhang et al. 2019, "Bridging the Gap between Training and Inference for NMT" (ACL) | d. Scheduled sampling | method-component | 训练时混合 model-generated tokens，对应 W8 讨论的 mitigation 方向 |
| 3 | Arora et al. 2022, "Why Exposure Bias Matters" (ACL Findings) | a. Exposure bias | theoretical-foundation | 用 imitation learning 证明 exposure bias → compounding errors 且 PPL 无法捕捉——直接支撑 30x gap 论证 |
| 4 | Mihaylova & Martins 2019, "Scheduled Sampling for Transformers" (ACL SRW) | d. Scheduled sampling | method-component | 将 scheduled sampling 扩展到 transformer，相关于 Discussion 中的 mitigation 未来方向 |
| 5 | Li et al. 2024, "Measuring and Controlling Instruction (In)Stability in Language Model Dialogs" (COLM) | b/c. GAR + Multi-turn attention | direct-competitor | 同一问题（attention 到 system prompt 随轮次衰减），识别 attention decay 机制，提出 split-softmax 推理时修复 |

同时已将 5 篇的 bib entries 添加到 `paper/references.bib`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5747cea-cc4f-4273-a829-2f2aa8a3b0af",
  "isSidechain": false,
  "requestId": "req_011CbH1hPV1m62XUGns1fCeP",
  "type": "assistant",
  "uuid": "b1da6556-5574-420d-b1f1-0200c8214b51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019syhjTENpoUeKySif7U78B",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 74003,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 825,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 512,
          "cache_read_input_tokens": 74003,
          "cache_creation_input_tokens": 825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 825
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

_source line 102_

```json
{
  "type": "last-prompt",
  "leafUuid": "b1da6556-5574-420d-b1f1-0200c8214b51",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---

### Runtime record

_source line 103_

```json
{
  "type": "ai-title",
  "aiTitle": "Fill literature map with core related papers",
  "sessionId": "79c91556-39c7-41c3-af87-6b5fcf7be31a"
}
```

---
