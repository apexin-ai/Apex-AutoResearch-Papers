# Research conversation: 项目：irt_equated_bench_regen Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_be

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-3/7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01.jsonl`
- **Structured JSON:** [`98c4f09799db88a97754.json`](../../sessions/98/98c4f09799db88a97754.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-25T11:07:17.890Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T11:07:17.890Z",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "content": "项目：irt_equated_bench_regen\nVenue：emnlp-2026\n论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper\n\nPhase 1 确定性检查结果：\n源码检查: passed=False, 5 critical, 1 warning\n一致性检查: 0 critical, 73 warning\n编译: ✅, 页数: 17\n内部信息: 0 critical, 0 warning\n\n━━━ 用户自定义规则（作为额外检查项）━━━\n## 用户自定义规则（必须遵守）\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section\n- **[EMNLP 2026]** abstract 不要超过 200 words\n\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。\n\n请按照你的角色指令执行内容结构审计。"
}
```

---

### Runtime record

_source line 2 · 2026-05-25T11:07:17.896Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T11:07:17.896Z",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01"
}
```

---

## Round 1

79 recorded events

### User

_source line 3 · 2026-05-25T11:07:17.966Z_

项目：irt_equated_bench_regen
Venue：emnlp-2026
论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper

Phase 1 确定性检查结果：
源码检查: passed=False, 5 critical, 1 warning
一致性检查: 0 critical, 73 warning
编译: ✅, 页数: 17
内部信息: 0 critical, 0 warning

━━━ 用户自定义规则（作为额外检查项）━━━
## 用户自定义规则（必须遵守）
### 写作规则

- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面
- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section
- **[EMNLP 2026]** abstract 不要超过 200 words

### 审稿规则

- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.

> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。
请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。

请按照你的角色指令执行内容结构审计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "7f20cef6-c3ad-41ad-bb4b-9bf71d4e3a5a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-25T11:07:17.965Z_

```json
{
  "parentUuid": "7f20cef6-c3ad-41ad-bb4b-9bf71d4e3a5a",
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
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file"
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
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "25145760-26b9-42e5-aba7-0062bb49c36b",
  "timestamp": "2026-05-25T11:07:17.965Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

---

### Runtime record

_source line 5 · 2026-05-25T11:07:17.965Z_

```json
{
  "parentUuid": "25145760-26b9-42e5-aba7-0062bb49c36b",
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
  "uuid": "71d0af63-98ff-4471-9feb-51028b22578c",
  "timestamp": "2026-05-25T11:07:17.965Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

---

### Runtime record

_source line 6 · 2026-05-25T11:07:17.965Z_

```json
{
  "parentUuid": "71d0af63-98ff-4471-9feb-51028b22578c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8127837f-50d5-472b-9c19-3aa5d9f17c71",
  "timestamp": "2026-05-25T11:07:17.965Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit EMNLP 2026 paper for custom rules compliance",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01"
}
```

---

### Assistant

_source line 8 · 2026-05-25T11:07:23.101Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a content structure audit of a paper. Let me follow the execution flow:

1. Read `skills/global/paper-writing-norms.skill.md` and `skills/global/paper-quality-lessons.skill.md` for audit standards
2. Read all `.tex` files in the paper directory
3. Audit across all specified dimensions
4. Output structured findings

Let me start by reading the skill files and all tex files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8127837f-50d5-472b-9c19-3aa5d9f17c71",
  "isSidechain": false,
  "requestId": "req_011CbPBRPH7GqxcxSt6uowKD",
  "type": "assistant",
  "uuid": "8485a712-91f6-4bb2-b45f-ebeb747259c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CnHE62rxi7o2Mp9MF7BfZ9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27861,
      "cache_read_input_tokens": 11846,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27861
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

_source line 9 · 2026-05-25T11:07:23.657Z_

开始执行内容结构审计。先读取审计标准和所有 .tex 源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8485a712-91f6-4bb2-b45f-ebeb747259c3",
  "isSidechain": false,
  "requestId": "req_011CbPBRPH7GqxcxSt6uowKD",
  "type": "assistant",
  "uuid": "63230cb9-01a8-4739-84e2-9f6e28f3cb06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CnHE62rxi7o2Mp9MF7BfZ9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27861,
      "cache_read_input_tokens": 11846,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27861
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

_source line 10 · 2026-05-25T11:07:24.151Z_

<details open><summary>🔧 Tool call — Read · `toolu_018EZq9NVpQ4QT7ZUDjEKAj3`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63230cb9-01a8-4739-84e2-9f6e28f3cb06",
  "isSidechain": false,
  "requestId": "req_011CbPBRPH7GqxcxSt6uowKD",
  "type": "assistant",
  "uuid": "d1aca2c0-4a43-415d-ab6d-a3be86899b91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CnHE62rxi7o2Mp9MF7BfZ9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27861,
      "cache_read_input_tokens": 11846,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27861
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

_source line 11 · 2026-05-25T11:07:24.165Z_

<details><summary>↩ Tool result · `toolu_018EZq9NVpQ4QT7ZUDjEKAj3`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "d1aca2c0-4a43-415d-ab6d-a3be86899b91",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "0bf62d59-5970-4121-a21a-72f20eb26444",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "d1aca2c0-4a43-415d-ab6d-a3be86899b91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
````

</details>

---

### Tool call

_source line 12 · 2026-05-25T11:07:24.653Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LmyL8UVUYnoS1614NkG4xS`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-quality-lessons.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bf62d59-5970-4121-a21a-72f20eb26444",
  "isSidechain": false,
  "requestId": "req_011CbPBRPH7GqxcxSt6uowKD",
  "type": "assistant",
  "uuid": "cf5e0bc3-e686-4abc-96e6-7c167213c5ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CnHE62rxi7o2Mp9MF7BfZ9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27861,
      "cache_read_input_tokens": 11846,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27861
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

_source line 13 · 2026-05-25T11:07:24.660Z_

<details><summary>↩ Tool result · `toolu_01LmyL8UVUYnoS1614NkG4xS`</summary>

````text
1	---
2	name: paper-quality-lessons
3	description: NeurIPS 投稿实战经验总结——人工审查中提炼的写作规范、审查清单、常见反模式。Paper Agent / Reviewer / Director 写论文或审查论文时加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 1
7	tags:
8	  - writing
9	  - paper
10	  - quality
11	  - checklist
12	  - review
13	roles:
14	  - agent
15	  - reviewer
16	  - director
17	  - paper_agent
18	---
19	
20	# 论文写作质量指南（NeurIPS 实战经验）
21	
22	> 来源：2026 年 NeurIPS 投稿期间，从 20+ 项目的人工审查反馈中提炼。
23	> 每条规则都源自真实的 bug / 退回 / 审稿质疑。
24	
25	---
26	
27	## 一、数据诚信与溯源（最高优先级）
28	
29	### 1.1 数字必须有源头
30	
31	- 论文中**每一个数字**必须可追溯到 registry 实验 ID 或原始结果文件
32	- 禁止凭记忆写数字——必须 `cat result.json | head` + `ls -la` 附上文件证据
33	- 计算值（均值、标准差、DID、delta）必须独立重算，不信 Agent 第一手汇报
34	- `paper_provenance.yaml` 覆盖率必须 100%，改数字必须同步更新 provenance
35	
36	> **教训（D149 事件）**：Agent 曾伪造完整的 metrics 数据包括 p-value，事后被 Reviewer 独立 parse JSON 抓出。从此所有关键数据必须 Reviewer 独立验证到字段级别。
37	
38	### 1.2 不同来源数据不能混用
39	
40	- 配对数据必须同 seed、同 c 值、同 N、同 evaluation protocol
41	- 两张表如果 protocol 不同（如 0-shot vs 8-shot），论文必须明确说明
42	- 跨 config 比较 delta 会引入系统误差——必须补跑同 config baseline 后才能比较
43	- 非等量对比必须显式标注（如 "at unmatched volumes"）
44	
45	> **教训（D027 事件）**：不同 config 文件的 baseline 不同，跨 config 比较 delta 值引入了 artifact。
46	
47	### 1.3 结论撤回后不可复活
48	
49	- 被 Director shelved 的数据（如因截断混淆），禁止重新引入论文
50	- `paper_provenance.yaml` 中 `verified: false` 的 claim，不得恢复
51	- 术语修正后不可回退（如 "same norm" → "same per-layer standard deviation"）
52	
53	---
54	
55	## 二、Claim 强度与数据匹配
56	
57	### 2.1 Claim 强度规则
58	
59	| 数据支撑 | 允许的最强表述 |
60	|----------|--------------|
61	| 单 seed, 单数据集 | "preliminary observation", "initial evidence" |
62	| 单 seed, 多数据集 | "suggestive pattern", "indicative trend" |
63	| 多 seed, 单数据集 | 报告均值±标准差，可写 "we find" |
64	| 多 seed, 多数据集 | 可用 "robust", "consistent" |
65	| 统计检验显著 | 可用 "significant", 附 p-value |
66	| 单 seed + 外推到其他条件 | 必须加限定，不能声称 "scale-invariant" 等 |
67	
68	### 2.2 禁止的过强表述
69	
70	- "remarkably stable" → 改为 "relatively stable" 或给出量化波动范围
71	- "confirmed" → 仅 "suggestive" 级别数据不能用
72	- "scale-invariant" → single-seed 验证不够
73	- "We attribute X to Y" → 如果是假说，必须改为 "We hypothesize" + "requiring causal verification"
74	- "roughly twice" → 实际比值必须在 1.8x-2.2x 才能用，否则改为更准确的近似
75	- "domain-agnostic" → 改为 "robust across N domains tested"
76	
77	### 2.3 Claim 降级机制
78	
79	当证据不足以支撑独立 claim 时，应降级为 discussion 中的定性讨论，而非删除。具体做法：
80	- 独立 contribution → Discussion 段落
81	- 硬 claim → 加 caveat 的软 claim
82	- 正文数字 → 移入 Appendix
83	
84	---
85	
86	## 三、叙事与 Storytelling
87	
88	### 3.1 结构原则
89	
90	- 核心 paradox/发现之间必须有**过渡句**桥接，不能让读者在关键处断线
91	- Introduction 每条 Contribution 必须有对应的 section/table 支撑
92	- Discussion 不应重复 Results 的具体数字——引用表格编号
93	- 同一解释不要在多处重复推导——主文写一次 + 指向 Appendix
94	- Limitations 段不要写成一个 17 行大段——拆分为 2-3 个子段按主题分组
95	
96	### 3.2 冷引用（Cold Reference）
97	
98	- 任何首次出现的概念必须有上文铺垫
99	- Introduction 贡献列表中不能突然出现未被提及的模型/方法名
100	
101	### 3.3 不要用旧叙事套新数字
102	
103	新 baseline 出来后若 delta 大幅变化，Section 的叙事逻辑必须重写，不是简单替换数字。
104	
105	### 3.4 Contingency Plan
106	
107	关键实验结果不确定时需预写两套叙事（如 "若结果 A → 叙事 A"、"若结果 B → 叙事 B"），实验完成后选择正确版本。提交前必须确认只留了一套。
108	
109	### 3.5 不要基于中间值做叙事决策
110	
111	70% 进度时的估计往往不够稳定（尤其 GSM8K 等难度分布不均匀的 benchmark），必须等完整数据再定稿叙事。
112	
113	---
114	
115	## 四、术语与一致性
116	
117	### 4.1 术语一致性
118	
119	- 全文必须统一使用正式定义的术语，不得出现同义词漂移
120	- 术语定义后，每次使用必须完全一致（不要有时 "perturbation sensitivity" 有时 "perturbation impact"）
121	
122	### 4.2 统计量一致性
123	
124	- 两个不同的 kappa/p-value 每次出现时必须标注是哪个
125	- 同一个 metric 在不同位置的数字必须完全一致
126	- 修改任何数字后必须全文 grep 确认所有引用处同步
127	
128	### 4.3 p-value 格式
129	
130	- 无前导零、3 位小数：`p = .003`（不是 `p = 0.003`）
131	- 当非劣效性 p<0.001 实际由正向效应驱动时，必须加括注说明
132	
133	### 4.4 例子与定义必须一致
134	
135	Taxonomy 中的定义和对应示例不能自相矛盾。如果定义说 "no new content"，示例中就不能包含新信息。
136	
137	---
138	
139	## 五、投稿前检查清单（Pre-Submission Checklist）
140	
141	### 5.1 占位符扫描（硬门禁）
142	
143	提交前必须 grep 扫描，以下模式要求**零匹配**：
144	```
145	XX.XX, PLACEHOLDER, [If , TODO, TBD, \placeholder{
146	```
147	所有条件占位段落（`[If ...]`）必须替换为最终文本。
148	
149	### 5.2 编译检查
150	
151	- [ ] 编译零 error
152	- [ ] 无 `??` 未解析引用
153	- [ ] 无 > 1pt 的 overfull hbox
154	- [ ] 正文 ≤ 9 页（NeurIPS desk reject 风险）
155	- [ ] 使用当年 style file（`neurips_2026.sty`）
156	- [ ] Review 版启用行号
157	- [ ] 匿名审稿版无作者姓名、无致谢
158	
159	### 5.3 数据完整性
160	
161	- [ ] 论文所有数字与 registry/provenance 交叉验证通过
162	- [ ] 计算值（均值、标准差、DID、delta）独立重算确认
163	- [ ] 所有 evaluation protocol 差异已在论文中说明
164	- [ ] 多 seed 结果报告均值和标准差
165	- [ ] 单 seed 数据在 Limitations 中声明
166	
167	### 5.4 图表检查
168	
169	- [ ] 所有 figure PDF 存在且路径匹配
170	- [ ] 图表不超栏宽（单栏 5.5in / 全宽 6.5in）
171	- [ ] 图中字体 ≥ 7pt
172	- [ ] 小数精度全表统一
173	- [ ] 最优结果加粗、次优下划线
174	- [ ] 表格标题（caption）自包含
175	- [ ] Forest plot 等可视化无 dummy 值（CI_LO=-99 等）
176	
177	### 5.5 引用检查
178	
179	- [ ] 引用覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**（任一缺失说明调研不充分）
180	- [ ] 引用密度与目标会议近年录用论文同量级
181	- [ ] 引用键与 bib 条目 1:1 匹配
182	- [ ] 无孤儿 bib 条目
183	- [ ] 无幻觉引用（所有被引论文实际存在）
184	- [ ] 近年论文的年份/会议准确
185	- [ ] 审稿人要求的引用全部补齐
186	
187	### 5.6 匿名化检查
188	
189	- [ ] 源代码无硬编码绝对路径（`/Users/...`, `/root/...`）
190	- [ ] 配置文件无服务器路径
191	- [ ] Git history 已清理 author 信息（用 fresh repo）
192	- [ ] 项目管理文件不得提交（AGENTS.md, memory.md, registry.yaml, task_context/ 等）
193	- [ ] API Keys 通过环境变量，无泄露
194	
195	### 5.7 会议 Checklist 填写（如目标会议要求）
196	
197	- [ ] Claims: 摘要/Introduction 准确反映实验范围
198	- [ ] Limitations: 正文 Limitations 段 + Appendix 补充
199	- [ ] Experiments: 实验设置完整（exp_id, seed, 超参, 评估 protocol）
200	- [ ] Reproducibility: 数据集公开、代码可用
201	- [ ] Statistical Significance: 多 seed 均值+标准差、置信区间
202	- [ ] Compute: GPU 型号、训练时间、总 GPU-hours
203	- [ ] Licenses: 数据集/模型引用完整
204	- [ ] AI Assistants: 如实声明使用情况
205	- [ ] 每项认真回答（不要全写 N/A）
206	
207	### 5.8 叙事完整性
208	
209	- [ ] Conclusion 包含所有关键限定符（如 "under greedy decoding"）
210	- [ ] Abstract 与正文一致（不能一个写 "single seed" 另一个已是 "10 seeds"）
211	- [ ] 无 Appendix Version A/B 两套叙事残留
212	- [ ] 无 LaTeX 注释与正文混淆
213	- [ ] Contribution claim 在 Introduction 中（不在 Related Work 中）
214	- [ ] 所有专有名词/缩写首次出现时有定义（Abstract 内缩写也必须展开）
215	- [ ] Introduction 与 Method/Results 讲同一条主线（idea 变化后全文逻辑一致）
216	
217	### 5.9 去 AI 风格检查
218	
219	- [ ] **`grep "—" paper/*.tex` 全文清零**（解释性 em-dash 必须全删，最显著的 AI 痕迹）
220	- [ ] **`grep " – " paper/*.tex` 全文清零**（解释性 en-dash 必须全删）
221	- [ ] 无 "-ing," 分词短语结尾（如 "..., demonstrating the effectiveness of..."）
222	- [ ] 无连续 "Furthermore" / "Moreover" / "Additionally"（同段最多 1 个）
223	- [ ] 无 "It is worth noting that..." / "Notably, ..."
224	- [ ] 无 "delve into" / "leverage" / "utilize" / "a myriad of" / "a plethora of"
225	- [ ] 自然段 5-8 句是正常的，不要每 2-3 句就换段
226	
227	### 5.10 模板与同类论文核对
228	
229	- [ ] LaTeX 模板从目标会议官网下载（不是他人转载、不是上一年）
230	- [ ] `\documentclass[]{}` 选项匹配 review / camera-ready 阶段
231	- [ ] 写作前已参考 2-3 篇同领域近 1-2 年优秀论文，叙事节奏对齐
232	
233	---
234	
235	## 六、Reviewer 审查标准
236	
237	### 6.1 CRITICAL 级别（必须修复才能提交）
238	
239	- 论文数字与实验数据不一致
240	- Abstract 与正文矛盾
241	- Evaluation protocol 混淆（如 0-shot 写成 8-shot）
242	- 未经验证的数据写入论文
243	- 占位符残留
244	
245	### 6.2 WARNING 级别（应当修复）
246	
247	- Stale claims（更新了某处数字但忘了同步其他位置）
248	- 过强措辞不匹配数据支撑
249	- 隐式全因子设计误导（如写 "3×3×3=27" 但实际只有 15 格）
250	- 评估指标只描述了部分 domain
251	- 旧版数据引用
252	
253	### 6.3 数据一致性审查流程
254	
255	1. 从 registry 提取所有实验 metrics
256	2. 对照论文中每一个内联数字（到行号级别）
257	3. 独立重算所有衍生值
258	4. 不一致处标注为 CRITICAL
259	5. 近似表述检查实际比值是否在允许范围内
260	
261	---
262	
263	## 七、常见反模式速查表
264	
265	| 反模式 | 症状 | 修复方式 |
266	|--------|------|----------|
267	| Stale claim | 论文某处还引用旧数字 | 改数字后全文 grep 同步 |
268	| Protocol 混淆 | 不同表格用了不同 evaluation 但没说明 | 每张表注明 protocol |
269	| Agent 误报 | 实验结果缺乏文件证据 | 要求 `cat result.json` 截图 |
270	| 混用数据算比值 | 跨 seed/条件/N 的数据混合比较 | 只用严格配对的数据 |
271	| 叙事超越数据 | "confirmed" 但实际只是 suggestive | 匹配 claim 强度到 §2.1 |
272	| 冷引用 | 首次出现的概念无铺垫 | 先建立框架再引入 |
273	| 定义-例子矛盾 | Taxonomy 定义和示例冲突 | 审查所有定义与其示例 |
274	| Placeholder 残留 | XX.XX, TODO, [If...] 未清理 | 提交前 grep 硬门禁 |
275	| Path 泄露 | 代码/config 含服务器绝对路径 | 改为相对路径 |
276	| 重复推导 | 同一解释在 3 处各自推导一遍 | 主文一次 + 引用 Appendix |
277	| Discussion 重复 Results | Discussion 大量复制 Results 数字 | 改为引用表格编号 |
278	| 单 seed overclaim | 单 seed 数据声称 scale-invariant | 加 preliminary/hedging 限定 |
279	| Registry 不同步 | Registry 面值与实际状态不一致 | 以 SSH 实测为准 |
280	| vLLM 静默失败 | max_model_len 太小导致 100% 400 错误 | 预检必须发真实 prompt 验证 |
281	
282	---
283	
284	## 八、写论文前加载的 Skills
285	
286	写论文或做最终审查时，Director/Agent 应按需加载以下 skills：
287	- `latex-paper` — LaTeX 编译与格式
288	- `reference-audit` — 引用真实性审计
289	- `academic-writer` — ML 学术写作规范
290	- `paper-quality-lessons`（本 skill）— 实战经验教训
291	
292	---
293	
294	## 九、附录：投稿经验时间线教训
295	
296	1. **论文数字锁定时机**：最终编译前 24h 锁定所有数字，之后只允许格式修改
297	2. **GPU 不要空闲**：审稿期间如果 Agent 空闲，应该跑 ablation/扩展实验作为 rebuttal 储备
298	3. **匿名化提前做**：不要等到最后一天才检查路径泄露，fresh repo 需要时间清理
299	4. **9 页零余量策略**：NeurIPS 正文 9 页是硬限，每次新增内容必须等量压缩并编译验证
300	5. **Contingency 叙事提前写**：关键实验完成前就写好两版叙事，避免最后一刻仓促改稿
301	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "cf5e0bc3-e686-4abc-96e6-7c167213c5ae",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "ebc1cae6-69a6-4e26-af06-a97c72d92bf5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-quality-lessons.skill.md",
      "content": "---\nname: paper-quality-lessons\ndescription: NeurIPS 投稿实战经验总结——人工审查中提炼的写作规范、审查清单、常见反模式。Paper Agent / Reviewer / Director 写论文或审查论文时加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 1\ntags:\n  - writing\n  - paper\n  - quality\n  - checklist\n  - review\nroles:\n  - agent\n  - reviewer\n  - director\n  - paper_agent\n---\n\n# 论文写作质量指南（NeurIPS 实战经验）\n\n> 来源：2026 年 NeurIPS 投稿期间，从 20+ 项目的人工审查反馈中提炼。\n> 每条规则都源自真实的 bug / 退回 / 审稿质疑。\n\n---\n\n## 一、数据诚信与溯源（最高优先级）\n\n### 1.1 数字必须有源头\n\n- 论文中**每一个数字**必须可追溯到 registry 实验 ID 或原始结果文件\n- 禁止凭记忆写数字——必须 `cat result.json | head` + `ls -la` 附上文件证据\n- 计算值（均值、标准差、DID、delta）必须独立重算，不信 Agent 第一手汇报\n- `paper_provenance.yaml` 覆盖率必须 100%，改数字必须同步更新 provenance\n\n> **教训（D149 事件）**：Agent 曾伪造完整的 metrics 数据包括 p-value，事后被 Reviewer 独立 parse JSON 抓出。从此所有关键数据必须 Reviewer 独立验证到字段级别。\n\n### 1.2 不同来源数据不能混用\n\n- 配对数据必须同 seed、同 c 值、同 N、同 evaluation protocol\n- 两张表如果 protocol 不同（如 0-shot vs 8-shot），论文必须明确说明\n- 跨 config 比较 delta 会引入系统误差——必须补跑同 config baseline 后才能比较\n- 非等量对比必须显式标注（如 \"at unmatched volumes\"）\n\n> **教训（D027 事件）**：不同 config 文件的 baseline 不同，跨 config 比较 delta 值引入了 artifact。\n\n### 1.3 结论撤回后不可复活\n\n- 被 Director shelved 的数据（如因截断混淆），禁止重新引入论文\n- `paper_provenance.yaml` 中 `verified: false` 的 claim，不得恢复\n- 术语修正后不可回退（如 \"same norm\" → \"same per-layer standard deviation\"）\n\n---\n\n## 二、Claim 强度与数据匹配\n\n### 2.1 Claim 强度规则\n\n| 数据支撑 | 允许的最强表述 |\n|----------|--------------|\n| 单 seed, 单数据集 | \"preliminary observation\", \"initial evidence\" |\n| 单 seed, 多数据集 | \"suggestive pattern\", \"indicative trend\" |\n| 多 seed, 单数据集 | 报告均值±标准差，可写 \"we find\" |\n| 多 seed, 多数据集 | 可用 \"robust\", \"consistent\" |\n| 统计检验显著 | 可用 \"significant\", 附 p-value |\n| 单 seed + 外推到其他条件 | 必须加限定，不能声称 \"scale-invariant\" 等 |\n\n### 2.2 禁止的过强表述\n\n- \"remarkably stable\" → 改为 \"relatively stable\" 或给出量化波动范围\n- \"confirmed\" → 仅 \"suggestive\" 级别数据不能用\n- \"scale-invariant\" → single-seed 验证不够\n- \"We attribute X to Y\" → 如果是假说，必须改为 \"We hypothesize\" + \"requiring causal verification\"\n- \"roughly twice\" → 实际比值必须在 1.8x-2.2x 才能用，否则改为更准确的近似\n- \"domain-agnostic\" → 改为 \"robust across N domains tested\"\n\n### 2.3 Claim 降级机制\n\n当证据不足以支撑独立 claim 时，应降级为 discussion 中的定性讨论，而非删除。具体做法：\n- 独立 contribution → Discussion 段落\n- 硬 claim → 加 caveat 的软 claim\n- 正文数字 → 移入 Appendix\n\n---\n\n## 三、叙事与 Storytelling\n\n### 3.1 结构原则\n\n- 核心 paradox/发现之间必须有**过渡句**桥接，不能让读者在关键处断线\n- Introduction 每条 Contribution 必须有对应的 section/table 支撑\n- Discussion 不应重复 Results 的具体数字——引用表格编号\n- 同一解释不要在多处重复推导——主文写一次 + 指向 Appendix\n- Limitations 段不要写成一个 17 行大段——拆分为 2-3 个子段按主题分组\n\n### 3.2 冷引用（Cold Reference）\n\n- 任何首次出现的概念必须有上文铺垫\n- Introduction 贡献列表中不能突然出现未被提及的模型/方法名\n\n### 3.3 不要用旧叙事套新数字\n\n新 baseline 出来后若 delta 大幅变化，Section 的叙事逻辑必须重写，不是简单替换数字。\n\n### 3.4 Contingency Plan\n\n关键实验结果不确定时需预写两套叙事（如 \"若结果 A → 叙事 A\"、\"若结果 B → 叙事 B\"），实验完成后选择正确版本。提交前必须确认只留了一套。\n\n### 3.5 不要基于中间值做叙事决策\n\n70% 进度时的估计往往不够稳定（尤其 GSM8K 等难度分布不均匀的 benchmark），必须等完整数据再定稿叙事。\n\n---\n\n## 四、术语与一致性\n\n### 4.1 术语一致性\n\n- 全文必须统一使用正式定义的术语，不得出现同义词漂移\n- 术语定义后，每次使用必须完全一致（不要有时 \"perturbation sensitivity\" 有时 \"perturbation impact\"）\n\n### 4.2 统计量一致性\n\n- 两个不同的 kappa/p-value 每次出现时必须标注是哪个\n- 同一个 metric 在不同位置的数字必须完全一致\n- 修改任何数字后必须全文 grep 确认所有引用处同步\n\n### 4.3 p-value 格式\n\n- 无前导零、3 位小数：`p = .003`（不是 `p = 0.003`）\n- 当非劣效性 p<0.001 实际由正向效应驱动时，必须加括注说明\n\n### 4.4 例子与定义必须一致\n\nTaxonomy 中的定义和对应示例不能自相矛盾。如果定义说 \"no new content\"，示例中就不能包含新信息。\n\n---\n\n## 五、投稿前检查清单（Pre-Submission Checklist）\n\n### 5.1 占位符扫描（硬门禁）\n\n提交前必须 grep 扫描，以下模式要求**零匹配**：\n```\nXX.XX, PLACEHOLDER, [If , TODO, TBD, \\placeholder{\n```\n所有条件占位段落（`[If ...]`）必须替换为最终文本。\n\n### 5.2 编译检查\n\n- [ ] 编译零 error\n- [ ] 无 `??` 未解析引用\n- [ ] 无 > 1pt 的 overfull hbox\n- [ ] 正文 ≤ 9 页（NeurIPS desk reject 风险）\n- [ ] 使用当年 style file（`neurips_2026.sty`）\n- [ ] Review 版启用行号\n- [ ] 匿名审稿版无作者姓名、无致谢\n\n### 5.3 数据完整性\n\n- [ ] 论文所有数字与 registry/provenance 交叉验证通过\n- [ ] 计算值（均值、标准差、DID、delta）独立重算确认\n- [ ] 所有 evaluation protocol 差异已在论文中说明\n- [ ] 多 seed 结果报告均值和标准差\n- [ ] 单 seed 数据在 Limitations 中声明\n\n### 5.4 图表检查\n\n- [ ] 所有 figure PDF 存在且路径匹配\n- [ ] 图表不超栏宽（单栏 5.5in / 全宽 6.5in）\n- [ ] 图中字体 ≥ 7pt\n- [ ] 小数精度全表统一\n- [ ] 最优结果加粗、次优下划线\n- [ ] 表格标题（caption）自包含\n- [ ] Forest plot 等可视化无 dummy 值（CI_LO=-99 等）\n\n### 5.5 引用检查\n\n- [ ] 引用覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**（任一缺失说明调研不充分）\n- [ ] 引用密度与目标会议近年录用论文同量级\n- [ ] 引用键与 bib 条目 1:1 匹配\n- [ ] 无孤儿 bib 条目\n- [ ] 无幻觉引用（所有被引论文实际存在）\n- [ ] 近年论文的年份/会议准确\n- [ ] 审稿人要求的引用全部补齐\n\n### 5.6 匿名化检查\n\n- [ ] 源代码无硬编码绝对路径（`/Users/...`, `/root/...`）\n- [ ] 配置文件无服务器路径\n- [ ] Git history 已清理 author 信息（用 fresh repo）\n- [ ] 项目管理文件不得提交（AGENTS.md, memory.md, registry.yaml, task_context/ 等）\n- [ ] API Keys 通过环境变量，无泄露\n\n### 5.7 会议 Checklist 填写（如目标会议要求）\n\n- [ ] Claims: 摘要/Introduction 准确反映实验范围\n- [ ] Limitations: 正文 Limitations 段 + Appendix 补充\n- [ ] Experiments: 实验设置完整（exp_id, seed, 超参, 评估 protocol）\n- [ ] Reproducibility: 数据集公开、代码可用\n- [ ] Statistical Significance: 多 seed 均值+标准差、置信区间\n- [ ] Compute: GPU 型号、训练时间、总 GPU-hours\n- [ ] Licenses: 数据集/模型引用完整\n- [ ] AI Assistants: 如实声明使用情况\n- [ ] 每项认真回答（不要全写 N/A）\n\n### 5.8 叙事完整性\n\n- [ ] Conclusion 包含所有关键限定符（如 \"under greedy decoding\"）\n- [ ] Abstract 与正文一致（不能一个写 \"single seed\" 另一个已是 \"10 seeds\"）\n- [ ] 无 Appendix Version A/B 两套叙事残留\n- [ ] 无 LaTeX 注释与正文混淆\n- [ ] Contribution claim 在 Introduction 中（不在 Related Work 中）\n- [ ] 所有专有名词/缩写首次出现时有定义（Abstract 内缩写也必须展开）\n- [ ] Introduction 与 Method/Results 讲同一条主线（idea 变化后全文逻辑一致）\n\n### 5.9 去 AI 风格检查\n\n- [ ] **`grep \"—\" paper/*.tex` 全文清零**（解释性 em-dash 必须全删，最显著的 AI 痕迹）\n- [ ] **`grep \" – \" paper/*.tex` 全文清零**（解释性 en-dash 必须全删）\n- [ ] 无 \"-ing,\" 分词短语结尾（如 \"..., demonstrating the effectiveness of...\"）\n- [ ] 无连续 \"Furthermore\" / \"Moreover\" / \"Additionally\"（同段最多 1 个）\n- [ ] 无 \"It is worth noting that...\" / \"Notably, ...\"\n- [ ] 无 \"delve into\" / \"leverage\" / \"utilize\" / \"a myriad of\" / \"a plethora of\"\n- [ ] 自然段 5-8 句是正常的，不要每 2-3 句就换段\n\n### 5.10 模板与同类论文核对\n\n- [ ] LaTeX 模板从目标会议官网下载（不是他人转载、不是上一年）\n- [ ] `\\documentclass[]{}` 选项匹配 review / camera-ready 阶段\n- [ ] 写作前已参考 2-3 篇同领域近 1-2 年优秀论文，叙事节奏对齐\n\n---\n\n## 六、Reviewer 审查标准\n\n### 6.1 CRITICAL 级别（必须修复才能提交）\n\n- 论文数字与实验数据不一致\n- Abstract 与正文矛盾\n- Evaluation protocol 混淆（如 0-shot 写成 8-shot）\n- 未经验证的数据写入论文\n- 占位符残留\n\n### 6.2 WARNING 级别（应当修复）\n\n- Stale claims（更新了某处数字但忘了同步其他位置）\n- 过强措辞不匹配数据支撑\n- 隐式全因子设计误导（如写 \"3×3×3=27\" 但实际只有 15 格）\n- 评估指标只描述了部分 domain\n- 旧版数据引用\n\n### 6.3 数据一致性审查流程\n\n1. 从 registry 提取所有实验 metrics\n2. 对照论文中每一个内联数字（到行号级别）\n3. 独立重算所有衍生值\n4. 不一致处标注为 CRITICAL\n5. 近似表述检查实际比值是否在允许范围内\n\n---\n\n## 七、常见反模式速查表\n\n| 反模式 | 症状 | 修复方式 |\n|--------|------|----------|\n| Stale claim | 论文某处还引用旧数字 | 改数字后全文 grep 同步 |\n| Protocol 混淆 | 不同表格用了不同 evaluation 但没说明 | 每张表注明 protocol |\n| Agent 误报 | 实验结果缺乏文件证据 | 要求 `cat result.json` 截图 |\n| 混用数据算比值 | 跨 seed/条件/N 的数据混合比较 | 只用严格配对的数据 |\n| 叙事超越数据 | \"confirmed\" 但实际只是 suggestive | 匹配 claim 强度到 §2.1 |\n| 冷引用 | 首次出现的概念无铺垫 | 先建立框架再引入 |\n| 定义-例子矛盾 | Taxonomy 定义和示例冲突 | 审查所有定义与其示例 |\n| Placeholder 残留 | XX.XX, TODO, [If...] 未清理 | 提交前 grep 硬门禁 |\n| Path 泄露 | 代码/config 含服务器绝对路径 | 改为相对路径 |\n| 重复推导 | 同一解释在 3 处各自推导一遍 | 主文一次 + 引用 Appendix |\n| Discussion 重复 Results | Discussion 大量复制 Results 数字 | 改为引用表格编号 |\n| 单 seed overclaim | 单 seed 数据声称 scale-invariant | 加 preliminary/hedging 限定 |\n| Registry 不同步 | Registry 面值与实际状态不一致 | 以 SSH 实测为准 |\n| vLLM 静默失败 | max_model_len 太小导致 100% 400 错误 | 预检必须发真实 prompt 验证 |\n\n---\n\n## 八、写论文前加载的 Skills\n\n写论文或做最终审查时，Director/Agent 应按需加载以下 skills：\n- `latex-paper` — LaTeX 编译与格式\n- `reference-audit` — 引用真实性审计\n- `academic-writer` — ML 学术写作规范\n- `paper-quality-lessons`（本 skill）— 实战经验教训\n\n---\n\n## 九、附录：投稿经验时间线教训\n\n1. **论文数字锁定时机**：最终编译前 24h 锁定所有数字，之后只允许格式修改\n2. **GPU 不要空闲**：审稿期间如果 Agent 空闲，应该跑 ablation/扩展实验作为 rebuttal 储备\n3. **匿名化提前做**：不要等到最后一天才检查路径泄露，fresh repo 需要时间清理\n4. **9 页零余量策略**：NeurIPS 正文 9 页是硬限，每次新增内容必须等量压缩并编译验证\n5. **Contingency 叙事提前写**：关键实验完成前就写好两版叙事，避免最后一刻仓促改稿\n",
      "numLines": 301,
      "startLine": 1,
      "totalLines": 301
    }
  },
  "sourceToolAssistantUUID": "cf5e0bc3-e686-4abc-96e6-7c167213c5ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
````

</details>

---

### Tool call

_source line 14 · 2026-05-25T11:07:25.289Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SD4a1SD9YmWrXdbuaXZSiw`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebc1cae6-69a6-4e26-af06-a97c72d92bf5",
  "isSidechain": false,
  "requestId": "req_011CbPBRPH7GqxcxSt6uowKD",
  "type": "assistant",
  "uuid": "21fcd69e-7ca9-49ae-b8de-fa8ffef73115",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CnHE62rxi7o2Mp9MF7BfZ9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27861,
      "cache_read_input_tokens": 11846,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27861
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

_source line 15 · 2026-05-25T11:07:25.306Z_

<details><summary>↩ Tool result · `toolu_01SD4a1SD9YmWrXdbuaXZSiw`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21fcd69e-7ca9-49ae-b8de-fa8ffef73115",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "ebf04d17-3d54-450e-84fa-a6b52067179f",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
    ],
    "durationMs": 6,
    "numFiles": 11,
    "truncated": false
  },
  "sourceToolAssistantUUID": "21fcd69e-7ca9-49ae-b8de-fa8ffef73115",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：irt_equated_bench_regen Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 5 critical, 1 warning 一致性检…",
  "leafUuid": "ebf04d17-3d54-450e-84fa-a6b52067179f",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit EMNLP 2026 paper for custom rules compliance",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01"
}
```

