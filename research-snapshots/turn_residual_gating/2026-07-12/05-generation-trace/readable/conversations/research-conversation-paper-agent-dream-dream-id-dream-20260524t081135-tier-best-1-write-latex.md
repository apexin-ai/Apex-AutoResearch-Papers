# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/861acd08-d758-4f58-ad0c-0078efc67a3c.jsonl`
- **Structured JSON:** [`95c2b6b0a1566e9b915c.json`](../../sessions/95/95c2b6b0a1566e9b915c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-24T08:46:14.079Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-24T08:46:14.079Z",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：完整 'discover→diagnose→remedy' 弧全面成立。9 项 planned 实验中，Llama SS 跨模型验证（plan_026） 和 λ_GAR 敏感性消融（plan_022）是最关键的新增证据——前者将 SS 升级为 model-general mitigation（C5）， 后者彻底消除 'gradient weight insufficient' 反驳（W2）。KL divergence（plan_025）提供 head-level 机制证据，锁定 '为什么 exposure bias 选择性破坏 GAR-ours 而非 GAR-Dongre'。3-seed 统计（plan_027） + 4th seed（plan_029）+ alternative GAR definitions（plan_028）形成方法论防火墙。长对话 eval （plan_030）展示 SS 在 20+ turn 场景下仍有效，增强实用价值叙事。所有 fatal/severe reviewer concerns 归零或降为 medium。Paper 定位 EMNLP main conference 3.5–4.0，Title 用 T2 'From Collapse to Recovery' 突出完整弧。核心差异化从 'gating 失败了' 升级为 '首个 exposure bias 对 auxiliary attention loss 的定量测量 + PCGrad 因果排除 + SS/steering 跨模型修复'。\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-24T08:46:14.082Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-24T08:46:14.082Z",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c"
}
```

---

## Round 1

39 recorded events

### User

_source line 3 · 2026-05-24T08:46:14.102Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：完整 'discover→diagnose→remedy' 弧全面成立。9 项 planned 实验中，Llama SS 跨模型验证（plan_026） 和 λ_GAR 敏感性消融（plan_022）是最关键的新增证据——前者将 SS 升级为 model-general mitigation（C5）， 后者彻底消除 'gradient weight insufficient' 反驳（W2）。KL divergence（plan_025）提供 head-level 机制证据，锁定 '为什么 exposure bias 选择性破坏 GAR-ours 而非 GAR-Dongre'。3-seed 统计（plan_027） + 4th seed（plan_029）+ alternative GAR definitions（plan_028）形成方法论防火墙。长对话 eval （plan_030）展示 SS 在 20+ turn 场景下仍有效，增强实用价值叙事。所有 fatal/severe reviewer concerns 归零或降为 medium。Paper 定位 EMNLP main conference 3.5–4.0，Title 用 T2 'From Collapse to Recovery' 突出完整弧。核心差异化从 'gating 失败了' 升级为 '首个 exposure bias 对 auxiliary attention loss 的定量测量 + PCGrad 因果排除 + SS/steering 跨模型修复'。
- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "be8647e7-c81c-41f4-b082-833d592c705c",
  "type": "user",
  "uuid": "63257c10-1db9-4c34-a360-d6ee8dc707c4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-24T08:46:14.101Z_

```json
{
  "parentUuid": "63257c10-1db9-4c34-a360-d6ee8dc707c4",
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
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
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
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "d2e9e36c-b48a-4327-a8cb-1e2ac8d3d08a",
  "timestamp": "2026-05-24T08:46:14.101Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-24T08:46:14.101Z_

```json
{
  "parentUuid": "d2e9e36c-b48a-4327-a8cb-1e2ac8d3d08a",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "57cf2555-01cb-4da9-a874-2579fba86b76",
  "timestamp": "2026-05-24T08:46:14.101Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-24T08:46:14.101Z_

```json
{
  "parentUuid": "57cf2555-01cb-4da9-a874-2579fba86b76",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "668d909a-4cc1-4a71-8335-85ee8a347368",
  "timestamp": "2026-05-24T08:46:14.101Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
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
  "aiTitle": "Generate simulation paper for dream research",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c"
}
```

---

### Assistant

_source line 8 · 2026-05-24T08:46:17.147Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "668d909a-4cc1-4a71-8335-85ee8a347368",
  "isSidechain": false,
  "requestId": "req_011CbM6rZTPsEe6uf8fz3Np7",
  "type": "assistant",
  "uuid": "3811711c-1870-4150-a4ca-5e0321664f52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZ9swAWjVbP94a4v94sq44",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13915,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13915
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

_source line 9 · 2026-05-24T08:46:18.113Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RkrTM2W1S4Fcykey38PxKi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3811711c-1870-4150-a4ca-5e0321664f52",
  "isSidechain": false,
  "requestId": "req_011CbM6rZTPsEe6uf8fz3Np7",
  "type": "assistant",
  "uuid": "4ba7fc5b-cc3b-4bf6-9bbf-c3937f22ce8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZ9swAWjVbP94a4v94sq44",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13915,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13915
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

_source line 10 · 2026-05-24T08:46:18.395Z_

<details open><summary>🔧 Tool call — Read · `toolu_019NN7pRaQbBfvsReXxdZQss`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ba7fc5b-cc3b-4bf6-9bbf-c3937f22ce8c",
  "isSidechain": false,
  "requestId": "req_011CbM6rZTPsEe6uf8fz3Np7",
  "type": "assistant",
  "uuid": "2b670f2b-7b6c-47de-b059-f9aabde5f620",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZ9swAWjVbP94a4v94sq44",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13915,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13915
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

_source line 11 · 2026-05-24T08:46:18.401Z_

<details><summary>↩ Tool result · `toolu_019NN7pRaQbBfvsReXxdZQss`</summary>

```text
1	# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering
2	
3	> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× gap，Qwen 7.8× / Llama 27× median）。这个 insight 为 auxiliary attention loss 在 teacher-forcing 下的 exposure bias 脆弱性提供首个实证刻画。**SS 初步修复: AR GAR 0.401±0.047（3-seed mean±std），TF/AR gap ~1.3×（range 1.15–1.45×）。**
4	> Novelty 排序: (1) exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画 (8×–27× gap) > (2) PCGrad 因果排除梯度方向冲突 + "观察→假设→排除→指向真因" 完整因果链 (D028) > (3) SS 迁移到 multi-turn transformer attention objectives (AR GAR 0.401±0.047, 3-seed) > (4) principled intervention + systematic ablation 的 negative result
5	> **⚠️ Dream review D024: "Cannot" overclaims, novelty "first measurement" 过高, 缺 gradient surgery baseline (PCGrad). 标题改 "Fails to", novelty 降级 "first empirical characterization"**
6	> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)
7	> 最后更新: 2026-05-24 (3-seed SS 数据完成: AR GAR 0.401±0.047, gap ~1.3× range 1.15–1.45×; β=3/5 跨 seed 极稳定 std<0.01; s42 是 β=0 outlier)
8	> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）
9	> **Framing 升级目标 3.5**: 对标 gromov2024/sun2025/xiao2024 "发现→定位→修复" 模式。SS AR GAR 0.401±0.047 (3-seed, vs base 0.019) 是真正的 positive result，不应埋在 Discussion。
10	
11	---
12	
13	## 1. Title Candidates
14	
15	- **T0 (当前)**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue: A Diagnostic Analysis of Per-Layer Residual Gating
16	- **T1**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue （去掉副标题，更简洁有力）
17	- **T2**: From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives （强调完整弧：发现+定位+修复）
18	- **T3**: The Exposure Bias Barrier: Why Auxiliary Attention Losses Fail at Multi-Turn Inference （barrier metaphor，聚焦机制）
19	
20	推荐 T1 或 T2。T1 保留当前论文最有记忆点的短语 "selectively destroys"，去掉冗长副标题。T2 强调 "发现→定位→修复" 完整弧，与 gromov2024/xiao2024 对标。T0 过长（20 词），审稿人可能记不住。T3 偏负面。
21	
22	---
23	
24	## 2. Story Arc
25	
26	Multi-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Accessibility Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), and this improvement transfers perfectly when evaluated on same-distribution text at inference (GAR-ours = 0.49). However, on model-generated text, GAR-ours collapses to 0.064 (Qwen N=50, 7.8× gap) or 0.018 (Llama N=20, 27× gap), driven by text distribution shift. Our central finding is that attention patterns learned under teacher-forced contexts (gold text) do not generalize to autoregressive generation contexts (model-generated text), the classic exposure bias phenomenon. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Notably, this 8×–27× gap is specific to GAR-ours (last-token attention to goals); GAR-Dongre (all-token attention) shows uniformly low values regardless of text distribution, revealing that exposure bias selectively disrupts summary-position attention patterns. Combined with Dongre et al.'s independent failure of goal re-injection, our results provide the first empirical characterization of how text distribution shift (exposure bias) selectively destroys attention patterns learned through auxiliary losses, and identify the specific mechanisms through which this vulnerability manifests. Crucially, we show that scheduled sampling—originally designed for RNN sequence models—transfers to multi-turn transformer attention objectives, compressing the TF–AR gap from 8× to ~1.3× with no perplexity cost (3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001). Inference-time β-steering independently recovers GAR from 0.064 to 0.727. These mitigation results upgrade the paper from pure negative result to a complete "discover → diagnose → initial remedy" arc, matching the narrative pattern of high-impact diagnostic papers (gromov2024, sun2025, xiao2024).
27	
28	---
29	
30	## 3. Core Claims
31	
32	| # | Claim | 支撑 | 状态 |
33	|---|-------|------|------|
34	| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | ✅ 已验证 |
35	| C2 | Residual gating 训练时在 same-distribution text 上有效优化 GAR-ours (TF GAR=0.50)，但在 model-generated text 上完全失败 (AR GAR=0.064, 7.8× gap on Qwen N=50; 27× median on Llama N=20)。GAR-Dongre 在两种分布上均低，无 gap——说明分布偏移选择性影响 summary-position attention pattern。 | v7 训练 + d048 N=50 eval + Llama eval + Reviewer 独立验证 | ✅ 已验证（N=50 precision） |
36	| C3 | 失败机制的因果分析: (1) Distribution shift 是主因（D028 PCGrad 因果排除梯度方向冲突）; (2) NTP 幅度主导 gate 学习 → NF1 反向 turn conditioning; (3) NF3 gate 干预强度不足 2-7%。PCGrad ablation: 消除方向冲突后 cos_sim 围绕 0 震荡(range -0.151 to +0.091)，但 L_GAR 坍塌轨迹不变且无延迟 → 方向冲突非因果因素。**推理端确认（IID same-protocol）**: v9 GAR-ours=0.0151 vs v7=0.0157 (差<0.1pp), **v9 IID PPL=2.780 vs v7=2.784 (差0.004，无改善)**——PCGrad 消除方向冲突后所有可观测指标均 ≈ v7，方向冲突因 NTP 幅度主导而完全 inconsequential | D014 gate-profile + 梯度冲突量化 + **D028 PCGrad 因果排除** + v9 推理 eval + **M017 PPL 修正** | ✅ **End-to-end 完成**: 训练端 + 推理端均确认梯度方向冲突对 GAR 和 PPL 均无因果影响 |
37	| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。IID: GAR 差异<0.6pp, PPL 均 ~2.78。**Model-gen (D033): v9 PCGrad=0.0151, UG=0.0149, LoRA-only=0.0245 均接近 baseline 0.0122——8×–27× gap 在所有训练变体上普遍存在，排除 gating mechanism / turn-conditioning / gradient conflict 作为因果因素** | D021 四路 eval + D033 model-gen eval | ✅ **双重验证**: IID (D021) + model-gen (D033)。model-gen regime 进一步确认 gating 零增量且 GAR collapse 是训练-推理分布偏移的普遍现象 |
38	| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Phase 1 ✅ (GAR decay 80.2%, D042), Phase 2 ✅ (TG gap 27× median, gating zero-increment TG≈LO, LoRA-only N=20 eval) | ✅ Fully confirmed |
39	
40	---
41	
42	## 4. Negative Findings (NF)
43	
44	| # | Finding | 证据 | 叙事角色 |
45	|---|---------|------|----------|
46	| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |
47	| NF2 | 8×–27× text distribution shift gap (GAR-ours): TF GAR=0.50 vs AR GAR=0.064 (Qwen N=50, 7.8× gap); Llama AR GAR=0.018 (27× median gap, N=20)。Same-distribution 泛化成功（TF eval GAR=0.50），cross-distribution 泛化失败。**D033 跨变体确认**: v9 PCGrad, UG, LoRA-only model-gen GAR 均接近 baseline——gap 独立于训练策略，是 exposure bias 的普遍表现。GAR-Dongre 在两种分布上均低，无 gap——分布偏移选择性影响 summary-position (last token) attention pattern | d048 N=50 eval + Llama eval + D033 cross-variant | 核心 negative finding。精确定位为 TEXT DISTRIBUTION SHIFT（exposure bias）。 |
48	| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |
49	| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |
50	
51	---
52	
53	## 5. Key Selling Points
54	
55	**SP1 (核心卖点): Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画。** 8×–27× training-inference GAR-ours gap（Qwen 7.8×, Llama 27× median）提供了 teacher-forcing distribution shift 如何摧毁 auxiliary attention loss 泛化性的实证证据。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。虽然 exposure bias 概念本身已知 (Bengio et al. 2015)，且 sequence generation 中有量化先例 (Ranzato et al. 2016, Wiseman & Rush 2016)，但此前无人刻画其对 auxiliary attention loss 的具体影响。我们的 8×–27× gap 测量展示了这种脆弱性在 attention steering 场景下的严重程度。**注意：(1) claim scope 严格限于 lightweight residual gating + GAR auxiliary loss 的实测范围，不泛化到所有 attention steering 方法。(2) gap 在 GAR-ours（last token only, summary-position attention）上测得（TF 0.50 vs AR 0.064 Qwen / 0.018 Llama）；GAR-Dongre（all response tokens）在两种分布上均低，无 gap——表明 exposure bias 选择性影响 summary-position attention pattern，这一差异本身有分析价值。**
56	
57	**SP2: NTP-GAR 梯度动力学 + PCGrad 因果排除（gradient conflict is inconsequential）。** 观察到 67-79% 的层 NTP-GAR 梯度方向冲突（cos_sim<0）+ NTP 幅度 3-15x 压制 GAR（mag_ratio 7.5→14.7x）。**PCGrad 消融（D028）因果排除方向冲突**：投影后 cos_sim 围绕 0 震荡（range -0.151 to +0.091），L_GAR 坍塌轨迹不变。**推理端确认（IID same-protocol）**: v9 IID PPL = 2.780 vs v7 = 2.784（差 0.004，无改善）; v9 GAR-ours = 0.0151 vs v7 = 0.0157（差 <0.1pp）——**PCGrad 消除方向冲突后所有可观测指标均无变化**（GAR、PPL、NTP 均 ≈ v7）。方向冲突虽然可测量存在于 v7 中，但对训练和推理结果无任何因果影响——7.5–14.7× NTP 幅度主导使方向冲突完全无关紧要（inconsequential）。**⚠️ M017: 此前 "PPL -46%" 和 "selective dissociation" 论述为跨协议对比伪影（model-gen PPL 1.50 vs IID PPL 2.78），已撤回。** **精确 claim scope**: gradient direction conflict is **neither necessary nor sufficient** for the 8×–27× GAR gap; exposure bias alone is sufficient。NOT necessary: 移除冲突→gap仍在; NOT sufficient: v7有冲突但L_GAR训练时收敛; Exposure bias is sufficient: 训练≠推理分布→GAR泛化失败。**Gate 行为额外 insight**: v9 gate dynamic range 比 v7 更宽 (L15 range 0.33 vs v7 0.21)——PCGrad 给 gate 更大自由度，但 gate 用该自由度更激进地优化 NTP 而非 GAR，说明优化景观固有偏好语言建模目标。
58	
59	**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融严格隔离贡献: TG (learned gate + GAR loss) / UG (uniform gate + GAR loss) / LoRA-only (gate=1.0 fixed + GAR loss, 无 gating 机制) / Base。注意：三个 fine-tuned 变体均使用 GAR loss，消融测试的是 gating 机制的增量贡献，而非 GAR loss 本身的效果。
60	
61	**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。
62	
63	**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。
64	
65	---
66	
67	## 6. Anticipated Reviewer Concerns
68	
69	| # | 严重度 | 预期质疑 | 回应策略 |
70	|---|--------|----------|----------|
71	| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |
72	| W2 | **严重** | "你只是没调对参数" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |
73	| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |
74	| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |
75	| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（8×–27× 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |
76	| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |
77	| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 "we extend Dongre"，而是 "Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations"。核心叙事是 mechanism discovery，非 follow-up work。 |
78	| W6 | **严重** | 引用不足（Dream review: 11篇远不够）| 目标 25-30 篇。必须覆盖: attention sinks (Xiao et al. 2024), Found-in-the-Middle (Ko et al. 2024), gated attention (Qiu et al. 2025), transformer circuits (Elhage et al. 2021), FlexiDepth (Luo et al. 2025), multi-turn eval (MT-Bench-101, MultiChallenge), exposure bias mitigation (Professor Forcing, SEARNN) 等。Paper Agent 写作时负责扩充。|
79	| W7 | **严重** | 单 seed 无方差估计 | 所有实验 seed=42，TG-LoRA 差异 ±0.001 在噪声层。回应: held-out eval 50 conversations 提供 paired bootstrap CI，若 CI 包含 0 则统计支持 "zero benefit"。必要时追加 2 个 seed 的训练。|
80	| W8 | **中等** | 缺 exposure-bias mitigation 实验 | 测试 scheduled sampling / model-generated context 训练能否缩小 8×–27× gap。加入 experiment_plan (P1)。如果实验表明 mitigation 确实缩小 gap，论文从 "negative result" 升级为 "negative result + constructive direction"。|
81	| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 exposure bias 的定量测量（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |
82	| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 "we extend Dongre"，而是 "Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations"。核心叙事是 mechanism discovery，非 follow-up work。 |
83	| R3 | 低 | 8×–27× gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |
84	| R4 | ~~低~~ **已核实** | Code-paper 公式语义相反 | **已确认不一致（plan_017 DONE）**。代码正确实现 ReZero-style: `x_{l+1} = x_l + g_l · f_l(x_l)`（gate 缩放子层输出，g→0=层 no-op）。Dream paper.tex 错误写为 `x_{l+1} = g_l · x_l + f_l(x_l)`（gate 缩放残差流，g→0=破坏 skip connection）。**实验数据不受影响**（所有实验用同一份代码）。**Paper Agent 写作时必须**: (1) Method section 用正确公式 `x + g·f(x)`; (2) 机制叙事修正: g→0 = 子层输出被抑制（层变 no-op），NTP 推 g→1 是为保留层计算能力，不是保留 skip connection; (3) NF3 "gate attenuation 2-7%" 指子层贡献缩放，表述正确但需明确。|
85	
86	---
87	
88	## 7. Dongre et al. 关系定位
89	
90	| 维度 | Dongre et al. | 本文 |
91	|------|---------------|------|
92	| 核心问题 | "发生了什么" + "为什么" | "怎么干预" + "为什么干预失败" |
93	| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |
94	| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 8×–27× 泛化 gap + turn conditioning 反转 |
95	| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |
96	| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |
97	
98	**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。
99	
100	共同推论: 两种独立干预路线均失败 → lightweight residual gating with auxiliary attention loss 在 teacher-forcing 下面临严重泛化障碍（8×–27× gap）→ 需要 inference-time 干预或 exposure bias mitigation（SS 已验证可将 gap 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047））。（注意：scope 限于 lightweight gating，不泛化到所有 attention steering 方法。）
101	
102	---
103	
104	## 8. GAR 定义策略
105	
106	| 用途 | 定义 | Goal tokens | Response tokens | 理由 |
107	|------|------|------------|----------------|------|
108	| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |
109	| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |
110	| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |
111	
112	**D024 精确化（d048 N=50 更新）**: GAR-ours TF=0.50, AR=0.064（Qwen 7.8× gap）; Llama AR=0.018（27× median gap）。GAR-Dongre 在两种分布上均低，无 gap。8×–27× gap 是 text distribution shift 现象，特定于 summary-position attention (GAR-ours)。
113	
114	---
115	
116	## 9. 论文结构草案
117	
118	1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示
119	2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表
120	3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention
121	4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据
122	5. **Method**: ThreadGate 架构（⚠️ 非简单标量 gate：per-layer 2 层 MLP + turn embedding，接收 hidden_state + turn_distance/turn_index，输出 per-token per-layer sigmoid gate 值。公式 g_l = σ(W_2·ReLU(W_1·[proj(x_l); emb(t_d, t_i)] + b_1) + b_2)。Uniform Gate = 同架构但用 constant_vector 替代 turn embedding，仍然 per-layer content-dependent）+ MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置
123	6. **Experiments**: §5.1 Setup → §5.2 Main Results (五路消融 TG/+PCGrad/UG/LoRA-only/Base) → §5.3 Inference-Time Steering (β-steering, GAR 0.727) → **§5.4 Scheduled Sampling (gap 8×→~1.3×, 独立 Results 小节)**
124	7. **Analysis**: §6.1 Gate Turn Conditioning → §6.2 PCGrad Gradient Conflict Exclusion → §6.3 Distribution Shift Analysis → §6.4 Mechanism Specificity → §6.5 Cross-Model Replication
125	8. **Discussion**: exposure bias 对 auxiliary attention loss 的具体影响机制 + Why NTP self-recovers but GAR does not + Downstream effects (instruction retention)。**SS 已移至 §5.4**
126	9. **Conclusion**: 完整弧总结——发现 (8×–27× collapse) + 定位 (PCGrad modus tollens) + 修复 (steering + SS)
127	
128	### 贡献列表（按 novelty 排序）
129	
130	1. **Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画**: 实证展示 teacher-forcing distribution shift 如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× training-inference GAR-ours gap），为 teacher-forcing 下的 attention steering 方法提供具体风险标杆
131	2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）
132	3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline
133	4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性
134	5. **Scheduled sampling 作为初步修复**: 首次证明 time-scheduled sampling（linearly mixing model-generated context，原为 RNN 设计）可迁移到 auxiliary attention objectives in multi-turn transformers，将 TF–AR gap 从 8× 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001），无 PPL 代价。配合 inference-time β-steering（GAR 0.064→0.727），构成完整的 mitigation toolkit。**注意**：Dou & Gales (2022) "Parallel Attention Forcing" 使用 data-dependent attention KL 选择训练模式（单轮 NMT），与我们的 time-scheduled + multi-turn + auxiliary attention 目标有三重区分。必须引用并区分。SS 与 steering 是替代关系而非互补——高 β 时两者趋同（β=5: SS 0.717 ≈ TG 0.727），Discussion 需明确说明
135	
136	---
137	
138	## 10. 竞争力评估
139	
140	### Dream Review 结果 (2026-05-19, dream_20260519T135115)
141	- **Best case**: 3.0 (Weak Reject / Findings-level)。主要扣分: claim 过度泛化 (W1), 引用不足 (W6), 单 seed (W7)。
142	- **Median case**: 3.0 (Weak Reject)。同上 + distribution shift insight incremental (W5)。
143	- **Worst case**: 未完成 review（crash），但 imagined experiments 显示最坏情况下 Llama-3 不复现 dramatic pattern。
144	
145	### 修正后预期（2026-05-23 Framing 升级后）
146	- **当前状态**: SS 升级为独立 Results + 5th contribution + 56 references + Llama 跨模型 + 3-seed 统计中 + bootstrap CI。
147	- **Best case**: 3.5 (Borderline Conference / Accept)。完整 "发现→定位→修复" 弧匹配 gromov/sun/xiao 模式。
148	- **Median case**: 3.0-3.5 (Findings-Conference borderline)。若 SS+steering 联合 eval 接近 TF parity → 推向 3.5。
149	- **冲 Main 条件**: SS+steering 联合接近 parity + Llama SS 跨模型复现 + KL divergence 机制证据 + 3-seed 正式统计。
150	- **核心差异化**: 不是 "gating 失败了"（弱），而是 "exposure bias 在 auxiliary attention loss 上的首个定量测量 + PCGrad 因果排除 + SS/steering 初步修复"（强）。
151	- **关键风险**: W5（exposure bias 已知）需要精确定位增量；SS+steering 联合是否真能接近 parity 待验证。
152	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b670f2b-7b6c-47de-b059-f9aabde5f620",
  "isSidechain": false,
  "promptId": "be8647e7-c81c-41f4-b082-833d592c705c",
  "type": "user",
  "uuid": "0e56e1ae-1544-4dbe-a09a-3eb3c7bf4d31",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper_framing.md",
      "content": "# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering\n\n> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× gap，Qwen 7.8× / Llama 27× median）。这个 insight 为 auxiliary attention loss 在 teacher-forcing 下的 exposure bias 脆弱性提供首个实证刻画。**SS 初步修复: AR GAR 0.401±0.047（3-seed mean±std），TF/AR gap ~1.3×（range 1.15–1.45×）。**\n> Novelty 排序: (1) exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画 (8×–27× gap) > (2) PCGrad 因果排除梯度方向冲突 + \"观察→假设→排除→指向真因\" 完整因果链 (D028) > (3) SS 迁移到 multi-turn transformer attention objectives (AR GAR 0.401±0.047, 3-seed) > (4) principled intervention + systematic ablation 的 negative result\n> **⚠️ Dream review D024: \"Cannot\" overclaims, novelty \"first measurement\" 过高, 缺 gradient surgery baseline (PCGrad). 标题改 \"Fails to\", novelty 降级 \"first empirical characterization\"**\n> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)\n> 最后更新: 2026-05-24 (3-seed SS 数据完成: AR GAR 0.401±0.047, gap ~1.3× range 1.15–1.45×; β=3/5 跨 seed 极稳定 std<0.01; s42 是 β=0 outlier)\n> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）\n> **Framing 升级目标 3.5**: 对标 gromov2024/sun2025/xiao2024 \"发现→定位→修复\" 模式。SS AR GAR 0.401±0.047 (3-seed, vs base 0.019) 是真正的 positive result，不应埋在 Discussion。\n\n---\n\n## 1. Title Candidates\n\n- **T0 (当前)**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue: A Diagnostic Analysis of Per-Layer Residual Gating\n- **T1**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue （去掉副标题，更简洁有力）\n- **T2**: From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives （强调完整弧：发现+定位+修复）\n- **T3**: The Exposure Bias Barrier: Why Auxiliary Attention Losses Fail at Multi-Turn Inference （barrier metaphor，聚焦机制）\n\n推荐 T1 或 T2。T1 保留当前论文最有记忆点的短语 \"selectively destroys\"，去掉冗长副标题。T2 强调 \"发现→定位→修复\" 完整弧，与 gromov2024/xiao2024 对标。T0 过长（20 词），审稿人可能记不住。T3 偏负面。\n\n---\n\n## 2. Story Arc\n\nMulti-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Accessibility Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), and this improvement transfers perfectly when evaluated on same-distribution text at inference (GAR-ours = 0.49). However, on model-generated text, GAR-ours collapses to 0.064 (Qwen N=50, 7.8× gap) or 0.018 (Llama N=20, 27× gap), driven by text distribution shift. Our central finding is that attention patterns learned under teacher-forced contexts (gold text) do not generalize to autoregressive generation contexts (model-generated text), the classic exposure bias phenomenon. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Notably, this 8×–27× gap is specific to GAR-ours (last-token attention to goals); GAR-Dongre (all-token attention) shows uniformly low values regardless of text distribution, revealing that exposure bias selectively disrupts summary-position attention patterns. Combined with Dongre et al.'s independent failure of goal re-injection, our results provide the first empirical characterization of how text distribution shift (exposure bias) selectively destroys attention patterns learned through auxiliary losses, and identify the specific mechanisms through which this vulnerability manifests. Crucially, we show that scheduled sampling—originally designed for RNN sequence models—transfers to multi-turn transformer attention objectives, compressing the TF–AR gap from 8× to ~1.3× with no perplexity cost (3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001). Inference-time β-steering independently recovers GAR from 0.064 to 0.727. These mitigation results upgrade the paper from pure negative result to a complete \"discover → diagnose → initial remedy\" arc, matching the narrative pattern of high-impact diagnostic papers (gromov2024, sun2025, xiao2024).\n\n---\n\n## 3. Core Claims\n\n| # | Claim | 支撑 | 状态 |\n|---|-------|------|------|\n| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | ✅ 已验证 |\n| C2 | Residual gating 训练时在 same-distribution text 上有效优化 GAR-ours (TF GAR=0.50)，但在 model-generated text 上完全失败 (AR GAR=0.064, 7.8× gap on Qwen N=50; 27× median on Llama N=20)。GAR-Dongre 在两种分布上均低，无 gap——说明分布偏移选择性影响 summary-position attention pattern。 | v7 训练 + d048 N=50 eval + Llama eval + Reviewer 独立验证 | ✅ 已验证（N=50 precision） |\n| C3 | 失败机制的因果分析: (1) Distribution shift 是主因（D028 PCGrad 因果排除梯度方向冲突）; (2) NTP 幅度主导 gate 学习 → NF1 反向 turn conditioning; (3) NF3 gate 干预强度不足 2-7%。PCGrad ablation: 消除方向冲突后 cos_sim 围绕 0 震荡(range -0.151 to +0.091)，但 L_GAR 坍塌轨迹不变且无延迟 → 方向冲突非因果因素。**推理端确认（IID same-protocol）**: v9 GAR-ours=0.0151 vs v7=0.0157 (差<0.1pp), **v9 IID PPL=2.780 vs v7=2.784 (差0.004，无改善)**——PCGrad 消除方向冲突后所有可观测指标均 ≈ v7，方向冲突因 NTP 幅度主导而完全 inconsequential | D014 gate-profile + 梯度冲突量化 + **D028 PCGrad 因果排除** + v9 推理 eval + **M017 PPL 修正** | ✅ **End-to-end 完成**: 训练端 + 推理端均确认梯度方向冲突对 GAR 和 PPL 均无因果影响 |\n| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。IID: GAR 差异<0.6pp, PPL 均 ~2.78。**Model-gen (D033): v9 PCGrad=0.0151, UG=0.0149, LoRA-only=0.0245 均接近 baseline 0.0122——8×–27× gap 在所有训练变体上普遍存在，排除 gating mechanism / turn-conditioning / gradient conflict 作为因果因素** | D021 四路 eval + D033 model-gen eval | ✅ **双重验证**: IID (D021) + model-gen (D033)。model-gen regime 进一步确认 gating 零增量且 GAR collapse 是训练-推理分布偏移的普遍现象 |\n| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Phase 1 ✅ (GAR decay 80.2%, D042), Phase 2 ✅ (TG gap 27× median, gating zero-increment TG≈LO, LoRA-only N=20 eval) | ✅ Fully confirmed |\n\n---\n\n## 4. Negative Findings (NF)\n\n| # | Finding | 证据 | 叙事角色 |\n|---|---------|------|----------|\n| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |\n| NF2 | 8×–27× text distribution shift gap (GAR-ours): TF GAR=0.50 vs AR GAR=0.064 (Qwen N=50, 7.8× gap); Llama AR GAR=0.018 (27× median gap, N=20)。Same-distribution 泛化成功（TF eval GAR=0.50），cross-distribution 泛化失败。**D033 跨变体确认**: v9 PCGrad, UG, LoRA-only model-gen GAR 均接近 baseline——gap 独立于训练策略，是 exposure bias 的普遍表现。GAR-Dongre 在两种分布上均低，无 gap——分布偏移选择性影响 summary-position (last token) attention pattern | d048 N=50 eval + Llama eval + D033 cross-variant | 核心 negative finding。精确定位为 TEXT DISTRIBUTION SHIFT（exposure bias）。 |\n| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |\n| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |\n\n---\n\n## 5. Key Selling Points\n\n**SP1 (核心卖点): Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画。** 8×–27× training-inference GAR-ours gap（Qwen 7.8×, Llama 27× median）提供了 teacher-forcing distribution shift 如何摧毁 auxiliary attention loss 泛化性的实证证据。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。虽然 exposure bias 概念本身已知 (Bengio et al. 2015)，且 sequence generation 中有量化先例 (Ranzato et al. 2016, Wiseman & Rush 2016)，但此前无人刻画其对 auxiliary attention loss 的具体影响。我们的 8×–27× gap 测量展示了这种脆弱性在 attention steering 场景下的严重程度。**注意：(1) claim scope 严格限于 lightweight residual gating + GAR auxiliary loss 的实测范围，不泛化到所有 attention steering 方法。(2) gap 在 GAR-ours（last token only, summary-position attention）上测得（TF 0.50 vs AR 0.064 Qwen / 0.018 Llama）；GAR-Dongre（all response tokens）在两种分布上均低，无 gap——表明 exposure bias 选择性影响 summary-position attention pattern，这一差异本身有分析价值。**\n\n**SP2: NTP-GAR 梯度动力学 + PCGrad 因果排除（gradient conflict is inconsequential）。** 观察到 67-79% 的层 NTP-GAR 梯度方向冲突（cos_sim<0）+ NTP 幅度 3-15x 压制 GAR（mag_ratio 7.5→14.7x）。**PCGrad 消融（D028）因果排除方向冲突**：投影后 cos_sim 围绕 0 震荡（range -0.151 to +0.091），L_GAR 坍塌轨迹不变。**推理端确认（IID same-protocol）**: v9 IID PPL = 2.780 vs v7 = 2.784（差 0.004，无改善）; v9 GAR-ours = 0.0151 vs v7 = 0.0157（差 <0.1pp）——**PCGrad 消除方向冲突后所有可观测指标均无变化**（GAR、PPL、NTP 均 ≈ v7）。方向冲突虽然可测量存在于 v7 中，但对训练和推理结果无任何因果影响——7.5–14.7× NTP 幅度主导使方向冲突完全无关紧要（inconsequential）。**⚠️ M017: 此前 \"PPL -46%\" 和 \"selective dissociation\" 论述为跨协议对比伪影（model-gen PPL 1.50 vs IID PPL 2.78），已撤回。** **精确 claim scope**: gradient direction conflict is **neither necessary nor sufficient** for the 8×–27× GAR gap; exposure bias alone is sufficient。NOT necessary: 移除冲突→gap仍在; NOT sufficient: v7有冲突但L_GAR训练时收敛; Exposure bias is sufficient: 训练≠推理分布→GAR泛化失败。**Gate 行为额外 insight**: v9 gate dynamic range 比 v7 更宽 (L15 range 0.33 vs v7 0.21)——PCGrad 给 gate 更大自由度，但 gate 用该自由度更激进地优化 NTP 而非 GAR，说明优化景观固有偏好语言建模目标。\n\n**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融严格隔离贡献: TG (learned gate + GAR loss) / UG (uniform gate + GAR loss) / LoRA-only (gate=1.0 fixed + GAR loss, 无 gating 机制) / Base。注意：三个 fine-tuned 变体均使用 GAR loss，消融测试的是 gating 机制的增量贡献，而非 GAR loss 本身的效果。\n\n**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。\n\n**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。\n\n---\n\n## 6. Anticipated Reviewer Concerns\n\n| # | 严重度 | 预期质疑 | 回应策略 |\n|---|--------|----------|----------|\n| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |\n| W2 | **严重** | \"你只是没调对参数\" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |\n| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |\n| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |\n| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（8×–27× 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| W6 | **严重** | 引用不足（Dream review: 11篇远不够）| 目标 25-30 篇。必须覆盖: attention sinks (Xiao et al. 2024), Found-in-the-Middle (Ko et al. 2024), gated attention (Qiu et al. 2025), transformer circuits (Elhage et al. 2021), FlexiDepth (Luo et al. 2025), multi-turn eval (MT-Bench-101, MultiChallenge), exposure bias mitigation (Professor Forcing, SEARNN) 等。Paper Agent 写作时负责扩充。|\n| W7 | **严重** | 单 seed 无方差估计 | 所有实验 seed=42，TG-LoRA 差异 ±0.001 在噪声层。回应: held-out eval 50 conversations 提供 paired bootstrap CI，若 CI 包含 0 则统计支持 \"zero benefit\"。必要时追加 2 个 seed 的训练。|\n| W8 | **中等** | 缺 exposure-bias mitigation 实验 | 测试 scheduled sampling / model-generated context 训练能否缩小 8×–27× gap。加入 experiment_plan (P1)。如果实验表明 mitigation 确实缩小 gap，论文从 \"negative result\" 升级为 \"negative result + constructive direction\"。|\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 exposure bias 的定量测量（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| R3 | 低 | 8×–27× gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |\n| R4 | ~~低~~ **已核实** | Code-paper 公式语义相反 | **已确认不一致（plan_017 DONE）**。代码正确实现 ReZero-style: `x_{l+1} = x_l + g_l · f_l(x_l)`（gate 缩放子层输出，g→0=层 no-op）。Dream paper.tex 错误写为 `x_{l+1} = g_l · x_l + f_l(x_l)`（gate 缩放残差流，g→0=破坏 skip connection）。**实验数据不受影响**（所有实验用同一份代码）。**Paper Agent 写作时必须**: (1) Method section 用正确公式 `x + g·f(x)`; (2) 机制叙事修正: g→0 = 子层输出被抑制（层变 no-op），NTP 推 g→1 是为保留层计算能力，不是保留 skip connection; (3) NF3 \"gate attenuation 2-7%\" 指子层贡献缩放，表述正确但需明确。|\n\n---\n\n## 7. Dongre et al. 关系定位\n\n| 维度 | Dongre et al. | 本文 |\n|------|---------------|------|\n| 核心问题 | \"发生了什么\" + \"为什么\" | \"怎么干预\" + \"为什么干预失败\" |\n| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |\n| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 8×–27× 泛化 gap + turn conditioning 反转 |\n| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |\n| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |\n\n**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。\n\n共同推论: 两种独立干预路线均失败 → lightweight residual gating with auxiliary attention loss 在 teacher-forcing 下面临严重泛化障碍（8×–27× gap）→ 需要 inference-time 干预或 exposure bias mitigation（SS 已验证可将 gap 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047））。（注意：scope 限于 lightweight gating，不泛化到所有 attention steering 方法。）\n\n---\n\n## 8. GAR 定义策略\n\n| 用途 | 定义 | Goal tokens | Response tokens | 理由 |\n|------|------|------------|----------------|------|\n| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |\n| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |\n| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |\n\n**D024 精确化（d048 N=50 更新）**: GAR-ours TF=0.50, AR=0.064（Qwen 7.8× gap）; Llama AR=0.018（27× median gap）。GAR-Dongre 在两种分布上均低，无 gap。8×–27× gap 是 text distribution shift 现象，特定于 summary-position attention (GAR-ours)。\n\n---\n\n## 9. 论文结构草案\n\n1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示\n2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表\n3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention\n4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据\n5. **Method**: ThreadGate 架构（⚠️ 非简单标量 gate：per-layer 2 层 MLP + turn embedding，接收 hidden_state + turn_distance/turn_index，输出 per-token per-layer sigmoid gate 值。公式 g_l = σ(W_2·ReLU(W_1·[proj(x_l); emb(t_d, t_i)] + b_1) + b_2)。Uniform Gate = 同架构但用 constant_vector 替代 turn embedding，仍然 per-layer content-dependent）+ MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置\n6. **Experiments**: §5.1 Setup → §5.2 Main Results (五路消融 TG/+PCGrad/UG/LoRA-only/Base) → §5.3 Inference-Time Steering (β-steering, GAR 0.727) → **§5.4 Scheduled Sampling (gap 8×→~1.3×, 独立 Results 小节)**\n7. **Analysis**: §6.1 Gate Turn Conditioning → §6.2 PCGrad Gradient Conflict Exclusion → §6.3 Distribution Shift Analysis → §6.4 Mechanism Specificity → §6.5 Cross-Model Replication\n8. **Discussion**: exposure bias 对 auxiliary attention loss 的具体影响机制 + Why NTP self-recovers but GAR does not + Downstream effects (instruction retention)。**SS 已移至 §5.4**\n9. **Conclusion**: 完整弧总结——发现 (8×–27× collapse) + 定位 (PCGrad modus tollens) + 修复 (steering + SS)\n\n### 贡献列表（按 novelty 排序）\n\n1. **Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画**: 实证展示 teacher-forcing distribution shift 如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× training-inference GAR-ours gap），为 teacher-forcing 下的 attention steering 方法提供具体风险标杆\n2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）\n3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline\n4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性\n5. **Scheduled sampling 作为初步修复**: 首次证明 time-scheduled sampling（linearly mixing model-generated context，原为 RNN 设计）可迁移到 auxiliary attention objectives in multi-turn transformers，将 TF–AR gap 从 8× 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001），无 PPL 代价。配合 inference-time β-steering（GAR 0.064→0.727），构成完整的 mitigation toolkit。**注意**：Dou & Gales (2022) \"Parallel Attention Forcing\" 使用 data-dependent attention KL 选择训练模式（单轮 NMT），与我们的 time-scheduled + multi-turn + auxiliary attention 目标有三重区分。必须引用并区分。SS 与 steering 是替代关系而非互补——高 β 时两者趋同（β=5: SS 0.717 ≈ TG 0.727），Discussion 需明确说明\n\n---\n\n## 10. 竞争力评估\n\n### Dream Review 结果 (2026-05-19, dream_20260519T135115)\n- **Best case**: 3.0 (Weak Reject / Findings-level)。主要扣分: claim 过度泛化 (W1), 引用不足 (W6), 单 seed (W7)。\n- **Median case**: 3.0 (Weak Reject)。同上 + distribution shift insight incremental (W5)。\n- **Worst case**: 未完成 review（crash），但 imagined experiments 显示最坏情况下 Llama-3 不复现 dramatic pattern。\n\n### 修正后预期（2026-05-23 Framing 升级后）\n- **当前状态**: SS 升级为独立 Results + 5th contribution + 56 references + Llama 跨模型 + 3-seed 统计中 + bootstrap CI。\n- **Best case**: 3.5 (Borderline Conference / Accept)。完整 \"发现→定位→修复\" 弧匹配 gromov/sun/xiao 模式。\n- **Median case**: 3.0-3.5 (Findings-Conference borderline)。若 SS+steering 联合 eval 接近 TF parity → 推向 3.5。\n- **冲 Main 条件**: SS+steering 联合接近 parity + Llama SS 跨模型复现 + KL divergence 机制证据 + 3-seed 正式统计。\n- **核心差异化**: 不是 \"gating 失败了\"（弱），而是 \"exposure bias 在 auxiliary attention loss 上的首个定量测量 + PCGrad 因果排除 + SS/steering 初步修复\"（强）。\n- **关键风险**: W5（exposure bias 已知）需要精确定位增量；SS+steering 联合是否真能接近 parity 待验证。\n",
      "numLines": 152,
      "startLine": 1,
      "totalLines": 152
    }
  },
  "sourceToolAssistantUUID": "2b670f2b-7b6c-47de-b059-f9aabde5f620",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T08:46:18.519Z_

