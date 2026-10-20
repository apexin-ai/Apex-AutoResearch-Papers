# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/77b0607c-003d-4705-b21b-c267a108326b.jsonl`
- **Structured JSON:** [`bb13e2f6a2a636bff8e6.json`](../../sessions/bb/bb13e2f6a2a636bff8e6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-24T08:52:14.888Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-24T08:52:14.888Z",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：核心诊断弧（8×–27× gap + PCGrad 因果排除 + four-way ablation）不受影响，仍为论文主力拿分项。 SS 在 Qwen 上强效（AR GAR 0.401±0.047, gap ~1.3×），但 Llama 跨模型效果显著减弱 （AR GAR β=0 ≈ 0.18, gap ~2.7×），导致 SS contribution 从 'general mitigation' 降级为 'effective on Qwen, partially effective cross-model, requires further validation'。 至少 1 位审稿人以 'exposure bias is a known phenomenon' 挑战 novelty（概率 0.3–0.7）， 需靠 8×–27× 定量测量在 auxiliary attention loss 场景的 first empirical characterization + mechanism specificity（GAR-ours vs GAR-Dongre 差异）回应。PCGrad 因果链被接受但被视为 'expected result'。Title 用 T1，Contribution #5 弱化措辞。Discussion 增加 SS transferability limitations 段落，分析 Llama 效果差异的可能原因。目标 Findings 3.0–3.5。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-24T08:52:14.893Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-24T08:52:14.893Z",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-24T08:52:14.916Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：核心诊断弧（8×–27× gap + PCGrad 因果排除 + four-way ablation）不受影响，仍为论文主力拿分项。 SS 在 Qwen 上强效（AR GAR 0.401±0.047, gap ~1.3×），但 Llama 跨模型效果显著减弱 （AR GAR β=0 ≈ 0.18, gap ~2.7×），导致 SS contribution 从 'general mitigation' 降级为 'effective on Qwen, partially effective cross-model, requires further validation'。 至少 1 位审稿人以 'exposure bias is a known phenomenon' 挑战 novelty（概率 0.3–0.7）， 需靠 8×–27× 定量测量在 auxiliary attention loss 场景的 first empirical characterization + mechanism specificity（GAR-ours vs GAR-Dongre 差异）回应。PCGrad 因果链被接受但被视为 'expected result'。Title 用 T1，Contribution #5 弱化措辞。Discussion 增加 SS transferability limitations 段落，分析 Llama 效果差异的可能原因。目标 Findings 3.0–3.5。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "67a87842-f41b-4d9e-9fbd-faa3f9849a08",
  "type": "user",
  "uuid": "1f1d9456-e9dc-4d43-9803-21dfcb6284c0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-24T08:52:14.915Z_

```json
{
  "parentUuid": "1f1d9456-e9dc-4d43-9803-21dfcb6284c0",
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
  "uuid": "936d9732-4bf2-4ed2-b3b0-cc4c7140dcbc",
  "timestamp": "2026-05-24T08:52:14.915Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-24T08:52:14.915Z_

```json
{
  "parentUuid": "936d9732-4bf2-4ed2-b3b0-cc4c7140dcbc",
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
  "uuid": "0324b7d1-2d81-477f-a5a3-49793789e3b1",
  "timestamp": "2026-05-24T08:52:14.915Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-24T08:52:14.915Z_

```json
{
  "parentUuid": "0324b7d1-2d81-477f-a5a3-49793789e3b1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e1ff7450-9d3f-490e-8843-da922a0feb92",
  "timestamp": "2026-05-24T08:52:14.915Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
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
  "aiTitle": "Generate EMNLP paper on residual gating mechanisms",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b"
}
```

---

### Assistant

_source line 8 · 2026-05-24T08:52:18.420Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1ff7450-9d3f-490e-8843-da922a0feb92",
  "isSidechain": false,
  "requestId": "req_011CbM7KA5xiyQ8vuBFGDmKL",
  "type": "assistant",
  "uuid": "5e3a8017-15af-4151-abcc-6a193bfd0f8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mux1gh9yJrGJXVkNpsJEm9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13874,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13874,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13874
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

_source line 9 · 2026-05-24T08:52:19.555Z_

<details open><summary>🔧 Tool call — Read · `toolu_011gGTioBU6tpeba21vfCWsx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e3a8017-15af-4151-abcc-6a193bfd0f8b",
  "isSidechain": false,
  "requestId": "req_011CbM7KA5xiyQ8vuBFGDmKL",
  "type": "assistant",
  "uuid": "d70b5363-a49c-47c4-a329-07f5a34e211c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mux1gh9yJrGJXVkNpsJEm9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13874,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13874,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13874
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

_source line 10 · 2026-05-24T08:52:19.733Z_

<details open><summary>🔧 Tool call — Read · `toolu_012CpJ6nucaBkGiU2bEiwhnN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d70b5363-a49c-47c4-a329-07f5a34e211c",
  "isSidechain": false,
  "requestId": "req_011CbM7KA5xiyQ8vuBFGDmKL",
  "type": "assistant",
  "uuid": "dcd32639-84e0-431e-af3a-64dfe8cbf22a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mux1gh9yJrGJXVkNpsJEm9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13874,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13874,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13874
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

_source line 11 · 2026-05-24T08:52:19.739Z_

<details><summary>↩ Tool result · `toolu_012CpJ6nucaBkGiU2bEiwhnN`</summary>

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
  "parentUuid": "dcd32639-84e0-431e-af3a-64dfe8cbf22a",
  "isSidechain": false,
  "promptId": "67a87842-f41b-4d9e-9fbd-faa3f9849a08",
  "type": "user",
  "uuid": "aadcdd9d-ba16-4332-aa2e-9ae8c7f84b90",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper_framing.md",
      "content": "# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering\n\n> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× gap，Qwen 7.8× / Llama 27× median）。这个 insight 为 auxiliary attention loss 在 teacher-forcing 下的 exposure bias 脆弱性提供首个实证刻画。**SS 初步修复: AR GAR 0.401±0.047（3-seed mean±std），TF/AR gap ~1.3×（range 1.15–1.45×）。**\n> Novelty 排序: (1) exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画 (8×–27× gap) > (2) PCGrad 因果排除梯度方向冲突 + \"观察→假设→排除→指向真因\" 完整因果链 (D028) > (3) SS 迁移到 multi-turn transformer attention objectives (AR GAR 0.401±0.047, 3-seed) > (4) principled intervention + systematic ablation 的 negative result\n> **⚠️ Dream review D024: \"Cannot\" overclaims, novelty \"first measurement\" 过高, 缺 gradient surgery baseline (PCGrad). 标题改 \"Fails to\", novelty 降级 \"first empirical characterization\"**\n> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)\n> 最后更新: 2026-05-24 (3-seed SS 数据完成: AR GAR 0.401±0.047, gap ~1.3× range 1.15–1.45×; β=3/5 跨 seed 极稳定 std<0.01; s42 是 β=0 outlier)\n> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）\n> **Framing 升级目标 3.5**: 对标 gromov2024/sun2025/xiao2024 \"发现→定位→修复\" 模式。SS AR GAR 0.401±0.047 (3-seed, vs base 0.019) 是真正的 positive result，不应埋在 Discussion。\n\n---\n\n## 1. Title Candidates\n\n- **T0 (当前)**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue: A Diagnostic Analysis of Per-Layer Residual Gating\n- **T1**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue （去掉副标题，更简洁有力）\n- **T2**: From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives （强调完整弧：发现+定位+修复）\n- **T3**: The Exposure Bias Barrier: Why Auxiliary Attention Losses Fail at Multi-Turn Inference （barrier metaphor，聚焦机制）\n\n推荐 T1 或 T2。T1 保留当前论文最有记忆点的短语 \"selectively destroys\"，去掉冗长副标题。T2 强调 \"发现→定位→修复\" 完整弧，与 gromov2024/xiao2024 对标。T0 过长（20 词），审稿人可能记不住。T3 偏负面。\n\n---\n\n## 2. Story Arc\n\nMulti-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Accessibility Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), and this improvement transfers perfectly when evaluated on same-distribution text at inference (GAR-ours = 0.49). However, on model-generated text, GAR-ours collapses to 0.064 (Qwen N=50, 7.8× gap) or 0.018 (Llama N=20, 27× gap), driven by text distribution shift. Our central finding is that attention patterns learned under teacher-forced contexts (gold text) do not generalize to autoregressive generation contexts (model-generated text), the classic exposure bias phenomenon. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Notably, this 8×–27× gap is specific to GAR-ours (last-token attention to goals); GAR-Dongre (all-token attention) shows uniformly low values regardless of text distribution, revealing that exposure bias selectively disrupts summary-position attention patterns. Combined with Dongre et al.'s independent failure of goal re-injection, our results provide the first empirical characterization of how text distribution shift (exposure bias) selectively destroys attention patterns learned through auxiliary losses, and identify the specific mechanisms through which this vulnerability manifests. Crucially, we show that scheduled sampling—originally designed for RNN sequence models—transfers to multi-turn transformer attention objectives, compressing the TF–AR gap from 8× to ~1.3× with no perplexity cost (3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001). Inference-time β-steering independently recovers GAR from 0.064 to 0.727. These mitigation results upgrade the paper from pure negative result to a complete \"discover → diagnose → initial remedy\" arc, matching the narrative pattern of high-impact diagnostic papers (gromov2024, sun2025, xiao2024).\n\n---\n\n## 3. Core Claims\n\n| # | Claim | 支撑 | 状态 |\n|---|-------|------|------|\n| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | ✅ 已验证 |\n| C2 | Residual gating 训练时在 same-distribution text 上有效优化 GAR-ours (TF GAR=0.50)，但在 model-generated text 上完全失败 (AR GAR=0.064, 7.8× gap on Qwen N=50; 27× median on Llama N=20)。GAR-Dongre 在两种分布上均低，无 gap——说明分布偏移选择性影响 summary-position attention pattern。 | v7 训练 + d048 N=50 eval + Llama eval + Reviewer 独立验证 | ✅ 已验证（N=50 precision） |\n| C3 | 失败机制的因果分析: (1) Distribution shift 是主因（D028 PCGrad 因果排除梯度方向冲突）; (2) NTP 幅度主导 gate 学习 → NF1 反向 turn conditioning; (3) NF3 gate 干预强度不足 2-7%。PCGrad ablation: 消除方向冲突后 cos_sim 围绕 0 震荡(range -0.151 to +0.091)，但 L_GAR 坍塌轨迹不变且无延迟 → 方向冲突非因果因素。**推理端确认（IID same-protocol）**: v9 GAR-ours=0.0151 vs v7=0.0157 (差<0.1pp), **v9 IID PPL=2.780 vs v7=2.784 (差0.004，无改善)**——PCGrad 消除方向冲突后所有可观测指标均 ≈ v7，方向冲突因 NTP 幅度主导而完全 inconsequential | D014 gate-profile + 梯度冲突量化 + **D028 PCGrad 因果排除** + v9 推理 eval + **M017 PPL 修正** | ✅ **End-to-end 完成**: 训练端 + 推理端均确认梯度方向冲突对 GAR 和 PPL 均无因果影响 |\n| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。IID: GAR 差异<0.6pp, PPL 均 ~2.78。**Model-gen (D033): v9 PCGrad=0.0151, UG=0.0149, LoRA-only=0.0245 均接近 baseline 0.0122——8×–27× gap 在所有训练变体上普遍存在，排除 gating mechanism / turn-conditioning / gradient conflict 作为因果因素** | D021 四路 eval + D033 model-gen eval | ✅ **双重验证**: IID (D021) + model-gen (D033)。model-gen regime 进一步确认 gating 零增量且 GAR collapse 是训练-推理分布偏移的普遍现象 |\n| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Phase 1 ✅ (GAR decay 80.2%, D042), Phase 2 ✅ (TG gap 27× median, gating zero-increment TG≈LO, LoRA-only N=20 eval) | ✅ Fully confirmed |\n\n---\n\n## 4. Negative Findings (NF)\n\n| # | Finding | 证据 | 叙事角色 |\n|---|---------|------|----------|\n| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |\n| NF2 | 8×–27× text distribution shift gap (GAR-ours): TF GAR=0.50 vs AR GAR=0.064 (Qwen N=50, 7.8× gap); Llama AR GAR=0.018 (27× median gap, N=20)。Same-distribution 泛化成功（TF eval GAR=0.50），cross-distribution 泛化失败。**D033 跨变体确认**: v9 PCGrad, UG, LoRA-only model-gen GAR 均接近 baseline——gap 独立于训练策略，是 exposure bias 的普遍表现。GAR-Dongre 在两种分布上均低，无 gap——分布偏移选择性影响 summary-position (last token) attention pattern | d048 N=50 eval + Llama eval + D033 cross-variant | 核心 negative finding。精确定位为 TEXT DISTRIBUTION SHIFT（exposure bias）。 |\n| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |\n| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |\n\n---\n\n## 5. Key Selling Points\n\n**SP1 (核心卖点): Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画。** 8×–27× training-inference GAR-ours gap（Qwen 7.8×, Llama 27× median）提供了 teacher-forcing distribution shift 如何摧毁 auxiliary attention loss 泛化性的实证证据。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。虽然 exposure bias 概念本身已知 (Bengio et al. 2015)，且 sequence generation 中有量化先例 (Ranzato et al. 2016, Wiseman & Rush 2016)，但此前无人刻画其对 auxiliary attention loss 的具体影响。我们的 8×–27× gap 测量展示了这种脆弱性在 attention steering 场景下的严重程度。**注意：(1) claim scope 严格限于 lightweight residual gating + GAR auxiliary loss 的实测范围，不泛化到所有 attention steering 方法。(2) gap 在 GAR-ours（last token only, summary-position attention）上测得（TF 0.50 vs AR 0.064 Qwen / 0.018 Llama）；GAR-Dongre（all response tokens）在两种分布上均低，无 gap——表明 exposure bias 选择性影响 summary-position attention pattern，这一差异本身有分析价值。**\n\n**SP2: NTP-GAR 梯度动力学 + PCGrad 因果排除（gradient conflict is inconsequential）。** 观察到 67-79% 的层 NTP-GAR 梯度方向冲突（cos_sim<0）+ NTP 幅度 3-15x 压制 GAR（mag_ratio 7.5→14.7x）。**PCGrad 消融（D028）因果排除方向冲突**：投影后 cos_sim 围绕 0 震荡（range -0.151 to +0.091），L_GAR 坍塌轨迹不变。**推理端确认（IID same-protocol）**: v9 IID PPL = 2.780 vs v7 = 2.784（差 0.004，无改善）; v9 GAR-ours = 0.0151 vs v7 = 0.0157（差 <0.1pp）——**PCGrad 消除方向冲突后所有可观测指标均无变化**（GAR、PPL、NTP 均 ≈ v7）。方向冲突虽然可测量存在于 v7 中，但对训练和推理结果无任何因果影响——7.5–14.7× NTP 幅度主导使方向冲突完全无关紧要（inconsequential）。**⚠️ M017: 此前 \"PPL -46%\" 和 \"selective dissociation\" 论述为跨协议对比伪影（model-gen PPL 1.50 vs IID PPL 2.78），已撤回。** **精确 claim scope**: gradient direction conflict is **neither necessary nor sufficient** for the 8×–27× GAR gap; exposure bias alone is sufficient。NOT necessary: 移除冲突→gap仍在; NOT sufficient: v7有冲突但L_GAR训练时收敛; Exposure bias is sufficient: 训练≠推理分布→GAR泛化失败。**Gate 行为额外 insight**: v9 gate dynamic range 比 v7 更宽 (L15 range 0.33 vs v7 0.21)——PCGrad 给 gate 更大自由度，但 gate 用该自由度更激进地优化 NTP 而非 GAR，说明优化景观固有偏好语言建模目标。\n\n**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融严格隔离贡献: TG (learned gate + GAR loss) / UG (uniform gate + GAR loss) / LoRA-only (gate=1.0 fixed + GAR loss, 无 gating 机制) / Base。注意：三个 fine-tuned 变体均使用 GAR loss，消融测试的是 gating 机制的增量贡献，而非 GAR loss 本身的效果。\n\n**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。\n\n**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。\n\n---\n\n## 6. Anticipated Reviewer Concerns\n\n| # | 严重度 | 预期质疑 | 回应策略 |\n|---|--------|----------|----------|\n| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |\n| W2 | **严重** | \"你只是没调对参数\" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |\n| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |\n| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |\n| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（8×–27× 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| W6 | **严重** | 引用不足（Dream review: 11篇远不够）| 目标 25-30 篇。必须覆盖: attention sinks (Xiao et al. 2024), Found-in-the-Middle (Ko et al. 2024), gated attention (Qiu et al. 2025), transformer circuits (Elhage et al. 2021), FlexiDepth (Luo et al. 2025), multi-turn eval (MT-Bench-101, MultiChallenge), exposure bias mitigation (Professor Forcing, SEARNN) 等。Paper Agent 写作时负责扩充。|\n| W7 | **严重** | 单 seed 无方差估计 | 所有实验 seed=42，TG-LoRA 差异 ±0.001 在噪声层。回应: held-out eval 50 conversations 提供 paired bootstrap CI，若 CI 包含 0 则统计支持 \"zero benefit\"。必要时追加 2 个 seed 的训练。|\n| W8 | **中等** | 缺 exposure-bias mitigation 实验 | 测试 scheduled sampling / model-generated context 训练能否缩小 8×–27× gap。加入 experiment_plan (P1)。如果实验表明 mitigation 确实缩小 gap，论文从 \"negative result\" 升级为 \"negative result + constructive direction\"。|\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 exposure bias 的定量测量（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| R3 | 低 | 8×–27× gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |\n| R4 | ~~低~~ **已核实** | Code-paper 公式语义相反 | **已确认不一致（plan_017 DONE）**。代码正确实现 ReZero-style: `x_{l+1} = x_l + g_l · f_l(x_l)`（gate 缩放子层输出，g→0=层 no-op）。Dream paper.tex 错误写为 `x_{l+1} = g_l · x_l + f_l(x_l)`（gate 缩放残差流，g→0=破坏 skip connection）。**实验数据不受影响**（所有实验用同一份代码）。**Paper Agent 写作时必须**: (1) Method section 用正确公式 `x + g·f(x)`; (2) 机制叙事修正: g→0 = 子层输出被抑制（层变 no-op），NTP 推 g→1 是为保留层计算能力，不是保留 skip connection; (3) NF3 \"gate attenuation 2-7%\" 指子层贡献缩放，表述正确但需明确。|\n\n---\n\n## 7. Dongre et al. 关系定位\n\n| 维度 | Dongre et al. | 本文 |\n|------|---------------|------|\n| 核心问题 | \"发生了什么\" + \"为什么\" | \"怎么干预\" + \"为什么干预失败\" |\n| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |\n| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 8×–27× 泛化 gap + turn conditioning 反转 |\n| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |\n| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |\n\n**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。\n\n共同推论: 两种独立干预路线均失败 → lightweight residual gating with auxiliary attention loss 在 teacher-forcing 下面临严重泛化障碍（8×–27× gap）→ 需要 inference-time 干预或 exposure bias mitigation（SS 已验证可将 gap 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047））。（注意：scope 限于 lightweight gating，不泛化到所有 attention steering 方法。）\n\n---\n\n## 8. GAR 定义策略\n\n| 用途 | 定义 | Goal tokens | Response tokens | 理由 |\n|------|------|------------|----------------|------|\n| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |\n| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |\n| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |\n\n**D024 精确化（d048 N=50 更新）**: GAR-ours TF=0.50, AR=0.064（Qwen 7.8× gap）; Llama AR=0.018（27× median gap）。GAR-Dongre 在两种分布上均低，无 gap。8×–27× gap 是 text distribution shift 现象，特定于 summary-position attention (GAR-ours)。\n\n---\n\n## 9. 论文结构草案\n\n1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示\n2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表\n3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention\n4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据\n5. **Method**: ThreadGate 架构（⚠️ 非简单标量 gate：per-layer 2 层 MLP + turn embedding，接收 hidden_state + turn_distance/turn_index，输出 per-token per-layer sigmoid gate 值。公式 g_l = σ(W_2·ReLU(W_1·[proj(x_l); emb(t_d, t_i)] + b_1) + b_2)。Uniform Gate = 同架构但用 constant_vector 替代 turn embedding，仍然 per-layer content-dependent）+ MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置\n6. **Experiments**: §5.1 Setup → §5.2 Main Results (五路消融 TG/+PCGrad/UG/LoRA-only/Base) → §5.3 Inference-Time Steering (β-steering, GAR 0.727) → **§5.4 Scheduled Sampling (gap 8×→~1.3×, 独立 Results 小节)**\n7. **Analysis**: §6.1 Gate Turn Conditioning → §6.2 PCGrad Gradient Conflict Exclusion → §6.3 Distribution Shift Analysis → §6.4 Mechanism Specificity → §6.5 Cross-Model Replication\n8. **Discussion**: exposure bias 对 auxiliary attention loss 的具体影响机制 + Why NTP self-recovers but GAR does not + Downstream effects (instruction retention)。**SS 已移至 §5.4**\n9. **Conclusion**: 完整弧总结——发现 (8×–27× collapse) + 定位 (PCGrad modus tollens) + 修复 (steering + SS)\n\n### 贡献列表（按 novelty 排序）\n\n1. **Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画**: 实证展示 teacher-forcing distribution shift 如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× training-inference GAR-ours gap），为 teacher-forcing 下的 attention steering 方法提供具体风险标杆\n2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）\n3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline\n4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性\n5. **Scheduled sampling 作为初步修复**: 首次证明 time-scheduled sampling（linearly mixing model-generated context，原为 RNN 设计）可迁移到 auxiliary attention objectives in multi-turn transformers，将 TF–AR gap 从 8× 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001），无 PPL 代价。配合 inference-time β-steering（GAR 0.064→0.727），构成完整的 mitigation toolkit。**注意**：Dou & Gales (2022) \"Parallel Attention Forcing\" 使用 data-dependent attention KL 选择训练模式（单轮 NMT），与我们的 time-scheduled + multi-turn + auxiliary attention 目标有三重区分。必须引用并区分。SS 与 steering 是替代关系而非互补——高 β 时两者趋同（β=5: SS 0.717 ≈ TG 0.727），Discussion 需明确说明\n\n---\n\n## 10. 竞争力评估\n\n### Dream Review 结果 (2026-05-19, dream_20260519T135115)\n- **Best case**: 3.0 (Weak Reject / Findings-level)。主要扣分: claim 过度泛化 (W1), 引用不足 (W6), 单 seed (W7)。\n- **Median case**: 3.0 (Weak Reject)。同上 + distribution shift insight incremental (W5)。\n- **Worst case**: 未完成 review（crash），但 imagined experiments 显示最坏情况下 Llama-3 不复现 dramatic pattern。\n\n### 修正后预期（2026-05-23 Framing 升级后）\n- **当前状态**: SS 升级为独立 Results + 5th contribution + 56 references + Llama 跨模型 + 3-seed 统计中 + bootstrap CI。\n- **Best case**: 3.5 (Borderline Conference / Accept)。完整 \"发现→定位→修复\" 弧匹配 gromov/sun/xiao 模式。\n- **Median case**: 3.0-3.5 (Findings-Conference borderline)。若 SS+steering 联合 eval 接近 TF parity → 推向 3.5。\n- **冲 Main 条件**: SS+steering 联合接近 parity + Llama SS 跨模型复现 + KL divergence 机制证据 + 3-seed 正式统计。\n- **核心差异化**: 不是 \"gating 失败了\"（弱），而是 \"exposure bias 在 auxiliary attention loss 上的首个定量测量 + PCGrad 因果排除 + SS/steering 初步修复\"（强）。\n- **关键风险**: W5（exposure bias 已知）需要精确定位增量；SS+steering 联合是否真能接近 parity 待验证。\n",
      "numLines": 152,
      "startLine": 1,
      "totalLines": 152
    }
  },
  "sourceToolAssistantUUID": "dcd32639-84e0-431e-af3a-64dfe8cbf22a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T08:52:19.818Z_

<details><summary>↩ Tool result · `toolu_011gGTioBU6tpeba21vfCWsx`</summary>

