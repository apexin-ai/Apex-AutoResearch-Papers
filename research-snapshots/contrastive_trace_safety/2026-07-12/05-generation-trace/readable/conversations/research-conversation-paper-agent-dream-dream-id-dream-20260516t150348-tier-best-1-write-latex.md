# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T150348 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/c4e37549-6632-48cc-a879-3de6d7b0e94c.jsonl`
- **Structured JSON:** [`ccdbb363da21ce242fcf.json`](../../sessions/cc/ccdbb363da21ce242fcf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T15:50:37.052Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T15:50:37.052Z",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T150348 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Framing B 完全成立：Paper = systematic mining study + methodological contribution。\nStandard eval 上 embed Δ 较小（Qwen ~+0.4pp, StarCoder ~+0.6pp），但 D062 query-split  evaluation 揭示标准评估因 checkpoint 过拟合掩盖了真实效应——held-out evaluation 上 embed Δ  恢复至 Qwen +1.4pp, StarCoder +0.9pp（均在 best 档预设范围内）。这一发现本身就是方法论贡献： checkpoint selection criterion effect (+16.3pp max) > mining strategy effect (~1pp)， 说明社区低估了 mining 效果是因为评估方法论缺陷。\nBM25 negatives 在两个 encoder 上均 harm（Δ ≤ -1.5pp），empirically 关闭 CoCoHaNeRe 修正论证。 UniXcoder 3-seed null result 干净地归因于 125M scale boundary condition。 RepoBench-R 替代 SWE-bench 作为 held-out external validation，CIs non-overlapping。\n3 claims 原样成立：Claim 1 (embed mining reliable) + Claim 2 (exploratory representation  geometry interaction) + 额外贡献 (checkpoint criterion methodology)。EMNLP Main 强投。\nM2 anchors — Standard eval: Qwen random=0.570, embed=0.573, SC random=0.479, embed=0.485。 D062 query-split: Qwen random=0.361, embed=0.375, SC random=0.305, embed=0.314。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T15:50:37.056Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T15:50:37.056Z",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c"
}
```

---

## Round 1

36 recorded events

### User

_source line 3 · 2026-05-16T15:50:37.077Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T150348 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Framing B 完全成立：Paper = systematic mining study + methodological contribution。
Standard eval 上 embed Δ 较小（Qwen ~+0.4pp, StarCoder ~+0.6pp），但 D062 query-split  evaluation 揭示标准评估因 checkpoint 过拟合掩盖了真实效应——held-out evaluation 上 embed Δ  恢复至 Qwen +1.4pp, StarCoder +0.9pp（均在 best 档预设范围内）。这一发现本身就是方法论贡献： checkpoint selection criterion effect (+16.3pp max) > mining strategy effect (~1pp)， 说明社区低估了 mining 效果是因为评估方法论缺陷。
BM25 negatives 在两个 encoder 上均 harm（Δ ≤ -1.5pp），empirically 关闭 CoCoHaNeRe 修正论证。 UniXcoder 3-seed null result 干净地归因于 125M scale boundary condition。 RepoBench-R 替代 SWE-bench 作为 held-out external validation，CIs non-overlapping。
3 claims 原样成立：Claim 1 (embed mining reliable) + Claim 2 (exploratory representation  geometry interaction) + 额外贡献 (checkpoint criterion methodology)。EMNLP Main 强投。
M2 anchors — Standard eval: Qwen random=0.570, embed=0.573, SC random=0.479, embed=0.485。 D062 query-split: Qwen random=0.361, embed=0.375, SC random=0.305, embed=0.314。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "724d7aca-00e7-494b-8d2d-e8d37c28745c",
  "type": "user",
  "uuid": "cfd1241c-edd6-4b95-8436-7a6c3f342f42",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T15:50:37.076Z_

```json
{
  "parentUuid": "cfd1241c-edd6-4b95-8436-7a6c3f342f42",
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
  "uuid": "8d6b8fc2-b04a-4f8e-9636-ad63b73a5e5f",
  "timestamp": "2026-05-16T15:50:37.076Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T15:50:37.076Z_

```json
{
  "parentUuid": "8d6b8fc2-b04a-4f8e-9636-ad63b73a5e5f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "947df479-af36-4412-adf6-085d4053ebe4",
  "timestamp": "2026-05-16T15:50:37.076Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
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
  "aiTitle": "Generate simulated research paper for dream mining evaluation",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c"
}
```

---

### Assistant

_source line 7 · 2026-05-16T15:50:41.064Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment data and paper framing files to understand what I need to write.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "947df479-af36-4412-adf6-085d4053ebe4",
  "isSidechain": false,
  "requestId": "req_011Cb6WkDkYfTyTTCkBPTudn",
  "type": "assistant",
  "uuid": "670fbd21-d2c8-4d03-b5bb-4aae7ad4e454",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRt9naATSroi7R1EWbExR2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11469,
      "cache_read_input_tokens": 11841,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11469,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 225,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11469
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

_source line 8 · 2026-05-16T15:50:41.570Z_

<details open><summary>🔧 Tool call — Read · `toolu_013GpRMzCRN9FDGDU1jrf34D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "670fbd21-d2c8-4d03-b5bb-4aae7ad4e454",
  "isSidechain": false,
  "requestId": "req_011Cb6WkDkYfTyTTCkBPTudn",
  "type": "assistant",
  "uuid": "a2502fa9-0074-497c-9eb6-3e3e981a8e67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRt9naATSroi7R1EWbExR2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11469,
      "cache_read_input_tokens": 11841,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11469,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 225,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11469
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

_source line 9 · 2026-05-16T15:50:42.216Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cxb3smxNqg6UY2xCPpKDke`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2502fa9-0074-497c-9eb6-3e3e981a8e67",
  "isSidechain": false,
  "requestId": "req_011Cb6WkDkYfTyTTCkBPTudn",
  "type": "assistant",
  "uuid": "d9e7d0ee-b0dc-4186-9bb7-76b7b484afc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRt9naATSroi7R1EWbExR2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11469,
      "cache_read_input_tokens": 11841,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11469,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 225,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11469
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

_source line 10 · 2026-05-16T15:50:42.223Z_

<details><summary>↩ Tool result · `toolu_01Cxb3smxNqg6UY2xCPpKDke`</summary>

```text
1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.
10	
11	2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.
12	
13	3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]
14	
15	## Story Spine
16	
17	- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.
18	
19	- **Existing approaches & gaps**:
20	  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies
21	  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal
22	  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
23	  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings
24	  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works
25	
26	- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.
27	
28	- **Headline result template**: "Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective."
29	
30	## Core Insight
31	
32	Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.
33	
34	## Dual-Pillar Motivation
35	
36	1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.
37	2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.
38	
39	## Formal Definition
40	
41	Given retrieval domain D, structural graph G, query q:
42	**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)
43	
44	The structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).
45	
46	## Title Options
47	
48	- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
49	- Alternative: "Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]
50	- Backup: "Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval"
51	
52	## Venue Fit
53	
54	1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
55	2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
56	3. **Against "incremental" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.
57	
58	## Anticipated Reviewer Concerns
59	
60	| Concern | Response | Evidence |
61	|---------|----------|----------|
62	| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |
63	| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |
64	| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |
65	| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |
66	| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |
67	| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |
68	| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |
69	| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |
70	| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |
71	| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |
72	| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |
73	| "Complementary signal" overstatement | Temper: "conditionally beneficial" not "always complementary" | Writing discipline |
74	| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |
75	
76	## Evidence Status
77	
78	### Confirmed findings (basis for claims):
79	- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline
80	- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction
81	- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)
82	- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only
83	- plan_006: CodeQL scalability confirmed at 123-repo scale
84	
85	### Evidence presentation strategy:
86	- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)
87	- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)
88	- Both metrics show directionally consistent results; no goalpost-moving between metrics
89	
90	### In progress:
91	- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.
92	- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.
93	- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15
94	
95	### Planned (priority order):
96	- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)
97	- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
98	- plan_019: Pool size sensitivity (Dream consensus — external validity)
99	- plan_014: Temperature ablation (Dream reviewer concern)
100	- plan_004: RepoBench-R second benchmark (with multi-seed CIs)
101	- plan_015: Dynamic mining baseline
102	- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)
103	- plan_007/008/009: Additional ablations
104	
105	## Limitations
106	
107	Effect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.
108	
109	## Contingency (if full M2 results weaken claims)
110	
111	### All 18 runs confirm pilot pattern: Best case
112	- Full statistical power, paper as framed above
113	- Target: EMNLP Main
114	
115	### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
116	- Drop Claim 2 to analysis observation
117	- Paper becomes: "Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions"
118	- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main
119	
120	### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]
121	- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment
122	- Pivot: "systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal"
123	- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome
124	- Claim 1 core preserved: "Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling"
125	- Impact: BM25 result determines narrative nuance, not core contribution
126	
127	### Embedding mining also loses advantage at full scale: Major reassessment needed
128	- Recheck data pipeline for bugs (full-scale data may have distribution differences)
129	- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
130	- Discuss with user before committing direction
131	
132	## Deprecated Claims (with reason)
133	
134	- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
135	
136	&lt;!-- Claim 2 wording fix: 2026-05-15 -->
137	&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->
138	&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->
139	&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->
140	&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->
141	&lt;!-- Status data refresh: s44 DONE, 4/9 runs, m1 90.5%, headline caveat: 2026-05-15 -->
142	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9e7d0ee-b0dc-4186-9bb7-76b7b484afc9",
  "isSidechain": false,
  "promptId": "724d7aca-00e7-494b-8d2d-e8d37c28745c",
  "type": "user",
  "uuid": "1d5dc202-dbc4-41e0-be5b-86a54cdca7a8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper_framing.md",
      "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\n\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\n\n- **Headline result template**: \"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\"\n\n## Core Insight\n\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\n- Backup: \"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### Evidence presentation strategy:\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\n\n### In progress:\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Limitations\n\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions\"\n- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main\n\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment\n- Pivot: \"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal\"\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome\n- Claim 1 core preserved: \"Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling\"\n- Impact: BM25 result determines narrative nuance, not core contribution\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->\n&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->\n&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->\n&lt;!-- Status data refresh: s44 DONE, 4/9 runs, m1 90.5%, headline caveat: 2026-05-15 -->\n",
      "numLines": 142,
      "startLine": 1,
      "totalLines": 142
    }
  },
  "sourceToolAssistantUUID": "d9e7d0ee-b0dc-4186-9bb7-76b7b484afc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T15:50:42.345Z_

<details><summary>↩ Tool result · `toolu_013GpRMzCRN9FDGDU1jrf34D`</summary>

```text
1	[
2	  {
3	    "name": "M3a SWE-bench Lite E2E — OOD Limitation Disclosure",
4	    "description": "3 strategies × best Qwen checkpoint on SWE-bench Lite 300 instances。 实际已完成（random_s42, 100 instances + BM25 baseline 300）。结果为 OOD 泛化失败， 在论文中作为 limitation 呈现而非贡献。\n",
5	    "results": {
6	      "random_s42_100": {
7	        "R_at_1": 0.04,
8	        "R_at_5": 0.11,
9	        "R_at_10": 0.14,
10	        "R_at_20": 0.16,
11	        "MRR": 0.0698
12	      },
13	      "bm25_baseline_300": {
14	        "R_at_1": 0.2733,
15	        "R_at_5": 0.4667,
16	        "R_at_10": 0.55
17	      },
18	      "neural_vs_bm25_gap_R1_pp": -23.3,
19	      "status": "DONE_FAILED",
20	      "director_decision": "放弃 SWE-bench 作为论文贡献，外部验证改用 RepoBench-R"
21	    },
22	    "tables": [
23	      {
24	        "name": "Table S4: SWE-bench OOD Evaluation (Limitation)",
25	        "columns": [
26	          "Retriever",
27	          "R@1",
28	          "R@5",
29	          "R@10",
30	          "MRR",
31	          "N"
32	        ],
33	        "rows": [
34	          [
35	            "BM25 (reference)",
36	            0.273,
37	            0.467,
38	            0.55,
39	            0.36,
40	            300
41	          ],
42	          [
43	            "StructFuse-random",
44	            0.04,
45	            0.11,
46	            0.14,
47	            0.07,
48	            100
49	          ]
50	        ]
51	      }
52	    ],
53	    "figures": [],
54	    "analysis": "SWE-bench failure 在 best tier 下反而加强了论文：它划定了清晰的 scope boundary， 展示了作者的自我审视能力。Reviewer concern \"no downstream eval\" 由 RepoBench-R 回应， SWE-bench 失败则作为 honest limitation 处理，1-2 段落放在 Limitations section。\n\n\nR@1=0.04 vs BM25=0.2733 表明 contrastive retriever 在 OOD 跨 repo 场景完全失败。 根因：SWE-smith 训练数据是 intra-repo 检索（query 与 candidates 来自同一 repo）， 而 SWE-bench 是 cross-repo 设置（模型未见过的 repo）。Contrastive fine-tuning在小 pool  内 intra-repo 检索上过拟合，丧失了 pretrained encoder 的 cross-repo 泛化能力。 BM25 因为是 lexical matching（不依赖 learned representations）所以不受此影响。\n在 best tier 下，这一失败被 strategically 利用：(1) 诚实报告增强论文可信度， (2) 明确 scope boundary \"our results apply to intra-repo retrieval settings\"， (3) 激发 future work 方向 \"bridging the intra/cross-repo gap\"。 RepoBench-R 替代作为 held-out evaluation（仍是 cross-file 但 repo-aware 设置）。\n"
55	  },
56	  {
57	    "name": "RepoBench-R Cross-File Retrieval with 3-Seed Bootstrap CIs",
58	    "description": "RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 3 seeds ×  3 strategies × 2 encoders（Qwen, StarCoder）。报告 R@1 均值 + 95% bootstrap CI。 这是 SWE-bench 失败后的替代 held-out external validation。\n",
59	    "results": {
60	      "qwen_test_hard": {
61	        "random_R1_mean": 0.62,
62	        "random_R1_ci": [
63	          0.615,
64	          0.625
65	        ],
66	        "embedding_R1_mean": 0.632,
67	        "embedding_R1_ci": [
68	          0.626,
69	          0.638
70	        ],
71	        "dataflow_R1_mean": 0.626,
72	        "dataflow_R1_ci": [
73	          0.62,
74	          0.632
75	        ],
76	        "bm25_R1_mean": 0.601,
77	        "bm25_R1_ci": [
78	          0.595,
79	          0.607
80	        ],
81	        "embedding_minus_random_pp": 1.2,
82	        "bm25_minus_random_pp": -1.9
83	      },
84	      "qwen_test_easy": {
85	        "random_R1_mean": 0.842,
86	        "embedding_R1_mean": 0.851,
87	        "dataflow_R1_mean": 0.847,
88	        "embedding_minus_random_pp": 0.9
89	      },
90	      "starcoder_test_hard": {
91	        "random_R1_mean": 0.571,
92	        "random_R1_ci": [
93	          0.565,
94	          0.577
95	        ],
96	        "embedding_R1_mean": 0.579,
97	        "embedding_R1_ci": [
98	          0.573,
99	          0.585
100	        ],
101	        "dataflow_R1_mean": 0.568,
102	        "dataflow_R1_ci": [
103	          0.562,
104	          0.574
105	        ],
106	        "bm25_R1_mean": 0.553,
107	        "bm25_R1_ci": [
108	          0.547,
109	          0.559
110	        ],
111	        "embedding_minus_random_pp": 0.8,
112	        "bm25_minus_random_pp": -1.8
113	      },
114	      "starcoder_test_easy": {
115	        "random_R1_mean": 0.81,
116	        "embedding_R1_mean": 0.816,
117	        "embedding_minus_random_pp": 0.6
118	      },
119	      "repobench_embed_vs_random_avg_pp": 1.0,
120	      "CI_non_overlapping_embed_vs_random": true,
121	      "bootstrap_N": 10000
122	    },
123	    "tables": [
124	      {
125	        "name": "Table 5: RepoBench-R Results (test_hard, pool≈18)",
126	        "columns": [
127	          "Encoder",
128	          "Strategy",
129	          "R@1 (%)",
130	          "95% CI",
131	          "Δ vs Random (pp)"
132	        ],
133	        "rows": [
134	          [
135	            "Qwen",
136	            "BM25",
137	            60.1,
138	            "[59.5, 60.7]",
139	            "-1.9"
140	          ],
141	          [
142	            "Qwen",
143	            "random",
144	            62.0,
145	            "[61.5, 62.5]",
146	            "—"
147	          ],
148	          [
149	            "Qwen",
150	            "dataflow",
151	            62.6,
152	            "[62.0, 63.2]",
153	            "+0.6"
154	          ],
155	          [
156	            "Qwen",
157	            "embedding",
158	            63.2,
159	            "[62.6, 63.8]",
160	            "+1.2"
161	          ],
162	          [
163	            "StarCoder",
164	            "BM25",
165	            55.3,
166	            "[54.7, 55.9]",
167	            "-1.8"
168	          ],
169	          [
170	            "StarCoder",
171	            "random",
172	            57.1,
173	            "[56.5, 57.7]",
174	            "—"
175	          ],
176	          [
177	            "StarCoder",
178	            "dataflow",
179	            56.8,
180	            "[56.2, 57.4]",
181	            "-0.3"
182	          ],
183	          [
184	            "StarCoder",
185	            "embedding",
186	            57.9,
187	            "[57.3, 58.5]",
188	            "+0.8"
189	          ]
190	        ]
191	      }
192	    ],
193	    "figures": [],
194	    "analysis": "Cross-benchmark 一致性是 best tier 核心证据：embedding mining 在 SWE-smith 和  RepoBench-R 上均显著提升两个 encoder，BM25 均 harm。这排除了 \"单 benchmark artifact\"  reviewer concern。Strategy ranking BM25 < random < dataflow ≤ embedding 完美保持。 test_easy ceiling effect 间接验证了 pool size 对效果幅度的调节作用（与 plan_019 互补）。\n\n\nRepoBench-R 是 cross-file code completion 任务，与 SWE-smith (bug-fix retrieval)  领域不同但任务结构相似（从 repo 内候选文件中检索正确文件）。Pool=18 (test_hard) 提供 足够的 distractor 使 mining 质量差异体现。\nEmbedding mining 在 test_hard 上持续帮助两个 encoder（Qwen +1.2pp, StarCoder +0.8pp）， 因为 harder negatives 训练使 encoder 更善于区分 \"semantically similar but functionally  distinct\" 文件——这一能力跨任务泛化。CIs non-overlapping 因为 8K test instances 提供 足够的统计功效，即使只有 3 seeds，instance-level bootstrap 也能给出 tight CIs。\nBM25 negatives 在 RepoBench-R 上同样 harm（-1.8 to -1.9pp），与 SWE-smith 一致， 说明 BM25 harm 不是 benchmark-specific artifact 而是 strategy 固有问题。\nTest_easy (pool=6) 上 delta 压缩至 0.6-0.9pp 是预期的 ceiling effect—— 6 candidates 中选对 1 个的 baseline 已经很高。\nDataflow 在 Qwen test_hard 上 +0.6pp 但 CI 与 random 接近重叠， StarCoder 上 -0.3pp（CI 含零）——与 SWE-smith encoder-strategy interaction 一致。\n"
195	  },
196	  {
197	    "name": "Stratified Analysis with 5 Strata (D062 Query-Split Evaluation)",
198	    "description": "5 层分层分析：repo size / pool size / query-positive similarity /  structural data availability (90% with m1_reextract_v2 vs 10% remaining errors) /  neg_difficulty quartile。使用 M2 best checkpoints 在 D062 query-split held-out  evaluation 上重新评估。\n",
199	    "results": {
200	      "stratum_structural_available": {
201	        "with_dataflow_90pct": {
202	          "qwen_dataflow_minus_random_pp": 0.8,
203	          "qwen_embed_minus_random_pp": 1.3,
204	          "starcoder_dataflow_minus_random_pp": -0.2,
205	          "n_instances": "~13000",
206	          "note": "m1_reextract_v2 提升 coverage 从 34% 到 90%"
207	        },
208	        "no_dataflow_10pct": {
209	          "qwen_dataflow_minus_random_pp": 0.1,
210	          "qwen_embed_minus_random_pp": 1.4,
211	          "n_instances": "~1400"
212	        }
213	      },
214	      "stratum_neg_difficulty_quartile": {
215	        "Q1_easiest": {
216	          "qwen_embed_minus_random_pp": 0.6,
217	          "qwen_dataflow_minus_random_pp": 0.2
218	        },
219	        "Q2": {
220	          "qwen_embed_minus_random_pp": 1.1,
221	          "qwen_dataflow_minus_random_pp": 0.5
222	        },
223	        "Q3": {
224	          "qwen_embed_minus_random_pp": 1.7,
225	          "qwen_dataflow_minus_random_pp": 0.9
226	        },
227	        "Q4_hardest": {
228	          "qwen_embed_minus_random_pp": 2.3,
229	          "qwen_dataflow_minus_random_pp": 1.5
230	        }
231	      },
232	      "stratum_repo_size": {
233	        "small_lt50": {
234	          "embedding_delta_pp": 2.0,
235	          "n": "~500"
236	        },
237	        "medium_50_200": {
238	          "embedding_delta_pp": 1.6,
239	          "n": "~4100"
240	        },
241	        "large_200_500": {
242	          "embedding_delta_pp": 1.3,
243	          "n": "~5500"
244	        },
245	        "xlarge_500plus": {
246	          "embedding_delta_pp": 1.0,
247	          "n": "~5100"
248	        }
249	      },
250	      "stratum_pool_size": {
251	        "pool_lt20": {
252	          "embedding_delta_pp": 0.7,
253	          "dataflow_delta_pp": 0.2
254	        },
255	        "pool_20_50": {
256	          "embedding_delta_pp": 1.5,
257	          "dataflow_delta_pp": 0.6
258	        },
259	        "pool_gt50": {
260	          "embedding_delta_pp": 1.9,
261	          "dataflow_delta_pp": 0.9
262	        }
263	      },
264	      "stratum_query_pos_sim": {
265	        "high_sim_gt095": {
266	          "embedding_delta_pp": 1.8,
267	          "dataflow_delta_pp": 1.2
268	        },
269	        "medium_sim_085_095": {
270	          "embedding_delta_pp": 1.3,
271	          "dataflow_delta_pp": 0.5
272	        },
273	        "low_sim_lt085": {
274	          "embedding_delta_pp": 0.8,
275	          "dataflow_delta_pp": 0.1
276	        }
277	      }
278	    },
279	    "tables": [
280	      {
281	        "name": "Table 6: Stratified Embed-Random Δ by Neg Difficulty Quartile (Qwen, D062 eval)",
282	        "columns": [
283	          "Quartile",
284	          "margin_mean",
285	          "emb−rand (pp)",
286	          "df−rand (pp)"
287	        ],
288	        "rows": [
289	          [
290	            "Q1 (easiest)",
291	            0.135,
292	            "+0.6",
293	            "+0.2"
294	          ],
295	          [
296	            "Q2",
297	            0.072,
298	            "+1.1",
299	            "+0.5"
300	          ],
301	          [
302	            "Q3",
303	            0.028,
304	            "+1.7",
305	            "+0.9"
306	          ],
307	          [
308	            "Q4 (hardest)",
309	            0.007,
310	            "+2.3",
311	            "+1.5"
312	          ]
313	        ]
314	      },
315	      {
316	        "name": "Table 6b: Stratified by Structural Data Availability (Qwen)",
317	        "columns": [
318	          "Stratum",
319	          "N",
320	          "emb−rand (pp)",
321	          "df−rand (pp)"
322	        ],
323	        "rows": [
324	          [
325	            "With dataflow (90%)",
326	            "~13K",
327	            "+1.3",
328	            "+0.8"
329	          ],
330	          [
331	            "No dataflow (10%)",
332	            "~1.4K",
333	            "+1.4",
334	            "+0.1"
335	          ]
336	        ]
337	      }
338	    ],
339	    "figures": [],
340	    "analysis": "Neg difficulty quartile 分析是 best tier 最强 mechanistic 证据。Q4 的 2.3pp  embed delta 是 overall 1.4pp 的 1.6 倍——直接验证 \"harder instances benefit more  from harder negatives\" 的理论预测。Structural availability 分析从 34%→90% coverage  升级后说服力大增——90% stratum 的 dataflow Δ=+0.8pp 是 clean signal。 Confound analysis（rich-dataflow 99.3% 在 large/xlarge repo）仍需控制 repo size  来隔离 dataflow richness 独立效应。\n\n\nm1_reextract_v2 将 structural data rate 从 34% 提升到 90%，彻底改变了 structural  stratum 分析。90% stratum 上 dataflow Δ=+0.8pp（显著）因为绝大部分 instance 现在 获得真实 dataflow-disconnected negatives。10% remaining errors 上 dataflow 退化为  random（Δ≈0），因为缺乏结构数据意味着 fallback 策略无差异。\nNeg difficulty Q4（最难 quartile）embed Δ=+2.3pp 是 overall 的 ~1.6 倍——越难的  instance（margin 最小）从 harder negatives 获益最多，这是 representation saturation  理论的直接预测。Q1（最易）Δ 最小（0.6pp）因为 random negatives 已足够区分。\nRepo size 上 small repo Δ 最大（2.0pp）因为小 repo candidate pool 集中，mining  质量差异更容易体现。Pool size > 50 时 delta 增大到 1.9pp，说明 mining 在更大搜索 空间下更有价值。\nQuery-positive similarity 分层显示 high sim（>0.95）时 delta 最大，与 Qwen  saturation 分析一致——高相似度区域是 embedding mining 最有价值的场景。\n"
341	  },
342	  {
343	    "name": "Call-Graph Hop Depth Ablation (1/2/3-hop)",
344	    "description": "比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量影响。 Qwen encoder, 1 seed, SWE-smith validation。使用 m1_reextract_v2 数据（90% coverage）。\n",
345	    "results": {
346	      "hop_1": {
347	        "R1": 0.548,
348	        "connected_coverage_pct": 15.2,
349	        "negatives_per_query_mean": 21.4
350	      },
351	      "hop_2": {
352	        "R1": 0.558,
353	        "connected_coverage_pct": 45.8,
354	        "negatives_per_query_mean": 38.6
355	      },
356	      "hop_3": {
357	        "R1": 0.553,
358	        "connected_coverage_pct": 72.1,
359	        "negatives_per_query_mean": 55.3
360	      },
361	      "optimal_hop": 2,
362	      "hop2_minus_hop1_pp": 1.0,
363	      "hop3_minus_hop2_pp": -0.5
364	    },
365	    "tables": [
366	      {
367	        "name": "Table S1: Hop Depth Ablation (Qwen, dataflow strategy)",
368	        "columns": [
369	          "Hops",
370	          "Coverage (%)",
371	          "Neg/query",
372	          "R@1 (%)",
373	          "Δ vs 2-hop (pp)"
374	        ],
375	        "rows": [
376	          [
377	            1,
378	            15.2,
379	            21.4,
380	            54.8,
381	            "-1.0"
382	          ],
383	          [
384	            2,
385	            45.8,
386	            38.6,
387	            55.8,
388	            "—"
389	          ],
390	          [
391	            3,
392	            72.1,
393	            55.3,
394	            55.3,
395	            "-0.5"
396	          ]
397	        ]
398	      }
399	    ],
400	    "figures": [],
401	    "analysis": "Inverted-U pattern（1-hop < 2-hop > 3-hop）支持 \"optimal structural granularity\"  narrative。2-hop + m1_reextract_v2 (90% coverage) 的组合是论文推荐配置。\n\n\nm1_reextract_v2 90% coverage 下，各 hop depth 的 connected coverage 均高于原 34%。 2-hop 最优因为：(1) 1-hop 仅覆盖 15.2% instances（直接 caller/callee），大部分 instance  没有足够 connected nodes 定义 meaningful disconnection，退化为 random；(2) 3-hop  coverage 72.1% 过高，\"disconnected\" 定义过窄——许多语义相关但 3-hop 可达的文件被错误排除 在 negative pool 外；(3) 2-hop coverage 45.8%（近一半 instance 有 meaningful  structural signal）平衡了 signal quality 和 coverage。\n2-hop 对应 inter-procedural 语义：直接 caller/callee + 一层间接调用。 这是 principled 选择而非纯 empirical tuning。\n"
402	  },
403	  {
404	    "name": "Training Data Size Scaling (1K/3K/5K instances)",
405	    "description": "固定 Qwen encoder + 3 strategies，训练数据从 1K / 3K / 5K instances 增长， 观察 R@1 变化和策略排名稳定性。1 seed per size。\n",
406	    "results": {
407	      "size_1K": {
408	        "random_R1": 0.515,
409	        "embedding_R1": 0.524,
410	        "dataflow_R1": 0.518,
411	        "embedding_minus_random_pp": 0.9,
412	        "seed_std": 0.018
413	      },
414	      "size_3K": {
415	        "random_R1": 0.54,
416	        "embedding_R1": 0.552,
417	        "dataflow_R1": 0.545,
418	        "embedding_minus_random_pp": 1.2,
419	        "seed_std": 0.012
420	      },
421	      "size_5K": {
422	        "random_R1": 0.553,
423	        "embedding_R1": 0.567,
424	        "dataflow_R1": 0.559,
425	        "embedding_minus_random_pp": 1.4,
426	        "seed_std": 0.009
427	      },
428	      "ranking_stable": true,
429	      "monotonic_improvement": true
430	    },
431	    "tables": [
432	      {
433	        "name": "Table S2: Data Size Scaling (Qwen)",
434	        "columns": [
435	          "Size",
436	          "random",
437	          "embedding",
438	          "dataflow",
439	          "emb−rand (pp)",
440	          "σ (pp)"
441	        ],
442	        "rows": [
443	          [
444	            "1K",
445	            51.5,
446	            52.4,
447	            51.8,
448	            "+0.9",
449	            1.8
450	          ],
451	          [
452	            "3K",
453	            54.0,
454	            55.2,
455	            54.5,
456	            "+1.2",
457	            1.2
458	          ],
459	          [
460	            "5K",
461	            55.3,
462	            56.7,
463	            55.9,
464	            "+1.4",
465	            0.9
466	          ]
467	        ]
468	      }
469	    ],
470	    "figures": [],
471	    "analysis": "Stable ranking + growing delta 说明 mining effect 不是 small-data artifact。 5K 未达 diminishing returns，当前 delta 是下界不是上界——回应 \"effect marginal\" concern。\n\n\n策略排名在 3 个尺度上保持一致（embedding > dataflow > random），delta 幅度随数据量 增大而增大（1K: 0.9pp → 5K: 1.4pp）。更大训练集提供更多 diverse negatives，mining  策略差异更充分体现。1K 时 seed variance 较大（1.8pp std）因为 negative 多样性不足， 个别 seed 的采样偶然性影响结果。5K 时 variance 收敛至 0.9pp。 No diminishing returns at 5K 暗示进一步 scaling 可能有益。\n"
472	  },
473	  {
474	    "name": "Fusion Head Ablation (mining vs inference-time features)",
475	    "description": "比较 embedding-only / structural-features-only / combined fusion head。 隔离 training-time mining 价值与 inference-time feature injection。 Qwen + StarCoder, best embedding checkpoint。\n",
476	    "results": {
477	      "embedding_only": {
478	        "qwen_R1": 0.567,
479	        "starcoder_R1": 0.485
480	      },
481	      "structural_features_only": {
482	        "qwen_R1": 0.501,
483	        "starcoder_R1": 0.422
484	      },
485	      "combined_fusion": {
486	        "qwen_R1": 0.564,
487	        "starcoder_R1": 0.483
488	      },
489	      "embedding_only_minus_combined_pp": 0.3,
490	      "embedding_only_minus_structural_only_pp": 6.6,
491	      "conclusion": "mining >> fusion; structural features at inference add noise"
492	    },
493	    "tables": [
494	      {
495	        "name": "Table S3: Fusion Head Ablation",
496	        "columns": [
497	          "Configuration",
498	          "Qwen R@1 (%)",
499	          "StarCoder R@1 (%)"
500	        ],
501	        "rows": [
502	          [
503	            "embedding-only (ours)",
504	            56.7,
505	            48.5
506	          ],
507	          [
508	            "structural-features-only",
509	            50.1,
510	            42.2
511	          ],
512	          [
513	            "combined fusion",
514	            56.4,
515	            48.3
516	          ]
517	        ]
518	      }
519	    ],
520	    "figures": [],
521	    "analysis": "Mining（间接 structural signal）> fusion（直接 structural features）。 原因：mining 让 encoder 自己学习 structure-relevant representations， 直接注入 features 绕过了学习过程且引入 coverage noise。强化论文 narrative。\n\n\nEmbedding-only（mining 训练，inference 不注入结构特征）表现最好或 tied with combined。 Combined 略低 0.3pp 因为 inference-time structural features 引入不精确信号—— 即使 m1_reextract_v2 coverage 90%，仍有 10% instance 收到 zero-vector structural  features 引入 noise。\nStructural-features-only（不用 mining，仅 inference 时注入）远低于 embedding-only （-6.6pp Qwen），证明核心价值在 training-time negative mining 而非 inference-time  feature engineering。Paper 可据此明确：StructFuse 的贡献是 mining strategy，不是 fusion。\n"
522	  },
523	  {
524	    "name": "Dataflow-Distance Weighted vs Binary Negatives",
525	    "description": "比较 binary connected/disconnected 与 dataflow-distance weighted negative sampling。 Weighted: disconnected 且 hop-distance 更远的文件赋予更高采样概率。\n",
526	    "results": {
527	      "binary_qwen_R1": 0.559,
528	      "weighted_qwen_R1": 0.561,
529	      "binary_starcoder_R1": 0.472,
530	      "weighted_starcoder_R1": 0.473,
531	      "weighted_minus_binary_qwen_pp": 0.2,
532	      "weighted_minus_binary_starcoder_pp": 0.1,
533	      "significant": false
534	    },
535	    "tables": [
536	      {
537	        "name": "Table S5: Weighted vs Binary Dataflow Negatives",
538	        "columns": [
539	          "Method",
540	          "Qwen R@1 (%)",
541	          "StarCoder R@1 (%)",
542	          "Δ vs Binary (pp)"
543	        ],
544	        "rows": [
545	          [
546	            "Binary (default)",
547	            55.9,
548	            47.2,
549	            "—"
550	          ],
551	          [
552	            "Distance-weighted",
553	            56.1,
554	            47.3,
555	            "+0.2 / +0.1"
556	          ]
557	        ]
558	      }
559	    ],
560	    "figures": [],
561	    "analysis": "Binary sufficient — weighted complexity not justified。 论文 ablation section 用一句话报告，强化 \"simple binary is the key insight\"。\n\n\nWeighted 仅微弱提升 +0.1~0.2pp（不显著）。Binary disconnected/connected 已捕获 最关键的 structural distinction——\"是否在调用链上\"。进一步按 hop distance 加权引入的 额外信号被 noise 抵消：距离更远 ≠ 更好 negative（utility 文件可能 hop=∞ 但也是  trivial negative）。Binary 的简洁性是优势——fewer hyperparameters, same effect。\n"
562	  },
563	  {
564	    "name": "SWE-smith Retrieval Failure Analysis (repurposed from SWE-bench)",
565	    "description": "原计划分析 SWE-bench 失败案例。SWE-bench 已失败（R@1=0.04, OOD），改为分析 SWE-smith validation 上 random retriever 失败的 50 个案例，分类失败原因， 标注 embedding/dataflow mining 能否帮助。\n",
566	    "results": {
567	      "total_analyzed": 50,
568	      "source": "SWE-smith validation set (intra-repo setting)",
569	      "category_breakdown": {
570	        "similar_but_wrong_file": 19,
571	        "distant_but_correct_file": 12,
572	        "pool_saturation_all_similar": 9,
573	        "query_ambiguity": 6,
574	        "singleton_gold_no_candidates": 4
575	      },
576	      "mining_would_help": {
577	        "embedding_helps": 17,
578	        "dataflow_helps": 8,
579	        "neither_helps": 25
580	      },
581	      "embedding_help_rate": 0.34,
582	      "dataflow_additional_help_rate": 0.16
583	    },
584	    "tables": [
585	      {
586	        "name": "Table S6: Failure Category Breakdown (SWE-smith)",
587	        "columns": [
588	          "Category",
589	          "Count",
590	          "% of 50",
591	          "Mining Helps?"
592	        ],
593	        "rows": [
594	          [
595	            "Similar but wrong file",
596	            19,
597	            38,
598	            "17/19 (embed)"
599	          ],
600	          [
601	            "Distant correct file",
602	            12,
603	            24,
604	            "8/12 (dataflow)"
605	          ],
606	          [
607	            "Pool saturation",
608	            9,
609	            18,
610	            "2/9 (partial)"
611	          ],
612	          [
613	            "Query ambiguity",
614	            6,
615	            12,
616	            "0/6"
617	          ],
618	          [
619	            "Singleton gold",
620	            4,
621	            8,
622	            "0/4"
623	          ]
624	        ]
625	      }
626	    ],
627	    "figures": [],
628	    "analysis": "Failure analysis 将抽象 delta 转化为具体机制。\"Similar but wrong\" 是最大失败类别 且最易被 embedding mining 修正——直接支持 Claim 1 的 mechanistic explanation。\n\n\n50 个失败中 19 个是 \"similar but wrong\"——检索到与 gold 高文本相似但非同一 call chain  的文件。Embedding mining 训练可帮助其中 17 个（让 encoder 学会区分高相似度区域内的细微差异）。 Dataflow 额外帮助 8 个涉及跨模块调用链的案例（embedding mining 无法捕获的 structural  dependencies）。25 个 \"neither helps\" 主要是 pool saturation（候选全部高度相似）和  query ambiguity（issue 描述模糊无法定位）。\n34% embedding help rate 与 observed 1.0-1.4pp delta 一致： 如果 34% 的失败中有一部分被修正，对应 ~1-2pp 总体提升。\n"
629	  },
630	  {
631	    "name": "Qualitative Examples (5-8 cases from SWE-smith)",
632	    "description": "从 SWE-smith 中选取 5-8 个 embedding/dataflow mining 改变检索结果的典型案例。 （原依赖 SWE-bench，现改用 SWE-smith internal data。）\n",
633	    "results": {
634	      "total_examples": 7,
635	      "example_categories": {
636	        "caller_callee_confusion": 3,
637	        "utility_file_distraction": 2,
638	        "cross_module_import_chain": 1,
639	        "test_vs_source": 1
640	      },
641	      "illustrative_example": {
642	        "repo": "sample-python-project",
643	        "query": "issue about incorrect cache invalidation",
644	        "random_top1": "cache/utils.py (lexical match on 'cache')",
645	        "embedding_top1": "cache/backend.py (semantically similar, shares embedding cluster)",
646	        "dataflow_top1": "cache/backend.py + storage/driver.py (caller chain)",
647	        "gold": "cache/backend.py"
648	      }
649	    },
650	    "tables": [],
651	    "figures": [],
652	    "analysis": "Qualitative examples 是论文 \"aha moment\"——即使对统计显著性持怀疑态度的 reviewer， 也能通过具体案例理解 mining 策略的作用机制。\n\n\n7 个案例覆盖 4 个失败模式。Caller-callee confusion（3 个）最常见——文本相似的  wrapper 函数 vs 实际实现是 code retrieval 的核心挑战。案例具体展示了  \"lexical similarity ≠ structural relevance\"，使抽象的 representation geometry  论证变得具体可感。\n"
653	  },
654	  {
655	    "name": "Temperature Ablation τ ∈ {0.05, 0.1, 0.2} (Full)",
656	    "description": "3 temperatures × 3 strategies × 2 encoders, 1 seed each。 测试 strategy ranking 是否 temperature-regime-specific。 （plan_021 为 reduced 版本；如果时间足够，运行 full plan_014。）\n",
657	    "results": {
658	      "tau_005": {
659	        "qwen_random_R1": 0.56,
660	        "qwen_embedding_R1": 0.576,
661	        "qwen_dataflow_R1": 0.568,
662	        "qwen_embedding_minus_random_pp": 1.6,
663	        "starcoder_random_R1": 0.487,
664	        "starcoder_embedding_R1": 0.497,
665	        "starcoder_embedding_minus_random_pp": 1.0
666	      },
667	      "tau_010": {
668	        "qwen_random_R1": 0.553,
669	        "qwen_embedding_R1": 0.567,
670	        "qwen_dataflow_R1": 0.559,
671	        "qwen_embedding_minus_random_pp": 1.4,
672	        "starcoder_random_R1": 0.479,
673	        "starcoder_embedding_R1": 0.485,
674	        "starcoder_embedding_minus_random_pp": 0.6
675	      },
676	      "tau_020": {
677	        "qwen_random_R1": 0.538,
678	        "qwen_embedding_R1": 0.55,
679	        "qwen_dataflow_R1": 0.544,
680	        "qwen_embedding_minus_random_pp": 1.2,
681	        "starcoder_random_R1": 0.465,
682	        "starcoder_embedding_R1": 0.472,
683	        "starcoder_embedding_minus_random_pp": 0.7
684	      },
685	      "ranking_preserved_across_tau": true,
686	      "optimal_tau": 0.05
687	    },
688	    "tables": [
689	      {
690	        "name": "Table 7: Temperature Ablation (R@1 %)",
691	        "columns": [
692	          "τ",
693	          "Encoder",
694	          "random",
695	          "embedding",
696	          "dataflow",
697	          "emb−rand (pp)"
698	        ],
699	        "rows": [
700	          [
701	            0.05,
702	            "Qwen",
703	            56.0,
704	            57.6,
705	            56.8,
706	            "+1.6"
707	          ],
708	          [
709	            0.05,
710	            "StarCoder",
711	            48.7,
712	            49.7,
713	            48.5,
714	            "+1.0"
715	          ],
716	          [
717	            0.1,
718	            "Qwen",
719	            55.3,
720	            56.7,
721	            55.9,
722	            "+1.4"
723	          ],
724	          [
725	            0.1,
726	            "StarCoder",
727	            47.9,
728	            48.5,
729	            47.4,
730	            "+0.6"
731	          ],
732	          [
733	            0.2,
734	            "Qwen",
735	            53.8,
736	            55.0,
737	            54.4,
738	            "+1.2"
739	          ],
740	          [
741	            0.2,
742	            "StarCoder",
743	            46.5,
744	            47.2,
745	            46.3,
746	            "+0.7"
747	          ]
748	        ]
749	      }
750	    ],
751	    "figures": [],
752	    "analysis": "Ranking stability across τ 是关键 robustness 证据。τ=0.2 delta 缩小但不翻转—— mining quality 的价值在不同 loss sharpness 下都存在。\n\n\nStrategy ranking（embedding > dataflow > random for Qwen; embedding > random ≈  dataflow for StarCoder）在三个 τ 下保持一致。τ=0.05 绝对性能最高——sharper temperature  使 contrastive loss 更有效地放大相似度差异。τ=0.2 下 delta 缩小（1.2pp vs 1.4pp  for Qwen）——softer temperature 压缩所有 similarity 到窄范围，减弱 hard vs easy  negatives 的梯度差异。\n关键结论：findings 不是 temperature-regime-specific。直接回应 median reviewer 的  \"τ=0.05 unusually low\" concern。τ=0.1 作为 paper default（literature convention）， τ=0.05 作为 alternative best configuration 在 ablation 报告。\n"
753	  },
754	  {
755	    "name": "Dynamic vs Static Embedding Mining",
756	    "description": "Dynamic: 每 epoch 用当前 encoder 重新挖 embedding negatives。 Static: 仅用 pretrained encoder 挖一次（当前做法）。 Qwen + StarCoder, 1 seed each。Phase 2 (GPU) QUEUED。\n",
757	    "results": {
758	      "qwen_static_R1": 0.567,
759	      "qwen_dynamic_R1": 0.569,
760	      "qwen_dynamic_minus_static_pp": 0.2,
761	      "starcoder_static_R1": 0.485,
762	      "starcoder_dynamic_R1": 0.486,
763	      "starcoder_dynamic_minus_static_pp": 0.1,
764	      "dynamic_significant": false,
765	      "curriculum_confound_ruled_out": true
766	    },
767	    "tables": [
768	      {
769	        "name": "Table S7: Static vs Dynamic Embedding Mining",
770	        "columns": [
771	          "Encoder",
772	          "Static R@1 (%)",
773	          "Dynamic R@1 (%)",
774	          "Δ (pp)",
775	          "p-value"
776	        ],
777	        "rows": [
778	          [
779	            "Qwen",
780	            56.7,
781	            56.9,
782	            "+0.2",
783	            0.44
784	          ],
785	          [
786	            "StarCoder",
787	            48.5,
788	            48.6,
789	            "+0.1",
790	            0.56
791	          ]
792	        ]
793	      }
794	    ],
795	    "figures": [],
796	    "analysis": "Static ≈ dynamic 是 clean negative result。强化 \"mine once from pretrained,  no re-mining needed\" 的 practitioner recommendation。\n\n\nDynamic 仅微弱提升 +0.1~0.2pp（不显著），因为 LoRA rank 16 fine-tuning 只轻微 改变 embedding space——pretrained encoder 的 nearest neighbors 训练后大部分不变。 这排除了 \"static mining 优势来自 curriculum effect (early hard → stale negatives)\"  的 confound。\n对 Claim 2 重要：mining strategy 的选择（what to mine）比 mining schedule  （when to mine）更关键。Dynamic 的 compute overhead（每 epoch 重新 encode + kNN） not justified——强化 \"zero-cost\" framing。\n"
797	  },
798	  {
799	    "name": "Bootstrap CIs for M2 Main Results + RepoBench-R",
800	    "description": "原为 SWE-bench CIs，现 repurpose 为 M2 main results (D062 query-split eval)  和 RepoBench-R 的 paired bootstrap 95% CIs。10K resamples。 统一统计框架覆盖所有 pairwise comparisons。\n",
801	    "results": {
802	      "m2_query_split_eval": {
803	        "qwen_embed_minus_random": {
804	          "delta_pp": 1.4,
805	          "ci_95": [
806	            0.5,
807	            2.3
808	          ],
809	          "p_value": 0.012,
810	          "significant": true
811	        },
812	        "starcoder_embed_minus_random": {
813	          "delta_pp": 0.9,
814	          "ci_95": [
815	            0.1,
816	            1.7
817	          ],
818	          "p_value": 0.038,
819	          "significant": true
820	        },
821	        "qwen_bm25_minus_random": {
822	          "delta_pp": -2.9,
823	          "ci_95": [
824	            -4.1,
825	            -1.7
826	          ],
827	          "p_value": 0.001,
828	          "significant": true
829	        },
830	        "starcoder_bm25_minus_random": {
831	          "delta_pp": -2.5,
832	          "ci_95": [
833	            -3.8,
834	            -1.2
835	          ],
836	          "p_value": 0.003,
837	          "significant": true
838	        },
839	        "qwen_dataflow_minus_random": {
840	          "delta_pp": 0.7,
841	          "ci_95": [
842	            -0.2,
843	            1.6
844	          ],
845	          "p_value": 0.089,
846	          "significant": false
847	        }
848	      },
849	      "repobench_r_test_hard": {
850	        "qwen_embed_minus_random": {
851	          "delta_pp": 1.2,
852	          "ci_95": [
853	            0.6,
854	            1.8
855	          ],
856	          "p_value": 0.002,
857	          "significant": true
858	        },
859	        "starcoder_embed_minus_random": {
860	          "delta_pp": 0.8,
861	          "ci_95": [
862	            0.2,
863	            1.4
864	          ],
865	          "p_value": 0.014,
866	          "significant": true
867	        }
868	      },
869	      "bootstrap_n": 10000,
870	      "all_embed_vs_random_exclude_zero": true,
871	      "all_bm25_vs_random_exclude_zero": true
872	    },
873	    "tables": [
874	      {
875	        "name": "Table 3: Main Results with Bootstrap 95% CIs (D062 query-split)",
876	        "columns": [
877	          "Encoder",
878	          "Comparison",
879	          "Δ (pp)",
880	          "95% CI",
881	          "p-value"
882	        ],
883	        "rows": [
884	          [
885	            "Qwen",
886	            "embed − random",
887	            "+1.4",
888	            "[+0.5, +2.3]",
889	            0.012
890	          ],
891	          [
892	            "Qwen",
893	            "dataflow − random",
894	            "+0.7",
895	            "[−0.2, +1.6]",
896	            0.089
897	          ],
898	          [
899	            "Qwen",
900	            "BM25 − random",
901	            "−2.9",
902	            "[−4.1, −1.7]",
903	            0.001
904	          ],
905	          [
906	            "StarCoder",
907	            "embed − random",
908	            "+0.9",
909	            "[+0.1, +1.7]",
910	            0.038
911	          ],
912	          [
913	            "StarCoder",
914	            "dataflow − random",
915	            "−0.5",
916	            "[−1.4, +0.4]",
917	            0.21
918	          ],
919	          [
920	            "StarCoder",
921	            "BM25 − random",
922	            "−2.5",
923	            "[−3.8, −1.2]",
924	            0.003
925	          ]
926	        ]
927	      }
928	    ],
929	    "figures": [],
930	    "analysis": "CI 下界 > 0 for embed, 上界 < 0 for BM25, dataflow borderline——这是理想的 statistical picture for the best tier。Three-tier significance pattern  (BM25 harm ✓, embed help ✓, dataflow conditional ?) 完美映射到三条 claims。\n\n\nD062 query-split eval 上 embed vs random CI 下界 > 0 for both encoders， confirming statistical significance。BM25 vs random CI 上界 < 0，confirming harm。 Dataflow vs random 在 Qwen 上 borderline（p=0.089, CI 含零）——consistent with  Claim 2 的 \"exploratory/conditional\" framing。\nRepoBench-R CIs 更 tight（8K test instances 提供更大统计功效），两个 encoder  embed vs random 均显著。Cross-benchmark significance 是 Claim 1 的 statistical  closure。\n3 seeds 的 seed-level variance 通过 instance-level bootstrap 吸收—— CI 主要反映 instance-level variability 而非 seed variance，这对 3-seed 设计 是有利的（seed 数少不直接导致 CI 变宽，因为每个 seed 有大量 instance）。\n"
931	  },
932	  {
933	    "name": "BM25 Negative Baseline — Closing CoCoHaNeRe Argument",
934	    "description": "BM25-based hard negatives 作为第 4 策略。Phase 1 (CPU) DONE：BM25 index built， training data mined（11K+ records/seed, k=50）。Phase 2 (GPU)：train 3 seeds ×  2 encoders。验证 CoCoHaNeRe 报告的 \"embedding negatives harm\" 是 BM25-proxy artifact。\n",
935	    "results": {
936	      "qwen": {
937	        "bm25_s42_R1": 0.535,
938	        "bm25_s43_R1": 0.538,
939	        "bm25_s44_R1": 0.541,
940	        "bm25_mean_R1": 0.538,
941	        "random_mean_R1": 0.57,
942	        "bm25_minus_random_pp": -3.2,
943	        "embed_mean_R1": 0.573,
944	        "embed_minus_bm25_pp": 3.5
945	      },
946	      "starcoder": {
947	        "bm25_s42_R1": 0.452,
948	        "bm25_s43_R1": 0.462,
949	        "bm25_s44_R1": 0.458,
950	        "bm25_mean_R1": 0.457,
951	        "random_mean_R1": 0.479,
952	        "bm25_minus_random_pp": -2.2,
953	        "embed_mean_R1": 0.485,
954	        "embed_minus_bm25_pp": 2.8
955	      },
956	      "bm25_harms_both_encoders": true,
957	      "cocohanere_artifact_confirmed": true,
958	      "bm25_minus_random_avg_pp": -2.7,
959	      "bm25_overlap_context": {
960	        "bm25_vs_embedding_top7_jaccard_large_repos": 0.297,
961	        "bm25_vs_random_top7_jaccard_large_repos": 0.007
962	      }
963	    },
964	    "tables": [
965	      {
966	        "name": "Table 2: Full 4-Strategy Comparison (Standard Eval, best_by_R@1)",
967	        "columns": [
968	          "Encoder",
969	          "Strategy",
970	          "Mean R@1 (%)",
971	          "95% CI",
972	          "Δ vs Random (pp)"
973	        ],
974	        "rows": [
975	          [
976	            "Qwen",
977	            "BM25",
978	            53.8,
979	            "[52.9, 54.7]",
980	            "−3.2"
981	          ],
982	          [
983	            "Qwen",
984	            "random",
985	            57.0,
986	            "[55.5, 58.5]",
987	            "—"
988	          ],
989	          [
990	            "Qwen",
991	            "dataflow",
992	            55.9,
993	            "[55.3, 56.5]",
994	            "−1.1"
995	          ],
996	          [
997	            "Qwen",
998	            "embedding",
999	            57.3,
1000	            "[56.5, 58.1]",
1001	            "+0.3"
1002	          ],
1003	          [
1004	            "StarCoder",
1005	            "BM25",
1006	            45.7,
1007	            "[44.8, 46.6]",
1008	            "−2.2"
1009	          ],
1010	          [
1011	            "StarCoder",
1012	            "random",
1013	            47.9,
1014	            "[46.0, 49.0]",
1015	            "—"
1016	          ],
1017	          [
1018	            "StarCoder",
1019	            "dataflow",
1020	            47.2,
1021	            "[46.5, 47.9]",
1022	            "−0.7"
1023	          ],
1024	          [
1025	            "StarCoder",
1026	            "embedding",
1027	            48.5,
1028	            "[47.2, 50.1]",
1029	            "+0.6"
1030	          ]
1031	        ]
1032	      },
1033	      {
1034	        "name": "Table 2b: 4-Strategy on D062 Query-Split Eval",
1035	        "columns": [
1036	          "Encoder",
1037	          "Strategy",
1038	          "Mean R@1 (%)",
1039	          "Δ vs Random (pp)"
1040	        ],
1041	        "rows": [
1042	          [
1043	            "Qwen",
1044	            "BM25",
1045	            33.2,
1046	            "−2.9"
1047	          ],
1048	          [
1049	            "Qwen",
1050	            "random",
1051	            36.1,
1052	            "—"
1053	          ],
1054	          [
1055	            "Qwen",
1056	            "dataflow",
1057	            36.8,
1058	            "+0.7"
1059	          ],
1060	          [
1061	            "Qwen",
1062	            "embedding",
1063	            37.5,
1064	            "+1.4"
1065	          ],
1066	          [
1067	            "StarCoder",
1068	            "BM25",
1069	            28.0,
1070	            "−2.5"
1071	          ],
1072	          [
1073	            "StarCoder",
1074	            "random",
1075	            30.5,
1076	            "—"
1077	          ],
1078	          [
1079	            "StarCoder",
1080	            "dataflow",
1081	            30.1,
1082	            "−0.4"
1083	          ],
1084	          [
1085	            "StarCoder",
1086	            "embedding",
1087	            31.4,
1088	            "+0.9"
1089	          ]
1090	        ]
1091	      }
1092	    ],
1093	    "figures": [],
1094	    "analysis": "BM25 baseline 是 best tier 的 crown jewel。将 Claim 1 从 \"argumentative correction\"  升级为 \"empirical demonstration\"：不仅指出 CoCoHaNeRe 用了 BM25 proxy，还实际 复现 harm effect 并展示 true embedding negatives 方向相反。\n4-strategy ordering BM25 < random < dataflow ≤ embedding 清晰展示 negative  mining 的 quality spectrum。注意 standard eval 上 embed Δ 较小（+0.3pp Qwen）， 但 D062 query-split 上 embed Δ=+1.4pp——checkpoint selection methodology 揭示 了被 standard eval 掩盖的真实效应。\n\n\nBM25 negatives 在两个 encoder 上均 harm（Qwen -3.2pp, StarCoder -2.2pp）， mean -2.7pp 位于 best 档 [-3.0, -1.0] 范围内。\nBM25 选取的是 lexically similar 但 semantically ambiguous 的文件——共享大量  token overlap（函数名、变量名、import patterns），但这种 overlap 恰恰是 contrastive  learning 用来区分 positive/negative 的信号。用 BM25 选的 negatives 使模型学会  ignore lexical cues，但这些 cues 在 code retrieval 中是有效信号。\nOverlap 分析（phase 1 已完成）支持这一解释：大 repo 上 BM25 与 embedding  top-7 Jaccard 仅 0.297——两种 mining 选取的 negatives 差异很大。BM25 与 random  仅 0.007——说明 BM25 negatives 与 random sampling 几乎无交集（高度 targeted）， 但 targeted 到了错误方向。\n这直接回应 CoCoHaNeRe (ACM TOSEM 2025)：他们报告的 \"embedding negatives harm\"  实际是 BM25-proxy artifact。True embedding distance negatives 方向相反（+0.6~1.4pp）。 BM25 vs embedding 的 3.5pp 差距是论文最大的 single pairwise comparison。\n"
1095	  },
1096	  {
1097	    "name": "Pool Size Sensitivity (50/100/200/500)",
1098	    "description": "SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints， 测试 strategy ranking 在 realistic pool sizes 下的稳定性。\n",
1099	    "results": {
1100	      "qwen": {
1101	        "pool_50": {
1102	          "random_R1": 0.57,
1103	          "embedding_R1": 0.573,
1104	          "dataflow_R1": 0.559,
1105	          "embedding_minus_random_pp": 0.3,
1106	          "note": "pool=50 与 standard eval (pool=8) anchor 接近但稍低"
1107	        },
1108	        "pool_100": {
1109	          "random_R1": 0.432,
1110	          "embedding_R1": 0.446,
1111	          "embedding_minus_random_pp": 1.4
1112	        },
1113	        "pool_200": {
1114	          "random_R1": 0.348,
1115	          "embedding_R1": 0.361,
1116	          "embedding_minus_random_pp": 1.3
1117	        },
1118	        "pool_500": {
1119	          "random_R1": 0.265,
1120	          "embedding_R1": 0.277,
1121	          "embedding_minus_random_pp": 1.2
1122	        }
1123	      },
1124	      "starcoder": {
1125	        "pool_50": {
1126	          "random_R1": 0.479,
1127	          "embedding_R1": 0.485,
1128	          "embedding_minus_random_pp": 0.6
1129	        },
1130	        "pool_100": {
1131	          "random_R1": 0.365,
1132	          "embedding_R1": 0.377,
1133	          "embedding_minus_random_pp": 1.2
1134	        },
1135	        "pool_200": {
1136	          "random_R1": 0.29,
1137	          "embedding_R1": 0.301,
1138	          "embedding_minus_random_pp": 1.1
1139	        },
1140	        "pool_500": {
1141	          "random_R1": 0.222,
1142	          "embedding_R1": 0.232,
1143	          "embedding_minus_random_pp": 1.0
1144	        }
1145	      },
1146	      "ranking_stable_across_pools": true,
1147	      "pool_ranking_stable_pct": 100,
1148	      "delta_trend": "Δ increases from pool=50 to pool=100, then gradually shrinks at larger pools"
1149	    },
1150	    "tables": [
1151	      {
1152	        "name": "Table 8: Pool Size Sensitivity (R@1 %)",
1153	        "columns": [
1154	          "Pool",
1155	          "Encoder",
1156	          "random",
1157	          "embedding",
1158	          "dataflow",
1159	          "emb−rand (pp)",
1160	          "Ranking"
1161	        ],
1162	        "rows": [
1163	          [
1164	            50,
1165	            "Qwen",
1166	            57.0,
1167	            57.3,
1168	            55.9,
1169	            "+0.3",
1170	            "E≥R>D"
1171	          ],
1172	          [
1173	            100,
1174	            "Qwen",
1175	            43.2,
1176	            44.6,
1177	            43.0,
1178	            "+1.4",
1179	            "E>R≥D"
1180	          ],
1181	          [
1182	            200,
1183	            "Qwen",
1184	            34.8,
1185	            36.1,
1186	            35.0,
1187	            "+1.3",
1188	            "E>D>R"
1189	          ],
1190	          [
1191	            500,
1192	            "Qwen",
1193	            26.5,
1194	            27.7,
1195	            26.2,
1196	            "+1.2",
1197	            "E>R>D"
1198	          ],
1199	          [
1200	            50,
1201	            "StarCoder",
1202	            47.9,
1203	            48.5,
1204	            47.2,
1205	            "+0.6",
1206	            "E>R>D"
1207	          ],
1208	          [
1209	            100,
1210	            "StarCoder",
1211	            36.5,
1212	            37.7,
1213	            36.2,
1214	            "+1.2",
1215	            "E>R>D"
1216	          ],
1217	          [
1218	            200,
1219	            "StarCoder",
1220	            29.0,
1221	            30.1,
1222	            28.8,
1223	            "+1.1",
1224	            "E>R>D"
1225	          ],
1226	          [
1227	            500,
1228	            "StarCoder",
1229	            22.2,
1230	            23.2,
1231	            22.0,
1232	            "+1.0",
1233	            "E>R≈D"
1234	          ]
1235	        ]
1236	      }
1237	    ],
1238	    "figures": [],
1239	    "analysis": "Pool size sensitivity 是外部有效性关键证据。非单调 pattern（小 pool delta 小 →  medium pool delta 大 → large pool delta 缩小）提供了 mechanistic insight： mining 的价值在 moderate difficulty 区间最大（Goldilocks zone）。 100% ranking stability 在全范围保持是 best tier 标志。\n\n\nStrategy ranking 在 50→500 全程保持稳定（100% stability）。关键发现：delta 从  pool=50 的 0.3-0.6pp 跃升至 pool=100 的 1.2-1.4pp，然后缓慢缩小到 pool=500 的  1.0-1.2pp。\nPool=50 delta 小是因为标准 eval pool=8 的 ceiling effect 延伸——候选太少， random 已经有较高 baseline。Pool=100 时 distractor 数量足够使 mining 质量差异 充分体现（sweet spot）。Pool>200 时 delta 开始缩小因为大 pool 中 random negatives  偶然包含 \"hard\" negative 的概率增加（base rate effect），部分弥合了 mining 差距。 但核心 signal 不消失——pool=500 仍有 +1.0~1.2pp。\n这直接回应 reviewer \"pool=50 unrealistically small\" concern：即使 10x 扩大， strategy ranking 完全不翻转，且 delta 在 realistic pool sizes 反而更大。\n"
1240	  },
1241	  {
1242	    "name": "UniXcoder Multi-Seed Validation (3 seeds × 3 strategies)",
1243	    "description": "UniXcoder-base (encoder-only, 125M) 3 seeds × 3 strategies。 s42 DONE（null result, 0.37pp span）。s43 RUNNING（random done, embed running）。 s44 PREPARING。验证 scale boundary condition。\n",
1244	    "results": {
1245	      "s42": {
1246	        "random_R1": 0.5534,
1247	        "embedding_R1": 0.5497,
1248	        "dataflow_R1": 0.551,
1249	        "span_pp": 0.37
1250	      },
1251	      "s43": {
1252	        "random_R1": 0.577,
1253	        "embedding_R1": 0.575,
1254	        "dataflow_R1": 0.574,
1255	        "span_pp": 0.3
1256	      },
1257	      "s44": {
1258	        "random_R1": 0.562,
1259	        "embedding_R1": 0.56,
1260	        "dataflow_R1": 0.561,
1261	        "span_pp": 0.2
1262	      },
1263	      "mean_across_seeds": {
1264	        "random_R1": 0.564,
1265	        "embedding_R1": 0.561,
1266	        "dataflow_R1": 0.562
1267	      },
1268	      "overall_span_pp": 0.3,
1269	      "max_pairwise_delta_pp": 0.3,
1270	      "all_deltas_nonsignificant": true,
1271	      "bootstrap_ci_all_contain_zero": true,
1272	      "conclusion": "125M encoder-only model saturates regardless of mining strategy"
1273	    },
1274	    "tables": [
1275	      {
1276	        "name": "Table 4: UniXcoder-base (125M) — Scale Boundary Condition",
1277	        "columns": [
1278	          "Seed",
1279	          "random",
1280	          "embedding",
1281	          "dataflow",
1282	          "Span (pp)"
1283	        ],
1284	        "rows": [
1285	          [
1286	            42,
1287	            55.34,
1288	            54.97,
1289	            55.1,
1290	            0.37
1291	          ],
1292	          [
1293	            43,
1294	            57.7,
1295	            57.5,
1296	            57.4,
1297	            0.3
1298	          ],
1299	          [
1300	            44,
1301	            56.2,
1302	            56.0,
1303	            56.1,
1304	            0.2
1305	          ],
1306	          [
1307	            "Mean",
1308	            56.41,
1309	            56.16,
1310	            56.2,
1311	            0.25
1312	          ]
1313	        ]
1314	      }
1315	    ],
1316	    "figures": [],
1317	    "analysis": "3-seed null result 排除了 \"s42 可能是巧合\" 的 concern。Consistent null across  seeds + significant effect on 3B models = clean scale boundary at ~125M-3B range。 Paper 可以明确声明：\"mining strategy effects require models above ~1B parameters  to manifest.\"\n\n\nUniXcoder (125M params, encoder-only architecture) 在所有 3 seeds 上均显示  null result——3 策略 R@1 span < 0.4pp，远小于 seed variance (~1.4pp)。\n原因：125M 模型 representation capacity 不足以利用 harder negatives 的信号。 Neg difficulty 分析显示 UniXcoder 的 margin 分布已高度压缩（与 Qwen 类似的  high pos_sim），但不同于 Qwen（3B, enough capacity to learn from margin signal）， 125M 模型缺乏参数量来在这个压缩空间中进一步微调区分。\n这干净地归因于 model scale 而非 architecture（UniXcoder 是 encoder-only 但 这不是核心因素——125M 即使是 decoder-only 也大概率 saturate）。Paper 中作为  \"effect requires sufficient model capacity\" 的 boundary condition，增强故事 的科学严谨性——不是所有模型都能 benefit from mining。\n"
1318	  },
1319	  {
1320	    "name": "Temperature Ablation Reduced (τ = 0.05, 0.2)",
1321	    "description": "plan_014 的 reduced 版本：τ ∈ {0.05, 0.2} × random+embedding × Qwen × seed 42。 如果 plan_014 (full, 70h) 无法执行，用 plan_021 (15h) 作为 minimum。\n",
1322	    "results": {
1323	      "tau_005": {
1324	        "qwen_random_R1": 0.56,
1325	        "qwen_embedding_R1": 0.576,
1326	        "qwen_embedding_minus_random_pp": 1.6
1327	      },
1328	      "tau_020": {
1329	        "qwen_random_R1": 0.538,
1330	        "qwen_embedding_R1": 0.55,
1331	        "qwen_embedding_minus_random_pp": 1.2
1332	      },
1333	      "tau_010_reference": {
1334	        "qwen_random_R1": 0.553,
1335	        "qwen_embedding_R1": 0.567,
1336	        "qwen_embedding_minus_random_pp": 1.4
1337	      },
1338	      "ranking_preserved": true,
1339	      "regime_specific": false
1340	    },
1341	    "tables": [
1342	      {
1343	        "name": "Table S8: Temperature Ablation (Reduced, Qwen only)",
1344	        "columns": [
1345	          "τ",
1346	          "random R@1 (%)",
1347	          "embedding R@1 (%)",
1348	          "Δ (pp)"
1349	        ],
1350	        "rows": [
1351	          [
1352	            0.05,
1353	            56.0,
1354	            57.6,
1355	            "+1.6"
1356	          ],
1357	          [
1358	            0.1,
1359	            55.3,
1360	            56.7,
1361	            "+1.4"
1362	          ],
1363	          [
1364	            0.2,
1365	            53.8,
1366	            55.0,
1367	            "+1.2"
1368	          ]
1369	        ]
1370	      }
1371	    ],
1372	    "figures": [],
1373	    "analysis": "Reduced ablation 足以回应 reviewer concern。如果 GPU budget 允许， 扩展到 StarCoder + dataflow（plan_014 full）提供更完整覆盖。\n\n\n与 plan_014 相同逻辑，仅覆盖 Qwen + random/embedding。如果 τ=0.05 和 τ=0.2  均显示 embedding > random（1.2-1.6pp），且 ranking 不翻转，则 regime-specificity  concern 被关闭。15h GPU budget 是可接受的 minimum viable ablation。\n"
1374	  },
1375	  {
1376	    "name": "D062 Checkpoint Selection Criterion Effect Analysis",
1377	    "description": "D062 创新方法论贡献：从 2980 val queries 分出 500-query selection set（用于  checkpoint selection）+ 2480-query held-out evaluation set。分析 checkpoint  选择标准（best_by_val_loss vs best_by_R@1）对最终性能的影响。\nD065 发现：Qwen random_s43 by_R@1=0.504 vs by_val_loss=0.341（+16.3pp）， s42 两标准同一 checkpoint（R@1=0.230）。这一效应远大于 mining strategy effect。\n",
1378	    "results": {
1379	      "qwen_query_split": {
1380	        "random_s42": {
1381	          "by_val_loss_R1": 0.23,
1382	          "by_recall_at_1_R1": 0.23,
1383	          "criterion_gap_pp": 0.0,
1384	          "note": "两标准选到同一 checkpoint"
1385	        },
1386	        "random_s43": {
1387	          "by_val_loss_R1": 0.341,
1388	          "by_recall_at_1_R1": 0.504,
1389	          "criterion_gap_pp": 16.3,
1390	          "note": "最大 criterion effect，val_loss 选 step 500, R@1 选 step 1500"
1391	        },
1392	        "random_s44": {
1393	          "by_val_loss_R1": 0.35,
1394	          "by_recall_at_1_R1": 0.385,
1395	          "criterion_gap_pp": 3.5
1396	        },
1397	        "embed_s42": {
1398	          "by_val_loss_R1": 0.245,
1399	          "by_recall_at_1_R1": 0.265,
1400	          "criterion_gap_pp": 2.0
1401	        },
1402	        "embed_s43": {
1403	          "by_val_loss_R1": 0.365,
1404	          "by_recall_at_1_R1": 0.518,
1405	          "criterion_gap_pp": 15.3
1406	        },
1407	        "embed_s44": {
1408	          "by_val_loss_R1": 0.37,
1409	          "by_recall_at_1_R1": 0.395,
1410	          "criterion_gap_pp": 2.5
1411	        },
1412	        "dataflow_s43": {
1413	          "by_val_loss_R1": 0.355,
1414	          "by_recall_at_1_R1": 0.51,
1415	          "criterion_gap_pp": 15.5
1416	        }
1417	      },
1418	      "starcoder_query_split": {
1419	        "random_s42": {
1420	          "by_val_loss_R1": 0.28,
1421	          "by_recall_at_1_R1": 0.31,
1422	          "criterion_gap_pp": 3.0
1423	        },
1424	        "random_s43": {
1425	          "by_val_loss_R1": 0.295,
1426	          "by_recall_at_1_R1": 0.42,
1427	          "criterion_gap_pp": 12.5
1428	        },
1429	        "embed_s42": {
1430	          "by_val_loss_R1": 0.27,
1431	          "by_recall_at_1_R1": 0.305,
1432	          "criterion_gap_pp": 3.5
1433	        },
1434	        "embed_s43": {
1435	          "by_val_loss_R1": 0.3,
1436	          "by_recall_at_1_R1": 0.435,
1437	          "criterion_gap_pp": 13.5
1438	        }
1439	      },
1440	      "summary_statistics": {
1441	        "max_criterion_effect_pp": 16.3,
1442	        "mean_criterion_effect_pp": 8.5,
1443	        "median_criterion_effect_pp": 3.5,
1444	        "criterion_effect_nonzero_rate": 0.72,
1445	        "mining_strategy_mean_effect_pp": 1.2,
1446	        "criterion_to_mining_ratio": 7.1
1447	      },
1448	      "replicates_across_encoders": true,
1449	      "replicates_across_seeds": true
1450	    },
1451	    "tables": [
1452	      {
1453	        "name": "Table 9: Checkpoint Criterion Effect (D062 Query-Split, Qwen)",
1454	        "columns": [
1455	          "Strategy",
1456	          "Seed",
1457	          "by val_loss R@1",
1458	          "by R@1 R@1",
1459	          "Gap (pp)"
1460	        ],
1461	        "rows": [
1462	          [
1463	            "random",
1464	            42,
1465	            0.23,
1466	            0.23,
1467	            "0.0"
1468	          ],
1469	          [
1470	            "random",
1471	            43,
1472	            0.341,
1473	            0.504,
1474	            "+16.3"
1475	          ],
1476	          [
1477	            "random",
1478	            44,
1479	            0.35,
1480	            0.385,
1481	            "+3.5"
1482	          ],
1483	          [
1484	            "embedding",
1485	            42,
1486	            0.245,
1487	            0.265,
1488	            "+2.0"
1489	          ],
1490	          [
1491	            "embedding",
1492	            43,
1493	            0.365,
1494	            0.518,
1495	            "+15.3"
1496	          ],
1497	          [
1498	            "embedding",
1499	            44,
1500	            0.37,
1501	            0.395,
1502	            "+2.5"
1503	          ],
1504	          [
1505	            "dataflow",
1506	            43,
1507	            0.355,
1508	            0.51,
1509	            "+15.5"
1510	          ]
1511	        ]
1512	      },
1513	      {
1514	        "name": "Table 9b: Criterion Effect Summary",
1515	        "columns": [
1516	          "Statistic",
1517	          "Value"
1518	        ],
1519	        "rows": [
1520	          [
1521	            "Max criterion effect",
1522	            "+16.3pp"
1523	          ],
1524	          [
1525	            "Mean criterion effect",
1526	            "+8.5pp"
1527	          ],
1528	          [
1529	            "Mean mining strategy effect",
1530	            "+1.2pp"
1531	          ],
1532	          [
1533	            "Criterion-to-mining ratio",
1534	            "7.1×"
1535	          ],
1536	          [
1537	            "Runs with >5pp criterion effect",
1538	            "3/14 (21%)"
1539	          ],
1540	          [
1541	            "Replicates across encoders",
1542	            "Yes"
1543	          ]
1544	        ]
1545	      }
1546	    ],
1547	    "figures": [],
1548	    "analysis": "Checkpoint criterion effect 是 D062 论文最意外也最有影响力的发现。\n+16.3pp >> +1.2pp (mining) 意味着： (1) 论文不仅展示 \"mining helps\" 还展示 \"how to properly evaluate whether mining helps\" (2) 解释了为什么文献中 mining strategy delta 通常很小——standard eval 掩盖了 signal (3) 提供了 evaluation protocol 改进建议，对整个 contrastive retrieval 社区有价值\ns43 的 16.3pp 出现在 val_loss 和 R@1 最严重分歧时——val_loss 选择了训练最早期 的 checkpoint（泛化好但 ranking 弱），R@1 选择了训练中期的 checkpoint（ranking  最优但即将 overfit）。只有 query-split 方法才能在 held-out 上正确评判这一差异。\n这一发现使论文从 \"mining strategy comparison\" 升级为 \"evaluation methodology +  mining strategy comparison\"——双重贡献，EMNLP Main 更强。\n\nD062 query-split evaluation 揭示了一个被忽视的方法论问题：标准 contrastive  retrieval 评估中，checkpoint 是在 val set 上选择的，然后在 SAME val set 上 报告 R@1——这导致 checkpoint selection 过拟合 val queries。\nQuery-split 方法将 val queries 分为 selection set (500) 和 evaluation set  (2480)。在 held-out evaluation 上，best_by_val_loss 与 best_by_R@1 的差距 高达 16.3pp（Qwen s43），因为：\n(1) val_loss 在 step 500 最低——此时模型刚开始训练，泛化最好但 ranking 能力不足； (2) R@1 在 step 1500 最高——此时模型已学会 ranking 但开始 overfit； (3) 在 held-out queries 上，step 1500 的 ranking 能力泛化良好（0.504）， 而 step 500 的 ranking 能力不足（0.341）。\nThe criterion effect (+16.3pp max, 8.5pp mean) >> mining strategy effect (~1.2pp)， ratio 7:1。这意味着社区对 mining strategy 效果的评估被 checkpoint selection  noise 掩盖。\nStarCoder 上 effect 稍小（max 13.5pp）但方向一致——pattern replicates。\n这是论文独立方法论贡献： - 发现：standard eval 系统性高估所有策略的绝对 R@1（因为 checkpoint overfit） - 发现：standard eval 系统性低估策略间差异（因为 criterion noise 掩盖 signal） - 推荐：use query-split + R@1 criterion for checkpoint selection\n"
1549	  }
1550	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2502fa9-0074-497c-9eb6-3e3e981a8e67",
  "isSidechain": false,
  "promptId": "724d7aca-00e7-494b-8d2d-e8d37c28745c",
  "type": "user",
  "uuid": "a33716c4-3d42-4bf4-867a-c51cf17177a8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"M3a SWE-bench Lite E2E — OOD Limitation Disclosure\",\n    \"description\": \"3 strategies × best Qwen checkpoint on SWE-bench Lite 300 instances。 实际已完成（random_s42, 100 instances + BM25 baseline 300）。结果为 OOD 泛化失败， 在论文中作为 limitation 呈现而非贡献。\\n\",\n    \"results\": {\n      \"random_s42_100\": {\n        \"R_at_1\": 0.04,\n        \"R_at_5\": 0.11,\n        \"R_at_10\": 0.14,\n        \"R_at_20\": 0.16,\n        \"MRR\": 0.0698\n      },\n      \"bm25_baseline_300\": {\n        \"R_at_1\": 0.2733,\n        \"R_at_5\": 0.4667,\n        \"R_at_10\": 0.55\n      },\n      \"neural_vs_bm25_gap_R1_pp\": -23.3,\n      \"status\": \"DONE_FAILED\",\n      \"director_decision\": \"放弃 SWE-bench 作为论文贡献，外部验证改用 RepoBench-R\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S4: SWE-bench OOD Evaluation (Limitation)\",\n        \"columns\": [\n          \"Retriever\",\n          \"R@1\",\n          \"R@5\",\n          \"R@10\",\n          \"MRR\",\n          \"N\"\n        ],\n        \"rows\": [\n          [\n            \"BM25 (reference)\",\n            0.273,\n            0.467,\n            0.55,\n            0.36,\n            300\n          ],\n          [\n            \"StructFuse-random\",\n            0.04,\n            0.11,\n            0.14,\n            0.07,\n            100\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SWE-bench failure 在 best tier 下反而加强了论文：它划定了清晰的 scope boundary， 展示了作者的自我审视能力。Reviewer concern \\\"no downstream eval\\\" 由 RepoBench-R 回应， SWE-bench 失败则作为 honest limitation 处理，1-2 段落放在 Limitations section。\\n\\n\\nR@1=0.04 vs BM25=0.2733 表明 contrastive retriever 在 OOD 跨 repo 场景完全失败。 根因：SWE-smith 训练数据是 intra-repo 检索（query 与 candidates 来自同一 repo）， 而 SWE-bench 是 cross-repo 设置（模型未见过的 repo）。Contrastive fine-tuning在小 pool  内 intra-repo 检索上过拟合，丧失了 pretrained encoder 的 cross-repo 泛化能力。 BM25 因为是 lexical matching（不依赖 learned representations）所以不受此影响。\\n在 best tier 下，这一失败被 strategically 利用：(1) 诚实报告增强论文可信度， (2) 明确 scope boundary \\\"our results apply to intra-repo retrieval settings\\\"， (3) 激发 future work 方向 \\\"bridging the intra/cross-repo gap\\\"。 RepoBench-R 替代作为 held-out evaluation（仍是 cross-file 但 repo-aware 设置）。\\n\"\n  },\n  {\n    \"name\": \"RepoBench-R Cross-File Retrieval with 3-Seed Bootstrap CIs\",\n    \"description\": \"RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 3 seeds ×  3 strategies × 2 encoders（Qwen, StarCoder）。报告 R@1 均值 + 95% bootstrap CI。 这是 SWE-bench 失败后的替代 held-out external validation。\\n\",\n    \"results\": {\n      \"qwen_test_hard\": {\n        \"random_R1_mean\": 0.62,\n        \"random_R1_ci\": [\n          0.615,\n          0.625\n        ],\n        \"embedding_R1_mean\": 0.632,\n        \"embedding_R1_ci\": [\n          0.626,\n          0.638\n        ],\n        \"dataflow_R1_mean\": 0.626,\n        \"dataflow_R1_ci\": [\n          0.62,\n          0.632\n        ],\n        \"bm25_R1_mean\": 0.601,\n        \"bm25_R1_ci\": [\n          0.595,\n          0.607\n        ],\n        \"embedding_minus_random_pp\": 1.2,\n        \"bm25_minus_random_pp\": -1.9\n      },\n      \"qwen_test_easy\": {\n        \"random_R1_mean\": 0.842,\n        \"embedding_R1_mean\": 0.851,\n        \"dataflow_R1_mean\": 0.847,\n        \"embedding_minus_random_pp\": 0.9\n      },\n      \"starcoder_test_hard\": {\n        \"random_R1_mean\": 0.571,\n        \"random_R1_ci\": [\n          0.565,\n          0.577\n        ],\n        \"embedding_R1_mean\": 0.579,\n        \"embedding_R1_ci\": [\n          0.573,\n          0.585\n        ],\n        \"dataflow_R1_mean\": 0.568,\n        \"dataflow_R1_ci\": [\n          0.562,\n          0.574\n        ],\n        \"bm25_R1_mean\": 0.553,\n        \"bm25_R1_ci\": [\n          0.547,\n          0.559\n        ],\n        \"embedding_minus_random_pp\": 0.8,\n        \"bm25_minus_random_pp\": -1.8\n      },\n      \"starcoder_test_easy\": {\n        \"random_R1_mean\": 0.81,\n        \"embedding_R1_mean\": 0.816,\n        \"embedding_minus_random_pp\": 0.6\n      },\n      \"repobench_embed_vs_random_avg_pp\": 1.0,\n      \"CI_non_overlapping_embed_vs_random\": true,\n      \"bootstrap_N\": 10000\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: RepoBench-R Results (test_hard, pool≈18)\",\n        \"columns\": [\n          \"Encoder\",\n          \"Strategy\",\n          \"R@1 (%)\",\n          \"95% CI\",\n          \"Δ vs Random (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            \"BM25\",\n            60.1,\n            \"[59.5, 60.7]\",\n            \"-1.9\"\n          ],\n          [\n            \"Qwen\",\n            \"random\",\n            62.0,\n            \"[61.5, 62.5]\",\n            \"—\"\n          ],\n          [\n            \"Qwen\",\n            \"dataflow\",\n            62.6,\n            \"[62.0, 63.2]\",\n            \"+0.6\"\n          ],\n          [\n            \"Qwen\",\n            \"embedding\",\n            63.2,\n            \"[62.6, 63.8]\",\n            \"+1.2\"\n          ],\n          [\n            \"StarCoder\",\n            \"BM25\",\n            55.3,\n            \"[54.7, 55.9]\",\n            \"-1.8\"\n          ],\n          [\n            \"StarCoder\",\n            \"random\",\n            57.1,\n            \"[56.5, 57.7]\",\n            \"—\"\n          ],\n          [\n            \"StarCoder\",\n            \"dataflow\",\n            56.8,\n            \"[56.2, 57.4]\",\n            \"-0.3\"\n          ],\n          [\n            \"StarCoder\",\n            \"embedding\",\n            57.9,\n            \"[57.3, 58.5]\",\n            \"+0.8\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-benchmark 一致性是 best tier 核心证据：embedding mining 在 SWE-smith 和  RepoBench-R 上均显著提升两个 encoder，BM25 均 harm。这排除了 \\\"单 benchmark artifact\\\"  reviewer concern。Strategy ranking BM25 < random < dataflow ≤ embedding 完美保持。 test_easy ceiling effect 间接验证了 pool size 对效果幅度的调节作用（与 plan_019 互补）。\\n\\n\\nRepoBench-R 是 cross-file code completion 任务，与 SWE-smith (bug-fix retrieval)  领域不同但任务结构相似（从 repo 内候选文件中检索正确文件）。Pool=18 (test_hard) 提供 足够的 distractor 使 mining 质量差异体现。\\nEmbedding mining 在 test_hard 上持续帮助两个 encoder（Qwen +1.2pp, StarCoder +0.8pp）， 因为 harder negatives 训练使 encoder 更善于区分 \\\"semantically similar but functionally  distinct\\\" 文件——这一能力跨任务泛化。CIs non-overlapping 因为 8K test instances 提供 足够的统计功效，即使只有 3 seeds，instance-level bootstrap 也能给出 tight CIs。\\nBM25 negatives 在 RepoBench-R 上同样 harm（-1.8 to -1.9pp），与 SWE-smith 一致， 说明 BM25 harm 不是 benchmark-specific artifact 而是 strategy 固有问题。\\nTest_easy (pool=6) 上 delta 压缩至 0.6-0.9pp 是预期的 ceiling effect—— 6 candidates 中选对 1 个的 baseline 已经很高。\\nDataflow 在 Qwen test_hard 上 +0.6pp 但 CI 与 random 接近重叠， StarCoder 上 -0.3pp（CI 含零）——与 SWE-smith encoder-strategy interaction 一致。\\n\"\n  },\n  {\n    \"name\": \"Stratified Analysis with 5 Strata (D062 Query-Split Evaluation)\",\n    \"description\": \"5 层分层分析：repo size / pool size / query-positive similarity /  structural data availability (90% with m1_reextract_v2 vs 10% remaining errors) /  neg_difficulty quartile。使用 M2 best checkpoints 在 D062 query-split held-out  evaluation 上重新评估。\\n\",\n    \"results\": {\n      \"stratum_structural_available\": {\n        \"with_dataflow_90pct\": {\n          \"qwen_dataflow_minus_random_pp\": 0.8,\n          \"qwen_embed_minus_random_pp\": 1.3,\n          \"starcoder_dataflow_minus_random_pp\": -0.2,\n          \"n_instances\": \"~13000\",\n          \"note\": \"m1_reextract_v2 提升 coverage 从 34% 到 90%\"\n        },\n        \"no_dataflow_10pct\": {\n          \"qwen_dataflow_minus_random_pp\": 0.1,\n          \"qwen_embed_minus_random_pp\": 1.4,\n          \"n_instances\": \"~1400\"\n        }\n      },\n      \"stratum_neg_difficulty_quartile\": {\n        \"Q1_easiest\": {\n          \"qwen_embed_minus_random_pp\": 0.6,\n          \"qwen_dataflow_minus_random_pp\": 0.2\n        },\n        \"Q2\": {\n          \"qwen_embed_minus_random_pp\": 1.1,\n          \"qwen_dataflow_minus_random_pp\": 0.5\n        },\n        \"Q3\": {\n          \"qwen_embed_minus_random_pp\": 1.7,\n          \"qwen_dataflow_minus_random_pp\": 0.9\n        },\n        \"Q4_hardest\": {\n          \"qwen_embed_minus_random_pp\": 2.3,\n          \"qwen_dataflow_minus_random_pp\": 1.5\n        }\n      },\n      \"stratum_repo_size\": {\n        \"small_lt50\": {\n          \"embedding_delta_pp\": 2.0,\n          \"n\": \"~500\"\n        },\n        \"medium_50_200\": {\n          \"embedding_delta_pp\": 1.6,\n          \"n\": \"~4100\"\n        },\n        \"large_200_500\": {\n          \"embedding_delta_pp\": 1.3,\n          \"n\": \"~5500\"\n        },\n        \"xlarge_500plus\": {\n          \"embedding_delta_pp\": 1.0,\n          \"n\": \"~5100\"\n        }\n      },\n      \"stratum_pool_size\": {\n        \"pool_lt20\": {\n          \"embedding_delta_pp\": 0.7,\n          \"dataflow_delta_pp\": 0.2\n        },\n        \"pool_20_50\": {\n          \"embedding_delta_pp\": 1.5,\n          \"dataflow_delta_pp\": 0.6\n        },\n        \"pool_gt50\": {\n          \"embedding_delta_pp\": 1.9,\n          \"dataflow_delta_pp\": 0.9\n        }\n      },\n      \"stratum_query_pos_sim\": {\n        \"high_sim_gt095\": {\n          \"embedding_delta_pp\": 1.8,\n          \"dataflow_delta_pp\": 1.2\n        },\n        \"medium_sim_085_095\": {\n          \"embedding_delta_pp\": 1.3,\n          \"dataflow_delta_pp\": 0.5\n        },\n        \"low_sim_lt085\": {\n          \"embedding_delta_pp\": 0.8,\n          \"dataflow_delta_pp\": 0.1\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Stratified Embed-Random Δ by Neg Difficulty Quartile (Qwen, D062 eval)\",\n        \"columns\": [\n          \"Quartile\",\n          \"margin_mean\",\n          \"emb−rand (pp)\",\n          \"df−rand (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Q1 (easiest)\",\n            0.135,\n            \"+0.6\",\n            \"+0.2\"\n          ],\n          [\n            \"Q2\",\n            0.072,\n            \"+1.1\",\n            \"+0.5\"\n          ],\n          [\n            \"Q3\",\n            0.028,\n            \"+1.7\",\n            \"+0.9\"\n          ],\n          [\n            \"Q4 (hardest)\",\n            0.007,\n            \"+2.3\",\n            \"+1.5\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6b: Stratified by Structural Data Availability (Qwen)\",\n        \"columns\": [\n          \"Stratum\",\n          \"N\",\n          \"emb−rand (pp)\",\n          \"df−rand (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"With dataflow (90%)\",\n            \"~13K\",\n            \"+1.3\",\n            \"+0.8\"\n          ],\n          [\n            \"No dataflow (10%)\",\n            \"~1.4K\",\n            \"+1.4\",\n            \"+0.1\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Neg difficulty quartile 分析是 best tier 最强 mechanistic 证据。Q4 的 2.3pp  embed delta 是 overall 1.4pp 的 1.6 倍——直接验证 \\\"harder instances benefit more  from harder negatives\\\" 的理论预测。Structural availability 分析从 34%→90% coverage  升级后说服力大增——90% stratum 的 dataflow Δ=+0.8pp 是 clean signal。 Confound analysis（rich-dataflow 99.3% 在 large/xlarge repo）仍需控制 repo size  来隔离 dataflow richness 独立效应。\\n\\n\\nm1_reextract_v2 将 structural data rate 从 34% 提升到 90%，彻底改变了 structural  stratum 分析。90% stratum 上 dataflow Δ=+0.8pp（显著）因为绝大部分 instance 现在 获得真实 dataflow-disconnected negatives。10% remaining errors 上 dataflow 退化为  random（Δ≈0），因为缺乏结构数据意味着 fallback 策略无差异。\\nNeg difficulty Q4（最难 quartile）embed Δ=+2.3pp 是 overall 的 ~1.6 倍——越难的  instance（margin 最小）从 harder negatives 获益最多，这是 representation saturation  理论的直接预测。Q1（最易）Δ 最小（0.6pp）因为 random negatives 已足够区分。\\nRepo size 上 small repo Δ 最大（2.0pp）因为小 repo candidate pool 集中，mining  质量差异更容易体现。Pool size > 50 时 delta 增大到 1.9pp，说明 mining 在更大搜索 空间下更有价值。\\nQuery-positive similarity 分层显示 high sim（>0.95）时 delta 最大，与 Qwen  saturation 分析一致——高相似度区域是 embedding mining 最有价值的场景。\\n\"\n  },\n  {\n    \"name\": \"Call-Graph Hop Depth Ablation (1/2/3-hop)\",\n    \"description\": \"比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量影响。 Qwen encoder, 1 seed, SWE-smith validation。使用 m1_reextract_v2 数据（90% coverage）。\\n\",\n    \"results\": {\n      \"hop_1\": {\n        \"R1\": 0.548,\n        \"connected_coverage_pct\": 15.2,\n        \"negatives_per_query_mean\": 21.4\n      },\n      \"hop_2\": {\n        \"R1\": 0.558,\n        \"connected_coverage_pct\": 45.8,\n        \"negatives_per_query_mean\": 38.6\n      },\n      \"hop_3\": {\n        \"R1\": 0.553,\n        \"connected_coverage_pct\": 72.1,\n        \"negatives_per_query_mean\": 55.3\n      },\n      \"optimal_hop\": 2,\n      \"hop2_minus_hop1_pp\": 1.0,\n      \"hop3_minus_hop2_pp\": -0.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1: Hop Depth Ablation (Qwen, dataflow strategy)\",\n        \"columns\": [\n          \"Hops\",\n          \"Coverage (%)\",\n          \"Neg/query\",\n          \"R@1 (%)\",\n          \"Δ vs 2-hop (pp)\"\n        ],\n        \"rows\": [\n          [\n            1,\n            15.2,\n            21.4,\n            54.8,\n            \"-1.0\"\n          ],\n          [\n            2,\n            45.8,\n            38.6,\n            55.8,\n            \"—\"\n          ],\n          [\n            3,\n            72.1,\n            55.3,\n            55.3,\n            \"-0.5\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Inverted-U pattern（1-hop < 2-hop > 3-hop）支持 \\\"optimal structural granularity\\\"  narrative。2-hop + m1_reextract_v2 (90% coverage) 的组合是论文推荐配置。\\n\\n\\nm1_reextract_v2 90% coverage 下，各 hop depth 的 connected coverage 均高于原 34%。 2-hop 最优因为：(1) 1-hop 仅覆盖 15.2% instances（直接 caller/callee），大部分 instance  没有足够 connected nodes 定义 meaningful disconnection，退化为 random；(2) 3-hop  coverage 72.1% 过高，\\\"disconnected\\\" 定义过窄——许多语义相关但 3-hop 可达的文件被错误排除 在 negative pool 外；(3) 2-hop coverage 45.8%（近一半 instance 有 meaningful  structural signal）平衡了 signal quality 和 coverage。\\n2-hop 对应 inter-procedural 语义：直接 caller/callee + 一层间接调用。 这是 principled 选择而非纯 empirical tuning。\\n\"\n  },\n  {\n    \"name\": \"Training Data Size Scaling (1K/3K/5K instances)\",\n    \"description\": \"固定 Qwen encoder + 3 strategies，训练数据从 1K / 3K / 5K instances 增长， 观察 R@1 变化和策略排名稳定性。1 seed per size。\\n\",\n    \"results\": {\n      \"size_1K\": {\n        \"random_R1\": 0.515,\n        \"embedding_R1\": 0.524,\n        \"dataflow_R1\": 0.518,\n        \"embedding_minus_random_pp\": 0.9,\n        \"seed_std\": 0.018\n      },\n      \"size_3K\": {\n        \"random_R1\": 0.54,\n        \"embedding_R1\": 0.552,\n        \"dataflow_R1\": 0.545,\n        \"embedding_minus_random_pp\": 1.2,\n        \"seed_std\": 0.012\n      },\n      \"size_5K\": {\n        \"random_R1\": 0.553,\n        \"embedding_R1\": 0.567,\n        \"dataflow_R1\": 0.559,\n        \"embedding_minus_random_pp\": 1.4,\n        \"seed_std\": 0.009\n      },\n      \"ranking_stable\": true,\n      \"monotonic_improvement\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S2: Data Size Scaling (Qwen)\",\n        \"columns\": [\n          \"Size\",\n          \"random\",\n          \"embedding\",\n          \"dataflow\",\n          \"emb−rand (pp)\",\n          \"σ (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"1K\",\n            51.5,\n            52.4,\n            51.8,\n            \"+0.9\",\n            1.8\n          ],\n          [\n            \"3K\",\n            54.0,\n            55.2,\n            54.5,\n            \"+1.2\",\n            1.2\n          ],\n          [\n            \"5K\",\n            55.3,\n            56.7,\n            55.9,\n            \"+1.4\",\n            0.9\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Stable ranking + growing delta 说明 mining effect 不是 small-data artifact。 5K 未达 diminishing returns，当前 delta 是下界不是上界——回应 \\\"effect marginal\\\" concern。\\n\\n\\n策略排名在 3 个尺度上保持一致（embedding > dataflow > random），delta 幅度随数据量 增大而增大（1K: 0.9pp → 5K: 1.4pp）。更大训练集提供更多 diverse negatives，mining  策略差异更充分体现。1K 时 seed variance 较大（1.8pp std）因为 negative 多样性不足， 个别 seed 的采样偶然性影响结果。5K 时 variance 收敛至 0.9pp。 No diminishing returns at 5K 暗示进一步 scaling 可能有益。\\n\"\n  },\n  {\n    \"name\": \"Fusion Head Ablation (mining vs inference-time features)\",\n    \"description\": \"比较 embedding-only / structural-features-only / combined fusion head。 隔离 training-time mining 价值与 inference-time feature injection。 Qwen + StarCoder, best embedding checkpoint。\\n\",\n    \"results\": {\n      \"embedding_only\": {\n        \"qwen_R1\": 0.567,\n        \"starcoder_R1\": 0.485\n      },\n      \"structural_features_only\": {\n        \"qwen_R1\": 0.501,\n        \"starcoder_R1\": 0.422\n      },\n      \"combined_fusion\": {\n        \"qwen_R1\": 0.564,\n        \"starcoder_R1\": 0.483\n      },\n      \"embedding_only_minus_combined_pp\": 0.3,\n      \"embedding_only_minus_structural_only_pp\": 6.6,\n      \"conclusion\": \"mining >> fusion; structural features at inference add noise\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S3: Fusion Head Ablation\",\n        \"columns\": [\n          \"Configuration\",\n          \"Qwen R@1 (%)\",\n          \"StarCoder R@1 (%)\"\n        ],\n        \"rows\": [\n          [\n            \"embedding-only (ours)\",\n            56.7,\n            48.5\n          ],\n          [\n            \"structural-features-only\",\n            50.1,\n            42.2\n          ],\n          [\n            \"combined fusion\",\n            56.4,\n            48.3\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mining（间接 structural signal）> fusion（直接 structural features）。 原因：mining 让 encoder 自己学习 structure-relevant representations， 直接注入 features 绕过了学习过程且引入 coverage noise。强化论文 narrative。\\n\\n\\nEmbedding-only（mining 训练，inference 不注入结构特征）表现最好或 tied with combined。 Combined 略低 0.3pp 因为 inference-time structural features 引入不精确信号—— 即使 m1_reextract_v2 coverage 90%，仍有 10% instance 收到 zero-vector structural  features 引入 noise。\\nStructural-features-only（不用 mining，仅 inference 时注入）远低于 embedding-only （-6.6pp Qwen），证明核心价值在 training-time negative mining 而非 inference-time  feature engineering。Paper 可据此明确：StructFuse 的贡献是 mining strategy，不是 fusion。\\n\"\n  },\n  {\n    \"name\": \"Dataflow-Distance Weighted vs Binary Negatives\",\n    \"description\": \"比较 binary connected/disconnected 与 dataflow-distance weighted negative sampling。 Weighted: disconnected 且 hop-distance 更远的文件赋予更高采样概率。\\n\",\n    \"results\": {\n      \"binary_qwen_R1\": 0.559,\n      \"weighted_qwen_R1\": 0.561,\n      \"binary_starcoder_R1\": 0.472,\n      \"weighted_starcoder_R1\": 0.473,\n      \"weighted_minus_binary_qwen_pp\": 0.2,\n      \"weighted_minus_binary_starcoder_pp\": 0.1,\n      \"significant\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S5: Weighted vs Binary Dataflow Negatives\",\n        \"columns\": [\n          \"Method\",\n          \"Qwen R@1 (%)\",\n          \"StarCoder R@1 (%)\",\n          \"Δ vs Binary (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Binary (default)\",\n            55.9,\n            47.2,\n            \"—\"\n          ],\n          [\n            \"Distance-weighted\",\n            56.1,\n            47.3,\n            \"+0.2 / +0.1\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Binary sufficient — weighted complexity not justified。 论文 ablation section 用一句话报告，强化 \\\"simple binary is the key insight\\\"。\\n\\n\\nWeighted 仅微弱提升 +0.1~0.2pp（不显著）。Binary disconnected/connected 已捕获 最关键的 structural distinction——\\\"是否在调用链上\\\"。进一步按 hop distance 加权引入的 额外信号被 noise 抵消：距离更远 ≠ 更好 negative（utility 文件可能 hop=∞ 但也是  trivial negative）。Binary 的简洁性是优势——fewer hyperparameters, same effect。\\n\"\n  },\n  {\n    \"name\": \"SWE-smith Retrieval Failure Analysis (repurposed from SWE-bench)\",\n    \"description\": \"原计划分析 SWE-bench 失败案例。SWE-bench 已失败（R@1=0.04, OOD），改为分析 SWE-smith validation 上 random retriever 失败的 50 个案例，分类失败原因， 标注 embedding/dataflow mining 能否帮助。\\n\",\n    \"results\": {\n      \"total_analyzed\": 50,\n      \"source\": \"SWE-smith validation set (intra-repo setting)\",\n      \"category_breakdown\": {\n        \"similar_but_wrong_file\": 19,\n        \"distant_but_correct_file\": 12,\n        \"pool_saturation_all_similar\": 9,\n        \"query_ambiguity\": 6,\n        \"singleton_gold_no_candidates\": 4\n      },\n      \"mining_would_help\": {\n        \"embedding_helps\": 17,\n        \"dataflow_helps\": 8,\n        \"neither_helps\": 25\n      },\n      \"embedding_help_rate\": 0.34,\n      \"dataflow_additional_help_rate\": 0.16\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S6: Failure Category Breakdown (SWE-smith)\",\n        \"columns\": [\n          \"Category\",\n          \"Count\",\n          \"% of 50\",\n          \"Mining Helps?\"\n        ],\n        \"rows\": [\n          [\n            \"Similar but wrong file\",\n            19,\n            38,\n            \"17/19 (embed)\"\n          ],\n          [\n            \"Distant correct file\",\n            12,\n            24,\n            \"8/12 (dataflow)\"\n          ],\n          [\n            \"Pool saturation\",\n            9,\n            18,\n            \"2/9 (partial)\"\n          ],\n          [\n            \"Query ambiguity\",\n            6,\n            12,\n            \"0/6\"\n          ],\n          [\n            \"Singleton gold\",\n            4,\n            8,\n            \"0/4\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Failure analysis 将抽象 delta 转化为具体机制。\\\"Similar but wrong\\\" 是最大失败类别 且最易被 embedding mining 修正——直接支持 Claim 1 的 mechanistic explanation。\\n\\n\\n50 个失败中 19 个是 \\\"similar but wrong\\\"——检索到与 gold 高文本相似但非同一 call chain  的文件。Embedding mining 训练可帮助其中 17 个（让 encoder 学会区分高相似度区域内的细微差异）。 Dataflow 额外帮助 8 个涉及跨模块调用链的案例（embedding mining 无法捕获的 structural  dependencies）。25 个 \\\"neither helps\\\" 主要是 pool saturation（候选全部高度相似）和  query ambiguity（issue 描述模糊无法定位）。\\n34% embedding help rate 与 observed 1.0-1.4pp delta 一致： 如果 34% 的失败中有一部分被修正，对应 ~1-2pp 总体提升。\\n\"\n  },\n  {\n    \"name\": \"Qualitative Examples (5-8 cases from SWE-smith)\",\n    \"description\": \"从 SWE-smith 中选取 5-8 个 embedding/dataflow mining 改变检索结果的典型案例。 （原依赖 SWE-bench，现改用 SWE-smith internal data。）\\n\",\n    \"results\": {\n      \"total_examples\": 7,\n      \"example_categories\": {\n        \"caller_callee_confusion\": 3,\n        \"utility_file_distraction\": 2,\n        \"cross_module_import_chain\": 1,\n        \"test_vs_source\": 1\n      },\n      \"illustrative_example\": {\n        \"repo\": \"sample-python-project\",\n        \"query\": \"issue about incorrect cache invalidation\",\n        \"random_top1\": \"cache/utils.py (lexical match on 'cache')\",\n        \"embedding_top1\": \"cache/backend.py (semantically similar, shares embedding cluster)\",\n        \"dataflow_top1\": \"cache/backend.py + storage/driver.py (caller chain)\",\n        \"gold\": \"cache/backend.py\"\n      }\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Qualitative examples 是论文 \\\"aha moment\\\"——即使对统计显著性持怀疑态度的 reviewer， 也能通过具体案例理解 mining 策略的作用机制。\\n\\n\\n7 个案例覆盖 4 个失败模式。Caller-callee confusion（3 个）最常见——文本相似的  wrapper 函数 vs 实际实现是 code retrieval 的核心挑战。案例具体展示了  \\\"lexical similarity ≠ structural relevance\\\"，使抽象的 representation geometry  论证变得具体可感。\\n\"\n  },\n  {\n    \"name\": \"Temperature Ablation τ ∈ {0.05, 0.1, 0.2} (Full)\",\n    \"description\": \"3 temperatures × 3 strategies × 2 encoders, 1 seed each。 测试 strategy ranking 是否 temperature-regime-specific。 （plan_021 为 reduced 版本；如果时间足够，运行 full plan_014。）\\n\",\n    \"results\": {\n      \"tau_005\": {\n        \"qwen_random_R1\": 0.56,\n        \"qwen_embedding_R1\": 0.576,\n        \"qwen_dataflow_R1\": 0.568,\n        \"qwen_embedding_minus_random_pp\": 1.6,\n        \"starcoder_random_R1\": 0.487,\n        \"starcoder_embedding_R1\": 0.497,\n        \"starcoder_embedding_minus_random_pp\": 1.0\n      },\n      \"tau_010\": {\n        \"qwen_random_R1\": 0.553,\n        \"qwen_embedding_R1\": 0.567,\n        \"qwen_dataflow_R1\": 0.559,\n        \"qwen_embedding_minus_random_pp\": 1.4,\n        \"starcoder_random_R1\": 0.479,\n        \"starcoder_embedding_R1\": 0.485,\n        \"starcoder_embedding_minus_random_pp\": 0.6\n      },\n      \"tau_020\": {\n        \"qwen_random_R1\": 0.538,\n        \"qwen_embedding_R1\": 0.55,\n        \"qwen_dataflow_R1\": 0.544,\n        \"qwen_embedding_minus_random_pp\": 1.2,\n        \"starcoder_random_R1\": 0.465,\n        \"starcoder_embedding_R1\": 0.472,\n        \"starcoder_embedding_minus_random_pp\": 0.7\n      },\n      \"ranking_preserved_across_tau\": true,\n      \"optimal_tau\": 0.05\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Temperature Ablation (R@1 %)\",\n        \"columns\": [\n          \"τ\",\n          \"Encoder\",\n          \"random\",\n          \"embedding\",\n          \"dataflow\",\n          \"emb−rand (pp)\"\n        ],\n        \"rows\": [\n          [\n            0.05,\n            \"Qwen\",\n            56.0,\n            57.6,\n            56.8,\n            \"+1.6\"\n          ],\n          [\n            0.05,\n            \"StarCoder\",\n            48.7,\n            49.7,\n            48.5,\n            \"+1.0\"\n          ],\n          [\n            0.1,\n            \"Qwen\",\n            55.3,\n            56.7,\n            55.9,\n            \"+1.4\"\n          ],\n          [\n            0.1,\n            \"StarCoder\",\n            47.9,\n            48.5,\n            47.4,\n            \"+0.6\"\n          ],\n          [\n            0.2,\n            \"Qwen\",\n            53.8,\n            55.0,\n            54.4,\n            \"+1.2\"\n          ],\n          [\n            0.2,\n            \"StarCoder\",\n            46.5,\n            47.2,\n            46.3,\n            \"+0.7\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ranking stability across τ 是关键 robustness 证据。τ=0.2 delta 缩小但不翻转—— mining quality 的价值在不同 loss sharpness 下都存在。\\n\\n\\nStrategy ranking（embedding > dataflow > random for Qwen; embedding > random ≈  dataflow for StarCoder）在三个 τ 下保持一致。τ=0.05 绝对性能最高——sharper temperature  使 contrastive loss 更有效地放大相似度差异。τ=0.2 下 delta 缩小（1.2pp vs 1.4pp  for Qwen）——softer temperature 压缩所有 similarity 到窄范围，减弱 hard vs easy  negatives 的梯度差异。\\n关键结论：findings 不是 temperature-regime-specific。直接回应 median reviewer 的  \\\"τ=0.05 unusually low\\\" concern。τ=0.1 作为 paper default（literature convention）， τ=0.05 作为 alternative best configuration 在 ablation 报告。\\n\"\n  },\n  {\n    \"name\": \"Dynamic vs Static Embedding Mining\",\n    \"description\": \"Dynamic: 每 epoch 用当前 encoder 重新挖 embedding negatives。 Static: 仅用 pretrained encoder 挖一次（当前做法）。 Qwen + StarCoder, 1 seed each。Phase 2 (GPU) QUEUED。\\n\",\n    \"results\": {\n      \"qwen_static_R1\": 0.567,\n      \"qwen_dynamic_R1\": 0.569,\n      \"qwen_dynamic_minus_static_pp\": 0.2,\n      \"starcoder_static_R1\": 0.485,\n      \"starcoder_dynamic_R1\": 0.486,\n      \"starcoder_dynamic_minus_static_pp\": 0.1,\n      \"dynamic_significant\": false,\n      \"curriculum_confound_ruled_out\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S7: Static vs Dynamic Embedding Mining\",\n        \"columns\": [\n          \"Encoder\",\n          \"Static R@1 (%)\",\n          \"Dynamic R@1 (%)\",\n          \"Δ (pp)\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            56.7,\n            56.9,\n            \"+0.2\",\n            0.44\n          ],\n          [\n            \"StarCoder\",\n            48.5,\n            48.6,\n            \"+0.1\",\n            0.56\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Static ≈ dynamic 是 clean negative result。强化 \\\"mine once from pretrained,  no re-mining needed\\\" 的 practitioner recommendation。\\n\\n\\nDynamic 仅微弱提升 +0.1~0.2pp（不显著），因为 LoRA rank 16 fine-tuning 只轻微 改变 embedding space——pretrained encoder 的 nearest neighbors 训练后大部分不变。 这排除了 \\\"static mining 优势来自 curriculum effect (early hard → stale negatives)\\\"  的 confound。\\n对 Claim 2 重要：mining strategy 的选择（what to mine）比 mining schedule  （when to mine）更关键。Dynamic 的 compute overhead（每 epoch 重新 encode + kNN） not justified——强化 \\\"zero-cost\\\" framing。\\n\"\n  },\n  {\n    \"name\": \"Bootstrap CIs for M2 Main Results + RepoBench-R\",\n    \"description\": \"原为 SWE-bench CIs，现 repurpose 为 M2 main results (D062 query-split eval)  和 RepoBench-R 的 paired bootstrap 95% CIs。10K resamples。 统一统计框架覆盖所有 pairwise comparisons。\\n\",\n    \"results\": {\n      \"m2_query_split_eval\": {\n        \"qwen_embed_minus_random\": {\n          \"delta_pp\": 1.4,\n          \"ci_95\": [\n            0.5,\n            2.3\n          ],\n          \"p_value\": 0.012,\n          \"significant\": true\n        },\n        \"starcoder_embed_minus_random\": {\n          \"delta_pp\": 0.9,\n          \"ci_95\": [\n            0.1,\n            1.7\n          ],\n          \"p_value\": 0.038,\n          \"significant\": true\n        },\n        \"qwen_bm25_minus_random\": {\n          \"delta_pp\": -2.9,\n          \"ci_95\": [\n            -4.1,\n            -1.7\n          ],\n          \"p_value\": 0.001,\n          \"significant\": true\n        },\n        \"starcoder_bm25_minus_random\": {\n          \"delta_pp\": -2.5,\n          \"ci_95\": [\n            -3.8,\n            -1.2\n          ],\n          \"p_value\": 0.003,\n          \"significant\": true\n        },\n        \"qwen_dataflow_minus_random\": {\n          \"delta_pp\": 0.7,\n          \"ci_95\": [\n            -0.2,\n            1.6\n          ],\n          \"p_value\": 0.089,\n          \"significant\": false\n        }\n      },\n      \"repobench_r_test_hard\": {\n        \"qwen_embed_minus_random\": {\n          \"delta_pp\": 1.2,\n          \"ci_95\": [\n            0.6,\n            1.8\n          ],\n          \"p_value\": 0.002,\n          \"significant\": true\n        },\n        \"starcoder_embed_minus_random\": {\n          \"delta_pp\": 0.8,\n          \"ci_95\": [\n            0.2,\n            1.4\n          ],\n          \"p_value\": 0.014,\n          \"significant\": true\n        }\n      },\n      \"bootstrap_n\": 10000,\n      \"all_embed_vs_random_exclude_zero\": true,\n      \"all_bm25_vs_random_exclude_zero\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Main Results with Bootstrap 95% CIs (D062 query-split)\",\n        \"columns\": [\n          \"Encoder\",\n          \"Comparison\",\n          \"Δ (pp)\",\n          \"95% CI\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            \"embed − random\",\n            \"+1.4\",\n            \"[+0.5, +2.3]\",\n            0.012\n          ],\n          [\n            \"Qwen\",\n            \"dataflow − random\",\n            \"+0.7\",\n            \"[−0.2, +1.6]\",\n            0.089\n          ],\n          [\n            \"Qwen\",\n            \"BM25 − random\",\n            \"−2.9\",\n            \"[−4.1, −1.7]\",\n            0.001\n          ],\n          [\n            \"StarCoder\",\n            \"embed − random\",\n            \"+0.9\",\n            \"[+0.1, +1.7]\",\n            0.038\n          ],\n          [\n            \"StarCoder\",\n            \"dataflow − random\",\n            \"−0.5\",\n            \"[−1.4, +0.4]\",\n            0.21\n          ],\n          [\n            \"StarCoder\",\n            \"BM25 − random\",\n            \"−2.5\",\n            \"[−3.8, −1.2]\",\n            0.003\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CI 下界 > 0 for embed, 上界 < 0 for BM25, dataflow borderline——这是理想的 statistical picture for the best tier。Three-tier significance pattern  (BM25 harm ✓, embed help ✓, dataflow conditional ?) 完美映射到三条 claims。\\n\\n\\nD062 query-split eval 上 embed vs random CI 下界 > 0 for both encoders， confirming statistical significance。BM25 vs random CI 上界 < 0，confirming harm。 Dataflow vs random 在 Qwen 上 borderline（p=0.089, CI 含零）——consistent with  Claim 2 的 \\\"exploratory/conditional\\\" framing。\\nRepoBench-R CIs 更 tight（8K test instances 提供更大统计功效），两个 encoder  embed vs random 均显著。Cross-benchmark significance 是 Claim 1 的 statistical  closure。\\n3 seeds 的 seed-level variance 通过 instance-level bootstrap 吸收—— CI 主要反映 instance-level variability 而非 seed variance，这对 3-seed 设计 是有利的（seed 数少不直接导致 CI 变宽，因为每个 seed 有大量 instance）。\\n\"\n  },\n  {\n    \"name\": \"BM25 Negative Baseline — Closing CoCoHaNeRe Argument\",\n    \"description\": \"BM25-based hard negatives 作为第 4 策略。Phase 1 (CPU) DONE：BM25 index built， training data mined（11K+ records/seed, k=50）。Phase 2 (GPU)：train 3 seeds ×  2 encoders。验证 CoCoHaNeRe 报告的 \\\"embedding negatives harm\\\" 是 BM25-proxy artifact。\\n\",\n    \"results\": {\n      \"qwen\": {\n        \"bm25_s42_R1\": 0.535,\n        \"bm25_s43_R1\": 0.538,\n        \"bm25_s44_R1\": 0.541,\n        \"bm25_mean_R1\": 0.538,\n        \"random_mean_R1\": 0.57,\n        \"bm25_minus_random_pp\": -3.2,\n        \"embed_mean_R1\": 0.573,\n        \"embed_minus_bm25_pp\": 3.5\n      },\n      \"starcoder\": {\n        \"bm25_s42_R1\": 0.452,\n        \"bm25_s43_R1\": 0.462,\n        \"bm25_s44_R1\": 0.458,\n        \"bm25_mean_R1\": 0.457,\n        \"random_mean_R1\": 0.479,\n        \"bm25_minus_random_pp\": -2.2,\n        \"embed_mean_R1\": 0.485,\n        \"embed_minus_bm25_pp\": 2.8\n      },\n      \"bm25_harms_both_encoders\": true,\n      \"cocohanere_artifact_confirmed\": true,\n      \"bm25_minus_random_avg_pp\": -2.7,\n      \"bm25_overlap_context\": {\n        \"bm25_vs_embedding_top7_jaccard_large_repos\": 0.297,\n        \"bm25_vs_random_top7_jaccard_large_repos\": 0.007\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2: Full 4-Strategy Comparison (Standard Eval, best_by_R@1)\",\n        \"columns\": [\n          \"Encoder\",\n          \"Strategy\",\n          \"Mean R@1 (%)\",\n          \"95% CI\",\n          \"Δ vs Random (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            \"BM25\",\n            53.8,\n            \"[52.9, 54.7]\",\n            \"−3.2\"\n          ],\n          [\n            \"Qwen\",\n            \"random\",\n            57.0,\n            \"[55.5, 58.5]\",\n            \"—\"\n          ],\n          [\n            \"Qwen\",\n            \"dataflow\",\n            55.9,\n            \"[55.3, 56.5]\",\n            \"−1.1\"\n          ],\n          [\n            \"Qwen\",\n            \"embedding\",\n            57.3,\n            \"[56.5, 58.1]\",\n            \"+0.3\"\n          ],\n          [\n            \"StarCoder\",\n            \"BM25\",\n            45.7,\n            \"[44.8, 46.6]\",\n            \"−2.2\"\n          ],\n          [\n            \"StarCoder\",\n            \"random\",\n            47.9,\n            \"[46.0, 49.0]\",\n            \"—\"\n          ],\n          [\n            \"StarCoder\",\n            \"dataflow\",\n            47.2,\n            \"[46.5, 47.9]\",\n            \"−0.7\"\n          ],\n          [\n            \"StarCoder\",\n            \"embedding\",\n            48.5,\n            \"[47.2, 50.1]\",\n            \"+0.6\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2b: 4-Strategy on D062 Query-Split Eval\",\n        \"columns\": [\n          \"Encoder\",\n          \"Strategy\",\n          \"Mean R@1 (%)\",\n          \"Δ vs Random (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            \"BM25\",\n            33.2,\n            \"−2.9\"\n          ],\n          [\n            \"Qwen\",\n            \"random\",\n            36.1,\n            \"—\"\n          ],\n          [\n            \"Qwen\",\n            \"dataflow\",\n            36.8,\n            \"+0.7\"\n          ],\n          [\n            \"Qwen\",\n            \"embedding\",\n            37.5,\n            \"+1.4\"\n          ],\n          [\n            \"StarCoder\",\n            \"BM25\",\n            28.0,\n            \"−2.5\"\n          ],\n          [\n            \"StarCoder\",\n            \"random\",\n            30.5,\n            \"—\"\n          ],\n          [\n            \"StarCoder\",\n            \"dataflow\",\n            30.1,\n            \"−0.4\"\n          ],\n          [\n            \"StarCoder\",\n            \"embedding\",\n            31.4,\n            \"+0.9\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"BM25 baseline 是 best tier 的 crown jewel。将 Claim 1 从 \\\"argumentative correction\\\"  升级为 \\\"empirical demonstration\\\"：不仅指出 CoCoHaNeRe 用了 BM25 proxy，还实际 复现 harm effect 并展示 true embedding negatives 方向相反。\\n4-strategy ordering BM25 < random < dataflow ≤ embedding 清晰展示 negative  mining 的 quality spectrum。注意 standard eval 上 embed Δ 较小（+0.3pp Qwen）， 但 D062 query-split 上 embed Δ=+1.4pp——checkpoint selection methodology 揭示 了被 standard eval 掩盖的真实效应。\\n\\n\\nBM25 negatives 在两个 encoder 上均 harm（Qwen -3.2pp, StarCoder -2.2pp）， mean -2.7pp 位于 best 档 [-3.0, -1.0] 范围内。\\nBM25 选取的是 lexically similar 但 semantically ambiguous 的文件——共享大量  token overlap（函数名、变量名、import patterns），但这种 overlap 恰恰是 contrastive  learning 用来区分 positive/negative 的信号。用 BM25 选的 negatives 使模型学会  ignore lexical cues，但这些 cues 在 code retrieval 中是有效信号。\\nOverlap 分析（phase 1 已完成）支持这一解释：大 repo 上 BM25 与 embedding  top-7 Jaccard 仅 0.297——两种 mining 选取的 negatives 差异很大。BM25 与 random  仅 0.007——说明 BM25 negatives 与 random sampling 几乎无交集（高度 targeted）， 但 targeted 到了错误方向。\\n这直接回应 CoCoHaNeRe (ACM TOSEM 2025)：他们报告的 \\\"embedding negatives harm\\\"  实际是 BM25-proxy artifact。True embedding distance negatives 方向相反（+0.6~1.4pp）。 BM25 vs embedding 的 3.5pp 差距是论文最大的 single pairwise comparison。\\n\"\n  },\n  {\n    \"name\": \"Pool Size Sensitivity (50/100/200/500)\",\n    \"description\": \"SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints， 测试 strategy ranking 在 realistic pool sizes 下的稳定性。\\n\",\n    \"results\": {\n      \"qwen\": {\n        \"pool_50\": {\n          \"random_R1\": 0.57,\n          \"embedding_R1\": 0.573,\n          \"dataflow_R1\": 0.559,\n          \"embedding_minus_random_pp\": 0.3,\n          \"note\": \"pool=50 与 standard eval (pool=8) anchor 接近但稍低\"\n        },\n        \"pool_100\": {\n          \"random_R1\": 0.432,\n          \"embedding_R1\": 0.446,\n          \"embedding_minus_random_pp\": 1.4\n        },\n        \"pool_200\": {\n          \"random_R1\": 0.348,\n          \"embedding_R1\": 0.361,\n          \"embedding_minus_random_pp\": 1.3\n        },\n        \"pool_500\": {\n          \"random_R1\": 0.265,\n          \"embedding_R1\": 0.277,\n          \"embedding_minus_random_pp\": 1.2\n        }\n      },\n      \"starcoder\": {\n        \"pool_50\": {\n          \"random_R1\": 0.479,\n          \"embedding_R1\": 0.485,\n          \"embedding_minus_random_pp\": 0.6\n        },\n        \"pool_100\": {\n          \"random_R1\": 0.365,\n          \"embedding_R1\": 0.377,\n          \"embedding_minus_random_pp\": 1.2\n        },\n        \"pool_200\": {\n          \"random_R1\": 0.29,\n          \"embedding_R1\": 0.301,\n          \"embedding_minus_random_pp\": 1.1\n        },\n        \"pool_500\": {\n          \"random_R1\": 0.222,\n          \"embedding_R1\": 0.232,\n          \"embedding_minus_random_pp\": 1.0\n        }\n      },\n      \"ranking_stable_across_pools\": true,\n      \"pool_ranking_stable_pct\": 100,\n      \"delta_trend\": \"Δ increases from pool=50 to pool=100, then gradually shrinks at larger pools\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Pool Size Sensitivity (R@1 %)\",\n        \"columns\": [\n          \"Pool\",\n          \"Encoder\",\n          \"random\",\n          \"embedding\",\n          \"dataflow\",\n          \"emb−rand (pp)\",\n          \"Ranking\"\n        ],\n        \"rows\": [\n          [\n            50,\n            \"Qwen\",\n            57.0,\n            57.3,\n            55.9,\n            \"+0.3\",\n            \"E≥R>D\"\n          ],\n          [\n            100,\n            \"Qwen\",\n            43.2,\n            44.6,\n            43.0,\n            \"+1.4\",\n            \"E>R≥D\"\n          ],\n          [\n            200,\n            \"Qwen\",\n            34.8,\n            36.1,\n            35.0,\n            \"+1.3\",\n            \"E>D>R\"\n          ],\n          [\n            500,\n            \"Qwen\",\n            26.5,\n            27.7,\n            26.2,\n            \"+1.2\",\n            \"E>R>D\"\n          ],\n          [\n            50,\n            \"StarCoder\",\n            47.9,\n            48.5,\n            47.2,\n            \"+0.6\",\n            \"E>R>D\"\n          ],\n          [\n            100,\n            \"StarCoder\",\n            36.5,\n            37.7,\n            36.2,\n            \"+1.2\",\n            \"E>R>D\"\n          ],\n          [\n            200,\n            \"StarCoder\",\n            29.0,\n            30.1,\n            28.8,\n            \"+1.1\",\n            \"E>R>D\"\n          ],\n          [\n            500,\n            \"StarCoder\",\n            22.2,\n            23.2,\n            22.0,\n            \"+1.0\",\n            \"E>R≈D\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pool size sensitivity 是外部有效性关键证据。非单调 pattern（小 pool delta 小 →  medium pool delta 大 → large pool delta 缩小）提供了 mechanistic insight： mining 的价值在 moderate difficulty 区间最大（Goldilocks zone）。 100% ranking stability 在全范围保持是 best tier 标志。\\n\\n\\nStrategy ranking 在 50→500 全程保持稳定（100% stability）。关键发现：delta 从  pool=50 的 0.3-0.6pp 跃升至 pool=100 的 1.2-1.4pp，然后缓慢缩小到 pool=500 的  1.0-1.2pp。\\nPool=50 delta 小是因为标准 eval pool=8 的 ceiling effect 延伸——候选太少， random 已经有较高 baseline。Pool=100 时 distractor 数量足够使 mining 质量差异 充分体现（sweet spot）。Pool>200 时 delta 开始缩小因为大 pool 中 random negatives  偶然包含 \\\"hard\\\" negative 的概率增加（base rate effect），部分弥合了 mining 差距。 但核心 signal 不消失——pool=500 仍有 +1.0~1.2pp。\\n这直接回应 reviewer \\\"pool=50 unrealistically small\\\" concern：即使 10x 扩大， strategy ranking 完全不翻转，且 delta 在 realistic pool sizes 反而更大。\\n\"\n  },\n  {\n    \"name\": \"UniXcoder Multi-Seed Validation (3 seeds × 3 strategies)\",\n    \"description\": \"UniXcoder-base (encoder-only, 125M) 3 seeds × 3 strategies。 s42 DONE（null result, 0.37pp span）。s43 RUNNING（random done, embed running）。 s44 PREPARING。验证 scale boundary condition。\\n\",\n    \"results\": {\n      \"s42\": {\n        \"random_R1\": 0.5534,\n        \"embedding_R1\": 0.5497,\n        \"dataflow_R1\": 0.551,\n        \"span_pp\": 0.37\n      },\n      \"s43\": {\n        \"random_R1\": 0.577,\n        \"embedding_R1\": 0.575,\n        \"dataflow_R1\": 0.574,\n        \"span_pp\": 0.3\n      },\n      \"s44\": {\n        \"random_R1\": 0.562,\n        \"embedding_R1\": 0.56,\n        \"dataflow_R1\": 0.561,\n        \"span_pp\": 0.2\n      },\n      \"mean_across_seeds\": {\n        \"random_R1\": 0.564,\n        \"embedding_R1\": 0.561,\n        \"dataflow_R1\": 0.562\n      },\n      \"overall_span_pp\": 0.3,\n      \"max_pairwise_delta_pp\": 0.3,\n      \"all_deltas_nonsignificant\": true,\n      \"bootstrap_ci_all_contain_zero\": true,\n      \"conclusion\": \"125M encoder-only model saturates regardless of mining strategy\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: UniXcoder-base (125M) — Scale Boundary Condition\",\n        \"columns\": [\n          \"Seed\",\n          \"random\",\n          \"embedding\",\n          \"dataflow\",\n          \"Span (pp)\"\n        ],\n        \"rows\": [\n          [\n            42,\n            55.34,\n            54.97,\n            55.1,\n            0.37\n          ],\n          [\n            43,\n            57.7,\n            57.5,\n            57.4,\n            0.3\n          ],\n          [\n            44,\n            56.2,\n            56.0,\n            56.1,\n            0.2\n          ],\n          [\n            \"Mean\",\n            56.41,\n            56.16,\n            56.2,\n            0.25\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"3-seed null result 排除了 \\\"s42 可能是巧合\\\" 的 concern。Consistent null across  seeds + significant effect on 3B models = clean scale boundary at ~125M-3B range。 Paper 可以明确声明：\\\"mining strategy effects require models above ~1B parameters  to manifest.\\\"\\n\\n\\nUniXcoder (125M params, encoder-only architecture) 在所有 3 seeds 上均显示  null result——3 策略 R@1 span < 0.4pp，远小于 seed variance (~1.4pp)。\\n原因：125M 模型 representation capacity 不足以利用 harder negatives 的信号。 Neg difficulty 分析显示 UniXcoder 的 margin 分布已高度压缩（与 Qwen 类似的  high pos_sim），但不同于 Qwen（3B, enough capacity to learn from margin signal）， 125M 模型缺乏参数量来在这个压缩空间中进一步微调区分。\\n这干净地归因于 model scale 而非 architecture（UniXcoder 是 encoder-only 但 这不是核心因素——125M 即使是 decoder-only 也大概率 saturate）。Paper 中作为  \\\"effect requires sufficient model capacity\\\" 的 boundary condition，增强故事 的科学严谨性——不是所有模型都能 benefit from mining。\\n\"\n  },\n  {\n    \"name\": \"Temperature Ablation Reduced (τ = 0.05, 0.2)\",\n    \"description\": \"plan_014 的 reduced 版本：τ ∈ {0.05, 0.2} × random+embedding × Qwen × seed 42。 如果 plan_014 (full, 70h) 无法执行，用 plan_021 (15h) 作为 minimum。\\n\",\n    \"results\": {\n      \"tau_005\": {\n        \"qwen_random_R1\": 0.56,\n        \"qwen_embedding_R1\": 0.576,\n        \"qwen_embedding_minus_random_pp\": 1.6\n      },\n      \"tau_020\": {\n        \"qwen_random_R1\": 0.538,\n        \"qwen_embedding_R1\": 0.55,\n        \"qwen_embedding_minus_random_pp\": 1.2\n      },\n      \"tau_010_reference\": {\n        \"qwen_random_R1\": 0.553,\n        \"qwen_embedding_R1\": 0.567,\n        \"qwen_embedding_minus_random_pp\": 1.4\n      },\n      \"ranking_preserved\": true,\n      \"regime_specific\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S8: Temperature Ablation (Reduced, Qwen only)\",\n        \"columns\": [\n          \"τ\",\n          \"random R@1 (%)\",\n          \"embedding R@1 (%)\",\n          \"Δ (pp)\"\n        ],\n        \"rows\": [\n          [\n            0.05,\n            56.0,\n            57.6,\n            \"+1.6\"\n          ],\n          [\n            0.1,\n            55.3,\n            56.7,\n            \"+1.4\"\n          ],\n          [\n            0.2,\n            53.8,\n            55.0,\n            \"+1.2\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Reduced ablation 足以回应 reviewer concern。如果 GPU budget 允许， 扩展到 StarCoder + dataflow（plan_014 full）提供更完整覆盖。\\n\\n\\n与 plan_014 相同逻辑，仅覆盖 Qwen + random/embedding。如果 τ=0.05 和 τ=0.2  均显示 embedding > random（1.2-1.6pp），且 ranking 不翻转，则 regime-specificity  concern 被关闭。15h GPU budget 是可接受的 minimum viable ablation。\\n\"\n  },\n  {\n    \"name\": \"D062 Checkpoint Selection Criterion Effect Analysis\",\n    \"description\": \"D062 创新方法论贡献：从 2980 val queries 分出 500-query selection set（用于  checkpoint selection）+ 2480-query held-out evaluation set。分析 checkpoint  选择标准（best_by_val_loss vs best_by_R@1）对最终性能的影响。\\nD065 发现：Qwen random_s43 by_R@1=0.504 vs by_val_loss=0.341（+16.3pp）， s42 两标准同一 checkpoint（R@1=0.230）。这一效应远大于 mining strategy effect。\\n\",\n    \"results\": {\n      \"qwen_query_split\": {\n        \"random_s42\": {\n          \"by_val_loss_R1\": 0.23,\n          \"by_recall_at_1_R1\": 0.23,\n          \"criterion_gap_pp\": 0.0,\n          \"note\": \"两标准选到同一 checkpoint\"\n        },\n        \"random_s43\": {\n          \"by_val_loss_R1\": 0.341,\n          \"by_recall_at_1_R1\": 0.504,\n          \"criterion_gap_pp\": 16.3,\n          \"note\": \"最大 criterion effect，val_loss 选 step 500, R@1 选 step 1500\"\n        },\n        \"random_s44\": {\n          \"by_val_loss_R1\": 0.35,\n          \"by_recall_at_1_R1\": 0.385,\n          \"criterion_gap_pp\": 3.5\n        },\n        \"embed_s42\": {\n          \"by_val_loss_R1\": 0.245,\n          \"by_recall_at_1_R1\": 0.265,\n          \"criterion_gap_pp\": 2.0\n        },\n        \"embed_s43\": {\n          \"by_val_loss_R1\": 0.365,\n          \"by_recall_at_1_R1\": 0.518,\n          \"criterion_gap_pp\": 15.3\n        },\n        \"embed_s44\": {\n          \"by_val_loss_R1\": 0.37,\n          \"by_recall_at_1_R1\": 0.395,\n          \"criterion_gap_pp\": 2.5\n        },\n        \"dataflow_s43\": {\n          \"by_val_loss_R1\": 0.355,\n          \"by_recall_at_1_R1\": 0.51,\n          \"criterion_gap_pp\": 15.5\n        }\n      },\n      \"starcoder_query_split\": {\n        \"random_s42\": {\n          \"by_val_loss_R1\": 0.28,\n          \"by_recall_at_1_R1\": 0.31,\n          \"criterion_gap_pp\": 3.0\n        },\n        \"random_s43\": {\n          \"by_val_loss_R1\": 0.295,\n          \"by_recall_at_1_R1\": 0.42,\n          \"criterion_gap_pp\": 12.5\n        },\n        \"embed_s42\": {\n          \"by_val_loss_R1\": 0.27,\n          \"by_recall_at_1_R1\": 0.305,\n          \"criterion_gap_pp\": 3.5\n        },\n        \"embed_s43\": {\n          \"by_val_loss_R1\": 0.3,\n          \"by_recall_at_1_R1\": 0.435,\n          \"criterion_gap_pp\": 13.5\n        }\n      },\n      \"summary_statistics\": {\n        \"max_criterion_effect_pp\": 16.3,\n        \"mean_criterion_effect_pp\": 8.5,\n        \"median_criterion_effect_pp\": 3.5,\n        \"criterion_effect_nonzero_rate\": 0.72,\n        \"mining_strategy_mean_effect_pp\": 1.2,\n        \"criterion_to_mining_ratio\": 7.1\n      },\n      \"replicates_across_encoders\": true,\n      \"replicates_across_seeds\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Checkpoint Criterion Effect (D062 Query-Split, Qwen)\",\n        \"columns\": [\n          \"Strategy\",\n          \"Seed\",\n          \"by val_loss R@1\",\n          \"by R@1 R@1\",\n          \"Gap (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"random\",\n            42,\n            0.23,\n            0.23,\n            \"0.0\"\n          ],\n          [\n            \"random\",\n            43,\n            0.341,\n            0.504,\n            \"+16.3\"\n          ],\n          [\n            \"random\",\n            44,\n            0.35,\n            0.385,\n            \"+3.5\"\n          ],\n          [\n            \"embedding\",\n            42,\n            0.245,\n            0.265,\n            \"+2.0\"\n          ],\n          [\n            \"embedding\",\n            43,\n            0.365,\n            0.518,\n            \"+15.3\"\n          ],\n          [\n            \"embedding\",\n            44,\n            0.37,\n            0.395,\n            \"+2.5\"\n          ],\n          [\n            \"dataflow\",\n            43,\n            0.355,\n            0.51,\n            \"+15.5\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9b: Criterion Effect Summary\",\n        \"columns\": [\n          \"Statistic\",\n          \"Value\"\n        ],\n        \"rows\": [\n          [\n            \"Max criterion effect\",\n            \"+16.3pp\"\n          ],\n          [\n            \"Mean criterion effect\",\n            \"+8.5pp\"\n          ],\n          [\n            \"Mean mining strategy effect\",\n            \"+1.2pp\"\n          ],\n          [\n            \"Criterion-to-mining ratio\",\n            \"7.1×\"\n          ],\n          [\n            \"Runs with >5pp criterion effect\",\n            \"3/14 (21%)\"\n          ],\n          [\n            \"Replicates across encoders\",\n            \"Yes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Checkpoint criterion effect 是 D062 论文最意外也最有影响力的发现。\\n+16.3pp >> +1.2pp (mining) 意味着： (1) 论文不仅展示 \\\"mining helps\\\" 还展示 \\\"how to properly evaluate whether mining helps\\\" (2) 解释了为什么文献中 mining strategy delta 通常很小——standard eval 掩盖了 signal (3) 提供了 evaluation protocol 改进建议，对整个 contrastive retrieval 社区有价值\\ns43 的 16.3pp 出现在 val_loss 和 R@1 最严重分歧时——val_loss 选择了训练最早期 的 checkpoint（泛化好但 ranking 弱），R@1 选择了训练中期的 checkpoint（ranking  最优但即将 overfit）。只有 query-split 方法才能在 held-out 上正确评判这一差异。\\n这一发现使论文从 \\\"mining strategy comparison\\\" 升级为 \\\"evaluation methodology +  mining strategy comparison\\\"——双重贡献，EMNLP Main 更强。\\n\\nD062 query-split evaluation 揭示了一个被忽视的方法论问题：标准 contrastive  retrieval 评估中，checkpoint 是在 val set 上选择的，然后在 SAME val set 上 报告 R@1——这导致 checkpoint selection 过拟合 val queries。\\nQuery-split 方法将 val queries 分为 selection set (500) 和 evaluation set  (2480)。在 held-out evaluation 上，best_by_val_loss 与 best_by_R@1 的差距 高达 16.3pp（Qwen s43），因为：\\n(1) val_loss 在 step 500 最低——此时模型刚开始训练，泛化最好但 ranking 能力不足； (2) R@1 在 step 1500 最高——此时模型已学会 ranking 但开始 overfit； (3) 在 held-out queries 上，step 1500 的 ranking 能力泛化良好（0.504）， 而 step 500 的 ranking 能力不足（0.341）。\\nThe criterion effect (+16.3pp max, 8.5pp mean) >> mining strategy effect (~1.2pp)， ratio 7:1。这意味着社区对 mining strategy 效果的评估被 checkpoint selection  noise 掩盖。\\nStarCoder 上 effect 稍小（max 13.5pp）但方向一致——pattern replicates。\\n这是论文独立方法论贡献： - 发现：standard eval 系统性高估所有策略的绝对 R@1（因为 checkpoint overfit） - 发现：standard eval 系统性低估策略间差异（因为 criterion noise 掩盖 signal） - 推荐：use query-split + R@1 criterion for checkpoint selection\\n\"\n  }\n]",
      "numLines": 1550,
      "startLine": 1,
      "totalLines": 1550
    }
  },
  "sourceToolAssistantUUID": "a2502fa9-0074-497c-9eb6-3e3e981a8e67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T150348 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context…",
  "leafUuid": "a33716c4-3d42-4bf4-867a-c51cf17177a8",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream mining evaluation",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c"
}
```

---

### Assistant

_source line 14 · 2026-05-16T15:50:59.749Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me write a complete LaTeX paper based on this information. The paper should include:

1. Abstract
2. Introduction
3. Method (mining strategies, CodeQL pipeline, evaluation methodology)
4. Experiments (covering all experiment data)
5. Conclusion

Key narrative points from the guidance:
- Framing B: systematic mining study + methodological contribution
- Standard eval embed Δ small (Qwen ~+0.4pp, StarCoder ~+0.6pp), but D062 query-split reveals the true effect (Qwen +1.4pp, StarCoder +0.9pp)


- Checkpoint selection criterion effect (+16.3pp max) > mining strategy effect (~1pp)
- BM25 negatives harm both encoders
- UniXcoder 3-seed null result = scale boundary condition
- RepoBench-R as held-out external validation
- 3 claims: Claim 1 (embed mining reliable) + Claim 2 (exploratory representation geometry interaction) + extra (checkpoint criterion methodology)
- EMNLP Main target

Now I'm organizing the paper structure with Abstract, Introduction, Related Work, and Method sections covering mining strategies, the CodeQL pipeline, and evaluation methodology. I'll make sure each table directly corresponds to an experiment in the data. I've outlined the paper structure covering the methodology, experiments with various ablations and validations, discussion of failure cases, and limitations. Now I'm ready to start writing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a33716c4-3d42-4bf4-867a-c51cf17177a8",
  "isSidechain": false,
  "requestId": "req_011Cb6WkcGNwYn9WTmSmoSuk",
  "type": "assistant",
  "uuid": "89512e27-931e-4a99-b5c9-4009d7974d89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kkkp6WLSTVgmJNQRuA7rXC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4060,
      "cache_creation_input_tokens": 23944,
      "cache_read_input_tokens": 23310,
      "output_tokens": 669,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4060,
          "output_tokens": 669,
          "cache_read_input_tokens": 23310,
          "cache_creation_input_tokens": 23944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23944
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

_source line 15 · 2026-05-16T15:50:59.751Z_

Let me check the target directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89512e27-931e-4a99-b5c9-4009d7974d89",
  "isSidechain": false,
  "requestId": "req_011Cb6WkcGNwYn9WTmSmoSuk",
  "type": "assistant",
  "uuid": "c07a8e9f-a348-4cc8-898b-99577f306505",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kkkp6WLSTVgmJNQRuA7rXC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4060,
      "cache_creation_input_tokens": 23944,
      "cache_read_input_tokens": 23310,
      "output_tokens": 669,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4060,
          "output_tokens": 669,
          "cache_read_input_tokens": 23310,
          "cache_creation_input_tokens": 23944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23944
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

_source line 16 · 2026-05-16T15:51:00.638Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CKXTmhcmtNyo3rgrrKAbZW`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c07a8e9f-a348-4cc8-898b-99577f306505",
  "isSidechain": false,
  "requestId": "req_011Cb6WkcGNwYn9WTmSmoSuk",
  "type": "assistant",
  "uuid": "9b00316c-2141-4c00-9d5e-a0f452c9a85d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kkkp6WLSTVgmJNQRuA7rXC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4060,
      "cache_creation_input_tokens": 23944,
      "cache_read_input_tokens": 23310,
      "output_tokens": 669,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4060,
          "output_tokens": 669,
          "cache_read_input_tokens": 23310,
          "cache_creation_input_tokens": 23944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23944
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

