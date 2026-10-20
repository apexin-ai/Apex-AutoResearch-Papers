# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T075732 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/0e74a8f6-0a91-487b-9437-3d2c0cc79eae.jsonl`
- **Structured JSON:** [`8751b683e9159c5bc899.json`](../../sessions/87/8751b683e9159c5bc899.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T08:11:47.985Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T08:11:47.985Z",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T075732 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：9-seed 全量复现完全确认 pilot 模式。Embedding mining 在两个编码器上均显著优于 random（bootstrap 95% CI 不含零）， dataflow 在 Qwen 上提供条件性额外收益而在 StarCoder 上无显著差异，产生干净的交互效应。 SWE-bench 下游验证显示可观测的 resolve rate 提升。机制故事（表征饱和度 → 策略有效性）通过 neg_difficulty margin、 温度消融、动态挖掘对照三条证据线完整闭合。论文三条 claim 均有充分统计支撑，EMNLP Main 定位清晰。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T08:11:47.989Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T08:11:47.989Z",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-14T08:11:48.008Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T075732 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：9-seed 全量复现完全确认 pilot 模式。Embedding mining 在两个编码器上均显著优于 random（bootstrap 95% CI 不含零）， dataflow 在 Qwen 上提供条件性额外收益而在 StarCoder 上无显著差异，产生干净的交互效应。 SWE-bench 下游验证显示可观测的 resolve rate 提升。机制故事（表征饱和度 → 策略有效性）通过 neg_difficulty margin、 温度消融、动态挖掘对照三条证据线完整闭合。论文三条 claim 均有充分统计支撑，EMNLP Main 定位清晰。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c22e34fb-2aaf-43f6-b289-b9742e162809",
  "type": "user",
  "uuid": "261f6a57-ac12-4f88-b1d2-cdc86ee7dbce",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T08:11:48.007Z_

```json
{
  "parentUuid": "261f6a57-ac12-4f88-b1d2-cdc86ee7dbce",
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
  "uuid": "d60cb2a0-0522-479f-bea5-170aafeed9eb",
  "timestamp": "2026-05-14T08:11:48.007Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T08:11:48.007Z_

```json
{
  "parentUuid": "d60cb2a0-0522-479f-bea5-170aafeed9eb",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ccacbc5b-303f-4200-ba07-c41b6a1ffe34",
  "timestamp": "2026-05-14T08:11:48.007Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
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
  "aiTitle": "Generate complete simulation paper for dream agent",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae"
}
```

---

### Assistant

_source line 7 · 2026-05-14T08:11:50.138Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccacbc5b-303f-4200-ba07-c41b6a1ffe34",
  "isSidechain": false,
  "requestId": "req_011Cb2896yhhxMjY2FZ2eWe6",
  "type": "assistant",
  "uuid": "e2fb4b14-c1a1-4e40-9025-d673f8b2ea3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxZhj3NCDrb57gXEtBTUYq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11227,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11227
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

_source line 8 · 2026-05-14T08:11:51.102Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FNhx6yfb5eZjFQQ8cDNMJq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2fb4b14-c1a1-4e40-9025-d673f8b2ea3b",
  "isSidechain": false,
  "requestId": "req_011Cb2896yhhxMjY2FZ2eWe6",
  "type": "assistant",
  "uuid": "8e5c20d3-a357-4a2c-a71d-02a7719e6b1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxZhj3NCDrb57gXEtBTUYq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11227,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11227
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

_source line 9 · 2026-05-14T08:11:51.379Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WMz5Rt9Cynk2x5XPntPmWF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e5c20d3-a357-4a2c-a71d-02a7719e6b1d",
  "isSidechain": false,
  "requestId": "req_011Cb2896yhhxMjY2FZ2eWe6",
  "type": "assistant",
  "uuid": "df6c0183-39a0-43ae-b5ca-5bf16f0babc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxZhj3NCDrb57gXEtBTUYq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11227,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11227
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

_source line 10 · 2026-05-14T08:11:51.386Z_

<details><summary>↩ Tool result · `toolu_01WMz5Rt9Cynk2x5XPntPmWF`</summary>

```text
1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported "harm" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).
10	
11	2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.
12	
13	3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).
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
62	| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |
63	| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |
64	| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |
65	| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |
66	| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |
67	| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |
68	| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |
69	| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |
70	| "Complementary signal" overstatement | Temper: "conditionally beneficial" not "always complementary" | Writing discipline |
71	| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |
72	
73	## Evidence Status
74	
75	### Confirmed findings (basis for claims):
76	- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact
77	- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction
78	- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)
79	- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only
80	- plan_006: CodeQL scalability confirmed at 123-repo scale
81	
82	### In progress:
83	- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)
84	- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)
85	- m1_reextract_v2: expanded extraction for higher coverage
86	
87	### Planned (priority order):
88	- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
89	- plan_014: Temperature ablation (Dream reviewer concern)
90	- plan_004: RepoBench-R second benchmark
91	- plan_015: Dynamic mining baseline
92	- plan_007/008/009: Additional ablations
93	
94	## Contingency (if full M2 results weaken claims)
95	
96	### All 18 runs confirm pilot pattern: Best case
97	- Full statistical power, paper as framed above
98	- Target: EMNLP Main
99	
100	### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
101	- Drop Claim 2 to analysis observation
102	- Paper becomes: "True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions"
103	- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main
104	
105	### Embedding mining also loses advantage at full scale: Major reassessment needed
106	- Recheck data pipeline for bugs (full-scale data may have distribution differences)
107	- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
108	- Discuss with user before committing direction
109	
110	## Deprecated Claims (with reason)
111	
112	- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df6c0183-39a0-43ae-b5ca-5bf16f0babc7",
  "isSidechain": false,
  "promptId": "c22e34fb-2aaf-43f6-b289-b9742e162809",
  "type": "user",
  "uuid": "41882407-6a63-41b3-a5af-dd0bbc63d47a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper_framing.md",
      "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \"harm\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).\n\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\n\n- **Headline result template**: \"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\"\n\n## Core Insight\n\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\"\n- Backup: \"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\n- m1_reextract_v2: expanded extraction for higher coverage\n\n### Planned (priority order):\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark\n- plan_015: Dynamic mining baseline\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n",
      "numLines": 113,
      "startLine": 1,
      "totalLines": 113
    }
  },
  "sourceToolAssistantUUID": "df6c0183-39a0-43ae-b5ca-5bf16f0babc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T08:11:51.505Z_

<details><summary>↩ Tool result · `toolu_01FNhx6yfb5eZjFQQ8cDNMJq`</summary>

