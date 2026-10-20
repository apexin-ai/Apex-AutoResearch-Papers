# Research conversation: <project_context> # 项目: gen-depth-contamination ## 运行环境 - 服务器名: cqa1-22115 - SSH 账户: root（调用 ssh_execute / submit_traini

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/99cf8106-e8a7-456c-8eba-4cb2eb8f94c0.jsonl`
- **Structured JSON:** [`de962546394927710970.json`](../../sessions/de/de962546394927710970.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-23T07:55:44.935Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T07:55:44.935Z",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "content": "&lt;project_context>\n# 项目: gen-depth-contamination\n\n## 运行环境\n- 服务器名: cqa1-22115\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh cqa1-22115  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/gen-depth-contamination\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n编译论文并验证 Pythia-1.4B AUC 数据一致性。\n\n步骤：\n1. cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper\n2. latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -20\n3. 确认 0 errors\n\n4. 验证数据一致性——检查这两个表的 Pythia 列是否完全一致：\n   - 打开 experiments_c1.tex，找 Table 2（tab:kstar_ci），记录 Pythia 列所有值\n   - 打开 appendix.tex，找 Table 10（tab:kstar_ci_extended），记录 Pythia 列所有值\n   - 逐行比对，确认 0v1, 1v2, 2v3, 3v4, 4v5 五行完全一致\n   - 特别确认：0v1=.9722, 1v2=.6074, 2v3=.5440, 3v4=.5051, 4v5=.5079\n\n5. 同时确认 Table 2 的 CI 与 Table 10 的 CI 一致（1v2 CI 和 2v3 CI）\n\n6. 确认页数仍为 8 页正文\n\n汇报：编译状态 + 数据一致性检查结果 + 页数。"
}
```

---

### Runtime record

_source line 2 · 2026-05-23T07:55:44.938Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T07:55:44.938Z",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-23T07:55:44.969Z_

&lt;project_context>
# 项目: gen-depth-contamination

## 运行环境
- 服务器名: cqa1-22115
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh cqa1-22115  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/gen-depth-contamination


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
编译论文并验证 Pythia-1.4B AUC 数据一致性。

步骤：
1. cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper
2. latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -20
3. 确认 0 errors

4. 验证数据一致性——检查这两个表的 Pythia 列是否完全一致：
   - 打开 experiments_c1.tex，找 Table 2（tab:kstar_ci），记录 Pythia 列所有值
   - 打开 appendix.tex，找 Table 10（tab:kstar_ci_extended），记录 Pythia 列所有值
   - 逐行比对，确认 0v1, 1v2, 2v3, 3v4, 4v5 五行完全一致
   - 特别确认：0v1=.9722, 1v2=.6074, 2v3=.5440, 3v4=.5051, 4v5=.5079

5. 同时确认 Table 2 的 CI 与 Table 10 的 CI 一致（1v2 CI 和 2v3 CI）

6. 确认页数仍为 8 页正文

汇报：编译状态 + 数据一致性检查结果 + 页数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "55d142f3-1246-4ea6-885d-cf2788d25a6d",
  "type": "user",
  "uuid": "63cff382-c4a1-4b92-9131-361d08ea85d9",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-23T07:55:44.969Z_

