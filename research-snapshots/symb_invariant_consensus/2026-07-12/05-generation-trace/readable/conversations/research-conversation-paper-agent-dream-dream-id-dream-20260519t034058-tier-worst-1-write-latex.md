# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T034058 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/08579623-f8e4-4cf1-a921-af800586a59b.jsonl`
- **Structured JSON:** [`e025bb2fecffadf3fa0b.json`](../../sessions/e0/e025bb2fecffadf3fa0b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T04:26:34.906Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T04:26:34.906Z",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T034058 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：放弃 Condorcet predictive framework 作为核心 claim。Reframe 为 \"Comprehensive Diagnostic Study of Symbolic Consensus Aggregation\"。 Eff-K 跨模型方向虽对但模型内无预测力，K/T curves 全是 noise，multi-temp 意外 positive 动摇 diversity 叙事。 三条腿支撑投 Findings：(1) Oracle gap hard result; (2) 9 种修复 breadth; (3) C0+SC diagnostic。 Title 改为 \"When Do Self-Extracted Symbolic Constraints Help LLM Reasoning? A Diagnostic Study\"。 估计 reviewer avg 2.5–3.0。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T04:26:34.910Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T04:26:34.910Z",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b"
}
```

---

## Round 1

40 recorded events

### User

_source line 3 · 2026-05-19T04:26:34.943Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T034058 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：放弃 Condorcet predictive framework 作为核心 claim。Reframe 为 "Comprehensive Diagnostic Study of Symbolic Consensus Aggregation"。 Eff-K 跨模型方向虽对但模型内无预测力，K/T curves 全是 noise，multi-temp 意外 positive 动摇 diversity 叙事。 三条腿支撑投 Findings：(1) Oracle gap hard result; (2) 9 种修复 breadth; (3) C0+SC diagnostic。 Title 改为 "When Do Self-Extracted Symbolic Constraints Help LLM Reasoning? A Diagnostic Study"。 估计 reviewer avg 2.5–3.0。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6cd4ba32-185c-4e26-8eaf-fcddb4213dff",
  "type": "user",
  "uuid": "da73e3ff-00f7-49ba-b2f3-d2997bef934c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T04:26:34.939Z_

```json
{
  "parentUuid": "da73e3ff-00f7-49ba-b2f3-d2997bef934c",
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
  "uuid": "2a2d6cb2-e7a1-465f-8910-3b30ab8e5946",
  "timestamp": "2026-05-19T04:26:34.939Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T04:26:34.939Z_

```json
{
  "parentUuid": "2a2d6cb2-e7a1-465f-8910-3b30ab8e5946",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c805d5b2-cffe-471c-88c0-002ea1e91461",
  "timestamp": "2026-05-19T04:26:34.939Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier symbolic consensus paper",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b"
}
```

---

### Assistant

_source line 7 · 2026-05-19T04:26:37.978Z_

I'll start by reading the input files to understand the experimental data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c805d5b2-cffe-471c-88c0-002ea1e91461",
  "isSidechain": false,
  "requestId": "req_011CbBJ1arUXivVhrKCEyd7z",
  "type": "assistant",
  "uuid": "d2a28301-8eda-431a-a5c7-92b666b7545f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SobJKrRvC7qKKCfU2WZ6gB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12782,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12782,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12782
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

_source line 8 · 2026-05-19T04:26:38.958Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MPDUXKdYC5jEyPkFTkRMpJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2a28301-8eda-431a-a5c7-92b666b7545f",
  "isSidechain": false,
  "requestId": "req_011CbBJ1arUXivVhrKCEyd7z",
  "type": "assistant",
  "uuid": "f6f08611-f643-4f9c-ae83-5ceb3bd28b93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SobJKrRvC7qKKCfU2WZ6gB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12782,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12782,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12782
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

_source line 9 · 2026-05-19T04:26:39.160Z_

<details open><summary>🔧 Tool call — Read · `toolu_018n48XN9QadVZA3wCrBFLhr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6f08611-f643-4f9c-ae83-5ceb3bd28b93",
  "isSidechain": false,
  "requestId": "req_011CbBJ1arUXivVhrKCEyd7z",
  "type": "assistant",
  "uuid": "7116e666-3395-4edb-9f73-e06bf315e9c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SobJKrRvC7qKKCfU2WZ6gB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12782,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12782,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12782
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

_source line 10 · 2026-05-19T04:26:39.166Z_

<details><summary>↩ Tool result · `toolu_018n48XN9QadVZA3wCrBFLhr`</summary>

```text
1	# Paper Framing — symb_invariant_consensus
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25)
5	- Deadline: May 25, 2026 (ARR submission)
6	
7	## D060 Direction: Pure Analysis Paper — Independence Bottleneck
8	
9	**D059 method improvement 三路失败后，回归纯 analysis paper。** 但比 D058 的 analysis 更强：
10	- **Condorcet independence 框架** 提供理论解释（非纯经验）
11	- **9 种修复全部失败**（比原 6 种多 3 种靶向尝试）→ bottleneck 是 fundamental
12	- **exp-052 p=0.039** → 2/3 seeds 显著 → 效应 IS real but fragile
13	- **K sensitivity 倒 U 型** → clean ablation 贡献
14	- **T sensitivity** → +4.90pp 仅在 T=0.7 存在，T=1.0 降到 +0.55pp → 效应极度脆弱
15	- 用户指示: 投 May 25 不变，≥3.0 兜底
16	
17	## Core Claims (5 条) — D060 纯 Analysis Framing
18	
19	### Analysis Claims (已验证)
20	
21	1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：
22	   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)
23	   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)
24	   - Mistral-7B FOLIO s42 (exp-033): κ=0.500, Eff-K=1.85 (Δ=+4.90pp p=0.013) ← primary seed
25	   - Mistral-7B FOLIO s123: κ=0.412, Eff-K=2.17 (Δ=+3.43pp p=0.039)
26	   - Mistral-7B FOLIO s456: κ=0.401, Eff-K=2.22 (Δ=-0.49pp n.s.)
27	   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)
28	   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +4.90pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。
29	
30	2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +4.9pp (best case) = 35% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:
31	   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）
32	   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）
33	   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的"区分方向"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。
34	
35	3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：
36	   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案
37	   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)
38	   - Goldilocks zone (~50-55% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+4.90pp, p=0.013)
39	   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)
40	
41	4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。
42	
43	### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)
44	
45	5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：
46	   - D059 三路 method improvement 全部失败：
47	     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op
48	     - T=1.0 (exp-054): delta 从 +4.90pp 崩塌到 +0.55pp，温度敏感性极端
49	     - Multi-Temp (exp-055): 早期 n=28 delta=0.00pp（待完成，但预期 negative）
50	   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT
51	   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental
52	
53	## Core Insight (D060 Updated — Dual Bottleneck)
54	
55	**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：
56	1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角
57	2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声
58	
59	Condorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。
60	
61	实验数据完美支持 dual requirement：
62	- **Qwen-14B**: Eff-K≈1.2-1.3（独立性不足）→ 0 gain，无论 SC 多高
63	- **Mistral-7B FOLIO**: Eff-K≈1.85-2.22（中等独立性）+ SC≈54%（中等质量）→ +4.90pp (2/3 seeds significant)
64	- **Mistral-7B PW-600**: Eff-K=3.63（最高独立性）但 SC=39%（质量不足）→ -2.83pp
65	- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta
66	
67	Oracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 35% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。
68	
69	**κ-delta 反相关解释**：exp-033 κ=0.500 比 exp-052/053 κ≈0.41 高，但 delta 最大。原因：exp-033 Unknown 比例低（49.9% vs 58.5%），traces 更 decisive（更多 True/False 判断）→ 同时导致更高 κ（更多 agreement）和更好的 constraint quality。κ 不是 SICA 效果的唯一决定因素。
70	
71	**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。
72	
73	**Key evidence**:
74	- **Condorcet independence quantification (Worker-verified, 公式: Eff-K=K/(1+(K-1)κ))**: exp-033 Mistral-7B s42 κ=0.500 (Eff-K=1.85), Mistral-7B s123 κ=0.412 (Eff-K=2.17), Mistral-7B s456 κ=0.401 (Eff-K=2.22), Mistral-7B PW-600 κ=0.210 (Eff-K=3.63), Qwen-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen-14B LogiQA κ=0.821 (Eff-K=1.20). 跨模型清晰: Qwen Eff-K≈1.2-1.3→0 gain, Mistral Eff-K≈1.85-3.63→variable. Eff-K necessary but not sufficient: exp-046 highest Eff-K(3.63) but negative delta(SC too low); within Mistral seeds Eff-K非单调 with delta.
75	- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.
76	- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.
77	- **K sensitivity (inverted U)**: K=4(-1.47pp), K=8(-0.98pp), K=12(+4.90pp p=0.013), K=16(+1.47pp), K=20(pending). Peak at K=12, then decline. Non-monotonic. K=4 SC ≈ K=12 SC but SICA differs by 6.4pp — proves SICA extracts different information than SC.
78	- **T sensitivity (extreme fragility)**: T=0.7(+4.90pp p=0.013), T=1.0(+0.49pp p=0.739). 温度从 0.7 提到 1.0 让增益降 90%。T=0.3 (exp-057, pending). SICA 效应极度依赖超参数。
79	- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=+0.25pp vs Mistral-7B (SC=54.41%) Δ=+4.90pp p=0.013
80	- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.
81	- **Seed replication**: 2/3 seeds significant at α=0.05 (exp-033 p=0.013, exp-052 p=0.039), 1/3 null (exp-053). Effect IS real but fragile — motivates deep analysis of WHY.
82	- **Nine remediation failures**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse), multi-temp (pending, early 0.00pp). All failed → trap is fundamental.
83	- **Entropy mechanism**: High-entropy problems proportion: Mistral 35.8% vs Qwen 10.3%. Unanimous rate: 18.6% vs 58.8%.
84	- **Confirmation bias quantification**: Override precision 70.6% (Mistral) vs 28.6% (Qwen). Constraint agreement >80%: 31.9% vs 62.3%.
85	
86	## Story Spine (D059 Updated)
87	
88	- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?
89	- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.
90	- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.
91	- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.
92	- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.
93	- **Headline result**: "Across 5 model families, symbolic consensus aggregation shows a real but fragile effect: significant improvement in 2/3 seeds under specific conditions (Mistral-7B, FOLIO, T=0.7, K=12), but zero or negative gains under any perturbation. Condorcet analysis reveals the root cause: Effective-K = 1.3-1.8 for nominal K=12 due to trace non-independence. Oracle constraints prove the aggregation mechanism works (+14.22pp), but 9 remediation strategies all fail to overcome the self-extraction bottleneck. C0+SC provides a zero-cost deployment diagnostic."
94	
95	## Anticipated Reviewer Concerns & Defensive Experiments
96	
97	1. **"Gains not statistically significant"** → exp-033 p=0.013 (n=204), exp-031 oracle p=2.0e-7. Combined N>1,200.
98	2. **"Only one positive result (exp-033)"** → Seed replication: 2/3 significant (p=0.013, p=0.039). Effect IS real but fragile — the fragility itself IS the finding (K/T sensitivity, Condorcet independence).
99	3. **"Condorcet framework is trivial"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.
100	4. **"Multi-temp / filtering should work"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.
101	5. **"Only Qwen models"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.
102	6. **"Only logic domain"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.
103	7. **"Oracle is unfair comparison"** → Diagnostic tool, not competing method. Separates extraction from aggregation.
104	8. **"MAX-SAT is over-engineering"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.
105	9. **"Self-extraction confound"** → Oracle control resolves completely.
106	10. **"Published methods achieve gains (DyLoS, Aristotle, FoVer)"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.
107	11. **"C0 is trivially derived"** → Zero-cost early stopping. Practical value.
108	12. **"Why not just use a reasoning model?"** → QwQ-32B: C0<5%, SICA≡SC.
109	13. **"Random tiebreak baseline"** → exp-003: SICA tiebreak 80% vs random 50%.
110	14. **"Method improvement is incremental"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.
111	15. **"Weighted SC is simpler"** → exp-016 planned. Weighted SC doesn't address independence.
112	16. **"Within-model ICL transition contradicts regime theory"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish "same model, different prompt" from "same model, same prompt, different accuracy."
113	
114	## Working Title
115	**"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning"**
116	(Alternatives:
117	- "The Independence Bottleneck: Why Self-Extracted Symbolic Constraints Cannot Beat Majority Voting"
118	- "Symbolic Consensus Under the Condorcet Lens: Independence, Extraction, and the Limits of Self-Aggregation")
119	
120	NOTE (Dream D037): Title MUST be scoped to "self-extracted constraints" / "SICA". Published methods (DyLoS, Aristotle, FoVer) use different approaches.
121	
122	## Paper Structure (EMNLP 8pp + appendix)
123	
124	### Main Tables
125	- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary
126	- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation
127	- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model
128	- T4: Extraction Error Taxonomy — trivially_satisfied / discriminative / both_wrong rates
129	- T5: K Sensitivity — K=4/8/12/16/20 with Eff-K and diversity metrics (inverted U curve)
130	
131	### Main Figures
132	- F1: Method Pipeline (SICA + oracle control design)
133	- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)
134	- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)
135	- F4: Extraction error breakdown (stacked bar)
136	
137	### Appendix
138	- K ablation details, temperature sensitivity, per-domain results, overhead analysis
139	- Entropy-conditioned analysis (continuous scatter + bin sensitivity)
140	- Six remediation strategy details
141	- Confirmation bias quantification
142	- Seed replication analysis
143	- QwQ-32B / DeepSeek-R1 negative control
144	
145	## Claim Risk Notes (D059)
146	- **Seed replication**: 2/3 significant (p=0.013, p=0.039), 1/3 null. Frame as "real but fragile effect" — motivates analysis of WHY.
147	- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.
148	- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.
149	- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple "SC determines SICA." Explain via trace generation characteristic change.
150	- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.
151	
152	## Required Citations (minimum 30 references)
153	
154	- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)
155	- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)
156	- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation
157	- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training
158	- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd
159	- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)
160	- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023
161	
162	## Claim Scoping Rules
163	- n=60 conditions: "suggestive/consistent with" NOT "confirming"
164	- n≥200 conditions: can "confirm"
165	- Combined N>1,300: acceptable if breakdown clearly stated
166	- Method claims: must show statistically significant improvement OR clear directional improvement with analysis
167	- "Independence bottleneck" framing: systematic quantification + theoretical grounding
168	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7116e666-3395-4edb-9f73-e06bf315e9c7",
  "isSidechain": false,
  "promptId": "6cd4ba32-185c-4e26-8eaf-fcddb4213dff",
  "type": "user",
  "uuid": "208c389d-9796-4781-8af1-b5582987f923",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/paper_framing.md",
      "content": "# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Deadline: May 25, 2026 (ARR submission)\n\n## D060 Direction: Pure Analysis Paper — Independence Bottleneck\n\n**D059 method improvement 三路失败后，回归纯 analysis paper。** 但比 D058 的 analysis 更强：\n- **Condorcet independence 框架** 提供理论解释（非纯经验）\n- **9 种修复全部失败**（比原 6 种多 3 种靶向尝试）→ bottleneck 是 fundamental\n- **exp-052 p=0.039** → 2/3 seeds 显著 → 效应 IS real but fragile\n- **K sensitivity 倒 U 型** → clean ablation 贡献\n- **T sensitivity** → +4.90pp 仅在 T=0.7 存在，T=1.0 降到 +0.55pp → 效应极度脆弱\n- 用户指示: 投 May 25 不变，≥3.0 兜底\n\n## Core Claims (5 条) — D060 纯 Analysis Framing\n\n### Analysis Claims (已验证)\n\n1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：\n   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)\n   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)\n   - Mistral-7B FOLIO s42 (exp-033): κ=0.500, Eff-K=1.85 (Δ=+4.90pp p=0.013) ← primary seed\n   - Mistral-7B FOLIO s123: κ=0.412, Eff-K=2.17 (Δ=+3.43pp p=0.039)\n   - Mistral-7B FOLIO s456: κ=0.401, Eff-K=2.22 (Δ=-0.49pp n.s.)\n   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)\n   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +4.90pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。\n\n2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +4.9pp (best case) = 35% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:\n   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）\n   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）\n   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的\"区分方向\"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。\n\n3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：\n   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案\n   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)\n   - Goldilocks zone (~50-55% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+4.90pp, p=0.013)\n   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)\n\n4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。\n\n### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)\n\n5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：\n   - D059 三路 method improvement 全部失败：\n     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op\n     - T=1.0 (exp-054): delta 从 +4.90pp 崩塌到 +0.55pp，温度敏感性极端\n     - Multi-Temp (exp-055): 早期 n=28 delta=0.00pp（待完成，但预期 negative）\n   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT\n   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental\n\n## Core Insight (D060 Updated — Dual Bottleneck)\n\n**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：\n1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角\n2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声\n\nCondorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。\n\n实验数据完美支持 dual requirement：\n- **Qwen-14B**: Eff-K≈1.2-1.3（独立性不足）→ 0 gain，无论 SC 多高\n- **Mistral-7B FOLIO**: Eff-K≈1.85-2.22（中等独立性）+ SC≈54%（中等质量）→ +4.90pp (2/3 seeds significant)\n- **Mistral-7B PW-600**: Eff-K=3.63（最高独立性）但 SC=39%（质量不足）→ -2.83pp\n- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta\n\nOracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 35% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。\n\n**κ-delta 反相关解释**：exp-033 κ=0.500 比 exp-052/053 κ≈0.41 高，但 delta 最大。原因：exp-033 Unknown 比例低（49.9% vs 58.5%），traces 更 decisive（更多 True/False 判断）→ 同时导致更高 κ（更多 agreement）和更好的 constraint quality。κ 不是 SICA 效果的唯一决定因素。\n\n**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。\n\n**Key evidence**:\n- **Condorcet independence quantification (Worker-verified, 公式: Eff-K=K/(1+(K-1)κ))**: exp-033 Mistral-7B s42 κ=0.500 (Eff-K=1.85), Mistral-7B s123 κ=0.412 (Eff-K=2.17), Mistral-7B s456 κ=0.401 (Eff-K=2.22), Mistral-7B PW-600 κ=0.210 (Eff-K=3.63), Qwen-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen-14B LogiQA κ=0.821 (Eff-K=1.20). 跨模型清晰: Qwen Eff-K≈1.2-1.3→0 gain, Mistral Eff-K≈1.85-3.63→variable. Eff-K necessary but not sufficient: exp-046 highest Eff-K(3.63) but negative delta(SC too low); within Mistral seeds Eff-K非单调 with delta.\n- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.\n- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.\n- **K sensitivity (inverted U)**: K=4(-1.47pp), K=8(-0.98pp), K=12(+4.90pp p=0.013), K=16(+1.47pp), K=20(pending). Peak at K=12, then decline. Non-monotonic. K=4 SC ≈ K=12 SC but SICA differs by 6.4pp — proves SICA extracts different information than SC.\n- **T sensitivity (extreme fragility)**: T=0.7(+4.90pp p=0.013), T=1.0(+0.49pp p=0.739). 温度从 0.7 提到 1.0 让增益降 90%。T=0.3 (exp-057, pending). SICA 效应极度依赖超参数。\n- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=+0.25pp vs Mistral-7B (SC=54.41%) Δ=+4.90pp p=0.013\n- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.\n- **Seed replication**: 2/3 seeds significant at α=0.05 (exp-033 p=0.013, exp-052 p=0.039), 1/3 null (exp-053). Effect IS real but fragile — motivates deep analysis of WHY.\n- **Nine remediation failures**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse), multi-temp (pending, early 0.00pp). All failed → trap is fundamental.\n- **Entropy mechanism**: High-entropy problems proportion: Mistral 35.8% vs Qwen 10.3%. Unanimous rate: 18.6% vs 58.8%.\n- **Confirmation bias quantification**: Override precision 70.6% (Mistral) vs 28.6% (Qwen). Constraint agreement >80%: 31.9% vs 62.3%.\n\n## Story Spine (D059 Updated)\n\n- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?\n- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.\n- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.\n- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.\n- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.\n- **Headline result**: \"Across 5 model families, symbolic consensus aggregation shows a real but fragile effect: significant improvement in 2/3 seeds under specific conditions (Mistral-7B, FOLIO, T=0.7, K=12), but zero or negative gains under any perturbation. Condorcet analysis reveals the root cause: Effective-K = 1.3-1.8 for nominal K=12 due to trace non-independence. Oracle constraints prove the aggregation mechanism works (+14.22pp), but 9 remediation strategies all fail to overcome the self-extraction bottleneck. C0+SC provides a zero-cost deployment diagnostic.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n\n1. **\"Gains not statistically significant\"** → exp-033 p=0.013 (n=204), exp-031 oracle p=2.0e-7. Combined N>1,200.\n2. **\"Only one positive result (exp-033)\"** → Seed replication: 2/3 significant (p=0.013, p=0.039). Effect IS real but fragile — the fragility itself IS the finding (K/T sensitivity, Condorcet independence).\n3. **\"Condorcet framework is trivial\"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.\n4. **\"Multi-temp / filtering should work\"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.\n5. **\"Only Qwen models\"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.\n6. **\"Only logic domain\"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.\n7. **\"Oracle is unfair comparison\"** → Diagnostic tool, not competing method. Separates extraction from aggregation.\n8. **\"MAX-SAT is over-engineering\"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.\n9. **\"Self-extraction confound\"** → Oracle control resolves completely.\n10. **\"Published methods achieve gains (DyLoS, Aristotle, FoVer)\"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.\n11. **\"C0 is trivially derived\"** → Zero-cost early stopping. Practical value.\n12. **\"Why not just use a reasoning model?\"** → QwQ-32B: C0<5%, SICA≡SC.\n13. **\"Random tiebreak baseline\"** → exp-003: SICA tiebreak 80% vs random 50%.\n14. **\"Method improvement is incremental\"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.\n15. **\"Weighted SC is simpler\"** → exp-016 planned. Weighted SC doesn't address independence.\n16. **\"Within-model ICL transition contradicts regime theory\"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish \"same model, different prompt\" from \"same model, same prompt, different accuracy.\"\n\n## Working Title\n**\"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning\"**\n(Alternatives:\n- \"The Independence Bottleneck: Why Self-Extracted Symbolic Constraints Cannot Beat Majority Voting\"\n- \"Symbolic Consensus Under the Condorcet Lens: Independence, Extraction, and the Limits of Self-Aggregation\")\n\nNOTE (Dream D037): Title MUST be scoped to \"self-extracted constraints\" / \"SICA\". Published methods (DyLoS, Aristotle, FoVer) use different approaches.\n\n## Paper Structure (EMNLP 8pp + appendix)\n\n### Main Tables\n- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary\n- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation\n- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model\n- T4: Extraction Error Taxonomy — trivially_satisfied / discriminative / both_wrong rates\n- T5: K Sensitivity — K=4/8/12/16/20 with Eff-K and diversity metrics (inverted U curve)\n\n### Main Figures\n- F1: Method Pipeline (SICA + oracle control design)\n- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)\n- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)\n- F4: Extraction error breakdown (stacked bar)\n\n### Appendix\n- K ablation details, temperature sensitivity, per-domain results, overhead analysis\n- Entropy-conditioned analysis (continuous scatter + bin sensitivity)\n- Six remediation strategy details\n- Confirmation bias quantification\n- Seed replication analysis\n- QwQ-32B / DeepSeek-R1 negative control\n\n## Claim Risk Notes (D059)\n- **Seed replication**: 2/3 significant (p=0.013, p=0.039), 1/3 null. Frame as \"real but fragile effect\" — motivates analysis of WHY.\n- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.\n- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.\n- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple \"SC determines SICA.\" Explain via trace generation characteristic change.\n- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.\n\n## Required Citations (minimum 30 references)\n\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)\n- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\n- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation\n- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd\n- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\n\n## Claim Scoping Rules\n- n=60 conditions: \"suggestive/consistent with\" NOT \"confirming\"\n- n≥200 conditions: can \"confirm\"\n- Combined N>1,300: acceptable if breakdown clearly stated\n- Method claims: must show statistically significant improvement OR clear directional improvement with analysis\n- \"Independence bottleneck\" framing: systematic quantification + theoretical grounding\n",
      "numLines": 168,
      "startLine": 1,
      "totalLines": 168
    }
  },
  "sourceToolAssistantUUID": "7116e666-3395-4edb-9f73-e06bf315e9c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T04:26:39.293Z_

<details><summary>↩ Tool result · `toolu_01MPDUXKdYC5jEyPkFTkRMpJ`</summary>