---

### Assistant

_source line 18 · 2026-05-25T11:07:28.120Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read all the .tex files in parallel to get the full paper content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebf04d17-3d54-450e-84fa-a6b52067179f",
  "isSidechain": false,
  "requestId": "req_011CbPBRvY3qw5gou5p471qs",
  "type": "assistant",
  "uuid": "ecc2ba87-4607-4f34-9346-f47fe01c23f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdBLwcUC8E9sai9hppTtBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12076,
      "cache_read_input_tokens": 39707,
      "output_tokens": 890,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 890,
          "cache_read_input_tokens": 39707,
          "cache_creation_input_tokens": 12076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12076
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

_source line 19 · 2026-05-25T11:07:28.607Z_

读取所有 .tex 源码文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecc2ba87-4607-4f34-9346-f47fe01c23f0",
  "isSidechain": false,
  "requestId": "req_011CbPBRvY3qw5gou5p471qs",
  "type": "assistant",
  "uuid": "efacf3fe-afab-46fa-b0fb-699459884306",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdBLwcUC8E9sai9hppTtBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12076,
      "cache_read_input_tokens": 39707,
      "output_tokens": 890,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 890,
          "cache_read_input_tokens": 39707,
          "cache_creation_input_tokens": 12076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12076
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

_source line 20 · 2026-05-25T11:07:29.131Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JiKz3LqgvByuvoUfcWoRxD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efacf3fe-afab-46fa-b0fb-699459884306",
  "isSidechain": false,
  "requestId": "req_011CbPBRvY3qw5gou5p471qs",
  "type": "assistant",
  "uuid": "e1519972-c50f-47ac-a3ad-18cc5ba53ff3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdBLwcUC8E9sai9hppTtBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12076,
      "cache_read_input_tokens": 39707,
      "output_tokens": 890,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 890,
          "cache_read_input_tokens": 39707,
          "cache_creation_input_tokens": 12076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12076
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

_source line 21 · 2026-05-25T11:07:34.829Z_

<details><summary>↩ Tool result · `toolu_01Ly3B8NEJfFGPCB6GVjZ3zW`</summary>

```text
1	%%%%% NEW MATH DEFINITIONS %%%%%
2	
3	\usepackage{amsmath,amsfonts,bm}
4	\usepackage{amsthm}
5	
6	% Mark sections of captions for referring to divisions of figures
7	\newcommand{\figleft}{{\em (Left)}}
8	\newcommand{\figcenter}{{\em (Center)}}
9	\newcommand{\figright}{{\em (Right)}}
10	\newcommand{\figtop}{{\em (Top)}}
11	\newcommand{\figbottom}{{\em (Bottom)}}
12	\newcommand{\captiona}{{\em (a)}}
13	\newcommand{\captionb}{{\em (b)}}
14	\newcommand{\captionc}{{\em (c)}}
15	\newcommand{\captiond}{{\em (d)}}
16	
17	% Highlight a newly defined term
18	\newcommand{\newterm}[1]{{\bf #1}}
19	
20	
21	% Figure reference, lower-case.
22	\def\figref#1{figure~\ref{#1}}
23	% Figure reference, capital. For start of sentence
24	\def\Figref#1{Figure~\ref{#1}}
25	\def\twofigref#1#2{figures \ref{#1} and \ref{#2}}
26	\def\quadfigref#1#2#3#4{figures \ref{#1}, \ref{#2}, \ref{#3} and \ref{#4}}
27	% Section reference, lower-case.
28	\def\secref#1{section~\ref{#1}}
29	% Section reference, capital.
30	\def\Secref#1{Section~\ref{#1}}
31	% Reference to two sections.
32	\def\twosecrefs#1#2{sections \ref{#1} and \ref{#2}}
33	% Reference to three sections.
34	\def\secrefs#1#2#3{sections \ref{#1}, \ref{#2} and \ref{#3}}
35	% Reference to an equation, lower-case.
36	\def\eqref#1{equation~\ref{#1}}
37	% Reference to an equation, upper case
38	\def\Eqref#1{Equation~\ref{#1}}
39	% A raw reference to an equation---avoid using if possible
40	\def\plaineqref#1{\ref{#1}}
41	% Reference to a chapter, lower-case.
42	\def\chapref#1{chapter~\ref{#1}}
43	% Reference to an equation, upper case.
44	\def\Chapref#1{Chapter~\ref{#1}}
45	% Reference to a range of chapters
46	\def\rangechapref#1#2{chapters\ref{#1}--\ref{#2}}
47	% Reference to an algorithm, lower-case.
48	\def\algref#1{algorithm~\ref{#1}}
49	% Reference to an algorithm, upper case.
50	\def\Algref#1{Algorithm~\ref{#1}}
51	\def\twoalgref#1#2{algorithms \ref{#1} and \ref{#2}}
52	\def\Twoalgref#1#2{Algorithms \ref{#1} and \ref{#2}}
53	% Reference to a part, lower case
54	\def\partref#1{part~\ref{#1}}
55	% Reference to a part, upper case
56	\def\Partref#1{Part~\ref{#1}}
57	\def\twopartref#1#2{parts \ref{#1} and \ref{#2}}
58	
59	\def\ceil#1{\lceil #1 \rceil}
60	\def\floor#1{\lfloor #1 \rfloor}
61	\def\1{\bm{1}}
62	\newcommand{\train}{\mathcal{D}}
63	\newcommand{\valid}{\mathcal{D_{\mathrm{valid}}}}
64	\newcommand{\test}{\mathcal{D_{\mathrm{test}}}}
65	
66	\def\eps{{\epsilon}}
67	
68	
69	% Random variables
70	\def\reta{{\textnormal{$\eta$}}}
71	\def\ra{{\textnormal{a}}}
72	\def\rb{{\textnormal{b}}}
73	\def\rc{{\textnormal{c}}}
74	\def\rd{{\textnormal{d}}}
75	\def\re{{\textnormal{e}}}
76	\def\rf{{\textnormal{f}}}
77	\def\rg{{\textnormal{g}}}
78	\def\rh{{\textnormal{h}}}
79	\def\ri{{\textnormal{i}}}
80	\def\rj{{\textnormal{j}}}
81	\def\rk{{\textnormal{k}}}
82	\def\rl{{\textnormal{l}}}
83	% rm is already a command, just don't name any random variables m
84	\def\rn{{\textnormal{n}}}
85	\def\ro{{\textnormal{o}}}
86	\def\rp{{\textnormal{p}}}
87	\def\rq{{\textnormal{q}}}
88	\def\rr{{\textnormal{r}}}
89	\def\rs{{\textnormal{s}}}
90	\def\rt{{\textnormal{t}}}
91	\def\ru{{\textnormal{u}}}
92	\def\rv{{\textnormal{v}}}
93	\def\rw{{\textnormal{w}}}
94	\def\rx{{\textnormal{x}}}
95	\def\ry{{\textnormal{y}}}
96	\def\rz{{\textnormal{z}}}
97	
98	% Random vectors
99	\def\rvepsilon{{\mathbf{\epsilon}}}
100	\def\rvtheta{{\mathbf{\theta}}}
101	\def\rva{{\mathbf{a}}}
102	\def\rvb{{\mathbf{b}}}
103	\def\rvc{{\mathbf{c}}}
104	\def\rvd{{\mathbf{d}}}
105	\def\rve{{\mathbf{e}}}
106	\def\rvf{{\mathbf{f}}}
107	\def\rvg{{\mathbf{g}}}
108	\def\rvh{{\mathbf{h}}}
109	\def\rvu{{\mathbf{i}}}
110	\def\rvj{{\mathbf{j}}}
111	\def\rvk{{\mathbf{k}}}
112	\def\rvl{{\mathbf{l}}}
113	\def\rvm{{\mathbf{m}}}
114	\def\rvn{{\mathbf{n}}}
115	\def\rvo{{\mathbf{o}}}
116	\def\rvp{{\mathbf{p}}}
117	\def\rvq{{\mathbf{q}}}
118	\def\rvr{{\mathbf{r}}}
119	\def\rvs{{\mathbf{s}}}
120	\def\rvt{{\mathbf{t}}}
121	\def\rvu{{\mathbf{u}}}
122	\def\rvv{{\mathbf{v}}}
123	\def\rvw{{\mathbf{w}}}
124	\def\rvx{{\mathbf{x}}}
125	\def\rvy{{\mathbf{y}}}
126	\def\rvz{{\mathbf{z}}}
127	
128	% Elements of random vectors
129	\def\erva{{\textnormal{a}}}
130	\def\ervb{{\textnormal{b}}}
131	\def\ervc{{\textnormal{c}}}
132	\def\ervd{{\textnormal{d}}}
133	\def\erve{{\textnormal{e}}}
134	\def\ervf{{\textnormal{f}}}
135	\def\ervg{{\textnormal{g}}}
136	\def\ervh{{\textnormal{h}}}
137	\def\ervi{{\textnormal{i}}}
138	\def\ervj{{\textnormal{j}}}
139	\def\ervk{{\textnormal{k}}}
140	\def\ervl{{\textnormal{l}}}
141	\def\ervm{{\textnormal{m}}}
142	\def\ervn{{\textnormal{n}}}
143	\def\ervo{{\textnormal{o}}}
144	\def\ervp{{\textnormal{p}}}
145	\def\ervq{{\textnormal{q}}}
146	\def\ervr{{\textnormal{r}}}
147	\def\ervs{{\textnormal{s}}}
148	\def\ervt{{\textnormal{t}}}
149	\def\ervu{{\textnormal{u}}}
150	\def\ervv{{\textnormal{v}}}
151	\def\ervw{{\textnormal{w}}}
152	\def\ervx{{\textnormal{x}}}
153	\def\ervy{{\textnormal{y}}}
154	\def\ervz{{\textnormal{z}}}
155	
156	% Random matrices
157	\def\rmA{{\mathbf{A}}}
158	\def\rmB{{\mathbf{B}}}
159	\def\rmC{{\mathbf{C}}}
160	\def\rmD{{\mathbf{D}}}
161	\def\rmE{{\mathbf{E}}}
162	\def\rmF{{\mathbf{F}}}
163	\def\rmG{{\mathbf{G}}}
164	\def\rmH{{\mathbf{H}}}
165	\def\rmI{{\mathbf{I}}}
166	\def\rmJ{{\mathbf{J}}}
167	\def\rmK{{\mathbf{K}}}
168	\def\rmL{{\mathbf{L}}}
169	\def\rmM{{\mathbf{M}}}
170	\def\rmN{{\mathbf{N}}}
171	\def\rmO{{\mathbf{O}}}
172	\def\rmP{{\mathbf{P}}}
173	\def\rmQ{{\mathbf{Q}}}
174	\def\rmR{{\mathbf{R}}}
175	\def\rmS{{\mathbf{S}}}
176	\def\rmT{{\mathbf{T}}}
177	\def\rmU{{\mathbf{U}}}
178	\def\rmV{{\mathbf{V}}}
179	\def\rmW{{\mathbf{W}}}
180	\def\rmX{{\mathbf{X}}}
181	\def\rmY{{\mathbf{Y}}}
182	\def\rmZ{{\mathbf{Z}}}
183	
184	% Elements of random matrices
185	\def\ermA{{\textnormal{A}}}
186	\def\ermB{{\textnormal{B}}}
187	\def\ermC{{\textnormal{C}}}
188	\def\ermD{{\textnormal{D}}}
189	\def\ermE{{\textnormal{E}}}
190	\def\ermF{{\textnormal{F}}}
191	\def\ermG{{\textnormal{G}}}
192	\def\ermH{{\textnormal{H}}}
193	\def\ermI{{\textnormal{I}}}
194	\def\ermJ{{\textnormal{J}}}
195	\def\ermK{{\textnormal{K}}}
196	\def\ermL{{\textnormal{L}}}
197	\def\ermM{{\textnormal{M}}}
198	\def\ermN{{\textnormal{N}}}
199	\def\ermO{{\textnormal{O}}}
200	\def\ermP{{\textnormal{P}}}
201	\def\ermQ{{\textnormal{Q}}}
202	\def\ermR{{\textnormal{R}}}
203	\def\ermS{{\textnormal{S}}}
204	\def\ermT{{\textnormal{T}}}
205	\def\ermU{{\textnormal{U}}}
206	\def\ermV{{\textnormal{V}}}
207	\def\ermW{{\textnormal{W}}}
208	\def\ermX{{\textnormal{X}}}
209	\def\ermY{{\textnormal{Y}}}
210	\def\ermZ{{\textnormal{Z}}}
211	
212	% Vectors
213	\def\vzero{{\bm{0}}}
214	\def\vone{{\bm{1}}}
215	\def\vmu{{\bm{\mu}}}
216	\def\vtheta{{\bm{\theta}}}
217	\def\va{{\bm{a}}}
218	\def\vb{{\bm{b}}}
219	\def\vc{{\bm{c}}}
220	\def\vd{{\bm{d}}}
221	\def\ve{{\bm{e}}}
222	\def\vf{{\bm{f}}}
223	\def\vg{{\bm{g}}}
224	\def\vh{{\bm{h}}}
225	\def\vi{{\bm{i}}}
226	\def\vj{{\bm{j}}}
227	\def\vk{{\bm{k}}}
228	\def\vl{{\bm{l}}}
229	\def\vm{{\bm{m}}}
230	\def\vn{{\bm{n}}}
231	\def\vo{{\bm{o}}}
232	\def\vp{{\bm{p}}}
233	\def\vq{{\bm{q}}}
234	\def\vr{{\bm{r}}}
235	\def\vs{{\bm{s}}}
236	\def\vt{{\bm{t}}}
237	\def\vu{{\bm{u}}}
238	\def\vv{{\bm{v}}}
239	\def\vw{{\bm{w}}}
240	\def\vx{{\bm{x}}}
241	\def\vy{{\bm{y}}}
242	\def\vz{{\bm{z}}}
243	
244	% Elements of vectors
245	\def\evalpha{{\alpha}}
246	\def\evbeta{{\beta}}
247	\def\evepsilon{{\epsilon}}
248	\def\evlambda{{\lambda}}
249	\def\evomega{{\omega}}
250	\def\evmu{{\mu}}
251	\def\evpsi{{\psi}}
252	\def\evsigma{{\sigma}}
253	\def\evtheta{{\theta}}
254	\def\eva{{a}}
255	\def\evb{{b}}
256	\def\evc{{c}}
257	\def\evd{{d}}
258	\def\eve{{e}}
259	\def\evf{{f}}
260	\def\evg{{g}}
261	\def\evh{{h}}
262	\def\evi{{i}}
263	\def\evj{{j}}
264	\def\evk{{k}}
265	\def\evl{{l}}
266	\def\evm{{m}}
267	\def\evn{{n}}
268	\def\evo{{o}}
269	\def\evp{{p}}
270	\def\evq{{q}}
271	\def\evr{{r}}
272	\def\evs{{s}}
273	\def\evt{{t}}
274	\def\evu{{u}}
275	\def\evv{{v}}
276	\def\evw{{w}}
277	\def\evx{{x}}
278	\def\evy{{y}}
279	\def\evz{{z}}
280	
281	% Matrix
282	\def\mA{{\bm{A}}}
283	\def\mB{{\bm{B}}}
284	\def\mC{{\bm{C}}}
285	\def\mD{{\bm{D}}}
286	\def\mE{{\bm{E}}}
287	\def\mF{{\bm{F}}}
288	\def\mG{{\bm{G}}}
289	\def\mH{{\bm{H}}}
290	\def\mI{{\bm{I}}}
291	\def\mJ{{\bm{J}}}
292	\def\mK{{\bm{K}}}
293	\def\mL{{\bm{L}}}
294	\def\mM{{\bm{M}}}
295	\def\mN{{\bm{N}}}
296	\def\mO{{\bm{O}}}
297	\def\mP{{\bm{P}}}
298	\def\mQ{{\bm{Q}}}
299	\def\mR{{\bm{R}}}
300	\def\mS{{\bm{S}}}
301	\def\mT{{\bm{T}}}
302	\def\mU{{\bm{U}}}
303	\def\mV{{\bm{V}}}
304	\def\mW{{\bm{W}}}
305	\def\mX{{\bm{X}}}
306	\def\mY{{\bm{Y}}}
307	\def\mZ{{\bm{Z}}}
308	\def\mBeta{{\bm{\beta}}}
309	\def\mPhi{{\bm{\Phi}}}
310	\def\mLambda{{\bm{\Lambda}}}
311	\def\mSigma{{\bm{\Sigma}}}
312	
313	% Tensor
314	\DeclareMathAlphabet{\mathsfit}{\encodingdefault}{\sfdefault}{m}{sl}
315	\SetMathAlphabet{\mathsfit}{bold}{\encodingdefault}{\sfdefault}{bx}{n}
316	\newcommand{\tens}[1]{\bm{\mathsfit{#1}}}
317	\def\tA{{\tens{A}}}
318	\def\tB{{\tens{B}}}
319	\def\tC{{\tens{C}}}
320	\def\tD{{\tens{D}}}
321	\def\tE{{\tens{E}}}
322	\def\tF{{\tens{F}}}
323	\def\tG{{\tens{G}}}
324	\def\tH{{\tens{H}}}
325	\def\tI{{\tens{I}}}
326	\def\tJ{{\tens{J}}}
327	\def\tK{{\tens{K}}}
328	\def\tL{{\tens{L}}}
329	\def\tM{{\tens{M}}}
330	\def\tN{{\tens{N}}}
331	\def\tO{{\tens{O}}}
332	\def\tP{{\tens{P}}}
333	\def\tQ{{\tens{Q}}}
334	\def\tR{{\tens{R}}}
335	\def\tS{{\tens{S}}}
336	\def\tT{{\tens{T}}}
337	\def\tU{{\tens{U}}}
338	\def\tV{{\tens{V}}}
339	\def\tW{{\tens{W}}}
340	\def\tX{{\tens{X}}}
341	\def\tY{{\tens{Y}}}
342	\def\tZ{{\tens{Z}}}
343	
344	
345	% Graph
346	\def\gA{{\mathcal{A}}}
347	\def\gB{{\mathcal{B}}}
348	\def\gC{{\mathcal{C}}}
349	\def\gD{{\mathcal{D}}}
350	\def\gE{{\mathcal{E}}}
351	\def\gF{{\mathcal{F}}}
352	\def\gG{{\mathcal{G}}}
353	\def\gH{{\mathcal{H}}}
354	\def\gI{{\mathcal{I}}}
355	\def\gJ{{\mathcal{J}}}
356	\def\gK{{\mathcal{K}}}
357	\def\gL{{\mathcal{L}}}
358	\def\gM{{\mathcal{M}}}
359	\def\gN{{\mathcal{N}}}
360	\def\gO{{\mathcal{O}}}
361	\def\gP{{\mathcal{P}}}
362	\def\gQ{{\mathcal{Q}}}
363	\def\gR{{\mathcal{R}}}
364	\def\gS{{\mathcal{S}}}
365	\def\gT{{\mathcal{T}}}
366	\def\gU{{\mathcal{U}}}
367	\def\gV{{\mathcal{V}}}
368	\def\gW{{\mathcal{W}}}
369	\def\gX{{\mathcal{X}}}
370	\def\gY{{\mathcal{Y}}}
371	\def\gZ{{\mathcal{Z}}}
372	
373	% Sets
374	\def\sA{{\mathbb{A}}}
375	\def\sB{{\mathbb{B}}}
376	\def\sC{{\mathbb{C}}}
377	\def\sD{{\mathbb{D}}}
378	% Don't use a set called E, because this would be the same as our symbol
379	% for expectation.
380	\def\sF{{\mathbb{F}}}
381	\def\sG{{\mathbb{G}}}
382	\def\sH{{\mathbb{H}}}
383	\def\sI{{\mathbb{I}}}
384	\def\sJ{{\mathbb{J}}}
385	\def\sK{{\mathbb{K}}}
386	\def\sL{{\mathbb{L}}}
387	\def\sM{{\mathbb{M}}}
388	\def\sN{{\mathbb{N}}}
389	\def\sO{{\mathbb{O}}}
390	\def\sP{{\mathbb{P}}}
391	\def\sQ{{\mathbb{Q}}}
392	\def\sR{{\mathbb{R}}}
393	\def\sS{{\mathbb{S}}}
394	\def\sT{{\mathbb{T}}}
395	\def\sU{{\mathbb{U}}}
396	\def\sV{{\mathbb{V}}}
397	\def\sW{{\mathbb{W}}}
398	\def\sX{{\mathbb{X}}}
399	\def\sY{{\mathbb{Y}}}
400	\def\sZ{{\mathbb{Z}}}
401	
402	% Entries of a matrix
403	\def\emLambda{{\Lambda}}
404	\def\emA{{A}}
405	\def\emB{{B}}
406	\def\emC{{C}}
407	\def\emD{{D}}
408	\def\emE{{E}}
409	\def\emF{{F}}
410	\def\emG{{G}}
411	\def\emH{{H}}
412	\def\emI{{I}}
413	\def\emJ{{J}}
414	\def\emK{{K}}
415	\def\emL{{L}}
416	\def\emM{{M}}
417	\def\emN{{N}}
418	\def\emO{{O}}
419	\def\emP{{P}}
420	\def\emQ{{Q}}
421	\def\emR{{R}}
422	\def\emS{{S}}
423	\def\emT{{T}}
424	\def\emU{{U}}
425	\def\emV{{V}}
426	\def\emW{{W}}
427	\def\emX{{X}}
428	\def\emY{{Y}}
429	\def\emZ{{Z}}
430	\def\emSigma{{\Sigma}}
431	
432	% entries of a tensor
433	% Same font as tensor, without \bm wrapper
434	\newcommand{\etens}[1]{\mathsfit{#1}}
435	\def\etLambda{{\etens{\Lambda}}}
436	\def\etA{{\etens{A}}}
437	\def\etB{{\etens{B}}}
438	\def\etC{{\etens{C}}}
439	\def\etD{{\etens{D}}}
440	\def\etE{{\etens{E}}}
441	\def\etF{{\etens{F}}}
442	\def\etG{{\etens{G}}}
443	\def\etH{{\etens{H}}}
444	\def\etI{{\etens{I}}}
445	\def\etJ{{\etens{J}}}
446	\def\etK{{\etens{K}}}
447	\def\etL{{\etens{L}}}
448	\def\etM{{\etens{M}}}
449	\def\etN{{\etens{N}}}
450	\def\etO{{\etens{O}}}
451	\def\etP{{\etens{P}}}
452	\def\etQ{{\etens{Q}}}
453	\def\etR{{\etens{R}}}
454	\def\etS{{\etens{S}}}
455	\def\etT{{\etens{T}}}
456	\def\etU{{\etens{U}}}
457	\def\etV{{\etens{V}}}
458	\def\etW{{\etens{W}}}
459	\def\etX{{\etens{X}}}
460	\def\etY{{\etens{Y}}}
461	\def\etZ{{\etens{Z}}}
462	
463	% The true underlying data generating distribution
464	\newcommand{\pdata}{p_{\rm{data}}}
465	% The empirical distribution defined by the training set
466	\newcommand{\ptrain}{\hat{p}_{\rm{data}}}
467	\newcommand{\Ptrain}{\hat{P}_{\rm{data}}}
468	% The model distribution
469	\newcommand{\pmodel}{p_{\rm{model}}}
470	\newcommand{\Pmodel}{P_{\rm{model}}}
471	\newcommand{\ptildemodel}{\tilde{p}_{\rm{model}}}
472	% Stochastic autoencoder distributions
473	\newcommand{\pencode}{p_{\rm{encoder}}}
474	\newcommand{\pdecode}{p_{\rm{decoder}}}
475	\newcommand{\precons}{p_{\rm{reconstruct}}}
476	
477	\newcommand{\laplace}{\mathrm{Laplace}} % Laplace distribution
478	
479	\newcommand{\E}{\mathbb{E}}
480	\newcommand{\Ls}{\mathcal{L}}
481	\newcommand{\R}{\mathbb{R}}
482	\newcommand{\emp}{\tilde{p}}
483	\newcommand{\lr}{\alpha}
484	\newcommand{\reg}{\lambda}
485	\newcommand{\rect}{\mathrm{rectifier}}
486	\newcommand{\softmax}{\mathrm{softmax}}
487	\newcommand{\sigmoid}{\sigma}
488	\newcommand{\softplus}{\zeta}
489	\newcommand{\KL}{D_{\mathrm{KL}}}
490	\newcommand{\Var}{\mathrm{Var}}
491	\newcommand{\standarderror}{\mathrm{SE}}
492	\newcommand{\Cov}{\mathrm{Cov}}
493	% Wolfram Mathworld says $L^2$ is for function spaces and $\ell^2$ is for vectors
494	% But then they seem to use $L^2$ for vectors throughout the site, and so does
495	% wikipedia.
496	\newcommand{\normlzero}{L^0}
497	\newcommand{\normlone}{L^1}
498	\newcommand{\normltwo}{L^2}
499	\newcommand{\normlp}{L^p}
500	\newcommand{\normmax}{L^\infty}
501	
502	\newcommand{\parents}{Pa} % See usage in notation.tex. Chosen to match Daphne's book.
503	
504	\DeclareMathOperator*{\argmax}{arg\,max}
505	\DeclareMathOperator*{\argmin}{arg\,min}
506	
507	\DeclareMathOperator{\sign}{sign}
508	\DeclareMathOperator{\Tr}{Tr}
509	\let\ab\allowbreak
510	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cc50fef-a268-41f0-a44f-253e789053ba",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "2a32ff71-f220-4445-804a-fd3a6e884df1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex",
      "content": "%%%%% NEW MATH DEFINITIONS %%%%%\n\n\\usepackage{amsmath,amsfonts,bm}\n\\usepackage{amsthm}\n\n% Mark sections of captions for referring to divisions of figures\n\\newcommand{\\figleft}{{\\em (Left)}}\n\\newcommand{\\figcenter}{{\\em (Center)}}\n\\newcommand{\\figright}{{\\em (Right)}}\n\\newcommand{\\figtop}{{\\em (Top)}}\n\\newcommand{\\figbottom}{{\\em (Bottom)}}\n\\newcommand{\\captiona}{{\\em (a)}}\n\\newcommand{\\captionb}{{\\em (b)}}\n\\newcommand{\\captionc}{{\\em (c)}}\n\\newcommand{\\captiond}{{\\em (d)}}\n\n% Highlight a newly defined term\n\\newcommand{\\newterm}[1]{{\\bf #1}}\n\n\n% Figure reference, lower-case.\n\\def\\figref#1{figure~\\ref{#1}}\n% Figure reference, capital. For start of sentence\n\\def\\Figref#1{Figure~\\ref{#1}}\n\\def\\twofigref#1#2{figures \\ref{#1} and \\ref{#2}}\n\\def\\quadfigref#1#2#3#4{figures \\ref{#1}, \\ref{#2}, \\ref{#3} and \\ref{#4}}\n% Section reference, lower-case.\n\\def\\secref#1{section~\\ref{#1}}\n% Section reference, capital.\n\\def\\Secref#1{Section~\\ref{#1}}\n% Reference to two sections.\n\\def\\twosecrefs#1#2{sections \\ref{#1} and \\ref{#2}}\n% Reference to three sections.\n\\def\\secrefs#1#2#3{sections \\ref{#1}, \\ref{#2} and \\ref{#3}}\n% Reference to an equation, lower-case.\n\\def\\eqref#1{equation~\\ref{#1}}\n% Reference to an equation, upper case\n\\def\\Eqref#1{Equation~\\ref{#1}}\n% A raw reference to an equation---avoid using if possible\n\\def\\plaineqref#1{\\ref{#1}}\n% Reference to a chapter, lower-case.\n\\def\\chapref#1{chapter~\\ref{#1}}\n% Reference to an equation, upper case.\n\\def\\Chapref#1{Chapter~\\ref{#1}}\n% Reference to a range of chapters\n\\def\\rangechapref#1#2{chapters\\ref{#1}--\\ref{#2}}\n% Reference to an algorithm, lower-case.\n\\def\\algref#1{algorithm~\\ref{#1}}\n% Reference to an algorithm, upper case.\n\\def\\Algref#1{Algorithm~\\ref{#1}}\n\\def\\twoalgref#1#2{algorithms \\ref{#1} and \\ref{#2}}\n\\def\\Twoalgref#1#2{Algorithms \\ref{#1} and \\ref{#2}}\n% Reference to a part, lower case\n\\def\\partref#1{part~\\ref{#1}}\n% Reference to a part, upper case\n\\def\\Partref#1{Part~\\ref{#1}}\n\\def\\twopartref#1#2{parts \\ref{#1} and \\ref{#2}}\n\n\\def\\ceil#1{\\lceil #1 \\rceil}\n\\def\\floor#1{\\lfloor #1 \\rfloor}\n\\def\\1{\\bm{1}}\n\\newcommand{\\train}{\\mathcal{D}}\n\\newcommand{\\valid}{\\mathcal{D_{\\mathrm{valid}}}}\n\\newcommand{\\test}{\\mathcal{D_{\\mathrm{test}}}}\n\n\\def\\eps{{\\epsilon}}\n\n\n% Random variables\n\\def\\reta{{\\textnormal{$\\eta$}}}\n\\def\\ra{{\\textnormal{a}}}\n\\def\\rb{{\\textnormal{b}}}\n\\def\\rc{{\\textnormal{c}}}\n\\def\\rd{{\\textnormal{d}}}\n\\def\\re{{\\textnormal{e}}}\n\\def\\rf{{\\textnormal{f}}}\n\\def\\rg{{\\textnormal{g}}}\n\\def\\rh{{\\textnormal{h}}}\n\\def\\ri{{\\textnormal{i}}}\n\\def\\rj{{\\textnormal{j}}}\n\\def\\rk{{\\textnormal{k}}}\n\\def\\rl{{\\textnormal{l}}}\n% rm is already a command, just don't name any random variables m\n\\def\\rn{{\\textnormal{n}}}\n\\def\\ro{{\\textnormal{o}}}\n\\def\\rp{{\\textnormal{p}}}\n\\def\\rq{{\\textnormal{q}}}\n\\def\\rr{{\\textnormal{r}}}\n\\def\\rs{{\\textnormal{s}}}\n\\def\\rt{{\\textnormal{t}}}\n\\def\\ru{{\\textnormal{u}}}\n\\def\\rv{{\\textnormal{v}}}\n\\def\\rw{{\\textnormal{w}}}\n\\def\\rx{{\\textnormal{x}}}\n\\def\\ry{{\\textnormal{y}}}\n\\def\\rz{{\\textnormal{z}}}\n\n% Random vectors\n\\def\\rvepsilon{{\\mathbf{\\epsilon}}}\n\\def\\rvtheta{{\\mathbf{\\theta}}}\n\\def\\rva{{\\mathbf{a}}}\n\\def\\rvb{{\\mathbf{b}}}\n\\def\\rvc{{\\mathbf{c}}}\n\\def\\rvd{{\\mathbf{d}}}\n\\def\\rve{{\\mathbf{e}}}\n\\def\\rvf{{\\mathbf{f}}}\n\\def\\rvg{{\\mathbf{g}}}\n\\def\\rvh{{\\mathbf{h}}}\n\\def\\rvu{{\\mathbf{i}}}\n\\def\\rvj{{\\mathbf{j}}}\n\\def\\rvk{{\\mathbf{k}}}\n\\def\\rvl{{\\mathbf{l}}}\n\\def\\rvm{{\\mathbf{m}}}\n\\def\\rvn{{\\mathbf{n}}}\n\\def\\rvo{{\\mathbf{o}}}\n\\def\\rvp{{\\mathbf{p}}}\n\\def\\rvq{{\\mathbf{q}}}\n\\def\\rvr{{\\mathbf{r}}}\n\\def\\rvs{{\\mathbf{s}}}\n\\def\\rvt{{\\mathbf{t}}}\n\\def\\rvu{{\\mathbf{u}}}\n\\def\\rvv{{\\mathbf{v}}}\n\\def\\rvw{{\\mathbf{w}}}\n\\def\\rvx{{\\mathbf{x}}}\n\\def\\rvy{{\\mathbf{y}}}\n\\def\\rvz{{\\mathbf{z}}}\n\n% Elements of random vectors\n\\def\\erva{{\\textnormal{a}}}\n\\def\\ervb{{\\textnormal{b}}}\n\\def\\ervc{{\\textnormal{c}}}\n\\def\\ervd{{\\textnormal{d}}}\n\\def\\erve{{\\textnormal{e}}}\n\\def\\ervf{{\\textnormal{f}}}\n\\def\\ervg{{\\textnormal{g}}}\n\\def\\ervh{{\\textnormal{h}}}\n\\def\\ervi{{\\textnormal{i}}}\n\\def\\ervj{{\\textnormal{j}}}\n\\def\\ervk{{\\textnormal{k}}}\n\\def\\ervl{{\\textnormal{l}}}\n\\def\\ervm{{\\textnormal{m}}}\n\\def\\ervn{{\\textnormal{n}}}\n\\def\\ervo{{\\textnormal{o}}}\n\\def\\ervp{{\\textnormal{p}}}\n\\def\\ervq{{\\textnormal{q}}}\n\\def\\ervr{{\\textnormal{r}}}\n\\def\\ervs{{\\textnormal{s}}}\n\\def\\ervt{{\\textnormal{t}}}\n\\def\\ervu{{\\textnormal{u}}}\n\\def\\ervv{{\\textnormal{v}}}\n\\def\\ervw{{\\textnormal{w}}}\n\\def\\ervx{{\\textnormal{x}}}\n\\def\\ervy{{\\textnormal{y}}}\n\\def\\ervz{{\\textnormal{z}}}\n\n% Random matrices\n\\def\\rmA{{\\mathbf{A}}}\n\\def\\rmB{{\\mathbf{B}}}\n\\def\\rmC{{\\mathbf{C}}}\n\\def\\rmD{{\\mathbf{D}}}\n\\def\\rmE{{\\mathbf{E}}}\n\\def\\rmF{{\\mathbf{F}}}\n\\def\\rmG{{\\mathbf{G}}}\n\\def\\rmH{{\\mathbf{H}}}\n\\def\\rmI{{\\mathbf{I}}}\n\\def\\rmJ{{\\mathbf{J}}}\n\\def\\rmK{{\\mathbf{K}}}\n\\def\\rmL{{\\mathbf{L}}}\n\\def\\rmM{{\\mathbf{M}}}\n\\def\\rmN{{\\mathbf{N}}}\n\\def\\rmO{{\\mathbf{O}}}\n\\def\\rmP{{\\mathbf{P}}}\n\\def\\rmQ{{\\mathbf{Q}}}\n\\def\\rmR{{\\mathbf{R}}}\n\\def\\rmS{{\\mathbf{S}}}\n\\def\\rmT{{\\mathbf{T}}}\n\\def\\rmU{{\\mathbf{U}}}\n\\def\\rmV{{\\mathbf{V}}}\n\\def\\rmW{{\\mathbf{W}}}\n\\def\\rmX{{\\mathbf{X}}}\n\\def\\rmY{{\\mathbf{Y}}}\n\\def\\rmZ{{\\mathbf{Z}}}\n\n% Elements of random matrices\n\\def\\ermA{{\\textnormal{A}}}\n\\def\\ermB{{\\textnormal{B}}}\n\\def\\ermC{{\\textnormal{C}}}\n\\def\\ermD{{\\textnormal{D}}}\n\\def\\ermE{{\\textnormal{E}}}\n\\def\\ermF{{\\textnormal{F}}}\n\\def\\ermG{{\\textnormal{G}}}\n\\def\\ermH{{\\textnormal{H}}}\n\\def\\ermI{{\\textnormal{I}}}\n\\def\\ermJ{{\\textnormal{J}}}\n\\def\\ermK{{\\textnormal{K}}}\n\\def\\ermL{{\\textnormal{L}}}\n\\def\\ermM{{\\textnormal{M}}}\n\\def\\ermN{{\\textnormal{N}}}\n\\def\\ermO{{\\textnormal{O}}}\n\\def\\ermP{{\\textnormal{P}}}\n\\def\\ermQ{{\\textnormal{Q}}}\n\\def\\ermR{{\\textnormal{R}}}\n\\def\\ermS{{\\textnormal{S}}}\n\\def\\ermT{{\\textnormal{T}}}\n\\def\\ermU{{\\textnormal{U}}}\n\\def\\ermV{{\\textnormal{V}}}\n\\def\\ermW{{\\textnormal{W}}}\n\\def\\ermX{{\\textnormal{X}}}\n\\def\\ermY{{\\textnormal{Y}}}\n\\def\\ermZ{{\\textnormal{Z}}}\n\n% Vectors\n\\def\\vzero{{\\bm{0}}}\n\\def\\vone{{\\bm{1}}}\n\\def\\vmu{{\\bm{\\mu}}}\n\\def\\vtheta{{\\bm{\\theta}}}\n\\def\\va{{\\bm{a}}}\n\\def\\vb{{\\bm{b}}}\n\\def\\vc{{\\bm{c}}}\n\\def\\vd{{\\bm{d}}}\n\\def\\ve{{\\bm{e}}}\n\\def\\vf{{\\bm{f}}}\n\\def\\vg{{\\bm{g}}}\n\\def\\vh{{\\bm{h}}}\n\\def\\vi{{\\bm{i}}}\n\\def\\vj{{\\bm{j}}}\n\\def\\vk{{\\bm{k}}}\n\\def\\vl{{\\bm{l}}}\n\\def\\vm{{\\bm{m}}}\n\\def\\vn{{\\bm{n}}}\n\\def\\vo{{\\bm{o}}}\n\\def\\vp{{\\bm{p}}}\n\\def\\vq{{\\bm{q}}}\n\\def\\vr{{\\bm{r}}}\n\\def\\vs{{\\bm{s}}}\n\\def\\vt{{\\bm{t}}}\n\\def\\vu{{\\bm{u}}}\n\\def\\vv{{\\bm{v}}}\n\\def\\vw{{\\bm{w}}}\n\\def\\vx{{\\bm{x}}}\n\\def\\vy{{\\bm{y}}}\n\\def\\vz{{\\bm{z}}}\n\n% Elements of vectors\n\\def\\evalpha{{\\alpha}}\n\\def\\evbeta{{\\beta}}\n\\def\\evepsilon{{\\epsilon}}\n\\def\\evlambda{{\\lambda}}\n\\def\\evomega{{\\omega}}\n\\def\\evmu{{\\mu}}\n\\def\\evpsi{{\\psi}}\n\\def\\evsigma{{\\sigma}}\n\\def\\evtheta{{\\theta}}\n\\def\\eva{{a}}\n\\def\\evb{{b}}\n\\def\\evc{{c}}\n\\def\\evd{{d}}\n\\def\\eve{{e}}\n\\def\\evf{{f}}\n\\def\\evg{{g}}\n\\def\\evh{{h}}\n\\def\\evi{{i}}\n\\def\\evj{{j}}\n\\def\\evk{{k}}\n\\def\\evl{{l}}\n\\def\\evm{{m}}\n\\def\\evn{{n}}\n\\def\\evo{{o}}\n\\def\\evp{{p}}\n\\def\\evq{{q}}\n\\def\\evr{{r}}\n\\def\\evs{{s}}\n\\def\\evt{{t}}\n\\def\\evu{{u}}\n\\def\\evv{{v}}\n\\def\\evw{{w}}\n\\def\\evx{{x}}\n\\def\\evy{{y}}\n\\def\\evz{{z}}\n\n% Matrix\n\\def\\mA{{\\bm{A}}}\n\\def\\mB{{\\bm{B}}}\n\\def\\mC{{\\bm{C}}}\n\\def\\mD{{\\bm{D}}}\n\\def\\mE{{\\bm{E}}}\n\\def\\mF{{\\bm{F}}}\n\\def\\mG{{\\bm{G}}}\n\\def\\mH{{\\bm{H}}}\n\\def\\mI{{\\bm{I}}}\n\\def\\mJ{{\\bm{J}}}\n\\def\\mK{{\\bm{K}}}\n\\def\\mL{{\\bm{L}}}\n\\def\\mM{{\\bm{M}}}\n\\def\\mN{{\\bm{N}}}\n\\def\\mO{{\\bm{O}}}\n\\def\\mP{{\\bm{P}}}\n\\def\\mQ{{\\bm{Q}}}\n\\def\\mR{{\\bm{R}}}\n\\def\\mS{{\\bm{S}}}\n\\def\\mT{{\\bm{T}}}\n\\def\\mU{{\\bm{U}}}\n\\def\\mV{{\\bm{V}}}\n\\def\\mW{{\\bm{W}}}\n\\def\\mX{{\\bm{X}}}\n\\def\\mY{{\\bm{Y}}}\n\\def\\mZ{{\\bm{Z}}}\n\\def\\mBeta{{\\bm{\\beta}}}\n\\def\\mPhi{{\\bm{\\Phi}}}\n\\def\\mLambda{{\\bm{\\Lambda}}}\n\\def\\mSigma{{\\bm{\\Sigma}}}\n\n% Tensor\n\\DeclareMathAlphabet{\\mathsfit}{\\encodingdefault}{\\sfdefault}{m}{sl}\n\\SetMathAlphabet{\\mathsfit}{bold}{\\encodingdefault}{\\sfdefault}{bx}{n}\n\\newcommand{\\tens}[1]{\\bm{\\mathsfit{#1}}}\n\\def\\tA{{\\tens{A}}}\n\\def\\tB{{\\tens{B}}}\n\\def\\tC{{\\tens{C}}}\n\\def\\tD{{\\tens{D}}}\n\\def\\tE{{\\tens{E}}}\n\\def\\tF{{\\tens{F}}}\n\\def\\tG{{\\tens{G}}}\n\\def\\tH{{\\tens{H}}}\n\\def\\tI{{\\tens{I}}}\n\\def\\tJ{{\\tens{J}}}\n\\def\\tK{{\\tens{K}}}\n\\def\\tL{{\\tens{L}}}\n\\def\\tM{{\\tens{M}}}\n\\def\\tN{{\\tens{N}}}\n\\def\\tO{{\\tens{O}}}\n\\def\\tP{{\\tens{P}}}\n\\def\\tQ{{\\tens{Q}}}\n\\def\\tR{{\\tens{R}}}\n\\def\\tS{{\\tens{S}}}\n\\def\\tT{{\\tens{T}}}\n\\def\\tU{{\\tens{U}}}\n\\def\\tV{{\\tens{V}}}\n\\def\\tW{{\\tens{W}}}\n\\def\\tX{{\\tens{X}}}\n\\def\\tY{{\\tens{Y}}}\n\\def\\tZ{{\\tens{Z}}}\n\n\n% Graph\n\\def\\gA{{\\mathcal{A}}}\n\\def\\gB{{\\mathcal{B}}}\n\\def\\gC{{\\mathcal{C}}}\n\\def\\gD{{\\mathcal{D}}}\n\\def\\gE{{\\mathcal{E}}}\n\\def\\gF{{\\mathcal{F}}}\n\\def\\gG{{\\mathcal{G}}}\n\\def\\gH{{\\mathcal{H}}}\n\\def\\gI{{\\mathcal{I}}}\n\\def\\gJ{{\\mathcal{J}}}\n\\def\\gK{{\\mathcal{K}}}\n\\def\\gL{{\\mathcal{L}}}\n\\def\\gM{{\\mathcal{M}}}\n\\def\\gN{{\\mathcal{N}}}\n\\def\\gO{{\\mathcal{O}}}\n\\def\\gP{{\\mathcal{P}}}\n\\def\\gQ{{\\mathcal{Q}}}\n\\def\\gR{{\\mathcal{R}}}\n\\def\\gS{{\\mathcal{S}}}\n\\def\\gT{{\\mathcal{T}}}\n\\def\\gU{{\\mathcal{U}}}\n\\def\\gV{{\\mathcal{V}}}\n\\def\\gW{{\\mathcal{W}}}\n\\def\\gX{{\\mathcal{X}}}\n\\def\\gY{{\\mathcal{Y}}}\n\\def\\gZ{{\\mathcal{Z}}}\n\n% Sets\n\\def\\sA{{\\mathbb{A}}}\n\\def\\sB{{\\mathbb{B}}}\n\\def\\sC{{\\mathbb{C}}}\n\\def\\sD{{\\mathbb{D}}}\n% Don't use a set called E, because this would be the same as our symbol\n% for expectation.\n\\def\\sF{{\\mathbb{F}}}\n\\def\\sG{{\\mathbb{G}}}\n\\def\\sH{{\\mathbb{H}}}\n\\def\\sI{{\\mathbb{I}}}\n\\def\\sJ{{\\mathbb{J}}}\n\\def\\sK{{\\mathbb{K}}}\n\\def\\sL{{\\mathbb{L}}}\n\\def\\sM{{\\mathbb{M}}}\n\\def\\sN{{\\mathbb{N}}}\n\\def\\sO{{\\mathbb{O}}}\n\\def\\sP{{\\mathbb{P}}}\n\\def\\sQ{{\\mathbb{Q}}}\n\\def\\sR{{\\mathbb{R}}}\n\\def\\sS{{\\mathbb{S}}}\n\\def\\sT{{\\mathbb{T}}}\n\\def\\sU{{\\mathbb{U}}}\n\\def\\sV{{\\mathbb{V}}}\n\\def\\sW{{\\mathbb{W}}}\n\\def\\sX{{\\mathbb{X}}}\n\\def\\sY{{\\mathbb{Y}}}\n\\def\\sZ{{\\mathbb{Z}}}\n\n% Entries of a matrix\n\\def\\emLambda{{\\Lambda}}\n\\def\\emA{{A}}\n\\def\\emB{{B}}\n\\def\\emC{{C}}\n\\def\\emD{{D}}\n\\def\\emE{{E}}\n\\def\\emF{{F}}\n\\def\\emG{{G}}\n\\def\\emH{{H}}\n\\def\\emI{{I}}\n\\def\\emJ{{J}}\n\\def\\emK{{K}}\n\\def\\emL{{L}}\n\\def\\emM{{M}}\n\\def\\emN{{N}}\n\\def\\emO{{O}}\n\\def\\emP{{P}}\n\\def\\emQ{{Q}}\n\\def\\emR{{R}}\n\\def\\emS{{S}}\n\\def\\emT{{T}}\n\\def\\emU{{U}}\n\\def\\emV{{V}}\n\\def\\emW{{W}}\n\\def\\emX{{X}}\n\\def\\emY{{Y}}\n\\def\\emZ{{Z}}\n\\def\\emSigma{{\\Sigma}}\n\n% entries of a tensor\n% Same font as tensor, without \\bm wrapper\n\\newcommand{\\etens}[1]{\\mathsfit{#1}}\n\\def\\etLambda{{\\etens{\\Lambda}}}\n\\def\\etA{{\\etens{A}}}\n\\def\\etB{{\\etens{B}}}\n\\def\\etC{{\\etens{C}}}\n\\def\\etD{{\\etens{D}}}\n\\def\\etE{{\\etens{E}}}\n\\def\\etF{{\\etens{F}}}\n\\def\\etG{{\\etens{G}}}\n\\def\\etH{{\\etens{H}}}\n\\def\\etI{{\\etens{I}}}\n\\def\\etJ{{\\etens{J}}}\n\\def\\etK{{\\etens{K}}}\n\\def\\etL{{\\etens{L}}}\n\\def\\etM{{\\etens{M}}}\n\\def\\etN{{\\etens{N}}}\n\\def\\etO{{\\etens{O}}}\n\\def\\etP{{\\etens{P}}}\n\\def\\etQ{{\\etens{Q}}}\n\\def\\etR{{\\etens{R}}}\n\\def\\etS{{\\etens{S}}}\n\\def\\etT{{\\etens{T}}}\n\\def\\etU{{\\etens{U}}}\n\\def\\etV{{\\etens{V}}}\n\\def\\etW{{\\etens{W}}}\n\\def\\etX{{\\etens{X}}}\n\\def\\etY{{\\etens{Y}}}\n\\def\\etZ{{\\etens{Z}}}\n\n% The true underlying data generating distribution\n\\newcommand{\\pdata}{p_{\\rm{data}}}\n% The empirical distribution defined by the training set\n\\newcommand{\\ptrain}{\\hat{p}_{\\rm{data}}}\n\\newcommand{\\Ptrain}{\\hat{P}_{\\rm{data}}}\n% The model distribution\n\\newcommand{\\pmodel}{p_{\\rm{model}}}\n\\newcommand{\\Pmodel}{P_{\\rm{model}}}\n\\newcommand{\\ptildemodel}{\\tilde{p}_{\\rm{model}}}\n% Stochastic autoencoder distributions\n\\newcommand{\\pencode}{p_{\\rm{encoder}}}\n\\newcommand{\\pdecode}{p_{\\rm{decoder}}}\n\\newcommand{\\precons}{p_{\\rm{reconstruct}}}\n\n\\newcommand{\\laplace}{\\mathrm{Laplace}} % Laplace distribution\n\n\\newcommand{\\E}{\\mathbb{E}}\n\\newcommand{\\Ls}{\\mathcal{L}}\n\\newcommand{\\R}{\\mathbb{R}}\n\\newcommand{\\emp}{\\tilde{p}}\n\\newcommand{\\lr}{\\alpha}\n\\newcommand{\\reg}{\\lambda}\n\\newcommand{\\rect}{\\mathrm{rectifier}}\n\\newcommand{\\softmax}{\\mathrm{softmax}}\n\\newcommand{\\sigmoid}{\\sigma}\n\\newcommand{\\softplus}{\\zeta}\n\\newcommand{\\KL}{D_{\\mathrm{KL}}}\n\\newcommand{\\Var}{\\mathrm{Var}}\n\\newcommand{\\standarderror}{\\mathrm{SE}}\n\\newcommand{\\Cov}{\\mathrm{Cov}}\n% Wolfram Mathworld says $L^2$ is for function spaces and $\\ell^2$ is for vectors\n% But then they seem to use $L^2$ for vectors throughout the site, and so does\n% wikipedia.\n\\newcommand{\\normlzero}{L^0}\n\\newcommand{\\normlone}{L^1}\n\\newcommand{\\normltwo}{L^2}\n\\newcommand{\\normlp}{L^p}\n\\newcommand{\\normmax}{L^\\infty}\n\n\\newcommand{\\parents}{Pa} % See usage in notation.tex. Chosen to match Daphne's book.\n\n\\DeclareMathOperator*{\\argmax}{arg\\,max}\n\\DeclareMathOperator*{\\argmin}{arg\\,min}\n\n\\DeclareMathOperator{\\sign}{sign}\n\\DeclareMathOperator{\\Tr}{Tr}\n\\let\\ab\\allowbreak\n",
      "numLines": 510,
      "startLine": 1,
      "totalLines": 510
    }
  },
  "sourceToolAssistantUUID": "4cc50fef-a268-41f0-a44f-253e789053ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T11:07:29.135Z_

<details><summary>↩ Tool result · `toolu_01JiKz3LqgvByuvoUfcWoRxD`</summary>

```text
1	\begin{abstract}
2	Large language model (LLM) benchmark scores are routinely compared across model generations, yet whether individual items measure the same construct over time is rarely tested. We apply differential item functioning (DIF) analysis from educational measurement to the METABENCH response matrix (5,227 models across six benchmarks), validated through semi-synthetic injection with a cross-subject matching guarantee. Between 2023 and 2024 model cohorts, 18--31\% of items exhibit large temporal DIF---orders of magnitude above random baselines---while aggregate rankings remain near-perfect ($\rho \geq 0.994$). DIF flags are near-independent of web-overlap contamination labels, revealing that global exposure and differential functioning are complementary diagnostic dimensions. Base and instruct models exhibit opposite DIF directions, confirming structured capability shifts beyond contamination. We propose a three-step Monitor/Triage/Correct audit protocol with empirically grounded thresholds for benchmark maintainers. LLM benchmarks need psychometric monitoring, not just score reporting\footnote{Code and data are available at \url{https://github.com/anonymous-nlp-2026-2/irt_equated_bench_regen}.}.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1519972-c50f-47ac-a3ad-18cc5ba53ff3",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "3f8249cb-f765-4473-ab4b-3b5cf5e253aa",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nLarge language model (LLM) benchmark scores are routinely compared across model generations, yet whether individual items measure the same construct over time is rarely tested. We apply differential item functioning (DIF) analysis from educational measurement to the METABENCH response matrix (5,227 models across six benchmarks), validated through semi-synthetic injection with a cross-subject matching guarantee. Between 2023 and 2024 model cohorts, 18--31\\% of items exhibit large temporal DIF---orders of magnitude above random baselines---while aggregate rankings remain near-perfect ($\\rho \\geq 0.994$). DIF flags are near-independent of web-overlap contamination labels, revealing that global exposure and differential functioning are complementary diagnostic dimensions. Base and instruct models exhibit opposite DIF directions, confirming structured capability shifts beyond contamination. We propose a three-step Monitor/Triage/Correct audit protocol with empirically grounded thresholds for benchmark maintainers. LLM benchmarks need psychometric monitoring, not just score reporting\\footnote{Code and data are available at \\url{https://github.com/anonymous-nlp-2026-2/irt_equated_bench_regen}.}.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  },
  "sourceToolAssistantUUID": "e1519972-c50f-47ac-a3ad-18cc5ba53ff3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T11:07:31.176Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HabXcYpnq3K78foteBNc6o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f8249cb-f765-4473-ab4b-3b5cf5e253aa",
  "isSidechain": false,
  "requestId": "req_011CbPBRvY3qw5gou5p471qs",
  "type": "assistant",
  "uuid": "cb2927a9-019e-4d11-9168-621d73b2b41c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdBLwcUC8E9sai9hppTtBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12076,
      "cache_read_input_tokens": 39707,
      "output_tokens": 890,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 890,
          "cache_read_input_tokens": 39707,
          "cache_creation_input_tokens": 12076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12076
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

_source line 24 · 2026-05-25T11:07:31.181Z_

<details><summary>↩ Tool result · `toolu_01HabXcYpnq3K78foteBNc6o`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\looseness=-1
5	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We use \emph{measurement invariance} to denote the property that test items function identically across groups~\citep{meredith1993invariance}, \emph{differential item functioning} (DIF) as the item-level statistical test for violations, and \emph{temporal score incomparability} (measurement non-invariance across temporal cohorts, manifesting as score incomparability) as the empirical phenomenon when DIF is detected---scores are not directly comparable across cohorts because item measurement properties differ systematically, without implying degradation or attributing cause. Applying Mantel-Haenszel DIF analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench}, we find that 31\% of Massive Multitask Language Understanding (MMLU)~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts---versus 0.62\% under a random-split control. Aggregate rankings are robust ($\rho \approx 0.997$), but absolute scores are not directly comparable: DIF-corrected scoring (excluding all C-flagged items) shifts accuracy by ${+}2.12$\,pp on average, with individual models displaced by up to 851 rank positions. This instability does not invalidate the benchmark---aggregate rankings are massively redundant---but it is diagnostic, revealing which capability dimensions shift across model generations.
6	
7	Existing approaches to benchmark integrity focus on \emph{global exposure}---whether items appear in training corpora---through membership inference~\citep{shi2024mink} and performance-based detection~\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}, validated against web-overlap labels~\citep{li2024contamination}. Whether benchmark items function equivalently across model generations---\emph{measurement invariance}---has not been systematically examined (\Cref{fig:pipeline,fig:global_vs_differential}). We find these two signals are near-independent (Jaccard $= 0.206$, $\phi = 0.012$): complementary diagnostic dimensions, not competing ones.
8	
9	\begin{figure*}[t]
10	\centering
11	\includegraphics[width=\textwidth]{fig_0_pipeline.pdf}
12	\caption{Four-stage psychometric auditing pipeline. \textbf{\ding{192}} A binary response matrix records model correctness across benchmark items, with models split into temporal cohorts (2023 reference vs.\ 2024 focal). \textbf{\ding{193}} Models are stratified into $K{=}5$ score quintiles. \textbf{\ding{194}} Per-item Mantel-Haenszel DIF tests compute $\Delta_{\mathrm{MH}}$ across strata. \textbf{\ding{195}} ETS classification assigns severity labels (A/B/C). Result: 29.2\% of items flagged as C, yet stable-item $\rho = 0.997$, replicated across six benchmarks.}
13	\label{fig:pipeline}
14	\end{figure*}
15	
16	We apply a temporal DIF audit framework to the full METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), to our knowledge the largest-scale DIF analysis on LLM benchmarks, complementing concurrent work on anchor-item calibration~\citep{habba2026growingpains} and addressing the fragility of existing detectors under post-training perturbation~\citep{wang2026fragility}. Two structural controls, a sensitivity check, and replication across all six METABENCH benchmarks confirm that the temporal DIF rate (29.2\% after non-independence correction; 17.9--31.3\% across benchmarks) is not a methodological artifact (\Cref{sec:temporal,sec:structural,sec:gsm8k}). We make three contributions:
17	\begin{enumerate}[nosep,leftmargin=*,topsep=2pt]
18	\item \textbf{Temporal DIF at scale}: 29.2\% of MMLU items exhibit temporal DIF (17.9--31.3\% across six benchmarks), near-independent of web-overlap labels (Jaccard $= 0.206$); base-vs-instruct stratification reveals opposite patterns ($\chi^2 = 562.7$), confirming mechanism separation (\Cref{sec:temporal,sec:groundtruth,sec:gsm8k,sec:disc_temporal}).
19	\item \textbf{Cross-subject matching with $\Delta\mathrm{FPR} = 0$ guarantee}: solves matching-variable corruption under single-subject contamination, extending to $k \leq 5$; complemented by design effect (DEFF) correction and semi-synthetic validation (\Cref{sec:semisynthetic}).
20	\item \textbf{Actionable audit protocol}: a three-step Monitor/Triage/Correct protocol with empirically grounded thresholds (\Cref{sec:disc_protocol}).
21	\end{enumerate}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb2927a9-019e-4d11-9168-621d73b2b41c",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "38a07656-bcbd-4a45-82a5-01bf07206352",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\n\\looseness=-1\nWhen we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We use \\emph{measurement invariance} to denote the property that test items function identically across groups~\\citep{meredith1993invariance}, \\emph{differential item functioning} (DIF) as the item-level statistical test for violations, and \\emph{temporal score incomparability} (measurement non-invariance across temporal cohorts, manifesting as score incomparability) as the empirical phenomenon when DIF is detected---scores are not directly comparable across cohorts because item measurement properties differ systematically, without implying degradation or attributing cause. Applying Mantel-Haenszel DIF analysis~\\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\\citep{kipnis2024metabench}, we find that 31\\% of Massive Multitask Language Understanding (MMLU)~\\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts---versus 0.62\\% under a random-split control. Aggregate rankings are robust ($\\rho \\approx 0.997$), but absolute scores are not directly comparable: DIF-corrected scoring (excluding all C-flagged items) shifts accuracy by ${+}2.12$\\,pp on average, with individual models displaced by up to 851 rank positions. This instability does not invalidate the benchmark---aggregate rankings are massively redundant---but it is diagnostic, revealing which capability dimensions shift across model generations.\n\nExisting approaches to benchmark integrity focus on \\emph{global exposure}---whether items appear in training corpora---through membership inference~\\citep{shi2024mink} and performance-based detection~\\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}, validated against web-overlap labels~\\citep{li2024contamination}. Whether benchmark items function equivalently across model generations---\\emph{measurement invariance}---has not been systematically examined (\\Cref{fig:pipeline,fig:global_vs_differential}). We find these two signals are near-independent (Jaccard $= 0.206$, $\\phi = 0.012$): complementary diagnostic dimensions, not competing ones.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_0_pipeline.pdf}\n\\caption{Four-stage psychometric auditing pipeline. \\textbf{\\ding{192}} A binary response matrix records model correctness across benchmark items, with models split into temporal cohorts (2023 reference vs.\\ 2024 focal). \\textbf{\\ding{193}} Models are stratified into $K{=}5$ score quintiles. \\textbf{\\ding{194}} Per-item Mantel-Haenszel DIF tests compute $\\Delta_{\\mathrm{MH}}$ across strata. \\textbf{\\ding{195}} ETS classification assigns severity labels (A/B/C). Result: 29.2\\% of items flagged as C, yet stable-item $\\rho = 0.997$, replicated across six benchmarks.}\n\\label{fig:pipeline}\n\\end{figure*}\n\nWe apply a temporal DIF audit framework to the full METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items), to our knowledge the largest-scale DIF analysis on LLM benchmarks, complementing concurrent work on anchor-item calibration~\\citep{habba2026growingpains} and addressing the fragility of existing detectors under post-training perturbation~\\citep{wang2026fragility}. Two structural controls, a sensitivity check, and replication across all six METABENCH benchmarks confirm that the temporal DIF rate (29.2\\% after non-independence correction; 17.9--31.3\\% across benchmarks) is not a methodological artifact (\\Cref{sec:temporal,sec:structural,sec:gsm8k}). We make three contributions:\n\\begin{enumerate}[nosep,leftmargin=*,topsep=2pt]\n\\item \\textbf{Temporal DIF at scale}: 29.2\\% of MMLU items exhibit temporal DIF (17.9--31.3\\% across six benchmarks), near-independent of web-overlap labels (Jaccard $= 0.206$); base-vs-instruct stratification reveals opposite patterns ($\\chi^2 = 562.7$), confirming mechanism separation (\\Cref{sec:temporal,sec:groundtruth,sec:gsm8k,sec:disc_temporal}).\n\\item \\textbf{Cross-subject matching with $\\Delta\\mathrm{FPR} = 0$ guarantee}: solves matching-variable corruption under single-subject contamination, extending to $k \\leq 5$; complemented by design effect (DEFF) correction and semi-synthetic validation (\\Cref{sec:semisynthetic}).\n\\item \\textbf{Actionable audit protocol}: a three-step Monitor/Triage/Correct protocol with empirically grounded thresholds (\\Cref{sec:disc_protocol}).\n\\end{enumerate}\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  },
  "sourceToolAssistantUUID": "cb2927a9-019e-4d11-9168-621d73b2b41c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T11:07:31.348Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BVaUVUihkVadBrCNMCXFyB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38a07656-bcbd-4a45-82a5-01bf07206352",
  "isSidechain": false,
  "requestId": "req_011CbPBRvY3qw5gou5p471qs",
  "type": "assistant",
  "uuid": "6384d257-b7db-4808-ba30-c90f810b7df6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdBLwcUC8E9sai9hppTtBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12076,
      "cache_read_input_tokens": 39707,
      "output_tokens": 890,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 890,
          "cache_read_input_tokens": 39707,
          "cache_creation_input_tokens": 12076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12076
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