```json
{
  "parentUuid": "63cff382-c4a1-4b92-9131-361d08ea85d9",
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "cf087a9e-3efb-4d25-baab-de47d6b85149",
  "timestamp": "2026-05-23T07:55:44.969Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-23T07:55:44.969Z_

```json
{
  "parentUuid": "cf087a9e-3efb-4d25-baab-de47d6b85149",
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
  "uuid": "9b8e9a8a-3ee3-47b0-9733-0a530b7a2787",
  "timestamp": "2026-05-23T07:55:44.969Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-23T07:55:44.969Z_

```json
{
  "parentUuid": "9b8e9a8a-3ee3-47b0-9733-0a530b7a2787",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "edd18f07-c164-4b40-8c08-6a309ec93590",
  "timestamp": "2026-05-23T07:55:44.969Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
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
  "aiTitle": "Compile paper and verify Pythia AUC consistency",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0"
}
```

---

### Assistant

_source line 8 · 2026-05-23T07:55:47.972Z_

I'll compile the paper and verify data consistency. Let me start by reading the relevant files and compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edd18f07-c164-4b40-8c08-6a309ec93590",
  "isSidechain": false,
  "requestId": "req_011CbK9CMS7egKXUAtqvcJNa",
  "type": "assistant",
  "uuid": "bffb7648-5643-467e-86c4-6c56b5d30019",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LtCdPTSG4aYShgCiw75uCZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12003,
      "cache_read_input_tokens": 11841,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12003,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 298,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12003
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

_source line 9 · 2026-05-23T07:55:49.080Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01S7snHYr3LSc4hJxxZQhWjG`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bffb7648-5643-467e-86c4-6c56b5d30019",
  "isSidechain": false,
  "requestId": "req_011CbK9CMS7egKXUAtqvcJNa",
  "type": "assistant",
  "uuid": "2aec6618-83ca-4654-8862-aee394204350",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LtCdPTSG4aYShgCiw75uCZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12003,
      "cache_read_input_tokens": 11841,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12003,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 298,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12003
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

_source line 10 · 2026-05-23T07:55:49.452Z_

<details open><summary>🔧 Tool call — Read · `toolu_017qLpkcjGRnFXetohFzNh1y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2aec6618-83ca-4654-8862-aee394204350",
  "isSidechain": false,
  "requestId": "req_011CbK9CMS7egKXUAtqvcJNa",
  "type": "assistant",
  "uuid": "ae496d44-5e34-49cd-9f16-9c6d6620bb24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LtCdPTSG4aYShgCiw75uCZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12003,
      "cache_read_input_tokens": 11841,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12003,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 298,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12003
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

_source line 11 · 2026-05-23T07:55:50.194Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RtbgsMN38hWdnNZLiPEunL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae496d44-5e34-49cd-9f16-9c6d6620bb24",
  "isSidechain": false,
  "requestId": "req_011CbK9CMS7egKXUAtqvcJNa",
  "type": "assistant",
  "uuid": "78afd710-d9ff-4d58-943d-62adb30fe47a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LtCdPTSG4aYShgCiw75uCZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12003,
      "cache_read_input_tokens": 11841,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12003,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 298,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12003
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

_source line 12 · 2026-05-23T07:55:50.740Z_

<details><summary>↩ Tool result · `toolu_01S7snHYr3LSc4hJxxZQhWjG`</summary>

```text
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam7.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur
w/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (18 pages, 554399 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2aec6618-83ca-4654-8862-aee394204350",
  "isSidechain": false,
  "promptId": "55d142f3-1246-4ea6-885d-cf2788d25a6d",
  "type": "user",
  "uuid": "573d9a25-375a-4037-af4d-90b787e0e6e8",
  "toolUseResult": {
    "stdout": "r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam7.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur\nw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (18 pages, 554399 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2aec6618-83ca-4654-8862-aee394204350",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-23T07:55:50.750Z_

<details><summary>↩ Tool result · `toolu_017qLpkcjGRnFXetohFzNh1y`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on ten model configurations spanning six architecture families:
5	Pythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{$\Kempirical \leq 2$ Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\resizebox{\textwidth}{!}{%
20	\begin{tabular}{lcccccccccc}
21	\toprule
22	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
23	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
24	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
25	\midrule
26	0v1 & .9956 & & .9722 & & .9860 & & .9971 & & .9638 & [.961,\,.967] \\
27	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6074 & [.598,\,.617]\rlap{$^*$} & .5001 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
28	2v3 & .5893 & [.580,\,.599] & .5440 & [.534,\,.554] & .4973 & [.486,\,.509] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
29	3v4 & .5435 & & .5051 & & .5024\rlap{$^\S$} & & .5409 & & .5276 & \\
30	4v5 & .5340 & & .5079 & & .4942 & & .5141 & & .5085 & \\
31	\bottomrule
32	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all starred boundary comparisons ($\auc > \theta$).} \\
33	\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\
34	\multicolumn{11}{l}{\footnotesize $^\S$OLMo 2v3 (0.497) $<$ 3v4 (0.502): non-monotonic reversal within noise ($\Delta = 0.005$).} \\
35	\multicolumn{11}{l}{\footnotesize Full results for all 10 configurations (including LLaMA-8B, Mistral-7B, Qwen-base, Gemma-2-2B, and Pythia-6.9B) in Table~\ref{tab:kstar_ci_extended}.}
36	\end{tabular}}
37	\end{table*}
38	
39	\begin{figure}[t]
40	\centering
41	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
42	\caption{Pairwise $\auc$ decay across adjacent depth pairs (0v1, 1v2, \ldots, 4v5) for model-mode configurations (solid) and decoding strategies (dashed); shaded bands show bootstrap 95\% confidence intervals. The horizontal dashed line marks $\theta = 0.60$.}
43	\label{fig:auc_decay}
44	\end{figure}
45	
46	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 10 configurations: 6/10 yield $\Kempirical{=}2$ (Qwen$\times$4, LLaMA-8B, Pythia-1.4B; 1v2 $\auc$: 0.607--0.696; $p < 0.001$), while OLMo-1B, Mistral-7B, Pythia-6.9B, and Gemma-2-2B yield $\Kempirical{=}1$ (1v2 $\auc$: 0.500--0.598; Section~\ref{sec:boundary_cases}).
47	Under Bonferroni correction (99.5\% CIs), three of six $\Kempirical{=}2$ configurations retain significance; the three marginal cases (Pythia-1.4B, Qwen-cont, LLaMA-8B; CI lower bounds 0.593--0.599) reflect narrow effect sizes rather than classification failure.
48	By architecture family: Qwen (4/4) and LLaMA (1/1) yield $\Kempirical{\geq}2$ at nominal significance; OLMo (1/1), Mistral (1/1), and Gemma (1/1) yield $\Kempirical{=}1$; Pythia exhibits a scale-dependent split (1.4B: $\Kempirical{=}2$, 6.9B: $\Kempirical{=}1$).
49	LLaMA-3.1-8B confirms $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123\;[0.603,\,0.622]$; CI lower bound above $\theta$; Table~\ref{tab:kstar_ci_extended}).
50	All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
51	The 1v2 spread due to generation mode ($\Delta = 8.4$\,pp within Qwen) exceeds the spread across $\Kempirical{=}2$ continuation models ($\Delta = 1.9$\,pp).
52	
53	\paragraph{Scale and instruction-tuning invariance.}
54	$\Kempirical{=}2$ persists from 1.5B through 8B: Qwen-7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\auc = 0.6123$) both exceed $\theta$, despite progressively reduced 0v1 signal (0.9638 and 0.9225 vs.\ $> 0.99$ at $\leq$1.5B).
55	A base-vs.-instruct ablation at 1.5B likewise yields $\Kempirical = 2$ (1v2 $\auc = 0.626$), confirming the boundary is not an instruction-tuning artifact.
56	
57	\begin{figure*}[t]
58	\centering
59	\includegraphics[width=0.75\textwidth]{figures/fig_kstar_theta.pdf}
60	\caption{$\Kempirical(\theta)$ sensitivity curve for five configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. Four of five configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line); OLMo yields $\Kempirical{=}1$. At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
61	\label{fig:kstar_theta}
62	\end{figure*}
63	
64	Figure~\ref{fig:kstar_theta} displays the sensitivity surface across $\theta \in [0.55, 0.70]$: five of six configurations yield $\Kempirical = 2$ within $\theta \in [0.51, 0.61]$ (OLMo: $\Kempirical = 1$ throughout); at $\theta{=}0.55$, two Qwen configurations reach $\Kempirical = 3$; at $\theta{=}0.70$, all drop to $\Kempirical = 1$.
65	
66	%% ====================================================================
67	\subsection{Cross-Model Transfer}
68	\label{sec:transfer}
69	
70	\begin{figure}[t]
71	\centering
72	\includegraphics[width=\columnwidth]{figures/fig3_transfer_heatmap.pdf}
73	\caption{Cross-model transfer heatmap (continuation-mode models). Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\leftrightarrow$OLMo: 90--92\%.}
74	\label{fig:transfer_heatmap}
75	\end{figure}
76	
77	Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
78	Qwen-rewrite classifiers transfer poorly (61--63\%), confirming reliance on mode-specific artifacts rather than generalizable depth features.
79	
80	\paragraph{Cross-scorer validation.}
81	Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\ref{tab:crossscorer}).
82	Feature ranking independence is a strong result: the same features dominate under all scorers.
83	$\Kempirical$ agreement, however, is signal-strength dependent: Qwen-rewrite (strong signal, 1v2 $\auc = 0.696$) retains $\Kempirical{=}2$ under all scorers, but Qwen-continuation (marginal, 1v2 $\auc = 0.611$, only 0.011 above $\theta$) drops to $\Kempirical{=}1$ (Pythia: $0.5923$; OLMo: $0.5858$).
84	A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; Table~\ref{tab:anova_crossscorer}) confirms a statistically significant but modest Scorer main effect ($\eta^2_p{=}.166$, $p < .001$) and a significant Generator$\times$Scorer interaction ($\eta^2_p{=}.146$), indicating that absolute AUC values are scorer-dependent even when $\Kempirical$ classifications largely agree.
85	
86	%% ====================================================================
87	\subsection{Feature Ordering and Generation Mode}
88	\label{sec:feature_degradation}
89	\label{sec:generation_mode}
90	
91	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
92	The top-3 features (\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability.
93	Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
94	Within Qwen, rewrite yields 1v2 $\auc = 0.6955$ vs.\ continuation's $0.6112$ ($\Delta = +8.4$\,pp); continuation mode is therefore recommended as the canonical condition.
95	
96	%% ====================================================================
97	\subsection{Neural Probe}
98	\label{sec:neural_probe}
99	
100	Replacing the 15D features with frozen encoder hidden states (MLP probe; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia remains at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3} = 0.5963$); OLMo yields $\Kempirical^{\text{neural}} = 1$ (1v2 $\auc = 0.5054$, consistent with its 15D boundary).
101	We hypothesize that the Qwen-only elevation reflects self-familiarity artifacts, consistent with the poor transfer observed in Section~\ref{sec:transfer}; the 15D features yield $\Kempirical = 2$ for most families (OLMo: $\Kempirical = 1$).
102	
103	\noindent\begin{minipage}{\columnwidth}
104	\centering
105	\footnotesize
106	\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $\Kempirical^{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
107	\label{tab:neural_probe_crossmodel}
108	\resizebox{\columnwidth}{!}{%
109	\begin{tabular}{lccc}
110	\toprule
111	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
112	\midrule
113	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
114	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
115	OLMo-1B    & 0.5056 & $[0.497,\,0.516]$ & 1\rlap{$^\dagger$} \\
116	\bottomrule
117	\multicolumn{4}{l}{\footnotesize $^\dagger$OLMo 1v2 $\auc = 0.5054$ (below $\theta$); $\Kempirical^{\text{neural}} = 1$.}
118	\end{tabular}}
119	\end{minipage}
120	
121	%% ====================================================================
122	\subsection{Cross-Domain Variation}
123	\label{sec:cross_domain}
124	
125	The preceding experiments use C4 (general web text).
126	To test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) across three architecture families.
127	Wikipedia yields $\Kempirical{=}2$ (1v2 $\auc = 0.623$, 2v3 $\auc = 0.571$), matching the C4 baseline.
128	Qwen-1.5B, Pythia-1.4B, and LLaMA-3.1-8B yield $\Kempirical{=}3$ for arXiv (Table~\ref{tab:domain_kstar}): 2v3 $\auc = 0.644\;[0.628,\,0.658]$, $0.655\;[0.640,\,0.669]$, and $0.620\;[0.605,\,0.635]$ respectively (bootstrap CI lower bounds above $\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.
129	The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.
130	We additionally evaluate on CodeSearchNet Python ($n{=}5{,}000$, continuation mode); all four tested models (Qwen-1.5B, Qwen-7B, LLaMA-8B, Mistral-7B) yield $\Kempirical{=}2$ (Table~\ref{tab:domain_kstar}), matching the C4 baseline.
131	
132	\begin{table}[t]
133	\centering
134	\footnotesize
135	\caption{Cross-domain $\Kempirical$ comparison. $\Kempirical{=}2$ for C4, Wikipedia, and Code; $\Kempirical{=}3$ for arXiv (three families confirmed in text; representative rows shown).}
136	\label{tab:domain_kstar}
137	\resizebox{\columnwidth}{!}{%
138	\begin{tabular}{llccc}
139	\toprule
140	\textbf{Domain} & \textbf{Model} & \textbf{1v2 $\auc$} & \textbf{2v3 $\auc$} & $\Kempirical$ \\
141	\midrule
142	arXiv & Qwen-1.5B  & .858 & .644 & 3 \\
143	arXiv & Pythia-1.4B & .805 & .655 & 3 \\
144	C4    & Qwen-1.5B  & .630 & .560 & 2 \\
145	Wiki  & Qwen-1.5B  & .620 & .550 & 2 \\
146	Code  & Qwen-1.5B  & .738 & .530 & 2 \\
147	Code  & LLaMA-8B   & .739 & .510 & 2 \\
148	\bottomrule
149	\end{tabular}}
150	\end{table}
151	
152	\paragraph{Robustness.}
153	\label{sec:robustness}
154	$\Kempirical{=}2$ holds across segment lengths of 128, 256, and 512 tokens (Table~\ref{tab:s11_length_ablation}); at 512 tokens the 1v2 CI lower bound falls marginally below $\theta$ but 2v3 remains well below $\theta$ at all lengths ($\leq 0.572$).
155	Seed robustness testing (seed $= 123$ vs.\ primary $= 42$; Table~\ref{tab:seed_robustness}) confirms $\Kempirical$ stability in 2/3 configurations; the one marginal shift (Qwen-Wikipedia $\Kempirical{=}2 \to 3$, 2v3 $\auc = 0.607$) has one of five folds below $\theta$.
156	The ${\pm}9$\,pp absolute AUC variation across seeds strengthens the case for threshold-based $\Kempirical$ over raw AUC comparisons.
157	
158	%% ====================================================================
159	\subsection{Binary Detector Confidence}
160	\label{sec:binary_confidence}
161	
162	Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) remain effective for human-vs.-machine classification but provide no usable depth signal beyond this binary boundary.
163	Pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$; moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) are driven entirely by the 0v1 gap rather than fine-grained depth discrimination, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
164	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae496d44-5e34-49cd-9f16-9c6d6620bb24",
  "isSidechain": false,
  "promptId": "55d142f3-1246-4ea6-885d-cf2788d25a6d",
  "type": "user",
  "uuid": "9793b01f-1641-4ecd-b67c-f5ec1a4837d3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate generational depth estimation on ten model configurations spanning six architecture families:\nPythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).\n\n%% ====================================================================\n\\subsection{$\\Kempirical \\leq 2$ Across Model Configurations (C4)}\n\\label{sec:kstar_boundary}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs with bootstrap 95\\% CIs and permutation $p$-values for boundary rows.\n$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.\nExtended results (all models) in Table~\\ref{tab:kstar_ci_extended}.}\n\\label{tab:kstar_ci}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{lcccccccccc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\n & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & .9956 & & .9722 & & .9860 & & .9971 & & .9638 & [.961,\\,.967] \\\\\n1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6074 & [.598,\\,.617]\\rlap{$^*$} & .5001 & [.496,\\,.519] & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} \\\\\n2v3 & .5893 & [.580,\\,.599] & .5440 & [.534,\\,.554] & .4973 & [.486,\\,.509] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] \\\\\n3v4 & .5435 & & .5051 & & .5024\\rlap{$^\\S$} & & .5409 & & .5276 & \\\\\n4v5 & .5340 & & .5079 & & .4942 & & .5141 & & .5085 & \\\\\n\\bottomrule\n\\multicolumn{11}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all starred boundary comparisons ($\\auc > \\theta$).} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\S$OLMo 2v3 (0.497) $<$ 3v4 (0.502): non-monotonic reversal within noise ($\\Delta = 0.005$).} \\\\\n\\multicolumn{11}{l}{\\footnotesize Full results for all 10 configurations (including LLaMA-8B, Mistral-7B, Qwen-base, Gemma-2-2B, and Pythia-6.9B) in Table~\\ref{tab:kstar_ci_extended}.}\n\\end{tabular}}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\n\\caption{Pairwise $\\auc$ decay across adjacent depth pairs (0v1, 1v2, \\ldots, 4v5) for model-mode configurations (solid) and decoding strategies (dashed); shaded bands show bootstrap 95\\% confidence intervals. The horizontal dashed line marks $\\theta = 0.60$.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:kstar_ci} and Figure~\\ref{fig:auc_decay} show $\\Kempirical \\leq 2$ across all 10 configurations: 6/10 yield $\\Kempirical{=}2$ (Qwen$\\times$4, LLaMA-8B, Pythia-1.4B; 1v2 $\\auc$: 0.607--0.696; $p < 0.001$), while OLMo-1B, Mistral-7B, Pythia-6.9B, and Gemma-2-2B yield $\\Kempirical{=}1$ (1v2 $\\auc$: 0.500--0.598; Section~\\ref{sec:boundary_cases}).\nUnder Bonferroni correction (99.5\\% CIs), three of six $\\Kempirical{=}2$ configurations retain significance; the three marginal cases (Pythia-1.4B, Qwen-cont, LLaMA-8B; CI lower bounds 0.593--0.599) reflect narrow effect sizes rather than classification failure.\nBy architecture family: Qwen (4/4) and LLaMA (1/1) yield $\\Kempirical{\\geq}2$ at nominal significance; OLMo (1/1), Mistral (1/1), and Gemma (1/1) yield $\\Kempirical{=}1$; Pythia exhibits a scale-dependent split (1.4B: $\\Kempirical{=}2$, 6.9B: $\\Kempirical{=}1$).\nLLaMA-3.1-8B confirms $\\Kempirical{=}2$ (0v1 $\\auc = 0.9225$, 1v2 $\\auc = 0.6123\\;[0.603,\\,0.622]$; CI lower bound above $\\theta$; Table~\\ref{tab:kstar_ci_extended}).\nAll four decoding strategies likewise yield $\\Kempirical{=}2$ (Table~\\ref{tab:s2_decoding}).\nThe 1v2 spread due to generation mode ($\\Delta = 8.4$\\,pp within Qwen) exceeds the spread across $\\Kempirical{=}2$ continuation models ($\\Delta = 1.9$\\,pp).\n\n\\paragraph{Scale and instruction-tuning invariance.}\n$\\Kempirical{=}2$ persists from 1.5B through 8B: Qwen-7B (1v2 $\\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\\auc = 0.6123$) both exceed $\\theta$, despite progressively reduced 0v1 signal (0.9638 and 0.9225 vs.\\ $> 0.99$ at $\\leq$1.5B).\nA base-vs.-instruct ablation at 1.5B likewise yields $\\Kempirical = 2$ (1v2 $\\auc = 0.626$), confirming the boundary is not an instruction-tuning artifact.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/fig_kstar_theta.pdf}\n\\caption{$\\Kempirical(\\theta)$ sensitivity curve for five configurations. $\\Kempirical$: maximum discriminable depth; $\\theta$: AUC decision threshold. Four of five configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (dashed line); OLMo yields $\\Kempirical{=}1$. At $\\theta{=}0.70$, all drop to $\\Kempirical{=}1$.}\n\\label{fig:kstar_theta}\n\\end{figure*}\n\nFigure~\\ref{fig:kstar_theta} displays the sensitivity surface across $\\theta \\in [0.55, 0.70]$: five of six configurations yield $\\Kempirical = 2$ within $\\theta \\in [0.51, 0.61]$ (OLMo: $\\Kempirical = 1$ throughout); at $\\theta{=}0.55$, two Qwen configurations reach $\\Kempirical = 3$; at $\\theta{=}0.70$, all drop to $\\Kempirical = 1$.\n\n%% ====================================================================\n\\subsection{Cross-Model Transfer}\n\\label{sec:transfer}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n\\caption{Cross-model transfer heatmap (continuation-mode models). Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\\leftrightarrow$OLMo: 90--92\\%.}\n\\label{fig:transfer_heatmap}\n\\end{figure}\n\nContinuation-mode classifiers transfer well across generators (Figure~\\ref{fig:transfer_heatmap}; full matrix in Table~\\ref{tab:s1_transfer}): Pythia$\\leftrightarrow$OLMo retains 90--92\\%, Qwen-cont$\\leftrightarrow$Pythia 84--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\% (0v1 cross-model $\\auc > 0.96$ for all pairs).\nQwen-rewrite classifiers transfer poorly (61--63\\%), confirming reliance on mode-specific artifacts rather than generalizable depth features.\n\n\\paragraph{Cross-scorer validation.}\nReplacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\\ref{tab:crossscorer}).\nFeature ranking independence is a strong result: the same features dominate under all scorers.\n$\\Kempirical$ agreement, however, is signal-strength dependent: Qwen-rewrite (strong signal, 1v2 $\\auc = 0.696$) retains $\\Kempirical{=}2$ under all scorers, but Qwen-continuation (marginal, 1v2 $\\auc = 0.611$, only 0.011 above $\\theta$) drops to $\\Kempirical{=}1$ (Pythia: $0.5923$; OLMo: $0.5858$).\nA three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair; Table~\\ref{tab:anova_crossscorer}) confirms a statistically significant but modest Scorer main effect ($\\eta^2_p{=}.166$, $p < .001$) and a significant Generator$\\times$Scorer interaction ($\\eta^2_p{=}.146$), indicating that absolute AUC values are scorer-dependent even when $\\Kempirical$ classifications largely agree.\n\n%% ====================================================================\n\\subsection{Feature Ordering and Generation Mode}\n\\label{sec:feature_degradation}\n\\label{sec:generation_mode}\n\nAmong continuation-mode models, single-feature $\\auc$ rankings are highly correlated ($\\rho \\geq 0.85$; Table~\\ref{tab:top_features}).\nThe top-3 features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability.\nQwen-rewrite diverges (\\texttt{freq\\_entropy} dominates), consistent with its poor cross-model transfer (61--63\\%).\nWithin Qwen, rewrite yields 1v2 $\\auc = 0.6955$ vs.\\ continuation's $0.6112$ ($\\Delta = +8.4$\\,pp); continuation mode is therefore recommended as the canonical condition.\n\n%% ====================================================================\n\\subsection{Neural Probe}\n\\label{sec:neural_probe}\n\nReplacing the 15D features with frozen encoder hidden states (MLP probe; Table~\\ref{tab:neural_probe_crossmodel}), Qwen achieves $\\Kempirical^{\\text{neural}} = 3$ (2v3 $\\auc = 0.6159$), while Pythia remains at $\\Kempirical^{\\text{neural}} = 2$ ($\\auc_{2v3} = 0.5963$); OLMo yields $\\Kempirical^{\\text{neural}} = 1$ (1v2 $\\auc = 0.5054$, consistent with its 15D boundary).\nWe hypothesize that the Qwen-only elevation reflects self-familiarity artifacts, consistent with the poor transfer observed in Section~\\ref{sec:transfer}; the 15D features yield $\\Kempirical = 2$ for most families (OLMo: $\\Kempirical = 1$).\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\\ $d{+}1$ text. $\\Kempirical^{\\text{neural}}$: maximum depth where AUC exceeds $\\theta = 0.60$.}\n\\label{tab:neural_probe_crossmodel}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & $\\Kempirical^{\\text{neural}}$ \\\\\n\\midrule\nQwen-1.5B  & 0.6159 & $[0.610,\\,0.622]$ & 3 \\\\\nPythia-1.4B & 0.5963 & $[0.589,\\,0.603]$ & 2 \\\\\nOLMo-1B    & 0.5056 & $[0.497,\\,0.516]$ & 1\\rlap{$^\\dagger$} \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$OLMo 1v2 $\\auc = 0.5054$ (below $\\theta$); $\\Kempirical^{\\text{neural}} = 1$.}\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Cross-Domain Variation}\n\\label{sec:cross_domain}\n\nThe preceding experiments use C4 (general web text).\nTo test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) across three architecture families.\nWikipedia yields $\\Kempirical{=}2$ (1v2 $\\auc = 0.623$, 2v3 $\\auc = 0.571$), matching the C4 baseline.\nQwen-1.5B, Pythia-1.4B, and LLaMA-3.1-8B yield $\\Kempirical{=}3$ for arXiv (Table~\\ref{tab:domain_kstar}): 2v3 $\\auc = 0.644\\;[0.628,\\,0.658]$, $0.655\\;[0.640,\\,0.669]$, and $0.620\\;[0.605,\\,0.635]$ respectively (bootstrap CI lower bounds above $\\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.\nThe elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\\ ${\\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.\nWe additionally evaluate on CodeSearchNet Python ($n{=}5{,}000$, continuation mode); all four tested models (Qwen-1.5B, Qwen-7B, LLaMA-8B, Mistral-7B) yield $\\Kempirical{=}2$ (Table~\\ref{tab:domain_kstar}), matching the C4 baseline.\n\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\caption{Cross-domain $\\Kempirical$ comparison. $\\Kempirical{=}2$ for C4, Wikipedia, and Code; $\\Kempirical{=}3$ for arXiv (three families confirmed in text; representative rows shown).}\n\\label{tab:domain_kstar}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Model} & \\textbf{1v2 $\\auc$} & \\textbf{2v3 $\\auc$} & $\\Kempirical$ \\\\\n\\midrule\narXiv & Qwen-1.5B  & .858 & .644 & 3 \\\\\narXiv & Pythia-1.4B & .805 & .655 & 3 \\\\\nC4    & Qwen-1.5B  & .630 & .560 & 2 \\\\\nWiki  & Qwen-1.5B  & .620 & .550 & 2 \\\\\nCode  & Qwen-1.5B  & .738 & .530 & 2 \\\\\nCode  & LLaMA-8B   & .739 & .510 & 2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Robustness.}\n\\label{sec:robustness}\n$\\Kempirical{=}2$ holds across segment lengths of 128, 256, and 512 tokens (Table~\\ref{tab:s11_length_ablation}); at 512 tokens the 1v2 CI lower bound falls marginally below $\\theta$ but 2v3 remains well below $\\theta$ at all lengths ($\\leq 0.572$).\nSeed robustness testing (seed $= 123$ vs.\\ primary $= 42$; Table~\\ref{tab:seed_robustness}) confirms $\\Kempirical$ stability in 2/3 configurations; the one marginal shift (Qwen-Wikipedia $\\Kempirical{=}2 \\to 3$, 2v3 $\\auc = 0.607$) has one of five folds below $\\theta$.\nThe ${\\pm}9$\\,pp absolute AUC variation across seeds strengthens the case for threshold-based $\\Kempirical$ over raw AUC comparisons.\n\n%% ====================================================================\n\\subsection{Binary Detector Confidence}\n\\label{sec:binary_confidence}\n\nBinary detectors (DivEye~\\cite{basani2026diveye}, Binoculars~\\cite{hans2024binoculars}) remain effective for human-vs.-machine classification but provide no usable depth signal beyond this binary boundary.\nPairwise $\\auc$ yields $\\Kempirical^{\\text{binary}} \\leq 1$; moderate rank correlations with depth ($|\\rho| = 0.06$--$0.46$; Table~\\ref{tab:s9_binary_spearman}) are driven entirely by the 0v1 gap rather than fine-grained depth discrimination, and multiple conditions exhibit non-monotonic AUC at deeper pairs.\n",
      "numLines": 164,
      "startLine": 1,
      "totalLines": 164
    }
  },
  "sourceToolAssistantUUID": "ae496d44-5e34-49cd-9f16-9c6d6620bb24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T07:55:50.754Z_

<details><summary>↩ Tool result · `toolu_01RtbgsMN38hWdnNZLiPEunL`</summary>

```text
1	\appendix
2	\section{Supplementary Materials}
3	\label{sec:appendix}
4	
5	This appendix provides supplementary figures, detailed experimental tables, dataset statistics, and complete feature descriptions referenced in the main text.
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
10	\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
11	\label{fig:filtering_strategies}
12	\end{figure}
13	
14	\paragraph{Feature ranking and cross-model consistency.}
15	Table~\ref{tab:top_features} reports per-model single-feature AUC rankings.
16	Surprisal derivative features (\texttt{surp\_d1\_std}, \texttt{surp\_d2\_std}) consistently rank among the top three across all continuation-mode models (Pythia, OLMo, Qwen-cont), with pairwise Spearman $\rho \geq 0.85$.
17	The rewrite-mode model (Qwen-rw) diverges by placing \texttt{freq\_entropy} first, reflecting a distributional shift that is lexical rather than surprisal-driven.
18	This scorer-invariant ranking supports the use of a fixed 15-dimensional feature set across generators without per-model feature selection.
19	
20	%%% Feature ranking table (moved from main text)
21	\begin{table}[!htbp]
22	\centering
23	\small
24	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
25	\label{tab:top_features}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{cllll}
28	\toprule
29	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
30	\midrule
31	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
32	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
33	3 & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_d2\_std}} \\
34	\bottomrule
35	\end{tabular}
36	}
37	\end{table}
38	
39	Table~\ref{tab:s1_transfer} reports the cross-model transfer accuracy matrix.
40	Classifiers trained on continuation-mode generators (Pythia, OLMo, Qwen-cont) transfer well to each other, with off-diagonal accuracy retaining 80--92\% of in-distribution performance.
41	The asymmetry between rewrite-mode and continuation-mode transfer (61--63\%) confirms that generation mode, rather than model family, is the primary axis of distributional variation (Section~\ref{sec:discussion}).
42	
43	%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
44	\begin{table}[!htbp]
45	  \centering
46	  \small
47	  \caption{Cross-model transfer accuracy matrix. Diagonal (\textbf{bold}): within-model; off-diagonal: cross-model. Retention: Pythia$\leftrightarrow$OLMo 91--92\%, Qwen-cont$\leftrightarrow$Pythia 83--85\%, Qwen-rw$\to$others 61--63\%.}
48	  \label{tab:s1_transfer}
49	  \resizebox{\columnwidth}{!}{%
50	  \begin{tabular}{lcccc}
51	    \toprule
52	    \textbf{Train} & Qwen-rw & Pythia & OLMo & Qwen-cont \\
53	    \midrule
54	    Qwen-rw   & \textbf{.423} & .259 & .265 & .347 \\
55	    Pythia    & .272 & \textbf{.386} & .353 & .329 \\
56	    OLMo      & .277 & .345 & \textbf{.382} & .324 \\
57	    Qwen-cont & .344 & .328 & .311 & \textbf{.388} \\
58	    \bottomrule
59	  \end{tabular}}
60	\end{table}
61	
62	\paragraph{Dataset construction.}
63	Table~\ref{tab:s4_dataset_stats} summarizes the generational depth corpus.
64	Each depth level contains 5{,}000 passages, yielding 30{,}000 total samples across six depths (0--5).
65	Depth~0 consists of human-written seed texts from the C4 English validation split, truncated to 256 subword tokens.
66	Subsequent depths are generated recursively: each depth-$k$ passage is produced by prompting the generator with the corresponding depth-$(k{-}1)$ passage.
67	The four model-mode configurations (Qwen-rw, Pythia-cont, OLMo-cont, Qwen-cont) share identical depth-0 seeds and generation pipeline, differing only in generator identity and prompting strategy (rewrite vs.\ continuation).
68	
69	%%% Table S4: Dataset Statistics
70	\begin{table}[!htbp]
71	  \centering
72	  \small
73	  \caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}
74	  \label{tab:s4_dataset_stats}
75	  \resizebox{\columnwidth}{!}{%
76	  \begin{tabular}{clrl}
77	    \toprule
78	    \textbf{Depth} & \textbf{$N$ samples} & \textbf{Mean tokens} & \textbf{Source} \\
79	    \midrule
80	    0 & 5{,}000 & 147.8 & C4 validation (human) \\
81	    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\
82	    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\
83	    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\
84	    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
85	    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
86	    \midrule
87	    \multicolumn{2}{l}{Total} & \multicolumn{2}{l}{30{,}000 samples} \\
88	    \bottomrule
89	  \end{tabular}}
90	\end{table}
91	
92	%%% Table S2: Decoding Ablation AUC (exp-003)
93	\begin{table*}[t]
94	  \centering
95	  \caption{Pairwise AUC with bootstrap 95\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\,vs.\,2 and 2\,vs.\,3 marks the empirical detectability boundary $\Kempirical=2$. Bottom rows report cross-configuration Spearman $\rho$ on per-feature discriminative-power rankings.}
96	  \label{tab:s2_decoding}
97	  \footnotesize
98	  \begin{tabular}{lcccc}
99	    \toprule
100	    \textbf{Depth Pair} & \textbf{Greedy} & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
101	    \midrule
102	    0 vs.\ 1 & $.980\;[.977,\,.982]$ & $.995\;[.993,\,.996]$ & $.988\;[.986,\,.990]$ & $.998\;[.998,\,.999]$ \\
103	    1 vs.\ 2 & $.689\;[.680,\,.698]$ & $.687\;[.677,\,.695]$ & $.689\;[.680,\,.697]$ & $.704\;[.695,\,.713]$ \\
104	    \cmidrule(lr){1-5}
105	    2 vs.\ 3 & $.561\;[.552,\,.571]$ & $.592\;[.582,\,.601]$\rlap{$^\dagger$} & $.590\;[.581,\,.600]$ & $.582\;[.572,\,.592]$ \\
106	    3 vs.\ 4 & $.540\;[.531,\,.550]$ & $.547\;[.537,\,.557]$ & $.539\;[.529,\,.549]$ & $.529\;[.519,\,.540]$ \\
107	    4 vs.\ 5 & $.514\;[.503,\,.524]$ & $.507\;[.496,\,.517]^{\ddagger}$ & $.535\;[.524,\,.545]$ & $.524\;[.513,\,.535]$ \\
108	    \midrule
109	    \multicolumn{5}{l}{\textbf{Cross-config feature Spearman $\rho$}} \\
110	    \midrule
111	    \multicolumn{2}{l}{Greedy vs.\ Nuc $p{=}0.9$} & 0.600 &
112	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}0.7$} & 0.782 \\
113	    \multicolumn{2}{l}{Greedy vs.\ $T{=}0.7$} & 0.914 &
114	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}1.2$} & 0.893 \\
115	    \multicolumn{2}{l}{Greedy vs.\ $T{=}1.2$} & 0.532 &
116	    \multicolumn{1}{l}{$T{=}0.7$ vs.\ $T{=}1.2$} & 0.668 \\
117	    \bottomrule
118	    \multicolumn{5}{l}{${}^{\dagger}$\,CI upper bound (0.601) marginally exceeds $\theta{=}0.60$ by 0.001.} \\
119	    \multicolumn{5}{l}{${}^{\ddagger}$\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}
120	  \end{tabular}
121	\end{table*}
122	
123	%%% Table S2b: Extended K* CI (all models including new additions)
124	\begin{table*}[t]
125	  \centering
126	  \scriptsize
127	  \caption{Extended pairwise $\auc$ with bootstrap 95\% CIs for all model configurations including new additions.
128	  This table extends Table~\ref{tab:kstar_ci} in the main text with Qwen-base, LLaMA-8B, Mistral-7B, Pythia-6.9B (nucleus), and Gemma-2-2B configurations.
129	  $\Kempirical = 2$ holds for 6/10 conditions at $\theta{=}0.60$ (OLMo-1B, Mistral-7B, Pythia-6.9B, Gemma-2-2B: $\Kempirical{=}1$).}
130	  \label{tab:kstar_ci_extended}
131	  \resizebox{\textwidth}{!}{%
132	  \begin{tabular}{lcccccccccccccccccccc}
133	    \toprule
134	     & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} & \multicolumn{2}{c}{Qwen-base} & \multicolumn{2}{c}{LLaMA-8B} & \multicolumn{2}{c}{Mistral-7B} & \multicolumn{2}{c}{Pythia-6.9B\rlap{$^\S$}} & \multicolumn{2}{c}{Gemma-2B} \\
135	    \cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}\cmidrule(lr){12-13}\cmidrule(lr){14-15}\cmidrule(lr){16-17}\cmidrule(lr){18-19}\cmidrule(lr){20-21}
136	     & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
137	    \midrule
138	    0v1 & .9956 & & .9722 & & .9860 & & .9971 & & .9638 & [.961,\,.967] & .987 & [.985,\,.989] & .9224 & [.917,\,.927] & .9170 & & .9599 & & .953 & [.949,\,.957] \\
139	    1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6074 & [.598,\,.617]\rlap{$^*$} & .5001 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} & .626 & [.617,\,.635]\rlap{$^*$} & .6123 & [.603,\,.622]\rlap{$^*$} & .5750 & & .5955 & & .5981 & [.588,\,.608] \\
140	    2v3 & .5893 & [.580,\,.599] & .5440 & [.534,\,.554] & .4973 & [.486,\,.509] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] & .550 & [.540,\,.560] & .5273 & [.517,\,.538] & .5369 & & .5298 & & .534 & [.523,\,.545] \\
141	    3v4 & .5435 & & .5051 & & .5024 & & .5409 & & .5276 & & .529 & [.519,\,.540] & .5168 & [.506,\,.528] & .5174 & & .5135 & & .5033 & [.492,\,.514] \\
142	    4v5 & .5340 & & .5079 & & .4942 & & .5141 & & .5085 & & .518 & [.508,\,.529] & .5159 & [.505,\,.527] & .5175 & & ---\rlap{$^\|$} & & .5025 & [.492,\,.514] \\
143	    \bottomrule
144	    \multicolumn{21}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all boundary comparisons.} \\
145	    \multicolumn{21}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\
146	    \multicolumn{21}{l}{\footnotesize $^\|$$\Kempirical{=}1$; 4v5 not required for boundary determination.} \\
147	    \multicolumn{21}{l}{\footnotesize $^\S$Pythia-6.9B evaluated separately; nucleus sampling ($p{=}0.95$, $T{=}1.0$), same as all other models.}
148	  \end{tabular}}% end resizebox
149	\end{table*}
150	
151	%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)
152	\begin{table}[t]
153	  \centering
154	  \scriptsize
155	  \caption{LLM zero-shot depth classification: $5{\times}5$ confusion matrices (Exp-011). Both frontier LLMs achieve high binary detection accuracy (GPT-5.5: 0.878; Claude Opus~4.6: 0.882) but near-chance 5-class accuracy (${\sim}$0.33 vs.\ OBD-LightGBM 0.386). Per-depth recall in Table~\ref{tab:s3c_perdepth}.}
156	  \label{tab:s3_llm_zeroshot}
157	
158	  \vspace{0.3em}
159	  \textbf{(a)} GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)
160	  \vspace{1pt}
161	
162	  \begin{tabular}{lcccccc}
163	    \toprule
164	    & \multicolumn{5}{c}{Predicted Depth} & \\
165	    \cmidrule(lr){2-6}
166	    True & 0 & 1 & 2 & 3 & 4 & Rec. \\
167	    \midrule
168	    0 & \textbf{77} & 18 &  4 &  0 &  1 & .770 \\
169	    1 &  9 & \textbf{19} & 36 & 24 & 12 & .190 \\
170	    2 &  8 & 10 & \textbf{38} & 35 &  9 & .380 \\
171	    3 & 10 & 16 & 35 & \textbf{24} & 15 & .240 \\
172	    4 & 11 & 13 & 50 & 18 &  \textbf{8} & .080 \\
173	    \bottomrule
174	  \end{tabular}
175	
176	  \vspace{4pt}
177	  \textbf{(b)} Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)
178	  \vspace{1pt}
179	
180	  \begin{tabular}{lcccccc}
181	    \toprule
182	    & \multicolumn{5}{c}{Predicted Depth} & \\
183	    \cmidrule(lr){2-6}
184	    True & 0 & 1 & 2 & 3 & 4 & Rec. \\
185	    \midrule
186	    0 & \textbf{69} & 26 &  3 &  0 &  2 & .690 \\
187	    1 &  8 & \textbf{21} & 32 & 11 & 28 & .210 \\
188	    2 &  6 & 36 & \textbf{28} &  5 & 25 & .280 \\
189	    3 &  7 & 20 & 31 & \textbf{10} & 31 & .100 \\
190	    4 &  7 & 28 & 22 &  6 & \textbf{37} & .370 \\
191	    \bottomrule
192	  \end{tabular}
193	\end{table}
194	
195	\begin{table}[t]
196	  \centering
197	  \small
198	  \caption{Per-depth recall (\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\geq 2$, consistent with $\Kempirical = 2$.}
199	  \label{tab:s3c_perdepth}
200	  \resizebox{\columnwidth}{!}{%
201	  \begin{tabular}{lccccc}
202	    \toprule
203	    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\
204	    \midrule
205	    OBD-LightGBM & \textbf{96} & \textbf{39} & 14 & 19 & 22 \\
206	    GPT-5.5      & 77 & 19 & \textbf{38} & \textbf{24} &  8 \\
207	    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \textbf{37} \\
208	    \bottomrule
209	  \end{tabular}}
210	\end{table}
211	
212	%%% Table: Token Length and EOS Truncation Analysis
213	\begin{table}[t]
214	  \centering
215	  \scriptsize
216	  \caption{Mean subword token count per depth and EOS truncation rate (\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend; the 0v1 length asymmetry (human texts shorter) makes detection \emph{more conservative}, not inflated. See Section~\ref{sec:length_confound}.}
217	  \label{tab:token_length}
218	  \resizebox{\columnwidth}{!}{%
219	  \begin{tabular}{lcccccccc}
220	    \toprule
221	    & \multicolumn{6}{c}{\textbf{Mean Token Count}} & & \\
222	    \cmidrule(lr){2-7}
223	    \textbf{Model} & D0 & D1 & D2 & D3 & D4 & D5 & \textbf{EOS\%} & \textbf{Sev.} \\
224	    \midrule
225	    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\
226	    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\
227	    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negl. \\
228	    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Mod. \\
229	    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\
230	    \midrule
231	    \multicolumn{9}{l}{\textit{Decoding ablation (Qwen-rw 1.5B)}} \\
232	    \quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\
233	    \quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\
234	    \quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\
235	    \quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\
236	    \bottomrule
237	    \multicolumn{9}{l}{EOS\%: generation terminated via EOS before 256-token limit. Ranges span depths 1--5.}
238	  \end{tabular}}
239	\end{table}
240	
241	%%% Table S5: Complete 15-D Feature Descriptions
242	\begin{table*}[t]
243	  \centering
244	  \caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}
245	  \label{tab:s5_features}
246	  \begin{tabular}{llp{0.45\textwidth}l}
247	    \toprule
248	    \textbf{Group} & \textbf{Feature} & \textbf{Description} & \textbf{Range} \\
249	    \midrule
250	    \multirow{9}{*}{\rotatebox[origin=c]{90}{\textsc{Surprisal}}}
251	    & \texttt{surp\_mean}   & Mean token surprisal $\frac{1}{T}\sum_t -\log p(x_t \mid x_{&lt;t})$ & $\mathbb{R}^+$ \\
252	    & \texttt{surp\_std}    & Standard deviation of token surprisal & $\mathbb{R}^+$ \\
253	    & \texttt{surp\_skew}   & Skewness of the surprisal distribution & $\mathbb{R}$ \\
254	    & \texttt{surp\_kurt}   & Excess kurtosis of the surprisal distribution & $\mathbb{R}$ \\
255	    & \texttt{surp\_d1\_mean} & Mean of first-order surprisal differences $\Delta s_t = s_{t+1} - s_t$ & $\mathbb{R}$ \\
256	    & \texttt{surp\_d1\_std}  & Std of first-order surprisal differences & $\mathbb{R}^+$ \\
257	    & \texttt{surp\_d1\_skew} & Skewness of first-order surprisal differences & $\mathbb{R}$ \\
258	    & \texttt{surp\_d2\_mean} & Mean of second-order differences $\Delta^2 s_t$ & $\mathbb{R}$ \\
259	    & \texttt{surp\_d2\_std}  & Std of second-order surprisal differences & $\mathbb{R}^+$ \\
260	    \midrule
261	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Lex}}}
262	    & \texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\
263	    & \texttt{hapax\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\
264	    & \texttt{self\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\
265	    \midrule
266	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Freq}}}
267	    & \texttt{freq\_kurtosis}  & Excess kurtosis of word frequency distribution & $\mathbb{R}$ \\
268	    & \texttt{freq\_entropy}   & Shannon entropy of word frequencies: $-\sum p_w \log_2 p_w$ & $\mathbb{R}^+$ \\
269	    & \texttt{low\_freq\_ratio} & Proportion of vocabulary with count $\leq 2$ & $[0, 1]$ \\
270	    \bottomrule
271	  \end{tabular}
272	\end{table*}
273	
274	%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap
275	\begin{table*}[t]
276	\begin{minipage}[t]{0.45\textwidth}
277	  \centering
278	  \small
279	  \captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \texttt{doc\_id} to prevent data leakage from the same seed document appearing in both train and test.}
280	  \label{tab:s6_lgbm_params}
281	  \begin{tabular}{ll}
282	    \toprule
283	    \textbf{Parameter} & \textbf{Value} \\
284	    \midrule
285	    \texttt{n\_estimators}      & 200 \\
286	    \texttt{learning\_rate}     & 0.05 \\
287	    \texttt{max\_depth}         & 6 \\
288	    \texttt{num\_leaves}        & 31 \\
289	    \texttt{verbose}            & $-1$ \\
290	    \texttt{n\_jobs}            & $-1$ (all cores) \\
291	    Cross-validation            & 5-fold GroupKFold \\
292	    Grouping key                & \texttt{doc\_id} \\
293	    Objective                   & Binary (per depth pair) \\
294	    \bottomrule
295	  \end{tabular}
296	\end{minipage}\hfill
297	\begin{minipage}[t]{0.52\textwidth}
298	  \centering
299	  \small
300	  \captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}
301	  \label{tab:s7_neural_probe}
302	  \resizebox{\textwidth}{!}{%
303	  \begin{tabular}{ll}
304	    \toprule
305	    \textbf{Component} & \textbf{Details} \\
306	    \midrule
307	    \multicolumn{2}{l}{\textit{Embedding extraction}} \\
308	    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\
309	    Representation    & Last hidden state, attention-masked avg pool \\
310	    Embedding dim     & 1536 / 2048 / 2048 \\
311	    Max sequence len   & 512 tokens \\
312	    \midrule
313	    \multicolumn{2}{l}{\textit{MLP classifier}} \\
314	    Architecture      & $d_{\text{emb}} \to 512 \to 256 \to 6$ \\
315	    Activations       & ReLU \\
316	    Dropout           & 0.1 (after each hidden layer) \\
317	    Output            & 6-class softmax \\
318	    \midrule
319	    \multicolumn{2}{l}{\textit{Training}} \\
320	    Optimizer         & Adam ($\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\
321	    Loss              & Cross-entropy \\
322	    Batch size        & 256 \\
323	    Max epochs        & 20 \\
324	    Early stopping    & Patience = 5 (validation loss) \\
325	    Cross-validation  & 5-fold GroupKFold \\
326	    \bottomrule
327	  \end{tabular}%
328	  }
329	\end{minipage}
330	\end{table*}
331	
332	%%% Table S8: Per-Model Bootstrap CI Results (exp-007)
333	\begin{table}[t]
334	  \centering
335	  \scriptsize
336	  \caption{Pairwise AUC with bootstrap 95\% CIs for four model-mode configurations (1{,}000 resamples). All boundary pairs ($\auc > \theta$) $p < 0.01$; OLMo 1v2--4v5 non-significant ($p > 0.09$).}
337	  \label{tab:s8_cv_folds}
338	  \resizebox{\columnwidth}{!}{%
339	  \begin{tabular}{lcccc}
340	    \toprule
341	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
342	    \midrule
343	    0v1 & $.996\;[.995,.997]$ & $.993\;[.992,.994]$ & $.986\;[.984,.988]$ & $.997\;[.996,.998]$ \\
344	    1v2 & $.696\;[.686,.704]$ & $.607\;[.598,.617]$ & $.500\;[.496,.519]$ & $.611\;[.602,.621]$ \\
345	    \cmidrule(lr){1-5}
346	    2v3 & $.589\;[.580,.599]$ & $.551\;[.542,.563]$ & $.497\;[.486,.509]$ & $.561\;[.551,.571]$ \\
347	    3v4 & $.544\;[.533,.555]$ & $.515\;[.504,.526]$ & $.502\;[.491,.513]$ & $.541\;[.531,.551]$ \\
348	    4v5 & $.534\;[.524,.545]$ & $.514\;[.502,.525]$ & $.494\;[.483,.506]$ & $.514\;[.504,.526]$ \\
349	    \bottomrule
350	  \end{tabular}}
351	\end{table}
352	
353	%%% Table S9: Binary Detector Spearman ρ (exp-012)
354	\begin{table}[t]
355	  \centering
356	  \scriptsize
357	  \caption{Spearman $\rho$ between binary detector scores and true depth, and 6-class accuracy. Correlations driven by 0v1; scores do not track depth beyond generation~1. Qwen-rw exhibits reversed sign ($\rho > 0$).}
358	  \label{tab:s9_binary_spearman}
359	  \resizebox{\columnwidth}{!}{%
360	  \begin{tabular}{lcccc}
361	    \toprule
362	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
363	    \midrule
364	    \multicolumn{5}{l}{\textit{Spearman $\rho$}} \\
365	    \quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\
366	    \quad log-PPL (obs.)     & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\
367	    \quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\
368	    \midrule
369	    6-class acc.              & 0.199    & 0.130    & 0.127    & 0.183 \\
370	    \bottomrule
371	    \multicolumn{5}{l}{Random baseline: 0.167} \\
372	  \end{tabular}}
373	\end{table}
374	
375	%%% Table S10: Pythia Decoding Ablation (exp-020)
376	\begin{table}[t]
377	  \centering
378	  \scriptsize
379	  \caption{Pythia-1.4B pairwise $\auc$ under four decoding configs (10K bootstrap). $^\dagger$Greedy triggers repetition collapse (4-gram repeat: $d_0{=}0.01 \to d_1{=}0.72$).}
380	  \label{tab:s10_pythia_decoding}
381	  \resizebox{\columnwidth}{!}{%
382	  \begin{tabular}{lcccc}
383	    \toprule
384	    & \textbf{Greedy}$^\dagger$ & \textbf{$p{=}0.9$} & \textbf{$T{=}0.7$} & \textbf{$T{=}1.2$} \\
385	    \midrule
386	    0v1 & $.999$ & $.995$ & $.996$ & $.994$ \\
387	    1v2 & $.884$ & $.675$ & $.728$ & $.618$ \\
388	    \cmidrule(lr){1-5}
389	    2v3 & $.531$ & $.559$ & $.598^\ddagger$ & $.531$ \\
390	    3v4 & $.522$ & $.524$ & $.563$ & $.520$ \\
391	    4v5 & $.514$ & $.501$ & $.527$ & $.510$ \\
392	    \midrule
393	    $\Kempirical$ & 2 & 2 & 2 & 2 \\
394	    \bottomrule
395	    \multicolumn{5}{l}{${}^{\ddagger}$CI upper 0.606 $> \theta$; point est.\ below.} \\
396	  \end{tabular}}
397	\end{table}
398	
399	%%% Table S11: Length Ablation (exp-021)
400	\begin{table}[t]
401	  \centering
402	  \small
403	  \caption{Pairwise $\auc$ for three segment lengths (Qwen-base, cont.\ mode). $\Kempirical{=}2$ at 128/256; 512 marginal ($^\dagger$CI lower $< \theta$).}
404	  \label{tab:s11_length_ablation}
405	  \begin{tabular}{lccc}
406	    \toprule
407	    & \textbf{128} & \textbf{256} & \textbf{512} \\
408	    \midrule
409	    0v1 & .979 & .991 & .992 \\
410	    1v2 & .622 & .628 & .607$^\dagger$ \\
411	    \cmidrule(lr){1-4}
412	    2v3 & .529 & .556 & .572 \\
413	    3v4 & .535 & .530 & .530 \\
414	    4v5 & .501 & .514 & .518 \\
415	    \midrule
416	    $\Kempirical$ & 2 & 2 & 2$^\dagger$ \\
417	    \bottomrule
418	  \end{tabular}
419	\end{table}
420	
421	%%% Table S12: Domain Ablation
422	\begin{table}[t]
423	  \centering
424	  \small
425	  \caption{Pairwise $\auc$ for three text domains (Qwen-cont). arXiv yields $\Kempirical{=}3$; C4 and Wikipedia $\Kempirical{=}2$.}
426	  \label{tab:s12_domain_ablation}
427	  \begin{tabular}{lccc}
428	    \toprule
429	    & \textbf{C4} & \textbf{Wiki} & \textbf{arXiv} \\
430	    \midrule
431	    0v1 & .997 & .996 & .995 \\
432	    1v2 & .611 & .619 & .858 \\
433	    \cmidrule(lr){1-4}
434	    2v3 & .561 & .550 & .644$^*$ \\
435	    3v4 & .541 & .523 & .544 \\
436	    4v5 & .514 & .514 & .530 \\
437	    \midrule
438	    $\Kempirical$ & 2 & 2 & 3 \\
439	    \bottomrule
440	    \multicolumn{4}{l}{\footnotesize $^*$CI $[.628,.658]$; $p < 0.001$.}
441	  \end{tabular}
442	\end{table}
443	
444	%%% Table S13: Scorer Sensitivity Analysis
445	\begin{table}[t]
446	  \centering
447	  \scriptsize
448	  \caption{Scorer sensitivity: $\Kempirical$ under self- vs.\ cross-scoring. Cross-scoring reduces $\Kempirical$ only for marginal Qwen-cont.}
449	  \label{tab:s13_scorer_sensitivity}
450	  \resizebox{\columnwidth}{!}{%
451	  \begin{tabular}{llcccc}
452	    \toprule
453	    \textbf{Generator} & \textbf{Mode} & \textbf{Self} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Agr.} \\
454	    \midrule
455	    Qwen-Inst & Rewrite & 2 & 2 & 2 & \checkmark \\
456	    Qwen-Inst & Cont.   & 2 & 1 & 1 & $\times$ \\
457	    Qwen-base & Cont.   & 2 & 2 & 2 & \checkmark \\
458	    Pythia    & Cont.   & 2 & 2 & 2 & \checkmark \\
459	    OLMo      & Cont.   & 1 & -- & -- & -- \\
460	    Qwen-7B   & Cont.   & 2 & -- & -- & -- \\
461	    Mistral   & Cont.   & 1 & -- & -- & -- \\
462	    \bottomrule
463	  \end{tabular}}
464	\end{table}
465	
466	\clearpage
467	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78afd710-d9ff-4d58-943d-62adb30fe47a",
  "isSidechain": false,
  "promptId": "55d142f3-1246-4ea6-885d-cf2788d25a6d",
  "type": "user",
  "uuid": "29e1a2c8-cdbf-4332-89d2-311561a93d98",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
      "content": "\\appendix\n\\section{Supplementary Materials}\n\\label{sec:appendix}\n\nThis appendix provides supplementary figures, detailed experimental tables, dataset statistics, and complete feature descriptions referenced in the main text.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_filtering_strategies.pdf}\n\\caption{Downstream performance of all filtering strategies (5 seeds, $\\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}\n\\label{fig:filtering_strategies}\n\\end{figure}\n\n\\paragraph{Feature ranking and cross-model consistency.}\nTable~\\ref{tab:top_features} reports per-model single-feature AUC rankings.\nSurprisal derivative features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_d2\\_std}) consistently rank among the top three across all continuation-mode models (Pythia, OLMo, Qwen-cont), with pairwise Spearman $\\rho \\geq 0.85$.\nThe rewrite-mode model (Qwen-rw) diverges by placing \\texttt{freq\\_entropy} first, reflecting a distributional shift that is lexical rather than surprisal-driven.\nThis scorer-invariant ranking supports the use of a fixed 15-dimensional feature set across generators without per-model feature selection.\n\n%%% Feature ranking table (moved from main text)\n\\begin{table}[!htbp]\n\\centering\n\\small\n\\caption{Top-3 features by single-feature $\\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}\n\\label{tab:top_features}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cllll}\n\\toprule\nRank & Pythia & OLMo & Qwen-rw & Qwen-cont \\\\\n\\midrule\n1 & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\texttt{freq\\_entropy} & \\textbf{\\texttt{surp\\_d1\\_std}} \\\\\n2 & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_std}} \\\\\n3 & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\nTable~\\ref{tab:s1_transfer} reports the cross-model transfer accuracy matrix.\nClassifiers trained on continuation-mode generators (Pythia, OLMo, Qwen-cont) transfer well to each other, with off-diagonal accuracy retaining 80--92\\% of in-distribution performance.\nThe asymmetry between rewrite-mode and continuation-mode transfer (61--63\\%) confirms that generation mode, rather than model family, is the primary axis of distributional variation (Section~\\ref{sec:discussion}).\n\n%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)\n\\begin{table}[!htbp]\n  \\centering\n  \\small\n  \\caption{Cross-model transfer accuracy matrix. Diagonal (\\textbf{bold}): within-model; off-diagonal: cross-model. Retention: Pythia$\\leftrightarrow$OLMo 91--92\\%, Qwen-cont$\\leftrightarrow$Pythia 83--85\\%, Qwen-rw$\\to$others 61--63\\%.}\n  \\label{tab:s1_transfer}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Train} & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n    \\midrule\n    Qwen-rw   & \\textbf{.423} & .259 & .265 & .347 \\\\\n    Pythia    & .272 & \\textbf{.386} & .353 & .329 \\\\\n    OLMo      & .277 & .345 & \\textbf{.382} & .324 \\\\\n    Qwen-cont & .344 & .328 & .311 & \\textbf{.388} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n\\paragraph{Dataset construction.}\nTable~\\ref{tab:s4_dataset_stats} summarizes the generational depth corpus.\nEach depth level contains 5{,}000 passages, yielding 30{,}000 total samples across six depths (0--5).\nDepth~0 consists of human-written seed texts from the C4 English validation split, truncated to 256 subword tokens.\nSubsequent depths are generated recursively: each depth-$k$ passage is produced by prompting the generator with the corresponding depth-$(k{-}1)$ passage.\nThe four model-mode configurations (Qwen-rw, Pythia-cont, OLMo-cont, Qwen-cont) share identical depth-0 seeds and generation pipeline, differing only in generator identity and prompting strategy (rewrite vs.\\ continuation).\n\n%%% Table S4: Dataset Statistics\n\\begin{table}[!htbp]\n  \\centering\n  \\small\n  \\caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}\n  \\label{tab:s4_dataset_stats}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{clrl}\n    \\toprule\n    \\textbf{Depth} & \\textbf{$N$ samples} & \\textbf{Mean tokens} & \\textbf{Source} \\\\\n    \\midrule\n    0 & 5{,}000 & 147.8 & C4 validation (human) \\\\\n    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\\\\n    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\\\\n    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\\\\n    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Total} & \\multicolumn{2}{l}{30{,}000 samples} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S2: Decoding Ablation AUC (exp-003)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Pairwise AUC with bootstrap 95\\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\\,vs.\\,2 and 2\\,vs.\\,3 marks the empirical detectability boundary $\\Kempirical=2$. Bottom rows report cross-configuration Spearman $\\rho$ on per-feature discriminative-power rankings.}\n  \\label{tab:s2_decoding}\n  \\footnotesize\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Greedy} & \\textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \\textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \\textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\\\\n    \\midrule\n    0 vs.\\ 1 & $.980\\;[.977,\\,.982]$ & $.995\\;[.993,\\,.996]$ & $.988\\;[.986,\\,.990]$ & $.998\\;[.998,\\,.999]$ \\\\\n    1 vs.\\ 2 & $.689\\;[.680,\\,.698]$ & $.687\\;[.677,\\,.695]$ & $.689\\;[.680,\\,.697]$ & $.704\\;[.695,\\,.713]$ \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3 & $.561\\;[.552,\\,.571]$ & $.592\\;[.582,\\,.601]$\\rlap{$^\\dagger$} & $.590\\;[.581,\\,.600]$ & $.582\\;[.572,\\,.592]$ \\\\\n    3 vs.\\ 4 & $.540\\;[.531,\\,.550]$ & $.547\\;[.537,\\,.557]$ & $.539\\;[.529,\\,.549]$ & $.529\\;[.519,\\,.540]$ \\\\\n    4 vs.\\ 5 & $.514\\;[.503,\\,.524]$ & $.507\\;[.496,\\,.517]^{\\ddagger}$ & $.535\\;[.524,\\,.545]$ & $.524\\;[.513,\\,.535]$ \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textbf{Cross-config feature Spearman $\\rho$}} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Greedy vs.\\ Nuc $p{=}0.9$} & 0.600 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}0.7$} & 0.782 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}0.7$} & 0.914 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}1.2$} & 0.893 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}1.2$} & 0.532 &\n    \\multicolumn{1}{l}{$T{=}0.7$ vs.\\ $T{=}1.2$} & 0.668 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{${}^{\\dagger}$\\,CI upper bound (0.601) marginally exceeds $\\theta{=}0.60$ by 0.001.} \\\\\n    \\multicolumn{5}{l}{${}^{\\ddagger}$\\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S2b: Extended K* CI (all models including new additions)\n\\begin{table*}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Extended pairwise $\\auc$ with bootstrap 95\\% CIs for all model configurations including new additions.\n  This table extends Table~\\ref{tab:kstar_ci} in the main text with Qwen-base, LLaMA-8B, Mistral-7B, Pythia-6.9B (nucleus), and Gemma-2-2B configurations.\n  $\\Kempirical = 2$ holds for 6/10 conditions at $\\theta{=}0.60$ (OLMo-1B, Mistral-7B, Pythia-6.9B, Gemma-2-2B: $\\Kempirical{=}1$).}\n  \\label{tab:kstar_ci_extended}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{lcccccccccccccccccccc}\n    \\toprule\n     & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} & \\multicolumn{2}{c}{Qwen-base} & \\multicolumn{2}{c}{LLaMA-8B} & \\multicolumn{2}{c}{Mistral-7B} & \\multicolumn{2}{c}{Pythia-6.9B\\rlap{$^\\S$}} & \\multicolumn{2}{c}{Gemma-2B} \\\\\n    \\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\\cmidrule(lr){12-13}\\cmidrule(lr){14-15}\\cmidrule(lr){16-17}\\cmidrule(lr){18-19}\\cmidrule(lr){20-21}\n     & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n    \\midrule\n    0v1 & .9956 & & .9722 & & .9860 & & .9971 & & .9638 & [.961,\\,.967] & .987 & [.985,\\,.989] & .9224 & [.917,\\,.927] & .9170 & & .9599 & & .953 & [.949,\\,.957] \\\\\n    1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6074 & [.598,\\,.617]\\rlap{$^*$} & .5001 & [.496,\\,.519] & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} & .626 & [.617,\\,.635]\\rlap{$^*$} & .6123 & [.603,\\,.622]\\rlap{$^*$} & .5750 & & .5955 & & .5981 & [.588,\\,.608] \\\\\n    2v3 & .5893 & [.580,\\,.599] & .5440 & [.534,\\,.554] & .4973 & [.486,\\,.509] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] & .550 & [.540,\\,.560] & .5273 & [.517,\\,.538] & .5369 & & .5298 & & .534 & [.523,\\,.545] \\\\\n    3v4 & .5435 & & .5051 & & .5024 & & .5409 & & .5276 & & .529 & [.519,\\,.540] & .5168 & [.506,\\,.528] & .5174 & & .5135 & & .5033 & [.492,\\,.514] \\\\\n    4v5 & .5340 & & .5079 & & .4942 & & .5141 & & .5085 & & .518 & [.508,\\,.529] & .5159 & [.505,\\,.527] & .5175 & & ---\\rlap{$^\\|$} & & .5025 & [.492,\\,.514] \\\\\n    \\bottomrule\n    \\multicolumn{21}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all boundary comparisons.} \\\\\n    \\multicolumn{21}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\\\\n    \\multicolumn{21}{l}{\\footnotesize $^\\|$$\\Kempirical{=}1$; 4v5 not required for boundary determination.} \\\\\n    \\multicolumn{21}{l}{\\footnotesize $^\\S$Pythia-6.9B evaluated separately; nucleus sampling ($p{=}0.95$, $T{=}1.0$), same as all other models.}\n  \\end{tabular}}% end resizebox\n\\end{table*}\n\n%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{LLM zero-shot depth classification: $5{\\times}5$ confusion matrices (Exp-011). Both frontier LLMs achieve high binary detection accuracy (GPT-5.5: 0.878; Claude Opus~4.6: 0.882) but near-chance 5-class accuracy (${\\sim}$0.33 vs.\\ OBD-LightGBM 0.386). Per-depth recall in Table~\\ref{tab:s3c_perdepth}.}\n  \\label{tab:s3_llm_zeroshot}\n\n  \\vspace{0.3em}\n  \\textbf{(a)} GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)\n  \\vspace{1pt}\n\n  \\begin{tabular}{lcccccc}\n    \\toprule\n    & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n    \\cmidrule(lr){2-6}\n    True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n    \\midrule\n    0 & \\textbf{77} & 18 &  4 &  0 &  1 & .770 \\\\\n    1 &  9 & \\textbf{19} & 36 & 24 & 12 & .190 \\\\\n    2 &  8 & 10 & \\textbf{38} & 35 &  9 & .380 \\\\\n    3 & 10 & 16 & 35 & \\textbf{24} & 15 & .240 \\\\\n    4 & 11 & 13 & 50 & 18 &  \\textbf{8} & .080 \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\textbf{(b)} Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)\n  \\vspace{1pt}\n\n  \\begin{tabular}{lcccccc}\n    \\toprule\n    & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n    \\cmidrule(lr){2-6}\n    True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n    \\midrule\n    0 & \\textbf{69} & 26 &  3 &  0 &  2 & .690 \\\\\n    1 &  8 & \\textbf{21} & 32 & 11 & 28 & .210 \\\\\n    2 &  6 & 36 & \\textbf{28} &  5 & 25 & .280 \\\\\n    3 &  7 & 20 & 31 & \\textbf{10} & 31 & .100 \\\\\n    4 &  7 & 28 & 22 &  6 & \\textbf{37} & .370 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Per-depth recall (\\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\\geq 2$, consistent with $\\Kempirical = 2$.}\n  \\label{tab:s3c_perdepth}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lccccc}\n    \\toprule\n    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\\\\n    \\midrule\n    OBD-LightGBM & \\textbf{96} & \\textbf{39} & 14 & 19 & 22 \\\\\n    GPT-5.5      & 77 & 19 & \\textbf{38} & \\textbf{24} &  8 \\\\\n    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \\textbf{37} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table: Token Length and EOS Truncation Analysis\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Mean subword token count per depth and EOS truncation rate (\\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend; the 0v1 length asymmetry (human texts shorter) makes detection \\emph{more conservative}, not inflated. See Section~\\ref{sec:length_confound}.}\n  \\label{tab:token_length}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccccccc}\n    \\toprule\n    & \\multicolumn{6}{c}{\\textbf{Mean Token Count}} & & \\\\\n    \\cmidrule(lr){2-7}\n    \\textbf{Model} & D0 & D1 & D2 & D3 & D4 & D5 & \\textbf{EOS\\%} & \\textbf{Sev.} \\\\\n    \\midrule\n    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\\\\n    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\\\\n    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negl. \\\\\n    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Mod. \\\\\n    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\\\\n    \\midrule\n    \\multicolumn{9}{l}{\\textit{Decoding ablation (Qwen-rw 1.5B)}} \\\\\n    \\quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\\\\n    \\quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\\\\n    \\quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\\\\n    \\quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\\\\n    \\bottomrule\n    \\multicolumn{9}{l}{EOS\\%: generation terminated via EOS before 256-token limit. Ranges span depths 1--5.}\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S5: Complete 15-D Feature Descriptions\n\\begin{table*}[t]\n  \\centering\n  \\caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}\n  \\label{tab:s5_features}\n  \\begin{tabular}{llp{0.45\\textwidth}l}\n    \\toprule\n    \\textbf{Group} & \\textbf{Feature} & \\textbf{Description} & \\textbf{Range} \\\\\n    \\midrule\n    \\multirow{9}{*}{\\rotatebox[origin=c]{90}{\\textsc{Surprisal}}}\n    & \\texttt{surp\\_mean}   & Mean token surprisal $\\frac{1}{T}\\sum_t -\\log p(x_t \\mid x_{&lt;t})$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_std}    & Standard deviation of token surprisal & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_skew}   & Skewness of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_kurt}   & Excess kurtosis of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_mean} & Mean of first-order surprisal differences $\\Delta s_t = s_{t+1} - s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_std}  & Std of first-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_d1\\_skew} & Skewness of first-order surprisal differences & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_mean} & Mean of second-order differences $\\Delta^2 s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_std}  & Std of second-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Lex}}}\n    & \\texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\\\\n    & \\texttt{hapax\\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\\\\n    & \\texttt{self\\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Freq}}}\n    & \\texttt{freq\\_kurtosis}  & Excess kurtosis of word frequency distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{freq\\_entropy}   & Shannon entropy of word frequencies: $-\\sum p_w \\log_2 p_w$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{low\\_freq\\_ratio} & Proportion of vocabulary with count $\\leq 2$ & $[0, 1]$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap\n\\begin{table*}[t]\n\\begin{minipage}[t]{0.45\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \\texttt{doc\\_id} to prevent data leakage from the same seed document appearing in both train and test.}\n  \\label{tab:s6_lgbm_params}\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Parameter} & \\textbf{Value} \\\\\n    \\midrule\n    \\texttt{n\\_estimators}      & 200 \\\\\n    \\texttt{learning\\_rate}     & 0.05 \\\\\n    \\texttt{max\\_depth}         & 6 \\\\\n    \\texttt{num\\_leaves}        & 31 \\\\\n    \\texttt{verbose}            & $-1$ \\\\\n    \\texttt{n\\_jobs}            & $-1$ (all cores) \\\\\n    Cross-validation            & 5-fold GroupKFold \\\\\n    Grouping key                & \\texttt{doc\\_id} \\\\\n    Objective                   & Binary (per depth pair) \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{minipage}\\hfill\n\\begin{minipage}[t]{0.52\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}\n  \\label{tab:s7_neural_probe}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Component} & \\textbf{Details} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Embedding extraction}} \\\\\n    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\\\\n    Representation    & Last hidden state, attention-masked avg pool \\\\\n    Embedding dim     & 1536 / 2048 / 2048 \\\\\n    Max sequence len   & 512 tokens \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{MLP classifier}} \\\\\n    Architecture      & $d_{\\text{emb}} \\to 512 \\to 256 \\to 6$ \\\\\n    Activations       & ReLU \\\\\n    Dropout           & 0.1 (after each hidden layer) \\\\\n    Output            & 6-class softmax \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Training}} \\\\\n    Optimizer         & Adam ($\\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\\\\n    Loss              & Cross-entropy \\\\\n    Batch size        & 256 \\\\\n    Max epochs        & 20 \\\\\n    Early stopping    & Patience = 5 (validation loss) \\\\\n    Cross-validation  & 5-fold GroupKFold \\\\\n    \\bottomrule\n  \\end{tabular}%\n  }\n\\end{minipage}\n\\end{table*}\n\n%%% Table S8: Per-Model Bootstrap CI Results (exp-007)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Pairwise AUC with bootstrap 95\\% CIs for four model-mode configurations (1{,}000 resamples). All boundary pairs ($\\auc > \\theta$) $p < 0.01$; OLMo 1v2--4v5 non-significant ($p > 0.09$).}\n  \\label{tab:s8_cv_folds}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Qwen-rw} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    0v1 & $.996\\;[.995,.997]$ & $.993\\;[.992,.994]$ & $.986\\;[.984,.988]$ & $.997\\;[.996,.998]$ \\\\\n    1v2 & $.696\\;[.686,.704]$ & $.607\\;[.598,.617]$ & $.500\\;[.496,.519]$ & $.611\\;[.602,.621]$ \\\\\n    \\cmidrule(lr){1-5}\n    2v3 & $.589\\;[.580,.599]$ & $.551\\;[.542,.563]$ & $.497\\;[.486,.509]$ & $.561\\;[.551,.571]$ \\\\\n    3v4 & $.544\\;[.533,.555]$ & $.515\\;[.504,.526]$ & $.502\\;[.491,.513]$ & $.541\\;[.531,.551]$ \\\\\n    4v5 & $.534\\;[.524,.545]$ & $.514\\;[.502,.525]$ & $.494\\;[.483,.506]$ & $.514\\;[.504,.526]$ \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S9: Binary Detector Spearman ρ (exp-012)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Spearman $\\rho$ between binary detector scores and true depth, and 6-class accuracy. Correlations driven by 0v1; scores do not track depth beyond generation~1. Qwen-rw exhibits reversed sign ($\\rho > 0$).}\n  \\label{tab:s9_binary_spearman}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Qwen-rw} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textit{Spearman $\\rho$}} \\\\\n    \\quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\\\\n    \\quad log-PPL (obs.)     & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\\\\n    \\quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\\\\n    \\midrule\n    6-class acc.              & 0.199    & 0.130    & 0.127    & 0.183 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{Random baseline: 0.167} \\\\\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S10: Pythia Decoding Ablation (exp-020)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Pythia-1.4B pairwise $\\auc$ under four decoding configs (10K bootstrap). $^\\dagger$Greedy triggers repetition collapse (4-gram repeat: $d_0{=}0.01 \\to d_1{=}0.72$).}\n  \\label{tab:s10_pythia_decoding}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Greedy}$^\\dagger$ & \\textbf{$p{=}0.9$} & \\textbf{$T{=}0.7$} & \\textbf{$T{=}1.2$} \\\\\n    \\midrule\n    0v1 & $.999$ & $.995$ & $.996$ & $.994$ \\\\\n    1v2 & $.884$ & $.675$ & $.728$ & $.618$ \\\\\n    \\cmidrule(lr){1-5}\n    2v3 & $.531$ & $.559$ & $.598^\\ddagger$ & $.531$ \\\\\n    3v4 & $.522$ & $.524$ & $.563$ & $.520$ \\\\\n    4v5 & $.514$ & $.501$ & $.527$ & $.510$ \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 2 & 2 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{${}^{\\ddagger}$CI upper 0.606 $> \\theta$; point est.\\ below.} \\\\\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S11: Length Ablation (exp-021)\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ for three segment lengths (Qwen-base, cont.\\ mode). $\\Kempirical{=}2$ at 128/256; 512 marginal ($^\\dagger$CI lower $< \\theta$).}\n  \\label{tab:s11_length_ablation}\n  \\begin{tabular}{lccc}\n    \\toprule\n    & \\textbf{128} & \\textbf{256} & \\textbf{512} \\\\\n    \\midrule\n    0v1 & .979 & .991 & .992 \\\\\n    1v2 & .622 & .628 & .607$^\\dagger$ \\\\\n    \\cmidrule(lr){1-4}\n    2v3 & .529 & .556 & .572 \\\\\n    3v4 & .535 & .530 & .530 \\\\\n    4v5 & .501 & .514 & .518 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 2$^\\dagger$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}\n\n%%% Table S12: Domain Ablation\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ for three text domains (Qwen-cont). arXiv yields $\\Kempirical{=}3$; C4 and Wikipedia $\\Kempirical{=}2$.}\n  \\label{tab:s12_domain_ablation}\n  \\begin{tabular}{lccc}\n    \\toprule\n    & \\textbf{C4} & \\textbf{Wiki} & \\textbf{arXiv} \\\\\n    \\midrule\n    0v1 & .997 & .996 & .995 \\\\\n    1v2 & .611 & .619 & .858 \\\\\n    \\cmidrule(lr){1-4}\n    2v3 & .561 & .550 & .644$^*$ \\\\\n    3v4 & .541 & .523 & .544 \\\\\n    4v5 & .514 & .514 & .530 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 3 \\\\\n    \\bottomrule\n    \\multicolumn{4}{l}{\\footnotesize $^*$CI $[.628,.658]$; $p < 0.001$.}\n  \\end{tabular}\n\\end{table}\n\n%%% Table S13: Scorer Sensitivity Analysis\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Scorer sensitivity: $\\Kempirical$ under self- vs.\\ cross-scoring. Cross-scoring reduces $\\Kempirical$ only for marginal Qwen-cont.}\n  \\label{tab:s13_scorer_sensitivity}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{llcccc}\n    \\toprule\n    \\textbf{Generator} & \\textbf{Mode} & \\textbf{Self} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Agr.} \\\\\n    \\midrule\n    Qwen-Inst & Rewrite & 2 & 2 & 2 & \\checkmark \\\\\n    Qwen-Inst & Cont.   & 2 & 1 & 1 & $\\times$ \\\\\n    Qwen-base & Cont.   & 2 & 2 & 2 & \\checkmark \\\\\n    Pythia    & Cont.   & 2 & 2 & 2 & \\checkmark \\\\\n    OLMo      & Cont.   & 1 & -- & -- & -- \\\\\n    Qwen-7B   & Cont.   & 2 & -- & -- & -- \\\\\n    Mistral   & Cont.   & 1 & -- & -- & -- \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n\\clearpage\n",
      "numLines": 467,
      "startLine": 1,
      "totalLines": 467
    }
  },
  "sourceToolAssistantUUID": "78afd710-d9ff-4d58-943d-62adb30fe47a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
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
  "leafUuid": "29e1a2c8-cdbf-4332-89d2-311561a93d98",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile paper and verify Pythia AUC consistency",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0"
}
```

---

### Assistant

_source line 17 · 2026-05-23T07:56:04.027Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the results:

**Compilation**: Output written on main.pdf (18 pages), no errors mentioned. Let me check for errors explicitly.

**Table 2 (tab:kstar_ci) - Pythia column** (experiments_c1.tex lines 26-30):
- 0v1: .9722
- 1v2: .6074, CI [.598,.617]
- 2v3: .5440, CI [.534,.554]
- 3v4: .5051
- 4v5: .5079

**Table 10 (tab:kstar_ci_extended) - Pythia column** (appendix.tex lines 138-142):


Now I'm verifying the values match between the two tables—checking each row's coefficient and confidence intervals to ensure consistency across the document. Now I need to figure out where the appendix begins to confirm the main text is actually 8 pages, since the total is 18 pages including everything else.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29e1a2c8-cdbf-4332-89d2-311561a93d98",
  "isSidechain": false,
  "requestId": "req_011CbK9CnAegYmTiHum5mYKf",
  "type": "assistant",
  "uuid": "0b2a1fd9-a4e4-41eb-b063-8de9012578a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWiB7CQQiZDX4m9U49AkcT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18466,
      "cache_read_input_tokens": 23844,
      "output_tokens": 973,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 973,
          "cache_read_input_tokens": 23844,
          "cache_creation_input_tokens": 18466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18466
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

_source line 18 · 2026-05-23T07:56:04.033Z_

Let me verify the compilation had 0 errors and check page count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b2a1fd9-a4e4-41eb-b063-8de9012578a5",
  "isSidechain": false,
  "requestId": "req_011CbK9CnAegYmTiHum5mYKf",
  "type": "assistant",
  "uuid": "c2cc3b7f-f82c-460b-844a-0ec1ce9ed2d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWiB7CQQiZDX4m9U49AkcT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18466,
      "cache_read_input_tokens": 23844,
      "output_tokens": 973,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 973,
          "cache_read_input_tokens": 23844,
          "cache_creation_input_tokens": 18466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18466
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

_source line 19 · 2026-05-23T07:56:06.098Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Tsb86yGFEr5VDPujbUSZzN`</summary>

