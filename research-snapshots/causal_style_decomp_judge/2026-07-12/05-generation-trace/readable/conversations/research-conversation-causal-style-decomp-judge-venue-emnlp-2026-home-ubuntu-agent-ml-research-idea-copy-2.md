# Research conversation: 项目：causal_style_decomp_judge Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/a4cc3ec9-74b4-4680-bbce-0f59e6ef824c.jsonl`
- **Structured JSON:** [`78da917f351c75044e27.json`](../../sessions/78/78da917f351c75044e27.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-25T06:23:38.098Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T06:23:38.098Z",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "content": "项目：causal_style_decomp_judge\nVenue：emnlp-2026\n论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper\n\nPhase 1 确定性检查结果：\n源码检查: passed=False, 3 critical, 2 warning\n一致性检查: 0 critical, 1 warning\n编译: ✅, 页数: 20\n内部信息: 0 critical, 0 warning\n\n━━━ 用户自定义规则（作为额外检查项）━━━\n## 用户自定义规则（必须遵守）\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section\n- **[EMNLP 2026]** abstract 不要超过 200 words\n\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。\n\n请按照你的角色指令执行内容结构审计。"
}
```

---

### Runtime record

_source line 2 · 2026-05-25T06:23:38.103Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T06:23:38.103Z",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c"
}
```

---

## Round 1

49 recorded events

### User

_source line 3 · 2026-05-25T06:23:38.161Z_

项目：causal_style_decomp_judge
Venue：emnlp-2026
论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper

Phase 1 确定性检查结果：
源码检查: passed=False, 3 critical, 2 warning
一致性检查: 0 critical, 1 warning
编译: ✅, 页数: 20
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
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "a0f9ebe5-86f6-47b3-bc61-7f8dabac2018",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-25T06:23:38.158Z_

```json
{
  "parentUuid": "a0f9ebe5-86f6-47b3-bc61-7f8dabac2018",
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
  "uuid": "b912f089-1d3c-4ee1-909b-622f8d068790",
  "timestamp": "2026-05-25T06:23:38.158Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-25T06:23:38.158Z_

```json
{
  "parentUuid": "b912f089-1d3c-4ee1-909b-622f8d068790",
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
  "uuid": "3b34ca47-6ef7-44bf-b9a2-3ef7d81d7221",
  "timestamp": "2026-05-25T06:23:38.158Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-25T06:23:38.158Z_

```json
{
  "parentUuid": "3b34ca47-6ef7-44bf-b9a2-3ef7d81d7221",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "98305479-d182-4cfd-b01b-761e65b9502f",
  "timestamp": "2026-05-25T06:23:38.158Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
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
  "aiTitle": "Audit causal style decomposition paper for EMNLP 2026",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c"
}
```

---

### Assistant

_source line 8 · 2026-05-25T06:23:46.263Z_

<details><summary>Logged reasoning block</summary>

```text
I need to execute a content structure audit on the paper. Let me follow the execution flow:

1. Read `skills/global/paper-writing-norms.skill.md` and `skills/global/paper-quality-lessons.skill.md` for audit standards
2. Read all `.tex` files in the paper directory
3. Audit by each dimension
4. Output structured findings

Let me start by reading the skill files and finding the tex files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98305479-d182-4cfd-b01b-761e65b9502f",
  "isSidechain": false,
  "requestId": "req_011CbNonnLD2nbcpj92s1My9",
  "type": "assistant",
  "uuid": "939abad4-a225-476e-8eab-41a7cc73e372",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fxfuxEE59ejqZETrQPs9c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27005,
      "cache_read_input_tokens": 11846,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27005
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

_source line 9 · 2026-05-25T06:23:46.763Z_

开始执行内容结构审计。先加载审计标准和论文源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "939abad4-a225-476e-8eab-41a7cc73e372",
  "isSidechain": false,
  "requestId": "req_011CbNonnLD2nbcpj92s1My9",
  "type": "assistant",
  "uuid": "632fa013-31b1-446e-aed8-e4ad42d98f6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fxfuxEE59ejqZETrQPs9c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27005,
      "cache_read_input_tokens": 11846,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27005
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

_source line 10 · 2026-05-25T06:23:48.043Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NuX2vX5wchV7ZhE4xdPK4g`</summary>

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
  "parentUuid": "632fa013-31b1-446e-aed8-e4ad42d98f6f",
  "isSidechain": false,
  "requestId": "req_011CbNonnLD2nbcpj92s1My9",
  "type": "assistant",
  "uuid": "56c6ba4c-4757-4def-9580-64ea430ec1a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fxfuxEE59ejqZETrQPs9c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27005,
      "cache_read_input_tokens": 11846,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27005
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

_source line 11 · 2026-05-25T06:23:48.064Z_

<details><summary>↩ Tool result · `toolu_01NuX2vX5wchV7ZhE4xdPK4g`</summary>

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
  "parentUuid": "56c6ba4c-4757-4def-9580-64ea430ec1a2",
  "isSidechain": false,
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "6659ca45-8d46-44cc-86bc-0726ab5c0154",
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
  "sourceToolAssistantUUID": "56c6ba4c-4757-4def-9580-64ea430ec1a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 12 · 2026-05-25T06:23:48.194Z_

<details open><summary>🔧 Tool call — Read · `toolu_011P5ExQ2zsjdgGpgyCdvf9t`</summary>

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
  "parentUuid": "6659ca45-8d46-44cc-86bc-0726ab5c0154",
  "isSidechain": false,
  "requestId": "req_011CbNonnLD2nbcpj92s1My9",
  "type": "assistant",
  "uuid": "4c640a89-066f-4044-8e6c-abad9a7953e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fxfuxEE59ejqZETrQPs9c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27005,
      "cache_read_input_tokens": 11846,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27005
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

_source line 13 · 2026-05-25T06:23:48.201Z_

<details><summary>↩ Tool result · `toolu_011P5ExQ2zsjdgGpgyCdvf9t`</summary>

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
  "parentUuid": "4c640a89-066f-4044-8e6c-abad9a7953e7",
  "isSidechain": false,
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "9570644b-f8d4-4303-9df6-f77dbd09c051",
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
  "sourceToolAssistantUUID": "4c640a89-066f-4044-8e6c-abad9a7953e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 14 · 2026-05-25T06:23:48.870Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015D9NRSrmScUX3uRX55D7gK`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9570644b-f8d4-4303-9df6-f77dbd09c051",
  "isSidechain": false,
  "requestId": "req_011CbNonnLD2nbcpj92s1My9",
  "type": "assistant",
  "uuid": "7544729e-b0f0-42ab-83fc-8db3b952125f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fxfuxEE59ejqZETrQPs9c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27005,
      "cache_read_input_tokens": 11846,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27005
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

_source line 15 · 2026-05-25T06:23:48.887Z_

<details><summary>↩ Tool result · `toolu_015D9NRSrmScUX3uRX55D7gK`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7544729e-b0f0-42ab-83fc-8db3b952125f",
  "isSidechain": false,
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "aac0c921-a1d6-4006-aab6-831a7d04201f",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
    ],
    "durationMs": 7,
    "numFiles": 8,
    "truncated": false
  },
  "sourceToolAssistantUUID": "7544729e-b0f0-42ab-83fc-8db3b952125f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：causal_style_decomp_judge Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 3 critical, 2 war…",
  "leafUuid": "aac0c921-a1d6-4006-aab6-831a7d04201f",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit causal style decomposition paper for EMNLP 2026",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c"
}
```

---

### Assistant

_source line 18 · 2026-05-25T06:23:52.221Z_

现在读取所有 tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aac0c921-a1d6-4006-aab6-831a7d04201f",
  "isSidechain": false,
  "requestId": "req_011CbNooa53iLuiMYGs1uqp2",
  "type": "assistant",
  "uuid": "5217b809-8cb6-4bba-8ed9-f18c16e89887",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CXtb2HkNS4YKuaqB1CQkH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11954,
      "cache_read_input_tokens": 38851,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 38851,
          "cache_creation_input_tokens": 11954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11954
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

_source line 19 · 2026-05-25T06:23:53.027Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EZ8z8cfuqQjQK8TgZVTnCs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5217b809-8cb6-4bba-8ed9-f18c16e89887",
  "isSidechain": false,
  "requestId": "req_011CbNooa53iLuiMYGs1uqp2",
  "type": "assistant",
  "uuid": "8954ba99-ec27-4abe-8b8c-136c630d0670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CXtb2HkNS4YKuaqB1CQkH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11954,
      "cache_read_input_tokens": 38851,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 38851,
          "cache_creation_input_tokens": 11954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11954
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

_source line 20 · 2026-05-25T06:23:53.033Z_

<details><summary>↩ Tool result · `toolu_01EZ8z8cfuqQjQK8TgZVTnCs`</summary>

```text
1	\begin{abstract}
2	Likert and pairwise scoring produce divergent style-sensitivity profiles when applied to large language model (LLM) judges.
3	We define this divergence, the \emph{Likert Blindspot}, as statistically significant pairwise sensitivity absent from Likert; it admits non-exclusive explanations including measurement attenuation, format amplification, and construct divergence.
4	We introduce Controlled Style Decomposition (CSD), a black-box diagnostic quantifying this divergence via natural language inference (NLI)-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
5	Across five judges from five independent providers and two primary axes (formality, verbosity), pairwise reaches significance ($p < 0.001$) where Likert does not ($p > 0.28$), with Likert effect sizes collapsing toward zero at larger $n$, replicated across three benchmarks and confirmed by seven statistical methods.
6	Generalized estimating equation (GEE) decomposition reveals distinct per-axis confound structures: verbosity bias is style-dominated (Style odds ratio [OR] $3$--$13$, Originality OR ${<}1$), while formality reflects joint style--quality contributions.
7	One judge (Claude Sonnet~4) exhibits benchmark-dependent sensitivity, illustrating bias as a judge$\times$benchmark interaction; non-tie concordance (76.6\%, $p < .001$) is more consistent with attenuation than construct divergence.
8	Likert-only audits may thus fail to surface style-driven preferences that propagate through pairwise-based alignment pipelines.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8954ba99-ec27-4abe-8b8c-136c630d0670",
  "isSidechain": false,
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "75a0c728-3c1c-4467-a1fc-e56407a12e3e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nLikert and pairwise scoring produce divergent style-sensitivity profiles when applied to large language model (LLM) judges.\nWe define this divergence, the \\emph{Likert Blindspot}, as statistically significant pairwise sensitivity absent from Likert; it admits non-exclusive explanations including measurement attenuation, format amplification, and construct divergence.\nWe introduce Controlled Style Decomposition (CSD), a black-box diagnostic quantifying this divergence via natural language inference (NLI)-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.\nAcross five judges from five independent providers and two primary axes (formality, verbosity), pairwise reaches significance ($p < 0.001$) where Likert does not ($p > 0.28$), with Likert effect sizes collapsing toward zero at larger $n$, replicated across three benchmarks and confirmed by seven statistical methods.\nGeneralized estimating equation (GEE) decomposition reveals distinct per-axis confound structures: verbosity bias is style-dominated (Style odds ratio [OR] $3$--$13$, Originality OR ${<}1$), while formality reflects joint style--quality contributions.\nOne judge (Claude Sonnet~4) exhibits benchmark-dependent sensitivity, illustrating bias as a judge$\\times$benchmark interaction; non-tie concordance (76.6\\%, $p < .001$) is more consistent with attenuation than construct divergence.\nLikert-only audits may thus fail to surface style-driven preferences that propagate through pairwise-based alignment pipelines.\n\\end{abstract}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "8954ba99-ec27-4abe-8b8c-136c630d0670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-25T06:23:56.757Z_

<details><summary>↩ Tool result · `toolu_012ZFAAh9Kc8Lxn3iUPTMCtc`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Measurement-Mode Divergence\\in LLM Judge Style Evaluation}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\textbf{Residual confounding.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself.
43	Although formality effects survive logistic adjustment (OR $= 2.32$, $p = 0.006$), residual confounding is not fully eliminated; definitive resolution requires human ground-truth comparison of Likert and pairwise judgments on identical pairs.
44	
45	\textbf{Detection vs.\ amplification.}
46	The Blindspot may partly reflect pairwise format amplification \citep{jeong2025comparative} rather than pure detection.
47	Six controls bound this risk (\S\ref{sec:amplification}), but we cannot precisely quantify the amplification factor without a ground-truth bias magnitude.
48	Qwen3-32B serves as both rewriter and judge; an independent GPT-4o rewriter yields 22\% lower Style OR, confirming the Blindspot persists but effect-size precision varies with rewriter choice (Appendix~\ref{app:rewriter_indep}).
49	
50	\textbf{Scope.}
51	CSD applies only to surface-level axes whose rewrites preserve semantic content; a tone pilot (assertive $\to$ hedging) was rejected by the NLI gate.
52	Primary analyses use LLMBar ($n = 100$) with five judges; generalization to additional axes, benchmarks, and judges remains open.
53	Style sensitivity may vary across model versions (\S\ref{sec:nli_validation}), and GEE odds-ratio estimates require large-sample validation to converge from initial upper-bound estimates ($49$--$72\%$ shrinkage at $n = 330$--$355$).
54	
55	\bibliography{references}
56	
57	\input{sections/appendix}
58	
59	\end{document}
60	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5594ab93-83b7-463f-bf66-9113f815ce64",
  "isSidechain": false,
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "90ecf62a-1cd2-4cab-a02c-1f52554a8c5d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n% \\usepackage{inconsolata} % unavailable locally; re-enable for submission\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{tikz}\n\\usetikzlibrary{arrows.meta,positioning}\n\n\\title{The Likert Blindspot: Measurement-Mode Divergence\\\\in LLM Judge Style Evaluation}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\n\\input{sections/introduction}\n\n\\input{sections/related_work}\n\n\\input{sections/method}\n\n\\input{sections/experiments}\n\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Residual confounding.}\nThe NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself.\nAlthough formality effects survive logistic adjustment (OR $= 2.32$, $p = 0.006$), residual confounding is not fully eliminated; definitive resolution requires human ground-truth comparison of Likert and pairwise judgments on identical pairs.\n\n\\textbf{Detection vs.\\ amplification.}\nThe Blindspot may partly reflect pairwise format amplification \\citep{jeong2025comparative} rather than pure detection.\nSix controls bound this risk (\\S\\ref{sec:amplification}), but we cannot precisely quantify the amplification factor without a ground-truth bias magnitude.\nQwen3-32B serves as both rewriter and judge; an independent GPT-4o rewriter yields 22\\% lower Style OR, confirming the Blindspot persists but effect-size precision varies with rewriter choice (Appendix~\\ref{app:rewriter_indep}).\n\n\\textbf{Scope.}\nCSD applies only to surface-level axes whose rewrites preserve semantic content; a tone pilot (assertive $\\to$ hedging) was rejected by the NLI gate.\nPrimary analyses use LLMBar ($n = 100$) with five judges; generalization to additional axes, benchmarks, and judges remains open.\nStyle sensitivity may vary across model versions (\\S\\ref{sec:nli_validation}), and GEE odds-ratio estimates require large-sample validation to converge from initial upper-bound estimates ($49$--$72\\%$ shrinkage at $n = 330$--$355$).\n\n\\bibliography{references}\n\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 60,
      "startLine": 1,
      "totalLines": 60
    }
  },
  "sourceToolAssistantUUID": "5594ab93-83b7-463f-bf66-9113f815ce64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T06:23:53.373Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XvqyBKFm8xS5uoJGMYsq6Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75a0c728-3c1c-4467-a1fc-e56407a12e3e",
  "isSidechain": false,
  "requestId": "req_011CbNooa53iLuiMYGs1uqp2",
  "type": "assistant",
  "uuid": "bde0be39-b297-4159-a304-2d9be7cb4160",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CXtb2HkNS4YKuaqB1CQkH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11954,
      "cache_read_input_tokens": 38851,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 38851,
          "cache_creation_input_tokens": 11954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11954
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

_source line 23 · 2026-05-25T06:23:53.378Z_

<details><summary>↩ Tool result · `toolu_01XvqyBKFm8xS5uoJGMYsq6Y`</summary>

