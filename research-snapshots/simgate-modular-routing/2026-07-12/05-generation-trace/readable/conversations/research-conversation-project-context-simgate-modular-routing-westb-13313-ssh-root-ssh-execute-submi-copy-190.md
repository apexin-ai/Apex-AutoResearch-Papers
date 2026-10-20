# Research conversation: <project_context> # 项目: simgate-modular-routing ## 运行环境 - 服务器名: westb-13313 - SSH 账户: root（调用 ssh_execute / submit_train

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/1b6d4d6b-1d9c-49fa-b51d-68bdda96025d.jsonl`
- **Structured JSON:** [`5ce59c03f46845e0cf4c.json`](../../sessions/5c/5ce59c03f46845e0cf4c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T10:18:30.880Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T10:18:30.880Z",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "content": "&lt;project_context>\n# 项目: simgate-modular-routing\n\n## 运行环境\n- 服务器名: westb-13313\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westb.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/simgate-modular-routing\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n对论文 Introduction 和 Related Work 做三处结构优化。**只改结构和流畅度，不改动任何具体数值或 claim 强度。**\n\n## 任务\n\n### 1. Introduction 数字重复合并\n- 读 `docs/paper/introduction.tex`\n- 找到 line ~12 和 line ~22 处重复出现的 78.9% 和 DAF=90.4%\n- 首次出现（line ~12 附近）保留详细数字\n- 第二处（line ~22 附近）改为简化引用，如 \"the dominance pattern described above\" 或 \"this death-avoidance dominance\"，不再重复具体数字\n\n### 2. Introduction 加\"问题重要性\"段\n- 在 line ~10 后（\"现有方法\"段之前）加 1-2 句\n- 说明为什么 death asymmetry 值得研究——可以从以下角度选：影响 agent 部署安全性、routing 策略选择、benchmark 可靠性\n- 保持简洁，不超过 2 句话\n\n### 3. Related Work 拆段\n- 读 `docs/paper/related_work.tex`\n- 找到 \"Safe RL and LLM Agents\" 段（line ~19 附近）\n- 拆为两段：\n  - **LLM Agent Environments**: ScienceWorld、ALFWorld、AgentBench 等环境，以及 ReAct/Reflexion/LATS 等推理方法\n  - **Safe RL**: safe RL survey、安全约束相关工作\n- 各段保持紧凑，结尾有明确的定位句（说明本文与这些工作的关系）\n\n## 硬约束\n- **不改动任何具体数值**（78.9%、90.4%、42.9% 等全部保留原样，不改措辞强度）\n- **不改动 Contribution 列表**\n- **不加破折号（— 或 –）**\n- **不加 -ing 短语结尾**\n- **不用黑名单词**（delve/leverage/utilize/facilitate/myriad/plethora）\n\n## 文件路径\n本地：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/`\n- introduction.tex\n- related_work.tex\n\n完成后报告具体改了什么（原文 → 新文本的 diff 摘要）。"
}
```

---

### Runtime record

_source line 2 · 2026-05-17T10:18:30.884Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T10:18:30.884Z",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-17T10:18:30.920Z_

&lt;project_context>
# 项目: simgate-modular-routing

## 运行环境
- 服务器名: westb-13313
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.westb.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/simgate-modular-routing


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
对论文 Introduction 和 Related Work 做三处结构优化。**只改结构和流畅度，不改动任何具体数值或 claim 强度。**

## 任务

### 1. Introduction 数字重复合并
- 读 `docs/paper/introduction.tex`
- 找到 line ~12 和 line ~22 处重复出现的 78.9% 和 DAF=90.4%
- 首次出现（line ~12 附近）保留详细数字
- 第二处（line ~22 附近）改为简化引用，如 "the dominance pattern described above" 或 "this death-avoidance dominance"，不再重复具体数字

### 2. Introduction 加"问题重要性"段
- 在 line ~10 后（"现有方法"段之前）加 1-2 句
- 说明为什么 death asymmetry 值得研究——可以从以下角度选：影响 agent 部署安全性、routing 策略选择、benchmark 可靠性
- 保持简洁，不超过 2 句话

### 3. Related Work 拆段
- 读 `docs/paper/related_work.tex`
- 找到 "Safe RL and LLM Agents" 段（line ~19 附近）
- 拆为两段：
  - **LLM Agent Environments**: ScienceWorld、ALFWorld、AgentBench 等环境，以及 ReAct/Reflexion/LATS 等推理方法
  - **Safe RL**: safe RL survey、安全约束相关工作
- 各段保持紧凑，结尾有明确的定位句（说明本文与这些工作的关系）

## 硬约束
- **不改动任何具体数值**（78.9%、90.4%、42.9% 等全部保留原样，不改措辞强度）
- **不改动 Contribution 列表**
- **不加破折号（— 或 –）**
- **不加 -ing 短语结尾**
- **不用黑名单词**（delve/leverage/utilize/facilitate/myriad/plethora）

## 文件路径
本地：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/`
- introduction.tex
- related_work.tex

完成后报告具体改了什么（原文 → 新文本的 diff 摘要）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a57bc070-52fc-47b4-b3d4-773f9e41a3e0",
  "type": "user",
  "uuid": "080f70dc-2985-4cdb-8d62-320acb8b044b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T10:18:30.919Z_

