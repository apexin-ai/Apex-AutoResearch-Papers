# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/3ff56e95-537a-47e8-910b-194e01cedc1e.jsonl`
- **Structured JSON:** [`0841c1042d31ee8a8dc3.json`](../../sessions/08/0841c1042d31ee8a8dc3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T05:43:21.409Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T05:43:21.409Z",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始几何洞见 framing 全面崩塌。Simpson's Paradox 在 20 语言全量验证中双架构均不显著（Qwen partial rho=+0.11, p=0.31; Llama partial rho=+0.08, p=0.42）， CKA 在 depth 之外无额外解释力——5 语言 pilot 结果被确认为 small-sample artifact。CaCLR 三个 OOM 的 β sweep 证实 consistency loss 完全 inert，且几何子空间解释也不成立：correctness direction 的跨语言 persistence 远弱于预期，非 robust low-dimensional subspace。 Pareto frontier 噪声极大，20 语言中仅 2-3 个达到 per-language 显著性，non-monotonic 模式普遍存在。控制任务分析揭示问题远超预期—— 不仅低资源语言 artifact rate 达 42%，中资源语言也有 37% 层级组合出现 capacity artifacts，这对整个跨语言 probing 文献构成方法论挑战。 Difficulty decomposition 完全无效，random-direction control 产生同量级效果。Linear projection 需要 120-180 pairs（非 50）， 且 Procrustes 效果反转阈值在语言间高度不一致，无法给出可靠的单一阈值。 新 framing 路线：'The limits of cross-lingual calibration probe transfer — a large-scale negative result with methodological implications'。 三层贡献重构：(1) 控制任务发现是最强贡献——首次在 cross-lingual probing 场景系统性应用 selectivity 检验，>35% artifact rate 对整个领域有直接 implication；(2) 综合 negative result 同时关闭 distributional matching 和 geometric alignment 两条路径， 附完整 ablation 和 sweep 数据；(3) 条件性实用指导——linear projection 作为唯一可行方案但需 100+ pairs， 按 resource-tier 和 baseline ZS quality 分层推荐。仍可发 EACL 作为 rigorous negative result + methodology paper。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T05:43:21.413Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T05:43:21.413Z",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-21T05:43:21.435Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始几何洞见 framing 全面崩塌。Simpson's Paradox 在 20 语言全量验证中双架构均不显著（Qwen partial rho=+0.11, p=0.31; Llama partial rho=+0.08, p=0.42）， CKA 在 depth 之外无额外解释力——5 语言 pilot 结果被确认为 small-sample artifact。CaCLR 三个 OOM 的 β sweep 证实 consistency loss 完全 inert，且几何子空间解释也不成立：correctness direction 的跨语言 persistence 远弱于预期，非 robust low-dimensional subspace。 Pareto frontier 噪声极大，20 语言中仅 2-3 个达到 per-language 显著性，non-monotonic 模式普遍存在。控制任务分析揭示问题远超预期—— 不仅低资源语言 artifact rate 达 42%，中资源语言也有 37% 层级组合出现 capacity artifacts，这对整个跨语言 probing 文献构成方法论挑战。 Difficulty decomposition 完全无效，random-direction control 产生同量级效果。Linear projection 需要 120-180 pairs（非 50）， 且 Procrustes 效果反转阈值在语言间高度不一致，无法给出可靠的单一阈值。 新 framing 路线：'The limits of cross-lingual calibration probe transfer — a large-scale negative result with methodological implications'。 三层贡献重构：(1) 控制任务发现是最强贡献——首次在 cross-lingual probing 场景系统性应用 selectivity 检验，>35% artifact rate 对整个领域有直接 implication；(2) 综合 negative result 同时关闭 distributional matching 和 geometric alignment 两条路径， 附完整 ablation 和 sweep 数据；(3) 条件性实用指导——linear projection 作为唯一可行方案但需 100+ pairs， 按 resource-tier 和 baseline ZS quality 分层推荐。仍可发 EACL 作为 rigorous negative result + methodology paper。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "7889e464-44f7-4bea-b8bc-94510499606c",
  "type": "user",
  "uuid": "7d84f454-15db-4076-bde2-a03c945c17af",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T05:43:21.434Z_

```json
{
  "parentUuid": "7d84f454-15db-4076-bde2-a03c945c17af",
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
  "uuid": "f7ce1451-d8a9-4997-b416-74a599bc4227",
  "timestamp": "2026-05-21T05:43:21.434Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T05:43:21.434Z_

```json
{
  "parentUuid": "f7ce1451-d8a9-4997-b416-74a599bc4227",
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
  "uuid": "aef1da67-7a32-4998-a880-6b45c52b4bd4",
  "timestamp": "2026-05-21T05:43:21.434Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T05:43:21.435Z_

```json
{
  "parentUuid": "aef1da67-7a32-4998-a880-6b45c52b4bd4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f81ace6a-6992-4a0d-9011-72bd177dd8ac",
  "timestamp": "2026-05-21T05:43:21.435Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
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
  "aiTitle": "Generate worst-tier calibration probe transfer paper",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e"
}
```

---

### Assistant

_source line 8 · 2026-05-21T05:43:25.888Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f81ace6a-6992-4a0d-9011-72bd177dd8ac",
  "isSidechain": false,
  "requestId": "req_011CbFBUyEpicDCaePPp8vCX",
  "type": "assistant",
  "uuid": "13b44c50-1bfa-4a77-8c39-846d2c53d3ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxzHy3H7d2BWPn2UWkLhci",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12333,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12333
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

_source line 9 · 2026-05-21T05:43:26.669Z_

<details open><summary>🔧 Tool call — Read · `toolu_013fjLRrx5KbuNkK6vq8L76R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13b44c50-1bfa-4a77-8c39-846d2c53d3ce",
  "isSidechain": false,
  "requestId": "req_011CbFBUyEpicDCaePPp8vCX",
  "type": "assistant",
  "uuid": "6ece6228-07ff-413f-a6ef-25d1c7712509",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxzHy3H7d2BWPn2UWkLhci",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12333,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12333
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

_source line 10 · 2026-05-21T05:43:26.724Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DUtcBBphq81AVdAq877CD2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ece6228-07ff-413f-a6ef-25d1c7712509",
  "isSidechain": false,
  "requestId": "req_011CbFBUyEpicDCaePPp8vCX",
  "type": "assistant",
  "uuid": "06ea8090-bac7-4605-b0fc-8420a608bc52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxzHy3H7d2BWPn2UWkLhci",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12333,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12333
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

_source line 11 · 2026-05-21T05:43:26.734Z_

<details><summary>↩ Tool result · `toolu_01DUtcBBphq81AVdAq877CD2`</summary>

```text
1	# Paper Framing — xling_calib_direction
2	
3	## Target Venue
4	- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
5	- Core submission: 2 models × 20 languages × all contributions
6	- Camera-ready extension: Gemma 4 31B Dense + 30+ languages
7	
8	## Core Insight
9	The model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. This geometric insight, combined with the architecture-dependent depth-transferability tradeoff (strong on Qwen, weak on Llama), provides a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.
10	
11	## Core Claims (4, causal chain)
12	
13	### Claim 1 — Pareto Frontier (Discovery)
14	Cross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).
15	- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).
16	- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.
17	
18	### Claim 2 — Decomposition (Analysis)
19	Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
20	- Evidence: IRT difficulty probes → project out → retrain → compare transfer.
21	
22	### Claim 3 — CaCLR (Method / Diagnostic)
23	CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.
24	- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.
25	- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.
26	- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.
27	- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.
28	- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.
29	- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.
30	
31	### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)
32	The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty ("method replication to more languages"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).
33	- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.
34	
35	### Key Empirical Contributions (elevated from appendix to main body, D012)
36	- **Control task methodological warning**: Hewitt & Liang selectivity analysis reveals ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold). First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.
37	- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.
38	- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.
39	
40	## Story Spine
41	- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
42	- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
43	- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) ~28% of low-resource probing results are capacity artifacts (control task warning for the field); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.
44	- **Headline template (method success)**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
45	- **Headline template (negative result)**: "Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines."
46	- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.
47	
48	## Field-Level Significance
49	This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.
50	
51	## Anticipated Reviewer Concerns & Responses
52	1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.
53	2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
54	3. **"Mean-shift too weak / why does it fail?"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.
55	4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
56	5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
57	6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
58	7. **"Predictable from domain adaptation theory"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.
59	8. **"No statistical tests"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.
60	9. **"Probing methodology concerns"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.
61	10. **"No mechanistic explanation"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as "geometric analysis" not "mechanistic explanation." **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.
62	11. **"Why not conformal prediction?"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.
63	12. **"CaCLR parallel activations = test leakage?"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.
64	13. **"CaCLR is your own method — self-debunking is less impactful"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.
65	14. **"CKA is correlational, not mechanistic"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.
66	
67	## Additional Related Work Coverage (Dream-identified gaps)
68	- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) "On learning invariant representations for domain adaptation" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.
69	- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.
70	- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.
71	- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.
72	- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.
73	- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.
74	- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.
75	
76	## Differentiation from Closest Prior Work
77	| Paper | Their Focus | Our Difference |
78	|-------|-------------|----------------|
79	| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |
80	| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
81	| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
82	| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
83	| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06ea8090-bac7-4605-b0fc-8420a608bc52",
  "isSidechain": false,
  "promptId": "7889e464-44f7-4bea-b8bc-94510499606c",
  "type": "user",
  "uuid": "dc50baf0-3d35-4f3c-8cf7-2657b52db7de",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. This geometric insight, combined with the architecture-dependent depth-transferability tradeoff (strong on Qwen, weak on Llama), provides a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\"method replication to more languages\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n### Key Empirical Contributions (elevated from appendix to main body, D012)\n- **Control task methodological warning**: Hewitt & Liang selectivity analysis reveals ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold). First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) ~28% of low-resource probing results are capacity artifacts (control task warning for the field); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \"geometric analysis\" not \"mechanistic explanation.\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 84,
      "startLine": 1,
      "totalLines": 84
    }
  },
  "sourceToolAssistantUUID": "06ea8090-bac7-4605-b0fc-8420a608bc52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "dc50baf0-3d35-4f3c-8cf7-2657b52db7de",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier calibration probe transfer paper",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e"
}
```

---

### Tool result

_source line 14 · 2026-05-21T05:43:26.995Z_

<details><summary>↩ Tool result · `toolu_013fjLRrx5KbuNkK6vq8L76R`</summary>

```text
1	[
2	  {
3	    "name": "Qwen3-235B Full Pareto Frontier",
4	    "description": "Qwen3-235B-A22B (94 layers, MoE, INT4), 24 probed layers (every 4th), 20 languages, 5 transfer conditions",
5	    "results": {
6	      "en_best_auroc": 0.738,
7	      "en_best_layer": 72,
8	      "en_auroc_range": [
9	        0.598,
10	        0.738
11	      ],
12	      "en_best_ece_raw": 0.203,
13	      "zs_pass_count": 12,
14	      "zs_pass_rate": 0.6,
15	      "zs_pass_langs": [
16	        "zh",
17	        "es",
18	        "fr",
19	        "de",
20	        "ja",
21	        "pt",
22	        "it",
23	        "ar",
24	        "hi",
25	        "ru",
26	        "ko",
27	        "vi"
28	      ],
29	      "zs_fail_langs": [
30	        "tr",
31	        "th",
32	        "sw",
33	        "bn",
34	        "am",
35	        "yo",
36	        "te",
37	        "my"
38	      ],
39	      "best_zs_auroc": {
40	        "zh": 0.672,
41	        "es": 0.681,
42	        "fr": 0.663,
43	        "de": 0.654,
44	        "ja": 0.582,
45	        "pt": 0.668,
46	        "it": 0.651,
47	        "ar": 0.603,
48	        "hi": 0.561,
49	        "ru": 0.624,
50	        "ko": 0.585,
51	        "tr": 0.541,
52	        "vi": 0.558,
53	        "th": 0.523,
54	        "sw": 0.512,
55	        "bn": 0.519,
56	        "am": 0.482,
57	        "yo": 0.471,
58	        "te": 0.498,
59	        "my": 0.463
60	      },
61	      "global_spearman_rho": -0.15,
62	      "global_spearman_p": 0.062,
63	      "per_lang_significant_negative_rho_count": 2,
64	      "per_lang_significant_positive_rho_count": 0,
65	      "per_lang_nonmonotonic_count": 14,
66	      "mean_shift_delta_auroc_all": 0.0,
67	      "linear_proj_200pair_mean_delta": 0.038,
68	      "fewshot_25_mean_delta": 0.022,
69	      "fewshot_100_mean_delta": 0.051
70	    },
71	    "tables": [
72	      {
73	        "name": "Table 1a: Qwen3-235B Per-Language Pareto Spearman ρ (Depth vs ZS-AUROC)",
74	        "columns": [
75	          "lang",
76	          "resource_tier",
77	          "best_zs_auroc",
78	          "best_zs_layer",
79	          "spearman_rho",
80	          "p_value",
81	          "pattern"
82	        ],
83	        "rows": [
84	          [
85	            "zh",
86	            "HIGH",
87	            0.672,
88	            60,
89	            -0.35,
90	            0.093,
91	            "weak negative"
92	          ],
93	          [
94	            "es",
95	            "HIGH",
96	            0.681,
97	            56,
98	            -0.28,
99	            0.184,
100	            "n.s."
101	          ],
102	          [
103	            "fr",
104	            "HIGH",
105	            0.663,
106	            60,
107	            -0.31,
108	            0.141,
109	            "n.s."
110	          ],
111	          [
112	            "de",
113	            "HIGH",
114	            0.654,
115	            56,
116	            -0.22,
117	            0.3,
118	            "n.s."
119	          ],
120	          [
121	            "ja",
122	            "HIGH",
123	            0.582,
124	            48,
125	            0.15,
126	            0.483,
127	            "non-monotonic U-shape"
128	          ],
129	          [
130	            "pt",
131	            "HIGH",
132	            0.668,
133	            60,
134	            -0.25,
135	            0.238,
136	            "n.s."
137	          ],
138	          [
139	            "it",
140	            "HIGH",
141	            0.651,
142	            56,
143	            -0.19,
144	            0.375,
145	            "n.s."
146	          ],
147	          [
148	            "ar",
149	            "MID",
150	            0.603,
151	            52,
152	            0.08,
153	            0.71,
154	            "flat"
155	          ],
156	          [
157	            "hi",
158	            "MID",
159	            0.561,
160	            48,
161	            -0.42,
162	            0.041,
163	            "significant negative"
164	          ],
165	          [
166	            "ru",
167	            "MID",
168	            0.624,
169	            56,
170	            -0.18,
171	            0.398,
172	            "n.s."
173	          ],
174	          [
175	            "ko",
176	            "MID",
177	            0.585,
178	            44,
179	            0.22,
180	            0.301,
181	            "inverted — deeper helps"
182	          ],
183	          [
184	            "tr",
185	            "MID",
186	            0.541,
187	            44,
188	            -0.12,
189	            0.576,
190	            "n.s."
191	          ],
192	          [
193	            "vi",
194	            "MID",
195	            0.558,
196	            48,
197	            0.05,
198	            0.815,
199	            "flat"
200	          ],
201	          [
202	            "th",
203	            "MID",
204	            0.523,
205	            40,
206	            -0.08,
207	            0.71,
208	            "n.s."
209	          ],
210	          [
211	            "sw",
212	            "LOW",
213	            0.512,
214	            36,
215	            -0.38,
216	            0.067,
217	            "marginal negative"
218	          ],
219	          [
220	            "bn",
221	            "LOW",
222	            0.519,
223	            40,
224	            -0.15,
225	            0.485,
226	            "n.s."
227	          ],
228	          [
229	            "am",
230	            "LOW",
231	            0.482,
232	            32,
233	            0.1,
234	            0.641,
235	            "non-monotonic"
236	          ],
237	          [
238	            "yo",
239	            "LOW",
240	            0.471,
241	            28,
242	            -0.05,
243	            0.815,
244	            "noisy flat"
245	          ],
246	          [
247	            "te",
248	            "LOW",
249	            0.498,
250	            36,
251	            -0.2,
252	            0.348,
253	            "n.s."
254	          ],
255	          [
256	            "my",
257	            "LOW",
258	            0.463,
259	            28,
260	            0.12,
261	            0.576,
262	            "non-monotonic"
263	          ]
264	        ]
265	      },
266	      {
267	        "name": "Table 1b: Qwen3-235B 5 Transfer Conditions Summary (mean across 20 langs)",
268	        "columns": [
269	          "condition",
270	          "mean_auroc",
271	          "std",
272	          "delta_vs_zs",
273	          "significant_improvement_count"
274	        ],
275	        "rows": [
276	          [
277	            "zero-shot",
278	            0.572,
279	            0.072,
280	            0.0,
281	            "—"
282	          ],
283	          [
284	            "mean-shift",
285	            0.572,
286	            0.072,
287	            0.0,
288	            "0/20"
289	          ],
290	          [
291	            "linear_proj_200",
292	            0.61,
293	            0.058,
294	            0.038,
295	            "11/20"
296	          ],
297	          [
298	            "fewshot_25",
299	            0.594,
300	            0.065,
301	            0.022,
302	            "7/20"
303	          ],
304	          [
305	            "fewshot_100",
306	            0.623,
307	            0.054,
308	            0.051,
309	            "13/20"
310	          ]
311	        ]
312	      }
313	    ],
314	    "figures": [],
315	    "analysis": "Qwen3-235B 的 Pareto frontier 远不如 MVP (Qwen2.5-7B) 清晰。MoE 架构的 expert routing 打破了 dense model 中 depth = specialization 的单调映射，导致 14/20 语言呈现 non-monotonic 模式。 仅 hi 和 sw 达到 per-language 显著性，但方向相反的 ko (+0.22, n.s.) 和 ja (+0.15, n.s.) 表明 depth-transfer tradeoff 不是普遍现象。Global rho=-0.15 被 between-language 差异驱动而非 within-language depth 效应。MVP 的 clear Pareto 可能是 dense 7B model 的特殊现象，不推广到大规模 MoE。 5 transfer conditions 中 linear projection 和 few-shot 100 有中等改善，但 significant improvement 仅覆盖 55-65% 的语言，且主要集中在高资源语言。\n\n\nEN best AUROC 落在 worst 范围 [0.7, 0.76] 内。MoE routing 导致层间 representation 变异度增大， 每第 4 层采样可能跳过 expert routing 的关键切换点，引入额外噪声。INT4 量化对 correctness signal 有轻微衰减（plan_010 将确认）。 ZS 60% pass rate 因为：(1) 235B 参数量提升了高/中资源语言的 representation quality，但 INT4 折损部分增益； (2) MoE 的 expert specialization 可能导致不同语言路由到不同 expert 子集，correctness direction 的跨语言一致性被 expert 分化削弱； (3) 低资源语言在预训练中 token 占比不足，加之 MoE 可能给它们分配较少 expert capacity。 Global Pareto rho=-0.15 仅 marginally significant (p=0.062)：depth-transfer tradeoff 在多数语言不显著， 因为 MoE 中 depth 不单调地映射到 representation specialization——expert routing 在不同深度可以\"重置\"语言特异性。 14/20 语言呈现 non-monotonic 模式（U 形、倒 U 形、锯齿形），这是 MoE 特有的现象。 Mean-shift ΔAUROC ≡ 0 符合已证明的数学不变性。Linear projection 和 few-shot 有正增益但方差大。\n"
316	  },
317	  {
318	    "name": "Llama 4 Scout Full Pareto Frontier",
319	    "description": "Llama 4 Scout (48 layers, MoE, W4A16), 12 probed layers, 20 languages, 5 transfer conditions",
320	    "results": {
321	      "en_best_auroc": 0.715,
322	      "en_best_layer": 40,
323	      "en_auroc_range": [
324	        0.612,
325	        0.715
326	      ],
327	      "en_best_ece_raw": 0.218,
328	      "zs_pass_count": 11,
329	      "zs_pass_rate": 0.55,
330	      "zs_pass_langs": [
331	        "zh",
332	        "es",
333	        "fr",
334	        "de",
335	        "pt",
336	        "it",
337	        "ar",
338	        "ru",
339	        "ko",
340	        "vi",
341	        "ja"
342	      ],
343	      "zs_fail_langs": [
344	        "hi",
345	        "tr",
346	        "th",
347	        "sw",
348	        "bn",
349	        "am",
350	        "yo",
351	        "te",
352	        "my"
353	      ],
354	      "best_zs_auroc": {
355	        "zh": 0.643,
356	        "es": 0.658,
357	        "fr": 0.641,
358	        "de": 0.632,
359	        "ja": 0.556,
360	        "pt": 0.645,
361	        "it": 0.628,
362	        "ar": 0.581,
363	        "hi": 0.542,
364	        "ru": 0.602,
365	        "ko": 0.571,
366	        "tr": 0.523,
367	        "vi": 0.555,
368	        "th": 0.508,
369	        "sw": 0.496,
370	        "bn": 0.505,
371	        "am": 0.468,
372	        "yo": 0.455,
373	        "te": 0.487,
374	        "my": 0.448
375	      },
376	      "global_spearman_rho": -0.08,
377	      "global_spearman_p": 0.218,
378	      "per_lang_significant_negative_rho_count": 0,
379	      "per_lang_significant_positive_rho_count": 0,
380	      "per_lang_nonmonotonic_count": 11
381	    },
382	    "tables": [
383	      {
384	        "name": "Table 2: Llama 4 Scout Per-Language Pareto Spearman ρ",
385	        "columns": [
386	          "lang",
387	          "resource_tier",
388	          "best_zs_auroc",
389	          "spearman_rho",
390	          "p_value"
391	        ],
392	        "rows": [
393	          [
394	            "zh",
395	            "HIGH",
396	            0.643,
397	            -0.2,
398	            0.533
399	          ],
400	          [
401	            "es",
402	            "HIGH",
403	            0.658,
404	            -0.15,
405	            0.641
406	          ],
407	          [
408	            "fr",
409	            "HIGH",
410	            0.641,
411	            -0.25,
412	            0.432
413	          ],
414	          [
415	            "de",
416	            "HIGH",
417	            0.632,
418	            -0.1,
419	            0.758
420	          ],
421	          [
422	            "ja",
423	            "HIGH",
424	            0.556,
425	            0.3,
426	            0.343
427	          ],
428	          [
429	            "pt",
430	            "HIGH",
431	            0.645,
432	            -0.18,
433	            0.576
434	          ],
435	          [
436	            "it",
437	            "HIGH",
438	            0.628,
439	            -0.08,
440	            0.805
441	          ],
442	          [
443	            "ar",
444	            "MID",
445	            0.581,
446	            0.25,
447	            0.432
448	          ],
449	          [
450	            "hi",
451	            "MID",
452	            0.542,
453	            -0.35,
454	            0.264
455	          ],
456	          [
457	            "ru",
458	            "MID",
459	            0.602,
460	            -0.05,
461	            0.878
462	          ],
463	          [
464	            "ko",
465	            "MID",
466	            0.571,
467	            0.4,
468	            0.198
469	          ],
470	          [
471	            "tr",
472	            "MID",
473	            0.523,
474	            0.1,
475	            0.758
476	          ],
477	          [
478	            "vi",
479	            "MID",
480	            0.555,
481	            0.15,
482	            0.641
483	          ],
484	          [
485	            "th",
486	            "MID",
487	            0.508,
488	            -0.2,
489	            0.533
490	          ],
491	          [
492	            "sw",
493	            "LOW",
494	            0.496,
495	            -0.28,
496	            0.379
497	          ],
498	          [
499	            "bn",
500	            "LOW",
501	            0.505,
502	            -0.1,
503	            0.758
504	          ],
505	          [
506	            "am",
507	            "LOW",
508	            0.468,
509	            0.05,
510	            0.878
511	          ],
512	          [
513	            "yo",
514	            "LOW",
515	            0.455,
516	            -0.15,
517	            0.641
518	          ],
519	          [
520	            "te",
521	            "LOW",
522	            0.487,
523	            -0.08,
524	            0.805
525	          ],
526	          [
527	            "my",
528	            "LOW",
529	            0.448,
530	            0.18,
531	            0.576
532	          ]
533	        ]
534	      }
535	    ],
536	    "figures": [],
537	    "analysis": "Llama 4 Scout 确认 worst tier 预期：depth-transfer tradeoff 在 MoE 架构上完全不显著。 与 Qwen3-235B 合并看，0 个架构在 p<0.05 水平展现清晰的 Pareto——pareto_spearman_rho_significant_archs=0。 MVP 中 Qwen2.5-7B dense model 的 clear Pareto 是 dense architecture + small scale 的特殊现象， 不推广到大规模 MoE。这对 Claim 1 是毁灭性的：无法声称存在普遍的 depth-transferability tradeoff。\n\n\nLlama 4 Scout 的 EN AUROC 低于 Qwen3 因为模型有效参数量更小（17B active vs 22B active）。 W4A16 量化对 correctness signal 有轻微额外损耗。ZS pass rate 55% 处于 worst 范围低端。 仅 12 probed layers 使 per-language Spearman 检验功效极低（n=12），无语言达到显著性。 MVP (Llama-3.1-8B) 中观察到的 architecture-specific 弱 Pareto 在 Scout 上进一步恶化： Scout 是 MoE (16 experts)，与 3.1-8B 的 dense 架构根本不同，expert routing 引入同样的 non-monotonic 行为。Global rho=-0.08 完全不显著——Llama 架构系列的 depth-transfer tradeoff 不稳定。\n"
538	  },
539	  {
540	    "name": "CaCLR Implementation and Comparative Evaluation",
541	    "description": "CaCLR (BCE + α·SB-ECE + β·MMD), β sweep 3 OOM, α sweep, component ablation, vs 4 baselines, 2 models × 20 langs",
542	    "results": {
543	      "caclr_mean_delta_auroc_vs_zs_qwen": -0.008,
544	      "caclr_mean_delta_auroc_vs_zs_llama": -0.012,
545	      "caclr_mean_delta_auroc_combined": -0.01,
546	      "caclr_best_beta": "none — all β values inert or harmful",
547	      "caclr_best_alpha": 0.1,
548	      "beta_sweep_results": {
549	        "beta_0.001": {
550	          "mean_delta_auroc": -0.003,
551	          "std": 0.018
552	        },
553	        "beta_0.01": {
554	          "mean_delta_auroc": -0.006,
555	          "std": 0.021
556	        },
557	        "beta_0.1": {
558	          "mean_delta_auroc": -0.011,
559	          "std": 0.025
560	        },
561	        "beta_1.0": {
562	          "mean_delta_auroc": -0.019,
563	          "std": 0.031
564	        }
565	      },
566	      "alpha_sweep_results": {
567	        "alpha_0.01": {
568	          "mean_delta_auroc": -0.002,
569	          "mean_delta_ece": 0.008
570	        },
571	        "alpha_0.1": {
572	          "mean_delta_auroc": -0.005,
573	          "mean_delta_ece": 0.003
574	        },
575	        "alpha_1.0": {
576	          "mean_delta_auroc": -0.012,
577	          "mean_delta_ece": -0.002
578	        },
579	        "alpha_10.0": {
580	          "mean_delta_auroc": -0.028,
581	          "mean_delta_ece": -0.005
582	        }
583	      },
584	      "component_ablation": {
585	        "bce_only": {
586	          "delta_vs_zs": -0.001,
587	          "note": "retraining from scratch ~= standard LR"
588	        },
589	        "bce_plus_sbece": {
590	          "delta_vs_zs": -0.007,
591	          "note": "SB-ECE regularization hurts discrimination"
592	        },
593	        "bce_plus_mmd": {
594	          "delta_vs_zs": -0.005,
595	          "note": "MMD inert to slightly harmful"
596	        },
597	        "full_caclr": {
598	          "delta_vs_zs": -0.01,
599	          "note": "combined losses compound harm"
600	        }
601	      },
602	      "linear_proj_vs_caclr_delta": 0.048,
603	      "fewshot100_vs_caclr_delta": 0.061,
604	      "implementation_spec": {
605	        "mmd_kernel": "Gaussian RBF, bandwidth=median heuristic",
606	        "optimizer": "Adam, lr=1e-3, cosine schedule",
607	        "epochs": 50,
608	        "early_stopping": "patience=10 on held-out BCE loss",
609	        "initialization": "from standard LR solution",
610	        "batch_size": 256,
611	        "mmd_items": "same items as BCE (probe_train split)",
612	        "parallel_set_size_range": [
613	          612,
614	          2847
615	        ]
616	      }
617	    },
618	    "tables": [
619	      {
620	        "name": "Table 3a: CaCLR β Sweep (Qwen3-235B, fixed layer 50% depth, 20 langs mean)",
621	        "columns": [
622	          "beta",
623	          "mean_auroc",
624	          "delta_vs_zs",
625	          "pct_langs_improved",
626	          "pct_langs_harmed"
627	        ],
628	        "rows": [
629	          [
630	            0.001,
631	            0.57,
632	            -0.003,
633	            "30%",
634	            "45%"
635	          ],
636	          [
637	            0.01,
638	            0.567,
639	            -0.006,
640	            "25%",
641	            "55%"
642	          ],
643	          [
644	            0.1,
645	            0.562,
646	            -0.011,
647	            "15%",
648	            "65%"
649	          ],
650	          [
651	            1.0,
652	            0.554,
653	            -0.019,
654	            "10%",
655	            "80%"
656	          ]
657	        ]
658	      },
659	      {
660	        "name": "Table 3b: 5-Way Transfer Condition Comparison (both models × 20 langs, EN-optimal layer)",
661	        "columns": [
662	          "condition",
663	          "mean_auroc",
664	          "mean_ece",
665	          "delta_auroc_vs_zs",
666	          "win_rate_vs_zs"
667	        ],
668	        "rows": [
669	          [
670	            "zero-shot",
671	            0.568,
672	            0.285,
673	            "—",
674	            "—"
675	          ],
676	          [
677	            "mean-shift",
678	            0.568,
679	            0.291,
680	            0.0,
681	            "0%"
682	          ],
683	          [
684	            "CaCLR_best",
685	            0.558,
686	            0.278,
687	            -0.01,
688	            "18%"
689	          ],
690	          [
691	            "linear_proj_200",
692	            0.606,
693	            0.248,
694	            0.038,
695	            "72%"
696	          ],
697	          [
698	            "fewshot_25",
699	            0.59,
700	            0.262,
701	            0.022,
702	            "55%"
703	          ],
704	          [
705	            "fewshot_100",
706	            0.619,
707	            0.235,
708	            0.051,
709	            "78%"
710	          ]
711	        ]
712	      },
713	      {
714	        "name": "Table 3c: CaCLR Component Ablation",
715	        "columns": [
716	          "configuration",
717	          "mean_auroc",
718	          "delta_vs_zs",
719	          "note"
720	        ],
721	        "rows": [
722	          [
723	            "BCE only (re-init)",
724	            0.567,
725	            -0.001,
726	            "≈ ZS baseline"
727	          ],
728	          [
729	            "BCE + SB-ECE (α=0.1)",
730	            0.561,
731	            -0.007,
732	            "ECE gains tiny, AUROC drops"
733	          ],
734	          [
735	            "BCE + MMD (β=0.01)",
736	            0.563,
737	            -0.005,
738	            "MMD inert/harmful"
739	          ],
740	          [
741	            "Full CaCLR (α=0.1, β=0.01)",
742	            0.558,
743	            -0.01,
744	            "compound degradation"
745	          ]
746	        ]
747	      }
748	    ],
749	    "figures": [],
750	    "analysis": "CaCLR 的 negative result 是 worst tier 的核心。β sweep 证实 consistency loss 在所有 3 OOM 均为 inert 或 harmful—— 这不是超参选择问题而是方法论层面的失败。1-D MMD 的结构性限制（probe logit 空间太低维）加上 conditional distribution mismatch（Zhao et al. 2019）导致 distributional matching 路径被彻底关闭。 与此同时，CKA subspace 解释也不成立（plan_011 将确认），所以\"MMD 失败是因为它只 match marginal 而不 match subspace direction\"这个 elegant 的解释也变成了 post-hoc rationalization—— 实际上 subspace 本身就不 robust。这是 worst tier 最痛苦的部分：不仅方法失败，解释也失败。 但作为 negative result，reproducibility 标准高：完整的 implementation spec、β/α sweep、 component ablation 使社区可以独立验证，避免重复尝试 distributional matching 路径。\n\n\nCaCLR 失败的根本原因：MMD 在 probe logits 空间操作，而 logits 是 1-D（线性 probe 的单一输出）。 1-D MMD 只能 match 两个标量分布的 marginal，无法对齐 correctness direction 的方向性结构。 即使 marginal logit 分布被 match，EN 和 target 的 conditional distributions P(logit|correct) vs P(logit|incorrect) 可能仍然不同——Zhao et al. (2019) 的理论预测得到验证。β 越大，MMD 约束越强， logits 被拉向无区分性的 marginal match，discrimination 下降。α 高值时 SB-ECE 正则化 进一步牺牲 AUROC 以换取 calibration 改善，但改善微小且不稳定。Component ablation 证实 每个额外 loss component 都是净负面的——base BCE（从 LR solution 初始化再微调）已经接近 ZS 性能， 额外优化无正贡献。Linear projection 和 few-shot 都显著优于 CaCLR，因为它们直接利用 target-language 信息（parallel pairs 或 labels）而非试图间接 match distributions。 CKA subspace 解释（correctness direction 是 low-dimensional language-agnostic subspace） 不成立——如果该 subspace 真的存在且 robust，MMD 应该至少能做到无害，但实际上有害， 说明 correctness signal 的跨语言结构比预期更 language-specific。\n"
751	  },
752	  {
753	    "name": "Difficulty-Controlled Decomposition Ablation",
754	    "description": "IRT difficulty probes → project out → retrain correctness probes, 10 langs × 8 layers × 2 models",
755	    "results": {
756	      "decomp_capability_delta_auroc_mean": -0.003,
757	      "decomp_capability_delta_auroc_range": [
758	        -0.015,
759	        0.008
760	      ],
761	      "random_direction_control_delta_mean": -0.005,
762	      "random_direction_control_delta_range": [
763	        -0.018,
764	        0.006
765	      ],
766	      "difficulty_probe_r2": 0.31,
767	      "decomp_vs_random_paired_test_p": 0.42,
768	      "per_tier_delta": {
769	        "HIGH": {
770	          "mean_delta": -0.002,
771	          "significant_count": "0/4"
772	        },
773	        "MID": {
774	          "mean_delta": -0.004,
775	          "significant_count": "0/3"
776	        },
777	        "LOW": {
778	          "mean_delta": -0.003,
779	          "significant_count": "0/3"
780	        }
781	      }
782	    },
783	    "tables": [
784	      {
785	        "name": "Table 4: Difficulty Decomposition Ablation (mean across 2 models)",
786	        "columns": [
787	          "lang",
788	          "resource_tier",
789	          "original_zs_auroc",
790	          "after_projection_auroc",
791	          "delta",
792	          "random_control_delta",
793	          "decomp_vs_random_p"
794	        ],
795	        "rows": [
796	          [
797	            "zh",
798	            "HIGH",
799	            0.658,
800	            0.655,
801	            -0.003,
802	            -0.006,
803	            0.61
804	          ],
805	          [
806	            "es",
807	            "HIGH",
808	            0.67,
809	            0.669,
810	            -0.001,
811	            -0.004,
812	            0.52
813	          ],
814	          [
815	            "fr",
816	            "HIGH",
817	            0.652,
818	            0.649,
819	            -0.003,
820	            -0.007,
821	            0.38
822	          ],
823	          [
824	            "de",
825	            "HIGH",
826	            0.643,
827	            0.642,
828	            -0.001,
829	            -0.003,
830	            0.71
831	          ],
832	          [
833	            "hi",
834	            "MID",
835	            0.552,
836	            0.547,
837	            -0.005,
838	            -0.008,
839	            0.55
840	          ],
841	          [
842	            "ru",
843	            "MID",
844	            0.613,
845	            0.61,
846	            -0.003,
847	            -0.005,
848	            0.64
849	          ],
850	          [
851	            "ko",
852	            "MID",
853	            0.578,
854	            0.572,
855	            -0.006,
856	            -0.004,
857	            0.48
858	          ],
859	          [
860	            "tr",
861	            "MID",
862	            0.532,
863	            0.53,
864	            -0.002,
865	            -0.006,
866	            0.33
867	          ],
868	          [
869	            "sw",
870	            "LOW",
871	            0.504,
872	            0.501,
873	            -0.003,
874	            -0.005,
875	            0.58
876	          ],
877	          [
878	            "bn",
879	            "LOW",
880	            0.512,
881	            0.504,
882	            -0.008,
883	            -0.007,
884	            0.82
885	          ]
886	        ]
887	      }
888	    ],
889	    "figures": [],
890	    "analysis": "Decomposition 的 null result 与 random-direction control 不可区分（p=0.42），表明投影效应来自 dimensionality reduction 而非 difficulty-specific 信号去除。这从根本上否定了 Claim 2 的因果叙述—— transfer degradation 不能分解为 difficulty-shared 和 capability-specific 两个可操作的 component。 在 worst tier framing 中，这成为 negative result 的一部分：decomposition 是另一条被关闭的路径。\n\n\nDifficulty decomposition 在 worst tier 无实质效果。两个原因：(1) difficulty 和 capability 信号在 representation 空间中高度纠缠——IRT difficulty direction 不是一个干净的、可投影去除的独立子空间， 而是与 correctness signal 共享大量方差。投影去除 difficulty 后 correctness signal 也被部分损坏， 导致 retrained probe 的 transfer 性能与原始相当甚至略差。(2) Random-direction control 产生 同量级的效果（mean delta -0.005 vs -0.003，paired test p=0.42），这意味着观察到的微小变化 主要来自 dimensionality reduction 效应而非 difficulty-specific 投影。Difficulty probe 本身 R²=0.31（低于理想值），表明 IRT difficulty 在 LLM representation 中的编码不够线性/集中， 使得 linear projection 无法有效捕获它。整个 decomposition framing 在经验层面被否定： transfer 的降解不能归因于 capability-specific component，或者说两个 component 不可分。\n"
891	  },
892	  {
893	    "name": "Cross-Lingual Orthogonality Analysis",
894	    "description": "Correctness-confidence cosine similarity, 20 langs × 2 architectures, resource-tier 和 language family 分析",
895	    "results": {
896	      "mean_cosine_high_resource": 0.038,
897	      "mean_cosine_mid_resource": 0.065,
898	      "mean_cosine_low_resource": 0.112,
899	      "std_cosine_low_resource": 0.082,
900	      "cosine_range_all": [
901	        0.008,
902	        0.198
903	      ],
904	      "architecture_agreement_rate": 0.65,
905	      "outlier_langs": [
906	        "am",
907	        "yo",
908	        "my"
909	      ]
910	    },
911	    "tables": [
912	      {
913	        "name": "Table 5: Cross-Lingual Orthogonality (Cosine Similarity)",
914	        "columns": [
915	          "lang",
916	          "tier",
917	          "qwen3_cosine",
918	          "llama4_cosine",
919	          "agreement",
920	          "note"
921	        ],
922	        "rows": [
923	          [
924	            "zh",
925	            "HIGH",
926	            0.031,
927	            0.028,
928	            "✓",
929	            ""
930	          ],
931	          [
932	            "es",
933	            "HIGH",
934	            0.025,
935	            0.033,
936	            "✓",
937	            ""
938	          ],
939	          [
940	            "fr",
941	            "HIGH",
942	            0.029,
943	            0.041,
944	            "✓",
945	            ""
946	          ],
947	          [
948	            "de",
949	            "HIGH",
950	            0.035,
951	            0.038,
952	            "✓",
953	            ""
954	          ],
955	          [
956	            "ja",
957	            "HIGH",
958	            0.048,
959	            0.052,
960	            "✓",
961	            ""
962	          ],
963	          [
964	            "pt",
965	            "HIGH",
966	            0.027,
967	            0.035,
968	            "✓",
969	            ""
970	          ],
971	          [
972	            "it",
973	            "HIGH",
974	            0.033,
975	            0.039,
976	            "✓",
977	            ""
978	          ],
979	          [
980	            "ar",
981	            "MID",
982	            0.042,
983	            0.058,
984	            "✓",
985	            ""
986	          ],
987	          [
988	            "hi",
989	            "MID",
990	            0.055,
991	            0.072,
992	            "✓",
993	            ""
994	          ],
995	          [
996	            "ru",
997	            "MID",
998	            0.038,
999	            0.045,
1000	            "✓",
1001	            ""
1002	          ],
1003	          [
1004	            "ko",
1005	            "MID",
1006	            0.061,
1007	            0.048,
1008	            "✗",
1009	            "direction reversed"
1010	          ],
1011	          [
1012	            "tr",
1013	            "MID",
1014	            0.075,
1015	            0.068,
1016	            "✓",
1017	            ""
1018	          ],
1019	          [
1020	            "vi",
1021	            "MID",
1022	            0.052,
1023	            0.082,
1024	            "✗",
1025	            "magnitude mismatch"
1026	          ],
1027	          [
1028	            "th",
1029	            "MID",
1030	            0.088,
1031	            0.065,
1032	            "✗",
1033	            "magnitude mismatch"
1034	          ],
1035	          [
1036	            "sw",
1037	            "LOW",
1038	            0.095,
1039	            0.108,
1040	            "✓",
1041	            "elevated"
1042	          ],
1043	          [
1044	            "bn",
1045	            "LOW",
1046	            0.082,
1047	            0.118,
1048	            "✗",
1049	            ""
1050	          ],
1051	          [
1052	            "am",
1053	            "LOW",
1054	            0.198,
1055	            0.152,
1056	            "✓",
1057	            "near non-orthogonal"
1058	          ],
1059	          [
1060	            "yo",
1061	            "LOW",
1062	            0.165,
1063	            0.128,
1064	            "✗",
1065	            ""
1066	          ],
1067	          [
1068	            "te",
1069	            "LOW",
1070	            0.105,
1071	            0.092,
1072	            "✓",
1073	            ""
1074	          ],
1075	          [
1076	            "my",
1077	            "LOW",
1078	            0.142,
1079	            0.118,
1080	            "✓",
1081	            "elevated"
1082	          ]
1083	        ]
1084	      }
1085	    ],
1086	    "figures": [],
1087	    "analysis": "Orthogonality 作为 subsection 贡献了一个 nuanced finding：该性质是 resource-tier dependent， 低资源语言中不可靠。但在 worst tier 下这个 finding 被 plan_013 的高 artifact rate 进一步削弱—— 低资源语言的高 cosine 可能反映 probe 本身的 capacity artifact 而非真正的非正交 representation 结构。 Section 简化为：\"orthogonality generally holds but becomes unreliable for low-resource languages， where probe validity itself is questionable (Section X).\" 贡献有限。\n\n\nOrthogonality 在高资源语言基本成立（cosine < 0.05），复现 Miao & Ungar (2026) 的英文发现。 但低资源语言的 cosine similarity 显著升高且方差极大（mean=0.112, std=0.082），部分语言 （am=0.198, yo=0.165, my=0.142）接近打破 orthogonality 假设。这可能是因为低资源语言 的 correctness 和 confidence directions 都更 noisy（probe 本身 selectivity 低——见 plan_013）， 而非真正的非正交结构。Architecture 一致性仅 65%：两个架构在 7/20 语言上对 orthogonality 程度 给出矛盾信号，削弱了\"orthogonality is a universal property\"的叙述。 作为 subsection（已从 standalone claim 降级），这些结果增加了复杂性但没有清晰的 takeaway。\n"
1088	  },
1089	  {
1090	    "name": "Probe Complexity Comparison",
1091	    "description": "Logistic regression vs 2-layer MLP, EN accuracy + cross-lingual transfer + calibration, 2 models × 20 langs",
1092	    "results": {
1093	      "en_auroc_lr_mean": 0.726,
1094	      "en_auroc_mlp_mean": 0.741,
1095	      "mlp_en_advantage": 0.015,
1096	      "zs_transfer_lr_mean_degradation": 0.152,
1097	      "zs_transfer_mlp_mean_degradation": 0.191,
1098	      "mlp_transfer_disadvantage": -0.039,
1099	      "lr_better_for_transfer_pct": 0.7,
1100	      "ece_lr_mean": 0.242,
1101	      "ece_mlp_mean": 0.258,
1102	      "selectivity_lr_mean": 0.218,
1103	      "selectivity_mlp_mean": 0.235
1104	    },
1105	    "tables": [
1106	      {
1107	        "name": "Table 6: Probe Complexity Comparison Summary",
1108	        "columns": [
1109	          "metric",
1110	          "logistic_regression",
1111	          "mlp_2layer",
1112	          "delta",
1113	          "p_value"
1114	        ],
1115	        "rows": [
1116	          [
1117	            "EN AUROC (mean)",
1118	            0.726,
1119	            0.741,
1120	            0.015,
1121	            0.008
1122	          ],
1123	          [
1124	            "ZS degradation (mean)",
1125	            "15.2%",
1126	            "19.1%",
1127	            "+3.9pp",
1128	            0.023
1129	          ],
1130	          [
1131	            "ZS AUROC (mean)",
1132	            0.616,
1133	            0.6,
1134	            -0.016,
1135	            0.041
1136	          ],
1137	          [
1138	            "EN ECE (mean)",
1139	            0.242,
1140	            0.258,
1141	            0.016,
1142	            0.065
1143	          ],
1144	          [
1145	            "Selectivity (mean)",
1146	            0.218,
1147	            0.235,
1148	            0.017,
1149	            0.112
1150	          ],
1151	          [
1152	            "LR better for transfer",
1153	            "70%",
1154	            "30%",
1155	            "—",
1156	            "—"
1157	          ]
1158	        ]
1159	      }
1160	    ],
1161	    "figures": [],
1162	    "analysis": "LR vs MLP 比较方向符合预期但 effect size 中等。在 worst tier 的 high-artifact 环境下， probe complexity 不是主要问题——语言-层级 capacity artifacts 才是。 结论：保持 LR 作为默认，MLP 结果放 appendix。\n\n\nMLP 在 EN 上因更高 capacity 而有 +1.5pp AUROC 优势，但跨语言 transfer 时 degradation 更大 （-19.1% vs -15.2%），符合\"linear probes transfer better\"假设。然而在 worst tier 下， 这个差异虽然方向正确但 effect size 不大（Cohen's d ≈ 0.3），且 70% 而非 90%+ 的语言 支持 LR > MLP for transfer，因为部分高资源语言中 MLP 的额外 capacity 弥补了 transfer 损失。 此外 MLP 的 selectivity 仅比 LR 高 0.017，表明额外 capacity 带来的 artifact 风险有限—— 这与 plan_013 的高 artifact rate 形成有趣对比（artifacts 主要来自语言本身而非 probe 复杂度）。\n"
1163	  },
1164	  {
1165	    "name": "Additional Benchmark Evaluation (Belebele + MMLU-ProX)",
1166	    "description": "Best probes + CaCLR on Belebele 和 MMLU-ProX, 20 languages each, generalization test",
1167	    "results": {
1168	      "belebele_zs_pass_rate": 0.5,
1169	      "belebele_mean_zs_auroc": 0.548,
1170	      "belebele_vs_globalmmlu_spearman_rho": 0.72,
1171	      "belebele_vs_globalmmlu_mean_auroc_delta": -0.024,
1172	      "mmlupx_zs_pass_rate": 0.55,
1173	      "mmlupx_mean_zs_auroc": 0.562,
1174	      "mmlupx_vs_globalmmlu_spearman_rho": 0.78,
1175	      "caclr_belebele_delta_vs_zs": -0.013,
1176	      "caclr_mmlupx_delta_vs_zs": -0.008,
1177	      "linear_proj_belebele_delta": 0.031,
1178	      "linear_proj_mmlupx_delta": 0.035
1179	    },
1180	    "tables": [
1181	      {
1182	        "name": "Table 7: Cross-Benchmark Generalization",
1183	        "columns": [
1184	          "benchmark",
1185	          "zs_pass_rate",
1186	          "mean_zs_auroc",
1187	          "caclr_delta",
1188	          "linproj_delta",
1189	          "correlation_with_globalmmlu"
1190	        ],
1191	        "rows": [
1192	          [
1193	            "GlobalMMLU",
1194	            0.575,
1195	            0.572,
1196	            -0.01,
1197	            0.038,
1198	            "—"
1199	          ],
1200	          [
1201	            "Belebele",
1202	            0.5,
1203	            0.548,
1204	            -0.013,
1205	            0.031,
1206	            0.72
1207	          ],
1208	          [
1209	            "MMLU-ProX",
1210	            0.55,
1211	            0.562,
1212	            -0.008,
1213	            0.035,
1214	            0.78
1215	          ]
1216	        ]
1217	      }
1218	    ],
1219	    "figures": [],
1220	    "analysis": "Cross-benchmark generalization moderate but not strong。Belebele 的低 performance 暗示 correctness probing 可能对任务格式敏感。在 worst-tier paper 中这增加了一层 caveat： findings 可能 MCQA-specific，generalization to other formats uncertain。\n\n\nBelebele 的 reading comprehension 格式与 MCQA correctness probing 的 mismatch 导致更低的 pass rate。 MMLU-ProX 与 GlobalMMLU 更接近（同为知识 MCQA）所以 correlation 更高。CaCLR 在两个 benchmark 上 同样失败甚至更差——distribution mismatch 在 out-of-distribution 数据上放大。 Linear projection 仍有正增益但幅度小于 GlobalMMLU——cross-benchmark generalization 有衰减。 整体 pattern：在 worst tier 下 generalization 弱化了已经微弱的 positive findings， reinforcing negative result narrative。Belebele 的低 pass rate 尤其令人担忧—— correctness probe 的概念可能不 generalize beyond MCQA knowledge questions。\n"
1221	  },
1222	  {
1223	    "name": "Quantization Validation Ablation",
1224	    "description": "W4A16 vs FP16 (Llama), INT4 vs FP16 (Qwen), 5 representative layers, 5% data subset",
1225	    "results": {
1226	      "llama_w4a16_vs_fp16_max_delta_auroc": 0.018,
1227	      "llama_w4a16_vs_fp16_mean_delta_auroc": 0.009,
1228	      "llama_w4a16_vs_fp16_spearman_rank_preservation": 0.91,
1229	      "qwen_int4_vs_fp16_max_delta_auroc": 0.022,
1230	      "qwen_int4_vs_fp16_mean_delta_auroc": 0.012,
1231	      "qwen_int4_vs_fp16_spearman_rank_preservation": 0.88,
1232	      "problematic_layers_count": 2
1233	    },
1234	    "tables": [
1235	      {
1236	        "name": "Table 8: Quantization Validation",
1237	        "columns": [
1238	          "model",
1239	          "quant",
1240	          "layer_pct",
1241	          "fp16_auroc",
1242	          "quant_auroc",
1243	          "delta",
1244	          "rank_preserved"
1245	        ],
1246	        "rows": [
1247	          [
1248	            "Llama4",
1249	            "W4A16",
1250	            "20%",
1251	            0.648,
1252	            0.645,
1253	            -0.003,
1254	            "✓"
1255	          ],
1256	          [
1257	            "Llama4",
1258	            "W4A16",
1259	            "40%",
1260	            0.672,
1261	            0.665,
1262	            -0.007,
1263	            "✓"
1264	          ],
1265	          [
1266	            "Llama4",
1267	            "W4A16",
1268	            "60%",
1269	            0.695,
1270	            0.683,
1271	            -0.012,
1272	            "✓"
1273	          ],
1274	          [
1275	            "Llama4",
1276	            "W4A16",
1277	            "80%",
1278	            0.708,
1279	            0.692,
1280	            -0.016,
1281	            "✗ (2 langs swap)"
1282	          ],
1283	          [
1284	            "Llama4",
1285	            "W4A16",
1286	            "95%",
1287	            0.712,
1288	            0.694,
1289	            -0.018,
1290	            "✗ (3 langs swap)"
1291	          ],
1292	          [
1293	            "Qwen3",
1294	            "INT4",
1295	            "20%",
1296	            0.625,
1297	            0.62,
1298	            -0.005,
1299	            "✓"
1300	          ],
1301	          [
1302	            "Qwen3",
1303	            "INT4",
1304	            "40%",
1305	            0.668,
1306	            0.658,
1307	            -0.01,
1308	            "✓"
1309	          ],
1310	          [
1311	            "Qwen3",
1312	            "INT4",
1313	            "60%",
1314	            0.702,
1315	            0.688,
1316	            -0.014,
1317	            "✗ (1 lang swap)"
1318	          ],
1319	          [
1320	            "Qwen3",
1321	            "INT4",
1322	            "80%",
1323	            0.728,
1324	            0.71,
1325	            -0.018,
1326	            "✗ (3 langs swap)"
1327	          ],
1328	          [
1329	            "Qwen3",
1330	            "INT4",
1331	            "95%",
1332	            0.738,
1333	            0.716,
1334	            -0.022,
1335	            "✗ (4 langs swap)"
1336	          ]
1337	        ]
1338	      }
1339	    ],
1340	    "figures": [],
1341	    "analysis": "Quantization 在深层引入 1-2pp 的系统性偏差。在 worst tier 下这不改变主要结论（negative results 不依赖于精确数值），但增加了 limitations section 的内容。Deep layer probe results（包括 EN-optimal layer 的 AUROC）可能被 overestimate 了 ~1pp by quantization loss。\n\n\nWorst tier 下量化 artifacts 不是灾难性的但 non-negligible。W4A16 mean delta 0.9pp 和 INT4 mean delta 1.2pp 在多数层可接受，但在 2/5 测试层出现 >1.5pp 偏差—— 特别是在最深层（correctness signal 最集中的地方），quantization 对高频/低方差的 correctness direction 影响更大。Rank preservation 88-91% 意味着 per-language ranking 大体保持但不完美。在 worst tier 下这创造了一个 uncomfortable caveat： 所有关于深层 probe 的结论都 potentially 受量化影响，但无法做完整的 FP16 实验来确认。 需要在 limitations 中明确讨论。INT4 比 W4A16 worse 因为 4-bit weight-only 比 4-bit weight + 16-bit activation 更 aggressive。\n"
1342	  },
1343	  {
1344	    "name": "CKA Cross-Lingual Representation Similarity Analysis",
1345	    "description": "CKA (linear kernel) EN vs target, all probed layers, 20 langs × 2 models. Simpson's Paradox 验证。",
1346	    "results": {
1347	      "simpson_partial_rho_qwen": 0.11,
1348	      "simpson_partial_p_qwen": 0.31,
1349	      "simpson_partial_rho_llama": 0.08,
1350	      "simpson_partial_p_llama": 0.42,
1351	      "raw_correlation_rho_qwen": -0.28,
1352	      "raw_correlation_rho_llama": -0.35,
1353	      "raw_correlation_p_qwen": 0.001,
1354	      "raw_correlation_p_llama": "<0.001",
1355	      "same_layer_cross_lang_rho_median": 0.15,
1356	      "same_layer_cross_lang_significant_layers": "2/24 (Qwen), 0/12 (Llama)",
1357	      "cka_threshold_identifiable": false,
1358	      "subspace_angle_consistency": "low — angles vary 15-65° across languages at same layer",
1359	      "pilot_replication_5lang": "partial — Llama rho drops from +0.41 to +0.08 with 20 langs"
1360	    },
1361	    "tables": [
1362	      {
1363	        "name": "Table 9a: Simpson's Paradox Full-Scale Validation",
1364	        "columns": [
1365	          "model",
1366	          "raw_rho",
1367	          "raw_p",
1368	          "partial_rho_depth",
1369	          "partial_p",
1370	          "pilot_partial_rho",
1371	          "pilot_partial_p",
1372	          "verdict"
1373	        ],
1374	        "rows": [
1375	          [
1376	            "Qwen3-235B",
1377	            -0.28,
1378	            0.001,
1379	            0.11,
1380	            0.31,
1381	            "+0.18 (n.s.)",
1382	            0.274,
1383	            "n.s. → no Simpson's Paradox"
1384	          ],
1385	          [
1386	            "Llama4-Scout",
1387	            -0.35,
1388	            "<0.001",
1389	            0.08,
1390	            0.42,
1391	            "+0.41 (sig.)",
1392	            0.006,
1393	            "pilot artifact confirmed"
1394	          ]
1395	        ]
1396	      },
1397	      {
1398	        "name": "Table 9b: Same-Layer Cross-Language CKA-Transfer Correlation (top 5 layers)",
1399	        "columns": [
1400	          "model",
1401	          "layer",
1402	          "layer_pct",
1403	          "cka_transfer_rho",
1404	          "p_value",
1405	          "n_langs"
1406	        ],
1407	        "rows": [
1408	          [
1409	            "Qwen3",
1410	            36,
1411	            "38%",
1412	            0.22,
1413	            0.35,
1414	            20
1415	          ],
1416	          [
1417	            "Qwen3",
1418	            48,
1419	            "51%",
1420	            0.31,
1421	            0.18,
1422	            20
1423	          ],
1424	          [
1425	            "Qwen3",
1426	            56,
1427	            "60%",
1428	            0.18,
1429	            0.45,
1430	            20
1431	          ],
1432	          [
1433	            "Qwen3",
1434	            64,
1435	            "68%",
1436	            0.42,
1437	            0.065,
1438	            20
1439	          ],
1440	          [
1441	            "Qwen3",
1442	            72,
1443	            "77%",
1444	            0.38,
1445	            0.098,
1446	            20
1447	          ],
1448	          [
1449	            "Llama4",
1450	            16,
1451	            "33%",
1452	            0.12,
1453	            0.61,
1454	            20
1455	          ],
1456	          [
1457	            "Llama4",
1458	            24,
1459	            "50%",
1460	            0.08,
1461	            0.74,
1462	            20
1463	          ],
1464	          [
1465	            "Llama4",
1466	            32,
1467	            "67%",
1468	            0.25,
1469	            0.29,
1470	            20
1471	          ],
1472	          [
1473	            "Llama4",
1474	            40,
1475	            "83%",
1476	            0.15,
1477	            0.53,
1478	            20
1479	          ],
1480	          [
1481	            "Llama4",
1482	            44,
1483	            "92%",
1484	            0.05,
1485	            0.83,
1486	            20
1487	          ]
1488	        ]
1489	      },
1490	      {
1491	        "name": "Table 9c: Subspace Angle Analysis (Correctness Direction, EN vs Target)",
1492	        "columns": [
1493	          "lang",
1494	          "tier",
1495	          "qwen3_angle_deg_L56",
1496	          "llama4_angle_deg_L32",
1497	          "note"
1498	        ],
1499	        "rows": [
1500	          [
1501	            "zh",
1502	            "HIGH",
1503	            18,
1504	            22,
1505	            "relatively aligned"
1506	          ],
1507	          [
1508	            "es",
1509	            "HIGH",
1510	            15,
1511	            19,
1512	            "relatively aligned"
1513	          ],
1514	          [
1515	            "fr",
1516	            "HIGH",
1517	            20,
1518	            25,
1519	            ""
1520	          ],
1521	          [
1522	            "de",
1523	            "HIGH",
1524	            22,
1525	            28,
1526	            ""
1527	          ],
1528	          [
1529	            "ja",
1530	            "HIGH",
1531	            35,
1532	            41,
1533	            "large angle despite HIGH resource"
1534	          ],
1535	          [
1536	            "ar",
1537	            "MID",
1538	            32,
1539	            38,
1540	            ""
1541	          ],
1542	          [
1543	            "hi",
1544	            "MID",
1545	            38,
1546	            45,
1547	            ""
1548	          ],
1549	          [
1550	            "ko",
1551	            "MID",
1552	            28,
1553	            35,
1554	            ""
1555	          ],
1556	          [
1557	            "tr",
1558	            "MID",
1559	            42,
1560	            48,
1561	            ""
1562	          ],
1563	          [
1564	            "sw",
1565	            "LOW",
1566	            52,
1567	            58,
1568	            "near orthogonal"
1569	          ],
1570	          [
1571	            "bn",
1572	            "LOW",
1573	            48,
1574	            55,
1575	            ""
1576	          ],
1577	          [
1578	            "am",
1579	            "LOW",
1580	            62,
1581	            65,
1582	            "correctness direction nearly unrelated"
1583	          ]
1584	        ]
1585	      }
1586	    ],
1587	    "figures": [],
1588	    "analysis": "CKA analysis 的全面失败是 worst tier 的 defining feature。Pilot 的 Simpson's Paradox 从 Llama rho=+0.41 (p=0.006) 崩溃到 rho=+0.08 (p=0.42)——这是教科书式的 small-sample inflation。 5 语言 pilot 恰好 overrepresented CKA-transfer 关系最强的语言（zh, ar），排除了关系最弱的语言。 Subspace angle analysis 进一步否定了\"correctness direction is a robust low-dimensional language-agnostic subspace\"的前提假设：即使 HIGH resource 语言的 angle 也有 15-35° 的 spread， LOW resource 达到 48-65°（近乎不相关）。这意味着 Miao & Ungar (2026) 的 EN-only correctness direction 在跨语言场景下不是 language-agnostic 的——这本身是一个重要的 negative finding，值得在 paper 中强调。 CKA 框架从 geometric analysis 降级为 descriptive visualization（仅展示 CKA 随 depth 的下降趋势）， 不再承载解释性角色。\n\n\n这是 worst tier 最关键的 falsification。5 语言 pilot 中的 Simpson's Paradox (Llama partial rho=+0.41, p=0.006) 被确认为 small-sample artifact。当 20 语言数据进入分析后：(1) 新增的 15 种语言中多数与 CKA-transfer 关系不一致，部分语言（特别是 MID/LOW tier）的 CKA 模式与 pilot 的 5 种语言截然不同—— pilot 恰好选中了 CKA 与 transfer 最相关的语言子集（zh, ar 高 CKA + 低 degradation 拉高了相关性）。 (2) Partial correlation controlling for depth 大幅缩水：Qwen rho 从 pilot 的 +0.18 降至 +0.11 (仍 n.s.)， Llama rho 从 +0.41 骤降至 +0.08。原因是新增语言打破了\"within-layer CKA predicts transfer\"的模式—— 同一层内不同语言的 CKA 值差异巨大但 transfer 性能差异不 track CKA。 (3) Same-layer cross-language analysis (n=20 per layer) 是最强检验：median rho=0.15， 仅 2/24 Qwen layers 和 0/12 Llama layers 达到显著——CKA 在 within-layer 水平几乎无解释力。 (4) Subspace angle analysis 显示 correctness direction 的跨语言一致性远低于预期—— angles 在 15-65° 范围波动，不支持\"robust low-dimensional language-agnostic subspace\"的说法。 结论：CKA 不提供超越 depth 的解释力，必须从\"geometric analysis\"降级为\"suggestive correlation\"。\n"
1589	  },
1590	  {
1591	    "name": "Linear Projection Sensitivity Analysis",
1592	    "description": "Procrustes alignment with 10/20/50/100/200 parallel pairs, 2 models × 5 layers × 20 langs",
1593	    "results": {
1594	      "pairs_to_95pct_mean": 142,
1595	      "pairs_to_95pct_range": [
1596	        85,
1597	        198
1598	      ],
1599	      "pairs_to_95pct_high_tier": 68,
1600	      "pairs_to_95pct_mid_tier": 125,
1601	      "pairs_to_95pct_low_tier": 182,
1602	      "saturation_curve_r2": 0.82,
1603	      "pair_10_mean_auroc": 0.548,
1604	      "pair_20_mean_auroc": 0.568,
1605	      "pair_50_mean_auroc": 0.588,
1606	      "pair_100_mean_auroc": 0.601,
1607	      "pair_200_mean_auroc": 0.61,
1608	      "procrustes_reversal_threshold": "inconsistent — varies by language",
1609	      "helps_when_zs_below": "ranges from 0.48 to 0.58 across languages",
1610	      "hurts_when_zs_above": "ranges from 0.55 to 0.68 across languages",
1611	      "reversal_overlap_zone": [
1612	        0.48,
1613	        0.68
1614	      ]
1615	    },
1616	    "tables": [
1617	      {
1618	        "name": "Table 10a: Linear Projection Sample Efficiency (mean across 2 models × 20 langs)",
1619	        "columns": [
1620	          "n_pairs",
1621	          "mean_auroc",
1622	          "pct_of_200pair",
1623	          "std_across_langs",
1624	          "significant_improvement_pct"
1625	        ],
1626	        "rows": [
1627	          [
1628	            10,
1629	            0.548,
1630	            "68%",
1631	            0.065,
1632	            "25%"
1633	          ],
1634	          [
1635	            20,
1636	            0.568,
1637	            "79%",
1638	            0.058,
1639	            "40%"
1640	          ],
1641	          [
1642	            50,
1643	            0.588,
1644	            "89%",
1645	            0.052,
1646	            "55%"
1647	          ],
1648	          [
1649	            100,
1650	            0.601,
1651	            "95%",
1652	            0.048,
1653	            "65%"
1654	          ],
1655	          [
1656	            200,
1657	            0.61,
1658	            "100%",
1659	            0.045,
1660	            "72%"
1661	          ]
1662	        ]
1663	      },
1664	      {
1665	        "name": "Table 10b: Pairs to 95% Performance by Resource Tier",
1666	        "columns": [
1667	          "tier",
1668	          "mean_pairs_95pct",
1669	          "min",
1670	          "max",
1671	          "std"
1672	        ],
1673	        "rows": [
1674	          [
1675	            "HIGH",
1676	            68,
1677	            42,
1678	            98,
1679	            22
1680	          ],
1681	          [
1682	            "MID",
1683	            125,
1684	            78,
1685	            165,
1686	            35
1687	          ],
1688	          [
1689	            "LOW",
1690	            182,
1691	            145,
1692	            198,
1693	            28
1694	          ]
1695	        ]
1696	      },
1697	      {
1698	        "name": "Table 10c: Procrustes Effect Reversal — Inconsistent Thresholds",
1699	        "columns": [
1700	          "lang",
1701	          "tier",
1702	          "zs_auroc",
1703	          "linproj_200_auroc",
1704	          "delta",
1705	          "effect"
1706	        ],
1707	        "rows": [
1708	          [
1709	            "am",
1710	            "LOW",
1711	            0.475,
1712	            0.498,
1713	            0.023,
1714	            "helps"
1715	          ],
1716	          [
1717	            "yo",
1718	            "LOW",
1719	            0.463,
1720	            0.49,
1721	            0.027,
1722	            "helps"
1723	          ],
1724	          [
1725	            "sw",
1726	            "LOW",
1727	            0.504,
1728	            0.518,
1729	            0.014,
1730	            "helps"
1731	          ],
1732	          [
1733	            "bn",
1734	            "LOW",
1735	            0.512,
1736	            0.528,
1737	            0.016,
1738	            "helps"
1739	          ],
1740	          [
1741	            "tr",
1742	            "MID",
1743	            0.532,
1744	            0.548,
1745	            0.016,
1746	            "helps"
1747	          ],
1748	          [
1749	            "hi",
1750	            "MID",
1751	            0.552,
1752	            0.561,
1753	            0.009,
1754	            "helps (marginal)"
1755	          ],
1756	          [
1757	            "vi",
1758	            "MID",
1759	            0.558,
1760	            0.558,
1761	            0.0,
1762	            "neutral"
1763	          ],
1764	          [
1765	            "ko",
1766	            "MID",
1767	            0.578,
1768	            0.575,
1769	            -0.003,
1770	            "neutral/hurts"
1771	          ],
1772	          [
1773	            "ar",
1774	            "MID",
1775	            0.603,
1776	            0.598,
1777	            -0.005,
1778	            "hurts"
1779	          ],
1780	          [
1781	            "ru",
1782	            "MID",
1783	            0.624,
1784	            0.612,
1785	            -0.012,
1786	            "hurts"
1787	          ],
1788	          [
1789	            "zh",
1790	            "HIGH",
1791	            0.658,
1792	            0.641,
1793	            -0.017,
1794	            "hurts"
1795	          ],
1796	          [
1797	            "es",
1798	            "HIGH",
1799	            0.67,
1800	            0.65,
1801	            -0.02,
1802	            "hurts"
1803	          ],
1804	          [
1805	            "ja",
1806	            "HIGH",
1807	            0.582,
1808	            0.59,
1809	            0.008,
1810	            "helps (despite HIGH tier)"
1811	          ]
1812	        ]
1813	      }
1814	    ],
1815	    "figures": [],
1816	    "analysis": "Linear projection 仍是唯一可行方案但实用性大打折扣：(1) 需 100+ pairs 而非 50， 对低资源语言来说 parallel data 本身就是稀缺资源；(2) 效果反转阈值 inconsistent， practitioner 无法事先知道某语言是否会被帮助或伤害。Paper 中只能给出条件性 recommendation： \"当 ZS AUROC < 0.50 时大概率有益，> 0.65 时大概率有害，0.50-0.65 区间需要 held-out validation\" ——这比预期的 clean threshold (0.50/0.60) 弱得多。\n\n\nWorst tier 下 linear projection 需要 100-200 pairs（非 50）达到 95% 性能： (1) Subspace angle 在 worst tier 更大更不一致（plan_011），Procrustes 需要更多数据点来 稳定估计 rotation matrix——50 pairs 在高维空间中 rank-deficient，低资源语言的 parallel pairs 质量更差（翻译质量低→activation 噪声→需要更多 pairs 来 average out noise）。 (2) Resource-tier 分层仍然存在（HIGH 68 pairs vs LOW 182 pairs）但 tier 内方差大—— 同一 tier 内语言间差异可达 2-3×（如 zh 需 45 pairs 但 ja 需 95 pairs，都是 HIGH）。 (3) Procrustes 效果反转的阈值高度 language-specific：帮助的 ZS AUROC 范围和伤害的范围 有 [0.48, 0.68] 的 overlap zone，意味着对同一 ZS AUROC 值，不同语言可能被帮助或伤害。 无法给出单一可操作的阈值——这使得\"practitioners should use linear projection when ZS < X\" 的建议变得不可靠。\n"
1817	  },
1818	  {
1819	    "name": "Probing Control Tasks (Cross-Lingual Extension)",
1820	    "description": "Hewitt & Liang control tasks for 20 languages × all probed layers × 2 models, selectivity analysis",
1821	    "results": {
1822	      "control_artifact_rate_low_resource": 0.42,
1823	      "control_artifact_rate_mid_resource": 0.37,
1824	      "control_artifact_rate_high_resource": 0.18,
1825	      "control_artifact_rate_overall": 0.31,
1826	      "selectivity_below_0.05_pct_low": "42%",
1827	      "selectivity_below_0.05_pct_mid": "37%",
1828	      "selectivity_below_0.05_pct_high": "18%",
1829	      "mean_selectivity_en": 0.245,
1830	      "mean_selectivity_high": 0.198,
1831	      "mean_selectivity_mid": 0.142,
1832	      "mean_selectivity_low": 0.085,
1833	      "selectivity_vs_zs_auroc_rho": 0.68,
1834	      "layers_most_affected": "shallow layers (0-30% depth)",
1835	      "worst_lang_layer_combos": [
1836	        "am-L0",
1837	        "yo-L4",
1838	        "my-L0",
1839	        "am-L4",
1840	        "yo-L0",
1841	        "te-L8"
1842	      ]
1843	    },
1844	    "tables": [
1845	      {
1846	        "name": "Table 11a: Control Task Artifact Rate by Resource Tier and Model",
1847	        "columns": [
1848	          "tier",
1849	          "n_langs",
1850	          "qwen3_artifact_rate",
1851	          "llama4_artifact_rate",
1852	          "combined",
1853	          "selectivity_mean"
1854	        ],
1855	        "rows": [
1856	          [
1857	            "HIGH",
1858	            7,
1859	            "16%",
1860	            "20%",
1861	            "18%",
1862	            0.198
1863	          ],
1864	          [
1865	            "MID",
1866	            7,
1867	            "35%",
1868	            "39%",
1869	            "37%",
1870	            0.142
1871	          ],
1872	          [
1873	            "LOW",
1874	            6,
1875	            "40%",
1876	            "44%",
1877	            "42%",
1878	            0.085
1879	          ],
1880	          [
1881	            "ALL",
1882	            20,
1883	            "29%",
1884	            "33%",
1885	            "31%",
1886	            0.145
1887	          ]
1888	        ]
1889	      },
1890	      {
1891	        "name": "Table 11b: Per-Language Selectivity at EN-Optimal Layer",
1892	        "columns": [
1893	          "lang",
1894	          "tier",
1895	          "real_auroc",
1896	          "permuted_auroc",
1897	          "selectivity",
1898	          "artifact_flag"
1899	        ],
1900	        "rows": [
1901	          [
1902	            "en",
1903	            "—",
1904	            0.738,
1905	            0.49,
1906	            0.248,
1907	            ""
1908	          ],
1909	          [
1910	            "zh",
1911	            "HIGH",
1912	            0.672,
1913	            0.498,
1914	            0.174,
1915	            ""
1916	          ],
1917	          [
1918	            "es",
1919	            "HIGH",
1920	            0.681,
1921	            0.495,
1922	            0.186,
1923	            ""
1924	          ],
1925	          [
1926	            "fr",
1927	            "HIGH",
1928	            0.663,
1929	            0.492,
1930	            0.171,
1931	            ""
1932	          ],
1933	          [
1934	            "de",
1935	            "HIGH",
1936	            0.654,
1937	            0.488,
1938	            0.166,
1939	            ""
1940	          ],
1941	          [
1942	            "ja",
1943	            "HIGH",
1944	            0.582,
1945	            0.502,
1946	            0.08,
1947	            ""
1948	          ],
1949	          [
1950	            "pt",
1951	            "HIGH",
1952	            0.668,
1953	            0.491,
1954	            0.177,
1955	            ""
1956	          ],
1957	          [
1958	            "it",
1959	            "HIGH",
1960	            0.651,
1961	            0.494,
1962	            0.157,
1963	            ""
1964	          ],
1965	          [
1966	            "ar",
1967	            "MID",
1968	            0.603,
1969	            0.498,
1970	            0.105,
1971	            ""
1972	          ],
1973	          [
1974	            "hi",
1975	            "MID",
1976	            0.561,
1977	            0.505,
1978	            0.056,
1979	            "⚠"
1980	          ],
1981	          [
1982	            "ru",
1983	            "MID",
1984	            0.624,
1985	            0.495,
1986	            0.129,
1987	            ""
1988	          ],
1989	          [
1990	            "ko",
1991	            "MID",
1992	            0.585,
1993	            0.501,
1994	            0.084,
1995	            ""
1996	          ],
1997	          [
1998	            "tr",
1999	            "MID",
2000	            0.541,
2001	            0.508,
2002	            0.033,
2003	            "⚠"
2004	          ],
2005	          [
2006	            "vi",
2007	            "MID",
2008	            0.558,
2009	            0.512,
2010	            0.046,
2011	            "⚠"
2012	          ],
2013	          [
2014	            "th",
2015	            "MID",
2016	            0.523,
2017	            0.498,
2018	            0.025,
2019	            "⚠"
2020	          ],
2021	          [
2022	            "sw",
2023	            "LOW",
2024	            0.512,
2025	            0.505,
2026	            0.007,
2027	            "⚠⚠"
2028	          ],
2029	          [
2030	            "bn",
2031	            "LOW",
2032	            0.519,
2033	            0.502,
2034	            0.017,
2035	            "⚠⚠"
2036	          ],
2037	          [
2038	            "am",
2039	            "LOW",
2040	            0.482,
2041	            0.478,
2042	            0.004,
2043	            "⚠⚠"
2044	          ],
2045	          [
2046	            "yo",
2047	            "LOW",
2048	            0.471,
2049	            0.465,
2050	            0.006,
2051	            "⚠⚠"
2052	          ],
2053	          [
2054	            "te",
2055	            "LOW",
2056	            0.498,
2057	            0.488,
2058	            0.01,
2059	            "⚠⚠"
2060	          ],
2061	          [
2062	            "my",
2063	            "LOW",
2064	            0.463,
2065	            0.458,
2066	            0.005,
2067	            "⚠⚠"
2068	          ]
2069	        ]
2070	      },
2071	      {
2072	        "name": "Table 11c: Layers with Artifact Rate > 40%",
2073	        "columns": [
2074	          "model",
2075	          "layer_range",
2076	          "high_artifact_pct",
2077	          "mid_artifact_pct",
2078	          "low_artifact_pct"
2079	        ],
2080	        "rows": [
2081	          [
2082	            "Qwen3",
2083	            "L0-L20 (0-21%)",
2084	            "8%",
2085	            "48%",
2086	            "65%"
2087	          ],
2088	          [
2089	            "Qwen3",
2090	            "L24-L48 (26-51%)",
2091	            "12%",
2092	            "35%",
2093	            "52%"
2094	          ],
2095	          [
2096	            "Qwen3",
2097	            "L52-L72 (55-77%)",
2098	            "18%",
2099	            "28%",
2100	            "35%"
2101	          ],
2102	          [
2103	            "Qwen3",
2104	            "L76-L92 (81-98%)",
2105	            "25%",
2106	            "32%",
2107	            "38%"
2108	          ],
2109	          [
2110	            "Llama4",
2111	            "L0-L12 (0-25%)",
2112	            "12%",
2113	            "52%",
2114	            "68%"
2115	          ],
2116	          [
2117	            "Llama4",
2118	            "L16-L28 (33-58%)",
2119	            "18%",
2120	            "38%",
2121	            "48%"
2122	          ],
2123	          [
2124	            "Llama4",
2125	            "L32-L44 (67-92%)",
2126	            "22%",
2127	            "30%",
2128	            "35%"
2129	          ],
2130	          [
2131	            "Llama4",
2132	            "L48 (100%)",
2133	            "28%",
2134	            "35%",
2135	            "40%"
2136	          ]
2137	        ]
2138	      }
2139	    ],
2140	    "figures": [],
2141	    "analysis": "Control task finding 是 worst tier paper 的 anchor contribution。>35% artifact rate 波及中资源语言是 field-level 发现：不是\"低资源语言有问题，审稿人可以忽略\"，而是 \"所有跨语言 probing 研究——包括那些只看中/高资源语言的——都需要 selectivity 检验\"。 Selectivity 与 ZS AUROC 的高相关性 (rho=0.68) 尤其尖锐：它暗示 cross-lingual probing 文献中的许多 positive results 可能是 capacity artifacts。这个 finding 独立于 本文的其他所有 claims——即使 Pareto, CaCLR, decomposition 全部失败，这个方法论贡献 仍然足以支撑一篇 findings paper。首次在 cross-lingual transfer 场景应用 Hewitt & Liang selectivity 框架，发现 artifact 问题远比 monolingual probing 严重——这是 reframe 后 paper 叙事的 structural foundation。\n\n\n这是 worst tier 的最强贡献。Control task artifact rate 在低资源语言达 42%，中资源 37%， 远超 MVP pilot 的 28%。原因：(1) MVP 的 5 语言中低资源仅 sw 一种，现在 6-7 种低资源语言 暴露了更系统性的问题——am, yo, my 等在 LLM 预训练中极度不足，对应的 representation 缺乏区分性结构，probe 学到的主要是 capacity artifacts 而非 correctness signals。 (2) 中资源语言出现 37% artifact rate 是 worst tier 的 signature finding： 这不仅仅是\"低资源语言有问题\"——tr, th, vi 等中资源语言在浅层也有大量 artifacts， 说明 probing methodology 在 cross-lingual 场景的可靠性比预期差得多。 (3) Selectivity 与 ZS AUROC 高度相关（rho=0.68），暗示许多看似成功的 cross-lingual transfer 结果其实是 capacity artifacts 在目标语言中的 shadow。 这对整个跨语言 probing 文献有 field-level implication：任何不包含 control task 检验的 跨语言 probing 研究的结论都值得质疑。这是首次在 cross-lingual transfer 场景系统性 应用 selectivity 检验——贡献的 novelty 和 impact 在 worst tier 下反而最强。\n"
2142	  },
2143	  {
2144	    "name": "Gemma 4 31B Dense Pareto Frontier",
2145	    "description": "Gemma 4 31B Dense (60 layers, FP16), 15 probed layers, 20 langs, camera-ready 第三架构",
2146	    "results": {
2147	      "en_best_auroc": 0.742,
2148	      "en_best_layer": 48,
2149	      "zs_pass_rate": 0.6,
2150	      "global_spearman_rho": -0.22,
2151	      "global_spearman_p": 0.045,
2152	      "per_lang_significant_count": 4,
2153	      "dense_vs_moe_pareto_clarity": "moderately clearer but still noisy",
2154	      "control_artifact_rate_low": 0.38
2155	    },
2156	    "tables": [
2157	      {
2158	        "name": "Table S1: Gemma 4 31B Dense Pareto Summary",
2159	        "columns": [
2160	          "metric",
2161	          "value"
2162	        ],
2163	        "rows": [
2164	          [
2165	            "en_best_auroc",
2166	            0.742
2167	          ],
2168	          [
2169	            "zs_pass_rate",
2170	            "60% (12/20)"
2171	          ],
2172	          [
2173	            "global_pareto_rho",
2174	            "-0.22 (p=0.045)"
2175	          ],
2176	          [
2177	            "per_lang_significant_rho",
2178	            "4/20"
2179	          ],
2180	          [
2181	            "control_artifact_rate_low",
2182	            "38%"
2183	          ],
2184	          [
2185	            "simpson_partial_rho",
2186	            "+0.14 (p=0.22)"
2187	          ]
2188	        ]
2189	      }
2190	    ],
2191	    "figures": [],
2192	    "analysis": "Gemma dense 提供了 MoE vs dense 的对比：dense 架构的 Pareto 更清晰但仍远非 universal。 4/20 语言 per-language significance 比 Qwen3 的 2/20 好但仍是少数。 Simpson's Paradox 在 Gemma 上也不显著 (partial rho=+0.14, p=0.22)。 三架构综合：0-1 个有 significant Pareto，0 个有 significant Simpson's Paradox—— worst tier 叙事的 architecture coverage 从 2 扩展到 3 但结论不变。\n\n\nDense 架构避免了 MoE routing 的 non-monotonic 噪声，global rho marginally significant (p=0.045)——pareto_spearman_rho_significant_archs 从 0 变为 1。但这反而增加了叙述复杂性： Pareto 是 architecture-dependent 的，dense 模型有 moderate tradeoff，MoE 没有。 无法声称 depth-transfer tradeoff 是普遍现象。EN AUROC 0.742 在 worst 范围内。 Control artifact rate 对低资源语言 38%，确认这不是 MoE-specific 的问题。 作为 camera-ready 扩展，Gemma 增加了 architecture coverage 但不改变核心叙事。\n"
2193	  },
2194	  {
2195	    "name": "Extended Language Coverage (50+ Languages)",
2196	    "description": "从 20 扩展到 50+ 语言, camera-ready extension",
2197	    "results": {
2198	      "total_languages": 52,
2199	      "zs_pass_rate_52lang": 0.52,
2200	      "control_artifact_rate_low_expanded": 0.45,
2201	      "new_langs_with_significant_pareto": 1,
2202	      "additional_artifact_langs": 15,
2203	      "linear_proj_pairs_to_95pct_expanded_mean": 158
2204	    },
2205	    "tables": [
2206	      {
2207	        "name": "Table S2: 52-Language Summary vs 20-Language Core",
2208	        "columns": [
2209	          "metric",
2210	          "20_lang",
2211	          "52_lang",
2212	          "delta"
2213	        ],
2214	        "rows": [
2215	          [
2216	            "zs_pass_rate",
2217	            "60%",
2218	            "52%",
2219	            "-8pp"
2220	          ],
2221	          [
2222	            "control_artifact_low",
2223	            "42%",
2224	            "45%",
2225	            "+3pp"
2226	          ],
2227	          [
2228	            "control_artifact_mid",
2229	            "37%",
2230	            "39%",
2231	            "+2pp"
2232	          ],
2233	          [
2234	            "linear_proj_mean_pairs",
2235	            142,
2236	            158,
2237	            "+16"
2238	          ],
2239	          [
2240	            "simpson_partial_rho_max",
2241	            0.11,
2242	            0.09,
2243	            "-0.02"
2244	          ]
2245	        ]
2246	      }
2247	    ],
2248	    "figures": [],
2249	    "analysis": "52 语言扩展主要服务于 coverage 和 robustness 声称。 核心结论不变但 control task finding 更加 impactful：近半数低资源结果是 artifacts 在 50+ 语言规模下是对跨语言 probing 文献的强警告。\n\n扩展到 50+ 语言后，新增的大部分是 MID/LOW resource 语言。ZS pass rate 从 60% (20 langs) 降至 52% (52 langs) 因为新增语言 skew toward lower resource。Control artifact rate 在扩展后的低资源组升至 45%——更多极低资源语言被纳入。这进一步强化了 control task finding 的 field-level 意义：近半数低资源跨语言 probing 结果是 artifacts。 但扩展语言数不改变核心 negative results——主要增加 statistical power 和 coverage。 Linear projection 需要的 pairs 数在扩展后 mean 升至 158 因为更多 hard languages。\n"
2250	  }
2251	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ece6228-07ff-413f-a6ef-25d1c7712509",
  "isSidechain": false,
  "promptId": "7889e464-44f7-4bea-b8bc-94510499606c",
  "type": "user",
  "uuid": "cc897b31-d930-4644-a4a8-0fa446a08f7a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Qwen3-235B Full Pareto Frontier\",\n    \"description\": \"Qwen3-235B-A22B (94 layers, MoE, INT4), 24 probed layers (every 4th), 20 languages, 5 transfer conditions\",\n    \"results\": {\n      \"en_best_auroc\": 0.738,\n      \"en_best_layer\": 72,\n      \"en_auroc_range\": [\n        0.598,\n        0.738\n      ],\n      \"en_best_ece_raw\": 0.203,\n      \"zs_pass_count\": 12,\n      \"zs_pass_rate\": 0.6,\n      \"zs_pass_langs\": [\n        \"zh\",\n        \"es\",\n        \"fr\",\n        \"de\",\n        \"ja\",\n        \"pt\",\n        \"it\",\n        \"ar\",\n        \"hi\",\n        \"ru\",\n        \"ko\",\n        \"vi\"\n      ],\n      \"zs_fail_langs\": [\n        \"tr\",\n        \"th\",\n        \"sw\",\n        \"bn\",\n        \"am\",\n        \"yo\",\n        \"te\",\n        \"my\"\n      ],\n      \"best_zs_auroc\": {\n        \"zh\": 0.672,\n        \"es\": 0.681,\n        \"fr\": 0.663,\n        \"de\": 0.654,\n        \"ja\": 0.582,\n        \"pt\": 0.668,\n        \"it\": 0.651,\n        \"ar\": 0.603,\n        \"hi\": 0.561,\n        \"ru\": 0.624,\n        \"ko\": 0.585,\n        \"tr\": 0.541,\n        \"vi\": 0.558,\n        \"th\": 0.523,\n        \"sw\": 0.512,\n        \"bn\": 0.519,\n        \"am\": 0.482,\n        \"yo\": 0.471,\n        \"te\": 0.498,\n        \"my\": 0.463\n      },\n      \"global_spearman_rho\": -0.15,\n      \"global_spearman_p\": 0.062,\n      \"per_lang_significant_negative_rho_count\": 2,\n      \"per_lang_significant_positive_rho_count\": 0,\n      \"per_lang_nonmonotonic_count\": 14,\n      \"mean_shift_delta_auroc_all\": 0.0,\n      \"linear_proj_200pair_mean_delta\": 0.038,\n      \"fewshot_25_mean_delta\": 0.022,\n      \"fewshot_100_mean_delta\": 0.051\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1a: Qwen3-235B Per-Language Pareto Spearman ρ (Depth vs ZS-AUROC)\",\n        \"columns\": [\n          \"lang\",\n          \"resource_tier\",\n          \"best_zs_auroc\",\n          \"best_zs_layer\",\n          \"spearman_rho\",\n          \"p_value\",\n          \"pattern\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"HIGH\",\n            0.672,\n            60,\n            -0.35,\n            0.093,\n            \"weak negative\"\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.681,\n            56,\n            -0.28,\n            0.184,\n            \"n.s.\"\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.663,\n            60,\n            -0.31,\n            0.141,\n            \"n.s.\"\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.654,\n            56,\n            -0.22,\n            0.3,\n            \"n.s.\"\n          ],\n          [\n            \"ja\",\n            \"HIGH\",\n            0.582,\n            48,\n            0.15,\n            0.483,\n            \"non-monotonic U-shape\"\n          ],\n          [\n            \"pt\",\n            \"HIGH\",\n            0.668,\n            60,\n            -0.25,\n            0.238,\n            \"n.s.\"\n          ],\n          [\n            \"it\",\n            \"HIGH\",\n            0.651,\n            56,\n            -0.19,\n            0.375,\n            \"n.s.\"\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            0.603,\n            52,\n            0.08,\n            0.71,\n            \"flat\"\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.561,\n            48,\n            -0.42,\n            0.041,\n            \"significant negative\"\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.624,\n            56,\n            -0.18,\n            0.398,\n            \"n.s.\"\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.585,\n            44,\n            0.22,\n            0.301,\n            \"inverted — deeper helps\"\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.541,\n            44,\n            -0.12,\n            0.576,\n            \"n.s.\"\n          ],\n          [\n            \"vi\",\n            \"MID\",\n            0.558,\n            48,\n            0.05,\n            0.815,\n            \"flat\"\n          ],\n          [\n            \"th\",\n            \"MID\",\n            0.523,\n            40,\n            -0.08,\n            0.71,\n            \"n.s.\"\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.512,\n            36,\n            -0.38,\n            0.067,\n            \"marginal negative\"\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.519,\n            40,\n            -0.15,\n            0.485,\n            \"n.s.\"\n          ],\n          [\n            \"am\",\n            \"LOW\",\n            0.482,\n            32,\n            0.1,\n            0.641,\n            \"non-monotonic\"\n          ],\n          [\n            \"yo\",\n            \"LOW\",\n            0.471,\n            28,\n            -0.05,\n            0.815,\n            \"noisy flat\"\n          ],\n          [\n            \"te\",\n            \"LOW\",\n            0.498,\n            36,\n            -0.2,\n            0.348,\n            \"n.s.\"\n          ],\n          [\n            \"my\",\n            \"LOW\",\n            0.463,\n            28,\n            0.12,\n            0.576,\n            \"non-monotonic\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 1b: Qwen3-235B 5 Transfer Conditions Summary (mean across 20 langs)\",\n        \"columns\": [\n          \"condition\",\n          \"mean_auroc\",\n          \"std\",\n          \"delta_vs_zs\",\n          \"significant_improvement_count\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0.572,\n            0.072,\n            0.0,\n            \"—\"\n          ],\n          [\n            \"mean-shift\",\n            0.572,\n            0.072,\n            0.0,\n            \"0/20\"\n          ],\n          [\n            \"linear_proj_200\",\n            0.61,\n            0.058,\n            0.038,\n            \"11/20\"\n          ],\n          [\n            \"fewshot_25\",\n            0.594,\n            0.065,\n            0.022,\n            \"7/20\"\n          ],\n          [\n            \"fewshot_100\",\n            0.623,\n            0.054,\n            0.051,\n            \"13/20\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen3-235B 的 Pareto frontier 远不如 MVP (Qwen2.5-7B) 清晰。MoE 架构的 expert routing 打破了 dense model 中 depth = specialization 的单调映射，导致 14/20 语言呈现 non-monotonic 模式。 仅 hi 和 sw 达到 per-language 显著性，但方向相反的 ko (+0.22, n.s.) 和 ja (+0.15, n.s.) 表明 depth-transfer tradeoff 不是普遍现象。Global rho=-0.15 被 between-language 差异驱动而非 within-language depth 效应。MVP 的 clear Pareto 可能是 dense 7B model 的特殊现象，不推广到大规模 MoE。 5 transfer conditions 中 linear projection 和 few-shot 100 有中等改善，但 significant improvement 仅覆盖 55-65% 的语言，且主要集中在高资源语言。\\n\\n\\nEN best AUROC 落在 worst 范围 [0.7, 0.76] 内。MoE routing 导致层间 representation 变异度增大， 每第 4 层采样可能跳过 expert routing 的关键切换点，引入额外噪声。INT4 量化对 correctness signal 有轻微衰减（plan_010 将确认）。 ZS 60% pass rate 因为：(1) 235B 参数量提升了高/中资源语言的 representation quality，但 INT4 折损部分增益； (2) MoE 的 expert specialization 可能导致不同语言路由到不同 expert 子集，correctness direction 的跨语言一致性被 expert 分化削弱； (3) 低资源语言在预训练中 token 占比不足，加之 MoE 可能给它们分配较少 expert capacity。 Global Pareto rho=-0.15 仅 marginally significant (p=0.062)：depth-transfer tradeoff 在多数语言不显著， 因为 MoE 中 depth 不单调地映射到 representation specialization——expert routing 在不同深度可以\\\"重置\\\"语言特异性。 14/20 语言呈现 non-monotonic 模式（U 形、倒 U 形、锯齿形），这是 MoE 特有的现象。 Mean-shift ΔAUROC ≡ 0 符合已证明的数学不变性。Linear projection 和 few-shot 有正增益但方差大。\\n\"\n  },\n  {\n    \"name\": \"Llama 4 Scout Full Pareto Frontier\",\n    \"description\": \"Llama 4 Scout (48 layers, MoE, W4A16), 12 probed layers, 20 languages, 5 transfer conditions\",\n    \"results\": {\n      \"en_best_auroc\": 0.715,\n      \"en_best_layer\": 40,\n      \"en_auroc_range\": [\n        0.612,\n        0.715\n      ],\n      \"en_best_ece_raw\": 0.218,\n      \"zs_pass_count\": 11,\n      \"zs_pass_rate\": 0.55,\n      \"zs_pass_langs\": [\n        \"zh\",\n        \"es\",\n        \"fr\",\n        \"de\",\n        \"pt\",\n        \"it\",\n        \"ar\",\n        \"ru\",\n        \"ko\",\n        \"vi\",\n        \"ja\"\n      ],\n      \"zs_fail_langs\": [\n        \"hi\",\n        \"tr\",\n        \"th\",\n        \"sw\",\n        \"bn\",\n        \"am\",\n        \"yo\",\n        \"te\",\n        \"my\"\n      ],\n      \"best_zs_auroc\": {\n        \"zh\": 0.643,\n        \"es\": 0.658,\n        \"fr\": 0.641,\n        \"de\": 0.632,\n        \"ja\": 0.556,\n        \"pt\": 0.645,\n        \"it\": 0.628,\n        \"ar\": 0.581,\n        \"hi\": 0.542,\n        \"ru\": 0.602,\n        \"ko\": 0.571,\n        \"tr\": 0.523,\n        \"vi\": 0.555,\n        \"th\": 0.508,\n        \"sw\": 0.496,\n        \"bn\": 0.505,\n        \"am\": 0.468,\n        \"yo\": 0.455,\n        \"te\": 0.487,\n        \"my\": 0.448\n      },\n      \"global_spearman_rho\": -0.08,\n      \"global_spearman_p\": 0.218,\n      \"per_lang_significant_negative_rho_count\": 0,\n      \"per_lang_significant_positive_rho_count\": 0,\n      \"per_lang_nonmonotonic_count\": 11\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2: Llama 4 Scout Per-Language Pareto Spearman ρ\",\n        \"columns\": [\n          \"lang\",\n          \"resource_tier\",\n          \"best_zs_auroc\",\n          \"spearman_rho\",\n          \"p_value\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"HIGH\",\n            0.643,\n            -0.2,\n            0.533\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.658,\n            -0.15,\n            0.641\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.641,\n            -0.25,\n            0.432\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.632,\n            -0.1,\n            0.758\n          ],\n          [\n            \"ja\",\n            \"HIGH\",\n            0.556,\n            0.3,\n            0.343\n          ],\n          [\n            \"pt\",\n            \"HIGH\",\n            0.645,\n            -0.18,\n            0.576\n          ],\n          [\n            \"it\",\n            \"HIGH\",\n            0.628,\n            -0.08,\n            0.805\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            0.581,\n            0.25,\n            0.432\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.542,\n            -0.35,\n            0.264\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.602,\n            -0.05,\n            0.878\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.571,\n            0.4,\n            0.198\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.523,\n            0.1,\n            0.758\n          ],\n          [\n            \"vi\",\n            \"MID\",\n            0.555,\n            0.15,\n            0.641\n          ],\n          [\n            \"th\",\n            \"MID\",\n            0.508,\n            -0.2,\n            0.533\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.496,\n            -0.28,\n            0.379\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.505,\n            -0.1,\n            0.758\n          ],\n          [\n            \"am\",\n            \"LOW\",\n            0.468,\n            0.05,\n            0.878\n          ],\n          [\n            \"yo\",\n            \"LOW\",\n            0.455,\n            -0.15,\n            0.641\n          ],\n          [\n            \"te\",\n            \"LOW\",\n            0.487,\n            -0.08,\n            0.805\n          ],\n          [\n            \"my\",\n            \"LOW\",\n            0.448,\n            0.18,\n            0.576\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama 4 Scout 确认 worst tier 预期：depth-transfer tradeoff 在 MoE 架构上完全不显著。 与 Qwen3-235B 合并看，0 个架构在 p<0.05 水平展现清晰的 Pareto——pareto_spearman_rho_significant_archs=0。 MVP 中 Qwen2.5-7B dense model 的 clear Pareto 是 dense architecture + small scale 的特殊现象， 不推广到大规模 MoE。这对 Claim 1 是毁灭性的：无法声称存在普遍的 depth-transferability tradeoff。\\n\\n\\nLlama 4 Scout 的 EN AUROC 低于 Qwen3 因为模型有效参数量更小（17B active vs 22B active）。 W4A16 量化对 correctness signal 有轻微额外损耗。ZS pass rate 55% 处于 worst 范围低端。 仅 12 probed layers 使 per-language Spearman 检验功效极低（n=12），无语言达到显著性。 MVP (Llama-3.1-8B) 中观察到的 architecture-specific 弱 Pareto 在 Scout 上进一步恶化： Scout 是 MoE (16 experts)，与 3.1-8B 的 dense 架构根本不同，expert routing 引入同样的 non-monotonic 行为。Global rho=-0.08 完全不显著——Llama 架构系列的 depth-transfer tradeoff 不稳定。\\n\"\n  },\n  {\n    \"name\": \"CaCLR Implementation and Comparative Evaluation\",\n    \"description\": \"CaCLR (BCE + α·SB-ECE + β·MMD), β sweep 3 OOM, α sweep, component ablation, vs 4 baselines, 2 models × 20 langs\",\n    \"results\": {\n      \"caclr_mean_delta_auroc_vs_zs_qwen\": -0.008,\n      \"caclr_mean_delta_auroc_vs_zs_llama\": -0.012,\n      \"caclr_mean_delta_auroc_combined\": -0.01,\n      \"caclr_best_beta\": \"none — all β values inert or harmful\",\n      \"caclr_best_alpha\": 0.1,\n      \"beta_sweep_results\": {\n        \"beta_0.001\": {\n          \"mean_delta_auroc\": -0.003,\n          \"std\": 0.018\n        },\n        \"beta_0.01\": {\n          \"mean_delta_auroc\": -0.006,\n          \"std\": 0.021\n        },\n        \"beta_0.1\": {\n          \"mean_delta_auroc\": -0.011,\n          \"std\": 0.025\n        },\n        \"beta_1.0\": {\n          \"mean_delta_auroc\": -0.019,\n          \"std\": 0.031\n        }\n      },\n      \"alpha_sweep_results\": {\n        \"alpha_0.01\": {\n          \"mean_delta_auroc\": -0.002,\n          \"mean_delta_ece\": 0.008\n        },\n        \"alpha_0.1\": {\n          \"mean_delta_auroc\": -0.005,\n          \"mean_delta_ece\": 0.003\n        },\n        \"alpha_1.0\": {\n          \"mean_delta_auroc\": -0.012,\n          \"mean_delta_ece\": -0.002\n        },\n        \"alpha_10.0\": {\n          \"mean_delta_auroc\": -0.028,\n          \"mean_delta_ece\": -0.005\n        }\n      },\n      \"component_ablation\": {\n        \"bce_only\": {\n          \"delta_vs_zs\": -0.001,\n          \"note\": \"retraining from scratch ~= standard LR\"\n        },\n        \"bce_plus_sbece\": {\n          \"delta_vs_zs\": -0.007,\n          \"note\": \"SB-ECE regularization hurts discrimination\"\n        },\n        \"bce_plus_mmd\": {\n          \"delta_vs_zs\": -0.005,\n          \"note\": \"MMD inert to slightly harmful\"\n        },\n        \"full_caclr\": {\n          \"delta_vs_zs\": -0.01,\n          \"note\": \"combined losses compound harm\"\n        }\n      },\n      \"linear_proj_vs_caclr_delta\": 0.048,\n      \"fewshot100_vs_caclr_delta\": 0.061,\n      \"implementation_spec\": {\n        \"mmd_kernel\": \"Gaussian RBF, bandwidth=median heuristic\",\n        \"optimizer\": \"Adam, lr=1e-3, cosine schedule\",\n        \"epochs\": 50,\n        \"early_stopping\": \"patience=10 on held-out BCE loss\",\n        \"initialization\": \"from standard LR solution\",\n        \"batch_size\": 256,\n        \"mmd_items\": \"same items as BCE (probe_train split)\",\n        \"parallel_set_size_range\": [\n          612,\n          2847\n        ]\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3a: CaCLR β Sweep (Qwen3-235B, fixed layer 50% depth, 20 langs mean)\",\n        \"columns\": [\n          \"beta\",\n          \"mean_auroc\",\n          \"delta_vs_zs\",\n          \"pct_langs_improved\",\n          \"pct_langs_harmed\"\n        ],\n        \"rows\": [\n          [\n            0.001,\n            0.57,\n            -0.003,\n            \"30%\",\n            \"45%\"\n          ],\n          [\n            0.01,\n            0.567,\n            -0.006,\n            \"25%\",\n            \"55%\"\n          ],\n          [\n            0.1,\n            0.562,\n            -0.011,\n            \"15%\",\n            \"65%\"\n          ],\n          [\n            1.0,\n            0.554,\n            -0.019,\n            \"10%\",\n            \"80%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 3b: 5-Way Transfer Condition Comparison (both models × 20 langs, EN-optimal layer)\",\n        \"columns\": [\n          \"condition\",\n          \"mean_auroc\",\n          \"mean_ece\",\n          \"delta_auroc_vs_zs\",\n          \"win_rate_vs_zs\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0.568,\n            0.285,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"mean-shift\",\n            0.568,\n            0.291,\n            0.0,\n            \"0%\"\n          ],\n          [\n            \"CaCLR_best\",\n            0.558,\n            0.278,\n            -0.01,\n            \"18%\"\n          ],\n          [\n            \"linear_proj_200\",\n            0.606,\n            0.248,\n            0.038,\n            \"72%\"\n          ],\n          [\n            \"fewshot_25\",\n            0.59,\n            0.262,\n            0.022,\n            \"55%\"\n          ],\n          [\n            \"fewshot_100\",\n            0.619,\n            0.235,\n            0.051,\n            \"78%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 3c: CaCLR Component Ablation\",\n        \"columns\": [\n          \"configuration\",\n          \"mean_auroc\",\n          \"delta_vs_zs\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            \"BCE only (re-init)\",\n            0.567,\n            -0.001,\n            \"≈ ZS baseline\"\n          ],\n          [\n            \"BCE + SB-ECE (α=0.1)\",\n            0.561,\n            -0.007,\n            \"ECE gains tiny, AUROC drops\"\n          ],\n          [\n            \"BCE + MMD (β=0.01)\",\n            0.563,\n            -0.005,\n            \"MMD inert/harmful\"\n          ],\n          [\n            \"Full CaCLR (α=0.1, β=0.01)\",\n            0.558,\n            -0.01,\n            \"compound degradation\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR 的 negative result 是 worst tier 的核心。β sweep 证实 consistency loss 在所有 3 OOM 均为 inert 或 harmful—— 这不是超参选择问题而是方法论层面的失败。1-D MMD 的结构性限制（probe logit 空间太低维）加上 conditional distribution mismatch（Zhao et al. 2019）导致 distributional matching 路径被彻底关闭。 与此同时，CKA subspace 解释也不成立（plan_011 将确认），所以\\\"MMD 失败是因为它只 match marginal 而不 match subspace direction\\\"这个 elegant 的解释也变成了 post-hoc rationalization—— 实际上 subspace 本身就不 robust。这是 worst tier 最痛苦的部分：不仅方法失败，解释也失败。 但作为 negative result，reproducibility 标准高：完整的 implementation spec、β/α sweep、 component ablation 使社区可以独立验证，避免重复尝试 distributional matching 路径。\\n\\n\\nCaCLR 失败的根本原因：MMD 在 probe logits 空间操作，而 logits 是 1-D（线性 probe 的单一输出）。 1-D MMD 只能 match 两个标量分布的 marginal，无法对齐 correctness direction 的方向性结构。 即使 marginal logit 分布被 match，EN 和 target 的 conditional distributions P(logit|correct) vs P(logit|incorrect) 可能仍然不同——Zhao et al. (2019) 的理论预测得到验证。β 越大，MMD 约束越强， logits 被拉向无区分性的 marginal match，discrimination 下降。α 高值时 SB-ECE 正则化 进一步牺牲 AUROC 以换取 calibration 改善，但改善微小且不稳定。Component ablation 证实 每个额外 loss component 都是净负面的——base BCE（从 LR solution 初始化再微调）已经接近 ZS 性能， 额外优化无正贡献。Linear projection 和 few-shot 都显著优于 CaCLR，因为它们直接利用 target-language 信息（parallel pairs 或 labels）而非试图间接 match distributions。 CKA subspace 解释（correctness direction 是 low-dimensional language-agnostic subspace） 不成立——如果该 subspace 真的存在且 robust，MMD 应该至少能做到无害，但实际上有害， 说明 correctness signal 的跨语言结构比预期更 language-specific。\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Decomposition Ablation\",\n    \"description\": \"IRT difficulty probes → project out → retrain correctness probes, 10 langs × 8 layers × 2 models\",\n    \"results\": {\n      \"decomp_capability_delta_auroc_mean\": -0.003,\n      \"decomp_capability_delta_auroc_range\": [\n        -0.015,\n        0.008\n      ],\n      \"random_direction_control_delta_mean\": -0.005,\n      \"random_direction_control_delta_range\": [\n        -0.018,\n        0.006\n      ],\n      \"difficulty_probe_r2\": 0.31,\n      \"decomp_vs_random_paired_test_p\": 0.42,\n      \"per_tier_delta\": {\n        \"HIGH\": {\n          \"mean_delta\": -0.002,\n          \"significant_count\": \"0/4\"\n        },\n        \"MID\": {\n          \"mean_delta\": -0.004,\n          \"significant_count\": \"0/3\"\n        },\n        \"LOW\": {\n          \"mean_delta\": -0.003,\n          \"significant_count\": \"0/3\"\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Difficulty Decomposition Ablation (mean across 2 models)\",\n        \"columns\": [\n          \"lang\",\n          \"resource_tier\",\n          \"original_zs_auroc\",\n          \"after_projection_auroc\",\n          \"delta\",\n          \"random_control_delta\",\n          \"decomp_vs_random_p\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"HIGH\",\n            0.658,\n            0.655,\n            -0.003,\n            -0.006,\n            0.61\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.67,\n            0.669,\n            -0.001,\n            -0.004,\n            0.52\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.652,\n            0.649,\n            -0.003,\n            -0.007,\n            0.38\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.643,\n            0.642,\n            -0.001,\n            -0.003,\n            0.71\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.552,\n            0.547,\n            -0.005,\n            -0.008,\n            0.55\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.613,\n            0.61,\n            -0.003,\n            -0.005,\n            0.64\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.578,\n            0.572,\n            -0.006,\n            -0.004,\n            0.48\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.532,\n            0.53,\n            -0.002,\n            -0.006,\n            0.33\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.504,\n            0.501,\n            -0.003,\n            -0.005,\n            0.58\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.512,\n            0.504,\n            -0.008,\n            -0.007,\n            0.82\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Decomposition 的 null result 与 random-direction control 不可区分（p=0.42），表明投影效应来自 dimensionality reduction 而非 difficulty-specific 信号去除。这从根本上否定了 Claim 2 的因果叙述—— transfer degradation 不能分解为 difficulty-shared 和 capability-specific 两个可操作的 component。 在 worst tier framing 中，这成为 negative result 的一部分：decomposition 是另一条被关闭的路径。\\n\\n\\nDifficulty decomposition 在 worst tier 无实质效果。两个原因：(1) difficulty 和 capability 信号在 representation 空间中高度纠缠——IRT difficulty direction 不是一个干净的、可投影去除的独立子空间， 而是与 correctness signal 共享大量方差。投影去除 difficulty 后 correctness signal 也被部分损坏， 导致 retrained probe 的 transfer 性能与原始相当甚至略差。(2) Random-direction control 产生 同量级的效果（mean delta -0.005 vs -0.003，paired test p=0.42），这意味着观察到的微小变化 主要来自 dimensionality reduction 效应而非 difficulty-specific 投影。Difficulty probe 本身 R²=0.31（低于理想值），表明 IRT difficulty 在 LLM representation 中的编码不够线性/集中， 使得 linear projection 无法有效捕获它。整个 decomposition framing 在经验层面被否定： transfer 的降解不能归因于 capability-specific component，或者说两个 component 不可分。\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Orthogonality Analysis\",\n    \"description\": \"Correctness-confidence cosine similarity, 20 langs × 2 architectures, resource-tier 和 language family 分析\",\n    \"results\": {\n      \"mean_cosine_high_resource\": 0.038,\n      \"mean_cosine_mid_resource\": 0.065,\n      \"mean_cosine_low_resource\": 0.112,\n      \"std_cosine_low_resource\": 0.082,\n      \"cosine_range_all\": [\n        0.008,\n        0.198\n      ],\n      \"architecture_agreement_rate\": 0.65,\n      \"outlier_langs\": [\n        \"am\",\n        \"yo\",\n        \"my\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Cross-Lingual Orthogonality (Cosine Similarity)\",\n        \"columns\": [\n          \"lang\",\n          \"tier\",\n          \"qwen3_cosine\",\n          \"llama4_cosine\",\n          \"agreement\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"HIGH\",\n            0.031,\n            0.028,\n            \"✓\",\n            \"\"\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.025,\n            0.033,\n            \"✓\",\n            \"\"\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.029,\n            0.041,\n            \"✓\",\n            \"\"\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.035,\n            0.038,\n            \"✓\",\n            \"\"\n          ],\n          [\n            \"ja\",\n            \"HIGH\",\n            0.048,\n            0.052,\n            \"✓\",\n            \"\"\n          ],\n          [\n            \"pt\",\n            \"HIGH\",\n            0.027,\n            0.035,\n            \"✓\",\n            \"\"\n          ],\n          [\n            \"it\",\n            \"HIGH\",\n            0.033,\n            0.039,\n            \"✓\",\n            \"\"\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            0.042,\n            0.058,\n            \"✓\",\n            \"\"\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.055,\n            0.072,\n            \"✓\",\n            \"\"\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.038,\n            0.045,\n            \"✓\",\n            \"\"\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.061,\n            0.048,\n            \"✗\",\n            \"direction reversed\"\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.075,\n            0.068,\n            \"✓\",\n            \"\"\n          ],\n          [\n            \"vi\",\n            \"MID\",\n            0.052,\n            0.082,\n            \"✗\",\n            \"magnitude mismatch\"\n          ],\n          [\n            \"th\",\n            \"MID\",\n            0.088,\n            0.065,\n            \"✗\",\n            \"magnitude mismatch\"\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.095,\n            0.108,\n            \"✓\",\n            \"elevated\"\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.082,\n            0.118,\n            \"✗\",\n            \"\"\n          ],\n          [\n            \"am\",\n            \"LOW\",\n            0.198,\n            0.152,\n            \"✓\",\n            \"near non-orthogonal\"\n          ],\n          [\n            \"yo\",\n            \"LOW\",\n            0.165,\n            0.128,\n            \"✗\",\n            \"\"\n          ],\n          [\n            \"te\",\n            \"LOW\",\n            0.105,\n            0.092,\n            \"✓\",\n            \"\"\n          ],\n          [\n            \"my\",\n            \"LOW\",\n            0.142,\n            0.118,\n            \"✓\",\n            \"elevated\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Orthogonality 作为 subsection 贡献了一个 nuanced finding：该性质是 resource-tier dependent， 低资源语言中不可靠。但在 worst tier 下这个 finding 被 plan_013 的高 artifact rate 进一步削弱—— 低资源语言的高 cosine 可能反映 probe 本身的 capacity artifact 而非真正的非正交 representation 结构。 Section 简化为：\\\"orthogonality generally holds but becomes unreliable for low-resource languages， where probe validity itself is questionable (Section X).\\\" 贡献有限。\\n\\n\\nOrthogonality 在高资源语言基本成立（cosine < 0.05），复现 Miao & Ungar (2026) 的英文发现。 但低资源语言的 cosine similarity 显著升高且方差极大（mean=0.112, std=0.082），部分语言 （am=0.198, yo=0.165, my=0.142）接近打破 orthogonality 假设。这可能是因为低资源语言 的 correctness 和 confidence directions 都更 noisy（probe 本身 selectivity 低——见 plan_013）， 而非真正的非正交结构。Architecture 一致性仅 65%：两个架构在 7/20 语言上对 orthogonality 程度 给出矛盾信号，削弱了\\\"orthogonality is a universal property\\\"的叙述。 作为 subsection（已从 standalone claim 降级），这些结果增加了复杂性但没有清晰的 takeaway。\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison\",\n    \"description\": \"Logistic regression vs 2-layer MLP, EN accuracy + cross-lingual transfer + calibration, 2 models × 20 langs\",\n    \"results\": {\n      \"en_auroc_lr_mean\": 0.726,\n      \"en_auroc_mlp_mean\": 0.741,\n      \"mlp_en_advantage\": 0.015,\n      \"zs_transfer_lr_mean_degradation\": 0.152,\n      \"zs_transfer_mlp_mean_degradation\": 0.191,\n      \"mlp_transfer_disadvantage\": -0.039,\n      \"lr_better_for_transfer_pct\": 0.7,\n      \"ece_lr_mean\": 0.242,\n      \"ece_mlp_mean\": 0.258,\n      \"selectivity_lr_mean\": 0.218,\n      \"selectivity_mlp_mean\": 0.235\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Probe Complexity Comparison Summary\",\n        \"columns\": [\n          \"metric\",\n          \"logistic_regression\",\n          \"mlp_2layer\",\n          \"delta\",\n          \"p_value\"\n        ],\n        \"rows\": [\n          [\n            \"EN AUROC (mean)\",\n            0.726,\n            0.741,\n            0.015,\n            0.008\n          ],\n          [\n            \"ZS degradation (mean)\",\n            \"15.2%\",\n            \"19.1%\",\n            \"+3.9pp\",\n            0.023\n          ],\n          [\n            \"ZS AUROC (mean)\",\n            0.616,\n            0.6,\n            -0.016,\n            0.041\n          ],\n          [\n            \"EN ECE (mean)\",\n            0.242,\n            0.258,\n            0.016,\n            0.065\n          ],\n          [\n            \"Selectivity (mean)\",\n            0.218,\n            0.235,\n            0.017,\n            0.112\n          ],\n          [\n            \"LR better for transfer\",\n            \"70%\",\n            \"30%\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LR vs MLP 比较方向符合预期但 effect size 中等。在 worst tier 的 high-artifact 环境下， probe complexity 不是主要问题——语言-层级 capacity artifacts 才是。 结论：保持 LR 作为默认，MLP 结果放 appendix。\\n\\n\\nMLP 在 EN 上因更高 capacity 而有 +1.5pp AUROC 优势，但跨语言 transfer 时 degradation 更大 （-19.1% vs -15.2%），符合\\\"linear probes transfer better\\\"假设。然而在 worst tier 下， 这个差异虽然方向正确但 effect size 不大（Cohen's d ≈ 0.3），且 70% 而非 90%+ 的语言 支持 LR > MLP for transfer，因为部分高资源语言中 MLP 的额外 capacity 弥补了 transfer 损失。 此外 MLP 的 selectivity 仅比 LR 高 0.017，表明额外 capacity 带来的 artifact 风险有限—— 这与 plan_013 的高 artifact rate 形成有趣对比（artifacts 主要来自语言本身而非 probe 复杂度）。\\n\"\n  },\n  {\n    \"name\": \"Additional Benchmark Evaluation (Belebele + MMLU-ProX)\",\n    \"description\": \"Best probes + CaCLR on Belebele 和 MMLU-ProX, 20 languages each, generalization test\",\n    \"results\": {\n      \"belebele_zs_pass_rate\": 0.5,\n      \"belebele_mean_zs_auroc\": 0.548,\n      \"belebele_vs_globalmmlu_spearman_rho\": 0.72,\n      \"belebele_vs_globalmmlu_mean_auroc_delta\": -0.024,\n      \"mmlupx_zs_pass_rate\": 0.55,\n      \"mmlupx_mean_zs_auroc\": 0.562,\n      \"mmlupx_vs_globalmmlu_spearman_rho\": 0.78,\n      \"caclr_belebele_delta_vs_zs\": -0.013,\n      \"caclr_mmlupx_delta_vs_zs\": -0.008,\n      \"linear_proj_belebele_delta\": 0.031,\n      \"linear_proj_mmlupx_delta\": 0.035\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Cross-Benchmark Generalization\",\n        \"columns\": [\n          \"benchmark\",\n          \"zs_pass_rate\",\n          \"mean_zs_auroc\",\n          \"caclr_delta\",\n          \"linproj_delta\",\n          \"correlation_with_globalmmlu\"\n        ],\n        \"rows\": [\n          [\n            \"GlobalMMLU\",\n            0.575,\n            0.572,\n            -0.01,\n            0.038,\n            \"—\"\n          ],\n          [\n            \"Belebele\",\n            0.5,\n            0.548,\n            -0.013,\n            0.031,\n            0.72\n          ],\n          [\n            \"MMLU-ProX\",\n            0.55,\n            0.562,\n            -0.008,\n            0.035,\n            0.78\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-benchmark generalization moderate but not strong。Belebele 的低 performance 暗示 correctness probing 可能对任务格式敏感。在 worst-tier paper 中这增加了一层 caveat： findings 可能 MCQA-specific，generalization to other formats uncertain。\\n\\n\\nBelebele 的 reading comprehension 格式与 MCQA correctness probing 的 mismatch 导致更低的 pass rate。 MMLU-ProX 与 GlobalMMLU 更接近（同为知识 MCQA）所以 correlation 更高。CaCLR 在两个 benchmark 上 同样失败甚至更差——distribution mismatch 在 out-of-distribution 数据上放大。 Linear projection 仍有正增益但幅度小于 GlobalMMLU——cross-benchmark generalization 有衰减。 整体 pattern：在 worst tier 下 generalization 弱化了已经微弱的 positive findings， reinforcing negative result narrative。Belebele 的低 pass rate 尤其令人担忧—— correctness probe 的概念可能不 generalize beyond MCQA knowledge questions。\\n\"\n  },\n  {\n    \"name\": \"Quantization Validation Ablation\",\n    \"description\": \"W4A16 vs FP16 (Llama), INT4 vs FP16 (Qwen), 5 representative layers, 5% data subset\",\n    \"results\": {\n      \"llama_w4a16_vs_fp16_max_delta_auroc\": 0.018,\n      \"llama_w4a16_vs_fp16_mean_delta_auroc\": 0.009,\n      \"llama_w4a16_vs_fp16_spearman_rank_preservation\": 0.91,\n      \"qwen_int4_vs_fp16_max_delta_auroc\": 0.022,\n      \"qwen_int4_vs_fp16_mean_delta_auroc\": 0.012,\n      \"qwen_int4_vs_fp16_spearman_rank_preservation\": 0.88,\n      \"problematic_layers_count\": 2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Quantization Validation\",\n        \"columns\": [\n          \"model\",\n          \"quant\",\n          \"layer_pct\",\n          \"fp16_auroc\",\n          \"quant_auroc\",\n          \"delta\",\n          \"rank_preserved\"\n        ],\n        \"rows\": [\n          [\n            \"Llama4\",\n            \"W4A16\",\n            \"20%\",\n            0.648,\n            0.645,\n            -0.003,\n            \"✓\"\n          ],\n          [\n            \"Llama4\",\n            \"W4A16\",\n            \"40%\",\n            0.672,\n            0.665,\n            -0.007,\n            \"✓\"\n          ],\n          [\n            \"Llama4\",\n            \"W4A16\",\n            \"60%\",\n            0.695,\n            0.683,\n            -0.012,\n            \"✓\"\n          ],\n          [\n            \"Llama4\",\n            \"W4A16\",\n            \"80%\",\n            0.708,\n            0.692,\n            -0.016,\n            \"✗ (2 langs swap)\"\n          ],\n          [\n            \"Llama4\",\n            \"W4A16\",\n            \"95%\",\n            0.712,\n            0.694,\n            -0.018,\n            \"✗ (3 langs swap)\"\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"20%\",\n            0.625,\n            0.62,\n            -0.005,\n            \"✓\"\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"40%\",\n            0.668,\n            0.658,\n            -0.01,\n            \"✓\"\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"60%\",\n            0.702,\n            0.688,\n            -0.014,\n            \"✗ (1 lang swap)\"\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"80%\",\n            0.728,\n            0.71,\n            -0.018,\n            \"✗ (3 langs swap)\"\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"95%\",\n            0.738,\n            0.716,\n            -0.022,\n            \"✗ (4 langs swap)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Quantization 在深层引入 1-2pp 的系统性偏差。在 worst tier 下这不改变主要结论（negative results 不依赖于精确数值），但增加了 limitations section 的内容。Deep layer probe results（包括 EN-optimal layer 的 AUROC）可能被 overestimate 了 ~1pp by quantization loss。\\n\\n\\nWorst tier 下量化 artifacts 不是灾难性的但 non-negligible。W4A16 mean delta 0.9pp 和 INT4 mean delta 1.2pp 在多数层可接受，但在 2/5 测试层出现 >1.5pp 偏差—— 特别是在最深层（correctness signal 最集中的地方），quantization 对高频/低方差的 correctness direction 影响更大。Rank preservation 88-91% 意味着 per-language ranking 大体保持但不完美。在 worst tier 下这创造了一个 uncomfortable caveat： 所有关于深层 probe 的结论都 potentially 受量化影响，但无法做完整的 FP16 实验来确认。 需要在 limitations 中明确讨论。INT4 比 W4A16 worse 因为 4-bit weight-only 比 4-bit weight + 16-bit activation 更 aggressive。\\n\"\n  },\n  {\n    \"name\": \"CKA Cross-Lingual Representation Similarity Analysis\",\n    \"description\": \"CKA (linear kernel) EN vs target, all probed layers, 20 langs × 2 models. Simpson's Paradox 验证。\",\n    \"results\": {\n      \"simpson_partial_rho_qwen\": 0.11,\n      \"simpson_partial_p_qwen\": 0.31,\n      \"simpson_partial_rho_llama\": 0.08,\n      \"simpson_partial_p_llama\": 0.42,\n      \"raw_correlation_rho_qwen\": -0.28,\n      \"raw_correlation_rho_llama\": -0.35,\n      \"raw_correlation_p_qwen\": 0.001,\n      \"raw_correlation_p_llama\": \"<0.001\",\n      \"same_layer_cross_lang_rho_median\": 0.15,\n      \"same_layer_cross_lang_significant_layers\": \"2/24 (Qwen), 0/12 (Llama)\",\n      \"cka_threshold_identifiable\": false,\n      \"subspace_angle_consistency\": \"low — angles vary 15-65° across languages at same layer\",\n      \"pilot_replication_5lang\": \"partial — Llama rho drops from +0.41 to +0.08 with 20 langs\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9a: Simpson's Paradox Full-Scale Validation\",\n        \"columns\": [\n          \"model\",\n          \"raw_rho\",\n          \"raw_p\",\n          \"partial_rho_depth\",\n          \"partial_p\",\n          \"pilot_partial_rho\",\n          \"pilot_partial_p\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B\",\n            -0.28,\n            0.001,\n            0.11,\n            0.31,\n            \"+0.18 (n.s.)\",\n            0.274,\n            \"n.s. → no Simpson's Paradox\"\n          ],\n          [\n            \"Llama4-Scout\",\n            -0.35,\n            \"<0.001\",\n            0.08,\n            0.42,\n            \"+0.41 (sig.)\",\n            0.006,\n            \"pilot artifact confirmed\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9b: Same-Layer Cross-Language CKA-Transfer Correlation (top 5 layers)\",\n        \"columns\": [\n          \"model\",\n          \"layer\",\n          \"layer_pct\",\n          \"cka_transfer_rho\",\n          \"p_value\",\n          \"n_langs\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3\",\n            36,\n            \"38%\",\n            0.22,\n            0.35,\n            20\n          ],\n          [\n            \"Qwen3\",\n            48,\n            \"51%\",\n            0.31,\n            0.18,\n            20\n          ],\n          [\n            \"Qwen3\",\n            56,\n            \"60%\",\n            0.18,\n            0.45,\n            20\n          ],\n          [\n            \"Qwen3\",\n            64,\n            \"68%\",\n            0.42,\n            0.065,\n            20\n          ],\n          [\n            \"Qwen3\",\n            72,\n            \"77%\",\n            0.38,\n            0.098,\n            20\n          ],\n          [\n            \"Llama4\",\n            16,\n            \"33%\",\n            0.12,\n            0.61,\n            20\n          ],\n          [\n            \"Llama4\",\n            24,\n            \"50%\",\n            0.08,\n            0.74,\n            20\n          ],\n          [\n            \"Llama4\",\n            32,\n            \"67%\",\n            0.25,\n            0.29,\n            20\n          ],\n          [\n            \"Llama4\",\n            40,\n            \"83%\",\n            0.15,\n            0.53,\n            20\n          ],\n          [\n            \"Llama4\",\n            44,\n            \"92%\",\n            0.05,\n            0.83,\n            20\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9c: Subspace Angle Analysis (Correctness Direction, EN vs Target)\",\n        \"columns\": [\n          \"lang\",\n          \"tier\",\n          \"qwen3_angle_deg_L56\",\n          \"llama4_angle_deg_L32\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"HIGH\",\n            18,\n            22,\n            \"relatively aligned\"\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            15,\n            19,\n            \"relatively aligned\"\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            20,\n            25,\n            \"\"\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            22,\n            28,\n            \"\"\n          ],\n          [\n            \"ja\",\n            \"HIGH\",\n            35,\n            41,\n            \"large angle despite HIGH resource\"\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            32,\n            38,\n            \"\"\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            38,\n            45,\n            \"\"\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            28,\n            35,\n            \"\"\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            42,\n            48,\n            \"\"\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            52,\n            58,\n            \"near orthogonal\"\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            48,\n            55,\n            \"\"\n          ],\n          [\n            \"am\",\n            \"LOW\",\n            62,\n            65,\n            \"correctness direction nearly unrelated\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CKA analysis 的全面失败是 worst tier 的 defining feature。Pilot 的 Simpson's Paradox 从 Llama rho=+0.41 (p=0.006) 崩溃到 rho=+0.08 (p=0.42)——这是教科书式的 small-sample inflation。 5 语言 pilot 恰好 overrepresented CKA-transfer 关系最强的语言（zh, ar），排除了关系最弱的语言。 Subspace angle analysis 进一步否定了\\\"correctness direction is a robust low-dimensional language-agnostic subspace\\\"的前提假设：即使 HIGH resource 语言的 angle 也有 15-35° 的 spread， LOW resource 达到 48-65°（近乎不相关）。这意味着 Miao & Ungar (2026) 的 EN-only correctness direction 在跨语言场景下不是 language-agnostic 的——这本身是一个重要的 negative finding，值得在 paper 中强调。 CKA 框架从 geometric analysis 降级为 descriptive visualization（仅展示 CKA 随 depth 的下降趋势）， 不再承载解释性角色。\\n\\n\\n这是 worst tier 最关键的 falsification。5 语言 pilot 中的 Simpson's Paradox (Llama partial rho=+0.41, p=0.006) 被确认为 small-sample artifact。当 20 语言数据进入分析后：(1) 新增的 15 种语言中多数与 CKA-transfer 关系不一致，部分语言（特别是 MID/LOW tier）的 CKA 模式与 pilot 的 5 种语言截然不同—— pilot 恰好选中了 CKA 与 transfer 最相关的语言子集（zh, ar 高 CKA + 低 degradation 拉高了相关性）。 (2) Partial correlation controlling for depth 大幅缩水：Qwen rho 从 pilot 的 +0.18 降至 +0.11 (仍 n.s.)， Llama rho 从 +0.41 骤降至 +0.08。原因是新增语言打破了\\\"within-layer CKA predicts transfer\\\"的模式—— 同一层内不同语言的 CKA 值差异巨大但 transfer 性能差异不 track CKA。 (3) Same-layer cross-language analysis (n=20 per layer) 是最强检验：median rho=0.15， 仅 2/24 Qwen layers 和 0/12 Llama layers 达到显著——CKA 在 within-layer 水平几乎无解释力。 (4) Subspace angle analysis 显示 correctness direction 的跨语言一致性远低于预期—— angles 在 15-65° 范围波动，不支持\\\"robust low-dimensional language-agnostic subspace\\\"的说法。 结论：CKA 不提供超越 depth 的解释力，必须从\\\"geometric analysis\\\"降级为\\\"suggestive correlation\\\"。\\n\"\n  },\n  {\n    \"name\": \"Linear Projection Sensitivity Analysis\",\n    \"description\": \"Procrustes alignment with 10/20/50/100/200 parallel pairs, 2 models × 5 layers × 20 langs\",\n    \"results\": {\n      \"pairs_to_95pct_mean\": 142,\n      \"pairs_to_95pct_range\": [\n        85,\n        198\n      ],\n      \"pairs_to_95pct_high_tier\": 68,\n      \"pairs_to_95pct_mid_tier\": 125,\n      \"pairs_to_95pct_low_tier\": 182,\n      \"saturation_curve_r2\": 0.82,\n      \"pair_10_mean_auroc\": 0.548,\n      \"pair_20_mean_auroc\": 0.568,\n      \"pair_50_mean_auroc\": 0.588,\n      \"pair_100_mean_auroc\": 0.601,\n      \"pair_200_mean_auroc\": 0.61,\n      \"procrustes_reversal_threshold\": \"inconsistent — varies by language\",\n      \"helps_when_zs_below\": \"ranges from 0.48 to 0.58 across languages\",\n      \"hurts_when_zs_above\": \"ranges from 0.55 to 0.68 across languages\",\n      \"reversal_overlap_zone\": [\n        0.48,\n        0.68\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10a: Linear Projection Sample Efficiency (mean across 2 models × 20 langs)\",\n        \"columns\": [\n          \"n_pairs\",\n          \"mean_auroc\",\n          \"pct_of_200pair\",\n          \"std_across_langs\",\n          \"significant_improvement_pct\"\n        ],\n        \"rows\": [\n          [\n            10,\n            0.548,\n            \"68%\",\n            0.065,\n            \"25%\"\n          ],\n          [\n            20,\n            0.568,\n            \"79%\",\n            0.058,\n            \"40%\"\n          ],\n          [\n            50,\n            0.588,\n            \"89%\",\n            0.052,\n            \"55%\"\n          ],\n          [\n            100,\n            0.601,\n            \"95%\",\n            0.048,\n            \"65%\"\n          ],\n          [\n            200,\n            0.61,\n            \"100%\",\n            0.045,\n            \"72%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 10b: Pairs to 95% Performance by Resource Tier\",\n        \"columns\": [\n          \"tier\",\n          \"mean_pairs_95pct\",\n          \"min\",\n          \"max\",\n          \"std\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH\",\n            68,\n            42,\n            98,\n            22\n          ],\n          [\n            \"MID\",\n            125,\n            78,\n            165,\n            35\n          ],\n          [\n            \"LOW\",\n            182,\n            145,\n            198,\n            28\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 10c: Procrustes Effect Reversal — Inconsistent Thresholds\",\n        \"columns\": [\n          \"lang\",\n          \"tier\",\n          \"zs_auroc\",\n          \"linproj_200_auroc\",\n          \"delta\",\n          \"effect\"\n        ],\n        \"rows\": [\n          [\n            \"am\",\n            \"LOW\",\n            0.475,\n            0.498,\n            0.023,\n            \"helps\"\n          ],\n          [\n            \"yo\",\n            \"LOW\",\n            0.463,\n            0.49,\n            0.027,\n            \"helps\"\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.504,\n            0.518,\n            0.014,\n            \"helps\"\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.512,\n            0.528,\n            0.016,\n            \"helps\"\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.532,\n            0.548,\n            0.016,\n            \"helps\"\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.552,\n            0.561,\n            0.009,\n            \"helps (marginal)\"\n          ],\n          [\n            \"vi\",\n            \"MID\",\n            0.558,\n            0.558,\n            0.0,\n            \"neutral\"\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.578,\n            0.575,\n            -0.003,\n            \"neutral/hurts\"\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            0.603,\n            0.598,\n            -0.005,\n            \"hurts\"\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.624,\n            0.612,\n            -0.012,\n            \"hurts\"\n          ],\n          [\n            \"zh\",\n            \"HIGH\",\n            0.658,\n            0.641,\n            -0.017,\n            \"hurts\"\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.67,\n            0.65,\n            -0.02,\n            \"hurts\"\n          ],\n          [\n            \"ja\",\n            \"HIGH\",\n            0.582,\n            0.59,\n            0.008,\n            \"helps (despite HIGH tier)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear projection 仍是唯一可行方案但实用性大打折扣：(1) 需 100+ pairs 而非 50， 对低资源语言来说 parallel data 本身就是稀缺资源；(2) 效果反转阈值 inconsistent， practitioner 无法事先知道某语言是否会被帮助或伤害。Paper 中只能给出条件性 recommendation： \\\"当 ZS AUROC < 0.50 时大概率有益，> 0.65 时大概率有害，0.50-0.65 区间需要 held-out validation\\\" ——这比预期的 clean threshold (0.50/0.60) 弱得多。\\n\\n\\nWorst tier 下 linear projection 需要 100-200 pairs（非 50）达到 95% 性能： (1) Subspace angle 在 worst tier 更大更不一致（plan_011），Procrustes 需要更多数据点来 稳定估计 rotation matrix——50 pairs 在高维空间中 rank-deficient，低资源语言的 parallel pairs 质量更差（翻译质量低→activation 噪声→需要更多 pairs 来 average out noise）。 (2) Resource-tier 分层仍然存在（HIGH 68 pairs vs LOW 182 pairs）但 tier 内方差大—— 同一 tier 内语言间差异可达 2-3×（如 zh 需 45 pairs 但 ja 需 95 pairs，都是 HIGH）。 (3) Procrustes 效果反转的阈值高度 language-specific：帮助的 ZS AUROC 范围和伤害的范围 有 [0.48, 0.68] 的 overlap zone，意味着对同一 ZS AUROC 值，不同语言可能被帮助或伤害。 无法给出单一可操作的阈值——这使得\\\"practitioners should use linear projection when ZS < X\\\" 的建议变得不可靠。\\n\"\n  },\n  {\n    \"name\": \"Probing Control Tasks (Cross-Lingual Extension)\",\n    \"description\": \"Hewitt & Liang control tasks for 20 languages × all probed layers × 2 models, selectivity analysis\",\n    \"results\": {\n      \"control_artifact_rate_low_resource\": 0.42,\n      \"control_artifact_rate_mid_resource\": 0.37,\n      \"control_artifact_rate_high_resource\": 0.18,\n      \"control_artifact_rate_overall\": 0.31,\n      \"selectivity_below_0.05_pct_low\": \"42%\",\n      \"selectivity_below_0.05_pct_mid\": \"37%\",\n      \"selectivity_below_0.05_pct_high\": \"18%\",\n      \"mean_selectivity_en\": 0.245,\n      \"mean_selectivity_high\": 0.198,\n      \"mean_selectivity_mid\": 0.142,\n      \"mean_selectivity_low\": 0.085,\n      \"selectivity_vs_zs_auroc_rho\": 0.68,\n      \"layers_most_affected\": \"shallow layers (0-30% depth)\",\n      \"worst_lang_layer_combos\": [\n        \"am-L0\",\n        \"yo-L4\",\n        \"my-L0\",\n        \"am-L4\",\n        \"yo-L0\",\n        \"te-L8\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11a: Control Task Artifact Rate by Resource Tier and Model\",\n        \"columns\": [\n          \"tier\",\n          \"n_langs\",\n          \"qwen3_artifact_rate\",\n          \"llama4_artifact_rate\",\n          \"combined\",\n          \"selectivity_mean\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH\",\n            7,\n            \"16%\",\n            \"20%\",\n            \"18%\",\n            0.198\n          ],\n          [\n            \"MID\",\n            7,\n            \"35%\",\n            \"39%\",\n            \"37%\",\n            0.142\n          ],\n          [\n            \"LOW\",\n            6,\n            \"40%\",\n            \"44%\",\n            \"42%\",\n            0.085\n          ],\n          [\n            \"ALL\",\n            20,\n            \"29%\",\n            \"33%\",\n            \"31%\",\n            0.145\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 11b: Per-Language Selectivity at EN-Optimal Layer\",\n        \"columns\": [\n          \"lang\",\n          \"tier\",\n          \"real_auroc\",\n          \"permuted_auroc\",\n          \"selectivity\",\n          \"artifact_flag\"\n        ],\n        \"rows\": [\n          [\n            \"en\",\n            \"—\",\n            0.738,\n            0.49,\n            0.248,\n            \"\"\n          ],\n          [\n            \"zh\",\n            \"HIGH\",\n            0.672,\n            0.498,\n            0.174,\n            \"\"\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.681,\n            0.495,\n            0.186,\n            \"\"\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.663,\n            0.492,\n            0.171,\n            \"\"\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.654,\n            0.488,\n            0.166,\n            \"\"\n          ],\n          [\n            \"ja\",\n            \"HIGH\",\n            0.582,\n            0.502,\n            0.08,\n            \"\"\n          ],\n          [\n            \"pt\",\n            \"HIGH\",\n            0.668,\n            0.491,\n            0.177,\n            \"\"\n          ],\n          [\n            \"it\",\n            \"HIGH\",\n            0.651,\n            0.494,\n            0.157,\n            \"\"\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            0.603,\n            0.498,\n            0.105,\n            \"\"\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.561,\n            0.505,\n            0.056,\n            \"⚠\"\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.624,\n            0.495,\n            0.129,\n            \"\"\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.585,\n            0.501,\n            0.084,\n            \"\"\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.541,\n            0.508,\n            0.033,\n            \"⚠\"\n          ],\n          [\n            \"vi\",\n            \"MID\",\n            0.558,\n            0.512,\n            0.046,\n            \"⚠\"\n          ],\n          [\n            \"th\",\n            \"MID\",\n            0.523,\n            0.498,\n            0.025,\n            \"⚠\"\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.512,\n            0.505,\n            0.007,\n            \"⚠⚠\"\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.519,\n            0.502,\n            0.017,\n            \"⚠⚠\"\n          ],\n          [\n            \"am\",\n            \"LOW\",\n            0.482,\n            0.478,\n            0.004,\n            \"⚠⚠\"\n          ],\n          [\n            \"yo\",\n            \"LOW\",\n            0.471,\n            0.465,\n            0.006,\n            \"⚠⚠\"\n          ],\n          [\n            \"te\",\n            \"LOW\",\n            0.498,\n            0.488,\n            0.01,\n            \"⚠⚠\"\n          ],\n          [\n            \"my\",\n            \"LOW\",\n            0.463,\n            0.458,\n            0.005,\n            \"⚠⚠\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 11c: Layers with Artifact Rate > 40%\",\n        \"columns\": [\n          \"model\",\n          \"layer_range\",\n          \"high_artifact_pct\",\n          \"mid_artifact_pct\",\n          \"low_artifact_pct\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3\",\n            \"L0-L20 (0-21%)\",\n            \"8%\",\n            \"48%\",\n            \"65%\"\n          ],\n          [\n            \"Qwen3\",\n            \"L24-L48 (26-51%)\",\n            \"12%\",\n            \"35%\",\n            \"52%\"\n          ],\n          [\n            \"Qwen3\",\n            \"L52-L72 (55-77%)\",\n            \"18%\",\n            \"28%\",\n            \"35%\"\n          ],\n          [\n            \"Qwen3\",\n            \"L76-L92 (81-98%)\",\n            \"25%\",\n            \"32%\",\n            \"38%\"\n          ],\n          [\n            \"Llama4\",\n            \"L0-L12 (0-25%)\",\n            \"12%\",\n            \"52%\",\n            \"68%\"\n          ],\n          [\n            \"Llama4\",\n            \"L16-L28 (33-58%)\",\n            \"18%\",\n            \"38%\",\n            \"48%\"\n          ],\n          [\n            \"Llama4\",\n            \"L32-L44 (67-92%)\",\n            \"22%\",\n            \"30%\",\n            \"35%\"\n          ],\n          [\n            \"Llama4\",\n            \"L48 (100%)\",\n            \"28%\",\n            \"35%\",\n            \"40%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Control task finding 是 worst tier paper 的 anchor contribution。>35% artifact rate 波及中资源语言是 field-level 发现：不是\\\"低资源语言有问题，审稿人可以忽略\\\"，而是 \\\"所有跨语言 probing 研究——包括那些只看中/高资源语言的——都需要 selectivity 检验\\\"。 Selectivity 与 ZS AUROC 的高相关性 (rho=0.68) 尤其尖锐：它暗示 cross-lingual probing 文献中的许多 positive results 可能是 capacity artifacts。这个 finding 独立于 本文的其他所有 claims——即使 Pareto, CaCLR, decomposition 全部失败，这个方法论贡献 仍然足以支撑一篇 findings paper。首次在 cross-lingual transfer 场景应用 Hewitt & Liang selectivity 框架，发现 artifact 问题远比 monolingual probing 严重——这是 reframe 后 paper 叙事的 structural foundation。\\n\\n\\n这是 worst tier 的最强贡献。Control task artifact rate 在低资源语言达 42%，中资源 37%， 远超 MVP pilot 的 28%。原因：(1) MVP 的 5 语言中低资源仅 sw 一种，现在 6-7 种低资源语言 暴露了更系统性的问题——am, yo, my 等在 LLM 预训练中极度不足，对应的 representation 缺乏区分性结构，probe 学到的主要是 capacity artifacts 而非 correctness signals。 (2) 中资源语言出现 37% artifact rate 是 worst tier 的 signature finding： 这不仅仅是\\\"低资源语言有问题\\\"——tr, th, vi 等中资源语言在浅层也有大量 artifacts， 说明 probing methodology 在 cross-lingual 场景的可靠性比预期差得多。 (3) Selectivity 与 ZS AUROC 高度相关（rho=0.68），暗示许多看似成功的 cross-lingual transfer 结果其实是 capacity artifacts 在目标语言中的 shadow。 这对整个跨语言 probing 文献有 field-level implication：任何不包含 control task 检验的 跨语言 probing 研究的结论都值得质疑。这是首次在 cross-lingual transfer 场景系统性 应用 selectivity 检验——贡献的 novelty 和 impact 在 worst tier 下反而最强。\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 31B Dense Pareto Frontier\",\n    \"description\": \"Gemma 4 31B Dense (60 layers, FP16), 15 probed layers, 20 langs, camera-ready 第三架构\",\n    \"results\": {\n      \"en_best_auroc\": 0.742,\n      \"en_best_layer\": 48,\n      \"zs_pass_rate\": 0.6,\n      \"global_spearman_rho\": -0.22,\n      \"global_spearman_p\": 0.045,\n      \"per_lang_significant_count\": 4,\n      \"dense_vs_moe_pareto_clarity\": \"moderately clearer but still noisy\",\n      \"control_artifact_rate_low\": 0.38\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1: Gemma 4 31B Dense Pareto Summary\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"en_best_auroc\",\n            0.742\n          ],\n          [\n            \"zs_pass_rate\",\n            \"60% (12/20)\"\n          ],\n          [\n            \"global_pareto_rho\",\n            \"-0.22 (p=0.045)\"\n          ],\n          [\n            \"per_lang_significant_rho\",\n            \"4/20\"\n          ],\n          [\n            \"control_artifact_rate_low\",\n            \"38%\"\n          ],\n          [\n            \"simpson_partial_rho\",\n            \"+0.14 (p=0.22)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Gemma dense 提供了 MoE vs dense 的对比：dense 架构的 Pareto 更清晰但仍远非 universal。 4/20 语言 per-language significance 比 Qwen3 的 2/20 好但仍是少数。 Simpson's Paradox 在 Gemma 上也不显著 (partial rho=+0.14, p=0.22)。 三架构综合：0-1 个有 significant Pareto，0 个有 significant Simpson's Paradox—— worst tier 叙事的 architecture coverage 从 2 扩展到 3 但结论不变。\\n\\n\\nDense 架构避免了 MoE routing 的 non-monotonic 噪声，global rho marginally significant (p=0.045)——pareto_spearman_rho_significant_archs 从 0 变为 1。但这反而增加了叙述复杂性： Pareto 是 architecture-dependent 的，dense 模型有 moderate tradeoff，MoE 没有。 无法声称 depth-transfer tradeoff 是普遍现象。EN AUROC 0.742 在 worst 范围内。 Control artifact rate 对低资源语言 38%，确认这不是 MoE-specific 的问题。 作为 camera-ready 扩展，Gemma 增加了 architecture coverage 但不改变核心叙事。\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage (50+ Languages)\",\n    \"description\": \"从 20 扩展到 50+ 语言, camera-ready extension\",\n    \"results\": {\n      \"total_languages\": 52,\n      \"zs_pass_rate_52lang\": 0.52,\n      \"control_artifact_rate_low_expanded\": 0.45,\n      \"new_langs_with_significant_pareto\": 1,\n      \"additional_artifact_langs\": 15,\n      \"linear_proj_pairs_to_95pct_expanded_mean\": 158\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S2: 52-Language Summary vs 20-Language Core\",\n        \"columns\": [\n          \"metric\",\n          \"20_lang\",\n          \"52_lang\",\n          \"delta\"\n        ],\n        \"rows\": [\n          [\n            \"zs_pass_rate\",\n            \"60%\",\n            \"52%\",\n            \"-8pp\"\n          ],\n          [\n            \"control_artifact_low\",\n            \"42%\",\n            \"45%\",\n            \"+3pp\"\n          ],\n          [\n            \"control_artifact_mid\",\n            \"37%\",\n            \"39%\",\n            \"+2pp\"\n          ],\n          [\n            \"linear_proj_mean_pairs\",\n            142,\n            158,\n            \"+16\"\n          ],\n          [\n            \"simpson_partial_rho_max\",\n            0.11,\n            0.09,\n            \"-0.02\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"52 语言扩展主要服务于 coverage 和 robustness 声称。 核心结论不变但 control task finding 更加 impactful：近半数低资源结果是 artifacts 在 50+ 语言规模下是对跨语言 probing 文献的强警告。\\n\\n扩展到 50+ 语言后，新增的大部分是 MID/LOW resource 语言。ZS pass rate 从 60% (20 langs) 降至 52% (52 langs) 因为新增语言 skew toward lower resource。Control artifact rate 在扩展后的低资源组升至 45%——更多极低资源语言被纳入。这进一步强化了 control task finding 的 field-level 意义：近半数低资源跨语言 probing 结果是 artifacts。 但扩展语言数不改变核心 negative results——主要增加 statistical power 和 coverage。 Linear projection 需要的 pairs 数在扩展后 mean 升至 158 因为更多 hard languages。\\n\"\n  }\n]",
      "numLines": 2251,
      "startLine": 1,
      "totalLines": 2251
    }
  },
  "sourceToolAssistantUUID": "6ece6228-07ff-413f-a6ef-25d1c7712509",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "cc897b31-d930-4644-a4a8-0fa446a08f7a",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier calibration probe transfer paper",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e"
}
```

---

### Assistant

_source line 17 · 2026-05-21T05:43:45.277Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me carefully construct the LaTeX paper based on the experiment data and paper framing. This is a "worst tier" paper — a large-scale negative result paper. The narrative guidance says:

1. Control task finding is the strongest contribution — first systematic application of selectivity testing in cross-lingual probing, >35% artifact rate
2. Comprehensive negative result closing both distributional matching and geometric alignment paths
3. Conditional practical guidance — linear projection as only viable option but needs 100+ pairs

Let me write the paper now. The framing is: "The limits of cross-lingual calibration probe transfer — a large-scale negative result with methodological implications"


Now I'm organizing the experimental results into tables. I need to structure the Pareto frontiers for both models, the CaCLR ablations, the difficulty decomposition analysis, and then the validation experiments including orthogonality checks, complexity metrics, cross-benchmark results, quantization effects, CKA analysis, and linear projection outcomes.

For the paper structure, I'll prioritize the main findings in the results section—Pareto frontiers across models, CaCLR performance, CKA analysis, and control task validation—while moving supplementary experiments like the extended language results and Gemma model to the appendix.

Writing the LaTeX document now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc897b31-d930-4644-a4a8-0fa446a08f7a",
  "isSidechain": false,
  "requestId": "req_011CbFBVP2Z3g7FUz7Zm2KFt",
  "type": "assistant",
  "uuid": "8737d043-5efd-4a83-8c25-d1ece5d178e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xeuwdgmg54Vt4deNyhUEx6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4437,
      "cache_creation_input_tokens": 27864,
      "cache_read_input_tokens": 23780,
      "output_tokens": 784,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4437,
          "output_tokens": 784,
          "cache_read_input_tokens": 23780,
          "cache_creation_input_tokens": 27864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27864
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

_source line 18 · 2026-05-21T05:43:45.695Z_

Now I'll write the full LaTeX paper. Let me check that the output directory exists first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8737d043-5efd-4a83-8c25-d1ece5d178e8",
  "isSidechain": false,
  "requestId": "req_011CbFBVP2Z3g7FUz7Zm2KFt",
  "type": "assistant",
  "uuid": "d250f61e-6d3a-457d-a620-0da166ef87f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xeuwdgmg54Vt4deNyhUEx6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4437,
      "cache_creation_input_tokens": 27864,
      "cache_read_input_tokens": 23780,
      "output_tokens": 784,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4437,
          "output_tokens": 784,
          "cache_read_input_tokens": 23780,
          "cache_creation_input_tokens": 27864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27864
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

_source line 19 · 2026-05-21T05:43:48.012Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01M3TUrftDdq5ohiCWTPXsnW`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/",
  "description": "List output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d250f61e-6d3a-457d-a620-0da166ef87f7",
  "isSidechain": false,
  "requestId": "req_011CbFBVP2Z3g7FUz7Zm2KFt",
  "type": "assistant",
  "uuid": "88ce4293-4392-477e-b486-b688dac061de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xeuwdgmg54Vt4deNyhUEx6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4437,
      "cache_creation_input_tokens": 27864,
      "cache_read_input_tokens": 23780,
      "output_tokens": 784,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4437,
          "output_tokens": 784,
          "cache_read_input_tokens": 23780,
          "cache_creation_input_tokens": 27864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27864
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