```text
1	[
2	  {
3	    "name": "Llama-3.1-8B Gradient Conflict Analysis",
4	    "description": "对 Llama TG v7 的 3 个 epoch checkpoint 计算 NTP vs GAR gate 参数梯度的 cos_sim 和 magnitude ratio，验证 NTP-GAR 梯度竞争是否跨模型一致。\n",
5	    "results": {
6	      "epoch0_cos_sim_mean": 0.012,
7	      "epoch0_cos_sim_std": 0.082,
8	      "epoch0_neg_layers_pct": 50.0,
9	      "epoch0_mag_ratio_median": 18.3,
10	      "epoch1_cos_sim_mean": 0.003,
11	      "epoch1_cos_sim_std": 0.068,
12	      "epoch1_neg_layers_pct": 53.1,
13	      "epoch1_mag_ratio_median": 24.5,
14	      "epoch2_cos_sim_mean": 0.005,
15	      "epoch2_cos_sim_std": 0.071,
16	      "epoch2_neg_layers_pct": 53.1,
17	      "epoch2_mag_ratio_median": 25.7,
18	      "overall_cos_sim": 0.005,
19	      "overall_neg_layers_pct": 53.1,
20	      "overall_mag_ratio_median": 25.7
21	    },
22	    "tables": [
23	      {
24	        "name": "Table: Cross-Model Gradient Analysis",
25	        "columns": [
26	          "Metric",
27	          "Qwen-2.5-7B",
28	          "Llama-3.1-8B",
29	          "Interpretation"
30	        ],
31	        "rows": [
32	          [
33	            "cos_sim (final epoch)",
34	            "-0.042",
35	            "+0.005",
36	            "Qwen: mild conflict; Llama: orthogonal"
37	          ],
38	          [
39	            "neg_layers %",
40	            "67.9%",
41	            "53.1%",
42	            "Qwen: moderate asymmetry; Llama: near-random"
43	          ],
44	          [
45	            "mag_ratio",
46	            "14.7×",
47	            "25.7×",
48	            "Llama NTP dominance ~1.7× stronger"
49	          ],
50	          [
51	            "TG AR GAR gap",
52	            "8× (N=50)",
53	            "27× (N=20 median)",
54	            "Correlates with mag_ratio"
55	          ]
56	        ]
57	      }
58	    ],
59	    "figures": [],
60	    "analysis": "跨模型梯度分析确认两个关键结论：(1) NTP-GAR 梯度方向不存在系统性冲突 （Llama 近乎正交，Qwen 轻度负相关），方向冲突不是 GAR collapse 的因果因素， 与 PCGrad 因果排除实验（plan_018）结论一致；(2) NTP 幅度主导是跨模型一致的 结构性特征（Qwen 7.5–14.7×, Llama 25.7×），且幅度主导程度与 TG 推理 gap 大小正相关。在 median 档叙事中，这个实验支撑 C3（失败机制因果分析）的 跨模型泛化性，且 Llama 的更极端 mag_ratio 为 Llama SS 效果更弱提供了 事前预测基础。Paper §6.5 Cross-Model Replication 需要报告此数据。 审稿人可能视此为 'expected result'（NTP 主导不意外），但 25.7× 这个数值 本身有定量参考价值。\n\n\nLlama-3.1-8B 采用 GQA（8 KV heads）+ 32 层架构，比 Qwen-2.5-7B（28 层）更深。 cos_sim ≈ 0 表示 NTP 和 GAR 梯度近乎正交而非冲突——这与 Qwen 的轻度负相关 （cos_sim -0.042 to -0.089）有微妙差异但结论一致：方向冲突不是 GAR collapse 的 因果因素。neg_layers ≈ 53%（接近随机 50%）进一步确认无系统性冲突。 mag_ratio 25.7× 显著高于 Qwen 的 7.5–14.7×，原因是 Llama 更深的网络使 NTP 梯度 有更多反向传播路径累积幅度。这解释了 Llama 上 TG gap 更大（27× vs 8×）： NTP 幅度主导更极端，gate 更难学到有意义的 GAR-oriented 行为。\n"
61	  },
62	  {
63	    "name": "Expanded Eval Set (N=200 TF + N=50 AR)",
64	    "description": "将 TF eval 从 N=50 扩展到 N=200（idx>=7000 from UltraChat）， 提升 bootstrap CI 统计功效。AR eval 保持 N=50（extreme effect size 下已充分）。\n",
65	    "results": {
66	      "tf_tg_gar_ours_n200": 0.5042,
67	      "tf_tg_gar_ours_ci95": [
68	        0.4891,
69	        0.5193
70	      ],
71	      "tf_ug_gar_ours_n200": 0.5061,
72	      "tf_lo_gar_ours_n200": 0.4985,
73	      "tf_base_gar_ours_n200": 0.0131,
74	      "tf_tg_ppl_n200": 2.78,
75	      "tf_tg_dongre_n200": 0.0148,
76	      "bootstrap_ci_tg_vs_lo_gar": [
77	        -0.0012,
78	        0.0028
79	      ],
80	      "bootstrap_ci_tg_vs_ug_gar": [
81	        -0.0022,
82	        0.0005
83	      ],
84	      "bootstrap_ci_includes_zero": true,
85	      "ci_width_reduction_vs_n50": 0.42
86	    },
87	    "tables": [
88	      {
89	        "name": "Table: TF Eval N=200 Summary",
90	        "columns": [
91	          "Variant",
92	          "GAR-ours",
93	          "95% CI",
94	          "GAR-Dongre",
95	          "PPL"
96	        ],
97	        "rows": [
98	          [
99	            "Base",
100	            "0.013",
101	            "[0.010, 0.016]",
102	            "0.003",
103	            "4.34"
104	          ],
105	          [
106	            "ThreadGate",
107	            "0.504",
108	            "[0.489, 0.519]",
109	            "0.015",
110	            "2.78"
111	          ],
112	          [
113	            "Uniform Gate",
114	            "0.506",
115	            "[0.491, 0.521]",
116	            "0.012",
117	            "2.78"
118	          ],
119	          [
120	            "LoRA-only",
121	            "0.499",
122	            "[0.483, 0.514]",
123	            "0.013",
124	            "2.78"
125	          ],
126	          [
127	            "TG-LO diff",
128	            "+0.006",
129	            "[-0.001, 0.003]",
130	            "+0.002",
131	            "0.00"
132	          ]
133	        ]
134	      }
135	    ],
136	    "figures": [],
137	    "analysis": "N=200 eval 是纯统计功效提升，不改变任何定性结论。在 median 档下，这个实验 的价值是堵住 W7 reviewer concern 的 one-liner：\"N=200 TF CI confirms zero gating benefit with narrower intervals.\" AR eval 保持 N=50 因为 8×–27× gap 的 effect size 足以在小样本下达到统计显著。审稿人在 median 档仍可能提 'would be nice to see AR N=200'，但不太可能构成 rejection 理由。\n\n\nN=200 TF eval 提供 4× 样本量（vs N=50），bootstrap CI 宽度按 √(50/200) ≈ 0.5 缩窄约一半。TG-LO GAR 差异 CI 仍包含 0，进一步强化 'zero gating benefit' 结论。 点估计与 N=50 eval（plan_008）一致（TG 0.504, UG 0.505, LO 0.498）， 因为 UltraChat idx>=7000 与 idx>=8000 的分布几乎相同。PPL 和 GAR-Dongre 同样一致。审稿人 W7（单 seed / 统计不足）的回应因此更有力：极端效应量 （GAR-ours TF 0.50 vs AR 0.016）在 N=200 下 CI 不包含 parity。 但 median 档下审稿人仍可能提 'more seeds' 作为 minor concern。\n"
138	  },
139	  {
140	    "name": "λ_GAR Sensitivity (λ=10, 1 epoch)",
141	    "description": "训练 v7 with λ_GAR=10（10× 默认值），测试提高 GAR loss 权重能否改善 gate 学习和 AR GAR。仅跑 1 epoch 以节省 GPU。若预算允许追加 λ=0.1。\n",
142	    "results": {
143	      "lambda10_training": {
144	        "epoch1_avg_loss": 1.012,
145	        "epoch1_avg_ntp": 0.946,
146	        "epoch1_avg_gar": 0.0066,
147	        "gate_mean": 0.905,
148	        "gate_std": 0.082,
149	        "gate_min": 0.68,
150	        "gate_max": 0.996,
151	        "wall_clock_hours": 2.1
152	      },
153	      "lambda10_eval_iid": {
154	        "gar_ours": 0.535,
155	        "gar_dongre": 0.018,
156	        "ppl": 2.95
157	      },
158	      "lambda10_eval_ar": {
159	        "gar_ours": 0.024,
160	        "gar_dongre": 0.019,
161	        "ppl": 1.41
162	      },
163	      "lambda10_gap_ratio": 22.3,
164	      "lambda01_training": {
165	        "epoch1_avg_loss": 0.978,
166	        "epoch1_avg_ntp": 0.977,
167	        "epoch1_avg_gar": 0.001,
168	        "gate_mean": 0.972,
169	        "gate_std": 0.022
170	      },
171	      "lambda01_eval_iid": {
172	        "gar_ours": 0.42,
173	        "gar_dongre": 0.011,
174	        "ppl": 2.76
175	      },
176	      "lambda01_eval_ar": {
177	        "gar_ours": 0.013,
178	        "gar_dongre": 0.016,
179	        "ppl": 1.38
180	      },
181	      "lambda01_gap_ratio": 32.3,
182	      "v7_reference_gap_ratio": 32.1
183	    },
184	    "tables": [
185	      {
186	        "name": "Table: λ_GAR Sensitivity",
187	        "columns": [
188	          "λ_GAR",
189	          "TF GAR-ours",
190	          "AR GAR-ours",
191	          "Gap",
192	          "IID PPL",
193	          "Gate Mean"
194	        ],
195	        "rows": [
196	          [
197	            "0.1",
198	            "0.42",
199	            "0.013",
200	            "32.3×",
201	            "2.76",
202	            "0.972"
203	          ],
204	          [
205	            "1.0 (v7)",
206	            "0.50",
207	            "0.016",
208	            "32.1×",
209	            "2.78",
210	            "0.934"
211	          ],
212	          [
213	            "10.0",
214	            "0.535",
215	            "0.024",
216	            "22.3×",
217	            "2.95",
218	            "0.905"
219	          ]
220	        ]
221	      }
222	    ],
223	    "figures": [],
224	    "analysis": "λ_GAR sensitivity 实验在 median 档扮演辅助角色：它不是核心 contribution 但 强化 W2 回应——\"你只是没调对参数\"。10× λ 使 GAR 梯度与 NTP 量级相当， gate 获得更大动态范围（std 0.082 vs 0.049），TF 性能确实提升（+3.5pp）， 但 AR GAR 仅微升 0.8pp，gap 仍 22×。这表明 gradient magnitude 不是瓶颈， exposure bias 是。Paper 中作为 Appendix λ-sensitivity 表格，正文一句引用： \"Even with 10× GAR weight (Table X), the TF–AR gap remains >20×, confirming that distribution shift, not gradient competition, is the limiting factor.\" 在 median 档下，审稿人可能视此为 'unsurprising follow-up' 但不会反对。\n\n\nλ_GAR=10 将 GAR 梯度幅度提升 10×，使有效 NTP/GAR ratio 从 7.5–14.7× 降至 0.75–1.47×——两者量级相当。结果：(1) TF GAR 从 0.50 提升到 0.535（GAR 获得 更多优化预算，gate 学到更强的注意力干预）；(2) gate_mean 从 0.93 降至 0.905, gate_std 从 0.049 提升到 0.082——gate 获得更大动态范围；(3) 但 AR GAR 仅从 0.016 微升到 0.024（仍然近乎 collapse，22× gap）。这是 median 档的关键证据： 梯度幅度平衡后 exposure bias gap 仍然巨大，直接排除 'gradient competition is the bottleneck' 假说。PPL 从 2.78 升至 2.95（+6%），因为 NTP 获得相对更少 优化预算。λ=0.1 方向上 gate 几乎冻结（gate_mean 0.972），gap 32×，接近 v7。 三点（λ=0.1/1.0/10）构成 λ sensitivity curve，在 Appendix 中报告。\n"
225	  },
226	  {
227	    "name": "TF vs AR Attention KL Divergence",
228	    "description": "对 50 conversations 计算 per-head KL(P_TF || P_AR) 量化注意力分布偏移。 分析 GAR-relevant heads 是否表现出更大的 KL。纯 CPU 分析。\n",
229	    "results": {
230	      "tg_mean_kl_all_heads": 0.054,
231	      "base_mean_kl_all_heads": 0.043,
232	      "tg_kl_std": 0.032,
233	      "base_kl_std": 0.028,
234	      "high_kl_layers": "L23-L27, L9",
235	      "high_kl_heads_top5": "L25H3, L27H1, L24H2, L9H0, L23H3",
236	      "gate_kl_correlation": 0.11,
237	      "gar_robustness_by_definition": {
238	        "gar_ours_tg_over_base_ratio": 21.4,
239	        "gar_goal_only_ratio": 63.0,
240	        "gar_all_token_ratio": 1.7,
241	        "gar_first_token_ratio": 1.8
242	      },
243	      "kl_percentile_95": 0.142,
244	      "kl_percentile_99": 0.198,
245	      "n_conversations": 50,
246	      "n_heads_total": 112
247	    },
248	    "tables": [
249	      {
250	        "name": "Table: KL Divergence by Layer Group",
251	        "columns": [
252	          "Layer Group",
253	          "TG Mean KL",
254	          "Base Mean KL",
255	          "TG/Base Ratio"
256	        ],
257	        "rows": [
258	          [
259	            "L0-L6 (shallow)",
260	            "0.031",
261	            "0.028",
262	            "1.11"
263	          ],
264	          [
265	            "L7-L13 (lower-mid)",
266	            "0.042",
267	            "0.036",
268	            "1.17"
269	          ],
270	          [
271	            "L14-L20 (upper-mid)",
272	            "0.058",
273	            "0.045",
274	            "1.29"
275	          ],
276	          [
277	            "L21-L27 (deep)",
278	            "0.089",
279	            "0.065",
280	            "1.37"
281	          ]
282	        ]
283	      },
284	      {
285	        "name": "Table: GAR Definition Sensitivity to Attention Shift",
286	        "columns": [
287	          "GAR Definition",
288	          "TG TF",
289	          "TG AR",
290	          "TG TF/AR Gap",
291	          "Sensitivity"
292	        ],
293	        "rows": [
294	          [
295	            "GAR-ours (last token)",
296	            "0.504",
297	            "0.016",
298	            "32×",
299	            "High"
300	          ],
301	          [
302	            "GAR goal-only",
303	            "0.630",
304	            "0.010",
305	            "63×",
306	            "Very High"
307	          ],
308	          [
309	            "GAR all-token",
310	            "0.028",
311	            "0.016",
312	            "1.7×",
313	            "Low"
314	          ],
315	          [
316	            "GAR first-token",
317	            "0.035",
318	            "0.019",
319	            "1.8×",
320	            "Low"
321	          ]
322	        ]
323	      }
324	    ],
325	    "figures": [],
326	    "analysis": "KL 分析在 median 档提供了 exposure bias 的注意力空间机制证据：分布偏移 在深层注意力头最严重（mean KL 0.089 vs 浅层 0.031），恰好是负责 long-range goal-attention routing 的层。GAR-ours 的 21.4× 敏感度 vs all-token 的 1.7× 解释了 mechanism specificity——为什么 exposure bias '选择性' 摧毁 summary-position attention。这个分析不需要额外 GPU，是 pure diagnostic，在 median 档下 审稿人会认为是 'nice additional evidence' 但不太可能改变评分。 Paper §6.4 Mechanism Specificity 使用此数据。\n\n\nTF vs AR 注意力分布的 KL 散度量化了 exposure bias 在注意力空间的具体表现。 TG 模型的 mean KL（0.054）高于 base（0.043），因为 TG 训练在 TF 条件下 专门塑造了注意力 pattern（GAR-ours 0.50），这些 pattern 在 AR 条件下偏移更大。 高 KL 集中在 L23-L27（深层 attention heads），与 gate profile 中这些层 gate value 最低（Llama L25=0.719）一致——gates 试图在这些层做最多干预， 恰好也是 TF-AR 分布偏移最大的层。Gate-KL 相关仅 0.11，说明 gate 没有学到 track distribution shift 的能力。GAR-ours（last-token）对 KL 的敏感度 21.4× 远高于 all-token（1.7×）和 first-token（1.8×），解释了为什么 exposure bias 选择性摧毁 summary-position attention：last-token attention 更依赖远程 context 质量，而 all/first-token 的 attention 更局部、更鲁棒。\n"
327	  },
328	  {
329	    "name": "Llama-3.1-8B Scheduled Sampling Training + Eval",
330	    "description": "在 Llama-3.1-8B 上复现 SS 训练（linear schedule 0→0.5 over 3 epochs）， 测试 SS gap 压缩能否跨模型泛化。这是 median 档最关键的实验—— 决定 SS 是 'general mitigation' 还是 'model-dependent'。\n",
331	    "results": {
332	      "training": {
333	        "total_steps": 3000,
334	        "epochs_completed": 3,
335	        "wall_clock_hours": 10.8,
336	        "final_loss": 0.927,
337	        "final_ntp_loss": 0.926,
338	        "final_gar_loss": 0.0009,
339	        "final_gate_mean": 0.925,
340	        "final_gate_std": 0.065,
341	        "final_gate_min": 0.705,
342	        "ss_ratio_final": 0.5,
343	        "ss_fallback_count": 12,
344	        "gpu_mem_gb": 71.2
345	      },
346	      "eval_tf": {
347	        "gar_ours": 0.485,
348	        "gar_dongre": 0.38,
349	        "ppl": 2.6,
350	        "n_conversations": 50
351	      },
352	      "eval_ar_beta0": {
353	        "gar_ours": 0.18,
354	        "gar_ours_std": 0.09,
355	        "gar_dongre": 0.25,
356	        "ppl": 1.4,
357	        "n_conversations": 20
358	      },
359	      "eval_ar_beta3": {
360	        "gar_ours": 0.45,
361	        "ppl": 1.55
362	      },
363	      "eval_ar_beta5": {
364	        "gar_ours": 0.62,
365	        "ppl": 1.72
366	      },
367	      "gap_ratio_beta0": 2.7,
368	      "gap_ratio_vs_tg_no_ss": 15.9,
369	      "improvement_over_tg_baseline": "10× (0.018→0.18)",
370	      "improvement_over_qwen_ss_comparison": "0.45× (0.18 vs Qwen 0.40)"
371	    },
372	    "tables": [
373	      {
374	        "name": "Table: Cross-Model SS Comparison (Key Paper Table)",
375	        "columns": [
376	          "Metric",
377	          "Qwen-2.5-7B",
378	          "Llama-3.1-8B",
379	          "Cross-Model Ratio"
380	        ],
381	        "rows": [
382	          [
383	            "Base AR GAR",
384	            "0.019",
385	            "0.009",
386	            "2.1×"
387	          ],
388	          [
389	            "TG AR GAR (no SS)",
390	            "0.064",
391	            "0.018",
392	            "3.6×"
393	          ],
394	          [
395	            "SS AR GAR β=0",
396	            "0.401±0.047",
397	            "0.18±0.09",
398	            "2.2×"
399	          ],
400	          [
401	            "SS AR GAR β=3",
402	            "0.596±0.008",
403	            "0.45",
404	            "1.3×"
405	          ],
406	          [
407	            "SS AR GAR β=5",
408	            "0.717±0.001",
409	            "0.62",
410	            "1.2×"
411	          ],
412	          [
413	            "TF GAR",
414	            "0.498±0.004",
415	            "0.485",
416	            "1.03×"
417	          ],
418	          [
419	            "SS Gap (TF/AR β=0)",
420	            "1.26×",
421	            "2.7×",
422	            "-"
423	          ],
424	          [
425	            "TG Gap (no SS)",
426	            "32×",
427	            "27× (median)",
428	            "-"
429	          ],
430	          [
431	            "SS PPL β=0",
432	            "1.441",
433	            "1.40",
434	            "1.03×"
435	          ]
436	        ]
437	      },
438	      {
439	        "name": "Table: Llama SS vs Llama TG Comparison",
440	        "columns": [
441	          "Condition",
442	          "AR GAR-ours",
443	          "AR GAR-Dongre",
444	          "PPL",
445	          "Improvement"
446	        ],
447	        "rows": [
448	          [
449	            "Base",
450	            "0.009",
451	            "0.005",
452	            "1.27",
453	            "—"
454	          ],
455	          [
456	            "TG (no SS)",
457	            "0.018",
458	            "0.018",
459	            "1.32",
460	            "2× over base"
461	          ],
462	          [
463	            "LO (no SS)",
464	            "0.018",
465	            "0.020",
466	            "1.32",
467	            "2× over base"
468	          ],
469	          [
470	            "SS β=0",
471	            "0.18",
472	            "0.25",
473	            "1.40",
474	            "20× over base"
475	          ],
476	          [
477	            "SS β=3",
478	            "0.45",
479	            "0.38",
480	            "1.55",
481	            "50× over base"
482	          ],
483	          [
484	            "SS β=5",
485	            "0.62",
486	            "0.48",
487	            "1.72",
488	            "69× over base"
489	          ]
490	        ]
491	      }
492	    ],
493	    "figures": [],
494	    "analysis": "Llama SS 是 median 档的 defining experiment。结果构成 'partial success' 叙事： SS 在 Llama 上有效（20× over base, gap 从 27× 压缩到 2.7×），但效果显著 弱于 Qwen（gap 2.7× vs 1.3×, AR GAR 0.18 vs 0.40）。这决定了论文 Contribution #5 的措辞必须弱化为 'model-dependent efficacy'，SS 从 'general mitigation' 降级为 'promising but requires further validation'。\n论文需要在 Discussion 中增加 'Limitations of SS Transferability' 段落，分析 架构差异（GQA head 数量、层数、attention sink 强度）作为可能原因， 并建议未来工作探索 model-specific SS schedule 调优。\n积极面：即使在 Llama 上，SS β=0 的 0.18 也远优于 TG 无 SS 的 0.018， 证明 SS 的方向是正确的。β-steering 仍然有效，β=5 时 Llama 达到 0.62 （Qwen 0.72），高 β 下两模型趋同，说明推理时干预的跨模型泛化性好于 训练时 SS 的泛化性。这个 insight 本身有 discussion 价值。\n审稿人视角：median 档下，至少 1 位审稿人会将 Llama SS 结果视为 'weakness' （SS 不 general），可能降低 contribution 评分。回应策略：(1) SS 方向正确 但 model-specific tuning needed；(2) 核心 contribution 是诊断（8×–27× gap + PCGrad）不依赖 SS 跨模型；(3) SS 作为 'initial evidence, not claim of generality'。\n\n\nLlama SS 在 median 档展现 'partial success'：AR GAR β=0 = 0.18，相比 Llama TG 无 SS 的 0.018（median）改善了 10×，但远逊于 Qwen SS 的 0.40。 Gap 从 TG 的 27×（median）压缩到 2.7×，但 Qwen SS 压缩到 ~1.3×。\n效果减弱的原因分析： (1) 架构差异：Llama GQA 使用 8 KV heads（vs Qwen 的不同 KV 配置），\n    attention head 更少意味着 goal-relevant routing 的容量更受限，\n    SS 修正训练分布后能利用的 head 容量上限更低。\n(2) NTP 幅度主导更极端：Llama mag_ratio 25.7×（vs Qwen 14.7×），\n    即使 SS 缩小了分布偏移，gates 仍然在更强的 NTP 压力下学习。\n(3) 基线 gap 更大：Llama 的原始 TG gap 27×（vs Qwen 8×），\n    说明 Llama 的注意力 pattern 对 context 分布更敏感，\n    SS 能部分补偿但无法完全克服这种固有脆弱性。\n(4) 32 层 vs 28 层：更多层意味着更多 gate-NTP 交互点，\n    SS 的修正信号被稀释。\n\nPPL 1.40 与 Llama TG 的 1.32 接近（+6%），说明 SS 没有显著 PPL 代价。 β-steering 仍然有效（β=5: 0.62），说明推理时干预在 Llama 上也 work。\n"
495	  },
496	  {
497	    "name": "SS 3-Seed Validation (Qwen)",
498	    "description": "Qwen SS 三个 seed（s42, s123, s456）的训练 + eval，提供 mean±std 统计。 回应 W7（单 seed 无方差估计）。\n",
499	    "results": {
500	      "per_seed_tf_gar": {
501	        "s42": 0.503,
502	        "s123": 0.495,
503	        "s456": 0.496
504	      },
505	      "per_seed_ar_gar_beta0": {
506	        "s42": 0.347,
507	        "s123": 0.423,
508	        "s456": 0.433
509	      },
510	      "per_seed_ar_gar_beta3": {
511	        "s42": 0.593,
512	        "s123": 0.59,
513	        "s456": 0.605
514	      },
515	      "per_seed_ar_gar_beta5": {
516	        "s42": 0.717,
517	        "s123": 0.717,
518	        "s456": 0.716
519	      },
520	      "per_seed_ppl_beta0": {
521	        "s42": 1.442,
522	        "s123": 1.441,
523	        "s456": 1.439
524	      },
525	      "three_seed_summary": {
526	        "tf_gar_mean": 0.498,
527	        "tf_gar_std": 0.004,
528	        "ar_gar_beta0_mean": 0.401,
529	        "ar_gar_beta0_std": 0.047,
530	        "ar_gar_beta3_mean": 0.596,
531	        "ar_gar_beta3_std": 0.008,
532	        "ar_gar_beta5_mean": 0.717,
533	        "ar_gar_beta5_std": 0.001,
534	        "ppl_mean": 1.441,
535	        "ppl_std": 0.001,
536	        "gap_mean": 1.26,
537	        "gap_std": 0.17,
538	        "gap_range": "1.15–1.45×"
539	      },
540	      "outlier_analysis": {
541	        "s42_is_beta0_outlier": true,
542	        "s42_ar_gar_deviation": "-1.15σ from mean",
543	        "s42_tf_gar_normal": true,
544	        "s42_note": "s42 在 β=0 偏低但 β≥3 正常，说明 s42 的 SS 训练在低 β 泛化稍弱"
545	      }
546	    },
547	    "tables": [
548	      {
549	        "name": "Table: SS 3-Seed Results",
550	        "columns": [
551	          "Seed",
552	          "TF GAR",
553	          "AR GAR β=0",
554	          "AR GAR β=3",
555	          "AR GAR β=5",
556	          "PPL β=0",
557	          "Gap"
558	        ],
559	        "rows": [
560	          [
561	            "s42",
562	            "0.503",
563	            "0.347",
564	            "0.593",
565	            "0.717",
566	            "1.442",
567	            "1.45×"
568	          ],
569	          [
570	            "s123",
571	            "0.495",
572	            "0.423",
573	            "0.590",
574	            "0.717",
575	            "1.441",
576	            "1.17×"
577	          ],
578	          [
579	            "s456",
580	            "0.496",
581	            "0.433",
582	            "0.605",
583	            "0.716",
584	            "1.439",
585	            "1.15×"
586	          ],
587	          [
588	            "Mean±Std",
589	            "0.498±0.004",
590	            "0.401±0.047",
591	            "0.596±0.008",
592	            "0.717±0.001",
593	            "1.441±0.001",
594	            "1.26±0.17"
595	          ]
596	        ]
597	      }
598	    ],
599	    "figures": [],
600	    "analysis": "3-seed 在 median 档为 SS claim 提供了最低限度的统计支撑。AR GAR 0.401±0.047 在 Qwen 上确认 SS 是有效的（effect size / std > 8），但 s42 的 outlier 行为 暗示 SS 的低 β 泛化性存在 seed sensitivity。论文应报告完整 3-seed 数据， 在正文用 mean±std，附录报告 per-seed breakdown。 关键：这个数据与 plan_026 的 Llama SS 结果联合解读——Qwen 3-seed 稳定但 Llama 效果弱，整体 narrative 是 'SS works but with model-dependent variance'。\n\n\n3-seed 统计在 median 档下通过：AR GAR β=0 = 0.401±0.047 落在 [0.38, 0.45] 范围内。 β=3/5 的 std 极低（<0.01），说明高 β steering 效果跨 seed 极稳定——β-steering 是确定性推理时干预，不依赖训练 seed 的随机性。\ns42 是 β=0 的 outlier（0.347 vs 均值 0.401, -1.15σ），但 TF GAR 正常（0.503）， 说明 s42 的问题在 SS 学到的 AR 泛化能力而非训练收敛。这个 seed 变异性 在 median 档下被审稿人注意但不构成严重问题——s123 和 s456 一致性很好 （0.423 和 0.433），3-seed 的 47pp std 在 effect size（0.40 vs 0.016 baseline） 面前是可接受的。\nPPL 方差极低（±0.001），确认 SS 无 PPL 代价跨 seed 稳定。 这回应 W7：3 个 seed 提供了方差估计，effect size / std ratio ≈ 8.2 （(0.401-0.016)/0.047），远超统计显著阈值。\nMedian 档下审稿人的 remaining concern：'3 seeds is minimal for a key claim; would prefer 5+ seeds' 作为 minor request。不阻碍 acceptance 但可能 出现在 review 中。\n"
601	  },
602	  {
603	    "name": "Alternative GAR Definition Robustness",
604	    "description": "4 种 token selection（last/all/first/goal-only）× 3 checkpoints（Base/TG/SS）， 测试 SS 的改善是否跨 GAR 定义泛化。需要 GPU 重新计算 raw attention。\n",
605	    "results": {
606	      "base": {
607	        "last_token": 0.019,
608	        "all_token": 0.018,
609	        "first_token": 0.02,
610	        "goal_only": 0.012
611	      },
612	      "tg": {
613	        "last_token": 0.064,
614	        "all_token": 0.025,
615	        "first_token": 0.039,
616	        "goal_only": 0.015
617	      },
618	      "ss": {
619	        "last_token": 0.401,
620	        "all_token": 0.36,
621	        "first_token": 0.25,
622	        "goal_only": 0.06
623	      },
624	      "ss_improves_count": 3,
625	      "improved_definitions": [
626	        "last_token",
627	        "all_token",
628	        "first_token"
629	      ],
630	      "not_improved": [
631	        "goal_only"
632	      ],
633	      "tg_only_improves": [
634	        "last_token"
635	      ]
636	    },
637	    "tables": [
638	      {
639	        "name": "Table: Alternative GAR Definitions (AR Eval)",
640	        "columns": [
641	          "Token Selection",
642	          "Base",
643	          "TG",
644	          "SS",
645	          "SS Improves?"
646	        ],
647	        "rows": [
648	          [
649	            "Last (GAR-ours)",
650	            "0.019",
651	            "0.064",
652	            "0.401",
653	            "Yes (21×)"
654	          ],
655	          [
656	            "All response tokens",
657	            "0.018",
658	            "0.025",
659	            "0.360",
660	            "Yes (20×)"
661	          ],
662	          [
663	            "First response token",
664	            "0.020",
665	            "0.039",
666	            "0.250",
667	            "Yes (12.5×)"
668	          ],
669	          [
670	            "Goal-only tokens",
671	            "0.012",
672	            "0.015",
673	            "0.060",
674	            "No (5× but < threshold)"
675	          ]
676	        ]
677	      }
678	    ],
679	    "figures": [],
680	    "analysis": "3/4 定义改善在 median 档下是 'partially robust' 的证据。论文叙事： \"SS builds broader goal-attention patterns that generalize across multiple token selection criteria, unlike TG which only improves the trained definition (last-token). However, the most restrictive definition (goal-only) remains resistant, suggesting that SS corrects distributional mismatch but does not fully solve the goal-attention routing problem.\"\n这个实验在正文 §5.4 或 §6.4 中用 1 段 + 1 表报告，支撑 W5 回应 （mechanism specificity 和 定量 novelty）以及 SS contribution 的 nuanced claim。审稿人在 median 档可能用 goal-only 失败来 argue 'SS is superficial improvement' —— 回应：goal-only 是最严格的定义， even Dongre 的 all-token GAR-Dongre 也不要求 goal-only precision。\n\n\nMedian 档下 SS 改善 3/4 定义（落在 [2, 4] 范围）。\nLast-token (GAR-ours): SS 0.401 >> TG 0.064 >> Base 0.019。这是训练目标直接 优化的定义，改善最大。\nAll-token: SS 0.36 > TG 0.025 ≈ Base 0.018。SS 训练中 model-generated context 暴露迫使模型在更多 response token 位置维持 goal attention，不仅仅是 last token。 TG 在 all-token 上几乎无改善（0.025 vs 0.018），因为 TF 训练只优化了 last-token attention，其他位置没有学到 goal routing。\nFirst-token: SS 0.25 > TG 0.039 > Base 0.020。First-token attention 部分 受益于 SS 的 broader attention pattern 建设，但不如 all-token 因为 first-token 位置在训练中接收的 GAR signal 较弱。\nGoal-only: SS 0.06 ≈ TG 0.015 ≈ Base 0.012。Goal-only 定义最严格（仅 system prompt task tokens，不含 first user query），即使 SS 也无法显著改善—— 说明 goal-only attention 需要更精确的 routing，SS 的 distributional correction 不足以触及这个层面。在 median 档下，这个 '1 失败定义' 会被审稿人注意但 不构成严重问题（3/4 通过已足够说明 robustness）。\nTG 仅改善 last-token 这个事实确认了 TG 的 'position-specific overfitting'—— TG 只学到了在训练分布（TF）下的 last-token attention routing， 而 SS 构建了更广泛的 goal-attention pattern。这是一个有价值的对比发现。\n"
681	  },
682	  {
683	    "name": "SS 4th Seed (s789)",
684	    "description": "追加第 4 个 seed（s789）以缩窄 mean±std 的 CI。优先级 P2， 在 plan_026（Llama SS）之后若有 GPU 余量再跑。\n",
685	    "results": {
686	      "training": {
687	        "wall_clock_hours": 6.8,
688	        "final_loss": 0.932,
689	        "final_ntp_loss": 0.931,
690	        "final_gar_loss": 0.0008,
691	        "final_gate_mean": 0.948,
692	        "final_gate_std": 0.055
693	      },
694	      "eval_ar_beta0": {
695	        "gar_ours": 0.415,
696	        "ppl": 1.44
697	      },
698	      "eval_ar_beta3": {
699	        "gar_ours": 0.598
700	      },
701	      "eval_ar_beta5": {
702	        "gar_ours": 0.718
703	      },
704	      "updated_4seed_summary": {
705	        "ar_gar_beta0_mean": 0.405,
706	        "ar_gar_beta0_std": 0.04,
707	        "ar_gar_beta3_mean": 0.597,
708	        "ar_gar_beta3_std": 0.007,
709	        "ppl_mean": 1.441,
710	        "ppl_std": 0.001,
711	        "gap_mean": 1.24,
712	        "gap_range": "1.15–1.45×"
713	      },
714	      "ci_improvement": "std 从 0.047 降至 0.040（-15%）"
715	    },
716	    "tables": [
717	      {
718	        "name": "Table: 4-Seed Summary (Appendix)",
719	        "columns": [
720	          "Statistic",
721	          "3-Seed",
722	          "4-Seed",
723	          "Change"
724	        ],
725	        "rows": [
726	          [
727	            "Mean AR GAR β=0",
728	            "0.401",
729	            "0.405",
730	            "+0.004"
731	          ],
732	          [
733	            "Std AR GAR β=0",
734	            "0.047",
735	            "0.040",
736	            "-15%"
737	          ],
738	          [
739	            "Effect / Std",
740	            "8.2",
741	            "9.7",
742	            "+18%"
743	          ]
744	        ]
745	      }
746	    ],
747	    "figures": [],
748	    "analysis": "4th seed 在 median 档是 'nice to have' 而非 necessary。3-seed 已足以通过 统计检验（effect size / std > 8），4th seed 的边际统计改善（std -15%） 不太可能改变审稿人评分。GPU 时间优先分配给 Llama SS（plan_026）。 如果 plan_026 结果弱（median 档预期），论文需要靠 Qwen 统计稳健性 弥补跨模型弱点，此时 4th seed 的价值提升。\n\n\ns789 的 AR GAR β=0 = 0.415 落在现有 3-seed 范围内（0.347–0.433）， 更接近 s123/s456 的稳定区间，符合 s42 是 outlier 的判断。4-seed mean 从 0.401 微升至 0.405，std 从 0.047 降至 0.040。CI 收窄 15%， 改善是边际的——原本 3-seed effect size / std 已经 > 8，4th seed 主要价值是防御性的（回应 '3 seeds is minimal' 的审稿人 comment）。\nMedian 档下，这个实验的 ROI 低于 Llama SS（cross-model > extra seed）， 但如果 GPU 时间允许则值得做。审稿人不太可能因 3 vs 4 seeds 改变评分。\n"
749	  },
750	  {
751	    "name": "Long Conversation Eval (>10 turns)",
752	    "description": "测试 exposure bias gap 是否随对话长度加剧。从 UltraChat 找 >10 turn 对话，eval TG 和 SS 在长对话上的表现。\n",
753	    "results": {
754	      "data_source": "UltraChat filtered for >=12 turns, N=15 conversations",
755	      "turn_ranges": {
756	        "turns_3_5": {
757	          "base_ar_gar": 0.016,
758	          "tg_ar_gar": 0.042,
759	          "ss_ar_gar": 0.38,
760	          "tg_gap": 12.0,
761	          "ss_gap": 1.32
762	        },
763	        "turns_6_10": {
764	          "base_ar_gar": 0.01,
765	          "tg_ar_gar": 0.02,
766	          "ss_ar_gar": 0.32,
767	          "tg_gap": 25.0,
768	          "ss_gap": 1.56
769	        },
770	        "turns_11_15": {
771	          "base_ar_gar": 0.006,
772	          "tg_ar_gar": 0.011,
773	          "ss_ar_gar": 0.25,
774	          "tg_gap": 45.0,
775	          "ss_gap": 2.0
776	        }
777	      },
778	      "tg_tf_gar_stable": 0.5,
779	      "ss_tf_gar_stable": 0.5,
780	      "ppl_trend": "PPL increases modestly with turns (1.35→1.42→1.48)",
781	      "n_valid_long_convs": 15
782	    },
783	    "tables": [
784	      {
785	        "name": "Table: Gap vs Conversation Length",
786	        "columns": [
787	          "Turn Range",
788	          "Base AR GAR",
789	          "TG AR GAR",
790	          "SS AR GAR",
791	          "TG Gap",
792	          "SS Gap"
793	        ],
794	        "rows": [
795	          [
796	            "3–5",
797	            "0.016",
798	            "0.042",
799	            "0.38",
800	            "12×",
801	            "1.32×"
802	          ],
803	          [
804	            "6–10",
805	            "0.010",
806	            "0.020",
807	            "0.32",
808	            "25×",
809	            "1.56×"
810	          ],
811	          [
812	            "11–15",
813	            "0.006",
814	            "0.011",
815	            "0.25",
816	            "45×",
817	            "2.0×"
818	          ]
819	        ]
820	      }
821	    ],
822	    "figures": [],
823	    "analysis": "长对话 eval 在 median 档为 paper 提供了 'exposure bias compounds over turns' 的补充证据。TG gap 从 12× 扩大到 45× 直观有力——随 model-generated context 累积，分布偏移逐 turn 加剧。SS gap 也在增长（1.32→2.0×），暗示 SS 的 修正并非完美的——超出训练 turn 长度的泛化性有限。\n论文用途：§6.3 Distribution Shift Analysis 中用 1 段 + 1 图报告， 强调 \"gap grows with conversation length, consistent with cumulative distribution shift.\" 在 Discussion 中提及 SS 的 turn-length limitation 作为 future work direction。\n审稿人风险：median 档下不太可能是 rejection 理由（N=15 样本太小 无法做严格推断）。但如果审稿人要求 N=50 长对话 eval， 则需要寻找或生成更多 >10 turn 数据。\n\nExposure bias 效应随对话长度累积：每增加一个 turn，model-generated context 占比增大，训练-推理分布偏移加剧。\nTG gap 从 12×（turns 3-5）扩大到 45×（turns 11-15），因为 TF GAR 稳定在 0.50（不依赖对话长度——TF 条件下 context 始终是 gold text），而 AR GAR 持续衰减（0.042→0.020→0.011）。这是 exposure bias 累积效应的直接证据。\nSS gap 也从 1.32× 扩大到 2.0×（turns 11-15），但增速远慢于 TG。 SS 训练中暴露了 model-generated context，部分缓解了分布偏移， 但 SS 训练数据的最大 turn 数与 eval 不同（训练 ~10 turns，eval 15 turns）， 超出训练分布的 turns 泛化性下降。\n在 median 档下，这个实验提供了有价值但非关键的 supplementary evidence。 审稿人可能感兴趣但不太可能要求 15+ turns eval 作为必要条件。 数据限制：UltraChat 中 >10 turn 对话较少（filtered N=15）， 统计功效受限，结果仅作为 trend 报告而非 claim。\n"
824	  }
825	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d70b5363-a49c-47c4-a329-07f5a34e211c",
  "isSidechain": false,
  "promptId": "67a87842-f41b-4d9e-9fbd-faa3f9849a08",
  "type": "user",
  "uuid": "f182e9b8-9f51-4f63-97fe-89ba48d35ccd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Llama-3.1-8B Gradient Conflict Analysis\",\n    \"description\": \"对 Llama TG v7 的 3 个 epoch checkpoint 计算 NTP vs GAR gate 参数梯度的 cos_sim 和 magnitude ratio，验证 NTP-GAR 梯度竞争是否跨模型一致。\\n\",\n    \"results\": {\n      \"epoch0_cos_sim_mean\": 0.012,\n      \"epoch0_cos_sim_std\": 0.082,\n      \"epoch0_neg_layers_pct\": 50.0,\n      \"epoch0_mag_ratio_median\": 18.3,\n      \"epoch1_cos_sim_mean\": 0.003,\n      \"epoch1_cos_sim_std\": 0.068,\n      \"epoch1_neg_layers_pct\": 53.1,\n      \"epoch1_mag_ratio_median\": 24.5,\n      \"epoch2_cos_sim_mean\": 0.005,\n      \"epoch2_cos_sim_std\": 0.071,\n      \"epoch2_neg_layers_pct\": 53.1,\n      \"epoch2_mag_ratio_median\": 25.7,\n      \"overall_cos_sim\": 0.005,\n      \"overall_neg_layers_pct\": 53.1,\n      \"overall_mag_ratio_median\": 25.7\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-Model Gradient Analysis\",\n        \"columns\": [\n          \"Metric\",\n          \"Qwen-2.5-7B\",\n          \"Llama-3.1-8B\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"cos_sim (final epoch)\",\n            \"-0.042\",\n            \"+0.005\",\n            \"Qwen: mild conflict; Llama: orthogonal\"\n          ],\n          [\n            \"neg_layers %\",\n            \"67.9%\",\n            \"53.1%\",\n            \"Qwen: moderate asymmetry; Llama: near-random\"\n          ],\n          [\n            \"mag_ratio\",\n            \"14.7×\",\n            \"25.7×\",\n            \"Llama NTP dominance ~1.7× stronger\"\n          ],\n          [\n            \"TG AR GAR gap\",\n            \"8× (N=50)\",\n            \"27× (N=20 median)\",\n            \"Correlates with mag_ratio\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"跨模型梯度分析确认两个关键结论：(1) NTP-GAR 梯度方向不存在系统性冲突 （Llama 近乎正交，Qwen 轻度负相关），方向冲突不是 GAR collapse 的因果因素， 与 PCGrad 因果排除实验（plan_018）结论一致；(2) NTP 幅度主导是跨模型一致的 结构性特征（Qwen 7.5–14.7×, Llama 25.7×），且幅度主导程度与 TG 推理 gap 大小正相关。在 median 档叙事中，这个实验支撑 C3（失败机制因果分析）的 跨模型泛化性，且 Llama 的更极端 mag_ratio 为 Llama SS 效果更弱提供了 事前预测基础。Paper §6.5 Cross-Model Replication 需要报告此数据。 审稿人可能视此为 'expected result'（NTP 主导不意外），但 25.7× 这个数值 本身有定量参考价值。\\n\\n\\nLlama-3.1-8B 采用 GQA（8 KV heads）+ 32 层架构，比 Qwen-2.5-7B（28 层）更深。 cos_sim ≈ 0 表示 NTP 和 GAR 梯度近乎正交而非冲突——这与 Qwen 的轻度负相关 （cos_sim -0.042 to -0.089）有微妙差异但结论一致：方向冲突不是 GAR collapse 的 因果因素。neg_layers ≈ 53%（接近随机 50%）进一步确认无系统性冲突。 mag_ratio 25.7× 显著高于 Qwen 的 7.5–14.7×，原因是 Llama 更深的网络使 NTP 梯度 有更多反向传播路径累积幅度。这解释了 Llama 上 TG gap 更大（27× vs 8×）： NTP 幅度主导更极端，gate 更难学到有意义的 GAR-oriented 行为。\\n\"\n  },\n  {\n    \"name\": \"Expanded Eval Set (N=200 TF + N=50 AR)\",\n    \"description\": \"将 TF eval 从 N=50 扩展到 N=200（idx>=7000 from UltraChat）， 提升 bootstrap CI 统计功效。AR eval 保持 N=50（extreme effect size 下已充分）。\\n\",\n    \"results\": {\n      \"tf_tg_gar_ours_n200\": 0.5042,\n      \"tf_tg_gar_ours_ci95\": [\n        0.4891,\n        0.5193\n      ],\n      \"tf_ug_gar_ours_n200\": 0.5061,\n      \"tf_lo_gar_ours_n200\": 0.4985,\n      \"tf_base_gar_ours_n200\": 0.0131,\n      \"tf_tg_ppl_n200\": 2.78,\n      \"tf_tg_dongre_n200\": 0.0148,\n      \"bootstrap_ci_tg_vs_lo_gar\": [\n        -0.0012,\n        0.0028\n      ],\n      \"bootstrap_ci_tg_vs_ug_gar\": [\n        -0.0022,\n        0.0005\n      ],\n      \"bootstrap_ci_includes_zero\": true,\n      \"ci_width_reduction_vs_n50\": 0.42\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: TF Eval N=200 Summary\",\n        \"columns\": [\n          \"Variant\",\n          \"GAR-ours\",\n          \"95% CI\",\n          \"GAR-Dongre\",\n          \"PPL\"\n        ],\n        \"rows\": [\n          [\n            \"Base\",\n            \"0.013\",\n            \"[0.010, 0.016]\",\n            \"0.003\",\n            \"4.34\"\n          ],\n          [\n            \"ThreadGate\",\n            \"0.504\",\n            \"[0.489, 0.519]\",\n            \"0.015\",\n            \"2.78\"\n          ],\n          [\n            \"Uniform Gate\",\n            \"0.506\",\n            \"[0.491, 0.521]\",\n            \"0.012\",\n            \"2.78\"\n          ],\n          [\n            \"LoRA-only\",\n            \"0.499\",\n            \"[0.483, 0.514]\",\n            \"0.013\",\n            \"2.78\"\n          ],\n          [\n            \"TG-LO diff\",\n            \"+0.006\",\n            \"[-0.001, 0.003]\",\n            \"+0.002\",\n            \"0.00\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"N=200 eval 是纯统计功效提升，不改变任何定性结论。在 median 档下，这个实验 的价值是堵住 W7 reviewer concern 的 one-liner：\\\"N=200 TF CI confirms zero gating benefit with narrower intervals.\\\" AR eval 保持 N=50 因为 8×–27× gap 的 effect size 足以在小样本下达到统计显著。审稿人在 median 档仍可能提 'would be nice to see AR N=200'，但不太可能构成 rejection 理由。\\n\\n\\nN=200 TF eval 提供 4× 样本量（vs N=50），bootstrap CI 宽度按 √(50/200) ≈ 0.5 缩窄约一半。TG-LO GAR 差异 CI 仍包含 0，进一步强化 'zero gating benefit' 结论。 点估计与 N=50 eval（plan_008）一致（TG 0.504, UG 0.505, LO 0.498）， 因为 UltraChat idx>=7000 与 idx>=8000 的分布几乎相同。PPL 和 GAR-Dongre 同样一致。审稿人 W7（单 seed / 统计不足）的回应因此更有力：极端效应量 （GAR-ours TF 0.50 vs AR 0.016）在 N=200 下 CI 不包含 parity。 但 median 档下审稿人仍可能提 'more seeds' 作为 minor concern。\\n\"\n  },\n  {\n    \"name\": \"λ_GAR Sensitivity (λ=10, 1 epoch)\",\n    \"description\": \"训练 v7 with λ_GAR=10（10× 默认值），测试提高 GAR loss 权重能否改善 gate 学习和 AR GAR。仅跑 1 epoch 以节省 GPU。若预算允许追加 λ=0.1。\\n\",\n    \"results\": {\n      \"lambda10_training\": {\n        \"epoch1_avg_loss\": 1.012,\n        \"epoch1_avg_ntp\": 0.946,\n        \"epoch1_avg_gar\": 0.0066,\n        \"gate_mean\": 0.905,\n        \"gate_std\": 0.082,\n        \"gate_min\": 0.68,\n        \"gate_max\": 0.996,\n        \"wall_clock_hours\": 2.1\n      },\n      \"lambda10_eval_iid\": {\n        \"gar_ours\": 0.535,\n        \"gar_dongre\": 0.018,\n        \"ppl\": 2.95\n      },\n      \"lambda10_eval_ar\": {\n        \"gar_ours\": 0.024,\n        \"gar_dongre\": 0.019,\n        \"ppl\": 1.41\n      },\n      \"lambda10_gap_ratio\": 22.3,\n      \"lambda01_training\": {\n        \"epoch1_avg_loss\": 0.978,\n        \"epoch1_avg_ntp\": 0.977,\n        \"epoch1_avg_gar\": 0.001,\n        \"gate_mean\": 0.972,\n        \"gate_std\": 0.022\n      },\n      \"lambda01_eval_iid\": {\n        \"gar_ours\": 0.42,\n        \"gar_dongre\": 0.011,\n        \"ppl\": 2.76\n      },\n      \"lambda01_eval_ar\": {\n        \"gar_ours\": 0.013,\n        \"gar_dongre\": 0.016,\n        \"ppl\": 1.38\n      },\n      \"lambda01_gap_ratio\": 32.3,\n      \"v7_reference_gap_ratio\": 32.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: λ_GAR Sensitivity\",\n        \"columns\": [\n          \"λ_GAR\",\n          \"TF GAR-ours\",\n          \"AR GAR-ours\",\n          \"Gap\",\n          \"IID PPL\",\n          \"Gate Mean\"\n        ],\n        \"rows\": [\n          [\n            \"0.1\",\n            \"0.42\",\n            \"0.013\",\n            \"32.3×\",\n            \"2.76\",\n            \"0.972\"\n          ],\n          [\n            \"1.0 (v7)\",\n            \"0.50\",\n            \"0.016\",\n            \"32.1×\",\n            \"2.78\",\n            \"0.934\"\n          ],\n          [\n            \"10.0\",\n            \"0.535\",\n            \"0.024\",\n            \"22.3×\",\n            \"2.95\",\n            \"0.905\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"λ_GAR sensitivity 实验在 median 档扮演辅助角色：它不是核心 contribution 但 强化 W2 回应——\\\"你只是没调对参数\\\"。10× λ 使 GAR 梯度与 NTP 量级相当， gate 获得更大动态范围（std 0.082 vs 0.049），TF 性能确实提升（+3.5pp）， 但 AR GAR 仅微升 0.8pp，gap 仍 22×。这表明 gradient magnitude 不是瓶颈， exposure bias 是。Paper 中作为 Appendix λ-sensitivity 表格，正文一句引用： \\\"Even with 10× GAR weight (Table X), the TF–AR gap remains >20×, confirming that distribution shift, not gradient competition, is the limiting factor.\\\" 在 median 档下，审稿人可能视此为 'unsurprising follow-up' 但不会反对。\\n\\n\\nλ_GAR=10 将 GAR 梯度幅度提升 10×，使有效 NTP/GAR ratio 从 7.5–14.7× 降至 0.75–1.47×——两者量级相当。结果：(1) TF GAR 从 0.50 提升到 0.535（GAR 获得 更多优化预算，gate 学到更强的注意力干预）；(2) gate_mean 从 0.93 降至 0.905, gate_std 从 0.049 提升到 0.082——gate 获得更大动态范围；(3) 但 AR GAR 仅从 0.016 微升到 0.024（仍然近乎 collapse，22× gap）。这是 median 档的关键证据： 梯度幅度平衡后 exposure bias gap 仍然巨大，直接排除 'gradient competition is the bottleneck' 假说。PPL 从 2.78 升至 2.95（+6%），因为 NTP 获得相对更少 优化预算。λ=0.1 方向上 gate 几乎冻结（gate_mean 0.972），gap 32×，接近 v7。 三点（λ=0.1/1.0/10）构成 λ sensitivity curve，在 Appendix 中报告。\\n\"\n  },\n  {\n    \"name\": \"TF vs AR Attention KL Divergence\",\n    \"description\": \"对 50 conversations 计算 per-head KL(P_TF || P_AR) 量化注意力分布偏移。 分析 GAR-relevant heads 是否表现出更大的 KL。纯 CPU 分析。\\n\",\n    \"results\": {\n      \"tg_mean_kl_all_heads\": 0.054,\n      \"base_mean_kl_all_heads\": 0.043,\n      \"tg_kl_std\": 0.032,\n      \"base_kl_std\": 0.028,\n      \"high_kl_layers\": \"L23-L27, L9\",\n      \"high_kl_heads_top5\": \"L25H3, L27H1, L24H2, L9H0, L23H3\",\n      \"gate_kl_correlation\": 0.11,\n      \"gar_robustness_by_definition\": {\n        \"gar_ours_tg_over_base_ratio\": 21.4,\n        \"gar_goal_only_ratio\": 63.0,\n        \"gar_all_token_ratio\": 1.7,\n        \"gar_first_token_ratio\": 1.8\n      },\n      \"kl_percentile_95\": 0.142,\n      \"kl_percentile_99\": 0.198,\n      \"n_conversations\": 50,\n      \"n_heads_total\": 112\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: KL Divergence by Layer Group\",\n        \"columns\": [\n          \"Layer Group\",\n          \"TG Mean KL\",\n          \"Base Mean KL\",\n          \"TG/Base Ratio\"\n        ],\n        \"rows\": [\n          [\n            \"L0-L6 (shallow)\",\n            \"0.031\",\n            \"0.028\",\n            \"1.11\"\n          ],\n          [\n            \"L7-L13 (lower-mid)\",\n            \"0.042\",\n            \"0.036\",\n            \"1.17\"\n          ],\n          [\n            \"L14-L20 (upper-mid)\",\n            \"0.058\",\n            \"0.045\",\n            \"1.29\"\n          ],\n          [\n            \"L21-L27 (deep)\",\n            \"0.089\",\n            \"0.065\",\n            \"1.37\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: GAR Definition Sensitivity to Attention Shift\",\n        \"columns\": [\n          \"GAR Definition\",\n          \"TG TF\",\n          \"TG AR\",\n          \"TG TF/AR Gap\",\n          \"Sensitivity\"\n        ],\n        \"rows\": [\n          [\n            \"GAR-ours (last token)\",\n            \"0.504\",\n            \"0.016\",\n            \"32×\",\n            \"High\"\n          ],\n          [\n            \"GAR goal-only\",\n            \"0.630\",\n            \"0.010\",\n            \"63×\",\n            \"Very High\"\n          ],\n          [\n            \"GAR all-token\",\n            \"0.028\",\n            \"0.016\",\n            \"1.7×\",\n            \"Low\"\n          ],\n          [\n            \"GAR first-token\",\n            \"0.035\",\n            \"0.019\",\n            \"1.8×\",\n            \"Low\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"KL 分析在 median 档提供了 exposure bias 的注意力空间机制证据：分布偏移 在深层注意力头最严重（mean KL 0.089 vs 浅层 0.031），恰好是负责 long-range goal-attention routing 的层。GAR-ours 的 21.4× 敏感度 vs all-token 的 1.7× 解释了 mechanism specificity——为什么 exposure bias '选择性' 摧毁 summary-position attention。这个分析不需要额外 GPU，是 pure diagnostic，在 median 档下 审稿人会认为是 'nice additional evidence' 但不太可能改变评分。 Paper §6.4 Mechanism Specificity 使用此数据。\\n\\n\\nTF vs AR 注意力分布的 KL 散度量化了 exposure bias 在注意力空间的具体表现。 TG 模型的 mean KL（0.054）高于 base（0.043），因为 TG 训练在 TF 条件下 专门塑造了注意力 pattern（GAR-ours 0.50），这些 pattern 在 AR 条件下偏移更大。 高 KL 集中在 L23-L27（深层 attention heads），与 gate profile 中这些层 gate value 最低（Llama L25=0.719）一致——gates 试图在这些层做最多干预， 恰好也是 TF-AR 分布偏移最大的层。Gate-KL 相关仅 0.11，说明 gate 没有学到 track distribution shift 的能力。GAR-ours（last-token）对 KL 的敏感度 21.4× 远高于 all-token（1.7×）和 first-token（1.8×），解释了为什么 exposure bias 选择性摧毁 summary-position attention：last-token attention 更依赖远程 context 质量，而 all/first-token 的 attention 更局部、更鲁棒。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B Scheduled Sampling Training + Eval\",\n    \"description\": \"在 Llama-3.1-8B 上复现 SS 训练（linear schedule 0→0.5 over 3 epochs）， 测试 SS gap 压缩能否跨模型泛化。这是 median 档最关键的实验—— 决定 SS 是 'general mitigation' 还是 'model-dependent'。\\n\",\n    \"results\": {\n      \"training\": {\n        \"total_steps\": 3000,\n        \"epochs_completed\": 3,\n        \"wall_clock_hours\": 10.8,\n        \"final_loss\": 0.927,\n        \"final_ntp_loss\": 0.926,\n        \"final_gar_loss\": 0.0009,\n        \"final_gate_mean\": 0.925,\n        \"final_gate_std\": 0.065,\n        \"final_gate_min\": 0.705,\n        \"ss_ratio_final\": 0.5,\n        \"ss_fallback_count\": 12,\n        \"gpu_mem_gb\": 71.2\n      },\n      \"eval_tf\": {\n        \"gar_ours\": 0.485,\n        \"gar_dongre\": 0.38,\n        \"ppl\": 2.6,\n        \"n_conversations\": 50\n      },\n      \"eval_ar_beta0\": {\n        \"gar_ours\": 0.18,\n        \"gar_ours_std\": 0.09,\n        \"gar_dongre\": 0.25,\n        \"ppl\": 1.4,\n        \"n_conversations\": 20\n      },\n      \"eval_ar_beta3\": {\n        \"gar_ours\": 0.45,\n        \"ppl\": 1.55\n      },\n      \"eval_ar_beta5\": {\n        \"gar_ours\": 0.62,\n        \"ppl\": 1.72\n      },\n      \"gap_ratio_beta0\": 2.7,\n      \"gap_ratio_vs_tg_no_ss\": 15.9,\n      \"improvement_over_tg_baseline\": \"10× (0.018→0.18)\",\n      \"improvement_over_qwen_ss_comparison\": \"0.45× (0.18 vs Qwen 0.40)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-Model SS Comparison (Key Paper Table)\",\n        \"columns\": [\n          \"Metric\",\n          \"Qwen-2.5-7B\",\n          \"Llama-3.1-8B\",\n          \"Cross-Model Ratio\"\n        ],\n        \"rows\": [\n          [\n            \"Base AR GAR\",\n            \"0.019\",\n            \"0.009\",\n            \"2.1×\"\n          ],\n          [\n            \"TG AR GAR (no SS)\",\n            \"0.064\",\n            \"0.018\",\n            \"3.6×\"\n          ],\n          [\n            \"SS AR GAR β=0\",\n            \"0.401±0.047\",\n            \"0.18±0.09\",\n            \"2.2×\"\n          ],\n          [\n            \"SS AR GAR β=3\",\n            \"0.596±0.008\",\n            \"0.45\",\n            \"1.3×\"\n          ],\n          [\n            \"SS AR GAR β=5\",\n            \"0.717±0.001\",\n            \"0.62\",\n            \"1.2×\"\n          ],\n          [\n            \"TF GAR\",\n            \"0.498±0.004\",\n            \"0.485\",\n            \"1.03×\"\n          ],\n          [\n            \"SS Gap (TF/AR β=0)\",\n            \"1.26×\",\n            \"2.7×\",\n            \"-\"\n          ],\n          [\n            \"TG Gap (no SS)\",\n            \"32×\",\n            \"27× (median)\",\n            \"-\"\n          ],\n          [\n            \"SS PPL β=0\",\n            \"1.441\",\n            \"1.40\",\n            \"1.03×\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Llama SS vs Llama TG Comparison\",\n        \"columns\": [\n          \"Condition\",\n          \"AR GAR-ours\",\n          \"AR GAR-Dongre\",\n          \"PPL\",\n          \"Improvement\"\n        ],\n        \"rows\": [\n          [\n            \"Base\",\n            \"0.009\",\n            \"0.005\",\n            \"1.27\",\n            \"—\"\n          ],\n          [\n            \"TG (no SS)\",\n            \"0.018\",\n            \"0.018\",\n            \"1.32\",\n            \"2× over base\"\n          ],\n          [\n            \"LO (no SS)\",\n            \"0.018\",\n            \"0.020\",\n            \"1.32\",\n            \"2× over base\"\n          ],\n          [\n            \"SS β=0\",\n            \"0.18\",\n            \"0.25\",\n            \"1.40\",\n            \"20× over base\"\n          ],\n          [\n            \"SS β=3\",\n            \"0.45\",\n            \"0.38\",\n            \"1.55\",\n            \"50× over base\"\n          ],\n          [\n            \"SS β=5\",\n            \"0.62\",\n            \"0.48\",\n            \"1.72\",\n            \"69× over base\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama SS 是 median 档的 defining experiment。结果构成 'partial success' 叙事： SS 在 Llama 上有效（20× over base, gap 从 27× 压缩到 2.7×），但效果显著 弱于 Qwen（gap 2.7× vs 1.3×, AR GAR 0.18 vs 0.40）。这决定了论文 Contribution #5 的措辞必须弱化为 'model-dependent efficacy'，SS 从 'general mitigation' 降级为 'promising but requires further validation'。\\n论文需要在 Discussion 中增加 'Limitations of SS Transferability' 段落，分析 架构差异（GQA head 数量、层数、attention sink 强度）作为可能原因， 并建议未来工作探索 model-specific SS schedule 调优。\\n积极面：即使在 Llama 上，SS β=0 的 0.18 也远优于 TG 无 SS 的 0.018， 证明 SS 的方向是正确的。β-steering 仍然有效，β=5 时 Llama 达到 0.62 （Qwen 0.72），高 β 下两模型趋同，说明推理时干预的跨模型泛化性好于 训练时 SS 的泛化性。这个 insight 本身有 discussion 价值。\\n审稿人视角：median 档下，至少 1 位审稿人会将 Llama SS 结果视为 'weakness' （SS 不 general），可能降低 contribution 评分。回应策略：(1) SS 方向正确 但 model-specific tuning needed；(2) 核心 contribution 是诊断（8×–27× gap + PCGrad）不依赖 SS 跨模型；(3) SS 作为 'initial evidence, not claim of generality'。\\n\\n\\nLlama SS 在 median 档展现 'partial success'：AR GAR β=0 = 0.18，相比 Llama TG 无 SS 的 0.018（median）改善了 10×，但远逊于 Qwen SS 的 0.40。 Gap 从 TG 的 27×（median）压缩到 2.7×，但 Qwen SS 压缩到 ~1.3×。\\n效果减弱的原因分析： (1) 架构差异：Llama GQA 使用 8 KV heads（vs Qwen 的不同 KV 配置），\\n    attention head 更少意味着 goal-relevant routing 的容量更受限，\\n    SS 修正训练分布后能利用的 head 容量上限更低。\\n(2) NTP 幅度主导更极端：Llama mag_ratio 25.7×（vs Qwen 14.7×），\\n    即使 SS 缩小了分布偏移，gates 仍然在更强的 NTP 压力下学习。\\n(3) 基线 gap 更大：Llama 的原始 TG gap 27×（vs Qwen 8×），\\n    说明 Llama 的注意力 pattern 对 context 分布更敏感，\\n    SS 能部分补偿但无法完全克服这种固有脆弱性。\\n(4) 32 层 vs 28 层：更多层意味着更多 gate-NTP 交互点，\\n    SS 的修正信号被稀释。\\n\\nPPL 1.40 与 Llama TG 的 1.32 接近（+6%），说明 SS 没有显著 PPL 代价。 β-steering 仍然有效（β=5: 0.62），说明推理时干预在 Llama 上也 work。\\n\"\n  },\n  {\n    \"name\": \"SS 3-Seed Validation (Qwen)\",\n    \"description\": \"Qwen SS 三个 seed（s42, s123, s456）的训练 + eval，提供 mean±std 统计。 回应 W7（单 seed 无方差估计）。\\n\",\n    \"results\": {\n      \"per_seed_tf_gar\": {\n        \"s42\": 0.503,\n        \"s123\": 0.495,\n        \"s456\": 0.496\n      },\n      \"per_seed_ar_gar_beta0\": {\n        \"s42\": 0.347,\n        \"s123\": 0.423,\n        \"s456\": 0.433\n      },\n      \"per_seed_ar_gar_beta3\": {\n        \"s42\": 0.593,\n        \"s123\": 0.59,\n        \"s456\": 0.605\n      },\n      \"per_seed_ar_gar_beta5\": {\n        \"s42\": 0.717,\n        \"s123\": 0.717,\n        \"s456\": 0.716\n      },\n      \"per_seed_ppl_beta0\": {\n        \"s42\": 1.442,\n        \"s123\": 1.441,\n        \"s456\": 1.439\n      },\n      \"three_seed_summary\": {\n        \"tf_gar_mean\": 0.498,\n        \"tf_gar_std\": 0.004,\n        \"ar_gar_beta0_mean\": 0.401,\n        \"ar_gar_beta0_std\": 0.047,\n        \"ar_gar_beta3_mean\": 0.596,\n        \"ar_gar_beta3_std\": 0.008,\n        \"ar_gar_beta5_mean\": 0.717,\n        \"ar_gar_beta5_std\": 0.001,\n        \"ppl_mean\": 1.441,\n        \"ppl_std\": 0.001,\n        \"gap_mean\": 1.26,\n        \"gap_std\": 0.17,\n        \"gap_range\": \"1.15–1.45×\"\n      },\n      \"outlier_analysis\": {\n        \"s42_is_beta0_outlier\": true,\n        \"s42_ar_gar_deviation\": \"-1.15σ from mean\",\n        \"s42_tf_gar_normal\": true,\n        \"s42_note\": \"s42 在 β=0 偏低但 β≥3 正常，说明 s42 的 SS 训练在低 β 泛化稍弱\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: SS 3-Seed Results\",\n        \"columns\": [\n          \"Seed\",\n          \"TF GAR\",\n          \"AR GAR β=0\",\n          \"AR GAR β=3\",\n          \"AR GAR β=5\",\n          \"PPL β=0\",\n          \"Gap\"\n        ],\n        \"rows\": [\n          [\n            \"s42\",\n            \"0.503\",\n            \"0.347\",\n            \"0.593\",\n            \"0.717\",\n            \"1.442\",\n            \"1.45×\"\n          ],\n          [\n            \"s123\",\n            \"0.495\",\n            \"0.423\",\n            \"0.590\",\n            \"0.717\",\n            \"1.441\",\n            \"1.17×\"\n          ],\n          [\n            \"s456\",\n            \"0.496\",\n            \"0.433\",\n            \"0.605\",\n            \"0.716\",\n            \"1.439\",\n            \"1.15×\"\n          ],\n          [\n            \"Mean±Std\",\n            \"0.498±0.004\",\n            \"0.401±0.047\",\n            \"0.596±0.008\",\n            \"0.717±0.001\",\n            \"1.441±0.001\",\n            \"1.26±0.17\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"3-seed 在 median 档为 SS claim 提供了最低限度的统计支撑。AR GAR 0.401±0.047 在 Qwen 上确认 SS 是有效的（effect size / std > 8），但 s42 的 outlier 行为 暗示 SS 的低 β 泛化性存在 seed sensitivity。论文应报告完整 3-seed 数据， 在正文用 mean±std，附录报告 per-seed breakdown。 关键：这个数据与 plan_026 的 Llama SS 结果联合解读——Qwen 3-seed 稳定但 Llama 效果弱，整体 narrative 是 'SS works but with model-dependent variance'。\\n\\n\\n3-seed 统计在 median 档下通过：AR GAR β=0 = 0.401±0.047 落在 [0.38, 0.45] 范围内。 β=3/5 的 std 极低（<0.01），说明高 β steering 效果跨 seed 极稳定——β-steering 是确定性推理时干预，不依赖训练 seed 的随机性。\\ns42 是 β=0 的 outlier（0.347 vs 均值 0.401, -1.15σ），但 TF GAR 正常（0.503）， 说明 s42 的问题在 SS 学到的 AR 泛化能力而非训练收敛。这个 seed 变异性 在 median 档下被审稿人注意但不构成严重问题——s123 和 s456 一致性很好 （0.423 和 0.433），3-seed 的 47pp std 在 effect size（0.40 vs 0.016 baseline） 面前是可接受的。\\nPPL 方差极低（±0.001），确认 SS 无 PPL 代价跨 seed 稳定。 这回应 W7：3 个 seed 提供了方差估计，effect size / std ratio ≈ 8.2 （(0.401-0.016)/0.047），远超统计显著阈值。\\nMedian 档下审稿人的 remaining concern：'3 seeds is minimal for a key claim; would prefer 5+ seeds' 作为 minor request。不阻碍 acceptance 但可能 出现在 review 中。\\n\"\n  },\n  {\n    \"name\": \"Alternative GAR Definition Robustness\",\n    \"description\": \"4 种 token selection（last/all/first/goal-only）× 3 checkpoints（Base/TG/SS）， 测试 SS 的改善是否跨 GAR 定义泛化。需要 GPU 重新计算 raw attention。\\n\",\n    \"results\": {\n      \"base\": {\n        \"last_token\": 0.019,\n        \"all_token\": 0.018,\n        \"first_token\": 0.02,\n        \"goal_only\": 0.012\n      },\n      \"tg\": {\n        \"last_token\": 0.064,\n        \"all_token\": 0.025,\n        \"first_token\": 0.039,\n        \"goal_only\": 0.015\n      },\n      \"ss\": {\n        \"last_token\": 0.401,\n        \"all_token\": 0.36,\n        \"first_token\": 0.25,\n        \"goal_only\": 0.06\n      },\n      \"ss_improves_count\": 3,\n      \"improved_definitions\": [\n        \"last_token\",\n        \"all_token\",\n        \"first_token\"\n      ],\n      \"not_improved\": [\n        \"goal_only\"\n      ],\n      \"tg_only_improves\": [\n        \"last_token\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Alternative GAR Definitions (AR Eval)\",\n        \"columns\": [\n          \"Token Selection\",\n          \"Base\",\n          \"TG\",\n          \"SS\",\n          \"SS Improves?\"\n        ],\n        \"rows\": [\n          [\n            \"Last (GAR-ours)\",\n            \"0.019\",\n            \"0.064\",\n            \"0.401\",\n            \"Yes (21×)\"\n          ],\n          [\n            \"All response tokens\",\n            \"0.018\",\n            \"0.025\",\n            \"0.360\",\n            \"Yes (20×)\"\n          ],\n          [\n            \"First response token\",\n            \"0.020\",\n            \"0.039\",\n            \"0.250\",\n            \"Yes (12.5×)\"\n          ],\n          [\n            \"Goal-only tokens\",\n            \"0.012\",\n            \"0.015\",\n            \"0.060\",\n            \"No (5× but < threshold)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"3/4 定义改善在 median 档下是 'partially robust' 的证据。论文叙事： \\\"SS builds broader goal-attention patterns that generalize across multiple token selection criteria, unlike TG which only improves the trained definition (last-token). However, the most restrictive definition (goal-only) remains resistant, suggesting that SS corrects distributional mismatch but does not fully solve the goal-attention routing problem.\\\"\\n这个实验在正文 §5.4 或 §6.4 中用 1 段 + 1 表报告，支撑 W5 回应 （mechanism specificity 和 定量 novelty）以及 SS contribution 的 nuanced claim。审稿人在 median 档可能用 goal-only 失败来 argue 'SS is superficial improvement' —— 回应：goal-only 是最严格的定义， even Dongre 的 all-token GAR-Dongre 也不要求 goal-only precision。\\n\\n\\nMedian 档下 SS 改善 3/4 定义（落在 [2, 4] 范围）。\\nLast-token (GAR-ours): SS 0.401 >> TG 0.064 >> Base 0.019。这是训练目标直接 优化的定义，改善最大。\\nAll-token: SS 0.36 > TG 0.025 ≈ Base 0.018。SS 训练中 model-generated context 暴露迫使模型在更多 response token 位置维持 goal attention，不仅仅是 last token。 TG 在 all-token 上几乎无改善（0.025 vs 0.018），因为 TF 训练只优化了 last-token attention，其他位置没有学到 goal routing。\\nFirst-token: SS 0.25 > TG 0.039 > Base 0.020。First-token attention 部分 受益于 SS 的 broader attention pattern 建设，但不如 all-token 因为 first-token 位置在训练中接收的 GAR signal 较弱。\\nGoal-only: SS 0.06 ≈ TG 0.015 ≈ Base 0.012。Goal-only 定义最严格（仅 system prompt task tokens，不含 first user query），即使 SS 也无法显著改善—— 说明 goal-only attention 需要更精确的 routing，SS 的 distributional correction 不足以触及这个层面。在 median 档下，这个 '1 失败定义' 会被审稿人注意但 不构成严重问题（3/4 通过已足够说明 robustness）。\\nTG 仅改善 last-token 这个事实确认了 TG 的 'position-specific overfitting'—— TG 只学到了在训练分布（TF）下的 last-token attention routing， 而 SS 构建了更广泛的 goal-attention pattern。这是一个有价值的对比发现。\\n\"\n  },\n  {\n    \"name\": \"SS 4th Seed (s789)\",\n    \"description\": \"追加第 4 个 seed（s789）以缩窄 mean±std 的 CI。优先级 P2， 在 plan_026（Llama SS）之后若有 GPU 余量再跑。\\n\",\n    \"results\": {\n      \"training\": {\n        \"wall_clock_hours\": 6.8,\n        \"final_loss\": 0.932,\n        \"final_ntp_loss\": 0.931,\n        \"final_gar_loss\": 0.0008,\n        \"final_gate_mean\": 0.948,\n        \"final_gate_std\": 0.055\n      },\n      \"eval_ar_beta0\": {\n        \"gar_ours\": 0.415,\n        \"ppl\": 1.44\n      },\n      \"eval_ar_beta3\": {\n        \"gar_ours\": 0.598\n      },\n      \"eval_ar_beta5\": {\n        \"gar_ours\": 0.718\n      },\n      \"updated_4seed_summary\": {\n        \"ar_gar_beta0_mean\": 0.405,\n        \"ar_gar_beta0_std\": 0.04,\n        \"ar_gar_beta3_mean\": 0.597,\n        \"ar_gar_beta3_std\": 0.007,\n        \"ppl_mean\": 1.441,\n        \"ppl_std\": 0.001,\n        \"gap_mean\": 1.24,\n        \"gap_range\": \"1.15–1.45×\"\n      },\n      \"ci_improvement\": \"std 从 0.047 降至 0.040（-15%）\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 4-Seed Summary (Appendix)\",\n        \"columns\": [\n          \"Statistic\",\n          \"3-Seed\",\n          \"4-Seed\",\n          \"Change\"\n        ],\n        \"rows\": [\n          [\n            \"Mean AR GAR β=0\",\n            \"0.401\",\n            \"0.405\",\n            \"+0.004\"\n          ],\n          [\n            \"Std AR GAR β=0\",\n            \"0.047\",\n            \"0.040\",\n            \"-15%\"\n          ],\n          [\n            \"Effect / Std\",\n            \"8.2\",\n            \"9.7\",\n            \"+18%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"4th seed 在 median 档是 'nice to have' 而非 necessary。3-seed 已足以通过 统计检验（effect size / std > 8），4th seed 的边际统计改善（std -15%） 不太可能改变审稿人评分。GPU 时间优先分配给 Llama SS（plan_026）。 如果 plan_026 结果弱（median 档预期），论文需要靠 Qwen 统计稳健性 弥补跨模型弱点，此时 4th seed 的价值提升。\\n\\n\\ns789 的 AR GAR β=0 = 0.415 落在现有 3-seed 范围内（0.347–0.433）， 更接近 s123/s456 的稳定区间，符合 s42 是 outlier 的判断。4-seed mean 从 0.401 微升至 0.405，std 从 0.047 降至 0.040。CI 收窄 15%， 改善是边际的——原本 3-seed effect size / std 已经 > 8，4th seed 主要价值是防御性的（回应 '3 seeds is minimal' 的审稿人 comment）。\\nMedian 档下，这个实验的 ROI 低于 Llama SS（cross-model > extra seed）， 但如果 GPU 时间允许则值得做。审稿人不太可能因 3 vs 4 seeds 改变评分。\\n\"\n  },\n  {\n    \"name\": \"Long Conversation Eval (>10 turns)\",\n    \"description\": \"测试 exposure bias gap 是否随对话长度加剧。从 UltraChat 找 >10 turn 对话，eval TG 和 SS 在长对话上的表现。\\n\",\n    \"results\": {\n      \"data_source\": \"UltraChat filtered for >=12 turns, N=15 conversations\",\n      \"turn_ranges\": {\n        \"turns_3_5\": {\n          \"base_ar_gar\": 0.016,\n          \"tg_ar_gar\": 0.042,\n          \"ss_ar_gar\": 0.38,\n          \"tg_gap\": 12.0,\n          \"ss_gap\": 1.32\n        },\n        \"turns_6_10\": {\n          \"base_ar_gar\": 0.01,\n          \"tg_ar_gar\": 0.02,\n          \"ss_ar_gar\": 0.32,\n          \"tg_gap\": 25.0,\n          \"ss_gap\": 1.56\n        },\n        \"turns_11_15\": {\n          \"base_ar_gar\": 0.006,\n          \"tg_ar_gar\": 0.011,\n          \"ss_ar_gar\": 0.25,\n          \"tg_gap\": 45.0,\n          \"ss_gap\": 2.0\n        }\n      },\n      \"tg_tf_gar_stable\": 0.5,\n      \"ss_tf_gar_stable\": 0.5,\n      \"ppl_trend\": \"PPL increases modestly with turns (1.35→1.42→1.48)\",\n      \"n_valid_long_convs\": 15\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Gap vs Conversation Length\",\n        \"columns\": [\n          \"Turn Range\",\n          \"Base AR GAR\",\n          \"TG AR GAR\",\n          \"SS AR GAR\",\n          \"TG Gap\",\n          \"SS Gap\"\n        ],\n        \"rows\": [\n          [\n            \"3–5\",\n            \"0.016\",\n            \"0.042\",\n            \"0.38\",\n            \"12×\",\n            \"1.32×\"\n          ],\n          [\n            \"6–10\",\n            \"0.010\",\n            \"0.020\",\n            \"0.32\",\n            \"25×\",\n            \"1.56×\"\n          ],\n          [\n            \"11–15\",\n            \"0.006\",\n            \"0.011\",\n            \"0.25\",\n            \"45×\",\n            \"2.0×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"长对话 eval 在 median 档为 paper 提供了 'exposure bias compounds over turns' 的补充证据。TG gap 从 12× 扩大到 45× 直观有力——随 model-generated context 累积，分布偏移逐 turn 加剧。SS gap 也在增长（1.32→2.0×），暗示 SS 的 修正并非完美的——超出训练 turn 长度的泛化性有限。\\n论文用途：§6.3 Distribution Shift Analysis 中用 1 段 + 1 图报告， 强调 \\\"gap grows with conversation length, consistent with cumulative distribution shift.\\\" 在 Discussion 中提及 SS 的 turn-length limitation 作为 future work direction。\\n审稿人风险：median 档下不太可能是 rejection 理由（N=15 样本太小 无法做严格推断）。但如果审稿人要求 N=50 长对话 eval， 则需要寻找或生成更多 >10 turn 数据。\\n\\nExposure bias 效应随对话长度累积：每增加一个 turn，model-generated context 占比增大，训练-推理分布偏移加剧。\\nTG gap 从 12×（turns 3-5）扩大到 45×（turns 11-15），因为 TF GAR 稳定在 0.50（不依赖对话长度——TF 条件下 context 始终是 gold text），而 AR GAR 持续衰减（0.042→0.020→0.011）。这是 exposure bias 累积效应的直接证据。\\nSS gap 也从 1.32× 扩大到 2.0×（turns 11-15），但增速远慢于 TG。 SS 训练中暴露了 model-generated context，部分缓解了分布偏移， 但 SS 训练数据的最大 turn 数与 eval 不同（训练 ~10 turns，eval 15 turns）， 超出训练分布的 turns 泛化性下降。\\n在 median 档下，这个实验提供了有价值但非关键的 supplementary evidence。 审稿人可能感兴趣但不太可能要求 15+ turns eval 作为必要条件。 数据限制：UltraChat 中 >10 turn 对话较少（filtered N=15）， 统计功效受限，结果仅作为 trend 报告而非 claim。\\n\"\n  }\n]",
      "numLines": 825,
      "startLine": 1,
      "totalLines": 825
    }
  },
  "sourceToolAssistantUUID": "d70b5363-a49c-47c4-a329-07f5a34e211c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_g…",
  "leafUuid": "f182e9b8-9f51-4f63-97fe-89ba48d35ccd",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on residual gating mechanisms",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b"
}
```

