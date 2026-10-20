# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/7c35f0a2-0423-4048-b741-51ef52323081.jsonl`
- **Structured JSON:** [`975617a6c15a5d41f09c.json`](../../sessions/97/975617a6c15a5d41f09c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T16:54:19.925Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T16:54:19.925Z",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Full-scale effect sizes collapse. Embedding-distance mining shows no reliable advantage over random baselines once multi-seed CIs are computed; dataflow negatives show no benefit or slight harm on both encoders. BM25 negatives perform statistically indistinguishable from embedding negatives, preventing closure of the CoCoHaNeRe correction argument. Pool size scaling destabilizes strategy rankings. SWE-bench shows no downstream signal. The paper must pivot to a negative-result framing: \"Why Hard Negative Mining Strategies Don't Differentiate for Code Retrieval at Scale.\" The salvageable contribution is the representation geometry analysis explaining *why* strategies converge (margins collapse post-fine-tuning), plus the methodological caution about BM25 proxies (downgraded from \"correction\" to \"observation\").\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T16:54:19.929Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T16:54:19.929Z",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-14T16:54:19.962Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Full-scale effect sizes collapse. Embedding-distance mining shows no reliable advantage over random baselines once multi-seed CIs are computed; dataflow negatives show no benefit or slight harm on both encoders. BM25 negatives perform statistically indistinguishable from embedding negatives, preventing closure of the CoCoHaNeRe correction argument. Pool size scaling destabilizes strategy rankings. SWE-bench shows no downstream signal. The paper must pivot to a negative-result framing: "Why Hard Negative Mining Strategies Don't Differentiate for Code Retrieval at Scale." The salvageable contribution is the representation geometry analysis explaining *why* strategies converge (margins collapse post-fine-tuning), plus the methodological caution about BM25 proxies (downgraded from "correction" to "observation").

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "66bbad76-7453-4fae-883a-01da252df421",
  "type": "user",
  "uuid": "0acbf50c-f45f-4ef6-bbfd-50244555a2a2",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T16:54:19.962Z_

```json
{
  "parentUuid": "0acbf50c-f45f-4ef6-bbfd-50244555a2a2",
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
  "uuid": "c0cc7ed9-b8dc-40f7-920d-c88a8c5aac3a",
  "timestamp": "2026-05-14T16:54:19.962Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T16:54:19.962Z_

```json
{
  "parentUuid": "c0cc7ed9-b8dc-40f7-920d-c88a8c5aac3a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ff485009-30b0-47c8-8a35-0fea6bdfaca3",
  "timestamp": "2026-05-14T16:54:19.962Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
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
  "aiTitle": "Hard negative mining strategies for code retrieval convergence analysis",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081"
}
```

---

### Assistant

_source line 7 · 2026-05-14T16:54:23.258Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff485009-30b0-47c8-8a35-0fea6bdfaca3",
  "isSidechain": false,
  "requestId": "req_011Cb2ozBzEmA33SZ2CqnswQ",
  "type": "assistant",
  "uuid": "ad85fbf2-cf4a-49d2-a1b4-c40d01ee91d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hx3KY4hP7WFeiKbmggY7FK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11210,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11210,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11210,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11210
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

_source line 8 · 2026-05-14T16:54:24.212Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FcWgMLdBgKdaG7sKcerUMv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad85fbf2-cf4a-49d2-a1b4-c40d01ee91d8",
  "isSidechain": false,
  "requestId": "req_011Cb2ozBzEmA33SZ2CqnswQ",
  "type": "assistant",
  "uuid": "505b6e75-c498-4a7e-9421-38c0687ca71c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hx3KY4hP7WFeiKbmggY7FK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11210,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11210,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11210,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11210
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

_source line 9 · 2026-05-14T16:54:24.394Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ZQwi9Ne2RaPuGZDPEf9HG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "505b6e75-c498-4a7e-9421-38c0687ca71c",
  "isSidechain": false,
  "requestId": "req_011Cb2ozBzEmA33SZ2CqnswQ",
  "type": "assistant",
  "uuid": "92dbf6e0-6414-4ca8-a7f2-a2777024f0e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hx3KY4hP7WFeiKbmggY7FK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11210,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11210,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11210,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11210
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

_source line 10 · 2026-05-14T16:54:24.401Z_

<details><summary>↩ Tool result · `toolu_013ZQwi9Ne2RaPuGZDPEf9HG`</summary>

```text
1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported "harm" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).
10	
11	2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.
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
23	  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance
24	  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works
25	
26	- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.
27	
28	- **Headline result template**: "True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis."
29	
30	## Core Insight
31	
32	The effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.
33	
34	## Dual-Pillar Motivation
35	
36	1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.
37	2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.
38	
39	## Formal Definition
40	
41	Given retrieval domain D, structural graph G, similarity function s, query q:
42	**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)
43	
44	The structural graph is externally fixed and does not update with the encoder (drift-immune).
45	
46	## Title Options
47	
48	- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
49	- Alternative: "StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval"
50	- Backup: "Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally"
51	
52	## Venue Fit
53	
54	1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
55	2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
56	3. **Against "incremental" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.
57	
58	## Anticipated Reviewer Concerns
59	
60	| Concern | Response | Evidence |
61	|---------|----------|----------|
62	| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |
63	| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |
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
79	- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact
80	- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction
81	- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)
82	- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only
83	- plan_006: CodeQL scalability confirmed at 123-repo scale
84	
85	### In progress:
86	- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)
87	- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)
88	- m1_reextract_v2: expanded extraction for higher coverage
89	
90	### Planned (priority order):
91	- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)
92	- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
93	- plan_019: Pool size sensitivity (Dream consensus — external validity)
94	- plan_014: Temperature ablation (Dream reviewer concern)
95	- plan_004: RepoBench-R second benchmark (with multi-seed CIs)
96	- plan_015: Dynamic mining baseline
97	- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)
98	- plan_007/008/009: Additional ablations
99	
100	## Contingency (if full M2 results weaken claims)
101	
102	### All 18 runs confirm pilot pattern: Best case
103	- Full statistical power, paper as framed above
104	- Target: EMNLP Main
105	
106	### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
107	- Drop Claim 2 to analysis observation
108	- Paper becomes: "True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions"
109	- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main
110	
111	### Embedding mining also loses advantage at full scale: Major reassessment needed
112	- Recheck data pipeline for bugs (full-scale data may have distribution differences)
113	- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
114	- Discuss with user before committing direction
115	
116	## Deprecated Claims (with reason)
117	
118	- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92dbf6e0-6414-4ca8-a7f2-a2777024f0e9",
  "isSidechain": false,
  "promptId": "66bbad76-7453-4fae-883a-01da252df421",
  "type": "user",
  "uuid": "ea411b9e-3cee-4767-b590-b7aead435329",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper_framing.md",
      "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \"harm\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).\n\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\n\n- **Headline result template**: \"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\"\n\n## Core Insight\n\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\"\n- Backup: \"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\n- m1_reextract_v2: expanded extraction for higher coverage\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  },
  "sourceToolAssistantUUID": "92dbf6e0-6414-4ca8-a7f2-a2777024f0e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-contex…",
  "leafUuid": "ea411b9e-3cee-4767-b590-b7aead435329",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Hard negative mining strategies for code retrieval convergence analysis",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081"
}
```

---

### Tool result

_source line 13 · 2026-05-14T16:54:24.561Z_

<details><summary>↩ Tool result · `toolu_01FcWgMLdBgKdaG7sKcerUMv`</summary>

```text
1	[
2	  {
3	    "name": "M2 Full Qwen 9-seed 3-strategy training",
4	    "description": "9 seeds × 3 strategies (random, embedding_distance, dataflow_aware) on Qwen2.5-Coder-3B LoRA. Full training data (~44K instances). Pool=50 eval.\n",
5	    "results": {
6	      "random_mean_R1": 0.529,
7	      "random_std_R1": 0.0085,
8	      "random_95CI": [
9	        0.5224,
10	        0.5356
11	      ],
12	      "embedding_distance_mean_R1": 0.531,
13	      "embedding_distance_std_R1": 0.0092,
14	      "embedding_distance_95CI": [
15	        0.5239,
16	        0.5381
17	      ],
18	      "dataflow_aware_mean_R1": 0.5245,
19	      "dataflow_aware_std_R1": 0.011,
20	      "dataflow_aware_95CI": [
21	        0.516,
22	        0.533
23	      ],
24	      "emb_minus_random_R1_pp": 0.2,
25	      "emb_minus_random_CI": [
26	        -0.62,
27	        1.02
28	      ],
29	      "df_minus_random_R1_pp": -0.45,
30	      "df_minus_random_CI": [
31	        -1.5,
32	        0.6
33	      ],
34	      "best_step_mode": 1000,
35	      "best_step_range": [
36	        500,
37	        1500
38	      ],
39	      "overfit_onset_step": 1500
40	    },
41	    "tables": [
42	      {
43	        "name": "Table 2: Full-Scale R@1 by Strategy × Encoder (Qwen)",
44	        "content": "Strategy          | Mean R@1 | Std   | 95% CI          | Δ vs Random | p (paired-t)\n------------------|----------|-------|-----------------|-------------|-------------\nrandom            | 0.5290   | 0.009 | [0.522, 0.536]  | —           | —\nembedding_dist    | 0.5310   | 0.009 | [0.524, 0.538]  | +0.20pp     | 0.58\ndataflow_aware    | 0.5245   | 0.011 | [0.516, 0.533]  | −0.45pp     | 0.31\n"
45	      }
46	    ],
47	    "figures": [],
48	    "analysis": "The pilot's +2.0pp embedding advantage was a seed-specific fluctuation. At full scale, the effect is +0.20pp with p=0.58 — no statistical significance. Dataflow shows a slight negative trend (−0.45pp) but also non-significant. Seed-to-seed variance (σ ≈ 0.009) exceeds the strategy effect, making it impossible to distinguish strategies on this encoder. This is consistent with Qwen's extreme representation saturation: when pos_sim=0.986, fine-tuning rapidly compresses any initial margin differences, and all strategies end up in the same loss basin.\n\n\nPilot showed emb +2.0pp over random (0.5557 vs 0.5357), but that was 1 seed on pilot-scale data. At full scale with 9 seeds, seed variance dominates the small effect. The 2.0pp pilot delta shrinks to ~0.2pp because: (1) full training data (44K vs pilot subset) gives random negatives more coverage of the embedding space, reducing the advantage of curated hard negatives; (2) Qwen's extremely saturated pretrained space (pos_sim=0.9855) means all strategies produce negatives that are very close to the query — the margin between random_neg_sim (0.911) and emb_neg_sim (0.969) gets compressed further during fine-tuning as the encoder adjusts; (3) with 9 seeds, some seeds favor random (data order effects), some favor embedding, and the mean converges. The CI clearly includes 0, killing the claim that embedding mining \"consistently improves\" retrieval. Dataflow negatives show slight harm because at full scale, the 34% structural coverage means 66% of training instances fall back to random, diluting any signal; the structural negatives for the remaining 34% may be less informative than embedding negatives (dataflow disconnection doesn't guarantee semantic difficulty).\n"
49	  },
50	  {
51	    "name": "M2 Full StarCoder 9-seed 3-strategy training",
52	    "description": "9 seeds × 3 strategies on StarCoder2-3B. Same protocol as Qwen.\n",
53	    "results": {
54	      "random_mean_R1": 0.443,
55	      "random_std_R1": 0.0105,
56	      "random_95CI": [
57	        0.4349,
58	        0.4511
59	      ],
60	      "embedding_distance_mean_R1": 0.4395,
61	      "embedding_distance_std_R1": 0.012,
62	      "embedding_distance_95CI": [
63	        0.4302,
64	        0.4488
65	      ],
66	      "dataflow_aware_mean_R1": 0.428,
67	      "dataflow_aware_std_R1": 0.0135,
68	      "dataflow_aware_95CI": [
69	        0.4176,
70	        0.4384
71	      ],
72	      "emb_minus_random_R1_pp": -0.35,
73	      "emb_minus_random_CI": [
74	        -1.4,
75	        0.7
76	      ],
77	      "df_minus_random_R1_pp": -1.5,
78	      "df_minus_random_CI": [
79	        -3.1,
80	        0.1
81	      ],
82	      "best_step_mode": 1000,
83	      "overfit_onset_step": 1500
84	    },
85	    "tables": [
86	      {
87	        "name": "Table 2 (continued): Full-Scale R@1 by Strategy × Encoder (StarCoder)",
88	        "content": "Strategy          | Mean R@1 | Std   | 95% CI          | Δ vs Random | p (paired-t)\n------------------|----------|-------|-----------------|-------------|-------------\nrandom            | 0.4430   | 0.011 | [0.435, 0.451]  | —           | —\nembedding_dist    | 0.4395   | 0.012 | [0.430, 0.449]  | −0.35pp     | 0.47\ndataflow_aware    | 0.4280   | 0.014 | [0.418, 0.438]  | −1.50pp     | 0.015\n"
89	      }
90	    ],
91	    "figures": [],
92	    "analysis": "StarCoder's full-scale results are worse than Qwen overall (R@1 ~0.44 vs ~0.53), consistent with decoder-only FIM pretraining being less suited for bidirectional retrieval. Critically, embedding mining does not help — the sign flipped from pilot (+1.56pp → −0.35pp). Dataflow shows possible harm (p=0.015), but with 9 comparisons across the study, this doesn't survive multiple-testing correction (Bonferroni threshold ~0.006). The dominant finding is that no strategy differentiates reliably. Combined with Qwen, neither encoder shows a strategy effect that survives multi-seed evaluation.\n\n\nStarCoder pilot showed embedding +1.56pp (0.5078 vs 0.4922), but pilot used post-hoc eval for random (no in-training eval), introducing measurement inconsistency. At full scale with 9 seeds and consistent eval: (1) StarCoder's healthier pretrained geometry (pos_sim=0.80) means random negatives already provide decent margin (0.194), so embedding mining's tighter margins (0.067) may actually hurt by making the contrastive task too hard early in training, causing some seeds to find worse optima; (2) the higher seed variance for StarCoder (σ=0.012 vs Qwen's 0.009) reflects the decoder-only architecture's sensitivity to initialization — FIM pretraining creates a less smooth loss landscape for retrieval fine-tuning; (3) dataflow negatives show the most harm (−1.50pp) because StarCoder's intact geometry already separates structural from non-structural code well, so forcing structural discrimination adds noise rather than signal. The CI for embedding nearly spans zero but slightly favors negative; for dataflow, the CI upper bound just barely touches zero, suggesting possible marginal harm.\n"
93	  },
94	  {
95	    "name": "M3a SWE-bench Lite end-to-end evaluation",
96	    "description": "3 strategies × best checkpoint per encoder, evaluated on SWE-bench Lite (300 instances) with Qwen3.6-27B agent. Measures resolve rate.\n",
97	    "results": {
98	      "qwen_random_resolve_rate": 0.2467,
99	      "qwen_embedding_resolve_rate": 0.25,
100	      "qwen_dataflow_resolve_rate": 0.2433,
101	      "starcoder_random_resolve_rate": 0.2267,
102	      "starcoder_embedding_resolve_rate": 0.2233,
103	      "starcoder_dataflow_resolve_rate": 0.22,
104	      "best_minus_worst_pp": 0.67,
105	      "swebench_resolve_rate_delta_pp": 0.33,
106	      "qwen_emb_minus_random_delta_pp": 0.33,
107	      "starcoder_emb_minus_random_delta_pp": -0.34
108	    },
109	    "tables": [
110	      {
111	        "name": "Table 4: SWE-bench Lite Resolve Rate",
112	        "content": "Encoder   | Strategy   | Resolve Rate | Δ vs Random | 95% Binom CI\n----------|------------|-------------|-------------|------------------\nQwen      | random     | 24.67%      | —           | [19.9%, 29.4%]\nQwen      | embedding  | 25.00%      | +0.33pp     | [20.2%, 29.8%]\nQwen      | dataflow   | 24.33%      | −0.33pp     | [19.6%, 29.1%]\nStarCoder | random     | 22.67%      | —           | [18.0%, 27.3%]\nStarCoder | embedding  | 22.33%      | −0.34pp     | [17.7%, 27.0%]\nStarCoder | dataflow   | 22.00%      | −0.67pp     | [17.3%, 26.7%]\n"
113	      }
114	    ],
115	    "figures": [],
116	    "analysis": "No downstream differentiation. The largest gap (Qwen-embedding vs StarCoder-dataflow) is 2.8pp, which is well within the ±5pp binomial CI. This confirms the worst-case prediction: when retrieval strategy differences are <0.5pp, the downstream task cannot detect them. The paper cannot claim any practical benefit from mining strategy choice. SWE-bench results must be reported transparently as showing no differentiation, which strengthens the negative-result narrative (\"practitioners need not invest GPU time in fancy mining\").\n\n\nSWE-bench resolve rate is dominated by the LLM agent's reasoning ability, not retrieval quality. The retrieval step provides a candidate set, but the agent re-ranks and explores beyond the initial retrieval. With R@1 differences of <0.5pp at pool=50, the downstream task absorbs the noise entirely. Quantitatively: (1) at resolve rates of ~24%, a 1pp R@1 improvement translates to at most ~0.3pp resolve rate improvement (retrieval → localization → patch → test is a multi-stage pipeline where errors compound but also get corrected by the agent); (2) with 300 instances, the binomial CI for a 24% resolve rate is ±4.8pp — any sub-1pp strategy difference is invisible; (3) the agent's exploration strategy (re-reading files, searching for imports) effectively compensates for missed retrievals, especially for the dataflow-relevant cases where structural dependencies guide the agent's natural exploration. The numbers bounce randomly around ~24% with no interpretable pattern.\n"
117	  },
118	  {
119	    "name": "M3b RepoBench-R cross-file retrieval evaluation",
120	    "description": "Retrieval-only evaluation on RepoBench-R (test_easy ~8K, test_hard ~8K). 3 strategies × 2 encoders × 9 seeds. Report R@1 with 95% bootstrap CIs.\n",
121	    "results": {
122	      "qwen_easy_random_mean_R1": 0.712,
123	      "qwen_easy_embedding_mean_R1": 0.715,
124	      "qwen_easy_dataflow_mean_R1": 0.709,
125	      "qwen_hard_random_mean_R1": 0.431,
126	      "qwen_hard_embedding_mean_R1": 0.434,
127	      "qwen_hard_dataflow_mean_R1": 0.427,
128	      "starcoder_easy_random_mean_R1": 0.685,
129	      "starcoder_easy_embedding_mean_R1": 0.681,
130	      "starcoder_easy_dataflow_mean_R1": 0.678,
131	      "starcoder_hard_random_mean_R1": 0.398,
132	      "starcoder_hard_embedding_mean_R1": 0.393,
133	      "starcoder_hard_dataflow_mean_R1": 0.389,
134	      "repobench_R1_delta_pp": 0.3,
135	      "bootstrap_CI_width_R1_pp": 3.5
136	    },
137	    "tables": [
138	      {
139	        "name": "Table 5: RepoBench-R R@1 by Strategy × Encoder × Split",
140	        "content": "Split | Encoder   | random       | embedding    | dataflow     | Δ emb-rand\n------|-----------|-------------|-------------|-------------|------------\neasy  | Qwen      | 71.2 ± 1.4  | 71.5 ± 1.5  | 70.9 ± 1.6  | +0.3pp\neasy  | StarCoder | 68.5 ± 1.6  | 68.1 ± 1.7  | 67.8 ± 1.8  | −0.4pp\nhard  | Qwen      | 43.1 ± 2.0  | 43.4 ± 2.1  | 42.7 ± 2.2  | +0.3pp\nhard  | StarCoder | 39.8 ± 2.2  | 39.3 ± 2.4  | 38.9 ± 2.5  | −0.5pp\nNote: ± indicates 95% bootstrap CI half-width. All CIs overlap across strategies.\n"
141	      }
142	    ],
143	    "figures": [],
144	    "analysis": "RepoBench-R confirms the SWE-smith full-scale finding: no strategy reliably differentiates on an external benchmark. The inconsistent sign across encoders (positive for Qwen, negative for StarCoder) is the signature of noise, not signal. CI widths of 3–5pp completely swamp the 0.3–0.5pp strategy effects. This external validation strengthens the negative-result claim: strategy choice doesn't matter even when measured on a different benchmark with different pool sizes and task formulation.\n\n\nRepoBench-R uses naturally small pools (~6 for easy, ~18 for hard), which compresses retrieval difficulty. At pool=6, even a mediocre encoder achieves high R@1 (>0.70 on easy), leaving little room for strategy differentiation. The training data (SWE-smith) and eval data (RepoBench-R) come from different distributions — SWE-smith is bug-fix focused while RepoBench is cross-file completion — so training signal transfer is lossy. With 9 seeds and bootstrap CIs, the inter-seed variance (~2-3pp) dwarfs the strategy effect (<0.5pp). The hard split shows more variance but still no consistent direction: embedding helps Qwen by 0.3pp but hurts StarCoder by 0.5pp, consistent with the full-scale result that strategy effects are noise. Dataflow shows slight consistent harm because the structural signal from SWE-smith repos doesn't transfer to RepoBench's different repo distribution.\n"
145	  },
146	  {
147	    "name": "Stratified analysis: 5-stratum deep dive",
148	    "description": "5 strata: (1) repo size, (2) pool size, (3) query-positive similarity, (4) structural data availability (34% vs 66%), (5) neg_difficulty quartile. Report per-stratum R@1 deltas for all 3 strategies × 2 encoders.\n",
149	    "results": {
150	      "struct_available_emb_minus_random_qwen": 0.15,
151	      "struct_available_df_minus_random_qwen": 0.4,
152	      "struct_fallback_emb_minus_random_qwen": 0.25,
153	      "struct_fallback_df_minus_random_qwen": -0.9,
154	      "neg_diff_Q1_easy_emb_delta": 0.6,
155	      "neg_diff_Q4_hard_emb_delta": -0.3,
156	      "repo_small_emb_delta": 0.8,
157	      "repo_large_emb_delta": -0.15,
158	      "pool_small_emb_delta": 0.35,
159	      "pool_large_emb_delta": -0.2,
160	      "no_stratum_significant_after_correction": true
161	    },
162	    "tables": [
163	      {
164	        "name": "Table 6: Per-Stratum Δ(embedding − random) R@1 (Qwen, pp)",
165	        "content": "Stratum                  | N instances | Δ R@1 (pp) | 95% CI         | Sig?\n-------------------------|-------------|-----------|----------------|-----\nRepo small (<200)        |  4596       | +0.80     | [−1.5, +3.1]   | No\nRepo large (≥200)        | 39577       | −0.15     | [−0.9, +0.6]   | No\nPool small (<30)         | 12044       | +0.35     | [−1.2, +1.9]   | No\nPool large (≥30)         | 32129       | −0.20     | [−1.0, +0.6]   | No\nHigh q-pos sim (>0.95)   | 28800       | −0.10     | [−0.8, +0.6]   | No\nLow q-pos sim (≤0.95)    | 15373       | +0.55     | [−0.9, +2.0]   | No\nStruct available (34%)   | 15133       | +0.15     | [−1.2, +1.5]   | No\nStruct fallback (66%)    | 29040       | +0.25     | [−0.5, +1.0]   | No\nNeg diff Q1 (easiest)    | 11043       | +0.60     | [−1.5, +2.7]   | No\nNeg diff Q4 (hardest)    | 11043       | −0.30     | [−2.3, +1.7]   | No\n"
166	      }
167	    ],
168	    "figures": [],
169	    "analysis": "No stratum produces a significant strategy effect after Bonferroni correction (10 comparisons, α=0.005). The structural availability stratum is the most informative: it shows that the 34% with real structural data has a tiny positive dataflow signal, but this is completely washed out by the 66% fallback. This is actually a useful finding for the negative-result paper: it suggests that structural negative mining *might* help if structural data coverage were higher (>80%), but at practical extraction rates (34%), the benefit is undetectable. This becomes an actionable takeaway: \"invest in extraction coverage before investing in mining strategy.\"\n\n\nStratified analysis reveals that the aggregate null result masks opposing sub-population effects that cancel out — but none are individually significant after multiple-testing correction. Structural data stratum: the 34% with dataflow data shows a tiny positive df effect (+0.4pp), but the 66% fallback (which uses random negatives labeled as \"dataflow\") dilutes and reverses it. This is expected because the fallback mechanism means the \"dataflow\" strategy is actually ~66% random, making the aggregate comparison (dataflow vs random) a comparison of (0.34×structural + 0.66×random) vs (1.0×random). The 34% pure structural signal is too diluted to surface. Neg_difficulty quartiles: the easiest quartile (Q1, high margin) shows slight embedding advantage because the encoder can exploit the difficulty gradient; the hardest quartile (Q4, near-zero margin) shows slight embedding harm because those negatives are false-negative-adjacent (too similar to be true negatives). But with 9 seeds, the per-quartile CIs are wide (~5pp) because each quartile has only ~25% of the data. Repo size and pool size strata show similar noisy, contradictory patterns.\n"
170	  },
171	  {
172	    "name": "Temperature ablation: τ ∈ {0.05, 0.1, 0.2}",
173	    "description": "3 temperatures × 3 strategies × 2 encoders. Tests whether the null result is regime-specific to τ=0.05.\n",
174	    "results": {
175	      "tau_005_emb_minus_random_qwen": 0.2,
176	      "tau_010_emb_minus_random_qwen": 0.35,
177	      "tau_020_emb_minus_random_qwen": -0.1,
178	      "tau_005_emb_minus_random_starcoder": -0.35,
179	      "tau_010_emb_minus_random_starcoder": 0.15,
180	      "tau_020_emb_minus_random_starcoder": -0.55,
181	      "best_tau_overall": 0.05,
182	      "strategy_ranking_changes_across_tau": true,
183	      "any_tau_significant": false
184	    },
185	    "tables": [
186	      {
187	        "name": "Table A1: Temperature × Strategy Interaction (R@1, Qwen)",
188	        "content": "τ    | random | embedding | dataflow | Δ emb-rand | Δ df-rand\n-----|--------|-----------|----------|-----------|----------\n0.05 | 0.5290 | 0.5310    | 0.5245   | +0.20     | −0.45\n0.10 | 0.5215 | 0.5250    | 0.5200   | +0.35     | −0.15\n0.20 | 0.5040 | 0.5030    | 0.5015   | −0.10     | −0.25\n"
189	      }
190	    ],
191	    "figures": [],
192	    "analysis": "Temperature ablation confirms the null result is not regime-specific. The best overall R@1 is at τ=0.05 (sharpest), but strategy differences remain noise-level at all temperatures. τ=0.2 degrades all strategies uniformly by ~2.5pp, consistent with known contrastive learning theory (too-warm temperatures lose discriminative power). The instability of strategy rankings across τ is itself evidence against a true strategy effect — a real signal would produce consistent rankings regardless of temperature. Report in appendix as robustness check.\n\n\nTemperature controls the sharpness of the contrastive loss. At τ=0.05 (current), the loss is very sharp and the hardest negatives dominate the gradient — this should maximally differentiate strategies. If strategies don't differentiate at τ=0.05, they're unlikely to at τ=0.1 or 0.2 (where the loss is smoother and hard negatives matter less). The results confirm this: τ=0.1 shows slightly larger positive deltas for Qwen (the warmer loss surface allows more exploration), but still non-significant. τ=0.2 makes the loss too smooth, suppressing all hard-negative signal. Importantly, strategy rankings are unstable across τ: embedding beats random at τ=0.1 but loses at τ=0.2, confirming that the null result is not an artifact of temperature choice — there is genuinely no robust strategy advantage.\n"
193	  },
194	  {
195	    "name": "Dynamic embedding mining baseline",
196	    "description": "Re-mine embedding negatives per epoch vs static (mine once from pretrained). 1 seed × 2 encoders. Tests whether static mining confound explains null result.\n",
197	    "results": {
198	      "qwen_dynamic_R1": 0.5315,
199	      "qwen_static_R1": 0.531,
200	      "qwen_dynamic_minus_static_pp": 0.05,
201	      "starcoder_dynamic_R1": 0.44,
202	      "starcoder_static_R1": 0.4395,
203	      "starcoder_dynamic_minus_static_pp": 0.05,
204	      "mining_time_overhead_pct": 340
205	    },
206	    "tables": [
207	      {
208	        "name": "Table A2: Static vs Dynamic Mining",
209	        "content": "Encoder   | Static R@1 | Dynamic R@1 | Δ (pp) | Time overhead\n----------|-----------|------------|--------|-------------\nQwen      | 0.5310    | 0.5315     | +0.05  | +340%\nStarCoder | 0.4395    | 0.4400     | +0.05  | +340%\n"
210	      }
211	    ],
212	    "figures": [],
213	    "analysis": "Dynamic mining is a non-factor. The encoder doesn't change enough during LoRA fine-tuning to make dynamic negatives meaningfully different from static ones. This rules out the confound that our null result is caused by stale negatives. For the negative-result paper, this is useful: \"even the theoretically optimal mining schedule (dynamic) cannot rescue strategy differentiation.\"\n\n\nDynamic mining re-computes negatives using the current encoder state each epoch, so negatives should be harder (adapted to the learned representation). However, in the worst case, this doesn't help because: (1) the encoder barely moves during 3 epochs of LoRA fine-tuning — the pretrained representation is 99% preserved, so dynamic and static negatives are nearly identical (the cosine similarity between epoch-0 and epoch-3 embeddings for any given sample is >0.995); (2) any benefit from harder negatives is offset by training instability (the loss landscape shifts each epoch, preventing convergence to a stable optimum); (3) the 3.4× time overhead (re-encoding 44K instances per epoch) makes this impractical for no gain. The delta of +0.05pp for both encoders is effectively zero, confirming that the null result is not an artifact of static mining.\n"
214	  },
215	  {
216	    "name": "Bootstrap CI for SWE-bench Lite resolve rates",
217	    "description": "10,000 bootstrap resamples for each strategy's resolve rate on SWE-bench Lite (300 instances). Tests statistical significance of resolve rate deltas.\n",
218	    "results": {
219	      "qwen_random_resolve_rate": 0.2467,
220	      "qwen_random_bootstrap_CI": [
221	        0.198,
222	        0.296
223	      ],
224	      "qwen_embedding_resolve_rate": 0.25,
225	      "qwen_embedding_bootstrap_CI": [
226	        0.201,
227	        0.299
228	      ],
229	      "qwen_dataflow_resolve_rate": 0.2433,
230	      "qwen_dataflow_bootstrap_CI": [
231	        0.196,
232	        0.292
233	      ],
234	      "emb_minus_random_bootstrap_CI": [
235	        -0.048,
236	        0.055
237	      ],
238	      "df_minus_random_bootstrap_CI": [
239	        -0.055,
240	        0.048
241	      ],
242	      "any_comparison_significant": false,
243	      "bootstrap_CI_width_pp": 4.9
244	    },
245	    "tables": [
246	      {
247	        "name": "Table 4 (extended): Bootstrap CIs for SWE-bench Resolve Rates",
248	        "content": "Comparison              | Δ (pp) | Bootstrap 95% CI | p-value\n------------------------|--------|------------------|--------\nQwen emb − random       | +0.33  | [−4.8, +5.5]    | 0.89\nQwen df − random        | −0.33  | [−5.5, +4.8]    | 0.89\nSC emb − random         | −0.34  | [−5.5, +4.8]    | 0.89\nSC df − random          | −0.67  | [−5.8, +4.5]    | 0.80\n"
249	      }
250	    ],
251	    "figures": [],
252	    "analysis": "Bootstrap CIs formalize what the point estimates already suggest: SWE-bench cannot discriminate between mining strategies at the effect sizes observed. This is not a power problem we can fix — it's a fundamental limitation of using 300-instance downstream evaluation to detect <1pp retrieval differences. For the negative-result paper, this motivates the argument that practitioners should not over-invest in mining strategy optimization based on downstream benchmarks.\n\n\nWith 300 binary outcomes and a base rate of ~25%, the binomial standard error is √(0.25×0.75/300) = 0.025, giving a 95% CI half-width of ~5pp. The strategy deltas (<0.5pp) are 10× smaller than the CI width. Bootstrap resampling confirms the analytical calculation: all pairwise CIs include zero, with p-values >0.5. This is the expected worst-case outcome: SWE-bench's small N makes it impossible to detect sub-1pp retrieval differences in downstream task performance. Even a \"true\" 0.5pp retrieval improvement would need N≈60,000 instances to detect at α=0.05 in downstream resolve rate.\n"
253	  },
254	  {
255	    "name": "BM25 negative baseline",
256	    "description": "Mine BM25-based hard negatives as 4th strategy. Train ≥1 seed × 2 encoders. Compare R@1 with random/embedding/dataflow to test whether BM25 negatives match embedding negatives (which would prevent closing the CoCoHaNeRe argument).\n",
257	    "results": {
258	      "qwen_bm25_R1": 0.5275,
259	      "qwen_bm25_95CI": [
260	        0.515,
261	        0.54
262	      ],
263	      "starcoder_bm25_R1": 0.437,
264	      "starcoder_bm25_95CI": [
265	        0.42,
266	        0.454
267	      ],
268	      "qwen_bm25_minus_random_pp": -0.15,
269	      "starcoder_bm25_minus_random_pp": -0.6,
270	      "qwen_bm25_minus_embedding_pp": -0.35,
271	      "starcoder_bm25_minus_embedding_pp": -0.25,
272	      "bm25_vs_embedding_p_value_qwen": 0.42,
273	      "bm25_vs_embedding_p_value_starcoder": 0.55,
274	      "bm25_minus_random_R1_pp": -0.38,
275	      "bm25_minus_random_CI": [
276	        -1.5,
277	        0.7
278	      ]
279	    },
280	    "tables": [
281	      {
282	        "name": "Table 3: 4-Strategy Comparison Including BM25 Baseline",
283	        "content": "Encoder   | random | embedding | dataflow | BM25   | BM25−emb (pp) | p\n----------|--------|-----------|----------|--------|---------------|------\nQwen      | 0.5290 | 0.5310    | 0.5245   | 0.5275 | −0.35         | 0.42\nStarCoder | 0.4430 | 0.4395    | 0.4280   | 0.4370 | −0.25         | 0.55\n"
284	      }
285	    ],
286	    "figures": [],
287	    "analysis": "The BM25 baseline delivers the worst possible outcome for the paper's original framing. BM25 ≈ embedding negatives means we cannot attribute CoCoHaNeRe's reported harm to their BM25-proxy methodology. The \"correction\" claim must be downgraded to an \"observation\": \"We note that CoCoHaNeRe's reported large negative effect (−27pp) was not reproduced in our controlled setup with either BM25 or embedding negatives, suggesting the effect may be attributable to other experimental differences (scale, encoder, evaluation protocol) rather than the BM25-vs-embedding distinction specifically.\" This is much weaker than the original Claim 1 framing. For the negative-result paper, this finding actually strengthens the narrative: even the BM25-vs-embedding distinction that motivated the study turns out to be illusory at scale.\n\n\nThe worst case for the CoCoHaNeRe correction argument: BM25 negatives perform similarly to embedding negatives, making it impossible to claim that BM25-proxy was the source of CoCoHaNeRe's reported harm. Why this happens: (1) at full scale with 44K training instances, BM25 top-k negatives and embedding-distance top-k negatives have ~60% overlap — high-BM25 documents tend to also have high embedding similarity because both capture lexical/semantic relatedness; (2) the non-overlapping 40% doesn't create enough differential training signal to separate the strategies; (3) CoCoHaNeRe's reported -27pp harm was likely driven by other confounds (different training data scale, different encoder, different evaluation protocol) not captured by the BM25-vs-embedding distinction alone. In the worst case, BM25 negatives are slightly worse than random (−0.15pp Qwen, −0.60pp StarCoder) but the CIs include zero and overlap completely with embedding CIs. The CoCoHaNeRe correction argument cannot be closed: we can say \"BM25 and embedding negatives produce similar results in our setup\" but not \"BM25-proxy caused the harm.\"\n"
288	  },
289	  {
290	    "name": "Pool size sensitivity analysis",
291	    "description": "Evaluate strategy rankings at pool={50, 100, 200, 500} using M2 best checkpoints on SWE-smith validation.\n",
292	    "results": {
293	      "pool_50": {
294	        "qwen_random_R1": 0.529,
295	        "qwen_embedding_R1": 0.531,
296	        "ranking": [
297	          "embedding",
298	          "random",
299	          "dataflow"
300	        ]
301	      },
302	      "pool_100": {
303	        "qwen_random_R1": 0.412,
304	        "qwen_embedding_R1": 0.4085,
305	        "ranking": [
306	          "random",
307	          "embedding",
308	          "dataflow"
309	        ]
310	      },
311	      "pool_200": {
312	        "qwen_random_R1": 0.324,
313	        "qwen_embedding_R1": 0.3265,
314	        "ranking": [
315	          "embedding",
316	          "dataflow",
317	          "random"
318	        ]
319	      },
320	      "pool_500": {
321	        "qwen_random_R1": 0.231,
322	        "qwen_embedding_R1": 0.2285,
323	        "ranking": [
324	          "random",
325	          "dataflow",
326	          "embedding"
327	        ]
328	      },
329	      "pool_ranking_stable_pct": 25,
330	      "ranking_flips": 3,
331	      "kendall_tau_50_vs_500": 0.33
332	    },
333	    "tables": [
334	      {
335	        "name": "Table 7: Strategy Ranking Stability Across Pool Sizes (Qwen)",
336	        "content": "Pool | random R@1 | emb R@1  | df R@1   | Best strategy | Rank = pool50?\n-----|-----------|----------|----------|---------------|---------------\n50   | 0.5290    | 0.5310   | 0.5245   | embedding     | (reference)\n100  | 0.4120    | 0.4085   | 0.4050   | random        | No\n200  | 0.3240    | 0.3265   | 0.3250   | embedding     | Yes\n500  | 0.2310    | 0.2285   | 0.2295   | random        | No\n"
337	      },
338	      {
339	        "name": "Table 7b: Strategy Ranking Stability (StarCoder)",
340	        "content": "Pool | random R@1 | emb R@1  | df R@1   | Best strategy | Rank = pool50?\n-----|-----------|----------|----------|---------------|---------------\n50   | 0.4430    | 0.4395   | 0.4280   | random        | (reference)\n100  | 0.3410    | 0.3380   | 0.3310   | random        | Yes\n200  | 0.2620    | 0.2640   | 0.2590   | embedding     | No\n500  | 0.1780    | 0.1750   | 0.1770   | random        | Yes\n"
341	      }
342	    ],
343	    "figures": [],
344	    "analysis": "Pool size sensitivity confirms the worst case: strategy rankings are unstable. Rankings flip 3 times across 4 pool sizes, with stability at only 25%. This means the paper's strategy comparison is contingent on the evaluation protocol, not a property of the strategies themselves. For the negative-result paper, this is a strong finding: \"strategy rankings are not robust to pool size choice, suggesting that reported differences in prior work may also be evaluation artifacts.\" The practical takeaway: don't optimize mining strategy based on a single pool size — the ranking you find may not hold at deployment scale.\n\n\nPool size sensitivity exposes the fragility of strategy rankings. At pool=50 (current), embedding slightly leads — but this is the artificial setting. As pool grows: (1) the absolute R@1 drops substantially because finding the gold file among 200 or 500 candidates is genuinely harder; (2) strategy rankings become unstable because the relative ordering depends on which specific distractor files are added to the pool — at pool=500, many repos don't have 500 files, so padding strategies introduce noise; (3) the models were trained with pool sizes effectively set by the negative sampling (3 negatives → effective pool ~4), so they're not calibrated for large-pool ranking; (4) the ranking instability (Kendall τ = 0.33 between pool=50 and pool=500) means the strategy comparison is not robust to evaluation protocol choices. Only 25% of the time does the pool=50 ranking agree with other pool sizes — well below the 50% threshold that would indicate stability.\n"
345	  },
346	  {
347	    "name": "Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding",
348	    "description": "Test whether expanding call-graph scope (1/2/3-hop) changes dataflow negative quality. 1 seed × Qwen.\n",
349	    "results": {
350	      "hop1_R1": 0.523,
351	      "hop2_R1": 0.5245,
352	      "hop3_R1": 0.521,
353	      "hop2_minus_hop1_pp": 0.15,
354	      "hop3_minus_hop2_pp": -0.35
355	    },
356	    "tables": [
357	      {
358	        "name": "Table A3: Hop Count Ablation (Qwen, dataflow strategy)",
359	        "content": "Hops | Connected files/query | Negatives available | R@1    | Δ vs random\n-----|----------------------|--------------------|---------|-----------\n1    | 2.1                  | 47.9               | 0.5230 | −0.60pp\n2    | 4.8                  | 45.2               | 0.5245 | −0.45pp\n3    | 11.3                 | 38.7               | 0.5210 | −0.80pp\n"
360	      }
361	    ],
362	    "figures": [],
363	    "analysis": "Hop count ablation is uninformative in the worst case — it's optimizing within a strategy that doesn't work. The only useful observation: 3-hop over-expansion is slightly worse, suggesting that very broad connectivity definitions reduce negative quality. But the effect is tiny (0.35pp) and this entire analysis is moot given the overarching null result. Relegate to appendix.\n\n\nIn the worst case, hop count doesn't matter because the dataflow strategy itself doesn't differentiate from random. 1-hop produces the most conservative connected set (fewer files connected → more negatives available → negatives are closer to embedding-based selection). 2-hop (current) is slightly better because it captures inter-procedural dependencies. 3-hop over-expands the connected set, marking too many files as connected and leaving fewer high-quality negatives. But all three are within noise of each other and within noise of random (0.5290), confirming that the structural signal pathway is not the bottleneck — the bottleneck is that no mining strategy differentiates at scale.\n"
364	  },
365	  {
366	    "name": "Ablation: training data size scaling",
367	    "description": "1K vs 3K vs 5K (full) training instances, all 3 strategies, 1 seed × Qwen. Tests whether strategy effects are scale-dependent.\n",
368	    "results": {
369	      "size_1K": {
370	        "random_R1": 0.505,
371	        "embedding_R1": 0.518,
372	        "dataflow_R1": 0.512,
373	        "emb_minus_random_pp": 1.3
374	      },
375	      "size_3K": {
376	        "random_R1": 0.52,
377	        "embedding_R1": 0.526,
378	        "dataflow_R1": 0.521,
379	        "emb_minus_random_pp": 0.6
380	      },
381	      "size_5K": {
382	        "random_R1": 0.529,
383	        "embedding_R1": 0.531,
384	        "dataflow_R1": 0.5245,
385	        "emb_minus_random_pp": 0.2
386	      },
387	      "effect_trend": "strategy advantage monotonically decreases with scale"
388	    },
389	    "tables": [
390	      {
391	        "name": "Table 8: Scale-Dependent Strategy Effects",
392	        "content": "Train size | random R@1 | embedding R@1 | Δ (pp) | df R@1  | Δ df-rand (pp)\n-----------|-----------|--------------|--------|---------|---------------\n1K         | 0.5050    | 0.5180       | +1.30  | 0.5120  | +0.70\n3K         | 0.5200    | 0.5260       | +0.60  | 0.5210  | +0.10\n5K (full)  | 0.5290    | 0.5310       | +0.20  | 0.5245  | −0.45\n"
393	      }
394	    ],
395	    "figures": [],
396	    "analysis": "This is the paper's most compelling experiment. The scale-dependent effect provides the mechanistic story: hard negative mining helps at small scale but its advantage vanishes as random sampling catches up. This connects to the representation geometry analysis: at small scale, random negatives are too easy (high margin) and the encoder doesn't learn the decision boundary well. As scale increases, random negatives include enough hard examples by chance. This reframes the negative result as a positive finding: \"scale is a substitute for curation in contrastive code retrieval.\" Actionable takeaway: if your training set is small (<2K), invest in mining; if large (>5K), random suffices.\n\n\nThis is the most important ablation for the negative-result narrative. At 1K instances (pilot-like scale), embedding mining shows a +1.3pp advantage — close to the pilot's +2.0pp, confirming that the pilot finding was real but scale-dependent. As training data increases to 3K and 5K, the advantage shrinks to 0.6pp and 0.2pp respectively. Mechanism: with more training data, the random negatives sample a wider swath of the embedding space, effectively approximating what curated embedding negatives provide. At small scale, curated negatives concentrate the training signal on the decision boundary; at large scale, random sampling covers the boundary adequately through sheer volume. This is a well-known phenomenon in contrastive learning (cf. SimCLR batch size scaling) and provides the mechanistic explanation for why pilot results didn't replicate at full scale.\n"
397	  },
398	  {
399	    "name": "Ablation: fusion head (embedding-only vs structural-only vs combined)",
400	    "description": "Test whether adding structural features at inference time helps. 3 heads × best checkpoint × Qwen.\n",
401	    "results": {
402	      "embedding_only_R1": 0.531,
403	      "structural_only_R1": 0.312,
404	      "combined_R1": 0.5285,
405	      "combined_minus_embedding_pp": -0.25
406	    },
407	    "tables": [
408	      {
409	        "name": "Table A4: Fusion Head Ablation (Qwen)",
410	        "content": "Head           | R@1    | R@5    | R@10   | Δ vs emb-only\n---------------|--------|--------|--------|--------------\nEmbedding only | 0.5310 | 0.9600 | 1.000  | —\nStructural only| 0.3120 | 0.6200 | 0.780  | −21.9pp\nCombined       | 0.5285 | 0.9550 | 0.998  | −0.25pp\n"
411	      }
412	    ],
413	    "figures": [],
414	    "analysis": "Fusion head ablation confirms structural features don't add value at inference time. The model effectively learns to zero out the structural channel. This is consistent with the broader finding that structural information's role in code retrieval is minimal when the training set is large enough.\n\n\nIn the worst case, the structural signal is weak enough that adding it to the embedding at inference time actually hurts slightly (−0.25pp). The structural-only head (using only dataflow features) performs poorly (R@1=0.312) because structural connectivity alone is too coarse — many connected files are not relevant, and many relevant files are not connected. The combined head underperforms embedding-only because the structural features add noise: the model has to learn to ignore the structural channel for the 66% of instances without structural data, and this interferes with the embedding channel. This confirms that structural information is better used at training time (as negative selection criterion) than at inference time — but even at training time it doesn't help in the worst case.\n"
415	  },
416	  {
417	    "name": "Ablation: dataflow-distance weighted negatives vs binary",
418	    "description": "Compare binary connected/disconnected with distance-weighted negative selection (closer disconnected files weighted higher). 1 seed × Qwen.\n",
419	    "results": {
420	      "binary_R1": 0.5245,
421	      "weighted_R1": 0.5255,
422	      "weighted_minus_binary_pp": 0.1
423	    },
424	    "tables": [
425	      {
426	        "name": "Table A5: Distance Weighting Ablation",
427	        "content": "Negative selection | R@1    | Δ vs random | Δ vs binary\n-------------------|--------|------------|-------------\nRandom             | 0.5290 | —          | —\nBinary disconnect  | 0.5245 | −0.45pp   | —\nDistance weighted  | 0.5255 | −0.35pp   | +0.10pp\n"
428	      }
429	    ],
430	    "figures": [],
431	    "analysis": "Marginal and uninformative. Confirms the dataflow pathway is not the lever. Appendix material only.\n\n\nDistance weighting provides slightly more informative negatives by preferring disconnected files that are structurally close (1-2 hops from connected boundary). But the improvement (+0.10pp) is negligible because: (1) the base dataflow strategy already doesn't help, so refining it doesn't matter; (2) the distance information from CodeQL is noisy (call-graph hop counts don't perfectly correlate with structural relevance); (3) at 34% structural coverage, most instances don't have distance information, so the weighting applies to a minority of training examples.\n"
432	  },
433	  {
434	    "name": "Failure analysis: 50 retrieval failures",
435	    "description": "Manual categorization of 50 cases where all strategies fail. Identify whether dataflow could have helped.\n",
436	    "results": {
437	      "total_failures_analyzed": 50,
438	      "categories": {
439	        "gold_file_very_different": 18,
440	        "gold_file_in_different_language": 4,
441	        "config_or_test_files": 12,
442	        "very_large_repo_dilution": 8,
443	        "dataflow_could_help": 5,
444	        "ambiguous": 3
445	      },
446	      "dataflow_could_help_pct": 10
447	    },
448	    "tables": [
449	      {
450	        "name": "Table 9: Failure Category Breakdown",
451	        "content": "Category                        | Count | Pct  | Structural fix possible?\n--------------------------------|-------|------|------------------------\nGold file lexically dissimilar  | 18    | 36%  | Unlikely\nConfig / test / non-code files  | 12    | 24%  | No\nLarge repo dilution (>500 files)| 8     | 16%  | Partial\nCross-language dependency       | 4     | 8%   | No\nStructural connectivity helps   | 5     | 10%  | Yes\nAmbiguous                       | 3     | 6%   | Maybe\n"
452	      }
453	    ],
454	    "figures": [],
455	    "analysis": "Failure analysis provides the ceiling argument for the negative-result paper: even a perfect structural negative mining strategy could only address ~10% of failure cases. The dominant failure mode (lexically dissimilar gold files) requires fundamentally different approaches (e.g., multi-modal queries that include error traces, stack traces, or issue descriptions). This explains *why* structural negatives don't help at scale: the failure distribution is dominated by cases where structure is irrelevant.\n\n\nMost retrieval failures are cases where the gold file is fundamentally different from the query (bug report → config file, error message → test file). These are not addressable by any negative mining strategy because the core problem is the query-document mismatch, not the contrastive training signal. Only ~10% of failures involve cases where structural connectivity could plausibly help (e.g., gold file is structurally connected but lexically dissimilar). This low ceiling limits the potential upside of any structural approach.\n"
456	  },
457	  {
458	    "name": "Qualitative examples: strategy comparison",
459	    "description": "5-10 cases where strategies produce different retrieval outcomes. Cherry-pick both directions (structural helps, structural hurts).\n",
460	    "results": {
461	      "examples_found": 7,
462	      "structural_helps": 2,
463	      "structural_hurts": 3,
464	      "no_clear_pattern": 2
465	    },
466	    "tables": [],
467	    "figures": [],
468	    "analysis": "Qualitative examples support the negative-result narrative: strategy choice cuts both ways, with no systematic direction. Use 2-3 examples in the paper to illustrate *why* strategies don't differentiate, not to argue for one strategy.\n\n\nIn the worst case, qualitative examples cannot construct a compelling narrative because the effects go both directions. The 2 cases where structural negatives help are genuine (query about a function call, gold file is the callee 2 hops away), but the 3 cases where they hurt are equally compelling (structural negatives push the encoder to distinguish files that are actually both relevant, causing it to miss the gold file). The balanced count prevents cherry-picking a one-directional story.\n"
469	  },
470	  {
471	    "name": "Inference-time graph method comparison (analysis only)",
472	    "description": "Literature analysis comparing training-time (StructFuse) vs inference-time (CodexGraph, LocAgent, RANGER) graph-based approaches. No experiment.\n",
473	    "results": {
474	      "papers_surveyed": 8,
475	      "conclusion": "complementary in theory, but our null result suggests training-time structural signal may be less valuable than inference-time navigation",
476	      "key_finding": "Inference-time methods re-compute structural relevance per query using the actual query context, while training-time methods (ours) bake structural signal into the encoder via negative selection. Our null result suggests the baked-in signal gets washed out, while inference-time methods preserve it. This reframes our contribution: training-time structure is less effective than inference-time structure for code retrieval.\n"
477	    },
478	    "tables": [],
479	    "figures": [],
480	    "analysis": "This comparison is uncomfortable but essential for the negative-result paper. It provides the theoretical explanation for our null result: static structural mining at training time cannot capture query-specific structural relevance. The practical takeaway: if you want to leverage code structure for retrieval, invest in inference-time graph navigation (CodexGraph, LocAgent), not training-time negative mining. This is an actionable, non-obvious conclusion that justifies the paper's contribution.\n\n\nThe literature comparison is more damaging in the worst case than it appears. If our structural mining doesn't help, but inference-time graph methods (LocAgent +8-12pp on SWE-bench, CodexGraph +5pp) do help, the implication is that structure matters but our approach to incorporating it (training-time negative selection) is the wrong mechanism. This shifts the paper from \"structure helps conditionally\" to \"training-time structure doesn't help, and we explain why inference-time approaches succeed where we fail.\" The explanation: training-time mining fixes the structural signal at corpus construction time, but the relevant structure changes per query (different bugs involve different call chains). Inference-time methods adapt to the query.\n"
481	  },
482	  {
483	    "name": "Representation geometry convergence analysis",
484	    "description": "Measure pos_sim, neg_sim, margin for all strategies using fine-tuned encoders (not just pretrained). Tests whether fine-tuning erases pretrained geometry differences.\n",
485	    "results": {
486	      "qwen_post_finetune": {
487	        "random": {
488	          "pos_sim": 0.912,
489	          "neg_sim": 0.845,
490	          "margin": 0.067
491	        },
492	        "embedding": {
493	          "pos_sim": 0.9135,
494	          "neg_sim": 0.862,
495	          "margin": 0.0515
496	        },
497	        "dataflow": {
498	          "pos_sim": 0.9128,
499	          "neg_sim": 0.854,
500	          "margin": 0.0588
501	        }
502	      },
503	      "starcoder_post_finetune": {
504	        "random": {
505	          "pos_sim": 0.865,
506	          "neg_sim": 0.792,
507	          "margin": 0.073
508	        },
509	        "embedding": {
510	          "pos_sim": 0.867,
511	          "neg_sim": 0.81,
512	          "margin": 0.057
513	        },
514	        "dataflow": {
515	          "pos_sim": 0.866,
516	          "neg_sim": 0.801,
517	          "margin": 0.065
518	        }
519	      },
520	      "margin_convergence_qwen_pct": 78,
521	      "margin_convergence_starcoder_pct": 65
522	    },
523	    "tables": [
524	      {
525	        "name": "Table 10: Representation Geometry Pre vs Post Fine-tuning",
526	        "content": "Encoder   | Phase      | Metric     | random | embedding | dataflow | Ratio(rand/emb)\n----------|------------|------------|--------|-----------|----------|---------------\nQwen      | Pretrained | margin     | 0.074  | 0.017     | 0.029    | 4.35\nQwen      | Fine-tuned | margin     | 0.067  | 0.052     | 0.059    | 1.29\nStarCoder | Pretrained | margin     | 0.194  | 0.067     | 0.119    | 2.90\nStarCoder | Fine-tuned | margin     | 0.073  | 0.057     | 0.065    | 1.28\n"
527	      }
528	    ],
529	    "figures": [],
530	    "analysis": "This is the paper's strongest contribution in the worst case: the mechanistic explanation for why strategy choice doesn't matter. Fine-tuning acts as a geometry equalizer — regardless of which negatives you use, the contrastive objective pushes the encoder toward the same representation geometry. The pretrained geometry (which determines initial negative difficulty) is a transient condition that gets erased. This explains why: (1) pilot-scale results showed strategy effects (not enough training to fully erase geometry), (2) full-scale results don't (enough training to converge), (3) temperature doesn't matter (the geometry convergence is objective-driven, not temperature-dependent). The representation geometry analysis transforms the negative result from \"nothing works\" to \"everything converges\" — a much more publishable framing.\n\nFine-tuning collapses the pretrained geometry differences. Pre-fine-tuning, Qwen (pos_sim=0.986) and StarCoder (pos_sim=0.798) had dramatically different geometries. Post-fine-tuning, both converge toward pos_sim ~0.87-0.91. The margins across strategies also converge: pretrained Qwen had random margin 0.074 vs embedding margin 0.017 (4.4× ratio); post-fine-tuning, random margin 0.067 vs embedding margin 0.052 (1.3× ratio). Fine-tuning acts as a geometry equalizer, pushing all representations toward the contrastive loss optimum regardless of the pretrained starting point. This explains why strategy differences that existed in the pretrained space don't translate to performance differences after training: the encoder adjusts its geometry to optimize the contrastive objective, and the specific negatives used matter less than the objective function itself. For Qwen, 78% of the pretrained margin difference between strategies is erased by fine-tuning. For StarCoder, 65% is erased.\n"
531	  }
532	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "505b6e75-c498-4a7e-9421-38c0687ca71c",
  "isSidechain": false,
  "promptId": "66bbad76-7453-4fae-883a-01da252df421",
  "type": "user",
  "uuid": "242375c8-68b7-4190-9fa7-e6c5d729058e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"M2 Full Qwen 9-seed 3-strategy training\",\n    \"description\": \"9 seeds × 3 strategies (random, embedding_distance, dataflow_aware) on Qwen2.5-Coder-3B LoRA. Full training data (~44K instances). Pool=50 eval.\\n\",\n    \"results\": {\n      \"random_mean_R1\": 0.529,\n      \"random_std_R1\": 0.0085,\n      \"random_95CI\": [\n        0.5224,\n        0.5356\n      ],\n      \"embedding_distance_mean_R1\": 0.531,\n      \"embedding_distance_std_R1\": 0.0092,\n      \"embedding_distance_95CI\": [\n        0.5239,\n        0.5381\n      ],\n      \"dataflow_aware_mean_R1\": 0.5245,\n      \"dataflow_aware_std_R1\": 0.011,\n      \"dataflow_aware_95CI\": [\n        0.516,\n        0.533\n      ],\n      \"emb_minus_random_R1_pp\": 0.2,\n      \"emb_minus_random_CI\": [\n        -0.62,\n        1.02\n      ],\n      \"df_minus_random_R1_pp\": -0.45,\n      \"df_minus_random_CI\": [\n        -1.5,\n        0.6\n      ],\n      \"best_step_mode\": 1000,\n      \"best_step_range\": [\n        500,\n        1500\n      ],\n      \"overfit_onset_step\": 1500\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2: Full-Scale R@1 by Strategy × Encoder (Qwen)\",\n        \"content\": \"Strategy          | Mean R@1 | Std   | 95% CI          | Δ vs Random | p (paired-t)\\n------------------|----------|-------|-----------------|-------------|-------------\\nrandom            | 0.5290   | 0.009 | [0.522, 0.536]  | —           | —\\nembedding_dist    | 0.5310   | 0.009 | [0.524, 0.538]  | +0.20pp     | 0.58\\ndataflow_aware    | 0.5245   | 0.011 | [0.516, 0.533]  | −0.45pp     | 0.31\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The pilot's +2.0pp embedding advantage was a seed-specific fluctuation. At full scale, the effect is +0.20pp with p=0.58 — no statistical significance. Dataflow shows a slight negative trend (−0.45pp) but also non-significant. Seed-to-seed variance (σ ≈ 0.009) exceeds the strategy effect, making it impossible to distinguish strategies on this encoder. This is consistent with Qwen's extreme representation saturation: when pos_sim=0.986, fine-tuning rapidly compresses any initial margin differences, and all strategies end up in the same loss basin.\\n\\n\\nPilot showed emb +2.0pp over random (0.5557 vs 0.5357), but that was 1 seed on pilot-scale data. At full scale with 9 seeds, seed variance dominates the small effect. The 2.0pp pilot delta shrinks to ~0.2pp because: (1) full training data (44K vs pilot subset) gives random negatives more coverage of the embedding space, reducing the advantage of curated hard negatives; (2) Qwen's extremely saturated pretrained space (pos_sim=0.9855) means all strategies produce negatives that are very close to the query — the margin between random_neg_sim (0.911) and emb_neg_sim (0.969) gets compressed further during fine-tuning as the encoder adjusts; (3) with 9 seeds, some seeds favor random (data order effects), some favor embedding, and the mean converges. The CI clearly includes 0, killing the claim that embedding mining \\\"consistently improves\\\" retrieval. Dataflow negatives show slight harm because at full scale, the 34% structural coverage means 66% of training instances fall back to random, diluting any signal; the structural negatives for the remaining 34% may be less informative than embedding negatives (dataflow disconnection doesn't guarantee semantic difficulty).\\n\"\n  },\n  {\n    \"name\": \"M2 Full StarCoder 9-seed 3-strategy training\",\n    \"description\": \"9 seeds × 3 strategies on StarCoder2-3B. Same protocol as Qwen.\\n\",\n    \"results\": {\n      \"random_mean_R1\": 0.443,\n      \"random_std_R1\": 0.0105,\n      \"random_95CI\": [\n        0.4349,\n        0.4511\n      ],\n      \"embedding_distance_mean_R1\": 0.4395,\n      \"embedding_distance_std_R1\": 0.012,\n      \"embedding_distance_95CI\": [\n        0.4302,\n        0.4488\n      ],\n      \"dataflow_aware_mean_R1\": 0.428,\n      \"dataflow_aware_std_R1\": 0.0135,\n      \"dataflow_aware_95CI\": [\n        0.4176,\n        0.4384\n      ],\n      \"emb_minus_random_R1_pp\": -0.35,\n      \"emb_minus_random_CI\": [\n        -1.4,\n        0.7\n      ],\n      \"df_minus_random_R1_pp\": -1.5,\n      \"df_minus_random_CI\": [\n        -3.1,\n        0.1\n      ],\n      \"best_step_mode\": 1000,\n      \"overfit_onset_step\": 1500\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2 (continued): Full-Scale R@1 by Strategy × Encoder (StarCoder)\",\n        \"content\": \"Strategy          | Mean R@1 | Std   | 95% CI          | Δ vs Random | p (paired-t)\\n------------------|----------|-------|-----------------|-------------|-------------\\nrandom            | 0.4430   | 0.011 | [0.435, 0.451]  | —           | —\\nembedding_dist    | 0.4395   | 0.012 | [0.430, 0.449]  | −0.35pp     | 0.47\\ndataflow_aware    | 0.4280   | 0.014 | [0.418, 0.438]  | −1.50pp     | 0.015\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"StarCoder's full-scale results are worse than Qwen overall (R@1 ~0.44 vs ~0.53), consistent with decoder-only FIM pretraining being less suited for bidirectional retrieval. Critically, embedding mining does not help — the sign flipped from pilot (+1.56pp → −0.35pp). Dataflow shows possible harm (p=0.015), but with 9 comparisons across the study, this doesn't survive multiple-testing correction (Bonferroni threshold ~0.006). The dominant finding is that no strategy differentiates reliably. Combined with Qwen, neither encoder shows a strategy effect that survives multi-seed evaluation.\\n\\n\\nStarCoder pilot showed embedding +1.56pp (0.5078 vs 0.4922), but pilot used post-hoc eval for random (no in-training eval), introducing measurement inconsistency. At full scale with 9 seeds and consistent eval: (1) StarCoder's healthier pretrained geometry (pos_sim=0.80) means random negatives already provide decent margin (0.194), so embedding mining's tighter margins (0.067) may actually hurt by making the contrastive task too hard early in training, causing some seeds to find worse optima; (2) the higher seed variance for StarCoder (σ=0.012 vs Qwen's 0.009) reflects the decoder-only architecture's sensitivity to initialization — FIM pretraining creates a less smooth loss landscape for retrieval fine-tuning; (3) dataflow negatives show the most harm (−1.50pp) because StarCoder's intact geometry already separates structural from non-structural code well, so forcing structural discrimination adds noise rather than signal. The CI for embedding nearly spans zero but slightly favors negative; for dataflow, the CI upper bound just barely touches zero, suggesting possible marginal harm.\\n\"\n  },\n  {\n    \"name\": \"M3a SWE-bench Lite end-to-end evaluation\",\n    \"description\": \"3 strategies × best checkpoint per encoder, evaluated on SWE-bench Lite (300 instances) with Qwen3.6-27B agent. Measures resolve rate.\\n\",\n    \"results\": {\n      \"qwen_random_resolve_rate\": 0.2467,\n      \"qwen_embedding_resolve_rate\": 0.25,\n      \"qwen_dataflow_resolve_rate\": 0.2433,\n      \"starcoder_random_resolve_rate\": 0.2267,\n      \"starcoder_embedding_resolve_rate\": 0.2233,\n      \"starcoder_dataflow_resolve_rate\": 0.22,\n      \"best_minus_worst_pp\": 0.67,\n      \"swebench_resolve_rate_delta_pp\": 0.33,\n      \"qwen_emb_minus_random_delta_pp\": 0.33,\n      \"starcoder_emb_minus_random_delta_pp\": -0.34\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: SWE-bench Lite Resolve Rate\",\n        \"content\": \"Encoder   | Strategy   | Resolve Rate | Δ vs Random | 95% Binom CI\\n----------|------------|-------------|-------------|------------------\\nQwen      | random     | 24.67%      | —           | [19.9%, 29.4%]\\nQwen      | embedding  | 25.00%      | +0.33pp     | [20.2%, 29.8%]\\nQwen      | dataflow   | 24.33%      | −0.33pp     | [19.6%, 29.1%]\\nStarCoder | random     | 22.67%      | —           | [18.0%, 27.3%]\\nStarCoder | embedding  | 22.33%      | −0.34pp     | [17.7%, 27.0%]\\nStarCoder | dataflow   | 22.00%      | −0.67pp     | [17.3%, 26.7%]\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"No downstream differentiation. The largest gap (Qwen-embedding vs StarCoder-dataflow) is 2.8pp, which is well within the ±5pp binomial CI. This confirms the worst-case prediction: when retrieval strategy differences are <0.5pp, the downstream task cannot detect them. The paper cannot claim any practical benefit from mining strategy choice. SWE-bench results must be reported transparently as showing no differentiation, which strengthens the negative-result narrative (\\\"practitioners need not invest GPU time in fancy mining\\\").\\n\\n\\nSWE-bench resolve rate is dominated by the LLM agent's reasoning ability, not retrieval quality. The retrieval step provides a candidate set, but the agent re-ranks and explores beyond the initial retrieval. With R@1 differences of <0.5pp at pool=50, the downstream task absorbs the noise entirely. Quantitatively: (1) at resolve rates of ~24%, a 1pp R@1 improvement translates to at most ~0.3pp resolve rate improvement (retrieval → localization → patch → test is a multi-stage pipeline where errors compound but also get corrected by the agent); (2) with 300 instances, the binomial CI for a 24% resolve rate is ±4.8pp — any sub-1pp strategy difference is invisible; (3) the agent's exploration strategy (re-reading files, searching for imports) effectively compensates for missed retrievals, especially for the dataflow-relevant cases where structural dependencies guide the agent's natural exploration. The numbers bounce randomly around ~24% with no interpretable pattern.\\n\"\n  },\n  {\n    \"name\": \"M3b RepoBench-R cross-file retrieval evaluation\",\n    \"description\": \"Retrieval-only evaluation on RepoBench-R (test_easy ~8K, test_hard ~8K). 3 strategies × 2 encoders × 9 seeds. Report R@1 with 95% bootstrap CIs.\\n\",\n    \"results\": {\n      \"qwen_easy_random_mean_R1\": 0.712,\n      \"qwen_easy_embedding_mean_R1\": 0.715,\n      \"qwen_easy_dataflow_mean_R1\": 0.709,\n      \"qwen_hard_random_mean_R1\": 0.431,\n      \"qwen_hard_embedding_mean_R1\": 0.434,\n      \"qwen_hard_dataflow_mean_R1\": 0.427,\n      \"starcoder_easy_random_mean_R1\": 0.685,\n      \"starcoder_easy_embedding_mean_R1\": 0.681,\n      \"starcoder_easy_dataflow_mean_R1\": 0.678,\n      \"starcoder_hard_random_mean_R1\": 0.398,\n      \"starcoder_hard_embedding_mean_R1\": 0.393,\n      \"starcoder_hard_dataflow_mean_R1\": 0.389,\n      \"repobench_R1_delta_pp\": 0.3,\n      \"bootstrap_CI_width_R1_pp\": 3.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: RepoBench-R R@1 by Strategy × Encoder × Split\",\n        \"content\": \"Split | Encoder   | random       | embedding    | dataflow     | Δ emb-rand\\n------|-----------|-------------|-------------|-------------|------------\\neasy  | Qwen      | 71.2 ± 1.4  | 71.5 ± 1.5  | 70.9 ± 1.6  | +0.3pp\\neasy  | StarCoder | 68.5 ± 1.6  | 68.1 ± 1.7  | 67.8 ± 1.8  | −0.4pp\\nhard  | Qwen      | 43.1 ± 2.0  | 43.4 ± 2.1  | 42.7 ± 2.2  | +0.3pp\\nhard  | StarCoder | 39.8 ± 2.2  | 39.3 ± 2.4  | 38.9 ± 2.5  | −0.5pp\\nNote: ± indicates 95% bootstrap CI half-width. All CIs overlap across strategies.\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RepoBench-R confirms the SWE-smith full-scale finding: no strategy reliably differentiates on an external benchmark. The inconsistent sign across encoders (positive for Qwen, negative for StarCoder) is the signature of noise, not signal. CI widths of 3–5pp completely swamp the 0.3–0.5pp strategy effects. This external validation strengthens the negative-result claim: strategy choice doesn't matter even when measured on a different benchmark with different pool sizes and task formulation.\\n\\n\\nRepoBench-R uses naturally small pools (~6 for easy, ~18 for hard), which compresses retrieval difficulty. At pool=6, even a mediocre encoder achieves high R@1 (>0.70 on easy), leaving little room for strategy differentiation. The training data (SWE-smith) and eval data (RepoBench-R) come from different distributions — SWE-smith is bug-fix focused while RepoBench is cross-file completion — so training signal transfer is lossy. With 9 seeds and bootstrap CIs, the inter-seed variance (~2-3pp) dwarfs the strategy effect (<0.5pp). The hard split shows more variance but still no consistent direction: embedding helps Qwen by 0.3pp but hurts StarCoder by 0.5pp, consistent with the full-scale result that strategy effects are noise. Dataflow shows slight consistent harm because the structural signal from SWE-smith repos doesn't transfer to RepoBench's different repo distribution.\\n\"\n  },\n  {\n    \"name\": \"Stratified analysis: 5-stratum deep dive\",\n    \"description\": \"5 strata: (1) repo size, (2) pool size, (3) query-positive similarity, (4) structural data availability (34% vs 66%), (5) neg_difficulty quartile. Report per-stratum R@1 deltas for all 3 strategies × 2 encoders.\\n\",\n    \"results\": {\n      \"struct_available_emb_minus_random_qwen\": 0.15,\n      \"struct_available_df_minus_random_qwen\": 0.4,\n      \"struct_fallback_emb_minus_random_qwen\": 0.25,\n      \"struct_fallback_df_minus_random_qwen\": -0.9,\n      \"neg_diff_Q1_easy_emb_delta\": 0.6,\n      \"neg_diff_Q4_hard_emb_delta\": -0.3,\n      \"repo_small_emb_delta\": 0.8,\n      \"repo_large_emb_delta\": -0.15,\n      \"pool_small_emb_delta\": 0.35,\n      \"pool_large_emb_delta\": -0.2,\n      \"no_stratum_significant_after_correction\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Per-Stratum Δ(embedding − random) R@1 (Qwen, pp)\",\n        \"content\": \"Stratum                  | N instances | Δ R@1 (pp) | 95% CI         | Sig?\\n-------------------------|-------------|-----------|----------------|-----\\nRepo small (<200)        |  4596       | +0.80     | [−1.5, +3.1]   | No\\nRepo large (≥200)        | 39577       | −0.15     | [−0.9, +0.6]   | No\\nPool small (<30)         | 12044       | +0.35     | [−1.2, +1.9]   | No\\nPool large (≥30)         | 32129       | −0.20     | [−1.0, +0.6]   | No\\nHigh q-pos sim (>0.95)   | 28800       | −0.10     | [−0.8, +0.6]   | No\\nLow q-pos sim (≤0.95)    | 15373       | +0.55     | [−0.9, +2.0]   | No\\nStruct available (34%)   | 15133       | +0.15     | [−1.2, +1.5]   | No\\nStruct fallback (66%)    | 29040       | +0.25     | [−0.5, +1.0]   | No\\nNeg diff Q1 (easiest)    | 11043       | +0.60     | [−1.5, +2.7]   | No\\nNeg diff Q4 (hardest)    | 11043       | −0.30     | [−2.3, +1.7]   | No\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"No stratum produces a significant strategy effect after Bonferroni correction (10 comparisons, α=0.005). The structural availability stratum is the most informative: it shows that the 34% with real structural data has a tiny positive dataflow signal, but this is completely washed out by the 66% fallback. This is actually a useful finding for the negative-result paper: it suggests that structural negative mining *might* help if structural data coverage were higher (>80%), but at practical extraction rates (34%), the benefit is undetectable. This becomes an actionable takeaway: \\\"invest in extraction coverage before investing in mining strategy.\\\"\\n\\n\\nStratified analysis reveals that the aggregate null result masks opposing sub-population effects that cancel out — but none are individually significant after multiple-testing correction. Structural data stratum: the 34% with dataflow data shows a tiny positive df effect (+0.4pp), but the 66% fallback (which uses random negatives labeled as \\\"dataflow\\\") dilutes and reverses it. This is expected because the fallback mechanism means the \\\"dataflow\\\" strategy is actually ~66% random, making the aggregate comparison (dataflow vs random) a comparison of (0.34×structural + 0.66×random) vs (1.0×random). The 34% pure structural signal is too diluted to surface. Neg_difficulty quartiles: the easiest quartile (Q1, high margin) shows slight embedding advantage because the encoder can exploit the difficulty gradient; the hardest quartile (Q4, near-zero margin) shows slight embedding harm because those negatives are false-negative-adjacent (too similar to be true negatives). But with 9 seeds, the per-quartile CIs are wide (~5pp) because each quartile has only ~25% of the data. Repo size and pool size strata show similar noisy, contradictory patterns.\\n\"\n  },\n  {\n    \"name\": \"Temperature ablation: τ ∈ {0.05, 0.1, 0.2}\",\n    \"description\": \"3 temperatures × 3 strategies × 2 encoders. Tests whether the null result is regime-specific to τ=0.05.\\n\",\n    \"results\": {\n      \"tau_005_emb_minus_random_qwen\": 0.2,\n      \"tau_010_emb_minus_random_qwen\": 0.35,\n      \"tau_020_emb_minus_random_qwen\": -0.1,\n      \"tau_005_emb_minus_random_starcoder\": -0.35,\n      \"tau_010_emb_minus_random_starcoder\": 0.15,\n      \"tau_020_emb_minus_random_starcoder\": -0.55,\n      \"best_tau_overall\": 0.05,\n      \"strategy_ranking_changes_across_tau\": true,\n      \"any_tau_significant\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table A1: Temperature × Strategy Interaction (R@1, Qwen)\",\n        \"content\": \"τ    | random | embedding | dataflow | Δ emb-rand | Δ df-rand\\n-----|--------|-----------|----------|-----------|----------\\n0.05 | 0.5290 | 0.5310    | 0.5245   | +0.20     | −0.45\\n0.10 | 0.5215 | 0.5250    | 0.5200   | +0.35     | −0.15\\n0.20 | 0.5040 | 0.5030    | 0.5015   | −0.10     | −0.25\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Temperature ablation confirms the null result is not regime-specific. The best overall R@1 is at τ=0.05 (sharpest), but strategy differences remain noise-level at all temperatures. τ=0.2 degrades all strategies uniformly by ~2.5pp, consistent with known contrastive learning theory (too-warm temperatures lose discriminative power). The instability of strategy rankings across τ is itself evidence against a true strategy effect — a real signal would produce consistent rankings regardless of temperature. Report in appendix as robustness check.\\n\\n\\nTemperature controls the sharpness of the contrastive loss. At τ=0.05 (current), the loss is very sharp and the hardest negatives dominate the gradient — this should maximally differentiate strategies. If strategies don't differentiate at τ=0.05, they're unlikely to at τ=0.1 or 0.2 (where the loss is smoother and hard negatives matter less). The results confirm this: τ=0.1 shows slightly larger positive deltas for Qwen (the warmer loss surface allows more exploration), but still non-significant. τ=0.2 makes the loss too smooth, suppressing all hard-negative signal. Importantly, strategy rankings are unstable across τ: embedding beats random at τ=0.1 but loses at τ=0.2, confirming that the null result is not an artifact of temperature choice — there is genuinely no robust strategy advantage.\\n\"\n  },\n  {\n    \"name\": \"Dynamic embedding mining baseline\",\n    \"description\": \"Re-mine embedding negatives per epoch vs static (mine once from pretrained). 1 seed × 2 encoders. Tests whether static mining confound explains null result.\\n\",\n    \"results\": {\n      \"qwen_dynamic_R1\": 0.5315,\n      \"qwen_static_R1\": 0.531,\n      \"qwen_dynamic_minus_static_pp\": 0.05,\n      \"starcoder_dynamic_R1\": 0.44,\n      \"starcoder_static_R1\": 0.4395,\n      \"starcoder_dynamic_minus_static_pp\": 0.05,\n      \"mining_time_overhead_pct\": 340\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table A2: Static vs Dynamic Mining\",\n        \"content\": \"Encoder   | Static R@1 | Dynamic R@1 | Δ (pp) | Time overhead\\n----------|-----------|------------|--------|-------------\\nQwen      | 0.5310    | 0.5315     | +0.05  | +340%\\nStarCoder | 0.4395    | 0.4400     | +0.05  | +340%\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Dynamic mining is a non-factor. The encoder doesn't change enough during LoRA fine-tuning to make dynamic negatives meaningfully different from static ones. This rules out the confound that our null result is caused by stale negatives. For the negative-result paper, this is useful: \\\"even the theoretically optimal mining schedule (dynamic) cannot rescue strategy differentiation.\\\"\\n\\n\\nDynamic mining re-computes negatives using the current encoder state each epoch, so negatives should be harder (adapted to the learned representation). However, in the worst case, this doesn't help because: (1) the encoder barely moves during 3 epochs of LoRA fine-tuning — the pretrained representation is 99% preserved, so dynamic and static negatives are nearly identical (the cosine similarity between epoch-0 and epoch-3 embeddings for any given sample is >0.995); (2) any benefit from harder negatives is offset by training instability (the loss landscape shifts each epoch, preventing convergence to a stable optimum); (3) the 3.4× time overhead (re-encoding 44K instances per epoch) makes this impractical for no gain. The delta of +0.05pp for both encoders is effectively zero, confirming that the null result is not an artifact of static mining.\\n\"\n  },\n  {\n    \"name\": \"Bootstrap CI for SWE-bench Lite resolve rates\",\n    \"description\": \"10,000 bootstrap resamples for each strategy's resolve rate on SWE-bench Lite (300 instances). Tests statistical significance of resolve rate deltas.\\n\",\n    \"results\": {\n      \"qwen_random_resolve_rate\": 0.2467,\n      \"qwen_random_bootstrap_CI\": [\n        0.198,\n        0.296\n      ],\n      \"qwen_embedding_resolve_rate\": 0.25,\n      \"qwen_embedding_bootstrap_CI\": [\n        0.201,\n        0.299\n      ],\n      \"qwen_dataflow_resolve_rate\": 0.2433,\n      \"qwen_dataflow_bootstrap_CI\": [\n        0.196,\n        0.292\n      ],\n      \"emb_minus_random_bootstrap_CI\": [\n        -0.048,\n        0.055\n      ],\n      \"df_minus_random_bootstrap_CI\": [\n        -0.055,\n        0.048\n      ],\n      \"any_comparison_significant\": false,\n      \"bootstrap_CI_width_pp\": 4.9\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4 (extended): Bootstrap CIs for SWE-bench Resolve Rates\",\n        \"content\": \"Comparison              | Δ (pp) | Bootstrap 95% CI | p-value\\n------------------------|--------|------------------|--------\\nQwen emb − random       | +0.33  | [−4.8, +5.5]    | 0.89\\nQwen df − random        | −0.33  | [−5.5, +4.8]    | 0.89\\nSC emb − random         | −0.34  | [−5.5, +4.8]    | 0.89\\nSC df − random          | −0.67  | [−5.8, +4.5]    | 0.80\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bootstrap CIs formalize what the point estimates already suggest: SWE-bench cannot discriminate between mining strategies at the effect sizes observed. This is not a power problem we can fix — it's a fundamental limitation of using 300-instance downstream evaluation to detect <1pp retrieval differences. For the negative-result paper, this motivates the argument that practitioners should not over-invest in mining strategy optimization based on downstream benchmarks.\\n\\n\\nWith 300 binary outcomes and a base rate of ~25%, the binomial standard error is √(0.25×0.75/300) = 0.025, giving a 95% CI half-width of ~5pp. The strategy deltas (<0.5pp) are 10× smaller than the CI width. Bootstrap resampling confirms the analytical calculation: all pairwise CIs include zero, with p-values >0.5. This is the expected worst-case outcome: SWE-bench's small N makes it impossible to detect sub-1pp retrieval differences in downstream task performance. Even a \\\"true\\\" 0.5pp retrieval improvement would need N≈60,000 instances to detect at α=0.05 in downstream resolve rate.\\n\"\n  },\n  {\n    \"name\": \"BM25 negative baseline\",\n    \"description\": \"Mine BM25-based hard negatives as 4th strategy. Train ≥1 seed × 2 encoders. Compare R@1 with random/embedding/dataflow to test whether BM25 negatives match embedding negatives (which would prevent closing the CoCoHaNeRe argument).\\n\",\n    \"results\": {\n      \"qwen_bm25_R1\": 0.5275,\n      \"qwen_bm25_95CI\": [\n        0.515,\n        0.54\n      ],\n      \"starcoder_bm25_R1\": 0.437,\n      \"starcoder_bm25_95CI\": [\n        0.42,\n        0.454\n      ],\n      \"qwen_bm25_minus_random_pp\": -0.15,\n      \"starcoder_bm25_minus_random_pp\": -0.6,\n      \"qwen_bm25_minus_embedding_pp\": -0.35,\n      \"starcoder_bm25_minus_embedding_pp\": -0.25,\n      \"bm25_vs_embedding_p_value_qwen\": 0.42,\n      \"bm25_vs_embedding_p_value_starcoder\": 0.55,\n      \"bm25_minus_random_R1_pp\": -0.38,\n      \"bm25_minus_random_CI\": [\n        -1.5,\n        0.7\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: 4-Strategy Comparison Including BM25 Baseline\",\n        \"content\": \"Encoder   | random | embedding | dataflow | BM25   | BM25−emb (pp) | p\\n----------|--------|-----------|----------|--------|---------------|------\\nQwen      | 0.5290 | 0.5310    | 0.5245   | 0.5275 | −0.35         | 0.42\\nStarCoder | 0.4430 | 0.4395    | 0.4280   | 0.4370 | −0.25         | 0.55\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The BM25 baseline delivers the worst possible outcome for the paper's original framing. BM25 ≈ embedding negatives means we cannot attribute CoCoHaNeRe's reported harm to their BM25-proxy methodology. The \\\"correction\\\" claim must be downgraded to an \\\"observation\\\": \\\"We note that CoCoHaNeRe's reported large negative effect (−27pp) was not reproduced in our controlled setup with either BM25 or embedding negatives, suggesting the effect may be attributable to other experimental differences (scale, encoder, evaluation protocol) rather than the BM25-vs-embedding distinction specifically.\\\" This is much weaker than the original Claim 1 framing. For the negative-result paper, this finding actually strengthens the narrative: even the BM25-vs-embedding distinction that motivated the study turns out to be illusory at scale.\\n\\n\\nThe worst case for the CoCoHaNeRe correction argument: BM25 negatives perform similarly to embedding negatives, making it impossible to claim that BM25-proxy was the source of CoCoHaNeRe's reported harm. Why this happens: (1) at full scale with 44K training instances, BM25 top-k negatives and embedding-distance top-k negatives have ~60% overlap — high-BM25 documents tend to also have high embedding similarity because both capture lexical/semantic relatedness; (2) the non-overlapping 40% doesn't create enough differential training signal to separate the strategies; (3) CoCoHaNeRe's reported -27pp harm was likely driven by other confounds (different training data scale, different encoder, different evaluation protocol) not captured by the BM25-vs-embedding distinction alone. In the worst case, BM25 negatives are slightly worse than random (−0.15pp Qwen, −0.60pp StarCoder) but the CIs include zero and overlap completely with embedding CIs. The CoCoHaNeRe correction argument cannot be closed: we can say \\\"BM25 and embedding negatives produce similar results in our setup\\\" but not \\\"BM25-proxy caused the harm.\\\"\\n\"\n  },\n  {\n    \"name\": \"Pool size sensitivity analysis\",\n    \"description\": \"Evaluate strategy rankings at pool={50, 100, 200, 500} using M2 best checkpoints on SWE-smith validation.\\n\",\n    \"results\": {\n      \"pool_50\": {\n        \"qwen_random_R1\": 0.529,\n        \"qwen_embedding_R1\": 0.531,\n        \"ranking\": [\n          \"embedding\",\n          \"random\",\n          \"dataflow\"\n        ]\n      },\n      \"pool_100\": {\n        \"qwen_random_R1\": 0.412,\n        \"qwen_embedding_R1\": 0.4085,\n        \"ranking\": [\n          \"random\",\n          \"embedding\",\n          \"dataflow\"\n        ]\n      },\n      \"pool_200\": {\n        \"qwen_random_R1\": 0.324,\n        \"qwen_embedding_R1\": 0.3265,\n        \"ranking\": [\n          \"embedding\",\n          \"dataflow\",\n          \"random\"\n        ]\n      },\n      \"pool_500\": {\n        \"qwen_random_R1\": 0.231,\n        \"qwen_embedding_R1\": 0.2285,\n        \"ranking\": [\n          \"random\",\n          \"dataflow\",\n          \"embedding\"\n        ]\n      },\n      \"pool_ranking_stable_pct\": 25,\n      \"ranking_flips\": 3,\n      \"kendall_tau_50_vs_500\": 0.33\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Strategy Ranking Stability Across Pool Sizes (Qwen)\",\n        \"content\": \"Pool | random R@1 | emb R@1  | df R@1   | Best strategy | Rank = pool50?\\n-----|-----------|----------|----------|---------------|---------------\\n50   | 0.5290    | 0.5310   | 0.5245   | embedding     | (reference)\\n100  | 0.4120    | 0.4085   | 0.4050   | random        | No\\n200  | 0.3240    | 0.3265   | 0.3250   | embedding     | Yes\\n500  | 0.2310    | 0.2285   | 0.2295   | random        | No\\n\"\n      },\n      {\n        \"name\": \"Table 7b: Strategy Ranking Stability (StarCoder)\",\n        \"content\": \"Pool | random R@1 | emb R@1  | df R@1   | Best strategy | Rank = pool50?\\n-----|-----------|----------|----------|---------------|---------------\\n50   | 0.4430    | 0.4395   | 0.4280   | random        | (reference)\\n100  | 0.3410    | 0.3380   | 0.3310   | random        | Yes\\n200  | 0.2620    | 0.2640   | 0.2590   | embedding     | No\\n500  | 0.1780    | 0.1750   | 0.1770   | random        | Yes\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pool size sensitivity confirms the worst case: strategy rankings are unstable. Rankings flip 3 times across 4 pool sizes, with stability at only 25%. This means the paper's strategy comparison is contingent on the evaluation protocol, not a property of the strategies themselves. For the negative-result paper, this is a strong finding: \\\"strategy rankings are not robust to pool size choice, suggesting that reported differences in prior work may also be evaluation artifacts.\\\" The practical takeaway: don't optimize mining strategy based on a single pool size — the ranking you find may not hold at deployment scale.\\n\\n\\nPool size sensitivity exposes the fragility of strategy rankings. At pool=50 (current), embedding slightly leads — but this is the artificial setting. As pool grows: (1) the absolute R@1 drops substantially because finding the gold file among 200 or 500 candidates is genuinely harder; (2) strategy rankings become unstable because the relative ordering depends on which specific distractor files are added to the pool — at pool=500, many repos don't have 500 files, so padding strategies introduce noise; (3) the models were trained with pool sizes effectively set by the negative sampling (3 negatives → effective pool ~4), so they're not calibrated for large-pool ranking; (4) the ranking instability (Kendall τ = 0.33 between pool=50 and pool=500) means the strategy comparison is not robust to evaluation protocol choices. Only 25% of the time does the pool=50 ranking agree with other pool sizes — well below the 50% threshold that would indicate stability.\\n\"\n  },\n  {\n    \"name\": \"Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding\",\n    \"description\": \"Test whether expanding call-graph scope (1/2/3-hop) changes dataflow negative quality. 1 seed × Qwen.\\n\",\n    \"results\": {\n      \"hop1_R1\": 0.523,\n      \"hop2_R1\": 0.5245,\n      \"hop3_R1\": 0.521,\n      \"hop2_minus_hop1_pp\": 0.15,\n      \"hop3_minus_hop2_pp\": -0.35\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table A3: Hop Count Ablation (Qwen, dataflow strategy)\",\n        \"content\": \"Hops | Connected files/query | Negatives available | R@1    | Δ vs random\\n-----|----------------------|--------------------|---------|-----------\\n1    | 2.1                  | 47.9               | 0.5230 | −0.60pp\\n2    | 4.8                  | 45.2               | 0.5245 | −0.45pp\\n3    | 11.3                 | 38.7               | 0.5210 | −0.80pp\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Hop count ablation is uninformative in the worst case — it's optimizing within a strategy that doesn't work. The only useful observation: 3-hop over-expansion is slightly worse, suggesting that very broad connectivity definitions reduce negative quality. But the effect is tiny (0.35pp) and this entire analysis is moot given the overarching null result. Relegate to appendix.\\n\\n\\nIn the worst case, hop count doesn't matter because the dataflow strategy itself doesn't differentiate from random. 1-hop produces the most conservative connected set (fewer files connected → more negatives available → negatives are closer to embedding-based selection). 2-hop (current) is slightly better because it captures inter-procedural dependencies. 3-hop over-expands the connected set, marking too many files as connected and leaving fewer high-quality negatives. But all three are within noise of each other and within noise of random (0.5290), confirming that the structural signal pathway is not the bottleneck — the bottleneck is that no mining strategy differentiates at scale.\\n\"\n  },\n  {\n    \"name\": \"Ablation: training data size scaling\",\n    \"description\": \"1K vs 3K vs 5K (full) training instances, all 3 strategies, 1 seed × Qwen. Tests whether strategy effects are scale-dependent.\\n\",\n    \"results\": {\n      \"size_1K\": {\n        \"random_R1\": 0.505,\n        \"embedding_R1\": 0.518,\n        \"dataflow_R1\": 0.512,\n        \"emb_minus_random_pp\": 1.3\n      },\n      \"size_3K\": {\n        \"random_R1\": 0.52,\n        \"embedding_R1\": 0.526,\n        \"dataflow_R1\": 0.521,\n        \"emb_minus_random_pp\": 0.6\n      },\n      \"size_5K\": {\n        \"random_R1\": 0.529,\n        \"embedding_R1\": 0.531,\n        \"dataflow_R1\": 0.5245,\n        \"emb_minus_random_pp\": 0.2\n      },\n      \"effect_trend\": \"strategy advantage monotonically decreases with scale\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Scale-Dependent Strategy Effects\",\n        \"content\": \"Train size | random R@1 | embedding R@1 | Δ (pp) | df R@1  | Δ df-rand (pp)\\n-----------|-----------|--------------|--------|---------|---------------\\n1K         | 0.5050    | 0.5180       | +1.30  | 0.5120  | +0.70\\n3K         | 0.5200    | 0.5260       | +0.60  | 0.5210  | +0.10\\n5K (full)  | 0.5290    | 0.5310       | +0.20  | 0.5245  | −0.45\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This is the paper's most compelling experiment. The scale-dependent effect provides the mechanistic story: hard negative mining helps at small scale but its advantage vanishes as random sampling catches up. This connects to the representation geometry analysis: at small scale, random negatives are too easy (high margin) and the encoder doesn't learn the decision boundary well. As scale increases, random negatives include enough hard examples by chance. This reframes the negative result as a positive finding: \\\"scale is a substitute for curation in contrastive code retrieval.\\\" Actionable takeaway: if your training set is small (<2K), invest in mining; if large (>5K), random suffices.\\n\\n\\nThis is the most important ablation for the negative-result narrative. At 1K instances (pilot-like scale), embedding mining shows a +1.3pp advantage — close to the pilot's +2.0pp, confirming that the pilot finding was real but scale-dependent. As training data increases to 3K and 5K, the advantage shrinks to 0.6pp and 0.2pp respectively. Mechanism: with more training data, the random negatives sample a wider swath of the embedding space, effectively approximating what curated embedding negatives provide. At small scale, curated negatives concentrate the training signal on the decision boundary; at large scale, random sampling covers the boundary adequately through sheer volume. This is a well-known phenomenon in contrastive learning (cf. SimCLR batch size scaling) and provides the mechanistic explanation for why pilot results didn't replicate at full scale.\\n\"\n  },\n  {\n    \"name\": \"Ablation: fusion head (embedding-only vs structural-only vs combined)\",\n    \"description\": \"Test whether adding structural features at inference time helps. 3 heads × best checkpoint × Qwen.\\n\",\n    \"results\": {\n      \"embedding_only_R1\": 0.531,\n      \"structural_only_R1\": 0.312,\n      \"combined_R1\": 0.5285,\n      \"combined_minus_embedding_pp\": -0.25\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table A4: Fusion Head Ablation (Qwen)\",\n        \"content\": \"Head           | R@1    | R@5    | R@10   | Δ vs emb-only\\n---------------|--------|--------|--------|--------------\\nEmbedding only | 0.5310 | 0.9600 | 1.000  | —\\nStructural only| 0.3120 | 0.6200 | 0.780  | −21.9pp\\nCombined       | 0.5285 | 0.9550 | 0.998  | −0.25pp\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Fusion head ablation confirms structural features don't add value at inference time. The model effectively learns to zero out the structural channel. This is consistent with the broader finding that structural information's role in code retrieval is minimal when the training set is large enough.\\n\\n\\nIn the worst case, the structural signal is weak enough that adding it to the embedding at inference time actually hurts slightly (−0.25pp). The structural-only head (using only dataflow features) performs poorly (R@1=0.312) because structural connectivity alone is too coarse — many connected files are not relevant, and many relevant files are not connected. The combined head underperforms embedding-only because the structural features add noise: the model has to learn to ignore the structural channel for the 66% of instances without structural data, and this interferes with the embedding channel. This confirms that structural information is better used at training time (as negative selection criterion) than at inference time — but even at training time it doesn't help in the worst case.\\n\"\n  },\n  {\n    \"name\": \"Ablation: dataflow-distance weighted negatives vs binary\",\n    \"description\": \"Compare binary connected/disconnected with distance-weighted negative selection (closer disconnected files weighted higher). 1 seed × Qwen.\\n\",\n    \"results\": {\n      \"binary_R1\": 0.5245,\n      \"weighted_R1\": 0.5255,\n      \"weighted_minus_binary_pp\": 0.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table A5: Distance Weighting Ablation\",\n        \"content\": \"Negative selection | R@1    | Δ vs random | Δ vs binary\\n-------------------|--------|------------|-------------\\nRandom             | 0.5290 | —          | —\\nBinary disconnect  | 0.5245 | −0.45pp   | —\\nDistance weighted  | 0.5255 | −0.35pp   | +0.10pp\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Marginal and uninformative. Confirms the dataflow pathway is not the lever. Appendix material only.\\n\\n\\nDistance weighting provides slightly more informative negatives by preferring disconnected files that are structurally close (1-2 hops from connected boundary). But the improvement (+0.10pp) is negligible because: (1) the base dataflow strategy already doesn't help, so refining it doesn't matter; (2) the distance information from CodeQL is noisy (call-graph hop counts don't perfectly correlate with structural relevance); (3) at 34% structural coverage, most instances don't have distance information, so the weighting applies to a minority of training examples.\\n\"\n  },\n  {\n    \"name\": \"Failure analysis: 50 retrieval failures\",\n    \"description\": \"Manual categorization of 50 cases where all strategies fail. Identify whether dataflow could have helped.\\n\",\n    \"results\": {\n      \"total_failures_analyzed\": 50,\n      \"categories\": {\n        \"gold_file_very_different\": 18,\n        \"gold_file_in_different_language\": 4,\n        \"config_or_test_files\": 12,\n        \"very_large_repo_dilution\": 8,\n        \"dataflow_could_help\": 5,\n        \"ambiguous\": 3\n      },\n      \"dataflow_could_help_pct\": 10\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Failure Category Breakdown\",\n        \"content\": \"Category                        | Count | Pct  | Structural fix possible?\\n--------------------------------|-------|------|------------------------\\nGold file lexically dissimilar  | 18    | 36%  | Unlikely\\nConfig / test / non-code files  | 12    | 24%  | No\\nLarge repo dilution (>500 files)| 8     | 16%  | Partial\\nCross-language dependency       | 4     | 8%   | No\\nStructural connectivity helps   | 5     | 10%  | Yes\\nAmbiguous                       | 3     | 6%   | Maybe\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Failure analysis provides the ceiling argument for the negative-result paper: even a perfect structural negative mining strategy could only address ~10% of failure cases. The dominant failure mode (lexically dissimilar gold files) requires fundamentally different approaches (e.g., multi-modal queries that include error traces, stack traces, or issue descriptions). This explains *why* structural negatives don't help at scale: the failure distribution is dominated by cases where structure is irrelevant.\\n\\n\\nMost retrieval failures are cases where the gold file is fundamentally different from the query (bug report → config file, error message → test file). These are not addressable by any negative mining strategy because the core problem is the query-document mismatch, not the contrastive training signal. Only ~10% of failures involve cases where structural connectivity could plausibly help (e.g., gold file is structurally connected but lexically dissimilar). This low ceiling limits the potential upside of any structural approach.\\n\"\n  },\n  {\n    \"name\": \"Qualitative examples: strategy comparison\",\n    \"description\": \"5-10 cases where strategies produce different retrieval outcomes. Cherry-pick both directions (structural helps, structural hurts).\\n\",\n    \"results\": {\n      \"examples_found\": 7,\n      \"structural_helps\": 2,\n      \"structural_hurts\": 3,\n      \"no_clear_pattern\": 2\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Qualitative examples support the negative-result narrative: strategy choice cuts both ways, with no systematic direction. Use 2-3 examples in the paper to illustrate *why* strategies don't differentiate, not to argue for one strategy.\\n\\n\\nIn the worst case, qualitative examples cannot construct a compelling narrative because the effects go both directions. The 2 cases where structural negatives help are genuine (query about a function call, gold file is the callee 2 hops away), but the 3 cases where they hurt are equally compelling (structural negatives push the encoder to distinguish files that are actually both relevant, causing it to miss the gold file). The balanced count prevents cherry-picking a one-directional story.\\n\"\n  },\n  {\n    \"name\": \"Inference-time graph method comparison (analysis only)\",\n    \"description\": \"Literature analysis comparing training-time (StructFuse) vs inference-time (CodexGraph, LocAgent, RANGER) graph-based approaches. No experiment.\\n\",\n    \"results\": {\n      \"papers_surveyed\": 8,\n      \"conclusion\": \"complementary in theory, but our null result suggests training-time structural signal may be less valuable than inference-time navigation\",\n      \"key_finding\": \"Inference-time methods re-compute structural relevance per query using the actual query context, while training-time methods (ours) bake structural signal into the encoder via negative selection. Our null result suggests the baked-in signal gets washed out, while inference-time methods preserve it. This reframes our contribution: training-time structure is less effective than inference-time structure for code retrieval.\\n\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"This comparison is uncomfortable but essential for the negative-result paper. It provides the theoretical explanation for our null result: static structural mining at training time cannot capture query-specific structural relevance. The practical takeaway: if you want to leverage code structure for retrieval, invest in inference-time graph navigation (CodexGraph, LocAgent), not training-time negative mining. This is an actionable, non-obvious conclusion that justifies the paper's contribution.\\n\\n\\nThe literature comparison is more damaging in the worst case than it appears. If our structural mining doesn't help, but inference-time graph methods (LocAgent +8-12pp on SWE-bench, CodexGraph +5pp) do help, the implication is that structure matters but our approach to incorporating it (training-time negative selection) is the wrong mechanism. This shifts the paper from \\\"structure helps conditionally\\\" to \\\"training-time structure doesn't help, and we explain why inference-time approaches succeed where we fail.\\\" The explanation: training-time mining fixes the structural signal at corpus construction time, but the relevant structure changes per query (different bugs involve different call chains). Inference-time methods adapt to the query.\\n\"\n  },\n  {\n    \"name\": \"Representation geometry convergence analysis\",\n    \"description\": \"Measure pos_sim, neg_sim, margin for all strategies using fine-tuned encoders (not just pretrained). Tests whether fine-tuning erases pretrained geometry differences.\\n\",\n    \"results\": {\n      \"qwen_post_finetune\": {\n        \"random\": {\n          \"pos_sim\": 0.912,\n          \"neg_sim\": 0.845,\n          \"margin\": 0.067\n        },\n        \"embedding\": {\n          \"pos_sim\": 0.9135,\n          \"neg_sim\": 0.862,\n          \"margin\": 0.0515\n        },\n        \"dataflow\": {\n          \"pos_sim\": 0.9128,\n          \"neg_sim\": 0.854,\n          \"margin\": 0.0588\n        }\n      },\n      \"starcoder_post_finetune\": {\n        \"random\": {\n          \"pos_sim\": 0.865,\n          \"neg_sim\": 0.792,\n          \"margin\": 0.073\n        },\n        \"embedding\": {\n          \"pos_sim\": 0.867,\n          \"neg_sim\": 0.81,\n          \"margin\": 0.057\n        },\n        \"dataflow\": {\n          \"pos_sim\": 0.866,\n          \"neg_sim\": 0.801,\n          \"margin\": 0.065\n        }\n      },\n      \"margin_convergence_qwen_pct\": 78,\n      \"margin_convergence_starcoder_pct\": 65\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Representation Geometry Pre vs Post Fine-tuning\",\n        \"content\": \"Encoder   | Phase      | Metric     | random | embedding | dataflow | Ratio(rand/emb)\\n----------|------------|------------|--------|-----------|----------|---------------\\nQwen      | Pretrained | margin     | 0.074  | 0.017     | 0.029    | 4.35\\nQwen      | Fine-tuned | margin     | 0.067  | 0.052     | 0.059    | 1.29\\nStarCoder | Pretrained | margin     | 0.194  | 0.067     | 0.119    | 2.90\\nStarCoder | Fine-tuned | margin     | 0.073  | 0.057     | 0.065    | 1.28\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This is the paper's strongest contribution in the worst case: the mechanistic explanation for why strategy choice doesn't matter. Fine-tuning acts as a geometry equalizer — regardless of which negatives you use, the contrastive objective pushes the encoder toward the same representation geometry. The pretrained geometry (which determines initial negative difficulty) is a transient condition that gets erased. This explains why: (1) pilot-scale results showed strategy effects (not enough training to fully erase geometry), (2) full-scale results don't (enough training to converge), (3) temperature doesn't matter (the geometry convergence is objective-driven, not temperature-dependent). The representation geometry analysis transforms the negative result from \\\"nothing works\\\" to \\\"everything converges\\\" — a much more publishable framing.\\n\\nFine-tuning collapses the pretrained geometry differences. Pre-fine-tuning, Qwen (pos_sim=0.986) and StarCoder (pos_sim=0.798) had dramatically different geometries. Post-fine-tuning, both converge toward pos_sim ~0.87-0.91. The margins across strategies also converge: pretrained Qwen had random margin 0.074 vs embedding margin 0.017 (4.4× ratio); post-fine-tuning, random margin 0.067 vs embedding margin 0.052 (1.3× ratio). Fine-tuning acts as a geometry equalizer, pushing all representations toward the contrastive loss optimum regardless of the pretrained starting point. This explains why strategy differences that existed in the pretrained space don't translate to performance differences after training: the encoder adjusts its geometry to optimize the contrastive objective, and the specific negatives used matter less than the objective function itself. For Qwen, 78% of the pretrained margin difference between strategies is erased by fine-tuning. For StarCoder, 65% is erased.\\n\"\n  }\n]",
      "numLines": 532,
      "startLine": 1,
      "totalLines": 532
    }
  },
  "sourceToolAssistantUUID": "505b6e75-c498-4a7e-9421-38c0687ca71c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-contex…",
  "leafUuid": "242375c8-68b7-4190-9fa7-e6c5d729058e",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Hard negative mining strategies for code retrieval convergence analysis",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081"
}
```

---

### Assistant

_source line 16 · 2026-05-14T16:54:36.765Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the data and framing. This is a "worst" tier dream paper — a negative result paper. Let me now write the full LaTeX paper.

Key points from the narrative guidance:
- Full-scale effect sizes collapse
- Embedding-distance mining shows no reliable advantage over random baselines with multi-seed CIs
- Dataflow negatives show no benefit or slight harm
- BM25 negatives perform statistically indistinguishable from embedding negatives
- Pool size scaling destabilizes strategy rankings
- SWE-bench shows no downstream signal


- I'll reframe this around why hard negative mining strategies fail to differentiate at scale, with a salvageable angle on representation geometry — specifically how margins collapse after fine-tuning — plus a methodological warning about using BM25 as a proxy for embedding-based negatives.

I'm structuring the paper with an abstract, introduction, related work, methods section covering the mining strategies and training setup, then experiments showing the main results across different models and datasets, including stratified analyses and pool size effects.

Writing the LaTeX document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "242375c8-68b7-4190-9fa7-e6c5d729058e",
  "isSidechain": false,
  "requestId": "req_011Cb2ozXbhNkrJXxLJ44HMD",
  "type": "assistant",
  "uuid": "cd9ee7d5-d5ed-4c0b-9445-c7c9bfcd9e4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152s9A12MTTweGnhU5WRQ8g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2954,
      "cache_creation_input_tokens": 15978,
      "cache_read_input_tokens": 23051,
      "output_tokens": 556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15978,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2954,
          "output_tokens": 556,
          "cache_read_input_tokens": 23051,
          "cache_creation_input_tokens": 15978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15978
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

_source line 17 · 2026-05-14T16:54:36.766Z_

Now I have all the data and framing. Let me write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd9ee7d5-d5ed-4c0b-9445-c7c9bfcd9e4b",
  "isSidechain": false,
  "requestId": "req_011Cb2ozXbhNkrJXxLJ44HMD",
  "type": "assistant",
  "uuid": "409801f3-da03-4729-a254-8ae44f94a160",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152s9A12MTTweGnhU5WRQ8g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2954,
      "cache_creation_input_tokens": 15978,
      "cache_read_input_tokens": 23051,
      "output_tokens": 556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15978,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2954,
          "output_tokens": 556,
          "cache_read_input_tokens": 23051,
          "cache_creation_input_tokens": 15978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15978
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

_source line 18 · 2026-05-14T16:54:38.424Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NTMaR6F4oAgZ2qcG9bYsPe`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "409801f3-da03-4729-a254-8ae44f94a160",
  "isSidechain": false,
  "requestId": "req_011Cb2ozXbhNkrJXxLJ44HMD",
  "type": "assistant",
  "uuid": "a67ba1dd-45ca-4f35-9e37-bfa048fbbb71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152s9A12MTTweGnhU5WRQ8g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2954,
      "cache_creation_input_tokens": 15978,
      "cache_read_input_tokens": 23051,
      "output_tokens": 556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15978,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2954,
          "output_tokens": 556,
          "cache_read_input_tokens": 23051,
          "cache_creation_input_tokens": 15978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15978
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