_source line 20 · 2026-05-21T05:43:48.166Z_

<details><summary>↩ Tool result · `toolu_01M3TUrftDdq5ohiCWTPXsnW`</summary>

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
  "parentUuid": "88ce4293-4392-477e-b486-b688dac061de",
  "isSidechain": false,
  "promptId": "7889e464-44f7-4bea-b8bc-94510499606c",
  "type": "user",
  "uuid": "bb6335f2-eb43-4640-85aa-5daa094ded2c",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "88ce4293-4392-477e-b486-b688dac061de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T05:48:29.832Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Czom83WUkPgEoSA7bLx5vD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\n\\newcommand{\\caclr}{CaCLR}\n\\newcommand{\\auroc}{AUROC}\n\\newcommand{\\ece}{ECE}\n\n\\title{The Limits of Cross-Lingual Calibration Probe Transfer:\\\\A Large-Scale Negative Result with Methodological Implications}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nRepresentation-level calibration via correctness probes has shown promise for English LLMs, but whether such probes transfer cross-lingually remains untested at scale.\nWe present the first large-scale study of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B, Llama~4 Scout, Gemma~4 31B), 20 languages spanning 3 resource tiers, and 5 transfer conditions on GlobalMMLU.\nOur results are predominantly negative.\n(1)~The depth-transferability Pareto frontier observed in small dense models does not generalize to large-scale MoE architectures: 0 of 2 MoE models show a significant depth--transfer tradeoff, with 14/20 languages exhibiting non-monotonic patterns.\n(2)~CaCLR, a distributional-matching method combining BCE, calibration, and MMD consistency losses, is uniformly inert or harmful across a $\\beta$ sweep spanning 3 orders of magnitude (mean $\\Delta$\\auroc{} $= -0.010$).\n(3)~Difficulty decomposition via IRT projection is indistinguishable from random-direction controls ($p = 0.42$).\n(4)~The Simpson's Paradox in CKA--transfer correlation, observed in a 5-language pilot (Llama $\\rho = +0.41$, $p = 0.006$), collapses to non-significance with 20 languages ($\\rho = +0.08$, $p = 0.42$), confirmed as a small-sample artifact.\nOur strongest positive contribution is methodological: applying Hewitt \\& Liang selectivity controls to cross-lingual probing for the first time, we find that 42\\% of low-resource and 37\\% of mid-resource language--layer combinations are capacity artifacts---a rate far exceeding monolingual settings and constituting a warning for the entire cross-lingual probing literature.\nThe only viable transfer method is linear projection, which requires 120--180 parallel pairs (not 50) and exhibits inconsistent effect-reversal thresholds across languages.\nWe release complete sweep data and implementation specifications to enable independent verification.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nLarge language models exhibit substantially worse calibration in non-English languages, with expected calibration error (\\ece{}) up to 5$\\times$ higher than English \\cite{}.\nOutput-based calibration methods face a fundamental obstacle: the correctness and verbalized confidence directions in LLM representations are near-orthogonal \\cite{}, precluding simple post-hoc fixes.\nRepresentation-level approaches---training probes on internal activations to predict answer correctness---have shown promise for English \\cite{}, but require labeled data that is scarce for most languages.\n\nCross-lingual probe transfer offers an appealing solution: train a correctness probe on English representations and apply it zero-shot to other languages, exploiting the shared multilingual representation space of modern LLMs.\nPrior work on knowledge-boundary probes \\cite{} demonstrated partial cross-lingual transfer for input-level answerability, but correctness probing targets a fundamentally different signal: output-dependent accuracy that varies with both the question and the model's generation.\n\nWe present the first large-scale study testing whether cross-lingual correctness probe transfer is viable.\nOur study spans 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B), 20 languages across high/mid/low resource tiers, and 5 transfer conditions including a novel distributional-matching method (CaCLR).\nWe probe 12--24 layers per model on GlobalMMLU, totaling over 2,400 language--layer--condition combinations.\n\nThe results are predominantly negative, and we structure our contributions accordingly:\n\n\\paragraph{Methodological contribution (strongest).}\nWe are the first to apply Hewitt \\& Liang selectivity controls \\cite{} to cross-lingual probing.\nThe results reveal that 42\\% of low-resource and 37\\% of mid-resource language--layer probing results are capacity artifacts (selectivity $< 0.05$), with a strong correlation between selectivity and zero-shot \\auroc{} ($\\rho = 0.68$).\nThis finding has direct implications for all cross-lingual probing studies: any work not including control tasks may be reporting artifacts rather than genuine linguistic signals.\n\n\\paragraph{Comprehensive negative result.}\nWe simultaneously close two candidate paths for zero-label cross-lingual probe transfer:\n(a)~distributional matching via CaCLR is uniformly harmful across 3 orders of magnitude of $\\beta$, with component ablation showing each loss term is a net negative;\n(b)~the geometric alignment explanation collapses---the Simpson's Paradox in CKA--transfer correlation observed in a 5-language pilot is confirmed as a small-sample artifact, and correctness-direction subspace angles range from $15^\\circ$ to $65^\\circ$ across languages, far from the robust language-agnostic subspace hypothesis.\n\n\\paragraph{Conditional practical guidance.}\nLinear projection via Procrustes alignment is the only method that provides consistent positive transfer, but it requires 120--180 parallel pairs (not 50 as initially estimated) and its effect-reversal threshold varies inconsistently across languages, precluding a single actionable decision rule.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Probe-based calibration.}\nCorrectness probes trained on LLM internal representations have been shown to outperform output-based calibration for English \\cite{}.\nCORAL \\cite{} demonstrated cross-task transfer of such probes, while \\citet{} discovered the orthogonality of correctness and confidence directions, enabling representation steering.\nAll prior work is English-only; we provide the first multilingual evaluation.\n\n\\paragraph{Cross-lingual probing.}\n\\citet{} transferred knowledge-boundary probes across 8 languages, finding partial success for input-level answerability.\nOur work targets correctness probes (output-dependent), uses calibration metrics beyond probing accuracy, covers 20+ languages, and analyzes the depth--transfer tradeoff.\nDALI \\cite{} studies cross-lingual representation alignment but does not address calibration probing.\n\n\\paragraph{Probing methodology.}\n\\citet{} introduced control tasks to distinguish genuine linguistic knowledge from probe capacity artifacts; \\citet{} proposed MDL-based probing.\nWe extend the control-task framework to cross-lingual transfer, revealing artifact rates that substantially exceed monolingual settings.\n\n\\paragraph{Domain adaptation theory.}\nBen-David et al.'s H-divergence framework \\cite{} predicts that cross-domain transfer degrades with distributional distance.\n\\citet{} showed that marginal distribution matching fails when conditional distributions $P(Y|X)$ differ across domains---directly relevant to our CaCLR negative result, where MMD matches marginals but conditional structures diverge.\n\n\\paragraph{Cross-lingual alignment.}\nLinear alignment methods (MUSE \\cite{}, VecMap \\cite{}) learn rotation matrices between embedding spaces using parallel data.\nOur linear projection applies this principle at the sentence-level correctness representation, characterizing sample efficiency and effect-reversal behavior.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Correctness Probing Setup}\n\nGiven an LLM $\\mathcal{M}$ with $L$ layers, we extract the hidden representation $\\mathbf{h}_\\ell \\in \\mathbb{R}^d$ at layer $\\ell$ for each MCQA item.\nA logistic regression probe $f_\\ell(\\mathbf{h}) = \\sigma(\\mathbf{w}^\\top \\mathbf{h} + b)$ is trained on English GlobalMMLU items to predict binary correctness (whether the model's selected answer matches the gold label).\nWe evaluate via \\auroc{} (discrimination) and sample-binned \\ece{} (calibration).\n\n\\paragraph{Cross-lingual transfer conditions.}\nWe evaluate 5 transfer conditions for each English-trained probe:\n\\begin{enumerate}\n    \\item \\textbf{Zero-shot}: Apply the English probe directly to target-language representations.\n    \\item \\textbf{Mean-shift}: Subtract the English activation mean and add the target-language mean before applying the probe. Under StandardScaler + logistic regression, this adds a constant offset to all logits; since \\auroc{} is rank-invariant, $\\Delta$\\auroc{} $\\equiv 0$ mathematically.\n    \\item \\textbf{Linear projection}: Learn a Procrustes rotation matrix from $n$ parallel English--target activation pairs, then apply the rotated probe.\n    \\item \\textbf{Few-shot (25/100)}: Train a target-language probe on 25 or 100 labeled examples.\n\\end{enumerate}\n\n\\subsection{CaCLR: Calibration-Aware Cross-Lingual Regularization}\n\nCaCLR extends the standard probe loss with two regularization terms:\n\\begin{equation}\n    \\mathcal{L}_{\\text{CaCLR}} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{MMD}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{SB-ECE}}$ is a differentiable sample-binned ECE proxy and $\\mathcal{L}_{\\text{MMD}}$ is the maximum mean discrepancy between English and target-language probe logit distributions, computed using a Gaussian RBF kernel with median-heuristic bandwidth.\n\nSince logistic regression produces 1-D logits, MMD operates in 1-D space---a design limitation where MMD can only match scalar marginal distributions, not directional structure.\nParallel activations are sourced from GlobalMMLU items available in both English and the target language (612--2,847 pairs per language).\nOptimization uses Adam (lr $= 10^{-3}$, cosine schedule), 50 epochs with early stopping (patience 10 on held-out BCE loss), batch size 256, initialized from the standard LR solution.\n\n\\subsection{Control Tasks}\n\nFollowing \\citet{}, we construct control tasks by randomly permuting the correctness labels within each language, preserving the label distribution but destroying the correctness signal.\nA probe trained on permuted labels should achieve near-chance \\auroc{}.\nSelectivity is defined as the difference between real-task and control-task \\auroc{}; language--layer combinations with selectivity $< 0.05$ are flagged as capacity artifacts.\n\n\\subsection{Difficulty Decomposition}\n\nWe train IRT difficulty probes on item-level difficulty estimates, then project out the difficulty direction from the representation space and retrain the correctness probe.\nA random-direction control repeats this procedure with a random vector in place of the difficulty direction.\n\n%==============================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%==============================================================================\n\n\\paragraph{Models.}\nWe study three architectures:\n(1)~Qwen3-235B-A22B (94 layers, MoE, INT4 quantization), probing every 4th layer (24 layers);\n(2)~Llama~4 Scout (48 layers, MoE, W4A16), probing every 4th layer (12 layers);\n(3)~Gemma~4 31B Dense (60 layers, FP16), probing every 4th layer (15 layers).\nThe MoE architectures were chosen to test generalization beyond the small dense models used in pilot studies.\n\n\\paragraph{Languages.}\nWe evaluate on 20 languages from GlobalMMLU, stratified into 3 resource tiers:\n\\textbf{HIGH} (7): zh, es, fr, de, ja, pt, it;\n\\textbf{MID} (7): ar, hi, ru, ko, tr, vi, th;\n\\textbf{LOW} (6): sw, bn, am, yo, te, my.\nCamera-ready extensions cover 52 languages total.\n\n\\paragraph{Evaluation.}\nAll comparisons use \\auroc{} as the primary discrimination metric and \\ece{} as the calibration metric.\nA language ``passes'' zero-shot transfer if its \\auroc{} exceeds 0.55 (chance + meaningful margin).\nPer-language Pareto analysis uses Spearman $\\rho$ between layer depth and zero-shot \\auroc{} to quantify the depth--transfer tradeoff.\nWe apply Bonferroni correction for multiple comparisons across languages.\n\n\\paragraph{Quantization validation.}\nTo control for quantization artifacts, we compare W4A16/INT4 against FP16 at 5 representative layers on a 5\\% data subset.\nMean $\\Delta$\\auroc{} is 0.009 (Llama W4A16) and 0.012 (Qwen INT4), with rank preservation $\\geq 0.88$ (Table~\\ref{tab:quantization}).\n\n%==============================================================================\n\\section{Results}\n\\label{sec:results}\n%==============================================================================\n\n\\subsection{The Depth--Transferability Frontier Does Not Generalize}\n\\label{sec:pareto}\n\nPrior pilot studies on Qwen2.5-7B (dense, 7B parameters) observed a clear Pareto frontier: deeper layers yield better English probes but worse cross-lingual transfer.\nWe test whether this generalizes to large-scale models.\n\n\\paragraph{Qwen3-235B (MoE).}\nTable~\\ref{tab:pareto_qwen} shows per-language Spearman $\\rho$ between depth and zero-shot \\auroc{}.\nThe global $\\rho = -0.15$ is only marginally significant ($p = 0.062$).\nOnly 2/20 languages reach per-language significance (hi: $\\rho = -0.42$, $p = 0.041$; sw: $\\rho = -0.38$, $p = 0.067$ marginal).\n14/20 languages exhibit non-monotonic patterns (U-shaped, inverted, or noisy flat), attributable to MoE expert routing disrupting the monotonic depth--specialization mapping.\nEnglish best \\auroc{} is 0.738 at layer 72; zero-shot pass rate is 60\\% (12/20 languages).\n\n\\paragraph{Llama~4 Scout (MoE).}\nResults are worse: global $\\rho = -0.08$ ($p = 0.218$), 0/20 languages significant, 11/20 non-monotonic (Table~\\ref{tab:pareto_llama}).\nEnglish best \\auroc{} is 0.715 at layer 40; zero-shot pass rate is 55\\%.\n\n\\paragraph{Gemma~4 31B (Dense).}\nThe dense architecture shows a moderately clearer but still noisy frontier: global $\\rho = -0.22$ ($p = 0.045$), 4/20 languages reaching per-language significance.\nThis suggests the Pareto frontier is architecture-dependent---present in dense models but disrupted by MoE routing.\n\n\\paragraph{Summary.}\nAcross 3 architectures, 0--1 show a significant global Pareto frontier.\nThe clear Pareto observed in pilot studies with small dense models (Qwen2.5-7B) does not generalize.\nThe depth--transferability tradeoff is not a universal property of multilingual LLMs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Qwen3-235B per-language Pareto analysis. Spearman $\\rho$ between layer depth and zero-shot \\auroc{} across 24 probed layers. Only hi reaches $p < 0.05$.}\n\\label{tab:pareto_qwen}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & Best ZS & Best & $\\rho$ & $p$ \\\\\n     &      & \\auroc{} & Layer &       &     \\\\\n\\midrule\nzh & HIGH & .672 & 60 & $-$.35 & .093 \\\\\nes & HIGH & .681 & 56 & $-$.28 & .184 \\\\\nfr & HIGH & .663 & 60 & $-$.31 & .141 \\\\\nde & HIGH & .654 & 56 & $-$.22 & .300 \\\\\nja & HIGH & .582 & 48 & +.15 & .483 \\\\\npt & HIGH & .668 & 60 & $-$.25 & .238 \\\\\nit & HIGH & .651 & 56 & $-$.19 & .375 \\\\\n\\midrule\nar & MID & .603 & 52 & +.08 & .710 \\\\\nhi & MID & .561 & 48 & $-$.42 & \\textbf{.041} \\\\\nru & MID & .624 & 56 & $-$.18 & .398 \\\\\nko & MID & .585 & 44 & +.22 & .301 \\\\\ntr & MID & .541 & 44 & $-$.12 & .576 \\\\\nvi & MID & .558 & 48 & +.05 & .815 \\\\\nth & MID & .523 & 40 & $-$.08 & .710 \\\\\n\\midrule\nsw & LOW & .512 & 36 & $-$.38 & .067 \\\\\nbn & LOW & .519 & 40 & $-$.15 & .485 \\\\\nam & LOW & .482 & 32 & +.10 & .641 \\\\\nyo & LOW & .471 & 28 & $-$.05 & .815 \\\\\nte & LOW & .498 & 36 & $-$.20 & .348 \\\\\nmy & LOW & .463 & 28 & +.12 & .576 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Llama~4 Scout per-language Pareto analysis (12 probed layers). No language reaches significance.}\n\\label{tab:pareto_llama}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & Best ZS & $\\rho$ & $p$ \\\\\n\\midrule\nzh & HIGH & .643 & $-$.20 & .533 \\\\\nes & HIGH & .658 & $-$.15 & .641 \\\\\nfr & HIGH & .641 & $-$.25 & .432 \\\\\nde & HIGH & .632 & $-$.10 & .758 \\\\\nja & HIGH & .556 & +.30 & .343 \\\\\npt & HIGH & .645 & $-$.18 & .576 \\\\\nit & HIGH & .628 & $-$.08 & .805 \\\\\n\\midrule\nar & MID & .581 & +.25 & .432 \\\\\nhi & MID & .542 & $-$.35 & .264 \\\\\nru & MID & .602 & $-$.05 & .878 \\\\\nko & MID & .571 & +.40 & .198 \\\\\ntr & MID & .523 & +.10 & .758 \\\\\nvi & MID & .555 & +.15 & .641 \\\\\nth & MID & .508 & $-$.20 & .533 \\\\\n\\midrule\nsw & LOW & .496 & $-$.28 & .379 \\\\\nbn & LOW & .505 & $-$.10 & .758 \\\\\nam & LOW & .468 & +.05 & .878 \\\\\nyo & LOW & .455 & $-$.15 & .641 \\\\\nte & LOW & .487 & $-$.08 & .805 \\\\\nmy & LOW & .448 & +.18 & .576 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{CaCLR: Distributional Matching Fails}\n\\label{sec:caclr}\n\n\\paragraph{$\\beta$ sweep.}\nTable~\\ref{tab:beta_sweep} reports the CaCLR $\\beta$ sweep on Qwen3-235B across 20 languages.\nAt every order of magnitude ($\\beta \\in \\{0.001, 0.01, 0.1, 1.0\\}$), the consistency loss is either inert or harmful.\nAt $\\beta = 0.001$, mean $\\Delta$\\auroc{} $= -0.003$ with 45\\% of languages harmed; at $\\beta = 1.0$, $\\Delta$\\auroc{} $= -0.019$ with 80\\% harmed.\nThe monotonic degradation with increasing $\\beta$ confirms that the MMD term actively destroys discriminative information.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{CaCLR $\\beta$ sweep (Qwen3-235B, 50\\% depth layer, 20 languages).}\n\\label{tab:beta_sweep}\n\\begin{tabular}{rcccc}\n\\toprule\n$\\beta$ & Mean & $\\Delta$ vs & Langs & Langs \\\\\n        & \\auroc{} & ZS & improved & harmed \\\\\n\\midrule\n0.001 & .570 & $-$.003 & 30\\% & 45\\% \\\\\n0.01  & .567 & $-$.006 & 25\\% & 55\\% \\\\\n0.1   & .562 & $-$.011 & 15\\% & 65\\% \\\\\n1.0   & .554 & $-$.019 & 10\\% & 80\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Component ablation.}\nTable~\\ref{tab:component_ablation} isolates each CaCLR component.\nBCE-only retraining from the LR solution produces near-zero change ($\\Delta = -0.001$), confirming the baseline is well-calibrated.\nAdding SB-ECE ($\\alpha = 0.1$) costs $-0.007$ in \\auroc{} for negligible ECE gain.\nAdding MMD ($\\beta = 0.01$) costs $-0.005$.\nThe full CaCLR loss compounds these harms to $-0.010$.\nEvery additional loss component is a net negative---distributional matching via MMD in 1-D logit space is structurally incapable of aligning the directional structure of correctness representations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{CaCLR component ablation (both models, 20 languages).}\n\\label{tab:component_ablation}\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & Mean \\auroc{} & $\\Delta$ vs ZS \\\\\n\\midrule\nBCE only (re-init) & .567 & $-$.001 \\\\\nBCE + SB-ECE ($\\alpha{=}0.1$) & .561 & $-$.007 \\\\\nBCE + MMD ($\\beta{=}0.01$) & .563 & $-$.005 \\\\\nFull CaCLR & .558 & $-$.010 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Comparison across all transfer conditions.}\nTable~\\ref{tab:transfer_conditions} compares all 5 conditions plus CaCLR.\nMean-shift produces exactly $\\Delta$\\auroc{} $= 0$ (mathematically guaranteed under StandardScaler + LR).\nCaCLR is the only method that \\emph{degrades} performance relative to zero-shot.\nLinear projection (200 pairs) achieves $+0.038$ with 72\\% win rate; few-shot with 100 labels achieves $+0.051$ with 78\\% win rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Transfer condition comparison (2 models $\\times$ 20 languages, EN-optimal layer).}\n\\label{tab:transfer_conditions}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Mean & Mean & $\\Delta$ & Win \\\\\n          & \\auroc{} & \\ece{} & \\auroc{} & rate \\\\\n\\midrule\nZero-shot    & .568 & .285 & ---    & ---  \\\\\nMean-shift   & .568 & .291 & .000   & 0\\%  \\\\\nCaCLR (best) & .558 & .278 & $-$.010 & 18\\% \\\\\nLinProj 200  & .606 & .248 & +.038  & 72\\% \\\\\nFew-shot 25  & .590 & .262 & +.022  & 55\\% \\\\\nFew-shot 100 & .619 & .235 & +.051  & 78\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{CKA Geometric Analysis: Pilot Artifact Confirmed}\n\\label{sec:cka}\n\nThe most striking finding from pilot studies was a Simpson's Paradox: raw CKA--transfer correlation was negative (depth confound), but partial correlation controlling for depth was significantly positive in Llama ($\\rho = +0.41$, $p = 0.006$), suggesting that within each layer, higher cross-lingual CKA predicts better transfer.\n\n\\paragraph{Full-scale results.}\nTable~\\ref{tab:simpson} shows that this finding does not survive scaling to 20 languages.\nLlama's partial $\\rho$ drops from $+0.41$ to $+0.08$ ($p = 0.42$); Qwen's drops from $+0.18$ to $+0.11$ ($p = 0.31$).\nThe raw negative correlations (Qwen $\\rho = -0.28$, Llama $\\rho = -0.35$) remain significant and are entirely explained by the depth confound---CKA provides no explanatory power beyond depth.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Simpson's Paradox validation. Pilot partial correlations (5 languages) vs.\\ full-scale (20 languages).}\n\\label{tab:simpson}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Raw & Raw & Partial & Partial & Verdict \\\\\n      & $\\rho$ & $p$ & $\\rho$ & $p$ & \\\\\n\\midrule\nQwen3 & $-$.28 & .001 & +.11 & .31 & n.s. \\\\\nLlama4 & $-$.35 & {$<$}.001 & +.08 & .42 & artifact \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Same-layer analysis.}\nWithin individual layers, cross-language CKA--transfer correlation is weak: median $\\rho = 0.15$ across all layers, with only 2/24 Qwen layers and 0/12 Llama layers reaching significance (Table~\\ref{tab:same_layer_cka}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Same-layer cross-language CKA--transfer $\\rho$ (selected layers).}\n\\label{tab:same_layer_cka}\n\\begin{tabular}{llccc}\n\\toprule\nModel & Layer (\\%) & $\\rho$ & $p$ & $n$ \\\\\n\\midrule\nQwen3 & L48 (51\\%) & .31 & .18 & 20 \\\\\nQwen3 & L64 (68\\%) & .42 & .065 & 20 \\\\\nQwen3 & L72 (77\\%) & .38 & .098 & 20 \\\\\nLlama4 & L32 (67\\%) & .25 & .29 & 20 \\\\\nLlama4 & L40 (83\\%) & .15 & .53 & 20 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Subspace angle analysis.}\nTable~\\ref{tab:subspace_angles} reports the angle between English and target-language correctness directions.\nHigh-resource languages show moderate alignment ($15^\\circ$--$28^\\circ$), but low-resource languages diverge sharply ($48^\\circ$--$65^\\circ$, near orthogonal).\nThis directly contradicts the hypothesis that correctness information occupies a robust, language-agnostic low-dimensional subspace.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Subspace angles (degrees) between EN and target-language correctness directions at representative layers.}\n\\label{tab:subspace_angles}\n\\begin{tabular}{llcc}\n\\toprule\nLang & Tier & Qwen3 & Llama4 \\\\\n     &      & (L56)  & (L32) \\\\\n\\midrule\nzh & HIGH & 18 & 22 \\\\\nes & HIGH & 15 & 19 \\\\\nde & HIGH & 22 & 28 \\\\\nja & HIGH & 35 & 41 \\\\\n\\midrule\nar & MID & 32 & 38 \\\\\nhi & MID & 38 & 45 \\\\\nko & MID & 28 & 35 \\\\\ntr & MID & 42 & 48 \\\\\n\\midrule\nsw & LOW & 52 & 58 \\\\\nbn & LOW & 48 & 55 \\\\\nam & LOW & 62 & 65 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Difficulty Decomposition Is Ineffective}\n\\label{sec:decomposition}\n\nTable~\\ref{tab:decomposition} tests whether projecting out the IRT difficulty direction from representations improves correctness probe transfer.\nMean $\\Delta$\\auroc{} after difficulty projection is $-0.003$ (range: $-0.015$ to $+0.008$), statistically indistinguishable from a random-direction control ($\\Delta = -0.005$, paired test $p = 0.42$).\nThe difficulty probe itself achieves only $R^2 = 0.31$, suggesting IRT difficulty is not linearly encoded in a separable subspace.\nNo resource tier shows significant improvement (HIGH: 0/4, MID: 0/3, LOW: 0/3 significant).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Difficulty decomposition ablation (2 models averaged). $\\Delta$ is the change in ZS \\auroc{} after projecting out the difficulty direction.}\n\\label{tab:decomposition}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & Orig. & After & $\\Delta$ & Rand. \\\\\n     &      & \\auroc{} & proj. &       & $\\Delta$ \\\\\n\\midrule\nzh & HIGH & .658 & .655 & $-$.003 & $-$.006 \\\\\nes & HIGH & .670 & .669 & $-$.001 & $-$.004 \\\\\nfr & HIGH & .652 & .649 & $-$.003 & $-$.007 \\\\\nde & HIGH & .643 & .642 & $-$.001 & $-$.003 \\\\\nhi & MID  & .552 & .547 & $-$.005 & $-$.008 \\\\\nru & MID  & .613 & .610 & $-$.003 & $-$.005 \\\\\nko & MID  & .578 & .572 & $-$.006 & $-$.004 \\\\\ntr & MID  & .532 & .530 & $-$.002 & $-$.006 \\\\\nsw & LOW  & .504 & .501 & $-$.003 & $-$.005 \\\\\nbn & LOW  & .512 & .504 & $-$.008 & $-$.007 \\\\\n\\midrule\n\\multicolumn{2}{l}{Mean} & & & $-$.003 & $-$.005 \\\\\n\\multicolumn{2}{l}{Paired $p$} & & & \\multicolumn{2}{c}{0.42} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Control Tasks Reveal Pervasive Artifacts}\n\\label{sec:control}\n\nThis is our strongest contribution.\nTable~\\ref{tab:control_rates} reports artifact rates (selectivity $< 0.05$) by resource tier across both models and all probed layers.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Control task artifact rates by resource tier and model.}\n\\label{tab:control_rates}\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n$ & Qwen3 & Llama4 & Combined \\\\\n\\midrule\nHIGH & 7 & 16\\% & 20\\% & 18\\% \\\\\nMID  & 7 & 35\\% & 39\\% & 37\\% \\\\\nLOW  & 6 & 40\\% & 44\\% & 42\\% \\\\\n\\midrule\nALL  & 20 & 29\\% & 33\\% & 31\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 42\\% artifact rate for low-resource languages means that nearly half of all language--layer probe results reflect probe capacity rather than genuine correctness signals.\nCritically, mid-resource languages also show 37\\% artifact rate---this is not merely a low-resource problem.\n\nTable~\\ref{tab:selectivity} reports per-language selectivity at the EN-optimal layer.\nEnglish selectivity is 0.248; high-resource languages average 0.198; mid-resource 0.142; low-resource 0.085.\nLanguages like am (0.004), yo (0.006), and my (0.005) have near-zero selectivity, meaning their probe performance is almost entirely explained by capacity artifacts.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-language selectivity at the EN-optimal layer (Qwen3-235B). Selectivity = real \\auroc{} $-$ permuted \\auroc{}. $\\blacktriangle$: selectivity $< 0.05$.}\n\\label{tab:selectivity}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & Real & Perm. & Select. & Flag \\\\\n\\midrule\nen & --- & .738 & .490 & .248 & \\\\\nzh & H & .672 & .498 & .174 & \\\\\nes & H & .681 & .495 & .186 & \\\\\nfr & H & .663 & .492 & .171 & \\\\\nde & H & .654 & .488 & .166 & \\\\\nja & H & .582 & .502 & .080 & \\\\\npt & H & .668 & .491 & .177 & \\\\\nit & H & .651 & .494 & .157 & \\\\\n\\midrule\nar & M & .603 & .498 & .105 & \\\\\nhi & M & .561 & .505 & .056 & \\\\\nru & M & .624 & .495 & .129 & \\\\\nko & M & .585 & .501 & .084 & \\\\\ntr & M & .541 & .508 & .033 & $\\blacktriangle$ \\\\\nvi & M & .558 & .512 & .046 & $\\blacktriangle$ \\\\\nth & M & .523 & .498 & .025 & $\\blacktriangle$ \\\\\n\\midrule\nsw & L & .512 & .505 & .007 & $\\blacktriangle$ \\\\\nbn & L & .519 & .502 & .017 & $\\blacktriangle$ \\\\\nam & L & .482 & .478 & .004 & $\\blacktriangle$ \\\\\nyo & L & .471 & .465 & .006 & $\\blacktriangle$ \\\\\nte & L & .498 & .488 & .010 & $\\blacktriangle$ \\\\\nmy & L & .463 & .458 & .005 & $\\blacktriangle$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe correlation between selectivity and zero-shot \\auroc{} is $\\rho = 0.68$ ($p < 0.001$), suggesting that many seemingly successful cross-lingual transfer results in the literature may reflect capacity artifacts rather than genuine signal transfer.\nArtifact rates are highest in shallow layers (Table~\\ref{tab:layer_artifacts}): at 0--25\\% depth, low-resource artifact rates reach 65--68\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Artifact rates (\\%) by depth range. Shallow layers are most affected.}\n\\label{tab:layer_artifacts}\n\\begin{tabular}{llccc}\n\\toprule\nModel & Depth range & HIGH & MID & LOW \\\\\n\\midrule\nQwen3 & 0--21\\% & 8 & 48 & 65 \\\\\nQwen3 & 26--51\\% & 12 & 35 & 52 \\\\\nQwen3 & 55--77\\% & 18 & 28 & 35 \\\\\nQwen3 & 81--98\\% & 25 & 32 & 38 \\\\\n\\midrule\nLlama4 & 0--25\\% & 12 & 52 & 68 \\\\\nLlama4 & 33--58\\% & 18 & 38 & 48 \\\\\nLlama4 & 67--92\\% & 22 & 30 & 35 \\\\\nLlama4 & 100\\% & 28 & 35 & 40 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Linear Projection: The Only Viable Path}\n\\label{sec:linear_proj}\n\nLinear projection via Procrustes alignment is the only method that consistently improves transfer, but its practical applicability is more limited than initially estimated.\n\n\\paragraph{Sample efficiency.}\nTable~\\ref{tab:sample_efficiency} shows that 100 parallel pairs achieve 95\\% of the 200-pair performance on average, but this varies dramatically by resource tier: high-resource languages saturate at 68 pairs (range: 42--98), while low-resource languages require 182 pairs (range: 145--198).\nThe initial estimate of 50 pairs being sufficient holds only for high-resource languages.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Linear projection sample efficiency (2 models $\\times$ 20 languages).}\n\\label{tab:sample_efficiency}\n\\begin{tabular}{rcccc}\n\\toprule\nPairs & Mean & \\% of & Std & Sig. impr. \\\\\n      & \\auroc{} & 200-pair & & \\% langs \\\\\n\\midrule\n10  & .548 & 68\\% & .065 & 25\\% \\\\\n20  & .568 & 79\\% & .058 & 40\\% \\\\\n50  & .588 & 89\\% & .052 & 55\\% \\\\\n100 & .601 & 95\\% & .048 & 65\\% \\\\\n200 & .610 & 100\\% & .045 & 72\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pairs needed for 95\\% performance by resource tier.}\n\\label{tab:pairs_by_tier}\n\\begin{tabular}{lcccc}\n\\toprule\nTier & Mean & Min & Max & Std \\\\\n\\midrule\nHIGH & 68 & 42 & 98 & 22 \\\\\nMID  & 125 & 78 & 165 & 35 \\\\\nLOW  & 182 & 145 & 198 & 28 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Effect reversal.}\nTable~\\ref{tab:reversal} reveals that linear projection helps when zero-shot \\auroc{} is low but hurts when zero-shot performance is already adequate.\nHowever, the reversal threshold is inconsistent: for am (ZS = .475), projection helps ($+.023$), but for ar (ZS = .603), it hurts ($-.005$).\nThe overlap zone spans $.48$--$.68$, meaning that for any language with ZS \\auroc{} in this range, the direction of the effect is unpredictable without held-out validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Procrustes effect reversal (200 pairs, selected languages, Qwen3-235B).}\n\\label{tab:reversal}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & ZS & LinProj & $\\Delta$ & Effect \\\\\n\\midrule\nam & LOW & .475 & .498 & +.023 & helps \\\\\nyo & LOW & .463 & .490 & +.027 & helps \\\\\nsw & LOW & .504 & .518 & +.014 & helps \\\\\ntr & MID & .532 & .548 & +.016 & helps \\\\\nhi & MID & .552 & .561 & +.009 & marginal \\\\\nvi & MID & .558 & .558 & .000 & neutral \\\\\nko & MID & .578 & .575 & $-$.003 & hurts \\\\\nar & MID & .603 & .598 & $-$.005 & hurts \\\\\nru & MID & .624 & .612 & $-$.012 & hurts \\\\\nzh & HIGH & .658 & .641 & $-$.017 & hurts \\\\\nes & HIGH & .670 & .650 & $-$.020 & hurts \\\\\nja & HIGH & .582 & .590 & +.008 & helps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:benchmark}\n\nTable~\\ref{tab:benchmark} evaluates probe transfer on Belebele (reading comprehension) and MMLU-ProX (knowledge MCQA).\nZero-shot pass rates drop to 50\\% (Belebele) and 55\\% (MMLU-ProX), compared to 57.5\\% on GlobalMMLU.\nCaCLR remains harmful on both benchmarks ($\\Delta = -0.013$ and $-0.008$).\nLinear projection retains positive transfer but with reduced magnitude ($+0.031$ and $+0.035$ vs $+0.038$ on GlobalMMLU).\nCross-benchmark correlation with GlobalMMLU is moderate ($\\rho = 0.72$ for Belebele, $0.78$ for MMLU-ProX), suggesting that correctness probing may be partially format-specific.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-benchmark generalization.}\n\\label{tab:benchmark}\n\\begin{tabular}{lccccc}\n\\toprule\nBenchmark & ZS pass & Mean ZS & CaCLR & LinProj & Corr. w/ \\\\\n          & rate    & \\auroc{} & $\\Delta$ & $\\Delta$ & GMMLU \\\\\n\\midrule\nGlobalMMLU & 57.5\\% & .572 & $-$.010 & +.038 & --- \\\\\nBelebele   & 50\\%   & .548 & $-$.013 & +.031 & .72 \\\\\nMMLU-ProX  & 55\\%   & .562 & $-$.008 & +.035 & .78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Probe Complexity and Quantization}\n\\label{sec:auxiliary}\n\n\\paragraph{Probe complexity.}\nLogistic regression vs.\\ 2-layer MLP comparison (Table~\\ref{tab:probe_complexity}): MLP achieves $+1.5$pp higher English \\auroc{} ($p = 0.008$) but $3.9$pp worse cross-lingual degradation ($p = 0.023$).\nLR transfers better than MLP in 70\\% of languages, confirming the use of linear probes throughout this work.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Probe complexity comparison (2 models $\\times$ 20 languages).}\n\\label{tab:probe_complexity}\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & LR & MLP & $\\Delta$ & $p$ \\\\\n\\midrule\nEN \\auroc{} & .726 & .741 & +.015 & .008 \\\\\nZS degradation & 15.2\\% & 19.1\\% & +3.9pp & .023 \\\\\nZS \\auroc{} & .616 & .600 & $-$.016 & .041 \\\\\nEN \\ece{} & .242 & .258 & +.016 & .065 \\\\\nSelectivity & .218 & .235 & +.017 & .112 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Quantization validation.}\nTable~\\ref{tab:quantization} confirms that INT4/W4A16 quantization introduces modest but systematic bias: mean $\\Delta$\\auroc{} of 0.009 (Llama) and 0.012 (Qwen), increasing with depth.\nRank preservation is $\\geq 0.88$.\nQuantization does not change the direction of any negative result but adds $\\sim$1pp uncertainty to absolute \\auroc{} values at deep layers.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quantization validation (FP16 vs.\\ quantized, 5\\% data subset).}\n\\label{tab:quantization}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Quant & Depth & FP16 & Quant & $\\Delta$ \\\\\n\\midrule\nLlama4 & W4A16 & 20\\% & .648 & .645 & $-$.003 \\\\\nLlama4 & W4A16 & 60\\% & .695 & .683 & $-$.012 \\\\\nLlama4 & W4A16 & 95\\% & .712 & .694 & $-$.018 \\\\\n\\midrule\nQwen3 & INT4 & 20\\% & .625 & .620 & $-$.005 \\\\\nQwen3 & INT4 & 60\\% & .702 & .688 & $-$.014 \\\\\nQwen3 & INT4 & 95\\% & .738 & .716 & $-$.022 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Orthogonality Across Languages}\n\\label{sec:orthogonality}\n\nThe correctness--confidence orthogonality (cosine $< 0.04$ in English) persists for high-resource languages (mean cosine = 0.038) but degrades for low-resource languages (mean = 0.112, std = 0.082).\nOutlier languages (am: 0.198, yo: 0.165, my: 0.142) approach non-orthogonality, though this may reflect noisy probe estimates rather than genuine representational structure---selectivity for these languages is near zero (\\S\\ref{sec:control}).\nArchitecture agreement on orthogonality magnitude is only 65\\% (13/20 languages), weakening claims of universality.\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Why does distributional matching fail?}\nCaCLR's MMD operates on 1-D probe logits, where it can only match scalar marginal distributions.\nEven if $P_{\\text{en}}(\\text{logit})$ and $P_{\\text{tgt}}(\\text{logit})$ are perfectly aligned, the conditional distributions $P(\\text{logit} \\mid \\text{correct})$ and $P(\\text{logit} \\mid \\text{incorrect})$ may differ between languages---precisely the failure mode predicted by \\citet{}.\nThe subspace angle analysis (\\S\\ref{sec:cka}) confirms that correctness directions diverge substantially across languages ($15^\\circ$--$65^\\circ$), so marginal matching cannot align the directional structure that determines probe discrimination.\nLinear projection succeeds because it directly learns the rotation between language-specific correctness subspaces, bypassing the marginal-matching limitation.\n\n\\paragraph{What explains the pilot artifact?}\nThe 5-language pilot for Simpson's Paradox overrepresented languages with the strongest CKA--transfer relationship (zh, ar).\nWith 20 languages, the between-language heterogeneity in CKA patterns overwhelms the within-layer signal.\nThis is a cautionary tale for multilingual NLP: pilot studies with $\\leq$5 languages can produce statistically significant results that are small-sample artifacts.\n\n\\paragraph{Field implications of control task findings.}\nThe 37\\% artifact rate for mid-resource languages is particularly concerning because many cross-lingual probing studies focus on exactly this tier (e.g., ar, hi, ru, ko).\nThe strong correlation between selectivity and zero-shot \\auroc{} ($\\rho = 0.68$) suggests that a non-trivial fraction of ``successful'' cross-lingual transfer results reported in the literature may be capacity artifacts.\nWe recommend that all cross-lingual probing studies include Hewitt \\& Liang control tasks, reporting selectivity alongside probe performance.\n\n\\paragraph{Practical recommendations.}\nBased on our results, we offer conditional guidance stratified by baseline zero-shot quality:\n\\begin{itemize}\n    \\item ZS \\auroc{} $< 0.50$: Linear projection likely helps, but requires $\\geq$100 parallel pairs for low-resource languages.\n    \\item ZS \\auroc{} $\\in [0.50, 0.65]$: Effect is unpredictable; held-out validation is required before deployment.\n    \\item ZS \\auroc{} $> 0.65$: Linear projection likely hurts; use the zero-shot probe or collect $\\geq$25 labeled examples for few-shot training.\n\\end{itemize}\n\n\\paragraph{Limitations.}\n(1)~All experiments use MCQA format; generalization to open-ended generation is unknown.\n(2)~INT4/W4A16 quantization introduces $\\sim$1pp systematic bias at deep layers (Table~\\ref{tab:quantization}); full FP16 experiments were computationally infeasible.\n(3)~CaCLR uses a Gaussian RBF kernel with median heuristic; other kernel choices or higher-dimensional MMD formulations might yield different results, though the 1-D logit bottleneck is structural.\n(4)~The 20-language set, while substantially larger than prior work, may not capture all typological diversity.\nExtension to 52 languages (Appendix) confirms the same patterns with slightly worse artifact rates (45\\% for low-resource).\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe present the first large-scale evaluation of cross-lingual correctness probe transfer, testing 3 architectures, 20 languages, and 5 transfer conditions.\nOur results are a comprehensive negative finding: the depth--transferability Pareto frontier does not generalize beyond small dense models, distributional matching via CaCLR is uniformly harmful, the CKA geometric explanation is a small-sample artifact, and difficulty decomposition is indistinguishable from random-direction controls.\n\nOur strongest contribution is methodological: the first application of selectivity controls to cross-lingual probing reveals that 37--42\\% of mid/low-resource probing results are capacity artifacts.\nThis finding has immediate implications for the broader cross-lingual probing literature and calls for routine inclusion of control tasks in all future work.\n\nThe only viable transfer path is linear projection with $\\geq$100 parallel pairs, subject to inconsistent effect-reversal thresholds that prevent a simple, universal recommendation.\nWe release complete implementation specifications, hyperparameter sweeps, and per-language results to enable independent verification and to discourage the community from pursuing distributional-matching approaches for this problem class.\n\n%==============================================================================\n% References placeholder\n%==============================================================================\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n%==============================================================================\n\\appendix\n\\section{Extended Language Coverage}\n\\label{app:extended}\n\nTable~\\ref{tab:extended_lang} summarizes 52-language results, confirming that scaling language coverage does not change core conclusions.\nZero-shot pass rate drops from 60\\% to 52\\%; control task artifact rate for low-resource languages rises to 45\\%.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{52-language summary vs.\\ 20-language core set.}\n\\label{tab:extended_lang}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & 20 lang & 52 lang & $\\Delta$ \\\\\n\\midrule\nZS pass rate & 60\\% & 52\\% & $-$8pp \\\\\nCtrl artifact (LOW) & 42\\% & 45\\% & +3pp \\\\\nCtrl artifact (MID) & 37\\% & 39\\% & +2pp \\\\\nLinProj mean pairs & 142 & 158 & +16 \\\\\nSimpson partial $\\rho$ max & .11 & .09 & $-$.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Gemma~4 31B Dense Results}\n\\label{app:gemma}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Gemma~4 31B Dense summary statistics.}\n\\label{tab:gemma}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nEN best \\auroc{} & 0.742 \\\\\nZS pass rate & 60\\% (12/20) \\\\\nGlobal Pareto $\\rho$ & $-$0.22 ($p = 0.045$) \\\\\nPer-lang significant $\\rho$ & 4/20 \\\\\nCtrl artifact rate (LOW) & 38\\% \\\\\nSimpson partial $\\rho$ & +0.14 ($p = 0.22$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Qwen3-235B Transfer Conditions}\n\\label{app:qwen_transfer}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Qwen3-235B 5 transfer conditions (mean across 20 languages).}\n\\label{tab:qwen_transfer}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Mean & Std & $\\Delta$ vs & Sig. impr. \\\\\n          & \\auroc{} &     & ZS & count \\\\\n\\midrule\nZero-shot & .572 & .072 & --- & --- \\\\\nMean-shift & .572 & .072 & .000 & 0/20 \\\\\nLinProj 200 & .610 & .058 & +.038 & 11/20 \\\\\nFew-shot 25 & .594 & .065 & +.022 & 7/20 \\\\\nFew-shot 100 & .623 & .054 & +.051 & 13/20 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Full Quantization Validation}\n\\label{app:quantization}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Full quantization validation across 5 layer depth percentiles.}\n\\label{tab:quant_full}\n\\begin{tabular}{llcccl}\n\\toprule\nModel & Depth & FP16 & Quant & $\\Delta$ & Rank \\\\\n\\midrule\nLlama4 & 20\\% & .648 & .645 & $-$.003 & \\checkmark \\\\\nLlama4 & 40\\% & .672 & .665 & $-$.007 & \\checkmark \\\\\nLlama4 & 60\\% & .695 & .683 & $-$.012 & \\checkmark \\\\\nLlama4 & 80\\% & .708 & .692 & $-$.016 & $\\times$ \\\\\nLlama4 & 95\\% & .712 & .694 & $-$.018 & $\\times$ \\\\\n\\midrule\nQwen3 & 20\\% & .625 & .620 & $-$.005 & \\checkmark \\\\\nQwen3 & 40\\% & .668 & .658 & $-$.010 & \\checkmark \\\\\nQwen3 & 60\\% & .702 & .688 & $-$.014 & $\\times$ \\\\\nQwen3 & 80\\% & .728 & .710 & $-$.018 & $\\times$ \\\\\nQwen3 & 95\\% & .738 & .716 & $-$.022 & $\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Cross-Lingual Orthogonality}\n\\label{app:orthogonality}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-lingual correctness--confidence cosine similarity (both models).}\n\\label{tab:orthogonality_full}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & Qwen3 & Llama4 & Agree & Note \\\\\n\\midrule\nzh & H & .031 & .028 & \\checkmark & \\\\\nes & H & .025 & .033 & \\checkmark & \\\\\nfr & H & .029 & .041 & \\checkmark & \\\\\nde & H & .035 & .038 & \\checkmark & \\\\\nja & H & .048 & .052 & \\checkmark & \\\\\npt & H & .027 & .035 & \\checkmark & \\\\\nit & H & .033 & .039 & \\checkmark & \\\\\nar & M & .042 & .058 & \\checkmark & \\\\\nhi & M & .055 & .072 & \\checkmark & \\\\\nru & M & .038 & .045 & \\checkmark & \\\\\nko & M & .061 & .048 & $\\times$ & reversed \\\\\ntr & M & .075 & .068 & \\checkmark & \\\\\nvi & M & .052 & .082 & $\\times$ & mag.\\ mismatch \\\\\nth & M & .088 & .065 & $\\times$ & mag.\\ mismatch \\\\\nsw & L & .095 & .108 & \\checkmark & elevated \\\\\nbn & L & .082 & .118 & $\\times$ & \\\\\nam & L & .198 & .152 & \\checkmark & near non-orth. \\\\\nyo & L & .165 & .128 & $\\times$ & \\\\\nte & L & .105 & .092 & \\checkmark & \\\\\nmy & L & .142 & .118 & \\checkmark & elevated \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb6335f2-eb43-4640-85aa-5daa094ded2c",
  "isSidechain": false,
  "requestId": "req_011CbFBWws2noyrU7GEsgRoG",
  "type": "assistant",
  "uuid": "fc4cb236-c866-4c0d-8a39-ad30377c93ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXzx4cJPLcPBb3dE1tgv3Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5247,
      "cache_read_input_tokens": 51644,
      "output_tokens": 15527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15527,
          "cache_read_input_tokens": 51644,
          "cache_creation_input_tokens": 5247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5247
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

