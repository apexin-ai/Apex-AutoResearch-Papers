# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T145320 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/9c898946-3fb8-4cb9-82ea-49687eee3396.jsonl`
- **Structured JSON:** [`1d2063d7c368fca41f28.json`](../../sessions/1d/1d2063d7c368fca41f28.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T15:13:37.956Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T15:13:37.956Z",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T145320 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Llama-3 复现失败趋势但幅度显著弱于 Qwen：base GAR 衰减仅 ~40%（vs Qwen 70.8%）， 训练-推理 gap ~10x（vs Qwen 30x），TG 与 LoRA-only 差异 1-3pp（vs Qwen <0.6pp）。 梯度冲突方向一致但 pattern 不完全干净（部分层 cos_sim 正值）。 Mitigation（scheduled sampling）将 gap 从 10x 缩小到 ~6x，统计上 marginal（p≈0.07）， bootstrap CI 宽且包含 0。整体叙事：Qwen 上的强定量证据 + Llama 上的方向一致性， mitigation 降级为 discussion 中的 suggestive evidence。C5 从\"普遍性\"弱化为 \"方向一致性，幅度与架构相关\"。标题考虑删除 'Cannot'，改为 'Struggles to' 或类似措辞。 投 EMNLP Findings 是合理目标。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T15:13:37.959Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T15:13:37.959Z",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-19T15:13:37.980Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T145320 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Llama-3 复现失败趋势但幅度显著弱于 Qwen：base GAR 衰减仅 ~40%（vs Qwen 70.8%）， 训练-推理 gap ~10x（vs Qwen 30x），TG 与 LoRA-only 差异 1-3pp（vs Qwen <0.6pp）。 梯度冲突方向一致但 pattern 不完全干净（部分层 cos_sim 正值）。 Mitigation（scheduled sampling）将 gap 从 10x 缩小到 ~6x，统计上 marginal（p≈0.07）， bootstrap CI 宽且包含 0。整体叙事：Qwen 上的强定量证据 + Llama 上的方向一致性， mitigation 降级为 discussion 中的 suggestive evidence。C5 从"普遍性"弱化为 "方向一致性，幅度与架构相关"。标题考虑删除 'Cannot'，改为 'Struggles to' 或类似措辞。 投 EMNLP Findings 是合理目标。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "60b11cf6-cc2f-4f15-8815-d9e57690cbb7",
  "type": "user",
  "uuid": "5260bb91-60b7-42dd-919f-a5a53efc9cde",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T15:13:37.979Z_

```json
{
  "parentUuid": "5260bb91-60b7-42dd-919f-a5a53efc9cde",
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
  "uuid": "bf1acb1a-e584-4ef4-8421-807465cc56dc",
  "timestamp": "2026-05-19T15:13:37.979Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T15:13:37.979Z_

```json
{
  "parentUuid": "bf1acb1a-e584-4ef4-8421-807465cc56dc",
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
  "uuid": "562562f4-15f4-4d1d-be0b-380d43af914d",
  "timestamp": "2026-05-19T15:13:37.979Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-19T15:13:37.979Z_

```json
{
  "parentUuid": "562562f4-15f4-4d1d-be0b-380d43af914d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2e39e1ff-d78b-4e1c-9561-fa5f5f717431",
  "timestamp": "2026-05-19T15:13:37.979Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
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
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396"
}
```

---

### Assistant

_source line 8 · 2026-05-19T15:13:46.952Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e39e1ff-d78b-4e1c-9561-fa5f5f717431",
  "isSidechain": false,
  "requestId": "req_011CbC9MPVNEHm7snJh2Ur5S",
  "type": "assistant",
  "uuid": "609fe50a-f586-464d-912a-268dafa03b41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNGdq7yQANA56uSUAfL13K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12239,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12239
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

_source line 9 · 2026-05-19T15:13:47.110Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KSzGyKE64avr2kFg4s2mHL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "609fe50a-f586-464d-912a-268dafa03b41",
  "isSidechain": false,
  "requestId": "req_011CbC9MPVNEHm7snJh2Ur5S",
  "type": "assistant",
  "uuid": "deb7a4cb-d6f9-484a-9582-5c9af187ad39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNGdq7yQANA56uSUAfL13K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12239,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12239
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

_source line 10 · 2026-05-19T15:13:47.163Z_

<details open><summary>🔧 Tool call — Read · `toolu_018UCfBoWECReEi1rJTiHHxA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "deb7a4cb-d6f9-484a-9582-5c9af187ad39",
  "isSidechain": false,
  "requestId": "req_011CbC9MPVNEHm7snJh2Ur5S",
  "type": "assistant",
  "uuid": "40bea833-e397-4692-b6c5-68a7abd1b788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNGdq7yQANA56uSUAfL13K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12239,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12239
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

_source line 11 · 2026-05-19T15:13:47.169Z_

<details><summary>↩ Tool result · `toolu_018UCfBoWECReEi1rJTiHHxA`</summary>

```text
1	# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering
2	
3	> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（30x 断层的定量证据）。这个 insight 为 auxiliary attention loss 在 teacher-forcing 下的 exposure bias 脆弱性提供首个定量测量。
4	> Novelty 排序: (1) exposure bias 在 auxiliary attention loss 上的首个定量测量 (30x gap) > (2) NTP-GAR 梯度竞争导致 gate 反向学习的逐层量化 > (3) principled intervention + systematic ablation 的 negative result
5	> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)
6	> 最后更新: 2026-05-19 (Dream review 后收窄 claim scope + 重新定位 distribution shift)
7	> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）
8	
9	---
10	
11	## 1. Title Candidates
12	
13	- **T1 (推荐)**: Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis
14	- **T2**: The Distribution Shift Trap: Why Training-Time Attention Steering Fails at Inference
15	- **T3**: Residual Gating Cannot Recover Goal Attention in Multi-Turn Dialogue
16	
17	推荐 T1: "Lightweight Gating" 比 "Residual Gating" 覆盖更广（含 uniform gate），"Mechanistic Analysis" 突出 insight 而非 negative result。
18	
19	---
20	
21	## 2. Story Arc
22	
23	Multi-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Attention Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), but this improvement completely fails to transfer to inference (GAR = 0.016, a 30x gap). Our central finding is that teacher-forcing training creates a fundamental distribution shift: attention patterns learned under teacher-forced contexts do not generalize to autoregressive generation, where the model conditions on its own outputs. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Combined with Dongre et al.'s independent failure of goal re-injection, our results provide the first quantitative evidence that lightweight residual gating with auxiliary attention losses is particularly vulnerable to the well-known teacher-forcing distribution shift (exposure bias), and identify the specific mechanisms through which this vulnerability manifests.
24	
25	---
26	
27	## 3. Core Claims
28	
29	| # | Claim | 支撑 | 状态 |
30	|---|-------|------|------|
31	| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | ✅ 已验证 |
32	| C2 | Residual gating 在训练端可有效优化 GAR (0.02→0.48)，但推理时完全不泛化 (GAR=0.016, 30x 断层) | v7 训练曲线 + D015/D017 confirmed non-bug | ✅ 已验证 |
33	| C3 | 三个耦合失败机制的因果分析: NF1 反向 turn conditioning + NF2 30x 泛化 gap + NF3 gate 干预强度不足 2-7% | D014 gate-profile 分析 + D015 代码验证 + 梯度冲突量化 | ✅ 已完成。梯度冲突数据：cos_sim -0.089→-0.042（方向冲突减弱），mag_ratio 7.5x→14.7x（NTP 幅度压制加剧），L27 ratio 135x→1139x |
34	| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。PPL 对比揭示 gating 不仅无 GAR 增量，也不影响语言建模质量（TG/UG/LO PPL 均 ~2.63 vs Base 4.23） | D021 四路 eval on standard_conversations | ✅ 已验证 (D021)。GAR: TG 0.487/UG 0.492/LO 0.486（差异<0.6pp）；PPL: TG 2.63/UG 2.62/LO 2.63（gating 不影响 PPL） |
35	| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Llama 实验 (待做) | ⬜ 待做 |
36	
37	---
38	
39	## 4. Negative Findings (NF)
40	
41	| # | Finding | 证据 | 叙事角色 |
42	|---|---------|------|----------|
43	| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |
44	| NF2 | 30x training-inference GAR gap: 训练 GAR=0.48 vs 推理 GAR=0.016 | D015 代码逐行验证非 bug，是 attention pattern 不泛化 | 核心 negative finding，对所有辅助 attention loss 方法有警示意义 |
45	| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |
46	| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |
47	
48	---
49	
50	## 5. Key Selling Points
51	
52	**SP1 (核心卖点): Exposure bias 在 auxiliary attention loss 上的首个定量测量。** 30x training-inference GAR gap 提供了 teacher-forcing distribution shift 如何摧毁 auxiliary attention loss 泛化性的首个定量证据。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。虽然 exposure bias 概念本身已知 (Bengio et al. 2015)，但此前无人量化其对 auxiliary attention loss 的具体影响。我们的 30x gap 测量展示了这种脆弱性的严重程度，为后续 attention steering 方法（尤其是依赖 teacher-forcing 训练的方法）提供了具体的风险标杆。**注意：claim scope 严格限于 lightweight residual gating + GAR auxiliary loss 的实测范围，不泛化到所有 attention steering 方法。**
53	
54	**SP2: NTP-GAR 梯度竞争的逐层量化。** 67-79% 的层 NTP 与 GAR 梯度方向相反（cos_sim -0.089→-0.042），且 NTP 幅度逐渐完全压制 GAR（mag_ratio 7.5x→14.7x）。方向冲突随训练减弱不是因为两个 loss 调和了，而是 GAR 信号被边缘化——NTP 逐渐完全压制 GAR。这导致 gates 学到反向 turn conditioning（NF1），是分布偏移的放大器。
55	
56	**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融 (TG/UG/LoRA-only/Base) 严格隔离贡献。
57	
58	**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。
59	
60	**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。
61	
62	---
63	
64	## 6. Anticipated Reviewer Concerns
65	
66	| # | 严重度 | 预期质疑 | 回应策略 |
67	|---|--------|----------|----------|
68	| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |
69	| W2 | **严重** | "你只是没调对参数" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |
70	| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |
71	| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |
72	| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（30x 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |
73	| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |
74	| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 "we extend Dongre"，而是 "Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations"。核心叙事是 mechanism discovery，非 follow-up work。 |
75	| W6 | **严重** | 引用不足（Dream review: 11篇远不够）| 目标 25-30 篇。必须覆盖: attention sinks (Xiao et al. 2024), Found-in-the-Middle (Ko et al. 2024), gated attention (Qiu et al. 2025), transformer circuits (Elhage et al. 2021), FlexiDepth (Luo et al. 2025), multi-turn eval (MT-Bench-101, MultiChallenge), exposure bias mitigation (Professor Forcing, SEARNN) 等。Paper Agent 写作时负责扩充。|
76	| W7 | **严重** | 单 seed 无方差估计 | 所有实验 seed=42，TG-LoRA 差异 ±0.001 在噪声层。回应: held-out eval 50 conversations 提供 paired bootstrap CI，若 CI 包含 0 则统计支持 "zero benefit"。必要时追加 2 个 seed 的训练。|
77	| W8 | **中等** | 缺 exposure-bias mitigation 实验 | 测试 scheduled sampling / model-generated context 训练能否缩小 30x gap。加入 experiment_plan (P1)。如果实验表明 mitigation 确实缩小 gap，论文从 "negative result" 升级为 "negative result + constructive direction"。|
78	| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 exposure bias 的定量测量（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |
79	| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 "we extend Dongre"，而是 "Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations"。核心叙事是 mechanism discovery，非 follow-up work。 |
80	| R3 | 低 | 30x gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |
81	| R4 | ~~低~~ **已核实** | Code-paper 公式语义相反 | **已确认不一致（plan_017 DONE）**。代码正确实现 ReZero-style: `x_{l+1} = x_l + g_l · f_l(x_l)`（gate 缩放子层输出，g→0=层 no-op）。Dream paper.tex 错误写为 `x_{l+1} = g_l · x_l + f_l(x_l)`（gate 缩放残差流，g→0=破坏 skip connection）。**实验数据不受影响**（所有实验用同一份代码）。**Paper Agent 写作时必须**: (1) Method section 用正确公式 `x + g·f(x)`; (2) 机制叙事修正: g→0 = 子层输出被抑制（层变 no-op），NTP 推 g→1 是为保留层计算能力，不是保留 skip connection; (3) NF3 "gate attenuation 2-7%" 指子层贡献缩放，表述正确但需明确。|
82	
83	---
84	
85	## 7. Dongre et al. 关系定位
86	
87	| 维度 | Dongre et al. | 本文 |
88	|------|---------------|------|
89	| 核心问题 | "发生了什么" + "为什么" | "怎么干预" + "为什么干预失败" |
90	| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |
91	| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 30x 泛化 gap + turn conditioning 反转 |
92	| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |
93	| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |
94	
95	**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。
96	
97	共同推论: 两种独立干预路线均失败 → lightweight residual gating with auxiliary attention loss 在 teacher-forcing 下面临严重泛化障碍 → 需要 inference-time 干预或 exposure bias mitigation。（注意：scope 限于 lightweight gating，不泛化到所有 attention steering 方法。）
98	
99	---
100	
101	## 8. GAR 定义策略
102	
103	| 用途 | 定义 | Goal tokens | Response tokens | 理由 |
104	|------|------|------------|----------------|------|
105	| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |
106	| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |
107	| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |
108	
109	两种定义下推理 GAR 均极低 (~0.016)，与训练 GAR (0.48) 形成 30x 断层。定义差异不影响 negative finding。
110	
111	---
112	
113	## 9. 论文结构草案
114	
115	1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示
116	2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表
117	3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention
118	4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据
119	5. **Method**: ThreadGate 架构 + MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置
120	6. **Experiments**: 四路消融 (TG/UG/LoRA-only/Base) with GAR + PPL dual metrics + 跨模型验证 (Llama-3.1-8B)
121	7. **Analysis**: NTP-GAR 梯度冲突 + 30x 泛化 gap 分析 + gate profile + attention 可视化 + 训练动力学三阶段
122	8. **Discussion**: 为什么 lightweight residual gating 不够 → exposure bias 对 auxiliary attention loss 的具体影响机制 → 潜在解决方向 (inference-time intervention / exposure bias mitigation for auxiliary losses / decoupled pathway / GAR-aware decoding) → **scope 声明: claim 限于 lightweight gating，不泛化到所有 attention steering**
123	9. **Conclusion**: negative result 总结 + 对社区的 actionable 建议
124	
125	### 贡献列表（按 novelty 排序）
126	
127	1. **Exposure bias 在 auxiliary attention loss 上的首个定量测量**: 首次量化 teacher-forcing distribution shift 如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（30x training-inference GAR gap），为 teacher-forcing 下的 attention steering 方法提供具体风险标杆
128	2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）
129	3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline
130	4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性
131	
132	---
133	
134	## 10. 竞争力评估
135	
136	### Dream Review 结果 (2026-05-19, dream_20260519T135115)
137	- **Best case**: 3.0 (Weak Reject / Findings-level)。主要扣分: claim 过度泛化 (W1), 引用不足 (W6), 单 seed (W7)。
138	- **Median case**: 3.0 (Weak Reject)。同上 + distribution shift insight incremental (W5)。
139	- **Worst case**: 未完成 review（crash），但 imagined experiments 显示最坏情况下 Llama-3 不复现 dramatic pattern。
140	
141	### 修正后预期
142	- **收窄 claim + 扩充引用 + code 验证后**: best 预期 3.5 (Weak Accept / Borderline Conference)。移除两个 Major weakness (W1 overclaim + W6 thin refs)。
143	- **加 bootstrap CI + Llama-3 数据后**: median 预期 3.0-3.5。
144	- **冲 Main 条件**: 上述修正 + exposure-bias mitigation 实验 (W8) + 25-30 references。
145	- **核心差异化**: 不是 "gating 失败了"（弱），而是 "exposure bias 在 auxiliary attention loss 上的首个定量测量 + 失败机制 taxonomy"。
146	- **关键风险**: W5（exposure bias 已知）需要精确定位增量；W7（单 seed）需 bootstrap CI 或追加 seed。
147	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40bea833-e397-4692-b6c5-68a7abd1b788",
  "isSidechain": false,
  "promptId": "60b11cf6-cc2f-4f15-8815-d9e57690cbb7",
  "type": "user",
  "uuid": "3e2f9ab7-d626-45a4-bf3b-9ea0ac5e7c5c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper_framing.md",
      "content": "# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering\n\n> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（30x 断层的定量证据）。这个 insight 为 auxiliary attention loss 在 teacher-forcing 下的 exposure bias 脆弱性提供首个定量测量。\n> Novelty 排序: (1) exposure bias 在 auxiliary attention loss 上的首个定量测量 (30x gap) > (2) NTP-GAR 梯度竞争导致 gate 反向学习的逐层量化 > (3) principled intervention + systematic ablation 的 negative result\n> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)\n> 最后更新: 2026-05-19 (Dream review 后收窄 claim scope + 重新定位 distribution shift)\n> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）\n\n---\n\n## 1. Title Candidates\n\n- **T1 (推荐)**: Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\n- **T2**: The Distribution Shift Trap: Why Training-Time Attention Steering Fails at Inference\n- **T3**: Residual Gating Cannot Recover Goal Attention in Multi-Turn Dialogue\n\n推荐 T1: \"Lightweight Gating\" 比 \"Residual Gating\" 覆盖更广（含 uniform gate），\"Mechanistic Analysis\" 突出 insight 而非 negative result。\n\n---\n\n## 2. Story Arc\n\nMulti-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Attention Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), but this improvement completely fails to transfer to inference (GAR = 0.016, a 30x gap). Our central finding is that teacher-forcing training creates a fundamental distribution shift: attention patterns learned under teacher-forced contexts do not generalize to autoregressive generation, where the model conditions on its own outputs. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Combined with Dongre et al.'s independent failure of goal re-injection, our results provide the first quantitative evidence that lightweight residual gating with auxiliary attention losses is particularly vulnerable to the well-known teacher-forcing distribution shift (exposure bias), and identify the specific mechanisms through which this vulnerability manifests.\n\n---\n\n## 3. Core Claims\n\n| # | Claim | 支撑 | 状态 |\n|---|-------|------|------|\n| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | ✅ 已验证 |\n| C2 | Residual gating 在训练端可有效优化 GAR (0.02→0.48)，但推理时完全不泛化 (GAR=0.016, 30x 断层) | v7 训练曲线 + D015/D017 confirmed non-bug | ✅ 已验证 |\n| C3 | 三个耦合失败机制的因果分析: NF1 反向 turn conditioning + NF2 30x 泛化 gap + NF3 gate 干预强度不足 2-7% | D014 gate-profile 分析 + D015 代码验证 + 梯度冲突量化 | ✅ 已完成。梯度冲突数据：cos_sim -0.089→-0.042（方向冲突减弱），mag_ratio 7.5x→14.7x（NTP 幅度压制加剧），L27 ratio 135x→1139x |\n| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。PPL 对比揭示 gating 不仅无 GAR 增量，也不影响语言建模质量（TG/UG/LO PPL 均 ~2.63 vs Base 4.23） | D021 四路 eval on standard_conversations | ✅ 已验证 (D021)。GAR: TG 0.487/UG 0.492/LO 0.486（差异<0.6pp）；PPL: TG 2.63/UG 2.62/LO 2.63（gating 不影响 PPL） |\n| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Llama 实验 (待做) | ⬜ 待做 |\n\n---\n\n## 4. Negative Findings (NF)\n\n| # | Finding | 证据 | 叙事角色 |\n|---|---------|------|----------|\n| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |\n| NF2 | 30x training-inference GAR gap: 训练 GAR=0.48 vs 推理 GAR=0.016 | D015 代码逐行验证非 bug，是 attention pattern 不泛化 | 核心 negative finding，对所有辅助 attention loss 方法有警示意义 |\n| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |\n| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |\n\n---\n\n## 5. Key Selling Points\n\n**SP1 (核心卖点): Exposure bias 在 auxiliary attention loss 上的首个定量测量。** 30x training-inference GAR gap 提供了 teacher-forcing distribution shift 如何摧毁 auxiliary attention loss 泛化性的首个定量证据。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。虽然 exposure bias 概念本身已知 (Bengio et al. 2015)，但此前无人量化其对 auxiliary attention loss 的具体影响。我们的 30x gap 测量展示了这种脆弱性的严重程度，为后续 attention steering 方法（尤其是依赖 teacher-forcing 训练的方法）提供了具体的风险标杆。**注意：claim scope 严格限于 lightweight residual gating + GAR auxiliary loss 的实测范围，不泛化到所有 attention steering 方法。**\n\n**SP2: NTP-GAR 梯度竞争的逐层量化。** 67-79% 的层 NTP 与 GAR 梯度方向相反（cos_sim -0.089→-0.042），且 NTP 幅度逐渐完全压制 GAR（mag_ratio 7.5x→14.7x）。方向冲突随训练减弱不是因为两个 loss 调和了，而是 GAR 信号被边缘化——NTP 逐渐完全压制 GAR。这导致 gates 学到反向 turn conditioning（NF1），是分布偏移的放大器。\n\n**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融 (TG/UG/LoRA-only/Base) 严格隔离贡献。\n\n**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。\n\n**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。\n\n---\n\n## 6. Anticipated Reviewer Concerns\n\n| # | 严重度 | 预期质疑 | 回应策略 |\n|---|--------|----------|----------|\n| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |\n| W2 | **严重** | \"你只是没调对参数\" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |\n| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |\n| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |\n| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（30x 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| W6 | **严重** | 引用不足（Dream review: 11篇远不够）| 目标 25-30 篇。必须覆盖: attention sinks (Xiao et al. 2024), Found-in-the-Middle (Ko et al. 2024), gated attention (Qiu et al. 2025), transformer circuits (Elhage et al. 2021), FlexiDepth (Luo et al. 2025), multi-turn eval (MT-Bench-101, MultiChallenge), exposure bias mitigation (Professor Forcing, SEARNN) 等。Paper Agent 写作时负责扩充。|\n| W7 | **严重** | 单 seed 无方差估计 | 所有实验 seed=42，TG-LoRA 差异 ±0.001 在噪声层。回应: held-out eval 50 conversations 提供 paired bootstrap CI，若 CI 包含 0 则统计支持 \"zero benefit\"。必要时追加 2 个 seed 的训练。|\n| W8 | **中等** | 缺 exposure-bias mitigation 实验 | 测试 scheduled sampling / model-generated context 训练能否缩小 30x gap。加入 experiment_plan (P1)。如果实验表明 mitigation 确实缩小 gap，论文从 \"negative result\" 升级为 \"negative result + constructive direction\"。|\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 exposure bias 的定量测量（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| R3 | 低 | 30x gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |\n| R4 | ~~低~~ **已核实** | Code-paper 公式语义相反 | **已确认不一致（plan_017 DONE）**。代码正确实现 ReZero-style: `x_{l+1} = x_l + g_l · f_l(x_l)`（gate 缩放子层输出，g→0=层 no-op）。Dream paper.tex 错误写为 `x_{l+1} = g_l · x_l + f_l(x_l)`（gate 缩放残差流，g→0=破坏 skip connection）。**实验数据不受影响**（所有实验用同一份代码）。**Paper Agent 写作时必须**: (1) Method section 用正确公式 `x + g·f(x)`; (2) 机制叙事修正: g→0 = 子层输出被抑制（层变 no-op），NTP 推 g→1 是为保留层计算能力，不是保留 skip connection; (3) NF3 \"gate attenuation 2-7%\" 指子层贡献缩放，表述正确但需明确。|\n\n---\n\n## 7. Dongre et al. 关系定位\n\n| 维度 | Dongre et al. | 本文 |\n|------|---------------|------|\n| 核心问题 | \"发生了什么\" + \"为什么\" | \"怎么干预\" + \"为什么干预失败\" |\n| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |\n| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 30x 泛化 gap + turn conditioning 反转 |\n| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |\n| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |\n\n**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。\n\n共同推论: 两种独立干预路线均失败 → lightweight residual gating with auxiliary attention loss 在 teacher-forcing 下面临严重泛化障碍 → 需要 inference-time 干预或 exposure bias mitigation。（注意：scope 限于 lightweight gating，不泛化到所有 attention steering 方法。）\n\n---\n\n## 8. GAR 定义策略\n\n| 用途 | 定义 | Goal tokens | Response tokens | 理由 |\n|------|------|------------|----------------|------|\n| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |\n| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |\n| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |\n\n两种定义下推理 GAR 均极低 (~0.016)，与训练 GAR (0.48) 形成 30x 断层。定义差异不影响 negative finding。\n\n---\n\n## 9. 论文结构草案\n\n1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示\n2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表\n3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention\n4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据\n5. **Method**: ThreadGate 架构 + MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置\n6. **Experiments**: 四路消融 (TG/UG/LoRA-only/Base) with GAR + PPL dual metrics + 跨模型验证 (Llama-3.1-8B)\n7. **Analysis**: NTP-GAR 梯度冲突 + 30x 泛化 gap 分析 + gate profile + attention 可视化 + 训练动力学三阶段\n8. **Discussion**: 为什么 lightweight residual gating 不够 → exposure bias 对 auxiliary attention loss 的具体影响机制 → 潜在解决方向 (inference-time intervention / exposure bias mitigation for auxiliary losses / decoupled pathway / GAR-aware decoding) → **scope 声明: claim 限于 lightweight gating，不泛化到所有 attention steering**\n9. **Conclusion**: negative result 总结 + 对社区的 actionable 建议\n\n### 贡献列表（按 novelty 排序）\n\n1. **Exposure bias 在 auxiliary attention loss 上的首个定量测量**: 首次量化 teacher-forcing distribution shift 如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（30x training-inference GAR gap），为 teacher-forcing 下的 attention steering 方法提供具体风险标杆\n2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）\n3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline\n4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性\n\n---\n\n## 10. 竞争力评估\n\n### Dream Review 结果 (2026-05-19, dream_20260519T135115)\n- **Best case**: 3.0 (Weak Reject / Findings-level)。主要扣分: claim 过度泛化 (W1), 引用不足 (W6), 单 seed (W7)。\n- **Median case**: 3.0 (Weak Reject)。同上 + distribution shift insight incremental (W5)。\n- **Worst case**: 未完成 review（crash），但 imagined experiments 显示最坏情况下 Llama-3 不复现 dramatic pattern。\n\n### 修正后预期\n- **收窄 claim + 扩充引用 + code 验证后**: best 预期 3.5 (Weak Accept / Borderline Conference)。移除两个 Major weakness (W1 overclaim + W6 thin refs)。\n- **加 bootstrap CI + Llama-3 数据后**: median 预期 3.0-3.5。\n- **冲 Main 条件**: 上述修正 + exposure-bias mitigation 实验 (W8) + 25-30 references。\n- **核心差异化**: 不是 \"gating 失败了\"（弱），而是 \"exposure bias 在 auxiliary attention loss 上的首个定量测量 + 失败机制 taxonomy\"。\n- **关键风险**: W5（exposure bias 已知）需要精确定位增量；W7（单 seed）需 bootstrap CI 或追加 seed。\n",
      "numLines": 147,
      "startLine": 1,
      "totalLines": 147
    }
  },
  "sourceToolAssistantUUID": "40bea833-e397-4692-b6c5-68a7abd1b788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T145320 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_g…",
  "leafUuid": "3e2f9ab7-d626-45a4-bf3b-9ea0ac5e7c5c",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396"
}
```

---

### Tool result

_source line 14 · 2026-05-19T15:13:47.397Z_

<details><summary>↩ Tool result · `toolu_01KSzGyKE64avr2kFg4s2mHL`</summary>

```text
1	[
2	  {
3	    "name": "Qwen Gradient Conflict Analysis (3 checkpoints)",
4	    "description": "对 v7 训练的 3 个 epoch checkpoint 计算 NTP vs GAR 在 gate 参数上的梯度 cos_sim 和 magnitude ratio，量化梯度竞争随训练的演化。\n",
5	    "results": {
6	      "epoch0_cos_sim_mean": -0.089,
7	      "epoch0_cos_sim_conflict_layer_pct": 0.79,
8	      "epoch0_mag_ratio_mean": 7.5,
9	      "epoch0_mag_ratio_max_layer": "L27",
10	      "epoch0_mag_ratio_max": 135,
11	      "epoch1_cos_sim_mean": -0.063,
12	      "epoch1_cos_sim_conflict_layer_pct": 0.71,
13	      "epoch1_mag_ratio_mean": 11.2,
14	      "epoch1_mag_ratio_max_layer": "L27",
15	      "epoch1_mag_ratio_max": 580,
16	      "epoch2_cos_sim_mean": -0.042,
17	      "epoch2_cos_sim_conflict_layer_pct": 0.67,
18	      "epoch2_mag_ratio_mean": 14.7,
19	      "epoch2_mag_ratio_max_layer": "L27",
20	      "epoch2_mag_ratio_max": 1139,
21	      "cos_sim_trend": "conflict weakens over training (-0.089 → -0.042)",
22	      "mag_ratio_trend": "NTP dominance increases (7.5x → 14.7x)"
23	    },
24	    "tables": [
25	      {
26	        "name": "Table: Per-layer gradient conflict evolution",
27	        "columns": [
28	          "Layer",
29	          "Epoch0 cos_sim",
30	          "Epoch1 cos_sim",
31	          "Epoch2 cos_sim",
32	          "Epoch0 mag_ratio",
33	          "Epoch1 mag_ratio",
34	          "Epoch2 mag_ratio"
35	        ],
36	        "description": "28 层 x 3 checkpoints 的完整 cos_sim + mag_ratio 矩阵。 高亮标注 cos_sim>0 的少数层（预期 6-9 层无冲突）和 mag_ratio 极端层。\n"
37	      }
38	    ],
39	    "figures": [],
40	    "analysis": "数据确认 NTP-GAR 梯度竞争是 ThreadGate 失败的关键放大器。cos_sim 随训练减弱 不代表两个 loss 目标趋于一致，而是 NTP 幅度完全压制 GAR 的结果——GAR 梯度 变得相对微不足道，方向冲突在实际参数更新中已无影响。这与 NF1（gate 反向 turn conditioning）形成因果链：NTP 推 gate→1.0 的梯度持续增强，导致 gate 在晚期 turn 变为 passive identity，正好是需要干预的时候。\n\n\n这些数值与 CLAUDE.md 中已有的梯度数据一致（cos_sim -0.089→-0.042，mag_ratio 7.5x→14.7x）。cos_sim 随训练变得更不负是因为 GAR 信号逐渐被边缘化——不是 两个 loss 达成调和，而是 GAR 梯度幅度相对 NTP 变得微不足道，方向冲突在绝对 量级上变得无关紧要。mag_ratio 持续增大证实了这一点：NTP 梯度越来越完全主导 gate 参数更新。L27 的极端 ratio（135→1139x）反映最后一层 NTP 信号最强。 67-79% 的层保持方向冲突，说明这是系统性现象而非个别层的特例。\n"
41	  },
42	  {
43	    "name": "Attention Heatmap Visualization",
44	    "description": "4 模型（Base/TG/UG/LoRA-only）x 3 conversations x 选定层的 attention heatmap，可视化 goal token 的 attention 权重在不同 turn 的变化。\n",
45	    "results": {
46	      "base_goal_attn_turn1": 0.042,
47	      "base_goal_attn_turn10": 0.012,
48	      "base_goal_attn_turn21": 0.006,
49	      "tg_goal_attn_turn1": 0.044,
50	      "tg_goal_attn_turn10": 0.013,
51	      "tg_goal_attn_turn21": 0.007,
52	      "ug_goal_attn_turn1": 0.043,
53	      "ug_goal_attn_turn10": 0.012,
54	      "ug_goal_attn_turn21": 0.006,
55	      "lora_goal_attn_turn1": 0.043,
56	      "lora_goal_attn_turn10": 0.013,
57	      "lora_goal_attn_turn21": 0.007,
58	      "visual_pattern": "所有 4 模型的 attention heatmap 在推理时几乎不可区分"
59	    },
60	    "tables": [],
61	    "figures": [],
62	    "analysis": "可视化提供了最直观的 negative result 证据：训练时 TG 的 attention pattern 与其他模型显著不同（GAR 0.48 vs 0.01），但推理时这种差异完全消失。 这正是 distribution shift 的视觉证据——teacher-forcing 下学到的 attention redistribution 在 autoregressive generation 中不迁移。\n\n\n推理时 GAR~0.015 对所有训练变体几乎一致（四路 eval 已确认差异<0.6pp）， 所以 attention heatmap 在推理时应呈现几乎相同的 pattern：goal token 的 attention 权重随 turn 衰减，且 4 个模型之间无可见差异。这直观地验证了 \"gating 无增量贡献\"——即使 TG 在训练时 GAR 达到 0.48，推理时生成的 attention pattern 与从未见过 GAR loss 的 LoRA-only 模型几乎一致。 选择关键层（如 L3/L4 gate 值最低层 和 L27 gate 值最高层）做对比， 可以进一步展示 gate 的层间差异在推理时也不反映为 attention 差异。\n"
63	  },
64	  {
65	    "name": "Llama-3.1-8B Phase 1 GAR Degradation Diagnosis",
66	    "description": "在 Llama-3.1-8B base model 上复现 Phase 1 GAR 衰减诊断，确认 GAR decay 是否存在于不同架构。使用与 Qwen 相同的 eval conversations。\n",
67	    "results": {
68	      "turn1_avg_gar": 0.038,
69	      "mid_turns_avg_gar": 0.0225,
70	      "relative_drop": 0.408,
71	      "num_conversations": 5,
72	      "num_turns": 10,
73	      "per_turn_avg_gar": [
74	        0.038,
75	        0.031,
76	        0.0295,
77	        0.026,
78	        0.0245,
79	        0.022,
80	        0.021,
81	        0.0195,
82	        0.02,
83	        0.0185
84	      ]
85	    },
86	    "tables": [
87	      {
88	        "name": "Table: Cross-model GAR decay comparison",
89	        "columns": [
90	          "Turn",
91	          "Qwen-2.5-7B GAR",
92	          "Llama-3.1-8B GAR"
93	        ],
94	        "description": "逐 turn 对比两个模型的 base GAR 衰减。"
95	      }
96	    ],
97	    "figures": [],
98	    "analysis": "Llama-3 的 GAR 衰减方向与 Qwen 一致，但幅度约为一半。这意味着 C1（GAR 衰减是结构性现象）在方向上得到跨模型验证，但\"严重\"（70.8%）这个修饰词 只能 claim 在 Qwen 上。Llama 的 40.8% 衰减仍有统计意义但不够 dramatic， 论文需报告为\"中等程度衰减\"。这影响了后续实验的预期：较弱的 base 衰减 意味着 gating 干预的潜在空间更小，可能导致效应更难检测。\n\n\nMedian 档预测 Llama-3 base GAR 衰减存在但较弱（raw drop 30-50%）。这里取 40.8%（在 [0.3, 0.5] 范围内）。Llama-3 架构与 Qwen-2.5 的关键差异包括 GQA（grouped query attention）vs MHA、不同的 positional encoding 实现（RoPE 参数不同）、以及不同的预训练数据分布。GQA 的 KV 共享机制可能 使得 goal token 的 attention 信号在 key-value 压缩后更持久，因为多个 query head 共享同一组 KV，减少了 attention pattern 的碎片化。此外 Llama-3 的 预训练可能包含更多多轮对话数据（Meta 的 RLHF 数据），使模型对 system prompt 的注意力衰减更慢。衰减方向一致（单调递减）但幅度约为 Qwen 的 一半，且衰减曲线更平缓（非陡降后平台，而是渐进式下降）。\n"
99	  },
100	  {
101	    "name": "Llama-3.1-8B ThreadGate v7 Training",
102	    "description": "在 Llama-3.1-8B 上复制 Qwen 的 ThreadGate v7 训练设置（MSE+gate_div loss）， 验证训练-推理 GAR gap 是否跨模型存在。\n",
103	    "results": {
104	      "training_gar_converged": 0.38,
105	      "training_gar_convergence_gs": 180,
106	      "training_time_hours": 7.2,
107	      "final_avg_ntp": 0.92,
108	      "final_avg_gar": 0.003,
109	      "final_gate_mean": 0.945,
110	      "final_gate_std": 0.038,
111	      "final_gate_min": 0.82,
112	      "final_gate_max": 0.99,
113	      "eval_dongre_mid_gar": 0.038,
114	      "eval_dongre_turn1_gar": 0.052,
115	      "eval_ours_mid_gar": 0.42,
116	      "eval_ours_turn1_gar": 0.46,
117	      "train_infer_gap_ratio_dongre": 10.0,
118	      "train_infer_gap_ratio_ours": 0.9,
119	      "gate_direction": "WRONG: same reverse turn conditioning as Qwen but less pronounced",
120	      "gate_top5_diff_range": [
121	        -0.12,
122	        -0.06
123	      ]
124	    },
125	    "tables": [
126	      {
127	        "name": "Table: Cross-model training-inference gap comparison",
128	        "columns": [
129	          "Metric",
130	          "Qwen-2.5-7B",
131	          "Llama-3.1-8B"
132	        ],
133	        "description": "训练 GAR、推理 GAR、gap ratio、gate profile 的双模型对比。"
134	      }
135	    ],
136	    "figures": [],
137	    "analysis": "10x gap 仍然是定量上显著的 distribution shift 证据，但无法与 Qwen 的 30x 等量齐观。论文中 SP1 的 \"30x gap\" 只能 claim 在 Qwen 上；Llama 需单独 报告为 \"10x gap\"。C2 的跨模型表述从\"训练-推理 GAR gap 是普遍现象\"调整为 \"gap 方向一致，幅度与架构相关（Qwen 30x, Llama 10x）\"。\n\n\nMedian 档预测训练-推理 gap 存在但较小（8-15x vs Qwen 30x）。取 10x。 训练端 GAR 收敛值略低于 Qwen（0.38 vs 0.48），因为 Llama-3 的 GQA 架构 使得 attention head 间的耦合更强——同一组 KV 被多个 query head 共享， MSE target 推动的 attention redistribution 受到更多约束。收敛也更慢 （gs180 vs gs144），反映优化 landscape 的差异。推理时 GAR=0.038 显著高于 Qwen 的 0.016，这与 base model 的更高 base GAR（0.022 vs 0.012）一致—— Llama 的 attention 本底就更多分配给 goal token，gating 后的推理 GAR 也相应更高。10x gap（0.38/0.038）虽然远小于 Qwen 的 30x（0.48/0.016）， 但方向完全一致：训练时有效的 GAR 优化在推理时大幅衰减。Gate 反向 turn conditioning 存在但幅度更小（diff -0.06~-0.12 vs Qwen -0.11~-0.21）， 符合\"pattern 一致但不如 Qwen 干净\"的预期。\n"
138	  },
139	  {
140	    "name": "Llama-3.1-8B LoRA-only Training",
141	    "description": "在 Llama-3.1-8B 上训练 LoRA-only baseline（无 gate，无 GAR loss）， 用于与 TG 对比隔离 gating 机制的增量贡献。\n",
142	    "results": {
143	      "epochs_completed": 3,
144	      "global_steps": 3000,
145	      "training_time_hours": 7.0,
146	      "final_lora_size_mb": 22,
147	      "gate_fixed": 1,
148	      "gate_type_actual": "none",
149	      "final_avg_ntp": 0.93
150	    },
151	    "tables": [],
152	    "figures": [],
153	    "analysis": "标准训练，无特殊发现。关键作用是作为 plan_012 的 baseline。\n\n\nLoRA-only 训练是标准的 NTP fine-tuning，无 GAR 目标，无 gate 参数。 Llama-3.1-8B 有 32 层（vs Qwen 28 层），LoRA 参数量略大（22MB vs 20MB）。 训练时间因模型稍大而略长。NTP loss 收敛值与 Qwen 的 LoRA-only 类似 （0.93 vs 0.95），因为两者都在相同的 UltraChat 数据上做 NTP fine-tuning。 这个实验本身没有新的 insight，纯粹是 plan_012 三路 eval 的前置依赖。\n"
154	  },
155	  {
156	    "name": "Llama-3.1-8B 3-way Eval",
157	    "description": "在 held-out data 上对 Llama-3.1-8B 的 Base/TG/LoRA-only 三路模型做 GAR + PPL 评估，验证 gating 增量贡献是否跨模型为零。\n",
158	    "results": {
159	      "base_dongre_mid_gar": 0.0045,
160	      "base_ppl": 4.5,
161	      "base_ntp": 1.45,
162	      "tg_dongre_mid_gar": 0.038,
163	      "tg_ppl": 2.85,
164	      "tg_ntp": 0.96,
165	      "lora_dongre_mid_gar": 0.022,
166	      "lora_ppl": 2.83,
167	      "lora_ntp": 0.95,
168	      "tg_vs_lora_dongre_gar_diff_pp": 1.6,
169	      "tg_vs_lora_ppl_diff": 0.02,
170	      "gating_incremental_benefit": "marginal_positive_but_noisy",
171	      "tg_ours_mid_gar": 0.42,
172	      "lora_ours_mid_gar": 0.4,
173	      "tg_vs_lora_ours_gar_diff_pp": 2.0
174	    },
175	    "tables": [
176	      {
177	        "name": "Table: Llama-3.1-8B 3-way eval results",
178	        "columns": [
179	          "Model",
180	          "GAR-Dongre mid",
181	          "GAR-ours mid",
182	          "PPL",
183	          "NTP"
184	        ],
185	        "description": "Base/TG/LoRA-only 三路评估结果。"
186	      },
187	      {
188	        "name": "Table: Cross-model gating increment comparison",
189	        "columns": [
190	          "Metric",
191	          "Qwen (TG-LO)",
192	          "Llama (TG-LO)"
193	        ],
194	        "description": "双模型 gating 增量对比。Qwen <0.6pp vs Llama 1.6pp。"
195	      }
196	    ],
197	    "figures": [],
198	    "analysis": "Llama 上 TG vs LoRA-only 差异更大（1.6pp vs <0.6pp）使得 C4（gating 无 增量贡献）的跨模型表述需要 nuance。在 Qwen 上可以 claim \"zero benefit\"， 在 Llama 上只能 claim \"marginal and inconsistent benefit\"。论文需承认 \"gating 在不同架构上的残余效应幅度不同\"，并解释可能的架构原因（GQA 的 KV 共享使部分 attention redistribution 在推理时更持久）。\n\n\nMedian 档预测 TG vs LoRA-only 差异在 1-3pp 范围，取 1.6pp（Dongre 定义）。 这比 Qwen 的 <0.6pp 差异更大，关键原因是 Llama 的 base GAR 本底更高 （0.022 vs 0.012），且 10x 的训练-推理 gap 比 Qwen 的 30x 更小——TG 在推理时保留了更多训练效果（虽然仍大幅衰减）。1.6pp 差异在 50 条对话 的 held-out eval 中可能在统计边缘（取决于方差），不足以 claim \"gating 有明确增量贡献\"，但也不像 Qwen 那样干净地 claim \"zero benefit\"。 这正是 median 档的核心困难：Llama 的结果不彻底否定也不彻底支持 gating， 只能描述为\"方向一致但效应更弱且差异更大\"。PPL 差异微小（0.02），仍然 支持\"gating 不影响语言建模质量\"。\n"
199	  },
200	  {
201	    "name": "Llama-3.1-8B Gradient Conflict Analysis",
202	    "description": "在 Llama-3.1-8B TG v7 的 checkpoints 上计算 NTP vs GAR 梯度冲突， 验证梯度竞争是否跨模型存在。\n",
203	    "results": {
204	      "epoch0_cos_sim_mean": -0.052,
205	      "epoch0_cos_sim_conflict_layer_pct": 0.63,
206	      "epoch0_mag_ratio_mean": 5.2,
207	      "epoch2_cos_sim_mean": -0.028,
208	      "epoch2_cos_sim_conflict_layer_pct": 0.56,
209	      "epoch2_mag_ratio_mean": 6.8,
210	      "epoch2_mag_ratio_max": 420,
211	      "positive_cos_sim_layers": [
212	        3,
213	        7,
214	        12,
215	        15,
216	        18,
217	        20,
218	        24,
219	        28,
220	        30,
221	        31
222	      ],
223	      "positive_cos_sim_layer_count": 10,
224	      "cos_sim_range": [
225	        -0.058,
226	        0.018
227	      ]
228	    },
229	    "tables": [
230	      {
231	        "name": "Table: Cross-model gradient conflict comparison",
232	        "columns": [
233	          "Metric",
234	          "Qwen-2.5-7B",
235	          "Llama-3.1-8B"
236	        ],
237	        "description": "cos_sim mean, conflict pct, mag_ratio 双模型对比。"
238	      }
239	    ],
240	    "figures": [],
241	    "analysis": "部分层 cos_sim 正值是 median 档的关键麻烦点。论文无法 claim 梯度冲突是 \"所有层的 universal pattern\"，只能说\"大多数层存在冲突，少数层因 GQA 的 KV 共享出现协同\"。这削弱了 SP2 的力度，但不完全否定——梯度冲突仍是 主导 pattern（56-63% 层），且 NTP 幅度仍全面压制 GAR（mag_ratio 5-7x）。\n\n\nMedian 档预测 cos_sim 在 [-0.06, 0.02] 范围，mag_ratio 在 [3, 8] 范围。 Llama 的梯度冲突存在但 pattern 不完全一致——约 56-63% 的层有方向冲突 （vs Qwen 67-79%），且有约 10/32 层显示正 cos_sim（协同而非冲突）。 这是 GQA 架构的结果：共享的 KV 使得某些层中 NTP 和 GAR 梯度方向意外 对齐（优化 NTP 的 KV 更新恰好也有利于 goal token attention）。mag_ratio 仍然倾向 NTP（5-7x），但远不如 Qwen 极端（7.5-14.7x）。最高层的 max ratio 420（vs Qwen 1139x）也反映了更温和的梯度支配。 这意味着 C3（NTP-GAR 梯度竞争导致 gate 反向学习）在 Llama 上是 \"存在但不完全一致\"——方向冲突在大多数层成立，但有足够多的例外层 使得 pattern 不如 Qwen 干净。论文需要从\"梯度冲突是 universal mechanism\" 弱化为\"梯度冲突是 dominant mechanism in Qwen, partially replicated in Llama\"。\n"
242	  },
243	  {
244	    "name": "Downstream Task Sanity Check",
245	    "description": "简单下游任务验证：测试 system prompt 中设定的 instruction（如角色扮演、 格式要求）在多轮对话中的保持率，将 GAR 与 task-level metric 关联。\n",
246	    "results": {
247	      "base_instruction_retention_turn1": 0.82,
248	      "base_instruction_retention_turn10": 0.68,
249	      "base_instruction_retention_turn21": 0.55,
250	      "tg_instruction_retention_turn1": 0.83,
251	      "tg_instruction_retention_turn10": 0.69,
252	      "tg_instruction_retention_turn21": 0.56,
253	      "lora_instruction_retention_turn1": 0.83,
254	      "lora_instruction_retention_turn10": 0.69,
255	      "lora_instruction_retention_turn21": 0.55,
256	      "gar_retention_correlation": 0.72,
257	      "cross_model_retention_diff_pp": "<1.5"
258	    },
259	    "tables": [
260	      {
261	        "name": "Table: Instruction retention vs GAR across turns",
262	        "columns": [
263	          "Turn",
264	          "Base GAR",
265	          "Base Retention",
266	          "TG GAR",
267	          "TG Retention"
268	        ],
269	        "description": "GAR 与 instruction retention 的逐 turn 对比。"
270	      }
271	    ],
272	    "figures": [],
273	    "analysis": "GAR 与下游 instruction retention 的正相关（r≈0.72）为 GAR 作为代理指标 提供了必要的验证。论文可以声明\"GAR 衰减不仅是 attention 层面的现象， 而且与可观测的 task performance 下降相关\"。但注意相关系数不极高（不是 0.95+），说明 GAR 只是影响 instruction following 的因素之一。\n\n\nInstruction retention rate 随 turn 下降与 GAR 衰减方向一致（相关系数 ~0.72），提供了 GAR 作为代理指标的 face validity。但三个训练变体之间 几乎无差异（<1.5pp），与推理 GAR 的一致性一致——gating 不改善推理时的 attention pattern，自然也不改善下游 instruction following。这个实验的 价值主要是回应 W3（GAR 作为唯一代理指标的担忧），证明 GAR 衰减确实 对应 task performance 下降，而非仅仅是一个无关的 attention 统计量。 Base model retention 从 82% 降到 55%（27pp 下降），与 GAR 70.8% 下降 幅度不完全一致，但方向一致。\n"
274	  },
275	  {
276	    "name": "Bootstrap CI Statistical Significance",
277	    "description": "对 held-out eval（50 conversations）的 TG vs LoRA-only GAR 差异做 paired bootstrap confidence interval，检验\"zero benefit\"假设。\n",
278	    "results": {
279	      "qwen_tg_lora_dongre_gar_diff_mean": 0.002,
280	      "qwen_tg_lora_dongre_gar_diff_ci95_lower": -0.018,
281	      "qwen_tg_lora_dongre_gar_diff_ci95_upper": 0.022,
282	      "qwen_ci_includes_zero": true,
283	      "qwen_bootstrap_p_value": 0.42,
284	      "qwen_effect_size_cohens_d": 0.05,
285	      "llama_tg_lora_dongre_gar_diff_mean": 0.016,
286	      "llama_tg_lora_dongre_gar_diff_ci95_lower": -0.008,
287	      "llama_tg_lora_dongre_gar_diff_ci95_upper": 0.041,
288	      "llama_ci_includes_zero": true,
289	      "llama_ci_width": 0.049,
290	      "llama_bootstrap_p_value": 0.12,
291	      "llama_effect_size_cohens_d": 0.22,
292	      "bootstrap_iterations": 10000
293	    },
294	    "tables": [
295	      {
296	        "name": "Table: Bootstrap CI summary (TG vs LoRA-only, Dongre GAR)",
297	        "columns": [
298	          "Model",
299	          "Mean diff",
300	          "95% CI lower",
301	          "95% CI upper",
302	          "p-value",
303	          "Cohen's d"
304	        ],
305	        "description": "Qwen 和 Llama 的 bootstrap CI 对比。"
306	      }
307	    ],
308	    "figures": [],
309	    "analysis": "Qwen 的结果干净地支持 C4（zero benefit）。Llama 的结果是 median 档的 典型 ambiguity：无法拒绝零假设，但也无法确信排除小正效应。论文需在 Results 中分别报告两个模型的 CI，并在 Discussion 中解释\"Llama 的更宽 CI 可能反映更高的 base GAR 方差或更弱但非零的 gating 残余效应\"。 追加 1-2 个 seed 可以缩窄 CI，但在 median 档下即使追加 seed 也只是 将 p 从 0.12 推到 0.07-0.09 附近，仍然 marginal。\n\n\nQwen 的 CI 紧且对称（[-0.018, 0.022]），含 0，p=0.42，效应量极小 （d=0.05）——统计上强支持\"zero benefit\"。这与 held-out eval 中 TG-LO 差异<0.6pp 一致。 Llama 的 CI 更宽（[-0.008, 0.041]，宽度 0.049 vs Qwen 0.040）， 仍含 0 但偏正（均值 0.016），p=0.12。这是 median 档的关键特征： CI 包含 0（技术上无法拒绝零假设），但宽度较大且偏向正方向，意味着 可能存在微小正效应但 50 条对话的 power 不足以检测。效应量 d=0.22 是\"小效应\"，统计学上 marginal。论文的表述需要是\"CI includes 0, consistent with zero or small positive benefit\"，而非 Qwen 那样 干净的\"statistically confirms zero benefit\"。\n"
310	  },
311	  {
312	    "name": "Exposure-Bias Mitigation (Scheduled Sampling)",
313	    "description": "在 ThreadGate v7 训练中引入 scheduled sampling：以递增概率用模型自身 生成的 context 替换 teacher-forced context，使 GAR loss 在更接近推理时 分布的 context 上优化。测试能否缩小 30x 训练-推理 GAR gap。\n",
314	    "results": {
315	      "qwen_ss_training_gar_converged": 0.32,
316	      "qwen_ss_training_gar_lower_than_tf": true,
317	      "qwen_ss_training_time_hours": 9.5,
318	      "qwen_ss_eval_dongre_mid_gar": 0.026,
319	      "qwen_ss_eval_ours_mid_gar": 0.35,
320	      "qwen_ss_train_infer_gap_ratio": 12.3,
321	      "qwen_ss_gap_reduction_vs_tf": 2.44,
322	      "qwen_ss_gap_reduction_factor": 1.6,
323	      "qwen_ss_ppl": 2.72,
324	      "qwen_ss_vs_lora_dongre_gar_diff_pp": 1.24,
325	      "qwen_ss_gate_mean": 0.918,
326	      "qwen_ss_gate_direction": "MIXED: 15/28 layers still show reverse conditioning, 13/28 show correct or neutral",
327	      "qwen_ss_vs_tf_bootstrap_p": 0.07,
328	      "qwen_ss_vs_tf_ci95_lower": -0.003,
329	      "qwen_ss_vs_tf_ci95_upper": 0.023,
330	      "qwen_ss_vs_tf_ci_includes_zero": true,
331	      "ss_sampling_schedule": "linear 0→0.5 over epoch 0-1, fixed 0.5 epoch 2",
332	      "ss_convergence_slower": true,
333	      "ss_convergence_gs": 210,
334	      "ss_training_instability": "mild oscillation in GAR loss during high sampling ratio"
335	    },
336	    "tables": [
337	      {
338	        "name": "Table: Mitigation comparison (Teacher-forcing vs Scheduled Sampling)",
339	        "columns": [
340	          "Metric",
341	          "TF (v7)",
342	          "SS",
343	          "Δ"
344	        ],
345	        "description": "训练 GAR、推理 GAR、gap ratio、PPL、gate direction 的 TF vs SS 对比。"
346	      }
347	    ],
348	    "figures": [],
349	    "analysis": "Scheduled sampling 展示了方向正确但幅度不足的改善。Gap 从 30x 缩小到 12.3x 说明 exposure bias 确实是 training-inference gap 的部分原因，但 即使缩小后 gap 仍然巨大（12.3x），说明 distribution shift 不仅仅来自 teacher-forcing vs autoregressive 的差异——可能还有 NTP 梯度压制、 训练数据长度分布等其他因素。\n统计上 marginal 的结果（p≈0.07，CI 含 0）意味着这个实验无法作为 独立的 positive claim，但可以作为 Discussion 中的 constructive evidence： \"scheduled sampling shows a suggestive but statistically inconclusive trend toward gap reduction, consistent with exposure bias being a contributing factor\"。\n论文策略：mitigation 结果降级到 Discussion section 作为 suggestive evidence，不放入 core claims。标题保持 negative result 基调。 如果追加 seed 或更大 eval set 能将 p 推到 <0.05，可以升级为 minor finding，但在 median 档下不太可能。\n\nMedian 档预测 mitigation 将 gap 缩小 1.2-2.0x（取 1.6x），post-inference GAR 在 0.02-0.04 范围（取 0.026）。\nScheduled sampling 的逻辑是正确的：在训练时混入 model-generated context 缩小 teacher-forcing 与 autoregressive generation 的分布差异。但在实践中 效果受限于几个因素：\n(1) 训练 GAR 收敛值降低（0.32 vs TF 的 0.48），因为 model-generated context 引入噪声，GAR target 更难达到。模型在\"混乱\"的 context 上 优化 attention 更困难。\n(2) 推理 GAR 确实提高（0.026 vs TF 的 0.016），说明部分 attention pattern 确实在更接近推理分布的 context 上得到了更好的泛化。但提升 幅度有限——从 0.016 到 0.026 只是 62.5% 相对提升，绝对值仍然极低。\n(3) Gap 从 30x 缩小到 12.3x（reduction factor 1.6x 在 [1.2, 2.0] 范围内），方向正确但幅度不够 convincing。12.3x 的 gap 仍然意味着 推理时 attention pattern 与训练时有一个数量级的差异。\n(4) 统计上 marginal：SS vs TF 的推理 GAR 差异 bootstrap p≈0.07， CI 包含 0（[-0.003, 0.023]）。在 conventional α=0.05 下无法拒绝 零假设，但方向一致（正效应）。这正是\"结果模糊\"的定义：有 suggestive evidence 但不够 conclusive。\n(5) Gate direction 部分修正（13/28 层不再反向 conditioning），说明 SS 确实改善了 gradient conflict 的某些方面，但未完全解决。\n(6) 训练更慢更不稳定（9.5h vs 5.9h），收敛需要更多 steps（gs210 vs gs144），GAR loss 在高 sampling ratio 时有震荡。这是 exposure bias mitigation 方法的已知代价（Bengio et al. 2015）。\n"
350	  }
351	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "deb7a4cb-d6f9-484a-9582-5c9af187ad39",
  "isSidechain": false,
  "promptId": "60b11cf6-cc2f-4f15-8815-d9e57690cbb7",
  "type": "user",
  "uuid": "6f6d009f-b37b-4999-8e0f-edcb7ffd19eb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Qwen Gradient Conflict Analysis (3 checkpoints)\",\n    \"description\": \"对 v7 训练的 3 个 epoch checkpoint 计算 NTP vs GAR 在 gate 参数上的梯度 cos_sim 和 magnitude ratio，量化梯度竞争随训练的演化。\\n\",\n    \"results\": {\n      \"epoch0_cos_sim_mean\": -0.089,\n      \"epoch0_cos_sim_conflict_layer_pct\": 0.79,\n      \"epoch0_mag_ratio_mean\": 7.5,\n      \"epoch0_mag_ratio_max_layer\": \"L27\",\n      \"epoch0_mag_ratio_max\": 135,\n      \"epoch1_cos_sim_mean\": -0.063,\n      \"epoch1_cos_sim_conflict_layer_pct\": 0.71,\n      \"epoch1_mag_ratio_mean\": 11.2,\n      \"epoch1_mag_ratio_max_layer\": \"L27\",\n      \"epoch1_mag_ratio_max\": 580,\n      \"epoch2_cos_sim_mean\": -0.042,\n      \"epoch2_cos_sim_conflict_layer_pct\": 0.67,\n      \"epoch2_mag_ratio_mean\": 14.7,\n      \"epoch2_mag_ratio_max_layer\": \"L27\",\n      \"epoch2_mag_ratio_max\": 1139,\n      \"cos_sim_trend\": \"conflict weakens over training (-0.089 → -0.042)\",\n      \"mag_ratio_trend\": \"NTP dominance increases (7.5x → 14.7x)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Per-layer gradient conflict evolution\",\n        \"columns\": [\n          \"Layer\",\n          \"Epoch0 cos_sim\",\n          \"Epoch1 cos_sim\",\n          \"Epoch2 cos_sim\",\n          \"Epoch0 mag_ratio\",\n          \"Epoch1 mag_ratio\",\n          \"Epoch2 mag_ratio\"\n        ],\n        \"description\": \"28 层 x 3 checkpoints 的完整 cos_sim + mag_ratio 矩阵。 高亮标注 cos_sim>0 的少数层（预期 6-9 层无冲突）和 mag_ratio 极端层。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"数据确认 NTP-GAR 梯度竞争是 ThreadGate 失败的关键放大器。cos_sim 随训练减弱 不代表两个 loss 目标趋于一致，而是 NTP 幅度完全压制 GAR 的结果——GAR 梯度 变得相对微不足道，方向冲突在实际参数更新中已无影响。这与 NF1（gate 反向 turn conditioning）形成因果链：NTP 推 gate→1.0 的梯度持续增强，导致 gate 在晚期 turn 变为 passive identity，正好是需要干预的时候。\\n\\n\\n这些数值与 CLAUDE.md 中已有的梯度数据一致（cos_sim -0.089→-0.042，mag_ratio 7.5x→14.7x）。cos_sim 随训练变得更不负是因为 GAR 信号逐渐被边缘化——不是 两个 loss 达成调和，而是 GAR 梯度幅度相对 NTP 变得微不足道，方向冲突在绝对 量级上变得无关紧要。mag_ratio 持续增大证实了这一点：NTP 梯度越来越完全主导 gate 参数更新。L27 的极端 ratio（135→1139x）反映最后一层 NTP 信号最强。 67-79% 的层保持方向冲突，说明这是系统性现象而非个别层的特例。\\n\"\n  },\n  {\n    \"name\": \"Attention Heatmap Visualization\",\n    \"description\": \"4 模型（Base/TG/UG/LoRA-only）x 3 conversations x 选定层的 attention heatmap，可视化 goal token 的 attention 权重在不同 turn 的变化。\\n\",\n    \"results\": {\n      \"base_goal_attn_turn1\": 0.042,\n      \"base_goal_attn_turn10\": 0.012,\n      \"base_goal_attn_turn21\": 0.006,\n      \"tg_goal_attn_turn1\": 0.044,\n      \"tg_goal_attn_turn10\": 0.013,\n      \"tg_goal_attn_turn21\": 0.007,\n      \"ug_goal_attn_turn1\": 0.043,\n      \"ug_goal_attn_turn10\": 0.012,\n      \"ug_goal_attn_turn21\": 0.006,\n      \"lora_goal_attn_turn1\": 0.043,\n      \"lora_goal_attn_turn10\": 0.013,\n      \"lora_goal_attn_turn21\": 0.007,\n      \"visual_pattern\": \"所有 4 模型的 attention heatmap 在推理时几乎不可区分\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"可视化提供了最直观的 negative result 证据：训练时 TG 的 attention pattern 与其他模型显著不同（GAR 0.48 vs 0.01），但推理时这种差异完全消失。 这正是 distribution shift 的视觉证据——teacher-forcing 下学到的 attention redistribution 在 autoregressive generation 中不迁移。\\n\\n\\n推理时 GAR~0.015 对所有训练变体几乎一致（四路 eval 已确认差异<0.6pp）， 所以 attention heatmap 在推理时应呈现几乎相同的 pattern：goal token 的 attention 权重随 turn 衰减，且 4 个模型之间无可见差异。这直观地验证了 \\\"gating 无增量贡献\\\"——即使 TG 在训练时 GAR 达到 0.48，推理时生成的 attention pattern 与从未见过 GAR loss 的 LoRA-only 模型几乎一致。 选择关键层（如 L3/L4 gate 值最低层 和 L27 gate 值最高层）做对比， 可以进一步展示 gate 的层间差异在推理时也不反映为 attention 差异。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B Phase 1 GAR Degradation Diagnosis\",\n    \"description\": \"在 Llama-3.1-8B base model 上复现 Phase 1 GAR 衰减诊断，确认 GAR decay 是否存在于不同架构。使用与 Qwen 相同的 eval conversations。\\n\",\n    \"results\": {\n      \"turn1_avg_gar\": 0.038,\n      \"mid_turns_avg_gar\": 0.0225,\n      \"relative_drop\": 0.408,\n      \"num_conversations\": 5,\n      \"num_turns\": 10,\n      \"per_turn_avg_gar\": [\n        0.038,\n        0.031,\n        0.0295,\n        0.026,\n        0.0245,\n        0.022,\n        0.021,\n        0.0195,\n        0.02,\n        0.0185\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-model GAR decay comparison\",\n        \"columns\": [\n          \"Turn\",\n          \"Qwen-2.5-7B GAR\",\n          \"Llama-3.1-8B GAR\"\n        ],\n        \"description\": \"逐 turn 对比两个模型的 base GAR 衰减。\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama-3 的 GAR 衰减方向与 Qwen 一致，但幅度约为一半。这意味着 C1（GAR 衰减是结构性现象）在方向上得到跨模型验证，但\\\"严重\\\"（70.8%）这个修饰词 只能 claim 在 Qwen 上。Llama 的 40.8% 衰减仍有统计意义但不够 dramatic， 论文需报告为\\\"中等程度衰减\\\"。这影响了后续实验的预期：较弱的 base 衰减 意味着 gating 干预的潜在空间更小，可能导致效应更难检测。\\n\\n\\nMedian 档预测 Llama-3 base GAR 衰减存在但较弱（raw drop 30-50%）。这里取 40.8%（在 [0.3, 0.5] 范围内）。Llama-3 架构与 Qwen-2.5 的关键差异包括 GQA（grouped query attention）vs MHA、不同的 positional encoding 实现（RoPE 参数不同）、以及不同的预训练数据分布。GQA 的 KV 共享机制可能 使得 goal token 的 attention 信号在 key-value 压缩后更持久，因为多个 query head 共享同一组 KV，减少了 attention pattern 的碎片化。此外 Llama-3 的 预训练可能包含更多多轮对话数据（Meta 的 RLHF 数据），使模型对 system prompt 的注意力衰减更慢。衰减方向一致（单调递减）但幅度约为 Qwen 的 一半，且衰减曲线更平缓（非陡降后平台，而是渐进式下降）。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B ThreadGate v7 Training\",\n    \"description\": \"在 Llama-3.1-8B 上复制 Qwen 的 ThreadGate v7 训练设置（MSE+gate_div loss）， 验证训练-推理 GAR gap 是否跨模型存在。\\n\",\n    \"results\": {\n      \"training_gar_converged\": 0.38,\n      \"training_gar_convergence_gs\": 180,\n      \"training_time_hours\": 7.2,\n      \"final_avg_ntp\": 0.92,\n      \"final_avg_gar\": 0.003,\n      \"final_gate_mean\": 0.945,\n      \"final_gate_std\": 0.038,\n      \"final_gate_min\": 0.82,\n      \"final_gate_max\": 0.99,\n      \"eval_dongre_mid_gar\": 0.038,\n      \"eval_dongre_turn1_gar\": 0.052,\n      \"eval_ours_mid_gar\": 0.42,\n      \"eval_ours_turn1_gar\": 0.46,\n      \"train_infer_gap_ratio_dongre\": 10.0,\n      \"train_infer_gap_ratio_ours\": 0.9,\n      \"gate_direction\": \"WRONG: same reverse turn conditioning as Qwen but less pronounced\",\n      \"gate_top5_diff_range\": [\n        -0.12,\n        -0.06\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-model training-inference gap comparison\",\n        \"columns\": [\n          \"Metric\",\n          \"Qwen-2.5-7B\",\n          \"Llama-3.1-8B\"\n        ],\n        \"description\": \"训练 GAR、推理 GAR、gap ratio、gate profile 的双模型对比。\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"10x gap 仍然是定量上显著的 distribution shift 证据，但无法与 Qwen 的 30x 等量齐观。论文中 SP1 的 \\\"30x gap\\\" 只能 claim 在 Qwen 上；Llama 需单独 报告为 \\\"10x gap\\\"。C2 的跨模型表述从\\\"训练-推理 GAR gap 是普遍现象\\\"调整为 \\\"gap 方向一致，幅度与架构相关（Qwen 30x, Llama 10x）\\\"。\\n\\n\\nMedian 档预测训练-推理 gap 存在但较小（8-15x vs Qwen 30x）。取 10x。 训练端 GAR 收敛值略低于 Qwen（0.38 vs 0.48），因为 Llama-3 的 GQA 架构 使得 attention head 间的耦合更强——同一组 KV 被多个 query head 共享， MSE target 推动的 attention redistribution 受到更多约束。收敛也更慢 （gs180 vs gs144），反映优化 landscape 的差异。推理时 GAR=0.038 显著高于 Qwen 的 0.016，这与 base model 的更高 base GAR（0.022 vs 0.012）一致—— Llama 的 attention 本底就更多分配给 goal token，gating 后的推理 GAR 也相应更高。10x gap（0.38/0.038）虽然远小于 Qwen 的 30x（0.48/0.016）， 但方向完全一致：训练时有效的 GAR 优化在推理时大幅衰减。Gate 反向 turn conditioning 存在但幅度更小（diff -0.06~-0.12 vs Qwen -0.11~-0.21）， 符合\\\"pattern 一致但不如 Qwen 干净\\\"的预期。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B LoRA-only Training\",\n    \"description\": \"在 Llama-3.1-8B 上训练 LoRA-only baseline（无 gate，无 GAR loss）， 用于与 TG 对比隔离 gating 机制的增量贡献。\\n\",\n    \"results\": {\n      \"epochs_completed\": 3,\n      \"global_steps\": 3000,\n      \"training_time_hours\": 7.0,\n      \"final_lora_size_mb\": 22,\n      \"gate_fixed\": 1,\n      \"gate_type_actual\": \"none\",\n      \"final_avg_ntp\": 0.93\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"标准训练，无特殊发现。关键作用是作为 plan_012 的 baseline。\\n\\n\\nLoRA-only 训练是标准的 NTP fine-tuning，无 GAR 目标，无 gate 参数。 Llama-3.1-8B 有 32 层（vs Qwen 28 层），LoRA 参数量略大（22MB vs 20MB）。 训练时间因模型稍大而略长。NTP loss 收敛值与 Qwen 的 LoRA-only 类似 （0.93 vs 0.95），因为两者都在相同的 UltraChat 数据上做 NTP fine-tuning。 这个实验本身没有新的 insight，纯粹是 plan_012 三路 eval 的前置依赖。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B 3-way Eval\",\n    \"description\": \"在 held-out data 上对 Llama-3.1-8B 的 Base/TG/LoRA-only 三路模型做 GAR + PPL 评估，验证 gating 增量贡献是否跨模型为零。\\n\",\n    \"results\": {\n      \"base_dongre_mid_gar\": 0.0045,\n      \"base_ppl\": 4.5,\n      \"base_ntp\": 1.45,\n      \"tg_dongre_mid_gar\": 0.038,\n      \"tg_ppl\": 2.85,\n      \"tg_ntp\": 0.96,\n      \"lora_dongre_mid_gar\": 0.022,\n      \"lora_ppl\": 2.83,\n      \"lora_ntp\": 0.95,\n      \"tg_vs_lora_dongre_gar_diff_pp\": 1.6,\n      \"tg_vs_lora_ppl_diff\": 0.02,\n      \"gating_incremental_benefit\": \"marginal_positive_but_noisy\",\n      \"tg_ours_mid_gar\": 0.42,\n      \"lora_ours_mid_gar\": 0.4,\n      \"tg_vs_lora_ours_gar_diff_pp\": 2.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Llama-3.1-8B 3-way eval results\",\n        \"columns\": [\n          \"Model\",\n          \"GAR-Dongre mid\",\n          \"GAR-ours mid\",\n          \"PPL\",\n          \"NTP\"\n        ],\n        \"description\": \"Base/TG/LoRA-only 三路评估结果。\"\n      },\n      {\n        \"name\": \"Table: Cross-model gating increment comparison\",\n        \"columns\": [\n          \"Metric\",\n          \"Qwen (TG-LO)\",\n          \"Llama (TG-LO)\"\n        ],\n        \"description\": \"双模型 gating 增量对比。Qwen <0.6pp vs Llama 1.6pp。\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama 上 TG vs LoRA-only 差异更大（1.6pp vs <0.6pp）使得 C4（gating 无 增量贡献）的跨模型表述需要 nuance。在 Qwen 上可以 claim \\\"zero benefit\\\"， 在 Llama 上只能 claim \\\"marginal and inconsistent benefit\\\"。论文需承认 \\\"gating 在不同架构上的残余效应幅度不同\\\"，并解释可能的架构原因（GQA 的 KV 共享使部分 attention redistribution 在推理时更持久）。\\n\\n\\nMedian 档预测 TG vs LoRA-only 差异在 1-3pp 范围，取 1.6pp（Dongre 定义）。 这比 Qwen 的 <0.6pp 差异更大，关键原因是 Llama 的 base GAR 本底更高 （0.022 vs 0.012），且 10x 的训练-推理 gap 比 Qwen 的 30x 更小——TG 在推理时保留了更多训练效果（虽然仍大幅衰减）。1.6pp 差异在 50 条对话 的 held-out eval 中可能在统计边缘（取决于方差），不足以 claim \\\"gating 有明确增量贡献\\\"，但也不像 Qwen 那样干净地 claim \\\"zero benefit\\\"。 这正是 median 档的核心困难：Llama 的结果不彻底否定也不彻底支持 gating， 只能描述为\\\"方向一致但效应更弱且差异更大\\\"。PPL 差异微小（0.02），仍然 支持\\\"gating 不影响语言建模质量\\\"。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B Gradient Conflict Analysis\",\n    \"description\": \"在 Llama-3.1-8B TG v7 的 checkpoints 上计算 NTP vs GAR 梯度冲突， 验证梯度竞争是否跨模型存在。\\n\",\n    \"results\": {\n      \"epoch0_cos_sim_mean\": -0.052,\n      \"epoch0_cos_sim_conflict_layer_pct\": 0.63,\n      \"epoch0_mag_ratio_mean\": 5.2,\n      \"epoch2_cos_sim_mean\": -0.028,\n      \"epoch2_cos_sim_conflict_layer_pct\": 0.56,\n      \"epoch2_mag_ratio_mean\": 6.8,\n      \"epoch2_mag_ratio_max\": 420,\n      \"positive_cos_sim_layers\": [\n        3,\n        7,\n        12,\n        15,\n        18,\n        20,\n        24,\n        28,\n        30,\n        31\n      ],\n      \"positive_cos_sim_layer_count\": 10,\n      \"cos_sim_range\": [\n        -0.058,\n        0.018\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-model gradient conflict comparison\",\n        \"columns\": [\n          \"Metric\",\n          \"Qwen-2.5-7B\",\n          \"Llama-3.1-8B\"\n        ],\n        \"description\": \"cos_sim mean, conflict pct, mag_ratio 双模型对比。\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"部分层 cos_sim 正值是 median 档的关键麻烦点。论文无法 claim 梯度冲突是 \\\"所有层的 universal pattern\\\"，只能说\\\"大多数层存在冲突，少数层因 GQA 的 KV 共享出现协同\\\"。这削弱了 SP2 的力度，但不完全否定——梯度冲突仍是 主导 pattern（56-63% 层），且 NTP 幅度仍全面压制 GAR（mag_ratio 5-7x）。\\n\\n\\nMedian 档预测 cos_sim 在 [-0.06, 0.02] 范围，mag_ratio 在 [3, 8] 范围。 Llama 的梯度冲突存在但 pattern 不完全一致——约 56-63% 的层有方向冲突 （vs Qwen 67-79%），且有约 10/32 层显示正 cos_sim（协同而非冲突）。 这是 GQA 架构的结果：共享的 KV 使得某些层中 NTP 和 GAR 梯度方向意外 对齐（优化 NTP 的 KV 更新恰好也有利于 goal token attention）。mag_ratio 仍然倾向 NTP（5-7x），但远不如 Qwen 极端（7.5-14.7x）。最高层的 max ratio 420（vs Qwen 1139x）也反映了更温和的梯度支配。 这意味着 C3（NTP-GAR 梯度竞争导致 gate 反向学习）在 Llama 上是 \\\"存在但不完全一致\\\"——方向冲突在大多数层成立，但有足够多的例外层 使得 pattern 不如 Qwen 干净。论文需要从\\\"梯度冲突是 universal mechanism\\\" 弱化为\\\"梯度冲突是 dominant mechanism in Qwen, partially replicated in Llama\\\"。\\n\"\n  },\n  {\n    \"name\": \"Downstream Task Sanity Check\",\n    \"description\": \"简单下游任务验证：测试 system prompt 中设定的 instruction（如角色扮演、 格式要求）在多轮对话中的保持率，将 GAR 与 task-level metric 关联。\\n\",\n    \"results\": {\n      \"base_instruction_retention_turn1\": 0.82,\n      \"base_instruction_retention_turn10\": 0.68,\n      \"base_instruction_retention_turn21\": 0.55,\n      \"tg_instruction_retention_turn1\": 0.83,\n      \"tg_instruction_retention_turn10\": 0.69,\n      \"tg_instruction_retention_turn21\": 0.56,\n      \"lora_instruction_retention_turn1\": 0.83,\n      \"lora_instruction_retention_turn10\": 0.69,\n      \"lora_instruction_retention_turn21\": 0.55,\n      \"gar_retention_correlation\": 0.72,\n      \"cross_model_retention_diff_pp\": \"<1.5\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Instruction retention vs GAR across turns\",\n        \"columns\": [\n          \"Turn\",\n          \"Base GAR\",\n          \"Base Retention\",\n          \"TG GAR\",\n          \"TG Retention\"\n        ],\n        \"description\": \"GAR 与 instruction retention 的逐 turn 对比。\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"GAR 与下游 instruction retention 的正相关（r≈0.72）为 GAR 作为代理指标 提供了必要的验证。论文可以声明\\\"GAR 衰减不仅是 attention 层面的现象， 而且与可观测的 task performance 下降相关\\\"。但注意相关系数不极高（不是 0.95+），说明 GAR 只是影响 instruction following 的因素之一。\\n\\n\\nInstruction retention rate 随 turn 下降与 GAR 衰减方向一致（相关系数 ~0.72），提供了 GAR 作为代理指标的 face validity。但三个训练变体之间 几乎无差异（<1.5pp），与推理 GAR 的一致性一致——gating 不改善推理时的 attention pattern，自然也不改善下游 instruction following。这个实验的 价值主要是回应 W3（GAR 作为唯一代理指标的担忧），证明 GAR 衰减确实 对应 task performance 下降，而非仅仅是一个无关的 attention 统计量。 Base model retention 从 82% 降到 55%（27pp 下降），与 GAR 70.8% 下降 幅度不完全一致，但方向一致。\\n\"\n  },\n  {\n    \"name\": \"Bootstrap CI Statistical Significance\",\n    \"description\": \"对 held-out eval（50 conversations）的 TG vs LoRA-only GAR 差异做 paired bootstrap confidence interval，检验\\\"zero benefit\\\"假设。\\n\",\n    \"results\": {\n      \"qwen_tg_lora_dongre_gar_diff_mean\": 0.002,\n      \"qwen_tg_lora_dongre_gar_diff_ci95_lower\": -0.018,\n      \"qwen_tg_lora_dongre_gar_diff_ci95_upper\": 0.022,\n      \"qwen_ci_includes_zero\": true,\n      \"qwen_bootstrap_p_value\": 0.42,\n      \"qwen_effect_size_cohens_d\": 0.05,\n      \"llama_tg_lora_dongre_gar_diff_mean\": 0.016,\n      \"llama_tg_lora_dongre_gar_diff_ci95_lower\": -0.008,\n      \"llama_tg_lora_dongre_gar_diff_ci95_upper\": 0.041,\n      \"llama_ci_includes_zero\": true,\n      \"llama_ci_width\": 0.049,\n      \"llama_bootstrap_p_value\": 0.12,\n      \"llama_effect_size_cohens_d\": 0.22,\n      \"bootstrap_iterations\": 10000\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Bootstrap CI summary (TG vs LoRA-only, Dongre GAR)\",\n        \"columns\": [\n          \"Model\",\n          \"Mean diff\",\n          \"95% CI lower\",\n          \"95% CI upper\",\n          \"p-value\",\n          \"Cohen's d\"\n        ],\n        \"description\": \"Qwen 和 Llama 的 bootstrap CI 对比。\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen 的结果干净地支持 C4（zero benefit）。Llama 的结果是 median 档的 典型 ambiguity：无法拒绝零假设，但也无法确信排除小正效应。论文需在 Results 中分别报告两个模型的 CI，并在 Discussion 中解释\\\"Llama 的更宽 CI 可能反映更高的 base GAR 方差或更弱但非零的 gating 残余效应\\\"。 追加 1-2 个 seed 可以缩窄 CI，但在 median 档下即使追加 seed 也只是 将 p 从 0.12 推到 0.07-0.09 附近，仍然 marginal。\\n\\n\\nQwen 的 CI 紧且对称（[-0.018, 0.022]），含 0，p=0.42，效应量极小 （d=0.05）——统计上强支持\\\"zero benefit\\\"。这与 held-out eval 中 TG-LO 差异<0.6pp 一致。 Llama 的 CI 更宽（[-0.008, 0.041]，宽度 0.049 vs Qwen 0.040）， 仍含 0 但偏正（均值 0.016），p=0.12。这是 median 档的关键特征： CI 包含 0（技术上无法拒绝零假设），但宽度较大且偏向正方向，意味着 可能存在微小正效应但 50 条对话的 power 不足以检测。效应量 d=0.22 是\\\"小效应\\\"，统计学上 marginal。论文的表述需要是\\\"CI includes 0, consistent with zero or small positive benefit\\\"，而非 Qwen 那样 干净的\\\"statistically confirms zero benefit\\\"。\\n\"\n  },\n  {\n    \"name\": \"Exposure-Bias Mitigation (Scheduled Sampling)\",\n    \"description\": \"在 ThreadGate v7 训练中引入 scheduled sampling：以递增概率用模型自身 生成的 context 替换 teacher-forced context，使 GAR loss 在更接近推理时 分布的 context 上优化。测试能否缩小 30x 训练-推理 GAR gap。\\n\",\n    \"results\": {\n      \"qwen_ss_training_gar_converged\": 0.32,\n      \"qwen_ss_training_gar_lower_than_tf\": true,\n      \"qwen_ss_training_time_hours\": 9.5,\n      \"qwen_ss_eval_dongre_mid_gar\": 0.026,\n      \"qwen_ss_eval_ours_mid_gar\": 0.35,\n      \"qwen_ss_train_infer_gap_ratio\": 12.3,\n      \"qwen_ss_gap_reduction_vs_tf\": 2.44,\n      \"qwen_ss_gap_reduction_factor\": 1.6,\n      \"qwen_ss_ppl\": 2.72,\n      \"qwen_ss_vs_lora_dongre_gar_diff_pp\": 1.24,\n      \"qwen_ss_gate_mean\": 0.918,\n      \"qwen_ss_gate_direction\": \"MIXED: 15/28 layers still show reverse conditioning, 13/28 show correct or neutral\",\n      \"qwen_ss_vs_tf_bootstrap_p\": 0.07,\n      \"qwen_ss_vs_tf_ci95_lower\": -0.003,\n      \"qwen_ss_vs_tf_ci95_upper\": 0.023,\n      \"qwen_ss_vs_tf_ci_includes_zero\": true,\n      \"ss_sampling_schedule\": \"linear 0→0.5 over epoch 0-1, fixed 0.5 epoch 2\",\n      \"ss_convergence_slower\": true,\n      \"ss_convergence_gs\": 210,\n      \"ss_training_instability\": \"mild oscillation in GAR loss during high sampling ratio\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Mitigation comparison (Teacher-forcing vs Scheduled Sampling)\",\n        \"columns\": [\n          \"Metric\",\n          \"TF (v7)\",\n          \"SS\",\n          \"Δ\"\n        ],\n        \"description\": \"训练 GAR、推理 GAR、gap ratio、PPL、gate direction 的 TF vs SS 对比。\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scheduled sampling 展示了方向正确但幅度不足的改善。Gap 从 30x 缩小到 12.3x 说明 exposure bias 确实是 training-inference gap 的部分原因，但 即使缩小后 gap 仍然巨大（12.3x），说明 distribution shift 不仅仅来自 teacher-forcing vs autoregressive 的差异——可能还有 NTP 梯度压制、 训练数据长度分布等其他因素。\\n统计上 marginal 的结果（p≈0.07，CI 含 0）意味着这个实验无法作为 独立的 positive claim，但可以作为 Discussion 中的 constructive evidence： \\\"scheduled sampling shows a suggestive but statistically inconclusive trend toward gap reduction, consistent with exposure bias being a contributing factor\\\"。\\n论文策略：mitigation 结果降级到 Discussion section 作为 suggestive evidence，不放入 core claims。标题保持 negative result 基调。 如果追加 seed 或更大 eval set 能将 p 推到 <0.05，可以升级为 minor finding，但在 median 档下不太可能。\\n\\nMedian 档预测 mitigation 将 gap 缩小 1.2-2.0x（取 1.6x），post-inference GAR 在 0.02-0.04 范围（取 0.026）。\\nScheduled sampling 的逻辑是正确的：在训练时混入 model-generated context 缩小 teacher-forcing 与 autoregressive generation 的分布差异。但在实践中 效果受限于几个因素：\\n(1) 训练 GAR 收敛值降低（0.32 vs TF 的 0.48），因为 model-generated context 引入噪声，GAR target 更难达到。模型在\\\"混乱\\\"的 context 上 优化 attention 更困难。\\n(2) 推理 GAR 确实提高（0.026 vs TF 的 0.016），说明部分 attention pattern 确实在更接近推理分布的 context 上得到了更好的泛化。但提升 幅度有限——从 0.016 到 0.026 只是 62.5% 相对提升，绝对值仍然极低。\\n(3) Gap 从 30x 缩小到 12.3x（reduction factor 1.6x 在 [1.2, 2.0] 范围内），方向正确但幅度不够 convincing。12.3x 的 gap 仍然意味着 推理时 attention pattern 与训练时有一个数量级的差异。\\n(4) 统计上 marginal：SS vs TF 的推理 GAR 差异 bootstrap p≈0.07， CI 包含 0（[-0.003, 0.023]）。在 conventional α=0.05 下无法拒绝 零假设，但方向一致（正效应）。这正是\\\"结果模糊\\\"的定义：有 suggestive evidence 但不够 conclusive。\\n(5) Gate direction 部分修正（13/28 层不再反向 conditioning），说明 SS 确实改善了 gradient conflict 的某些方面，但未完全解决。\\n(6) 训练更慢更不稳定（9.5h vs 5.9h），收敛需要更多 steps（gs210 vs gs144），GAR loss 在高 sampling ratio 时有震荡。这是 exposure bias mitigation 方法的已知代价（Bengio et al. 2015）。\\n\"\n  }\n]",
      "numLines": 351,
      "startLine": 1,
      "totalLines": 351
    }
  },
  "sourceToolAssistantUUID": "deb7a4cb-d6f9-484a-9582-5c9af187ad39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T145320 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_g…",
  "leafUuid": "6f6d009f-b37b-4999-8e0f-edcb7ffd19eb",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396"
}
```

---

### Assistant

_source line 17 · 2026-05-19T15:14:17.143Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the paper writing norms skill to ensure I follow proper academic writing conventions.

Actually, the user asked me not to go through a pipeline, and to write the paper directly. Let me also check if there's a LaTeX template or existing structure I should follow.

Let me now synthesize the experiment data and paper framing to write a complete LaTeX paper. Let me organize the data:

**Experiments:**

1. **Qwen Gradient Conflict Analysis** - 3 checkpoints, cos_sim and mag_ratio data
2. **Attention Heatmap Visualization** - 4 models, showing attention patterns indistinguishable at inference


3. **Llama-3.1-8B Phase 1 GAR Degradation** - base GAR decay ~40.8%
4. **Llama-3.1-8B ThreadGate v7 Training** - 10x gap (vs Qwen 30x)
5. **Llama-3.1-8B LoRA-only Training** - baseline
6. **Llama-3.1-8B 3-way Eval** - TG vs LoRA diff 1.6pp
7. **Llama-3.1-8B Gradient Conflict** - partial cos_sim positive layers

I've got the full set of experiments mapped out across both Qwen and Llama models, covering gradient conflicts, attention patterns, training degradation, and comparative evaluations. Looking at the gradient dynamics and gate behavior across turns, I'm seeing consistent degradation patterns—the cosine similarity shifts toward more negative values while magnitude ratios expand significantly, and nearly all layers show declining gate values from early to late turns. Now I'm ready to structure the paper with the corrected ReZero formulation and the refined title emphasizing why gating mechanisms struggle rather than completely fail at addressing this multi-turn attention problem.

For the experimental validation, I'm planning a comprehensive set of tables that will systematically demonstrate the core findings: how GAR decays across turns in different base models, where the training-inference gap emerges when applying ThreadGate, the comparative performance across different mitigation strategies on both Qwen and Llama, and the underlying gradient conflicts and instruction retention patterns that explain why lightweight gating alone isn't sufficient.

Now I need to finalize the paper structure and set up the LaTeX formatting to present these results clearly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f6d009f-b37b-4999-8e0f-edcb7ffd19eb",
  "isSidechain": false,
  "requestId": "req_011CbC9N5mYUYXiauX4ebcuF",
  "type": "assistant",
  "uuid": "ee2fa228-7d63-435f-9040-bbaabf5de08c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ux2anV8bLDMoqtD3jPa7G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6780,
      "cache_creation_input_tokens": 10768,
      "cache_read_input_tokens": 23686,
      "output_tokens": 1301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6780,
          "output_tokens": 1301,
          "cache_read_input_tokens": 23686,
          "cache_creation_input_tokens": 10768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10768
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

_source line 18 · 2026-05-19T15:14:17.395Z_

Let me check for available LaTeX templates and the output directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee2fa228-7d63-435f-9040-bbaabf5de08c",
  "isSidechain": false,
  "requestId": "req_011CbC9N5mYUYXiauX4ebcuF",
  "type": "assistant",
  "uuid": "c08eed86-cd88-4952-a6b0-c78389fa42e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ux2anV8bLDMoqtD3jPa7G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6780,
      "cache_creation_input_tokens": 10768,
      "cache_read_input_tokens": 23686,
      "output_tokens": 1301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6780,
          "output_tokens": 1301,
          "cache_read_input_tokens": 23686,
          "cache_creation_input_tokens": 10768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10768
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

_source line 19 · 2026-05-19T15:14:19.756Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KmcYXQFnbG4UuPy9MpLsEB`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/ 2>/dev/null",
  "description": "List median dream report directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c08eed86-cd88-4952-a6b0-c78389fa42e8",
  "isSidechain": false,
  "requestId": "req_011CbC9N5mYUYXiauX4ebcuF",
  "type": "assistant",
  "uuid": "b2b91d2b-f30b-4483-b6ba-6a8951b239b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ux2anV8bLDMoqtD3jPa7G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6780,
      "cache_creation_input_tokens": 10768,
      "cache_read_input_tokens": 23686,
      "output_tokens": 1301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6780,
          "output_tokens": 1301,
          "cache_read_input_tokens": 23686,
          "cache_creation_input_tokens": 10768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10768
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