```text
1	[
2	  {
3	    "name": "sica_k_ablation_14b",
4	    "description": "K=6/8/11/12/16/20 sensitivity on D012 60q, Qwen2.5-14B",
5	    "results": {
6	      "K6_delta_pp": 0.0,
7	      "K8_delta_pp": -1.7,
8	      "K11_delta_pp": 0.0,
9	      "K12_delta_pp": -5.0,
10	      "K16_delta_pp": -3.3,
11	      "K20_delta_pp": -3.3,
12	      "inverted_u_visual": "无——SICA 在所有 K 均 ≤ SC，随 K 增大单调恶化",
13	      "K11_odd_k_gap": 0.0
14	    },
15	    "tables": [
16	      "T5 (partial): K sensitivity — 仅 14B 列"
17	    ],
18	    "figures": [],
19	    "analysis": "14B K ablation 在 worst tier 下完全符合 Type A 预期——SC 太高时 SICA 无论 K 取何值都无法超越。 这本身不是 worst tier 的关键问题（实际已完成数据也如此），关键是 Mistral K ablation (exp-051) 也无 clean pattern 时，整个 K sensitivity 叙事崩塌。\n\n\nQwen-14B SC≈75% (Type A regime)，confirmation bias 主导。K 增大只增加冗余 correlated constraints， 不增加独立信息。Eff-K≈1.3 意味着 K=6 和 K=20 的 effective voters 几乎相同（~1.3）。 无 inverted-U 因为 14B 在此 regime 下 SICA 本身就没有正向效应，K 的变化只引入更多 noise。 K=11 odd-K 消除 tiebreak 后 gap=0 进一步确认 14B 效应完全是 tiebreak artifact。\n"
20	  },
21	  {
22	    "name": "tiebreak_baseline_analysis",
23	    "description": "SICA vs SC-random-tiebreak vs SC-deterministic, CPU-only",
24	    "results": {
25	      "sica_tiebreak_accuracy_pct": 80.0,
26	      "random_tiebreak_accuracy_pct": 50.0,
27	      "alphabetical_tiebreak_accuracy_pct": 60.0,
28	      "first_seen_tiebreak_accuracy_pct": 40.0,
29	      "n_tiebreak_problems": 5
30	    },
31	    "tables": [],
32	    "figures": [],
33	    "analysis": "Tiebreak 80% 看似有意义但 n=5 完全无 statistical significance。 Worst tier 下 reviewer 直接忽略此 result (\"interesting but underpowered\")。\n\n\nTiebreak 分析在 worst tier 下结果不变（已完成的 CPU 分析）。问题在于 n=5 tiebreak cases 太少， reviewer 会质疑 80% (4/5) 的 statistical power。且 SICA 的 tiebreak 优势仅在极少数问题上体现， 不构成 compelling evidence。在 worst tier 下 reviewer 将此视为 anecdotal。\n"
34	  },
35	  {
36	    "name": "sica_7b_scaling",
37	    "description": "Qwen2.5-7B on D012 60q, test C0-as-predictor",
38	    "results": {
39	      "sica_accuracy": 0.683,
40	      "sc_accuracy": 0.683,
41	      "delta_pp": 0.0,
42	      "multi_candidate_rate": 0.433,
43	      "mcnemar_p": 1.0,
44	      "discordant_sica_wins": 2,
45	      "discordant_sc_wins": 2
46	    },
47	    "tables": [
48	      "T1: Qwen-7B 行"
49	    ],
50	    "figures": [],
51	    "analysis": "Qwen-7B 支持跨模型 Eff-K 叙事（Qwen 家族 Eff-K 低→0 gain）但在 worst tier 下 reviewer 认为这只是\"同家族 same behavior\"，不算独立 evidence。\n\n\n7B SC≈68% 仍在 Type A regime 上沿（C0=43% 比 14B 高但仍不够）。 Qwen 家族内 Eff-K 普遍 ≈1.2-1.3，7B 的 lower capability 提高 C0 但不提高 constraint quality。 Constraints 仍然 mirror 模型偏差。Delta=0 确认 Qwen 家族 SICA 无效。 Worst case: 与 14B 结果一致，无法单独贡献 regime boundary 叙事。\n"
52	  },
53	  {
54	    "name": "qwq_32b_operating_regime",
55	    "description": "QwQ-32B negative control, data from MVP phase",
56	    "results": {
57	      "aggregate_c0_effective_pct": 2.6,
58	      "aime_delta_pp": 0.0,
59	      "proofwriter_delta_pp": -5.9,
60	      "total_problems": 46,
61	      "c0_below_threshold": true
62	    },
63	    "tables": [
64	      "T1: QwQ-32B 行",
65	      "Appendix: QwQ negative control detail"
66	    ],
67	    "figures": [],
68	    "analysis": "QwQ-32B C0<5% 是最 clean 的 negative result，但 worst tier 下 reviewer 视为 obvious—— \"当然 reasoning model 不需要 SICA\"。价值被低估。\n\n\nReasoning model 的 deterministic chain 产生近乎相同 traces (C0 effective≈2.6%)。 SICA≡SC 是必然——无 multi-candidate problems，MAX-SAT 无从发挥。 PW delta=-5.9pp 因 n=17 不 significant 但方向 negative。 Worst case: reviewer 认为 QwQ 是 trivially expected negative control，不算 contribution。\n"
69	  },
70	  {
71	    "name": "c0_diagnostic_validation",
72	    "description": "C0 vs SICA-SC gap scatter across all models/K values",
73	    "results": {
74	      "conditions_plotted": 12,
75	      "c0_delta_correlation_r": 0.31,
76	      "c0_delta_correlation_p": 0.33,
77	      "correctly_predicted_direction": 5,
78	      "total_conditions": 12,
79	      "prediction_accuracy_pct": 41.7
80	    },
81	    "tables": [],
82	    "figures": [],
83	    "analysis": "C0 diagnostic 在 worst tier 下失去 predictive power。只能做 necessary condition (C0<5% → SICA≡SC) 但 sufficient condition 不成立。Reviewer 会说 \"C0 just tells you there's variance, not that SICA helps\"。 降级为 \"deployment screening tool\" (排除 SICA 必然无用的 cases) 而非 \"predictor\"。\n\n\nWorst tier 核心假设: Eff-K+SC joint prediction ≤6/12 conditions 方向正确。 C0 单独作为 predictor 更差——Mistral PW-600 (C0 high, delta negative) 和  LLaMA-8B FOLIO (C0 high, delta negative) 都是反例。 Scatter plot 呈现 no clean trend，high C0 对应 both positive 和 negative deltas。 Correlation r≈0.31 不 significant (p>0.3, n=12)。\n"
84	  },
85	  {
86	    "name": "sica_72b_awq",
87	    "description": "Qwen2.5-72B-AWQ 4-bit on D012 60q",
88	    "results": {
89	      "sica_accuracy": 0.817,
90	      "sc_accuracy": 0.833,
91	      "delta_pp": -1.67,
92	      "multi_candidate_rate": 0.2,
93	      "mcnemar_p": 0.625,
94	      "extraction_rate": 0.95
95	    },
96	    "tables": [
97	      "T1: Qwen-72B 行"
98	    ],
99	    "figures": [],
100	    "analysis": "72B 进一步确认 Type A regime。但 worst tier 下 reviewer 说 \"you're just showing that SICA doesn't help strong models — this is obvious\"。缺乏新 insight。\n\n\n72B SC≈83% (deep Type A regime)。C0 进一步降至 ~20% 因为更大模型更 unanimous。 SICA 因 confirmation bias 甚至略 negative——constraints 强化已有高置信度答案， 少数 override 方向是错的。Qwen 家族 pattern 延续: 更大模型→更高 SC→更低 C0→更无用 SICA。\n"
101	  },
102	  {
103	    "name": "constraint_quality_case_studies",
104	    "description": "5-10 representative questions 的 constraint 质量定性分析",
105	    "results": {
106	      "cases_analyzed": 8,
107	      "trivially_satisfied_pct": 45,
108	      "confirmation_bias_cases": 6,
109	      "genuinely_informative_constraints": 1,
110	      "constraint_mirrors_model_answer_pct": 78
111	    },
112	    "tables": [],
113	    "figures": [],
114	    "analysis": "Case studies 支持 confirmation bias 叙事但在 worst tier 下 reviewer 认为 n=8 qualitative analysis 不算 rigorous evidence。\"Show me this at scale\" → 需要 exp-019 的 correlation， 但 exp-019 也 noisy。\n\n\n定性分析在 worst tier 下揭示 constraints 几乎完全 mirror 模型的 chain-of-thought 结论。 Even \"discriminative\" constraints 的 discriminative direction 与模型偏差一致。 唯一 genuinely informative case 是模型恰好 extract 了 premise 中的 explicit logical structure。 但 reviewer 可能认为 case studies 是 cherry-picked。\n"
115	  },
116	  {
117	    "name": "overhead_analysis",
118	    "description": "Wall-time breakdown per question",
119	    "results": {
120	      "mean_total_wall_s": 61.6,
121	      "trace_gen_pct": 51.3,
122	      "extraction_pct": 47.0,
123	      "maxsat_pct": 0.005,
124	      "sica_overhead_pct": 48.7
125	    },
126	    "tables": [
127	      "Appendix: overhead breakdown table"
128	    ],
129	    "figures": [],
130	    "analysis": "Overhead analysis 在 worst tier 下变成 anti-argument: \"你花了 2× compute 得到了 noise\"。 但可以 reframe 为 \"extraction is the bottleneck, not solving\" (MAX-SAT <0.01% time)， 说明未来研究应聚焦 extraction quality 而非 solver improvements。\n\n\nSICA 几乎 doubles wall time (49% overhead) 但 delta≈0 across most conditions。 Worst tier 下 cost-benefit 极差: 2× compute for 0 gain in majority of conditions, fragile +4.9pp in one specific setting (Mistral/FOLIO/T=0.7/K=12/s42)。 Reviewer: \"this is not practical\"。\n"
131	  },
132	  {
133	    "name": "sica_llama_8b",
134	    "description": "LLaMA-3.1-8B on D012 60q",
135	    "results": {
136	      "sica_accuracy": 0.667,
137	      "sc_accuracy": 0.6,
138	      "delta_pp": 6.67,
139	      "multi_candidate_rate": 0.617,
140	      "mcnemar_p": 0.219,
141	      "truncated_traces": 44,
142	      "answer_extraction_rate": 0.896
143	    },
144	    "tables": [
145	      "T1: LLaMA-8B 行"
146	    ],
147	    "figures": [],
148	    "analysis": "LLaMA-8B 是 worst tier 的典型 case: small-n positive 被 larger-n 反转。 Reviewer 会直接引用 FOLIO-204 result dismiss D012 result。 Combined evidence: SICA on LLaMA 是 noise。\n\n\nLLaMA-8B delta=+6.67pp 看似 positive 但 p=0.219 (n=60) 完全 n.s.。 且 truncated_traces=44 和 answer_extraction_rate=89.6% 说明 pipeline 对 LLaMA 有 artifacts。 Worst tier 下 reviewer 质疑: (1) n.s. result; (2) 44 truncated traces 是否 confound; (3) answer extraction 失败的 traces 是否 systematically biased。 扩展到 FOLIO-204 (exp-020) 后 delta 反转为 -2.45pp → D012 的 +6.67pp 是 small-n artifact。\n"
149	  },
150	  {
151	    "name": "gsm8k_pilot_14b",
152	    "description": "Qwen2.5-14B on GSM8K 30q pilot",
153	    "results": {
154	      "sica_accuracy": 0.967,
155	      "sc_accuracy": 0.967,
156	      "delta_pp": 0.0,
157	      "multi_candidate_rate": 0.133,
158	      "extraction_success_rate": 0.147
159	    },
160	    "tables": [
161	      "T1: GSM8K 行 (footnote: extraction failure)"
162	    ],
163	    "figures": [],
164	    "analysis": "GSM8K 在 worst tier 下是 domain 不匹配的 obvious failure。Reviewer 不会 penalize 但也不加分。 Reframe 为 Type B (domain not formalizable as FOL) 的 additional evidence。\n\n\n14B 在 GSM8K 准确率极高 (97%)，C0=13.3% 低于 threshold。 更关键的是 FOL extraction 几乎完全失败 (success=14.7%) — math domain 的 constraints 需要 numerical reasoning 而非 propositional logic，SICA pipeline 在此 domain 根本不适用。 这不是 SICA 的 negative evidence 而是 domain mismatch。\n"
165	  },
166	  {
167	    "name": "constraint_ablation",
168	    "description": "MaxSAT vs count-only vs random-weight, CPU-only on exp-001 data",
169	    "results": {
170	      "maxsat_accuracy": 0.765,
171	      "count_only_accuracy": 0.766,
172	      "random_weight_accuracy": 0.759,
173	      "sc_baseline_accuracy": 0.762,
174	      "agreement_maxsat_vs_countonly": "803/804",
175	      "mcnemar_p_all_gt_05": true
176	    },
177	    "tables": [
178	      "Appendix: constraint ablation comparison"
179	    ],
180	    "figures": [],
181	    "analysis": "MaxSAT≈count-only 在 worst tier 下是 devastating: 论文的 \"symbolic\" 框架核心价值被掏空。 但可 reframe 为 evidence: \"even the most powerful aggregation mechanism cannot help  when constraints are non-independent\"。即 solver 能力不是瓶颈，constraint quality/independence 才是。\n\n\nMaxSAT 和 count-only 在 804 题中仅 1 题不同。这证明 MAX-SAT solver 几乎无贡献—— 简单 count constraints per answer 就等价。原因: constraints 的 satisfiability weights  几乎不区分 answers (mean_sat_ratio≈0.96，接近 1.0)。 Worst tier 下 reviewer: \"所以 SAT solver 是 over-engineering，constraint counting 就够了—— 但 counting 本身也不 work (delta≈0)\"。双重打击。\n"
182	  },
183	  {
184	    "name": "sica_deepseek_r1_llama_8b",
185	    "description": "DeepSeek-R1-Distill-Qwen-7B on D012 60q",
186	    "results": {
187	      "sica_accuracy": 0.683,
188	      "sc_accuracy": 0.717,
189	      "delta_pp": -3.33,
190	      "multi_candidate_rate": 0.583,
191	      "truncated_traces": 72,
192	      "mcnemar_p": 0.48
193	    },
194	    "tables": [
195	      "T1: DeepSeek-R1 行"
196	    ],
197	    "figures": [],
198	    "analysis": "DeepSeek-R1 delta=-3.33pp 在 worst tier 下补充了 exp-046 (Mistral-PW) 的 evidence: high C0 但 low constraint quality → negative delta。但 reviewer 可能归咎于 truncation artifact 而非 fundamental。\n\n\nReasoning model distillation 产生 longer traces (72 truncated) 但 reasoning quality  不 translate to better constraints。High C0 (58.3%) 但 delta negative —  与 Mistral-PW600 类似的 pattern (high diversity + low quality = negative)。 Truncation 是额外 confound: 被截断的 traces 产生 incomplete constraints。\n"
199	  },
200	  {
201	    "name": "logic_lm_baseline",
202	    "description": "Logic-LM × K + majority vote on FOLIO, CPU-only",
203	    "results": {
204	      "logic_lm_k_vote_accuracy": 0.755,
205	      "sica_accuracy": 0.745,
206	      "sc_accuracy": 0.75,
207	      "logic_lm_vs_sc_delta_pp": 0.5,
208	      "logic_lm_vs_sica_delta_pp": 1.0
209	    },
210	    "tables": [
211	      "Appendix: Logic-LM comparison"
212	    ],
213	    "figures": [],
214	    "analysis": "Logic-LM baseline 在 worst tier 下进一步削弱 MAX-SAT aggregation 的 novelty。 但可以 reframe: \"即使 Logic-LM style 的 approach 也不超过 SC， 问题在 extraction 而非 aggregation strategy\"——与 oracle gap 叙事一致。\n\n\nLogic-LM 单 trace FOL verification × K 然后 vote 的精度 ≈ SC ≈ SICA。 原因: 单 trace FOL 质量和多 trace aggregated FOL 质量差不多——因为 traces 高度相关， 多 trace 不增加新 constraint information。 Worst tier: reviewer 说 \"Logic-LM × K 就和 SICA 一样好，那 MAX-SAT aggregation 的意义是什么？\"\n"
215	  },
216	  {
217	    "name": "weighted_sc_baseline",
218	    "description": "Weighted SC (length/logprob/constraint-count) on exp-001 data",
219	    "results": {
220	      "sc_uniform_accuracy": 0.762,
221	      "inv_length_accuracy": 0.767,
222	      "length_weighted_accuracy": 0.753,
223	      "constraint_count_accuracy": 0.753,
224	      "all_nonsignificant": true,
225	      "inv_length_vs_sc_p": 0.453
226	    },
227	    "tables": [
228	      "Appendix: weighted SC comparison"
229	    ],
230	    "figures": [],
231	    "analysis": "Weighted SC 无效在 worst tier 下实际是 neutral-to-positive: 证明 simple weighting  也不能 beat SC，strengthens \"independence is the bottleneck not aggregation strategy\"。 但 reviewer 可能说 \"you should try more sophisticated weighting (e.g., diversity-weighted)\"。\n\n\n所有 weighting schemes 与 uniform SC 无 significant 差异。 Inv-length 略好 (+0.5pp) 但完全 n.s.。Constraint-count weighting 和 length-weighting  甚至略 worse。原因: weighting 不解决 independence 问题——如果 votes 本身高度相关， re-weighting 相关 votes 不改变结果。\n"
232	  },
233	  {
234	    "name": "sica_strategyqa_14b",
235	    "description": "Qwen2.5-14B on StrategyQA 60q",
236	    "results": {
237	      "sica_accuracy": 0.567,
238	      "sc_accuracy": 0.533,
239	      "delta_pp": 3.33,
240	      "multi_candidate_rate": 0.1,
241	      "mcnemar_p": "n.s.",
242	      "bootstrap_p": 0.135,
243	      "extraction_rate_trace": 0.704
244	    },
245	    "tables": [
246	      "T1: StrategyQA 行"
247	    ],
248	    "figures": [],
249	    "analysis": "StrategyQA 的 positive-but-n.s. delta 在 worst tier 下是 problematic:  不够 clean 作为 null result (方向 positive)，又不够 significant 作为 positive result。 Reviewer 可能要求 larger n 来 resolve ambiguity。\n\n\nStrategyQA C0=10% 远低于 FOLIO (38%)。Binary format + commonsense domain →  大多数问题 SC unanimous。Delta=+3.33pp 来自仅 2 个 discordant problems (n=60)， 完全 n.s.。Extraction rate 低 (70%) 因为 commonsense reasoning 难以形式化为 FOL。 Worst tier: reviewer 视为 Type B (domain 不可形式化) 的 additional evidence， 但 +3.33pp 不是 clean null (creates ambiguity)。\n"
250	  },
251	  {
252	    "name": "sica_arc_challenge_14b",
253	    "description": "Qwen2.5-14B on ARC-Challenge 60q",
254	    "results": {
255	      "sica_accuracy": 0.95,
256	      "sc_accuracy": 0.967,
257	      "delta_pp": -1.67,
258	      "multi_candidate_rate": 0.05,
259	      "discordant_sica_wins": 0,
260	      "discordant_sc_wins": 1
261	    },
262	    "tables": [
263	      "T1: ARC 行"
264	    ],
265	    "figures": [],
266	    "analysis": "ARC 是 clean Type A negative。Worst tier 下 reviewer 不 surprised 但也不 impressed。 \"Of course SICA doesn't help a 97% baseline\" — trivially expected。\n\n\n14B 在 ARC-Challenge 极强 (SC≈97%)，C0=5% — 几乎所有问题 unanimous。 SICA 在唯一 discordant problem 上选错 → delta=-1.67pp。 Deep Type A regime: 模型已经极度 confident 且正确，constraints 无法 add value。\n"
267	  },
268	  {
269	    "name": "constraint_quality_correlation",
270	    "description": "Constraint precision per domain × model, correlate with C0 and delta",
271	    "results": {
272	      "conditions_analyzed": 10,
273	      "constraint_precision_delta_r": 0.28,
274	      "constraint_precision_delta_p": 0.43,
275	      "c0_precision_r": -0.15,
276	      "c0_precision_p": 0.68,
277	      "high_c0_low_quality_conditions": 3,
278	      "high_c0_high_quality_conditions": 2
279	    },
280	    "tables": [],
281	    "figures": [],
282	    "analysis": "exp-019 在 worst tier 下 kills the clean \"inverse C0-quality correlation\" story。 No single metric (C0, Eff-K, constraint precision) predicts SICA effectiveness。 Must retreat to \"SICA effectiveness is determined by a complex interaction of factors  that we characterize but cannot predict\" — weak for a paper claim。\n\n\nWorst tier: constraint quality 与 delta 之间无 significant correlation。 High C0 不 predict low quality (counter to capability trap theory)—— 有 high C0 + high quality 的 conditions (LLaMA D012) 和 high C0 + low quality 的 (Mistral PW600)。 R≈0.28 (n=10) 完全无 statistical power。 Capability trap 作为 clean theory 不 hold: 实际 pattern 是 noisy 的 condition-specific interactions。\n"
283	  },
284	  {
285	    "name": "mistral_k_sensitivity",
286	    "description": "Mistral-7B K=4/8/12/16/20 on FOLIO-204, seed 42",
287	    "results": {
288	      "K4_sica_accuracy": 0.534,
289	      "K4_sc_accuracy": 0.544,
290	      "K4_delta_pp": -0.98,
291	      "K8_sica_accuracy": 0.559,
292	      "K8_sc_accuracy": 0.539,
293	      "K8_delta_pp": 1.96,
294	      "K12_sica_accuracy": 0.593,
295	      "K12_sc_accuracy": 0.544,
296	      "K12_delta_pp": 4.9,
297	      "K16_sica_accuracy": 0.554,
298	      "K16_sc_accuracy": 0.539,
299	      "K16_delta_pp": 1.47,
300	      "K20_sica_accuracy": 0.524,
301	      "K20_sc_accuracy": 0.549,
302	      "K20_delta_pp": -2.45,
303	      "inverted_u_visual": "无可辨识 pattern，noise ≫ signal",
304	      "peak_K": 12,
305	      "peak_delta_pp": 4.9,
306	      "k4_vs_k12_difference_significant": false
307	    },
308	    "tables": [
309	      "T5: K sensitivity — Mistral 列 with CI"
310	    ],
311	    "figures": [],
312	    "analysis": "K sensitivity 在 worst tier 下是 paper 的最大损失之一。原本 inverted-U 是 Table 5 / Figure 3 的 hero result，解释了 \"why K=12 is optimal\"。现在只能说 \"K=12 happened to give the best result  in this specific seed, but we cannot distinguish signal from noise\"。 Frame 改为 \"high variance across K values demonstrates fragility of the effect\"—— 从 clean ablation contribution 降级为 fragility evidence。\n\n\nWorst tier 核心假设: K sensitivity 无 inverted-U。K=12 仍然是 peak (因为 exp-033 的 seed 42  就是用 K=12) 但 K=8 和 K=16 的 delta 在 noise band 内 random walk。 K=4 delta≈-1pp, K=8≈+2pp, K=12≈+5pp, K=16≈+1.5pp, K=20≈-2.5pp。 看 curve: 不是 smooth inverted-U 而是 up-down-up-down noise pattern。 K=8→K=12 jump (+3pp) 和 K=12→K=16 drop (-3.4pp) 都可能是 random variation at n=204。 CI bars 大量重叠，无法 reject \"all K have same delta\" null hypothesis。 Eff-K 也不 monotonically increase with K (因为 κ 本身随 K 变化)。\n"
313	  },
314	  {
315	    "name": "multitemp_mistral_folio",
316	    "description": "Multi-temperature (T=0.3/0.7/1.0 混合) Mistral-7B FOLIO-204",
317	    "results": {
318	      "sica_accuracy": 0.564,
319	      "sc_accuracy": 0.544,
320	      "delta_pp": 2.45,
321	      "mcnemar_p": 0.18,
322	      "trace_diversity_increase_pct": 35,
323	      "effk_multitemp": 2.8,
324	      "effk_single_t07": 1.85
325	    },
326	    "tables": [
327	      "T_remediation: multi-temp 行改为 '+2.45pp (n.s.)' 而非 'negative'"
328	    ],
329	    "figures": [],
330	    "analysis": "Multi-temp positive 是 worst tier 的 second most damaging result (after K sensitivity noise)。 \"9 种修复全部失败\" 要改为 \"8 种修复失败 + 1 种 promising but underpowered\"。 Reviewer 会问: \"为什么不 scale up multi-temp to n=600？\" — 如果我们没做，是 obvious gap； 如果做了且 positive，paper narrative completely changes。 唯一 defense: argue that +2.45pp n.s. is within noise, and even if real,  Eff-K increase from 1.85→2.8 still far below nominal K=12。\n\n\nWorst tier 核心假设: multi-temp 意外 positive (≥+2pp)。 Multi-temp 通过混合不同温度 traces 确实增加了 diversity (Eff-K 从 1.85 → 2.8)。 Delta=+2.45pp 虽然 n.s. (p=0.18) 但方向 positive。 这动摇 \"diversity alone is not sufficient\" claim——如果 simple temperature mixing  就能 partially recover SICA effectiveness，那 independence bottleneck 不是 \"fundamental\"。 Reviewer: \"你说 9 种修复全部失败，但 multi-temp 实际上 showed promise？\" 无法再 claim \"trap is fundamental\" 当 diversity intervention shows positive direction。\n"
331	  },
332	  {
333	    "name": "mistral_folio204_t03",
334	    "description": "Mistral-7B FOLIO-204 at T=0.3",
335	    "results": {
336	      "sica_accuracy": 0.574,
337	      "sc_accuracy": 0.534,
338	      "delta_pp": 3.92,
339	      "mcnemar_p": 0.065,
340	      "multi_candidate_rate": 0.55,
341	      "effk_t03": 1.45
342	    },
343	    "tables": [
344	      "Appendix T sensitivity table: T=0.3 行"
345	    ],
346	    "figures": [],
347	    "analysis": "T=0.3 comparable to T=0.7 是 worst tier 定义的关键指标。 叙事从 \"narrow window of fragile effect\" 变成 \"moderate robustness across low-medium temperatures,  failure only at high T\"——这实际上 WEAKENS the pure-negative-results paper framing。 If SICA works at T=0.3-0.7, it's not a \"dead end\" but a \"limited but reproducible effect\"。 Reviewer: \"这看起来不像 pure negative results，更像 modest positive results with caveats\"。 Paper 陷入尴尬中间地带: 不够 positive 做 method paper，不够 negative 做 clean diagnostic paper。\n\n\nWorst tier 核心假设: T=0.3 delta ≥+3pp，与 T=0.7 的 +4.9pp 可比。 T=0.3 SC 略低于 T=0.7 (53.4% vs 54.4%) 但 delta 仍然 substantial (+3.92pp)。 这 destroys \"narrow temperature window\" narrative。原来的故事是 \"SICA only works at T=0.7,  collapses at T=1.0\" → 暗示 very specific sweet spot。 现在 T=0.3 (+3.92pp), T=0.7 (+4.90pp), T=1.0 (+0.49pp) → SICA 在 low-to-medium T  都有效，只是 T=1.0 太 noisy 才 collapse。 这个 pattern 不是 \"fragile\" 而是 \"works except at high T\"——undermines fragility framing。\n"
348	  },
349	  {
350	    "name": "mistral_folio204_t05",
351	    "description": "Mistral-7B FOLIO-204 at T=0.5",
352	    "results": {
353	      "sica_accuracy": 0.564,
354	      "sc_accuracy": 0.539,
355	      "delta_pp": 2.45,
356	      "mcnemar_p": 0.23,
357	      "multi_candidate_rate": 0.62,
358	      "effk_t05": 1.65
359	    },
360	    "tables": [
361	      "Appendix T sensitivity table: T=0.5 行"
362	    ],
363	    "figures": [],
364	    "analysis": "T=0.5 填充了 curve 但增加了 noise。4 个 temperature points 无 clean trend  (not inverted-U, not monotonic, not plateau-then-cliff)。 Worst tier 下 T sensitivity section 从 \"clean ablation\" 降级为 \"noisy exploration\"。 Only defensible claim: \"SICA delta decreases substantially at T=1.0\"， but even this is one data point (could reframe as \"high temperature degrades constraint extraction\"  which is somewhat obvious)。\n\n\nT=0.5 delta=+2.45pp 进一步填充 T sensitivity curve。 Pattern: T=0.3 (+3.92pp) > T=0.5 (+2.45pp) < T=0.7 (+4.90pp) > T=1.0 (+0.49pp)。 不是 monotonic decline 也不是 clean peak——是 noisy 的 non-monotonic pattern。 T=0.5 比 T=0.3 低可能是 random noise at n=204。 Combined with T=0.3 result，T sensitivity curve 是 \"generally positive at low-medium T,  negative at high T\" 但无 clean functional form。\n"
365	  },
366	  {
367	    "name": "effk_sc_joint_prediction",
368	    "description": "Eff-K + SC joint prediction accuracy across all 12+ conditions",
369	    "results": {
370	      "total_conditions": 12,
371	      "correctly_predicted_positive": 2,
372	      "correctly_predicted_negative": 4,
373	      "incorrectly_predicted": 6,
374	      "prediction_accuracy_pct": 50.0,
375	      "key_failures": [
376	        "Mistral-PW600: Eff-K=3.63 (highest) predicts positive but delta=-2.83pp",
377	        "Mistral-s42 vs s123: similar Eff-K+SC but delta differs by 1.47pp",
378	        "LLaMA-D012: Eff-K unknown but high C0 → predicted positive, actual +6.67pp n.s.",
379	        "Mistral-s456: Eff-K=2.22 similar to s123 (2.17) but delta reverses sign"
380	      ]
381	    },
382	    "tables": [
383	      "T3: 增加 prediction hit/miss column"
384	    ],
385	    "figures": [],
386	    "analysis": "Joint prediction ≤50% accuracy 是 worst tier 下 Condorcet framework 的死亡判决。 不能说 \"Eff-K predicts SICA effectiveness\" 只能说 \"Eff-K explains why Qwen family  uniformly fails\"。Claim 1 从 \"Independence Bottleneck\" (predictive) 降为  \"Independence Observation\" (descriptive)。Condorcet 从 core claim 降入 discussion。\n\nWorst tier: Eff-K+SC framework predicts ≤6/12 conditions correctly (≤50%)。 跨模型 direction 正确 (Qwen→0, Mistral→variable) 但 Mistral 内部完全不 work。 Eff-K 与 delta 在 Mistral seeds 内无 monotonic relationship (s42: Eff-K=1.85, delta=+4.9;  s123: Eff-K=2.17, delta=+3.4; s456: Eff-K=2.22, delta=-0.5)——方向甚至相反。 PW-600 (Eff-K=3.63, delta=-2.83) 用 \"SC too low\" 勉强解释，但 reviewer 会说  这是 post-hoc rationalization。 Framework 降级: \"Eff-K is a necessary condition for cross-model comparison  but has no within-model predictive power\"——这是一个 much weaker claim。\n"
387	  }
388	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6f08611-f643-4f9c-ae83-5ceb3bd28b93",
  "isSidechain": false,
  "promptId": "6cd4ba32-185c-4e26-8eaf-fcddb4213dff",
  "type": "user",
  "uuid": "225dc03b-1650-43e9-a186-a3861836b007",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"sica_k_ablation_14b\",\n    \"description\": \"K=6/8/11/12/16/20 sensitivity on D012 60q, Qwen2.5-14B\",\n    \"results\": {\n      \"K6_delta_pp\": 0.0,\n      \"K8_delta_pp\": -1.7,\n      \"K11_delta_pp\": 0.0,\n      \"K12_delta_pp\": -5.0,\n      \"K16_delta_pp\": -3.3,\n      \"K20_delta_pp\": -3.3,\n      \"inverted_u_visual\": \"无——SICA 在所有 K 均 ≤ SC，随 K 增大单调恶化\",\n      \"K11_odd_k_gap\": 0.0\n    },\n    \"tables\": [\n      \"T5 (partial): K sensitivity — 仅 14B 列\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"14B K ablation 在 worst tier 下完全符合 Type A 预期——SC 太高时 SICA 无论 K 取何值都无法超越。 这本身不是 worst tier 的关键问题（实际已完成数据也如此），关键是 Mistral K ablation (exp-051) 也无 clean pattern 时，整个 K sensitivity 叙事崩塌。\\n\\n\\nQwen-14B SC≈75% (Type A regime)，confirmation bias 主导。K 增大只增加冗余 correlated constraints， 不增加独立信息。Eff-K≈1.3 意味着 K=6 和 K=20 的 effective voters 几乎相同（~1.3）。 无 inverted-U 因为 14B 在此 regime 下 SICA 本身就没有正向效应，K 的变化只引入更多 noise。 K=11 odd-K 消除 tiebreak 后 gap=0 进一步确认 14B 效应完全是 tiebreak artifact。\\n\"\n  },\n  {\n    \"name\": \"tiebreak_baseline_analysis\",\n    \"description\": \"SICA vs SC-random-tiebreak vs SC-deterministic, CPU-only\",\n    \"results\": {\n      \"sica_tiebreak_accuracy_pct\": 80.0,\n      \"random_tiebreak_accuracy_pct\": 50.0,\n      \"alphabetical_tiebreak_accuracy_pct\": 60.0,\n      \"first_seen_tiebreak_accuracy_pct\": 40.0,\n      \"n_tiebreak_problems\": 5\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Tiebreak 80% 看似有意义但 n=5 完全无 statistical significance。 Worst tier 下 reviewer 直接忽略此 result (\\\"interesting but underpowered\\\")。\\n\\n\\nTiebreak 分析在 worst tier 下结果不变（已完成的 CPU 分析）。问题在于 n=5 tiebreak cases 太少， reviewer 会质疑 80% (4/5) 的 statistical power。且 SICA 的 tiebreak 优势仅在极少数问题上体现， 不构成 compelling evidence。在 worst tier 下 reviewer 将此视为 anecdotal。\\n\"\n  },\n  {\n    \"name\": \"sica_7b_scaling\",\n    \"description\": \"Qwen2.5-7B on D012 60q, test C0-as-predictor\",\n    \"results\": {\n      \"sica_accuracy\": 0.683,\n      \"sc_accuracy\": 0.683,\n      \"delta_pp\": 0.0,\n      \"multi_candidate_rate\": 0.433,\n      \"mcnemar_p\": 1.0,\n      \"discordant_sica_wins\": 2,\n      \"discordant_sc_wins\": 2\n    },\n    \"tables\": [\n      \"T1: Qwen-7B 行\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen-7B 支持跨模型 Eff-K 叙事（Qwen 家族 Eff-K 低→0 gain）但在 worst tier 下 reviewer 认为这只是\\\"同家族 same behavior\\\"，不算独立 evidence。\\n\\n\\n7B SC≈68% 仍在 Type A regime 上沿（C0=43% 比 14B 高但仍不够）。 Qwen 家族内 Eff-K 普遍 ≈1.2-1.3，7B 的 lower capability 提高 C0 但不提高 constraint quality。 Constraints 仍然 mirror 模型偏差。Delta=0 确认 Qwen 家族 SICA 无效。 Worst case: 与 14B 结果一致，无法单独贡献 regime boundary 叙事。\\n\"\n  },\n  {\n    \"name\": \"qwq_32b_operating_regime\",\n    \"description\": \"QwQ-32B negative control, data from MVP phase\",\n    \"results\": {\n      \"aggregate_c0_effective_pct\": 2.6,\n      \"aime_delta_pp\": 0.0,\n      \"proofwriter_delta_pp\": -5.9,\n      \"total_problems\": 46,\n      \"c0_below_threshold\": true\n    },\n    \"tables\": [\n      \"T1: QwQ-32B 行\",\n      \"Appendix: QwQ negative control detail\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"QwQ-32B C0<5% 是最 clean 的 negative result，但 worst tier 下 reviewer 视为 obvious—— \\\"当然 reasoning model 不需要 SICA\\\"。价值被低估。\\n\\n\\nReasoning model 的 deterministic chain 产生近乎相同 traces (C0 effective≈2.6%)。 SICA≡SC 是必然——无 multi-candidate problems，MAX-SAT 无从发挥。 PW delta=-5.9pp 因 n=17 不 significant 但方向 negative。 Worst case: reviewer 认为 QwQ 是 trivially expected negative control，不算 contribution。\\n\"\n  },\n  {\n    \"name\": \"c0_diagnostic_validation\",\n    \"description\": \"C0 vs SICA-SC gap scatter across all models/K values\",\n    \"results\": {\n      \"conditions_plotted\": 12,\n      \"c0_delta_correlation_r\": 0.31,\n      \"c0_delta_correlation_p\": 0.33,\n      \"correctly_predicted_direction\": 5,\n      \"total_conditions\": 12,\n      \"prediction_accuracy_pct\": 41.7\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"C0 diagnostic 在 worst tier 下失去 predictive power。只能做 necessary condition (C0<5% → SICA≡SC) 但 sufficient condition 不成立。Reviewer 会说 \\\"C0 just tells you there's variance, not that SICA helps\\\"。 降级为 \\\"deployment screening tool\\\" (排除 SICA 必然无用的 cases) 而非 \\\"predictor\\\"。\\n\\n\\nWorst tier 核心假设: Eff-K+SC joint prediction ≤6/12 conditions 方向正确。 C0 单独作为 predictor 更差——Mistral PW-600 (C0 high, delta negative) 和  LLaMA-8B FOLIO (C0 high, delta negative) 都是反例。 Scatter plot 呈现 no clean trend，high C0 对应 both positive 和 negative deltas。 Correlation r≈0.31 不 significant (p>0.3, n=12)。\\n\"\n  },\n  {\n    \"name\": \"sica_72b_awq\",\n    \"description\": \"Qwen2.5-72B-AWQ 4-bit on D012 60q\",\n    \"results\": {\n      \"sica_accuracy\": 0.817,\n      \"sc_accuracy\": 0.833,\n      \"delta_pp\": -1.67,\n      \"multi_candidate_rate\": 0.2,\n      \"mcnemar_p\": 0.625,\n      \"extraction_rate\": 0.95\n    },\n    \"tables\": [\n      \"T1: Qwen-72B 行\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"72B 进一步确认 Type A regime。但 worst tier 下 reviewer 说 \\\"you're just showing that SICA doesn't help strong models — this is obvious\\\"。缺乏新 insight。\\n\\n\\n72B SC≈83% (deep Type A regime)。C0 进一步降至 ~20% 因为更大模型更 unanimous。 SICA 因 confirmation bias 甚至略 negative——constraints 强化已有高置信度答案， 少数 override 方向是错的。Qwen 家族 pattern 延续: 更大模型→更高 SC→更低 C0→更无用 SICA。\\n\"\n  },\n  {\n    \"name\": \"constraint_quality_case_studies\",\n    \"description\": \"5-10 representative questions 的 constraint 质量定性分析\",\n    \"results\": {\n      \"cases_analyzed\": 8,\n      \"trivially_satisfied_pct\": 45,\n      \"confirmation_bias_cases\": 6,\n      \"genuinely_informative_constraints\": 1,\n      \"constraint_mirrors_model_answer_pct\": 78\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Case studies 支持 confirmation bias 叙事但在 worst tier 下 reviewer 认为 n=8 qualitative analysis 不算 rigorous evidence。\\\"Show me this at scale\\\" → 需要 exp-019 的 correlation， 但 exp-019 也 noisy。\\n\\n\\n定性分析在 worst tier 下揭示 constraints 几乎完全 mirror 模型的 chain-of-thought 结论。 Even \\\"discriminative\\\" constraints 的 discriminative direction 与模型偏差一致。 唯一 genuinely informative case 是模型恰好 extract 了 premise 中的 explicit logical structure。 但 reviewer 可能认为 case studies 是 cherry-picked。\\n\"\n  },\n  {\n    \"name\": \"overhead_analysis\",\n    \"description\": \"Wall-time breakdown per question\",\n    \"results\": {\n      \"mean_total_wall_s\": 61.6,\n      \"trace_gen_pct\": 51.3,\n      \"extraction_pct\": 47.0,\n      \"maxsat_pct\": 0.005,\n      \"sica_overhead_pct\": 48.7\n    },\n    \"tables\": [\n      \"Appendix: overhead breakdown table\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Overhead analysis 在 worst tier 下变成 anti-argument: \\\"你花了 2× compute 得到了 noise\\\"。 但可以 reframe 为 \\\"extraction is the bottleneck, not solving\\\" (MAX-SAT <0.01% time)， 说明未来研究应聚焦 extraction quality 而非 solver improvements。\\n\\n\\nSICA 几乎 doubles wall time (49% overhead) 但 delta≈0 across most conditions。 Worst tier 下 cost-benefit 极差: 2× compute for 0 gain in majority of conditions, fragile +4.9pp in one specific setting (Mistral/FOLIO/T=0.7/K=12/s42)。 Reviewer: \\\"this is not practical\\\"。\\n\"\n  },\n  {\n    \"name\": \"sica_llama_8b\",\n    \"description\": \"LLaMA-3.1-8B on D012 60q\",\n    \"results\": {\n      \"sica_accuracy\": 0.667,\n      \"sc_accuracy\": 0.6,\n      \"delta_pp\": 6.67,\n      \"multi_candidate_rate\": 0.617,\n      \"mcnemar_p\": 0.219,\n      \"truncated_traces\": 44,\n      \"answer_extraction_rate\": 0.896\n    },\n    \"tables\": [\n      \"T1: LLaMA-8B 行\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"LLaMA-8B 是 worst tier 的典型 case: small-n positive 被 larger-n 反转。 Reviewer 会直接引用 FOLIO-204 result dismiss D012 result。 Combined evidence: SICA on LLaMA 是 noise。\\n\\n\\nLLaMA-8B delta=+6.67pp 看似 positive 但 p=0.219 (n=60) 完全 n.s.。 且 truncated_traces=44 和 answer_extraction_rate=89.6% 说明 pipeline 对 LLaMA 有 artifacts。 Worst tier 下 reviewer 质疑: (1) n.s. result; (2) 44 truncated traces 是否 confound; (3) answer extraction 失败的 traces 是否 systematically biased。 扩展到 FOLIO-204 (exp-020) 后 delta 反转为 -2.45pp → D012 的 +6.67pp 是 small-n artifact。\\n\"\n  },\n  {\n    \"name\": \"gsm8k_pilot_14b\",\n    \"description\": \"Qwen2.5-14B on GSM8K 30q pilot\",\n    \"results\": {\n      \"sica_accuracy\": 0.967,\n      \"sc_accuracy\": 0.967,\n      \"delta_pp\": 0.0,\n      \"multi_candidate_rate\": 0.133,\n      \"extraction_success_rate\": 0.147\n    },\n    \"tables\": [\n      \"T1: GSM8K 行 (footnote: extraction failure)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"GSM8K 在 worst tier 下是 domain 不匹配的 obvious failure。Reviewer 不会 penalize 但也不加分。 Reframe 为 Type B (domain not formalizable as FOL) 的 additional evidence。\\n\\n\\n14B 在 GSM8K 准确率极高 (97%)，C0=13.3% 低于 threshold。 更关键的是 FOL extraction 几乎完全失败 (success=14.7%) — math domain 的 constraints 需要 numerical reasoning 而非 propositional logic，SICA pipeline 在此 domain 根本不适用。 这不是 SICA 的 negative evidence 而是 domain mismatch。\\n\"\n  },\n  {\n    \"name\": \"constraint_ablation\",\n    \"description\": \"MaxSAT vs count-only vs random-weight, CPU-only on exp-001 data\",\n    \"results\": {\n      \"maxsat_accuracy\": 0.765,\n      \"count_only_accuracy\": 0.766,\n      \"random_weight_accuracy\": 0.759,\n      \"sc_baseline_accuracy\": 0.762,\n      \"agreement_maxsat_vs_countonly\": \"803/804\",\n      \"mcnemar_p_all_gt_05\": true\n    },\n    \"tables\": [\n      \"Appendix: constraint ablation comparison\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"MaxSAT≈count-only 在 worst tier 下是 devastating: 论文的 \\\"symbolic\\\" 框架核心价值被掏空。 但可 reframe 为 evidence: \\\"even the most powerful aggregation mechanism cannot help  when constraints are non-independent\\\"。即 solver 能力不是瓶颈，constraint quality/independence 才是。\\n\\n\\nMaxSAT 和 count-only 在 804 题中仅 1 题不同。这证明 MAX-SAT solver 几乎无贡献—— 简单 count constraints per answer 就等价。原因: constraints 的 satisfiability weights  几乎不区分 answers (mean_sat_ratio≈0.96，接近 1.0)。 Worst tier 下 reviewer: \\\"所以 SAT solver 是 over-engineering，constraint counting 就够了—— 但 counting 本身也不 work (delta≈0)\\\"。双重打击。\\n\"\n  },\n  {\n    \"name\": \"sica_deepseek_r1_llama_8b\",\n    \"description\": \"DeepSeek-R1-Distill-Qwen-7B on D012 60q\",\n    \"results\": {\n      \"sica_accuracy\": 0.683,\n      \"sc_accuracy\": 0.717,\n      \"delta_pp\": -3.33,\n      \"multi_candidate_rate\": 0.583,\n      \"truncated_traces\": 72,\n      \"mcnemar_p\": 0.48\n    },\n    \"tables\": [\n      \"T1: DeepSeek-R1 行\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"DeepSeek-R1 delta=-3.33pp 在 worst tier 下补充了 exp-046 (Mistral-PW) 的 evidence: high C0 但 low constraint quality → negative delta。但 reviewer 可能归咎于 truncation artifact 而非 fundamental。\\n\\n\\nReasoning model distillation 产生 longer traces (72 truncated) 但 reasoning quality  不 translate to better constraints。High C0 (58.3%) 但 delta negative —  与 Mistral-PW600 类似的 pattern (high diversity + low quality = negative)。 Truncation 是额外 confound: 被截断的 traces 产生 incomplete constraints。\\n\"\n  },\n  {\n    \"name\": \"logic_lm_baseline\",\n    \"description\": \"Logic-LM × K + majority vote on FOLIO, CPU-only\",\n    \"results\": {\n      \"logic_lm_k_vote_accuracy\": 0.755,\n      \"sica_accuracy\": 0.745,\n      \"sc_accuracy\": 0.75,\n      \"logic_lm_vs_sc_delta_pp\": 0.5,\n      \"logic_lm_vs_sica_delta_pp\": 1.0\n    },\n    \"tables\": [\n      \"Appendix: Logic-LM comparison\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Logic-LM baseline 在 worst tier 下进一步削弱 MAX-SAT aggregation 的 novelty。 但可以 reframe: \\\"即使 Logic-LM style 的 approach 也不超过 SC， 问题在 extraction 而非 aggregation strategy\\\"——与 oracle gap 叙事一致。\\n\\n\\nLogic-LM 单 trace FOL verification × K 然后 vote 的精度 ≈ SC ≈ SICA。 原因: 单 trace FOL 质量和多 trace aggregated FOL 质量差不多——因为 traces 高度相关， 多 trace 不增加新 constraint information。 Worst tier: reviewer 说 \\\"Logic-LM × K 就和 SICA 一样好，那 MAX-SAT aggregation 的意义是什么？\\\"\\n\"\n  },\n  {\n    \"name\": \"weighted_sc_baseline\",\n    \"description\": \"Weighted SC (length/logprob/constraint-count) on exp-001 data\",\n    \"results\": {\n      \"sc_uniform_accuracy\": 0.762,\n      \"inv_length_accuracy\": 0.767,\n      \"length_weighted_accuracy\": 0.753,\n      \"constraint_count_accuracy\": 0.753,\n      \"all_nonsignificant\": true,\n      \"inv_length_vs_sc_p\": 0.453\n    },\n    \"tables\": [\n      \"Appendix: weighted SC comparison\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Weighted SC 无效在 worst tier 下实际是 neutral-to-positive: 证明 simple weighting  也不能 beat SC，strengthens \\\"independence is the bottleneck not aggregation strategy\\\"。 但 reviewer 可能说 \\\"you should try more sophisticated weighting (e.g., diversity-weighted)\\\"。\\n\\n\\n所有 weighting schemes 与 uniform SC 无 significant 差异。 Inv-length 略好 (+0.5pp) 但完全 n.s.。Constraint-count weighting 和 length-weighting  甚至略 worse。原因: weighting 不解决 independence 问题——如果 votes 本身高度相关， re-weighting 相关 votes 不改变结果。\\n\"\n  },\n  {\n    \"name\": \"sica_strategyqa_14b\",\n    \"description\": \"Qwen2.5-14B on StrategyQA 60q\",\n    \"results\": {\n      \"sica_accuracy\": 0.567,\n      \"sc_accuracy\": 0.533,\n      \"delta_pp\": 3.33,\n      \"multi_candidate_rate\": 0.1,\n      \"mcnemar_p\": \"n.s.\",\n      \"bootstrap_p\": 0.135,\n      \"extraction_rate_trace\": 0.704\n    },\n    \"tables\": [\n      \"T1: StrategyQA 行\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"StrategyQA 的 positive-but-n.s. delta 在 worst tier 下是 problematic:  不够 clean 作为 null result (方向 positive)，又不够 significant 作为 positive result。 Reviewer 可能要求 larger n 来 resolve ambiguity。\\n\\n\\nStrategyQA C0=10% 远低于 FOLIO (38%)。Binary format + commonsense domain →  大多数问题 SC unanimous。Delta=+3.33pp 来自仅 2 个 discordant problems (n=60)， 完全 n.s.。Extraction rate 低 (70%) 因为 commonsense reasoning 难以形式化为 FOL。 Worst tier: reviewer 视为 Type B (domain 不可形式化) 的 additional evidence， 但 +3.33pp 不是 clean null (creates ambiguity)。\\n\"\n  },\n  {\n    \"name\": \"sica_arc_challenge_14b\",\n    \"description\": \"Qwen2.5-14B on ARC-Challenge 60q\",\n    \"results\": {\n      \"sica_accuracy\": 0.95,\n      \"sc_accuracy\": 0.967,\n      \"delta_pp\": -1.67,\n      \"multi_candidate_rate\": 0.05,\n      \"discordant_sica_wins\": 0,\n      \"discordant_sc_wins\": 1\n    },\n    \"tables\": [\n      \"T1: ARC 行\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"ARC 是 clean Type A negative。Worst tier 下 reviewer 不 surprised 但也不 impressed。 \\\"Of course SICA doesn't help a 97% baseline\\\" — trivially expected。\\n\\n\\n14B 在 ARC-Challenge 极强 (SC≈97%)，C0=5% — 几乎所有问题 unanimous。 SICA 在唯一 discordant problem 上选错 → delta=-1.67pp。 Deep Type A regime: 模型已经极度 confident 且正确，constraints 无法 add value。\\n\"\n  },\n  {\n    \"name\": \"constraint_quality_correlation\",\n    \"description\": \"Constraint precision per domain × model, correlate with C0 and delta\",\n    \"results\": {\n      \"conditions_analyzed\": 10,\n      \"constraint_precision_delta_r\": 0.28,\n      \"constraint_precision_delta_p\": 0.43,\n      \"c0_precision_r\": -0.15,\n      \"c0_precision_p\": 0.68,\n      \"high_c0_low_quality_conditions\": 3,\n      \"high_c0_high_quality_conditions\": 2\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"exp-019 在 worst tier 下 kills the clean \\\"inverse C0-quality correlation\\\" story。 No single metric (C0, Eff-K, constraint precision) predicts SICA effectiveness。 Must retreat to \\\"SICA effectiveness is determined by a complex interaction of factors  that we characterize but cannot predict\\\" — weak for a paper claim。\\n\\n\\nWorst tier: constraint quality 与 delta 之间无 significant correlation。 High C0 不 predict low quality (counter to capability trap theory)—— 有 high C0 + high quality 的 conditions (LLaMA D012) 和 high C0 + low quality 的 (Mistral PW600)。 R≈0.28 (n=10) 完全无 statistical power。 Capability trap 作为 clean theory 不 hold: 实际 pattern 是 noisy 的 condition-specific interactions。\\n\"\n  },\n  {\n    \"name\": \"mistral_k_sensitivity\",\n    \"description\": \"Mistral-7B K=4/8/12/16/20 on FOLIO-204, seed 42\",\n    \"results\": {\n      \"K4_sica_accuracy\": 0.534,\n      \"K4_sc_accuracy\": 0.544,\n      \"K4_delta_pp\": -0.98,\n      \"K8_sica_accuracy\": 0.559,\n      \"K8_sc_accuracy\": 0.539,\n      \"K8_delta_pp\": 1.96,\n      \"K12_sica_accuracy\": 0.593,\n      \"K12_sc_accuracy\": 0.544,\n      \"K12_delta_pp\": 4.9,\n      \"K16_sica_accuracy\": 0.554,\n      \"K16_sc_accuracy\": 0.539,\n      \"K16_delta_pp\": 1.47,\n      \"K20_sica_accuracy\": 0.524,\n      \"K20_sc_accuracy\": 0.549,\n      \"K20_delta_pp\": -2.45,\n      \"inverted_u_visual\": \"无可辨识 pattern，noise ≫ signal\",\n      \"peak_K\": 12,\n      \"peak_delta_pp\": 4.9,\n      \"k4_vs_k12_difference_significant\": false\n    },\n    \"tables\": [\n      \"T5: K sensitivity — Mistral 列 with CI\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"K sensitivity 在 worst tier 下是 paper 的最大损失之一。原本 inverted-U 是 Table 5 / Figure 3 的 hero result，解释了 \\\"why K=12 is optimal\\\"。现在只能说 \\\"K=12 happened to give the best result  in this specific seed, but we cannot distinguish signal from noise\\\"。 Frame 改为 \\\"high variance across K values demonstrates fragility of the effect\\\"—— 从 clean ablation contribution 降级为 fragility evidence。\\n\\n\\nWorst tier 核心假设: K sensitivity 无 inverted-U。K=12 仍然是 peak (因为 exp-033 的 seed 42  就是用 K=12) 但 K=8 和 K=16 的 delta 在 noise band 内 random walk。 K=4 delta≈-1pp, K=8≈+2pp, K=12≈+5pp, K=16≈+1.5pp, K=20≈-2.5pp。 看 curve: 不是 smooth inverted-U 而是 up-down-up-down noise pattern。 K=8→K=12 jump (+3pp) 和 K=12→K=16 drop (-3.4pp) 都可能是 random variation at n=204。 CI bars 大量重叠，无法 reject \\\"all K have same delta\\\" null hypothesis。 Eff-K 也不 monotonically increase with K (因为 κ 本身随 K 变化)。\\n\"\n  },\n  {\n    \"name\": \"multitemp_mistral_folio\",\n    \"description\": \"Multi-temperature (T=0.3/0.7/1.0 混合) Mistral-7B FOLIO-204\",\n    \"results\": {\n      \"sica_accuracy\": 0.564,\n      \"sc_accuracy\": 0.544,\n      \"delta_pp\": 2.45,\n      \"mcnemar_p\": 0.18,\n      \"trace_diversity_increase_pct\": 35,\n      \"effk_multitemp\": 2.8,\n      \"effk_single_t07\": 1.85\n    },\n    \"tables\": [\n      \"T_remediation: multi-temp 行改为 '+2.45pp (n.s.)' 而非 'negative'\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Multi-temp positive 是 worst tier 的 second most damaging result (after K sensitivity noise)。 \\\"9 种修复全部失败\\\" 要改为 \\\"8 种修复失败 + 1 种 promising but underpowered\\\"。 Reviewer 会问: \\\"为什么不 scale up multi-temp to n=600？\\\" — 如果我们没做，是 obvious gap； 如果做了且 positive，paper narrative completely changes。 唯一 defense: argue that +2.45pp n.s. is within noise, and even if real,  Eff-K increase from 1.85→2.8 still far below nominal K=12。\\n\\n\\nWorst tier 核心假设: multi-temp 意外 positive (≥+2pp)。 Multi-temp 通过混合不同温度 traces 确实增加了 diversity (Eff-K 从 1.85 → 2.8)。 Delta=+2.45pp 虽然 n.s. (p=0.18) 但方向 positive。 这动摇 \\\"diversity alone is not sufficient\\\" claim——如果 simple temperature mixing  就能 partially recover SICA effectiveness，那 independence bottleneck 不是 \\\"fundamental\\\"。 Reviewer: \\\"你说 9 种修复全部失败，但 multi-temp 实际上 showed promise？\\\" 无法再 claim \\\"trap is fundamental\\\" 当 diversity intervention shows positive direction。\\n\"\n  },\n  {\n    \"name\": \"mistral_folio204_t03\",\n    \"description\": \"Mistral-7B FOLIO-204 at T=0.3\",\n    \"results\": {\n      \"sica_accuracy\": 0.574,\n      \"sc_accuracy\": 0.534,\n      \"delta_pp\": 3.92,\n      \"mcnemar_p\": 0.065,\n      \"multi_candidate_rate\": 0.55,\n      \"effk_t03\": 1.45\n    },\n    \"tables\": [\n      \"Appendix T sensitivity table: T=0.3 行\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"T=0.3 comparable to T=0.7 是 worst tier 定义的关键指标。 叙事从 \\\"narrow window of fragile effect\\\" 变成 \\\"moderate robustness across low-medium temperatures,  failure only at high T\\\"——这实际上 WEAKENS the pure-negative-results paper framing。 If SICA works at T=0.3-0.7, it's not a \\\"dead end\\\" but a \\\"limited but reproducible effect\\\"。 Reviewer: \\\"这看起来不像 pure negative results，更像 modest positive results with caveats\\\"。 Paper 陷入尴尬中间地带: 不够 positive 做 method paper，不够 negative 做 clean diagnostic paper。\\n\\n\\nWorst tier 核心假设: T=0.3 delta ≥+3pp，与 T=0.7 的 +4.9pp 可比。 T=0.3 SC 略低于 T=0.7 (53.4% vs 54.4%) 但 delta 仍然 substantial (+3.92pp)。 这 destroys \\\"narrow temperature window\\\" narrative。原来的故事是 \\\"SICA only works at T=0.7,  collapses at T=1.0\\\" → 暗示 very specific sweet spot。 现在 T=0.3 (+3.92pp), T=0.7 (+4.90pp), T=1.0 (+0.49pp) → SICA 在 low-to-medium T  都有效，只是 T=1.0 太 noisy 才 collapse。 这个 pattern 不是 \\\"fragile\\\" 而是 \\\"works except at high T\\\"——undermines fragility framing。\\n\"\n  },\n  {\n    \"name\": \"mistral_folio204_t05\",\n    \"description\": \"Mistral-7B FOLIO-204 at T=0.5\",\n    \"results\": {\n      \"sica_accuracy\": 0.564,\n      \"sc_accuracy\": 0.539,\n      \"delta_pp\": 2.45,\n      \"mcnemar_p\": 0.23,\n      \"multi_candidate_rate\": 0.62,\n      \"effk_t05\": 1.65\n    },\n    \"tables\": [\n      \"Appendix T sensitivity table: T=0.5 行\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"T=0.5 填充了 curve 但增加了 noise。4 个 temperature points 无 clean trend  (not inverted-U, not monotonic, not plateau-then-cliff)。 Worst tier 下 T sensitivity section 从 \\\"clean ablation\\\" 降级为 \\\"noisy exploration\\\"。 Only defensible claim: \\\"SICA delta decreases substantially at T=1.0\\\"， but even this is one data point (could reframe as \\\"high temperature degrades constraint extraction\\\"  which is somewhat obvious)。\\n\\n\\nT=0.5 delta=+2.45pp 进一步填充 T sensitivity curve。 Pattern: T=0.3 (+3.92pp) > T=0.5 (+2.45pp) < T=0.7 (+4.90pp) > T=1.0 (+0.49pp)。 不是 monotonic decline 也不是 clean peak——是 noisy 的 non-monotonic pattern。 T=0.5 比 T=0.3 低可能是 random noise at n=204。 Combined with T=0.3 result，T sensitivity curve 是 \\\"generally positive at low-medium T,  negative at high T\\\" 但无 clean functional form。\\n\"\n  },\n  {\n    \"name\": \"effk_sc_joint_prediction\",\n    \"description\": \"Eff-K + SC joint prediction accuracy across all 12+ conditions\",\n    \"results\": {\n      \"total_conditions\": 12,\n      \"correctly_predicted_positive\": 2,\n      \"correctly_predicted_negative\": 4,\n      \"incorrectly_predicted\": 6,\n      \"prediction_accuracy_pct\": 50.0,\n      \"key_failures\": [\n        \"Mistral-PW600: Eff-K=3.63 (highest) predicts positive but delta=-2.83pp\",\n        \"Mistral-s42 vs s123: similar Eff-K+SC but delta differs by 1.47pp\",\n        \"LLaMA-D012: Eff-K unknown but high C0 → predicted positive, actual +6.67pp n.s.\",\n        \"Mistral-s456: Eff-K=2.22 similar to s123 (2.17) but delta reverses sign\"\n      ]\n    },\n    \"tables\": [\n      \"T3: 增加 prediction hit/miss column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Joint prediction ≤50% accuracy 是 worst tier 下 Condorcet framework 的死亡判决。 不能说 \\\"Eff-K predicts SICA effectiveness\\\" 只能说 \\\"Eff-K explains why Qwen family  uniformly fails\\\"。Claim 1 从 \\\"Independence Bottleneck\\\" (predictive) 降为  \\\"Independence Observation\\\" (descriptive)。Condorcet 从 core claim 降入 discussion。\\n\\nWorst tier: Eff-K+SC framework predicts ≤6/12 conditions correctly (≤50%)。 跨模型 direction 正确 (Qwen→0, Mistral→variable) 但 Mistral 内部完全不 work。 Eff-K 与 delta 在 Mistral seeds 内无 monotonic relationship (s42: Eff-K=1.85, delta=+4.9;  s123: Eff-K=2.17, delta=+3.4; s456: Eff-K=2.22, delta=-0.5)——方向甚至相反。 PW-600 (Eff-K=3.63, delta=-2.83) 用 \\\"SC too low\\\" 勉强解释，但 reviewer 会说  这是 post-hoc rationalization。 Framework 降级: \\\"Eff-K is a necessary condition for cross-model comparison  but has no within-model predictive power\\\"——这是一个 much weaker claim。\\n\"\n  }\n]",
      "numLines": 388,
      "startLine": 1,
      "totalLines": 388
    }
  },
  "sourceToolAssistantUUID": "f6f08611-f643-4f9c-ae83-5ceb3bd28b93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T034058 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_co…",
  "leafUuid": "225dc03b-1650-43e9-a186-a3861836b007",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier symbolic consensus paper",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b"
}
```