---

### Assistant

_source line 15 · 2026-05-24T08:52:59.102Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me now write a complete LaTeX paper for this dream report. I need to:

1. First, check if the output directory exists
2. Write the complete LaTeX paper
3. Compile it

Let me check the directory first and also load the paper-writing-norms skill and distilled-writing skill for reference.

Actually, given the instructions say "够审级" (reviewable quality), I should focus on getting a complete, well-structured paper with all the data properly presented, without spending too much time on perfecting every sentence.

Let me structure the paper:


- Abstract, introduction, and related work sections
- Background covering GAR definition and residual stream persistence
- Method section detailing ThreadGate architecture and loss design
- Comprehensive experiments section with setup, main ablation results, inference-time steering, and scheduled sampling
- Analysis covering gate turn conditioning, gradient conflict exclusion, distribution shift patterns, mechanism specificity across models, and sensitivity studies
- Discussion of transfer learning implications

Now I'm wrapping up with limitations and future directions, then the conclusion. I'm also reviewing the experimental data—looking at gradient conflict patterns across Llama and Qwen models, the expanded evaluation results with tighter confidence intervals, and sensitivity analysis for the GAR weighting parameter. Now I'm looking at the Llama results with different beta values, seeing how the gap shrinks as beta increases. The three-seed validation on Qwen shows consistent performance around 0.40 with a gap of 1.26×, and the alternative definitions mostly improve except for goal-only. The long conversation evaluation reveals that the gap grows significantly over turns—up to 45× for the base model but only 2.0× with our approach.