_source line 20 · 2026-05-19T15:14:19.919Z_

<details><summary>↩ Tool result · `toolu_01KmcYXQFnbG4UuPy9MpLsEB`</summary>

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
  "parentUuid": "b2b91d2b-f30b-4483-b6ba-6a8951b239b5",
  "isSidechain": false,
  "promptId": "60b11cf6-cc2f-4f15-8815-d9e57690cbb7",
  "type": "user",
  "uuid": "7c39d6ab-fe33-4e88-ac0d-5e6e7678e6e3",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b2b91d2b-f30b-4483-b6ba-6a8951b239b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T15:14:21.336Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014w92TSRUVqBha98GRGrysf`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating -name \"acl*.sty\" -o -name \"acl*.cls\" -o -name \"emnlp*.sty\" 2>/dev/null | head -5; which pdflatex 2>/dev/null",
  "description": "Find ACL/EMNLP style files and check pdflatex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c39d6ab-fe33-4e88-ac0d-5e6e7678e6e3",
  "isSidechain": false,
  "requestId": "req_011CbC9N5mYUYXiauX4ebcuF",
  "type": "assistant",
  "uuid": "f798e652-2b1e-4ad1-a0d3-3c7466087553",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ux2anV8bLDMoqtD3jPa7G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6780,
      "cache_creation_input_tokens": 10768,
      "cache_read_input_tokens": 23686,
      "output_tokens": 1301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6780,
          "output_tokens": 1301,
          "cache_read_input_tokens": 23686,
          "cache_creation_input_tokens": 10768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10768
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

_source line 22 · 2026-05-19T15:14:21.414Z_

<details><summary>↩ Tool result · `toolu_014w92TSRUVqBha98GRGrysf`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/acl.sty
/usr/bin/pdflatex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f798e652-2b1e-4ad1-a0d3-3c7466087553",
  "isSidechain": false,
  "promptId": "60b11cf6-cc2f-4f15-8815-d9e57690cbb7",
  "type": "user",
  "uuid": "48569bf0-5877-459c-9297-af499c205e54",
  "toolUseResult": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/acl.sty\n/usr/bin/pdflatex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f798e652-2b1e-4ad1-a0d3-3c7466087553",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T15:14:25.638Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ctaf83TbfKCkW4ixw1pQji`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/acl* 2>/dev/null",
  "description": "Check ACL style files in best directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48569bf0-5877-459c-9297-af499c205e54",
  "isSidechain": false,
  "requestId": "req_011CbC9Qb7wpk8tQ22svhdPc",
  "type": "assistant",
  "uuid": "2c6f0bd3-d6af-47b9-a9b4-0880e14d926c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WLcPRg2PyTSpW6rGiQtHiR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8216,
      "cache_read_input_tokens": 34454,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8216,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 34454,
          "cache_creation_input_tokens": 8216,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8216
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

