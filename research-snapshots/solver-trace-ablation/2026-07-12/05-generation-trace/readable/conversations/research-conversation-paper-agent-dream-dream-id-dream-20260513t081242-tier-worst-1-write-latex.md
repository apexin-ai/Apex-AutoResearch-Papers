# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T081242 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/ed25cbee-36c3-40dd-ae0a-cde849c662b4.jsonl`
- **Structured JSON:** [`393e7981bda87158aafe.json`](../../sessions/39/393e7981bda87158aafe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T08:54:33.176Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T08:54:33.176Z",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T081242 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Method paper 不可行，必须 pivot 为 analysis paper。 新叙事：\"Why Cross-Method Circuit Consensus Fails: An Empirical Analysis\"。 核心贡献变为：(1) 揭示 circuit discovery 方法在多数任务上高度相关或互补性不足， binary consensus 的前提（独立证据源）在实践中很少满足； (2) ACDC isinf binarization 问题的系统性分析（Claim 3，已强支撑）； (3) CSS 跨模型 scaling 的结构性失败（D034，179k-edge graph 下所有方法 Jaccard≈0）； (4) Jaccard 作为方法兼容性诊断工具（不再是 \"predicts success\" 而是 \"explains failure\"）。 IOI GPT-2 成为 \"唯一有效案例\" 的 case study 而非 generalization 的起点。 投稿目标降级为 EMNLP Findings 或 workshop paper。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-13T08:54:33.180Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T08:54:33.180Z",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-13T08:54:33.203Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T081242 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Method paper 不可行，必须 pivot 为 analysis paper。 新叙事："Why Cross-Method Circuit Consensus Fails: An Empirical Analysis"。 核心贡献变为：(1) 揭示 circuit discovery 方法在多数任务上高度相关或互补性不足， binary consensus 的前提（独立证据源）在实践中很少满足； (2) ACDC isinf binarization 问题的系统性分析（Claim 3，已强支撑）； (3) CSS 跨模型 scaling 的结构性失败（D034，179k-edge graph 下所有方法 Jaccard≈0）； (4) Jaccard 作为方法兼容性诊断工具（不再是 "predicts success" 而是 "explains failure"）。 IOI GPT-2 成为 "唯一有效案例" 的 case study 而非 generalization 的起点。 投稿目标降级为 EMNLP Findings 或 workshop paper。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "aae39cf0-5fb2-4fec-8482-5067bb253164",
  "type": "user",
  "uuid": "aacfbbb3-cf73-440e-b5ab-48c03d545be9",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T08:54:33.202Z_

```json
{
  "parentUuid": "aacfbbb3-cf73-440e-b5ab-48c03d545be9",
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
  "uuid": "1fc4f615-9cef-4c57-b659-ad74cf14917e",
  "timestamp": "2026-05-13T08:54:33.202Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T08:54:33.202Z_

```json
{
  "parentUuid": "1fc4f615-9cef-4c57-b659-ad74cf14917e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4aec1189-8780-492c-8123-91fe7b561f86",
  "timestamp": "2026-05-13T08:54:33.202Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
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
  "aiTitle": "Generate worst-tier simulation paper for dream_id",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4"
}
```

---

### Assistant

_source line 7 · 2026-05-13T08:54:37.229Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aec1189-8780-492c-8123-91fe7b561f86",
  "isSidechain": false,
  "requestId": "req_011CazHbH8A79XdTvry3eoz3",
  "type": "assistant",
  "uuid": "fb279504-e9fe-486e-b8d6-0eb90aa854ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdqTtnUaexP9hGLWKEhRvm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11306,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11306
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

_source line 8 · 2026-05-13T08:54:38.286Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WXEvD7HCuHS9uGa2sRUA4r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb279504-e9fe-486e-b8d6-0eb90aa854ad",
  "isSidechain": false,
  "requestId": "req_011CazHbH8A79XdTvry3eoz3",
  "type": "assistant",
  "uuid": "26b70f7a-9575-4483-9af3-07e52a4c9ecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdqTtnUaexP9hGLWKEhRvm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11306,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11306
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

_source line 9 · 2026-05-13T08:54:38.479Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V1a1DmjsmKwMSDmSMFcHMA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26b70f7a-9575-4483-9af3-07e52a4c9ecc",
  "isSidechain": false,
  "requestId": "req_011CazHbH8A79XdTvry3eoz3",
  "type": "assistant",
  "uuid": "53276b9f-4d5d-48c2-8693-ebc8b96fabe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdqTtnUaexP9hGLWKEhRvm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11306,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11306
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

_source line 10 · 2026-05-13T08:54:38.485Z_

<details><summary>↩ Tool result · `toolu_01V1a1DmjsmKwMSDmSMFcHMA`</summary>

```text
1	# Paper Framing — structfuse-context
2	
3	> 最后更新: 2026-05-13 | 更新原因: MVP 结果出齐，基于 D027 reframe
4	
5	## Target Venue
6	EMNLP 2026 Main (ARR deadline 2026-05-25)
7	
8	## Core Insight
9	Cross-method binary consensus (CSS) identifies faithful and edge-efficient circuit subsets **when discovery methods genuinely disagree** (low pairwise Jaccard). When methods are highly correlated (high Jaccard), CSS degenerates and provides no additional value over any single method. Inter-method correlation is a predictive signal for consensus utility.
10	
11	## Narrative Arc
12	1. Circuit discovery methods (EAP-IG, Edge Pruning, ACDC) find different circuits for the same task — but which edges are "real"?
13	2. We propose CSS: binary consensus scoring across K≥3 methods from different algorithmic families
14	3. CSS=1.0 (full consensus) circuits are dramatically smaller yet comparably or more faithful — but only when methods provide independent evidence
15	4. When methods are correlated (same algorithmic family, or task structure forces agreement), CSS degenerates to the most selective method
16	5. This reveals a fundamental property: consensus value ∝ method diversity, measurable via pairwise Jaccard
17	
18	## Core Claims
19	
20	### Claim 1: CSS identifies edge-efficient consensus circuits (PRIMARY)
21	- **Evidence needed**: CSS=1.0 CPR ≥ best single-method CPR on tasks with low inter-method Jaccard
22	- **Current status**: IOI PASS (CSS=1.0 14 edges, CPR=0.109 > all 50-edge single methods)
23	- **Strength**: Strong on IOI; needs 2+ more localized-circuit tasks
24	
25	### Claim 2: CSS utility is predicted by inter-method correlation (PRIMARY)
26	- **Evidence needed**: Positive correlation between method diversity (1 - max pairwise Jaccard) and CSS faithfulness advantage
27	- **Current status**: IOI Jaccard=0.31 → CSS works; Arithmetic Jaccard=0.695 → CSS fails. Two data points.
28	- **Strength**: Mechanistically motivated, needs 3+ tasks to establish pattern
29	
30	### Claim 3: ACDC isinf binarization causes CSS degeneration (METHODOLOGICAL)
31	- **Evidence needed**: Show CSS=1.0 ≡ ACDC under isinf; top-k breaks degeneration
32	- **Current status**: Fully demonstrated on both IOI and Arithmetic
33	- **Strength**: Strong, fully supported
34	
35	### Claim 4: CSS as diagnostic taxonomy (SECONDARY)
36	- **Evidence needed**: CSS distribution (1/3, 2/3, 3/3 proportions) reveals task structure
37	- **Current status**: IOI has dispersed CSS distribution (low 3/3 ratio); Arithmetic has concentrated distribution (high 3/3 ratio when k normalized)
38	- **Strength**: Needs more tasks and mechanistic analysis
39	
40	## Anticipated Reviewer Concerns
41	
42	### R1: "Only 2 tasks, generalization unclear"
43	- **Mitigation**: Add SVA (localized), DocQA or similar (distributed) to establish pattern
44	- **Phase 2 models with IFR** naturally increase method diversity → should help
45	
46	### R2: "CSS=1.0 edge efficiency could be just circuit size effect"
47	- **Mitigation**: Size-normalized CPR comparison; show CSS=1.0 achieves same CPR as 3-5x larger single-method circuits
48	
49	### R3: "EAP-IG and EP are gradient-adjacent, K=3 effectively K≈2"
50	- **Mitigation**: Phase 2 adds IFR (similarity-based, different family); Jaccard analysis shows exactly when this matters
51	
52	### R4: "Why not use score averaging instead of binary consensus?"
53	- **Mitigation**: Binary consensus is threshold-free (no score calibration needed across methods); compare with Mondorf et al. score averaging
54	
55	### R5: "ACDC binarization sensitivity undermines robustness"
56	- **Mitigation**: Top-k normalization as standard preprocessing; show results stable across k=50-150
57	
58	## Competitors
59	- **CIRCUS** (Parekh 2026): Threshold diversity within single method; we tried it, it failed (D021 negative ablation)
60	- **Mondorf et al.** (2510.06811): Cross-method score averaging (gradient family only); we use binary consensus across diverse families
61	- **PIE** (2604.16889): Iterative pruning ensemble; single paradigm
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53276b9f-4d5d-48c2-8693-ebc8b96fabe3",
  "isSidechain": false,
  "promptId": "aae39cf0-5fb2-4fec-8482-5067bb253164",
  "type": "user",
  "uuid": "c0fd6fc7-b1fb-4c5a-bb80-327a93719cf0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper_framing.md",
      "content": "# Paper Framing — structfuse-context\n\n> 最后更新: 2026-05-13 | 更新原因: MVP 结果出齐，基于 D027 reframe\n\n## Target Venue\nEMNLP 2026 Main (ARR deadline 2026-05-25)\n\n## Core Insight\nCross-method binary consensus (CSS) identifies faithful and edge-efficient circuit subsets **when discovery methods genuinely disagree** (low pairwise Jaccard). When methods are highly correlated (high Jaccard), CSS degenerates and provides no additional value over any single method. Inter-method correlation is a predictive signal for consensus utility.\n\n## Narrative Arc\n1. Circuit discovery methods (EAP-IG, Edge Pruning, ACDC) find different circuits for the same task — but which edges are \"real\"?\n2. We propose CSS: binary consensus scoring across K≥3 methods from different algorithmic families\n3. CSS=1.0 (full consensus) circuits are dramatically smaller yet comparably or more faithful — but only when methods provide independent evidence\n4. When methods are correlated (same algorithmic family, or task structure forces agreement), CSS degenerates to the most selective method\n5. This reveals a fundamental property: consensus value ∝ method diversity, measurable via pairwise Jaccard\n\n## Core Claims\n\n### Claim 1: CSS identifies edge-efficient consensus circuits (PRIMARY)\n- **Evidence needed**: CSS=1.0 CPR ≥ best single-method CPR on tasks with low inter-method Jaccard\n- **Current status**: IOI PASS (CSS=1.0 14 edges, CPR=0.109 > all 50-edge single methods)\n- **Strength**: Strong on IOI; needs 2+ more localized-circuit tasks\n\n### Claim 2: CSS utility is predicted by inter-method correlation (PRIMARY)\n- **Evidence needed**: Positive correlation between method diversity (1 - max pairwise Jaccard) and CSS faithfulness advantage\n- **Current status**: IOI Jaccard=0.31 → CSS works; Arithmetic Jaccard=0.695 → CSS fails. Two data points.\n- **Strength**: Mechanistically motivated, needs 3+ tasks to establish pattern\n\n### Claim 3: ACDC isinf binarization causes CSS degeneration (METHODOLOGICAL)\n- **Evidence needed**: Show CSS=1.0 ≡ ACDC under isinf; top-k breaks degeneration\n- **Current status**: Fully demonstrated on both IOI and Arithmetic\n- **Strength**: Strong, fully supported\n\n### Claim 4: CSS as diagnostic taxonomy (SECONDARY)\n- **Evidence needed**: CSS distribution (1/3, 2/3, 3/3 proportions) reveals task structure\n- **Current status**: IOI has dispersed CSS distribution (low 3/3 ratio); Arithmetic has concentrated distribution (high 3/3 ratio when k normalized)\n- **Strength**: Needs more tasks and mechanistic analysis\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Only 2 tasks, generalization unclear\"\n- **Mitigation**: Add SVA (localized), DocQA or similar (distributed) to establish pattern\n- **Phase 2 models with IFR** naturally increase method diversity → should help\n\n### R2: \"CSS=1.0 edge efficiency could be just circuit size effect\"\n- **Mitigation**: Size-normalized CPR comparison; show CSS=1.0 achieves same CPR as 3-5x larger single-method circuits\n\n### R3: \"EAP-IG and EP are gradient-adjacent, K=3 effectively K≈2\"\n- **Mitigation**: Phase 2 adds IFR (similarity-based, different family); Jaccard analysis shows exactly when this matters\n\n### R4: \"Why not use score averaging instead of binary consensus?\"\n- **Mitigation**: Binary consensus is threshold-free (no score calibration needed across methods); compare with Mondorf et al. score averaging\n\n### R5: \"ACDC binarization sensitivity undermines robustness\"\n- **Mitigation**: Top-k normalization as standard preprocessing; show results stable across k=50-150\n\n## Competitors\n- **CIRCUS** (Parekh 2026): Threshold diversity within single method; we tried it, it failed (D021 negative ablation)\n- **Mondorf et al.** (2510.06811): Cross-method score averaging (gradient family only); we use binary consensus across diverse families\n- **PIE** (2604.16889): Iterative pruning ensemble; single paradigm\n",
      "numLines": 62,
      "startLine": 1,
      "totalLines": 62
    }
  },
  "sourceToolAssistantUUID": "53276b9f-4d5d-48c2-8693-ebc8b96fabe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T08:54:38.618Z_

<details><summary>↩ Tool result · `toolu_01WXEvD7HCuHS9uGa2sRUA4r`</summary>

