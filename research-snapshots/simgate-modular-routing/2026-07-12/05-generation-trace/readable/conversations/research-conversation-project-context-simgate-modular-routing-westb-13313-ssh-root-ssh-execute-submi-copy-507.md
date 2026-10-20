# Research conversation: <project_context> # 项目: simgate-modular-routing ## 运行环境 - 服务器名: westb-13313 - SSH 账户: root（调用 ssh_execute / submit_train

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/2e772352-b537-4f05-916f-93da1b428592.jsonl`
- **Structured JSON:** [`1e29cf3a38f94b5e78ef.json`](../../sessions/1e/1e29cf3a38f94b5e78ef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T10:14:25.176Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T10:14:25.176Z",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
  "content": "&lt;project_context>\n# 项目: simgate-modular-routing\n\n## 运行环境\n- 服务器名: westb-13313\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westb.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/simgate-modular-routing\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：扩写 Related Work (§2)\n\n### 背景\n论文从 short paper (4p) 升级为 long paper (8p)。Related Work 需要从目前的 ~0.5 page 扩展到 ~1 page，成为独立 section。\n\n### 当前内容\n读取：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex`\n\n### 扩写要求\n\n论文主题是：\"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"。核心贡献是 counterfactual 分析方法论 + death avoidance empirical finding。\n\n需要覆盖以下 subsections/paragraphs（每个 1-2 段）：\n\n#### 1. Tool Use and External Computation in LLMs\n- ReAct, Toolformer, ART, Chameleon — 已有引用，可适当展开\n- ToolkenGPT — 已有引用\n- 新增近期工作（引用已在 bib 中）：\n  - tool-overuse-illusion-2026: Tool-Overuse Illusion\n  - when2tool-2026: LLMs Already Know When to Call Tools\n  - tool-use-tax-2026: Tool-Use Tax\n  - to-call-or-not-2026: To Call or Not to Call\n\n#### 2. Adaptive Computation and Routing\n- CogRouter, ARES, Mixture-of-Recursions, MTRouter — 已有引用\n- ReTool — 已有引用\n- 定位我们的工作：不是设计更好的 router，而是分析 routing signal 本身\n\n#### 3. Counterfactual Evaluation in RL\n- 已有段落但较短，展开\n- amitai2024, gajcin2023, olson2021 — 已有引用\n- 强调我们的 episode-level 方法与 step-level 的区别\n\n#### 4. Safe RL and Catastrophic Failure\n- garcia2015comprehensive — 已有引用\n- 联系 death avoidance 与 safe RL 文献\n- 可提及 reward shaping 中的 penalty 设计\n\n#### 5. LLM Agents in Interactive Environments\n- ScienceWorld (scienceworld-2022), Voyager (voyager-2023), ALFWorld (alfworld-2021) — 已有引用\n- ITP (itp-2026), Dyna-Think (dynathink-2025) — 已有引用\n\n### 写作规范\n- 每个 subsection 用 \\paragraph{} 分隔\n- 引用必须使用 references.bib 中已有的 entries（不要发明新引用）\n- 定位清晰：与每组工作的 contrast/connection\n- Long paper 的 Related Work 预期 0.8-1.2 pages\n- 不要重复 Introduction 的内容\n\n### 参考文件\n- bib 文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib`\n- 当前 related work：同目录下 `related_work.tex`\n\n### 文件路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/`"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T10:14:25.180Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T10:14:25.180Z",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-15T10:14:25.216Z_

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
## 任务：扩写 Related Work (§2)

### 背景
论文从 short paper (4p) 升级为 long paper (8p)。Related Work 需要从目前的 ~0.5 page 扩展到 ~1 page，成为独立 section。

### 当前内容
读取：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex`

### 扩写要求

论文主题是："Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"。核心贡献是 counterfactual 分析方法论 + death avoidance empirical finding。

需要覆盖以下 subsections/paragraphs（每个 1-2 段）：

#### 1. Tool Use and External Computation in LLMs
- ReAct, Toolformer, ART, Chameleon — 已有引用，可适当展开
- ToolkenGPT — 已有引用
- 新增近期工作（引用已在 bib 中）：
  - tool-overuse-illusion-2026: Tool-Overuse Illusion
  - when2tool-2026: LLMs Already Know When to Call Tools
  - tool-use-tax-2026: Tool-Use Tax
  - to-call-or-not-2026: To Call or Not to Call

#### 2. Adaptive Computation and Routing
- CogRouter, ARES, Mixture-of-Recursions, MTRouter — 已有引用
- ReTool — 已有引用
- 定位我们的工作：不是设计更好的 router，而是分析 routing signal 本身

#### 3. Counterfactual Evaluation in RL
- 已有段落但较短，展开
- amitai2024, gajcin2023, olson2021 — 已有引用
- 强调我们的 episode-level 方法与 step-level 的区别

#### 4. Safe RL and Catastrophic Failure
- garcia2015comprehensive — 已有引用
- 联系 death avoidance 与 safe RL 文献
- 可提及 reward shaping 中的 penalty 设计

#### 5. LLM Agents in Interactive Environments
- ScienceWorld (scienceworld-2022), Voyager (voyager-2023), ALFWorld (alfworld-2021) — 已有引用
- ITP (itp-2026), Dyna-Think (dynathink-2025) — 已有引用

### 写作规范
- 每个 subsection 用 \paragraph{} 分隔
- 引用必须使用 references.bib 中已有的 entries（不要发明新引用）
- 定位清晰：与每组工作的 contrast/connection
- Long paper 的 Related Work 预期 0.8-1.2 pages
- 不要重复 Introduction 的内容

### 参考文件
- bib 文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib`
- 当前 related work：同目录下 `related_work.tex`