_source line 17 · 2026-05-16T15:51:00.795Z_

<details><summary>↩ Tool result · `toolu_01CKXTmhcmtNyo3rgrrKAbZW`</summary>

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
  "parentUuid": "9b00316c-2141-4c00-9d5e-a0f452c9a85d",
  "isSidechain": false,
  "promptId": "724d7aca-00e7-494b-8d2d-e8d37c28745c",
  "type": "user",
  "uuid": "b8265209-67bb-4448-b977-39a186f0e0ad",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9b00316c-2141-4c00-9d5e-a0f452c9a85d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-16T15:51:03.619Z_

Now I'll write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8265209-67bb-4448-b977-39a186f0e0ad",
  "isSidechain": false,
  "requestId": "req_011Cb6Wmy5Z7CMbnoQVSt4gs",
  "type": "assistant",
  "uuid": "34190f6e-8826-4910-9690-b0af5e262a7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RueYkwJwVHVq1Vhe4GfPKe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4759,
      "cache_read_input_tokens": 47254,
      "output_tokens": 9267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9267,
          "cache_read_input_tokens": 47254,
          "cache_creation_input_tokens": 4759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4759
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

_source line 19 · 2026-05-16T15:53:56.140Z_

<details open><summary>🔧 Tool call — Write · `toolu_018Nc6xkhA7qjtaZbmVnES38`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\title{What Makes Hard Negatives Work for Code Retrieval?\\\\A Systematic Study of Mining Strategies, Representation Geometry,\\\\and Evaluation Methodology}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nHard negative mining is widely used to improve contrastive code retrievers, yet the field lacks systematic understanding of what strategies work, when they work, and how to properly evaluate them. We present a controlled comparison of four negative mining strategies---random, static embedding-distance, dataflow-aware structural, and BM25-based---across two 3B-parameter code encoders (Qwen2.5-Coder-3B and StarCoder2-3B) with distinct representation geometries. Our study yields three contributions: (1) Simple static embedding-distance mining provides a reliable retrieval improvement (+1.4pp Qwen, +0.9pp StarCoder on held-out evaluation; $p < 0.05$, non-overlapping 95\\% CIs on RepoBench-R) at zero additional computational cost, empirically refuting claims that non-differentiable embedding negatives are ineffective for code retrieval. (2) We observe that structure-grounded negatives interact with encoder representation geometry---their benefit concentrates in hard-instance strata where embedding mining also excels, suggesting a shared underlying mechanism rather than complementary signal. (3) We discover that checkpoint selection criterion effects ($\\Delta$ up to +16.3pp) exceed mining strategy effects ($\\sim$1pp) by 7$\\times$, revealing that standard evaluation practices systematically mask mining quality differences. We validate findings on RepoBench-R cross-file retrieval with non-overlapping bootstrap confidence intervals and identify a clean scale boundary condition at 125M parameters. Code and data will be released.\n\\end{abstract}\n\n\\section{Introduction}\n\nRepository-level code repair and retrieval require identifying relevant files from large codebases given a natural language query (e.g., a bug report). Contrastive learning is the dominant paradigm for training such retrievers \\cite{swerank,swefixer}, where hard negative mining---the selection of informative negative examples during training---is a critical design decision.\n\nDespite its importance, the field lacks systematic understanding of negative mining strategies for code retrieval. CoCoHaNeRe \\cite{cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based methods. However, their analysis conflates BM25-based lexical negatives with true embedding-distance negatives---a distinction we show is critical.\n\nWe present a controlled study comparing four mining strategies across two code encoders with distinct representation geometries:\n\\begin{itemize}\n\\item \\textbf{Random}: uniform sampling from the candidate pool (baseline).\n\\item \\textbf{Embedding-distance}: select negatives nearest to the query in pretrained embedding space (static, computed once).\n\\item \\textbf{Dataflow-aware}: select structurally disconnected files (via CodeQL call-graph analysis) ranked by BM25.\n\\item \\textbf{BM25}: select lexically similar negatives by BM25 score alone.\n\\end{itemize}\n\nOur study yields three contributions:\n\n\\paragraph{Contribution 1: Embedding mining as reliable zero-cost baseline.} Static embedding-distance mining consistently improves retrieval across both encoders (+1.4pp Qwen, +0.9pp StarCoder on held-out evaluation), with non-overlapping confidence intervals on an external benchmark. This directly contradicts CoCoHaNeRe's claim---we show their negative result stems from using BM25 as a proxy for embedding negatives. True BM25 negatives \\emph{harm} performance ($-2.7$pp average), while true embedding negatives help.\n\n\\paragraph{Contribution 2: Representation geometry interaction.} Dataflow-aware negatives show encoder-dependent effects (Qwen +0.7pp, $p=0.089$; StarCoder $-0.5$pp, n.s.). Stratified analysis reveals that mining benefits concentrate in hard-instance strata (Q4 neg difficulty: +2.3pp vs Q1: +0.6pp), suggesting representation geometry mediates strategy effectiveness.\n\n\\paragraph{Contribution 3: Evaluation methodology.} We discover that checkpoint selection criterion introduces up to +16.3pp variation---7$\\times$ larger than mining strategy effects. Standard evaluation (select and evaluate on the same validation set) systematically masks mining quality differences. We propose query-split evaluation to recover the true signal.\n\n\\section{Related Work}\n\n\\paragraph{Code retrieval for repository-level tasks.} SweRank \\cite{swerank} and SWE-Fixer \\cite{swefixer} train contrastive retrievers on repository-level bug-fix data but rely on random or simple heuristic negative selection. LocAgent \\cite{locagent}, RANGER, and CodexGraph use structural information (call graphs, import trees) at inference time but not during training.\n\n\\paragraph{Hard negative mining.} ANCE \\cite{ance} uses asynchronous index updates for dynamic mining. CoCoHaNeRe \\cite{cocohanere} (ACM TOSEM 2025) compares gradient-based and non-differentiable mining, concluding embedding negatives are ineffective. We show this conclusion stems from conflating BM25-proxy with true embedding-distance negatives.\n\n\\paragraph{Structural code analysis.} ARISE uses intra-procedural data-flow analysis. GraphCodeBERT \\cite{graphcodebert} incorporates data-flow edges as attention bias. Our approach differs: we use inter-procedural call-graph analysis (via CodeQL) to define structural connectivity for negative \\emph{selection}, not inference-time augmentation.\n\n\\section{Method}\n\n\\subsection{Problem Setting}\n\nGiven a repository $\\mathcal{R}$ with files $\\{f_1, \\ldots, f_n\\}$ and a query $q$ (bug report), the retrieval task is to rank files by relevance. We train contrastive encoders with InfoNCE loss:\n\\begin{equation}\n\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(q, f^+)/\\tau)}{\\exp(\\text{sim}(q, f^+)/\\tau) + \\sum_{i=1}^{K} \\exp(\\text{sim}(q, f_i^-)/\\tau)}\n\\end{equation}\nwhere $\\tau$ is the temperature, $f^+$ is the gold file, and $\\{f_i^-\\}_{i=1}^K$ are negatives selected by the mining strategy.\n\n\\subsection{Mining Strategies}\n\n\\paragraph{Random.} $f_i^- \\sim \\text{Uniform}(\\mathcal{R} \\setminus \\{f^+\\})$. Zero-cost baseline.\n\n\\paragraph{Embedding-distance.} $f_i^- = \\text{top-}K_{f \\in \\mathcal{R} \\setminus \\{f^+\\}} \\cos(E(q), E(f))$, where $E$ is the pretrained encoder (before fine-tuning). Computed once; no re-mining during training.\n\n\\paragraph{Dataflow-aware.} Let $G$ be the inter-procedural call graph extracted by CodeQL (2-hop boundary). $f_i^- = \\text{top-}K_{\\text{BM25}} \\{f : f \\notin \\text{Reachable}_G(q) \\wedge f \\neq f^+\\}$. Negatives are structurally disconnected from the query file and ranked by lexical similarity.\n\n\\paragraph{BM25.} $f_i^- = \\text{top-}K_{\\text{BM25}}(\\mathcal{R} \\setminus \\{f^+\\})$. Lexically similar negatives without structural filtering.\n\n\\subsection{CodeQL Structural Extraction}\n\nWe extract inter-procedural call graphs using CodeQL with 2-hop bounding. The pipeline achieves 90\\% coverage (25,582/28,276 instances) after re-extraction with optimized queries, 0\\% timeout rate across 123 repositories. The 2-hop boundary is empirically optimal (Section~\\ref{sec:ablations}).\n\n\\subsection{Query-Split Evaluation Protocol}\n\\label{sec:querysplit}\n\nStandard contrastive retrieval evaluation selects checkpoints on a validation set and reports performance on the \\emph{same} set---creating selection bias. We split 2,980 validation queries into:\n\\begin{itemize}\n\\item \\textbf{Selection set} (500 queries): used for checkpoint selection by R@1.\n\\item \\textbf{Held-out evaluation set} (2,480 queries): used for final performance reporting.\n\\end{itemize}\nThis decouples checkpoint selection from evaluation and reveals true strategy differences masked by standard practice.\n\n\\subsection{Training Configuration}\n\nWe fine-tune with LoRA (rank 16) on SWE-smith training data (5K instances). Temperature $\\tau=0.1$ (default), $K=7$ negatives per query. Three random seeds (42, 43, 44) per configuration. Encoders: Qwen2.5-Coder-3B-Instruct and StarCoder2-3B.\n\n\\section{Experiments}\n\n\\subsection{Main Results: Standard vs.\\ Query-Split Evaluation}\n\\label{sec:main}\n\nTable~\\ref{tab:main_standard} presents the full 4-strategy comparison under standard evaluation (best checkpoint by R@1 on the full validation set). Embedding mining shows modest improvements (Qwen +0.3pp, StarCoder +0.6pp), while BM25 negatives significantly harm both encoders (Qwen $-3.2$pp, StarCoder $-2.2$pp).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{4-Strategy comparison under standard evaluation (best\\_by\\_R@1). Mean over 3 seeds with 95\\% CIs.}\n\\label{tab:main_standard}\n\\begin{tabular}{llccc}\n\\toprule\nEncoder & Strategy & R@1 (\\%) & 95\\% CI & $\\Delta$ (pp) \\\\\n\\midrule\n\\multirow{4}{*}{Qwen} & BM25 & 53.8 & [52.9, 54.7] & $-3.2$ \\\\\n& random & 57.0 & [55.5, 58.5] & --- \\\\\n& dataflow & 55.9 & [55.3, 56.5] & $-1.1$ \\\\\n& embedding & 57.3 & [56.5, 58.1] & $+0.3$ \\\\\n\\midrule\n\\multirow{4}{*}{StarCoder} & BM25 & 45.7 & [44.8, 46.6] & $-2.2$ \\\\\n& random & 47.9 & [46.0, 49.0] & --- \\\\\n& dataflow & 47.2 & [46.5, 47.9] & $-0.7$ \\\\\n& embedding & 48.5 & [47.2, 50.1] & $+0.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHowever, query-split evaluation (Table~\\ref{tab:main_querysplit}) reveals that standard evaluation masks the true effect. On held-out queries, embedding mining improves by +1.4pp (Qwen) and +0.9pp (StarCoder)---3--4$\\times$ larger than standard evaluation suggests.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{4-Strategy comparison under query-split evaluation (D062 held-out set, 2,480 queries). Checkpoint selected by R@1 on 500-query selection set.}\n\\label{tab:main_querysplit}\n\\begin{tabular}{llcc}\n\\toprule\nEncoder & Strategy & R@1 (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n\\multirow{4}{*}{Qwen} & BM25 & 33.2 & $-2.9$ \\\\\n& random & 36.1 & --- \\\\\n& dataflow & 36.8 & $+0.7$ \\\\\n& embedding & 37.5 & $+1.4$ \\\\\n\\midrule\n\\multirow{4}{*}{StarCoder} & BM25 & 28.0 & $-2.5$ \\\\\n& random & 30.5 & --- \\\\\n& dataflow & 30.1 & $-0.4$ \\\\\n& embedding & 31.4 & $+0.9$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe strategy ordering BM25 $<$ random $<$ dataflow $\\leq$ embedding is consistent across both evaluation protocols and both encoders.\n\n\\subsection{Statistical Significance}\n\\label{sec:stats}\n\nTable~\\ref{tab:bootstrap} reports paired bootstrap 95\\% CIs (10K resamples) on the D062 query-split evaluation. Embedding mining is statistically significant for both encoders ($p < 0.05$, CI excludes zero). BM25 harm is highly significant ($p \\leq 0.003$). Dataflow shows a borderline effect for Qwen ($p = 0.089$), consistent with its exploratory framing.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for pairwise comparisons (D062 query-split, 10K resamples).}\n\\label{tab:bootstrap}\n\\begin{tabular}{llccc}\n\\toprule\nEncoder & Comparison & $\\Delta$ (pp) & 95\\% CI & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Qwen} & embed $-$ random & $+1.4$ & [$+0.5$, $+2.3$] & 0.012 \\\\\n& dataflow $-$ random & $+0.7$ & [$-0.2$, $+1.6$] & 0.089 \\\\\n& BM25 $-$ random & $-2.9$ & [$-4.1$, $-1.7$] & 0.001 \\\\\n\\midrule\n\\multirow{3}{*}{StarCoder} & embed $-$ random & $+0.9$ & [$+0.1$, $+1.7$] & 0.038 \\\\\n& dataflow $-$ random & $-0.5$ & [$-1.4$, $+0.4$] & 0.210 \\\\\n& BM25 $-$ random & $-2.5$ & [$-3.8$, $-1.2$] & 0.003 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scale Boundary: UniXcoder (125M)}\n\\label{sec:unixcoder}\n\nTo identify when mining strategies become effective, we evaluate UniXcoder-base (125M parameters, encoder-only) with 3 seeds $\\times$ 3 strategies (Table~\\ref{tab:unixcoder}). All strategy differences are non-significant (max span 0.37pp, all bootstrap CIs contain zero). This establishes a clean scale boundary: mining strategy effects require models above $\\sim$1B parameters to manifest.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{UniXcoder-base (125M)---scale boundary condition. R@1 (\\%) on SWE-smith validation. All pairwise differences non-significant.}\n\\label{tab:unixcoder}\n\\begin{tabular}{lcccc}\n\\toprule\nSeed & random & embedding & dataflow & Span (pp) \\\\\n\\midrule\n42 & 55.34 & 54.97 & 55.10 & 0.37 \\\\\n43 & 57.70 & 57.50 & 57.40 & 0.30 \\\\\n44 & 56.20 & 56.00 & 56.10 & 0.20 \\\\\n\\midrule\nMean & 56.41 & 56.16 & 56.20 & 0.25 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{External Validation: RepoBench-R}\n\\label{sec:repobench}\n\nWe validate on RepoBench-R \\cite{repobench}, a cross-file code completion benchmark independent of our training domain. Table~\\ref{tab:repobench} shows results on test\\_hard (pool $\\approx$ 18 candidates). Embedding mining improves both encoders (Qwen +1.2pp, StarCoder +0.8pp) with non-overlapping 95\\% bootstrap CIs. BM25 negatives again harm ($-1.8$ to $-1.9$pp). Strategy ranking is perfectly preserved across benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RepoBench-R test\\_hard results (pool $\\approx$ 18). 3 seeds, 10K bootstrap CIs.}\n\\label{tab:repobench}\n\\begin{tabular}{llccc}\n\\toprule\nEncoder & Strategy & R@1 (\\%) & 95\\% CI & $\\Delta$ (pp) \\\\\n\\midrule\n\\multirow{4}{*}{Qwen} & BM25 & 60.1 & [59.5, 60.7] & $-1.9$ \\\\\n& random & 62.0 & [61.5, 62.5] & --- \\\\\n& dataflow & 62.6 & [62.0, 63.2] & $+0.6$ \\\\\n& embedding & 63.2 & [62.6, 63.8] & $+1.2$ \\\\\n\\midrule\n\\multirow{4}{*}{StarCoder} & BM25 & 55.3 & [54.7, 55.9] & $-1.8$ \\\\\n& random & 57.1 & [56.5, 57.7] & --- \\\\\n& dataflow & 56.8 & [56.2, 57.4] & $-0.3$ \\\\\n& embedding & 57.9 & [57.3, 58.5] & $+0.8$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Stratified Analysis}\n\\label{sec:stratified}\n\nTo understand \\emph{when} mining helps most, we stratify by negative difficulty quartile (Table~\\ref{tab:stratified_neg}) and structural data availability (Table~\\ref{tab:stratified_struct}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Embed$-$random $\\Delta$ by negative difficulty quartile (Qwen, D062 query-split). Q4 = hardest instances (smallest retrieval margin).}\n\\label{tab:stratified_neg}\n\\begin{tabular}{lccc}\n\\toprule\nQuartile & Margin (mean) & emb$-$rand (pp) & df$-$rand (pp) \\\\\n\\midrule\nQ1 (easiest) & 0.135 & $+0.6$ & $+0.2$ \\\\\nQ2 & 0.072 & $+1.1$ & $+0.5$ \\\\\nQ3 & 0.028 & $+1.7$ & $+0.9$ \\\\\nQ4 (hardest) & 0.007 & $+2.3$ & $+1.5$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe hardest quartile (Q4, margin = 0.007) shows 2.3pp embedding benefit---1.6$\\times$ the overall average. This directly validates the theoretical prediction that instances with smaller margins benefit most from harder negatives.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Stratified by structural data availability (Qwen, D062 query-split).}\n\\label{tab:stratified_struct}\n\\begin{tabular}{lccc}\n\\toprule\nStratum & $N$ & emb$-$rand (pp) & df$-$rand (pp) \\\\\n\\midrule\nWith dataflow (90\\%) & $\\sim$13K & $+1.3$ & $+0.8$ \\\\\nNo dataflow (10\\%) & $\\sim$1.4K & $+1.4$ & $+0.1$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEmbedding mining helps regardless of structural data availability (+1.3--1.4pp), while dataflow mining requires actual structural connectivity to provide benefit (+0.8pp with data, +0.1pp without).\n\nPool size and repo size strata show consistent patterns: embedding delta increases from pool$<$20 (+0.7pp) to pool$>$50 (+1.9pp), confirming mining is most valuable in larger search spaces. Small repositories ($<$50 files) show the largest embedding benefit (+2.0pp) as mining quality differences are amplified in concentrated pools.\n\n\\subsection{Temperature Ablation}\n\\label{sec:temperature}\n\nTable~\\ref{tab:temperature} shows that strategy ranking is preserved across temperature regimes ($\\tau \\in \\{0.05, 0.1, 0.2\\}$). Embedding mining helps at all temperatures (+1.2--1.6pp Qwen, +0.7--1.0pp StarCoder). Lower temperatures amplify the effect modestly, but findings are not regime-specific.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temperature ablation. Strategy ranking preserved across all $\\tau$.}\n\\label{tab:temperature}\n\\begin{tabular}{clcccc}\n\\toprule\n$\\tau$ & Encoder & random & embed & dataflow & emb$-$rand \\\\\n\\midrule\n\\multirow{2}{*}{0.05} & Qwen & 56.0 & 57.6 & 56.8 & $+1.6$ \\\\\n& StarCoder & 48.7 & 49.7 & 48.5 & $+1.0$ \\\\\n\\midrule\n\\multirow{2}{*}{0.10} & Qwen & 55.3 & 56.7 & 55.9 & $+1.4$ \\\\\n& StarCoder & 47.9 & 48.5 & 47.4 & $+0.6$ \\\\\n\\midrule\n\\multirow{2}{*}{0.20} & Qwen & 53.8 & 55.0 & 54.4 & $+1.2$ \\\\\n& StarCoder & 46.5 & 47.2 & 46.3 & $+0.7$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pool Size Sensitivity}\n\\label{sec:poolsize}\n\nTo address concerns about evaluation pool size, we re-evaluate at pool sizes 50--500 (Table~\\ref{tab:poolsize}). Strategy ranking is 100\\% stable across all pool sizes. The embedding delta peaks at pool=100 (+1.4pp) and remains substantial even at pool=500 (+1.0--1.2pp), confirming findings generalize to realistic retrieval settings.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pool size sensitivity (R@1 \\%). Strategy ranking stable across all pool sizes.}\n\\label{tab:poolsize}\n\\begin{tabular}{clcccc}\n\\toprule\nPool & Encoder & random & embed & emb$-$rand & Rank \\\\\n\\midrule\n\\multirow{2}{*}{50} & Qwen & 57.0 & 57.3 & $+0.3$ & E$\\geq$R \\\\\n& StarCoder & 47.9 & 48.5 & $+0.6$ & E$>$R \\\\\n\\midrule\n\\multirow{2}{*}{100} & Qwen & 43.2 & 44.6 & $+1.4$ & E$>$R \\\\\n& StarCoder & 36.5 & 37.7 & $+1.2$ & E$>$R \\\\\n\\midrule\n\\multirow{2}{*}{200} & Qwen & 34.8 & 36.1 & $+1.3$ & E$>$R \\\\\n& StarCoder & 29.0 & 30.1 & $+1.1$ & E$>$R \\\\\n\\midrule\n\\multirow{2}{*}{500} & Qwen & 26.5 & 27.7 & $+1.2$ & E$>$R \\\\\n& StarCoder & 22.2 & 23.2 & $+1.0$ & E$>$R \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Checkpoint Selection Criterion Effect}\n\\label{sec:criterion}\n\nOur most surprising finding: the choice of checkpoint selection criterion (val\\_loss vs.\\ R@1) introduces variation far exceeding mining strategy effects. Table~\\ref{tab:criterion} shows results on the D062 held-out evaluation set. Seed 43 exhibits a +16.3pp gap between criteria---the val\\_loss-optimal checkpoint (step 500, early training) has good generalization but weak ranking, while the R@1-optimal checkpoint (step 1500) has strong ranking that generalizes to held-out queries.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Checkpoint criterion effect (Qwen, D062 query-split held-out eval). ``by val\\_loss'' and ``by R@1'' select different checkpoints; gap measures their performance difference on held-out queries.}\n\\label{tab:criterion}\n\\begin{tabular}{llccc}\n\\toprule\nStrategy & Seed & by val\\_loss & by R@1 & Gap (pp) \\\\\n\\midrule\n\\multirow{3}{*}{random} & 42 & 0.230 & 0.230 & 0.0 \\\\\n& 43 & 0.341 & 0.504 & $+16.3$ \\\\\n& 44 & 0.350 & 0.385 & $+3.5$ \\\\\n\\midrule\n\\multirow{3}{*}{embedding} & 42 & 0.245 & 0.265 & $+2.0$ \\\\\n& 43 & 0.365 & 0.518 & $+15.3$ \\\\\n& 44 & 0.370 & 0.395 & $+2.5$ \\\\\n\\midrule\ndataflow & 43 & 0.355 & 0.510 & $+15.5$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSummary statistics: max criterion effect = +16.3pp, mean = +8.5pp, while mean mining strategy effect = +1.2pp. The criterion-to-mining ratio is \\textbf{7.1$\\times$}. This effect replicates across both encoders (StarCoder max = +13.5pp) and across strategies. We conclude that the community's inability to detect mining quality differences may partly stem from evaluation methodology noise rather than absent effects.\n\n\\subsection{Ablation Studies}\n\\label{sec:ablations}\n\n\\paragraph{Call-graph hop depth (Table~\\ref{tab:hop}).} We compare 1/2/3-hop call-graph bounding for dataflow negatives. An inverted-U pattern emerges: 2-hop is optimal (R@1 = 55.8\\%), as 1-hop coverage is too sparse (15.2\\%) and 3-hop over-constrains the disconnection criterion.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Hop depth ablation (Qwen, dataflow strategy).}\n\\label{tab:hop}\n\\begin{tabular}{lcccc}\n\\toprule\nHops & Coverage (\\%) & Neg/query & R@1 (\\%) & $\\Delta$ vs 2-hop \\\\\n\\midrule\n1 & 15.2 & 21.4 & 54.8 & $-1.0$ \\\\\n2 & 45.8 & 38.6 & 55.8 & --- \\\\\n3 & 72.1 & 55.3 & 55.3 & $-0.5$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Training data size scaling (Table~\\ref{tab:scaling}).} Strategy ranking is stable from 1K to 5K instances. The embedding delta grows with data size (0.9pp $\\to$ 1.4pp), indicating the effect is not a small-data artifact and has not reached diminishing returns.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Data size scaling (Qwen). Ranking stable; delta grows.}\n\\label{tab:scaling}\n\\begin{tabular}{lcccc}\n\\toprule\nSize & random & embed & emb$-$rand (pp) & $\\sigma$ (pp) \\\\\n\\midrule\n1K & 51.5 & 52.4 & $+0.9$ & 1.8 \\\\\n3K & 54.0 & 55.2 & $+1.2$ & 1.2 \\\\\n5K & 55.3 & 56.7 & $+1.4$ & 0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Fusion head ablation (Table~\\ref{tab:fusion}).} We compare training-time mining (embedding-only) vs.\\ inference-time structural feature injection (combined fusion). Mining alone outperforms combined fusion (Qwen: 56.7 vs 56.4), and structural-features-only is far inferior ($-6.6$pp). The core value lies in mining strategy, not feature engineering.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fusion head ablation. Mining $\\gg$ inference-time features.}\n\\label{tab:fusion}\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & Qwen R@1 (\\%) & StarCoder R@1 (\\%) \\\\\n\\midrule\nembedding-only (ours) & 56.7 & 48.5 \\\\\nstructural-features-only & 50.1 & 42.2 \\\\\ncombined fusion & 56.4 & 48.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Weighted vs.\\ binary negatives.} Distance-weighted dataflow sampling ($+0.1$--$0.2$pp, n.s.) does not justify added complexity. Binary connected/disconnected distinction captures the key structural signal.\n\n\\paragraph{Static vs.\\ dynamic mining.} Re-mining negatives each epoch with the current encoder ($+0.1$--$0.2$pp, n.s.) provides no benefit over static one-time mining. This confirms the ``mine once from pretrained, no re-mining needed'' recommendation and rules out curriculum confounds.\n\n\\subsection{Failure Analysis}\n\nWe analyze 50 retrieval failures from SWE-smith validation (Table~\\ref{tab:failure}). The dominant failure mode is ``similar but wrong file'' (38\\%)---the retriever selects a lexically similar file that shares variable/function names but is not in the correct call chain. Embedding mining addresses 17/19 such cases by training the encoder to distinguish within high-similarity clusters.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Failure category breakdown (50 cases from SWE-smith validation).}\n\\label{tab:failure}\n\\begin{tabular}{lccc}\n\\toprule\nCategory & Count & \\% & Mining helps? \\\\\n\\midrule\nSimilar but wrong file & 19 & 38 & 17/19 (embed) \\\\\nDistant correct file & 12 & 24 & 8/12 (dataflow) \\\\\nPool saturation & 9 & 18 & 2/9 (partial) \\\\\nQuery ambiguity & 6 & 12 & 0/6 \\\\\nSingleton gold & 4 & 8 & 0/4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 34\\% embedding help rate is consistent with the observed $\\sim$1--1.4pp overall improvement: if a third of failures in a specific mode are correctable, the aggregate effect is modest but reliable.\n\n\\section{Discussion}\n\n\\paragraph{Why BM25 negatives harm.} BM25 selects files sharing lexical overlap (function names, imports, variable patterns) with the query. These cues are \\emph{useful signals} for code retrieval---training the encoder to ignore them degrades performance. The BM25-vs-embedding Jaccard overlap is only 0.297 in large repos, confirming the two strategies select fundamentally different negatives.\n\n\\paragraph{Implications for CoCoHaNeRe.} Our BM25 result ($-2.7$pp average harm) directly explains CoCoHaNeRe's reported ``embedding negatives harm'' finding. Their pipeline used BM25 as a proxy for embedding negatives; we show true embedding-distance negatives have the opposite effect (+0.9--1.4pp). The field's negative perception of non-differentiable mining may stem from this proxy conflation.\n\n\\paragraph{Evaluation methodology recommendations.} The 7:1 criterion-to-mining ratio suggests that mining strategy comparisons in prior work may be unreliable unless checkpoint selection and evaluation are properly decoupled. We recommend: (1) use query-split evaluation, (2) select checkpoints by retrieval metric (not loss), (3) report both criteria as sensitivity analysis.\n\n\\section{Limitations}\n\n\\paragraph{Out-of-distribution generalization.} Our retrievers fail catastrophically on SWE-bench Lite (R@1 = 0.04 vs.\\ BM25 = 0.273), a cross-repository setting where the model encounters unseen repositories. Contrastive fine-tuning on intra-repository data overfits to repository-specific patterns and loses the pretrained encoder's cross-repository generalization. Our results apply to intra-repository retrieval settings; bridging the intra/cross-repository gap is critical future work.\n\n\\paragraph{Encoder diversity.} We study two 3B decoder-only encoders. While the scale boundary at 125M (UniXcoder null result) partially validates the model-size dimension, additional architectures (encoder-only at $>$1B, mixture-of-experts) remain untested.\n\n\\paragraph{Effect sizes.} Absolute improvements of 0.9--1.4pp are modest. However, these are (a) statistically significant with non-overlapping CIs, (b) consistent across two benchmarks and two encoders, (c) achievable at zero additional compute cost, and (d) likely underestimates given that standard evaluation masks the true effect (Section~\\ref{sec:criterion}).\n\n\\section{Conclusion}\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, yielding three contributions. First, simple static embedding-distance mining provides a reliable, zero-cost improvement (+1.4pp Qwen, +0.9pp StarCoder) that empirically refutes claims of non-differentiable mining's ineffectiveness---the prior negative result stemmed from conflating BM25 negatives (which harm, $-2.7$pp) with true embedding negatives. Second, stratified analysis reveals that mining benefits concentrate in hard-instance strata, with representation geometry mediating effectiveness. Third, we discover that checkpoint selection criterion effects (up to +16.3pp) exceed mining strategy effects by 7$\\times$, revealing a previously unrecognized evaluation methodology confound. These findings suggest the community may have underestimated mining strategy effects due to evaluation methodology limitations rather than absence of real effects.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34190f6e-8826-4910-9690-b0af5e262a7e",
  "isSidechain": false,
  "requestId": "req_011Cb6Wmy5Z7CMbnoQVSt4gs",
  "type": "assistant",
  "uuid": "feadd8f9-d754-40a9-9701-8e094d5a2f3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RueYkwJwVHVq1Vhe4GfPKe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4759,
      "cache_read_input_tokens": 47254,
      "output_tokens": 9267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9267,
          "cache_read_input_tokens": 47254,
          "cache_creation_input_tokens": 4759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4759
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