```json
{
  "parentUuid": "080f70dc-2985-4cdb-8d62-320acb8b044b",
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
  "uuid": "abc59004-81ad-46fc-8d1a-4b1bff8e53ea",
  "timestamp": "2026-05-17T10:18:30.919Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T10:18:30.919Z_

```json
{
  "parentUuid": "abc59004-81ad-46fc-8d1a-4b1bff8e53ea",
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
  "uuid": "110e99fb-d0b9-4787-a2c9-1e0b8aa7da08",
  "timestamp": "2026-05-17T10:18:30.919Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-17T10:18:30.919Z_

```json
{
  "parentUuid": "110e99fb-d0b9-4787-a2c9-1e0b8aa7da08",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9f4ee8be-24e2-440e-96f9-0dece079e96e",
  "timestamp": "2026-05-17T10:18:30.919Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
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
  "aiTitle": "Optimize paper structure in Introduction and Related Work",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d"
}
```

---

### Assistant

_source line 8 · 2026-05-17T10:18:33.859Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read both files first to understand the current content and make the requested changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f4ee8be-24e2-440e-96f9-0dece079e96e",
  "isSidechain": false,
  "requestId": "req_011Cb7yEHuPTEGKWuiBNoQfa",
  "type": "assistant",
  "uuid": "dde0e6f2-55ad-4748-9f39-247deecb8d0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mp3rHNh6Nejs9FxNsaatwr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12710,
      "cache_read_input_tokens": 11841,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 196,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12710
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

_source line 9 · 2026-05-17T10:18:34.977Z_

<details open><summary>🔧 Tool call — Read · `toolu_01USrax99P8hvqzQjVQvCWCP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dde0e6f2-55ad-4748-9f39-247deecb8d0e",
  "isSidechain": false,
  "requestId": "req_011Cb7yEHuPTEGKWuiBNoQfa",
  "type": "assistant",
  "uuid": "cd948e26-3aa4-4be2-86ec-37d34e07049c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mp3rHNh6Nejs9FxNsaatwr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12710,
      "cache_read_input_tokens": 11841,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 196,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12710
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

_source line 10 · 2026-05-17T10:18:34.986Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JHxX1XVHZNa4Gx2mvffVar`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd948e26-3aa4-4be2-86ec-37d34e07049c",
  "isSidechain": false,
  "requestId": "req_011Cb7yEHuPTEGKWuiBNoQfa",
  "type": "assistant",
  "uuid": "33433303-e916-4137-811e-82003a49169c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mp3rHNh6Nejs9FxNsaatwr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12710,
      "cache_read_input_tokens": 11841,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 196,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12710
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

_source line 11 · 2026-05-17T10:18:34.994Z_

<details><summary>↩ Tool result · `toolu_01USrax99P8hvqzQjVQvCWCP`</summary>

```text
1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	A Qwen2.5-7B-Instruct agent navigating ScienceWorld \cite{scienceworld-2022}, a text-based science simulation with 30 task types, faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \emph{when should an agent route computation externally versus reasoning internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision.
7	Toolformer \cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.
8	More recent adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}.
9	The shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.
10	But this assumption has never been systematically verified: \emph{what actually drives the value of routing decisions in interactive environments?}
11	
12	We propose a \emph{formal diagnostic framework} for answering this question. The framework comprises (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), a metric that decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, the framework reveals a surprisingly concentrated answer: \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95, penalty-independent); under ScienceWorld's default penalty ($P{=}100$), this corresponds to DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$).
13	The internal strategy's hallucination-induced failures trigger catastrophic agent death (a $-100$ penalty), while the deterministic strategy survives the same episodes.
14	Once death episodes are removed, the performance gap between strategies collapses to $\Delta_{\text{nd}} = +2.84$.
15	
16	This framework addresses a methodological gap.
17	The standard approach to generating routing labels, per-step oracle comparison, degenerates under sparse rewards.
18	In ScienceWorld, non-zero reward arrives only at episode termination; 97.4\% of steps (across 11 prescreened task types) produce identical scores regardless of modality, leaving no step-level signal to learn from (\S\ref{sec:collection}).
19	Keyword-based heuristics also fail structurally, as ScienceWorld actions lack science-specific terminology (\S\ref{sec:baselines}).
20	Our counterfactual approach runs complete episodes under pure-internal (ReAct \cite{react-2023}) and pure-deterministic strategies, then compares episode outcomes to generate routing labels (\S\ref{sec:collection}). The framework is applicable to any environment with controllable modality comparison and binary catastrophic outcomes, requiring only paired episode outcomes under two modalities.
21	
22	Among the 11 prescreened task types (245 episode pairs), 78.9\% of non-tie routing labels arise from death asymmetry (penalty-independent); DAF $= 90.4\%$ at $P{=}100$. The per-task $r = 0.97$ follows algebraically from death dominance when $P$ is constant (\S\ref{sec:death-decomp}).
23	
24	Two cross-context checks probe the specificity of this finding.
25	First, a MATH Level~4--5 evaluation ($N{=}795$ problems), using a code interpreter as the deterministic modality, confirms no routing signal without catastrophic failure: internal reasoning and code interpretation achieve near-identical accuracy ($73.5\%$ vs.\ $73.0\%$, $p = 0.81$).
26	Without death risk, modality routing confers no systematic advantage.
27	Second, a cross-model replication with Llama-3.1-8B-Instruct (7 task types, 70 episode pairs) shows direction-consistent death patterns for all task types, with a larger death-rate differential ($+34.3\%$ vs.\ $+26.6\%$ for Qwen; Appendix~\ref{app:cross-model}); the phenomenon generalizes across model families.
28	An exploratory router (Qwen3 with LoRA, 0.6B--4B) trained on these counterfactual labels yields flat step-level balanced accuracy across scales ($56$--$59\%$); at episode level, only 4B exceeds the always-deterministic baseline ($59.0\%$), while smaller scales remain at or below chance. Data scaling ($32{\times}$) ablations confirm this is structural rather than data-limited (\S\ref{sec:router-diagnostic}).
29	
30	Our contributions are:
31	\begin{enumerate}
32	    \item \textbf{A formal episode-level counterfactual framework (Algorithm~\ref{alg:labeling}) with dual penalty-independent and penalty-dependent metrics} for decomposing routing signal into death-avoidance and non-death components. The framework applies to any environment with controllable modality comparison and binary catastrophic outcomes (\S\ref{sec:collection}--\ref{sec:daf}).
33	
34	    \item \textbf{Empirical application to ScienceWorld} revealing that 78.9\% of non-tie routing labels are driven by death asymmetry (penalty-independent), with DAF $= 90.4\%$ at $P{=}100$ (penalty-dependent). Router training yields flat step-level accuracy across scales ($56$--$59\%$); at episode level, only 4B exceeds the baseline ($59.0\%$), and the cost is disproportionate to routing benefit. Death dominance renders always-deterministic near-optimal (\S\ref{sec:death-decomp}--\ref{sec:router-diagnostic}).
35	
36	    \item \textbf{Cross-environment diagnostic contrasts} establishing framework boundary conditions: MATH ($N{=}795$) confirms the predicted null ($p = 0.81$, no routing signal without catastrophic failure); ALFWorld ($N{=}135$) identifies an alternative mechanism (information asymmetry); a Llama-3.1-8B-Instruct pilot confirms directional consistency across model families. True quantitative DAF replication requires a second catastrophic-failure environment (\S\ref{sec:discussion}).
37	\end{enumerate}
38	
39	
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd948e26-3aa4-4be2-86ec-37d34e07049c",
  "isSidechain": false,
  "promptId": "a57bc070-52fc-47b4-b3d4-773f9e41a3e0",
  "type": "user",
  "uuid": "e8ef0765-96f9-487c-9b87-393b31a071f0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nLarge language models deployed as interactive agents must repeatedly decide \\emph{how} to compute: reason internally, or delegate to an external tool.\nA Qwen2.5-7B-Instruct agent navigating ScienceWorld \\cite{scienceworld-2022}, a text-based science simulation with 30 task types, faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \\emph{when should an agent route computation externally versus reasoning internally?}\n\nExisting routing approaches frame this as a capability or efficiency decision.\nToolformer \\cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \\cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \\cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.\nMore recent adaptive-computation methods route to different reasoning depths \\cite{cogrouter-2026,ares-2026} or model tiers \\cite{mtrouter-2026}.\nThe shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.\nBut this assumption has never been systematically verified: \\emph{what actually drives the value of routing decisions in interactive environments?}\n\nWe propose a \\emph{formal diagnostic framework} for answering this question. The framework comprises (i)~episode-level counterfactual labeling under pure strategies (\\S\\ref{sec:collection}--\\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), a metric that decomposes the routing score gap into death-avoidance and non-death components (\\S\\ref{sec:daf}). Applied to ScienceWorld, the framework reveals a surprisingly concentrated answer: \\textbf{78.9\\% of non-tie routing labels arise from death asymmetry} (75 of 95, penalty-independent); under ScienceWorld's default penalty ($P{=}100$), this corresponds to DAF $= 90.4\\%$ (95\\% CI: $[81.6\\%, 98.8\\%]$).\nThe internal strategy's hallucination-induced failures trigger catastrophic agent death (a $-100$ penalty), while the deterministic strategy survives the same episodes.\nOnce death episodes are removed, the performance gap between strategies collapses to $\\Delta_{\\text{nd}} = +2.84$.\n\nThis framework addresses a methodological gap.\nThe standard approach to generating routing labels, per-step oracle comparison, degenerates under sparse rewards.\nIn ScienceWorld, non-zero reward arrives only at episode termination; 97.4\\% of steps (across 11 prescreened task types) produce identical scores regardless of modality, leaving no step-level signal to learn from (\\S\\ref{sec:collection}).\nKeyword-based heuristics also fail structurally, as ScienceWorld actions lack science-specific terminology (\\S\\ref{sec:baselines}).\nOur counterfactual approach runs complete episodes under pure-internal (ReAct \\cite{react-2023}) and pure-deterministic strategies, then compares episode outcomes to generate routing labels (\\S\\ref{sec:collection}). The framework is applicable to any environment with controllable modality comparison and binary catastrophic outcomes, requiring only paired episode outcomes under two modalities.\n\nAmong the 11 prescreened task types (245 episode pairs), 78.9\\% of non-tie routing labels arise from death asymmetry (penalty-independent); DAF $= 90.4\\%$ at $P{=}100$. The per-task $r = 0.97$ follows algebraically from death dominance when $P$ is constant (\\S\\ref{sec:death-decomp}).\n\nTwo cross-context checks probe the specificity of this finding.\nFirst, a MATH Level~4--5 evaluation ($N{=}795$ problems), using a code interpreter as the deterministic modality, confirms no routing signal without catastrophic failure: internal reasoning and code interpretation achieve near-identical accuracy ($73.5\\%$ vs.\\ $73.0\\%$, $p = 0.81$).\nWithout death risk, modality routing confers no systematic advantage.\nSecond, a cross-model replication with Llama-3.1-8B-Instruct (7 task types, 70 episode pairs) shows direction-consistent death patterns for all task types, with a larger death-rate differential ($+34.3\\%$ vs.\\ $+26.6\\%$ for Qwen; Appendix~\\ref{app:cross-model}); the phenomenon generalizes across model families.\nAn exploratory router (Qwen3 with LoRA, 0.6B--4B) trained on these counterfactual labels yields flat step-level balanced accuracy across scales ($56$--$59\\%$); at episode level, only 4B exceeds the always-deterministic baseline ($59.0\\%$), while smaller scales remain at or below chance. Data scaling ($32{\\times}$) ablations confirm this is structural rather than data-limited (\\S\\ref{sec:router-diagnostic}).\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{A formal episode-level counterfactual framework (Algorithm~\\ref{alg:labeling}) with dual penalty-independent and penalty-dependent metrics} for decomposing routing signal into death-avoidance and non-death components. The framework applies to any environment with controllable modality comparison and binary catastrophic outcomes (\\S\\ref{sec:collection}--\\ref{sec:daf}).\n\n    \\item \\textbf{Empirical application to ScienceWorld} revealing that 78.9\\% of non-tie routing labels are driven by death asymmetry (penalty-independent), with DAF $= 90.4\\%$ at $P{=}100$ (penalty-dependent). Router training yields flat step-level accuracy across scales ($56$--$59\\%$); at episode level, only 4B exceeds the baseline ($59.0\\%$), and the cost is disproportionate to routing benefit. Death dominance renders always-deterministic near-optimal (\\S\\ref{sec:death-decomp}--\\ref{sec:router-diagnostic}).\n\n    \\item \\textbf{Cross-environment diagnostic contrasts} establishing framework boundary conditions: MATH ($N{=}795$) confirms the predicted null ($p = 0.81$, no routing signal without catastrophic failure); ALFWorld ($N{=}135$) identifies an alternative mechanism (information asymmetry); a Llama-3.1-8B-Instruct pilot confirms directional consistency across model families. True quantitative DAF replication requires a second catastrophic-failure environment (\\S\\ref{sec:discussion}).\n\\end{enumerate}\n\n\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  },
  "sourceToolAssistantUUID": "cd948e26-3aa4-4be2-86ec-37d34e07049c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T10:18:34.992Z_

<details><summary>↩ Tool result · `toolu_01JHxX1XVHZNa4Gx2mvffVar`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}.
5	Toolformer \cite{toolformer-2023} teaches LLMs to insert API calls via self-supervised loss filtering; ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask; ReTool \cite{retool-2025} applies RL to discover when code execution is preferable to chain-of-thought.
6	These focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
7	Recent concurrent work sharpens this question: \citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect, \citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \citet{tool-use-tax-2026} quantify a ``tool-use tax,'' and \citet{to-call-or-not-2026} propose a necessity--utility--affordability framework. Our decomposition provides environment-grounded evidence: in ScienceWorld, $90.4\%$ of routing signal at $P{=}100$ traces to catastrophic-failure prevention.
8	
9	\paragraph{Adaptive Computation and Routing.}
10	CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \cite{mtrouter-2026} addresses multi-turn routing.
11	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models.
12	These optimize \emph{how} to route; we reveal \emph{why} routing helps: in interactive environments, the dominant signal is catastrophic-failure avoidance.
13	
14	\paragraph{Counterfactual Evaluation in RL.}
15	Prior work generates counterfactual explanations for RL agents by perturbing individual actions within a fixed policy \citep{olson2021counterfactual, gajcin2023counterfactual, amitai2024explaining}.
16	Our approach differs in both purpose and granularity: we execute two complete episodes under different routing strategies, producing prospective paired comparisons that isolate routing signal \emph{before} any router is trained.
17	
18	\paragraph{Safe RL and LLM Agents.}
19	\citet{garcia2015comprehensive} survey safe RL methods; \citet{crpo-2021} develop constrained optimization with formal convergence guarantees. ScienceWorld \cite{scienceworld-2022} serves as our primary testbed; ALFWorld \cite{alfworld-2021} provides a complementary household environment; AgentBench \cite{agentbench-2024} offers systematic evaluation across diverse environments. ReAct \cite{react-2023} interleaves reasoning with actions and serves as our internal baseline; Reflexion \cite{reflexion-2023} extends this with verbal self-reflection; LATS \cite{lats-2024} unifies reasoning, acting, and planning via tree search. SelfCheckGPT \cite{selfcheckgpt-2023} identifies unreliable LLM outputs; our work shows that in interactive environments, such unreliability manifests as catastrophic agent death. Our decomposition reveals that modality routing functions primarily as a safety mechanism.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33433303-e916-4137-811e-82003a49169c",
  "isSidechain": false,
  "promptId": "a57bc070-52fc-47b4-b3d4-773f9e41a3e0",
  "type": "user",
  "uuid": "4e25683f-0a1d-4e91-8b12-b30a08ba3b5b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\n\\paragraph{Tool Use and External Computation in LLMs.}\nA growing body of work augments language models with external tools \\citep{tool-learning-survey-2024}.\nToolformer \\cite{toolformer-2023} teaches LLMs to insert API calls via self-supervised loss filtering; ToolkenGPT \\cite{toolkengpt-2023} represents tools as special tokens; ART \\cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \\cite{chameleon-2023} composes heterogeneous modules per subtask; ReTool \\cite{retool-2025} applies RL to discover when code execution is preferable to chain-of-thought.\nThese focus on \\emph{learning to use tools}; we ask a prior question: \\emph{what signal drives the routing decision?}\nRecent concurrent work sharpens this question: \\citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect, \\citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \\citet{tool-use-tax-2026} quantify a ``tool-use tax,'' and \\citet{to-call-or-not-2026} propose a necessity--utility--affordability framework. Our decomposition provides environment-grounded evidence: in ScienceWorld, $90.4\\%$ of routing signal at $P{=}100$ traces to catastrophic-failure prevention.\n\n\\paragraph{Adaptive Computation and Routing.}\nCogRouter \\cite{cogrouter-2026} adapts reasoning depth per step, ARES \\cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \\cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \\cite{mtrouter-2026} addresses multi-turn routing.\nRouteLLM \\citep{routellm-2024} learns routers from preference data to select between strong and weak models.\nThese optimize \\emph{how} to route; we reveal \\emph{why} routing helps: in interactive environments, the dominant signal is catastrophic-failure avoidance.\n\n\\paragraph{Counterfactual Evaluation in RL.}\nPrior work generates counterfactual explanations for RL agents by perturbing individual actions within a fixed policy \\citep{olson2021counterfactual, gajcin2023counterfactual, amitai2024explaining}.\nOur approach differs in both purpose and granularity: we execute two complete episodes under different routing strategies, producing prospective paired comparisons that isolate routing signal \\emph{before} any router is trained.\n\n\\paragraph{Safe RL and LLM Agents.}\n\\citet{garcia2015comprehensive} survey safe RL methods; \\citet{crpo-2021} develop constrained optimization with formal convergence guarantees. ScienceWorld \\cite{scienceworld-2022} serves as our primary testbed; ALFWorld \\cite{alfworld-2021} provides a complementary household environment; AgentBench \\cite{agentbench-2024} offers systematic evaluation across diverse environments. ReAct \\cite{react-2023} interleaves reasoning with actions and serves as our internal baseline; Reflexion \\cite{reflexion-2023} extends this with verbal self-reflection; LATS \\cite{lats-2024} unifies reasoning, acting, and planning via tree search. SelfCheckGPT \\cite{selfcheckgpt-2023} identifies unreliable LLM outputs; our work shows that in interactive environments, such unreliability manifests as catastrophic agent death. Our decomposition reveals that modality routing functions primarily as a safety mechanism.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "33433303-e916-4137-811e-82003a49169c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "leafUuid": "e8ef0765-96f9-487c-9b87-393b31a071f0",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Optimize paper structure in Introduction and Related Work",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d"
}
```

---

### Assistant

_source line 15 · 2026-05-17T10:19:03.030Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both files. Let me plan the three changes:

### 1. Introduction 数字重复合并
- Line 12 has the first occurrence: "78.9% of non-tie routing labels arise from death asymmetry" and "DAF = 90.4%"
- Line 22 has the second occurrence: "78.9% of non-tie routing labels arise from death asymmetry (penalty-independent); DAF $= 90.4\%$ at $P{=}100$"

I need to keep line 12's detailed numbers and simplify line 22 to refer back without repeating the numbers.


### 2. Introduction 加"问题重要性"段
Looking at the structure, lines 6-10 discuss existing routing approaches and end with a question about what drives routing value. The task asks me to insert 1-2 sentences after line 10 but before the existing methods section—but that's where those lines already are. I need to clarify whether the insertion point is actually after the existing methods discussion ends, or if I'm meant to add a separate paragraph about why death asymmetry matters for agent safety and benchmark reliability. Looking at the document structure against the CLAUDE.md norms, I see there's a gap—the current draft is missing the "问题重要性" section that should come after the research background and before the existing methods. The task is asking me to insert 1-2 sentences about why this problem matters, and I need to figure out where exactly that fits in the flow. I need to bridge the gap between identifying the routing question and proposing the framework—adding 1-2 sentences that explain why understanding what drives routing decisions matters for agent safety and benchmark design. Then I'm splitting the Related Work section to separate LLM agent environments from safe RL literature, which currently gets lumped together. Let me draft those connector sentences and reorganize that paragraph. I'm going to apply these edits now—replacing the repeated numbers with a back-reference, adding the deployment implications section, and splitting the Safe RL paragraph into two separate sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e25683f-0a1d-4e91-8b12-b30a08ba3b5b",
  "isSidechain": false,
  "requestId": "req_011Cb7yEbQ6kfYQK31GNz3Zd",
  "type": "assistant",
  "uuid": "5045e93f-0e5f-4181-8bdf-59b268f21878",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5eD4dqVPxhv2SzYCTcx99",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 24551,
      "output_tokens": 1756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1756,
          "cache_read_input_tokens": 24551,
          "cache_creation_input_tokens": 2975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2975
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

_source line 16 · 2026-05-17T10:19:03.070Z_

三处修改开始。

**Edit 1: Introduction line 22 — 合并重复数字**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5045e93f-0e5f-4181-8bdf-59b268f21878",
  "isSidechain": false,
  "requestId": "req_011Cb7yEbQ6kfYQK31GNz3Zd",
  "type": "assistant",
  "uuid": "50405677-1990-4514-b943-dcb50d326ba8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5eD4dqVPxhv2SzYCTcx99",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 24551,
      "output_tokens": 1756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1756,
          "cache_read_input_tokens": 24551,
          "cache_creation_input_tokens": 2975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2975
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

_source line 17 · 2026-05-17T10:19:05.735Z_

<details open><summary>🔧 Tool call — Edit · `toolu_017inJ6eBRse1LKY176U25DD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex",
  "old_string": "Among the 11 prescreened task types (245 episode pairs), 78.9\\% of non-tie routing labels arise from death asymmetry (penalty-independent); DAF $= 90.4\\%$ at $P{=}100$. The per-task $r = 0.97$ follows algebraically from death dominance when $P$ is constant (\\S\\ref{sec:death-decomp}).",
  "new_string": "Among the 11 prescreened task types (245 episode pairs), this death-avoidance dominance holds at the same magnitude reported above, both in the penalty-independent count and in DAF at $P{=}100$. The per-task $r = 0.97$ follows algebraically from death dominance when $P$ is constant (\\S\\ref{sec:death-decomp})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50405677-1990-4514-b943-dcb50d326ba8",
  "isSidechain": false,
  "requestId": "req_011Cb7yEbQ6kfYQK31GNz3Zd",
  "type": "assistant",
  "uuid": "e32f14ff-6a92-407f-a4e2-d7aad7e2e9e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5eD4dqVPxhv2SzYCTcx99",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 24551,
      "output_tokens": 1756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1756,
          "cache_read_input_tokens": 24551,
          "cache_creation_input_tokens": 2975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2975
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

_source line 18 · 2026-05-17T10:19:05.755Z_

<details><summary>↩ Tool result · `toolu_017inJ6eBRse1LKY176U25DD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e32f14ff-6a92-407f-a4e2-d7aad7e2e9e9",
  "isSidechain": false,
  "promptId": "a57bc070-52fc-47b4-b3d4-773f9e41a3e0",
  "type": "user",
  "uuid": "a67ff13b-3e7c-4bb5-8b41-82df9a7edd70",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex",
    "oldString": "Among the 11 prescreened task types (245 episode pairs), 78.9\\% of non-tie routing labels arise from death asymmetry (penalty-independent); DAF $= 90.4\\%$ at $P{=}100$. The per-task $r = 0.97$ follows algebraically from death dominance when $P$ is constant (\\S\\ref{sec:death-decomp}).",
    "newString": "Among the 11 prescreened task types (245 episode pairs), this death-avoidance dominance holds at the same magnitude reported above, both in the penalty-independent count and in DAF at $P{=}100$. The per-task $r = 0.97$ follows algebraically from death dominance when $P$ is constant (\\S\\ref{sec:death-decomp}).",
    "originalFile": "\\section{Introduction}\n\nLarge language models deployed as interactive agents must repeatedly decide \\emph{how} to compute: reason internally, or delegate to an external tool.\nA Qwen2.5-7B-Instruct agent navigating ScienceWorld \\cite{scienceworld-2022}, a text-based science simulation with 30 task types, faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \\emph{when should an agent route computation externally versus reasoning internally?}\n\nExisting routing approaches frame this as a capability or efficiency decision.\nToolformer \\cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \\cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \\cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.\nMore recent adaptive-computation methods route to different reasoning depths \\cite{cogrouter-2026,ares-2026} or model tiers \\cite{mtrouter-2026}.\nThe shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.\nBut this assumption has never been systematically verified: \\emph{what actually drives the value of routing decisions in interactive environments?}\n\nWe propose a \\emph{formal diagnostic framework} for answering this question. The framework comprises (i)~episode-level counterfactual labeling under pure strategies (\\S\\ref{sec:collection}--\\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), a metric that decomposes the routing score gap into death-avoidance and non-death components (\\S\\ref{sec:daf}). Applied to ScienceWorld, the framework reveals a surprisingly concentrated answer: \\textbf{78.9\\% of non-tie routing labels arise from death asymmetry} (75 of 95, penalty-independent); under ScienceWorld's default penalty ($P{=}100$), this corresponds to DAF $= 90.4\\%$ (95\\% CI: $[81.6\\%, 98.8\\%]$).\nThe internal strategy's hallucination-induced failures trigger catastrophic agent death (a $-100$ penalty), while the deterministic strategy survives the same episodes.\nOnce death episodes are removed, the performance gap between strategies collapses to $\\Delta_{\\text{nd}} = +2.84$.\n\nThis framework addresses a methodological gap.\nThe standard approach to generating routing labels, per-step oracle comparison, degenerates under sparse rewards.\nIn ScienceWorld, non-zero reward arrives only at episode termination; 97.4\\% of steps (across 11 prescreened task types) produce identical scores regardless of modality, leaving no step-level signal to learn from (\\S\\ref{sec:collection}).\nKeyword-based heuristics also fail structurally, as ScienceWorld actions lack science-specific terminology (\\S\\ref{sec:baselines}).\nOur counterfactual approach runs complete episodes under pure-internal (ReAct \\cite{react-2023}) and pure-deterministic strategies, then compares episode outcomes to generate routing labels (\\S\\ref{sec:collection}). The framework is applicable to any environment with controllable modality comparison and binary catastrophic outcomes, requiring only paired episode outcomes under two modalities.\n\nAmong the 11 prescreened task types (245 episode pairs), 78.9\\% of non-tie routing labels arise from death asymmetry (penalty-independent); DAF $= 90.4\\%$ at $P{=}100$. The per-task $r = 0.97$ follows algebraically from death dominance when $P$ is constant (\\S\\ref{sec:death-decomp}).\n\nTwo cross-context checks probe the specificity of this finding.\nFirst, a MATH Level~4--5 evaluation ($N{=}795$ problems), using a code interpreter as the deterministic modality, confirms no routing signal without catastrophic failure: internal reasoning and code interpretation achieve near-identical accuracy ($73.5\\%$ vs.\\ $73.0\\%$, $p = 0.81$).\nWithout death risk, modality routing confers no systematic advantage.\nSecond, a cross-model replication with Llama-3.1-8B-Instruct (7 task types, 70 episode pairs) shows direction-consistent death patterns for all task types, with a larger death-rate differential ($+34.3\\%$ vs.\\ $+26.6\\%$ for Qwen; Appendix~\\ref{app:cross-model}); the phenomenon generalizes across model families.\nAn exploratory router (Qwen3 with LoRA, 0.6B--4B) trained on these counterfactual labels yields flat step-level balanced accuracy across scales ($56$--$59\\%$); at episode level, only 4B exceeds the always-deterministic baseline ($59.0\\%$), while smaller scales remain at or below chance. Data scaling ($32{\\times}$) ablations confirm this is structural rather than data-limited (\\S\\ref{sec:router-diagnostic}).\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{A formal episode-level counterfactual framework (Algorithm~\\ref{alg:labeling}) with dual penalty-independent and penalty-dependent metrics} for decomposing routing signal into death-avoidance and non-death components. The framework applies to any environment with controllable modality comparison and binary catastrophic outcomes (\\S\\ref{sec:collection}--\\ref{sec:daf}).\n\n    \\item \\textbf{Empirical application to ScienceWorld} revealing that 78.9\\% of non-tie routing labels are driven by death asymmetry (penalty-independent), with DAF $= 90.4\\%$ at $P{=}100$ (penalty-dependent). Router training yields flat step-level accuracy across scales ($56$--$59\\%$); at episode level, only 4B exceeds the baseline ($59.0\\%$), and the cost is disproportionate to routing benefit. Death dominance renders always-deterministic near-optimal (\\S\\ref{sec:death-decomp}--\\ref{sec:router-diagnostic}).\n\n    \\item \\textbf{Cross-environment diagnostic contrasts} establishing framework boundary conditions: MATH ($N{=}795$) confirms the predicted null ($p = 0.81$, no routing signal without catastrophic failure); ALFWorld ($N{=}135$) identifies an alternative mechanism (information asymmetry); a Llama-3.1-8B-Instruct pilot confirms directional consistency across model families. True quantitative DAF replication requires a second catastrophic-failure environment (\\S\\ref{sec:discussion}).\n\\end{enumerate}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 7,
        "newStart": 19,
        "newLines": 7,
        "lines": [
          " Keyword-based heuristics also fail structurally, as ScienceWorld actions lack science-specific terminology (\\S\\ref{sec:baselines}).",
          " Our counterfactual approach runs complete episodes under pure-internal (ReAct \\cite{react-2023}) and pure-deterministic strategies, then compares episode outcomes to generate routing labels (\\S\\ref{sec:collection}). The framework is applicable to any environment with controllable modality comparison and binary catastrophic outcomes, requiring only paired episode outcomes under two modalities.",
          " ",
          "-Among the 11 prescreened task types (245 episode pairs), 78.9\\% of non-tie routing labels arise from death asymmetry (penalty-independent); DAF $= 90.4\\%$ at $P{=}100$. The per-task $r = 0.97$ follows algebraically from death dominance when $P$ is constant (\\S\\ref{sec:death-decomp}).",
          "+Among the 11 prescreened task types (245 episode pairs), this death-avoidance dominance holds at the same magnitude reported above, both in the penalty-independent count and in DAF at $P{=}100$. The per-task $r = 0.97$ follows algebraically from death dominance when $P$ is constant (\\S\\ref{sec:death-decomp}).",
          " ",
          " Two cross-context checks probe the specificity of this finding.",
          " First, a MATH Level~4--5 evaluation ($N{=}795$ problems), using a code interpreter as the deterministic modality, confirms no routing signal without catastrophic failure: internal reasoning and code interpretation achieve near-identical accuracy ($73.5\\%$ vs.\\ $73.0\\%$, $p = 0.81$)."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "e32f14ff-6a92-407f-a4e2-d7aad7e2e9e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-17T10:19:08.793Z_

**Edit 2: Introduction — 加"问题重要性"句**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a67ff13b-3e7c-4bb5-8b41-82df9a7edd70",
  "isSidechain": false,
  "requestId": "req_011Cb7yGs2kwCBed6MUvZLPr",
  "type": "assistant",
  "uuid": "a02a7df4-eebc-423c-af27-d326131eca68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7SyLJGTCKJBE5focrpGV9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 27526,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 277,
          "cache_read_input_tokens": 27526,
          "cache_creation_input_tokens": 1826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1826
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

_source line 20 · 2026-05-17T10:19:11.565Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Ayt5poDvyRmRvQKbpVsDUD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex",
  "old_string": "But this assumption has never been systematically verified: \\emph{what actually drives the value of routing decisions in interactive environments?}\n\nWe propose",
  "new_string": "But this assumption has never been systematically verified: \\emph{what actually drives the value of routing decisions in interactive environments?}\nUnderstanding what concentrates routing signal has direct implications for agent deployment safety and routing strategy selection: if the value of routing traces to a single failure mode, practitioners can replace complex learned routers with simpler safety-aware policies, reducing both computational cost and deployment risk.\n\nWe propose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a02a7df4-eebc-423c-af27-d326131eca68",
  "isSidechain": false,
  "requestId": "req_011Cb7yGs2kwCBed6MUvZLPr",
  "type": "assistant",
  "uuid": "ee77b89a-bc88-421b-a915-33ce0690aea1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7SyLJGTCKJBE5focrpGV9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 27526,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 277,
          "cache_read_input_tokens": 27526,
          "cache_creation_input_tokens": 1826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1826
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

_source line 21 · 2026-05-17T10:19:11.574Z_

<details><summary>↩ Tool result · `toolu_01Ayt5poDvyRmRvQKbpVsDUD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee77b89a-bc88-421b-a915-33ce0690aea1",
  "isSidechain": false,
  "promptId": "a57bc070-52fc-47b4-b3d4-773f9e41a3e0",
  "type": "user",
  "uuid": "3b43f787-d423-49e8-b247-6cdb11243924",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex",
    "oldString": "But this assumption has never been systematically verified: \\emph{what actually drives the value of routing decisions in interactive environments?}\n\nWe propose",
    "newString": "But this assumption has never been systematically verified: \\emph{what actually drives the value of routing decisions in interactive environments?}\nUnderstanding what concentrates routing signal has direct implications for agent deployment safety and routing strategy selection: if the value of routing traces to a single failure mode, practitioners can replace complex learned routers with simpler safety-aware policies, reducing both computational cost and deployment risk.\n\nWe propose",
    "originalFile": "\\section{Introduction}\n\nLarge language models deployed as interactive agents must repeatedly decide \\emph{how} to compute: reason internally, or delegate to an external tool.\nA Qwen2.5-7B-Instruct agent navigating ScienceWorld \\cite{scienceworld-2022}, a text-based science simulation with 30 task types, faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \\emph{when should an agent route computation externally versus reasoning internally?}\n\nExisting routing approaches frame this as a capability or efficiency decision.\nToolformer \\cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \\cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \\cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.\nMore recent adaptive-computation methods route to different reasoning depths \\cite{cogrouter-2026,ares-2026} or model tiers \\cite{mtrouter-2026}.\nThe shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.\nBut this assumption has never been systematically verified: \\emph{what actually drives the value of routing decisions in interactive environments?}\n\nWe propose a \\emph{formal diagnostic framework} for answering this question. The framework comprises (i)~episode-level counterfactual labeling under pure strategies (\\S\\ref{sec:collection}--\\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), a metric that decomposes the routing score gap into death-avoidance and non-death components (\\S\\ref{sec:daf}). Applied to ScienceWorld, the framework reveals a surprisingly concentrated answer: \\textbf{78.9\\% of non-tie routing labels arise from death asymmetry} (75 of 95, penalty-independent); under ScienceWorld's default penalty ($P{=}100$), this corresponds to DAF $= 90.4\\%$ (95\\% CI: $[81.6\\%, 98.8\\%]$).\nThe internal strategy's hallucination-induced failures trigger catastrophic agent death (a $-100$ penalty), while the deterministic strategy survives the same episodes.\nOnce death episodes are removed, the performance gap between strategies collapses to $\\Delta_{\\text{nd}} = +2.84$.\n\nThis framework addresses a methodological gap.\nThe standard approach to generating routing labels, per-step oracle comparison, degenerates under sparse rewards.\nIn ScienceWorld, non-zero reward arrives only at episode termination; 97.4\\% of steps (across 11 prescreened task types) produce identical scores regardless of modality, leaving no step-level signal to learn from (\\S\\ref{sec:collection}).\nKeyword-based heuristics also fail structurally, as ScienceWorld actions lack science-specific terminology (\\S\\ref{sec:baselines}).\nOur counterfactual approach runs complete episodes under pure-internal (ReAct \\cite{react-2023}) and pure-deterministic strategies, then compares episode outcomes to generate routing labels (\\S\\ref{sec:collection}). The framework is applicable to any environment with controllable modality comparison and binary catastrophic outcomes, requiring only paired episode outcomes under two modalities.\n\nAmong the 11 prescreened task types (245 episode pairs), this death-avoidance dominance holds at the same magnitude reported above, both in the penalty-independent count and in DAF at $P{=}100$. The per-task $r = 0.97$ follows algebraically from death dominance when $P$ is constant (\\S\\ref{sec:death-decomp}).\n\nTwo cross-context checks probe the specificity of this finding.\nFirst, a MATH Level~4--5 evaluation ($N{=}795$ problems), using a code interpreter as the deterministic modality, confirms no routing signal without catastrophic failure: internal reasoning and code interpretation achieve near-identical accuracy ($73.5\\%$ vs.\\ $73.0\\%$, $p = 0.81$).\nWithout death risk, modality routing confers no systematic advantage.\nSecond, a cross-model replication with Llama-3.1-8B-Instruct (7 task types, 70 episode pairs) shows direction-consistent death patterns for all task types, with a larger death-rate differential ($+34.3\\%$ vs.\\ $+26.6\\%$ for Qwen; Appendix~\\ref{app:cross-model}); the phenomenon generalizes across model families.\nAn exploratory router (Qwen3 with LoRA, 0.6B--4B) trained on these counterfactual labels yields flat step-level balanced accuracy across scales ($56$--$59\\%$); at episode level, only 4B exceeds the always-deterministic baseline ($59.0\\%$), while smaller scales remain at or below chance. Data scaling ($32{\\times}$) ablations confirm this is structural rather than data-limited (\\S\\ref{sec:router-diagnostic}).\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{A formal episode-level counterfactual framework (Algorithm~\\ref{alg:labeling}) with dual penalty-independent and penalty-dependent metrics} for decomposing routing signal into death-avoidance and non-death components. The framework applies to any environment with controllable modality comparison and binary catastrophic outcomes (\\S\\ref{sec:collection}--\\ref{sec:daf}).\n\n    \\item \\textbf{Empirical application to ScienceWorld} revealing that 78.9\\% of non-tie routing labels are driven by death asymmetry (penalty-independent), with DAF $= 90.4\\%$ at $P{=}100$ (penalty-dependent). Router training yields flat step-level accuracy across scales ($56$--$59\\%$); at episode level, only 4B exceeds the baseline ($59.0\\%$), and the cost is disproportionate to routing benefit. Death dominance renders always-deterministic near-optimal (\\S\\ref{sec:death-decomp}--\\ref{sec:router-diagnostic}).\n\n    \\item \\textbf{Cross-environment diagnostic contrasts} establishing framework boundary conditions: MATH ($N{=}795$) confirms the predicted null ($p = 0.81$, no routing signal without catastrophic failure); ALFWorld ($N{=}135$) identifies an alternative mechanism (information asymmetry); a Llama-3.1-8B-Instruct pilot confirms directional consistency across model families. True quantitative DAF replication requires a second catastrophic-failure environment (\\S\\ref{sec:discussion}).\n\\end{enumerate}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 6,
        "newStart": 8,
        "newLines": 7,
        "lines": [
          " More recent adaptive-computation methods route to different reasoning depths \\cite{cogrouter-2026,ares-2026} or model tiers \\cite{mtrouter-2026}.",
          " The shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.",
          " But this assumption has never been systematically verified: \\emph{what actually drives the value of routing decisions in interactive environments?}",
          "+Understanding what concentrates routing signal has direct implications for agent deployment safety and routing strategy selection: if the value of routing traces to a single failure mode, practitioners can replace complex learned routers with simpler safety-aware policies, reducing both computational cost and deployment risk.",
          " ",
          " We propose a \\emph{formal diagnostic framework} for answering this question. The framework comprises (i)~episode-level counterfactual labeling under pure strategies (\\S\\ref{sec:collection}--\\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), a metric that decomposes the routing score gap into death-avoidance and non-death components (\\S\\ref{sec:daf}). Applied to ScienceWorld, the framework reveals a surprisingly concentrated answer: \\textbf{78.9\\% of non-tie routing labels arise from death asymmetry} (75 of 95, penalty-independent); under ScienceWorld's default penalty ($P{=}100$), this corresponds to DAF $= 90.4\\%$ (95\\% CI: $[81.6\\%, 98.8\\%]$).",
          " The internal strategy's hallucination-induced failures trigger catastrophic agent death (a $-100$ penalty), while the deterministic strategy survives the same episodes."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "ee77b89a-bc88-421b-a915-33ce0690aea1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "leafUuid": "3b43f787-d423-49e8-b247-6cdb11243924",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Optimize paper structure in Introduction and Related Work",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d"
}
```

---

### Assistant

_source line 24 · 2026-05-17T10:19:13.940Z_

**Edit 3: Related Work — 拆 "Safe RL and LLM Agents" 为两段**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b43f787-d423-49e8-b247-6cdb11243924",
  "isSidechain": false,
  "requestId": "req_011Cb7yHHuimCE6ix7iA32Dd",
  "type": "assistant",
  "uuid": "d727392a-e39d-428b-85d5-c889be325eed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154wKx2gQFyFWFDPj8uiMKB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 332,
      "cache_read_input_tokens": 29352,
      "output_tokens": 721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 721,
          "cache_read_input_tokens": 29352,
          "cache_creation_input_tokens": 332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 332
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

_source line 25 · 2026-05-17T10:19:21.014Z_

<details open><summary>🔧 Tool call — Edit · `toolu_012DUFVSBLGxPoiwNYqxQYsJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex",
  "old_string": "\\paragraph{Safe RL and LLM Agents.}\n\\citet{garcia2015comprehensive} survey safe RL methods; \\citet{crpo-2021} develop constrained optimization with formal convergence guarantees. ScienceWorld \\cite{scienceworld-2022} serves as our primary testbed; ALFWorld \\cite{alfworld-2021} provides a complementary household environment; AgentBench \\cite{agentbench-2024} offers systematic evaluation across diverse environments. ReAct \\cite{react-2023} interleaves reasoning with actions and serves as our internal baseline; Reflexion \\cite{reflexion-2023} extends this with verbal self-reflection; LATS \\cite{lats-2024} unifies reasoning, acting, and planning via tree search. SelfCheckGPT \\cite{selfcheckgpt-2023} identifies unreliable LLM outputs; our work shows that in interactive environments, such unreliability manifests as catastrophic agent death. Our decomposition reveals that modality routing functions primarily as a safety mechanism.",
  "new_string": "\\paragraph{LLM Agent Environments and Reasoning.}\nScienceWorld \\cite{scienceworld-2022} serves as our primary testbed; ALFWorld \\cite{alfworld-2021} provides a complementary household environment; AgentBench \\cite{agentbench-2024} offers systematic evaluation across diverse environments. ReAct \\cite{react-2023} interleaves reasoning with actions and serves as our internal baseline; Reflexion \\cite{reflexion-2023} extends this with verbal self-reflection; LATS \\cite{lats-2024} unifies reasoning, acting, and planning via tree search. SelfCheckGPT \\cite{selfcheckgpt-2023} identifies unreliable LLM outputs; our work shows that in interactive environments, such unreliability manifests as catastrophic agent death. We build on these environments and reasoning frameworks to isolate what routing signal they produce.\n\n\\paragraph{Safe RL.}\n\\citet{garcia2015comprehensive} survey safe RL methods; \\citet{crpo-2021} develop constrained optimization with formal convergence guarantees. These works design algorithms that satisfy safety constraints during training or deployment. Our contribution is complementary: rather than proposing a new safe policy, we provide a diagnostic that reveals modality routing functions primarily as a safety mechanism in environments with catastrophic failure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d727392a-e39d-428b-85d5-c889be325eed",
  "isSidechain": false,
  "requestId": "req_011Cb7yHHuimCE6ix7iA32Dd",
  "type": "assistant",
  "uuid": "9f68bbd0-c609-406c-8686-d085cb3ea62b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154wKx2gQFyFWFDPj8uiMKB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 332,
      "cache_read_input_tokens": 29352,
      "output_tokens": 721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 721,
          "cache_read_input_tokens": 29352,
          "cache_creation_input_tokens": 332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 332
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

_source line 26 · 2026-05-17T10:19:21.026Z_

<details><summary>↩ Tool result · `toolu_012DUFVSBLGxPoiwNYqxQYsJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f68bbd0-c609-406c-8686-d085cb3ea62b",
  "isSidechain": false,
  "promptId": "a57bc070-52fc-47b4-b3d4-773f9e41a3e0",
  "type": "user",
  "uuid": "11ce230b-99d9-48a1-9d6e-45420fb245b3",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex",
    "oldString": "\\paragraph{Safe RL and LLM Agents.}\n\\citet{garcia2015comprehensive} survey safe RL methods; \\citet{crpo-2021} develop constrained optimization with formal convergence guarantees. ScienceWorld \\cite{scienceworld-2022} serves as our primary testbed; ALFWorld \\cite{alfworld-2021} provides a complementary household environment; AgentBench \\cite{agentbench-2024} offers systematic evaluation across diverse environments. ReAct \\cite{react-2023} interleaves reasoning with actions and serves as our internal baseline; Reflexion \\cite{reflexion-2023} extends this with verbal self-reflection; LATS \\cite{lats-2024} unifies reasoning, acting, and planning via tree search. SelfCheckGPT \\cite{selfcheckgpt-2023} identifies unreliable LLM outputs; our work shows that in interactive environments, such unreliability manifests as catastrophic agent death. Our decomposition reveals that modality routing functions primarily as a safety mechanism.",
    "newString": "\\paragraph{LLM Agent Environments and Reasoning.}\nScienceWorld \\cite{scienceworld-2022} serves as our primary testbed; ALFWorld \\cite{alfworld-2021} provides a complementary household environment; AgentBench \\cite{agentbench-2024} offers systematic evaluation across diverse environments. ReAct \\cite{react-2023} interleaves reasoning with actions and serves as our internal baseline; Reflexion \\cite{reflexion-2023} extends this with verbal self-reflection; LATS \\cite{lats-2024} unifies reasoning, acting, and planning via tree search. SelfCheckGPT \\cite{selfcheckgpt-2023} identifies unreliable LLM outputs; our work shows that in interactive environments, such unreliability manifests as catastrophic agent death. We build on these environments and reasoning frameworks to isolate what routing signal they produce.\n\n\\paragraph{Safe RL.}\n\\citet{garcia2015comprehensive} survey safe RL methods; \\citet{crpo-2021} develop constrained optimization with formal convergence guarantees. These works design algorithms that satisfy safety constraints during training or deployment. Our contribution is complementary: rather than proposing a new safe policy, we provide a diagnostic that reveals modality routing functions primarily as a safety mechanism in environments with catastrophic failure.",
    "originalFile": "\\section{Related Work}\n\n\\paragraph{Tool Use and External Computation in LLMs.}\nA growing body of work augments language models with external tools \\citep{tool-learning-survey-2024}.\nToolformer \\cite{toolformer-2023} teaches LLMs to insert API calls via self-supervised loss filtering; ToolkenGPT \\cite{toolkengpt-2023} represents tools as special tokens; ART \\cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \\cite{chameleon-2023} composes heterogeneous modules per subtask; ReTool \\cite{retool-2025} applies RL to discover when code execution is preferable to chain-of-thought.\nThese focus on \\emph{learning to use tools}; we ask a prior question: \\emph{what signal drives the routing decision?}\nRecent concurrent work sharpens this question: \\citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect, \\citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \\citet{tool-use-tax-2026} quantify a ``tool-use tax,'' and \\citet{to-call-or-not-2026} propose a necessity--utility--affordability framework. Our decomposition provides environment-grounded evidence: in ScienceWorld, $90.4\\%$ of routing signal at $P{=}100$ traces to catastrophic-failure prevention.\n\n\\paragraph{Adaptive Computation and Routing.}\nCogRouter \\cite{cogrouter-2026} adapts reasoning depth per step, ARES \\cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \\cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \\cite{mtrouter-2026} addresses multi-turn routing.\nRouteLLM \\citep{routellm-2024} learns routers from preference data to select between strong and weak models.\nThese optimize \\emph{how} to route; we reveal \\emph{why} routing helps: in interactive environments, the dominant signal is catastrophic-failure avoidance.\n\n\\paragraph{Counterfactual Evaluation in RL.}\nPrior work generates counterfactual explanations for RL agents by perturbing individual actions within a fixed policy \\citep{olson2021counterfactual, gajcin2023counterfactual, amitai2024explaining}.\nOur approach differs in both purpose and granularity: we execute two complete episodes under different routing strategies, producing prospective paired comparisons that isolate routing signal \\emph{before} any router is trained.\n\n\\paragraph{Safe RL and LLM Agents.}\n\\citet{garcia2015comprehensive} survey safe RL methods; \\citet{crpo-2021} develop constrained optimization with formal convergence guarantees. ScienceWorld \\cite{scienceworld-2022} serves as our primary testbed; ALFWorld \\cite{alfworld-2021} provides a complementary household environment; AgentBench \\cite{agentbench-2024} offers systematic evaluation across diverse environments. ReAct \\cite{react-2023} interleaves reasoning with actions and serves as our internal baseline; Reflexion \\cite{reflexion-2023} extends this with verbal self-reflection; LATS \\cite{lats-2024} unifies reasoning, acting, and planning via tree search. SelfCheckGPT \\cite{selfcheckgpt-2023} identifies unreliable LLM outputs; our work shows that in interactive environments, such unreliability manifests as catastrophic agent death. Our decomposition reveals that modality routing functions primarily as a safety mechanism.\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 5,
        "newStart": 15,
        "newLines": 8,
        "lines": [
          " Prior work generates counterfactual explanations for RL agents by perturbing individual actions within a fixed policy \\citep{olson2021counterfactual, gajcin2023counterfactual, amitai2024explaining}.",
          " Our approach differs in both purpose and granularity: we execute two complete episodes under different routing strategies, producing prospective paired comparisons that isolate routing signal \\emph{before} any router is trained.",
          " ",
          "-\\paragraph{Safe RL and LLM Agents.}",
          "-\\citet{garcia2015comprehensive} survey safe RL methods; \\citet{crpo-2021} develop constrained optimization with formal convergence guarantees. ScienceWorld \\cite{scienceworld-2022} serves as our primary testbed; ALFWorld \\cite{alfworld-2021} provides a complementary household environment; AgentBench \\cite{agentbench-2024} offers systematic evaluation across diverse environments. ReAct \\cite{react-2023} interleaves reasoning with actions and serves as our internal baseline; Reflexion \\cite{reflexion-2023} extends this with verbal self-reflection; LATS \\cite{lats-2024} unifies reasoning, acting, and planning via tree search. SelfCheckGPT \\cite{selfcheckgpt-2023} identifies unreliable LLM outputs; our work shows that in interactive environments, such unreliability manifests as catastrophic agent death. Our decomposition reveals that modality routing functions primarily as a safety mechanism.",
          "+\\paragraph{LLM Agent Environments and Reasoning.}",
          "+ScienceWorld \\cite{scienceworld-2022} serves as our primary testbed; ALFWorld \\cite{alfworld-2021} provides a complementary household environment; AgentBench \\cite{agentbench-2024} offers systematic evaluation across diverse environments. ReAct \\cite{react-2023} interleaves reasoning with actions and serves as our internal baseline; Reflexion \\cite{reflexion-2023} extends this with verbal self-reflection; LATS \\cite{lats-2024} unifies reasoning, acting, and planning via tree search. SelfCheckGPT \\cite{selfcheckgpt-2023} identifies unreliable LLM outputs; our work shows that in interactive environments, such unreliability manifests as catastrophic agent death. We build on these environments and reasoning frameworks to isolate what routing signal they produce.",
          "+",
          "+\\paragraph{Safe RL.}",
          "+\\citet{garcia2015comprehensive} survey safe RL methods; \\citet{crpo-2021} develop constrained optimization with formal convergence guarantees. These works design algorithms that satisfy safety constraints during training or deployment. Our contribution is complementary: rather than proposing a new safe policy, we provide a diagnostic that reveals modality routing functions primarily as a safety mechanism in environments with catastrophic failure."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "9f68bbd0-c609-406c-8686-d085cb3ea62b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-17T10:19:24.518Z_

验证最终文件状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11ce230b-99d9-48a1-9d6e-45420fb245b3",
  "isSidechain": false,
  "requestId": "req_011Cb7yHzE8JyjbLLBwFR1u7",
  "type": "assistant",
  "uuid": "e6b8ec80-4ef1-471a-9672-edee455d3939",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZe5uux1Aq6bk5KH12HJTX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 778,
      "cache_read_input_tokens": 29684,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 29684,
          "cache_creation_input_tokens": 778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 778
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

_source line 28 · 2026-05-17T10:19:25.527Z_

<details open><summary>🔧 Tool call — Read · `toolu_019nsix3Z4L3qbgoPAteC2uB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex",
  "offset": 9,
  "limit": 16
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6b8ec80-4ef1-471a-9672-edee455d3939",
  "isSidechain": false,
  "requestId": "req_011Cb7yHzE8JyjbLLBwFR1u7",
  "type": "assistant",
  "uuid": "7e293467-adc1-453b-b37b-79c5d1a33bf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZe5uux1Aq6bk5KH12HJTX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 778,
      "cache_read_input_tokens": 29684,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 29684,
          "cache_creation_input_tokens": 778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 778
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

_source line 29 · 2026-05-17T10:19:25.534Z_

<details><summary>↩ Tool result · `toolu_019nsix3Z4L3qbgoPAteC2uB`</summary>

```text
9	The shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.
10	But this assumption has never been systematically verified: \emph{what actually drives the value of routing decisions in interactive environments?}
11	Understanding what concentrates routing signal has direct implications for agent deployment safety and routing strategy selection: if the value of routing traces to a single failure mode, practitioners can replace complex learned routers with simpler safety-aware policies, reducing both computational cost and deployment risk.
12	
13	We propose a \emph{formal diagnostic framework} for answering this question. The framework comprises (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), a metric that decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, the framework reveals a surprisingly concentrated answer: \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95, penalty-independent); under ScienceWorld's default penalty ($P{=}100$), this corresponds to DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$).
14	The internal strategy's hallucination-induced failures trigger catastrophic agent death (a $-100$ penalty), while the deterministic strategy survives the same episodes.
15	Once death episodes are removed, the performance gap between strategies collapses to $\Delta_{\text{nd}} = +2.84$.
16	
17	This framework addresses a methodological gap.
18	The standard approach to generating routing labels, per-step oracle comparison, degenerates under sparse rewards.
19	In ScienceWorld, non-zero reward arrives only at episode termination; 97.4\% of steps (across 11 prescreened task types) produce identical scores regardless of modality, leaving no step-level signal to learn from (\S\ref{sec:collection}).
20	Keyword-based heuristics also fail structurally, as ScienceWorld actions lack science-specific terminology (\S\ref{sec:baselines}).
21	Our counterfactual approach runs complete episodes under pure-internal (ReAct \cite{react-2023}) and pure-deterministic strategies, then compares episode outcomes to generate routing labels (\S\ref{sec:collection}). The framework is applicable to any environment with controllable modality comparison and binary catastrophic outcomes, requiring only paired episode outcomes under two modalities.
22	
23	Among the 11 prescreened task types (245 episode pairs), this death-avoidance dominance holds at the same magnitude reported above, both in the penalty-independent count and in DAF at $P{=}100$. The per-task $r = 0.97$ follows algebraically from death dominance when $P$ is constant (\S\ref{sec:death-decomp}).
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e293467-adc1-453b-b37b-79c5d1a33bf6",
  "isSidechain": false,
  "promptId": "a57bc070-52fc-47b4-b3d4-773f9e41a3e0",
  "type": "user",
  "uuid": "b5c2d677-87a2-4e2d-bf68-c0b522b5ea70",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex",
      "content": "The shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.\nBut this assumption has never been systematically verified: \\emph{what actually drives the value of routing decisions in interactive environments?}\nUnderstanding what concentrates routing signal has direct implications for agent deployment safety and routing strategy selection: if the value of routing traces to a single failure mode, practitioners can replace complex learned routers with simpler safety-aware policies, reducing both computational cost and deployment risk.\n\nWe propose a \\emph{formal diagnostic framework} for answering this question. The framework comprises (i)~episode-level counterfactual labeling under pure strategies (\\S\\ref{sec:collection}--\\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), a metric that decomposes the routing score gap into death-avoidance and non-death components (\\S\\ref{sec:daf}). Applied to ScienceWorld, the framework reveals a surprisingly concentrated answer: \\textbf{78.9\\% of non-tie routing labels arise from death asymmetry} (75 of 95, penalty-independent); under ScienceWorld's default penalty ($P{=}100$), this corresponds to DAF $= 90.4\\%$ (95\\% CI: $[81.6\\%, 98.8\\%]$).\nThe internal strategy's hallucination-induced failures trigger catastrophic agent death (a $-100$ penalty), while the deterministic strategy survives the same episodes.\nOnce death episodes are removed, the performance gap between strategies collapses to $\\Delta_{\\text{nd}} = +2.84$.\n\nThis framework addresses a methodological gap.\nThe standard approach to generating routing labels, per-step oracle comparison, degenerates under sparse rewards.\nIn ScienceWorld, non-zero reward arrives only at episode termination; 97.4\\% of steps (across 11 prescreened task types) produce identical scores regardless of modality, leaving no step-level signal to learn from (\\S\\ref{sec:collection}).\nKeyword-based heuristics also fail structurally, as ScienceWorld actions lack science-specific terminology (\\S\\ref{sec:baselines}).\nOur counterfactual approach runs complete episodes under pure-internal (ReAct \\cite{react-2023}) and pure-deterministic strategies, then compares episode outcomes to generate routing labels (\\S\\ref{sec:collection}). The framework is applicable to any environment with controllable modality comparison and binary catastrophic outcomes, requiring only paired episode outcomes under two modalities.\n\nAmong the 11 prescreened task types (245 episode pairs), this death-avoidance dominance holds at the same magnitude reported above, both in the penalty-independent count and in DAF at $P{=}100$. The per-task $r = 0.97$ follows algebraically from death dominance when $P$ is constant (\\S\\ref{sec:death-decomp}).\n",
      "numLines": 16,
      "startLine": 9,
      "totalLines": 41
    }
  },
  "sourceToolAssistantUUID": "7e293467-adc1-453b-b37b-79c5d1a33bf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T10:19:26.326Z_