<details><summary>↩ Tool result · `toolu_01RkrTM2W1S4Fcykey38PxKi`</summary>

```text
1	[
2	  {
3	    "name": "Llama-3.1-8B Gradient Conflict Cross-Model Analysis",
4	    "description": "Verify NTP-GAR gradient competition pattern on Llama-3.1-8B. Test whether gradient direction conflict is model-agnostic or architecture-dependent.",
5	    "results": {
6	      "cos_sim_mean": 0.0045,
7	      "cos_sim_std": 0.07,
8	      "neg_cos_sim_layers_pct": 53.1,
9	      "mag_ratio_median": 25.7,
10	      "cross_model_ntp_dominance": true,
11	      "gradient_direction_pattern": "near-orthogonal, not systematic conflict"
12	    },
13	    "tables": [
14	      {
15	        "caption": "Cross-model NTP-GAR gradient analysis on gate parameters",
16	        "columns": [
17	          "Model",
18	          "cos_sim",
19	          "neg_layers %",
20	          "mag_ratio",
21	          "Direction Pattern"
22	        ],
23	        "rows": [
24	          [
25	            "Qwen-2.5-7B (ep0)",
26	            "-0.089",
27	            "78.6%",
28	            "7.5x",
29	            "Systematic conflict"
30	          ],
31	          [
32	            "Qwen-2.5-7B (ep2)",
33	            "-0.042",
34	            "67.9%",
35	            "14.7x",
36	            "Conflict weakens, amp grows"
37	          ],
38	          [
39	            "Llama-3.1-8B (ep2)",
40	            "+0.005",
41	            "53.1%",
42	            "25.7x",
43	            "Near-orthogonal, strong amp"
44	          ]
45	        ]
46	      }
47	    ],
48	    "figures": [],
49	    "analysis": "进入 §6.2 PCGrad Gradient Conflict Exclusion 和 §6.5 Cross-Model Replication。 与 plan_018（Qwen PCGrad）形成 modus tollens：消除冲突→gap 不变（Qwen v9）， 本无冲突→gap 同样严重（Llama），∴ 方向冲突在任何模型上都不是 gap 的因果因素。 mag_ratio 的跨模型一致性（Qwen 14.7×, Llama 25.7×）支撑 '幅度主导使方向无关紧要' 论述。此数据可合并到 cross-model summary table。\n\nLlama 架构与 Qwen 不同（GQA vs MHA, 32 vs 28 层, RoPE 实现差异），但 NTP-GAR 梯度关系的 核心模式——NTP 幅度压制 GAR——在两模型上一致。Llama mag_ratio=25.7× 甚至高于 Qwen 的 14.7× （epoch 2），反映 32 层架构中 NTP 梯度沿更长残差链积累，GAR 信号在相同层数中被更强稀释。 cos_sim≈0（近正交）而非 Qwen 的 cos_sim<0（冲突），说明 Llama 上 NTP 和 GAR 梯度方向几乎 无系统性交互——53.1% 负层比例接近随机期望 50%。这为 PCGrad 因果排除提供完美跨模型补充： Qwen 有真实方向冲突，PCGrad 消除后 gap 不变；Llama 连方向冲突都不存在，gap 同样严重（15.9×）。 两者共同构成 modus tollens：方向冲突既非必要条件（Llama 无冲突仍有 gap）也非充分条件 （Qwen 有冲突但 PCGrad 消除后无改善），对 exposure bias gap 完全无因果影响。"
50	  },
51	  {
52	    "name": "Expanded TF Eval Set (N=200)",
53	    "description": "Increase TF eval from 50 to 200 conversations for tighter bootstrap CI. AR eval stays at N=50 (sufficient given extreme effect sizes).",
54	    "results": {
55	      "tf_n_conversations": 200,
56	      "ar_n_conversations": 50,
57	      "tg_lo_gar_ci_n200": [
58	        -0.0012,
59	        0.0028
60	      ],
61	      "ug_lo_gar_ci_n200": [
62	        -0.0004,
63	        0.0035
64	      ],
65	      "tg_ug_gar_ci_n200": [
66	        -0.0022,
67	        0.0004
68	      ],
69	      "tg_lo_ppl_ci_n200": [
70	        -0.003,
71	        0.003
72	      ],
73	      "all_cis_include_zero": true,
74	      "ci_width_reduction_vs_n50_pct": 28
75	    },
76	    "tables": [
77	      {
78	        "caption": "Bootstrap 95% CI: zero-benefit test at N=50 vs N=200",
79	        "columns": [
80	          "Comparison",
81	          "N=50 CI",
82	          "N=200 CI",
83	          "Zero in CI?"
84	        ],
85	        "rows": [
86	          [
87	            "TG - LoRA (GAR)",
88	            "[-0.0018, +0.0036]",
89	            "[-0.0012, +0.0028]",
90	            "Yes"
91	          ],
92	          [
93	            "UG - LoRA (GAR)",
94	            "[-0.0006, +0.0045]",
95	            "[-0.0004, +0.0035]",
96	            "Yes"
97	          ],
98	          [
99	            "TG - UG (GAR)",
100	            "[-0.0030, +0.0006]",
101	            "[-0.0022, +0.0004]",
102	            "Yes"
103	          ],
104	          [
105	            "TG - LoRA (PPL)",
106	            "[-0.004, +0.004]",
107	            "[-0.003, +0.003]",
108	            "Yes"
109	          ]
110	        ]
111	      }
112	    ],
113	    "figures": [],
114	    "analysis": "数据进入 §5.2 Main Results 统计注脚或 Appendix A。N=200 CI 收窄但结论不变—— 审稿人无法以 'insufficient eval size' 为由质疑 zero-benefit 结论。此实验与 plan_015（bootstrap CI）和 plan_027（3-seed）共同构成方法论防火墙。\n\nN=200 TF eval 将 bootstrap CI 宽度缩小约 28%（CI 宽度 ∝ 1/√N，√(50/200)=0.5， 从 N=50 的 width 0.0054 收窄到 N=200 的 ~0.0040）。所有 pairwise comparison 的 95% CI 仍包含 0，统计上确认 TG/UG/LoRA-only 三者在 TF regime 下 GAR-ours 无差异。 AR eval 保持 N=50 因为效应量极大（8×–27× gap 下即使 N=10 也足以检测 SS vs TG 差异）。 在 best 档位下，此实验是纯方法论稳健性增量——不改变任何结论，但为 bootstrap CI 提供更窄的置信带，提升论文的统计可信度。W7 的统计维度由此全面覆盖。"
115	  },
116	  {
117	    "name": "λ_GAR Sensitivity Ablation (λ=0.1 and λ=10)",
118	    "description": "Train v7 with λ_GAR=10 and λ_GAR=0.1 (1 epoch each). Test whether GAR loss weight affects the exposure bias gap. Directly addresses W2 (hyperparameter tuning).",
119	    "results": {
120	      "lambda10_tf_gar_ours": 0.52,
121	      "lambda10_ar_gar_ours": 0.018,
122	      "lambda10_gap": 28.9,
123	      "lambda10_ppl": 2.95,
124	      "lambda10_gate_mean": 0.905,
125	      "lambda10_mag_ratio_epoch0": 0.75,
126	      "lambda10_ntp_loss": 0.951,
127	      "lambda01_tf_gar_ours": 0.28,
128	      "lambda01_ar_gar_ours": 0.013,
129	      "lambda01_gap": 21.5,
130	      "lambda01_ppl": 2.79,
131	      "lambda01_gate_mean": 0.975,
132	      "lambda01_mag_ratio_epoch0": 75.0,
133	      "v7_tf_gar_ours": 0.5,
134	      "v7_ar_gar_ours": 0.016,
135	      "v7_gap": 31.3,
136	      "v7_ppl": 2.78,
137	      "ar_gar_invariant_to_lambda": true,
138	      "ar_gar_range_across_lambda": [
139	        0.013,
140	        0.018
141	      ],
142	      "baseline_ar_gar": 0.012
143	    },
144	    "tables": [
145	      {
146	        "caption": "lambda_GAR sensitivity: AR GAR invariant to loss weight",
147	        "columns": [
148	          "lambda_GAR",
149	          "Epochs",
150	          "TF GAR",
151	          "AR GAR",
152	          "Gap",
153	          "PPL",
154	          "mag_ratio (ep0)"
155	        ],
156	        "rows": [
157	          [
158	            "0.1",
159	            "1",
160	            "0.28",
161	            "0.013",
162	            "21.5x",
163	            "2.79",
164	            "75x"
165	          ],
166	          [
167	            "1.0 (v7)",
168	            "3",
169	            "0.50",
170	            "0.016",
171	            "31.3x",
172	            "2.78",
173	            "7.5x"
174	          ],
175	          [
176	            "10.0",
177	            "1",
178	            "0.52",
179	            "0.018",
180	            "28.9x",
181	            "2.95",
182	            "0.75x"
183	          ],
184	          [
185	            "Baseline",
186	            "-",
187	            "-",
188	            "0.012",
189	            "-",
190	            "-",
191	            "-"
192	          ]
193	        ]
194	      }
195	    ],
196	    "figures": [],
197	    "analysis": "进入 Appendix B 或 §6.1 Gate Turn Conditioning Analysis 作为补充消融。核心论点： λ=10 使 GAR gradient 实际主导训练（mag_ratio<1），但 AR GAR 不变——与 PCGrad 结果（plan_018）形成正交互补：PCGrad 消除方向冲突→gap 不变，λ=10 消除幅度差距 →gap 不变。两者共同排除 gradient competition 在方向和幅度两个维度上的因果作用， 仅剩 exposure bias（distribution shift）作为唯一未被排除的根因。W2 彻底消除。\n\nλ_GAR=10 使 GAR 梯度幅度在训练初期实际超过 NTP（epoch 0 mag_ratio 降到 0.75×， 即 GAR gradient 1.33× > NTP），gate 获得充足梯度学习 GAR-optimal 配置（gate_mean 降到 0.905，比 v7 的 0.934 有更大调制幅度）。TF GAR 确实提升到 0.52（vs v7 0.50）， 证明更高 λ 推动了更强的 gold-distribution GAR 优化。但 AR GAR 仍停在 0.018—— 仅比 baseline 0.012 高 0.006，在 baseline 噪声范围内。Gap 28.9× 与 v7 的 31.3× 基本相当（差异来自 TF GAR 分子变化，非 AR GAR 分母改善）。PPL 轻微恶化（2.95 vs 2.78）反映 GAR 梯度竞争了 NTP 的优化预算。λ=0.1 时 GAR 训练不充分（TF 0.28）， gate 近乎 identity（0.975），但 AR GAR（0.013）同样停在 baseline 水平。三个 λ 值跨 100× 范围，AR GAR 始终在 [0.013, 0.018] 窄带内——此窄带恰好覆盖 base model 的自然 GAR（0.012），说明 exposure bias 完全抵消了训练获得的 attention steering 能力。这是最直接的 W2 消除证据：即使让 GAR gradient 幅度主导训练（λ=10, mag_ratio<1），推理时的 distribution shift 仍然摧毁所有训练收益。"
198	  },
199	  {
200	    "name": "TF vs AR Per-Head Attention KL Divergence",
201	    "description": "Compute KL(P_TF||P_AR) per attention head on 50 conversations. Quantify which heads are most disrupted by distribution shift and correlate with GAR contribution.",
202	    "results": {
203	      "mean_kl_all_heads": 0.087,
204	      "std_kl_all_heads": 0.052,
205	      "mean_kl_early_L0_L5": 0.034,
206	      "mean_kl_mid_early_L6_L13": 0.058,
207	      "mean_kl_mid_late_L14_L19": 0.092,
208	      "mean_kl_late_L20_L27": 0.18,
209	      "max_kl_single_head": 0.42,
210	      "max_kl_head_id": "L25H3",
211	      "pct_high_kl_heads_in_gar_relevant_top_quartile": 72,
212	      "pearson_r_kl_vs_gar_contribution": 0.38,
213	      "pearson_p_kl_vs_gar_contribution": 0.002,
214	      "ss_model_mean_kl": 0.048,
215	      "ss_kl_reduction_vs_tg_pct": 45,
216	      "n_conversations": 50,
217	      "n_heads_total": 196
218	    },
219	    "tables": [
220	      {
221	        "caption": "Per-layer-group attention KL divergence (TG v7 model)",
222	        "columns": [
223	          "Layer Group",
224	          "Mean KL (nats)",
225	          "Std",
226	          "GAR-relevant heads %",
227	          "Top KL quartile %"
228	        ],
229	        "rows": [
230	          [
231	            "L0-L5 (early)",
232	            "0.034",
233	            "0.012",
234	            "15%",
235	            "8%"
236	          ],
237	          [
238	            "L6-L13 (mid-early)",
239	            "0.058",
240	            "0.021",
241	            "22%",
242	            "18%"
243	          ],
244	          [
245	            "L14-L19 (mid-late)",
246	            "0.092",
247	            "0.031",
248	            "28%",
249	            "25%"
250	          ],
251	          [
252	            "L20-L27 (late)",
253	            "0.180",
254	            "0.065",
255	            "35%",
256	            "49%"
257	          ]
258	        ]
259	      },
260	      {
261	        "caption": "KL divergence: TG vs SS model",
262	        "columns": [
263	          "Model",
264	          "Mean KL",
265	          "Late-layer KL",
266	          "GAR-KL correlation r"
267	        ],
268	        "rows": [
269	          [
270	            "TG v7",
271	            "0.087",
272	            "0.180",
273	            "0.38"
274	          ],
275	          [
276	            "SS v8b",
277	            "0.048",
278	            "0.098",
279	            "0.22"
280	          ],
281	          [
282	            "Reduction",
283	            "-45%",
284	            "-46%",
285	            "-"
286	          ]
287	        ]
288	      }
289	    ],
290	    "figures": [],
291	    "analysis": "进入 §6.3 Distribution Shift Analysis 作为核心机制证据。论点链：(1) distribution shift 导致 attention 分布改变 (KL>0)；(2) KL 在负责 goal-routing 的 heads 上最大 (r=0.38)；(3) 这些 heads 是 GAR-ours 依赖的 (summary-position → goal)；(4) GAR-Dongre 不依赖这些 heads 所以无 gap。将 8×–27× gap 从 aggregate observation 升级为 head-level mechanistic explanation。SS 的 45% KL 降低与 plan_028（SS 改善 所有 GAR 定义）形成一致叙事——SS 的有效性来自真正缩小了 TF-AR attention distribution 的差异，不是 metric hacking。此 figure 适合作为论文 Fig.3 或 Fig.4。\n\nKL(P_TF||P_AR) 量化每个 attention head 在 teacher-forced vs autoregressive context 下的注意力分布差异。Late layers（L20-L27）平均 KL 0.180，是 early layers（L0-L5, 0.034）的 5.3×——深层负责高层语义整合和跨 turn goal-relevant routing，对 input distribution 的变化最敏感。早期层主要处理局部 token 关系（syntax, local coherence）， 对 gold vs model-generated text 的差异不敏感。最关键发现是 head-GAR 相关性：对 goal-token attention 贡献最大的 heads 中 72% 落入高 KL quartile（r=0.38, p=0.002）。 这提供了 exposure bias 选择性破坏 GAR-ours 的 head-level 因果路径：last-token → goal 的 summary attention routing 由少数 specialized heads 执行（集中在 L20-L27）， 这些 heads 恰好是 distribution shift 影响最大的。GAR-Dongre（all-token attention） 不依赖这些 specialized routing heads，而是利用较低层的 content-overlap attention， 所以 TF-AR 无 gap。SS 模型的 mean KL 下降 45%（0.087→0.048），证明 SS 训练确实 通过缩小 TF-AR attention 分布差异来改善 GAR，而非通过其他间接机制。L25H3 的 max KL=0.42 表明个别 head 的 distribution shift 极度严重。"
292	  },
293	  {
294	    "name": "Llama-3.1-8B Scheduled Sampling Training + Eval",
295	    "description": "Replicate SS on Llama-3.1-8B. If gap also compresses, SS upgrades from Qwen-specific finding to model-general mitigation. MUST-HAVE for best tier.",
296	    "results": {
297	      "training_epochs": 3,
298	      "training_wall_clock_hours": 8.5,
299	      "final_loss": 0.924,
300	      "final_ntp_loss": 0.923,
301	      "final_gar_loss": 0.001,
302	      "final_gate_mean": 0.935,
303	      "final_gate_std": 0.062,
304	      "ss_max_ratio": 0.3,
305	      "ss_steps_observed_pct": 29,
306	      "tf_gar_ours": 0.47,
307	      "tf_gar_dongre": 0.35,
308	      "tf_ppl": 2.55,
309	      "ar_gar_beta0": 0.35,
310	      "ar_gar_beta0_ci_95": [
311	        0.32,
312	        0.38
313	      ],
314	      "ar_gar_beta3": 0.56,
315	      "ar_gar_beta5": 0.7,
316	      "ar_ppl_beta0": 1.36,
317	      "ar_ppl_beta3": 1.52,
318	      "ar_ppl_beta5": 1.71,
319	      "gap_ratio": 1.34,
320	      "vs_llama_tg_gap": 15.9,
321	      "gap_compression_factor": 11.9,
322	      "vs_qwen_ss_gap": 1.26,
323	      "cross_model_consistency": true
324	    },
325	    "tables": [
326	      {
327	        "caption": "Llama-3.1-8B inference comparison: SS vs baselines",
328	        "columns": [
329	          "Method",
330	          "TF GAR",
331	          "AR GAR (beta=0)",
332	          "Gap",
333	          "PPL",
334	          "Gap Compression"
335	        ],
336	        "rows": [
337	          [
338	            "Base",
339	            "0.017",
340	            "0.009",
341	            "1.9x",
342	            "1.24",
343	            "-"
344	          ],
345	          [
346	            "TG v7",
347	            "0.484",
348	            "0.030",
349	            "15.9x",
350	            "1.32",
351	            "1.0x (ref)"
352	          ],
353	          [
354	            "LoRA-only",
355	            "0.481",
356	            "0.028",
357	            "17.2x",
358	            "1.32",
359	            "0.93x"
360	          ],
361	          [
362	            "SS (ours)",
363	            "0.47",
364	            "0.35",
365	            "1.34x",
366	            "1.36",
367	            "11.9x"
368	          ]
369	        ]
370	      },
371	      {
372	        "caption": "Cross-model SS gap compression (main contribution table)",
373	        "columns": [
374	          "Model",
375	          "Arch",
376	          "TG Gap",
377	          "SS Gap",
378	          "SS AR GAR",
379	          "Compression",
380	          "PPL delta"
381	        ],
382	        "rows": [
383	          [
384	            "Qwen-2.5-7B",
385	            "MHA 28L",
386	            "32.1x",
387	            "1.26x",
388	            "0.401+-0.047 (3-seed)",
389	            "25.5x",
390	            "+0.01"
391	          ],
392	          [
393	            "Llama-3.1-8B",
394	            "GQA 32L",
395	            "15.9x",
396	            "1.34x",
397	            "0.35",
398	            "11.9x",
399	            "+0.04"
400	          ]
401	        ]
402	      },
403	      {
404	        "caption": "Llama SS: beta-steering response",
405	        "columns": [
406	          "beta",
407	          "AR GAR (Llama SS)",
408	          "AR GAR (Qwen SS 3-seed)",
409	          "PPL (Llama SS)"
410	        ],
411	        "rows": [
412	          [
413	            "0",
414	            "0.35",
415	            "0.401+-0.047",
416	            "1.36"
417	          ],
418	          [
419	            "3",
420	            "0.56",
421	            "0.596+-0.008",
422	            "1.52"
423	          ],
424	          [
425	            "5",
426	            "0.70",
427	            "0.717+-0.001",
428	            "1.71"
429	          ]
430	        ]
431	      }
432	    ],
433	    "figures": [],
434	    "analysis": "进入 §5.4 Scheduled Sampling Results 和 §6.5 Cross-Model Replication。这是 best 档位的核心实验——将 C5 从 'cross-model failure replication' 升级为 'cross-model mitigation validation'，也是 Title T2 'From Collapse to Recovery' 的跨模型支撑。 Cross-model SS summary table 是论文的 flagship contribution table，直接支撑 5th contribution claim。两模型 gap compression 的一致性（均 >10×）确认 SS 解决 的是 fundamental distributional issue。Discussion 需注明 Llama compression 稍低 可能因 ss_max_ratio=0.3（vs Qwen 0.5），未来工作可测试 ratio 提升的效果。 W1（single model）至此彻底消除。\n\nLlama SS 的 gap 压缩（15.9× → 1.34×）与 Qwen 上的模式一致（32× → 1.26×）， 尽管两个模型架构差异显著（GQA vs MHA, 32 vs 28 层, 不同 tokenizer/vocab size） 且 ss_max_ratio 不同（Llama 0.3 vs Qwen 0.5）。AR GAR β=0=0.35 落在 best 档位 要求的 [0.3, 0.5] 范围内。Gap 1.34× 落在 [1.0, 2.0] 范围内。SS 有效性的跨模型 一致性源于其解决的是 fundamental distributional problem——训练时 context 是 gold text，推理时是 model-generated text，SS 通过在训练中混入 model-generated context 缩小这一分布差距。这个机制不依赖特定的 attention 架构（MHA 或 GQA），因为 exposure bias 是所有 teacher-forced 训练的共性问题。Llama gap 略高于 Qwen（1.34× vs 1.26×）， 可能因 ss_max_ratio 0.3 暴露的 model-generated context 比例更低——若提升到 0.5 预计可进一步压缩。PPL 1.36 与 Llama TG（1.32）可比（Δ=0.04），Llama base（1.24） 差距也很小，确认 SS 训练不损害语言建模质量。β steering 同样有效且跨模型一致： β=3 时 Llama 0.56（Qwen 0.596），β=5 时 Llama 0.70（Qwen 0.717）。"
435	  },
436	  {
437	    "name": "SS 3-Seed Statistical Validation (Qwen-2.5-7B)",
438	    "description": "3 seeds (42, 123, 456) for SS training. Provide mean±std and bootstrap CI for all key metrics. Addresses W7 (single seed).",
439	    "results": {
440	      "tf_gar_mean": 0.498,
441	      "tf_gar_std": 0.004,
442	      "tf_gar_s42": 0.503,
443	      "tf_gar_s123": 0.495,
444	      "tf_gar_s456": 0.496,
445	      "ar_gar_beta0_mean": 0.401,
446	      "ar_gar_beta0_std": 0.047,
447	      "ar_gar_beta0_s42": 0.347,
448	      "ar_gar_beta0_s123": 0.423,
449	      "ar_gar_beta0_s456": 0.433,
450	      "ar_gar_beta3_mean": 0.596,
451	      "ar_gar_beta3_std": 0.008,
452	      "ar_gar_beta5_mean": 0.717,
453	      "ar_gar_beta5_std": 0.001,
454	      "ppl_beta0_mean": 1.441,
455	      "ppl_beta0_std": 0.001,
456	      "gap_mean": 1.26,
457	      "gap_std": 0.17,
458	      "gap_range_min": 1.15,
459	      "gap_range_max": 1.45,
460	      "cohens_d_ss_vs_baseline": 8.1
461	    },
462	    "tables": [
463	      {
464	        "caption": "3-seed SS results on Qwen-2.5-7B",
465	        "columns": [
466	          "Seed",
467	          "TF GAR",
468	          "AR GAR beta=0",
469	          "AR GAR beta=3",
470	          "AR GAR beta=5",
471	          "PPL beta=0",
472	          "Gap"
473	        ],
474	        "rows": [
475	          [
476	            "s42",
477	            "0.503",
478	            "0.347",
479	            "0.593",
480	            "0.717",
481	            "1.442",
482	            "1.45x"
483	          ],
484	          [
485	            "s123",
486	            "0.495",
487	            "0.423",
488	            "0.590",
489	            "0.717",
490	            "1.441",
491	            "1.17x"
492	          ],
493	          [
494	            "s456",
495	            "0.496",
496	            "0.433",
497	            "0.605",
498	            "0.716",
499	            "1.439",
500	            "1.15x"
501	          ],
502	          [
503	            "Mean+-std",
504	            "0.498+-0.004",
505	            "0.401+-0.047",
506	            "0.596+-0.008",
507	            "0.717+-0.001",
508	            "1.441+-0.001",
509	            "1.26+-0.17"
510	          ]
511	        ]
512	      }
513	    ],
514	    "figures": [],
515	    "analysis": "进入 §5.4 Scheduled Sampling Results 主表。3-seed 统计直接回应 W7（single seed）， 将 SS 从 'one-shot finding' 升级为 'statistically validated result'。β-dependent variance pattern 提供额外 insight 写入 Discussion §7.2：推理时 steering 是一种 implicit variance reduction mechanism，对训练随机性的敏感性随 β 单调下降。3-seed 足够因为 Cohen's d=8.1（vs baseline 0.019）是极强效应——即使 s42 这个最弱的 seed 的 AR GAR（0.347）也是 baseline 的 18.3×。\n\n3-seed 均值 AR GAR β=0=0.401±0.047 落在 best 档位 [0.38, 0.45] 范围内。Gap 1.26±0.17 落在 [1.1, 1.5] 范围内。关键发现：(1) TF GAR 跨 seed 极稳定（std=0.004）， 证明 SS 在 gold distribution 上的训练高度可复现——三个 seed 的 TF GAR 仅在 0.495–0.503 范围内波动（相对变异 0.8%）。(2) AR GAR β=0 变异较大（std=0.047, 相对变异 11.7%），s42 是低端 outlier（0.347 vs s123/s456 的 0.423/0.433）。这种 IID 稳定 + OOD 变异大的模式本身就是 exposure bias 的统计 signature：模型在 IID 条件下行为高度一致，但在 OOD 条件下对训练随机性更敏感——distribution shift 放大了 random seed 对 learned attention pattern 的影响。(3) β=3/5 的跨 seed 方差消失 （std<0.01），因为推理时 steering 主导了 attention pattern，覆盖了训练 seed 的 随机效应——β 越大，TF/AR 行为越趋同。(4) PPL 1.441±0.001 跨 seed 几乎无差异， 确认 SS 训练不损害语言建模质量。Cohen's d=8.1（SS vs baseline AR GAR）是极强效应。"
516	  },
517	  {
518	    "name": "Alternative GAR Definition Robustness (4 definitions x 3 models)",
519	    "description": "Test 4 token-selection GAR variants (last/all/first/goal-only) on Base/TG/SS in AR regime. Verify SS improvement is broad, not position-specific overfitting.",
520	    "results": {
521	      "base_last_token": 0.019,
522	      "base_all_token": 0.015,
523	      "base_first_token": 0.018,
524	      "base_goal_only": 0.022,
525	      "tg_last_token": 0.325,
526	      "tg_all_token": 0.025,
527	      "tg_first_token": 0.039,
528	      "tg_goal_only": 0.02,
529	      "ss_last_token": 0.401,
530	      "ss_all_token": 0.385,
531	      "ss_first_token": 0.362,
532	      "ss_goal_only": 0.378,
533	      "n_definitions_ss_improves": 4,
534	      "n_definitions_tg_improves": 1,
535	      "ss_min_improvement_over_base": 16.4,
536	      "tg_only_last_token_ratio_vs_others": 8.1
537	    },
538	    "tables": [
539	      {
540	        "caption": "AR GAR across 4 token-selection definitions (beta=0)",
541	        "columns": [
542	          "GAR Definition",
543	          "Response Tokens",
544	          "Base",
545	          "TG",
546	          "SS",
547	          "SS/Base"
548	        ],
549	        "rows": [
550	          [
551	            "Last-token (GAR-ours)",
552	            "Last token per turn",
553	            "0.019",
554	            "0.325",
555	            "0.401",
556	            "21.1x"
557	          ],
558	          [
559	            "All-token (GAR-Dongre)",
560	            "All response tokens",
561	            "0.015",
562	            "0.025",
563	            "0.385",
564	            "25.7x"
565	          ],
566	          [
567	            "First-token",
568	            "First token per turn",
569	            "0.018",
570	            "0.039",
571	            "0.362",
572	            "20.1x"
573	          ],
574	          [
575	            "Goal-only",
576	            "Goal-adjacent tokens",
577	            "0.022",
578	            "0.020",
579	            "0.378",
580	            "17.2x"
581	          ]
582	        ]
583	      }
584	    ],
585	    "figures": [],
586	    "analysis": "进入 §6.4 Mechanism Specificity 或 Appendix D。双重叙事价值：(1) 解释为什么 TG 的 exposure bias gap 如此严重——TG 学到 position-fragile shortcut；(2) 解释为什么 SS 的 gap 更小——SS 学到 distribution-robust semantic attention。也回应 W3 'GAR-ours 是否过于 narrow 的指标'：SS 在所有 4 种定义上的改善表明改善是 genuine attention steering 而非对特定 metric 的 overfitting。与 plan_025（KL divergence） 互补：KL 从 head 维度解释 'why GAR-ours collapses'，alternative GAR defs 从 token-position 维度解释 'why SS works broadly'。\n\nTG 仅改善 last-token GAR（0.325），all/first/goal-only 接近 baseline（0.020–0.039）， 揭示 TG 在 teacher-forcing 下学到的是 position-specific attention shortcut： 专门将 last token 的 attention 导向 goal tokens。这种 narrow routing pattern 高度依赖 gold context 的 token 位置分布——model-generated text 的 token 组织方式 不同，learned shortcut 即失效。SS 改善所有 4 种定义（均 >0.36），说明 SS 学到的 是更 broad 的 goal-attention encoding：不仅 summary position（last token），而是 response 的多个位置都建立了 goal attention。机制解释：SS 训练中 model-generated context 的分布多样性迫使模型不能依赖 position-specific cue，因为 model-generated text 的 token 位置特征与 gold text 不同（不同的 word choice → 不同的 sequence length → 不同的 positional pattern）。模型被迫学习基于 semantic goal-relevance 而非 positional shortcut 的 attention pattern，这种 pattern 天然 distribution-robust。 4/4 定义改善满足 best 档位 [3, 4] 要求。Base 一致 <0.022 排除随机性。"
587	  },
588	  {
589	    "name": "SS 4th Seed (s789) Supplementary Validation",
590	    "description": "Additional seed to tighten mean±std. Lower ROI than Llama SS but adds reviewer confidence. Run only if GPU budget remains after plan_026.",
591	    "results": {
592	      "s789_tf_gar": 0.497,
593	      "s789_ar_gar_beta0": 0.41,
594	      "s789_ar_gar_beta3": 0.598,
595	      "s789_ar_gar_beta5": 0.716,
596	      "s789_ppl_beta0": 1.441,
597	      "s789_gap": 1.21,
598	      "four_seed_mean_beta0": 0.404,
599	      "four_seed_std_beta0": 0.037,
600	      "four_seed_ci_95": [
601	        0.345,
602	        0.463
603	      ],
604	      "ci_width_reduction_vs_3seed_pct": 21,
605	      "cohens_d_4seed": 9.2
606	    },
607	    "tables": [
608	      {
609	        "caption": "4-seed SS statistics (Qwen-2.5-7B, Appendix)",
610	        "columns": [
611	          "Seed",
612	          "AR GAR beta=0",
613	          "AR GAR beta=3",
614	          "AR GAR beta=5",
615	          "PPL",
616	          "Gap"
617	        ],
618	        "rows": [
619	          [
620	            "s42",
621	            "0.347",
622	            "0.593",
623	            "0.717",
624	            "1.442",
625	            "1.45x"
626	          ],
627	          [
628	            "s123",
629	            "0.423",
630	            "0.590",
631	            "0.717",
632	            "1.441",
633	            "1.17x"
634	          ],
635	          [
636	            "s456",
637	            "0.433",
638	            "0.605",
639	            "0.716",
640	            "1.439",
641	            "1.15x"
642	          ],
643	          [
644	            "s789",
645	            "0.41",
646	            "0.598",
647	            "0.716",
648	            "1.441",
649	            "1.21x"
650	          ],
651	          [
652	            "Mean+-std",
653	            "0.404+-0.037",
654	            "0.597+-0.006",
655	            "0.717+-0.001",
656	            "1.441+-0.001",
657	            "1.25+-0.14"
658	          ]
659	        ]
660	      }
661	    ],
662	    "figures": [],
663	    "analysis": "进入 Appendix 表格。4-seed 不改变 §5.4 主表（仍用 3-seed），但可在 rebuttal 中作为补充证据使用。主要价值：展示 due diligence + 确认 s42 是 low-end outlier。\n\ns789 的 AR GAR β=0=0.41 与 3-seed 均值 0.401 高度一致，不是 outlier。加入后 4-seed std 从 0.047 收窄到 0.037（CI 宽度缩小 21%），95% CI [0.345, 0.463] 下限 0.345 仍远高于 baseline 0.019（18.2×）。Cohen's d 从 8.1 提升到 9.2。 但此实验的边际信息量有限——3-seed 的效应量已经足够极端，第 4 seed 不改变统计 结论或审稿人评分。s789 gap=1.21× 略低于 3-seed 均值 1.26×，进一步确认 s42 的 1.45× 是高端离群值而非 typical behavior。β=3/5 继续显示极低跨 seed 方差 （std<0.01），steering 稳定性不随 seed 数量变化。PPL 1.441 与所有前 3 seed 完全一致（std 仍为 0.001），语言建模质量不受训练随机性影响。ROI 明确低于 plan_026（Llama SS）——跨模型验证的 novelty 贡献远大于 same-model 额外 seed 的统计边际值。建议仅在 Llama SS 完成后有剩余 GPU 预算时执行。"
664	  },
665	  {
666	    "name": "Long Conversation Eval (15-20 turns)",
667	    "description": "Test exposure bias gap scaling with conversation length (10/15/20 turns). Verify SS maintains advantage at longer conversations where mitigation matters most.",
668	    "results": {
669	      "turns_tested": [
670	        10,
671	        15,
672	        20
673	      ],
674	      "base_gar_t10": 0.012,
675	      "base_gar_t15": 0.008,
676	      "base_gar_t20": 0.006,
677	      "base_gar_decay_10to20_pct": 50,
678	      "tg_ar_gar_t10": 0.016,
679	      "tg_ar_gar_t15": 0.012,
680	      "tg_ar_gar_t20": 0.009,
681	      "tg_ar_gar_decay_10to20_pct": 44,
682	      "ss_ar_gar_t10": 0.347,
683	      "ss_ar_gar_t15": 0.305,
684	      "ss_ar_gar_t20": 0.27,
685	      "ss_ar_gar_decay_10to20_pct": 22,
686	      "tg_gap_t10": 31.5,
687	      "tg_gap_t15": 41.7,
688	      "tg_gap_t20": 55.6,
689	      "tg_gap_growth_10to20_pct": 77,
690	      "ss_gap_t10": 1.45,
691	      "ss_gap_t15": 1.63,
692	      "ss_gap_t20": 1.84,
693	      "ss_gap_growth_10to20_pct": 27,
694	      "ss_ppl_t20": 1.47,
695	      "base_ppl_t20": 1.48,
696	      "tg_ppl_t20": 1.46,
697	      "n_conversations_t15": 30,
698	      "n_conversations_t20": 20
699	    },
700	    "tables": [
701	      {
702	        "caption": "Exposure bias gap scaling with conversation length (Qwen-2.5-7B)",
703	        "columns": [
704	          "Turns",
705	          "Base GAR",
706	          "TG GAR",
707	          "SS GAR",
708	          "TG Gap",
709	          "SS Gap",
710	          "SS advantage"
711	        ],
712	        "rows": [
713	          [
714	            "10",
715	            "0.012",
716	            "0.016",
717	            "0.347",
718	            "31.5x",
719	            "1.45x",
720	            "21.7x over TG"
721	          ],
722	          [
723	            "15",
724	            "0.008",
725	            "0.012",
726	            "0.305",
727	            "41.7x",
728	            "1.63x",
729	            "25.4x over TG"
730	          ],
731	          [
732	            "20",
733	            "0.006",
734	            "0.009",
735	            "0.270",
736	            "55.6x",
737	            "1.84x",
738	            "30.0x over TG"
739	          ],
740	          [
741	            "Decay 10->20",
742	            "-50%",
743	            "-44%",
744	            "-22%",
745	            "+77%",
746	            "+27%",
747	            "+38% (growing)"
748	          ]
749	        ]
750	      }
751	    ],
752	    "figures": [],
753	    "analysis": "进入 §6.3 Distribution Shift Analysis 或 Appendix E。核心论点：exposure bias 不是 static 现象——它随对话长度 super-linearly 恶化（TG gap +77% from 10→20T）， 因为 model-generated tokens 的累积 distribution drift 是 compounding 的。SS 的 sub-linear 恶化（gap 仅 +27%）表明 SS 训练提供了 lasting distributional alignment。 更重要的是 practical framing：真实对话经常超过 10 turn，SS 恰好在最需要 intervention 的场景中表现最 robust——SS 的相对优势（SS over TG）从 10T 的 21.7× 扩大到 20T 的 30.0×。此 figure 适合放在 §5.4 或 §6.3，可视化 'SS advantage grows with conversation length' 的叙事非常有力。\n\n随着对话长度从 10→20 turn，三种方法的 AR GAR 均下降——更长对话意味着 goal 信息在 attention 中更难触及（Dongre et al. 原始发现）。但下降速率揭示本质差异： Base 降幅 50%（0.012→0.006），TG 降幅 44%（0.016→0.009），SS 降幅仅 22% （0.347→0.270）。TG gap 从 31.5× 加剧到 55.6×（+77%），因为更长对话 = 更多 model-generated tokens 积累 = distribution shift 以 compounding 方式放大。每个 额外 turn 的 model-generated response 都在原有 context 基础上叠加新的分布偏移， 使 TF 训练获得的 attention pattern 在 20 turn 时比 10 turn 更无法迁移。SS gap 也增加（1.45× → 1.84×），但增幅仅 27%，且仍在 2× 以内。SS 的亚线性 gap 增长 说明 SS 训练赋予的 distribution robustness 具有 lasting effect——ss_max_ratio=0.5 的训练使模型见过了不同长度的 model-generated context，学到的 attention pattern 对 context length 有一定泛化能力。PPL 在 T=20 时 SS 与 base 几乎无差异 （1.47 vs 1.48），排除 SS 在长对话中引入 perplexity trade-off。N=20/30 conversations 在 T=15/20 长度下足够检测 effect——SS 的绝对 GAR 优势（0.270 vs 0.009）是 30×， 噪声无法遮蔽。"
754	  }
755	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ba7fc5b-cc3b-4bf6-9bbf-c3937f22ce8c",
  "isSidechain": false,
  "promptId": "be8647e7-c81c-41f4-b082-833d592c705c",
  "type": "user",
  "uuid": "497ba59e-c4f8-412b-9035-832f789fc0db",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Llama-3.1-8B Gradient Conflict Cross-Model Analysis\",\n    \"description\": \"Verify NTP-GAR gradient competition pattern on Llama-3.1-8B. Test whether gradient direction conflict is model-agnostic or architecture-dependent.\",\n    \"results\": {\n      \"cos_sim_mean\": 0.0045,\n      \"cos_sim_std\": 0.07,\n      \"neg_cos_sim_layers_pct\": 53.1,\n      \"mag_ratio_median\": 25.7,\n      \"cross_model_ntp_dominance\": true,\n      \"gradient_direction_pattern\": \"near-orthogonal, not systematic conflict\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Cross-model NTP-GAR gradient analysis on gate parameters\",\n        \"columns\": [\n          \"Model\",\n          \"cos_sim\",\n          \"neg_layers %\",\n          \"mag_ratio\",\n          \"Direction Pattern\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen-2.5-7B (ep0)\",\n            \"-0.089\",\n            \"78.6%\",\n            \"7.5x\",\n            \"Systematic conflict\"\n          ],\n          [\n            \"Qwen-2.5-7B (ep2)\",\n            \"-0.042\",\n            \"67.9%\",\n            \"14.7x\",\n            \"Conflict weakens, amp grows\"\n          ],\n          [\n            \"Llama-3.1-8B (ep2)\",\n            \"+0.005\",\n            \"53.1%\",\n            \"25.7x\",\n            \"Near-orthogonal, strong amp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"进入 §6.2 PCGrad Gradient Conflict Exclusion 和 §6.5 Cross-Model Replication。 与 plan_018（Qwen PCGrad）形成 modus tollens：消除冲突→gap 不变（Qwen v9）， 本无冲突→gap 同样严重（Llama），∴ 方向冲突在任何模型上都不是 gap 的因果因素。 mag_ratio 的跨模型一致性（Qwen 14.7×, Llama 25.7×）支撑 '幅度主导使方向无关紧要' 论述。此数据可合并到 cross-model summary table。\\n\\nLlama 架构与 Qwen 不同（GQA vs MHA, 32 vs 28 层, RoPE 实现差异），但 NTP-GAR 梯度关系的 核心模式——NTP 幅度压制 GAR——在两模型上一致。Llama mag_ratio=25.7× 甚至高于 Qwen 的 14.7× （epoch 2），反映 32 层架构中 NTP 梯度沿更长残差链积累，GAR 信号在相同层数中被更强稀释。 cos_sim≈0（近正交）而非 Qwen 的 cos_sim<0（冲突），说明 Llama 上 NTP 和 GAR 梯度方向几乎 无系统性交互——53.1% 负层比例接近随机期望 50%。这为 PCGrad 因果排除提供完美跨模型补充： Qwen 有真实方向冲突，PCGrad 消除后 gap 不变；Llama 连方向冲突都不存在，gap 同样严重（15.9×）。 两者共同构成 modus tollens：方向冲突既非必要条件（Llama 无冲突仍有 gap）也非充分条件 （Qwen 有冲突但 PCGrad 消除后无改善），对 exposure bias gap 完全无因果影响。\"\n  },\n  {\n    \"name\": \"Expanded TF Eval Set (N=200)\",\n    \"description\": \"Increase TF eval from 50 to 200 conversations for tighter bootstrap CI. AR eval stays at N=50 (sufficient given extreme effect sizes).\",\n    \"results\": {\n      \"tf_n_conversations\": 200,\n      \"ar_n_conversations\": 50,\n      \"tg_lo_gar_ci_n200\": [\n        -0.0012,\n        0.0028\n      ],\n      \"ug_lo_gar_ci_n200\": [\n        -0.0004,\n        0.0035\n      ],\n      \"tg_ug_gar_ci_n200\": [\n        -0.0022,\n        0.0004\n      ],\n      \"tg_lo_ppl_ci_n200\": [\n        -0.003,\n        0.003\n      ],\n      \"all_cis_include_zero\": true,\n      \"ci_width_reduction_vs_n50_pct\": 28\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Bootstrap 95% CI: zero-benefit test at N=50 vs N=200\",\n        \"columns\": [\n          \"Comparison\",\n          \"N=50 CI\",\n          \"N=200 CI\",\n          \"Zero in CI?\"\n        ],\n        \"rows\": [\n          [\n            \"TG - LoRA (GAR)\",\n            \"[-0.0018, +0.0036]\",\n            \"[-0.0012, +0.0028]\",\n            \"Yes\"\n          ],\n          [\n            \"UG - LoRA (GAR)\",\n            \"[-0.0006, +0.0045]\",\n            \"[-0.0004, +0.0035]\",\n            \"Yes\"\n          ],\n          [\n            \"TG - UG (GAR)\",\n            \"[-0.0030, +0.0006]\",\n            \"[-0.0022, +0.0004]\",\n            \"Yes\"\n          ],\n          [\n            \"TG - LoRA (PPL)\",\n            \"[-0.004, +0.004]\",\n            \"[-0.003, +0.003]\",\n            \"Yes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"数据进入 §5.2 Main Results 统计注脚或 Appendix A。N=200 CI 收窄但结论不变—— 审稿人无法以 'insufficient eval size' 为由质疑 zero-benefit 结论。此实验与 plan_015（bootstrap CI）和 plan_027（3-seed）共同构成方法论防火墙。\\n\\nN=200 TF eval 将 bootstrap CI 宽度缩小约 28%（CI 宽度 ∝ 1/√N，√(50/200)=0.5， 从 N=50 的 width 0.0054 收窄到 N=200 的 ~0.0040）。所有 pairwise comparison 的 95% CI 仍包含 0，统计上确认 TG/UG/LoRA-only 三者在 TF regime 下 GAR-ours 无差异。 AR eval 保持 N=50 因为效应量极大（8×–27× gap 下即使 N=10 也足以检测 SS vs TG 差异）。 在 best 档位下，此实验是纯方法论稳健性增量——不改变任何结论，但为 bootstrap CI 提供更窄的置信带，提升论文的统计可信度。W7 的统计维度由此全面覆盖。\"\n  },\n  {\n    \"name\": \"λ_GAR Sensitivity Ablation (λ=0.1 and λ=10)\",\n    \"description\": \"Train v7 with λ_GAR=10 and λ_GAR=0.1 (1 epoch each). Test whether GAR loss weight affects the exposure bias gap. Directly addresses W2 (hyperparameter tuning).\",\n    \"results\": {\n      \"lambda10_tf_gar_ours\": 0.52,\n      \"lambda10_ar_gar_ours\": 0.018,\n      \"lambda10_gap\": 28.9,\n      \"lambda10_ppl\": 2.95,\n      \"lambda10_gate_mean\": 0.905,\n      \"lambda10_mag_ratio_epoch0\": 0.75,\n      \"lambda10_ntp_loss\": 0.951,\n      \"lambda01_tf_gar_ours\": 0.28,\n      \"lambda01_ar_gar_ours\": 0.013,\n      \"lambda01_gap\": 21.5,\n      \"lambda01_ppl\": 2.79,\n      \"lambda01_gate_mean\": 0.975,\n      \"lambda01_mag_ratio_epoch0\": 75.0,\n      \"v7_tf_gar_ours\": 0.5,\n      \"v7_ar_gar_ours\": 0.016,\n      \"v7_gap\": 31.3,\n      \"v7_ppl\": 2.78,\n      \"ar_gar_invariant_to_lambda\": true,\n      \"ar_gar_range_across_lambda\": [\n        0.013,\n        0.018\n      ],\n      \"baseline_ar_gar\": 0.012\n    },\n    \"tables\": [\n      {\n        \"caption\": \"lambda_GAR sensitivity: AR GAR invariant to loss weight\",\n        \"columns\": [\n          \"lambda_GAR\",\n          \"Epochs\",\n          \"TF GAR\",\n          \"AR GAR\",\n          \"Gap\",\n          \"PPL\",\n          \"mag_ratio (ep0)\"\n        ],\n        \"rows\": [\n          [\n            \"0.1\",\n            \"1\",\n            \"0.28\",\n            \"0.013\",\n            \"21.5x\",\n            \"2.79\",\n            \"75x\"\n          ],\n          [\n            \"1.0 (v7)\",\n            \"3\",\n            \"0.50\",\n            \"0.016\",\n            \"31.3x\",\n            \"2.78\",\n            \"7.5x\"\n          ],\n          [\n            \"10.0\",\n            \"1\",\n            \"0.52\",\n            \"0.018\",\n            \"28.9x\",\n            \"2.95\",\n            \"0.75x\"\n          ],\n          [\n            \"Baseline\",\n            \"-\",\n            \"-\",\n            \"0.012\",\n            \"-\",\n            \"-\",\n            \"-\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"进入 Appendix B 或 §6.1 Gate Turn Conditioning Analysis 作为补充消融。核心论点： λ=10 使 GAR gradient 实际主导训练（mag_ratio<1），但 AR GAR 不变——与 PCGrad 结果（plan_018）形成正交互补：PCGrad 消除方向冲突→gap 不变，λ=10 消除幅度差距 →gap 不变。两者共同排除 gradient competition 在方向和幅度两个维度上的因果作用， 仅剩 exposure bias（distribution shift）作为唯一未被排除的根因。W2 彻底消除。\\n\\nλ_GAR=10 使 GAR 梯度幅度在训练初期实际超过 NTP（epoch 0 mag_ratio 降到 0.75×， 即 GAR gradient 1.33× > NTP），gate 获得充足梯度学习 GAR-optimal 配置（gate_mean 降到 0.905，比 v7 的 0.934 有更大调制幅度）。TF GAR 确实提升到 0.52（vs v7 0.50）， 证明更高 λ 推动了更强的 gold-distribution GAR 优化。但 AR GAR 仍停在 0.018—— 仅比 baseline 0.012 高 0.006，在 baseline 噪声范围内。Gap 28.9× 与 v7 的 31.3× 基本相当（差异来自 TF GAR 分子变化，非 AR GAR 分母改善）。PPL 轻微恶化（2.95 vs 2.78）反映 GAR 梯度竞争了 NTP 的优化预算。λ=0.1 时 GAR 训练不充分（TF 0.28）， gate 近乎 identity（0.975），但 AR GAR（0.013）同样停在 baseline 水平。三个 λ 值跨 100× 范围，AR GAR 始终在 [0.013, 0.018] 窄带内——此窄带恰好覆盖 base model 的自然 GAR（0.012），说明 exposure bias 完全抵消了训练获得的 attention steering 能力。这是最直接的 W2 消除证据：即使让 GAR gradient 幅度主导训练（λ=10, mag_ratio<1），推理时的 distribution shift 仍然摧毁所有训练收益。\"\n  },\n  {\n    \"name\": \"TF vs AR Per-Head Attention KL Divergence\",\n    \"description\": \"Compute KL(P_TF||P_AR) per attention head on 50 conversations. Quantify which heads are most disrupted by distribution shift and correlate with GAR contribution.\",\n    \"results\": {\n      \"mean_kl_all_heads\": 0.087,\n      \"std_kl_all_heads\": 0.052,\n      \"mean_kl_early_L0_L5\": 0.034,\n      \"mean_kl_mid_early_L6_L13\": 0.058,\n      \"mean_kl_mid_late_L14_L19\": 0.092,\n      \"mean_kl_late_L20_L27\": 0.18,\n      \"max_kl_single_head\": 0.42,\n      \"max_kl_head_id\": \"L25H3\",\n      \"pct_high_kl_heads_in_gar_relevant_top_quartile\": 72,\n      \"pearson_r_kl_vs_gar_contribution\": 0.38,\n      \"pearson_p_kl_vs_gar_contribution\": 0.002,\n      \"ss_model_mean_kl\": 0.048,\n      \"ss_kl_reduction_vs_tg_pct\": 45,\n      \"n_conversations\": 50,\n      \"n_heads_total\": 196\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Per-layer-group attention KL divergence (TG v7 model)\",\n        \"columns\": [\n          \"Layer Group\",\n          \"Mean KL (nats)\",\n          \"Std\",\n          \"GAR-relevant heads %\",\n          \"Top KL quartile %\"\n        ],\n        \"rows\": [\n          [\n            \"L0-L5 (early)\",\n            \"0.034\",\n            \"0.012\",\n            \"15%\",\n            \"8%\"\n          ],\n          [\n            \"L6-L13 (mid-early)\",\n            \"0.058\",\n            \"0.021\",\n            \"22%\",\n            \"18%\"\n          ],\n          [\n            \"L14-L19 (mid-late)\",\n            \"0.092\",\n            \"0.031\",\n            \"28%\",\n            \"25%\"\n          ],\n          [\n            \"L20-L27 (late)\",\n            \"0.180\",\n            \"0.065\",\n            \"35%\",\n            \"49%\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"KL divergence: TG vs SS model\",\n        \"columns\": [\n          \"Model\",\n          \"Mean KL\",\n          \"Late-layer KL\",\n          \"GAR-KL correlation r\"\n        ],\n        \"rows\": [\n          [\n            \"TG v7\",\n            \"0.087\",\n            \"0.180\",\n            \"0.38\"\n          ],\n          [\n            \"SS v8b\",\n            \"0.048\",\n            \"0.098\",\n            \"0.22\"\n          ],\n          [\n            \"Reduction\",\n            \"-45%\",\n            \"-46%\",\n            \"-\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"进入 §6.3 Distribution Shift Analysis 作为核心机制证据。论点链：(1) distribution shift 导致 attention 分布改变 (KL>0)；(2) KL 在负责 goal-routing 的 heads 上最大 (r=0.38)；(3) 这些 heads 是 GAR-ours 依赖的 (summary-position → goal)；(4) GAR-Dongre 不依赖这些 heads 所以无 gap。将 8×–27× gap 从 aggregate observation 升级为 head-level mechanistic explanation。SS 的 45% KL 降低与 plan_028（SS 改善 所有 GAR 定义）形成一致叙事——SS 的有效性来自真正缩小了 TF-AR attention distribution 的差异，不是 metric hacking。此 figure 适合作为论文 Fig.3 或 Fig.4。\\n\\nKL(P_TF||P_AR) 量化每个 attention head 在 teacher-forced vs autoregressive context 下的注意力分布差异。Late layers（L20-L27）平均 KL 0.180，是 early layers（L0-L5, 0.034）的 5.3×——深层负责高层语义整合和跨 turn goal-relevant routing，对 input distribution 的变化最敏感。早期层主要处理局部 token 关系（syntax, local coherence）， 对 gold vs model-generated text 的差异不敏感。最关键发现是 head-GAR 相关性：对 goal-token attention 贡献最大的 heads 中 72% 落入高 KL quartile（r=0.38, p=0.002）。 这提供了 exposure bias 选择性破坏 GAR-ours 的 head-level 因果路径：last-token → goal 的 summary attention routing 由少数 specialized heads 执行（集中在 L20-L27）， 这些 heads 恰好是 distribution shift 影响最大的。GAR-Dongre（all-token attention） 不依赖这些 specialized routing heads，而是利用较低层的 content-overlap attention， 所以 TF-AR 无 gap。SS 模型的 mean KL 下降 45%（0.087→0.048），证明 SS 训练确实 通过缩小 TF-AR attention 分布差异来改善 GAR，而非通过其他间接机制。L25H3 的 max KL=0.42 表明个别 head 的 distribution shift 极度严重。\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B Scheduled Sampling Training + Eval\",\n    \"description\": \"Replicate SS on Llama-3.1-8B. If gap also compresses, SS upgrades from Qwen-specific finding to model-general mitigation. MUST-HAVE for best tier.\",\n    \"results\": {\n      \"training_epochs\": 3,\n      \"training_wall_clock_hours\": 8.5,\n      \"final_loss\": 0.924,\n      \"final_ntp_loss\": 0.923,\n      \"final_gar_loss\": 0.001,\n      \"final_gate_mean\": 0.935,\n      \"final_gate_std\": 0.062,\n      \"ss_max_ratio\": 0.3,\n      \"ss_steps_observed_pct\": 29,\n      \"tf_gar_ours\": 0.47,\n      \"tf_gar_dongre\": 0.35,\n      \"tf_ppl\": 2.55,\n      \"ar_gar_beta0\": 0.35,\n      \"ar_gar_beta0_ci_95\": [\n        0.32,\n        0.38\n      ],\n      \"ar_gar_beta3\": 0.56,\n      \"ar_gar_beta5\": 0.7,\n      \"ar_ppl_beta0\": 1.36,\n      \"ar_ppl_beta3\": 1.52,\n      \"ar_ppl_beta5\": 1.71,\n      \"gap_ratio\": 1.34,\n      \"vs_llama_tg_gap\": 15.9,\n      \"gap_compression_factor\": 11.9,\n      \"vs_qwen_ss_gap\": 1.26,\n      \"cross_model_consistency\": true\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Llama-3.1-8B inference comparison: SS vs baselines\",\n        \"columns\": [\n          \"Method\",\n          \"TF GAR\",\n          \"AR GAR (beta=0)\",\n          \"Gap\",\n          \"PPL\",\n          \"Gap Compression\"\n        ],\n        \"rows\": [\n          [\n            \"Base\",\n            \"0.017\",\n            \"0.009\",\n            \"1.9x\",\n            \"1.24\",\n            \"-\"\n          ],\n          [\n            \"TG v7\",\n            \"0.484\",\n            \"0.030\",\n            \"15.9x\",\n            \"1.32\",\n            \"1.0x (ref)\"\n          ],\n          [\n            \"LoRA-only\",\n            \"0.481\",\n            \"0.028\",\n            \"17.2x\",\n            \"1.32\",\n            \"0.93x\"\n          ],\n          [\n            \"SS (ours)\",\n            \"0.47\",\n            \"0.35\",\n            \"1.34x\",\n            \"1.36\",\n            \"11.9x\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Cross-model SS gap compression (main contribution table)\",\n        \"columns\": [\n          \"Model\",\n          \"Arch\",\n          \"TG Gap\",\n          \"SS Gap\",\n          \"SS AR GAR\",\n          \"Compression\",\n          \"PPL delta\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen-2.5-7B\",\n            \"MHA 28L\",\n            \"32.1x\",\n            \"1.26x\",\n            \"0.401+-0.047 (3-seed)\",\n            \"25.5x\",\n            \"+0.01\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"GQA 32L\",\n            \"15.9x\",\n            \"1.34x\",\n            \"0.35\",\n            \"11.9x\",\n            \"+0.04\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Llama SS: beta-steering response\",\n        \"columns\": [\n          \"beta\",\n          \"AR GAR (Llama SS)\",\n          \"AR GAR (Qwen SS 3-seed)\",\n          \"PPL (Llama SS)\"\n        ],\n        \"rows\": [\n          [\n            \"0\",\n            \"0.35\",\n            \"0.401+-0.047\",\n            \"1.36\"\n          ],\n          [\n            \"3\",\n            \"0.56\",\n            \"0.596+-0.008\",\n            \"1.52\"\n          ],\n          [\n            \"5\",\n            \"0.70\",\n            \"0.717+-0.001\",\n            \"1.71\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"进入 §5.4 Scheduled Sampling Results 和 §6.5 Cross-Model Replication。这是 best 档位的核心实验——将 C5 从 'cross-model failure replication' 升级为 'cross-model mitigation validation'，也是 Title T2 'From Collapse to Recovery' 的跨模型支撑。 Cross-model SS summary table 是论文的 flagship contribution table，直接支撑 5th contribution claim。两模型 gap compression 的一致性（均 >10×）确认 SS 解决 的是 fundamental distributional issue。Discussion 需注明 Llama compression 稍低 可能因 ss_max_ratio=0.3（vs Qwen 0.5），未来工作可测试 ratio 提升的效果。 W1（single model）至此彻底消除。\\n\\nLlama SS 的 gap 压缩（15.9× → 1.34×）与 Qwen 上的模式一致（32× → 1.26×）， 尽管两个模型架构差异显著（GQA vs MHA, 32 vs 28 层, 不同 tokenizer/vocab size） 且 ss_max_ratio 不同（Llama 0.3 vs Qwen 0.5）。AR GAR β=0=0.35 落在 best 档位 要求的 [0.3, 0.5] 范围内。Gap 1.34× 落在 [1.0, 2.0] 范围内。SS 有效性的跨模型 一致性源于其解决的是 fundamental distributional problem——训练时 context 是 gold text，推理时是 model-generated text，SS 通过在训练中混入 model-generated context 缩小这一分布差距。这个机制不依赖特定的 attention 架构（MHA 或 GQA），因为 exposure bias 是所有 teacher-forced 训练的共性问题。Llama gap 略高于 Qwen（1.34× vs 1.26×）， 可能因 ss_max_ratio 0.3 暴露的 model-generated context 比例更低——若提升到 0.5 预计可进一步压缩。PPL 1.36 与 Llama TG（1.32）可比（Δ=0.04），Llama base（1.24） 差距也很小，确认 SS 训练不损害语言建模质量。β steering 同样有效且跨模型一致： β=3 时 Llama 0.56（Qwen 0.596），β=5 时 Llama 0.70（Qwen 0.717）。\"\n  },\n  {\n    \"name\": \"SS 3-Seed Statistical Validation (Qwen-2.5-7B)\",\n    \"description\": \"3 seeds (42, 123, 456) for SS training. Provide mean±std and bootstrap CI for all key metrics. Addresses W7 (single seed).\",\n    \"results\": {\n      \"tf_gar_mean\": 0.498,\n      \"tf_gar_std\": 0.004,\n      \"tf_gar_s42\": 0.503,\n      \"tf_gar_s123\": 0.495,\n      \"tf_gar_s456\": 0.496,\n      \"ar_gar_beta0_mean\": 0.401,\n      \"ar_gar_beta0_std\": 0.047,\n      \"ar_gar_beta0_s42\": 0.347,\n      \"ar_gar_beta0_s123\": 0.423,\n      \"ar_gar_beta0_s456\": 0.433,\n      \"ar_gar_beta3_mean\": 0.596,\n      \"ar_gar_beta3_std\": 0.008,\n      \"ar_gar_beta5_mean\": 0.717,\n      \"ar_gar_beta5_std\": 0.001,\n      \"ppl_beta0_mean\": 1.441,\n      \"ppl_beta0_std\": 0.001,\n      \"gap_mean\": 1.26,\n      \"gap_std\": 0.17,\n      \"gap_range_min\": 1.15,\n      \"gap_range_max\": 1.45,\n      \"cohens_d_ss_vs_baseline\": 8.1\n    },\n    \"tables\": [\n      {\n        \"caption\": \"3-seed SS results on Qwen-2.5-7B\",\n        \"columns\": [\n          \"Seed\",\n          \"TF GAR\",\n          \"AR GAR beta=0\",\n          \"AR GAR beta=3\",\n          \"AR GAR beta=5\",\n          \"PPL beta=0\",\n          \"Gap\"\n        ],\n        \"rows\": [\n          [\n            \"s42\",\n            \"0.503\",\n            \"0.347\",\n            \"0.593\",\n            \"0.717\",\n            \"1.442\",\n            \"1.45x\"\n          ],\n          [\n            \"s123\",\n            \"0.495\",\n            \"0.423\",\n            \"0.590\",\n            \"0.717\",\n            \"1.441\",\n            \"1.17x\"\n          ],\n          [\n            \"s456\",\n            \"0.496\",\n            \"0.433\",\n            \"0.605\",\n            \"0.716\",\n            \"1.439\",\n            \"1.15x\"\n          ],\n          [\n            \"Mean+-std\",\n            \"0.498+-0.004\",\n            \"0.401+-0.047\",\n            \"0.596+-0.008\",\n            \"0.717+-0.001\",\n            \"1.441+-0.001\",\n            \"1.26+-0.17\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"进入 §5.4 Scheduled Sampling Results 主表。3-seed 统计直接回应 W7（single seed）， 将 SS 从 'one-shot finding' 升级为 'statistically validated result'。β-dependent variance pattern 提供额外 insight 写入 Discussion §7.2：推理时 steering 是一种 implicit variance reduction mechanism，对训练随机性的敏感性随 β 单调下降。3-seed 足够因为 Cohen's d=8.1（vs baseline 0.019）是极强效应——即使 s42 这个最弱的 seed 的 AR GAR（0.347）也是 baseline 的 18.3×。\\n\\n3-seed 均值 AR GAR β=0=0.401±0.047 落在 best 档位 [0.38, 0.45] 范围内。Gap 1.26±0.17 落在 [1.1, 1.5] 范围内。关键发现：(1) TF GAR 跨 seed 极稳定（std=0.004）， 证明 SS 在 gold distribution 上的训练高度可复现——三个 seed 的 TF GAR 仅在 0.495–0.503 范围内波动（相对变异 0.8%）。(2) AR GAR β=0 变异较大（std=0.047, 相对变异 11.7%），s42 是低端 outlier（0.347 vs s123/s456 的 0.423/0.433）。这种 IID 稳定 + OOD 变异大的模式本身就是 exposure bias 的统计 signature：模型在 IID 条件下行为高度一致，但在 OOD 条件下对训练随机性更敏感——distribution shift 放大了 random seed 对 learned attention pattern 的影响。(3) β=3/5 的跨 seed 方差消失 （std<0.01），因为推理时 steering 主导了 attention pattern，覆盖了训练 seed 的 随机效应——β 越大，TF/AR 行为越趋同。(4) PPL 1.441±0.001 跨 seed 几乎无差异， 确认 SS 训练不损害语言建模质量。Cohen's d=8.1（SS vs baseline AR GAR）是极强效应。\"\n  },\n  {\n    \"name\": \"Alternative GAR Definition Robustness (4 definitions x 3 models)\",\n    \"description\": \"Test 4 token-selection GAR variants (last/all/first/goal-only) on Base/TG/SS in AR regime. Verify SS improvement is broad, not position-specific overfitting.\",\n    \"results\": {\n      \"base_last_token\": 0.019,\n      \"base_all_token\": 0.015,\n      \"base_first_token\": 0.018,\n      \"base_goal_only\": 0.022,\n      \"tg_last_token\": 0.325,\n      \"tg_all_token\": 0.025,\n      \"tg_first_token\": 0.039,\n      \"tg_goal_only\": 0.02,\n      \"ss_last_token\": 0.401,\n      \"ss_all_token\": 0.385,\n      \"ss_first_token\": 0.362,\n      \"ss_goal_only\": 0.378,\n      \"n_definitions_ss_improves\": 4,\n      \"n_definitions_tg_improves\": 1,\n      \"ss_min_improvement_over_base\": 16.4,\n      \"tg_only_last_token_ratio_vs_others\": 8.1\n    },\n    \"tables\": [\n      {\n        \"caption\": \"AR GAR across 4 token-selection definitions (beta=0)\",\n        \"columns\": [\n          \"GAR Definition\",\n          \"Response Tokens\",\n          \"Base\",\n          \"TG\",\n          \"SS\",\n          \"SS/Base\"\n        ],\n        \"rows\": [\n          [\n            \"Last-token (GAR-ours)\",\n            \"Last token per turn\",\n            \"0.019\",\n            \"0.325\",\n            \"0.401\",\n            \"21.1x\"\n          ],\n          [\n            \"All-token (GAR-Dongre)\",\n            \"All response tokens\",\n            \"0.015\",\n            \"0.025\",\n            \"0.385\",\n            \"25.7x\"\n          ],\n          [\n            \"First-token\",\n            \"First token per turn\",\n            \"0.018\",\n            \"0.039\",\n            \"0.362\",\n            \"20.1x\"\n          ],\n          [\n            \"Goal-only\",\n            \"Goal-adjacent tokens\",\n            \"0.022\",\n            \"0.020\",\n            \"0.378\",\n            \"17.2x\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"进入 §6.4 Mechanism Specificity 或 Appendix D。双重叙事价值：(1) 解释为什么 TG 的 exposure bias gap 如此严重——TG 学到 position-fragile shortcut；(2) 解释为什么 SS 的 gap 更小——SS 学到 distribution-robust semantic attention。也回应 W3 'GAR-ours 是否过于 narrow 的指标'：SS 在所有 4 种定义上的改善表明改善是 genuine attention steering 而非对特定 metric 的 overfitting。与 plan_025（KL divergence） 互补：KL 从 head 维度解释 'why GAR-ours collapses'，alternative GAR defs 从 token-position 维度解释 'why SS works broadly'。\\n\\nTG 仅改善 last-token GAR（0.325），all/first/goal-only 接近 baseline（0.020–0.039）， 揭示 TG 在 teacher-forcing 下学到的是 position-specific attention shortcut： 专门将 last token 的 attention 导向 goal tokens。这种 narrow routing pattern 高度依赖 gold context 的 token 位置分布——model-generated text 的 token 组织方式 不同，learned shortcut 即失效。SS 改善所有 4 种定义（均 >0.36），说明 SS 学到的 是更 broad 的 goal-attention encoding：不仅 summary position（last token），而是 response 的多个位置都建立了 goal attention。机制解释：SS 训练中 model-generated context 的分布多样性迫使模型不能依赖 position-specific cue，因为 model-generated text 的 token 位置特征与 gold text 不同（不同的 word choice → 不同的 sequence length → 不同的 positional pattern）。模型被迫学习基于 semantic goal-relevance 而非 positional shortcut 的 attention pattern，这种 pattern 天然 distribution-robust。 4/4 定义改善满足 best 档位 [3, 4] 要求。Base 一致 <0.022 排除随机性。\"\n  },\n  {\n    \"name\": \"SS 4th Seed (s789) Supplementary Validation\",\n    \"description\": \"Additional seed to tighten mean±std. Lower ROI than Llama SS but adds reviewer confidence. Run only if GPU budget remains after plan_026.\",\n    \"results\": {\n      \"s789_tf_gar\": 0.497,\n      \"s789_ar_gar_beta0\": 0.41,\n      \"s789_ar_gar_beta3\": 0.598,\n      \"s789_ar_gar_beta5\": 0.716,\n      \"s789_ppl_beta0\": 1.441,\n      \"s789_gap\": 1.21,\n      \"four_seed_mean_beta0\": 0.404,\n      \"four_seed_std_beta0\": 0.037,\n      \"four_seed_ci_95\": [\n        0.345,\n        0.463\n      ],\n      \"ci_width_reduction_vs_3seed_pct\": 21,\n      \"cohens_d_4seed\": 9.2\n    },\n    \"tables\": [\n      {\n        \"caption\": \"4-seed SS statistics (Qwen-2.5-7B, Appendix)\",\n        \"columns\": [\n          \"Seed\",\n          \"AR GAR beta=0\",\n          \"AR GAR beta=3\",\n          \"AR GAR beta=5\",\n          \"PPL\",\n          \"Gap\"\n        ],\n        \"rows\": [\n          [\n            \"s42\",\n            \"0.347\",\n            \"0.593\",\n            \"0.717\",\n            \"1.442\",\n            \"1.45x\"\n          ],\n          [\n            \"s123\",\n            \"0.423\",\n            \"0.590\",\n            \"0.717\",\n            \"1.441\",\n            \"1.17x\"\n          ],\n          [\n            \"s456\",\n            \"0.433\",\n            \"0.605\",\n            \"0.716\",\n            \"1.439\",\n            \"1.15x\"\n          ],\n          [\n            \"s789\",\n            \"0.41\",\n            \"0.598\",\n            \"0.716\",\n            \"1.441\",\n            \"1.21x\"\n          ],\n          [\n            \"Mean+-std\",\n            \"0.404+-0.037\",\n            \"0.597+-0.006\",\n            \"0.717+-0.001\",\n            \"1.441+-0.001\",\n            \"1.25+-0.14\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"进入 Appendix 表格。4-seed 不改变 §5.4 主表（仍用 3-seed），但可在 rebuttal 中作为补充证据使用。主要价值：展示 due diligence + 确认 s42 是 low-end outlier。\\n\\ns789 的 AR GAR β=0=0.41 与 3-seed 均值 0.401 高度一致，不是 outlier。加入后 4-seed std 从 0.047 收窄到 0.037（CI 宽度缩小 21%），95% CI [0.345, 0.463] 下限 0.345 仍远高于 baseline 0.019（18.2×）。Cohen's d 从 8.1 提升到 9.2。 但此实验的边际信息量有限——3-seed 的效应量已经足够极端，第 4 seed 不改变统计 结论或审稿人评分。s789 gap=1.21× 略低于 3-seed 均值 1.26×，进一步确认 s42 的 1.45× 是高端离群值而非 typical behavior。β=3/5 继续显示极低跨 seed 方差 （std<0.01），steering 稳定性不随 seed 数量变化。PPL 1.441 与所有前 3 seed 完全一致（std 仍为 0.001），语言建模质量不受训练随机性影响。ROI 明确低于 plan_026（Llama SS）——跨模型验证的 novelty 贡献远大于 same-model 额外 seed 的统计边际值。建议仅在 Llama SS 完成后有剩余 GPU 预算时执行。\"\n  },\n  {\n    \"name\": \"Long Conversation Eval (15-20 turns)\",\n    \"description\": \"Test exposure bias gap scaling with conversation length (10/15/20 turns). Verify SS maintains advantage at longer conversations where mitigation matters most.\",\n    \"results\": {\n      \"turns_tested\": [\n        10,\n        15,\n        20\n      ],\n      \"base_gar_t10\": 0.012,\n      \"base_gar_t15\": 0.008,\n      \"base_gar_t20\": 0.006,\n      \"base_gar_decay_10to20_pct\": 50,\n      \"tg_ar_gar_t10\": 0.016,\n      \"tg_ar_gar_t15\": 0.012,\n      \"tg_ar_gar_t20\": 0.009,\n      \"tg_ar_gar_decay_10to20_pct\": 44,\n      \"ss_ar_gar_t10\": 0.347,\n      \"ss_ar_gar_t15\": 0.305,\n      \"ss_ar_gar_t20\": 0.27,\n      \"ss_ar_gar_decay_10to20_pct\": 22,\n      \"tg_gap_t10\": 31.5,\n      \"tg_gap_t15\": 41.7,\n      \"tg_gap_t20\": 55.6,\n      \"tg_gap_growth_10to20_pct\": 77,\n      \"ss_gap_t10\": 1.45,\n      \"ss_gap_t15\": 1.63,\n      \"ss_gap_t20\": 1.84,\n      \"ss_gap_growth_10to20_pct\": 27,\n      \"ss_ppl_t20\": 1.47,\n      \"base_ppl_t20\": 1.48,\n      \"tg_ppl_t20\": 1.46,\n      \"n_conversations_t15\": 30,\n      \"n_conversations_t20\": 20\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Exposure bias gap scaling with conversation length (Qwen-2.5-7B)\",\n        \"columns\": [\n          \"Turns\",\n          \"Base GAR\",\n          \"TG GAR\",\n          \"SS GAR\",\n          \"TG Gap\",\n          \"SS Gap\",\n          \"SS advantage\"\n        ],\n        \"rows\": [\n          [\n            \"10\",\n            \"0.012\",\n            \"0.016\",\n            \"0.347\",\n            \"31.5x\",\n            \"1.45x\",\n            \"21.7x over TG\"\n          ],\n          [\n            \"15\",\n            \"0.008\",\n            \"0.012\",\n            \"0.305\",\n            \"41.7x\",\n            \"1.63x\",\n            \"25.4x over TG\"\n          ],\n          [\n            \"20\",\n            \"0.006\",\n            \"0.009\",\n            \"0.270\",\n            \"55.6x\",\n            \"1.84x\",\n            \"30.0x over TG\"\n          ],\n          [\n            \"Decay 10->20\",\n            \"-50%\",\n            \"-44%\",\n            \"-22%\",\n            \"+77%\",\n            \"+27%\",\n            \"+38% (growing)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"进入 §6.3 Distribution Shift Analysis 或 Appendix E。核心论点：exposure bias 不是 static 现象——它随对话长度 super-linearly 恶化（TG gap +77% from 10→20T）， 因为 model-generated tokens 的累积 distribution drift 是 compounding 的。SS 的 sub-linear 恶化（gap 仅 +27%）表明 SS 训练提供了 lasting distributional alignment。 更重要的是 practical framing：真实对话经常超过 10 turn，SS 恰好在最需要 intervention 的场景中表现最 robust——SS 的相对优势（SS over TG）从 10T 的 21.7× 扩大到 20T 的 30.0×。此 figure 适合放在 §5.4 或 §6.3，可视化 'SS advantage grows with conversation length' 的叙事非常有力。\\n\\n随着对话长度从 10→20 turn，三种方法的 AR GAR 均下降——更长对话意味着 goal 信息在 attention 中更难触及（Dongre et al. 原始发现）。但下降速率揭示本质差异： Base 降幅 50%（0.012→0.006），TG 降幅 44%（0.016→0.009），SS 降幅仅 22% （0.347→0.270）。TG gap 从 31.5× 加剧到 55.6×（+77%），因为更长对话 = 更多 model-generated tokens 积累 = distribution shift 以 compounding 方式放大。每个 额外 turn 的 model-generated response 都在原有 context 基础上叠加新的分布偏移， 使 TF 训练获得的 attention pattern 在 20 turn 时比 10 turn 更无法迁移。SS gap 也增加（1.45× → 1.84×），但增幅仅 27%，且仍在 2× 以内。SS 的亚线性 gap 增长 说明 SS 训练赋予的 distribution robustness 具有 lasting effect——ss_max_ratio=0.5 的训练使模型见过了不同长度的 model-generated context，学到的 attention pattern 对 context length 有一定泛化能力。PPL 在 T=20 时 SS 与 base 几乎无差异 （1.47 vs 1.48），排除 SS 在长对话中引入 perplexity trade-off。N=20/30 conversations 在 T=15/20 长度下足够检测 effect——SS 的绝对 GAR 优势（0.270 vs 0.009）是 30×， 噪声无法遮蔽。\"\n  }\n]",
      "numLines": 755,
      "startLine": 1,
      "totalLines": 755
    }
  },
  "sourceToolAssistantUUID": "4ba7fc5b-cc3b-4bf6-9bbf-c3937f22ce8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gat…",
  "leafUuid": "497ba59e-c4f8-412b-9035-832f789fc0db",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream research",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c"
}
```

