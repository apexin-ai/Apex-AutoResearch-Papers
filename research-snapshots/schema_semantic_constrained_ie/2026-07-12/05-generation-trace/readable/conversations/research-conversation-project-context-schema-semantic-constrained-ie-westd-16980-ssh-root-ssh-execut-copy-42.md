# Research conversation: <project_context> # 项目: schema_semantic_constrained_ie ## 运行环境 - 服务器名: westd-16980 - SSH 账户: root（调用 ssh_execute / submi

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-1/7c183f8e-6937-44d3-95b4-38b985cfc909.jsonl`
- **Structured JSON:** [`441308c9ee9074180dc5.json`](../../sessions/44/441308c9ee9074180dc5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T02:35:23.406Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T02:35:23.406Z",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "content": "&lt;project_context>\n# 项目: schema_semantic_constrained_ie\n\n## 运行环境\n- 服务器名: westd-16980\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/schema_semantic_constrained_ie\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n为 OntoCoDec 论文的 Related Work section 做文献调研。\n\n## 项目背景\nOntoCoDec 将 IE ontology 的 domain/range 约束编译进 LLM 解码时的 logits masking，在 SciERC 上实现 DR violation 15.37%→0.93%（↓94%）且 F1 无损。方法分两层：\n- Grammar 层 (XGrammar): JSON schema + enum 约束，消除 RV/ET violations\n- Semantic 层 (TypeConstraintProcessor): domain/range logits masking，消除 DR violations\n- 两种组合策略: S1 (单通道 grammar+semantic) 和 S2 (两通道分离)\n\n## 调研要求\n覆盖 5 个 constraint paradigm，每个找 3-5 篇代表性工作（优先 2023-2026 近期工作）：\n\n### 1. Grammar-constrained decoding\n- XGrammar, Guidance, Outlines, LMQL 等\n- 重点：如何用 CFG/正则/schema 约束 LLM 输出格式\n- 与 OntoCoDec 关系：OntoCoDec 的 grammar 层基于 XGrammar\n\n### 2. Vocabulary/type-constrained generation\n- GENRE (entity linking), constrained beam search, trie-based decoding\n- 重点：在 beam/token 级别限制输出词汇\n- 与 OntoCoDec 关系：OntoCoDec 的 semantic 层是 token 级 logits masking\n\n### 3. Structural constraint for IE\n- structured prediction + LLM, UIE, InstructUIE, GoLLIE, CodeIE 等\n- 重点：如何让 LLM 遵守 IE 任务的结构约束\n- 与 OntoCoDec 关系：这些方法靠 prompt/训练而非 decoding-time enforcement\n\n### 4. Type-checking / ontology validation in NLP\n- post-hoc validation approaches, LLM+ASP (ICLP 2025), ontology-guided NER/RE\n- 重点：利用本体知识验证/约束 NLP 输出\n- 与 OntoCoDec 关系：post-hoc vs decoding-time enforcement 的根本区别\n\n### 5. Constrained decoding quality concerns\n- CRANE (NeurIPS 2024), Structure Snowballing 等\n- 重点：constrained decoding 对生成质量的负面影响\n- 与 OntoCoDec 关系：OntoCoDec 证明 F1 无损，回应这类 concern\n\n## 输出格式\n写到 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/related_work_survey.md`\n\n每个 paradigm 一个 section，每篇论文记录：\n- **Title** | Venue Year\n- **核心方法**: 1-2 句话\n- **与 OntoCoDec 的关系**: differentiation point（为什么 OntoCoDec 不同/更好/互补）\n- **BibTeX key 建议**: 供后续引用\n\n最后一个 section 总结 OntoCoDec 在 landscape 中的 positioning。\n\n完成后用 register_artifact 注册产出文件。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T02:35:23.410Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T02:35:23.410Z",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-14T02:35:23.445Z_

&lt;project_context>
# 项目: schema_semantic_constrained_ie

## 运行环境
- 服务器名: westd-16980
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/schema_semantic_constrained_ie


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
为 OntoCoDec 论文的 Related Work section 做文献调研。

## 项目背景
OntoCoDec 将 IE ontology 的 domain/range 约束编译进 LLM 解码时的 logits masking，在 SciERC 上实现 DR violation 15.37%→0.93%（↓94%）且 F1 无损。方法分两层：
- Grammar 层 (XGrammar): JSON schema + enum 约束，消除 RV/ET violations
- Semantic 层 (TypeConstraintProcessor): domain/range logits masking，消除 DR violations
- 两种组合策略: S1 (单通道 grammar+semantic) 和 S2 (两通道分离)

## 调研要求
覆盖 5 个 constraint paradigm，每个找 3-5 篇代表性工作（优先 2023-2026 近期工作）：

### 1. Grammar-constrained decoding
- XGrammar, Guidance, Outlines, LMQL 等
- 重点：如何用 CFG/正则/schema 约束 LLM 输出格式
- 与 OntoCoDec 关系：OntoCoDec 的 grammar 层基于 XGrammar

### 2. Vocabulary/type-constrained generation
- GENRE (entity linking), constrained beam search, trie-based decoding
- 重点：在 beam/token 级别限制输出词汇
- 与 OntoCoDec 关系：OntoCoDec 的 semantic 层是 token 级 logits masking

### 3. Structural constraint for IE
- structured prediction + LLM, UIE, InstructUIE, GoLLIE, CodeIE 等
- 重点：如何让 LLM 遵守 IE 任务的结构约束
- 与 OntoCoDec 关系：这些方法靠 prompt/训练而非 decoding-time enforcement

### 4. Type-checking / ontology validation in NLP
- post-hoc validation approaches, LLM+ASP (ICLP 2025), ontology-guided NER/RE
- 重点：利用本体知识验证/约束 NLP 输出
- 与 OntoCoDec 关系：post-hoc vs decoding-time enforcement 的根本区别

### 5. Constrained decoding quality concerns
- CRANE (NeurIPS 2024), Structure Snowballing 等
- 重点：constrained decoding 对生成质量的负面影响
- 与 OntoCoDec 关系：OntoCoDec 证明 F1 无损，回应这类 concern