```text
1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} --- in our experiments, given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions.
5	We term this the \emph{Likert Blindspot}, an operational descriptor for the measurement-mode divergence where pairwise comparison detects statistically significant style sensitivity that Likert scoring fails to detect on the same data, without committing to a specific causal mechanism.
6	This divergence admits multiple non-exclusive explanations (Likert measurement attenuation, pairwise format amplification \citep{jeong2025comparative}, or construct-level differences), which our controlled design bounds but cannot definitively adjudicate (\S\ref{sec:likert_pairwise}).
7	This example reflects a consistent pattern: surface-level style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}, with 76--92\% of preferences originating from style cues \citep{li2026preference,soumik2026judging}.
8	
9	LLM judges are central infrastructure for natural language processing (NLP) evaluation and alignment training (reinforcement learning from human feedback [RLHF], direct preference optimization [DPO]), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.
10	Despite this, existing approaches address individual requirements (multi-dimensional style analysis \citep{casse2026concise,wang2026fairjudge}, interventional design \citep{reber2025rate}, population-level correction \citep{dubois2025lc}), but no single framework integrates per-axis decomposition, interventional identification, confound-structure analysis, and black-box applicability.
11	Classical psychometrics establishes that pairwise comparison yields higher discriminability than absolute rating \citep{thurstone1927law,david1988method}; our power analysis (Figure~\ref{fig:power_curve}) is quantitatively consistent.
12	In the LLM judge setting, this gap has \emph{per-axis} confound signatures: verbosity is style-dominated (Style OR $3$--$13$) while formality is quality-confounded (Table~\ref{tab:gee}), a decomposition not previously applied in LLM judge evaluation.
13	
14	We propose Controlled Style Decomposition (CSD), combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
15	Inspired by interventional text analysis \citep{veitch2020adapting}, CSD operates in three stages: style-controlled rewriting along a single axis, NLI entailment verification, and bias measurement via forced-choice comparison.
16	CSD requires no access to judge internals and applies post-hoc to any black-box judge.
17	Our experiments demonstrate the \emph{Likert Blindspot} across four target judges from independent providers (GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash), a fifth judge (Claude Sonnet~4) with benchmark-dependent sensitivity, three benchmarks, and two primary style axes, with exploratory register evidence.
18	On formality data, Likert yields non-significant effects ($p = 0.905$, $0.461$), while Bradley-Terry (BT) detects 63.0\% (GPT-4o, $p = 0.0004$) and 66.5\% (Qwen3-32B, $p < 0.0001$) formal preferences; verbosity shows 77.3\% BT ($p < 0.0001$) invisible to Likert ($p = 0.395$; Figure~\ref{fig:forest_plot}).
19	
20	Our contributions are both methodological and empirical:
21	\begin{itemize}
22	    \item \textbf{Empirical finding:} the first systematic demonstration that pairwise and Likert formats yield qualitatively divergent style sensitivity profiles across four judges, three benchmarks, and two axes with position control, with selective cross-benchmark validation targeting the strongest effects (Table~\ref{tab:main_results}).
23	    \item \textbf{Analytical contribution:} GEE conditional decomposition reveals per-axis confound structures invisible to aggregate analysis: verbosity is style-dominated (Style OR $3$--$13$) while formality reflects joint style--quality confounding (Table~\ref{tab:gee}).
24	    \item \textbf{Practical contribution:} CSD operates as a black-box diagnostic requiring no access to model internals, applicable post-hoc to any judge (\S\ref{sec:method}).
25	\end{itemize}
26	
27	\begin{figure*}[t]
28	\centering
29	\includegraphics[width=0.92\textwidth]{figures/pipeline_diagram.pdf}
30	\vspace{-6pt}
31	\caption{CSD pipeline overview. Numbers indicate sample attrition at each stage.}
32	\label{fig:pipeline}
33	\end{figure*}
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bde0be39-b297-4159-a304-2d9be7cb4160",
  "isSidechain": false,
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "b4693db7-e3ea-4c91-a6f9-97645d647ee7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\n\\emph{``What is the average height for a male?''} --- in our experiments, given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \\emph{higher} on a 1--10 Likert scale (8 vs.\\ 5), yet consistently selects the formal variant in pairwise comparison.\nSame judge, same texts, opposite conclusions.\nWe term this the \\emph{Likert Blindspot}, an operational descriptor for the measurement-mode divergence where pairwise comparison detects statistically significant style sensitivity that Likert scoring fails to detect on the same data, without committing to a specific causal mechanism.\nThis divergence admits multiple non-exclusive explanations (Likert measurement attenuation, pairwise format amplification \\citep{jeong2025comparative}, or construct-level differences), which our controlled design bounds but cannot definitively adjudicate (\\S\\ref{sec:likert_pairwise}).\nThis example reflects a consistent pattern: surface-level style features alone explain most of the variance in judge scores \\citep{murugadoss2025sos}, with 76--92\\% of preferences originating from style cues \\citep{li2026preference,soumik2026judging}.\n\nLLM judges are central infrastructure for natural language processing (NLP) evaluation and alignment training (reinforcement learning from human feedback [RLHF], direct preference optimization [DPO]), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.\nDespite this, existing approaches address individual requirements (multi-dimensional style analysis \\citep{casse2026concise,wang2026fairjudge}, interventional design \\citep{reber2025rate}, population-level correction \\citep{dubois2025lc}), but no single framework integrates per-axis decomposition, interventional identification, confound-structure analysis, and black-box applicability.\nClassical psychometrics establishes that pairwise comparison yields higher discriminability than absolute rating \\citep{thurstone1927law,david1988method}; our power analysis (Figure~\\ref{fig:power_curve}) is quantitatively consistent.\nIn the LLM judge setting, this gap has \\emph{per-axis} confound signatures: verbosity is style-dominated (Style OR $3$--$13$) while formality is quality-confounded (Table~\\ref{tab:gee}), a decomposition not previously applied in LLM judge evaluation.\n\nWe propose Controlled Style Decomposition (CSD), combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.\nInspired by interventional text analysis \\citep{veitch2020adapting}, CSD operates in three stages: style-controlled rewriting along a single axis, NLI entailment verification, and bias measurement via forced-choice comparison.\nCSD requires no access to judge internals and applies post-hoc to any black-box judge.\nOur experiments demonstrate the \\emph{Likert Blindspot} across four target judges from independent providers (GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash), a fifth judge (Claude Sonnet~4) with benchmark-dependent sensitivity, three benchmarks, and two primary style axes, with exploratory register evidence.\nOn formality data, Likert yields non-significant effects ($p = 0.905$, $0.461$), while Bradley-Terry (BT) detects 63.0\\% (GPT-4o, $p = 0.0004$) and 66.5\\% (Qwen3-32B, $p < 0.0001$) formal preferences; verbosity shows 77.3\\% BT ($p < 0.0001$) invisible to Likert ($p = 0.395$; Figure~\\ref{fig:forest_plot}).\n\nOur contributions are both methodological and empirical:\n\\begin{itemize}\n    \\item \\textbf{Empirical finding:} the first systematic demonstration that pairwise and Likert formats yield qualitatively divergent style sensitivity profiles across four judges, three benchmarks, and two axes with position control, with selective cross-benchmark validation targeting the strongest effects (Table~\\ref{tab:main_results}).\n    \\item \\textbf{Analytical contribution:} GEE conditional decomposition reveals per-axis confound structures invisible to aggregate analysis: verbosity is style-dominated (Style OR $3$--$13$) while formality reflects joint style--quality confounding (Table~\\ref{tab:gee}).\n    \\item \\textbf{Practical contribution:} CSD operates as a black-box diagnostic requiring no access to model internals, applicable post-hoc to any judge (\\S\\ref{sec:method}).\n\\end{itemize}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth]{figures/pipeline_diagram.pdf}\n\\vspace{-6pt}\n\\caption{CSD pipeline overview. Numbers indicate sample attrition at each stage.}\n\\label{fig:pipeline}\n\\end{figure*}\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "bde0be39-b297-4159-a304-2d9be7cb4160",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T06:23:53.877Z_

<details open><summary>🔧 Tool call — Read · `toolu_019jGwJSpJqABvQqs3THQLah`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4693db7-e3ea-4c91-a6f9-97645d647ee7",
  "isSidechain": false,
  "requestId": "req_011CbNooa53iLuiMYGs1uqp2",
  "type": "assistant",
  "uuid": "c43a681f-7b83-47f0-9c15-f77419e30eb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CXtb2HkNS4YKuaqB1CQkH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11954,
      "cache_read_input_tokens": 38851,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 38851,
          "cache_creation_input_tokens": 11954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11954
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

_source line 25 · 2026-05-25T06:23:53.897Z_

<details><summary>↩ Tool result · `toolu_019jGwJSpJqABvQqs3THQLah`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Interventional Approaches to Judge Bias}
5	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
6	\citet{reber2025rate} propose RATE, which rewrites outputs along style attributes and measures causal effects via Likert average treatment effect (ATE); however, our experiments show 60\% of style-transformed pairs receive identical Likert scores, yielding non-significant effects that pairwise comparison detects at $p = 0.006$.
7	CSD differs in targeting individual style axes, using position-controlled pairwise comparison, and enforcing content preservation via NLI gating.
8	\citet{counterfactual2025rhetorical} adopt a similar design at persona-level granularity, whereas CSD intervenes on specific style axes with position control.
9	
10	\paragraph{Style Bias in LLM Judges}
11	The foundational LLM-as-judge framework \citep{zheng2023judging} documented position bias; \citet{shi2024judging} study it across 15 judges, and \citet{ye2024justice} quantify 12 bias types, though neither isolates individual style effects.
12	Style bias as a separate source has received recent attention \citep{wu2023style,murugadoss2025sos,saito2023verbosity,li2026preference,soumik2026judging}; \citet{li2026preference} show that style-mediated \emph{preference leakage} propagates through evaluation pipelines.
13	Multi-feature frameworks such as CASSE \citep{casse2026concise} and FairJudge \citep{wang2026fairjudge} decompose style into finer dimensions but rely on correlational analyses that cannot distinguish causal style effects from content quality confounds.
14	\citet{jeong2025comparative} identify the Comparative Trap---pairwise comparison may amplify style biases---which we address in \S\ref{sec:amplification}.
15	Unlike human evaluators, LLM judges acquire format-specific biases through RLHF training: pairwise comparison serves as the reward signal in DPO pipelines, while Likert scoring is used for evaluation, motivating independent quantification of the format gap.
16	
17	\paragraph{Measurement Format Sensitivity}
18	The superiority of pairwise comparison over rating scales has been established since \citet{thurstone1927law}; \citet{carterette2008here} confirm this for information retrieval, and \citet{krosnick1999survey} documents satisficing behavior that may compound the tie inflation we observe.
19	Within NLP, \citet{amidei2019likert} review Likert scales \citep{likert1932technique} in natural language generation (NLG) evaluation, and \citet{novikova2018rankme} confirm that forced-choice methods detect quality differences that rating scales miss.
20	The Bradley-Terry model \citep{bradley1952rank} underpins Chatbot Arena \citep{chiang2024chatbot} and AlpacaFarm \citep{dubois2023alpacafarm}; no prior work combines BT with per-axis GEE decomposition to expose confound structures invisible to aggregate scores.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c43a681f-7b83-47f0-9c15-f77419e30eb8",
  "isSidechain": false,
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "9d2d3061-ea18-4ade-9248-7315ecde31cc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Interventional Approaches to Judge Bias}\nText-based interventional methods have a growing methodological foundation \\citep{feder2021causalm,wu2021polyjuice,feder2022causal}.\n\\citet{reber2025rate} propose RATE, which rewrites outputs along style attributes and measures causal effects via Likert average treatment effect (ATE); however, our experiments show 60\\% of style-transformed pairs receive identical Likert scores, yielding non-significant effects that pairwise comparison detects at $p = 0.006$.\nCSD differs in targeting individual style axes, using position-controlled pairwise comparison, and enforcing content preservation via NLI gating.\n\\citet{counterfactual2025rhetorical} adopt a similar design at persona-level granularity, whereas CSD intervenes on specific style axes with position control.\n\n\\paragraph{Style Bias in LLM Judges}\nThe foundational LLM-as-judge framework \\citep{zheng2023judging} documented position bias; \\citet{shi2024judging} study it across 15 judges, and \\citet{ye2024justice} quantify 12 bias types, though neither isolates individual style effects.\nStyle bias as a separate source has received recent attention \\citep{wu2023style,murugadoss2025sos,saito2023verbosity,li2026preference,soumik2026judging}; \\citet{li2026preference} show that style-mediated \\emph{preference leakage} propagates through evaluation pipelines.\nMulti-feature frameworks such as CASSE \\citep{casse2026concise} and FairJudge \\citep{wang2026fairjudge} decompose style into finer dimensions but rely on correlational analyses that cannot distinguish causal style effects from content quality confounds.\n\\citet{jeong2025comparative} identify the Comparative Trap---pairwise comparison may amplify style biases---which we address in \\S\\ref{sec:amplification}.\nUnlike human evaluators, LLM judges acquire format-specific biases through RLHF training: pairwise comparison serves as the reward signal in DPO pipelines, while Likert scoring is used for evaluation, motivating independent quantification of the format gap.\n\n\\paragraph{Measurement Format Sensitivity}\nThe superiority of pairwise comparison over rating scales has been established since \\citet{thurstone1927law}; \\citet{carterette2008here} confirm this for information retrieval, and \\citet{krosnick1999survey} documents satisficing behavior that may compound the tie inflation we observe.\nWithin NLP, \\citet{amidei2019likert} review Likert scales \\citep{likert1932technique} in natural language generation (NLG) evaluation, and \\citet{novikova2018rankme} confirm that forced-choice methods detect quality differences that rating scales miss.\nThe Bradley-Terry model \\citep{bradley1952rank} underpins Chatbot Arena \\citep{chiang2024chatbot} and AlpacaFarm \\citep{dubois2023alpacafarm}; no prior work combines BT with per-axis GEE decomposition to expose confound structures invisible to aggregate scores.\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  },
  "sourceToolAssistantUUID": "c43a681f-7b83-47f0-9c15-f77419e30eb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T06:23:54.640Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KD3CTguP3Eiqd3TzcEwZyz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d2d3061-ea18-4ade-9248-7315ecde31cc",
  "isSidechain": false,
  "requestId": "req_011CbNooa53iLuiMYGs1uqp2",
  "type": "assistant",
  "uuid": "854639cf-1c34-459b-ae6d-53fb01b3d341",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CXtb2HkNS4YKuaqB1CQkH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11954,
      "cache_read_input_tokens": 38851,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 38851,
          "cache_creation_input_tokens": 11954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11954
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

_source line 27 · 2026-05-25T06:23:54.646Z_

<details><summary>↩ Tool result · `toolu_01KD3CTguP3Eiqd3TzcEwZyz`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Style-Controlled Rewriting}
5	\label{sec:rewriting}
6	
7	We isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis while holding content fixed, a single-axis intervention design that enables per-axis causal attribution rather than aggregate style sensitivity measurement.
8	For each text, an instruction-tuned LLM (Qwen3-32B) classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification).
9	It then rewrites the text toward the opposite pole (temperature 0.7, selected to balance diversity with coherence in pilot experiments) according to an axis-specific prompt (Appendix~\ref{app:rewriting_prompts}).
10	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
11	Each operation approximates a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}; Appendix~\ref{app:cross_axis_contamination}).
12	To control for rewriting artifact bias (the possibility that the judge prefers original text over any rewrite regardless of style), we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
13	
14	\subsection{Content Preservation Verification}
15	\label{sec:nli_gate}
16	
17	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
18	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large fine-tuned on Multi-Genre NLI (MNLI; \citealp{williams2018broad}) with an entailment threshold of 0.90, selected as the threshold above which NLI performance plateaus (Appendix~\ref{app:nli_sweep}).
19	For axes that preserve information density (formality, register), we apply standard bidirectional entailment: both NLI(original $\to$ rewrite) and NLI(rewrite $\to$ original) must exceed this value.
20	For axes that inherently change information density (e.g., verbosity), bidirectional verification is inappropriate because expansion necessarily introduces new content that the original cannot entail.
21	We instead apply direction-aware verification: for expansions, only backward entailment (rewrite entails original); for compressions, only forward entailment (original entails rewrite).
22	This recovered verbosity from 65\% to 86\% pass rate without inflating the effect estimate; for formality, strict bidirectional gating is necessary (Appendix~\ref{app:gate_validation}).
23	This gating mechanism provides filtering-based confounder control \citep{veitch2020adapting} by ensuring that retained pairs differ only in style, not in content quality (validated by human annotation; \S\ref{sec:nli_validation}).
24	BERTScore serves as a supplementary monitor (mean $\Delta$BERTScore $< 0.02$ for gate-passed pairs) but does not participate in gating, as NLI provides stronger semantic equivalence guarantees than token-overlap metrics.
25	
26	\begin{figure}[t]
27	\centering
28	\includegraphics[width=\columnwidth]{figures/dag_diagram.pdf}
29	\caption{Assumed data-generating process (design rationale, not a claim of perfect identification). The rewriting mechanism $R$ targets style $S$ but may inadvertently alter content quality $Q$ (dash-dot, blocked by NLI gate) or introduce rewriting artifacts ($R \to Y$, blocked by double-rewrite control). Position bias $P \to Y$ is controlled by order swapping. The dashed $S \to Q$ path represents residual confounding (Limitations). $Y$: judge score.}
30	\label{fig:dag}
31	\end{figure}
32	
33	\subsection{Measurement Protocol}
34	\label{sec:measurement}
35	
36	Each pair that passes the NLI gate is evaluated by four target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B, and Gemini-2.5-Flash) under two complementary scoring modes.
37	In Likert mode, the judge assigns an integer score from 1 to 10 for overall quality to each text independently; the coarse integer scale is typical of deployed evaluation systems but limits measurement resolution for subtle effects.
38	In pairwise mode, the judge receives both texts as candidates A and B and makes a forced choice of which response is better, eliminating anchoring effects inherent in absolute rating.
39	This dual-mode design enables direct comparison of measurement sensitivity on identical data, isolating format-induced differences from content variation.
40	
41	To control for position bias, each pairwise comparison is evaluated twice with the presentation order swapped, which produces $n_{\text{pairs}} \times 2$ observations.
42	We apply two analysis strategies to these data.
43	For the nonparametric sign test, we retain only \emph{consistent} pairs where the judge selected the same text in both orderings.
44	For the Bradley-Terry model, we use all observations including inconsistent pairs, as the model naturally accommodates noise in individual comparisons.
45	The BT model assumes a single latent quality dimension; per-axis GEE decomposition (\S\ref{sec:direction}) complements this by separating style-specific from quality-correlated components.
46	
47	\subsection{Experimental Setup}
48	\label{sec:setup}
49	
50	We evaluate primarily on LLMBar \citep{zeng2023llmbar}, a benchmark of $n = 100$ instruction-response pairs spanning diverse task types, designed to test LLM judges' ability to distinguish response quality with human-verified quality labels.
51	LLMBar is well-suited for style sensitivity detection because its human-verified labels provide ground truth against which judge deviations can be measured, and its moderate size permits exhaustive pairwise evaluation with position control.
52	For cross-benchmark validation, we additionally evaluate on AlpacaEval \citep{dubois2023alpacafarm} and MT-Bench \citep{zheng2023judging}, targeting the strongest effects from the primary analysis to test whether style sensitivity generalizes beyond a single benchmark's distributional characteristics.
53	We select formality and verbosity as primary axes based on prior evidence that these are among the most commonly reported style sensitivities in LLM judges \citep{wu2023style,saito2023verbosity}, with register (academic vs.\ conversational) as an exploratory third axis (implementation details in Appendix~\ref{app:implementation}).
54	
55	\subsection{Design Rationale}
56	\label{sec:causal_framework}
57	
58	Figure~\ref{fig:dag} presents the assumed data-generating process.
59	CSD approximates the effect of style $S$ on judge score $Y$ while blocking confounding through content quality $Q$: the NLI gate blocks $R \to Q$, position swapping controls presentation order, and the rewrite targets a single axis.
60	The residual $S \to Q$ path (dashed in Figure~\ref{fig:dag}) represents the fundamental identification challenge: style and quality may be intrinsically correlated (e.g., formal writing may signal higher quality), which NLI gating cannot block.
61	GEE conditional decomposition (\S\ref{sec:direction}) partially addresses this by separating style-direction and originality effects, though omitted variables may confound both terms.
62	Our approach provides interventional rather than formal causal evidence (details in Appendix~\ref{app:design_rationale}).
63	A tone axis pilot (assertive $\to$ hedging) did not pass NLI gating, establishing a practical scope boundary for CSD at surface-level axes (Limitations).
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "854639cf-1c34-459b-ae6d-53fb01b3d341",
  "isSidechain": false,
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "3e733d56-c5f3-4274-b423-2030c58fbc1b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Style-Controlled Rewriting}\n\\label{sec:rewriting}\n\nWe isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis while holding content fixed, a single-axis intervention design that enables per-axis causal attribution rather than aggregate style sensitivity measurement.\nFor each text, an instruction-tuned LLM (Qwen3-32B) classifies its current style along the target axis (e.g., formal vs.\\ casual via binary classification).\nIt then rewrites the text toward the opposite pole (temperature 0.7, selected to balance diversity with coherence in pilot experiments) according to an axis-specific prompt (Appendix~\\ref{app:rewriting_prompts}).\nThis produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.\nEach operation approximates a binary intervention on a single style variable while all other axes remain fixed (Section~\\ref{sec:causal_framework}; Appendix~\\ref{app:cross_axis_contamination}).\nTo control for rewriting artifact bias (the possibility that the judge prefers original text over any rewrite regardless of style), we additionally generate a same-style double-rewrite for each text (e.g., formal $\\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \\citep{reber2025rate}.\n\n\\subsection{Content Preservation Verification}\n\\label{sec:nli_gate}\n\nStyle-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \\to Q$ path in Figure~\\ref{fig:dag}).\nTo block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large fine-tuned on Multi-Genre NLI (MNLI; \\citealp{williams2018broad}) with an entailment threshold of 0.90, selected as the threshold above which NLI performance plateaus (Appendix~\\ref{app:nli_sweep}).\nFor axes that preserve information density (formality, register), we apply standard bidirectional entailment: both NLI(original $\\to$ rewrite) and NLI(rewrite $\\to$ original) must exceed this value.\nFor axes that inherently change information density (e.g., verbosity), bidirectional verification is inappropriate because expansion necessarily introduces new content that the original cannot entail.\nWe instead apply direction-aware verification: for expansions, only backward entailment (rewrite entails original); for compressions, only forward entailment (original entails rewrite).\nThis recovered verbosity from 65\\% to 86\\% pass rate without inflating the effect estimate; for formality, strict bidirectional gating is necessary (Appendix~\\ref{app:gate_validation}).\nThis gating mechanism provides filtering-based confounder control \\citep{veitch2020adapting} by ensuring that retained pairs differ only in style, not in content quality (validated by human annotation; \\S\\ref{sec:nli_validation}).\nBERTScore serves as a supplementary monitor (mean $\\Delta$BERTScore $< 0.02$ for gate-passed pairs) but does not participate in gating, as NLI provides stronger semantic equivalence guarantees than token-overlap metrics.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/dag_diagram.pdf}\n\\caption{Assumed data-generating process (design rationale, not a claim of perfect identification). The rewriting mechanism $R$ targets style $S$ but may inadvertently alter content quality $Q$ (dash-dot, blocked by NLI gate) or introduce rewriting artifacts ($R \\to Y$, blocked by double-rewrite control). Position bias $P \\to Y$ is controlled by order swapping. The dashed $S \\to Q$ path represents residual confounding (Limitations). $Y$: judge score.}\n\\label{fig:dag}\n\\end{figure}\n\n\\subsection{Measurement Protocol}\n\\label{sec:measurement}\n\nEach pair that passes the NLI gate is evaluated by four target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B, and Gemini-2.5-Flash) under two complementary scoring modes.\nIn Likert mode, the judge assigns an integer score from 1 to 10 for overall quality to each text independently; the coarse integer scale is typical of deployed evaluation systems but limits measurement resolution for subtle effects.\nIn pairwise mode, the judge receives both texts as candidates A and B and makes a forced choice of which response is better, eliminating anchoring effects inherent in absolute rating.\nThis dual-mode design enables direct comparison of measurement sensitivity on identical data, isolating format-induced differences from content variation.\n\nTo control for position bias, each pairwise comparison is evaluated twice with the presentation order swapped, which produces $n_{\\text{pairs}} \\times 2$ observations.\nWe apply two analysis strategies to these data.\nFor the nonparametric sign test, we retain only \\emph{consistent} pairs where the judge selected the same text in both orderings.\nFor the Bradley-Terry model, we use all observations including inconsistent pairs, as the model naturally accommodates noise in individual comparisons.\nThe BT model assumes a single latent quality dimension; per-axis GEE decomposition (\\S\\ref{sec:direction}) complements this by separating style-specific from quality-correlated components.\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe evaluate primarily on LLMBar \\citep{zeng2023llmbar}, a benchmark of $n = 100$ instruction-response pairs spanning diverse task types, designed to test LLM judges' ability to distinguish response quality with human-verified quality labels.\nLLMBar is well-suited for style sensitivity detection because its human-verified labels provide ground truth against which judge deviations can be measured, and its moderate size permits exhaustive pairwise evaluation with position control.\nFor cross-benchmark validation, we additionally evaluate on AlpacaEval \\citep{dubois2023alpacafarm} and MT-Bench \\citep{zheng2023judging}, targeting the strongest effects from the primary analysis to test whether style sensitivity generalizes beyond a single benchmark's distributional characteristics.\nWe select formality and verbosity as primary axes based on prior evidence that these are among the most commonly reported style sensitivities in LLM judges \\citep{wu2023style,saito2023verbosity}, with register (academic vs.\\ conversational) as an exploratory third axis (implementation details in Appendix~\\ref{app:implementation}).\n\n\\subsection{Design Rationale}\n\\label{sec:causal_framework}\n\nFigure~\\ref{fig:dag} presents the assumed data-generating process.\nCSD approximates the effect of style $S$ on judge score $Y$ while blocking confounding through content quality $Q$: the NLI gate blocks $R \\to Q$, position swapping controls presentation order, and the rewrite targets a single axis.\nThe residual $S \\to Q$ path (dashed in Figure~\\ref{fig:dag}) represents the fundamental identification challenge: style and quality may be intrinsically correlated (e.g., formal writing may signal higher quality), which NLI gating cannot block.\nGEE conditional decomposition (\\S\\ref{sec:direction}) partially addresses this by separating style-direction and originality effects, though omitted variables may confound both terms.\nOur approach provides interventional rather than formal causal evidence (details in Appendix~\\ref{app:design_rationale}).\nA tone axis pilot (assertive $\\to$ hedging) did not pass NLI gating, establishing a practical scope boundary for CSD at surface-level axes (Limitations).\n",
      "numLines": 64,
      "startLine": 1,
      "totalLines": 64
    }
  },
  "sourceToolAssistantUUID": "854639cf-1c34-459b-ae6d-53fb01b3d341",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T06:23:55.111Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GNWshMAwv6WkRSpQXmbiYN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e733d56-c5f3-4274-b423-2030c58fbc1b",
  "isSidechain": false,
  "requestId": "req_011CbNooa53iLuiMYGs1uqp2",
  "type": "assistant",
  "uuid": "7a2f88d3-804e-41f8-8f1d-f22ca816c292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CXtb2HkNS4YKuaqB1CQkH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11954,
      "cache_read_input_tokens": 38851,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 38851,
          "cache_creation_input_tokens": 11954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11954
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

_source line 29 · 2026-05-25T06:23:55.117Z_

<details><summary>↩ Tool result · `toolu_01GNWshMAwv6WkRSpQXmbiYN`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	The primary family comprises six tests (three target judges $\times$ two axes), corrected via Holm-Bonferroni at $\alpha = 0.05$; Gemini-2.5-Flash serves as confirmatory replication and is excluded from family-wise error rate (FWER) control; as a sensitivity check, all eight tests remain significant under the expanded family (Appendix~\ref{app:holm8}).
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses use uncorrected $p$-values; confirmatory analyses (pipeline validity) are evaluated at $\alpha = 0.05$ without additional correction.
12	Bradley-Terry parameters \citep{bradley1952rank,luce1959individual} are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the \texttt{choix} Python library's default L2 regularization ($\alpha = 10^{-6}$).
13	In binary-choice BT models, independence of irrelevant alternatives (IIA) is structurally satisfied; the direction asymmetry in Appendix~\ref{app:bt_gof} (formality: formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$) reflects heterogeneous treatment effects rather than IIA violation.
14	All bootstrap confidence intervals are percentile CIs from 10{,}000 pair-level resamples with seed 42; we verify bootstrap stability by confirming that halving the resample count changes interval widths by $<$1pp.
15	GEE models use exchangeable working correlation with sandwich standard errors (robust to correlation misspecification), justified by near-zero estimated within-pair correlations ($\hat{\alpha} \in [-0.25, +0.11]$; Appendix~\ref{app:gee_diagnostics}).
16	A prospective power analysis (Appendix~\ref{app:power_analysis}) confirms that our sample sizes ($n = 86$--$88$ pairs) provide $>$90\% power to detect BT effects of the observed magnitude ($P \geq 0.63$), whereas Likert requires $4$--$206\times$ the sample size for equivalent power (Figure~\ref{fig:power_curve}).
17	
18	\paragraph{Model selection.}
19	Target judges span four architectures from independent providers: GPT-4o (\texttt{2024-08-06}; OpenAI), Qwen3-32B-Instruct (Alibaba; also serving as rewriter), Llama-3.3-70B-Instruct (Meta), and Gemini-2.5-Flash (Google).
20	This diversity guards against provider-specific artifacts in both training data and RLHF reward modeling; Claude Sonnet~4 (Anthropic) provides discriminative validity evidence (\S\ref{sec:cross_judge}), serving as a fifth judge from a provider not represented in the primary family.
21	All judges are accessed via their respective APIs with temperature 0 (deterministic decoding) and default system prompts to ensure reproducibility.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\caption{Primary results on LLMBar ($n = 88$ formality, $86$ verbosity, except where noted) across five judges and three style axes. BT $> 0.50$ indicates style preference; $\dagger$ marks Blindspot cases (BT significant, Likert not). Cross-benchmark replication in Appendix~\ref{app:cross_bench}. BT: Bradley-Terry win probability (95\% CIs in Appendix~\ref{app:bt_ci}).}
27	\label{tab:main_results}
28	\begin{tabular}{@{}llccc@{}}
29	\toprule
30	Judge & Axis & BT $P$ & Likert $d$ ($p$) & Cat.\ \\
31	\midrule
32	GPT-4o & Form.\ & .630$^{***}$ & $-$.041 (.905) & $\dagger$ \\
33	GPT-4o & Verb.\ & .760$^{***}$ & .049 (.403) & $\dagger$ \\
34	GPT-4o & Reg.\ & .570$^{\dagger}$ & .000 (.785) & $\dagger_{\text{e}}$ \\
35	\cmidrule{1-5}
36	Qwen3 & Form.\ & .665$^{***}$ & $-$.052 (.461) & $\dagger$ \\
37	Qwen3 & Form.$^b$ & .675$^{***}$ & $-$.025 (.600) & $\dagger$ \\
38	Qwen3 & Verb.\ & .773$^{***}$ & .036 (.395) & $\dagger$ \\
39	Qwen3 & Reg.\ & .553 & $-$.073 (.373) & $\dagger_{\text{e}}$ \\
40	\cmidrule{1-5}
41	Llama-70B & Form.\ & .695$^{***}$ & .010 (.534) & $\dagger$ \\
42	Llama-70B & Verb.\ & .735$^{***}$ & .020 (.284) & $\dagger$ \\
43	Llama-70B & Reg.\ & .635$^{\dagger}$ & .024 (.524) & $\dagger_{\text{e}}$ \\
44	\cmidrule{1-5}
45	Gemini & Form.\ & .574$^{*}$ & $-$.082 (.309) & $\dagger_{\text{c}}$ \\
46	Gemini & Verb.\ & .708$^{***}$ & .051 (.370) & $\dagger_{\text{c}}$ \\
47	\cmidrule{1-5}
48	Claude & Form.\ & .562 & $-$.021 (.721) & --- \\
49	Claude & Verb.\ & .541 & $-$.039 (.743) & --- \\
50	\bottomrule
51	\multicolumn{5}{@{}p{\columnwidth}@{}}{\footnotesize $^{***}\!p < 0.001$; $^{*}\!p < 0.05$ (Holm-adj.\ for primary; raw for $_{\text{c}}$). $\dagger$: Blindspot (BT sig., Likert n.s.); ---: neither sig.; $_{\text{e}}$: exploratory; $_{\text{c}}$: confirmatory. Negative $d$: styled variants scored lower.}\\
52	\multicolumn{5}{@{}p{\columnwidth}@{}}{\footnotesize $^b$ Scaled replication ($n = 355$). Qwen3 serves as both rewriter and judge; independent GPT-4o rewriter yields 22\% lower Style OR (App.~\ref{app:rewriter_indep}).}\\
53	\multicolumn{5}{@{}p{\columnwidth}@{}}{\footnotesize Form.\ direction asymmetry: formal-origin 78.8\% vs.\ casual-origin 54.5\%; GEE-adj.\ Style OR$=$2.58 ($p{=}.002$; App.~\ref{app:direction}).}
54	\end{tabular}
55	\end{table}
56	
57	
58	\begin{figure}[t]
59	\centering
60	\includegraphics[width=\columnwidth]{figures/forest_plot.pdf}
61	\caption{Bradley-Terry win probabilities across four target judges and three style axes. Filled diamonds: significant ($p < 0.05$); open diamonds: non-significant. Error bars: 95\% bootstrap CI. The dashed line at 0.50 indicates no style preference. Verbosity shows the strongest and most consistent bias across all four judges.}
62	\label{fig:forest_plot}
63	\end{figure}
64	
65	\section{Analysis}
66	\label{sec:analysis}
67	
68	
69	\subsection{The Likert Blindspot}
70	\label{sec:likert_pairwise}
71	
72	\paragraph{Head-to-head comparison with RATE.}
73	Applying RATE's Likert ATE methodology \citep{reber2025rate} to our formality style-transformed pairs yields Cohen's $d = {-}0.04$, $p = 0.91$ (non-significant, $n = 88$); pairwise comparison on identical data reveals a 63.0\% formal preference ($p = 0.0004$, Bradley-Terry on all 173 comparisons), confirmed by a consistency-filtered sign test (73.9\%, $p = 0.006$, $n = 46$ consistent pairs).
74	This is the Likert Blindspot: the same data, the same style intervention, two measurement instruments, yet one detects bias and the other does not.
75	A $4\times$ scaled replication ($n = 355$) distinguishes measurement attenuation from insufficient power: the Likert effect size shrinks to $d = {-}0.025$ (near zero) while BT remains stable at $67.5\%$ ($p < 0.0001$). If the gap were merely statistical power, $d$ would remain non-zero at larger $n$.
76	Bootstrap subsampling confirms $d$ remains near zero as $n$ grows (Appendix~\ref{app:bootstrap_attenuation}).
77	Post hoc, attenuation follows a severity spectrum: complete at moderate bias ($d \to 0$, BT 63--67\%) and partial at stronger effects (${>}60\%$ loss, BT ${>}70\%$), explaining three cross-benchmark exceptions ($\ddagger$, Table~\ref{tab:cross_bench}).
78	
79	RATE and CSD are complementary (Likert ATE vs.\ forced-choice BT); the Blindspot arises from Likert tie rates of 58--73\%, unresolved by 100-point continuous scaling (all three judges $p > 0.15$; Appendix~\ref{app:likert100}).
80	
81	
82	\paragraph{Sensitivity hierarchy across measurement methods.}
83	Seven measurement methods applied to the same formality data confirm the Blindspot is not test-specific: both pairwise methods detect the formality preference while all five Likert-based methods fail regardless of scaling assumption (interval, ordinal, or nonparametric), with verbosity showing the same pattern (Table~\ref{tab:sensitivity}, Appendix~\ref{app:sensitivity}; verbosity replication in Appendix~\ref{app:verb_sensitivity}).
84	
85	Figure~\ref{fig:power_curve} plots detection probability at observed effect magnitudes (not post-hoc power; cf.\ \citealt{hoenig2001abuse}): across six cells, Likert requires $4$--$206\times$ the current $n$ ($336$--$27{,}159$ pairs; Appendix~\ref{app:power_analysis}) to detect effects BT identifies at $p < 0.001$ with $n \leq 100$.
86	Under format equivalence, observing 8/8 primary cells as Blindspot has binomial probability $p = 0.004$; non-tie concordance (76.6\%, $p < .001$; \S\ref{sec:likert_pairwise}) provides a complementary formal test of format divergence.
87	\paragraph{Interpreting the divergence.}
88	The measurement-mode divergence admits three non-exclusive interpretations: (a)~\emph{Likert attenuation}, where tie inflation and residual signal loss reduce Likert sensitivity below detection thresholds; (b)~\emph{pairwise amplification}, where forced-choice comparison inflates micro-preferences into apparent biases \citep{jeong2025comparative}; (c)~\emph{construct divergence}, where the two formats measure different constructs (absolute quality vs.\ ordinal preference; \citealt{tripathi2025pairwise}).
89	Six experimental controls (\S\ref{sec:amplification}) bound the amplification factor but cannot eliminate it; the attenuation evidence ($d \to 0$ at $n = 355$) is necessary but not sufficient for causal identification.
90	Non-tie concordance analysis partially adjudicates: among 201 Likert non-tie pairs (pooled across judges and axes), 76.6\% agree with pairwise direction [70.3\%, 81.9\%], $p < 0.001$; point-biserial correlations are uniformly positive ($r = 0.20$--$0.45$, 7/9 significant; Appendix~\ref{app:concordance}), evidence more consistent with measurement attenuation than construct divergence, though partial construct divergence remains at weaker effect sizes.
91	Claude's benchmark-dependent profile illustrates why aggregate BT is insufficient for bias attribution: LLMBar formality shows near-null sensitivity (Style OR n.s.) while AEval verbosity reveals significant sensitivity (Style OR $= 4.76$, $p < .001$), a pattern disambiguated only by per-axis GEE decomposition (\S\ref{sec:cross_judge}; Appendix~\ref{app:claude_tost}).
92	All three interpretations converge on one practical conclusion: single-format audits risk incomplete bias coverage; the Blindspot manifests in 8/11 bias-positive cells, with three exceptions ($\ddagger$) confirming effect-size dependence.
93	For alignment pipelines where pairwise judgments serve as reward signals, this implies that biases embedded during RLHF training may go undetected by Likert-based evaluation at standard benchmark scales.
94	
95	\begin{figure}[t]
96	\centering
97	\includegraphics[width=\columnwidth]{figures/power_curve.pdf}
98	\caption{Detection probability at observed effect magnitudes. 80\% power crossings: sign test $n \approx 62$, BT $n \approx 114$, binarized Likert $n \approx 462$, Likert ATE $n \approx 1{,}473$. At typical scales ($n = 50$--$200$, shaded), pairwise methods reach 80\% power while Likert methods remain far below. At $n = 355$, Likert $d = {-}0.025$ confirms the gap is structural, not merely a power issue.}
99	\label{fig:power_curve}
100	\end{figure}
101	
102	\subsection{Per-Axis Confound Structure}
103	\label{sec:direction}
104	
105	GEE conditional decomposition \citep{liang1986gee} with exchangeable working correlation and robust standard errors separates style from originality effects (Appendix~\ref{app:direction}; model diagnostics including correlation structure robustness and interaction tests in Appendix~\ref{app:gee_diagnostics}).
106	After controlling for original preference, the formality effect remains significant (GPT-4o: OR $= 2.58$, $p = 0.002$; Qwen3-32B: OR $= 2.15$, $p < 0.0001$, $n = 355$; Llama-70B: OR $= 4.81$, $p < 0.0001$; Table~\ref{tab:gee}); the significant originality ORs confirm residual confounding.
107	For formality, both style preference and quality correlation contribute (a conditional effect); the two-predictor GEE provides a parsimonious decomposition rather than causal identification; omitted variables (text length, lexical complexity) may partly confound both terms.
108	This per-axis heterogeneity has direct implications for bias mitigation: verbosity bias can be addressed by style-level interventions (e.g., length normalization or debiased prompting), whereas formality bias requires disentangling genuine quality correlates from surface-level preferences, a fundamentally harder problem that aggregate bias metrics cannot even detect.
109	
110	\begin{table}[t]
111	\centering
112	\small
113	\caption{GEE conditional decomposition (exchangeable correlation). Style OR: style-direction odds ratio; Orig OR: original-preference odds ratio (OR $> 1$ favors original). $n{=}88$ ORs are upper-bound estimates; scaled replications ($n = 330$--$355$) show $49$--$72\%$ shrinkage \citep{nemes2009bias}. Verbosity is style-dominated; formality shows varying confound structure.}
114	\label{tab:gee}
115	\begin{tabular}{@{}llclc@{}}
116	\toprule
117	 & \multicolumn{2}{c}{Style OR} & \multicolumn{2}{c}{Originality OR} \\
118	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
119	Config & OR & $p$ & OR & $p$ \\
120	\midrule
121	Qwen3 verb.\ & 13.10 & ${<}.0001$ & 0.49 & .096 \\
122	GPT-4o verb.\ & 11.34 & ${<}.0001$ & 0.45 & .062 \\
123	Llama-70B verb.\ & 8.21 & ${<}.0001$ & 0.38 & .020 \\
124	Gemini verb.\ & 8.98 & ${<}.0001$ & 0.46 & .061 \\
125	\midrule
126	GPT-4o form.\ & 2.58 & .002 & 2.32 & .006 \\
127	Qwen3 form.\ & 4.20 & .0002 & 4.70 & .0001 \\
128	Qwen3 form.$^a$ & 2.15 & ${<}.0001$ & 4.99 & ${<}.0001$ \\
129	Llama-70B form.\ & 4.81 & ${<}.0001$ & 3.12 & .0007 \\
130	Gemini form.\ & 1.64 & .101 & 2.51 & .002 \\
131	\midrule
132	GPT-4o reg.\ & 1.88 & .029 & 2.21 & .006 \\
133	Qwen3 reg.\ & 1.91 & .046 & 5.72 & ${<}.0001$ \\
134	Llama-70B reg.\ & 3.33 & .0003 & 3.07 & .0008 \\
135	\bottomrule
136	\multicolumn{5}{l}{\footnotesize $^a$ $n = 355$; other rows: $n = 88$. 95\% CIs in Appendix.}
137	\end{tabular}
138	\end{table}
139	
140	The confound structure is consistent across all four target judges for verbosity (style-dominated at $n = 88$: Style OR $8.2$--$13.1$, Orig OR $0.38$--$0.49$; confirmed at $n = 330$: Style OR $2.5$--$4.0$); formality is conditionally style-driven in three judges but originality-dominated in Gemini; register is judge-dependent (Figure~\ref{fig:gee_decomp}).
141	Same-style double-rewrite controls confirm a rewriting artifact (Appendix~\ref{app:artifact_control}), absorbed by GEE's originality term.
142	The Gemini exception (formality Style OR $= 1.64$, n.s.) demonstrates that the decomposition is not uniformly biased toward detecting style effects; judges with weaker style sensitivity produce correspondingly weaker Style ORs.
143	
144	\begin{figure}[t]
145	\centering
146	\includegraphics[width=\columnwidth]{figures/gee_decomposition.pdf}
147	\caption{GEE conditional decomposition across four judges ($n = 88$, LLMBar). Verbosity (left) is style-dominated: Style OR $\gg 1$, Originality OR $< 1$. Formality (right) shows joint contributions from both predictors. Dashed line: OR $= 1$ (no effect). Hatched bars: Originality OR. Log scale.}
148	\label{fig:gee_decomp}
149	\end{figure}
150	
151	\paragraph{Sample-size sensitivity.}
152	At $n = 355$, the Qwen3-32B formality Style OR drops from $4.20$ to $2.15$ ($-49\%$), consistent with small-sample upward bias \citep{nemes2009bias}; the regime classification remains stable (both effects significant; Orig OR $4.70 \to 4.99$).
153	Verbosity $n = 330$ confirms 51--72\% GEE shrinkage (Style OR $2.5$--$4.0$; Appendix~\ref{app:verb_n355}), preserving the style-dominated classification; Likert begins detecting the strongest effects at this $n$, reframing the Blindspot as a $3$--$4\times$ efficiency gap rather than absolute failure.
154	This convergence at larger $n$ is practically important: it means that labs with sufficient evaluation budgets ($n > 300$) can detect the strongest biases with Likert alone, but typical benchmark sizes ($n = 50$--$200$) systematically miss them.
155	
156	\subsection{Cross-Judge and Cross-Axis Replication}
157	\label{sec:cross_judge}
158	
159	Two independent judges replicate the formality Blindspot: Qwen3-32B (BT 66.5\%, $p < 0.0001$; Likert $p = 0.461$) and Llama-3.3-70B (BT 69.5\%, $p = 0.0001$; Likert $p = 0.534$).
160	Gemini-2.5-Flash shows a weaker, originality-dominated formality pattern (confirmatory: BT 57.4\%, $p = 0.031$; Likert $d = {-}0.08$, n.s.; Style OR $= 1.64$, n.s.; Orig OR $= 2.51$, $p = 0.002$; \S\ref{sec:direction}).
161	Claude Sonnet~4 shows near-null sensitivity on LLMBar for both axes (BT $\leq 0.562$, n.s.), providing discriminative validity: CSD does not uniformly inflate bias estimates across all judges.
162	
163	Verbosity provides the strongest Blindspot: all four target judges show consistent preference (GPT-4o 76.0\%, Qwen3-32B 77.3\%, Llama-70B 73.5\%, Gemini 70.8\%; all $p \leq 0.0001$), while Likert ATE remains non-significant for all ($p = 0.284$--$0.403$).
164	GEE confirms style dominance (Style OR $8.2$--$13.1$, all $p < .0001$; Orig OR $0.38$--$0.49$; Table~\ref{tab:gee}).
165	Both rewriting directions favor verbose responses (90.7\%/80.6\%); length-controlled Style OR is unchanged ($<$2\%), and an independent GPT-4o rewriter bounds evaluator-producer overlap to a 22\% reduction (Appendix~\ref{app:rewriter_indep}).
166	Length-controlled regression confirms 60\% of the Flesch-Kincaid (FK) cross-axis effect is mediated by sentence length (Sobel $z = 2.15$, $p = .031$); under the assumed causal structure (Figure~\ref{fig:dag}), FK acts as a plausible mediator ($S \to \text{FK} \to Y$; \citealp{pearl2009causality}), yielding a direct-effect Style OR of $2.15$ for GPT-4o (total OR $= 2.70$; Appendix~\ref{app:fk_length}).
167	
168	These per-axis patterns selectively replicate across benchmarks (6/24 possible cells; Figure~\ref{fig:cross_bench_heatmap}), targeting the strongest effects: Llama-70B formality on AlpacaEval (BT 75.0\%, Style OR $= 7.64$) is strong enough for Likert detection ($\ddagger$ rows), confirming the severity spectrum.
169	The selective replication strategy prioritizes cells where effects are strongest, providing an informative lower bound on cross-benchmark generalization without requiring exhaustive evaluation of all judge--axis--benchmark combinations.
170	
171	\begin{figure}[t]
172	\centering
173	\includegraphics[width=\columnwidth]{figures/cross_benchmark_heatmap.pdf}
174	\caption{Pairwise BT win probabilities across five judges, three benchmarks, and three style axes. Bold: $p < .05$; color intensity encodes significance level. Grey $\times$: not tested. Claude cross-benchmark effects are quality-driven (\S\ref{sec:cross_judge}; Appendix~\ref{app:claude_crossbench}). Full results in Table~\ref{tab:cross_bench}.}
175	\label{fig:cross_bench_heatmap}
176	\end{figure}
177	
178	\subsection{Robustness}
179	\label{sec:nli_validation}
180	
181	\paragraph{Content preservation.}
182	Two independent annotators evaluated 100 NLI-scored pairs (50 per axis; 70 gate-passed, 30 gate-failed), confirming $98.6\%$ gate pass precision ($69/70$; Gwet's AC$_1 = 0.96$; Appendix~\ref{app:annotation_agreement}).
183	\label{sec:nli_threshold}
184	BT remains stable (${\leq}3$pp variation) across 11 NLI thresholds (Appendix~\ref{app:nli_sweep}), confirming that results are not artifacts of a particular gating stringency.
185	Annotators judged only 49--66\% of NLI-passed pairs as showing detectable style change, suggesting observed effects represent a diluted lower bound on true style sensitivity: the NLI gate retains pairs with subtle rewrites that human annotators cannot detect, yet judges still systematically prefer one variant.
186	
187	\paragraph{Detection vs.\ amplification.}
188	\label{sec:amplification}
189	\citet{jeong2025comparative} show that pairwise comparison amplifies style biases (the Comparative Trap).
190	The divergence cannot be definitively resolved without human ground-truth measurements; six controls bound amplification risk: (i)~NLI ablation reverses NLI-fail pairs (BT 41.7\%); (ii)~Claude shows benchmark-dependent sensitivity (formality Style OR n.s.; AEval verbosity OR $= 4.76$, $p < .001$); (iii)~cross-axis BT variation inconsistent with uniform amplification; (iv)~rewriting artifact absorbed by GEE; (v)~debiased prompting ($-5.2$/$-13.1$pp), bounding the amplification factor at ${\sim}9$--$17\%$ of the total BT effect; (vi)~four-architecture replication with consistent GEE structure.
191	Register is exploratory with evaluator-producer overlap and judge-dependent effects (Table~\ref{tab:gee}).
192	Same-style double-rewrite controls confirm that any residual rewriting artifact is absorbed by the GEE originality term rather than inflating the style coefficient.
193	The combination of NLI validation and amplification controls establishes that while the exact magnitude of style sensitivity remains bounded rather than point-identified, the qualitative finding (systematic style preferences invisible to Likert) is robust across judges, axes, and measurement assumptions.
194	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a2f88d3-804e-41f8-8f1d-f22ca816c292",
  "isSidechain": false,
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "a9b8d481-bec3-44fd-a104-b8dc7c35427c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\n\\subsection{Statistical Framework}\n\\label{sec:stat_framework}\n\nThe primary family comprises six tests (three target judges $\\times$ two axes), corrected via Holm-Bonferroni at $\\alpha = 0.05$; Gemini-2.5-Flash serves as confirmatory replication and is excluded from family-wise error rate (FWER) control; as a sensitivity check, all eight tests remain significant under the expanded family (Appendix~\\ref{app:holm8}).\nTable~\\ref{tab:main_results} reports both raw and adjusted $p$-values.\nAnalyses outside this grid are classified as either \\emph{exploratory} (NLI threshold sensitivity sweep, \\S\\ref{sec:nli_threshold}) or \\emph{confirmatory} (consistency filter validation, \\S\\ref{sec:consistency}).\nExploratory analyses use uncorrected $p$-values; confirmatory analyses (pipeline validity) are evaluated at $\\alpha = 0.05$ without additional correction.\nBradley-Terry parameters \\citep{bradley1952rank,luce1959individual} are estimated via spectral initialization followed by minorization-maximization \\citep{hunter2004mm}, using the \\texttt{choix} Python library's default L2 regularization ($\\alpha = 10^{-6}$).\nIn binary-choice BT models, independence of irrelevant alternatives (IIA) is structurally satisfied; the direction asymmetry in Appendix~\\ref{app:bt_gof} (formality: formal-origin 88.9\\% vs.\\ casual-origin 52.6\\%, Fisher $p = 0.015$) reflects heterogeneous treatment effects rather than IIA violation.\nAll bootstrap confidence intervals are percentile CIs from 10{,}000 pair-level resamples with seed 42; we verify bootstrap stability by confirming that halving the resample count changes interval widths by $<$1pp.\nGEE models use exchangeable working correlation with sandwich standard errors (robust to correlation misspecification), justified by near-zero estimated within-pair correlations ($\\hat{\\alpha} \\in [-0.25, +0.11]$; Appendix~\\ref{app:gee_diagnostics}).\nA prospective power analysis (Appendix~\\ref{app:power_analysis}) confirms that our sample sizes ($n = 86$--$88$ pairs) provide $>$90\\% power to detect BT effects of the observed magnitude ($P \\geq 0.63$), whereas Likert requires $4$--$206\\times$ the sample size for equivalent power (Figure~\\ref{fig:power_curve}).\n\n\\paragraph{Model selection.}\nTarget judges span four architectures from independent providers: GPT-4o (\\texttt{2024-08-06}; OpenAI), Qwen3-32B-Instruct (Alibaba; also serving as rewriter), Llama-3.3-70B-Instruct (Meta), and Gemini-2.5-Flash (Google).\nThis diversity guards against provider-specific artifacts in both training data and RLHF reward modeling; Claude Sonnet~4 (Anthropic) provides discriminative validity evidence (\\S\\ref{sec:cross_judge}), serving as a fifth judge from a provider not represented in the primary family.\nAll judges are accessed via their respective APIs with temperature 0 (deterministic decoding) and default system prompts to ensure reproducibility.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Primary results on LLMBar ($n = 88$ formality, $86$ verbosity, except where noted) across five judges and three style axes. BT $> 0.50$ indicates style preference; $\\dagger$ marks Blindspot cases (BT significant, Likert not). Cross-benchmark replication in Appendix~\\ref{app:cross_bench}. BT: Bradley-Terry win probability (95\\% CIs in Appendix~\\ref{app:bt_ci}).}\n\\label{tab:main_results}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nJudge & Axis & BT $P$ & Likert $d$ ($p$) & Cat.\\ \\\\\n\\midrule\nGPT-4o & Form.\\ & .630$^{***}$ & $-$.041 (.905) & $\\dagger$ \\\\\nGPT-4o & Verb.\\ & .760$^{***}$ & .049 (.403) & $\\dagger$ \\\\\nGPT-4o & Reg.\\ & .570$^{\\dagger}$ & .000 (.785) & $\\dagger_{\\text{e}}$ \\\\\n\\cmidrule{1-5}\nQwen3 & Form.\\ & .665$^{***}$ & $-$.052 (.461) & $\\dagger$ \\\\\nQwen3 & Form.$^b$ & .675$^{***}$ & $-$.025 (.600) & $\\dagger$ \\\\\nQwen3 & Verb.\\ & .773$^{***}$ & .036 (.395) & $\\dagger$ \\\\\nQwen3 & Reg.\\ & .553 & $-$.073 (.373) & $\\dagger_{\\text{e}}$ \\\\\n\\cmidrule{1-5}\nLlama-70B & Form.\\ & .695$^{***}$ & .010 (.534) & $\\dagger$ \\\\\nLlama-70B & Verb.\\ & .735$^{***}$ & .020 (.284) & $\\dagger$ \\\\\nLlama-70B & Reg.\\ & .635$^{\\dagger}$ & .024 (.524) & $\\dagger_{\\text{e}}$ \\\\\n\\cmidrule{1-5}\nGemini & Form.\\ & .574$^{*}$ & $-$.082 (.309) & $\\dagger_{\\text{c}}$ \\\\\nGemini & Verb.\\ & .708$^{***}$ & .051 (.370) & $\\dagger_{\\text{c}}$ \\\\\n\\cmidrule{1-5}\nClaude & Form.\\ & .562 & $-$.021 (.721) & --- \\\\\nClaude & Verb.\\ & .541 & $-$.039 (.743) & --- \\\\\n\\bottomrule\n\\multicolumn{5}{@{}p{\\columnwidth}@{}}{\\footnotesize $^{***}\\!p < 0.001$; $^{*}\\!p < 0.05$ (Holm-adj.\\ for primary; raw for $_{\\text{c}}$). $\\dagger$: Blindspot (BT sig., Likert n.s.); ---: neither sig.; $_{\\text{e}}$: exploratory; $_{\\text{c}}$: confirmatory. Negative $d$: styled variants scored lower.}\\\\\n\\multicolumn{5}{@{}p{\\columnwidth}@{}}{\\footnotesize $^b$ Scaled replication ($n = 355$). Qwen3 serves as both rewriter and judge; independent GPT-4o rewriter yields 22\\% lower Style OR (App.~\\ref{app:rewriter_indep}).}\\\\\n\\multicolumn{5}{@{}p{\\columnwidth}@{}}{\\footnotesize Form.\\ direction asymmetry: formal-origin 78.8\\% vs.\\ casual-origin 54.5\\%; GEE-adj.\\ Style OR$=$2.58 ($p{=}.002$; App.~\\ref{app:direction}).}\n\\end{tabular}\n\\end{table}\n\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/forest_plot.pdf}\n\\caption{Bradley-Terry win probabilities across four target judges and three style axes. Filled diamonds: significant ($p < 0.05$); open diamonds: non-significant. Error bars: 95\\% bootstrap CI. The dashed line at 0.50 indicates no style preference. Verbosity shows the strongest and most consistent bias across all four judges.}\n\\label{fig:forest_plot}\n\\end{figure}\n\n\\section{Analysis}\n\\label{sec:analysis}\n\n\n\\subsection{The Likert Blindspot}\n\\label{sec:likert_pairwise}\n\n\\paragraph{Head-to-head comparison with RATE.}\nApplying RATE's Likert ATE methodology \\citep{reber2025rate} to our formality style-transformed pairs yields Cohen's $d = {-}0.04$, $p = 0.91$ (non-significant, $n = 88$); pairwise comparison on identical data reveals a 63.0\\% formal preference ($p = 0.0004$, Bradley-Terry on all 173 comparisons), confirmed by a consistency-filtered sign test (73.9\\%, $p = 0.006$, $n = 46$ consistent pairs).\nThis is the Likert Blindspot: the same data, the same style intervention, two measurement instruments, yet one detects bias and the other does not.\nA $4\\times$ scaled replication ($n = 355$) distinguishes measurement attenuation from insufficient power: the Likert effect size shrinks to $d = {-}0.025$ (near zero) while BT remains stable at $67.5\\%$ ($p < 0.0001$). If the gap were merely statistical power, $d$ would remain non-zero at larger $n$.\nBootstrap subsampling confirms $d$ remains near zero as $n$ grows (Appendix~\\ref{app:bootstrap_attenuation}).\nPost hoc, attenuation follows a severity spectrum: complete at moderate bias ($d \\to 0$, BT 63--67\\%) and partial at stronger effects (${>}60\\%$ loss, BT ${>}70\\%$), explaining three cross-benchmark exceptions ($\\ddagger$, Table~\\ref{tab:cross_bench}).\n\nRATE and CSD are complementary (Likert ATE vs.\\ forced-choice BT); the Blindspot arises from Likert tie rates of 58--73\\%, unresolved by 100-point continuous scaling (all three judges $p > 0.15$; Appendix~\\ref{app:likert100}).\n\n\n\\paragraph{Sensitivity hierarchy across measurement methods.}\nSeven measurement methods applied to the same formality data confirm the Blindspot is not test-specific: both pairwise methods detect the formality preference while all five Likert-based methods fail regardless of scaling assumption (interval, ordinal, or nonparametric), with verbosity showing the same pattern (Table~\\ref{tab:sensitivity}, Appendix~\\ref{app:sensitivity}; verbosity replication in Appendix~\\ref{app:verb_sensitivity}).\n\nFigure~\\ref{fig:power_curve} plots detection probability at observed effect magnitudes (not post-hoc power; cf.\\ \\citealt{hoenig2001abuse}): across six cells, Likert requires $4$--$206\\times$ the current $n$ ($336$--$27{,}159$ pairs; Appendix~\\ref{app:power_analysis}) to detect effects BT identifies at $p < 0.001$ with $n \\leq 100$.\nUnder format equivalence, observing 8/8 primary cells as Blindspot has binomial probability $p = 0.004$; non-tie concordance (76.6\\%, $p < .001$; \\S\\ref{sec:likert_pairwise}) provides a complementary formal test of format divergence.\n\\paragraph{Interpreting the divergence.}\nThe measurement-mode divergence admits three non-exclusive interpretations: (a)~\\emph{Likert attenuation}, where tie inflation and residual signal loss reduce Likert sensitivity below detection thresholds; (b)~\\emph{pairwise amplification}, where forced-choice comparison inflates micro-preferences into apparent biases \\citep{jeong2025comparative}; (c)~\\emph{construct divergence}, where the two formats measure different constructs (absolute quality vs.\\ ordinal preference; \\citealt{tripathi2025pairwise}).\nSix experimental controls (\\S\\ref{sec:amplification}) bound the amplification factor but cannot eliminate it; the attenuation evidence ($d \\to 0$ at $n = 355$) is necessary but not sufficient for causal identification.\nNon-tie concordance analysis partially adjudicates: among 201 Likert non-tie pairs (pooled across judges and axes), 76.6\\% agree with pairwise direction [70.3\\%, 81.9\\%], $p < 0.001$; point-biserial correlations are uniformly positive ($r = 0.20$--$0.45$, 7/9 significant; Appendix~\\ref{app:concordance}), evidence more consistent with measurement attenuation than construct divergence, though partial construct divergence remains at weaker effect sizes.\nClaude's benchmark-dependent profile illustrates why aggregate BT is insufficient for bias attribution: LLMBar formality shows near-null sensitivity (Style OR n.s.) while AEval verbosity reveals significant sensitivity (Style OR $= 4.76$, $p < .001$), a pattern disambiguated only by per-axis GEE decomposition (\\S\\ref{sec:cross_judge}; Appendix~\\ref{app:claude_tost}).\nAll three interpretations converge on one practical conclusion: single-format audits risk incomplete bias coverage; the Blindspot manifests in 8/11 bias-positive cells, with three exceptions ($\\ddagger$) confirming effect-size dependence.\nFor alignment pipelines where pairwise judgments serve as reward signals, this implies that biases embedded during RLHF training may go undetected by Likert-based evaluation at standard benchmark scales.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/power_curve.pdf}\n\\caption{Detection probability at observed effect magnitudes. 80\\% power crossings: sign test $n \\approx 62$, BT $n \\approx 114$, binarized Likert $n \\approx 462$, Likert ATE $n \\approx 1{,}473$. At typical scales ($n = 50$--$200$, shaded), pairwise methods reach 80\\% power while Likert methods remain far below. At $n = 355$, Likert $d = {-}0.025$ confirms the gap is structural, not merely a power issue.}\n\\label{fig:power_curve}\n\\end{figure}\n\n\\subsection{Per-Axis Confound Structure}\n\\label{sec:direction}\n\nGEE conditional decomposition \\citep{liang1986gee} with exchangeable working correlation and robust standard errors separates style from originality effects (Appendix~\\ref{app:direction}; model diagnostics including correlation structure robustness and interaction tests in Appendix~\\ref{app:gee_diagnostics}).\nAfter controlling for original preference, the formality effect remains significant (GPT-4o: OR $= 2.58$, $p = 0.002$; Qwen3-32B: OR $= 2.15$, $p < 0.0001$, $n = 355$; Llama-70B: OR $= 4.81$, $p < 0.0001$; Table~\\ref{tab:gee}); the significant originality ORs confirm residual confounding.\nFor formality, both style preference and quality correlation contribute (a conditional effect); the two-predictor GEE provides a parsimonious decomposition rather than causal identification; omitted variables (text length, lexical complexity) may partly confound both terms.\nThis per-axis heterogeneity has direct implications for bias mitigation: verbosity bias can be addressed by style-level interventions (e.g., length normalization or debiased prompting), whereas formality bias requires disentangling genuine quality correlates from surface-level preferences, a fundamentally harder problem that aggregate bias metrics cannot even detect.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{GEE conditional decomposition (exchangeable correlation). Style OR: style-direction odds ratio; Orig OR: original-preference odds ratio (OR $> 1$ favors original). $n{=}88$ ORs are upper-bound estimates; scaled replications ($n = 330$--$355$) show $49$--$72\\%$ shrinkage \\citep{nemes2009bias}. Verbosity is style-dominated; formality shows varying confound structure.}\n\\label{tab:gee}\n\\begin{tabular}{@{}llclc@{}}\n\\toprule\n & \\multicolumn{2}{c}{Style OR} & \\multicolumn{2}{c}{Originality OR} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nConfig & OR & $p$ & OR & $p$ \\\\\n\\midrule\nQwen3 verb.\\ & 13.10 & ${<}.0001$ & 0.49 & .096 \\\\\nGPT-4o verb.\\ & 11.34 & ${<}.0001$ & 0.45 & .062 \\\\\nLlama-70B verb.\\ & 8.21 & ${<}.0001$ & 0.38 & .020 \\\\\nGemini verb.\\ & 8.98 & ${<}.0001$ & 0.46 & .061 \\\\\n\\midrule\nGPT-4o form.\\ & 2.58 & .002 & 2.32 & .006 \\\\\nQwen3 form.\\ & 4.20 & .0002 & 4.70 & .0001 \\\\\nQwen3 form.$^a$ & 2.15 & ${<}.0001$ & 4.99 & ${<}.0001$ \\\\\nLlama-70B form.\\ & 4.81 & ${<}.0001$ & 3.12 & .0007 \\\\\nGemini form.\\ & 1.64 & .101 & 2.51 & .002 \\\\\n\\midrule\nGPT-4o reg.\\ & 1.88 & .029 & 2.21 & .006 \\\\\nQwen3 reg.\\ & 1.91 & .046 & 5.72 & ${<}.0001$ \\\\\nLlama-70B reg.\\ & 3.33 & .0003 & 3.07 & .0008 \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^a$ $n = 355$; other rows: $n = 88$. 95\\% CIs in Appendix.}\n\\end{tabular}\n\\end{table}\n\nThe confound structure is consistent across all four target judges for verbosity (style-dominated at $n = 88$: Style OR $8.2$--$13.1$, Orig OR $0.38$--$0.49$; confirmed at $n = 330$: Style OR $2.5$--$4.0$); formality is conditionally style-driven in three judges but originality-dominated in Gemini; register is judge-dependent (Figure~\\ref{fig:gee_decomp}).\nSame-style double-rewrite controls confirm a rewriting artifact (Appendix~\\ref{app:artifact_control}), absorbed by GEE's originality term.\nThe Gemini exception (formality Style OR $= 1.64$, n.s.) demonstrates that the decomposition is not uniformly biased toward detecting style effects; judges with weaker style sensitivity produce correspondingly weaker Style ORs.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/gee_decomposition.pdf}\n\\caption{GEE conditional decomposition across four judges ($n = 88$, LLMBar). Verbosity (left) is style-dominated: Style OR $\\gg 1$, Originality OR $< 1$. Formality (right) shows joint contributions from both predictors. Dashed line: OR $= 1$ (no effect). Hatched bars: Originality OR. Log scale.}\n\\label{fig:gee_decomp}\n\\end{figure}\n\n\\paragraph{Sample-size sensitivity.}\nAt $n = 355$, the Qwen3-32B formality Style OR drops from $4.20$ to $2.15$ ($-49\\%$), consistent with small-sample upward bias \\citep{nemes2009bias}; the regime classification remains stable (both effects significant; Orig OR $4.70 \\to 4.99$).\nVerbosity $n = 330$ confirms 51--72\\% GEE shrinkage (Style OR $2.5$--$4.0$; Appendix~\\ref{app:verb_n355}), preserving the style-dominated classification; Likert begins detecting the strongest effects at this $n$, reframing the Blindspot as a $3$--$4\\times$ efficiency gap rather than absolute failure.\nThis convergence at larger $n$ is practically important: it means that labs with sufficient evaluation budgets ($n > 300$) can detect the strongest biases with Likert alone, but typical benchmark sizes ($n = 50$--$200$) systematically miss them.\n\n\\subsection{Cross-Judge and Cross-Axis Replication}\n\\label{sec:cross_judge}\n\nTwo independent judges replicate the formality Blindspot: Qwen3-32B (BT 66.5\\%, $p < 0.0001$; Likert $p = 0.461$) and Llama-3.3-70B (BT 69.5\\%, $p = 0.0001$; Likert $p = 0.534$).\nGemini-2.5-Flash shows a weaker, originality-dominated formality pattern (confirmatory: BT 57.4\\%, $p = 0.031$; Likert $d = {-}0.08$, n.s.; Style OR $= 1.64$, n.s.; Orig OR $= 2.51$, $p = 0.002$; \\S\\ref{sec:direction}).\nClaude Sonnet~4 shows near-null sensitivity on LLMBar for both axes (BT $\\leq 0.562$, n.s.), providing discriminative validity: CSD does not uniformly inflate bias estimates across all judges.\n\nVerbosity provides the strongest Blindspot: all four target judges show consistent preference (GPT-4o 76.0\\%, Qwen3-32B 77.3\\%, Llama-70B 73.5\\%, Gemini 70.8\\%; all $p \\leq 0.0001$), while Likert ATE remains non-significant for all ($p = 0.284$--$0.403$).\nGEE confirms style dominance (Style OR $8.2$--$13.1$, all $p < .0001$; Orig OR $0.38$--$0.49$; Table~\\ref{tab:gee}).\nBoth rewriting directions favor verbose responses (90.7\\%/80.6\\%); length-controlled Style OR is unchanged ($<$2\\%), and an independent GPT-4o rewriter bounds evaluator-producer overlap to a 22\\% reduction (Appendix~\\ref{app:rewriter_indep}).\nLength-controlled regression confirms 60\\% of the Flesch-Kincaid (FK) cross-axis effect is mediated by sentence length (Sobel $z = 2.15$, $p = .031$); under the assumed causal structure (Figure~\\ref{fig:dag}), FK acts as a plausible mediator ($S \\to \\text{FK} \\to Y$; \\citealp{pearl2009causality}), yielding a direct-effect Style OR of $2.15$ for GPT-4o (total OR $= 2.70$; Appendix~\\ref{app:fk_length}).\n\nThese per-axis patterns selectively replicate across benchmarks (6/24 possible cells; Figure~\\ref{fig:cross_bench_heatmap}), targeting the strongest effects: Llama-70B formality on AlpacaEval (BT 75.0\\%, Style OR $= 7.64$) is strong enough for Likert detection ($\\ddagger$ rows), confirming the severity spectrum.\nThe selective replication strategy prioritizes cells where effects are strongest, providing an informative lower bound on cross-benchmark generalization without requiring exhaustive evaluation of all judge--axis--benchmark combinations.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/cross_benchmark_heatmap.pdf}\n\\caption{Pairwise BT win probabilities across five judges, three benchmarks, and three style axes. Bold: $p < .05$; color intensity encodes significance level. Grey $\\times$: not tested. Claude cross-benchmark effects are quality-driven (\\S\\ref{sec:cross_judge}; Appendix~\\ref{app:claude_crossbench}). Full results in Table~\\ref{tab:cross_bench}.}\n\\label{fig:cross_bench_heatmap}\n\\end{figure}\n\n\\subsection{Robustness}\n\\label{sec:nli_validation}\n\n\\paragraph{Content preservation.}\nTwo independent annotators evaluated 100 NLI-scored pairs (50 per axis; 70 gate-passed, 30 gate-failed), confirming $98.6\\%$ gate pass precision ($69/70$; Gwet's AC$_1 = 0.96$; Appendix~\\ref{app:annotation_agreement}).\n\\label{sec:nli_threshold}\nBT remains stable (${\\leq}3$pp variation) across 11 NLI thresholds (Appendix~\\ref{app:nli_sweep}), confirming that results are not artifacts of a particular gating stringency.\nAnnotators judged only 49--66\\% of NLI-passed pairs as showing detectable style change, suggesting observed effects represent a diluted lower bound on true style sensitivity: the NLI gate retains pairs with subtle rewrites that human annotators cannot detect, yet judges still systematically prefer one variant.\n\n\\paragraph{Detection vs.\\ amplification.}\n\\label{sec:amplification}\n\\citet{jeong2025comparative} show that pairwise comparison amplifies style biases (the Comparative Trap).\nThe divergence cannot be definitively resolved without human ground-truth measurements; six controls bound amplification risk: (i)~NLI ablation reverses NLI-fail pairs (BT 41.7\\%); (ii)~Claude shows benchmark-dependent sensitivity (formality Style OR n.s.; AEval verbosity OR $= 4.76$, $p < .001$); (iii)~cross-axis BT variation inconsistent with uniform amplification; (iv)~rewriting artifact absorbed by GEE; (v)~debiased prompting ($-5.2$/$-13.1$pp), bounding the amplification factor at ${\\sim}9$--$17\\%$ of the total BT effect; (vi)~four-architecture replication with consistent GEE structure.\nRegister is exploratory with evaluator-producer overlap and judge-dependent effects (Table~\\ref{tab:gee}).\nSame-style double-rewrite controls confirm that any residual rewriting artifact is absorbed by the GEE originality term rather than inflating the style coefficient.\nThe combination of NLI validation and amplification controls establishes that while the exact magnitude of style sensitivity remains bounded rather than point-identified, the qualitative finding (systematic style preferences invisible to Likert) is robust across judges, axes, and measurement assumptions.\n",
      "numLines": 194,
      "startLine": 1,
      "totalLines": 194
    }
  },
  "sourceToolAssistantUUID": "7a2f88d3-804e-41f8-8f1d-f22ca816c292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T06:23:55.640Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hsc18W3u2GWNdpdBwsmE3X`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9b8d481-bec3-44fd-a104-b8dc7c35427c",
  "isSidechain": false,
  "requestId": "req_011CbNooa53iLuiMYGs1uqp2",
  "type": "assistant",
  "uuid": "8d1af41b-8175-457c-bf9b-ffa06549290f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CXtb2HkNS4YKuaqB1CQkH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11954,
      "cache_read_input_tokens": 38851,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 38851,
          "cache_creation_input_tokens": 11954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11954
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