_source line 19 · 2026-05-14T16:54:38.598Z_

<details><summary>↩ Tool result · `toolu_01NTMaR6F4oAgZ2qcG9bYsPe`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a67ba1dd-45ca-4f35-9e37-bfa048fbbb71",
  "isSidechain": false,
  "promptId": "66bbad76-7453-4fae-883a-01da252df421",
  "type": "user",
  "uuid": "42fbccaa-e53d-441b-af0a-b8b9852af260",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "a67ba1dd-45ca-4f35-9e37-bfa048fbbb71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T16:57:47.939Z_

<details open><summary>🔧 Tool call — Write · `toolu_0136iCCGygQMFd8aAjHSqXuX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{adjustbox}\n\n\\aclfinalcopy\n\n\\title{Why Hard Negative Mining Strategies Don't Differentiate\\\\for Code Retrieval at Scale}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nHard negative mining is widely believed to be critical for training contrastive code retrievers, yet the field lacks controlled comparisons isolating the effect of mining strategy from confounding factors such as training scale, encoder choice, and evaluation protocol.\nWe present a systematic study of four negative mining strategies---random, embedding-distance, dataflow-aware, and BM25---across two decoder-only code encoders (Qwen2.5-Coder-3B and StarCoder2-3B) with 9 random seeds per condition.\nOur central finding is \\emph{negative}: at full training scale ($\\sim$44K instances), no mining strategy reliably outperforms random baselines.\nThe largest observed effect is $+0.20$ percentage points (pp) for embedding mining on Qwen ($p=0.58$), with 95\\% confidence intervals spanning zero for all comparisons.\nStrategy rankings are unstable across pool sizes (Kendall $\\tau=0.33$ between pool 50 and 500), and downstream SWE-bench Lite evaluation shows no differentiation ($\\Delta < 0.67$pp, bootstrap CI width $\\sim$5pp).\nWe provide a mechanistic explanation: fine-tuning acts as a \\emph{geometry equalizer}, collapsing pretrained margin differences across strategies by 65--78\\%.\nA data-scaling ablation reveals that mining advantages observed at pilot scale ($+1.3$pp at 1K instances) vanish monotonically with training set size, suggesting that scale substitutes for curation in contrastive code retrieval.\nWe additionally show that BM25 negatives perform indistinguishably from embedding negatives ($p > 0.42$), preventing closure of the argument that prior work's reported harm from hard negatives was caused by BM25-proxy methodology.\nOur results caution against over-investing in mining strategy optimization and redirect attention toward training scale and inference-time structural methods.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nRepository-level code retrieval---selecting the relevant source files from a large codebase given a bug report or issue description---is a critical bottleneck in automated software repair pipelines \\cite{jimenez2024swebench}.\nContrastive learning has emerged as the dominant paradigm for training dense code retrievers, where the choice of \\emph{hard negatives} is believed to strongly influence retrieval quality.\n\nPrior work offers conflicting guidance on hard negative mining for code.\nCoCoHaNeRe reports that embedding-distance negatives \\emph{harm} code search by up to 27 percentage points in R@1, advocating instead for keyword-based retrieval of negatives.\nHowever, this finding was obtained using BM25 as a proxy for embedding distance, raising the question of whether the reported harm reflects true embedding mining or confounds introduced by the proxy.\nMeanwhile, the contrastive learning literature in NLP and vision consistently finds that harder negatives improve representation quality, at least up to a difficulty threshold beyond which false negatives degrade training.\n\nWe set out to resolve this contradiction through a controlled study comparing four negative mining strategies for code retrieval: (1) random sampling, (2) true embedding-distance mining, (3) structure-grounded (dataflow-aware) mining using inter-procedural call-graph analysis, and (4) BM25-based mining.\nWe train with each strategy on two decoder-only code encoders with distinct pretrained representation geometries---Qwen2.5-Coder-3B (saturated, $\\text{pos\\_sim}=0.986$) and StarCoder2-3B (healthy, $\\text{pos\\_sim}=0.798$)---using 9 random seeds per condition to obtain reliable confidence intervals.\n\nOur findings are predominantly negative, which we argue is itself a contribution:\n\n\\begin{enumerate}\n    \\item \\textbf{No strategy differentiates at scale.} At full training scale ($\\sim$44K instances), all mining strategies produce statistically indistinguishable R@1 on both encoders. The largest effect ($+0.20$pp) has $p=0.58$.\n    \\item \\textbf{Representation geometry convergence.} Fine-tuning collapses pretrained margin differences by 65--78\\%, explaining why strategies that produce different negative difficulties in the pretrained space converge after training.\n    \\item \\textbf{Scale substitutes for curation.} Mining advantages observed at 1K instances ($+1.3$pp) vanish monotonically as training data grows, reaching $+0.2$pp at 5K instances.\n    \\item \\textbf{BM25 $\\approx$ embedding negatives.} BM25 and embedding-distance negatives are statistically indistinguishable ($p > 0.42$), preventing attribution of prior work's reported harm to the BM25-proxy methodology.\n    \\item \\textbf{Unstable strategy rankings.} Rankings flip across pool sizes (stability $= 25\\%$), temperatures, and encoders, indicating that reported differences in prior work may be evaluation artifacts.\n\\end{enumerate}\n\nThese results caution practitioners against investing GPU time in sophisticated mining pipelines when simple random sampling suffices at scale, and redirect attention toward training data volume and inference-time structural navigation methods.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Hard Negative Mining for Retrieval.}\nHard negative mining has a long history in metric learning and dense retrieval.\nANCE~\\cite{xiong2021approximate} periodically refreshes negatives using the current encoder, DPR~\\cite{karpukhin2020dense} uses BM25 negatives for open-domain QA, and curriculum-based approaches gradually increase negative difficulty during training.\nFor code, CoCoHaNeRe reports that embedding-distance negatives harm code search, but uses BM25 as a proxy rather than true embedding distance.\nOur work directly tests this claim with proper controls.\n\n\\paragraph{Code Retrieval.}\nDense retrieval for code has been explored with encoder-only models (GraphCodeBERT, CodeBERT) and more recently with decoder-only models fine-tuned for retrieval (SweRank, SWE-Fixer).\nThese systems typically use random or in-batch negatives without systematic comparison of mining strategies.\nRepoBench~\\cite{liu2023repobench} provides a cross-file retrieval benchmark that we use for external validation.\n\n\\paragraph{Structure-Aware Code Understanding.}\nGraph-based approaches to code operate at either training time or inference time.\nTraining-time methods (GraphCodeBERT) encode structural features into the model.\nInference-time methods (CodexGraph, LocAgent, RANGER) navigate code structure during retrieval using the query context.\nOur dataflow-aware mining falls in the training-time category; our null result suggests inference-time approaches may be more effective for leveraging structure.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Problem Setting}\n\nGiven a repository $\\mathcal{R}$ with source files $\\{f_1, \\ldots, f_n\\}$ and a query $q$ (e.g., a bug report), the retrieval task is to rank files by relevance.\nWe train a contrastive encoder $E_\\theta$ using InfoNCE loss with temperature $\\tau$:\n\\begin{equation}\n\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(q, f^+)/\\tau)}{\\exp(\\text{sim}(q, f^+)/\\tau) + \\sum_{i=1}^{K} \\exp(\\text{sim}(q, f_i^-)/\\tau)}\n\\end{equation}\nwhere $f^+$ is the gold file and $\\{f_i^-\\}_{i=1}^K$ are negatives selected by the mining strategy.\n\n\\subsection{Negative Mining Strategies}\n\nWe compare four strategies that differ only in how $\\{f_i^-\\}$ are selected:\n\n\\paragraph{Random.} Sample $K$ negatives uniformly from non-gold files in the repository.\n\n\\paragraph{Embedding-distance.} Using the pretrained encoder, compute cosine similarity between the query and all non-gold files. Select the top-$K$ most similar as hard negatives.\n\n\\paragraph{Dataflow-aware.} Using inter-procedural call-graph analysis via CodeQL, identify files that are \\emph{not} reachable from the gold file within 2 hops. Among these structurally disconnected files, select the top-$K$ by embedding similarity. This produces negatives that are semantically similar but structurally unrelated---the intuition being that structural disconnection is a stronger signal of irrelevance than embedding distance alone. Structural data is available for 34\\% of training instances; the remaining 66\\% fall back to embedding-distance mining.\n\n\\paragraph{BM25.} Tokenize query and files, compute BM25 scores, select top-$K$ non-gold files. This replicates the methodology attributed to ``embedding negatives'' in prior work.\n\n\\subsection{Encoders}\n\nWe fine-tune two 3B-parameter decoder-only code models using LoRA:\n\n\\begin{itemize}\n    \\item \\textbf{Qwen2.5-Coder-3B}: Pretrained with Fill-in-the-Middle. Exhibits saturated representation geometry ($\\text{pos\\_sim}=0.986$, margin $= 0.074$ for random negatives).\n    \\item \\textbf{StarCoder2-3B}: Pretrained with Fill-in-the-Middle on a different corpus. Healthier geometry ($\\text{pos\\_sim}=0.798$, margin $= 0.194$ for random negatives).\n\\end{itemize}\n\n\\subsection{Training Protocol}\n\nAll models are trained on $\\sim$44K instances from SWE-smith with $K=3$ negatives, $\\tau=0.05$, LoRA rank 16, for 3 epochs.\nEach strategy $\\times$ encoder combination is trained with 9 random seeds.\nEvaluation uses R@1 at pool size 50 on a held-out validation set unless otherwise noted.\n\n%==============================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n%==============================================================================\n\n\\subsection{Main Result: No Strategy Differentiates at Full Scale}\n\\label{sec:main_result}\n\nTable~\\ref{tab:main} presents the central result.\nOn Qwen, embedding mining achieves $+0.20$pp over random ($p=0.58$); on StarCoder, it achieves $-0.35$pp ($p=0.47$).\nNeither difference is statistically significant, and the signs are inconsistent across encoders---a signature of noise, not signal.\nDataflow-aware mining shows slight harm on both encoders ($-0.45$pp Qwen, $-1.50$pp StarCoder), with the StarCoder result reaching $p=0.015$ before multiple-testing correction but not surviving Bonferroni adjustment across the study's comparisons.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full-scale R@1 by strategy and encoder (9 seeds, pool=50). No strategy significantly outperforms random.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Strategy} & \\textbf{Mean R@1} & \\textbf{Std} & \\textbf{95\\% CI} & \\textbf{$\\Delta$ vs Rand} \\\\\n\\midrule\n\\multirow{3}{*}{Qwen} & Random & 0.529 & 0.009 & [.522, .536] & --- \\\\\n & Embedding & 0.531 & 0.009 & [.524, .538] & +0.20pp \\\\\n & Dataflow & 0.525 & 0.011 & [.516, .533] & $-$0.45pp \\\\\n\\midrule\n\\multirow{3}{*}{StarCoder} & Random & 0.443 & 0.011 & [.435, .451] & --- \\\\\n & Embedding & 0.440 & 0.012 & [.430, .449] & $-$0.35pp \\\\\n & Dataflow & 0.428 & 0.014 & [.418, .438] & $-$1.50pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeed-to-seed variance ($\\sigma \\approx 0.009$--$0.014$) exceeds the strategy effects in all cases.\nThe confidence intervals for all pairwise strategy comparisons include zero:\nembedding $-$ random on Qwen: $[-0.62, +1.02]$pp;\nembedding $-$ random on StarCoder: $[-1.4, +0.7]$pp;\ndataflow $-$ random on StarCoder: $[-3.1, +0.1]$pp.\n\n\\subsection{BM25 Negatives Match Embedding Negatives}\n\\label{sec:bm25}\n\nTable~\\ref{tab:bm25} adds BM25 as a fourth strategy.\nBM25 negatives are statistically indistinguishable from embedding negatives on both encoders (Qwen: $-0.35$pp, $p=0.42$; StarCoder: $-0.25$pp, $p=0.55$).\nThis prevents closing the argument that prior work's reported harm from hard negatives was caused by the BM25-proxy methodology specifically.\nThe high overlap ($\\sim$60\\%) between BM25 and embedding top-$K$ negatives at full scale explains this convergence.\n\n\\begin{table}[t]\n\\centering\n\\caption{Four-strategy comparison including BM25 baseline. BM25 and embedding negatives are indistinguishable.}\n\\label{tab:bm25}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Random} & \\textbf{Embedding} & \\textbf{Dataflow} & \\textbf{BM25} & \\textbf{BM25$-$Emb} \\\\\n\\midrule\nQwen & 0.529 & 0.531 & 0.525 & 0.528 & $-$0.35pp \\\\\nStarCoder & 0.443 & 0.440 & 0.428 & 0.437 & $-$0.25pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe observe that CoCoHaNeRe's reported $-27$pp harm was not reproduced in our controlled setup with either BM25 or embedding negatives, suggesting the effect is attributable to other experimental differences (scale, encoder, evaluation protocol) rather than the BM25-vs-embedding distinction.\n\n\\subsection{No Downstream Signal on SWE-bench Lite}\n\\label{sec:swebench}\n\nTable~\\ref{tab:swebench} reports end-to-end resolve rates on SWE-bench Lite (300 instances) using a Qwen3.6-27B agent.\nThe largest gap across all conditions is 3.0pp (Qwen-embedding 25.0\\% vs StarCoder-dataflow 22.0\\%), well within the $\\pm$5pp binomial confidence interval.\nBootstrap resampling (10,000 iterations) confirms all pairwise comparisons are non-significant ($p > 0.80$).\n\n\\begin{table}[t]\n\\centering\n\\caption{SWE-bench Lite resolve rates. No mining strategy produces detectable downstream improvement.}\n\\label{tab:swebench}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Strategy} & \\textbf{Resolve \\%} & \\textbf{$\\Delta$ vs Rand} & \\textbf{95\\% Boot.\\ CI} \\\\\n\\midrule\n\\multirow{3}{*}{Qwen} & Random & 24.67 & --- & [19.9, 29.4] \\\\\n & Embedding & 25.00 & +0.33pp & [20.2, 29.8] \\\\\n & Dataflow & 24.33 & $-$0.33pp & [19.6, 29.1] \\\\\n\\midrule\n\\multirow{3}{*}{StarCoder} & Random & 22.67 & --- & [18.0, 27.3] \\\\\n & Embedding & 22.33 & $-$0.34pp & [17.7, 27.0] \\\\\n & Dataflow & 22.00 & $-$0.67pp & [17.3, 26.7] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith 300 binary outcomes at a base rate of $\\sim$25\\%, the binomial standard error is $\\sqrt{0.25 \\times 0.75 / 300} \\approx 0.025$, yielding a CI half-width of $\\sim$5pp.\nDetecting a 0.5pp retrieval difference would require $N \\approx 60{,}000$ instances.\nThis is not a power problem we can fix---it is a fundamental limitation of downstream evaluation for detecting sub-1pp retrieval differences.\n\n\\subsection{External Validation: RepoBench-R}\n\\label{sec:repobench}\n\nTable~\\ref{tab:repobench} reports R@1 on RepoBench-R (easy and hard splits, $\\sim$8K instances each).\nAll confidence intervals overlap across strategies.\nThe inconsistent sign pattern across encoders (positive for Qwen, negative for StarCoder) replicates the main result: strategy differences are noise.\n\n\\begin{table}[t]\n\\centering\n\\caption{RepoBench-R R@1 (\\%) by strategy, encoder, and split. $\\pm$ indicates 95\\% bootstrap CI half-width.}\n\\label{tab:repobench}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Split} & \\textbf{Encoder} & \\textbf{Random} & \\textbf{Embedding} & \\textbf{Dataflow} & \\textbf{$\\Delta$ E$-$R} \\\\\n\\midrule\n\\multirow{2}{*}{Easy} & Qwen & 71.2$\\pm$1.4 & 71.5$\\pm$1.5 & 70.9$\\pm$1.6 & +0.3pp \\\\\n & StarCoder & 68.5$\\pm$1.6 & 68.1$\\pm$1.7 & 67.8$\\pm$1.8 & $-$0.4pp \\\\\n\\midrule\n\\multirow{2}{*}{Hard} & Qwen & 43.1$\\pm$2.0 & 43.4$\\pm$2.1 & 42.7$\\pm$2.2 & +0.3pp \\\\\n & StarCoder & 39.8$\\pm$2.2 & 39.3$\\pm$2.4 & 38.9$\\pm$2.5 & $-$0.5pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Stratified Analysis}\n\\label{sec:stratified}\n\nTable~\\ref{tab:stratified} breaks down the embedding-minus-random delta across five strata on Qwen.\nNo stratum produces a significant effect after Bonferroni correction (10 comparisons, $\\alpha_{\\text{adj}}=0.005$).\nThe most informative finding: the 34\\% of instances with structural data show a tiny positive dataflow signal ($+0.40$pp), completely washed out by the 66\\% fallback instances.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-stratum $\\Delta$(embedding $-$ random) R@1 on Qwen. None significant after correction.}\n\\label{tab:stratified}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Stratum} & \\textbf{$N$} & \\textbf{$\\Delta$ R@1 (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nRepo small ($<$200 files) & 4,596 & +0.80 & [$-$1.5, +3.1] \\\\\nRepo large ($\\geq$200 files) & 39,577 & $-$0.15 & [$-$0.9, +0.6] \\\\\nPool small ($<$30) & 12,044 & +0.35 & [$-$1.2, +1.9] \\\\\nPool large ($\\geq$30) & 32,129 & $-$0.20 & [$-$1.0, +0.6] \\\\\nHigh query-pos sim ($>$0.95) & 28,800 & $-$0.10 & [$-$0.8, +0.6] \\\\\nLow query-pos sim ($\\leq$0.95) & 15,373 & +0.55 & [$-$0.9, +2.0] \\\\\nStruct.\\ available (34\\%) & 15,133 & +0.15 & [$-$1.2, +1.5] \\\\\nStruct.\\ fallback (66\\%) & 29,040 & +0.25 & [$-$0.5, +1.0] \\\\\nNeg.\\ diff.\\ Q1 (easiest) & 11,043 & +0.60 & [$-$1.5, +2.7] \\\\\nNeg.\\ diff.\\ Q4 (hardest) & 11,043 & $-$0.30 & [$-$2.3, +1.7] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pool Size Sensitivity}\n\\label{sec:pool}\n\nTable~\\ref{tab:pool} evaluates strategy rankings at pool sizes $\\{50, 100, 200, 500\\}$.\nStrategy rankings are highly unstable: the best strategy changes 3 times across 4 pool sizes (stability $= 25\\%$), and Kendall's $\\tau$ between pool-50 and pool-500 rankings is only 0.33.\nThis instability holds for both encoders.\n\n\\begin{table}[t]\n\\centering\n\\caption{Strategy ranking stability across pool sizes (Qwen).}\n\\label{tab:pool}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Pool} & \\textbf{Rand R@1} & \\textbf{Emb R@1} & \\textbf{DF R@1} & \\textbf{Best} \\\\\n\\midrule\n50 & 0.529 & 0.531 & 0.525 & Emb \\\\\n100 & 0.412 & 0.409 & 0.405 & Rand \\\\\n200 & 0.324 & 0.327 & 0.325 & Emb \\\\\n500 & 0.231 & 0.229 & 0.230 & Rand \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Strategy ranking stability across pool sizes (StarCoder).}\n\\label{tab:pool_sc}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Pool} & \\textbf{Rand R@1} & \\textbf{Emb R@1} & \\textbf{DF R@1} & \\textbf{Best} \\\\\n\\midrule\n50 & 0.443 & 0.440 & 0.428 & Rand \\\\\n100 & 0.341 & 0.338 & 0.331 & Rand \\\\\n200 & 0.262 & 0.264 & 0.259 & Emb \\\\\n500 & 0.178 & 0.175 & 0.177 & Rand \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scale-Dependent Strategy Effects}\n\\label{sec:scale}\n\nTable~\\ref{tab:scale} reveals the paper's most explanatory result.\nAt 1K training instances, embedding mining shows $+1.3$pp---consistent with pilot-scale findings.\nThis advantage decreases monotonically to $+0.6$pp at 3K and $+0.2$pp at 5K (full scale).\nDataflow mining follows the same pattern, dropping from $+0.7$pp to $-0.45$pp.\n\n\\begin{table}[t]\n\\centering\n\\caption{Strategy effects decrease monotonically with training scale (Qwen, 1 seed).}\n\\label{tab:scale}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Train size} & \\textbf{Rand R@1} & \\textbf{Emb R@1} & \\textbf{$\\Delta$ (pp)} & \\textbf{DF $\\Delta$ (pp)} \\\\\n\\midrule\n1K & 0.505 & 0.518 & +1.30 & +0.70 \\\\\n3K & 0.520 & 0.526 & +0.60 & +0.10 \\\\\n5K (full) & 0.529 & 0.531 & +0.20 & $-$0.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mechanism is straightforward: with more training data, random negatives sample a wider region of the embedding space, effectively approximating the coverage that curated negatives provide by design.\nAt small scale, curated negatives concentrate training signal on the decision boundary; at large scale, random sampling covers the boundary through sheer volume.\nThis phenomenon parallels batch-size scaling effects observed in visual contrastive learning.\n\n\\subsection{Failure Analysis}\n\\label{sec:failure}\n\nManual categorization of 50 retrieval failures (cases where all strategies fail) reveals a ceiling on the potential benefit of any mining strategy (Table~\\ref{tab:failure}).\nThe dominant failure mode (36\\%) is that the gold file is lexically dissimilar to the query, requiring fundamentally different approaches (e.g., multi-modal queries with error traces).\nOnly 10\\% of failures involve cases where structural connectivity could plausibly help.\n\n\\begin{table}[t]\n\\centering\n\\caption{Failure category breakdown ($n=50$). Structure can address only $\\sim$10\\% of failures.}\n\\label{tab:failure}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Category} & \\textbf{Count} & \\textbf{\\%} \\\\\n\\midrule\nGold file lexically dissimilar & 18 & 36 \\\\\nConfig / test / non-code files & 12 & 24 \\\\\nLarge repo dilution ($>$500 files) & 8 & 16 \\\\\nCross-language dependency & 4 & 8 \\\\\nStructural connectivity helps & 5 & 10 \\\\\nAmbiguous & 3 & 6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Representation Geometry Convergence}\n\\label{sec:geometry}\n\nTable~\\ref{tab:geometry} presents the mechanistic core of our analysis.\nBefore fine-tuning, mining strategies produce markedly different negative difficulties: on Qwen, random negatives have margin 0.074 while embedding negatives have margin 0.017 (ratio 4.35$\\times$).\nAfter fine-tuning, this ratio collapses to 1.29$\\times$ (margins 0.067 vs.\\ 0.052).\nFine-tuning erases 78\\% of the pretrained margin difference on Qwen and 65\\% on StarCoder.\n\n\\begin{table}[t]\n\\centering\n\\caption{Representation geometry pre- vs.\\ post-fine-tuning. Fine-tuning collapses margin differences across strategies.}\n\\label{tab:geometry}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Phase} & \\textbf{Rand.\\ margin} & \\textbf{Emb.\\ margin} & \\textbf{DF margin} & \\textbf{Ratio (R/E)} \\\\\n\\midrule\n\\multirow{2}{*}{Qwen} & Pretrained & 0.074 & 0.017 & 0.029 & 4.35 \\\\\n & Fine-tuned & 0.067 & 0.052 & 0.059 & 1.29 \\\\\n\\midrule\n\\multirow{2}{*}{StarCoder} & Pretrained & 0.194 & 0.067 & 0.119 & 2.90 \\\\\n & Fine-tuned & 0.073 & 0.057 & 0.065 & 1.28 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe contrastive objective drives all strategies toward the same representation geometry regardless of the specific negatives used.\nPretrained geometry---which determines initial negative difficulty---is a transient condition that gets erased during training.\nThis explains why pilot-scale results showed strategy effects (insufficient training to erase geometry) while full-scale results do not (sufficient training to converge).\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Why strategies converge.}\nThe representation geometry analysis (\\S\\ref{sec:geometry}) provides a unified explanation.\nThe contrastive loss optimizes for a target geometry (margins that minimize loss), and LoRA fine-tuning has sufficient capacity to reach this target from any starting point defined by the mining strategy.\nDifferent strategies change the \\emph{path} through representation space but converge to the same \\emph{destination}.\nAt small scale (\\S\\ref{sec:scale}), training is insufficient to complete this convergence, so initial differences persist and strategy choice matters.\nAt full scale, convergence is complete and strategy choice is irrelevant.\n\n\\paragraph{Implications for the BM25-proxy debate.}\nOur finding that BM25 and embedding negatives are indistinguishable (\\S\\ref{sec:bm25}) means that prior work's reported harm cannot be attributed to the BM25-vs-embedding distinction.\nWe observe that CoCoHaNeRe's $-27$pp effect was not reproduced in our setup with either method, suggesting other experimental factors (training scale, encoder architecture, evaluation protocol) are responsible.\nWe frame this as an \\emph{observation} rather than a correction, as we cannot fully disentangle the confounds.\n\n\\paragraph{Training-time vs.\\ inference-time structure.}\nOur null result for dataflow-aware training-time mining contrasts with reported gains from inference-time graph navigation methods (LocAgent: $+8$--$12$pp on SWE-bench; CodexGraph: $+5$pp).\nThe key difference: training-time mining fixes structural signal at corpus construction time, but the relevant structure changes per query.\nInference-time methods adapt structural navigation to the specific query context.\nThis reframes our contribution: structure matters for code retrieval, but the mechanism for incorporating it should be inference-time navigation, not training-time negative curation.\n\n\\paragraph{Practical recommendations.}\n\\begin{enumerate}\n    \\item If your training set exceeds $\\sim$5K instances, random negative sampling is sufficient. Save the GPU time that would be spent on mining.\n    \\item If your training set is small ($<$2K), embedding-distance mining provides a modest benefit ($+1.3$pp) worth the overhead.\n    \\item Do not optimize mining strategy based on a single pool size---rankings are unstable (Kendall $\\tau = 0.33$).\n    \\item For leveraging code structure in retrieval, invest in inference-time graph navigation rather than training-time negative mining.\n    \\item If structural negative mining is attempted, invest in extraction coverage first: at 34\\% coverage, the structural signal is too diluted to surface.\n\\end{enumerate}\n\n\\paragraph{Limitations.}\nOur study uses two 3B-parameter encoders; larger models may exhibit different convergence behavior.\nAll training uses LoRA; full fine-tuning might preserve more strategy-specific signal.\nThe dataflow extraction covers only 34\\% of instances; higher coverage might change the dataflow result, though the stratified analysis (\\S\\ref{sec:stratified}) suggests the effect would remain small.\nSWE-bench Lite's 300 instances provide limited statistical power for downstream evaluation.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe presented a controlled study of hard negative mining strategies for contrastive code retrieval, finding that no strategy---embedding-distance, dataflow-aware, or BM25---reliably outperforms random baselines at full training scale.\nThe representation geometry convergence analysis reveals the mechanism: fine-tuning acts as a geometry equalizer, collapsing pretrained margin differences by 65--78\\% and rendering the initial negative difficulty distribution irrelevant.\nData-scaling ablations show that mining advantages observed at pilot scale vanish monotonically with training set size, consistent with scale substituting for curation.\n\nOur negative results carry actionable implications: practitioners should prioritize training data volume over mining sophistication, use random negatives at scale, and leverage code structure through inference-time navigation rather than training-time negative selection.\nWe hope this work encourages the community to report and value negative results in retrieval research, where publication bias toward positive findings can mislead practitioners into over-investing in techniques that do not survive rigorous evaluation.\n\n%==============================================================================\n\\appendix\n\\section{Temperature Ablation}\n\\label{app:temperature}\n%==============================================================================\n\nTable~\\ref{tab:temp} shows that the null result holds across temperatures $\\tau \\in \\{0.05, 0.10, 0.20\\}$.\nStrategy rankings are unstable across temperatures (embedding leads at $\\tau=0.10$ but trails at $\\tau=0.20$), confirming the absence of a robust strategy effect.\nHigher temperatures degrade all strategies uniformly by $\\sim$2.5pp at $\\tau=0.20$.\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature $\\times$ strategy interaction (R@1, Qwen).}\n\\label{tab:temp}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\tau$ & \\textbf{Random} & \\textbf{Embedding} & $\\Delta$ \\textbf{E$-$R} & $\\Delta$ \\textbf{DF$-$R} \\\\\n\\midrule\n0.05 & 0.529 & 0.531 & +0.20pp & $-$0.45pp \\\\\n0.10 & 0.522 & 0.525 & +0.35pp & $-$0.15pp \\\\\n0.20 & 0.504 & 0.503 & $-$0.10pp & $-$0.25pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Dynamic Mining Ablation}\n\\label{app:dynamic}\n%==============================================================================\n\nRe-mining embedding negatives per epoch (dynamic) vs.\\ once from the pretrained encoder (static) yields negligible improvement (Table~\\ref{tab:dynamic}): $+0.05$pp on both encoders at $3.4\\times$ time overhead.\nThe encoder changes minimally during LoRA fine-tuning (cosine similarity between epoch-0 and epoch-3 embeddings $>0.995$), so dynamic and static negatives are nearly identical.\n\n\\begin{table}[h]\n\\centering\n\\caption{Static vs.\\ dynamic embedding mining.}\n\\label{tab:dynamic}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Static R@1} & \\textbf{Dynamic R@1} & $\\Delta$ \\textbf{(pp)} & \\textbf{Time $\\times$} \\\\\n\\midrule\nQwen & 0.531 & 0.532 & +0.05 & 3.4$\\times$ \\\\\nStarCoder & 0.440 & 0.440 & +0.05 & 3.4$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Hop Count Ablation}\n\\label{app:hop}\n%==============================================================================\n\nExpanding call-graph scope from 1-hop to 3-hop does not rescue the dataflow strategy (Table~\\ref{tab:hop}).\nAll hop counts produce R@1 within noise of random (0.529).\n3-hop slightly worsens performance by over-expanding the connected set, reducing the pool of available structural negatives.\n\n\\begin{table}[h]\n\\centering\n\\caption{Hop count ablation (Qwen, dataflow strategy, 1 seed).}\n\\label{tab:hop}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Hops} & \\textbf{Connected/query} & \\textbf{Neg.\\ available} & \\textbf{R@1} & $\\Delta$ \\textbf{vs Rand} \\\\\n\\midrule\n1 & 2.1 & 47.9 & 0.523 & $-$0.60pp \\\\\n2 & 4.8 & 45.2 & 0.525 & $-$0.45pp \\\\\n3 & 11.3 & 38.7 & 0.521 & $-$0.80pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Fusion Head Ablation}\n\\label{app:fusion}\n%==============================================================================\n\nAdding structural features at inference time via a combined scoring head does not improve over embedding-only retrieval (Table~\\ref{tab:fusion}).\nThe structural-only head performs poorly (R@1 $= 0.312$), and the combined head slightly underperforms embedding-only ($-0.25$pp), suggesting the model learns to partially ignore the noisy structural channel.\n\n\\begin{table}[h]\n\\centering\n\\caption{Fusion head ablation (Qwen, best checkpoint).}\n\\label{tab:fusion}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Head} & \\textbf{R@1} & \\textbf{R@5} & $\\Delta$ \\textbf{vs Emb} \\\\\n\\midrule\nEmbedding only & 0.531 & 0.960 & --- \\\\\nStructural only & 0.312 & 0.620 & $-$21.9pp \\\\\nCombined & 0.529 & 0.955 & $-$0.25pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Distance Weighting Ablation}\n\\label{app:distance}\n%==============================================================================\n\nUsing dataflow-distance-weighted negative selection instead of binary connected/disconnected yields a marginal $+0.10$pp over binary, still underperforming random by $0.35$pp (Table~\\ref{tab:dist_weight}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Distance weighting ablation (Qwen, 1 seed).}\n\\label{tab:dist_weight}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Selection} & \\textbf{R@1} & $\\Delta$ \\textbf{vs Rand} & $\\Delta$ \\textbf{vs Binary} \\\\\n\\midrule\nRandom & 0.529 & --- & --- \\\\\nBinary disconnect & 0.525 & $-$0.45pp & --- \\\\\nDistance weighted & 0.526 & $-$0.35pp & +0.10pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\bibliography{custom}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42fbccaa-e53d-441b-af0a-b8b9852af260",
  "isSidechain": false,
  "requestId": "req_011Cb2p1ZoBdtxkLEaKXex33",
  "type": "assistant",
  "uuid": "020b2fb4-4b7c-4b2d-b6af-4c7f7d92dad8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLhrqytihNbwqRpoPHLPYc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3526,
      "cache_read_input_tokens": 39029,
      "output_tokens": 10397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3526,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10397,
          "cache_read_input_tokens": 39029,
          "cache_creation_input_tokens": 3526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3526
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

_source line 21 · 2026-05-14T16:57:47.963Z_

<details><summary>↩ Tool result · `toolu_0136iCCGygQMFd8aAjHSqXuX`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "020b2fb4-4b7c-4b2d-b6af-4c7f7d92dad8",
  "isSidechain": false,
  "promptId": "66bbad76-7453-4fae-883a-01da252df421",
  "type": "user",
  "uuid": "b67575a9-7ef2-4bd9-8b3a-137b74663c89",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{adjustbox}\n\n\\aclfinalcopy\n\n\\title{Why Hard Negative Mining Strategies Don't Differentiate\\\\for Code Retrieval at Scale}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nHard negative mining is widely believed to be critical for training contrastive code retrievers, yet the field lacks controlled comparisons isolating the effect of mining strategy from confounding factors such as training scale, encoder choice, and evaluation protocol.\nWe present a systematic study of four negative mining strategies---random, embedding-distance, dataflow-aware, and BM25---across two decoder-only code encoders (Qwen2.5-Coder-3B and StarCoder2-3B) with 9 random seeds per condition.\nOur central finding is \\emph{negative}: at full training scale ($\\sim$44K instances), no mining strategy reliably outperforms random baselines.\nThe largest observed effect is $+0.20$ percentage points (pp) for embedding mining on Qwen ($p=0.58$), with 95\\% confidence intervals spanning zero for all comparisons.\nStrategy rankings are unstable across pool sizes (Kendall $\\tau=0.33$ between pool 50 and 500), and downstream SWE-bench Lite evaluation shows no differentiation ($\\Delta < 0.67$pp, bootstrap CI width $\\sim$5pp).\nWe provide a mechanistic explanation: fine-tuning acts as a \\emph{geometry equalizer}, collapsing pretrained margin differences across strategies by 65--78\\%.\nA data-scaling ablation reveals that mining advantages observed at pilot scale ($+1.3$pp at 1K instances) vanish monotonically with training set size, suggesting that scale substitutes for curation in contrastive code retrieval.\nWe additionally show that BM25 negatives perform indistinguishably from embedding negatives ($p > 0.42$), preventing closure of the argument that prior work's reported harm from hard negatives was caused by BM25-proxy methodology.\nOur results caution against over-investing in mining strategy optimization and redirect attention toward training scale and inference-time structural methods.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nRepository-level code retrieval---selecting the relevant source files from a large codebase given a bug report or issue description---is a critical bottleneck in automated software repair pipelines \\cite{jimenez2024swebench}.\nContrastive learning has emerged as the dominant paradigm for training dense code retrievers, where the choice of \\emph{hard negatives} is believed to strongly influence retrieval quality.\n\nPrior work offers conflicting guidance on hard negative mining for code.\nCoCoHaNeRe reports that embedding-distance negatives \\emph{harm} code search by up to 27 percentage points in R@1, advocating instead for keyword-based retrieval of negatives.\nHowever, this finding was obtained using BM25 as a proxy for embedding distance, raising the question of whether the reported harm reflects true embedding mining or confounds introduced by the proxy.\nMeanwhile, the contrastive learning literature in NLP and vision consistently finds that harder negatives improve representation quality, at least up to a difficulty threshold beyond which false negatives degrade training.\n\nWe set out to resolve this contradiction through a controlled study comparing four negative mining strategies for code retrieval: (1) random sampling, (2) true embedding-distance mining, (3) structure-grounded (dataflow-aware) mining using inter-procedural call-graph analysis, and (4) BM25-based mining.\nWe train with each strategy on two decoder-only code encoders with distinct pretrained representation geometries---Qwen2.5-Coder-3B (saturated, $\\text{pos\\_sim}=0.986$) and StarCoder2-3B (healthy, $\\text{pos\\_sim}=0.798$)---using 9 random seeds per condition to obtain reliable confidence intervals.\n\nOur findings are predominantly negative, which we argue is itself a contribution:\n\n\\begin{enumerate}\n    \\item \\textbf{No strategy differentiates at scale.} At full training scale ($\\sim$44K instances), all mining strategies produce statistically indistinguishable R@1 on both encoders. The largest effect ($+0.20$pp) has $p=0.58$.\n    \\item \\textbf{Representation geometry convergence.} Fine-tuning collapses pretrained margin differences by 65--78\\%, explaining why strategies that produce different negative difficulties in the pretrained space converge after training.\n    \\item \\textbf{Scale substitutes for curation.} Mining advantages observed at 1K instances ($+1.3$pp) vanish monotonically as training data grows, reaching $+0.2$pp at 5K instances.\n    \\item \\textbf{BM25 $\\approx$ embedding negatives.} BM25 and embedding-distance negatives are statistically indistinguishable ($p > 0.42$), preventing attribution of prior work's reported harm to the BM25-proxy methodology.\n    \\item \\textbf{Unstable strategy rankings.} Rankings flip across pool sizes (stability $= 25\\%$), temperatures, and encoders, indicating that reported differences in prior work may be evaluation artifacts.\n\\end{enumerate}\n\nThese results caution practitioners against investing GPU time in sophisticated mining pipelines when simple random sampling suffices at scale, and redirect attention toward training data volume and inference-time structural navigation methods.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Hard Negative Mining for Retrieval.}\nHard negative mining has a long history in metric learning and dense retrieval.\nANCE~\\cite{xiong2021approximate} periodically refreshes negatives using the current encoder, DPR~\\cite{karpukhin2020dense} uses BM25 negatives for open-domain QA, and curriculum-based approaches gradually increase negative difficulty during training.\nFor code, CoCoHaNeRe reports that embedding-distance negatives harm code search, but uses BM25 as a proxy rather than true embedding distance.\nOur work directly tests this claim with proper controls.\n\n\\paragraph{Code Retrieval.}\nDense retrieval for code has been explored with encoder-only models (GraphCodeBERT, CodeBERT) and more recently with decoder-only models fine-tuned for retrieval (SweRank, SWE-Fixer).\nThese systems typically use random or in-batch negatives without systematic comparison of mining strategies.\nRepoBench~\\cite{liu2023repobench} provides a cross-file retrieval benchmark that we use for external validation.\n\n\\paragraph{Structure-Aware Code Understanding.}\nGraph-based approaches to code operate at either training time or inference time.\nTraining-time methods (GraphCodeBERT) encode structural features into the model.\nInference-time methods (CodexGraph, LocAgent, RANGER) navigate code structure during retrieval using the query context.\nOur dataflow-aware mining falls in the training-time category; our null result suggests inference-time approaches may be more effective for leveraging structure.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Problem Setting}\n\nGiven a repository $\\mathcal{R}$ with source files $\\{f_1, \\ldots, f_n\\}$ and a query $q$ (e.g., a bug report), the retrieval task is to rank files by relevance.\nWe train a contrastive encoder $E_\\theta$ using InfoNCE loss with temperature $\\tau$:\n\\begin{equation}\n\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(q, f^+)/\\tau)}{\\exp(\\text{sim}(q, f^+)/\\tau) + \\sum_{i=1}^{K} \\exp(\\text{sim}(q, f_i^-)/\\tau)}\n\\end{equation}\nwhere $f^+$ is the gold file and $\\{f_i^-\\}_{i=1}^K$ are negatives selected by the mining strategy.\n\n\\subsection{Negative Mining Strategies}\n\nWe compare four strategies that differ only in how $\\{f_i^-\\}$ are selected:\n\n\\paragraph{Random.} Sample $K$ negatives uniformly from non-gold files in the repository.\n\n\\paragraph{Embedding-distance.} Using the pretrained encoder, compute cosine similarity between the query and all non-gold files. Select the top-$K$ most similar as hard negatives.\n\n\\paragraph{Dataflow-aware.} Using inter-procedural call-graph analysis via CodeQL, identify files that are \\emph{not} reachable from the gold file within 2 hops. Among these structurally disconnected files, select the top-$K$ by embedding similarity. This produces negatives that are semantically similar but structurally unrelated---the intuition being that structural disconnection is a stronger signal of irrelevance than embedding distance alone. Structural data is available for 34\\% of training instances; the remaining 66\\% fall back to embedding-distance mining.\n\n\\paragraph{BM25.} Tokenize query and files, compute BM25 scores, select top-$K$ non-gold files. This replicates the methodology attributed to ``embedding negatives'' in prior work.\n\n\\subsection{Encoders}\n\nWe fine-tune two 3B-parameter decoder-only code models using LoRA:\n\n\\begin{itemize}\n    \\item \\textbf{Qwen2.5-Coder-3B}: Pretrained with Fill-in-the-Middle. Exhibits saturated representation geometry ($\\text{pos\\_sim}=0.986$, margin $= 0.074$ for random negatives).\n    \\item \\textbf{StarCoder2-3B}: Pretrained with Fill-in-the-Middle on a different corpus. Healthier geometry ($\\text{pos\\_sim}=0.798$, margin $= 0.194$ for random negatives).\n\\end{itemize}\n\n\\subsection{Training Protocol}\n\nAll models are trained on $\\sim$44K instances from SWE-smith with $K=3$ negatives, $\\tau=0.05$, LoRA rank 16, for 3 epochs.\nEach strategy $\\times$ encoder combination is trained with 9 random seeds.\nEvaluation uses R@1 at pool size 50 on a held-out validation set unless otherwise noted.\n\n%==============================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n%==============================================================================\n\n\\subsection{Main Result: No Strategy Differentiates at Full Scale}\n\\label{sec:main_result}\n\nTable~\\ref{tab:main} presents the central result.\nOn Qwen, embedding mining achieves $+0.20$pp over random ($p=0.58$); on StarCoder, it achieves $-0.35$pp ($p=0.47$).\nNeither difference is statistically significant, and the signs are inconsistent across encoders---a signature of noise, not signal.\nDataflow-aware mining shows slight harm on both encoders ($-0.45$pp Qwen, $-1.50$pp StarCoder), with the StarCoder result reaching $p=0.015$ before multiple-testing correction but not surviving Bonferroni adjustment across the study's comparisons.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full-scale R@1 by strategy and encoder (9 seeds, pool=50). No strategy significantly outperforms random.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Strategy} & \\textbf{Mean R@1} & \\textbf{Std} & \\textbf{95\\% CI} & \\textbf{$\\Delta$ vs Rand} \\\\\n\\midrule\n\\multirow{3}{*}{Qwen} & Random & 0.529 & 0.009 & [.522, .536] & --- \\\\\n & Embedding & 0.531 & 0.009 & [.524, .538] & +0.20pp \\\\\n & Dataflow & 0.525 & 0.011 & [.516, .533] & $-$0.45pp \\\\\n\\midrule\n\\multirow{3}{*}{StarCoder} & Random & 0.443 & 0.011 & [.435, .451] & --- \\\\\n & Embedding & 0.440 & 0.012 & [.430, .449] & $-$0.35pp \\\\\n & Dataflow & 0.428 & 0.014 & [.418, .438] & $-$1.50pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeed-to-seed variance ($\\sigma \\approx 0.009$--$0.014$) exceeds the strategy effects in all cases.\nThe confidence intervals for all pairwise strategy comparisons include zero:\nembedding $-$ random on Qwen: $[-0.62, +1.02]$pp;\nembedding $-$ random on StarCoder: $[-1.4, +0.7]$pp;\ndataflow $-$ random on StarCoder: $[-3.1, +0.1]$pp.\n\n\\subsection{BM25 Negatives Match Embedding Negatives}\n\\label{sec:bm25}\n\nTable~\\ref{tab:bm25} adds BM25 as a fourth strategy.\nBM25 negatives are statistically indistinguishable from embedding negatives on both encoders (Qwen: $-0.35$pp, $p=0.42$; StarCoder: $-0.25$pp, $p=0.55$).\nThis prevents closing the argument that prior work's reported harm from hard negatives was caused by the BM25-proxy methodology specifically.\nThe high overlap ($\\sim$60\\%) between BM25 and embedding top-$K$ negatives at full scale explains this convergence.\n\n\\begin{table}[t]\n\\centering\n\\caption{Four-strategy comparison including BM25 baseline. BM25 and embedding negatives are indistinguishable.}\n\\label{tab:bm25}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Random} & \\textbf{Embedding} & \\textbf{Dataflow} & \\textbf{BM25} & \\textbf{BM25$-$Emb} \\\\\n\\midrule\nQwen & 0.529 & 0.531 & 0.525 & 0.528 & $-$0.35pp \\\\\nStarCoder & 0.443 & 0.440 & 0.428 & 0.437 & $-$0.25pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe observe that CoCoHaNeRe's reported $-27$pp harm was not reproduced in our controlled setup with either BM25 or embedding negatives, suggesting the effect is attributable to other experimental differences (scale, encoder, evaluation protocol) rather than the BM25-vs-embedding distinction.\n\n\\subsection{No Downstream Signal on SWE-bench Lite}\n\\label{sec:swebench}\n\nTable~\\ref{tab:swebench} reports end-to-end resolve rates on SWE-bench Lite (300 instances) using a Qwen3.6-27B agent.\nThe largest gap across all conditions is 3.0pp (Qwen-embedding 25.0\\% vs StarCoder-dataflow 22.0\\%), well within the $\\pm$5pp binomial confidence interval.\nBootstrap resampling (10,000 iterations) confirms all pairwise comparisons are non-significant ($p > 0.80$).\n\n\\begin{table}[t]\n\\centering\n\\caption{SWE-bench Lite resolve rates. No mining strategy produces detectable downstream improvement.}\n\\label{tab:swebench}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Strategy} & \\textbf{Resolve \\%} & \\textbf{$\\Delta$ vs Rand} & \\textbf{95\\% Boot.\\ CI} \\\\\n\\midrule\n\\multirow{3}{*}{Qwen} & Random & 24.67 & --- & [19.9, 29.4] \\\\\n & Embedding & 25.00 & +0.33pp & [20.2, 29.8] \\\\\n & Dataflow & 24.33 & $-$0.33pp & [19.6, 29.1] \\\\\n\\midrule\n\\multirow{3}{*}{StarCoder} & Random & 22.67 & --- & [18.0, 27.3] \\\\\n & Embedding & 22.33 & $-$0.34pp & [17.7, 27.0] \\\\\n & Dataflow & 22.00 & $-$0.67pp & [17.3, 26.7] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith 300 binary outcomes at a base rate of $\\sim$25\\%, the binomial standard error is $\\sqrt{0.25 \\times 0.75 / 300} \\approx 0.025$, yielding a CI half-width of $\\sim$5pp.\nDetecting a 0.5pp retrieval difference would require $N \\approx 60{,}000$ instances.\nThis is not a power problem we can fix---it is a fundamental limitation of downstream evaluation for detecting sub-1pp retrieval differences.\n\n\\subsection{External Validation: RepoBench-R}\n\\label{sec:repobench}\n\nTable~\\ref{tab:repobench} reports R@1 on RepoBench-R (easy and hard splits, $\\sim$8K instances each).\nAll confidence intervals overlap across strategies.\nThe inconsistent sign pattern across encoders (positive for Qwen, negative for StarCoder) replicates the main result: strategy differences are noise.\n\n\\begin{table}[t]\n\\centering\n\\caption{RepoBench-R R@1 (\\%) by strategy, encoder, and split. $\\pm$ indicates 95\\% bootstrap CI half-width.}\n\\label{tab:repobench}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Split} & \\textbf{Encoder} & \\textbf{Random} & \\textbf{Embedding} & \\textbf{Dataflow} & \\textbf{$\\Delta$ E$-$R} \\\\\n\\midrule\n\\multirow{2}{*}{Easy} & Qwen & 71.2$\\pm$1.4 & 71.5$\\pm$1.5 & 70.9$\\pm$1.6 & +0.3pp \\\\\n & StarCoder & 68.5$\\pm$1.6 & 68.1$\\pm$1.7 & 67.8$\\pm$1.8 & $-$0.4pp \\\\\n\\midrule\n\\multirow{2}{*}{Hard} & Qwen & 43.1$\\pm$2.0 & 43.4$\\pm$2.1 & 42.7$\\pm$2.2 & +0.3pp \\\\\n & StarCoder & 39.8$\\pm$2.2 & 39.3$\\pm$2.4 & 38.9$\\pm$2.5 & $-$0.5pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Stratified Analysis}\n\\label{sec:stratified}\n\nTable~\\ref{tab:stratified} breaks down the embedding-minus-random delta across five strata on Qwen.\nNo stratum produces a significant effect after Bonferroni correction (10 comparisons, $\\alpha_{\\text{adj}}=0.005$).\nThe most informative finding: the 34\\% of instances with structural data show a tiny positive dataflow signal ($+0.40$pp), completely washed out by the 66\\% fallback instances.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-stratum $\\Delta$(embedding $-$ random) R@1 on Qwen. None significant after correction.}\n\\label{tab:stratified}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Stratum} & \\textbf{$N$} & \\textbf{$\\Delta$ R@1 (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nRepo small ($<$200 files) & 4,596 & +0.80 & [$-$1.5, +3.1] \\\\\nRepo large ($\\geq$200 files) & 39,577 & $-$0.15 & [$-$0.9, +0.6] \\\\\nPool small ($<$30) & 12,044 & +0.35 & [$-$1.2, +1.9] \\\\\nPool large ($\\geq$30) & 32,129 & $-$0.20 & [$-$1.0, +0.6] \\\\\nHigh query-pos sim ($>$0.95) & 28,800 & $-$0.10 & [$-$0.8, +0.6] \\\\\nLow query-pos sim ($\\leq$0.95) & 15,373 & +0.55 & [$-$0.9, +2.0] \\\\\nStruct.\\ available (34\\%) & 15,133 & +0.15 & [$-$1.2, +1.5] \\\\\nStruct.\\ fallback (66\\%) & 29,040 & +0.25 & [$-$0.5, +1.0] \\\\\nNeg.\\ diff.\\ Q1 (easiest) & 11,043 & +0.60 & [$-$1.5, +2.7] \\\\\nNeg.\\ diff.\\ Q4 (hardest) & 11,043 & $-$0.30 & [$-$2.3, +1.7] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pool Size Sensitivity}\n\\label{sec:pool}\n\nTable~\\ref{tab:pool} evaluates strategy rankings at pool sizes $\\{50, 100, 200, 500\\}$.\nStrategy rankings are highly unstable: the best strategy changes 3 times across 4 pool sizes (stability $= 25\\%$), and Kendall's $\\tau$ between pool-50 and pool-500 rankings is only 0.33.\nThis instability holds for both encoders.\n\n\\begin{table}[t]\n\\centering\n\\caption{Strategy ranking stability across pool sizes (Qwen).}\n\\label{tab:pool}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Pool} & \\textbf{Rand R@1} & \\textbf{Emb R@1} & \\textbf{DF R@1} & \\textbf{Best} \\\\\n\\midrule\n50 & 0.529 & 0.531 & 0.525 & Emb \\\\\n100 & 0.412 & 0.409 & 0.405 & Rand \\\\\n200 & 0.324 & 0.327 & 0.325 & Emb \\\\\n500 & 0.231 & 0.229 & 0.230 & Rand \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Strategy ranking stability across pool sizes (StarCoder).}\n\\label{tab:pool_sc}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Pool} & \\textbf{Rand R@1} & \\textbf{Emb R@1} & \\textbf{DF R@1} & \\textbf{Best} \\\\\n\\midrule\n50 & 0.443 & 0.440 & 0.428 & Rand \\\\\n100 & 0.341 & 0.338 & 0.331 & Rand \\\\\n200 & 0.262 & 0.264 & 0.259 & Emb \\\\\n500 & 0.178 & 0.175 & 0.177 & Rand \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scale-Dependent Strategy Effects}\n\\label{sec:scale}\n\nTable~\\ref{tab:scale} reveals the paper's most explanatory result.\nAt 1K training instances, embedding mining shows $+1.3$pp---consistent with pilot-scale findings.\nThis advantage decreases monotonically to $+0.6$pp at 3K and $+0.2$pp at 5K (full scale).\nDataflow mining follows the same pattern, dropping from $+0.7$pp to $-0.45$pp.\n\n\\begin{table}[t]\n\\centering\n\\caption{Strategy effects decrease monotonically with training scale (Qwen, 1 seed).}\n\\label{tab:scale}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Train size} & \\textbf{Rand R@1} & \\textbf{Emb R@1} & \\textbf{$\\Delta$ (pp)} & \\textbf{DF $\\Delta$ (pp)} \\\\\n\\midrule\n1K & 0.505 & 0.518 & +1.30 & +0.70 \\\\\n3K & 0.520 & 0.526 & +0.60 & +0.10 \\\\\n5K (full) & 0.529 & 0.531 & +0.20 & $-$0.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mechanism is straightforward: with more training data, random negatives sample a wider region of the embedding space, effectively approximating the coverage that curated negatives provide by design.\nAt small scale, curated negatives concentrate training signal on the decision boundary; at large scale, random sampling covers the boundary through sheer volume.\nThis phenomenon parallels batch-size scaling effects observed in visual contrastive learning.\n\n\\subsection{Failure Analysis}\n\\label{sec:failure}\n\nManual categorization of 50 retrieval failures (cases where all strategies fail) reveals a ceiling on the potential benefit of any mining strategy (Table~\\ref{tab:failure}).\nThe dominant failure mode (36\\%) is that the gold file is lexically dissimilar to the query, requiring fundamentally different approaches (e.g., multi-modal queries with error traces).\nOnly 10\\% of failures involve cases where structural connectivity could plausibly help.\n\n\\begin{table}[t]\n\\centering\n\\caption{Failure category breakdown ($n=50$). Structure can address only $\\sim$10\\% of failures.}\n\\label{tab:failure}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Category} & \\textbf{Count} & \\textbf{\\%} \\\\\n\\midrule\nGold file lexically dissimilar & 18 & 36 \\\\\nConfig / test / non-code files & 12 & 24 \\\\\nLarge repo dilution ($>$500 files) & 8 & 16 \\\\\nCross-language dependency & 4 & 8 \\\\\nStructural connectivity helps & 5 & 10 \\\\\nAmbiguous & 3 & 6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Representation Geometry Convergence}\n\\label{sec:geometry}\n\nTable~\\ref{tab:geometry} presents the mechanistic core of our analysis.\nBefore fine-tuning, mining strategies produce markedly different negative difficulties: on Qwen, random negatives have margin 0.074 while embedding negatives have margin 0.017 (ratio 4.35$\\times$).\nAfter fine-tuning, this ratio collapses to 1.29$\\times$ (margins 0.067 vs.\\ 0.052).\nFine-tuning erases 78\\% of the pretrained margin difference on Qwen and 65\\% on StarCoder.\n\n\\begin{table}[t]\n\\centering\n\\caption{Representation geometry pre- vs.\\ post-fine-tuning. Fine-tuning collapses margin differences across strategies.}\n\\label{tab:geometry}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Phase} & \\textbf{Rand.\\ margin} & \\textbf{Emb.\\ margin} & \\textbf{DF margin} & \\textbf{Ratio (R/E)} \\\\\n\\midrule\n\\multirow{2}{*}{Qwen} & Pretrained & 0.074 & 0.017 & 0.029 & 4.35 \\\\\n & Fine-tuned & 0.067 & 0.052 & 0.059 & 1.29 \\\\\n\\midrule\n\\multirow{2}{*}{StarCoder} & Pretrained & 0.194 & 0.067 & 0.119 & 2.90 \\\\\n & Fine-tuned & 0.073 & 0.057 & 0.065 & 1.28 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe contrastive objective drives all strategies toward the same representation geometry regardless of the specific negatives used.\nPretrained geometry---which determines initial negative difficulty---is a transient condition that gets erased during training.\nThis explains why pilot-scale results showed strategy effects (insufficient training to erase geometry) while full-scale results do not (sufficient training to converge).\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Why strategies converge.}\nThe representation geometry analysis (\\S\\ref{sec:geometry}) provides a unified explanation.\nThe contrastive loss optimizes for a target geometry (margins that minimize loss), and LoRA fine-tuning has sufficient capacity to reach this target from any starting point defined by the mining strategy.\nDifferent strategies change the \\emph{path} through representation space but converge to the same \\emph{destination}.\nAt small scale (\\S\\ref{sec:scale}), training is insufficient to complete this convergence, so initial differences persist and strategy choice matters.\nAt full scale, convergence is complete and strategy choice is irrelevant.\n\n\\paragraph{Implications for the BM25-proxy debate.}\nOur finding that BM25 and embedding negatives are indistinguishable (\\S\\ref{sec:bm25}) means that prior work's reported harm cannot be attributed to the BM25-vs-embedding distinction.\nWe observe that CoCoHaNeRe's $-27$pp effect was not reproduced in our setup with either method, suggesting other experimental factors (training scale, encoder architecture, evaluation protocol) are responsible.\nWe frame this as an \\emph{observation} rather than a correction, as we cannot fully disentangle the confounds.\n\n\\paragraph{Training-time vs.\\ inference-time structure.}\nOur null result for dataflow-aware training-time mining contrasts with reported gains from inference-time graph navigation methods (LocAgent: $+8$--$12$pp on SWE-bench; CodexGraph: $+5$pp).\nThe key difference: training-time mining fixes structural signal at corpus construction time, but the relevant structure changes per query.\nInference-time methods adapt structural navigation to the specific query context.\nThis reframes our contribution: structure matters for code retrieval, but the mechanism for incorporating it should be inference-time navigation, not training-time negative curation.\n\n\\paragraph{Practical recommendations.}\n\\begin{enumerate}\n    \\item If your training set exceeds $\\sim$5K instances, random negative sampling is sufficient. Save the GPU time that would be spent on mining.\n    \\item If your training set is small ($<$2K), embedding-distance mining provides a modest benefit ($+1.3$pp) worth the overhead.\n    \\item Do not optimize mining strategy based on a single pool size---rankings are unstable (Kendall $\\tau = 0.33$).\n    \\item For leveraging code structure in retrieval, invest in inference-time graph navigation rather than training-time negative mining.\n    \\item If structural negative mining is attempted, invest in extraction coverage first: at 34\\% coverage, the structural signal is too diluted to surface.\n\\end{enumerate}\n\n\\paragraph{Limitations.}\nOur study uses two 3B-parameter encoders; larger models may exhibit different convergence behavior.\nAll training uses LoRA; full fine-tuning might preserve more strategy-specific signal.\nThe dataflow extraction covers only 34\\% of instances; higher coverage might change the dataflow result, though the stratified analysis (\\S\\ref{sec:stratified}) suggests the effect would remain small.\nSWE-bench Lite's 300 instances provide limited statistical power for downstream evaluation.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe presented a controlled study of hard negative mining strategies for contrastive code retrieval, finding that no strategy---embedding-distance, dataflow-aware, or BM25---reliably outperforms random baselines at full training scale.\nThe representation geometry convergence analysis reveals the mechanism: fine-tuning acts as a geometry equalizer, collapsing pretrained margin differences by 65--78\\% and rendering the initial negative difficulty distribution irrelevant.\nData-scaling ablations show that mining advantages observed at pilot scale vanish monotonically with training set size, consistent with scale substituting for curation.\n\nOur negative results carry actionable implications: practitioners should prioritize training data volume over mining sophistication, use random negatives at scale, and leverage code structure through inference-time navigation rather than training-time negative selection.\nWe hope this work encourages the community to report and value negative results in retrieval research, where publication bias toward positive findings can mislead practitioners into over-investing in techniques that do not survive rigorous evaluation.\n\n%==============================================================================\n\\appendix\n\\section{Temperature Ablation}\n\\label{app:temperature}\n%==============================================================================\n\nTable~\\ref{tab:temp} shows that the null result holds across temperatures $\\tau \\in \\{0.05, 0.10, 0.20\\}$.\nStrategy rankings are unstable across temperatures (embedding leads at $\\tau=0.10$ but trails at $\\tau=0.20$), confirming the absence of a robust strategy effect.\nHigher temperatures degrade all strategies uniformly by $\\sim$2.5pp at $\\tau=0.20$.\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature $\\times$ strategy interaction (R@1, Qwen).}\n\\label{tab:temp}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\tau$ & \\textbf{Random} & \\textbf{Embedding} & $\\Delta$ \\textbf{E$-$R} & $\\Delta$ \\textbf{DF$-$R} \\\\\n\\midrule\n0.05 & 0.529 & 0.531 & +0.20pp & $-$0.45pp \\\\\n0.10 & 0.522 & 0.525 & +0.35pp & $-$0.15pp \\\\\n0.20 & 0.504 & 0.503 & $-$0.10pp & $-$0.25pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Dynamic Mining Ablation}\n\\label{app:dynamic}\n%==============================================================================\n\nRe-mining embedding negatives per epoch (dynamic) vs.\\ once from the pretrained encoder (static) yields negligible improvement (Table~\\ref{tab:dynamic}): $+0.05$pp on both encoders at $3.4\\times$ time overhead.\nThe encoder changes minimally during LoRA fine-tuning (cosine similarity between epoch-0 and epoch-3 embeddings $>0.995$), so dynamic and static negatives are nearly identical.\n\n\\begin{table}[h]\n\\centering\n\\caption{Static vs.\\ dynamic embedding mining.}\n\\label{tab:dynamic}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Static R@1} & \\textbf{Dynamic R@1} & $\\Delta$ \\textbf{(pp)} & \\textbf{Time $\\times$} \\\\\n\\midrule\nQwen & 0.531 & 0.532 & +0.05 & 3.4$\\times$ \\\\\nStarCoder & 0.440 & 0.440 & +0.05 & 3.4$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Hop Count Ablation}\n\\label{app:hop}\n%==============================================================================\n\nExpanding call-graph scope from 1-hop to 3-hop does not rescue the dataflow strategy (Table~\\ref{tab:hop}).\nAll hop counts produce R@1 within noise of random (0.529).\n3-hop slightly worsens performance by over-expanding the connected set, reducing the pool of available structural negatives.\n\n\\begin{table}[h]\n\\centering\n\\caption{Hop count ablation (Qwen, dataflow strategy, 1 seed).}\n\\label{tab:hop}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Hops} & \\textbf{Connected/query} & \\textbf{Neg.\\ available} & \\textbf{R@1} & $\\Delta$ \\textbf{vs Rand} \\\\\n\\midrule\n1 & 2.1 & 47.9 & 0.523 & $-$0.60pp \\\\\n2 & 4.8 & 45.2 & 0.525 & $-$0.45pp \\\\\n3 & 11.3 & 38.7 & 0.521 & $-$0.80pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Fusion Head Ablation}\n\\label{app:fusion}\n%==============================================================================\n\nAdding structural features at inference time via a combined scoring head does not improve over embedding-only retrieval (Table~\\ref{tab:fusion}).\nThe structural-only head performs poorly (R@1 $= 0.312$), and the combined head slightly underperforms embedding-only ($-0.25$pp), suggesting the model learns to partially ignore the noisy structural channel.\n\n\\begin{table}[h]\n\\centering\n\\caption{Fusion head ablation (Qwen, best checkpoint).}\n\\label{tab:fusion}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Head} & \\textbf{R@1} & \\textbf{R@5} & $\\Delta$ \\textbf{vs Emb} \\\\\n\\midrule\nEmbedding only & 0.531 & 0.960 & --- \\\\\nStructural only & 0.312 & 0.620 & $-$21.9pp \\\\\nCombined & 0.529 & 0.955 & $-$0.25pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Distance Weighting Ablation}\n\\label{app:distance}\n%==============================================================================\n\nUsing dataflow-distance-weighted negative selection instead of binary connected/disconnected yields a marginal $+0.10$pp over binary, still underperforming random by $0.35$pp (Table~\\ref{tab:dist_weight}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Distance weighting ablation (Qwen, 1 seed).}\n\\label{tab:dist_weight}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Selection} & \\textbf{R@1} & $\\Delta$ \\textbf{vs Rand} & $\\Delta$ \\textbf{vs Binary} \\\\\n\\midrule\nRandom & 0.529 & --- & --- \\\\\nBinary disconnect & 0.525 & $-$0.45pp & --- \\\\\nDistance weighted & 0.526 & $-$0.35pp & +0.10pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\bibliography{custom}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "020b2fb4-4b7c-4b2d-b6af-4c7f7d92dad8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-contex…",
  "leafUuid": "b67575a9-7ef2-4bd9-8b3a-137b74663c89",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Hard negative mining strategies for code retrieval convergence analysis",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081"
}
```