```text
1	[
2	  {
3	    "name": "GPT-2 SVA K=3 CSS（css_1.00 重新评估）",
4	    "description": "已有两次运行（mvp_sva_gpt2_k3 top-100, mvp_sva_gpt2_k3_topk top-k）。 Worst 档下 SVA re-eval 用 css_1.00 重新评估条件④，Δ(CPR) 降至 <0.005 或为负值， condition④ FAIL。D033 降级为 inconclusive 在 worst 档下进一步恶化： 多 seed bootstrap 表明 Δ=0.0127 是上界，真实均值 ≤0.003。\n",
5	    "results": {
6	      "status": "done",
7	      "conclusion": "negative",
8	      "pairwise_jaccard": {
9	        "eapig_x_ep": 0.6529,
10	        "eapig_x_acdc": 0.3158,
11	        "ep_x_acdc": 0.4184
12	      },
13	      "max_jaccard": 0.6529,
14	      "three_way_ratio": 0.2785,
15	      "css_distribution": {
16	        "0.33": 60,
17	        "0.67": 54,
18	        "1.00": 44
19	      },
20	      "faithfulness_mean": {
21	        "css_1.00": {
22	          "edges": 44,
23	          "CPR": 1.173,
24	          "CMD": 0.558
25	        },
26	        "css_0.67": {
27	          "edges": 98,
28	          "CPR": 1.1724,
29	          "CMD": 0.503
30	        },
31	        "eapig_k75": {
32	          "edges": 75,
33	          "CPR": 1.1703,
34	          "CMD": 0.53
35	        },
36	        "ep_k75": {
37	          "edges": 75,
38	          "CPR": 1.1703,
39	          "CMD": 0.53
40	        },
41	        "acdc_k75": {
42	          "edges": 75,
43	          "CPR": 1.1746,
44	          "CMD": 0.52
45	        }
46	      },
47	      "css_1.00_delta_cpr": -0.0016,
48	      "d025_cond4_verdict": "FAIL (css_1.00 CPR=1.173 < acdc=1.175, Δ=−0.002)",
49	      "bootstrap_analysis": {
50	        "n_seeds": 5,
51	        "delta_mean": 0.003,
52	        "delta_95ci": "[-0.012, +0.019]",
53	        "ci_includes_zero": true
54	      },
55	      "sva_gate_verdict": "FAIL — multi-seed bootstrap CI includes zero; D033 inconclusive confirmed as negative"
56	    },
57	    "tables": [
58	      {
59	        "caption": "Table: SVA css_1.00 multi-seed bootstrap (worst tier)",
60	        "rows": [
61	          [
62	            "Seed",
63	            "CSS=1.0 CPR",
64	            "ACDC CPR",
65	            "Δ"
66	          ],
67	          [
68	            "42 (original)",
69	            "1.187",
70	            "1.175",
71	            "+0.013"
72	          ],
73	          [
74	            "123",
75	            "1.168",
76	            "1.179",
77	            "−0.011"
78	          ],
79	          [
80	            "456",
81	            "1.178",
82	            "1.182",
83	            "−0.004"
84	          ],
85	          [
86	            "789",
87	            "1.175",
88	            "1.170",
89	            "+0.005"
90	          ],
91	          [
92	            "1024",
93	            "1.171",
94	            "1.174",
95	            "−0.003"
96	          ],
97	          [
98	            "mean ± std",
99	            "1.176 ± 0.007",
100	            "1.176 ± 0.005",
101	            "+0.000 ± 0.009"
102	          ]
103	        ]
104	      },
105	      {
106	        "caption": "Table: SVA D025 conditions (worst tier final)",
107	        "rows": [
108	          [
109	            "Condition",
110	            "Result",
111	            "Note"
112	          ],
113	          [
114	            "①Jaccard<0.70",
115	            "PASS (0.653)",
116	            "marginal"
117	          ],
118	          [
119	            "②CSS≥2/3≥10",
120	            "PASS (54)",
121	            ""
122	          ],
123	          [
124	            "③CSS=1.0≥3",
125	            "PASS (44)",
126	            ""
127	          ],
128	          [
129	            "④CPR dominance",
130	            "FAIL (Δ≈0, CI includes zero)",
131	            "D033→negative"
132	          ]
133	        ]
134	      }
135	    ],
136	    "figures": [],
137	    "analysis": "SVA 在 worst 档下确认为 FAIL。至此 GPT-2 三任务中仅 IOI 明确 PASS， 成功率 1/3。SVA 的 max_jaccard=0.653 过高，gradient methods 主导的 consensus 退化为 ACDC 和 gradient-pair 交集。对 Claim 2 提供了一个符合预期方向的数据点 （高 Jaccard → CSS 无优势），但 Δ≈0 无法区分 \"marginal positive\" 和 \"neutral\"， 这是 n=3-4 时 Jaccard-utility regression 的致命噪声源。\n\n\nD032 报告的 Δ=0.0127 来自单一 seed（seed=42）。Worst 档假设这是随机波动上界： SVA 的 EAP-IG×EP Jaccard=0.6529 接近 Arithmetic 的 0.695， 两种 gradient 方法在 SVA number-tracking heads (layer 7-10) 上高度一致， ACDC top-k 虽然引入了名义上的 \"第三视角\"，但其在 GPT-2 12层模型上的 greedy search 仍然优先选择与 gradient saliency 高度相关的边。在 5 个 bootstrap seeds 下， css_1.00 CPR 的波动范围 [1.168, 1.192]，acdc CPR 的波动范围 [1.170, 1.182]， 两者重叠区域大——Δ 的 95% CI 横跨零点。实际观测到的 Δ=0.0127 恰好落在 CI 上界附近， 属于统计上的 \"lucky draw\"。D033 的 \"inconclusive\" 判定在 worst 档下变为明确 FAIL： 无法区分 CSS=1.0 和 ACDC 单方法。SVA 从 \"marginal PASS\" 彻底变为 FAIL。\n"
138	  },
139	  {
140	    "name": "GPT-2 Factual Recall K=3 CSS",
141	    "description": "GPT-2 Small 上的 factual recall (国家首都)。GPT-2 Small 117M 参数 对 factual knowledge 能力极弱，circuit discovery 前提（clean baseline performance）不满足。\n",
142	    "results": {
143	      "status": "abandoned",
144	      "conclusion": "task_model_mismatch",
145	      "partial_metrics": {
146	        "baseline_accuracy": 0.52,
147	        "baseline_accuracy_note": "几乎随机 (random=0.25, GPT-2 仅略好)",
148	        "eapig_completed": true,
149	        "ep_completed": true,
150	        "acdc_completed": false,
151	        "acdc_failure_reason": "GPT-2 Small 对 \"The capital of France is ___\" 类问题准确率 ~52%， clean performance 波动 ±15%。ACDC patching 在 baseline 不稳定时 无法收敛——阈值过高得空电路，过低保留全图。\n",
152	        "eapig_k50_cpr": 0.02,
153	        "ep_k50_cpr": -0.01,
154	        "cpr_note": "faithfulness 接近零，电路无意义"
155	      }
156	    },
157	    "tables": [],
158	    "figures": [],
159	    "analysis": "第四 GPT-2 任务失败。论文只能报告 3 个 GPT-2 tasks。 在 Limitations 说明 GPT-2 Small 对 factual recall 能力不足。 Reviewer 攻击 \"only 3 tasks on one tiny model\" 时防守空间有限。\n\n\nGPT-2 Small 的 parametric knowledge 极度稀疏——factual recall 没有形成 dedicated retrieval circuit。信息分散在 residual stream 中，无法 localize。 这不是 CSS 方法论的失败，而是 task-model 根本不匹配。 ACDC 对这种 diffuse computation 最敏感：所有边的 importance 都在噪声水平。 Worst 档下这个实验浪费了 ~4 GPU hours 才确认失败，挤占了写作时间。\n"
160	  },
161	  {
162	    "name": "Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + ACDC top-k)",
163	    "description": "D029 后用 ACDC top-k 替代 IFR。D034 已确认结果：CSS=1.0=0 边， 所有 pairwise Jaccard≈0。CSS 跨模型 scaling 根本性失败。 Worst 档下这是 paper 的致命打击——CSS 仅在 GPT-2 (32k edges) 上工作， 无法 scale 到 Qwen (179k edges)。\n",
164	    "results": {
165	      "status": "done",
166	      "conclusion": "negative",
167	      "total_edges": 179388,
168	      "binarization": "top-0.3% (~538 edges per method)",
169	      "pairwise_jaccard": {
170	        "eapig_x_ep": 0.042,
171	        "eapig_x_acdc": 0.006,
172	        "ep_x_acdc": 0.008
173	      },
174	      "max_jaccard": 0.042,
175	      "css_distribution": {
176	        "1/3": 1058,
177	        "2/3": 66,
178	        "3/3": 0
179	      },
180	      "css_core_3of3": 0,
181	      "faithfulness_mean": {
182	        "css_0.67": {
183	          "edges": 66,
184	          "CPR": 0.031,
185	          "CMD": 0.972
186	        },
187	        "eapig_top538": {
188	          "edges": 538,
189	          "CPR": 0.055,
190	          "CMD": 0.948
191	        },
192	        "ep_top538": {
193	          "edges": 538,
194	          "CPR": 0.048,
195	          "CMD": 0.955
196	        },
197	        "acdc_top538": {
198	          "edges": 538,
199	          "CPR": 0.029,
200	          "CMD": 0.974
201	        }
202	      },
203	      "d025_verdict": "FAIL — CSS=1.0 = empty set",
204	      "ifr_version_comparison": {
205	        "ifr_jaccard_eapig": 0.0,
206	        "ifr_jaccard_ep": 0.0,
207	        "acdc_jaccard_eapig": 0.006,
208	        "acdc_jaccard_ep": 0.008,
209	        "note": "ACDC 比 IFR 稍好但仍实质为零——问题不在方法选择而在模型规模"
210	      },
211	      "scaling_analysis": {
212	        "gpt2_edge_space": 32491,
213	        "qwen_edge_space": 179388,
214	        "ratio": 5.52,
215	        "gpt2_topk_pct": 0.31,
216	        "qwen_topk_pct": 0.3,
217	        "gpt2_max_jaccard": 0.307,
218	        "qwen_max_jaccard": 0.042,
219	        "jaccard_ratio": 7.3,
220	        "conclusion": "相同比例的 top-k 在更大 edge space 中产生更低 Jaccard，这是组合稀释效应"
221	      }
222	    },
223	    "tables": [
224	      {
225	        "caption": "Table: GPT-2 vs Qwen edge space scaling",
226	        "rows": [
227	          [
228	            "",
229	            "GPT-2 Small",
230	            "Qwen-2.5 0.5B",
231	            "Ratio"
232	          ],
233	          [
234	            "Total edges",
235	            "32,491",
236	            "179,388",
237	            "5.5×"
238	          ],
239	          [
240	            "Top-k (0.3%)",
241	            "~100",
242	            "~538",
243	            "5.4×"
244	          ],
245	          [
246	            "Max Jaccard (EAP-IG×EP)",
247	            "0.307",
248	            "0.042",
249	            "7.3×↓"
250	          ],
251	          [
252	            "CSS=1.0 edges",
253	            "7",
254	            "0",
255	            "—"
256	          ],
257	          [
258	            "CSS=1.0 CPR",
259	            "0.109",
260	            "—",
261	            "—"
262	          ]
263	        ]
264	      },
265	      {
266	        "caption": "Table: Qwen IOI method comparison — IFR vs ACDC (both fail)",
267	        "rows": [
268	          [
269	            "Third method",
270	            "J(×EAP-IG)",
271	            "J(×EP)",
272	            "CSS=1.0"
273	          ],
274	          [
275	            "IFR (D028)",
276	            "0.000",
277	            "0.000",
278	            "0 edges"
279	          ],
280	          [
281	            "ACDC (D034)",
282	            "0.006",
283	            "0.008",
284	            "0 edges"
285	          ]
286	        ]
287	      }
288	    ],
289	    "figures": [],
290	    "analysis": "D034 是 worst 档的核心证据之一。CSS 跨模型 scaling 的结构性失败 意味着论文不能 claim \"CSS generalizes across models\"。 在 analysis paper 中重构为：\"CSS 的 edge-level consensus 依赖于 methods 在相同 edge space 中有 meaningful overlap， 这一前提在 model scale up 时因组合稀释而系统性地被违反。\" 这是一个有价值的 negative finding，但将 CSS 定位为 \"仅适用于小模型\" 的方法。\n\n\nD034 已确认：ACDC 在 179k-edge Qwen 图上退化为 node-level scoring， 与 IFR 的 block-voting 问题本质相同。核心机制是组合稀释： top-0.3% 在 32k 边的 GPT-2 上选约 100 条边，方法间有 meaningful overlap； 在 179k 边的 Qwen 上选约 538 条边，但 edge space 增大 5.5×， 而 circuit structure 并非线性 scale——IOI circuit 在 Qwen 上分散到更多层/头， 方法各自 \"看到\" 不同子集。EAP-IG×EP Jaccard 从 GPT-2 的 0.31 暴跌至 0.04， ACDC 与任何方法几乎零重叠。CSS=1.0 要求三方法全部同意——在 Jaccard≈0 时 这是空集。即使放宽到 CSS≥0.67，也只有 66 条边，CPR=0.031 远低于单方法。 这证明 CSS 的前提（方法对同一 edge 有 meaningful overlap）在大模型上不成立。\n"
291	  },
292	  {
293	    "name": "Qwen-2.5 0.5B Arithmetic K=3 (EAP-IG + EP + ACDC top-k)",
294	    "description": "基于 D034 的结果，Qwen Arithmetic 预期与 Qwen IOI 相同模式： ACDC 在大 edge space 上退化，CSS=1.0 为空集或退化。\n",
295	    "results": {
296	      "status": "planned",
297	      "conclusion": "negative",
298	      "total_edges": "~179000",
299	      "pairwise_jaccard": {
300	        "eapig_x_ep": 0.038,
301	        "eapig_x_acdc": 0.004,
302	        "ep_x_acdc": 0.005
303	      },
304	      "max_jaccard": 0.038,
305	      "css_distribution": {
306	        "1/3": "~1080",
307	        "2/3": "~55",
308	        "3/3": 0
309	      },
310	      "css_core_3of3": 0,
311	      "faithfulness_mean": {
312	        "css_0.67": {
313	          "edges": "~55",
314	          "CPR": 0.025,
315	          "CMD": 0.978
316	        },
317	        "eapig_top538": {
318	          "edges": 538,
319	          "CPR": 0.049,
320	          "CMD": 0.954
321	        }
322	      },
323	      "d025_verdict": "FAIL — CSS=1.0 = empty set, same as Qwen IOI",
324	      "qwen_ioi_css10_cpr_vs_best": null,
325	      "note": "CSS=1.0 为空集，无法计算 CPR vs best single"
326	    },
327	    "tables": [
328	      {
329	        "caption": "Table: Qwen tasks — all fail with same pattern",
330	        "rows": [
331	          [
332	            "Task",
333	            "CSS=1.0 edges",
334	            "Max Jaccard",
335	            "Verdict"
336	          ],
337	          [
338	            "IOI (IFR)",
339	            "0",
340	            "0.000",
341	            "FAIL"
342	          ],
343	          [
344	            "IOI (ACDC)",
345	            "0",
346	            "0.042",
347	            "FAIL"
348	          ],
349	          [
350	            "Arithmetic (ACDC, predicted)",
351	            "0",
352	            "~0.038",
353	            "FAIL"
354	          ]
355	        ]
356	      }
357	    ],
358	    "figures": [],
359	    "analysis": "Qwen Arithmetic 是 sunk cost。D034 已证明问题是结构性的（edge space scaling）， 不因任务而异。在 analysis paper 中只需一句： \"We verified the scaling failure extends to Arithmetic (Table X)\"。 不值得单独的 figure 或 detailed analysis。\n\n\nQwen IOI (D034) 已证明 ACDC 在 179k-edge graph 上退化。 Arithmetic 在 Qwen 上的 edge space 与 IOI 几乎相同（同一模型）， EAP-IG×EP 的 Jaccard 预期更低（Arithmetic 在更大模型上更分散）， ACDC 的退化模式完全相同（node-level scoring）。 这个实验本质上是 Qwen IOI 的重复，不产生新信息。 Worst 档建议：如果 Qwen IOI 已 FAIL，跳过 Qwen Arithmetic 以节省时间。\n"
360	  },
361	  {
362	    "name": "Gemma-2 2B IOI K=3",
363	    "description": "Scale 到 2B 模型。Worst 档下 Qwen 0.5B 已完全失败， Gemma-2 2B 的 edge space 更大（~500k+），失败是确定性的。\n",
364	    "results": {
365	      "status": "not_attempted",
366	      "conclusion": null,
367	      "predicted_outcome": "FAIL — edge space ~500k+, Jaccard→0, CSS=1.0→empty set",
368	      "reason_not_attempted": "D034 已证明 CSS 在 179k-edge Qwen 上失败。Gemma-2 2B 有 26 层 16 头， edge space 估计 >500k，组合稀释效应更严重。 投入 ~16 GPU-hours 仅为确认一个已知结论不合理。\n"
369	    },
370	    "tables": [],
371	    "figures": [],
372	    "analysis": "明确建议取消。节省 16 GPU-hours 和 2 天调试时间用于论文写作。 在 paper 中用 back-of-envelope 计算替代实验： \"At Gemma-2 2B scale (~500k edges), top-0.3% binarization yields ~1500 edges per method; extrapolating from GPT-2→Qwen Jaccard decay (0.31→0.04), expected max Jaccard ≈ 0.01, rendering consensus trivially empty.\"\n\n\nGemma-2 2B 的 edge space 是 Qwen 的 ~3×，Qwen 上已观察到 Jaccard→0。 在更大 edge space 中，top-0.3% 选约 1500+ 条边，但三种方法各自 \"看到\" 的功能通路更加分散——26 层中 IOI 信息流经更多 intermediate heads。 CSS 的 edge-level consensus 前提在此彻底不成立。 这个实验的唯一价值是确认 \"scaling law\"，但 GPT-2 → Qwen 的两个数据点 已足够支撑 analysis paper 的论点。\n"
373	  },
374	  {
375	    "name": "Llama-3.1 8B IOI K=3",
376	    "description": "最大规模实验。Worst 档下无论如何都不应运行。\n",
377	    "results": {
378	      "status": "not_attempted",
379	      "conclusion": null,
380	      "predicted_outcome": "FAIL — edge space ~2M+, hardware insufficient (needs A100 80GB)",
381	      "reason_not_attempted": "P3 priority + hardware barrier (RTX 4090D 24GB insufficient for EP) + D034 已证明 scaling failure"
382	    },
383	    "tables": [],
384	    "figures": [],
385	    "analysis": "明确取消。在 Future Work 中一句带过即可。\n\n\n8B 模型有 32 层 32 头，edge space 估计 ~2M。 top-0.3% ≈ 6000 条边/方法，但 pairwise Jaccard 在如此巨大的空间中 趋近于 random intersection baseline (~0.003)。 EP 在 8B 上需要 A100 80GB（edge-level pruning 内存超线性增长）， 当前 RTX 4090D 24GB 完全不够。即使有硬件，ROI 为负。\n"
386	  },
387	  {
388	    "name": "Top-k Binarization Sensitivity Sweep",
389	    "description": "系统性 top-k sweep (k=50, 75, 100, 150) 在 GPT-2 tasks 上。 Worst 档下 CSS CPR 对 k 稳定——但这只证明 CSS 是 \"consistently mediocre\"， 优势永远不超过 single method（IOI 除外）。 关键发现：ACDC isinf-vs-topk 的 Jaccard 差异驱动了虚假的 Jaccard-utility 关联。\n",
390	    "results": {
391	      "status": "done",
392	      "conclusion": "stable_but_irrelevant",
393	      "ioi_gpt2_css_cpr_by_k": {
394	        "k50": 0.109,
395	        "k75": 0.102,
396	        "k100": 0.095,
397	        "k150": 0.088
398	      },
399	      "sva_gpt2_css_cpr_by_k": {
400	        "k50": -0.82,
401	        "k75": -0.82,
402	        "k100": -0.74,
403	        "k150": -0.71
404	      },
405	      "arithmetic_gpt2_css_cpr_by_k": {
406	        "k50": 0.919,
407	        "k75": 0.919,
408	        "k100": 0.926,
409	        "k150": 0.933
410	      },
411	      "sva_mean_css_cpr_by_k": {
412	        "k50": 1.185,
413	        "k75": 1.187,
414	        "k100": 1.174,
415	        "k150": 1.168
416	      },
417	      "css_stable_across_k": true,
418	      "but_advantage_never_positive_except_ioi": true,
419	      "key_finding": "CSS CPR 在 k=50-150 内稳定 (std<0.02)，但这只说明 binarization 不是 CSS 失败的原因—— 方法相关性才是。CSS 在 SVA 和 Arithmetic 上 never beats single method， 无论 k 取什么值。\n",
420	      "acdc_isinf_vs_topk_jaccard_gap": {
421	        "ioi": "isinf J=0.09 → topk J=0.25 (Δ=+0.16)",
422	        "arithmetic": "isinf J=0.17 → topk J=0.42 (Δ=+0.25)",
423	        "sva": "isinf J=0.37 → topk J=0.37 (Δ=0, already topk)"
424	      },
425	      "confound_implication": "IOI 的 \"low Jaccard → CSS works\" 部分由 ACDC isinf 的极端 sparsity (14 edges) 驱动。 ACDC isinf 人为压低了 ACDC×EAP-IG 和 ACDC×EP 的 Jaccard。 top-k 归一化后 IOI max Jaccard 从 0.31 上升到约 0.41 (EAP-IG×EP pair 不变， 但 ACDC pair 上升)。Jaccard-utility 关系中 IOI 的 \"low Jaccard\" 被 ACDC binarization inflated。\n"
426	    },
427	    "tables": [
428	      {
429	        "caption": "Table: CSS=1.0 CPR across k values (GPT-2 tasks, zero ablation for IOI, mean for others)",
430	        "rows": [
431	          [
432	            "Task",
433	            "k=50",
434	            "k=75",
435	            "k=100",
436	            "k=150",
437	            "Stable?",
438	            "Beats single?"
439	          ],
440	          [
441	            "IOI (zero)",
442	            "0.109",
443	            "0.102",
444	            "0.095",
445	            "0.088",
446	            "Yes",
447	            "Yes (all k)"
448	          ],
449	          [
450	            "SVA (mean)",
451	            "1.185",
452	            "1.187",
453	            "1.174",
454	            "1.168",
455	            "Yes",
456	            "No (all k)"
457	          ],
458	          [
459	            "Arith (mean)",
460	            "0.919",
461	            "0.919",
462	            "0.926",
463	            "0.933",
464	            "Yes",
465	            "No (all k)"
466	          ]
467	        ]
468	      },
469	      {
470	        "caption": "Table: ACDC binarization effect on Jaccard",
471	        "rows": [
472	          [
473	            "Task",
474	            "J (isinf)",
475	            "J (top-k)",
476	            "Δ",
477	            "CSS outcome changes?"
478	          ],
479	          [
480	            "IOI",
481	            "0.09",
482	            "0.25",
483	            "+0.16",
484	            "No (still PASS)"
485	          ],
486	          [
487	            "Arithmetic",
488	            "0.17",
489	            "0.42",
490	            "+0.25",
491	            "No (still FAIL)"
492	          ],
493	          [
494	            "SVA",
495	            "0.37 (already topk)",
496	            "0.37",
497	            "0",
498	            "N/A"
499	          ]
500	        ]
501	      }
502	    ],
503	    "figures": [],
504	    "analysis": "Binarization sensitivity 是 worst 档下最有分析价值的实验之一。 两个结论：(1) CSS 对 k 稳定——方法论上 clean； (2) Jaccard-utility 关系的一部分方差由 ACDC binarization 解释， 而非 genuine method diversity。 这为 analysis paper 提供了 \"binarization pathology taxonomy\" 贡献 （Claim 3 延伸），也是 \"why consensus fails\" 叙事的技术核心。\n\n\nTop-k 归一化使三种方法在 comparable edge budget 下比较，消除了 ACDC isinf 的 extreme sparsity artifact。k 越大，pairwise overlap 自然增加， CSS=1.0 集合扩大但新增的边是 low-confidence coincidental consensus。 IOI 在所有 k 下仍为正面是因为其 14 条核心 ACDC isinf 边（全被三方法确认） 质量极高——但这是 IOI 任务 + GPT-2 模型的特异性，非方法优势。 ACDC isinf-vs-topk Jaccard 差异是 worst 档 Jaccard-utility confound 的核心： 在 isinf 下 ACDC 只有 14-17 条边，与 100 条边的 EAP-IG/EP 的 Jaccard 自然极低； top-k 归一化后差异缩小，但 IOI 的正面结果不变—— 这说明 IOI 的 CSS 优势与 Jaccard level 关系弱于预期。\n"
505	  },
506	  {
507	    "name": "Ablation Method Comparison (Zero vs Mean vs Resample)",
508	    "description": "在 IOI 上比较 zero/mean/resample ablation 下 CSS 优势。 Worst 档揭示 IOI positive result 部分由 zero ablation bias 驱动。\n",
509	    "results": {
510	      "status": "partial",
511	      "conclusion": "ioi_advantage_ablation_dependent",
512	      "completed_tasks": [
513	        "IOI (GPT-2)"
514	      ],
515	      "ioi_gpt2": {
516	        "zero": {
517	          "css_1_cpr": 0.109,
518	          "best_single_cpr": 0.029,
519	          "advantage": 0.08
520	        },
521	        "mean": {
522	          "css_1_cpr": 0.095,
523	          "best_single_cpr": 0.088,
524	          "advantage": 0.007
525	        },
526	        "resample": {
527	          "css_1_cpr": 0.082,
528	          "best_single_cpr": 0.079,
529	          "advantage": 0.003
530	        }
531	      },
532	      "sva_gpt2": {
533	        "zero": {
534	          "css_1_cpr": -0.82,
535	          "best_single_cpr": -0.35,
536	          "advantage": -0.47
537	        },
538	        "mean": {
539	          "css_1_cpr": 1.173,
540	          "best_single_cpr": 1.175,
541	          "advantage": -0.002
542	        },
543	        "resample": {
544	          "css_1_cpr": 1.05,
545	          "best_single_cpr": 1.07,
546	          "advantage": -0.02
547	        }
548	      },
549	      "arithmetic_gpt2": {
550	        "zero": {
551	          "css_1_cpr": -0.184,
552	          "best_single_cpr": -0.131,
553	          "advantage": -0.053
554	        },
555	        "mean": {
556	          "css_1_cpr": 0.919,
557	          "best_single_cpr": 0.985,
558	          "advantage": -0.066
559	        },
560	        "resample": {
561	          "css_1_cpr": 0.85,
562	          "best_single_cpr": 0.92,
563	          "advantage": -0.07
564	        }
565	      },
566	      "key_finding": "IOI 的 CSS 优势从 zero (+0.080) 到 mean (+0.007) 到 resample (+0.003) 急剧衰减。Mean/resample 下的 Δ 在噪声水平内。 IOI positive result 高度依赖于 zero ablation 的破坏性偏差—— zero ablation 对 100-edge 电路的惩罚远大于 7-edge 电路。\n"
567	    },
568	    "tables": [
569	      {
570	        "caption": "Table: CSS advantage by ablation method × task",
571	        "rows": [
572	          [
573	            "Task",
574	            "Zero Δ",
575	            "Mean Δ",
576	            "Resample Δ"
577	          ],
578	          [
579	            "IOI",
580	            "+0.080",
581	            "+0.007",
582	            "+0.003"
583	          ],
584	          [
585	            "SVA",
586	            "−0.470",
587	            "−0.002",
588	            "−0.020"
589	          ],
590	          [
591	            "Arithmetic",
592	            "−0.053",
593	            "−0.066",
594	            "−0.070"
595	          ]
596	        ]
597	      }
598	    ],
599	    "figures": [],
600	    "analysis": "IOI 的 zero ablation bias 是 worst 档对 Claim 1 的第二个打击 （第一个是 ACDC isinf confound）。综合两个 confound： IOI CSS positive result = ACDC isinf extreme sparsity + zero ablation size bias。 去除任一 confound（用 top-k / 用 mean ablation），CSS 优势大幅缩水。 两个 confound 同时存在时才产生 Δ=+0.08 的 \"impressive\" 结果。 Analysis paper 中这是诚实且有价值的方法论贡献： \"Evaluation confounds in circuit faithfulness measurement\"。\n\n\nZero ablation 将 ablated edges 设为零，破坏性与 circuit size 成正比： 100 条边的 EAP-IG circuit 中有 93 条非 CSS=1.0 边被保留， 但这 93 条边在 zero ablation 下仍会因 cascade effects 被部分破坏。 相比之下 CSS=1.0 的 7 条边几乎没有 cascade loss。 这给了 CSS=1.0 一个 evaluation artifact 优势，而非 genuine faithfulness 优势。 Mean ablation 将 baseline 设为均值，大大减少了 cascade destruction， 所有方法的 CPR 趋近——CSS 优势从 0.08 缩到 0.007。 Resample ablation 进一步消除 OOD artifact，CSS 优势仅 0.003。 这意味着 IOI 的 \"strong positive result\" 是 evaluation method confound： 选不同的 ablation method 就能让 CSS 优势消失。 SVA 和 Arithmetic 在所有 ablation 下 CSS 都不优，进一步确认 IOI 是唯一正面案例且其正面性高度 fragile。\n"
601	  },
602	  {
603	    "name": "CIRCUS vs CSS Negative Ablation",
604	    "description": "D021 CIRCUS 失败数据的整理。Worst 档下 CSS 也在多数任务失败， 对比变为 \"both fail, CSS marginally less bad\"。\n",
605	    "results": {
606	      "status": "done",
607	      "conclusion": "both_methods_limited",
608	      "circus_ioi_cpr": -0.108,
609	      "circus_sva_cpr": -0.15,
610	      "circus_arithmetic_cpr": -0.12,
611	      "css_ioi_cpr": 0.109,
612	      "css_sva_cpr": -0.82,
613	      "css_arithmetic_cpr": -0.184,
614	      "circus_failure_rate": "3/3 tasks",
615	      "css_failure_rate": "2/3 tasks (only IOI positive)",
616	      "comparison_framing": "CIRCUS 在所有任务上 CPR 为负（比 random 还差）。 CSS 在 IOI 上为正但在 SVA/Arithmetic 上也为负（zero ablation）。 两种 consensus 方法在多数场景都失败——区别仅在于 CSS 在一个 特定任务上因 ACDC isinf + zero ablation 的组合而显正。\n"
617	    },
618	    "tables": [
619	      {
620	        "caption": "Table: CIRCUS vs CSS on all GPT-2 tasks (zero ablation)",
621	        "rows": [
622	          [
623	            "Method",
624	            "IOI CPR",
625	            "SVA CPR",
626	            "Arith CPR",
627	            "Tasks positive"
628	          ],
629	          [
630	            "CIRCUS",
631	            "−0.108",
632	            "−0.150",
633	            "−0.120",
634	            "0/3"
635	          ],
636	          [
637	            "CSS=1.0",
638	            "+0.109",
639	            "−0.820",
640	            "−0.184",
641	            "1/3"
642	          ],
643	          [
644	            "Best single",
645	            "+0.029",
646	            "−0.348",
647	            "−0.131",
648	            "0/3 (all neg)"
649	          ]
650	        ]
651	      }
652	    ],
653	    "figures": [],
654	    "analysis": "CIRCUS negative ablation 在 worst 档下从 \"CSS clearly better\" 变为 \"both methods severely limited\"。这仍是有效的分析贡献—— 审稿人不会因为你的方法也不好而否定你说竞品不好的论述。 在 analysis paper 中用一段说明： \"Neither structural consensus (CSS) nor within-method stability (CIRCUS) consistently identifies faithful circuits, though CSS shows advantage on IOI where methods genuinely disagree.\"\n\n\nCIRCUS 使用 threshold diversity 在单一方法内构建 consensus—— 本质是 nested sets (k=50 ⊂ k=100 ⊂ k=150) 的交集， 等价于最 conservative 的 cut。CSS 使用跨方法 binary agreement， 至少利用了方法间的信息差异。但当方法本身高度相关时（SVA, Arithmetic）， CSS 的跨方法 consensus 也退化为 single-method artifact。 IOI 是唯一例外——三方法 genuinely disagree (max Jaccard=0.31)， consensus 有意义。CIRCUS 在 IOI 上也失败是因为它只用了一种方法的 threshold sweep， 完全无法利用跨方法信息。\n"
655	  },
656	  {
657	    "name": "Jaccard-CSS Utility Correlation Analysis",
658	    "description": "汇总所有 model×task 数据点，拟合 Jaccard vs CSS advantage 关系。 Worst 档下仅有 2-3 个有效 GPT-2 数据点 + Qwen 全部 degenerate， correlation 不显著且由单个 confounded IOI 数据点驱动。\n",
659	    "results": {
660	      "status": "done",
661	      "conclusion": "not_significant_confounded",
662	      "data_points": [
663	        {
664	          "task": "IOI",
665	          "model": "GPT-2",
666	          "max_jaccard": 0.307,
667	          "css_advantage": 0.08,
668	          "confounds": "ACDC isinf + zero ablation",
669	          "quality": "confounded_positive"
670	        },
671	        {
672	          "task": "SVA",
673	          "model": "GPT-2",
674	          "max_jaccard": 0.653,
675	          "css_advantage": -0.002,
676	          "confounds": "Δ within noise (bootstrap CI includes zero)",
677	          "quality": "neutral"
678	        },
679	        {
680	          "task": "Arithmetic",
681	          "model": "GPT-2",
682	          "max_jaccard": 0.695,
683	          "css_advantage": -0.066,
684	          "confounds": null,
685	          "quality": "clear_negative"
686	        },
687	        {
688	          "task": "IOI",
689	          "model": "Qwen-0.5B",
690	          "max_jaccard": 0.042,
691	          "css_advantage": null,
692	          "confounds": "CSS=1.0 empty set — degenerate, cannot compute advantage",
693	          "quality": "degenerate"
694	        },
695	        {
696	          "task": "Arithmetic",
697	          "model": "Qwen-0.5B",
698	          "max_jaccard": 0.038,
699	          "css_advantage": null,
700	          "confounds": "CSS=1.0 empty set — degenerate",
701	          "quality": "degenerate"
702	        }
703	      ],
704	      "n_valid_data_points": 3,
705	      "n_degenerate": 2,
706	      "spearman_rho": -0.5,
707	      "spearman_p_value": 0.67,
708	      "pearson_r": -0.58,
709	      "pearson_p_value": 0.61,
710	      "note": "n=3 (excluding degenerate Qwen points)",
711	      "confound_analysis": "去除 IOI GPT-2（唯一用 ACDC isinf 且 zero ablation 的数据点）后： n=2, correlation undefined。IOI GPT-2 是 Cook's D > 5.0 的 extreme influential point，驱动了全部 negative correlation。 Qwen 数据点无法参与 regression（CSS advantage undefined when CSS=1.0 empty）。\n",
712	      "jaccard_utility_spearman_rho": -0.5,
713	      "total_task_model_points": 3,
714	      "low_jaccard_css_pass_fraction": 0.33
715	    },
716	    "tables": [
717	      {
718	        "caption": "Table: Jaccard-CSS correlation data (worst tier)",
719	        "rows": [
720	          [
721	            "Task×Model",
722	            "Max Jaccard",
723	            "CSS Advantage",
724	            "Quality",
725	            "Confounds"
726	          ],
727	          [
728	            "IOI×GPT-2",
729	            "0.307",
730	            "+0.080",
731	            "confounded",
732	            "ACDC isinf + zero ablation"
733	          ],
734	          [
735	            "SVA×GPT-2",
736	            "0.653",
737	            "−0.002",
738	            "neutral",
739	            "Δ ≈ noise"
740	          ],
741	          [
742	            "Arith×GPT-2",
743	            "0.695",
744	            "−0.066",
745	            "negative",
746	            "—"
747	          ],
748	          [
749	            "IOI×Qwen",
750	            "0.042",
751	            "undefined",
752	            "degenerate",
753	            "CSS=1.0 empty"
754	          ],
755	          [
756	            "Arith×Qwen",
757	            "0.038",
758	            "undefined",
759	            "degenerate",
760	            "CSS=1.0 empty"
761	          ]
762	        ]
763	      },
764	      {
765	        "caption": "Table: Correlation robustness analysis",
766	        "rows": [
767	          [
768	            "Analysis",
769	            "ρ",
770	            "p",
771	            "n",
772	            "Interpretation"
773	          ],
774	          [
775	            "All valid points",
776	            "−0.50",
777	            "0.67",
778	            "3",
779	            "not significant"
780	          ],
781	          [
782	            "Remove IOI (confounded)",
783	            "undefined",
784	            "—",
785	            "2",
786	            "cannot compute"
787	          ],
788	          [
789	            "Include Qwen as Δ=−0.05 proxy",
790	            "−0.30",
791	            "0.62",
792	            "5",
793	            "not significant"
794	          ]
795	        ]
796	      }
797	    ],
798	    "figures": [],
799	    "analysis": "Jaccard-utility 分析在 worst 档下从 \"primary finding\" 降级为 \"exploratory observation\"。 3 个有效点 + 2 个 degenerate 点无法支撑任何统计 claim。 Qwen 的 degenerate points 反而提供了不同的 insight： 在 extremely low Jaccard (0.04) 时 CSS 不是 \"works great\" 而是 \"completely breaks\" (empty consensus set)—— 这否定了 \"lower Jaccard → better CSS\" 的简单线性关系， 暗示存在一个 U-shaped failure mode： 太高 → methods agree, no consensus value； 太低 → methods completely disagree, no consensus possible。 这是 analysis paper 中最有趣的 reframe： \"Consensus requires a Goldilocks zone of inter-method agreement— high enough for non-empty intersection, low enough for information gain.\" 但 n=5 (3 valid + 2 degenerate) 仅能 suggest 而非 prove 这个 framework。\n\nWorst 档下有效数据仅 3 个 GPT-2 点（IOI/SVA/Arithmetic）。 Qwen 的两个点因 CSS=1.0 为空集而 degenerate——它们甚至不在 Jaccard-utility scatter plot 的定义域内（y 轴 \"CSS advantage\" 无法计算）。 这 3 个点中 IOI 是唯一正面且同时有两个 confounds (isinf + zero ablation)。 去除 IOI 后，剩余 2 个点（SVA neutral, Arithmetic negative） 无法拟合任何趋势。n=3 下 Spearman test 的 power 极低—— 即使完美 rank correlation (rho=−1.0)，p 也只有 0.17。 Jaccard-utility 关系在 worst 档下是 one-point story： IOI GPT-2 是唯一 CSS positive case，恰好也是最低 Jaccard—— 但这可能是 ACDC isinf 的 artifact 而非 causal relationship。 论文不能声称 \"Jaccard predicts CSS utility\" 作为 empirical finding， 只能提出为 \"hypothesis suggested by a single data point\"。\n"
800	  }
801	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26b70f7a-9575-4483-9af3-07e52a4c9ecc",
  "isSidechain": false,
  "promptId": "aae39cf0-5fb2-4fec-8482-5067bb253164",
  "type": "user",
  "uuid": "2a633871-8d38-49b1-a9cb-c072490653a1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"GPT-2 SVA K=3 CSS（css_1.00 重新评估）\",\n    \"description\": \"已有两次运行（mvp_sva_gpt2_k3 top-100, mvp_sva_gpt2_k3_topk top-k）。 Worst 档下 SVA re-eval 用 css_1.00 重新评估条件④，Δ(CPR) 降至 <0.005 或为负值， condition④ FAIL。D033 降级为 inconclusive 在 worst 档下进一步恶化： 多 seed bootstrap 表明 Δ=0.0127 是上界，真实均值 ≤0.003。\\n\",\n    \"results\": {\n      \"status\": \"done\",\n      \"conclusion\": \"negative\",\n      \"pairwise_jaccard\": {\n        \"eapig_x_ep\": 0.6529,\n        \"eapig_x_acdc\": 0.3158,\n        \"ep_x_acdc\": 0.4184\n      },\n      \"max_jaccard\": 0.6529,\n      \"three_way_ratio\": 0.2785,\n      \"css_distribution\": {\n        \"0.33\": 60,\n        \"0.67\": 54,\n        \"1.00\": 44\n      },\n      \"faithfulness_mean\": {\n        \"css_1.00\": {\n          \"edges\": 44,\n          \"CPR\": 1.173,\n          \"CMD\": 0.558\n        },\n        \"css_0.67\": {\n          \"edges\": 98,\n          \"CPR\": 1.1724,\n          \"CMD\": 0.503\n        },\n        \"eapig_k75\": {\n          \"edges\": 75,\n          \"CPR\": 1.1703,\n          \"CMD\": 0.53\n        },\n        \"ep_k75\": {\n          \"edges\": 75,\n          \"CPR\": 1.1703,\n          \"CMD\": 0.53\n        },\n        \"acdc_k75\": {\n          \"edges\": 75,\n          \"CPR\": 1.1746,\n          \"CMD\": 0.52\n        }\n      },\n      \"css_1.00_delta_cpr\": -0.0016,\n      \"d025_cond4_verdict\": \"FAIL (css_1.00 CPR=1.173 < acdc=1.175, Δ=−0.002)\",\n      \"bootstrap_analysis\": {\n        \"n_seeds\": 5,\n        \"delta_mean\": 0.003,\n        \"delta_95ci\": \"[-0.012, +0.019]\",\n        \"ci_includes_zero\": true\n      },\n      \"sva_gate_verdict\": \"FAIL — multi-seed bootstrap CI includes zero; D033 inconclusive confirmed as negative\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: SVA css_1.00 multi-seed bootstrap (worst tier)\",\n        \"rows\": [\n          [\n            \"Seed\",\n            \"CSS=1.0 CPR\",\n            \"ACDC CPR\",\n            \"Δ\"\n          ],\n          [\n            \"42 (original)\",\n            \"1.187\",\n            \"1.175\",\n            \"+0.013\"\n          ],\n          [\n            \"123\",\n            \"1.168\",\n            \"1.179\",\n            \"−0.011\"\n          ],\n          [\n            \"456\",\n            \"1.178\",\n            \"1.182\",\n            \"−0.004\"\n          ],\n          [\n            \"789\",\n            \"1.175\",\n            \"1.170\",\n            \"+0.005\"\n          ],\n          [\n            \"1024\",\n            \"1.171\",\n            \"1.174\",\n            \"−0.003\"\n          ],\n          [\n            \"mean ± std\",\n            \"1.176 ± 0.007\",\n            \"1.176 ± 0.005\",\n            \"+0.000 ± 0.009\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Table: SVA D025 conditions (worst tier final)\",\n        \"rows\": [\n          [\n            \"Condition\",\n            \"Result\",\n            \"Note\"\n          ],\n          [\n            \"①Jaccard<0.70\",\n            \"PASS (0.653)\",\n            \"marginal\"\n          ],\n          [\n            \"②CSS≥2/3≥10\",\n            \"PASS (54)\",\n            \"\"\n          ],\n          [\n            \"③CSS=1.0≥3\",\n            \"PASS (44)\",\n            \"\"\n          ],\n          [\n            \"④CPR dominance\",\n            \"FAIL (Δ≈0, CI includes zero)\",\n            \"D033→negative\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SVA 在 worst 档下确认为 FAIL。至此 GPT-2 三任务中仅 IOI 明确 PASS， 成功率 1/3。SVA 的 max_jaccard=0.653 过高，gradient methods 主导的 consensus 退化为 ACDC 和 gradient-pair 交集。对 Claim 2 提供了一个符合预期方向的数据点 （高 Jaccard → CSS 无优势），但 Δ≈0 无法区分 \\\"marginal positive\\\" 和 \\\"neutral\\\"， 这是 n=3-4 时 Jaccard-utility regression 的致命噪声源。\\n\\n\\nD032 报告的 Δ=0.0127 来自单一 seed（seed=42）。Worst 档假设这是随机波动上界： SVA 的 EAP-IG×EP Jaccard=0.6529 接近 Arithmetic 的 0.695， 两种 gradient 方法在 SVA number-tracking heads (layer 7-10) 上高度一致， ACDC top-k 虽然引入了名义上的 \\\"第三视角\\\"，但其在 GPT-2 12层模型上的 greedy search 仍然优先选择与 gradient saliency 高度相关的边。在 5 个 bootstrap seeds 下， css_1.00 CPR 的波动范围 [1.168, 1.192]，acdc CPR 的波动范围 [1.170, 1.182]， 两者重叠区域大——Δ 的 95% CI 横跨零点。实际观测到的 Δ=0.0127 恰好落在 CI 上界附近， 属于统计上的 \\\"lucky draw\\\"。D033 的 \\\"inconclusive\\\" 判定在 worst 档下变为明确 FAIL： 无法区分 CSS=1.0 和 ACDC 单方法。SVA 从 \\\"marginal PASS\\\" 彻底变为 FAIL。\\n\"\n  },\n  {\n    \"name\": \"GPT-2 Factual Recall K=3 CSS\",\n    \"description\": \"GPT-2 Small 上的 factual recall (国家首都)。GPT-2 Small 117M 参数 对 factual knowledge 能力极弱，circuit discovery 前提（clean baseline performance）不满足。\\n\",\n    \"results\": {\n      \"status\": \"abandoned\",\n      \"conclusion\": \"task_model_mismatch\",\n      \"partial_metrics\": {\n        \"baseline_accuracy\": 0.52,\n        \"baseline_accuracy_note\": \"几乎随机 (random=0.25, GPT-2 仅略好)\",\n        \"eapig_completed\": true,\n        \"ep_completed\": true,\n        \"acdc_completed\": false,\n        \"acdc_failure_reason\": \"GPT-2 Small 对 \\\"The capital of France is ___\\\" 类问题准确率 ~52%， clean performance 波动 ±15%。ACDC patching 在 baseline 不稳定时 无法收敛——阈值过高得空电路，过低保留全图。\\n\",\n        \"eapig_k50_cpr\": 0.02,\n        \"ep_k50_cpr\": -0.01,\n        \"cpr_note\": \"faithfulness 接近零，电路无意义\"\n      }\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"第四 GPT-2 任务失败。论文只能报告 3 个 GPT-2 tasks。 在 Limitations 说明 GPT-2 Small 对 factual recall 能力不足。 Reviewer 攻击 \\\"only 3 tasks on one tiny model\\\" 时防守空间有限。\\n\\n\\nGPT-2 Small 的 parametric knowledge 极度稀疏——factual recall 没有形成 dedicated retrieval circuit。信息分散在 residual stream 中，无法 localize。 这不是 CSS 方法论的失败，而是 task-model 根本不匹配。 ACDC 对这种 diffuse computation 最敏感：所有边的 importance 都在噪声水平。 Worst 档下这个实验浪费了 ~4 GPU hours 才确认失败，挤占了写作时间。\\n\"\n  },\n  {\n    \"name\": \"Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + ACDC top-k)\",\n    \"description\": \"D029 后用 ACDC top-k 替代 IFR。D034 已确认结果：CSS=1.0=0 边， 所有 pairwise Jaccard≈0。CSS 跨模型 scaling 根本性失败。 Worst 档下这是 paper 的致命打击——CSS 仅在 GPT-2 (32k edges) 上工作， 无法 scale 到 Qwen (179k edges)。\\n\",\n    \"results\": {\n      \"status\": \"done\",\n      \"conclusion\": \"negative\",\n      \"total_edges\": 179388,\n      \"binarization\": \"top-0.3% (~538 edges per method)\",\n      \"pairwise_jaccard\": {\n        \"eapig_x_ep\": 0.042,\n        \"eapig_x_acdc\": 0.006,\n        \"ep_x_acdc\": 0.008\n      },\n      \"max_jaccard\": 0.042,\n      \"css_distribution\": {\n        \"1/3\": 1058,\n        \"2/3\": 66,\n        \"3/3\": 0\n      },\n      \"css_core_3of3\": 0,\n      \"faithfulness_mean\": {\n        \"css_0.67\": {\n          \"edges\": 66,\n          \"CPR\": 0.031,\n          \"CMD\": 0.972\n        },\n        \"eapig_top538\": {\n          \"edges\": 538,\n          \"CPR\": 0.055,\n          \"CMD\": 0.948\n        },\n        \"ep_top538\": {\n          \"edges\": 538,\n          \"CPR\": 0.048,\n          \"CMD\": 0.955\n        },\n        \"acdc_top538\": {\n          \"edges\": 538,\n          \"CPR\": 0.029,\n          \"CMD\": 0.974\n        }\n      },\n      \"d025_verdict\": \"FAIL — CSS=1.0 = empty set\",\n      \"ifr_version_comparison\": {\n        \"ifr_jaccard_eapig\": 0.0,\n        \"ifr_jaccard_ep\": 0.0,\n        \"acdc_jaccard_eapig\": 0.006,\n        \"acdc_jaccard_ep\": 0.008,\n        \"note\": \"ACDC 比 IFR 稍好但仍实质为零——问题不在方法选择而在模型规模\"\n      },\n      \"scaling_analysis\": {\n        \"gpt2_edge_space\": 32491,\n        \"qwen_edge_space\": 179388,\n        \"ratio\": 5.52,\n        \"gpt2_topk_pct\": 0.31,\n        \"qwen_topk_pct\": 0.3,\n        \"gpt2_max_jaccard\": 0.307,\n        \"qwen_max_jaccard\": 0.042,\n        \"jaccard_ratio\": 7.3,\n        \"conclusion\": \"相同比例的 top-k 在更大 edge space 中产生更低 Jaccard，这是组合稀释效应\"\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: GPT-2 vs Qwen edge space scaling\",\n        \"rows\": [\n          [\n            \"\",\n            \"GPT-2 Small\",\n            \"Qwen-2.5 0.5B\",\n            \"Ratio\"\n          ],\n          [\n            \"Total edges\",\n            \"32,491\",\n            \"179,388\",\n            \"5.5×\"\n          ],\n          [\n            \"Top-k (0.3%)\",\n            \"~100\",\n            \"~538\",\n            \"5.4×\"\n          ],\n          [\n            \"Max Jaccard (EAP-IG×EP)\",\n            \"0.307\",\n            \"0.042\",\n            \"7.3×↓\"\n          ],\n          [\n            \"CSS=1.0 edges\",\n            \"7\",\n            \"0\",\n            \"—\"\n          ],\n          [\n            \"CSS=1.0 CPR\",\n            \"0.109\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Table: Qwen IOI method comparison — IFR vs ACDC (both fail)\",\n        \"rows\": [\n          [\n            \"Third method\",\n            \"J(×EAP-IG)\",\n            \"J(×EP)\",\n            \"CSS=1.0\"\n          ],\n          [\n            \"IFR (D028)\",\n            \"0.000\",\n            \"0.000\",\n            \"0 edges\"\n          ],\n          [\n            \"ACDC (D034)\",\n            \"0.006\",\n            \"0.008\",\n            \"0 edges\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"D034 是 worst 档的核心证据之一。CSS 跨模型 scaling 的结构性失败 意味着论文不能 claim \\\"CSS generalizes across models\\\"。 在 analysis paper 中重构为：\\\"CSS 的 edge-level consensus 依赖于 methods 在相同 edge space 中有 meaningful overlap， 这一前提在 model scale up 时因组合稀释而系统性地被违反。\\\" 这是一个有价值的 negative finding，但将 CSS 定位为 \\\"仅适用于小模型\\\" 的方法。\\n\\n\\nD034 已确认：ACDC 在 179k-edge Qwen 图上退化为 node-level scoring， 与 IFR 的 block-voting 问题本质相同。核心机制是组合稀释： top-0.3% 在 32k 边的 GPT-2 上选约 100 条边，方法间有 meaningful overlap； 在 179k 边的 Qwen 上选约 538 条边，但 edge space 增大 5.5×， 而 circuit structure 并非线性 scale——IOI circuit 在 Qwen 上分散到更多层/头， 方法各自 \\\"看到\\\" 不同子集。EAP-IG×EP Jaccard 从 GPT-2 的 0.31 暴跌至 0.04， ACDC 与任何方法几乎零重叠。CSS=1.0 要求三方法全部同意——在 Jaccard≈0 时 这是空集。即使放宽到 CSS≥0.67，也只有 66 条边，CPR=0.031 远低于单方法。 这证明 CSS 的前提（方法对同一 edge 有 meaningful overlap）在大模型上不成立。\\n\"\n  },\n  {\n    \"name\": \"Qwen-2.5 0.5B Arithmetic K=3 (EAP-IG + EP + ACDC top-k)\",\n    \"description\": \"基于 D034 的结果，Qwen Arithmetic 预期与 Qwen IOI 相同模式： ACDC 在大 edge space 上退化，CSS=1.0 为空集或退化。\\n\",\n    \"results\": {\n      \"status\": \"planned\",\n      \"conclusion\": \"negative\",\n      \"total_edges\": \"~179000\",\n      \"pairwise_jaccard\": {\n        \"eapig_x_ep\": 0.038,\n        \"eapig_x_acdc\": 0.004,\n        \"ep_x_acdc\": 0.005\n      },\n      \"max_jaccard\": 0.038,\n      \"css_distribution\": {\n        \"1/3\": \"~1080\",\n        \"2/3\": \"~55\",\n        \"3/3\": 0\n      },\n      \"css_core_3of3\": 0,\n      \"faithfulness_mean\": {\n        \"css_0.67\": {\n          \"edges\": \"~55\",\n          \"CPR\": 0.025,\n          \"CMD\": 0.978\n        },\n        \"eapig_top538\": {\n          \"edges\": 538,\n          \"CPR\": 0.049,\n          \"CMD\": 0.954\n        }\n      },\n      \"d025_verdict\": \"FAIL — CSS=1.0 = empty set, same as Qwen IOI\",\n      \"qwen_ioi_css10_cpr_vs_best\": null,\n      \"note\": \"CSS=1.0 为空集，无法计算 CPR vs best single\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Qwen tasks — all fail with same pattern\",\n        \"rows\": [\n          [\n            \"Task\",\n            \"CSS=1.0 edges\",\n            \"Max Jaccard\",\n            \"Verdict\"\n          ],\n          [\n            \"IOI (IFR)\",\n            \"0\",\n            \"0.000\",\n            \"FAIL\"\n          ],\n          [\n            \"IOI (ACDC)\",\n            \"0\",\n            \"0.042\",\n            \"FAIL\"\n          ],\n          [\n            \"Arithmetic (ACDC, predicted)\",\n            \"0\",\n            \"~0.038\",\n            \"FAIL\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen Arithmetic 是 sunk cost。D034 已证明问题是结构性的（edge space scaling）， 不因任务而异。在 analysis paper 中只需一句： \\\"We verified the scaling failure extends to Arithmetic (Table X)\\\"。 不值得单独的 figure 或 detailed analysis。\\n\\n\\nQwen IOI (D034) 已证明 ACDC 在 179k-edge graph 上退化。 Arithmetic 在 Qwen 上的 edge space 与 IOI 几乎相同（同一模型）， EAP-IG×EP 的 Jaccard 预期更低（Arithmetic 在更大模型上更分散）， ACDC 的退化模式完全相同（node-level scoring）。 这个实验本质上是 Qwen IOI 的重复，不产生新信息。 Worst 档建议：如果 Qwen IOI 已 FAIL，跳过 Qwen Arithmetic 以节省时间。\\n\"\n  },\n  {\n    \"name\": \"Gemma-2 2B IOI K=3\",\n    \"description\": \"Scale 到 2B 模型。Worst 档下 Qwen 0.5B 已完全失败， Gemma-2 2B 的 edge space 更大（~500k+），失败是确定性的。\\n\",\n    \"results\": {\n      \"status\": \"not_attempted\",\n      \"conclusion\": null,\n      \"predicted_outcome\": \"FAIL — edge space ~500k+, Jaccard→0, CSS=1.0→empty set\",\n      \"reason_not_attempted\": \"D034 已证明 CSS 在 179k-edge Qwen 上失败。Gemma-2 2B 有 26 层 16 头， edge space 估计 >500k，组合稀释效应更严重。 投入 ~16 GPU-hours 仅为确认一个已知结论不合理。\\n\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"明确建议取消。节省 16 GPU-hours 和 2 天调试时间用于论文写作。 在 paper 中用 back-of-envelope 计算替代实验： \\\"At Gemma-2 2B scale (~500k edges), top-0.3% binarization yields ~1500 edges per method; extrapolating from GPT-2→Qwen Jaccard decay (0.31→0.04), expected max Jaccard ≈ 0.01, rendering consensus trivially empty.\\\"\\n\\n\\nGemma-2 2B 的 edge space 是 Qwen 的 ~3×，Qwen 上已观察到 Jaccard→0。 在更大 edge space 中，top-0.3% 选约 1500+ 条边，但三种方法各自 \\\"看到\\\" 的功能通路更加分散——26 层中 IOI 信息流经更多 intermediate heads。 CSS 的 edge-level consensus 前提在此彻底不成立。 这个实验的唯一价值是确认 \\\"scaling law\\\"，但 GPT-2 → Qwen 的两个数据点 已足够支撑 analysis paper 的论点。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1 8B IOI K=3\",\n    \"description\": \"最大规模实验。Worst 档下无论如何都不应运行。\\n\",\n    \"results\": {\n      \"status\": \"not_attempted\",\n      \"conclusion\": null,\n      \"predicted_outcome\": \"FAIL — edge space ~2M+, hardware insufficient (needs A100 80GB)\",\n      \"reason_not_attempted\": \"P3 priority + hardware barrier (RTX 4090D 24GB insufficient for EP) + D034 已证明 scaling failure\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"明确取消。在 Future Work 中一句带过即可。\\n\\n\\n8B 模型有 32 层 32 头，edge space 估计 ~2M。 top-0.3% ≈ 6000 条边/方法，但 pairwise Jaccard 在如此巨大的空间中 趋近于 random intersection baseline (~0.003)。 EP 在 8B 上需要 A100 80GB（edge-level pruning 内存超线性增长）， 当前 RTX 4090D 24GB 完全不够。即使有硬件，ROI 为负。\\n\"\n  },\n  {\n    \"name\": \"Top-k Binarization Sensitivity Sweep\",\n    \"description\": \"系统性 top-k sweep (k=50, 75, 100, 150) 在 GPT-2 tasks 上。 Worst 档下 CSS CPR 对 k 稳定——但这只证明 CSS 是 \\\"consistently mediocre\\\"， 优势永远不超过 single method（IOI 除外）。 关键发现：ACDC isinf-vs-topk 的 Jaccard 差异驱动了虚假的 Jaccard-utility 关联。\\n\",\n    \"results\": {\n      \"status\": \"done\",\n      \"conclusion\": \"stable_but_irrelevant\",\n      \"ioi_gpt2_css_cpr_by_k\": {\n        \"k50\": 0.109,\n        \"k75\": 0.102,\n        \"k100\": 0.095,\n        \"k150\": 0.088\n      },\n      \"sva_gpt2_css_cpr_by_k\": {\n        \"k50\": -0.82,\n        \"k75\": -0.82,\n        \"k100\": -0.74,\n        \"k150\": -0.71\n      },\n      \"arithmetic_gpt2_css_cpr_by_k\": {\n        \"k50\": 0.919,\n        \"k75\": 0.919,\n        \"k100\": 0.926,\n        \"k150\": 0.933\n      },\n      \"sva_mean_css_cpr_by_k\": {\n        \"k50\": 1.185,\n        \"k75\": 1.187,\n        \"k100\": 1.174,\n        \"k150\": 1.168\n      },\n      \"css_stable_across_k\": true,\n      \"but_advantage_never_positive_except_ioi\": true,\n      \"key_finding\": \"CSS CPR 在 k=50-150 内稳定 (std<0.02)，但这只说明 binarization 不是 CSS 失败的原因—— 方法相关性才是。CSS 在 SVA 和 Arithmetic 上 never beats single method， 无论 k 取什么值。\\n\",\n      \"acdc_isinf_vs_topk_jaccard_gap\": {\n        \"ioi\": \"isinf J=0.09 → topk J=0.25 (Δ=+0.16)\",\n        \"arithmetic\": \"isinf J=0.17 → topk J=0.42 (Δ=+0.25)\",\n        \"sva\": \"isinf J=0.37 → topk J=0.37 (Δ=0, already topk)\"\n      },\n      \"confound_implication\": \"IOI 的 \\\"low Jaccard → CSS works\\\" 部分由 ACDC isinf 的极端 sparsity (14 edges) 驱动。 ACDC isinf 人为压低了 ACDC×EAP-IG 和 ACDC×EP 的 Jaccard。 top-k 归一化后 IOI max Jaccard 从 0.31 上升到约 0.41 (EAP-IG×EP pair 不变， 但 ACDC pair 上升)。Jaccard-utility 关系中 IOI 的 \\\"low Jaccard\\\" 被 ACDC binarization inflated。\\n\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: CSS=1.0 CPR across k values (GPT-2 tasks, zero ablation for IOI, mean for others)\",\n        \"rows\": [\n          [\n            \"Task\",\n            \"k=50\",\n            \"k=75\",\n            \"k=100\",\n            \"k=150\",\n            \"Stable?\",\n            \"Beats single?\"\n          ],\n          [\n            \"IOI (zero)\",\n            \"0.109\",\n            \"0.102\",\n            \"0.095\",\n            \"0.088\",\n            \"Yes\",\n            \"Yes (all k)\"\n          ],\n          [\n            \"SVA (mean)\",\n            \"1.185\",\n            \"1.187\",\n            \"1.174\",\n            \"1.168\",\n            \"Yes\",\n            \"No (all k)\"\n          ],\n          [\n            \"Arith (mean)\",\n            \"0.919\",\n            \"0.919\",\n            \"0.926\",\n            \"0.933\",\n            \"Yes\",\n            \"No (all k)\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Table: ACDC binarization effect on Jaccard\",\n        \"rows\": [\n          [\n            \"Task\",\n            \"J (isinf)\",\n            \"J (top-k)\",\n            \"Δ\",\n            \"CSS outcome changes?\"\n          ],\n          [\n            \"IOI\",\n            \"0.09\",\n            \"0.25\",\n            \"+0.16\",\n            \"No (still PASS)\"\n          ],\n          [\n            \"Arithmetic\",\n            \"0.17\",\n            \"0.42\",\n            \"+0.25\",\n            \"No (still FAIL)\"\n          ],\n          [\n            \"SVA\",\n            \"0.37 (already topk)\",\n            \"0.37\",\n            \"0\",\n            \"N/A\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Binarization sensitivity 是 worst 档下最有分析价值的实验之一。 两个结论：(1) CSS 对 k 稳定——方法论上 clean； (2) Jaccard-utility 关系的一部分方差由 ACDC binarization 解释， 而非 genuine method diversity。 这为 analysis paper 提供了 \\\"binarization pathology taxonomy\\\" 贡献 （Claim 3 延伸），也是 \\\"why consensus fails\\\" 叙事的技术核心。\\n\\n\\nTop-k 归一化使三种方法在 comparable edge budget 下比较，消除了 ACDC isinf 的 extreme sparsity artifact。k 越大，pairwise overlap 自然增加， CSS=1.0 集合扩大但新增的边是 low-confidence coincidental consensus。 IOI 在所有 k 下仍为正面是因为其 14 条核心 ACDC isinf 边（全被三方法确认） 质量极高——但这是 IOI 任务 + GPT-2 模型的特异性，非方法优势。 ACDC isinf-vs-topk Jaccard 差异是 worst 档 Jaccard-utility confound 的核心： 在 isinf 下 ACDC 只有 14-17 条边，与 100 条边的 EAP-IG/EP 的 Jaccard 自然极低； top-k 归一化后差异缩小，但 IOI 的正面结果不变—— 这说明 IOI 的 CSS 优势与 Jaccard level 关系弱于预期。\\n\"\n  },\n  {\n    \"name\": \"Ablation Method Comparison (Zero vs Mean vs Resample)\",\n    \"description\": \"在 IOI 上比较 zero/mean/resample ablation 下 CSS 优势。 Worst 档揭示 IOI positive result 部分由 zero ablation bias 驱动。\\n\",\n    \"results\": {\n      \"status\": \"partial\",\n      \"conclusion\": \"ioi_advantage_ablation_dependent\",\n      \"completed_tasks\": [\n        \"IOI (GPT-2)\"\n      ],\n      \"ioi_gpt2\": {\n        \"zero\": {\n          \"css_1_cpr\": 0.109,\n          \"best_single_cpr\": 0.029,\n          \"advantage\": 0.08\n        },\n        \"mean\": {\n          \"css_1_cpr\": 0.095,\n          \"best_single_cpr\": 0.088,\n          \"advantage\": 0.007\n        },\n        \"resample\": {\n          \"css_1_cpr\": 0.082,\n          \"best_single_cpr\": 0.079,\n          \"advantage\": 0.003\n        }\n      },\n      \"sva_gpt2\": {\n        \"zero\": {\n          \"css_1_cpr\": -0.82,\n          \"best_single_cpr\": -0.35,\n          \"advantage\": -0.47\n        },\n        \"mean\": {\n          \"css_1_cpr\": 1.173,\n          \"best_single_cpr\": 1.175,\n          \"advantage\": -0.002\n        },\n        \"resample\": {\n          \"css_1_cpr\": 1.05,\n          \"best_single_cpr\": 1.07,\n          \"advantage\": -0.02\n        }\n      },\n      \"arithmetic_gpt2\": {\n        \"zero\": {\n          \"css_1_cpr\": -0.184,\n          \"best_single_cpr\": -0.131,\n          \"advantage\": -0.053\n        },\n        \"mean\": {\n          \"css_1_cpr\": 0.919,\n          \"best_single_cpr\": 0.985,\n          \"advantage\": -0.066\n        },\n        \"resample\": {\n          \"css_1_cpr\": 0.85,\n          \"best_single_cpr\": 0.92,\n          \"advantage\": -0.07\n        }\n      },\n      \"key_finding\": \"IOI 的 CSS 优势从 zero (+0.080) 到 mean (+0.007) 到 resample (+0.003) 急剧衰减。Mean/resample 下的 Δ 在噪声水平内。 IOI positive result 高度依赖于 zero ablation 的破坏性偏差—— zero ablation 对 100-edge 电路的惩罚远大于 7-edge 电路。\\n\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: CSS advantage by ablation method × task\",\n        \"rows\": [\n          [\n            \"Task\",\n            \"Zero Δ\",\n            \"Mean Δ\",\n            \"Resample Δ\"\n          ],\n          [\n            \"IOI\",\n            \"+0.080\",\n            \"+0.007\",\n            \"+0.003\"\n          ],\n          [\n            \"SVA\",\n            \"−0.470\",\n            \"−0.002\",\n            \"−0.020\"\n          ],\n          [\n            \"Arithmetic\",\n            \"−0.053\",\n            \"−0.066\",\n            \"−0.070\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"IOI 的 zero ablation bias 是 worst 档对 Claim 1 的第二个打击 （第一个是 ACDC isinf confound）。综合两个 confound： IOI CSS positive result = ACDC isinf extreme sparsity + zero ablation size bias。 去除任一 confound（用 top-k / 用 mean ablation），CSS 优势大幅缩水。 两个 confound 同时存在时才产生 Δ=+0.08 的 \\\"impressive\\\" 结果。 Analysis paper 中这是诚实且有价值的方法论贡献： \\\"Evaluation confounds in circuit faithfulness measurement\\\"。\\n\\n\\nZero ablation 将 ablated edges 设为零，破坏性与 circuit size 成正比： 100 条边的 EAP-IG circuit 中有 93 条非 CSS=1.0 边被保留， 但这 93 条边在 zero ablation 下仍会因 cascade effects 被部分破坏。 相比之下 CSS=1.0 的 7 条边几乎没有 cascade loss。 这给了 CSS=1.0 一个 evaluation artifact 优势，而非 genuine faithfulness 优势。 Mean ablation 将 baseline 设为均值，大大减少了 cascade destruction， 所有方法的 CPR 趋近——CSS 优势从 0.08 缩到 0.007。 Resample ablation 进一步消除 OOD artifact，CSS 优势仅 0.003。 这意味着 IOI 的 \\\"strong positive result\\\" 是 evaluation method confound： 选不同的 ablation method 就能让 CSS 优势消失。 SVA 和 Arithmetic 在所有 ablation 下 CSS 都不优，进一步确认 IOI 是唯一正面案例且其正面性高度 fragile。\\n\"\n  },\n  {\n    \"name\": \"CIRCUS vs CSS Negative Ablation\",\n    \"description\": \"D021 CIRCUS 失败数据的整理。Worst 档下 CSS 也在多数任务失败， 对比变为 \\\"both fail, CSS marginally less bad\\\"。\\n\",\n    \"results\": {\n      \"status\": \"done\",\n      \"conclusion\": \"both_methods_limited\",\n      \"circus_ioi_cpr\": -0.108,\n      \"circus_sva_cpr\": -0.15,\n      \"circus_arithmetic_cpr\": -0.12,\n      \"css_ioi_cpr\": 0.109,\n      \"css_sva_cpr\": -0.82,\n      \"css_arithmetic_cpr\": -0.184,\n      \"circus_failure_rate\": \"3/3 tasks\",\n      \"css_failure_rate\": \"2/3 tasks (only IOI positive)\",\n      \"comparison_framing\": \"CIRCUS 在所有任务上 CPR 为负（比 random 还差）。 CSS 在 IOI 上为正但在 SVA/Arithmetic 上也为负（zero ablation）。 两种 consensus 方法在多数场景都失败——区别仅在于 CSS 在一个 特定任务上因 ACDC isinf + zero ablation 的组合而显正。\\n\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: CIRCUS vs CSS on all GPT-2 tasks (zero ablation)\",\n        \"rows\": [\n          [\n            \"Method\",\n            \"IOI CPR\",\n            \"SVA CPR\",\n            \"Arith CPR\",\n            \"Tasks positive\"\n          ],\n          [\n            \"CIRCUS\",\n            \"−0.108\",\n            \"−0.150\",\n            \"−0.120\",\n            \"0/3\"\n          ],\n          [\n            \"CSS=1.0\",\n            \"+0.109\",\n            \"−0.820\",\n            \"−0.184\",\n            \"1/3\"\n          ],\n          [\n            \"Best single\",\n            \"+0.029\",\n            \"−0.348\",\n            \"−0.131\",\n            \"0/3 (all neg)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CIRCUS negative ablation 在 worst 档下从 \\\"CSS clearly better\\\" 变为 \\\"both methods severely limited\\\"。这仍是有效的分析贡献—— 审稿人不会因为你的方法也不好而否定你说竞品不好的论述。 在 analysis paper 中用一段说明： \\\"Neither structural consensus (CSS) nor within-method stability (CIRCUS) consistently identifies faithful circuits, though CSS shows advantage on IOI where methods genuinely disagree.\\\"\\n\\n\\nCIRCUS 使用 threshold diversity 在单一方法内构建 consensus—— 本质是 nested sets (k=50 ⊂ k=100 ⊂ k=150) 的交集， 等价于最 conservative 的 cut。CSS 使用跨方法 binary agreement， 至少利用了方法间的信息差异。但当方法本身高度相关时（SVA, Arithmetic）， CSS 的跨方法 consensus 也退化为 single-method artifact。 IOI 是唯一例外——三方法 genuinely disagree (max Jaccard=0.31)， consensus 有意义。CIRCUS 在 IOI 上也失败是因为它只用了一种方法的 threshold sweep， 完全无法利用跨方法信息。\\n\"\n  },\n  {\n    \"name\": \"Jaccard-CSS Utility Correlation Analysis\",\n    \"description\": \"汇总所有 model×task 数据点，拟合 Jaccard vs CSS advantage 关系。 Worst 档下仅有 2-3 个有效 GPT-2 数据点 + Qwen 全部 degenerate， correlation 不显著且由单个 confounded IOI 数据点驱动。\\n\",\n    \"results\": {\n      \"status\": \"done\",\n      \"conclusion\": \"not_significant_confounded\",\n      \"data_points\": [\n        {\n          \"task\": \"IOI\",\n          \"model\": \"GPT-2\",\n          \"max_jaccard\": 0.307,\n          \"css_advantage\": 0.08,\n          \"confounds\": \"ACDC isinf + zero ablation\",\n          \"quality\": \"confounded_positive\"\n        },\n        {\n          \"task\": \"SVA\",\n          \"model\": \"GPT-2\",\n          \"max_jaccard\": 0.653,\n          \"css_advantage\": -0.002,\n          \"confounds\": \"Δ within noise (bootstrap CI includes zero)\",\n          \"quality\": \"neutral\"\n        },\n        {\n          \"task\": \"Arithmetic\",\n          \"model\": \"GPT-2\",\n          \"max_jaccard\": 0.695,\n          \"css_advantage\": -0.066,\n          \"confounds\": null,\n          \"quality\": \"clear_negative\"\n        },\n        {\n          \"task\": \"IOI\",\n          \"model\": \"Qwen-0.5B\",\n          \"max_jaccard\": 0.042,\n          \"css_advantage\": null,\n          \"confounds\": \"CSS=1.0 empty set — degenerate, cannot compute advantage\",\n          \"quality\": \"degenerate\"\n        },\n        {\n          \"task\": \"Arithmetic\",\n          \"model\": \"Qwen-0.5B\",\n          \"max_jaccard\": 0.038,\n          \"css_advantage\": null,\n          \"confounds\": \"CSS=1.0 empty set — degenerate\",\n          \"quality\": \"degenerate\"\n        }\n      ],\n      \"n_valid_data_points\": 3,\n      \"n_degenerate\": 2,\n      \"spearman_rho\": -0.5,\n      \"spearman_p_value\": 0.67,\n      \"pearson_r\": -0.58,\n      \"pearson_p_value\": 0.61,\n      \"note\": \"n=3 (excluding degenerate Qwen points)\",\n      \"confound_analysis\": \"去除 IOI GPT-2（唯一用 ACDC isinf 且 zero ablation 的数据点）后： n=2, correlation undefined。IOI GPT-2 是 Cook's D > 5.0 的 extreme influential point，驱动了全部 negative correlation。 Qwen 数据点无法参与 regression（CSS advantage undefined when CSS=1.0 empty）。\\n\",\n      \"jaccard_utility_spearman_rho\": -0.5,\n      \"total_task_model_points\": 3,\n      \"low_jaccard_css_pass_fraction\": 0.33\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Jaccard-CSS correlation data (worst tier)\",\n        \"rows\": [\n          [\n            \"Task×Model\",\n            \"Max Jaccard\",\n            \"CSS Advantage\",\n            \"Quality\",\n            \"Confounds\"\n          ],\n          [\n            \"IOI×GPT-2\",\n            \"0.307\",\n            \"+0.080\",\n            \"confounded\",\n            \"ACDC isinf + zero ablation\"\n          ],\n          [\n            \"SVA×GPT-2\",\n            \"0.653\",\n            \"−0.002\",\n            \"neutral\",\n            \"Δ ≈ noise\"\n          ],\n          [\n            \"Arith×GPT-2\",\n            \"0.695\",\n            \"−0.066\",\n            \"negative\",\n            \"—\"\n          ],\n          [\n            \"IOI×Qwen\",\n            \"0.042\",\n            \"undefined\",\n            \"degenerate\",\n            \"CSS=1.0 empty\"\n          ],\n          [\n            \"Arith×Qwen\",\n            \"0.038\",\n            \"undefined\",\n            \"degenerate\",\n            \"CSS=1.0 empty\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Table: Correlation robustness analysis\",\n        \"rows\": [\n          [\n            \"Analysis\",\n            \"ρ\",\n            \"p\",\n            \"n\",\n            \"Interpretation\"\n          ],\n          [\n            \"All valid points\",\n            \"−0.50\",\n            \"0.67\",\n            \"3\",\n            \"not significant\"\n          ],\n          [\n            \"Remove IOI (confounded)\",\n            \"undefined\",\n            \"—\",\n            \"2\",\n            \"cannot compute\"\n          ],\n          [\n            \"Include Qwen as Δ=−0.05 proxy\",\n            \"−0.30\",\n            \"0.62\",\n            \"5\",\n            \"not significant\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Jaccard-utility 分析在 worst 档下从 \\\"primary finding\\\" 降级为 \\\"exploratory observation\\\"。 3 个有效点 + 2 个 degenerate 点无法支撑任何统计 claim。 Qwen 的 degenerate points 反而提供了不同的 insight： 在 extremely low Jaccard (0.04) 时 CSS 不是 \\\"works great\\\" 而是 \\\"completely breaks\\\" (empty consensus set)—— 这否定了 \\\"lower Jaccard → better CSS\\\" 的简单线性关系， 暗示存在一个 U-shaped failure mode： 太高 → methods agree, no consensus value； 太低 → methods completely disagree, no consensus possible。 这是 analysis paper 中最有趣的 reframe： \\\"Consensus requires a Goldilocks zone of inter-method agreement— high enough for non-empty intersection, low enough for information gain.\\\" 但 n=5 (3 valid + 2 degenerate) 仅能 suggest 而非 prove 这个 framework。\\n\\nWorst 档下有效数据仅 3 个 GPT-2 点（IOI/SVA/Arithmetic）。 Qwen 的两个点因 CSS=1.0 为空集而 degenerate——它们甚至不在 Jaccard-utility scatter plot 的定义域内（y 轴 \\\"CSS advantage\\\" 无法计算）。 这 3 个点中 IOI 是唯一正面且同时有两个 confounds (isinf + zero ablation)。 去除 IOI 后，剩余 2 个点（SVA neutral, Arithmetic negative） 无法拟合任何趋势。n=3 下 Spearman test 的 power 极低—— 即使完美 rank correlation (rho=−1.0)，p 也只有 0.17。 Jaccard-utility 关系在 worst 档下是 one-point story： IOI GPT-2 是唯一 CSS positive case，恰好也是最低 Jaccard—— 但这可能是 ACDC isinf 的 artifact 而非 causal relationship。 论文不能声称 \\\"Jaccard predicts CSS utility\\\" 作为 empirical finding， 只能提出为 \\\"hypothesis suggested by a single data point\\\"。\\n\"\n  }\n]",
      "numLines": 801,
      "startLine": 1,
      "totalLines": 801
    }
  },
  "sourceToolAssistantUUID": "26b70f7a-9575-4483-9af3-07e52a4c9ecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T081242 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-contex…",
  "leafUuid": "2a633871-8d38-49b1-a9cb-c072490653a1",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulation paper for dream_id",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4"
}
```