_source line 31 · 2026-05-25T06:23:55.646Z_

<details><summary>↩ Tool result · `toolu_01Hsc18W3u2GWNdpdBwsmE3X`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	CSD yields two findings: the \emph{Likert Blindspot} (divergent pairwise/Likert verdicts in 8/8 primary and 6/24 cross-benchmark cells; $d \!\to\! 0$ at $n{=}355$) and per-axis confound structures via GEE (verbosity style-dominated, formality conditional, register judge-dependent); concordance ($p < .001$) favors attenuation over divergence.
4	These results carry a practical recommendation: style-bias audits that rely exclusively on Likert scoring risk false negatives at typical benchmark sizes ($n < 200$); pairing with pairwise evaluation or increasing $n$ by $3$--$4\times$ provides more complete coverage.
5	For alignment pipelines, the per-axis confound structure implies that verbosity preferences in RLHF reward signals are predominantly style-driven, while formality preferences partially reflect genuine quality differences, a distinction invisible without per-axis decomposition and undetectable by aggregate bias metrics.
6	CSD generalizes to any surface-level axis with content-preserving rewrites; deeper axes (e.g., reasoning depth, factual density) that resist content-neutral manipulation remain open for future work.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d1af41b-8175-457c-bf9b-ffa06549290f",
  "isSidechain": false,
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "0ab977d6-86ec-4855-866d-a8cf23485dfa",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\nCSD yields two findings: the \\emph{Likert Blindspot} (divergent pairwise/Likert verdicts in 8/8 primary and 6/24 cross-benchmark cells; $d \\!\\to\\! 0$ at $n{=}355$) and per-axis confound structures via GEE (verbosity style-dominated, formality conditional, register judge-dependent); concordance ($p < .001$) favors attenuation over divergence.\nThese results carry a practical recommendation: style-bias audits that rely exclusively on Likert scoring risk false negatives at typical benchmark sizes ($n < 200$); pairing with pairwise evaluation or increasing $n$ by $3$--$4\\times$ provides more complete coverage.\nFor alignment pipelines, the per-axis confound structure implies that verbosity preferences in RLHF reward signals are predominantly style-driven, while formality preferences partially reflect genuine quality differences, a distinction invisible without per-axis decomposition and undetectable by aggregate bias metrics.\nCSD generalizes to any surface-level axis with content-preserving rewrites; deeper axes (e.g., reasoning depth, factual density) that resist content-neutral manipulation remain open for future work.\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  },
  "sourceToolAssistantUUID": "8d1af41b-8175-457c-bf9b-ffa06549290f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T06:23:56.170Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Eey2ZrQuNMqP7FNCxZ3Yqq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ab977d6-86ec-4855-866d-a8cf23485dfa",
  "isSidechain": false,
  "requestId": "req_011CbNooa53iLuiMYGs1uqp2",
  "type": "assistant",
  "uuid": "fe4c1103-4ce0-41c3-af12-f31b5d8aa2f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CXtb2HkNS4YKuaqB1CQkH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11954,
      "cache_read_input_tokens": 38851,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 38851,
          "cache_creation_input_tokens": 11954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11954
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

_source line 33 · 2026-05-25T06:23:56.448Z_

<details><summary>↩ Tool result · `toolu_01Eey2ZrQuNMqP7FNCxZ3Yqq`</summary>