---

### Assistant

_source line 14 · 2026-05-19T04:28:37.796Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experimental data and the paper framing. Let me now write the paper for the "worst" tier, following the narrative guidance:

- Reframe as "Comprehensive Diagnostic Study of Symbolic Consensus Aggregation"
- Title: "When Do Self-Extracted Symbolic Constraints Help LLM Reasoning? A Diagnostic Study"
- Three pillars: (1) Oracle gap hard result; (2) 9 remediation breadth; (3) C0+SC diagnostic
- Eff-K cross-model direction correct but no within-model predictive power


- K/T curves show mostly noise, and multi-temperature results surprisingly favor diversity despite the narrative I expected
- Reviewer reception likely around 2.5-3.0 on average

I'm planning the paper structure as a diagnostic study rather than a method contribution, starting with abstract and introduction, then related work and the SICA pipeline with diagnostic framework, followed by experiments with the main results table across all models and domains, and the oracle gap analysis.

The analysis sections will cover independence quantification through Eff-K, sensitivity across K and T parameters, remediation attempts, computational overhead, and constraint quality, then move into regime characterization and the C0+SC diagnostic before concluding.

Now I'm compiling the main results table from the experimental data, pulling accuracy numbers for each model-domain pair and calculating the deltas between baseline and SICA performance. Now I'm looking at the Mistral-7B results across different temperature settings, seeing how the performance gains from SICA vary—they're strongest at T=0.7 with a +4.9 improvement and statistical significance, while lower temperatures show smaller gains that don't reach significance. Now I'm looking at the K sensitivity results for Mistral across different parameter values on FOLIO-204, and I can see the constraint ablation showing MaxSAT and count-only variants performing similarly around 76%, with an oracle gap of about 14 percentage points between the gold FOL representation and the current SC baseline. I'm ready to start writing up the paper using a standard article format, structuring the experiments section around the diagnostic findings. I'm working through the experimental data carefully, cross-referencing the K ablation results with the baseline numbers from the framing document to get the exact accuracy figures for each model and domain combination. I'm finishing up the data collection—Qwen-14B shows a 0.25 percentage point improvement on FOLIO/D012 according to the framing documents, which I'll use for consistency. Now I need to write out the full paper with all these results integrated.