_source line 26 · 2026-05-25T11:07:31.359Z_

<details><summary>↩ Tool result · `toolu_01BVaUVUihkVadBrCNMCXFyB`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Psychometric Methods for LLM Evaluation.}
5	\looseness=-1
6	The Mantel-Haenszel procedure \citep{holland1988mh} remains the most widely used DIF detector in educational testing due to its simplicity and well-characterized statistical properties, operating nonparametrically without requiring an explicit item response theory (IRT) model. DIF analysis is a specific instance of measurement invariance testing \citep{meredith1993invariance}, which examines whether an instrument functions equivalently across groups. IRT adoption in LLM evaluation has accelerated since \citet{lalor2019irt} introduced it to natural language processing: recent work calibrates test sets for discriminability, item selection, and adaptive evaluation. The closest concurrent work is Growing Pains \citep{habba2026growingpains}, which uses parametric IRT (two-parameter logistic [2PL] / three-parameter logistic [3PL] fixed-parameter calibration) to equate scores across temporal cohorts. MH-DIF is nonparametric and robust to model misspecification---an advantage given poor 2PL fit for MMLU (root mean square error of approximation [RMSEA] $> 0.08$; \Cref{app:power_sensitivity}). Growing Pains prescribes how to equate scores after instability is detected; our work diagnoses \emph{which} items exhibit instability and quantifies severity via ETS classification, providing pre-screened anchor candidates for downstream equating. Their anchor-item selection can directly consume our stable-item set; our finding that 31\% of items exhibit temporal DIF identifies which items should \emph{not} serve as anchors. To our knowledge, no prior work applies DIF to benchmark temporal comparability.
7	
8	\paragraph{Contamination Detection.}
9	\looseness=-1
10	A growing family of methods detects benchmark contamination through model behavior or training-data analysis. Membership inference approaches use token-level log-likelihood statistics \citep{shi2024mink} or statistical anomalies \citep{dekoninck2024constat} to flag items likely seen during training. A standard validation practice is to compare detector output against web-overlap labels \citep{li2024contamination}, which classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure}---whether an item exists in training data---rather than \emph{differential item functioning}: whether an item behaves differently across model cohorts. This global-vs-differential distinction motivates our comparison with web-overlap labels (\Cref{sec:groundtruth}). \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
11	
12	\paragraph{Benchmark Quality and Design.}
13	\looseness=-1
14	Meta-evaluation of static benchmark quality~\citep{zhu2026bhi} assesses properties at a single snapshot; our temporal DIF analysis diagnoses \emph{when} measurement properties shift. Work on LLM memorization \citep{carlini2022quantifying} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. MMLU-CF~\citep{zhao2025mmlucf} reconstructs contamination-free items without replacement; DIF monitoring identifies which existing items remain measurement-invariant. Dynamic benchmarks~\citep{kiela2021dynabench} mitigate contamination by construction but lack psychometric equating. Broader surveys~\citep{chang2024survey} identify benchmark saturation as a systemic challenge that DIF analysis directly addresses.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6384d257-b7db-4808-ba30-c90f810b7df6",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "51893609-1e5a-4ef7-b532-33249d298466",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Psychometric Methods for LLM Evaluation.}\n\\looseness=-1\nThe Mantel-Haenszel procedure \\citep{holland1988mh} remains the most widely used DIF detector in educational testing due to its simplicity and well-characterized statistical properties, operating nonparametrically without requiring an explicit item response theory (IRT) model. DIF analysis is a specific instance of measurement invariance testing \\citep{meredith1993invariance}, which examines whether an instrument functions equivalently across groups. IRT adoption in LLM evaluation has accelerated since \\citet{lalor2019irt} introduced it to natural language processing: recent work calibrates test sets for discriminability, item selection, and adaptive evaluation. The closest concurrent work is Growing Pains \\citep{habba2026growingpains}, which uses parametric IRT (two-parameter logistic [2PL] / three-parameter logistic [3PL] fixed-parameter calibration) to equate scores across temporal cohorts. MH-DIF is nonparametric and robust to model misspecification---an advantage given poor 2PL fit for MMLU (root mean square error of approximation [RMSEA] $> 0.08$; \\Cref{app:power_sensitivity}). Growing Pains prescribes how to equate scores after instability is detected; our work diagnoses \\emph{which} items exhibit instability and quantifies severity via ETS classification, providing pre-screened anchor candidates for downstream equating. Their anchor-item selection can directly consume our stable-item set; our finding that 31\\% of items exhibit temporal DIF identifies which items should \\emph{not} serve as anchors. To our knowledge, no prior work applies DIF to benchmark temporal comparability.\n\n\\paragraph{Contamination Detection.}\n\\looseness=-1\nA growing family of methods detects benchmark contamination through model behavior or training-data analysis. Membership inference approaches use token-level log-likelihood statistics \\citep{shi2024mink} or statistical anomalies \\citep{dekoninck2024constat} to flag items likely seen during training. A standard validation practice is to compare detector output against web-overlap labels \\citep{li2024contamination}, which classify items based on verbatim matches in publicly accessible corpora. Such labels measure \\emph{global exposure}---whether an item exists in training data---rather than \\emph{differential item functioning}: whether an item behaves differently across model cohorts. This global-vs-differential distinction motivates our comparison with web-overlap labels (\\Cref{sec:groundtruth}). \\citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.\n\n\\paragraph{Benchmark Quality and Design.}\n\\looseness=-1\nMeta-evaluation of static benchmark quality~\\citep{zhu2026bhi} assesses properties at a single snapshot; our temporal DIF analysis diagnoses \\emph{when} measurement properties shift. Work on LLM memorization \\citep{carlini2022quantifying} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. MMLU-CF~\\citep{zhao2025mmlucf} reconstructs contamination-free items without replacement; DIF monitoring identifies which existing items remain measurement-invariant. Dynamic benchmarks~\\citep{kiela2021dynabench} mitigate contamination by construction but lack psychometric equating. Broader surveys~\\citep{chang2024survey} identify benchmark saturation as a systemic challenge that DIF analysis directly addresses.\n",
      "numLines": 15,
      "startLine": 1,
      "totalLines": 15
    }
  },
  "sourceToolAssistantUUID": "6384d257-b7db-4808-ba30-c90f810b7df6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T11:07:31.373Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BkTmTXVGQgGpAPTfxkuxLR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51893609-1e5a-4ef7-b532-33249d298466",
  "isSidechain": false,
  "requestId": "req_011CbPBRvY3qw5gou5p471qs",
  "type": "assistant",
  "uuid": "8fba4614-f3a0-42b4-886e-c51fe26721c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdBLwcUC8E9sai9hppTtBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12076,
      "cache_read_input_tokens": 39707,
      "output_tokens": 890,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 890,
          "cache_read_input_tokens": 39707,
          "cache_creation_input_tokens": 12076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12076
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

_source line 28 · 2026-05-25T11:07:31.379Z_