---

### Assistant

_source line 24 · 2026-05-14T16:57:50.717Z_

Now compile it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b67575a9-7ef2-4bd9-8b3a-137b74663c89",
  "isSidechain": false,
  "requestId": "req_011Cb2pFXWQP5VEHZ8CsdLab",
  "type": "assistant",
  "uuid": "8ed84dfe-cde9-4e26-8b8f-9709e24c01ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dd2YZhyGTEwzPkr621fqwg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10462,
      "cache_read_input_tokens": 42555,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10462,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 42555,
          "cache_creation_input_tokens": 10462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10462
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

_source line 25 · 2026-05-14T16:57:52.086Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012hNC2YjAmAozwzRvdFuaQ4`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "Compile LaTeX paper (two passes)",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ed84dfe-cde9-4e26-8b8f-9709e24c01ff",
  "isSidechain": false,
  "requestId": "req_011Cb2pFXWQP5VEHZ8CsdLab",
  "type": "assistant",
  "uuid": "bbc3584d-5c62-4169-8619-08f857f621ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dd2YZhyGTEwzPkr621fqwg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10462,
      "cache_read_input_tokens": 42555,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10462,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 42555,
          "cache_creation_input_tokens": 10462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10462
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

_source line 26 · 2026-05-14T16:57:52.245Z_

<details><summary>↩ Tool result · reported error · `toolu_012hNC2YjAmAozwzRvdFuaQ4`</summary>

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
  "parentUuid": "bbc3584d-5c62-4169-8619-08f857f621ec",
  "isSidechain": false,
  "promptId": "66bbad76-7453-4fae-883a-01da252df421",
  "type": "user",
  "uuid": "c5523cf8-893b-4491-a521-797c9881897a",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "bbc3584d-5c62-4169-8619-08f857f621ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-14T16:57:55.722Z_

<details><summary>Logged reasoning block</summary>

```text
The ACL style file is not available. Let me switch to a simpler document class that doesn't require external style files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5523cf8-893b-4491-a521-797c9881897a",
  "isSidechain": false,
  "requestId": "req_011Cb2pFqm1druooNFVq1qN8",
  "type": "assistant",
  "uuid": "b953fc04-ba11-4a52-8d68-d7bafcdf4542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7TyEFuZPAjTcfZNghhbvx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 53017,
      "output_tokens": 494,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 494,
          "cache_read_input_tokens": 53017,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 476
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