Let me check what LaTeX packages are available and just start drafting the paper structure. I'll aim for at least 30 references as required and keep the writing efficient. The core narrative is that SICA doesn't reliably outperform SC across the board—the oracle results show the aggregation mechanism itself works, but self-extraction is where things break down. The C0+SC diagnostic can predict when SICA will fail, and I've tested nine remediation strategies that either didn't help or only showed marginal gains. I need to be transparent about the noisy K sensitivity results and the unexpected positive direction in multi-temperature experiments, since Eff-K doesn't have predictive power within individual models.

Let me organize all the numbers carefully and start writing.

Generating markdown table... Now I'm looking at the oracle control results showing a substantial gap between the gold standard approach and self-consistency, then examining independence metrics across different models and domains to understand how the framing affects performance variability. Now I'm looking at how K and T parameters affect performance across different model configurations, tracking the sensitivity of accuracy improvements as these values change. Now I'm looking at the performance metrics across different constraint and weighting strategies—the Logic-LM variants show vote-based approaches performing around 75%, while the diagnostic data reveals some concerning patterns in constraint quality, with only about 1 in 8 constraints being genuinely informative. The overhead analysis shows trace generation and extraction dominating the computational cost, and the tiebreak strategies vary dramatically in effectiveness, with SICA achieving 80% compared to random's 50%.

Given these results, I need to be candid about what's not working: the sensitivity curves lack clear patterns, the joint prediction accuracy is only at 50%, and most of the positive findings aren't statistically significant. The MaxSAT solver isn't adding meaningful value over simple counting, and the constraint correlations are weak across the board. But I do have two solid legs to build the paper on—the oracle gap result is statistically robust, and I can demonstrate breadth across the nine remediation approaches.

Now I'm planning out the paper structure, starting with the abstract and introduction, then moving through the background, the SICA pipeline methodology, and experimental setup before diving into the results. The core analysis will cover the oracle gap, independence quantification, sensitivity analysis, constraint quality, and the remediation attempts, with the C0+SC diagnostic framework as a key contribution. I'll wrap up with discussion and conclusion, plus appendix tables for additional details.

For references, I need to pull together the key papers on self-consistency and constraint-based approaches, along with foundational work on voting theory and recent related work in the space. I've compiled a solid list of 32+ references covering the key work in this space. Now I'm ready to start writing the actual paper, but I need to be careful about the data—I'll stick to what's directly in the JSON and the framing document rather than making up any numbers. Let me also check if there's an ACL or EMNLP style template I should be using.

For a paper at this tier, a simple article class should be fine—the goal is to be good enough for review, not polished for submission. Now I'm drafting the full paper with a clear structure: testing SICA across 7 models and 6 domains, showing the oracle gap validates the mechanism, identifying self-extraction as the bottleneck through confirmation bias and non-independence issues, demonstrating that most remediation strategies fail with only marginal promise from one approach, positioning C0+SC as a deployment screening diagnostic, and explaining cross-model patterns through Eff-K while acknowledging it doesn't capture within-model variation. This honest framing reorients the narrative away from Condorcet as a core claim and toward a diagnostic study instead.

I need to set up the LaTeX structure with standard packages and macros for SICA and SC, then organize the experimental data into coherent tables. Let me map out which experiments go where: the main results table will cover the scaling studies across different models and domains, and I'll structure the remaining tables to show the oracle gap, self-extraction failures, and remediation attempts. Now I'm mapping out the remaining tables—temperature sensitivity across multiple runs, remediation attempts, constraint ablations, and various comparisons in the appendix. I've got the data sources lined up for constraint quality diagnostics and the joint prediction results. Time to start writing the paper.

For the Qwen-14B FOLIO results, I need to be careful about which numbers to use. The framing data shows SC at 75.49% with a delta of +0.25pp, giving SICA at 75.74%. But I should check the K ablation results to make sure I'm using the right baseline—the mixed dataset D012 behaves differently than pure FOLIO, so I'll keep those separate and note the distinction.

Let me verify the consistency across datasets. Mistral-7B on FOLIO with K=12 shows a delta of +4.90pp with p=0.013, which matches what I see in the sensitivity table. Now I'll structure the paper with the main results table showing Qwen-14B on FOLIO specifically, and then present the K sensitivity analysis separately.

I've got all the replication data I need: across three seeds on FOLIO, the improvements range from -0.49pp to +4.90pp, with two showing statistical significance. The PW-600 dataset shows a different pattern with a negative delta. Now I'm ready to draft the paper, starting with the abstract that frames the core contribution around whether symbolic constraint extraction and SAT-based aggregation can overcome the trace non-independence problem that limits standard self-consistency approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "225dc03b-1650-43e9-a186-a3861836b007",
  "isSidechain": false,
  "requestId": "req_011CbBJ1trwrdpUu3X5krHii",
  "type": "assistant",
  "uuid": "be89dcbe-ec04-4bfc-8ed0-e11d0bf3557e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jM7Fcmi8CEVUfpnBZ8FXC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6384,
      "cache_creation_input_tokens": 10820,
      "cache_read_input_tokens": 24623,
      "output_tokens": 6945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6384,
          "output_tokens": 6945,
          "cache_read_input_tokens": 24623,
          "cache_creation_input_tokens": 10820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10820
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

_source line 15 · 2026-05-19T04:28:37.799Z_

Let me check what LaTeX packages are available, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be89dcbe-ec04-4bfc-8ed0-e11d0bf3557e",
  "isSidechain": false,
  "requestId": "req_011CbBJ1trwrdpUu3X5krHii",
  "type": "assistant",
  "uuid": "f95e8d76-dcf1-49f4-87e2-3d507838bca6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jM7Fcmi8CEVUfpnBZ8FXC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6384,
      "cache_creation_input_tokens": 10820,
      "cache_read_input_tokens": 24623,
      "output_tokens": 6945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6384,
          "output_tokens": 6945,
          "cache_read_input_tokens": 24623,
          "cache_creation_input_tokens": 10820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10820
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

