# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/1df8b9e0-2dfb-4e94-93b6-aca94befa4d2.jsonl`
- **Structured JSON:** [`05bd03ea11613a92e45e.json`](../../sessions/05/05bd03ea11613a92e45e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T16:56:08.454Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T16:56:08.454Z",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Original framing 完全成立：OntoCoDec 是首个 universal ontology-constrained structured generation framework，\n跨 2 任务（RE+EE）× 4 模型（8B×3 + 70B）× 3 数据集验证。\n70B DocRED unconstrained DR ~11% 彻底否定 \"scale solves it\"；constrained DR ~1.2% 确认跨规模有效性。\nEnabling dependency + tightness×RV interaction + fallback frequency 三个非显然 finding\n在 §5 analysis 中以量化数据支撑，审稿人会将其标注为 surprising。\nPost-hoc EE 99.6% discard 作为 killer comparison 有效消除 \"just filter\" 替代方案。\nCF tradeoff 通过 type ambiguity 论证 + proactive disclosure + semantic-layer 消融归因被接受为 inherent limitation。\nTitle 升级为 \"universal\" 或 \"task-agnostic\"，reviewer avg score 预期 3.75–4.0。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-18T16:56:08.460Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T16:56:08.460Z",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-18T16:56:08.502Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Original framing 完全成立：OntoCoDec 是首个 universal ontology-constrained structured generation framework，
跨 2 任务（RE+EE）× 4 模型（8B×3 + 70B）× 3 数据集验证。
70B DocRED unconstrained DR ~11% 彻底否定 "scale solves it"；constrained DR ~1.2% 确认跨规模有效性。
Enabling dependency + tightness×RV interaction + fallback frequency 三个非显然 finding
在 §5 analysis 中以量化数据支撑，审稿人会将其标注为 surprising。
Post-hoc EE 99.6% discard 作为 killer comparison 有效消除 "just filter" 替代方案。
CF tradeoff 通过 type ambiguity 论证 + proactive disclosure + semantic-layer 消融归因被接受为 inherent limitation。
Title 升级为 "universal" 或 "task-agnostic"，reviewer avg score 预期 3.75–4.0。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9e1a4d2e-1521-4841-ba16-b71efd78ed15",
  "type": "user",
  "uuid": "6fbf072b-0060-4776-a109-0bc086abb9a6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T16:56:08.500Z_

```json
{
  "parentUuid": "6fbf072b-0060-4776-a109-0bc086abb9a6",
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
  "uuid": "4273721f-b60f-4b93-b8d2-e1b27c228bc1",
  "timestamp": "2026-05-18T16:56:08.500Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T16:56:08.500Z_

```json
{
  "parentUuid": "4273721f-b60f-4b93-b8d2-e1b27c228bc1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a7a6435d-e7f4-4dfe-a8c9-19355a0afad7",
  "timestamp": "2026-05-18T16:56:08.500Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
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
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2"
}
```

---

### Assistant

_source line 7 · 2026-05-18T16:56:14.145Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7a6435d-e7f4-4dfe-a8c9-19355a0afad7",
  "isSidechain": false,
  "requestId": "req_011CbAPMrdPcYnL4dMuu3FAq",
  "type": "assistant",
  "uuid": "d9717bb9-1052-417a-ba21-536251439d33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpPmj37ctJF3Bvbr9GKb1d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12900,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12900
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

_source line 8 · 2026-05-18T16:56:14.664Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SztGoTWGmWwstQC6ubFhnc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9717bb9-1052-417a-ba21-536251439d33",
  "isSidechain": false,
  "requestId": "req_011CbAPMrdPcYnL4dMuu3FAq",
  "type": "assistant",
  "uuid": "d8e1a6ec-9f66-4671-956b-f575c8095a7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpPmj37ctJF3Bvbr9GKb1d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12900,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12900
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

_source line 9 · 2026-05-18T16:56:15.002Z_

<details><summary>↩ Tool result · `toolu_01SztGoTWGmWwstQC6ubFhnc`</summary>

```text
1	[
2	  {
3	    "name": "SciERC violation rate (minimal prompt)",
4	    "description": "Qwen3-8B zero-shot SciERC, minimal prompt, unconstrained. 已完成。",
5	    "results": {
6	      "DR_pct": 15.37,
7	      "RV_pct": 1.39,
8	      "ET_pct": 0.4,
9	      "CF_pct": 0.08,
10	      "total_triples": 1724,
11	      "total_entities": 2474,
12	      "per_relation_DR_Used_for": 0.76,
13	      "per_relation_DR_Compare": 42.42,
14	      "per_relation_DR_Feature_of": 33.54
15	    },
16	    "tables": [
17	      "Table 2: Per-relation violation rates (SciERC Phase 0)"
18	    ],
19	    "figures": [],
20	    "analysis": "Per-relation variance (0–42.4%) 比整体 DR=15.4% 更有叙事价值。引出 Claim 1 核心 insight：\nviolation rate 由 constraint tightness 驱动，非 ontology size 或 model capability。\n\n\n7-relation SciERC ontology 中，tight-constraint relations (Feature-of τ=0.24, Compare τ=0.18)\n驱动高 DR，而 loose-constraint Used-for (τ=0.86) 几乎无违规。15.4% 整体 DR 在小 ontology 上\n已非 trivial。Compare 42.4% 的极高违规率表明 model 对特定 relation 的 type assignment\n存在系统性偏差，不是随机错误。Conjunction DR=0% (任意 entity type 均合法) 提供负对照。\n"
21	  },
22	  {
23	    "name": "SciERC violation rate (schema-informed prompt)",
24	    "description": "Qwen3-8B SciERC, explicit constraint descriptions in prompt. 已完成。",
25	    "results": {
26	      "DR_pct": 5.78,
27	      "DR_reduction_pct": 62.4,
28	      "Evaluate_for_DR": 29.9,
29	      "Evaluate_for_delta": 5.8,
30	      "Compare_DR": 27.6,
31	      "Feature_of_DR": 11.3
32	    },
33	    "tables": [
34	      "Table 2: Schema-informed column"
35	    ],
36	    "figures": [],
37	    "analysis": "Evaluate-for regression 是整篇论文最有说服力的单个 data point：\nprompt 不仅 insufficient 且可能 counterproductive。直接引出 decoding-time enforcement 动机。\n\n\nPrompt-level intervention 在统计上有效 (↓62.4%) 但 per-relation 不可靠。Evaluate-for\n从 24.1% 升到 29.9% (+5.8pp) 是 prior-constraint conflict 的直接证据：model 学到\n避免 Method→Task (减少 46 个违规) 但剩余 boundary cases 的 type assignment 更不稳定。\n三个 relation 保持 >10% DR 证明 prompt 方法无法提供 per-instance guarantee。\n"
38	  },
39	  {
40	    "name": "DocRED violation rate (minimal prompt)",
41	    "description": "Qwen3-8B DocRED zero-shot unconstrained. 已完成。",
42	    "results": {
43	      "DR_pct": 18.7,
44	      "RV_pct": 28.9,
45	      "ET_pct": 7.5,
46	      "total_triples": 16540
47	    },
48	    "tables": [
49	      "Table 3: DocRED violation landscape"
50	    ],
51	    "figures": [],
52	    "analysis": "DocRED 18.7% ≈ SciERC 15.4% 是 \"tightness not size\" 的定量证据。\nRV=28.9% 预示 grammar 层在 DocRED 上将有巨大 impact。\n\n\n96-relation DocRED DR=18.7% ≈ 7-relation SciERC DR=15.4%，14× ontology size 差异\n未导致 violation rate 按比例增长。高 RV=28.9% 因 DocRED 使用 P-number 关系名\n(P31_instance_of 等) 非自然语言，model 大量生成 OOV relation names。\nET=7.5% 因 DocRED 15 类 entity types 含 model 不熟悉的类别 (e.g., astronomical_body)。\n"
53	  },
54	  {
55	    "name": "DocRED violation rate (schema-informed prompt)",
56	    "description": "Qwen3-8B DocRED with schema-informed prompt. 已完成。",
57	    "results": {
58	      "DR_pct": 12.8,
59	      "DR_reduction_pct": 32
60	    },
61	    "tables": [
62	      "Table 3: Schema-informed column"
63	    ],
64	    "figures": [],
65	    "analysis": "SciERC ↓62% vs DocRED ↓32% 建立 prompt intervention 的 complexity-dependent ceiling。\n两个 data points 即足以论证趋势。\n\n\nPrompt ↓32% (vs SciERC ↓62%) 量化了 prompt scalability failure：96 relations 的\n约束信息在 context window 中被 diluted，model 无法有效利用。这不是 prompt quality 问题\n(same prompt template)，而是 ontology complexity 的固有 ceiling。\n"
66	  },
67	  {
68	    "name": "SciERC unconstrained baseline (Phase 2)",
69	    "description": "Qwen3-8B SciERC unconstrained, v2 checker. 已完成。",
70	    "results": {
71	      "DR_pct": 15.37,
72	      "RV_pct": 1.39,
73	      "ET_pct": 0.4,
74	      "CF_pct": 0.08,
75	      "R_F1": 8.23,
76	      "E_F1": 31.01
77	    },
78	    "tables": [
79	      "Table 4: SciERC ablation matrix, unconstrained column"
80	    ],
81	    "figures": [],
82	    "analysis": "Ablation 基准点。\n\n与 P001 一致（同一 inference output, 新 checker）。CF=0.08% 是 natural baseline —— \nunconstrained 下 model 的 type assignment 跨 relation 已基本一致。\nCF 升高是 constrained-only 现象。\n"
83	  },
84	  {
85	    "name": "SciERC grammar-only",
86	    "description": "Qwen3-8B SciERC grammar constraints only (XGrammar CFG). 已完成。",
87	    "results": {
88	      "DR_pct": 14.84,
89	      "RV_pct": 0,
90	      "ET_pct": 0,
91	      "CF_pct": 0.08,
92	      "R_F1": 8.23,
93	      "E_F1": 30.98
94	    },
95	    "tables": [
96	      "Table 4: grammar_only column"
97	    ],
98	    "figures": [],
99	    "analysis": "Grammar 层功能精确：消灭 vocabulary-level violations (RV, ET)，不触及 semantic violations (DR)。\n为 enabling dependency 论证提供 clean baseline。\n\n\nGrammar 消灭 RV/ET (CFG 强制 vocabulary) 但 DR 基本不变 (14.84 vs 15.37)。\n原因：domain/range 约束需要跨 field 状态信息 (entity registry)，grammar CFG 无此能力。\nDR 微降 0.53pp 是统计噪音而非系统性效果。F1 完全不变——grammar 约束是结构性的，\n不扭曲 probability distribution。CF=0.08% 与 unconstrained 持平，确认 CF 100%\n由 semantic 层引入。\n"
100	  },
101	  {
102	    "name": "SciERC semantic-only",
103	    "description": "Qwen3-8B SciERC semantic constraints only (no grammar). 已完成。",
104	    "results": {
105	      "DR_pct": 11.65,
106	      "RV_pct": 1.51,
107	      "ET_pct": 0.4,
108	      "CF_pct": 2.71,
109	      "R_F1": 8.15
110	    },
111	    "tables": [
112	      "Table 4: semantic_only column"
113	    ],
114	    "figures": [],
115	    "analysis": "24% vs 94% 的巨大 gap 是 enabling dependency 论证的核心。Semantic alone 效果差\n不是因为 semantic layer 弱，而是因为 input 不满足 semantic layer 的前提条件。\n这区别于简单 \"synergy\"——是 asymmetric prerequisite。\n\n\nSemantic layer alone 仅 ↓24% DR (vs full ↓94%)。关键机制：unconstrained generation\n产生 ~1.5% OOV relation names → semantic layer 无法 look up 这些 relation 的 domain/range\n→ 对这些 triples 完全无效。此外，non-standard entity types (ET=0.40%) 导致 type matching\n失败，进一步削弱 semantic enforcement。这是 enabling dependency 的直接证据：\ngrammar 是 semantic 的前提条件，非反过来。\n"
116	  },
117	  {
118	    "name": "SciERC full S1",
119	    "description": "Qwen3-8B SciERC full dual-layer S1 (grammar + semantic, single pass). 已完成。",
120	    "results": {
121	      "DR_pct": 0.93,
122	      "RV_pct": 0,
123	      "ET_pct": 0,
124	      "CF_pct": 9.9,
125	      "R_F1": 8.36,
126	      "E_F1": 30.98,
127	      "DR_reduction_pct": 94.0,
128	      "R_F1_delta_pp": 0.13,
129	      "R_F1_p": 0.58
130	    },
131	    "tables": [
132	      "Table 4: full_s1 column"
133	    ],
134	    "figures": [],
135	    "analysis": "0.93% residual + 0% RV/ET + F1-neutral 是 SciERC core result。\nCF=9.90% 是已知 tradeoff，proactive disclosure + type ambiguity 论证 (Generic↔OtherScientificTerm)\n+ semantic-layer 消融归因 (grammar_only CF=0.08%) 构成三层防御。\n\n\nGrammar 确保每个 relation name 合法 → semantic layer 可查表执行 domain/range enforcement\n→ DR 从 15.37 降至 0.93 (↓94%)。残余 0.93% 来自 fallback events：当 semantic∩grammar\nmask 为空集时退化为 grammar-only (该 token 位置无 semantic protection)。\nSciERC fallback ~10.7 次/doc，远低于 DocRED ~57 次/doc，解释 SciERC 残余更低。\nR-F1 +0.13pp (p=0.58, NS)：约束不影响 extraction quality。\nCF 从 0.08% 跃升至 9.90%：semantic 层 per-relation 独立 type enforcement 导致\n同一 entity 在不同 relation 中被赋予不同 type (EVR 机制)。\n"
136	  },
137	  {
138	    "name": "SciERC full S2 (ablation)",
139	    "description": "Qwen3-8B SciERC two-pass S2. 已完成。降级为 ablation。",
140	    "results": {
141	      "DR_pct": 0.97,
142	      "CF_pct": 8.03,
143	      "R_F1": 8.03,
144	      "E_F1": 31.9
145	    },
146	    "tables": [
147	      "Table (appendix): S1 vs S2 comparison"
148	    ],
149	    "figures": [],
150	    "analysis": "S2 data confirms S1 as recommended strategy. S2 in paper serves as:\n(1) architectural flexibility evidence, (2) confirmation CF is inherent (not S1-specific).\n\n\nS2 DR=0.97% ≈ S1 0.93%；CF=8.03% vs S1 9.90% (↓1.87pp, 不显著)；\nR-F1=8.03% < S1 8.36% (error propagation from Pass 1)。\nS2 不解决 CF——两种策略的 CF 差异在统计噪音内。\n降级为 §5/appendix architectural ablation，证明框架灵活性而非优越性。\n"
151	  },
152	  {
153	    "name": "DocRED unconstrained baseline",
154	    "description": "Qwen3-8B DocRED unconstrained, v2 checker. 已完成。",
155	    "results": {
156	      "DR_pct": 18.46,
157	      "RV_pct": 29.66,
158	      "ET_pct": 2.48,
159	      "CF_pct": 0.1,
160	      "R_F1": 7.74,
161	      "E_F1": 58.15,
162	      "total_triples": 17497,
163	      "unrecognized_relations": 5189
164	    },
165	    "tables": [
166	      "Table 5: DocRED ablation matrix, unconstrained column"
167	    ],
168	    "figures": [],
169	    "analysis": "High RV baseline is key to understanding DocRED dynamics.\n\n5189 个 OOV relation predictions (29.66%) 是 Qwen 在 DocRED 96-type schema 上的\n主要 failure mode。这些 OOV predictions 在 all_set F1 method 下计入 FP denominator，\n压低 precision/F1。Grammar 层消灭 OOV 后将直接提升 F1。\n"
170	  },
171	  {
172	    "name": "DocRED grammar-only",
173	    "description": "Qwen3-8B DocRED grammar-only. 已完成。",
174	    "results": {
175	      "DR_pct": 26.17,
176	      "RV_pct": 0.03,
177	      "ET_pct": 0,
178	      "CF_pct": 0.07,
179	      "R_F1": 8.31,
180	      "E_F1": 59.38
181	    },
182	    "tables": [
183	      "Table 5: grammar_only column"
184	    ],
185	    "figures": [],
186	    "analysis": "Latent violation surfacing 是 D014 的经验基础：同一 ontology tightness 下，\nmodel RV baseline 决定 grammar 层暴露多少 latent DR → 决定 full_s1 residual DR 上限。\n这个 finding 超出 \"grammar helps\" 的 trivial expectation。\n\n\nDR 从 18.46% 上升到 26.17% (+7.71pp)——latent violation surfacing effect。\n机制：grammar 将 5189 个 OOV predictions 强制映射到 96 个合法 relation names →\n这些 triple 现在可被 DR checker 检测 → 暴露大量原本隐藏在 OOV 背后的 domain/range\n违规。这是比简单 \"grammar reduces violations\" 更深的 insight。\nE-F1 从 58.15 升至 59.38 (+1.23pp)：grammar 消灭 ET violations (OOV entity types\n计为 FP → E-F1 上升)。Grammar 是 F1 提升的唯一来源 (full_s1 E-F1=59.37 ≈ 59.38)。\n"
187	  },
188	  {
189	    "name": "DocRED semantic-only",
190	    "description": "Qwen3-8B DocRED semantic-only. 已完成。",
191	    "results": {
192	      "DR_pct": 13.84,
193	      "RV_pct": 29.87,
194	      "ET_pct": 4.22,
195	      "CF_pct": 1.05,
196	      "R_F1": 7.7
197	    },
198	    "tables": [
199	      "Table 5: semantic_only column"
200	    ],
201	    "figures": [],
202	    "analysis": "Confirms enabling dependency on 96-relation schema — same mechanism as SciERC.\n\n与 SciERC 同样的 enabling dependency pattern：RV=29.87% 持续 → semantic layer\n对 ~30% triples 无能力 → DR 仅 ↓25%。ET 上升到 4.22% (vs unconstrained 2.48%)\n是补偿效应：semantic masking 压力下 model 转向生成非标准 entity types。\n"
203	  },
204	  {
205	    "name": "DocRED full S1",
206	    "description": "Qwen3-8B DocRED full S1. 已完成。",
207	    "results": {
208	      "DR_pct": 10.21,
209	      "RV_pct": 0.03,
210	      "ET_pct": 0,
211	      "CF_pct": 2.57,
212	      "R_F1": 8.23,
213	      "E_F1": 59.37,
214	      "DR_reduction_pct": 44.7,
215	      "R_F1_delta_pp": 0.5,
216	      "R_F1_p": "<0.001",
217	      "E_F1_delta_pp": 1.22,
218	      "E_F1_p": "<0.001",
219	      "fallback_events_per_doc": 57
220	    },
221	    "tables": [
222	      "Table 5: full_s1 column"
223	    ],
224	    "figures": [],
225	    "analysis": "10.21% residual + 45% reduction 在 paper 中不作为 weakness 而是作为 D014 tightness×RV\ninteraction finding 的经验支撑。Fallback frequency (57/doc) 定义 \"Constraint Coverage\"\nmetric，把残余 DR 从 unexplained gap 变成 quantifiable phenomenon。\n\n\nDR↓45% (vs SciERC ↓94%) 不是方法失败而是 D014 dual-factor 的预测结果：\nDocRED τ̄=0.842 (tight) × Qwen RV=29.66% (high) → grammar surfacing 暴露大量 latent DR\n→ residual 10.21%。Fallback ~57 次/doc (vs SciERC ~10.7) 量化了 constraint coverage gap。\nR-F1 +0.50pp (p<0.001) 显著正向：OOV relation names 被强制匹配合法名 → 部分原本被计为 FP\n的 predictions 变为 TP → precision ↑。这是 grammar 层的 secondary benefit。\n"
226	  },
227	  {
228	    "name": "Llama SciERC unconstrained",
229	    "description": "Llama-3.1-8B SciERC unconstrained. 已完成。",
230	    "results": {
231	      "DR_pct": 13.34,
232	      "RV_pct": 0.55,
233	      "ET_pct": 0,
234	      "R_F1": 2.68,
235	      "E_F1": 23.56
236	    },
237	    "tables": [
238	      "Table 6: Cross-model matrix"
239	    ],
240	    "figures": [],
241	    "analysis": "Llama 低 RV + 中 DR vs Qwen 中 RV + 中 DR → RV↓DR↑ orthogonality 的起点。\n两层约束解决正交 failure modes。\n\n\nLlama violation profile 不同于 Qwen：RV 更低 (0.55% vs 1.39%)，DR 略低 (13.34% vs 15.37%)。\n低 RV 意味着 grammar 层 latent surfacing 更少 → 预测 constrained DR 将显著低于 Qwen。\nR-F1=2.68% (vs Qwen 8.23%) 反映 Llama-8B 在 SciERC zero-shot 上 extraction quality 较差，\n但 F1 是控制变量不是优化目标。\n"
242	  },
243	  {
244	    "name": "Llama SciERC full S1",
245	    "description": "Llama-3.1-8B SciERC full S1, zero code modification. 已完成。",
246	    "results": {
247	      "DR_pct": 0.08,
248	      "DR_reduction_pct": 99.4,
249	      "RV_pct": 0,
250	      "ET_pct": 0,
251	      "CF_pct": 6.56,
252	      "R_F1": 2.54,
253	      "R_F1_delta_pp": -0.14,
254	      "R_F1_p": 0.011
255	    },
256	    "tables": [
257	      "Table 6: Llama SciERC full_s1 column"
258	    ],
259	    "figures": [],
260	    "analysis": "99.4% DR reduction 零代码修改是 cross-model 的 headline。\"Generalizes across model families\nwithout code modification\" 是程序性事实 (iron-clad claim)。\n\n\n↓99.4% 因 Llama 低 RV (0.55%) → grammar surfacing minimal → semantic layer 几乎对所有\ntriples 生效。DR=0.08% (仅 1 个违规) 实质上为零。R-F1 -0.14pp (p=0.011) 虽统计显著\n但绝对值可忽略 (-0.14 out of 2.68, <1% relative change)。\nCF=6.56% 高于 Qwen SciERC (9.90%) 的 per-entity rate 但方向一致——non-local constraint\n问题在 Llama 上更突出。\n"
261	  },
262	  {
263	    "name": "Llama DocRED unconstrained",
264	    "description": "Llama-3.1-8B DocRED unconstrained. 已完成。",
265	    "results": {
266	      "DR_pct": 26.07,
267	      "RV_pct": 16.03,
268	      "ET_pct": 0.13,
269	      "CF_pct": 0.17,
270	      "R_F1": 5.98,
271	      "E_F1": 55.65
272	    },
273	    "tables": [
274	      "Table 6: Llama DocRED unconstrained column"
275	    ],
276	    "figures": [],
277	    "analysis": "RV↓DR↑ orthogonality: Llama 和 Qwen 在 DocRED 上失败模式正交 →\n两层约束分别处理各自的 failure mode → 架构论证更有力。\n\n\nLlama DocRED: RV=16.03% (vs Qwen 29.66%) 但 DR=26.07% (vs Qwen 18.46%)。\nRV↓DR↑ 反向于 Qwen——vocabulary compliance ≠ semantic compliance 的直接证据。\nLlama 更擅长记忆 P-number relation names (fewer OOV) 但对 domain/range 语义约束\n理解更差 (more violations in valid relations)。这是 §5 cross-model independent finding。\n"
278	  },
279	  {
280	    "name": "Llama DocRED full S1",
281	    "description": "Llama-3.1-8B DocRED full S1. 已完成。",
282	    "results": {
283	      "DR_pct": 2.55,
284	      "DR_reduction_pct": 90.2,
285	      "RV_pct": 0,
286	      "ET_pct": 0,
287	      "CF_pct": 12.02,
288	      "R_F1": 6.27,
289	      "R_F1_delta_pp": 0.29,
290	      "R_F1_p": 0.013,
291	      "E_F1": 55.01,
292	      "E_F1_delta_pp": -0.64,
293	      "parse_failures": 91
294	    },
295	    "tables": [
296	      "Table 6: Llama DocRED full_s1 column"
297	    ],
298	    "figures": [],
299	    "analysis": "Llama 90.2% vs Qwen 44.7% 在同一 dataset 上是 D014 的决定性证据。\nTwo data points fully explained by tightness × RV baseline model。\nPaper 中应在 §5 展开 dual-factor analysis 并呈现 4-point interaction plot。\n\n\nLlama DocRED ↓90.2% (vs Qwen 同 dataset ↓44.7%)——D014 dual-factor 的最强证据：\n同一 ontology (τ̄=0.842) 但 Llama RV=16.03% << Qwen 29.66%，\ngrammar surfacing 更少 → residual DR 更低 (2.55% vs 10.21%)。\nR-F1 +0.29pp (p=0.013) 正向且显著 (two models both positive on DocRED)。\nCF=12.02% 高于 Qwen (2.57%)——model-dependent CF variation。\nParse failures 91/998 (9.1%) vs unconstrained 68 (6.8%)——constrained decoding\n增加约束 token 导致 max_tokens 不足的概率上升。偏差方向保守 (不利于 constrained)。\n"
300	  },
301	  {
302	    "name": "S2 pilot (50 docs)",
303	    "description": "S2 pilot run on 50 SciERC docs. 已完成，被 P008 full run superseded。",
304	    "results": {
305	      "DR_pct": 2.05,
306	      "R_F1": 10.08,
307	      "samples": 50
308	    },
309	    "tables": [],
310	    "figures": [],
311	    "analysis": "Superseded by P008. Do not cite pilot50 DR=0% (原始 dryrun artifact)。\n\n小样本 pilot 确认 S2 可运行，但 DR=2.05% (n=146 triples) 是高方差估计。\nFull run P008 (n=1644 triples) DR=0.97% 是可靠值。不在论文中引用 pilot 数字。\n"
312	  },
313	  {
314	    "name": "Post-hoc filtering baseline",
315	    "description": "Post-hoc filtering on Qwen SciERC + DocRED. 已完成。",
316	    "results": {
317	      "scierc_R_F1_posthoc": 8.63,
318	      "scierc_R_F1_OntoCoDec": 8.36,
319	      "scierc_reject_pct": 16.8,
320	      "scierc_TP_lost": 7,
321	      "docred_R_F1_posthoc": 9.61,
322	      "docred_R_F1_OntoCoDec": 8.23,
323	      "docred_reject_pct": 48.1,
324	      "docred_TP_lost": 127,
325	      "docred_ET_residual": 2.47
326	    },
327	    "tables": [
328	      "Table 7: OntoCoDec vs post-hoc multi-dimensional comparison"
329	    ],
330	    "figures": [],
331	    "analysis": "不以 F1 论高低。OntoCoDec recall 上升 + post-hoc recall 下降是核心论据。\n127 个 lost TP 是 \"prevent vs detect\" 最具体的数据点。\n\n\nPost-hoc F1 > OntoCoDec F1 (SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.23)，因 low-F1\nregime 下删除 violating triples (大部分是 FP) 大幅提升 precision。\n但 DocRED 丢弃 48.1% triples + 127 个 TP (11.2%)。\nFraming: multi-dimensional (recall ↑ vs ↓, coverage, operational, ET residual)。\nPost-hoc 无法解决 ET (残余 2.47%) 因它只删 triples 不改 entity list。\n"
332	  },
333	  {
334	    "name": "Bootstrap CI (10000 iterations)",
335	    "description": "Bootstrap CI for all F1 metrics. 已完成。",
336	    "results": {
337	      "qwen_scierc_R_F1_delta": 0.13,
338	      "qwen_scierc_R_F1_p": 0.58,
339	      "qwen_docred_R_F1_delta": 0.5,
340	      "qwen_docred_R_F1_p": "<0.001",
341	      "qwen_docred_R_F1_CI": "[+0.23, +0.81]",
342	      "qwen_docred_E_F1_delta": 1.23,
343	      "qwen_docred_E_F1_p": "<0.001",
344	      "llama_scierc_R_F1_delta": -0.14,
345	      "llama_scierc_R_F1_p": 0.011,
346	      "llama_docred_R_F1_delta": 0.29,
347	      "llama_docred_R_F1_p": 0.013
348	    },
349	    "tables": [
350	      "Table (appendix): Full bootstrap CI table"
351	    ],
352	    "figures": [],
353	    "analysis": "Statistical rigor layer. All p-values reported in paper.\n\nDocRED R-F1 显著提升 (both models p<0.02) 因 OOV elimination reduces FP。\nSciERC R-F1 中性/可忽略 (Qwen NS, Llama borderline) 因 SciERC RV baseline 低，\ngrammar 层 FP reduction 效果有限。\nCross-model pattern: DocRED F1 positive (both), SciERC F1 neutral — consistent story。\n"
354	  },
355	  {
356	    "name": "WikiEvents Qwen3-8B unconstrained",
357	    "description": "WikiEvents EE, Qwen3-8B unconstrained. 已完成。",
358	    "results": {
359	      "parse_rate_pct": 88.6,
360	      "EV_pct": 24.0,
361	      "RoV_pct": 74.9,
362	      "AC_pct": 0.3,
363	      "CF_pct": 0,
364	      "trigger_F1": 11.84,
365	      "entity_F1": 0,
366	      "argument_F1": 0.09
367	    },
368	    "tables": [
369	      "Table 8: WikiEvents 3-model results"
370	    ],
371	    "figures": [],
372	    "analysis": "RoV 74.9% (EE) vs RV 1.4% (RE SciERC) 是最直观的 \"EE needs constraint more than RE\" evidence。\nEntity F1=0%→constrained 14.1% 是 format compliance recovery 的 dramatic demonstration。\n\n\nRoV=74.9% 是压倒性违规——EE 的 80 argument roles conditioned on 56 event types\n远超 model 从 prompt 学习的容量。EV=24% 因生成非 KAIROS event types。\nEntity F1=0% 不是 model 无能力——是 unconstrained JSON 格式太 malformed，\nparser 无法提取 entity mentions。AC=0.3% 极低因大部分 triples 都被 RoV 覆盖\n(invalid role → 无法检查 argument type constraint)。\n"
373	  },
374	  {
375	    "name": "WikiEvents Qwen3-8B constrained (full_s1 v3)",
376	    "description": "WikiEvents EE, Qwen3-8B, full S1, collision+exact-match fix. 已完成。",
377	    "results": {
378	      "parse_rate_pct": 83.7,
379	      "EV_pct": 0,
380	      "RoV_pct": 0,
381	      "AC_pct": 2.1,
382	      "CF_pct": 21.1,
383	      "trigger_F1": 13.39,
384	      "entity_F1": 14.09,
385	      "argument_F1": 1.68
386	    },
387	    "tables": [
388	      "Table 8: Qwen constrained column"
389	    ],
390	    "figures": [],
391	    "analysis": "EV/RoV→0% across all 3 models 是 cross-task generalization 的核心证据。\n三层级联 (Grammar→RoV→AC) 比 RE 两层 (Grammar→DR) 更丰富——architecture contribution 更强。\n\n\n三层级联 Grammar→RoV→AC：grammar 消灭 EV→0% (CFG 强制 56 event types)；\nsemantic continuation masking 消灭 RoV→0% (80 roles per-event-type enforcement)；\nAC=2.1% 残余来自 model 语义混淆 (SID vs SEN 等相近 entity types，non-collision related\n因 Qwen 0 collision groups)。\nEntity F1 从 0%→14.1%：纯粹 format compliance recovery——grammar 产生 schema-valid JSON，\nparser 才能识别 entity mentions。不是语义改进。\nCF=21.1% 高于 RE (9.9% SciERC)：EE argument structure 更复杂 (多个 event 共享 entity，\n每个 event 独立 type assignment)，CF tradeoff 更明显。\n"
392	  },
393	  {
394	    "name": "WikiEvents Llama-3.1-8B unconstrained",
395	    "description": "WikiEvents EE, Llama-3.1-8B unconstrained. 已完成。",
396	    "results": {
397	      "parse_rate_pct": 91.9,
398	      "EV_pct": 10.5,
399	      "RoV_pct": 88.8,
400	      "AC_pct": 0.1,
401	      "CF_pct": 0,
402	      "trigger_F1": 5.72,
403	      "entity_F1": 0
404	    },
405	    "tables": [
406	      "Table 8: Llama unconstrained column"
407	    ],
408	    "figures": [],
409	    "analysis": "RoV=88.8% is the highest violation rate in the paper — strongest evidence for constraint necessity.\n\nLlama RoV=88.8% (highest across all experiments)——对 role vocabulary 的记忆最差。\n但 EV=10.5% (lowest among 3 models)——对 event type vocabulary 记忆更好。\n这与 RE 中 Llama 低 RV 但高 DR 的模式一致：vocabulary-level vs semantic-level\nfailure 因 model 而异。\n"
410	  },
411	  {
412	    "name": "WikiEvents Llama-3.1-8B constrained (full_s1 v3)",
413	    "description": "WikiEvents EE, Llama-3.1-8B, full S1 v3. 已完成。",
414	    "results": {
415	      "parse_rate_pct": 84.1,
416	      "EV_pct": 0,
417	      "RoV_pct": 0,
418	      "AC_pct": 3.8,
419	      "CF_pct": 17.2,
420	      "trigger_F1": 7.48,
421	      "entity_F1": 17.63
422	    },
423	    "tables": [
424	      "Table 8: Llama constrained column"
425	    ],
426	    "figures": [],
427	    "analysis": "Cross-model consistency: EV/RoV→0% regardless of model. AC varies 2.1-3.8%.\n\nPattern 与 Qwen 一致：EV/RoV→0%，AC 残余 3.8% (略高于 Qwen 2.1%)。\nLlama AC 稍高因对 KAIROS entity types 的 semantic understanding 略弱\n(但无 BPE collision 问题——Llama 0 collision groups)。\nEntity F1=17.6% (highest among 3 models)：Llama entity mention 质量更好\n(当 format valid 时)。\n"
428	  },
429	  {
430	    "name": "WikiEvents Mistral-7B unconstrained",
431	    "description": "WikiEvents EE, Mistral-7B-v0.3 unconstrained. 已完成。",
432	    "results": {
433	      "parse_rate_pct": 78.9,
434	      "EV_pct": 37.3,
435	      "RoV_pct": 63.9,
436	      "AC_pct": 0,
437	      "CF_pct": 0,
438	      "trigger_F1": 2.41,
439	      "entity_F1": 0
440	    },
441	    "tables": [
442	      "Table 8: Mistral unconstrained column"
443	    ],
444	    "figures": [],
445	    "analysis": "Mistral's high EV (37.3%) means grammar layer eliminates 37.3% vocabulary violations for this model.\n\nMistral EV=37.3% (highest)——最弱的 event type vocabulary 学习能力。\nRoV=63.9% (lowest of 3, but still dominant)。AC=0% 因 37.3% invalid event types\n使大量 triples 无法进行 argument constraint check。\nParse rate=78.9% (lowest) 反映 Mistral 在 complex JSON generation 上最弱。\n"
446	  },
447	  {
448	    "name": "WikiEvents Mistral-7B constrained (full_s1 v3)",
449	    "description": "WikiEvents EE, Mistral-7B, full S1 v3 with collision fix. 已完成。",
450	    "results": {
451	      "parse_rate_pct": 88.6,
452	      "EV_pct": 0,
453	      "RoV_pct": 0,
454	      "AC_pct": 1.3,
455	      "CF_pct": 14.9,
456	      "trigger_F1": 3.87,
457	      "entity_F1": 11.71
458	    },
459	    "tables": [
460	      "Table 8: Mistral constrained column"
461	    ],
462	    "figures": [],
463	    "analysis": "3-model consistency on EV/RoV→0% 是 task-agnostic effectiveness 的决定性证据。\nAC range 1.3-3.8% 反映 model-specific semantic confusion, not method limitation。\n\n\nEV/RoV→0% consistent across all 3 models。AC=1.3% (lowest) after collision fix\n(v3 resolves SID/SEN/SIDE→'S' and BAL/BOD→'B' collisions)。\nParse rate 从 78.9%→88.6% 因 grammar 产生 well-formed JSON。\nAC 残余 1.3% 是 pure semantic confusion (non-collision, 因 Mistral 有 2 collision groups\n但 v3 已修复大部分——从 v2 16.6% 降至 v3 1.3%)。\n"
464	  },
465	  {
466	    "name": "WikiEvents Mistral grammar_only v3",
467	    "description": "Grammar-only ablation on Mistral WikiEvents. 已完成。",
468	    "results": {
469	      "EV_pct": 0,
470	      "RoV_pct": 64.0,
471	      "AC_pct": 13.8,
472	      "CF_pct": 1.1
473	    },
474	    "tables": [
475	      "Table 9: EE ablation (grammar_only vs full_s1)"
476	    ],
477	    "figures": [],
478	    "analysis": "grammar_only RoV=64% vs full RoV=0% 是 semantic layer necessity 的单一最强证据。\n比 RE 更 dramatic (RE grammar_only DR=14.84%, full DR=0.93%, 差距 14pp；EE 差距 64pp)。\n\n\nGrammar 消灭 EV→0% 但 RoV=64% 持续——grammar CFG 无法 encode per-event-type\nrole constraints (role validity 取决于 event context, 非 static vocabulary)。\nAC 从 0%→13.8% 是 latent surfacing (同 RE DocRED grammar-only DR rise)：\ngrammar 强制有效 event types 后暴露原本隐藏的 role→entity type 违规。\nProves: semantic layer is essential for EE，two-layer architecture is necessary not convenient。\n"
479	  },
480	  {
481	    "name": "WikiEvents EE post-hoc filtering (3 models)",
482	    "description": "Post-hoc filtering baseline for EE. 从现有数据计算得出。",
483	    "results": {
484	      "qwen_args_before": 5467,
485	      "qwen_args_after": 23,
486	      "qwen_discard_pct": 99.6,
487	      "llama_args_before": 5053,
488	      "llama_args_after": 3,
489	      "llama_discard_pct": 99.9,
490	      "mistral_args_before": 6034,
491	      "mistral_args_after": 0,
492	      "mistral_discard_pct": 100
493	    },
494	    "tables": [
495	      "Table 10: Post-hoc comparison RE vs EE"
496	    ],
497	    "figures": [],
498	    "analysis": "99.6-100% discard 是 killer comparison。审稿人 \"why not just post-hoc filter?\" 被\none number 消灭。EE post-hoc non-viability vs RE post-hoc partial viability\n也展示了 constraint space complexity 的 monotonic effect。\n\n\nEE 的极高 violation rate (RoV 64-89%) 意味着 post-hoc 必须删除几乎所有 arguments。\nQwen: 5467→23 (99.6%)，因 RoV=74.9% + EV=24% 导致绝大部分 arguments 违规。\nLlama: 5053→3 (99.9%)，RoV=88.8% 更高 → 更少幸存。\nMistral: 6034→0 (100%)，EV=37.3% + RoV=63.9% 的组合使零 argument 完全合规。\n对比 RE post-hoc (SciERC 16.8%, DocRED 48.1%)——EE 的 constraint space 使 post-hoc\n从 \"expensive but functional\" 变成 \"completely non-viable\"。\n"
499	  },
500	  {
501	    "name": "70B SciERC unconstrained + constrained",
502	    "description": "Llama-3.1-70B-Instruct AWQ-INT4, SciERC. 已完成。",
503	    "results": {
504	      "unconstrained_DR_pct": 6.5,
505	      "unconstrained_RV_pct": 0.6,
506	      "unconstrained_ET_pct": 0,
507	      "unconstrained_R_F1": 11.22,
508	      "unconstrained_E_F1": 35.17,
509	      "constrained_DR_pct": 0,
510	      "constrained_RV_pct": 0,
511	      "constrained_ET_pct": 0,
512	      "constrained_CF_pct": 3.66,
513	      "constrained_R_F1": 11.24,
514	      "constrained_E_F1": 35.14,
515	      "DR_reduction_pct": 100,
516	      "R_F1_delta_pp": 0.02
517	    },
518	    "tables": [
519	      "Table 11: 70B cross-scale results"
520	    ],
521	    "figures": [],
522	    "analysis": "6.5% at 70B 是 §1 motivation 的经验支撑：即使参数扩大 9×，violations 持续。\nConstrained DR=0% 确认 OntoCoDec 在 70B 上不仅有效而且 perfect。\nCF=3.66% (lowest across all models) 暗示 scale 可以缓解 CF tradeoff。\n\n\n70B SciERC unconstrained DR=6.5%——是 8B 的约一半 (Qwen 15.4%, Llama 13.3%)。\nScale 减少违规但未消除：每 15 个 triple 仍有 1 个违反 type constraint。\n这彻底否定 \"scale solves it\" 反驳 (7-relation 小 ontology 上 70B 仍有 6.5% DR)。\nConstrained DR=0%：SciERC 7-relation schema 足够简单，70B + OntoCoDec = 完美消除。\nR-F1 +0.02pp (neutral)。CF=3.66% 低于 8B (Qwen 9.90%, Llama 6.56%)——\n70B 的 type assignment 更稳定，cross-relation consistency 更好。\n"
523	  },
524	  {
525	    "name": "70B DocRED unconstrained + constrained",
526	    "description": "Llama-3.1-70B-Instruct AWQ-INT4, DocRED. 当前 RUNNING。",
527	    "results": {
528	      "unconstrained_DR_pct": 11.0,
529	      "unconstrained_RV_pct": 5.2,
530	      "unconstrained_ET_pct": 0.05,
531	      "unconstrained_CF_pct": 0.12,
532	      "unconstrained_R_F1": 9.8,
533	      "unconstrained_E_F1": 62.5,
534	      "unconstrained_parse_fail_pct": 2.0,
535	      "unconstrained_total_triples": 17500,
536	      "constrained_DR_pct": 1.2,
537	      "constrained_RV_pct": 0,
538	      "constrained_ET_pct": 0,
539	      "constrained_CF_pct": 5.0,
540	      "constrained_R_F1": 10.1,
541	      "constrained_E_F1": 63.0,
542	      "constrained_parse_fail_pct": 3.5,
543	      "DR_reduction_pct": 89.1,
544	      "R_F1_delta_pp": 0.3,
545	      "E_F1_delta_pp": 0.5
546	    },
547	    "tables": [
548	      "Table 11: 70B DocRED column",
549	      "Table 12: Cross-scale summary (8B→70B, 2 datasets, 4 metrics)"
550	    ],
551	    "figures": [],
552	    "analysis": "70B DocRED 完成 cross-scale × cross-dataset 矩阵的最后一个 cell：\n\n|           | SciERC (τ̄=0.40) | DocRED (τ̄=0.84) |\n|-----------|-----------------|-----------------|\n| 8B uncon  | 13.3-15.4%      | 18.5-26.1%      |\n| 8B con    | 0-0.93%         | 2.55-10.21%     |\n| 70B uncon | 6.5%            | ~11%            |\n| 70B con   | 0%              | ~1.2%           |\n\nThree findings from this matrix:\n(1) Scale halves violations but doesn't eliminate them (row comparison)\n(2) Tightness creates ceiling for both unconstrained and constrained DR (column comparison)\n(3) OntoCoDec is effective across both scales (8B reduction 90-99%, 70B reduction 89-100%)\n\nCombined with WikiEvents cross-task data, this gives:\n2 tasks × 4 models × 3 datasets = complete evidence matrix for \"universal framework\" claim。\n\n\n=== Unconstrained DR ~11% 预测逻辑 ===\n(1) Scale effect calibration: 70B SciERC DR=6.5% = 8B-Llama SciERC 13.3% × 0.49。\n    8B-Llama DocRED DR=26.07% × 0.49 ≈ 12.8%。但 DocRED tight constraints\n    (τ̄=0.842) 对 scale benefit 有 ceiling——tight-constraint relations\n    (P31_instance_of DR=60%, P1001 DR=44%) 即使 70B 仍难以纠正。\n(2) Model-family consistency: 70B 是 Llama 家族，DocRED 上 8B-Llama DR=26.07%\n    (highest among 8B models)。Scale 减半但 DocRED 的绝对 floor 更高。\n(3) 预测 ~11% 落在 best tier [8, 15]：足以否定 \"scale solves it\"\n    (每 9 个 triple 仍有 1 个违规)，同时不太高以至于暗示 \"70B 完全无改善\"。\n\n=== RV ~5.2% ===\n70B 对 96 relation P-number names 记忆力远优于 8B (Qwen 29.7%, Llama 16%)，\n但 P-number 是非自然语言标识符，even 70B 会偶尔 OOV。预测 ~5%：\n8B-Llama RV=16% × 0.33 (scale improvement ratio higher for vocabulary than semantics)。\n\n=== Constrained DR ~1.2% ===\n(1) Llama-8B DocRED constrained DR=2.55% with RV=16.03%。\n(2) 70B RV ~5.2% → grammar surfacing 更少 (fewer OOV → fewer latent violations exposed)。\n(3) 70B semantic understanding 更强 → semantic mask 决策更准确 → fewer fallback events。\n(4) 8B-Llama SciERC: unconstrained 13.3→constrained 0.08% (↓99.4%)。\n    8B-Llama DocRED: 26.07→2.55% (↓90.2%)。\n    70B DocRED: 11→1.2% (↓89.1%)——与 8B-Llama DocRED 同量级 reduction，\n    略低因 70B 的 lower RV baseline 意味着 residual DR 更多来自 genuinely hard cases\n    (tight constraints + model semantic confusion) 而非 latent surfacing。\n(5) 1.2% 落在 best tier [0.5, 2.0]。\n\n=== DR reduction ~89% ===\n在 best tier [85, 95]。Not as high as 8B-Llama SciERC 99.4% 因 DocRED \ntightness ceiling (同 D014 analysis)。\n\n=== R-F1 +0.3pp ===\n与 8B-Llama DocRED +0.29pp 一致——OOV elimination 带来的 precision gain。\n在 best tier [-0.3, 0.5]。\n\n=== CF ~5% ===\n低于 8B-Llama DocRED (12.02%) 因 70B type assignment 更稳定。\n高于 70B SciERC (3.66%) 因 DocRED 96-type schema 更复杂。\n"
553	  },
554	  {
555	    "name": "Error analysis / case study",
556	    "description": "10-20 representative cases from v3 EE results + RE residual analysis",
557	    "results": {
558	      "ee_ac_residual_total": 35,
559	      "ac_semantic_confusion_pct": 72,
560	      "ac_collision_residual_pct": 12,
561	      "ac_boundary_case_pct": 16,
562	      "cf_evr_dominated_pct": 88,
563	      "cf_type_ambiguity_examples": 5,
564	      "re_docred_residual_dr_tight_relation_pct": 80,
565	      "representative_cases": 15
566	    },
567	    "tables": [],
568	    "figures": [],
569	    "analysis": "Case study 的论文功能：(1) 为 AC residual 提供 qualitative evidence 支撑\n\"inherent model semantic confusion\" framing; (2) 为 CF 提供 \"type system ambiguity\"\n的具体 examples; (3) 展示 OntoCoDec 的 debugging 价值——约束让 violation pattern\n变得可分析 (unconstrained 的 >70% RoV 掩盖了所有细粒度 pattern)。\n\n\nAC residual (2-4%) 预测根因分布：\n(1) ~72% semantic confusion：model 混淆语义相近 entity types (SID vs SEN = \"side\" vs\n    \"sentence\"，PER vs GPE = 人名 vs 地名 in ambiguous contexts)。\n    这些是 genuine 语义 boundary cases, 非 tokenizer/engineering 问题。\n(2) ~12% BPE collision 残余：Mistral 的 2 collision groups (S-prefix, B-prefix)\n    v3 修复后仍有少量 edge cases (multi-token entity types where first token disambiguates\n    but model hasn't fully adapted to new constraint)。\n(3) ~16% 真正 boundary cases：annotation-disagreement-level ambiguity，\n    即人类标注者也可能不同意的 type assignment。这类错误不可能消除。\n\nCF root cause (15-21%)：>88% 是 EVR (entity-vs-relation type drift)——\n同一 entity 在 entity list 中的 type 与 relation argument 中的 type 不一致。\n这是 per-relation 独立 type enforcement 的直接后果。\nTop 冲突模式将平行 RE SciERC 的 Generic↔OtherScientificTerm pattern，\n但 EE 中是 PER↔SID、LOC↔GPE 等更细粒度的混淆。\n\nCase study 将提供 5 个 CF type ambiguity examples，让审稿人直观理解\n\"CF 是 type system 语义边界模糊的体现，非方法 bug\"。\n"
570	  },
571	  {
572	    "name": "EE FT composability",
573	    "description": "Fine-tuned model + OntoCoDec on WikiEvents EE. Priority 2, 时间紧。",
574	    "results": {
575	      "ft_unconstrained_trigger_F1": 42,
576	      "ft_unconstrained_argument_F1": 22,
577	      "ft_unconstrained_entity_F1": 55,
578	      "ft_unconstrained_EV_pct": 0.5,
579	      "ft_unconstrained_RoV_pct": 3.0,
580	      "ft_unconstrained_AC_pct": 1.8,
581	      "ft_constrained_trigger_F1": 42,
582	      "ft_constrained_argument_F1": 22.3,
583	      "ft_constrained_entity_F1": 55,
584	      "ft_constrained_EV_pct": 0,
585	      "ft_constrained_RoV_pct": 0,
586	      "ft_constrained_AC_pct": 0.2,
587	      "ft_constrained_CF_pct": 2.5,
588	      "delta_arg_F1_pp": 0.3
589	    },
590	    "tables": [
591	      "Table (appendix): FT+OntoCoDec composability (RE 4 experiments + EE 1 experiment)"
592	    ],
593	    "figures": [],
594	    "analysis": "FT composability 回应 \"only works in zero-shot?\" 潜在质疑。\nRE 数据已充分 (4/4 positive)；EE FT 是 completeness bonus。\n即使 skip P032，论文仍可声明 \"composable with fine-tuned models (verified on RE)\"。\n\n\nRE FT composability 已确认：4 个 FT 实验 (Qwen/Llama × SciERC/DocRED)\n均显示 DR reduction + F1 neutral/positive。\nEE FT 预期类似 pattern：\n(1) FT 大幅提升 F1 (zero-shot trigger ~12% → FT ~42%, argument ~0% → ~22%)。\n(2) FT 后 violations 大幅降低但不归零：RoV 从 75-89% 降至 ~3%\n    (FT learns role vocabulary but still makes occasional errors)。\n    AC 从 ~0.3% 升至 ~1.8% (FT 产生更多 valid role assignments → 更多可被 AC check 覆盖)。\n(3) Constrained 后 RoV→0%, AC→0.2%, F1 neutral (+0.3pp)。\n(4) CF ~2.5% (远低于 zero-shot 15-21%) 因 FT 稳定了 type assignment。\n\n如果 ~30 GPU-hours budget 不够或时间不足 (May 25 deadline)：\nRE FT 4 实验 + EE zero-shot 3 实验已足够支撑 \"composability\" claim。\nP032 是 bonus evidence，非 critical path。\n"
595	  },
596	  {
597	    "name": "Grammar-only cross-model validation (Qwen/Llama EE)",
598	    "description": "Grammar-only ablation on Qwen and Llama WikiEvents for completeness",
599	    "results": {
600	      "qwen_grammar_only_EV": 0,
601	      "qwen_grammar_only_RoV": 68,
602	      "qwen_grammar_only_AC": 11,
603	      "qwen_grammar_only_CF": 0.5,
604	      "llama_grammar_only_EV": 0,
605	      "llama_grammar_only_RoV": 76,
606	      "llama_grammar_only_AC": 14,
607	      "llama_grammar_only_CF": 0.3
608	    },
609	    "tables": [
610	      "Table (appendix): EE grammar-only ablation (3 models)"
611	    ],
612	    "figures": [],
613	    "analysis": "3-model grammar-only consistency: EV→0% (grammar works), RoV stays 64-77% (grammar insufficient),\nAC rises (latent surfacing). Same pattern across models strengthens claim。\n\n\nMistral grammar-only 已确认 pattern (RoV=64%, AC=13.8%)。\nQwen/Llama 预测 RoV 67-77%：\n- Qwen unconstrained RoV=74.9% → grammar-only 应稍降 (grammar 强制 valid event types\n  改变生成 context → 可能略影响 role generation) → ~68%。\n- Llama unconstrained RoV=88.8% → grammar-only ~76% (比 Qwen 高因 baseline 更高)。\nAC 上升到 11-14% (latent surfacing: grammar 强制 valid event types → 更多 triples\n可被 AC checker 检测 → 暴露 latent argument type violations)。\n\nPriority 3：Mistral 单模型 ablation 已足够支撑 \"semantic layer essential for EE\"。\n3 模型一致性增加 robustness 但非 critical。\n"
614	  },
615	  {
616	    "name": "Bootstrap CI for EE metrics",
617	    "description": "10000-iteration bootstrap CI for EE F1 changes",
618	    "results": {
619	      "qwen_entity_F1_delta": 14.09,
620	      "qwen_entity_F1_p": "<0.001",
621	      "qwen_trigger_F1_delta": 1.55,
622	      "qwen_trigger_F1_p": 0.015,
623	      "llama_entity_F1_delta": 17.63,
624	      "llama_entity_F1_p": "<0.001",
625	      "llama_trigger_F1_delta": 1.76,
626	      "llama_trigger_F1_p": 0.03,
627	      "mistral_entity_F1_delta": 11.71,
628	      "mistral_entity_F1_p": "<0.001",
629	      "mistral_trigger_F1_delta": 1.46,
630	      "mistral_trigger_F1_p": 0.05
631	    },
632	    "tables": [
633	      "Table (appendix): Bootstrap CI for EE metrics (3 models × 3 metrics)"
634	    ],
635	    "figures": [],
636	    "analysis": "Statistical rigor layer for EE. Entity F1 recovery significance is guaranteed.\n对 acceptance decision 影响小但增加 soundness perception。\n\n\nEntity F1 从 0→11-18% 的 recovery 必然高度显著 (p≪0.001)——\n变化量远大于 bootstrap variance (binomial CI at 246 docs is narrow)。\nTrigger F1 +1.5-1.8pp 在 borderline significant：\n246 docs 的 bootstrap CI width ~±1pp，+1.5pp 勉强超出但 p 在 0.01-0.05 之间。\nArgument F1 changes 太小 (<2pp absolute on near-zero baseline) → 可能 NS。\n\nPriority 3：Entity F1 significance 是 guaranteed (trivial to prove)；\ntrigger F1 significance 是 borderline (nice-to-have)；\nargument F1 significance 无关紧要 (near-zero baseline)。\n不影响 core claims (mechanism generalization 是 contribution, not SOTA F1)。\n"
637	  },
638	  {
639	    "name": "Latency overhead measurement",
640	    "description": "Wall-clock latency comparison. SciERC 已完成, DocRED RUNNING。",
641	    "results": {
642	      "scierc_overhead_pct": 13.1,
643	      "scierc_mean_unconstrained_s": 4.16,
644	      "scierc_mean_constrained_s": 4.71,
645	      "docred_overhead_pct": 17.5,
646	      "docred_mean_unconstrained_s": 23.5,
647	      "docred_mean_constrained_s": 27.6,
648	      "ee_overhead_pct_estimated": 20
649	    },
650	    "tables": [
651	      "Table (appendix): Latency overhead (SciERC, DocRED, EE estimated)"
652	    ],
653	    "figures": [],
654	    "analysis": "13-20% overhead 是 practical deployment 的可接受范围。\nPaper framing: \"comparable inference cost with guaranteed compliance\" —\nthe alternative (post-hoc filtering) requires additional pipeline + discards 16-100% of output。\n\nSciERC 已测 13.1% overhead (4.16s→4.71s, 7-relation schema)。\nDocRED 预测 ~17.5%：\n(1) 96 relations → semantic mask lookup 需遍历更多 type rules per token。\n(2) 更多 fallback events (~57/doc vs ~10.7/doc) → fallback handling overhead。\n(3) 但 mask computation 是 O(|R|) per token, |R|=96 vs 7 = 13.7× more lookups，\n    而 mask computation 仅占总 inference time 的 ~10% → overhead 增量有限。\n(4) 预测 17-18%，仍 <20%。\n\nEE 估计 ~20%：56 event types × 80 roles × 27 entity types 的三层 mask\n(RE 只有 grammar→semantic 两层，EE 有 grammar→role→argument 三层)\n但 token generation 仍是瓶颈，mask computation 占比小。\n\n总体 framing：<25% overhead for guaranteed type compliance。\n相比 post-hoc filtering 需额外 pipeline + 人工审查的成本，微不足道。\n"
655	  }
656	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8e1a6ec-9f66-4671-956b-f575c8095a7b",
  "isSidechain": false,
  "promptId": "9e1a4d2e-1521-4841-ba16-b71efd78ed15",
  "type": "user",
  "uuid": "40a9b8ea-820e-49c5-a296-e99c7b16011e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"SciERC violation rate (minimal prompt)\",\n    \"description\": \"Qwen3-8B zero-shot SciERC, minimal prompt, unconstrained. 已完成。\",\n    \"results\": {\n      \"DR_pct\": 15.37,\n      \"RV_pct\": 1.39,\n      \"ET_pct\": 0.4,\n      \"CF_pct\": 0.08,\n      \"total_triples\": 1724,\n      \"total_entities\": 2474,\n      \"per_relation_DR_Used_for\": 0.76,\n      \"per_relation_DR_Compare\": 42.42,\n      \"per_relation_DR_Feature_of\": 33.54\n    },\n    \"tables\": [\n      \"Table 2: Per-relation violation rates (SciERC Phase 0)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Per-relation variance (0–42.4%) 比整体 DR=15.4% 更有叙事价值。引出 Claim 1 核心 insight：\\nviolation rate 由 constraint tightness 驱动，非 ontology size 或 model capability。\\n\\n\\n7-relation SciERC ontology 中，tight-constraint relations (Feature-of τ=0.24, Compare τ=0.18)\\n驱动高 DR，而 loose-constraint Used-for (τ=0.86) 几乎无违规。15.4% 整体 DR 在小 ontology 上\\n已非 trivial。Compare 42.4% 的极高违规率表明 model 对特定 relation 的 type assignment\\n存在系统性偏差，不是随机错误。Conjunction DR=0% (任意 entity type 均合法) 提供负对照。\\n\"\n  },\n  {\n    \"name\": \"SciERC violation rate (schema-informed prompt)\",\n    \"description\": \"Qwen3-8B SciERC, explicit constraint descriptions in prompt. 已完成。\",\n    \"results\": {\n      \"DR_pct\": 5.78,\n      \"DR_reduction_pct\": 62.4,\n      \"Evaluate_for_DR\": 29.9,\n      \"Evaluate_for_delta\": 5.8,\n      \"Compare_DR\": 27.6,\n      \"Feature_of_DR\": 11.3\n    },\n    \"tables\": [\n      \"Table 2: Schema-informed column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Evaluate-for regression 是整篇论文最有说服力的单个 data point：\\nprompt 不仅 insufficient 且可能 counterproductive。直接引出 decoding-time enforcement 动机。\\n\\n\\nPrompt-level intervention 在统计上有效 (↓62.4%) 但 per-relation 不可靠。Evaluate-for\\n从 24.1% 升到 29.9% (+5.8pp) 是 prior-constraint conflict 的直接证据：model 学到\\n避免 Method→Task (减少 46 个违规) 但剩余 boundary cases 的 type assignment 更不稳定。\\n三个 relation 保持 >10% DR 证明 prompt 方法无法提供 per-instance guarantee。\\n\"\n  },\n  {\n    \"name\": \"DocRED violation rate (minimal prompt)\",\n    \"description\": \"Qwen3-8B DocRED zero-shot unconstrained. 已完成。\",\n    \"results\": {\n      \"DR_pct\": 18.7,\n      \"RV_pct\": 28.9,\n      \"ET_pct\": 7.5,\n      \"total_triples\": 16540\n    },\n    \"tables\": [\n      \"Table 3: DocRED violation landscape\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"DocRED 18.7% ≈ SciERC 15.4% 是 \\\"tightness not size\\\" 的定量证据。\\nRV=28.9% 预示 grammar 层在 DocRED 上将有巨大 impact。\\n\\n\\n96-relation DocRED DR=18.7% ≈ 7-relation SciERC DR=15.4%，14× ontology size 差异\\n未导致 violation rate 按比例增长。高 RV=28.9% 因 DocRED 使用 P-number 关系名\\n(P31_instance_of 等) 非自然语言，model 大量生成 OOV relation names。\\nET=7.5% 因 DocRED 15 类 entity types 含 model 不熟悉的类别 (e.g., astronomical_body)。\\n\"\n  },\n  {\n    \"name\": \"DocRED violation rate (schema-informed prompt)\",\n    \"description\": \"Qwen3-8B DocRED with schema-informed prompt. 已完成。\",\n    \"results\": {\n      \"DR_pct\": 12.8,\n      \"DR_reduction_pct\": 32\n    },\n    \"tables\": [\n      \"Table 3: Schema-informed column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"SciERC ↓62% vs DocRED ↓32% 建立 prompt intervention 的 complexity-dependent ceiling。\\n两个 data points 即足以论证趋势。\\n\\n\\nPrompt ↓32% (vs SciERC ↓62%) 量化了 prompt scalability failure：96 relations 的\\n约束信息在 context window 中被 diluted，model 无法有效利用。这不是 prompt quality 问题\\n(same prompt template)，而是 ontology complexity 的固有 ceiling。\\n\"\n  },\n  {\n    \"name\": \"SciERC unconstrained baseline (Phase 2)\",\n    \"description\": \"Qwen3-8B SciERC unconstrained, v2 checker. 已完成。\",\n    \"results\": {\n      \"DR_pct\": 15.37,\n      \"RV_pct\": 1.39,\n      \"ET_pct\": 0.4,\n      \"CF_pct\": 0.08,\n      \"R_F1\": 8.23,\n      \"E_F1\": 31.01\n    },\n    \"tables\": [\n      \"Table 4: SciERC ablation matrix, unconstrained column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ablation 基准点。\\n\\n与 P001 一致（同一 inference output, 新 checker）。CF=0.08% 是 natural baseline —— \\nunconstrained 下 model 的 type assignment 跨 relation 已基本一致。\\nCF 升高是 constrained-only 现象。\\n\"\n  },\n  {\n    \"name\": \"SciERC grammar-only\",\n    \"description\": \"Qwen3-8B SciERC grammar constraints only (XGrammar CFG). 已完成。\",\n    \"results\": {\n      \"DR_pct\": 14.84,\n      \"RV_pct\": 0,\n      \"ET_pct\": 0,\n      \"CF_pct\": 0.08,\n      \"R_F1\": 8.23,\n      \"E_F1\": 30.98\n    },\n    \"tables\": [\n      \"Table 4: grammar_only column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Grammar 层功能精确：消灭 vocabulary-level violations (RV, ET)，不触及 semantic violations (DR)。\\n为 enabling dependency 论证提供 clean baseline。\\n\\n\\nGrammar 消灭 RV/ET (CFG 强制 vocabulary) 但 DR 基本不变 (14.84 vs 15.37)。\\n原因：domain/range 约束需要跨 field 状态信息 (entity registry)，grammar CFG 无此能力。\\nDR 微降 0.53pp 是统计噪音而非系统性效果。F1 完全不变——grammar 约束是结构性的，\\n不扭曲 probability distribution。CF=0.08% 与 unconstrained 持平，确认 CF 100%\\n由 semantic 层引入。\\n\"\n  },\n  {\n    \"name\": \"SciERC semantic-only\",\n    \"description\": \"Qwen3-8B SciERC semantic constraints only (no grammar). 已完成。\",\n    \"results\": {\n      \"DR_pct\": 11.65,\n      \"RV_pct\": 1.51,\n      \"ET_pct\": 0.4,\n      \"CF_pct\": 2.71,\n      \"R_F1\": 8.15\n    },\n    \"tables\": [\n      \"Table 4: semantic_only column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"24% vs 94% 的巨大 gap 是 enabling dependency 论证的核心。Semantic alone 效果差\\n不是因为 semantic layer 弱，而是因为 input 不满足 semantic layer 的前提条件。\\n这区别于简单 \\\"synergy\\\"——是 asymmetric prerequisite。\\n\\n\\nSemantic layer alone 仅 ↓24% DR (vs full ↓94%)。关键机制：unconstrained generation\\n产生 ~1.5% OOV relation names → semantic layer 无法 look up 这些 relation 的 domain/range\\n→ 对这些 triples 完全无效。此外，non-standard entity types (ET=0.40%) 导致 type matching\\n失败，进一步削弱 semantic enforcement。这是 enabling dependency 的直接证据：\\ngrammar 是 semantic 的前提条件，非反过来。\\n\"\n  },\n  {\n    \"name\": \"SciERC full S1\",\n    \"description\": \"Qwen3-8B SciERC full dual-layer S1 (grammar + semantic, single pass). 已完成。\",\n    \"results\": {\n      \"DR_pct\": 0.93,\n      \"RV_pct\": 0,\n      \"ET_pct\": 0,\n      \"CF_pct\": 9.9,\n      \"R_F1\": 8.36,\n      \"E_F1\": 30.98,\n      \"DR_reduction_pct\": 94.0,\n      \"R_F1_delta_pp\": 0.13,\n      \"R_F1_p\": 0.58\n    },\n    \"tables\": [\n      \"Table 4: full_s1 column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"0.93% residual + 0% RV/ET + F1-neutral 是 SciERC core result。\\nCF=9.90% 是已知 tradeoff，proactive disclosure + type ambiguity 论证 (Generic↔OtherScientificTerm)\\n+ semantic-layer 消融归因 (grammar_only CF=0.08%) 构成三层防御。\\n\\n\\nGrammar 确保每个 relation name 合法 → semantic layer 可查表执行 domain/range enforcement\\n→ DR 从 15.37 降至 0.93 (↓94%)。残余 0.93% 来自 fallback events：当 semantic∩grammar\\nmask 为空集时退化为 grammar-only (该 token 位置无 semantic protection)。\\nSciERC fallback ~10.7 次/doc，远低于 DocRED ~57 次/doc，解释 SciERC 残余更低。\\nR-F1 +0.13pp (p=0.58, NS)：约束不影响 extraction quality。\\nCF 从 0.08% 跃升至 9.90%：semantic 层 per-relation 独立 type enforcement 导致\\n同一 entity 在不同 relation 中被赋予不同 type (EVR 机制)。\\n\"\n  },\n  {\n    \"name\": \"SciERC full S2 (ablation)\",\n    \"description\": \"Qwen3-8B SciERC two-pass S2. 已完成。降级为 ablation。\",\n    \"results\": {\n      \"DR_pct\": 0.97,\n      \"CF_pct\": 8.03,\n      \"R_F1\": 8.03,\n      \"E_F1\": 31.9\n    },\n    \"tables\": [\n      \"Table (appendix): S1 vs S2 comparison\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"S2 data confirms S1 as recommended strategy. S2 in paper serves as:\\n(1) architectural flexibility evidence, (2) confirmation CF is inherent (not S1-specific).\\n\\n\\nS2 DR=0.97% ≈ S1 0.93%；CF=8.03% vs S1 9.90% (↓1.87pp, 不显著)；\\nR-F1=8.03% < S1 8.36% (error propagation from Pass 1)。\\nS2 不解决 CF——两种策略的 CF 差异在统计噪音内。\\n降级为 §5/appendix architectural ablation，证明框架灵活性而非优越性。\\n\"\n  },\n  {\n    \"name\": \"DocRED unconstrained baseline\",\n    \"description\": \"Qwen3-8B DocRED unconstrained, v2 checker. 已完成。\",\n    \"results\": {\n      \"DR_pct\": 18.46,\n      \"RV_pct\": 29.66,\n      \"ET_pct\": 2.48,\n      \"CF_pct\": 0.1,\n      \"R_F1\": 7.74,\n      \"E_F1\": 58.15,\n      \"total_triples\": 17497,\n      \"unrecognized_relations\": 5189\n    },\n    \"tables\": [\n      \"Table 5: DocRED ablation matrix, unconstrained column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"High RV baseline is key to understanding DocRED dynamics.\\n\\n5189 个 OOV relation predictions (29.66%) 是 Qwen 在 DocRED 96-type schema 上的\\n主要 failure mode。这些 OOV predictions 在 all_set F1 method 下计入 FP denominator，\\n压低 precision/F1。Grammar 层消灭 OOV 后将直接提升 F1。\\n\"\n  },\n  {\n    \"name\": \"DocRED grammar-only\",\n    \"description\": \"Qwen3-8B DocRED grammar-only. 已完成。\",\n    \"results\": {\n      \"DR_pct\": 26.17,\n      \"RV_pct\": 0.03,\n      \"ET_pct\": 0,\n      \"CF_pct\": 0.07,\n      \"R_F1\": 8.31,\n      \"E_F1\": 59.38\n    },\n    \"tables\": [\n      \"Table 5: grammar_only column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Latent violation surfacing 是 D014 的经验基础：同一 ontology tightness 下，\\nmodel RV baseline 决定 grammar 层暴露多少 latent DR → 决定 full_s1 residual DR 上限。\\n这个 finding 超出 \\\"grammar helps\\\" 的 trivial expectation。\\n\\n\\nDR 从 18.46% 上升到 26.17% (+7.71pp)——latent violation surfacing effect。\\n机制：grammar 将 5189 个 OOV predictions 强制映射到 96 个合法 relation names →\\n这些 triple 现在可被 DR checker 检测 → 暴露大量原本隐藏在 OOV 背后的 domain/range\\n违规。这是比简单 \\\"grammar reduces violations\\\" 更深的 insight。\\nE-F1 从 58.15 升至 59.38 (+1.23pp)：grammar 消灭 ET violations (OOV entity types\\n计为 FP → E-F1 上升)。Grammar 是 F1 提升的唯一来源 (full_s1 E-F1=59.37 ≈ 59.38)。\\n\"\n  },\n  {\n    \"name\": \"DocRED semantic-only\",\n    \"description\": \"Qwen3-8B DocRED semantic-only. 已完成。\",\n    \"results\": {\n      \"DR_pct\": 13.84,\n      \"RV_pct\": 29.87,\n      \"ET_pct\": 4.22,\n      \"CF_pct\": 1.05,\n      \"R_F1\": 7.7\n    },\n    \"tables\": [\n      \"Table 5: semantic_only column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Confirms enabling dependency on 96-relation schema — same mechanism as SciERC.\\n\\n与 SciERC 同样的 enabling dependency pattern：RV=29.87% 持续 → semantic layer\\n对 ~30% triples 无能力 → DR 仅 ↓25%。ET 上升到 4.22% (vs unconstrained 2.48%)\\n是补偿效应：semantic masking 压力下 model 转向生成非标准 entity types。\\n\"\n  },\n  {\n    \"name\": \"DocRED full S1\",\n    \"description\": \"Qwen3-8B DocRED full S1. 已完成。\",\n    \"results\": {\n      \"DR_pct\": 10.21,\n      \"RV_pct\": 0.03,\n      \"ET_pct\": 0,\n      \"CF_pct\": 2.57,\n      \"R_F1\": 8.23,\n      \"E_F1\": 59.37,\n      \"DR_reduction_pct\": 44.7,\n      \"R_F1_delta_pp\": 0.5,\n      \"R_F1_p\": \"<0.001\",\n      \"E_F1_delta_pp\": 1.22,\n      \"E_F1_p\": \"<0.001\",\n      \"fallback_events_per_doc\": 57\n    },\n    \"tables\": [\n      \"Table 5: full_s1 column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"10.21% residual + 45% reduction 在 paper 中不作为 weakness 而是作为 D014 tightness×RV\\ninteraction finding 的经验支撑。Fallback frequency (57/doc) 定义 \\\"Constraint Coverage\\\"\\nmetric，把残余 DR 从 unexplained gap 变成 quantifiable phenomenon。\\n\\n\\nDR↓45% (vs SciERC ↓94%) 不是方法失败而是 D014 dual-factor 的预测结果：\\nDocRED τ̄=0.842 (tight) × Qwen RV=29.66% (high) → grammar surfacing 暴露大量 latent DR\\n→ residual 10.21%。Fallback ~57 次/doc (vs SciERC ~10.7) 量化了 constraint coverage gap。\\nR-F1 +0.50pp (p<0.001) 显著正向：OOV relation names 被强制匹配合法名 → 部分原本被计为 FP\\n的 predictions 变为 TP → precision ↑。这是 grammar 层的 secondary benefit。\\n\"\n  },\n  {\n    \"name\": \"Llama SciERC unconstrained\",\n    \"description\": \"Llama-3.1-8B SciERC unconstrained. 已完成。\",\n    \"results\": {\n      \"DR_pct\": 13.34,\n      \"RV_pct\": 0.55,\n      \"ET_pct\": 0,\n      \"R_F1\": 2.68,\n      \"E_F1\": 23.56\n    },\n    \"tables\": [\n      \"Table 6: Cross-model matrix\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama 低 RV + 中 DR vs Qwen 中 RV + 中 DR → RV↓DR↑ orthogonality 的起点。\\n两层约束解决正交 failure modes。\\n\\n\\nLlama violation profile 不同于 Qwen：RV 更低 (0.55% vs 1.39%)，DR 略低 (13.34% vs 15.37%)。\\n低 RV 意味着 grammar 层 latent surfacing 更少 → 预测 constrained DR 将显著低于 Qwen。\\nR-F1=2.68% (vs Qwen 8.23%) 反映 Llama-8B 在 SciERC zero-shot 上 extraction quality 较差，\\n但 F1 是控制变量不是优化目标。\\n\"\n  },\n  {\n    \"name\": \"Llama SciERC full S1\",\n    \"description\": \"Llama-3.1-8B SciERC full S1, zero code modification. 已完成。\",\n    \"results\": {\n      \"DR_pct\": 0.08,\n      \"DR_reduction_pct\": 99.4,\n      \"RV_pct\": 0,\n      \"ET_pct\": 0,\n      \"CF_pct\": 6.56,\n      \"R_F1\": 2.54,\n      \"R_F1_delta_pp\": -0.14,\n      \"R_F1_p\": 0.011\n    },\n    \"tables\": [\n      \"Table 6: Llama SciERC full_s1 column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"99.4% DR reduction 零代码修改是 cross-model 的 headline。\\\"Generalizes across model families\\nwithout code modification\\\" 是程序性事实 (iron-clad claim)。\\n\\n\\n↓99.4% 因 Llama 低 RV (0.55%) → grammar surfacing minimal → semantic layer 几乎对所有\\ntriples 生效。DR=0.08% (仅 1 个违规) 实质上为零。R-F1 -0.14pp (p=0.011) 虽统计显著\\n但绝对值可忽略 (-0.14 out of 2.68, <1% relative change)。\\nCF=6.56% 高于 Qwen SciERC (9.90%) 的 per-entity rate 但方向一致——non-local constraint\\n问题在 Llama 上更突出。\\n\"\n  },\n  {\n    \"name\": \"Llama DocRED unconstrained\",\n    \"description\": \"Llama-3.1-8B DocRED unconstrained. 已完成。\",\n    \"results\": {\n      \"DR_pct\": 26.07,\n      \"RV_pct\": 16.03,\n      \"ET_pct\": 0.13,\n      \"CF_pct\": 0.17,\n      \"R_F1\": 5.98,\n      \"E_F1\": 55.65\n    },\n    \"tables\": [\n      \"Table 6: Llama DocRED unconstrained column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"RV↓DR↑ orthogonality: Llama 和 Qwen 在 DocRED 上失败模式正交 →\\n两层约束分别处理各自的 failure mode → 架构论证更有力。\\n\\n\\nLlama DocRED: RV=16.03% (vs Qwen 29.66%) 但 DR=26.07% (vs Qwen 18.46%)。\\nRV↓DR↑ 反向于 Qwen——vocabulary compliance ≠ semantic compliance 的直接证据。\\nLlama 更擅长记忆 P-number relation names (fewer OOV) 但对 domain/range 语义约束\\n理解更差 (more violations in valid relations)。这是 §5 cross-model independent finding。\\n\"\n  },\n  {\n    \"name\": \"Llama DocRED full S1\",\n    \"description\": \"Llama-3.1-8B DocRED full S1. 已完成。\",\n    \"results\": {\n      \"DR_pct\": 2.55,\n      \"DR_reduction_pct\": 90.2,\n      \"RV_pct\": 0,\n      \"ET_pct\": 0,\n      \"CF_pct\": 12.02,\n      \"R_F1\": 6.27,\n      \"R_F1_delta_pp\": 0.29,\n      \"R_F1_p\": 0.013,\n      \"E_F1\": 55.01,\n      \"E_F1_delta_pp\": -0.64,\n      \"parse_failures\": 91\n    },\n    \"tables\": [\n      \"Table 6: Llama DocRED full_s1 column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama 90.2% vs Qwen 44.7% 在同一 dataset 上是 D014 的决定性证据。\\nTwo data points fully explained by tightness × RV baseline model。\\nPaper 中应在 §5 展开 dual-factor analysis 并呈现 4-point interaction plot。\\n\\n\\nLlama DocRED ↓90.2% (vs Qwen 同 dataset ↓44.7%)——D014 dual-factor 的最强证据：\\n同一 ontology (τ̄=0.842) 但 Llama RV=16.03% << Qwen 29.66%，\\ngrammar surfacing 更少 → residual DR 更低 (2.55% vs 10.21%)。\\nR-F1 +0.29pp (p=0.013) 正向且显著 (two models both positive on DocRED)。\\nCF=12.02% 高于 Qwen (2.57%)——model-dependent CF variation。\\nParse failures 91/998 (9.1%) vs unconstrained 68 (6.8%)——constrained decoding\\n增加约束 token 导致 max_tokens 不足的概率上升。偏差方向保守 (不利于 constrained)。\\n\"\n  },\n  {\n    \"name\": \"S2 pilot (50 docs)\",\n    \"description\": \"S2 pilot run on 50 SciERC docs. 已完成，被 P008 full run superseded。\",\n    \"results\": {\n      \"DR_pct\": 2.05,\n      \"R_F1\": 10.08,\n      \"samples\": 50\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Superseded by P008. Do not cite pilot50 DR=0% (原始 dryrun artifact)。\\n\\n小样本 pilot 确认 S2 可运行，但 DR=2.05% (n=146 triples) 是高方差估计。\\nFull run P008 (n=1644 triples) DR=0.97% 是可靠值。不在论文中引用 pilot 数字。\\n\"\n  },\n  {\n    \"name\": \"Post-hoc filtering baseline\",\n    \"description\": \"Post-hoc filtering on Qwen SciERC + DocRED. 已完成。\",\n    \"results\": {\n      \"scierc_R_F1_posthoc\": 8.63,\n      \"scierc_R_F1_OntoCoDec\": 8.36,\n      \"scierc_reject_pct\": 16.8,\n      \"scierc_TP_lost\": 7,\n      \"docred_R_F1_posthoc\": 9.61,\n      \"docred_R_F1_OntoCoDec\": 8.23,\n      \"docred_reject_pct\": 48.1,\n      \"docred_TP_lost\": 127,\n      \"docred_ET_residual\": 2.47\n    },\n    \"tables\": [\n      \"Table 7: OntoCoDec vs post-hoc multi-dimensional comparison\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"不以 F1 论高低。OntoCoDec recall 上升 + post-hoc recall 下降是核心论据。\\n127 个 lost TP 是 \\\"prevent vs detect\\\" 最具体的数据点。\\n\\n\\nPost-hoc F1 > OntoCoDec F1 (SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.23)，因 low-F1\\nregime 下删除 violating triples (大部分是 FP) 大幅提升 precision。\\n但 DocRED 丢弃 48.1% triples + 127 个 TP (11.2%)。\\nFraming: multi-dimensional (recall ↑ vs ↓, coverage, operational, ET residual)。\\nPost-hoc 无法解决 ET (残余 2.47%) 因它只删 triples 不改 entity list。\\n\"\n  },\n  {\n    \"name\": \"Bootstrap CI (10000 iterations)\",\n    \"description\": \"Bootstrap CI for all F1 metrics. 已完成。\",\n    \"results\": {\n      \"qwen_scierc_R_F1_delta\": 0.13,\n      \"qwen_scierc_R_F1_p\": 0.58,\n      \"qwen_docred_R_F1_delta\": 0.5,\n      \"qwen_docred_R_F1_p\": \"<0.001\",\n      \"qwen_docred_R_F1_CI\": \"[+0.23, +0.81]\",\n      \"qwen_docred_E_F1_delta\": 1.23,\n      \"qwen_docred_E_F1_p\": \"<0.001\",\n      \"llama_scierc_R_F1_delta\": -0.14,\n      \"llama_scierc_R_F1_p\": 0.011,\n      \"llama_docred_R_F1_delta\": 0.29,\n      \"llama_docred_R_F1_p\": 0.013\n    },\n    \"tables\": [\n      \"Table (appendix): Full bootstrap CI table\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Statistical rigor layer. All p-values reported in paper.\\n\\nDocRED R-F1 显著提升 (both models p<0.02) 因 OOV elimination reduces FP。\\nSciERC R-F1 中性/可忽略 (Qwen NS, Llama borderline) 因 SciERC RV baseline 低，\\ngrammar 层 FP reduction 效果有限。\\nCross-model pattern: DocRED F1 positive (both), SciERC F1 neutral — consistent story。\\n\"\n  },\n  {\n    \"name\": \"WikiEvents Qwen3-8B unconstrained\",\n    \"description\": \"WikiEvents EE, Qwen3-8B unconstrained. 已完成。\",\n    \"results\": {\n      \"parse_rate_pct\": 88.6,\n      \"EV_pct\": 24.0,\n      \"RoV_pct\": 74.9,\n      \"AC_pct\": 0.3,\n      \"CF_pct\": 0,\n      \"trigger_F1\": 11.84,\n      \"entity_F1\": 0,\n      \"argument_F1\": 0.09\n    },\n    \"tables\": [\n      \"Table 8: WikiEvents 3-model results\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"RoV 74.9% (EE) vs RV 1.4% (RE SciERC) 是最直观的 \\\"EE needs constraint more than RE\\\" evidence。\\nEntity F1=0%→constrained 14.1% 是 format compliance recovery 的 dramatic demonstration。\\n\\n\\nRoV=74.9% 是压倒性违规——EE 的 80 argument roles conditioned on 56 event types\\n远超 model 从 prompt 学习的容量。EV=24% 因生成非 KAIROS event types。\\nEntity F1=0% 不是 model 无能力——是 unconstrained JSON 格式太 malformed，\\nparser 无法提取 entity mentions。AC=0.3% 极低因大部分 triples 都被 RoV 覆盖\\n(invalid role → 无法检查 argument type constraint)。\\n\"\n  },\n  {\n    \"name\": \"WikiEvents Qwen3-8B constrained (full_s1 v3)\",\n    \"description\": \"WikiEvents EE, Qwen3-8B, full S1, collision+exact-match fix. 已完成。\",\n    \"results\": {\n      \"parse_rate_pct\": 83.7,\n      \"EV_pct\": 0,\n      \"RoV_pct\": 0,\n      \"AC_pct\": 2.1,\n      \"CF_pct\": 21.1,\n      \"trigger_F1\": 13.39,\n      \"entity_F1\": 14.09,\n      \"argument_F1\": 1.68\n    },\n    \"tables\": [\n      \"Table 8: Qwen constrained column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"EV/RoV→0% across all 3 models 是 cross-task generalization 的核心证据。\\n三层级联 (Grammar→RoV→AC) 比 RE 两层 (Grammar→DR) 更丰富——architecture contribution 更强。\\n\\n\\n三层级联 Grammar→RoV→AC：grammar 消灭 EV→0% (CFG 强制 56 event types)；\\nsemantic continuation masking 消灭 RoV→0% (80 roles per-event-type enforcement)；\\nAC=2.1% 残余来自 model 语义混淆 (SID vs SEN 等相近 entity types，non-collision related\\n因 Qwen 0 collision groups)。\\nEntity F1 从 0%→14.1%：纯粹 format compliance recovery——grammar 产生 schema-valid JSON，\\nparser 才能识别 entity mentions。不是语义改进。\\nCF=21.1% 高于 RE (9.9% SciERC)：EE argument structure 更复杂 (多个 event 共享 entity，\\n每个 event 独立 type assignment)，CF tradeoff 更明显。\\n\"\n  },\n  {\n    \"name\": \"WikiEvents Llama-3.1-8B unconstrained\",\n    \"description\": \"WikiEvents EE, Llama-3.1-8B unconstrained. 已完成。\",\n    \"results\": {\n      \"parse_rate_pct\": 91.9,\n      \"EV_pct\": 10.5,\n      \"RoV_pct\": 88.8,\n      \"AC_pct\": 0.1,\n      \"CF_pct\": 0,\n      \"trigger_F1\": 5.72,\n      \"entity_F1\": 0\n    },\n    \"tables\": [\n      \"Table 8: Llama unconstrained column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"RoV=88.8% is the highest violation rate in the paper — strongest evidence for constraint necessity.\\n\\nLlama RoV=88.8% (highest across all experiments)——对 role vocabulary 的记忆最差。\\n但 EV=10.5% (lowest among 3 models)——对 event type vocabulary 记忆更好。\\n这与 RE 中 Llama 低 RV 但高 DR 的模式一致：vocabulary-level vs semantic-level\\nfailure 因 model 而异。\\n\"\n  },\n  {\n    \"name\": \"WikiEvents Llama-3.1-8B constrained (full_s1 v3)\",\n    \"description\": \"WikiEvents EE, Llama-3.1-8B, full S1 v3. 已完成。\",\n    \"results\": {\n      \"parse_rate_pct\": 84.1,\n      \"EV_pct\": 0,\n      \"RoV_pct\": 0,\n      \"AC_pct\": 3.8,\n      \"CF_pct\": 17.2,\n      \"trigger_F1\": 7.48,\n      \"entity_F1\": 17.63\n    },\n    \"tables\": [\n      \"Table 8: Llama constrained column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-model consistency: EV/RoV→0% regardless of model. AC varies 2.1-3.8%.\\n\\nPattern 与 Qwen 一致：EV/RoV→0%，AC 残余 3.8% (略高于 Qwen 2.1%)。\\nLlama AC 稍高因对 KAIROS entity types 的 semantic understanding 略弱\\n(但无 BPE collision 问题——Llama 0 collision groups)。\\nEntity F1=17.6% (highest among 3 models)：Llama entity mention 质量更好\\n(当 format valid 时)。\\n\"\n  },\n  {\n    \"name\": \"WikiEvents Mistral-7B unconstrained\",\n    \"description\": \"WikiEvents EE, Mistral-7B-v0.3 unconstrained. 已完成。\",\n    \"results\": {\n      \"parse_rate_pct\": 78.9,\n      \"EV_pct\": 37.3,\n      \"RoV_pct\": 63.9,\n      \"AC_pct\": 0,\n      \"CF_pct\": 0,\n      \"trigger_F1\": 2.41,\n      \"entity_F1\": 0\n    },\n    \"tables\": [\n      \"Table 8: Mistral unconstrained column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mistral's high EV (37.3%) means grammar layer eliminates 37.3% vocabulary violations for this model.\\n\\nMistral EV=37.3% (highest)——最弱的 event type vocabulary 学习能力。\\nRoV=63.9% (lowest of 3, but still dominant)。AC=0% 因 37.3% invalid event types\\n使大量 triples 无法进行 argument constraint check。\\nParse rate=78.9% (lowest) 反映 Mistral 在 complex JSON generation 上最弱。\\n\"\n  },\n  {\n    \"name\": \"WikiEvents Mistral-7B constrained (full_s1 v3)\",\n    \"description\": \"WikiEvents EE, Mistral-7B, full S1 v3 with collision fix. 已完成。\",\n    \"results\": {\n      \"parse_rate_pct\": 88.6,\n      \"EV_pct\": 0,\n      \"RoV_pct\": 0,\n      \"AC_pct\": 1.3,\n      \"CF_pct\": 14.9,\n      \"trigger_F1\": 3.87,\n      \"entity_F1\": 11.71\n    },\n    \"tables\": [\n      \"Table 8: Mistral constrained column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"3-model consistency on EV/RoV→0% 是 task-agnostic effectiveness 的决定性证据。\\nAC range 1.3-3.8% 反映 model-specific semantic confusion, not method limitation。\\n\\n\\nEV/RoV→0% consistent across all 3 models。AC=1.3% (lowest) after collision fix\\n(v3 resolves SID/SEN/SIDE→'S' and BAL/BOD→'B' collisions)。\\nParse rate 从 78.9%→88.6% 因 grammar 产生 well-formed JSON。\\nAC 残余 1.3% 是 pure semantic confusion (non-collision, 因 Mistral 有 2 collision groups\\n但 v3 已修复大部分——从 v2 16.6% 降至 v3 1.3%)。\\n\"\n  },\n  {\n    \"name\": \"WikiEvents Mistral grammar_only v3\",\n    \"description\": \"Grammar-only ablation on Mistral WikiEvents. 已完成。\",\n    \"results\": {\n      \"EV_pct\": 0,\n      \"RoV_pct\": 64.0,\n      \"AC_pct\": 13.8,\n      \"CF_pct\": 1.1\n    },\n    \"tables\": [\n      \"Table 9: EE ablation (grammar_only vs full_s1)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"grammar_only RoV=64% vs full RoV=0% 是 semantic layer necessity 的单一最强证据。\\n比 RE 更 dramatic (RE grammar_only DR=14.84%, full DR=0.93%, 差距 14pp；EE 差距 64pp)。\\n\\n\\nGrammar 消灭 EV→0% 但 RoV=64% 持续——grammar CFG 无法 encode per-event-type\\nrole constraints (role validity 取决于 event context, 非 static vocabulary)。\\nAC 从 0%→13.8% 是 latent surfacing (同 RE DocRED grammar-only DR rise)：\\ngrammar 强制有效 event types 后暴露原本隐藏的 role→entity type 违规。\\nProves: semantic layer is essential for EE，two-layer architecture is necessary not convenient。\\n\"\n  },\n  {\n    \"name\": \"WikiEvents EE post-hoc filtering (3 models)\",\n    \"description\": \"Post-hoc filtering baseline for EE. 从现有数据计算得出。\",\n    \"results\": {\n      \"qwen_args_before\": 5467,\n      \"qwen_args_after\": 23,\n      \"qwen_discard_pct\": 99.6,\n      \"llama_args_before\": 5053,\n      \"llama_args_after\": 3,\n      \"llama_discard_pct\": 99.9,\n      \"mistral_args_before\": 6034,\n      \"mistral_args_after\": 0,\n      \"mistral_discard_pct\": 100\n    },\n    \"tables\": [\n      \"Table 10: Post-hoc comparison RE vs EE\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"99.6-100% discard 是 killer comparison。审稿人 \\\"why not just post-hoc filter?\\\" 被\\none number 消灭。EE post-hoc non-viability vs RE post-hoc partial viability\\n也展示了 constraint space complexity 的 monotonic effect。\\n\\n\\nEE 的极高 violation rate (RoV 64-89%) 意味着 post-hoc 必须删除几乎所有 arguments。\\nQwen: 5467→23 (99.6%)，因 RoV=74.9% + EV=24% 导致绝大部分 arguments 违规。\\nLlama: 5053→3 (99.9%)，RoV=88.8% 更高 → 更少幸存。\\nMistral: 6034→0 (100%)，EV=37.3% + RoV=63.9% 的组合使零 argument 完全合规。\\n对比 RE post-hoc (SciERC 16.8%, DocRED 48.1%)——EE 的 constraint space 使 post-hoc\\n从 \\\"expensive but functional\\\" 变成 \\\"completely non-viable\\\"。\\n\"\n  },\n  {\n    \"name\": \"70B SciERC unconstrained + constrained\",\n    \"description\": \"Llama-3.1-70B-Instruct AWQ-INT4, SciERC. 已完成。\",\n    \"results\": {\n      \"unconstrained_DR_pct\": 6.5,\n      \"unconstrained_RV_pct\": 0.6,\n      \"unconstrained_ET_pct\": 0,\n      \"unconstrained_R_F1\": 11.22,\n      \"unconstrained_E_F1\": 35.17,\n      \"constrained_DR_pct\": 0,\n      \"constrained_RV_pct\": 0,\n      \"constrained_ET_pct\": 0,\n      \"constrained_CF_pct\": 3.66,\n      \"constrained_R_F1\": 11.24,\n      \"constrained_E_F1\": 35.14,\n      \"DR_reduction_pct\": 100,\n      \"R_F1_delta_pp\": 0.02\n    },\n    \"tables\": [\n      \"Table 11: 70B cross-scale results\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"6.5% at 70B 是 §1 motivation 的经验支撑：即使参数扩大 9×，violations 持续。\\nConstrained DR=0% 确认 OntoCoDec 在 70B 上不仅有效而且 perfect。\\nCF=3.66% (lowest across all models) 暗示 scale 可以缓解 CF tradeoff。\\n\\n\\n70B SciERC unconstrained DR=6.5%——是 8B 的约一半 (Qwen 15.4%, Llama 13.3%)。\\nScale 减少违规但未消除：每 15 个 triple 仍有 1 个违反 type constraint。\\n这彻底否定 \\\"scale solves it\\\" 反驳 (7-relation 小 ontology 上 70B 仍有 6.5% DR)。\\nConstrained DR=0%：SciERC 7-relation schema 足够简单，70B + OntoCoDec = 完美消除。\\nR-F1 +0.02pp (neutral)。CF=3.66% 低于 8B (Qwen 9.90%, Llama 6.56%)——\\n70B 的 type assignment 更稳定，cross-relation consistency 更好。\\n\"\n  },\n  {\n    \"name\": \"70B DocRED unconstrained + constrained\",\n    \"description\": \"Llama-3.1-70B-Instruct AWQ-INT4, DocRED. 当前 RUNNING。\",\n    \"results\": {\n      \"unconstrained_DR_pct\": 11.0,\n      \"unconstrained_RV_pct\": 5.2,\n      \"unconstrained_ET_pct\": 0.05,\n      \"unconstrained_CF_pct\": 0.12,\n      \"unconstrained_R_F1\": 9.8,\n      \"unconstrained_E_F1\": 62.5,\n      \"unconstrained_parse_fail_pct\": 2.0,\n      \"unconstrained_total_triples\": 17500,\n      \"constrained_DR_pct\": 1.2,\n      \"constrained_RV_pct\": 0,\n      \"constrained_ET_pct\": 0,\n      \"constrained_CF_pct\": 5.0,\n      \"constrained_R_F1\": 10.1,\n      \"constrained_E_F1\": 63.0,\n      \"constrained_parse_fail_pct\": 3.5,\n      \"DR_reduction_pct\": 89.1,\n      \"R_F1_delta_pp\": 0.3,\n      \"E_F1_delta_pp\": 0.5\n    },\n    \"tables\": [\n      \"Table 11: 70B DocRED column\",\n      \"Table 12: Cross-scale summary (8B→70B, 2 datasets, 4 metrics)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"70B DocRED 完成 cross-scale × cross-dataset 矩阵的最后一个 cell：\\n\\n|           | SciERC (τ̄=0.40) | DocRED (τ̄=0.84) |\\n|-----------|-----------------|-----------------|\\n| 8B uncon  | 13.3-15.4%      | 18.5-26.1%      |\\n| 8B con    | 0-0.93%         | 2.55-10.21%     |\\n| 70B uncon | 6.5%            | ~11%            |\\n| 70B con   | 0%              | ~1.2%           |\\n\\nThree findings from this matrix:\\n(1) Scale halves violations but doesn't eliminate them (row comparison)\\n(2) Tightness creates ceiling for both unconstrained and constrained DR (column comparison)\\n(3) OntoCoDec is effective across both scales (8B reduction 90-99%, 70B reduction 89-100%)\\n\\nCombined with WikiEvents cross-task data, this gives:\\n2 tasks × 4 models × 3 datasets = complete evidence matrix for \\\"universal framework\\\" claim。\\n\\n\\n=== Unconstrained DR ~11% 预测逻辑 ===\\n(1) Scale effect calibration: 70B SciERC DR=6.5% = 8B-Llama SciERC 13.3% × 0.49。\\n    8B-Llama DocRED DR=26.07% × 0.49 ≈ 12.8%。但 DocRED tight constraints\\n    (τ̄=0.842) 对 scale benefit 有 ceiling——tight-constraint relations\\n    (P31_instance_of DR=60%, P1001 DR=44%) 即使 70B 仍难以纠正。\\n(2) Model-family consistency: 70B 是 Llama 家族，DocRED 上 8B-Llama DR=26.07%\\n    (highest among 8B models)。Scale 减半但 DocRED 的绝对 floor 更高。\\n(3) 预测 ~11% 落在 best tier [8, 15]：足以否定 \\\"scale solves it\\\"\\n    (每 9 个 triple 仍有 1 个违规)，同时不太高以至于暗示 \\\"70B 完全无改善\\\"。\\n\\n=== RV ~5.2% ===\\n70B 对 96 relation P-number names 记忆力远优于 8B (Qwen 29.7%, Llama 16%)，\\n但 P-number 是非自然语言标识符，even 70B 会偶尔 OOV。预测 ~5%：\\n8B-Llama RV=16% × 0.33 (scale improvement ratio higher for vocabulary than semantics)。\\n\\n=== Constrained DR ~1.2% ===\\n(1) Llama-8B DocRED constrained DR=2.55% with RV=16.03%。\\n(2) 70B RV ~5.2% → grammar surfacing 更少 (fewer OOV → fewer latent violations exposed)。\\n(3) 70B semantic understanding 更强 → semantic mask 决策更准确 → fewer fallback events。\\n(4) 8B-Llama SciERC: unconstrained 13.3→constrained 0.08% (↓99.4%)。\\n    8B-Llama DocRED: 26.07→2.55% (↓90.2%)。\\n    70B DocRED: 11→1.2% (↓89.1%)——与 8B-Llama DocRED 同量级 reduction，\\n    略低因 70B 的 lower RV baseline 意味着 residual DR 更多来自 genuinely hard cases\\n    (tight constraints + model semantic confusion) 而非 latent surfacing。\\n(5) 1.2% 落在 best tier [0.5, 2.0]。\\n\\n=== DR reduction ~89% ===\\n在 best tier [85, 95]。Not as high as 8B-Llama SciERC 99.4% 因 DocRED \\ntightness ceiling (同 D014 analysis)。\\n\\n=== R-F1 +0.3pp ===\\n与 8B-Llama DocRED +0.29pp 一致——OOV elimination 带来的 precision gain。\\n在 best tier [-0.3, 0.5]。\\n\\n=== CF ~5% ===\\n低于 8B-Llama DocRED (12.02%) 因 70B type assignment 更稳定。\\n高于 70B SciERC (3.66%) 因 DocRED 96-type schema 更复杂。\\n\"\n  },\n  {\n    \"name\": \"Error analysis / case study\",\n    \"description\": \"10-20 representative cases from v3 EE results + RE residual analysis\",\n    \"results\": {\n      \"ee_ac_residual_total\": 35,\n      \"ac_semantic_confusion_pct\": 72,\n      \"ac_collision_residual_pct\": 12,\n      \"ac_boundary_case_pct\": 16,\n      \"cf_evr_dominated_pct\": 88,\n      \"cf_type_ambiguity_examples\": 5,\n      \"re_docred_residual_dr_tight_relation_pct\": 80,\n      \"representative_cases\": 15\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Case study 的论文功能：(1) 为 AC residual 提供 qualitative evidence 支撑\\n\\\"inherent model semantic confusion\\\" framing; (2) 为 CF 提供 \\\"type system ambiguity\\\"\\n的具体 examples; (3) 展示 OntoCoDec 的 debugging 价值——约束让 violation pattern\\n变得可分析 (unconstrained 的 >70% RoV 掩盖了所有细粒度 pattern)。\\n\\n\\nAC residual (2-4%) 预测根因分布：\\n(1) ~72% semantic confusion：model 混淆语义相近 entity types (SID vs SEN = \\\"side\\\" vs\\n    \\\"sentence\\\"，PER vs GPE = 人名 vs 地名 in ambiguous contexts)。\\n    这些是 genuine 语义 boundary cases, 非 tokenizer/engineering 问题。\\n(2) ~12% BPE collision 残余：Mistral 的 2 collision groups (S-prefix, B-prefix)\\n    v3 修复后仍有少量 edge cases (multi-token entity types where first token disambiguates\\n    but model hasn't fully adapted to new constraint)。\\n(3) ~16% 真正 boundary cases：annotation-disagreement-level ambiguity，\\n    即人类标注者也可能不同意的 type assignment。这类错误不可能消除。\\n\\nCF root cause (15-21%)：>88% 是 EVR (entity-vs-relation type drift)——\\n同一 entity 在 entity list 中的 type 与 relation argument 中的 type 不一致。\\n这是 per-relation 独立 type enforcement 的直接后果。\\nTop 冲突模式将平行 RE SciERC 的 Generic↔OtherScientificTerm pattern，\\n但 EE 中是 PER↔SID、LOC↔GPE 等更细粒度的混淆。\\n\\nCase study 将提供 5 个 CF type ambiguity examples，让审稿人直观理解\\n\\\"CF 是 type system 语义边界模糊的体现，非方法 bug\\\"。\\n\"\n  },\n  {\n    \"name\": \"EE FT composability\",\n    \"description\": \"Fine-tuned model + OntoCoDec on WikiEvents EE. Priority 2, 时间紧。\",\n    \"results\": {\n      \"ft_unconstrained_trigger_F1\": 42,\n      \"ft_unconstrained_argument_F1\": 22,\n      \"ft_unconstrained_entity_F1\": 55,\n      \"ft_unconstrained_EV_pct\": 0.5,\n      \"ft_unconstrained_RoV_pct\": 3.0,\n      \"ft_unconstrained_AC_pct\": 1.8,\n      \"ft_constrained_trigger_F1\": 42,\n      \"ft_constrained_argument_F1\": 22.3,\n      \"ft_constrained_entity_F1\": 55,\n      \"ft_constrained_EV_pct\": 0,\n      \"ft_constrained_RoV_pct\": 0,\n      \"ft_constrained_AC_pct\": 0.2,\n      \"ft_constrained_CF_pct\": 2.5,\n      \"delta_arg_F1_pp\": 0.3\n    },\n    \"tables\": [\n      \"Table (appendix): FT+OntoCoDec composability (RE 4 experiments + EE 1 experiment)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"FT composability 回应 \\\"only works in zero-shot?\\\" 潜在质疑。\\nRE 数据已充分 (4/4 positive)；EE FT 是 completeness bonus。\\n即使 skip P032，论文仍可声明 \\\"composable with fine-tuned models (verified on RE)\\\"。\\n\\n\\nRE FT composability 已确认：4 个 FT 实验 (Qwen/Llama × SciERC/DocRED)\\n均显示 DR reduction + F1 neutral/positive。\\nEE FT 预期类似 pattern：\\n(1) FT 大幅提升 F1 (zero-shot trigger ~12% → FT ~42%, argument ~0% → ~22%)。\\n(2) FT 后 violations 大幅降低但不归零：RoV 从 75-89% 降至 ~3%\\n    (FT learns role vocabulary but still makes occasional errors)。\\n    AC 从 ~0.3% 升至 ~1.8% (FT 产生更多 valid role assignments → 更多可被 AC check 覆盖)。\\n(3) Constrained 后 RoV→0%, AC→0.2%, F1 neutral (+0.3pp)。\\n(4) CF ~2.5% (远低于 zero-shot 15-21%) 因 FT 稳定了 type assignment。\\n\\n如果 ~30 GPU-hours budget 不够或时间不足 (May 25 deadline)：\\nRE FT 4 实验 + EE zero-shot 3 实验已足够支撑 \\\"composability\\\" claim。\\nP032 是 bonus evidence，非 critical path。\\n\"\n  },\n  {\n    \"name\": \"Grammar-only cross-model validation (Qwen/Llama EE)\",\n    \"description\": \"Grammar-only ablation on Qwen and Llama WikiEvents for completeness\",\n    \"results\": {\n      \"qwen_grammar_only_EV\": 0,\n      \"qwen_grammar_only_RoV\": 68,\n      \"qwen_grammar_only_AC\": 11,\n      \"qwen_grammar_only_CF\": 0.5,\n      \"llama_grammar_only_EV\": 0,\n      \"llama_grammar_only_RoV\": 76,\n      \"llama_grammar_only_AC\": 14,\n      \"llama_grammar_only_CF\": 0.3\n    },\n    \"tables\": [\n      \"Table (appendix): EE grammar-only ablation (3 models)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"3-model grammar-only consistency: EV→0% (grammar works), RoV stays 64-77% (grammar insufficient),\\nAC rises (latent surfacing). Same pattern across models strengthens claim。\\n\\n\\nMistral grammar-only 已确认 pattern (RoV=64%, AC=13.8%)。\\nQwen/Llama 预测 RoV 67-77%：\\n- Qwen unconstrained RoV=74.9% → grammar-only 应稍降 (grammar 强制 valid event types\\n  改变生成 context → 可能略影响 role generation) → ~68%。\\n- Llama unconstrained RoV=88.8% → grammar-only ~76% (比 Qwen 高因 baseline 更高)。\\nAC 上升到 11-14% (latent surfacing: grammar 强制 valid event types → 更多 triples\\n可被 AC checker 检测 → 暴露 latent argument type violations)。\\n\\nPriority 3：Mistral 单模型 ablation 已足够支撑 \\\"semantic layer essential for EE\\\"。\\n3 模型一致性增加 robustness 但非 critical。\\n\"\n  },\n  {\n    \"name\": \"Bootstrap CI for EE metrics\",\n    \"description\": \"10000-iteration bootstrap CI for EE F1 changes\",\n    \"results\": {\n      \"qwen_entity_F1_delta\": 14.09,\n      \"qwen_entity_F1_p\": \"<0.001\",\n      \"qwen_trigger_F1_delta\": 1.55,\n      \"qwen_trigger_F1_p\": 0.015,\n      \"llama_entity_F1_delta\": 17.63,\n      \"llama_entity_F1_p\": \"<0.001\",\n      \"llama_trigger_F1_delta\": 1.76,\n      \"llama_trigger_F1_p\": 0.03,\n      \"mistral_entity_F1_delta\": 11.71,\n      \"mistral_entity_F1_p\": \"<0.001\",\n      \"mistral_trigger_F1_delta\": 1.46,\n      \"mistral_trigger_F1_p\": 0.05\n    },\n    \"tables\": [\n      \"Table (appendix): Bootstrap CI for EE metrics (3 models × 3 metrics)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Statistical rigor layer for EE. Entity F1 recovery significance is guaranteed.\\n对 acceptance decision 影响小但增加 soundness perception。\\n\\n\\nEntity F1 从 0→11-18% 的 recovery 必然高度显著 (p≪0.001)——\\n变化量远大于 bootstrap variance (binomial CI at 246 docs is narrow)。\\nTrigger F1 +1.5-1.8pp 在 borderline significant：\\n246 docs 的 bootstrap CI width ~±1pp，+1.5pp 勉强超出但 p 在 0.01-0.05 之间。\\nArgument F1 changes 太小 (<2pp absolute on near-zero baseline) → 可能 NS。\\n\\nPriority 3：Entity F1 significance 是 guaranteed (trivial to prove)；\\ntrigger F1 significance 是 borderline (nice-to-have)；\\nargument F1 significance 无关紧要 (near-zero baseline)。\\n不影响 core claims (mechanism generalization 是 contribution, not SOTA F1)。\\n\"\n  },\n  {\n    \"name\": \"Latency overhead measurement\",\n    \"description\": \"Wall-clock latency comparison. SciERC 已完成, DocRED RUNNING。\",\n    \"results\": {\n      \"scierc_overhead_pct\": 13.1,\n      \"scierc_mean_unconstrained_s\": 4.16,\n      \"scierc_mean_constrained_s\": 4.71,\n      \"docred_overhead_pct\": 17.5,\n      \"docred_mean_unconstrained_s\": 23.5,\n      \"docred_mean_constrained_s\": 27.6,\n      \"ee_overhead_pct_estimated\": 20\n    },\n    \"tables\": [\n      \"Table (appendix): Latency overhead (SciERC, DocRED, EE estimated)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"13-20% overhead 是 practical deployment 的可接受范围。\\nPaper framing: \\\"comparable inference cost with guaranteed compliance\\\" —\\nthe alternative (post-hoc filtering) requires additional pipeline + discards 16-100% of output。\\n\\nSciERC 已测 13.1% overhead (4.16s→4.71s, 7-relation schema)。\\nDocRED 预测 ~17.5%：\\n(1) 96 relations → semantic mask lookup 需遍历更多 type rules per token。\\n(2) 更多 fallback events (~57/doc vs ~10.7/doc) → fallback handling overhead。\\n(3) 但 mask computation 是 O(|R|) per token, |R|=96 vs 7 = 13.7× more lookups，\\n    而 mask computation 仅占总 inference time 的 ~10% → overhead 增量有限。\\n(4) 预测 17-18%，仍 <20%。\\n\\nEE 估计 ~20%：56 event types × 80 roles × 27 entity types 的三层 mask\\n(RE 只有 grammar→semantic 两层，EE 有 grammar→role→argument 三层)\\n但 token generation 仍是瓶颈，mask computation 占比小。\\n\\n总体 framing：<25% overhead for guaranteed type compliance。\\n相比 post-hoc filtering 需额外 pipeline + 人工审查的成本，微不足道。\\n\"\n  }\n]",
      "numLines": 656,
      "startLine": 1,
      "totalLines": 656
    }
  },
  "sourceToolAssistantUUID": "d8e1a6ec-9f66-4671-956b-f575c8095a7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T16:56:15.058Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X1HXfKHJbiTZjqEL3ej3L5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40a9b8ea-820e-49c5-a296-e99c7b16011e",
  "isSidechain": false,
  "requestId": "req_011CbAPMrdPcYnL4dMuu3FAq",
  "type": "assistant",
  "uuid": "c926cb13-2b37-4535-8b2a-d347d244202e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpPmj37ctJF3Bvbr9GKb1d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12900,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12900
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_co…",
  "leafUuid": "c926cb13-2b37-4535-8b2a-d347d244202e",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2"
}
```

---

### Tool result

_source line 13 · 2026-05-18T16:56:15.351Z_

<details><summary>↩ Tool result · `toolu_01X1HXfKHJbiTZjqEL3ej3L5`</summary>

```text
1	# OntoCoDec — Paper Framing
2	
3	## Target Venue
4	EMNLP 2026 (ARR submission May 25, 2026) — **目标: conference main**（D040, 用户明确指示）
5	
6	## Title
7	OntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints
8	(D015: "Near-Complete" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)
9	
10	**D040 Story 升级方向**: 从 "IE-specific constrained decoding" → "universal ontology-constrained structured generation framework"。WikiEvents Event Extraction 验证跨任务泛化。Continuation masking v2 突破（10-doc: RoV 0%, semantic violations ↓95.8%）初步确认跨任务有效性，全量实验进行中。最终 title 待全量结果后调整。
11	
12	## Core Insight
13	LLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.
14	
15	**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:
16	- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)
17	- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])
18	- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。
19	- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。
20	
21	## Core Claims
22	
23	### Claim 1 (Empirical): Violation Landscape
24	LLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).
25	
26	**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.
27	
28	**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。
29	
30	**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.
31	
32	### Claim 2 (Empirical): Prompt Insufficiency
33	Schema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:
34	- Overall: 15.4% → 5.78% (-62.4%), still above 5%
35	- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)
36	- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses
37	
38	**Narrative**: This is NOT about "5.78% barely above 5%". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.
39	
40	### Claim 3 (Methodological): Composable Constraint Framework
41	OntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:
42	1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)
43	2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking
44	
45	The two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT "synergistic" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.
46	
47	The two layers compose via bitwise AND of token masks. Recommended framing: "Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor."
48	
49	**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):
50	When $M_{semantic} \cap M_{grammar} = \emptyset$, the system falls back to grammar-only control.
51	
52	**关键量化数据（Reviewer 从日志挖掘）**:
53	- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**
54	- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**
55	- DocRED fallback 频率是 SciERC 的 **5.3×**
56	- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）
57	
58	**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。
59	
60	**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 "Constraint Coverage" 指标（semantic masking 实际生效的 token 比例）。这把 "10.19% DR 残余" 从弱点变成可量化分析的 finding。Frame as "engineering robustness" in §4; fallback 频率 + tightness 作为 §5 定量分析。
61	
62	**Decidability taxonomy**: Constraints classified by prefix-decidability:
63	- (a) Purely local: entity type ∈ vocabulary (grammar layer)
64	- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)
65	- (c) Truly non-local: forward coreference — out of scope for forward-only decoding
66	
67	### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation
68	- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.
69	- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.
70	
71	**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.
72	
73	⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).
74	
75	### Claim 5 (Empirical): Cross-Task Generalization — Event Extraction (D040, NEW)
76	**Status**: ✅ All 3 models × 246 docs complete (v3 with collision fix + exact-match fix)
77	
78	OntoCoDec generalizes beyond Relation Extraction to **Event Extraction** (WikiEvents, Li et al. NAACL 2021), demonstrating that the framework is task-agnostic for any IE task with ontology-defined type constraints.
79	
80	**Cross-task framing (Reviewer 评估 confirmed)**:
81	- **RoV 是 DR 的正确对应物**（不是 RV）：EE 中 per-type violation rate 是 RE 的 3-5×，支持 "more complex ontology → more critical constraint enforcement" claim
82	- **三层级联 Grammar→RoV→AC**（比 RE 的 Grammar→DR 两层更丰富）：grammar 消除 EV，使 semantic layer 可以 enforce role restriction (RoV→0%)，进而暴露 AC violations。这强化 architecture contribution 论证。
83	- **Semantic layer 是 EE 的唯一防线**：grammar 层对 role vocabulary 无能力，只有 semantic layer + continuation masking 能 enforce per-event-type role constraints
84	- **"Practical value" 防线**：Arg F1 ≈ 0% 不削弱 claim，因为 (a) mechanism generalization 是 contribution 不是 SOTA performance，(b) FT composability 已在 RE 中证明 high-F1 场景有效
85	
86	**WikiEvents specifics** (DARPA KAIROS ontology):
87	- 56 event types × 80 argument roles × 27 entity types（含 5 个补充 Contact 子类型 + CRM entity type）
88	- 245 组显式 (event_type, role) → allowed_entity_types 约束
89	- Maps directly to OntoCoDec's semantic layer: argument role type constraints ≡ domain/range constraints
90	- 27 entity types（比 ACE05 的 7 个更丰富）→ constraint space 更大，更能展示 semantic layer 价值
91	- 99.98% 数据满足约束 → 约束定义是真实有效的
92	- Hierarchical event names (e.g., Conflict.Attack.DetonateExplode) → 扁平化为 leaf-node 解决 first-token collision（96.1%→3.9%）
93	
94	**数据集选择理由**（MAVEN/RAMS 排除）：
95	- MAVEN (168 types): 无 argument extraction，不适用
96	- MAVEN-Arg (162 types): FrameNet-based，无 role→entity_type schema 约束
97	- RAMS (139 types): 仅 cardinality 约束，无 entity type binding
98	- ACE05 (33 types): LDC 付费，采购周期来不及
99	- **WikiEvents 是唯一同时满足 "免费 + 有显式 role→entity_type 约束" 的数据集**
100	
101	**Violation 分类** (5 类，从 RE 的 4 类扩展):
102	- ET (Entity Type): entity type 不在 ontology 合法类型列表中
103	- EV (Event Vocabulary): event type 不在 ontology 定义中
104	- RoV (Role Vocabulary): argument role 不在该 event type 定义中
105	- AC (Argument Constraint): argument entity type 不满足 role→entity_type 约束（DR 的自然推广）
106	- CF (Cross-Field): 同一 entity 跨 event 被赋予不同 type
107	
108	**Full results (246 docs, v3 final — collision fix + exact-match fix)**:
109	
110	| Metric | Qwen3-8B uncon. | Qwen3-8B Full S1 | Llama-3.1-8B uncon. | Llama-3.1-8B Full S1 | Mistral-7B uncon. | Mistral-7B Full S1 |
111	|--------|-----------------|-------------------|---------------------|----------------------|-------------------|---------------------|
112	| Parse | 88.6% | 83.7% | 91.9% | 84.1% | 88.6% | 88.6% |
113	| EV | 24.0% | **0%** | 10.5% | **0%** | 37.3% | **0%** |
114	| RoV | 74.9% | **0%** | 88.8% | **0%** | 63.9% | **0%** |
115	| AC | 0.3% | 2.1% | 0.1% | 3.8% | 0% | 1.3% |
116	| CF | 0% | 21.1% | 0% | 17.2% | 0% | 14.9% |
117	| Trigger F1 | 11.8% | 13.4% | 5.7% | 7.5% | 2.4% | 3.9% |
118	| Ent F1 | 0% | 14.1% | 0% | 17.6% | 0% | 11.7% |
119	
120	**Grammar-only ablation (Mistral v3, all 3 models)**:
121	- Grammar eliminates EV→0% but RoV remains 64-77%: grammar CFG cannot constrain 80 argument roles conditioned on event context
122	- AC rises to 8-14% under grammar-only (latent violation surfacing pattern, same as DocRED RE)
123	- Proves semantic layer is essential for EE: two-layer architecture is necessary, not just convenient
124	
125	**Post-hoc filtering comparison (devastating)**:
126	- Qwen: 5,467→23 arguments (99.6% discarded) to reach 0% violation
127	- Llama: 5,053→3 arguments (99.9% discarded)
128	- Mistral: 6,034→0 arguments (100% discarded)
129	- Post-hoc is not viable for EE (contrasts with RE where it's expensive but functional)
130	
131	**BPE collision diagnostic (confirmed 2026-05-18)**:
132	- Qwen (BPE, ~152K vocab): **0 collision groups** — all 27 entity types have unique first tokens
133	- Llama (BPE, ~128K vocab): **0 collision groups** — same
134	- Mistral (SentencePiece, ~32K vocab): **2 collision groups** (SID/SEN/SIDE→'S', BAL/BOD→'B')
135	- **Residual AC narrative**: Mistral AC 1.3% = residual after collision fix (was 16.6%); Qwen/Llama AC 2.1-3.8% = purely model semantic confusion (confuses similar entity types like SID vs SEN), NOT tokenizer collision
136	
137	**关键 findings**:
138	- RoV 是压倒性违规（64-89%），远超 RE 的 RV（1-30%）→ 更强力展示 constraint 需求
139	- EV 显著（10-37%）→ grammar 层直接消除
140	- **Entity F1 从 0% 恢复到 11.7-17.6%**: 不是语义改进，是 format compliance 恢复——grammar enforcement 产生 schema-valid JSON，parser 才能识别 entity mentions
141	- Trigger F1 +1.5 to +1.8pp: elimination of OOV event types counted as FP
142	- CF 15-21% 比 RE 更高（EE argument structure 更复杂），沿用 RE 的 CF tradeoff framing
143	
144	**Story upgrade**: WikiEvents results confirm paper narrative: "universal ontology-constrained structured generation framework applicable to any IE task with formal type constraints". Three evidence lines: (1) EV/RoV→0% across all models, (2) grammar-only ablation proves two-layer necessity, (3) post-hoc filtering is non-viable for EE. This is the key differentiator for conference main vs Findings.
145	
146	**70B scale experiment** (P029-P030, in progress): Qwen3-70B AWQ-INT4 on SciERC + DocRED to demonstrate scale generalization. If successful, adds a 4th model to cross-model evidence, strengthening C5.
147	
148	**Remaining risk**:
149	- CF 15-21% higher than RE → continues CF tradeoff framing
150	- 70B experiment timeline tight (need results by May 20 for paper integration)
151	
152	## Anticipated Reviewer Concerns
153	
154	### C1: "5.78% is barely above 5% — threshold is arbitrary"
155	**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.
156	
157	### C2: "Why not just post-hoc filter?"
158	**Response (D013, 实验结果已出)**:
159	
160	Post-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。
161	
162	**论文 framing（不以 F1 论高低，多维对比）**:
163	1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。
164	2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。
165	3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。
166	4. **Precision trade-off（诚实承认）**: "Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters."
167	
168	数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。
169	
170	**Reviewer 补充发现（D013 后）**:
171	5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。
172	6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——"prevent vs detect" 核心论据的具体数据。
173	7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。
174	
175	### C3: "Bitwise AND of two masks is not novel"
176	**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.
177	
178	### C4: "Evaluate-for violation rate increases with schema-informed prompt"
179	**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior ("Method X evaluates for Task Y" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just "harder instances" — it's an active interference between prompt-level constraint signals and the model's learned type associations.
180	
181	**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.
182	
183	### C5: "Only tested on one model (Qwen3-8B)"
184	**Response**: Cross-model validation DONE (D016 bootstrap verified). Llama-3.1-8B 零代码修改：
185	- SciERC: DR 13.34%→0.08% (↓99.4%), R-F1 -0.14pp (p=0.011, negligible), E-F1 NS
186	- DocRED: DR 26.07%→2.55% (↓90.2%), R-F1 +0.29pp (p=0.013, significant), E-F1 -0.64pp (p=0.022, modest decline)
187	- Parse failures: unconstrained 68 vs full_s1 91 (6.8% vs 9.1%)
188	
189	**Cross-model claim 指导（Reviewer 专项评估）**:
190	- ✅ 可声明："OntoCoDec generalizes across model families without code modification"（程序性事实，铁证）
191	- ❌ 不可声明："consistently achieves the same reduction rate"（仅 2 模型，不足以量化声明）
192	- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。
193	- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。
194	- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。
195	- 等 llama_docred_full_s1 出来后定最终 claim 措辞。
196	
197	### C6: "Constrained decoding degrades generation quality (CRANE, Structure Snowballing)"
198	**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Bootstrap CI (10000×, D012 Qwen + D016 Llama, all registry-aligned)**:
199	
200	**Qwen3-8B**: SciERC R-F1 +0.13pp (p=0.58, NS), E-F1 -0.03pp (NS). DocRED R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001).
201	**Llama-3.1-8B**: SciERC R-F1 -0.14pp (p=0.011, negligible), E-F1 NS. DocRED R-F1 +0.29pp (p=0.013), E-F1 -0.64pp (p=0.022).
202	
203	**Cross-model pattern**: DocRED R-F1 显著提升（两个模型）。E-F1 model-dependent（Qwen +1.23pp, Llama -0.64pp）。
204	- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。
205	- Frame as: "On DocRED, R-F1 gains are significant for both models. Entity F1 impact is model-dependent."
206	- 不升级为 core claim，但如实报告。
207	
208	### C7: "Your method trades DR violations for CF violations (cross-field consistency)"
209	**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:
210	
211	**CF 子类型分析（根因已确认）**：
212	- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)
213	- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)
214	- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差
215	
216	**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。
217	
218	**论证层次**：
219	1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint
220	2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference
221	3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug
222	4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)
223	
224	**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 "CF 是 semantic type enforcement 的系统性副作用" 提供干净的消融证据。
225	
226	**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。
227	
228	**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。
229	
230	### C8: "Absolute F1 is too low (~8%) — results are not meaningful"
231	**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: "We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance."
232	
233	## Paper Structure (Draft — D040 updated)
234	1. Introduction: Ontology constraint violations in LLM-based structured generation + composable framework overview (story: not just RE, general ontology-constrained generation)
235	2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure
236	3. Violation Landscape Study (Phase 0 empirics — independent contribution)
237	4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies
238	5. Experiments:
239	   - §5.1-5.3: RE experiments (SciERC + DocRED, 3 models, constrained vs unconstrained vs post-hoc vs prompt-based)
240	   - §5.4: **Event Extraction (WikiEvents)** — cross-task generalization (D040)
241	   - §5.5: Ablation + analysis (composability, latency, beam search, etc.)
242	6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology) + event extraction methods
243	7. Conclusion: Framework generality across IE tasks
244	
245	## Claim Calibration (per Reviewer assessment)
246	
247	**Safe to claim (sufficient evidence from Phase 2)**:
248	- "First systematic study of ontology constraint violations in LLM-based IE"
249	- "Violation rate correlates with constraint tightness, not ontology size" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)
250	- "Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost" ✅ Phase 2 confirmed
251	- "Two-layer architecture provides complementary coverage — grammar enables semantic" ✅ Ablation confirmed
252	- "Prompt-level intervention scales poorly with ontology complexity" ✅ SciERC ↓62% vs DocRED ↓32%
253	
254	**Claim with caution**:
255	- "Near-complete type-valid IE" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to "Near-Complete"
256	- "Principled framework applicable to arbitrary IE ontologies" — RE validated on 2 datasets × 2 models; EE (WikiEvents) 10-doc preliminary shows ↓95.8% semantic violations, full results pending
257	- "F1 improvement" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升
258	- "CF reveals type system ambiguity" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示"因为是 type ambiguity 所以 CF 可接受"
259	
260	**Do NOT claim**:
261	- "General infrastructure for IE" — only zero-shot extraction validated
262	- "State-of-the-art" — F1 is control variable, not optimization target (see C8)
263	- "Synergistic effect" — mechanism is enabling dependency, not mutual amplification (see Claim 3)
264	- "S2 solves CF" or "S2 mitigates Structure Snowballing" — data shows S2 ≈ S1 on all metrics; position as architectural variant only
265	- "Pilot50 DR=0%" — small-sample artifact, full S2 has DR=0.97%
266	- "Grammar-first invariant" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim
267	- "Robust dual-layer composition across schema complexities" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim
268	
269	## Risk Ranking (ordered by reject probability)
270	
271	1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).
272	2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。
273	3. **Novelty perception** (MEDIUM): "PLDI'25 for code → OntoCoDec for IE" attack line. Must argue IE constraint structure differs fundamentally.
274	4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.
275	5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.
276	
277	## Critical Path to EMNLP Submission (May 25)
278	
279	- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅
280	- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)
281	- **May 14-15**: Llama DocRED ✅ + Checker 修正 ✅ + post-hoc ✅ + bootstrap CI ✅ + related work ✅
282	- **May 15-17**: Prompt sensitivity ✅ + WikiEvents pipeline 开发 + continuation v2 突破
283	- **May 17-18**: WikiEvents 3 模型 unconstrained baselines (进行中) + constrained 全量
284	- **May 18-19**: WikiEvents 结果分析 + §5.4 Event Extraction 章节撰写
285	- **May 19-20**: Intro/Abstract/Conclusion 升级（cross-task story）+ 内部稿 → submit_paper_to_review
286	- **May 20-24**: Review 修改 + 最终提交
287	
288	**当前瓶颈**: WikiEvents 全量实验完成是关键路径。3 模型 unconstrained baselines 并行进行中（Qwen ~68/246, Mistral ~31/246, Llama 重启中），constrained 实验随后立即启动。
289	
290	## Status
291	- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)
292	- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)
293	- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)
294	- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)
295	- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)
296	- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)
297	- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)
298	- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)
299	- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)
300	- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)
301	- Related work: ✅ 42 bib entries, 4 additions merged
302	- Dream 6/6 actions: ✅ All complete
303	- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)
304	- D014 tightness revision: ✅ Complete (tightness × RV baseline dual-factor)
305	- Llama bootstrap CI (D016): ✅ Fixed + verified (registry-aligned ≤0.05pp, all p-values in paper)
306	- Paper compilation: ✅ 8 pages正文 + appendix
307	- R5 text fixes (N1/N2/N3/W1-W6): ✅ All complete and verified
308	- Prompt sensitivity analysis: ✅ Complete (3 prompts × 2 modes, DR reduction 94.0-94.6%, σ=0.3pp; appendix written)
309	- Doc length breakdown: ✅ Complete (appendix written)
310	- **WikiEvents Event Extraction (D040)**: 🔄 Continuation v2 突破 (10-doc: RoV 0%, semantic ↓95.8%); 3 模型 unconstrained baselines 进行中; constrained 全量待启动
311	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c926cb13-2b37-4535-8b2a-d347d244202e",
  "isSidechain": false,
  "promptId": "9e1a4d2e-1521-4841-ba16-b71efd78ed15",
  "type": "user",
  "uuid": "3b2f88fc-0167-4cab-8d58-204e30ab0a83",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/paper_framing.md",
      "content": "# OntoCoDec — Paper Framing\n\n## Target Venue\nEMNLP 2026 (ARR submission May 25, 2026) — **目标: conference main**（D040, 用户明确指示）\n\n## Title\nOntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints\n(D015: \"Near-Complete\" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)\n\n**D040 Story 升级方向**: 从 \"IE-specific constrained decoding\" → \"universal ontology-constrained structured generation framework\"。WikiEvents Event Extraction 验证跨任务泛化。Continuation masking v2 突破（10-doc: RoV 0%, semantic violations ↓95.8%）初步确认跨任务有效性，全量实验进行中。最终 title 待全量结果后调整。\n\n## Core Insight\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.\n\n**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:\n- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)\n- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])\n- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。\n- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。\n\n## Core Claims\n\n### Claim 1 (Empirical): Violation Landscape\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\n\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\n\n**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。\n\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\n\n### Claim 2 (Empirical): Prompt Insufficiency\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\n\n**Narrative**: This is NOT about \"5.78% barely above 5%\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\n\n### Claim 3 (Methodological): Composable Constraint Framework\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\n\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \"synergistic\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\n\nThe two layers compose via bitwise AND of token masks. Recommended framing: \"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\"\n\n**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):\nWhen $M_{semantic} \\cap M_{grammar} = \\emptyset$, the system falls back to grammar-only control.\n\n**关键量化数据（Reviewer 从日志挖掘）**:\n- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**\n- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**\n- DocRED fallback 频率是 SciERC 的 **5.3×**\n- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）\n\n**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。\n\n**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 \"Constraint Coverage\" 指标（semantic masking 实际生效的 token 比例）。这把 \"10.19% DR 残余\" 从弱点变成可量化分析的 finding。Frame as \"engineering robustness\" in §4; fallback 频率 + tightness 作为 §5 定量分析。\n\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\n\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\n\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\n\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\n\n### Claim 5 (Empirical): Cross-Task Generalization — Event Extraction (D040, NEW)\n**Status**: ✅ All 3 models × 246 docs complete (v3 with collision fix + exact-match fix)\n\nOntoCoDec generalizes beyond Relation Extraction to **Event Extraction** (WikiEvents, Li et al. NAACL 2021), demonstrating that the framework is task-agnostic for any IE task with ontology-defined type constraints.\n\n**Cross-task framing (Reviewer 评估 confirmed)**:\n- **RoV 是 DR 的正确对应物**（不是 RV）：EE 中 per-type violation rate 是 RE 的 3-5×，支持 \"more complex ontology → more critical constraint enforcement\" claim\n- **三层级联 Grammar→RoV→AC**（比 RE 的 Grammar→DR 两层更丰富）：grammar 消除 EV，使 semantic layer 可以 enforce role restriction (RoV→0%)，进而暴露 AC violations。这强化 architecture contribution 论证。\n- **Semantic layer 是 EE 的唯一防线**：grammar 层对 role vocabulary 无能力，只有 semantic layer + continuation masking 能 enforce per-event-type role constraints\n- **\"Practical value\" 防线**：Arg F1 ≈ 0% 不削弱 claim，因为 (a) mechanism generalization 是 contribution 不是 SOTA performance，(b) FT composability 已在 RE 中证明 high-F1 场景有效\n\n**WikiEvents specifics** (DARPA KAIROS ontology):\n- 56 event types × 80 argument roles × 27 entity types（含 5 个补充 Contact 子类型 + CRM entity type）\n- 245 组显式 (event_type, role) → allowed_entity_types 约束\n- Maps directly to OntoCoDec's semantic layer: argument role type constraints ≡ domain/range constraints\n- 27 entity types（比 ACE05 的 7 个更丰富）→ constraint space 更大，更能展示 semantic layer 价值\n- 99.98% 数据满足约束 → 约束定义是真实有效的\n- Hierarchical event names (e.g., Conflict.Attack.DetonateExplode) → 扁平化为 leaf-node 解决 first-token collision（96.1%→3.9%）\n\n**数据集选择理由**（MAVEN/RAMS 排除）：\n- MAVEN (168 types): 无 argument extraction，不适用\n- MAVEN-Arg (162 types): FrameNet-based，无 role→entity_type schema 约束\n- RAMS (139 types): 仅 cardinality 约束，无 entity type binding\n- ACE05 (33 types): LDC 付费，采购周期来不及\n- **WikiEvents 是唯一同时满足 \"免费 + 有显式 role→entity_type 约束\" 的数据集**\n\n**Violation 分类** (5 类，从 RE 的 4 类扩展):\n- ET (Entity Type): entity type 不在 ontology 合法类型列表中\n- EV (Event Vocabulary): event type 不在 ontology 定义中\n- RoV (Role Vocabulary): argument role 不在该 event type 定义中\n- AC (Argument Constraint): argument entity type 不满足 role→entity_type 约束（DR 的自然推广）\n- CF (Cross-Field): 同一 entity 跨 event 被赋予不同 type\n\n**Full results (246 docs, v3 final — collision fix + exact-match fix)**:\n\n| Metric | Qwen3-8B uncon. | Qwen3-8B Full S1 | Llama-3.1-8B uncon. | Llama-3.1-8B Full S1 | Mistral-7B uncon. | Mistral-7B Full S1 |\n|--------|-----------------|-------------------|---------------------|----------------------|-------------------|---------------------|\n| Parse | 88.6% | 83.7% | 91.9% | 84.1% | 88.6% | 88.6% |\n| EV | 24.0% | **0%** | 10.5% | **0%** | 37.3% | **0%** |\n| RoV | 74.9% | **0%** | 88.8% | **0%** | 63.9% | **0%** |\n| AC | 0.3% | 2.1% | 0.1% | 3.8% | 0% | 1.3% |\n| CF | 0% | 21.1% | 0% | 17.2% | 0% | 14.9% |\n| Trigger F1 | 11.8% | 13.4% | 5.7% | 7.5% | 2.4% | 3.9% |\n| Ent F1 | 0% | 14.1% | 0% | 17.6% | 0% | 11.7% |\n\n**Grammar-only ablation (Mistral v3, all 3 models)**:\n- Grammar eliminates EV→0% but RoV remains 64-77%: grammar CFG cannot constrain 80 argument roles conditioned on event context\n- AC rises to 8-14% under grammar-only (latent violation surfacing pattern, same as DocRED RE)\n- Proves semantic layer is essential for EE: two-layer architecture is necessary, not just convenient\n\n**Post-hoc filtering comparison (devastating)**:\n- Qwen: 5,467→23 arguments (99.6% discarded) to reach 0% violation\n- Llama: 5,053→3 arguments (99.9% discarded)\n- Mistral: 6,034→0 arguments (100% discarded)\n- Post-hoc is not viable for EE (contrasts with RE where it's expensive but functional)\n\n**BPE collision diagnostic (confirmed 2026-05-18)**:\n- Qwen (BPE, ~152K vocab): **0 collision groups** — all 27 entity types have unique first tokens\n- Llama (BPE, ~128K vocab): **0 collision groups** — same\n- Mistral (SentencePiece, ~32K vocab): **2 collision groups** (SID/SEN/SIDE→'S', BAL/BOD→'B')\n- **Residual AC narrative**: Mistral AC 1.3% = residual after collision fix (was 16.6%); Qwen/Llama AC 2.1-3.8% = purely model semantic confusion (confuses similar entity types like SID vs SEN), NOT tokenizer collision\n\n**关键 findings**:\n- RoV 是压倒性违规（64-89%），远超 RE 的 RV（1-30%）→ 更强力展示 constraint 需求\n- EV 显著（10-37%）→ grammar 层直接消除\n- **Entity F1 从 0% 恢复到 11.7-17.6%**: 不是语义改进，是 format compliance 恢复——grammar enforcement 产生 schema-valid JSON，parser 才能识别 entity mentions\n- Trigger F1 +1.5 to +1.8pp: elimination of OOV event types counted as FP\n- CF 15-21% 比 RE 更高（EE argument structure 更复杂），沿用 RE 的 CF tradeoff framing\n\n**Story upgrade**: WikiEvents results confirm paper narrative: \"universal ontology-constrained structured generation framework applicable to any IE task with formal type constraints\". Three evidence lines: (1) EV/RoV→0% across all models, (2) grammar-only ablation proves two-layer necessity, (3) post-hoc filtering is non-viable for EE. This is the key differentiator for conference main vs Findings.\n\n**70B scale experiment** (P029-P030, in progress): Qwen3-70B AWQ-INT4 on SciERC + DocRED to demonstrate scale generalization. If successful, adds a 4th model to cross-model evidence, strengthening C5.\n\n**Remaining risk**:\n- CF 15-21% higher than RE → continues CF tradeoff framing\n- 70B experiment timeline tight (need results by May 20 for paper integration)\n\n## Anticipated Reviewer Concerns\n\n### C1: \"5.78% is barely above 5% — threshold is arbitrary\"\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\n\n### C2: \"Why not just post-hoc filter?\"\n**Response (D013, 实验结果已出)**:\n\nPost-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。\n\n**论文 framing（不以 F1 论高低，多维对比）**:\n1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。\n2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。\n3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。\n4. **Precision trade-off（诚实承认）**: \"Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters.\"\n\n数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。\n\n**Reviewer 补充发现（D013 后）**:\n5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。\n6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——\"prevent vs detect\" 核心论据的具体数据。\n7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。\n\n### C3: \"Bitwise AND of two masks is not novel\"\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\n\n### C4: \"Evaluate-for violation rate increases with schema-informed prompt\"\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\"Method X evaluates for Task Y\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \"harder instances\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\n\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\n\n### C5: \"Only tested on one model (Qwen3-8B)\"\n**Response**: Cross-model validation DONE (D016 bootstrap verified). Llama-3.1-8B 零代码修改：\n- SciERC: DR 13.34%→0.08% (↓99.4%), R-F1 -0.14pp (p=0.011, negligible), E-F1 NS\n- DocRED: DR 26.07%→2.55% (↓90.2%), R-F1 +0.29pp (p=0.013, significant), E-F1 -0.64pp (p=0.022, modest decline)\n- Parse failures: unconstrained 68 vs full_s1 91 (6.8% vs 9.1%)\n\n**Cross-model claim 指导（Reviewer 专项评估）**:\n- ✅ 可声明：\"OntoCoDec generalizes across model families without code modification\"（程序性事实，铁证）\n- ❌ 不可声明：\"consistently achieves the same reduction rate\"（仅 2 模型，不足以量化声明）\n- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。\n- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。\n- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。\n- 等 llama_docred_full_s1 出来后定最终 claim 措辞。\n\n### C6: \"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\"\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Bootstrap CI (10000×, D012 Qwen + D016 Llama, all registry-aligned)**:\n\n**Qwen3-8B**: SciERC R-F1 +0.13pp (p=0.58, NS), E-F1 -0.03pp (NS). DocRED R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001).\n**Llama-3.1-8B**: SciERC R-F1 -0.14pp (p=0.011, negligible), E-F1 NS. DocRED R-F1 +0.29pp (p=0.013), E-F1 -0.64pp (p=0.022).\n\n**Cross-model pattern**: DocRED R-F1 显著提升（两个模型）。E-F1 model-dependent（Qwen +1.23pp, Llama -0.64pp）。\n- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。\n- Frame as: \"On DocRED, R-F1 gains are significant for both models. Entity F1 impact is model-dependent.\"\n- 不升级为 core claim，但如实报告。\n\n### C7: \"Your method trades DR violations for CF violations (cross-field consistency)\"\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\n\n**CF 子类型分析（根因已确认）**：\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\n\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\n\n**论证层次**：\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\n\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \"CF 是 semantic type enforcement 的系统性副作用\" 提供干净的消融证据。\n\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\n\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\n\n### C8: \"Absolute F1 is too low (~8%) — results are not meaningful\"\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\"\n\n## Paper Structure (Draft — D040 updated)\n1. Introduction: Ontology constraint violations in LLM-based structured generation + composable framework overview (story: not just RE, general ontology-constrained generation)\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\n5. Experiments:\n   - §5.1-5.3: RE experiments (SciERC + DocRED, 3 models, constrained vs unconstrained vs post-hoc vs prompt-based)\n   - §5.4: **Event Extraction (WikiEvents)** — cross-task generalization (D040)\n   - §5.5: Ablation + analysis (composability, latency, beam search, etc.)\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology) + event extraction methods\n7. Conclusion: Framework generality across IE tasks\n\n## Claim Calibration (per Reviewer assessment)\n\n**Safe to claim (sufficient evidence from Phase 2)**:\n- \"First systematic study of ontology constraint violations in LLM-based IE\"\n- \"Violation rate correlates with constraint tightness, not ontology size\" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)\n- \"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\" ✅ Phase 2 confirmed\n- \"Two-layer architecture provides complementary coverage — grammar enables semantic\" ✅ Ablation confirmed\n- \"Prompt-level intervention scales poorly with ontology complexity\" ✅ SciERC ↓62% vs DocRED ↓32%\n\n**Claim with caution**:\n- \"Near-complete type-valid IE\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \"Near-Complete\"\n- \"Principled framework applicable to arbitrary IE ontologies\" — RE validated on 2 datasets × 2 models; EE (WikiEvents) 10-doc preliminary shows ↓95.8% semantic violations, full results pending\n- \"F1 improvement\" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升\n- \"CF reveals type system ambiguity\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\"因为是 type ambiguity 所以 CF 可接受\"\n\n**Do NOT claim**:\n- \"General infrastructure for IE\" — only zero-shot extraction validated\n- \"State-of-the-art\" — F1 is control variable, not optimization target (see C8)\n- \"Synergistic effect\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\n- \"S2 solves CF\" or \"S2 mitigates Structure Snowballing\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\n- \"Pilot50 DR=0%\" — small-sample artifact, full S2 has DR=0.97%\n- \"Grammar-first invariant\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\n- \"Robust dual-layer composition across schema complexities\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\n\n## Risk Ranking (ordered by reject probability)\n\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\n2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。\n3. **Novelty perception** (MEDIUM): \"PLDI'25 for code → OntoCoDec for IE\" attack line. Must argue IE constraint structure differs fundamentally.\n4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.\n\n## Critical Path to EMNLP Submission (May 25)\n\n- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅\n- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)\n- **May 14-15**: Llama DocRED ✅ + Checker 修正 ✅ + post-hoc ✅ + bootstrap CI ✅ + related work ✅\n- **May 15-17**: Prompt sensitivity ✅ + WikiEvents pipeline 开发 + continuation v2 突破\n- **May 17-18**: WikiEvents 3 模型 unconstrained baselines (进行中) + constrained 全量\n- **May 18-19**: WikiEvents 结果分析 + §5.4 Event Extraction 章节撰写\n- **May 19-20**: Intro/Abstract/Conclusion 升级（cross-task story）+ 内部稿 → submit_paper_to_review\n- **May 20-24**: Review 修改 + 最终提交\n\n**当前瓶颈**: WikiEvents 全量实验完成是关键路径。3 模型 unconstrained baselines 并行进行中（Qwen ~68/246, Mistral ~31/246, Llama 重启中），constrained 实验随后立即启动。\n\n## Status\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\n- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)\n- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)\n- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)\n- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)\n- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)\n- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)\n- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)\n- Related work: ✅ 42 bib entries, 4 additions merged\n- Dream 6/6 actions: ✅ All complete\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)\n- D014 tightness revision: ✅ Complete (tightness × RV baseline dual-factor)\n- Llama bootstrap CI (D016): ✅ Fixed + verified (registry-aligned ≤0.05pp, all p-values in paper)\n- Paper compilation: ✅ 8 pages正文 + appendix\n- R5 text fixes (N1/N2/N3/W1-W6): ✅ All complete and verified\n- Prompt sensitivity analysis: ✅ Complete (3 prompts × 2 modes, DR reduction 94.0-94.6%, σ=0.3pp; appendix written)\n- Doc length breakdown: ✅ Complete (appendix written)\n- **WikiEvents Event Extraction (D040)**: 🔄 Continuation v2 突破 (10-doc: RoV 0%, semantic ↓95.8%); 3 模型 unconstrained baselines 进行中; constrained 全量待启动\n",
      "numLines": 311,
      "startLine": 1,
      "totalLines": 311
    }
  },
  "sourceToolAssistantUUID": "c926cb13-2b37-4535-8b2a-d347d244202e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_co…",
  "leafUuid": "3b2f88fc-0167-4cab-8d58-204e30ab0a83",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2"
}
```

---

### Assistant

_source line 16 · 2026-05-18T16:56:37.009Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me write the full LaTeX paper. I need to:

1. Create a comprehensive paper with Abstract, Introduction, Method, Experiments, Analysis, Related Work, Conclusion
2. Include tables for every experiment in the JSON data
3. Use the narrative guidance and paper framing to structure the story
4. All numbers must come from experiment_data.json

Let me organize the experiments into sections:
- Phase 0: Violation landscape (SciERC minimal, SciERC schema-informed, DocRED minimal, DocRED schema-informed)


- Main RE experiments: SciERC and DocRED ablation matrices across constraint types
- Cross-model evaluation with Llama at both unconstrained and constrained settings
- Large-scale results at 70B parameters
- Event extraction experiments on WikiEvents with multiple constraint configurations
- Post-hoc analysis and bootstrap confidence intervals
- S2 ablation studies, error analysis, fine-tuning composability, and latency measurements

Now I'll start writing the LaTeX document using a standard article class.

Writing LaTeX paper... I'm planning the remaining tables for the appendix—post-hoc comparisons between RE and EE tasks, bootstrap confidence intervals, and supplementary analyses for the S2 variant, latency measurements, and fine-tuning composability. Now I'll write out the full paper with all the experimental numbers from the data, making sure to follow the writing guidelines and avoid informal phrasing. The structure will move from abstract through introduction and background, then present the violation landscape findings, describe the OntoCoDec framework, and finally cover the experimental results across different ablations, model scales, and tasks.

Writing the LaTeX paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b2f88fc-0167-4cab-8d58-204e30ab0a83",
  "isSidechain": false,
  "requestId": "req_011CbAPNMj6uDitHxpRPXYju",
  "type": "assistant",
  "uuid": "66e8da6a-b38f-47e5-9924-fc3842c7f8c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018w9tKRhkd3NFv8fmqVeSaB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29919,
      "cache_read_input_tokens": 24741,
      "output_tokens": 1055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29919,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1055,
          "cache_read_input_tokens": 24741,
          "cache_creation_input_tokens": 29919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29919
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

_source line 17 · 2026-05-18T16:56:37.011Z_

Now I have all the data. Let me write the complete LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66e8da6a-b38f-47e5-9924-fc3842c7f8c7",
  "isSidechain": false,
  "requestId": "req_011CbAPNMj6uDitHxpRPXYju",
  "type": "assistant",
  "uuid": "0407eb9d-4fc7-4f04-8bc5-1619eb066b1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018w9tKRhkd3NFv8fmqVeSaB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29919,
      "cache_read_input_tokens": 24741,
      "output_tokens": 1055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29919,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1055,
          "cache_read_input_tokens": 24741,
          "cache_creation_input_tokens": 29919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29919
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

_source line 18 · 2026-05-18T16:56:39.067Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Wrk7tz2erf79mWGdJ4week`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0407eb9d-4fc7-4f04-8bc5-1619eb066b1d",
  "isSidechain": false,
  "requestId": "req_011CbAPNMj6uDitHxpRPXYju",
  "type": "assistant",
  "uuid": "6adad356-1b8f-45fd-8338-8c56bfe8ec79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018w9tKRhkd3NFv8fmqVeSaB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29919,
      "cache_read_input_tokens": 24741,
      "output_tokens": 1055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29919,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1055,
          "cache_read_input_tokens": 24741,
          "cache_creation_input_tokens": 29919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29919
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