## 输出格式
写到 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/related_work_survey.md`

每个 paradigm 一个 section，每篇论文记录：
- **Title** | Venue Year
- **核心方法**: 1-2 句话
- **与 OntoCoDec 的关系**: differentiation point（为什么 OntoCoDec 不同/更好/互补）
- **BibTeX key 建议**: 供后续引用

最后一个 section 总结 OntoCoDec 在 landscape 中的 positioning。

完成后用 register_artifact 注册产出文件。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "type": "user",
  "uuid": "e044b841-608d-4183-b849-f2763cb10441",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T02:35:23.444Z_

```json
{
  "parentUuid": "e044b841-608d-4183-b849-f2763cb10441",
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
  "uuid": "725d5605-5e81-4dc6-9e28-93edeb540c45",
  "timestamp": "2026-05-14T02:35:23.444Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T02:35:23.444Z_

```json
{
  "parentUuid": "725d5605-5e81-4dc6-9e28-93edeb540c45",
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
  "uuid": "d19af6a9-e57f-4731-a601-ccc2b4c414fc",
  "timestamp": "2026-05-14T02:35:23.444Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T02:35:23.444Z_

```json
{
  "parentUuid": "d19af6a9-e57f-4731-a601-ccc2b4c414fc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4725d35e-9c05-4dfe-8e20-543e76d6cb24",
  "timestamp": "2026-05-14T02:35:23.444Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
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
  "aiTitle": "Literature survey for OntoCoDec related work",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909"
}
```

---

### Assistant

_source line 8 · 2026-05-14T02:35:26.304Z_

我来为 OntoCoDec 论文做 Related Work 文献调研。先搜索各个 paradigm 的代表性工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4725d35e-9c05-4dfe-8e20-543e76d6cb24",
  "isSidechain": false,
  "requestId": "req_011Cb1gVDDmjwRShV8rWDrdY",
  "type": "assistant",
  "uuid": "dc7be6f2-9c92-426f-8525-cba86477cabc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HcpT3L6fdyHwE3hX2VG4Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11684,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1596,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11684,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1596,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11684
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

_source line 9 · 2026-05-14T02:35:32.700Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015diNCrEvx5fpG7XJTAoxzF`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Grammar-constrained decoding survey",
  "prompt": "Search the web for representative papers on grammar-constrained decoding for LLMs (2023-2026). I need 4-5 key papers covering:\n\n1. **XGrammar** - the system for grammar-guided structured generation (likely from MLSys or similar venue)\n2. **Guidance** (Microsoft) - constrained generation framework\n3. **Outlines** (2024) - structured text generation with regular expressions/CFGs\n4. **LMQL** - query language for LLMs with constraints\n5. **SGLang** or other notable grammar-constrained decoding systems\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nAlso search for any survey papers on constrained decoding for LLMs (2024-2026).\n\nReport all findings in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc7be6f2-9c92-426f-8525-cba86477cabc",
  "isSidechain": false,
  "requestId": "req_011Cb1gVDDmjwRShV8rWDrdY",
  "type": "assistant",
  "uuid": "5f8a8a4e-4c09-4d69-942b-864b618a53bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HcpT3L6fdyHwE3hX2VG4Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11684,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1596,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11684,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1596,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11684
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

_source line 10 · 2026-05-14T02:35:36.994Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XXuMqxUuY6Fea3GpLwCfR2`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Vocabulary/type-constrained generation survey",
  "prompt": "Search the web for representative papers on vocabulary-constrained and type-constrained generation/decoding for NLP (2020-2026). I need 4-5 key papers covering:\n\n1. **GENRE** - Generative Entity Retrieval (De Cao et al.) - constrained beam search for entity linking\n2. **Constrained beam search** methods - trie-based decoding for knowledge-grounded generation\n3. **NeuroLogDecoding** or **Neurologic** - constrained text generation with lexical constraints\n4. **TRIE-based constrained decoding** approaches for entity/type-constrained generation\n5. Any recent (2024-2026) work on token-level logits masking for type constraints in NLP\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f8a8a4e-4c09-4d69-942b-864b618a53bd",
  "isSidechain": false,
  "requestId": "req_011Cb1gVDDmjwRShV8rWDrdY",
  "type": "assistant",
  "uuid": "0e303a99-7b8f-4a49-9a10-64d7ef6abea0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HcpT3L6fdyHwE3hX2VG4Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11684,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1596,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11684,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1596,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11684
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

_source line 11 · 2026-05-14T02:35:41.728Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KVcWuXxaboYA4GoYk91uGK`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Structural constraint IE survey",
  "prompt": "Search the web for representative papers on structural constraints for Information Extraction (IE) with LLMs (2022-2026). I need 5-6 key papers covering:\n\n1. **UIE** (Unified Structure Generation for Universal Information Extraction) - Lu et al.\n2. **InstructUIE** - instruction-tuned universal IE\n3. **GoLLIE** - Guideline-following Large Language Model for IE (likely ICLR 2024)\n4. **CodeIE** - code generation approach for IE\n5. **USM** or **UniRel** or other structured prediction + LLM approaches for IE\n6. Any 2024-2025 work on making LLMs output structured IE results (NER, RE, EE)\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e303a99-7b8f-4a49-9a10-64d7ef6abea0",
  "isSidechain": false,
  "requestId": "req_011Cb1gVDDmjwRShV8rWDrdY",
  "type": "assistant",
  "uuid": "f6eda583-72d4-4d63-872f-3dd0a70cfffe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HcpT3L6fdyHwE3hX2VG4Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11684,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1596,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11684,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1596,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11684
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

_source line 12 · 2026-05-14T02:35:46.057Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NScH3NoBdckpLKd2TLJxXN`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Ontology validation NLP survey",
  "prompt": "Search the web for representative papers on type-checking, ontology validation, and ontology-guided constraints in NLP (2020-2026). I need 4-5 key papers covering:\n\n1. **LLM+ASP** approaches - using Answer Set Programming to validate/constrain LLM outputs (check ICLP 2025 or similar logic programming venues)\n2. **Ontology-guided NER** - using ontological knowledge to guide named entity recognition\n3. **Post-hoc validation** approaches for LLM outputs against knowledge bases or ontologies\n4. **Type-constrained relation extraction** - enforcing entity type constraints in RE\n5. Any work on using domain/range constraints from ontologies to validate IE outputs\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6eda583-72d4-4d63-872f-3dd0a70cfffe",
  "isSidechain": false,
  "requestId": "req_011Cb1gVDDmjwRShV8rWDrdY",
  "type": "assistant",
  "uuid": "f095d071-d395-4e6f-8cd1-782aedecbb6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HcpT3L6fdyHwE3hX2VG4Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11684,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1596,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11684,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1596,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11684
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

_source line 13 · 2026-05-14T02:35:50.437Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01G6VBcaGt99gKykurE3Zfsz`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Constrained decoding quality survey",
  "prompt": "Search the web for representative papers on the quality concerns and negative effects of constrained decoding on LLM generation (2023-2026). I need 3-5 key papers covering:\n\n1. **CRANE** (NeurIPS 2024) - about how constrained decoding can degrade generation quality. Search for \"CRANE constrained decoding NeurIPS 2024\" or \"Let Me Speak Freely\"\n2. **Structure Snowballing** or any paper about how structured output constraints cause quality degradation\n3. Any empirical studies showing constrained decoding hurts LLM performance\n4. Papers proposing solutions to maintain quality under constraints\n5. \"Let Me Speak Freely\" paper if different from CRANE\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method/finding in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f095d071-d395-4e6f-8cd1-782aedecbb6a",
  "isSidechain": false,
  "requestId": "req_011Cb1gVDDmjwRShV8rWDrdY",
  "type": "assistant",
  "uuid": "33724b89-1514-4a21-b2e8-e809fdf54f7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HcpT3L6fdyHwE3hX2VG4Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11684,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1596,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11684,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1596,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11684
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

_source line 14 · 2026-05-14T02:36:49.526Z_

<details><summary>↩ Tool result · `toolu_01XXuMqxUuY6Fea3GpLwCfR2`</summary>

```text
Here are the findings.

---

## 1. GENRE -- Autoregressive Entity Retrieval

- **Title:** Autoregressive Entity Retrieval
- **Authors:** Nicola De Cao, Gautier Izacard, Sebastian Riedel, Fabio Petroni
- **Venue:** ICLR 2021 (Spotlight)
- **ArXiv:** 2010.00904
- **Core method:** First system to retrieve entities by autoregressively generating entity names token-by-token using a fine-tuned BART model. Uses a prefix trie (trie-based constrained beam search) to restrict decoding to only valid entity identifiers, dramatically reducing memory footprint compared to bi-encoder retrieval while achieving SOTA on 20+ entity disambiguation and linking benchmarks.

---

## 2. GenIE -- Generative Information Extraction

- **Title:** GenIE: Generative Information Extraction
- **Authors:** Martin Josifoski, Nicola De Cao, Maxime Peyrard, Fabio Petroni, Robert West
- **Venue:** NAACL 2022
- **ArXiv:** 2112.08340
- **Core method:** Autoregressive seq2seq model that generates (subject, relation, object) triplets for closed IE. Combines trie-based lexical constraints (forcing outputs to be valid entity/relation identifiers from a predefined schema) with state-based constraints (enforcing valid triplet structure), achieving end-to-end extraction without pipeline components.

---

## 3. NeuroLogic Decoding

- **Title:** NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints
- **Authors:** Ximing Lu, Peter West, Rowan Zellers, Ronan Le Bras, Chandra Bhagavatula, Yejin Choi
- **Venue:** NAACL 2021
- **ArXiv:** 2010.12884
- **Core method:** A decoding algorithm that enables LMs to generate fluent text satisfying complex lexical constraints expressed as predicate logic formulas (conjunctions/disjunctions of must-include or must-exclude tokens). Operates by pruning and re-ranking beams at each step, with asymptotic runtime equivalent to standard beam search.

**Follow-up:** NeuroLogic A\*esque Decoding (Lu et al., NAACL 2022, arXiv 2112.08726) extends this with lookahead heuristics inspired by A\* search, estimating future constraint satisfaction cost to avoid dead ends.

---

## 4. Knowledge Infused Decoding (KID)

- **Title:** Knowledge Infused Decoding
- **Authors:** Ruibo Liu, Guoqing Zheng, Shashank Gupta, Radhika Gaonkar, Chongyang Gao, Soroush Vosoughi, Milad Shokouhi, Ahmed H. Awadallah
- **Venue:** ICLR 2022
- **ArXiv:** 2204.03084
- **Core method:** Task-agnostic decoding algorithm that dynamically infuses external knowledge at each generation step. Maintains a local knowledge memory interacting with a dynamically constructed knowledge trie from retrieved documents, using RL-based scoring to guide token selection toward knowledge-grounded continuations. Outperforms task-specific models on 6 knowledge-intensive NLG tasks.

---

## 5. Grammar-Constrained Decoding for Structured NLP Tasks (recent, 2023)

- **Title:** Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning
- **Authors:** Saibo Geng, Martin Josifoski, Maxime Peyrard, Robert West
- **Venue:** EMNLP 2023
- **ArXiv:** 2305.13971
- **Core method:** Proposes grammar-constrained decoding (GCD) as a unified framework for structured NLP: at each decoding step, tokens violating a formal grammar are masked by setting logits to negative infinity, guaranteeing structurally valid output without finetuning. Introduces input-dependent grammars for flexibility. Evaluated on information extraction, entity disambiguation, and constituency parsing -- directly relevant to type-constrained generation via logit masking.

This is the most directly relevant recent work on token-level logit masking for type/schema constraints. The XGrammar system (Dong et al., 2024) further optimizes this approach for production LLM serving (default backend in vLLM/SGLang as of 2026), but the Geng et al. EMNLP 2023 paper is the key academic reference connecting grammar-constrained logit masking to IE and entity typing tasks.

---

Sources:
- [Autoregressive Entity Retrieval (GENRE) - arXiv](https://arxiv.org/abs/2010.00904)
- [GenIE: Generative Information Extraction - arXiv](https://arxiv.org/abs/2112.08340)
- [GenIE - ACL Anthology](https://aclanthology.org/2022.naacl-main.342/)
- [NeuroLogic Decoding - arXiv](https://arxiv.org/abs/2010.12884)
- [NeuroLogic Decoding - ACL Anthology](https://aclanthology.org/2021.naacl-main.339/)
- [NeuroLogic A*esque Decoding - arXiv](https://arxiv.org/abs/2112.08726)
- [Knowledge Infused Decoding - arXiv](https://arxiv.org/abs/2204.03084)
- [Grammar-Constrained Decoding - arXiv](https://arxiv.org/abs/2305.13971)
- [Grammar-Constrained Decoding - ACL Anthology](https://aclanthology.org/2023.emnlp-main.674/)
- [GENRE GitHub Repository](https://github.com/facebookresearch/GENRE)

agentId: ae39bf4ac705763a8 (use SendMessage with to: 'ae39bf4ac705763a8' to continue this agent)
&lt;usage>total_tokens: 27051
tool_uses: 11
duration_ms: 72529&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e303a99-7b8f-4a49-9a10-64d7ef6abea0",
  "isSidechain": false,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "type": "user",
  "uuid": "d2189d05-4682-4067-bf15-b63940cd5815",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for representative papers on vocabulary-constrained and type-constrained generation/decoding for NLP (2020-2026). I need 4-5 key papers covering:\n\n1. **GENRE** - Generative Entity Retrieval (De Cao et al.) - constrained beam search for entity linking\n2. **Constrained beam search** methods - trie-based decoding for knowledge-grounded generation\n3. **NeuroLogDecoding** or **Neurologic** - constrained text generation with lexical constraints\n4. **TRIE-based constrained decoding** approaches for entity/type-constrained generation\n5. Any recent (2024-2026) work on token-level logits masking for type constraints in NLP\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format.",
    "agentId": "ae39bf4ac705763a8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings.\n\n---\n\n## 1. GENRE -- Autoregressive Entity Retrieval\n\n- **Title:** Autoregressive Entity Retrieval\n- **Authors:** Nicola De Cao, Gautier Izacard, Sebastian Riedel, Fabio Petroni\n- **Venue:** ICLR 2021 (Spotlight)\n- **ArXiv:** 2010.00904\n- **Core method:** First system to retrieve entities by autoregressively generating entity names token-by-token using a fine-tuned BART model. Uses a prefix trie (trie-based constrained beam search) to restrict decoding to only valid entity identifiers, dramatically reducing memory footprint compared to bi-encoder retrieval while achieving SOTA on 20+ entity disambiguation and linking benchmarks.\n\n---\n\n## 2. GenIE -- Generative Information Extraction\n\n- **Title:** GenIE: Generative Information Extraction\n- **Authors:** Martin Josifoski, Nicola De Cao, Maxime Peyrard, Fabio Petroni, Robert West\n- **Venue:** NAACL 2022\n- **ArXiv:** 2112.08340\n- **Core method:** Autoregressive seq2seq model that generates (subject, relation, object) triplets for closed IE. Combines trie-based lexical constraints (forcing outputs to be valid entity/relation identifiers from a predefined schema) with state-based constraints (enforcing valid triplet structure), achieving end-to-end extraction without pipeline components.\n\n---\n\n## 3. NeuroLogic Decoding\n\n- **Title:** NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints\n- **Authors:** Ximing Lu, Peter West, Rowan Zellers, Ronan Le Bras, Chandra Bhagavatula, Yejin Choi\n- **Venue:** NAACL 2021\n- **ArXiv:** 2010.12884\n- **Core method:** A decoding algorithm that enables LMs to generate fluent text satisfying complex lexical constraints expressed as predicate logic formulas (conjunctions/disjunctions of must-include or must-exclude tokens). Operates by pruning and re-ranking beams at each step, with asymptotic runtime equivalent to standard beam search.\n\n**Follow-up:** NeuroLogic A\\*esque Decoding (Lu et al., NAACL 2022, arXiv 2112.08726) extends this with lookahead heuristics inspired by A\\* search, estimating future constraint satisfaction cost to avoid dead ends.\n\n---\n\n## 4. Knowledge Infused Decoding (KID)\n\n- **Title:** Knowledge Infused Decoding\n- **Authors:** Ruibo Liu, Guoqing Zheng, Shashank Gupta, Radhika Gaonkar, Chongyang Gao, Soroush Vosoughi, Milad Shokouhi, Ahmed H. Awadallah\n- **Venue:** ICLR 2022\n- **ArXiv:** 2204.03084\n- **Core method:** Task-agnostic decoding algorithm that dynamically infuses external knowledge at each generation step. Maintains a local knowledge memory interacting with a dynamically constructed knowledge trie from retrieved documents, using RL-based scoring to guide token selection toward knowledge-grounded continuations. Outperforms task-specific models on 6 knowledge-intensive NLG tasks.\n\n---\n\n## 5. Grammar-Constrained Decoding for Structured NLP Tasks (recent, 2023)\n\n- **Title:** Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning\n- **Authors:** Saibo Geng, Martin Josifoski, Maxime Peyrard, Robert West\n- **Venue:** EMNLP 2023\n- **ArXiv:** 2305.13971\n- **Core method:** Proposes grammar-constrained decoding (GCD) as a unified framework for structured NLP: at each decoding step, tokens violating a formal grammar are masked by setting logits to negative infinity, guaranteeing structurally valid output without finetuning. Introduces input-dependent grammars for flexibility. Evaluated on information extraction, entity disambiguation, and constituency parsing -- directly relevant to type-constrained generation via logit masking.\n\nThis is the most directly relevant recent work on token-level logit masking for type/schema constraints. The XGrammar system (Dong et al., 2024) further optimizes this approach for production LLM serving (default backend in vLLM/SGLang as of 2026), but the Geng et al. EMNLP 2023 paper is the key academic reference connecting grammar-constrained logit masking to IE and entity typing tasks.\n\n---\n\nSources:\n- [Autoregressive Entity Retrieval (GENRE) - arXiv](https://arxiv.org/abs/2010.00904)\n- [GenIE: Generative Information Extraction - arXiv](https://arxiv.org/abs/2112.08340)\n- [GenIE - ACL Anthology](https://aclanthology.org/2022.naacl-main.342/)\n- [NeuroLogic Decoding - arXiv](https://arxiv.org/abs/2010.12884)\n- [NeuroLogic Decoding - ACL Anthology](https://aclanthology.org/2021.naacl-main.339/)\n- [NeuroLogic A*esque Decoding - arXiv](https://arxiv.org/abs/2112.08726)\n- [Knowledge Infused Decoding - arXiv](https://arxiv.org/abs/2204.03084)\n- [Grammar-Constrained Decoding - arXiv](https://arxiv.org/abs/2305.13971)\n- [Grammar-Constrained Decoding - ACL Anthology](https://aclanthology.org/2023.emnlp-main.674/)\n- [GENRE GitHub Repository](https://github.com/facebookresearch/GENRE)"
      }
    ],
    "totalDurationMs": 72529,
    "totalTokens": 27051,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 745,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 23696,
      "output_tokens": 1476,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1134
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 745,
          "output_tokens": 1476,
          "cache_read_input_tokens": 23696,
          "cache_creation_input_tokens": 1134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1134,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 11
    }
  },
  "sourceToolAssistantUUID": "0e303a99-7b8f-4a49-9a10-64d7ef6abea0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "leafUuid": "d2189d05-4682-4067-bf15-b63940cd5815",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey for OntoCoDec related work",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909"
}
```

---

### Tool result

_source line 17 · 2026-05-14T02:37:00.670Z_

<details><summary>↩ Tool result · `toolu_01KVcWuXxaboYA4GoYk91uGK`</summary>

```text
Here are the findings for 6 representative papers on structural constraints for IE with LLMs (2022--2026):

---

**1. UIE -- Unified Structure Generation for Universal Information Extraction**
- **Authors:** Yaojie Lu, Qing Liu, Dai Dai, et al.
- **Venue:** ACL 2022
- **ArXiv:** 2203.12277
- **Method:** Defines a structured extraction language (SEL) to uniformly encode different IE output structures (entity, relation, event, sentiment). Uses a schema-based prompt mechanism (Structural Schema Instructor) with a large-scale pre-trained text-to-structure model to adaptively generate target structures. Achieves SOTA on 4 IE tasks across 13 datasets in supervised, low-resource, and few-shot settings.

---

**2. InstructUIE -- Multi-task Instruction Tuning for Unified Information Extraction**
- **Authors:** Xiao Wang, Weikang Zhou, Can Zu, et al.
- **Venue:** arXiv 2023 (2304.08085)
- **ArXiv:** 2304.08085
- **Method:** Builds IE INSTRUCTIONS, a benchmark of 32 diverse IE datasets in unified text-to-text format with expert-written instructions. Fine-tunes Flan-T5 on this benchmark, enabling a single model to handle NER, RE, EE, etc. via natural language instructions. Demonstrates that instruction-tuned smaller models can substantially outperform GPT-3.5 on IE tasks.

---

**3. GoLLIE -- Annotation Guidelines improve Zero-Shot Information-Extraction**
- **Authors:** Oscar Sainz, Iker Garcia-Ferrero, Rodrigo Agerri, et al.
- **Venue:** ICLR 2024
- **ArXiv:** 2310.03668
- **Method:** Fine-tunes Code-LLaMA to follow annotation guidelines expressed as Python class definitions (code-based schema representation). The model takes entity/relation/event type definitions as Python dataclasses and generates structured output as Python code. This code-based formulation enables strong zero-shot generalization to unseen IE schemas, outperforming previous zero-shot IE approaches.

---

**4. CodeIE -- Large Code Generation Models are Better Few-Shot Information Extractors**
- **Authors:** Peng Li, Tianxiang Sun, Qiong Tang, et al.
- **Venue:** ACL 2023
- **ArXiv:** 2305.05711
- **Method:** Recasts IE structured output as code rather than natural language and uses code-LLMs (e.g., Codex) with code-style prompts to perform NER and RE as code generation tasks. The code formulation naturally captures the structured nature of IE outputs. Consistently outperforms both fine-tuned IE-specific models (e.g., UIE) and NL-LLM prompting under few-shot settings.

---

**5. USM -- Universal Information Extraction as Unified Semantic Matching**
- **Authors:** Jie Lou, Yaojie Lu, Dai Dai, et al.
- **Venue:** AAAI 2023
- **ArXiv:** 2301.03282
- **Method:** Models IE as unified semantic matching via three token-linking operations that capture structuring (identifying spans/structures) and conceptualizing (mapping to schema types). Jointly encodes schema and input text, extracts substructures in parallel, and controllably decodes target structures on demand. Achieves SOTA on 4 IE tasks with strong zero/few-shot transfer ability.

---

**6. ADELIE -- Aligning Large Language Models on Information Extraction**
- **Authors:** Yunjia Qi, Hao Peng, Xiaozhi Wang, et al. (THU-KEG)
- **Venue:** EMNLP 2024
- **ArXiv:** 2405.05008
- **Method:** Constructs IEInstruct, a high-quality alignment corpus for IE, then trains LLMs with instruction tuning (SFT) followed by Direct Preference Optimization (DPO). Covers closed IE, open IE, and on-demand IE. ADELIE achieves SOTA among open-source models on diverse held-out IE benchmarks while preserving general LLM capabilities. Released in 1.5B/3B/7B sizes.

---

**Summary of the landscape:** These papers represent three main paradigms for structural constraints in LLM-based IE:
- **Text-to-structure generation** (UIE, InstructUIE): Define a linearized structure language and train seq2seq models to generate it.
- **Code-based schema representation** (GoLLIE, CodeIE): Leverage code LLMs and Python class/function definitions to naturally express IE schemas and structured outputs.
- **Semantic matching / alignment** (USM, ADELIE): Frame IE as matching or align LLMs specifically for IE through curated data and preference optimization.

agentId: a88824f793ba94b4e (use SendMessage with to: 'a88824f793ba94b4e' to continue this agent)
&lt;usage>total_tokens: 27410
tool_uses: 12
duration_ms: 78939&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6eda583-72d4-4d63-872f-3dd0a70cfffe",
  "isSidechain": false,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "type": "user",
  "uuid": "61d9801d-b401-44eb-98f0-d2b468423f85",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for representative papers on structural constraints for Information Extraction (IE) with LLMs (2022-2026). I need 5-6 key papers covering:\n\n1. **UIE** (Unified Structure Generation for Universal Information Extraction) - Lu et al.\n2. **InstructUIE** - instruction-tuned universal IE\n3. **GoLLIE** - Guideline-following Large Language Model for IE (likely ICLR 2024)\n4. **CodeIE** - code generation approach for IE\n5. **USM** or **UniRel** or other structured prediction + LLM approaches for IE\n6. Any 2024-2025 work on making LLMs output structured IE results (NER, RE, EE)\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format.",
    "agentId": "a88824f793ba94b4e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings for 6 representative papers on structural constraints for IE with LLMs (2022--2026):\n\n---\n\n**1. UIE -- Unified Structure Generation for Universal Information Extraction**\n- **Authors:** Yaojie Lu, Qing Liu, Dai Dai, et al.\n- **Venue:** ACL 2022\n- **ArXiv:** 2203.12277\n- **Method:** Defines a structured extraction language (SEL) to uniformly encode different IE output structures (entity, relation, event, sentiment). Uses a schema-based prompt mechanism (Structural Schema Instructor) with a large-scale pre-trained text-to-structure model to adaptively generate target structures. Achieves SOTA on 4 IE tasks across 13 datasets in supervised, low-resource, and few-shot settings.\n\n---\n\n**2. InstructUIE -- Multi-task Instruction Tuning for Unified Information Extraction**\n- **Authors:** Xiao Wang, Weikang Zhou, Can Zu, et al.\n- **Venue:** arXiv 2023 (2304.08085)\n- **ArXiv:** 2304.08085\n- **Method:** Builds IE INSTRUCTIONS, a benchmark of 32 diverse IE datasets in unified text-to-text format with expert-written instructions. Fine-tunes Flan-T5 on this benchmark, enabling a single model to handle NER, RE, EE, etc. via natural language instructions. Demonstrates that instruction-tuned smaller models can substantially outperform GPT-3.5 on IE tasks.\n\n---\n\n**3. GoLLIE -- Annotation Guidelines improve Zero-Shot Information-Extraction**\n- **Authors:** Oscar Sainz, Iker Garcia-Ferrero, Rodrigo Agerri, et al.\n- **Venue:** ICLR 2024\n- **ArXiv:** 2310.03668\n- **Method:** Fine-tunes Code-LLaMA to follow annotation guidelines expressed as Python class definitions (code-based schema representation). The model takes entity/relation/event type definitions as Python dataclasses and generates structured output as Python code. This code-based formulation enables strong zero-shot generalization to unseen IE schemas, outperforming previous zero-shot IE approaches.\n\n---\n\n**4. CodeIE -- Large Code Generation Models are Better Few-Shot Information Extractors**\n- **Authors:** Peng Li, Tianxiang Sun, Qiong Tang, et al.\n- **Venue:** ACL 2023\n- **ArXiv:** 2305.05711\n- **Method:** Recasts IE structured output as code rather than natural language and uses code-LLMs (e.g., Codex) with code-style prompts to perform NER and RE as code generation tasks. The code formulation naturally captures the structured nature of IE outputs. Consistently outperforms both fine-tuned IE-specific models (e.g., UIE) and NL-LLM prompting under few-shot settings.\n\n---\n\n**5. USM -- Universal Information Extraction as Unified Semantic Matching**\n- **Authors:** Jie Lou, Yaojie Lu, Dai Dai, et al.\n- **Venue:** AAAI 2023\n- **ArXiv:** 2301.03282\n- **Method:** Models IE as unified semantic matching via three token-linking operations that capture structuring (identifying spans/structures) and conceptualizing (mapping to schema types). Jointly encodes schema and input text, extracts substructures in parallel, and controllably decodes target structures on demand. Achieves SOTA on 4 IE tasks with strong zero/few-shot transfer ability.\n\n---\n\n**6. ADELIE -- Aligning Large Language Models on Information Extraction**\n- **Authors:** Yunjia Qi, Hao Peng, Xiaozhi Wang, et al. (THU-KEG)\n- **Venue:** EMNLP 2024\n- **ArXiv:** 2405.05008\n- **Method:** Constructs IEInstruct, a high-quality alignment corpus for IE, then trains LLMs with instruction tuning (SFT) followed by Direct Preference Optimization (DPO). Covers closed IE, open IE, and on-demand IE. ADELIE achieves SOTA among open-source models on diverse held-out IE benchmarks while preserving general LLM capabilities. Released in 1.5B/3B/7B sizes.\n\n---\n\n**Summary of the landscape:** These papers represent three main paradigms for structural constraints in LLM-based IE:\n- **Text-to-structure generation** (UIE, InstructUIE): Define a linearized structure language and train seq2seq models to generate it.\n- **Code-based schema representation** (GoLLIE, CodeIE): Leverage code LLMs and Python class/function definitions to naturally express IE schemas and structured outputs.\n- **Semantic matching / alignment** (USM, ADELIE): Frame IE as matching or align LLMs specifically for IE through curated data and preference optimization."
      }
    ],
    "totalDurationMs": 78939,
    "totalTokens": 27410,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3320,
      "cache_read_input_tokens": 22898,
      "output_tokens": 1191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3320
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1191,
          "cache_read_input_tokens": 22898,
          "cache_creation_input_tokens": 3320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3320,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 12
    }
  },
  "sourceToolAssistantUUID": "f6eda583-72d4-4d63-872f-3dd0a70cfffe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T02:37:08.035Z_

<details><summary>↩ Tool result · `toolu_01G6VBcaGt99gKykurE3Zfsz`</summary>

```text
Here are the findings, structured by paper:

---

## Paper 1: Let Me Speak Freely?

- **Full title:** Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models
- **Authors:** Zhi Rui Tam, Cheng-Kuang Wu, Yi-Lin Tsai, Chieh-Yen Lin, Hung-yi Lee, Yun-Nung Chen
- **Venue:** EMNLP 2024 Industry Track (not NeurIPS 2024 as initially assumed)
- **ArXiv ID:** 2408.02442
- **Core finding:** Structured format constraints (JSON, XML, YAML) cause significant decline in LLM reasoning abilities. Rigid formats hurt reasoning-heavy tasks (math, multi-hop QA) but help classification tasks (slot-filling, intent detection). Stricter format constraints generally lead to greater performance degradation.

---

## Paper 2: CRANE

- **Full title:** CRANE: Reasoning with Constrained LLM Generation
- **Authors:** Debangshu Banerjee, Tarun Suresh, Shubham Ugare, Sasa Misailovic, Gagandeep Singh
- **Venue:** ICML 2025 (PMLR 267) -- note: NOT NeurIPS 2024
- **ArXiv ID:** 2502.09061
- **Core finding:** Provides a theoretical explanation for why constraining LLM outputs to restrictive grammars (only allowing syntactically valid final answers) reduces reasoning capabilities. Proposes alternating between unconstrained generation (for reasoning/chain-of-thought) and constrained generation (for structured output), achieving up to 10 percentage points accuracy improvement on GSM-symbolic and FOLIO benchmarks.

---

## Paper 3: Grammar-Aligned Decoding (GAD)

- **Full title:** Grammar-Aligned Decoding
- **Authors:** Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, Loris D'Antoni
- **Venue:** NeurIPS 2024 (Main Conference)
- **ArXiv ID:** 2405.21047
- **Core finding:** Grammar-constrained decoding (GCD) techniques distort the LLM's distribution -- outputs are grammatically valid but appear with likelihoods disproportionate to the original LLM distribution, producing syntactically correct but semantically degraded outputs. Proposes ASAp (Adaptive Sampling with Approximate Expected Futures), a decoding algorithm that guarantees grammatical output while provably remaining unbiased with respect to the original LM distribution.

---

## Paper 4: Structure Snowballing

- **Full title:** From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection
- **Authors:** Hongxu Zhou (single author; Saarland University)
- **Venue:** arXiv preprint, April 2026 (no conference venue yet)
- **ArXiv ID:** 2604.06066
- **Core finding:** Identifies a new failure mode called "structure snowballing" -- when constrained decoding is applied to LLM self-correction/reflection, the cognitive load of satisfying strict formatting rules pushes the model into formatting traps rather than improving reasoning. Imposing structural constraints does not improve self-correction and exposes an "alignment tax" highlighting tension between structural granularity and internal model capacity.

---

## Paper 5: The Hidden Cost of Structure

- **Full title:** The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance
- **Authors:** Maximilian Schall, Gerard de Melo
- **Venue:** RANLP 2025 (Proceedings of the 15th International Conference on Recent Advances in Natural Language Processing), pp. 1074-1084, Varna, Bulgaria
- **ArXiv ID:** Not confirmed (available via ACL Anthology)
- **Core finding:** Comprehensive empirical study across 11 models and multiple benchmarks. Uncovers a fundamental divergence between base and instruction-tuned models under structural constraints. Despite guaranteeing format validity, constrained decoding often reduces semantic correctness on reasoning-intensive tasks, with documented performance degradation of 10-30% compared to unconstrained generation.

---

**Key correction:** The user's query assumed CRANE was a NeurIPS 2024 paper -- it is actually ICML 2025. The NeurIPS 2024 paper on constrained decoding quality is **Grammar-Aligned Decoding** (Paper 3 above). "Let Me Speak Freely" appeared at EMNLP 2024, not NeurIPS.

agentId: a28931f55692878b6 (use SendMessage with to: 'a28931f55692878b6' to continue this agent)
&lt;usage>total_tokens: 27404
tool_uses: 13
duration_ms: 77592&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33724b89-1514-4a21-b2e8-e809fdf54f7d",
  "isSidechain": false,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "type": "user",
  "uuid": "06289dfe-5c03-4a13-bd5b-d771a70b53b9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for representative papers on the quality concerns and negative effects of constrained decoding on LLM generation (2023-2026). I need 3-5 key papers covering:\n\n1. **CRANE** (NeurIPS 2024) - about how constrained decoding can degrade generation quality. Search for \"CRANE constrained decoding NeurIPS 2024\" or \"Let Me Speak Freely\"\n2. **Structure Snowballing** or any paper about how structured output constraints cause quality degradation\n3. Any empirical studies showing constrained decoding hurts LLM performance\n4. Papers proposing solutions to maintain quality under constraints\n5. \"Let Me Speak Freely\" paper if different from CRANE\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method/finding in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format.",
    "agentId": "a28931f55692878b6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings, structured by paper:\n\n---\n\n## Paper 1: Let Me Speak Freely?\n\n- **Full title:** Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\n- **Authors:** Zhi Rui Tam, Cheng-Kuang Wu, Yi-Lin Tsai, Chieh-Yen Lin, Hung-yi Lee, Yun-Nung Chen\n- **Venue:** EMNLP 2024 Industry Track (not NeurIPS 2024 as initially assumed)\n- **ArXiv ID:** 2408.02442\n- **Core finding:** Structured format constraints (JSON, XML, YAML) cause significant decline in LLM reasoning abilities. Rigid formats hurt reasoning-heavy tasks (math, multi-hop QA) but help classification tasks (slot-filling, intent detection). Stricter format constraints generally lead to greater performance degradation.\n\n---\n\n## Paper 2: CRANE\n\n- **Full title:** CRANE: Reasoning with Constrained LLM Generation\n- **Authors:** Debangshu Banerjee, Tarun Suresh, Shubham Ugare, Sasa Misailovic, Gagandeep Singh\n- **Venue:** ICML 2025 (PMLR 267) -- note: NOT NeurIPS 2024\n- **ArXiv ID:** 2502.09061\n- **Core finding:** Provides a theoretical explanation for why constraining LLM outputs to restrictive grammars (only allowing syntactically valid final answers) reduces reasoning capabilities. Proposes alternating between unconstrained generation (for reasoning/chain-of-thought) and constrained generation (for structured output), achieving up to 10 percentage points accuracy improvement on GSM-symbolic and FOLIO benchmarks.\n\n---\n\n## Paper 3: Grammar-Aligned Decoding (GAD)\n\n- **Full title:** Grammar-Aligned Decoding\n- **Authors:** Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, Loris D'Antoni\n- **Venue:** NeurIPS 2024 (Main Conference)\n- **ArXiv ID:** 2405.21047\n- **Core finding:** Grammar-constrained decoding (GCD) techniques distort the LLM's distribution -- outputs are grammatically valid but appear with likelihoods disproportionate to the original LLM distribution, producing syntactically correct but semantically degraded outputs. Proposes ASAp (Adaptive Sampling with Approximate Expected Futures), a decoding algorithm that guarantees grammatical output while provably remaining unbiased with respect to the original LM distribution.\n\n---\n\n## Paper 4: Structure Snowballing\n\n- **Full title:** From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection\n- **Authors:** Hongxu Zhou (single author; Saarland University)\n- **Venue:** arXiv preprint, April 2026 (no conference venue yet)\n- **ArXiv ID:** 2604.06066\n- **Core finding:** Identifies a new failure mode called \"structure snowballing\" -- when constrained decoding is applied to LLM self-correction/reflection, the cognitive load of satisfying strict formatting rules pushes the model into formatting traps rather than improving reasoning. Imposing structural constraints does not improve self-correction and exposes an \"alignment tax\" highlighting tension between structural granularity and internal model capacity.\n\n---\n\n## Paper 5: The Hidden Cost of Structure\n\n- **Full title:** The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\n- **Authors:** Maximilian Schall, Gerard de Melo\n- **Venue:** RANLP 2025 (Proceedings of the 15th International Conference on Recent Advances in Natural Language Processing), pp. 1074-1084, Varna, Bulgaria\n- **ArXiv ID:** Not confirmed (available via ACL Anthology)\n- **Core finding:** Comprehensive empirical study across 11 models and multiple benchmarks. Uncovers a fundamental divergence between base and instruction-tuned models under structural constraints. Despite guaranteeing format validity, constrained decoding often reduces semantic correctness on reasoning-intensive tasks, with documented performance degradation of 10-30% compared to unconstrained generation.\n\n---\n\n**Key correction:** The user's query assumed CRANE was a NeurIPS 2024 paper -- it is actually ICML 2025. The NeurIPS 2024 paper on constrained decoding quality is **Grammar-Aligned Decoding** (Paper 3 above). \"Let Me Speak Freely\" appeared at EMNLP 2024, not NeurIPS."
      }
    ],
    "totalDurationMs": 77592,
    "totalTokens": 27404,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 25378,
      "output_tokens": 1131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 894
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1131,
          "cache_read_input_tokens": 25378,
          "cache_creation_input_tokens": 894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 894,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 13
    }
  },
  "sourceToolAssistantUUID": "33724b89-1514-4a21-b2e8-e809fdf54f7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T02:37:26.854Z_