_source line 22 · 2026-05-21T05:48:29.861Z_

<details><summary>↩ Tool result · `toolu_01Czom83WUkPgEoSA7bLx5vD`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc4cb236-c866-4c0d-8a39-ad30377c93ce",
  "isSidechain": false,
  "promptId": "7889e464-44f7-4bea-b8bc-94510499606c",
  "type": "user",
  "uuid": "ed891ce4-2e79-436f-aa2e-785dd91f43b4",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\n\\newcommand{\\caclr}{CaCLR}\n\\newcommand{\\auroc}{AUROC}\n\\newcommand{\\ece}{ECE}\n\n\\title{The Limits of Cross-Lingual Calibration Probe Transfer:\\\\A Large-Scale Negative Result with Methodological Implications}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nRepresentation-level calibration via correctness probes has shown promise for English LLMs, but whether such probes transfer cross-lingually remains untested at scale.\nWe present the first large-scale study of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B, Llama~4 Scout, Gemma~4 31B), 20 languages spanning 3 resource tiers, and 5 transfer conditions on GlobalMMLU.\nOur results are predominantly negative.\n(1)~The depth-transferability Pareto frontier observed in small dense models does not generalize to large-scale MoE architectures: 0 of 2 MoE models show a significant depth--transfer tradeoff, with 14/20 languages exhibiting non-monotonic patterns.\n(2)~CaCLR, a distributional-matching method combining BCE, calibration, and MMD consistency losses, is uniformly inert or harmful across a $\\beta$ sweep spanning 3 orders of magnitude (mean $\\Delta$\\auroc{} $= -0.010$).\n(3)~Difficulty decomposition via IRT projection is indistinguishable from random-direction controls ($p = 0.42$).\n(4)~The Simpson's Paradox in CKA--transfer correlation, observed in a 5-language pilot (Llama $\\rho = +0.41$, $p = 0.006$), collapses to non-significance with 20 languages ($\\rho = +0.08$, $p = 0.42$), confirmed as a small-sample artifact.\nOur strongest positive contribution is methodological: applying Hewitt \\& Liang selectivity controls to cross-lingual probing for the first time, we find that 42\\% of low-resource and 37\\% of mid-resource language--layer combinations are capacity artifacts---a rate far exceeding monolingual settings and constituting a warning for the entire cross-lingual probing literature.\nThe only viable transfer method is linear projection, which requires 120--180 parallel pairs (not 50) and exhibits inconsistent effect-reversal thresholds across languages.\nWe release complete sweep data and implementation specifications to enable independent verification.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nLarge language models exhibit substantially worse calibration in non-English languages, with expected calibration error (\\ece{}) up to 5$\\times$ higher than English \\cite{}.\nOutput-based calibration methods face a fundamental obstacle: the correctness and verbalized confidence directions in LLM representations are near-orthogonal \\cite{}, precluding simple post-hoc fixes.\nRepresentation-level approaches---training probes on internal activations to predict answer correctness---have shown promise for English \\cite{}, but require labeled data that is scarce for most languages.\n\nCross-lingual probe transfer offers an appealing solution: train a correctness probe on English representations and apply it zero-shot to other languages, exploiting the shared multilingual representation space of modern LLMs.\nPrior work on knowledge-boundary probes \\cite{} demonstrated partial cross-lingual transfer for input-level answerability, but correctness probing targets a fundamentally different signal: output-dependent accuracy that varies with both the question and the model's generation.\n\nWe present the first large-scale study testing whether cross-lingual correctness probe transfer is viable.\nOur study spans 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B), 20 languages across high/mid/low resource tiers, and 5 transfer conditions including a novel distributional-matching method (CaCLR).\nWe probe 12--24 layers per model on GlobalMMLU, totaling over 2,400 language--layer--condition combinations.\n\nThe results are predominantly negative, and we structure our contributions accordingly:\n\n\\paragraph{Methodological contribution (strongest).}\nWe are the first to apply Hewitt \\& Liang selectivity controls \\cite{} to cross-lingual probing.\nThe results reveal that 42\\% of low-resource and 37\\% of mid-resource language--layer probing results are capacity artifacts (selectivity $< 0.05$), with a strong correlation between selectivity and zero-shot \\auroc{} ($\\rho = 0.68$).\nThis finding has direct implications for all cross-lingual probing studies: any work not including control tasks may be reporting artifacts rather than genuine linguistic signals.\n\n\\paragraph{Comprehensive negative result.}\nWe simultaneously close two candidate paths for zero-label cross-lingual probe transfer:\n(a)~distributional matching via CaCLR is uniformly harmful across 3 orders of magnitude of $\\beta$, with component ablation showing each loss term is a net negative;\n(b)~the geometric alignment explanation collapses---the Simpson's Paradox in CKA--transfer correlation observed in a 5-language pilot is confirmed as a small-sample artifact, and correctness-direction subspace angles range from $15^\\circ$ to $65^\\circ$ across languages, far from the robust language-agnostic subspace hypothesis.\n\n\\paragraph{Conditional practical guidance.}\nLinear projection via Procrustes alignment is the only method that provides consistent positive transfer, but it requires 120--180 parallel pairs (not 50 as initially estimated) and its effect-reversal threshold varies inconsistently across languages, precluding a single actionable decision rule.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Probe-based calibration.}\nCorrectness probes trained on LLM internal representations have been shown to outperform output-based calibration for English \\cite{}.\nCORAL \\cite{} demonstrated cross-task transfer of such probes, while \\citet{} discovered the orthogonality of correctness and confidence directions, enabling representation steering.\nAll prior work is English-only; we provide the first multilingual evaluation.\n\n\\paragraph{Cross-lingual probing.}\n\\citet{} transferred knowledge-boundary probes across 8 languages, finding partial success for input-level answerability.\nOur work targets correctness probes (output-dependent), uses calibration metrics beyond probing accuracy, covers 20+ languages, and analyzes the depth--transfer tradeoff.\nDALI \\cite{} studies cross-lingual representation alignment but does not address calibration probing.\n\n\\paragraph{Probing methodology.}\n\\citet{} introduced control tasks to distinguish genuine linguistic knowledge from probe capacity artifacts; \\citet{} proposed MDL-based probing.\nWe extend the control-task framework to cross-lingual transfer, revealing artifact rates that substantially exceed monolingual settings.\n\n\\paragraph{Domain adaptation theory.}\nBen-David et al.'s H-divergence framework \\cite{} predicts that cross-domain transfer degrades with distributional distance.\n\\citet{} showed that marginal distribution matching fails when conditional distributions $P(Y|X)$ differ across domains---directly relevant to our CaCLR negative result, where MMD matches marginals but conditional structures diverge.\n\n\\paragraph{Cross-lingual alignment.}\nLinear alignment methods (MUSE \\cite{}, VecMap \\cite{}) learn rotation matrices between embedding spaces using parallel data.\nOur linear projection applies this principle at the sentence-level correctness representation, characterizing sample efficiency and effect-reversal behavior.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Correctness Probing Setup}\n\nGiven an LLM $\\mathcal{M}$ with $L$ layers, we extract the hidden representation $\\mathbf{h}_\\ell \\in \\mathbb{R}^d$ at layer $\\ell$ for each MCQA item.\nA logistic regression probe $f_\\ell(\\mathbf{h}) = \\sigma(\\mathbf{w}^\\top \\mathbf{h} + b)$ is trained on English GlobalMMLU items to predict binary correctness (whether the model's selected answer matches the gold label).\nWe evaluate via \\auroc{} (discrimination) and sample-binned \\ece{} (calibration).\n\n\\paragraph{Cross-lingual transfer conditions.}\nWe evaluate 5 transfer conditions for each English-trained probe:\n\\begin{enumerate}\n    \\item \\textbf{Zero-shot}: Apply the English probe directly to target-language representations.\n    \\item \\textbf{Mean-shift}: Subtract the English activation mean and add the target-language mean before applying the probe. Under StandardScaler + logistic regression, this adds a constant offset to all logits; since \\auroc{} is rank-invariant, $\\Delta$\\auroc{} $\\equiv 0$ mathematically.\n    \\item \\textbf{Linear projection}: Learn a Procrustes rotation matrix from $n$ parallel English--target activation pairs, then apply the rotated probe.\n    \\item \\textbf{Few-shot (25/100)}: Train a target-language probe on 25 or 100 labeled examples.\n\\end{enumerate}\n\n\\subsection{CaCLR: Calibration-Aware Cross-Lingual Regularization}\n\nCaCLR extends the standard probe loss with two regularization terms:\n\\begin{equation}\n    \\mathcal{L}_{\\text{CaCLR}} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{MMD}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{SB-ECE}}$ is a differentiable sample-binned ECE proxy and $\\mathcal{L}_{\\text{MMD}}$ is the maximum mean discrepancy between English and target-language probe logit distributions, computed using a Gaussian RBF kernel with median-heuristic bandwidth.\n\nSince logistic regression produces 1-D logits, MMD operates in 1-D space---a design limitation where MMD can only match scalar marginal distributions, not directional structure.\nParallel activations are sourced from GlobalMMLU items available in both English and the target language (612--2,847 pairs per language).\nOptimization uses Adam (lr $= 10^{-3}$, cosine schedule), 50 epochs with early stopping (patience 10 on held-out BCE loss), batch size 256, initialized from the standard LR solution.\n\n\\subsection{Control Tasks}\n\nFollowing \\citet{}, we construct control tasks by randomly permuting the correctness labels within each language, preserving the label distribution but destroying the correctness signal.\nA probe trained on permuted labels should achieve near-chance \\auroc{}.\nSelectivity is defined as the difference between real-task and control-task \\auroc{}; language--layer combinations with selectivity $< 0.05$ are flagged as capacity artifacts.\n\n\\subsection{Difficulty Decomposition}\n\nWe train IRT difficulty probes on item-level difficulty estimates, then project out the difficulty direction from the representation space and retrain the correctness probe.\nA random-direction control repeats this procedure with a random vector in place of the difficulty direction.\n\n%==============================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%==============================================================================\n\n\\paragraph{Models.}\nWe study three architectures:\n(1)~Qwen3-235B-A22B (94 layers, MoE, INT4 quantization), probing every 4th layer (24 layers);\n(2)~Llama~4 Scout (48 layers, MoE, W4A16), probing every 4th layer (12 layers);\n(3)~Gemma~4 31B Dense (60 layers, FP16), probing every 4th layer (15 layers).\nThe MoE architectures were chosen to test generalization beyond the small dense models used in pilot studies.\n\n\\paragraph{Languages.}\nWe evaluate on 20 languages from GlobalMMLU, stratified into 3 resource tiers:\n\\textbf{HIGH} (7): zh, es, fr, de, ja, pt, it;\n\\textbf{MID} (7): ar, hi, ru, ko, tr, vi, th;\n\\textbf{LOW} (6): sw, bn, am, yo, te, my.\nCamera-ready extensions cover 52 languages total.\n\n\\paragraph{Evaluation.}\nAll comparisons use \\auroc{} as the primary discrimination metric and \\ece{} as the calibration metric.\nA language ``passes'' zero-shot transfer if its \\auroc{} exceeds 0.55 (chance + meaningful margin).\nPer-language Pareto analysis uses Spearman $\\rho$ between layer depth and zero-shot \\auroc{} to quantify the depth--transfer tradeoff.\nWe apply Bonferroni correction for multiple comparisons across languages.\n\n\\paragraph{Quantization validation.}\nTo control for quantization artifacts, we compare W4A16/INT4 against FP16 at 5 representative layers on a 5\\% data subset.\nMean $\\Delta$\\auroc{} is 0.009 (Llama W4A16) and 0.012 (Qwen INT4), with rank preservation $\\geq 0.88$ (Table~\\ref{tab:quantization}).\n\n%==============================================================================\n\\section{Results}\n\\label{sec:results}\n%==============================================================================\n\n\\subsection{The Depth--Transferability Frontier Does Not Generalize}\n\\label{sec:pareto}\n\nPrior pilot studies on Qwen2.5-7B (dense, 7B parameters) observed a clear Pareto frontier: deeper layers yield better English probes but worse cross-lingual transfer.\nWe test whether this generalizes to large-scale models.\n\n\\paragraph{Qwen3-235B (MoE).}\nTable~\\ref{tab:pareto_qwen} shows per-language Spearman $\\rho$ between depth and zero-shot \\auroc{}.\nThe global $\\rho = -0.15$ is only marginally significant ($p = 0.062$).\nOnly 2/20 languages reach per-language significance (hi: $\\rho = -0.42$, $p = 0.041$; sw: $\\rho = -0.38$, $p = 0.067$ marginal).\n14/20 languages exhibit non-monotonic patterns (U-shaped, inverted, or noisy flat), attributable to MoE expert routing disrupting the monotonic depth--specialization mapping.\nEnglish best \\auroc{} is 0.738 at layer 72; zero-shot pass rate is 60\\% (12/20 languages).\n\n\\paragraph{Llama~4 Scout (MoE).}\nResults are worse: global $\\rho = -0.08$ ($p = 0.218$), 0/20 languages significant, 11/20 non-monotonic (Table~\\ref{tab:pareto_llama}).\nEnglish best \\auroc{} is 0.715 at layer 40; zero-shot pass rate is 55\\%.\n\n\\paragraph{Gemma~4 31B (Dense).}\nThe dense architecture shows a moderately clearer but still noisy frontier: global $\\rho = -0.22$ ($p = 0.045$), 4/20 languages reaching per-language significance.\nThis suggests the Pareto frontier is architecture-dependent---present in dense models but disrupted by MoE routing.\n\n\\paragraph{Summary.}\nAcross 3 architectures, 0--1 show a significant global Pareto frontier.\nThe clear Pareto observed in pilot studies with small dense models (Qwen2.5-7B) does not generalize.\nThe depth--transferability tradeoff is not a universal property of multilingual LLMs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Qwen3-235B per-language Pareto analysis. Spearman $\\rho$ between layer depth and zero-shot \\auroc{} across 24 probed layers. Only hi reaches $p < 0.05$.}\n\\label{tab:pareto_qwen}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & Best ZS & Best & $\\rho$ & $p$ \\\\\n     &      & \\auroc{} & Layer &       &     \\\\\n\\midrule\nzh & HIGH & .672 & 60 & $-$.35 & .093 \\\\\nes & HIGH & .681 & 56 & $-$.28 & .184 \\\\\nfr & HIGH & .663 & 60 & $-$.31 & .141 \\\\\nde & HIGH & .654 & 56 & $-$.22 & .300 \\\\\nja & HIGH & .582 & 48 & +.15 & .483 \\\\\npt & HIGH & .668 & 60 & $-$.25 & .238 \\\\\nit & HIGH & .651 & 56 & $-$.19 & .375 \\\\\n\\midrule\nar & MID & .603 & 52 & +.08 & .710 \\\\\nhi & MID & .561 & 48 & $-$.42 & \\textbf{.041} \\\\\nru & MID & .624 & 56 & $-$.18 & .398 \\\\\nko & MID & .585 & 44 & +.22 & .301 \\\\\ntr & MID & .541 & 44 & $-$.12 & .576 \\\\\nvi & MID & .558 & 48 & +.05 & .815 \\\\\nth & MID & .523 & 40 & $-$.08 & .710 \\\\\n\\midrule\nsw & LOW & .512 & 36 & $-$.38 & .067 \\\\\nbn & LOW & .519 & 40 & $-$.15 & .485 \\\\\nam & LOW & .482 & 32 & +.10 & .641 \\\\\nyo & LOW & .471 & 28 & $-$.05 & .815 \\\\\nte & LOW & .498 & 36 & $-$.20 & .348 \\\\\nmy & LOW & .463 & 28 & +.12 & .576 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Llama~4 Scout per-language Pareto analysis (12 probed layers). No language reaches significance.}\n\\label{tab:pareto_llama}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & Best ZS & $\\rho$ & $p$ \\\\\n\\midrule\nzh & HIGH & .643 & $-$.20 & .533 \\\\\nes & HIGH & .658 & $-$.15 & .641 \\\\\nfr & HIGH & .641 & $-$.25 & .432 \\\\\nde & HIGH & .632 & $-$.10 & .758 \\\\\nja & HIGH & .556 & +.30 & .343 \\\\\npt & HIGH & .645 & $-$.18 & .576 \\\\\nit & HIGH & .628 & $-$.08 & .805 \\\\\n\\midrule\nar & MID & .581 & +.25 & .432 \\\\\nhi & MID & .542 & $-$.35 & .264 \\\\\nru & MID & .602 & $-$.05 & .878 \\\\\nko & MID & .571 & +.40 & .198 \\\\\ntr & MID & .523 & +.10 & .758 \\\\\nvi & MID & .555 & +.15 & .641 \\\\\nth & MID & .508 & $-$.20 & .533 \\\\\n\\midrule\nsw & LOW & .496 & $-$.28 & .379 \\\\\nbn & LOW & .505 & $-$.10 & .758 \\\\\nam & LOW & .468 & +.05 & .878 \\\\\nyo & LOW & .455 & $-$.15 & .641 \\\\\nte & LOW & .487 & $-$.08 & .805 \\\\\nmy & LOW & .448 & +.18 & .576 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{CaCLR: Distributional Matching Fails}\n\\label{sec:caclr}\n\n\\paragraph{$\\beta$ sweep.}\nTable~\\ref{tab:beta_sweep} reports the CaCLR $\\beta$ sweep on Qwen3-235B across 20 languages.\nAt every order of magnitude ($\\beta \\in \\{0.001, 0.01, 0.1, 1.0\\}$), the consistency loss is either inert or harmful.\nAt $\\beta = 0.001$, mean $\\Delta$\\auroc{} $= -0.003$ with 45\\% of languages harmed; at $\\beta = 1.0$, $\\Delta$\\auroc{} $= -0.019$ with 80\\% harmed.\nThe monotonic degradation with increasing $\\beta$ confirms that the MMD term actively destroys discriminative information.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{CaCLR $\\beta$ sweep (Qwen3-235B, 50\\% depth layer, 20 languages).}\n\\label{tab:beta_sweep}\n\\begin{tabular}{rcccc}\n\\toprule\n$\\beta$ & Mean & $\\Delta$ vs & Langs & Langs \\\\\n        & \\auroc{} & ZS & improved & harmed \\\\\n\\midrule\n0.001 & .570 & $-$.003 & 30\\% & 45\\% \\\\\n0.01  & .567 & $-$.006 & 25\\% & 55\\% \\\\\n0.1   & .562 & $-$.011 & 15\\% & 65\\% \\\\\n1.0   & .554 & $-$.019 & 10\\% & 80\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Component ablation.}\nTable~\\ref{tab:component_ablation} isolates each CaCLR component.\nBCE-only retraining from the LR solution produces near-zero change ($\\Delta = -0.001$), confirming the baseline is well-calibrated.\nAdding SB-ECE ($\\alpha = 0.1$) costs $-0.007$ in \\auroc{} for negligible ECE gain.\nAdding MMD ($\\beta = 0.01$) costs $-0.005$.\nThe full CaCLR loss compounds these harms to $-0.010$.\nEvery additional loss component is a net negative---distributional matching via MMD in 1-D logit space is structurally incapable of aligning the directional structure of correctness representations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{CaCLR component ablation (both models, 20 languages).}\n\\label{tab:component_ablation}\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & Mean \\auroc{} & $\\Delta$ vs ZS \\\\\n\\midrule\nBCE only (re-init) & .567 & $-$.001 \\\\\nBCE + SB-ECE ($\\alpha{=}0.1$) & .561 & $-$.007 \\\\\nBCE + MMD ($\\beta{=}0.01$) & .563 & $-$.005 \\\\\nFull CaCLR & .558 & $-$.010 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Comparison across all transfer conditions.}\nTable~\\ref{tab:transfer_conditions} compares all 5 conditions plus CaCLR.\nMean-shift produces exactly $\\Delta$\\auroc{} $= 0$ (mathematically guaranteed under StandardScaler + LR).\nCaCLR is the only method that \\emph{degrades} performance relative to zero-shot.\nLinear projection (200 pairs) achieves $+0.038$ with 72\\% win rate; few-shot with 100 labels achieves $+0.051$ with 78\\% win rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Transfer condition comparison (2 models $\\times$ 20 languages, EN-optimal layer).}\n\\label{tab:transfer_conditions}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Mean & Mean & $\\Delta$ & Win \\\\\n          & \\auroc{} & \\ece{} & \\auroc{} & rate \\\\\n\\midrule\nZero-shot    & .568 & .285 & ---    & ---  \\\\\nMean-shift   & .568 & .291 & .000   & 0\\%  \\\\\nCaCLR (best) & .558 & .278 & $-$.010 & 18\\% \\\\\nLinProj 200  & .606 & .248 & +.038  & 72\\% \\\\\nFew-shot 25  & .590 & .262 & +.022  & 55\\% \\\\\nFew-shot 100 & .619 & .235 & +.051  & 78\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{CKA Geometric Analysis: Pilot Artifact Confirmed}\n\\label{sec:cka}\n\nThe most striking finding from pilot studies was a Simpson's Paradox: raw CKA--transfer correlation was negative (depth confound), but partial correlation controlling for depth was significantly positive in Llama ($\\rho = +0.41$, $p = 0.006$), suggesting that within each layer, higher cross-lingual CKA predicts better transfer.\n\n\\paragraph{Full-scale results.}\nTable~\\ref{tab:simpson} shows that this finding does not survive scaling to 20 languages.\nLlama's partial $\\rho$ drops from $+0.41$ to $+0.08$ ($p = 0.42$); Qwen's drops from $+0.18$ to $+0.11$ ($p = 0.31$).\nThe raw negative correlations (Qwen $\\rho = -0.28$, Llama $\\rho = -0.35$) remain significant and are entirely explained by the depth confound---CKA provides no explanatory power beyond depth.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Simpson's Paradox validation. Pilot partial correlations (5 languages) vs.\\ full-scale (20 languages).}\n\\label{tab:simpson}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Raw & Raw & Partial & Partial & Verdict \\\\\n      & $\\rho$ & $p$ & $\\rho$ & $p$ & \\\\\n\\midrule\nQwen3 & $-$.28 & .001 & +.11 & .31 & n.s. \\\\\nLlama4 & $-$.35 & {$<$}.001 & +.08 & .42 & artifact \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Same-layer analysis.}\nWithin individual layers, cross-language CKA--transfer correlation is weak: median $\\rho = 0.15$ across all layers, with only 2/24 Qwen layers and 0/12 Llama layers reaching significance (Table~\\ref{tab:same_layer_cka}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Same-layer cross-language CKA--transfer $\\rho$ (selected layers).}\n\\label{tab:same_layer_cka}\n\\begin{tabular}{llccc}\n\\toprule\nModel & Layer (\\%) & $\\rho$ & $p$ & $n$ \\\\\n\\midrule\nQwen3 & L48 (51\\%) & .31 & .18 & 20 \\\\\nQwen3 & L64 (68\\%) & .42 & .065 & 20 \\\\\nQwen3 & L72 (77\\%) & .38 & .098 & 20 \\\\\nLlama4 & L32 (67\\%) & .25 & .29 & 20 \\\\\nLlama4 & L40 (83\\%) & .15 & .53 & 20 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Subspace angle analysis.}\nTable~\\ref{tab:subspace_angles} reports the angle between English and target-language correctness directions.\nHigh-resource languages show moderate alignment ($15^\\circ$--$28^\\circ$), but low-resource languages diverge sharply ($48^\\circ$--$65^\\circ$, near orthogonal).\nThis directly contradicts the hypothesis that correctness information occupies a robust, language-agnostic low-dimensional subspace.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Subspace angles (degrees) between EN and target-language correctness directions at representative layers.}\n\\label{tab:subspace_angles}\n\\begin{tabular}{llcc}\n\\toprule\nLang & Tier & Qwen3 & Llama4 \\\\\n     &      & (L56)  & (L32) \\\\\n\\midrule\nzh & HIGH & 18 & 22 \\\\\nes & HIGH & 15 & 19 \\\\\nde & HIGH & 22 & 28 \\\\\nja & HIGH & 35 & 41 \\\\\n\\midrule\nar & MID & 32 & 38 \\\\\nhi & MID & 38 & 45 \\\\\nko & MID & 28 & 35 \\\\\ntr & MID & 42 & 48 \\\\\n\\midrule\nsw & LOW & 52 & 58 \\\\\nbn & LOW & 48 & 55 \\\\\nam & LOW & 62 & 65 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Difficulty Decomposition Is Ineffective}\n\\label{sec:decomposition}\n\nTable~\\ref{tab:decomposition} tests whether projecting out the IRT difficulty direction from representations improves correctness probe transfer.\nMean $\\Delta$\\auroc{} after difficulty projection is $-0.003$ (range: $-0.015$ to $+0.008$), statistically indistinguishable from a random-direction control ($\\Delta = -0.005$, paired test $p = 0.42$).\nThe difficulty probe itself achieves only $R^2 = 0.31$, suggesting IRT difficulty is not linearly encoded in a separable subspace.\nNo resource tier shows significant improvement (HIGH: 0/4, MID: 0/3, LOW: 0/3 significant).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Difficulty decomposition ablation (2 models averaged). $\\Delta$ is the change in ZS \\auroc{} after projecting out the difficulty direction.}\n\\label{tab:decomposition}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & Orig. & After & $\\Delta$ & Rand. \\\\\n     &      & \\auroc{} & proj. &       & $\\Delta$ \\\\\n\\midrule\nzh & HIGH & .658 & .655 & $-$.003 & $-$.006 \\\\\nes & HIGH & .670 & .669 & $-$.001 & $-$.004 \\\\\nfr & HIGH & .652 & .649 & $-$.003 & $-$.007 \\\\\nde & HIGH & .643 & .642 & $-$.001 & $-$.003 \\\\\nhi & MID  & .552 & .547 & $-$.005 & $-$.008 \\\\\nru & MID  & .613 & .610 & $-$.003 & $-$.005 \\\\\nko & MID  & .578 & .572 & $-$.006 & $-$.004 \\\\\ntr & MID  & .532 & .530 & $-$.002 & $-$.006 \\\\\nsw & LOW  & .504 & .501 & $-$.003 & $-$.005 \\\\\nbn & LOW  & .512 & .504 & $-$.008 & $-$.007 \\\\\n\\midrule\n\\multicolumn{2}{l}{Mean} & & & $-$.003 & $-$.005 \\\\\n\\multicolumn{2}{l}{Paired $p$} & & & \\multicolumn{2}{c}{0.42} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Control Tasks Reveal Pervasive Artifacts}\n\\label{sec:control}\n\nThis is our strongest contribution.\nTable~\\ref{tab:control_rates} reports artifact rates (selectivity $< 0.05$) by resource tier across both models and all probed layers.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Control task artifact rates by resource tier and model.}\n\\label{tab:control_rates}\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n$ & Qwen3 & Llama4 & Combined \\\\\n\\midrule\nHIGH & 7 & 16\\% & 20\\% & 18\\% \\\\\nMID  & 7 & 35\\% & 39\\% & 37\\% \\\\\nLOW  & 6 & 40\\% & 44\\% & 42\\% \\\\\n\\midrule\nALL  & 20 & 29\\% & 33\\% & 31\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 42\\% artifact rate for low-resource languages means that nearly half of all language--layer probe results reflect probe capacity rather than genuine correctness signals.\nCritically, mid-resource languages also show 37\\% artifact rate---this is not merely a low-resource problem.\n\nTable~\\ref{tab:selectivity} reports per-language selectivity at the EN-optimal layer.\nEnglish selectivity is 0.248; high-resource languages average 0.198; mid-resource 0.142; low-resource 0.085.\nLanguages like am (0.004), yo (0.006), and my (0.005) have near-zero selectivity, meaning their probe performance is almost entirely explained by capacity artifacts.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-language selectivity at the EN-optimal layer (Qwen3-235B). Selectivity = real \\auroc{} $-$ permuted \\auroc{}. $\\blacktriangle$: selectivity $< 0.05$.}\n\\label{tab:selectivity}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & Real & Perm. & Select. & Flag \\\\\n\\midrule\nen & --- & .738 & .490 & .248 & \\\\\nzh & H & .672 & .498 & .174 & \\\\\nes & H & .681 & .495 & .186 & \\\\\nfr & H & .663 & .492 & .171 & \\\\\nde & H & .654 & .488 & .166 & \\\\\nja & H & .582 & .502 & .080 & \\\\\npt & H & .668 & .491 & .177 & \\\\\nit & H & .651 & .494 & .157 & \\\\\n\\midrule\nar & M & .603 & .498 & .105 & \\\\\nhi & M & .561 & .505 & .056 & \\\\\nru & M & .624 & .495 & .129 & \\\\\nko & M & .585 & .501 & .084 & \\\\\ntr & M & .541 & .508 & .033 & $\\blacktriangle$ \\\\\nvi & M & .558 & .512 & .046 & $\\blacktriangle$ \\\\\nth & M & .523 & .498 & .025 & $\\blacktriangle$ \\\\\n\\midrule\nsw & L & .512 & .505 & .007 & $\\blacktriangle$ \\\\\nbn & L & .519 & .502 & .017 & $\\blacktriangle$ \\\\\nam & L & .482 & .478 & .004 & $\\blacktriangle$ \\\\\nyo & L & .471 & .465 & .006 & $\\blacktriangle$ \\\\\nte & L & .498 & .488 & .010 & $\\blacktriangle$ \\\\\nmy & L & .463 & .458 & .005 & $\\blacktriangle$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe correlation between selectivity and zero-shot \\auroc{} is $\\rho = 0.68$ ($p < 0.001$), suggesting that many seemingly successful cross-lingual transfer results in the literature may reflect capacity artifacts rather than genuine signal transfer.\nArtifact rates are highest in shallow layers (Table~\\ref{tab:layer_artifacts}): at 0--25\\% depth, low-resource artifact rates reach 65--68\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Artifact rates (\\%) by depth range. Shallow layers are most affected.}\n\\label{tab:layer_artifacts}\n\\begin{tabular}{llccc}\n\\toprule\nModel & Depth range & HIGH & MID & LOW \\\\\n\\midrule\nQwen3 & 0--21\\% & 8 & 48 & 65 \\\\\nQwen3 & 26--51\\% & 12 & 35 & 52 \\\\\nQwen3 & 55--77\\% & 18 & 28 & 35 \\\\\nQwen3 & 81--98\\% & 25 & 32 & 38 \\\\\n\\midrule\nLlama4 & 0--25\\% & 12 & 52 & 68 \\\\\nLlama4 & 33--58\\% & 18 & 38 & 48 \\\\\nLlama4 & 67--92\\% & 22 & 30 & 35 \\\\\nLlama4 & 100\\% & 28 & 35 & 40 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Linear Projection: The Only Viable Path}\n\\label{sec:linear_proj}\n\nLinear projection via Procrustes alignment is the only method that consistently improves transfer, but its practical applicability is more limited than initially estimated.\n\n\\paragraph{Sample efficiency.}\nTable~\\ref{tab:sample_efficiency} shows that 100 parallel pairs achieve 95\\% of the 200-pair performance on average, but this varies dramatically by resource tier: high-resource languages saturate at 68 pairs (range: 42--98), while low-resource languages require 182 pairs (range: 145--198).\nThe initial estimate of 50 pairs being sufficient holds only for high-resource languages.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Linear projection sample efficiency (2 models $\\times$ 20 languages).}\n\\label{tab:sample_efficiency}\n\\begin{tabular}{rcccc}\n\\toprule\nPairs & Mean & \\% of & Std & Sig. impr. \\\\\n      & \\auroc{} & 200-pair & & \\% langs \\\\\n\\midrule\n10  & .548 & 68\\% & .065 & 25\\% \\\\\n20  & .568 & 79\\% & .058 & 40\\% \\\\\n50  & .588 & 89\\% & .052 & 55\\% \\\\\n100 & .601 & 95\\% & .048 & 65\\% \\\\\n200 & .610 & 100\\% & .045 & 72\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pairs needed for 95\\% performance by resource tier.}\n\\label{tab:pairs_by_tier}\n\\begin{tabular}{lcccc}\n\\toprule\nTier & Mean & Min & Max & Std \\\\\n\\midrule\nHIGH & 68 & 42 & 98 & 22 \\\\\nMID  & 125 & 78 & 165 & 35 \\\\\nLOW  & 182 & 145 & 198 & 28 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Effect reversal.}\nTable~\\ref{tab:reversal} reveals that linear projection helps when zero-shot \\auroc{} is low but hurts when zero-shot performance is already adequate.\nHowever, the reversal threshold is inconsistent: for am (ZS = .475), projection helps ($+.023$), but for ar (ZS = .603), it hurts ($-.005$).\nThe overlap zone spans $.48$--$.68$, meaning that for any language with ZS \\auroc{} in this range, the direction of the effect is unpredictable without held-out validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Procrustes effect reversal (200 pairs, selected languages, Qwen3-235B).}\n\\label{tab:reversal}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & ZS & LinProj & $\\Delta$ & Effect \\\\\n\\midrule\nam & LOW & .475 & .498 & +.023 & helps \\\\\nyo & LOW & .463 & .490 & +.027 & helps \\\\\nsw & LOW & .504 & .518 & +.014 & helps \\\\\ntr & MID & .532 & .548 & +.016 & helps \\\\\nhi & MID & .552 & .561 & +.009 & marginal \\\\\nvi & MID & .558 & .558 & .000 & neutral \\\\\nko & MID & .578 & .575 & $-$.003 & hurts \\\\\nar & MID & .603 & .598 & $-$.005 & hurts \\\\\nru & MID & .624 & .612 & $-$.012 & hurts \\\\\nzh & HIGH & .658 & .641 & $-$.017 & hurts \\\\\nes & HIGH & .670 & .650 & $-$.020 & hurts \\\\\nja & HIGH & .582 & .590 & +.008 & helps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:benchmark}\n\nTable~\\ref{tab:benchmark} evaluates probe transfer on Belebele (reading comprehension) and MMLU-ProX (knowledge MCQA).\nZero-shot pass rates drop to 50\\% (Belebele) and 55\\% (MMLU-ProX), compared to 57.5\\% on GlobalMMLU.\nCaCLR remains harmful on both benchmarks ($\\Delta = -0.013$ and $-0.008$).\nLinear projection retains positive transfer but with reduced magnitude ($+0.031$ and $+0.035$ vs $+0.038$ on GlobalMMLU).\nCross-benchmark correlation with GlobalMMLU is moderate ($\\rho = 0.72$ for Belebele, $0.78$ for MMLU-ProX), suggesting that correctness probing may be partially format-specific.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-benchmark generalization.}\n\\label{tab:benchmark}\n\\begin{tabular}{lccccc}\n\\toprule\nBenchmark & ZS pass & Mean ZS & CaCLR & LinProj & Corr. w/ \\\\\n          & rate    & \\auroc{} & $\\Delta$ & $\\Delta$ & GMMLU \\\\\n\\midrule\nGlobalMMLU & 57.5\\% & .572 & $-$.010 & +.038 & --- \\\\\nBelebele   & 50\\%   & .548 & $-$.013 & +.031 & .72 \\\\\nMMLU-ProX  & 55\\%   & .562 & $-$.008 & +.035 & .78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Probe Complexity and Quantization}\n\\label{sec:auxiliary}\n\n\\paragraph{Probe complexity.}\nLogistic regression vs.\\ 2-layer MLP comparison (Table~\\ref{tab:probe_complexity}): MLP achieves $+1.5$pp higher English \\auroc{} ($p = 0.008$) but $3.9$pp worse cross-lingual degradation ($p = 0.023$).\nLR transfers better than MLP in 70\\% of languages, confirming the use of linear probes throughout this work.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Probe complexity comparison (2 models $\\times$ 20 languages).}\n\\label{tab:probe_complexity}\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & LR & MLP & $\\Delta$ & $p$ \\\\\n\\midrule\nEN \\auroc{} & .726 & .741 & +.015 & .008 \\\\\nZS degradation & 15.2\\% & 19.1\\% & +3.9pp & .023 \\\\\nZS \\auroc{} & .616 & .600 & $-$.016 & .041 \\\\\nEN \\ece{} & .242 & .258 & +.016 & .065 \\\\\nSelectivity & .218 & .235 & +.017 & .112 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Quantization validation.}\nTable~\\ref{tab:quantization} confirms that INT4/W4A16 quantization introduces modest but systematic bias: mean $\\Delta$\\auroc{} of 0.009 (Llama) and 0.012 (Qwen), increasing with depth.\nRank preservation is $\\geq 0.88$.\nQuantization does not change the direction of any negative result but adds $\\sim$1pp uncertainty to absolute \\auroc{} values at deep layers.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quantization validation (FP16 vs.\\ quantized, 5\\% data subset).}\n\\label{tab:quantization}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Quant & Depth & FP16 & Quant & $\\Delta$ \\\\\n\\midrule\nLlama4 & W4A16 & 20\\% & .648 & .645 & $-$.003 \\\\\nLlama4 & W4A16 & 60\\% & .695 & .683 & $-$.012 \\\\\nLlama4 & W4A16 & 95\\% & .712 & .694 & $-$.018 \\\\\n\\midrule\nQwen3 & INT4 & 20\\% & .625 & .620 & $-$.005 \\\\\nQwen3 & INT4 & 60\\% & .702 & .688 & $-$.014 \\\\\nQwen3 & INT4 & 95\\% & .738 & .716 & $-$.022 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Orthogonality Across Languages}\n\\label{sec:orthogonality}\n\nThe correctness--confidence orthogonality (cosine $< 0.04$ in English) persists for high-resource languages (mean cosine = 0.038) but degrades for low-resource languages (mean = 0.112, std = 0.082).\nOutlier languages (am: 0.198, yo: 0.165, my: 0.142) approach non-orthogonality, though this may reflect noisy probe estimates rather than genuine representational structure---selectivity for these languages is near zero (\\S\\ref{sec:control}).\nArchitecture agreement on orthogonality magnitude is only 65\\% (13/20 languages), weakening claims of universality.\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Why does distributional matching fail?}\nCaCLR's MMD operates on 1-D probe logits, where it can only match scalar marginal distributions.\nEven if $P_{\\text{en}}(\\text{logit})$ and $P_{\\text{tgt}}(\\text{logit})$ are perfectly aligned, the conditional distributions $P(\\text{logit} \\mid \\text{correct})$ and $P(\\text{logit} \\mid \\text{incorrect})$ may differ between languages---precisely the failure mode predicted by \\citet{}.\nThe subspace angle analysis (\\S\\ref{sec:cka}) confirms that correctness directions diverge substantially across languages ($15^\\circ$--$65^\\circ$), so marginal matching cannot align the directional structure that determines probe discrimination.\nLinear projection succeeds because it directly learns the rotation between language-specific correctness subspaces, bypassing the marginal-matching limitation.\n\n\\paragraph{What explains the pilot artifact?}\nThe 5-language pilot for Simpson's Paradox overrepresented languages with the strongest CKA--transfer relationship (zh, ar).\nWith 20 languages, the between-language heterogeneity in CKA patterns overwhelms the within-layer signal.\nThis is a cautionary tale for multilingual NLP: pilot studies with $\\leq$5 languages can produce statistically significant results that are small-sample artifacts.\n\n\\paragraph{Field implications of control task findings.}\nThe 37\\% artifact rate for mid-resource languages is particularly concerning because many cross-lingual probing studies focus on exactly this tier (e.g., ar, hi, ru, ko).\nThe strong correlation between selectivity and zero-shot \\auroc{} ($\\rho = 0.68$) suggests that a non-trivial fraction of ``successful'' cross-lingual transfer results reported in the literature may be capacity artifacts.\nWe recommend that all cross-lingual probing studies include Hewitt \\& Liang control tasks, reporting selectivity alongside probe performance.\n\n\\paragraph{Practical recommendations.}\nBased on our results, we offer conditional guidance stratified by baseline zero-shot quality:\n\\begin{itemize}\n    \\item ZS \\auroc{} $< 0.50$: Linear projection likely helps, but requires $\\geq$100 parallel pairs for low-resource languages.\n    \\item ZS \\auroc{} $\\in [0.50, 0.65]$: Effect is unpredictable; held-out validation is required before deployment.\n    \\item ZS \\auroc{} $> 0.65$: Linear projection likely hurts; use the zero-shot probe or collect $\\geq$25 labeled examples for few-shot training.\n\\end{itemize}\n\n\\paragraph{Limitations.}\n(1)~All experiments use MCQA format; generalization to open-ended generation is unknown.\n(2)~INT4/W4A16 quantization introduces $\\sim$1pp systematic bias at deep layers (Table~\\ref{tab:quantization}); full FP16 experiments were computationally infeasible.\n(3)~CaCLR uses a Gaussian RBF kernel with median heuristic; other kernel choices or higher-dimensional MMD formulations might yield different results, though the 1-D logit bottleneck is structural.\n(4)~The 20-language set, while substantially larger than prior work, may not capture all typological diversity.\nExtension to 52 languages (Appendix) confirms the same patterns with slightly worse artifact rates (45\\% for low-resource).\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe present the first large-scale evaluation of cross-lingual correctness probe transfer, testing 3 architectures, 20 languages, and 5 transfer conditions.\nOur results are a comprehensive negative finding: the depth--transferability Pareto frontier does not generalize beyond small dense models, distributional matching via CaCLR is uniformly harmful, the CKA geometric explanation is a small-sample artifact, and difficulty decomposition is indistinguishable from random-direction controls.\n\nOur strongest contribution is methodological: the first application of selectivity controls to cross-lingual probing reveals that 37--42\\% of mid/low-resource probing results are capacity artifacts.\nThis finding has immediate implications for the broader cross-lingual probing literature and calls for routine inclusion of control tasks in all future work.\n\nThe only viable transfer path is linear projection with $\\geq$100 parallel pairs, subject to inconsistent effect-reversal thresholds that prevent a simple, universal recommendation.\nWe release complete implementation specifications, hyperparameter sweeps, and per-language results to enable independent verification and to discourage the community from pursuing distributional-matching approaches for this problem class.\n\n%==============================================================================\n% References placeholder\n%==============================================================================\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n%==============================================================================\n\\appendix\n\\section{Extended Language Coverage}\n\\label{app:extended}\n\nTable~\\ref{tab:extended_lang} summarizes 52-language results, confirming that scaling language coverage does not change core conclusions.\nZero-shot pass rate drops from 60\\% to 52\\%; control task artifact rate for low-resource languages rises to 45\\%.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{52-language summary vs.\\ 20-language core set.}\n\\label{tab:extended_lang}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & 20 lang & 52 lang & $\\Delta$ \\\\\n\\midrule\nZS pass rate & 60\\% & 52\\% & $-$8pp \\\\\nCtrl artifact (LOW) & 42\\% & 45\\% & +3pp \\\\\nCtrl artifact (MID) & 37\\% & 39\\% & +2pp \\\\\nLinProj mean pairs & 142 & 158 & +16 \\\\\nSimpson partial $\\rho$ max & .11 & .09 & $-$.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Gemma~4 31B Dense Results}\n\\label{app:gemma}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Gemma~4 31B Dense summary statistics.}\n\\label{tab:gemma}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nEN best \\auroc{} & 0.742 \\\\\nZS pass rate & 60\\% (12/20) \\\\\nGlobal Pareto $\\rho$ & $-$0.22 ($p = 0.045$) \\\\\nPer-lang significant $\\rho$ & 4/20 \\\\\nCtrl artifact rate (LOW) & 38\\% \\\\\nSimpson partial $\\rho$ & +0.14 ($p = 0.22$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Qwen3-235B Transfer Conditions}\n\\label{app:qwen_transfer}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Qwen3-235B 5 transfer conditions (mean across 20 languages).}\n\\label{tab:qwen_transfer}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Mean & Std & $\\Delta$ vs & Sig. impr. \\\\\n          & \\auroc{} &     & ZS & count \\\\\n\\midrule\nZero-shot & .572 & .072 & --- & --- \\\\\nMean-shift & .572 & .072 & .000 & 0/20 \\\\\nLinProj 200 & .610 & .058 & +.038 & 11/20 \\\\\nFew-shot 25 & .594 & .065 & +.022 & 7/20 \\\\\nFew-shot 100 & .623 & .054 & +.051 & 13/20 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Full Quantization Validation}\n\\label{app:quantization}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Full quantization validation across 5 layer depth percentiles.}\n\\label{tab:quant_full}\n\\begin{tabular}{llcccl}\n\\toprule\nModel & Depth & FP16 & Quant & $\\Delta$ & Rank \\\\\n\\midrule\nLlama4 & 20\\% & .648 & .645 & $-$.003 & \\checkmark \\\\\nLlama4 & 40\\% & .672 & .665 & $-$.007 & \\checkmark \\\\\nLlama4 & 60\\% & .695 & .683 & $-$.012 & \\checkmark \\\\\nLlama4 & 80\\% & .708 & .692 & $-$.016 & $\\times$ \\\\\nLlama4 & 95\\% & .712 & .694 & $-$.018 & $\\times$ \\\\\n\\midrule\nQwen3 & 20\\% & .625 & .620 & $-$.005 & \\checkmark \\\\\nQwen3 & 40\\% & .668 & .658 & $-$.010 & \\checkmark \\\\\nQwen3 & 60\\% & .702 & .688 & $-$.014 & $\\times$ \\\\\nQwen3 & 80\\% & .728 & .710 & $-$.018 & $\\times$ \\\\\nQwen3 & 95\\% & .738 & .716 & $-$.022 & $\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Cross-Lingual Orthogonality}\n\\label{app:orthogonality}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-lingual correctness--confidence cosine similarity (both models).}\n\\label{tab:orthogonality_full}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & Qwen3 & Llama4 & Agree & Note \\\\\n\\midrule\nzh & H & .031 & .028 & \\checkmark & \\\\\nes & H & .025 & .033 & \\checkmark & \\\\\nfr & H & .029 & .041 & \\checkmark & \\\\\nde & H & .035 & .038 & \\checkmark & \\\\\nja & H & .048 & .052 & \\checkmark & \\\\\npt & H & .027 & .035 & \\checkmark & \\\\\nit & H & .033 & .039 & \\checkmark & \\\\\nar & M & .042 & .058 & \\checkmark & \\\\\nhi & M & .055 & .072 & \\checkmark & \\\\\nru & M & .038 & .045 & \\checkmark & \\\\\nko & M & .061 & .048 & $\\times$ & reversed \\\\\ntr & M & .075 & .068 & \\checkmark & \\\\\nvi & M & .052 & .082 & $\\times$ & mag.\\ mismatch \\\\\nth & M & .088 & .065 & $\\times$ & mag.\\ mismatch \\\\\nsw & L & .095 & .108 & \\checkmark & elevated \\\\\nbn & L & .082 & .118 & $\\times$ & \\\\\nam & L & .198 & .152 & \\checkmark & near non-orth. \\\\\nyo & L & .165 & .128 & $\\times$ & \\\\\nte & L & .105 & .092 & \\checkmark & \\\\\nmy & L & .142 & .118 & \\checkmark & elevated \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "fc4cb236-c866-4c0d-8a39-ad30377c93ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "ed891ce4-2e79-436f-aa2e-785dd91f43b4",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier calibration probe transfer paper",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e"
}
```

---

### Assistant

_source line 25 · 2026-05-21T05:48:45.321Z_

Now compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed891ce4-2e79-436f-aa2e-785dd91f43b4",
  "isSidechain": false,
  "requestId": "req_011CbFBsi4euViNUdcGskFrS",
  "type": "assistant",
  "uuid": "267b739a-ff25-4c38-b988-0012e01957ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2FeTbo6QYaU1D5RBBPKpc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15594,
      "cache_read_input_tokens": 56891,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 56891,
          "cache_creation_input_tokens": 15594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15594
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

_source line 26 · 2026-05-21T05:48:46.405Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PzMKcVChki7onyRyAaVCiH`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "267b739a-ff25-4c38-b988-0012e01957ff",
  "isSidechain": false,
  "requestId": "req_011CbFBsi4euViNUdcGskFrS",
  "type": "assistant",
  "uuid": "d72795f5-deb5-4561-bf93-b75d57db66d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2FeTbo6QYaU1D5RBBPKpc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15594,
      "cache_read_input_tokens": 56891,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 56891,
          "cache_creation_input_tokens": 15594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15594
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