---

### Assistant

_source line 14 · 2026-05-13T08:54:58.112Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the data and framing. Let me write the LaTeX paper. The narrative guidance says:

- Method paper 不可行，必须 pivot 为 analysis paper
- 新叙事："Why Cross-Method Circuit Consensus Fails: An Empirical Analysis"
- 核心贡献变为：
  1. 揭示 circuit discovery 方法在多数任务上高度相关或互补性不足，binary consensus 的前提（独立证据源）在实践中很少满足
  2. ACDC isinf binarization 问题的系统性分析（Claim 3，已强支撑）
  3. CSS 跨模型 scaling 的结构性失败——在大规模图上所有方法的 Jaccard 相似度趋近于零
  4. 重新定位 Jaccard 作为诊断工具，用来解释方法失败而非预测成功

IOI 和 GPT-2 的案例研究成为唯一有效的例外，而不是推广的基础。投稿目标调整为 EMNLP Findings 或 workshop paper。

现在我需要整理所有实验的完整覆盖范围：GPT-2 上的 SVA 和 Factual Recall 任务、Qwen-2.5 0.5B 在 IOI 和 Arithmetic 上的结果、Gemma-2 和 Llama-3.1 的预测失败情况，加上 top-k 二值化敏感性扫描和各种方法的消融对比。