<details><summary>↩ Tool result · `toolu_01NScH3NoBdckpLKd2TLJxXN`</summary>

```text
Now let me save these findings as a structured report.

Here are the findings across the five categories:

---

## 1. LLM + ASP (Answer Set Programming) for Constraint Validation

### Paper 1a: Solver-in-the-Loop Framework
- **Title:** A Solver-in-the-Loop Framework for Improving LLMs on Answer Set Programming for Logic Puzzle Solving
- **Authors:** Timo Pierre Schrader, Lukas Lange, Tobias Kaminski, Simon Razniewski, Annemarie Friedrich
- **Venue:** AAAI 2026 (Proceedings of the AAAI Conference on Artificial Intelligence, 40(30), pp. 25226-25234)
- **ArXiv:** 2512.17093 (December 2025)
- **Core method:** Introduces an ASP-solver-in-the-loop approach where LLM-generated ASP encodings are automatically evaluated by an ASP solver; solver feedback categorizes outputs as chosen/rejected for supervised fine-tuning, combined with solver-guided best-of-N sampling at inference time.

### Paper 1b: LLASP
- **Title:** LLASP: Fine-tuning Large Language Models for Answer Set Programming
- **Authors:** Erica Coppolillo, Francesco Calimeri, Giuseppe Manco, Simona Perri, Francesco Ricca
- **Venue:** KR 2024 (21st International Conference on Principles of Knowledge Representation and Reasoning), pp. 834-844
- **ArXiv:** 2407.18723
- **Core method:** Fine-tunes a lightweight LLM on a curated dataset of diverse ASP program patterns; demonstrates that this domain-specific fine-tuning outperforms much larger general-purpose LLMs in generating semantically correct ASP programs.

---

## 2. Ontology-Guided NER

### Paper 2: Ontology-Conformal NER for Materials
- **Title:** Ontology-conformal recognition of materials entities using language models
- **Authors:** Sai Teja Potu, Rachana Niranjan Murthy, Akhil Thomas, Lokesh Mishra, et al.
- **Venue:** Scientific Reports, volume 15, Article 18597 (May 2025)
- **DOI:** 10.1038/s41598-025-03619-y
- **Core method:** Evaluates foundation LLMs vs. domain-specific pre-trained models on ontology-conformal NER in materials science, where entity labels must map directly to a pre-existing domain ontology. Proposes a two-stage prompting strategy for GPT-4 that achieves competitive F1 despite limited demonstrations, while domain-specific models significantly outperform general models on fine-grained ontology-constrained labels.

---

## 3. Post-hoc Validation of LLM Outputs

### Paper 3: Can LLMs be Knowledge Graph Curators?
- **Title:** Can LLMs be Knowledge Graph Curators for Validating Triple Insertions?
- **Authors:** Andre Gomes Regino, Julio Cesar dos Reis
- **Venue:** GenAIK Workshop 2025 (Workshop on Generative AI and Knowledge Graphs), pp. 87-99, Abu Dhabi
- **Available at:** ACL Anthology (aclanthology.org/2025.genaik-1.10/)
- **Core method:** Proposes a systematic prompt-based validation pipeline that guides LLMs through staged evaluation of RDF triple insertions against existing KG structure, testing domain/range consistency and semantic coherence. Finds that larger models (Llama-3-70B-Instruct) offer superior accuracy but highlights challenges in domain generalization and semantic drift.

---

## 4. Type-Constrained Relation Extraction

### Paper 4a: ETCGN
- **Title:** ETCGN: Entity Type-Constrained Graph Networks for Document-Level Relation Extraction
- **Authors:** Yang H., Chen C., Zhang S., et al.
- **Venue:** International Journal of Machine Learning and Cybernetics, volume 15, pp. 5949-5962 (2024)
- **Core method:** Constructs a graph structure capturing mention interactions within documents, then applies entity type constraints to confine the scope of possible relations for each entity pair. Uses path-based reasoning with type-constrained edges to achieve state-of-the-art on DocRED and HacRED benchmarks.

### Paper 4b: EnriCo
- **Title:** EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction
- **Authors:** Urchade Zaratiana, Nadi Tomeh, Yann Dauxais, Pierre Holat, Thierry Charnois
- **Venue:** arXiv preprint (2024)
- **ArXiv:** 2404.12493
- **Core method:** Introduces attention-based enriched representations for joint entity and relation extraction, combined with a suite of constrained decoding algorithms that enforce task-specific structural constraints (e.g., entity type compatibility for relations) during inference, promoting coherent outputs.

---

## 5. Domain/Range Constraints from Ontologies for IE Validation

### Paper 5a: ODKE+
- **Title:** ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs
- **Authors:** Samira Khorshidi, Azadeh Nikfarjam, Suprita Shankar, Yisi Sang, et al. (Apple)
- **Venue:** arXiv preprint (September 2025)
- **ArXiv:** 2509.04696
- **Core method:** A production-grade system that dynamically generates ontology snippets (including domain/range constraints) tailored to each entity type, then uses these to align LLM extractions with schema constraints. Processes 9M+ Wikipedia pages, ingesting 19M facts at 98.8% precision across 195 predicates.

### Paper 5b: Open IE with Entity Focused Constraints
- **Title:** Open Information Extraction with Entity Focused Constraints
- **Authors:** Prajna Upadhyay, Oana Balalau, Ioana Manolescu
- **Venue:** Findings of EACL 2023, Dubrovnik, Croatia
- **Available at:** ACL Anthology (aclanthology.org/2023.findings-eacl.95/)
- **Core method:** Injects entity-type knowledge as constraints into Open IE via two mechanisms: constrained inference (at decoding time) and constraint-aware training. Built on OpenIE6, achieves 29.17% F1 improvement on CaRB and 24.37% on WIRe57 benchmarks.

---

**Summary of coverage:**
- **LLM+ASP:** Two papers (AAAI 2026, KR 2024) showing solver-in-the-loop and fine-tuning approaches for neuro-symbolic constraint enforcement
- **Ontology-guided NER:** One paper (Scientific Reports 2025) directly addressing ontology-conformal entity recognition
- **Post-hoc validation:** One paper (GenAIK 2025) on LLM-based RDF triple validation against KG schemas
- **Type-constrained RE:** Two papers (IJMLC 2024, arXiv 2024) on entity type constraints in document-level and joint extraction
- **Domain/range ontology constraints:** Two papers (arXiv 2025 from Apple, Findings of EACL 2023) on ontology-guided extraction with schema constraint enforcement

agentId: afdd0236fb2ec259a (use SendMessage with to: 'afdd0236fb2ec259a' to continue this agent)
&lt;usage>total_tokens: 33192
tool_uses: 17
duration_ms: 100792&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f095d071-d395-4e6f-8cd1-782aedecbb6a",
  "isSidechain": false,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "type": "user",
  "uuid": "32bb3a7f-bbeb-4ff5-ad8e-e15e0c2fdb2c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for representative papers on type-checking, ontology validation, and ontology-guided constraints in NLP (2020-2026). I need 4-5 key papers covering:\n\n1. **LLM+ASP** approaches - using Answer Set Programming to validate/constrain LLM outputs (check ICLP 2025 or similar logic programming venues)\n2. **Ontology-guided NER** - using ontological knowledge to guide named entity recognition\n3. **Post-hoc validation** approaches for LLM outputs against knowledge bases or ontologies\n4. **Type-constrained relation extraction** - enforcing entity type constraints in RE\n5. Any work on using domain/range constraints from ontologies to validate IE outputs\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format.",
    "agentId": "afdd0236fb2ec259a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now let me save these findings as a structured report.\n\nHere are the findings across the five categories:\n\n---\n\n## 1. LLM + ASP (Answer Set Programming) for Constraint Validation\n\n### Paper 1a: Solver-in-the-Loop Framework\n- **Title:** A Solver-in-the-Loop Framework for Improving LLMs on Answer Set Programming for Logic Puzzle Solving\n- **Authors:** Timo Pierre Schrader, Lukas Lange, Tobias Kaminski, Simon Razniewski, Annemarie Friedrich\n- **Venue:** AAAI 2026 (Proceedings of the AAAI Conference on Artificial Intelligence, 40(30), pp. 25226-25234)\n- **ArXiv:** 2512.17093 (December 2025)\n- **Core method:** Introduces an ASP-solver-in-the-loop approach where LLM-generated ASP encodings are automatically evaluated by an ASP solver; solver feedback categorizes outputs as chosen/rejected for supervised fine-tuning, combined with solver-guided best-of-N sampling at inference time.\n\n### Paper 1b: LLASP\n- **Title:** LLASP: Fine-tuning Large Language Models for Answer Set Programming\n- **Authors:** Erica Coppolillo, Francesco Calimeri, Giuseppe Manco, Simona Perri, Francesco Ricca\n- **Venue:** KR 2024 (21st International Conference on Principles of Knowledge Representation and Reasoning), pp. 834-844\n- **ArXiv:** 2407.18723\n- **Core method:** Fine-tunes a lightweight LLM on a curated dataset of diverse ASP program patterns; demonstrates that this domain-specific fine-tuning outperforms much larger general-purpose LLMs in generating semantically correct ASP programs.\n\n---\n\n## 2. Ontology-Guided NER\n\n### Paper 2: Ontology-Conformal NER for Materials\n- **Title:** Ontology-conformal recognition of materials entities using language models\n- **Authors:** Sai Teja Potu, Rachana Niranjan Murthy, Akhil Thomas, Lokesh Mishra, et al.\n- **Venue:** Scientific Reports, volume 15, Article 18597 (May 2025)\n- **DOI:** 10.1038/s41598-025-03619-y\n- **Core method:** Evaluates foundation LLMs vs. domain-specific pre-trained models on ontology-conformal NER in materials science, where entity labels must map directly to a pre-existing domain ontology. Proposes a two-stage prompting strategy for GPT-4 that achieves competitive F1 despite limited demonstrations, while domain-specific models significantly outperform general models on fine-grained ontology-constrained labels.\n\n---\n\n## 3. Post-hoc Validation of LLM Outputs\n\n### Paper 3: Can LLMs be Knowledge Graph Curators?\n- **Title:** Can LLMs be Knowledge Graph Curators for Validating Triple Insertions?\n- **Authors:** Andre Gomes Regino, Julio Cesar dos Reis\n- **Venue:** GenAIK Workshop 2025 (Workshop on Generative AI and Knowledge Graphs), pp. 87-99, Abu Dhabi\n- **Available at:** ACL Anthology (aclanthology.org/2025.genaik-1.10/)\n- **Core method:** Proposes a systematic prompt-based validation pipeline that guides LLMs through staged evaluation of RDF triple insertions against existing KG structure, testing domain/range consistency and semantic coherence. Finds that larger models (Llama-3-70B-Instruct) offer superior accuracy but highlights challenges in domain generalization and semantic drift.\n\n---\n\n## 4. Type-Constrained Relation Extraction\n\n### Paper 4a: ETCGN\n- **Title:** ETCGN: Entity Type-Constrained Graph Networks for Document-Level Relation Extraction\n- **Authors:** Yang H., Chen C., Zhang S., et al.\n- **Venue:** International Journal of Machine Learning and Cybernetics, volume 15, pp. 5949-5962 (2024)\n- **Core method:** Constructs a graph structure capturing mention interactions within documents, then applies entity type constraints to confine the scope of possible relations for each entity pair. Uses path-based reasoning with type-constrained edges to achieve state-of-the-art on DocRED and HacRED benchmarks.\n\n### Paper 4b: EnriCo\n- **Title:** EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction\n- **Authors:** Urchade Zaratiana, Nadi Tomeh, Yann Dauxais, Pierre Holat, Thierry Charnois\n- **Venue:** arXiv preprint (2024)\n- **ArXiv:** 2404.12493\n- **Core method:** Introduces attention-based enriched representations for joint entity and relation extraction, combined with a suite of constrained decoding algorithms that enforce task-specific structural constraints (e.g., entity type compatibility for relations) during inference, promoting coherent outputs.\n\n---\n\n## 5. Domain/Range Constraints from Ontologies for IE Validation\n\n### Paper 5a: ODKE+\n- **Title:** ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs\n- **Authors:** Samira Khorshidi, Azadeh Nikfarjam, Suprita Shankar, Yisi Sang, et al. (Apple)\n- **Venue:** arXiv preprint (September 2025)\n- **ArXiv:** 2509.04696\n- **Core method:** A production-grade system that dynamically generates ontology snippets (including domain/range constraints) tailored to each entity type, then uses these to align LLM extractions with schema constraints. Processes 9M+ Wikipedia pages, ingesting 19M facts at 98.8% precision across 195 predicates.\n\n### Paper 5b: Open IE with Entity Focused Constraints\n- **Title:** Open Information Extraction with Entity Focused Constraints\n- **Authors:** Prajna Upadhyay, Oana Balalau, Ioana Manolescu\n- **Venue:** Findings of EACL 2023, Dubrovnik, Croatia\n- **Available at:** ACL Anthology (aclanthology.org/2023.findings-eacl.95/)\n- **Core method:** Injects entity-type knowledge as constraints into Open IE via two mechanisms: constrained inference (at decoding time) and constraint-aware training. Built on OpenIE6, achieves 29.17% F1 improvement on CaRB and 24.37% on WIRe57 benchmarks.\n\n---\n\n**Summary of coverage:**\n- **LLM+ASP:** Two papers (AAAI 2026, KR 2024) showing solver-in-the-loop and fine-tuning approaches for neuro-symbolic constraint enforcement\n- **Ontology-guided NER:** One paper (Scientific Reports 2025) directly addressing ontology-conformal entity recognition\n- **Post-hoc validation:** One paper (GenAIK 2025) on LLM-based RDF triple validation against KG schemas\n- **Type-constrained RE:** Two papers (IJMLC 2024, arXiv 2024) on entity type constraints in document-level and joint extraction\n- **Domain/range ontology constraints:** Two papers (arXiv 2025 from Apple, Findings of EACL 2023) on ontology-guided extraction with schema constraint enforcement"
      }
    ],
    "totalDurationMs": 100792,
    "totalTokens": 33192,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1805,
      "cache_read_input_tokens": 29551,
      "output_tokens": 1835,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1805
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1835,
          "cache_read_input_tokens": 29551,
          "cache_creation_input_tokens": 1805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1805,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 17
    }
  },
  "sourceToolAssistantUUID": "f095d071-d395-4e6f-8cd1-782aedecbb6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "leafUuid": "32bb3a7f-bbeb-4ff5-ad8e-e15e0c2fdb2c",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey for OntoCoDec related work",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909"
}
```