I'm also pulling in some additional results from the paper framing that weren't in the main experiments: the v7 training showed a 7.8× gap between TF and AR, Llama had an even worse 27× gap, and the PCGrad ablation showed minimal differences. The four-way ablation suggests TG, UG, and LO are roughly equivalent, while the gate analysis reveals most layers show reverse turn conditioning with very small attenuation effects. The beta-steering results are striking—pushing GAR from 0.064 all the way to 0.727.

Now I'm ready to write the paper, but I need to be precise about a few things: the gate formula follows a ReZero-style residual structure, the title should emphasize how exposure bias specifically damages auxiliary attention losses in dialogue, I'm toning down contribution five for the supplementary section, and I'm pulling all numbers directly from the experiment data rather than estimating. Let me set up the directory and start writing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f182e9b8-9f51-4f63-97fe-89ba48d35ccd",
  "isSidechain": false,
  "requestId": "req_011CbM7KX14TMSgUy6b2C7FD",
  "type": "assistant",
  "uuid": "f6598a10-798d-4853-95db-54cd42ae991b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR2gFAN4avpJZfCv6aHCm1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9523,
      "cache_creation_input_tokens": 15415,
      "cache_read_input_tokens": 25321,
      "output_tokens": 1442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9523,
          "output_tokens": 1442,
          "cache_read_input_tokens": 25321,
          "cache_creation_input_tokens": 15415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15415
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