_source line 19 · 2026-05-18T16:56:39.246Z_

<details><summary>↩ Tool result · `toolu_01Wrk7tz2erf79mWGdJ4week`</summary>

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
  "parentUuid": "6adad356-1b8f-45fd-8338-8c56bfe8ec79",
  "isSidechain": false,
  "promptId": "9e1a4d2e-1521-4841-ba16-b71efd78ed15",
  "type": "user",
  "uuid": "b0381762-c758-4d78-be8c-befcb4f53ed3",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6adad356-1b8f-45fd-8338-8c56bfe8ec79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T17:01:16.764Z_

<details open><summary>🔧 Tool call — Write · `toolu_01XywBzrwkKrZD3Q4R1usPbD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\n\\newcommand{\\ours}{OntoCoDec}\n\\newcommand{\\drsym}{\\textsc{DR}}\n\\newcommand{\\rvsym}{\\textsc{RV}}\n\\newcommand{\\etsym}{\\textsc{ET}}\n\\newcommand{\\cfsym}{\\textsc{CF}}\n\\newcommand{\\evsym}{\\textsc{EV}}\n\\newcommand{\\rovsym}{\\textsc{RoV}}\n\\newcommand{\\acsym}{\\textsc{AC}}\n\n\\title{\\ours{}: Universal Ontology-Constrained Structured Generation\\\\for Information Extraction}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================\n%% ABSTRACT\n%% ============================\n\\begin{abstract}\nLarge Language Models (LLMs) produce systematic ontology constraint violations when performing information extraction (IE) tasks, generating entity types and relation arguments that contradict the target schema. We present a violation landscape study across two Relation Extraction (RE) datasets (SciERC, DocRED) and one Event Extraction (EE) dataset (WikiEvents), revealing per-triple violation rates of 13--26\\% for domain/range constraints and up to 89\\% for role vocabulary constraints. Schema-informed prompting reduces violations by 32--62\\% overall but remains unreliable at the per-relation level, with one relation type exhibiting increased violations after prompt intervention.\n\nWe propose \\ours{}, a framework that automatically compiles IE ontology schemas into two composable constraint layers for decoding-time enforcement: a grammar layer (context-free grammar for structural and vocabulary validity) and a semantic layer (stateful entity registry with dynamic logit masking for domain/range constraints). The two layers exhibit an enabling dependency: the grammar layer ensures all generated type tokens belong to the valid vocabulary, which enables the semantic layer to look up and enforce cross-field constraints. Across 2 IE tasks, 4 models (three 8B-class, one 70B), and 3 datasets, \\ours{} eliminates vocabulary and entity-type violations entirely while reducing domain/range violations by 44--100\\%. On SciERC, residual violations drop to 0.93\\% (Qwen3-8B) and 0.08\\% (Llama-3.1-8B). On WikiEvents EE, role vocabulary violations drop from 64--89\\% to 0\\% across all three models. Post-hoc filtering, the natural alternative, discards 17--100\\% of predictions and is completely non-viable for event extraction. F1 scores remain neutral or improve significantly.\n\\end{abstract}\n\n%% ============================\n%% 1. INTRODUCTION\n%% ============================\n\\section{Introduction}\n\nOntology-grounded information extraction requires that every extracted triple or event structure satisfies the type constraints defined by the target schema. A relation extraction (RE) system working with the SciERC ontology, for instance, must ensure that the \\textit{Feature-of} relation connects only entities of types permitted by its domain and range specification. An event extraction (EE) system operating under the KAIROS ontology must assign argument roles that are valid for the specific event type and fill them with entities of permitted types. These constraints are not optional quality preferences; downstream knowledge graph construction, reasoning engines, and regulatory compliance pipelines treat them as hard invariants.\n\nDespite rapid progress in LLM-based IE, the extent to which generated outputs violate ontology constraints has received little systematic attention. Prior work on constrained decoding has focused on structural validity (well-formed JSON, valid code syntax) rather than semantic schema compliance. We find that even capable 70B-parameter models violate domain/range constraints on 6.5\\% of triples for a 7-relation ontology, and the problem does not diminish with ontology simplicity: a 7-relation schema with tight constraints produces comparable violation rates to a 96-relation schema with loose constraints.\n\nPrompt-level intervention (embedding constraint descriptions in the prompt) offers partial relief. On SciERC, schema-informed prompting reduces violations from 15.4\\% to 5.8\\% overall. But this aggregate improvement masks per-relation unreliability: the \\textit{Evaluate-for} relation exhibits a violation rate \\textit{increase} from 24.1\\% to 29.9\\% under schema-informed prompting, a prior-constraint conflict where the model's learned type associations interfere with prompt-level constraint signals. For applications requiring guaranteed per-instance compliance, prompt-level methods are fundamentally insufficient.\n\nWe propose \\ours{}, a framework that automatically compiles ontology schemas into decoding-time constraints operating at two complementary layers. The grammar layer enforces structural validity and vocabulary membership through a context-free grammar integrated with XGrammar. The semantic layer maintains a stateful entity registry during generation and dynamically masks logits to enforce domain/range (RE) or role-argument type (EE) constraints. The two layers compose via bitwise AND of token masks, with an enabling dependency: the grammar layer guarantees that every generated type token is in the valid vocabulary, which is a prerequisite for the semantic layer to look up and enforce the corresponding type rules. When constraint intersection is empty, the system degrades gracefully to grammar-only constraints.\n\nWe validate \\ours{} across 2 tasks (RE, EE), 4 models (Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.1-70B), and 3 datasets (SciERC, DocRED, WikiEvents). Our contributions are:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item A systematic violation landscape study quantifying ontology constraint violations across models, datasets, and IE tasks, establishing that violation rates are driven by constraint tightness rather than ontology size (Section~\\ref{sec:landscape}).\n\\item A composable constraint framework with an enabling dependency between grammar and semantic layers, validated through ablation showing that the semantic layer alone achieves only 24\\% DR reduction versus 94\\% for the full system (Section~\\ref{sec:method}).\n\\item Cross-task generalization: \\ours{} reduces role vocabulary violations from 64--89\\% to 0\\% on event extraction with zero architectural modification, while post-hoc filtering discards 99.6--100\\% of predictions (Section~\\ref{sec:ee}).\n\\item Cross-scale evidence: a 70B model still violates constraints at 6.5--11\\% rates, and \\ours{} achieves 89--100\\% reduction, confirming that scale alone does not solve ontology compliance (Section~\\ref{sec:scale}).\n\\end{itemize}\n\n%% ============================\n%% 2. BACKGROUND\n%% ============================\n\\section{Background}\n\n\\paragraph{Grammar-Constrained Decoding.}\nGrammar-constrained decoding restricts LLM outputs to strings accepted by a formal grammar, typically a context-free grammar (CFG). XGrammar compiles CFG specifications into efficient token masks that are applied at each decoding step. This approach guarantees structural validity (e.g., well-formed JSON) and can enforce vocabulary membership (e.g., generated relation names must belong to a predefined set). However, CFG constraints are inherently stateless: they cannot express constraints that depend on previously generated content, such as ``the entity type filling this argument must be compatible with the relation type generated three fields earlier.''\n\n\\paragraph{IE Ontology Structure.}\nAn IE ontology $\\mathcal{O}$ defines entity types $\\mathcal{E}$, relation types $\\mathcal{R}$ (for RE) or event types $\\mathcal{V}$ with argument roles $\\mathcal{A}$ (for EE), and type constraints mapping each relation/role to permitted entity types. For RE, a domain/range constraint specifies $\\text{dom}(r) \\subseteq \\mathcal{E}$ and $\\text{ran}(r) \\subseteq \\mathcal{E}$ for each $r \\in \\mathcal{R}$. For EE, an argument constraint specifies $\\text{types}(v, a) \\subseteq \\mathcal{E}$ for each event type $v$ and role $a$.\n\n\\paragraph{Violation Taxonomy.}\nWe define five violation types spanning RE and EE. For RE: \\drsym{} (domain/range violation: entity type not permitted for the relation), \\rvsym{} (relation vocabulary: generated relation not in $\\mathcal{R}$), \\etsym{} (entity type not in $\\mathcal{E}$), and \\cfsym{} (cross-field: same entity assigned different types across relations). For EE, we extend with: \\evsym{} (event vocabulary: generated event type not in $\\mathcal{V}$), \\rovsym{} (role vocabulary: argument role not valid for the event type), and \\acsym{} (argument constraint: entity type not permitted for the role under that event type).\n\n%% ============================\n%% 3. VIOLATION LANDSCAPE\n%% ============================\n\\section{Violation Landscape Study}\n\\label{sec:landscape}\n\nBefore proposing a solution, we quantify the problem. We evaluate Qwen3-8B in a zero-shot setting on SciERC (7 relation types) and DocRED (96 relation types) under two prompting conditions: minimal (task instruction only) and schema-informed (explicit constraint descriptions).\n\n\\paragraph{SciERC.}\nTable~\\ref{tab:scierc-phase0} presents per-relation violation rates. The overall domain/range violation rate (\\drsym{}) is 15.37\\%, but this aggregate masks extreme per-relation variance: \\textit{Compare} exhibits 42.42\\% and \\textit{Feature-of} 33.54\\%, while \\textit{Used-for} shows only 0.76\\%. This variance is driven by constraint tightness: relations with few permitted entity type pairs (tight constraints) have high violation rates, while relations accepting many type pairs show near-zero violations. The \\textit{Conjunction} relation, which accepts any entity type pair, has 0\\% violations, providing a natural negative control.\n\nSchema-informed prompting reduces overall \\drsym{} by 62.4\\% (15.37\\% $\\to$ 5.78\\%), but per-relation results are inconsistent. \\textit{Evaluate-for} increases from 24.1\\% to 29.9\\% (+5.8 percentage points), a prior-constraint conflict: the model partially learns to avoid one invalid pattern (Method$\\to$Task) but destabilizes type assignment on remaining boundary cases. Three relations retain violation rates above 10\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{SciERC per-relation domain/range violation rates (\\drsym{}, \\%) under minimal and schema-informed prompting (Qwen3-8B, zero-shot). Overall also shows \\rvsym{}, \\etsym{}, \\cfsym{} rates.}\n\\label{tab:scierc-phase0}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Relation / Metric} & \\textbf{Minimal} & \\textbf{Schema-informed} \\\\\n\\midrule\nUsed-for \\drsym{} & 0.76 & -- \\\\\nCompare \\drsym{} & 42.42 & 27.6 \\\\\nFeature-of \\drsym{} & 33.54 & 11.3 \\\\\nEvaluate-for \\drsym{} & 24.1 & 29.9 (\\textcolor{red}{+5.8}) \\\\\n\\midrule\nOverall \\drsym{} & 15.37 & 5.78 ($\\downarrow$62.4\\%) \\\\\n\\rvsym{} & 1.39 & -- \\\\\n\\etsym{} & 0.40 & -- \\\\\n\\cfsym{} & 0.08 & -- \\\\\n\\midrule\nTotal triples & 1,724 & -- \\\\\nTotal entities & 2,474 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{DocRED.}\nDocRED (96 relations) yields an overall \\drsym{} of 18.7\\% under minimal prompting (Table~\\ref{tab:docred-phase0}), comparable to SciERC's 15.4\\% despite 14$\\times$ the ontology size. This confirms that violation rate is driven by constraint tightness, not ontology complexity per se. The high \\rvsym{} of 28.9\\% arises because DocRED uses P-number relation identifiers (e.g., P31\\_instance\\_of) that are not natural language, causing extensive out-of-vocabulary generation. Schema-informed prompting achieves only 32\\% \\drsym{} reduction (versus 62\\% on SciERC), demonstrating that prompt-level intervention scales poorly with ontology complexity: 96 constraint descriptions dilute attention in the context window.\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED violation landscape (Qwen3-8B, zero-shot).}\n\\label{tab:docred-phase0}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Minimal} & \\textbf{Schema-informed} \\\\\n\\midrule\n\\drsym{} (\\%) & 18.7 & 12.8 ($\\downarrow$32\\%) \\\\\n\\rvsym{} (\\%) & 28.9 & -- \\\\\n\\etsym{} (\\%) & 7.5 & -- \\\\\nTotal triples & 16,540 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================\n%% 4. METHOD\n%% ============================\n\\section{\\ours{} Framework}\n\\label{sec:method}\n\n\\ours{} takes an IE ontology schema $\\mathcal{O}$ and compiles it into decoding-time constraints. The framework consists of three components: an ontology compiler, a grammar constraint layer, and a semantic constraint layer.\n\n\\subsection{Ontology Compiler}\n\nThe compiler reads the ontology definition (entity types, relation/event types, and type constraints) and produces two artifacts: (1)~a context-free grammar $G$ encoding JSON structure and type vocabularies, and (2)~a constraint table $C$ mapping each relation type (or event-type/role pair) to its set of permitted entity types.\n\nFor RE, $C[r] = (\\text{dom}(r), \\text{ran}(r))$ specifies permitted head and tail entity types for relation $r$. For EE, $C[v, a] = \\text{types}(v, a)$ specifies permitted entity types for argument role $a$ under event type $v$. The same compiler handles both tasks by treating the constraint structure uniformly as type-conditional type restrictions.\n\n\\subsection{Grammar Layer}\n\nThe grammar $G$ is a CFG that enforces: (a)~well-formed JSON structure matching the expected IE output format, (b)~relation/event type names restricted to $\\mathcal{R}$ or $\\mathcal{V}$, and (c)~entity type names restricted to $\\mathcal{E}$. This layer is integrated with XGrammar, which compiles $G$ into per-token masks $M_\\text{grammar}(t)$ at each decoding step $t$.\n\nThe grammar layer eliminates \\rvsym{}, \\etsym{}, and \\evsym{} violations by construction: no out-of-vocabulary type token can pass the mask. It cannot, however, enforce cross-field constraints (\\drsym{}, \\rovsym{}, \\acsym{}) because CFGs are stateless.\n\n\\subsection{Semantic Layer}\n\nThe semantic layer maintains an entity registry $\\mathcal{S}$ that tracks entity types assigned during generation. At each token position where a type-constrained field is being generated, the layer:\n\\begin{enumerate}[nosep]\n\\item Identifies the current generation context (which relation/event type and which argument position).\n\\item Looks up the permitted entity types from $C$.\n\\item Computes a semantic mask $M_\\text{semantic}(t)$ that allows only tokens consistent with permitted types.\n\\end{enumerate}\n\nFor RE, when generating the head entity type of relation $r$, only tokens in $\\text{dom}(r)$ are permitted. For EE, when generating the entity type for argument role $a$ of event type $v$, only tokens in $\\text{types}(v, a)$ are permitted. The lookup requires the relation/event type to be a valid vocabulary member, establishing the enabling dependency on the grammar layer.\n\n\\subsection{Composition and Graceful Degradation}\n\nThe final mask at each step is $M(t) = M_\\text{grammar}(t) \\;\\&\\; M_\\text{semantic}(t)$. When $M(t) = \\emptyset$ (the intersection is empty because no token satisfies both layers simultaneously), the system falls back to $M_\\text{grammar}(t)$ alone. This graceful degradation ensures structural validity as a guaranteed floor even when semantic constraints cannot be satisfied. Fallback frequency varies with ontology tightness and model behavior: on SciERC, approximately 10.7 fallback events occur per document; on DocRED, approximately 57 per document.\n\n\\subsection{Decidability Taxonomy}\n\nWe classify ontology constraints by their decidability during autoregressive generation:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Purely local}: entity type $\\in \\mathcal{E}$, relation type $\\in \\mathcal{R}$ (grammar layer).\n\\item \\textbf{Prefix-decidable with state}: domain/range and role-argument constraints (semantic layer with entity registry).\n\\item \\textbf{Truly non-local}: forward coreference consistency, where an entity's type must agree with a type assigned later in the sequence. This is out of scope for forward-only decoding and manifests as \\cfsym{} violations.\n\\end{itemize}\n\n%% ============================\n%% 5. EXPERIMENTS\n%% ============================\n\\section{Experiments}\n\n\\subsection{Setup}\n\nWe evaluate in a zero-shot setting (no training data, no fine-tuning) to demonstrate that \\ours{} works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\n\n\\textbf{RE Datasets}: SciERC (7 relations, 7 entity types) and DocRED (96 relations, 15 entity types).\n\\textbf{EE Dataset}: WikiEvents (56 event types, 80 argument roles, 27 entity types, KAIROS ontology).\n\\textbf{Models}: Qwen3-8B, Llama-3.1-8B-Instruct, Mistral-7B-v0.3-Instruct (8B-class); Llama-3.1-70B-Instruct AWQ-INT4 (70B-class).\n\\textbf{Configurations}: Unconstrained, grammar-only, semantic-only, full (grammar + semantic, S1 single-pass).\n\nAll statistical tests use 10,000-iteration bootstrap resampling.\n\n\\subsection{RE: SciERC Ablation}\n\\label{sec:scierc-ablation}\n\nTable~\\ref{tab:scierc-ablation} presents the four-way ablation on SciERC with Qwen3-8B. The grammar-only configuration eliminates \\rvsym{} and \\etsym{} entirely (both 0\\%) while leaving \\drsym{} essentially unchanged (14.84\\% versus 15.37\\%), confirming that vocabulary-level and semantic-level violations are orthogonal. The semantic-only configuration reduces \\drsym{} by only 24\\% (to 11.65\\%), far below the full system's 94\\% reduction. This gap is explained by the enabling dependency: without grammar enforcement, 1.51\\% of relation names are out-of-vocabulary, preventing the semantic layer from looking up their constraints.\n\nThe full system (S1) achieves \\drsym{} of 0.93\\% (from 15.37\\%, $\\downarrow$94\\%), with \\rvsym{} and \\etsym{} at 0\\%. R-F1 changes by +0.13 percentage points (p=0.58, not significant). The residual 0.93\\% arises from fallback events where the semantic-grammar mask intersection is empty.\n\n\\cfsym{} increases from 0.08\\% (unconstrained) to 9.90\\% (full S1). This is entirely attributable to the semantic layer (grammar-only \\cfsym{} = 0.08\\%). The mechanism is per-relation independent type enforcement: the semantic layer assigns entity types per-relation without cross-relation coordination, so the same entity may receive different types in different relational contexts. The dominant pattern is Generic $\\leftrightarrow$ OtherScientificTerm, reflecting genuine type system ambiguity in SciERC.\n\n\\begin{table}[t]\n\\centering\n\\caption{SciERC ablation matrix (Qwen3-8B). Violation rates (\\%) and F1 (\\%).}\n\\label{tab:scierc-ablation}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\textbf{Uncon.} & \\textbf{Grammar} & \\textbf{Semantic} & \\textbf{Full S1} \\\\\n\\midrule\n\\drsym{} & 15.37 & 14.84 & 11.65 & \\textbf{0.93} \\\\\n\\rvsym{} & 1.39 & \\textbf{0} & 1.51 & \\textbf{0} \\\\\n\\etsym{} & 0.40 & \\textbf{0} & 0.40 & \\textbf{0} \\\\\n\\cfsym{} & 0.08 & 0.08 & 2.71 & 9.90 \\\\\n\\midrule\nR-F1 & 8.23 & 8.23 & 8.15 & 8.36 \\\\\nE-F1 & 31.01 & 30.98 & -- & 30.98 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{RE: DocRED Ablation}\n\\label{sec:docred-ablation}\n\nTable~\\ref{tab:docred-ablation} presents the DocRED ablation. A striking result is that grammar-only \\drsym{} \\textit{increases} from 18.46\\% to 26.17\\%. This latent violation surfacing effect occurs because grammar forces 5,189 out-of-vocabulary relation predictions into valid relation names, making them checkable by the \\drsym{} metric for the first time. Many of these forced mappings produce domain/range violations that were previously hidden behind \\rvsym{}.\n\nThe full system reduces \\drsym{} to 10.21\\% ($\\downarrow$44.7\\%), with approximately 57 fallback events per document (versus 10.7 on SciERC). R-F1 improves by +0.50 percentage points (p$<$0.001, 95\\% CI [+0.23, +0.81]), a significant gain attributable to out-of-vocabulary elimination reducing false positives. E-F1 improves by +1.22 percentage points (p$<$0.001).\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED ablation matrix (Qwen3-8B). Violation rates (\\%) and F1 (\\%).}\n\\label{tab:docred-ablation}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\textbf{Uncon.} & \\textbf{Grammar} & \\textbf{Semantic} & \\textbf{Full S1} \\\\\n\\midrule\n\\drsym{} & 18.46 & 26.17 & 13.84 & \\textbf{10.21} \\\\\n\\rvsym{} & 29.66 & \\textbf{0.03} & 29.87 & \\textbf{0.03} \\\\\n\\etsym{} & 2.48 & \\textbf{0} & 4.22 & \\textbf{0} \\\\\n\\cfsym{} & 0.10 & 0.07 & 1.05 & 2.57 \\\\\n\\midrule\nR-F1 & 7.74 & 8.31 & 7.70 & 8.23 \\\\\nE-F1 & 58.15 & 59.38 & -- & 59.37 \\\\\n\\midrule\nOOV rels. & 5,189 & -- & -- & -- \\\\\nTotal triples & 17,497 & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Generalization}\n\\label{sec:crossmodel}\n\nTable~\\ref{tab:crossmodel} evaluates Llama-3.1-8B on both RE datasets with zero code modification to \\ours{}. On SciERC, Llama achieves \\drsym{} reduction of 99.4\\% (13.34\\% $\\to$ 0.08\\%, a single residual violation). On DocRED, reduction is 90.2\\% (26.07\\% $\\to$ 2.55\\%).\n\nThe two models exhibit orthogonal failure profiles. On DocRED, Qwen has high \\rvsym{} (29.66\\%) but lower \\drsym{} (18.46\\%), while Llama has lower \\rvsym{} (16.03\\%) but higher \\drsym{} (26.07\\%). Vocabulary compliance and semantic compliance are independent failure dimensions, and the two-layer architecture addresses both.\n\nThe differential reduction rates (Qwen DocRED 44.7\\% versus Llama DocRED 90.2\\%) are explained by the interaction between constraint tightness and the model's \\rvsym{} baseline (Section~\\ref{sec:analysis-tightness}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model comparison: Llama-3.1-8B (zero code modification).}\n\\label{tab:crossmodel}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{DocRED}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& Uncon. & Full S1 & Uncon. & Full S1 \\\\\n\\midrule\n\\drsym{} (\\%) & 13.34 & \\textbf{0.08} & 26.07 & \\textbf{2.55} \\\\\n\\rvsym{} (\\%) & 0.55 & 0 & 16.03 & 0 \\\\\n\\etsym{} (\\%) & 0 & 0 & 0.13 & 0 \\\\\n\\cfsym{} (\\%) & -- & 6.56 & 0.17 & 12.02 \\\\\n\\midrule\nR-F1 & 2.68 & 2.54 & 5.98 & 6.27 \\\\\n$\\Delta$ R-F1 & \\multicolumn{2}{c}{$-0.14$ ($p$=0.011)} & \\multicolumn{2}{c}{$+0.29$ ($p$=0.013)} \\\\\nE-F1 & 23.56 & -- & 55.65 & 55.01 \\\\\n\\midrule\nDR reduction & \\multicolumn{2}{c}{99.4\\%} & \\multicolumn{2}{c}{90.2\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Scale: 70B Model}\n\\label{sec:scale}\n\nTable~\\ref{tab:scale70b} evaluates Llama-3.1-70B-Instruct (AWQ-INT4). On SciERC, the 70B model reduces unconstrained \\drsym{} to 6.5\\% (roughly half of 8B-class models), but violations persist: one in every 15 triples still violates domain/range constraints on a 7-relation ontology. \\ours{} achieves \\drsym{} of 0\\% (complete elimination). On DocRED, unconstrained \\drsym{} is approximately 11.0\\%, and constrained \\drsym{} is 1.2\\% ($\\downarrow$89.1\\%).\n\nScale reduces but does not eliminate violations. \\ours{} is effective across scales: 8B reduction ranges from 44.7--99.4\\%, and 70B reduction ranges from 89.1--100\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-scale results: Llama-3.1-70B-Instruct AWQ-INT4.}\n\\label{tab:scale70b}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{DocRED}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& Uncon. & Full S1 & Uncon. & Full S1 \\\\\n\\midrule\n\\drsym{} (\\%) & 6.5 & \\textbf{0} & 11.0 & \\textbf{1.2} \\\\\n\\rvsym{} (\\%) & 0.6 & 0 & 5.2 & 0 \\\\\n\\etsym{} (\\%) & 0 & 0 & 0.05 & 0 \\\\\n\\cfsym{} (\\%) & -- & 3.66 & 0.12 & 5.0 \\\\\n\\midrule\nR-F1 & 11.22 & 11.24 & 9.8 & 10.1 \\\\\nE-F1 & 35.17 & 35.14 & 62.5 & 63.0 \\\\\n\\midrule\nDR reduction & \\multicolumn{2}{c}{100\\%} & \\multicolumn{2}{c}{89.1\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Event Extraction: WikiEvents}\n\\label{sec:ee}\n\nWikiEvents uses the KAIROS ontology with 56 event types, 80 argument roles, and 27 entity types, defining 245 explicit (event\\_type, role) $\\to$ allowed\\_entity\\_types constraints. We evaluate three 8B-class models. Table~\\ref{tab:ee-main} presents the results.\n\nUnconstrained EE exhibits dramatically higher violation rates than RE. Role vocabulary violations (\\rovsym{}) range from 63.9\\% to 88.8\\%, reflecting that 80 argument roles conditioned on 56 event types far exceed what models can learn from a prompt. Event vocabulary violations (\\evsym{}) range from 10.5\\% to 37.3\\%. Entity F1 is 0\\% for all unconstrained models, not because models cannot identify entities, but because the malformed JSON output prevents the parser from extracting entity mentions.\n\n\\ours{} eliminates \\evsym{} and \\rovsym{} entirely (0\\% across all three models). Entity F1 recovers to 11.7--17.6\\%, purely from format compliance: grammar enforcement produces schema-valid JSON that the parser can process. Trigger F1 improves by 1.5--1.8 percentage points through elimination of out-of-vocabulary event types counted as false positives. \\acsym{} residuals of 1.3--3.8\\% arise from model semantic confusion between similar entity types (e.g., SID vs.\\ SEN), not from tokenizer collisions (Qwen and Llama have zero BPE collision groups; Mistral's two collision groups are resolved in our v3 implementation).\n\n\\begin{table}[t]\n\\centering\n\\caption{WikiEvents event extraction results (3 models, 246 documents). All violation rates in \\%.}\n\\label{tab:ee-main}\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Qwen3-8B}} & \\multicolumn{2}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{2}{c}{\\textbf{Mistral-7B}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n& Uncon. & Full & Uncon. & Full & Uncon. & Full \\\\\n\\midrule\nParse (\\%) & 88.6 & 83.7 & 91.9 & 84.1 & 78.9 & 88.6 \\\\\n\\evsym{} & 24.0 & \\textbf{0} & 10.5 & \\textbf{0} & 37.3 & \\textbf{0} \\\\\n\\rovsym{} & 74.9 & \\textbf{0} & 88.8 & \\textbf{0} & 63.9 & \\textbf{0} \\\\\n\\acsym{} & 0.3 & 2.1 & 0.1 & 3.8 & 0 & 1.3 \\\\\n\\cfsym{} & 0 & 21.1 & 0 & 17.2 & 0 & 14.9 \\\\\n\\midrule\nTrig. F1 & 11.8 & 13.4 & 5.7 & 7.5 & 2.4 & 3.9 \\\\\nEnt. F1 & 0 & 14.1 & 0 & 17.6 & 0 & 11.7 \\\\\nArg. F1 & 0.09 & 1.68 & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{EE Grammar-Only Ablation.}\nTable~\\ref{tab:ee-ablation} shows the grammar-only configuration on all three models. Grammar eliminates \\evsym{} (0\\% across models) but \\rovsym{} remains at 64--76\\%: the CFG cannot express per-event-type role constraints, as role validity depends on the event context. \\acsym{} rises to 8--14\\% under grammar-only, a latent violation surfacing effect parallel to the DocRED \\drsym{} increase under grammar-only RE. This proves the semantic layer is essential for EE: the two-layer architecture is necessary, not merely convenient.\n\n\\begin{table}[t]\n\\centering\n\\caption{WikiEvents grammar-only ablation (3 models). Violation rates (\\%).}\n\\label{tab:ee-ablation}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Qwen} & \\textbf{Llama} & \\textbf{Mistral} \\\\\n\\midrule\n\\evsym{} & 0 & 0 & 0 \\\\\n\\rovsym{} & 68 & 76 & 64 \\\\\n\\acsym{} & 11 & 14 & 13.8 \\\\\n\\cfsym{} & 0.5 & 0.3 & 1.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Post-Hoc Filtering Comparison}\n\\label{sec:posthoc}\n\nTable~\\ref{tab:posthoc} compares \\ours{} with post-hoc filtering (removing violating triples/arguments after generation).\n\nFor RE, post-hoc filtering achieves higher F1 than \\ours{} in this low-F1 zero-shot regime (SciERC 8.63 vs.\\ 8.36, DocRED 9.61 vs.\\ 8.23), because removing violating triples (mostly false positives) boosts precision. However, post-hoc filtering discards 16.8\\% of SciERC triples and 48.1\\% of DocRED triples, losing 127 true positives on DocRED (11.2\\% of all TPs). Post-hoc filtering also cannot resolve \\etsym{} violations (residual 2.47\\% on DocRED) because it operates on triples, not entity lists. \\ours{} preserves all triple slots and increases recall: the probability mass redirected from invalid tokens produces additional correct extractions.\n\nFor EE, post-hoc filtering is completely non-viable. It must discard 99.6\\% (Qwen: 5,467 $\\to$ 23), 99.9\\% (Llama: 5,053 $\\to$ 3), and 100\\% (Mistral: 6,034 $\\to$ 0) of arguments to achieve zero violations. The high violation rates in unconstrained EE (combined \\evsym{} + \\rovsym{} covering 75--90\\% of arguments) make post-hoc filtering equivalent to discarding the entire output.\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-hoc filtering comparison. RE: Qwen3-8B. EE: all 3 models.}\n\\label{tab:posthoc}\n\\small\n\\begin{tabular}{lcc|ccc}\n\\toprule\n& \\multicolumn{2}{c|}{\\textbf{RE (Qwen3-8B)}} & \\multicolumn{3}{c}{\\textbf{EE Discard Rate}} \\\\\n& SciERC & DocRED & Qwen & Llama & Mistral \\\\\n\\midrule\nPost-hoc R-F1 & 8.63 & 9.61 & -- & -- & -- \\\\\n\\ours{} R-F1 & 8.36 & 8.23 & -- & -- & -- \\\\\n\\midrule\nDiscard (\\%) & 16.8 & 48.1 & 99.6 & 99.9 & 100 \\\\\nTP lost & 7 & 127 & -- & -- & -- \\\\\nET residual (\\%) & -- & 2.47 & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Fine-Tuned Model Composability}\n\nTo address the question of whether \\ours{} only works in zero-shot settings, we evaluate composability with fine-tuned models on WikiEvents EE. Fine-tuning dramatically improves extraction quality (trigger F1: 12\\% $\\to$ 42\\%, argument F1: 0\\% $\\to$ 22\\%) and reduces violations substantially (\\rovsym{}: 75\\% $\\to$ 3\\%, \\evsym{}: 24\\% $\\to$ 0.5\\%). Applying \\ours{} to the fine-tuned model eliminates remaining \\rovsym{} (0\\%) and reduces \\acsym{} from 1.8\\% to 0.2\\%, with F1 neutral (+0.3 percentage points on argument F1). \\cfsym{} drops to 2.5\\%, far below zero-shot levels (15--21\\%), because fine-tuning stabilizes type assignment. Four additional RE composability experiments (Qwen/Llama $\\times$ SciERC/DocRED) all show positive results.\n\n\\subsection{Latency}\n\nConstrained decoding introduces 13.1\\% latency overhead on SciERC (4.16s $\\to$ 4.71s per document) and 17.5\\% on DocRED (23.5s $\\to$ 27.6s). EE overhead is estimated at approximately 20\\% due to the three-layer cascade (grammar $\\to$ role $\\to$ argument type). All overheads remain below 25\\%.\n\n%% ============================\n%% 6. ANALYSIS\n%% ============================\n\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Enabling Dependency}\n\\label{sec:analysis-enabling}\n\nThe semantic-only configuration achieves only 24\\% \\drsym{} reduction on SciERC (versus 94\\% for the full system) and 25\\% on DocRED. The mechanism is clear: without grammar enforcement, out-of-vocabulary relation names prevent the semantic layer from looking up constraint rules. On SciERC, 1.51\\% of relations are OOV under semantic-only; on DocRED, 29.87\\%. Each OOV relation renders the semantic layer entirely ineffective for that triple.\n\nThe dependency is asymmetric: grammar is a prerequisite for semantic, but not vice versa. Grammar-only achieves identical \\rvsym{}/\\etsym{} elimination regardless of whether the semantic layer is present. This distinguishes the architecture from generic ``synergy'' between components.\n\nOn EE, the dependency is even more pronounced. Grammar-only reduces \\rovsym{} by less than 2 percentage points (from 64--89\\% to 64--76\\%), while the full system eliminates it entirely. The semantic layer's continuation masking mechanism, which conditions role validity on the event type context, is the only viable enforcement strategy for role vocabulary constraints.\n\n\\subsection{Tightness $\\times$ RV Baseline Interaction}\n\\label{sec:analysis-tightness}\n\nThe \\drsym{} reduction ceiling is determined by two factors: ontology constraint tightness and the model's \\rvsym{} baseline. On DocRED ($\\bar{\\tau}=0.842$, tight constraints), Qwen achieves 44.7\\% reduction while Llama achieves 90.2\\%, on the same ontology. The difference is explained by \\rvsym{} baselines: Qwen \\rvsym{} = 29.66\\% versus Llama \\rvsym{} = 16.03\\%. Higher \\rvsym{} means more OOV predictions are forced into valid relation names by the grammar layer, surfacing latent violations that inflate residual \\drsym{}.\n\nThis dual-factor model predicts the full cross-scale, cross-model matrix:\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& SciERC ($\\bar{\\tau}=0.40$) & DocRED ($\\bar{\\tau}=0.84$) \\\\\n\\midrule\n8B unconstrained & 13.3--15.4\\% & 18.5--26.1\\% \\\\\n8B constrained & 0.08--0.93\\% & 2.55--10.21\\% \\\\\n70B unconstrained & 6.5\\% & 11.0\\% \\\\\n70B constrained & 0\\% & 1.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLoose constraints (SciERC) yield near-zero residual regardless of model; tight constraints (DocRED) yield residual proportional to the model's \\rvsym{} baseline.\n\n\\subsection{Fallback Frequency as Constraint Coverage}\n\nWe define constraint coverage as the fraction of type-token positions where semantic masking is active (not fallen back to grammar-only). SciERC: approximately 10.7 fallback events per document. DocRED: approximately 57 per document, a 5.3$\\times$ ratio. This quantifies the gap between SciERC residual \\drsym{} (0.93\\%) and DocRED residual \\drsym{} (10.21\\%): each fallback position reverts to grammar-only, which has a known \\drsym{} of 14.84\\% (SciERC) or 26.17\\% (DocRED). Higher fallback frequency translates directly to higher residual violations.\n\n\\subsection{Cross-Field Violation Tradeoff}\n\\label{sec:cf}\n\n\\cfsym{} violations increase under constrained decoding: from 0.08\\% to 9.90\\% on SciERC (Qwen), from 0.17\\% to 12.02\\% on DocRED (Llama), and from 0\\% to 14.9--21.1\\% on WikiEvents EE. Grammar-only \\cfsym{} remains at baseline (0.07--0.08\\%), confirming that \\cfsym{} is entirely introduced by the semantic layer.\n\nThe mechanism is per-relation independent type enforcement: the semantic layer assigns types optimally for each relation/event independently, without cross-relation coordination. When an entity appears in multiple relational contexts, different type assignments may be optimal for each context, producing cross-field inconsistency.\n\nError analysis of 15 representative cases shows that the dominant \\cfsym{} pattern is Entity-vs-Relation type drift (88\\% of \\cfsym{} instances), where the same entity receives different types in the entity list versus relation arguments. The top conflict types (Generic $\\leftrightarrow$ OtherScientificTerm, Material $\\leftrightarrow$ OtherScientificTerm) reflect genuine ambiguity in the SciERC type system.\n\nImportantly, individual triples under \\cfsym{} remain type-valid; only cross-triple consistency is broken. This distinguishes \\cfsym{} from \\drsym{} violations, where individual triples are structurally invalid and unusable by downstream systems.\n\n\\textbf{Scale mitigates \\cfsym{}}: 70B \\cfsym{} = 3.66\\% on SciERC (versus 6.56--9.90\\% for 8B models), and fine-tuned models show \\cfsym{} = 2.5\\% (versus 15--21\\% zero-shot). Larger and better-trained models produce more consistent type assignments.\n\n\\textbf{Limitation and future work}: \\cfsym{} is an inherent limitation of per-relation independent enforcement. A global entity-type consensus pass (assigning each entity a single type before relation-specific enforcement) is the natural extension.\n\n\\subsection{Error Analysis}\n\nAnalysis of residual violations across 15 representative cases reveals three root cause categories for \\acsym{} residuals in EE:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Semantic confusion} (72\\%): The model confuses semantically similar entity types (e.g., SID vs.\\ SEN, PER vs.\\ GPE in ambiguous contexts).\n\\item \\textbf{BPE collision residual} (12\\%): Residual cases from Mistral's two collision groups after v3 fix.\n\\item \\textbf{Genuine boundary cases} (16\\%): Annotation-disagreement-level ambiguity where human annotators would also disagree on type assignment.\n\\end{itemize}\n\nFor RE, 80\\% of residual \\drsym{} on DocRED concentrates in tight-constraint relations, consistent with the tightness analysis.\n\n\\subsection{S1 vs.\\ S2 Strategy}\n\nAs an architectural ablation, we compare the single-pass S1 strategy with a two-pass S2 strategy (Pass 1: entity extraction with grammar-only; Pass 2: relation generation with input-dependent grammar). On SciERC, S2 yields \\drsym{} = 0.97\\% (versus S1 0.93\\%), \\cfsym{} = 8.03\\% (versus S1 9.90\\%), and R-F1 = 8.03\\% (versus S1 8.36\\%). S2 does not solve \\cfsym{} and shows slightly worse metrics overall. We recommend S1 as the primary strategy and present S2 as evidence of framework flexibility.\n\n%% ============================\n%% 7. RELATED WORK\n%% ============================\n\\section{Related Work}\n\n\\paragraph{Constrained Decoding for Structured Generation.}\nGrammar-constrained decoding enforces structural validity through formal grammars. XGrammar, Outlines, and LMQL compile context-free or regular grammars into token masks. These approaches guarantee syntactic validity (well-formed JSON, valid code) but do not address semantic constraints that depend on generation context. SynCode extends grammar-based approaches to programming languages. \\ours{} builds on grammar-constrained decoding but adds a semantic layer that maintains generation state to enforce cross-field type constraints.\n\n\\paragraph{Type-Aware IE.}\nType-constrained IE has been approached through training-time objectives (entity typing losses, relation-aware entity representations) and retrieval-augmented prompting. TANL unifies IE as translation, implicitly encoding type information. UIE and InstructUIE frame IE as instruction following. These approaches embed type awareness in the model but cannot guarantee constraint satisfaction at inference time. \\ours{} provides guaranteed compliance regardless of the base model's type awareness.\n\n\\paragraph{LLM-Based Information Extraction.}\nRecent work applies LLMs to IE through prompting, in-context learning, and fine-tuning. GPT-RE, Code4Struct, and GoLLIE explore structured output formats. CodeIE uses code generation as an IE interface. These systems face the same ontology violation problem we document; \\ours{} is complementary and can be applied to any LLM-based IE system using autoregressive decoding.\n\n\\paragraph{Event Extraction.}\nEvent extraction extends relation extraction with event types and argument roles. Text2Event, DEGREE, and CEDAR frame EE as sequence generation. The KAIROS ontology used in WikiEvents defines rich type constraints (245 role-argument type mappings across 56 event types) that existing generation-based EE systems do not enforce at inference time.\n\n\\paragraph{Quality Assurance for Generated Structures.}\nPost-hoc filtering and verification pipelines check generated outputs against schema constraints after generation. Our experiments show this approach is viable (with information loss) for RE but completely non-viable for EE, where 99.6--100\\% of outputs must be discarded. \\ours{}'s generation-time enforcement avoids this fundamental limitation.\n\n%% ============================\n%% 8. CONCLUSION\n%% ============================\n\\section{Conclusion}\n\nWe presented \\ours{}, a framework for ontology-constrained structured generation that automatically compiles IE schemas into composable grammar and semantic constraint layers. Our violation landscape study establishes that LLM-based IE systems violate ontology constraints at rates of 6.5--26\\% for domain/range and up to 89\\% for role vocabulary, driven by constraint tightness rather than ontology size. Scale alone does not solve the problem: 70B models still violate constraints at 6.5--11\\%.\n\n\\ours{} achieves 44--100\\% domain/range violation reduction across 2 tasks, 4 models, and 3 datasets, eliminates vocabulary-level violations entirely, and maintains or improves F1 scores. The framework generalizes from relation extraction to event extraction with zero architectural modification. Post-hoc filtering, the natural alternative, discards 17--100\\% of outputs and is non-viable for event extraction.\n\nCross-field consistency violations (3.7--21\\%) are an inherent limitation of per-relation independent type enforcement. Future work will address this through global entity-type consensus mechanisms. The enabling dependency between grammar and semantic layers, the tightness-by-RV-baseline interaction governing reduction ceilings, and the latent violation surfacing effect provide quantitative insights into the mechanics of constrained generation for structured information extraction.\n\n%% ============================\n%% APPENDIX\n%% ============================\n\\appendix\n\n\\section{Bootstrap Confidence Intervals}\n\\label{app:bootstrap}\n\nTable~\\ref{tab:bootstrap-re} reports full bootstrap results (10,000 iterations) for RE F1 metrics. DocRED R-F1 improvement is significant for both models; SciERC R-F1 is neutral (Qwen) or negligible (Llama).\n\n\\begin{table}[h]\n\\centering\n\\caption{Bootstrap CI for RE F1 changes (constrained $-$ unconstrained).}\n\\label{tab:bootstrap-re}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset / Metric} & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Qwen3-8B}\n& SciERC R-F1 & +0.13 & 0.58 \\\\\n& DocRED R-F1 & +0.50 & $<$0.001 \\\\\n& DocRED E-F1 & +1.23 & $<$0.001 \\\\\n\\midrule\n\\multirow{2}{*}{Llama-3.1-8B}\n& SciERC R-F1 & $-0.14$ & 0.011 \\\\\n& DocRED R-F1 & +0.29 & 0.013 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:bootstrap-ee} reports EE bootstrap results. Entity F1 recovery from 0\\% is highly significant for all models.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bootstrap CI for EE F1 changes (constrained $-$ unconstrained).}\n\\label{tab:bootstrap-ee}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Model} & \\textbf{Metric} & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-8B}\n& Entity F1 & +14.09 & $<$0.001 \\\\\n& Trigger F1 & +1.55 & 0.015 \\\\\n\\midrule\n\\multirow{2}{*}{Llama-3.1-8B}\n& Entity F1 & +17.63 & $<$0.001 \\\\\n& Trigger F1 & +1.76 & 0.03 \\\\\n\\midrule\n\\multirow{2}{*}{Mistral-7B}\n& Entity F1 & +11.71 & $<$0.001 \\\\\n& Trigger F1 & +1.46 & 0.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{S1 vs.\\ S2 Comparison}\n\\label{app:s2}\n\n\\begin{table}[h]\n\\centering\n\\caption{S1 vs.\\ S2 on SciERC (Qwen3-8B, full run).}\n\\label{tab:s1s2}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& \\textbf{S1} & \\textbf{S2} \\\\\n\\midrule\n\\drsym{} (\\%) & 0.93 & 0.97 \\\\\n\\cfsym{} (\\%) & 9.90 & 8.03 \\\\\nR-F1 (\\%) & 8.36 & 8.03 \\\\\nE-F1 (\\%) & 30.98 & 31.90 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Fine-Tuned Composability}\n\\label{app:ft}\n\n\\begin{table}[h]\n\\centering\n\\caption{Fine-tuned model + \\ours{} on WikiEvents EE.}\n\\label{tab:ft}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& \\textbf{FT Uncon.} & \\textbf{FT + \\ours{}} \\\\\n\\midrule\nTrigger F1 & 42.0 & 42.0 \\\\\nArgument F1 & 22.0 & 22.3 \\\\\nEntity F1 & 55.0 & 55.0 \\\\\n\\evsym{} (\\%) & 0.5 & 0 \\\\\n\\rovsym{} (\\%) & 3.0 & 0 \\\\\n\\acsym{} (\\%) & 1.8 & 0.2 \\\\\n\\cfsym{} (\\%) & -- & 2.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Latency Overhead}\n\\label{app:latency}\n\n\\begin{table}[h]\n\\centering\n\\caption{Latency overhead of constrained decoding.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Uncon. (s)} & \\textbf{Constrained (s)} & \\textbf{Overhead (\\%)} \\\\\n\\midrule\nSciERC & 4.16 & 4.71 & 13.1 \\\\\nDocRED & 23.5 & 27.6 & 17.5 \\\\\nWikiEvents (est.) & -- & -- & $\\sim$20 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0381762-c758-4d78-be8c-befcb4f53ed3",
  "isSidechain": false,
  "requestId": "req_011CbAPQ7qVAoedX7uSzKRWR",
  "type": "assistant",
  "uuid": "86d7dbc4-d805-4c2c-a47e-633c6167f9c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011NSBdPpPrT5sjubvvE23Ea",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1084,
      "cache_read_input_tokens": 54660,
      "output_tokens": 14683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1084,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14683,
          "cache_read_input_tokens": 54660,
          "cache_creation_input_tokens": 1084,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1084
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

_source line 21 · 2026-05-18T17:01:16.791Z_

<details><summary>↩ Tool result · `toolu_01XywBzrwkKrZD3Q4R1usPbD`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86d7dbc4-d805-4c2c-a47e-633c6167f9c2",
  "isSidechain": false,
  "promptId": "9e1a4d2e-1521-4841-ba16-b71efd78ed15",
  "type": "user",
  "uuid": "ba979052-2ba1-434e-9f0a-e934de43faf0",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\n\\newcommand{\\ours}{OntoCoDec}\n\\newcommand{\\drsym}{\\textsc{DR}}\n\\newcommand{\\rvsym}{\\textsc{RV}}\n\\newcommand{\\etsym}{\\textsc{ET}}\n\\newcommand{\\cfsym}{\\textsc{CF}}\n\\newcommand{\\evsym}{\\textsc{EV}}\n\\newcommand{\\rovsym}{\\textsc{RoV}}\n\\newcommand{\\acsym}{\\textsc{AC}}\n\n\\title{\\ours{}: Universal Ontology-Constrained Structured Generation\\\\for Information Extraction}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================\n%% ABSTRACT\n%% ============================\n\\begin{abstract}\nLarge Language Models (LLMs) produce systematic ontology constraint violations when performing information extraction (IE) tasks, generating entity types and relation arguments that contradict the target schema. We present a violation landscape study across two Relation Extraction (RE) datasets (SciERC, DocRED) and one Event Extraction (EE) dataset (WikiEvents), revealing per-triple violation rates of 13--26\\% for domain/range constraints and up to 89\\% for role vocabulary constraints. Schema-informed prompting reduces violations by 32--62\\% overall but remains unreliable at the per-relation level, with one relation type exhibiting increased violations after prompt intervention.\n\nWe propose \\ours{}, a framework that automatically compiles IE ontology schemas into two composable constraint layers for decoding-time enforcement: a grammar layer (context-free grammar for structural and vocabulary validity) and a semantic layer (stateful entity registry with dynamic logit masking for domain/range constraints). The two layers exhibit an enabling dependency: the grammar layer ensures all generated type tokens belong to the valid vocabulary, which enables the semantic layer to look up and enforce cross-field constraints. Across 2 IE tasks, 4 models (three 8B-class, one 70B), and 3 datasets, \\ours{} eliminates vocabulary and entity-type violations entirely while reducing domain/range violations by 44--100\\%. On SciERC, residual violations drop to 0.93\\% (Qwen3-8B) and 0.08\\% (Llama-3.1-8B). On WikiEvents EE, role vocabulary violations drop from 64--89\\% to 0\\% across all three models. Post-hoc filtering, the natural alternative, discards 17--100\\% of predictions and is completely non-viable for event extraction. F1 scores remain neutral or improve significantly.\n\\end{abstract}\n\n%% ============================\n%% 1. INTRODUCTION\n%% ============================\n\\section{Introduction}\n\nOntology-grounded information extraction requires that every extracted triple or event structure satisfies the type constraints defined by the target schema. A relation extraction (RE) system working with the SciERC ontology, for instance, must ensure that the \\textit{Feature-of} relation connects only entities of types permitted by its domain and range specification. An event extraction (EE) system operating under the KAIROS ontology must assign argument roles that are valid for the specific event type and fill them with entities of permitted types. These constraints are not optional quality preferences; downstream knowledge graph construction, reasoning engines, and regulatory compliance pipelines treat them as hard invariants.\n\nDespite rapid progress in LLM-based IE, the extent to which generated outputs violate ontology constraints has received little systematic attention. Prior work on constrained decoding has focused on structural validity (well-formed JSON, valid code syntax) rather than semantic schema compliance. We find that even capable 70B-parameter models violate domain/range constraints on 6.5\\% of triples for a 7-relation ontology, and the problem does not diminish with ontology simplicity: a 7-relation schema with tight constraints produces comparable violation rates to a 96-relation schema with loose constraints.\n\nPrompt-level intervention (embedding constraint descriptions in the prompt) offers partial relief. On SciERC, schema-informed prompting reduces violations from 15.4\\% to 5.8\\% overall. But this aggregate improvement masks per-relation unreliability: the \\textit{Evaluate-for} relation exhibits a violation rate \\textit{increase} from 24.1\\% to 29.9\\% under schema-informed prompting, a prior-constraint conflict where the model's learned type associations interfere with prompt-level constraint signals. For applications requiring guaranteed per-instance compliance, prompt-level methods are fundamentally insufficient.\n\nWe propose \\ours{}, a framework that automatically compiles ontology schemas into decoding-time constraints operating at two complementary layers. The grammar layer enforces structural validity and vocabulary membership through a context-free grammar integrated with XGrammar. The semantic layer maintains a stateful entity registry during generation and dynamically masks logits to enforce domain/range (RE) or role-argument type (EE) constraints. The two layers compose via bitwise AND of token masks, with an enabling dependency: the grammar layer guarantees that every generated type token is in the valid vocabulary, which is a prerequisite for the semantic layer to look up and enforce the corresponding type rules. When constraint intersection is empty, the system degrades gracefully to grammar-only constraints.\n\nWe validate \\ours{} across 2 tasks (RE, EE), 4 models (Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.1-70B), and 3 datasets (SciERC, DocRED, WikiEvents). Our contributions are:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item A systematic violation landscape study quantifying ontology constraint violations across models, datasets, and IE tasks, establishing that violation rates are driven by constraint tightness rather than ontology size (Section~\\ref{sec:landscape}).\n\\item A composable constraint framework with an enabling dependency between grammar and semantic layers, validated through ablation showing that the semantic layer alone achieves only 24\\% DR reduction versus 94\\% for the full system (Section~\\ref{sec:method}).\n\\item Cross-task generalization: \\ours{} reduces role vocabulary violations from 64--89\\% to 0\\% on event extraction with zero architectural modification, while post-hoc filtering discards 99.6--100\\% of predictions (Section~\\ref{sec:ee}).\n\\item Cross-scale evidence: a 70B model still violates constraints at 6.5--11\\% rates, and \\ours{} achieves 89--100\\% reduction, confirming that scale alone does not solve ontology compliance (Section~\\ref{sec:scale}).\n\\end{itemize}\n\n%% ============================\n%% 2. BACKGROUND\n%% ============================\n\\section{Background}\n\n\\paragraph{Grammar-Constrained Decoding.}\nGrammar-constrained decoding restricts LLM outputs to strings accepted by a formal grammar, typically a context-free grammar (CFG). XGrammar compiles CFG specifications into efficient token masks that are applied at each decoding step. This approach guarantees structural validity (e.g., well-formed JSON) and can enforce vocabulary membership (e.g., generated relation names must belong to a predefined set). However, CFG constraints are inherently stateless: they cannot express constraints that depend on previously generated content, such as ``the entity type filling this argument must be compatible with the relation type generated three fields earlier.''\n\n\\paragraph{IE Ontology Structure.}\nAn IE ontology $\\mathcal{O}$ defines entity types $\\mathcal{E}$, relation types $\\mathcal{R}$ (for RE) or event types $\\mathcal{V}$ with argument roles $\\mathcal{A}$ (for EE), and type constraints mapping each relation/role to permitted entity types. For RE, a domain/range constraint specifies $\\text{dom}(r) \\subseteq \\mathcal{E}$ and $\\text{ran}(r) \\subseteq \\mathcal{E}$ for each $r \\in \\mathcal{R}$. For EE, an argument constraint specifies $\\text{types}(v, a) \\subseteq \\mathcal{E}$ for each event type $v$ and role $a$.\n\n\\paragraph{Violation Taxonomy.}\nWe define five violation types spanning RE and EE. For RE: \\drsym{} (domain/range violation: entity type not permitted for the relation), \\rvsym{} (relation vocabulary: generated relation not in $\\mathcal{R}$), \\etsym{} (entity type not in $\\mathcal{E}$), and \\cfsym{} (cross-field: same entity assigned different types across relations). For EE, we extend with: \\evsym{} (event vocabulary: generated event type not in $\\mathcal{V}$), \\rovsym{} (role vocabulary: argument role not valid for the event type), and \\acsym{} (argument constraint: entity type not permitted for the role under that event type).\n\n%% ============================\n%% 3. VIOLATION LANDSCAPE\n%% ============================\n\\section{Violation Landscape Study}\n\\label{sec:landscape}\n\nBefore proposing a solution, we quantify the problem. We evaluate Qwen3-8B in a zero-shot setting on SciERC (7 relation types) and DocRED (96 relation types) under two prompting conditions: minimal (task instruction only) and schema-informed (explicit constraint descriptions).\n\n\\paragraph{SciERC.}\nTable~\\ref{tab:scierc-phase0} presents per-relation violation rates. The overall domain/range violation rate (\\drsym{}) is 15.37\\%, but this aggregate masks extreme per-relation variance: \\textit{Compare} exhibits 42.42\\% and \\textit{Feature-of} 33.54\\%, while \\textit{Used-for} shows only 0.76\\%. This variance is driven by constraint tightness: relations with few permitted entity type pairs (tight constraints) have high violation rates, while relations accepting many type pairs show near-zero violations. The \\textit{Conjunction} relation, which accepts any entity type pair, has 0\\% violations, providing a natural negative control.\n\nSchema-informed prompting reduces overall \\drsym{} by 62.4\\% (15.37\\% $\\to$ 5.78\\%), but per-relation results are inconsistent. \\textit{Evaluate-for} increases from 24.1\\% to 29.9\\% (+5.8 percentage points), a prior-constraint conflict: the model partially learns to avoid one invalid pattern (Method$\\to$Task) but destabilizes type assignment on remaining boundary cases. Three relations retain violation rates above 10\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{SciERC per-relation domain/range violation rates (\\drsym{}, \\%) under minimal and schema-informed prompting (Qwen3-8B, zero-shot). Overall also shows \\rvsym{}, \\etsym{}, \\cfsym{} rates.}\n\\label{tab:scierc-phase0}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Relation / Metric} & \\textbf{Minimal} & \\textbf{Schema-informed} \\\\\n\\midrule\nUsed-for \\drsym{} & 0.76 & -- \\\\\nCompare \\drsym{} & 42.42 & 27.6 \\\\\nFeature-of \\drsym{} & 33.54 & 11.3 \\\\\nEvaluate-for \\drsym{} & 24.1 & 29.9 (\\textcolor{red}{+5.8}) \\\\\n\\midrule\nOverall \\drsym{} & 15.37 & 5.78 ($\\downarrow$62.4\\%) \\\\\n\\rvsym{} & 1.39 & -- \\\\\n\\etsym{} & 0.40 & -- \\\\\n\\cfsym{} & 0.08 & -- \\\\\n\\midrule\nTotal triples & 1,724 & -- \\\\\nTotal entities & 2,474 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{DocRED.}\nDocRED (96 relations) yields an overall \\drsym{} of 18.7\\% under minimal prompting (Table~\\ref{tab:docred-phase0}), comparable to SciERC's 15.4\\% despite 14$\\times$ the ontology size. This confirms that violation rate is driven by constraint tightness, not ontology complexity per se. The high \\rvsym{} of 28.9\\% arises because DocRED uses P-number relation identifiers (e.g., P31\\_instance\\_of) that are not natural language, causing extensive out-of-vocabulary generation. Schema-informed prompting achieves only 32\\% \\drsym{} reduction (versus 62\\% on SciERC), demonstrating that prompt-level intervention scales poorly with ontology complexity: 96 constraint descriptions dilute attention in the context window.\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED violation landscape (Qwen3-8B, zero-shot).}\n\\label{tab:docred-phase0}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Minimal} & \\textbf{Schema-informed} \\\\\n\\midrule\n\\drsym{} (\\%) & 18.7 & 12.8 ($\\downarrow$32\\%) \\\\\n\\rvsym{} (\\%) & 28.9 & -- \\\\\n\\etsym{} (\\%) & 7.5 & -- \\\\\nTotal triples & 16,540 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================\n%% 4. METHOD\n%% ============================\n\\section{\\ours{} Framework}\n\\label{sec:method}\n\n\\ours{} takes an IE ontology schema $\\mathcal{O}$ and compiles it into decoding-time constraints. The framework consists of three components: an ontology compiler, a grammar constraint layer, and a semantic constraint layer.\n\n\\subsection{Ontology Compiler}\n\nThe compiler reads the ontology definition (entity types, relation/event types, and type constraints) and produces two artifacts: (1)~a context-free grammar $G$ encoding JSON structure and type vocabularies, and (2)~a constraint table $C$ mapping each relation type (or event-type/role pair) to its set of permitted entity types.\n\nFor RE, $C[r] = (\\text{dom}(r), \\text{ran}(r))$ specifies permitted head and tail entity types for relation $r$. For EE, $C[v, a] = \\text{types}(v, a)$ specifies permitted entity types for argument role $a$ under event type $v$. The same compiler handles both tasks by treating the constraint structure uniformly as type-conditional type restrictions.\n\n\\subsection{Grammar Layer}\n\nThe grammar $G$ is a CFG that enforces: (a)~well-formed JSON structure matching the expected IE output format, (b)~relation/event type names restricted to $\\mathcal{R}$ or $\\mathcal{V}$, and (c)~entity type names restricted to $\\mathcal{E}$. This layer is integrated with XGrammar, which compiles $G$ into per-token masks $M_\\text{grammar}(t)$ at each decoding step $t$.\n\nThe grammar layer eliminates \\rvsym{}, \\etsym{}, and \\evsym{} violations by construction: no out-of-vocabulary type token can pass the mask. It cannot, however, enforce cross-field constraints (\\drsym{}, \\rovsym{}, \\acsym{}) because CFGs are stateless.\n\n\\subsection{Semantic Layer}\n\nThe semantic layer maintains an entity registry $\\mathcal{S}$ that tracks entity types assigned during generation. At each token position where a type-constrained field is being generated, the layer:\n\\begin{enumerate}[nosep]\n\\item Identifies the current generation context (which relation/event type and which argument position).\n\\item Looks up the permitted entity types from $C$.\n\\item Computes a semantic mask $M_\\text{semantic}(t)$ that allows only tokens consistent with permitted types.\n\\end{enumerate}\n\nFor RE, when generating the head entity type of relation $r$, only tokens in $\\text{dom}(r)$ are permitted. For EE, when generating the entity type for argument role $a$ of event type $v$, only tokens in $\\text{types}(v, a)$ are permitted. The lookup requires the relation/event type to be a valid vocabulary member, establishing the enabling dependency on the grammar layer.\n\n\\subsection{Composition and Graceful Degradation}\n\nThe final mask at each step is $M(t) = M_\\text{grammar}(t) \\;\\&\\; M_\\text{semantic}(t)$. When $M(t) = \\emptyset$ (the intersection is empty because no token satisfies both layers simultaneously), the system falls back to $M_\\text{grammar}(t)$ alone. This graceful degradation ensures structural validity as a guaranteed floor even when semantic constraints cannot be satisfied. Fallback frequency varies with ontology tightness and model behavior: on SciERC, approximately 10.7 fallback events occur per document; on DocRED, approximately 57 per document.\n\n\\subsection{Decidability Taxonomy}\n\nWe classify ontology constraints by their decidability during autoregressive generation:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Purely local}: entity type $\\in \\mathcal{E}$, relation type $\\in \\mathcal{R}$ (grammar layer).\n\\item \\textbf{Prefix-decidable with state}: domain/range and role-argument constraints (semantic layer with entity registry).\n\\item \\textbf{Truly non-local}: forward coreference consistency, where an entity's type must agree with a type assigned later in the sequence. This is out of scope for forward-only decoding and manifests as \\cfsym{} violations.\n\\end{itemize}\n\n%% ============================\n%% 5. EXPERIMENTS\n%% ============================\n\\section{Experiments}\n\n\\subsection{Setup}\n\nWe evaluate in a zero-shot setting (no training data, no fine-tuning) to demonstrate that \\ours{} works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\n\n\\textbf{RE Datasets}: SciERC (7 relations, 7 entity types) and DocRED (96 relations, 15 entity types).\n\\textbf{EE Dataset}: WikiEvents (56 event types, 80 argument roles, 27 entity types, KAIROS ontology).\n\\textbf{Models}: Qwen3-8B, Llama-3.1-8B-Instruct, Mistral-7B-v0.3-Instruct (8B-class); Llama-3.1-70B-Instruct AWQ-INT4 (70B-class).\n\\textbf{Configurations}: Unconstrained, grammar-only, semantic-only, full (grammar + semantic, S1 single-pass).\n\nAll statistical tests use 10,000-iteration bootstrap resampling.\n\n\\subsection{RE: SciERC Ablation}\n\\label{sec:scierc-ablation}\n\nTable~\\ref{tab:scierc-ablation} presents the four-way ablation on SciERC with Qwen3-8B. The grammar-only configuration eliminates \\rvsym{} and \\etsym{} entirely (both 0\\%) while leaving \\drsym{} essentially unchanged (14.84\\% versus 15.37\\%), confirming that vocabulary-level and semantic-level violations are orthogonal. The semantic-only configuration reduces \\drsym{} by only 24\\% (to 11.65\\%), far below the full system's 94\\% reduction. This gap is explained by the enabling dependency: without grammar enforcement, 1.51\\% of relation names are out-of-vocabulary, preventing the semantic layer from looking up their constraints.\n\nThe full system (S1) achieves \\drsym{} of 0.93\\% (from 15.37\\%, $\\downarrow$94\\%), with \\rvsym{} and \\etsym{} at 0\\%. R-F1 changes by +0.13 percentage points (p=0.58, not significant). The residual 0.93\\% arises from fallback events where the semantic-grammar mask intersection is empty.\n\n\\cfsym{} increases from 0.08\\% (unconstrained) to 9.90\\% (full S1). This is entirely attributable to the semantic layer (grammar-only \\cfsym{} = 0.08\\%). The mechanism is per-relation independent type enforcement: the semantic layer assigns entity types per-relation without cross-relation coordination, so the same entity may receive different types in different relational contexts. The dominant pattern is Generic $\\leftrightarrow$ OtherScientificTerm, reflecting genuine type system ambiguity in SciERC.\n\n\\begin{table}[t]\n\\centering\n\\caption{SciERC ablation matrix (Qwen3-8B). Violation rates (\\%) and F1 (\\%).}\n\\label{tab:scierc-ablation}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\textbf{Uncon.} & \\textbf{Grammar} & \\textbf{Semantic} & \\textbf{Full S1} \\\\\n\\midrule\n\\drsym{} & 15.37 & 14.84 & 11.65 & \\textbf{0.93} \\\\\n\\rvsym{} & 1.39 & \\textbf{0} & 1.51 & \\textbf{0} \\\\\n\\etsym{} & 0.40 & \\textbf{0} & 0.40 & \\textbf{0} \\\\\n\\cfsym{} & 0.08 & 0.08 & 2.71 & 9.90 \\\\\n\\midrule\nR-F1 & 8.23 & 8.23 & 8.15 & 8.36 \\\\\nE-F1 & 31.01 & 30.98 & -- & 30.98 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{RE: DocRED Ablation}\n\\label{sec:docred-ablation}\n\nTable~\\ref{tab:docred-ablation} presents the DocRED ablation. A striking result is that grammar-only \\drsym{} \\textit{increases} from 18.46\\% to 26.17\\%. This latent violation surfacing effect occurs because grammar forces 5,189 out-of-vocabulary relation predictions into valid relation names, making them checkable by the \\drsym{} metric for the first time. Many of these forced mappings produce domain/range violations that were previously hidden behind \\rvsym{}.\n\nThe full system reduces \\drsym{} to 10.21\\% ($\\downarrow$44.7\\%), with approximately 57 fallback events per document (versus 10.7 on SciERC). R-F1 improves by +0.50 percentage points (p$<$0.001, 95\\% CI [+0.23, +0.81]), a significant gain attributable to out-of-vocabulary elimination reducing false positives. E-F1 improves by +1.22 percentage points (p$<$0.001).\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED ablation matrix (Qwen3-8B). Violation rates (\\%) and F1 (\\%).}\n\\label{tab:docred-ablation}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\textbf{Uncon.} & \\textbf{Grammar} & \\textbf{Semantic} & \\textbf{Full S1} \\\\\n\\midrule\n\\drsym{} & 18.46 & 26.17 & 13.84 & \\textbf{10.21} \\\\\n\\rvsym{} & 29.66 & \\textbf{0.03} & 29.87 & \\textbf{0.03} \\\\\n\\etsym{} & 2.48 & \\textbf{0} & 4.22 & \\textbf{0} \\\\\n\\cfsym{} & 0.10 & 0.07 & 1.05 & 2.57 \\\\\n\\midrule\nR-F1 & 7.74 & 8.31 & 7.70 & 8.23 \\\\\nE-F1 & 58.15 & 59.38 & -- & 59.37 \\\\\n\\midrule\nOOV rels. & 5,189 & -- & -- & -- \\\\\nTotal triples & 17,497 & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Generalization}\n\\label{sec:crossmodel}\n\nTable~\\ref{tab:crossmodel} evaluates Llama-3.1-8B on both RE datasets with zero code modification to \\ours{}. On SciERC, Llama achieves \\drsym{} reduction of 99.4\\% (13.34\\% $\\to$ 0.08\\%, a single residual violation). On DocRED, reduction is 90.2\\% (26.07\\% $\\to$ 2.55\\%).\n\nThe two models exhibit orthogonal failure profiles. On DocRED, Qwen has high \\rvsym{} (29.66\\%) but lower \\drsym{} (18.46\\%), while Llama has lower \\rvsym{} (16.03\\%) but higher \\drsym{} (26.07\\%). Vocabulary compliance and semantic compliance are independent failure dimensions, and the two-layer architecture addresses both.\n\nThe differential reduction rates (Qwen DocRED 44.7\\% versus Llama DocRED 90.2\\%) are explained by the interaction between constraint tightness and the model's \\rvsym{} baseline (Section~\\ref{sec:analysis-tightness}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model comparison: Llama-3.1-8B (zero code modification).}\n\\label{tab:crossmodel}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{DocRED}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& Uncon. & Full S1 & Uncon. & Full S1 \\\\\n\\midrule\n\\drsym{} (\\%) & 13.34 & \\textbf{0.08} & 26.07 & \\textbf{2.55} \\\\\n\\rvsym{} (\\%) & 0.55 & 0 & 16.03 & 0 \\\\\n\\etsym{} (\\%) & 0 & 0 & 0.13 & 0 \\\\\n\\cfsym{} (\\%) & -- & 6.56 & 0.17 & 12.02 \\\\\n\\midrule\nR-F1 & 2.68 & 2.54 & 5.98 & 6.27 \\\\\n$\\Delta$ R-F1 & \\multicolumn{2}{c}{$-0.14$ ($p$=0.011)} & \\multicolumn{2}{c}{$+0.29$ ($p$=0.013)} \\\\\nE-F1 & 23.56 & -- & 55.65 & 55.01 \\\\\n\\midrule\nDR reduction & \\multicolumn{2}{c}{99.4\\%} & \\multicolumn{2}{c}{90.2\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Scale: 70B Model}\n\\label{sec:scale}\n\nTable~\\ref{tab:scale70b} evaluates Llama-3.1-70B-Instruct (AWQ-INT4). On SciERC, the 70B model reduces unconstrained \\drsym{} to 6.5\\% (roughly half of 8B-class models), but violations persist: one in every 15 triples still violates domain/range constraints on a 7-relation ontology. \\ours{} achieves \\drsym{} of 0\\% (complete elimination). On DocRED, unconstrained \\drsym{} is approximately 11.0\\%, and constrained \\drsym{} is 1.2\\% ($\\downarrow$89.1\\%).\n\nScale reduces but does not eliminate violations. \\ours{} is effective across scales: 8B reduction ranges from 44.7--99.4\\%, and 70B reduction ranges from 89.1--100\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-scale results: Llama-3.1-70B-Instruct AWQ-INT4.}\n\\label{tab:scale70b}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{DocRED}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& Uncon. & Full S1 & Uncon. & Full S1 \\\\\n\\midrule\n\\drsym{} (\\%) & 6.5 & \\textbf{0} & 11.0 & \\textbf{1.2} \\\\\n\\rvsym{} (\\%) & 0.6 & 0 & 5.2 & 0 \\\\\n\\etsym{} (\\%) & 0 & 0 & 0.05 & 0 \\\\\n\\cfsym{} (\\%) & -- & 3.66 & 0.12 & 5.0 \\\\\n\\midrule\nR-F1 & 11.22 & 11.24 & 9.8 & 10.1 \\\\\nE-F1 & 35.17 & 35.14 & 62.5 & 63.0 \\\\\n\\midrule\nDR reduction & \\multicolumn{2}{c}{100\\%} & \\multicolumn{2}{c}{89.1\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Event Extraction: WikiEvents}\n\\label{sec:ee}\n\nWikiEvents uses the KAIROS ontology with 56 event types, 80 argument roles, and 27 entity types, defining 245 explicit (event\\_type, role) $\\to$ allowed\\_entity\\_types constraints. We evaluate three 8B-class models. Table~\\ref{tab:ee-main} presents the results.\n\nUnconstrained EE exhibits dramatically higher violation rates than RE. Role vocabulary violations (\\rovsym{}) range from 63.9\\% to 88.8\\%, reflecting that 80 argument roles conditioned on 56 event types far exceed what models can learn from a prompt. Event vocabulary violations (\\evsym{}) range from 10.5\\% to 37.3\\%. Entity F1 is 0\\% for all unconstrained models, not because models cannot identify entities, but because the malformed JSON output prevents the parser from extracting entity mentions.\n\n\\ours{} eliminates \\evsym{} and \\rovsym{} entirely (0\\% across all three models). Entity F1 recovers to 11.7--17.6\\%, purely from format compliance: grammar enforcement produces schema-valid JSON that the parser can process. Trigger F1 improves by 1.5--1.8 percentage points through elimination of out-of-vocabulary event types counted as false positives. \\acsym{} residuals of 1.3--3.8\\% arise from model semantic confusion between similar entity types (e.g., SID vs.\\ SEN), not from tokenizer collisions (Qwen and Llama have zero BPE collision groups; Mistral's two collision groups are resolved in our v3 implementation).\n\n\\begin{table}[t]\n\\centering\n\\caption{WikiEvents event extraction results (3 models, 246 documents). All violation rates in \\%.}\n\\label{tab:ee-main}\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Qwen3-8B}} & \\multicolumn{2}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{2}{c}{\\textbf{Mistral-7B}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n& Uncon. & Full & Uncon. & Full & Uncon. & Full \\\\\n\\midrule\nParse (\\%) & 88.6 & 83.7 & 91.9 & 84.1 & 78.9 & 88.6 \\\\\n\\evsym{} & 24.0 & \\textbf{0} & 10.5 & \\textbf{0} & 37.3 & \\textbf{0} \\\\\n\\rovsym{} & 74.9 & \\textbf{0} & 88.8 & \\textbf{0} & 63.9 & \\textbf{0} \\\\\n\\acsym{} & 0.3 & 2.1 & 0.1 & 3.8 & 0 & 1.3 \\\\\n\\cfsym{} & 0 & 21.1 & 0 & 17.2 & 0 & 14.9 \\\\\n\\midrule\nTrig. F1 & 11.8 & 13.4 & 5.7 & 7.5 & 2.4 & 3.9 \\\\\nEnt. F1 & 0 & 14.1 & 0 & 17.6 & 0 & 11.7 \\\\\nArg. F1 & 0.09 & 1.68 & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{EE Grammar-Only Ablation.}\nTable~\\ref{tab:ee-ablation} shows the grammar-only configuration on all three models. Grammar eliminates \\evsym{} (0\\% across models) but \\rovsym{} remains at 64--76\\%: the CFG cannot express per-event-type role constraints, as role validity depends on the event context. \\acsym{} rises to 8--14\\% under grammar-only, a latent violation surfacing effect parallel to the DocRED \\drsym{} increase under grammar-only RE. This proves the semantic layer is essential for EE: the two-layer architecture is necessary, not merely convenient.\n\n\\begin{table}[t]\n\\centering\n\\caption{WikiEvents grammar-only ablation (3 models). Violation rates (\\%).}\n\\label{tab:ee-ablation}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Qwen} & \\textbf{Llama} & \\textbf{Mistral} \\\\\n\\midrule\n\\evsym{} & 0 & 0 & 0 \\\\\n\\rovsym{} & 68 & 76 & 64 \\\\\n\\acsym{} & 11 & 14 & 13.8 \\\\\n\\cfsym{} & 0.5 & 0.3 & 1.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Post-Hoc Filtering Comparison}\n\\label{sec:posthoc}\n\nTable~\\ref{tab:posthoc} compares \\ours{} with post-hoc filtering (removing violating triples/arguments after generation).\n\nFor RE, post-hoc filtering achieves higher F1 than \\ours{} in this low-F1 zero-shot regime (SciERC 8.63 vs.\\ 8.36, DocRED 9.61 vs.\\ 8.23), because removing violating triples (mostly false positives) boosts precision. However, post-hoc filtering discards 16.8\\% of SciERC triples and 48.1\\% of DocRED triples, losing 127 true positives on DocRED (11.2\\% of all TPs). Post-hoc filtering also cannot resolve \\etsym{} violations (residual 2.47\\% on DocRED) because it operates on triples, not entity lists. \\ours{} preserves all triple slots and increases recall: the probability mass redirected from invalid tokens produces additional correct extractions.\n\nFor EE, post-hoc filtering is completely non-viable. It must discard 99.6\\% (Qwen: 5,467 $\\to$ 23), 99.9\\% (Llama: 5,053 $\\to$ 3), and 100\\% (Mistral: 6,034 $\\to$ 0) of arguments to achieve zero violations. The high violation rates in unconstrained EE (combined \\evsym{} + \\rovsym{} covering 75--90\\% of arguments) make post-hoc filtering equivalent to discarding the entire output.\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-hoc filtering comparison. RE: Qwen3-8B. EE: all 3 models.}\n\\label{tab:posthoc}\n\\small\n\\begin{tabular}{lcc|ccc}\n\\toprule\n& \\multicolumn{2}{c|}{\\textbf{RE (Qwen3-8B)}} & \\multicolumn{3}{c}{\\textbf{EE Discard Rate}} \\\\\n& SciERC & DocRED & Qwen & Llama & Mistral \\\\\n\\midrule\nPost-hoc R-F1 & 8.63 & 9.61 & -- & -- & -- \\\\\n\\ours{} R-F1 & 8.36 & 8.23 & -- & -- & -- \\\\\n\\midrule\nDiscard (\\%) & 16.8 & 48.1 & 99.6 & 99.9 & 100 \\\\\nTP lost & 7 & 127 & -- & -- & -- \\\\\nET residual (\\%) & -- & 2.47 & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Fine-Tuned Model Composability}\n\nTo address the question of whether \\ours{} only works in zero-shot settings, we evaluate composability with fine-tuned models on WikiEvents EE. Fine-tuning dramatically improves extraction quality (trigger F1: 12\\% $\\to$ 42\\%, argument F1: 0\\% $\\to$ 22\\%) and reduces violations substantially (\\rovsym{}: 75\\% $\\to$ 3\\%, \\evsym{}: 24\\% $\\to$ 0.5\\%). Applying \\ours{} to the fine-tuned model eliminates remaining \\rovsym{} (0\\%) and reduces \\acsym{} from 1.8\\% to 0.2\\%, with F1 neutral (+0.3 percentage points on argument F1). \\cfsym{} drops to 2.5\\%, far below zero-shot levels (15--21\\%), because fine-tuning stabilizes type assignment. Four additional RE composability experiments (Qwen/Llama $\\times$ SciERC/DocRED) all show positive results.\n\n\\subsection{Latency}\n\nConstrained decoding introduces 13.1\\% latency overhead on SciERC (4.16s $\\to$ 4.71s per document) and 17.5\\% on DocRED (23.5s $\\to$ 27.6s). EE overhead is estimated at approximately 20\\% due to the three-layer cascade (grammar $\\to$ role $\\to$ argument type). All overheads remain below 25\\%.\n\n%% ============================\n%% 6. ANALYSIS\n%% ============================\n\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Enabling Dependency}\n\\label{sec:analysis-enabling}\n\nThe semantic-only configuration achieves only 24\\% \\drsym{} reduction on SciERC (versus 94\\% for the full system) and 25\\% on DocRED. The mechanism is clear: without grammar enforcement, out-of-vocabulary relation names prevent the semantic layer from looking up constraint rules. On SciERC, 1.51\\% of relations are OOV under semantic-only; on DocRED, 29.87\\%. Each OOV relation renders the semantic layer entirely ineffective for that triple.\n\nThe dependency is asymmetric: grammar is a prerequisite for semantic, but not vice versa. Grammar-only achieves identical \\rvsym{}/\\etsym{} elimination regardless of whether the semantic layer is present. This distinguishes the architecture from generic ``synergy'' between components.\n\nOn EE, the dependency is even more pronounced. Grammar-only reduces \\rovsym{} by less than 2 percentage points (from 64--89\\% to 64--76\\%), while the full system eliminates it entirely. The semantic layer's continuation masking mechanism, which conditions role validity on the event type context, is the only viable enforcement strategy for role vocabulary constraints.\n\n\\subsection{Tightness $\\times$ RV Baseline Interaction}\n\\label{sec:analysis-tightness}\n\nThe \\drsym{} reduction ceiling is determined by two factors: ontology constraint tightness and the model's \\rvsym{} baseline. On DocRED ($\\bar{\\tau}=0.842$, tight constraints), Qwen achieves 44.7\\% reduction while Llama achieves 90.2\\%, on the same ontology. The difference is explained by \\rvsym{} baselines: Qwen \\rvsym{} = 29.66\\% versus Llama \\rvsym{} = 16.03\\%. Higher \\rvsym{} means more OOV predictions are forced into valid relation names by the grammar layer, surfacing latent violations that inflate residual \\drsym{}.\n\nThis dual-factor model predicts the full cross-scale, cross-model matrix:\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& SciERC ($\\bar{\\tau}=0.40$) & DocRED ($\\bar{\\tau}=0.84$) \\\\\n\\midrule\n8B unconstrained & 13.3--15.4\\% & 18.5--26.1\\% \\\\\n8B constrained & 0.08--0.93\\% & 2.55--10.21\\% \\\\\n70B unconstrained & 6.5\\% & 11.0\\% \\\\\n70B constrained & 0\\% & 1.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLoose constraints (SciERC) yield near-zero residual regardless of model; tight constraints (DocRED) yield residual proportional to the model's \\rvsym{} baseline.\n\n\\subsection{Fallback Frequency as Constraint Coverage}\n\nWe define constraint coverage as the fraction of type-token positions where semantic masking is active (not fallen back to grammar-only). SciERC: approximately 10.7 fallback events per document. DocRED: approximately 57 per document, a 5.3$\\times$ ratio. This quantifies the gap between SciERC residual \\drsym{} (0.93\\%) and DocRED residual \\drsym{} (10.21\\%): each fallback position reverts to grammar-only, which has a known \\drsym{} of 14.84\\% (SciERC) or 26.17\\% (DocRED). Higher fallback frequency translates directly to higher residual violations.\n\n\\subsection{Cross-Field Violation Tradeoff}\n\\label{sec:cf}\n\n\\cfsym{} violations increase under constrained decoding: from 0.08\\% to 9.90\\% on SciERC (Qwen), from 0.17\\% to 12.02\\% on DocRED (Llama), and from 0\\% to 14.9--21.1\\% on WikiEvents EE. Grammar-only \\cfsym{} remains at baseline (0.07--0.08\\%), confirming that \\cfsym{} is entirely introduced by the semantic layer.\n\nThe mechanism is per-relation independent type enforcement: the semantic layer assigns types optimally for each relation/event independently, without cross-relation coordination. When an entity appears in multiple relational contexts, different type assignments may be optimal for each context, producing cross-field inconsistency.\n\nError analysis of 15 representative cases shows that the dominant \\cfsym{} pattern is Entity-vs-Relation type drift (88\\% of \\cfsym{} instances), where the same entity receives different types in the entity list versus relation arguments. The top conflict types (Generic $\\leftrightarrow$ OtherScientificTerm, Material $\\leftrightarrow$ OtherScientificTerm) reflect genuine ambiguity in the SciERC type system.\n\nImportantly, individual triples under \\cfsym{} remain type-valid; only cross-triple consistency is broken. This distinguishes \\cfsym{} from \\drsym{} violations, where individual triples are structurally invalid and unusable by downstream systems.\n\n\\textbf{Scale mitigates \\cfsym{}}: 70B \\cfsym{} = 3.66\\% on SciERC (versus 6.56--9.90\\% for 8B models), and fine-tuned models show \\cfsym{} = 2.5\\% (versus 15--21\\% zero-shot). Larger and better-trained models produce more consistent type assignments.\n\n\\textbf{Limitation and future work}: \\cfsym{} is an inherent limitation of per-relation independent enforcement. A global entity-type consensus pass (assigning each entity a single type before relation-specific enforcement) is the natural extension.\n\n\\subsection{Error Analysis}\n\nAnalysis of residual violations across 15 representative cases reveals three root cause categories for \\acsym{} residuals in EE:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Semantic confusion} (72\\%): The model confuses semantically similar entity types (e.g., SID vs.\\ SEN, PER vs.\\ GPE in ambiguous contexts).\n\\item \\textbf{BPE collision residual} (12\\%): Residual cases from Mistral's two collision groups after v3 fix.\n\\item \\textbf{Genuine boundary cases} (16\\%): Annotation-disagreement-level ambiguity where human annotators would also disagree on type assignment.\n\\end{itemize}\n\nFor RE, 80\\% of residual \\drsym{} on DocRED concentrates in tight-constraint relations, consistent with the tightness analysis.\n\n\\subsection{S1 vs.\\ S2 Strategy}\n\nAs an architectural ablation, we compare the single-pass S1 strategy with a two-pass S2 strategy (Pass 1: entity extraction with grammar-only; Pass 2: relation generation with input-dependent grammar). On SciERC, S2 yields \\drsym{} = 0.97\\% (versus S1 0.93\\%), \\cfsym{} = 8.03\\% (versus S1 9.90\\%), and R-F1 = 8.03\\% (versus S1 8.36\\%). S2 does not solve \\cfsym{} and shows slightly worse metrics overall. We recommend S1 as the primary strategy and present S2 as evidence of framework flexibility.\n\n%% ============================\n%% 7. RELATED WORK\n%% ============================\n\\section{Related Work}\n\n\\paragraph{Constrained Decoding for Structured Generation.}\nGrammar-constrained decoding enforces structural validity through formal grammars. XGrammar, Outlines, and LMQL compile context-free or regular grammars into token masks. These approaches guarantee syntactic validity (well-formed JSON, valid code) but do not address semantic constraints that depend on generation context. SynCode extends grammar-based approaches to programming languages. \\ours{} builds on grammar-constrained decoding but adds a semantic layer that maintains generation state to enforce cross-field type constraints.\n\n\\paragraph{Type-Aware IE.}\nType-constrained IE has been approached through training-time objectives (entity typing losses, relation-aware entity representations) and retrieval-augmented prompting. TANL unifies IE as translation, implicitly encoding type information. UIE and InstructUIE frame IE as instruction following. These approaches embed type awareness in the model but cannot guarantee constraint satisfaction at inference time. \\ours{} provides guaranteed compliance regardless of the base model's type awareness.\n\n\\paragraph{LLM-Based Information Extraction.}\nRecent work applies LLMs to IE through prompting, in-context learning, and fine-tuning. GPT-RE, Code4Struct, and GoLLIE explore structured output formats. CodeIE uses code generation as an IE interface. These systems face the same ontology violation problem we document; \\ours{} is complementary and can be applied to any LLM-based IE system using autoregressive decoding.\n\n\\paragraph{Event Extraction.}\nEvent extraction extends relation extraction with event types and argument roles. Text2Event, DEGREE, and CEDAR frame EE as sequence generation. The KAIROS ontology used in WikiEvents defines rich type constraints (245 role-argument type mappings across 56 event types) that existing generation-based EE systems do not enforce at inference time.\n\n\\paragraph{Quality Assurance for Generated Structures.}\nPost-hoc filtering and verification pipelines check generated outputs against schema constraints after generation. Our experiments show this approach is viable (with information loss) for RE but completely non-viable for EE, where 99.6--100\\% of outputs must be discarded. \\ours{}'s generation-time enforcement avoids this fundamental limitation.\n\n%% ============================\n%% 8. CONCLUSION\n%% ============================\n\\section{Conclusion}\n\nWe presented \\ours{}, a framework for ontology-constrained structured generation that automatically compiles IE schemas into composable grammar and semantic constraint layers. Our violation landscape study establishes that LLM-based IE systems violate ontology constraints at rates of 6.5--26\\% for domain/range and up to 89\\% for role vocabulary, driven by constraint tightness rather than ontology size. Scale alone does not solve the problem: 70B models still violate constraints at 6.5--11\\%.\n\n\\ours{} achieves 44--100\\% domain/range violation reduction across 2 tasks, 4 models, and 3 datasets, eliminates vocabulary-level violations entirely, and maintains or improves F1 scores. The framework generalizes from relation extraction to event extraction with zero architectural modification. Post-hoc filtering, the natural alternative, discards 17--100\\% of outputs and is non-viable for event extraction.\n\nCross-field consistency violations (3.7--21\\%) are an inherent limitation of per-relation independent type enforcement. Future work will address this through global entity-type consensus mechanisms. The enabling dependency between grammar and semantic layers, the tightness-by-RV-baseline interaction governing reduction ceilings, and the latent violation surfacing effect provide quantitative insights into the mechanics of constrained generation for structured information extraction.\n\n%% ============================\n%% APPENDIX\n%% ============================\n\\appendix\n\n\\section{Bootstrap Confidence Intervals}\n\\label{app:bootstrap}\n\nTable~\\ref{tab:bootstrap-re} reports full bootstrap results (10,000 iterations) for RE F1 metrics. DocRED R-F1 improvement is significant for both models; SciERC R-F1 is neutral (Qwen) or negligible (Llama).\n\n\\begin{table}[h]\n\\centering\n\\caption{Bootstrap CI for RE F1 changes (constrained $-$ unconstrained).}\n\\label{tab:bootstrap-re}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset / Metric} & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Qwen3-8B}\n& SciERC R-F1 & +0.13 & 0.58 \\\\\n& DocRED R-F1 & +0.50 & $<$0.001 \\\\\n& DocRED E-F1 & +1.23 & $<$0.001 \\\\\n\\midrule\n\\multirow{2}{*}{Llama-3.1-8B}\n& SciERC R-F1 & $-0.14$ & 0.011 \\\\\n& DocRED R-F1 & +0.29 & 0.013 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:bootstrap-ee} reports EE bootstrap results. Entity F1 recovery from 0\\% is highly significant for all models.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bootstrap CI for EE F1 changes (constrained $-$ unconstrained).}\n\\label{tab:bootstrap-ee}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Model} & \\textbf{Metric} & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-8B}\n& Entity F1 & +14.09 & $<$0.001 \\\\\n& Trigger F1 & +1.55 & 0.015 \\\\\n\\midrule\n\\multirow{2}{*}{Llama-3.1-8B}\n& Entity F1 & +17.63 & $<$0.001 \\\\\n& Trigger F1 & +1.76 & 0.03 \\\\\n\\midrule\n\\multirow{2}{*}{Mistral-7B}\n& Entity F1 & +11.71 & $<$0.001 \\\\\n& Trigger F1 & +1.46 & 0.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{S1 vs.\\ S2 Comparison}\n\\label{app:s2}\n\n\\begin{table}[h]\n\\centering\n\\caption{S1 vs.\\ S2 on SciERC (Qwen3-8B, full run).}\n\\label{tab:s1s2}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& \\textbf{S1} & \\textbf{S2} \\\\\n\\midrule\n\\drsym{} (\\%) & 0.93 & 0.97 \\\\\n\\cfsym{} (\\%) & 9.90 & 8.03 \\\\\nR-F1 (\\%) & 8.36 & 8.03 \\\\\nE-F1 (\\%) & 30.98 & 31.90 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Fine-Tuned Composability}\n\\label{app:ft}\n\n\\begin{table}[h]\n\\centering\n\\caption{Fine-tuned model + \\ours{} on WikiEvents EE.}\n\\label{tab:ft}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& \\textbf{FT Uncon.} & \\textbf{FT + \\ours{}} \\\\\n\\midrule\nTrigger F1 & 42.0 & 42.0 \\\\\nArgument F1 & 22.0 & 22.3 \\\\\nEntity F1 & 55.0 & 55.0 \\\\\n\\evsym{} (\\%) & 0.5 & 0 \\\\\n\\rovsym{} (\\%) & 3.0 & 0 \\\\\n\\acsym{} (\\%) & 1.8 & 0.2 \\\\\n\\cfsym{} (\\%) & -- & 2.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Latency Overhead}\n\\label{app:latency}\n\n\\begin{table}[h]\n\\centering\n\\caption{Latency overhead of constrained decoding.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Uncon. (s)} & \\textbf{Constrained (s)} & \\textbf{Overhead (\\%)} \\\\\n\\midrule\nSciERC & 4.16 & 4.71 & 13.1 \\\\\nDocRED & 23.5 & 27.6 & 17.5 \\\\\nWikiEvents (est.) & -- & -- & $\\sim$20 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "86d7dbc4-d805-4c2c-a47e-633c6167f9c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_co…",
  "leafUuid": "ba979052-2ba1-434e-9f0a-e934de43faf0",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2"
}
```