### 文件路径
`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ca07304c-4ca6-4192-a3b8-c383b7da71fe",
  "type": "user",
  "uuid": "0be5374e-1c59-4745-8c93-409c71d673a1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T10:14:25.215Z_

```json
{
  "parentUuid": "0be5374e-1c59-4745-8c93-409c71d673a1",
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
  "uuid": "8d436491-1820-42ec-8557-6e554a462589",
  "timestamp": "2026-05-15T10:14:25.215Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T10:14:25.215Z_

```json
{
  "parentUuid": "8d436491-1820-42ec-8557-6e554a462589",
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
  "uuid": "7b4aa689-4ce4-41b1-954b-173ba4427be3",
  "timestamp": "2026-05-15T10:14:25.215Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T10:14:25.215Z_

```json
{
  "parentUuid": "7b4aa689-4ce4-41b1-954b-173ba4427be3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e2074327-93ab-4ebc-8a8e-0ebfe699ade2",
  "timestamp": "2026-05-15T10:14:25.215Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
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
  "aiTitle": "Expand related work section for long paper",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592"
}
```

---

### Assistant

_source line 8 · 2026-05-15T10:14:29.398Z_

Let me read the current related work and bib file first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2074327-93ab-4ebc-8a8e-0ebfe699ade2",
  "isSidechain": false,
  "requestId": "req_011Cb4BJMGYD2npJWyfeJnga",
  "type": "assistant",
  "uuid": "d9890a88-998b-4eaf-8ba1-09e8f5bb2b51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hht5QYFDShBemzS29Dg4ak",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11678,
      "cache_read_input_tokens": 11841,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 179,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11678
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

_source line 9 · 2026-05-15T10:14:29.880Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ExuetmWx4sEiLgHFZR3F4K`</summary>

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
  "parentUuid": "d9890a88-998b-4eaf-8ba1-09e8f5bb2b51",
  "isSidechain": false,
  "requestId": "req_011Cb4BJMGYD2npJWyfeJnga",
  "type": "assistant",
  "uuid": "01324b52-e432-4c7c-a744-880ccfb2b326",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hht5QYFDShBemzS29Dg4ak",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11678,
      "cache_read_input_tokens": 11841,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 179,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11678
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

_source line 10 · 2026-05-15T10:14:29.891Z_

<details><summary>↩ Tool result · `toolu_01ExuetmWx4sEiLgHFZR3F4K`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Tool-Use Learning.}
4	Toolformer \cite{toolformer-2024}, ToolkenGPT \cite{toolkengpt-2023}, ART \cite{art-2023}, Chameleon \cite{chameleon-2024}, and ReTool \cite{retool-2026} learn tool-use policies via self-supervised, embedding-based, or RL approaches.
5	We generate labels via \emph{episode-level counterfactual analysis}, framing routing as \emph{catastrophic failure prevention}.
6	
7	\paragraph{Adaptive Computation.}
8	CogRouter \cite{cogrouter-2026}, ARES \cite{ares-2026}, and Mixture-of-Recursions \cite{mixture-of-recursions-2025} route \emph{how much} computation; MTRouter \cite{mtrouter-2026} routes \emph{which model}. We route \emph{which modality} and find death avoidance accounts for ${\sim}90\%$ of routing signal at $P{=}100$.
9	
10	\paragraph{World Model Routing.}
11	ITP \cite{itp-2026} and Dyna-Think \cite{dynathink-2025} route to approximate world models that inherit hallucination failures; our deterministic modality provides exact transitions, mattering almost exclusively for death avoidance.
12	
13	\paragraph{Agent Frameworks.}
14	ReAct \cite{react-2023} serves as our internal-reasoning baseline; ALFWorld \cite{alfworld-2021} provides a complementary text-based benchmark. We analyze \emph{when} reasoning should yield to deterministic computation, connecting to safe RL \citep{garcia2015comprehensive}.
15	
16	\paragraph{Counterfactual Evaluation in RL.}
17	Counterfactual reasoning has been applied to explain RL agent behavior post-hoc---comparing observed actions against hypothetical alternatives \cite{olson2021counterfactual,gajcin2023counterfactual,amitai2024explaining}. Our approach differs fundamentally: rather than explaining a fixed policy, we execute two complete episodes under different routing strategies, producing prospective paired comparisons that isolate the routing signal before any router is trained.
18	
19	\paragraph{Concurrent Work.}
20	Concurrent studies examine complementary aspects: cognitive illusions driving tool overuse \cite{tool-overuse-illusion-2026}, hidden-state encoding of tool-call decisions \cite{when2tool-2026}, a ``tool-use tax'' where tools are not always beneficial \cite{tool-use-tax-2026}, and necessity/utility/affordability evaluation \cite{to-call-or-not-2026}. Our death avoidance decomposition provides concrete quantification---${\sim}90\%$ of routing signal at $P{=}100$ stems from catastrophic-failure prevention---grounding these frameworks in interactive-environment evidence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01324b52-e432-4c7c-a744-880ccfb2b326",
  "isSidechain": false,
  "promptId": "ca07304c-4ca6-4192-a3b8-c383b7da71fe",
  "type": "user",
  "uuid": "54d79b54-3c5e-4b94-b973-4357160120b9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\n\\paragraph{Tool-Use Learning.}\nToolformer \\cite{toolformer-2024}, ToolkenGPT \\cite{toolkengpt-2023}, ART \\cite{art-2023}, Chameleon \\cite{chameleon-2024}, and ReTool \\cite{retool-2026} learn tool-use policies via self-supervised, embedding-based, or RL approaches.\nWe generate labels via \\emph{episode-level counterfactual analysis}, framing routing as \\emph{catastrophic failure prevention}.\n\n\\paragraph{Adaptive Computation.}\nCogRouter \\cite{cogrouter-2026}, ARES \\cite{ares-2026}, and Mixture-of-Recursions \\cite{mixture-of-recursions-2025} route \\emph{how much} computation; MTRouter \\cite{mtrouter-2026} routes \\emph{which model}. We route \\emph{which modality} and find death avoidance accounts for ${\\sim}90\\%$ of routing signal at $P{=}100$.\n\n\\paragraph{World Model Routing.}\nITP \\cite{itp-2026} and Dyna-Think \\cite{dynathink-2025} route to approximate world models that inherit hallucination failures; our deterministic modality provides exact transitions, mattering almost exclusively for death avoidance.\n\n\\paragraph{Agent Frameworks.}\nReAct \\cite{react-2023} serves as our internal-reasoning baseline; ALFWorld \\cite{alfworld-2021} provides a complementary text-based benchmark. We analyze \\emph{when} reasoning should yield to deterministic computation, connecting to safe RL \\citep{garcia2015comprehensive}.\n\n\\paragraph{Counterfactual Evaluation in RL.}\nCounterfactual reasoning has been applied to explain RL agent behavior post-hoc---comparing observed actions against hypothetical alternatives \\cite{olson2021counterfactual,gajcin2023counterfactual,amitai2024explaining}. Our approach differs fundamentally: rather than explaining a fixed policy, we execute two complete episodes under different routing strategies, producing prospective paired comparisons that isolate the routing signal before any router is trained.\n\n\\paragraph{Concurrent Work.}\nConcurrent studies examine complementary aspects: cognitive illusions driving tool overuse \\cite{tool-overuse-illusion-2026}, hidden-state encoding of tool-call decisions \\cite{when2tool-2026}, a ``tool-use tax'' where tools are not always beneficial \\cite{tool-use-tax-2026}, and necessity/utility/affordability evaluation \\cite{to-call-or-not-2026}. Our death avoidance decomposition provides concrete quantification---${\\sim}90\\%$ of routing signal at $P{=}100$ stems from catastrophic-failure prevention---grounding these frameworks in interactive-environment evidence.",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "01324b52-e432-4c7c-a744-880ccfb2b326",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T10:14:33.516Z_