_source line 24 · 2026-05-19T15:14:25.683Z_

<details><summary>↩ Tool result · `toolu_01Ctaf83TbfKCkW4ixw1pQji`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/acl_natbib.bst
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c6f0bd3-d6af-47b9-a9b4-0880e14d926c",
  "isSidechain": false,
  "promptId": "60b11cf6-cc2f-4f15-8815-d9e57690cbb7",
  "type": "user",
  "uuid": "39e669a6-c5c5-444a-bb31-e6f84c53c9fc",
  "toolUseResult": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/acl.sty\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/acl_natbib.bst",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2c6f0bd3-d6af-47b9-a9b4-0880e14d926c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T15:14:29.254Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EEYtrkpt2YyWwZ2G2cmKKc`</summary>

```json
{
  "command": "head -30 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/acl.sty",
  "description": "Check ACL style file header"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39e669a6-c5c5-444a-bb31-e6f84c53c9fc",
  "isSidechain": false,
  "requestId": "req_011CbC9QuRmbam3wjZ5DX9Bx",
  "type": "assistant",
  "uuid": "2d5fa13a-41e0-47cf-a45f-fabf7353bddf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AzKfk57jJzAvhvmDJ5x7Se",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 252,
      "cache_read_input_tokens": 42670,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 42670,
          "cache_creation_input_tokens": 252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 252
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

_source line 26 · 2026-05-19T15:14:29.304Z_

<details><summary>↩ Tool result · `toolu_01EEYtrkpt2YyWwZ2G2cmKKc`</summary>

```text
% This is the LaTex style file for *ACL.
% The official sources can be found at
%
%     https://github.com/acl-org/acl-style-files/
%
% This package is activated by adding
%
%    \usepackage{acl}
%
% to your LaTeX file. When submitting your paper for review, add the "review" option:
%
%    \usepackage[review]{acl}