```text
1	\appendix
2	
3	\noindent\emph{Organization: design rationale (A$^*$), confound analysis (A--B), model diagnostics (C), independence tests (D), gate validation (E--F), equivalence testing (G), statistical details (H--K), sensitivity analyses (L--N), artifact controls (O), implementation (P), multiplicity (Q), cross-axis contamination (R), FK length-control (R$'$), human annotation agreement (S), cross-benchmark replication (T), Claude cross-benchmark (U), rewriting prompts (V), non-tie concordance (W).}
4	
5	\section{Design Rationale}
6	\label{app:design_rationale}
7	
8	Three variables govern the observed judge score $Y$: the style attribute $S$ (e.g., formality), the original content quality $Q$, and the judge's internal scoring function.
9	Both $S$ and $Q$ causally influence $Y$; the goal of CSD is to approximate the effect $S \to Y$ while blocking confounding through $Q$.
10	Style-controlled rewriting generates a text pair that differs along a single style axis, but any rewriting operation risks inadvertently altering content quality ($R \to Q$).
11	The NLI gate (\S\ref{sec:nli_gate}) blocks this path, yielding a controlled estimate of the $S \to Y$ effect.
12	Our approach provides interventional rather than formal causal evidence: we do not claim that the DAG in Figure~\ref{fig:dag} is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework.
13	``Controlled'' in this context refers to experimentally controlled rewriting conditions, not formal causal identification in the potential-outcomes sense.
14	Our identification rests on three operational assumptions: (i)~the NLI gate approximates content preservation, blocking the $R \to Q$ path; (ii)~position swapping controls for presentation-order effects; and (iii)~the style rewrite introduces no systematic differences beyond the target axis.
15	
16	\section{Direction Asymmetry and Quality Confounding}
17	\label{app:direction}
18	
19	The formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\% of formal-is-rewrite pairs ($p = 0.001$) but only 54.5\% of casual-is-rewrite pairs ($p = 0.83$).
20	This asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.
21	To quantify this, we fit a GEE logistic model (exchangeable correlation) with both formality and original-preference as predictors.
22	After controlling for original preference, the formality effect remains significant ($\text{OR} = 2.58$, $p = 0.002$), and the original-preference effect is also significant ($\text{OR} = 2.32$, $p = 0.006$).
23	The formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.
24	
25	At $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exceeded the GPT-4o estimate ($2.58$), but a scaled replication ($n = 355$) corrects this to $2.15$ ($p < 0.0001$), comparable to GPT-4o and consistent with small-sample upward bias rather than evaluator-producer inflation of the style effect.
26	The originality confound remains stronger ($4.99$ vs.\ $2.32$), consistent with evaluator-producer bias inflating the originality component (Limitations).
27	The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.
28	
29	The NLI gate blocks \emph{content} changes but cannot block quality perception shifts that are themselves mediated by style---a fundamental identifiability limit of any text-rewriting approach.
30	
31	\section{Consistency Filter Robustness}
32	\label{sec:consistency}
33	
34	The position-consistency filter retains 55 of 98 valid pairs (56.1\%); consistent and inconsistent groups show no significant differences across four covariates (NLI score $p = 0.824$, BERTScore $p = 0.12$, text length $p = 0.137$, length diff $p = 0.715$), indicating selection on judge decisiveness rather than text properties.
35	The BT model using all 173 comparisons including inconsistent pairs yields 63.0\% ($p = 0.0004$), consistent with the filtered sign test (73.9\%, $p = 0.006$), confirming no systematic bias from the filter.
36	Chi-squared tests confirm that NLI gate pass/reject status is independent of source category ($\chi^2 = 1.30$, $p = .73$), original formality ($p = .37$), and gold label ($p = 1.0$), indicating no systematic selection bias along these dimensions.
37	
38	Verbosity gate-passed pairs are significantly longer than rejected pairs (token count KS $p = 0.003$; sentence length MWU $p = 0.006$).
39	This reflects the gate's content-preservation mandate: verbosity transformations on shorter texts alter content ratios more substantially, causing correct NLI rejection.
40	Length-controlled GEE analysis (\S\ref{sec:direction}; Style OR change ${<}2\%$) confirms this selection does not confound the verbosity effect.
41	
42	\section{GEE Model Diagnostics}
43	\label{app:gee_diagnostics}
44	
45	\paragraph{Correlation structure robustness.}
46	Table~\ref{tab:gee_corr} compares exchangeable and independence working correlation structures across all nine judge$\times$axis cells.
47	The two structures yield virtually identical results: $|\Delta\text{QIC}| < 0.001$ and maximum coefficient change ${<}0.02$ in every cell, with estimated within-pair correlations $\hat{\alpha} \in [-0.25, +0.11]$.
48	All GEE results reported in the main text are therefore robust to correlation structure specification.
49	
50	\begin{table}[h]
51	\centering
52	\small
53	\caption{GEE correlation structure comparison across nine judge$\times$axis cells.}
54	\label{tab:gee_corr}
55	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}lcccc@{}}
56	\toprule
57	Config & Exch.\ QIC & Indep.\ QIC & $|\Delta\text{QIC}|$ & Max$|\Delta\text{Coef}|$ \\
58	\midrule
59	GPT-4o form.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
60	Qwen3 form.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
61	Llama-70B form.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
62	GPT-4o verb.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
63	Qwen3 verb.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
64	Llama-70B verb.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
65	GPT-4o reg.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
66	Qwen3 reg.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
67	Llama-70B reg.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
68	\bottomrule
69	\multicolumn{5}{l}{\footnotesize Absolute QIC values omitted; only $|\Delta\text{QIC}|$ is reported.}
70	\end{tabular}}
71	\end{table}
72	
73	\paragraph{Interaction test.}
74	Adding a Style$\times$Originality interaction term to the additive GEE specification yields no significant interactions in any of the nine judge$\times$axis cells (all $p > 0.13$, range $0.14$--$0.96$), confirming that the additive model is the correct specification and that regime classifications are robust to model specification.
75	Table~\ref{tab:gee-interaction} reports interaction terms; none are significant, confirming the additive specification.
76	
77	\begin{table}[h]
78	\centering
79	\small
80	\caption{GEE Style $\times$ Originality interaction terms. None are significant ($p > 0.13$), confirming the additive model specification.}
81	\label{tab:gee-interaction}
82	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}llccc@{}}
83	\toprule
84	Judge & Axis & Interaction OR & 95\% CI & $p$ \\
85	\midrule
86	GPT-4o & Formality & 0.661 & [0.18, 2.38] & .527 \\
87	GPT-4o & Verbosity & 1.269 & [0.37, 4.34] & .705 \\
88	GPT-4o & Register & 2.601 & [0.74, 9.15] & .136 \\
89	Qwen3-32B & Formality & 0.518 & [0.14, 1.89] & .320 \\
90	Qwen3-32B & Verbosity & 0.450 & [0.13, 1.62] & .221 \\
91	Qwen3-32B & Register & 0.555 & [0.15, 2.08] & .383 \\
92	Llama-70B & Formality & 0.968 & [0.25, 3.78] & .963 \\
93	Llama-70B & Verbosity & 1.103 & [0.34, 3.58] & .870 \\
94	\bottomrule
95	\end{tabular}}
96	\end{table}
97	
98	\paragraph{95\% confidence intervals.}
99	Table~\ref{tab:gee_ci} reports 95\% CIs for all GEE odds ratios in Table~\ref{tab:gee}.
100	
101	\begin{table}[h]
102	\centering
103	\small
104	\caption{95\% CIs for GEE conditional decomposition (Table~\ref{tab:gee}).}
105	\label{tab:gee_ci}
106	\begin{tabular}{@{}lcc@{}}
107	\toprule
108	Config & Style OR [CI] & Orig OR [CI] \\
109	\midrule
110	Qwen3 verb.\ & 13.10 [5.62, 30.55] & 0.49 [0.21, 1.14] \\
111	GPT-4o verb.\ & 11.34 [4.93, 26.10] & 0.45 [0.20, 1.04] \\
112	Llama-70B verb.\ & 8.21 [3.62, 18.65] & 0.38 [0.17, 0.86] \\
113	Gemini verb.\ & 8.98 [3.68, 21.94] & 0.46 [0.20, 1.04] \\
114	GPT-4o form.\ & 2.58 [1.41, 4.73] & 2.32 [1.27, 4.26] \\
115	Qwen3 form.\ & 4.20 [1.99, 8.87] & 4.70 [2.22, 9.96] \\
116	Qwen3 form.$^a$ & 2.15 [1.46, 3.16] & 4.99 [3.40, 7.34] \\
117	Llama-70B form.\ & 4.81 [2.48, 9.33] & 3.12 [1.61, 6.04] \\
118	Gemini form.\ & 1.64 [0.91, 2.98] & 2.51 [1.39, 4.54] \\
119	GPT-4o reg.\ & 1.88 [1.08, 3.28] & 2.21 [1.26, 3.86] \\
120	Qwen3 reg.\ & 1.91 [1.01, 3.58] & 5.72 [3.02, 10.82] \\
121	Llama-70B reg.\ & 3.33 [1.73, 6.42] & 3.07 [1.60, 5.92] \\
122	\bottomrule
123	\multicolumn{3}{l}{\footnotesize $^a$ $n = 355$; other rows: $n = 88$.}
124	\end{tabular}
125	\end{table}
126	
127	\section{Rewriter Independence}
128	\label{app:rewriter_indep}
129	
130	Evaluator-producer overlap is limited to Qwen3-32B (rewriter $=$ judge); the independence test below bounds this to a 22\% Style OR reduction. The other three target judges (GPT-4o, Llama-70B, Gemini) use a different rewriter and are not subject to this confound.
131	
132	To test whether the Blindspot depends on the rewriter's identity, we replace Qwen3-32B with GPT-4o as rewriter while keeping Qwen3-32B as judge.
133	
134	\paragraph{Verbosity (Table~\ref{tab:rewriter_indep}).}
135	The Style OR decreases by $22\%$ ($13.10 \to 10.17$), bounding evaluator-producer inflation of the style effect; the pure-style pattern (Originality n.s.) and Blindspot (BT significant, Likert n.s.) both persist.
136	
137	\begin{table}[h]
138	\centering
139	\small
140	\caption{Rewriter independence test: verbosity axis, Qwen3-32B judge. GPT-4o rewriter eliminates evaluator-producer overlap while preserving the Blindspot.}
141	\label{tab:rewriter_indep}
142	\begin{tabular}{lcc}
143	\toprule
144	 & GPT-4o Rewriter & Qwen3 Rewriter \\
145	\midrule
146	NLI pass rate & 81/100 (81\%) & 86/100 (86\%) \\
147	BT $P$ [95\% CI] & .735 [.654, .809] & .773 [.703, .843] \\
148	Likert ATE ($p$) & .000 (.838) & ${\sim}$0 (.179) \\
149	Blindspot & Yes & Yes \\
150	GEE Style OR ($p$) & 10.17 (${<}.0001$) & 13.10 (${<}.0001$) \\
151	GEE Orig OR ($p$) & 1.61 (n.s.) & 0.49 (n.s.) \\
152	\bottomrule
153	\end{tabular}
154	\end{table}
155	
156	\paragraph{Formality (Table~\ref{tab:rewriter_indep_form}).}
157	GPT-4o rewriter produces formality-manipulated pairs yielding BT $64.4\%$ $[56.1, 72.8]$, statistically indistinguishable from the Qwen3-32B baseline ($66.5\%$ $[58.5, 73.9]$; $\Delta = -2.1$pp).
158	The Likert Blindspot replicates with the independent rewriter ($p = 0.184$, n.s.).
159	
160	\begin{table}[h]
161	\centering
162	\small
163	\caption{Rewriter independence test: formality axis, Qwen3-32B judge.}
164	\label{tab:rewriter_indep_form}
165	\begin{tabular}{lcc}
166	\toprule
167	 & GPT-4o Rewriter & Qwen3 Rewriter \\
168	\midrule
169	NLI pass rate & 90/100 (90\%) & 88/100 (88\%) \\
170	BT $P$ [95\% CI] & .644 [.561, .728] & .665 [.585, .739] \\
171	Likert $d$ ($p$) & $-$.081 (.184) & .011 (.908) \\
172	Blindspot & Yes & Yes \\
173	\bottomrule
174	\end{tabular}
175	\end{table}
176	
177	\section{NLI Threshold Sensitivity Sweep}
178	\label{app:nli_sweep}
179	
180	Table~\ref{tab:nli_sweep} reports BT win probabilities across 11 NLI entailment thresholds for all four judge$\times$axis configurations.
181	All 44 combinations are significant ($p < 0.05$), and within each configuration BT varies by at most 3pp, ruling out threshold selection bias.
182	The stability reflects the bimodal NLI score distribution: most pairs score above 0.95 or below 0.30, so thresholds between 0.50 and 0.95 admit nearly identical pair sets.
183	
184	\begin{table}[h]
185	\centering
186	\small
187	\caption{BT win probability across NLI thresholds. All 44 cells significant ($p < 0.05$). $n$: pairs passing threshold.}
188	\label{tab:nli_sweep}
189	\begin{tabular}{@{}rcccc@{}}
190	\toprule
191	Thresh & \multicolumn{2}{c}{Formality BT} & \multicolumn{2}{c}{Verbosity BT} \\
192	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
193	 & Qwen3 & GPT-4o & Qwen3 & GPT-4o \\
194	\midrule
195	.50 & .648 & .615 & .770 & .768 \\
196	.55 & .648 & .615 & .770 & .768 \\
197	.60 & .656 & .621 & .770 & .768 \\
198	.65 & .656 & .621 & .767 & .766 \\
199	.70 & .657 & .623 & .767 & .766 \\
200	.75 & .657 & .623 & .773 & .760 \\
201	.80 & .657 & .623 & .773 & .760 \\
202	.85 & .657 & .623 & .773 & .760 \\
203	.90 & .665 & .630 & .773 & .760 \\
204	.95 & .653 & .629 & .765 & .752 \\
205	.98 & .649 & .642 & .771 & .769 \\
206	\bottomrule
207	\end{tabular}
208	\end{table}
209	
210	\section{Direction-Aware Gate Validation}
211	\label{app:gate_validation}
212	
213	For verbosity, the direction-aware NLI gate admits 21 additional pairs (32\%) compared to strict bidirectional verification.
214	The two groups show no significant difference in BT win probability (78.5\% bidirectional vs.\ 73.8\% DA-only; permutation $p = .663$; $\Delta = {-}1.1$pp, 95\% CI $[{-}5.6, {+}3.0]$) or Likert $d$ ($0.038$ vs.\ $0.029$).
215	Both groups exhibit the Blindspot pattern (BT significant, Likert NS), confirming that direction-aware gating recovers valid pairs without inflating the effect or introducing selection bias.
216	Cross-judge validation on all 21 direction-aware pairs confirms this: Fisher exact tests comparing BT estimates between direction-aware and bidirectional-pass subsets are non-significant for all five judges ($p > 0.66$), indicating that the DA-gate does not differentially affect any judge's preference signal.
217	For formality, strict bidirectional verification is appropriate: a relaxed (direction-aware) gate would admit 9 additional pairs with reversed preference (BT 33.4\%), indicating content preservation failure rather than genuine style preference.
218	This asymmetry empirically justifies the axis-dependent gating strategy described in Section~\ref{sec:nli_gate}.
219	
220	\section{Claude Sonnet 4 Equivalence Testing}
221	\label{app:claude_tost}
222	
223	Claude Sonnet~4 exhibits benchmark-dependent sensitivity ($n = 88$; LLMBar BT 56.2\%/54.1\%, $p = 0.091$/$0.284$).
224	Formal equivalence testing \citep[TOST;][]{lakens2017equivalence} yields margin-dependent conclusions (Table~\ref{tab:tost_sensitivity}): per-axis equivalence is confirmed at $\Delta = 15$pp ($p = .010$), corresponding to a BT threshold of 65\%.
225	At $\Delta = 10$pp, per-axis TOST is not significant ($p = .156$, power $\approx 42\%$).
226	Pooling both axes ($n = 174$, BT $= 55.17\%$) achieves equivalence at $\Delta = 12$pp ($p = .035$) but not at $\Delta = 10$pp ($p = .100$), tightening the bound on Claude's style sensitivity.
227	We adopt $\Delta = 12$pp as it corresponds to a small effect (Cohen's $h = 0.24$), below which style sensitivity is unlikely to materially affect downstream RLHF reward modeling; a 12pp BT shift means ${\sim}12\%$ of preference pairs change direction. This is also the smallest margin at which pooled significance is achieved.
228	We report all tested margins for transparency.
229	
230	\begin{table}[h]
231	\centering
232	\small
233	\caption{TOST equivalence sensitivity for Claude. Per-axis: formality only (BT $= 0.562$, $n = 88$). Pooled: both axes combined ($n = 174$).}
234	\label{tab:tost_sensitivity}
235	\begin{tabular}{ccl}
236	\toprule
237	$\Delta$ (pp) & $p$ & Result \\
238	\midrule
239	5 & .626 & Not equivalent (per-axis) \\
240	10 & .156 & Not equivalent (per-axis) \\
241	10 & .100 & Not equivalent (pooled) \\
242	12 & .035 & Equivalent (pooled) \\
243	15 & .010 & Equivalent (per-axis) \\
244	20 & .0001 & Equivalent (per-axis) \\
245	\bottomrule
246	\end{tabular}
247	\end{table}
248	
249	\paragraph{Bayesian equivalence.}
250	We complement frequentist TOST with Bayesian equivalence testing to quantify evidence strength for the null hypothesis.
251	Table~\ref{tab:bayesian_equiv} reports BF$_{01}$ (evidence for null over alternative) under three half-normal prior scales.
252	
253	\begin{table}[h]
254	\centering
255	\small
256	\caption{Bayesian equivalence (BF$_{01}$) for Claude Sonnet~4 Likert ATE. BF$_{01} > 3$: moderate evidence for null; $1$--$3$: anecdotal; $< 1$: favors alternative.}
257	\label{tab:bayesian_equiv}
258	\begin{tabular}{@{}lccc@{}}
259	\toprule
260	Data & $\sigma = 0.3$ & $\sigma = 0.5$ & $\sigma = 1.0$ \\
261	\midrule
262	Pooled ($n = 348$) & 0.57 & 0.80 & 1.48 \\
263	Verbosity & 1.40 & 2.03 & 3.78 \\
264	Formality & 0.74 & 0.97 & 1.73 \\
265	\bottomrule
266	\end{tabular}
267	\end{table}
268	
269	Pooled evidence is inconclusive (BF$_{01} < 3$ across all priors), consistent with Claude exhibiting a small (${\sim}5$pp) rather than zero style preference on LLMBar.
270	Verbosity alone approaches moderate evidence for the null (BF$_{01} = 2.03$--$3.78$); formality pulls down the pooled estimate (BF$_{01} = 0.74$--$1.73$).
271	
272	\section{Bradley-Terry Goodness of Fit and Stratified Analysis}
273	\label{app:bt_gof}
274	
275	Bradley-Terry goodness-of-fit tests confirm adequate model fit for both axes (formality: deviance $= 52.80$, $\text{df} = 45$, $p = 0.198$; verbosity: $p = 0.905$).
276	Stratified analysis of consistent pairs by original-text direction reveals no preference heterogeneity for verbosity (Fisher $p = 0.453$) but significant direction asymmetry for formality ($88.9\%$ vs.\ $52.6\%$, Fisher $p = 0.015$), independently confirming the originality confound structure identified by GEE (Table~\ref{tab:gee}).
277	
278	To assess robustness to originality confounding, we restrict to pairs where the judge assigned equal Likert scores to original and counterfactual texts (eliminating detectable quality differences).
279	Style preference persists: formality BT $= 67.3\%$ ($n = 55$, $\Delta = {+}0.8$pp from full sample, 95\% CI $[{-}11.0, {+}12.6]$); verbosity BT $= 76.0\%$ ($n = 50$, $\Delta = {-}1.3$pp, 95\% CI $[{-}13.3, {+}10.3]$).
280	In the anti-originality subset (pairs where the original never wins), effects strengthen (formality $75.0\%$, verbosity $86.1\%$), confirming that style preference is not an artifact of originality confounding.
281	
282	\section{Bradley-Terry Confidence Intervals}
283	\label{app:bt_ci}
284	
285	Table~\ref{tab:bt_ci} reports bootstrap 95\% confidence intervals for all Bradley-Terry estimates in Table~\ref{tab:main_results}.
286	
287	\begin{table}[h]
288	\centering
289	\small
290	\caption{Bootstrap 95\% CIs for BT win probabilities (10{,}000 pair-level resamples).}
291	\label{tab:bt_ci}
292	\begin{tabular}{lllc}
293	\toprule
294	Bench & Judge & Axis & BT $P$ [95\% CI] \\
295	\midrule
296	LLMBar & GPT-4o & Form.\ & .630 [.557, .703] \\
297	 & GPT-4o & Verb.\ & .760 [.667, .853] \\
298	 & GPT-4o & Reg.\ & .570 [.468, .673] \\
299	\cmidrule{2-4}
300	 & Qwen3 & Form.\ & .665 [.585, .739] \\
301	 & Qwen3 & Verb.\ & .773 [.703, .843] \\
302	 & Qwen3 & Reg.\ & .553 [.479, .628] \\
303	\cmidrule{2-4}
304	 & Llama-70B & Form.\ & .695 [.619, .765] \\
305	 & Llama-70B & Verb.\ & .735 [.655, .809] \\
306	 & Llama-70B & Reg.\ & .635 [.555, .712] \\
307	\cmidrule{2-4}
308	 & Claude & Form.\ & .562 [.489, .636] \\
309	 & Claude & Verb.\ & .541 [.459, .616] \\
310	\midrule
311	AEval & GPT-4o & Form.\ & .727 [.663, .785] \\
312	 & Qwen3 & Form.\ & .657 [.581, .733] \\
313	 & Qwen3 & Verb.\ & .841 [.774, .902] \\
314	\midrule
315	MTB & GPT-4o & Form.\ & .692 [.623, .753] \\
316	 & Qwen3 & Form.\ & .712 [.630, .788] \\
317	\bottomrule
318	\end{tabular}
319	\end{table}
320	
321	\section{Bootstrap Attenuation Analysis}
322	\label{app:bootstrap_attenuation}
323	
324	To distinguish measurement attenuation from insufficient statistical power, we subsample the $n = 355$ formality replication (Qwen3-32B) at seven sample sizes and compute Likert Cohen's $d$ with bootstrap 95\% CIs at each (Table~\ref{tab:attenuation}).
325	Under a power limitation, $d$ would remain constant while only $p$-values improve with larger $n$; under measurement attenuation, $d$ itself converges to zero.
326	The data support attenuation: $d_{\text{median}} = {-}0.017$ across all sample sizes, with CIs narrowing from ${\pm}0.3$ to ${\pm}0.1$ but never excluding zero.
327	The same data yield BT $= 66.5\%$ ($p < 0.0001$), confirming that the pairwise signal is robust.
328	Verbosity shows a similar pattern ($d \approx 0.15$--$0.19$, stable, CIs always containing zero; BT $= 76$--$77\%$, $p < 0.0001$).
329	Within the agnostic framework of \S\ref{sec:likert_pairwise}, this evidence favors the measurement attenuation interpretation but does not exclude construct divergence.
330	
331	\begin{table}[h]
332	\centering
333	\small
334	\caption{Bootstrap attenuation analysis: formality $\times$ Qwen3-32B. Likert $d$ remains flat near zero across sample sizes while BT is stable at 66.5\%.}
335	\label{tab:attenuation}
336	\begin{tabular}{@{}rccc@{}}
337	\toprule
338	$n$ & Likert $d$ & 95\% CI & Contains 0? \\
339	\midrule
340	50 & $-$0.017 & [$-$0.308, 0.262] & Yes \\
341	100 & $-$0.015 & [$-$0.219, 0.176] & Yes \\
342	150 & $-$0.019 & [$-$0.179, 0.145] & Yes \\
343	200 & $-$0.016 & [$-$0.157, 0.119] & Yes \\
344	250 & $-$0.018 & [$-$0.144, 0.107] & Yes \\
345	300 & $-$0.018 & [$-$0.131, 0.095] & Yes \\
346	355 & $-$0.017 & [$-$0.123, 0.087] & Yes \\
347	\bottomrule
348	\end{tabular}
349	\end{table}
350	
351	\section{Formal Power Analysis}
352	\label{app:power_analysis}
353	
354	Table~\ref{tab:power} reports the sample size required for Likert ATE to achieve 80\% power at observed effect sizes across all six judge$\times$axis cells.
355	Required sample sizes range from $336$ (Qwen3-32B verbosity, $d = 0.153$) to $27{,}159$ (Qwen3-32B formality, $d = {-}0.017$), representing $4$--$206\times$ the current $n$.
356	For five of six cells, the required $n$ exceeds $1{,}200$---far beyond typical evaluation budgets---converging with the bootstrap attenuation curve (Appendix~\ref{app:bootstrap_attenuation}) to confirm the Blindspot as a structural measurement limitation.
357	
358	\begin{table}[h]
359	\centering
360	\small
361	\caption{Required Likert sample size for 80\% power at observed $d$. BT detects all six effects at $p < 0.001$ with $n \leq 100$.}
362	\label{tab:power}
363	\begin{tabular}{@{}llcrc@{}}
364	\toprule
365	Judge & Axis & Observed $d$ & Required $n$ & Ratio \\
366	\midrule
367	GPT-4o & Form.\ & 0.073 & 1{,}473 & 16.7$\times$ \\
368	GPT-4o & Verb.\ & 0.080 & 1{,}227 & 14.3$\times$ \\
369	Qwen3 & Form.\ & $-$0.017 & 27{,}159 & 76.5$\times$ \\
370	Qwen3 & Verb.\ & 0.153 & 336 & 3.9$\times$ \\
371	Llama-70B & Form.\ & 0.021 & 18{,}157 & 206.3$\times$ \\
372	Llama-70B & Verb.\ & 0.034 & 6{,}737 & 78.3$\times$ \\
373	\bottomrule
374	\end{tabular}
375	\end{table}
376	
377	\section{Formality Sensitivity Hierarchy}
378	\label{app:sensitivity}
379	
380	Table~\ref{tab:sensitivity} applies seven measurement methods to the same formality style-transformed data (GPT-4o, LLMBar, $n = 88$).
381	Only pairwise methods reach significance; all Likert-based methods fail regardless of scaling assumption.
382	
383	\begin{table}[h]
384	\centering
385	\small
386	\caption{Sensitivity hierarchy: seven measurement methods applied to the same formality data. Only pairwise methods (top two rows) reach significance.}
387	\label{tab:sensitivity}
388	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}lccc@{}}
389	\toprule
390	Method & Statistic & $p$ & Data \\
391	\midrule
392	BT model & 63.0\% $[55.7, 70.3]$ & $0.0004$ & All 173 comp. \\
393	Sign test (filtered) & 73.9\% (34/46) & 0.006 & Consistent \\
394	\midrule
395	Likert ATE ($t$-test) & $d = 0.102$ & 0.332 & NLI$\geq$0.90 \\
396	Binarized Likert & 60.6\% & 0.296 & Non-tied \\
397	Ordinal reg.\ (prop.\ odds) & $\beta = {-}0.079$ & 0.769 & NLI$\geq$0.90 \\
398	GEE (exchangeable) & $\beta = {-}0.084$ & 0.587 & NLI$\geq$0.90 \\
399	Wilcoxon signed-rank & $W = 274$ & 0.905 & NLI$\geq$0.90 \\
400	\bottomrule
401	\end{tabular}}
402	\end{table}
403	
404	\section{Verbosity Sensitivity Hierarchy}
405	\label{app:verb_sensitivity}
406	
407	Table~\ref{tab:verb_sensitivity} replicates the seven-method sensitivity analysis (Table~\ref{tab:sensitivity}) on the verbosity axis ($n = 86$ NLI-filtered pairs, Qwen3-32B judge, LLMBar).
408	The attenuation pattern is more extreme than formality: all six Likert-based methods remain non-significant (lowest $p = 0.213$) despite a stronger pairwise signal (BT 77.3\% vs.\ 66.5\% for formality), and Likert effect sizes ($d = 0.036$--$0.056$) are near zero.
409	
410	\begin{table}[h]
411	\centering
412	\small
413	\caption{Sensitivity hierarchy for verbosity ($n = 86$, Qwen3-32B, LLMBar). All Likert methods fail; only BT reaches significance.}
414	\label{tab:verb_sensitivity}
415	\begin{tabular}{lccc}
416	\toprule
417	Method & Statistic & $p$ & Sig? \\
418	\midrule
419	BT model & 77.3\% $[70.3, 84.3]$ & ${<}0.001$ & Yes \\
420	\midrule
421	Likert ATE & $d = 0.056$ & 0.691 & No \\
422	Binarized $\chi^2$ & OR $= 2.16$ & 0.213 & No \\
423	Ordinal reg.\ & $\beta = 0.159$ & 0.575 & No \\
424	Paired $t$-test & $d = 0.056$ & 0.607 & No \\
425	Mann-Whitney $U$ & $r = {-}0.046$ & 0.578 & No \\
426	Cohen's $d$ & $d = 0.036$ & --- & No \\
427	\bottomrule
428	\multicolumn{4}{p{0.9\columnwidth}}{\footnotesize Effect sizes use style-aligned scoring (verbose $-$ concise), isolating style preference direction. Table~\ref{tab:main_results} reports RATE-compatible ATE (counterfactual $-$ original), which conflates style and originality effects.}
429	\end{tabular}
430	\end{table}
431	
432	\subsection{Scaled Replication ($n = 330$)}
433	\label{app:verb_n355}
434	
435	Table~\ref{tab:verb_n355} reports verbosity results at $n = 330$ (from 355 generated pairs, 330 passing NLI gate at $\tau = 0.90$), replicating across four judges (GPT-4o was not re-scored at this scale).
436	The Blindspot partially resolves for judges with strong style effects: Qwen3-32B ($d = .149$, $p < .001$) and Llama-70B ($d = .160$, $p < .001$) now reach Likert significance, consistent with the power curve (Figure~\ref{fig:power_curve}) predicting ${\sim}40\%$ power at $n = 330$ for $d \approx 0.15$.
437	However, two judges maintain the Blindspot: Gemini-2.5-Flash ($d = .087$, borderline) and Claude Sonnet~4 ($d = .032$, NS).
438	The magnitude discrepancy persists even where Likert reaches significance: BT detects 73--76\% win rates while Likert yields $d \approx 0.15$, confirming the attenuation interpretation.
439	
440	GEE conditional decomposition at $n = 330$ confirms substantial shrinkage from $n = 88$ estimates, consistent with more extreme initial estimates producing larger corrections \citep{nemes2009bias}: Qwen3 $13.10 \to 3.83$ ($-71\%$), Llama $8.21 \to 4.01$ ($-51\%$), Gemini $8.98 \to 2.52$ ($-72\%$).
441	Despite shrinkage, verbosity remains style-dominated for these three judges (Style OR $2.5$--$4.0$, all $p < .001$; Orig OR $0.52$--$0.69$).
442	Claude shows a non-significant style effect at $n = 330$ (Style OR $= 1.22$, $p = .134$), with its elevated BT reflecting originality rather than style preference (Orig OR $= 1.69$).
443	As predicted by the power analysis (Figure~\ref{fig:power_curve}), Likert begins detecting the strongest effects at $n \approx 330$ (Qwen3 $d = .15$, $p < .001$; Llama $d = .16$, $p < .001$), while two judges maintain the Blindspot (Claude $d = .03$, NS; Gemini borderline $d = .09$, $p = .02$ by Wilcoxon but $p = .11$ by $t$-test).
444	The efficiency gap---Likert requiring $3$--$4\times$ the sample size pairwise needs---rather than absolute failure, is the practical concern.
445	
446	\begin{table}[h]
447	\centering
448	\small
449	\caption{Verbosity scaled replication ($n = 330$, four judges; GPT-4o not re-scored). Blindspot partially resolves for strong effects (Qwen3, Llama-70B) but persists for weaker-effect judges (Gemini, Claude).}
450	\label{tab:verb_n355}
451	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}lcccc@{}}
452	\toprule
453	Judge & BT $P(\text{V})$ & [95\% CI] & Likert $d$ ($p$) & Blindspot? \\
454	\midrule
455	Qwen3-32B & .733$^{***}$ & [.696, .770] & .149 (.001) & No \\
456	Llama-70B & .759$^{***}$ & [.722, .793] & .160 ({<}.001) & No \\
457	Gemini-2.5 & .678$^{***}$ & [.638, .717] & .087 (.021) & $\dagger$ \\
458	Claude S4 & .608$^{***}$ & [.567, .649] & .032 (.317) & $\dagger$ \\
459	\bottomrule
460	\end{tabular}}
461	\par\vspace{2pt}
462	{\footnotesize $^{***}$\,$p < 0.001$. $\dagger$ marks Blindspot cases (BT significant, Likert $d$ non-significant at $\alpha = 0.05$ by Wilcoxon). Likert $p$ values from Wilcoxon signed-rank test on non-zero differences.}
463	\end{table}
464	
465	\section{100-Point Continuous Likert Scale}
466	\label{app:likert100}
467	
468	To test whether the Blindspot reflects integer-scale granularity rather than a paradigm difference between absolute and relative evaluation, we replicate the formality experiment using a 100-point continuous scale ($1$--$100$) with three judges (Table~\ref{tab:likert100}).
469	All three judges remain non-significant (all $p > 0.15$).
470	Tie rates decrease substantially with finer granularity (1--10 scale: 58--73\%; 1--100 scale: 40--66\%), yet ATE remains non-significant, confirming the gap reflects measurement mode rather than scale granularity \citep{preston2000scale}.
471	Judges differ markedly in effective granularity usage: GPT-4o clusters scores into ${\sim}5$ distinct bins (modes at 70, 75, 80), Qwen3-32B uses ${\sim}20$ distinct values spanning $45$--$95$, and Llama-70B exploits $50{+}$ unique scores with near-uniform coverage---yet none resolves the Blindspot.
472	Score distributions are unimodal and right-skewed for all three judges, with medians in the $72$--$80$ range; the score \emph{difference} distributions (original minus rewrite) are symmetric around zero, confirming no net directional shift under Likert scoring.
473	
474	\begin{table}[h]
475	\centering
476	\small
477	\caption{Formality Likert ATE: 1--10 vs.\ 1--100 scale. Finer granularity reduces tie rates but does not resolve the Blindspot (all 1--100 $p > 0.15$).}
478	\label{tab:likert100}
479	\resizebox{\columnwidth}{!}{%
480	\begin{tabular}{@{}lcccc@{}}
481	\toprule
482	Judge & 1--10 $d$ ($p$) & 1--100 $d$ ($p$) & Tie 1--10 & Tie 1--100 \\
483	\midrule
484	GPT-4o & --- & $-$.038 (.725) & --- & 65.9\% \\
485	Qwen3-32B & .012 (.908) & .153 (.154) & 72.7\% & 51.1\% \\
486	Llama-70B$^a$ & .000 (1.00) & .085 (.440) & 72.7\% & 39.8\% \\
487	\bottomrule
488	\multicolumn{5}{l}{\footnotesize $^a$ 5 pairs returned score $= 0$ (out of range); effective $n = 83$.}
489	\end{tabular}}
490	\end{table}
491	
492	\section{NLI Gate Ablation}
493	\label{app:nli_ablation}
494	
495	Table~\ref{tab:nli_ablation} compares BT estimates across NLI-pass, NLI-fail, and all pairs.
496	For formality, NLI-fail pairs reverse to 41.7\% (preferring casual over formal), demonstrating that the gate removes content-confounded pairs rather than amplifying style signal.
497	The small NLI-fail sample ($n \approx 12$) limits precision; this serves as a bounding analysis.
498	For verbosity, NLI-fail pairs remain at 75.0\%, consistent with the dominant style effect (OR $= 13.10$) overwhelming content noise.
499	
500	\begin{table}[h]
501	\centering
502	\small
503	\caption{NLI gate ablation: BT win probability by NLI subset.}
504	\label{tab:nli_ablation}
505	\begin{tabular}{lccc}
506	\toprule
507	Axis & NLI-pass & NLI-fail & All \\
508	\midrule
509	Formality & 66.5\% & 41.7\% & 63.0\% \\
510	Verbosity & 77.3\% & 75.0\% & 76.0\% \\
511	\bottomrule
512	\end{tabular}
513	\end{table}
514	
515	\section{Rewriting Artifact Control}
516	\label{app:artifact_control}
517	
518	Same-style double-rewrite (DR) controls quantify the rewriting artifact using BT models (consistent with all other pairwise analyses).
519	Table~\ref{tab:artifact} reports BT $P(\text{original})$---the probability the judge prefers the original over its same-style DR.
520	Both judges systematically prefer LLM-polished text across axes; for verbosity, BT $P(\text{original}) < 0.17$ indicates that rewriting quality dominates when content is held constant, validating the GEE decomposition that separates style from artifact effects.
521	Same-style double-rewrite controls for style-neutral polishing artifacts but cannot exclude style-specific polishing interactions (e.g., formal rewriting may polish differently than casual rewriting).
522	
523	\begin{table}[h]
524	\centering
525	\small
526	\caption{Rewriting artifact: BT $P(\text{orig})$ vs.\ same-style double-rewrite (bootstrap 95\% CI, 10{,}000 resamples). Values ${<}0.5$: judges prefer LLM-polished text.}
527	\label{tab:artifact}
528	\begin{tabular}{@{}llcc@{}}
529	\toprule
530	Axis & Judge & BT $P(\text{orig})$ [CI] & $p$ \\
531	\midrule
532	Form.\ & GPT-4o & .418 [.342, .500] & .037 \\
533	 & Qwen3 & .377 [.303, .451] & .0006 \\
534	\midrule
535	Verb.\ & GPT-4o & .167 [.084, .262] & ${<}.0001$ \\
536	 & Qwen3 & .082 [.035, .140] & ${<}.0001$ \\
537	\bottomrule
538	\end{tabular}
539	\end{table}
540	
541	\section{Implementation Details}
542	\label{app:implementation}
543	
544	\paragraph{Models and APIs.}
545	Style-controlled rewriting uses Qwen3-32B (temperature $0.7$, top-$p$ $0.9$).
546	Target judges: GPT-4o (\texttt{gpt-4o-2024-08-06}, accessed April--May 2026), Qwen3-32B (locally hosted), Llama-3.3-70B (locally hosted via vLLM).
547	Claude Sonnet 4 (\texttt{claude-sonnet-4-20250514}, accessed May 2026) provides discriminative validity evidence with benchmark-dependent sensitivity.
548	All judge calls use temperature $0$ and $\texttt{max\_tokens} = 2048$.
549	
550	\paragraph{NLI gate.}
551	Content preservation is verified using DeBERTa-v3-large \citep{he2021debertav3} fine-tuned on MNLI, with entailment threshold $\tau = 0.90$.
552	Bidirectional entailment is applied for formality and register; direction-aware entailment for verbosity (Section~\ref{sec:nli_gate}).
553	
554	\paragraph{Statistical methods.}
555	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm} using the \texttt{choix} Python library (default L2 regularization $\alpha = 10^{-6}$); varying $\alpha$ from $10^{-6}$ to $1.0$ changes all BT probabilities by ${<}0.002$.
556	All bootstrap CIs use 10{,}000 pair-level resamples with seed $42$.
557	GEE models use exchangeable working correlation with robust (sandwich) standard errors via \texttt{statsmodels} (Section~\ref{sec:direction}; diagnostics in Appendix~\ref{app:gee_diagnostics}).
558	
559	\paragraph{Benchmarks.}
560	LLMBar \citep{zeng2023llmbar}: 100 instruction-response pairs ($n = 88$ after NLI gate, $n = 355$ for scaled replication).
561	AlpacaEval \citep{dubois2025lc}: 100 sampled pairs.
562	MT-Bench \citep{zheng2023judging}: 80 multi-turn pairs.
563	
564	\paragraph{Code and data.}
565	All code, prompts, and experimental data will be released upon acceptance under an open-source license.
566	
567	\section{Holm-Bonferroni Sensitivity Analysis}
568	\label{app:holm8}
569	
570	Table~\ref{tab:holm8} reports adjusted $p$-values under the full 8-test family (4 judges $\times$ 2 primary axes), including Gemini-2.5-Flash which is excluded from the primary 6-test family (\S\ref{sec:stat_framework}).
571	All results remain significant at $\alpha = 0.05$.
572	
573	\begin{table}[h]
574	\centering
575	\small
576	\caption{Holm-Bonferroni sensitivity analysis: 8-test family (4 judges $\times$ 2 primary axes). All results remain significant under the expanded family ($\alpha = 0.05$).}
577	\label{tab:holm8}
578	\resizebox{\columnwidth}{!}{%
579	\begin{tabular}{@{}cllcccc@{}}
580	\toprule
581	Rank & Judge & Axis & BT $P$ & Raw $p$ & Threshold & Adj.\ $p$ \\
582	\midrule
583	1 & Gemini Flash & Verb.\ & .708 & ${<}.0001$ & .00625 & ${<}.001$ \\
584	2 & GPT-4o & Verb.\ & .760 & .0001 & .00714 & .0007 \\
585	3 & Qwen3-32B & Form.\ & .665 & .0001 & .00833 & .0007 \\
586	4 & Qwen3-32B & Verb.\ & .773 & .0001 & .0100 & .0007 \\
587	5 & Llama-70B & Form.\ & .695 & .0001 & .0125 & .0007 \\
588	6 & Llama-70B & Verb.\ & .735 & .0001 & .0167 & .0007 \\
589	7 & GPT-4o & Form.\ & .630 & .0004 & .0250 & .0008 \\
590	8 & Gemini Flash & Form.\ & .574 & .0306 & .0500 & .0306 \\
591	\bottomrule
592	\end{tabular}}
593	\end{table}
594	
595	\section{Cross-Axis Contamination Analysis}
596	\label{app:cross_axis_contamination}
597	
598	Our per-axis design assumes that rewriting along one style axis does not substantially alter the text along other axes.
599	We quantify cross-axis contamination by measuring off-target surface proxies before and after rewriting.
600	For formality rewrites ($n = 355$), we measure word count and sentence count as verbosity proxies; for verbosity rewrites ($n = 86$), we measure type-token ratio (TTR) as a lexical diversity proxy for formality, and Flesch-Kincaid (FK) grade level.
601	
602	\begin{table}[h]
603	\centering
604	\small
605	\caption{Cross-axis contamination: effect of rewriting along one style axis on surface proxies of the other axis. Cohen's $d$: $|d| < 0.20$ negligible, $0.20$--$0.50$ small contamination \citep{cohen1988statistical}.}
606	\label{tab:cross_axis}
607	\resizebox{\columnwidth}{!}{%
608	\begin{tabular}{@{}llrrl@{}}
609	\toprule
610	Direction & Proxy & $\Delta$ & $d$ & Interp.\ \\
611	\midrule
612	Form.\ $\to$ Verb.\ & Word count & $-3.4\%$ & $-0.23$ & Small \\
613	Form.\ $\to$ Verb.\ & Sent.\ count & $-0.2\%$ & $-0.03$ & Negligible \\
614	Verb.\ $\to$ Form.\ & TTR & $-0.006$ & $-0.04$ & Negligible \\
615	Verb.\ $\to$ Form.\ & FK grade & --- & $0.50$ & Confounded$^*$ \\
616	\bottomrule
617	\multicolumn{5}{l}{\footnotesize $^*$ FK $=$ $f$(sentence length, word length); sentence length change is}\\
618	\multicolumn{5}{l}{\footnotesize inherent to verbosity manipulation, not formality contamination.}
619	\end{tabular}}
620	\end{table}
621	
622	Formality rewrites leave sentence structure virtually unchanged ($d = -0.03$); the word count shift ($d = -0.23$, exceeding the negligible threshold but within the small range) reflects word-level adjustments (contractions, elaboration) that are directionally symmetric (formal$\to$casual $-5.0\%$, casual$\to$formal $+5.6\%$) and do not constitute verbosity contamination.
623	Verbosity rewrites leave lexical diversity unchanged (TTR $d = -0.04$); the elevated FK grade ($d = 0.50$) is an artifact of FK's dependence on sentence length, which changes by design in verbosity manipulation.
624	These results confirm that cross-axis contamination is small to negligible for the proxies measured; the GEE originality term (\S\ref{sec:direction}) provides additional protection by absorbing any residual quality confound.
625	A robustness check adding word-count change as a GEE covariate leaves all Style ORs virtually unchanged ($\Delta < 12\%$, all covariate $p > .28$), confirming that the small cross-axis word-count shift does not confound formality estimates.
626	
627	\section{FK Length-Control Analysis}
628	\label{app:fk_length}
629	
630	The elevated FK grade shift for verbosity rewrites ($d = 0.50$; Table~\ref{tab:cross_axis}) could reflect genuine formality contamination or simply FK's structural dependence on sentence length.
631	We disentangle these via length-controlled regression and mediation analysis.
632	
633	\begin{table}[h]
634	\centering
635	\small
636	\caption{Descriptive statistics for FK grade and sentence length changes by rewriting axis. Computed on all pairs; regression analysis below uses NLI-verified pairs only ($n_{\text{form}} = 88$, $n_{\text{verb}} = 86$).}
637	\label{tab:fk_desc}
638	\begin{tabular}{@{}llrr@{}}
639	\toprule
640	Axis & Metric & $\Delta$ & $d$ \\
641	\midrule
642	Verbosity & FK grade & $+2.26$ & $0.50$ \\
643	Verbosity & Sent.\ length (words) & $+3.40$ & $0.35$ \\
644	Formality & FK grade & $-0.30$ & $-0.08$ \\
645	Formality & Sent.\ length (words) & $-0.11$ & $-0.04$ \\
646	\bottomrule
647	\end{tabular}
648	\end{table}
649	
650	Regressing FK change on style axis without controls yields $\beta = 2.69$ ($p < .001$, $R^2 = 0.100$); adding sentence length as a covariate reduces the coefficient to $\beta = 1.07$ ($p = .020$, $R^2 = 0.546$), a 60.3\% reduction.
651	Sobel mediation test confirms that sentence length mediates 60\% of the total effect ($z = 2.15$, $p = .031$); the 40\% residual direct effect reflects multi-syllable vocabulary shifts (e.g., ``use'' $\to$ ``utilize'') that are inherent to verbose style rather than formality contamination.
652	
653	\paragraph{GEE with FK covariate.}
654	As a further robustness check, we add FK grade change as a covariate to the GEE formality model.
655	FK grade is not independently significant for any judge ($p > .11$), but its inclusion reduces formality Style ORs by 20--51\% due to collinearity between formality and readability: GPT-4o Style OR drops from $2.70$ to $2.15$ ($p = .132$, no longer significant); Qwen3-32B from $4.20$ to $3.38$ ($p = .014$); Llama-70B from $5.52$ to $2.69$ ($p = .037$).
656	Two of three judges retain significant formality effects after readability control, confirming that formality style sensitivity is not fully reducible to readability differences.
657	
658	\section{Human Annotation Agreement Statistics}
659	\label{app:annotation_agreement}
660	
661	Two independent annotators evaluated 100 NLI-scored pairs (50 formality, 50 verbosity), stratified into 70 NLI-pass and 30 NLI-fail pairs for content preservation.
662	Annotator~1 (A1) judged 99/100 pairs content-preserving; Annotator~2 (A2) judged 97/100.
663	
664	\paragraph{Agreement.}
665	On the \emph{preserves\_meaning} label, 96/100 pairs are concordant, yielding Gwet's AC$_1 = 0.958$ \citep{gwet2008ac1}.
666	Cohen's $\kappa = {-}0.015$ is misleading here: with ${>}96\%$ positive prevalence, chance agreement is near-ceiling and $\kappa$ is compressed toward zero regardless of actual agreement---the well-documented prevalence paradox \citep{feinstein1990kappa}.
667	AC$_1$ is the appropriate statistic under such extreme marginal distributions.
668	
669	\paragraph{Gate pass precision.}
670	Both annotators independently confirm 69/70 gate-passed pairs as content-preserving ($98.6\%$; Wilson CI $[92.3\%, 99.8\%]$).
671	Only two gate-passed pairs were flagged by either annotator (S073 and S063, both formality); excluding these changes BT by ${<}0.3$\,pp and Style OR by ${<}4\%$ relative, with all significance levels unchanged.
672	
673	\paragraph{Gate-failed analysis.}
674	Among 30 gate-rejected pairs, A1 judges 30/30 and A2 judges 28/30 as content-preserving, confirming that the gate's dominant error mode is false rejection rather than false acceptance.
675	This conservative calibration ensures high pass precision at the cost of reduced recall (59.5\%).
676	
677	\paragraph{Disagreement analysis.}
678	Four pairs show annotator disagreement: S073, S098, S063, S136 (3 formality, 1 verbosity; 2 NLI-pass, 2 NLI-fail).
679	All disagreements involve borderline meaning-equivalence judgments rather than clear content contamination.
680	
681	\paragraph{Comparison with 50-pair pilot.}
682	The expanded 100-pair annotation tightens the precision estimate from $84$--$100\%$ (individual annotators on 25 gate-passed pairs) to $98.6\%$ (both annotators concordant on 70 gate-passed pairs), and raises AC$_1$ from $0.65$ to $0.96$.
683	
684	\paragraph{Style detection agreement.}
685	Agreement on \emph{style\_change\_detected} is lower ($58\%$, $\kappa = 0.138$, AC$_1 = 0.206$), reflecting genuine difficulty in judging whether a rewrite altered style.
686	This does not affect the primary validation target, which concerns content preservation rather than style detection.
687	
688	\section{Cross-Benchmark Replication}
689	\label{app:cross_bench}
690	
691	Table~\ref{tab:cross_bench} reports cross-benchmark replication results on AlpacaEval and MT-Bench.
692	Selection criterion: we targeted the six judge$\times$axis cells with the largest LLMBar BT effects (BT $\geq .63$, all $p < .001$), prioritizing cells where the Blindspot was strongest.
693	The remaining 18/24 cells (3 benchmarks $\times$ 4 target judges $\times$ 2 axes, minus 6 tested) were not evaluated; generalization to weaker-effect configurations remains open.
694	
695	\begin{table}[h]
696	\centering
697	\small
698	\caption{Cross-benchmark replication on AlpacaEval (AEval) and MT-Bench (MTB). $\ddagger$: both BT and Likert significant; $\dagger$: Blindspot (BT significant, Likert not).}
699	\label{tab:cross_bench}
700	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}lllccc@{}}
701	\toprule
702	Bench & Judge & Axis & BT $P$ & Likert $d$ ($p$) & Cat.\ \\
703	\midrule
704	AEval & GPT-4o & Form.\ & .727$^{***}$ & .005 (.909) & $\dagger$ \\
705	 & Qwen3 & Form.\ & .657$^{***}$ & .081 (.198) & $\dagger$ \\
706	 & Qwen3 & Verb.\ & .841$^{***}$ & .375 (.0003) & $\ddagger$ \\
707	 & Llama-70B & Form.\ & .750$^{***}$ & .212 (.012) & $\ddagger$ \\
708	\midrule
709	MTB & GPT-4o & Form.\ & .692$^{***}$ & .111 (.016) & $\ddagger$ \\
710	 & Qwen3 & Form.\ & .712$^{***}$ & .149 (.007) & $\ddagger$ \\
711	\bottomrule
712	\multicolumn{6}{l}{\footnotesize $^{***}$ $p < 0.001$. $\ddagger$: both sig.;\; $\dagger$: Blindspot.}
713	\end{tabular}}
714	\end{table}
715	
716	\section{Claude Cross-Benchmark Analysis}
717	\label{app:claude_crossbench}
718	
719	Claude Sonnet~4 exhibits near-null style sensitivity on LLMBar (\S\ref{sec:amplification}; Appendix~\ref{app:claude_tost}).
720	Cross-benchmark GEE decomposition reveals that Claude's elevated aggregate BT on AEval/MT-Bench reflects quality detection rather than style preference.
721	Table~\ref{tab:claude_crossbench} reports results across all five tested configurations.
722	
723	\begin{table}[h]
724	\centering
725	\small
726	\caption{Claude Sonnet~4 cross-benchmark results with GEE decomposition. Formality Style OR is non-significant across all three benchmarks; elevated BT on AEval/MT-Bench is driven by Orig OR (quality detection). AEval verbosity is the sole genuine style effect.}
727	\label{tab:claude_crossbench}
728	\resizebox{\columnwidth}{!}{%
729	\begin{tabular}{@{}llccccc@{}}
730	\toprule
731	Bench & Axis & BT $P$ & Likert $d$ ($p$) & Style OR ($p$) & Orig OR ($p$) \\
732	\midrule
733	LLMBar & Form.\ & .562 & $-$.021 (.721) & 1.47 (.276) & 6.66 (${<}.001$) \\
734	LLMBar & Verb.\ & .541 & $-$.039 (.743) & 1.52 (.286) & 0.80 (.563) \\
735	\midrule
736	AEval & Form.\ & .698$^{***}$ & .081 (.090) & 1.99 (.082) & 9.33 (${<}.001$) \\
737	AEval & Verb.\ & .683$^{***}$ & .252 (.002) & \textbf{4.76} (${<}.001$) & 0.87 (.732) \\
738	\midrule
739	MTB & Form.\ & .733$^{***}$ & .233 (${<}.001$) & 1.64 (.364) & 11.85 (${<}.001$) \\
740	\bottomrule
741	\multicolumn{6}{l}{\footnotesize $^{***}$ $p < 0.001$. All Style ORs except AEval verbosity are non-significant.}\\
742	\multicolumn{6}{l}{\footnotesize Negative $d$: styled variant scored lower.}
743	\end{tabular}}
744	\end{table}
745	
746	\paragraph{Formality.}
747	Claude's formality Style OR is non-significant across all three benchmarks ($1.47$/$1.99$/$1.64$, all $p > .08$), indicating consistently low formality sensitivity regardless of benchmark.
748	The elevated BT on AEval (69.8\%) and MT-Bench (73.3\%) is driven entirely by Orig OR ($9.33$/$11.85$, both $p < .001$): Claude detects quality differences between original and counterfactual texts without exhibiting formality preference.
749	AEval formality produces a Blindspot (BT significant, Likert n.s.), but GEE decomposition reveals this as quality detection rather than style sensitivity---illustrating why aggregate BT alone is insufficient for bias attribution.
750	
751	\paragraph{Verbosity.}
752	AEval verbosity is the sole configuration where Claude exhibits genuine style sensitivity (Style OR $= 4.76$, $p < .001$; Orig OR $= 0.87$, n.s.), a style-dominated pattern.
753	LLMBar verbosity remains null (Style OR $= 1.52$, n.s.), confirming benchmark-dependent sensitivity.
754	
755	\section{Rewriting Prompts}
756	\label{app:rewriting_prompts}
757	
758	Below are the axis-specific rewriting prompts used in Section~\ref{sec:rewriting}. All prompts are issued to Qwen3-32B-Instruct at temperature 0.7.
759	
760	\paragraph{Formality.}
761	\texttt{Rewrite the following text to be more [formal/casual] while preserving the exact same content and meaning. Do not add, remove, or change any factual information. Only adjust the level of formality in the language.}
762	
763	\paragraph{Verbosity.}
764	\texttt{Rewrite the following text to be more [verbose/concise] while preserving the exact same content and meaning. Do not add, remove, or change any factual information. Only adjust the level of detail and elaboration.}
765	
766	\paragraph{Register.}
767	\texttt{Rewrite the following text to use a more [academic/conversational] register while preserving the exact same content and meaning. Do not add, remove, or change any factual information. Only adjust the register and tone.}
768	
769	\paragraph{Same-style double-rewrite.}
770	\texttt{Rewrite the following text in the same style (keep it [formal/casual/verbose/concise]) while preserving the exact same content and meaning. Paraphrase the text without changing its style.}
771	
772	\section{Non-Tie Concordance Analysis}
773	\label{app:concordance}
774	
775	To adjudicate between measurement attenuation and construct divergence as explanations for the Likert Blindspot (\S\ref{sec:likert_pairwise}), we examine whether Likert and pairwise evaluations agree \emph{when Likert does differentiate}.
776	For each pair where Likert assigned different scores to the two texts (non-tie), we check whether the higher-scoring text matches the pairwise-preferred text; if the two methods measure the same underlying construct, non-tie concordance should substantially exceed chance (50\%).
777	We additionally compute point-biserial correlations ($r_{\text{pb}}$) between Likert score differences and pairwise outcomes across all pairs with valid pairwise preferences.
778	
779	\begin{table}[h]
780	\centering
781	\small
782	\caption{Non-tie concordance between Likert and pairwise preferences. For each judge$\times$axis condition, we identify Likert non-tie pairs and check agreement with pairwise preference direction. Wilson 95\% CIs; $p$ from two-sided binomial test against 50\%. $r_{\text{pb}}$: point-biserial correlation between Likert score difference and pairwise outcome (all pairs with valid pairwise preference).}
783	\label{tab:concordance}
784	\resizebox{\columnwidth}{!}{%
785	\begin{tabular}{@{}llrcccrc@{}}
786	\toprule
787	Bench & Config & $n_{\text{nt}}$ & Conc. & Rate & 95\% CI & $p$ & $r_{\text{pb}}$ ($p$) \\
788	\midrule
789	LLMBar & Llama verb.\ & 25 & 22 & 88.0\% & [70.0, 95.8] & ${<}.001$ & .412 (.001) \\
790	 & GPT-4o verb.\ & 30 & 25 & 83.3\% & [66.4, 92.7] & ${<}.001$ & .373 (.003) \\
791	 & Llama form.\ & 18 & 15 & 83.3\% & [60.8, 94.2] & .008 & .447 (.001) \\
792	 & Qwen3 verb.\ & 27 & 20 & 74.1\% & [55.3, 86.8] & .019 & .296 (.019) \\
793	 & Gemini verb.\ & 24 & 17 & 70.8\% & [50.8, 85.1] & .064 & .346 (.012) \\
794	 & Qwen3 form.\ & 15 & 10 & 66.7\% & [41.7, 84.8] & .302 & .274 (.065) \\
795	 & Gemini form.\ & 15 & 10 & 66.7\% & [41.7, 84.8] & .302 & .373 (.012) \\
796	\midrule
797	AEval & Qwen3 form.\ & 26 & 20 & 76.9\% & [57.9, 89.0] & .009 & .203 (.146) \\
798	 & GPT-4o form.\ & 21 & 15 & 71.4\% & [50.0, 86.2] & .078 & .340 (.019) \\
799	\midrule
800	\multicolumn{2}{@{}l}{\textbf{Pooled}} & \textbf{201} & \textbf{154} & \textbf{76.6\%} & \textbf{[70.3, 81.9]} & $\mathbf{{<}.001}$ & --- \\
801	\bottomrule
802	\end{tabular}}
803	\end{table}
804	
805	Pooled concordance is 76.6\% (154/201 non-tie pairs; binomial $p < .001$; Table~\ref{tab:concordance}), substantially exceeding the 50\% chance baseline.
806	Point-biserial correlations are positive in all nine conditions ($r_{\text{pb}} = 0.20$--$0.45$), with seven of nine reaching significance ($p < .05$).
807	Concordance is highest for verbosity ($74$--$88\%$) and for Llama-70B across both axes ($83$--$88\%$), consistent with Llama's lower Likert tie rate (Table~\ref{tab:likert100}).
808	
809	These results favor the measurement attenuation interpretation: when Likert scoring does differentiate between texts, its preference direction aligns with pairwise judgment in more than three-quarters of cases.
810	The primary driver of the Blindspot is thus the high Likert tie rate (60--73\% across conditions) rather than a fundamental disagreement between the two evaluation paradigms about what constitutes quality.
811	The ${\sim}23\%$ discordance rate leaves room for partial construct divergence---pairwise comparison may access quality dimensions that Likert cannot express---but the dominant pattern is signal attenuation through discretization and ceiling effects.
812	
813	\section*{Code and Data}
814	
815	Code and data will be released upon acceptance.
816	
817	\section*{Use of AI Assistants}
818	\label{app:ai-assistants}
819	
820	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
821	\begin{itemize}
822	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
823	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting LaTeX.
824	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
825	\end{itemize}
826	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe4c1103-4ce0-41c3-af12-f31b5d8aa2f7",
  "isSidechain": false,
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "81bf1f67-dcbc-4f2c-9d31-dd5abafb8f11",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
      "content": "\\appendix\n\n\\noindent\\emph{Organization: design rationale (A$^*$), confound analysis (A--B), model diagnostics (C), independence tests (D), gate validation (E--F), equivalence testing (G), statistical details (H--K), sensitivity analyses (L--N), artifact controls (O), implementation (P), multiplicity (Q), cross-axis contamination (R), FK length-control (R$'$), human annotation agreement (S), cross-benchmark replication (T), Claude cross-benchmark (U), rewriting prompts (V), non-tie concordance (W).}\n\n\\section{Design Rationale}\n\\label{app:design_rationale}\n\nThree variables govern the observed judge score $Y$: the style attribute $S$ (e.g., formality), the original content quality $Q$, and the judge's internal scoring function.\nBoth $S$ and $Q$ causally influence $Y$; the goal of CSD is to approximate the effect $S \\to Y$ while blocking confounding through $Q$.\nStyle-controlled rewriting generates a text pair that differs along a single style axis, but any rewriting operation risks inadvertently altering content quality ($R \\to Q$).\nThe NLI gate (\\S\\ref{sec:nli_gate}) blocks this path, yielding a controlled estimate of the $S \\to Y$ effect.\nOur approach provides interventional rather than formal causal evidence: we do not claim that the DAG in Figure~\\ref{fig:dag} is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework.\n``Controlled'' in this context refers to experimentally controlled rewriting conditions, not formal causal identification in the potential-outcomes sense.\nOur identification rests on three operational assumptions: (i)~the NLI gate approximates content preservation, blocking the $R \\to Q$ path; (ii)~position swapping controls for presentation-order effects; and (iii)~the style rewrite introduces no systematic differences beyond the target axis.\n\n\\section{Direction Asymmetry and Quality Confounding}\n\\label{app:direction}\n\nThe formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\\% of formal-is-rewrite pairs ($p = 0.001$) but only 54.5\\% of casual-is-rewrite pairs ($p = 0.83$).\nThis asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.\nTo quantify this, we fit a GEE logistic model (exchangeable correlation) with both formality and original-preference as predictors.\nAfter controlling for original preference, the formality effect remains significant ($\\text{OR} = 2.58$, $p = 0.002$), and the original-preference effect is also significant ($\\text{OR} = 2.32$, $p = 0.006$).\nThe formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.\n\nAt $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exceeded the GPT-4o estimate ($2.58$), but a scaled replication ($n = 355$) corrects this to $2.15$ ($p < 0.0001$), comparable to GPT-4o and consistent with small-sample upward bias rather than evaluator-producer inflation of the style effect.\nThe originality confound remains stronger ($4.99$ vs.\\ $2.32$), consistent with evaluator-producer bias inflating the originality component (Limitations).\nThe directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.\n\nThe NLI gate blocks \\emph{content} changes but cannot block quality perception shifts that are themselves mediated by style---a fundamental identifiability limit of any text-rewriting approach.\n\n\\section{Consistency Filter Robustness}\n\\label{sec:consistency}\n\nThe position-consistency filter retains 55 of 98 valid pairs (56.1\\%); consistent and inconsistent groups show no significant differences across four covariates (NLI score $p = 0.824$, BERTScore $p = 0.12$, text length $p = 0.137$, length diff $p = 0.715$), indicating selection on judge decisiveness rather than text properties.\nThe BT model using all 173 comparisons including inconsistent pairs yields 63.0\\% ($p = 0.0004$), consistent with the filtered sign test (73.9\\%, $p = 0.006$), confirming no systematic bias from the filter.\nChi-squared tests confirm that NLI gate pass/reject status is independent of source category ($\\chi^2 = 1.30$, $p = .73$), original formality ($p = .37$), and gold label ($p = 1.0$), indicating no systematic selection bias along these dimensions.\n\nVerbosity gate-passed pairs are significantly longer than rejected pairs (token count KS $p = 0.003$; sentence length MWU $p = 0.006$).\nThis reflects the gate's content-preservation mandate: verbosity transformations on shorter texts alter content ratios more substantially, causing correct NLI rejection.\nLength-controlled GEE analysis (\\S\\ref{sec:direction}; Style OR change ${<}2\\%$) confirms this selection does not confound the verbosity effect.\n\n\\section{GEE Model Diagnostics}\n\\label{app:gee_diagnostics}\n\n\\paragraph{Correlation structure robustness.}\nTable~\\ref{tab:gee_corr} compares exchangeable and independence working correlation structures across all nine judge$\\times$axis cells.\nThe two structures yield virtually identical results: $|\\Delta\\text{QIC}| < 0.001$ and maximum coefficient change ${<}0.02$ in every cell, with estimated within-pair correlations $\\hat{\\alpha} \\in [-0.25, +0.11]$.\nAll GEE results reported in the main text are therefore robust to correlation structure specification.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{GEE correlation structure comparison across nine judge$\\times$axis cells.}\n\\label{tab:gee_corr}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nConfig & Exch.\\ QIC & Indep.\\ QIC & $|\\Delta\\text{QIC}|$ & Max$|\\Delta\\text{Coef}|$ \\\\\n\\midrule\nGPT-4o form.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nQwen3 form.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nLlama-70B form.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nGPT-4o verb.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nQwen3 verb.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nLlama-70B verb.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nGPT-4o reg.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nQwen3 reg.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nLlama-70B reg.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize Absolute QIC values omitted; only $|\\Delta\\text{QIC}|$ is reported.}\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Interaction test.}\nAdding a Style$\\times$Originality interaction term to the additive GEE specification yields no significant interactions in any of the nine judge$\\times$axis cells (all $p > 0.13$, range $0.14$--$0.96$), confirming that the additive model is the correct specification and that regime classifications are robust to model specification.\nTable~\\ref{tab:gee-interaction} reports interaction terms; none are significant, confirming the additive specification.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{GEE Style $\\times$ Originality interaction terms. None are significant ($p > 0.13$), confirming the additive model specification.}\n\\label{tab:gee-interaction}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}llccc@{}}\n\\toprule\nJudge & Axis & Interaction OR & 95\\% CI & $p$ \\\\\n\\midrule\nGPT-4o & Formality & 0.661 & [0.18, 2.38] & .527 \\\\\nGPT-4o & Verbosity & 1.269 & [0.37, 4.34] & .705 \\\\\nGPT-4o & Register & 2.601 & [0.74, 9.15] & .136 \\\\\nQwen3-32B & Formality & 0.518 & [0.14, 1.89] & .320 \\\\\nQwen3-32B & Verbosity & 0.450 & [0.13, 1.62] & .221 \\\\\nQwen3-32B & Register & 0.555 & [0.15, 2.08] & .383 \\\\\nLlama-70B & Formality & 0.968 & [0.25, 3.78] & .963 \\\\\nLlama-70B & Verbosity & 1.103 & [0.34, 3.58] & .870 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{95\\% confidence intervals.}\nTable~\\ref{tab:gee_ci} reports 95\\% CIs for all GEE odds ratios in Table~\\ref{tab:gee}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{95\\% CIs for GEE conditional decomposition (Table~\\ref{tab:gee}).}\n\\label{tab:gee_ci}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nConfig & Style OR [CI] & Orig OR [CI] \\\\\n\\midrule\nQwen3 verb.\\ & 13.10 [5.62, 30.55] & 0.49 [0.21, 1.14] \\\\\nGPT-4o verb.\\ & 11.34 [4.93, 26.10] & 0.45 [0.20, 1.04] \\\\\nLlama-70B verb.\\ & 8.21 [3.62, 18.65] & 0.38 [0.17, 0.86] \\\\\nGemini verb.\\ & 8.98 [3.68, 21.94] & 0.46 [0.20, 1.04] \\\\\nGPT-4o form.\\ & 2.58 [1.41, 4.73] & 2.32 [1.27, 4.26] \\\\\nQwen3 form.\\ & 4.20 [1.99, 8.87] & 4.70 [2.22, 9.96] \\\\\nQwen3 form.$^a$ & 2.15 [1.46, 3.16] & 4.99 [3.40, 7.34] \\\\\nLlama-70B form.\\ & 4.81 [2.48, 9.33] & 3.12 [1.61, 6.04] \\\\\nGemini form.\\ & 1.64 [0.91, 2.98] & 2.51 [1.39, 4.54] \\\\\nGPT-4o reg.\\ & 1.88 [1.08, 3.28] & 2.21 [1.26, 3.86] \\\\\nQwen3 reg.\\ & 1.91 [1.01, 3.58] & 5.72 [3.02, 10.82] \\\\\nLlama-70B reg.\\ & 3.33 [1.73, 6.42] & 3.07 [1.60, 5.92] \\\\\n\\bottomrule\n\\multicolumn{3}{l}{\\footnotesize $^a$ $n = 355$; other rows: $n = 88$.}\n\\end{tabular}\n\\end{table}\n\n\\section{Rewriter Independence}\n\\label{app:rewriter_indep}\n\nEvaluator-producer overlap is limited to Qwen3-32B (rewriter $=$ judge); the independence test below bounds this to a 22\\% Style OR reduction. The other three target judges (GPT-4o, Llama-70B, Gemini) use a different rewriter and are not subject to this confound.\n\nTo test whether the Blindspot depends on the rewriter's identity, we replace Qwen3-32B with GPT-4o as rewriter while keeping Qwen3-32B as judge.\n\n\\paragraph{Verbosity (Table~\\ref{tab:rewriter_indep}).}\nThe Style OR decreases by $22\\%$ ($13.10 \\to 10.17$), bounding evaluator-producer inflation of the style effect; the pure-style pattern (Originality n.s.) and Blindspot (BT significant, Likert n.s.) both persist.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Rewriter independence test: verbosity axis, Qwen3-32B judge. GPT-4o rewriter eliminates evaluator-producer overlap while preserving the Blindspot.}\n\\label{tab:rewriter_indep}\n\\begin{tabular}{lcc}\n\\toprule\n & GPT-4o Rewriter & Qwen3 Rewriter \\\\\n\\midrule\nNLI pass rate & 81/100 (81\\%) & 86/100 (86\\%) \\\\\nBT $P$ [95\\% CI] & .735 [.654, .809] & .773 [.703, .843] \\\\\nLikert ATE ($p$) & .000 (.838) & ${\\sim}$0 (.179) \\\\\nBlindspot & Yes & Yes \\\\\nGEE Style OR ($p$) & 10.17 (${<}.0001$) & 13.10 (${<}.0001$) \\\\\nGEE Orig OR ($p$) & 1.61 (n.s.) & 0.49 (n.s.) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Formality (Table~\\ref{tab:rewriter_indep_form}).}\nGPT-4o rewriter produces formality-manipulated pairs yielding BT $64.4\\%$ $[56.1, 72.8]$, statistically indistinguishable from the Qwen3-32B baseline ($66.5\\%$ $[58.5, 73.9]$; $\\Delta = -2.1$pp).\nThe Likert Blindspot replicates with the independent rewriter ($p = 0.184$, n.s.).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Rewriter independence test: formality axis, Qwen3-32B judge.}\n\\label{tab:rewriter_indep_form}\n\\begin{tabular}{lcc}\n\\toprule\n & GPT-4o Rewriter & Qwen3 Rewriter \\\\\n\\midrule\nNLI pass rate & 90/100 (90\\%) & 88/100 (88\\%) \\\\\nBT $P$ [95\\% CI] & .644 [.561, .728] & .665 [.585, .739] \\\\\nLikert $d$ ($p$) & $-$.081 (.184) & .011 (.908) \\\\\nBlindspot & Yes & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{NLI Threshold Sensitivity Sweep}\n\\label{app:nli_sweep}\n\nTable~\\ref{tab:nli_sweep} reports BT win probabilities across 11 NLI entailment thresholds for all four judge$\\times$axis configurations.\nAll 44 combinations are significant ($p < 0.05$), and within each configuration BT varies by at most 3pp, ruling out threshold selection bias.\nThe stability reflects the bimodal NLI score distribution: most pairs score above 0.95 or below 0.30, so thresholds between 0.50 and 0.95 admit nearly identical pair sets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BT win probability across NLI thresholds. All 44 cells significant ($p < 0.05$). $n$: pairs passing threshold.}\n\\label{tab:nli_sweep}\n\\begin{tabular}{@{}rcccc@{}}\n\\toprule\nThresh & \\multicolumn{2}{c}{Formality BT} & \\multicolumn{2}{c}{Verbosity BT} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & Qwen3 & GPT-4o & Qwen3 & GPT-4o \\\\\n\\midrule\n.50 & .648 & .615 & .770 & .768 \\\\\n.55 & .648 & .615 & .770 & .768 \\\\\n.60 & .656 & .621 & .770 & .768 \\\\\n.65 & .656 & .621 & .767 & .766 \\\\\n.70 & .657 & .623 & .767 & .766 \\\\\n.75 & .657 & .623 & .773 & .760 \\\\\n.80 & .657 & .623 & .773 & .760 \\\\\n.85 & .657 & .623 & .773 & .760 \\\\\n.90 & .665 & .630 & .773 & .760 \\\\\n.95 & .653 & .629 & .765 & .752 \\\\\n.98 & .649 & .642 & .771 & .769 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Direction-Aware Gate Validation}\n\\label{app:gate_validation}\n\nFor verbosity, the direction-aware NLI gate admits 21 additional pairs (32\\%) compared to strict bidirectional verification.\nThe two groups show no significant difference in BT win probability (78.5\\% bidirectional vs.\\ 73.8\\% DA-only; permutation $p = .663$; $\\Delta = {-}1.1$pp, 95\\% CI $[{-}5.6, {+}3.0]$) or Likert $d$ ($0.038$ vs.\\ $0.029$).\nBoth groups exhibit the Blindspot pattern (BT significant, Likert NS), confirming that direction-aware gating recovers valid pairs without inflating the effect or introducing selection bias.\nCross-judge validation on all 21 direction-aware pairs confirms this: Fisher exact tests comparing BT estimates between direction-aware and bidirectional-pass subsets are non-significant for all five judges ($p > 0.66$), indicating that the DA-gate does not differentially affect any judge's preference signal.\nFor formality, strict bidirectional verification is appropriate: a relaxed (direction-aware) gate would admit 9 additional pairs with reversed preference (BT 33.4\\%), indicating content preservation failure rather than genuine style preference.\nThis asymmetry empirically justifies the axis-dependent gating strategy described in Section~\\ref{sec:nli_gate}.\n\n\\section{Claude Sonnet 4 Equivalence Testing}\n\\label{app:claude_tost}\n\nClaude Sonnet~4 exhibits benchmark-dependent sensitivity ($n = 88$; LLMBar BT 56.2\\%/54.1\\%, $p = 0.091$/$0.284$).\nFormal equivalence testing \\citep[TOST;][]{lakens2017equivalence} yields margin-dependent conclusions (Table~\\ref{tab:tost_sensitivity}): per-axis equivalence is confirmed at $\\Delta = 15$pp ($p = .010$), corresponding to a BT threshold of 65\\%.\nAt $\\Delta = 10$pp, per-axis TOST is not significant ($p = .156$, power $\\approx 42\\%$).\nPooling both axes ($n = 174$, BT $= 55.17\\%$) achieves equivalence at $\\Delta = 12$pp ($p = .035$) but not at $\\Delta = 10$pp ($p = .100$), tightening the bound on Claude's style sensitivity.\nWe adopt $\\Delta = 12$pp as it corresponds to a small effect (Cohen's $h = 0.24$), below which style sensitivity is unlikely to materially affect downstream RLHF reward modeling; a 12pp BT shift means ${\\sim}12\\%$ of preference pairs change direction. This is also the smallest margin at which pooled significance is achieved.\nWe report all tested margins for transparency.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST equivalence sensitivity for Claude. Per-axis: formality only (BT $= 0.562$, $n = 88$). Pooled: both axes combined ($n = 174$).}\n\\label{tab:tost_sensitivity}\n\\begin{tabular}{ccl}\n\\toprule\n$\\Delta$ (pp) & $p$ & Result \\\\\n\\midrule\n5 & .626 & Not equivalent (per-axis) \\\\\n10 & .156 & Not equivalent (per-axis) \\\\\n10 & .100 & Not equivalent (pooled) \\\\\n12 & .035 & Equivalent (pooled) \\\\\n15 & .010 & Equivalent (per-axis) \\\\\n20 & .0001 & Equivalent (per-axis) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Bayesian equivalence.}\nWe complement frequentist TOST with Bayesian equivalence testing to quantify evidence strength for the null hypothesis.\nTable~\\ref{tab:bayesian_equiv} reports BF$_{01}$ (evidence for null over alternative) under three half-normal prior scales.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Bayesian equivalence (BF$_{01}$) for Claude Sonnet~4 Likert ATE. BF$_{01} > 3$: moderate evidence for null; $1$--$3$: anecdotal; $< 1$: favors alternative.}\n\\label{tab:bayesian_equiv}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nData & $\\sigma = 0.3$ & $\\sigma = 0.5$ & $\\sigma = 1.0$ \\\\\n\\midrule\nPooled ($n = 348$) & 0.57 & 0.80 & 1.48 \\\\\nVerbosity & 1.40 & 2.03 & 3.78 \\\\\nFormality & 0.74 & 0.97 & 1.73 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPooled evidence is inconclusive (BF$_{01} < 3$ across all priors), consistent with Claude exhibiting a small (${\\sim}5$pp) rather than zero style preference on LLMBar.\nVerbosity alone approaches moderate evidence for the null (BF$_{01} = 2.03$--$3.78$); formality pulls down the pooled estimate (BF$_{01} = 0.74$--$1.73$).\n\n\\section{Bradley-Terry Goodness of Fit and Stratified Analysis}\n\\label{app:bt_gof}\n\nBradley-Terry goodness-of-fit tests confirm adequate model fit for both axes (formality: deviance $= 52.80$, $\\text{df} = 45$, $p = 0.198$; verbosity: $p = 0.905$).\nStratified analysis of consistent pairs by original-text direction reveals no preference heterogeneity for verbosity (Fisher $p = 0.453$) but significant direction asymmetry for formality ($88.9\\%$ vs.\\ $52.6\\%$, Fisher $p = 0.015$), independently confirming the originality confound structure identified by GEE (Table~\\ref{tab:gee}).\n\nTo assess robustness to originality confounding, we restrict to pairs where the judge assigned equal Likert scores to original and counterfactual texts (eliminating detectable quality differences).\nStyle preference persists: formality BT $= 67.3\\%$ ($n = 55$, $\\Delta = {+}0.8$pp from full sample, 95\\% CI $[{-}11.0, {+}12.6]$); verbosity BT $= 76.0\\%$ ($n = 50$, $\\Delta = {-}1.3$pp, 95\\% CI $[{-}13.3, {+}10.3]$).\nIn the anti-originality subset (pairs where the original never wins), effects strengthen (formality $75.0\\%$, verbosity $86.1\\%$), confirming that style preference is not an artifact of originality confounding.\n\n\\section{Bradley-Terry Confidence Intervals}\n\\label{app:bt_ci}\n\nTable~\\ref{tab:bt_ci} reports bootstrap 95\\% confidence intervals for all Bradley-Terry estimates in Table~\\ref{tab:main_results}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for BT win probabilities (10{,}000 pair-level resamples).}\n\\label{tab:bt_ci}\n\\begin{tabular}{lllc}\n\\toprule\nBench & Judge & Axis & BT $P$ [95\\% CI] \\\\\n\\midrule\nLLMBar & GPT-4o & Form.\\ & .630 [.557, .703] \\\\\n & GPT-4o & Verb.\\ & .760 [.667, .853] \\\\\n & GPT-4o & Reg.\\ & .570 [.468, .673] \\\\\n\\cmidrule{2-4}\n & Qwen3 & Form.\\ & .665 [.585, .739] \\\\\n & Qwen3 & Verb.\\ & .773 [.703, .843] \\\\\n & Qwen3 & Reg.\\ & .553 [.479, .628] \\\\\n\\cmidrule{2-4}\n & Llama-70B & Form.\\ & .695 [.619, .765] \\\\\n & Llama-70B & Verb.\\ & .735 [.655, .809] \\\\\n & Llama-70B & Reg.\\ & .635 [.555, .712] \\\\\n\\cmidrule{2-4}\n & Claude & Form.\\ & .562 [.489, .636] \\\\\n & Claude & Verb.\\ & .541 [.459, .616] \\\\\n\\midrule\nAEval & GPT-4o & Form.\\ & .727 [.663, .785] \\\\\n & Qwen3 & Form.\\ & .657 [.581, .733] \\\\\n & Qwen3 & Verb.\\ & .841 [.774, .902] \\\\\n\\midrule\nMTB & GPT-4o & Form.\\ & .692 [.623, .753] \\\\\n & Qwen3 & Form.\\ & .712 [.630, .788] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Bootstrap Attenuation Analysis}\n\\label{app:bootstrap_attenuation}\n\nTo distinguish measurement attenuation from insufficient statistical power, we subsample the $n = 355$ formality replication (Qwen3-32B) at seven sample sizes and compute Likert Cohen's $d$ with bootstrap 95\\% CIs at each (Table~\\ref{tab:attenuation}).\nUnder a power limitation, $d$ would remain constant while only $p$-values improve with larger $n$; under measurement attenuation, $d$ itself converges to zero.\nThe data support attenuation: $d_{\\text{median}} = {-}0.017$ across all sample sizes, with CIs narrowing from ${\\pm}0.3$ to ${\\pm}0.1$ but never excluding zero.\nThe same data yield BT $= 66.5\\%$ ($p < 0.0001$), confirming that the pairwise signal is robust.\nVerbosity shows a similar pattern ($d \\approx 0.15$--$0.19$, stable, CIs always containing zero; BT $= 76$--$77\\%$, $p < 0.0001$).\nWithin the agnostic framework of \\S\\ref{sec:likert_pairwise}, this evidence favors the measurement attenuation interpretation but does not exclude construct divergence.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Bootstrap attenuation analysis: formality $\\times$ Qwen3-32B. Likert $d$ remains flat near zero across sample sizes while BT is stable at 66.5\\%.}\n\\label{tab:attenuation}\n\\begin{tabular}{@{}rccc@{}}\n\\toprule\n$n$ & Likert $d$ & 95\\% CI & Contains 0? \\\\\n\\midrule\n50 & $-$0.017 & [$-$0.308, 0.262] & Yes \\\\\n100 & $-$0.015 & [$-$0.219, 0.176] & Yes \\\\\n150 & $-$0.019 & [$-$0.179, 0.145] & Yes \\\\\n200 & $-$0.016 & [$-$0.157, 0.119] & Yes \\\\\n250 & $-$0.018 & [$-$0.144, 0.107] & Yes \\\\\n300 & $-$0.018 & [$-$0.131, 0.095] & Yes \\\\\n355 & $-$0.017 & [$-$0.123, 0.087] & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Formal Power Analysis}\n\\label{app:power_analysis}\n\nTable~\\ref{tab:power} reports the sample size required for Likert ATE to achieve 80\\% power at observed effect sizes across all six judge$\\times$axis cells.\nRequired sample sizes range from $336$ (Qwen3-32B verbosity, $d = 0.153$) to $27{,}159$ (Qwen3-32B formality, $d = {-}0.017$), representing $4$--$206\\times$ the current $n$.\nFor five of six cells, the required $n$ exceeds $1{,}200$---far beyond typical evaluation budgets---converging with the bootstrap attenuation curve (Appendix~\\ref{app:bootstrap_attenuation}) to confirm the Blindspot as a structural measurement limitation.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Required Likert sample size for 80\\% power at observed $d$. BT detects all six effects at $p < 0.001$ with $n \\leq 100$.}\n\\label{tab:power}\n\\begin{tabular}{@{}llcrc@{}}\n\\toprule\nJudge & Axis & Observed $d$ & Required $n$ & Ratio \\\\\n\\midrule\nGPT-4o & Form.\\ & 0.073 & 1{,}473 & 16.7$\\times$ \\\\\nGPT-4o & Verb.\\ & 0.080 & 1{,}227 & 14.3$\\times$ \\\\\nQwen3 & Form.\\ & $-$0.017 & 27{,}159 & 76.5$\\times$ \\\\\nQwen3 & Verb.\\ & 0.153 & 336 & 3.9$\\times$ \\\\\nLlama-70B & Form.\\ & 0.021 & 18{,}157 & 206.3$\\times$ \\\\\nLlama-70B & Verb.\\ & 0.034 & 6{,}737 & 78.3$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Formality Sensitivity Hierarchy}\n\\label{app:sensitivity}\n\nTable~\\ref{tab:sensitivity} applies seven measurement methods to the same formality style-transformed data (GPT-4o, LLMBar, $n = 88$).\nOnly pairwise methods reach significance; all Likert-based methods fail regardless of scaling assumption.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Sensitivity hierarchy: seven measurement methods applied to the same formality data. Only pairwise methods (top two rows) reach significance.}\n\\label{tab:sensitivity}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & Statistic & $p$ & Data \\\\\n\\midrule\nBT model & 63.0\\% $[55.7, 70.3]$ & $0.0004$ & All 173 comp. \\\\\nSign test (filtered) & 73.9\\% (34/46) & 0.006 & Consistent \\\\\n\\midrule\nLikert ATE ($t$-test) & $d = 0.102$ & 0.332 & NLI$\\geq$0.90 \\\\\nBinarized Likert & 60.6\\% & 0.296 & Non-tied \\\\\nOrdinal reg.\\ (prop.\\ odds) & $\\beta = {-}0.079$ & 0.769 & NLI$\\geq$0.90 \\\\\nGEE (exchangeable) & $\\beta = {-}0.084$ & 0.587 & NLI$\\geq$0.90 \\\\\nWilcoxon signed-rank & $W = 274$ & 0.905 & NLI$\\geq$0.90 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Verbosity Sensitivity Hierarchy}\n\\label{app:verb_sensitivity}\n\nTable~\\ref{tab:verb_sensitivity} replicates the seven-method sensitivity analysis (Table~\\ref{tab:sensitivity}) on the verbosity axis ($n = 86$ NLI-filtered pairs, Qwen3-32B judge, LLMBar).\nThe attenuation pattern is more extreme than formality: all six Likert-based methods remain non-significant (lowest $p = 0.213$) despite a stronger pairwise signal (BT 77.3\\% vs.\\ 66.5\\% for formality), and Likert effect sizes ($d = 0.036$--$0.056$) are near zero.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Sensitivity hierarchy for verbosity ($n = 86$, Qwen3-32B, LLMBar). All Likert methods fail; only BT reaches significance.}\n\\label{tab:verb_sensitivity}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Statistic & $p$ & Sig? \\\\\n\\midrule\nBT model & 77.3\\% $[70.3, 84.3]$ & ${<}0.001$ & Yes \\\\\n\\midrule\nLikert ATE & $d = 0.056$ & 0.691 & No \\\\\nBinarized $\\chi^2$ & OR $= 2.16$ & 0.213 & No \\\\\nOrdinal reg.\\ & $\\beta = 0.159$ & 0.575 & No \\\\\nPaired $t$-test & $d = 0.056$ & 0.607 & No \\\\\nMann-Whitney $U$ & $r = {-}0.046$ & 0.578 & No \\\\\nCohen's $d$ & $d = 0.036$ & --- & No \\\\\n\\bottomrule\n\\multicolumn{4}{p{0.9\\columnwidth}}{\\footnotesize Effect sizes use style-aligned scoring (verbose $-$ concise), isolating style preference direction. Table~\\ref{tab:main_results} reports RATE-compatible ATE (counterfactual $-$ original), which conflates style and originality effects.}\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scaled Replication ($n = 330$)}\n\\label{app:verb_n355}\n\nTable~\\ref{tab:verb_n355} reports verbosity results at $n = 330$ (from 355 generated pairs, 330 passing NLI gate at $\\tau = 0.90$), replicating across four judges (GPT-4o was not re-scored at this scale).\nThe Blindspot partially resolves for judges with strong style effects: Qwen3-32B ($d = .149$, $p < .001$) and Llama-70B ($d = .160$, $p < .001$) now reach Likert significance, consistent with the power curve (Figure~\\ref{fig:power_curve}) predicting ${\\sim}40\\%$ power at $n = 330$ for $d \\approx 0.15$.\nHowever, two judges maintain the Blindspot: Gemini-2.5-Flash ($d = .087$, borderline) and Claude Sonnet~4 ($d = .032$, NS).\nThe magnitude discrepancy persists even where Likert reaches significance: BT detects 73--76\\% win rates while Likert yields $d \\approx 0.15$, confirming the attenuation interpretation.\n\nGEE conditional decomposition at $n = 330$ confirms substantial shrinkage from $n = 88$ estimates, consistent with more extreme initial estimates producing larger corrections \\citep{nemes2009bias}: Qwen3 $13.10 \\to 3.83$ ($-71\\%$), Llama $8.21 \\to 4.01$ ($-51\\%$), Gemini $8.98 \\to 2.52$ ($-72\\%$).\nDespite shrinkage, verbosity remains style-dominated for these three judges (Style OR $2.5$--$4.0$, all $p < .001$; Orig OR $0.52$--$0.69$).\nClaude shows a non-significant style effect at $n = 330$ (Style OR $= 1.22$, $p = .134$), with its elevated BT reflecting originality rather than style preference (Orig OR $= 1.69$).\nAs predicted by the power analysis (Figure~\\ref{fig:power_curve}), Likert begins detecting the strongest effects at $n \\approx 330$ (Qwen3 $d = .15$, $p < .001$; Llama $d = .16$, $p < .001$), while two judges maintain the Blindspot (Claude $d = .03$, NS; Gemini borderline $d = .09$, $p = .02$ by Wilcoxon but $p = .11$ by $t$-test).\nThe efficiency gap---Likert requiring $3$--$4\\times$ the sample size pairwise needs---rather than absolute failure, is the practical concern.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Verbosity scaled replication ($n = 330$, four judges; GPT-4o not re-scored). Blindspot partially resolves for strong effects (Qwen3, Llama-70B) but persists for weaker-effect judges (Gemini, Claude).}\n\\label{tab:verb_n355}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nJudge & BT $P(\\text{V})$ & [95\\% CI] & Likert $d$ ($p$) & Blindspot? \\\\\n\\midrule\nQwen3-32B & .733$^{***}$ & [.696, .770] & .149 (.001) & No \\\\\nLlama-70B & .759$^{***}$ & [.722, .793] & .160 ({<}.001) & No \\\\\nGemini-2.5 & .678$^{***}$ & [.638, .717] & .087 (.021) & $\\dagger$ \\\\\nClaude S4 & .608$^{***}$ & [.567, .649] & .032 (.317) & $\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\par\\vspace{2pt}\n{\\footnotesize $^{***}$\\,$p < 0.001$. $\\dagger$ marks Blindspot cases (BT significant, Likert $d$ non-significant at $\\alpha = 0.05$ by Wilcoxon). Likert $p$ values from Wilcoxon signed-rank test on non-zero differences.}\n\\end{table}\n\n\\section{100-Point Continuous Likert Scale}\n\\label{app:likert100}\n\nTo test whether the Blindspot reflects integer-scale granularity rather than a paradigm difference between absolute and relative evaluation, we replicate the formality experiment using a 100-point continuous scale ($1$--$100$) with three judges (Table~\\ref{tab:likert100}).\nAll three judges remain non-significant (all $p > 0.15$).\nTie rates decrease substantially with finer granularity (1--10 scale: 58--73\\%; 1--100 scale: 40--66\\%), yet ATE remains non-significant, confirming the gap reflects measurement mode rather than scale granularity \\citep{preston2000scale}.\nJudges differ markedly in effective granularity usage: GPT-4o clusters scores into ${\\sim}5$ distinct bins (modes at 70, 75, 80), Qwen3-32B uses ${\\sim}20$ distinct values spanning $45$--$95$, and Llama-70B exploits $50{+}$ unique scores with near-uniform coverage---yet none resolves the Blindspot.\nScore distributions are unimodal and right-skewed for all three judges, with medians in the $72$--$80$ range; the score \\emph{difference} distributions (original minus rewrite) are symmetric around zero, confirming no net directional shift under Likert scoring.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Formality Likert ATE: 1--10 vs.\\ 1--100 scale. Finer granularity reduces tie rates but does not resolve the Blindspot (all 1--100 $p > 0.15$).}\n\\label{tab:likert100}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nJudge & 1--10 $d$ ($p$) & 1--100 $d$ ($p$) & Tie 1--10 & Tie 1--100 \\\\\n\\midrule\nGPT-4o & --- & $-$.038 (.725) & --- & 65.9\\% \\\\\nQwen3-32B & .012 (.908) & .153 (.154) & 72.7\\% & 51.1\\% \\\\\nLlama-70B$^a$ & .000 (1.00) & .085 (.440) & 72.7\\% & 39.8\\% \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^a$ 5 pairs returned score $= 0$ (out of range); effective $n = 83$.}\n\\end{tabular}}\n\\end{table}\n\n\\section{NLI Gate Ablation}\n\\label{app:nli_ablation}\n\nTable~\\ref{tab:nli_ablation} compares BT estimates across NLI-pass, NLI-fail, and all pairs.\nFor formality, NLI-fail pairs reverse to 41.7\\% (preferring casual over formal), demonstrating that the gate removes content-confounded pairs rather than amplifying style signal.\nThe small NLI-fail sample ($n \\approx 12$) limits precision; this serves as a bounding analysis.\nFor verbosity, NLI-fail pairs remain at 75.0\\%, consistent with the dominant style effect (OR $= 13.10$) overwhelming content noise.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI gate ablation: BT win probability by NLI subset.}\n\\label{tab:nli_ablation}\n\\begin{tabular}{lccc}\n\\toprule\nAxis & NLI-pass & NLI-fail & All \\\\\n\\midrule\nFormality & 66.5\\% & 41.7\\% & 63.0\\% \\\\\nVerbosity & 77.3\\% & 75.0\\% & 76.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Rewriting Artifact Control}\n\\label{app:artifact_control}\n\nSame-style double-rewrite (DR) controls quantify the rewriting artifact using BT models (consistent with all other pairwise analyses).\nTable~\\ref{tab:artifact} reports BT $P(\\text{original})$---the probability the judge prefers the original over its same-style DR.\nBoth judges systematically prefer LLM-polished text across axes; for verbosity, BT $P(\\text{original}) < 0.17$ indicates that rewriting quality dominates when content is held constant, validating the GEE decomposition that separates style from artifact effects.\nSame-style double-rewrite controls for style-neutral polishing artifacts but cannot exclude style-specific polishing interactions (e.g., formal rewriting may polish differently than casual rewriting).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Rewriting artifact: BT $P(\\text{orig})$ vs.\\ same-style double-rewrite (bootstrap 95\\% CI, 10{,}000 resamples). Values ${<}0.5$: judges prefer LLM-polished text.}\n\\label{tab:artifact}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nAxis & Judge & BT $P(\\text{orig})$ [CI] & $p$ \\\\\n\\midrule\nForm.\\ & GPT-4o & .418 [.342, .500] & .037 \\\\\n & Qwen3 & .377 [.303, .451] & .0006 \\\\\n\\midrule\nVerb.\\ & GPT-4o & .167 [.084, .262] & ${<}.0001$ \\\\\n & Qwen3 & .082 [.035, .140] & ${<}.0001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Implementation Details}\n\\label{app:implementation}\n\n\\paragraph{Models and APIs.}\nStyle-controlled rewriting uses Qwen3-32B (temperature $0.7$, top-$p$ $0.9$).\nTarget judges: GPT-4o (\\texttt{gpt-4o-2024-08-06}, accessed April--May 2026), Qwen3-32B (locally hosted), Llama-3.3-70B (locally hosted via vLLM).\nClaude Sonnet 4 (\\texttt{claude-sonnet-4-20250514}, accessed May 2026) provides discriminative validity evidence with benchmark-dependent sensitivity.\nAll judge calls use temperature $0$ and $\\texttt{max\\_tokens} = 2048$.\n\n\\paragraph{NLI gate.}\nContent preservation is verified using DeBERTa-v3-large \\citep{he2021debertav3} fine-tuned on MNLI, with entailment threshold $\\tau = 0.90$.\nBidirectional entailment is applied for formality and register; direction-aware entailment for verbosity (Section~\\ref{sec:nli_gate}).\n\n\\paragraph{Statistical methods.}\nBradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \\citep{hunter2004mm} using the \\texttt{choix} Python library (default L2 regularization $\\alpha = 10^{-6}$); varying $\\alpha$ from $10^{-6}$ to $1.0$ changes all BT probabilities by ${<}0.002$.\nAll bootstrap CIs use 10{,}000 pair-level resamples with seed $42$.\nGEE models use exchangeable working correlation with robust (sandwich) standard errors via \\texttt{statsmodels} (Section~\\ref{sec:direction}; diagnostics in Appendix~\\ref{app:gee_diagnostics}).\n\n\\paragraph{Benchmarks.}\nLLMBar \\citep{zeng2023llmbar}: 100 instruction-response pairs ($n = 88$ after NLI gate, $n = 355$ for scaled replication).\nAlpacaEval \\citep{dubois2025lc}: 100 sampled pairs.\nMT-Bench \\citep{zheng2023judging}: 80 multi-turn pairs.\n\n\\paragraph{Code and data.}\nAll code, prompts, and experimental data will be released upon acceptance under an open-source license.\n\n\\section{Holm-Bonferroni Sensitivity Analysis}\n\\label{app:holm8}\n\nTable~\\ref{tab:holm8} reports adjusted $p$-values under the full 8-test family (4 judges $\\times$ 2 primary axes), including Gemini-2.5-Flash which is excluded from the primary 6-test family (\\S\\ref{sec:stat_framework}).\nAll results remain significant at $\\alpha = 0.05$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Holm-Bonferroni sensitivity analysis: 8-test family (4 judges $\\times$ 2 primary axes). All results remain significant under the expanded family ($\\alpha = 0.05$).}\n\\label{tab:holm8}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}cllcccc@{}}\n\\toprule\nRank & Judge & Axis & BT $P$ & Raw $p$ & Threshold & Adj.\\ $p$ \\\\\n\\midrule\n1 & Gemini Flash & Verb.\\ & .708 & ${<}.0001$ & .00625 & ${<}.001$ \\\\\n2 & GPT-4o & Verb.\\ & .760 & .0001 & .00714 & .0007 \\\\\n3 & Qwen3-32B & Form.\\ & .665 & .0001 & .00833 & .0007 \\\\\n4 & Qwen3-32B & Verb.\\ & .773 & .0001 & .0100 & .0007 \\\\\n5 & Llama-70B & Form.\\ & .695 & .0001 & .0125 & .0007 \\\\\n6 & Llama-70B & Verb.\\ & .735 & .0001 & .0167 & .0007 \\\\\n7 & GPT-4o & Form.\\ & .630 & .0004 & .0250 & .0008 \\\\\n8 & Gemini Flash & Form.\\ & .574 & .0306 & .0500 & .0306 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Cross-Axis Contamination Analysis}\n\\label{app:cross_axis_contamination}\n\nOur per-axis design assumes that rewriting along one style axis does not substantially alter the text along other axes.\nWe quantify cross-axis contamination by measuring off-target surface proxies before and after rewriting.\nFor formality rewrites ($n = 355$), we measure word count and sentence count as verbosity proxies; for verbosity rewrites ($n = 86$), we measure type-token ratio (TTR) as a lexical diversity proxy for formality, and Flesch-Kincaid (FK) grade level.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-axis contamination: effect of rewriting along one style axis on surface proxies of the other axis. Cohen's $d$: $|d| < 0.20$ negligible, $0.20$--$0.50$ small contamination \\citep{cohen1988statistical}.}\n\\label{tab:cross_axis}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrl@{}}\n\\toprule\nDirection & Proxy & $\\Delta$ & $d$ & Interp.\\ \\\\\n\\midrule\nForm.\\ $\\to$ Verb.\\ & Word count & $-3.4\\%$ & $-0.23$ & Small \\\\\nForm.\\ $\\to$ Verb.\\ & Sent.\\ count & $-0.2\\%$ & $-0.03$ & Negligible \\\\\nVerb.\\ $\\to$ Form.\\ & TTR & $-0.006$ & $-0.04$ & Negligible \\\\\nVerb.\\ $\\to$ Form.\\ & FK grade & --- & $0.50$ & Confounded$^*$ \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^*$ FK $=$ $f$(sentence length, word length); sentence length change is}\\\\\n\\multicolumn{5}{l}{\\footnotesize inherent to verbosity manipulation, not formality contamination.}\n\\end{tabular}}\n\\end{table}\n\nFormality rewrites leave sentence structure virtually unchanged ($d = -0.03$); the word count shift ($d = -0.23$, exceeding the negligible threshold but within the small range) reflects word-level adjustments (contractions, elaboration) that are directionally symmetric (formal$\\to$casual $-5.0\\%$, casual$\\to$formal $+5.6\\%$) and do not constitute verbosity contamination.\nVerbosity rewrites leave lexical diversity unchanged (TTR $d = -0.04$); the elevated FK grade ($d = 0.50$) is an artifact of FK's dependence on sentence length, which changes by design in verbosity manipulation.\nThese results confirm that cross-axis contamination is small to negligible for the proxies measured; the GEE originality term (\\S\\ref{sec:direction}) provides additional protection by absorbing any residual quality confound.\nA robustness check adding word-count change as a GEE covariate leaves all Style ORs virtually unchanged ($\\Delta < 12\\%$, all covariate $p > .28$), confirming that the small cross-axis word-count shift does not confound formality estimates.\n\n\\section{FK Length-Control Analysis}\n\\label{app:fk_length}\n\nThe elevated FK grade shift for verbosity rewrites ($d = 0.50$; Table~\\ref{tab:cross_axis}) could reflect genuine formality contamination or simply FK's structural dependence on sentence length.\nWe disentangle these via length-controlled regression and mediation analysis.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Descriptive statistics for FK grade and sentence length changes by rewriting axis. Computed on all pairs; regression analysis below uses NLI-verified pairs only ($n_{\\text{form}} = 88$, $n_{\\text{verb}} = 86$).}\n\\label{tab:fk_desc}\n\\begin{tabular}{@{}llrr@{}}\n\\toprule\nAxis & Metric & $\\Delta$ & $d$ \\\\\n\\midrule\nVerbosity & FK grade & $+2.26$ & $0.50$ \\\\\nVerbosity & Sent.\\ length (words) & $+3.40$ & $0.35$ \\\\\nFormality & FK grade & $-0.30$ & $-0.08$ \\\\\nFormality & Sent.\\ length (words) & $-0.11$ & $-0.04$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRegressing FK change on style axis without controls yields $\\beta = 2.69$ ($p < .001$, $R^2 = 0.100$); adding sentence length as a covariate reduces the coefficient to $\\beta = 1.07$ ($p = .020$, $R^2 = 0.546$), a 60.3\\% reduction.\nSobel mediation test confirms that sentence length mediates 60\\% of the total effect ($z = 2.15$, $p = .031$); the 40\\% residual direct effect reflects multi-syllable vocabulary shifts (e.g., ``use'' $\\to$ ``utilize'') that are inherent to verbose style rather than formality contamination.\n\n\\paragraph{GEE with FK covariate.}\nAs a further robustness check, we add FK grade change as a covariate to the GEE formality model.\nFK grade is not independently significant for any judge ($p > .11$), but its inclusion reduces formality Style ORs by 20--51\\% due to collinearity between formality and readability: GPT-4o Style OR drops from $2.70$ to $2.15$ ($p = .132$, no longer significant); Qwen3-32B from $4.20$ to $3.38$ ($p = .014$); Llama-70B from $5.52$ to $2.69$ ($p = .037$).\nTwo of three judges retain significant formality effects after readability control, confirming that formality style sensitivity is not fully reducible to readability differences.\n\n\\section{Human Annotation Agreement Statistics}\n\\label{app:annotation_agreement}\n\nTwo independent annotators evaluated 100 NLI-scored pairs (50 formality, 50 verbosity), stratified into 70 NLI-pass and 30 NLI-fail pairs for content preservation.\nAnnotator~1 (A1) judged 99/100 pairs content-preserving; Annotator~2 (A2) judged 97/100.\n\n\\paragraph{Agreement.}\nOn the \\emph{preserves\\_meaning} label, 96/100 pairs are concordant, yielding Gwet's AC$_1 = 0.958$ \\citep{gwet2008ac1}.\nCohen's $\\kappa = {-}0.015$ is misleading here: with ${>}96\\%$ positive prevalence, chance agreement is near-ceiling and $\\kappa$ is compressed toward zero regardless of actual agreement---the well-documented prevalence paradox \\citep{feinstein1990kappa}.\nAC$_1$ is the appropriate statistic under such extreme marginal distributions.\n\n\\paragraph{Gate pass precision.}\nBoth annotators independently confirm 69/70 gate-passed pairs as content-preserving ($98.6\\%$; Wilson CI $[92.3\\%, 99.8\\%]$).\nOnly two gate-passed pairs were flagged by either annotator (S073 and S063, both formality); excluding these changes BT by ${<}0.3$\\,pp and Style OR by ${<}4\\%$ relative, with all significance levels unchanged.\n\n\\paragraph{Gate-failed analysis.}\nAmong 30 gate-rejected pairs, A1 judges 30/30 and A2 judges 28/30 as content-preserving, confirming that the gate's dominant error mode is false rejection rather than false acceptance.\nThis conservative calibration ensures high pass precision at the cost of reduced recall (59.5\\%).\n\n\\paragraph{Disagreement analysis.}\nFour pairs show annotator disagreement: S073, S098, S063, S136 (3 formality, 1 verbosity; 2 NLI-pass, 2 NLI-fail).\nAll disagreements involve borderline meaning-equivalence judgments rather than clear content contamination.\n\n\\paragraph{Comparison with 50-pair pilot.}\nThe expanded 100-pair annotation tightens the precision estimate from $84$--$100\\%$ (individual annotators on 25 gate-passed pairs) to $98.6\\%$ (both annotators concordant on 70 gate-passed pairs), and raises AC$_1$ from $0.65$ to $0.96$.\n\n\\paragraph{Style detection agreement.}\nAgreement on \\emph{style\\_change\\_detected} is lower ($58\\%$, $\\kappa = 0.138$, AC$_1 = 0.206$), reflecting genuine difficulty in judging whether a rewrite altered style.\nThis does not affect the primary validation target, which concerns content preservation rather than style detection.\n\n\\section{Cross-Benchmark Replication}\n\\label{app:cross_bench}\n\nTable~\\ref{tab:cross_bench} reports cross-benchmark replication results on AlpacaEval and MT-Bench.\nSelection criterion: we targeted the six judge$\\times$axis cells with the largest LLMBar BT effects (BT $\\geq .63$, all $p < .001$), prioritizing cells where the Blindspot was strongest.\nThe remaining 18/24 cells (3 benchmarks $\\times$ 4 target judges $\\times$ 2 axes, minus 6 tested) were not evaluated; generalization to weaker-effect configurations remains open.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-benchmark replication on AlpacaEval (AEval) and MT-Bench (MTB). $\\ddagger$: both BT and Likert significant; $\\dagger$: Blindspot (BT significant, Likert not).}\n\\label{tab:cross_bench}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lllccc@{}}\n\\toprule\nBench & Judge & Axis & BT $P$ & Likert $d$ ($p$) & Cat.\\ \\\\\n\\midrule\nAEval & GPT-4o & Form.\\ & .727$^{***}$ & .005 (.909) & $\\dagger$ \\\\\n & Qwen3 & Form.\\ & .657$^{***}$ & .081 (.198) & $\\dagger$ \\\\\n & Qwen3 & Verb.\\ & .841$^{***}$ & .375 (.0003) & $\\ddagger$ \\\\\n & Llama-70B & Form.\\ & .750$^{***}$ & .212 (.012) & $\\ddagger$ \\\\\n\\midrule\nMTB & GPT-4o & Form.\\ & .692$^{***}$ & .111 (.016) & $\\ddagger$ \\\\\n & Qwen3 & Form.\\ & .712$^{***}$ & .149 (.007) & $\\ddagger$ \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^{***}$ $p < 0.001$. $\\ddagger$: both sig.;\\; $\\dagger$: Blindspot.}\n\\end{tabular}}\n\\end{table}\n\n\\section{Claude Cross-Benchmark Analysis}\n\\label{app:claude_crossbench}\n\nClaude Sonnet~4 exhibits near-null style sensitivity on LLMBar (\\S\\ref{sec:amplification}; Appendix~\\ref{app:claude_tost}).\nCross-benchmark GEE decomposition reveals that Claude's elevated aggregate BT on AEval/MT-Bench reflects quality detection rather than style preference.\nTable~\\ref{tab:claude_crossbench} reports results across all five tested configurations.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Claude Sonnet~4 cross-benchmark results with GEE decomposition. Formality Style OR is non-significant across all three benchmarks; elevated BT on AEval/MT-Bench is driven by Orig OR (quality detection). AEval verbosity is the sole genuine style effect.}\n\\label{tab:claude_crossbench}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccccc@{}}\n\\toprule\nBench & Axis & BT $P$ & Likert $d$ ($p$) & Style OR ($p$) & Orig OR ($p$) \\\\\n\\midrule\nLLMBar & Form.\\ & .562 & $-$.021 (.721) & 1.47 (.276) & 6.66 (${<}.001$) \\\\\nLLMBar & Verb.\\ & .541 & $-$.039 (.743) & 1.52 (.286) & 0.80 (.563) \\\\\n\\midrule\nAEval & Form.\\ & .698$^{***}$ & .081 (.090) & 1.99 (.082) & 9.33 (${<}.001$) \\\\\nAEval & Verb.\\ & .683$^{***}$ & .252 (.002) & \\textbf{4.76} (${<}.001$) & 0.87 (.732) \\\\\n\\midrule\nMTB & Form.\\ & .733$^{***}$ & .233 (${<}.001$) & 1.64 (.364) & 11.85 (${<}.001$) \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^{***}$ $p < 0.001$. All Style ORs except AEval verbosity are non-significant.}\\\\\n\\multicolumn{6}{l}{\\footnotesize Negative $d$: styled variant scored lower.}\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Formality.}\nClaude's formality Style OR is non-significant across all three benchmarks ($1.47$/$1.99$/$1.64$, all $p > .08$), indicating consistently low formality sensitivity regardless of benchmark.\nThe elevated BT on AEval (69.8\\%) and MT-Bench (73.3\\%) is driven entirely by Orig OR ($9.33$/$11.85$, both $p < .001$): Claude detects quality differences between original and counterfactual texts without exhibiting formality preference.\nAEval formality produces a Blindspot (BT significant, Likert n.s.), but GEE decomposition reveals this as quality detection rather than style sensitivity---illustrating why aggregate BT alone is insufficient for bias attribution.\n\n\\paragraph{Verbosity.}\nAEval verbosity is the sole configuration where Claude exhibits genuine style sensitivity (Style OR $= 4.76$, $p < .001$; Orig OR $= 0.87$, n.s.), a style-dominated pattern.\nLLMBar verbosity remains null (Style OR $= 1.52$, n.s.), confirming benchmark-dependent sensitivity.\n\n\\section{Rewriting Prompts}\n\\label{app:rewriting_prompts}\n\nBelow are the axis-specific rewriting prompts used in Section~\\ref{sec:rewriting}. All prompts are issued to Qwen3-32B-Instruct at temperature 0.7.\n\n\\paragraph{Formality.}\n\\texttt{Rewrite the following text to be more [formal/casual] while preserving the exact same content and meaning. Do not add, remove, or change any factual information. Only adjust the level of formality in the language.}\n\n\\paragraph{Verbosity.}\n\\texttt{Rewrite the following text to be more [verbose/concise] while preserving the exact same content and meaning. Do not add, remove, or change any factual information. Only adjust the level of detail and elaboration.}\n\n\\paragraph{Register.}\n\\texttt{Rewrite the following text to use a more [academic/conversational] register while preserving the exact same content and meaning. Do not add, remove, or change any factual information. Only adjust the register and tone.}\n\n\\paragraph{Same-style double-rewrite.}\n\\texttt{Rewrite the following text in the same style (keep it [formal/casual/verbose/concise]) while preserving the exact same content and meaning. Paraphrase the text without changing its style.}\n\n\\section{Non-Tie Concordance Analysis}\n\\label{app:concordance}\n\nTo adjudicate between measurement attenuation and construct divergence as explanations for the Likert Blindspot (\\S\\ref{sec:likert_pairwise}), we examine whether Likert and pairwise evaluations agree \\emph{when Likert does differentiate}.\nFor each pair where Likert assigned different scores to the two texts (non-tie), we check whether the higher-scoring text matches the pairwise-preferred text; if the two methods measure the same underlying construct, non-tie concordance should substantially exceed chance (50\\%).\nWe additionally compute point-biserial correlations ($r_{\\text{pb}}$) between Likert score differences and pairwise outcomes across all pairs with valid pairwise preferences.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Non-tie concordance between Likert and pairwise preferences. For each judge$\\times$axis condition, we identify Likert non-tie pairs and check agreement with pairwise preference direction. Wilson 95\\% CIs; $p$ from two-sided binomial test against 50\\%. $r_{\\text{pb}}$: point-biserial correlation between Likert score difference and pairwise outcome (all pairs with valid pairwise preference).}\n\\label{tab:concordance}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrcccrc@{}}\n\\toprule\nBench & Config & $n_{\\text{nt}}$ & Conc. & Rate & 95\\% CI & $p$ & $r_{\\text{pb}}$ ($p$) \\\\\n\\midrule\nLLMBar & Llama verb.\\ & 25 & 22 & 88.0\\% & [70.0, 95.8] & ${<}.001$ & .412 (.001) \\\\\n & GPT-4o verb.\\ & 30 & 25 & 83.3\\% & [66.4, 92.7] & ${<}.001$ & .373 (.003) \\\\\n & Llama form.\\ & 18 & 15 & 83.3\\% & [60.8, 94.2] & .008 & .447 (.001) \\\\\n & Qwen3 verb.\\ & 27 & 20 & 74.1\\% & [55.3, 86.8] & .019 & .296 (.019) \\\\\n & Gemini verb.\\ & 24 & 17 & 70.8\\% & [50.8, 85.1] & .064 & .346 (.012) \\\\\n & Qwen3 form.\\ & 15 & 10 & 66.7\\% & [41.7, 84.8] & .302 & .274 (.065) \\\\\n & Gemini form.\\ & 15 & 10 & 66.7\\% & [41.7, 84.8] & .302 & .373 (.012) \\\\\n\\midrule\nAEval & Qwen3 form.\\ & 26 & 20 & 76.9\\% & [57.9, 89.0] & .009 & .203 (.146) \\\\\n & GPT-4o form.\\ & 21 & 15 & 71.4\\% & [50.0, 86.2] & .078 & .340 (.019) \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textbf{Pooled}} & \\textbf{201} & \\textbf{154} & \\textbf{76.6\\%} & \\textbf{[70.3, 81.9]} & $\\mathbf{{<}.001}$ & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nPooled concordance is 76.6\\% (154/201 non-tie pairs; binomial $p < .001$; Table~\\ref{tab:concordance}), substantially exceeding the 50\\% chance baseline.\nPoint-biserial correlations are positive in all nine conditions ($r_{\\text{pb}} = 0.20$--$0.45$), with seven of nine reaching significance ($p < .05$).\nConcordance is highest for verbosity ($74$--$88\\%$) and for Llama-70B across both axes ($83$--$88\\%$), consistent with Llama's lower Likert tie rate (Table~\\ref{tab:likert100}).\n\nThese results favor the measurement attenuation interpretation: when Likert scoring does differentiate between texts, its preference direction aligns with pairwise judgment in more than three-quarters of cases.\nThe primary driver of the Blindspot is thus the high Likert tie rate (60--73\\% across conditions) rather than a fundamental disagreement between the two evaluation paradigms about what constitutes quality.\nThe ${\\sim}23\\%$ discordance rate leaves room for partial construct divergence---pairwise comparison may access quality dimensions that Likert cannot express---but the dominant pattern is signal attenuation through discretization and ceiling effects.\n\n\\section*{Code and Data}\n\nCode and data will be released upon acceptance.\n\n\\section*{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform the related-work section.\n\\end{itemize}\n",
      "numLines": 826,
      "startLine": 1,
      "totalLines": 826
    }
  },
  "sourceToolAssistantUUID": "fe4c1103-4ce0-41c3-af12-f31b5d8aa2f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T06:23:56.752Z_

<details open><summary>🔧 Tool call — Read · `toolu_012ZFAAh9Kc8Lxn3iUPTMCtc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81bf1f67-dcbc-4f2c-9d31-dd5abafb8f11",
  "isSidechain": false,
  "requestId": "req_011CbNooa53iLuiMYGs1uqp2",
  "type": "assistant",
  "uuid": "5594ab93-83b7-463f-bf66-9113f815ce64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CXtb2HkNS4YKuaqB1CQkH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11954,
      "cache_read_input_tokens": 38851,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 38851,
          "cache_creation_input_tokens": 11954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11954
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