_source line 28 · 2026-05-14T16:57:56.238Z_

ACL style not available. I'll switch to a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b953fc04-ba11-4a52-8d68-d7bafcdf4542",
  "isSidechain": false,
  "requestId": "req_011Cb2pFqm1druooNFVq1qN8",
  "type": "assistant",
  "uuid": "db228af8-f15b-4c61-9bf6-66f09c342cc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7TyEFuZPAjTcfZNghhbvx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 53017,
      "output_tokens": 494,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 494,
          "cache_read_input_tokens": 53017,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 476
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

_source line 29 · 2026-05-14T16:58:00.490Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01S7EffcZMHNXAq8to55voDG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{adjustbox}\n\n\\aclfinalcopy\n\n\\title{Why Hard Negative Mining Strategies Don't Differentiate\\\\for Code Retrieval at Scale}\n\n\\author{Anonymous}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\n\\title{Why Hard Negative Mining Strategies Don't Differentiate\\\\for Code Retrieval at Scale}\n\n\\author{Anonymous}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db228af8-f15b-4c61-9bf6-66f09c342cc9",
  "isSidechain": false,
  "requestId": "req_011Cb2pFqm1druooNFVq1qN8",
  "type": "assistant",
  "uuid": "de3a067e-e76d-40c2-a3a4-58ce33ac68ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7TyEFuZPAjTcfZNghhbvx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 53017,
      "output_tokens": 494,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 494,
          "cache_read_input_tokens": 53017,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 476
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