---

### Tool result

_source line 22 · 2026-05-14T02:37:29.416Z_

<details><summary>↩ Tool result · `toolu_015diNCrEvx5fpG7XJTAoxzF`</summary>

```text
Here are the findings, structured by paper.

---

## 1. XGrammar

- **Full title:** XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models
- **Authors:** Yixin Dong, Charlie F. Ruan, Yaxing Cai, Ruihang Lai, Ziyi Xu, Yilong Zhao, Tianqi Chen
- **Venue:** MLSys 2025
- **ArXiv:** [2411.15100](https://arxiv.org/abs/2411.15100) (Nov 2024)
- **Core method:** Divides the vocabulary into context-independent tokens (pre-checkable offline) and context-dependent tokens (checked at runtime), combined with persistent stack-based pushdown automata for efficient CFG constraint enforcement. Achieves up to 100x speedup over prior grammar-constrained decoding approaches.
- **Note:** A follow-up, XGrammar-2 (arXiv [2601.04426](https://arxiv.org/html/2601.04426)), extends to dynamic structured generation for agentic LLMs.

---

## 2. Guidance / Domino (Microsoft / ETH Zurich)

Microsoft's **Guidance** library ([github.com/guidance-ai/guidance](https://github.com/guidance-ai/guidance)) is an open-source framework but does not have a standalone academic paper. The closest peer-reviewed work by the same research group is:

- **Full title:** Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation
- **Authors:** Luca Beurer-Kellner, Marc Fischer, Martin Vechev
- **Venue:** ICML 2024
- **ArXiv:** [2403.06988](https://arxiv.org/abs/2403.06988) (Mar 2024)
- **Core method:** Proposes the DOMINO algorithm for non-invasive constrained decoding that enforces CFG constraints while minimally distorting the LLM's original distribution. Leverages pre-computation and speculative decoding, achieving throughput that can even exceed unconstrained generation.

---

## 3. Outlines

- **Full title:** Efficient Guided Generation for Large Language Models
- **Authors:** Brandon T. Willard, Remi Louf
- **Venue:** arXiv preprint (no confirmed top-venue publication; widely cited)
- **ArXiv:** [2307.09702](https://arxiv.org/abs/2307.09702) (Jul 2023, updated 2024)
- **Core method:** Reformulates constrained text generation as transitions in a finite-state machine (FSM). Builds an offline index over the vocabulary for each FSM state, enabling O(1) amortized per-token constraint checking for regular expressions. Extends to context-free grammars via LALR(1) parsers. Implemented in the open-source Outlines library.

---

## 4. LMQL

- **Full title:** Prompting Is Programming: A Query Language for Large Language Models
- **Authors:** Luca Beurer-Kellner, Marc Fischer, Martin Vechev
- **Venue:** PLDI 2023 (ACM SIGPLAN Conference on Programming Language Design and Implementation)
- **ArXiv:** [2212.06094](https://arxiv.org/abs/2212.06094) (Dec 2022)
- **Core method:** Introduces LMQL, a SQL-like query language for LLMs where users combine natural language prompts with programmatic control flow and declarative constraints (type, length, regex, stopping conditions). The LMQL runtime compiles these constraints into an efficient token-level masking procedure, reducing API costs by 26-85% while maintaining or improving accuracy.

---

## 5. SGLang

- **Full title:** SGLang: Efficient Execution of Structured Language Model Programs
- **Authors:** Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie, Chuyue Sun, Jeff Huang, Cody Hao Yu, Shiyi Cao, Christos Kozyrakis, Ion Stoica, Joseph E. Gonzalez, Clark Barrett, Ying Sheng
- **Venue:** NeurIPS 2024
- **ArXiv:** [2312.07104](https://arxiv.org/abs/2312.07104) (Dec 2023)
- **Core method:** A domain-specific language embedded in Python with a co-designed runtime. Key innovations include RadixAttention for KV cache reuse across structured program branches and compressed finite state machines for faster structured output decoding. Achieves up to 6.4x higher throughput than SOTA inference systems on structured generation tasks.

---

## 6. Grammar-Aligned Decoding (bonus notable paper)

- **Full title:** Grammar-Aligned Decoding
- **Authors:** Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, Loris D'Antoni
- **Venue:** NeurIPS 2024
- **ArXiv:** [2405.21047](https://arxiv.org/abs/2405.21047) (May 2024)
- **Core method:** Proposes ASAp (Adaptive Sampling with Approximate expected futures), a decoding algorithm that enforces grammar constraints while provably preserving the LLM's conditional distribution given the grammar, addressing the distribution distortion problem in naive token masking.

---

## Survey / Benchmark Papers

**JSONSchemaBench (Benchmark, 2025)**
- **Full title:** JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models
- **Authors:** Saibo Geng, Hudson Cooper, Michal Moskal, Samuel Jenkins, Julian Berman, Nathan Ranchin, Robert West, Eric Horvitz, Harsha Nori
- **ArXiv:** [2501.10868](https://arxiv.org/abs/2501.10868) (Jan 2025)
- **Summary:** Benchmark of 10K real-world JSON schemas evaluating six constrained decoding frameworks (Guidance, Outlines, Llamacpp, XGrammar, OpenAI, Gemini) across efficiency, coverage, and output quality.

**Controllable Text Generation Survey (2024)**
- **Full title:** Controllable Text Generation for Large Language Models: A Survey
- **Authors:** Xun Liang, Hanyu Wang, Yezhaohui Wang, Shichao Song, et al.
- **ArXiv:** [2408.12599](https://arxiv.org/abs/2408.12599) (Aug 2024)
- **Summary:** Broad survey categorizing CTG into content control and attribute control, covering methods from fine-tuning to decoding-time intervention including constrained decoding.

**GUARD (ICLR 2025)**
- **Full title:** Guaranteed Generation from Large Language Models
- **Authors:** (see paper)
- **Venue:** ICLR 2025
- **ArXiv:** [2410.06716](https://arxiv.org/abs/2410.06716)
- **Summary:** Defines the ideal constrained distribution as the closest to the original LLM satisfying constraints, proves autoregressive training alone cannot reach it, and proposes GUARD combining training-time and inference-time methods with rejection sampling.

**Awesome-LLM-Constrained-Decoding** (curated list): [github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding](https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding) -- comprehensive repository tracking all papers in this space.

---

Notable observation: Beurer-Kellner, Fischer, and Vechev (ETH Zurich) authored both LMQL (PLDI 2023) and Domino/Guidance (ICML 2024), making them a central group in this area. The SGLang system (NeurIPS 2024) now integrates XGrammar (MLSys 2025) as its grammar engine, forming the current highest-performance open-source stack for grammar-constrained serving.

agentId: ab33888ae5255d2f0 (use SendMessage with to: 'ab33888ae5255d2f0' to continue this agent)
&lt;usage>total_tokens: 33439
tool_uses: 18
duration_ms: 116709&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f8a8a4e-4c09-4d69-942b-864b618a53bd",
  "isSidechain": false,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "type": "user",
  "uuid": "86664e44-3e85-426d-85d2-727116b2768a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for representative papers on grammar-constrained decoding for LLMs (2023-2026). I need 4-5 key papers covering:\n\n1. **XGrammar** - the system for grammar-guided structured generation (likely from MLSys or similar venue)\n2. **Guidance** (Microsoft) - constrained generation framework\n3. **Outlines** (2024) - structured text generation with regular expressions/CFGs\n4. **LMQL** - query language for LLMs with constraints\n5. **SGLang** or other notable grammar-constrained decoding systems\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nAlso search for any survey papers on constrained decoding for LLMs (2024-2026).\n\nReport all findings in a structured format.",
    "agentId": "ab33888ae5255d2f0",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings, structured by paper.\n\n---\n\n## 1. XGrammar\n\n- **Full title:** XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models\n- **Authors:** Yixin Dong, Charlie F. Ruan, Yaxing Cai, Ruihang Lai, Ziyi Xu, Yilong Zhao, Tianqi Chen\n- **Venue:** MLSys 2025\n- **ArXiv:** [2411.15100](https://arxiv.org/abs/2411.15100) (Nov 2024)\n- **Core method:** Divides the vocabulary into context-independent tokens (pre-checkable offline) and context-dependent tokens (checked at runtime), combined with persistent stack-based pushdown automata for efficient CFG constraint enforcement. Achieves up to 100x speedup over prior grammar-constrained decoding approaches.\n- **Note:** A follow-up, XGrammar-2 (arXiv [2601.04426](https://arxiv.org/html/2601.04426)), extends to dynamic structured generation for agentic LLMs.\n\n---\n\n## 2. Guidance / Domino (Microsoft / ETH Zurich)\n\nMicrosoft's **Guidance** library ([github.com/guidance-ai/guidance](https://github.com/guidance-ai/guidance)) is an open-source framework but does not have a standalone academic paper. The closest peer-reviewed work by the same research group is:\n\n- **Full title:** Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation\n- **Authors:** Luca Beurer-Kellner, Marc Fischer, Martin Vechev\n- **Venue:** ICML 2024\n- **ArXiv:** [2403.06988](https://arxiv.org/abs/2403.06988) (Mar 2024)\n- **Core method:** Proposes the DOMINO algorithm for non-invasive constrained decoding that enforces CFG constraints while minimally distorting the LLM's original distribution. Leverages pre-computation and speculative decoding, achieving throughput that can even exceed unconstrained generation.\n\n---\n\n## 3. Outlines\n\n- **Full title:** Efficient Guided Generation for Large Language Models\n- **Authors:** Brandon T. Willard, Remi Louf\n- **Venue:** arXiv preprint (no confirmed top-venue publication; widely cited)\n- **ArXiv:** [2307.09702](https://arxiv.org/abs/2307.09702) (Jul 2023, updated 2024)\n- **Core method:** Reformulates constrained text generation as transitions in a finite-state machine (FSM). Builds an offline index over the vocabulary for each FSM state, enabling O(1) amortized per-token constraint checking for regular expressions. Extends to context-free grammars via LALR(1) parsers. Implemented in the open-source Outlines library.\n\n---\n\n## 4. LMQL\n\n- **Full title:** Prompting Is Programming: A Query Language for Large Language Models\n- **Authors:** Luca Beurer-Kellner, Marc Fischer, Martin Vechev\n- **Venue:** PLDI 2023 (ACM SIGPLAN Conference on Programming Language Design and Implementation)\n- **ArXiv:** [2212.06094](https://arxiv.org/abs/2212.06094) (Dec 2022)\n- **Core method:** Introduces LMQL, a SQL-like query language for LLMs where users combine natural language prompts with programmatic control flow and declarative constraints (type, length, regex, stopping conditions). The LMQL runtime compiles these constraints into an efficient token-level masking procedure, reducing API costs by 26-85% while maintaining or improving accuracy.\n\n---\n\n## 5. SGLang\n\n- **Full title:** SGLang: Efficient Execution of Structured Language Model Programs\n- **Authors:** Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie, Chuyue Sun, Jeff Huang, Cody Hao Yu, Shiyi Cao, Christos Kozyrakis, Ion Stoica, Joseph E. Gonzalez, Clark Barrett, Ying Sheng\n- **Venue:** NeurIPS 2024\n- **ArXiv:** [2312.07104](https://arxiv.org/abs/2312.07104) (Dec 2023)\n- **Core method:** A domain-specific language embedded in Python with a co-designed runtime. Key innovations include RadixAttention for KV cache reuse across structured program branches and compressed finite state machines for faster structured output decoding. Achieves up to 6.4x higher throughput than SOTA inference systems on structured generation tasks.\n\n---\n\n## 6. Grammar-Aligned Decoding (bonus notable paper)\n\n- **Full title:** Grammar-Aligned Decoding\n- **Authors:** Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, Loris D'Antoni\n- **Venue:** NeurIPS 2024\n- **ArXiv:** [2405.21047](https://arxiv.org/abs/2405.21047) (May 2024)\n- **Core method:** Proposes ASAp (Adaptive Sampling with Approximate expected futures), a decoding algorithm that enforces grammar constraints while provably preserving the LLM's conditional distribution given the grammar, addressing the distribution distortion problem in naive token masking.\n\n---\n\n## Survey / Benchmark Papers\n\n**JSONSchemaBench (Benchmark, 2025)**\n- **Full title:** JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\n- **Authors:** Saibo Geng, Hudson Cooper, Michal Moskal, Samuel Jenkins, Julian Berman, Nathan Ranchin, Robert West, Eric Horvitz, Harsha Nori\n- **ArXiv:** [2501.10868](https://arxiv.org/abs/2501.10868) (Jan 2025)\n- **Summary:** Benchmark of 10K real-world JSON schemas evaluating six constrained decoding frameworks (Guidance, Outlines, Llamacpp, XGrammar, OpenAI, Gemini) across efficiency, coverage, and output quality.\n\n**Controllable Text Generation Survey (2024)**\n- **Full title:** Controllable Text Generation for Large Language Models: A Survey\n- **Authors:** Xun Liang, Hanyu Wang, Yezhaohui Wang, Shichao Song, et al.\n- **ArXiv:** [2408.12599](https://arxiv.org/abs/2408.12599) (Aug 2024)\n- **Summary:** Broad survey categorizing CTG into content control and attribute control, covering methods from fine-tuning to decoding-time intervention including constrained decoding.\n\n**GUARD (ICLR 2025)**\n- **Full title:** Guaranteed Generation from Large Language Models\n- **Authors:** (see paper)\n- **Venue:** ICLR 2025\n- **ArXiv:** [2410.06716](https://arxiv.org/abs/2410.06716)\n- **Summary:** Defines the ideal constrained distribution as the closest to the original LLM satisfying constraints, proves autoregressive training alone cannot reach it, and proposes GUARD combining training-time and inference-time methods with rejection sampling.\n\n**Awesome-LLM-Constrained-Decoding** (curated list): [github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding](https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding) -- comprehensive repository tracking all papers in this space.\n\n---\n\nNotable observation: Beurer-Kellner, Fischer, and Vechev (ETH Zurich) authored both LMQL (PLDI 2023) and Domino/Guidance (ICML 2024), making them a central group in this area. The SGLang system (NeurIPS 2024) now integrates XGrammar (MLSys 2025) as its grammar engine, forming the current highest-performance open-source stack for grammar-constrained serving."
      }
    ],
    "totalDurationMs": 116709,
    "totalTokens": 33439,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2025,
      "cache_read_input_tokens": 29429,
      "output_tokens": 1984,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2025
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1984,
          "cache_read_input_tokens": 29429,
          "cache_creation_input_tokens": 2025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2025,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 18
    }
  },
  "sourceToolAssistantUUID": "5f8a8a4e-4c09-4d69-942b-864b618a53bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T02:37:32.479Z_

<details><summary>Logged reasoning block</summary>

```text
I now have comprehensive findings from all 5 agents. Let me compile these into the survey document. Let me also check the existing project artifacts directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86664e44-3e85-426d-85d2-727116b2768a",
  "isSidechain": false,
  "requestId": "req_011Cb1geVjhnvGYXivyfPGMz",
  "type": "assistant",
  "uuid": "646c9fdd-f247-4e83-8055-0c797ea9be6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrDhF9vLApHSDh5jE2tryd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6009,
      "cache_creation_input_tokens": 3647,
      "cache_read_input_tokens": 23525,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6009,
          "output_tokens": 181,
          "cache_read_input_tokens": 23525,
          "cache_creation_input_tokens": 3647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3647
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