```json
{
  "command": "grep -c \"^!\" main.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2cc3b7f-f82c-460b-844a-0ec1ce9ed2d6",
  "isSidechain": false,
  "requestId": "req_011CbK9CnAegYmTiHum5mYKf",
  "type": "assistant",
  "uuid": "367fbb26-edd6-4692-ac5e-cd336d19dcda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWiB7CQQiZDX4m9U49AkcT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18466,
      "cache_read_input_tokens": 23844,
      "output_tokens": 973,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 973,
          "cache_read_input_tokens": 23844,
          "cache_creation_input_tokens": 18466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18466
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

_source line 20 · 2026-05-23T07:56:06.140Z_

<details><summary>↩ Tool result · `toolu_01Tsb86yGFEr5VDPujbUSZzN`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "367fbb26-edd6-4692-ac5e-cd336d19dcda",
  "isSidechain": false,
  "promptId": "55d142f3-1246-4ea6-885d-cf2788d25a6d",
  "type": "user",
  "uuid": "1973e146-999e-443c-bd11-c386da42e742",
  "toolUseResult": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "367fbb26-edd6-4692-ac5e-cd336d19dcda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T07:56:10.064Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015rtip4KpvAaxPZ1kAtvavB`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\n# Find where References or Bibliography starts, and where Appendix starts\nlines = text.split('\\n')\nfor i, line in enumerate(lines):\n    if 'References' == line.strip() or '\\\\appendix' in line or line.strip().startswith('A ') and 'Supplementary' in line:\n        print(f'Line {i}: {line.strip()[:80]}')\n\" 2>/dev/null; # Also check via page markers\ngrep -n \"\\\\\\\\newpage\\|\\\\\\\\clearpage\\|\\\\\\\\appendix\" main.tex | head -20\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1973e146-999e-443c-bd11-c386da42e742",
  "isSidechain": false,
  "requestId": "req_011CbK9CnAegYmTiHum5mYKf",
  "type": "assistant",
  "uuid": "7d41cf66-3757-4ff5-8150-087a37d01c6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWiB7CQQiZDX4m9U49AkcT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18466,
      "cache_read_input_tokens": 23844,
      "output_tokens": 973,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 973,
          "cache_read_input_tokens": 23844,
          "cache_creation_input_tokens": 18466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18466
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