_source line 30 · 2026-05-14T16:58:00.513Z_

<details><summary>↩ Tool result · `toolu_01S7EffcZMHNXAq8to55voDG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de3a067e-e76d-40c2-a3a4-58ce33ac68ec",
  "isSidechain": false,
  "promptId": "66bbad76-7453-4fae-883a-01da252df421",
  "type": "user",
  "uuid": "e03a6c73-98f4-43e4-a420-cc76781f426a",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{adjustbox}\n\n\\aclfinalcopy\n\n\\title{Why Hard Negative Mining Strategies Don't Differentiate\\\\for Code Retrieval at Scale}\n\n\\author{Anonymous}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\n\\title{Why Hard Negative Mining Strategies Don't Differentiate\\\\for Code Retrieval at Scale}\n\n\\author{Anonymous}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 18,
        "newStart": 1,
        "newLines": 15,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{acl}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          "-\\usepackage{latexsym}",
          " \\usepackage{graphicx}",
          " \\usepackage{booktabs}",
          " \\usepackage{amsmath}",
          " \\usepackage{amssymb}",
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          "-\\usepackage{tabularx}",
          "-\\usepackage{adjustbox}",
          "+\\usepackage{hyperref}",
          "+\\usepackage{natbib}",
          " ",
          "-\\aclfinalcopy",
          "-",
          " \\title{Why Hard Negative Mining Strategies Don't Differentiate\\\\for Code Retrieval at Scale}",
          " ",
          " \\author{Anonymous}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "de3a067e-e76d-40c2-a3a4-58ce33ac68ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-14T16:58:00.517Z_

```json
{
  "parentUuid": "e03a6c73-98f4-43e4-a420-cc76781f426a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "237a006e-f073-47d7-8ec0-a8a2d7e26858",
  "timestamp": "2026-05-14T16:58:00.517Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-14T16:58:03.808Z_

Also need to fix the bibliography command since there's no .bib file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "237a006e-f073-47d7-8ec0-a8a2d7e26858",
  "isSidechain": false,
  "requestId": "req_011Cb2pGSs8bFVy5XSmVKDgA",
  "type": "assistant",
  "uuid": "3accae12-239b-4426-9af7-7077da07aa02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpukP9suQgTq4uFjG3iFpc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 53493,
      "output_tokens": 574,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 574,
          "cache_read_input_tokens": 53493,
          "cache_creation_input_tokens": 683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 683
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

_source line 33 · 2026-05-14T16:58:11.768Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01AWq7ZcegsQuqfnYM3SQatM`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex",
  "old_string": "\\bibliography{custom}\n\n\\end{document}",
  "new_string": "\\begin{thebibliography}{9}\n\n\\bibitem{jimenez2024swebench}\nCarlos~E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan.\n\\newblock {SWE-bench}: Can language models resolve real-world {GitHub} issues?\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\bibitem{xiong2021approximate}\nLee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, and Arnold Overwijk.\n\\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.\n\\newblock In \\emph{Proc.\\ ICLR}, 2021.\n\n\\bibitem{karpukhin2020dense}\nVladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau Yih.\n\\newblock Dense passage retrieval for open-domain question answering.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2020.\n\n\\bibitem{liu2023repobench}\nTianyang Liu, Canwen Xu, and Julian McAuley.\n\\newblock {RepoBench}: Benchmarking repository-level code auto-completion systems.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3accae12-239b-4426-9af7-7077da07aa02",
  "isSidechain": false,
  "requestId": "req_011Cb2pGSs8bFVy5XSmVKDgA",
  "type": "assistant",
  "uuid": "b3975525-ac6d-4ac8-8618-6b5f3609af99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpukP9suQgTq4uFjG3iFpc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 53493,
      "output_tokens": 574,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 574,
          "cache_read_input_tokens": 53493,
          "cache_creation_input_tokens": 683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 683
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

_source line 34 · 2026-05-14T16:58:11.860Z_

<details><summary>↩ Tool result · `toolu_01AWq7ZcegsQuqfnYM3SQatM`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3975525-ac6d-4ac8-8618-6b5f3609af99",
  "isSidechain": false,
  "promptId": "66bbad76-7453-4fae-883a-01da252df421",
  "type": "user",
  "uuid": "f0db1d49-11f3-4a0f-853f-4de9520faa86",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex",
    "oldString": "\\bibliography{custom}\n\n\\end{document}",
    "newString": "\\begin{thebibliography}{9}\n\n\\bibitem{jimenez2024swebench}\nCarlos~E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan.\n\\newblock {SWE-bench}: Can language models resolve real-world {GitHub} issues?\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\bibitem{xiong2021approximate}\nLee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, and Arnold Overwijk.\n\\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.\n\\newblock In \\emph{Proc.\\ ICLR}, 2021.\n\n\\bibitem{karpukhin2020dense}\nVladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau Yih.\n\\newblock Dense passage retrieval for open-domain question answering.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2020.\n\n\\bibitem{liu2023repobench}\nTianyang Liu, Canwen Xu, and Julian McAuley.\n\\newblock {RepoBench}: Benchmarking repository-level code auto-completion systems.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 568,
        "oldLines": 6,
        "newStart": 568,
        "newLines": 28,
        "lines": [
          " \\end{tabular}",
          " \\end{table}",
          " ",
          "-\\bibliography{custom}",
          "+\\begin{thebibliography}{9}",
          " ",
          "+\\bibitem{jimenez2024swebench}",
          "+Carlos~E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan.",
          "+\\newblock {SWE-bench}: Can language models resolve real-world {GitHub} issues?",
          "+\\newblock In \\emph{Proc.\\ ICLR}, 2024.",
          "+",
          "+\\bibitem{xiong2021approximate}",
          "+Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, and Arnold Overwijk.",
          "+\\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.",
          "+\\newblock In \\emph{Proc.\\ ICLR}, 2021.",
          "+",
          "+\\bibitem{karpukhin2020dense}",
          "+Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau Yih.",
          "+\\newblock Dense passage retrieval for open-domain question answering.",
          "+\\newblock In \\emph{Proc.\\ EMNLP}, 2020.",
          "+",
          "+\\bibitem{liu2023repobench}",
          "+Tianyang Liu, Canwen Xu, and Julian McAuley.",
          "+\\newblock {RepoBench}: Benchmarking repository-level code auto-completion systems.",
          "+\\newblock In \\emph{Proc.\\ ICLR}, 2024.",
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
  "sourceToolAssistantUUID": "b3975525-ac6d-4ac8-8618-6b5f3609af99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T16:58:15.255Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XD8Vc5A6dTwfdD7Qcr3EPK`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper (two passes)",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0db1d49-11f3-4a0f-853f-4de9520faa86",
  "isSidechain": false,
  "requestId": "req_011Cb2pHHRPQQkmE8S9VDBNE",
  "type": "assistant",
  "uuid": "5a8b2609-1dd7-46fb-aaad-70b89e75c7c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGwjEzq14SwyZKR5ceWj4G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 54176,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 659,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 54176,
          "cache_creation_input_tokens": 659,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 659
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

_source line 36 · 2026-05-14T16:58:15.759Z_

<details><summary>↩ Tool result · reported error · `toolu_01XD8Vc5A6dTwfdD7Qcr3EPK`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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

Package natbib Warning: Citation `jimenez2024swebench' on page 1 undefined on i
nput line 39.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `xiong2021approximate' on page 2 undefined on 
input line 69.


Package natbib Warning: Citation `karpukhin2020dense' on page 2 undefined on in
put line 69.


Package natbib Warning: Citation `liu2023repobench' on page 2 undefined on inpu
t line 76.

[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)

LaTeX Warning: Reference `tab:main' on page 3 undefined on input line 133.


LaTeX Warning: Reference `tab:bm25' on page 3 undefined on input line 167.

[3]

LaTeX Warning: Reference `tab:swebench' on page 4 undefined on input line 192.


Overfull \hbox (7.01205pt too wide) in paragraph at lines 216--219
[]\OT1/ptm/m/n/10.95 With 300 bi-nary out-comes at a base rate of $\OMS/cmsy/m/
n/10.95 ^^X$\OT1/ptm/m/n/10.95 25%, the bi-no-mial stan-dard er-ror is $[] \OMS
/cmsy/m/n/10.95 ^^Y

LaTeX Warning: Reference `tab:repobench' on page 4 undefined on input line 223.



LaTeX Warning: Reference `tab:stratified' on page 4 undefined on input line 248
.


LaTeX Warning: Reference `tab:pool' on page 4 undefined on input line 278.

[4]

LaTeX Warning: Reference `tab:scale' on page 5 undefined on input line 319.


LaTeX Warning: Reference `tab:failure' on page 5 undefined on input line 347.


LaTeX Warning: Reference `tab:geometry' on page 5 undefined on input line 373.

[5]

LaTeX Warning: Reference `sec:geometry' on page 6 undefined on input line 406.


LaTeX Warning: Reference `sec:scale' on page 6 undefined on input line 409.


LaTeX Warning: Reference `sec:bm25' on page 6 undefined on input line 413.

[6]
Overfull \hbox (1.82867pt too wide) in paragraph at lines 426--427
[]\OT1/ptm/m/n/10.95 If your train-ing set is small ($\OML/cmm/m/it/10.95 <$\OT
1/ptm/m/n/10.95 2K), embedding-distance min-ing pro-vides a mod-est ben-e-fit (
$\OT1/cmr/m/n/10.95 +1\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 3$\OT1/ptm/m/n/10
.95 pp)

LaTeX Warning: Reference `sec:stratified' on page 7 undefined on input line 435
.


LaTeX Warning: Reference `tab:temp' on page 7 undefined on input line 456.

[7]

LaTeX Warning: Reference `tab:dynamic' on page 8 undefined on input line 481.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:hop' on page 8 undefined on input line 504.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:fusion' on page 8 undefined on input line 529.


Overfull \hbox (11.21982pt too wide) in paragraph at lines 529--531
\OT1/ptm/m/n/10.95 Adding struc-tural fea-tures at in-fer-ence time via a com-b
ined scor-ing head does not im-prove over embedding-
[8]

LaTeX Warning: Reference `tab:dist_weight' on page 9 undefined on input line 55
3.


LaTeX Warning: `h' float specifier changed to `ht'.


Package natbib Warning: There were undefined citations.

[9] [10] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.


! Package natbib Error: Bibliography not compatible with author-year citations.

(natbib)                Press &lt;return> to continue in numerical citation style.


See the natbib package documentation for explanation.
Type  H &lt;return>  for immediate help.
 ...                                              
                                                  
l.89 ...mand\NAT@force@numbers{}\NAT@force@numbers
                                                  
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
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 149529 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a8b2609-1dd7-46fb-aaad-70b89e75c7c5",
  "isSidechain": false,
  "promptId": "66bbad76-7453-4fae-883a-01da252df421",
  "type": "user",
  "uuid": "9fc24628-9bc8-43b9-bab9-08571bae5f01",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `jimenez2024swebench' on page 1 undefined on i\nnput line 39.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `xiong2021approximate' on page 2 undefined on \ninput line 69.\n\n\nPackage natbib Warning: Citation `karpukhin2020dense' on page 2 undefined on in\nput line 69.\n\n\nPackage natbib Warning: Citation `liu2023repobench' on page 2 undefined on inpu\nt line 76.\n\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n\nLaTeX Warning: Reference `tab:main' on page 3 undefined on input line 133.\n\n\nLaTeX Warning: Reference `tab:bm25' on page 3 undefined on input line 167.\n\n[3]\n\nLaTeX Warning: Reference `tab:swebench' on page 4 undefined on input line 192.\n\n\nOverfull \\hbox (7.01205pt too wide) in paragraph at lines 216--219\n[]\\OT1/ptm/m/n/10.95 With 300 bi-nary out-comes at a base rate of $\\OMS/cmsy/m/\nn/10.95 ^^X$\\OT1/ptm/m/n/10.95 25%, the bi-no-mial stan-dard er-ror is $[] \\OMS\n/cmsy/m/n/10.95 ^^Y\n\nLaTeX Warning: Reference `tab:repobench' on page 4 undefined on input line 223.\n\n\n\nLaTeX Warning: Reference `tab:stratified' on page 4 undefined on input line 248\n.\n\n\nLaTeX Warning: Reference `tab:pool' on page 4 undefined on input line 278.\n\n[4]\n\nLaTeX Warning: Reference `tab:scale' on page 5 undefined on input line 319.\n\n\nLaTeX Warning: Reference `tab:failure' on page 5 undefined on input line 347.\n\n\nLaTeX Warning: Reference `tab:geometry' on page 5 undefined on input line 373.\n\n[5]\n\nLaTeX Warning: Reference `sec:geometry' on page 6 undefined on input line 406.\n\n\nLaTeX Warning: Reference `sec:scale' on page 6 undefined on input line 409.\n\n\nLaTeX Warning: Reference `sec:bm25' on page 6 undefined on input line 413.\n\n[6]\nOverfull \\hbox (1.82867pt too wide) in paragraph at lines 426--427\n[]\\OT1/ptm/m/n/10.95 If your train-ing set is small ($\\OML/cmm/m/it/10.95 <$\\OT\n1/ptm/m/n/10.95 2K), embedding-distance min-ing pro-vides a mod-est ben-e-fit (\n$\\OT1/cmr/m/n/10.95 +1\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 3$\\OT1/ptm/m/n/10\n.95 pp)\n\nLaTeX Warning: Reference `sec:stratified' on page 7 undefined on input line 435\n.\n\n\nLaTeX Warning: Reference `tab:temp' on page 7 undefined on input line 456.\n\n[7]\n\nLaTeX Warning: Reference `tab:dynamic' on page 8 undefined on input line 481.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:hop' on page 8 undefined on input line 504.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:fusion' on page 8 undefined on input line 529.\n\n\nOverfull \\hbox (11.21982pt too wide) in paragraph at lines 529--531\n\\OT1/ptm/m/n/10.95 Adding struc-tural fea-tures at in-fer-ence time via a com-b\nined scor-ing head does not im-prove over embedding-\n[8]\n\nLaTeX Warning: Reference `tab:dist_weight' on page 9 undefined on input line 55\n3.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nPackage natbib Warning: There were undefined citations.\n\n[9] [10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n\n! Package natbib Error: Bibliography not compatible with author-year citations.\n\n(natbib)                Press &lt;return> to continue in numerical citation style.\n\n\nSee the natbib package documentation for explanation.\nType  H &lt;return>  for immediate help.\n ...                                              \n                                                  \nl.89 ...mand\\NAT@force@numbers{}\\NAT@force@numbers\n                                                  \n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 149529 bytes).\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "5a8b2609-1dd7-46fb-aaad-70b89e75c7c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-contex…",
  "leafUuid": "9fc24628-9bc8-43b9-bab9-08571bae5f01",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Hard negative mining strategies for code retrieval convergence analysis",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081"
}
```

---

### Assistant

_source line 39 · 2026-05-14T16:58:20.599Z_

The first pass produced a PDF (10 pages). The error is from natbib incompatibility with the thebibliography environment. Let me fix by removing natbib and running again.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fc24628-9bc8-43b9-bab9-08571bae5f01",
  "isSidechain": false,
  "requestId": "req_011Cb2pHaBhAsFLR4iYjE25b",
  "type": "assistant",
  "uuid": "1740c9a7-1b48-485e-92c9-7ecd82b53ad4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sKYbnLzATwXVNiwDDwdXZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3804,
      "cache_read_input_tokens": 54835,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 222,
          "cache_read_input_tokens": 54835,
          "cache_creation_input_tokens": 3804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3804
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

_source line 40 · 2026-05-14T16:58:21.348Z_

<details open><summary>🔧 Tool call — Edit · `toolu_017yTgZkMDFd7hwoa8fofvJZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex",
  "old_string": "\\usepackage{hyperref}\n\\usepackage{natbib}",
  "new_string": "\\usepackage{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1740c9a7-1b48-485e-92c9-7ecd82b53ad4",
  "isSidechain": false,
  "requestId": "req_011Cb2pHaBhAsFLR4iYjE25b",
  "type": "assistant",
  "uuid": "57d5074e-b86b-434d-ae36-bc7ff0905237",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sKYbnLzATwXVNiwDDwdXZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3804,
      "cache_read_input_tokens": 54835,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 222,
          "cache_read_input_tokens": 54835,
          "cache_creation_input_tokens": 3804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3804
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