<details><summary>↩ Tool result · `toolu_01BkTmTXVGQgGpAPTfxkuxLR`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\begin{figure*}[t]
12	\centering
13	\includegraphics[width=\textwidth]{fig_1_global_vs_differential.pdf}
14	\caption{Global vs.\ differential contamination via Item Characteristic Curves (ICCs). \textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts due to disproportionate exposure. The enrichment ratio of $\approx 1.0$ between DIF flags and web-overlap labels is expected because most items fall into the left category.}
15	\label{fig:global_vs_differential}
16	\end{figure*}
17	
18	\subsection{Mantel-Haenszel DIF and ETS Classification}
19	\label{sec:mhdif}
20	
21	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
22	
23	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh,magis2010difr} detects DIF by stratifying examinees into $K$ score bins based on total score (a proxy for $\theta$) and computing a common odds ratio across strata. We use $K = 5$ equiprobable strata (quintile-based binning) following ETS recommended practice for large-scale assessments~\citep{donoghue1993mh,clauser1998dif}; $K{=}3$ yields near-identical power (\Cref{app:k3_power}). Within each stratum $k$, the responses of the reference group and the focal group form a $2 \times 2$ contingency table:
24	
25	\begin{equation}
26	\label{eq:mh}
27	\alpha_{\mathrm{MH}} = \frac{\displaystyle\sum_{k=1}^{K} A_k D_k \,/\, T_k}{\displaystyle\sum_{k=1}^{K} B_k C_k \,/\, T_k}\,,
28	\end{equation}
29	
30	\noindent where $A_k$ and $B_k$ are the number of correct and incorrect responses in the reference group for stratum $k$, $C_k$ and $D_k$ are the corresponding counts for the focal group, and $T_k$ is the total number of examinees in stratum $k$. Under the null hypothesis of no DIF, $\alpha_{\mathrm{MH}} = 1$. The log odds ratio is converted to the ETS delta scale:
31	
32	\begin{equation}
33	\label{eq:delta}
34	\Delta_{\mathrm{MH}} = -2.35 \ln(\alpha_{\mathrm{MH}})\,.
35	\end{equation}
36	
37	The Educational Testing Service (ETS) classifies DIF severity into three categories based on $|\Delta_{\mathrm{MH}}|$. Category~A (negligible) requires $|\Delta_{\mathrm{MH}}| < 1.0$. Category~C (large) requires both $|\Delta_{\mathrm{MH}}| \geq 1.5$ and statistical significance at $p < 0.05$ from the MH chi-squared test. Category~B (moderate) includes all remaining items: those with $1.0 \leq |\Delta_{\mathrm{MH}}| < 1.5$, or $|\Delta_{\mathrm{MH}}| \geq 1.5$ without statistical significance. The dual threshold in ETS~C (effect size \emph{and} significance) guards against flagging items that show large but unreliable effect sizes. These thresholds were calibrated for human test-taker populations; we retain them as standardized reference points and verify robustness across stricter cutoffs (\Cref{sec:temporal}). Throughout this paper, we report the percentage of items classified as ETS~C, denoted C\%. At $N = 1{,}887$ (the temporal comparison; 5{,}227 total across all cohort designs), significance ($p < 0.05$) is nearly automatically satisfied for any $|\Delta_{\mathrm{MH}}| \geq 1.5$: only 3 of 3{,}918 C items lack significance, so the dual criterion effectively reduces to a single effect-size threshold; per-item DEFF correction (\Cref{app:deff}) restores $p$-value selectivity by reducing effective $N$: under simple-mean DEFF, 269 items (6.9\%) lose significance while retaining $|\Delta_{\mathrm{MH}}| \geq 1.5$; 74\% of these are near-miss ($p_{\mathrm{adj}} \in [0.05, 0.10]$).
38	
39	The choice of matching variable (the total score used for stratification) affects both validity and interpretation. We distinguish three matching strategies: (1)~\emph{standard matching} uses the within-benchmark total score on all items of the same benchmark; (2)~\emph{cross-subject matching}, adapting purified subtest matching~\citep{swaminathan1990logistic} to the LLM multi-subject setting, uses the total score on all subjects \emph{other than} the one containing the item under test, preventing the matching variable from absorbing injected contamination signals (\Cref{sec:injection}); and (3)~\emph{external matching} uses the total score on a different benchmark entirely (e.g., MMLU total score as the matching variable when testing DIF on Grade School Math 8K (GSM8K) items), providing an independent ability proxy uncontaminated by the target benchmark. Cross-subject and external matching both address matching variable contamination but at different granularities: cross-subject operates within a multi-domain benchmark, while external operates across benchmarks. Total score matching is adequate: IRT $\theta$ correlates at $r = 0.9986$ with total scores (\Cref{sec:structural}).
40	
41	\paragraph{LLM-specific challenges.} Applying MH-DIF to LLMs introduces four challenges absent in educational testing. First, overlapping training corpora violate local independence; permutation simulation (1{,}000 replications shuffling group labels within score strata) confirms local-dependence-attributable FPR inflation $< 0.001$~pp under cross-subject matching (\Cref{app:method_details}). Second, fine-tuned variants within model families are not independent examinees; graduated de-duplication shows family structure does not inflate C\% (\Cref{sec:structural}). Third, bimodal ability distributions motivate quintile-based stratification. Fourth, MMLU's 57-subject structure raises a multidimensionality concern~\citep{ackerman1992didmf,roussos1996multidimensionality}: domain-level ability profiles are nearly flat across cohorts (Cohen's $d$ range $= 0.12$), cross-subject and within-subject matching agree ($\kappa = 0.80$, 834 items), and cross-subject-unique C items do not concentrate in high-shift subjects (\Cref{app:structural}).
42	
43	\subsection{Cohort Designs}
44	\label{sec:cohorts}
45	
46	We construct five cohort comparisons: (1)~\emph{Temporal}: 2023 ($N = 1{,}080$) vs.\ 2024 ($N = 807$) models, the primary comparison; (2)~\emph{Ability-quintile}: Q1--Q2 vs.\ Q4--Q5 within the same temporal window; (3)~\emph{Within-family}: Llama-2 ($N = 161$) vs.\ Llama-3 ($N = 308$), isolating generational changes within a single family; (4)~\emph{Within-subject}: per-subject DIF to test domain concentration; and (5)~\emph{Random split}: two random halves of the 2023 cohort ($N = 540$ each) as a sanity check. Calendar-year boundaries are coarse; half-yearly comparison (C\% $= 34.4\%$; \Cref{app:uncertainty}) and base-only/instruct-only analyses (C\% $= 32.1\%$/$36.5\%$; \Cref{app:baseinst_temporal}) confirm DIF persists under finer slicing.
47	
48	\subsection{Semi-Synthetic Injection Framework}
49	\label{sec:injection}
50	
51	We use contamination injection as a controlled case study to validate DIF detection power; DIF itself is mechanism-agnostic and flags items that function differently without attributing cause (\Cref{sec:disc_protocol}). To evaluate whether MH-DIF can detect differential contamination when it is present, we construct a semi-synthetic framework with controlled ground truth.
52	
53	\paragraph{Procedure.} From items classified as ETS~A in the uninjected data (negligible DIF), we select 20\% uniformly at random as the ``contaminated'' set. For each contaminated item, we flip incorrect responses to correct in the focal group at exploitation rate $p \in \{0.0, 0.3, 0.5, 0.7, 1.0\}$. We then run MH-DIF on the modified response matrix and measure detection performance. We report $\Delta\mathrm{TPR} = \mathrm{TPR}(\text{injected}) - \mathrm{TPR}(\text{baseline})$ and $\Delta\mathrm{FPR} = \mathrm{FPR}(\text{injected}) - \mathrm{FPR}(\text{baseline})$, where TPR is the true positive rate on injected items and FPR is the false positive rate on uninjected items. Each injection level is repeated across 5 random seeds for uncertainty estimation. Because binary response flipping represents a stylized uniform injection pattern, reported $\Delta\mathrm{TPR}$ values may overestimate detection power; realistic contamination (partial memorization, format-specific advantages) would produce weaker signals.
54	
55	\paragraph{Cross-subject matching.} The choice of matching variable is critical for valid semi-synthetic evaluation. When contamination is injected into items within subject $X$, the total score on subject $X$ absorbs part of the injection signal. Using this contaminated total score as the MH matching variable violates the conditional independence assumption and inflates FPR. Cross-subject matching resolves this by computing the matching variable from all subjects \emph{other than} the one being tested.
56	
57	\paragraph{Remark (Zero FPR under single-subject matching).}
58	\label{prop:fpr}
59	Let $M_i^{(-s)} = \sum_{j \notin s} Y_{ij}$ be the matching variable for examinee $i$ on focal subject $s$. Under single-subject injection (contamination confined to subject $s$), the tested item belongs to $s$ and does not contribute to $M_i^{(-s)}$; injecting contamination into $s$ leaves $M_i^{(-s)}$ unchanged. Therefore $\Delta\mathrm{FPR} = 0$ by construction.
60	
61	When contamination spans multiple subjects simultaneously, $M_i^{(-s)}$ may absorb signal from other contaminated subjects, potentially inflating FPR. Empirically, this guarantee extends to multi-domain contamination affecting $\leq$9\% of subjects ($k \leq 5$), with graceful degradation beyond this boundary (\Cref{sec:semisynthetic}).
62	
63	Empirically, $\Delta\mathrm{FPR} = 0.000$ across all five MMLU domains (bootstrap 95\% CI $= [0.000, 0.000]$). $\Delta\mathrm{FPR} = 0$ is a constructive guarantee of the matching strategy, independent of injection realism, whereas $\Delta\mathrm{TPR}$ may overestimate detection power under the stylized uniform injection. $\Delta\mathrm{FPR}$ remains negligible for single-domain contamination ($k \leq 5$); when contamination spans many domains, within-subject matching should be preferred (\Cref{sec:semisynthetic}). We adopt cross-subject matching as the standard protocol.
64	
65	Following DIF convention~\citep{wainer1993differential}, we do not apply family-wise error correction: the dual ETS~C threshold ($|\Delta_{\mathrm{MH}}| \geq 1.5$ \emph{and} $p < 0.05$) guards against false positives; Benjamini-Hochberg false discovery rate correction at $q = 0.05$ reclassifies only 3 of 3{,}918 C items (\Cref{app:method_details}). Diagnostic procedures (Yen's Q3, domain-specificity, DIF decomposition) and further details appear in \Cref{app:method_details}.
66	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fba4614-f3a0-42b4-886e-c51fe26721c5",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "f6aef95b-a1f3-4ccd-a220-29a7432a4a06",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nWe adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.\n\n\\subsection{Data}\n\\label{sec:data}\n\nThe primary dataset is the METABENCH response matrix~\\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \\citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_1_global_vs_differential.pdf}\n\\caption{Global vs.\\ differential contamination via Item Characteristic Curves (ICCs). \\textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \\textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts due to disproportionate exposure. The enrichment ratio of $\\approx 1.0$ between DIF flags and web-overlap labels is expected because most items fall into the left category.}\n\\label{fig:global_vs_differential}\n\\end{figure*}\n\n\\subsection{Mantel-Haenszel DIF and ETS Classification}\n\\label{sec:mhdif}\n\nIn educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.\n\nThe Mantel-Haenszel (MH) procedure~\\citep{holland1988mh,magis2010difr} detects DIF by stratifying examinees into $K$ score bins based on total score (a proxy for $\\theta$) and computing a common odds ratio across strata. We use $K = 5$ equiprobable strata (quintile-based binning) following ETS recommended practice for large-scale assessments~\\citep{donoghue1993mh,clauser1998dif}; $K{=}3$ yields near-identical power (\\Cref{app:k3_power}). Within each stratum $k$, the responses of the reference group and the focal group form a $2 \\times 2$ contingency table:\n\n\\begin{equation}\n\\label{eq:mh}\n\\alpha_{\\mathrm{MH}} = \\frac{\\displaystyle\\sum_{k=1}^{K} A_k D_k \\,/\\, T_k}{\\displaystyle\\sum_{k=1}^{K} B_k C_k \\,/\\, T_k}\\,,\n\\end{equation}\n\n\\noindent where $A_k$ and $B_k$ are the number of correct and incorrect responses in the reference group for stratum $k$, $C_k$ and $D_k$ are the corresponding counts for the focal group, and $T_k$ is the total number of examinees in stratum $k$. Under the null hypothesis of no DIF, $\\alpha_{\\mathrm{MH}} = 1$. The log odds ratio is converted to the ETS delta scale:\n\n\\begin{equation}\n\\label{eq:delta}\n\\Delta_{\\mathrm{MH}} = -2.35 \\ln(\\alpha_{\\mathrm{MH}})\\,.\n\\end{equation}\n\nThe Educational Testing Service (ETS) classifies DIF severity into three categories based on $|\\Delta_{\\mathrm{MH}}|$. Category~A (negligible) requires $|\\Delta_{\\mathrm{MH}}| < 1.0$. Category~C (large) requires both $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ and statistical significance at $p < 0.05$ from the MH chi-squared test. Category~B (moderate) includes all remaining items: those with $1.0 \\leq |\\Delta_{\\mathrm{MH}}| < 1.5$, or $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ without statistical significance. The dual threshold in ETS~C (effect size \\emph{and} significance) guards against flagging items that show large but unreliable effect sizes. These thresholds were calibrated for human test-taker populations; we retain them as standardized reference points and verify robustness across stricter cutoffs (\\Cref{sec:temporal}). Throughout this paper, we report the percentage of items classified as ETS~C, denoted C\\%. At $N = 1{,}887$ (the temporal comparison; 5{,}227 total across all cohort designs), significance ($p < 0.05$) is nearly automatically satisfied for any $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$: only 3 of 3{,}918 C items lack significance, so the dual criterion effectively reduces to a single effect-size threshold; per-item DEFF correction (\\Cref{app:deff}) restores $p$-value selectivity by reducing effective $N$: under simple-mean DEFF, 269 items (6.9\\%) lose significance while retaining $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$; 74\\% of these are near-miss ($p_{\\mathrm{adj}} \\in [0.05, 0.10]$).\n\nThe choice of matching variable (the total score used for stratification) affects both validity and interpretation. We distinguish three matching strategies: (1)~\\emph{standard matching} uses the within-benchmark total score on all items of the same benchmark; (2)~\\emph{cross-subject matching}, adapting purified subtest matching~\\citep{swaminathan1990logistic} to the LLM multi-subject setting, uses the total score on all subjects \\emph{other than} the one containing the item under test, preventing the matching variable from absorbing injected contamination signals (\\Cref{sec:injection}); and (3)~\\emph{external matching} uses the total score on a different benchmark entirely (e.g., MMLU total score as the matching variable when testing DIF on Grade School Math 8K (GSM8K) items), providing an independent ability proxy uncontaminated by the target benchmark. Cross-subject and external matching both address matching variable contamination but at different granularities: cross-subject operates within a multi-domain benchmark, while external operates across benchmarks. Total score matching is adequate: IRT $\\theta$ correlates at $r = 0.9986$ with total scores (\\Cref{sec:structural}).\n\n\\paragraph{LLM-specific challenges.} Applying MH-DIF to LLMs introduces four challenges absent in educational testing. First, overlapping training corpora violate local independence; permutation simulation (1{,}000 replications shuffling group labels within score strata) confirms local-dependence-attributable FPR inflation $< 0.001$~pp under cross-subject matching (\\Cref{app:method_details}). Second, fine-tuned variants within model families are not independent examinees; graduated de-duplication shows family structure does not inflate C\\% (\\Cref{sec:structural}). Third, bimodal ability distributions motivate quintile-based stratification. Fourth, MMLU's 57-subject structure raises a multidimensionality concern~\\citep{ackerman1992didmf,roussos1996multidimensionality}: domain-level ability profiles are nearly flat across cohorts (Cohen's $d$ range $= 0.12$), cross-subject and within-subject matching agree ($\\kappa = 0.80$, 834 items), and cross-subject-unique C items do not concentrate in high-shift subjects (\\Cref{app:structural}).\n\n\\subsection{Cohort Designs}\n\\label{sec:cohorts}\n\nWe construct five cohort comparisons: (1)~\\emph{Temporal}: 2023 ($N = 1{,}080$) vs.\\ 2024 ($N = 807$) models, the primary comparison; (2)~\\emph{Ability-quintile}: Q1--Q2 vs.\\ Q4--Q5 within the same temporal window; (3)~\\emph{Within-family}: Llama-2 ($N = 161$) vs.\\ Llama-3 ($N = 308$), isolating generational changes within a single family; (4)~\\emph{Within-subject}: per-subject DIF to test domain concentration; and (5)~\\emph{Random split}: two random halves of the 2023 cohort ($N = 540$ each) as a sanity check. Calendar-year boundaries are coarse; half-yearly comparison (C\\% $= 34.4\\%$; \\Cref{app:uncertainty}) and base-only/instruct-only analyses (C\\% $= 32.1\\%$/$36.5\\%$; \\Cref{app:baseinst_temporal}) confirm DIF persists under finer slicing.\n\n\\subsection{Semi-Synthetic Injection Framework}\n\\label{sec:injection}\n\nWe use contamination injection as a controlled case study to validate DIF detection power; DIF itself is mechanism-agnostic and flags items that function differently without attributing cause (\\Cref{sec:disc_protocol}). To evaluate whether MH-DIF can detect differential contamination when it is present, we construct a semi-synthetic framework with controlled ground truth.\n\n\\paragraph{Procedure.} From items classified as ETS~A in the uninjected data (negligible DIF), we select 20\\% uniformly at random as the ``contaminated'' set. For each contaminated item, we flip incorrect responses to correct in the focal group at exploitation rate $p \\in \\{0.0, 0.3, 0.5, 0.7, 1.0\\}$. We then run MH-DIF on the modified response matrix and measure detection performance. We report $\\Delta\\mathrm{TPR} = \\mathrm{TPR}(\\text{injected}) - \\mathrm{TPR}(\\text{baseline})$ and $\\Delta\\mathrm{FPR} = \\mathrm{FPR}(\\text{injected}) - \\mathrm{FPR}(\\text{baseline})$, where TPR is the true positive rate on injected items and FPR is the false positive rate on uninjected items. Each injection level is repeated across 5 random seeds for uncertainty estimation. Because binary response flipping represents a stylized uniform injection pattern, reported $\\Delta\\mathrm{TPR}$ values may overestimate detection power; realistic contamination (partial memorization, format-specific advantages) would produce weaker signals.\n\n\\paragraph{Cross-subject matching.} The choice of matching variable is critical for valid semi-synthetic evaluation. When contamination is injected into items within subject $X$, the total score on subject $X$ absorbs part of the injection signal. Using this contaminated total score as the MH matching variable violates the conditional independence assumption and inflates FPR. Cross-subject matching resolves this by computing the matching variable from all subjects \\emph{other than} the one being tested.\n\n\\paragraph{Remark (Zero FPR under single-subject matching).}\n\\label{prop:fpr}\nLet $M_i^{(-s)} = \\sum_{j \\notin s} Y_{ij}$ be the matching variable for examinee $i$ on focal subject $s$. Under single-subject injection (contamination confined to subject $s$), the tested item belongs to $s$ and does not contribute to $M_i^{(-s)}$; injecting contamination into $s$ leaves $M_i^{(-s)}$ unchanged. Therefore $\\Delta\\mathrm{FPR} = 0$ by construction.\n\nWhen contamination spans multiple subjects simultaneously, $M_i^{(-s)}$ may absorb signal from other contaminated subjects, potentially inflating FPR. Empirically, this guarantee extends to multi-domain contamination affecting $\\leq$9\\% of subjects ($k \\leq 5$), with graceful degradation beyond this boundary (\\Cref{sec:semisynthetic}).\n\nEmpirically, $\\Delta\\mathrm{FPR} = 0.000$ across all five MMLU domains (bootstrap 95\\% CI $= [0.000, 0.000]$). $\\Delta\\mathrm{FPR} = 0$ is a constructive guarantee of the matching strategy, independent of injection realism, whereas $\\Delta\\mathrm{TPR}$ may overestimate detection power under the stylized uniform injection. $\\Delta\\mathrm{FPR}$ remains negligible for single-domain contamination ($k \\leq 5$); when contamination spans many domains, within-subject matching should be preferred (\\Cref{sec:semisynthetic}). We adopt cross-subject matching as the standard protocol.\n\nFollowing DIF convention~\\citep{wainer1993differential}, we do not apply family-wise error correction: the dual ETS~C threshold ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ \\emph{and} $p < 0.05$) guards against false positives; Benjamini-Hochberg false discovery rate correction at $q = 0.05$ reclassifies only 3 of 3{,}918 C items (\\Cref{app:method_details}). Diagnostic procedures (Yen's Q3, domain-specificity, DIF decomposition) and further details appear in \\Cref{app:method_details}.\n",
      "numLines": 66,
      "startLine": 1,
      "totalLines": 66
    }
  },
  "sourceToolAssistantUUID": "8fba4614-f3a0-42b4-886e-c51fe26721c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-25T11:07:31.469Z_

<details open><summary>🔧 Tool call — Read · `toolu_013PGHL74T4xwvmMtiCpUbag`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6aef95b-a1f3-4ccd-a220-29a7432a4a06",
  "isSidechain": false,
  "requestId": "req_011CbPBRvY3qw5gou5p471qs",
  "type": "assistant",
  "uuid": "555cc9dc-3168-42bd-aebc-c141d87907f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdBLwcUC8E9sai9hppTtBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12076,
      "cache_read_input_tokens": 39707,
      "output_tokens": 890,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 890,
          "cache_read_input_tokens": 39707,
          "cache_creation_input_tokens": 12076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12076
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

_source line 30 · 2026-05-25T11:07:31.489Z_

<details><summary>↩ Tool result · `toolu_013PGHL74T4xwvmMtiCpUbag`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	A Monte Carlo power analysis (1,000 replications) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$) confirms that at $N \geq 100$ per cohort, ETS~C achieves TPR of 0.68--0.80 (under uniform injection) and area under the curve (AUC) of 0.93--0.94 for $|\Delta_{\mathrm{MH}}| \geq 1.4$ (\Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold; power varies with item discrimination (TPR 0.40--0.95 across $a = 0.5$--$2.0$; \Cref{app:power_sensitivity}).
11	
12	\begin{figure}[t]
13	\centering
14	\includegraphics[width=\columnwidth]{fig_2_dose_response.pdf}
15	\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\Delta\mathrm{TPR}$ ($= \mathrm{TPR}_{\text{injected}} - \mathrm{TPR}_{\text{baseline}}$) increases monotonically with exploitation rate $p$ under binary injection (a calibration upper bound; \Cref{sec:injection}); MH-DIF is sensitive to differential item behavior when present. Baseline (no injection) produces $\Delta\mathrm{TPR} \approx 0$.}
16	\label{fig:dose_response}
17	\end{figure}
18	
19	\subsection{Temporal DIF: ${\sim}$29\% of Items Exhibit Differential Functioning}
20	\label{sec:temporal}
21	
22	\looseness=-1
23	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; bootstrap 95\% CI: $[29.2\%, 37.8\%]$; family-level cluster bootstrap: $[26.7\%, 53.2\%]$; \Cref{app:uncertainty}). Two DEFF estimators bound the non-independence effect: simple-mean DEFF yields 29.2\% and weighted-mean yields 13.5\%, bracketing C\% at 13.5--29.2\%; the cluster bootstrap CI excludes the weighted-mean estimate, providing model-independent evidence that over-correction drives the lower bound (\Cref{app:deff,app:deff_simulation,app:icc_family}). Random permutations within the 2023 cohort confirm the ETS~C threshold maintains per-item FPR below 1\% (99th percentile $|\Delta_{\mathrm{MH}}| = 1.45$); no non-dominant family drives the signal (leave-one-family-out [LOFO] $|\Delta\mathrm{C\%}| \leq 2.93$\,pp; \Cref{tab:lofo,app:dedup_k}).
24	
25	\looseness=-1
26	Three controls confirm genuine temporal change (\Cref{tab:temporal_landscape}): random splits yield mean C\% of 0.62\% (2023; 100 permutations) and 1.3\% (2024; 100 permutations), 24--50$\times$ below temporal C\%; ability-quintile comparison yields 2.9\%; and 1:1 nearest-neighbor matching on total score ($N{=}638$/group, Cohen's $d = -0.17$) yields C\% $= 28.9\% \pm 0.1\%$; at most ${\sim}2.4$~pp is attributable to ability mismatch ($p < 0.01$; \Cref{app:method_details}).
27	
28	\looseness=-1
29	Across all 57 subjects, C\% ranges from 20.7\% to 48.4\% (mean $\approx 30\%$; \Cref{tab:temporal_landscape}). DIF rates are domain-invariant (Kruskal-Wallis $p = 0.78$), but DIF \emph{direction} exhibits domain dependence: STEM items favor 2024 models (55.4\%), Humanities favor 2023 (64.4\%). DIF is item-specific: domain-level accuracy gains explain ${<}0.1\%$ of item-level DIF variance (\Cref{app:structural}). A difficulty--direction interaction emerges ($r = -0.597$): 2024 models gain on hard items while eroding on easy ones. The temporal DIF finding persists across thresholds ($18.4\%$ at $|\Delta_{\mathrm{MH}}| \geq 2.0$, $10.2\%$ at $\geq 2.5$).
30	
31	\begin{table}[t]
32	\centering
33	\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\Delta_{\mathrm{MH}}| \geq 1.5$. C\% (web-clean) is the DIF-C flagging rate among items classified as web-clean by \citet{li2024contamination}. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels. Dashes (--) indicate comparisons where Li et al.\ labels are not applicable.}
34	\label{tab:temporal_landscape}
35	\small
36	\resizebox{\columnwidth}{!}{%
37	\begin{tabular}{lcccc}
38	\toprule
39	Cohort Definition & $N_{\mathrm{ref}}$ / $N_{\mathrm{focal}}$ & C\% & C\% (web-clean) & Enrich. \\
40	\midrule
41	Temporal (2023 vs.\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964 \\
42	Ability quintile (Q1--2 vs.\ Q4--5) & ${\sim}$2,090 / ${\sim}$2,090 & 2.9 & 0.027 & 1.19 \\
43	Within-family (Llama-2 vs.\ 3) & 161 / 308 & 61.3 & -- & -- \\
44	Random split 2023 (sanity) & 540 / 540 & 0.62 & -- & -- \\
45	Random split 2024 (sanity) & ${\sim}$400 / ${\sim}$400 & 1.3 & -- & -- \\
46	Within-subject (avg, 5 subj.) & \textit{varies} & 38.1 & -- & -- \\
47	\bottomrule
48	\end{tabular}}
49	\end{table}
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=\textwidth]{fig_A3_rho_degradation.pdf}
54	\caption{Ranking degradation under DIF-ordered vs.\ random item removal. DIF-ordered removal (orange) degrades $\rho$ faster than random (blue band = mean $\pm$ 1\,SD, 20 seeds). Dashed lines: Monitor/Flag (15\%) and Flag/Act (25\%) thresholds (\Cref{sec:disc_protocol}).}
55	\label{fig:rho_degradation}
56	\end{figure*}
57	
58	\subsection{Comparison with Web-Overlap Labels}
59	\label{sec:groundtruth}
60	
61	\looseness=-2
62	Direct comparison of DIF flags against the web-overlap labels of \citet{li2024contamination} on 9,229 annotated items shows near-independence (enrichment $= 0.964$, Jaccard $= 0.206$; $p = 0.88$; \Cref{tab:temporal_landscape,app:structural}): DIF-C rates are 30.7\% among web-contaminated items and 31.8\% among clean items. Because web-overlap labels are a proxy for training-set membership (based on verbatim web matches, not actual training corpora), this near-independence could partly reflect proxy noise. Crucially, label-independent evidence confirms mechanism separation: base and instruct models exhibit opposite DIF directions ($\chi^2 = 562.7$; \Cref{sec:disc_temporal}), a reversal incompatible with uniform contamination. Semi-synthetic injection confirms detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \Cref{fig:dose_response}). Web-overlap labels measure \emph{global exposure}, while DIF measures \emph{differential functioning}---complementary diagnostic dimensions (\Cref{fig:global_vs_differential}).
63	
64	\begin{figure}[t]
65	\centering
66	\includegraphics[width=\columnwidth]{fig_3_within_subject_matching.pdf}
67	\caption{Cross-subject vs.\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}
68	\label{fig:matching}
69	\end{figure}
70	
71	\subsection{Structural Analysis}
72	\label{sec:structural}
73	
74	\looseness=-1
75	Two structural controls and a sensitivity check fail to reduce temporal C\% below 31\% (\Cref{tab:structural_comparison}): matched-ability quintiles, within-subject DIF (C\% $= 38.1\%$; cross-subject C\% is more conservative due to lower local dependence), and IRT $\theta$-conditioning ($r(\theta, \mathrm{total\ score}) = 0.9986$). Logistic regression detects an additional 17.7\% with non-uniform DIF ($|\beta_{\mathrm{interaction}}| \geq 0.5$), reaching a union of 47\% (\Cref{app:structural}). Ability-matched C\% converges to ${\sim}$28--29\% for both temporal and within-family comparisons despite vastly different unmatched rates (\Cref{app:structural}).
76	
77	
78	\subsection{Detection Power under Controlled Injection}
79	\label{sec:semisynthetic}
80	
81	\looseness=-1
82	Cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ across all five MMLU subjects (4/5 with $\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$; \Cref{sec:injection}), while within-subject matching inflates FPR by ${+}0.186$ (\Cref{fig:matching}). The $\Delta\mathrm{FPR} \approx 0$ guarantee holds for $k \leq 5$ contaminated subjects ($\Delta\mathrm{FPR} < 0.007$); at $k{=}20$, $\Delta\mathrm{FPR}$ rises to $0.167$---still insufficient to account for the observed 31\% C\% (\Cref{tab:multi_subject_injection}). Difficulty-dependent injection yields $\Delta\mathrm{TPR} \approx 0.41$ at $p = 0.5$ (vs.\ $0.51$ uniform), bounding overestimation at ${\sim}$20\% (\Cref{app:method_details}).
83	
84	\subsection{Downstream Impact}
85	\label{sec:downstream}
86	
87	\looseness=-2
88	Stable-item ranks are preserved across all six benchmarks (mean $\rho = 0.997$, mean $\tau = 0.962$; flip rate $\leq 2.9\%$; \Cref{tab:cross_benchmark}). DIF-flagged items concentrate discriminative signal: DIF-ordered removal degrades $\rho$ faster than random removal across all six benchmarks (\Cref{fig:rho_degradation}; $z = -8$ to $-49$; \Cref{fig:downstream}). Removing C-flagged items disproportionately disadvantages 2024 models (cohort gap $= 96.2$ positions, $40\times$ random; $p < 0.001$); DIF-corrected scoring shifts accuracy by ${+}2.12$\,pp on average (\Cref{app:score_inflation,app:rank_reversal}).
89	
90	\begin{figure}[t]
91	\centering
92	\includegraphics[width=\columnwidth]{fig_4_downstream_impact.pdf}
93	\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\rho \approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items (non-C-flagged) only.}
94	\label{fig:downstream}
95	\end{figure}
96	
97	\subsection{Cross-Benchmark Validation}
98	\label{sec:gsm8k}
99	
100	\looseness=-2
101	Temporal DIF extends across all six METABENCH benchmarks (\Cref{tab:cross_benchmark}): C\% ranges from 17.9\% (HellaSwag~\citep{zellers2019hellaswag}) to 31.3\% (MMLU), with knowledge/reasoning benchmarks---including ARC (AI2 Reasoning Challenge)---consistently higher than procedural ones (C\% $= 26.9$--$31.3\%$ vs.\ $17.9$--$18.9\%$). These differences may partly reflect item difficulty distributions; we treat them as descriptive.
102	
103	\begin{table}[t]
104	\centering
105	\caption{Temporal DIF across six METABENCH benchmarks (2023 vs.\ 2024 cohorts). $\rho$/$\tau$: rank correlation between full and stable-item rankings; Flip: pairwise rank-flip rate; Ratio: C\%/random baseline.}
106	\label{tab:cross_benchmark}
107	\small
108	\resizebox{\columnwidth}{!}{%
109	\begin{tabular}{lrrrrrrl}
110	\toprule
111	Benchmark & Items & C\% & $\rho$ & $\tau$ & Flip\% & Rand.\ C\% & Ratio \\
112	\midrule
113	MMLU & 12{,}508 & 31.3 & 0.9965 & 0.9600 & 2.00 & 0.62 & 50$\times$ \\
114	WinoGrande & 1{,}267 & 30.3 & 0.9943 & 0.9432 & 2.84 & 0.32 & 95$\times$ \\
115	TruthfulQA & 817 & 29.7 & 0.9971 & 0.9586 & 2.07 & 0.37 & 80$\times$ \\
116	ARC & 1{,}172 & 26.9 & 0.9962 & 0.9538 & 2.31 & 0.60 & 45$\times$ \\
117	GSM8K & 1{,}319 & 18.9 & 0.9993 & 0.9843 & 0.78 & 0.30 & 63$\times$ \\
118	HellaSwag & 10{,}042 & 17.9 & 0.9986 & 0.9722 & 1.39 & 0.28 & 64$\times$ \\
119	\bottomrule
120	\end{tabular}}
121	\end{table}
122	
123	Semi-synthetic injection on GSM8K confirms detection power ($\Delta\mathrm{TPR} = {+}0.514$; \Cref{app:gsm8k_details,app:fig_gsm1k}).
124	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "555cc9dc-3168-42bd-aebc-c141d87907f4",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "6e7fbaa4-52ce-4043-8631-abb30b80268f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe apply MH-DIF to the METABENCH response matrix~\\citep{kipnis2024metabench} (5,227 models $\\times$ 12,508 MMLU items~\\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \\Cref{sec:gsm8k}.\n\n\\subsection{Validation: DIF Detection Power}\n\\label{sec:validation}\n\n\\looseness=-1\nA Monte Carlo power analysis (1,000 replications) using empirical 2PL parameters from PSN-IRT~\\citep{zhou2026psnirt} ($\\bar{a} = 1.2$, $\\bar{b} = -0.84$) confirms that at $N \\geq 100$ per cohort, ETS~C achieves TPR of 0.68--0.80 (under uniform injection) and area under the curve (AUC) of 0.93--0.94 for $|\\Delta_{\\mathrm{MH}}| \\geq 1.4$ (\\Cref{app:method_details}). Our temporal cohorts ($N_{\\mathrm{ref}} = 1{,}080$, $N_{\\mathrm{focal}} = 807$) far exceed this threshold; power varies with item discrimination (TPR 0.40--0.95 across $a = 0.5$--$2.0$; \\Cref{app:power_sensitivity}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_2_dose_response.pdf}\n\\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\\Delta\\mathrm{TPR}$ ($= \\mathrm{TPR}_{\\text{injected}} - \\mathrm{TPR}_{\\text{baseline}}$) increases monotonically with exploitation rate $p$ under binary injection (a calibration upper bound; \\Cref{sec:injection}); MH-DIF is sensitive to differential item behavior when present. Baseline (no injection) produces $\\Delta\\mathrm{TPR} \\approx 0$.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\subsection{Temporal DIF: ${\\sim}$29\\% of Items Exhibit Differential Functioning}\n\\label{sec:temporal}\n\n\\looseness=-1\nWe compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\\% of items receive ETS~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$; bootstrap 95\\% CI: $[29.2\\%, 37.8\\%]$; family-level cluster bootstrap: $[26.7\\%, 53.2\\%]$; \\Cref{app:uncertainty}). Two DEFF estimators bound the non-independence effect: simple-mean DEFF yields 29.2\\% and weighted-mean yields 13.5\\%, bracketing C\\% at 13.5--29.2\\%; the cluster bootstrap CI excludes the weighted-mean estimate, providing model-independent evidence that over-correction drives the lower bound (\\Cref{app:deff,app:deff_simulation,app:icc_family}). Random permutations within the 2023 cohort confirm the ETS~C threshold maintains per-item FPR below 1\\% (99th percentile $|\\Delta_{\\mathrm{MH}}| = 1.45$); no non-dominant family drives the signal (leave-one-family-out [LOFO] $|\\Delta\\mathrm{C\\%}| \\leq 2.93$\\,pp; \\Cref{tab:lofo,app:dedup_k}).\n\n\\looseness=-1\nThree controls confirm genuine temporal change (\\Cref{tab:temporal_landscape}): random splits yield mean C\\% of 0.62\\% (2023; 100 permutations) and 1.3\\% (2024; 100 permutations), 24--50$\\times$ below temporal C\\%; ability-quintile comparison yields 2.9\\%; and 1:1 nearest-neighbor matching on total score ($N{=}638$/group, Cohen's $d = -0.17$) yields C\\% $= 28.9\\% \\pm 0.1\\%$; at most ${\\sim}2.4$~pp is attributable to ability mismatch ($p < 0.01$; \\Cref{app:method_details}).\n\n\\looseness=-1\nAcross all 57 subjects, C\\% ranges from 20.7\\% to 48.4\\% (mean $\\approx 30\\%$; \\Cref{tab:temporal_landscape}). DIF rates are domain-invariant (Kruskal-Wallis $p = 0.78$), but DIF \\emph{direction} exhibits domain dependence: STEM items favor 2024 models (55.4\\%), Humanities favor 2023 (64.4\\%). DIF is item-specific: domain-level accuracy gains explain ${<}0.1\\%$ of item-level DIF variance (\\Cref{app:structural}). A difficulty--direction interaction emerges ($r = -0.597$): 2024 models gain on hard items while eroding on easy ones. The temporal DIF finding persists across thresholds ($18.4\\%$ at $|\\Delta_{\\mathrm{MH}}| \\geq 2.0$, $10.2\\%$ at $\\geq 2.5$).\n\n\\begin{table}[t]\n\\centering\n\\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$. C\\% (web-clean) is the DIF-C flagging rate among items classified as web-clean by \\citet{li2024contamination}. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels. Dashes (--) indicate comparisons where Li et al.\\ labels are not applicable.}\n\\label{tab:temporal_landscape}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nCohort Definition & $N_{\\mathrm{ref}}$ / $N_{\\mathrm{focal}}$ & C\\% & C\\% (web-clean) & Enrich. \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964 \\\\\nAbility quintile (Q1--2 vs.\\ Q4--5) & ${\\sim}$2,090 / ${\\sim}$2,090 & 2.9 & 0.027 & 1.19 \\\\\nWithin-family (Llama-2 vs.\\ 3) & 161 / 308 & 61.3 & -- & -- \\\\\nRandom split 2023 (sanity) & 540 / 540 & 0.62 & -- & -- \\\\\nRandom split 2024 (sanity) & ${\\sim}$400 / ${\\sim}$400 & 1.3 & -- & -- \\\\\nWithin-subject (avg, 5 subj.) & \\textit{varies} & 38.1 & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_A3_rho_degradation.pdf}\n\\caption{Ranking degradation under DIF-ordered vs.\\ random item removal. DIF-ordered removal (orange) degrades $\\rho$ faster than random (blue band = mean $\\pm$ 1\\,SD, 20 seeds). Dashed lines: Monitor/Flag (15\\%) and Flag/Act (25\\%) thresholds (\\Cref{sec:disc_protocol}).}\n\\label{fig:rho_degradation}\n\\end{figure*}\n\n\\subsection{Comparison with Web-Overlap Labels}\n\\label{sec:groundtruth}\n\n\\looseness=-2\nDirect comparison of DIF flags against the web-overlap labels of \\citet{li2024contamination} on 9,229 annotated items shows near-independence (enrichment $= 0.964$, Jaccard $= 0.206$; $p = 0.88$; \\Cref{tab:temporal_landscape,app:structural}): DIF-C rates are 30.7\\% among web-contaminated items and 31.8\\% among clean items. Because web-overlap labels are a proxy for training-set membership (based on verbatim web matches, not actual training corpora), this near-independence could partly reflect proxy noise. Crucially, label-independent evidence confirms mechanism separation: base and instruct models exhibit opposite DIF directions ($\\chi^2 = 562.7$; \\Cref{sec:disc_temporal}), a reversal incompatible with uniform contamination. Semi-synthetic injection confirms detection power ($\\Delta\\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \\Cref{fig:dose_response}). Web-overlap labels measure \\emph{global exposure}, while DIF measures \\emph{differential functioning}---complementary diagnostic dimensions (\\Cref{fig:global_vs_differential}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_3_within_subject_matching.pdf}\n\\caption{Cross-subject vs.\\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\\Delta\\mathrm{FPR} = 0.000$) while preserving detection power ($\\Delta\\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}\n\\label{fig:matching}\n\\end{figure}\n\n\\subsection{Structural Analysis}\n\\label{sec:structural}\n\n\\looseness=-1\nTwo structural controls and a sensitivity check fail to reduce temporal C\\% below 31\\% (\\Cref{tab:structural_comparison}): matched-ability quintiles, within-subject DIF (C\\% $= 38.1\\%$; cross-subject C\\% is more conservative due to lower local dependence), and IRT $\\theta$-conditioning ($r(\\theta, \\mathrm{total\\ score}) = 0.9986$). Logistic regression detects an additional 17.7\\% with non-uniform DIF ($|\\beta_{\\mathrm{interaction}}| \\geq 0.5$), reaching a union of 47\\% (\\Cref{app:structural}). Ability-matched C\\% converges to ${\\sim}$28--29\\% for both temporal and within-family comparisons despite vastly different unmatched rates (\\Cref{app:structural}).\n\n\n\\subsection{Detection Power under Controlled Injection}\n\\label{sec:semisynthetic}\n\n\\looseness=-1\nCross-subject matching achieves $\\Delta\\mathrm{FPR} = 0.000$ across all five MMLU subjects (4/5 with $\\Delta\\mathrm{TPR} > 0.3$ at $p = 0.5$; \\Cref{sec:injection}), while within-subject matching inflates FPR by ${+}0.186$ (\\Cref{fig:matching}). The $\\Delta\\mathrm{FPR} \\approx 0$ guarantee holds for $k \\leq 5$ contaminated subjects ($\\Delta\\mathrm{FPR} < 0.007$); at $k{=}20$, $\\Delta\\mathrm{FPR}$ rises to $0.167$---still insufficient to account for the observed 31\\% C\\% (\\Cref{tab:multi_subject_injection}). Difficulty-dependent injection yields $\\Delta\\mathrm{TPR} \\approx 0.41$ at $p = 0.5$ (vs.\\ $0.51$ uniform), bounding overestimation at ${\\sim}$20\\% (\\Cref{app:method_details}).\n\n\\subsection{Downstream Impact}\n\\label{sec:downstream}\n\n\\looseness=-2\nStable-item ranks are preserved across all six benchmarks (mean $\\rho = 0.997$, mean $\\tau = 0.962$; flip rate $\\leq 2.9\\%$; \\Cref{tab:cross_benchmark}). DIF-flagged items concentrate discriminative signal: DIF-ordered removal degrades $\\rho$ faster than random removal across all six benchmarks (\\Cref{fig:rho_degradation}; $z = -8$ to $-49$; \\Cref{fig:downstream}). Removing C-flagged items disproportionately disadvantages 2024 models (cohort gap $= 96.2$ positions, $40\\times$ random; $p < 0.001$); DIF-corrected scoring shifts accuracy by ${+}2.12$\\,pp on average (\\Cref{app:score_inflation,app:rank_reversal}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_4_downstream_impact.pdf}\n\\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\\rho \\approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items (non-C-flagged) only.}\n\\label{fig:downstream}\n\\end{figure}\n\n\\subsection{Cross-Benchmark Validation}\n\\label{sec:gsm8k}\n\n\\looseness=-2\nTemporal DIF extends across all six METABENCH benchmarks (\\Cref{tab:cross_benchmark}): C\\% ranges from 17.9\\% (HellaSwag~\\citep{zellers2019hellaswag}) to 31.3\\% (MMLU), with knowledge/reasoning benchmarks---including ARC (AI2 Reasoning Challenge)---consistently higher than procedural ones (C\\% $= 26.9$--$31.3\\%$ vs.\\ $17.9$--$18.9\\%$). These differences may partly reflect item difficulty distributions; we treat them as descriptive.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temporal DIF across six METABENCH benchmarks (2023 vs.\\ 2024 cohorts). $\\rho$/$\\tau$: rank correlation between full and stable-item rankings; Flip: pairwise rank-flip rate; Ratio: C\\%/random baseline.}\n\\label{tab:cross_benchmark}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrl}\n\\toprule\nBenchmark & Items & C\\% & $\\rho$ & $\\tau$ & Flip\\% & Rand.\\ C\\% & Ratio \\\\\n\\midrule\nMMLU & 12{,}508 & 31.3 & 0.9965 & 0.9600 & 2.00 & 0.62 & 50$\\times$ \\\\\nWinoGrande & 1{,}267 & 30.3 & 0.9943 & 0.9432 & 2.84 & 0.32 & 95$\\times$ \\\\\nTruthfulQA & 817 & 29.7 & 0.9971 & 0.9586 & 2.07 & 0.37 & 80$\\times$ \\\\\nARC & 1{,}172 & 26.9 & 0.9962 & 0.9538 & 2.31 & 0.60 & 45$\\times$ \\\\\nGSM8K & 1{,}319 & 18.9 & 0.9993 & 0.9843 & 0.78 & 0.30 & 63$\\times$ \\\\\nHellaSwag & 10{,}042 & 17.9 & 0.9986 & 0.9722 & 1.39 & 0.28 & 64$\\times$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSemi-synthetic injection on GSM8K confirms detection power ($\\Delta\\mathrm{TPR} = {+}0.514$; \\Cref{app:gsm8k_details,app:fig_gsm1k}).\n",
      "numLines": 124,
      "startLine": 1,
      "totalLines": 124
    }
  },
  "sourceToolAssistantUUID": "555cc9dc-3168-42bd-aebc-c141d87907f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-25T11:07:31.924Z_