_source line 22 · 2026-05-23T07:56:10.370Z_

<details><summary>↩ Tool result · `toolu_015rtip4KpvAaxPZ1kAtvavB`</summary>

```text
Line 1972: References
84:\clearpage
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d41cf66-3757-4ff5-8150-087a37d01c6e",
  "isSidechain": false,
  "promptId": "55d142f3-1246-4ea6-885d-cf2788d25a6d",
  "type": "user",
  "uuid": "8c84fe57-0d68-4e61-a0dd-6fe55d0145ca",
  "toolUseResult": {
    "stdout": "Line 1972: References\n84:\\clearpage",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7d41cf66-3757-4ff5-8150-087a37d01c6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T07:56:17.467Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gc5oXmGX7auio4rPmFMmod`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\n# Count pages before appendix by checking where 'A Supplementary' appears\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nprint(f'Total pages: {len(pages)}')\nfor i, page in enumerate(pages):\n    first_lines = page.strip()[:200]\n    if 'Supplementary' in page[:300] or 'Appendix' in page[:300]:\n        print(f'Page {i+1}: Appendix starts here')\n        break\n    if 'References' in page[:300] and i > 5:\n        print(f'Page {i+1}: References start here')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c84fe57-0d68-4e61-a0dd-6fe55d0145ca",
  "isSidechain": false,
  "requestId": "req_011CbK9EE2vmB5EnNL3BzLVh",
  "type": "assistant",
  "uuid": "787ed2bb-0886-4edc-8326-268ada40bcb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DR4wioVE27TyFHabxVEjaj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 978,
      "cache_read_input_tokens": 42310,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 978,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 279,
          "cache_read_input_tokens": 42310,
          "cache_creation_input_tokens": 978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 978
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