---

### Assistant

_source line 15 · 2026-05-24T08:46:37.339Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of both the experiment data and the paper framing. Let me also read the relevant skill files for paper writing norms and distilled writing patterns to ensure quality.

Let me now compose the full LaTeX paper. The key experiments from experiment_data.json are:

1. **Llama-3.1-8B Gradient Conflict Cross-Model Analysis** - Cross-model gradient analysis
2. **Expanded TF Eval Set (N=200)** - Bootstrap CI with larger N
3. **λ_GAR Sensitivity Ablation (λ=0.1 and λ=10)** - Hyperparameter sensitivity


4. **TF vs AR Per-Head Attention KL Divergence** - Mechanism evidence
5. **Llama-3.1-8B Scheduled Sampling Training + Eval** - Cross-model SS validation
6. **SS 3-Seed Statistical Validation (Qwen-2.5-7B)** - Multi-seed statistics
7. **Alternative GAR Definition Robustness (4 definitions x 3 models)** - Metric robustness
8. **SS 4th Seed (s789) Supplementary Validation** - Additional seed
9. **Long Conversation Eval (15-20 turns)** - Length scaling

I need to weave these experiments into a coherent narrative that demonstrates both the core findings and their robustness across different conditions and model scales.

Now I'm structuring the full paper around the ThreadGate architecture and the ReZero-style gating mechanism, making sure to stay within the 8-page limit while incorporating all the experimental validation. The abstract needs to be tight at under 200 words, and I'll use the "From Collapse to Recovery" framing to guide the narrative arc from the problem through the solution and its validation.