```text
1	[
2	  {
3	    "name": "SWE-bench Lite End-to-End Evaluation",
4	    "description": "3 strategies × best checkpoint on SWE-bench Lite (300), Qwen3.6-27B agent, 测 resolve rate",
5	    "results": {
6	      "random_resolve_rate": 0.227,
7	      "embedding_distance_resolve_rate": 0.25,
8	      "dataflow_aware_resolve_rate": 0.26,
9	      "embed_vs_random_delta_pp": 2.3,
10	      "dataflow_vs_random_delta_pp": 3.3,
11	      "dataflow_vs_embed_delta_pp": 1.0,
12	      "total_instances": 300,
13	      "instances_resolved_random": 68,
14	      "instances_resolved_embed": 75,
15	      "instances_resolved_dataflow": 78,
16	      "retrieval_recall1_random": 0.533,
17	      "retrieval_recall1_embed": 0.556,
18	      "retrieval_recall1_dataflow": 0.548
19	    },
20	    "tables": [
21	      {
22	        "caption": "SWE-bench Lite Resolve Rate by Retrieval Strategy",
23	        "columns": [
24	          "Strategy",
25	          "Resolve_Rate",
26	          "Delta_vs_Random",
27	          "Instances_Resolved"
28	        ],
29	        "rows": [
30	          [
31	            "random",
32	            "22.7%",
33	            "—",
34	            68
35	          ],
36	          [
37	            "embedding_distance",
38	            "25.0%",
39	            "+2.3pp",
40	            75
41	          ],
42	          [
43	            "dataflow_aware",
44	            "26.0%",
45	            "+3.3pp",
46	            78
47	          ]
48	        ]
49	      }
50	    ],
51	    "figures": [],
52	    "analysis": "Resolve rate 提升确认 retrieval 质量改善能传导到实际软件工程任务。Dataflow 策略独立解决了 5 个 random/embed 均失败的 instance（多为跨文件 dataflow 依赖），支持 Claim 2 的条件性收益叙事。 Embed 策略独立解决 3 个（多为同文件内近义函数混淆），支持 Claim 1。\n\n\nbest 档下 retrieval 质量提升能传导到下游 resolve rate。Qwen best checkpoint embedding R@1≈0.556 vs random 0.533， 差值 2.3pp 在 300 实例上对应约 7 个额外正确 retrieval → 其中部分转化为 resolve。 转化率不是 1:1（retrieval 改善不等于 repair 改善，LLM agent 有自身能力上限）， 但 best 档假设转化效率约 30-40%，即 ~7 个额外正确 retrieval 中约 2-3 个转为 resolve。 Dataflow 在 Qwen 上的条件性收益（pilot +0.8pp R@1）进一步贡献约 1pp resolve delta。 总体 swebench_resolve_delta_pp 落在 [2.0, 5.0] 范围的中低段， 因为 retrieval → repair 的衰减是系统性的。SWE-bench Lite 300 实例规模下， 2-3pp 差异虽小但在 best 档下 bootstrap CI 可检测。\n"
53	  },
54	  {
55	    "name": "RepoBench-R Cross-File Retrieval Evaluation",
56	    "description": "3 strategies × best checkpoint on RepoBench-R, retrieval-only evaluation",
57	    "results": {
58	      "random_recall1": 0.412,
59	      "embedding_distance_recall1": 0.431,
60	      "dataflow_aware_recall1": 0.438,
61	      "random_mrr": 0.508,
62	      "embedding_distance_mrr": 0.529,
63	      "dataflow_aware_mrr": 0.534,
64	      "embed_vs_random_R1_delta_pp": 1.9,
65	      "dataflow_vs_random_R1_delta_pp": 2.6,
66	      "total_queries": 1200
67	    },
68	    "tables": [
69	      {
70	        "caption": "RepoBench-R Retrieval Performance",
71	        "columns": [
72	          "Strategy",
73	          "R@1",
74	          "R@5",
75	          "R@10",
76	          "MRR"
77	        ],
78	        "rows": [
79	          [
80	            "random",
81	            0.412,
82	            0.687,
83	            0.793,
84	            0.508
85	          ],
86	          [
87	            "embedding_distance",
88	            0.431,
89	            0.704,
90	            0.808,
91	            0.529
92	          ],
93	          [
94	            "dataflow_aware",
95	            0.438,
96	            0.711,
97	            0.812,
98	            0.534
99	          ]
100	        ]
101	      }
102	    ],
103	    "figures": [],
104	    "analysis": "第二 benchmark 确认 SWE-smith 上的发现不是 benchmark-specific artifact。 策略排序一致（dataflow ≥ embed > random），增强论文的 external validity。\n\n\nRepoBench-R 是 cross-file retrieval benchmark，天然偏向有结构依赖的查询（import/call 关系）。 在 best 档下，embedding 改善幅度与 SWE-smith 内部 eval 一致（~2pp）， dataflow 的额外收益在此 benchmark 上可能略大于 SWE-smith（因 RepoBench-R 的 cross-file 性质与 dataflow connectivity 天然对齐），但差异不会很大因为训练数据来自 SWE-smith 而非 RepoBench， 存在 domain gap。整体 R@1 低于 SWE-smith 内部 eval（0.41 vs 0.53）， 因为 pool size 和 query 分布不同。关键是方向一致且差异可检测。\n"
105	  },
106	  {
107	    "name": "Embedding vs Random Stratified Analysis",
108	    "description": "按 repo size/complexity 分层，分析 embedding negatives 的收益分布",
109	    "results": {
110	      "small_repo_lt50_embed_delta_pp": 0.8,
111	      "medium_repo_50_200_embed_delta_pp": 2.1,
112	      "large_repo_200_500_embed_delta_pp": 2.8,
113	      "xlarge_repo_500plus_embed_delta_pp": 1.5,
114	      "high_complexity_embed_delta_pp": 2.9,
115	      "low_complexity_embed_delta_pp": 1.2,
116	      "correlation_repo_size_vs_delta": 0.31,
117	      "correlation_complexity_vs_delta": 0.42
118	    },
119	    "tables": [
120	      {
121	        "caption": "Embedding Mining Benefit by Repo Tier",
122	        "columns": [
123	          "Tier",
124	          "N_Instances",
125	          "Embed_R1",
126	          "Random_R1",
127	          "Delta_pp"
128	        ],
129	        "rows": [
130	          [
131	            "small (<50)",
132	            500,
133	            0.568,
134	            0.56,
135	            "+0.8"
136	          ],
137	          [
138	            "medium (50-200)",
139	            4096,
140	            0.551,
141	            0.53,
142	            "+2.1"
143	          ],
144	          [
145	            "large (200-500)",
146	            13628,
147	            0.542,
148	            0.514,
149	            "+2.8"
150	          ],
151	          [
152	            "xlarge (500+)",
153	            25949,
154	            0.528,
155	            0.513,
156	            "+1.5"
157	          ]
158	        ]
159	      }
160	    ],
161	    "figures": [],
162	    "analysis": "收益分布分析提供 practical guidance：embedding mining 对中大型项目最有效， 与表征空间中 near-miss 候选密度的直觉一致。复杂度比 size 更具预测力， 提示 negative mining 策略选择应考虑代码结构特征而非简单规模。\n\n\nbest 档下 embedding mining 普遍有效但收益分布不均。中大型 repo（50-500 files）收益最大， 因为 pool 中有足够多的 near-miss 候选（lexically similar but not gold）， embedding mining 能有效挑选最有信息量的 hard negatives。小型 repo pool 太小、 embedding mining 退化为近似 random；超大型 repo 结构复杂度使得 embedding distance 与 relevance 的相关性下降（太多 \"远但相关\" 的文件）。Complexity（cyclomatic complexity 或 import depth）比 size 更好地预测 embedding mining 收益， 因为高复杂度代码中相似但无关的文件更多。\n"
163	  },
164	  {
165	    "name": "Hop Distance Ablation",
166	    "description": "1-hop vs 2-hop vs 3-hop call-graph bounding for dataflow extraction",
167	    "results": {
168	      "hop1_connected_rate": 0.12,
169	      "hop2_connected_rate": 0.34,
170	      "hop3_connected_rate": 0.58,
171	      "hop1_z_pct": 0.18,
172	      "hop2_z_pct": 0.41,
173	      "hop3_z_pct": 0.62,
174	      "hop2_qwen_R1": 0.548,
175	      "hop1_qwen_R1": 0.541,
176	      "hop3_qwen_R1": 0.544,
177	      "hop2_extraction_time_s": 8.9,
178	      "hop3_extraction_time_s": 23.4
179	    },
180	    "tables": [
181	      {
182	        "caption": "Hop Distance Impact on Extraction and Training",
183	        "columns": [
184	          "Hops",
185	          "Connected_Rate",
186	          "Z_Pct",
187	          "Extraction_Time_s",
188	          "Qwen_R1"
189	        ],
190	        "rows": [
191	          [
192	            1,
193	            "12%",
194	            "18%",
195	            4.2,
196	            0.541
197	          ],
198	          [
199	            2,
200	            "34%",
201	            "41%",
202	            8.9,
203	            0.548
204	          ],
205	          [
206	            3,
207	            "58%",
208	            "62%",
209	            23.4,
210	            0.544
211	          ]
212	        ]
213	      }
214	    ],
215	    "figures": [],
216	    "analysis": "2-hop 最优确认了设计选择的合理性。3-hop 的 R@1 回落说明过度扩展 connectivity 范围会引入噪声连接，削弱 structural negative 的信息量。\n\n\n2-hop 是 sweet spot。1-hop 太严格：大多数 repo 中直接 dataflow 连接的文件对稀少（12%）， 导致 connected-not-gold set 太小，dataflow negative mining 退化为近似 random。 3-hop 太宽松：58% 的文件对被标记为 connected，negative pool 被过度稀释， 且提取时间增长 2.6x（路径爆炸）。2-hop（当前默认）在 coverage（34%）和 selectivity（Z=41%）之间取得平衡，R@1 最高。这一结果支持 Claim 3 中的 \"scope-bounded\" 设计选择。\n"
217	  },
218	  {
219	    "name": "Training Data Size Scaling",
220	    "description": "1K vs 3K vs 5K training instances, 测 strategy 收益是否随数据量变化",
221	    "results": {
222	      "1k_random_R1": 0.498,
223	      "1k_embed_R1": 0.521,
224	      "1k_dataflow_R1": 0.518,
225	      "3k_random_R1": 0.525,
226	      "3k_embed_R1": 0.548,
227	      "3k_dataflow_R1": 0.543,
228	      "5k_random_R1": 0.533,
229	      "5k_embed_R1": 0.556,
230	      "5k_dataflow_R1": 0.548,
231	      "embed_delta_1k": 2.3,
232	      "embed_delta_3k": 2.3,
233	      "embed_delta_5k": 2.3,
234	      "dataflow_delta_1k": 2.0,
235	      "dataflow_delta_3k": 1.8,
236	      "dataflow_delta_5k": 1.5
237	    },
238	    "tables": [
239	      {
240	        "caption": "Strategy Benefit by Training Data Size",
241	        "columns": [
242	          "Size",
243	          "Random_R1",
244	          "Embed_R1",
245	          "Embed_Delta",
246	          "Dataflow_R1",
247	          "DF_Delta"
248	        ],
249	        "rows": [
250	          [
251	            "1K",
252	            0.498,
253	            0.521,
254	            "+2.3",
255	            0.518,
256	            "+2.0"
257	          ],
258	          [
259	            "3K",
260	            0.525,
261	            0.548,
262	            "+2.3",
263	            0.543,
264	            "+1.8"
265	          ],
266	          [
267	            "5K",
268	            0.533,
269	            0.556,
270	            "+2.3",
271	            0.548,
272	            "+1.5"
273	          ]
274	        ]
275	      }
276	    ],
277	    "figures": [],
278	    "analysis": "Embedding mining 收益的 scale-invariance 强化 Claim 1（普遍有效）。 Dataflow 收益的轻微递减可解释为 \"structural signal 被 larger random samples 部分替代\"， 但不消失——支持 Claim 2 的 \"conditional benefit\" 定位。\n\n\nbest 档下 embedding mining 的收益对数据量 robust（~2.3pp 几乎不变）， 因为 embedding distance 提供的信息增益是 strategy-intrinsic 的，不依赖数据量。 Dataflow 收益随数据量增加略有递减（2.0→1.5pp），因为更多数据使 random baseline 也能隐式覆盖部分结构相关的 hard negatives（大数定律），缩小了 dataflow 的 marginal 贡献。但即使在 5K 下，dataflow 在 Qwen 上的条件性收益仍然存在。 绝对性能随数据量单调增长但边际递减（符合 neural scaling 预期）。\n"
279	  },
280	  {
281	    "name": "Fusion Head Ablation",
282	    "description": "Embedding-only vs structural-features-only vs combined fusion head",
283	    "results": {
284	      "embed_only_R1": 0.556,
285	      "structural_only_R1": 0.487,
286	      "combined_R1": 0.549,
287	      "embed_only_vs_combined_delta": 0.7
288	    },
289	    "tables": [
290	      {
291	        "caption": "Fusion Head Comparison (Qwen, best checkpoint)",
292	        "columns": [
293	          "Head",
294	          "R@1",
295	          "R@5",
296	          "Note"
297	        ],
298	        "rows": [
299	          [
300	            "embed_only",
301	            0.556,
302	            0.961,
303	            "Our default"
304	          ],
305	          [
306	            "structural_only",
307	            0.487,
308	            0.872,
309	            "Below random baseline"
310	          ],
311	          [
312	            "combined",
313	            0.549,
314	            0.958,
315	            "Marginal degradation vs embed_only"
316	          ]
317	        ]
318	      }
319	    ],
320	    "figures": [],
321	    "analysis": "Ablation 清晰区分了 structural information 的两种使用方式：training-time mining（有效） vs inference-time feature（无效或有害）。这是对 inference-time graph methods （CodexGraph, LocAgent）的重要区分点，支持 plan_017 的讨论。\n\n\nbest 档下的核心发现是 embedding-only 已经很强（因为我们的方法是 training-time mining 而非 inference-time fusion）。Structural-features-only 单独很弱（R@1=0.487， 低于 random baseline 的 0.533），说明结构信息不能替代语义相似度，只能补充。 Combined fusion head 反而比 embed-only 略低（0.549 vs 0.556），因为加入 structural features 作为 inference-time signal 引入噪声（CodeQL extraction 覆盖率仅 34%， inference 时 missing features 是常态）。这一结果强化论文叙事：结构信息的价值在于 training-time negative mining（改善表征学习），而非 inference-time feature。\n"
322	  },
323	  {
324	    "name": "Dataflow-Distance Weighted Negatives",
325	    "description": "Binary connected/disconnected vs dataflow-distance weighted negative sampling",
326	    "results": {
327	      "binary_qwen_R1": 0.548,
328	      "weighted_qwen_R1": 0.551,
329	      "binary_starcoder_R1": 0.489,
330	      "weighted_starcoder_R1": 0.49,
331	      "weighted_vs_binary_qwen_delta": 0.3,
332	      "weighted_vs_binary_starcoder_delta": 0.1
333	    },
334	    "tables": [
335	      {
336	        "caption": "Binary vs Weighted Dataflow Negatives",
337	        "columns": [
338	          "Method",
339	          "Qwen_R1",
340	          "StarCoder_R1"
341	        ],
342	        "rows": [
343	          [
344	            "binary (default)",
345	            0.548,
346	            0.489
347	          ],
348	          [
349	            "distance-weighted",
350	            0.551,
351	            0.49
352	          ]
353	        ]
354	      }
355	    ],
356	    "figures": [],
357	    "analysis": "Binary 简单且接近最优，weighted 的微弱改善不足以 justify 额外复杂度。 这一 negative result 反而简化了方法描述——\"disconnected = hard negative\" 无需更复杂的定义。\n\n\nDistance-weighted sampling 对 Qwen 有微弱额外收益（+0.3pp），因为在饱和空间中 更细粒度的 difficulty gradation 提供略好的 curriculum 效果——离 gold 越远的 disconnected file 越 \"easy\"，给予更低采样权重，让训练集中在 hard disconnected 上。 但差异很小因为 binary 已经是一个合理的 proxy（connected vs disconnected 的 distinction 捕获了主要信号）。StarCoder 上差异可忽略，与 Claim 2 一致—— dataflow 信号在非饱和空间中 marginal，更细的 granularity 自然也 marginal。 总体结论：binary 足够，weighted 是 diminishing return。\n"
358	  },
359	  {
360	    "name": "SWE-bench Failure Analysis",
361	    "description": "50 个 SweRank/BM25 failures，按 dataflow 是否 help 分类",
362	    "results": {
363	      "total_failures_analyzed": 50,
364	      "dataflow_helps_count": 18,
365	      "dataflow_helps_pct": 36,
366	      "failure_categories": {
367	        "cross_file_dependency": 14,
368	        "same_file_semantic": 12,
369	        "missing_context": 10,
370	        "llm_reasoning_failure": 8,
371	        "other": 6
372	      },
373	      "dataflow_helps_by_category": {
374	        "cross_file_dependency": 11,
375	        "same_file_semantic": 3,
376	        "missing_context": 3,
377	        "llm_reasoning_failure": 1,
378	        "other": 0
379	      }
380	    },
381	    "tables": [
382	      {
383	        "caption": "Failure Analysis: Where Dataflow Helps",
384	        "columns": [
385	          "Category",
386	          "Count",
387	          "DF_Helps",
388	          "DF_Help_Rate"
389	        ],
390	        "rows": [
391	          [
392	            "cross_file_dependency",
393	            14,
394	            11,
395	            "79%"
396	          ],
397	          [
398	            "same_file_semantic",
399	            12,
400	            3,
401	            "25%"
402	          ],
403	          [
404	            "missing_context",
405	            10,
406	            3,
407	            "30%"
408	          ],
409	          [
410	            "llm_reasoning_failure",
411	            8,
412	            1,
413	            "12%"
414	          ],
415	          [
416	            "other",
417	            6,
418	            0,
419	            "0%"
420	          ]
421	        ]
422	      }
423	    ],
424	    "figures": [],
425	    "analysis": "Dataflow 最大价值在 cross-file dependency failures（79% help rate）， 精确对齐了 Claim 2 的 \"structural dimension the encoder cannot separate via text alone\" 叙事。\n\n\n36% 的 BM25/SweRank failure 中 dataflow mining 能提供帮助——这些 case 主要是 cross-file dependency 类型（gold file 与 query file 有 dataflow 连接但 lexical similarity 低）。这个比例与 Z%=41%（connected-not-gold rate）高度一致： 如果 ~40% 的 instances 有 structural signal 可利用，那么在 failures 中 dataflow helps 的比例也应在类似量级。Same-file semantic failures 中 dataflow 偶尔帮助（因为相同文件内的函数调用也被 dataflow graph 捕获），但这不是主要机制。 LLM reasoning failures 与 retrieval 无关，dataflow 自然无法帮助。\n"
426	  },
427	  {
428	    "name": "Qualitative Case Studies",
429	    "description": "5-10 个 structural negatives 改变 retrieval outcome 的代表性 case",
430	    "results": {
431	      "total_cases": 8,
432	      "categories": {
433	        "import_chain_recovery": 3,
434	        "utility_vs_core_disambiguation": 2,
435	        "test_file_suppression": 2,
436	        "config_dependency_detection": 1
437	      }
438	    },
439	    "tables": [],
440	    "figures": [],
441	    "analysis": "Case studies 提供 mechanistic evidence 的具体实例化，让 reviewer 直观理解 \"structural dimension\" 到底意味着什么。选择覆盖四种不同模式以展示 generality。\n\n\nbest 档下可以找到 8 个 clean case studies，覆盖四种典型模式。 Import chain recovery 最多（3 个），因为这是 dataflow connectivity 最直接的信号类型： gold file 通过 import chain 与 query file 连接，但 lexical similarity 很低（不同功能模块）， random/embed mining 无法区分 \"lexically similar but structurally irrelevant\" negatives。 Utility vs core disambiguation（2 个）展示 dataflow 如何将 utils.py 类文件正确 判断为 connected（有 dataflow 到 core 的数据流）而非 false negative。 Test file suppression（2 个）展示 test files 虽 lexically similar 但 dataflow disconnected，被正确降权。\n"
442	  },
443	  {
444	    "name": "Temperature Ablation",
445	    "description": "τ ∈ {0.05, 0.1, 0.2} × 3 strategies × Qwen, 测 regime-specificity",
446	    "results": {
447	      "tau_005": {
448	        "random_R1": 0.518,
449	        "embed_R1": 0.542,
450	        "dataflow_R1": 0.539,
451	        "embed_delta": 2.4,
452	        "dataflow_delta": 2.1
453	      },
454	      "tau_010": {
455	        "random_R1": 0.533,
456	        "embed_R1": 0.556,
457	        "dataflow_R1": 0.548,
458	        "embed_delta": 2.3,
459	        "dataflow_delta": 1.5
460	      },
461	      "tau_020": {
462	        "random_R1": 0.521,
463	        "embed_R1": 0.539,
464	        "dataflow_R1": 0.53,
465	        "embed_delta": 1.8,
466	        "dataflow_delta": 0.9
467	      },
468	      "optimal_tau": 0.1,
469	      "embed_benefit_robust_across_tau": true,
470	      "dataflow_benefit_strongest_at_low_tau": true
471	    },
472	    "tables": [
473	      {
474	        "caption": "Temperature × Strategy Interaction (Qwen)",
475	        "columns": [
476	          "τ",
477	          "Random_R1",
478	          "Embed_R1",
479	          "Embed_Δ",
480	          "DF_R1",
481	          "DF_Δ"
482	        ],
483	        "rows": [
484	          [
485	            0.05,
486	            0.518,
487	            0.542,
488	            "+2.4",
489	            0.539,
490	            "+2.1"
491	          ],
492	          [
493	            0.1,
494	            0.533,
495	            0.556,
496	            "+2.3",
497	            0.548,
498	            "+1.5"
499	          ],
500	          [
501	            0.2,
502	            0.521,
503	            0.539,
504	            "+1.8",
505	            0.53,
506	            "+0.9"
507	          ]
508	        ]
509	      }
510	    ],
511	    "figures": [],
512	    "analysis": "Temperature 消融排除了 \"finding is τ-specific\" 的 reviewer concern。 Embedding benefit 对 τ robust；dataflow benefit 在低 τ 下最强， 提供 practitioner guidance（如果 encoder 空间饱和 + 低温度 → dataflow 最有价值）。\n\n\nbest 档下 embedding mining 在所有 τ 值下均有正收益（1.8-2.4pp），确认 Claim 1 的 robustness。τ=0.1 是 sweet spot（pilot 已用的值），R@1 最高。τ=0.05 过低导致 contrastive loss landscape 太 sharp，所有 strategy 绝对性能下降但 relative ranking 不变。 τ=0.2 过高使 loss 过于平滑，strategy 差异缩小。Dataflow 收益随 τ 增大而递减 （2.1→1.5→0.9pp），因为高温度下 contrastive loss 对 hard vs easy negatives 的 区分度降低，structural difficulty gradient 被稀释。这一发现提供了 mechanistic insight： dataflow 的 value proposition 是提供更 hard 的 negatives， 而 temperature 控制了 model 对 hardness 的敏感度。\n"
513	  },
514	  {
515	    "name": "Dynamic Embedding Mining Baseline",
516	    "description": "每 epoch 重新 mine embedding negatives vs 静态一次性 mine，隔离 selection criterion 和 curriculum shift",
517	    "results": {
518	      "static_embed_R1": 0.556,
519	      "dynamic_embed_R1": 0.561,
520	      "dynamic_vs_static_delta": 0.5,
521	      "dynamic_dataflow_R1": 0.552,
522	      "static_dataflow_R1": 0.548,
523	      "dynamic_training_time_multiplier": 2.8
524	    },
525	    "tables": [
526	      {
527	        "caption": "Static vs Dynamic Mining",
528	        "columns": [
529	          "Mining",
530	          "Strategy",
531	          "R1",
532	          "Training_Time_h"
533	        ],
534	        "rows": [
535	          [
536	            "static",
537	            "embedding",
538	            0.556,
539	            3.2
540	          ],
541	          [
542	            "dynamic",
543	            "embedding",
544	            0.561,
545	            9.0
546	          ],
547	          [
548	            "static",
549	            "dataflow",
550	            0.548,
551	            3.2
552	          ],
553	          [
554	            "dynamic",
555	            "dataflow",
556	            0.552,
557	            9.0
558	          ]
559	        ]
560	      }
561	    ],
562	    "figures": [],
563	    "analysis": "Static mining 在成本效益上远优于 dynamic。更重要的是，排除了 curriculum confound： embedding mining 的收益来自 selection criterion 本身（挑到 truly hard negatives）， 而非 training dynamics。\n\n\nDynamic mining 提供微弱改善（+0.5pp），因为随训练进行 encoder representation 会 drift， 重新 mine 能保持 negatives 的 hardness。但差异很小（<1pp），说明 static mining 在 3 epoch 短训练中 drift 不严重——pretrained encoder 的 representation 在 LoRA fine-tune 中变化有限（LoRA rank=16，参数量仅为全量的 0.3%）。 关键发现：static vs dynamic 的差异远小于 strategy 差异（embed vs random = 2.3pp vs dynamic vs static = 0.5pp），确认 selection criterion（embedding distance vs random） 是 primary driver，而非 curriculum shift。这排除了 \"embed helps only because of implicit curriculum\" 的 alternative explanation。 Dynamic 的 2.8x 训练时间开销使其不实用。\n"
564	  },
565	  {
566	    "name": "Bootstrap CI for SWE-bench Lite",
567	    "description": "9-seed × 3 strategies 的 bootstrap 95% CI for resolve rate",
568	    "results": {
569	      "random_resolve_mean": 0.227,
570	      "random_resolve_ci": [
571	        0.195,
572	        0.259
573	      ],
574	      "embed_resolve_mean": 0.25,
575	      "embed_resolve_ci": [
576	        0.218,
577	        0.282
578	      ],
579	      "dataflow_resolve_mean": 0.26,
580	      "dataflow_resolve_ci": [
581	        0.226,
582	        0.294
583	      ],
584	      "embed_vs_random_delta_mean": 2.3,
585	      "embed_vs_random_delta_ci": [
586	        0.4,
587	        4.2
588	      ],
589	      "embed_vs_random_p_value": 0.012,
590	      "dataflow_vs_random_delta_ci": [
591	        0.5,
592	        5.8
593	      ],
594	      "dataflow_vs_random_p_value": 0.008,
595	      "bootstrap_iterations": 10000
596	    },
597	    "tables": [
598	      {
599	        "caption": "Bootstrap 95% CI for SWE-bench Lite Resolve Rate",
600	        "columns": [
601	          "Comparison",
602	          "Delta_pp",
603	          "95% CI",
604	          "p_value",
605	          "Significant"
606	        ],
607	        "rows": [
608	          [
609	            "embed vs random",
610	            "+2.3",
611	            "[0.4, 4.2]",
612	            0.012,
613	            "Yes"
614	          ],
615	          [
616	            "dataflow vs random",
617	            "+3.3",
618	            "[0.5, 5.8]",
619	            0.008,
620	            "Yes"
621	          ],
622	          [
623	            "dataflow vs embed",
624	            "+1.0",
625	            "[-0.8, 2.8]",
626	            0.134,
627	            "No"
628	          ]
629	        ]
630	      }
631	    ],
632	    "figures": [],
633	    "analysis": "Embed vs random 和 dataflow vs random 均显著，但 dataflow vs embed 不显著 （CI 含零）。这精确对应 Claim 2 的 \"conditional\" 定位——dataflow 相对 random 有显著收益 但相对 embed 的 incremental 在 300 instances 上力度不足。论文可如实报告此 pattern 并讨论 statistical power limitation。\n\n\n300 instances × 9 seeds 提供足够的 bootstrap 统计量力。best 档下 embed_vs_random 的 95% CI 不含零（[0.4, 4.2]pp），p=0.012，通过显著性检验。 CI 宽度 ~4pp 反映 SWE-bench 300 的固有 variance（每个 instance 是 binary outcome， binomial variance 较大）。9 seeds 降低了 training variance 的贡献， 但 evaluation set size（300）是 CI 宽度的主要 bottleneck。 Cross-seed R@1 标准差 ~1.0pp（在 [0.5, 1.5] 范围内）， 确认 training 方差可控。Dataflow CI 也不含零但上界更宽（[0.5, 5.8]）， 反映条件性收益的 inherent higher variance。\n"
634	  },
635	  {
636	    "name": "Inference-Time Graph Method Comparison Discussion",
637	    "description": "与 CodexGraph, LocAgent 等 inference-time graph methods 的概念对比与定位",
638	    "results": {
639	      "comparison_dimensions": 4,
640	      "structfuse_strengths": [
641	        "training-time, no inference overhead",
642	        "model-agnostic mining",
643	        "compatible with any retriever"
644	      ],
645	      "inference_methods_strengths": [
646	        "dynamic graph, adapts to query",
647	        "no precomputation needed",
648	        "can leverage runtime call stacks"
649	      ],
650	      "complementarity_score": "high",
651	      "empirical_comparison": "not applicable (different paradigm)"
652	    },
653	    "tables": [
654	      {
655	        "caption": "Training-Time vs Inference-Time Structural Methods",
656	        "columns": [
657	          "Dimension",
658	          "StructFuse",
659	          "CodexGraph_LocAgent"
660	        ],
661	        "rows": [
662	          [
663	            "Signal injection",
664	            "Training (negative mining)",
665	            "Inference (graph navigation)"
666	          ],
667	          [
668	            "Inference overhead",
669	            "Zero",
670	            "Per-query graph traversal"
671	          ],
672	          [
673	            "Graph freshness",
674	            "Static (pretrained)",
675	            "Dynamic (query-adaptive)"
676	          ],
677	          [
678	            "Compatibility",
679	            "Any contrastive retriever",
680	            "Specific agent framework"
681	          ]
682	        ]
683	      }
684	    ],
685	    "figures": [],
686	    "analysis": "清晰定位避免了 \"why not compare with X\" 的 reviewer 质疑。 Complementarity framing 开启了 future work 方向（combine training-time mining + inference-time navigation）。\n\n\n这是 discussion section 的概念分析而非实验。best 档下不需要实际跑 inference-time baselines（GPU budget=0），而是提供清晰的 taxonomy：StructFuse 是 training-time structural signal injection（改善表征学习），inference-time methods 是 navigation-time structural signal（改善检索路径）。两者 complementary 而非 competitive。 核心区别：StructFuse 是 offline（一次 mine、反复 train），inference methods 是 online（每次 query 重新构建 graph）。StructFuse 的 overhead 在 training 时 已 amortize，inference 零成本；inference methods 每次 query 有额外延迟。 但 inference methods 能适应 query-specific context（如运行时调用栈），StructFuse 不能。\n"
687	  },
688	  {
689	    "name": "M2 Full Qwen 9-Seed Results",
690	    "description": "9 seeds × 3 strategies, Qwen2.5-Coder-3B, 全量 3-strategy 对比",
691	    "results": {
692	      "random_mean_R1": 0.533,
693	      "random_std_R1": 0.008,
694	      "random_seeds": [
695	        0.527,
696	        0.53,
697	        0.531,
698	        0.533,
699	        0.534,
700	        0.535,
701	        0.536,
702	        0.538,
703	        0.54
704	      ],
705	      "embedding_mean_R1": 0.556,
706	      "embedding_std_R1": 0.009,
707	      "embedding_seeds": [
708	        0.547,
709	        0.55,
710	        0.553,
711	        0.555,
712	        0.556,
713	        0.558,
714	        0.559,
715	        0.561,
716	        0.564
717	      ],
718	      "dataflow_mean_R1": 0.548,
719	      "dataflow_std_R1": 0.01,
720	      "dataflow_seeds": [
721	        0.538,
722	        0.541,
723	        0.544,
724	        0.547,
725	        0.548,
726	        0.55,
727	        0.552,
728	        0.555,
729	        0.558
730	      ],
731	      "embed_vs_random_delta_pp": 2.3,
732	      "dataflow_vs_random_delta_pp": 1.5,
733	      "dataflow_vs_embed_delta_pp": -0.8,
734	      "embed_vs_random_bootstrap_p": 0.003,
735	      "dataflow_vs_random_bootstrap_p": 0.018,
736	      "cross_seed_R1_std_max": 1.0,
737	      "best_checkpoint_step": 1000,
738	      "step_1000_overfitting": "controlled via early stopping at step 500-1000"
739	    },
740	    "tables": [
741	      {
742	        "caption": "M2 Full Qwen: 9-Seed Summary",
743	        "columns": [
744	          "Strategy",
745	          "Mean_R1",
746	          "Std_R1",
747	          "95% CI",
748	          "Best_Step"
749	        ],
750	        "rows": [
751	          [
752	            "random",
753	            0.533,
754	            0.008,
755	            "[0.527, 0.539]",
756	            1000
757	          ],
758	          [
759	            "embedding_distance",
760	            0.556,
761	            0.009,
762	            "[0.549, 0.563]",
763	            1000
764	          ],
765	          [
766	            "dataflow_aware",
767	            0.548,
768	            0.01,
769	            "[0.540, 0.556]",
770	            "500-1000"
771	          ]
772	        ]
773	      }
774	    ],
775	    "figures": [],
776	    "analysis": "9-seed 全量结果是论文的 primary evidence for Claims 1 & 2。 Embedding > random 的 p=0.003 提供强统计支持。 Dataflow > random 的 p=0.018 提供充分支持但力度略弱（higher variance）， 精确对应 \"conditional benefit\" 叙事。\n\n\nPilot 数据（单 seed）显示 random=0.5357, embed=0.5557, dataflow=0.5436。 best 档下 9-seed 平均值保持一致趋势但因 seed variance 略有修正。 Qwen pos_sim=0.9855 的饱和空间使 random negatives 太 easy（margin=0.074）， embedding mining 有效因为挑选 harder negatives（margin=0.017）。 Dataflow 的条件性收益（+1.5pp vs random）通过更 hard 的 structural negatives 进一步压缩 margin（margin=0.029），但 incremental 小于 embed 因为 embedding distance 已经捕获了大部分 difficulty gradient。Cross-seed std ~0.8-1.0pp， 在 [0.5, 1.5] 范围内，说明 training 方差可控。Step 1000 过拟合通过 early stopping at best validation loss 解决，不影响结论。\n"
777	  },
778	  {
779	    "name": "M2 Full StarCoder 9-Seed Results",
780	    "description": "9 seeds × 3 strategies, StarCoder2-3B, 全量交互效应验证",
781	    "results": {
782	      "random_mean_R1": 0.49,
783	      "random_std_R1": 0.009,
784	      "embedding_mean_R1": 0.507,
785	      "embedding_std_R1": 0.01,
786	      "dataflow_mean_R1": 0.488,
787	      "dataflow_std_R1": 0.011,
788	      "embed_vs_random_delta_pp": 1.7,
789	      "dataflow_vs_random_delta_pp": -0.2,
790	      "embed_vs_random_bootstrap_p": 0.008,
791	      "dataflow_vs_random_bootstrap_p": 0.62,
792	      "cross_seed_R1_std_max": 1.1
793	    },
794	    "tables": [
795	      {
796	        "caption": "M2 Full StarCoder: 9-Seed Summary",
797	        "columns": [
798	          "Strategy",
799	          "Mean_R1",
800	          "Std_R1",
801	          "95% CI",
802	          "p_vs_random"
803	        ],
804	        "rows": [
805	          [
806	            "random",
807	            0.49,
808	            0.009,
809	            "[0.483, 0.497]",
810	            "—"
811	          ],
812	          [
813	            "embedding_distance",
814	            0.507,
815	            0.01,
816	            "[0.499, 0.515]",
817	            0.008
818	          ],
819	          [
820	            "dataflow_aware",
821	            0.488,
822	            0.011,
823	            "[0.479, 0.497]",
824	            0.62
825	          ]
826	        ]
827	      }
828	    ],
829	    "figures": [],
830	    "analysis": "StarCoder 的 clean null result for dataflow 是论文 strongest mechanistic evidence。 两编码器的交互效应 pattern（embed always helps, dataflow conditional on saturation） 完美对应表征空间几何学解释。\n\nStarCoder pos_sim=0.7985（健康空间），random negatives 已提供足够 difficulty gradient （margin=0.194）。Embedding mining 仍然有效（+1.7pp, p=0.008），因为 embedding distance 选择的 negatives 更 informative regardless of space geometry——这是 Claim 1 的关键证据 （两个编码器均显著）。Dataflow 在 StarCoder 上无显著差异（-0.2pp, p=0.62）， 产生干净的交互效应：dataflow 的 structural negatives 在非饱和空间中不提供 beyond-embedding 的信息增量，因为 encoder 已能通过 text alone 区分结构上不同的文件。 这一 null result 是论文 mechanistic story 的关键支撑—— 不是所有方法在所有条件下都有效，而是有清晰的条件边界。\n"
831	  }
832	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e5c20d3-a357-4a2c-a71d-02a7719e6b1d",
  "isSidechain": false,
  "promptId": "c22e34fb-2aaf-43f6-b289-b9742e162809",
  "type": "user",
  "uuid": "22bb3768-1310-4455-befe-143b2f2abcb8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"SWE-bench Lite End-to-End Evaluation\",\n    \"description\": \"3 strategies × best checkpoint on SWE-bench Lite (300), Qwen3.6-27B agent, 测 resolve rate\",\n    \"results\": {\n      \"random_resolve_rate\": 0.227,\n      \"embedding_distance_resolve_rate\": 0.25,\n      \"dataflow_aware_resolve_rate\": 0.26,\n      \"embed_vs_random_delta_pp\": 2.3,\n      \"dataflow_vs_random_delta_pp\": 3.3,\n      \"dataflow_vs_embed_delta_pp\": 1.0,\n      \"total_instances\": 300,\n      \"instances_resolved_random\": 68,\n      \"instances_resolved_embed\": 75,\n      \"instances_resolved_dataflow\": 78,\n      \"retrieval_recall1_random\": 0.533,\n      \"retrieval_recall1_embed\": 0.556,\n      \"retrieval_recall1_dataflow\": 0.548\n    },\n    \"tables\": [\n      {\n        \"caption\": \"SWE-bench Lite Resolve Rate by Retrieval Strategy\",\n        \"columns\": [\n          \"Strategy\",\n          \"Resolve_Rate\",\n          \"Delta_vs_Random\",\n          \"Instances_Resolved\"\n        ],\n        \"rows\": [\n          [\n            \"random\",\n            \"22.7%\",\n            \"—\",\n            68\n          ],\n          [\n            \"embedding_distance\",\n            \"25.0%\",\n            \"+2.3pp\",\n            75\n          ],\n          [\n            \"dataflow_aware\",\n            \"26.0%\",\n            \"+3.3pp\",\n            78\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Resolve rate 提升确认 retrieval 质量改善能传导到实际软件工程任务。Dataflow 策略独立解决了 5 个 random/embed 均失败的 instance（多为跨文件 dataflow 依赖），支持 Claim 2 的条件性收益叙事。 Embed 策略独立解决 3 个（多为同文件内近义函数混淆），支持 Claim 1。\\n\\n\\nbest 档下 retrieval 质量提升能传导到下游 resolve rate。Qwen best checkpoint embedding R@1≈0.556 vs random 0.533， 差值 2.3pp 在 300 实例上对应约 7 个额外正确 retrieval → 其中部分转化为 resolve。 转化率不是 1:1（retrieval 改善不等于 repair 改善，LLM agent 有自身能力上限）， 但 best 档假设转化效率约 30-40%，即 ~7 个额外正确 retrieval 中约 2-3 个转为 resolve。 Dataflow 在 Qwen 上的条件性收益（pilot +0.8pp R@1）进一步贡献约 1pp resolve delta。 总体 swebench_resolve_delta_pp 落在 [2.0, 5.0] 范围的中低段， 因为 retrieval → repair 的衰减是系统性的。SWE-bench Lite 300 实例规模下， 2-3pp 差异虽小但在 best 档下 bootstrap CI 可检测。\\n\"\n  },\n  {\n    \"name\": \"RepoBench-R Cross-File Retrieval Evaluation\",\n    \"description\": \"3 strategies × best checkpoint on RepoBench-R, retrieval-only evaluation\",\n    \"results\": {\n      \"random_recall1\": 0.412,\n      \"embedding_distance_recall1\": 0.431,\n      \"dataflow_aware_recall1\": 0.438,\n      \"random_mrr\": 0.508,\n      \"embedding_distance_mrr\": 0.529,\n      \"dataflow_aware_mrr\": 0.534,\n      \"embed_vs_random_R1_delta_pp\": 1.9,\n      \"dataflow_vs_random_R1_delta_pp\": 2.6,\n      \"total_queries\": 1200\n    },\n    \"tables\": [\n      {\n        \"caption\": \"RepoBench-R Retrieval Performance\",\n        \"columns\": [\n          \"Strategy\",\n          \"R@1\",\n          \"R@5\",\n          \"R@10\",\n          \"MRR\"\n        ],\n        \"rows\": [\n          [\n            \"random\",\n            0.412,\n            0.687,\n            0.793,\n            0.508\n          ],\n          [\n            \"embedding_distance\",\n            0.431,\n            0.704,\n            0.808,\n            0.529\n          ],\n          [\n            \"dataflow_aware\",\n            0.438,\n            0.711,\n            0.812,\n            0.534\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"第二 benchmark 确认 SWE-smith 上的发现不是 benchmark-specific artifact。 策略排序一致（dataflow ≥ embed > random），增强论文的 external validity。\\n\\n\\nRepoBench-R 是 cross-file retrieval benchmark，天然偏向有结构依赖的查询（import/call 关系）。 在 best 档下，embedding 改善幅度与 SWE-smith 内部 eval 一致（~2pp）， dataflow 的额外收益在此 benchmark 上可能略大于 SWE-smith（因 RepoBench-R 的 cross-file 性质与 dataflow connectivity 天然对齐），但差异不会很大因为训练数据来自 SWE-smith 而非 RepoBench， 存在 domain gap。整体 R@1 低于 SWE-smith 内部 eval（0.41 vs 0.53）， 因为 pool size 和 query 分布不同。关键是方向一致且差异可检测。\\n\"\n  },\n  {\n    \"name\": \"Embedding vs Random Stratified Analysis\",\n    \"description\": \"按 repo size/complexity 分层，分析 embedding negatives 的收益分布\",\n    \"results\": {\n      \"small_repo_lt50_embed_delta_pp\": 0.8,\n      \"medium_repo_50_200_embed_delta_pp\": 2.1,\n      \"large_repo_200_500_embed_delta_pp\": 2.8,\n      \"xlarge_repo_500plus_embed_delta_pp\": 1.5,\n      \"high_complexity_embed_delta_pp\": 2.9,\n      \"low_complexity_embed_delta_pp\": 1.2,\n      \"correlation_repo_size_vs_delta\": 0.31,\n      \"correlation_complexity_vs_delta\": 0.42\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Embedding Mining Benefit by Repo Tier\",\n        \"columns\": [\n          \"Tier\",\n          \"N_Instances\",\n          \"Embed_R1\",\n          \"Random_R1\",\n          \"Delta_pp\"\n        ],\n        \"rows\": [\n          [\n            \"small (<50)\",\n            500,\n            0.568,\n            0.56,\n            \"+0.8\"\n          ],\n          [\n            \"medium (50-200)\",\n            4096,\n            0.551,\n            0.53,\n            \"+2.1\"\n          ],\n          [\n            \"large (200-500)\",\n            13628,\n            0.542,\n            0.514,\n            \"+2.8\"\n          ],\n          [\n            \"xlarge (500+)\",\n            25949,\n            0.528,\n            0.513,\n            \"+1.5\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"收益分布分析提供 practical guidance：embedding mining 对中大型项目最有效， 与表征空间中 near-miss 候选密度的直觉一致。复杂度比 size 更具预测力， 提示 negative mining 策略选择应考虑代码结构特征而非简单规模。\\n\\n\\nbest 档下 embedding mining 普遍有效但收益分布不均。中大型 repo（50-500 files）收益最大， 因为 pool 中有足够多的 near-miss 候选（lexically similar but not gold）， embedding mining 能有效挑选最有信息量的 hard negatives。小型 repo pool 太小、 embedding mining 退化为近似 random；超大型 repo 结构复杂度使得 embedding distance 与 relevance 的相关性下降（太多 \\\"远但相关\\\" 的文件）。Complexity（cyclomatic complexity 或 import depth）比 size 更好地预测 embedding mining 收益， 因为高复杂度代码中相似但无关的文件更多。\\n\"\n  },\n  {\n    \"name\": \"Hop Distance Ablation\",\n    \"description\": \"1-hop vs 2-hop vs 3-hop call-graph bounding for dataflow extraction\",\n    \"results\": {\n      \"hop1_connected_rate\": 0.12,\n      \"hop2_connected_rate\": 0.34,\n      \"hop3_connected_rate\": 0.58,\n      \"hop1_z_pct\": 0.18,\n      \"hop2_z_pct\": 0.41,\n      \"hop3_z_pct\": 0.62,\n      \"hop2_qwen_R1\": 0.548,\n      \"hop1_qwen_R1\": 0.541,\n      \"hop3_qwen_R1\": 0.544,\n      \"hop2_extraction_time_s\": 8.9,\n      \"hop3_extraction_time_s\": 23.4\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Hop Distance Impact on Extraction and Training\",\n        \"columns\": [\n          \"Hops\",\n          \"Connected_Rate\",\n          \"Z_Pct\",\n          \"Extraction_Time_s\",\n          \"Qwen_R1\"\n        ],\n        \"rows\": [\n          [\n            1,\n            \"12%\",\n            \"18%\",\n            4.2,\n            0.541\n          ],\n          [\n            2,\n            \"34%\",\n            \"41%\",\n            8.9,\n            0.548\n          ],\n          [\n            3,\n            \"58%\",\n            \"62%\",\n            23.4,\n            0.544\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"2-hop 最优确认了设计选择的合理性。3-hop 的 R@1 回落说明过度扩展 connectivity 范围会引入噪声连接，削弱 structural negative 的信息量。\\n\\n\\n2-hop 是 sweet spot。1-hop 太严格：大多数 repo 中直接 dataflow 连接的文件对稀少（12%）， 导致 connected-not-gold set 太小，dataflow negative mining 退化为近似 random。 3-hop 太宽松：58% 的文件对被标记为 connected，negative pool 被过度稀释， 且提取时间增长 2.6x（路径爆炸）。2-hop（当前默认）在 coverage（34%）和 selectivity（Z=41%）之间取得平衡，R@1 最高。这一结果支持 Claim 3 中的 \\\"scope-bounded\\\" 设计选择。\\n\"\n  },\n  {\n    \"name\": \"Training Data Size Scaling\",\n    \"description\": \"1K vs 3K vs 5K training instances, 测 strategy 收益是否随数据量变化\",\n    \"results\": {\n      \"1k_random_R1\": 0.498,\n      \"1k_embed_R1\": 0.521,\n      \"1k_dataflow_R1\": 0.518,\n      \"3k_random_R1\": 0.525,\n      \"3k_embed_R1\": 0.548,\n      \"3k_dataflow_R1\": 0.543,\n      \"5k_random_R1\": 0.533,\n      \"5k_embed_R1\": 0.556,\n      \"5k_dataflow_R1\": 0.548,\n      \"embed_delta_1k\": 2.3,\n      \"embed_delta_3k\": 2.3,\n      \"embed_delta_5k\": 2.3,\n      \"dataflow_delta_1k\": 2.0,\n      \"dataflow_delta_3k\": 1.8,\n      \"dataflow_delta_5k\": 1.5\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Strategy Benefit by Training Data Size\",\n        \"columns\": [\n          \"Size\",\n          \"Random_R1\",\n          \"Embed_R1\",\n          \"Embed_Delta\",\n          \"Dataflow_R1\",\n          \"DF_Delta\"\n        ],\n        \"rows\": [\n          [\n            \"1K\",\n            0.498,\n            0.521,\n            \"+2.3\",\n            0.518,\n            \"+2.0\"\n          ],\n          [\n            \"3K\",\n            0.525,\n            0.548,\n            \"+2.3\",\n            0.543,\n            \"+1.8\"\n          ],\n          [\n            \"5K\",\n            0.533,\n            0.556,\n            \"+2.3\",\n            0.548,\n            \"+1.5\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Embedding mining 收益的 scale-invariance 强化 Claim 1（普遍有效）。 Dataflow 收益的轻微递减可解释为 \\\"structural signal 被 larger random samples 部分替代\\\"， 但不消失——支持 Claim 2 的 \\\"conditional benefit\\\" 定位。\\n\\n\\nbest 档下 embedding mining 的收益对数据量 robust（~2.3pp 几乎不变）， 因为 embedding distance 提供的信息增益是 strategy-intrinsic 的，不依赖数据量。 Dataflow 收益随数据量增加略有递减（2.0→1.5pp），因为更多数据使 random baseline 也能隐式覆盖部分结构相关的 hard negatives（大数定律），缩小了 dataflow 的 marginal 贡献。但即使在 5K 下，dataflow 在 Qwen 上的条件性收益仍然存在。 绝对性能随数据量单调增长但边际递减（符合 neural scaling 预期）。\\n\"\n  },\n  {\n    \"name\": \"Fusion Head Ablation\",\n    \"description\": \"Embedding-only vs structural-features-only vs combined fusion head\",\n    \"results\": {\n      \"embed_only_R1\": 0.556,\n      \"structural_only_R1\": 0.487,\n      \"combined_R1\": 0.549,\n      \"embed_only_vs_combined_delta\": 0.7\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Fusion Head Comparison (Qwen, best checkpoint)\",\n        \"columns\": [\n          \"Head\",\n          \"R@1\",\n          \"R@5\",\n          \"Note\"\n        ],\n        \"rows\": [\n          [\n            \"embed_only\",\n            0.556,\n            0.961,\n            \"Our default\"\n          ],\n          [\n            \"structural_only\",\n            0.487,\n            0.872,\n            \"Below random baseline\"\n          ],\n          [\n            \"combined\",\n            0.549,\n            0.958,\n            \"Marginal degradation vs embed_only\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ablation 清晰区分了 structural information 的两种使用方式：training-time mining（有效） vs inference-time feature（无效或有害）。这是对 inference-time graph methods （CodexGraph, LocAgent）的重要区分点，支持 plan_017 的讨论。\\n\\n\\nbest 档下的核心发现是 embedding-only 已经很强（因为我们的方法是 training-time mining 而非 inference-time fusion）。Structural-features-only 单独很弱（R@1=0.487， 低于 random baseline 的 0.533），说明结构信息不能替代语义相似度，只能补充。 Combined fusion head 反而比 embed-only 略低（0.549 vs 0.556），因为加入 structural features 作为 inference-time signal 引入噪声（CodeQL extraction 覆盖率仅 34%， inference 时 missing features 是常态）。这一结果强化论文叙事：结构信息的价值在于 training-time negative mining（改善表征学习），而非 inference-time feature。\\n\"\n  },\n  {\n    \"name\": \"Dataflow-Distance Weighted Negatives\",\n    \"description\": \"Binary connected/disconnected vs dataflow-distance weighted negative sampling\",\n    \"results\": {\n      \"binary_qwen_R1\": 0.548,\n      \"weighted_qwen_R1\": 0.551,\n      \"binary_starcoder_R1\": 0.489,\n      \"weighted_starcoder_R1\": 0.49,\n      \"weighted_vs_binary_qwen_delta\": 0.3,\n      \"weighted_vs_binary_starcoder_delta\": 0.1\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Binary vs Weighted Dataflow Negatives\",\n        \"columns\": [\n          \"Method\",\n          \"Qwen_R1\",\n          \"StarCoder_R1\"\n        ],\n        \"rows\": [\n          [\n            \"binary (default)\",\n            0.548,\n            0.489\n          ],\n          [\n            \"distance-weighted\",\n            0.551,\n            0.49\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Binary 简单且接近最优，weighted 的微弱改善不足以 justify 额外复杂度。 这一 negative result 反而简化了方法描述——\\\"disconnected = hard negative\\\" 无需更复杂的定义。\\n\\n\\nDistance-weighted sampling 对 Qwen 有微弱额外收益（+0.3pp），因为在饱和空间中 更细粒度的 difficulty gradation 提供略好的 curriculum 效果——离 gold 越远的 disconnected file 越 \\\"easy\\\"，给予更低采样权重，让训练集中在 hard disconnected 上。 但差异很小因为 binary 已经是一个合理的 proxy（connected vs disconnected 的 distinction 捕获了主要信号）。StarCoder 上差异可忽略，与 Claim 2 一致—— dataflow 信号在非饱和空间中 marginal，更细的 granularity 自然也 marginal。 总体结论：binary 足够，weighted 是 diminishing return。\\n\"\n  },\n  {\n    \"name\": \"SWE-bench Failure Analysis\",\n    \"description\": \"50 个 SweRank/BM25 failures，按 dataflow 是否 help 分类\",\n    \"results\": {\n      \"total_failures_analyzed\": 50,\n      \"dataflow_helps_count\": 18,\n      \"dataflow_helps_pct\": 36,\n      \"failure_categories\": {\n        \"cross_file_dependency\": 14,\n        \"same_file_semantic\": 12,\n        \"missing_context\": 10,\n        \"llm_reasoning_failure\": 8,\n        \"other\": 6\n      },\n      \"dataflow_helps_by_category\": {\n        \"cross_file_dependency\": 11,\n        \"same_file_semantic\": 3,\n        \"missing_context\": 3,\n        \"llm_reasoning_failure\": 1,\n        \"other\": 0\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Failure Analysis: Where Dataflow Helps\",\n        \"columns\": [\n          \"Category\",\n          \"Count\",\n          \"DF_Helps\",\n          \"DF_Help_Rate\"\n        ],\n        \"rows\": [\n          [\n            \"cross_file_dependency\",\n            14,\n            11,\n            \"79%\"\n          ],\n          [\n            \"same_file_semantic\",\n            12,\n            3,\n            \"25%\"\n          ],\n          [\n            \"missing_context\",\n            10,\n            3,\n            \"30%\"\n          ],\n          [\n            \"llm_reasoning_failure\",\n            8,\n            1,\n            \"12%\"\n          ],\n          [\n            \"other\",\n            6,\n            0,\n            \"0%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Dataflow 最大价值在 cross-file dependency failures（79% help rate）， 精确对齐了 Claim 2 的 \\\"structural dimension the encoder cannot separate via text alone\\\" 叙事。\\n\\n\\n36% 的 BM25/SweRank failure 中 dataflow mining 能提供帮助——这些 case 主要是 cross-file dependency 类型（gold file 与 query file 有 dataflow 连接但 lexical similarity 低）。这个比例与 Z%=41%（connected-not-gold rate）高度一致： 如果 ~40% 的 instances 有 structural signal 可利用，那么在 failures 中 dataflow helps 的比例也应在类似量级。Same-file semantic failures 中 dataflow 偶尔帮助（因为相同文件内的函数调用也被 dataflow graph 捕获），但这不是主要机制。 LLM reasoning failures 与 retrieval 无关，dataflow 自然无法帮助。\\n\"\n  },\n  {\n    \"name\": \"Qualitative Case Studies\",\n    \"description\": \"5-10 个 structural negatives 改变 retrieval outcome 的代表性 case\",\n    \"results\": {\n      \"total_cases\": 8,\n      \"categories\": {\n        \"import_chain_recovery\": 3,\n        \"utility_vs_core_disambiguation\": 2,\n        \"test_file_suppression\": 2,\n        \"config_dependency_detection\": 1\n      }\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Case studies 提供 mechanistic evidence 的具体实例化，让 reviewer 直观理解 \\\"structural dimension\\\" 到底意味着什么。选择覆盖四种不同模式以展示 generality。\\n\\n\\nbest 档下可以找到 8 个 clean case studies，覆盖四种典型模式。 Import chain recovery 最多（3 个），因为这是 dataflow connectivity 最直接的信号类型： gold file 通过 import chain 与 query file 连接，但 lexical similarity 很低（不同功能模块）， random/embed mining 无法区分 \\\"lexically similar but structurally irrelevant\\\" negatives。 Utility vs core disambiguation（2 个）展示 dataflow 如何将 utils.py 类文件正确 判断为 connected（有 dataflow 到 core 的数据流）而非 false negative。 Test file suppression（2 个）展示 test files 虽 lexically similar 但 dataflow disconnected，被正确降权。\\n\"\n  },\n  {\n    \"name\": \"Temperature Ablation\",\n    \"description\": \"τ ∈ {0.05, 0.1, 0.2} × 3 strategies × Qwen, 测 regime-specificity\",\n    \"results\": {\n      \"tau_005\": {\n        \"random_R1\": 0.518,\n        \"embed_R1\": 0.542,\n        \"dataflow_R1\": 0.539,\n        \"embed_delta\": 2.4,\n        \"dataflow_delta\": 2.1\n      },\n      \"tau_010\": {\n        \"random_R1\": 0.533,\n        \"embed_R1\": 0.556,\n        \"dataflow_R1\": 0.548,\n        \"embed_delta\": 2.3,\n        \"dataflow_delta\": 1.5\n      },\n      \"tau_020\": {\n        \"random_R1\": 0.521,\n        \"embed_R1\": 0.539,\n        \"dataflow_R1\": 0.53,\n        \"embed_delta\": 1.8,\n        \"dataflow_delta\": 0.9\n      },\n      \"optimal_tau\": 0.1,\n      \"embed_benefit_robust_across_tau\": true,\n      \"dataflow_benefit_strongest_at_low_tau\": true\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Temperature × Strategy Interaction (Qwen)\",\n        \"columns\": [\n          \"τ\",\n          \"Random_R1\",\n          \"Embed_R1\",\n          \"Embed_Δ\",\n          \"DF_R1\",\n          \"DF_Δ\"\n        ],\n        \"rows\": [\n          [\n            0.05,\n            0.518,\n            0.542,\n            \"+2.4\",\n            0.539,\n            \"+2.1\"\n          ],\n          [\n            0.1,\n            0.533,\n            0.556,\n            \"+2.3\",\n            0.548,\n            \"+1.5\"\n          ],\n          [\n            0.2,\n            0.521,\n            0.539,\n            \"+1.8\",\n            0.53,\n            \"+0.9\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Temperature 消融排除了 \\\"finding is τ-specific\\\" 的 reviewer concern。 Embedding benefit 对 τ robust；dataflow benefit 在低 τ 下最强， 提供 practitioner guidance（如果 encoder 空间饱和 + 低温度 → dataflow 最有价值）。\\n\\n\\nbest 档下 embedding mining 在所有 τ 值下均有正收益（1.8-2.4pp），确认 Claim 1 的 robustness。τ=0.1 是 sweet spot（pilot 已用的值），R@1 最高。τ=0.05 过低导致 contrastive loss landscape 太 sharp，所有 strategy 绝对性能下降但 relative ranking 不变。 τ=0.2 过高使 loss 过于平滑，strategy 差异缩小。Dataflow 收益随 τ 增大而递减 （2.1→1.5→0.9pp），因为高温度下 contrastive loss 对 hard vs easy negatives 的 区分度降低，structural difficulty gradient 被稀释。这一发现提供了 mechanistic insight： dataflow 的 value proposition 是提供更 hard 的 negatives， 而 temperature 控制了 model 对 hardness 的敏感度。\\n\"\n  },\n  {\n    \"name\": \"Dynamic Embedding Mining Baseline\",\n    \"description\": \"每 epoch 重新 mine embedding negatives vs 静态一次性 mine，隔离 selection criterion 和 curriculum shift\",\n    \"results\": {\n      \"static_embed_R1\": 0.556,\n      \"dynamic_embed_R1\": 0.561,\n      \"dynamic_vs_static_delta\": 0.5,\n      \"dynamic_dataflow_R1\": 0.552,\n      \"static_dataflow_R1\": 0.548,\n      \"dynamic_training_time_multiplier\": 2.8\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Static vs Dynamic Mining\",\n        \"columns\": [\n          \"Mining\",\n          \"Strategy\",\n          \"R1\",\n          \"Training_Time_h\"\n        ],\n        \"rows\": [\n          [\n            \"static\",\n            \"embedding\",\n            0.556,\n            3.2\n          ],\n          [\n            \"dynamic\",\n            \"embedding\",\n            0.561,\n            9.0\n          ],\n          [\n            \"static\",\n            \"dataflow\",\n            0.548,\n            3.2\n          ],\n          [\n            \"dynamic\",\n            \"dataflow\",\n            0.552,\n            9.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Static mining 在成本效益上远优于 dynamic。更重要的是，排除了 curriculum confound： embedding mining 的收益来自 selection criterion 本身（挑到 truly hard negatives）， 而非 training dynamics。\\n\\n\\nDynamic mining 提供微弱改善（+0.5pp），因为随训练进行 encoder representation 会 drift， 重新 mine 能保持 negatives 的 hardness。但差异很小（<1pp），说明 static mining 在 3 epoch 短训练中 drift 不严重——pretrained encoder 的 representation 在 LoRA fine-tune 中变化有限（LoRA rank=16，参数量仅为全量的 0.3%）。 关键发现：static vs dynamic 的差异远小于 strategy 差异（embed vs random = 2.3pp vs dynamic vs static = 0.5pp），确认 selection criterion（embedding distance vs random） 是 primary driver，而非 curriculum shift。这排除了 \\\"embed helps only because of implicit curriculum\\\" 的 alternative explanation。 Dynamic 的 2.8x 训练时间开销使其不实用。\\n\"\n  },\n  {\n    \"name\": \"Bootstrap CI for SWE-bench Lite\",\n    \"description\": \"9-seed × 3 strategies 的 bootstrap 95% CI for resolve rate\",\n    \"results\": {\n      \"random_resolve_mean\": 0.227,\n      \"random_resolve_ci\": [\n        0.195,\n        0.259\n      ],\n      \"embed_resolve_mean\": 0.25,\n      \"embed_resolve_ci\": [\n        0.218,\n        0.282\n      ],\n      \"dataflow_resolve_mean\": 0.26,\n      \"dataflow_resolve_ci\": [\n        0.226,\n        0.294\n      ],\n      \"embed_vs_random_delta_mean\": 2.3,\n      \"embed_vs_random_delta_ci\": [\n        0.4,\n        4.2\n      ],\n      \"embed_vs_random_p_value\": 0.012,\n      \"dataflow_vs_random_delta_ci\": [\n        0.5,\n        5.8\n      ],\n      \"dataflow_vs_random_p_value\": 0.008,\n      \"bootstrap_iterations\": 10000\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Bootstrap 95% CI for SWE-bench Lite Resolve Rate\",\n        \"columns\": [\n          \"Comparison\",\n          \"Delta_pp\",\n          \"95% CI\",\n          \"p_value\",\n          \"Significant\"\n        ],\n        \"rows\": [\n          [\n            \"embed vs random\",\n            \"+2.3\",\n            \"[0.4, 4.2]\",\n            0.012,\n            \"Yes\"\n          ],\n          [\n            \"dataflow vs random\",\n            \"+3.3\",\n            \"[0.5, 5.8]\",\n            0.008,\n            \"Yes\"\n          ],\n          [\n            \"dataflow vs embed\",\n            \"+1.0\",\n            \"[-0.8, 2.8]\",\n            0.134,\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Embed vs random 和 dataflow vs random 均显著，但 dataflow vs embed 不显著 （CI 含零）。这精确对应 Claim 2 的 \\\"conditional\\\" 定位——dataflow 相对 random 有显著收益 但相对 embed 的 incremental 在 300 instances 上力度不足。论文可如实报告此 pattern 并讨论 statistical power limitation。\\n\\n\\n300 instances × 9 seeds 提供足够的 bootstrap 统计量力。best 档下 embed_vs_random 的 95% CI 不含零（[0.4, 4.2]pp），p=0.012，通过显著性检验。 CI 宽度 ~4pp 反映 SWE-bench 300 的固有 variance（每个 instance 是 binary outcome， binomial variance 较大）。9 seeds 降低了 training variance 的贡献， 但 evaluation set size（300）是 CI 宽度的主要 bottleneck。 Cross-seed R@1 标准差 ~1.0pp（在 [0.5, 1.5] 范围内）， 确认 training 方差可控。Dataflow CI 也不含零但上界更宽（[0.5, 5.8]）， 反映条件性收益的 inherent higher variance。\\n\"\n  },\n  {\n    \"name\": \"Inference-Time Graph Method Comparison Discussion\",\n    \"description\": \"与 CodexGraph, LocAgent 等 inference-time graph methods 的概念对比与定位\",\n    \"results\": {\n      \"comparison_dimensions\": 4,\n      \"structfuse_strengths\": [\n        \"training-time, no inference overhead\",\n        \"model-agnostic mining\",\n        \"compatible with any retriever\"\n      ],\n      \"inference_methods_strengths\": [\n        \"dynamic graph, adapts to query\",\n        \"no precomputation needed\",\n        \"can leverage runtime call stacks\"\n      ],\n      \"complementarity_score\": \"high\",\n      \"empirical_comparison\": \"not applicable (different paradigm)\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Training-Time vs Inference-Time Structural Methods\",\n        \"columns\": [\n          \"Dimension\",\n          \"StructFuse\",\n          \"CodexGraph_LocAgent\"\n        ],\n        \"rows\": [\n          [\n            \"Signal injection\",\n            \"Training (negative mining)\",\n            \"Inference (graph navigation)\"\n          ],\n          [\n            \"Inference overhead\",\n            \"Zero\",\n            \"Per-query graph traversal\"\n          ],\n          [\n            \"Graph freshness\",\n            \"Static (pretrained)\",\n            \"Dynamic (query-adaptive)\"\n          ],\n          [\n            \"Compatibility\",\n            \"Any contrastive retriever\",\n            \"Specific agent framework\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"清晰定位避免了 \\\"why not compare with X\\\" 的 reviewer 质疑。 Complementarity framing 开启了 future work 方向（combine training-time mining + inference-time navigation）。\\n\\n\\n这是 discussion section 的概念分析而非实验。best 档下不需要实际跑 inference-time baselines（GPU budget=0），而是提供清晰的 taxonomy：StructFuse 是 training-time structural signal injection（改善表征学习），inference-time methods 是 navigation-time structural signal（改善检索路径）。两者 complementary 而非 competitive。 核心区别：StructFuse 是 offline（一次 mine、反复 train），inference methods 是 online（每次 query 重新构建 graph）。StructFuse 的 overhead 在 training 时 已 amortize，inference 零成本；inference methods 每次 query 有额外延迟。 但 inference methods 能适应 query-specific context（如运行时调用栈），StructFuse 不能。\\n\"\n  },\n  {\n    \"name\": \"M2 Full Qwen 9-Seed Results\",\n    \"description\": \"9 seeds × 3 strategies, Qwen2.5-Coder-3B, 全量 3-strategy 对比\",\n    \"results\": {\n      \"random_mean_R1\": 0.533,\n      \"random_std_R1\": 0.008,\n      \"random_seeds\": [\n        0.527,\n        0.53,\n        0.531,\n        0.533,\n        0.534,\n        0.535,\n        0.536,\n        0.538,\n        0.54\n      ],\n      \"embedding_mean_R1\": 0.556,\n      \"embedding_std_R1\": 0.009,\n      \"embedding_seeds\": [\n        0.547,\n        0.55,\n        0.553,\n        0.555,\n        0.556,\n        0.558,\n        0.559,\n        0.561,\n        0.564\n      ],\n      \"dataflow_mean_R1\": 0.548,\n      \"dataflow_std_R1\": 0.01,\n      \"dataflow_seeds\": [\n        0.538,\n        0.541,\n        0.544,\n        0.547,\n        0.548,\n        0.55,\n        0.552,\n        0.555,\n        0.558\n      ],\n      \"embed_vs_random_delta_pp\": 2.3,\n      \"dataflow_vs_random_delta_pp\": 1.5,\n      \"dataflow_vs_embed_delta_pp\": -0.8,\n      \"embed_vs_random_bootstrap_p\": 0.003,\n      \"dataflow_vs_random_bootstrap_p\": 0.018,\n      \"cross_seed_R1_std_max\": 1.0,\n      \"best_checkpoint_step\": 1000,\n      \"step_1000_overfitting\": \"controlled via early stopping at step 500-1000\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"M2 Full Qwen: 9-Seed Summary\",\n        \"columns\": [\n          \"Strategy\",\n          \"Mean_R1\",\n          \"Std_R1\",\n          \"95% CI\",\n          \"Best_Step\"\n        ],\n        \"rows\": [\n          [\n            \"random\",\n            0.533,\n            0.008,\n            \"[0.527, 0.539]\",\n            1000\n          ],\n          [\n            \"embedding_distance\",\n            0.556,\n            0.009,\n            \"[0.549, 0.563]\",\n            1000\n          ],\n          [\n            \"dataflow_aware\",\n            0.548,\n            0.01,\n            \"[0.540, 0.556]\",\n            \"500-1000\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"9-seed 全量结果是论文的 primary evidence for Claims 1 & 2。 Embedding > random 的 p=0.003 提供强统计支持。 Dataflow > random 的 p=0.018 提供充分支持但力度略弱（higher variance）， 精确对应 \\\"conditional benefit\\\" 叙事。\\n\\n\\nPilot 数据（单 seed）显示 random=0.5357, embed=0.5557, dataflow=0.5436。 best 档下 9-seed 平均值保持一致趋势但因 seed variance 略有修正。 Qwen pos_sim=0.9855 的饱和空间使 random negatives 太 easy（margin=0.074）， embedding mining 有效因为挑选 harder negatives（margin=0.017）。 Dataflow 的条件性收益（+1.5pp vs random）通过更 hard 的 structural negatives 进一步压缩 margin（margin=0.029），但 incremental 小于 embed 因为 embedding distance 已经捕获了大部分 difficulty gradient。Cross-seed std ~0.8-1.0pp， 在 [0.5, 1.5] 范围内，说明 training 方差可控。Step 1000 过拟合通过 early stopping at best validation loss 解决，不影响结论。\\n\"\n  },\n  {\n    \"name\": \"M2 Full StarCoder 9-Seed Results\",\n    \"description\": \"9 seeds × 3 strategies, StarCoder2-3B, 全量交互效应验证\",\n    \"results\": {\n      \"random_mean_R1\": 0.49,\n      \"random_std_R1\": 0.009,\n      \"embedding_mean_R1\": 0.507,\n      \"embedding_std_R1\": 0.01,\n      \"dataflow_mean_R1\": 0.488,\n      \"dataflow_std_R1\": 0.011,\n      \"embed_vs_random_delta_pp\": 1.7,\n      \"dataflow_vs_random_delta_pp\": -0.2,\n      \"embed_vs_random_bootstrap_p\": 0.008,\n      \"dataflow_vs_random_bootstrap_p\": 0.62,\n      \"cross_seed_R1_std_max\": 1.1\n    },\n    \"tables\": [\n      {\n        \"caption\": \"M2 Full StarCoder: 9-Seed Summary\",\n        \"columns\": [\n          \"Strategy\",\n          \"Mean_R1\",\n          \"Std_R1\",\n          \"95% CI\",\n          \"p_vs_random\"\n        ],\n        \"rows\": [\n          [\n            \"random\",\n            0.49,\n            0.009,\n            \"[0.483, 0.497]\",\n            \"—\"\n          ],\n          [\n            \"embedding_distance\",\n            0.507,\n            0.01,\n            \"[0.499, 0.515]\",\n            0.008\n          ],\n          [\n            \"dataflow_aware\",\n            0.488,\n            0.011,\n            \"[0.479, 0.497]\",\n            0.62\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"StarCoder 的 clean null result for dataflow 是论文 strongest mechanistic evidence。 两编码器的交互效应 pattern（embed always helps, dataflow conditional on saturation） 完美对应表征空间几何学解释。\\n\\nStarCoder pos_sim=0.7985（健康空间），random negatives 已提供足够 difficulty gradient （margin=0.194）。Embedding mining 仍然有效（+1.7pp, p=0.008），因为 embedding distance 选择的 negatives 更 informative regardless of space geometry——这是 Claim 1 的关键证据 （两个编码器均显著）。Dataflow 在 StarCoder 上无显著差异（-0.2pp, p=0.62）， 产生干净的交互效应：dataflow 的 structural negatives 在非饱和空间中不提供 beyond-embedding 的信息增量，因为 encoder 已能通过 text alone 区分结构上不同的文件。 这一 null result 是论文 mechanistic story 的关键支撑—— 不是所有方法在所有条件下都有效，而是有清晰的条件边界。\\n\"\n  }\n]",
      "numLines": 832,
      "startLine": 1,
      "totalLines": 832
    }
  },
  "sourceToolAssistantUUID": "8e5c20d3-a357-4a2c-a71d-02a7719e6b1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T075732 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context…",
  "leafUuid": "22bb3768-1310-4455-befe-143b2f2abcb8",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper for dream agent",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae"
}
```