_source line 24 · 2026-05-23T07:56:17.702Z_

<details><summary>↩ Tool result · `toolu_01Gc5oXmGX7auio4rPmFMmod`</summary>

```text
Total pages: 19
Page 11: Appendix starts here
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "787ed2bb-0886-4edc-8326-268ada40bcb0",
  "isSidechain": false,
  "promptId": "55d142f3-1246-4ea6-885d-cf2788d25a6d",
  "type": "user",
  "uuid": "90940df8-2706-4c80-8cbb-e212ca0d94a2",
  "toolUseResult": {
    "stdout": "Total pages: 19\nPage 11: Appendix starts here",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "787ed2bb-0886-4edc-8326-268ada40bcb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T07:56:24.855Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UK1BztE9ALeNz3dUrjRqUz`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nfor i, page in enumerate(pages[:12]):\n    # Show first 100 chars to identify content\n    first = page.strip()[:120].replace('\\n', ' | ')\n    print(f'Page {i+1}: {first}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90940df8-2706-4c80-8cbb-e212ca0d94a2",
  "isSidechain": false,
  "requestId": "req_011CbK9EmNapR6tmhsmbMef5",
  "type": "assistant",
  "uuid": "a32fea5c-b905-4b23-8f9e-d8a85e9d1d21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTp7p1JvkuyjDXP3Uvq8yK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 43288,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 272,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 43288,
          "cache_creation_input_tokens": 272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 272
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