还要分析 CIRCUS 与 CSS 的负向消融以及 Jaccard-CSS 效用相关性。现在开始生成 LaTeX 论文。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a633871-8d38-49b1-a9cb-c072490653a1",
  "isSidechain": false,
  "requestId": "req_011CazHbgEU1Gffxyu4wTSxf",
  "type": "assistant",
  "uuid": "ede045cc-44d2-4700-9fec-dd81e6bc6a30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWwgNu58AjRGXafKaPf3kN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1258,
      "cache_creation_input_tokens": 14181,
      "cache_read_input_tokens": 23147,
      "output_tokens": 716,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14181,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1258,
          "output_tokens": 716,
          "cache_read_input_tokens": 23147,
          "cache_creation_input_tokens": 14181,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14181
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

_source line 15 · 2026-05-13T08:54:58.116Z_

Now I have all the data. Let me write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ede045cc-44d2-4700-9fec-dd81e6bc6a30",
  "isSidechain": false,
  "requestId": "req_011CazHbgEU1Gffxyu4wTSxf",
  "type": "assistant",
  "uuid": "e929b7f8-52dd-449b-bda1-48a6fb926054",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWwgNu58AjRGXafKaPf3kN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1258,
      "cache_creation_input_tokens": 14181,
      "cache_read_input_tokens": 23147,
      "output_tokens": 716,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14181,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1258,
          "output_tokens": 716,
          "cache_read_input_tokens": 23147,
          "cache_creation_input_tokens": 14181,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14181
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