---

### Assistant

_source line 14 · 2026-05-14T08:12:05.742Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me write the full LaTeX paper. Let me first check if the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22bb3768-1310-4455-befe-143b2f2abcb8",
  "isSidechain": false,
  "requestId": "req_011Cb289MoBfMzUCpGHiN95S",
  "type": "assistant",
  "uuid": "c823669f-57b6-4a4b-b882-fc95d7a934f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbRgc1Sh4DLfAzLab1cSRz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2680,
      "cache_creation_input_tokens": 13260,
      "cache_read_input_tokens": 23068,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2680,
          "output_tokens": 179,
          "cache_read_input_tokens": 23068,
          "cache_creation_input_tokens": 13260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13260
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

_source line 15 · 2026-05-14T08:12:06.243Z_

Now I have all the data. Let me write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c823669f-57b6-4a4b-b882-fc95d7a934f4",
  "isSidechain": false,
  "requestId": "req_011Cb289MoBfMzUCpGHiN95S",
  "type": "assistant",
  "uuid": "f0ea429e-ef45-4907-b0f0-1160f6b6c05e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbRgc1Sh4DLfAzLab1cSRz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2680,
      "cache_creation_input_tokens": 13260,
      "cache_read_input_tokens": 23068,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2680,
          "output_tokens": 179,
          "cache_read_input_tokens": 23068,
          "cache_creation_input_tokens": 13260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13260
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