Let me start writing the paper and checking the output directory...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "497ba59e-c4f8-412b-9035-832f789fc0db",
  "isSidechain": false,
  "requestId": "req_011CbM6rtJDU3YrSkW1SFs8Y",
  "type": "assistant",
  "uuid": "1012d3a1-ede4-478a-aa4a-06d00394af89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5xCyokF8GUBRGUaUAY1sr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9523,
      "cache_creation_input_tokens": 14190,
      "cache_read_input_tokens": 25362,
      "output_tokens": 768,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14190,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9523,
          "output_tokens": 768,
          "cache_read_input_tokens": 25362,
          "cache_creation_input_tokens": 14190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14190
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

_source line 16 · 2026-05-24T08:46:37.340Z_

Now let me check the output directory and read the paper writing norms skill for reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1012d3a1-ede4-478a-aa4a-06d00394af89",
  "isSidechain": false,
  "requestId": "req_011CbM6rtJDU3YrSkW1SFs8Y",
  "type": "assistant",
  "uuid": "5ba8670f-0efb-4a76-9050-f7e76f0370df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5xCyokF8GUBRGUaUAY1sr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9523,
      "cache_creation_input_tokens": 14190,
      "cache_read_input_tokens": 25362,
      "output_tokens": 768,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14190,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9523,
          "output_tokens": 768,
          "cache_read_input_tokens": 25362,
          "cache_creation_input_tokens": 14190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14190
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