_source line 35 · 2026-05-25T06:23:56.823Z_

```json
{
  "parentUuid": "90ecf62a-1cd2-4cab-a02c-1f52554a8c5d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "16c0f664-433c-49e3-8312-88a45152236a",
  "timestamp": "2026-05-25T06:23:56.823Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：causal_style_decomp_judge Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 3 critical, 2 war…",
  "leafUuid": "16c0f664-433c-49e3-8312-88a45152236a",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit causal style decomposition paper for EMNLP 2026",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c"
}
```

---

### Assistant

_source line 38 · 2026-05-25T06:27:21.052Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the tex files. Let me perform a systematic content audit across all the dimensions specified in the instructions.

Let me analyze each dimension:

## 1. 叙事一致性 (Narrative Consistency)

**Abstract's "problem":**
- Likert and pairwise scoring produce divergent style-sensitivity profiles in LLM judges (the "Likert Blindspot")

**Intro's "problem":**
- Same judge, same texts, opposite conclusions (Likert vs pairwise); the Likert Blindspot - measurement-mode divergence where pairwise detects style sensitivity that Likert misses


- This is consistent with Abstract ✓

**Intro's contributions:**
1. Empirical finding: first systematic demonstration that pairwise and Likert formats yield qualitatively divergent style sensitivity profiles across 4 judges, 3 benchmarks, 2 axes
2. Analytical contribution: GEE conditional decomposition reveals per-axis confound structures
3. Practical contribution: CSD operates as a black-box diagnostic