_source line 16 · 2026-05-24T08:52:59.131Z_

Let me check that the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6598a10-798d-4853-95db-54cd42ae991b",
  "isSidechain": false,
  "requestId": "req_011CbM7KX14TMSgUy6b2C7FD",
  "type": "assistant",
  "uuid": "d87b6774-9487-4c5d-a92a-ae460eb99e15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR2gFAN4avpJZfCv6aHCm1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9523,
      "cache_creation_input_tokens": 15415,
      "cache_read_input_tokens": 25321,
      "output_tokens": 1442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9523,
          "output_tokens": 1442,
          "cache_read_input_tokens": 25321,
          "cache_creation_input_tokens": 15415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15415
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

_source line 17 · 2026-05-24T08:52:59.540Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017xKhGUu4LUncqZNvvSQXn6`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/",
  "description": "List median directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d87b6774-9487-4c5d-a92a-ae460eb99e15",
  "isSidechain": false,
  "requestId": "req_011CbM7KX14TMSgUy6b2C7FD",
  "type": "assistant",
  "uuid": "77ed5302-a560-405c-bd8a-cca42d0db5bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR2gFAN4avpJZfCv6aHCm1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9523,
      "cache_creation_input_tokens": 15415,
      "cache_read_input_tokens": 25321,
      "output_tokens": 1442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9523,
          "output_tokens": 1442,
          "cache_read_input_tokens": 25321,
          "cache_creation_input_tokens": 15415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15415
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

_source line 18 · 2026-05-24T08:52:59.703Z_

<details><summary>↩ Tool result · `toolu_017xKhGUu4LUncqZNvvSQXn6`</summary>

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
  "parentUuid": "77ed5302-a560-405c-bd8a-cca42d0db5bb",
  "isSidechain": false,
  "promptId": "67a87842-f41b-4d9e-9fbd-faa3f9849a08",
  "type": "user",
  "uuid": "417f4e8e-c67d-4292-9ef4-e0a97a110034",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "77ed5302-a560-405c-bd8a-cca42d0db5bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-24T08:53:04.756Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists. Now let me write the full LaTeX paper. I need to be thorough and include all the experimental data.

Let me structure this carefully. I'll use a standard ACL/EMNLP format. Since this is a "够审" (reviewable) quality paper, I need to be complete but not necessarily polished to submission quality.

Key things to include:
- Title: T1 from framing
- All experiments mapped to sections/tables
- Correct formulas
- Proper framing per narrative guidance

Let me write this now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "417f4e8e-c67d-4292-9ef4-e0a97a110034",
  "isSidechain": false,
  "requestId": "req_011CbM7NTVoUUAQa6WwXr74T",
  "type": "assistant",
  "uuid": "7c10f502-b962-4f9d-829f-0eeed78328c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016esBBHPr1T8yQFsexkAasf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10992,
      "cache_read_input_tokens": 40736,
      "output_tokens": 12699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10992,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12699,
          "cache_read_input_tokens": 40736,
          "cache_creation_input_tokens": 10992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10992
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

_source line 20 · 2026-05-24T08:53:05.333Z_

Now writing the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c10f502-b962-4f9d-829f-0eeed78328c8",
  "isSidechain": false,
  "requestId": "req_011CbM7NTVoUUAQa6WwXr74T",
  "type": "assistant",
  "uuid": "06878ffb-4ceb-40b1-a480-7405c6de79ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016esBBHPr1T8yQFsexkAasf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10992,
      "cache_read_input_tokens": 40736,
      "output_tokens": 12699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10992,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12699,
          "cache_read_input_tokens": 40736,
          "cache_creation_input_tokens": 10992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10992
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

_source line 21 · 2026-05-24T08:57:06.665Z_

<details open><summary>🔧 Tool call — Write · `toolu_01PfaEWBgtAgMkzosWkn1Xe3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\title{Exposure Bias Selectively Destroys Auxiliary Attention Losses\\\\in Multi-Turn Dialogue}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nMulti-turn dialogue models suffer from progressive goal accessibility degradation as conversations lengthen: attention to task-relevant information in early turns diminishes over subsequent turns. Prior work shows that goal information persists in residual streams (probe AUC$=$0.98) even as the attention channel closes, motivating learnable residual gating as a remedy. We implement ThreadGate, a per-layer gating module jointly trained with next-token prediction (NTP) and a Goal Accessibility Ratio (GAR) auxiliary loss. ThreadGate successfully optimizes GAR under teacher-forced evaluation (GAR$=$0.50), but collapses under autoregressive generation (GAR$=$0.064 on Qwen-2.5-7B, 0.018 on Llama-3.1-8B), revealing an 8$\\times$--27$\\times$ training--inference gap. We trace this failure to exposure bias: attention patterns learned on gold-text contexts do not transfer to model-generated contexts. A PCGrad ablation causally excludes gradient direction conflict as a contributing factor, while NTP gradient magnitude dominance (7.5--25.7$\\times$) drives gates toward identity. Four-way ablation confirms gating provides zero incremental benefit. Scheduled sampling compresses the gap from 8$\\times$ to ${\\sim}$1.3$\\times$ on Qwen (AR GAR$=$0.401$\\pm$0.047, 4 seeds) with no perplexity cost, though cross-model transfer to Llama is partial (gap$=$2.7$\\times$). These results provide the first empirical characterization of how exposure bias selectively destroys auxiliary attention losses in multi-turn settings.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nLarge language models exhibit progressive degradation in multi-turn dialogue: as conversations grow longer, models increasingly fail to attend to task-relevant information from early turns~\\cite{dongre2026gar,zheng2023judging}. \\citet{dongre2026gar} formalized this through the Goal Accessibility Ratio (GAR), documenting 27--48\\% drops across 12 models over 50 turns. Crucially, their residual stream probes reveal that goal information \\emph{persists} in hidden states (AUC up to 0.98) even as the attention channel closes---the information is present but inaccessible through attention.\n\nThis creates a natural architectural hypothesis: if goal information is retained in the residual stream but attention fails to route it, a learnable gate on the residual connection should recover accessibility. We implement this as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. The design is principled: gates modulate sub-layer output magnitude, allowing the model to selectively amplify or suppress layer contributions based on turn structure.\n\nThreadGate succeeds during training. On teacher-forced (TF) evaluation with gold-text contexts, GAR-ours reaches 0.50---a 25$\\times$ improvement over the base model's 0.019. However, under autoregressive (AR) generation with model-generated contexts, GAR-ours collapses to 0.064 on Qwen-2.5-7B (7.8$\\times$ gap) and 0.018 on Llama-3.1-8B (27$\\times$ gap). This dramatic discrepancy---attention patterns that work perfectly on gold text but fail completely on generated text---is the signature of exposure bias~\\cite{bengio2015scheduled,ranzato2016sequence}.\n\nOur analysis reveals three coupled mechanisms behind this failure: (1) the training--inference distribution shift is the primary cause, as confirmed by a PCGrad ablation that causally excludes gradient direction conflict; (2) NTP gradient magnitude dominates gate parameters by 7.5--25.7$\\times$, driving gates toward identity and producing reverse turn conditioning; (3) at inference time, gates attenuate sub-layer output by only 2--7\\%, far too weak to shift attention patterns. Four-way ablation (ThreadGate / Uniform Gate / LoRA-only / Base) confirms gating provides zero incremental contribution over LoRA fine-tuning alone.\n\nWe further show that scheduled sampling---mixing model-generated context during training---compresses the TF--AR gap from 8$\\times$ to ${\\sim}$1.3$\\times$ on Qwen (AR GAR $=$ 0.401$\\pm$0.047, 4 seeds) with no perplexity cost, though cross-model efficacy on Llama is partial (gap $=$ 2.7$\\times$). Inference-time $\\beta$-steering independently recovers GAR from 0.064 to 0.727. Our contributions are:\n\\begin{enumerate}\n    \\item The first empirical characterization of how exposure bias destroys auxiliary attention loss generalization (8$\\times$--27$\\times$ gap), specific to summary-position attention.\n    \\item Per-layer quantification of NTP--GAR gradient dynamics, with PCGrad causal exclusion of gradient direction conflict.\n    \\item Systematic four-way ablation isolating gating contributions across two model families.\n    \\item Cross-model validation (Qwen-2.5-7B + Llama-3.1-8B) confirming the generality of the failure mode.\n    \\item Initial evidence that scheduled sampling transfers to multi-turn auxiliary attention objectives, effective on Qwen but with reduced cross-model efficacy requiring further investigation.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Multi-Turn Dialogue Degradation.}\nGoal accessibility degradation in multi-turn LLM dialogue has been characterized by \\citet{dongre2026gar}, who introduced the GAR metric and documented systematic attention decay across 12 models. MT-Bench~\\cite{zheng2023judging} and MT-Bench-101~\\cite{bai2024mtbench101} evaluate multi-turn capabilities but focus on response quality rather than attention mechanisms. Lost-in-the-Middle~\\cite{liu2024lost} documents position-dependent retrieval failure in long contexts, a related but distinct phenomenon.\n\n\\paragraph{Residual Gating and Adaptive Depth.}\nResidual gating has been explored for adaptive computation depth. ReZero~\\cite{bachlechner2021rezero} initializes residual connections with learnable zero-initialized scalars. SkipNet~\\cite{wang2018skipnet} learns binary skip decisions. LayerDrop~\\cite{fan2020reducing} uses structured dropout during training. FlexiDepth~\\cite{luo2025flexidepth} enables per-token adaptive depth. Our ThreadGate differs in that gates are conditioned on turn structure and trained with an auxiliary attention objective rather than for computational efficiency.\n\n\\paragraph{Attention Steering and Intervention.}\nAttention sinks~\\cite{xiao2024efficient} reveal that initial tokens absorb disproportionate attention mass regardless of content. Gated attention mechanisms~\\cite{qiu2025gated} modulate attention weights within layers. Transformer circuits analysis~\\cite{elhage2021mathematical} provides mechanistic understanding of attention head specialization. Our work attempts to steer attention through residual gating rather than direct attention weight modification.\n\n\\paragraph{Exposure Bias.}\nThe training--inference distribution mismatch in autoregressive models was identified by \\citet{bengio2015scheduled}, who proposed scheduled sampling as a remedy. Subsequent work includes Professor Forcing~\\cite{lamb2016professor}, SEARNN~\\cite{leblond2018searnn}, and sequence-level training~\\cite{ranzato2016sequence,wiseman2016sequence}. \\citet{dou2022parallel} applied attention-forcing to NMT with data-dependent mode selection. Our contribution is demonstrating that this classical problem manifests with particular severity (8$\\times$--27$\\times$ gap) in auxiliary attention losses for multi-turn dialogue, and that time-scheduled sampling transfers to this setting.\n\n% ============================================================\n\\section{Background}\n\n\\subsection{Goal Accessibility Ratio}\n\nFollowing \\citet{dongre2026gar}, we measure how well a model's attention mechanism routes information from goal-specifying tokens to response generation positions. We define two GAR variants:\n\n\\textbf{GAR-ours} measures attention from the last token of each assistant response to goal tokens (system prompt + first user query):\n\\begin{equation}\n\\text{GAR-ours} = \\frac{1}{|H|} \\sum_{h \\in H} \\sum_{g \\in \\mathcal{G}} A_h[\\text{last}, g]\n\\end{equation}\nwhere $H$ is the set of attention heads, $\\mathcal{G}$ is the set of goal token positions, and $A_h[\\text{last}, g]$ is the attention weight from the last response token to goal token $g$ in head $h$.\n\n\\textbf{GAR-Dongre} uses all response tokens and restricts goals to system prompt task tokens only, enabling direct comparison with \\citet{dongre2026gar}.\n\n\\subsection{Residual Stream Persistence}\n\n\\citet{dongre2026gar} demonstrated via linear probes that goal information persists in residual stream representations (AUC up to 0.98) even at late turns where attention-based GAR has degraded severely. This dissociation---information present in hidden states but inaccessible through attention---motivates architectural interventions on the residual connection.\n\n% ============================================================\n\\section{Method}\n\n\\subsection{ThreadGate Architecture}\n\nThreadGate introduces a per-layer scalar gate $g_l \\in (0, 1)$ that modulates the sub-layer output in a ReZero-style residual connection:\n\\begin{equation}\n\\mathbf{x}_{l+1} = \\mathbf{x}_l + g_l \\cdot f_l(\\mathbf{x}_l)\n\\label{eq:gate}\n\\end{equation}\nwhere $f_l$ is the sub-layer transformation (self-attention or FFN) at layer $l$. When $g_l \\to 0$, the sub-layer becomes a no-op (identity); when $g_l \\to 1$, the full sub-layer output is retained.\n\nEach gate is computed by a 2-layer MLP conditioned on hidden state and turn structure:\n\\begin{equation}\ng_l = \\sigma\\!\\left(W_2 \\cdot \\text{ReLU}(W_1 \\cdot [\\text{proj}(\\mathbf{x}_l); \\text{emb}(t_d, t_i)] + b_1) + b_2\\right)\n\\end{equation}\nwhere $t_d$ is the turn distance (tokens since last turn boundary) and $t_i$ is the turn index. The gate produces per-token, per-layer values, enabling turn-aware modulation.\n\n\\textbf{Uniform Gate (UG)} uses the same architecture but replaces turn embeddings with a constant vector, isolating turn-conditioning effects while retaining content-dependent gating.\n\n\\textbf{LoRA-only} fixes $g_l = 1.0$ (no gating) while retaining the GAR loss, isolating the contribution of the gating mechanism itself.\n\n\\subsection{Training Objective}\n\nThe joint loss combines NTP and GAR terms:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_{\\text{NTP}} + \\lambda_{\\text{GAR}} \\cdot \\mathcal{L}_{\\text{GAR}} + \\lambda_{\\text{div}} \\cdot \\mathcal{L}_{\\text{div}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{GAR}}$ is an MSE loss pushing GAR toward a target value and $\\mathcal{L}_{\\text{div}}$ is a gate diversity regularizer preventing gate collapse. We set $\\lambda_{\\text{GAR}} = 1.0$ and $\\lambda_{\\text{div}} = 0.01$ by default.\n\nThe MSE+gate\\_div formulation (v7) was selected after iterating through four loss families: cumulative attention (v1--v2), maximize attention (v3--v5), smooth saturation (v6), and MSE target (v7). Only v7 achieved stable training convergence.\n\n\\subsection{Scheduled Sampling}\n\nTo address the training--inference distribution shift, we apply scheduled sampling (SS)~\\cite{bengio2015scheduled} adapted for multi-turn dialogue. During training, each assistant turn's context is constructed from either gold text (teacher forcing) or model-generated text (autoregressive), selected per-turn with probability $p_{\\text{ss}}(t)$ that increases linearly from 0 to 0.5 over the training epochs:\n\\begin{equation}\np_{\\text{ss}}(t) = \\min\\!\\left(0.5, \\frac{t}{T} \\cdot 0.5\\right)\n\\end{equation}\nwhere $t$ is the current step and $T$ is the total training steps. This exposes the model to its own generation distribution during training, reducing the TF--AR mismatch.\n\n\\subsection{Inference-Time $\\beta$-Steering}\n\nAt inference time, we amplify gate influence by raising gate values to a power $\\beta < 1$:\n\\begin{equation}\ng_l^{\\text{steer}} = g_l^{1/\\beta}\n\\end{equation}\nFor $\\beta > 1$, gates closer to 1.0 are pushed further from identity, amplifying the sub-layer modulation that gates learned during training but apply too weakly at inference.\n\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Models.} We conduct primary experiments on Qwen-2.5-7B (28 layers, GQA) and cross-model validation on Llama-3.1-8B (32 layers, 8 KV heads).\n\n\\paragraph{Data.} Training uses UltraChat~\\cite{ding2023enhancing} multi-turn conversations. Evaluation uses held-out conversations: $N{=}200$ for TF evaluation and $N{=}50$ for AR evaluation on Qwen; $N{=}20$ for Llama AR evaluation.\n\n\\paragraph{Training.} All models are fine-tuned with LoRA (rank 16) for 3 epochs. Seed$=$42 for primary experiments; seeds \\{42, 123, 456, 789\\} for SS multi-seed validation. Training uses bfloat16 mixed precision on a single A100 80GB GPU.\n\n\\paragraph{Evaluation Protocol.} We evaluate under two conditions: (1) \\textbf{Teacher-forced (TF)}: model processes gold-text conversations, measuring attention patterns on the training distribution; (2) \\textbf{Autoregressive (AR)}: model generates its own responses turn by turn, measuring attention patterns on the inference distribution. The TF/AR gap quantifies the exposure bias effect.\n\n\\subsection{Main Results: Four-Way Ablation}\n\nTable~\\ref{tab:main} presents the four-way ablation on Qwen-2.5-7B with $N{=}200$ TF evaluation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Four-way ablation on Qwen-2.5-7B. TF evaluation uses $N{=}200$ conversations with 95\\% bootstrap CI. All fine-tuned variants achieve comparable TF GAR ($\\sim$0.50) and PPL ($\\sim$2.78), but AR GAR collapses uniformly. Gating provides zero incremental benefit over LoRA-only.}\n\\label{tab:main}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nVariant & GAR-ours & 95\\% CI & GAR-D & PPL \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Teacher-Forced (TF) Evaluation, N=200}} \\\\\nBase & 0.013 & [0.010, 0.016] & 0.003 & 4.34 \\\\\nThreadGate & 0.504 & [0.489, 0.519] & 0.015 & 2.78 \\\\\nUniform Gate & 0.506 & [0.491, 0.521] & 0.012 & 2.78 \\\\\nLoRA-only & 0.499 & [0.483, 0.514] & 0.013 & 2.78 \\\\\n\\midrule\nTG$-$LO diff & +0.006 & [$-$0.001, 0.003] & +0.002 & 0.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll three fine-tuned variants (ThreadGate, Uniform Gate, LoRA-only) achieve near-identical TF GAR-ours ($\\sim$0.50) and perplexity ($\\sim$2.78). The TG--LO difference CI includes zero, confirming that gating provides no measurable benefit. The $N{=}200$ evaluation reduces CI width by 42\\% compared to $N{=}50$, strengthening the null result.\n\nUnder AR generation, all variants collapse: ThreadGate AR GAR-ours $=$ 0.064, producing an 8$\\times$ gap (Qwen) that widens to 27$\\times$ on Llama-3.1-8B. GAR-Dongre shows uniformly low values ($<$0.02) in both TF and AR conditions, indicating that the distribution shift selectively affects summary-position (last-token) attention patterns.\n\n\\subsection{Inference-Time $\\beta$-Steering}\n\n$\\beta$-steering amplifies gate influence at inference time without retraining. On Qwen-2.5-7B, GAR-ours increases from 0.064 ($\\beta{=}0$) to 0.727 ($\\beta{=}5$), demonstrating that the gate contains latent structure that is underutilized at default scale. However, this is a post-hoc intervention that does not address the underlying distribution shift.\n\n\\subsection{Scheduled Sampling Results}\n\n\\paragraph{Qwen-2.5-7B (4-seed).}\nTable~\\ref{tab:ss_seeds} presents SS results across 4 seeds. SS compresses the TF--AR gap from 8$\\times$ to 1.24$\\times$ (mean), with AR GAR-ours $=$ 0.405$\\pm$0.040 at $\\beta{=}0$ and no perplexity cost (PPL 1.441$\\pm$0.001).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scheduled sampling results on Qwen-2.5-7B across 4 seeds. $\\beta$ controls inference-time gate amplification. Effect size / std $=$ 9.7 at $\\beta{=}0$, confirming statistical significance.}\n\\label{tab:ss_seeds}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nSeed & TF GAR & AR $\\beta{=}0$ & AR $\\beta{=}3$ & AR $\\beta{=}5$ & PPL \\\\\n\\midrule\ns42 & 0.503 & 0.347 & 0.593 & 0.717 & 1.442 \\\\\ns123 & 0.495 & 0.423 & 0.590 & 0.717 & 1.441 \\\\\ns456 & 0.496 & 0.433 & 0.605 & 0.716 & 1.439 \\\\\ns789 & --- & 0.415 & 0.598 & 0.718 & 1.440 \\\\\n\\midrule\nMean$\\pm$Std & 0.498$\\pm$.004 & 0.405$\\pm$.040 & 0.597$\\pm$.007 & 0.717$\\pm$.001 & 1.441$\\pm$.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\beta{\\geq}3$, cross-seed variance drops below 0.01, indicating that inference-time steering is a deterministic intervention independent of training seed randomness. Seed s42 is a mild outlier at $\\beta{=}0$ (0.347, $-$1.15$\\sigma$ from mean) but converges with other seeds at higher $\\beta$.\n\n\\paragraph{Cross-Model: Llama-3.1-8B.}\nTable~\\ref{tab:cross_model_ss} compares SS efficacy across model families. SS is effective on Llama (20$\\times$ improvement over base, gap compressed from 27$\\times$ to 2.7$\\times$), but substantially weaker than on Qwen (AR GAR 0.18 vs.\\ 0.40, gap 2.7$\\times$ vs.\\ 1.3$\\times$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model SS comparison. SS is effective on both models but with reduced efficacy on Llama-3.1-8B. $\\beta$-steering narrows the cross-model gap at higher values.}\n\\label{tab:cross_model_ss}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMetric & Qwen-2.5-7B & Llama-3.1-8B & Ratio \\\\\n\\midrule\nBase AR GAR & 0.019 & 0.009 & 2.1$\\times$ \\\\\nTG AR GAR (no SS) & 0.064 & 0.018 & 3.6$\\times$ \\\\\nSS AR GAR $\\beta{=}0$ & 0.401$\\pm$.047 & 0.18$\\pm$.09 & 2.2$\\times$ \\\\\nSS AR GAR $\\beta{=}3$ & 0.596$\\pm$.008 & 0.45 & 1.3$\\times$ \\\\\nSS AR GAR $\\beta{=}5$ & 0.717$\\pm$.001 & 0.62 & 1.2$\\times$ \\\\\nTF GAR & 0.498$\\pm$.004 & 0.485 & 1.03$\\times$ \\\\\nSS Gap (TF/AR $\\beta{=}0$) & 1.26$\\times$ & 2.7$\\times$ & --- \\\\\nTG Gap (no SS) & 8$\\times$ & 27$\\times$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\beta{=}5$, the cross-model gap narrows to 1.2$\\times$ (Llama 0.62 vs.\\ Qwen 0.72), suggesting that inference-time steering generalizes better than training-time SS across architectures.\n\n% ============================================================\n\\section{Analysis}\n\n\\subsection{Gate Turn Conditioning}\n\nAnalysis of gate activation profiles reveals that 27 of 28 layers exhibit \\emph{reverse} turn conditioning: gate values at early turns (where GAR is highest and intervention is least needed) are lower than at late turns (where GAR has degraded and intervention is most needed). Gate mean across layers is 0.93--0.98 at late turns, producing only 2--7\\% sub-layer attenuation---too weak to meaningfully shift attention patterns. This reverse conditioning arises because NTP loss gradients dominate gate parameters, pushing gates toward 1.0 (preserving full layer computation) most strongly at late turns where NTP loss is highest.\n\n\\subsection{PCGrad Causal Exclusion of Gradient Conflict}\n\\label{sec:pcgrad}\n\nWe observe that NTP and GAR gradients conflict in direction (cosine similarity $<$ 0) in 67--79\\% of layers, with NTP magnitude dominating by 7.5--14.7$\\times$ on Qwen. To test whether this directional conflict causally contributes to GAR collapse, we train a PCGrad variant~\\cite{yu2020gradient} that projects conflicting gradients to eliminate directional interference.\n\nPCGrad successfully eliminates directional conflict (post-projection $\\cos_{\\text{sim}}$ oscillates around 0, range $-$0.151 to $+$0.091). However, $\\mathcal{L}_{\\text{GAR}}$ collapse trajectory is unchanged and shows no delay. Inference evaluation confirms: PCGrad GAR-ours $=$ 0.0151 vs.\\ standard v7 $=$ 0.0157 (difference $<$ 0.1pp); PCGrad PPL $=$ 2.780 vs.\\ v7 PPL $=$ 2.784. All observable metrics are statistically identical, establishing that gradient direction conflict is neither necessary nor sufficient for the 8$\\times$--27$\\times$ GAR gap. Exposure bias (distribution shift) alone is sufficient.\n\n\\subsection{Distribution Shift Compounds Over Conversation Length}\n\nTable~\\ref{tab:long_conv} shows that the TF--AR gap grows with conversation length, consistent with cumulative distribution shift as model-generated context accumulates.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{GAR gap versus conversation length ($N{=}15$ conversations with $\\geq$12 turns). TG gap grows from 12$\\times$ to 45$\\times$ as turns increase. SS mitigates but does not eliminate the length effect.}\n\\label{tab:long_conv}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nTurns & Base & TG AR & SS AR & TG Gap & SS Gap \\\\\n\\midrule\n3--5 & 0.016 & 0.042 & 0.38 & 12$\\times$ & 1.32$\\times$ \\\\\n6--10 & 0.010 & 0.020 & 0.32 & 25$\\times$ & 1.56$\\times$ \\\\\n11--15 & 0.006 & 0.011 & 0.25 & 45$\\times$ & 2.0$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTF GAR remains stable at $\\sim$0.50 regardless of conversation length (gold-text context quality does not degrade), while AR GAR decays monotonically. The 45$\\times$ gap at turns 11--15 reflects severe cumulative error: each turn's model-generated text shifts the context distribution further from training conditions. SS reduces but does not eliminate this compounding (gap 1.32$\\times$ to 2.0$\\times$), suggesting that SS generalization has limits beyond the training turn-length distribution.\n\n\\subsection{Mechanism Specificity: KL Divergence Analysis}\n\nTo characterize \\emph{where} in the attention space exposure bias manifests, we compute per-head KL divergence $D_{\\text{KL}}(P_{\\text{TF}} \\| P_{\\text{AR}})$ across 50 conversations (Table~\\ref{tab:kl}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TF--AR attention KL divergence by layer group. Distribution shift concentrates in deep layers (L21--27), where gates attempt the most intervention.}\n\\label{tab:kl}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nLayer Group & TG KL & Base KL & TG/Base \\\\\n\\midrule\nL0--6 (shallow) & 0.031 & 0.028 & 1.11 \\\\\nL7--13 (lower-mid) & 0.042 & 0.036 & 1.17 \\\\\nL14--20 (upper-mid) & 0.058 & 0.045 & 1.29 \\\\\nL21--27 (deep) & 0.089 & 0.065 & 1.37 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTG models show larger KL divergence than base models (mean 0.054 vs.\\ 0.043), because TG training shapes attention patterns specifically for the TF distribution, which then shift more under AR conditions. The effect concentrates in deep layers (L21--27, TG/Base ratio 1.37), precisely where gates attempt the most intervention.\n\nTable~\\ref{tab:gar_defs} reveals that GAR sensitivity to distribution shift varies dramatically across token selection criteria.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{GAR definition sensitivity to TF--AR distribution shift. Summary-position attention (last-token, goal-only) is highly sensitive; distributed attention (all-token, first-token) is robust.}\n\\label{tab:gar_defs}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nDefinition & TF & AR & Gap & Sensitivity \\\\\n\\midrule\nLast token (ours) & 0.504 & 0.016 & 32$\\times$ & High \\\\\nGoal-only & 0.630 & 0.010 & 63$\\times$ & Very high \\\\\nAll tokens & 0.028 & 0.016 & 1.7$\\times$ & Low \\\\\nFirst token & 0.035 & 0.019 & 1.8$\\times$ & Low \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLast-token and goal-only GAR definitions, which measure long-range attention routing to specific positions, exhibit 32--63$\\times$ gaps. All-token and first-token definitions, which measure more distributed or local attention, show only 1.7--1.8$\\times$ gaps. This demonstrates that exposure bias \\emph{selectively} disrupts summary-position attention patterns that depend on long-range context quality, while leaving local attention patterns largely unaffected.\n\n\\subsection{Alternative GAR Definition Robustness of SS}\n\nTable~\\ref{tab:gar_alt} tests whether SS improvements generalize across GAR definitions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SS effect across alternative GAR definitions (AR evaluation on Qwen). SS improves 3 of 4 definitions; goal-only remains resistant.}\n\\label{tab:gar_alt}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nToken Selection & Base & TG & SS & Improves? \\\\\n\\midrule\nLast (GAR-ours) & 0.019 & 0.064 & 0.401 & Yes (21$\\times$) \\\\\nAll tokens & 0.018 & 0.025 & 0.360 & Yes (20$\\times$) \\\\\nFirst token & 0.020 & 0.039 & 0.250 & Yes (12.5$\\times$) \\\\\nGoal-only & 0.012 & 0.015 & 0.060 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSS improves 3 of 4 definitions, indicating that it builds broader goal-attention patterns rather than overfitting to the trained definition. TG without SS only improves the trained definition (last-token: 0.064 vs.\\ base 0.019), confirming position-specific overfitting under teacher forcing. The most restrictive definition (goal-only) remains resistant even to SS, suggesting that precise goal-token routing requires mechanisms beyond distributional correction.\n\n\\subsection{Cross-Model Gradient Analysis}\n\nTable~\\ref{tab:grad_cross} compares NTP--GAR gradient dynamics across architectures.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model gradient analysis. Llama shows orthogonal (not conflicting) gradients but more extreme NTP magnitude dominance, correlating with a larger TG gap.}\n\\label{tab:grad_cross}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMetric & Qwen-2.5-7B & Llama-3.1-8B & Interp. \\\\\n\\midrule\n$\\cos_{\\text{sim}}$ (final) & $-$0.042 & $+$0.005 & Qwen: mild conflict \\\\\n & & & Llama: orthogonal \\\\\nneg\\_layers \\% & 67.9\\% & 53.1\\% & Qwen: moderate \\\\\n & & & Llama: near-random \\\\\nmag\\_ratio & 14.7$\\times$ & 25.7$\\times$ & Llama NTP \\\\\n & & & dominance stronger \\\\\nTG AR GAR gap & 8$\\times$ & 27$\\times$ & Correlates with \\\\\n & & & mag\\_ratio \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLlama's gradient dynamics differ qualitatively from Qwen: gradients are near-orthogonal ($\\cos_{\\text{sim}} \\approx 0$) rather than conflicting, and NTP magnitude dominance is more extreme (25.7$\\times$ vs.\\ 14.7$\\times$). The correlation between magnitude ratio and TG gap size (14.7$\\times$ mag $\\to$ 8$\\times$ gap; 25.7$\\times$ mag $\\to$ 27$\\times$ gap) suggests that NTP dominance, not directional conflict, is the relevant gradient-level predictor of GAR collapse severity.\n\n\\subsection{$\\lambda_{\\text{GAR}}$ Sensitivity}\n\nTable~\\ref{tab:lambda} tests whether rebalancing gradient magnitudes resolves the gap.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\lambda_{\\text{GAR}}$ sensitivity. Even 10$\\times$ GAR weight, which balances NTP and GAR gradient magnitudes, leaves a 22$\\times$ gap. Distribution shift, not gradient competition, is the bottleneck.}\n\\label{tab:lambda}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n$\\lambda_{\\text{GAR}}$ & TF GAR & AR GAR & Gap & PPL & Gate $\\mu$ \\\\\n\\midrule\n0.1 & 0.42 & 0.013 & 32.3$\\times$ & 2.76 & 0.972 \\\\\n1.0 (default) & 0.50 & 0.016 & 32.1$\\times$ & 2.78 & 0.934 \\\\\n10.0 & 0.535 & 0.024 & 22.3$\\times$ & 2.95 & 0.905 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\lambda_{\\text{GAR}}{=}10$, GAR gradients reach parity with NTP in magnitude, gates achieve wider dynamic range (std 0.082 vs.\\ 0.049), and TF GAR improves to 0.535. Yet AR GAR rises only marginally (0.024), leaving a 22$\\times$ gap. The PPL increase (+6\\%) reflects reduced NTP optimization budget. This confirms that gradient magnitude imbalance is not the bottleneck: even with balanced gradients, exposure bias prevents TF-trained attention patterns from transferring to AR generation.\n\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why Exposure Bias Selectively Destroys Auxiliary Attention Losses.}\nOur results reveal a specificity in how exposure bias manifests: it selectively disrupts summary-position attention (32--63$\\times$ gap for last-token and goal-only GAR) while leaving distributed attention largely unaffected (1.7--1.8$\\times$ for all-token and first-token). This selectivity arises because last-token attention depends on long-range context quality---the precise dimension along which gold and generated text diverge most.\n\n\\paragraph{Why NTP Self-Recovers but GAR Does Not.}\nNTP loss, computed on the current token given preceding context, is inherently local: even with degraded context, the model can partially recover by relying on short-range dependencies. GAR-ours, by contrast, requires accurate long-range attention routing from the response's final token to goal tokens in the system prompt, making it maximally sensitive to context distribution shifts.\n\n\\paragraph{SS Transferability Limitations.}\nWhile SS compresses the TF--AR gap to $\\sim$1.3$\\times$ on Qwen (AR GAR 0.401$\\pm$0.040, 4 seeds), its efficacy on Llama-3.1-8B is substantially reduced (gap 2.7$\\times$, AR GAR 0.18$\\pm$0.09). Several architectural differences may explain this: (1) Llama uses GQA with 8 KV heads, potentially limiting the attention routing capacity available for goal-relevant patterns; (2) Llama's 32 layers (vs.\\ Qwen's 28) dilute the SS correction signal across more gate--NTP interaction points; (3) Llama's more extreme NTP magnitude dominance (25.7$\\times$ vs.\\ 14.7$\\times$) may create a steeper optimization landscape for gate learning even under SS. The convergence of both models at high $\\beta$ ($\\beta{=}5$: Llama 0.62, Qwen 0.72) suggests that inference-time steering transfers better than training-time SS across architectures, indicating that the limitation is in SS training dynamics rather than a fundamental attention capacity constraint.\n\n\\paragraph{Implications for Attention Steering Methods.}\nOur findings suggest that any attention steering method trained with teacher forcing and evaluated under autoregressive generation faces the risk of this distribution shift. The 8$\\times$--27$\\times$ gap we measure provides a concrete risk benchmark. Methods that operate at inference time (e.g., $\\beta$-steering, activation engineering) may be more robust to this failure mode, as they bypass the training distribution entirely. Future work should investigate (1) model-specific SS schedule optimization, (2) decoupled goal-processing pathways that bypass the residual connection, and (3) GAR-aware decoding strategies.\n\n% ============================================================\n\\section{Conclusion}\n\nWe present the first empirical characterization of how exposure bias destroys auxiliary attention loss generalization in multi-turn dialogue. ThreadGate, a per-layer residual gating module, achieves GAR-ours $=$ 0.50 under teacher forcing but collapses to 0.064 (Qwen) and 0.018 (Llama) under autoregressive generation, an 8$\\times$--27$\\times$ gap. PCGrad ablation causally excludes gradient direction conflict, identifying distribution shift as the sole cause. Four-way ablation confirms gating provides zero incremental benefit. Scheduled sampling compresses the gap to $\\sim$1.3$\\times$ on Qwen (AR GAR 0.401$\\pm$0.040, 4 seeds) but with reduced cross-model efficacy (Llama gap $=$ 2.7$\\times$), establishing SS as a promising but model-dependent mitigation strategy for auxiliary attention objectives.\n\n% ============================================================\n\\section*{Limitations}\n\nOur experiments are conducted on two 7--8B parameter models; the generalization of the 8$\\times$--27$\\times$ gap to larger or smaller models remains untested. The evaluation uses GAR as a proxy metric for goal accessibility rather than downstream task performance (e.g., instruction following accuracy). SS multi-seed validation uses 4 seeds on Qwen and a single seed on Llama, limiting statistical power for the cross-model comparison.\n\n% ============================================================\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Bachlechner et~al.(2021)]{bachlechner2021rezero}\nThomas Bachlechner, Bodhisattwa~Prasad Majumder, Huanru~Henry Mao, Gary~W. Garrison, Bhanu~Pratap Laker, and Julian McAuley. 2021. ReZero is All You Need: Fast Convergence at Large Depth. In \\emph{UAI}.\n\n\\bibitem[Bai et~al.(2024)]{bai2024mtbench101}\nYushi Bai, Xin Lv, Jiajie Zhang, Yuze He, Ji Qi, Lei Hou, Zhiyuan Liu, Juanzi Li, and Jie Tang. 2024. MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogue. In \\emph{ACL}.\n\n\\bibitem[Bengio et~al.(2015)]{bengio2015scheduled}\nSamy Bengio, Oriol Vinyals, Navdeep Jaitly, and Noam Shazeer. 2015. Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks. In \\emph{NeurIPS}.\n\n\\bibitem[Ding et~al.(2023)]{ding2023enhancing}\nNing Ding, Yulin Chen, Bokai Xu, Yujia Qin, Zhi Zheng, Shengding Hu, Zhiyuan Liu, Maosong Sun, and Bowen Zhou. 2023. Enhancing Chat Language Models by Scaling High-quality Instructional Conversations. In \\emph{EMNLP}.\n\n\\bibitem[Dongre et~al.(2026)]{dongre2026gar}\nAmey Dongre, et~al. 2026. Goal Accessibility Ratio: Measuring Multi-Turn Dialogue Degradation. \\emph{Preprint}.\n\n\\bibitem[Dou and Gales(2022)]{dou2022parallel}\nZi-Yi Dou and Mark Gales. 2022. Parallel Attention Forcing for Machine Translation. In \\emph{NAACL}.\n\n\\bibitem[Elhage et~al.(2021)]{elhage2021mathematical}\nNelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, and Chris Olah. 2021. A Mathematical Framework for Transformer Circuits. \\emph{Transformer Circuits Thread}.\n\n\\bibitem[Fan et~al.(2020)]{fan2020reducing}\nAngela Fan, Edouard Grave, and Armand Joulin. 2020. Reducing Transformer Depth on Demand with Structured Dropout. In \\emph{ICLR}.\n\n\\bibitem[Lamb et~al.(2016)]{lamb2016professor}\nAlex~M. Lamb, Anirudh Goyal, Ying Zhang, Saizheng Zhang, Aaron~C. Courville, and Yoshua Bengio. 2016. Professor Forcing: A New Algorithm for Training Recurrent Networks. In \\emph{NeurIPS}.\n\n\\bibitem[Leblond et~al.(2018)]{leblond2018searnn}\nR{\\'e}mi Leblond, Jean-Baptiste Alayrac, Anton Osokin, and Simon Lacoste-Julien. 2018. SEARNN: Training RNNs with Global-Local Losses. In \\emph{ICLR}.\n\n\\bibitem[Liu et~al.(2024)]{liu2024lost}\nNelson~F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2024. Lost in the Middle: How Language Models Use Long Contexts. \\emph{TACL}.\n\n\\bibitem[Luo et~al.(2025)]{luo2025flexidepth}\nYifan Luo, et~al. 2025. FlexiDepth: Dynamic Depth for Efficient Transformers. \\emph{Preprint}.\n\n\\bibitem[Qiu et~al.(2025)]{qiu2025gated}\nXin Qiu, et~al. 2025. Gated Attention Mechanisms for Controlled Generation. \\emph{Preprint}.\n\n\\bibitem[Ranzato et~al.(2016)]{ranzato2016sequence}\nMarc'Aurelio Ranzato, Sumit Chopra, Michael Auli, and Wojciech Zaremba. 2016. Sequence Level Training with Recurrent Neural Networks. In \\emph{ICLR}.\n\n\\bibitem[Wang et~al.(2018)]{wang2018skipnet}\nXin Wang, Fisher Yu, Zi-Yi Dou, Trevor Darrell, and Joseph~E. Gonzalez. 2018. SkipNet: Learning Dynamic Routing in Convolutional Networks. In \\emph{ECCV}.\n\n\\bibitem[Wiseman and Rush(2016)]{wiseman2016sequence}\nSam Wiseman and Alexander~M. Rush. 2016. Sequence-to-Sequence Learning as Beam-Search Optimization. In \\emph{EMNLP}.\n\n\\bibitem[Xiao et~al.(2024)]{xiao2024efficient}\nGuangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. 2024. Efficient Streaming Language Models with Attention Sinks. In \\emph{ICLR}.\n\n\\bibitem[Yu et~al.(2020)]{yu2020gradient}\nTianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol Hausman, and Chelsea Finn. 2020. Gradient Surgery for Multi-Task Learning. In \\emph{NeurIPS}.\n\n\\bibitem[Zheng et~al.(2023)]{zheng2023judging}\nLianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric~P. Xing, Hao Zhang, Joseph~E. Gonzalez, and Ion Stoica. 2023. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In \\emph{NeurIPS}.\n\n\\end{thebibliography}\n\n% ============================================================\n\\appendix\n\\section{$\\lambda_{\\text{GAR}}$ Sensitivity Details}\n\nSee Table~\\ref{tab:lambda} in the main text. The three-point sweep ($\\lambda \\in \\{0.1, 1.0, 10.0\\}$) confirms that even 10$\\times$ GAR weight, which brings NTP and GAR gradient magnitudes to approximate parity (effective ratio 0.75--1.47$\\times$), leaves a 22$\\times$ TF--AR gap. Gate dynamic range increases with $\\lambda$ (std 0.022 $\\to$ 0.049 $\\to$ 0.082), but the additional gate freedom is directed toward TF optimization rather than AR generalization.\n\n\\section{4-Seed vs.\\ 3-Seed Comparison}\n\nAdding seed s789 (AR GAR $\\beta{=}0$ $=$ 0.415) reduces the standard deviation from 0.047 to 0.040 ($-$15\\%) and increases the effect size / std ratio from 8.2 to 9.7 ($+$18\\%). The 4-seed mean (0.405) is within 0.004 of the 3-seed mean (0.401), confirming stability.\n\n\\section{Llama-3.1-8B Detailed SS Results}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Llama-3.1-8B SS results at different $\\beta$ values. Improvement over base is substantial (20$\\times$ at $\\beta{=}0$) but weaker than Qwen.}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nCondition & AR GAR-ours & AR GAR-D & PPL & vs.\\ Base \\\\\n\\midrule\nBase & 0.009 & 0.005 & 1.27 & --- \\\\\nTG (no SS) & 0.018 & 0.018 & 1.32 & 2$\\times$ \\\\\nLO (no SS) & 0.018 & 0.020 & 1.32 & 2$\\times$ \\\\\nSS $\\beta{=}0$ & 0.18 & 0.25 & 1.40 & 20$\\times$ \\\\\nSS $\\beta{=}3$ & 0.45 & 0.38 & 1.55 & 50$\\times$ \\\\\nSS $\\beta{=}5$ & 0.62 & 0.48 & 1.72 & 69$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06878ffb-4ceb-40b1-a480-7405c6de79ca",
  "isSidechain": false,
  "requestId": "req_011CbM7NTVoUUAQa6WwXr74T",
  "type": "assistant",
  "uuid": "3b5859ff-ed46-4991-99d5-c77cde892264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016esBBHPr1T8yQFsexkAasf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10992,
      "cache_read_input_tokens": 40736,
      "output_tokens": 12699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10992,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12699,
          "cache_read_input_tokens": 40736,
          "cache_creation_input_tokens": 10992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10992
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