_source line 26 · 2026-05-23T07:56:25.089Z_

<details><summary>↩ Tool result · `toolu_01UK1BztE9ALeNz3dUrjRqUz`</summary>

```text
Page 1: Generational Depth Estimation of Recursive Synthetic Text: |                           Measuring the Discrimination Bounda
Page 2: 084            ∗ |             Kempirical =3), and quantifies boundary sensi-         benchmarks like RAID (Dugan et al., 
Page 3: Seed Corpus             Recursive                Feature                       OBD               K * Estimation |         
Page 4: Table 1: Experimental configurations for depth-chain                                                  K * boundary |      
Page 5: Table 2: Pairwise AUC for adjacent depth pairs with bootstrap 95% CIs and permutation p-values for boundary |             
Page 6: = 0.60 |  |                                                   (a) Pairwise AUC profile                                      
Page 7: 413   4.6    Binary Detector Confidence                              Table 5: Downstream task performance (MMLU, Hel- |   
Page 8: 499   one depth level of sensitivity for cross-model               Prompt-chain scope and retrain-chain gap.            
Page 9: 597   Limitations                                                  Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi     
Page 10: 698   Yanzhu Guo, Guokan Shang, Michalis Vazirgiannis, and              Zhen Sun, Zongmin Zhang, Xinyue Shen, Ziyi Zhang
Page 11: 802   A       Supplementary Materials                                                        0.5975 |                     
Page 12: Table 9: Pairwise AUC with bootstrap 95% CIs across depth pairs for four decoding configurations (all using | Qwen2.5-1.5B
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a32fea5c-b905-4b23-8f9e-d8a85e9d1d21",
  "isSidechain": false,
  "promptId": "55d142f3-1246-4ea6-885d-cf2788d25a6d",
  "type": "user",
  "uuid": "119f2ff0-1478-41bd-a7f8-e9be49680d8c",
  "toolUseResult": {
    "stdout": "Page 1: Generational Depth Estimation of Recursive Synthetic Text: |                           Measuring the Discrimination Bounda\nPage 2: 084            ∗ |             Kempirical =3), and quantifies boundary sensi-         benchmarks like RAID (Dugan et al., \nPage 3: Seed Corpus             Recursive                Feature                       OBD               K * Estimation |         \nPage 4: Table 1: Experimental configurations for depth-chain                                                  K * boundary |      \nPage 5: Table 2: Pairwise AUC for adjacent depth pairs with bootstrap 95% CIs and permutation p-values for boundary |             \nPage 6: = 0.60 |  |                                                   (a) Pairwise AUC profile                                      \nPage 7: 413   4.6    Binary Detector Confidence                              Table 5: Downstream task performance (MMLU, Hel- |   \nPage 8: 499   one depth level of sensitivity for cross-model               Prompt-chain scope and retrain-chain gap.            \nPage 9: 597   Limitations                                                  Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi     \nPage 10: 698   Yanzhu Guo, Guokan Shang, Michalis Vazirgiannis, and              Zhen Sun, Zongmin Zhang, Xinyue Shen, Ziyi Zhang\nPage 11: 802   A       Supplementary Materials                                                        0.5975 |                     \nPage 12: Table 9: Pairwise AUC with bootstrap 95% CIs across depth pairs for four decoding configurations (all using | Qwen2.5-1.5B",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a32fea5c-b905-4b23-8f9e-d8a85e9d1d21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-23T07:56:40.132Z_

<details><summary>Logged reasoning block</summary>

```text
So:
- Pages 1-8: Main text (page 8 ends with content, page 9 starts with "Limitations" which is part of the main text)
- Wait, page 9 starts with "Limitations" - that's still main text. Let me check more carefully.