_source line 16 · 2026-05-13T08:54:59.659Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016kNjcsEQ6A2hbgZWRAUZr5`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/",
  "description": "Check output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e929b7f8-52dd-449b-bda1-48a6fb926054",
  "isSidechain": false,
  "requestId": "req_011CazHbgEU1Gffxyu4wTSxf",
  "type": "assistant",
  "uuid": "f15b8200-b782-48e4-9681-33dc854bd9e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWwgNu58AjRGXafKaPf3kN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1258,
      "cache_creation_input_tokens": 14181,
      "cache_read_input_tokens": 23147,
      "output_tokens": 716,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14181,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1258,
          "output_tokens": 716,
          "cache_read_input_tokens": 23147,
          "cache_creation_input_tokens": 14181,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14181
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

_source line 17 · 2026-05-13T08:54:59.821Z_

<details><summary>↩ Tool result · `toolu_016kNjcsEQ6A2hbgZWRAUZr5`</summary>

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
  "parentUuid": "f15b8200-b782-48e4-9681-33dc854bd9e4",
  "isSidechain": false,
  "promptId": "aae39cf0-5fb2-4fec-8482-5067bb253164",
  "type": "user",
  "uuid": "71d0299b-2345-445b-a2c3-ad68fb8f7c3b",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f15b8200-b782-48e4-9681-33dc854bd9e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-13T08:58:07.276Z_

<details open><summary>🔧 Tool call — Write · `toolu_016BfQmkevwGV6yuXQwwPwmN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{microtype}\n\n\\newcommand{\\css}{\\textsc{CSS}}\n\\newcommand{\\circus}{\\textsc{Circus}}\n\\newcommand{\\eapig}{\\textsc{EAP-IG}}\n\\newcommand{\\ep}{\\textsc{EP}}\n\\newcommand{\\acdc}{\\textsc{ACDC}}\n\\newcommand{\\cpr}{\\text{CPR}}\n\\newcommand{\\cmd}{\\text{CMD}}\n\n\\title{Why Cross-Method Circuit Consensus Fails:\\\\An Empirical Analysis}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nCircuit discovery methods---such as Edge Attribution Patching (\\eapig{}), Edge Pruning (\\ep{}), and Automated Circuit Discovery (\\acdc{})---aim to identify minimal subgraphs that faithfully explain model behavior. A natural hypothesis is that \\emph{consensus} across independently derived circuits should yield higher-quality, more faithful subgraphs.\nWe systematically evaluate this hypothesis through \\emph{Cross-method Structural consensus Scoring} (\\css{}), a binary consensus framework applied to $K \\ge 3$ circuit discovery methods across multiple tasks and models.\nOur findings are predominantly negative.\nOn GPT-2 Small, \\css{} produces a faithful consensus circuit only on Indirect Object Identification (IOI), while failing on Subject--Verb Agreement (SVA) and Arithmetic---a 1/3 success rate.\nMoreover, the sole positive result is confounded by two evaluation artifacts: \\acdc{}'s \\texttt{isinf} binarization and zero-ablation size bias.\nOn Qwen-2.5 0.5B (179k edges), all methods exhibit near-zero pairwise overlap (Jaccard $\\approx 0.04$), rendering consensus trivially empty.\nWe identify three structural causes of failure: (1) high inter-method correlation on most tasks eliminates the independent-evidence premise of consensus; (2) \\acdc{} binarization pathologies inflate apparent method diversity; and (3) combinatorial dilution in larger edge spaces systematically destroys cross-method overlap.\nThese results suggest that binary circuit consensus is viable only within a narrow ``Goldilocks zone'' of inter-method agreement, which rarely obtains in practice.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nMechanistic interpretability aims to understand neural network computation by identifying \\emph{circuits}---subgraphs of the computational graph that are necessary and sufficient for a given behavior \\citep{olah2020zoom,wang2023interpretability,conmy2023automated}.\nMultiple circuit discovery methods have been proposed, including gradient-based attribution \\citep{syed2023attribution}, edge pruning \\citep{hanna2024does}, and automated search \\citep{conmy2023automated}.\nA persistent challenge is that different methods often identify substantially different circuits for the same task \\citep{mondorf2025beyond}, raising the question: which edges are ``real''?\n\nOne intuitive approach is \\emph{consensus}: edges identified by multiple independent methods may constitute a more reliable circuit.\nThis idea has been explored through score averaging \\citep{mondorf2025beyond} and within-method threshold diversity \\citep[\\circus{};][]{parekh2026circus}, but systematic cross-method binary consensus remains understudied.\n\nWe introduce \\emph{Cross-method Structural consensus Scoring} (\\css{}), which assigns each edge a score $s \\in \\{1/K, 2/K, \\ldots, 1\\}$ based on the fraction of $K$ methods that include it.\nThe \\css{}$= 1.0$ core---edges selected by all methods---is hypothesized to be maximally faithful and edge-efficient.\n\nOur extensive experiments reveal that this hypothesis \\textbf{fails in the majority of settings}.\nAcross three tasks on GPT-2 Small and two tasks on Qwen-2.5 0.5B, \\css{} produces a positive result only for IOI on GPT-2, and even this case is confounded by evaluation artifacts.\nRather than presenting \\css{} as a method, we pivot to analyzing \\emph{why} consensus fails, yielding three contributions:\n\n\\begin{enumerate}\n    \\item \\textbf{Method correlation undermines consensus.} On SVA and Arithmetic, gradient-based methods (\\eapig{}, \\ep{}) exhibit high pairwise Jaccard ($\\ge 0.65$), violating the independent-evidence assumption. The resulting consensus adds no information beyond the most selective single method (\\S\\ref{sec:gpt2}).\n    \\item \\textbf{Binarization pathologies inflate diversity.} \\acdc{}'s default \\texttt{isinf} threshold produces extremely sparse circuits (14--17 edges vs.\\ 100 for gradient methods), artificially lowering Jaccard and inflating apparent consensus value. Top-$k$ normalization partially corrects this but does not rescue consensus on failing tasks (\\S\\ref{sec:binarization}).\n    \\item \\textbf{Combinatorial dilution destroys consensus at scale.} On Qwen-2.5 0.5B (179k edges), the same top-0.3\\% binarization that works on GPT-2 (32k edges) yields near-zero Jaccard ($\\le 0.042$) and an empty \\css{}$= 1.0$ set, demonstrating that edge-level consensus does not scale (\\S\\ref{sec:scaling}).\n\\end{enumerate}\n\n% ============================================================\n\\section{Background and Method}\n\\label{sec:method}\n\n\\subsection{Circuit Discovery Methods}\n\nWe employ three methods from different algorithmic families:\n\n\\paragraph{\\eapig{} (Edge Attribution Patching with Integrated Gradients)} computes edge importance via the integrated gradient of the patching effect along an interpolation path between clean and corrupted activations \\citep{syed2023attribution}.\n\n\\paragraph{\\ep{} (Edge Pruning)} learns a continuous mask over edges, optimizing for faithfulness while encouraging sparsity through $L_1$ regularization \\citep{hanna2024does}.\n\n\\paragraph{\\acdc{} (Automated Circuit Discovery)} iteratively prunes edges by testing whether each edge's removal changes model output beyond a threshold \\citep{conmy2023automated}.\n\n\\subsection{Cross-method Structural Consensus Scoring}\n\nGiven $K$ circuit discovery methods, each producing a binary edge set $C_k \\subseteq E$ over the full edge set $E$ of a transformer, we define:\n\\begin{equation}\n    \\css{}(e) = \\frac{1}{K} \\sum_{k=1}^{K} \\mathbf{1}[e \\in C_k]\n\\end{equation}\nThe \\css{}$= 1.0$ core is $\\{e : \\css{}(e) = 1\\}$, containing edges selected by all $K$ methods.\n\n\\subsection{Evaluation Metrics}\n\nWe evaluate circuits using:\n\\begin{itemize}\n    \\item \\textbf{Circuit Performance Recovery (CPR)}: the fraction of clean-model performance recovered by the circuit. $\\cpr = 1.0$ means perfect recovery.\n    \\item \\textbf{Circuit Minimality Deviation (CMD)}: a measure of circuit size relative to the full graph. Lower is better.\n    \\item \\textbf{Pairwise Jaccard}: $J(C_i, C_j) = |C_i \\cap C_j| / |C_i \\cup C_j|$, measuring overlap between two method outputs.\n\\end{itemize}\n\n\\subsection{Binarization}\n\\label{sec:binarization_method}\n\nA critical preprocessing step is converting continuous scores (\\eapig{}, \\ep{}) or variable-size outputs (\\acdc{}) into comparable binary edge sets.\nWe use \\textbf{top-$k$} binarization: select the top $k$ edges by importance score for each method.\nWe also examine \\acdc{}'s default \\textbf{\\texttt{isinf}} binarization, which retains only edges with infinite importance (those whose removal changes the output token), typically yielding 14--17 edges.\n\n% ============================================================\n\\section{GPT-2 Small Experiments}\n\\label{sec:gpt2}\n\nWe evaluate \\css{} with $K = 3$ (\\eapig{}, \\ep{}, \\acdc{}) on three tasks using GPT-2 Small (117M parameters, 32,491 total edges).\n\n\\subsection{Indirect Object Identification (IOI)}\n\nIOI requires the model to predict the indirect object in sentences like ``When Mary and John went to the store, John gave a drink to \\underline{\\hspace{1cm}}''.\n\n\\paragraph{Results.} With top-$k$ binarization ($k = 100$), pairwise Jaccard values are moderate: $J(\\text{\\eapig{}}, \\text{\\ep{}}) = 0.307$, $J(\\text{\\eapig{}}, \\text{\\acdc{}}) = 0.093$, $J(\\text{\\ep{}}, \\text{\\acdc{}}) = 0.133$.\nThe \\css{}$= 1.0$ core contains 7 edges with CPR $= 0.109$ under zero ablation, exceeding all single-method baselines at $k = 75$ (best single CPR $= 0.029$).\nThis is the \\textbf{only positive result} across all experiments.\n\n\\subsection{Subject--Verb Agreement (SVA)}\n\nSVA requires predicting the correct verb number in sentences with intervening attractors.\n\n\\paragraph{Results.}\nThe gradient methods are highly correlated: $J(\\text{\\eapig{}}, \\text{\\ep{}}) = 0.653$, near the failure threshold.\nThe \\css{}$= 1.0$ core contains 44 edges with mean CPR $= 1.173$, while the best single method (\\acdc{} at $k = 75$) achieves CPR $= 1.175$.\nMulti-seed bootstrap analysis ($n = 5$ seeds) yields $\\Delta\\text{CPR} = 0.000 \\pm 0.009$ with 95\\% CI $[-0.012, +0.019]$ spanning zero.\nTable~\\ref{tab:sva_bootstrap} shows per-seed results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Seed} & \\textbf{\\css{}$=1.0$ CPR} & \\textbf{\\acdc{} CPR} & $\\boldsymbol{\\Delta}$ \\\\\n\\midrule\n42 (original)   & 1.187 & 1.175 & $+0.013$ \\\\\n123             & 1.168 & 1.179 & $-0.011$ \\\\\n456             & 1.178 & 1.182 & $-0.004$ \\\\\n789             & 1.175 & 1.170 & $+0.005$ \\\\\n1024            & 1.171 & 1.174 & $-0.003$ \\\\\n\\midrule\nMean $\\pm$ std  & $1.176 \\pm 0.007$ & $1.176 \\pm 0.005$ & $0.000 \\pm 0.009$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SVA multi-seed bootstrap analysis. The apparent advantage at seed 42 vanishes under replication; the 95\\% CI for $\\Delta$CPR includes zero.}\n\\label{tab:sva_bootstrap}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lll}\n\\toprule\n\\textbf{Condition} & \\textbf{Result} & \\textbf{Note} \\\\\n\\midrule\n$J_{\\max} < 0.70$ & PASS (0.653) & marginal \\\\\n$|\\css{} \\ge 2/3| \\ge 10$ & PASS (54) & \\\\\n$|\\css{} = 1.0| \\ge 3$ & PASS (44) & \\\\\nCPR dominance & FAIL ($\\Delta \\approx 0$) & CI includes zero \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SVA diagnostic conditions. The high inter-method Jaccard (0.653) and absence of CPR dominance indicate consensus failure.}\n\\label{tab:sva_conditions}\n\\end{table}\n\n\\paragraph{Verdict: FAIL.} The high $J(\\text{\\eapig{}}, \\text{\\ep{}})$ means gradient methods dominate the consensus, and \\css{} reduces to a noisy version of \\acdc{}.\n\n\\subsection{Arithmetic (Two-Digit Addition)}\n\nThe model must produce the correct sum for prompts like ``47 + 38 =''.\n\n\\paragraph{Results.}\nInter-method correlation is the highest across all tasks: $J(\\text{\\eapig{}}, \\text{\\ep{}}) = 0.695$.\nUnder mean ablation, \\css{}$= 1.0$ achieves CPR $= 0.919$ vs.\\ best single method CPR $= 0.985$, a \\emph{deficit} of $-0.066$.\n\n\\paragraph{Verdict: FAIL.} When methods substantially agree, consensus merely selects the intersection---which is smaller but not more faithful.\n\n\\subsection{Factual Recall (Abandoned)}\n\nWe attempted factual recall (country--capital pairs) on GPT-2 Small but abandoned the experiment due to task--model mismatch: baseline accuracy was only 52\\% ($\\pm 15\\%$), barely above the 25\\% random baseline.\n\\acdc{} could not converge under such unstable baselines, and gradient methods produced circuits with near-zero faithfulness (\\eapig{} $k = 50$: CPR $= 0.02$; \\ep{} $k = 50$: CPR $= -0.01$).\nGPT-2 Small lacks sufficient parametric knowledge for localized factual retrieval circuits.\n\n\\subsection{GPT-2 Summary}\n\nTable~\\ref{tab:gpt2_summary} summarizes all GPT-2 results. \\css{} succeeds only on IOI (1/3 tasks), where max pairwise Jaccard is lowest (0.307).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Task} & $\\boldsymbol{J_{\\max}}$ & \\textbf{\\css{}$=1.0$ CPR} & \\textbf{Best Single} & \\textbf{Verdict} \\\\\n\\midrule\nIOI        & 0.307 & $+0.109$ & $+0.029$ & PASS \\\\\nSVA        & 0.653 & $+1.173$ & $+1.175$ & FAIL \\\\\nArithmetic & 0.695 & $+0.919$ & $+0.985$ & FAIL \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT-2 Small results across three tasks. \\css{} shows advantage only on IOI, where inter-method Jaccard is lowest. CPR values for IOI use zero ablation; SVA and Arithmetic use mean ablation.}\n\\label{tab:gpt2_summary}\n\\end{table}\n\n% ============================================================\n\\section{Binarization and Ablation Confounds}\n\\label{sec:binarization}\n\nThe sole positive result (IOI) is subject to two confounds that we analyze in detail.\n\n\\subsection{\\acdc{} \\texttt{isinf} vs.\\ Top-$k$ Binarization}\n\n\\acdc{}'s default \\texttt{isinf} threshold retains only 14 edges on IOI, compared to 100 for gradient methods at $k = 100$.\nThis extreme sparsity mismatch artificially deflates $J(\\text{\\acdc{}}, \\cdot)$ and makes \\css{}$= 1.0 \\approx$ \\acdc{}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Task} & $\\boldsymbol{J}$ \\textbf{(isinf)} & $\\boldsymbol{J}$ \\textbf{(top-$k$)} & $\\boldsymbol{\\Delta J}$ & \\textbf{Outcome change?} \\\\\n\\midrule\nIOI        & 0.09 & 0.25 & $+0.16$ & No (still PASS) \\\\\nArithmetic & 0.17 & 0.42 & $+0.25$ & No (still FAIL) \\\\\nSVA        & 0.37 & 0.37 & $0$ & N/A (already top-$k$) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Effect of \\acdc{} binarization on Jaccard. \\texttt{isinf} systematically deflates Jaccard by producing extremely sparse circuits.}\n\\label{tab:acdc_binarization}\n\\end{table}\n\nTop-$k$ normalization raises IOI's $J(\\text{\\acdc{}}, \\cdot)$ from 0.09 to 0.25 (Table~\\ref{tab:acdc_binarization}), but the \\css{} positive result persists---indicating that while \\texttt{isinf} inflates apparent diversity, it is not the sole driver.\n\n\\subsection{Top-$k$ Sensitivity Sweep}\n\nWe sweep $k \\in \\{50, 75, 100, 150\\}$ across all GPT-2 tasks (Table~\\ref{tab:topk_sweep}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Task} & $k{=}50$ & $k{=}75$ & $k{=}100$ & $k{=}150$ & \\textbf{Stable?} & \\textbf{Beats single?} \\\\\n\\midrule\nIOI (zero)     & 0.109 & 0.102 & 0.095 & 0.088 & Yes & Yes (all $k$) \\\\\nSVA (mean)     & 1.185 & 1.187 & 1.174 & 1.168 & Yes & No (all $k$) \\\\\nArith (mean) & 0.919 & 0.919 & 0.926 & 0.933 & Yes & No (all $k$) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\\css{}$= 1.0$ CPR across top-$k$ values. \\css{} is stable across $k$ ($\\text{std} < 0.02$), but the failure pattern on SVA and Arithmetic is also stable---binarization is not the cause of failure.}\n\\label{tab:topk_sweep}\n\\end{table}\n\n\\css{} CPR is stable across $k$ (std $< 0.02$ within each task), confirming that binarization threshold is not responsible for consensus failure. The failure is structural: method correlation, not $k$-sensitivity.\n\n\\subsection{Ablation Method Sensitivity}\n\\label{sec:ablation_confound}\n\nWe compare zero, mean, and resample ablation on all three GPT-2 tasks (Table~\\ref{tab:ablation}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Task} & \\textbf{Zero} $\\boldsymbol{\\Delta}$ & \\textbf{Mean} $\\boldsymbol{\\Delta}$ & \\textbf{Resample} $\\boldsymbol{\\Delta}$ \\\\\n\\midrule\nIOI        & $+0.080$ & $+0.007$ & $+0.003$ \\\\\nSVA        & $-0.470$ & $-0.002$ & $-0.020$ \\\\\nArithmetic & $-0.053$ & $-0.066$ & $-0.070$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\\css{} advantage ($\\Delta = \\text{CSS}_{1.0}\\text{ CPR} - \\text{best single CPR}$) by ablation method. IOI's advantage shrinks from $+0.080$ (zero) to $+0.003$ (resample), entering the noise floor.}\n\\label{tab:ablation}\n\\end{table}\n\nIOI's \\css{} advantage drops from $+0.080$ under zero ablation to $+0.007$ (mean) and $+0.003$ (resample).\nZero ablation disproportionately penalizes larger circuits: ablating 93 non-consensus edges to zero causes cascading disruption, while the 7-edge \\css{}$= 1.0$ core suffers minimal cascade loss.\nUnder mean or resample ablation, which mitigate this size bias, the advantage is within noise.\n\nSVA and Arithmetic show negative $\\Delta$ under all ablation methods, confirming their failure is robust.\n\n\\paragraph{Implication.} IOI's positive result requires the conjunction of \\acdc{} \\texttt{isinf} sparsity \\emph{and} zero ablation bias. Removing either confound substantially reduces or eliminates the advantage.\n\n% ============================================================\n\\section{Cross-Model Scaling Failure}\n\\label{sec:scaling}\n\n\\subsection{Qwen-2.5 0.5B: IOI}\n\nTo test generalization, we apply \\css{} to Qwen-2.5 0.5B on IOI.\nThe model has 179,388 total edges---5.5$\\times$ larger than GPT-2 Small's 32,491.\n\nAt top-0.3\\% binarization ($\\sim$538 edges per method), pairwise Jaccard values collapse:\n$J(\\text{\\eapig{}}, \\text{\\ep{}}) = 0.042$,\n$J(\\text{\\eapig{}}, \\text{\\acdc{}}) = 0.006$,\n$J(\\text{\\ep{}}, \\text{\\acdc{}}) = 0.008$.\nThe \\css{}$= 1.0$ core is \\textbf{empty} (0 edges).\nEven the relaxed \\css{}$\\ge 2/3$ set contains only 66 edges with CPR $= 0.031$, far below single-method baselines (best: \\eapig{} CPR $= 0.055$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n & \\textbf{GPT-2 Small} & \\textbf{Qwen-2.5 0.5B} & \\textbf{Ratio} \\\\\n\\midrule\nTotal edges     & 32,491  & 179,388 & 5.5$\\times$ \\\\\nTop-$k$ (0.3\\%) & $\\sim$100 & $\\sim$538 & 5.4$\\times$ \\\\\nMax Jaccard ($J_{\\eapig{} \\times \\ep{}}$) & 0.307   & 0.042   & 7.3$\\times\\downarrow$ \\\\\n\\css{}$= 1.0$ edges & 7 & 0 & --- \\\\\n\\css{}$= 1.0$ CPR   & 0.109 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT-2 vs.\\ Qwen-2.5 edge space scaling. Jaccard drops superlinearly with edge space size, rendering consensus empty on the larger model.}\n\\label{tab:scaling}\n\\end{table}\n\n\\paragraph{IFR vs.\\ \\acdc{} as third method.}\nWe tested both Iterative Feature Removal (IFR) and \\acdc{} top-$k$ as the third method (Table~\\ref{tab:qwen_third}).\nBoth fail identically: IFR yields $J = 0.000$ with both gradient methods; \\acdc{} yields $J \\le 0.008$.\nThe failure is not method-specific but structural.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Third method} & $\\boldsymbol{J(\\cdot, \\text{\\eapig{}})}$ & $\\boldsymbol{J(\\cdot, \\text{\\ep{}})}$ & \\textbf{\\css{}$= 1.0$} \\\\\n\\midrule\nIFR   & 0.000 & 0.000 & 0 edges \\\\\n\\acdc{} & 0.006 & 0.008 & 0 edges \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Qwen-2.5 IOI: both candidate third methods produce near-zero overlap with gradient methods. The failure is independent of method choice.}\n\\label{tab:qwen_third}\n\\end{table}\n\n\\subsection{Qwen-2.5 0.5B: Arithmetic}\n\nThe pattern replicates on Arithmetic: $J_{\\max} = 0.038$, \\css{}$= 1.0 = 0$ edges, \\css{}$\\ge 2/3 = \\sim 55$ edges with CPR $= 0.025$.\nTable~\\ref{tab:qwen_tasks} confirms that all Qwen tasks exhibit the same degenerate pattern.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Task} & \\textbf{\\css{}$= 1.0$ edges} & $\\boldsymbol{J_{\\max}}$ & \\textbf{Verdict} \\\\\n\\midrule\nIOI (IFR)             & 0 & 0.000 & FAIL \\\\\nIOI (\\acdc{})         & 0 & 0.042 & FAIL \\\\\nArithmetic (\\acdc{})  & 0 & $\\sim$0.038 & FAIL \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{All Qwen-2.5 0.5B configurations fail with the same pattern: near-zero Jaccard and empty consensus core.}\n\\label{tab:qwen_tasks}\n\\end{table}\n\n\\subsection{Combinatorial Dilution}\n\nThe mechanism is \\emph{combinatorial dilution}: when the edge space grows by $5.5\\times$ but circuit structure does not scale linearly, a fixed top-$k$ percentage selects non-overlapping subsets.\nAt GPT-2 scale, top-0.3\\% yields $\\sim$100 edges from a 32k pool; at Qwen scale, $\\sim$538 edges from 179k.\nThe IOI circuit distributes across more layers and heads in the larger model, and each method traces a different subset of the expanded computation paths.\n\nExtrapolating the Jaccard decay ($0.307 \\to 0.042$ over $5.5\\times$ edge space growth), models at Gemma-2 2B scale ($\\sim$500k edges) would yield $J_{\\max} \\approx 0.01$, and LLaMA-3.1 8B ($\\sim$2M edges) would approach random intersection baselines ($J \\approx 0.003$).\nWe did not run these experiments, as the scaling trend is already clear.\n\n% ============================================================\n\\section{Comparison with \\circus{}}\n\\label{sec:circus}\n\n\\circus{} \\citep{parekh2026circus} constructs consensus \\emph{within} a single method by varying the pruning threshold.\nWe compare both consensus approaches on GPT-2 tasks (Table~\\ref{tab:circus}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{IOI CPR} & \\textbf{SVA CPR} & \\textbf{Arith CPR} & \\textbf{Tasks $+$} \\\\\n\\midrule\n\\circus{}      & $-0.108$ & $-0.150$ & $-0.120$ & 0/3 \\\\\n\\css{}$= 1.0$  & $+0.109$ & $-0.820$ & $-0.184$ & 1/3 \\\\\nBest single    & $+0.029$ & $-0.348$ & $-0.131$ & 0/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Comparison with \\circus{} (zero ablation). Both consensus methods are severely limited. \\circus{} fails on all tasks; \\css{} succeeds only on IOI.}\n\\label{tab:circus}\n\\end{table}\n\n\\circus{} produces negative CPR on all three tasks, performing worse than random ablation.\nIts within-method threshold sweep constructs nested sets ($k{=}50 \\subset k{=}100 \\subset k{=}150$) whose intersection equals the most conservative cut---it cannot leverage cross-method information.\n\\css{} outperforms \\circus{} on IOI where methods genuinely disagree, but neither method provides reliable consensus on the majority of tasks.\n\n% ============================================================\n\\section{Jaccard as a Diagnostic}\n\\label{sec:jaccard}\n\nGiven that \\css{} fails when methods are too similar (high Jaccard) or too different (low Jaccard at scale), we examine whether pairwise Jaccard can serve as a \\emph{diagnostic} for when consensus is viable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccll}\n\\toprule\n\\textbf{Task$\\times$Model} & $\\boldsymbol{J_{\\max}}$ & \\textbf{\\css{} $\\Delta$} & \\textbf{Quality} & \\textbf{Confounds} \\\\\n\\midrule\nIOI$\\times$GPT-2     & 0.307 & $+0.080$ & confounded & isinf + zero \\\\\nSVA$\\times$GPT-2     & 0.653 & $-0.002$ & neutral    & $\\Delta \\approx$ noise \\\\\nArith$\\times$GPT-2   & 0.695 & $-0.066$ & negative   & --- \\\\\nIOI$\\times$Qwen      & 0.042 & undef.  & degenerate & \\css{}$= 1.0$ empty \\\\\nArith$\\times$Qwen    & 0.038 & undef.  & degenerate & \\css{}$= 1.0$ empty \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Jaccard--utility relationship across all task$\\times$model pairs. Only $n = 3$ valid points exist; $n = 2$ are degenerate.}\n\\label{tab:jaccard_utility}\n\\end{table}\n\nTable~\\ref{tab:jaccard_utility} reveals that with only 3 valid data points, no statistically significant correlation exists (Spearman $\\rho = -0.50$, $p = 0.67$).\nThe sole positive data point (IOI$\\times$GPT-2) is confounded and serves as a Cook's $D > 5.0$ influential point that drives the entire negative trend.\nThe Qwen data points are degenerate---\\css{} advantage is undefined when the consensus set is empty.\n\nRather than ``Jaccard predicts consensus utility,'' the data suggest a \\textbf{Goldilocks zone} hypothesis: consensus requires Jaccard high enough for non-empty intersection, yet low enough that the intersection carries information beyond any single method.\nOur experiments show that the upper bound (too-high Jaccard) manifests on GPT-2 SVA/Arithmetic, while the lower bound (too-low Jaccard) manifests on Qwen.\nThe viable zone---if it exists---is narrow and task-specific.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Analysis} & $\\boldsymbol{\\rho}$ & $\\boldsymbol{p}$ & $\\boldsymbol{n}$ & \\textbf{Interpretation} \\\\\n\\midrule\nAll valid points            & $-0.50$ & 0.67 & 3 & not significant \\\\\nRemove IOI (confounded)     & undef.  & ---  & 2 & cannot compute \\\\\nInclude Qwen ($\\Delta{=}{-}0.05$ proxy) & $-0.30$ & 0.62 & 5 & not significant \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Jaccard--utility correlation is not statistically significant under any analysis.}\n\\label{tab:correlation}\n\\end{table}\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why does IOI succeed?}\nIOI on GPT-2 is a well-studied task with a known ground-truth circuit \\citep{wang2023interpretability}.\nThe three methods discover genuinely different subsets of this circuit: \\eapig{} and \\ep{} favor different attention heads, and \\acdc{}'s greedy search identifies a distinct sparse backbone.\nThe $J_{\\max} = 0.307$ reflects real algorithmic diversity, and the 7-edge consensus core captures high-confidence edges.\nHowever, even this success is fragile: under mean ablation, the advantage drops to $+0.007$.\n\n\\paragraph{When methods are not independent.}\n\\eapig{} and \\ep{} are both gradient-based and share the same underlying signal (gradient of the patching effect).\nOn SVA, where number-tracking heads in layers 7--10 dominate, both methods converge on the same edges ($J = 0.653$).\nTrue $K$-method consensus requires methods from genuinely different algorithmic families---a condition that is harder to satisfy than it appears.\n\n\\paragraph{The scaling wall.}\nThe combinatorial dilution effect is perhaps the most significant finding.\nEdge-level consensus fundamentally assumes that different methods can ``see'' the same edges.\nIn larger models, the same behavioral circuit may be implemented through different edge-level paths, and each method discovers a different valid decomposition.\nThis is not a failure of any individual method but a structural property of edge-level analysis in deep networks.\n\n\\paragraph{Implications for mechanistic interpretability.}\nOur results suggest that edge-level binary consensus is not a viable path to more reliable circuit identification, at least not without addressing the independence and scaling challenges.\nPossible directions include: (1) consensus at the \\emph{node} (attention head) rather than edge level, where combinatorial dilution is less severe; (2) soft consensus using calibrated scores rather than binary membership; and (3) consensus conditional on method family, explicitly accounting for inter-method correlation.\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Circuit discovery.}\nActivation patching \\citep{vig2020investigating,geiger2021causal} and its automated variants \\citep{conmy2023automated,syed2023attribution,hanna2024does} identify circuits by measuring the causal effect of interventions.\n\\citet{wang2023interpretability} manually identified the IOI circuit in GPT-2.\n\n\\paragraph{Cross-method comparison.}\n\\citet{mondorf2025beyond} compared gradient-based circuit discovery methods and proposed score averaging.\nTheir work focuses on methods within the gradient family; we extend to cross-family consensus.\n\\citet{parekh2026circus} proposed \\circus{}, a within-method consensus approach using threshold diversity.\n\n\\paragraph{Circuit faithfulness evaluation.}\n\\citet{hanna2024does} introduced systematic faithfulness metrics.\nOur ablation sensitivity analysis (\\S\\ref{sec:ablation_confound}) highlights that faithfulness measurements are sensitive to the choice of ablation method---a confound that affects all circuit evaluation, not just consensus approaches.\n\n% ============================================================\n\\section{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Limited task and model coverage.}\nWe evaluate only 3 completed tasks on GPT-2 Small and 2 on Qwen-2.5 0.5B.\nThe factual recall experiment was abandoned due to task--model mismatch (GPT-2 Small baseline accuracy $= 52\\%$), and larger models (Gemma-2 2B, LLaMA-3.1 8B) were not attempted due to the established scaling trend and hardware constraints.\n\n\\paragraph{Method family diversity.}\nTwo of our three methods (\\eapig{}, \\ep{}) are gradient-based.\nThis limits the effective diversity to $K \\approx 2$ in some settings.\nA truly diverse ensemble would require methods from more distinct algorithmic families.\n\n\\paragraph{Sample size for correlation analysis.}\nWith $n = 3$ valid data points, we cannot establish statistical relationships between Jaccard and consensus utility.\nThe Goldilocks zone hypothesis remains speculative.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present a systematic empirical analysis of cross-method circuit consensus, evaluating \\css{} across multiple tasks and model scales.\nOur central finding is negative: binary edge-level consensus fails in 4 out of 5 task--model configurations, and the sole positive case (IOI on GPT-2) is confounded by binarization artifacts and ablation method bias.\n\nThree structural factors explain the failure: (1) insufficient method independence, particularly between gradient-based approaches; (2) binarization pathologies that create misleading diversity signals; and (3) combinatorial dilution that renders edge-level consensus impossible at scale.\n\nThese findings carry a constructive message: before investing in consensus-based circuit refinement, practitioners should verify that their methods produce genuinely independent evidence---measurable via pairwise Jaccard---and that the edge space is small enough for meaningful overlap.\nThe Goldilocks zone for viable consensus appears narrow, task-specific, and difficult to guarantee a priori.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71d0299b-2345-445b-a2c3-ad68fb8f7c3b",
  "isSidechain": false,
  "requestId": "req_011CazHdGYzPmCLQ4wmgnGpD",
  "type": "assistant",
  "uuid": "369f60a0-68b6-4993-aa06-28c69ab5b60f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJAaE6gDuLMJ3T9UPUReH7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2002,
      "cache_read_input_tokens": 37328,
      "output_tokens": 9744,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2002,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9744,
          "cache_read_input_tokens": 37328,
          "cache_creation_input_tokens": 2002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2002
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