_source line 16 · 2026-05-19T04:28:38.572Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QyU7mq24yUdErQgFfSxxPo`</summary>

```json
{
  "command": "which pdflatex && pdflatex --version | head -3",
  "description": "Check pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f95e8d76-dcf1-49f4-87e2-3d507838bca6",
  "isSidechain": false,
  "requestId": "req_011CbBJ1trwrdpUu3X5krHii",
  "type": "assistant",
  "uuid": "f165261d-5e59-4a52-99bb-ecc2bdb8f7d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jM7Fcmi8CEVUfpnBZ8FXC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6384,
      "cache_creation_input_tokens": 10820,
      "cache_read_input_tokens": 24623,
      "output_tokens": 6945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6384,
          "output_tokens": 6945,
          "cache_read_input_tokens": 24623,
          "cache_creation_input_tokens": 10820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10820
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

_source line 17 · 2026-05-19T04:28:40.896Z_

<details><summary>↩ Tool result · `toolu_013eqofQu3HVYcmZh4qjHkTZ`</summary>

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
  "parentUuid": "6d1932ab-66b9-439c-8e14-1e38c19ec505",
  "isSidechain": false,
  "promptId": "6cd4ba32-185c-4e26-8eaf-fcddb4213dff",
  "type": "user",
  "uuid": "6db86ac5-f50d-4227-8bc0-f047d90946e5",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6d1932ab-66b9-439c-8e14-1e38c19ec505",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T04:28:38.803Z_

<details><summary>↩ Tool result · `toolu_01QyU7mq24yUdErQgFfSxxPo`</summary>

```text
/usr/bin/pdflatex
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)
kpathsea version 6.4.1
Copyright 2025 Han The Thanh (pdfTeX) et al.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f165261d-5e59-4a52-99bb-ecc2bdb8f7d6",
  "isSidechain": false,
  "promptId": "6cd4ba32-185c-4e26-8eaf-fcddb4213dff",
  "type": "user",
  "uuid": "23be1781-67ab-4569-b365-e86845543c8f",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)\nkpathsea version 6.4.1\nCopyright 2025 Han The Thanh (pdfTeX) et al.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f165261d-5e59-4a52-99bb-ecc2bdb8f7d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T04:28:40.797Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013eqofQu3HVYcmZh4qjHkTZ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/",
  "description": "List existing files in target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23be1781-67ab-4569-b365-e86845543c8f",
  "isSidechain": false,
  "requestId": "req_011CbBJ1trwrdpUu3X5krHii",
  "type": "assistant",
  "uuid": "6d1932ab-66b9-439c-8e14-1e38c19ec505",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jM7Fcmi8CEVUfpnBZ8FXC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6384,
      "cache_creation_input_tokens": 10820,
      "cache_read_input_tokens": 24623,
      "output_tokens": 6945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6384,
          "output_tokens": 6945,
          "cache_read_input_tokens": 24623,
          "cache_creation_input_tokens": 10820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10820
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T034058 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_co…",
  "leafUuid": "6db86ac5-f50d-4227-8bc0-f047d90946e5",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier symbolic consensus paper",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b"
}
```

---

### Assistant

_source line 22 · 2026-05-19T04:28:59.403Z_

<details><summary>Logged reasoning block</summary>

```text
Good, pdflatex is available. Let me now write the complete paper. I'll use standard LaTeX packages that should be available in TeX Live 2025.

Let me write the full paper now. This is going to be a substantial document. Let me be methodical about this.

I need to structure the paper carefully. Let me write it section by section.

Key things to remember:
- Worst tier: honest about noisy results, weak predictions
- Three pillars: (1) Oracle gap, (2) 9 remediation breadth, (3) C0+SC diagnostic
- Title: "When Do Self-Extracted Symbolic Constraints Help LLM Reasoning? A Diagnostic Study"


- No em-dashes, no -ing phrase endings, no AI writing style
- All numbers from experiment_data.json
- Comprehensive tables covering all experiments

Now I need to nail down the exact numbers for the main results table. For Qwen-14B on FOLIO, the SC result is 75.49% with a negligible +0.25pp improvement, but I should clarify that the K ablation uses the combined D012 dataset (FOLIO+LogiQA+PW) for the 14B model. Let me pull the FOLIO-specific baseline and build the table from there.

I'm structuring this as two parts: first showing the cross-model comparison on FOLIO with Mistral-7B and Qwen-14B, then the model scaling results on D012 with Qwen-7B and LLaMA-8B to demonstrate how the approach performs across different model sizes.

Then I'm adding domain transfer results for Qwen-14B across GSM8K, StrategyQA, and ARC-Challenge to show generalization, followed by negative controls to establish baseline performance.

Now I'm consolidating all these results into a single comprehensive table for clarity, then moving forward with writing the full paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6db86ac5-f50d-4227-8bc0-f047d90946e5",
  "isSidechain": false,
  "requestId": "req_011CbBJArwrE2dNK6qPZBiij",
  "type": "assistant",
  "uuid": "c25b1774-e24b-49e0-8127-b74539fa71b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q2Q6LGMk6VCSgb93qUdhvS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13456,
      "cache_read_input_tokens": 35443,
      "output_tokens": 14484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14484,
          "cache_read_input_tokens": 35443,
          "cache_creation_input_tokens": 13456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13456
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

_source line 23 · 2026-05-19T04:28:59.422Z_

Writing the full paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c25b1774-e24b-49e0-8127-b74539fa71b0",
  "isSidechain": false,
  "requestId": "req_011CbBJArwrE2dNK6qPZBiij",
  "type": "assistant",
  "uuid": "d9c2fc66-2a90-47ce-b6a8-f407fc801bd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q2Q6LGMk6VCSgb93qUdhvS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13456,
      "cache_read_input_tokens": 35443,
      "output_tokens": 14484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14484,
          "cache_read_input_tokens": 35443,
          "cache_creation_input_tokens": 13456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13456
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

_source line 24 · 2026-05-19T04:33:14.997Z_

<details open><summary>🔧 Tool call — Write · `toolu_01R8dTwLoMEumooWqGcdELfb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{subcaption}\n\\usepackage{array}\n\n\\newcommand{\\sica}{\\textsc{Sica}}\n\\newcommand{\\effk}{\\text{Eff-K}}\n\\newcommand{\\pp}{\\text{pp}}\n\n\\title{When Do Self-Extracted Symbolic Constraints Help LLM Reasoning?\\\\A Diagnostic Study}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nSelf-consistency (SC) improves large language model (LLM) reasoning by sampling multiple chains of thought and taking a majority vote.\nA natural extension is to extract formal constraints from reasoning traces and aggregate them with a MAX-SAT solver, selecting answers that satisfy the most constraints.\nWe conduct a systematic diagnostic study of this approach, which we call Symbolic Invariant Consensus Aggregation (\\sica{}), across 7 models and 6 reasoning domains.\nOur oracle control establishes that MAX-SAT aggregation over gold first-order logic (FOL) annotations yields +14.2 percentage points over SC ($p < 10^{-6}$), confirming that the aggregation mechanism itself is sound.\nHowever, when models extract their own constraints, \\sica{} produces zero or negative gains in 9 of 12 tested conditions.\nThe single reliably positive condition (Mistral-7B on FOLIO, $\\Delta$=+4.9\\pp{}, $p$=0.013) does not generalize across seeds (1 of 3 seeds yields a null result).\nWe characterize three failure regimes, quantify trace non-independence via Fleiss' $\\kappa$ (effective sample sizes of 1.2--3.6 from nominal $K$=12), and show that 9 targeted remediation strategies all fail to close the oracle gap.\nWe propose a zero-cost diagnostic based on the multi-candidate rate (C0) and SC accuracy that identifies conditions where \\sica{} is guaranteed to be ineffective.\n\\end{abstract}\n\n\\section{Introduction}\n\nSelf-consistency \\citep{wang2023selfconsistency} is one of the most widely adopted strategies for improving LLM reasoning at inference time.\nBy sampling $K$ reasoning traces and selecting the most frequent answer via majority vote, SC exploits the observation that correct reasoning paths tend to converge.\nThis approach has been extended to more sophisticated aggregation: extracting formal constraints from traces and using satisfiability solvers to select answers that are maximally consistent with the extracted knowledge \\citep{pan2023logiclm,olausson2023linc}.\n\nThe theoretical foundation for such voting-based aggregation is the Condorcet Jury Theorem \\citep{condorcet1785}, which guarantees that majority voting converges to the correct answer as the number of independent voters grows, provided each voter is correct with probability $p > 0.5$.\nHowever, this guarantee depends critically on voter independence.\nWhen LLM reasoning traces are sampled from the same model, the independence assumption is severely violated: traces share the same parametric knowledge, the same systematic biases, and often converge to the same errors.\n\nIn this work, we ask: \\emph{under what conditions can self-extracted symbolic constraints improve over simple majority voting?}\nWe conduct a comprehensive diagnostic study of Symbolic Invariant Consensus Aggregation (\\sica{}), a pipeline that extracts first-order logic constraints from sampled traces and aggregates them via weighted MAX-SAT solving.\nOur study spans 7 model families (Qwen-7B/14B/72B, Mistral-7B, LLaMA-3.1-8B, DeepSeek-R1-7B, QwQ-32B) across 6 reasoning domains (FOLIO, ProofWriter, LogiQA, StrategyQA, GSM8K, ARC-Challenge).\n\nOur contributions are:\n\\begin{enumerate}\n\\item \\textbf{Oracle gap localization.} Gold FOL constraints with MAX-SAT yield +14.2\\pp{} over SC ($p < 10^{-6}$), proving the aggregation mechanism is sound. Self-extracted constraints capture only 35\\% of this theoretical potential, localizing the bottleneck to extraction quality.\n\\item \\textbf{Systematic failure characterization.} We identify three failure regimes (high-accuracy confirmation bias, low-accuracy noise, domain non-formalizability) and document that \\sica{} yields zero or negative gains in 9 of 12 conditions. The single positive condition is fragile across seeds and hyperparameters.\n\\item \\textbf{Remediation breadth.} Nine targeted interventions spanning prompting, architecture, capability, verification, diversity, and filtering all fail to close the oracle gap, suggesting that the self-extraction bottleneck is structural.\n\\item \\textbf{Deployment diagnostic.} The multi-candidate rate (C0) combined with SC accuracy provides a zero-cost screening tool: C0 $< 5\\%$ guarantees \\sica{} $\\equiv$ SC, eliminating unnecessary computation in the majority of deployment scenarios.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Self-Consistency and Extensions.}\nWang et al.~\\citeyearpar{wang2023selfconsistency} introduced SC for chain-of-thought reasoning.\nSubsequent work has explored universal SC \\citep{chen2023usc}, diversity-aware sampling \\citep{li2023diverse}, weighted voting \\citep{taubenfeld2025weighted}, and scaling analysis of SC \\citep{loo2025sc}.\nThese approaches share the fundamental assumption that sampling diverse traces provides complementary information, an assumption we directly test.\n\n\\paragraph{Neuro-Symbolic Reasoning.}\nSeveral systems combine LLM reasoning with formal logic.\nLogic-LM \\citep{pan2023logiclm} translates problems to symbolic form and uses solvers for inference.\nLINC \\citep{olausson2023linc} performs neurosymbolic reasoning via in-context learning.\nMore recent work includes DyLoS \\citep{dylos2026}, which trains dedicated extractors, Aristotle \\citep{aristotle2025}, which uses structured reasoning with external verifiers, and FoVer \\citep{fover2025}, which performs formal verification of LLM outputs.\nOur work differs from these in studying \\emph{self-extraction} without trained extractors or external verifiers.\n\n\\paragraph{Condorcet Jury Theorem and LLM Ensembles.}\nThe connection between CJT and LLM voting has been explored by \\citet{li2024independence}, who study independence violations in cross-model sentiment analysis ensembles.\nOur work applies CJT analysis to \\emph{within-model} trace sampling, quantifying independence via Fleiss' $\\kappa$ \\citep{fleiss1971} and introducing the effective sample size metric $\\effk{}$.\n\n\\paragraph{Test-Time Compute and Verification.}\nScaling inference-time computation through repeated sampling \\citep{snell2025scaling}, process reward models \\citep{lightman2023prm}, outcome reward models \\citep{cobbe2021orm}, and extended reasoning \\citep{deepseekr1} represent alternatives to symbolic aggregation.\nOur oracle gap analysis clarifies when symbolic approaches have theoretical headroom over these alternatives.\n\n\\section{Method: \\sica{} Pipeline}\n\n\\subsection{Overview}\n\nGiven a reasoning problem $q$ and an LLM $\\mathcal{M}$, \\sica{} proceeds in three stages:\n\n\\paragraph{Stage 1: Trace Sampling.}\nSample $K$ reasoning traces $\\{t_1, \\ldots, t_K\\}$ from $\\mathcal{M}$ at temperature $T$, each producing a candidate answer $a_i$.\n\n\\paragraph{Stage 2: Constraint Extraction.}\nFor each trace $t_i$, prompt $\\mathcal{M}$ to extract first-order logic (FOL) constraints $\\{c_{i,1}, \\ldots, c_{i,m_i}\\}$ that formalize the reasoning steps. Each constraint is a FOL formula over the candidate answer set.\n\n\\paragraph{Stage 3: MAX-SAT Aggregation.}\nEncode each constraint as a weighted clause in a MAX-SAT instance. For each candidate answer $a$, compute the total weight of satisfied constraints. Select the answer maximizing total satisfied weight:\n\\begin{equation}\na^* = \\arg\\max_{a \\in \\mathcal{A}} \\sum_{i=1}^{K} \\sum_{j=1}^{m_i} w_{i,j} \\cdot \\mathbf{1}[c_{i,j} \\text{ satisfied by } a]\n\\end{equation}\n\n\\subsection{Independence Quantification}\n\nWe measure trace agreement using Fleiss' $\\kappa$ \\citep{fleiss1971} computed over the $K$ traces' answer distributions per problem. The effective number of independent voters is:\n\\begin{equation}\n\\effk{} = \\frac{K}{1 + (K-1)\\kappa}\n\\end{equation}\nwhere $\\kappa$ is the average pairwise agreement. When $\\kappa = 0$ (full independence), $\\effk{} = K$. When $\\kappa = 1$ (perfect agreement), $\\effk{} = 1$.\n\n\\subsection{Diagnostic Metrics}\n\n\\paragraph{Multi-Candidate Rate (C0).}\nThe fraction of problems where at least two distinct candidate answers appear across $K$ traces. Problems with C0 = 0 (unanimous agreement) are trivially identical under SC and \\sica{}.\n\n\\paragraph{Oracle Control.}\nTo separate extraction quality from aggregation quality, we replace self-extracted constraints with gold-standard FOL annotations and measure the resulting MAX-SAT accuracy.\n\n\\section{Experimental Setup}\n\n\\paragraph{Models.}\nWe evaluate 7 models spanning 5 families: Qwen2.5-7B, Qwen2.5-14B, Qwen2.5-72B-AWQ (4-bit), LLaMA-3.1-8B, Mistral-7B-Instruct-v0.3, DeepSeek-R1-Distill-Qwen-7B, and QwQ-32B.\n\n\\paragraph{Datasets.}\nFOLIO \\citep{han2022folio} (natural language FOL inference, 204 problems), ProofWriter \\citep{tafjord2021proofwriter} (synthetic deductive reasoning), LogiQA \\citep{liu2023logiqa} (logical comprehension), StrategyQA \\citep{geva2021strategyqa} (multi-hop commonsense, 60 problems), ARC-Challenge \\citep{clark2018arc} (science QA, 60 problems), and GSM8K \\citep{cobbe2021gsm8k} (math word problems, 30 problems). D012 denotes the combined FOLIO+LogiQA+ProofWriter subset (60 problems).\n\n\\paragraph{Configuration.}\nDefault: $K$=12, $T$=0.7, seed 42. Sensitivity analyses vary $K \\in \\{4, 6, 8, 11, 12, 16, 20\\}$ and $T \\in \\{0.3, 0.5, 0.7, 1.0\\}$. Statistical significance is assessed via McNemar's test.\n\n\\section{Results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents \\sica{} versus SC across all model-domain conditions.\nOf 12 primary conditions, only one (Mistral-7B on FOLIO-204) yields a statistically significant positive result ($\\Delta$=+4.9\\pp{}, $p$=0.013).\nThree conditions show positive but non-significant trends (LLaMA-8B on D012, +6.7\\pp{}, $p$=0.219; Qwen-14B on StrategyQA, +3.3\\pp{}, $p > 0.1$; QwQ-32B on AIME, $\\Delta$=0.0).\nThe remaining conditions show zero or negative deltas.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results: SC vs.\\ \\sica{} across models and domains. $n$: number of problems. C0: multi-candidate rate. $\\Delta$: SICA $-$ SC in percentage points. Bold: statistically significant ($p < 0.05$).}\n\\label{tab:main}\n\\small\n\\begin{tabular}{llrrrrrr}\n\\toprule\nModel & Domain & $n$ & SC\\% & \\sica{}\\% & $\\Delta$\\pp{} & $p$ & C0 \\\\\n\\midrule\nMistral-7B & FOLIO-204 & 204 & 54.4 & 59.3 & \\textbf{+4.90} & \\textbf{0.013} & 0.69 \\\\\nQwen2.5-14B & FOLIO & 204 & 75.5 & 75.7 & +0.25 & n.s. & 0.38 \\\\\nQwen2.5-7B & D012 & 60 & 68.3 & 68.3 & 0.00 & 1.000 & 0.43 \\\\\nQwen2.5-72B & D012 & 60 & 83.3 & 81.7 & $-$1.67 & 0.625 & 0.20 \\\\\nLLaMA-3.1-8B & D012 & 60 & 60.0 & 66.7 & +6.67 & 0.219 & 0.62 \\\\\nDeepSeek-R1-7B & D012 & 60 & 71.7 & 68.3 & $-$3.33 & 0.480 & 0.58 \\\\\nQwQ-32B & AIME & 29 & --- & --- & 0.00 & n.s. & 0.03 \\\\\nQwQ-32B & PW & 17 & --- & --- & $-$5.90 & n.s. & 0.03 \\\\\n\\midrule\nQwen2.5-14B & StrategyQA & 60 & 53.3 & 56.7 & +3.33 & n.s. & 0.10 \\\\\nQwen2.5-14B & ARC-Chall. & 60 & 96.7 & 95.0 & $-$1.67 & --- & 0.05 \\\\\nQwen2.5-14B & GSM8K & 30 & 96.7 & 96.7 & 0.00 & --- & 0.13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeveral patterns emerge.\nThe Qwen model family shows zero or negative gains at all scales (7B, 14B, 72B), consistent with high baseline accuracy and low C0 values.\nLLaMA-8B shows a positive trend (+6.7\\pp{}) on D012 ($n$=60), but this result has $p$=0.219 and is accompanied by 44 truncated traces (of 60 problems) and an answer extraction rate of only 89.6\\%, raising concerns about pipeline artifacts.\nQwQ-32B, a reasoning-specialized model, has C0 $< 5\\%$ across both domains (aggregate C0 effective = 2.6\\%), confirming that near-deterministic trace generation renders \\sica{} equivalent to SC.\nGSM8K exhibits a domain mismatch: FOL extraction succeeds on only 14.7\\% of traces, as mathematical reasoning requires numerical constraints rather than propositional logic.\n\n\\subsection{Oracle Gap Analysis}\n\nTable~\\ref{tab:oracle} presents the oracle control experiment on Qwen2.5-14B FOLIO.\nGold FOL annotations with MAX-SAT aggregation yield 89.7\\% accuracy, a +14.2\\pp{} improvement over SC ($p = 2.0 \\times 10^{-7}$).\nSelf-extracted \\sica{} achieves only +0.25\\pp{}, capturing approximately 2\\% of the oracle potential.\nEven in the best self-extraction condition (Mistral-7B FOLIO, +4.9\\pp{}), the utilization rate is only 35\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{Oracle control on Qwen2.5-14B FOLIO ($n$=204). Gold FOL: human-annotated first-order logic constraints. Self: model-extracted constraints.}\n\\label{tab:oracle}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\nMethod & Accuracy\\% & $\\Delta$ vs.\\ SC & $p$-value \\\\\n\\midrule\nSC (majority vote) & 75.5 & --- & --- \\\\\n\\sica{} (self-extracted) & 75.7 & +0.25\\pp{} & n.s. \\\\\n\\sica{} (gold FOL) & 89.7 & +14.22\\pp{} & $2.0 \\times 10^{-7}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis result has two implications.\nFirst, the MAX-SAT aggregation mechanism is not the bottleneck; when given high-quality constraints, it substantially outperforms majority voting.\nSecond, the gap between oracle and self-extraction performance localizes the failure to constraint quality.\nA two-layer analysis reveals the mechanism: 43\\% of self-extracted constraints are trivially satisfied by all candidate answers (providing no discriminative signal), and 78\\% of constraints mirror the model's own answer (confirmation bias).\n\n\\subsection{Independence Quantification}\n\nTable~\\ref{tab:independence} reports Fleiss' $\\kappa$ and $\\effk{}$ across model-domain conditions.\nFor $K$=12 nominal traces, the effective number of independent voters ranges from 1.20 (Qwen-14B LogiQA) to 3.63 (Mistral-7B ProofWriter-600).\n\n\\begin{table}[t]\n\\centering\n\\caption{Trace independence metrics. $\\kappa$: Fleiss' kappa. $\\effk{}$: effective independent voters for $K$=12. SC: self-consistency accuracy. $\\Delta$: \\sica{}$-$SC.}\n\\label{tab:independence}\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\nModel & Domain (seed) & $\\kappa$ & $\\effk{}$ & SC\\% & $\\Delta$\\pp{} \\\\\n\\midrule\nQwen-14B & FOLIO & 0.744 & 1.31 & 75.5 & +0.25 \\\\\nQwen-14B & LogiQA & 0.821 & 1.20 & 78.5 & +0.50 \\\\\nMistral-7B & FOLIO (s42) & 0.500 & 1.85 & 54.4 & +4.90 \\\\\nMistral-7B & FOLIO (s123) & 0.412 & 2.17 & 54.4 & +3.43 \\\\\nMistral-7B & FOLIO (s456) & 0.401 & 2.22 & 54.4 & $-$0.49 \\\\\nMistral-7B & PW-600 & 0.210 & 3.63 & 39.3 & $-$2.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA cross-model pattern is clear: Qwen-14B ($\\effk{} \\approx 1.2$--$1.3$) consistently shows zero gain, while Mistral-7B ($\\effk{} \\approx 1.9$--$2.2$ on FOLIO) shows variable gains.\nHowever, $\\effk{}$ has no within-model predictive power.\nAmong the three Mistral-7B FOLIO seeds, seed 42 has the \\emph{lowest} $\\effk{}$ (1.85) yet the highest $\\Delta$ (+4.9\\pp{}), while seed 456 has higher $\\effk{}$ (2.22) but negative $\\Delta$ ($-$0.49\\pp{}).\nMistral-7B on ProofWriter-600 has the highest $\\effk{}$ of all conditions (3.63) yet produces a significant \\emph{negative} $\\Delta$ ($-$2.83\\pp{}, $p$=0.010), because SC accuracy (39.3\\%) falls below the quality threshold.\n\nTo quantify this predictive failure, we evaluated joint $\\effk{}$+SC prediction across all 12 conditions (Table~\\ref{tab:prediction}).\nThe framework correctly predicts the sign of $\\Delta$ in only 6 of 12 conditions (50\\%), equivalent to chance.\nKey failures include Mistral-7B PW-600 (highest $\\effk{}$, predicted positive, actual $-$2.83\\pp{}) and within-seed reversals where similar $\\effk{}$+SC values produce opposite-sign deltas.\n\n\\begin{table}[t]\n\\centering\n\\caption{Joint $\\effk{}$+SC prediction accuracy across 12 conditions. The framework predicts the sign of $\\Delta$ at chance level (50\\%).}\n\\label{tab:prediction}\n\\small\n\\begin{tabular}{lrr}\n\\toprule\nPrediction outcome & Count & Fraction \\\\\n\\midrule\nCorrectly predicted positive & 2 & 16.7\\% \\\\\nCorrectly predicted negative/zero & 4 & 33.3\\% \\\\\nIncorrectly predicted & 6 & 50.0\\% \\\\\n\\midrule\nTotal & 12 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{K Sensitivity}\n\nWe vary $K$ for both Mistral-7B (FOLIO-204) and Qwen2.5-14B (D012, 60 problems). Results appear in Table~\\ref{tab:ksens}.\n\n\\begin{table}[t]\n\\centering\n\\caption{$K$ sensitivity. Left: Mistral-7B on FOLIO-204 (seed 42). Right: Qwen2.5-14B on D012 (60 problems). None of the pairwise differences are statistically significant.}\n\\label{tab:ksens}\n\\small\n\\begin{tabular}{crrrcrr}\n\\toprule\n& \\multicolumn{3}{c}{Mistral-7B / FOLIO-204} & & \\multicolumn{2}{c}{Qwen-14B / D012} \\\\\n\\cmidrule{2-4} \\cmidrule{6-7}\n$K$ & SC\\% & \\sica{}\\% & $\\Delta$\\pp{} & & $K$ & $\\Delta$\\pp{} \\\\\n\\midrule\n4 & 54.4 & 53.4 & $-$0.98 & & 6 & 0.0 \\\\\n8 & 53.9 & 55.9 & +1.96 & & 8 & $-$1.7 \\\\\n12 & 54.4 & 59.3 & +4.90 & & 11 & 0.0 \\\\\n16 & 53.9 & 55.4 & +1.47 & & 12 & $-$5.0 \\\\\n20 & 54.9 & 52.4 & $-$2.45 & & 16 & $-$3.3 \\\\\n & & & & & 20 & $-$3.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor Mistral-7B, $K$=12 produces the largest $\\Delta$ (+4.9\\pp{}), but the pattern across $K$ values does not follow a smooth trend.\nThe sequence ($-$1.0, +2.0, +4.9, +1.5, $-$2.5) is consistent with random fluctuation at $n$=204; confidence intervals overlap substantially, and we cannot reject the null hypothesis that all $K$ values produce the same $\\Delta$.\nFor Qwen-14B, all $K$ values yield zero or negative $\\Delta$, with monotonic degradation at $K \\geq 12$, consistent with redundant correlated constraints accumulating noise.\n\n\\subsection{Temperature Sensitivity}\n\nTable~\\ref{tab:tsens} reports \\sica{} performance at four temperature values and a multi-temperature mixing condition for Mistral-7B on FOLIO-204.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temperature sensitivity for Mistral-7B on FOLIO-204 ($K$=12). Multi-temp mixes equal numbers of traces at $T$=0.3, 0.7, and 1.0. $\\effk{}$ computed from Fleiss' $\\kappa$ at each temperature.}\n\\label{tab:tsens}\n\\small\n\\begin{tabular}{lrrrrl}\n\\toprule\n$T$ & SC\\% & \\sica{}\\% & $\\Delta$\\pp{} & $\\effk{}$ & $p$-value \\\\\n\\midrule\n0.3 & 53.4 & 57.4 & +3.92 & 1.45 & 0.065 \\\\\n0.5 & 53.9 & 56.4 & +2.45 & 1.65 & 0.230 \\\\\n0.7 & 54.4 & 59.3 & +4.90 & 1.85 & 0.013 \\\\\n1.0 & --- & --- & +0.49 & --- & 0.739 \\\\\n\\midrule\nMulti & 54.4 & 56.4 & +2.45 & 2.80 & 0.180 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\sica{} shows positive $\\Delta$ at $T$=0.3 through $T$=0.7, with only $T$=1.0 collapsing to near zero.\nThis pattern complicates a simple fragility narrative: the effect is not confined to a narrow temperature window but persists across low-to-medium temperatures, although none of the individual conditions except $T$=0.7 reach significance.\nThe non-monotonic pattern across temperatures ($T$=0.3: +3.9, $T$=0.5: +2.5, $T$=0.7: +4.9, $T$=1.0: +0.5) lacks a clean functional form.\n\nThe multi-temperature condition is informative.\nMixing traces across temperatures increases $\\effk{}$ from 1.85 (single $T$=0.7) to 2.80, a 51\\% improvement in effective independence.\nThe resulting $\\Delta$ of +2.45\\pp{} ($p$=0.18), while non-significant, is positive, and this is the only remediation strategy that increases both diversity \\emph{and} shows a positive trend.\nThis result weakens a blanket claim that diversity interventions cannot help, though the evidence remains underpowered.\n\n\\subsection{Constraint Quality Analysis}\n\n\\paragraph{Qualitative analysis.}\nWe analyze constraint quality on 8 representative problems.\nOf these, 45\\% contain only trivially satisfied constraints (satisfied by all candidate answers), 6 of 8 exhibit confirmation bias (constraints mirror the model's own answer), and only 1 of 8 contains a genuinely informative constraint.\nOverall, 78\\% of extracted constraints agree with the model's majority-vote answer, indicating that the extraction process largely recapitulates the model's existing beliefs rather than introducing independent evidence.\n\n\\paragraph{Quantitative correlation.}\nAcross 10 model-domain conditions, the correlation between constraint precision and $\\Delta$ is $r$=0.28 ($p$=0.43, $n$=10), far from significant.\nSimilarly, C0 alone correlates with $\\Delta$ at $r$=0.31 ($p$=0.33, $n$=12), and correctly predicts the direction of $\\Delta$ in only 5 of 12 conditions (41.7\\%).\nHigh C0 is associated with both positive deltas (LLaMA-8B D012: C0=0.62, $\\Delta$=+6.7\\pp{}) and negative deltas (DeepSeek-R1 D012: C0=0.58, $\\Delta$=$-$3.3\\pp{}), indicating that answer diversity is necessary but not sufficient for \\sica{} effectiveness.\n\n\\paragraph{Aggregation mechanism ablation.}\nTo test whether MAX-SAT solving contributes beyond simple constraint counting, we compare three aggregation strategies on 804 problems from the primary dataset (Table~\\ref{tab:ablation}).\nMAX-SAT and count-only agree on 803 of 804 problems.\nNo method significantly outperforms the SC baseline.\nThis result indicates that the symbolic optimization machinery (weighted MAX-SAT) provides negligible value over simple constraint counting, because constraint satisfaction scores are nearly uniform across candidates (mean satisfaction ratio $\\approx$ 0.96).\n\n\\begin{table}[t]\n\\centering\n\\caption{Aggregation mechanism ablation ($n$=804). Agreement: fraction of problems where method and count-only produce the same answer.}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lrr}\n\\toprule\nMethod & Accuracy\\% & Agreement w/ count-only \\\\\n\\midrule\nSC (majority vote) & 76.2 & --- \\\\\nMAX-SAT (weighted) & 76.5 & --- \\\\\nCount-only & 76.6 & 803/804 \\\\\nRandom-weight & 75.9 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Seed Replication}\n\nThe primary positive result (Mistral-7B FOLIO-204, $K$=12, $T$=0.7) was replicated across three random seeds.\nTwo of three seeds yield significant positive results: seed 42 ($\\Delta$=+4.90\\pp{}, $p$=0.013) and seed 123 ($\\Delta$=+3.43\\pp{}, $p$=0.039).\nSeed 456 produces a null result ($\\Delta$=$-$0.49\\pp{}, n.s.).\nThe effect is real but fragile: even under identical hyperparameters and the same model-domain combination, random seed variation can eliminate or reverse the gain.\n\n\\subsection{Remediation Attempts}\n\nTable~\\ref{tab:remediation} summarizes 9 remediation strategies targeting different hypothesized bottlenecks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Nine remediation strategies and their outcomes. All were applied to Mistral-7B FOLIO. ``Outcome'' indicates the effect on $\\Delta$ relative to the base condition.}\n\\label{tab:remediation}\n\\small\n\\begin{tabular}{p{3.5cm}p{3cm}p{4.5cm}}\n\\toprule\nStrategy & Target & Outcome \\\\\n\\midrule\nContrastive prompting & Extraction quality & No improvement \\\\\nCross-model extraction & Independence & No improvement \\\\\nGenerational scaling & Model capability & No improvement \\\\\nSolver-guided refinement & Constraint consistency & No improvement \\\\\nConsistency filtering & Noise reduction & No improvement \\\\\nCross-trace UNSAT & Contradiction detection & No improvement \\\\\nDiscriminative filtering & Non-informative removal & 0 gains (92\\% already discriminative) \\\\\n$T$=1.0 diversity & Trace diversity & $\\Delta$ collapses: +4.9 $\\to$ +0.5\\pp{} \\\\\nMulti-temperature & Structured diversity & +2.45\\pp{} (n.s., $p$=0.18) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEight of nine strategies produce no improvement or degradation.\nThe single partial exception is multi-temperature mixing, which increases $\\effk{}$ from 1.85 to 2.80 and yields $\\Delta$=+2.45\\pp{}, positive but non-significant.\nThis result suggests that structured diversity interventions may have marginal value, but the effect size is smaller than the single-temperature optimum (+4.9\\pp{} at $T$=0.7) and not statistically reliable.\nNotably, simply increasing temperature to $T$=1.0 collapses $\\Delta$ from +4.9 to +0.5\\pp{}, demonstrating that unstructured diversity is harmful.\n\nThe discriminative filtering result is particularly informative: 92\\% of constraints are already discriminative (they assign different scores to different candidates), yet removing the 8\\% non-discriminative constraints produces zero improvement.\nThe problem is not that constraints lack discriminative power, but that their discriminative direction aligns with the model's existing biases.\n\n\\subsection{Additional Baselines}\n\n\\paragraph{Weighted SC.}\nWe test three weighting schemes for SC: inverse-length, length-weighted, and constraint-count weighted (Table~\\ref{tab:weightedsc}).\nNo scheme significantly outperforms uniform SC, consistent with the thesis that re-weighting correlated votes does not address the underlying independence problem.\n\n\\begin{table}[t]\n\\centering\n\\caption{Weighted SC variants on the primary dataset ($n$=804). All differences are non-significant.}\n\\label{tab:weightedsc}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nWeighting & Accuracy\\% \\\\\n\\midrule\nUniform (SC) & 76.2 \\\\\nInverse-length & 76.7 \\\\\nLength-weighted & 75.3 \\\\\nConstraint-count & 75.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Logic-LM baseline.}\nWe compare against a Logic-LM-style approach that performs single-trace FOL verification across $K$ traces and takes a majority vote.\nOn FOLIO, this achieves 75.5\\% (vs.\\ SC 75.0\\%, \\sica{} 74.5\\%).\nAll three methods are statistically indistinguishable, suggesting that multi-trace constraint aggregation provides no advantage over per-trace symbolic verification when traces are highly correlated.\n\n\\subsection{Deployment Diagnostic: C0 + SC}\n\nWe propose a two-dimensional diagnostic for screening \\sica{} applicability before deployment.\n\n\\paragraph{C0 screening.}\nWhen C0 $< 5\\%$, \\sica{} is mathematically equivalent to SC (no multi-candidate problems exist for MAX-SAT to resolve).\nThis condition holds for QwQ-32B (C0 = 2.6\\%), ARC-Challenge (C0 = 5\\%), and near-threshold for GSM8K (C0 = 13.3\\%, but with 14.7\\% extraction success).\nC0 screening eliminates approximately half of model-domain conditions from consideration at zero computational cost.\n\n\\paragraph{SC accuracy regime.}\nAmong conditions where C0 is sufficient, SC accuracy further stratifies outcomes:\n\\begin{itemize}\n\\item SC $> 75\\%$ (Type A): Confirmation bias dominates. Constraints mirror correct answers, providing no additional signal. Examples: Qwen-14B FOLIO (75.5\\%), Qwen-72B D012 (83.3\\%).\n\\item SC $< 40\\%$ (Type C): Trace quality is insufficient. Constraints encode mostly incorrect reasoning, degrading performance. Example: Mistral-7B PW-600 (39.3\\%, $\\Delta$=$-$2.83\\pp{}).\n\\item SC $\\approx$ 50--55\\% with high C0 (candidate zone): The only observed positive results fall here. Example: Mistral-7B FOLIO (54.4\\%, C0=0.69, $\\Delta$=+4.9\\pp{}).\n\\end{itemize}\n\nHowever, we emphasize that this diagnostic has limited positive predictive power.\nWhile C0 $< 5\\%$ reliably predicts $\\Delta \\approx 0$ (necessary condition), high C0 combined with moderate SC does not guarantee positive $\\Delta$ (the prediction accuracy is 41.7\\% across all conditions).\nThe diagnostic is useful for ruling out \\sica{}, not for recommending it.\n\n\\subsection{Overhead Analysis}\n\n\\sica{} approximately doubles wall-clock time per problem: mean total time is 61.6 seconds, with trace generation consuming 51.3\\% and constraint extraction consuming 47.0\\%.\nMAX-SAT solving accounts for less than 0.01\\% of total time.\nGiven that $\\Delta \\leq 0$ in the majority of conditions, the cost-benefit ratio is unfavorable for general deployment.\nThe overhead analysis does suggest that future work should focus on extraction quality rather than solver efficiency, as the computational bottleneck and the quality bottleneck coincide in the extraction stage.\n\n\\section{Discussion}\n\n\\paragraph{The self-extraction trap.}\nOur results paint a consistent picture: the MAX-SAT aggregation mechanism is effective when given high-quality constraints (oracle gap: +14.2\\pp{}), but self-extraction from the same model that generated the reasoning traces produces constraints that largely recapitulate the model's existing beliefs.\nThis is not a simple quality problem (92\\% of constraints are discriminative) but a directionality problem: constraints discriminate in the same direction as the model's majority vote, providing no orthogonal signal.\n\n\\paragraph{Limitations of the independence framework.}\nWhile Fleiss' $\\kappa$ and $\\effk{}$ provide a useful descriptive vocabulary (explaining why Qwen-family models uniformly show zero gain), the framework has no predictive power within a model family.\nThe 50\\% joint prediction accuracy across 12 conditions is equivalent to random guessing.\nWe therefore present $\\effk{}$ as a diagnostic tool for cross-model comparison, not as a predictive framework.\n\n\\paragraph{Multi-temperature as a promising direction.}\nThe multi-temperature result ($\\Delta$=+2.45\\pp{}, $\\effk{}$ increase from 1.85 to 2.80) is the only remediation showing a positive trend.\nWhile underpowered in our study ($p$=0.18), this suggests that structured diversity interventions deserve further investigation, particularly at larger sample sizes.\nThis partially qualifies our ``9/9 failed'' framing: 8 strategies clearly failed, and 1 showed marginal promise.\n\n\\paragraph{Limitations.}\nOur primary positive result comes from a single model-domain-temperature combination (Mistral-7B, FOLIO, $T$=0.7).\nSample sizes for pilot domains (StrategyQA, ARC, GSM8K) are small ($n$=30--60), limiting statistical power.\nThe LLaMA-8B result (+6.7\\pp{}) may be confounded by high trace truncation rates (73\\%).\nWe do not evaluate trained extractors or external verifiers, which represent a different paradigm from the self-extraction setting we study.\n\n\\section{Conclusion}\n\nWe present a diagnostic study of symbolic consensus aggregation across 7 models and 6 domains.\nThree findings stand out.\nFirst, the oracle gap (+14.2\\pp{}) proves that constraint-based aggregation is a viable mechanism when constraints are reliable, localizing the current failure to extraction quality.\nSecond, nine remediation strategies fail to close this gap, with only multi-temperature mixing showing marginal promise, suggesting that the self-extraction bottleneck is largely structural.\nThird, the C0+SC diagnostic provides a practical screening tool that can eliminate unnecessary \\sica{} computation in the majority of deployment scenarios, despite its limited positive predictive power.\nThe central lesson is that same-model self-extraction produces constraints that mirror rather than complement the model's reasoning, a fundamental limitation that simple diversity or filtering interventions cannot overcome.\n\n\\bibliography{references}\n\\bibliographystyle{plainnat}\n\n\\appendix\n\n\\section{Tiebreak Analysis}\n\\label{app:tiebreak}\n\nWhen SC produces a tie (equal votes for two answers), \\sica{} can break the tie using constraint satisfaction scores. On $n$=5 tiebreak problems, \\sica{} achieves 80\\% accuracy compared to 50\\% for random tiebreak, 60\\% for alphabetical, and 40\\% for first-seen ordering. The sample size is too small for statistical inference.\n\n\\section{QwQ-32B Negative Control}\n\\label{app:qwq}\n\nQwQ-32B, a reasoning-specialized model, produces near-deterministic traces with aggregate C0 effective of 2.6\\%. On AIME ($n$=29), $\\Delta$=0.0\\pp{}. On ProofWriter ($n$=17), $\\Delta$=$-$5.9\\pp{} (non-significant given the small sample). This confirms that reasoning models with low trace diversity gain nothing from symbolic aggregation.\n\n\\section{Full Overhead Breakdown}\n\\label{app:overhead}\n\n\\begin{table}[h]\n\\centering\n\\caption{Wall-time breakdown per problem (mean over all conditions).}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nStage & \\% of total time \\\\\n\\midrule\nTrace generation & 51.3\\% \\\\\nConstraint extraction & 47.0\\% \\\\\nMAX-SAT solving & $<$0.01\\% \\\\\nOther & 1.7\\% \\\\\n\\midrule\nTotal (mean) & 61.6 seconds \\\\\n\\sica{} overhead vs.\\ SC-only & +48.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{thebibliography}{40}\n\n\\bibitem[Wang et al.(2023)]{wang2023selfconsistency}\nWang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., and Zhou, D.\n\\newblock Self-consistency improves chain of thought reasoning in language models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Pan et al.(2023)]{pan2023logiclm}\nPan, L., Alber, M., Chen, W., Gashteovski, K., Xie, Y., Feng, Z., and Lawrence, C.\n\\newblock Logic-LM: Empowering large language models with symbolic solvers for faithful logical reasoning.\n\\newblock In \\emph{Findings of EMNLP}, 2023.\n\n\\bibitem[Olausson et al.(2023)]{olausson2023linc}\nOlausson, T.~X., Gu, A., Lipkin, B., Zhang, C.~E., Solar-Lezama, A., Tenenbaum, J.~B., and Levy, R.\n\\newblock LINC: A neurosymbolic approach for logical reasoning by combining language models with first-order logic provers.\n\\newblock In \\emph{EMNLP}, 2023.\n\n\\bibitem[Condorcet(1785)]{condorcet1785}\nde Condorcet, M.~J.~A.~N.\n\\newblock \\emph{Essai sur l'application de l'analyse \\`{a} la probabilit\\'{e} des d\\'{e}cisions rendues \\`{a} la pluralit\\'{e} des voix}.\n\\newblock 1785.\n\n\\bibitem[Austen-Smith and Banks(1996)]{austensmith1996}\nAusten-Smith, D. and Banks, J.~S.\n\\newblock Information aggregation, rationality, and the {C}ondorcet jury theorem.\n\\newblock \\emph{American Political Science Review}, 90(1):34--45, 1996.\n\n\\bibitem[Li et al.(2024)]{li2024independence}\nLi, Z., et al.\n\\newblock Examining independence in ensemble sentiment classification: A {C}ondorcet jury theorem perspective.\n\\newblock \\emph{arXiv:2409.00094}, 2024.\n\n\\bibitem[Fleiss(1971)]{fleiss1971}\nFleiss, J.~L.\n\\newblock Measuring nominal scale agreement among many raters.\n\\newblock \\emph{Psychological Bulletin}, 76(5):378--382, 1971.\n\n\\bibitem[Chen et al.(2023)]{chen2023usc}\nChen, X., Aksitov, R., Alon, U., Ren, J., Xiao, K., Yin, P., Prakash, S., Sutton, C., Wang, X., and Zhou, D.\n\\newblock Universal self-consistency for large language model generation.\n\\newblock \\emph{arXiv:2311.17311}, 2023.\n\n\\bibitem[Li et al.(2023)]{li2023diverse}\nLi, Y., Lin, Z., Zhang, S., Fu, Q., Chen, B., Lou, J.-G., and Chen, W.\n\\newblock Making language models better reasoners with step-aware verifier.\n\\newblock In \\emph{ACL}, 2023.\n\n\\bibitem[Taubenfeld et al.(2025)]{taubenfeld2025weighted}\nTaubenfeld, A., et al.\n\\newblock Weighted self-consistency for language model reasoning.\n\\newblock 2025.\n\n\\bibitem[Loo et al.(2025)]{loo2025sc}\nLoo, N., et al.\n\\newblock On the scaling limits of self-consistency.\n\\newblock 2025.\n\n\\bibitem[{DyLoS}(2026)]{dylos2026}\n{DyLoS Authors}.\n\\newblock {DyLoS}: Dynamic logic solving with language models.\n\\newblock In \\emph{EACL}, 2026.\n\n\\bibitem[{Aristotle}(2025)]{aristotle2025}\n{Aristotle Authors}.\n\\newblock Aristotle: Structured reasoning with external verification.\n\\newblock In \\emph{ACL}, 2025.\n\n\\bibitem[{FoVer}(2025)]{fover2025}\n{FoVer Authors}.\n\\newblock {FoVer}: Formal verification of large language model outputs.\n\\newblock \\emph{TACL}, 2025.\n\n\\bibitem[Snell et al.(2025)]{snell2025scaling}\nSnell, C., et al.\n\\newblock Scaling {LLM} test-time compute.\n\\newblock 2025.\n\n\\bibitem[{DeepSeek-AI}(2025)]{deepseekr1}\n{DeepSeek-AI}.\n\\newblock {DeepSeek-R1}: Incentivizing reasoning capability in {LLMs} via reinforcement learning.\n\\newblock \\emph{arXiv:2501.12948}, 2025.\n\n\\bibitem[Cobbe et al.(2021)]{cobbe2021orm}\nCobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., Hesse, C., and Schulman, J.\n\\newblock Training verifiers to solve math word problems.\n\\newblock \\emph{arXiv:2110.14168}, 2021.\n\n\\bibitem[Cobbe et al.(2021b)]{cobbe2021gsm8k}\nCobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., Hesse, C., and Schulman, J.\n\\newblock Training verifiers to solve math word problems.\n\\newblock \\emph{arXiv:2110.14168}, 2021.\n\n\\bibitem[Lightman et al.(2023)]{lightman2023prm}\nLightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I., and Alignment, K.\n\\newblock Let's verify step by step.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Liang et al.(2023)]{liang2023debate}\nLiang, T., He, Z., Jiao, W., Wang, X., Wang, Y., Wang, R., Yang, Y., Tu, Z., and Shi, S.\n\\newblock Encouraging divergent thinking in large language models through multi-agent debate.\n\\newblock \\emph{arXiv:2305.19118}, 2023.\n\n\\bibitem[Du et al.(2023)]{du2023debate}\nDu, Y., Li, S., Torralba, A., Tenenbaum, J.~B., and Mordatch, I.\n\\newblock Improving factuality and reasoning in language models through multiagent debate.\n\\newblock \\emph{arXiv:2305.14325}, 2023.\n\n\\bibitem[Wei et al.(2022)]{wei2022cot}\nWei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., and Zhou, D.\n\\newblock Chain-of-thought prompting elicits reasoning in large language models.\n\\newblock In \\emph{NeurIPS}, 2022.\n\n\\bibitem[Kojima et al.(2022)]{kojima2022zerocot}\nKojima, T., Gu, S.~S., Reid, M., Matsuo, Y., and Iwasawa, Y.\n\\newblock Large language models are zero-shot reasoners.\n\\newblock In \\emph{NeurIPS}, 2022.\n\n\\bibitem[Han et al.(2022)]{han2022folio}\nHan, S., Schoelkopf, H., Zhao, Y., Qi, Z., Riddell, M., Benson, L., Sun, L., Zubova, E., Qiao, Y., Burtell, M., et al.\n\\newblock {FOLIO}: Natural language reasoning with first-order logic.\n\\newblock \\emph{arXiv:2209.00840}, 2022.\n\n\\bibitem[Tafjord et al.(2021)]{tafjord2021proofwriter}\nTafjord, O., Dalvi, B., and Clark, P.\n\\newblock {ProofWriter}: Generating implications, proofs, and abductive statements over natural language.\n\\newblock In \\emph{Findings of ACL}, 2021.\n\n\\bibitem[Clark et al.(2018)]{clark2018arc}\nClark, P., Cowhey, I., Etzioni, O., Khot, T., Sabharwal, A., Schoenick, C., and Tafjord, O.\n\\newblock Think you have solved question answering? {T}ry {ARC}, the {AI2} reasoning challenge.\n\\newblock \\emph{arXiv:1803.05457}, 2018.\n\n\\bibitem[Geva et al.(2021)]{geva2021strategyqa}\nGeva, M., Khashabi, D., Segal, E., Khot, T., Roth, D., and Berant, J.\n\\newblock Did {A}ristotle use a laptop? {A} question answering benchmark with implicit reasoning strategies.\n\\newblock \\emph{TACL}, 2021.\n\n\\bibitem[Liu et al.(2023)]{liu2023logiqa}\nLiu, J., et al.\n\\newblock {LogiQA} 2.0: An improved dataset for logical reasoning.\n\\newblock \\emph{IEEE/ACM Transactions on Audio, Speech, and Language Processing}, 2023.\n\n\\bibitem[Jiang et al.(2023)]{jiang2023mistral}\nJiang, A.~Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D.~S., de~las Casas, D., Bressand, F., Lengyel, G., Lample, G., et al.\n\\newblock Mistral 7{B}.\n\\newblock \\emph{arXiv:2310.06825}, 2023.\n\n\\bibitem[{Qwen Team}(2024)]{qwen2024}\n{Qwen Team}.\n\\newblock Qwen2.5 technical report.\n\\newblock 2024.\n\n\\bibitem[Touvron et al.(2023)]{touvron2023llama}\nTouvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., et al.\n\\newblock {LLaMA} 2: Open foundation and fine-tuned chat models.\n\\newblock \\emph{arXiv:2307.09288}, 2023.\n\n\\bibitem[{SATBench}(2025)]{satbench2025}\n{SATBench Authors}.\n\\newblock {SATBench}: Benchmarking constraint satisfaction with language models.\n\\newblock In \\emph{EMNLP}, 2025.\n\n\\bibitem[{LLM-CP}(2025)]{llmcp2025}\n{LLM-CP Authors}.\n\\newblock {LLM} meets constraint propagation.\n\\newblock In \\emph{IJCAI}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9c2fc66-2a90-47ce-b6a8-f407fc801bd9",
  "isSidechain": false,
  "requestId": "req_011CbBJArwrE2dNK6qPZBiij",
  "type": "assistant",
  "uuid": "e92fa37d-abeb-43fe-9148-a519fedb9507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q2Q6LGMk6VCSgb93qUdhvS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13456,
      "cache_read_input_tokens": 35443,
      "output_tokens": 14484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14484,
          "cache_read_input_tokens": 35443,
          "cache_creation_input_tokens": 13456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13456
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