**Method actually does:**
- Style-Controlled Rewriting (per-axis)
- NLI gate for content preservation
- Measurement Protocol (dual Likert + pairwise)
- Design Rationale (causal framework)
This matches contributions ✓

The intro identifies a gap where no existing framework combines per-axis decomposition with interventional identification and confound analysis in a way that's practically applicable. My method's design directly addresses this. The experiments then validate each contribution: Table 1 demonstrates the divergent measurement profiles, the GEE analysis exposes the per-axis confound structures, and the results show the approach works as a practical diagnostic tool. The conclusion ties back to these findings—showing the Likert blindspot across benchmarks, the importance of multi-format audits, and that the method generalizes beyond the specific axes tested.

Now I'm checking whether the narrative stays consistent from abstract through conclusion. The abstract mentions five judges from independent providers, which aligns with the intro's description of four target judges plus Claude Sonnet 4. The two primary axes (formality and verbosity) are consistent throughout, and the three benchmarks mentioned in the abstract match what appears in the experiments. The abstract also references seven statistical methods, which I can confirm in the sensitivity hierarchy section. The claim about Likert effect sizes collapsing at larger sample sizes is supported by the n=355 replication. Let me verify the concordance figures and other key statistics are accurately represented across sections.

I notice the abstract says "replicated across three benchmarks" but the actual cross-benchmark testing only covers 6 out of 24 possible cells. However, the intro already frames this as "selective cross-benchmark validation," so there's no real inconsistency—it's just a matter of how the scope is described. The narrative holds together well.