\newif\ifacl@finalcopy
\newif\ifacl@anonymize
\newif\ifacl@linenumbers
\newif\ifacl@pagenumbers
\DeclareOption{final}{\acl@finalcopytrue\acl@anonymizefalse\acl@linenumbersfalse\acl@pagenumbersfalse}
\DeclareOption{review}{\acl@finalcopyfalse\acl@anonymizetrue\acl@linenumberstrue\acl@pagenumberstrue}
\DeclareOption{preprint}{\acl@finalcopytrue\acl@anonymizefalse\acl@linenumbersfalse\acl@pagenumberstrue}
\ExecuteOptions{final} % final copy is the default

% include hyperref, unless user specifies nohyperref option like this:
% \usepackage[nohyperref]{acl}
\newif\ifacl@hyperref
\DeclareOption{hyperref}{\acl@hyperreftrue}
\DeclareOption{nohyperref}{\acl@hyperreffalse}
\ExecuteOptions{hyperref} % default is to use hyperref
\ProcessOptions\relax
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d5fa13a-41e0-47cf-a45f-fabf7353bddf",
  "isSidechain": false,
  "promptId": "60b11cf6-cc2f-4f15-8815-d9e57690cbb7",
  "type": "user",
  "uuid": "d1a7e04c-1b4b-43d8-bce0-f9c6e72bd9b4",
  "toolUseResult": {
    "stdout": "% This is the LaTex style file for *ACL.\n% The official sources can be found at\n%\n%     https://github.com/acl-org/acl-style-files/\n%\n% This package is activated by adding\n%\n%    \\usepackage{acl}\n%\n% to your LaTeX file. When submitting your paper for review, add the \"review\" option:\n%\n%    \\usepackage[review]{acl}\n\n\\newif\\ifacl@finalcopy\n\\newif\\ifacl@anonymize\n\\newif\\ifacl@linenumbers\n\\newif\\ifacl@pagenumbers\n\\DeclareOption{final}{\\acl@finalcopytrue\\acl@anonymizefalse\\acl@linenumbersfalse\\acl@pagenumbersfalse}\n\\DeclareOption{review}{\\acl@finalcopyfalse\\acl@anonymizetrue\\acl@linenumberstrue\\acl@pagenumberstrue}\n\\DeclareOption{preprint}{\\acl@finalcopytrue\\acl@anonymizefalse\\acl@linenumbersfalse\\acl@pagenumberstrue}\n\\ExecuteOptions{final} % final copy is the default\n\n% include hyperref, unless user specifies nohyperref option like this:\n% \\usepackage[nohyperref]{acl}\n\\newif\\ifacl@hyperref\n\\DeclareOption{hyperref}{\\acl@hyperreftrue}\n\\DeclareOption{nohyperref}{\\acl@hyperreffalse}\n\\ExecuteOptions{hyperref} % default is to use hyperref\n\\ProcessOptions\\relax",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2d5fa13a-41e0-47cf-a45f-fabf7353bddf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T15:14:34.343Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AFytbLQeKCAtnmgEpJsbDg`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/acl.sty /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/acl.sty && cp /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/acl_natbib.bst /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/acl_natbib.bst 2>/dev/null; echo \"done\"",
  "description": "Copy ACL style files to median directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1a7e04c-1b4b-43d8-bce0-f9c6e72bd9b4",
  "isSidechain": false,
  "requestId": "req_011CbC9RBfLEtYx9ajarhgcA",
  "type": "assistant",
  "uuid": "12fc225a-99df-4c3b-a36d-d7cf5291c2d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5WrweTo3dyfzj3qt5hJsW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 558,
      "cache_read_input_tokens": 42922,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 558,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 305,
          "cache_read_input_tokens": 42922,
          "cache_creation_input_tokens": 558,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 558
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

_source line 28 · 2026-05-19T15:14:34.410Z_

<details><summary>↩ Tool result · `toolu_01AFytbLQeKCAtnmgEpJsbDg`</summary>

```text
done
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12fc225a-99df-4c3b-a36d-d7cf5291c2d0",
  "isSidechain": false,
  "promptId": "60b11cf6-cc2f-4f15-8815-d9e57690cbb7",
  "type": "user",
  "uuid": "887bb02e-d879-4d75-8d3e-a20d92afd498",
  "toolUseResult": {
    "stdout": "done",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "12fc225a-99df-4c3b-a36d-d7cf5291c2d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-19T15:15:16.915Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me write the full LaTeX paper. I need to carefully incorporate all experiment data and follow the narrative guidance.

Key data points I need to include:

**Qwen-2.5-7B experiments (from framing doc + experiment_data.json):**
- Base GAR decay: 70.8% raw
- TG training GAR: 0.48, inference GAR: 0.016, gap: 30x
- 4-way eval: TG 0.487, UG 0.492, LO 0.486 (GAR); PPL TG 2.63, UG 2.62, LO 2.63, Base 4.23


- Gate means consistently high (0.93-0.98) with negative drift across most layers, showing gradient conflicts intensifying from cosine similarity of -0.089 to -0.042 and magnitude ratios ballooning from 7.5x to 14.7x, with layer 27 reaching extreme 135x to 1139x scaling.

**Llama-3.1-8B experiments:**
- Base GAR decay: 40.8% (turn1 0.038 → mid 0.0225)
- TG training GAR: 0.38, inference GAR: 0.038, gap: 10x
- Gate mean: 0.945

For the three-way evaluation, I'm seeing TG outperforms base significantly (0.038 vs 0.0045 GAR, 2.85 vs 4.5 PPL) while LO achieves similar perplexity with slightly lower GAR, creating only a 1.6 percentage point gap between them. The gradient analysis shows conflict decreasing from 63% to 56% of layers, with cosine similarity improving from -0.052 to -0.028, though magnitude ratios still climb from 5.2 to 6.8 with peaks at 420. Cross-model bootstrap confidence intervals suggest the effects aren't statistically significant for either Qwen (p=0.42) or Llama (p=0.12), though Llama shows a larger effect size. I'm now looking at scheduled sampling as a potential mitigation strategy.

With scheduled sampling applied to Qwen, training GAR drops to 0.32 compared to the teacher forcing baseline of 0.48, but inference GAR actually increases to 0.026 versus 0.016—reducing the train-inference gap from 30x down to 12.3x with a 1.6x improvement factor. The gate directions become more mixed across layers, and the bootstrap p-value climbs to 0.07 with a confidence interval that includes zero. Downstream instruction retention shows the base model maintains 82% accuracy on turn 1 but degrades to 55% by turn 21, with TG and LO performing nearly identically. The attention heatmaps across all four models look indistinguishable at inference, suggesting the gating mechanism isn't creating meaningful attention pattern differences.

The narrative guidance pushes toward framing this as a struggle rather than a failure—Llama shows directional consistency but weaker effects overall, and the mitigation remains suggestive rather than conclusive, which belongs in the discussion. The title should shift from "Cannot" to "Struggles to," targeting EMNLP Findings. I'm settling on "Why Lightweight Gating Struggles to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis" and structuring the paper with abstract, introduction, related work, and background sections covering GAR and residual stream dynamics.

Now I'm laying out the full experimental structure: training dynamics, a four-way ablation on Qwen, cross-model validation with Llama, downstream task validation, then analysis sections covering training-inference distribution shift, gradient conflicts, gate profiles, attention visualizations, and statistical significance. The discussion will address exposure bias mitigation and future directions. I need tables for the four-way Qwen evaluation, cross-model GAR decay, training-inference gaps, Llama three-way results, and gradient conflict metrics.

For the paper itself, I'm aiming for about 8 pages of main text to hit that high-quality standard while keeping it focused and comprehensive. I should verify the core formula is correct—the ReZero-style residual connection where the next layer state equals the current state plus the gated function output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "887bb02e-d879-4d75-8d3e-a20d92afd498",
  "isSidechain": false,
  "requestId": "req_011CbC9RYe9MiVftBzYfYYws",
  "type": "assistant",
  "uuid": "7a376ea0-61b3-4ce6-91bf-31d81956a833",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Q6MfFfuit6u612NdFxQv4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 43480,
      "output_tokens": 13625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13625,
          "cache_read_input_tokens": 43480,
          "cache_creation_input_tokens": 318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 318
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

_source line 30 · 2026-05-19T15:15:17.300Z_

Now writing the full LaTeX paper. This covers all 9 experiments from the data, with proper tables, cross-model analysis, and the mitigation discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a376ea0-61b3-4ce6-91bf-31d81956a833",
  "isSidechain": false,
  "requestId": "req_011CbC9RYe9MiVftBzYfYYws",
  "type": "assistant",
  "uuid": "0627cbd5-00b4-4e2e-bfe1-768e6d003070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Q6MfFfuit6u612NdFxQv4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 43480,
      "output_tokens": 13625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13625,
          "cache_read_input_tokens": 43480,
          "cache_creation_input_tokens": 318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 318
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

_source line 31 · 2026-05-19T15:19:03.862Z_

<details open><summary>🔧 Tool call — Write · `toolu_017i39C93MLzq2K5nUoqoTmb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{tabularx}\n\\usepackage{subcaption}\n\n\\title{Why Lightweight Gating Struggles to Fix Multi-Turn Attention Degradation:\\\\A Mechanistic Analysis}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLarge language models progressively lose track of goal instructions as multi-turn dialogues grow longer.\nRecent work by \\citet{dongre2026multi} quantified this degradation through Goal Attention Ratio (GAR) and showed that goal information persists in the residual stream (probe AUC$=$0.98) even as the attention channel closes, suggesting that a learnable gate on the residual connection could recover it.\nWe test this hypothesis with ThreadGate, a per-layer gating module trained jointly with next-token prediction (NTP) and an auxiliary GAR objective.\nThreadGate successfully optimizes GAR during training (0.02$\\to$0.48 on Qwen-2.5-7B), yet this improvement fails to transfer to autoregressive inference (GAR$=$0.016, a 30$\\times$ gap).\nWe identify two coupled mechanisms behind this failure:\n(1)~NTP gradients dominate gate parameters by 7--15$\\times$ in magnitude, causing gates to learn \\emph{reverse} turn conditioning---suppressing intervention where it is most needed;\n(2)~teacher-forcing creates a distribution shift under which attention patterns learned on gold contexts do not generalize to model-generated contexts.\nFour-way ablation confirms that gating provides no statistically significant incremental benefit over LoRA-only fine-tuning (bootstrap $p{=}0.42$, Cohen's $d{=}0.05$ on Qwen).\nCross-model experiments on Llama-3.1-8B show directional consistency in all failure modes, with a 10$\\times$ training-inference gap and 1.6 percentage-point gating increment that remains statistically non-significant ($p{=}0.12$).\nA scheduled-sampling mitigation reduces the gap from 30$\\times$ to 12.3$\\times$ ($p{\\approx}0.07$), providing suggestive evidence that exposure bias is a contributing factor.\nOur results constitute the first quantitative measurement of how teacher-forcing distribution shift undermines auxiliary attention losses in lightweight residual gating, and identify the specific mechanisms through which this vulnerability manifests.\n\\end{abstract}\n\n%-------------------------------------------------------------------\n\\section{Introduction}\n%-------------------------------------------------------------------\n\nMulti-turn dialogue is the primary mode of interaction with modern large language models (LLMs), yet model performance degrades systematically as conversations grow longer \\cite{liu2024lost,xiao2024efficient,ko2024found}.\nA key manifestation is the declining adherence to goal instructions specified in the system prompt, which \\citet{dongre2026multi} quantified through the Goal Attention Ratio (GAR)---the fraction of attention mass allocated to goal-relevant tokens.\nAcross 12 models, they observed 27--48\\% GAR drops over 50 turns, establishing GAR decay as a robust structural phenomenon.\n\nA striking finding from \\citet{dongre2026multi} is that goal information \\emph{persists} in the residual stream throughout the conversation (linear probe AUC up to 0.98), even as the attention channel closes.\nThis creates a natural hypothesis: if goal information is available in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it by modulating how much each layer's computation contributes to the output.\n\nWe test this hypothesis through ThreadGate, a per-layer gating module inspired by ReZero initialization \\cite{bachlechner2021rezero} and adaptive-depth architectures \\cite{raposo2024mixture,luo2025flexidepth}.\nEach Transformer layer receives a scalar gate $g_l \\in [0,1]$ trained with a joint NTP and GAR objective.\nOver seven training configurations (v1--v7) covering four loss families, we find that MSE-based targeting with gate diversity regularization (v7) is the only configuration that achieves stable training convergence.\n\nThe central finding is negative: despite successful training-time GAR optimization (0.02$\\to$0.48), inference-time GAR remains at 0.016---a 30$\\times$ gap.\nFour-way ablation (ThreadGate / Uniform Gate / LoRA-only / Base) confirms that gating provides zero incremental contribution over standard LoRA fine-tuning.\n\nOur mechanistic analysis reveals two coupled failure modes:\n\\begin{itemize}\n\\item \\textbf{Gradient competition}: NTP loss dominates gate gradients by 7--15$\\times$ in magnitude, with 67--79\\% of layers showing opposing gradient directions (cosine similarity $-0.089$ to $-0.042$). This causes gates to learn reverse turn conditioning, becoming passive precisely at late turns where intervention is most needed.\n\\item \\textbf{Distribution shift}: Teacher-forcing trains attention patterns on gold contexts, which do not transfer to model-generated contexts at inference time. This is the well-known exposure bias \\cite{bengio2015scheduled,ranzato2016sequence}, but we provide the first quantitative measurement of its impact on auxiliary attention losses (30$\\times$ gap).\n\\end{itemize}\n\nCross-model experiments on Llama-3.1-8B demonstrate directional consistency: a 10$\\times$ training-inference gap, reverse gate conditioning, and gradient conflict in 56--63\\% of layers, though with weaker magnitudes reflecting architectural differences (GQA vs.\\ MHA).\n\nOur contributions are:\n\\begin{enumerate}\n\\item The first quantitative measurement of how teacher-forcing distribution shift undermines auxiliary attention losses in lightweight residual gating (30$\\times$ training-inference GAR gap on Qwen, 10$\\times$ on Llama).\n\\item Per-layer quantification of NTP--GAR gradient competition showing magnitude ratios of 7--15$\\times$ and systematic direction conflict.\n\\item Systematic ablation across two model families isolating the contribution of gating, LoRA fine-tuning, and loss design.\n\\item Suggestive evidence from scheduled-sampling mitigation that exposure bias is a contributing factor (gap reduction from 30$\\times$ to 12.3$\\times$, $p{\\approx}0.07$).\n\\end{enumerate}\n\n%-------------------------------------------------------------------\n\\section{Related Work}\n%-------------------------------------------------------------------\n\n\\paragraph{Multi-turn dialogue degradation.}\nPerformance loss over extended conversations has been documented across multiple dimensions.\n\\citet{liu2024lost} identify a ``lost in the middle'' effect where models struggle with information placed in the center of long contexts.\n\\citet{xiao2024efficient} analyze attention sinks---the concentration of attention on initial tokens regardless of relevance---as a contributor to context degradation.\n\\citet{ko2024found} investigate position-dependent retrieval failures in multi-turn settings.\nMT-Bench-101 \\cite{bai2024mt} and MultiChallenge \\cite{wang2024multichallenge} provide standardized benchmarks for multi-turn evaluation.\nMost directly relevant, \\citet{dongre2026multi} introduce GAR as a quantitative metric for goal attention decay, measure it across 12 models, and show through residual stream probing that goal information persists even as attention degrades.\n\n\\paragraph{Residual gating and adaptive depth.}\nReZero \\cite{bachlechner2021rezero} initializes residual connections with learnable scalars to stabilize deep network training.\nMixture-of-Depths \\cite{raposo2024mixture} and FlexiDepth \\cite{luo2025flexidepth} use per-layer gating to adaptively skip computation.\n\\citet{qiu2025gated} propose gated attention mechanisms for selective information routing.\nOur ThreadGate adopts the ReZero formulation but repurposes it for attention steering rather than training stability.\n\n\\paragraph{Attention steering and intervention.}\nAttention manipulation approaches include attention masking \\cite{zhang2024tell}, activation steering \\cite{li2024inference,turner2024activation}, and representation engineering \\cite{zou2023representation}.\n\\citet{dongre2026multi} attempt goal re-injection through residual stream manipulation (Appendix H) but report failure.\nOur work provides a complementary failure case through residual gating, and identifies the mechanistic reasons.\n\n\\paragraph{Exposure bias.}\nThe mismatch between teacher-forced training and autoregressive inference was identified by \\citet{bengio2015scheduled}, who proposed scheduled sampling as mitigation.\nSubsequent work includes Professor Forcing \\cite{lamb2016professor}, SEARNN \\cite{leblond2018searnn}, and various reinforcement learning approaches \\cite{ranzato2016sequence}.\nExposure bias is well-studied for generation quality but its impact on auxiliary loss objectives has received little attention.\nWe provide the first quantitative measurement of how this distribution shift specifically undermines auxiliary attention losses.\n\n\\paragraph{Multi-task gradient conflict.}\nGradient conflicts in multi-task learning have been studied extensively \\cite{yu2020gradient,liu2021conflict,chen2020just}.\nPCGrad \\cite{yu2020gradient} projects conflicting gradients; GradNorm \\cite{chen2018gradnorm} normalizes gradient magnitudes.\nOur gradient analysis reveals that the NTP--GAR conflict is particularly severe because NTP gradients dominate in both direction and magnitude.\n\n%-------------------------------------------------------------------\n\\section{Background}\n\\label{sec:background}\n%-------------------------------------------------------------------\n\n\\paragraph{Goal Attention Ratio (GAR).}\nFollowing \\citet{dongre2026multi}, GAR measures the fraction of attention mass allocated to goal-relevant tokens. For a response token $r$ at layer $l$ and head $h$:\n\\begin{equation}\n\\text{GAR}(r, l, h) = \\sum_{t \\in \\mathcal{G}} \\alpha_{r,t}^{(l,h)}\n\\end{equation}\nwhere $\\mathcal{G}$ is the set of goal tokens in the system prompt and $\\alpha_{r,t}^{(l,h)}$ is the attention weight.\nWe aggregate across layers, heads, and response tokens to obtain per-turn GAR values.\n\nWe employ two GAR definitions: GAR-Dongre (system prompt task tokens as goals, all response tokens) for comparability with \\citet{dongre2026multi}, and GAR-ours (system prompt + first user query as goals, last token per assistant turn) as the training signal.\nBoth definitions yield consistent negative findings.\n\n\\paragraph{Residual stream persistence.}\n\\citet{dongre2026multi} demonstrate through linear probing that goal-relevant information remains decodable from the residual stream (AUC up to 0.98) even at late conversation turns where GAR has dropped significantly.\nThis persistence motivates the hypothesis that a learnable gate on the residual connection could recover goal attention by modulating layer-wise computation.\n\n%-------------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n%-------------------------------------------------------------------\n\n\\subsection{ThreadGate Architecture}\n\nThreadGate augments each Transformer layer $l$ with a scalar gate $g_l \\in [0,1]$, modifying the residual connection as:\n\\begin{equation}\n\\mathbf{x}_{l+1} = \\mathbf{x}_l + g_l \\cdot f_l(\\mathbf{x}_l)\n\\label{eq:gate}\n\\end{equation}\nwhere $f_l$ denotes the combined self-attention and feed-forward computation of layer $l$.\nWhen $g_l \\to 0$, the layer becomes a no-op (identity mapping); when $g_l = 1$, the standard residual connection is recovered.\nGates are initialized to 1.0 (identity) and parameterized as $g_l = \\sigma(w_l)$ where $\\sigma$ is the sigmoid function and $w_l$ is an unconstrained scalar.\n\n\\subsection{Training Objective}\n\nThe v7 configuration uses a joint loss:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_{\\text{NTP}} + \\lambda_{\\text{GAR}} \\cdot \\mathcal{L}_{\\text{GAR}} + \\lambda_{\\text{div}} \\cdot \\mathcal{L}_{\\text{div}}\n\\end{equation}\n\nThe GAR component uses an MSE target that provides bidirectional gradients:\n\\begin{equation}\n\\mathcal{L}_{\\text{GAR}} = \\frac{1}{|\\mathcal{T}|} \\sum_{t \\in \\mathcal{T}} \\left( \\text{GAR}(t) - \\tau(t) \\right)^2\n\\end{equation}\nwhere $\\tau(t)$ is a per-turn target derived from the turn-1 GAR level, encouraging the model to maintain early-turn attention throughout the conversation.\n\nThe diversity term $\\mathcal{L}_{\\text{div}} = -\\text{Var}(\\{g_l\\}_{l=1}^{L})$ encourages gates to differentiate across layers rather than collapsing to a uniform value.\n\n\\subsection{Loss Design Evolution}\n\nWe explored four loss families across seven configurations:\n\\emph{cumulative} (v1--v2) accumulating GAR over turns,\n\\emph{maximize} (v3--v5) directly maximizing GAR,\n\\emph{smooth saturation} (v6) with gradient-friendly saturation curves, and\n\\emph{MSE target} (v7) with bidirectional gradients.\nOnly v7 achieved stable training convergence; earlier variants suffered from gradient vanishing (v1--v2), training instability (v3--v5), or slow convergence (v6).\n\n\\subsection{Training Setup}\n\nWe fine-tune Qwen-2.5-7B and Llama-3.1-8B using LoRA (rank 16) on UltraChat multi-turn dialogue data.\nThreadGate adds $L$ scalar parameters (28 for Qwen, 32 for Llama) on top of the LoRA parameters ($\\sim$20--22 MB).\nTraining runs for 3 epochs with learning rate $2\\times10^{-4}$, batch size 4, and seed 42.\n$\\lambda_{\\text{GAR}} = 0.1$, $\\lambda_{\\text{div}} = 0.01$.\n\n%-------------------------------------------------------------------\n\\section{Experiments}\n\\label{sec:experiments}\n%-------------------------------------------------------------------\n\n\\subsection{Phase 1: Base Model GAR Decay}\n\nWe first verify GAR decay on our target models using 5 held-out conversations of 10+ turns each.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Turn} & \\textbf{Qwen-2.5-7B} & \\textbf{Llama-3.1-8B} \\\\\n\\midrule\n1  & 0.041 & 0.038 \\\\\n2  & 0.029 & 0.031 \\\\\n3  & 0.024 & 0.030 \\\\\n4  & 0.019 & 0.026 \\\\\n5  & 0.016 & 0.025 \\\\\n6  & 0.014 & 0.022 \\\\\n7  & 0.013 & 0.021 \\\\\n8  & 0.012 & 0.020 \\\\\n9  & 0.012 & 0.020 \\\\\n10 & 0.012 & 0.019 \\\\\n\\midrule\n\\textit{Relative drop} & \\textit{70.8\\%} & \\textit{40.8\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-turn GAR decay (GAR-Dongre, mid-turn average) for base models. Qwen shows a steep 70.8\\% decline from turn~1 to mid-turns; Llama shows a more gradual 40.8\\% decline. Both exhibit monotonic decay, confirming GAR degradation as a cross-architecture phenomenon, though severity varies.}\n\\label{tab:gar_decay}\n\\end{table}\n\nTable~\\ref{tab:gar_decay} confirms that GAR decay is present in both architectures, with Qwen exhibiting substantially steeper decline (70.8\\% vs.\\ 40.8\\%).\nThe less severe decay in Llama may reflect architectural differences (grouped query attention, different RoPE parameters) or pretraining data composition.\n\n\\subsection{Training Dynamics}\n\nOn Qwen-2.5-7B, ThreadGate v7 exhibits a three-phase training trajectory: an initial plateau (steps 0--50), a phase transition where GAR rapidly increases (steps 50--100), and convergence to GAR$\\approx$0.48 by step 144.\nLlama-3.1-8B shows similar dynamics but converges more slowly (step 180) to a lower GAR value (0.38), consistent with stronger KV-sharing constraints from GQA.\n\nBoth models achieve stable NTP convergence (Qwen: 0.95, Llama: 0.92), indicating that the auxiliary GAR loss does not impair language modeling.\n\n\\subsection{Four-Way Ablation (Qwen-2.5-7B)}\n\nWe evaluate four model variants on 50 held-out conversations:\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{GAR-D} & \\textbf{GAR-O} & \\textbf{PPL} & \\textbf{NTP} \\\\\n\\midrule\nBase         & 0.012 & 0.010 & 4.23 & 1.52 \\\\\nLoRA-only    & 0.014 & 0.486 & 2.63 & 0.95 \\\\\nThreadGate   & 0.016 & 0.487 & 2.63 & 0.95 \\\\\nUniform Gate & 0.015 & 0.492 & 2.62 & 0.94 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Four-way evaluation on Qwen-2.5-7B (50 held-out conversations). GAR-D: GAR-Dongre (mid-turn); GAR-O: GAR-ours (mid-turn); PPL: perplexity; NTP: NTP loss. All fine-tuned models achieve nearly identical GAR and PPL, confirming that gating provides no incremental benefit.}\n\\label{tab:qwen_4way}\n\\end{table}\n\nTable~\\ref{tab:qwen_4way} reveals a striking negative result: despite ThreadGate achieving GAR$=$0.48 during training, its inference GAR-Dongre (0.016) is indistinguishable from LoRA-only (0.014) and Uniform Gate (0.015).\nThe maximum pairwise difference is 0.6 percentage points.\nPPL values are virtually identical across all fine-tuned variants ($\\sim$2.63), indicating that gating neither helps nor harms language modeling quality.\n\n\\subsection{Three-Way Evaluation (Llama-3.1-8B)}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{GAR-D} & \\textbf{GAR-O} & \\textbf{PPL} & \\textbf{NTP} \\\\\n\\midrule\nBase       & 0.005 & ---   & 4.50 & 1.45 \\\\\nLoRA-only  & 0.022 & 0.400 & 2.83 & 0.95 \\\\\nThreadGate & 0.038 & 0.420 & 2.85 & 0.96 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Three-way evaluation on Llama-3.1-8B. ThreadGate shows a 1.6 pp advantage over LoRA-only in GAR-Dongre (0.038 vs.\\ 0.022), larger than the $<$0.6 pp difference observed on Qwen, but still statistically non-significant (Table~\\ref{tab:bootstrap}).}\n\\label{tab:llama_3way}\n\\end{table}\n\nTable~\\ref{tab:llama_3way} shows that on Llama, ThreadGate achieves a 1.6 percentage-point advantage over LoRA-only in GAR-Dongre---larger than the near-zero difference on Qwen.\nHowever, as we show in Section~\\ref{sec:statistical}, this difference is not statistically significant, and PPL remains comparable (2.85 vs.\\ 2.83).\n\n\\subsection{Cross-Model Training-Inference Gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-2.5-7B} & \\textbf{Llama-3.1-8B} \\\\\n\\midrule\nTraining GAR (converged)   & 0.48  & 0.38  \\\\\nInference GAR-D (mid-turn) & 0.016 & 0.038 \\\\\nGap ratio                  & 30$\\times$ & 10$\\times$ \\\\\n\\midrule\nGate mean                  & 0.93--0.98 & 0.945 \\\\\nGate std                   & ---        & 0.038 \\\\\nGate direction             & Reverse (27/28) & Reverse (weaker) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Training-inference gap comparison. Both models show large gaps between training-time and inference-time GAR, confirming the distribution shift is not architecture-specific. Llama's smaller gap (10$\\times$ vs.\\ 30$\\times$) correlates with its higher base GAR and GQA architecture.}\n\\label{tab:gap}\n\\end{table}\n\nTable~\\ref{tab:gap} presents the core negative finding: ThreadGate achieves substantial training-time GAR optimization on both architectures, but this improvement collapses at inference.\nThe 30$\\times$ gap on Qwen and 10$\\times$ gap on Llama represent the first quantitative measurements of how teacher-forcing distribution shift undermines auxiliary attention loss objectives.\n\n\\subsection{Downstream Task Validation}\n\nTo verify that GAR decay corresponds to observable task-level degradation, we measure instruction retention rate---the fraction of system-prompt-specified instructions (role, format constraints) that the model follows---across turns.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Turn} & \\textbf{Base GAR} & \\textbf{Base Ret.} & \\textbf{TG GAR} & \\textbf{TG Ret.} \\\\\n\\midrule\n1  & 0.041 & 0.82 & 0.044 & 0.83 \\\\\n10 & 0.012 & 0.68 & 0.013 & 0.69 \\\\\n21 & 0.006 & 0.55 & 0.007 & 0.56 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GAR and instruction retention rate across turns (Qwen). GAR and retention are positively correlated ($r{=}0.72$), validating GAR as a proxy for task-level degradation. ThreadGate does not improve retention ($<$1.5 pp difference).}\n\\label{tab:retention}\n\\end{table}\n\nTable~\\ref{tab:retention} shows a positive correlation ($r{=}0.72$) between GAR and instruction retention, validating GAR as a meaningful proxy for task-level performance.\nCritically, ThreadGate provides no improvement in retention rate ($<$1.5 percentage-point difference from base), consistent with its failure to improve inference-time GAR.\n\n%-------------------------------------------------------------------\n\\section{Analysis}\n\\label{sec:analysis}\n%-------------------------------------------------------------------\n\n\\subsection{Gradient Conflict Analysis}\n\nWe compute the cosine similarity and magnitude ratio between NTP and GAR gradients on gate parameters across three training checkpoints.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-2.5-7B} & \\textbf{Llama-3.1-8B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Epoch 0}} \\\\\n\\quad cos\\_sim mean       & $-0.089$ & $-0.052$ \\\\\n\\quad Conflict layers (\\%)& 79\\%     & 63\\% \\\\\n\\quad mag\\_ratio mean     & 7.5$\\times$  & 5.2$\\times$ \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Epoch 2}} \\\\\n\\quad cos\\_sim mean       & $-0.042$ & $-0.028$ \\\\\n\\quad Conflict layers (\\%)& 67\\%     & 56\\% \\\\\n\\quad mag\\_ratio mean     & 14.7$\\times$ & 6.8$\\times$ \\\\\n\\quad mag\\_ratio max      & 1139$\\times$ (L27) & 420$\\times$ \\\\\n\\midrule\nPositive cos\\_sim layers  & 6--9/28  & 10/32 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{NTP--GAR gradient conflict across training. On both architectures, a majority of layers show opposing gradient directions (negative cosine similarity), while NTP magnitude increasingly dominates. Llama shows more layers with positive cosine similarity (10/32), reflecting the cooperative effect of GQA's shared KV projections.}\n\\label{tab:gradient}\n\\end{table}\n\nTable~\\ref{tab:gradient} reveals systematic gradient conflict between NTP and GAR objectives.\nOn Qwen, 67--79\\% of layers show opposing gradient directions, with NTP magnitude dominance increasing from 7.5$\\times$ to 14.7$\\times$ over training.\nThe weakening of directional conflict (cos\\_sim $-0.089 \\to -0.042$) does \\emph{not} indicate objective alignment; rather, it reflects GAR gradients becoming negligible relative to NTP.\nLayer 27 exhibits extreme NTP dominance (1139$\\times$ by epoch 2), corresponding to the strongest NTP signal at the output layer.\n\nOn Llama, the pattern is directionally consistent but less clean: only 56--63\\% of layers show conflict, and 10 of 32 layers have positive cosine similarity (cooperative gradients).\nThis partial cooperation may arise from GQA's shared key-value projections, where optimizing NTP's KV updates incidentally benefits goal token attention in certain layers.\nMagnitude ratios are also lower (5.2--6.8$\\times$), consistent with Llama's smaller training-inference gap.\n\n\\subsection{Gate Profile Analysis}\n\nAt inference, gates cluster near identity ($g_l \\in [0.93, 0.99]$ for Qwen; mean 0.945 for Llama), attenuating sub-layer output by only 2--7\\%.\nThis intervention strength is insufficient to meaningfully shift attention patterns.\n\nOn Qwen, 27 of 28 layers exhibit \\emph{reverse} turn conditioning: the gate difference between turn~1 and turn~21 is negative, meaning gates suppress sub-layer contributions more at early turns (where GAR is high) and become increasingly passive at late turns (where intervention is most needed).\nThis reversal is a direct consequence of NTP gradient dominance: NTP pushes gates toward 1.0 to preserve layer computation, and this pressure intensifies at late turns where NTP loss is largest.\n\nOn Llama, reverse turn conditioning is present but less pronounced (gate top-5 diff range: $[-0.12, -0.06]$ vs.\\ Qwen $[-0.21, -0.11]$), consistent with the smaller gradient magnitude ratios.\n\n\\subsection{Attention Visualization}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Turn 1} & \\textbf{Turn 10} & \\textbf{Turn 21} \\\\\n\\midrule\nBase       & 0.042 & 0.012 & 0.006 \\\\\nThreadGate & 0.044 & 0.013 & 0.007 \\\\\nUniform Gate & 0.043 & 0.012 & 0.006 \\\\\nLoRA-only  & 0.043 & 0.013 & 0.007 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inference-time goal token attention weights across turns (Qwen). All four model variants produce virtually identical attention patterns, despite ThreadGate achieving substantially different patterns during training (GAR 0.48). This is the clearest evidence of training-inference distribution shift.}\n\\label{tab:attention}\n\\end{table}\n\nTable~\\ref{tab:attention} provides the most direct evidence of distribution shift: at inference time, all four model variants produce virtually indistinguishable attention patterns over goal tokens, despite ThreadGate achieving dramatically different attention during training.\nThe attention decay pattern (turn~1: 0.042--0.044; turn~21: 0.006--0.007) is identical across all variants, confirming that gating has no detectable effect on inference-time attention allocation.\n\n\\subsection{Statistical Significance}\n\\label{sec:statistical}\n\nWe perform paired bootstrap resampling (10,000 iterations) on the 50-conversation held-out evaluation to quantify uncertainty in the ThreadGate vs.\\ LoRA-only comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Mean $\\Delta$} & \\textbf{95\\% CI} & \\textbf{$p$} & \\textbf{$d$} \\\\\n\\midrule\nQwen  & 0.002 & [$-$0.018, 0.022] & 0.42 & 0.05 \\\\\nLlama & 0.016 & [$-$0.008, 0.041] & 0.12 & 0.22 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Bootstrap confidence intervals for ThreadGate vs.\\ LoRA-only GAR-Dongre difference. Both CIs include zero. Qwen shows negligible effect ($d{=}0.05$); Llama shows a small effect ($d{=}0.22$) that does not reach significance.}\n\\label{tab:bootstrap}\n\\end{table}\n\nOn Qwen, the 95\\% confidence interval [$-$0.018, 0.022] is tight, symmetric around zero, with $p{=}0.42$ and negligible effect size ($d{=}0.05$).\nThis cleanly supports the null hypothesis of zero gating benefit.\n\nOn Llama, the CI is wider [$-$0.008, 0.041] and shifted positive (mean 0.016), with $p{=}0.12$ and small effect size ($d{=}0.22$).\nThe null hypothesis cannot be rejected, but the possibility of a small positive effect cannot be excluded.\nThis ambiguity is characteristic of Llama's consistently weaker but non-zero gating residual across all analyses.\n\n%-------------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n%-------------------------------------------------------------------\n\n\\subsection{Exposure Bias Mitigation}\n\nTo test whether exposure bias contributes to the training-inference gap, we train a ThreadGate variant with scheduled sampling \\cite{bengio2015scheduled}: during training, model-generated tokens replace teacher-forced tokens with linearly increasing probability (0$\\to$0.5 over epoch~0--1, fixed at 0.5 for epoch~2).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{TF (v7)} & \\textbf{SS} & \\textbf{$\\Delta$} \\\\\n\\midrule\nTraining GAR         & 0.48  & 0.32  & $-$0.16 \\\\\nInference GAR-D      & 0.016 & 0.026 & +0.010 \\\\\nGap ratio            & 30$\\times$  & 12.3$\\times$ & $-$17.7 \\\\\nPPL                  & 2.63  & 2.72  & +0.09 \\\\\nGate direction       & 27/28 rev.  & 15/28 rev. & improved \\\\\nTraining time (h)    & 5.9   & 9.5   & +3.6 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{SS vs.\\ TF bootstrap (10k iterations)}} \\\\\n$p$-value            & \\multicolumn{3}{c}{0.07} \\\\\n95\\% CI              & \\multicolumn{3}{c}{[$-$0.003, 0.023]} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scheduled sampling (SS) vs.\\ teacher-forcing (TF) on Qwen. SS reduces the training-inference gap from 30$\\times$ to 12.3$\\times$ and partially corrects gate direction (13/28 layers no longer reversed), but the improvement is statistically marginal ($p{\\approx}0.07$, CI includes zero).}\n\\label{tab:mitigation}\n\\end{table}\n\nTable~\\ref{tab:mitigation} shows that scheduled sampling reduces the gap from 30$\\times$ to 12.3$\\times$ (reduction factor 1.6$\\times$) and partially corrects gate direction (13 of 28 layers no longer show reverse conditioning).\nHowever, the improvement is statistically marginal ($p \\approx 0.07$, CI [$-$0.003, 0.023] includes zero), and the residual 12.3$\\times$ gap remains substantial.\n\nThese results provide suggestive but inconclusive evidence that exposure bias is a contributing factor to the training-inference gap.\nThe remaining gap after mitigation implies that other mechanisms---gradient competition, training data length distribution, NTP dominance---are also at play.\nScheduled sampling also incurs costs: lower training GAR (0.32 vs.\\ 0.48), mild PPL degradation (+0.09), and 61\\% longer training time due to autoregressive generation during training.\n\n\\subsection{Why Lightweight Gating Is Insufficient}\n\nOur results identify a structural limitation of lightweight residual gating with auxiliary attention losses trained under teacher-forcing.\nThe failure is not due to poor loss design (v1--v7 covered four families), insufficient capacity (gates are per-layer scalars by design to avoid overfitting), or training instability (v7 converges cleanly).\nRather, the failure stems from two coupled mechanisms:\n\n\\textbf{Gradient competition} ensures that NTP loss dominates gate parameter updates, pushing gates toward identity (preserving full layer computation) regardless of GAR objectives.\nThe 7--15$\\times$ magnitude ratio means the GAR signal is progressively marginalized during training.\n\n\\textbf{Distribution shift} ensures that even if gating learns useful attention patterns under teacher-forcing, these patterns do not transfer to inference where the model conditions on its own (potentially degraded) outputs.\nThe 30$\\times$ gap quantifies this failure mode.\n\nThese mechanisms are coupled: gradient competition causes gates to converge near identity, which means even the small transferable signal is attenuated to 2--7\\%---far below any detectable effect.\n\n\\subsection{Scope and Limitations}\n\nOur claims are limited to lightweight residual gating (per-layer scalar gates) with auxiliary attention losses (GAR variants) trained under standard teacher-forcing.\nWe do not claim that all attention steering methods are equally vulnerable to distribution shift.\nHeavier interventions (attention masking, activation steering at inference time) bypass training-inference distribution shift entirely and remain viable.\n\nSingle-seed training (seed=42) limits variance estimation.\nWe compensate with paired bootstrap CIs on the 50-conversation evaluation, but multi-seed training would strengthen conclusions.\n\n\\subsection{Future Directions}\n\nOur analysis suggests several paths forward:\n\\begin{enumerate}\n\\item \\textbf{Inference-time intervention}: Attention masking or activation steering applied at inference time bypasses the distribution shift entirely \\cite{li2024inference}.\n\\item \\textbf{Decoupled goal-processing pathways}: Architectures that process goal information through a separate pathway, avoiding competition with NTP on shared parameters.\n\\item \\textbf{GAR-aware decoding}: Modifying the decoding procedure rather than the training objective to maintain goal attention, e.g., through constrained beam search with GAR as a reward signal.\n\\item \\textbf{Stronger exposure bias mitigation}: Techniques beyond scheduled sampling, such as Professor Forcing \\cite{lamb2016professor} or reinforcement learning on the GAR objective with model-generated contexts.\n\\end{enumerate}\n\n%-------------------------------------------------------------------\n\\section{Conclusion}\n%-------------------------------------------------------------------\n\nWe present a mechanistic analysis of why lightweight residual gating fails to fix multi-turn attention degradation in LLMs.\nThreadGate, a per-layer gating module trained with auxiliary GAR objectives, achieves successful training-time optimization (GAR 0.02$\\to$0.48 on Qwen-2.5-7B) but collapses at inference (30$\\times$ gap).\nCross-model experiments on Llama-3.1-8B confirm directional consistency (10$\\times$ gap) with architecture-dependent magnitude.\n\nOur gradient analysis reveals that NTP loss dominates gate parameters by 7--15$\\times$, causing reverse turn conditioning in the majority of layers.\nFour-way ablation confirms zero incremental benefit of gating over standard LoRA fine-tuning on Qwen (bootstrap $p{=}0.42$) and marginal, non-significant benefit on Llama ($p{=}0.12$).\nScheduled-sampling mitigation provides suggestive evidence ($p{\\approx}0.07$) that exposure bias is a contributing factor, reducing the gap from 30$\\times$ to 12.3$\\times$.\n\nThese findings offer the first quantitative measurement of how teacher-forcing distribution shift undermines auxiliary attention losses in lightweight residual gating, and highlight the need for inference-time or distribution-shift-aware approaches to multi-turn attention steering.\n\n%-------------------------------------------------------------------\n% References\n%-------------------------------------------------------------------\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Bachlechner et~al.}2021]{bachlechner2021rezero}\nThomas Bachlechner, Bodhisattwa~Prasad Majumder, Henry~Huai Mao, Garrison~W. Cottrell, and Julian McAuley. 2021.\n\\newblock {ReZero} is all you need: Fast convergence at large depth.\n\\newblock In \\emph{Proceedings of the Thirty-Fifth AAAI Conference on Artificial Intelligence}.\n\n\\bibitem[\\protect\\citename{Bai et~al.}2024]{bai2024mt}\nYushi Bai, Xin Lv, Jiajie Zhang, Yuze He, Ji Qi, Lei Hou, Jie Tang, Juanzi Li, and Zhiyuan Liu. 2024.\n\\newblock {MT-Bench-101}: A fine-grained benchmark for evaluating large language models in multi-turn dialogue.\n\\newblock In \\emph{Proceedings of ACL 2024}.\n\n\\bibitem[\\protect\\citename{Bengio et~al.}2015]{bengio2015scheduled}\nSamy Bengio, Oriol Vinyals, Navdeep Jaitly, and Noam Shazeer. 2015.\n\\newblock Scheduled sampling for sequence prediction with recurrent neural networks.\n\\newblock In \\emph{Advances in Neural Information Processing Systems}.\n\n\\bibitem[\\protect\\citename{Chen et~al.}2018]{chen2018gradnorm}\nZhao Chen, Vijay Badrinarayanan, Chen-Yu Lee, and Andrew Rabinovich. 2018.\n\\newblock {GradNorm}: Gradient normalization for adaptive loss balancing in deep multitask networks.\n\\newblock In \\emph{Proceedings of ICML 2018}.\n\n\\bibitem[\\protect\\citename{Chen et~al.}2020]{chen2020just}\nZhao Chen, Jiquan Ngiam, Yanping Huang, Thang Luong, Henrik Kretzschmar, Yuning Chai, and Dragomir Anguelov. 2020.\n\\newblock Just pick a sign: Optimizing deep multitask models with gradient sign dropout.\n\\newblock In \\emph{Advances in Neural Information Processing Systems}.\n\n\\bibitem[\\protect\\citename{Dongre et~al.}2026]{dongre2026multi}\nAditya Dongre, Abhay Kumar, Aseem Srivastava, Rajiv Ratn Shah, and Ponnurangam Kumaraguru. 2026.\n\\newblock Multi-turn attention degradation in large language models: Goal attention ratio analysis and residual stream probing.\n\\newblock In \\emph{Proceedings of NAACL 2026}.\n\n\\bibitem[\\protect\\citename{Elhage et~al.}2021]{elhage2021mathematical}\nNelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, et~al. 2021.\n\\newblock A mathematical framework for transformer circuits.\n\\newblock \\emph{Transformer Circuits Thread}.\n\n\\bibitem[\\protect\\citename{Ko et~al.}2024]{ko2024found}\nJongho Ko, Kyungjae Lee, Minjoon Seo, and Hyunwoo Kim. 2024.\n\\newblock Found in the middle: How language models use long contexts better via multi-turn dialogue.\n\\newblock \\emph{arXiv preprint arXiv:2403.13795}.\n\n\\bibitem[\\protect\\citename{Lamb et~al.}2016]{lamb2016professor}\nAlex~M. Lamb, Anirudh Goyal~Alias~Parth Goyal, Ying Zhang, Saizheng Zhang, Aaron~C. Courville, and Yoshua Bengio. 2016.\n\\newblock Professor forcing: A new algorithm for training recurrent networks.\n\\newblock In \\emph{Advances in Neural Information Processing Systems}.\n\n\\bibitem[\\protect\\citename{Leblond et~al.}2018]{leblond2018searnn}\nR{\\'e}mi Leblond, Jean-Baptiste Alayrac, Anton Osokin, and Simon Lacoste-Julien. 2018.\n\\newblock {SEARNN}: Training {RNNs} with global-local losses.\n\\newblock In \\emph{Proceedings of ICLR 2018}.\n\n\\bibitem[\\protect\\citename{Li et~al.}2024]{li2024inference}\nKenneth Li, Oam Patel, Fernanda Vi{\\'e}gas, Hanspeter Pfister, and Martin Wattenberg. 2024.\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock In \\emph{Advances in Neural Information Processing Systems}.\n\n\\bibitem[\\protect\\citename{Liu et~al.}2024]{liu2024lost}\nNelson~F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2024.\n\\newblock Lost in the middle: How language models use long contexts.\n\\newblock \\emph{Transactions of the Association for Computational Linguistics}, 12:157--173.\n\n\\bibitem[\\protect\\citename{Luo et~al.}2025]{luo2025flexidepth}\nYifan Luo, Zhenhua Liu, and Shanghua Gao. 2025.\n\\newblock {FlexiDepth}: Dynamic depth inference for efficient transformers.\n\\newblock In \\emph{Proceedings of ICLR 2025}.\n\n\\bibitem[\\protect\\citename{Qiu et~al.}2025]{qiu2025gated}\nXin Qiu, Rui Wang, and Yongbin Li. 2025.\n\\newblock Gated attention networks for selective information routing.\n\\newblock In \\emph{Proceedings of ACL 2025}.\n\n\\bibitem[\\protect\\citename{Ranzato et~al.}2016]{ranzato2016sequence}\nMarc'Aurelio Ranzato, Sumit Chopra, Michael Auli, and Wojciech Zaremba. 2016.\n\\newblock Sequence level training with recurrent neural networks.\n\\newblock In \\emph{Proceedings of ICLR 2016}.\n\n\\bibitem[\\protect\\citename{Raposo et~al.}2024]{raposo2024mixture}\nDavid Raposo, Sam Ritter, Blake Richards, Timothy Lillicrap, Peter~Conway Humphreys, and Adam Santoro. 2024.\n\\newblock Mixture-of-depths: Dynamically allocating compute in transformer-based language models.\n\\newblock \\emph{arXiv preprint arXiv:2404.02258}.\n\n\\bibitem[\\protect\\citename{Turner et~al.}2024]{turner2024activation}\nAlex Turner, Lisa Thiergart, David Udell, Gavin Leech, Ulisse Mini, and Monte MacDiarmid. 2024.\n\\newblock Activation addition: Steering language models without optimization.\n\\newblock \\emph{arXiv preprint arXiv:2308.10248}.\n\n\\bibitem[\\protect\\citename{Wang et~al.}2024]{wang2024multichallenge}\nYifan Wang, Jinhao Duan, and Kaidi Xu. 2024.\n\\newblock {MultiChallenge}: A benchmark for multi-turn dialogue challenges.\n\\newblock \\emph{arXiv preprint arXiv:2402.09800}.\n\n\\bibitem[\\protect\\citename{Xiao et~al.}2024]{xiao2024efficient}\nGuangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. 2024.\n\\newblock Efficient streaming language models with attention sinks.\n\\newblock In \\emph{Proceedings of ICLR 2024}.\n\n\\bibitem[\\protect\\citename{Yu et~al.}2020]{yu2020gradient}\nTianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol Hausman, and Chelsea Finn. 2020.\n\\newblock Gradient surgery for multi-task learning.\n\\newblock In \\emph{Advances in Neural Information Processing Systems}.\n\n\\bibitem[\\protect\\citename{Zhang et~al.}2024]{zhang2024tell}\nYifan Zhang, Yifeng Liu, Huizhuo Yuan, Zhen Qin, and Quanquan Gu. 2024.\n\\newblock Tell your model where to attend: Post-hoc attention steering for {LLMs}.\n\\newblock In \\emph{Proceedings of ICLR 2024}.\n\n\\bibitem[\\protect\\citename{Zou et~al.}2023]{zou2023representation}\nAndy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mantas Mazeika, Ann-Kathrin Dombrowski, et~al. 2023.\n\\newblock Representation engineering: A top-down approach to {AI} transparency.\n\\newblock \\emph{arXiv preprint arXiv:2310.01405}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0627cbd5-00b4-4e2e-bfe1-768e6d003070",
  "isSidechain": false,
  "requestId": "req_011CbC9RYe9MiVftBzYfYYws",
  "type": "assistant",
  "uuid": "fcc02cea-07c9-448e-891d-9db11f1eaf53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Q6MfFfuit6u612NdFxQv4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 43480,
      "output_tokens": 13625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13625,
          "cache_read_input_tokens": 43480,
          "cache_creation_input_tokens": 318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 318
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

_source line 32 · 2026-05-19T15:19:03.911Z_

<details><summary>↩ Tool result · `toolu_017i39C93MLzq2K5nUoqoTmb`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcc02cea-07c9-448e-891d-9db11f1eaf53",
  "isSidechain": false,
  "promptId": "60b11cf6-cc2f-4f15-8815-d9e57690cbb7",
  "type": "user",
  "uuid": "710de81f-bc5c-446a-aa11-2d5e5e94c68c",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{tabularx}\n\\usepackage{subcaption}\n\n\\title{Why Lightweight Gating Struggles to Fix Multi-Turn Attention Degradation:\\\\A Mechanistic Analysis}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLarge language models progressively lose track of goal instructions as multi-turn dialogues grow longer.\nRecent work by \\citet{dongre2026multi} quantified this degradation through Goal Attention Ratio (GAR) and showed that goal information persists in the residual stream (probe AUC$=$0.98) even as the attention channel closes, suggesting that a learnable gate on the residual connection could recover it.\nWe test this hypothesis with ThreadGate, a per-layer gating module trained jointly with next-token prediction (NTP) and an auxiliary GAR objective.\nThreadGate successfully optimizes GAR during training (0.02$\\to$0.48 on Qwen-2.5-7B), yet this improvement fails to transfer to autoregressive inference (GAR$=$0.016, a 30$\\times$ gap).\nWe identify two coupled mechanisms behind this failure:\n(1)~NTP gradients dominate gate parameters by 7--15$\\times$ in magnitude, causing gates to learn \\emph{reverse} turn conditioning---suppressing intervention where it is most needed;\n(2)~teacher-forcing creates a distribution shift under which attention patterns learned on gold contexts do not generalize to model-generated contexts.\nFour-way ablation confirms that gating provides no statistically significant incremental benefit over LoRA-only fine-tuning (bootstrap $p{=}0.42$, Cohen's $d{=}0.05$ on Qwen).\nCross-model experiments on Llama-3.1-8B show directional consistency in all failure modes, with a 10$\\times$ training-inference gap and 1.6 percentage-point gating increment that remains statistically non-significant ($p{=}0.12$).\nA scheduled-sampling mitigation reduces the gap from 30$\\times$ to 12.3$\\times$ ($p{\\approx}0.07$), providing suggestive evidence that exposure bias is a contributing factor.\nOur results constitute the first quantitative measurement of how teacher-forcing distribution shift undermines auxiliary attention losses in lightweight residual gating, and identify the specific mechanisms through which this vulnerability manifests.\n\\end{abstract}\n\n%-------------------------------------------------------------------\n\\section{Introduction}\n%-------------------------------------------------------------------\n\nMulti-turn dialogue is the primary mode of interaction with modern large language models (LLMs), yet model performance degrades systematically as conversations grow longer \\cite{liu2024lost,xiao2024efficient,ko2024found}.\nA key manifestation is the declining adherence to goal instructions specified in the system prompt, which \\citet{dongre2026multi} quantified through the Goal Attention Ratio (GAR)---the fraction of attention mass allocated to goal-relevant tokens.\nAcross 12 models, they observed 27--48\\% GAR drops over 50 turns, establishing GAR decay as a robust structural phenomenon.\n\nA striking finding from \\citet{dongre2026multi} is that goal information \\emph{persists} in the residual stream throughout the conversation (linear probe AUC up to 0.98), even as the attention channel closes.\nThis creates a natural hypothesis: if goal information is available in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it by modulating how much each layer's computation contributes to the output.\n\nWe test this hypothesis through ThreadGate, a per-layer gating module inspired by ReZero initialization \\cite{bachlechner2021rezero} and adaptive-depth architectures \\cite{raposo2024mixture,luo2025flexidepth}.\nEach Transformer layer receives a scalar gate $g_l \\in [0,1]$ trained with a joint NTP and GAR objective.\nOver seven training configurations (v1--v7) covering four loss families, we find that MSE-based targeting with gate diversity regularization (v7) is the only configuration that achieves stable training convergence.\n\nThe central finding is negative: despite successful training-time GAR optimization (0.02$\\to$0.48), inference-time GAR remains at 0.016---a 30$\\times$ gap.\nFour-way ablation (ThreadGate / Uniform Gate / LoRA-only / Base) confirms that gating provides zero incremental contribution over standard LoRA fine-tuning.\n\nOur mechanistic analysis reveals two coupled failure modes:\n\\begin{itemize}\n\\item \\textbf{Gradient competition}: NTP loss dominates gate gradients by 7--15$\\times$ in magnitude, with 67--79\\% of layers showing opposing gradient directions (cosine similarity $-0.089$ to $-0.042$). This causes gates to learn reverse turn conditioning, becoming passive precisely at late turns where intervention is most needed.\n\\item \\textbf{Distribution shift}: Teacher-forcing trains attention patterns on gold contexts, which do not transfer to model-generated contexts at inference time. This is the well-known exposure bias \\cite{bengio2015scheduled,ranzato2016sequence}, but we provide the first quantitative measurement of its impact on auxiliary attention losses (30$\\times$ gap).\n\\end{itemize}\n\nCross-model experiments on Llama-3.1-8B demonstrate directional consistency: a 10$\\times$ training-inference gap, reverse gate conditioning, and gradient conflict in 56--63\\% of layers, though with weaker magnitudes reflecting architectural differences (GQA vs.\\ MHA).\n\nOur contributions are:\n\\begin{enumerate}\n\\item The first quantitative measurement of how teacher-forcing distribution shift undermines auxiliary attention losses in lightweight residual gating (30$\\times$ training-inference GAR gap on Qwen, 10$\\times$ on Llama).\n\\item Per-layer quantification of NTP--GAR gradient competition showing magnitude ratios of 7--15$\\times$ and systematic direction conflict.\n\\item Systematic ablation across two model families isolating the contribution of gating, LoRA fine-tuning, and loss design.\n\\item Suggestive evidence from scheduled-sampling mitigation that exposure bias is a contributing factor (gap reduction from 30$\\times$ to 12.3$\\times$, $p{\\approx}0.07$).\n\\end{enumerate}\n\n%-------------------------------------------------------------------\n\\section{Related Work}\n%-------------------------------------------------------------------\n\n\\paragraph{Multi-turn dialogue degradation.}\nPerformance loss over extended conversations has been documented across multiple dimensions.\n\\citet{liu2024lost} identify a ``lost in the middle'' effect where models struggle with information placed in the center of long contexts.\n\\citet{xiao2024efficient} analyze attention sinks---the concentration of attention on initial tokens regardless of relevance---as a contributor to context degradation.\n\\citet{ko2024found} investigate position-dependent retrieval failures in multi-turn settings.\nMT-Bench-101 \\cite{bai2024mt} and MultiChallenge \\cite{wang2024multichallenge} provide standardized benchmarks for multi-turn evaluation.\nMost directly relevant, \\citet{dongre2026multi} introduce GAR as a quantitative metric for goal attention decay, measure it across 12 models, and show through residual stream probing that goal information persists even as attention degrades.\n\n\\paragraph{Residual gating and adaptive depth.}\nReZero \\cite{bachlechner2021rezero} initializes residual connections with learnable scalars to stabilize deep network training.\nMixture-of-Depths \\cite{raposo2024mixture} and FlexiDepth \\cite{luo2025flexidepth} use per-layer gating to adaptively skip computation.\n\\citet{qiu2025gated} propose gated attention mechanisms for selective information routing.\nOur ThreadGate adopts the ReZero formulation but repurposes it for attention steering rather than training stability.\n\n\\paragraph{Attention steering and intervention.}\nAttention manipulation approaches include attention masking \\cite{zhang2024tell}, activation steering \\cite{li2024inference,turner2024activation}, and representation engineering \\cite{zou2023representation}.\n\\citet{dongre2026multi} attempt goal re-injection through residual stream manipulation (Appendix H) but report failure.\nOur work provides a complementary failure case through residual gating, and identifies the mechanistic reasons.\n\n\\paragraph{Exposure bias.}\nThe mismatch between teacher-forced training and autoregressive inference was identified by \\citet{bengio2015scheduled}, who proposed scheduled sampling as mitigation.\nSubsequent work includes Professor Forcing \\cite{lamb2016professor}, SEARNN \\cite{leblond2018searnn}, and various reinforcement learning approaches \\cite{ranzato2016sequence}.\nExposure bias is well-studied for generation quality but its impact on auxiliary loss objectives has received little attention.\nWe provide the first quantitative measurement of how this distribution shift specifically undermines auxiliary attention losses.\n\n\\paragraph{Multi-task gradient conflict.}\nGradient conflicts in multi-task learning have been studied extensively \\cite{yu2020gradient,liu2021conflict,chen2020just}.\nPCGrad \\cite{yu2020gradient} projects conflicting gradients; GradNorm \\cite{chen2018gradnorm} normalizes gradient magnitudes.\nOur gradient analysis reveals that the NTP--GAR conflict is particularly severe because NTP gradients dominate in both direction and magnitude.\n\n%-------------------------------------------------------------------\n\\section{Background}\n\\label{sec:background}\n%-------------------------------------------------------------------\n\n\\paragraph{Goal Attention Ratio (GAR).}\nFollowing \\citet{dongre2026multi}, GAR measures the fraction of attention mass allocated to goal-relevant tokens. For a response token $r$ at layer $l$ and head $h$:\n\\begin{equation}\n\\text{GAR}(r, l, h) = \\sum_{t \\in \\mathcal{G}} \\alpha_{r,t}^{(l,h)}\n\\end{equation}\nwhere $\\mathcal{G}$ is the set of goal tokens in the system prompt and $\\alpha_{r,t}^{(l,h)}$ is the attention weight.\nWe aggregate across layers, heads, and response tokens to obtain per-turn GAR values.\n\nWe employ two GAR definitions: GAR-Dongre (system prompt task tokens as goals, all response tokens) for comparability with \\citet{dongre2026multi}, and GAR-ours (system prompt + first user query as goals, last token per assistant turn) as the training signal.\nBoth definitions yield consistent negative findings.\n\n\\paragraph{Residual stream persistence.}\n\\citet{dongre2026multi} demonstrate through linear probing that goal-relevant information remains decodable from the residual stream (AUC up to 0.98) even at late conversation turns where GAR has dropped significantly.\nThis persistence motivates the hypothesis that a learnable gate on the residual connection could recover goal attention by modulating layer-wise computation.\n\n%-------------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n%-------------------------------------------------------------------\n\n\\subsection{ThreadGate Architecture}\n\nThreadGate augments each Transformer layer $l$ with a scalar gate $g_l \\in [0,1]$, modifying the residual connection as:\n\\begin{equation}\n\\mathbf{x}_{l+1} = \\mathbf{x}_l + g_l \\cdot f_l(\\mathbf{x}_l)\n\\label{eq:gate}\n\\end{equation}\nwhere $f_l$ denotes the combined self-attention and feed-forward computation of layer $l$.\nWhen $g_l \\to 0$, the layer becomes a no-op (identity mapping); when $g_l = 1$, the standard residual connection is recovered.\nGates are initialized to 1.0 (identity) and parameterized as $g_l = \\sigma(w_l)$ where $\\sigma$ is the sigmoid function and $w_l$ is an unconstrained scalar.\n\n\\subsection{Training Objective}\n\nThe v7 configuration uses a joint loss:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_{\\text{NTP}} + \\lambda_{\\text{GAR}} \\cdot \\mathcal{L}_{\\text{GAR}} + \\lambda_{\\text{div}} \\cdot \\mathcal{L}_{\\text{div}}\n\\end{equation}\n\nThe GAR component uses an MSE target that provides bidirectional gradients:\n\\begin{equation}\n\\mathcal{L}_{\\text{GAR}} = \\frac{1}{|\\mathcal{T}|} \\sum_{t \\in \\mathcal{T}} \\left( \\text{GAR}(t) - \\tau(t) \\right)^2\n\\end{equation}\nwhere $\\tau(t)$ is a per-turn target derived from the turn-1 GAR level, encouraging the model to maintain early-turn attention throughout the conversation.\n\nThe diversity term $\\mathcal{L}_{\\text{div}} = -\\text{Var}(\\{g_l\\}_{l=1}^{L})$ encourages gates to differentiate across layers rather than collapsing to a uniform value.\n\n\\subsection{Loss Design Evolution}\n\nWe explored four loss families across seven configurations:\n\\emph{cumulative} (v1--v2) accumulating GAR over turns,\n\\emph{maximize} (v3--v5) directly maximizing GAR,\n\\emph{smooth saturation} (v6) with gradient-friendly saturation curves, and\n\\emph{MSE target} (v7) with bidirectional gradients.\nOnly v7 achieved stable training convergence; earlier variants suffered from gradient vanishing (v1--v2), training instability (v3--v5), or slow convergence (v6).\n\n\\subsection{Training Setup}\n\nWe fine-tune Qwen-2.5-7B and Llama-3.1-8B using LoRA (rank 16) on UltraChat multi-turn dialogue data.\nThreadGate adds $L$ scalar parameters (28 for Qwen, 32 for Llama) on top of the LoRA parameters ($\\sim$20--22 MB).\nTraining runs for 3 epochs with learning rate $2\\times10^{-4}$, batch size 4, and seed 42.\n$\\lambda_{\\text{GAR}} = 0.1$, $\\lambda_{\\text{div}} = 0.01$.\n\n%-------------------------------------------------------------------\n\\section{Experiments}\n\\label{sec:experiments}\n%-------------------------------------------------------------------\n\n\\subsection{Phase 1: Base Model GAR Decay}\n\nWe first verify GAR decay on our target models using 5 held-out conversations of 10+ turns each.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Turn} & \\textbf{Qwen-2.5-7B} & \\textbf{Llama-3.1-8B} \\\\\n\\midrule\n1  & 0.041 & 0.038 \\\\\n2  & 0.029 & 0.031 \\\\\n3  & 0.024 & 0.030 \\\\\n4  & 0.019 & 0.026 \\\\\n5  & 0.016 & 0.025 \\\\\n6  & 0.014 & 0.022 \\\\\n7  & 0.013 & 0.021 \\\\\n8  & 0.012 & 0.020 \\\\\n9  & 0.012 & 0.020 \\\\\n10 & 0.012 & 0.019 \\\\\n\\midrule\n\\textit{Relative drop} & \\textit{70.8\\%} & \\textit{40.8\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-turn GAR decay (GAR-Dongre, mid-turn average) for base models. Qwen shows a steep 70.8\\% decline from turn~1 to mid-turns; Llama shows a more gradual 40.8\\% decline. Both exhibit monotonic decay, confirming GAR degradation as a cross-architecture phenomenon, though severity varies.}\n\\label{tab:gar_decay}\n\\end{table}\n\nTable~\\ref{tab:gar_decay} confirms that GAR decay is present in both architectures, with Qwen exhibiting substantially steeper decline (70.8\\% vs.\\ 40.8\\%).\nThe less severe decay in Llama may reflect architectural differences (grouped query attention, different RoPE parameters) or pretraining data composition.\n\n\\subsection{Training Dynamics}\n\nOn Qwen-2.5-7B, ThreadGate v7 exhibits a three-phase training trajectory: an initial plateau (steps 0--50), a phase transition where GAR rapidly increases (steps 50--100), and convergence to GAR$\\approx$0.48 by step 144.\nLlama-3.1-8B shows similar dynamics but converges more slowly (step 180) to a lower GAR value (0.38), consistent with stronger KV-sharing constraints from GQA.\n\nBoth models achieve stable NTP convergence (Qwen: 0.95, Llama: 0.92), indicating that the auxiliary GAR loss does not impair language modeling.\n\n\\subsection{Four-Way Ablation (Qwen-2.5-7B)}\n\nWe evaluate four model variants on 50 held-out conversations:\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{GAR-D} & \\textbf{GAR-O} & \\textbf{PPL} & \\textbf{NTP} \\\\\n\\midrule\nBase         & 0.012 & 0.010 & 4.23 & 1.52 \\\\\nLoRA-only    & 0.014 & 0.486 & 2.63 & 0.95 \\\\\nThreadGate   & 0.016 & 0.487 & 2.63 & 0.95 \\\\\nUniform Gate & 0.015 & 0.492 & 2.62 & 0.94 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Four-way evaluation on Qwen-2.5-7B (50 held-out conversations). GAR-D: GAR-Dongre (mid-turn); GAR-O: GAR-ours (mid-turn); PPL: perplexity; NTP: NTP loss. All fine-tuned models achieve nearly identical GAR and PPL, confirming that gating provides no incremental benefit.}\n\\label{tab:qwen_4way}\n\\end{table}\n\nTable~\\ref{tab:qwen_4way} reveals a striking negative result: despite ThreadGate achieving GAR$=$0.48 during training, its inference GAR-Dongre (0.016) is indistinguishable from LoRA-only (0.014) and Uniform Gate (0.015).\nThe maximum pairwise difference is 0.6 percentage points.\nPPL values are virtually identical across all fine-tuned variants ($\\sim$2.63), indicating that gating neither helps nor harms language modeling quality.\n\n\\subsection{Three-Way Evaluation (Llama-3.1-8B)}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{GAR-D} & \\textbf{GAR-O} & \\textbf{PPL} & \\textbf{NTP} \\\\\n\\midrule\nBase       & 0.005 & ---   & 4.50 & 1.45 \\\\\nLoRA-only  & 0.022 & 0.400 & 2.83 & 0.95 \\\\\nThreadGate & 0.038 & 0.420 & 2.85 & 0.96 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Three-way evaluation on Llama-3.1-8B. ThreadGate shows a 1.6 pp advantage over LoRA-only in GAR-Dongre (0.038 vs.\\ 0.022), larger than the $<$0.6 pp difference observed on Qwen, but still statistically non-significant (Table~\\ref{tab:bootstrap}).}\n\\label{tab:llama_3way}\n\\end{table}\n\nTable~\\ref{tab:llama_3way} shows that on Llama, ThreadGate achieves a 1.6 percentage-point advantage over LoRA-only in GAR-Dongre---larger than the near-zero difference on Qwen.\nHowever, as we show in Section~\\ref{sec:statistical}, this difference is not statistically significant, and PPL remains comparable (2.85 vs.\\ 2.83).\n\n\\subsection{Cross-Model Training-Inference Gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-2.5-7B} & \\textbf{Llama-3.1-8B} \\\\\n\\midrule\nTraining GAR (converged)   & 0.48  & 0.38  \\\\\nInference GAR-D (mid-turn) & 0.016 & 0.038 \\\\\nGap ratio                  & 30$\\times$ & 10$\\times$ \\\\\n\\midrule\nGate mean                  & 0.93--0.98 & 0.945 \\\\\nGate std                   & ---        & 0.038 \\\\\nGate direction             & Reverse (27/28) & Reverse (weaker) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Training-inference gap comparison. Both models show large gaps between training-time and inference-time GAR, confirming the distribution shift is not architecture-specific. Llama's smaller gap (10$\\times$ vs.\\ 30$\\times$) correlates with its higher base GAR and GQA architecture.}\n\\label{tab:gap}\n\\end{table}\n\nTable~\\ref{tab:gap} presents the core negative finding: ThreadGate achieves substantial training-time GAR optimization on both architectures, but this improvement collapses at inference.\nThe 30$\\times$ gap on Qwen and 10$\\times$ gap on Llama represent the first quantitative measurements of how teacher-forcing distribution shift undermines auxiliary attention loss objectives.\n\n\\subsection{Downstream Task Validation}\n\nTo verify that GAR decay corresponds to observable task-level degradation, we measure instruction retention rate---the fraction of system-prompt-specified instructions (role, format constraints) that the model follows---across turns.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Turn} & \\textbf{Base GAR} & \\textbf{Base Ret.} & \\textbf{TG GAR} & \\textbf{TG Ret.} \\\\\n\\midrule\n1  & 0.041 & 0.82 & 0.044 & 0.83 \\\\\n10 & 0.012 & 0.68 & 0.013 & 0.69 \\\\\n21 & 0.006 & 0.55 & 0.007 & 0.56 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GAR and instruction retention rate across turns (Qwen). GAR and retention are positively correlated ($r{=}0.72$), validating GAR as a proxy for task-level degradation. ThreadGate does not improve retention ($<$1.5 pp difference).}\n\\label{tab:retention}\n\\end{table}\n\nTable~\\ref{tab:retention} shows a positive correlation ($r{=}0.72$) between GAR and instruction retention, validating GAR as a meaningful proxy for task-level performance.\nCritically, ThreadGate provides no improvement in retention rate ($<$1.5 percentage-point difference from base), consistent with its failure to improve inference-time GAR.\n\n%-------------------------------------------------------------------\n\\section{Analysis}\n\\label{sec:analysis}\n%-------------------------------------------------------------------\n\n\\subsection{Gradient Conflict Analysis}\n\nWe compute the cosine similarity and magnitude ratio between NTP and GAR gradients on gate parameters across three training checkpoints.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-2.5-7B} & \\textbf{Llama-3.1-8B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Epoch 0}} \\\\\n\\quad cos\\_sim mean       & $-0.089$ & $-0.052$ \\\\\n\\quad Conflict layers (\\%)& 79\\%     & 63\\% \\\\\n\\quad mag\\_ratio mean     & 7.5$\\times$  & 5.2$\\times$ \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Epoch 2}} \\\\\n\\quad cos\\_sim mean       & $-0.042$ & $-0.028$ \\\\\n\\quad Conflict layers (\\%)& 67\\%     & 56\\% \\\\\n\\quad mag\\_ratio mean     & 14.7$\\times$ & 6.8$\\times$ \\\\\n\\quad mag\\_ratio max      & 1139$\\times$ (L27) & 420$\\times$ \\\\\n\\midrule\nPositive cos\\_sim layers  & 6--9/28  & 10/32 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{NTP--GAR gradient conflict across training. On both architectures, a majority of layers show opposing gradient directions (negative cosine similarity), while NTP magnitude increasingly dominates. Llama shows more layers with positive cosine similarity (10/32), reflecting the cooperative effect of GQA's shared KV projections.}\n\\label{tab:gradient}\n\\end{table}\n\nTable~\\ref{tab:gradient} reveals systematic gradient conflict between NTP and GAR objectives.\nOn Qwen, 67--79\\% of layers show opposing gradient directions, with NTP magnitude dominance increasing from 7.5$\\times$ to 14.7$\\times$ over training.\nThe weakening of directional conflict (cos\\_sim $-0.089 \\to -0.042$) does \\emph{not} indicate objective alignment; rather, it reflects GAR gradients becoming negligible relative to NTP.\nLayer 27 exhibits extreme NTP dominance (1139$\\times$ by epoch 2), corresponding to the strongest NTP signal at the output layer.\n\nOn Llama, the pattern is directionally consistent but less clean: only 56--63\\% of layers show conflict, and 10 of 32 layers have positive cosine similarity (cooperative gradients).\nThis partial cooperation may arise from GQA's shared key-value projections, where optimizing NTP's KV updates incidentally benefits goal token attention in certain layers.\nMagnitude ratios are also lower (5.2--6.8$\\times$), consistent with Llama's smaller training-inference gap.\n\n\\subsection{Gate Profile Analysis}\n\nAt inference, gates cluster near identity ($g_l \\in [0.93, 0.99]$ for Qwen; mean 0.945 for Llama), attenuating sub-layer output by only 2--7\\%.\nThis intervention strength is insufficient to meaningfully shift attention patterns.\n\nOn Qwen, 27 of 28 layers exhibit \\emph{reverse} turn conditioning: the gate difference between turn~1 and turn~21 is negative, meaning gates suppress sub-layer contributions more at early turns (where GAR is high) and become increasingly passive at late turns (where intervention is most needed).\nThis reversal is a direct consequence of NTP gradient dominance: NTP pushes gates toward 1.0 to preserve layer computation, and this pressure intensifies at late turns where NTP loss is largest.\n\nOn Llama, reverse turn conditioning is present but less pronounced (gate top-5 diff range: $[-0.12, -0.06]$ vs.\\ Qwen $[-0.21, -0.11]$), consistent with the smaller gradient magnitude ratios.\n\n\\subsection{Attention Visualization}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Turn 1} & \\textbf{Turn 10} & \\textbf{Turn 21} \\\\\n\\midrule\nBase       & 0.042 & 0.012 & 0.006 \\\\\nThreadGate & 0.044 & 0.013 & 0.007 \\\\\nUniform Gate & 0.043 & 0.012 & 0.006 \\\\\nLoRA-only  & 0.043 & 0.013 & 0.007 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inference-time goal token attention weights across turns (Qwen). All four model variants produce virtually identical attention patterns, despite ThreadGate achieving substantially different patterns during training (GAR 0.48). This is the clearest evidence of training-inference distribution shift.}\n\\label{tab:attention}\n\\end{table}\n\nTable~\\ref{tab:attention} provides the most direct evidence of distribution shift: at inference time, all four model variants produce virtually indistinguishable attention patterns over goal tokens, despite ThreadGate achieving dramatically different attention during training.\nThe attention decay pattern (turn~1: 0.042--0.044; turn~21: 0.006--0.007) is identical across all variants, confirming that gating has no detectable effect on inference-time attention allocation.\n\n\\subsection{Statistical Significance}\n\\label{sec:statistical}\n\nWe perform paired bootstrap resampling (10,000 iterations) on the 50-conversation held-out evaluation to quantify uncertainty in the ThreadGate vs.\\ LoRA-only comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Mean $\\Delta$} & \\textbf{95\\% CI} & \\textbf{$p$} & \\textbf{$d$} \\\\\n\\midrule\nQwen  & 0.002 & [$-$0.018, 0.022] & 0.42 & 0.05 \\\\\nLlama & 0.016 & [$-$0.008, 0.041] & 0.12 & 0.22 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Bootstrap confidence intervals for ThreadGate vs.\\ LoRA-only GAR-Dongre difference. Both CIs include zero. Qwen shows negligible effect ($d{=}0.05$); Llama shows a small effect ($d{=}0.22$) that does not reach significance.}\n\\label{tab:bootstrap}\n\\end{table}\n\nOn Qwen, the 95\\% confidence interval [$-$0.018, 0.022] is tight, symmetric around zero, with $p{=}0.42$ and negligible effect size ($d{=}0.05$).\nThis cleanly supports the null hypothesis of zero gating benefit.\n\nOn Llama, the CI is wider [$-$0.008, 0.041] and shifted positive (mean 0.016), with $p{=}0.12$ and small effect size ($d{=}0.22$).\nThe null hypothesis cannot be rejected, but the possibility of a small positive effect cannot be excluded.\nThis ambiguity is characteristic of Llama's consistently weaker but non-zero gating residual across all analyses.\n\n%-------------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n%-------------------------------------------------------------------\n\n\\subsection{Exposure Bias Mitigation}\n\nTo test whether exposure bias contributes to the training-inference gap, we train a ThreadGate variant with scheduled sampling \\cite{bengio2015scheduled}: during training, model-generated tokens replace teacher-forced tokens with linearly increasing probability (0$\\to$0.5 over epoch~0--1, fixed at 0.5 for epoch~2).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{TF (v7)} & \\textbf{SS} & \\textbf{$\\Delta$} \\\\\n\\midrule\nTraining GAR         & 0.48  & 0.32  & $-$0.16 \\\\\nInference GAR-D      & 0.016 & 0.026 & +0.010 \\\\\nGap ratio            & 30$\\times$  & 12.3$\\times$ & $-$17.7 \\\\\nPPL                  & 2.63  & 2.72  & +0.09 \\\\\nGate direction       & 27/28 rev.  & 15/28 rev. & improved \\\\\nTraining time (h)    & 5.9   & 9.5   & +3.6 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{SS vs.\\ TF bootstrap (10k iterations)}} \\\\\n$p$-value            & \\multicolumn{3}{c}{0.07} \\\\\n95\\% CI              & \\multicolumn{3}{c}{[$-$0.003, 0.023]} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scheduled sampling (SS) vs.\\ teacher-forcing (TF) on Qwen. SS reduces the training-inference gap from 30$\\times$ to 12.3$\\times$ and partially corrects gate direction (13/28 layers no longer reversed), but the improvement is statistically marginal ($p{\\approx}0.07$, CI includes zero).}\n\\label{tab:mitigation}\n\\end{table}\n\nTable~\\ref{tab:mitigation} shows that scheduled sampling reduces the gap from 30$\\times$ to 12.3$\\times$ (reduction factor 1.6$\\times$) and partially corrects gate direction (13 of 28 layers no longer show reverse conditioning).\nHowever, the improvement is statistically marginal ($p \\approx 0.07$, CI [$-$0.003, 0.023] includes zero), and the residual 12.3$\\times$ gap remains substantial.\n\nThese results provide suggestive but inconclusive evidence that exposure bias is a contributing factor to the training-inference gap.\nThe remaining gap after mitigation implies that other mechanisms---gradient competition, training data length distribution, NTP dominance---are also at play.\nScheduled sampling also incurs costs: lower training GAR (0.32 vs.\\ 0.48), mild PPL degradation (+0.09), and 61\\% longer training time due to autoregressive generation during training.\n\n\\subsection{Why Lightweight Gating Is Insufficient}\n\nOur results identify a structural limitation of lightweight residual gating with auxiliary attention losses trained under teacher-forcing.\nThe failure is not due to poor loss design (v1--v7 covered four families), insufficient capacity (gates are per-layer scalars by design to avoid overfitting), or training instability (v7 converges cleanly).\nRather, the failure stems from two coupled mechanisms:\n\n\\textbf{Gradient competition} ensures that NTP loss dominates gate parameter updates, pushing gates toward identity (preserving full layer computation) regardless of GAR objectives.\nThe 7--15$\\times$ magnitude ratio means the GAR signal is progressively marginalized during training.\n\n\\textbf{Distribution shift} ensures that even if gating learns useful attention patterns under teacher-forcing, these patterns do not transfer to inference where the model conditions on its own (potentially degraded) outputs.\nThe 30$\\times$ gap quantifies this failure mode.\n\nThese mechanisms are coupled: gradient competition causes gates to converge near identity, which means even the small transferable signal is attenuated to 2--7\\%---far below any detectable effect.\n\n\\subsection{Scope and Limitations}\n\nOur claims are limited to lightweight residual gating (per-layer scalar gates) with auxiliary attention losses (GAR variants) trained under standard teacher-forcing.\nWe do not claim that all attention steering methods are equally vulnerable to distribution shift.\nHeavier interventions (attention masking, activation steering at inference time) bypass training-inference distribution shift entirely and remain viable.\n\nSingle-seed training (seed=42) limits variance estimation.\nWe compensate with paired bootstrap CIs on the 50-conversation evaluation, but multi-seed training would strengthen conclusions.\n\n\\subsection{Future Directions}\n\nOur analysis suggests several paths forward:\n\\begin{enumerate}\n\\item \\textbf{Inference-time intervention}: Attention masking or activation steering applied at inference time bypasses the distribution shift entirely \\cite{li2024inference}.\n\\item \\textbf{Decoupled goal-processing pathways}: Architectures that process goal information through a separate pathway, avoiding competition with NTP on shared parameters.\n\\item \\textbf{GAR-aware decoding}: Modifying the decoding procedure rather than the training objective to maintain goal attention, e.g., through constrained beam search with GAR as a reward signal.\n\\item \\textbf{Stronger exposure bias mitigation}: Techniques beyond scheduled sampling, such as Professor Forcing \\cite{lamb2016professor} or reinforcement learning on the GAR objective with model-generated contexts.\n\\end{enumerate}\n\n%-------------------------------------------------------------------\n\\section{Conclusion}\n%-------------------------------------------------------------------\n\nWe present a mechanistic analysis of why lightweight residual gating fails to fix multi-turn attention degradation in LLMs.\nThreadGate, a per-layer gating module trained with auxiliary GAR objectives, achieves successful training-time optimization (GAR 0.02$\\to$0.48 on Qwen-2.5-7B) but collapses at inference (30$\\times$ gap).\nCross-model experiments on Llama-3.1-8B confirm directional consistency (10$\\times$ gap) with architecture-dependent magnitude.\n\nOur gradient analysis reveals that NTP loss dominates gate parameters by 7--15$\\times$, causing reverse turn conditioning in the majority of layers.\nFour-way ablation confirms zero incremental benefit of gating over standard LoRA fine-tuning on Qwen (bootstrap $p{=}0.42$) and marginal, non-significant benefit on Llama ($p{=}0.12$).\nScheduled-sampling mitigation provides suggestive evidence ($p{\\approx}0.07$) that exposure bias is a contributing factor, reducing the gap from 30$\\times$ to 12.3$\\times$.\n\nThese findings offer the first quantitative measurement of how teacher-forcing distribution shift undermines auxiliary attention losses in lightweight residual gating, and highlight the need for inference-time or distribution-shift-aware approaches to multi-turn attention steering.\n\n%-------------------------------------------------------------------\n% References\n%-------------------------------------------------------------------\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Bachlechner et~al.}2021]{bachlechner2021rezero}\nThomas Bachlechner, Bodhisattwa~Prasad Majumder, Henry~Huai Mao, Garrison~W. Cottrell, and Julian McAuley. 2021.\n\\newblock {ReZero} is all you need: Fast convergence at large depth.\n\\newblock In \\emph{Proceedings of the Thirty-Fifth AAAI Conference on Artificial Intelligence}.\n\n\\bibitem[\\protect\\citename{Bai et~al.}2024]{bai2024mt}\nYushi Bai, Xin Lv, Jiajie Zhang, Yuze He, Ji Qi, Lei Hou, Jie Tang, Juanzi Li, and Zhiyuan Liu. 2024.\n\\newblock {MT-Bench-101}: A fine-grained benchmark for evaluating large language models in multi-turn dialogue.\n\\newblock In \\emph{Proceedings of ACL 2024}.\n\n\\bibitem[\\protect\\citename{Bengio et~al.}2015]{bengio2015scheduled}\nSamy Bengio, Oriol Vinyals, Navdeep Jaitly, and Noam Shazeer. 2015.\n\\newblock Scheduled sampling for sequence prediction with recurrent neural networks.\n\\newblock In \\emph{Advances in Neural Information Processing Systems}.\n\n\\bibitem[\\protect\\citename{Chen et~al.}2018]{chen2018gradnorm}\nZhao Chen, Vijay Badrinarayanan, Chen-Yu Lee, and Andrew Rabinovich. 2018.\n\\newblock {GradNorm}: Gradient normalization for adaptive loss balancing in deep multitask networks.\n\\newblock In \\emph{Proceedings of ICML 2018}.\n\n\\bibitem[\\protect\\citename{Chen et~al.}2020]{chen2020just}\nZhao Chen, Jiquan Ngiam, Yanping Huang, Thang Luong, Henrik Kretzschmar, Yuning Chai, and Dragomir Anguelov. 2020.\n\\newblock Just pick a sign: Optimizing deep multitask models with gradient sign dropout.\n\\newblock In \\emph{Advances in Neural Information Processing Systems}.\n\n\\bibitem[\\protect\\citename{Dongre et~al.}2026]{dongre2026multi}\nAditya Dongre, Abhay Kumar, Aseem Srivastava, Rajiv Ratn Shah, and Ponnurangam Kumaraguru. 2026.\n\\newblock Multi-turn attention degradation in large language models: Goal attention ratio analysis and residual stream probing.\n\\newblock In \\emph{Proceedings of NAACL 2026}.\n\n\\bibitem[\\protect\\citename{Elhage et~al.}2021]{elhage2021mathematical}\nNelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, et~al. 2021.\n\\newblock A mathematical framework for transformer circuits.\n\\newblock \\emph{Transformer Circuits Thread}.\n\n\\bibitem[\\protect\\citename{Ko et~al.}2024]{ko2024found}\nJongho Ko, Kyungjae Lee, Minjoon Seo, and Hyunwoo Kim. 2024.\n\\newblock Found in the middle: How language models use long contexts better via multi-turn dialogue.\n\\newblock \\emph{arXiv preprint arXiv:2403.13795}.\n\n\\bibitem[\\protect\\citename{Lamb et~al.}2016]{lamb2016professor}\nAlex~M. Lamb, Anirudh Goyal~Alias~Parth Goyal, Ying Zhang, Saizheng Zhang, Aaron~C. Courville, and Yoshua Bengio. 2016.\n\\newblock Professor forcing: A new algorithm for training recurrent networks.\n\\newblock In \\emph{Advances in Neural Information Processing Systems}.\n\n\\bibitem[\\protect\\citename{Leblond et~al.}2018]{leblond2018searnn}\nR{\\'e}mi Leblond, Jean-Baptiste Alayrac, Anton Osokin, and Simon Lacoste-Julien. 2018.\n\\newblock {SEARNN}: Training {RNNs} with global-local losses.\n\\newblock In \\emph{Proceedings of ICLR 2018}.\n\n\\bibitem[\\protect\\citename{Li et~al.}2024]{li2024inference}\nKenneth Li, Oam Patel, Fernanda Vi{\\'e}gas, Hanspeter Pfister, and Martin Wattenberg. 2024.\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock In \\emph{Advances in Neural Information Processing Systems}.\n\n\\bibitem[\\protect\\citename{Liu et~al.}2024]{liu2024lost}\nNelson~F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2024.\n\\newblock Lost in the middle: How language models use long contexts.\n\\newblock \\emph{Transactions of the Association for Computational Linguistics}, 12:157--173.\n\n\\bibitem[\\protect\\citename{Luo et~al.}2025]{luo2025flexidepth}\nYifan Luo, Zhenhua Liu, and Shanghua Gao. 2025.\n\\newblock {FlexiDepth}: Dynamic depth inference for efficient transformers.\n\\newblock In \\emph{Proceedings of ICLR 2025}.\n\n\\bibitem[\\protect\\citename{Qiu et~al.}2025]{qiu2025gated}\nXin Qiu, Rui Wang, and Yongbin Li. 2025.\n\\newblock Gated attention networks for selective information routing.\n\\newblock In \\emph{Proceedings of ACL 2025}.\n\n\\bibitem[\\protect\\citename{Ranzato et~al.}2016]{ranzato2016sequence}\nMarc'Aurelio Ranzato, Sumit Chopra, Michael Auli, and Wojciech Zaremba. 2016.\n\\newblock Sequence level training with recurrent neural networks.\n\\newblock In \\emph{Proceedings of ICLR 2016}.\n\n\\bibitem[\\protect\\citename{Raposo et~al.}2024]{raposo2024mixture}\nDavid Raposo, Sam Ritter, Blake Richards, Timothy Lillicrap, Peter~Conway Humphreys, and Adam Santoro. 2024.\n\\newblock Mixture-of-depths: Dynamically allocating compute in transformer-based language models.\n\\newblock \\emph{arXiv preprint arXiv:2404.02258}.\n\n\\bibitem[\\protect\\citename{Turner et~al.}2024]{turner2024activation}\nAlex Turner, Lisa Thiergart, David Udell, Gavin Leech, Ulisse Mini, and Monte MacDiarmid. 2024.\n\\newblock Activation addition: Steering language models without optimization.\n\\newblock \\emph{arXiv preprint arXiv:2308.10248}.\n\n\\bibitem[\\protect\\citename{Wang et~al.}2024]{wang2024multichallenge}\nYifan Wang, Jinhao Duan, and Kaidi Xu. 2024.\n\\newblock {MultiChallenge}: A benchmark for multi-turn dialogue challenges.\n\\newblock \\emph{arXiv preprint arXiv:2402.09800}.\n\n\\bibitem[\\protect\\citename{Xiao et~al.}2024]{xiao2024efficient}\nGuangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. 2024.\n\\newblock Efficient streaming language models with attention sinks.\n\\newblock In \\emph{Proceedings of ICLR 2024}.\n\n\\bibitem[\\protect\\citename{Yu et~al.}2020]{yu2020gradient}\nTianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol Hausman, and Chelsea Finn. 2020.\n\\newblock Gradient surgery for multi-task learning.\n\\newblock In \\emph{Advances in Neural Information Processing Systems}.\n\n\\bibitem[\\protect\\citename{Zhang et~al.}2024]{zhang2024tell}\nYifan Zhang, Yifeng Liu, Huizhuo Yuan, Zhen Qin, and Quanquan Gu. 2024.\n\\newblock Tell your model where to attend: Post-hoc attention steering for {LLMs}.\n\\newblock In \\emph{Proceedings of ICLR 2024}.\n\n\\bibitem[\\protect\\citename{Zou et~al.}2023]{zou2023representation}\nAndy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mantas Mazeika, Ann-Kathrin Dombrowski, et~al. 2023.\n\\newblock Representation engineering: A top-down approach to {AI} transparency.\n\\newblock \\emph{arXiv preprint arXiv:2310.01405}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "fcc02cea-07c9-448e-891d-9db11f1eaf53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-19T15:19:03.949Z_

```json
{
  "parentUuid": "710de81f-bc5c-446a-aa11-2d5e5e94c68c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c78f7e3a-6b0c-461c-81ab-a48822e3bae9",
  "timestamp": "2026-05-19T15:19:03.949Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T145320 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_g…",
  "leafUuid": "c78f7e3a-6b0c-461c-81ab-a48822e3bae9",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396"
}
```

---

### Tool call

_source line 36 · 2026-05-19T15:19:11.550Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ThbtEXA7e9SRoC3DHhBJW3`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex compilation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c78f7e3a-6b0c-461c-81ab-a48822e3bae9",
  "isSidechain": false,
  "requestId": "req_011CbC9mR5HTqnC7wftPGhGn",
  "type": "assistant",
  "uuid": "5a3e78fa-c967-49c0-833f-bb7e5bd7267d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zTuygKwXkWWv7NZB3qKMy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13791,
      "cache_read_input_tokens": 43798,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 43798,
          "cache_creation_input_tokens": 13791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13791
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

_source line 37 · 2026-05-19T15:19:12.447Z_

<details><summary>↩ Tool result · `toolu_01ThbtEXA7e9SRoC3DHhBJW3`</summary>

```text
[7] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim
es/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>

Output written on paper.pdf (7 pages, 193724 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a3e78fa-c967-49c0-833f-bb7e5bd7267d",
  "isSidechain": false,
  "promptId": "60b11cf6-cc2f-4f15-8815-d9e57690cbb7",
  "type": "user",
  "uuid": "fb200eed-7ce1-412e-a357-41e1abf7af8f",
  "toolUseResult": {
    "stdout": "[7] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim\nes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\n\nOutput written on paper.pdf (7 pages, 193724 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5a3e78fa-c967-49c0-833f-bb7e5bd7267d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T15:19:16.981Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01T8ifYkAVi6BwtAUAFkDAEz`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10",
  "description": "Second pdflatex compilation for cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb200eed-7ce1-412e-a357-41e1abf7af8f",
  "isSidechain": false,
  "requestId": "req_011CbC9n3QaGgx89Yuwjr2U2",
  "type": "assistant",
  "uuid": "66635518-9120-4a57-ac98-27dc41a5165a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MC1XqjP9CYiiNU4gZy3B2P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 57589,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 57589,
          "cache_creation_input_tokens": 827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 827
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

_source line 39 · 2026-05-19T15:19:17.833Z_

<details><summary>↩ Tool result · `toolu_01T8ifYkAVi6BwtAUAFkDAEz`</summary>

```text
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim
es/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>

Output written on paper.pdf (7 pages, 196623 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66635518-9120-4a57-ac98-27dc41a5165a",
  "isSidechain": false,
  "promptId": "60b11cf6-cc2f-4f15-8815-d9e57690cbb7",
  "type": "user",
  "uuid": "44188f5d-3c44-4c73-84d6-ac370e613aa1",
  "toolUseResult": {
    "stdout": ".pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim\nes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\n\nOutput written on paper.pdf (7 pages, 196623 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "66635518-9120-4a57-ac98-27dc41a5165a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T15:19:26.031Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01T3ENiXkzzDwqVjnQi4HdaJ`</summary>

```json
{
  "command": "grep -c \"Warning\" paper.log | head -1; grep \"LaTeX Warning\" paper.log | head -5",
  "description": "Check for remaining LaTeX warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44188f5d-3c44-4c73-84d6-ac370e613aa1",
  "isSidechain": false,
  "requestId": "req_011CbC9nSSB3RMszaHh9y9kL",
  "type": "assistant",
  "uuid": "c5407a76-d0dd-4d21-a5d9-b85fea6a3ff8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PqqEVMcXpxZHEi4xnM3FMT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 425,
      "cache_read_input_tokens": 58416,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 425,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 58416,
          "cache_creation_input_tokens": 425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 425
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

_source line 41 · 2026-05-19T15:19:26.106Z_

<details><summary>↩ Tool result · `toolu_01T3ENiXkzzDwqVjnQi4HdaJ`</summary>

```text
42
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5407a76-d0dd-4d21-a5d9-b85fea6a3ff8",
  "isSidechain": false,
  "promptId": "60b11cf6-cc2f-4f15-8815-d9e57690cbb7",
  "type": "user",
  "uuid": "e360c51d-097e-479c-8694-3d7bf3cd0a36",
  "toolUseResult": {
    "stdout": "42",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c5407a76-d0dd-4d21-a5d9-b85fea6a3ff8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-19T15:19:32.244Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NqVfsrgQPp4VcGWg92UN86`</summary>

```json
{
  "command": "grep \"LaTeX Warning\" paper.log | head -10",
  "description": "Check specific LaTeX warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e360c51d-097e-479c-8694-3d7bf3cd0a36",
  "isSidechain": false,
  "requestId": "req_011CbC9o3kCApWcv89dyZEiM",
  "type": "assistant",
  "uuid": "47519e8c-e67d-427b-8793-88192c6febaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sd6MJfsaQANuZs2ctxomX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 113,
      "cache_read_input_tokens": 58841,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 113,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 58841,
          "cache_creation_input_tokens": 113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 113
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

_source line 43 · 2026-05-19T15:19:32.300Z_

<details><summary>↩ Tool result · `toolu_01NqVfsrgQPp4VcGWg92UN86`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47519e8c-e67d-427b-8793-88192c6febaf",
  "isSidechain": false,
  "promptId": "60b11cf6-cc2f-4f15-8815-d9e57690cbb7",
  "type": "user",
  "uuid": "0e5e6e2d-1d0c-4425-af9d-2afb9ed06d2e",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "47519e8c-e67d-427b-8793-88192c6febaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-19T15:19:59.966Z_

编译成功，无 LaTeX Warning。7 页 PDF 已生成。

输出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper.pdf`

论文覆盖了 experiment_data.json 中全部 9 个实验：
- **Table 1**: Qwen/Llama 逐 turn GAR 衰减对比
- **Table 2**: Qwen 四路消融 (TG/UG/LO/Base)
- **Table 3**: Llama 三路评估
- **Table 4**: 跨模型训练-推理 gap (30x vs 10x)
- **Table 5**: Instruction retention vs GAR (r=0.72)
- **Table 6**: 梯度冲突对比 (cos_sim + mag_ratio)
- **Table 7**: Attention 可视化数据
- **Table 8**: Bootstrap CI 统计显著性
- **Table 9**: Scheduled sampling mitigation (gap 30x→12.3x, p≈0.07)

叙事按 narrative guidance 处理：Llama 弱化为"方向一致性"，mitigation 降级至 Discussion 作为 suggestive evidence，标题用 "Struggles to" 替换 "Cannot"，公式已修正为 ReZero-style `x + g·f(x)`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e5e6e2d-1d0c-4425-af9d-2afb9ed06d2e",
  "isSidechain": false,
  "requestId": "req_011CbC9oWXm3ZCYk5hTA8Evg",
  "type": "assistant",
  "uuid": "8e597137-c7fd-4192-885a-8e45c46e69ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6k2gofXtw1rFz63PeybNU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 103,
      "cache_read_input_tokens": 58954,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 103,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 394,
          "cache_read_input_tokens": 58954,
          "cache_creation_input_tokens": 103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 103
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T145320 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_g…",
  "leafUuid": "8e597137-c7fd-4192-885a-8e45c46e69ea",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "9c898946-3fb8-4cb9-82ea-49687eee3396"
}
```

---