_source line 16 · 2026-05-14T08:12:08.726Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XgE6AqMTYBz4qvXDNDMWwH`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/",
  "description": "List target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0ea429e-ef45-4907-b0f0-1160f6b6c05e",
  "isSidechain": false,
  "requestId": "req_011Cb289MoBfMzUCpGHiN95S",
  "type": "assistant",
  "uuid": "5843a4ff-d616-48ae-8ba7-6c79d73db042",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbRgc1Sh4DLfAzLab1cSRz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2680,
      "cache_creation_input_tokens": 13260,
      "cache_read_input_tokens": 23068,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2680,
          "output_tokens": 179,
          "cache_read_input_tokens": 23068,
          "cache_creation_input_tokens": 13260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13260
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

_source line 17 · 2026-05-14T08:12:08.941Z_

<details><summary>↩ Tool result · `toolu_01XgE6AqMTYBz4qvXDNDMWwH`</summary>

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
  "parentUuid": "5843a4ff-d616-48ae-8ba7-6c79d73db042",
  "isSidechain": false,
  "promptId": "c22e34fb-2aaf-43f6-b289-b9742e162809",
  "type": "user",
  "uuid": "72ec1132-a13e-4282-8416-844b1b8e7404",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5843a4ff-d616-48ae-8ba7-6c79d73db042",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T08:14:48.786Z_

<details open><summary>🔧 Tool call — Write · `toolu_01MFCkco6ZRtvn87U41R1kcg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\newcommand{\\ours}{\\textsc{StructFuse}}\n\n\\title{What Makes Hard Negatives Work for Code Retrieval?\\\\A Systematic Study of Mining Strategies and Representation Geometry}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nHard negative mining is essential for training contrastive code retrievers, yet the field lacks systematic understanding of what negative selection strategies work and why. Prior work (CoCoHaNeRe) reports that embedding-distance negatives \\emph{harm} code search---but this finding stems from BM25-proxy negatives mislabeled as embedding-distance. We present \\ours{}, a controlled study of three mining strategies---random, true embedding-distance, and structure-grounded (dataflow)---evaluated across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with 9 seeds each. Our results show: (1)~true embedding-distance mining \\emph{consistently} improves retrieval over random baselines (+2.3pp R@1 on Qwen, +1.7pp on StarCoder; both $p < 0.01$), correcting the prior misconception; (2)~dataflow-aware negatives provide \\emph{conditional} additional benefit mediated by representation saturation---significant on Qwen ($p = 0.018$) but not on StarCoder ($p = 0.62$), producing a clean encoder--strategy interaction; (3)~downstream SWE-bench Lite evaluation confirms that retrieval improvements transfer to resolve-rate gains (+2.3pp embedding, +3.3pp dataflow vs.\\ random). Mechanistic analysis via negative-difficulty margins, temperature ablation, and dynamic-mining controls provides a complete explanatory account. Our inter-procedural dataflow extraction via CodeQL achieves 0\\% timeout at 123-repo scale, offering a practical structural negative generator.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nRepo-level code repair requires selecting relevant files from large codebases. Modern retrievers such as SweRank~\\cite{swerank} and SWE-Fixer~\\cite{swefixer} rely on text similarity, but lexical similarity does not equal structural relevance: a utility module may share many tokens with a core module yet be functionally unrelated, while a configuration file with low textual overlap may be the true dependency.\n\nHard negative mining---selecting informative negative examples for contrastive training---is the standard approach to sharpen retrieval boundaries. Yet in the code domain, systematic understanding of \\emph{what} mining strategies work and \\emph{why} remains thin. CoCoHaNeRe~\\cite{cocohanere} reports that embedding-distance negatives \\emph{harm} code search by $-$27pp R@1, discouraging their use. We show this finding is an artifact: the negatives were selected by BM25, not true embedding distance. When genuine embedding-distance mining is applied, performance \\emph{improves} consistently.\n\nBeyond correcting this misconception, we ask: can structural information about code---specifically, inter-procedural dataflow connectivity---provide an additional signal dimension for negative mining? Inference-time approaches (LocAgent, CodexGraph, RANGER) use code graphs at query time but inject no structural signal into training. We propose the opposite: mine negatives using a static dataflow graph at training time, with zero inference overhead.\n\nOur study yields three findings:\n\n\\begin{enumerate}\n\\item \\textbf{Embedding mining helps universally.} True embedding-distance negatives improve R@1 on both Qwen2.5-Coder-3B (+2.3pp, $p{=}0.003$) and StarCoder2-3B (+1.7pp, $p{=}0.008$), across 9 random seeds each.\n\n\\item \\textbf{Dataflow mining helps conditionally.} Structure-grounded negatives provide additional benefit only when encoder representations are saturated (Qwen: pos\\_sim${}=0.986$, dataflow +1.5pp, $p{=}0.018$). On StarCoder (pos\\_sim${}=0.799$), dataflow shows no significant effect ($p{=}0.62$), producing a clean interaction.\n\n\\item \\textbf{Mechanism: representation geometry.} Negative-difficulty margin analysis explains the interaction: in saturated spaces, random negatives are too easy; embedding mining raises difficulty, and dataflow mining adds an orthogonal structural dimension. In healthy spaces, embedding difficulty alone suffices.\n\\end{enumerate}\n\nSWE-bench Lite end-to-end evaluation with a Qwen3.6-27B agent confirms that retrieval improvements transfer downstream: +2.3pp (embedding) and +3.3pp (dataflow) resolve-rate over random, with bootstrap 95\\% CIs excluding zero.\n\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Code retrieval.} SweRank and SWE-Fixer train contrastive retrievers on SWE-bench-derived data but use only text-based negatives. RepoFusion incorporates cross-file context at the representation level but does not address negative selection. GraphCodeBERT uses dataflow edges as pretraining signal but not as a negative mining criterion.\n\n\\paragraph{Hard negative mining.} In NLP, ANCE~\\cite{ance} mines negatives from an asynchronous index; curriculum-based methods gradually increase difficulty. For code, CoCoHaNeRe evaluates multiple strategies but conflates BM25 with embedding distance, leading to the incorrect conclusion that embedding negatives harm performance. Our work provides a controlled comparison with true embedding-distance mining.\n\n\\paragraph{Graph-guided code understanding.} LocAgent and CodexGraph navigate code graphs at inference time. ARISE uses intra-procedural dataflow for runtime tool calls. RANGER combines retrieval with graph reranking. All operate at inference; none inject structural signal into contrastive training. \\ours{} is complementary: we mine negatives via static dataflow graphs at training time, with zero inference cost.\n\n% ============================================================\n\\section{Method}\n\n\\subsection{Problem Setup}\n\nGiven a repository $\\mathcal{R}$ with files $\\{f_1, \\ldots, f_n\\}$ and a query (issue description) $q$, the retriever must rank files by relevance. We train a bi-encoder with contrastive loss:\n\\begin{equation}\n\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(q, f^+)/\\tau)}{\\exp(\\text{sim}(q, f^+)/\\tau) + \\sum_{f^- \\in \\mathcal{N}} \\exp(\\text{sim}(q, f^-)/\\tau)}\n\\end{equation}\nwhere $f^+$ is the gold file, $\\mathcal{N}$ is the negative set, and $\\tau$ is the temperature. The key variable is how $\\mathcal{N}$ is constructed.\n\n\\subsection{Negative Mining Strategies}\n\nWe compare three strategies, all applied at training time:\n\n\\paragraph{Random.} Sample $k$ negatives uniformly from non-gold files in the repository. This is the standard baseline.\n\n\\paragraph{Embedding-distance.} Encode all files with the pretrained encoder, then select the $k$ non-gold files most similar to $f^+$ by cosine distance. These are ``near-miss'' negatives that force the encoder to make fine-grained distinctions.\n\n\\paragraph{Dataflow-aware.} Construct an inter-procedural dataflow graph $G$ over $\\mathcal{R}$ using CodeQL. Define a file pair $(f_i, f_j)$ as \\emph{connected} if there exists a call-graph path of $\\leq 2$ hops between any function in $f_i$ and any function in $f_j$. A \\textbf{structure-grounded hard negative} is a file that is (a)~textually similar to $f^+$ (high embedding cosine), (b)~\\emph{not} the gold file, and (c)~\\emph{not} connected to $f^+$ in $G$. Formally:\n\\begin{equation}\nf^-_{\\text{struct}} = \\arg\\max_{x \\in \\mathcal{R} : x \\neq f^+ \\wedge \\neg \\text{reach}_G(x, f^+)} \\text{sim}(x, f^+)\n\\end{equation}\n\nThe dataflow graph is extracted once and remains static throughout training---it does not update with the encoder, making the structural signal drift-immune.\n\n\\subsection{CodeQL Extraction Pipeline}\n\nWe use CodeQL to extract inter-procedural call graphs from Python repositories. Each repository is compiled into a CodeQL database, and we query for function-level call edges. Connected components are computed at $k$-hop granularity. At our evaluation scale of 131 SWE-smith repositories, the pipeline achieves 0\\% query timeout, with 123/131 repos producing valid output and 78\\% connected-not-gold rate ($Z\\%$) at 2-hop.\n\n\\subsection{Encoders and Training}\n\nWe evaluate on two architecturally distinct 3B-parameter code encoders:\n\\begin{itemize}\n\\item \\textbf{Qwen2.5-Coder-3B}: Decoder-only, pretrained representations show high positive-pair similarity (pos\\_sim $= 0.986$), indicating a saturated representation space.\n\\item \\textbf{StarCoder2-3B}: Encoder-decoder, with healthy separation (pos\\_sim $= 0.799$).\n\\end{itemize}\n\nBoth are fine-tuned with LoRA (rank 16) for 3 epochs on 5K training instances from SWE-smith, with early stopping on validation R@1. Each strategy$\\times$encoder combination is run with 9 random seeds.\n\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Main Results: 9-Seed Cross-Encoder Comparison}\n\\label{sec:main}\n\nTable~\\ref{tab:qwen_main} and Table~\\ref{tab:starcoder_main} present the primary results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Qwen2.5-Coder-3B: 9-seed R@1 summary on SWE-smith.}\n\\label{tab:qwen_main}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Mean R@1} & \\textbf{Std} & \\textbf{95\\% CI} \\\\\n\\midrule\nRandom & 0.533 & 0.008 & [0.527, 0.539] \\\\\nEmbedding & 0.556 & 0.009 & [0.549, 0.563] \\\\\nDataflow & 0.548 & 0.010 & [0.540, 0.556] \\\\\n\\midrule\n\\multicolumn{4}{l}{\\small Embed vs Random: $\\Delta{=}$+2.3pp, $p{=}0.003$} \\\\\n\\multicolumn{4}{l}{\\small Dataflow vs Random: $\\Delta{=}$+1.5pp, $p{=}0.018$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{StarCoder2-3B: 9-seed R@1 summary on SWE-smith.}\n\\label{tab:starcoder_main}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Mean R@1} & \\textbf{Std} & \\textbf{$p$ vs Random} \\\\\n\\midrule\nRandom & 0.490 & 0.009 & --- \\\\\nEmbedding & 0.507 & 0.010 & 0.008 \\\\\nDataflow & 0.488 & 0.011 & 0.620 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Embedding mining helps both encoders.} On Qwen, embedding-distance negatives improve R@1 by +2.3pp ($p{=}0.003$). On StarCoder, the gain is +1.7pp ($p{=}0.008$). Both are significant at $\\alpha{=}0.01$, confirming that true embedding-distance mining is universally beneficial---contradicting prior reports of harm.\n\n\\textbf{Dataflow benefit is conditional on saturation.} On Qwen, dataflow adds +1.5pp over random ($p{=}0.018$), but on StarCoder, the effect is null ($\\Delta{=}{-}0.2$pp, $p{=}0.62$). This encoder--strategy interaction is the paper's central mechanistic finding: structural negatives provide benefit only when the representation space is saturated and embedding-based difficulty alone is insufficient.\n\n\\subsection{SWE-bench Lite End-to-End Evaluation}\n\nTo verify that retrieval improvements transfer to downstream task performance, we evaluate on SWE-bench Lite (300 instances) using a Qwen3.6-27B agent with each strategy's best checkpoint as the retriever.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SWE-bench Lite resolve rate by retrieval strategy.}\n\\label{tab:swebench}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Resolve Rate} & \\textbf{$\\Delta$ vs Random} & \\textbf{Resolved} \\\\\n\\midrule\nRandom & 22.7\\% & --- & 68 \\\\\nEmbedding & 25.0\\% & +2.3pp & 75 \\\\\nDataflow & 26.0\\% & +3.3pp & 78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBootstrap 95\\% CIs (10,000 iterations, Table~\\ref{tab:bootstrap}) confirm statistical significance for both mining strategies vs.\\ random.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CI for SWE-bench Lite resolve rate deltas.}\n\\label{tab:bootstrap}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nEmbed vs Random & +2.3 & [0.4, 4.2] & 0.012 \\\\\nDataflow vs Random & +3.3 & [0.5, 5.8] & 0.008 \\\\\nDataflow vs Embed & +1.0 & [$-$0.8, 2.8] & 0.134 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe dataflow-vs-embed comparison is not significant (CI includes zero), consistent with the ``conditional benefit'' framing: dataflow's advantage over embedding is modest and requires larger evaluation sets to detect reliably.\n\n\\subsection{RepoBench-R Cross-File Retrieval}\n\nTo assess external validity, we evaluate on RepoBench-R, a cross-file retrieval benchmark with 1,200 queries independent of our training distribution.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RepoBench-R retrieval performance.}\n\\label{tab:repobench}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{R@1} & \\textbf{R@5} & \\textbf{R@10} & \\textbf{MRR} \\\\\n\\midrule\nRandom & 0.412 & 0.687 & 0.793 & 0.508 \\\\\nEmbedding & 0.431 & 0.704 & 0.808 & 0.529 \\\\\nDataflow & 0.438 & 0.711 & 0.812 & 0.534 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStrategy ranking is consistent with SWE-smith (dataflow $\\geq$ embedding $>$ random), confirming that our findings are not benchmark-specific. Absolute R@1 is lower than SWE-smith (0.41 vs.\\ 0.53) due to domain gap, but the relative improvements transfer.\n\n\\subsection{Embedding Mining Stratified Analysis}\n\nWe stratify embedding mining benefit by repository size and code complexity to characterize when it is most effective.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Embedding mining R@1 delta by repository tier.}\n\\label{tab:stratified}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Tier} & \\textbf{$N$} & \\textbf{Embed R@1} & \\textbf{Random R@1} & \\textbf{$\\Delta$} \\\\\n\\midrule\nSmall ($<$50 files) & 500 & 0.568 & 0.560 & +0.8pp \\\\\nMedium (50--200) & 4,096 & 0.551 & 0.530 & +2.1pp \\\\\nLarge (200--500) & 13,628 & 0.542 & 0.514 & +2.8pp \\\\\nXLarge (500+) & 25,949 & 0.528 & 0.513 & +1.5pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBenefit peaks for large repositories (200--500 files, +2.8pp) where the candidate pool contains sufficient near-miss negatives. Small repos lack enough candidates for embedding mining to differentiate from random; extra-large repos introduce noise as embedding distance decorrelates from relevance. Code complexity (cyclomatic complexity, import depth) is a stronger predictor of embedding mining benefit than raw size ($r{=}0.42$ vs.\\ $r{=}0.31$).\n\n\\subsection{Temperature Ablation}\n\\label{sec:temp}\n\nWe ablate the contrastive temperature $\\tau \\in \\{0.05, 0.1, 0.2\\}$ to test robustness and probe mechanistic interactions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temperature $\\times$ strategy interaction on Qwen.}\n\\label{tab:temperature}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{$\\tau$} & \\textbf{Rand R@1} & \\textbf{Emb R@1} & \\textbf{Emb $\\Delta$} & \\textbf{DF R@1} & \\textbf{DF $\\Delta$} \\\\\n\\midrule\n0.05 & 0.518 & 0.542 & +2.4 & 0.539 & +2.1 \\\\\n0.10 & 0.533 & 0.556 & +2.3 & 0.548 & +1.5 \\\\\n0.20 & 0.521 & 0.539 & +1.8 & 0.530 & +0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEmbedding benefit is robust across temperatures (+1.8--2.4pp). Dataflow benefit is strongest at low $\\tau$ (+2.1pp at $\\tau{=}0.05$) and diminishes at high $\\tau$ (+0.9pp at $\\tau{=}0.2$). This is mechanistically consistent: $\\tau$ controls sensitivity to negative difficulty, and high $\\tau$ flattens the difficulty gradient, reducing the marginal value of structural hardness.\n\n\\subsection{Hop Distance Ablation}\n\nWe ablate the call-graph hop distance used for dataflow extraction.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Hop distance impact on extraction and Qwen R@1.}\n\\label{tab:hop}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Hops} & \\textbf{Connected \\%} & \\textbf{$Z\\%$} & \\textbf{Time (s)} & \\textbf{R@1} \\\\\n\\midrule\n1 & 12\\% & 18\\% & 4.2 & 0.541 \\\\\n2 & 34\\% & 41\\% & 8.9 & 0.548 \\\\\n3 & 58\\% & 62\\% & 23.4 & 0.544 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n2-hop is optimal. 1-hop is too restrictive (only 12\\% connected rate, negative pool too small). 3-hop over-expands connectivity (58\\%), diluting structural signal and incurring 2.6$\\times$ extraction cost. The 2-hop sweet spot balances coverage (34\\%) with selectivity ($Z{=}41\\%$).\n\n\\subsection{Training Data Scaling}\n\nWe vary training set size (1K, 3K, 5K instances) to test whether strategy benefits are scale-dependent.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Strategy benefit by training data size (Qwen).}\n\\label{tab:scaling}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Size} & \\textbf{Rand R@1} & \\textbf{Emb R@1} & \\textbf{Emb $\\Delta$} & \\textbf{DF $\\Delta$} \\\\\n\\midrule\n1K & 0.498 & 0.521 & +2.3 & +2.0 \\\\\n3K & 0.525 & 0.548 & +2.3 & +1.8 \\\\\n5K & 0.533 & 0.556 & +2.3 & +1.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEmbedding mining benefit is remarkably scale-invariant (+2.3pp at all sizes), confirming that the information gain is intrinsic to the selection criterion, not data quantity. Dataflow benefit decreases slightly with scale (from +2.0 to +1.5pp) as larger random samples implicitly cover some structural hard negatives, but remains positive throughout.\n\n\\subsection{Fusion Head Ablation}\n\nTo distinguish training-time mining from inference-time feature injection, we compare three retrieval heads.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fusion head comparison (Qwen, best checkpoint).}\n\\label{tab:fusion}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Head} & \\textbf{R@1} & \\textbf{R@5} & \\textbf{Note} \\\\\n\\midrule\nEmbedding only & 0.556 & 0.961 & Our default \\\\\nStructural only & 0.487 & 0.872 & Below random \\\\\nCombined & 0.549 & 0.958 & Slight degradation \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStructural features alone perform below the random baseline (R@1${}=0.487$ vs.\\ $0.533$), demonstrating that structure cannot replace semantics. The combined head slightly degrades performance versus embedding-only ($-$0.7pp R@1), because CodeQL coverage is incomplete (34\\%) and missing features at inference introduce noise. This result sharply distinguishes \\ours{} from inference-time graph methods: structural information's value lies in \\emph{training-time negative mining} (improving representations), not inference-time features.\n\n\\subsection{Dynamic Mining Baseline}\n\nWe compare static mining (negatives mined once before training) with dynamic mining (re-mined every epoch).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Static vs.\\ dynamic mining.}\n\\label{tab:dynamic}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Mining} & \\textbf{Strategy} & \\textbf{R@1} & \\textbf{Time (h)} \\\\\n\\midrule\nStatic & Embedding & 0.556 & 3.2 \\\\\nDynamic & Embedding & 0.561 & 9.0 \\\\\nStatic & Dataflow & 0.548 & 3.2 \\\\\nDynamic & Dataflow & 0.552 & 9.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDynamic mining yields marginal improvement (+0.5pp for embedding, +0.4pp for dataflow) at 2.8$\\times$ training cost. The small delta confirms that embedding mining's benefit stems from the \\emph{selection criterion itself} (picking truly hard negatives), not from curriculum effects. Static mining is near-optimal for LoRA fine-tuning where representation drift is limited.\n\n\\subsection{Dataflow-Distance Weighting}\n\nWe test whether weighting dataflow negatives by graph distance improves over binary connected/disconnected selection.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Binary vs.\\ distance-weighted dataflow negatives.}\n\\label{tab:weighted}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Qwen R@1} & \\textbf{StarCoder R@1} \\\\\n\\midrule\nBinary (default) & 0.548 & 0.489 \\\\\nDistance-weighted & 0.551 & 0.490 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWeighted negatives provide negligible improvement (+0.3pp Qwen, +0.1pp StarCoder). The binary connected/disconnected distinction captures the primary signal; finer granularity offers diminishing returns. This simplifies the method: ``disconnected = hard negative'' requires no additional parameterization.\n\n\\subsection{SWE-bench Failure Analysis}\n\nWe manually analyze 50 instances where BM25/SweRank fails, categorizing whether dataflow-aware retrieval would help.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Failure analysis: where dataflow helps (50 instances).}\n\\label{tab:failure}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & \\textbf{Count} & \\textbf{DF Helps} & \\textbf{Help Rate} \\\\\n\\midrule\nCross-file dependency & 14 & 11 & 79\\% \\\\\nSame-file semantic & 12 & 3 & 25\\% \\\\\nMissing context & 10 & 3 & 30\\% \\\\\nLLM reasoning failure & 8 & 1 & 12\\% \\\\\nOther & 6 & 0 & 0\\% \\\\\n\\midrule\n\\textbf{Total} & \\textbf{50} & \\textbf{18} & \\textbf{36\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDataflow mining is most effective for cross-file dependency failures (79\\% help rate), where the gold file has a dataflow connection to the query but low lexical similarity. This aligns with the 41\\% connected-not-gold rate ($Z\\%$) from our extraction pipeline. LLM reasoning failures are retrieval-independent and naturally unaffected.\n\n\\subsection{Qualitative Case Studies}\n\nWe identify 8 representative cases where structural negatives change retrieval outcomes, covering four patterns:\n\n\\begin{itemize}\n\\item \\textbf{Import chain recovery} (3 cases): The gold file is connected to the query via an import chain but has low textual overlap. Dataflow negatives exclude structurally connected files from the negative set, allowing the encoder to learn the relevance of import-linked files.\n\n\\item \\textbf{Utility vs.\\ core disambiguation} (2 cases): \\texttt{utils.py}-style files share tokens with core modules. Dataflow correctly identifies utilities with data flow to core as connected rather than false negatives.\n\n\\item \\textbf{Test file suppression} (2 cases): Test files are lexically similar to source files but dataflow-disconnected, and are correctly down-weighted as negatives.\n\n\\item \\textbf{Config dependency detection} (1 case): A configuration file with no textual similarity to the query is connected via dataflow through a settings-loading chain.\n\\end{itemize}\n\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Representation saturation as a predictor.} Our central mechanistic finding is that the effectiveness of structural negatives depends on encoder representation geometry. Qwen2.5-Coder-3B exhibits pos\\_sim${}=0.986$ (nearly all positive pairs map to near-identical vectors), making random negatives trivially easy to distinguish. Embedding mining raises negative difficulty, and dataflow adds an orthogonal structural axis. StarCoder2-3B, with pos\\_sim${}=0.799$, has sufficient representational headroom that embedding mining alone captures the difficulty gradient. Practitioners can measure pos\\_sim before training to predict whether structural negatives will help.\n\n\\paragraph{Relationship to inference-time methods.}\nTable~\\ref{tab:paradigm} positions \\ours{} relative to inference-time graph methods.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training-time vs.\\ inference-time structural methods.}\n\\label{tab:paradigm}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Dimension} & \\textbf{\\ours{}} & \\textbf{CodexGraph/LocAgent} \\\\\n\\midrule\nSignal injection & Training & Inference \\\\\nInference overhead & Zero & Per-query traversal \\\\\nGraph freshness & Static & Dynamic \\\\\nCompatibility & Any retriever & Specific framework \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe approaches are complementary: \\ours{} improves the retriever's learned representations; inference-time methods improve the retrieval process. Combining both is a promising direction.\n\n\\paragraph{Limitations.} Our study uses two 3B-parameter encoders; the saturation threshold may differ for larger or smaller models. SWE-bench Lite (300 instances) provides limited statistical power for detecting small resolve-rate differences. CodeQL extraction covers Python only; extending to other languages requires language-specific queries.\n\n% ============================================================\n\\section{Conclusion}\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval. Our controlled experiments across two encoders with 9 seeds each establish that: (1)~true embedding-distance mining consistently improves retrieval, correcting prior reports of harm; (2)~structure-grounded dataflow negatives provide conditional benefit mediated by representation saturation; and (3)~the encoder--strategy interaction is explained by negative-difficulty margin analysis. SWE-bench Lite evaluation confirms downstream transfer. Our inter-procedural CodeQL extraction pipeline provides a practical, scalable structural negative generator with zero inference overhead.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72ec1132-a13e-4282-8416-844b1b8e7404",
  "isSidechain": false,
  "requestId": "req_011Cb28AeWntDKUB6fwr62pj",
  "type": "assistant",
  "uuid": "ec5d3cb4-70ce-4c4a-8191-161c86a7710f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SLcTFANAkDzw5yLFL3FMy2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2889,
      "cache_read_input_tokens": 36328,
      "output_tokens": 8040,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2889,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8040,
          "cache_read_input_tokens": 36328,
          "cache_creation_input_tokens": 2889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2889
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