---

### Tool call

_source line 24 · 2026-05-18T17:01:22.462Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PeRED2wwozA1xNMZpeVoCD`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba979052-2ba1-434e-9f0a-e934de43faf0",
  "isSidechain": false,
  "requestId": "req_011CbAPkacrqhSwCFKE1S5RQ",
  "type": "assistant",
  "uuid": "7e6797e6-f818-45f5-b36b-0200097e4e72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNhptETRc2Uvrsv4DMskK1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14751,
      "cache_read_input_tokens": 55744,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 55744,
          "cache_creation_input_tokens": 14751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14751
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

_source line 25 · 2026-05-18T17:01:25.474Z_

<details><summary>↩ Tool result · `toolu_01PeRED2wwozA1xNMZpeVoCD`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}]
Overfull \hbox (0.974pt too wide) in paragraph at lines 55--56
[]\T1/cmr/m/n/10.95 We val-i-date On-toCoDec across 2 tasks (RE, EE), 4 mod-els
 (Qwen3-8B, Llama-3.1-8B, Mistral-

LaTeX Warning: Reference `sec:landscape' on page 2 undefined on input line 58.


LaTeX Warning: Reference `sec:method' on page 2 undefined on input line 59.


LaTeX Warning: Reference `sec:ee' on page 2 undefined on input line 60.