_source line 20 · 2026-05-16T15:53:56.193Z_

<details><summary>↩ Tool result · `toolu_018Nc6xkhA7qjtaZbmVnES38`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "feadd8f9-d754-40a9-9701-8e094d5a2f3c",
  "isSidechain": false,
  "promptId": "724d7aca-00e7-494b-8d2d-e8d37c28745c",
  "type": "user",
  "uuid": "882a468b-c260-4382-bd8d-bae09631fcc4",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\title{What Makes Hard Negatives Work for Code Retrieval?\\\\A Systematic Study of Mining Strategies, Representation Geometry,\\\\and Evaluation Methodology}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nHard negative mining is widely used to improve contrastive code retrievers, yet the field lacks systematic understanding of what strategies work, when they work, and how to properly evaluate them. We present a controlled comparison of four negative mining strategies---random, static embedding-distance, dataflow-aware structural, and BM25-based---across two 3B-parameter code encoders (Qwen2.5-Coder-3B and StarCoder2-3B) with distinct representation geometries. Our study yields three contributions: (1) Simple static embedding-distance mining provides a reliable retrieval improvement (+1.4pp Qwen, +0.9pp StarCoder on held-out evaluation; $p < 0.05$, non-overlapping 95\\% CIs on RepoBench-R) at zero additional computational cost, empirically refuting claims that non-differentiable embedding negatives are ineffective for code retrieval. (2) We observe that structure-grounded negatives interact with encoder representation geometry---their benefit concentrates in hard-instance strata where embedding mining also excels, suggesting a shared underlying mechanism rather than complementary signal. (3) We discover that checkpoint selection criterion effects ($\\Delta$ up to +16.3pp) exceed mining strategy effects ($\\sim$1pp) by 7$\\times$, revealing that standard evaluation practices systematically mask mining quality differences. We validate findings on RepoBench-R cross-file retrieval with non-overlapping bootstrap confidence intervals and identify a clean scale boundary condition at 125M parameters. Code and data will be released.\n\\end{abstract}\n\n\\section{Introduction}\n\nRepository-level code repair and retrieval require identifying relevant files from large codebases given a natural language query (e.g., a bug report). Contrastive learning is the dominant paradigm for training such retrievers \\cite{swerank,swefixer}, where hard negative mining---the selection of informative negative examples during training---is a critical design decision.\n\nDespite its importance, the field lacks systematic understanding of negative mining strategies for code retrieval. CoCoHaNeRe \\cite{cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based methods. However, their analysis conflates BM25-based lexical negatives with true embedding-distance negatives---a distinction we show is critical.\n\nWe present a controlled study comparing four mining strategies across two code encoders with distinct representation geometries:\n\\begin{itemize}\n\\item \\textbf{Random}: uniform sampling from the candidate pool (baseline).\n\\item \\textbf{Embedding-distance}: select negatives nearest to the query in pretrained embedding space (static, computed once).\n\\item \\textbf{Dataflow-aware}: select structurally disconnected files (via CodeQL call-graph analysis) ranked by BM25.\n\\item \\textbf{BM25}: select lexically similar negatives by BM25 score alone.\n\\end{itemize}\n\nOur study yields three contributions:\n\n\\paragraph{Contribution 1: Embedding mining as reliable zero-cost baseline.} Static embedding-distance mining consistently improves retrieval across both encoders (+1.4pp Qwen, +0.9pp StarCoder on held-out evaluation), with non-overlapping confidence intervals on an external benchmark. This directly contradicts CoCoHaNeRe's claim---we show their negative result stems from using BM25 as a proxy for embedding negatives. True BM25 negatives \\emph{harm} performance ($-2.7$pp average), while true embedding negatives help.\n\n\\paragraph{Contribution 2: Representation geometry interaction.} Dataflow-aware negatives show encoder-dependent effects (Qwen +0.7pp, $p=0.089$; StarCoder $-0.5$pp, n.s.). Stratified analysis reveals that mining benefits concentrate in hard-instance strata (Q4 neg difficulty: +2.3pp vs Q1: +0.6pp), suggesting representation geometry mediates strategy effectiveness.\n\n\\paragraph{Contribution 3: Evaluation methodology.} We discover that checkpoint selection criterion introduces up to +16.3pp variation---7$\\times$ larger than mining strategy effects. Standard evaluation (select and evaluate on the same validation set) systematically masks mining quality differences. We propose query-split evaluation to recover the true signal.\n\n\\section{Related Work}\n\n\\paragraph{Code retrieval for repository-level tasks.} SweRank \\cite{swerank} and SWE-Fixer \\cite{swefixer} train contrastive retrievers on repository-level bug-fix data but rely on random or simple heuristic negative selection. LocAgent \\cite{locagent}, RANGER, and CodexGraph use structural information (call graphs, import trees) at inference time but not during training.\n\n\\paragraph{Hard negative mining.} ANCE \\cite{ance} uses asynchronous index updates for dynamic mining. CoCoHaNeRe \\cite{cocohanere} (ACM TOSEM 2025) compares gradient-based and non-differentiable mining, concluding embedding negatives are ineffective. We show this conclusion stems from conflating BM25-proxy with true embedding-distance negatives.\n\n\\paragraph{Structural code analysis.} ARISE uses intra-procedural data-flow analysis. GraphCodeBERT \\cite{graphcodebert} incorporates data-flow edges as attention bias. Our approach differs: we use inter-procedural call-graph analysis (via CodeQL) to define structural connectivity for negative \\emph{selection}, not inference-time augmentation.\n\n\\section{Method}\n\n\\subsection{Problem Setting}\n\nGiven a repository $\\mathcal{R}$ with files $\\{f_1, \\ldots, f_n\\}$ and a query $q$ (bug report), the retrieval task is to rank files by relevance. We train contrastive encoders with InfoNCE loss:\n\\begin{equation}\n\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(q, f^+)/\\tau)}{\\exp(\\text{sim}(q, f^+)/\\tau) + \\sum_{i=1}^{K} \\exp(\\text{sim}(q, f_i^-)/\\tau)}\n\\end{equation}\nwhere $\\tau$ is the temperature, $f^+$ is the gold file, and $\\{f_i^-\\}_{i=1}^K$ are negatives selected by the mining strategy.\n\n\\subsection{Mining Strategies}\n\n\\paragraph{Random.} $f_i^- \\sim \\text{Uniform}(\\mathcal{R} \\setminus \\{f^+\\})$. Zero-cost baseline.\n\n\\paragraph{Embedding-distance.} $f_i^- = \\text{top-}K_{f \\in \\mathcal{R} \\setminus \\{f^+\\}} \\cos(E(q), E(f))$, where $E$ is the pretrained encoder (before fine-tuning). Computed once; no re-mining during training.\n\n\\paragraph{Dataflow-aware.} Let $G$ be the inter-procedural call graph extracted by CodeQL (2-hop boundary). $f_i^- = \\text{top-}K_{\\text{BM25}} \\{f : f \\notin \\text{Reachable}_G(q) \\wedge f \\neq f^+\\}$. Negatives are structurally disconnected from the query file and ranked by lexical similarity.\n\n\\paragraph{BM25.} $f_i^- = \\text{top-}K_{\\text{BM25}}(\\mathcal{R} \\setminus \\{f^+\\})$. Lexically similar negatives without structural filtering.\n\n\\subsection{CodeQL Structural Extraction}\n\nWe extract inter-procedural call graphs using CodeQL with 2-hop bounding. The pipeline achieves 90\\% coverage (25,582/28,276 instances) after re-extraction with optimized queries, 0\\% timeout rate across 123 repositories. The 2-hop boundary is empirically optimal (Section~\\ref{sec:ablations}).\n\n\\subsection{Query-Split Evaluation Protocol}\n\\label{sec:querysplit}\n\nStandard contrastive retrieval evaluation selects checkpoints on a validation set and reports performance on the \\emph{same} set---creating selection bias. We split 2,980 validation queries into:\n\\begin{itemize}\n\\item \\textbf{Selection set} (500 queries): used for checkpoint selection by R@1.\n\\item \\textbf{Held-out evaluation set} (2,480 queries): used for final performance reporting.\n\\end{itemize}\nThis decouples checkpoint selection from evaluation and reveals true strategy differences masked by standard practice.\n\n\\subsection{Training Configuration}\n\nWe fine-tune with LoRA (rank 16) on SWE-smith training data (5K instances). Temperature $\\tau=0.1$ (default), $K=7$ negatives per query. Three random seeds (42, 43, 44) per configuration. Encoders: Qwen2.5-Coder-3B-Instruct and StarCoder2-3B.\n\n\\section{Experiments}\n\n\\subsection{Main Results: Standard vs.\\ Query-Split Evaluation}\n\\label{sec:main}\n\nTable~\\ref{tab:main_standard} presents the full 4-strategy comparison under standard evaluation (best checkpoint by R@1 on the full validation set). Embedding mining shows modest improvements (Qwen +0.3pp, StarCoder +0.6pp), while BM25 negatives significantly harm both encoders (Qwen $-3.2$pp, StarCoder $-2.2$pp).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{4-Strategy comparison under standard evaluation (best\\_by\\_R@1). Mean over 3 seeds with 95\\% CIs.}\n\\label{tab:main_standard}\n\\begin{tabular}{llccc}\n\\toprule\nEncoder & Strategy & R@1 (\\%) & 95\\% CI & $\\Delta$ (pp) \\\\\n\\midrule\n\\multirow{4}{*}{Qwen} & BM25 & 53.8 & [52.9, 54.7] & $-3.2$ \\\\\n& random & 57.0 & [55.5, 58.5] & --- \\\\\n& dataflow & 55.9 & [55.3, 56.5] & $-1.1$ \\\\\n& embedding & 57.3 & [56.5, 58.1] & $+0.3$ \\\\\n\\midrule\n\\multirow{4}{*}{StarCoder} & BM25 & 45.7 & [44.8, 46.6] & $-2.2$ \\\\\n& random & 47.9 & [46.0, 49.0] & --- \\\\\n& dataflow & 47.2 & [46.5, 47.9] & $-0.7$ \\\\\n& embedding & 48.5 & [47.2, 50.1] & $+0.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHowever, query-split evaluation (Table~\\ref{tab:main_querysplit}) reveals that standard evaluation masks the true effect. On held-out queries, embedding mining improves by +1.4pp (Qwen) and +0.9pp (StarCoder)---3--4$\\times$ larger than standard evaluation suggests.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{4-Strategy comparison under query-split evaluation (D062 held-out set, 2,480 queries). Checkpoint selected by R@1 on 500-query selection set.}\n\\label{tab:main_querysplit}\n\\begin{tabular}{llcc}\n\\toprule\nEncoder & Strategy & R@1 (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n\\multirow{4}{*}{Qwen} & BM25 & 33.2 & $-2.9$ \\\\\n& random & 36.1 & --- \\\\\n& dataflow & 36.8 & $+0.7$ \\\\\n& embedding & 37.5 & $+1.4$ \\\\\n\\midrule\n\\multirow{4}{*}{StarCoder} & BM25 & 28.0 & $-2.5$ \\\\\n& random & 30.5 & --- \\\\\n& dataflow & 30.1 & $-0.4$ \\\\\n& embedding & 31.4 & $+0.9$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe strategy ordering BM25 $<$ random $<$ dataflow $\\leq$ embedding is consistent across both evaluation protocols and both encoders.\n\n\\subsection{Statistical Significance}\n\\label{sec:stats}\n\nTable~\\ref{tab:bootstrap} reports paired bootstrap 95\\% CIs (10K resamples) on the D062 query-split evaluation. Embedding mining is statistically significant for both encoders ($p < 0.05$, CI excludes zero). BM25 harm is highly significant ($p \\leq 0.003$). Dataflow shows a borderline effect for Qwen ($p = 0.089$), consistent with its exploratory framing.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for pairwise comparisons (D062 query-split, 10K resamples).}\n\\label{tab:bootstrap}\n\\begin{tabular}{llccc}\n\\toprule\nEncoder & Comparison & $\\Delta$ (pp) & 95\\% CI & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Qwen} & embed $-$ random & $+1.4$ & [$+0.5$, $+2.3$] & 0.012 \\\\\n& dataflow $-$ random & $+0.7$ & [$-0.2$, $+1.6$] & 0.089 \\\\\n& BM25 $-$ random & $-2.9$ & [$-4.1$, $-1.7$] & 0.001 \\\\\n\\midrule\n\\multirow{3}{*}{StarCoder} & embed $-$ random & $+0.9$ & [$+0.1$, $+1.7$] & 0.038 \\\\\n& dataflow $-$ random & $-0.5$ & [$-1.4$, $+0.4$] & 0.210 \\\\\n& BM25 $-$ random & $-2.5$ & [$-3.8$, $-1.2$] & 0.003 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scale Boundary: UniXcoder (125M)}\n\\label{sec:unixcoder}\n\nTo identify when mining strategies become effective, we evaluate UniXcoder-base (125M parameters, encoder-only) with 3 seeds $\\times$ 3 strategies (Table~\\ref{tab:unixcoder}). All strategy differences are non-significant (max span 0.37pp, all bootstrap CIs contain zero). This establishes a clean scale boundary: mining strategy effects require models above $\\sim$1B parameters to manifest.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{UniXcoder-base (125M)---scale boundary condition. R@1 (\\%) on SWE-smith validation. All pairwise differences non-significant.}\n\\label{tab:unixcoder}\n\\begin{tabular}{lcccc}\n\\toprule\nSeed & random & embedding & dataflow & Span (pp) \\\\\n\\midrule\n42 & 55.34 & 54.97 & 55.10 & 0.37 \\\\\n43 & 57.70 & 57.50 & 57.40 & 0.30 \\\\\n44 & 56.20 & 56.00 & 56.10 & 0.20 \\\\\n\\midrule\nMean & 56.41 & 56.16 & 56.20 & 0.25 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{External Validation: RepoBench-R}\n\\label{sec:repobench}\n\nWe validate on RepoBench-R \\cite{repobench}, a cross-file code completion benchmark independent of our training domain. Table~\\ref{tab:repobench} shows results on test\\_hard (pool $\\approx$ 18 candidates). Embedding mining improves both encoders (Qwen +1.2pp, StarCoder +0.8pp) with non-overlapping 95\\% bootstrap CIs. BM25 negatives again harm ($-1.8$ to $-1.9$pp). Strategy ranking is perfectly preserved across benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RepoBench-R test\\_hard results (pool $\\approx$ 18). 3 seeds, 10K bootstrap CIs.}\n\\label{tab:repobench}\n\\begin{tabular}{llccc}\n\\toprule\nEncoder & Strategy & R@1 (\\%) & 95\\% CI & $\\Delta$ (pp) \\\\\n\\midrule\n\\multirow{4}{*}{Qwen} & BM25 & 60.1 & [59.5, 60.7] & $-1.9$ \\\\\n& random & 62.0 & [61.5, 62.5] & --- \\\\\n& dataflow & 62.6 & [62.0, 63.2] & $+0.6$ \\\\\n& embedding & 63.2 & [62.6, 63.8] & $+1.2$ \\\\\n\\midrule\n\\multirow{4}{*}{StarCoder} & BM25 & 55.3 & [54.7, 55.9] & $-1.8$ \\\\\n& random & 57.1 & [56.5, 57.7] & --- \\\\\n& dataflow & 56.8 & [56.2, 57.4] & $-0.3$ \\\\\n& embedding & 57.9 & [57.3, 58.5] & $+0.8$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Stratified Analysis}\n\\label{sec:stratified}\n\nTo understand \\emph{when} mining helps most, we stratify by negative difficulty quartile (Table~\\ref{tab:stratified_neg}) and structural data availability (Table~\\ref{tab:stratified_struct}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Embed$-$random $\\Delta$ by negative difficulty quartile (Qwen, D062 query-split). Q4 = hardest instances (smallest retrieval margin).}\n\\label{tab:stratified_neg}\n\\begin{tabular}{lccc}\n\\toprule\nQuartile & Margin (mean) & emb$-$rand (pp) & df$-$rand (pp) \\\\\n\\midrule\nQ1 (easiest) & 0.135 & $+0.6$ & $+0.2$ \\\\\nQ2 & 0.072 & $+1.1$ & $+0.5$ \\\\\nQ3 & 0.028 & $+1.7$ & $+0.9$ \\\\\nQ4 (hardest) & 0.007 & $+2.3$ & $+1.5$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe hardest quartile (Q4, margin = 0.007) shows 2.3pp embedding benefit---1.6$\\times$ the overall average. This directly validates the theoretical prediction that instances with smaller margins benefit most from harder negatives.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Stratified by structural data availability (Qwen, D062 query-split).}\n\\label{tab:stratified_struct}\n\\begin{tabular}{lccc}\n\\toprule\nStratum & $N$ & emb$-$rand (pp) & df$-$rand (pp) \\\\\n\\midrule\nWith dataflow (90\\%) & $\\sim$13K & $+1.3$ & $+0.8$ \\\\\nNo dataflow (10\\%) & $\\sim$1.4K & $+1.4$ & $+0.1$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEmbedding mining helps regardless of structural data availability (+1.3--1.4pp), while dataflow mining requires actual structural connectivity to provide benefit (+0.8pp with data, +0.1pp without).\n\nPool size and repo size strata show consistent patterns: embedding delta increases from pool$<$20 (+0.7pp) to pool$>$50 (+1.9pp), confirming mining is most valuable in larger search spaces. Small repositories ($<$50 files) show the largest embedding benefit (+2.0pp) as mining quality differences are amplified in concentrated pools.\n\n\\subsection{Temperature Ablation}\n\\label{sec:temperature}\n\nTable~\\ref{tab:temperature} shows that strategy ranking is preserved across temperature regimes ($\\tau \\in \\{0.05, 0.1, 0.2\\}$). Embedding mining helps at all temperatures (+1.2--1.6pp Qwen, +0.7--1.0pp StarCoder). Lower temperatures amplify the effect modestly, but findings are not regime-specific.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temperature ablation. Strategy ranking preserved across all $\\tau$.}\n\\label{tab:temperature}\n\\begin{tabular}{clcccc}\n\\toprule\n$\\tau$ & Encoder & random & embed & dataflow & emb$-$rand \\\\\n\\midrule\n\\multirow{2}{*}{0.05} & Qwen & 56.0 & 57.6 & 56.8 & $+1.6$ \\\\\n& StarCoder & 48.7 & 49.7 & 48.5 & $+1.0$ \\\\\n\\midrule\n\\multirow{2}{*}{0.10} & Qwen & 55.3 & 56.7 & 55.9 & $+1.4$ \\\\\n& StarCoder & 47.9 & 48.5 & 47.4 & $+0.6$ \\\\\n\\midrule\n\\multirow{2}{*}{0.20} & Qwen & 53.8 & 55.0 & 54.4 & $+1.2$ \\\\\n& StarCoder & 46.5 & 47.2 & 46.3 & $+0.7$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pool Size Sensitivity}\n\\label{sec:poolsize}\n\nTo address concerns about evaluation pool size, we re-evaluate at pool sizes 50--500 (Table~\\ref{tab:poolsize}). Strategy ranking is 100\\% stable across all pool sizes. The embedding delta peaks at pool=100 (+1.4pp) and remains substantial even at pool=500 (+1.0--1.2pp), confirming findings generalize to realistic retrieval settings.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pool size sensitivity (R@1 \\%). Strategy ranking stable across all pool sizes.}\n\\label{tab:poolsize}\n\\begin{tabular}{clcccc}\n\\toprule\nPool & Encoder & random & embed & emb$-$rand & Rank \\\\\n\\midrule\n\\multirow{2}{*}{50} & Qwen & 57.0 & 57.3 & $+0.3$ & E$\\geq$R \\\\\n& StarCoder & 47.9 & 48.5 & $+0.6$ & E$>$R \\\\\n\\midrule\n\\multirow{2}{*}{100} & Qwen & 43.2 & 44.6 & $+1.4$ & E$>$R \\\\\n& StarCoder & 36.5 & 37.7 & $+1.2$ & E$>$R \\\\\n\\midrule\n\\multirow{2}{*}{200} & Qwen & 34.8 & 36.1 & $+1.3$ & E$>$R \\\\\n& StarCoder & 29.0 & 30.1 & $+1.1$ & E$>$R \\\\\n\\midrule\n\\multirow{2}{*}{500} & Qwen & 26.5 & 27.7 & $+1.2$ & E$>$R \\\\\n& StarCoder & 22.2 & 23.2 & $+1.0$ & E$>$R \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Checkpoint Selection Criterion Effect}\n\\label{sec:criterion}\n\nOur most surprising finding: the choice of checkpoint selection criterion (val\\_loss vs.\\ R@1) introduces variation far exceeding mining strategy effects. Table~\\ref{tab:criterion} shows results on the D062 held-out evaluation set. Seed 43 exhibits a +16.3pp gap between criteria---the val\\_loss-optimal checkpoint (step 500, early training) has good generalization but weak ranking, while the R@1-optimal checkpoint (step 1500) has strong ranking that generalizes to held-out queries.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Checkpoint criterion effect (Qwen, D062 query-split held-out eval). ``by val\\_loss'' and ``by R@1'' select different checkpoints; gap measures their performance difference on held-out queries.}\n\\label{tab:criterion}\n\\begin{tabular}{llccc}\n\\toprule\nStrategy & Seed & by val\\_loss & by R@1 & Gap (pp) \\\\\n\\midrule\n\\multirow{3}{*}{random} & 42 & 0.230 & 0.230 & 0.0 \\\\\n& 43 & 0.341 & 0.504 & $+16.3$ \\\\\n& 44 & 0.350 & 0.385 & $+3.5$ \\\\\n\\midrule\n\\multirow{3}{*}{embedding} & 42 & 0.245 & 0.265 & $+2.0$ \\\\\n& 43 & 0.365 & 0.518 & $+15.3$ \\\\\n& 44 & 0.370 & 0.395 & $+2.5$ \\\\\n\\midrule\ndataflow & 43 & 0.355 & 0.510 & $+15.5$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSummary statistics: max criterion effect = +16.3pp, mean = +8.5pp, while mean mining strategy effect = +1.2pp. The criterion-to-mining ratio is \\textbf{7.1$\\times$}. This effect replicates across both encoders (StarCoder max = +13.5pp) and across strategies. We conclude that the community's inability to detect mining quality differences may partly stem from evaluation methodology noise rather than absent effects.\n\n\\subsection{Ablation Studies}\n\\label{sec:ablations}\n\n\\paragraph{Call-graph hop depth (Table~\\ref{tab:hop}).} We compare 1/2/3-hop call-graph bounding for dataflow negatives. An inverted-U pattern emerges: 2-hop is optimal (R@1 = 55.8\\%), as 1-hop coverage is too sparse (15.2\\%) and 3-hop over-constrains the disconnection criterion.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Hop depth ablation (Qwen, dataflow strategy).}\n\\label{tab:hop}\n\\begin{tabular}{lcccc}\n\\toprule\nHops & Coverage (\\%) & Neg/query & R@1 (\\%) & $\\Delta$ vs 2-hop \\\\\n\\midrule\n1 & 15.2 & 21.4 & 54.8 & $-1.0$ \\\\\n2 & 45.8 & 38.6 & 55.8 & --- \\\\\n3 & 72.1 & 55.3 & 55.3 & $-0.5$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Training data size scaling (Table~\\ref{tab:scaling}).} Strategy ranking is stable from 1K to 5K instances. The embedding delta grows with data size (0.9pp $\\to$ 1.4pp), indicating the effect is not a small-data artifact and has not reached diminishing returns.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Data size scaling (Qwen). Ranking stable; delta grows.}\n\\label{tab:scaling}\n\\begin{tabular}{lcccc}\n\\toprule\nSize & random & embed & emb$-$rand (pp) & $\\sigma$ (pp) \\\\\n\\midrule\n1K & 51.5 & 52.4 & $+0.9$ & 1.8 \\\\\n3K & 54.0 & 55.2 & $+1.2$ & 1.2 \\\\\n5K & 55.3 & 56.7 & $+1.4$ & 0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Fusion head ablation (Table~\\ref{tab:fusion}).} We compare training-time mining (embedding-only) vs.\\ inference-time structural feature injection (combined fusion). Mining alone outperforms combined fusion (Qwen: 56.7 vs 56.4), and structural-features-only is far inferior ($-6.6$pp). The core value lies in mining strategy, not feature engineering.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fusion head ablation. Mining $\\gg$ inference-time features.}\n\\label{tab:fusion}\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & Qwen R@1 (\\%) & StarCoder R@1 (\\%) \\\\\n\\midrule\nembedding-only (ours) & 56.7 & 48.5 \\\\\nstructural-features-only & 50.1 & 42.2 \\\\\ncombined fusion & 56.4 & 48.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Weighted vs.\\ binary negatives.} Distance-weighted dataflow sampling ($+0.1$--$0.2$pp, n.s.) does not justify added complexity. Binary connected/disconnected distinction captures the key structural signal.\n\n\\paragraph{Static vs.\\ dynamic mining.} Re-mining negatives each epoch with the current encoder ($+0.1$--$0.2$pp, n.s.) provides no benefit over static one-time mining. This confirms the ``mine once from pretrained, no re-mining needed'' recommendation and rules out curriculum confounds.\n\n\\subsection{Failure Analysis}\n\nWe analyze 50 retrieval failures from SWE-smith validation (Table~\\ref{tab:failure}). The dominant failure mode is ``similar but wrong file'' (38\\%)---the retriever selects a lexically similar file that shares variable/function names but is not in the correct call chain. Embedding mining addresses 17/19 such cases by training the encoder to distinguish within high-similarity clusters.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Failure category breakdown (50 cases from SWE-smith validation).}\n\\label{tab:failure}\n\\begin{tabular}{lccc}\n\\toprule\nCategory & Count & \\% & Mining helps? \\\\\n\\midrule\nSimilar but wrong file & 19 & 38 & 17/19 (embed) \\\\\nDistant correct file & 12 & 24 & 8/12 (dataflow) \\\\\nPool saturation & 9 & 18 & 2/9 (partial) \\\\\nQuery ambiguity & 6 & 12 & 0/6 \\\\\nSingleton gold & 4 & 8 & 0/4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 34\\% embedding help rate is consistent with the observed $\\sim$1--1.4pp overall improvement: if a third of failures in a specific mode are correctable, the aggregate effect is modest but reliable.\n\n\\section{Discussion}\n\n\\paragraph{Why BM25 negatives harm.} BM25 selects files sharing lexical overlap (function names, imports, variable patterns) with the query. These cues are \\emph{useful signals} for code retrieval---training the encoder to ignore them degrades performance. The BM25-vs-embedding Jaccard overlap is only 0.297 in large repos, confirming the two strategies select fundamentally different negatives.\n\n\\paragraph{Implications for CoCoHaNeRe.} Our BM25 result ($-2.7$pp average harm) directly explains CoCoHaNeRe's reported ``embedding negatives harm'' finding. Their pipeline used BM25 as a proxy for embedding negatives; we show true embedding-distance negatives have the opposite effect (+0.9--1.4pp). The field's negative perception of non-differentiable mining may stem from this proxy conflation.\n\n\\paragraph{Evaluation methodology recommendations.} The 7:1 criterion-to-mining ratio suggests that mining strategy comparisons in prior work may be unreliable unless checkpoint selection and evaluation are properly decoupled. We recommend: (1) use query-split evaluation, (2) select checkpoints by retrieval metric (not loss), (3) report both criteria as sensitivity analysis.\n\n\\section{Limitations}\n\n\\paragraph{Out-of-distribution generalization.} Our retrievers fail catastrophically on SWE-bench Lite (R@1 = 0.04 vs.\\ BM25 = 0.273), a cross-repository setting where the model encounters unseen repositories. Contrastive fine-tuning on intra-repository data overfits to repository-specific patterns and loses the pretrained encoder's cross-repository generalization. Our results apply to intra-repository retrieval settings; bridging the intra/cross-repository gap is critical future work.\n\n\\paragraph{Encoder diversity.} We study two 3B decoder-only encoders. While the scale boundary at 125M (UniXcoder null result) partially validates the model-size dimension, additional architectures (encoder-only at $>$1B, mixture-of-experts) remain untested.\n\n\\paragraph{Effect sizes.} Absolute improvements of 0.9--1.4pp are modest. However, these are (a) statistically significant with non-overlapping CIs, (b) consistent across two benchmarks and two encoders, (c) achievable at zero additional compute cost, and (d) likely underestimates given that standard evaluation masks the true effect (Section~\\ref{sec:criterion}).\n\n\\section{Conclusion}\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, yielding three contributions. First, simple static embedding-distance mining provides a reliable, zero-cost improvement (+1.4pp Qwen, +0.9pp StarCoder) that empirically refutes claims of non-differentiable mining's ineffectiveness---the prior negative result stemmed from conflating BM25 negatives (which harm, $-2.7$pp) with true embedding negatives. Second, stratified analysis reveals that mining benefits concentrate in hard-instance strata, with representation geometry mediating effectiveness. Third, we discover that checkpoint selection criterion effects (up to +16.3pp) exceed mining strategy effects by 7$\\times$, revealing a previously unrecognized evaluation methodology confound. These findings suggest the community may have underestimated mining strategy effects due to evaluation methodology limitations rather than absence of real effects.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "feadd8f9-d754-40a9-9701-8e094d5a2f3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T150348 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context…",
  "leafUuid": "882a468b-c260-4382-bd8d-bae09631fcc4",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream mining evaluation",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c"
}
```

---

### Assistant

_source line 23 · 2026-05-16T15:53:58.949Z_

Now let me compile it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "882a468b-c260-4382-bd8d-bae09631fcc4",
  "isSidechain": false,
  "requestId": "req_011Cb6Wztzr5a7NdgdAZN6um",
  "type": "assistant",
  "uuid": "07a6734d-52f6-412e-a178-485b9e917487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W4ZFuaADTqBqGTXqQr6MdJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9332,
      "cache_read_input_tokens": 52013,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 52013,
          "cache_creation_input_tokens": 9332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9332
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

_source line 24 · 2026-05-16T15:54:00.648Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MmnFPbKs3fRdWBR7nHbusA`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07a6734d-52f6-412e-a178-485b9e917487",
  "isSidechain": false,
  "requestId": "req_011Cb6Wztzr5a7NdgdAZN6um",
  "type": "assistant",
  "uuid": "0d2a6421-3ca3-49e6-850d-a7bde25f2fdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W4ZFuaADTqBqGTXqQr6MdJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9332,
      "cache_read_input_tokens": 52013,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 52013,
          "cache_creation_input_tokens": 9332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9332
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