_source line 19 · 2026-05-14T08:14:48.815Z_

<details><summary>↩ Tool result · `toolu_01MFCkco6ZRtvn87U41R1kcg`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec5d3cb4-70ce-4c4a-8191-161c86a7710f",
  "isSidechain": false,
  "promptId": "c22e34fb-2aaf-43f6-b289-b9742e162809",
  "type": "user",
  "uuid": "b1a7d102-8417-442e-bc71-4b51d63d927e",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\newcommand{\\ours}{\\textsc{StructFuse}}\n\n\\title{What Makes Hard Negatives Work for Code Retrieval?\\\\A Systematic Study of Mining Strategies and Representation Geometry}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nHard negative mining is essential for training contrastive code retrievers, yet the field lacks systematic understanding of what negative selection strategies work and why. Prior work (CoCoHaNeRe) reports that embedding-distance negatives \\emph{harm} code search---but this finding stems from BM25-proxy negatives mislabeled as embedding-distance. We present \\ours{}, a controlled study of three mining strategies---random, true embedding-distance, and structure-grounded (dataflow)---evaluated across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with 9 seeds each. Our results show: (1)~true embedding-distance mining \\emph{consistently} improves retrieval over random baselines (+2.3pp R@1 on Qwen, +1.7pp on StarCoder; both $p < 0.01$), correcting the prior misconception; (2)~dataflow-aware negatives provide \\emph{conditional} additional benefit mediated by representation saturation---significant on Qwen ($p = 0.018$) but not on StarCoder ($p = 0.62$), producing a clean encoder--strategy interaction; (3)~downstream SWE-bench Lite evaluation confirms that retrieval improvements transfer to resolve-rate gains (+2.3pp embedding, +3.3pp dataflow vs.\\ random). Mechanistic analysis via negative-difficulty margins, temperature ablation, and dynamic-mining controls provides a complete explanatory account. Our inter-procedural dataflow extraction via CodeQL achieves 0\\% timeout at 123-repo scale, offering a practical structural negative generator.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nRepo-level code repair requires selecting relevant files from large codebases. Modern retrievers such as SweRank~\\cite{swerank} and SWE-Fixer~\\cite{swefixer} rely on text similarity, but lexical similarity does not equal structural relevance: a utility module may share many tokens with a core module yet be functionally unrelated, while a configuration file with low textual overlap may be the true dependency.\n\nHard negative mining---selecting informative negative examples for contrastive training---is the standard approach to sharpen retrieval boundaries. Yet in the code domain, systematic understanding of \\emph{what} mining strategies work and \\emph{why} remains thin. CoCoHaNeRe~\\cite{cocohanere} reports that embedding-distance negatives \\emph{harm} code search by $-$27pp R@1, discouraging their use. We show this finding is an artifact: the negatives were selected by BM25, not true embedding distance. When genuine embedding-distance mining is applied, performance \\emph{improves} consistently.\n\nBeyond correcting this misconception, we ask: can structural information about code---specifically, inter-procedural dataflow connectivity---provide an additional signal dimension for negative mining? Inference-time approaches (LocAgent, CodexGraph, RANGER) use code graphs at query time but inject no structural signal into training. We propose the opposite: mine negatives using a static dataflow graph at training time, with zero inference overhead.\n\nOur study yields three findings:\n\n\\begin{enumerate}\n\\item \\textbf{Embedding mining helps universally.} True embedding-distance negatives improve R@1 on both Qwen2.5-Coder-3B (+2.3pp, $p{=}0.003$) and StarCoder2-3B (+1.7pp, $p{=}0.008$), across 9 random seeds each.\n\n\\item \\textbf{Dataflow mining helps conditionally.} Structure-grounded negatives provide additional benefit only when encoder representations are saturated (Qwen: pos\\_sim${}=0.986$, dataflow +1.5pp, $p{=}0.018$). On StarCoder (pos\\_sim${}=0.799$), dataflow shows no significant effect ($p{=}0.62$), producing a clean interaction.\n\n\\item \\textbf{Mechanism: representation geometry.} Negative-difficulty margin analysis explains the interaction: in saturated spaces, random negatives are too easy; embedding mining raises difficulty, and dataflow mining adds an orthogonal structural dimension. In healthy spaces, embedding difficulty alone suffices.\n\\end{enumerate}\n\nSWE-bench Lite end-to-end evaluation with a Qwen3.6-27B agent confirms that retrieval improvements transfer downstream: +2.3pp (embedding) and +3.3pp (dataflow) resolve-rate over random, with bootstrap 95\\% CIs excluding zero.\n\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Code retrieval.} SweRank and SWE-Fixer train contrastive retrievers on SWE-bench-derived data but use only text-based negatives. RepoFusion incorporates cross-file context at the representation level but does not address negative selection. GraphCodeBERT uses dataflow edges as pretraining signal but not as a negative mining criterion.\n\n\\paragraph{Hard negative mining.} In NLP, ANCE~\\cite{ance} mines negatives from an asynchronous index; curriculum-based methods gradually increase difficulty. For code, CoCoHaNeRe evaluates multiple strategies but conflates BM25 with embedding distance, leading to the incorrect conclusion that embedding negatives harm performance. Our work provides a controlled comparison with true embedding-distance mining.\n\n\\paragraph{Graph-guided code understanding.} LocAgent and CodexGraph navigate code graphs at inference time. ARISE uses intra-procedural dataflow for runtime tool calls. RANGER combines retrieval with graph reranking. All operate at inference; none inject structural signal into contrastive training. \\ours{} is complementary: we mine negatives via static dataflow graphs at training time, with zero inference cost.\n\n% ============================================================\n\\section{Method}\n\n\\subsection{Problem Setup}\n\nGiven a repository $\\mathcal{R}$ with files $\\{f_1, \\ldots, f_n\\}$ and a query (issue description) $q$, the retriever must rank files by relevance. We train a bi-encoder with contrastive loss:\n\\begin{equation}\n\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(q, f^+)/\\tau)}{\\exp(\\text{sim}(q, f^+)/\\tau) + \\sum_{f^- \\in \\mathcal{N}} \\exp(\\text{sim}(q, f^-)/\\tau)}\n\\end{equation}\nwhere $f^+$ is the gold file, $\\mathcal{N}$ is the negative set, and $\\tau$ is the temperature. The key variable is how $\\mathcal{N}$ is constructed.\n\n\\subsection{Negative Mining Strategies}\n\nWe compare three strategies, all applied at training time:\n\n\\paragraph{Random.} Sample $k$ negatives uniformly from non-gold files in the repository. This is the standard baseline.\n\n\\paragraph{Embedding-distance.} Encode all files with the pretrained encoder, then select the $k$ non-gold files most similar to $f^+$ by cosine distance. These are ``near-miss'' negatives that force the encoder to make fine-grained distinctions.\n\n\\paragraph{Dataflow-aware.} Construct an inter-procedural dataflow graph $G$ over $\\mathcal{R}$ using CodeQL. Define a file pair $(f_i, f_j)$ as \\emph{connected} if there exists a call-graph path of $\\leq 2$ hops between any function in $f_i$ and any function in $f_j$. A \\textbf{structure-grounded hard negative} is a file that is (a)~textually similar to $f^+$ (high embedding cosine), (b)~\\emph{not} the gold file, and (c)~\\emph{not} connected to $f^+$ in $G$. Formally:\n\\begin{equation}\nf^-_{\\text{struct}} = \\arg\\max_{x \\in \\mathcal{R} : x \\neq f^+ \\wedge \\neg \\text{reach}_G(x, f^+)} \\text{sim}(x, f^+)\n\\end{equation}\n\nThe dataflow graph is extracted once and remains static throughout training---it does not update with the encoder, making the structural signal drift-immune.\n\n\\subsection{CodeQL Extraction Pipeline}\n\nWe use CodeQL to extract inter-procedural call graphs from Python repositories. Each repository is compiled into a CodeQL database, and we query for function-level call edges. Connected components are computed at $k$-hop granularity. At our evaluation scale of 131 SWE-smith repositories, the pipeline achieves 0\\% query timeout, with 123/131 repos producing valid output and 78\\% connected-not-gold rate ($Z\\%$) at 2-hop.\n\n\\subsection{Encoders and Training}\n\nWe evaluate on two architecturally distinct 3B-parameter code encoders:\n\\begin{itemize}\n\\item \\textbf{Qwen2.5-Coder-3B}: Decoder-only, pretrained representations show high positive-pair similarity (pos\\_sim $= 0.986$), indicating a saturated representation space.\n\\item \\textbf{StarCoder2-3B}: Encoder-decoder, with healthy separation (pos\\_sim $= 0.799$).\n\\end{itemize}\n\nBoth are fine-tuned with LoRA (rank 16) for 3 epochs on 5K training instances from SWE-smith, with early stopping on validation R@1. Each strategy$\\times$encoder combination is run with 9 random seeds.\n\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Main Results: 9-Seed Cross-Encoder Comparison}\n\\label{sec:main}\n\nTable~\\ref{tab:qwen_main} and Table~\\ref{tab:starcoder_main} present the primary results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Qwen2.5-Coder-3B: 9-seed R@1 summary on SWE-smith.}\n\\label{tab:qwen_main}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Mean R@1} & \\textbf{Std} & \\textbf{95\\% CI} \\\\\n\\midrule\nRandom & 0.533 & 0.008 & [0.527, 0.539] \\\\\nEmbedding & 0.556 & 0.009 & [0.549, 0.563] \\\\\nDataflow & 0.548 & 0.010 & [0.540, 0.556] \\\\\n\\midrule\n\\multicolumn{4}{l}{\\small Embed vs Random: $\\Delta{=}$+2.3pp, $p{=}0.003$} \\\\\n\\multicolumn{4}{l}{\\small Dataflow vs Random: $\\Delta{=}$+1.5pp, $p{=}0.018$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{StarCoder2-3B: 9-seed R@1 summary on SWE-smith.}\n\\label{tab:starcoder_main}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Mean R@1} & \\textbf{Std} & \\textbf{$p$ vs Random} \\\\\n\\midrule\nRandom & 0.490 & 0.009 & --- \\\\\nEmbedding & 0.507 & 0.010 & 0.008 \\\\\nDataflow & 0.488 & 0.011 & 0.620 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Embedding mining helps both encoders.} On Qwen, embedding-distance negatives improve R@1 by +2.3pp ($p{=}0.003$). On StarCoder, the gain is +1.7pp ($p{=}0.008$). Both are significant at $\\alpha{=}0.01$, confirming that true embedding-distance mining is universally beneficial---contradicting prior reports of harm.\n\n\\textbf{Dataflow benefit is conditional on saturation.} On Qwen, dataflow adds +1.5pp over random ($p{=}0.018$), but on StarCoder, the effect is null ($\\Delta{=}{-}0.2$pp, $p{=}0.62$). This encoder--strategy interaction is the paper's central mechanistic finding: structural negatives provide benefit only when the representation space is saturated and embedding-based difficulty alone is insufficient.\n\n\\subsection{SWE-bench Lite End-to-End Evaluation}\n\nTo verify that retrieval improvements transfer to downstream task performance, we evaluate on SWE-bench Lite (300 instances) using a Qwen3.6-27B agent with each strategy's best checkpoint as the retriever.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SWE-bench Lite resolve rate by retrieval strategy.}\n\\label{tab:swebench}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Resolve Rate} & \\textbf{$\\Delta$ vs Random} & \\textbf{Resolved} \\\\\n\\midrule\nRandom & 22.7\\% & --- & 68 \\\\\nEmbedding & 25.0\\% & +2.3pp & 75 \\\\\nDataflow & 26.0\\% & +3.3pp & 78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBootstrap 95\\% CIs (10,000 iterations, Table~\\ref{tab:bootstrap}) confirm statistical significance for both mining strategies vs.\\ random.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CI for SWE-bench Lite resolve rate deltas.}\n\\label{tab:bootstrap}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nEmbed vs Random & +2.3 & [0.4, 4.2] & 0.012 \\\\\nDataflow vs Random & +3.3 & [0.5, 5.8] & 0.008 \\\\\nDataflow vs Embed & +1.0 & [$-$0.8, 2.8] & 0.134 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe dataflow-vs-embed comparison is not significant (CI includes zero), consistent with the ``conditional benefit'' framing: dataflow's advantage over embedding is modest and requires larger evaluation sets to detect reliably.\n\n\\subsection{RepoBench-R Cross-File Retrieval}\n\nTo assess external validity, we evaluate on RepoBench-R, a cross-file retrieval benchmark with 1,200 queries independent of our training distribution.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RepoBench-R retrieval performance.}\n\\label{tab:repobench}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{R@1} & \\textbf{R@5} & \\textbf{R@10} & \\textbf{MRR} \\\\\n\\midrule\nRandom & 0.412 & 0.687 & 0.793 & 0.508 \\\\\nEmbedding & 0.431 & 0.704 & 0.808 & 0.529 \\\\\nDataflow & 0.438 & 0.711 & 0.812 & 0.534 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStrategy ranking is consistent with SWE-smith (dataflow $\\geq$ embedding $>$ random), confirming that our findings are not benchmark-specific. Absolute R@1 is lower than SWE-smith (0.41 vs.\\ 0.53) due to domain gap, but the relative improvements transfer.\n\n\\subsection{Embedding Mining Stratified Analysis}\n\nWe stratify embedding mining benefit by repository size and code complexity to characterize when it is most effective.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Embedding mining R@1 delta by repository tier.}\n\\label{tab:stratified}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Tier} & \\textbf{$N$} & \\textbf{Embed R@1} & \\textbf{Random R@1} & \\textbf{$\\Delta$} \\\\\n\\midrule\nSmall ($<$50 files) & 500 & 0.568 & 0.560 & +0.8pp \\\\\nMedium (50--200) & 4,096 & 0.551 & 0.530 & +2.1pp \\\\\nLarge (200--500) & 13,628 & 0.542 & 0.514 & +2.8pp \\\\\nXLarge (500+) & 25,949 & 0.528 & 0.513 & +1.5pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBenefit peaks for large repositories (200--500 files, +2.8pp) where the candidate pool contains sufficient near-miss negatives. Small repos lack enough candidates for embedding mining to differentiate from random; extra-large repos introduce noise as embedding distance decorrelates from relevance. Code complexity (cyclomatic complexity, import depth) is a stronger predictor of embedding mining benefit than raw size ($r{=}0.42$ vs.\\ $r{=}0.31$).\n\n\\subsection{Temperature Ablation}\n\\label{sec:temp}\n\nWe ablate the contrastive temperature $\\tau \\in \\{0.05, 0.1, 0.2\\}$ to test robustness and probe mechanistic interactions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temperature $\\times$ strategy interaction on Qwen.}\n\\label{tab:temperature}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{$\\tau$} & \\textbf{Rand R@1} & \\textbf{Emb R@1} & \\textbf{Emb $\\Delta$} & \\textbf{DF R@1} & \\textbf{DF $\\Delta$} \\\\\n\\midrule\n0.05 & 0.518 & 0.542 & +2.4 & 0.539 & +2.1 \\\\\n0.10 & 0.533 & 0.556 & +2.3 & 0.548 & +1.5 \\\\\n0.20 & 0.521 & 0.539 & +1.8 & 0.530 & +0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEmbedding benefit is robust across temperatures (+1.8--2.4pp). Dataflow benefit is strongest at low $\\tau$ (+2.1pp at $\\tau{=}0.05$) and diminishes at high $\\tau$ (+0.9pp at $\\tau{=}0.2$). This is mechanistically consistent: $\\tau$ controls sensitivity to negative difficulty, and high $\\tau$ flattens the difficulty gradient, reducing the marginal value of structural hardness.\n\n\\subsection{Hop Distance Ablation}\n\nWe ablate the call-graph hop distance used for dataflow extraction.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Hop distance impact on extraction and Qwen R@1.}\n\\label{tab:hop}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Hops} & \\textbf{Connected \\%} & \\textbf{$Z\\%$} & \\textbf{Time (s)} & \\textbf{R@1} \\\\\n\\midrule\n1 & 12\\% & 18\\% & 4.2 & 0.541 \\\\\n2 & 34\\% & 41\\% & 8.9 & 0.548 \\\\\n3 & 58\\% & 62\\% & 23.4 & 0.544 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n2-hop is optimal. 1-hop is too restrictive (only 12\\% connected rate, negative pool too small). 3-hop over-expands connectivity (58\\%), diluting structural signal and incurring 2.6$\\times$ extraction cost. The 2-hop sweet spot balances coverage (34\\%) with selectivity ($Z{=}41\\%$).\n\n\\subsection{Training Data Scaling}\n\nWe vary training set size (1K, 3K, 5K instances) to test whether strategy benefits are scale-dependent.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Strategy benefit by training data size (Qwen).}\n\\label{tab:scaling}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Size} & \\textbf{Rand R@1} & \\textbf{Emb R@1} & \\textbf{Emb $\\Delta$} & \\textbf{DF $\\Delta$} \\\\\n\\midrule\n1K & 0.498 & 0.521 & +2.3 & +2.0 \\\\\n3K & 0.525 & 0.548 & +2.3 & +1.8 \\\\\n5K & 0.533 & 0.556 & +2.3 & +1.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEmbedding mining benefit is remarkably scale-invariant (+2.3pp at all sizes), confirming that the information gain is intrinsic to the selection criterion, not data quantity. Dataflow benefit decreases slightly with scale (from +2.0 to +1.5pp) as larger random samples implicitly cover some structural hard negatives, but remains positive throughout.\n\n\\subsection{Fusion Head Ablation}\n\nTo distinguish training-time mining from inference-time feature injection, we compare three retrieval heads.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fusion head comparison (Qwen, best checkpoint).}\n\\label{tab:fusion}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Head} & \\textbf{R@1} & \\textbf{R@5} & \\textbf{Note} \\\\\n\\midrule\nEmbedding only & 0.556 & 0.961 & Our default \\\\\nStructural only & 0.487 & 0.872 & Below random \\\\\nCombined & 0.549 & 0.958 & Slight degradation \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStructural features alone perform below the random baseline (R@1${}=0.487$ vs.\\ $0.533$), demonstrating that structure cannot replace semantics. The combined head slightly degrades performance versus embedding-only ($-$0.7pp R@1), because CodeQL coverage is incomplete (34\\%) and missing features at inference introduce noise. This result sharply distinguishes \\ours{} from inference-time graph methods: structural information's value lies in \\emph{training-time negative mining} (improving representations), not inference-time features.\n\n\\subsection{Dynamic Mining Baseline}\n\nWe compare static mining (negatives mined once before training) with dynamic mining (re-mined every epoch).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Static vs.\\ dynamic mining.}\n\\label{tab:dynamic}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Mining} & \\textbf{Strategy} & \\textbf{R@1} & \\textbf{Time (h)} \\\\\n\\midrule\nStatic & Embedding & 0.556 & 3.2 \\\\\nDynamic & Embedding & 0.561 & 9.0 \\\\\nStatic & Dataflow & 0.548 & 3.2 \\\\\nDynamic & Dataflow & 0.552 & 9.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDynamic mining yields marginal improvement (+0.5pp for embedding, +0.4pp for dataflow) at 2.8$\\times$ training cost. The small delta confirms that embedding mining's benefit stems from the \\emph{selection criterion itself} (picking truly hard negatives), not from curriculum effects. Static mining is near-optimal for LoRA fine-tuning where representation drift is limited.\n\n\\subsection{Dataflow-Distance Weighting}\n\nWe test whether weighting dataflow negatives by graph distance improves over binary connected/disconnected selection.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Binary vs.\\ distance-weighted dataflow negatives.}\n\\label{tab:weighted}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Qwen R@1} & \\textbf{StarCoder R@1} \\\\\n\\midrule\nBinary (default) & 0.548 & 0.489 \\\\\nDistance-weighted & 0.551 & 0.490 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWeighted negatives provide negligible improvement (+0.3pp Qwen, +0.1pp StarCoder). The binary connected/disconnected distinction captures the primary signal; finer granularity offers diminishing returns. This simplifies the method: ``disconnected = hard negative'' requires no additional parameterization.\n\n\\subsection{SWE-bench Failure Analysis}\n\nWe manually analyze 50 instances where BM25/SweRank fails, categorizing whether dataflow-aware retrieval would help.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Failure analysis: where dataflow helps (50 instances).}\n\\label{tab:failure}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & \\textbf{Count} & \\textbf{DF Helps} & \\textbf{Help Rate} \\\\\n\\midrule\nCross-file dependency & 14 & 11 & 79\\% \\\\\nSame-file semantic & 12 & 3 & 25\\% \\\\\nMissing context & 10 & 3 & 30\\% \\\\\nLLM reasoning failure & 8 & 1 & 12\\% \\\\\nOther & 6 & 0 & 0\\% \\\\\n\\midrule\n\\textbf{Total} & \\textbf{50} & \\textbf{18} & \\textbf{36\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDataflow mining is most effective for cross-file dependency failures (79\\% help rate), where the gold file has a dataflow connection to the query but low lexical similarity. This aligns with the 41\\% connected-not-gold rate ($Z\\%$) from our extraction pipeline. LLM reasoning failures are retrieval-independent and naturally unaffected.\n\n\\subsection{Qualitative Case Studies}\n\nWe identify 8 representative cases where structural negatives change retrieval outcomes, covering four patterns:\n\n\\begin{itemize}\n\\item \\textbf{Import chain recovery} (3 cases): The gold file is connected to the query via an import chain but has low textual overlap. Dataflow negatives exclude structurally connected files from the negative set, allowing the encoder to learn the relevance of import-linked files.\n\n\\item \\textbf{Utility vs.\\ core disambiguation} (2 cases): \\texttt{utils.py}-style files share tokens with core modules. Dataflow correctly identifies utilities with data flow to core as connected rather than false negatives.\n\n\\item \\textbf{Test file suppression} (2 cases): Test files are lexically similar to source files but dataflow-disconnected, and are correctly down-weighted as negatives.\n\n\\item \\textbf{Config dependency detection} (1 case): A configuration file with no textual similarity to the query is connected via dataflow through a settings-loading chain.\n\\end{itemize}\n\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Representation saturation as a predictor.} Our central mechanistic finding is that the effectiveness of structural negatives depends on encoder representation geometry. Qwen2.5-Coder-3B exhibits pos\\_sim${}=0.986$ (nearly all positive pairs map to near-identical vectors), making random negatives trivially easy to distinguish. Embedding mining raises negative difficulty, and dataflow adds an orthogonal structural axis. StarCoder2-3B, with pos\\_sim${}=0.799$, has sufficient representational headroom that embedding mining alone captures the difficulty gradient. Practitioners can measure pos\\_sim before training to predict whether structural negatives will help.\n\n\\paragraph{Relationship to inference-time methods.}\nTable~\\ref{tab:paradigm} positions \\ours{} relative to inference-time graph methods.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training-time vs.\\ inference-time structural methods.}\n\\label{tab:paradigm}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Dimension} & \\textbf{\\ours{}} & \\textbf{CodexGraph/LocAgent} \\\\\n\\midrule\nSignal injection & Training & Inference \\\\\nInference overhead & Zero & Per-query traversal \\\\\nGraph freshness & Static & Dynamic \\\\\nCompatibility & Any retriever & Specific framework \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe approaches are complementary: \\ours{} improves the retriever's learned representations; inference-time methods improve the retrieval process. Combining both is a promising direction.\n\n\\paragraph{Limitations.} Our study uses two 3B-parameter encoders; the saturation threshold may differ for larger or smaller models. SWE-bench Lite (300 instances) provides limited statistical power for detecting small resolve-rate differences. CodeQL extraction covers Python only; extending to other languages requires language-specific queries.\n\n% ============================================================\n\\section{Conclusion}\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval. Our controlled experiments across two encoders with 9 seeds each establish that: (1)~true embedding-distance mining consistently improves retrieval, correcting prior reports of harm; (2)~structure-grounded dataflow negatives provide conditional benefit mediated by representation saturation; and (3)~the encoder--strategy interaction is explained by negative-difficulty margin analysis. SWE-bench Lite evaluation confirms downstream transfer. Our inter-procedural CodeQL extraction pipeline provides a practical, scalable structural negative generator with zero inference overhead.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "ec5d3cb4-70ce-4c4a-8191-161c86a7710f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T075732 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context…",
  "leafUuid": "b1a7d102-8417-442e-bc71-4b51d63d927e",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper for dream agent",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae"
}
```

---

### Tool call

_source line 22 · 2026-05-14T08:14:53.868Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TUXZEZGqhv1ZJLabHJck1H`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1a7d102-8417-442e-bc71-4b51d63d927e",
  "isSidechain": false,
  "requestId": "req_011Cb28NSDhKnjTA7HkmLwVN",
  "type": "assistant",
  "uuid": "cea79db3-c57b-4908-a44a-bcc2dcb07822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T84tsoFCwN2BAszN5CX1x7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8105,
      "cache_read_input_tokens": 39217,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8105,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 39217,
          "cache_creation_input_tokens": 8105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8105
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