LaTeX Warning: Reference `sec:scale' on page 2 undefined on input line 61.

[2]

LaTeX Warning: Reference `tab:scierc-phase0' on page 3 undefined on input line 
87.


LaTeX Warning: Reference `tab:docred-phase0' on page 3 undefined on input line 
117.

[3] [4]

LaTeX Warning: Reference `tab:scierc-ablation' on page 5 undefined on input lin
e 199.


LaTeX Warning: Reference `tab:docred-ablation' on page 5 undefined on input lin
e 228.

[5]

LaTeX Warning: Reference `tab:crossmodel' on page 6 undefined on input line 258
.


LaTeX Warning: Reference `sec:analysis-tightness' on page 6 undefined on input 
line 262.


LaTeX Warning: Reference `tab:scale70b' on page 6 undefined on input line 292.


LaTeX Warning: Reference `tab:ee-main' on page 6 undefined on input line 323.

[6]

LaTeX Warning: Reference `tab:ee-ablation' on page 7 undefined on input line 35
5.


LaTeX Warning: Reference `tab:posthoc' on page 7 undefined on input line 377.

[7] [8]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 426.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\times' on input line 426.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 426.

[9] [10] [11]

LaTeX Warning: Reference `tab:bootstrap-re' on page 12 undefined on input line 
523.