_source line 41 · 2026-05-14T16:58:21.360Z_

<details><summary>↩ Tool result · `toolu_017yTgZkMDFd7hwoa8fofvJZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57d5074e-b86b-434d-ae36-bc7ff0905237",
  "isSidechain": false,
  "promptId": "66bbad76-7453-4fae-883a-01da252df421",
  "type": "user",
  "uuid": "03a36895-2748-440e-8a34-ef7c95230163",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex",
    "oldString": "\\usepackage{hyperref}\n\\usepackage{natbib}",
    "newString": "\\usepackage{hyperref}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 6,
        "lines": [
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          " \\usepackage{hyperref}",
          "-\\usepackage{natbib}",
          " ",
          " \\title{Why Hard Negative Mining Strategies Don't Differentiate\\\\for Code Retrieval at Scale}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "57d5074e-b86b-434d-ae36-bc7ff0905237",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T16:58:24.983Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FYhQHYUExDAbqrabAhyk2S`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst && rm -f paper.aux paper.log paper.out && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -15",
  "description": "Recompile LaTeX paper without natbib",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03a36895-2748-440e-8a34-ef7c95230163",
  "isSidechain": false,
  "requestId": "req_011Cb2pHzC5Bqac9yVkN149H",
  "type": "assistant",
  "uuid": "719cdb5a-3b99-42cb-ba2c-3da124e5d1b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTvpxrsgvhCuUDch5M6XG7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 288,
      "cache_read_input_tokens": 58639,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 58639,
          "cache_creation_input_tokens": 288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 288
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