_source line 24 · 2026-05-14T02:37:32.968Z_

调研完成，开始整理产出文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "646c9fdd-f247-4e83-8055-0c797ea9be6f",
  "isSidechain": false,
  "requestId": "req_011Cb1geVjhnvGYXivyfPGMz",
  "type": "assistant",
  "uuid": "906739aa-a040-48ad-998e-c21ff2b295ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrDhF9vLApHSDh5jE2tryd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6009,
      "cache_creation_input_tokens": 3647,
      "cache_read_input_tokens": 23525,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6009,
          "output_tokens": 181,
          "cache_read_input_tokens": 23525,
          "cache_creation_input_tokens": 3647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3647
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

_source line 25 · 2026-05-14T02:37:34.966Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JHkd7n1mvtM7BCGVYDMMGW`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ 2>/dev/null || echo \"DIR_NOT_EXIST\"",
  "description": "Check artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "906739aa-a040-48ad-998e-c21ff2b295ad",
  "isSidechain": false,
  "requestId": "req_011Cb1geVjhnvGYXivyfPGMz",
  "type": "assistant",
  "uuid": "7f87c23f-64c2-4934-8662-9384dd883aec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrDhF9vLApHSDh5jE2tryd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6009,
      "cache_creation_input_tokens": 3647,
      "cache_read_input_tokens": 23525,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6009,
          "output_tokens": 181,
          "cache_read_input_tokens": 23525,
          "cache_creation_input_tokens": 3647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3647
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

_source line 26 · 2026-05-14T02:37:35.134Z_

<details><summary>↩ Tool result · `toolu_01JHkd7n1mvtM7BCGVYDMMGW`</summary>

```text
_project
analyze_ontology_docred.py
compare_prompts.py
literature_map.yaml
literature_survey_constrained_decoding_ie.md
literature_survey_ontology_constrained_ie.md
manifest.yaml
paper_results_summary.md
run_constrained_extraction.py
run_extraction_docred.py
violation_checker_docred.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f87c23f-64c2-4934-8662-9384dd883aec",
  "isSidechain": false,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "type": "user",
  "uuid": "0cd9b12c-c936-459d-bd86-60d74346f547",
  "toolUseResult": {
    "stdout": "_project\nanalyze_ontology_docred.py\ncompare_prompts.py\nliterature_map.yaml\nliterature_survey_constrained_decoding_ie.md\nliterature_survey_ontology_constrained_ie.md\nmanifest.yaml\npaper_results_summary.md\nrun_constrained_extraction.py\nrun_extraction_docred.py\nviolation_checker_docred.py",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7f87c23f-64c2-4934-8662-9384dd883aec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T02:40:05.874Z_

<details open><summary>🔧 Tool call — Write · `toolu_01HAim65d5696zZYLFtijTKY`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/related_work_survey.md",
  "content": "# OntoCoDec Related Work Survey\n\n## 1. Grammar-Constrained Decoding\n\n### XGrammar | MLSys 2025\n- **Title:** XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models\n- **Authors:** Dong et al.\n- **核心方法:** 将词表划分为 context-independent（离线预检）和 context-dependent（运行时检查）两类 token，结合 persistent stack-based pushdown automata 高效执行 CFG 约束，比先前方法快 100x。\n- **与 OntoCoDec 的关系:** OntoCoDec 的 Grammar 层直接基于 XGrammar 实现 JSON schema + enum 约束，消除 RV/ET violations。XGrammar 提供格式正确性保证，但不处理语义层约束（domain/range），这正是 OntoCoDec Semantic 层的贡献。\n- **BibTeX key:** `dong2025xgrammar`\n- **ArXiv:** 2411.15100\n\n### Outlines | arXiv 2023\n- **Title:** Efficient Guided Generation for Large Language Models\n- **Authors:** Willard & Louf\n- **核心方法:** 将受约束文本生成重构为有限状态机（FSM）中的状态转移，为每个 FSM 状态离线构建词表索引，实现正则表达式约束的 O(1) 均摊 per-token 检查，扩展至 LALR(1) parser 支持 CFG。\n- **与 OntoCoDec 的关系:** Outlines 是 grammar-constrained decoding 的开源先驱之一，与 XGrammar 属同一技术路线。OntoCoDec 选择 XGrammar 而非 Outlines 是因为其更高效的 vocabulary 预处理和对 LLM serving 框架（vLLM/SGLang）的原生集成。\n- **BibTeX key:** `willard2023outlines`\n- **ArXiv:** 2307.09702\n\n### LMQL | PLDI 2023\n- **Title:** Prompting Is Programming: A Query Language for Large Language Models\n- **Authors:** Beurer-Kellner, Fischer & Vechev\n- **核心方法:** SQL 风格的 LLM 查询语言，将自然语言 prompt 与程序控制流和声明式约束（类型、长度、正则、停止条件）结合，运行时编译为 token-level masking，减少 26-85% API 成本。\n- **与 OntoCoDec 的关系:** LMQL 提供通用的声明式约束框架，但约束表达能力限于格式层面（类型、长度、正则）。OntoCoDec 的 Semantic 层引入了 IE 任务特有的 domain/range 本体约束，超越了通用格式约束的范畴。\n- **BibTeX key:** `beurer-kellner2023lmql`\n- **ArXiv:** 2212.06094\n\n### DOMINO | ICML 2024\n- **Title:** Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation\n- **Authors:** Beurer-Kellner, Fischer & Vechev\n- **核心方法:** 提出 non-invasive constrained decoding 算法，在执行 CFG 约束的同时最小化对 LLM 原始分布的扭曲，利用预计算和 speculative decoding 实现甚至超过无约束生成的吞吐。\n- **与 OntoCoDec 的关系:** DOMINO 关注 distribution distortion 问题——约束解码如何改变 LLM 的 token 分布。OntoCoDec 的 F1 无损结果从实验角度呼应了这一方向：精心设计的约束不必牺牲生成质量。\n- **BibTeX key:** `beurer-kellner2024domino`\n- **ArXiv:** 2403.06988\n\n### Grammar-Aligned Decoding (ASAp) | NeurIPS 2024\n- **Title:** Grammar-Aligned Decoding\n- **Authors:** Park, Wang, Berg-Kirkpatrick, Polikarpova & D'Antoni\n- **核心方法:** 证明 naive token masking 会扭曲 LLM 的条件分布，提出 ASAp（Adaptive Sampling with Approximate expected futures）算法，在保证语法正确性的同时保持对原始 LM 分布的无偏性。\n- **与 OntoCoDec 的关系:** ASAp 解决的是 grammar-constrained decoding 的理论正确性问题。OntoCoDec 的 logits masking 也面临类似的分布扭曲风险，但实验证明在 IE 任务上 F1 无损，说明 IE 场景中合法约束的 masking 影响有限。\n- **BibTeX key:** `park2024grammar`\n- **ArXiv:** 2405.21047\n\n---\n\n## 2. Vocabulary/Type-Constrained Generation\n\n### GENRE | ICLR 2021\n- **Title:** Autoregressive Entity Retrieval\n- **Authors:** De Cao, Izacard, Riedel & Petroni\n- **核心方法:** 首个用自回归生成方式检索实体的系统，基于 fine-tuned BART 逐 token 生成实体名，用 prefix trie 约束 beam search 只允许生成合法实体标识符，在 20+ entity disambiguation/linking 基准上达到 SOTA。\n- **与 OntoCoDec 的关系:** GENRE 的 trie-based constrained beam search 是 vocabulary-constrained generation 的经典范式。OntoCoDec 的 Semantic 层借鉴类似思路（限制输出到合法类型/实体），但不需要构建 trie，而是通过 logits masking 直接在 token 级别实施 domain/range 约束。\n- **BibTeX key:** `decao2021genre`\n- **ArXiv:** 2010.00904\n\n### GenIE | NAACL 2022\n- **Title:** GenIE: Generative Information Extraction\n- **Authors:** Josifoski, De Cao, Peyrard, Petroni & West\n- **核心方法:** 自回归 seq2seq 模型生成 (subject, relation, object) 三元组，结合 trie-based lexical constraints（强制输出合法实体/关系标识符）和 state-based constraints（强制合法三元组结构），实现端到端抽取。\n- **与 OntoCoDec 的关系:** GenIE 是将 vocabulary constraint 应用于 IE 的先驱，但需要 fine-tuning 专用模型。OntoCoDec 的关键优势是 training-free——直接在通用 LLM 上通过解码时约束实现，无需额外训练。\n- **BibTeX key:** `josifoski2022genie`\n- **ArXiv:** 2112.08340\n\n### NeuroLogic Decoding | NAACL 2021\n- **Title:** NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints\n- **Authors:** Lu, West, Zellers, Le Bras, Bhagavatula & Choi\n- **核心方法:** 将词汇约束表达为谓词逻辑公式（合取/析取 of must-include/must-exclude tokens），在每步通过 pruning 和 re-ranking beams 执行约束，渐近复杂度等同标准 beam search。\n- **与 OntoCoDec 的关系:** NeuroLogic 处理的是 lexical inclusion/exclusion 约束（\"生成必须包含词 X\"），而 OntoCoDec 的 Semantic 层处理的是 relational/type 约束（\"关系 R 的 head 必须是类型 T\"）。约束语义层次不同。\n- **BibTeX key:** `lu2021neurologic`\n- **ArXiv:** 2010.12884\n\n### Grammar-Constrained Decoding for Structured NLP | EMNLP 2023\n- **Title:** Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning\n- **Authors:** Geng, Josifoski, Peyrard & West\n- **核心方法:** 提出 grammar-constrained decoding（GCD）统一框架：每步将违反形式文法的 token logits 设为负无穷，保证结构合法输出，无需 fine-tuning。引入 input-dependent grammars 增加灵活性。在 IE、entity disambiguation、constituency parsing 上验证。\n- **与 OntoCoDec 的关系:** 这是最直接的前驱工作——同样对 IE 任务使用 logits masking。但 Geng et al. 的约束限于语法层面（输出格式合法），OntoCoDec 在此基础上增加了语义层约束（domain/range 合法），是从格式正确到语义正确的扩展。\n- **BibTeX key:** `geng2023gcd`\n- **ArXiv:** 2305.13971\n\n---\n\n## 3. Structural Constraints for Information Extraction\n\n### UIE | ACL 2022\n- **Title:** Unified Structure Generation for Universal Information Extraction\n- **Authors:** Lu, Liu, Dai et al.\n- **核心方法:** 定义 Structured Extraction Language（SEL）统一编码不同 IE 输出结构（entity, relation, event, sentiment），配合 schema-based prompt（Structural Schema Instructor）和大规模预训练 text-to-structure 模型，在 4 个 IE 任务 13 个数据集上达到 SOTA。\n- **与 OntoCoDec 的关系:** UIE 通过训练让模型\"学会\"输出合法结构，但无法保证推理时不违反 schema 约束。OntoCoDec 是 decoding-time enforcement，提供硬性保证——违反 domain/range 的输出不可能被生成。\n- **BibTeX key:** `lu2022uie`\n- **ArXiv:** 2203.12277\n\n### GoLLIE | ICLR 2024\n- **Title:** Annotation Guidelines improve Zero-Shot Information-Extraction\n- **Authors:** Sainz, Garcia-Ferrero, Agerri et al.\n- **核心方法:** 将 annotation guidelines 表达为 Python class 定义（dataclass），fine-tune Code-LLaMA 生成 Python 代码形式的结构化输出，通过 code-based schema 表达实现强零样本泛化到未见 IE schema。\n- **与 OntoCoDec 的关系:** GoLLIE 用 Python 类型系统隐式表达类型约束，但执行仍依赖模型训练。OntoCoDec 在解码时显式执行本体约束，两者互补——GoLLIE 的 code-based schema 可与 OntoCoDec 的 decoding-time enforcement 结合。\n- **BibTeX key:** `sainz2024gollie`\n- **ArXiv:** 2310.03668\n\n### CodeIE | ACL 2023\n- **Title:** Large Code Generation Models are Better Few-Shot Information Extractors\n- **Authors:** Li, Sun, Tang et al.\n- **核心方法:** 将 IE 结构化输出重构为代码生成任务，用 code-LLM（Codex）+ code-style prompts 执行 NER 和 RE，代码形式天然捕获 IE 输出的结构性。在 few-shot 设置下一致优于 fine-tuned IE 模型和 NL-LLM prompting。\n- **与 OntoCoDec 的关系:** CodeIE 通过代码形式化提高结构一致性，但仍是 soft constraint（模型可能生成非法代码）。OntoCoDec 的 Grammar+Semantic 层提供 hard constraint——输出格式和语义类型均被强制保证。\n- **BibTeX key:** `li2023codeie`\n- **ArXiv:** 2305.05711\n\n### InstructUIE | arXiv 2023\n- **Title:** Multi-task Instruction Tuning for Unified Information Extraction\n- **Authors:** Wang, Zhou, Zu et al.\n- **核心方法:** 构建 IE INSTRUCTIONS 基准（32 个 IE 数据集统一为 text-to-text 格式 + 专家指令），fine-tune Flan-T5 实现单模型处理 NER/RE/EE。指令微调的小模型大幅超越 GPT-3.5。\n- **与 OntoCoDec 的关系:** InstructUIE 靠 instruction tuning 提高 IE 输出质量，但无结构保证。OntoCoDec 与 InstructUIE 正交——可在 instruction-tuned 模型上叠加 decoding-time 约束进一步消除违规。\n- **BibTeX key:** `wang2023instructuie`\n- **ArXiv:** 2304.08085\n\n### ADELIE | EMNLP 2024\n- **Title:** Aligning Large Language Models on Information Extraction\n- **Authors:** Qi, Peng, Wang et al. (THU-KEG)\n- **核心方法:** 构建 IEInstruct 高质量对齐语料，用 SFT + DPO 训练 LLM 进行 IE，覆盖 closed IE、open IE、on-demand IE。ADELIE 在开源模型中达到 SOTA，同时保持通用 LLM 能力。\n- **与 OntoCoDec 的关系:** ADELIE 代表 training-time alignment 路线，通过 preference optimization 让模型偏好合法输出。OntoCoDec 是 decoding-time enforcement 路线，提供更强保证且 training-free。两者可叠加使用。\n- **BibTeX key:** `qi2024adelie`\n- **ArXiv:** 2405.05008\n\n---\n\n## 4. Type-Checking / Ontology Validation in NLP\n\n### ODKE+ | arXiv 2025\n- **Title:** ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs\n- **Authors:** Khorshidi, Nikfarjam, Shankar et al. (Apple)\n- **核心方法:** 动态生成针对每种实体类型的 ontology snippets（含 domain/range 约束），用于对齐 LLM 抽取结果与 schema 约束。处理 9M+ Wikipedia 页面，19M facts，98.8% precision across 195 predicates。\n- **与 OntoCoDec 的关系:** ODKE+ 在 prompt 层面注入 ontology 约束，属于 soft guidance。OntoCoDec 在 decoding 层面强制执行 domain/range 约束，属于 hard enforcement。ODKE+ 无法保证 0% violation rate，OntoCoDec 可以。\n- **BibTeX key:** `khorshidi2025odke`\n- **ArXiv:** 2509.04696\n\n### Open IE with Entity Focused Constraints | Findings of EACL 2023\n- **Title:** Open Information Extraction with Entity Focused Constraints\n- **Authors:** Upadhyay, Balalau & Manolescu\n- **核心方法:** 将 entity-type 知识作为约束注入 Open IE，通过 constrained inference（解码时）和 constraint-aware training 两种机制实现，在 CaRB 上 F1 提升 29.17%。\n- **与 OntoCoDec 的关系:** 与 OntoCoDec 最相近的工作之一——同样在解码时利用 entity type 约束。但该方法针对 Open IE 的通用类型约束，OntoCoDec 针对 closed IE 的 ontology-specific domain/range 约束，粒度更细。\n- **BibTeX key:** `upadhyay2023openie`\n\n### EnriCo | arXiv 2024\n- **Title:** EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction\n- **Authors:** Zaratiana, Tomeh, Dauxais, Holat & Charnois\n- **核心方法:** Attention-based enriched representations for joint entity and relation extraction，结合一套 constrained decoding 算法在推理时强制执行任务特定的结构约束（如 entity type compatibility for relations）。\n- **与 OntoCoDec 的关系:** EnriCo 在传统 joint extraction 模型上加 constrained decoding，OntoCoDec 在 LLM 上做。EnriCo 的约束是模型特定的，OntoCoDec 的约束来自外部 ontology，更通用、可复用。\n- **BibTeX key:** `zaratiana2024enrico`\n- **ArXiv:** 2404.12493\n\n### LLM as KG Curators | GenAIK 2025\n- **Title:** Can LLMs be Knowledge Graph Curators for Validating Triple Insertions?\n- **Authors:** Regino & dos Reis\n- **核心方法:** 用 prompt-based 多阶段验证管线引导 LLM 评估 RDF triple 插入的 domain/range 一致性和语义连贯性。\n- **与 OntoCoDec 的关系:** 典型的 post-hoc validation 方法——先生成再验证。OntoCoDec 是 preventive 方法——在生成时就阻止违规，不需要后续验证和纠错循环。\n- **BibTeX key:** `regino2025kgcurator`\n\n---\n\n## 5. Constrained Decoding Quality Concerns\n\n### Let Me Speak Freely? | EMNLP 2024\n- **Title:** Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\n- **Authors:** Tam, Wu, Tsai, Lin, Lee & Chen\n- **核心方法:** 系统研究结构化格式约束（JSON, XML, YAML）对 LLM 推理能力的影响。发现刚性格式约束损害推理密集型任务（数学、多跳 QA）但有利于分类任务（slot-filling、intent detection）。约束越严格，性能退化越大。\n- **与 OntoCoDec 的关系:** 这是 OntoCoDec 需要直接回应的 concern。OntoCoDec 在 SciERC 上证明 F1 无损（甚至略有提升），说明在 IE 任务场景下——属于该论文发现的\"分类任务\"范畴——约束解码不仅不损害质量，反而可能有益。\n- **BibTeX key:** `tam2024letmespeak`\n- **ArXiv:** 2408.02442\n\n### CRANE | ICML 2025\n- **Title:** CRANE: Reasoning with Constrained LLM Generation\n- **Authors:** Banerjee, Suresh, Ugare, Misailovic & Singh\n- **核心方法:** 从理论角度解释为什么将 LLM 输出约束到 restrictive grammars（只允许语法合法的最终答案）会降低推理能力。提出 alternating strategy：在 unconstrained generation（推理/CoT）和 constrained generation（结构化输出）之间交替，在 GSM-symbolic 和 FOLIO 上提升最多 10 个百分点。\n- **与 OntoCoDec 的关系:** CRANE 的发现验证了 OntoCoDec S2 策略（两通道分离）的合理性——S2 将推理（生成候选）和约束（格式化输出）分离到两个 pass，正是 CRANE 理论推荐的 alternating approach。\n- **BibTeX key:** `banerjee2025crane`\n- **ArXiv:** 2502.09061\n\n### Structure Snowballing | arXiv 2026\n- **Title:** From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection\n- **Authors:** Zhou (Saarland University)\n- **核心方法:** 发现 constrained decoding 应用于 LLM self-correction/reflection 时的新失败模式——\"structure snowballing\"：满足严格格式规则的认知负荷将模型推入格式陷阱而非改善推理。揭示结构粒度与模型内部容量之间的张力。\n- **与 OntoCoDec 的关系:** OntoCoDec 避免了 snowballing 风险：其约束是 task-specific 的 IE 本体约束而非通用格式约束，且约束空间有限（合法类型集合远小于 free-form 生成空间），不会引入过度的认知负荷。\n- **BibTeX key:** `zhou2026snowballing`\n- **ArXiv:** 2604.06066\n\n### The Hidden Cost of Structure | RANLP 2025\n- **Title:** The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\n- **Authors:** Schall & de Melo\n- **核心方法:** 跨 11 个模型和多个基准的系统实证研究。发现 base model 和 instruction-tuned model 在结构约束下表现分化：尽管约束保证格式合法，constrained decoding 在推理密集型任务上常降低语义正确性 10-30%。\n- **与 OntoCoDec 的关系:** OntoCoDec 的实验在 instruction-tuned model 上进行，且 IE 任务是\"extraction\"而非\"reasoning\"，属于该论文发现的约束解码影响较小的任务类型。F1 无损结果与该论文的观察一致。\n- **BibTeX key:** `schall2025hiddencost`\n\n---\n\n## 6. OntoCoDec 在 Landscape 中的定位\n\n### 核心差异化\n\nOntoCoDec 在约束解码 landscape 中占据独特位置，体现为三个维度的创新：\n\n**1. 约束层次：从格式到语义**\n- 现有 grammar-constrained decoding（XGrammar, Outlines, LMQL）保证**格式正确性**（valid JSON, enum values）\n- 现有 vocabulary-constrained generation（GENRE, NeuroLogic）保证**词汇合法性**（输出在预定义词表中）\n- OntoCoDec 增加**语义正确性**层（domain/range 约束），将约束从 syntactic 扩展到 semantic\n\n**2. 执行时机：从 post-hoc 到 preventive**\n- 传统 ontology validation 方法（ODKE+, KG validation）是 post-hoc：先生成再验证\n- 训练方法（UIE, GoLLIE, ADELIE）是 soft constraint：通过训练引导模型偏好合法输出，但无保证\n- OntoCoDec 是 decoding-time enforcement：不合法的输出不可能被生成，无需验证-纠错循环\n\n**3. 质量保持：约束无损**\n- 约束解码质量 concern（Let Me Speak Freely, CRANE, Structure Snowballing）指出约束常损害推理\n- OntoCoDec 在 SciERC 上 DR violation 15.37%→0.93%（↓94%）且 F1 无损，反驳\"约束必损质量\"的 narrative\n- OntoCoDec S2 策略（两通道分离）符合 CRANE 理论推荐的 alternating approach\n\n### 技术栈定位\n\n```\nLayer 3 (OntoCoDec Semantic): domain/range logits masking ← 本文贡献\nLayer 2 (OntoCoDec Grammar):  JSON schema + enum constraints ← 基于 XGrammar\nLayer 1 (LLM):                base language model generation\n```\n\n- Layer 2 消除 format violations（RV/ET），与 Outlines/LMQL/SGLang 同层\n- Layer 3 消除 semantic violations（DR），是 OntoCoDec 独有的贡献\n- 两层组合（S1 单通道或 S2 两通道）实现从格式到语义的完整约束覆盖\n\n### 与各 paradigm 的关系总结\n\n| Paradigm | 代表工作 | OntoCoDec 关系 |\n|----------|----------|---------------|\n| Grammar-constrained decoding | XGrammar, Outlines, LMQL | OntoCoDec Grammar 层基于此；Semantic 层是超越 |\n| Vocabulary/type-constrained generation | GENRE, GenIE, GCD | OntoCoDec 借鉴 logits masking 技术，但约束来自 IE ontology 而非固定词表 |\n| Structural constraint for IE | UIE, GoLLIE, CodeIE | 这些方法靠 training/prompting，OntoCoDec 是 decoding-time enforcement，两者互补 |\n| Ontology validation | ODKE+, EnriCo | Post-hoc validation vs. preventive enforcement 的本质区别 |\n| Constrained decoding quality | Let Me Speak Freely, CRANE | OntoCoDec F1 无损实验直接回应此 concern，S2 策略符合 CRANE 理论 |\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cd9b12c-c936-459d-bd86-60d74346f547",
  "isSidechain": false,
  "requestId": "req_011Cb1gevAsjxFUPQYsxpG4M",
  "type": "assistant",
  "uuid": "e47006c3-ac39-4774-85b0-3da6c0a3eab5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbUumDpKTPDmJfjKs51Wcr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6293,
      "cache_read_input_tokens": 27172,
      "output_tokens": 7102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7102,
          "cache_read_input_tokens": 27172,
          "cache_creation_input_tokens": 6293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6293
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

_source line 28 · 2026-05-14T02:40:05.951Z_

<details><summary>↩ Tool result · `toolu_01HAim65d5696zZYLFtijTKY`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/related_work_survey.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "e47006c3-ac39-4774-85b0-3da6c0a3eab5",
  "isSidechain": false,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "type": "user",
  "uuid": "9694ea5d-1afb-4c7e-81bc-c78eabdad2ce",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/related_work_survey.md",
    "content": "# OntoCoDec Related Work Survey\n\n## 1. Grammar-Constrained Decoding\n\n### XGrammar | MLSys 2025\n- **Title:** XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models\n- **Authors:** Dong et al.\n- **核心方法:** 将词表划分为 context-independent（离线预检）和 context-dependent（运行时检查）两类 token，结合 persistent stack-based pushdown automata 高效执行 CFG 约束，比先前方法快 100x。\n- **与 OntoCoDec 的关系:** OntoCoDec 的 Grammar 层直接基于 XGrammar 实现 JSON schema + enum 约束，消除 RV/ET violations。XGrammar 提供格式正确性保证，但不处理语义层约束（domain/range），这正是 OntoCoDec Semantic 层的贡献。\n- **BibTeX key:** `dong2025xgrammar`\n- **ArXiv:** 2411.15100\n\n### Outlines | arXiv 2023\n- **Title:** Efficient Guided Generation for Large Language Models\n- **Authors:** Willard & Louf\n- **核心方法:** 将受约束文本生成重构为有限状态机（FSM）中的状态转移，为每个 FSM 状态离线构建词表索引，实现正则表达式约束的 O(1) 均摊 per-token 检查，扩展至 LALR(1) parser 支持 CFG。\n- **与 OntoCoDec 的关系:** Outlines 是 grammar-constrained decoding 的开源先驱之一，与 XGrammar 属同一技术路线。OntoCoDec 选择 XGrammar 而非 Outlines 是因为其更高效的 vocabulary 预处理和对 LLM serving 框架（vLLM/SGLang）的原生集成。\n- **BibTeX key:** `willard2023outlines`\n- **ArXiv:** 2307.09702\n\n### LMQL | PLDI 2023\n- **Title:** Prompting Is Programming: A Query Language for Large Language Models\n- **Authors:** Beurer-Kellner, Fischer & Vechev\n- **核心方法:** SQL 风格的 LLM 查询语言，将自然语言 prompt 与程序控制流和声明式约束（类型、长度、正则、停止条件）结合，运行时编译为 token-level masking，减少 26-85% API 成本。\n- **与 OntoCoDec 的关系:** LMQL 提供通用的声明式约束框架，但约束表达能力限于格式层面（类型、长度、正则）。OntoCoDec 的 Semantic 层引入了 IE 任务特有的 domain/range 本体约束，超越了通用格式约束的范畴。\n- **BibTeX key:** `beurer-kellner2023lmql`\n- **ArXiv:** 2212.06094\n\n### DOMINO | ICML 2024\n- **Title:** Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation\n- **Authors:** Beurer-Kellner, Fischer & Vechev\n- **核心方法:** 提出 non-invasive constrained decoding 算法，在执行 CFG 约束的同时最小化对 LLM 原始分布的扭曲，利用预计算和 speculative decoding 实现甚至超过无约束生成的吞吐。\n- **与 OntoCoDec 的关系:** DOMINO 关注 distribution distortion 问题——约束解码如何改变 LLM 的 token 分布。OntoCoDec 的 F1 无损结果从实验角度呼应了这一方向：精心设计的约束不必牺牲生成质量。\n- **BibTeX key:** `beurer-kellner2024domino`\n- **ArXiv:** 2403.06988\n\n### Grammar-Aligned Decoding (ASAp) | NeurIPS 2024\n- **Title:** Grammar-Aligned Decoding\n- **Authors:** Park, Wang, Berg-Kirkpatrick, Polikarpova & D'Antoni\n- **核心方法:** 证明 naive token masking 会扭曲 LLM 的条件分布，提出 ASAp（Adaptive Sampling with Approximate expected futures）算法，在保证语法正确性的同时保持对原始 LM 分布的无偏性。\n- **与 OntoCoDec 的关系:** ASAp 解决的是 grammar-constrained decoding 的理论正确性问题。OntoCoDec 的 logits masking 也面临类似的分布扭曲风险，但实验证明在 IE 任务上 F1 无损，说明 IE 场景中合法约束的 masking 影响有限。\n- **BibTeX key:** `park2024grammar`\n- **ArXiv:** 2405.21047\n\n---\n\n## 2. Vocabulary/Type-Constrained Generation\n\n### GENRE | ICLR 2021\n- **Title:** Autoregressive Entity Retrieval\n- **Authors:** De Cao, Izacard, Riedel & Petroni\n- **核心方法:** 首个用自回归生成方式检索实体的系统，基于 fine-tuned BART 逐 token 生成实体名，用 prefix trie 约束 beam search 只允许生成合法实体标识符，在 20+ entity disambiguation/linking 基准上达到 SOTA。\n- **与 OntoCoDec 的关系:** GENRE 的 trie-based constrained beam search 是 vocabulary-constrained generation 的经典范式。OntoCoDec 的 Semantic 层借鉴类似思路（限制输出到合法类型/实体），但不需要构建 trie，而是通过 logits masking 直接在 token 级别实施 domain/range 约束。\n- **BibTeX key:** `decao2021genre`\n- **ArXiv:** 2010.00904\n\n### GenIE | NAACL 2022\n- **Title:** GenIE: Generative Information Extraction\n- **Authors:** Josifoski, De Cao, Peyrard, Petroni & West\n- **核心方法:** 自回归 seq2seq 模型生成 (subject, relation, object) 三元组，结合 trie-based lexical constraints（强制输出合法实体/关系标识符）和 state-based constraints（强制合法三元组结构），实现端到端抽取。\n- **与 OntoCoDec 的关系:** GenIE 是将 vocabulary constraint 应用于 IE 的先驱，但需要 fine-tuning 专用模型。OntoCoDec 的关键优势是 training-free——直接在通用 LLM 上通过解码时约束实现，无需额外训练。\n- **BibTeX key:** `josifoski2022genie`\n- **ArXiv:** 2112.08340\n\n### NeuroLogic Decoding | NAACL 2021\n- **Title:** NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints\n- **Authors:** Lu, West, Zellers, Le Bras, Bhagavatula & Choi\n- **核心方法:** 将词汇约束表达为谓词逻辑公式（合取/析取 of must-include/must-exclude tokens），在每步通过 pruning 和 re-ranking beams 执行约束，渐近复杂度等同标准 beam search。\n- **与 OntoCoDec 的关系:** NeuroLogic 处理的是 lexical inclusion/exclusion 约束（\"生成必须包含词 X\"），而 OntoCoDec 的 Semantic 层处理的是 relational/type 约束（\"关系 R 的 head 必须是类型 T\"）。约束语义层次不同。\n- **BibTeX key:** `lu2021neurologic`\n- **ArXiv:** 2010.12884\n\n### Grammar-Constrained Decoding for Structured NLP | EMNLP 2023\n- **Title:** Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning\n- **Authors:** Geng, Josifoski, Peyrard & West\n- **核心方法:** 提出 grammar-constrained decoding（GCD）统一框架：每步将违反形式文法的 token logits 设为负无穷，保证结构合法输出，无需 fine-tuning。引入 input-dependent grammars 增加灵活性。在 IE、entity disambiguation、constituency parsing 上验证。\n- **与 OntoCoDec 的关系:** 这是最直接的前驱工作——同样对 IE 任务使用 logits masking。但 Geng et al. 的约束限于语法层面（输出格式合法），OntoCoDec 在此基础上增加了语义层约束（domain/range 合法），是从格式正确到语义正确的扩展。\n- **BibTeX key:** `geng2023gcd`\n- **ArXiv:** 2305.13971\n\n---\n\n## 3. Structural Constraints for Information Extraction\n\n### UIE | ACL 2022\n- **Title:** Unified Structure Generation for Universal Information Extraction\n- **Authors:** Lu, Liu, Dai et al.\n- **核心方法:** 定义 Structured Extraction Language（SEL）统一编码不同 IE 输出结构（entity, relation, event, sentiment），配合 schema-based prompt（Structural Schema Instructor）和大规模预训练 text-to-structure 模型，在 4 个 IE 任务 13 个数据集上达到 SOTA。\n- **与 OntoCoDec 的关系:** UIE 通过训练让模型\"学会\"输出合法结构，但无法保证推理时不违反 schema 约束。OntoCoDec 是 decoding-time enforcement，提供硬性保证——违反 domain/range 的输出不可能被生成。\n- **BibTeX key:** `lu2022uie`\n- **ArXiv:** 2203.12277\n\n### GoLLIE | ICLR 2024\n- **Title:** Annotation Guidelines improve Zero-Shot Information-Extraction\n- **Authors:** Sainz, Garcia-Ferrero, Agerri et al.\n- **核心方法:** 将 annotation guidelines 表达为 Python class 定义（dataclass），fine-tune Code-LLaMA 生成 Python 代码形式的结构化输出，通过 code-based schema 表达实现强零样本泛化到未见 IE schema。\n- **与 OntoCoDec 的关系:** GoLLIE 用 Python 类型系统隐式表达类型约束，但执行仍依赖模型训练。OntoCoDec 在解码时显式执行本体约束，两者互补——GoLLIE 的 code-based schema 可与 OntoCoDec 的 decoding-time enforcement 结合。\n- **BibTeX key:** `sainz2024gollie`\n- **ArXiv:** 2310.03668\n\n### CodeIE | ACL 2023\n- **Title:** Large Code Generation Models are Better Few-Shot Information Extractors\n- **Authors:** Li, Sun, Tang et al.\n- **核心方法:** 将 IE 结构化输出重构为代码生成任务，用 code-LLM（Codex）+ code-style prompts 执行 NER 和 RE，代码形式天然捕获 IE 输出的结构性。在 few-shot 设置下一致优于 fine-tuned IE 模型和 NL-LLM prompting。\n- **与 OntoCoDec 的关系:** CodeIE 通过代码形式化提高结构一致性，但仍是 soft constraint（模型可能生成非法代码）。OntoCoDec 的 Grammar+Semantic 层提供 hard constraint——输出格式和语义类型均被强制保证。\n- **BibTeX key:** `li2023codeie`\n- **ArXiv:** 2305.05711\n\n### InstructUIE | arXiv 2023\n- **Title:** Multi-task Instruction Tuning for Unified Information Extraction\n- **Authors:** Wang, Zhou, Zu et al.\n- **核心方法:** 构建 IE INSTRUCTIONS 基准（32 个 IE 数据集统一为 text-to-text 格式 + 专家指令），fine-tune Flan-T5 实现单模型处理 NER/RE/EE。指令微调的小模型大幅超越 GPT-3.5。\n- **与 OntoCoDec 的关系:** InstructUIE 靠 instruction tuning 提高 IE 输出质量，但无结构保证。OntoCoDec 与 InstructUIE 正交——可在 instruction-tuned 模型上叠加 decoding-time 约束进一步消除违规。\n- **BibTeX key:** `wang2023instructuie`\n- **ArXiv:** 2304.08085\n\n### ADELIE | EMNLP 2024\n- **Title:** Aligning Large Language Models on Information Extraction\n- **Authors:** Qi, Peng, Wang et al. (THU-KEG)\n- **核心方法:** 构建 IEInstruct 高质量对齐语料，用 SFT + DPO 训练 LLM 进行 IE，覆盖 closed IE、open IE、on-demand IE。ADELIE 在开源模型中达到 SOTA，同时保持通用 LLM 能力。\n- **与 OntoCoDec 的关系:** ADELIE 代表 training-time alignment 路线，通过 preference optimization 让模型偏好合法输出。OntoCoDec 是 decoding-time enforcement 路线，提供更强保证且 training-free。两者可叠加使用。\n- **BibTeX key:** `qi2024adelie`\n- **ArXiv:** 2405.05008\n\n---\n\n## 4. Type-Checking / Ontology Validation in NLP\n\n### ODKE+ | arXiv 2025\n- **Title:** ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs\n- **Authors:** Khorshidi, Nikfarjam, Shankar et al. (Apple)\n- **核心方法:** 动态生成针对每种实体类型的 ontology snippets（含 domain/range 约束），用于对齐 LLM 抽取结果与 schema 约束。处理 9M+ Wikipedia 页面，19M facts，98.8% precision across 195 predicates。\n- **与 OntoCoDec 的关系:** ODKE+ 在 prompt 层面注入 ontology 约束，属于 soft guidance。OntoCoDec 在 decoding 层面强制执行 domain/range 约束，属于 hard enforcement。ODKE+ 无法保证 0% violation rate，OntoCoDec 可以。\n- **BibTeX key:** `khorshidi2025odke`\n- **ArXiv:** 2509.04696\n\n### Open IE with Entity Focused Constraints | Findings of EACL 2023\n- **Title:** Open Information Extraction with Entity Focused Constraints\n- **Authors:** Upadhyay, Balalau & Manolescu\n- **核心方法:** 将 entity-type 知识作为约束注入 Open IE，通过 constrained inference（解码时）和 constraint-aware training 两种机制实现，在 CaRB 上 F1 提升 29.17%。\n- **与 OntoCoDec 的关系:** 与 OntoCoDec 最相近的工作之一——同样在解码时利用 entity type 约束。但该方法针对 Open IE 的通用类型约束，OntoCoDec 针对 closed IE 的 ontology-specific domain/range 约束，粒度更细。\n- **BibTeX key:** `upadhyay2023openie`\n\n### EnriCo | arXiv 2024\n- **Title:** EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction\n- **Authors:** Zaratiana, Tomeh, Dauxais, Holat & Charnois\n- **核心方法:** Attention-based enriched representations for joint entity and relation extraction，结合一套 constrained decoding 算法在推理时强制执行任务特定的结构约束（如 entity type compatibility for relations）。\n- **与 OntoCoDec 的关系:** EnriCo 在传统 joint extraction 模型上加 constrained decoding，OntoCoDec 在 LLM 上做。EnriCo 的约束是模型特定的，OntoCoDec 的约束来自外部 ontology，更通用、可复用。\n- **BibTeX key:** `zaratiana2024enrico`\n- **ArXiv:** 2404.12493\n\n### LLM as KG Curators | GenAIK 2025\n- **Title:** Can LLMs be Knowledge Graph Curators for Validating Triple Insertions?\n- **Authors:** Regino & dos Reis\n- **核心方法:** 用 prompt-based 多阶段验证管线引导 LLM 评估 RDF triple 插入的 domain/range 一致性和语义连贯性。\n- **与 OntoCoDec 的关系:** 典型的 post-hoc validation 方法——先生成再验证。OntoCoDec 是 preventive 方法——在生成时就阻止违规，不需要后续验证和纠错循环。\n- **BibTeX key:** `regino2025kgcurator`\n\n---\n\n## 5. Constrained Decoding Quality Concerns\n\n### Let Me Speak Freely? | EMNLP 2024\n- **Title:** Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\n- **Authors:** Tam, Wu, Tsai, Lin, Lee & Chen\n- **核心方法:** 系统研究结构化格式约束（JSON, XML, YAML）对 LLM 推理能力的影响。发现刚性格式约束损害推理密集型任务（数学、多跳 QA）但有利于分类任务（slot-filling、intent detection）。约束越严格，性能退化越大。\n- **与 OntoCoDec 的关系:** 这是 OntoCoDec 需要直接回应的 concern。OntoCoDec 在 SciERC 上证明 F1 无损（甚至略有提升），说明在 IE 任务场景下——属于该论文发现的\"分类任务\"范畴——约束解码不仅不损害质量，反而可能有益。\n- **BibTeX key:** `tam2024letmespeak`\n- **ArXiv:** 2408.02442\n\n### CRANE | ICML 2025\n- **Title:** CRANE: Reasoning with Constrained LLM Generation\n- **Authors:** Banerjee, Suresh, Ugare, Misailovic & Singh\n- **核心方法:** 从理论角度解释为什么将 LLM 输出约束到 restrictive grammars（只允许语法合法的最终答案）会降低推理能力。提出 alternating strategy：在 unconstrained generation（推理/CoT）和 constrained generation（结构化输出）之间交替，在 GSM-symbolic 和 FOLIO 上提升最多 10 个百分点。\n- **与 OntoCoDec 的关系:** CRANE 的发现验证了 OntoCoDec S2 策略（两通道分离）的合理性——S2 将推理（生成候选）和约束（格式化输出）分离到两个 pass，正是 CRANE 理论推荐的 alternating approach。\n- **BibTeX key:** `banerjee2025crane`\n- **ArXiv:** 2502.09061\n\n### Structure Snowballing | arXiv 2026\n- **Title:** From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection\n- **Authors:** Zhou (Saarland University)\n- **核心方法:** 发现 constrained decoding 应用于 LLM self-correction/reflection 时的新失败模式——\"structure snowballing\"：满足严格格式规则的认知负荷将模型推入格式陷阱而非改善推理。揭示结构粒度与模型内部容量之间的张力。\n- **与 OntoCoDec 的关系:** OntoCoDec 避免了 snowballing 风险：其约束是 task-specific 的 IE 本体约束而非通用格式约束，且约束空间有限（合法类型集合远小于 free-form 生成空间），不会引入过度的认知负荷。\n- **BibTeX key:** `zhou2026snowballing`\n- **ArXiv:** 2604.06066\n\n### The Hidden Cost of Structure | RANLP 2025\n- **Title:** The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\n- **Authors:** Schall & de Melo\n- **核心方法:** 跨 11 个模型和多个基准的系统实证研究。发现 base model 和 instruction-tuned model 在结构约束下表现分化：尽管约束保证格式合法，constrained decoding 在推理密集型任务上常降低语义正确性 10-30%。\n- **与 OntoCoDec 的关系:** OntoCoDec 的实验在 instruction-tuned model 上进行，且 IE 任务是\"extraction\"而非\"reasoning\"，属于该论文发现的约束解码影响较小的任务类型。F1 无损结果与该论文的观察一致。\n- **BibTeX key:** `schall2025hiddencost`\n\n---\n\n## 6. OntoCoDec 在 Landscape 中的定位\n\n### 核心差异化\n\nOntoCoDec 在约束解码 landscape 中占据独特位置，体现为三个维度的创新：\n\n**1. 约束层次：从格式到语义**\n- 现有 grammar-constrained decoding（XGrammar, Outlines, LMQL）保证**格式正确性**（valid JSON, enum values）\n- 现有 vocabulary-constrained generation（GENRE, NeuroLogic）保证**词汇合法性**（输出在预定义词表中）\n- OntoCoDec 增加**语义正确性**层（domain/range 约束），将约束从 syntactic 扩展到 semantic\n\n**2. 执行时机：从 post-hoc 到 preventive**\n- 传统 ontology validation 方法（ODKE+, KG validation）是 post-hoc：先生成再验证\n- 训练方法（UIE, GoLLIE, ADELIE）是 soft constraint：通过训练引导模型偏好合法输出，但无保证\n- OntoCoDec 是 decoding-time enforcement：不合法的输出不可能被生成，无需验证-纠错循环\n\n**3. 质量保持：约束无损**\n- 约束解码质量 concern（Let Me Speak Freely, CRANE, Structure Snowballing）指出约束常损害推理\n- OntoCoDec 在 SciERC 上 DR violation 15.37%→0.93%（↓94%）且 F1 无损，反驳\"约束必损质量\"的 narrative\n- OntoCoDec S2 策略（两通道分离）符合 CRANE 理论推荐的 alternating approach\n\n### 技术栈定位\n\n```\nLayer 3 (OntoCoDec Semantic): domain/range logits masking ← 本文贡献\nLayer 2 (OntoCoDec Grammar):  JSON schema + enum constraints ← 基于 XGrammar\nLayer 1 (LLM):                base language model generation\n```\n\n- Layer 2 消除 format violations（RV/ET），与 Outlines/LMQL/SGLang 同层\n- Layer 3 消除 semantic violations（DR），是 OntoCoDec 独有的贡献\n- 两层组合（S1 单通道或 S2 两通道）实现从格式到语义的完整约束覆盖\n\n### 与各 paradigm 的关系总结\n\n| Paradigm | 代表工作 | OntoCoDec 关系 |\n|----------|----------|---------------|\n| Grammar-constrained decoding | XGrammar, Outlines, LMQL | OntoCoDec Grammar 层基于此；Semantic 层是超越 |\n| Vocabulary/type-constrained generation | GENRE, GenIE, GCD | OntoCoDec 借鉴 logits masking 技术，但约束来自 IE ontology 而非固定词表 |\n| Structural constraint for IE | UIE, GoLLIE, CodeIE | 这些方法靠 training/prompting，OntoCoDec 是 decoding-time enforcement，两者互补 |\n| Ontology validation | ODKE+, EnriCo | Post-hoc validation vs. preventive enforcement 的本质区别 |\n| Constrained decoding quality | Let Me Speak Freely, CRANE | OntoCoDec F1 无损实验直接回应此 concern，S2 策略符合 CRANE 理论 |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "e47006c3-ac39-4774-85b0-3da6c0a3eab5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "leafUuid": "9694ea5d-1afb-4c7e-81bc-c78eabdad2ce",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey for OntoCoDec related work",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909"
}
```

---

### Tool call

_source line 31 · 2026-05-14T02:40:08.854Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01B1qG4jRhDQ9v1pf57N2C9X`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9694ea5d-1afb-4c7e-81bc-c78eabdad2ce",
  "isSidechain": false,
  "requestId": "req_011Cb1gr31wokPzBYHTXW3Yu",
  "type": "assistant",
  "uuid": "a5966717-5229-4cc9-8b2b-04357531a5f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReTbG5U4VDuNW2uYUgaT6g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7159,
      "cache_read_input_tokens": 33465,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7159,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 33465,
          "cache_creation_input_tokens": 7159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7159
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