_source line 25 · 2026-05-19T04:33:15.023Z_

<details><summary>↩ Tool result · `toolu_01R8dTwLoMEumooWqGcdELfb`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e92fa37d-abeb-43fe-9148-a519fedb9507",
  "isSidechain": false,
  "promptId": "6cd4ba32-185c-4e26-8eaf-fcddb4213dff",
  "type": "user",
  "uuid": "c7d3ff51-d92d-4e7d-9935-c9841b577714",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{subcaption}\n\\usepackage{array}\n\n\\newcommand{\\sica}{\\textsc{Sica}}\n\\newcommand{\\effk}{\\text{Eff-K}}\n\\newcommand{\\pp}{\\text{pp}}\n\n\\title{When Do Self-Extracted Symbolic Constraints Help LLM Reasoning?\\\\A Diagnostic Study}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nSelf-consistency (SC) improves large language model (LLM) reasoning by sampling multiple chains of thought and taking a majority vote.\nA natural extension is to extract formal constraints from reasoning traces and aggregate them with a MAX-SAT solver, selecting answers that satisfy the most constraints.\nWe conduct a systematic diagnostic study of this approach, which we call Symbolic Invariant Consensus Aggregation (\\sica{}), across 7 models and 6 reasoning domains.\nOur oracle control establishes that MAX-SAT aggregation over gold first-order logic (FOL) annotations yields +14.2 percentage points over SC ($p < 10^{-6}$), confirming that the aggregation mechanism itself is sound.\nHowever, when models extract their own constraints, \\sica{} produces zero or negative gains in 9 of 12 tested conditions.\nThe single reliably positive condition (Mistral-7B on FOLIO, $\\Delta$=+4.9\\pp{}, $p$=0.013) does not generalize across seeds (1 of 3 seeds yields a null result).\nWe characterize three failure regimes, quantify trace non-independence via Fleiss' $\\kappa$ (effective sample sizes of 1.2--3.6 from nominal $K$=12), and show that 9 targeted remediation strategies all fail to close the oracle gap.\nWe propose a zero-cost diagnostic based on the multi-candidate rate (C0) and SC accuracy that identifies conditions where \\sica{} is guaranteed to be ineffective.\n\\end{abstract}\n\n\\section{Introduction}\n\nSelf-consistency \\citep{wang2023selfconsistency} is one of the most widely adopted strategies for improving LLM reasoning at inference time.\nBy sampling $K$ reasoning traces and selecting the most frequent answer via majority vote, SC exploits the observation that correct reasoning paths tend to converge.\nThis approach has been extended to more sophisticated aggregation: extracting formal constraints from traces and using satisfiability solvers to select answers that are maximally consistent with the extracted knowledge \\citep{pan2023logiclm,olausson2023linc}.\n\nThe theoretical foundation for such voting-based aggregation is the Condorcet Jury Theorem \\citep{condorcet1785}, which guarantees that majority voting converges to the correct answer as the number of independent voters grows, provided each voter is correct with probability $p > 0.5$.\nHowever, this guarantee depends critically on voter independence.\nWhen LLM reasoning traces are sampled from the same model, the independence assumption is severely violated: traces share the same parametric knowledge, the same systematic biases, and often converge to the same errors.\n\nIn this work, we ask: \\emph{under what conditions can self-extracted symbolic constraints improve over simple majority voting?}\nWe conduct a comprehensive diagnostic study of Symbolic Invariant Consensus Aggregation (\\sica{}), a pipeline that extracts first-order logic constraints from sampled traces and aggregates them via weighted MAX-SAT solving.\nOur study spans 7 model families (Qwen-7B/14B/72B, Mistral-7B, LLaMA-3.1-8B, DeepSeek-R1-7B, QwQ-32B) across 6 reasoning domains (FOLIO, ProofWriter, LogiQA, StrategyQA, GSM8K, ARC-Challenge).\n\nOur contributions are:\n\\begin{enumerate}\n\\item \\textbf{Oracle gap localization.} Gold FOL constraints with MAX-SAT yield +14.2\\pp{} over SC ($p < 10^{-6}$), proving the aggregation mechanism is sound. Self-extracted constraints capture only 35\\% of this theoretical potential, localizing the bottleneck to extraction quality.\n\\item \\textbf{Systematic failure characterization.} We identify three failure regimes (high-accuracy confirmation bias, low-accuracy noise, domain non-formalizability) and document that \\sica{} yields zero or negative gains in 9 of 12 conditions. The single positive condition is fragile across seeds and hyperparameters.\n\\item \\textbf{Remediation breadth.} Nine targeted interventions spanning prompting, architecture, capability, verification, diversity, and filtering all fail to close the oracle gap, suggesting that the self-extraction bottleneck is structural.\n\\item \\textbf{Deployment diagnostic.} The multi-candidate rate (C0) combined with SC accuracy provides a zero-cost screening tool: C0 $< 5\\%$ guarantees \\sica{} $\\equiv$ SC, eliminating unnecessary computation in the majority of deployment scenarios.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Self-Consistency and Extensions.}\nWang et al.~\\citeyearpar{wang2023selfconsistency} introduced SC for chain-of-thought reasoning.\nSubsequent work has explored universal SC \\citep{chen2023usc}, diversity-aware sampling \\citep{li2023diverse}, weighted voting \\citep{taubenfeld2025weighted}, and scaling analysis of SC \\citep{loo2025sc}.\nThese approaches share the fundamental assumption that sampling diverse traces provides complementary information, an assumption we directly test.\n\n\\paragraph{Neuro-Symbolic Reasoning.}\nSeveral systems combine LLM reasoning with formal logic.\nLogic-LM \\citep{pan2023logiclm} translates problems to symbolic form and uses solvers for inference.\nLINC \\citep{olausson2023linc} performs neurosymbolic reasoning via in-context learning.\nMore recent work includes DyLoS \\citep{dylos2026}, which trains dedicated extractors, Aristotle \\citep{aristotle2025}, which uses structured reasoning with external verifiers, and FoVer \\citep{fover2025}, which performs formal verification of LLM outputs.\nOur work differs from these in studying \\emph{self-extraction} without trained extractors or external verifiers.\n\n\\paragraph{Condorcet Jury Theorem and LLM Ensembles.}\nThe connection between CJT and LLM voting has been explored by \\citet{li2024independence}, who study independence violations in cross-model sentiment analysis ensembles.\nOur work applies CJT analysis to \\emph{within-model} trace sampling, quantifying independence via Fleiss' $\\kappa$ \\citep{fleiss1971} and introducing the effective sample size metric $\\effk{}$.\n\n\\paragraph{Test-Time Compute and Verification.}\nScaling inference-time computation through repeated sampling \\citep{snell2025scaling}, process reward models \\citep{lightman2023prm}, outcome reward models \\citep{cobbe2021orm}, and extended reasoning \\citep{deepseekr1} represent alternatives to symbolic aggregation.\nOur oracle gap analysis clarifies when symbolic approaches have theoretical headroom over these alternatives.\n\n\\section{Method: \\sica{} Pipeline}\n\n\\subsection{Overview}\n\nGiven a reasoning problem $q$ and an LLM $\\mathcal{M}$, \\sica{} proceeds in three stages:\n\n\\paragraph{Stage 1: Trace Sampling.}\nSample $K$ reasoning traces $\\{t_1, \\ldots, t_K\\}$ from $\\mathcal{M}$ at temperature $T$, each producing a candidate answer $a_i$.\n\n\\paragraph{Stage 2: Constraint Extraction.}\nFor each trace $t_i$, prompt $\\mathcal{M}$ to extract first-order logic (FOL) constraints $\\{c_{i,1}, \\ldots, c_{i,m_i}\\}$ that formalize the reasoning steps. Each constraint is a FOL formula over the candidate answer set.\n\n\\paragraph{Stage 3: MAX-SAT Aggregation.}\nEncode each constraint as a weighted clause in a MAX-SAT instance. For each candidate answer $a$, compute the total weight of satisfied constraints. Select the answer maximizing total satisfied weight:\n\\begin{equation}\na^* = \\arg\\max_{a \\in \\mathcal{A}} \\sum_{i=1}^{K} \\sum_{j=1}^{m_i} w_{i,j} \\cdot \\mathbf{1}[c_{i,j} \\text{ satisfied by } a]\n\\end{equation}\n\n\\subsection{Independence Quantification}\n\nWe measure trace agreement using Fleiss' $\\kappa$ \\citep{fleiss1971} computed over the $K$ traces' answer distributions per problem. The effective number of independent voters is:\n\\begin{equation}\n\\effk{} = \\frac{K}{1 + (K-1)\\kappa}\n\\end{equation}\nwhere $\\kappa$ is the average pairwise agreement. When $\\kappa = 0$ (full independence), $\\effk{} = K$. When $\\kappa = 1$ (perfect agreement), $\\effk{} = 1$.\n\n\\subsection{Diagnostic Metrics}\n\n\\paragraph{Multi-Candidate Rate (C0).}\nThe fraction of problems where at least two distinct candidate answers appear across $K$ traces. Problems with C0 = 0 (unanimous agreement) are trivially identical under SC and \\sica{}.\n\n\\paragraph{Oracle Control.}\nTo separate extraction quality from aggregation quality, we replace self-extracted constraints with gold-standard FOL annotations and measure the resulting MAX-SAT accuracy.\n\n\\section{Experimental Setup}\n\n\\paragraph{Models.}\nWe evaluate 7 models spanning 5 families: Qwen2.5-7B, Qwen2.5-14B, Qwen2.5-72B-AWQ (4-bit), LLaMA-3.1-8B, Mistral-7B-Instruct-v0.3, DeepSeek-R1-Distill-Qwen-7B, and QwQ-32B.\n\n\\paragraph{Datasets.}\nFOLIO \\citep{han2022folio} (natural language FOL inference, 204 problems), ProofWriter \\citep{tafjord2021proofwriter} (synthetic deductive reasoning), LogiQA \\citep{liu2023logiqa} (logical comprehension), StrategyQA \\citep{geva2021strategyqa} (multi-hop commonsense, 60 problems), ARC-Challenge \\citep{clark2018arc} (science QA, 60 problems), and GSM8K \\citep{cobbe2021gsm8k} (math word problems, 30 problems). D012 denotes the combined FOLIO+LogiQA+ProofWriter subset (60 problems).\n\n\\paragraph{Configuration.}\nDefault: $K$=12, $T$=0.7, seed 42. Sensitivity analyses vary $K \\in \\{4, 6, 8, 11, 12, 16, 20\\}$ and $T \\in \\{0.3, 0.5, 0.7, 1.0\\}$. Statistical significance is assessed via McNemar's test.\n\n\\section{Results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents \\sica{} versus SC across all model-domain conditions.\nOf 12 primary conditions, only one (Mistral-7B on FOLIO-204) yields a statistically significant positive result ($\\Delta$=+4.9\\pp{}, $p$=0.013).\nThree conditions show positive but non-significant trends (LLaMA-8B on D012, +6.7\\pp{}, $p$=0.219; Qwen-14B on StrategyQA, +3.3\\pp{}, $p > 0.1$; QwQ-32B on AIME, $\\Delta$=0.0).\nThe remaining conditions show zero or negative deltas.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results: SC vs.\\ \\sica{} across models and domains. $n$: number of problems. C0: multi-candidate rate. $\\Delta$: SICA $-$ SC in percentage points. Bold: statistically significant ($p < 0.05$).}\n\\label{tab:main}\n\\small\n\\begin{tabular}{llrrrrrr}\n\\toprule\nModel & Domain & $n$ & SC\\% & \\sica{}\\% & $\\Delta$\\pp{} & $p$ & C0 \\\\\n\\midrule\nMistral-7B & FOLIO-204 & 204 & 54.4 & 59.3 & \\textbf{+4.90} & \\textbf{0.013} & 0.69 \\\\\nQwen2.5-14B & FOLIO & 204 & 75.5 & 75.7 & +0.25 & n.s. & 0.38 \\\\\nQwen2.5-7B & D012 & 60 & 68.3 & 68.3 & 0.00 & 1.000 & 0.43 \\\\\nQwen2.5-72B & D012 & 60 & 83.3 & 81.7 & $-$1.67 & 0.625 & 0.20 \\\\\nLLaMA-3.1-8B & D012 & 60 & 60.0 & 66.7 & +6.67 & 0.219 & 0.62 \\\\\nDeepSeek-R1-7B & D012 & 60 & 71.7 & 68.3 & $-$3.33 & 0.480 & 0.58 \\\\\nQwQ-32B & AIME & 29 & --- & --- & 0.00 & n.s. & 0.03 \\\\\nQwQ-32B & PW & 17 & --- & --- & $-$5.90 & n.s. & 0.03 \\\\\n\\midrule\nQwen2.5-14B & StrategyQA & 60 & 53.3 & 56.7 & +3.33 & n.s. & 0.10 \\\\\nQwen2.5-14B & ARC-Chall. & 60 & 96.7 & 95.0 & $-$1.67 & --- & 0.05 \\\\\nQwen2.5-14B & GSM8K & 30 & 96.7 & 96.7 & 0.00 & --- & 0.13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeveral patterns emerge.\nThe Qwen model family shows zero or negative gains at all scales (7B, 14B, 72B), consistent with high baseline accuracy and low C0 values.\nLLaMA-8B shows a positive trend (+6.7\\pp{}) on D012 ($n$=60), but this result has $p$=0.219 and is accompanied by 44 truncated traces (of 60 problems) and an answer extraction rate of only 89.6\\%, raising concerns about pipeline artifacts.\nQwQ-32B, a reasoning-specialized model, has C0 $< 5\\%$ across both domains (aggregate C0 effective = 2.6\\%), confirming that near-deterministic trace generation renders \\sica{} equivalent to SC.\nGSM8K exhibits a domain mismatch: FOL extraction succeeds on only 14.7\\% of traces, as mathematical reasoning requires numerical constraints rather than propositional logic.\n\n\\subsection{Oracle Gap Analysis}\n\nTable~\\ref{tab:oracle} presents the oracle control experiment on Qwen2.5-14B FOLIO.\nGold FOL annotations with MAX-SAT aggregation yield 89.7\\% accuracy, a +14.2\\pp{} improvement over SC ($p = 2.0 \\times 10^{-7}$).\nSelf-extracted \\sica{} achieves only +0.25\\pp{}, capturing approximately 2\\% of the oracle potential.\nEven in the best self-extraction condition (Mistral-7B FOLIO, +4.9\\pp{}), the utilization rate is only 35\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{Oracle control on Qwen2.5-14B FOLIO ($n$=204). Gold FOL: human-annotated first-order logic constraints. Self: model-extracted constraints.}\n\\label{tab:oracle}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\nMethod & Accuracy\\% & $\\Delta$ vs.\\ SC & $p$-value \\\\\n\\midrule\nSC (majority vote) & 75.5 & --- & --- \\\\\n\\sica{} (self-extracted) & 75.7 & +0.25\\pp{} & n.s. \\\\\n\\sica{} (gold FOL) & 89.7 & +14.22\\pp{} & $2.0 \\times 10^{-7}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis result has two implications.\nFirst, the MAX-SAT aggregation mechanism is not the bottleneck; when given high-quality constraints, it substantially outperforms majority voting.\nSecond, the gap between oracle and self-extraction performance localizes the failure to constraint quality.\nA two-layer analysis reveals the mechanism: 43\\% of self-extracted constraints are trivially satisfied by all candidate answers (providing no discriminative signal), and 78\\% of constraints mirror the model's own answer (confirmation bias).\n\n\\subsection{Independence Quantification}\n\nTable~\\ref{tab:independence} reports Fleiss' $\\kappa$ and $\\effk{}$ across model-domain conditions.\nFor $K$=12 nominal traces, the effective number of independent voters ranges from 1.20 (Qwen-14B LogiQA) to 3.63 (Mistral-7B ProofWriter-600).\n\n\\begin{table}[t]\n\\centering\n\\caption{Trace independence metrics. $\\kappa$: Fleiss' kappa. $\\effk{}$: effective independent voters for $K$=12. SC: self-consistency accuracy. $\\Delta$: \\sica{}$-$SC.}\n\\label{tab:independence}\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\nModel & Domain (seed) & $\\kappa$ & $\\effk{}$ & SC\\% & $\\Delta$\\pp{} \\\\\n\\midrule\nQwen-14B & FOLIO & 0.744 & 1.31 & 75.5 & +0.25 \\\\\nQwen-14B & LogiQA & 0.821 & 1.20 & 78.5 & +0.50 \\\\\nMistral-7B & FOLIO (s42) & 0.500 & 1.85 & 54.4 & +4.90 \\\\\nMistral-7B & FOLIO (s123) & 0.412 & 2.17 & 54.4 & +3.43 \\\\\nMistral-7B & FOLIO (s456) & 0.401 & 2.22 & 54.4 & $-$0.49 \\\\\nMistral-7B & PW-600 & 0.210 & 3.63 & 39.3 & $-$2.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA cross-model pattern is clear: Qwen-14B ($\\effk{} \\approx 1.2$--$1.3$) consistently shows zero gain, while Mistral-7B ($\\effk{} \\approx 1.9$--$2.2$ on FOLIO) shows variable gains.\nHowever, $\\effk{}$ has no within-model predictive power.\nAmong the three Mistral-7B FOLIO seeds, seed 42 has the \\emph{lowest} $\\effk{}$ (1.85) yet the highest $\\Delta$ (+4.9\\pp{}), while seed 456 has higher $\\effk{}$ (2.22) but negative $\\Delta$ ($-$0.49\\pp{}).\nMistral-7B on ProofWriter-600 has the highest $\\effk{}$ of all conditions (3.63) yet produces a significant \\emph{negative} $\\Delta$ ($-$2.83\\pp{}, $p$=0.010), because SC accuracy (39.3\\%) falls below the quality threshold.\n\nTo quantify this predictive failure, we evaluated joint $\\effk{}$+SC prediction across all 12 conditions (Table~\\ref{tab:prediction}).\nThe framework correctly predicts the sign of $\\Delta$ in only 6 of 12 conditions (50\\%), equivalent to chance.\nKey failures include Mistral-7B PW-600 (highest $\\effk{}$, predicted positive, actual $-$2.83\\pp{}) and within-seed reversals where similar $\\effk{}$+SC values produce opposite-sign deltas.\n\n\\begin{table}[t]\n\\centering\n\\caption{Joint $\\effk{}$+SC prediction accuracy across 12 conditions. The framework predicts the sign of $\\Delta$ at chance level (50\\%).}\n\\label{tab:prediction}\n\\small\n\\begin{tabular}{lrr}\n\\toprule\nPrediction outcome & Count & Fraction \\\\\n\\midrule\nCorrectly predicted positive & 2 & 16.7\\% \\\\\nCorrectly predicted negative/zero & 4 & 33.3\\% \\\\\nIncorrectly predicted & 6 & 50.0\\% \\\\\n\\midrule\nTotal & 12 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{K Sensitivity}\n\nWe vary $K$ for both Mistral-7B (FOLIO-204) and Qwen2.5-14B (D012, 60 problems). Results appear in Table~\\ref{tab:ksens}.\n\n\\begin{table}[t]\n\\centering\n\\caption{$K$ sensitivity. Left: Mistral-7B on FOLIO-204 (seed 42). Right: Qwen2.5-14B on D012 (60 problems). None of the pairwise differences are statistically significant.}\n\\label{tab:ksens}\n\\small\n\\begin{tabular}{crrrcrr}\n\\toprule\n& \\multicolumn{3}{c}{Mistral-7B / FOLIO-204} & & \\multicolumn{2}{c}{Qwen-14B / D012} \\\\\n\\cmidrule{2-4} \\cmidrule{6-7}\n$K$ & SC\\% & \\sica{}\\% & $\\Delta$\\pp{} & & $K$ & $\\Delta$\\pp{} \\\\\n\\midrule\n4 & 54.4 & 53.4 & $-$0.98 & & 6 & 0.0 \\\\\n8 & 53.9 & 55.9 & +1.96 & & 8 & $-$1.7 \\\\\n12 & 54.4 & 59.3 & +4.90 & & 11 & 0.0 \\\\\n16 & 53.9 & 55.4 & +1.47 & & 12 & $-$5.0 \\\\\n20 & 54.9 & 52.4 & $-$2.45 & & 16 & $-$3.3 \\\\\n & & & & & 20 & $-$3.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor Mistral-7B, $K$=12 produces the largest $\\Delta$ (+4.9\\pp{}), but the pattern across $K$ values does not follow a smooth trend.\nThe sequence ($-$1.0, +2.0, +4.9, +1.5, $-$2.5) is consistent with random fluctuation at $n$=204; confidence intervals overlap substantially, and we cannot reject the null hypothesis that all $K$ values produce the same $\\Delta$.\nFor Qwen-14B, all $K$ values yield zero or negative $\\Delta$, with monotonic degradation at $K \\geq 12$, consistent with redundant correlated constraints accumulating noise.\n\n\\subsection{Temperature Sensitivity}\n\nTable~\\ref{tab:tsens} reports \\sica{} performance at four temperature values and a multi-temperature mixing condition for Mistral-7B on FOLIO-204.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temperature sensitivity for Mistral-7B on FOLIO-204 ($K$=12). Multi-temp mixes equal numbers of traces at $T$=0.3, 0.7, and 1.0. $\\effk{}$ computed from Fleiss' $\\kappa$ at each temperature.}\n\\label{tab:tsens}\n\\small\n\\begin{tabular}{lrrrrl}\n\\toprule\n$T$ & SC\\% & \\sica{}\\% & $\\Delta$\\pp{} & $\\effk{}$ & $p$-value \\\\\n\\midrule\n0.3 & 53.4 & 57.4 & +3.92 & 1.45 & 0.065 \\\\\n0.5 & 53.9 & 56.4 & +2.45 & 1.65 & 0.230 \\\\\n0.7 & 54.4 & 59.3 & +4.90 & 1.85 & 0.013 \\\\\n1.0 & --- & --- & +0.49 & --- & 0.739 \\\\\n\\midrule\nMulti & 54.4 & 56.4 & +2.45 & 2.80 & 0.180 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\sica{} shows positive $\\Delta$ at $T$=0.3 through $T$=0.7, with only $T$=1.0 collapsing to near zero.\nThis pattern complicates a simple fragility narrative: the effect is not confined to a narrow temperature window but persists across low-to-medium temperatures, although none of the individual conditions except $T$=0.7 reach significance.\nThe non-monotonic pattern across temperatures ($T$=0.3: +3.9, $T$=0.5: +2.5, $T$=0.7: +4.9, $T$=1.0: +0.5) lacks a clean functional form.\n\nThe multi-temperature condition is informative.\nMixing traces across temperatures increases $\\effk{}$ from 1.85 (single $T$=0.7) to 2.80, a 51\\% improvement in effective independence.\nThe resulting $\\Delta$ of +2.45\\pp{} ($p$=0.18), while non-significant, is positive, and this is the only remediation strategy that increases both diversity \\emph{and} shows a positive trend.\nThis result weakens a blanket claim that diversity interventions cannot help, though the evidence remains underpowered.\n\n\\subsection{Constraint Quality Analysis}\n\n\\paragraph{Qualitative analysis.}\nWe analyze constraint quality on 8 representative problems.\nOf these, 45\\% contain only trivially satisfied constraints (satisfied by all candidate answers), 6 of 8 exhibit confirmation bias (constraints mirror the model's own answer), and only 1 of 8 contains a genuinely informative constraint.\nOverall, 78\\% of extracted constraints agree with the model's majority-vote answer, indicating that the extraction process largely recapitulates the model's existing beliefs rather than introducing independent evidence.\n\n\\paragraph{Quantitative correlation.}\nAcross 10 model-domain conditions, the correlation between constraint precision and $\\Delta$ is $r$=0.28 ($p$=0.43, $n$=10), far from significant.\nSimilarly, C0 alone correlates with $\\Delta$ at $r$=0.31 ($p$=0.33, $n$=12), and correctly predicts the direction of $\\Delta$ in only 5 of 12 conditions (41.7\\%).\nHigh C0 is associated with both positive deltas (LLaMA-8B D012: C0=0.62, $\\Delta$=+6.7\\pp{}) and negative deltas (DeepSeek-R1 D012: C0=0.58, $\\Delta$=$-$3.3\\pp{}), indicating that answer diversity is necessary but not sufficient for \\sica{} effectiveness.\n\n\\paragraph{Aggregation mechanism ablation.}\nTo test whether MAX-SAT solving contributes beyond simple constraint counting, we compare three aggregation strategies on 804 problems from the primary dataset (Table~\\ref{tab:ablation}).\nMAX-SAT and count-only agree on 803 of 804 problems.\nNo method significantly outperforms the SC baseline.\nThis result indicates that the symbolic optimization machinery (weighted MAX-SAT) provides negligible value over simple constraint counting, because constraint satisfaction scores are nearly uniform across candidates (mean satisfaction ratio $\\approx$ 0.96).\n\n\\begin{table}[t]\n\\centering\n\\caption{Aggregation mechanism ablation ($n$=804). Agreement: fraction of problems where method and count-only produce the same answer.}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lrr}\n\\toprule\nMethod & Accuracy\\% & Agreement w/ count-only \\\\\n\\midrule\nSC (majority vote) & 76.2 & --- \\\\\nMAX-SAT (weighted) & 76.5 & --- \\\\\nCount-only & 76.6 & 803/804 \\\\\nRandom-weight & 75.9 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Seed Replication}\n\nThe primary positive result (Mistral-7B FOLIO-204, $K$=12, $T$=0.7) was replicated across three random seeds.\nTwo of three seeds yield significant positive results: seed 42 ($\\Delta$=+4.90\\pp{}, $p$=0.013) and seed 123 ($\\Delta$=+3.43\\pp{}, $p$=0.039).\nSeed 456 produces a null result ($\\Delta$=$-$0.49\\pp{}, n.s.).\nThe effect is real but fragile: even under identical hyperparameters and the same model-domain combination, random seed variation can eliminate or reverse the gain.\n\n\\subsection{Remediation Attempts}\n\nTable~\\ref{tab:remediation} summarizes 9 remediation strategies targeting different hypothesized bottlenecks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Nine remediation strategies and their outcomes. All were applied to Mistral-7B FOLIO. ``Outcome'' indicates the effect on $\\Delta$ relative to the base condition.}\n\\label{tab:remediation}\n\\small\n\\begin{tabular}{p{3.5cm}p{3cm}p{4.5cm}}\n\\toprule\nStrategy & Target & Outcome \\\\\n\\midrule\nContrastive prompting & Extraction quality & No improvement \\\\\nCross-model extraction & Independence & No improvement \\\\\nGenerational scaling & Model capability & No improvement \\\\\nSolver-guided refinement & Constraint consistency & No improvement \\\\\nConsistency filtering & Noise reduction & No improvement \\\\\nCross-trace UNSAT & Contradiction detection & No improvement \\\\\nDiscriminative filtering & Non-informative removal & 0 gains (92\\% already discriminative) \\\\\n$T$=1.0 diversity & Trace diversity & $\\Delta$ collapses: +4.9 $\\to$ +0.5\\pp{} \\\\\nMulti-temperature & Structured diversity & +2.45\\pp{} (n.s., $p$=0.18) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEight of nine strategies produce no improvement or degradation.\nThe single partial exception is multi-temperature mixing, which increases $\\effk{}$ from 1.85 to 2.80 and yields $\\Delta$=+2.45\\pp{}, positive but non-significant.\nThis result suggests that structured diversity interventions may have marginal value, but the effect size is smaller than the single-temperature optimum (+4.9\\pp{} at $T$=0.7) and not statistically reliable.\nNotably, simply increasing temperature to $T$=1.0 collapses $\\Delta$ from +4.9 to +0.5\\pp{}, demonstrating that unstructured diversity is harmful.\n\nThe discriminative filtering result is particularly informative: 92\\% of constraints are already discriminative (they assign different scores to different candidates), yet removing the 8\\% non-discriminative constraints produces zero improvement.\nThe problem is not that constraints lack discriminative power, but that their discriminative direction aligns with the model's existing biases.\n\n\\subsection{Additional Baselines}\n\n\\paragraph{Weighted SC.}\nWe test three weighting schemes for SC: inverse-length, length-weighted, and constraint-count weighted (Table~\\ref{tab:weightedsc}).\nNo scheme significantly outperforms uniform SC, consistent with the thesis that re-weighting correlated votes does not address the underlying independence problem.\n\n\\begin{table}[t]\n\\centering\n\\caption{Weighted SC variants on the primary dataset ($n$=804). All differences are non-significant.}\n\\label{tab:weightedsc}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nWeighting & Accuracy\\% \\\\\n\\midrule\nUniform (SC) & 76.2 \\\\\nInverse-length & 76.7 \\\\\nLength-weighted & 75.3 \\\\\nConstraint-count & 75.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Logic-LM baseline.}\nWe compare against a Logic-LM-style approach that performs single-trace FOL verification across $K$ traces and takes a majority vote.\nOn FOLIO, this achieves 75.5\\% (vs.\\ SC 75.0\\%, \\sica{} 74.5\\%).\nAll three methods are statistically indistinguishable, suggesting that multi-trace constraint aggregation provides no advantage over per-trace symbolic verification when traces are highly correlated.\n\n\\subsection{Deployment Diagnostic: C0 + SC}\n\nWe propose a two-dimensional diagnostic for screening \\sica{} applicability before deployment.\n\n\\paragraph{C0 screening.}\nWhen C0 $< 5\\%$, \\sica{} is mathematically equivalent to SC (no multi-candidate problems exist for MAX-SAT to resolve).\nThis condition holds for QwQ-32B (C0 = 2.6\\%), ARC-Challenge (C0 = 5\\%), and near-threshold for GSM8K (C0 = 13.3\\%, but with 14.7\\% extraction success).\nC0 screening eliminates approximately half of model-domain conditions from consideration at zero computational cost.\n\n\\paragraph{SC accuracy regime.}\nAmong conditions where C0 is sufficient, SC accuracy further stratifies outcomes:\n\\begin{itemize}\n\\item SC $> 75\\%$ (Type A): Confirmation bias dominates. Constraints mirror correct answers, providing no additional signal. Examples: Qwen-14B FOLIO (75.5\\%), Qwen-72B D012 (83.3\\%).\n\\item SC $< 40\\%$ (Type C): Trace quality is insufficient. Constraints encode mostly incorrect reasoning, degrading performance. Example: Mistral-7B PW-600 (39.3\\%, $\\Delta$=$-$2.83\\pp{}).\n\\item SC $\\approx$ 50--55\\% with high C0 (candidate zone): The only observed positive results fall here. Example: Mistral-7B FOLIO (54.4\\%, C0=0.69, $\\Delta$=+4.9\\pp{}).\n\\end{itemize}\n\nHowever, we emphasize that this diagnostic has limited positive predictive power.\nWhile C0 $< 5\\%$ reliably predicts $\\Delta \\approx 0$ (necessary condition), high C0 combined with moderate SC does not guarantee positive $\\Delta$ (the prediction accuracy is 41.7\\% across all conditions).\nThe diagnostic is useful for ruling out \\sica{}, not for recommending it.\n\n\\subsection{Overhead Analysis}\n\n\\sica{} approximately doubles wall-clock time per problem: mean total time is 61.6 seconds, with trace generation consuming 51.3\\% and constraint extraction consuming 47.0\\%.\nMAX-SAT solving accounts for less than 0.01\\% of total time.\nGiven that $\\Delta \\leq 0$ in the majority of conditions, the cost-benefit ratio is unfavorable for general deployment.\nThe overhead analysis does suggest that future work should focus on extraction quality rather than solver efficiency, as the computational bottleneck and the quality bottleneck coincide in the extraction stage.\n\n\\section{Discussion}\n\n\\paragraph{The self-extraction trap.}\nOur results paint a consistent picture: the MAX-SAT aggregation mechanism is effective when given high-quality constraints (oracle gap: +14.2\\pp{}), but self-extraction from the same model that generated the reasoning traces produces constraints that largely recapitulate the model's existing beliefs.\nThis is not a simple quality problem (92\\% of constraints are discriminative) but a directionality problem: constraints discriminate in the same direction as the model's majority vote, providing no orthogonal signal.\n\n\\paragraph{Limitations of the independence framework.}\nWhile Fleiss' $\\kappa$ and $\\effk{}$ provide a useful descriptive vocabulary (explaining why Qwen-family models uniformly show zero gain), the framework has no predictive power within a model family.\nThe 50\\% joint prediction accuracy across 12 conditions is equivalent to random guessing.\nWe therefore present $\\effk{}$ as a diagnostic tool for cross-model comparison, not as a predictive framework.\n\n\\paragraph{Multi-temperature as a promising direction.}\nThe multi-temperature result ($\\Delta$=+2.45\\pp{}, $\\effk{}$ increase from 1.85 to 2.80) is the only remediation showing a positive trend.\nWhile underpowered in our study ($p$=0.18), this suggests that structured diversity interventions deserve further investigation, particularly at larger sample sizes.\nThis partially qualifies our ``9/9 failed'' framing: 8 strategies clearly failed, and 1 showed marginal promise.\n\n\\paragraph{Limitations.}\nOur primary positive result comes from a single model-domain-temperature combination (Mistral-7B, FOLIO, $T$=0.7).\nSample sizes for pilot domains (StrategyQA, ARC, GSM8K) are small ($n$=30--60), limiting statistical power.\nThe LLaMA-8B result (+6.7\\pp{}) may be confounded by high trace truncation rates (73\\%).\nWe do not evaluate trained extractors or external verifiers, which represent a different paradigm from the self-extraction setting we study.\n\n\\section{Conclusion}\n\nWe present a diagnostic study of symbolic consensus aggregation across 7 models and 6 domains.\nThree findings stand out.\nFirst, the oracle gap (+14.2\\pp{}) proves that constraint-based aggregation is a viable mechanism when constraints are reliable, localizing the current failure to extraction quality.\nSecond, nine remediation strategies fail to close this gap, with only multi-temperature mixing showing marginal promise, suggesting that the self-extraction bottleneck is largely structural.\nThird, the C0+SC diagnostic provides a practical screening tool that can eliminate unnecessary \\sica{} computation in the majority of deployment scenarios, despite its limited positive predictive power.\nThe central lesson is that same-model self-extraction produces constraints that mirror rather than complement the model's reasoning, a fundamental limitation that simple diversity or filtering interventions cannot overcome.\n\n\\bibliography{references}\n\\bibliographystyle{plainnat}\n\n\\appendix\n\n\\section{Tiebreak Analysis}\n\\label{app:tiebreak}\n\nWhen SC produces a tie (equal votes for two answers), \\sica{} can break the tie using constraint satisfaction scores. On $n$=5 tiebreak problems, \\sica{} achieves 80\\% accuracy compared to 50\\% for random tiebreak, 60\\% for alphabetical, and 40\\% for first-seen ordering. The sample size is too small for statistical inference.\n\n\\section{QwQ-32B Negative Control}\n\\label{app:qwq}\n\nQwQ-32B, a reasoning-specialized model, produces near-deterministic traces with aggregate C0 effective of 2.6\\%. On AIME ($n$=29), $\\Delta$=0.0\\pp{}. On ProofWriter ($n$=17), $\\Delta$=$-$5.9\\pp{} (non-significant given the small sample). This confirms that reasoning models with low trace diversity gain nothing from symbolic aggregation.\n\n\\section{Full Overhead Breakdown}\n\\label{app:overhead}\n\n\\begin{table}[h]\n\\centering\n\\caption{Wall-time breakdown per problem (mean over all conditions).}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nStage & \\% of total time \\\\\n\\midrule\nTrace generation & 51.3\\% \\\\\nConstraint extraction & 47.0\\% \\\\\nMAX-SAT solving & $<$0.01\\% \\\\\nOther & 1.7\\% \\\\\n\\midrule\nTotal (mean) & 61.6 seconds \\\\\n\\sica{} overhead vs.\\ SC-only & +48.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{thebibliography}{40}\n\n\\bibitem[Wang et al.(2023)]{wang2023selfconsistency}\nWang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., and Zhou, D.\n\\newblock Self-consistency improves chain of thought reasoning in language models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Pan et al.(2023)]{pan2023logiclm}\nPan, L., Alber, M., Chen, W., Gashteovski, K., Xie, Y., Feng, Z., and Lawrence, C.\n\\newblock Logic-LM: Empowering large language models with symbolic solvers for faithful logical reasoning.\n\\newblock In \\emph{Findings of EMNLP}, 2023.\n\n\\bibitem[Olausson et al.(2023)]{olausson2023linc}\nOlausson, T.~X., Gu, A., Lipkin, B., Zhang, C.~E., Solar-Lezama, A., Tenenbaum, J.~B., and Levy, R.\n\\newblock LINC: A neurosymbolic approach for logical reasoning by combining language models with first-order logic provers.\n\\newblock In \\emph{EMNLP}, 2023.\n\n\\bibitem[Condorcet(1785)]{condorcet1785}\nde Condorcet, M.~J.~A.~N.\n\\newblock \\emph{Essai sur l'application de l'analyse \\`{a} la probabilit\\'{e} des d\\'{e}cisions rendues \\`{a} la pluralit\\'{e} des voix}.\n\\newblock 1785.\n\n\\bibitem[Austen-Smith and Banks(1996)]{austensmith1996}\nAusten-Smith, D. and Banks, J.~S.\n\\newblock Information aggregation, rationality, and the {C}ondorcet jury theorem.\n\\newblock \\emph{American Political Science Review}, 90(1):34--45, 1996.\n\n\\bibitem[Li et al.(2024)]{li2024independence}\nLi, Z., et al.\n\\newblock Examining independence in ensemble sentiment classification: A {C}ondorcet jury theorem perspective.\n\\newblock \\emph{arXiv:2409.00094}, 2024.\n\n\\bibitem[Fleiss(1971)]{fleiss1971}\nFleiss, J.~L.\n\\newblock Measuring nominal scale agreement among many raters.\n\\newblock \\emph{Psychological Bulletin}, 76(5):378--382, 1971.\n\n\\bibitem[Chen et al.(2023)]{chen2023usc}\nChen, X., Aksitov, R., Alon, U., Ren, J., Xiao, K., Yin, P., Prakash, S., Sutton, C., Wang, X., and Zhou, D.\n\\newblock Universal self-consistency for large language model generation.\n\\newblock \\emph{arXiv:2311.17311}, 2023.\n\n\\bibitem[Li et al.(2023)]{li2023diverse}\nLi, Y., Lin, Z., Zhang, S., Fu, Q., Chen, B., Lou, J.-G., and Chen, W.\n\\newblock Making language models better reasoners with step-aware verifier.\n\\newblock In \\emph{ACL}, 2023.\n\n\\bibitem[Taubenfeld et al.(2025)]{taubenfeld2025weighted}\nTaubenfeld, A., et al.\n\\newblock Weighted self-consistency for language model reasoning.\n\\newblock 2025.\n\n\\bibitem[Loo et al.(2025)]{loo2025sc}\nLoo, N., et al.\n\\newblock On the scaling limits of self-consistency.\n\\newblock 2025.\n\n\\bibitem[{DyLoS}(2026)]{dylos2026}\n{DyLoS Authors}.\n\\newblock {DyLoS}: Dynamic logic solving with language models.\n\\newblock In \\emph{EACL}, 2026.\n\n\\bibitem[{Aristotle}(2025)]{aristotle2025}\n{Aristotle Authors}.\n\\newblock Aristotle: Structured reasoning with external verification.\n\\newblock In \\emph{ACL}, 2025.\n\n\\bibitem[{FoVer}(2025)]{fover2025}\n{FoVer Authors}.\n\\newblock {FoVer}: Formal verification of large language model outputs.\n\\newblock \\emph{TACL}, 2025.\n\n\\bibitem[Snell et al.(2025)]{snell2025scaling}\nSnell, C., et al.\n\\newblock Scaling {LLM} test-time compute.\n\\newblock 2025.\n\n\\bibitem[{DeepSeek-AI}(2025)]{deepseekr1}\n{DeepSeek-AI}.\n\\newblock {DeepSeek-R1}: Incentivizing reasoning capability in {LLMs} via reinforcement learning.\n\\newblock \\emph{arXiv:2501.12948}, 2025.\n\n\\bibitem[Cobbe et al.(2021)]{cobbe2021orm}\nCobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., Hesse, C., and Schulman, J.\n\\newblock Training verifiers to solve math word problems.\n\\newblock \\emph{arXiv:2110.14168}, 2021.\n\n\\bibitem[Cobbe et al.(2021b)]{cobbe2021gsm8k}\nCobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., Hesse, C., and Schulman, J.\n\\newblock Training verifiers to solve math word problems.\n\\newblock \\emph{arXiv:2110.14168}, 2021.\n\n\\bibitem[Lightman et al.(2023)]{lightman2023prm}\nLightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I., and Alignment, K.\n\\newblock Let's verify step by step.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Liang et al.(2023)]{liang2023debate}\nLiang, T., He, Z., Jiao, W., Wang, X., Wang, Y., Wang, R., Yang, Y., Tu, Z., and Shi, S.\n\\newblock Encouraging divergent thinking in large language models through multi-agent debate.\n\\newblock \\emph{arXiv:2305.19118}, 2023.\n\n\\bibitem[Du et al.(2023)]{du2023debate}\nDu, Y., Li, S., Torralba, A., Tenenbaum, J.~B., and Mordatch, I.\n\\newblock Improving factuality and reasoning in language models through multiagent debate.\n\\newblock \\emph{arXiv:2305.14325}, 2023.\n\n\\bibitem[Wei et al.(2022)]{wei2022cot}\nWei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., and Zhou, D.\n\\newblock Chain-of-thought prompting elicits reasoning in large language models.\n\\newblock In \\emph{NeurIPS}, 2022.\n\n\\bibitem[Kojima et al.(2022)]{kojima2022zerocot}\nKojima, T., Gu, S.~S., Reid, M., Matsuo, Y., and Iwasawa, Y.\n\\newblock Large language models are zero-shot reasoners.\n\\newblock In \\emph{NeurIPS}, 2022.\n\n\\bibitem[Han et al.(2022)]{han2022folio}\nHan, S., Schoelkopf, H., Zhao, Y., Qi, Z., Riddell, M., Benson, L., Sun, L., Zubova, E., Qiao, Y., Burtell, M., et al.\n\\newblock {FOLIO}: Natural language reasoning with first-order logic.\n\\newblock \\emph{arXiv:2209.00840}, 2022.\n\n\\bibitem[Tafjord et al.(2021)]{tafjord2021proofwriter}\nTafjord, O., Dalvi, B., and Clark, P.\n\\newblock {ProofWriter}: Generating implications, proofs, and abductive statements over natural language.\n\\newblock In \\emph{Findings of ACL}, 2021.\n\n\\bibitem[Clark et al.(2018)]{clark2018arc}\nClark, P., Cowhey, I., Etzioni, O., Khot, T., Sabharwal, A., Schoenick, C., and Tafjord, O.\n\\newblock Think you have solved question answering? {T}ry {ARC}, the {AI2} reasoning challenge.\n\\newblock \\emph{arXiv:1803.05457}, 2018.\n\n\\bibitem[Geva et al.(2021)]{geva2021strategyqa}\nGeva, M., Khashabi, D., Segal, E., Khot, T., Roth, D., and Berant, J.\n\\newblock Did {A}ristotle use a laptop? {A} question answering benchmark with implicit reasoning strategies.\n\\newblock \\emph{TACL}, 2021.\n\n\\bibitem[Liu et al.(2023)]{liu2023logiqa}\nLiu, J., et al.\n\\newblock {LogiQA} 2.0: An improved dataset for logical reasoning.\n\\newblock \\emph{IEEE/ACM Transactions on Audio, Speech, and Language Processing}, 2023.\n\n\\bibitem[Jiang et al.(2023)]{jiang2023mistral}\nJiang, A.~Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D.~S., de~las Casas, D., Bressand, F., Lengyel, G., Lample, G., et al.\n\\newblock Mistral 7{B}.\n\\newblock \\emph{arXiv:2310.06825}, 2023.\n\n\\bibitem[{Qwen Team}(2024)]{qwen2024}\n{Qwen Team}.\n\\newblock Qwen2.5 technical report.\n\\newblock 2024.\n\n\\bibitem[Touvron et al.(2023)]{touvron2023llama}\nTouvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., et al.\n\\newblock {LLaMA} 2: Open foundation and fine-tuned chat models.\n\\newblock \\emph{arXiv:2307.09288}, 2023.\n\n\\bibitem[{SATBench}(2025)]{satbench2025}\n{SATBench Authors}.\n\\newblock {SATBench}: Benchmarking constraint satisfaction with language models.\n\\newblock In \\emph{EMNLP}, 2025.\n\n\\bibitem[{LLM-CP}(2025)]{llmcp2025}\n{LLM-CP Authors}.\n\\newblock {LLM} meets constraint propagation.\n\\newblock In \\emph{IJCAI}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "e92fa37d-abeb-43fe-9148-a519fedb9507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T034058 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_co…",
  "leafUuid": "c7d3ff51-d92d-4e7d-9935-c9841b577714",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier symbolic consensus paper",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b"
}
```

---

### Tool call

_source line 28 · 2026-05-19T04:33:18.843Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XoXGcsNqJBbAFbSB6h5CDe`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7d3ff51-d92d-4e7d-9935-c9841b577714",
  "isSidechain": false,
  "requestId": "req_011CbBJX56ADSxjx9nFaQi84",
  "type": "assistant",
  "uuid": "823c9c54-6418-4c7d-9656-53c3aeecda4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YN6GsYwV5ezpFhqUzyesim",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14551,
      "cache_read_input_tokens": 48899,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 48899,
          "cache_creation_input_tokens": 14551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14551
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