_source line 22 · 2026-05-24T08:57:06.682Z_

<details><summary>↩ Tool result · `toolu_01PfaEWBgtAgMkzosWkn1Xe3`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b5859ff-ed46-4991-99d5-c77cde892264",
  "isSidechain": false,
  "promptId": "67a87842-f41b-4d9e-9fbd-faa3f9849a08",
  "type": "user",
  "uuid": "4fc5f01a-18d0-435d-a6c2-7e5edf5cc74d",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\title{Exposure Bias Selectively Destroys Auxiliary Attention Losses\\\\in Multi-Turn Dialogue}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nMulti-turn dialogue models suffer from progressive goal accessibility degradation as conversations lengthen: attention to task-relevant information in early turns diminishes over subsequent turns. Prior work shows that goal information persists in residual streams (probe AUC$=$0.98) even as the attention channel closes, motivating learnable residual gating as a remedy. We implement ThreadGate, a per-layer gating module jointly trained with next-token prediction (NTP) and a Goal Accessibility Ratio (GAR) auxiliary loss. ThreadGate successfully optimizes GAR under teacher-forced evaluation (GAR$=$0.50), but collapses under autoregressive generation (GAR$=$0.064 on Qwen-2.5-7B, 0.018 on Llama-3.1-8B), revealing an 8$\\times$--27$\\times$ training--inference gap. We trace this failure to exposure bias: attention patterns learned on gold-text contexts do not transfer to model-generated contexts. A PCGrad ablation causally excludes gradient direction conflict as a contributing factor, while NTP gradient magnitude dominance (7.5--25.7$\\times$) drives gates toward identity. Four-way ablation confirms gating provides zero incremental benefit. Scheduled sampling compresses the gap from 8$\\times$ to ${\\sim}$1.3$\\times$ on Qwen (AR GAR$=$0.401$\\pm$0.047, 4 seeds) with no perplexity cost, though cross-model transfer to Llama is partial (gap$=$2.7$\\times$). These results provide the first empirical characterization of how exposure bias selectively destroys auxiliary attention losses in multi-turn settings.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nLarge language models exhibit progressive degradation in multi-turn dialogue: as conversations grow longer, models increasingly fail to attend to task-relevant information from early turns~\\cite{dongre2026gar,zheng2023judging}. \\citet{dongre2026gar} formalized this through the Goal Accessibility Ratio (GAR), documenting 27--48\\% drops across 12 models over 50 turns. Crucially, their residual stream probes reveal that goal information \\emph{persists} in hidden states (AUC up to 0.98) even as the attention channel closes---the information is present but inaccessible through attention.\n\nThis creates a natural architectural hypothesis: if goal information is retained in the residual stream but attention fails to route it, a learnable gate on the residual connection should recover accessibility. We implement this as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. The design is principled: gates modulate sub-layer output magnitude, allowing the model to selectively amplify or suppress layer contributions based on turn structure.\n\nThreadGate succeeds during training. On teacher-forced (TF) evaluation with gold-text contexts, GAR-ours reaches 0.50---a 25$\\times$ improvement over the base model's 0.019. However, under autoregressive (AR) generation with model-generated contexts, GAR-ours collapses to 0.064 on Qwen-2.5-7B (7.8$\\times$ gap) and 0.018 on Llama-3.1-8B (27$\\times$ gap). This dramatic discrepancy---attention patterns that work perfectly on gold text but fail completely on generated text---is the signature of exposure bias~\\cite{bengio2015scheduled,ranzato2016sequence}.\n\nOur analysis reveals three coupled mechanisms behind this failure: (1) the training--inference distribution shift is the primary cause, as confirmed by a PCGrad ablation that causally excludes gradient direction conflict; (2) NTP gradient magnitude dominates gate parameters by 7.5--25.7$\\times$, driving gates toward identity and producing reverse turn conditioning; (3) at inference time, gates attenuate sub-layer output by only 2--7\\%, far too weak to shift attention patterns. Four-way ablation (ThreadGate / Uniform Gate / LoRA-only / Base) confirms gating provides zero incremental contribution over LoRA fine-tuning alone.\n\nWe further show that scheduled sampling---mixing model-generated context during training---compresses the TF--AR gap from 8$\\times$ to ${\\sim}$1.3$\\times$ on Qwen (AR GAR $=$ 0.401$\\pm$0.047, 4 seeds) with no perplexity cost, though cross-model efficacy on Llama is partial (gap $=$ 2.7$\\times$). Inference-time $\\beta$-steering independently recovers GAR from 0.064 to 0.727. Our contributions are:\n\\begin{enumerate}\n    \\item The first empirical characterization of how exposure bias destroys auxiliary attention loss generalization (8$\\times$--27$\\times$ gap), specific to summary-position attention.\n    \\item Per-layer quantification of NTP--GAR gradient dynamics, with PCGrad causal exclusion of gradient direction conflict.\n    \\item Systematic four-way ablation isolating gating contributions across two model families.\n    \\item Cross-model validation (Qwen-2.5-7B + Llama-3.1-8B) confirming the generality of the failure mode.\n    \\item Initial evidence that scheduled sampling transfers to multi-turn auxiliary attention objectives, effective on Qwen but with reduced cross-model efficacy requiring further investigation.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Multi-Turn Dialogue Degradation.}\nGoal accessibility degradation in multi-turn LLM dialogue has been characterized by \\citet{dongre2026gar}, who introduced the GAR metric and documented systematic attention decay across 12 models. MT-Bench~\\cite{zheng2023judging} and MT-Bench-101~\\cite{bai2024mtbench101} evaluate multi-turn capabilities but focus on response quality rather than attention mechanisms. Lost-in-the-Middle~\\cite{liu2024lost} documents position-dependent retrieval failure in long contexts, a related but distinct phenomenon.\n\n\\paragraph{Residual Gating and Adaptive Depth.}\nResidual gating has been explored for adaptive computation depth. ReZero~\\cite{bachlechner2021rezero} initializes residual connections with learnable zero-initialized scalars. SkipNet~\\cite{wang2018skipnet} learns binary skip decisions. LayerDrop~\\cite{fan2020reducing} uses structured dropout during training. FlexiDepth~\\cite{luo2025flexidepth} enables per-token adaptive depth. Our ThreadGate differs in that gates are conditioned on turn structure and trained with an auxiliary attention objective rather than for computational efficiency.\n\n\\paragraph{Attention Steering and Intervention.}\nAttention sinks~\\cite{xiao2024efficient} reveal that initial tokens absorb disproportionate attention mass regardless of content. Gated attention mechanisms~\\cite{qiu2025gated} modulate attention weights within layers. Transformer circuits analysis~\\cite{elhage2021mathematical} provides mechanistic understanding of attention head specialization. Our work attempts to steer attention through residual gating rather than direct attention weight modification.\n\n\\paragraph{Exposure Bias.}\nThe training--inference distribution mismatch in autoregressive models was identified by \\citet{bengio2015scheduled}, who proposed scheduled sampling as a remedy. Subsequent work includes Professor Forcing~\\cite{lamb2016professor}, SEARNN~\\cite{leblond2018searnn}, and sequence-level training~\\cite{ranzato2016sequence,wiseman2016sequence}. \\citet{dou2022parallel} applied attention-forcing to NMT with data-dependent mode selection. Our contribution is demonstrating that this classical problem manifests with particular severity (8$\\times$--27$\\times$ gap) in auxiliary attention losses for multi-turn dialogue, and that time-scheduled sampling transfers to this setting.\n\n% ============================================================\n\\section{Background}\n\n\\subsection{Goal Accessibility Ratio}\n\nFollowing \\citet{dongre2026gar}, we measure how well a model's attention mechanism routes information from goal-specifying tokens to response generation positions. We define two GAR variants:\n\n\\textbf{GAR-ours} measures attention from the last token of each assistant response to goal tokens (system prompt + first user query):\n\\begin{equation}\n\\text{GAR-ours} = \\frac{1}{|H|} \\sum_{h \\in H} \\sum_{g \\in \\mathcal{G}} A_h[\\text{last}, g]\n\\end{equation}\nwhere $H$ is the set of attention heads, $\\mathcal{G}$ is the set of goal token positions, and $A_h[\\text{last}, g]$ is the attention weight from the last response token to goal token $g$ in head $h$.\n\n\\textbf{GAR-Dongre} uses all response tokens and restricts goals to system prompt task tokens only, enabling direct comparison with \\citet{dongre2026gar}.\n\n\\subsection{Residual Stream Persistence}\n\n\\citet{dongre2026gar} demonstrated via linear probes that goal information persists in residual stream representations (AUC up to 0.98) even at late turns where attention-based GAR has degraded severely. This dissociation---information present in hidden states but inaccessible through attention---motivates architectural interventions on the residual connection.\n\n% ============================================================\n\\section{Method}\n\n\\subsection{ThreadGate Architecture}\n\nThreadGate introduces a per-layer scalar gate $g_l \\in (0, 1)$ that modulates the sub-layer output in a ReZero-style residual connection:\n\\begin{equation}\n\\mathbf{x}_{l+1} = \\mathbf{x}_l + g_l \\cdot f_l(\\mathbf{x}_l)\n\\label{eq:gate}\n\\end{equation}\nwhere $f_l$ is the sub-layer transformation (self-attention or FFN) at layer $l$. When $g_l \\to 0$, the sub-layer becomes a no-op (identity); when $g_l \\to 1$, the full sub-layer output is retained.\n\nEach gate is computed by a 2-layer MLP conditioned on hidden state and turn structure:\n\\begin{equation}\ng_l = \\sigma\\!\\left(W_2 \\cdot \\text{ReLU}(W_1 \\cdot [\\text{proj}(\\mathbf{x}_l); \\text{emb}(t_d, t_i)] + b_1) + b_2\\right)\n\\end{equation}\nwhere $t_d$ is the turn distance (tokens since last turn boundary) and $t_i$ is the turn index. The gate produces per-token, per-layer values, enabling turn-aware modulation.\n\n\\textbf{Uniform Gate (UG)} uses the same architecture but replaces turn embeddings with a constant vector, isolating turn-conditioning effects while retaining content-dependent gating.\n\n\\textbf{LoRA-only} fixes $g_l = 1.0$ (no gating) while retaining the GAR loss, isolating the contribution of the gating mechanism itself.\n\n\\subsection{Training Objective}\n\nThe joint loss combines NTP and GAR terms:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_{\\text{NTP}} + \\lambda_{\\text{GAR}} \\cdot \\mathcal{L}_{\\text{GAR}} + \\lambda_{\\text{div}} \\cdot \\mathcal{L}_{\\text{div}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{GAR}}$ is an MSE loss pushing GAR toward a target value and $\\mathcal{L}_{\\text{div}}$ is a gate diversity regularizer preventing gate collapse. We set $\\lambda_{\\text{GAR}} = 1.0$ and $\\lambda_{\\text{div}} = 0.01$ by default.\n\nThe MSE+gate\\_div formulation (v7) was selected after iterating through four loss families: cumulative attention (v1--v2), maximize attention (v3--v5), smooth saturation (v6), and MSE target (v7). Only v7 achieved stable training convergence.\n\n\\subsection{Scheduled Sampling}\n\nTo address the training--inference distribution shift, we apply scheduled sampling (SS)~\\cite{bengio2015scheduled} adapted for multi-turn dialogue. During training, each assistant turn's context is constructed from either gold text (teacher forcing) or model-generated text (autoregressive), selected per-turn with probability $p_{\\text{ss}}(t)$ that increases linearly from 0 to 0.5 over the training epochs:\n\\begin{equation}\np_{\\text{ss}}(t) = \\min\\!\\left(0.5, \\frac{t}{T} \\cdot 0.5\\right)\n\\end{equation}\nwhere $t$ is the current step and $T$ is the total training steps. This exposes the model to its own generation distribution during training, reducing the TF--AR mismatch.\n\n\\subsection{Inference-Time $\\beta$-Steering}\n\nAt inference time, we amplify gate influence by raising gate values to a power $\\beta < 1$:\n\\begin{equation}\ng_l^{\\text{steer}} = g_l^{1/\\beta}\n\\end{equation}\nFor $\\beta > 1$, gates closer to 1.0 are pushed further from identity, amplifying the sub-layer modulation that gates learned during training but apply too weakly at inference.\n\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Models.} We conduct primary experiments on Qwen-2.5-7B (28 layers, GQA) and cross-model validation on Llama-3.1-8B (32 layers, 8 KV heads).\n\n\\paragraph{Data.} Training uses UltraChat~\\cite{ding2023enhancing} multi-turn conversations. Evaluation uses held-out conversations: $N{=}200$ for TF evaluation and $N{=}50$ for AR evaluation on Qwen; $N{=}20$ for Llama AR evaluation.\n\n\\paragraph{Training.} All models are fine-tuned with LoRA (rank 16) for 3 epochs. Seed$=$42 for primary experiments; seeds \\{42, 123, 456, 789\\} for SS multi-seed validation. Training uses bfloat16 mixed precision on a single A100 80GB GPU.\n\n\\paragraph{Evaluation Protocol.} We evaluate under two conditions: (1) \\textbf{Teacher-forced (TF)}: model processes gold-text conversations, measuring attention patterns on the training distribution; (2) \\textbf{Autoregressive (AR)}: model generates its own responses turn by turn, measuring attention patterns on the inference distribution. The TF/AR gap quantifies the exposure bias effect.\n\n\\subsection{Main Results: Four-Way Ablation}\n\nTable~\\ref{tab:main} presents the four-way ablation on Qwen-2.5-7B with $N{=}200$ TF evaluation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Four-way ablation on Qwen-2.5-7B. TF evaluation uses $N{=}200$ conversations with 95\\% bootstrap CI. All fine-tuned variants achieve comparable TF GAR ($\\sim$0.50) and PPL ($\\sim$2.78), but AR GAR collapses uniformly. Gating provides zero incremental benefit over LoRA-only.}\n\\label{tab:main}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nVariant & GAR-ours & 95\\% CI & GAR-D & PPL \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Teacher-Forced (TF) Evaluation, N=200}} \\\\\nBase & 0.013 & [0.010, 0.016] & 0.003 & 4.34 \\\\\nThreadGate & 0.504 & [0.489, 0.519] & 0.015 & 2.78 \\\\\nUniform Gate & 0.506 & [0.491, 0.521] & 0.012 & 2.78 \\\\\nLoRA-only & 0.499 & [0.483, 0.514] & 0.013 & 2.78 \\\\\n\\midrule\nTG$-$LO diff & +0.006 & [$-$0.001, 0.003] & +0.002 & 0.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll three fine-tuned variants (ThreadGate, Uniform Gate, LoRA-only) achieve near-identical TF GAR-ours ($\\sim$0.50) and perplexity ($\\sim$2.78). The TG--LO difference CI includes zero, confirming that gating provides no measurable benefit. The $N{=}200$ evaluation reduces CI width by 42\\% compared to $N{=}50$, strengthening the null result.\n\nUnder AR generation, all variants collapse: ThreadGate AR GAR-ours $=$ 0.064, producing an 8$\\times$ gap (Qwen) that widens to 27$\\times$ on Llama-3.1-8B. GAR-Dongre shows uniformly low values ($<$0.02) in both TF and AR conditions, indicating that the distribution shift selectively affects summary-position (last-token) attention patterns.\n\n\\subsection{Inference-Time $\\beta$-Steering}\n\n$\\beta$-steering amplifies gate influence at inference time without retraining. On Qwen-2.5-7B, GAR-ours increases from 0.064 ($\\beta{=}0$) to 0.727 ($\\beta{=}5$), demonstrating that the gate contains latent structure that is underutilized at default scale. However, this is a post-hoc intervention that does not address the underlying distribution shift.\n\n\\subsection{Scheduled Sampling Results}\n\n\\paragraph{Qwen-2.5-7B (4-seed).}\nTable~\\ref{tab:ss_seeds} presents SS results across 4 seeds. SS compresses the TF--AR gap from 8$\\times$ to 1.24$\\times$ (mean), with AR GAR-ours $=$ 0.405$\\pm$0.040 at $\\beta{=}0$ and no perplexity cost (PPL 1.441$\\pm$0.001).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scheduled sampling results on Qwen-2.5-7B across 4 seeds. $\\beta$ controls inference-time gate amplification. Effect size / std $=$ 9.7 at $\\beta{=}0$, confirming statistical significance.}\n\\label{tab:ss_seeds}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nSeed & TF GAR & AR $\\beta{=}0$ & AR $\\beta{=}3$ & AR $\\beta{=}5$ & PPL \\\\\n\\midrule\ns42 & 0.503 & 0.347 & 0.593 & 0.717 & 1.442 \\\\\ns123 & 0.495 & 0.423 & 0.590 & 0.717 & 1.441 \\\\\ns456 & 0.496 & 0.433 & 0.605 & 0.716 & 1.439 \\\\\ns789 & --- & 0.415 & 0.598 & 0.718 & 1.440 \\\\\n\\midrule\nMean$\\pm$Std & 0.498$\\pm$.004 & 0.405$\\pm$.040 & 0.597$\\pm$.007 & 0.717$\\pm$.001 & 1.441$\\pm$.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\beta{\\geq}3$, cross-seed variance drops below 0.01, indicating that inference-time steering is a deterministic intervention independent of training seed randomness. Seed s42 is a mild outlier at $\\beta{=}0$ (0.347, $-$1.15$\\sigma$ from mean) but converges with other seeds at higher $\\beta$.\n\n\\paragraph{Cross-Model: Llama-3.1-8B.}\nTable~\\ref{tab:cross_model_ss} compares SS efficacy across model families. SS is effective on Llama (20$\\times$ improvement over base, gap compressed from 27$\\times$ to 2.7$\\times$), but substantially weaker than on Qwen (AR GAR 0.18 vs.\\ 0.40, gap 2.7$\\times$ vs.\\ 1.3$\\times$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model SS comparison. SS is effective on both models but with reduced efficacy on Llama-3.1-8B. $\\beta$-steering narrows the cross-model gap at higher values.}\n\\label{tab:cross_model_ss}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMetric & Qwen-2.5-7B & Llama-3.1-8B & Ratio \\\\\n\\midrule\nBase AR GAR & 0.019 & 0.009 & 2.1$\\times$ \\\\\nTG AR GAR (no SS) & 0.064 & 0.018 & 3.6$\\times$ \\\\\nSS AR GAR $\\beta{=}0$ & 0.401$\\pm$.047 & 0.18$\\pm$.09 & 2.2$\\times$ \\\\\nSS AR GAR $\\beta{=}3$ & 0.596$\\pm$.008 & 0.45 & 1.3$\\times$ \\\\\nSS AR GAR $\\beta{=}5$ & 0.717$\\pm$.001 & 0.62 & 1.2$\\times$ \\\\\nTF GAR & 0.498$\\pm$.004 & 0.485 & 1.03$\\times$ \\\\\nSS Gap (TF/AR $\\beta{=}0$) & 1.26$\\times$ & 2.7$\\times$ & --- \\\\\nTG Gap (no SS) & 8$\\times$ & 27$\\times$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\beta{=}5$, the cross-model gap narrows to 1.2$\\times$ (Llama 0.62 vs.\\ Qwen 0.72), suggesting that inference-time steering generalizes better than training-time SS across architectures.\n\n% ============================================================\n\\section{Analysis}\n\n\\subsection{Gate Turn Conditioning}\n\nAnalysis of gate activation profiles reveals that 27 of 28 layers exhibit \\emph{reverse} turn conditioning: gate values at early turns (where GAR is highest and intervention is least needed) are lower than at late turns (where GAR has degraded and intervention is most needed). Gate mean across layers is 0.93--0.98 at late turns, producing only 2--7\\% sub-layer attenuation---too weak to meaningfully shift attention patterns. This reverse conditioning arises because NTP loss gradients dominate gate parameters, pushing gates toward 1.0 (preserving full layer computation) most strongly at late turns where NTP loss is highest.\n\n\\subsection{PCGrad Causal Exclusion of Gradient Conflict}\n\\label{sec:pcgrad}\n\nWe observe that NTP and GAR gradients conflict in direction (cosine similarity $<$ 0) in 67--79\\% of layers, with NTP magnitude dominating by 7.5--14.7$\\times$ on Qwen. To test whether this directional conflict causally contributes to GAR collapse, we train a PCGrad variant~\\cite{yu2020gradient} that projects conflicting gradients to eliminate directional interference.\n\nPCGrad successfully eliminates directional conflict (post-projection $\\cos_{\\text{sim}}$ oscillates around 0, range $-$0.151 to $+$0.091). However, $\\mathcal{L}_{\\text{GAR}}$ collapse trajectory is unchanged and shows no delay. Inference evaluation confirms: PCGrad GAR-ours $=$ 0.0151 vs.\\ standard v7 $=$ 0.0157 (difference $<$ 0.1pp); PCGrad PPL $=$ 2.780 vs.\\ v7 PPL $=$ 2.784. All observable metrics are statistically identical, establishing that gradient direction conflict is neither necessary nor sufficient for the 8$\\times$--27$\\times$ GAR gap. Exposure bias (distribution shift) alone is sufficient.\n\n\\subsection{Distribution Shift Compounds Over Conversation Length}\n\nTable~\\ref{tab:long_conv} shows that the TF--AR gap grows with conversation length, consistent with cumulative distribution shift as model-generated context accumulates.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{GAR gap versus conversation length ($N{=}15$ conversations with $\\geq$12 turns). TG gap grows from 12$\\times$ to 45$\\times$ as turns increase. SS mitigates but does not eliminate the length effect.}\n\\label{tab:long_conv}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nTurns & Base & TG AR & SS AR & TG Gap & SS Gap \\\\\n\\midrule\n3--5 & 0.016 & 0.042 & 0.38 & 12$\\times$ & 1.32$\\times$ \\\\\n6--10 & 0.010 & 0.020 & 0.32 & 25$\\times$ & 1.56$\\times$ \\\\\n11--15 & 0.006 & 0.011 & 0.25 & 45$\\times$ & 2.0$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTF GAR remains stable at $\\sim$0.50 regardless of conversation length (gold-text context quality does not degrade), while AR GAR decays monotonically. The 45$\\times$ gap at turns 11--15 reflects severe cumulative error: each turn's model-generated text shifts the context distribution further from training conditions. SS reduces but does not eliminate this compounding (gap 1.32$\\times$ to 2.0$\\times$), suggesting that SS generalization has limits beyond the training turn-length distribution.\n\n\\subsection{Mechanism Specificity: KL Divergence Analysis}\n\nTo characterize \\emph{where} in the attention space exposure bias manifests, we compute per-head KL divergence $D_{\\text{KL}}(P_{\\text{TF}} \\| P_{\\text{AR}})$ across 50 conversations (Table~\\ref{tab:kl}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TF--AR attention KL divergence by layer group. Distribution shift concentrates in deep layers (L21--27), where gates attempt the most intervention.}\n\\label{tab:kl}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nLayer Group & TG KL & Base KL & TG/Base \\\\\n\\midrule\nL0--6 (shallow) & 0.031 & 0.028 & 1.11 \\\\\nL7--13 (lower-mid) & 0.042 & 0.036 & 1.17 \\\\\nL14--20 (upper-mid) & 0.058 & 0.045 & 1.29 \\\\\nL21--27 (deep) & 0.089 & 0.065 & 1.37 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTG models show larger KL divergence than base models (mean 0.054 vs.\\ 0.043), because TG training shapes attention patterns specifically for the TF distribution, which then shift more under AR conditions. The effect concentrates in deep layers (L21--27, TG/Base ratio 1.37), precisely where gates attempt the most intervention.\n\nTable~\\ref{tab:gar_defs} reveals that GAR sensitivity to distribution shift varies dramatically across token selection criteria.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{GAR definition sensitivity to TF--AR distribution shift. Summary-position attention (last-token, goal-only) is highly sensitive; distributed attention (all-token, first-token) is robust.}\n\\label{tab:gar_defs}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nDefinition & TF & AR & Gap & Sensitivity \\\\\n\\midrule\nLast token (ours) & 0.504 & 0.016 & 32$\\times$ & High \\\\\nGoal-only & 0.630 & 0.010 & 63$\\times$ & Very high \\\\\nAll tokens & 0.028 & 0.016 & 1.7$\\times$ & Low \\\\\nFirst token & 0.035 & 0.019 & 1.8$\\times$ & Low \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLast-token and goal-only GAR definitions, which measure long-range attention routing to specific positions, exhibit 32--63$\\times$ gaps. All-token and first-token definitions, which measure more distributed or local attention, show only 1.7--1.8$\\times$ gaps. This demonstrates that exposure bias \\emph{selectively} disrupts summary-position attention patterns that depend on long-range context quality, while leaving local attention patterns largely unaffected.\n\n\\subsection{Alternative GAR Definition Robustness of SS}\n\nTable~\\ref{tab:gar_alt} tests whether SS improvements generalize across GAR definitions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SS effect across alternative GAR definitions (AR evaluation on Qwen). SS improves 3 of 4 definitions; goal-only remains resistant.}\n\\label{tab:gar_alt}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nToken Selection & Base & TG & SS & Improves? \\\\\n\\midrule\nLast (GAR-ours) & 0.019 & 0.064 & 0.401 & Yes (21$\\times$) \\\\\nAll tokens & 0.018 & 0.025 & 0.360 & Yes (20$\\times$) \\\\\nFirst token & 0.020 & 0.039 & 0.250 & Yes (12.5$\\times$) \\\\\nGoal-only & 0.012 & 0.015 & 0.060 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSS improves 3 of 4 definitions, indicating that it builds broader goal-attention patterns rather than overfitting to the trained definition. TG without SS only improves the trained definition (last-token: 0.064 vs.\\ base 0.019), confirming position-specific overfitting under teacher forcing. The most restrictive definition (goal-only) remains resistant even to SS, suggesting that precise goal-token routing requires mechanisms beyond distributional correction.\n\n\\subsection{Cross-Model Gradient Analysis}\n\nTable~\\ref{tab:grad_cross} compares NTP--GAR gradient dynamics across architectures.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model gradient analysis. Llama shows orthogonal (not conflicting) gradients but more extreme NTP magnitude dominance, correlating with a larger TG gap.}\n\\label{tab:grad_cross}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMetric & Qwen-2.5-7B & Llama-3.1-8B & Interp. \\\\\n\\midrule\n$\\cos_{\\text{sim}}$ (final) & $-$0.042 & $+$0.005 & Qwen: mild conflict \\\\\n & & & Llama: orthogonal \\\\\nneg\\_layers \\% & 67.9\\% & 53.1\\% & Qwen: moderate \\\\\n & & & Llama: near-random \\\\\nmag\\_ratio & 14.7$\\times$ & 25.7$\\times$ & Llama NTP \\\\\n & & & dominance stronger \\\\\nTG AR GAR gap & 8$\\times$ & 27$\\times$ & Correlates with \\\\\n & & & mag\\_ratio \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLlama's gradient dynamics differ qualitatively from Qwen: gradients are near-orthogonal ($\\cos_{\\text{sim}} \\approx 0$) rather than conflicting, and NTP magnitude dominance is more extreme (25.7$\\times$ vs.\\ 14.7$\\times$). The correlation between magnitude ratio and TG gap size (14.7$\\times$ mag $\\to$ 8$\\times$ gap; 25.7$\\times$ mag $\\to$ 27$\\times$ gap) suggests that NTP dominance, not directional conflict, is the relevant gradient-level predictor of GAR collapse severity.\n\n\\subsection{$\\lambda_{\\text{GAR}}$ Sensitivity}\n\nTable~\\ref{tab:lambda} tests whether rebalancing gradient magnitudes resolves the gap.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\lambda_{\\text{GAR}}$ sensitivity. Even 10$\\times$ GAR weight, which balances NTP and GAR gradient magnitudes, leaves a 22$\\times$ gap. Distribution shift, not gradient competition, is the bottleneck.}\n\\label{tab:lambda}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n$\\lambda_{\\text{GAR}}$ & TF GAR & AR GAR & Gap & PPL & Gate $\\mu$ \\\\\n\\midrule\n0.1 & 0.42 & 0.013 & 32.3$\\times$ & 2.76 & 0.972 \\\\\n1.0 (default) & 0.50 & 0.016 & 32.1$\\times$ & 2.78 & 0.934 \\\\\n10.0 & 0.535 & 0.024 & 22.3$\\times$ & 2.95 & 0.905 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\lambda_{\\text{GAR}}{=}10$, GAR gradients reach parity with NTP in magnitude, gates achieve wider dynamic range (std 0.082 vs.\\ 0.049), and TF GAR improves to 0.535. Yet AR GAR rises only marginally (0.024), leaving a 22$\\times$ gap. The PPL increase (+6\\%) reflects reduced NTP optimization budget. This confirms that gradient magnitude imbalance is not the bottleneck: even with balanced gradients, exposure bias prevents TF-trained attention patterns from transferring to AR generation.\n\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why Exposure Bias Selectively Destroys Auxiliary Attention Losses.}\nOur results reveal a specificity in how exposure bias manifests: it selectively disrupts summary-position attention (32--63$\\times$ gap for last-token and goal-only GAR) while leaving distributed attention largely unaffected (1.7--1.8$\\times$ for all-token and first-token). This selectivity arises because last-token attention depends on long-range context quality---the precise dimension along which gold and generated text diverge most.\n\n\\paragraph{Why NTP Self-Recovers but GAR Does Not.}\nNTP loss, computed on the current token given preceding context, is inherently local: even with degraded context, the model can partially recover by relying on short-range dependencies. GAR-ours, by contrast, requires accurate long-range attention routing from the response's final token to goal tokens in the system prompt, making it maximally sensitive to context distribution shifts.\n\n\\paragraph{SS Transferability Limitations.}\nWhile SS compresses the TF--AR gap to $\\sim$1.3$\\times$ on Qwen (AR GAR 0.401$\\pm$0.040, 4 seeds), its efficacy on Llama-3.1-8B is substantially reduced (gap 2.7$\\times$, AR GAR 0.18$\\pm$0.09). Several architectural differences may explain this: (1) Llama uses GQA with 8 KV heads, potentially limiting the attention routing capacity available for goal-relevant patterns; (2) Llama's 32 layers (vs.\\ Qwen's 28) dilute the SS correction signal across more gate--NTP interaction points; (3) Llama's more extreme NTP magnitude dominance (25.7$\\times$ vs.\\ 14.7$\\times$) may create a steeper optimization landscape for gate learning even under SS. The convergence of both models at high $\\beta$ ($\\beta{=}5$: Llama 0.62, Qwen 0.72) suggests that inference-time steering transfers better than training-time SS across architectures, indicating that the limitation is in SS training dynamics rather than a fundamental attention capacity constraint.\n\n\\paragraph{Implications for Attention Steering Methods.}\nOur findings suggest that any attention steering method trained with teacher forcing and evaluated under autoregressive generation faces the risk of this distribution shift. The 8$\\times$--27$\\times$ gap we measure provides a concrete risk benchmark. Methods that operate at inference time (e.g., $\\beta$-steering, activation engineering) may be more robust to this failure mode, as they bypass the training distribution entirely. Future work should investigate (1) model-specific SS schedule optimization, (2) decoupled goal-processing pathways that bypass the residual connection, and (3) GAR-aware decoding strategies.\n\n% ============================================================\n\\section{Conclusion}\n\nWe present the first empirical characterization of how exposure bias destroys auxiliary attention loss generalization in multi-turn dialogue. ThreadGate, a per-layer residual gating module, achieves GAR-ours $=$ 0.50 under teacher forcing but collapses to 0.064 (Qwen) and 0.018 (Llama) under autoregressive generation, an 8$\\times$--27$\\times$ gap. PCGrad ablation causally excludes gradient direction conflict, identifying distribution shift as the sole cause. Four-way ablation confirms gating provides zero incremental benefit. Scheduled sampling compresses the gap to $\\sim$1.3$\\times$ on Qwen (AR GAR 0.401$\\pm$0.040, 4 seeds) but with reduced cross-model efficacy (Llama gap $=$ 2.7$\\times$), establishing SS as a promising but model-dependent mitigation strategy for auxiliary attention objectives.\n\n% ============================================================\n\\section*{Limitations}\n\nOur experiments are conducted on two 7--8B parameter models; the generalization of the 8$\\times$--27$\\times$ gap to larger or smaller models remains untested. The evaluation uses GAR as a proxy metric for goal accessibility rather than downstream task performance (e.g., instruction following accuracy). SS multi-seed validation uses 4 seeds on Qwen and a single seed on Llama, limiting statistical power for the cross-model comparison.\n\n% ============================================================\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Bachlechner et~al.(2021)]{bachlechner2021rezero}\nThomas Bachlechner, Bodhisattwa~Prasad Majumder, Huanru~Henry Mao, Gary~W. Garrison, Bhanu~Pratap Laker, and Julian McAuley. 2021. ReZero is All You Need: Fast Convergence at Large Depth. In \\emph{UAI}.\n\n\\bibitem[Bai et~al.(2024)]{bai2024mtbench101}\nYushi Bai, Xin Lv, Jiajie Zhang, Yuze He, Ji Qi, Lei Hou, Zhiyuan Liu, Juanzi Li, and Jie Tang. 2024. MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogue. In \\emph{ACL}.\n\n\\bibitem[Bengio et~al.(2015)]{bengio2015scheduled}\nSamy Bengio, Oriol Vinyals, Navdeep Jaitly, and Noam Shazeer. 2015. Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks. In \\emph{NeurIPS}.\n\n\\bibitem[Ding et~al.(2023)]{ding2023enhancing}\nNing Ding, Yulin Chen, Bokai Xu, Yujia Qin, Zhi Zheng, Shengding Hu, Zhiyuan Liu, Maosong Sun, and Bowen Zhou. 2023. Enhancing Chat Language Models by Scaling High-quality Instructional Conversations. In \\emph{EMNLP}.\n\n\\bibitem[Dongre et~al.(2026)]{dongre2026gar}\nAmey Dongre, et~al. 2026. Goal Accessibility Ratio: Measuring Multi-Turn Dialogue Degradation. \\emph{Preprint}.\n\n\\bibitem[Dou and Gales(2022)]{dou2022parallel}\nZi-Yi Dou and Mark Gales. 2022. Parallel Attention Forcing for Machine Translation. In \\emph{NAACL}.\n\n\\bibitem[Elhage et~al.(2021)]{elhage2021mathematical}\nNelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, and Chris Olah. 2021. A Mathematical Framework for Transformer Circuits. \\emph{Transformer Circuits Thread}.\n\n\\bibitem[Fan et~al.(2020)]{fan2020reducing}\nAngela Fan, Edouard Grave, and Armand Joulin. 2020. Reducing Transformer Depth on Demand with Structured Dropout. In \\emph{ICLR}.\n\n\\bibitem[Lamb et~al.(2016)]{lamb2016professor}\nAlex~M. Lamb, Anirudh Goyal, Ying Zhang, Saizheng Zhang, Aaron~C. Courville, and Yoshua Bengio. 2016. Professor Forcing: A New Algorithm for Training Recurrent Networks. In \\emph{NeurIPS}.\n\n\\bibitem[Leblond et~al.(2018)]{leblond2018searnn}\nR{\\'e}mi Leblond, Jean-Baptiste Alayrac, Anton Osokin, and Simon Lacoste-Julien. 2018. SEARNN: Training RNNs with Global-Local Losses. In \\emph{ICLR}.\n\n\\bibitem[Liu et~al.(2024)]{liu2024lost}\nNelson~F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2024. Lost in the Middle: How Language Models Use Long Contexts. \\emph{TACL}.\n\n\\bibitem[Luo et~al.(2025)]{luo2025flexidepth}\nYifan Luo, et~al. 2025. FlexiDepth: Dynamic Depth for Efficient Transformers. \\emph{Preprint}.\n\n\\bibitem[Qiu et~al.(2025)]{qiu2025gated}\nXin Qiu, et~al. 2025. Gated Attention Mechanisms for Controlled Generation. \\emph{Preprint}.\n\n\\bibitem[Ranzato et~al.(2016)]{ranzato2016sequence}\nMarc'Aurelio Ranzato, Sumit Chopra, Michael Auli, and Wojciech Zaremba. 2016. Sequence Level Training with Recurrent Neural Networks. In \\emph{ICLR}.\n\n\\bibitem[Wang et~al.(2018)]{wang2018skipnet}\nXin Wang, Fisher Yu, Zi-Yi Dou, Trevor Darrell, and Joseph~E. Gonzalez. 2018. SkipNet: Learning Dynamic Routing in Convolutional Networks. In \\emph{ECCV}.\n\n\\bibitem[Wiseman and Rush(2016)]{wiseman2016sequence}\nSam Wiseman and Alexander~M. Rush. 2016. Sequence-to-Sequence Learning as Beam-Search Optimization. In \\emph{EMNLP}.\n\n\\bibitem[Xiao et~al.(2024)]{xiao2024efficient}\nGuangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. 2024. Efficient Streaming Language Models with Attention Sinks. In \\emph{ICLR}.\n\n\\bibitem[Yu et~al.(2020)]{yu2020gradient}\nTianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol Hausman, and Chelsea Finn. 2020. Gradient Surgery for Multi-Task Learning. In \\emph{NeurIPS}.\n\n\\bibitem[Zheng et~al.(2023)]{zheng2023judging}\nLianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric~P. Xing, Hao Zhang, Joseph~E. Gonzalez, and Ion Stoica. 2023. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In \\emph{NeurIPS}.\n\n\\end{thebibliography}\n\n% ============================================================\n\\appendix\n\\section{$\\lambda_{\\text{GAR}}$ Sensitivity Details}\n\nSee Table~\\ref{tab:lambda} in the main text. The three-point sweep ($\\lambda \\in \\{0.1, 1.0, 10.0\\}$) confirms that even 10$\\times$ GAR weight, which brings NTP and GAR gradient magnitudes to approximate parity (effective ratio 0.75--1.47$\\times$), leaves a 22$\\times$ TF--AR gap. Gate dynamic range increases with $\\lambda$ (std 0.022 $\\to$ 0.049 $\\to$ 0.082), but the additional gate freedom is directed toward TF optimization rather than AR generalization.\n\n\\section{4-Seed vs.\\ 3-Seed Comparison}\n\nAdding seed s789 (AR GAR $\\beta{=}0$ $=$ 0.415) reduces the standard deviation from 0.047 to 0.040 ($-$15\\%) and increases the effect size / std ratio from 8.2 to 9.7 ($+$18\\%). The 4-seed mean (0.405) is within 0.004 of the 3-seed mean (0.401), confirming stability.\n\n\\section{Llama-3.1-8B Detailed SS Results}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Llama-3.1-8B SS results at different $\\beta$ values. Improvement over base is substantial (20$\\times$ at $\\beta{=}0$) but weaker than Qwen.}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nCondition & AR GAR-ours & AR GAR-D & PPL & vs.\\ Base \\\\\n\\midrule\nBase & 0.009 & 0.005 & 1.27 & --- \\\\\nTG (no SS) & 0.018 & 0.018 & 1.32 & 2$\\times$ \\\\\nLO (no SS) & 0.018 & 0.020 & 1.32 & 2$\\times$ \\\\\nSS $\\beta{=}0$ & 0.18 & 0.25 & 1.40 & 20$\\times$ \\\\\nSS $\\beta{=}3$ & 0.45 & 0.38 & 1.55 & 50$\\times$ \\\\\nSS $\\beta{=}5$ & 0.62 & 0.48 & 1.72 & 69$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "3b5859ff-ed46-4991-99d5-c77cde892264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_g…",
  "leafUuid": "4fc5f01a-18d0-435d-a6c2-7e5edf5cc74d",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on residual gating mechanisms",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b"
}
```

---

### Tool call

_source line 25 · 2026-05-24T08:57:12.365Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jqary4UxYB3g5mq5X7v2YA`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fc5f01a-18d0-435d-a6c2-7e5edf5cc74d",
  "isSidechain": false,
  "requestId": "req_011CbM7gfgHXnhwa1vyZ5hMR",
  "type": "assistant",
  "uuid": "9a5dcbf2-837a-442e-b6e7-9a923502d371",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtQvmNvhQYDXFf5LZV87XD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12765,
      "cache_read_input_tokens": 51728,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12765,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 51728,
          "cache_creation_input_tokens": 12765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12765
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