<details><summary>↩ Tool result · `toolu_01X5sK6XjLx8ciPZW68Z2H64`</summary>

```text
1	@inproceedings{scienceworld-2022,
2	  title={ScienceWorld: Is Your Agent Smarter Than a 5th Grader?},
3	  author={Wang, Ruoyao and Jansen, Peter and C\^{o}t\'{e}, Marc-Alexandre and Ammanabrolu, Prithviraj},
4	  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
5	  year={2022}
6	}
7	
8	@inproceedings{react-2023,
9	  title={ReAct: Synergizing Reasoning and Acting in Language Models},
10	  author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
11	  booktitle={International Conference on Learning Representations (ICLR)},
12	  year={2023}
13	}
14	
15	@inproceedings{toolformer-2024,
16	  title={Toolformer: Language Models Can Teach Themselves to Use Tools},
17	  author={Schick, Timo and Dwivedi-Yu, Jane and Dess\`{i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
18	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
19	  year={2023}
20	}
21	
22	@article{art-2023,
23	  title={ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models},
24	  author={Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Ribeiro, Marco Tulio},
25	  journal={arXiv preprint arXiv:2303.09014},
26	  year={2023}
27	}
28	
29	@inproceedings{chameleon-2024,
30	  title={Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models},
31	  author={Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Gao, Jianfeng},
32	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
33	  year={2023}
34	}
35	
36	@article{retool-2026,
37	  title={ReTool: Reinforcement Learning for Strategic Tool Use in LLMs},
38	  author={Feng, Jiazhan and others},
39	  journal={arXiv preprint arXiv:2504.11536},
40	  year={2025}
41	}
42	
43	@article{cogrouter-2026,
44	  title={Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents},
45	  author={Yang, Ruihan and others},
46	  journal={arXiv preprint arXiv:2602.12662},
47	  year={2026}
48	}
49	
50	@article{ares-2026,
51	  title={ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents},
52	  author={Yang, Jingbo and others},
53	  journal={arXiv preprint arXiv:2603.07915},
54	  year={2026}
55	}
56	
57	@inproceedings{mixture-of-recursions-2025,
58	  title={Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation},
59	  author={Bae, Sangmin and others},
60	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
61	  year={2025}
62	}
63	
64	@inproceedings{mtrouter-2026,
65	  title={MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings},
66	  author={Zhang, Yiqun and others},
67	  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL)},
68	  year={2026}
69	}
70	
71	@article{itp-2026,
72	  title={Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models},
73	  author={Liu, Youwei and others},
74	  journal={arXiv preprint arXiv:2601.08955},
75	  year={2026}
76	}
77	
78	@article{dynathink-2025,
79	  title={Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents},
80	  author={Yu, Xiao and others},
81	  journal={arXiv preprint arXiv:2506.00320},
82	  year={2025}
83	}
84	
85	@article{tool-overuse-illusion-2026,
86	  title={The Tool-Overuse Illusion: Why Does {LLM} Prefer External Tools over Internal Knowledge?},
87	  author={Zeng, Yirong and You, Shen and Liu, Yufei and Du, Qunyao and Ding, Xiao and Hou, Yutai and Wang, Yuxian and Ning, Wu and Song, Haonan and Tu, Dandan and Cai, Bibo and Liu, Ting},
88	  journal={arXiv preprint arXiv:2604.19749},
89	  year={2026}
90	}
91	
92	@article{when2tool-2026,
93	  title={{LLM} Agents Already Know When to Call Tools -- Even Without Reasoning},
94	  author={Sun, Chung-En and Liu, Linbo and Yan, Ge and Wang, Zimo and Weng, Tsui-Wei},
95	  journal={arXiv preprint arXiv:2605.09252},
96	  year={2026}
97	}
98	
99	@article{tool-use-tax-2026,
100	  title={Are Tools All We Need? Unveiling the Tool-Use Tax in {LLM} Agents},
101	  author={Zhang, Kaituo and Xiong, Zhen and Zhong, Mingyu and Jiang, Zhimeng and Yuan, Zhouyuan and Li, Zhecheng and Lin, Ying},
102	  journal={arXiv preprint arXiv:2605.00136},
103	  year={2026}
104	}
105	
106	@article{to-call-or-not-2026,
107	  title={To Call or Not to Call: A Framework to Assess and Optimize {LLM} Tool Calling},
108	  author={Wu, Qinyuan and Das, Soumi and Amani, Mahsa and Nag, Arijit and Lee, Seungeon and Gummadi, Krishna P. and Ravichander, Abhilasha and Zafar, Muhammad Bilal},
109	  journal={arXiv preprint arXiv:2605.00737},
110	  year={2026}
111	}
112	
113	@inproceedings{dagger-2011,
114	  title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},
115	  author={Ross, St\'{e}phane and Gordon, Geoffrey J and Bagnell, Drew},
116	  booktitle={Proceedings of the International Conference on Artificial Intelligence and Statistics (AISTATS)},
117	  year={2011}
118	}
119	
120	@inproceedings{toolkengpt-2023,
121	  title={ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings},
122	  author={Hao, Shibo and Liu, Tianyang and Wang, Zhen and Hu, Zhiting},
123	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
124	  year={2023}
125	}
126	
127	@inproceedings{alfworld-2021,
128	  title={ALFWorld: Aligning Text and Embodied Environments for Interactive Learning},
129	  author={Shridhar, Mohit and Yuan, Xingdi and C\^{o}t\'{e}, Marc-Alexandre and Bisk, Yonatan and Trischler, Adam and Hausknecht, Matthew},
130	  booktitle={International Conference on Learning Representations (ICLR)},
131	  year={2021}
132	}
133	
134	@article{garcia2015comprehensive,
135	  title={A Comprehensive Survey on Safe Reinforcement Learning},
136	  author={Garc\'{i}a, Javier and Fern\'{a}ndez, Fernando},
137	  journal={Journal of Machine Learning Research},
138	  volume={16},
139	  number={1},
140	  pages={1437--1480},
141	  year={2015}
142	}
143	
144	@article{voyager-2023,
145	  title={Voyager: An Open-Ended Embodied Agent with Large Language Models},
146	  author={Wang, Guanzhi and Xie, Yuqi and Jiang, Yunfan and Mandlekar, Ajay and Xiao, Chaowei and Zhu, Yuke and Fan, Linxi and Anandkumar, Anima},
147	  journal={arXiv preprint arXiv:2305.16291},
148	  year={2023}
149	}
150	
151	@inproceedings{amitai2024explaining,
152	  title={Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes},
153	  author={Amitai, Yotam and Septon, Guy and Amir, Ofra},
154	  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
155	  year={2024}
156	}
157	
158	@inproceedings{gajcin2023counterfactual,
159	  title={Counterfactual Explanations for Reinforcement Learning Agents},
160	  author={Gajcin, Jasmina},
161	  booktitle={Proceedings of the International Conference on Autonomous Agents and Multiagent Systems (AAMAS)},
162	  year={2023}
163	}
164	
165	@article{olson2021counterfactual,
166	  title={Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning},
167	  author={Olson, Matthew L. and Khanna, Roli and Neal, Lawrence and Li, Fuxin and Wong, Weng-Keen},
168	  journal={Artificial Intelligence},
169	  volume={295},
170	  pages={103455},
171	  year={2021}
172	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e78ef975-2bcd-4833-ab5e-ffa8b85ca21f",
  "isSidechain": false,
  "promptId": "ca07304c-4ca6-4192-a3b8-c383b7da71fe",
  "type": "user",
  "uuid": "250211b1-0d14-46cc-bc3f-57729b82ec4c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib",
      "content": "@inproceedings{scienceworld-2022,\n  title={ScienceWorld: Is Your Agent Smarter Than a 5th Grader?},\n  author={Wang, Ruoyao and Jansen, Peter and C\\^{o}t\\'{e}, Marc-Alexandre and Ammanabrolu, Prithviraj},\n  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2022}\n}\n\n@inproceedings{react-2023,\n  title={ReAct: Synergizing Reasoning and Acting in Language Models},\n  author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n@inproceedings{toolformer-2024,\n  title={Toolformer: Language Models Can Teach Themselves to Use Tools},\n  author={Schick, Timo and Dwivedi-Yu, Jane and Dess\\`{i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@article{art-2023,\n  title={ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models},\n  author={Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Ribeiro, Marco Tulio},\n  journal={arXiv preprint arXiv:2303.09014},\n  year={2023}\n}\n\n@inproceedings{chameleon-2024,\n  title={Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models},\n  author={Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Gao, Jianfeng},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@article{retool-2026,\n  title={ReTool: Reinforcement Learning for Strategic Tool Use in LLMs},\n  author={Feng, Jiazhan and others},\n  journal={arXiv preprint arXiv:2504.11536},\n  year={2025}\n}\n\n@article{cogrouter-2026,\n  title={Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents},\n  author={Yang, Ruihan and others},\n  journal={arXiv preprint arXiv:2602.12662},\n  year={2026}\n}\n\n@article{ares-2026,\n  title={ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents},\n  author={Yang, Jingbo and others},\n  journal={arXiv preprint arXiv:2603.07915},\n  year={2026}\n}\n\n@inproceedings{mixture-of-recursions-2025,\n  title={Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation},\n  author={Bae, Sangmin and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@inproceedings{mtrouter-2026,\n  title={MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings},\n  author={Zhang, Yiqun and others},\n  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2026}\n}\n\n@article{itp-2026,\n  title={Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models},\n  author={Liu, Youwei and others},\n  journal={arXiv preprint arXiv:2601.08955},\n  year={2026}\n}\n\n@article{dynathink-2025,\n  title={Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents},\n  author={Yu, Xiao and others},\n  journal={arXiv preprint arXiv:2506.00320},\n  year={2025}\n}\n\n@article{tool-overuse-illusion-2026,\n  title={The Tool-Overuse Illusion: Why Does {LLM} Prefer External Tools over Internal Knowledge?},\n  author={Zeng, Yirong and You, Shen and Liu, Yufei and Du, Qunyao and Ding, Xiao and Hou, Yutai and Wang, Yuxian and Ning, Wu and Song, Haonan and Tu, Dandan and Cai, Bibo and Liu, Ting},\n  journal={arXiv preprint arXiv:2604.19749},\n  year={2026}\n}\n\n@article{when2tool-2026,\n  title={{LLM} Agents Already Know When to Call Tools -- Even Without Reasoning},\n  author={Sun, Chung-En and Liu, Linbo and Yan, Ge and Wang, Zimo and Weng, Tsui-Wei},\n  journal={arXiv preprint arXiv:2605.09252},\n  year={2026}\n}\n\n@article{tool-use-tax-2026,\n  title={Are Tools All We Need? Unveiling the Tool-Use Tax in {LLM} Agents},\n  author={Zhang, Kaituo and Xiong, Zhen and Zhong, Mingyu and Jiang, Zhimeng and Yuan, Zhouyuan and Li, Zhecheng and Lin, Ying},\n  journal={arXiv preprint arXiv:2605.00136},\n  year={2026}\n}\n\n@article{to-call-or-not-2026,\n  title={To Call or Not to Call: A Framework to Assess and Optimize {LLM} Tool Calling},\n  author={Wu, Qinyuan and Das, Soumi and Amani, Mahsa and Nag, Arijit and Lee, Seungeon and Gummadi, Krishna P. and Ravichander, Abhilasha and Zafar, Muhammad Bilal},\n  journal={arXiv preprint arXiv:2605.00737},\n  year={2026}\n}\n\n@inproceedings{dagger-2011,\n  title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},\n  author={Ross, St\\'{e}phane and Gordon, Geoffrey J and Bagnell, Drew},\n  booktitle={Proceedings of the International Conference on Artificial Intelligence and Statistics (AISTATS)},\n  year={2011}\n}\n\n@inproceedings{toolkengpt-2023,\n  title={ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings},\n  author={Hao, Shibo and Liu, Tianyang and Wang, Zhen and Hu, Zhiting},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{alfworld-2021,\n  title={ALFWorld: Aligning Text and Embodied Environments for Interactive Learning},\n  author={Shridhar, Mohit and Yuan, Xingdi and C\\^{o}t\\'{e}, Marc-Alexandre and Bisk, Yonatan and Trischler, Adam and Hausknecht, Matthew},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@article{garcia2015comprehensive,\n  title={A Comprehensive Survey on Safe Reinforcement Learning},\n  author={Garc\\'{i}a, Javier and Fern\\'{a}ndez, Fernando},\n  journal={Journal of Machine Learning Research},\n  volume={16},\n  number={1},\n  pages={1437--1480},\n  year={2015}\n}\n\n@article{voyager-2023,\n  title={Voyager: An Open-Ended Embodied Agent with Large Language Models},\n  author={Wang, Guanzhi and Xie, Yuqi and Jiang, Yunfan and Mandlekar, Ajay and Xiao, Chaowei and Zhu, Yuke and Fan, Linxi and Anandkumar, Anima},\n  journal={arXiv preprint arXiv:2305.16291},\n  year={2023}\n}\n\n@inproceedings{amitai2024explaining,\n  title={Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes},\n  author={Amitai, Yotam and Septon, Guy and Amir, Ofra},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},\n  year={2024}\n}\n\n@inproceedings{gajcin2023counterfactual,\n  title={Counterfactual Explanations for Reinforcement Learning Agents},\n  author={Gajcin, Jasmina},\n  booktitle={Proceedings of the International Conference on Autonomous Agents and Multiagent Systems (AAMAS)},\n  year={2023}\n}\n\n@article{olson2021counterfactual,\n  title={Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning},\n  author={Olson, Matthew L. and Khanna, Roli and Neal, Lawrence and Li, Fuxin and Wong, Weng-Keen},\n  journal={Artificial Intelligence},\n  volume={295},\n  pages={103455},\n  year={2021}\n}",
      "numLines": 172,
      "startLine": 1,
      "totalLines": 172
    }
  },
  "sourceToolAssistantUUID": "e78ef975-2bcd-4833-ab5e-ffa8b85ca21f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T10:14:33.510Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X5sK6XjLx8ciPZW68Z2H64`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54d79b54-3c5e-4b94-b973-4357160120b9",
  "isSidechain": false,
  "requestId": "req_011Cb4BJMGYD2npJWyfeJnga",
  "type": "assistant",
  "uuid": "e78ef975-2bcd-4833-ab5e-ffa8b85ca21f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hht5QYFDShBemzS29Dg4ak",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11678,
      "cache_read_input_tokens": 11841,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 179,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11678
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
  "leafUuid": "250211b1-0d14-46cc-bc3f-57729b82ec4c",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Expand related work section for long paper",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592"
}
```

---

### Assistant

_source line 15 · 2026-05-15T10:14:44.936Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both files. Let me write the expanded related work section. I need to:

1. Tool Use and External Computation in LLMs - expand with ReAct, Toolformer, ART, Chameleon, ToolkenGPT, and the new concurrent works
2. Adaptive Computation and Routing - expand with CogRouter, ARES, MoR, MTRouter, ReTool
3. Counterfactual Evaluation in RL - expand existing paragraph
4. Safe RL and Catastrophic Failure - new, using garcia2015comprehensive


5. LLM Agents in Interactive Environments - expand with ScienceWorld, Voyager, ALFWorld, ITP, Dyna-Think

I'm checking the available bibliography keys to make sure I have everything I need for these sections.

Now I'm reviewing the additional citations I can use - there are several more papers on tool use, counterfactual reasoning, and the specific environments I want to cover. I need to structure the related work carefully to avoid repeating what's already in the introduction, keep it to about a page, and organize it into five clear subsections that position my work against different research groups.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "250211b1-0d14-46cc-bc3f-57729b82ec4c",
  "isSidechain": false,
  "requestId": "req_011Cb4BJxzs9ogVAJWsyEykP",
  "type": "assistant",
  "uuid": "f36c5ff4-17e3-44a3-928f-5eff64e268b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNP1cnQk7S3NzfjXG1oCBY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 23519,
      "output_tokens": 1955,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1955,
          "cache_read_input_tokens": 23519,
          "cache_creation_input_tokens": 3884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3884
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

_source line 16 · 2026-05-15T10:14:44.939Z_

Now I'll write the expanded related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f36c5ff4-17e3-44a3-928f-5eff64e268b3",
  "isSidechain": false,
  "requestId": "req_011Cb4BJxzs9ogVAJWsyEykP",
  "type": "assistant",
  "uuid": "cfd0ea25-deee-4786-816c-9b4fc8782f1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNP1cnQk7S3NzfjXG1oCBY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 23519,
      "output_tokens": 1955,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1955,
          "cache_read_input_tokens": 23519,
          "cache_creation_input_tokens": 3884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3884
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

_source line 17 · 2026-05-15T10:15:14.472Z_

<details open><summary>🔧 Tool call — Write · `toolu_016Ks7vZEbGu9Zxpr4bgfrLK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\n\n\\paragraph{Tool Use and External Computation in LLMs.}\nA growing body of work augments language models with external tools.\nToolformer \\cite{toolformer-2024} teaches LLMs to insert API calls via self-supervised loss filtering, while ToolkenGPT \\cite{toolkengpt-2023} represents tools as special tokens in the embedding space, enabling frozen models to invoke massive tool libraries.\nART \\cite{art-2023} decomposes tasks into multi-step programs that interleave reasoning with tool calls, and Chameleon \\cite{chameleon-2024} composes heterogeneous modules (search, code, vision) via LLM-generated programs.\nReTool \\cite{retool-2026} applies reinforcement learning to let models discover when code execution is preferable to chain-of-thought.\nThese approaches focus on \\emph{learning to use tools}; our work instead asks a prior question: \\emph{what signal drives the decision to route to an external modality at all?}\n\nRecent concurrent studies sharpen this question from multiple angles.\n\\citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect in which LLMs default to external tools even when internal knowledge suffices.\n\\citet{when2tool-2026} show that tool-call decisions are already encoded in hidden states before explicit reasoning occurs.\n\\citet{tool-use-tax-2026} quantify a ``tool-use tax''---cases where invoking a tool degrades rather than improves performance.\n\\citet{to-call-or-not-2026} propose a necessity--utility--affordability framework for deciding whether to call a tool.\nOur counterfactual decomposition provides complementary, environment-grounded evidence: in ScienceWorld, ${\\sim}90\\%$ of the routing signal at $P{=}100$ traces to catastrophic-failure prevention rather than general utility, offering a concrete quantification that these frameworks currently lack.\n\n\\paragraph{Adaptive Computation and Routing.}\nRather than adding new tools, a parallel line of research routes inputs to different computation budgets or models.\nCogRouter \\cite{cogrouter-2026} adapts reasoning depth per step, ARES \\cite{ares-2026} selects among reasoning effort levels for LLM agents, and Mixture-of-Recursions \\cite{mixture-of-recursions-2025} learns token-level recursion depths within a single model.\nMTRouter \\cite{mtrouter-2026} addresses multi-turn routing across heterogeneous models by jointly embedding conversation history and model capabilities.\nThese systems optimize \\emph{how} to route; we focus on \\emph{why} routing helps.\nOur counterfactual analysis reveals that, in interactive environments, the dominant routing signal is not efficiency or capability matching but catastrophic-failure avoidance---a finding that could inform the objective design of future routers.\n\n\\paragraph{Counterfactual Evaluation in RL.}\nCounterfactual reasoning has been used to explain RL agent behavior post hoc.\n\\citet{olson2021counterfactual} generate counterfactual states via deep generative models to highlight features critical to an agent's decisions.\n\\citet{gajcin2023counterfactual} produce counterfactual action explanations that show users which alternative actions would have led to different outcomes.\n\\citet{amitai2024explaining} extend this to action-outcome explanations, contrasting observed and hypothetical trajectories at the step level.\nA common thread is that these methods perturb \\emph{individual actions} within a fixed policy to attribute credit.\nOur approach differs in both purpose and granularity: we execute two \\emph{complete episodes} under different routing strategies (LLM-only vs.\\ LLM+simulator), producing prospective paired comparisons that isolate the routing signal \\emph{before} any router is trained.\nThis episode-level design sidesteps compounding perturbation artifacts and directly measures the aggregate effect of modality access on task outcomes.\n\n\\paragraph{Safe RL and Catastrophic Failure.}\n\\citet{garcia2015comprehensive} survey safe RL methods that constrain policies to avoid catastrophic outcomes, categorizing approaches into constrained optimization, risk-sensitive criteria, and external-knowledge incorporation.\nA common mechanism is reward shaping with large negative penalties for unsafe states, which implicitly teaches agents to avoid irreversible failures.\nOur findings connect to this literature from an analytical rather than algorithmic perspective: the counterfactual decomposition reveals that death avoidance---preventing irreversible task failure---is the dominant component of the routing signal in ScienceWorld.\nThis suggests that modality routing in interactive environments functions primarily as a safety mechanism, and that router design may benefit from explicitly modeling catastrophic-failure risk rather than treating routing as a generic capability-matching problem.\n\n\\paragraph{LLM Agents in Interactive Environments.}\nScienceWorld \\cite{scienceworld-2022} provides a text-based science-experiment environment requiring multi-step causal reasoning, serving as our primary testbed.\nALFWorld \\cite{alfworld-2021} offers a complementary text-based household environment; Voyager \\cite{voyager-2023} demonstrates open-ended exploration in Minecraft using LLM-driven curriculum and skill libraries.\nReAct \\cite{react-2023} interleaves reasoning traces with environment actions and serves as our internal-reasoning baseline.\nMore recent work augments agents with world models: ITP \\cite{itp-2026} uses learned world models for lookahead planning, while Dyna-Think \\cite{dynathink-2025} synergizes reasoning, acting, and world-model simulation.\nBoth inherit the hallucination risks of approximate world models.\nOur deterministic simulator modality provides exact state transitions, and our analysis shows that this exactness matters almost exclusively for death avoidance---the cases where hallucinated transitions would be most costly.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfd0ea25-deee-4786-816c-9b4fc8782f1b",
  "isSidechain": false,
  "requestId": "req_011Cb4BJxzs9ogVAJWsyEykP",
  "type": "assistant",
  "uuid": "c1df4184-3ee8-4092-857b-5ca695ff74b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNP1cnQk7S3NzfjXG1oCBY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 23519,
      "output_tokens": 1955,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1955,
          "cache_read_input_tokens": 23519,
          "cache_creation_input_tokens": 3884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3884
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