_source line 29 · 2026-05-19T04:33:19.375Z_

<details><summary>↩ Tool result · `toolu_01XoXGcsNqJBbAFbSB6h5CDe`</summary>

```text
LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmcsc10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (12 pages, 236469 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "823c9c54-6418-4c7d-9656-53c3aeecda4e",
  "isSidechain": false,
  "promptId": "6cd4ba32-185c-4e26-8eaf-fcddb4213dff",
  "type": "user",
  "uuid": "e59a9708-e77a-46cb-a384-1bcfb869d5da",
  "toolUseResult": {
    "stdout": "LaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmcsc10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (12 pages, 236469 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "823c9c54-6418-4c7d-9656-53c3aeecda4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-19T04:33:23.115Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013y6WRsfhsMaWWvjRSEG2Dq`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10",
  "description": "Second pdflatex pass for cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e59a9708-e77a-46cb-a384-1bcfb869d5da",
  "isSidechain": false,
  "requestId": "req_011CbBJXPMksgKb7nUpjYDCy",
  "type": "assistant",
  "uuid": "57975d31-54be-426e-bc99-a1b0bc5c09c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199x3TmA87aacX5Codu6uZC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 63450,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 905,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 63450,
          "cache_creation_input_tokens": 905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 905
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

_source line 31 · 2026-05-19T04:33:23.692Z_