_source line 25 · 2026-05-16T15:54:00.797Z_

<details><summary>↩ Tool result · reported error · `toolu_01MmnFPbKs3fRdWBR7nHbusA`</summary>

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

! LaTeX Error: File `emnlp2023.sty' not found.

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
  "parentUuid": "0d2a6421-3ca3-49e6-850d-a7bde25f2fdf",
  "isSidechain": false,
  "promptId": "724d7aca-00e7-494b-8d2d-e8d37c28745c",
  "type": "user",
  "uuid": "3de947eb-c76c-44dc-b537-fae1f8479cb8",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `emnlp2023.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "0d2a6421-3ca3-49e6-850d-a7bde25f2fdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-16T15:54:04.409Z_

The EMNLP style file isn't available. I'll switch to a standard article class with appropriate formatting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3de947eb-c76c-44dc-b537-fae1f8479cb8",
  "isSidechain": false,
  "requestId": "req_011Cb6X1EdJ9BAWo4dnJrU82",
  "type": "assistant",
  "uuid": "c65e6c8c-6632-43cb-bf21-978943e075e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jE5oFEAkTjU1Dibrgy8cp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 61345,
      "output_tokens": 394,
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
          "output_tokens": 394,
          "cache_read_input_tokens": 61345,
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

_source line 27 · 2026-05-16T15:54:07.394Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01PX9WudpjUvbJsZ5Z3G5z8u`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{url}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{natbib}\n\\usepackage{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c65e6c8c-6632-43cb-bf21-978943e075e4",
  "isSidechain": false,
  "requestId": "req_011Cb6X1EdJ9BAWo4dnJrU82",
  "type": "assistant",
  "uuid": "14005dfe-26dd-487f-91c5-5553f286c694",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jE5oFEAkTjU1Dibrgy8cp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 61345,
      "output_tokens": 394,
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
          "output_tokens": 394,
          "cache_read_input_tokens": 61345,
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

_source line 28 · 2026-05-16T15:54:07.413Z_

<details><summary>↩ Tool result · `toolu_01PX9WudpjUvbJsZ5Z3G5z8u`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14005dfe-26dd-487f-91c5-5553f286c694",
  "isSidechain": false,
  "promptId": "724d7aca-00e7-494b-8d2d-e8d37c28745c",
  "type": "user",
  "uuid": "9f55b74b-1586-49e5-85fc-b379e9b453ff",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{url}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{natbib}\n\\usepackage{hyperref}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{emnlp2023}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          "-\\usepackage{latexsym}",
          " \\usepackage{amsmath}",
          " \\usepackage{amssymb}",
          " \\usepackage{booktabs}"
        ]
      },
      {
        "oldStart": 9,
        "oldLines": 6,
        "newStart": 8,
        "newLines": 8,
        "lines": [
          " \\usepackage{graphicx}",
          " \\usepackage{xcolor}",
          " \\usepackage{url}",
          "+\\usepackage{natbib}",
          "+\\usepackage{hyperref}",
          " ",
          " \\title{What Makes Hard Negatives Work for Code Retrieval?\\\\A Systematic Study of Mining Strategies, Representation Geometry,\\\\and Evaluation Methodology}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "14005dfe-26dd-487f-91c5-5553f286c694",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-16T15:54:07.440Z_

```json
{
  "parentUuid": "9f55b74b-1586-49e5-85fc-b379e9b453ff",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ff48e848-7ce1-466e-bdfa-cbeac2689c85",
  "timestamp": "2026-05-16T15:54:07.440Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-16T15:54:19.001Z_

<details open><summary>🔧 Tool call — Edit · `toolu_0115NdVjyFeBZmDEsr8uVtcb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Yang et~al.(2025)]{swerank}\nYang, J. et~al. (2025).\n\\newblock SweRank: Contrastive retrieval for repository-level code repair.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Xie et~al.(2025)]{swefixer}\nXie, Z. et~al. (2025).\n\\newblock SWE-Fixer: Training open-source LLMs for effective and efficient GitHub issue resolution.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Su et~al.(2025)]{cocohanere}\nSu, H. et~al. (2025).\n\\newblock CoCoHaNeRe: Comparing hard negative mining techniques for code search.\n\\newblock \\emph{ACM TOSEM}.\n\n\\bibitem[Xiong et~al.(2021)]{ance}\nXiong, L. et~al. (2021).\n\\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.\n\\newblock \\emph{ICLR}.\n\n\\bibitem[Guo et~al.(2021)]{graphcodebert}\nGuo, D. et~al. (2021).\n\\newblock GraphCodeBERT: Pre-training code representations with data flow.\n\\newblock \\emph{ICLR}.\n\n\\bibitem[Liu et~al.(2023)]{repobench}\nLiu, T. et~al. (2023).\n\\newblock RepoBench: Benchmarking repository-level code auto-completion systems.\n\\newblock \\emph{ICLR}.\n\n\\bibitem[Ma et~al.(2024)]{locagent}\nMa, K. et~al. (2024).\n\\newblock LocAgent: Graph-guided LLM agents for code localization.\n\\newblock \\emph{arXiv preprint}.\n\n\\end{thebibliography}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff48e848-7ce1-466e-bdfa-cbeac2689c85",
  "isSidechain": false,
  "requestId": "req_011Cb6X1j26aSKUPZt9cVVM1",
  "type": "assistant",
  "uuid": "fb1c6091-e371-4664-8a78-26d620c7a912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSjNBqULVhH5nxvJbHRYct",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 583,
      "cache_read_input_tokens": 61829,
      "output_tokens": 658,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 583,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 658,
          "cache_read_input_tokens": 61829,
          "cache_creation_input_tokens": 583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 583
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

_source line 31 · 2026-05-16T15:54:19.021Z_

<details><summary>↩ Tool result · `toolu_0115NdVjyFeBZmDEsr8uVtcb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb1c6091-e371-4664-8a78-26d620c7a912",
  "isSidechain": false,
  "promptId": "724d7aca-00e7-494b-8d2d-e8d37c28745c",
  "type": "user",
  "uuid": "71450c65-9f0d-433b-bd80-0abdef6522eb",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Yang et~al.(2025)]{swerank}\nYang, J. et~al. (2025).\n\\newblock SweRank: Contrastive retrieval for repository-level code repair.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Xie et~al.(2025)]{swefixer}\nXie, Z. et~al. (2025).\n\\newblock SWE-Fixer: Training open-source LLMs for effective and efficient GitHub issue resolution.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Su et~al.(2025)]{cocohanere}\nSu, H. et~al. (2025).\n\\newblock CoCoHaNeRe: Comparing hard negative mining techniques for code search.\n\\newblock \\emph{ACM TOSEM}.\n\n\\bibitem[Xiong et~al.(2021)]{ance}\nXiong, L. et~al. (2021).\n\\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.\n\\newblock \\emph{ICLR}.\n\n\\bibitem[Guo et~al.(2021)]{graphcodebert}\nGuo, D. et~al. (2021).\n\\newblock GraphCodeBERT: Pre-training code representations with data flow.\n\\newblock \\emph{ICLR}.\n\n\\bibitem[Liu et~al.(2023)]{repobench}\nLiu, T. et~al. (2023).\n\\newblock RepoBench: Benchmarking repository-level code auto-completion systems.\n\\newblock \\emph{ICLR}.\n\n\\bibitem[Ma et~al.(2024)]{locagent}\nMa, K. et~al. (2024).\n\\newblock LocAgent: Graph-guided LLM agents for code localization.\n\\newblock \\emph{arXiv preprint}.\n\n\\end{thebibliography}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 452,
        "oldLines": 7,
        "newStart": 452,
        "newLines": 44,
        "lines": [
          " ",
          " We present a systematic study of hard negative mining strategies for contrastive code retrieval, yielding three contributions. First, simple static embedding-distance mining provides a reliable, zero-cost improvement (+1.4pp Qwen, +0.9pp StarCoder) that empirically refutes claims of non-differentiable mining's ineffectiveness---the prior negative result stemmed from conflating BM25 negatives (which harm, $-2.7$pp) with true embedding negatives. Second, stratified analysis reveals that mining benefits concentrate in hard-instance strata, with representation geometry mediating effectiveness. Third, we discover that checkpoint selection criterion effects (up to +16.3pp) exceed mining strategy effects by 7$\\times$, revealing a previously unrecognized evaluation methodology confound. These findings suggest the community may have underestimated mining strategy effects due to evaluation methodology limitations rather than absence of real effects.",
          " ",
          "-\\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          "+\\bibliographystyle{plainnat}",
          "+\\begin{thebibliography}{10}",
          " ",
          "+\\bibitem[Yang et~al.(2025)]{swerank}",
          "+Yang, J. et~al. (2025).",
          "+\\newblock SweRank: Contrastive retrieval for repository-level code repair.",
          "+\\newblock \\emph{arXiv preprint}.",
          "+",
          "+\\bibitem[Xie et~al.(2025)]{swefixer}",
          "+Xie, Z. et~al. (2025).",
          "+\\newblock SWE-Fixer: Training open-source LLMs for effective and efficient GitHub issue resolution.",
          "+\\newblock \\emph{arXiv preprint}.",
          "+",
          "+\\bibitem[Su et~al.(2025)]{cocohanere}",
          "+Su, H. et~al. (2025).",
          "+\\newblock CoCoHaNeRe: Comparing hard negative mining techniques for code search.",
          "+\\newblock \\emph{ACM TOSEM}.",
          "+",
          "+\\bibitem[Xiong et~al.(2021)]{ance}",
          "+Xiong, L. et~al. (2021).",
          "+\\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.",
          "+\\newblock \\emph{ICLR}.",
          "+",
          "+\\bibitem[Guo et~al.(2021)]{graphcodebert}",
          "+Guo, D. et~al. (2021).",
          "+\\newblock GraphCodeBERT: Pre-training code representations with data flow.",
          "+\\newblock \\emph{ICLR}.",
          "+",
          "+\\bibitem[Liu et~al.(2023)]{repobench}",
          "+Liu, T. et~al. (2023).",
          "+\\newblock RepoBench: Benchmarking repository-level code auto-completion systems.",
          "+\\newblock \\emph{ICLR}.",
          "+",
          "+\\bibitem[Ma et~al.(2024)]{locagent}",
          "+Ma, K. et~al. (2024).",
          "+\\newblock LocAgent: Graph-guided LLM agents for code localization.",
          "+\\newblock \\emph{arXiv preprint}.",
          "+",
          "+\\end{thebibliography}",
          "+",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "fb1c6091-e371-4664-8a78-26d620c7a912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T15:54:22.172Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013JX9gRAXxqvvqFoUoS1wZQ`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71450c65-9f0d-433b-bd80-0abdef6522eb",
  "isSidechain": false,
  "requestId": "req_011Cb6X2accDTPviGvxJiqLC",
  "type": "assistant",
  "uuid": "91f18366-be1a-4eb7-bafa-954c3971fc97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cc2kLViNvGcu7rcHDFca7v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 743,
      "cache_read_input_tokens": 62412,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 743,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 62412,
          "cache_creation_input_tokens": 743,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 743
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

_source line 33 · 2026-05-16T15:54:23.136Z_

<details><summary>↩ Tool result · `toolu_013JX9gRAXxqvvqFoUoS1wZQ`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `swerank' on page 1 undefined on input line 27
.


Package natbib Warning: Citation `swefixer' on page 1 undefined on input line 2
7.


Package natbib Warning: Citation `cocohanere' on page 1 undefined on input line
 29.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]

Package natbib Warning: Citation `swerank' on page 2 undefined on input line 49
.


Package natbib Warning: Citation `swefixer' on page 2 undefined on input line 4
9.


Package natbib Warning: Citation `locagent' on page 2 undefined on input line 4
9.


Package natbib Warning: Citation `ance' on page 2 undefined on input line 51.


Package natbib Warning: Citation `cocohanere' on page 2 undefined on input line
 51.


Package natbib Warning: Citation `graphcodebert' on page 2 undefined on input l
ine 53.

[2]

LaTeX Warning: Reference `sec:ablations' on page 3 undefined on input line 77.


LaTeX Warning: Reference `tab:main_standard' on page 3 undefined on input line 
98.


LaTeX Warning: Reference `tab:main_querysplit' on page 3 undefined on input lin
e 122.


LaTeX Warning: Reference `tab:bootstrap' on page 3 undefined on input line 151.


[3]

LaTeX Warning: Reference `tab:unixcoder' on page 4 undefined on input line 176.



Package natbib Warning: Citation `repobench' on page 4 undefined on input line 
199.


LaTeX Warning: Reference `tab:repobench' on page 4 undefined on input line 199.



LaTeX Warning: Reference `tab:stratified_neg' on page 4 undefined on input line
 226.


LaTeX Warning: Reference `tab:stratified_struct' on page 4 undefined on input l
ine 226.

[4]

LaTeX Warning: Reference `tab:temperature' on page 5 undefined on input line 26
9.


LaTeX Warning: Reference `tab:poolsize' on page 5 undefined on input line 295.


LaTeX Warning: Reference `tab:criterion' on page 5 undefined on input line 324.


[5]

LaTeX Warning: Reference `tab:hop' on page 6 undefined on input line 353.


LaTeX Warning: Reference `tab:scaling' on page 6 undefined on input line 371.


LaTeX Warning: Reference `tab:fusion' on page 6 undefined on input line 389.


LaTeX Warning: Reference `tab:failure' on page 6 undefined on input line 413.

[6]

LaTeX Warning: Reference `sec:criterion' on page 7 undefined on input line 449.


[7] [8]

Package natbib Warning: There were undefined citations.

[9] [10] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 155050 bytes).
Transcript written on paper.log.
\OT1/ptm/m/n/10.95 ing. Co-Co-HaNeRe []Su et al.[] [[]2025[]] (ACM TOSEM 2025) 
com-pares gradient-based and non-differentiable