_source line 32 · 2026-05-14T02:40:08.879Z_

<details><summary>↩ Tool result · `toolu_01B1qG4jRhDQ9v1pf57N2C9X`</summary>

````text
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
  "parentUuid": "a5966717-5229-4cc9-8b2b-04357531a5f1",
  "isSidechain": false,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "type": "user",
  "uuid": "7d461ba8-3940-4ae6-9ff2-e856d7455e22",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "a5966717-5229-4cc9-8b2b-04357531a5f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-14T02:40:08.932Z_

```json
{
  "parentUuid": "7d461ba8-3940-4ae6-9ff2-e856d7455e22",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "48e3f226-999e-4ed8-8cd2-bb88c82fbcf9",
  "timestamp": "2026-05-14T02:40:08.932Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 34 · 2026-05-14T02:40:12.545Z_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool only allows writing to memory.md, writing_plan.yaml, paper_framing.md. The artifact is already written to the artifacts directory. I need to register it. Let me search for the register_artifact tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48e3f226-999e-4ed8-8cd2-bb88c82fbcf9",
  "isSidechain": false,
  "requestId": "req_011Cb1grFkuSYnUNs17fkNBr",
  "type": "assistant",
  "uuid": "d68ee445-640f-4290-9f8c-97ca5d7bb37c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JPhF7PMjuUeUucSVDKMqoM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 40624,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 465,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 143,
          "cache_read_input_tokens": 40624,
          "cache_creation_input_tokens": 465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 465
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

_source line 35 · 2026-05-14T02:40:12.939Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TusqsU99yMbJFAHcZskqD7`</summary>