Now I'm doing a word count check on the abstract. It's a dense paragraph with several complex sentences, so I'm breaking it down piece by piece to estimate the total length, which looks to be somewhere in the 180-200 word range. Likert-only audits may thus fail to surface style-driven preferences that propagate through pairwise-based alignment pipelines. The word count is hovering right around 190–200 words, so I'm flagging this as close to the limit but likely acceptable.

For the introduction, I've structured it across three paragraphs: the opening example and problem definition, the motivation around why LLM judges matter and where existing work falls short, and then our method with key results. The contributions list follows naturally.

The related work section is organized thematically rather than as a list of prior work—covering interventional approaches, style bias in LLM judges, and measurement format sensitivity—which positions our contribution clearly relative to others.

Now I'm checking the contribution-scope alignment. The empirical finding is backed by the main table and forest plot showing cross-benchmark results. The analytical contribution has support from the GEE analysis and additional figures. The practical contribution is demonstrated through the black-box nature of the method. Everything maps cleanly to the evidence.

I'm also verifying the specific claims in the abstract and title match what's actually in the paper. The five judges, two axes of variation, three benchmarks, and seven statistical methods all check out against the tables. There are no orphaned sections—all substantial content ties back to a contribution.

For claim strength, I'm confirming we're not overstating anything. We don't use "significantly outperforms" or claim state-of-the-art. The statistical claims all have p-values and confidence intervals. The specific comparison about pairwise reaching significance where Likert doesn't is directly supported by the data.

Now I'm checking the odds ratio claim in the abstract. The Style OR range of 3–13 appears in the main table at n=88 (8.21–13.10), but the appendix shows 2.5–4.0 at n=330, which dips below 3. The abstract's "3–13" range seems to be trying to cover both sample sizes, though the smaller sample gives the higher estimates. The abstract's "3--13" range technically undershoots the full span of estimates (2.5-13.10), since the scaled replication results at n=330 show odds ratios as low as 2.5. The paper acknowledges the n=88 estimates are upper-bound figures, but the abstract doesn't clarify this distinction, making the stated range slightly conservative compared to what the data actually shows.

Now I'm reviewing the experimental rigor—checking that bootstrap confidence intervals are reported, the baseline comparisons are appropriate, and the statistical corrections are properly applied.  The ablations are thorough, covering the key components like the NLI threshold, rewriter independence, and consistency filtering. For reproducibility, the paper specifies model versions, temperature settings, the NLI model details, and the exact bootstrap parameters with a fixed seed. Code and data availability is mentioned but appears to be incomplete in the disclosure.

On terminology, the paper maintains consistent notation throughout—"Likert Blindspot," Bradley-Terry model, odds ratios, and all the key acronyms are defined upfront and used uniformly. There's a potential ambiguity between capital P for win probability in the Bradley-Terry framework versus lowercase p for p-values that could use clarification.

Now checking the section transitions and how the narrative flows from abstract through introduction into related work.

The progression feels natural overall, though the split between experiments and analysis sections is a bit unconventional—section 4 covers the statistical framework and model selection, while section 5 dives into the actual analysis findings like the Likert blindspot and cross-judge replication patterns.

Looking at the limitations section now, there are three main concerns the authors address: residual confounding, the distinction between detection and amplification, and the scope of the work.

The word count comes in around 150-180 words, which meets the requirement. These aren't vague "future work" statements either—they're concrete acknowledgments of real methodological constraints. The section aligns perfectly with the custom rule about keeping limitations brief and focused on a few key points. I should also verify there's no duplicate limitations section buried in the appendix, which there isn't.

Now I'm checking for em-dashes throughout the paper. There's one instance in the introduction using the LaTeX triple-dash syntax for a parenthetical explanation, but that's the only one I can find across all the main sections.

For en-dashes, I'm seeing legitimate uses in number ranges like "1--10" and "76--92%", which follow the style guide correctly. There are also compound modifiers like "style--quality" that appear multiple times, which are appropriate uses.

I'm not finding obvious patterns of AI-typical filler like "-ing phrase endings" or overused transition words such as "notably" or "importantly". The paragraphs maintain substantial length throughout, which is good.

Checking for internal information leakage—there are no experiment IDs, server names, or internal process references visible. The mention of "accessed April--May 2026" for API dates is fine since it's methodological transparency rather than a red flag.

Now I'm verifying the EMNLP 2026 submission requirements, specifically the abstract word limit. I'm counting through the sentences to see if it stays within the 200-word constraint. gated content control, per-axis style decomposition, and position-controlled pairwise comparison." = 27 words

Sentence 4: "Across five judges from five independent providers and two primary axes (formality, verbosity), pairwise reaches significance (p < 0.001) where Likert does not (p > 0.28), with Likert effect sizes collapsing toward zero at larger n, replicated across three benchmarks and confirmed by seven statistical methods." = 46 words

Sentence 5: "Generalized estimating equation (GEE) decomposition reveals distinct per-axis confound structures: verbosity bias is style-dominated (Style odds ratio [OR] 3--13, Originality OR <1), while formality reflects joint style--quality contributions." = 30 words

Sentence 6: "One judge (Claude Sonnet 4) exhibits benchmark-dependent sensitivity, illustrating bias as a judge×benchmark interaction; non-tie concordance (76.6%, p < .001) is more consistent with attenuation than construct divergence." = 28 words

Sentence 7: "Likert-only audits may thus fail to surface style-driven preferences that propagate through pairwise-based alignment pipelines." = 15 words

Now I'm checking the word count—191 words total, which stays under the 200-word limit. The limitations section covers the three key points needed, and I'm confirming there's only one limitations section in the main body with none in the appendix. I need to verify the ARR Responsible NLP Checklist placement on the OpenReview submission form.

Looking at the page count, the compiled PDF runs 20 pages including references and appendix, but I need to determine if the main text fits within the 8-page limit. Based on the structure—introduction around 1.5 pages, related work roughly 1 page, methods about 2 pages, experiments and analysis taking up 4 pages, conclusion half a page, and limitations half a page—it appears the main text could be tight against the constraint. I should cross-check the abstract claim about p-values against Table 1 to verify the Likert statistics are accurate. I'm checking the dash usage in compound terms like "style--quality" which is standard academic notation, and verifying the conclusion's claim about 8 primary Blindspot cases by cross-referencing Table 1—confirming that formality and verbosity metrics for GPT-4o, Qwen3, and Llama all show Blindspot patterns as stated.