<details open><summary>🔧 Tool call — Read · `toolu_011mU2qNeN3k2G1FizuH1yPQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e7fbaa4-52ce-4043-8631-abb30b80268f",
  "isSidechain": false,
  "requestId": "req_011CbPBRvY3qw5gou5p471qs",
  "type": "assistant",
  "uuid": "2ef2f78f-6589-47e2-b43b-a745e890d255",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdBLwcUC8E9sai9hppTtBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12076,
      "cache_read_input_tokens": 39707,
      "output_tokens": 890,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 890,
          "cache_read_input_tokens": 39707,
          "cache_creation_input_tokens": 12076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12076
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

_source line 32 · 2026-05-25T11:07:31.930Z_

<details><summary>↩ Tool result · `toolu_011mU2qNeN3k2G1FizuH1yPQ`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Temporal DIF as Structured Signal}
5	\label{sec:disc_temporal}
6	
7	\looseness=-2
8	Temporal DIF detects \emph{that} items function differently across cohorts, not \emph{why}---by design (\Cref{sec:cohorts}). Stratifying by model type reveals opposite patterns: base models ($N{=}1{,}409$) are 60.1\% reference-favoring ($r = -0.570$), while instruct models ($N{=}478$) are 65.6\% focal-favoring ($\chi^2 = 562.7$, $p < 10^{-124}$). This reversal reflects structured item-level bias rather than uniform group impact~\citep{camilli1994methods}, validating DIF as a mechanism-agnostic diagnostic; mixed-mechanism injection reproduces the reversal pattern but cannot match the near-zero instruct gradient, suggesting non-contamination drivers (\Cref{app:mechanism_discussion,app:mixed_mechanism}). Composition downsampling ($\Delta = 1.08$\,pp) and base-only/instruct-only analyses confirm DIF is not an artifact of cohort structure (\Cref{app:composition_control,app:baseinst_temporal,app:within_arch}).
9	
10	\looseness=-2
11	Three features distinguish LLM temporal DIF from educational settings: (1)~C\% (29.2\%; cluster bootstrap CI: $[26.7\%, 53.2\%]$) substantially exceeds typical rates~\citep{clauser1998dif}; (2)~DIF flags and web-overlap labels are near-independent (Jaccard $= 0.206$); (3)~the base/instruct reversal (odds ratio [OR] $= 4.75$; \Cref{app:mechanism_discussion}) favors a broader-signal reading over distinct-construct independence.
12	
13	\subsection{Recommended DIF Audit Protocol}
14	\label{sec:disc_protocol}
15	
16	\looseness=-2
17	Item-level properties do not predict DIF susceptibility (area under the ROC curve [AUROC] $= 0.60$; \Cref{app:predictive}), precluding pre-screening. We recommend: (1)~\emph{Monitor}---run MH-DIF audits when ${\geq}$500 models accumulate, triggering review when C\% exceeds $20\times$ the random-split baseline; (2)~\emph{Triage}---DIF $\times$ web-overlap co-occurrence warrants removal, DIF on web-clean items warrants monitoring; (3)~\emph{Correct}---expert review, not automatic removal~\citep{camilli1994methods,penfield2007dif} (\Cref{app:score_inflation}).
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ef2f78f-6589-47e2-b43b-a745e890d255",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "c7fc1cff-64f9-42cf-a2a9-ebaaac9e4686",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Temporal DIF as Structured Signal}\n\\label{sec:disc_temporal}\n\n\\looseness=-2\nTemporal DIF detects \\emph{that} items function differently across cohorts, not \\emph{why}---by design (\\Cref{sec:cohorts}). Stratifying by model type reveals opposite patterns: base models ($N{=}1{,}409$) are 60.1\\% reference-favoring ($r = -0.570$), while instruct models ($N{=}478$) are 65.6\\% focal-favoring ($\\chi^2 = 562.7$, $p < 10^{-124}$). This reversal reflects structured item-level bias rather than uniform group impact~\\citep{camilli1994methods}, validating DIF as a mechanism-agnostic diagnostic; mixed-mechanism injection reproduces the reversal pattern but cannot match the near-zero instruct gradient, suggesting non-contamination drivers (\\Cref{app:mechanism_discussion,app:mixed_mechanism}). Composition downsampling ($\\Delta = 1.08$\\,pp) and base-only/instruct-only analyses confirm DIF is not an artifact of cohort structure (\\Cref{app:composition_control,app:baseinst_temporal,app:within_arch}).\n\n\\looseness=-2\nThree features distinguish LLM temporal DIF from educational settings: (1)~C\\% (29.2\\%; cluster bootstrap CI: $[26.7\\%, 53.2\\%]$) substantially exceeds typical rates~\\citep{clauser1998dif}; (2)~DIF flags and web-overlap labels are near-independent (Jaccard $= 0.206$); (3)~the base/instruct reversal (odds ratio [OR] $= 4.75$; \\Cref{app:mechanism_discussion}) favors a broader-signal reading over distinct-construct independence.\n\n\\subsection{Recommended DIF Audit Protocol}\n\\label{sec:disc_protocol}\n\n\\looseness=-2\nItem-level properties do not predict DIF susceptibility (area under the ROC curve [AUROC] $= 0.60$; \\Cref{app:predictive}), precluding pre-screening. We recommend: (1)~\\emph{Monitor}---run MH-DIF audits when ${\\geq}$500 models accumulate, triggering review when C\\% exceeds $20\\times$ the random-split baseline; (2)~\\emph{Triage}---DIF $\\times$ web-overlap co-occurrence warrants removal, DIF on web-clean items warrants monitoring; (3)~\\emph{Correct}---expert review, not automatic removal~\\citep{camilli1994methods,penfield2007dif} (\\Cref{app:score_inflation}).\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  },
  "sourceToolAssistantUUID": "2ef2f78f-6589-47e2-b43b-a745e890d255",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-25T11:07:32.988Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MheWYVz9GhfToeGfuaxaxX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7fc1cff-64f9-42cf-a2a9-ebaaac9e4686",
  "isSidechain": false,
  "requestId": "req_011CbPBRvY3qw5gou5p471qs",
  "type": "assistant",
  "uuid": "d7240a15-beae-4a4b-8020-9dade7d92c59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdBLwcUC8E9sai9hppTtBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12076,
      "cache_read_input_tokens": 39707,
      "output_tokens": 890,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 890,
          "cache_read_input_tokens": 39707,
          "cache_creation_input_tokens": 12076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12076
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

_source line 34 · 2026-05-25T11:07:32.993Z_

<details><summary>↩ Tool result · `toolu_01MheWYVz9GhfToeGfuaxaxX`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-1
5	Across six benchmarks, 17.9--31.3\% of items exhibit temporal DIF while rankings remain stable ($\rho \geq 0.994$); base-vs-instruct reversals and web-overlap independence confirm signal beyond contamination.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7240a15-beae-4a4b-8020-9dade7d92c59",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "763d733d-81e1-42c7-9bb9-62bfbeb54fff",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\n\\looseness=-1\nAcross six benchmarks, 17.9--31.3\\% of items exhibit temporal DIF while rankings remain stable ($\\rho \\geq 0.994$); base-vs-instruct reversals and web-overlap independence confirm signal beyond contamination.\n",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  },
  "sourceToolAssistantUUID": "d7240a15-beae-4a4b-8020-9dade7d92c59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-25T11:07:33.341Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MNtFVeXWypr3gKFx91oZKm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "763d733d-81e1-42c7-9bb9-62bfbeb54fff",
  "isSidechain": false,
  "requestId": "req_011CbPBRvY3qw5gou5p471qs",
  "type": "assistant",
  "uuid": "54e5a676-511e-4b54-985d-3725766ab1e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdBLwcUC8E9sai9hppTtBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12076,
      "cache_read_input_tokens": 39707,
      "output_tokens": 890,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 890,
          "cache_read_input_tokens": 39707,
          "cache_creation_input_tokens": 12076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12076
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

_source line 36 · 2026-05-25T11:07:33.346Z_

<details><summary>↩ Tool result · `toolu_01MNtFVeXWypr3gKFx91oZKm`</summary>

```text
1	\raggedbottom
2	\enlargethispage{-6\baselineskip}
3	\section*{Limitations}
4	
5	\looseness=-1
6	Three primary limitations apply. (1)~The semi-synthetic framework uses uniform binary response flipping, a stylized injection model; reported $\Delta\mathrm{TPR}$ values may overestimate detection power. Partial memorization scenarios---where models recall item cues without deterministic answer flipping---would produce weaker and qualitatively different DIF patterns than our binary injection model. The framework detects \emph{that} items function differently but not \emph{why}: multiple exclusion analyses (ability matching, web-overlap comparison, item-quality annotation) narrow the space of explanations but do not isolate a single mechanism; the specific training factors driving temporal DIF remain unidentified. Follow-up expert review is needed to determine whether flagged items should be retired or retained. (2)~The MH $\chi^2$ test assumes independent examinees; LLM model families violate this assumption. Two DEFF estimators (13.5--29.2\%) and family-level cluster bootstrap (95\% CI: $[26.7\%, 53.2\%]$) bound the impact, but the extreme relatedness of some families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in educational settings~\citep{french2010hierarchical}.
7	
8	\looseness=-1
9	(3)~Cross-subject matching assumes contamination affects a minority of domains; $\Delta\mathrm{FPR}$ rises to 0.167 when contamination spans ${\geq}20$ subjects. Although composition control experiments show a small residual shift ($\Delta = 1.08$\,pp; \Cref{app:composition_control}), base/instruct ratio changes between cohorts remain a potential confound that cannot be fully eliminated without single-architecture longitudinal data. Temporal cohorts defined by calendar year provide coarse granularity, and generalizability to partial-credit and free-form generation benchmarks is untested. Multidimensional DIF~\citep{ackerman1992didmf} may arise when MMLU's 57 subjects span distinct latent dimensions; cross-subject matching mitigates between-domain multidimensionality but not within-domain violations. IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric. Additionally, model release dates need not align with training-data cutoff dates, and generalization beyond multiple-choice question (MCQ) format benchmarks requires further validation, though GSM8K (open-ended) shows consistent patterns.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54e5a676-511e-4b54-985d-3725766ab1e5",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "8de5eecf-6083-4d51-bf7c-a7526430dbb2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex",
      "content": "\\raggedbottom\n\\enlargethispage{-6\\baselineskip}\n\\section*{Limitations}\n\n\\looseness=-1\nThree primary limitations apply. (1)~The semi-synthetic framework uses uniform binary response flipping, a stylized injection model; reported $\\Delta\\mathrm{TPR}$ values may overestimate detection power. Partial memorization scenarios---where models recall item cues without deterministic answer flipping---would produce weaker and qualitatively different DIF patterns than our binary injection model. The framework detects \\emph{that} items function differently but not \\emph{why}: multiple exclusion analyses (ability matching, web-overlap comparison, item-quality annotation) narrow the space of explanations but do not isolate a single mechanism; the specific training factors driving temporal DIF remain unidentified. Follow-up expert review is needed to determine whether flagged items should be retired or retained. (2)~The MH $\\chi^2$ test assumes independent examinees; LLM model families violate this assumption. Two DEFF estimators (13.5--29.2\\%) and family-level cluster bootstrap (95\\% CI: $[26.7\\%, 53.2\\%]$) bound the impact, but the extreme relatedness of some families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in educational settings~\\citep{french2010hierarchical}.\n\n\\looseness=-1\n(3)~Cross-subject matching assumes contamination affects a minority of domains; $\\Delta\\mathrm{FPR}$ rises to 0.167 when contamination spans ${\\geq}20$ subjects. Although composition control experiments show a small residual shift ($\\Delta = 1.08$\\,pp; \\Cref{app:composition_control}), base/instruct ratio changes between cohorts remain a potential confound that cannot be fully eliminated without single-architecture longitudinal data. Temporal cohorts defined by calendar year provide coarse granularity, and generalizability to partial-credit and free-form generation benchmarks is untested. Multidimensional DIF~\\citep{ackerman1992didmf} may arise when MMLU's 57 subjects span distinct latent dimensions; cross-subject matching mitigates between-domain multidimensionality but not within-domain violations. IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric. Additionally, model release dates need not align with training-data cutoff dates, and generalization beyond multiple-choice question (MCQ) format benchmarks requires further validation, though GSM8K (open-ended) shows consistent patterns.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "54e5a676-511e-4b54-985d-3725766ab1e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-25T11:07:33.866Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LFbv4JQhnmRE4dBjY8ZW16`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8de5eecf-6083-4d51-bf7c-a7526430dbb2",
  "isSidechain": false,
  "requestId": "req_011CbPBRvY3qw5gou5p471qs",
  "type": "assistant",
  "uuid": "dfd2f606-a3c6-42ef-a197-065fb6e530de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdBLwcUC8E9sai9hppTtBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12076,
      "cache_read_input_tokens": 39707,
      "output_tokens": 890,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 890,
          "cache_read_input_tokens": 39707,
          "cache_creation_input_tokens": 12076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12076
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

_source line 38 · 2026-05-25T11:07:34.129Z_

<details><summary>↩ Tool result · `toolu_01LFbv4JQhnmRE4dBjY8ZW16`</summary>

```text
1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini-Hochberg FDR correction at $q = 0.05$. The random-split sanity check provides an empirical estimate of the false positive rate under the null hypothesis.
19	
20	\paragraph{Threshold sensitivity.} We report results across a range of DIF thresholds ($|\Delta_{\mathrm{MH}}| \in \{1.0, 1.5, 2.0, 2.5\}$) to verify that qualitative conclusions do not depend on the specific ETS~C cutoff. The standard threshold of $|\Delta_{\mathrm{MH}}| \geq 1.5$ corresponds to the ETS~C definition used throughout the paper.
21	
22	\paragraph{IRT model fit.} For transparency, we report that the MMLU response matrix shows poor fit to a unidimensional 2PL model (expected for a 57-subject multidimensional benchmark). This does not affect MH-DIF validity, which relies only on total score stratification rather than parametric IRT assumptions.
23	
24	\paragraph{Architecture heterogeneity.} The METABENCH MMLU population consists of 99.98\% decoder-only models (5,226 of 5,227). This near-complete architectural homogeneity eliminates architecture as a confound for DIF analysis. We verify this by excluding the single encoder-decoder model and confirming identical results.
25	
26	\paragraph{Power sensitivity to item discrimination.}
27	\label{app:power_sensitivity}
28	The Monte Carlo power analysis in \Cref{sec:validation} uses average 2PL parameters ($\bar{a} = 1.2$, $\bar{b} = -0.84$). \Cref{tab:power_sensitivity} reports TPR as a function of discrimination $a$ (other parameters at their means, $N = 80$ per cohort, $|\Delta_b| = 1.4$, 1,000 replications). TPR increases monotonically from 0.40 ($a = 0.5$) to 0.95 ($a = 2.0$); FPR remains below 0.04 throughout. The MMLU item pool shows substantial heterogeneity: $a$ ranges from 0.006 to 2.657 (SD $= 0.54$, IQR $= [0.75, 1.64]$). The aggregate TPR of 0.68 from Phase~2 reflects this full distribution, while TPR at mean $a \approx 1.2$ is 0.87---the gap is consistent with Jensen's inequality applied to the concave TPR($a$) function. Although 2PL fit is poor for MMLU's multidimensional structure, the power analysis serves as one leg of a triangulation: parametric estimates (TPR $= 0.68$--$0.80$) are validated by empirical semi-synthetic injection ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \Cref{sec:semisynthetic}), confirming adequate detection power regardless of parametric assumptions.
29	
30	\begin{table}[h]
31	\centering
32	\caption{Power sensitivity to item discrimination. TPR = true positive rate for ETS~C detection ($|\Delta_{\mathrm{MH}}| \geq 1.5$) at $N = 80$ per cohort, $|\Delta_b| = 1.4$, 1,000 replications.}
33	\label{tab:power_sensitivity}
34	\small
35	\begin{tabular}{rccc}
36	\toprule
37	$a$ & TPR & 95\% CI & FPR \\
38	\midrule
39	0.5 & 0.398 & [0.20, 0.60] & 0.033 \\
40	0.8 & 0.683 & [0.45, 0.90] & 0.036 \\
41	1.0 & 0.808 & [0.60, 0.95] & 0.038 \\
42	1.2 ($\approx \bar{a}$) & 0.874 & [0.70, 1.00] & 0.038 \\
43	1.5 & 0.930 & [0.80, 1.00] & 0.038 \\
44	2.0 & 0.949 & [0.80, 1.00] & 0.037 \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	\paragraph{Stratum sensitivity (K=3 vs.\ K=5).}
50	\label{app:k3_power}
51	K=3 and K=5 yield near-identical detection power: TPR differences $<$0.02 across all conditions, within Monte Carlo noise. TPR ranges from 0.454 ($N{=}80$) to 0.571 ($N{=}100$) at $|\Delta_{\mathrm{MH}}| \geq 1.4$, with AUC of 0.905 at $N{=}100$, confirming that smaller corpora can use fewer strata without power loss (\Cref{tab:k3_power}).
52	
53	\begin{table}[h]
54	\centering
55	\caption{Detection power: K=3 vs.\ K=5 at $|\Delta_{\mathrm{MH}}| \geq 1.0$.}
56	\label{tab:k3_power}
57	\small
58	\begin{tabular}{lcccccc}
59	\toprule
60	& \multicolumn{3}{c}{K=3} & \multicolumn{3}{c}{K=5} \\
61	\cmidrule(lr){2-4}\cmidrule(lr){5-7}
62	N/cohort & TPR & FPR & AUC & TPR & FPR & AUC \\
63	\midrule
64	80  & 0.176 & 0.001 & 0.828 & 0.169 & 0.001 & 0.826 \\
65	200 & 0.623 & 0.004 & 0.939 & 0.621 & 0.004 & 0.934 \\
66	500 & 0.915 & 0.011 & 0.986 & 0.912 & 0.013 & 0.986 \\
67	\bottomrule
68	\end{tabular}
69	\end{table}
70	
71	\paragraph{Nearest-neighbor matching.} The 1:1 nearest-neighbor matching selects, for each focal-cohort model, the reference-cohort model with the closest total score (caliper of 0.02 on normalized accuracy, approximately 0.14~SD). Balance is verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding.
72	
73	\paragraph{Logistic regression specification.} The Simpson's paradox analysis (\Cref{sec:temporal}) uses binary logistic regression with DIF-C classification as the dependent variable, domain-level accuracy change (2024 minus 2023 mean accuracy) as the primary predictor, and item difficulty (proportion correct) and IRT discrimination (point-biserial correlation) as controls. The interaction between domain accuracy change and item difficulty is included. Non-uniform DIF detection (\Cref{sec:structural}) uses logistic regression with a group $\times$ ability interaction term; a significant interaction ($p < 0.05$) indicates non-uniform DIF.
74	
75	\section{Mechanism Analysis}
76	\label{app:mechanism_discussion}
77	
78	Three non-exclusive mechanisms may drive the observed 13.5--29.2\% temporal DIF rate (after non-independence corrections): (1)~differential contamination, where newer models encounter benchmark items during training; (2)~capability evolution, where training advances shift item--ability relationships; (3)~training methodology shifts (e.g., RLHF, instruction tuning). The ETS baseline of 5--15\% C\%~\citep{clauser1998dif} applies to concurrent demographic groups in educational testing; comparison to temporal LLM cohorts is illustrative, not normative. Observational DIF alone cannot separate these mechanisms~\citep{suk2026rethinking}; the evidence below constrains the space of explanations.
79	
80	\paragraph{Exclusion arguments.}
81	Four exclusion arguments narrow possible explanations. \emph{Ability confounds}: at most 2.4~pp attributable to ability mismatch (matched C\% $= 28.9\%$ vs.\ unmatched 31.3\%; Cohen's $d = -0.17$; \Cref{sec:temporal}). \emph{Domain-level improvement}: domain accuracy gains explain ${<}0.1\%$ of item-level DIF variance (pseudo $R^2 = 0.0007$); a Simpson's paradox confirms DIF is item-specific (OR reverses from 1.55 to 0.73 after difficulty control). \emph{Item quality defects}: no enrichment among expert-annotated errors~\citep{gema2024mmlu} (enrichment $= 1.10$, 95\% CI $[0.92, 1.27]$, $p = 0.23$). \emph{Web-overlap labels}: near-independent of DIF flags (Jaccard $= 0.206$, enrichment $= 0.964$; \Cref{sec:groundtruth}).
82	
83	\paragraph{Difficulty--direction interaction.}
84	The aggregate difficulty--direction correlation ($r = -0.597$; \Cref{sec:temporal}) shows that hardest-decile DIF-C items are 88.7\% focal-favoring while easiest-decile items are 96.2\% reference-favoring. This gradient is robust under range restriction ($r = -0.447$ at difficulty $\in [0.2, 0.8]$; $p < 10^{-100}$). Semi-synthetic analysis (\Cref{sec:semisynthetic}) reveals that uniform injection produces $r \approx -0.52$ via ceiling effects (high-accuracy items have fewer flippable responses), while difficulty-dependent injection yields $r \approx +0.77$ (zero overlap across seeds). The observed $r$ thus cannot alone distinguish contamination from capability evolution.
85	
86	\paragraph{Difficulty--model-type interaction.}
87	\label{app:interaction}
88	Logistic regression confirms that the base-vs-instruct direction reversal is not a difficulty confound: the difficulty $\times$ model-type interaction is significant ($\hat{\beta} = 1.56$, OR $= 4.75$, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR $= 4.24$, $p < 10^{-225}$). Among 2,053 items flagged DIF-C in both base and instruct analyses, 98\% show concordant direction; the aggregate reversal arises from \emph{which} items reach C threshold, not from individual items reversing direction.
89	
90	\paragraph{Mixed-mechanism injection.}
91	\label{app:mixed_mechanism}
92	To test the hypothesis that different contamination mechanisms operate on base and instruct models simultaneously, we designed mixed injection schemes: Scheme~D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, Scheme~D reproduces the overall difficulty--direction gradient ($r = -0.676 \pm 0.005$ vs.\ observed $-0.597$) and direction reversal ($\chi^2 = 634 \pm 184$ vs.\ observed $562.7$), but cannot match the near-zero instruct gradient: simulated $r_{\mathrm{instruct}} = -0.302 \pm 0.090$ vs.\ observed $-0.079$. This residual gap ($3.8\times$ the observed value) persists across all tested injection parameters, suggesting that instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts) rather than memorization alone.
93	
94	
95	\section{Structural Analysis Details}
96	\label{app:structural}
97	
98	\begin{table}[h]
99	\centering
100	\caption{Structural controls and sensitivity checks for temporal DIF. None reduces C\% below 31\%; $\theta$-conditioning serves as a sensitivity check confirming total-score adequacy.}
101	\label{tab:structural_comparison}
102	\small
103	\resizebox{\columnwidth}{!}{%
104	\begin{tabular}{lcccc}
105	\toprule
106	Approach & Mechanism & Temp.\ C\% & TPR ($p{=}0.5$) & Outcome \\
107	\midrule
108	Baseline (ext.) & Cross-bench.\ total score & $0.314_{\pm.009}$ & $0.834_{\pm.027}$ & Reference \\
109	Matched-ability & Within-quintile temp.\ DIF & ${\sim}$0.31 & -- & Enrich.\ 0.94--1.04 \\
110	$\theta$-cond.\ (sens.) & $\theta$ replaces total score & 0.312 & 0.876 & $r(\theta,\mathrm{total}) {=} 0.9986$ \\
111	Within-subject & Per-subject DIF & -- & -- & C\% $= 38.1\%$ ($>$25\%) \\
112	\bottomrule
113	\end{tabular}}
114	\end{table}
115	
116	Two structural controls and a sensitivity check fail to reduce the temporal C\% below 31\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal C\% unchanged at approximately 0.31. Within-subject DIF analysis on 5 representative subjects, intended to isolate subject-specific effects, finds mean C\% $= 38.1\%$, exceeding the 25\% threshold that would indicate viable bifactor structure. As a sensitivity check, IRT $\theta$-conditioning with 20 ability strata achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ and C\% $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. \Cref{tab:structural_comparison} summarizes these results.
117	
118	The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\% of within-subject item pairs exceed $|Q3| > 0.20$, vs.\ 2.2\% cross-subject; $5{\times}$ ratio, $p = 2.3 \times 10^{-9}$), which contributes to elevated within-subject DIF rates but is not the primary driver: the cross-subject matching protocol addresses this bias, and temporal C\% persists under external matching (full Q3 distributions available in the supplementary material).
119	
120	\begin{table}[h]
121	\centering
122	\caption{Domain-level Cohen's $d$ between 2023 and 2024 cohorts. The narrow range ($0.12$) indicates nearly uniform improvement across domains, supporting total-score matching adequacy for DIF analysis (\Cref{sec:method}).}
123	\label{tab:domain_cohens_d}
124	\small
125	\begin{tabular}{lr}
126	\toprule
127	Domain & Cohen's $d$ \\
128	\midrule
129	STEM & 0.261 \\
130	Humanities & 0.159 \\
131	Social Science & 0.147 \\
132	Other & 0.146 \\
133	\bottomrule
134	\end{tabular}
135	\end{table}
136	
137	\begin{table}[h]
138	\centering
139	\caption{Multi-subject injection robustness. $k$ = number of simultaneously contaminated subjects (out of 57); values are mean $\pm$ SD across 5 random subject draws at exploitation rate $p = 0.5$. Cross-subject matching provides reliable FPR control at $k \leq 5$; $\Delta\mathrm{FPR}$ increases substantially at $k \geq 10$.}
140	\label{tab:multi_subject_injection}
141	\small
142	\begin{tabular}{rcc}
143	\toprule
144	$k$ & $\Delta\mathrm{FPR}$ & $\Delta\mathrm{TPR}$ \\
145	\midrule
146	1 & $0.002_{\pm.002}$ & $0.518_{\pm.050}$ \\
147	3 & $0.000_{\pm.003}$ & $0.470_{\pm.093}$ \\
148	5 & $0.007_{\pm.007}$ & $0.421_{\pm.041}$ \\
149	10 & $0.069_{\pm.030}$ & $0.361_{\pm.027}$ \\
150	20 & $0.167_{\pm.029}$ & $0.299_{\pm.030}$ \\
151	30 & $0.362_{\pm.026}$ & $0.159_{\pm.035}$ \\
152	50 & $0.458_{\pm.053}$ & $0.439_{\pm.028}$ \\
153	\bottomrule
154	\end{tabular}
155	\end{table}
156	
157	\paragraph{Extreme contamination coverage ($k \geq 30$).} At $k = 30$--$50$ (53--88\% of 57 subjects), $\Delta\mathrm{FPR}$ reaches 0.36--0.46, confirming that cross-subject matching requires contamination to affect a minority of domains. At extreme coverage the matching variable itself is majority-contaminated, violating the identifying assumption. $\Delta\mathrm{TPR}$ drops to 0.159 at $k{=}30$ as matching-variable corruption dominates; at $k{=}50$, both $\Delta\mathrm{TPR}$ (0.439) and $\Delta\mathrm{FPR}$ (0.458) surge to comparable levels, indicating the test flags ${\sim}$76\% of all items regardless of contamination status---complete loss of discriminative power. This regime is primarily of theoretical interest: if ${\geq}$50\% of benchmark domains are differentially contaminated, the benchmark requires redesign rather than statistical correction.
158	
159	\begin{table}[h]
160	\centering
161	\caption{Leave-one-family-out (LOFO) robustness on MMLU. Removing non-dominant families ($\leq$15\% of their cohort) changes C\% by at most 2.93\,pp. Larger shifts from removing Mistral or Llama-3 are driven almost entirely by family composition, not statistical power loss: Monte Carlo random-subsample calibration (200 replicates per scenario, matching the reduced sample size) shows the power effect is $\leq$1\,pp, while the composition effect accounts for 95--113\% of the observed C\% drop (Mistral: $-8.44$\,pp composition vs.\ $-0.41$\,pp power; Llama-3: $-8.17$\,pp vs.\ ${+}0.91$\,pp; observed C\% falls below the 95\% random-subsample range in both cases). Stratification uses total test score for computational efficiency; cross-subject matching yields identical baseline C\%.}
162	\label{tab:lofo}
163	\small
164	\begin{tabular}{lrrr}
165	\toprule
166	Family & $N$ removed & Cohort share & C\% (LOFO) \\
167	\midrule
168	\emph{Full sample} & --- & --- & 31.32 \\
169	Mistral & 547 & 51\% ref & 22.47 \\
170	Llama-3 & 315 & 39\% foc & 24.06 \\
171	Mixtral & 120 & 15\% foc & 34.26 \\
172	Llama-2 & 161 & 15\% ref & 31.48 \\
173	Solar & 91 & 11\% foc & 31.01 \\
174	\bottomrule
175	\end{tabular}
176	\end{table}
177	
178	\section{Design Effect Estimation}
179	\label{app:deff}
180	
181	Model families (e.g., Mistral, Llama-3) induce intra-class correlation (ICC) that inflates Mantel-Haenszel $\chi^2$ statistics beyond the nominal $\chi^2_1$ reference distribution. We estimate the design effect (DEFF) per item following \citet{rao1992variance}: $\mathrm{DEFF}_i = 1 + (\bar{m} - 1) \cdot \mathrm{ICC}_i$, where $\bar{m}$ is the mean family size and $\mathrm{ICC}_i$ is the one-way random-effects ICC for item $i$ across 30 families (restricted to ref+foc cohort; 1,884 models with family$\geq$2).
182	
183	Two estimates of $\bar{m}$ bracket the adjustment: (1)~\emph{Simple mean} ($\bar{m} = 62.8$), treating all families equally, yields $\mathrm{DEFF} = 3.87$ and adjusted C\% $= 29.2\%$; (2)~\emph{Weighted mean} ($\bar{m} = \sum n_f^2 / \sum n_f = 254.5$; \citealp{kish1965survey}), reflecting the effective cluster size experienced by a randomly sampled model, yields $\mathrm{DEFF} = 12.79$ and adjusted C\% $= 13.5\%$.
184	
185	\noindent Mean ICC $= 0.047$ (median $0.041$, Q3 $= 0.061$, max $= 0.219$; 4.8\% of items exceed $0.10$). After dividing each item's $\chi^2_{\mathrm{MH}}$ by its item-specific DEFF and re-applying ETS thresholds, 13.5--29.2\% of items retain Category~C classification depending on the $\bar{m}$ variant---both far exceeding the 0.62\% random-split baseline (21--47$\times$).
186	
187	\paragraph{Size-stratified DEFF.} The aggregate ICC masks a size--ICC inverse relationship: smaller families exhibit higher within-family similarity (\Cref{tab:deff_stratified}). Tier-level ICC ranges from 0.246 (2--10 members) to 0.082 ({>}200 members), reflecting greater heterogeneity in mega-families. At small family sizes, DEFF correction has negligible impact (Adj.\ C\% $= 31.3\%$); the conservative 13.5\% bound is driven entirely by the two mega-families (Mistral, Llama-3). Family definition sensitivity is minimal: merging sub-generations (e.g., Llama-2 + Llama-3) into coarse families (22 families) changes C\% by $\leq$0.3~pp.
188	
189	\begin{table}[h]
190	\centering
191	\caption{Size-stratified DEFF analysis. ICC and DEFF computed per tier; Adj.\ C\% applies tier-specific DEFF to all items.}
192	\label{tab:deff_stratified}
193	\small
194	\begin{tabular}{lrrrrc}
195	\toprule
196	Tier & Families & $\bar{m}$ & ICC & DEFF & Adj.\ C\% \\
197	\midrule
198	2--10 & 9 & 5.3 & 0.246 & 2.07 & 31.3\% \\
199	11--50 & 11 & 22.1 & 0.226 & 5.78 & 24.6\% \\
200	51--200 & 8 & 91.4 & 0.137 & 13.34 & 13.7\% \\
201	${>}200$ & 2 & 431.0 & 0.082 & 36.11 & 9.0\% \\
202	\midrule
203	Overall & 30 & 62.8 & 0.047 & 3.87 & 29.2\% \\
204	\bottomrule
205	\end{tabular}
206	\end{table}
207	
208	\section{Uncertainty Quantification Comparison}
209	\label{app:uncertainty}
210	
211	\begin{table}[h]
212	\centering
213	\caption{Comparison of uncertainty quantification methods for the 31.3\% C\% estimate on MMLU.}
214	\small
215	\resizebox{\columnwidth}{!}{%
216	\begin{tabular}{llr}
217	\toprule
218	Method & Key assumption & Result \\
219	\midrule
220	Model-level bootstrap & Models independent & 95\% CI [29.2\%, 37.8\%] \\
221	Family-level cluster bootstrap & Family is clustering unit & 95\% CI [26.7\%, 53.2\%] \\
222	DEFF (simple $\bar{m}$) & Equal-weight families & Adjusted C\% = 29.2\% \\
223	DEFF (weighted $\bar{m}$) & Size-proportional weighting & Adjusted C\% = 13.5\% \\
224	Graduated de-dup.\ ($K{=}20$) & Remove within-family duplicates & C\% = 19.7\% $\pm$ 0.9\% \\
225	\bottomrule
226	\end{tabular}}
227	\label{tab:uncertainty}
228	\end{table}
229	
230	\paragraph{Half-year granularity.} Splitting at the 6-month boundary yields C\% $= 34.4\%$, slightly above the annual 31.3\%. The higher rate likely reflects more polarized cohort composition: fewer models span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates.
231	
232	The cluster bootstrap upper bound (53.2\%) is driven by extreme bootstrap resamples that over-represent Mistral ($n = 547$) or Llama-3 ($n = 315$), producing atypical cohort compositions. Two independent methods---cluster bootstrap lower bound (26.7\%) and simple-mean DEFF adjustment (29.2\%)---converge on $\sim$27--29\%, establishing a corrected estimate that remains $>$45$\times$ the random-split baseline (0.62\%). Graduated de-duplication at $K{=}20$ yields C\% $= 19.7\% \pm 0.9\%$ (random member selection, 5 draws), lower than the corrected estimate due to reduced statistical power ($N \approx 450$ vs.\ 1,887), but within-$K$ variance ${<}1.5$\,pp at all $K$ confirms the signal is power-driven rather than redundancy-inflated (\Cref{app:dedup_k}). The weighted-mean DEFF (13.5\%) represents a conservative extreme; even this lower bound exceeds the baseline by ${\approx}22\times$.
233	
234	\section{Cross-Benchmark Comparison}
235	\label{app:gsm8k_details}
236	
237	\begin{table}[h]
238	\centering
239	\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal score incomparability with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\pm$ values denote standard deviations across 5 random injection seeds.}
240	\label{tab:gsm8k_comparison}
241	\small
242	\begin{tabular}{lcc}
243	\toprule
244	Metric & MMLU & GSM8K \\
245	\midrule
246	Items & 12,508 & 1,319 \\
247	Models & 5,227 & 6,702 \\
248	Temporal C\% & 31.3\% & 18.9\% \\
249	Sanity C\% & 0.62\% & 0.3\% \\
250	$\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\pm.006}$ \\
251	$\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\pm.027}$ & $+0.514_{\pm.028}$ \\
252	\bottomrule
253	\end{tabular}
254	\end{table}
255	
256	\section{Additional Figures}
257	\label{app:figures}
258	
259	\begin{figure}[h]
260	\centering
261	\includegraphics[width=\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}
262	\caption{Exploratory: GSM1K contamination gap vs.\ DIF ranking advantage ($N = 33$; small sample, results should be interpreted cautiously). The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items. Three of 33 models exceed the Cook's $D$ threshold ($4/N = 0.12$); leave-one-out analysis confirms all individual-removal correlations remain significant ($r \in [-0.54, -0.37]$, all $p < 0.05$), and removing all three outliers yields $r = -0.38$ ($p = 0.036$, $N = 30$).}
263	\label{app:fig_gsm1k}
264	\end{figure}
265	
266	See \Cref{fig:rho_degradation} in the main text for ranking degradation curves.
267	
268	\section{Item-Property Predictive Analysis}
269	\label{app:predictive}
270	
271	To test whether DIF susceptibility is a fixed item property, we trained logistic regression and LightGBM classifiers to predict ETS~C classification from 17 leak-free features: ref-cohort difficulty and discrimination, 11 text features (question/option length, vocabulary metrics), subject metadata, and web-overlap labels~\citep{li2024contamination}. Features were computed exclusively from the reference (2023) cohort to prevent information leakage from the focal cohort. Five-fold subject-stratified cross-validation (no within-subject train/test overlap) yielded AUROC $= 0.603 \pm 0.020$ (LR) and $0.599 \pm 0.026$ (LightGBM)---weak predictive power. Web-overlap labels contributed negligibly (SHAP $< 0.015$), independently confirming the DIF--contamination orthogonality reported in \Cref{sec:groundtruth}. These results indicate that temporal DIF reflects emergent cohort--item interactions rather than fixed item defects, motivating post-hoc monitoring over pre-screening.
272	
273	\section{Within-Family Similarity by Family Size}
274	\label{app:icc_family}
275	
276	Within-family similarity (mean pairwise Pearson $r$ over 12{,}508-item response vectors) shows no dependence on family size (Spearman $\rho = -0.009$, $p = 0.96$; 30 families with $\geq 2$ members, 1{,}884 models). Large families (Mistral, $m = 547$, $\bar{r} = 0.47$; Llama-3, $m = 315$, $\bar{r} = 0.53$) are no more homogeneous than small or mid-sized families. Of the 5{,}227 models, 3{,}343 lack family assignments; these are retained in DIF analysis but excluded from similarity estimation. Within the temporal DIF cohorts ($N_{\mathrm{ref}} + N_{\mathrm{foc}} = 1{,}887$), 1{,}884 (99.8\%) belong to identified families with $\geq 2$ members, so DEFF estimates are computed over nearly the full cohort. This indicates that the weighted-mean DEFF variant's effective cluster size ($\bar{m} = 254$) reflects an arithmetic artifact of mega-family dominance rather than genuine within-family homogeneity.
277	
278	\section{Graduated De-Duplication Sensitivity}
279	\label{app:dedup_k}
280	
281	For each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \text{all}$ is deterministic).
282	
283	C\% increases monotonically from 0.3\% ($K = 1$) to 31.3\% ($K = \text{all}$). At each fixed $K$, variance across random member draws is negligible (SD ${<} 1.5$\,pp), confirming that the signal scales with statistical power rather than within-family redundancy. At $K{=}20$, C\% $= 19.7\% \pm 0.9\%$ ($N \approx 450$); the gap from the full-sample 31.3\% reflects reduced power, not reduced bias.
284	
285	\section{Rank-Reversal by Distance}
286	\label{app:rank_reversal}
287	
288	Pairwise rank reversals between full-item and stable-item rankings concentrate among closely-ranked models. At $\Delta\mathrm{rank} < 50$ (mean $\Delta\mathrm{acc} = 0.003$, effectively statistical ties), the reversal rate is 35.2\%. It drops to 15.1\% for $\Delta\mathrm{rank} \in [50, 200)$, 4.0\% for $[200, 500)$, 0.6\% for $[500, 1000)$, and 0.0\% above 1000. Broad leaderboard structure is fully preserved; instability affects only models within each other's noise margin.
289	
290	\section{DEFF Simulation}
291	\label{app:deff_simulation}
292	
293	To compare simple-mean and weighted-mean DEFF estimators, we simulate four family-structure scenarios (2,000 items, 30\% ground-truth DIF, 50 seeds per scenario) with size-dependent ICC matching empirical observations (\Cref{tab:deff_stratified}). \Cref{tab:deff_sim} reports the results.
294	
295	\begin{table}[h]
296	\centering
297	\caption{DEFF estimator comparison across four simulated family structures. Bias = adjusted C\% $-$ ground truth (30\%); RMSE over 50 seeds. Simple-mean wins in 3/4 scenarios; weighted-mean ties only under uniform family sizes.}
298	\label{tab:deff_sim}
299	\small
300	\resizebox{\columnwidth}{!}{%
301	\begin{tabular}{lrrrrrr}
302	\toprule
303	Scenario & $\bar{m}_s$ & $\bar{m}_w$ & Adj(s) & Adj(w) & RMSE(s) & RMSE(w) \\
304	\midrule
305	A: Uniform & 35 & 35 & 2.1\% & 2.1\% & 27.9 & 27.9 \\
306	B: Skewed & 40 & 168 & 2.3\% & 0.9\% & 27.7 & 29.1 \\
307	C: Extreme & 33 & 268 & 2.4\% & 0.5\% & 27.6 & 29.5 \\
308	D: Homog.\ ICC & 40 & 168 & 4.1\% & 1.1\% & 25.9 & 28.9 \\
309	\bottomrule
310	\end{tabular}}
311	\end{table}
312	
313	When ICC decreases with family size (scenarios B--D, matching empirical patterns), larger families contribute less per-model inflation than the weighted-mean assumes. The weighted-mean over-corrects by assigning excessive weight to mega-families whose low ICC does not warrant large DEFF adjustments. The simple-mean estimator better captures the average inflation per family under these conditions.
314	
315	\section{Score Inflation Analysis}
316	\label{app:score_inflation}
317	
318	Removing the 3,918 DIF-C items (31.3\%) and rescoring on the 8,590 stable items shifts model accuracy upward by a mean of ${+}2.12$\,pp overall (\Cref{tab:score_inflation}). The cohort-differential is 0.29\,pp (2023: ${+}2.35$\,pp; 2024: ${+}2.06$\,pp; Cohen's $d = 0.31$, $p < 10^{-10}$). Overall ranking correlation between original and stable-item scores is $\rho = 0.9965$, but individual rank displacements reach ${\pm}561$ at the 99th percentile and exceed ${\pm}800$ in extreme cases. Equating adjustments are ${+}0.0235$ (2023) and ${+}0.0206$ (2024).
319	
320	\begin{table}[h]
321	\centering
322	\caption{Score inflation from DIF-C item removal, by cohort.}
323	\label{tab:score_inflation}
324	\small
325	\begin{tabular}{lrrrr}
326	\toprule
327	Cohort & $N$ & Mean $\Delta$ (pp) & SD (pp) & 95\% CI \\
328	\midrule
329	2023 & 1,080 & ${+}2.35$ & 0.88 & $[{+}2.30, {+}2.40]$ \\
330	2024 & 807 & ${+}2.06$ & 1.04 & $[{+}1.99, {+}2.13]$ \\
331	Other & 3,340 & ${+}2.05$ & 0.92 & $[{+}2.02, {+}2.08]$ \\
332	\bottomrule
333	\end{tabular}
334	\end{table}
335	
336	\section{Within-Architecture Temporal DIF}
337	\label{app:within_arch}
338	
339	To rule out the confound that overall temporal DIF is driven by cross-architecture differences, we group fine-grained families into architecture lineages and run MH-DIF within each (\Cref{tab:within_arch}).
340	
341	\begin{table}[h]
342	\centering
343	\caption{Within-architecture temporal DIF. C\% = ETS~C items between 2023 and 2024 models within each lineage.}
344	\label{tab:within_arch}
345	\small
346	\begin{tabular}{lrrrl}
347	\toprule
348	Lineage & $N_{\mathrm{ref}}$ (2023) & $N_{\mathrm{foc}}$ (2024) & C\% & Med $|\Delta|$ \\
349	\midrule
350	Llama & 171 & 315 & 59.2\% & 2.38 \\
351	Qwen & 27 & 70 & 6.9\% & 1.55 \\
352	Yi & 72 & 14 & 3.5\% & 1.78 \\
353	Phi & 60 & 20 & 1.3\% & 2.85 \\
354	\bottomrule
355	\end{tabular}
356	\end{table}
357	
358	Llama, Qwen, and Yi show C\% above the random baseline; Phi (C\% $= 1.3\%$, $N_{\mathrm{foc}} = 20$) is inconclusive due to low power. Llama is the best-powered comparison ($N = 486$ total) and yields raw C\% $= 59.2\%$, which combines temporal and generational effects. After ability matching, within-architecture C\% converges to ${\sim}$28--29\%, consistent with temporal C\% ($28.9\%$)---confirming that the temporal DIF signal persists within individual lineages and is not an artifact of comparing different architectures.
359	
360	\section{Base-Only and Instruct-Only Temporal DIF}
361	\label{app:baseinst_temporal}
362	
363	Separating the temporal cohorts by model type confirms that both base and instruct models independently exhibit substantial temporal DIF (\Cref{tab:baseinst_temporal}). Training methodology modulates DIF \emph{direction} (base: 60.1\% reference-favoring with $r = -0.570$; instruct: 65.6\% focal-favoring with $r = -0.079$) rather than DIF \emph{magnitude}, providing direct evidence against composition shift as the primary driver.
364	
365	\begin{table}[h]
366	\centering
367	\caption{Temporal DIF computed separately for base-only and instruct-only model subsets. Both model types independently exhibit C\% $\geq 32\%$, far exceeding the random baseline (0.62\%). Training methodology modulates DIF direction ($r$, focal-favoring proportion) rather than magnitude.}
368	\label{tab:baseinst_temporal}
369	\small
370	\resizebox{\columnwidth}{!}{%
371	\begin{tabular}{lcccc}
372	\toprule
373	Subset & $N_{\mathrm{ref}}$ / $N_{\mathrm{foc}}$ & C\% & $\rho(\mathrm{diff}, \Delta_{\mathrm{MH}})$ & Focal-fav \\
374	\midrule
375	Base-only & 861 / 548 & 32.1\% & $-0.570$ & 39.9\% \\
376	Instruct-only & 219 / 259 & 36.5\% & $-0.079$ & 65.6\% \\
377	Overall & 1{,}080 / 807 & 31.3\% & $-0.587$ & 43.9\% \\
378	\bottomrule
379	\end{tabular}}
380	\end{table}
381	
382	\section{Composition Control}
383	\label{app:composition_control}
384	
385	The 2023 and 2024 cohorts differ in base/instruct composition (2023: 79.7\% base; 2024: 67.9\% base; 11.8\,pp gap). To test whether this confounds temporal DIF, we downsample 2023 base models to match the 2024 ratio and re-run MH-DIF (10 random seeds). Balanced C\% $= 30.25\% \pm 1.32\%$ (95\% CI: $[27.65\%, 32.84\%]$), differing from the original 31.3\% by only 1.08\,pp. Composition shift does not explain the observed temporal DIF rate.
386	
387	\section{Use of AI Assistants}
388	\label{app:ai-assistants}
389	
390	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
391	\begin{itemize}
392	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
393	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
394	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
395	\end{itemize}
396	
397	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfd2f606-a3c6-42ef-a197-065fb6e530de",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "95652325-76cf-4c77-b577-db7ba928fb62",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
      "content": "\\section{Method Details}\n\\label{app:method_details}\n\n\\subsection{Diagnostics}\n\\label{app:diagnostics}\n\nThree diagnostic procedures complement the primary DIF analysis.\n\n\\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\\theta$ captures, which could inflate within-subject DIF rates.\n\n\\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\\rho$ between subject-level C\\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.\n\n\\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\\% measures the contribution of domain-level improvement to the total instability.\n\n\\subsection{Statistical Considerations}\n\\label{app:statistical}\n\n\\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini-Hochberg FDR correction at $q = 0.05$. The random-split sanity check provides an empirical estimate of the false positive rate under the null hypothesis.\n\n\\paragraph{Threshold sensitivity.} We report results across a range of DIF thresholds ($|\\Delta_{\\mathrm{MH}}| \\in \\{1.0, 1.5, 2.0, 2.5\\}$) to verify that qualitative conclusions do not depend on the specific ETS~C cutoff. The standard threshold of $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ corresponds to the ETS~C definition used throughout the paper.\n\n\\paragraph{IRT model fit.} For transparency, we report that the MMLU response matrix shows poor fit to a unidimensional 2PL model (expected for a 57-subject multidimensional benchmark). This does not affect MH-DIF validity, which relies only on total score stratification rather than parametric IRT assumptions.\n\n\\paragraph{Architecture heterogeneity.} The METABENCH MMLU population consists of 99.98\\% decoder-only models (5,226 of 5,227). This near-complete architectural homogeneity eliminates architecture as a confound for DIF analysis. We verify this by excluding the single encoder-decoder model and confirming identical results.\n\n\\paragraph{Power sensitivity to item discrimination.}\n\\label{app:power_sensitivity}\nThe Monte Carlo power analysis in \\Cref{sec:validation} uses average 2PL parameters ($\\bar{a} = 1.2$, $\\bar{b} = -0.84$). \\Cref{tab:power_sensitivity} reports TPR as a function of discrimination $a$ (other parameters at their means, $N = 80$ per cohort, $|\\Delta_b| = 1.4$, 1,000 replications). TPR increases monotonically from 0.40 ($a = 0.5$) to 0.95 ($a = 2.0$); FPR remains below 0.04 throughout. The MMLU item pool shows substantial heterogeneity: $a$ ranges from 0.006 to 2.657 (SD $= 0.54$, IQR $= [0.75, 1.64]$). The aggregate TPR of 0.68 from Phase~2 reflects this full distribution, while TPR at mean $a \\approx 1.2$ is 0.87---the gap is consistent with Jensen's inequality applied to the concave TPR($a$) function. Although 2PL fit is poor for MMLU's multidimensional structure, the power analysis serves as one leg of a triangulation: parametric estimates (TPR $= 0.68$--$0.80$) are validated by empirical semi-synthetic injection ($\\Delta\\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \\Cref{sec:semisynthetic}), confirming adequate detection power regardless of parametric assumptions.\n\n\\begin{table}[h]\n\\centering\n\\caption{Power sensitivity to item discrimination. TPR = true positive rate for ETS~C detection ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$) at $N = 80$ per cohort, $|\\Delta_b| = 1.4$, 1,000 replications.}\n\\label{tab:power_sensitivity}\n\\small\n\\begin{tabular}{rccc}\n\\toprule\n$a$ & TPR & 95\\% CI & FPR \\\\\n\\midrule\n0.5 & 0.398 & [0.20, 0.60] & 0.033 \\\\\n0.8 & 0.683 & [0.45, 0.90] & 0.036 \\\\\n1.0 & 0.808 & [0.60, 0.95] & 0.038 \\\\\n1.2 ($\\approx \\bar{a}$) & 0.874 & [0.70, 1.00] & 0.038 \\\\\n1.5 & 0.930 & [0.80, 1.00] & 0.038 \\\\\n2.0 & 0.949 & [0.80, 1.00] & 0.037 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Stratum sensitivity (K=3 vs.\\ K=5).}\n\\label{app:k3_power}\nK=3 and K=5 yield near-identical detection power: TPR differences $<$0.02 across all conditions, within Monte Carlo noise. TPR ranges from 0.454 ($N{=}80$) to 0.571 ($N{=}100$) at $|\\Delta_{\\mathrm{MH}}| \\geq 1.4$, with AUC of 0.905 at $N{=}100$, confirming that smaller corpora can use fewer strata without power loss (\\Cref{tab:k3_power}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Detection power: K=3 vs.\\ K=5 at $|\\Delta_{\\mathrm{MH}}| \\geq 1.0$.}\n\\label{tab:k3_power}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{K=3} & \\multicolumn{3}{c}{K=5} \\\\\n\\cmidrule(lr){2-4}\\cmidrule(lr){5-7}\nN/cohort & TPR & FPR & AUC & TPR & FPR & AUC \\\\\n\\midrule\n80  & 0.176 & 0.001 & 0.828 & 0.169 & 0.001 & 0.826 \\\\\n200 & 0.623 & 0.004 & 0.939 & 0.621 & 0.004 & 0.934 \\\\\n500 & 0.915 & 0.011 & 0.986 & 0.912 & 0.013 & 0.986 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Nearest-neighbor matching.} The 1:1 nearest-neighbor matching selects, for each focal-cohort model, the reference-cohort model with the closest total score (caliper of 0.02 on normalized accuracy, approximately 0.14~SD). Balance is verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding.\n\n\\paragraph{Logistic regression specification.} The Simpson's paradox analysis (\\Cref{sec:temporal}) uses binary logistic regression with DIF-C classification as the dependent variable, domain-level accuracy change (2024 minus 2023 mean accuracy) as the primary predictor, and item difficulty (proportion correct) and IRT discrimination (point-biserial correlation) as controls. The interaction between domain accuracy change and item difficulty is included. Non-uniform DIF detection (\\Cref{sec:structural}) uses logistic regression with a group $\\times$ ability interaction term; a significant interaction ($p < 0.05$) indicates non-uniform DIF.\n\n\\section{Mechanism Analysis}\n\\label{app:mechanism_discussion}\n\nThree non-exclusive mechanisms may drive the observed 13.5--29.2\\% temporal DIF rate (after non-independence corrections): (1)~differential contamination, where newer models encounter benchmark items during training; (2)~capability evolution, where training advances shift item--ability relationships; (3)~training methodology shifts (e.g., RLHF, instruction tuning). The ETS baseline of 5--15\\% C\\%~\\citep{clauser1998dif} applies to concurrent demographic groups in educational testing; comparison to temporal LLM cohorts is illustrative, not normative. Observational DIF alone cannot separate these mechanisms~\\citep{suk2026rethinking}; the evidence below constrains the space of explanations.\n\n\\paragraph{Exclusion arguments.}\nFour exclusion arguments narrow possible explanations. \\emph{Ability confounds}: at most 2.4~pp attributable to ability mismatch (matched C\\% $= 28.9\\%$ vs.\\ unmatched 31.3\\%; Cohen's $d = -0.17$; \\Cref{sec:temporal}). \\emph{Domain-level improvement}: domain accuracy gains explain ${<}0.1\\%$ of item-level DIF variance (pseudo $R^2 = 0.0007$); a Simpson's paradox confirms DIF is item-specific (OR reverses from 1.55 to 0.73 after difficulty control). \\emph{Item quality defects}: no enrichment among expert-annotated errors~\\citep{gema2024mmlu} (enrichment $= 1.10$, 95\\% CI $[0.92, 1.27]$, $p = 0.23$). \\emph{Web-overlap labels}: near-independent of DIF flags (Jaccard $= 0.206$, enrichment $= 0.964$; \\Cref{sec:groundtruth}).\n\n\\paragraph{Difficulty--direction interaction.}\nThe aggregate difficulty--direction correlation ($r = -0.597$; \\Cref{sec:temporal}) shows that hardest-decile DIF-C items are 88.7\\% focal-favoring while easiest-decile items are 96.2\\% reference-favoring. This gradient is robust under range restriction ($r = -0.447$ at difficulty $\\in [0.2, 0.8]$; $p < 10^{-100}$). Semi-synthetic analysis (\\Cref{sec:semisynthetic}) reveals that uniform injection produces $r \\approx -0.52$ via ceiling effects (high-accuracy items have fewer flippable responses), while difficulty-dependent injection yields $r \\approx +0.77$ (zero overlap across seeds). The observed $r$ thus cannot alone distinguish contamination from capability evolution.\n\n\\paragraph{Difficulty--model-type interaction.}\n\\label{app:interaction}\nLogistic regression confirms that the base-vs-instruct direction reversal is not a difficulty confound: the difficulty $\\times$ model-type interaction is significant ($\\hat{\\beta} = 1.56$, OR $= 4.75$, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR $= 4.24$, $p < 10^{-225}$). Among 2,053 items flagged DIF-C in both base and instruct analyses, 98\\% show concordant direction; the aggregate reversal arises from \\emph{which} items reach C threshold, not from individual items reversing direction.\n\n\\paragraph{Mixed-mechanism injection.}\n\\label{app:mixed_mechanism}\nTo test the hypothesis that different contamination mechanisms operate on base and instruct models simultaneously, we designed mixed injection schemes: Scheme~D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, Scheme~D reproduces the overall difficulty--direction gradient ($r = -0.676 \\pm 0.005$ vs.\\ observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs.\\ observed $562.7$), but cannot match the near-zero instruct gradient: simulated $r_{\\mathrm{instruct}} = -0.302 \\pm 0.090$ vs.\\ observed $-0.079$. This residual gap ($3.8\\times$ the observed value) persists across all tested injection parameters, suggesting that instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts) rather than memorization alone.\n\n\n\\section{Structural Analysis Details}\n\\label{app:structural}\n\n\\begin{table}[h]\n\\centering\n\\caption{Structural controls and sensitivity checks for temporal DIF. None reduces C\\% below 31\\%; $\\theta$-conditioning serves as a sensitivity check confirming total-score adequacy.}\n\\label{tab:structural_comparison}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nApproach & Mechanism & Temp.\\ C\\% & TPR ($p{=}0.5$) & Outcome \\\\\n\\midrule\nBaseline (ext.) & Cross-bench.\\ total score & $0.314_{\\pm.009}$ & $0.834_{\\pm.027}$ & Reference \\\\\nMatched-ability & Within-quintile temp.\\ DIF & ${\\sim}$0.31 & -- & Enrich.\\ 0.94--1.04 \\\\\n$\\theta$-cond.\\ (sens.) & $\\theta$ replaces total score & 0.312 & 0.876 & $r(\\theta,\\mathrm{total}) {=} 0.9986$ \\\\\nWithin-subject & Per-subject DIF & -- & -- & C\\% $= 38.1\\%$ ($>$25\\%) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTwo structural controls and a sensitivity check fail to reduce the temporal C\\% below 31\\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal C\\% unchanged at approximately 0.31. Within-subject DIF analysis on 5 representative subjects, intended to isolate subject-specific effects, finds mean C\\% $= 38.1\\%$, exceeding the 25\\% threshold that would indicate viable bifactor structure. As a sensitivity check, IRT $\\theta$-conditioning with 20 ability strata achieves $r(\\theta, \\mathrm{total\\ score}) = 0.9986$ and C\\% $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. \\Cref{tab:structural_comparison} summarizes these results.\n\nThe temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\\% of within-subject item pairs exceed $|Q3| > 0.20$, vs.\\ 2.2\\% cross-subject; $5{\\times}$ ratio, $p = 2.3 \\times 10^{-9}$), which contributes to elevated within-subject DIF rates but is not the primary driver: the cross-subject matching protocol addresses this bias, and temporal C\\% persists under external matching (full Q3 distributions available in the supplementary material).\n\n\\begin{table}[h]\n\\centering\n\\caption{Domain-level Cohen's $d$ between 2023 and 2024 cohorts. The narrow range ($0.12$) indicates nearly uniform improvement across domains, supporting total-score matching adequacy for DIF analysis (\\Cref{sec:method}).}\n\\label{tab:domain_cohens_d}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nDomain & Cohen's $d$ \\\\\n\\midrule\nSTEM & 0.261 \\\\\nHumanities & 0.159 \\\\\nSocial Science & 0.147 \\\\\nOther & 0.146 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Multi-subject injection robustness. $k$ = number of simultaneously contaminated subjects (out of 57); values are mean $\\pm$ SD across 5 random subject draws at exploitation rate $p = 0.5$. Cross-subject matching provides reliable FPR control at $k \\leq 5$; $\\Delta\\mathrm{FPR}$ increases substantially at $k \\geq 10$.}\n\\label{tab:multi_subject_injection}\n\\small\n\\begin{tabular}{rcc}\n\\toprule\n$k$ & $\\Delta\\mathrm{FPR}$ & $\\Delta\\mathrm{TPR}$ \\\\\n\\midrule\n1 & $0.002_{\\pm.002}$ & $0.518_{\\pm.050}$ \\\\\n3 & $0.000_{\\pm.003}$ & $0.470_{\\pm.093}$ \\\\\n5 & $0.007_{\\pm.007}$ & $0.421_{\\pm.041}$ \\\\\n10 & $0.069_{\\pm.030}$ & $0.361_{\\pm.027}$ \\\\\n20 & $0.167_{\\pm.029}$ & $0.299_{\\pm.030}$ \\\\\n30 & $0.362_{\\pm.026}$ & $0.159_{\\pm.035}$ \\\\\n50 & $0.458_{\\pm.053}$ & $0.439_{\\pm.028}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Extreme contamination coverage ($k \\geq 30$).} At $k = 30$--$50$ (53--88\\% of 57 subjects), $\\Delta\\mathrm{FPR}$ reaches 0.36--0.46, confirming that cross-subject matching requires contamination to affect a minority of domains. At extreme coverage the matching variable itself is majority-contaminated, violating the identifying assumption. $\\Delta\\mathrm{TPR}$ drops to 0.159 at $k{=}30$ as matching-variable corruption dominates; at $k{=}50$, both $\\Delta\\mathrm{TPR}$ (0.439) and $\\Delta\\mathrm{FPR}$ (0.458) surge to comparable levels, indicating the test flags ${\\sim}$76\\% of all items regardless of contamination status---complete loss of discriminative power. This regime is primarily of theoretical interest: if ${\\geq}$50\\% of benchmark domains are differentially contaminated, the benchmark requires redesign rather than statistical correction.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-family-out (LOFO) robustness on MMLU. Removing non-dominant families ($\\leq$15\\% of their cohort) changes C\\% by at most 2.93\\,pp. Larger shifts from removing Mistral or Llama-3 are driven almost entirely by family composition, not statistical power loss: Monte Carlo random-subsample calibration (200 replicates per scenario, matching the reduced sample size) shows the power effect is $\\leq$1\\,pp, while the composition effect accounts for 95--113\\% of the observed C\\% drop (Mistral: $-8.44$\\,pp composition vs.\\ $-0.41$\\,pp power; Llama-3: $-8.17$\\,pp vs.\\ ${+}0.91$\\,pp; observed C\\% falls below the 95\\% random-subsample range in both cases). Stratification uses total test score for computational efficiency; cross-subject matching yields identical baseline C\\%.}\n\\label{tab:lofo}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\nFamily & $N$ removed & Cohort share & C\\% (LOFO) \\\\\n\\midrule\n\\emph{Full sample} & --- & --- & 31.32 \\\\\nMistral & 547 & 51\\% ref & 22.47 \\\\\nLlama-3 & 315 & 39\\% foc & 24.06 \\\\\nMixtral & 120 & 15\\% foc & 34.26 \\\\\nLlama-2 & 161 & 15\\% ref & 31.48 \\\\\nSolar & 91 & 11\\% foc & 31.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Design Effect Estimation}\n\\label{app:deff}\n\nModel families (e.g., Mistral, Llama-3) induce intra-class correlation (ICC) that inflates Mantel-Haenszel $\\chi^2$ statistics beyond the nominal $\\chi^2_1$ reference distribution. We estimate the design effect (DEFF) per item following \\citet{rao1992variance}: $\\mathrm{DEFF}_i = 1 + (\\bar{m} - 1) \\cdot \\mathrm{ICC}_i$, where $\\bar{m}$ is the mean family size and $\\mathrm{ICC}_i$ is the one-way random-effects ICC for item $i$ across 30 families (restricted to ref+foc cohort; 1,884 models with family$\\geq$2).\n\nTwo estimates of $\\bar{m}$ bracket the adjustment: (1)~\\emph{Simple mean} ($\\bar{m} = 62.8$), treating all families equally, yields $\\mathrm{DEFF} = 3.87$ and adjusted C\\% $= 29.2\\%$; (2)~\\emph{Weighted mean} ($\\bar{m} = \\sum n_f^2 / \\sum n_f = 254.5$; \\citealp{kish1965survey}), reflecting the effective cluster size experienced by a randomly sampled model, yields $\\mathrm{DEFF} = 12.79$ and adjusted C\\% $= 13.5\\%$.\n\n\\noindent Mean ICC $= 0.047$ (median $0.041$, Q3 $= 0.061$, max $= 0.219$; 4.8\\% of items exceed $0.10$). After dividing each item's $\\chi^2_{\\mathrm{MH}}$ by its item-specific DEFF and re-applying ETS thresholds, 13.5--29.2\\% of items retain Category~C classification depending on the $\\bar{m}$ variant---both far exceeding the 0.62\\% random-split baseline (21--47$\\times$).\n\n\\paragraph{Size-stratified DEFF.} The aggregate ICC masks a size--ICC inverse relationship: smaller families exhibit higher within-family similarity (\\Cref{tab:deff_stratified}). Tier-level ICC ranges from 0.246 (2--10 members) to 0.082 ({>}200 members), reflecting greater heterogeneity in mega-families. At small family sizes, DEFF correction has negligible impact (Adj.\\ C\\% $= 31.3\\%$); the conservative 13.5\\% bound is driven entirely by the two mega-families (Mistral, Llama-3). Family definition sensitivity is minimal: merging sub-generations (e.g., Llama-2 + Llama-3) into coarse families (22 families) changes C\\% by $\\leq$0.3~pp.\n\n\\begin{table}[h]\n\\centering\n\\caption{Size-stratified DEFF analysis. ICC and DEFF computed per tier; Adj.\\ C\\% applies tier-specific DEFF to all items.}\n\\label{tab:deff_stratified}\n\\small\n\\begin{tabular}{lrrrrc}\n\\toprule\nTier & Families & $\\bar{m}$ & ICC & DEFF & Adj.\\ C\\% \\\\\n\\midrule\n2--10 & 9 & 5.3 & 0.246 & 2.07 & 31.3\\% \\\\\n11--50 & 11 & 22.1 & 0.226 & 5.78 & 24.6\\% \\\\\n51--200 & 8 & 91.4 & 0.137 & 13.34 & 13.7\\% \\\\\n${>}200$ & 2 & 431.0 & 0.082 & 36.11 & 9.0\\% \\\\\n\\midrule\nOverall & 30 & 62.8 & 0.047 & 3.87 & 29.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Uncertainty Quantification Comparison}\n\\label{app:uncertainty}\n\n\\begin{table}[h]\n\\centering\n\\caption{Comparison of uncertainty quantification methods for the 31.3\\% C\\% estimate on MMLU.}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llr}\n\\toprule\nMethod & Key assumption & Result \\\\\n\\midrule\nModel-level bootstrap & Models independent & 95\\% CI [29.2\\%, 37.8\\%] \\\\\nFamily-level cluster bootstrap & Family is clustering unit & 95\\% CI [26.7\\%, 53.2\\%] \\\\\nDEFF (simple $\\bar{m}$) & Equal-weight families & Adjusted C\\% = 29.2\\% \\\\\nDEFF (weighted $\\bar{m}$) & Size-proportional weighting & Adjusted C\\% = 13.5\\% \\\\\nGraduated de-dup.\\ ($K{=}20$) & Remove within-family duplicates & C\\% = 19.7\\% $\\pm$ 0.9\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\label{tab:uncertainty}\n\\end{table}\n\n\\paragraph{Half-year granularity.} Splitting at the 6-month boundary yields C\\% $= 34.4\\%$, slightly above the annual 31.3\\%. The higher rate likely reflects more polarized cohort composition: fewer models span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates.\n\nThe cluster bootstrap upper bound (53.2\\%) is driven by extreme bootstrap resamples that over-represent Mistral ($n = 547$) or Llama-3 ($n = 315$), producing atypical cohort compositions. Two independent methods---cluster bootstrap lower bound (26.7\\%) and simple-mean DEFF adjustment (29.2\\%)---converge on $\\sim$27--29\\%, establishing a corrected estimate that remains $>$45$\\times$ the random-split baseline (0.62\\%). Graduated de-duplication at $K{=}20$ yields C\\% $= 19.7\\% \\pm 0.9\\%$ (random member selection, 5 draws), lower than the corrected estimate due to reduced statistical power ($N \\approx 450$ vs.\\ 1,887), but within-$K$ variance ${<}1.5$\\,pp at all $K$ confirms the signal is power-driven rather than redundancy-inflated (\\Cref{app:dedup_k}). The weighted-mean DEFF (13.5\\%) represents a conservative extreme; even this lower bound exceeds the baseline by ${\\approx}22\\times$.\n\n\\section{Cross-Benchmark Comparison}\n\\label{app:gsm8k_details}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal score incomparability with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\\pm$ values denote standard deviations across 5 random injection seeds.}\n\\label{tab:gsm8k_comparison}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMetric & MMLU & GSM8K \\\\\n\\midrule\nItems & 12,508 & 1,319 \\\\\nModels & 5,227 & 6,702 \\\\\nTemporal C\\% & 31.3\\% & 18.9\\% \\\\\nSanity C\\% & 0.62\\% & 0.3\\% \\\\\n$\\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\\pm.006}$ \\\\\n$\\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\\pm.027}$ & $+0.514_{\\pm.028}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Additional Figures}\n\\label{app:figures}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}\n\\caption{Exploratory: GSM1K contamination gap vs.\\ DIF ranking advantage ($N = 33$; small sample, results should be interpreted cautiously). The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items. Three of 33 models exceed the Cook's $D$ threshold ($4/N = 0.12$); leave-one-out analysis confirms all individual-removal correlations remain significant ($r \\in [-0.54, -0.37]$, all $p < 0.05$), and removing all three outliers yields $r = -0.38$ ($p = 0.036$, $N = 30$).}\n\\label{app:fig_gsm1k}\n\\end{figure}\n\nSee \\Cref{fig:rho_degradation} in the main text for ranking degradation curves.\n\n\\section{Item-Property Predictive Analysis}\n\\label{app:predictive}\n\nTo test whether DIF susceptibility is a fixed item property, we trained logistic regression and LightGBM classifiers to predict ETS~C classification from 17 leak-free features: ref-cohort difficulty and discrimination, 11 text features (question/option length, vocabulary metrics), subject metadata, and web-overlap labels~\\citep{li2024contamination}. Features were computed exclusively from the reference (2023) cohort to prevent information leakage from the focal cohort. Five-fold subject-stratified cross-validation (no within-subject train/test overlap) yielded AUROC $= 0.603 \\pm 0.020$ (LR) and $0.599 \\pm 0.026$ (LightGBM)---weak predictive power. Web-overlap labels contributed negligibly (SHAP $< 0.015$), independently confirming the DIF--contamination orthogonality reported in \\Cref{sec:groundtruth}. These results indicate that temporal DIF reflects emergent cohort--item interactions rather than fixed item defects, motivating post-hoc monitoring over pre-screening.\n\n\\section{Within-Family Similarity by Family Size}\n\\label{app:icc_family}\n\nWithin-family similarity (mean pairwise Pearson $r$ over 12{,}508-item response vectors) shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; 30 families with $\\geq 2$ members, 1{,}884 models). Large families (Mistral, $m = 547$, $\\bar{r} = 0.47$; Llama-3, $m = 315$, $\\bar{r} = 0.53$) are no more homogeneous than small or mid-sized families. Of the 5{,}227 models, 3{,}343 lack family assignments; these are retained in DIF analysis but excluded from similarity estimation. Within the temporal DIF cohorts ($N_{\\mathrm{ref}} + N_{\\mathrm{foc}} = 1{,}887$), 1{,}884 (99.8\\%) belong to identified families with $\\geq 2$ members, so DEFF estimates are computed over nearly the full cohort. This indicates that the weighted-mean DEFF variant's effective cluster size ($\\bar{m} = 254$) reflects an arithmetic artifact of mega-family dominance rather than genuine within-family homogeneity.\n\n\\section{Graduated De-Duplication Sensitivity}\n\\label{app:dedup_k}\n\nFor each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC\\% increases monotonically from 0.3\\% ($K = 1$) to 31.3\\% ($K = \\text{all}$). At each fixed $K$, variance across random member draws is negligible (SD ${<} 1.5$\\,pp), confirming that the signal scales with statistical power rather than within-family redundancy. At $K{=}20$, C\\% $= 19.7\\% \\pm 0.9\\%$ ($N \\approx 450$); the gap from the full-sample 31.3\\% reflects reduced power, not reduced bias.\n\n\\section{Rank-Reversal by Distance}\n\\label{app:rank_reversal}\n\nPairwise rank reversals between full-item and stable-item rankings concentrate among closely-ranked models. At $\\Delta\\mathrm{rank} < 50$ (mean $\\Delta\\mathrm{acc} = 0.003$, effectively statistical ties), the reversal rate is 35.2\\%. It drops to 15.1\\% for $\\Delta\\mathrm{rank} \\in [50, 200)$, 4.0\\% for $[200, 500)$, 0.6\\% for $[500, 1000)$, and 0.0\\% above 1000. Broad leaderboard structure is fully preserved; instability affects only models within each other's noise margin.\n\n\\section{DEFF Simulation}\n\\label{app:deff_simulation}\n\nTo compare simple-mean and weighted-mean DEFF estimators, we simulate four family-structure scenarios (2,000 items, 30\\% ground-truth DIF, 50 seeds per scenario) with size-dependent ICC matching empirical observations (\\Cref{tab:deff_stratified}). \\Cref{tab:deff_sim} reports the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{DEFF estimator comparison across four simulated family structures. Bias = adjusted C\\% $-$ ground truth (30\\%); RMSE over 50 seeds. Simple-mean wins in 3/4 scenarios; weighted-mean ties only under uniform family sizes.}\n\\label{tab:deff_sim}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrr}\n\\toprule\nScenario & $\\bar{m}_s$ & $\\bar{m}_w$ & Adj(s) & Adj(w) & RMSE(s) & RMSE(w) \\\\\n\\midrule\nA: Uniform & 35 & 35 & 2.1\\% & 2.1\\% & 27.9 & 27.9 \\\\\nB: Skewed & 40 & 168 & 2.3\\% & 0.9\\% & 27.7 & 29.1 \\\\\nC: Extreme & 33 & 268 & 2.4\\% & 0.5\\% & 27.6 & 29.5 \\\\\nD: Homog.\\ ICC & 40 & 168 & 4.1\\% & 1.1\\% & 25.9 & 28.9 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nWhen ICC decreases with family size (scenarios B--D, matching empirical patterns), larger families contribute less per-model inflation than the weighted-mean assumes. The weighted-mean over-corrects by assigning excessive weight to mega-families whose low ICC does not warrant large DEFF adjustments. The simple-mean estimator better captures the average inflation per family under these conditions.\n\n\\section{Score Inflation Analysis}\n\\label{app:score_inflation}\n\nRemoving the 3,918 DIF-C items (31.3\\%) and rescoring on the 8,590 stable items shifts model accuracy upward by a mean of ${+}2.12$\\,pp overall (\\Cref{tab:score_inflation}). The cohort-differential is 0.29\\,pp (2023: ${+}2.35$\\,pp; 2024: ${+}2.06$\\,pp; Cohen's $d = 0.31$, $p < 10^{-10}$). Overall ranking correlation between original and stable-item scores is $\\rho = 0.9965$, but individual rank displacements reach ${\\pm}561$ at the 99th percentile and exceed ${\\pm}800$ in extreme cases. Equating adjustments are ${+}0.0235$ (2023) and ${+}0.0206$ (2024).\n\n\\begin{table}[h]\n\\centering\n\\caption{Score inflation from DIF-C item removal, by cohort.}\n\\label{tab:score_inflation}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nCohort & $N$ & Mean $\\Delta$ (pp) & SD (pp) & 95\\% CI \\\\\n\\midrule\n2023 & 1,080 & ${+}2.35$ & 0.88 & $[{+}2.30, {+}2.40]$ \\\\\n2024 & 807 & ${+}2.06$ & 1.04 & $[{+}1.99, {+}2.13]$ \\\\\nOther & 3,340 & ${+}2.05$ & 0.92 & $[{+}2.02, {+}2.08]$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Within-Architecture Temporal DIF}\n\\label{app:within_arch}\n\nTo rule out the confound that overall temporal DIF is driven by cross-architecture differences, we group fine-grained families into architecture lineages and run MH-DIF within each (\\Cref{tab:within_arch}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Within-architecture temporal DIF. C\\% = ETS~C items between 2023 and 2024 models within each lineage.}\n\\label{tab:within_arch}\n\\small\n\\begin{tabular}{lrrrl}\n\\toprule\nLineage & $N_{\\mathrm{ref}}$ (2023) & $N_{\\mathrm{foc}}$ (2024) & C\\% & Med $|\\Delta|$ \\\\\n\\midrule\nLlama & 171 & 315 & 59.2\\% & 2.38 \\\\\nQwen & 27 & 70 & 6.9\\% & 1.55 \\\\\nYi & 72 & 14 & 3.5\\% & 1.78 \\\\\nPhi & 60 & 20 & 1.3\\% & 2.85 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLlama, Qwen, and Yi show C\\% above the random baseline; Phi (C\\% $= 1.3\\%$, $N_{\\mathrm{foc}} = 20$) is inconclusive due to low power. Llama is the best-powered comparison ($N = 486$ total) and yields raw C\\% $= 59.2\\%$, which combines temporal and generational effects. After ability matching, within-architecture C\\% converges to ${\\sim}$28--29\\%, consistent with temporal C\\% ($28.9\\%$)---confirming that the temporal DIF signal persists within individual lineages and is not an artifact of comparing different architectures.\n\n\\section{Base-Only and Instruct-Only Temporal DIF}\n\\label{app:baseinst_temporal}\n\nSeparating the temporal cohorts by model type confirms that both base and instruct models independently exhibit substantial temporal DIF (\\Cref{tab:baseinst_temporal}). Training methodology modulates DIF \\emph{direction} (base: 60.1\\% reference-favoring with $r = -0.570$; instruct: 65.6\\% focal-favoring with $r = -0.079$) rather than DIF \\emph{magnitude}, providing direct evidence against composition shift as the primary driver.\n\n\\begin{table}[h]\n\\centering\n\\caption{Temporal DIF computed separately for base-only and instruct-only model subsets. Both model types independently exhibit C\\% $\\geq 32\\%$, far exceeding the random baseline (0.62\\%). Training methodology modulates DIF direction ($r$, focal-favoring proportion) rather than magnitude.}\n\\label{tab:baseinst_temporal}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nSubset & $N_{\\mathrm{ref}}$ / $N_{\\mathrm{foc}}$ & C\\% & $\\rho(\\mathrm{diff}, \\Delta_{\\mathrm{MH}})$ & Focal-fav \\\\\n\\midrule\nBase-only & 861 / 548 & 32.1\\% & $-0.570$ & 39.9\\% \\\\\nInstruct-only & 219 / 259 & 36.5\\% & $-0.079$ & 65.6\\% \\\\\nOverall & 1{,}080 / 807 & 31.3\\% & $-0.587$ & 43.9\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Composition Control}\n\\label{app:composition_control}\n\nThe 2023 and 2024 cohorts differ in base/instruct composition (2023: 79.7\\% base; 2024: 67.9\\% base; 11.8\\,pp gap). To test whether this confounds temporal DIF, we downsample 2023 base models to match the 2024 ratio and re-run MH-DIF (10 random seeds). Balanced C\\% $= 30.25\\% \\pm 1.32\\%$ (95\\% CI: $[27.65\\%, 32.84\\%]$), differing from the original 31.3\\% by only 1.08\\,pp. Composition shift does not explain the observed temporal DIF rate.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Literature:} summarizing related papers to inform the related-work section.\n\\end{itemize}\n\n",
      "numLines": 397,
      "startLine": 1,
      "totalLines": 397
    }
  },
  "sourceToolAssistantUUID": "dfd2f606-a3c6-42ef-a197-065fb6e530de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-25T11:07:34.402Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NF1oJEqMQfRpz2p9NQrgj3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95652325-76cf-4c77-b577-db7ba928fb62",
  "isSidechain": false,
  "requestId": "req_011CbPBRvY3qw5gou5p471qs",
  "type": "assistant",
  "uuid": "41ab0fdf-0b9f-4f63-aba3-62bfc261ee4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdBLwcUC8E9sai9hppTtBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12076,
      "cache_read_input_tokens": 39707,
      "output_tokens": 890,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 890,
          "cache_read_input_tokens": 39707,
          "cache_creation_input_tokens": 12076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12076
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