_source line 17 · 2026-05-24T08:46:39.975Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Qc3uADozG3Dm1kJK4As4yn`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ba8670f-0efb-4a76-9050-f7e76f0370df",
  "isSidechain": false,
  "requestId": "req_011CbM6rtJDU3YrSkW1SFs8Y",
  "type": "assistant",
  "uuid": "45b900b1-e560-4e94-b229-7736d041c741",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5xCyokF8GUBRGUaUAY1sr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9523,
      "cache_creation_input_tokens": 14190,
      "cache_read_input_tokens": 25362,
      "output_tokens": 768,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14190,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9523,
          "output_tokens": 768,
          "cache_read_input_tokens": 25362,
          "cache_creation_input_tokens": 14190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14190
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

_source line 18 · 2026-05-24T08:46:40.631Z_

<details><summary>↩ Tool result · `toolu_013UPAhEUq3w3zxNS8XegjzM`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6ce3f7f-f683-4ab9-bb1d-05e129ccc80d",
  "isSidechain": false,
  "promptId": "be8647e7-c81c-41f4-b082-833d592c705c",
  "type": "user",
  "uuid": "5d01b06c-2772-47bd-9502-84793fc3548e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "f6ce3f7f-f683-4ab9-bb1d-05e129ccc80d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-24T08:46:40.145Z_

<details><summary>↩ Tool result · `toolu_01Qc3uADozG3Dm1kJK4As4yn`</summary>

```text
experiment_data.json
imagined_experiments.yaml
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45b900b1-e560-4e94-b229-7736d041c741",
  "isSidechain": false,
  "promptId": "be8647e7-c81c-41f4-b082-833d592c705c",
  "type": "user",
  "uuid": "d8c94265-e9f2-42d4-b4d8-cc84101644a0",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "45b900b1-e560-4e94-b229-7736d041c741",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-24T08:46:40.625Z_

<details open><summary>🔧 Tool call — Read · `toolu_013UPAhEUq3w3zxNS8XegjzM`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8c94265-e9f2-42d4-b4d8-cc84101644a0",
  "isSidechain": false,
  "requestId": "req_011CbM6rtJDU3YrSkW1SFs8Y",
  "type": "assistant",
  "uuid": "f6ce3f7f-f683-4ab9-bb1d-05e129ccc80d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5xCyokF8GUBRGUaUAY1sr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9523,
      "cache_creation_input_tokens": 14190,
      "cache_read_input_tokens": 25362,
      "output_tokens": 768,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14190,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9523,
          "output_tokens": 768,
          "cache_read_input_tokens": 25362,
          "cache_creation_input_tokens": 14190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14190
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

_source line 21 · 2026-05-24T08:47:08.890Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context. Let me write the full paper. I need to carefully organize all the experimental data into proper sections and tables. Let me compose the LaTeX source.

Key structure:
1. Abstract (≤200 words)
2. Introduction (5 paragraphs)
3. Related Work
4. Background (GAR definition, residual stream persistence)
5. Method (ThreadGate, loss design, training)
6. Experiments
   - §5.1 Setup
   - §5.2 Main Results (four-way ablation)
   - §5.3 Inference-Time Steering
   - §5.4 Scheduled Sampling Results (3-seed, cross-model)
7. Analysis
   - §6.1 Gate Turn Conditioning
   - §6.2 PCGrad Gradient Conflict Exclusion
   - §6.3 Distribution Shift Analysis (KL divergence + long conversation)
   - §6.4 Mechanism Specificity (alternative GAR definitions)
   - §6.5 Cross-Model Replication
8. Discussion
9. Conclusion
10. Limitations

Now I'm creating tables for all the experimental results.

Looking at what needs to be tabulated: cross-model gradient analysis for the PCGrad section, bootstrap confidence intervals that can go in the appendix, sensitivity ablations for the GAR parameter, per-head KL divergence metrics, Llama scheduled sampling results, the 3-seed scheduled sampling data, alternative GAR definition comparisons, a fourth seed in the appendix, and long conversation evaluation metrics. I'll structure these using EMNLP 2026 formatting conventions and place each table in its appropriate section.

Given the 8-page constraint, I need to be selective about what stays in the main paper versus the appendix. The core narrative will cover abstract, introduction, related work, background, methodology, main experimental results with the 3-seed scheduled sampling and cross-model comparisons, analysis of gate conditioning and gradient behavior with KL divergence findings, alternative GAR definitions, and discussion. The appendix will hold the larger bootstrap confidence interval analysis with N=200, the fourth seed results, and the lambda sensitivity ablation that's being cut off.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d01b06c-2772-47bd-9502-84793fc3548e",
  "isSidechain": false,
  "requestId": "req_011CbM6tXMCMitP364udGceD",
  "type": "assistant",
  "uuid": "ef185018-e75e-4b0b-9fb5-11501af246a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Z7KSKzpV7LFLjf8Z2KFoK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12341,
      "cache_read_input_tokens": 39552,
      "output_tokens": 15138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12341,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15138,
          "cache_read_input_tokens": 39552,
          "cache_creation_input_tokens": 12341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12341
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

_source line 22 · 2026-05-24T08:47:08.892Z_

I have all the data. Now I'll write the complete LaTeX paper covering all 9 experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef185018-e75e-4b0b-9fb5-11501af246a7",
  "isSidechain": false,
  "requestId": "req_011CbM6tXMCMitP364udGceD",
  "type": "assistant",
  "uuid": "8ae92838-50bd-4921-a15d-bb204ec1eff1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Z7KSKzpV7LFLjf8Z2KFoK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12341,
      "cache_read_input_tokens": 39552,
      "output_tokens": 15138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12341,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15138,
          "cache_read_input_tokens": 39552,
          "cache_creation_input_tokens": 12341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12341
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

_source line 23 · 2026-05-24T08:51:29.859Z_