_source line 18 · 2026-05-15T10:15:14.511Z_

<details><summary>↩ Tool result · `toolu_016Ks7vZEbGu9Zxpr4bgfrLK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1df4184-3ee8-4092-857b-5ca695ff74b0",
  "isSidechain": false,
  "promptId": "ca07304c-4ca6-4192-a3b8-c383b7da71fe",
  "type": "user",
  "uuid": "e8195980-ef54-4277-8f6c-92f27646ddc7",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\n\n\\paragraph{Tool Use and External Computation in LLMs.}\nA growing body of work augments language models with external tools.\nToolformer \\cite{toolformer-2024} teaches LLMs to insert API calls via self-supervised loss filtering, while ToolkenGPT \\cite{toolkengpt-2023} represents tools as special tokens in the embedding space, enabling frozen models to invoke massive tool libraries.\nART \\cite{art-2023} decomposes tasks into multi-step programs that interleave reasoning with tool calls, and Chameleon \\cite{chameleon-2024} composes heterogeneous modules (search, code, vision) via LLM-generated programs.\nReTool \\cite{retool-2026} applies reinforcement learning to let models discover when code execution is preferable to chain-of-thought.\nThese approaches focus on \\emph{learning to use tools}; our work instead asks a prior question: \\emph{what signal drives the decision to route to an external modality at all?}\n\nRecent concurrent studies sharpen this question from multiple angles.\n\\citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect in which LLMs default to external tools even when internal knowledge suffices.\n\\citet{when2tool-2026} show that tool-call decisions are already encoded in hidden states before explicit reasoning occurs.\n\\citet{tool-use-tax-2026} quantify a ``tool-use tax''---cases where invoking a tool degrades rather than improves performance.\n\\citet{to-call-or-not-2026} propose a necessity--utility--affordability framework for deciding whether to call a tool.\nOur counterfactual decomposition provides complementary, environment-grounded evidence: in ScienceWorld, ${\\sim}90\\%$ of the routing signal at $P{=}100$ traces to catastrophic-failure prevention rather than general utility, offering a concrete quantification that these frameworks currently lack.\n\n\\paragraph{Adaptive Computation and Routing.}\nRather than adding new tools, a parallel line of research routes inputs to different computation budgets or models.\nCogRouter \\cite{cogrouter-2026} adapts reasoning depth per step, ARES \\cite{ares-2026} selects among reasoning effort levels for LLM agents, and Mixture-of-Recursions \\cite{mixture-of-recursions-2025} learns token-level recursion depths within a single model.\nMTRouter \\cite{mtrouter-2026} addresses multi-turn routing across heterogeneous models by jointly embedding conversation history and model capabilities.\nThese systems optimize \\emph{how} to route; we focus on \\emph{why} routing helps.\nOur counterfactual analysis reveals that, in interactive environments, the dominant routing signal is not efficiency or capability matching but catastrophic-failure avoidance---a finding that could inform the objective design of future routers.\n\n\\paragraph{Counterfactual Evaluation in RL.}\nCounterfactual reasoning has been used to explain RL agent behavior post hoc.\n\\citet{olson2021counterfactual} generate counterfactual states via deep generative models to highlight features critical to an agent's decisions.\n\\citet{gajcin2023counterfactual} produce counterfactual action explanations that show users which alternative actions would have led to different outcomes.\n\\citet{amitai2024explaining} extend this to action-outcome explanations, contrasting observed and hypothetical trajectories at the step level.\nA common thread is that these methods perturb \\emph{individual actions} within a fixed policy to attribute credit.\nOur approach differs in both purpose and granularity: we execute two \\emph{complete episodes} under different routing strategies (LLM-only vs.\\ LLM+simulator), producing prospective paired comparisons that isolate the routing signal \\emph{before} any router is trained.\nThis episode-level design sidesteps compounding perturbation artifacts and directly measures the aggregate effect of modality access on task outcomes.\n\n\\paragraph{Safe RL and Catastrophic Failure.}\n\\citet{garcia2015comprehensive} survey safe RL methods that constrain policies to avoid catastrophic outcomes, categorizing approaches into constrained optimization, risk-sensitive criteria, and external-knowledge incorporation.\nA common mechanism is reward shaping with large negative penalties for unsafe states, which implicitly teaches agents to avoid irreversible failures.\nOur findings connect to this literature from an analytical rather than algorithmic perspective: the counterfactual decomposition reveals that death avoidance---preventing irreversible task failure---is the dominant component of the routing signal in ScienceWorld.\nThis suggests that modality routing in interactive environments functions primarily as a safety mechanism, and that router design may benefit from explicitly modeling catastrophic-failure risk rather than treating routing as a generic capability-matching problem.\n\n\\paragraph{LLM Agents in Interactive Environments.}\nScienceWorld \\cite{scienceworld-2022} provides a text-based science-experiment environment requiring multi-step causal reasoning, serving as our primary testbed.\nALFWorld \\cite{alfworld-2021} offers a complementary text-based household environment; Voyager \\cite{voyager-2023} demonstrates open-ended exploration in Minecraft using LLM-driven curriculum and skill libraries.\nReAct \\cite{react-2023} interleaves reasoning traces with environment actions and serves as our internal-reasoning baseline.\nMore recent work augments agents with world models: ITP \\cite{itp-2026} uses learned world models for lookahead planning, while Dyna-Think \\cite{dynathink-2025} synergizes reasoning, acting, and world-model simulation.\nBoth inherit the hallucination risks of approximate world models.\nOur deterministic simulator modality provides exact state transitions, and our analysis shows that this exactness matters almost exclusively for death avoidance---the cases where hallucinated transitions would be most costly.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 20,
        "newStart": 1,
        "newLines": 45,
        "lines": [
          " \\section{Related Work}",
          " ",
          "-\\paragraph{Tool-Use Learning.}",
          "-Toolformer \\cite{toolformer-2024}, ToolkenGPT \\cite{toolkengpt-2023}, ART \\cite{art-2023}, Chameleon \\cite{chameleon-2024}, and ReTool \\cite{retool-2026} learn tool-use policies via self-supervised, embedding-based, or RL approaches.",
          "-We generate labels via \\emph{episode-level counterfactual analysis}, framing routing as \\emph{catastrophic failure prevention}.",
          "+\\paragraph{Tool Use and External Computation in LLMs.}",
          "+A growing body of work augments language models with external tools.",
          "+Toolformer \\cite{toolformer-2024} teaches LLMs to insert API calls via self-supervised loss filtering, while ToolkenGPT \\cite{toolkengpt-2023} represents tools as special tokens in the embedding space, enabling frozen models to invoke massive tool libraries.",
          "+ART \\cite{art-2023} decomposes tasks into multi-step programs that interleave reasoning with tool calls, and Chameleon \\cite{chameleon-2024} composes heterogeneous modules (search, code, vision) via LLM-generated programs.",
          "+ReTool \\cite{retool-2026} applies reinforcement learning to let models discover when code execution is preferable to chain-of-thought.",
          "+These approaches focus on \\emph{learning to use tools}; our work instead asks a prior question: \\emph{what signal drives the decision to route to an external modality at all?}",
          " ",
          "-\\paragraph{Adaptive Computation.}",
          "-CogRouter \\cite{cogrouter-2026}, ARES \\cite{ares-2026}, and Mixture-of-Recursions \\cite{mixture-of-recursions-2025} route \\emph{how much} computation; MTRouter \\cite{mtrouter-2026} routes \\emph{which model}. We route \\emph{which modality} and find death avoidance accounts for ${\\sim}90\\%$ of routing signal at $P{=}100$.",
          "+Recent concurrent studies sharpen this question from multiple angles.",
          "+\\citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect in which LLMs default to external tools even when internal knowledge suffices.",
          "+\\citet{when2tool-2026} show that tool-call decisions are already encoded in hidden states before explicit reasoning occurs.",
          "+\\citet{tool-use-tax-2026} quantify a ``tool-use tax''---cases where invoking a tool degrades rather than improves performance.",
          "+\\citet{to-call-or-not-2026} propose a necessity--utility--affordability framework for deciding whether to call a tool.",
          "+Our counterfactual decomposition provides complementary, environment-grounded evidence: in ScienceWorld, ${\\sim}90\\%$ of the routing signal at $P{=}100$ traces to catastrophic-failure prevention rather than general utility, offering a concrete quantification that these frameworks currently lack.",
          " ",
          "-\\paragraph{World Model Routing.}",
          "-ITP \\cite{itp-2026} and Dyna-Think \\cite{dynathink-2025} route to approximate world models that inherit hallucination failures; our deterministic modality provides exact transitions, mattering almost exclusively for death avoidance.",
          "+\\paragraph{Adaptive Computation and Routing.}",
          "+Rather than adding new tools, a parallel line of research routes inputs to different computation budgets or models.",
          "+CogRouter \\cite{cogrouter-2026} adapts reasoning depth per step, ARES \\cite{ares-2026} selects among reasoning effort levels for LLM agents, and Mixture-of-Recursions \\cite{mixture-of-recursions-2025} learns token-level recursion depths within a single model.",
          "+MTRouter \\cite{mtrouter-2026} addresses multi-turn routing across heterogeneous models by jointly embedding conversation history and model capabilities.",
          "+These systems optimize \\emph{how} to route; we focus on \\emph{why} routing helps.",
          "+Our counterfactual analysis reveals that, in interactive environments, the dominant routing signal is not efficiency or capability matching but catastrophic-failure avoidance---a finding that could inform the objective design of future routers.",
          " ",
          "-\\paragraph{Agent Frameworks.}",
          "-ReAct \\cite{react-2023} serves as our internal-reasoning baseline; ALFWorld \\cite{alfworld-2021} provides a complementary text-based benchmark. We analyze \\emph{when} reasoning should yield to deterministic computation, connecting to safe RL \\citep{garcia2015comprehensive}.",
          "-",
          " \\paragraph{Counterfactual Evaluation in RL.}",
          "-Counterfactual reasoning has been applied to explain RL agent behavior post-hoc---comparing observed actions against hypothetical alternatives \\cite{olson2021counterfactual,gajcin2023counterfactual,amitai2024explaining}. Our approach differs fundamentally: rather than explaining a fixed policy, we execute two complete episodes under different routing strategies, producing prospective paired comparisons that isolate the routing signal before any router is trained.",
          "+Counterfactual reasoning has been used to explain RL agent behavior post hoc.",
          "+\\citet{olson2021counterfactual} generate counterfactual states via deep generative models to highlight features critical to an agent's decisions.",
          "+\\citet{gajcin2023counterfactual} produce counterfactual action explanations that show users which alternative actions would have led to different outcomes.",
          "+\\citet{amitai2024explaining} extend this to action-outcome explanations, contrasting observed and hypothetical trajectories at the step level.",
          "+A common thread is that these methods perturb \\emph{individual actions} within a fixed policy to attribute credit.",
          "+Our approach differs in both purpose and granularity: we execute two \\emph{complete episodes} under different routing strategies (LLM-only vs.\\ LLM+simulator), producing prospective paired comparisons that isolate the routing signal \\emph{before} any router is trained.",
          "+This episode-level design sidesteps compounding perturbation artifacts and directly measures the aggregate effect of modality access on task outcomes.",
          " ",
          "-\\paragraph{Concurrent Work.}",
          "-Concurrent studies examine complementary aspects: cognitive illusions driving tool overuse \\cite{tool-overuse-illusion-2026}, hidden-state encoding of tool-call decisions \\cite{when2tool-2026}, a ``tool-use tax'' where tools are not always beneficial \\cite{tool-use-tax-2026}, and necessity/utility/affordability evaluation \\cite{to-call-or-not-2026}. Our death avoidance decomposition provides concrete quantification---${\\sim}90\\%$ of routing signal at $P{=}100$ stems from catastrophic-failure prevention---grounding these frameworks in interactive-environment evidence.",
          "\\ No newline at end of file",
          "+\\paragraph{Safe RL and Catastrophic Failure.}",
          "+\\citet{garcia2015comprehensive} survey safe RL methods that constrain policies to avoid catastrophic outcomes, categorizing approaches into constrained optimization, risk-sensitive criteria, and external-knowledge incorporation.",
          "+A common mechanism is reward shaping with large negative penalties for unsafe states, which implicitly teaches agents to avoid irreversible failures.",
          "+Our findings connect to this literature from an analytical rather than algorithmic perspective: the counterfactual decomposition reveals that death avoidance---preventing irreversible task failure---is the dominant component of the routing signal in ScienceWorld.",
          "+This suggests that modality routing in interactive environments functions primarily as a safety mechanism, and that router design may benefit from explicitly modeling catastrophic-failure risk rather than treating routing as a generic capability-matching problem.",
          "+",
          "+\\paragraph{LLM Agents in Interactive Environments.}",
          "+ScienceWorld \\cite{scienceworld-2022} provides a text-based science-experiment environment requiring multi-step causal reasoning, serving as our primary testbed.",
          "+ALFWorld \\cite{alfworld-2021} offers a complementary text-based household environment; Voyager \\cite{voyager-2023} demonstrates open-ended exploration in Minecraft using LLM-driven curriculum and skill libraries.",
          "+ReAct \\cite{react-2023} interleaves reasoning traces with environment actions and serves as our internal-reasoning baseline.",
          "+More recent work augments agents with world models: ITP \\cite{itp-2026} uses learned world models for lookahead planning, while Dyna-Think \\cite{dynathink-2025} synergizes reasoning, acting, and world-model simulation.",
          "+Both inherit the hallucination risks of approximate world models.",
          "+Our deterministic simulator modality provides exact state transitions, and our analysis shows that this exactness matters almost exclusively for death avoidance---the cases where hallucinated transitions would be most costly."
        ]
      }
    ],
    "originalFile": "\\section{Related Work}\n\n\\paragraph{Tool-Use Learning.}\nToolformer \\cite{toolformer-2024}, ToolkenGPT \\cite{toolkengpt-2023}, ART \\cite{art-2023}, Chameleon \\cite{chameleon-2024}, and ReTool \\cite{retool-2026} learn tool-use policies via self-supervised, embedding-based, or RL approaches.\nWe generate labels via \\emph{episode-level counterfactual analysis}, framing routing as \\emph{catastrophic failure prevention}.\n\n\\paragraph{Adaptive Computation.}\nCogRouter \\cite{cogrouter-2026}, ARES \\cite{ares-2026}, and Mixture-of-Recursions \\cite{mixture-of-recursions-2025} route \\emph{how much} computation; MTRouter \\cite{mtrouter-2026} routes \\emph{which model}. We route \\emph{which modality} and find death avoidance accounts for ${\\sim}90\\%$ of routing signal at $P{=}100$.\n\n\\paragraph{World Model Routing.}\nITP \\cite{itp-2026} and Dyna-Think \\cite{dynathink-2025} route to approximate world models that inherit hallucination failures; our deterministic modality provides exact transitions, mattering almost exclusively for death avoidance.\n\n\\paragraph{Agent Frameworks.}\nReAct \\cite{react-2023} serves as our internal-reasoning baseline; ALFWorld \\cite{alfworld-2021} provides a complementary text-based benchmark. We analyze \\emph{when} reasoning should yield to deterministic computation, connecting to safe RL \\citep{garcia2015comprehensive}.\n\n\\paragraph{Counterfactual Evaluation in RL.}\nCounterfactual reasoning has been applied to explain RL agent behavior post-hoc---comparing observed actions against hypothetical alternatives \\cite{olson2021counterfactual,gajcin2023counterfactual,amitai2024explaining}. Our approach differs fundamentally: rather than explaining a fixed policy, we execute two complete episodes under different routing strategies, producing prospective paired comparisons that isolate the routing signal before any router is trained.\n\n\\paragraph{Concurrent Work.}\nConcurrent studies examine complementary aspects: cognitive illusions driving tool overuse \\cite{tool-overuse-illusion-2026}, hidden-state encoding of tool-call decisions \\cite{when2tool-2026}, a ``tool-use tax'' where tools are not always beneficial \\cite{tool-use-tax-2026}, and necessity/utility/affordability evaluation \\cite{to-call-or-not-2026}. Our death avoidance decomposition provides concrete quantification---${\\sim}90\\%$ of routing signal at $P{=}100$ stems from catastrophic-failure prevention---grounding these frameworks in interactive-environment evidence.",
    "userModified": false
  },
  "sourceToolAssistantUUID": "c1df4184-3ee8-4092-857b-5ca695ff74b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T10:15:18.625Z_

Related Work 已扩写完成。5 个 paragraph 覆盖了要求的全部主题，所有引用均来自 `references.bib`，每个段落末尾都有与本文工作的明确定位对比。篇幅约 1 page。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8195980-ef54-4277-8f6c-92f27646ddc7",
  "isSidechain": false,
  "requestId": "req_011Cb4BMyzyfxCw1eo5EomaF",
  "type": "assistant",
  "uuid": "52ad4e42-096b-4079-a832-26b1ef13d9b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01156CgRhKeaXooEPGHbv5At",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2007,
      "cache_read_input_tokens": 27403,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2007,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 27403,
          "cache_creation_input_tokens": 2007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2007
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

_source line 20_

```json
{
  "type": "last-prompt",
  "leafUuid": "52ad4e42-096b-4079-a832-26b1ef13d9b3",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Expand related work section for long paper",
  "sessionId": "2e772352-b537-4f05-916f-93da1b428592"
}
```

---