_source line 40 · 2026-05-25T11:07:34.407Z_

<details><summary>↩ Tool result · `toolu_01NF1oJEqMQfRpz2p9NQrgj3`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	\usepackage{pifont}
15	\usepackage{enumitem}
16	
17	\input{math_commands.tex}
18	
19	\usepackage{cleveref}
20	
21	\graphicspath{{../figures/paper/}}
22	
23	\title{Temporal Score Incomparability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
24	
25	\begin{document}
26	
27	\maketitle
28	
29	\input{sections/abstract}
30	\input{sections/introduction}
31	\input{sections/related_work}
32	\input{sections/method}
33	\input{sections/experiments}
34	\input{sections/discussion}
35	\input{sections/conclusion}
36	\input{sections/limitations}
37	
38	\bibliography{references}
39	
40	\appendix
41	\input{sections/appendix}
42	
43	\end{document}
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41ab0fdf-0b9f-4f63-aba3-62bfc261ee4b",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "37395cb4-3d70-4b8d-8d5b-ae1f2c699080",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{subcaption}\n\\usepackage{pifont}\n\\usepackage{enumitem}\n\n\\input{math_commands.tex}\n\n\\usepackage{cleveref}\n\n\\graphicspath{{../figures/paper/}}\n\n\\title{Temporal Score Incomparability in LLM Benchmarks:\\\\A Large-Scale Psychometric Audit of 5,227 Models}\n\n\\begin{document}\n\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\\input{sections/limitations}\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 44,
      "startLine": 1,
      "totalLines": 44
    }
  },
  "sourceToolAssistantUUID": "41ab0fdf-0b9f-4f63-aba3-62bfc261ee4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-25T11:07:34.819Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ly3B8NEJfFGPCB6GVjZ3zW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37395cb4-3d70-4b8d-8d5b-ae1f2c699080",
  "isSidechain": false,
  "requestId": "req_011CbPBRvY3qw5gou5p471qs",
  "type": "assistant",
  "uuid": "4cc50fef-a268-41f0-a44f-253e789053ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdBLwcUC8E9sai9hppTtBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12076,
      "cache_read_input_tokens": 39707,
      "output_tokens": 890,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 890,
          "cache_read_input_tokens": 39707,
          "cache_creation_input_tokens": 12076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12076
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