Looking at page 9: "Limitations" and then "References" start. Page 10 seems to have more references. Page 11 starts appendix.

So the main text structure:
- Pages 1-8: Main body content


- Page 9: Limitations section + start of References
- Page 10: More references
- Page 11+: Appendix

But the user said "8 pages正文" - in EMNLP format, the 8-page limit is for main text, with references and limitations not counting. Let me re-check the guidelines: EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit.

So limitations doesn't count toward the page limit. I need to find where the main text actually ends before the Limitations section begins.

Looking at the page breaks: Page 8 ends with line 499 from the discussion section, and Page 9 starts with line 597 showing "Limitations". This means the main text spans pages 1-8, which is exactly 8 pages as required. The structure checks out.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "119f2ff0-1478-41bd-a7f8-e9be49680d8c",
  "isSidechain": false,
  "requestId": "req_011CbK9FJxNmNtP9ujsVeLdx",
  "type": "assistant",
  "uuid": "9a55ccfb-9b05-42f8-a6cc-5aea80d4f2e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TktWMH54Thirf6zVUjPTbW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 43560,
      "output_tokens": 826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 826,
          "cache_read_input_tokens": 43560,
          "cache_creation_input_tokens": 610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 610
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

_source line 28 · 2026-05-23T07:56:45.780Z_