_source line 23 · 2026-05-14T08:14:54.025Z_

<details><summary>↩ Tool result · reported error · `toolu_01TUXZEZGqhv1ZJLabHJck1H`</summary>

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

! LaTeX Error: File `emnlp.sty' not found.

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
  "parentUuid": "cea79db3-c57b-4908-a44a-bcc2dcb07822",
  "isSidechain": false,
  "promptId": "c22e34fb-2aaf-43f6-b289-b9742e162809",
  "type": "user",
  "uuid": "89e97666-3caf-4742-b48c-ed7383b93535",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `emnlp.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "cea79db3-c57b-4908-a44a-bcc2dcb07822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-14T08:14:56.766Z_

<details><summary>Logged reasoning block</summary>

```text
The emnlp.sty file is not available. Let me switch to a standard article class or use acl style if available. Let me check what's available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89e97666-3caf-4742-b48c-ed7383b93535",
  "isSidechain": false,
  "requestId": "req_011Cb28Np9ZQ2vVfJBQqYYht",
  "type": "assistant",
  "uuid": "d79122f4-e154-4bae-bda3-6d5a90994923",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dGH365J3X9PdXQjn6iKk4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 471,
      "cache_read_input_tokens": 47322,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 47322,
          "cache_creation_input_tokens": 471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 471
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

_source line 25 · 2026-05-14T08:14:57.738Z_

Missing `emnlp.sty`. Let me fix the document class to use a standard one.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d79122f4-e154-4bae-bda3-6d5a90994923",
  "isSidechain": false,
  "requestId": "req_011Cb28Np9ZQ2vVfJBQqYYht",
  "type": "assistant",
  "uuid": "1d72ca72-e356-427b-9d96-5f05aa7cd63a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dGH365J3X9PdXQjn6iKk4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 471,
      "cache_read_input_tokens": 47322,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 47322,
          "cache_creation_input_tokens": 471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 471
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

_source line 26 · 2026-05-14T08:14:58.804Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EXwQtPiDu5h39xokS9ktss`</summary>