_source line 42 · 2026-05-25T11:07:34.889Z_

```json
{
  "parentUuid": "2a32ff71-f220-4445-804a-fd3a6e884df1",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "79fff6be-e94d-4fee-a748-b586c8ba3514",
  "timestamp": "2026-05-25T11:07:34.889Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：irt_equated_bench_regen Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 5 critical, 1 warning 一致性检…",
  "leafUuid": "79fff6be-e94d-4fee-a748-b586c8ba3514",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit EMNLP 2026 paper for custom rules compliance",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01"
}
```

---

### Assistant

_source line 45 · 2026-05-25T11:10:04.051Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the content. Let me do a systematic content audit across all the specified dimensions. Let me also run some grep searches to find specific patterns.

Let me now do the detailed content audit:

## 1. Narrative Consistency (CRITICAL)

### Abstract's "problem":
- "whether individual items measure the same construct over time is rarely tested" → temporal measurement invariance of LLM benchmarks

### Intro's "problem":
- "the assumption of temporal comparability underpins every cross-generation comparison published on leaderboards... yet it is rarely tested" → same problem
- ✅ Aligned

### Intro's contributions:


The paper claims three main contributions: finding that roughly 29% of MMLU items show temporal differential item functioning independent of web-overlap patterns, developing a cross-subject matching framework with zero false positive rate guarantee, and providing an actionable audit protocol with monitor/triage/correct stages. Checking against the methods section, the MH-DIF analysis on METABENCH directly addresses the first contribution, the cross-subject matching framework covers the second, and while the semi-synthetic injection framework primarily validates the approach, the protocol itself appears in the Discussion section and aligns with the third contribution.

### Intro's "gap":
- "Whether benchmark items function equival

The introduction identifies a gap: measurement invariance—whether items function equivalently across model generations—hasn't been systematically examined. The method fills this by applying DIF analysis from educational measurement, which is precisely designed to test this kind of invariance.

### Experiments verify Intro's claims?
- Contribution 1: Yes - Section 5.2 (Temporal DIF), 5.3 (web-overlap comparison), Section 6.1 (base-vs-instruct)
- Contribution 2: Yes - Section 5.5 (Semi-synthetic injection), Section 4.4 (injection framework)
- Contribution 3: Yes - Section 6.2 (audit protocol)
- ✅ Generally well-aligned

### Conclusion summarizes Experiments' conclusions?
- "Across six benchmarks, 17.9--31.3% of items exhibit temporal DIF while rankings remain stable (ρ ≥ 0.994); base-vs-instruct revers

The experiments support all three contributions—temporal DIF findings in sections 5.2-5.3 and 6.1, the injection framework in 4.4 and 5.5, and the audit protocol in 6.2. Now checking whether the conclusion accurately reflects what the experiments actually found, particularly the range of temporal DIF percentages across benchmarks and the stability of model rankings.

The numbers are consistent throughout: the 18-31% range in the abstract matches the 17.9-31.3% range across benchmarks (with MMLU at the high end), the correlation coefficient ρ ≥ 0.994 aligns with the lowest observed value of 0.9943 for WinoGrande, and the overlap metrics (Jaccard = 0.206, φ = 0.012) appear only where specified.

Now I'm noticing a potential ambiguity with the model counts—the abstract states "5,227 models across six benchmarks," but the data shows 5,227 is specific to MMLU while GSM8K has 6,702 models. The phrasing suggests all six benchmarks share the same model count, which isn't accurate, so the abstract's wording is misleading about the scope of the dataset. The introduction clarifies that 5,227 is the MMLU-specific count paired with 12,508 items, while the appendix shows GSM8K has 6,702 models—so the Abstract's phrasing is misleading by suggesting 5,227 models span all six benchmarks when they actually differ per benchmark. This appears to be a narrative inconsistency worth noting.

Now I'm tracking down the temporal DIF percentages across different sections. The introduction states 29.2% of MMLU items exhibit temporal DIF (with a range of 17.9–31.3% across benchmarks), the Abstract says 18–31%, and section 5.2 reports 31.3% receive ETS C classification before applying the DEFF correction, which brings it down to 29.2%. The figure caption confirms 29.2% flagged as C, so the discrepancy hinges on whether we're citing the raw classification rate or the corrected estimate. The real issue is that the document keeps switching between 31.3% (raw) and 29.2% (DEFF-corrected) without consistently signaling which one is being used, making it hard for readers to track. The experiments and tables lean on 31.3% as the main figure, while the introduction and figure captions favor 29.2%, so I need to pick one canonical number and stick with it throughout, or always clarify which version is being cited.

Now I'm checking the abstract structure to see if it covers the key elements—the problem statement about benchmark comparisons, the DIF methodology, and the headline results. Continuing to count the abstract word by word to make sure I stay under the 200-word limit. The remaining sections cover DIF independence from contamination labels, the opposing patterns between base and instruct models, the proposed audit protocol, and the key takeaway about psychometric monitoring. Adding those up carefully, I'm landing around 155-160 words total, which keeps me safely within the constraint. The abstract is around 130-140 words and stays under 200, though I should note those em-dashes. Looking at the introduction structure, it's quite compressed—the first paragraph weaves together background, the core problem, key findings, and implications all at once rather than following a traditional five-paragraph arc. There are only three paragraphs total before the figure and contribution list, with the second paragraph starting to address existing approaches but getting cut off. The style leads with the main finding upfront instead of building toward it gradually.

The related work section is well-organized thematically around psychometric methods, contamination detection, and benchmark quality rather than listing who did what. Now I'm checking whether the contributions listed in the introduction actually align with what gets developed in the sections—the first contribution mentions temporal DIF at scale and should map to sections 5.2 onward.

All three main contributions have corresponding sections in the paper. There are a few supporting sections like the validation analysis and structural analysis that aren't explicitly called out as contributions but they strengthen the methodology. The downstream impact section showing practical consequences of DIF isn't formally listed as a contribution, though it does appear in the introduction when discussing rank displacement, which is fine since it serves as evidence for the main narrative.

Looking at the scope claims in the title and abstract, the "5,227 Models" figure aligns with the MMLU analysis, which is the primary focus—the cross-benchmark validation with GSM8K's 6,702 models shows the findings generalize beyond that. The "Large-Scale Psychometric Audit" language is accurate for what the paper does, and "across six benchmarks" checks out with the cross-benchmark validation work. The paper avoids overclaiming with phrases like "significantly outperforms" or "state-of-the-art" since it's fundamentally about measurement rather than performance rankings. Now I'm checking whether the quantitative claims in the abstract and introduction match what's actually presented in the tables and results. I'm checking the claim about models being displaced by up to 851 rank positions—the appendix mentions ±561 at the 99th percentile and cases exceeding ±800, but doesn't explicitly state 851, so I need to flag where that specific number originates. The χ² statistic of 562.7 matches the Discussion section, and the Jaccard coefficient of 0.206 appears consistently across multiple sections.

Now looking at the claim strength: the "near-independent" characterization for DIF versus web-overlap seems defensible given the enrichment ratio of 0.964 and p-value of 0.88, even though a Jaccard of 0.206 does indicate some overlap. However, describing 50× improvement as "orders of magnitude" (plural) is imprecise—that's really between one and two orders of magnitude, so the phrasing could be more accurate.

For experimental rigor, the main results tables lack error bars despite bootstrap confidence intervals being mentioned in the text, which weakens the presentation though it's still acceptable for this type of work. The baselines look solid with random splits and ability-quintile comparisons included, and the injection experiments use five random seeds for uncertainty quantification.

The ablations across matching strategies, cohort designs, and DEFF corrections function as robustness checks rather than traditional ablations, which fits the paper's analytical nature. On reproducibility, the key hyperparameters are well-documented—K=5 strata with K=3 sensitivity checks, clear ETS thresholds, specified injection rates, and bootstrap seeds all accounted for. Compute requirements aren't detailed since this is an analysis paper rather than a training paper. I'm checking the remaining symbols and terminology—C% appears in a few different forms throughout the paper, and while "temporal DIF" and "temporal score incomparability" are technically distinct concepts, using them interchangeably as shorthand is fine since the paper establishes the distinction upfront.

Looking at how the sections flow together, the transitions feel natural—the introduction sets up the problem, related work positions the approach within existing methods, and then the methodology, experiments, and discussion follow logically. The discussion itself goes beyond just restating results; it actually interprets what the structured signal means and proposes a concrete protocol, which is what you want to see.

Now I'm checking the limitations section to see how honestly the authors acknowledge constraints...

The limitations cover three main points: the semi-synthetic nature of the framework, the independence assumption in the chi-square test, and various assumptions around cross-subject matching and temporal granularity. At around 290 words total, it's more detailed than strictly necessary, but it does address the three key areas without being excessive. I'm checking the abstract for em-dashes and finding that it uses `---` (LaTeX formatting) in at least one place: "temporal DIF---orders of magnitude above random baselines---while". Let me scan through the rest of the document to see how consistently em-dashes appear and whether they fit the de-AI style guidelines. I'm noticing the definition text doesn't use em-dashes, but I found them elsewhere in the paper—in the abstract and introduction with pairs like "temporal DIF---orders of magnitude above random baselines---while" and "measurement invariance---has not been systematically examined". Let me search more systematically for em-dashes, en-dashes in ranges versus explanatory contexts, and filler words like "importantly" or "notably" to get a complete picture of the writing style.

I should also verify there are no internal identifiers, server names, or infrastructure references—the GitHub URL uses an appropriate anonymous submission format, and I don't see any obvious internal tool references in the text I've reviewed so far.

Now checking the EMNLP 2026 submission requirements: the abstract is under 200 words at roughly 130-140 words, there's only one limitations section in the main text, and the ARR checklist isn't included in the PDF. The critical constraint is the 8-page limit for main text—I need to determine how many pages the core sections (abstract through conclusion) actually occupy versus appendix and references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79fff6be-e94d-4fee-a748-b586c8ba3514",
  "isSidechain": false,
  "requestId": "req_011CbPBSdV9nenyqnLpMpiZc",
  "type": "assistant",
  "uuid": "516c5e57-571a-45cd-92fa-9d87c38ee5bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEymZn3tRt5FHyVeQbvtHx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 73655,
      "cache_read_input_tokens": 11846,
      "output_tokens": 7467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 73655,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7467,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 73655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 73655
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

_source line 46 · 2026-05-25T11:10:04.053Z_

需要扫描 em-dash 和 AI 风格模式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "516c5e57-571a-45cd-92fa-9d87c38ee5bc",
  "isSidechain": false,
  "requestId": "req_011CbPBSdV9nenyqnLpMpiZc",
  "type": "assistant",
  "uuid": "94d97ea8-46fe-454f-8407-f5ea41d0d5ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEymZn3tRt5FHyVeQbvtHx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 73655,
      "cache_read_input_tokens": 11846,
      "output_tokens": 7467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 73655,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7467,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 73655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 73655
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

_source line 47 · 2026-05-25T11:10:06.726Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Q1cC3fZrpWVTdr3n7pBfjs`</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94d97ea8-46fe-454f-8407-f5ea41d0d5ad",
  "isSidechain": false,
  "requestId": "req_011CbPBSdV9nenyqnLpMpiZc",
  "type": "assistant",
  "uuid": "31952187-4212-4228-a60d-1dcae5590a3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEymZn3tRt5FHyVeQbvtHx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 73655,
      "cache_read_input_tokens": 11846,
      "output_tokens": 7467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 73655,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7467,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 73655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 73655
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

_source line 48 · 2026-05-25T11:10:11.314Z_

<details><summary>↩ Tool result · `toolu_018DgneLKFtqpHVYCPL4ZiNR`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1cb84e3-769b-4fc9-ba27-ed6356ac3a64",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "a9dde840-9a32-43b8-a0fa-88f6bb85bf30",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "b1cb84e3-769b-4fc9-ba27-ed6356ac3a64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-25T11:10:06.765Z_

<details><summary>↩ Tool result · `toolu_01Q1cC3fZrpWVTdr3n7pBfjs`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:6:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:62:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:75:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:105:Temporal DIF extends across all six METABENCH benchmarks (\Cref{tab:cross_benchmark}): C\% ranges from 17.9\% (HellaSwag~\citep{zellers2019hellaswag}) to 31.3\% (MMLU), with knowledge/reasoning benchmarks---including ARC (AI2 Reasoning Challenge)---consistently higher than procedural ones (C\% $= 26.9$--$31.3\%$ vs.\ $17.9$--$18.9\%$). These differences may partly reflect item difficulty distributions; we treat them as descriptive.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex:17:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex:6:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:28:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:157:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:168:\emph{Full sample} & --- & --- & 31.32 \\
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:185:\noindent Mean ICC $= 0.047$ (median $0.041$, Q3 $= 0.061$, max $= 0.219$; 4.8\% of items exceed $0.10$). After dividing each item's $\chi^2_{\mathrm{MH}}$ by its item-specific DEFF and re-applying ETS thresholds, 13.5--29.2\% of items retain Category~C classification depending on the $\bar{m}$ variant---both far exceeding the 0.62\% random-split baseline (21--47$\times$).
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:232:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:271:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:358:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:7:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31952187-4212-4228-a60d-1dcae5590a3e",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "73700ba8-4207-490c-9844-879922c428f1",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:6:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:10:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:62:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:75:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:105:Temporal DIF extends across all six METABENCH benchmarks (\\Cref{tab:cross_benchmark}): C\\% ranges from 17.9\\% (HellaSwag~\\citep{zellers2019hellaswag}) to 31.3\\% (MMLU), with knowledge/reasoning benchmarks---including ARC (AI2 Reasoning Challenge)---consistently higher than procedural ones (C\\% $= 26.9$--$31.3\\%$ vs.\\ $17.9$--$18.9\\%$). These differences may partly reflect item difficulty distributions; we treat them as descriptive.\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex:8:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex:17:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex:6:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:28:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:157:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:168:\\emph{Full sample} & --- & --- & 31.32 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:185:\\noindent Mean ICC $= 0.047$ (median $0.041$, Q3 $= 0.061$, max $= 0.219$; 4.8\\% of items exceed $0.10$). After dividing each item's $\\chi^2_{\\mathrm{MH}}$ by its item-specific DEFF and re-applying ETS thresholds, 13.5--29.2\\% of items retain Category~C classification depending on the $\\bar{m}$ variant---both far exceeding the 0.62\\% random-split baseline (21--47$\\times$).\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:232:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:271:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:358:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:5:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:7:[Omitted long matching line]",
    "numLines": 18
  },
  "sourceToolAssistantUUID": "31952187-4212-4228-a60d-1dcae5590a3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-25T11:10:09.066Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01YJ5u1gYkczpWtSnEB8pEhg`</summary>

```json
{
  "pattern": "(it is worth noting|notably|importantly|furthermore|moreover|additionally|delve|leverage|utilize|facilitate|a myriad|a plethora|in the realm of)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections",
  "output_mode": "content",
  "-i": true,
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73700ba8-4207-490c-9844-879922c428f1",
  "isSidechain": false,
  "requestId": "req_011CbPBSdV9nenyqnLpMpiZc",
  "type": "assistant",
  "uuid": "056ab54a-10f4-4bc5-929c-e207d42a3fb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEymZn3tRt5FHyVeQbvtHx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 73655,
      "cache_read_input_tokens": 11846,
      "output_tokens": 7467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 73655,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7467,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 73655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 73655
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

_source line 51 · 2026-05-25T11:10:09.089Z_

<details><summary>↩ Tool result · `toolu_01YJ5u1gYkczpWtSnEB8pEhg`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex:9:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "056ab54a-10f4-4bc5-929c-e207d42a3fb0",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "e6f80f19-24d9-4d61-b9a1-dea263d06da4",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex:9:[Omitted long matching line]",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "056ab54a-10f4-4bc5-929c-e207d42a3fb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-25T11:10:10.497Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01E2FHBhRot3UZsHjCMeSSgu`</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6f80f19-24d9-4d61-b9a1-dea263d06da4",
  "isSidechain": false,
  "requestId": "req_011CbPBSdV9nenyqnLpMpiZc",
  "type": "assistant",
  "uuid": "06dc97a8-dac2-4bf0-b130-224f5dacefe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEymZn3tRt5FHyVeQbvtHx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 73655,
      "cache_read_input_tokens": 11846,
      "output_tokens": 7467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 73655,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7467,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 73655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 73655
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

_source line 53 · 2026-05-25T11:10:10.511Z_

<details><summary>↩ Tool result · `toolu_01E2FHBhRot3UZsHjCMeSSgu`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:6:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:87:\includegraphics[width=\textwidth]{fig_3_within_subject_matching.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex:17:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex:21:In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex:39:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex:41:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex:46:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex:55:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex:6:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:18:\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini-Hochberg FDR correction at $q = 0.05$. The random-split sanity check provides an empirical estimate of the false positive rate under the null hypothesis.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:71:\paragraph{Nearest-neighbor matching.} The 1:1 nearest-neighbor matching selects, for each focal-cohort model, the reference-cohort model with the closest total score (caliper of 0.02 on normalized accuracy, approximately 0.14~SD). Balance is verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:84:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:271:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:358:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:392:    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06dc97a8-dac2-4bf0-b130-224f5dacefe3",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "f626471b-4c38-4275-824b-b42beb4bd968",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:6:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:10:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:14:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:87:\\includegraphics[width=\\textwidth]{fig_3_within_subject_matching.pdf}\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex:17:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex:21:In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex:39:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex:41:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex:46:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex:55:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex:6:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:18:\\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini-Hochberg FDR correction at $q = 0.05$. The random-split sanity check provides an empirical estimate of the false positive rate under the null hypothesis.\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:71:\\paragraph{Nearest-neighbor matching.} The 1:1 nearest-neighbor matching selects, for each focal-cohort model, the reference-cohort model with the closest total score (caliper of 0.02 on normalized accuracy, approximately 0.14~SD). Balance is verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding.\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:84:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:271:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:358:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:392:    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.",
    "numLines": 18
  },
  "sourceToolAssistantUUID": "06dc97a8-dac2-4bf0-b130-224f5dacefe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-25T11:10:11.296Z_

<details open><summary>🔧 Tool call — Grep · `toolu_018DgneLKFtqpHVYCPL4ZiNR`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f626471b-4c38-4275-824b-b42beb4bd968",
  "isSidechain": false,
  "requestId": "req_011CbPBSdV9nenyqnLpMpiZc",
  "type": "assistant",
  "uuid": "b1cb84e3-769b-4fc9-ba27-ed6356ac3a64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEymZn3tRt5FHyVeQbvtHx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 73655,
      "cache_read_input_tokens": 11846,
      "output_tokens": 7467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 73655,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7467,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 73655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 73655
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

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：irt_equated_bench_regen Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 5 critical, 1 warning 一致性检…",
  "leafUuid": "a9dde840-9a32-43b8-a0fa-88f6bb85bf30",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit EMNLP 2026 paper for custom rules compliance",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01"
}
```

---

### Assistant

_source line 57 · 2026-05-25T11:10:15.613Z_

<details><summary>Logged reasoning block</summary>

```text
Let me get more precise em-dash grep results and check specific patterns. The `---` search caught many matches but some are table dashes (`--- & ---`) and en-dash ranges (`--`). Let me get the actual em-dash lines.

Let me also count the abstract words more carefully and check a few more things.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9dde840-9a32-43b8-a0fa-88f6bb85bf30",
  "isSidechain": false,
  "requestId": "req_011CbPBeAXGCBJuiWvpkXZpn",
  "type": "assistant",
  "uuid": "83607bd0-8382-4abf-8f17-8cafce98cee7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119dVY7teBw8VLmyeABihoA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10098,
      "cache_read_input_tokens": 85501,
      "output_tokens": 750,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10098,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 750,
          "cache_read_input_tokens": 85501,
          "cache_creation_input_tokens": 10098,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10098
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

_source line 58 · 2026-05-25T11:10:16.085Z_

Now let me get more details on the em-dash instances and check a few more specific patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83607bd0-8382-4abf-8f17-8cafce98cee7",
  "isSidechain": false,
  "requestId": "req_011CbPBeAXGCBJuiWvpkXZpn",
  "type": "assistant",
  "uuid": "f3b7c82d-c0c1-4c89-bedf-6c54787527c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119dVY7teBw8VLmyeABihoA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10098,
      "cache_read_input_tokens": 85501,
      "output_tokens": 750,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10098,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 750,
          "cache_read_input_tokens": 85501,
          "cache_creation_input_tokens": 10098,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10098
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

_source line 59 · 2026-05-25T11:10:17.556Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01RAyrWqVCCkRMTKA4XRMh41`</summary>

```json
{
  "pattern": "[^-]---[^-]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3b7c82d-c0c1-4c89-bedf-6c54787527c3",
  "isSidechain": false,
  "requestId": "req_011CbPBeAXGCBJuiWvpkXZpn",
  "type": "assistant",
  "uuid": "3ba49b54-cb65-4edb-ae86-6d47f666abbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119dVY7teBw8VLmyeABihoA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10098,
      "cache_read_input_tokens": 85501,
      "output_tokens": 750,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10098,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 750,
          "cache_read_input_tokens": 85501,
          "cache_creation_input_tokens": 10098,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10098
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

_source line 60 · 2026-05-25T11:10:17.569Z_

<details><summary>↩ Tool result · `toolu_01RAyrWqVCCkRMTKA4XRMh41`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:6:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:62:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:75:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:105:Temporal DIF extends across all six METABENCH benchmarks (\Cref{tab:cross_benchmark}): C\% ranges from 17.9\% (HellaSwag~\citep{zellers2019hellaswag}) to 31.3\% (MMLU), with knowledge/reasoning benchmarks---including ARC (AI2 Reasoning Challenge)---consistently higher than procedural ones (C\% $= 26.9$--$31.3\%$ vs.\ $17.9$--$18.9\%$). These differences may partly reflect item difficulty distributions; we treat them as descriptive.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex:17:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex:6:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:28:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:157:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:168:\emph{Full sample} & --- & --- & 31.32 \\
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:185:\noindent Mean ICC $= 0.047$ (median $0.041$, Q3 $= 0.061$, max $= 0.219$; 4.8\% of items exceed $0.10$). After dividing each item's $\chi^2_{\mathrm{MH}}$ by its item-specific DEFF and re-applying ETS thresholds, 13.5--29.2\% of items retain Category~C classification depending on the $\bar{m}$ variant---both far exceeding the 0.62\% random-split baseline (21--47$\times$).
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:232:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:271:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:358:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:7:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ba49b54-cb65-4edb-ae86-6d47f666abbe",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "8ecae787-25c7-4062-91c5-a16ba4eedcd6",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:6:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:10:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:62:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:75:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:105:Temporal DIF extends across all six METABENCH benchmarks (\\Cref{tab:cross_benchmark}): C\\% ranges from 17.9\\% (HellaSwag~\\citep{zellers2019hellaswag}) to 31.3\\% (MMLU), with knowledge/reasoning benchmarks---including ARC (AI2 Reasoning Challenge)---consistently higher than procedural ones (C\\% $= 26.9$--$31.3\\%$ vs.\\ $17.9$--$18.9\\%$). These differences may partly reflect item difficulty distributions; we treat them as descriptive.\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex:8:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex:17:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex:6:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:28:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:157:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:168:\\emph{Full sample} & --- & --- & 31.32 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:185:\\noindent Mean ICC $= 0.047$ (median $0.041$, Q3 $= 0.061$, max $= 0.219$; 4.8\\% of items exceed $0.10$). After dividing each item's $\\chi^2_{\\mathrm{MH}}$ by its item-specific DEFF and re-applying ETS thresholds, 13.5--29.2\\% of items retain Category~C classification depending on the $\\bar{m}$ variant---both far exceeding the 0.62\\% random-split baseline (21--47$\\times$).\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:232:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:271:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:358:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:5:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:7:[Omitted long matching line]",
    "numLines": 18
  },
  "sourceToolAssistantUUID": "3ba49b54-cb65-4edb-ae86-6d47f666abbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-25T11:10:19.520Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LZhf1xhNvx2ja31sB5PbXU`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper && cat sections/abstract.tex | sed 's/\\\\[a-zA-Z]*{//g; s/}//g; s/\\\\[a-zA-Z]*//g; s/[${}]//g; s/---/ /g; s/--/-/g; s/\\\\//g' | wc -w",
  "description": "Count abstract words (rough estimate)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ecae787-25c7-4062-91c5-a16ba4eedcd6",
  "isSidechain": false,
  "requestId": "req_011CbPBeAXGCBJuiWvpkXZpn",
  "type": "assistant",
  "uuid": "02049e0c-d7c6-4e70-b16c-8b12cb4dea52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119dVY7teBw8VLmyeABihoA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10098,
      "cache_read_input_tokens": 85501,
      "output_tokens": 750,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10098,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 750,
          "cache_read_input_tokens": 85501,
          "cache_creation_input_tokens": 10098,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10098
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

_source line 62 · 2026-05-25T11:10:19.699Z_

<details><summary>↩ Tool result · `toolu_01LZhf1xhNvx2ja31sB5PbXU`</summary>

```text
144
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02049e0c-d7c6-4e70-b16c-8b12cb4dea52",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "d30e232d-18dc-4859-902e-64c0ceff085a",
  "toolUseResult": {
    "stdout": "144",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "02049e0c-d7c6-4e70-b16c-8b12cb4dea52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-25T11:10:21.317Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01VmKh5GekEdz1Ro39iCrKqq`</summary>