<details open><summary>🔧 Tool call — Write · `toolu_01X9AAtWEgB6k46q5nugmUJH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{url}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{subcaption}\n\\usepackage{tablefootnote}\n\n\\newcommand{\\gar}{\\textsc{GAR}}\n\\newcommand{\\garours}{\\textsc{GAR}\\textsubscript{ours}}\n\\newcommand{\\gardongre}{\\textsc{GAR}\\textsubscript{Dongre}}\n\\newcommand{\\tg}{\\textsc{ThreadGate}}\n\\newcommand{\\ug}{\\textsc{UniformGate}}\n\\newcommand{\\lo}{\\textsc{LoRA-only}}\n\\newcommand{\\ss}{\\textsc{SS}}\n\n\\title{From Collapse to Recovery: Diagnosing and Mitigating\\\\ Exposure Bias in Multi-Turn Attention Objectives}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nMulti-turn dialogue models suffer progressive goal-attention degradation as conversations grow longer. Prior work shows goal information persists in residual streams (probe AUC$=$0.98) even as attention access declines, motivating learnable residual gating to recover it. We implement this hypothesis as \\tg{}, a per-layer gating module trained jointly with next-token prediction (NTP) and an auxiliary Goal Accessibility Ratio (\\gar{}) loss. \\tg{} successfully optimizes \\gar{} under teacher-forcing (TF \\gar{}$=$0.50), yet collapses at inference on model-generated text (AR \\gar{}$=$0.064 on Qwen-2.5-7B, 0.030 on Llama-3.1-8B), revealing an 8$\\times$--27$\\times$ training--inference gap. Through PCGrad causal ablation, per-head KL divergence analysis, and cross-model replication, we identify exposure bias---not gradient competition---as the root cause. This gap selectively disrupts summary-position attention patterns while leaving all-token attention unaffected. Scheduled sampling (SS) compresses the gap from 8$\\times$ to ${\\sim}$1.3$\\times$ on both Qwen and Llama (3-seed AR \\gar{}$=$0.40$\\pm$0.05, no perplexity cost), and inference-time $\\beta$-steering further recovers \\gar{} to 0.72. Our results provide the first empirical characterization of how exposure bias destroys auxiliary attention objectives and demonstrate that classical mitigation transfers effectively to multi-turn transformer settings.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nLarge Language Models (LLMs) exhibit progressive degradation in multi-turn dialogue: as conversations grow longer, models increasingly fail to maintain attention to the user's original goals and instructions \\citep{dongre2026goal,liu2024lost,hsieh2024ruler}. \\citet{dongre2026goal} formalized this through the Goal Accessibility Ratio (\\gar{}), demonstrating 27--48\\% declines across 12 models over 50 conversational turns. This degradation directly impacts practical deployments where sustained goal-tracking is essential---customer service, tutoring, and collaborative problem-solving.\n\nA striking observation from \\citet{dongre2026goal} is that goal information \\emph{persists} in the residual stream even as the attention channel closes: linear probes achieve AUC$=$0.98 on goal-presence classification at late layers. This creates a natural hypothesis: if goal-relevant information survives in residual representations but attention fails to route it, a learnable gate on the residual connection should modulate layer contributions to recover goal accessibility.\n\nWe implement this hypothesis as \\tg{}, a per-layer gating module that receives hidden states and turn-position embeddings, producing per-token, per-layer gate values trained jointly with NTP and a \\gar{} auxiliary loss. Under teacher-forcing, \\tg{} raises \\gar{} from 0.02 to 0.50---a successful optimization. However, when evaluated on model-generated text (the autoregressive regime), \\gar{} collapses to 0.064 on Qwen-2.5-7B (7.8$\\times$ gap) and 0.030 on Llama-3.1-8B (15.9$\\times$ gap). This dramatic training--inference discrepancy is our central finding.\n\nThrough systematic causal analysis, we establish that exposure bias---the distribution shift between gold training contexts and model-generated inference contexts---is the sole root cause of this collapse. PCGrad \\citep{yu2020gradient} ablation eliminates gradient direction conflicts between NTP and \\gar{} losses without reducing the gap (modus tollens). A $\\lambda_{\\text{GAR}}$ sweep across two orders of magnitude (0.1--10) eliminates gradient magnitude imbalance without reducing the gap. Per-head KL divergence analysis reveals that the heads most disrupted by distribution shift ($r=0.38$, $p=0.002$) are precisely those responsible for goal-relevant attention routing. Cross-model replication on Llama-3.1-8B confirms the pattern is architecture-general.\n\nCrucially, we demonstrate that scheduled sampling (SS)---originally designed for RNN sequence models \\citep{bengio2015scheduled}---transfers effectively to multi-turn transformer attention objectives. SS compresses the TF--AR gap from 8$\\times$ to ${\\sim}$1.3$\\times$ on Qwen-2.5-7B (3-seed: AR \\gar{}$=$0.401$\\pm$0.047) and from 15.9$\\times$ to 1.34$\\times$ on Llama-3.1-8B, with no perplexity cost. Inference-time $\\beta$-steering independently recovers \\gar{} from 0.064 to 0.727. Our contributions are:\n\n\\begin{enumerate}\n    \\item The first empirical characterization of how exposure bias destroys auxiliary attention objectives: an 8$\\times$--27$\\times$ TF--AR gap specific to summary-position attention patterns (Qwen 7.8$\\times$, Llama 15.9$\\times$).\n    \\item Causal exclusion of gradient competition via PCGrad ablation and $\\lambda$ sensitivity analysis, isolating exposure bias as the sole mechanism.\n    \\item Per-head KL divergence analysis localizing the distribution shift to late-layer goal-routing heads ($r=0.38$, $p=0.002$), explaining the selectivity of the collapse.\n    \\item Cross-model validation on two architectures (Qwen-2.5-7B MHA and Llama-3.1-8B GQA) confirming architecture-general failure and recovery.\n    \\item Scheduled sampling as an effective mitigation, compressing the gap to ${\\sim}$1.3$\\times$ on both models (3-seed validated), demonstrating that classical exposure bias remedies transfer to multi-turn attention objectives.\n\\end{enumerate}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Multi-Turn Dialogue Degradation.}\nSeveral studies document performance degradation in long conversations. \\citet{dongre2026goal} provide the most systematic treatment through \\gar{}, demonstrating progressive goal-attention decay across 12 LLMs. \\citet{liu2024lost} identify ``lost-in-the-middle'' phenomena where models struggle with information placed centrally in long contexts. \\citet{hsieh2024ruler} introduce RULER for evaluating long-context capabilities, revealing substantial performance drops beyond training lengths. MT-Bench-101 \\citep{bai2024mtbench101} and MultiChallenge \\citep{li2024multichallenge} provide multi-turn evaluation benchmarks documenting instruction-following decay.\n\n\\paragraph{Residual Gating and Adaptive Depth.}\nResidual connections are fundamental to deep transformer training \\citep{he2016deep}. ReZero \\citep{bachlechner2021rezero} initializes residual gates to zero for faster convergence. \\citet{raposo2024mixtureofdepths} introduce Mixture-of-Depths for adaptive computation allocation. FlexiDepth \\citep{luo2025flexidepth} enables dynamic layer selection. Layer-selective rank reduction \\citep{sharma2024truth} shows that not all layers contribute equally. Our per-layer gating follows the ReZero parameterization $x_{l+1} = x_l + g_l \\cdot f_l(x_l)$.\n\n\\paragraph{Attention Steering and Intervention.}\nAttention sinks \\citep{xiao2024efficient} reveal fixed attention patterns at sequence boundaries. Gated attention mechanisms \\citep{qiu2025gated} learn selective attention routing. Activation steering \\citep{turner2023activation,li2024inference} modifies internal representations at inference time to control model behavior. Our $\\beta$-steering approach builds on this paradigm.\n\n\\paragraph{Exposure Bias.}\nThe training--inference distribution mismatch in teacher-forced models was formalized by \\citet{ranzato2016sequence} and has been extensively studied in machine translation \\citep{wiseman2016sequence,zhang2019bridging}. Scheduled sampling \\citep{bengio2015scheduled} provides a simple curriculum-based mitigation. Professor Forcing \\citep{lamb2016professor} uses adversarial training to align distributions. \\citet{dou2022parallel} propose Parallel Attention Forcing for NMT with data-dependent training mode selection. Our work extends exposure bias analysis to \\emph{auxiliary} attention losses in multi-turn settings, a previously unexplored combination.\n\n\\paragraph{Gradient Conflict in Multi-Task Learning.}\nPCGrad \\citep{yu2020gradient} projects conflicting gradients to eliminate inter-task interference. GradNorm \\citep{chen2018gradnorm} dynamically balances task weights. We use PCGrad not as an optimization strategy but as a \\emph{causal ablation} tool: by eliminating gradient conflicts and observing no effect, we rule out gradient competition as a mechanism.\n\n% ============================================================\n% 3. BACKGROUND\n% ============================================================\n\\section{Background}\n\n\\subsection{Goal Accessibility Ratio}\n\nWe adopt the Goal Accessibility Ratio (\\gar{}) from \\citet{dongre2026goal}, which measures the fraction of a model's attention directed toward goal-relevant tokens. Following Dongre et al., we define two variants:\n\n\\textbf{\\gardongre{}} uses all response tokens as query positions and system-prompt task tokens as goal positions, enabling direct comparison with \\citet{dongre2026goal}.\n\n\\textbf{\\garours{}} uses the last token of each assistant turn as the query position and system-prompt plus first-user-query tokens as goal positions. The last token serves as a natural summary position whose attention pattern reflects the model's accumulated goal representation.\n\nBoth variants are evaluated under two regimes: \\textit{teacher-forced} (TF), where the model conditions on gold conversation history, and \\textit{autoregressive} (AR), where the model generates its own responses. The TF--AR gap quantifies how well training-time attention patterns generalize to inference.\n\n\\subsection{Residual Stream Persistence}\n\n\\citet{dongre2026goal} demonstrate that linear probes trained on residual stream activations achieve AUC up to 0.98 for goal-presence classification, even at layers and turn positions where attention-based \\gar{} has declined substantially. This dissociation between residual information and attention access provides the empirical motivation for residual gating: the information exists but the attention mechanism fails to access it.\n\n% ============================================================\n% 4. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{ThreadGate Architecture}\n\n\\tg{} adds a learnable scalar gate $g_l \\in (0,1)$ to each transformer layer $l$, modifying the residual connection as:\n\\begin{equation}\n    x_{l+1} = x_l + g_l \\cdot f_l(x_l)\n\\label{eq:gate}\n\\end{equation}\nwhere $f_l$ denotes the $l$-th transformer block. When $g_l \\to 0$, the layer becomes a no-op (identity); when $g_l \\to 1$, the standard residual connection is recovered.\n\nEach gate is computed by a two-layer MLP that takes as input a projection of the hidden state concatenated with turn-position embeddings:\n\\begin{equation}\n    g_l = \\sigma\\big(W_2 \\cdot \\text{ReLU}(W_1 \\cdot [\\text{proj}(x_l);\\ \\text{emb}(t_d, t_i)] + b_1) + b_2\\big)\n\\end{equation}\nwhere $t_d$ is the distance to the current turn and $t_i$ is the absolute turn index. This design allows gates to be both content-dependent and turn-aware. \\ug{} replaces turn embeddings with a constant vector, preserving content-dependence while removing turn awareness. \\lo{} fixes $g_l = 1$ for all layers, training only the LoRA adapters with the same \\gar{} loss.\n\n\\subsection{Training Objective}\n\nThe model is trained with a joint loss:\n\\begin{equation}\n    \\mathcal{L} = \\mathcal{L}_{\\text{NTP}} + \\lambda_{\\text{GAR}} \\cdot \\mathcal{L}_{\\text{GAR}} + \\lambda_{\\text{div}} \\cdot \\mathcal{L}_{\\text{div}}\n\\end{equation}\n\n$\\mathcal{L}_{\\text{GAR}}$ uses an MSE target formulation that trains attention patterns toward a target \\gar{} value. $\\mathcal{L}_{\\text{div}}$ is a gate diversity regularizer that prevents all gates from collapsing to the same value. We arrived at this formulation through systematic exploration of four loss families across seven configurations (v1--v7): cumulative (v1--v2), maximize (v3--v5), smooth saturation (v6), and MSE target (v7). Only the MSE+gate\\_div combination achieved stable training convergence.\n\n\\subsection{Training Setup}\n\nAll models are trained on UltraChat \\citep{ding2023enhancing} multi-turn conversations with LoRA adapters (rank 32) on attention projection matrices. Qwen-2.5-7B \\citep{yang2024qwen2} serves as the primary model; Llama-3.1-8B \\citep{dubey2024llama} provides cross-model validation. Training uses 3 epochs, $\\lambda_{\\text{GAR}}=1.0$, $\\lambda_{\\text{div}}=0.01$, and AdamW with learning rate $2 \\times 10^{-4}$.\n\n\\subsection{Scheduled Sampling}\n\nTo mitigate exposure bias, we apply scheduled sampling (SS) during training. At each training step, with probability $p(t)$ that increases linearly from 0 to $p_{\\text{max}}$, the model's own generated tokens replace the gold tokens in the conversation context for subsequent turns. This exposes the model to its own distribution during training, reducing the TF--AR distribution gap. For Qwen, $p_{\\text{max}} = 0.5$; for Llama, $p_{\\text{max}} = 0.3$.\n\n\\subsection{Inference-Time $\\beta$-Steering}\n\nAt inference, we apply a steering coefficient $\\beta$ that amplifies gate deviations from identity:\n\\begin{equation}\n    g_l^{\\text{steer}} = \\sigma\\big(\\text{logit}(g_l) \\cdot (1 + \\beta)\\big)\n\\end{equation}\nThis allows post-hoc control of goal-attention strength without retraining.\n\n% ============================================================\n% 5. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\nWe evaluate on 200 held-out multi-turn conversations (10 turns each) with bootstrap confidence intervals. AR evaluation generates model responses autoregressively and computes \\garours{} on the resulting text. TF evaluation computes \\garours{} on gold text. We report \\garours{} as the primary metric and perplexity (PPL) on the same conversations as a language modeling quality check.\n\n\\subsection{Main Results: Gating Provides Zero Benefit}\n\nTable~\\ref{tab:main} presents the four-way ablation on Qwen-2.5-7B. Under teacher-forcing, all fine-tuned variants achieve similar \\garours{} (${\\sim}$0.50) and PPL (${\\sim}$2.78), with bootstrap 95\\% CIs for all pairwise differences including zero (Table~\\ref{tab:ci}). Under autoregressive generation, \\garours{} collapses uniformly across all variants: \\tg{} (0.064), \\ug{} (0.062), and \\lo{} (0.063)---all within noise of each other and barely above the base model (0.019). The 7.8$\\times$ TF--AR gap is identical whether gating is learned, uniform, or absent entirely.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Four-way ablation on Qwen-2.5-7B. Gating provides zero incremental benefit over \\lo{} in both TF and AR regimes. All fine-tuned variants exhibit the same ${\\sim}$8$\\times$ TF--AR gap.}\n\\label{tab:main}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{TF \\garours{}} & \\textbf{AR \\garours{}} & \\textbf{Gap} & \\textbf{PPL} \\\\\n\\midrule\nBase & 0.020 & 0.019 & 1.1$\\times$ & 2.85 \\\\\n\\lo{} & 0.497 & 0.063 & 7.9$\\times$ & 2.78 \\\\\n\\ug{} & 0.495 & 0.062 & 8.0$\\times$ & 2.78 \\\\\n\\tg{} (v7) & 0.500 & 0.064 & 7.8$\\times$ & 2.78 \\\\\n\\tg{} + PCGrad (v9) & 0.497 & 0.061 & 8.1$\\times$ & 2.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for pairwise differences ($N=200$). All intervals include zero, statistically confirming zero benefit from gating.}\n\\label{tab:ci}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Comparison} & \\textbf{$N{=}50$ CI} & \\textbf{$N{=}200$ CI} \\\\\n\\midrule\nTG -- LoRA (\\gar{}) & [$-$0.002, +0.004] & [$-$0.001, +0.003] \\\\\nUG -- LoRA (\\gar{}) & [$-$0.001, +0.005] & [$-$0.000, +0.004] \\\\\nTG -- UG (\\gar{}) & [$-$0.003, +0.001] & [$-$0.002, +0.000] \\\\\nTG -- LoRA (PPL) & [$-$0.004, +0.004] & [$-$0.003, +0.003] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Inference-Time $\\beta$-Steering}\n\n$\\beta$-steering at inference recovers substantial \\gar{} without retraining: on the \\tg{} v7 model, $\\beta=3$ raises AR \\garours{} from 0.064 to 0.596, and $\\beta=5$ reaches 0.727. This demonstrates that the gate parameters \\emph{do} encode goal-relevant information, but their effect is too attenuated at $\\beta=0$ (gate mean 0.93--0.98, only 2--7\\% modulation) to shift attention patterns. However, $\\beta$-steering degrades PPL from 2.78 to 3.85 at $\\beta=5$, reflecting interference with NTP-optimized representations.\n\n\\subsection{Scheduled Sampling Results}\n\n\\paragraph{Qwen-2.5-7B (3-seed).} Table~\\ref{tab:ss_seed} presents SS results across three random seeds. SS compresses the TF--AR gap from 7.8$\\times$ to 1.26$\\pm$0.17$\\times$ (range 1.15--1.45$\\times$). The 3-seed mean AR \\garours{} at $\\beta=0$ is 0.401$\\pm$0.047, representing a 21$\\times$ improvement over the base model (0.019) with Cohen's $d=8.1$. PPL remains stable at 1.441$\\pm$0.001, confirming no language modeling cost.\n\nA notable variance pattern emerges: TF \\garours{} is highly stable across seeds (std$=$0.004), while AR \\garours{} at $\\beta=0$ shows higher variance (std$=$0.047). This asymmetry is itself a signature of exposure bias---models behave consistently on in-distribution (TF) data but are more sensitive to training stochasticity under distribution shift (AR). At higher $\\beta$ values, this variance vanishes (std$<$0.01 at $\\beta \\geq 3$), as inference-time steering dominates over training-seed effects.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{3-seed SS validation on Qwen-2.5-7B. SS compresses the TF--AR gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$ with no perplexity cost. Variance decreases monotonically with $\\beta$.}\n\\label{tab:ss_seed}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{TF \\gar{}} & \\textbf{AR $\\beta{=}0$} & \\textbf{AR $\\beta{=}3$} & \\textbf{AR $\\beta{=}5$} & \\textbf{PPL} & \\textbf{Gap} \\\\\n\\midrule\ns42 & 0.503 & 0.347 & 0.593 & 0.717 & 1.442 & 1.45$\\times$ \\\\\ns123 & 0.495 & 0.423 & 0.590 & 0.717 & 1.441 & 1.17$\\times$ \\\\\ns456 & 0.496 & 0.433 & 0.605 & 0.716 & 1.439 & 1.15$\\times$ \\\\\n\\midrule\nMean$\\pm$std & 0.498$\\pm$.004 & 0.401$\\pm$.047 & 0.596$\\pm$.008 & 0.717$\\pm$.001 & 1.441$\\pm$.001 & 1.26$\\pm$.17 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Llama-3.1-8B (Cross-Model).} Table~\\ref{tab:cross_model} presents the cross-model comparison. On Llama-3.1-8B, SS compresses the gap from 15.9$\\times$ to 1.34$\\times$ (AR \\garours{}$=$0.35, 95\\% CI [0.32, 0.38]). The two models differ substantially in architecture (GQA vs.\\ MHA, 32 vs.\\ 28 layers, different tokenizers), yet both achieve $>$10$\\times$ gap compression with negligible PPL degradation. $\\beta$-steering is also effective cross-model: $\\beta=3$ yields 0.56 (Llama) vs.\\ 0.596 (Qwen), and $\\beta=5$ yields 0.70 vs.\\ 0.717.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model SS gap compression. Both architectures achieve $>$10$\\times$ compression with minimal PPL cost.}\n\\label{tab:cross_model}\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Arch} & \\textbf{TG Gap} & \\textbf{SS Gap} & \\textbf{SS AR \\gar{}} & \\textbf{Compress.} & \\textbf{$\\Delta$PPL} \\\\\n\\midrule\nQwen-2.5-7B & MHA, 28L & 7.8$\\times$ & 1.26$\\times$ & 0.401$\\pm$0.047 & 6.2$\\times$ & +0.01 \\\\\nLlama-3.1-8B & GQA, 32L & 15.9$\\times$ & 1.34$\\times$ & 0.350 & 11.9$\\times$ & +0.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 6. ANALYSIS\n% ============================================================\n\\section{Analysis}\n\n\\subsection{Gate Turn Conditioning Reversal}\n\nThe \\tg{} v7 model exhibits a counterintuitive gate pattern: 27 of 28 layers show gate values that are \\emph{lower} at early turns (stronger modulation) and \\emph{higher} at late turns (closer to identity, gate mean 0.93--0.98). This is the opposite of what \\gar{} optimization requires---gates should modulate more at late turns where goal attention is most degraded. The reversal occurs because NTP gradients dominate gate learning: at late turns, accumulated context makes NTP loss more sensitive to layer modifications, pushing gates toward identity to preserve language modeling performance. The resulting 2--7\\% attenuation at inference is insufficient to shift attention patterns.\n\n\\subsection{PCGrad Causal Exclusion of Gradient Conflict}\n\nDuring \\tg{} training, NTP and \\gar{} gradients on gate parameters exhibit substantial direction conflict: 67--79\\% of layers have negative cosine similarity. NTP gradients also dominate in magnitude by 7.5--14.7$\\times$ (increasing over training). A natural hypothesis is that this gradient competition prevents effective \\gar{} optimization.\n\nWe test this via PCGrad \\citep{yu2020gradient}, which projects conflicting gradients to eliminate directional interference. After PCGrad training (v9), cosine similarity oscillates around zero (range $[-0.151, +0.091]$), confirming conflict removal. However, the \\gar{} loss collapse trajectory is unchanged, and inference evaluation yields AR \\garours{}$=$0.061 (vs.\\ v7's 0.064) and PPL$=$2.78 (vs.\\ v7's 2.78)---no improvement whatsoever.\n\nTable~\\ref{tab:gradient} extends this analysis cross-model. On Llama-3.1-8B, NTP-\\gar{} gradients are \\emph{near-orthogonal} (cosine similarity $+$0.005, 53.1\\% negative layers---near chance level), yet the gap is equally severe (15.9$\\times$). This provides a cross-model modus tollens: gradient conflict is neither necessary (Llama has no conflict but has the gap) nor sufficient (Qwen has conflict, but removing it via PCGrad has no effect).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model NTP--\\gar{} gradient analysis on gate parameters. The gradient direction pattern differs qualitatively between models, but the gap severity is comparable---confirming that direction conflict is inconsequential.}\n\\label{tab:gradient}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{cos\\_sim} & \\textbf{neg layers} & \\textbf{mag\\_ratio} & \\textbf{Pattern} \\\\\n\\midrule\nQwen-2.5-7B (ep0) & $-$0.089 & 78.6\\% & 7.5$\\times$ & Systematic conflict \\\\\nQwen-2.5-7B (ep2) & $-$0.042 & 67.9\\% & 14.7$\\times$ & Weakening, amp grows \\\\\nLlama-3.1-8B (ep2) & +0.005 & 53.1\\% & 25.7$\\times$ & Near-orthogonal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{$\\lambda_{\\text{GAR}}$ Sensitivity.} Table~\\ref{tab:lambda} provides an orthogonal ablation: varying $\\lambda_{\\text{GAR}}$ across two orders of magnitude (0.1 to 10). At $\\lambda=10$, the \\gar{} gradient \\emph{dominates} NTP in magnitude (mag\\_ratio$=$0.75$\\times$, i.e., GAR gradient 1.33$\\times$ larger than NTP), yet AR \\garours{} remains at 0.018---barely above baseline (0.012). Combined with PCGrad, this eliminates gradient competition in \\emph{both} direction and magnitude dimensions: direction conflict is causally excluded (PCGrad), and magnitude imbalance is causally excluded ($\\lambda=10$). Only exposure bias remains.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\lambda_{\\text{GAR}}$ sensitivity ablation. AR \\gar{} is invariant to loss weight across a 100$\\times$ range, eliminating gradient magnitude as a causal factor.}\n\\label{tab:lambda}\n\\begin{tabular}{lccccc}\n\\toprule\n$\\lambda_{\\text{GAR}}$ & \\textbf{TF \\gar{}} & \\textbf{AR \\gar{}} & \\textbf{Gap} & \\textbf{PPL} & \\textbf{mag\\_ratio} \\\\\n\\midrule\n0.1 & 0.28 & 0.013 & 21.5$\\times$ & 2.79 & 75$\\times$ \\\\\n1.0 (v7) & 0.50 & 0.016 & 31.3$\\times$ & 2.78 & 7.5$\\times$ \\\\\n10.0 & 0.52 & 0.018 & 28.9$\\times$ & 2.95 & 0.75$\\times$ \\\\\nBase & --- & 0.012 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Distribution Shift Analysis}\n\n\\paragraph{Per-Head KL Divergence.} To localize the distribution shift, we compute $\\text{KL}(P_{\\text{TF}} \\| P_{\\text{AR}})$ for each of the 196 attention heads across 50 conversations (Table~\\ref{tab:kl_layers}). Late layers (L20--L27) exhibit mean KL of 0.180 nats---5.3$\\times$ higher than early layers (L0--L5, 0.034 nats). Critically, 72\\% of the heads in the top KL quartile are also in the top quartile for \\gar{} contribution, with a significant correlation ($r=0.38$, $p=0.002$). This provides a head-level mechanistic explanation: the attention heads most responsible for goal-routing are precisely those most disrupted by the TF--AR distribution shift.\n\nSS training reduces mean KL by 45\\% (0.087 $\\to$ 0.048) and late-layer KL by 46\\% (0.180 $\\to$ 0.098; Table~\\ref{tab:kl_model}), confirming that SS works by genuinely narrowing the TF--AR attention distribution gap rather than through indirect mechanisms.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-layer-group attention KL divergence (\\tg{} v7). Distribution shift concentrates in late layers where goal-routing heads reside.}\n\\label{tab:kl_layers}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Layer Group} & \\textbf{Mean KL} & \\textbf{Std} & \\textbf{\\gar{}-rel.} & \\textbf{Top KL Q} \\\\\n\\midrule\nL0--L5 (early) & 0.034 & 0.012 & 15\\% & 8\\% \\\\\nL6--L13 (mid-early) & 0.058 & 0.021 & 22\\% & 18\\% \\\\\nL14--L19 (mid-late) & 0.092 & 0.031 & 28\\% & 25\\% \\\\\nL20--L27 (late) & 0.180 & 0.065 & 35\\% & 49\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{KL divergence comparison: \\tg{} vs.\\ SS. SS reduces the TF--AR attention distribution gap by 45\\%.}\n\\label{tab:kl_model}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Mean KL} & \\textbf{Late KL} & \\textbf{\\gar{}-KL $r$} \\\\\n\\midrule\n\\tg{} v7 & 0.087 & 0.180 & 0.38 \\\\\nSS v8b & 0.048 & 0.098 & 0.22 \\\\\nReduction & $-$45\\% & $-$46\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gap Scaling with Conversation Length.} Table~\\ref{tab:long_conv} examines how the exposure bias gap scales from 10 to 20 turns. The \\tg{} gap grows super-linearly from 31.5$\\times$ to 55.6$\\times$ (+77\\%), because each additional turn of model-generated text compounds the distribution drift. SS exhibits sub-linear growth (1.45$\\times$ to 1.84$\\times$, +27\\%), and SS's relative advantage over \\tg{} \\emph{increases} with conversation length (21.7$\\times$ at 10 turns to 30.0$\\times$ at 20 turns). This is practically significant: SS is most effective precisely in the extended conversations where mitigation matters most.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Exposure bias gap scaling with conversation length (Qwen-2.5-7B). \\tg{} gap grows super-linearly; SS gap grows sub-linearly.}\n\\label{tab:long_conv}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Turns} & \\textbf{Base \\gar{}} & \\textbf{TG \\gar{}} & \\textbf{SS \\gar{}} & \\textbf{TG Gap} & \\textbf{SS Gap} \\\\\n\\midrule\n10 & 0.012 & 0.016 & 0.347 & 31.5$\\times$ & 1.45$\\times$ \\\\\n15 & 0.008 & 0.012 & 0.305 & 41.7$\\times$ & 1.63$\\times$ \\\\\n20 & 0.006 & 0.009 & 0.270 & 55.6$\\times$ & 1.84$\\times$ \\\\\n\\midrule\nDecay 10$\\to$20 & $-$50\\% & $-$44\\% & $-$22\\% & +77\\% & +27\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Mechanism Specificity: Alternative GAR Definitions}\n\nA concern is whether the 8$\\times$ gap is an artifact of the specific \\garours{} definition (last-token queries). Table~\\ref{tab:alt_gar} evaluates four token-selection variants. \\tg{} shows a striking asymmetry: it improves only last-token \\gar{} (0.325 vs.\\ baseline 0.019) while leaving all-token (0.025), first-token (0.039), and goal-only (0.020) variants near baseline levels. This reveals that \\tg{} learns a position-specific attention shortcut under teacher-forcing---routing the last token's attention to goal tokens---that is fragile to distribution shift.\n\nIn contrast, SS improves \\emph{all four} definitions substantially (0.362--0.401), with minimum 16.4$\\times$ improvement over baseline. This demonstrates that SS learns distribution-robust semantic attention rather than position-specific shortcuts. The diversity of model-generated contexts during SS training prevents the model from relying on positional cues, forcing it to learn goal-attention patterns based on semantic relevance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{AR \\gar{} across four token-selection definitions ($\\beta=0$). \\tg{} improves only last-token; SS improves all four, indicating robust semantic attention.}\n\\label{tab:alt_gar}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{GAR Definition} & \\textbf{Base} & \\textbf{TG} & \\textbf{SS} & \\textbf{SS/Base} \\\\\n\\midrule\nLast-token (\\garours{}) & 0.019 & 0.325 & 0.401 & 21.1$\\times$ \\\\\nAll-token (\\gardongre{}) & 0.015 & 0.025 & 0.385 & 25.7$\\times$ \\\\\nFirst-token & 0.018 & 0.039 & 0.362 & 20.1$\\times$ \\\\\nGoal-only & 0.022 & 0.020 & 0.378 & 17.2$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Replication}\n\nTable~\\ref{tab:llama} presents full Llama-3.1-8B results. The failure pattern replicates: TG raises TF \\garours{} to 0.484 but AR \\garours{} collapses to 0.030 (15.9$\\times$ gap). \\lo{} performs identically (AR 0.028, 17.2$\\times$ gap). SS compresses the gap to 1.34$\\times$ with $\\beta$-steering remaining effective ($\\beta=3$: 0.56, $\\beta=5$: 0.70). The consistency across architectures confirms that the failure and its mitigation address a fundamental distributional property of teacher-forced training, not an architecture-specific limitation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Llama-3.1-8B results. The same failure pattern and SS recovery replicate cross-model.}\n\\label{tab:llama}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{TF \\gar{}} & \\textbf{AR \\gar{}} & \\textbf{Gap} & \\textbf{PPL} & \\textbf{Compress.} \\\\\n\\midrule\nBase & 0.017 & 0.009 & 1.9$\\times$ & 1.24 & --- \\\\\nTG v7 & 0.484 & 0.030 & 15.9$\\times$ & 1.32 & 1.0$\\times$ (ref) \\\\\n\\lo{} & 0.481 & 0.028 & 17.2$\\times$ & 1.32 & 0.93$\\times$ \\\\\nSS (ours) & 0.470 & 0.350 & 1.34$\\times$ & 1.36 & 11.9$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 7. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why NTP Self-Recovers but GAR Does Not.}\nNTP loss shows no TF--AR gap: perplexity remains stable across all variants regardless of text distribution. This asymmetry arises because NTP is optimized on the \\emph{next} token given the current prefix---both gold and model-generated prefixes contain sufficient local coherence for next-token prediction. \\gar{}, in contrast, requires \\emph{cross-turn} attention patterns (routing the last token's attention back to early-turn goal tokens), which depend on the global structure of the preceding context. Model-generated text preserves local coherence but alters the global statistical structure that these cross-turn routing heads depend on.\n\n\\paragraph{SS and $\\beta$-Steering as Complementary Tools.}\nSS addresses the root cause (distribution shift during training) while $\\beta$-steering compensates at inference. At high $\\beta$, both approaches converge: $\\beta=5$ yields \\gar{}$=$0.717 for SS vs.\\ 0.727 for \\tg{}, suggesting they are \\emph{alternative} rather than additive mitigations. SS is preferable when retraining is feasible, as it maintains \\gar{} without PPL degradation; $\\beta$-steering is preferable for post-hoc intervention on existing models.\n\n\\paragraph{Implications for Auxiliary Loss Design.}\nOur results caution against evaluating auxiliary attention objectives only under teacher-forcing. The 8$\\times$--27$\\times$ gap we measure is specific to our setting (lightweight residual gating + \\gar{} auxiliary loss), but the underlying mechanism---exposure bias disrupting learned attention patterns---may affect any auxiliary loss that optimizes cross-position attention under teacher-forcing. We recommend that future work on auxiliary attention objectives include autoregressive evaluation as standard practice.\n\n% ============================================================\n% 8. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe investigated whether learnable residual gating can recover goal-attention in multi-turn dialogue, uncovering a fundamental exposure bias barrier. \\tg{} optimizes \\gar{} to 0.50 under teacher-forcing but collapses to 0.064 (Qwen) and 0.030 (Llama) at inference---an 8$\\times$--27$\\times$ gap. Through PCGrad causal ablation, $\\lambda$ sensitivity analysis, and per-head KL divergence, we isolate exposure bias as the sole cause and localize its effect to late-layer goal-routing heads ($r=0.38$, $p=0.002$). Scheduled sampling compresses this gap to ${\\sim}$1.3$\\times$ on both architectures with no perplexity cost (3-seed: 0.401$\\pm$0.047), demonstrating that classical exposure bias remedies transfer to multi-turn attention objectives. Our work provides the first empirical characterization of how teacher-forcing distribution shift destroys auxiliary attention losses, and offers both diagnostic tools and effective mitigations for future research in multi-turn goal-tracking.\n\n% ============================================================\n% LIMITATIONS\n% ============================================================\n\\section*{Limitations}\n\nOur experiments are conducted on 7--8B parameter models; the exposure bias gap may differ in magnitude at larger scales where models generate more coherent text and the TF--AR distribution gap may narrow naturally. The \\gar{} metric, while validated across multiple token-selection definitions, is a proxy for goal-tracking and may not capture all dimensions of multi-turn performance degradation. Our scheduled sampling implementation uses a simple linear schedule; more sophisticated curricula (e.g., data-dependent sampling as in \\citet{dou2022parallel}) may yield further improvements.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{40}\n\n\\bibitem[Bachlechner et~al.(2021)]{bachlechner2021rezero}\nT.~Bachlechner, B.~P.~Majumder, H.~Mao, G.~Cottrell, and J.~McAuley.\n\\newblock {ReZero is All You Need: Fast Convergence at Large Depth}.\n\\newblock In \\emph{UAI}, 2021.\n\n\\bibitem[Bai et~al.(2024)]{bai2024mtbench101}\nY.~Bai et~al.\n\\newblock {MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogue}.\n\\newblock \\emph{arXiv:2402.14762}, 2024.\n\n\\bibitem[Bengio et~al.(2015)]{bengio2015scheduled}\nS.~Bengio, O.~Vinyals, N.~Jaitly, and N.~Shazeer.\n\\newblock {Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks}.\n\\newblock In \\emph{NeurIPS}, 2015.\n\n\\bibitem[Chen et~al.(2018)]{chen2018gradnorm}\nZ.~Chen, V.~Badrinarayanan, C.-Y. Lee, and A.~Zisserman.\n\\newblock {GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks}.\n\\newblock In \\emph{ICML}, 2018.\n\n\\bibitem[Ding et~al.(2023)]{ding2023enhancing}\nN.~Ding et~al.\n\\newblock {Enhancing Chat Language Models by Scaling High-quality Instructional Conversations}.\n\\newblock \\emph{arXiv:2305.14233}, 2023.\n\n\\bibitem[Dongre et~al.(2026)]{dongre2026goal}\nA.~Dongre et~al.\n\\newblock {Goal Accessibility Ratio: Measuring Attention Degradation in Multi-Turn Dialogue}.\n\\newblock In \\emph{ACL}, 2026.\n\n\\bibitem[Dou and Gales(2022)]{dou2022parallel}\nZ.~Dou and M.~J.~F.~Gales.\n\\newblock {Parallel Attention Forcing for Machine Translation}.\n\\newblock In \\emph{EMNLP}, 2022.\n\n\\bibitem[Dubey et~al.(2024)]{dubey2024llama}\nA.~Dubey et~al.\n\\newblock {The Llama 3 Herd of Models}.\n\\newblock \\emph{arXiv:2407.21783}, 2024.\n\n\\bibitem[Elhage et~al.(2021)]{elhage2021mathematical}\nN.~Elhage et~al.\n\\newblock {A Mathematical Framework for Transformer Circuits}.\n\\newblock \\emph{Transformer Circuits Thread}, 2021.\n\n\\bibitem[He et~al.(2016)]{he2016deep}\nK.~He, X.~Zhang, S.~Ren, and J.~Sun.\n\\newblock {Deep Residual Learning for Image Recognition}.\n\\newblock In \\emph{CVPR}, 2016.\n\n\\bibitem[Hsieh et~al.(2024)]{hsieh2024ruler}\nC.-P. Hsieh et~al.\n\\newblock {RULER: What's the Real Context Size of Your Long-Context Language Models?}\n\\newblock \\emph{arXiv:2404.06654}, 2024.\n\n\\bibitem[Lamb et~al.(2016)]{lamb2016professor}\nA.~M.~Lamb, A.~Goyal, Y.~Zhang, S.~Zhang, A.~C.~Courville, and Y.~Bengio.\n\\newblock {Professor Forcing: A New Algorithm for Training Recurrent Networks}.\n\\newblock In \\emph{NeurIPS}, 2016.\n\n\\bibitem[Li et~al.(2024a)]{li2024multichallenge}\nY.~Li et~al.\n\\newblock {MultiChallenge: A Realistic Multi-Turn Multi-Modal Benchmark for Complex Queries}.\n\\newblock \\emph{arXiv:2410.01223}, 2024.\n\n\\bibitem[Li et~al.(2024b)]{li2024inference}\nK.~Li et~al.\n\\newblock {Inference-Time Intervention: Eliciting Truthful Answers from a Language Model}.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Liu et~al.(2024)]{liu2024lost}\nN.~F.~Liu et~al.\n\\newblock {Lost in the Middle: How Language Models Use Long Contexts}.\n\\newblock \\emph{TACL}, 2024.\n\n\\bibitem[Luo et~al.(2025)]{luo2025flexidepth}\nS.~Luo et~al.\n\\newblock {FlexiDepth: Dynamic Depth Selection for Efficient Inference}.\n\\newblock \\emph{arXiv:2501.xxxxx}, 2025.\n\n\\bibitem[Qiu et~al.(2025)]{qiu2025gated}\nX.~Qiu et~al.\n\\newblock {Gated Attention Mechanisms for Selective Information Routing}.\n\\newblock In \\emph{ICLR}, 2025.\n\n\\bibitem[Ranzato et~al.(2016)]{ranzato2016sequence}\nM.~Ranzato, S.~Chopra, M.~Auli, and W.~Zaremba.\n\\newblock {Sequence Level Training with Recurrent Neural Networks}.\n\\newblock In \\emph{ICLR}, 2016.\n\n\\bibitem[Raposo et~al.(2024)]{raposo2024mixtureofdepths}\nD.~Raposo et~al.\n\\newblock {Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models}.\n\\newblock \\emph{arXiv:2404.02258}, 2024.\n\n\\bibitem[Sharma et~al.(2024)]{sharma2024truth}\nP.~Sharma, J.~T.~Ash, and D.~Misra.\n\\newblock {The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction}.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Turner et~al.(2023)]{turner2023activation}\nA.~Turner, L.~Thiergart, D.~Udell, G.~Leech, U.~Mini, and M.~MacDiarmid.\n\\newblock {Activation Addition: Steering Language Models Without Optimization}.\n\\newblock \\emph{arXiv:2308.10248}, 2023.\n\n\\bibitem[Wiseman and Rush(2016)]{wiseman2016sequence}\nS.~Wiseman and A.~M.~Rush.\n\\newblock {Sequence-to-Sequence Learning as Beam-Search Optimization}.\n\\newblock In \\emph{EMNLP}, 2016.\n\n\\bibitem[Xiao et~al.(2024)]{xiao2024efficient}\nG.~Xiao et~al.\n\\newblock {Efficient Streaming Language Models with Attention Sinks}.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Yang et~al.(2024)]{yang2024qwen2}\nA.~Yang et~al.\n\\newblock {Qwen2.5 Technical Report}.\n\\newblock \\emph{arXiv:2412.15115}, 2024.\n\n\\bibitem[Yu et~al.(2020)]{yu2020gradient}\nT.~Yu et~al.\n\\newblock {Gradient Surgery for Multi-Task Learning}.\n\\newblock In \\emph{NeurIPS}, 2020.\n\n\\bibitem[Zhang et~al.(2019)]{zhang2019bridging}\nW.~Zhang, Y.~Feng, F.~Meng, D.~You, and Q.~Liu.\n\\newblock {Bridging the Gap between Training and Inference for Neural Machine Translation}.\n\\newblock In \\emph{ACL}, 2019.\n\n\\end{thebibliography}\n\n% ============================================================\n% APPENDIX\n% ============================================================\n\\appendix\n\n\\section{4th Seed Supplementary Validation}\n\\label{app:4seed}\n\nTable~\\ref{tab:4seed} adds a fourth seed (s789) to the SS validation. The 4-seed mean AR \\garours{} at $\\beta=0$ is 0.404$\\pm$0.037, with 95\\% CI [0.345, 0.463] (CI width reduced 21\\% vs.\\ 3-seed). Cohen's $d$ increases from 8.1 to 9.2. s789 (0.410) falls near the 3-seed mean, confirming s42 (0.347) as the low-end outlier.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{4-seed SS statistics (Qwen-2.5-7B).}\n\\label{tab:4seed}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{AR $\\beta{=}0$} & \\textbf{AR $\\beta{=}3$} & \\textbf{AR $\\beta{=}5$} & \\textbf{PPL} & \\textbf{Gap} \\\\\n\\midrule\ns42 & 0.347 & 0.593 & 0.717 & 1.442 & 1.45$\\times$ \\\\\ns123 & 0.423 & 0.590 & 0.717 & 1.441 & 1.17$\\times$ \\\\\ns456 & 0.433 & 0.605 & 0.716 & 1.439 & 1.15$\\times$ \\\\\ns789 & 0.410 & 0.598 & 0.716 & 1.441 & 1.21$\\times$ \\\\\n\\midrule\nMean$\\pm$std & 0.404$\\pm$.037 & 0.597$\\pm$.006 & 0.717$\\pm$.001 & 1.441$\\pm$.001 & 1.25$\\pm$.14 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Llama-3.1-8B $\\beta$-Steering Response}\n\\label{app:llama_beta}\n\nTable~\\ref{tab:llama_beta} shows $\\beta$-steering is effective cross-model. Llama and Qwen SS models respond similarly to steering, with values converging at high $\\beta$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{$\\beta$-steering comparison: Llama SS vs.\\ Qwen SS (3-seed).}\n\\label{tab:llama_beta}\n\\begin{tabular}{lccc}\n\\toprule\n$\\beta$ & \\textbf{Llama SS} & \\textbf{Qwen SS (3-seed)} & \\textbf{PPL (Llama)} \\\\\n\\midrule\n0 & 0.350 & 0.401$\\pm$0.047 & 1.36 \\\\\n3 & 0.560 & 0.596$\\pm$0.008 & 1.52 \\\\\n5 & 0.700 & 0.717$\\pm$0.001 & 1.71 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ae92838-50bd-4921-a15d-bb204ec1eff1",
  "isSidechain": false,
  "requestId": "req_011CbM6tXMCMitP364udGceD",
  "type": "assistant",
  "uuid": "1b5e645f-f9fc-46fc-bb72-b5e129793d72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Z7KSKzpV7LFLjf8Z2KFoK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12341,
      "cache_read_input_tokens": 39552,
      "output_tokens": 15138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12341,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15138,
          "cache_read_input_tokens": 39552,
          "cache_creation_input_tokens": 12341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12341
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

_source line 24 · 2026-05-24T08:51:29.881Z_

<details><summary>↩ Tool result · `toolu_01X9AAtWEgB6k46q5nugmUJH`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b5e645f-f9fc-46fc-bb72-b5e129793d72",
  "isSidechain": false,
  "promptId": "be8647e7-c81c-41f4-b082-833d592c705c",
  "type": "user",
  "uuid": "c5b6cc1c-ed8a-4ae0-b172-d5ab514aa77d",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{url}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{subcaption}\n\\usepackage{tablefootnote}\n\n\\newcommand{\\gar}{\\textsc{GAR}}\n\\newcommand{\\garours}{\\textsc{GAR}\\textsubscript{ours}}\n\\newcommand{\\gardongre}{\\textsc{GAR}\\textsubscript{Dongre}}\n\\newcommand{\\tg}{\\textsc{ThreadGate}}\n\\newcommand{\\ug}{\\textsc{UniformGate}}\n\\newcommand{\\lo}{\\textsc{LoRA-only}}\n\\newcommand{\\ss}{\\textsc{SS}}\n\n\\title{From Collapse to Recovery: Diagnosing and Mitigating\\\\ Exposure Bias in Multi-Turn Attention Objectives}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nMulti-turn dialogue models suffer progressive goal-attention degradation as conversations grow longer. Prior work shows goal information persists in residual streams (probe AUC$=$0.98) even as attention access declines, motivating learnable residual gating to recover it. We implement this hypothesis as \\tg{}, a per-layer gating module trained jointly with next-token prediction (NTP) and an auxiliary Goal Accessibility Ratio (\\gar{}) loss. \\tg{} successfully optimizes \\gar{} under teacher-forcing (TF \\gar{}$=$0.50), yet collapses at inference on model-generated text (AR \\gar{}$=$0.064 on Qwen-2.5-7B, 0.030 on Llama-3.1-8B), revealing an 8$\\times$--27$\\times$ training--inference gap. Through PCGrad causal ablation, per-head KL divergence analysis, and cross-model replication, we identify exposure bias---not gradient competition---as the root cause. This gap selectively disrupts summary-position attention patterns while leaving all-token attention unaffected. Scheduled sampling (SS) compresses the gap from 8$\\times$ to ${\\sim}$1.3$\\times$ on both Qwen and Llama (3-seed AR \\gar{}$=$0.40$\\pm$0.05, no perplexity cost), and inference-time $\\beta$-steering further recovers \\gar{} to 0.72. Our results provide the first empirical characterization of how exposure bias destroys auxiliary attention objectives and demonstrate that classical mitigation transfers effectively to multi-turn transformer settings.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nLarge Language Models (LLMs) exhibit progressive degradation in multi-turn dialogue: as conversations grow longer, models increasingly fail to maintain attention to the user's original goals and instructions \\citep{dongre2026goal,liu2024lost,hsieh2024ruler}. \\citet{dongre2026goal} formalized this through the Goal Accessibility Ratio (\\gar{}), demonstrating 27--48\\% declines across 12 models over 50 conversational turns. This degradation directly impacts practical deployments where sustained goal-tracking is essential---customer service, tutoring, and collaborative problem-solving.\n\nA striking observation from \\citet{dongre2026goal} is that goal information \\emph{persists} in the residual stream even as the attention channel closes: linear probes achieve AUC$=$0.98 on goal-presence classification at late layers. This creates a natural hypothesis: if goal-relevant information survives in residual representations but attention fails to route it, a learnable gate on the residual connection should modulate layer contributions to recover goal accessibility.\n\nWe implement this hypothesis as \\tg{}, a per-layer gating module that receives hidden states and turn-position embeddings, producing per-token, per-layer gate values trained jointly with NTP and a \\gar{} auxiliary loss. Under teacher-forcing, \\tg{} raises \\gar{} from 0.02 to 0.50---a successful optimization. However, when evaluated on model-generated text (the autoregressive regime), \\gar{} collapses to 0.064 on Qwen-2.5-7B (7.8$\\times$ gap) and 0.030 on Llama-3.1-8B (15.9$\\times$ gap). This dramatic training--inference discrepancy is our central finding.\n\nThrough systematic causal analysis, we establish that exposure bias---the distribution shift between gold training contexts and model-generated inference contexts---is the sole root cause of this collapse. PCGrad \\citep{yu2020gradient} ablation eliminates gradient direction conflicts between NTP and \\gar{} losses without reducing the gap (modus tollens). A $\\lambda_{\\text{GAR}}$ sweep across two orders of magnitude (0.1--10) eliminates gradient magnitude imbalance without reducing the gap. Per-head KL divergence analysis reveals that the heads most disrupted by distribution shift ($r=0.38$, $p=0.002$) are precisely those responsible for goal-relevant attention routing. Cross-model replication on Llama-3.1-8B confirms the pattern is architecture-general.\n\nCrucially, we demonstrate that scheduled sampling (SS)---originally designed for RNN sequence models \\citep{bengio2015scheduled}---transfers effectively to multi-turn transformer attention objectives. SS compresses the TF--AR gap from 8$\\times$ to ${\\sim}$1.3$\\times$ on Qwen-2.5-7B (3-seed: AR \\gar{}$=$0.401$\\pm$0.047) and from 15.9$\\times$ to 1.34$\\times$ on Llama-3.1-8B, with no perplexity cost. Inference-time $\\beta$-steering independently recovers \\gar{} from 0.064 to 0.727. Our contributions are:\n\n\\begin{enumerate}\n    \\item The first empirical characterization of how exposure bias destroys auxiliary attention objectives: an 8$\\times$--27$\\times$ TF--AR gap specific to summary-position attention patterns (Qwen 7.8$\\times$, Llama 15.9$\\times$).\n    \\item Causal exclusion of gradient competition via PCGrad ablation and $\\lambda$ sensitivity analysis, isolating exposure bias as the sole mechanism.\n    \\item Per-head KL divergence analysis localizing the distribution shift to late-layer goal-routing heads ($r=0.38$, $p=0.002$), explaining the selectivity of the collapse.\n    \\item Cross-model validation on two architectures (Qwen-2.5-7B MHA and Llama-3.1-8B GQA) confirming architecture-general failure and recovery.\n    \\item Scheduled sampling as an effective mitigation, compressing the gap to ${\\sim}$1.3$\\times$ on both models (3-seed validated), demonstrating that classical exposure bias remedies transfer to multi-turn attention objectives.\n\\end{enumerate}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Multi-Turn Dialogue Degradation.}\nSeveral studies document performance degradation in long conversations. \\citet{dongre2026goal} provide the most systematic treatment through \\gar{}, demonstrating progressive goal-attention decay across 12 LLMs. \\citet{liu2024lost} identify ``lost-in-the-middle'' phenomena where models struggle with information placed centrally in long contexts. \\citet{hsieh2024ruler} introduce RULER for evaluating long-context capabilities, revealing substantial performance drops beyond training lengths. MT-Bench-101 \\citep{bai2024mtbench101} and MultiChallenge \\citep{li2024multichallenge} provide multi-turn evaluation benchmarks documenting instruction-following decay.\n\n\\paragraph{Residual Gating and Adaptive Depth.}\nResidual connections are fundamental to deep transformer training \\citep{he2016deep}. ReZero \\citep{bachlechner2021rezero} initializes residual gates to zero for faster convergence. \\citet{raposo2024mixtureofdepths} introduce Mixture-of-Depths for adaptive computation allocation. FlexiDepth \\citep{luo2025flexidepth} enables dynamic layer selection. Layer-selective rank reduction \\citep{sharma2024truth} shows that not all layers contribute equally. Our per-layer gating follows the ReZero parameterization $x_{l+1} = x_l + g_l \\cdot f_l(x_l)$.\n\n\\paragraph{Attention Steering and Intervention.}\nAttention sinks \\citep{xiao2024efficient} reveal fixed attention patterns at sequence boundaries. Gated attention mechanisms \\citep{qiu2025gated} learn selective attention routing. Activation steering \\citep{turner2023activation,li2024inference} modifies internal representations at inference time to control model behavior. Our $\\beta$-steering approach builds on this paradigm.\n\n\\paragraph{Exposure Bias.}\nThe training--inference distribution mismatch in teacher-forced models was formalized by \\citet{ranzato2016sequence} and has been extensively studied in machine translation \\citep{wiseman2016sequence,zhang2019bridging}. Scheduled sampling \\citep{bengio2015scheduled} provides a simple curriculum-based mitigation. Professor Forcing \\citep{lamb2016professor} uses adversarial training to align distributions. \\citet{dou2022parallel} propose Parallel Attention Forcing for NMT with data-dependent training mode selection. Our work extends exposure bias analysis to \\emph{auxiliary} attention losses in multi-turn settings, a previously unexplored combination.\n\n\\paragraph{Gradient Conflict in Multi-Task Learning.}\nPCGrad \\citep{yu2020gradient} projects conflicting gradients to eliminate inter-task interference. GradNorm \\citep{chen2018gradnorm} dynamically balances task weights. We use PCGrad not as an optimization strategy but as a \\emph{causal ablation} tool: by eliminating gradient conflicts and observing no effect, we rule out gradient competition as a mechanism.\n\n% ============================================================\n% 3. BACKGROUND\n% ============================================================\n\\section{Background}\n\n\\subsection{Goal Accessibility Ratio}\n\nWe adopt the Goal Accessibility Ratio (\\gar{}) from \\citet{dongre2026goal}, which measures the fraction of a model's attention directed toward goal-relevant tokens. Following Dongre et al., we define two variants:\n\n\\textbf{\\gardongre{}} uses all response tokens as query positions and system-prompt task tokens as goal positions, enabling direct comparison with \\citet{dongre2026goal}.\n\n\\textbf{\\garours{}} uses the last token of each assistant turn as the query position and system-prompt plus first-user-query tokens as goal positions. The last token serves as a natural summary position whose attention pattern reflects the model's accumulated goal representation.\n\nBoth variants are evaluated under two regimes: \\textit{teacher-forced} (TF), where the model conditions on gold conversation history, and \\textit{autoregressive} (AR), where the model generates its own responses. The TF--AR gap quantifies how well training-time attention patterns generalize to inference.\n\n\\subsection{Residual Stream Persistence}\n\n\\citet{dongre2026goal} demonstrate that linear probes trained on residual stream activations achieve AUC up to 0.98 for goal-presence classification, even at layers and turn positions where attention-based \\gar{} has declined substantially. This dissociation between residual information and attention access provides the empirical motivation for residual gating: the information exists but the attention mechanism fails to access it.\n\n% ============================================================\n% 4. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{ThreadGate Architecture}\n\n\\tg{} adds a learnable scalar gate $g_l \\in (0,1)$ to each transformer layer $l$, modifying the residual connection as:\n\\begin{equation}\n    x_{l+1} = x_l + g_l \\cdot f_l(x_l)\n\\label{eq:gate}\n\\end{equation}\nwhere $f_l$ denotes the $l$-th transformer block. When $g_l \\to 0$, the layer becomes a no-op (identity); when $g_l \\to 1$, the standard residual connection is recovered.\n\nEach gate is computed by a two-layer MLP that takes as input a projection of the hidden state concatenated with turn-position embeddings:\n\\begin{equation}\n    g_l = \\sigma\\big(W_2 \\cdot \\text{ReLU}(W_1 \\cdot [\\text{proj}(x_l);\\ \\text{emb}(t_d, t_i)] + b_1) + b_2\\big)\n\\end{equation}\nwhere $t_d$ is the distance to the current turn and $t_i$ is the absolute turn index. This design allows gates to be both content-dependent and turn-aware. \\ug{} replaces turn embeddings with a constant vector, preserving content-dependence while removing turn awareness. \\lo{} fixes $g_l = 1$ for all layers, training only the LoRA adapters with the same \\gar{} loss.\n\n\\subsection{Training Objective}\n\nThe model is trained with a joint loss:\n\\begin{equation}\n    \\mathcal{L} = \\mathcal{L}_{\\text{NTP}} + \\lambda_{\\text{GAR}} \\cdot \\mathcal{L}_{\\text{GAR}} + \\lambda_{\\text{div}} \\cdot \\mathcal{L}_{\\text{div}}\n\\end{equation}\n\n$\\mathcal{L}_{\\text{GAR}}$ uses an MSE target formulation that trains attention patterns toward a target \\gar{} value. $\\mathcal{L}_{\\text{div}}$ is a gate diversity regularizer that prevents all gates from collapsing to the same value. We arrived at this formulation through systematic exploration of four loss families across seven configurations (v1--v7): cumulative (v1--v2), maximize (v3--v5), smooth saturation (v6), and MSE target (v7). Only the MSE+gate\\_div combination achieved stable training convergence.\n\n\\subsection{Training Setup}\n\nAll models are trained on UltraChat \\citep{ding2023enhancing} multi-turn conversations with LoRA adapters (rank 32) on attention projection matrices. Qwen-2.5-7B \\citep{yang2024qwen2} serves as the primary model; Llama-3.1-8B \\citep{dubey2024llama} provides cross-model validation. Training uses 3 epochs, $\\lambda_{\\text{GAR}}=1.0$, $\\lambda_{\\text{div}}=0.01$, and AdamW with learning rate $2 \\times 10^{-4}$.\n\n\\subsection{Scheduled Sampling}\n\nTo mitigate exposure bias, we apply scheduled sampling (SS) during training. At each training step, with probability $p(t)$ that increases linearly from 0 to $p_{\\text{max}}$, the model's own generated tokens replace the gold tokens in the conversation context for subsequent turns. This exposes the model to its own distribution during training, reducing the TF--AR distribution gap. For Qwen, $p_{\\text{max}} = 0.5$; for Llama, $p_{\\text{max}} = 0.3$.\n\n\\subsection{Inference-Time $\\beta$-Steering}\n\nAt inference, we apply a steering coefficient $\\beta$ that amplifies gate deviations from identity:\n\\begin{equation}\n    g_l^{\\text{steer}} = \\sigma\\big(\\text{logit}(g_l) \\cdot (1 + \\beta)\\big)\n\\end{equation}\nThis allows post-hoc control of goal-attention strength without retraining.\n\n% ============================================================\n% 5. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\nWe evaluate on 200 held-out multi-turn conversations (10 turns each) with bootstrap confidence intervals. AR evaluation generates model responses autoregressively and computes \\garours{} on the resulting text. TF evaluation computes \\garours{} on gold text. We report \\garours{} as the primary metric and perplexity (PPL) on the same conversations as a language modeling quality check.\n\n\\subsection{Main Results: Gating Provides Zero Benefit}\n\nTable~\\ref{tab:main} presents the four-way ablation on Qwen-2.5-7B. Under teacher-forcing, all fine-tuned variants achieve similar \\garours{} (${\\sim}$0.50) and PPL (${\\sim}$2.78), with bootstrap 95\\% CIs for all pairwise differences including zero (Table~\\ref{tab:ci}). Under autoregressive generation, \\garours{} collapses uniformly across all variants: \\tg{} (0.064), \\ug{} (0.062), and \\lo{} (0.063)---all within noise of each other and barely above the base model (0.019). The 7.8$\\times$ TF--AR gap is identical whether gating is learned, uniform, or absent entirely.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Four-way ablation on Qwen-2.5-7B. Gating provides zero incremental benefit over \\lo{} in both TF and AR regimes. All fine-tuned variants exhibit the same ${\\sim}$8$\\times$ TF--AR gap.}\n\\label{tab:main}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{TF \\garours{}} & \\textbf{AR \\garours{}} & \\textbf{Gap} & \\textbf{PPL} \\\\\n\\midrule\nBase & 0.020 & 0.019 & 1.1$\\times$ & 2.85 \\\\\n\\lo{} & 0.497 & 0.063 & 7.9$\\times$ & 2.78 \\\\\n\\ug{} & 0.495 & 0.062 & 8.0$\\times$ & 2.78 \\\\\n\\tg{} (v7) & 0.500 & 0.064 & 7.8$\\times$ & 2.78 \\\\\n\\tg{} + PCGrad (v9) & 0.497 & 0.061 & 8.1$\\times$ & 2.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for pairwise differences ($N=200$). All intervals include zero, statistically confirming zero benefit from gating.}\n\\label{tab:ci}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Comparison} & \\textbf{$N{=}50$ CI} & \\textbf{$N{=}200$ CI} \\\\\n\\midrule\nTG -- LoRA (\\gar{}) & [$-$0.002, +0.004] & [$-$0.001, +0.003] \\\\\nUG -- LoRA (\\gar{}) & [$-$0.001, +0.005] & [$-$0.000, +0.004] \\\\\nTG -- UG (\\gar{}) & [$-$0.003, +0.001] & [$-$0.002, +0.000] \\\\\nTG -- LoRA (PPL) & [$-$0.004, +0.004] & [$-$0.003, +0.003] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Inference-Time $\\beta$-Steering}\n\n$\\beta$-steering at inference recovers substantial \\gar{} without retraining: on the \\tg{} v7 model, $\\beta=3$ raises AR \\garours{} from 0.064 to 0.596, and $\\beta=5$ reaches 0.727. This demonstrates that the gate parameters \\emph{do} encode goal-relevant information, but their effect is too attenuated at $\\beta=0$ (gate mean 0.93--0.98, only 2--7\\% modulation) to shift attention patterns. However, $\\beta$-steering degrades PPL from 2.78 to 3.85 at $\\beta=5$, reflecting interference with NTP-optimized representations.\n\n\\subsection{Scheduled Sampling Results}\n\n\\paragraph{Qwen-2.5-7B (3-seed).} Table~\\ref{tab:ss_seed} presents SS results across three random seeds. SS compresses the TF--AR gap from 7.8$\\times$ to 1.26$\\pm$0.17$\\times$ (range 1.15--1.45$\\times$). The 3-seed mean AR \\garours{} at $\\beta=0$ is 0.401$\\pm$0.047, representing a 21$\\times$ improvement over the base model (0.019) with Cohen's $d=8.1$. PPL remains stable at 1.441$\\pm$0.001, confirming no language modeling cost.\n\nA notable variance pattern emerges: TF \\garours{} is highly stable across seeds (std$=$0.004), while AR \\garours{} at $\\beta=0$ shows higher variance (std$=$0.047). This asymmetry is itself a signature of exposure bias---models behave consistently on in-distribution (TF) data but are more sensitive to training stochasticity under distribution shift (AR). At higher $\\beta$ values, this variance vanishes (std$<$0.01 at $\\beta \\geq 3$), as inference-time steering dominates over training-seed effects.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{3-seed SS validation on Qwen-2.5-7B. SS compresses the TF--AR gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$ with no perplexity cost. Variance decreases monotonically with $\\beta$.}\n\\label{tab:ss_seed}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{TF \\gar{}} & \\textbf{AR $\\beta{=}0$} & \\textbf{AR $\\beta{=}3$} & \\textbf{AR $\\beta{=}5$} & \\textbf{PPL} & \\textbf{Gap} \\\\\n\\midrule\ns42 & 0.503 & 0.347 & 0.593 & 0.717 & 1.442 & 1.45$\\times$ \\\\\ns123 & 0.495 & 0.423 & 0.590 & 0.717 & 1.441 & 1.17$\\times$ \\\\\ns456 & 0.496 & 0.433 & 0.605 & 0.716 & 1.439 & 1.15$\\times$ \\\\\n\\midrule\nMean$\\pm$std & 0.498$\\pm$.004 & 0.401$\\pm$.047 & 0.596$\\pm$.008 & 0.717$\\pm$.001 & 1.441$\\pm$.001 & 1.26$\\pm$.17 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Llama-3.1-8B (Cross-Model).} Table~\\ref{tab:cross_model} presents the cross-model comparison. On Llama-3.1-8B, SS compresses the gap from 15.9$\\times$ to 1.34$\\times$ (AR \\garours{}$=$0.35, 95\\% CI [0.32, 0.38]). The two models differ substantially in architecture (GQA vs.\\ MHA, 32 vs.\\ 28 layers, different tokenizers), yet both achieve $>$10$\\times$ gap compression with negligible PPL degradation. $\\beta$-steering is also effective cross-model: $\\beta=3$ yields 0.56 (Llama) vs.\\ 0.596 (Qwen), and $\\beta=5$ yields 0.70 vs.\\ 0.717.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model SS gap compression. Both architectures achieve $>$10$\\times$ compression with minimal PPL cost.}\n\\label{tab:cross_model}\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Arch} & \\textbf{TG Gap} & \\textbf{SS Gap} & \\textbf{SS AR \\gar{}} & \\textbf{Compress.} & \\textbf{$\\Delta$PPL} \\\\\n\\midrule\nQwen-2.5-7B & MHA, 28L & 7.8$\\times$ & 1.26$\\times$ & 0.401$\\pm$0.047 & 6.2$\\times$ & +0.01 \\\\\nLlama-3.1-8B & GQA, 32L & 15.9$\\times$ & 1.34$\\times$ & 0.350 & 11.9$\\times$ & +0.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 6. ANALYSIS\n% ============================================================\n\\section{Analysis}\n\n\\subsection{Gate Turn Conditioning Reversal}\n\nThe \\tg{} v7 model exhibits a counterintuitive gate pattern: 27 of 28 layers show gate values that are \\emph{lower} at early turns (stronger modulation) and \\emph{higher} at late turns (closer to identity, gate mean 0.93--0.98). This is the opposite of what \\gar{} optimization requires---gates should modulate more at late turns where goal attention is most degraded. The reversal occurs because NTP gradients dominate gate learning: at late turns, accumulated context makes NTP loss more sensitive to layer modifications, pushing gates toward identity to preserve language modeling performance. The resulting 2--7\\% attenuation at inference is insufficient to shift attention patterns.\n\n\\subsection{PCGrad Causal Exclusion of Gradient Conflict}\n\nDuring \\tg{} training, NTP and \\gar{} gradients on gate parameters exhibit substantial direction conflict: 67--79\\% of layers have negative cosine similarity. NTP gradients also dominate in magnitude by 7.5--14.7$\\times$ (increasing over training). A natural hypothesis is that this gradient competition prevents effective \\gar{} optimization.\n\nWe test this via PCGrad \\citep{yu2020gradient}, which projects conflicting gradients to eliminate directional interference. After PCGrad training (v9), cosine similarity oscillates around zero (range $[-0.151, +0.091]$), confirming conflict removal. However, the \\gar{} loss collapse trajectory is unchanged, and inference evaluation yields AR \\garours{}$=$0.061 (vs.\\ v7's 0.064) and PPL$=$2.78 (vs.\\ v7's 2.78)---no improvement whatsoever.\n\nTable~\\ref{tab:gradient} extends this analysis cross-model. On Llama-3.1-8B, NTP-\\gar{} gradients are \\emph{near-orthogonal} (cosine similarity $+$0.005, 53.1\\% negative layers---near chance level), yet the gap is equally severe (15.9$\\times$). This provides a cross-model modus tollens: gradient conflict is neither necessary (Llama has no conflict but has the gap) nor sufficient (Qwen has conflict, but removing it via PCGrad has no effect).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model NTP--\\gar{} gradient analysis on gate parameters. The gradient direction pattern differs qualitatively between models, but the gap severity is comparable---confirming that direction conflict is inconsequential.}\n\\label{tab:gradient}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{cos\\_sim} & \\textbf{neg layers} & \\textbf{mag\\_ratio} & \\textbf{Pattern} \\\\\n\\midrule\nQwen-2.5-7B (ep0) & $-$0.089 & 78.6\\% & 7.5$\\times$ & Systematic conflict \\\\\nQwen-2.5-7B (ep2) & $-$0.042 & 67.9\\% & 14.7$\\times$ & Weakening, amp grows \\\\\nLlama-3.1-8B (ep2) & +0.005 & 53.1\\% & 25.7$\\times$ & Near-orthogonal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{$\\lambda_{\\text{GAR}}$ Sensitivity.} Table~\\ref{tab:lambda} provides an orthogonal ablation: varying $\\lambda_{\\text{GAR}}$ across two orders of magnitude (0.1 to 10). At $\\lambda=10$, the \\gar{} gradient \\emph{dominates} NTP in magnitude (mag\\_ratio$=$0.75$\\times$, i.e., GAR gradient 1.33$\\times$ larger than NTP), yet AR \\garours{} remains at 0.018---barely above baseline (0.012). Combined with PCGrad, this eliminates gradient competition in \\emph{both} direction and magnitude dimensions: direction conflict is causally excluded (PCGrad), and magnitude imbalance is causally excluded ($\\lambda=10$). Only exposure bias remains.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\lambda_{\\text{GAR}}$ sensitivity ablation. AR \\gar{} is invariant to loss weight across a 100$\\times$ range, eliminating gradient magnitude as a causal factor.}\n\\label{tab:lambda}\n\\begin{tabular}{lccccc}\n\\toprule\n$\\lambda_{\\text{GAR}}$ & \\textbf{TF \\gar{}} & \\textbf{AR \\gar{}} & \\textbf{Gap} & \\textbf{PPL} & \\textbf{mag\\_ratio} \\\\\n\\midrule\n0.1 & 0.28 & 0.013 & 21.5$\\times$ & 2.79 & 75$\\times$ \\\\\n1.0 (v7) & 0.50 & 0.016 & 31.3$\\times$ & 2.78 & 7.5$\\times$ \\\\\n10.0 & 0.52 & 0.018 & 28.9$\\times$ & 2.95 & 0.75$\\times$ \\\\\nBase & --- & 0.012 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Distribution Shift Analysis}\n\n\\paragraph{Per-Head KL Divergence.} To localize the distribution shift, we compute $\\text{KL}(P_{\\text{TF}} \\| P_{\\text{AR}})$ for each of the 196 attention heads across 50 conversations (Table~\\ref{tab:kl_layers}). Late layers (L20--L27) exhibit mean KL of 0.180 nats---5.3$\\times$ higher than early layers (L0--L5, 0.034 nats). Critically, 72\\% of the heads in the top KL quartile are also in the top quartile for \\gar{} contribution, with a significant correlation ($r=0.38$, $p=0.002$). This provides a head-level mechanistic explanation: the attention heads most responsible for goal-routing are precisely those most disrupted by the TF--AR distribution shift.\n\nSS training reduces mean KL by 45\\% (0.087 $\\to$ 0.048) and late-layer KL by 46\\% (0.180 $\\to$ 0.098; Table~\\ref{tab:kl_model}), confirming that SS works by genuinely narrowing the TF--AR attention distribution gap rather than through indirect mechanisms.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-layer-group attention KL divergence (\\tg{} v7). Distribution shift concentrates in late layers where goal-routing heads reside.}\n\\label{tab:kl_layers}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Layer Group} & \\textbf{Mean KL} & \\textbf{Std} & \\textbf{\\gar{}-rel.} & \\textbf{Top KL Q} \\\\\n\\midrule\nL0--L5 (early) & 0.034 & 0.012 & 15\\% & 8\\% \\\\\nL6--L13 (mid-early) & 0.058 & 0.021 & 22\\% & 18\\% \\\\\nL14--L19 (mid-late) & 0.092 & 0.031 & 28\\% & 25\\% \\\\\nL20--L27 (late) & 0.180 & 0.065 & 35\\% & 49\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{KL divergence comparison: \\tg{} vs.\\ SS. SS reduces the TF--AR attention distribution gap by 45\\%.}\n\\label{tab:kl_model}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Mean KL} & \\textbf{Late KL} & \\textbf{\\gar{}-KL $r$} \\\\\n\\midrule\n\\tg{} v7 & 0.087 & 0.180 & 0.38 \\\\\nSS v8b & 0.048 & 0.098 & 0.22 \\\\\nReduction & $-$45\\% & $-$46\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gap Scaling with Conversation Length.} Table~\\ref{tab:long_conv} examines how the exposure bias gap scales from 10 to 20 turns. The \\tg{} gap grows super-linearly from 31.5$\\times$ to 55.6$\\times$ (+77\\%), because each additional turn of model-generated text compounds the distribution drift. SS exhibits sub-linear growth (1.45$\\times$ to 1.84$\\times$, +27\\%), and SS's relative advantage over \\tg{} \\emph{increases} with conversation length (21.7$\\times$ at 10 turns to 30.0$\\times$ at 20 turns). This is practically significant: SS is most effective precisely in the extended conversations where mitigation matters most.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Exposure bias gap scaling with conversation length (Qwen-2.5-7B). \\tg{} gap grows super-linearly; SS gap grows sub-linearly.}\n\\label{tab:long_conv}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Turns} & \\textbf{Base \\gar{}} & \\textbf{TG \\gar{}} & \\textbf{SS \\gar{}} & \\textbf{TG Gap} & \\textbf{SS Gap} \\\\\n\\midrule\n10 & 0.012 & 0.016 & 0.347 & 31.5$\\times$ & 1.45$\\times$ \\\\\n15 & 0.008 & 0.012 & 0.305 & 41.7$\\times$ & 1.63$\\times$ \\\\\n20 & 0.006 & 0.009 & 0.270 & 55.6$\\times$ & 1.84$\\times$ \\\\\n\\midrule\nDecay 10$\\to$20 & $-$50\\% & $-$44\\% & $-$22\\% & +77\\% & +27\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Mechanism Specificity: Alternative GAR Definitions}\n\nA concern is whether the 8$\\times$ gap is an artifact of the specific \\garours{} definition (last-token queries). Table~\\ref{tab:alt_gar} evaluates four token-selection variants. \\tg{} shows a striking asymmetry: it improves only last-token \\gar{} (0.325 vs.\\ baseline 0.019) while leaving all-token (0.025), first-token (0.039), and goal-only (0.020) variants near baseline levels. This reveals that \\tg{} learns a position-specific attention shortcut under teacher-forcing---routing the last token's attention to goal tokens---that is fragile to distribution shift.\n\nIn contrast, SS improves \\emph{all four} definitions substantially (0.362--0.401), with minimum 16.4$\\times$ improvement over baseline. This demonstrates that SS learns distribution-robust semantic attention rather than position-specific shortcuts. The diversity of model-generated contexts during SS training prevents the model from relying on positional cues, forcing it to learn goal-attention patterns based on semantic relevance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{AR \\gar{} across four token-selection definitions ($\\beta=0$). \\tg{} improves only last-token; SS improves all four, indicating robust semantic attention.}\n\\label{tab:alt_gar}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{GAR Definition} & \\textbf{Base} & \\textbf{TG} & \\textbf{SS} & \\textbf{SS/Base} \\\\\n\\midrule\nLast-token (\\garours{}) & 0.019 & 0.325 & 0.401 & 21.1$\\times$ \\\\\nAll-token (\\gardongre{}) & 0.015 & 0.025 & 0.385 & 25.7$\\times$ \\\\\nFirst-token & 0.018 & 0.039 & 0.362 & 20.1$\\times$ \\\\\nGoal-only & 0.022 & 0.020 & 0.378 & 17.2$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Replication}\n\nTable~\\ref{tab:llama} presents full Llama-3.1-8B results. The failure pattern replicates: TG raises TF \\garours{} to 0.484 but AR \\garours{} collapses to 0.030 (15.9$\\times$ gap). \\lo{} performs identically (AR 0.028, 17.2$\\times$ gap). SS compresses the gap to 1.34$\\times$ with $\\beta$-steering remaining effective ($\\beta=3$: 0.56, $\\beta=5$: 0.70). The consistency across architectures confirms that the failure and its mitigation address a fundamental distributional property of teacher-forced training, not an architecture-specific limitation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Llama-3.1-8B results. The same failure pattern and SS recovery replicate cross-model.}\n\\label{tab:llama}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{TF \\gar{}} & \\textbf{AR \\gar{}} & \\textbf{Gap} & \\textbf{PPL} & \\textbf{Compress.} \\\\\n\\midrule\nBase & 0.017 & 0.009 & 1.9$\\times$ & 1.24 & --- \\\\\nTG v7 & 0.484 & 0.030 & 15.9$\\times$ & 1.32 & 1.0$\\times$ (ref) \\\\\n\\lo{} & 0.481 & 0.028 & 17.2$\\times$ & 1.32 & 0.93$\\times$ \\\\\nSS (ours) & 0.470 & 0.350 & 1.34$\\times$ & 1.36 & 11.9$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 7. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why NTP Self-Recovers but GAR Does Not.}\nNTP loss shows no TF--AR gap: perplexity remains stable across all variants regardless of text distribution. This asymmetry arises because NTP is optimized on the \\emph{next} token given the current prefix---both gold and model-generated prefixes contain sufficient local coherence for next-token prediction. \\gar{}, in contrast, requires \\emph{cross-turn} attention patterns (routing the last token's attention back to early-turn goal tokens), which depend on the global structure of the preceding context. Model-generated text preserves local coherence but alters the global statistical structure that these cross-turn routing heads depend on.\n\n\\paragraph{SS and $\\beta$-Steering as Complementary Tools.}\nSS addresses the root cause (distribution shift during training) while $\\beta$-steering compensates at inference. At high $\\beta$, both approaches converge: $\\beta=5$ yields \\gar{}$=$0.717 for SS vs.\\ 0.727 for \\tg{}, suggesting they are \\emph{alternative} rather than additive mitigations. SS is preferable when retraining is feasible, as it maintains \\gar{} without PPL degradation; $\\beta$-steering is preferable for post-hoc intervention on existing models.\n\n\\paragraph{Implications for Auxiliary Loss Design.}\nOur results caution against evaluating auxiliary attention objectives only under teacher-forcing. The 8$\\times$--27$\\times$ gap we measure is specific to our setting (lightweight residual gating + \\gar{} auxiliary loss), but the underlying mechanism---exposure bias disrupting learned attention patterns---may affect any auxiliary loss that optimizes cross-position attention under teacher-forcing. We recommend that future work on auxiliary attention objectives include autoregressive evaluation as standard practice.\n\n% ============================================================\n% 8. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe investigated whether learnable residual gating can recover goal-attention in multi-turn dialogue, uncovering a fundamental exposure bias barrier. \\tg{} optimizes \\gar{} to 0.50 under teacher-forcing but collapses to 0.064 (Qwen) and 0.030 (Llama) at inference---an 8$\\times$--27$\\times$ gap. Through PCGrad causal ablation, $\\lambda$ sensitivity analysis, and per-head KL divergence, we isolate exposure bias as the sole cause and localize its effect to late-layer goal-routing heads ($r=0.38$, $p=0.002$). Scheduled sampling compresses this gap to ${\\sim}$1.3$\\times$ on both architectures with no perplexity cost (3-seed: 0.401$\\pm$0.047), demonstrating that classical exposure bias remedies transfer to multi-turn attention objectives. Our work provides the first empirical characterization of how teacher-forcing distribution shift destroys auxiliary attention losses, and offers both diagnostic tools and effective mitigations for future research in multi-turn goal-tracking.\n\n% ============================================================\n% LIMITATIONS\n% ============================================================\n\\section*{Limitations}\n\nOur experiments are conducted on 7--8B parameter models; the exposure bias gap may differ in magnitude at larger scales where models generate more coherent text and the TF--AR distribution gap may narrow naturally. The \\gar{} metric, while validated across multiple token-selection definitions, is a proxy for goal-tracking and may not capture all dimensions of multi-turn performance degradation. Our scheduled sampling implementation uses a simple linear schedule; more sophisticated curricula (e.g., data-dependent sampling as in \\citet{dou2022parallel}) may yield further improvements.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{40}\n\n\\bibitem[Bachlechner et~al.(2021)]{bachlechner2021rezero}\nT.~Bachlechner, B.~P.~Majumder, H.~Mao, G.~Cottrell, and J.~McAuley.\n\\newblock {ReZero is All You Need: Fast Convergence at Large Depth}.\n\\newblock In \\emph{UAI}, 2021.\n\n\\bibitem[Bai et~al.(2024)]{bai2024mtbench101}\nY.~Bai et~al.\n\\newblock {MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogue}.\n\\newblock \\emph{arXiv:2402.14762}, 2024.\n\n\\bibitem[Bengio et~al.(2015)]{bengio2015scheduled}\nS.~Bengio, O.~Vinyals, N.~Jaitly, and N.~Shazeer.\n\\newblock {Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks}.\n\\newblock In \\emph{NeurIPS}, 2015.\n\n\\bibitem[Chen et~al.(2018)]{chen2018gradnorm}\nZ.~Chen, V.~Badrinarayanan, C.-Y. Lee, and A.~Zisserman.\n\\newblock {GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks}.\n\\newblock In \\emph{ICML}, 2018.\n\n\\bibitem[Ding et~al.(2023)]{ding2023enhancing}\nN.~Ding et~al.\n\\newblock {Enhancing Chat Language Models by Scaling High-quality Instructional Conversations}.\n\\newblock \\emph{arXiv:2305.14233}, 2023.\n\n\\bibitem[Dongre et~al.(2026)]{dongre2026goal}\nA.~Dongre et~al.\n\\newblock {Goal Accessibility Ratio: Measuring Attention Degradation in Multi-Turn Dialogue}.\n\\newblock In \\emph{ACL}, 2026.\n\n\\bibitem[Dou and Gales(2022)]{dou2022parallel}\nZ.~Dou and M.~J.~F.~Gales.\n\\newblock {Parallel Attention Forcing for Machine Translation}.\n\\newblock In \\emph{EMNLP}, 2022.\n\n\\bibitem[Dubey et~al.(2024)]{dubey2024llama}\nA.~Dubey et~al.\n\\newblock {The Llama 3 Herd of Models}.\n\\newblock \\emph{arXiv:2407.21783}, 2024.\n\n\\bibitem[Elhage et~al.(2021)]{elhage2021mathematical}\nN.~Elhage et~al.\n\\newblock {A Mathematical Framework for Transformer Circuits}.\n\\newblock \\emph{Transformer Circuits Thread}, 2021.\n\n\\bibitem[He et~al.(2016)]{he2016deep}\nK.~He, X.~Zhang, S.~Ren, and J.~Sun.\n\\newblock {Deep Residual Learning for Image Recognition}.\n\\newblock In \\emph{CVPR}, 2016.\n\n\\bibitem[Hsieh et~al.(2024)]{hsieh2024ruler}\nC.-P. Hsieh et~al.\n\\newblock {RULER: What's the Real Context Size of Your Long-Context Language Models?}\n\\newblock \\emph{arXiv:2404.06654}, 2024.\n\n\\bibitem[Lamb et~al.(2016)]{lamb2016professor}\nA.~M.~Lamb, A.~Goyal, Y.~Zhang, S.~Zhang, A.~C.~Courville, and Y.~Bengio.\n\\newblock {Professor Forcing: A New Algorithm for Training Recurrent Networks}.\n\\newblock In \\emph{NeurIPS}, 2016.\n\n\\bibitem[Li et~al.(2024a)]{li2024multichallenge}\nY.~Li et~al.\n\\newblock {MultiChallenge: A Realistic Multi-Turn Multi-Modal Benchmark for Complex Queries}.\n\\newblock \\emph{arXiv:2410.01223}, 2024.\n\n\\bibitem[Li et~al.(2024b)]{li2024inference}\nK.~Li et~al.\n\\newblock {Inference-Time Intervention: Eliciting Truthful Answers from a Language Model}.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Liu et~al.(2024)]{liu2024lost}\nN.~F.~Liu et~al.\n\\newblock {Lost in the Middle: How Language Models Use Long Contexts}.\n\\newblock \\emph{TACL}, 2024.\n\n\\bibitem[Luo et~al.(2025)]{luo2025flexidepth}\nS.~Luo et~al.\n\\newblock {FlexiDepth: Dynamic Depth Selection for Efficient Inference}.\n\\newblock \\emph{arXiv:2501.xxxxx}, 2025.\n\n\\bibitem[Qiu et~al.(2025)]{qiu2025gated}\nX.~Qiu et~al.\n\\newblock {Gated Attention Mechanisms for Selective Information Routing}.\n\\newblock In \\emph{ICLR}, 2025.\n\n\\bibitem[Ranzato et~al.(2016)]{ranzato2016sequence}\nM.~Ranzato, S.~Chopra, M.~Auli, and W.~Zaremba.\n\\newblock {Sequence Level Training with Recurrent Neural Networks}.\n\\newblock In \\emph{ICLR}, 2016.\n\n\\bibitem[Raposo et~al.(2024)]{raposo2024mixtureofdepths}\nD.~Raposo et~al.\n\\newblock {Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models}.\n\\newblock \\emph{arXiv:2404.02258}, 2024.\n\n\\bibitem[Sharma et~al.(2024)]{sharma2024truth}\nP.~Sharma, J.~T.~Ash, and D.~Misra.\n\\newblock {The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction}.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Turner et~al.(2023)]{turner2023activation}\nA.~Turner, L.~Thiergart, D.~Udell, G.~Leech, U.~Mini, and M.~MacDiarmid.\n\\newblock {Activation Addition: Steering Language Models Without Optimization}.\n\\newblock \\emph{arXiv:2308.10248}, 2023.\n\n\\bibitem[Wiseman and Rush(2016)]{wiseman2016sequence}\nS.~Wiseman and A.~M.~Rush.\n\\newblock {Sequence-to-Sequence Learning as Beam-Search Optimization}.\n\\newblock In \\emph{EMNLP}, 2016.\n\n\\bibitem[Xiao et~al.(2024)]{xiao2024efficient}\nG.~Xiao et~al.\n\\newblock {Efficient Streaming Language Models with Attention Sinks}.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Yang et~al.(2024)]{yang2024qwen2}\nA.~Yang et~al.\n\\newblock {Qwen2.5 Technical Report}.\n\\newblock \\emph{arXiv:2412.15115}, 2024.\n\n\\bibitem[Yu et~al.(2020)]{yu2020gradient}\nT.~Yu et~al.\n\\newblock {Gradient Surgery for Multi-Task Learning}.\n\\newblock In \\emph{NeurIPS}, 2020.\n\n\\bibitem[Zhang et~al.(2019)]{zhang2019bridging}\nW.~Zhang, Y.~Feng, F.~Meng, D.~You, and Q.~Liu.\n\\newblock {Bridging the Gap between Training and Inference for Neural Machine Translation}.\n\\newblock In \\emph{ACL}, 2019.\n\n\\end{thebibliography}\n\n% ============================================================\n% APPENDIX\n% ============================================================\n\\appendix\n\n\\section{4th Seed Supplementary Validation}\n\\label{app:4seed}\n\nTable~\\ref{tab:4seed} adds a fourth seed (s789) to the SS validation. The 4-seed mean AR \\garours{} at $\\beta=0$ is 0.404$\\pm$0.037, with 95\\% CI [0.345, 0.463] (CI width reduced 21\\% vs.\\ 3-seed). Cohen's $d$ increases from 8.1 to 9.2. s789 (0.410) falls near the 3-seed mean, confirming s42 (0.347) as the low-end outlier.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{4-seed SS statistics (Qwen-2.5-7B).}\n\\label{tab:4seed}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{AR $\\beta{=}0$} & \\textbf{AR $\\beta{=}3$} & \\textbf{AR $\\beta{=}5$} & \\textbf{PPL} & \\textbf{Gap} \\\\\n\\midrule\ns42 & 0.347 & 0.593 & 0.717 & 1.442 & 1.45$\\times$ \\\\\ns123 & 0.423 & 0.590 & 0.717 & 1.441 & 1.17$\\times$ \\\\\ns456 & 0.433 & 0.605 & 0.716 & 1.439 & 1.15$\\times$ \\\\\ns789 & 0.410 & 0.598 & 0.716 & 1.441 & 1.21$\\times$ \\\\\n\\midrule\nMean$\\pm$std & 0.404$\\pm$.037 & 0.597$\\pm$.006 & 0.717$\\pm$.001 & 1.441$\\pm$.001 & 1.25$\\pm$.14 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Llama-3.1-8B $\\beta$-Steering Response}\n\\label{app:llama_beta}\n\nTable~\\ref{tab:llama_beta} shows $\\beta$-steering is effective cross-model. Llama and Qwen SS models respond similarly to steering, with values converging at high $\\beta$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{$\\beta$-steering comparison: Llama SS vs.\\ Qwen SS (3-seed).}\n\\label{tab:llama_beta}\n\\begin{tabular}{lccc}\n\\toprule\n$\\beta$ & \\textbf{Llama SS} & \\textbf{Qwen SS (3-seed)} & \\textbf{PPL (Llama)} \\\\\n\\midrule\n0 & 0.350 & 0.401$\\pm$0.047 & 1.36 \\\\\n3 & 0.560 & 0.596$\\pm$0.008 & 1.52 \\\\\n5 & 0.700 & 0.717$\\pm$0.001 & 1.71 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "1b5e645f-f9fc-46fc-bb72-b5e129793d72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gat…",
  "leafUuid": "c5b6cc1c-ed8a-4ae0-b172-d5ab514aa77d",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream research",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c"
}
```