<details><summary>↩ Tool result · `toolu_01WjyL28Qj9rh2aNAZ1kcCyU`</summary>

```text
17	
18	\paragraph{LLM Agent Environments and Reasoning.}
19	ScienceWorld \cite{scienceworld-2022} serves as our primary testbed; ALFWorld \cite{alfworld-2021} provides a complementary household environment; AgentBench \cite{agentbench-2024} offers systematic evaluation across diverse environments. ReAct \cite{react-2023} interleaves reasoning with actions and serves as our internal baseline; Reflexion \cite{reflexion-2023} extends this with verbal self-reflection; LATS \cite{lats-2024} unifies reasoning, acting, and planning via tree search. SelfCheckGPT \cite{selfcheckgpt-2023} identifies unreliable LLM outputs; our work shows that in interactive environments, such unreliability manifests as catastrophic agent death. We build on these environments and reasoning frameworks to isolate what routing signal they produce.
20	
21	\paragraph{Safe RL.}
22	\citet{garcia2015comprehensive} survey safe RL methods; \citet{crpo-2021} develop constrained optimization with formal convergence guarantees. These works design algorithms that satisfy safety constraints during training or deployment. Our contribution is complementary: rather than proposing a new safe policy, we provide a diagnostic that reveals modality routing functions primarily as a safety mechanism in environments with catastrophic failure.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bbb84c5-0fa9-4514-87b7-2275cb3e8401",
  "isSidechain": false,
  "promptId": "a57bc070-52fc-47b4-b3d4-773f9e41a3e0",
  "type": "user",
  "uuid": "47fd541e-749f-44df-8362-992f13625dde",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex",
      "content": "\n\\paragraph{LLM Agent Environments and Reasoning.}\nScienceWorld \\cite{scienceworld-2022} serves as our primary testbed; ALFWorld \\cite{alfworld-2021} provides a complementary household environment; AgentBench \\cite{agentbench-2024} offers systematic evaluation across diverse environments. ReAct \\cite{react-2023} interleaves reasoning with actions and serves as our internal baseline; Reflexion \\cite{reflexion-2023} extends this with verbal self-reflection; LATS \\cite{lats-2024} unifies reasoning, acting, and planning via tree search. SelfCheckGPT \\cite{selfcheckgpt-2023} identifies unreliable LLM outputs; our work shows that in interactive environments, such unreliability manifests as catastrophic agent death. We build on these environments and reasoning frameworks to isolate what routing signal they produce.\n\n\\paragraph{Safe RL.}\n\\citet{garcia2015comprehensive} survey safe RL methods; \\citet{crpo-2021} develop constrained optimization with formal convergence guarantees. These works design algorithms that satisfy safety constraints during training or deployment. Our contribution is complementary: rather than proposing a new safe policy, we provide a diagnostic that reveals modality routing functions primarily as a safety mechanism in environments with catastrophic failure.\n",
      "numLines": 7,
      "startLine": 17,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "6bbb84c5-0fa9-4514-87b7-2275cb3e8401",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T10:19:26.321Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WjyL28Qj9rh2aNAZ1kcCyU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex",
  "offset": 17,
  "limit": 12
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5c2d677-87a2-4e2d-bf68-c0b522b5ea70",
  "isSidechain": false,
  "requestId": "req_011Cb7yHzE8JyjbLLBwFR1u7",
  "type": "assistant",
  "uuid": "6bbb84c5-0fa9-4514-87b7-2275cb3e8401",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZe5uux1Aq6bk5KH12HJTX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 778,
      "cache_read_input_tokens": 29684,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 29684,
          "cache_creation_input_tokens": 778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 778
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

_source line 32 · 2026-05-17T10:19:26.379Z_

```json
{
  "parentUuid": "47fd541e-749f-44df-8362-992f13625dde",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "472d3333-0c8a-4984-a7d1-72cff96f23e3",
  "timestamp": "2026-05-17T10:19:26.379Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-17T10:19:35.549Z_

三处修改完成。Diff 摘要：

| # | 位置 | 原文 | 改后 |
|---|------|------|------|
| 1 | `introduction.tex` line 23 | `78.9\% of non-tie routing labels arise from death asymmetry (penalty-independent); DAF $= 90.4\%$ at $P{=}100$.` | `this death-avoidance dominance holds at the same magnitude reported above, both in the penalty-independent count and in DAF at $P{=}100$.` |
| 2 | `introduction.tex` line 11 (新增) | (无) | 一句话说明 routing signal 集中性对 agent 部署安全和策略选择的实际意义 |
| 3 | `related_work.tex` lines 18-22 | 单段 `\paragraph{Safe RL and LLM Agents.}` | 拆为 `\paragraph{LLM Agent Environments and Reasoning.}`（环境+推理方法，定位句指向 routing signal 诊断）和 `\paragraph{Safe RL.}`（安全约束方法，定位句说明本文提供诊断而非新 safe policy） |

所有数值、Contribution 列表、claim 强度均未改动；无破折号、无 -ing 结尾、无黑名单词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "472d3333-0c8a-4984-a7d1-72cff96f23e3",
  "isSidechain": false,
  "requestId": "req_011Cb7yJNzLyKfmG2rDpagUp",
  "type": "assistant",
  "uuid": "c2258a0d-4529-41a1-a419-6870f9f1e09e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kt251xiM18mXJ3S9WQfi6u",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 30462,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1455,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 30462,
          "cache_creation_input_tokens": 1455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1455
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

_source line 34_

```json
{
  "type": "last-prompt",
  "leafUuid": "c2258a0d-4529-41a1-a419-6870f9f1e09e",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Optimize paper structure in Introduction and Related Work",
  "sessionId": "1b6d4d6b-1d9c-49fa-b51d-68bdda96025d"
}
```

---