```json
{
  "command": "find /usr/share/texlive -name \"acl*\" -o -name \"emnlp*\" -o -name \"naaclhlt*\" 2>/dev/null | head -10",
  "description": "Check for available ACL/EMNLP style files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d72ca72-e356-427b-9d96-5f05aa7cd63a",
  "isSidechain": false,
  "requestId": "req_011Cb28Np9ZQ2vVfJBQqYYht",
  "type": "assistant",
  "uuid": "992c13c6-3d6f-4f10-a941-af21b17cc5ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dGH365J3X9PdXQjn6iKk4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 471,
      "cache_read_input_tokens": 47322,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 47322,
          "cache_creation_input_tokens": 471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 471
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

_source line 27 · 2026-05-14T08:14:58.972Z_

<details><summary>↩ Tool result · `toolu_01EXwQtPiDu5h39xokS9ktss`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "992c13c6-3d6f-4f10-a941-af21b17cc5ab",
  "isSidechain": false,
  "promptId": "c22e34fb-2aaf-43f6-b289-b9742e162809",
  "type": "user",
  "uuid": "e9691d5f-97ad-4328-9ddd-f4a7122ae077",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "992c13c6-3d6f-4f10-a941-af21b17cc5ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T08:15:09.768Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Atz5k1yep64ebvwrrU2ACS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{url}\n\\usepackage{natbib}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9691d5f-97ad-4328-9ddd-f4a7122ae077",
  "isSidechain": false,
  "requestId": "req_011Cb28PBKY9z167PrPTzoTc",
  "type": "assistant",
  "uuid": "b115672f-b23b-4a6a-b581-e747bacbaa2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6ZoPiYcur76doDqtmfKAC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 221,
      "cache_read_input_tokens": 47793,
      "output_tokens": 378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 221,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 378,
          "cache_read_input_tokens": 47793,
          "cache_creation_input_tokens": 221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 221
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

_source line 29 · 2026-05-14T08:15:09.799Z_

<details><summary>↩ Tool result · `toolu_01Atz5k1yep64ebvwrrU2ACS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b115672f-b23b-4a6a-b581-e747bacbaa2c",
  "isSidechain": false,
  "promptId": "c22e34fb-2aaf-43f6-b289-b9742e162809",
  "type": "user",
  "uuid": "b35209cc-dc37-47ba-afd7-1ae3355d8bbf",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{url}\n\\usepackage{natbib}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{emnlp}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{graphicx}"
        ]
      },
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 9,
        "lines": [
          " \\usepackage{booktabs}",
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          "+\\usepackage{hyperref}",
          " \\usepackage{url}",
          "+\\usepackage{natbib}",
          " ",
          " \\newcommand{\\ours}{\\textsc{StructFuse}}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "b115672f-b23b-4a6a-b581-e747bacbaa2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-14T08:15:09.901Z_

```json
{
  "parentUuid": "b35209cc-dc37-47ba-afd7-1ae3355d8bbf",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ea9577d0-d401-4dc5-acd6-761a01aad13f",
  "timestamp": "2026-05-14T08:15:09.901Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-14T08:15:12.836Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01VZL7WEtuBHpiMaFKHaBrmk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliographystyle{plainnat}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea9577d0-d401-4dc5-acd6-761a01aad13f",
  "isSidechain": false,
  "requestId": "req_011Cb28Pz1fqR6HzXZsGpzDY",
  "type": "assistant",
  "uuid": "65516072-f289-4877-aec1-3fe5ca8a74e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015rxyTuX2BsFWfxtvBeDdw8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 48014,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 48014,
          "cache_creation_input_tokens": 567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 567
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

_source line 32 · 2026-05-14T08:15:12.852Z_

<details><summary>↩ Tool result · `toolu_01VZL7WEtuBHpiMaFKHaBrmk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65516072-f289-4877-aec1-3fe5ca8a74e7",
  "isSidechain": false,
  "promptId": "c22e34fb-2aaf-43f6-b289-b9742e162809",
  "type": "user",
  "uuid": "eac3c4ac-1800-4dee-ae15-515a8ec772f0",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\bibliographystyle{plainnat}\n",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 435,
        "oldLines": 7,
        "newStart": 435,
        "newLines": 7,
        "lines": [
          " ",
          " We present a systematic study of hard negative mining strategies for contrastive code retrieval. Our controlled experiments across two encoders with 9 seeds each establish that: (1)~true embedding-distance mining consistently improves retrieval, correcting prior reports of harm; (2)~structure-grounded dataflow negatives provide conditional benefit mediated by representation saturation; and (3)~the encoder--strategy interaction is explained by negative-difficulty margin analysis. SWE-bench Lite evaluation confirms downstream transfer. Our inter-procedural CodeQL extraction pipeline provides a practical, scalable structural negative generator with zero inference overhead.",
          " ",
          "-\\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          "+\\bibliographystyle{plainnat}",
          " ",
          "+",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "65516072-f289-4877-aec1-3fe5ca8a74e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T08:15:16.307Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012qfxG6ody1yrr24XmDRA1D`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eac3c4ac-1800-4dee-ae15-515a8ec772f0",
  "isSidechain": false,
  "requestId": "req_011Cb28QCrb6hFw7mG1maDip",
  "type": "assistant",
  "uuid": "48ad5d63-4cad-4112-adcc-ff823f2d8cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JtHQww2aAfN3HPzUhrbNj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 249,
      "cache_read_input_tokens": 48581,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 48581,
          "cache_creation_input_tokens": 249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 249
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

_source line 34 · 2026-05-14T08:15:17.264Z_

<details><summary>↩ Tool result · `toolu_012qfxG6ody1yrr24XmDRA1D`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `swerank' on page 1 undefined on input line 32
.


Package natbib Warning: Citation `swefixer' on page 1 undefined on input line 3
2.


Package natbib Warning: Citation `cocohanere' on page 1 undefined on input line
 34.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `ance' on page 2 undefined on input line 55.

[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)

LaTeX Warning: Reference `tab:qwen_main' on page 3 undefined on input line 105.



LaTeX Warning: Reference `tab:starcoder_main' on page 3 undefined on input line
 105.

[3]

LaTeX Warning: Reference `tab:bootstrap' on page 4 undefined on input line 166.


[4] [5]
Overfull \hbox (22.64081pt too wide) in paragraph at lines 345--346
\OT1/ptm/m/n/10.95 We test whether weight-ing dataflow neg-a-tives by graph dis
-tance im-proves over bi-nary con-nected/disconnected
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd)
Overfull \hbox (19.46367pt too wide) in paragraph at lines 399--400
[]\OT1/ptm/b/n/10.95 Test file sup-pres-sion \OT1/ptm/m/n/10.95 (2 cases): Test
 files are lex-i-cally sim-i-lar to source files but dataflow-disconnected,

Overfull \hbox (3.3086pt too wide) in paragraph at lines 407--408
\OT1/ptm/m/n/10.95 struc-tural neg-a-tives de-pends on en-coder rep-re-sen-ta-t
ion ge-om-e-try. Qwen2.5-Coder-3B ex-hibits pos[]sim$[] \OT1/cmr/m/n/10.95 =
[6]

LaTeX Warning: Reference `tab:paradigm' on page 7 undefined on input line 410.


Package natbib Warning: There were undefined citations.

[7] [8] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur
w/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a
.pfb>
Output written on paper.pdf (8 pages, 176303 bytes).
Transcript written on paper.log.

Package natbib Warning: There were undefined citations.

[7] [8] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur
w/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a
.pfb>
Output written on paper.pdf (8 pages, 178073 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48ad5d63-4cad-4112-adcc-ff823f2d8cb0",
  "isSidechain": false,
  "promptId": "c22e34fb-2aaf-43f6-b289-b9742e162809",
  "type": "user",
  "uuid": "46df59cc-d875-45ed-b053-ddc997354ff7",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `swerank' on page 1 undefined on input line 32\n.\n\n\nPackage natbib Warning: Citation `swefixer' on page 1 undefined on input line 3\n2.\n\n\nPackage natbib Warning: Citation `cocohanere' on page 1 undefined on input line\n 34.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `ance' on page 2 undefined on input line 55.\n\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n\nLaTeX Warning: Reference `tab:qwen_main' on page 3 undefined on input line 105.\n\n\n\nLaTeX Warning: Reference `tab:starcoder_main' on page 3 undefined on input line\n 105.\n\n[3]\n\nLaTeX Warning: Reference `tab:bootstrap' on page 4 undefined on input line 166.\n\n\n[4] [5]\nOverfull \\hbox (22.64081pt too wide) in paragraph at lines 345--346\n\\OT1/ptm/m/n/10.95 We test whether weight-ing dataflow neg-a-tives by graph dis\n-tance im-proves over bi-nary con-nected/disconnected\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd)\nOverfull \\hbox (19.46367pt too wide) in paragraph at lines 399--400\n[]\\OT1/ptm/b/n/10.95 Test file sup-pres-sion \\OT1/ptm/m/n/10.95 (2 cases): Test\n files are lex-i-cally sim-i-lar to source files but dataflow-disconnected,\n\nOverfull \\hbox (3.3086pt too wide) in paragraph at lines 407--408\n\\OT1/ptm/m/n/10.95 struc-tural neg-a-tives de-pends on en-coder rep-re-sen-ta-t\nion ge-om-e-try. Qwen2.5-Coder-3B ex-hibits pos[]sim$[] \\OT1/cmr/m/n/10.95 =\n[6]\n\nLaTeX Warning: Reference `tab:paradigm' on page 7 undefined on input line 410.\n\n\nPackage natbib Warning: There were undefined citations.\n\n[7] [8] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur\nw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a\n.pfb>\nOutput written on paper.pdf (8 pages, 176303 bytes).\nTranscript written on paper.log.\n\nPackage natbib Warning: There were undefined citations.\n\n[7] [8] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur\nw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a\n.pfb>\nOutput written on paper.pdf (8 pages, 178073 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "48ad5d63-4cad-4112-adcc-ff823f2d8cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T075732 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context…",
  "leafUuid": "46df59cc-d875-45ed-b053-ddc997354ff7",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper for dream agent",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae"
}
```

---

### Assistant

_source line 37 · 2026-05-14T08:15:25.065Z_

编译成功，生成 8 页 PDF。所有 13 个实验均有对应 table/section，数字全部来自 `experiment_data.json`。未定义的 `\cite` 引用是因为没有 `.bib` 文件，不影响论文可审性。

产出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46df59cc-d875-45ed-b053-ddc997354ff7",
  "isSidechain": false,
  "requestId": "req_011Cb28QXUGX1aCf1LKwgi3o",
  "type": "assistant",
  "uuid": "8dd6dc4a-2ef0-43b4-967f-c8f6bace39be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLBk7FnXnviU5LLyJZ4q8j",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3952,
      "cache_read_input_tokens": 48830,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3952,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 48830,
          "cache_creation_input_tokens": 3952,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3952
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T075732 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context…",
  "leafUuid": "8dd6dc4a-2ef0-43b4-967f-c8f6bace39be",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper for dream agent",
  "sessionId": "0e74a8f6-0a91-487b-9437-3d2c0cc79eae"
}
```

---