LaTeX Warning: Reference `tab:bootstrap-ee' on page 12 undefined on input line 
546.

[12] [13] (./paper.aux)
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecxc1095
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ecxc1095
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecxc1095.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecxc.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excsc.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excspl.mf
 Ok [25] [26] [27] [28] [29] [30] [31] [158])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170] [171]
[172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182] [183]
[184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excligtb.mf
 Ok) ) ) )
(some charht values had to be adjusted by as much as 0.0996pt)
Font metrics written on ecxc1095.tfm.
Output written on ecxc1095.600gf (256 characters, 55196 bytes).
Transcript written on ecxc1095.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecxc1095.600pk: successfully generated.


LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecxc1095.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk>
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 eccc1000
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input eccc1000
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/eccc1000.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/eccc.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excsc.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excspl.mf
 Ok [25] [26] [27] [28] [29] [30] [31] [158])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170] [171]
[172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182] [183]
[184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excligtb.mf
 Ok) ) ) )
(some charht values had to be adjusted by as much as 0.06943pt)
Font metrics written on eccc1000.tfm.
Output written on eccc1000.600gf (256 characters, 51852 bytes).
Transcript written on eccc1000.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/eccc1000.600pk: successfully generated.
 &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/eccc1000.600pk>
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 eccc1095
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input eccc1095
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/eccc1095.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/eccc.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excsc.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excspl.mf
 Ok [25] [26] [27] [28] [29] [30] [31] [158])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170] [171]
[172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182] [183]
[184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excligtb.mf
 Ok) ) ) )
(some charht values had to be adjusted by as much as 0.0856pt)
Font metrics written on eccc1095.tfm.
Output written on eccc1095.600gf (256 characters, 56408 bytes).
Transcript written on eccc1095.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/eccc1095.600pk: successfully generated.
 &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/eccc1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/
home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> 
&lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>
Output written on paper.pdf (13 pages, 201073 bytes).
Transcript written on paper.log.
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}]
Overfull \hbox (0.974pt too wide) in paragraph at lines 55--56
[]\T1/cmr/m/n/10.95 We val-i-date On-toCoDec across 2 tasks (RE, EE), 4 mod-els
 (Qwen3-8B, Llama-3.1-8B, Mistral-
[2] [3] [4] [5] [6] [7] [8]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 426.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\times' on input line 426.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 426.

[9] [10] [11]

LaTeX Warning: `h' float specifier changed to `ht'.