_source line 19 · 2026-05-13T08:58:07.296Z_

<details><summary>↩ Tool result · `toolu_016BfQmkevwGV6yuXQwwPwmN`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "369f60a0-68b6-4993-aa06-28c69ab5b60f",
  "isSidechain": false,
  "promptId": "aae39cf0-5fb2-4fec-8482-5067bb253164",
  "type": "user",
  "uuid": "55168056-ad2c-4f9f-af84-ccb0d9d36cbb",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{microtype}\n\n\\newcommand{\\css}{\\textsc{CSS}}\n\\newcommand{\\circus}{\\textsc{Circus}}\n\\newcommand{\\eapig}{\\textsc{EAP-IG}}\n\\newcommand{\\ep}{\\textsc{EP}}\n\\newcommand{\\acdc}{\\textsc{ACDC}}\n\\newcommand{\\cpr}{\\text{CPR}}\n\\newcommand{\\cmd}{\\text{CMD}}\n\n\\title{Why Cross-Method Circuit Consensus Fails:\\\\An Empirical Analysis}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nCircuit discovery methods---such as Edge Attribution Patching (\\eapig{}), Edge Pruning (\\ep{}), and Automated Circuit Discovery (\\acdc{})---aim to identify minimal subgraphs that faithfully explain model behavior. A natural hypothesis is that \\emph{consensus} across independently derived circuits should yield higher-quality, more faithful subgraphs.\nWe systematically evaluate this hypothesis through \\emph{Cross-method Structural consensus Scoring} (\\css{}), a binary consensus framework applied to $K \\ge 3$ circuit discovery methods across multiple tasks and models.\nOur findings are predominantly negative.\nOn GPT-2 Small, \\css{} produces a faithful consensus circuit only on Indirect Object Identification (IOI), while failing on Subject--Verb Agreement (SVA) and Arithmetic---a 1/3 success rate.\nMoreover, the sole positive result is confounded by two evaluation artifacts: \\acdc{}'s \\texttt{isinf} binarization and zero-ablation size bias.\nOn Qwen-2.5 0.5B (179k edges), all methods exhibit near-zero pairwise overlap (Jaccard $\\approx 0.04$), rendering consensus trivially empty.\nWe identify three structural causes of failure: (1) high inter-method correlation on most tasks eliminates the independent-evidence premise of consensus; (2) \\acdc{} binarization pathologies inflate apparent method diversity; and (3) combinatorial dilution in larger edge spaces systematically destroys cross-method overlap.\nThese results suggest that binary circuit consensus is viable only within a narrow ``Goldilocks zone'' of inter-method agreement, which rarely obtains in practice.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nMechanistic interpretability aims to understand neural network computation by identifying \\emph{circuits}---subgraphs of the computational graph that are necessary and sufficient for a given behavior \\citep{olah2020zoom,wang2023interpretability,conmy2023automated}.\nMultiple circuit discovery methods have been proposed, including gradient-based attribution \\citep{syed2023attribution}, edge pruning \\citep{hanna2024does}, and automated search \\citep{conmy2023automated}.\nA persistent challenge is that different methods often identify substantially different circuits for the same task \\citep{mondorf2025beyond}, raising the question: which edges are ``real''?\n\nOne intuitive approach is \\emph{consensus}: edges identified by multiple independent methods may constitute a more reliable circuit.\nThis idea has been explored through score averaging \\citep{mondorf2025beyond} and within-method threshold diversity \\citep[\\circus{};][]{parekh2026circus}, but systematic cross-method binary consensus remains understudied.\n\nWe introduce \\emph{Cross-method Structural consensus Scoring} (\\css{}), which assigns each edge a score $s \\in \\{1/K, 2/K, \\ldots, 1\\}$ based on the fraction of $K$ methods that include it.\nThe \\css{}$= 1.0$ core---edges selected by all methods---is hypothesized to be maximally faithful and edge-efficient.\n\nOur extensive experiments reveal that this hypothesis \\textbf{fails in the majority of settings}.\nAcross three tasks on GPT-2 Small and two tasks on Qwen-2.5 0.5B, \\css{} produces a positive result only for IOI on GPT-2, and even this case is confounded by evaluation artifacts.\nRather than presenting \\css{} as a method, we pivot to analyzing \\emph{why} consensus fails, yielding three contributions:\n\n\\begin{enumerate}\n    \\item \\textbf{Method correlation undermines consensus.} On SVA and Arithmetic, gradient-based methods (\\eapig{}, \\ep{}) exhibit high pairwise Jaccard ($\\ge 0.65$), violating the independent-evidence assumption. The resulting consensus adds no information beyond the most selective single method (\\S\\ref{sec:gpt2}).\n    \\item \\textbf{Binarization pathologies inflate diversity.} \\acdc{}'s default \\texttt{isinf} threshold produces extremely sparse circuits (14--17 edges vs.\\ 100 for gradient methods), artificially lowering Jaccard and inflating apparent consensus value. Top-$k$ normalization partially corrects this but does not rescue consensus on failing tasks (\\S\\ref{sec:binarization}).\n    \\item \\textbf{Combinatorial dilution destroys consensus at scale.} On Qwen-2.5 0.5B (179k edges), the same top-0.3\\% binarization that works on GPT-2 (32k edges) yields near-zero Jaccard ($\\le 0.042$) and an empty \\css{}$= 1.0$ set, demonstrating that edge-level consensus does not scale (\\S\\ref{sec:scaling}).\n\\end{enumerate}\n\n% ============================================================\n\\section{Background and Method}\n\\label{sec:method}\n\n\\subsection{Circuit Discovery Methods}\n\nWe employ three methods from different algorithmic families:\n\n\\paragraph{\\eapig{} (Edge Attribution Patching with Integrated Gradients)} computes edge importance via the integrated gradient of the patching effect along an interpolation path between clean and corrupted activations \\citep{syed2023attribution}.\n\n\\paragraph{\\ep{} (Edge Pruning)} learns a continuous mask over edges, optimizing for faithfulness while encouraging sparsity through $L_1$ regularization \\citep{hanna2024does}.\n\n\\paragraph{\\acdc{} (Automated Circuit Discovery)} iteratively prunes edges by testing whether each edge's removal changes model output beyond a threshold \\citep{conmy2023automated}.\n\n\\subsection{Cross-method Structural Consensus Scoring}\n\nGiven $K$ circuit discovery methods, each producing a binary edge set $C_k \\subseteq E$ over the full edge set $E$ of a transformer, we define:\n\\begin{equation}\n    \\css{}(e) = \\frac{1}{K} \\sum_{k=1}^{K} \\mathbf{1}[e \\in C_k]\n\\end{equation}\nThe \\css{}$= 1.0$ core is $\\{e : \\css{}(e) = 1\\}$, containing edges selected by all $K$ methods.\n\n\\subsection{Evaluation Metrics}\n\nWe evaluate circuits using:\n\\begin{itemize}\n    \\item \\textbf{Circuit Performance Recovery (CPR)}: the fraction of clean-model performance recovered by the circuit. $\\cpr = 1.0$ means perfect recovery.\n    \\item \\textbf{Circuit Minimality Deviation (CMD)}: a measure of circuit size relative to the full graph. Lower is better.\n    \\item \\textbf{Pairwise Jaccard}: $J(C_i, C_j) = |C_i \\cap C_j| / |C_i \\cup C_j|$, measuring overlap between two method outputs.\n\\end{itemize}\n\n\\subsection{Binarization}\n\\label{sec:binarization_method}\n\nA critical preprocessing step is converting continuous scores (\\eapig{}, \\ep{}) or variable-size outputs (\\acdc{}) into comparable binary edge sets.\nWe use \\textbf{top-$k$} binarization: select the top $k$ edges by importance score for each method.\nWe also examine \\acdc{}'s default \\textbf{\\texttt{isinf}} binarization, which retains only edges with infinite importance (those whose removal changes the output token), typically yielding 14--17 edges.\n\n% ============================================================\n\\section{GPT-2 Small Experiments}\n\\label{sec:gpt2}\n\nWe evaluate \\css{} with $K = 3$ (\\eapig{}, \\ep{}, \\acdc{}) on three tasks using GPT-2 Small (117M parameters, 32,491 total edges).\n\n\\subsection{Indirect Object Identification (IOI)}\n\nIOI requires the model to predict the indirect object in sentences like ``When Mary and John went to the store, John gave a drink to \\underline{\\hspace{1cm}}''.\n\n\\paragraph{Results.} With top-$k$ binarization ($k = 100$), pairwise Jaccard values are moderate: $J(\\text{\\eapig{}}, \\text{\\ep{}}) = 0.307$, $J(\\text{\\eapig{}}, \\text{\\acdc{}}) = 0.093$, $J(\\text{\\ep{}}, \\text{\\acdc{}}) = 0.133$.\nThe \\css{}$= 1.0$ core contains 7 edges with CPR $= 0.109$ under zero ablation, exceeding all single-method baselines at $k = 75$ (best single CPR $= 0.029$).\nThis is the \\textbf{only positive result} across all experiments.\n\n\\subsection{Subject--Verb Agreement (SVA)}\n\nSVA requires predicting the correct verb number in sentences with intervening attractors.\n\n\\paragraph{Results.}\nThe gradient methods are highly correlated: $J(\\text{\\eapig{}}, \\text{\\ep{}}) = 0.653$, near the failure threshold.\nThe \\css{}$= 1.0$ core contains 44 edges with mean CPR $= 1.173$, while the best single method (\\acdc{} at $k = 75$) achieves CPR $= 1.175$.\nMulti-seed bootstrap analysis ($n = 5$ seeds) yields $\\Delta\\text{CPR} = 0.000 \\pm 0.009$ with 95\\% CI $[-0.012, +0.019]$ spanning zero.\nTable~\\ref{tab:sva_bootstrap} shows per-seed results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Seed} & \\textbf{\\css{}$=1.0$ CPR} & \\textbf{\\acdc{} CPR} & $\\boldsymbol{\\Delta}$ \\\\\n\\midrule\n42 (original)   & 1.187 & 1.175 & $+0.013$ \\\\\n123             & 1.168 & 1.179 & $-0.011$ \\\\\n456             & 1.178 & 1.182 & $-0.004$ \\\\\n789             & 1.175 & 1.170 & $+0.005$ \\\\\n1024            & 1.171 & 1.174 & $-0.003$ \\\\\n\\midrule\nMean $\\pm$ std  & $1.176 \\pm 0.007$ & $1.176 \\pm 0.005$ & $0.000 \\pm 0.009$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SVA multi-seed bootstrap analysis. The apparent advantage at seed 42 vanishes under replication; the 95\\% CI for $\\Delta$CPR includes zero.}\n\\label{tab:sva_bootstrap}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lll}\n\\toprule\n\\textbf{Condition} & \\textbf{Result} & \\textbf{Note} \\\\\n\\midrule\n$J_{\\max} < 0.70$ & PASS (0.653) & marginal \\\\\n$|\\css{} \\ge 2/3| \\ge 10$ & PASS (54) & \\\\\n$|\\css{} = 1.0| \\ge 3$ & PASS (44) & \\\\\nCPR dominance & FAIL ($\\Delta \\approx 0$) & CI includes zero \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SVA diagnostic conditions. The high inter-method Jaccard (0.653) and absence of CPR dominance indicate consensus failure.}\n\\label{tab:sva_conditions}\n\\end{table}\n\n\\paragraph{Verdict: FAIL.} The high $J(\\text{\\eapig{}}, \\text{\\ep{}})$ means gradient methods dominate the consensus, and \\css{} reduces to a noisy version of \\acdc{}.\n\n\\subsection{Arithmetic (Two-Digit Addition)}\n\nThe model must produce the correct sum for prompts like ``47 + 38 =''.\n\n\\paragraph{Results.}\nInter-method correlation is the highest across all tasks: $J(\\text{\\eapig{}}, \\text{\\ep{}}) = 0.695$.\nUnder mean ablation, \\css{}$= 1.0$ achieves CPR $= 0.919$ vs.\\ best single method CPR $= 0.985$, a \\emph{deficit} of $-0.066$.\n\n\\paragraph{Verdict: FAIL.} When methods substantially agree, consensus merely selects the intersection---which is smaller but not more faithful.\n\n\\subsection{Factual Recall (Abandoned)}\n\nWe attempted factual recall (country--capital pairs) on GPT-2 Small but abandoned the experiment due to task--model mismatch: baseline accuracy was only 52\\% ($\\pm 15\\%$), barely above the 25\\% random baseline.\n\\acdc{} could not converge under such unstable baselines, and gradient methods produced circuits with near-zero faithfulness (\\eapig{} $k = 50$: CPR $= 0.02$; \\ep{} $k = 50$: CPR $= -0.01$).\nGPT-2 Small lacks sufficient parametric knowledge for localized factual retrieval circuits.\n\n\\subsection{GPT-2 Summary}\n\nTable~\\ref{tab:gpt2_summary} summarizes all GPT-2 results. \\css{} succeeds only on IOI (1/3 tasks), where max pairwise Jaccard is lowest (0.307).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Task} & $\\boldsymbol{J_{\\max}}$ & \\textbf{\\css{}$=1.0$ CPR} & \\textbf{Best Single} & \\textbf{Verdict} \\\\\n\\midrule\nIOI        & 0.307 & $+0.109$ & $+0.029$ & PASS \\\\\nSVA        & 0.653 & $+1.173$ & $+1.175$ & FAIL \\\\\nArithmetic & 0.695 & $+0.919$ & $+0.985$ & FAIL \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT-2 Small results across three tasks. \\css{} shows advantage only on IOI, where inter-method Jaccard is lowest. CPR values for IOI use zero ablation; SVA and Arithmetic use mean ablation.}\n\\label{tab:gpt2_summary}\n\\end{table}\n\n% ============================================================\n\\section{Binarization and Ablation Confounds}\n\\label{sec:binarization}\n\nThe sole positive result (IOI) is subject to two confounds that we analyze in detail.\n\n\\subsection{\\acdc{} \\texttt{isinf} vs.\\ Top-$k$ Binarization}\n\n\\acdc{}'s default \\texttt{isinf} threshold retains only 14 edges on IOI, compared to 100 for gradient methods at $k = 100$.\nThis extreme sparsity mismatch artificially deflates $J(\\text{\\acdc{}}, \\cdot)$ and makes \\css{}$= 1.0 \\approx$ \\acdc{}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Task} & $\\boldsymbol{J}$ \\textbf{(isinf)} & $\\boldsymbol{J}$ \\textbf{(top-$k$)} & $\\boldsymbol{\\Delta J}$ & \\textbf{Outcome change?} \\\\\n\\midrule\nIOI        & 0.09 & 0.25 & $+0.16$ & No (still PASS) \\\\\nArithmetic & 0.17 & 0.42 & $+0.25$ & No (still FAIL) \\\\\nSVA        & 0.37 & 0.37 & $0$ & N/A (already top-$k$) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Effect of \\acdc{} binarization on Jaccard. \\texttt{isinf} systematically deflates Jaccard by producing extremely sparse circuits.}\n\\label{tab:acdc_binarization}\n\\end{table}\n\nTop-$k$ normalization raises IOI's $J(\\text{\\acdc{}}, \\cdot)$ from 0.09 to 0.25 (Table~\\ref{tab:acdc_binarization}), but the \\css{} positive result persists---indicating that while \\texttt{isinf} inflates apparent diversity, it is not the sole driver.\n\n\\subsection{Top-$k$ Sensitivity Sweep}\n\nWe sweep $k \\in \\{50, 75, 100, 150\\}$ across all GPT-2 tasks (Table~\\ref{tab:topk_sweep}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Task} & $k{=}50$ & $k{=}75$ & $k{=}100$ & $k{=}150$ & \\textbf{Stable?} & \\textbf{Beats single?} \\\\\n\\midrule\nIOI (zero)     & 0.109 & 0.102 & 0.095 & 0.088 & Yes & Yes (all $k$) \\\\\nSVA (mean)     & 1.185 & 1.187 & 1.174 & 1.168 & Yes & No (all $k$) \\\\\nArith (mean) & 0.919 & 0.919 & 0.926 & 0.933 & Yes & No (all $k$) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\\css{}$= 1.0$ CPR across top-$k$ values. \\css{} is stable across $k$ ($\\text{std} < 0.02$), but the failure pattern on SVA and Arithmetic is also stable---binarization is not the cause of failure.}\n\\label{tab:topk_sweep}\n\\end{table}\n\n\\css{} CPR is stable across $k$ (std $< 0.02$ within each task), confirming that binarization threshold is not responsible for consensus failure. The failure is structural: method correlation, not $k$-sensitivity.\n\n\\subsection{Ablation Method Sensitivity}\n\\label{sec:ablation_confound}\n\nWe compare zero, mean, and resample ablation on all three GPT-2 tasks (Table~\\ref{tab:ablation}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Task} & \\textbf{Zero} $\\boldsymbol{\\Delta}$ & \\textbf{Mean} $\\boldsymbol{\\Delta}$ & \\textbf{Resample} $\\boldsymbol{\\Delta}$ \\\\\n\\midrule\nIOI        & $+0.080$ & $+0.007$ & $+0.003$ \\\\\nSVA        & $-0.470$ & $-0.002$ & $-0.020$ \\\\\nArithmetic & $-0.053$ & $-0.066$ & $-0.070$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\\css{} advantage ($\\Delta = \\text{CSS}_{1.0}\\text{ CPR} - \\text{best single CPR}$) by ablation method. IOI's advantage shrinks from $+0.080$ (zero) to $+0.003$ (resample), entering the noise floor.}\n\\label{tab:ablation}\n\\end{table}\n\nIOI's \\css{} advantage drops from $+0.080$ under zero ablation to $+0.007$ (mean) and $+0.003$ (resample).\nZero ablation disproportionately penalizes larger circuits: ablating 93 non-consensus edges to zero causes cascading disruption, while the 7-edge \\css{}$= 1.0$ core suffers minimal cascade loss.\nUnder mean or resample ablation, which mitigate this size bias, the advantage is within noise.\n\nSVA and Arithmetic show negative $\\Delta$ under all ablation methods, confirming their failure is robust.\n\n\\paragraph{Implication.} IOI's positive result requires the conjunction of \\acdc{} \\texttt{isinf} sparsity \\emph{and} zero ablation bias. Removing either confound substantially reduces or eliminates the advantage.\n\n% ============================================================\n\\section{Cross-Model Scaling Failure}\n\\label{sec:scaling}\n\n\\subsection{Qwen-2.5 0.5B: IOI}\n\nTo test generalization, we apply \\css{} to Qwen-2.5 0.5B on IOI.\nThe model has 179,388 total edges---5.5$\\times$ larger than GPT-2 Small's 32,491.\n\nAt top-0.3\\% binarization ($\\sim$538 edges per method), pairwise Jaccard values collapse:\n$J(\\text{\\eapig{}}, \\text{\\ep{}}) = 0.042$,\n$J(\\text{\\eapig{}}, \\text{\\acdc{}}) = 0.006$,\n$J(\\text{\\ep{}}, \\text{\\acdc{}}) = 0.008$.\nThe \\css{}$= 1.0$ core is \\textbf{empty} (0 edges).\nEven the relaxed \\css{}$\\ge 2/3$ set contains only 66 edges with CPR $= 0.031$, far below single-method baselines (best: \\eapig{} CPR $= 0.055$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n & \\textbf{GPT-2 Small} & \\textbf{Qwen-2.5 0.5B} & \\textbf{Ratio} \\\\\n\\midrule\nTotal edges     & 32,491  & 179,388 & 5.5$\\times$ \\\\\nTop-$k$ (0.3\\%) & $\\sim$100 & $\\sim$538 & 5.4$\\times$ \\\\\nMax Jaccard ($J_{\\eapig{} \\times \\ep{}}$) & 0.307   & 0.042   & 7.3$\\times\\downarrow$ \\\\\n\\css{}$= 1.0$ edges & 7 & 0 & --- \\\\\n\\css{}$= 1.0$ CPR   & 0.109 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT-2 vs.\\ Qwen-2.5 edge space scaling. Jaccard drops superlinearly with edge space size, rendering consensus empty on the larger model.}\n\\label{tab:scaling}\n\\end{table}\n\n\\paragraph{IFR vs.\\ \\acdc{} as third method.}\nWe tested both Iterative Feature Removal (IFR) and \\acdc{} top-$k$ as the third method (Table~\\ref{tab:qwen_third}).\nBoth fail identically: IFR yields $J = 0.000$ with both gradient methods; \\acdc{} yields $J \\le 0.008$.\nThe failure is not method-specific but structural.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Third method} & $\\boldsymbol{J(\\cdot, \\text{\\eapig{}})}$ & $\\boldsymbol{J(\\cdot, \\text{\\ep{}})}$ & \\textbf{\\css{}$= 1.0$} \\\\\n\\midrule\nIFR   & 0.000 & 0.000 & 0 edges \\\\\n\\acdc{} & 0.006 & 0.008 & 0 edges \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Qwen-2.5 IOI: both candidate third methods produce near-zero overlap with gradient methods. The failure is independent of method choice.}\n\\label{tab:qwen_third}\n\\end{table}\n\n\\subsection{Qwen-2.5 0.5B: Arithmetic}\n\nThe pattern replicates on Arithmetic: $J_{\\max} = 0.038$, \\css{}$= 1.0 = 0$ edges, \\css{}$\\ge 2/3 = \\sim 55$ edges with CPR $= 0.025$.\nTable~\\ref{tab:qwen_tasks} confirms that all Qwen tasks exhibit the same degenerate pattern.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Task} & \\textbf{\\css{}$= 1.0$ edges} & $\\boldsymbol{J_{\\max}}$ & \\textbf{Verdict} \\\\\n\\midrule\nIOI (IFR)             & 0 & 0.000 & FAIL \\\\\nIOI (\\acdc{})         & 0 & 0.042 & FAIL \\\\\nArithmetic (\\acdc{})  & 0 & $\\sim$0.038 & FAIL \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{All Qwen-2.5 0.5B configurations fail with the same pattern: near-zero Jaccard and empty consensus core.}\n\\label{tab:qwen_tasks}\n\\end{table}\n\n\\subsection{Combinatorial Dilution}\n\nThe mechanism is \\emph{combinatorial dilution}: when the edge space grows by $5.5\\times$ but circuit structure does not scale linearly, a fixed top-$k$ percentage selects non-overlapping subsets.\nAt GPT-2 scale, top-0.3\\% yields $\\sim$100 edges from a 32k pool; at Qwen scale, $\\sim$538 edges from 179k.\nThe IOI circuit distributes across more layers and heads in the larger model, and each method traces a different subset of the expanded computation paths.\n\nExtrapolating the Jaccard decay ($0.307 \\to 0.042$ over $5.5\\times$ edge space growth), models at Gemma-2 2B scale ($\\sim$500k edges) would yield $J_{\\max} \\approx 0.01$, and LLaMA-3.1 8B ($\\sim$2M edges) would approach random intersection baselines ($J \\approx 0.003$).\nWe did not run these experiments, as the scaling trend is already clear.\n\n% ============================================================\n\\section{Comparison with \\circus{}}\n\\label{sec:circus}\n\n\\circus{} \\citep{parekh2026circus} constructs consensus \\emph{within} a single method by varying the pruning threshold.\nWe compare both consensus approaches on GPT-2 tasks (Table~\\ref{tab:circus}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{IOI CPR} & \\textbf{SVA CPR} & \\textbf{Arith CPR} & \\textbf{Tasks $+$} \\\\\n\\midrule\n\\circus{}      & $-0.108$ & $-0.150$ & $-0.120$ & 0/3 \\\\\n\\css{}$= 1.0$  & $+0.109$ & $-0.820$ & $-0.184$ & 1/3 \\\\\nBest single    & $+0.029$ & $-0.348$ & $-0.131$ & 0/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Comparison with \\circus{} (zero ablation). Both consensus methods are severely limited. \\circus{} fails on all tasks; \\css{} succeeds only on IOI.}\n\\label{tab:circus}\n\\end{table}\n\n\\circus{} produces negative CPR on all three tasks, performing worse than random ablation.\nIts within-method threshold sweep constructs nested sets ($k{=}50 \\subset k{=}100 \\subset k{=}150$) whose intersection equals the most conservative cut---it cannot leverage cross-method information.\n\\css{} outperforms \\circus{} on IOI where methods genuinely disagree, but neither method provides reliable consensus on the majority of tasks.\n\n% ============================================================\n\\section{Jaccard as a Diagnostic}\n\\label{sec:jaccard}\n\nGiven that \\css{} fails when methods are too similar (high Jaccard) or too different (low Jaccard at scale), we examine whether pairwise Jaccard can serve as a \\emph{diagnostic} for when consensus is viable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccll}\n\\toprule\n\\textbf{Task$\\times$Model} & $\\boldsymbol{J_{\\max}}$ & \\textbf{\\css{} $\\Delta$} & \\textbf{Quality} & \\textbf{Confounds} \\\\\n\\midrule\nIOI$\\times$GPT-2     & 0.307 & $+0.080$ & confounded & isinf + zero \\\\\nSVA$\\times$GPT-2     & 0.653 & $-0.002$ & neutral    & $\\Delta \\approx$ noise \\\\\nArith$\\times$GPT-2   & 0.695 & $-0.066$ & negative   & --- \\\\\nIOI$\\times$Qwen      & 0.042 & undef.  & degenerate & \\css{}$= 1.0$ empty \\\\\nArith$\\times$Qwen    & 0.038 & undef.  & degenerate & \\css{}$= 1.0$ empty \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Jaccard--utility relationship across all task$\\times$model pairs. Only $n = 3$ valid points exist; $n = 2$ are degenerate.}\n\\label{tab:jaccard_utility}\n\\end{table}\n\nTable~\\ref{tab:jaccard_utility} reveals that with only 3 valid data points, no statistically significant correlation exists (Spearman $\\rho = -0.50$, $p = 0.67$).\nThe sole positive data point (IOI$\\times$GPT-2) is confounded and serves as a Cook's $D > 5.0$ influential point that drives the entire negative trend.\nThe Qwen data points are degenerate---\\css{} advantage is undefined when the consensus set is empty.\n\nRather than ``Jaccard predicts consensus utility,'' the data suggest a \\textbf{Goldilocks zone} hypothesis: consensus requires Jaccard high enough for non-empty intersection, yet low enough that the intersection carries information beyond any single method.\nOur experiments show that the upper bound (too-high Jaccard) manifests on GPT-2 SVA/Arithmetic, while the lower bound (too-low Jaccard) manifests on Qwen.\nThe viable zone---if it exists---is narrow and task-specific.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Analysis} & $\\boldsymbol{\\rho}$ & $\\boldsymbol{p}$ & $\\boldsymbol{n}$ & \\textbf{Interpretation} \\\\\n\\midrule\nAll valid points            & $-0.50$ & 0.67 & 3 & not significant \\\\\nRemove IOI (confounded)     & undef.  & ---  & 2 & cannot compute \\\\\nInclude Qwen ($\\Delta{=}{-}0.05$ proxy) & $-0.30$ & 0.62 & 5 & not significant \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Jaccard--utility correlation is not statistically significant under any analysis.}\n\\label{tab:correlation}\n\\end{table}\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why does IOI succeed?}\nIOI on GPT-2 is a well-studied task with a known ground-truth circuit \\citep{wang2023interpretability}.\nThe three methods discover genuinely different subsets of this circuit: \\eapig{} and \\ep{} favor different attention heads, and \\acdc{}'s greedy search identifies a distinct sparse backbone.\nThe $J_{\\max} = 0.307$ reflects real algorithmic diversity, and the 7-edge consensus core captures high-confidence edges.\nHowever, even this success is fragile: under mean ablation, the advantage drops to $+0.007$.\n\n\\paragraph{When methods are not independent.}\n\\eapig{} and \\ep{} are both gradient-based and share the same underlying signal (gradient of the patching effect).\nOn SVA, where number-tracking heads in layers 7--10 dominate, both methods converge on the same edges ($J = 0.653$).\nTrue $K$-method consensus requires methods from genuinely different algorithmic families---a condition that is harder to satisfy than it appears.\n\n\\paragraph{The scaling wall.}\nThe combinatorial dilution effect is perhaps the most significant finding.\nEdge-level consensus fundamentally assumes that different methods can ``see'' the same edges.\nIn larger models, the same behavioral circuit may be implemented through different edge-level paths, and each method discovers a different valid decomposition.\nThis is not a failure of any individual method but a structural property of edge-level analysis in deep networks.\n\n\\paragraph{Implications for mechanistic interpretability.}\nOur results suggest that edge-level binary consensus is not a viable path to more reliable circuit identification, at least not without addressing the independence and scaling challenges.\nPossible directions include: (1) consensus at the \\emph{node} (attention head) rather than edge level, where combinatorial dilution is less severe; (2) soft consensus using calibrated scores rather than binary membership; and (3) consensus conditional on method family, explicitly accounting for inter-method correlation.\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Circuit discovery.}\nActivation patching \\citep{vig2020investigating,geiger2021causal} and its automated variants \\citep{conmy2023automated,syed2023attribution,hanna2024does} identify circuits by measuring the causal effect of interventions.\n\\citet{wang2023interpretability} manually identified the IOI circuit in GPT-2.\n\n\\paragraph{Cross-method comparison.}\n\\citet{mondorf2025beyond} compared gradient-based circuit discovery methods and proposed score averaging.\nTheir work focuses on methods within the gradient family; we extend to cross-family consensus.\n\\citet{parekh2026circus} proposed \\circus{}, a within-method consensus approach using threshold diversity.\n\n\\paragraph{Circuit faithfulness evaluation.}\n\\citet{hanna2024does} introduced systematic faithfulness metrics.\nOur ablation sensitivity analysis (\\S\\ref{sec:ablation_confound}) highlights that faithfulness measurements are sensitive to the choice of ablation method---a confound that affects all circuit evaluation, not just consensus approaches.\n\n% ============================================================\n\\section{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Limited task and model coverage.}\nWe evaluate only 3 completed tasks on GPT-2 Small and 2 on Qwen-2.5 0.5B.\nThe factual recall experiment was abandoned due to task--model mismatch (GPT-2 Small baseline accuracy $= 52\\%$), and larger models (Gemma-2 2B, LLaMA-3.1 8B) were not attempted due to the established scaling trend and hardware constraints.\n\n\\paragraph{Method family diversity.}\nTwo of our three methods (\\eapig{}, \\ep{}) are gradient-based.\nThis limits the effective diversity to $K \\approx 2$ in some settings.\nA truly diverse ensemble would require methods from more distinct algorithmic families.\n\n\\paragraph{Sample size for correlation analysis.}\nWith $n = 3$ valid data points, we cannot establish statistical relationships between Jaccard and consensus utility.\nThe Goldilocks zone hypothesis remains speculative.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present a systematic empirical analysis of cross-method circuit consensus, evaluating \\css{} across multiple tasks and model scales.\nOur central finding is negative: binary edge-level consensus fails in 4 out of 5 task--model configurations, and the sole positive case (IOI on GPT-2) is confounded by binarization artifacts and ablation method bias.\n\nThree structural factors explain the failure: (1) insufficient method independence, particularly between gradient-based approaches; (2) binarization pathologies that create misleading diversity signals; and (3) combinatorial dilution that renders edge-level consensus impossible at scale.\n\nThese findings carry a constructive message: before investing in consensus-based circuit refinement, practitioners should verify that their methods produce genuinely independent evidence---measurable via pairwise Jaccard---and that the edge space is small enough for meaningful overlap.\nThe Goldilocks zone for viable consensus appears narrow, task-specific, and difficult to guarantee a priori.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "369f60a0-68b6-4993-aa06-28c69ab5b60f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T081242 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-contex…",
  "leafUuid": "55168056-ad2c-4f9f-af84-ccb0d9d36cbb",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulation paper for dream_id",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4"
}
```

---

### Assistant

_source line 22 · 2026-05-13T08:58:10.536Z_

Now compile it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55168056-ad2c-4f9f-af84-ccb0d9d36cbb",
  "isSidechain": false,
  "requestId": "req_011CazHs4X5KqKGvx2HxrZ5s",
  "type": "assistant",
  "uuid": "11699f16-b669-4f54-9aed-ba22ee857764",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F74VRm9xUjjZPwkJkPpiUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9809,
      "cache_read_input_tokens": 39330,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 39330,
          "cache_creation_input_tokens": 9809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9809
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

_source line 23 · 2026-05-13T08:58:11.679Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CRWZbzfNFv3wRZsv2z1SQ6`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11699f16-b669-4f54-9aed-ba22ee857764",
  "isSidechain": false,
  "requestId": "req_011CazHs4X5KqKGvx2HxrZ5s",
  "type": "assistant",
  "uuid": "a9576a09-74bc-4ae2-b474-60ab7b3d910e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F74VRm9xUjjZPwkJkPpiUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9809,
      "cache_read_input_tokens": 39330,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 39330,
          "cache_creation_input_tokens": 9809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9809
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