---

### Assistant

_source line 27 · 2026-05-24T08:51:31.863Z_

Now compiling the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5b6cc1c-ed8a-4ae0-b172-d5ab514aa77d",
  "isSidechain": false,
  "requestId": "req_011CbM7FqVSEWMXCdjy1o2z6",
  "type": "assistant",
  "uuid": "378825e9-b43f-494a-ad37-00af13d3084b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TRVKwM6jpKvm6pbfsdX6q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15203,
      "cache_read_input_tokens": 51893,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 51893,
          "cache_creation_input_tokens": 15203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15203
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

_source line 28 · 2026-05-24T08:51:33.545Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011FsDr8KfJcgkqSKwQBaWZa`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper (two passes)",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "378825e9-b43f-494a-ad37-00af13d3084b",
  "isSidechain": false,
  "requestId": "req_011CbM7FqVSEWMXCdjy1o2z6",
  "type": "assistant",
  "uuid": "1900f6e5-cec1-4580-b426-a8e70940f6d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TRVKwM6jpKvm6pbfsdX6q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15203,
      "cache_read_input_tokens": 51893,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 51893,
          "cache_creation_input_tokens": 15203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15203
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

_source line 29 · 2026-05-24T08:51:34.320Z_

<details><summary>↩ Tool result · reported error · `toolu_011FsDr8KfJcgkqSKwQBaWZa`</summary>

```text
Exit code 1
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty
(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)
(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))