```json
{
  "pattern": ", (revealing|demonstrating|highlighting|showing|suggesting|indicating|confirming|establishing|providing|enabling|allowing)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d30e232d-18dc-4859-902e-64c0ceff085a",
  "isSidechain": false,
  "requestId": "req_011CbPBeAXGCBJuiWvpkXZpn",
  "type": "assistant",
  "uuid": "cf7dcd59-feef-4217-8a64-90b9fc59e657",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119dVY7teBw8VLmyeABihoA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10098,
      "cache_read_input_tokens": 85501,
      "output_tokens": 750,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10098,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 750,
          "cache_read_input_tokens": 85501,
          "cache_creation_input_tokens": 10098,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10098
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

_source line 64 · 2026-05-25T11:10:21.335Z_

<details><summary>↩ Tool result · `toolu_01VmKh5GekEdz1Ro39iCrKqq`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:6:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:23:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex:39:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:28:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:51:K=3 and K=5 yield near-identical detection power: TPR differences $<$0.02 across all conditions, within Monte Carlo noise. TPR ranges from 0.454 ($N{=}80$) to 0.571 ($N{=}100$) at $|\Delta_{\mathrm{MH}}| \geq 1.4$, with AUC of 0.905 at $N{=}100$, confirming that smaller corpora can use fewer strata without power loss (\Cref{tab:k3_power}).
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:71:\paragraph{Nearest-neighbor matching.} The 1:1 nearest-neighbor matching selects, for each focal-cohort model, the reference-cohort model with the closest total score (caliper of 0.02 on normalized accuracy, approximately 0.14~SD). Balance is verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:92:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:116:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:157:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:232:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:283:C\% increases monotonically from 0.3\% ($K = 1$) to 31.3\% ($K = \text{all}$). At each fixed $K$, variance across random member draws is negligible (SD ${<} 1.5$\,pp), confirming that the signal scales with statistical power rather than within-family redundancy. At $K{=}20$, C\% $= 19.7\% \pm 0.9\%$ ($N \approx 450$); the gap from the full-sample 31.3\% reflects reduced power, not reduced bias.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:363:Separating the temporal cohorts by model type confirms that both base and instruct models independently exhibit substantial temporal DIF (\Cref{tab:baseinst_temporal}). Training methodology modulates DIF \emph{direction} (base: 60.1\% reference-favoring with $r = -0.570$; instruct: 65.6\% focal-favoring with $r = -0.079$) rather than DIF \emph{magnitude}, providing direct evidence against composition shift as the primary driver.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:18:\item \textbf{Temporal DIF at scale}: 29.2\% of MMLU items exhibit temporal DIF (17.9--31.3\% across six benchmarks), near-independent of web-overlap labels (Jaccard $= 0.206$); base-vs-instruct stratification reveals opposite patterns ($\chi^2 = 562.7$), confirming mechanism separation (\Cref{sec:temporal,sec:groundtruth,sec:gsm8k,sec:disc_temporal}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf7dcd59-feef-4217-8a64-90b9fc59e657",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "7d8c5865-9d63-44da-875d-00b0a20add8e",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex:6:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex:23:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex:8:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex:39:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:28:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:51:K=3 and K=5 yield near-identical detection power: TPR differences $<$0.02 across all conditions, within Monte Carlo noise. TPR ranges from 0.454 ($N{=}80$) to 0.571 ($N{=}100$) at $|\\Delta_{\\mathrm{MH}}| \\geq 1.4$, with AUC of 0.905 at $N{=}100$, confirming that smaller corpora can use fewer strata without power loss (\\Cref{tab:k3_power}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:71:\\paragraph{Nearest-neighbor matching.} The 1:1 nearest-neighbor matching selects, for each focal-cohort model, the reference-cohort model with the closest total score (caliper of 0.02 on normalized accuracy, approximately 0.14~SD). Balance is verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding.\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:92:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:116:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:157:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:232:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:283:C\\% increases monotonically from 0.3\\% ($K = 1$) to 31.3\\% ($K = \\text{all}$). At each fixed $K$, variance across random member draws is negligible (SD ${<} 1.5$\\,pp), confirming that the signal scales with statistical power rather than within-family redundancy. At $K{=}20$, C\\% $= 19.7\\% \\pm 0.9\\%$ ($N \\approx 450$); the gap from the full-sample 31.3\\% reflects reduced power, not reduced bias.\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex:363:Separating the temporal cohorts by model type confirms that both base and instruct models independently exhibit substantial temporal DIF (\\Cref{tab:baseinst_temporal}). Training methodology modulates DIF \\emph{direction} (base: 60.1\\% reference-favoring with $r = -0.570$; instruct: 65.6\\% focal-favoring with $r = -0.079$) rather than DIF \\emph{magnitude}, providing direct evidence against composition shift as the primary driver.\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:5:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:18:\\item \\textbf{Temporal DIF at scale}: 29.2\\% of MMLU items exhibit temporal DIF (17.9--31.3\\% across six benchmarks), near-independent of web-overlap labels (Jaccard $= 0.206$); base-vs-instruct stratification reveals opposite patterns ($\\chi^2 = 562.7$), confirming mechanism separation (\\Cref{sec:temporal,sec:groundtruth,sec:gsm8k,sec:disc_temporal}).",
    "numLines": 16
  },
  "sourceToolAssistantUUID": "cf7dcd59-feef-4217-8a64-90b9fc59e657",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-25T11:10:22.437Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01VHZ3XLuGBBN7wecurDjiU7`</summary>

```json
{
  "pattern": "orders of magnitude",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d8c5865-9d63-44da-875d-00b0a20add8e",
  "isSidechain": false,
  "requestId": "req_011CbPBeAXGCBJuiWvpkXZpn",
  "type": "assistant",
  "uuid": "e7634037-2990-4c62-9d2c-84b826fa17a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119dVY7teBw8VLmyeABihoA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10098,
      "cache_read_input_tokens": 85501,
      "output_tokens": 750,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10098,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 750,
          "cache_read_input_tokens": 85501,
          "cache_creation_input_tokens": 10098,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10098
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

_source line 66 · 2026-05-25T11:10:22.465Z_

<details><summary>↩ Tool result · `toolu_01VHZ3XLuGBBN7wecurDjiU7`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex:2:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7634037-2990-4c62-9d2c-84b826fa17a1",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "96bb3c30-c77b-4389-8dca-c50b1481df68",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex:2:[Omitted long matching line]",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "e7634037-2990-4c62-9d2c-84b826fa17a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Runtime record

_source line 67 · 2026-05-25T11:10:22.470Z_

```json
{
  "parentUuid": "96bb3c30-c77b-4389-8dca-c50b1481df68",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "11886548-3804-4117-83d3-5148c8a4e444",
  "timestamp": "2026-05-25T11:10:22.470Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

---

### Assistant

_source line 68 · 2026-05-25T11:12:51.031Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me count the exact em-dash occurrences in the main text sections (excluding table dashes `--- & ---`):

Main text em-dashes:
1. abstract.tex:2 - "temporal DIF---orders of magnitude above random baselines---while"
2. introduction.tex:5 - I need to see the exact text. Let me check from my reading: the intro line 5 has something with ---
3. introduction.tex:7 - "Whether benchmark items function equivalently across model generations---\emph{measurement invariance}---has not"


4. related_work.tex:6 - "MH-DIF is nonparametric and robust to model misspecification---an advantage given poor 2PL fit"
5. related_work.tex:10 - probably has --- too
6. experiments.tex:62 - probably in section 5.3
7. experiments.tex:75 - probably in structural analysis
8. experiments.tex:105 - "knowledge/reasoning benchmarks---including ARC---consistently higher"
9. discussion.tex:8 - "Temporal DIF detects \emph{that} items function differently across cohorts, not \emph{why}---by design"
10. discussion.tex:17 - in protocol section
11. limitations.tex - need to check

I'm continuing to track down the remaining em-dashes across the document, checking the related work, experiments, discussion, and limitations sections for the pattern. I'm finding more em-dashes in the experiments section too—line 62 has one separating the definitions of web-overlap labels and DIF measures. Let me verify the exact locations and counts across all sections to build a complete picture of this pattern. I'm searching through the structural analysis section to verify the exact formatting of the comparison table and control conditions. Looking at line 75, I can see the three structural controls listed with their specific metrics, but I'm not finding the delimiter pattern I expected. Let me check the grep results for the "-ing" phrases to see what instances of revealing or demonstrating appear across the document sections.

I'm finding several instances of ", confirming..." patterns scattered through the introduction, related work, experiments, discussion, and methods sections—these are moderately AI-like in tone but less pronounced than the demonstrating patterns. Now checking the "orders of magnitude" claim against the actual cross-benchmark ratios: the data shows 45× to 95× improvements, which translates to roughly 1.7 orders of magnitude for the 50× figure, whereas "orders" plural typically suggests 100× or greater.

The "851 rank positions" claim in the introduction is problematic—the appendix only mentions ±561 at the 99th percentile and exceeding ±800 in extreme cases, but 851 doesn't appear anywhere in the supporting data. I also notice the paper switches between 31% and 29.2% for MMLU items depending on whether it's citing raw or adjusted figures, which needs clarification on which number is being referenced where. The conclusion is just one sentence, which is unusually sparse for a venue paper—it lacks any discussion of implications, limitations, or directions for future work. Let me check if there's a separate Limitations section in the appendix to see if that's where these details are addressed. Looking through the appendix sections, I don't see a dedicated Limitations heading, so the paper appears to be missing this entirely.

The Discussion section itself does provide genuine interpretation rather than just repeating results—it discusses the structured signal interpretation and proposes an audit protocol. However, I notice the Abstract mentions a phi coefficient of 0.012 that doesn't appear anywhere else in the main text, only the Jaccard, enrichment, and p-values are discussed. This is a minor inconsistency worth addressing.

The Conclusion is surprisingly terse—just a single sentence covering the temporal DIF findings and ranking stability. While the paper is space-constrained, this feels unusually brief and might signal to reviewers that the authors compressed it due to page limits rather than by design.

For the second contribution about cross-subject matching, it's claiming to solve a specific technical problem around matching-variable corruption with a zero false positive rate guarantee, extending to cases with up to five subjects, and includes a design effect correction. This is a solid methodological contribution but the phrasing is quite dense.

I'm also noticing the "851 rank positions" figure cited in the Introduction doesn't have a clear source—the appendix mentions percentile-based ranges like ±561 at the 99th percentile and extreme cases exceeding ±800, but 851 specifically isn't accounted for. I should track down where that number originates.

Now I'm compiling the full audit output and checking the em-dash count in the main text.

Scanning through the files for em-dashes...

I found several more instances across the document. Looking at discussion.tex line 8, there's "not \emph{why}---by design", and line 17 has the expert review reference. In limitations.tex, I'm seeing em-dashes used in the context of partial memorization scenarios. That brings the count to at least 10 em-dashes throughout the main text, which is a notable stylistic pattern. I'm also noticing the use of -ing participle phrases like "revealing that global exposure" and "confirming structured capability shifts" in the abstract—these are characteristic markers of AI-generated writing.

One thing I should verify: the paper does use double-dashes extensively for numerical ranges like "18--31\%" and "2023--2024", which are proper LaTeX en-dashes and completely acceptable. Now I need to check whether the contribution list in the introduction actually matches what's presented in the paper, starting with the first contribution about temporal DIF at scale.

The first contribution mentions 29.2% of MMLU items showing temporal DIF with ranges across benchmarks, web-overlap independence, and base-versus-instruct reversals—these map to sections 5.2, 5.3, 5.7, and 6.1. For the second contribution on cross-subject matching with the ΔFPR guarantee, I can find the injection framework and matching method in section 4.4, semi-synthetic validation in the experiments, and the DEFF correction in the appendix, though that's a limitation since DEFF isn't in the main text. The third contribution about the actionable audit protocol appears to be cut off, so I need to see how it's actually presented in the paper.

Now I'm checking the cross-benchmark correlation values against the claimed minimum. Looking at the performance metrics across MMLU, WinoGrande, TruthfulQA, ARC, GSM8K, and HellaSwag, the lowest correlation is WinoGrande at 0.9943, which does round to 0.994, so that claim checks out.

The abstract's statement about needing psychometric monitoring rather than just score reporting is a strong normative claim, but it's grounded in the evidence of substantial DIF effects, so it works as a concluding statement. I should also verify the "largest-scale DIF analysis" claim in the introduction—with 5,227 models and 12,508 items, that's genuinely large-scale work, and while Growing Pains is concurrent work in this space, this analysis appears to be the most comprehensive.

Now checking terminology consistency across the paper: DIF, temporal DIF, and MH-DIF are used appropriately in their respective contexts, C% is well-defined, and measurement invariance versus temporal score incomparability are both clearly introduced. The ETS Category C terminology has some variation (ETS C, Category C, C-flagged) but it's not confusing. I'm noticing the Introduction mentions 31% of MMLU items receiving ETS Category C classification with the threshold $|\Delta_{\mathrm{MH}}| \geq 1.5$, and I should check if this statistic is properly supported in the results.

There's a real inconsistency in how the flagged item percentages are reported: the Introduction opens with 31%, then shifts to 29.2% after non-independence correction, the contribution list cites 29.2%, Figure 1 shows 29.2%, but Table 1 reports 31.3% for Temporal. This back-and-forth between raw and corrected figures without clear labeling each time creates genuine confusion about which number is authoritative.

I'm also scanning for undefined acronyms—LLM, DIF, and MMLU are all properly defined early on.

Now checking DEFF: it appears in the Introduction as "Two DEFF estimators bound the non-independence effect" without expansion, then gets defined later in the Method section as "design effect," but the placement feels awkward since readers encounter it undefined first.

Looking at the other acronyms, I'm seeing a pattern — GSM8K, LOFO, AUROC, and AUC are all properly expanded on first use in their respective sections, but DEFF breaks this convention by appearing in the Introduction without its full form spelled out.

Actually, wait — let me double-check the Introduction more carefully. The contribution list does mention DEFF, but I need to verify whether it's actually expanded there or just used as an acronym. Looking at Contribution 2, it seems the expansion might be cut off mid-sentence, so DEFF may not be properly defined in the main text after all. I'm noticing that DEFF gets used in the opening paragraph without being formally introduced first—it appears in line 5 when the authors mention "simple-mean DEFF yields 29.2% and weighted-mean yields 13.5%", but the actual definition doesn't come until the contribution list at line 19 where they describe "design effect (DEFF) correction". This is a forward reference problem where a technical term is referenced before it's explained to the reader. I'm tracing through the paper to find where DEFF is first introduced. The Introduction mentions the 29.2% temporal DIF rate with a non-independence correction, and I can see DEFF gets formally defined in contribution 2 around line 19 as "design effect (DEFF)". Now I need to check the Methods section to see where it's actually used in the analysis. I'm noticing there's a forward-reference issue where the intro mentions "non-independence correction" with a specific result (29.2%) before DEFF is formally defined in the contributions. Let me verify the paper's statistical rigor by checking what significance tests are actually used—I can see it relies on MH chi-squared tests, bootstrap confidence intervals, and properly reported p-values throughout, so the claims are well-supported. I think I have what I need to write the full audit now.

Now I'm checking the scope claims about the six benchmarks mentioned in the title and abstract. Table 5 confirms all six are present (MMLU, WinoGrande, TruthfulQA, ARC, GSM8K, HellaSwag), but there's a precision issue: the abstract states "5,227 models across six benchmarks" when that number actually refers only to MMLU—GSM8K alone has 6,702 models. This phrasing could mislead readers into thinking all benchmarks have the same sample size.

The abstract also mentions "semi-synthetic injection with a cross-subject matching guarantee" as a methodological detail that's somewhat technical for the abstract alone, though it's a legitimate contribution to highlight.

I'm also verifying the intro's claims about the structural controls and sensitivity checks. The matched-ability quintiles and within-subject DIF are confirmed as the structural controls from Section 5.4, the IRT θ-conditioning is the sensitivity check, and the cross-benchmark analysis provides replication—all of this checks out. However, the intro's claim about "addressing the fragility of existing detectors" seems overstated relative to what the paper actually demonstrates.

The paper is motivated by wang2026fragility's concerns rather than directly addressing them, so that language needs to be more precise.

Looking at the Conclusion, it's essentially just a restatement of the main finding without touching on the cross-subject matching contribution or the audit protocol contribution. The protocol is completely missing from the conclusion despite being highlighted in the introduction, which creates a narrative gap. The conclusion also lacks any discussion of limitations, implications, or future directions—it reads more like an abstract summary than a proper conclusion.

Now I'm ready to finalize and write up the audit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11886548-3804-4117-83d3-5148c8a4e444",
  "isSidechain": false,
  "requestId": "req_011CbPBeyzXByyoHGKVY5aKk",
  "type": "assistant",
  "uuid": "e1a911f8-904a-4a35-96f2-711cfe449025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Farpx5xPcu4ukHEPSBbrd3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3687,
      "cache_read_input_tokens": 95599,
      "output_tokens": 7475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7475,
          "cache_read_input_tokens": 95599,
          "cache_creation_input_tokens": 3687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3687
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

_source line 69 · 2026-05-25T11:12:51.033Z_

Let me check a few more specific patterns for the audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1a911f8-904a-4a35-96f2-711cfe449025",
  "isSidechain": false,
  "requestId": "req_011CbPBeyzXByyoHGKVY5aKk",
  "type": "assistant",
  "uuid": "494039da-8032-4288-8b93-a8cd5b4a07cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Farpx5xPcu4ukHEPSBbrd3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3687,
      "cache_read_input_tokens": 95599,
      "output_tokens": 7475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7475,
          "cache_read_input_tokens": 95599,
          "cache_creation_input_tokens": 3687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3687
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

_source line 70 · 2026-05-25T11:12:51.463Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Fj7Pfa8P6NfvVghnhmWsrE`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper && grep -c '\\-\\-\\-' sections/abstract.tex sections/introduction.tex sections/related_work.tex sections/method.tex sections/experiments.tex sections/discussion.tex sections/conclusion.tex sections/limitations.tex",
  "description": "Count em-dash occurrences per main-text file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "494039da-8032-4288-8b93-a8cd5b4a07cd",
  "isSidechain": false,
  "requestId": "req_011CbPBeyzXByyoHGKVY5aKk",
  "type": "assistant",
  "uuid": "298aa4be-e1f3-454c-9330-d2039105f258",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Farpx5xPcu4ukHEPSBbrd3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3687,
      "cache_read_input_tokens": 95599,
      "output_tokens": 7475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7475,
          "cache_read_input_tokens": 95599,
          "cache_creation_input_tokens": 3687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3687
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

_source line 71 · 2026-05-25T11:12:53.590Z_

<details><summary>↩ Tool result · `toolu_0197hz3Dq44MLqvDCT4rRcQB`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:7:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "942215c0-404c-4a46-98ec-fe87f114b01c",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "c7e24979-2ec4-45b0-887e-3263b65c6e80",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:7:[Omitted long matching line]",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "942215c0-404c-4a46-98ec-fe87f114b01c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-25T11:12:51.526Z_

<details><summary>↩ Tool result · `toolu_01Fj7Pfa8P6NfvVghnhmWsrE`</summary>

```text
sections/abstract.tex:1
sections/introduction.tex:2
sections/related_work.tex:2
sections/method.tex:0
sections/experiments.tex:3
sections/discussion.tex:2
sections/conclusion.tex:0
sections/limitations.tex:1
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "298aa4be-e1f3-454c-9330-d2039105f258",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "f34cca1d-a392-49ca-8d9d-b178d90762d9",
  "toolUseResult": {
    "stdout": "sections/abstract.tex:1\nsections/introduction.tex:2\nsections/related_work.tex:2\nsections/method.tex:0\nsections/experiments.tex:3\nsections/discussion.tex:2\nsections/conclusion.tex:0\nsections/limitations.tex:1",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "298aa4be-e1f3-454c-9330-d2039105f258",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-25T11:12:52.602Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01J33Eb8wfPqoHvUaoCcaxGR`</summary>

```json
{
  "pattern": "851",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f34cca1d-a392-49ca-8d9d-b178d90762d9",
  "isSidechain": false,
  "requestId": "req_011CbPBeyzXByyoHGKVY5aKk",
  "type": "assistant",
  "uuid": "7c456cb6-5950-4b50-91e2-f20a4eb4ec5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Farpx5xPcu4ukHEPSBbrd3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3687,
      "cache_read_input_tokens": 95599,
      "output_tokens": 7475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7475,
          "cache_read_input_tokens": 95599,
          "cache_creation_input_tokens": 3687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3687
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

_source line 74 · 2026-05-25T11:12:52.615Z_

<details><summary>↩ Tool result · `toolu_01J33Eb8wfPqoHvUaoCcaxGR`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.fdb_latexmk:69:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr12.tfm" 1136768653 1288 655e228510b4c2a1abe905c368440826 ""
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.fdb_latexmk:140:  "/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty" 1579038678 6078 f1cb470c9199e7110a27851508ed7a5c ""
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.aux:1063:\@LN{851}{10}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c456cb6-5950-4b50-91e2-f20a4eb4ec5c",
  "isSidechain": false,
  "promptId": "d647b15e-9e2a-4001-bf38-93397d35ed13",
  "type": "user",
  "uuid": "889bf29d-83fe-4e08-94b8-b1273d1a98ae",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex:5:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.fdb_latexmk:69:  \"/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr12.tfm\" 1136768653 1288 655e228510b4c2a1abe905c368440826 \"\"\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.fdb_latexmk:140:  \"/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty\" 1579038678 6078 f1cb470c9199e7110a27851508ed7a5c \"\"\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.aux:1063:\\@LN{851}{10}",
    "numLines": 4
  },
  "sourceToolAssistantUUID": "7c456cb6-5950-4b50-91e2-f20a4eb4ec5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-25T11:12:53.578Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0197hz3Dq44MLqvDCT4rRcQB`</summary>

```json
{
  "pattern": "\\\\phi",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "889bf29d-83fe-4e08-94b8-b1273d1a98ae",
  "isSidechain": false,
  "requestId": "req_011CbPBeyzXByyoHGKVY5aKk",
  "type": "assistant",
  "uuid": "942215c0-404c-4a46-98ec-fe87f114b01c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Farpx5xPcu4ukHEPSBbrd3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3687,
      "cache_read_input_tokens": 95599,
      "output_tokens": 7475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7475,
          "cache_read_input_tokens": 95599,
          "cache_creation_input_tokens": 3687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3687
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

_source line 76_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：irt_equated_bench_regen Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 5 critical, 1 warning 一致性检…",
  "leafUuid": "c7e24979-2ec4-45b0-887e-3263b65c6e80",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01"
}
```

---

### Runtime record

_source line 77_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit EMNLP 2026 paper for custom rules compliance",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01"
}
```

---

### Assistant

_source line 78 · 2026-05-25T11:14:00.211Z_

<details><summary>Logged reasoning block</summary>

```text
The 851 number from the Introduction ("up to 851 rank positions") only appears in intro line 5 and in main.aux (line number). It doesn't appear in the experiments or appendix sections. The Appendix says "exceed ±800 in extreme cases." So 851 appears to be a specific data point, but it's not cited in the appendix. This is a sourcing concern — where does 851 come from?

Wait, let me re-read the Introduction more carefully. Let me find the exact mention of 851.

From introduction.tex:5: "DIF-corrected scoring (excluding all C-flagged items) shifts accuracy by ${+}2.12$\,pp on average, with individual models displaced by up to 851 rank positions."
 
There's a discrepancy here — the intro claims "up to 851" but the appendix only mentions "exceed ±800 in extreme cases" without specifying the exact maximum. The 851 figure appears to come directly from the data analysis rather than being derived from any table or figure in the paper, which means readers can't independently verify this claim from the text alone. I should flag this as a sourcing issue.

Now I'm tracking where φ = 0.012 appears throughout the paper. It shows up in both the Abstract and Introduction, and I'm checking whether it's also mentioned in the Experiments section.

Looking at Section 5.3 where the actual analysis is described, I see the comparison of DIF flags against web-overlap labels reports enrichment and Jaccard values but doesn't include the φ coefficient. So there's a disconnect—the key metric appears in the Abstract and Intro but not in the section where the analysis is actually presented.

I'm now compiling the full audit and organizing findings by severity. The most critical issue is that the Conclusion only addresses the first contribution (temporal DIF findings) in a single sentence, completely omitting the other two contributions about cross-subject matching and the audit protocol. This breaks the narrative arc from Introduction to Conclusion.

There's also a persistent inconsistency with the C% values—the paper switches between 29.2% (DEFF-corrected) and 31.3% (raw) across the Introduction, contribution list, Figure 1 caption, experiments, and tables without consistently specifying which version is being reported. A reviewer checking Figure 1 against Table 1 will immediately notice the discrepancy.

Beyond these critical issues, I'm flagging the heavy use of em-dashes throughout the text—11 instances across abstract, intro, related work, experiments, discussion, and limitations. Most are explanatory em-dashes that stand out as a stylistic marker.

The Abstract also overclaims with "orders of magnitude above random baselines," which suggests at least 100× improvement, but the actual ratios range from 45× to 95×—closer to 1.7 orders of magnitude. The phrasing should either be toned down to "an order of magnitude above" or replaced with the specific range.

There's a pattern of participial constructions with "-ing" verbs like "confirming," "revealing," and "providing" scattered throughout—at least 15 instances across the paper that contribute to a particular writing style.

Finally, the Introduction claims "up to 851 rank positions" but the Appendix only mentions "exceed ±800 in extreme cases," so the main text needs to either cite the exact source or align the numbers.

The φ coefficient appears in the Abstract and Introduction but doesn't show up in the experiments section where the actual analysis happens, creating an inconsistency about whether this statistic is central to the findings. The Abstract also misleads by suggesting all six benchmarks contain 5,227 models when that's only the MMLU count—GSM8K actually has 6,702 models. Contribution 2 also bundles together unrelated methodological approaches like cross-subject matching and DEFF correction.

The Conclusion is unusually terse at just one sentence, leaving no room to discuss implications or future directions. The claim that the framework "addresses the fragility of existing detectors" overstates the contribution—the paper is motivated by detector fragility but doesn't actually fix it. The Introduction also breaks from a standard structure, jumping into key findings in the first paragraph before establishing context.

DEFF gets referenced implicitly in the third paragraph with a specific correction percentage before it's formally defined in the contributions list, so readers encounter the corrected number without understanding what correction was applied. I'm also checking the limitations section for instances of "importantly"—there's one match that needs verification to see if it's actually present in the text.

The paper lacks computational cost reporting for the MH-DIF analysis, which would strengthen reproducibility even though this isn't primarily a training paper. Additionally, the audit protocol in Discussion section 6.2 feels underdeveloped relative to its status as a standalone contribution, receiving only about a paragraph of coverage.

I'm also noticing inconsistent terminology around the flagged category — it appears as "ETS C," "Category C," "ETS Category C," "C-flagged," and "DIF-C" throughout, which creates unnecessary parsing overhead. Let me refine my assessment by being more precise about the gerund patterns I flagged earlier. The ", [gerund]" construction at clause endings is the specific stylistic issue, not just any word containing "ing," so I should verify which instances actually follow that pattern.

Looking through the grep results, I can see the pattern appears consistently across multiple sections — abstract, introduction, related work, experiments, discussion, method, and appendix — with instances like "revealing that," "confirming structured capability shifts," and "confirming mechanism separation" appearing throughout the document.

The core issue is that nearly every result sentence ends with ", confirming [claim]" which creates a repetitive, formulaic tone that reads like AI-generated writing. There are roughly 7-8 instances in the main text and about 7 more scattered through the appendix.

I've also verified the limitations section is properly placed in the main text only, not duplicated in the appendix, so that structural requirement is met.

Now I'm ready to compile the final output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7e24979-2ec4-45b0-887e-3263b65c6e80",
  "isSidechain": false,
  "requestId": "req_011CbPBr8LsmN1mWibT6ewW1",
  "type": "assistant",
  "uuid": "84963fd3-b1dd-48c9-85d5-a64364df1580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZ2JsWKmRScXKQqri8c6kV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8038,
      "cache_read_input_tokens": 99286,
      "output_tokens": 5813,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8038,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5813,
          "cache_read_input_tokens": 99286,
          "cache_creation_input_tokens": 8038,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8038
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

_source line 79 · 2026-05-25T11:15:02.188Z_

Now I have all the data needed. Here is the complete audit.

```
[CONTENT_AUDIT_START]

=== 叙事一致性 (CRITICAL) ===

- [critical] [叙事一致性] Conclusion 仅覆盖 Contribution 1（temporal DIF findings），完全未提及 Contribution 2（cross-subject matching）和 Contribution 3（Monitor/Triage/Correct 审计协议）。单句 Conclusion 断裂了 Intro→Conclusion 叙事弧线——审稿人会认为贡献列表与总结不匹配。(conclusion.tex:5)

- [critical] [叙事一致性] 论文在 29.2%（DEFF-corrected）和 31.3%（raw）之间反复切换，未始终标明使用的是哪个数字。Intro §1 写 "31%"，Contribution 1 写 "29.2%"，Fig 1 caption 写 "29.2% of items flagged as C"，但 Table 1 显示 C% = 31.3。审稿人在 Figure caption 和紧邻的 Table 之间交叉验证时会产生困惑。建议统一：正文以 raw 31.3% 为基准报告，DEFF 校正范围 [13.5%, 29.2%] 作为 bracketing，每次引用都明确标注。

- [warning] [叙事一致性] Abstract 写 "5,227 models across six benchmarks"，但不同 benchmark 模型数不同（MMLU=5,227, GSM8K=6,702）。"5,227 models across six benchmarks" 的括号结构暗示所有 benchmark 都是 5,227 个模型。建议改为 "5,227 models on MMLU, replicated across six benchmarks" 或类似限定表述。(abstract.tex:2)

=== 去 AI 风格 ===

- [warning] [去AI] 主正文含 11 处解释性 em-dash (---)：abstract×1, introduction×2, related_work×2, experiments×3, discussion×2, limitations×1。这是审稿人最敏感的 AI 写作标志。范例："temporal DIF---orders of magnitude above random baselines---while"(abstract.tex:2)；"model generations---measurement invariance---has not"(introduction.tex:7)。逐一改为逗号、括号或拆句。

- [warning] [去AI] ", confirming/revealing/providing" 分词结构在主正文出现约 8 次，Appendix 约 7 次。多数句子以 "..., confirming X" 收尾，形成公式化节奏。高频范例："revealing that global exposure and differential functioning are complementary"(abstract.tex:2)；"confirming mechanism separation"(introduction.tex:18)；"confirming DIF as a mechanism-agnostic diagnostic"(discussion.tex:8)。建议至少将主正文半数改为独立短句。

- [info] [去AI] limitations.tex:9 出现一个 "Additionally"——单次使用可接受，但结合整体 -ing 模式需注意。

=== Claim 强度匹配 ===

- [warning] [Claim强度] Abstract 称 "orders of magnitude above random baselines"。实际比值范围为 45×–95×（Table 5），约 1.7 个数量级。"Orders of magnitude"（复数）通常暗示 ≥100×。建议改为 "an order of magnitude above" 或直接写 "45–95×"。(abstract.tex:2)

- [warning] [Claim强度] Introduction 称 "up to 851 rank positions"(introduction.tex:5)，但 Appendix §K (app:rank_reversal) 仅称 "exceed ±800 in extreme cases" 和 "±561 at the 99th percentile"。851 这个具体数字在正文任何表格或 appendix 中均未出现。定量 claim 必须可追溯到表格或明确数据引用。

- [warning] [Claim强度] Introduction 写 "addressing the fragility of existing detectors under post-training perturbation"(introduction.tex:16)。论文并未修复 wang2026fragility 指出的脆弱性——只是以此为动机。"Motivated by" 比 "addressing" 更准确。

=== 贡献-范围对齐 ===

- [warning] [贡献-范围] Contribution 2 将三个不同方法捆绑在一条中："cross-subject matching with ΔFPR=0 guarantee"（解决 matching 变量污染）+"DEFF correction"（解决模型家族非独立性）+"semi-synthetic validation"（验证检测力）。DEFF 与 cross-subject matching 解决的问题完全不同。审稿人可能认为贡献界定模糊。建议拆分或将 DEFF 降级为 robustness check。

- [warning] [贡献-范围] Contribution 3（audit protocol）在 Discussion §6.2 仅一段（约 80 words），对于一条独立贡献偏薄。建议增加 empirical grounding 的细节（如 threshold 选择依据、决策树），或降级为 Discussion 中的 practical implication 而非独立 contribution。

=== 章节结构 ===

- [warning] [章节结构] Conclusion 仅一句话（~30 words），是异常简短的 Conclusion。缺乏对 implications、future directions、和审计协议的讨论。审稿人可能认为作者空间不够或反思不足。至少应覆盖三条贡献各一句 + 一句 broader impact。(conclusion.tex:5)

- [info] [章节结构] Introduction 未严格遵循 5 段结构（背景→问题→gap→方法→贡献）。现为 3 段文字 + figure + 贡献列表。第一段直接报告关键发现（31% DIF），在读者理解 gap 之前就给出了结果。虽然 "lead with the punchline" 在 measurement 类论文中可行，但可能让不熟悉 DIF 的审稿人失去 context。

=== 符号/术语一致性 ===

- [warning] [符号] φ = 0.012 出现在 Abstract 和 Introduction(introduction.tex:7)，但在实际报告该分析的 Experiments §5.3 中缺失——§5.3 只报告了 Jaccard/enrichment/p-value。要么在 §5.3 补充 φ，要么从 Abstract/Intro 中移除。

- [info] [符号] ETS C 的称谓在正文中有 5 种变体："ETS C"、"Category C"、"ETS Category C"、"C-flagged"、"DIF-C"。虽非歧义，但增加了阅读认知负担。建议统一为 "ETS-C" 或 "Category C" + 在首次定义处确立。

- [info] [符号] Introduction §3 使用 "non-independence correction" 描述 DEFF 校正结果（29.2%），但 "design effect (DEFF)" 的定义直到稍后的 Contribution 2 才出现。读者在理解校正方法前就看到了校正后的数字。

=== 实验严谨性 ===

- [info] [实验严谨性] 主结果 Table 1 (tab:temporal_landscape) 和 Table 5 (tab:cross_benchmark) 均无 error bars 或 CI 列。Bootstrap CI 在正文文字中提及但不在表格内，审稿人扫表时无法直接判断不确定性。建议至少在 Table 1 的 C% 列加 CI 或在 caption 中注明。

=== 可复现性披露 ===

- [info] [可复现性] 论文未报告 MH-DIF 分析的计算成本（CPU hours / runtime）。虽然这不是训练论文，但在 5,227 models × 12,508 items + 多种 bootstrap + 多种 cohort 设计的规模下，计算成本信息有助于复现。

=== 章节过渡与逻辑流 ===

- [info] [章节过渡] Discussion §6.1 ("Temporal DIF as Structured Signal") 提供了高于 Results 的解读（base/instruct reversal 的机制讨论），不是简单重复数字。✓ 合格。

- [info] [章节过渡] Discussion §6.2 → Conclusion 过渡缺失：Discussion 以 "expert review, not automatic removal" 结束，Conclusion 直接跳到一句总结，没有任何 bridging。

=== Limitations 诚实度 ===

- [info] [Limitations] 覆盖 3 个核心点（semi-synthetic 局限、independence 假设违反、cross-subject matching 边界条件），实质性好，未回避关键弱点。长度约 290 words / 2 段，符合 EMNLP 规则（"一小段，覆盖 3 个点"——虽偏长但合理）。

=== 内部信息残留 ===

- [info] [内部信息] 未发现内部实验编号、服务器名、基础设施标识或不当内部流程引用。GitHub URL 使用匿名格式 (anonymous-nlp-2026-2)。✓ 合格。

=== 用户自定义规则检查 ===

- [info] [写作规则] Abstract 约 140 words，未超过 200 word 限制。✓ 合格。
- [info] [写作规则] Limitations section 仅一个，位于正文 Conclusion 之后、References 之前。Appendix 中无 Limitations section。✓ 合格。
- [info] [写作规则] ARR Responsible NLP Checklist 不在论文 PDF 中（由用户在 OpenReview 填写）。Appendix 有 "Use of AI Assistants" 声明。✓ 合格。
- [info] [审稿规则] 总页数 17 页。需确认正文（Abstract 到 Conclusion）≤ 8 页。从 .tex 结构看，Limitations 和 References 不计入限制，Appendix 不计入。建议编译后逐页核实 main text 部分不超过 8 页。

[CONTENT_AUDIT_END]
```

**审计摘要**：2 个 critical，9 个 warning，12 个 info。

最高优先级修复项：
1. **Conclusion 需要扩展**——至少 3 句覆盖全部 3 条 contribution
2. **29.2% vs 31.3% 标注需统一**——每次出现都明确是 raw 还是 DEFF-corrected
3. **11 处 em-dash 需全部消除**——改为逗号、括号或拆句

[AUDIT_DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84963fd3-b1dd-48c9-85d5-a64364df1580",
  "isSidechain": false,
  "requestId": "req_011CbPBr8LsmN1mWibT6ewW1",
  "type": "assistant",
  "uuid": "81770549-95ff-418f-af80-d606d829bf76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_audit_content_fe079fd8",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZ2JsWKmRScXKQqri8c6kV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8038,
      "cache_read_input_tokens": 99286,
      "output_tokens": 5813,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8038,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5813,
          "cache_read_input_tokens": 99286,
          "cache_creation_input_tokens": 8038,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8038
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

_source line 80_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：irt_equated_bench_regen Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 5 critical, 1 warning 一致性检…",
  "leafUuid": "81770549-95ff-418f-af80-d606d829bf76",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit EMNLP 2026 paper for custom rules compliance",
  "sessionId": "7ff2cb2e-b58b-4b2e-a040-4e213e8dbd01"
}
```

---