_source line 43 · 2026-05-14T16:58:26.111Z_

<details><summary>↩ Tool result · `toolu_01FYhQHYUExDAbqrabAhyk2S`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

LaTeX Warning: Citation `jimenez2024swebench' on page 1 undefined on input line
 38.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

LaTeX Warning: Citation `xiong2021approximate' on page 2 undefined on input lin
e 68.


LaTeX Warning: Citation `karpukhin2020dense' on page 2 undefined on input line 
68.


LaTeX Warning: Citation `liu2023repobench' on page 2 undefined on input line 75
.

[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)

LaTeX Warning: Reference `tab:main' on page 3 undefined on input line 132.


LaTeX Warning: Reference `tab:bm25' on page 3 undefined on input line 166.

[3]

LaTeX Warning: Reference `tab:swebench' on page 4 undefined on input line 191.


Overfull \hbox (7.01205pt too wide) in paragraph at lines 215--218
[]\OT1/ptm/m/n/10.95 With 300 bi-nary out-comes at a base rate of $\OMS/cmsy/m/
n/10.95 ^^X$\OT1/ptm/m/n/10.95 25%, the bi-no-mial stan-dard er-ror is $[] \OMS
/cmsy/m/n/10.95 ^^Y

LaTeX Warning: Reference `tab:repobench' on page 4 undefined on input line 222.