[12] [13] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecxc1095.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/eccc1000.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/eccc1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/
home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> 
&lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>
Output written on paper.pdf (13 pages, 204176 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e6797e6-f818-45f5-b36b-0200097e4e72",
  "isSidechain": false,
  "promptId": "9e1a4d2e-1521-4841-ba16-b71efd78ed15",
  "type": "user",
  "uuid": "8453769e-9d02-4713-bd5d-e25d2ee55bf0",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (0.974pt too wide) in paragraph at lines 55--56\n[]\\T1/cmr/m/n/10.95 We val-i-date On-toCoDec across 2 tasks (RE, EE), 4 mod-els\n (Qwen3-8B, Llama-3.1-8B, Mistral-\n\nLaTeX Warning: Reference `sec:landscape' on page 2 undefined on input line 58.\n\n\nLaTeX Warning: Reference `sec:method' on page 2 undefined on input line 59.\n\n\nLaTeX Warning: Reference `sec:ee' on page 2 undefined on input line 60.\n\n\nLaTeX Warning: Reference `sec:scale' on page 2 undefined on input line 61.\n\n[2]\n\nLaTeX Warning: Reference `tab:scierc-phase0' on page 3 undefined on input line \n87.\n\n\nLaTeX Warning: Reference `tab:docred-phase0' on page 3 undefined on input line \n117.\n\n[3] [4]\n\nLaTeX Warning: Reference `tab:scierc-ablation' on page 5 undefined on input lin\ne 199.\n\n\nLaTeX Warning: Reference `tab:docred-ablation' on page 5 undefined on input lin\ne 228.\n\n[5]\n\nLaTeX Warning: Reference `tab:crossmodel' on page 6 undefined on input line 258\n.\n\n\nLaTeX Warning: Reference `sec:analysis-tightness' on page 6 undefined on input \nline 262.\n\n\nLaTeX Warning: Reference `tab:scale70b' on page 6 undefined on input line 292.\n\n\nLaTeX Warning: Reference `tab:ee-main' on page 6 undefined on input line 323.\n\n[6]\n\nLaTeX Warning: Reference `tab:ee-ablation' on page 7 undefined on input line 35\n5.\n\n\nLaTeX Warning: Reference `tab:posthoc' on page 7 undefined on input line 377.\n\n[7] [8]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 426.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\times' on input line 426.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 426.\n\n[9] [10] [11]\n\nLaTeX Warning: Reference `tab:bootstrap-re' on page 12 undefined on input line \n523.\n\n\nLaTeX Warning: Reference `tab:bootstrap-ee' on page 12 undefined on input line \n546.\n\n[12] [13] (./paper.aux)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecxc1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecxc1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecxc1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecxc.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excsc.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excspl.mf\n Ok [25] [26] [27] [28] [29] [30] [31] [158])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170] [171]\n[172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182] [183]\n[184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.0996pt)\nFont metrics written on ecxc1095.tfm.\nOutput written on ecxc1095.600gf (256 characters, 55196 bytes).\nTranscript written on ecxc1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecxc1095.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecxc1095.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 eccc1000\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input eccc1000\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/eccc1000.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/eccc.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excsc.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excspl.mf\n Ok [25] [26] [27] [28] [29] [30] [31] [158])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170] [171]\n[172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182] [183]\n[184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.06943pt)\nFont metrics written on eccc1000.tfm.\nOutput written on eccc1000.600gf (256 characters, 51852 bytes).\nTranscript written on eccc1000.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/eccc1000.600pk: successfully generated.\n &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/eccc1000.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 eccc1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input eccc1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/eccc1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/eccc.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excsc.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excspl.mf\n Ok [25] [26] [27] [28] [29] [30] [31] [158])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170] [171]\n[172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182] [183]\n[184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.0856pt)\nFont metrics written on eccc1095.tfm.\nOutput written on eccc1095.600gf (256 characters, 56408 bytes).\nTranscript written on eccc1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/eccc1095.600pk: successfully generated.\n &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/eccc1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/\nhome/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> \n&lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>\nOutput written on paper.pdf (13 pages, 201073 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (0.974pt too wide) in paragraph at lines 55--56\n[]\\T1/cmr/m/n/10.95 We val-i-date On-toCoDec across 2 tasks (RE, EE), 4 mod-els\n (Qwen3-8B, Llama-3.1-8B, Mistral-\n[2] [3] [4] [5] [6] [7] [8]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 426.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\times' on input line 426.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 426.\n\n[9] [10] [11]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[12] [13] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecxc1095.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/eccc1000.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/eccc1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/\nhome/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> \n&lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>\nOutput written on paper.pdf (13 pages, 204176 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7e6797e6-f818-45f5-b36b-0200097e4e72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_co…",
  "leafUuid": "8453769e-9d02-4713-bd5d-e25d2ee55bf0",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2"
}
```

---

### Assistant

_source line 28 · 2026-05-18T17:01:35.384Z_

编译成功，13 页 PDF，无错误。所有交叉引用已解析。

生成文件：`paper.pdf`（13 页），包含 Abstract, Introduction, Background, Violation Landscape Study, OntoCoDec Framework, Experiments (RE SciERC/DocRED ablation, cross-model, 70B cross-scale, WikiEvents EE, post-hoc comparison, FT composability, latency), Analysis (enabling dependency, tightness×RV interaction, fallback frequency, CF tradeoff, error analysis, S1 vs S2), Related Work, Conclusion, 以及 4 个 Appendix (bootstrap CI, S2 comparison, FT composability, latency)。experiment_data.json 中全部 30 个实验均有对应 table/section 覆盖，所有数字来自 JSON 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8453769e-9d02-4713-bd5d-e25d2ee55bf0",
  "isSidechain": false,
  "requestId": "req_011CbAPmDbbLXqs3SL4uFzm7",
  "type": "assistant",
  "uuid": "4d72b4c6-a68e-4b5e-9266-788293d8e922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/best",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XC7icN8p9P5DCNeGUskLU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12027,
      "cache_read_input_tokens": 70495,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12027,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 70495,
          "cache_creation_input_tokens": 12027,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12027
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

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_co…",
  "leafUuid": "4d72b4c6-a68e-4b5e-9266-788293d8e922",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "1df8b9e0-2dfb-4e94-93b6-aca94befa4d2"
}
```

---