_source line 26 · 2026-05-24T08:57:12.588Z_

<details><summary>↩ Tool result · reported error · `toolu_01Jqary4UxYB3g5mq5X7v2YA`</summary>

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
  "parentUuid": "9a5dcbf2-837a-442e-b6e7-9a923502d371",
  "isSidechain": false,
  "promptId": "67a87842-f41b-4d9e-9fbd-faa3f9849a08",
  "type": "user",
  "uuid": "336a06c8-975a-4ee3-a599-98cbcdce56b6",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "9a5dcbf2-837a-442e-b6e7-9a923502d371",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-24T08:57:21.292Z_

<details><summary>Logged reasoning block</summary>

```text
The acl.sty file is not available. Let me switch to a simpler document class or find what's available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "336a06c8-975a-4ee3-a599-98cbcdce56b6",
  "isSidechain": false,
  "requestId": "req_011CbM7h6gSZxqKQP9UzsKxd",
  "type": "assistant",
  "uuid": "a55fbbc0-4957-4cb7-81c4-b07997e64f62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iAk937bzVjBtujj3E6NGC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 64493,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 64493,
          "cache_creation_input_tokens": 475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 475
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

_source line 28 · 2026-05-24T08:57:21.801Z_

ACL style not available. Let me switch to a standard article class with appropriate formatting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a55fbbc0-4957-4cb7-81c4-b07997e64f62",
  "isSidechain": false,
  "requestId": "req_011CbM7h6gSZxqKQP9UzsKxd",
  "type": "assistant",
  "uuid": "4617326c-d92c-4ffe-924f-60509fcb0ab2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iAk937bzVjBtujj3E6NGC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 64493,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 64493,
          "cache_creation_input_tokens": 475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 475
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

_source line 29 · 2026-05-24T08:57:23.930Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KU7Vo7eXhXUJxD9jY5jS9X`</summary>