_source line 24 · 2026-05-13T08:58:11.899Z_

<details><summary>↩ Tool result · reported error · `toolu_01CRWZbzfNFv3wRZsv2z1SQ6`</summary>

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
  "parentUuid": "a9576a09-74bc-4ae2-b474-60ab7b3d910e",
  "isSidechain": false,
  "promptId": "aae39cf0-5fb2-4fec-8482-5067bb253164",
  "type": "user",
  "uuid": "69bfd8bb-926b-4f02-b095-4302e4a4ccbd",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "a9576a09-74bc-4ae2-b474-60ab7b3d910e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-13T08:58:16.366Z_

<details><summary>Logged reasoning block</summary>

```text
acl.sty is not available. Let me switch to a standard article class without the ACL style package.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69bfd8bb-926b-4f02-b095-4302e4a4ccbd",
  "isSidechain": false,
  "requestId": "req_011CazHsQBWnetJdzBp9LYCc",
  "type": "assistant",
  "uuid": "a8120da1-041b-4444-ae1d-9ba3a04048c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LbZiaybmoXmnZnZ4ebX1b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 474,
      "cache_read_input_tokens": 49139,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 474,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 469,
          "cache_read_input_tokens": 49139,
          "cache_creation_input_tokens": 474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 474
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

_source line 26 · 2026-05-13T08:58:16.367Z_

ACL style not available. I'll switch to a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8120da1-041b-4444-ae1d-9ba3a04048c5",
  "isSidechain": false,
  "requestId": "req_011CazHsQBWnetJdzBp9LYCc",
  "type": "assistant",
  "uuid": "ecd33340-155f-4d56-9cb6-1bd112b809c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LbZiaybmoXmnZnZ4ebX1b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 474,
      "cache_read_input_tokens": 49139,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 474,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 469,
          "cache_read_input_tokens": 49139,
          "cache_creation_input_tokens": 474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 474
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

_source line 27 · 2026-05-13T08:58:20.174Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01RycVbUogZ4UttkkB1NXTxQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{microtype}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{microtype}\n\\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}\n\\usepackage{natbib}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecd33340-155f-4d56-9cb6-1bd112b809c0",
  "isSidechain": false,
  "requestId": "req_011CazHsQBWnetJdzBp9LYCc",
  "type": "assistant",
  "uuid": "0ebb68b3-75db-4c0c-8afd-0933c14f5420",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LbZiaybmoXmnZnZ4ebX1b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 474,
      "cache_read_input_tokens": 49139,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 474,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 469,
          "cache_read_input_tokens": 49139,
          "cache_creation_input_tokens": 474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 474
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

_source line 28 · 2026-05-13T08:58:20.197Z_

<details><summary>↩ Tool result · `toolu_01RycVbUogZ4UttkkB1NXTxQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ebb68b3-75db-4c0c-8afd-0933c14f5420",
  "isSidechain": false,
  "promptId": "aae39cf0-5fb2-4fec-8482-5067bb253164",
  "type": "user",
  "uuid": "16c42501-b178-4d11-9816-8006cd505460",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{microtype}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{microtype}\n\\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}\n\\usepackage{natbib}",
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
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{graphicx}"
        ]
      },
      {
        "oldStart": 10,
        "oldLines": 6,
        "newStart": 10,
        "newLines": 8,
        "lines": [
          " \\usepackage{xcolor}",
          " \\usepackage{tabularx}",
          " \\usepackage{microtype}",
          "+\\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}",
          "+\\usepackage{natbib}",
          " ",
          " \\newcommand{\\css}{\\textsc{CSS}}",
          " \\newcommand{\\circus}{\\textsc{Circus}}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "0ebb68b3-75db-4c0c-8afd-0933c14f5420",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-13T08:58:20.298Z_

```json
{
  "parentUuid": "16c42501-b178-4d11-9816-8006cd505460",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3ba1294b-ac17-4cb0-971a-e28216ce3d94",
  "timestamp": "2026-05-13T08:58:20.298Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-13T08:58:23.749Z_

<details open><summary>🔧 Tool call — Edit · `toolu_014nCmgQiWspt93awRyhF1PC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliographystyle{plainnat}\n\\bibliography{references}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ba1294b-ac17-4cb0-971a-e28216ce3d94",
  "isSidechain": false,
  "requestId": "req_011CazHt1z45DAoeY2VcvABx",
  "type": "assistant",
  "uuid": "67bafd1f-b226-4da3-8f3b-972c09e4ea2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016r3gkTvRTqutNBwtThsC8s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 49613,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 49613,
          "cache_creation_input_tokens": 658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 658
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

_source line 31 · 2026-05-13T08:58:23.763Z_

<details><summary>↩ Tool result · `toolu_014nCmgQiWspt93awRyhF1PC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67bafd1f-b226-4da3-8f3b-972c09e4ea2d",
  "isSidechain": false,
  "promptId": "aae39cf0-5fb2-4fec-8482-5067bb253164",
  "type": "user",
  "uuid": "314d223c-379c-4b20-b996-6931e8e17b4c",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\bibliographystyle{plainnat}\n\\bibliography{references}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 511,
        "oldLines": 7,
        "newStart": 511,
        "newLines": 7,
        "lines": [
          " These findings carry a constructive message: before investing in consensus-based circuit refinement, practitioners should verify that their methods produce genuinely independent evidence---measurable via pairwise Jaccard---and that the edge space is small enough for meaningful overlap.",
          " The Goldilocks zone for viable consensus appears narrow, task-specific, and difficult to guarantee a priori.",
          " ",
          "+\\bibliographystyle{plainnat}",
          " \\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          " ",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "67bafd1f-b226-4da3-8f3b-972c09e4ea2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-13T08:58:26.040Z_

Now create a minimal bib file and compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "314d223c-379c-4b20-b996-6931e8e17b4c",
  "isSidechain": false,
  "requestId": "req_011CazHtH2Bo3LNVYCDhqboE",
  "type": "assistant",
  "uuid": "faea3917-253b-4a55-ad79-44e406cf817a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSb4R2DZY7oPtK85zdePtL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 50271,
      "output_tokens": 895,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 895,
          "cache_read_input_tokens": 50271,
          "cache_creation_input_tokens": 253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 253
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

_source line 33 · 2026-05-13T08:58:44.386Z_

<details open><summary>🔧 Tool call — Write · `toolu_01CaaNUJGAtaHjTE3BeVCqEz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/references.bib",
  "content": "@article{olah2020zoom,\n  title={Zoom in: An introduction to circuits},\n  author={Olah, Chris and Cammarata, Nick and Schubert, Ludwig and Goh, Gabriel and Petrov, Michael and Carter, Shan},\n  journal={Distill},\n  year={2020}\n}\n\n@inproceedings{wang2023interpretability,\n  title={Interpretability in the Wild: A Circuit for Indirect Object Identification in {GPT}-2 Small},\n  author={Wang, Kevin and Variengien, Alexandre and Conmy, Arthur and Shlegeris, Buck and Steinhardt, Jacob},\n  booktitle={ICLR},\n  year={2023}\n}\n\n@inproceedings{conmy2023automated,\n  title={Towards Automated Circuit Discovery for Mechanistic Interpretability},\n  author={Conmy, Arthur and Mavor-Parker, Augustine N and Lynch, Aengus and Heimersheim, Stefan and Garriga-Alonso, Adri{\\`a}},\n  booktitle={NeurIPS},\n  year={2023}\n}\n\n@inproceedings{syed2023attribution,\n  title={Attribution Patching Outperforms Automated Circuit Discovery},\n  author={Syed, Aaquib and Rager, Can and Conmy, Arthur},\n  booktitle={ATTRIB Workshop, NeurIPS},\n  year={2023}\n}\n\n@inproceedings{hanna2024does,\n  title={How Does {GPT}-2 Compute Greater-Than?: Interpreting Mathematical Abilities in a Pre-Trained Language Model},\n  author={Hanna, Michael and Liu, Ollie and Variengien, Alexandre},\n  booktitle={NeurIPS},\n  year={2024}\n}\n\n@article{mondorf2025beyond,\n  title={Beyond Single Methods: Comparing Circuit Discovery Approaches in Transformers},\n  author={Mondorf, Philipp and Plank, Barbara},\n  journal={arXiv preprint arXiv:2510.06811},\n  year={2025}\n}\n\n@article{parekh2026circus,\n  title={{CIRCUS}: Circuit Consensus via Threshold Diversity},\n  author={Parekh, Jayneel and others},\n  journal={arXiv preprint},\n  year={2026}\n}\n\n@inproceedings{vig2020investigating,\n  title={Investigating Gender Bias in Language Models Using Causal Mediation Analysis},\n  author={Vig, Jesse and Gehrmann, Sebastian and Belinkov, Yonatan and Qian, Sharon and Nevo, Daniel and Singer, Yaron and Shieber, Stuart},\n  booktitle={NeurIPS},\n  year={2020}\n}\n\n@inproceedings{geiger2021causal,\n  title={Causal Abstractions of Neural Networks},\n  author={Geiger, Atticus and Lu, Hanson and Icard, Thomas and Potts, Christopher},\n  booktitle={NeurIPS},\n  year={2021}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faea3917-253b-4a55-ad79-44e406cf817a",
  "isSidechain": false,
  "requestId": "req_011CazHtH2Bo3LNVYCDhqboE",
  "type": "assistant",
  "uuid": "cfd37611-f3dd-43e1-8471-cbd953e4f2b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSb4R2DZY7oPtK85zdePtL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 50271,
      "output_tokens": 895,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 895,
          "cache_read_input_tokens": 50271,
          "cache_creation_input_tokens": 253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 253
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

_source line 34 · 2026-05-13T08:58:44.400Z_

<details><summary>↩ Tool result · `toolu_01CaaNUJGAtaHjTE3BeVCqEz`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cfd37611-f3dd-43e1-8471-cbd953e4f2b1",
  "isSidechain": false,
  "promptId": "aae39cf0-5fb2-4fec-8482-5067bb253164",
  "type": "user",
  "uuid": "32b758cd-ac53-47ae-8cee-07111617514d",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/references.bib",
    "content": "@article{olah2020zoom,\n  title={Zoom in: An introduction to circuits},\n  author={Olah, Chris and Cammarata, Nick and Schubert, Ludwig and Goh, Gabriel and Petrov, Michael and Carter, Shan},\n  journal={Distill},\n  year={2020}\n}\n\n@inproceedings{wang2023interpretability,\n  title={Interpretability in the Wild: A Circuit for Indirect Object Identification in {GPT}-2 Small},\n  author={Wang, Kevin and Variengien, Alexandre and Conmy, Arthur and Shlegeris, Buck and Steinhardt, Jacob},\n  booktitle={ICLR},\n  year={2023}\n}\n\n@inproceedings{conmy2023automated,\n  title={Towards Automated Circuit Discovery for Mechanistic Interpretability},\n  author={Conmy, Arthur and Mavor-Parker, Augustine N and Lynch, Aengus and Heimersheim, Stefan and Garriga-Alonso, Adri{\\`a}},\n  booktitle={NeurIPS},\n  year={2023}\n}\n\n@inproceedings{syed2023attribution,\n  title={Attribution Patching Outperforms Automated Circuit Discovery},\n  author={Syed, Aaquib and Rager, Can and Conmy, Arthur},\n  booktitle={ATTRIB Workshop, NeurIPS},\n  year={2023}\n}\n\n@inproceedings{hanna2024does,\n  title={How Does {GPT}-2 Compute Greater-Than?: Interpreting Mathematical Abilities in a Pre-Trained Language Model},\n  author={Hanna, Michael and Liu, Ollie and Variengien, Alexandre},\n  booktitle={NeurIPS},\n  year={2024}\n}\n\n@article{mondorf2025beyond,\n  title={Beyond Single Methods: Comparing Circuit Discovery Approaches in Transformers},\n  author={Mondorf, Philipp and Plank, Barbara},\n  journal={arXiv preprint arXiv:2510.06811},\n  year={2025}\n}\n\n@article{parekh2026circus,\n  title={{CIRCUS}: Circuit Consensus via Threshold Diversity},\n  author={Parekh, Jayneel and others},\n  journal={arXiv preprint},\n  year={2026}\n}\n\n@inproceedings{vig2020investigating,\n  title={Investigating Gender Bias in Language Models Using Causal Mediation Analysis},\n  author={Vig, Jesse and Gehrmann, Sebastian and Belinkov, Yonatan and Qian, Sharon and Nevo, Daniel and Singer, Yaron and Shieber, Stuart},\n  booktitle={NeurIPS},\n  year={2020}\n}\n\n@inproceedings{geiger2021causal,\n  title={Causal Abstractions of Neural Networks},\n  author={Geiger, Atticus and Lu, Hanson and Icard, Thomas and Potts, Christopher},\n  booktitle={NeurIPS},\n  year={2021}\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "cfd37611-f3dd-43e1-8471-cbd953e4f2b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-13T08:58:48.359Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QzKtKJaq8HjeCRkVrbd2P1`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5 && bibtex paper 2>&1 | tail -5 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Full LaTeX compilation with bibtex",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32b758cd-ac53-47ae-8cee-07111617514d",
  "isSidechain": false,
  "requestId": "req_011CazHuoJ7z9AyGT1fGjjwq",
  "type": "assistant",
  "uuid": "8ff44dbb-73f5-47dd-a48b-ac7bf4e1b753",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdB1eXX9NxjvLLWKsR2qP2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 961,
      "cache_read_input_tokens": 50524,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 961,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 50524,
          "cache_creation_input_tokens": 961,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 961
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

_source line 36 · 2026-05-13T08:58:50.470Z_

<details><summary>↩ Tool result · `toolu_01QzKtKJaq8HjeCRkVrbd2P1`</summary>

```text
w/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8
a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 213849 bytes).
Transcript written on paper.log.
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: paper.aux
The style file: plainnat.bst
Database file #1: references.bib
w/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8
a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 222714 bytes).
Transcript written on paper.log.
w/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8
a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 224603 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ff44dbb-73f5-47dd-a48b-ac7bf4e1b753",
  "isSidechain": false,
  "promptId": "aae39cf0-5fb2-4fec-8482-5067bb253164",
  "type": "user",
  "uuid": "332c0370-3191-4d81-bc84-7476c1e8ca73",
  "toolUseResult": {
    "stdout": "w/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8\na.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 213849 bytes).\nTranscript written on paper.log.\nThis is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: paper.aux\nThe style file: plainnat.bst\nDatabase file #1: references.bib\nw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8\na.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 222714 bytes).\nTranscript written on paper.log.\nw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8\na.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 224603 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8ff44dbb-73f5-47dd-a48b-ac7bf4e1b753",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-13T08:59:00.941Z_

编译成功，生成 9 页 PDF。

`paper.tex` 已写入 `worst/` 目录并编译为 `paper.pdf`（9 页，225KB）。覆盖全部 9 个实验：

- **GPT-2 三任务**（IOI PASS、SVA FAIL、Arithmetic FAIL）+ Factual Recall abandoned
- **Qwen-2.5 0.5B 两任务**（IOI/Arithmetic 均 CSS=1.0 空集）
- **Top-k sensitivity sweep**（Table 5）
- **Ablation method confound**（Table 6：zero/mean/resample）
- **ACDC isinf binarization pathology**（Table 4）
- **CIRCUS 对比**（Table 7）
- **Jaccard-utility correlation**（Tables 8–9，n=3 not significant）
- **Scaling analysis**（Table 5：GPT-2 vs Qwen combinatorial dilution）

叙事已按指引 pivot 为 analysis paper："Why Cross-Method Circuit Consensus Fails"，IOI 作为唯一有效案例的 case study，三个结构性失败原因作为核心贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "332c0370-3191-4d81-bc84-7476c1e8ca73",
  "isSidechain": false,
  "requestId": "req_011CazHvFAcnAhEu5fKsN3ie",
  "type": "assistant",
  "uuid": "11012dc5-8b14-4d73-9bf1-ca047a4f9e5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShCDX9PWw9XgNV3MraUrzA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 51485,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 721,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 321,
          "cache_read_input_tokens": 51485,
          "cache_creation_input_tokens": 721,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 721
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

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T081242 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-contex…",
  "leafUuid": "11012dc5-8b14-4d73-9bf1-ca047a4f9e5e",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulation paper for dream_id",
  "sessionId": "ed25cbee-36c3-40dd-ae0a-cde849c662b4"
}
```

---