LaTeX Warning: Reference `tab:stratified' on page 4 undefined on input line 247
.


LaTeX Warning: Reference `tab:pool' on page 4 undefined on input line 277.

[4]

LaTeX Warning: Reference `tab:scale' on page 5 undefined on input line 318.


LaTeX Warning: Reference `tab:failure' on page 5 undefined on input line 346.


LaTeX Warning: Reference `tab:geometry' on page 5 undefined on input line 372.

[5]

LaTeX Warning: Reference `sec:geometry' on page 6 undefined on input line 405.


LaTeX Warning: Reference `sec:scale' on page 6 undefined on input line 408.


LaTeX Warning: Reference `sec:bm25' on page 6 undefined on input line 412.

[6]
Overfull \hbox (1.82867pt too wide) in paragraph at lines 425--426
[]\OT1/ptm/m/n/10.95 If your train-ing set is small ($\OML/cmm/m/it/10.95 <$\OT
1/ptm/m/n/10.95 2K), embedding-distance min-ing pro-vides a mod-est ben-e-fit (
$\OT1/cmr/m/n/10.95 +1\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 3$\OT1/ptm/m/n/10
.95 pp)

LaTeX Warning: Reference `sec:stratified' on page 7 undefined on input line 434
.


LaTeX Warning: Reference `tab:temp' on page 7 undefined on input line 455.

[7]

LaTeX Warning: Reference `tab:dynamic' on page 8 undefined on input line 480.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:hop' on page 8 undefined on input line 503.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:fusion' on page 8 undefined on input line 528.


Overfull \hbox (11.21982pt too wide) in paragraph at lines 528--530
\OT1/ptm/m/n/10.95 Adding struc-tural fea-tures at in-fer-ence time via a com-b
ined scor-ing head does not im-prove over embedding-
[8]

LaTeX Warning: Reference `tab:dist_weight' on page 9 undefined on input line 55
2.


LaTeX Warning: `h' float specifier changed to `ht'.

[9] [10] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 149547 bytes).
Transcript written on paper.log.
LaTeX Warning: `h' float specifier changed to `ht'.

[9] [10] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 152089 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "719cdb5a-3b99-42cb-ba2c-3da124e5d1b5",
  "isSidechain": false,
  "promptId": "66bbad76-7453-4fae-883a-01da252df421",
  "type": "user",
  "uuid": "90c36ed8-141d-433f-b6d3-3da2866ec303",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nLaTeX Warning: Citation `jimenez2024swebench' on page 1 undefined on input line\n 38.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nLaTeX Warning: Citation `xiong2021approximate' on page 2 undefined on input lin\ne 68.\n\n\nLaTeX Warning: Citation `karpukhin2020dense' on page 2 undefined on input line \n68.\n\n\nLaTeX Warning: Citation `liu2023repobench' on page 2 undefined on input line 75\n.\n\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n\nLaTeX Warning: Reference `tab:main' on page 3 undefined on input line 132.\n\n\nLaTeX Warning: Reference `tab:bm25' on page 3 undefined on input line 166.\n\n[3]\n\nLaTeX Warning: Reference `tab:swebench' on page 4 undefined on input line 191.\n\n\nOverfull \\hbox (7.01205pt too wide) in paragraph at lines 215--218\n[]\\OT1/ptm/m/n/10.95 With 300 bi-nary out-comes at a base rate of $\\OMS/cmsy/m/\nn/10.95 ^^X$\\OT1/ptm/m/n/10.95 25%, the bi-no-mial stan-dard er-ror is $[] \\OMS\n/cmsy/m/n/10.95 ^^Y\n\nLaTeX Warning: Reference `tab:repobench' on page 4 undefined on input line 222.\n\n\n\nLaTeX Warning: Reference `tab:stratified' on page 4 undefined on input line 247\n.\n\n\nLaTeX Warning: Reference `tab:pool' on page 4 undefined on input line 277.\n\n[4]\n\nLaTeX Warning: Reference `tab:scale' on page 5 undefined on input line 318.\n\n\nLaTeX Warning: Reference `tab:failure' on page 5 undefined on input line 346.\n\n\nLaTeX Warning: Reference `tab:geometry' on page 5 undefined on input line 372.\n\n[5]\n\nLaTeX Warning: Reference `sec:geometry' on page 6 undefined on input line 405.\n\n\nLaTeX Warning: Reference `sec:scale' on page 6 undefined on input line 408.\n\n\nLaTeX Warning: Reference `sec:bm25' on page 6 undefined on input line 412.\n\n[6]\nOverfull \\hbox (1.82867pt too wide) in paragraph at lines 425--426\n[]\\OT1/ptm/m/n/10.95 If your train-ing set is small ($\\OML/cmm/m/it/10.95 <$\\OT\n1/ptm/m/n/10.95 2K), embedding-distance min-ing pro-vides a mod-est ben-e-fit (\n$\\OT1/cmr/m/n/10.95 +1\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 3$\\OT1/ptm/m/n/10\n.95 pp)\n\nLaTeX Warning: Reference `sec:stratified' on page 7 undefined on input line 434\n.\n\n\nLaTeX Warning: Reference `tab:temp' on page 7 undefined on input line 455.\n\n[7]\n\nLaTeX Warning: Reference `tab:dynamic' on page 8 undefined on input line 480.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:hop' on page 8 undefined on input line 503.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:fusion' on page 8 undefined on input line 528.\n\n\nOverfull \\hbox (11.21982pt too wide) in paragraph at lines 528--530\n\\OT1/ptm/m/n/10.95 Adding struc-tural fea-tures at in-fer-ence time via a com-b\nined scor-ing head does not im-prove over embedding-\n[8]\n\nLaTeX Warning: Reference `tab:dist_weight' on page 9 undefined on input line 55\n2.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9] [10] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 149547 bytes).\nTranscript written on paper.log.\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9] [10] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 152089 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "719cdb5a-3b99-42cb-ba2c-3da124e5d1b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-14T16:58:36.907Z_

编译成功，10 页 PDF。

输出：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex` → `paper.pdf` (10 pages, 152KB)。

论文结构：
- **Abstract + Introduction**: 负结果框架——mining 策略在全量训练规模下不可区分
- **Method**: 4 种策略（random/embedding/dataflow/BM25）× 2 编码器 × 9 seed
- **Experiments**: 覆盖 JSON 中全部 15 个实验，对应 Tables 2–10 + Appendix Tables A1–A5
- **核心发现**: 几何收敛机制（margin 差异被 fine-tuning 抹平 65–78%）+ 规模替代策略（1K→5K 效果单调衰减）
- **Discussion**: BM25-proxy 无法归因、训练时 vs 推理时结构利用、实践建议
- **Appendix**: 温度消融、动态挖掘、hop 数、融合头、距离加权

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90c36ed8-141d-433f-b6d3-3da2866ec303",
  "isSidechain": false,
  "requestId": "req_011Cb2pJLJo8P8fZAjSyiA1h",
  "type": "assistant",
  "uuid": "14f591a6-7acd-4f0b-b472-71eb699311eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XrkTous4DUshszX9AyztDd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4051,
      "cache_read_input_tokens": 58927,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4051,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 325,
          "cache_read_input_tokens": 58927,
          "cache_creation_input_tokens": 4051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4051
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-contex…",
  "leafUuid": "14f591a6-7acd-4f0b-b472-71eb699311eb",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Hard negative mining strategies for code retrieval convergence analysis",
  "sessionId": "7c35f0a2-0423-4048-b741-51ef52323081"
}
```

---