But now I'm noticing a discrepancy: the statistical framework defines the primary family as six tests (three target judges × two axes), yet the conclusion claims "8/8 primary" Blindspot cases, which would suggest eight tests instead. Gemini is marked as confirmatory replication and excluded from FWER control, so it shouldn't count toward the primary family. I need to reread the conclusion more carefully to understand what the "8/8" actually refers to.

Looking at the binomial probability statement in the experiments section, it's treating 8 primary cells as the unit of analysis. Ah—I see the distinction now. The primary family for FWER correction is indeed 6 (GPT-4o, Qwen3, and Llama, each with formality and verbosity), but the Blindspot count includes all four judges across those two axes, giving 8 cells total. Gemini gets excluded from the multiple comparison correction but still participates in the Blindspot pattern count. And Claude doesn't show the Blindspot pattern at all—it's marked as absent in the table.

Now checking whether Gemini's formality effect actually qualifies as Blindspot. The table shows Gemini Form with a significant effect, so I need to verify if that's truly demonstrating the pattern or if there's something else going on there. ), marked as †_c (confirmatory). And in the GEE analysis, Gemini formality Style OR = 1.64 (n.s.). The text in §5.3 says "Gemini-2.5-Flash shows a weaker, originality-dominated formality pattern (confirmatory: BT 57.4%, p = 0.031; Likert d = −0.08, n.s.; Style OR = 1.64, n.s.; Orig OR = 2.51, p = 0.002)". So Gemini formality IS a Blindspot (BT significant but Likert not), but the style effect is weak and originality-dominated. It's still counted in 8/8. OK ✓.

Now checking the introduction's mention of GPT-4o at 63.0% and Qwen3-32B at 66.5% formal preferences against Table 1, which confirms both values with their significance markers. The abstract's claim about Likert effect sizes collapsing toward zero holds up in the n=355 replication with d = -0.025. Looking at the Discussion section, I notice the paper actually transitions directly from Analysis to Conclusion without a separate Discussion—the Analysis section handles both results and interpretation, which works for this format. The Conclusion itself is brief at six lines, and it covers the two main findings: the Likert Blindspot showing divergent verdicts across 8/8 primary and 6/24 cross-benchmark cells with effect sizes approaching zero at larger sample sizes, plus the per-axis confound structures identified through GEE analysis with verbosity being style-dominated and formality showing conditional patterns. The citation properly attributes the 76-92% figure to other work, so that's acceptable. I notice there's an em-dash in the introduction that needs to be removed since the guidelines require eliminating all explanatory em-dashes. Checking for overused terms like "novel" and "leverage" — neither appears in the text. The transitions flow naturally without repetitive connectors, and paragraph lengths seem reasonable throughout.

The em-dash in the introduction is the only instance I found in the main text. The hyphenated compounds like "style-quality" are standard academic typesetting and don't need changes.

Now I'm checking whether the abstract introduces the CSD concept before establishing the problem context.

The abstract follows a solid structure: it opens with the divergence problem, defines the Likert Blindspot, introduces CSD as the solution, presents the results, and concludes with significance. The claim about the Blindspot in experiments.tex is clearly stated without overclaiming, and the binomial probability test is properly formalized. I should verify that Likert scoring is described consistently throughout the Method section.

Looking at the scale descriptions, the primary experiments use a 1-10 scale while the appendix tests a 1-100 continuous scale for robustness—these are consistent. One thing I'm noticing is the potential confound where Qwen3-32B serves as both rewriter and judge. The paper does acknowledge this transparently with an independence test showing 22% lower Style OR when using GPT-4o as the rewriter instead, and this is flagged in Table 1's footnote. I should check whether the Limitations section adequately addresses this methodological concern.

The paper handles the rewriter-judge confound well in the Limitations, noting that while the Blindspot persists with independent rewriters, the effect-size precision varies depending on which model does the rewriting. Beyond just reporting numbers, the Analysis section offers three non-exclusive interpretations of the divergence between metrics—attenuation, amplification, and construct divergence—which shows genuine higher-level thinking. The implications for bias mitigation are also discussed, distinguishing between issues that can be addressed through style-level interventions versus those requiring deeper disentanglement of quality factors. The Conclusion wraps this up with practical recommendations for alignment pipelines.

I'm also verifying formatting consistency throughout the paper. The model name "Claude Sonnet~4" uses a non-breaking space and appears consistently across the document. The section structure follows standard ACL conventions with six numbered main sections and an unnumbered Limitations section, which is appropriate. I don't see any filler phrases like "it is worth noting" cluttering the text.

Now I'm compiling my audit findings: the introduction has one em-dash that warrants a note, the abstract sits right at the word count boundary around 191 words, and there's a minor issue where the GEE OR range in the abstract slightly understates the lower bound compared to the actual minimum of 2.52 when including all estimates. Table 1 lacks error bars in the main text though they're available in the appendix version, and while there's no dedicated Discussion section, the Analysis section effectively serves that purpose with higher-level interpretation. Let me take another closer look at Table 1's caption to make sure I'm capturing everything accurately.

The caption notes that Bradley-Terry confidence intervals are relegated to the appendix, which is a space-saving choice but means the primary results table doesn't display uncertainty visually—generally better practice would be to include them in the main table, though EMNLP's constraints might justify the decision. The double-rewrite control mentioned in the methods is a methodological component rather than a standalone contribution, which is appropriate since it's integrated into the CSD pipeline. I'm also noticing a potential inconsistency: the Experiments section describes six primary tests based on three target judges and two axes, but Table 1 appears to show four target judges instead.

Actually, looking more carefully at the explanation, it clarifies that Gemini-2.5-Flash is excluded from the family-wise error rate control and serves as confirmatory replication, so the primary family is indeed three judges (GPT-4o, Qwen3, Llama) times two axes, with Gemini and Claude added for other purposes. That resolves the apparent discrepancy. The title accurately captures the paper's focus on measurement-mode divergence in LLM evaluation, so everything checks out.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16c0f664-433c-49e3-8312-88a45152236a",
  "isSidechain": false,
  "requestId": "req_011CbNop9wWAXHRQa3ggTz48",
  "type": "assistant",
  "uuid": "401785cb-465b-4aae-ac5f-42b1811f1820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRGwZ7CmtiCsLfAruPsQAF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34361,
      "cache_read_input_tokens": 50805,
      "output_tokens": 9684,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9684,
          "cache_read_input_tokens": 50805,
          "cache_creation_input_tokens": 34361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34361
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

_source line 39 · 2026-05-25T06:27:21.053Z_

Now let me do targeted searches for AI-style markers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "401785cb-465b-4aae-ac5f-42b1811f1820",
  "isSidechain": false,
  "requestId": "req_011CbNop9wWAXHRQa3ggTz48",
  "type": "assistant",
  "uuid": "1558fd47-c582-4a90-a740-ae59f4c23e62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRGwZ7CmtiCsLfAruPsQAF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34361,
      "cache_read_input_tokens": 50805,
      "output_tokens": 9684,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9684,
          "cache_read_input_tokens": 50805,
          "cache_creation_input_tokens": 34361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34361
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

_source line 40 · 2026-05-25T06:27:22.501Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013uJYCuyHg3M6rB7TVijipo`</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1558fd47-c582-4a90-a740-ae59f4c23e62",
  "isSidechain": false,
  "requestId": "req_011CbNop9wWAXHRQa3ggTz48",
  "type": "assistant",
  "uuid": "c74be5db-0feb-4f9c-a999-206381058dc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRGwZ7CmtiCsLfAruPsQAF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34361,
      "cache_read_input_tokens": 50805,
      "output_tokens": 9684,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9684,
          "cache_read_input_tokens": 50805,
          "cache_creation_input_tokens": 34361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34361
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

_source line 41 · 2026-05-25T06:27:25.687Z_

<details><summary>↩ Tool result · `toolu_012ypXpRJxbbsnCKdXkBFE7e`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex:7:CSD differs in targeting individual style axes, using position-controlled pairwise comparison, and enforcing content preservation via NLI gating.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex:106:After controlling for original preference, the formality effect remains significant (GPT-4o: OR $= 2.58$, $p = 0.002$; Qwen3-32B: OR $= 2.15$, $p < 0.0001$, $n = 355$; Llama-70B: OR $= 4.81$, $p < 0.0001$; Table~\ref{tab:gee}); the significant originality ORs confirm residual confounding.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex:24:BERTScore serves as a supplementary monitor (mean $\Delta$BERTScore $< 0.02$ for gate-passed pairs) but does not participate in gating, as NLI provides stronger semantic equivalence guarantees than token-overlap metrics.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex:29:\caption{Assumed data-generating process (design rationale, not a claim of perfect identification). The rewriting mechanism $R$ targets style $S$ but may inadvertently alter content quality $Q$ (dash-dot, blocked by NLI gate) or introduce rewriting artifacts ($R \to Y$, blocked by double-rewrite control). Position bias $P \to Y$ is controlled by order swapping. The dashed $S \to Q$ path represents residual confounding (Limitations). $Y$: judge score.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex:38:In pairwise mode, the judge receives both texts as candidates A and B and makes a forced choice of which response is better, eliminating anchoring effects inherent in absolute rating.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex:63:A tone axis pilot (assertive $\to$ hedging) did not pass NLI gating, establishing a practical scope boundary for CSD at surface-level axes (Limitations).
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:23:The formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:278:To assess robustness to originality confounding, we restrict to pairs where the judge assigned equal Likert scores to original and counterfactual texts (eliminating detectable quality differences).
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:280:In the anti-originality subset (pairs where the original never wins), effects strengthen (formality $75.0\%$, verbosity $86.1\%$), confirming that style preference is not an artifact of originality confounding.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:472:Score distributions are unimodal and right-skewed for all three judges, with medians in the $72$--$80$ range; the score \emph{difference} distributions (original minus rewrite) are symmetric around zero, confirming no net directional shift under Likert scoring.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:599:We quantify cross-axis contamination by measuring off-target surface proxies before and after rewriting.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:674:Among 30 gate-rejected pairs, A1 judges 30/30 and A2 judges 28/30 as content-preserving, confirming that the gate's dominant error mode is false rejection rather than false acceptance.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:761:\texttt{Rewrite the following text to be more [formal/casual] while preserving the exact same content and meaning. Do not add, remove, or change any factual information. Only adjust the level of formality in the language.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:764:\texttt{Rewrite the following text to be more [verbose/concise] while preserving the exact same content and meaning. Do not add, remove, or change any factual information. Only adjust the level of detail and elaboration.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:767:\texttt{Rewrite the following text to use a more [academic/conversational] register while preserving the exact same content and meaning. Do not add, remove, or change any factual information. Only adjust the register and tone.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:770:\texttt{Rewrite the following text in the same style (keep it [formal/casual/verbose/concise]) while preserving the exact same content and meaning. Paraphrase the text without changing its style.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:822:    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex:12:In the LLM judge setting, this gap has \emph{per-axis} confound signatures: verbosity is style-dominated (Style OR $3$--$13$) while formality is quality-confounded (Table~\ref{tab:gee}), a decomposition not previously applied in LLM judge evaluation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5841970-6815-48a6-84b5-5a32f9b58145",
  "isSidechain": false,
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "9816b8ff-c245-4a10-8247-07569c97ac3a",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex:7:CSD differs in targeting individual style axes, using position-controlled pairwise comparison, and enforcing content preservation via NLI gating.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex:106:After controlling for original preference, the formality effect remains significant (GPT-4o: OR $= 2.58$, $p = 0.002$; Qwen3-32B: OR $= 2.15$, $p < 0.0001$, $n = 355$; Llama-70B: OR $= 4.81$, $p < 0.0001$; Table~\\ref{tab:gee}); the significant originality ORs confirm residual confounding.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex:24:BERTScore serves as a supplementary monitor (mean $\\Delta$BERTScore $< 0.02$ for gate-passed pairs) but does not participate in gating, as NLI provides stronger semantic equivalence guarantees than token-overlap metrics.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex:29:\\caption{Assumed data-generating process (design rationale, not a claim of perfect identification). The rewriting mechanism $R$ targets style $S$ but may inadvertently alter content quality $Q$ (dash-dot, blocked by NLI gate) or introduce rewriting artifacts ($R \\to Y$, blocked by double-rewrite control). Position bias $P \\to Y$ is controlled by order swapping. The dashed $S \\to Q$ path represents residual confounding (Limitations). $Y$: judge score.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex:38:In pairwise mode, the judge receives both texts as candidates A and B and makes a forced choice of which response is better, eliminating anchoring effects inherent in absolute rating.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex:63:A tone axis pilot (assertive $\\to$ hedging) did not pass NLI gating, establishing a practical scope boundary for CSD at surface-level axes (Limitations).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:23:The formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:278:To assess robustness to originality confounding, we restrict to pairs where the judge assigned equal Likert scores to original and counterfactual texts (eliminating detectable quality differences).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:280:In the anti-originality subset (pairs where the original never wins), effects strengthen (formality $75.0\\%$, verbosity $86.1\\%$), confirming that style preference is not an artifact of originality confounding.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:472:Score distributions are unimodal and right-skewed for all three judges, with medians in the $72$--$80$ range; the score \\emph{difference} distributions (original minus rewrite) are symmetric around zero, confirming no net directional shift under Likert scoring.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:599:We quantify cross-axis contamination by measuring off-target surface proxies before and after rewriting.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:674:Among 30 gate-rejected pairs, A1 judges 30/30 and A2 judges 28/30 as content-preserving, confirming that the gate's dominant error mode is false rejection rather than false acceptance.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:761:\\texttt{Rewrite the following text to be more [formal/casual] while preserving the exact same content and meaning. Do not add, remove, or change any factual information. Only adjust the level of formality in the language.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:764:\\texttt{Rewrite the following text to be more [verbose/concise] while preserving the exact same content and meaning. Do not add, remove, or change any factual information. Only adjust the level of detail and elaboration.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:767:\\texttt{Rewrite the following text to use a more [academic/conversational] register while preserving the exact same content and meaning. Do not add, remove, or change any factual information. Only adjust the register and tone.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:770:\\texttt{Rewrite the following text in the same style (keep it [formal/casual/verbose/concise]) while preserving the exact same content and meaning. Paraphrase the text without changing its style.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:822:    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex:12:In the LLM judge setting, this gap has \\emph{per-axis} confound signatures: verbosity is style-dominated (Style OR $3$--$13$) while formality is quality-confounded (Table~\\ref{tab:gee}), a decomposition not previously applied in LLM judge evaluation.",
    "numLines": 18
  },
  "sourceToolAssistantUUID": "d5841970-6815-48a6-84b5-5a32f9b58145",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-25T06:27:22.531Z_

<details><summary>↩ Tool result · `toolu_013uJYCuyHg3M6rB7TVijipo`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex:14:\citet{jeong2025comparative} identify the Comparative Trap---pairwise comparison may amplify style biases---which we address in \S\ref{sec:amplification}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex:48:Claude & Form.\ & .562 & $-$.021 (.721) & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex:49:Claude & Verb.\ & .541 & $-$.039 (.743) & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex:51:\multicolumn{5}{@{}p{\columnwidth}@{}}{\footnotesize $^{***}\!p < 0.001$; $^{*}\!p < 0.05$ (Holm-adj.\ for primary; raw for $_{\text{c}}$). $\dagger$: Blindspot (BT sig., Likert n.s.); ---: neither sig.; $_{\text{e}}$: exploratory; $_{\text{c}}$: confirmatory. Negative $d$: styled variants scored lower.}\\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:20:This asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:27:The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:29:The NLI gate blocks \emph{content} changes but cannot block quality perception shifts that are themselves mediated by style---a fundamental identifiability limit of any text-rewriting approach.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:59:GPT-4o form.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:60:Qwen3 form.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:61:Llama-70B form.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:62:GPT-4o verb.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:63:Qwen3 verb.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:64:Llama-70B verb.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:65:GPT-4o reg.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:66:Qwen3 reg.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:67:Llama-70B reg.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:356:For five of six cells, the required $n$ exceeds $1{,}200$---far beyond typical evaluation budgets---converging with the bootstrap attenuation curve (Appendix~\ref{app:bootstrap_attenuation}) to confirm the Blindspot as a structural measurement limitation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:426:Cohen's $d$ & $d = 0.036$ & --- & No \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:444:The efficiency gap---Likert requiring $3$--$4\times$ the sample size pairwise needs---rather than absolute failure, is the practical concern.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:471:Judges differ markedly in effective granularity usage: GPT-4o clusters scores into ${\sim}5$ distinct bins (modes at 70, 75, 80), Qwen3-32B uses ${\sim}20$ distinct values spanning $45$--$95$, and Llama-70B exploits $50{+}$ unique scores with near-uniform coverage---yet none resolves the Blindspot.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:484:GPT-4o & --- & $-$.038 (.725) & --- & 65.9\% \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:519:Table~\ref{tab:artifact} reports BT $P(\text{original})$---the probability the judge prefers the original over its same-style DR.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:615:Verb.\ $\to$ Form.\ & FK grade & --- & $0.50$ & Confounded$^*$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:666:Cohen's $\kappa = {-}0.015$ is misleading here: with ${>}96\%$ positive prevalence, chance agreement is near-ceiling and $\kappa$ is compressed toward zero regardless of actual agreement---the well-documented prevalence paradox \citep{feinstein1990kappa}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:749:AEval formality produces a Blindspot (BT significant, Likert n.s.), but GEE decomposition reveals this as quality detection rather than style sensitivity---illustrating why aggregate BT alone is insufficient for bias attribution.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:800:\multicolumn{2}{@{}l}{\textbf{Pooled}} & \textbf{201} & \textbf{154} & \textbf{76.6\%} & \textbf{[70.3, 81.9]} & $\mathbf{{<}.001}$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:811:The ${\sim}23\%$ discordance rate leaves room for partial construct divergence---pairwise comparison may access quality dimensions that Likert cannot express---but the dominant pattern is signal attenuation through discretization and ceiling effects.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex:3:\emph{``What is the average height for a male?''} --- in our experiments, given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c74be5db-0feb-4f9c-a999-206381058dc2",
  "isSidechain": false,
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "45311ed6-7bc8-44d6-8df4-02425bab8a87",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex:14:\\citet{jeong2025comparative} identify the Comparative Trap---pairwise comparison may amplify style biases---which we address in \\S\\ref{sec:amplification}.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex:48:Claude & Form.\\ & .562 & $-$.021 (.721) & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex:49:Claude & Verb.\\ & .541 & $-$.039 (.743) & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex:51:\\multicolumn{5}{@{}p{\\columnwidth}@{}}{\\footnotesize $^{***}\\!p < 0.001$; $^{*}\\!p < 0.05$ (Holm-adj.\\ for primary; raw for $_{\\text{c}}$). $\\dagger$: Blindspot (BT sig., Likert n.s.); ---: neither sig.; $_{\\text{e}}$: exploratory; $_{\\text{c}}$: confirmatory. Negative $d$: styled variants scored lower.}\\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:20:This asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:27:The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:29:The NLI gate blocks \\emph{content} changes but cannot block quality perception shifts that are themselves mediated by style---a fundamental identifiability limit of any text-rewriting approach.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:59:GPT-4o form.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:60:Qwen3 form.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:61:Llama-70B form.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:62:GPT-4o verb.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:63:Qwen3 verb.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:64:Llama-70B verb.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:65:GPT-4o reg.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:66:Qwen3 reg.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:67:Llama-70B reg.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:356:For five of six cells, the required $n$ exceeds $1{,}200$---far beyond typical evaluation budgets---converging with the bootstrap attenuation curve (Appendix~\\ref{app:bootstrap_attenuation}) to confirm the Blindspot as a structural measurement limitation.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:426:Cohen's $d$ & $d = 0.036$ & --- & No \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:444:The efficiency gap---Likert requiring $3$--$4\\times$ the sample size pairwise needs---rather than absolute failure, is the practical concern.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:471:Judges differ markedly in effective granularity usage: GPT-4o clusters scores into ${\\sim}5$ distinct bins (modes at 70, 75, 80), Qwen3-32B uses ${\\sim}20$ distinct values spanning $45$--$95$, and Llama-70B exploits $50{+}$ unique scores with near-uniform coverage---yet none resolves the Blindspot.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:484:GPT-4o & --- & $-$.038 (.725) & --- & 65.9\\% \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:519:Table~\\ref{tab:artifact} reports BT $P(\\text{original})$---the probability the judge prefers the original over its same-style DR.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:615:Verb.\\ $\\to$ Form.\\ & FK grade & --- & $0.50$ & Confounded$^*$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:666:Cohen's $\\kappa = {-}0.015$ is misleading here: with ${>}96\\%$ positive prevalence, chance agreement is near-ceiling and $\\kappa$ is compressed toward zero regardless of actual agreement---the well-documented prevalence paradox \\citep{feinstein1990kappa}.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:749:AEval formality produces a Blindspot (BT significant, Likert n.s.), but GEE decomposition reveals this as quality detection rather than style sensitivity---illustrating why aggregate BT alone is insufficient for bias attribution.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:800:\\multicolumn{2}{@{}l}{\\textbf{Pooled}} & \\textbf{201} & \\textbf{154} & \\textbf{76.6\\%} & \\textbf{[70.3, 81.9]} & $\\mathbf{{<}.001}$ & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:811:The ${\\sim}23\\%$ discordance rate leaves room for partial construct divergence---pairwise comparison may access quality dimensions that Likert cannot express---but the dominant pattern is signal attenuation through discretization and ceiling effects.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex:3:\\emph{``What is the average height for a male?''} --- in our experiments, given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \\emph{higher} on a 1--10 Likert scale (8 vs.\\ 5), yet consistently selects the formal variant in pairwise comparison.",
    "numLines": 28
  },
  "sourceToolAssistantUUID": "c74be5db-0feb-4f9c-a999-206381058dc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-25T06:27:24.913Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01KuYPekrNnfLsh8dKbKpuw8`</summary>

```json
{
  "pattern": "(notably|importantly|it is worth noting|furthermore|moreover|additionally|delve|leverage|utilize|facilitate|a myriad|a plethora)",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45311ed6-7bc8-44d6-8df4-02425bab8a87",
  "isSidechain": false,
  "requestId": "req_011CbNop9wWAXHRQa3ggTz48",
  "type": "assistant",
  "uuid": "2afac40f-3207-4208-b08b-6ffc22a3b6e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRGwZ7CmtiCsLfAruPsQAF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34361,
      "cache_read_input_tokens": 50805,
      "output_tokens": 9684,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9684,
          "cache_read_input_tokens": 50805,
          "cache_creation_input_tokens": 34361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34361
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

_source line 44 · 2026-05-25T06:27:24.934Z_

<details><summary>↩ Tool result · `toolu_01KuYPekrNnfLsh8dKbKpuw8`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex:12:To control for rewriting artifact bias (the possibility that the judge prefers original text over any rewrite regardless of style), we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex:52:For cross-benchmark validation, we additionally evaluate on AlpacaEval \citep{dubois2023alpacafarm} and MT-Bench \citep{zheng2023judging}, targeting the strongest effects from the primary analysis to test whether style sensitivity generalizes beyond a single benchmark's distributional characteristics.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:651:Sobel mediation test confirms that sentence length mediates 60\% of the total effect ($z = 2.15$, $p = .031$); the 40\% residual direct effect reflects multi-syllable vocabulary shifts (e.g., ``use'' $\to$ ``utilize'') that are inherent to verbose style rather than formality contamination.
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:777:We additionally compute point-biserial correlations ($r_{\text{pb}}$) between Likert score differences and pairwise outcomes across all pairs with valid pairwise preferences.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2afac40f-3207-4208-b08b-6ffc22a3b6e3",
  "isSidechain": false,
  "promptId": "52d50d60-0c84-4f07-9433-1d8d5a366481",
  "type": "user",
  "uuid": "c3956b49-719c-4e5e-a52c-603e0c2f630f",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex:12:To control for rewriting artifact bias (the possibility that the judge prefers original text over any rewrite regardless of style), we additionally generate a same-style double-rewrite for each text (e.g., formal $\\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \\citep{reber2025rate}.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex:52:For cross-benchmark validation, we additionally evaluate on AlpacaEval \\citep{dubois2023alpacafarm} and MT-Bench \\citep{zheng2023judging}, targeting the strongest effects from the primary analysis to test whether style sensitivity generalizes beyond a single benchmark's distributional characteristics.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:651:Sobel mediation test confirms that sentence length mediates 60\\% of the total effect ($z = 2.15$, $p = .031$); the 40\\% residual direct effect reflects multi-syllable vocabulary shifts (e.g., ``use'' $\\to$ ``utilize'') that are inherent to verbose style rather than formality contamination.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex:777:We additionally compute point-biserial correlations ($r_{\\text{pb}}$) between Likert score differences and pairwise outcomes across all pairs with valid pairwise preferences.",
    "numLines": 4
  },
  "sourceToolAssistantUUID": "2afac40f-3207-4208-b08b-6ffc22a3b6e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-25T06:27:25.668Z_

<details open><summary>🔧 Tool call — Grep · `toolu_012ypXpRJxbbsnCKdXkBFE7e`</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3956b49-719c-4e5e-a52c-603e0c2f630f",
  "isSidechain": false,
  "requestId": "req_011CbNop9wWAXHRQa3ggTz48",
  "type": "assistant",
  "uuid": "d5841970-6815-48a6-84b5-5a32f9b58145",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRGwZ7CmtiCsLfAruPsQAF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34361,
      "cache_read_input_tokens": 50805,
      "output_tokens": 9684,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9684,
          "cache_read_input_tokens": 50805,
          "cache_creation_input_tokens": 34361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34361
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

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：causal_style_decomp_judge Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 3 critical, 2 war…",
  "leafUuid": "9816b8ff-c245-4a10-8247-07569c97ac3a",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit causal style decomposition paper for EMNLP 2026",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c"
}
```

---

### Assistant

_source line 48 · 2026-05-25T06:27:50.183Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed to produce the audit. Let me compile:

Em-dashes (---) in prose (not tables):
1. introduction.tex:3 — `--- in our experiments`
2. related_work.tex:14 — `Trap---pairwise comparison may amplify style biases---which`
3. appendix.tex:20 — `confounded---formally written texts`
4. appendix.tex:27 — `judges---both favor formal text...---supports`
5. appendix.tex:29 — `style---a fundamental identifiability limit`


6. appendix.tex:356 — `$1{,}200$---far beyond typical evaluation budgets---converging`
7. appendix.tex:444 — `gap---Likert requiring $3$--$4\times$ the sample size pairwise needs---rather`
8. appendix.tex:471 — `coverage---yet none resolves the Blindspot`
9. appendix.tex:519 — `$P(\text{original})$---the probability`
10. appendix.tex:666 — `agreement---the well-documented prevalence paradox`
11. appendix.tex:749 — `sensitivity---illustrating why`
12. appendix.tex:811 — `divergence---pairwise comparison...---but the dominant`

So the em-dashes cluster heavily in the appendix with just a couple instances in the main text. The "additionally" uses are mostly inline within sentences, though one in the appendix starts a sentence which is borderline. For the -ing patterns, that related work example is just a list of gerunds describing comparison methods, not an actual AI issue.

Looking more carefully at the trailing -ing phrases, most are genuinely natural language—things like "confirming that" or "establishing a practical scope boundary." The paper overall reads cleanly, with the main stylistic concern being the em-dash usage scattered throughout, especially in the appendix sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9816b8ff-c245-4a10-8247-07569c97ac3a",
  "isSidechain": false,
  "requestId": "req_011CbNp5ZCA4P3fbLmLhv5Ay",
  "type": "assistant",
  "uuid": "187d6589-b6d4-45b6-9def-980ddc54ed4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eg8s3YUpsH5qvfTooq8iuS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14559,
      "cache_read_input_tokens": 85166,
      "output_tokens": 1706,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14559,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1706,
          "cache_read_input_tokens": 85166,
          "cache_creation_input_tokens": 14559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14559
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

_source line 49 · 2026-05-25T06:28:13.640Z_

审计完成。以下是结构化输出。

```
[CONTENT_AUDIT_START]
- [warning] [去AI] introduction.tex:3 Em-dash "--- in our experiments" 用于解释性连接，应改为句号或冒号
- [warning] [去AI] related_work.tex:14 双 em-dash "Trap---pairwise comparison may amplify style biases---which" 应改为括号或拆分句子
- [info] [去AI] appendix.tex:20,27,29,356,444,471,519,666,749,811 Appendix 中有约 10 处解释性 em-dash（---），建议统一替换为逗号/括号/分句
- [info] [叙事一致性] Abstract 写 "Style OR 3--13" 但 n=330 缩放复制后实际最低值为 2.52（Gemini），下界略偏高；建议改为 "2.5--13" 或注明 "at n=88"
- [info] [Claim强度] experiments.tex:153 "reframing the Blindspot as a 3--4× efficiency gap rather than absolute failure" — 这一重要限定仅出现在 Analysis 后段，Abstract/Conclusion 中仅提及 "collapsing toward zero" 未提此 nuance；审稿人可能认为 Conclusion 过度简化
- [info] [章节结构] Table 1 的 95% CI 仅出现在 Appendix（Table H），主表缺少不确定性可视化；在顶会投稿中，主结果表直接展示 CI 更有说服力（但可能受页面空间限制）
- [info] [实验严谨性] 主实验使用单一 rewriter（Qwen3-32B），虽有 GPT-4o rewriter 独立性测试（Appendix D），但仅限 verbosity+formality 两个 axis 的 Qwen3 judge；其他三个 judge 均未做 rewriter 独立性验证
- [info] [符号一致性] "additionally" 在 method.tex:12,52 和 appendix.tex:777 出现 3 次作为句内副词——本身不构成 AI 痕迹，但三处全用 "additionally" 有轻微重复感
- [info] [贡献-范围对齐] Register axis 在 Table 1 标记为 exploratory（†_e），但 Introduction 未提及 "exploratory" 性质，仅说 "with exploratory register evidence"——对齐充分
- [info] [可复现性] 缺少 API 调用总 cost 和 wall-clock time 信息；对于纯 API 实验，审稿人可能关心可复现成本
[CONTENT_AUDIT_END]
```

**审计总结：**

叙事一致性整体优秀——Abstract→Intro→Method→Experiments→Conclusion 讲同一个故事，贡献列表与实验验证严格对应，无叙事漂移。Claim 强度控制得当（广泛使用 hedging 如 "admits non-exclusive explanations"、"bounds but cannot eliminate"）。统计严谨性突出（Holm-Bonferroni、7 种方法交叉验证、power analysis、bootstrap attenuation）。

主要可操作项是正文中 2 处 em-dash（introduction.tex:3、related_work.tex:14）和 appendix 约 10 处，应在提交前统一清除。

[AUDIT_DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "187d6589-b6d4-45b6-9def-980ddc54ed4b",
  "isSidechain": false,
  "requestId": "req_011CbNp5ZCA4P3fbLmLhv5Ay",
  "type": "assistant",
  "uuid": "b10731a1-29a6-4e9e-ba1f-b67d26ebe540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/paper_audit_content_b8101b18",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eg8s3YUpsH5qvfTooq8iuS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14559,
      "cache_read_input_tokens": 85166,
      "output_tokens": 1706,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14559,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1706,
          "cache_read_input_tokens": 85166,
          "cache_creation_input_tokens": 14559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14559
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

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：causal_style_decomp_judge Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 3 critical, 2 war…",
  "leafUuid": "b10731a1-29a6-4e9e-ba1f-b67d26ebe540",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit causal style decomposition paper for EMNLP 2026",
  "sessionId": "a4cc3ec9-74b4-4680-bbce-0f59e6ef824c"
}
```

---