```json
{
  "command": "kpsewhich acl.sty 2>/dev/null; kpsewhich acl_natbib.bst 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/*.sty 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/*.cls 2>/dev/null; kpsewhich natbib.sty",
  "description": "Check available LaTeX styles"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4617326c-d92c-4ffe-924f-60509fcb0ab2",
  "isSidechain": false,
  "requestId": "req_011CbM7h6gSZxqKQP9UzsKxd",
  "type": "assistant",
  "uuid": "dc905ff8-360f-4682-8817-5c35fa4845de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iAk937bzVjBtujj3E6NGC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 64493,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 64493,
          "cache_creation_input_tokens": 475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 475
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

_source line 30 · 2026-05-24T08:57:24.261Z_

<details><summary>↩ Tool result · `toolu_01KU7Vo7eXhXUJxD9jY5jS9X`</summary>

```text
/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc905ff8-360f-4682-8817-5c35fa4845de",
  "isSidechain": false,
  "promptId": "67a87842-f41b-4d9e-9fbd-faa3f9849a08",
  "type": "user",
  "uuid": "70e8f657-e710-4318-bfe0-5a6b1c87f439",
  "toolUseResult": {
    "stdout": "/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "dc905ff8-360f-4682-8817-5c35fa4845de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-24T08:57:24.266Z_

```json
{
  "parentUuid": "70e8f657-e710-4318-bfe0-5a6b1c87f439",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "dcd383e8-caad-4aff-b5f1-b56e7ca604c9",
  "timestamp": "2026-05-24T08:57:24.266Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 32 · 2026-05-24T08:57:30.251Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01STgz8CH4sdHgtDhjYCTEAG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex",
  "old_string": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{subcaption}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{natbib}\n\\usepackage[colorlinks,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcd383e8-caad-4aff-b5f1-b56e7ca604c9",
  "isSidechain": false,
  "requestId": "req_011CbM7hxeXJt3urDseRdeSp",
  "type": "assistant",
  "uuid": "4ceee726-828a-486f-8018-25f85db57fec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012drEQaSbscv5t4GSEkdpqu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 403,
      "cache_read_input_tokens": 64968,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 403,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 397,
          "cache_read_input_tokens": 64968,
          "cache_creation_input_tokens": 403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 403
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

_source line 33 · 2026-05-24T08:57:30.267Z_

<details><summary>↩ Tool result · `toolu_01STgz8CH4sdHgtDhjYCTEAG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ceee726-828a-486f-8018-25f85db57fec",
  "isSidechain": false,
  "promptId": "67a87842-f41b-4d9e-9fbd-faa3f9849a08",
  "type": "user",
  "uuid": "bbe300c4-4360-45de-af1f-2b7185140694",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex",
    "oldString": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{subcaption}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{natbib}\n\\usepackage[colorlinks,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          "-\\documentclass[11pt]{article}",
          "-\\usepackage[hyperref]{acl}",
          "+\\documentclass[11pt,a4paper]{article}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath}"
        ]
      },
      {
        "oldStart": 9,
        "oldLines": 6,
        "newStart": 9,
        "newLines": 8,
        "lines": [
          " \\usepackage{graphicx}",
          " \\usepackage{xcolor}",
          " \\usepackage{subcaption}",
          "+\\usepackage{natbib}",
          "+\\usepackage[colorlinks,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}",
          " ",
          " \\title{Exposure Bias Selectively Destroys Auxiliary Attention Losses\\\\in Multi-Turn Dialogue}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "4ceee726-828a-486f-8018-25f85db57fec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-24T08:57:32.386Z_

Also need to remove the acl bibliography style reference and replace it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbe300c4-4360-45de-af1f-2b7185140694",
  "isSidechain": false,
  "requestId": "req_011CbM7iQJNRwjVcAq5q6Qjs",
  "type": "assistant",
  "uuid": "0d9e5467-ed8e-473d-ab78-dbf37d7a7b16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wnsrzr4oS7zqUqUjSqWTdq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 65371,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 65371,
          "cache_creation_input_tokens": 484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 484
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

_source line 35 · 2026-05-24T08:57:33.592Z_

<details open><summary>🔧 Tool call — Edit · `toolu_016X2mWT7ktM1pqPsjedB1Yk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{30}",
  "new_string": "\\begin{thebibliography}{30}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d9e5467-ed8e-473d-ab78-dbf37d7a7b16",
  "isSidechain": false,
  "requestId": "req_011CbM7iQJNRwjVcAq5q6Qjs",
  "type": "assistant",
  "uuid": "046bfeb1-e813-4011-a443-5ff492cea72c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wnsrzr4oS7zqUqUjSqWTdq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 65371,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 65371,
          "cache_creation_input_tokens": 484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 484
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

_source line 36 · 2026-05-24T08:57:33.603Z_

<details><summary>↩ Tool result · `toolu_016X2mWT7ktM1pqPsjedB1Yk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "046bfeb1-e813-4011-a443-5ff492cea72c",
  "isSidechain": false,
  "promptId": "67a87842-f41b-4d9e-9fbd-faa3f9849a08",
  "type": "user",
  "uuid": "cc7e4800-ebc2-408c-abbe-bbeeff903622",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{30}",
    "newString": "\\begin{thebibliography}{30}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 401,
        "oldLines": 9,
        "newStart": 401,
        "newLines": 6,
        "lines": [
          " Our experiments are conducted on two 7--8B parameter models; the generalization of the 8$\\times$--27$\\times$ gap to larger or smaller models remains untested. The evaluation uses GAR as a proxy metric for goal accessibility rather than downstream task performance (e.g., instruction following accuracy). SS multi-seed validation uses 4 seeds on Qwen and a single seed on Llama, limiting statistical power for the cross-model comparison.",
          " ",
          " % ============================================================",
          "-\\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          "-",
          " \\begin{thebibliography}{30}",
          " ",
          " \\bibitem[Bachlechner et~al.(2021)]{bachlechner2021rezero}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "046bfeb1-e813-4011-a443-5ff492cea72c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-24T08:57:37.484Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017fADxU4kZp3SwmfBMHynBi`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc7e4800-ebc2-408c-abbe-bbeeff903622",
  "isSidechain": false,
  "requestId": "req_011CbM7ieuCxXoYVQsc7HCB4",
  "type": "assistant",
  "uuid": "fb66ba28-027a-49c6-822f-bc8c254440ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwQKiRMEGRMv2WBoWsrj7j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 280,
      "cache_read_input_tokens": 65855,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 280,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 65855,
          "cache_creation_input_tokens": 280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 280
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

_source line 38 · 2026-05-24T08:57:39.062Z_

<details><summary>↩ Tool result · `toolu_017fADxU4kZp3SwmfBMHynBi`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `dongre2026gar' on page 1 undefined on input l
ine 30.


Package natbib Warning: Citation `zheng2023judging' on page 1 undefined on inpu
t line 30.


Package natbib Warning: Citation `dongre2026gar' on page 1 undefined on input l
ine 30.


Package natbib Warning: Citation `bengio2015scheduled' on page 1 undefined on i
nput line 34.


Package natbib Warning: Citation `ranzato2016sequence' on page 1 undefined on i
nput line 34.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
Overfull \hbox (21.80292pt too wide) in paragraph at lines 38--39
[]\OT1/ptm/m/n/10.95 We fur-ther show that sched-uled sampling---mixing model-g
enerated con-text dur-ing training---compresses

Package natbib Warning: Citation `dongre2026gar' on page 2 undefined on input l
ine 51.


Package natbib Warning: Citation `zheng2023judging' on page 2 undefined on inpu
t line 51.


Package natbib Warning: Citation `bai2024mtbench101' on page 2 undefined on inp
ut line 51.


Package natbib Warning: Citation `liu2024lost' on page 2 undefined on input lin
e 51.


Package natbib Warning: Citation `bachlechner2021rezero' on page 2 undefined on
 input line 54.


Package natbib Warning: Citation `wang2018skipnet' on page 2 undefined on input
 line 54.


Package natbib Warning: Citation `fan2020reducing' on page 2 undefined on input
 line 54.


Package natbib Warning: Citation `luo2025flexidepth' on page 2 undefined on inp
ut line 54.


Package natbib Warning: Citation `xiao2024efficient' on page 2 undefined on inp
ut line 57.


Package natbib Warning: Citation `qiu2025gated' on page 2 undefined on input li
ne 57.


Package natbib Warning: Citation `elhage2021mathematical' on page 2 undefined o
n input line 57.


Package natbib Warning: Citation `bengio2015scheduled' on page 2 undefined on i
nput line 60.


Package natbib Warning: Citation `lamb2016professor' on page 2 undefined on inp
ut line 60.


Package natbib Warning: Citation `leblond2018searnn' on page 2 undefined on inp
ut line 60.


Package natbib Warning: Citation `ranzato2016sequence' on page 2 undefined on i
nput line 60.


Package natbib Warning: Citation `wiseman2016sequence' on page 2 undefined on i
nput line 60.


Package natbib Warning: Citation `dou2022parallel' on page 2 undefined on input
 line 60.


Package natbib Warning: Citation `dongre2026gar' on page 2 undefined on input l
ine 67.


Overfull \hbox (9.31392pt too wide) in paragraph at lines 67--68
\OT1/ptm/m/n/10.95 Following \OT1/ptm/b/n/10.95 ?\OT1/ptm/m/n/10.95 , we mea-su
re how well a model's at-ten-tion mech-a-nism routes in-for-ma-tion from goal-s
pecifying
[2]

Package natbib Warning: Citation `dongre2026gar' on page 3 undefined on input l
ine 75.


Package natbib Warning: Citation `dongre2026gar' on page 3 undefined on input l
ine 79.


Package natbib Warning: Citation `bengio2015scheduled' on page 3 undefined on i
nput line 115.

[3]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 121.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\beta' on input line 121.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 121.


Package natbib Warning: Citation `ding2023enhancing' on page 4 undefined on inp
ut line 136.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/omsptm.fd)

LaTeX Warning: Reference `tab:main' on page 4 undefined on input line 144.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 170.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\beta' on input line 170.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 170.

[4]

LaTeX Warning: Reference `tab:ss_seeds' on page 5 undefined on input line 177.


LaTeX Warning: Reference `tab:cross_model_ss' on page 5 undefined on input line
 201.


Overfull \hbox (0.9328pt too wide) in paragraph at lines 224--225
[]\OT1/ptm/m/n/10.95 At $\OML/cmm/m/it/10.95 ^^L[]\OT1/cmr/m/n/10.95 5$\OT1/ptm
/m/n/10.95 , the cross-model gap nar-rows to 1.2$\OMS/cmsy/m/n/10.95 ^^B$ \OT1/
ptm/m/n/10.95 (Llama 0.62 vs. Qwen 0.72), sug-gest-ing that inference-
[5]

Package natbib Warning: Citation `yu2020gradient' on page 6 undefined on input 
line 236.


LaTeX Warning: Reference `tab:long_conv' on page 6 undefined on input line 242.



LaTeX Warning: Reference `tab:kl' on page 6 undefined on input line 264.

[6]

LaTeX Warning: Reference `tab:gar_defs' on page 7 undefined on input line 285.


LaTeX Warning: Reference `tab:gar_alt' on page 7 undefined on input line 308.


LaTeX Warning: Reference `tab:grad_cross' on page 7 undefined on input line 331
.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 356.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\lambda' on input line 356.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 356.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 356.


LaTeX Warning: Reference `tab:lambda' on page 7 undefined on input line 358.

[7] [8]
Overfull \hbox (2.88626pt too wide) in paragraph at lines 391--392
 []\OT1/ptm/b/n/10.95 Implications for At-ten-tion Steer-ing Meth-ods.[] \OT1/p
tm/m/n/10.95 Our find-ings sug-gest that any at-ten-tion steer-ing method

Underfull \hbox (badness 1496) in paragraph at lines 407--408
[]\OT1/ptm/m/n/10.95 Thomas Bach-lech-ner, Bod-hisattwa Prasad Ma-jumder, Huanr
u Henry Mao, Gary W. Gar-ri-son,
[9]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 467.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\lambda' on input line 467.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 467.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 467.


LaTeX Warning: Reference `tab:lambda' on page 10 undefined on input line 469.

[10]

Package natbib Warning: There were undefined citations.

[11] (./paper.aux

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
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 172733 bytes).
Transcript written on paper.log.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 467.

[10] [11] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 177455 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb66ba28-027a-49c6-822f-bc8c254440ab",
  "isSidechain": false,
  "promptId": "67a87842-f41b-4d9e-9fbd-faa3f9849a08",
  "type": "user",
  "uuid": "ec73b6ca-d5fb-4c52-bcfa-fdc9fa6f3cae",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `dongre2026gar' on page 1 undefined on input l\nine 30.\n\n\nPackage natbib Warning: Citation `zheng2023judging' on page 1 undefined on inpu\nt line 30.\n\n\nPackage natbib Warning: Citation `dongre2026gar' on page 1 undefined on input l\nine 30.\n\n\nPackage natbib Warning: Citation `bengio2015scheduled' on page 1 undefined on i\nnput line 34.\n\n\nPackage natbib Warning: Citation `ranzato2016sequence' on page 1 undefined on i\nnput line 34.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\nOverfull \\hbox (21.80292pt too wide) in paragraph at lines 38--39\n[]\\OT1/ptm/m/n/10.95 We fur-ther show that sched-uled sampling---mixing model-g\nenerated con-text dur-ing training---compresses\n\nPackage natbib Warning: Citation `dongre2026gar' on page 2 undefined on input l\nine 51.\n\n\nPackage natbib Warning: Citation `zheng2023judging' on page 2 undefined on inpu\nt line 51.\n\n\nPackage natbib Warning: Citation `bai2024mtbench101' on page 2 undefined on inp\nut line 51.\n\n\nPackage natbib Warning: Citation `liu2024lost' on page 2 undefined on input lin\ne 51.\n\n\nPackage natbib Warning: Citation `bachlechner2021rezero' on page 2 undefined on\n input line 54.\n\n\nPackage natbib Warning: Citation `wang2018skipnet' on page 2 undefined on input\n line 54.\n\n\nPackage natbib Warning: Citation `fan2020reducing' on page 2 undefined on input\n line 54.\n\n\nPackage natbib Warning: Citation `luo2025flexidepth' on page 2 undefined on inp\nut line 54.\n\n\nPackage natbib Warning: Citation `xiao2024efficient' on page 2 undefined on inp\nut line 57.\n\n\nPackage natbib Warning: Citation `qiu2025gated' on page 2 undefined on input li\nne 57.\n\n\nPackage natbib Warning: Citation `elhage2021mathematical' on page 2 undefined o\nn input line 57.\n\n\nPackage natbib Warning: Citation `bengio2015scheduled' on page 2 undefined on i\nnput line 60.\n\n\nPackage natbib Warning: Citation `lamb2016professor' on page 2 undefined on inp\nut line 60.\n\n\nPackage natbib Warning: Citation `leblond2018searnn' on page 2 undefined on inp\nut line 60.\n\n\nPackage natbib Warning: Citation `ranzato2016sequence' on page 2 undefined on i\nnput line 60.\n\n\nPackage natbib Warning: Citation `wiseman2016sequence' on page 2 undefined on i\nnput line 60.\n\n\nPackage natbib Warning: Citation `dou2022parallel' on page 2 undefined on input\n line 60.\n\n\nPackage natbib Warning: Citation `dongre2026gar' on page 2 undefined on input l\nine 67.\n\n\nOverfull \\hbox (9.31392pt too wide) in paragraph at lines 67--68\n\\OT1/ptm/m/n/10.95 Following \\OT1/ptm/b/n/10.95 ?\\OT1/ptm/m/n/10.95 , we mea-su\nre how well a model's at-ten-tion mech-a-nism routes in-for-ma-tion from goal-s\npecifying\n[2]\n\nPackage natbib Warning: Citation `dongre2026gar' on page 3 undefined on input l\nine 75.\n\n\nPackage natbib Warning: Citation `dongre2026gar' on page 3 undefined on input l\nine 79.\n\n\nPackage natbib Warning: Citation `bengio2015scheduled' on page 3 undefined on i\nnput line 115.\n\n[3]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 121.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\beta' on input line 121.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 121.\n\n\nPackage natbib Warning: Citation `ding2023enhancing' on page 4 undefined on inp\nut line 136.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/omsptm.fd)\n\nLaTeX Warning: Reference `tab:main' on page 4 undefined on input line 144.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 170.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\beta' on input line 170.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 170.\n\n[4]\n\nLaTeX Warning: Reference `tab:ss_seeds' on page 5 undefined on input line 177.\n\n\nLaTeX Warning: Reference `tab:cross_model_ss' on page 5 undefined on input line\n 201.\n\n\nOverfull \\hbox (0.9328pt too wide) in paragraph at lines 224--225\n[]\\OT1/ptm/m/n/10.95 At $\\OML/cmm/m/it/10.95 ^^L[]\\OT1/cmr/m/n/10.95 5$\\OT1/ptm\n/m/n/10.95 , the cross-model gap nar-rows to 1.2$\\OMS/cmsy/m/n/10.95 ^^B$ \\OT1/\nptm/m/n/10.95 (Llama 0.62 vs. Qwen 0.72), sug-gest-ing that inference-\n[5]\n\nPackage natbib Warning: Citation `yu2020gradient' on page 6 undefined on input \nline 236.\n\n\nLaTeX Warning: Reference `tab:long_conv' on page 6 undefined on input line 242.\n\n\n\nLaTeX Warning: Reference `tab:kl' on page 6 undefined on input line 264.\n\n[6]\n\nLaTeX Warning: Reference `tab:gar_defs' on page 7 undefined on input line 285.\n\n\nLaTeX Warning: Reference `tab:gar_alt' on page 7 undefined on input line 308.\n\n\nLaTeX Warning: Reference `tab:grad_cross' on page 7 undefined on input line 331\n.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 356.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\lambda' on input line 356.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 356.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 356.\n\n\nLaTeX Warning: Reference `tab:lambda' on page 7 undefined on input line 358.\n\n[7] [8]\nOverfull \\hbox (2.88626pt too wide) in paragraph at lines 391--392\n []\\OT1/ptm/b/n/10.95 Implications for At-ten-tion Steer-ing Meth-ods.[] \\OT1/p\ntm/m/n/10.95 Our find-ings sug-gest that any at-ten-tion steer-ing method\n\nUnderfull \\hbox (badness 1496) in paragraph at lines 407--408\n[]\\OT1/ptm/m/n/10.95 Thomas Bach-lech-ner, Bod-hisattwa Prasad Ma-jumder, Huanr\nu Henry Mao, Gary W. Gar-ri-son,\n[9]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 467.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\lambda' on input line 467.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 467.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 467.\n\n\nLaTeX Warning: Reference `tab:lambda' on page 10 undefined on input line 469.\n\n[10]\n\nPackage natbib Warning: There were undefined citations.\n\n[11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 172733 bytes).\nTranscript written on paper.log.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 467.\n\n[10] [11] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 177455 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fb66ba28-027a-49c6-822f-bc8c254440ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_g…",
  "leafUuid": "ec73b6ca-d5fb-4c52-bcfa-fdc9fa6f3cae",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on residual gating mechanisms",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b"
}
```

---

### Assistant

_source line 41 · 2026-05-24T08:57:49.356Z_

PDF compiled successfully (11 pages, 177KB). The paper covers all 8 experiments from `experiment_data.json`:

1. **Llama Gradient Conflict Analysis** → Table 7 (§6.6 Cross-Model Gradient Analysis)
2. **Expanded Eval N=200** → Table 1 (§5.2 Main Results)
3. **λ\_GAR Sensitivity** → Table 8 (§6.7) + Appendix A
4. **TF vs AR Attention KL Divergence** → Tables 4, 5 (§6.4 Mechanism Specificity)
5. **Llama SS Training + Eval** → Table 3 (§5.4) + Appendix C
6. **SS 3-Seed Validation** → Table 2 (§5.4)
7. **Alternative GAR Definition Robustness** → Table 6 (§6.5)
8. **SS 4th Seed** → Appendix B
9. **Long Conversation Eval** → Table 3 (§6.3)

All quantitative claims use numbers directly from `experiment_data.json`. Title uses T1 per narrative guidance. Contribution #5 is weakened to "initial evidence...requiring further investigation." Discussion includes SS transferability limitations paragraph analyzing Llama's weaker results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec73b6ca-d5fb-4c52-bcfa-fdc9fa6f3cae",
  "isSidechain": false,
  "requestId": "req_011CbM7j3tp4fj56gyMwgijC",
  "type": "assistant",
  "uuid": "6857bf18-6126-42e7-bb65-fcc27e3b2392",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127chPZMpVqjdq1Vk6rmQvi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5552,
      "cache_read_input_tokens": 66135,
      "output_tokens": 324,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5552,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 324,
          "cache_read_input_tokens": 66135,
          "cache_creation_input_tokens": 5552,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5552
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_g…",
  "leafUuid": "6857bf18-6126-42e7-bb65-fcc27e3b2392",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on residual gating mechanisms",
  "sessionId": "77b0607c-003d-4705-b21b-c267a108326b"
}
```

---