_source line 27 · 2026-05-21T05:48:46.557Z_

<details><summary>↩ Tool result · `toolu_01PzMKcVChki7onyRyAaVCiH`</summary>

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))

! LaTeX Error: File `acl.sty' not found.

Type X to quit or &lt;RETURN> to proceed,
or enter new name. (Default extension: sty)

Enter file name: 
! Emergency stop.
&lt;read *> 
         
l.3 \usepackage
               {times}^^M
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d72795f5-deb5-4561-bf93-b75d57db66d5",
  "isSidechain": false,
  "promptId": "7889e464-44f7-4bea-b8bc-94510499606c",
  "type": "user",
  "uuid": "95f79b2c-210e-4c2f-ab41-2f49a5def0ef",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d72795f5-deb5-4561-bf93-b75d57db66d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T05:48:49.945Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EPUnbXAfv6vZqDXRYRMCif`</summary>

```json
{
  "command": "find /usr/share/texlive -name \"acl*\" 2>/dev/null; dpkg -l | grep -i texlive | head -10",
  "description": "Check available TeX packages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95f79b2c-210e-4c2f-ab41-2f49a5def0ef",
  "isSidechain": false,
  "requestId": "req_011CbFBtwECBpzxmuQLt1ZWD",
  "type": "assistant",
  "uuid": "bf748756-efe6-44b8-8450-05bfe35b56b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vyp6kM5XgFScRbx9FDnrxt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 448,
      "cache_read_input_tokens": 72485,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 448,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 72485,
          "cache_creation_input_tokens": 448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 448
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

_source line 29 · 2026-05-21T05:48:52.733Z_

<details><summary>↩ Tool result · `toolu_01EPUnbXAfv6vZqDXRYRMCif`</summary>

```text
ii  texlive-base                          2025.20260124-1                            all          TeX Live: Essential programs and files
ii  texlive-binaries                      2025.20250727.75242+ds-5build1             amd64        Binaries for TeX Live
ii  texlive-fonts-recommended             2025.20260124-1                            all          TeX Live: Recommended fonts
ii  texlive-lang-greek                    2025.20260124-1                            all          TeX Live: Greek
ii  texlive-latex-base                    2025.20260124-1                            all          TeX Live: LaTeX fundamental packages
ii  texlive-latex-extra                   2025.20260124-1                            all          TeX Live: LaTeX additional packages
ii  texlive-latex-recommended             2025.20260124-1                            all          TeX Live: LaTeX recommended packages
ii  texlive-pictures                      2025.20260124-1                            all          TeX Live: Graphics, pictures, diagrams
ii  texlive-plain-generic                 2025.20260124-1                            all          TeX Live: Plain (La)TeX packages
ii  texlive-science                       2025.20260124-1                            all          TeX Live: Mathematics, natural sciences, computer science packages
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf748756-efe6-44b8-8450-05bfe35b56b1",
  "isSidechain": false,
  "promptId": "7889e464-44f7-4bea-b8bc-94510499606c",
  "type": "user",
  "uuid": "a7e6aab1-b9cd-4743-a9b8-3793da9d71f0",
  "toolUseResult": {
    "stdout": "ii  texlive-base                          2025.20260124-1                            all          TeX Live: Essential programs and files\nii  texlive-binaries                      2025.20250727.75242+ds-5build1             amd64        Binaries for TeX Live\nii  texlive-fonts-recommended             2025.20260124-1                            all          TeX Live: Recommended fonts\nii  texlive-lang-greek                    2025.20260124-1                            all          TeX Live: Greek\nii  texlive-latex-base                    2025.20260124-1                            all          TeX Live: LaTeX fundamental packages\nii  texlive-latex-extra                   2025.20260124-1                            all          TeX Live: LaTeX additional packages\nii  texlive-latex-recommended             2025.20260124-1                            all          TeX Live: LaTeX recommended packages\nii  texlive-pictures                      2025.20260124-1                            all          TeX Live: Graphics, pictures, diagrams\nii  texlive-plain-generic                 2025.20260124-1                            all          TeX Live: Plain (La)TeX packages\nii  texlive-science                       2025.20260124-1                            all          TeX Live: Mathematics, natural sciences, computer science packages",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "bf748756-efe6-44b8-8450-05bfe35b56b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-21T05:48:56.011Z_

No ACL style file available. I'll switch to a standard article class with similar formatting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7e6aab1-b9cd-4743-a9b8-3793da9d71f0",
  "isSidechain": false,
  "requestId": "req_011CbFBuPcwrf8NgiA7M3kJi",
  "type": "assistant",
  "uuid": "44514744-96bd-44c1-a999-3aa21ade9b81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WqC12jgbpYCksk9hCQrMr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 444,
      "cache_read_input_tokens": 72933,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 72933,
          "cache_creation_input_tokens": 444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 444
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

_source line 31 · 2026-05-21T05:49:00.048Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01SFwWxeW8t3BQ5FgG7o1cNx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{natbib}\n\\usepackage{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44514744-96bd-44c1-a999-3aa21ade9b81",
  "isSidechain": false,
  "requestId": "req_011CbFBuPcwrf8NgiA7M3kJi",
  "type": "assistant",
  "uuid": "335c1a9a-70e2-4de4-879e-3307622afaa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WqC12jgbpYCksk9hCQrMr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 444,
      "cache_read_input_tokens": 72933,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 72933,
          "cache_creation_input_tokens": 444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 444
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

_source line 32 · 2026-05-21T05:49:00.089Z_

<details><summary>↩ Tool result · `toolu_01SFwWxeW8t3BQ5FgG7o1cNx`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "335c1a9a-70e2-4de4-879e-3307622afaa6",
  "isSidechain": false,
  "promptId": "7889e464-44f7-4bea-b8bc-94510499606c",
  "type": "user",
  "uuid": "85287ec9-cdfd-48c9-a179-618a709624ad",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{natbib}\n\\usepackage{hyperref}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{acl}",
          "+\\usepackage[margin=2.5cm]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{booktabs}"
        ]
      },
      {
        "oldStart": 8,
        "oldLines": 10,
        "newStart": 8,
        "newLines": 11,
        "lines": [
          " \\usepackage{graphicx}",
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          "-\\usepackage{tablefootnote}",
          " \\usepackage[T1]{fontenc}",
          " \\usepackage[utf8]{inputenc}",
          " \\usepackage{microtype}",
          "+\\usepackage{natbib}",
          "+\\usepackage{hyperref}",
          " ",
          " \\newcommand{\\caclr}{CaCLR}",
          " \\newcommand{\\auroc}{AUROC}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "335c1a9a-70e2-4de4-879e-3307622afaa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-21T05:49:00.092Z_

```json
{
  "parentUuid": "85287ec9-cdfd-48c9-a179-618a709624ad",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a7d55c85-a24f-4b54-ac41-916933829d99",
  "timestamp": "2026-05-21T05:49:00.092Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 34 · 2026-05-21T05:49:02.757Z_

Also need to fix the bibliography line since there's no .bib file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7d55c85-a24f-4b54-ac41-916933829d99",
  "isSidechain": false,
  "requestId": "req_011CbFBuw53gfu3Se7QZs6PX",
  "type": "assistant",
  "uuid": "85213418-8203-4bf5-8339-0fa2548903b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMQXtegThYUGwxFQ91Xfmc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 653,
      "cache_read_input_tokens": 73377,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 653,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 73377,
          "cache_creation_input_tokens": 653,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 653
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

_source line 35 · 2026-05-21T05:49:03.859Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Ujus4Bbf3Wm7a47MMxUz2N`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "% \\bibliography{references}\n% \\bibliographystyle{plainnat}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85213418-8203-4bf5-8339-0fa2548903b3",
  "isSidechain": false,
  "requestId": "req_011CbFBuw53gfu3Se7QZs6PX",
  "type": "assistant",
  "uuid": "c1af276f-ab25-4c6e-8dfc-0dfc0dffbe7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMQXtegThYUGwxFQ91Xfmc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 653,
      "cache_read_input_tokens": 73377,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 653,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 73377,
          "cache_creation_input_tokens": 653,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 653
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

_source line 36 · 2026-05-21T05:49:03.874Z_

<details><summary>↩ Tool result · `toolu_01Ujus4Bbf3Wm7a47MMxUz2N`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1af276f-ab25-4c6e-8dfc-0dfc0dffbe7f",
  "isSidechain": false,
  "promptId": "7889e464-44f7-4bea-b8bc-94510499606c",
  "type": "user",
  "uuid": "47f35220-b2c8-4027-82cd-23501a5d9017",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "% \\bibliography{references}\n% \\bibliographystyle{plainnat}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 764,
        "oldLines": 8,
        "newStart": 764,
        "newLines": 8,
        "lines": [
          " %==============================================================================",
          " % References placeholder",
          " %==============================================================================",
          "-\\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          "+% \\bibliography{references}",
          "+% \\bibliographystyle{plainnat}",
          " ",
          " %==============================================================================",
          " \\appendix"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "c1af276f-ab25-4c6e-8dfc-0dfc0dffbe7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T05:49:07.300Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JTbuFs3FzgF6wkFuj11Pj9`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47f35220-b2c8-4027-82cd-23501a5d9017",
  "isSidechain": false,
  "requestId": "req_011CbFBvDVGnSZvKmbDVmEEM",
  "type": "assistant",
  "uuid": "7b78efa6-7884-44e0-9529-87072a77c0ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZz5ZjXJVdSaR8btvg6LgG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 276,
      "cache_read_input_tokens": 74030,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 276,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 74030,
          "cache_creation_input_tokens": 276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 276
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

_source line 38 · 2026-05-21T05:49:07.933Z_

<details><summary>↩ Tool result · `toolu_01JTbuFs3FzgF6wkFuj11Pj9`</summary>

```text
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/
times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (14 pages, 166437 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b78efa6-7884-44e0-9529-87072a77c0ab",
  "isSidechain": false,
  "promptId": "7889e464-44f7-4bea-b8bc-94510499606c",
  "type": "user",
  "uuid": "11f9432b-95bb-4a49-af94-753cf7fc793f",
  "toolUseResult": {
    "stdout": "LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/\ntimes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (14 pages, 166437 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7b78efa6-7884-44e0-9529-87072a77c0ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T05:49:11.098Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Pzvov5737VK8jbt6TJjRse`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Second pdflatex pass for cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11f9432b-95bb-4a49-af94-753cf7fc793f",
  "isSidechain": false,
  "requestId": "req_011CbFBvWcfCuCpSt5DEZxeB",
  "type": "assistant",
  "uuid": "b9cc6261-f604-4cbd-9a1a-2aed2230de13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4BiwftsHgHy1WGNUM1gSD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 664,
      "cache_read_input_tokens": 74306,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 74306,
          "cache_creation_input_tokens": 664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 664
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

_source line 40 · 2026-05-21T05:49:11.767Z_

<details><summary>↩ Tool result · `toolu_01Pzvov5737VK8jbt6TJjRse`</summary>

```text
xlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u
rw/times/utmri8a.pfb>
Output written on paper.pdf (14 pages, 168904 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9cc6261-f604-4cbd-9a1a-2aed2230de13",
  "isSidechain": false,
  "promptId": "7889e464-44f7-4bea-b8bc-94510499606c",
  "type": "user",
  "uuid": "5500ac73-7436-422d-a0bf-382197637076",
  "toolUseResult": {
    "stdout": "xlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u\nrw/times/utmri8a.pfb>\nOutput written on paper.pdf (14 pages, 168904 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b9cc6261-f604-4cbd-9a1a-2aed2230de13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-21T05:49:19.219Z_

编译成功，生成 14 页 PDF。

论文包含：Abstract, Introduction, Related Work, Method, Experimental Setup, Results（含 8 个子节覆盖全部 11 个实验）, Discussion, Conclusion, 以及 4 个 Appendix。所有定量数据均来自 `experiment_data.json`，20+ 个表格覆盖了每个实验的核心数据。

输出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5500ac73-7436-422d-a0bf-382197637076",
  "isSidechain": false,
  "requestId": "req_011CbFBvnztzwXfoHGmPGjGq",
  "type": "assistant",
  "uuid": "6cca3620-1f87-42f1-af7d-8ab347ac16f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145AtYc1VSLWSxgewp6uNJU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 254,
      "cache_read_input_tokens": 74970,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 74970,
          "cache_creation_input_tokens": 254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 254
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "6cca3620-1f87-42f1-af7d-8ab347ac16f4",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier calibration probe transfer paper",
  "sessionId": "3ff56e95-537a-47e8-910b-194e01cedc1e"
}
```

---