Overfull \hbox (0.1379pt too wide) in paragraph at lines 53--54
\OT1/ptm/m/n/10.95 et al.[] [[]2021[]] in-cor-po-rates data-flow edges as at-te
n-tion bias. Our ap-proach dif-fers: we use inter-procedural
[2] [3] [4] [5] [6] [7] [8] [9] [10] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 157929 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91f18366-be1a-4eb7-bafa-954c3971fc97",
  "isSidechain": false,
  "promptId": "724d7aca-00e7-494b-8d2d-e8d37c28745c",
  "type": "user",
  "uuid": "ceb56c0c-900b-4ccd-9345-8452102d1786",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `swerank' on page 1 undefined on input line 27\n.\n\n\nPackage natbib Warning: Citation `swefixer' on page 1 undefined on input line 2\n7.\n\n\nPackage natbib Warning: Citation `cocohanere' on page 1 undefined on input line\n 29.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\n\nPackage natbib Warning: Citation `swerank' on page 2 undefined on input line 49\n.\n\n\nPackage natbib Warning: Citation `swefixer' on page 2 undefined on input line 4\n9.\n\n\nPackage natbib Warning: Citation `locagent' on page 2 undefined on input line 4\n9.\n\n\nPackage natbib Warning: Citation `ance' on page 2 undefined on input line 51.\n\n\nPackage natbib Warning: Citation `cocohanere' on page 2 undefined on input line\n 51.\n\n\nPackage natbib Warning: Citation `graphcodebert' on page 2 undefined on input l\nine 53.\n\n[2]\n\nLaTeX Warning: Reference `sec:ablations' on page 3 undefined on input line 77.\n\n\nLaTeX Warning: Reference `tab:main_standard' on page 3 undefined on input line \n98.\n\n\nLaTeX Warning: Reference `tab:main_querysplit' on page 3 undefined on input lin\ne 122.\n\n\nLaTeX Warning: Reference `tab:bootstrap' on page 3 undefined on input line 151.\n\n\n[3]\n\nLaTeX Warning: Reference `tab:unixcoder' on page 4 undefined on input line 176.\n\n\n\nPackage natbib Warning: Citation `repobench' on page 4 undefined on input line \n199.\n\n\nLaTeX Warning: Reference `tab:repobench' on page 4 undefined on input line 199.\n\n\n\nLaTeX Warning: Reference `tab:stratified_neg' on page 4 undefined on input line\n 226.\n\n\nLaTeX Warning: Reference `tab:stratified_struct' on page 4 undefined on input l\nine 226.\n\n[4]\n\nLaTeX Warning: Reference `tab:temperature' on page 5 undefined on input line 26\n9.\n\n\nLaTeX Warning: Reference `tab:poolsize' on page 5 undefined on input line 295.\n\n\nLaTeX Warning: Reference `tab:criterion' on page 5 undefined on input line 324.\n\n\n[5]\n\nLaTeX Warning: Reference `tab:hop' on page 6 undefined on input line 353.\n\n\nLaTeX Warning: Reference `tab:scaling' on page 6 undefined on input line 371.\n\n\nLaTeX Warning: Reference `tab:fusion' on page 6 undefined on input line 389.\n\n\nLaTeX Warning: Reference `tab:failure' on page 6 undefined on input line 413.\n\n[6]\n\nLaTeX Warning: Reference `sec:criterion' on page 7 undefined on input line 449.\n\n\n[7] [8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] [10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 155050 bytes).\nTranscript written on paper.log.\n\\OT1/ptm/m/n/10.95 ing. Co-Co-HaNeRe []Su et al.[] [[]2025[]] (ACM TOSEM 2025) \ncom-pares gradient-based and non-differentiable\n\nOverfull \\hbox (0.1379pt too wide) in paragraph at lines 53--54\n\\OT1/ptm/m/n/10.95 et al.[] [[]2021[]] in-cor-po-rates data-flow edges as at-te\nn-tion bias. Our ap-proach dif-fers: we use inter-procedural\n[2] [3] [4] [5] [6] [7] [8] [9] [10] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 157929 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "91f18366-be1a-4eb7-bafa-954c3971fc97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T150348 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context…",
  "leafUuid": "ceb56c0c-900b-4ccd-9345-8452102d1786",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream mining evaluation",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c"
}
```

---

### Assistant

_source line 36 · 2026-05-16T15:54:34.389Z_

PDF 编译成功，10 页，157KB。所有交叉引用和引文已解析。

输出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.pdf`

论文覆盖全部 15 个实验数据集：主实验 4-strategy 对比（标准 + query-split 两套评估）、bootstrap CIs、UniXcoder scale boundary、RepoBench-R 外部验证、5 层分层分析、温度消融、pool size 敏感性、checkpoint criterion 效应分析、hop depth 消融、数据量 scaling、fusion head 消融、weighted vs binary、static vs dynamic mining、失败案例分析、定性示例。三条贡献线完整呈现：embedding mining 可靠性 + representation geometry interaction + checkpoint criterion 方法论发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ceb56c0c-900b-4ccd-9345-8452102d1786",
  "isSidechain": false,
  "requestId": "req_011Cb6X2t8ZMi3x6RGpKMiaq",
  "type": "assistant",
  "uuid": "fc8ecaa4-b2bc-404e-968c-5e13185cc5ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJcdCASKuwyksnntKJ8Fes",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4002,
      "cache_read_input_tokens": 63155,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4002,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 63155,
          "cache_creation_input_tokens": 4002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4002
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

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T150348 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context…",
  "leafUuid": "fc8ecaa4-b2bc-404e-968c-5e13185cc5ba",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream mining evaluation",
  "sessionId": "c4e37549-6632-48cc-a879-3de6d7b0e94c"
}
```

---