```json
{
  "query": "register artifact",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d68ee445-640f-4290-9f8c-97ca5d7bb37c",
  "isSidechain": false,
  "requestId": "req_011Cb1grFkuSYnUNs17fkNBr",
  "type": "assistant",
  "uuid": "8de9755e-4dc6-4b73-a61f-af0a49359304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JPhF7PMjuUeUucSVDKMqoM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 40624,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 465,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 143,
          "cache_read_input_tokens": 40624,
          "cache_creation_input_tokens": 465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 465
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

_source line 36 · 2026-05-14T02:40:12.944Z_

<details><summary>↩ Tool result · `toolu_01TusqsU99yMbJFAHcZskqD7`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8de9755e-4dc6-4b73-a61f-af0a49359304",
  "isSidechain": false,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "type": "user",
  "uuid": "1cab1c28-0935-4a5a-ba73-ae3e2a7d8f7b",
  "toolUseResult": {
    "matches": [],
    "query": "register artifact",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "8de9755e-4dc6-4b73-a61f-af0a49359304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T02:40:15.116Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Fpip2yKBWAaX7m5mRE4Vk2`</summary>

```json
{
  "query": "artifact",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cab1c28-0935-4a5a-ba73-ae3e2a7d8f7b",
  "isSidechain": false,
  "requestId": "req_011Cb1grZ7gYFNjbKW429fbs",
  "type": "assistant",
  "uuid": "88d8d1ef-0b2a-413d-8187-b203d48ca568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XQSdizynckRoXJvyUGaCX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 162,
      "cache_read_input_tokens": 41089,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 162,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 41089,
          "cache_creation_input_tokens": 162,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 162
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

_source line 38 · 2026-05-14T02:40:15.123Z_

<details><summary>↩ Tool result · `toolu_01Fpip2yKBWAaX7m5mRE4Vk2`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88d8d1ef-0b2a-413d-8187-b203d48ca568",
  "isSidechain": false,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "type": "user",
  "uuid": "69156040-dbb9-4ca2-b190-09ae3b7c15af",
  "toolUseResult": {
    "matches": [],
    "query": "artifact",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "88d8d1ef-0b2a-413d-8187-b203d48ca568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T02:40:18.210Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016wZLreFxQvhBAiWNPMsfUp`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml",
  "description": "Read manifest to understand artifact registration format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69156040-dbb9-4ca2-b190-09ae3b7c15af",
  "isSidechain": false,
  "requestId": "req_011Cb1griVVSstVczqaWXdV5",
  "type": "assistant",
  "uuid": "8deea3a7-616a-4c64-a19d-219ce7751815",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CxgC5Z1MARKoXiT95qcXM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 90,
      "cache_read_input_tokens": 41251,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 90,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 111,
          "cache_read_input_tokens": 41251,
          "cache_creation_input_tokens": 90,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 90
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