<details><summary>↩ Tool result · `toolu_013y6WRsfhsMaWWvjRSEG2Dq`</summary>

```text
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (12 pages, 240313 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57975d31-54be-426e-bc99-a1b0bc5c09c9",
  "isSidechain": false,
  "promptId": "6cd4ba32-185c-4e26-8eaf-fcddb4213dff",
  "type": "user",
  "uuid": "d41be91a-e65b-4d60-ac26-f20903355b39",
  "toolUseResult": {
    "stdout": "pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (12 pages, 240313 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "57975d31-54be-426e-bc99-a1b0bc5c09c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-19T04:33:23.696Z_

```json
{
  "parentUuid": "d41be91a-e65b-4d60-ac26-f20903355b39",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fe6c07ac-b680-4fa2-a8de-ac62ab30c9c2",
  "timestamp": "2026-05-19T04:33:23.696Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-19T04:33:27.229Z_

<details><summary>Logged reasoning block</summary>

```text
The paper compiles successfully to 12 pages. Let me check for any warnings or errors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe6c07ac-b680-4fa2-a8de-ac62ab30c9c2",
  "isSidechain": false,
  "requestId": "req_011CbBJXhqW23GpssR36Vdeo",
  "type": "assistant",
  "uuid": "ef8c7fd6-7797-4de6-95d1-c67d5efaabde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RTK7f2VeUNKnmcMYh5cFRY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 64355,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 541,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 64355,
          "cache_creation_input_tokens": 541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 541
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

_source line 34 · 2026-05-19T04:33:27.761Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01N3fYbEkntSJJ5zyWLYqzpF`</summary>

```json
{
  "command": "grep -c \"Warning\\|Error\" paper.log",
  "description": "Count warnings/errors in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef8c7fd6-7797-4de6-95d1-c67d5efaabde",
  "isSidechain": false,
  "requestId": "req_011CbBJXhqW23GpssR36Vdeo",
  "type": "assistant",
  "uuid": "1bdbcc6d-f870-4267-b7bd-c0fb79f727e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RTK7f2VeUNKnmcMYh5cFRY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 64355,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 541,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 64355,
          "cache_creation_input_tokens": 541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 541
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

_source line 35 · 2026-05-19T04:33:27.812Z_

<details><summary>↩ Tool result · `toolu_01N3fYbEkntSJJ5zyWLYqzpF`</summary>

```text
3
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bdbcc6d-f870-4267-b7bd-c0fb79f727e4",
  "isSidechain": false,
  "promptId": "6cd4ba32-185c-4e26-8eaf-fcddb4213dff",
  "type": "user",
  "uuid": "6732871f-c411-468f-bddc-a7567a0d4d87",
  "toolUseResult": {
    "stdout": "3",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1bdbcc6d-f870-4267-b7bd-c0fb79f727e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-19T04:33:31.456Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HEuxepxpbkXqXNsYNh214n`</summary>

```json
{
  "command": "grep \"Warning\\|Error\" paper.log | head -10",
  "description": "Show specific warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6732871f-c411-468f-bddc-a7567a0d4d87",
  "isSidechain": false,
  "requestId": "req_011CbBJY2iJziUPrC1LRt9z8",
  "type": "assistant",
  "uuid": "dae94bb9-afd1-45c0-a5dd-0a060f4727c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015AtwJ9GgyM3Pnnkzu4sfwn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 133,
      "cache_read_input_tokens": 64896,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 133,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 64896,
          "cache_creation_input_tokens": 133,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 133
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

_source line 37 · 2026-05-19T04:33:31.531Z_

<details><summary>↩ Tool result · `toolu_01HEuxepxpbkXqXNsYNh214n`</summary>

```text
LaTeX Font Warning: Font shape `OT1/cmr/bx/sc' undefined
LaTeX Font Warning: Some font shapes were not available, defaults substituted.
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dae94bb9-afd1-45c0-a5dd-0a060f4727c9",
  "isSidechain": false,
  "promptId": "6cd4ba32-185c-4e26-8eaf-fcddb4213dff",
  "type": "user",
  "uuid": "7e2bb35f-ff23-4a06-b018-39960c16ebdd",
  "toolUseResult": {
    "stdout": "LaTeX Font Warning: Font shape `OT1/cmr/bx/sc' undefined\nLaTeX Font Warning: Some font shapes were not available, defaults substituted.\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "dae94bb9-afd1-45c0-a5dd-0a060f4727c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T04:33:39.434Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01V4idA1fwRFACgTEGQ9me1L`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"Output written|Error|pages\"",
  "description": "Third pdflatex pass to resolve remaining cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e2bb35f-ff23-4a06-b018-39960c16ebdd",
  "isSidechain": false,
  "requestId": "req_011CbBJYHLP9DwH9VTGhJEPL",
  "type": "assistant",
  "uuid": "9baece20-2a3f-4d36-b8b2-cd38b6e9a5b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FcGyY71KDEEyyJospBV88V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 156,
      "cache_read_input_tokens": 65029,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 65029,
          "cache_creation_input_tokens": 156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 156
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

_source line 39 · 2026-05-19T04:33:40.496Z_

<details><summary>↩ Tool result · `toolu_01V4idA1fwRFACgTEGQ9me1L`</summary>

```text
Output written on paper.pdf (12 pages, 240313 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9baece20-2a3f-4d36-b8b2-cd38b6e9a5b1",
  "isSidechain": false,
  "promptId": "6cd4ba32-185c-4e26-8eaf-fcddb4213dff",
  "type": "user",
  "uuid": "9315bc10-bd0f-49ea-9519-80fb4c44b30d",
  "toolUseResult": {
    "stdout": "Output written on paper.pdf (12 pages, 240313 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9baece20-2a3f-4d36-b8b2-cd38b6e9a5b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-19T04:33:53.583Z_

编译成功，12 页 PDF，无错误。

论文以 "Comprehensive Diagnostic Study" 重新定位，覆盖 experiment_data.json 中全部 20 个实验：

- **Table 1**: 主结果 (11 个 model×domain 条件)
- **Table 2**: Oracle gap (+14.22pp, p < 10⁻⁶)
- **Table 3**: Independence 量化 (κ, Eff-K, 6 个条件)
- **Table 4**: Joint prediction 准确率 (50%, 等于随机)
- **Table 5**: K sensitivity (Mistral + Qwen)
- **Table 6**: T sensitivity (4 温度 + multi-temp)
- **Table 7**: 9 种 remediation 汇总
- **Table 8**: Aggregation ablation (MAX-SAT ≈ count-only)
- **Table 9**: Weighted SC (全部 n.s.)
- **Appendix**: Tiebreak, QwQ negative control, overhead breakdown

叙事三条腿：(1) Oracle gap 硬结果；(2) 9 种修复广度；(3) C0+SC 诊断。诚实处理了 multi-temp 意外正向、K/T 曲线 noisy、Eff-K 模型内无预测力等 worst-tier 弱点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9315bc10-bd0f-49ea-9519-80fb4c44b30d",
  "isSidechain": false,
  "requestId": "req_011CbBJYwfUjaqr2LCtwDcnc",
  "type": "assistant",
  "uuid": "b80d1b59-9908-4594-85a3-b90c7ad5ae6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLtY4Du6NRyALgsevnMy9S",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 139,
      "cache_read_input_tokens": 65185,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 139,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 372,
          "cache_read_input_tokens": 65185,
          "cache_creation_input_tokens": 139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 139
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

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T034058 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_co…",
  "leafUuid": "b80d1b59-9908-4594-85a3-b90c7ad5ae6d",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier symbolic consensus paper",
  "sessionId": "08579623-f8e4-4cf1-a921-af800586a59b"
}
```

---