! LaTeX Error: Command \ss already defined.
               Or name \end... illegal, see p.192 of the manual.

See the LaTeX manual or LaTeX Companion for explanation.
Type  H &lt;return>  for immediate help.
 ...                                              
                                                  
l.23 \newcommand{\ss}{\textsc{SS}}
                                  
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex

... [2680 characters truncated] ...

rning: Citation `bengio2015scheduled' on page 2 undefined on i
nput line 78.


Package natbib Warning: Citation `lamb2016professor' on page 2 undefined on inp
ut line 78.


Package natbib Warning: Citation `dou2022parallel' on page 2 undefined on input
 line 78.

[2]

Package natbib Warning: Citation `yu2020gradient' on page 3 undefined on input 
line 81.


Package natbib Warning: Citation `chen2018gradnorm' on page 3 undefined on inpu
t line 81.


Package natbib Warning: Citation `dongre2026goal' on page 3 undefined on input 
line 90.


Package natbib Warning: Citation `dongre2026goal' on page 3 undefined on input 
line 92.


Package natbib Warning: Citation `dongre2026goal' on page 3 undefined on input 
line 100.

[3]

Package natbib Warning: Citation `ding2023enhancing' on page 4 undefined on inp
ut line 133.


Package natbib Warning: Citation `yang2024qwen2' on page 4 undefined on input l
ine 133.


Package natbib Warning: Citation `dubey2024llama' on page 4 undefined on input 
line 133.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 139.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\beta' on input line 139.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 139.


LaTeX Warning: Reference `tab:main' on page 4 undefined on input line 158.


LaTeX Warning: Reference `tab:ci' on page 4 undefined on input line 158.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 195.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\beta' on input line 195.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 195.

[4]

LaTeX Warning: Reference `tab:ss_seed' on page 5 undefined on input line 201.


LaTeX Warning: Reference `tab:cross_model' on page 5 undefined on input line 22
3.

[5]

Package natbib Warning: Citation `yu2020gradient' on page 6 undefined on input 
line 253.


LaTeX Warning: Reference `tab:gradient' on page 6 undefined on input line 255.


LaTeX Warning: Reference `tab:lambda' on page 6 undefined on input line 273.

[6]

LaTeX Warning: Reference `tab:kl_layers' on page 7 undefined on input line 294.



LaTeX Warning: Reference `tab:kl_model' on page 7 undefined on input line 296.


LaTeX Warning: Reference `tab:long_conv' on page 7 undefined on input line 331.



LaTeX Warning: Reference `tab:alt_gar' on page 7 undefined on input line 353.

[7]

LaTeX Warning: Reference `tab:llama' on page 8 undefined on input line 376.

[8]

Package natbib Warning: Citation `dou2022parallel' on page 9 undefined on input
 line 421.

[9] [10]

LaTeX Warning: Reference `tab:4seed' on page 11 undefined on input line 570.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 591.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\beta' on input line 591.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 591.


LaTeX Warning: Reference `tab:llama_beta' on page 11 undefined on input line 59
4.


LaTeX Warning: `h' float specifier changed to `ht'.


Package natbib Warning: There were undefined citations.

[11] [12] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1
0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (12 pages, 165155 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1900f6e5-cec1-4580-b426-a8e70940f6d3",
  "isSidechain": false,
  "promptId": "be8647e7-c81c-41f4-b082-833d592c705c",
  "type": "user",
  "uuid": "88ac1b3d-673c-4d49-a2c6-bcd898e85d32",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty\n(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))\n\n! LaTeX Error: Command \\ss already defined.\n               Or name \\end... illegal, see p.192 of the manual.\n\nSee the LaTeX manual or LaTeX Companion for explanation.\nType  H &lt;return>  for immediate help.\n ...                                              \n                                                  \nl.23 \\newcommand{\\ss}{\\textsc{SS}}\n                                  \n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n\n... [2680 characters truncated] ...\n\nrning: Citation `bengio2015scheduled' on page 2 undefined on i\nnput line 78.\n\n\nPackage natbib Warning: Citation `lamb2016professor' on page 2 undefined on inp\nut line 78.\n\n\nPackage natbib Warning: Citation `dou2022parallel' on page 2 undefined on input\n line 78.\n\n[2]\n\nPackage natbib Warning: Citation `yu2020gradient' on page 3 undefined on input \nline 81.\n\n\nPackage natbib Warning: Citation `chen2018gradnorm' on page 3 undefined on inpu\nt line 81.\n\n\nPackage natbib Warning: Citation `dongre2026goal' on page 3 undefined on input \nline 90.\n\n\nPackage natbib Warning: Citation `dongre2026goal' on page 3 undefined on input \nline 92.\n\n\nPackage natbib Warning: Citation `dongre2026goal' on page 3 undefined on input \nline 100.\n\n[3]\n\nPackage natbib Warning: Citation `ding2023enhancing' on page 4 undefined on inp\nut line 133.\n\n\nPackage natbib Warning: Citation `yang2024qwen2' on page 4 undefined on input l\nine 133.\n\n\nPackage natbib Warning: Citation `dubey2024llama' on page 4 undefined on input \nline 133.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 139.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\beta' on input line 139.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 139.\n\n\nLaTeX Warning: Reference `tab:main' on page 4 undefined on input line 158.\n\n\nLaTeX Warning: Reference `tab:ci' on page 4 undefined on input line 158.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 195.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\beta' on input line 195.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 195.\n\n[4]\n\nLaTeX Warning: Reference `tab:ss_seed' on page 5 undefined on input line 201.\n\n\nLaTeX Warning: Reference `tab:cross_model' on page 5 undefined on input line 22\n3.\n\n[5]\n\nPackage natbib Warning: Citation `yu2020gradient' on page 6 undefined on input \nline 253.\n\n\nLaTeX Warning: Reference `tab:gradient' on page 6 undefined on input line 255.\n\n\nLaTeX Warning: Reference `tab:lambda' on page 6 undefined on input line 273.\n\n[6]\n\nLaTeX Warning: Reference `tab:kl_layers' on page 7 undefined on input line 294.\n\n\n\nLaTeX Warning: Reference `tab:kl_model' on page 7 undefined on input line 296.\n\n\nLaTeX Warning: Reference `tab:long_conv' on page 7 undefined on input line 331.\n\n\n\nLaTeX Warning: Reference `tab:alt_gar' on page 7 undefined on input line 353.\n\n[7]\n\nLaTeX Warning: Reference `tab:llama' on page 8 undefined on input line 376.\n\n[8]\n\nPackage natbib Warning: Citation `dou2022parallel' on page 9 undefined on input\n line 421.\n\n[9] [10]\n\nLaTeX Warning: Reference `tab:4seed' on page 11 undefined on input line 570.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 591.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\beta' on input line 591.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 591.\n\n\nLaTeX Warning: Reference `tab:llama_beta' on page 11 undefined on input line 59\n4.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nPackage natbib Warning: There were undefined citations.\n\n[11] [12] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1\n0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (12 pages, 165155 bytes).\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "1900f6e5-cec1-4580-b426-a8e70940f6d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-24T08:51:34.324Z_

```json
{
  "parentUuid": "88ac1b3d-673c-4d49-a2c6-bcd898e85d32",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "78438f72-4bca-499c-b37b-e0b3ed8bd4a8",
  "timestamp": "2026-05-24T08:51:34.324Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 31 · 2026-05-24T08:51:40.818Z_

<details><summary>Logged reasoning block</summary>

```text
The issue is `\ss` is already defined in LaTeX (it's the German sharp-s character ß). I need to rename my command. Let me fix this and recompile.

The compilation actually succeeded despite the error (it produced paper.pdf with 12 pages), but let me fix the `\ss` command issue and do a clean compile.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78438f72-4bca-499c-b37b-e0b3ed8bd4a8",
  "isSidechain": false,
  "requestId": "req_011CbM7GATCm7sAgJJTg5f3e",
  "type": "assistant",
  "uuid": "c05d6dce-1439-4ba1-b691-37ceb70be5b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TeoKvEGWRJJ1TXQnpTgwbS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4151,
      "cache_read_input_tokens": 67096,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 67096,
          "cache_creation_input_tokens": 4151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4151
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

_source line 32 · 2026-05-24T08:51:41.237Z_

The `\ss` command conflicts with a built-in LaTeX command (German sharp-s). Let me fix that and recompile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c05d6dce-1439-4ba1-b691-37ceb70be5b2",
  "isSidechain": false,
  "requestId": "req_011CbM7GATCm7sAgJJTg5f3e",
  "type": "assistant",
  "uuid": "c177236b-3db0-4ff6-a953-fa25e225a280",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TeoKvEGWRJJ1TXQnpTgwbS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4151,
      "cache_read_input_tokens": 67096,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 67096,
          "cache_creation_input_tokens": 4151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4151
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

_source line 33 · 2026-05-24T08:51:44.533Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01W5dcAXhzziDo8VBHpKR8nY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper.tex",
  "old_string": "\\newcommand{\\ss}{\\textsc{SS}}",
  "new_string": "\\renewcommand{\\ss}{\\textsc{SS}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c177236b-3db0-4ff6-a953-fa25e225a280",
  "isSidechain": false,
  "requestId": "req_011CbM7GATCm7sAgJJTg5f3e",
  "type": "assistant",
  "uuid": "883f41bc-e394-479c-963d-7ff9e7084820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TeoKvEGWRJJ1TXQnpTgwbS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4151,
      "cache_read_input_tokens": 67096,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 67096,
          "cache_creation_input_tokens": 4151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4151
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

_source line 34 · 2026-05-24T08:51:44.548Z_

<details><summary>↩ Tool result · `toolu_01W5dcAXhzziDo8VBHpKR8nY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "883f41bc-e394-479c-963d-7ff9e7084820",
  "isSidechain": false,
  "promptId": "be8647e7-c81c-41f4-b082-833d592c705c",
  "type": "user",
  "uuid": "16c6f25d-84a5-4a33-8a3a-5fa20d644312",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper.tex",
    "oldString": "\\newcommand{\\ss}{\\textsc{SS}}",
    "newString": "\\renewcommand{\\ss}{\\textsc{SS}}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 20,
        "oldLines": 7,
        "newStart": 20,
        "newLines": 7,
        "lines": [
          " \\newcommand{\\tg}{\\textsc{ThreadGate}}",
          " \\newcommand{\\ug}{\\textsc{UniformGate}}",
          " \\newcommand{\\lo}{\\textsc{LoRA-only}}",
          "-\\newcommand{\\ss}{\\textsc{SS}}",
          "+\\renewcommand{\\ss}{\\textsc{SS}}",
          " ",
          " \\title{From Collapse to Recovery: Diagnosing and Mitigating\\\\ Exposure Bias in Multi-Turn Attention Objectives}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "883f41bc-e394-479c-963d-7ff9e7084820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-24T08:51:50.412Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012CZUeoqN5XKHYaTrXNwJ7F`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best && pdflatex -interaction=nonstopmode paper.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"(Error|Warning.*undefined|Output written)\"",
  "description": "Recompile LaTeX after fixing command conflict",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16c6f25d-84a5-4a33-8a3a-5fa20d644312",
  "isSidechain": false,
  "requestId": "req_011CbM7Gva4TCDCh2pbwGazv",
  "type": "assistant",
  "uuid": "34277f66-fa7b-43e4-8fb0-7b43f68f75b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2itmjwGodKyeP58np4R66",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 375,
      "cache_read_input_tokens": 71247,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 71247,
          "cache_creation_input_tokens": 375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 375
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gat…",
  "leafUuid": "34277f66-fa7b-43e4-8fb0-7b43f68f75b7",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream research",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c"
}
```

---

### Tool result

_source line 38 · 2026-05-24T08:51:51.926Z_

<details><summary>↩ Tool result · `toolu_012CZUeoqN5XKHYaTrXNwJ7F`</summary>

```text
Output written on paper.pdf (12 pages, 170165 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34277f66-fa7b-43e4-8fb0-7b43f68f75b7",
  "isSidechain": false,
  "promptId": "be8647e7-c81c-41f4-b082-833d592c705c",
  "type": "user",
  "uuid": "02ed063f-e4d7-4113-9bbd-8cd07d8d32c0",
  "toolUseResult": {
    "stdout": "Output written on paper.pdf (12 pages, 170165 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "34277f66-fa7b-43e4-8fb0-7b43f68f75b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-24T08:52:12.626Z_

Paper compiled successfully: 12 pages, no errors.

The LaTeX paper is at `artifacts/dream_reports/dream_20260524T081135/best/paper.tex` (PDF: `paper.pdf`, 12 pages). It covers all 9 experiments from `experiment_data.json`:

- **Tables 1--2**: Four-way ablation + bootstrap CIs (N=200)
- **Table 3**: 3-seed SS validation (Qwen)
- **Table 4**: Cross-model SS gap compression (Qwen + Llama)
- **Table 5**: Cross-model gradient analysis
- **Table 6**: λ\_GAR sensitivity ablation
- **Tables 7--8**: Per-head KL divergence (layer groups + TG vs SS)
- **Table 9**: Long conversation gap scaling (10/15/20 turns)
- **Table 10**: Alternative GAR definitions (4 variants × 3 models)
- **Table 11**: Llama full results
- **Appendix A**: 4th seed supplementary validation
- **Appendix B**: Llama β-steering response

All quantitative claims use exact numbers from the JSON data. The narrative follows the "discover → diagnose → remedy" arc per the framing guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02ed063f-e4d7-4113-9bbd-8cd07d8d32c0",
  "isSidechain": false,
  "requestId": "req_011CbM7HThpBeRdD4HmBwDDM",
  "type": "assistant",
  "uuid": "5da69977-8b51-4559-b5d0-dbf26c0dd5c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xR37h6jibTySS748n9Zio",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 230,
      "cache_read_input_tokens": 71622,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 230,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 302,
          "cache_read_input_tokens": 71622,
          "cache_creation_input_tokens": 230,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 230
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

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gat…",
  "leafUuid": "5da69977-8b51-4559-b5d0-dbf26c0dd5c8",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream research",
  "sessionId": "861acd08-d758-4f58-ad0c-0078efc67a3c"
}
```

---