_source line 40 · 2026-05-14T02:40:18.284Z_

<details><summary>↩ Tool result · `toolu_016wZLreFxQvhBAiWNPMsfUp`</summary>

```text
- id: art_20260514_3bc71e
  name: paper_results_summary
  type: report
  description: 'Structured paper results summary: SciERC Phase 2 main table (5 modes),
    DocRED Phase 0 comparison, per-relation DR breakdown, claim-evidence mapping,
    CF root cause analysis, S1/S2 trade-off, pending experiments'
  path: projects/schema_semantic_constrained_ie/artifacts/_project/report/paper_results_summary.md
  url: null
  project: schema_semantic_constrained_ie
  exp_id: null
  skill: ''
  created_at: '2026-05-14T02:32:05.148204+00:00'
  tags:
  - paper
  - results
  - tables
  - emnlp2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8deea3a7-616a-4c64-a19d-219ce7751815",
  "isSidechain": false,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "type": "user",
  "uuid": "8936f6ec-ea5c-42ef-a53f-168af6821709",
  "toolUseResult": {
    "stdout": "- id: art_20260514_3bc71e\n  name: paper_results_summary\n  type: report\n  description: 'Structured paper results summary: SciERC Phase 2 main table (5 modes),\n    DocRED Phase 0 comparison, per-relation DR breakdown, claim-evidence mapping,\n    CF root cause analysis, S1/S2 trade-off, pending experiments'\n  path: projects/schema_semantic_constrained_ie/artifacts/_project/report/paper_results_summary.md\n  url: null\n  project: schema_semantic_constrained_ie\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-14T02:32:05.148204+00:00'\n  tags:\n  - paper\n  - results\n  - tables\n  - emnlp2026",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8deea3a7-616a-4c64-a19d-219ce7751815",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T02:40:26.173Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PPvtN6DKXFfnThQjJEh1Qo`</summary>

```json
{
  "command": "cat >> /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml << 'EOF'\n- id: art_20260514_rw_survey\n  name: related_work_survey\n  type: report\n  description: 'Related Work literature survey for OntoCoDec paper: 5 constraint paradigms\n    (grammar-constrained decoding, vocabulary/type-constrained generation, structural\n    constraints for IE, ontology validation, constrained decoding quality concerns),\n    20+ papers with differentiation analysis and positioning summary'\n  path: projects/schema_semantic_constrained_ie/artifacts/related_work_survey.md\n  url: null\n  project: schema_semantic_constrained_ie\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-14T12:00:00.000000+00:00'\n  tags:\n  - paper\n  - related-work\n  - literature-survey\n  - emnlp2026\nEOF",
  "description": "Register artifact in manifest"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8936f6ec-ea5c-42ef-a53f-168af6821709",
  "isSidechain": false,
  "requestId": "req_011Cb1grwijUL5cbwm9u48c4",
  "type": "assistant",
  "uuid": "5d562293-aef3-4942-8f65-6e225197b94c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkZmfZeGyCezuy7ZEwcv7d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 41341,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 41341,
          "cache_creation_input_tokens": 328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 328
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

_source line 42 · 2026-05-14T02:40:26.230Z_

<details><summary>↩ Tool result · `toolu_01PPvtN6DKXFfnThQjJEh1Qo`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d562293-aef3-4942-8f65-6e225197b94c",
  "isSidechain": false,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "type": "user",
  "uuid": "94880433-13bf-4919-9cb8-09c35e475a30",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5d562293-aef3-4942-8f65-6e225197b94c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 43 · 2026-05-14T02:40:26.244Z_

```json
{
  "parentUuid": "94880433-13bf-4919-9cb8-09c35e475a30",
  "isSidechain": false,
  "attachment": {
    "type": "edited_text_file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml",
    "snippet": "10\t  exp_id: null\n11\t  skill: ''\n12\t  created_at: '2026-05-14T02:32:05.148204+00:00'\n13\t  tags:\n14\t  - paper\n15\t  - results\n16\t  - tables\n17\t  - emnlp2026\n18\t- id: art_20260514_rw_survey\n19\t  name: related_work_survey\n20\t  type: report\n21\t  description: 'Related Work literature survey for OntoCoDec paper: 5 constraint paradigms\n22\t    (grammar-constrained decoding, vocabulary/type-constrained generation, structural\n23\t    constraints for IE, ontology validation, constrained decoding quality concerns),\n24\t    20+ papers with differentiation analysis and positioning summary'\n25\t  path: projects/schema_semantic_constrained_ie/artifacts/related_work_survey.md\n26\t  url: null\n27\t  project: schema_semantic_constrained_ie\n28\t  exp_id: null\n29\t  skill: ''\n30\t  created_at: '2026-05-14T12:00:00.000000+00:00'\n31\t  tags:\n32\t  - paper\n33\t  - related-work\n34\t  - literature-survey\n35\t  - emnlp2026"
  },
  "type": "attachment",
  "uuid": "e75d759c-9443-4398-8e92-26eac165462a",
  "timestamp": "2026-05-14T02:40:26.244Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 44 · 2026-05-14T02:40:41.262Z_

产出文件已写入并注册：
`artifacts/related_work_survey.md`

**覆盖 5 个 paradigm，共 20 篇论文：**

| Paradigm | 论文数 | 代表工作 |
|----------|--------|----------|
| Grammar-constrained decoding | 5 | XGrammar (MLSys'25), Outlines, LMQL (PLDI'23), DOMINO (ICML'24), ASAp (NeurIPS'24) |
| Vocabulary/type-constrained generation | 4 | GENRE (ICLR'21), GenIE (NAACL'22), NeuroLogic (NAACL'21), GCD (EMNLP'23) |
| Structural constraints for IE | 5 | UIE (ACL'22), GoLLIE (ICLR'24), CodeIE (ACL'23), InstructUIE, ADELIE (EMNLP'24) |
| Ontology validation | 4 | ODKE+ (Apple'25), OpenIE w/ entity constraints (EACL'23), EnriCo, KG validation (GenAIK'25) |
| Constrained decoding quality | 4 | Let Me Speak Freely (EMNLP'24), CRANE (ICML'25), Structure Snowballing, Hidden Cost (RANLP'25) |

**OntoCoDec 定位总结（3 个差异化维度）：**
1. **约束层次**：从格式（grammar）扩展到语义（domain/range）
2. **执行时机**：decoding-time preventive enforcement vs post-hoc validation / training-time soft guidance
3. **质量保持**：F1 无损 + S2 两通道策略符合 CRANE 的 alternating approach 理论

注意：CRANE 实际是 ICML 2025 而非 NeurIPS 2024，已在文档中修正。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e75d759c-9443-4398-8e92-26eac165462a",
  "isSidechain": false,
  "requestId": "req_011Cb1gsXiNsj2ouWqB8dqr8",
  "type": "assistant",
  "uuid": "ab22bee1-b0e4-4ba7-8461-bd968e406be7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UesnJ2pEhqHs9YvHxtRD2e",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 41669,
      "output_tokens": 521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 521,
          "cache_read_input_tokens": 41669,
          "cache_creation_input_tokens": 790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 790
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

_source line 45_

```json
{
  "type": "last-prompt",
  "leafUuid": "ab22bee1-b0e4-4ba7-8461-bd968e406be7",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey for OntoCoDec related work",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909"
}
```

---