结果汇报：

**编译状态**：0 errors，PDF 生成成功（18 页总计）。

**Pythia-1.4B AUC 数据一致性**：Table 2 与 Table 10 完全一致 ✓

| Depth Pair | Table 2 | Table 10 | 匹配 |
|---|---|---|---|
| 0v1 | .9722 | .9722 | ✓ |
| 1v2 | .6074 | .6074 | ✓ |
| 2v3 | .5440 | .5440 | ✓ |
| 3v4 | .5051 | .5051 | ✓ |
| 4v5 | .5079 | .5079 | ✓ |

与预期值完全吻合：0v1=.9722, 1v2=.6074, 2v3=.5440, 3v4=.5051, 4v5=.5079 ✓

**CI 一致性**：
- 1v2 CI：两表均为 [.598, .617] ✓
- 2v3 CI：两表均为 [.534, .554] ✓

**页数**：正文 8 页（pages 1-8），Limitations 从第 9 页开始（不计入页数限制），符合 EMNLP 2026 要求 ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a55ccfb-9b05-42f8-a6cc-5aea80d4f2e6",
  "isSidechain": false,
  "requestId": "req_011CbK9FJxNmNtP9ujsVeLdx",
  "type": "assistant",
  "uuid": "920b87d0-d5d4-4e21-ba74-ed7b0b806741",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TktWMH54Thirf6zVUjPTbW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 43560,
      "output_tokens": 826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 826,
          "cache_read_input_tokens": 43560,
          "cache_creation_input_tokens": 610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 610
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

_source line 29_

```json
{
  "type": "last-prompt",
  "leafUuid": "920b87d0-d5d4-4e21-ba74-ed7b0b806741",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile paper and verify Pythia AUC consistency",
  "sessionId": "99cf8106-e8a7-456c-8eba-4cb2eb8f94c0"
}
```

---
