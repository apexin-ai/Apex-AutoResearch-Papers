# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/16dcf9d3-8694-4893-940b-07925e20d246.jsonl`
- **Structured JSON:** [`4300d6e3fb372cb8cfcf.json`](../../sessions/43/4300d6e3fb372cb8cfcf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T10:25:32.344Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T10:25:32.344Z",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始 framing 成立，微调定位。Title 保持 'Near-Complete'，abstract 明确限定：\n'near-complete for tightly-constrained ontologies (94% DR reduction on SciERC),\nwith predictable partial reduction for complex ontologies (46-55% on DocRED)'。\n核心 novelty 三叉：(1) 首个 violation landscape 系统研究，\n(2) grammar 层完美跨数据集泛化（ET/RV→0%），\n(3) tightness-DR 相关性作为独立 analytical contribution。\nDocRED 10.19% 残留 DR 不是弱点而是 tightness theory 的验证数据点。Claims 无需降级。\nCF rate 在 DocRED 上显著低于 SciERC（~2.6% vs 9.9%），\n进一步支持 \"CF 根因是 type system 模糊性\" 论点。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T10:25:32.347Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T10:25:32.347Z",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-14T10:25:32.368Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始 framing 成立，微调定位。Title 保持 'Near-Complete'，abstract 明确限定：
'near-complete for tightly-constrained ontologies (94% DR reduction on SciERC),
with predictable partial reduction for complex ontologies (46-55% on DocRED)'。
核心 novelty 三叉：(1) 首个 violation landscape 系统研究，
(2) grammar 层完美跨数据集泛化（ET/RV→0%），
(3) tightness-DR 相关性作为独立 analytical contribution。
DocRED 10.19% 残留 DR 不是弱点而是 tightness theory 的验证数据点。Claims 无需降级。
CF rate 在 DocRED 上显著低于 SciERC（~2.6% vs 9.9%），
进一步支持 "CF 根因是 type system 模糊性" 论点。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "09bcd997-7727-4bef-8159-0d7f38bdc5f8",
  "type": "user",
  "uuid": "ff8b6cba-4686-470a-a388-d28db175908a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T10:25:32.368Z_

```json
{
  "parentUuid": "ff8b6cba-4686-470a-a388-d28db175908a",
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
  "uuid": "82e30ea2-d346-4781-9ab7-01286d4f0f22",
  "timestamp": "2026-05-14T10:25:32.368Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T10:25:32.368Z_

```json
{
  "parentUuid": "82e30ea2-d346-4781-9ab7-01286d4f0f22",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "467ffb63-df64-4f4e-882f-5479c36091ac",
  "timestamp": "2026-05-14T10:25:32.368Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
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
  "aiTitle": "Generate complete paper for dream session",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246"
}
```

---

### Assistant

_source line 7 · 2026-05-14T10:25:34.634Z_

Let me start by reading the input files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "467ffb63-df64-4f4e-882f-5479c36091ac",
  "isSidechain": false,
  "requestId": "req_011Cb2JLcpHuZGmWB1KrU2Pm",
  "type": "assistant",
  "uuid": "187e7082-9dfa-4165-a0c0-4ee733be60b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TY6v7Kyz8wVeZJmJeFvhNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11322,
      "cache_read_input_tokens": 11841,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11322
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

_source line 8 · 2026-05-14T10:25:36.032Z_

<details open><summary>🔧 Tool call — Read · `toolu_013XBsMsqaGFPs7URK7eReXz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "187e7082-9dfa-4165-a0c0-4ee733be60b5",
  "isSidechain": false,
  "requestId": "req_011Cb2JLcpHuZGmWB1KrU2Pm",
  "type": "assistant",
  "uuid": "5e9d5d1c-1260-4b60-acfc-a065f0ee4e88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TY6v7Kyz8wVeZJmJeFvhNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11322,
      "cache_read_input_tokens": 11841,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11322
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

_source line 9 · 2026-05-14T10:25:36.272Z_

<details open><summary>🔧 Tool call — Read · `toolu_019sUr6Fv7NGfEr9nhyQMR4o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e9d5d1c-1260-4b60-acfc-a065f0ee4e88",
  "isSidechain": false,
  "requestId": "req_011Cb2JLcpHuZGmWB1KrU2Pm",
  "type": "assistant",
  "uuid": "6387b384-8823-4c7a-a34b-0448f59a0a7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TY6v7Kyz8wVeZJmJeFvhNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11322,
      "cache_read_input_tokens": 11841,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11322
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

_source line 10 · 2026-05-14T10:25:36.318Z_

<details><summary>↩ Tool result · `toolu_013XBsMsqaGFPs7URK7eReXz`</summary>

```text
1	[
2	  {
3	    "name": "DocRED Phase 2 unconstrained baseline",
4	    "description": "DocRED 998 文档，Phase2 code path 无约束运行。\n验证 Phase2 环境下的 unconstrained DR 与 Phase0 一致（18-20%），\n为计算 DR reduction 提供可比基线。\n",
5	    "results": {
6	      "documents": 998,
7	      "documents_checked": 962,
8	      "parse_failures": 36,
9	      "json_parse_rate": 0.964,
10	      "total_triples": 16600,
11	      "total_entities": 19200,
12	      "entity_type_violation_rate": 0.075,
13	      "relation_vocabulary_violation_rate": 0.289,
14	      "domain_range_violation_rate": 0.19,
15	      "domain_range_violations": 3154,
16	      "cross_field_consistency_violation_rate": 0.001,
17	      "entity_f1": 59.0,
18	      "relation_f1": 8.2,
19	      "relation_precision": 7.0,
20	      "relation_recall": 9.9,
21	      "dr_reduction_full_s1_vs_unconstrained_pct": 46.4
22	    },
23	    "tables": [
24	      "Table 3: DocRED Constrained Decoding Ablation — unconstrained column",
25	      "Table 1: Cross-dataset Violation Landscape — DocRED Phase2 unconstrained row"
26	    ],
27	    "figures": [],
28	    "analysis": "关键验证点：Phase2 unconstrained DR ≈ Phase0 DR（±1pp），\n确保 reduction 计算分母可比。若偏差 >2pp 需审查 code path 差异。\n46.4% reduction 支持 \"predictable partial reduction for complex ontologies\" 叙事。\n\n\nPhase2 SciERC unconstrained 与 Phase0 完全一致（DR=15.37%），\n证明 Phase2 code path 不引入偏差。DocRED 应同样复现 Phase0 数字。\nDR 预测 19.0%（vs Phase0 18.7%）：Phase2 unconstrained 使用相同 generation 参数，\n但 code path 中的 JSON 后处理可能与 Phase0 略有差异（如 unicode 处理），\n导致少量 triples 解析方式不同，~0.3pp 方差在正常范围。\nParse rate 保持 ~96.4%——无 grammar 约束时 JSON 格式错误率是模型固有属性。\nRV=28.9% 和 ET=7.5% 复现 Phase0，均为模型在无约束下的自然错误率。\nF1 与 grammar_only(8.24) 和 full_s1(8.17) 持平，确认约束 F1-neutral。\ndr_reduction 46.4% = (19.0-10.19)/19.0，落入 best 档 [46,55] 下界。\n"
29	  },
30	  {
31	    "name": "DocRED Phase 2 semantic-only constrained decoding",
32	    "description": "仅启用 semantic 层（TypeConstraintProcessor），不启用 grammar 层。\n验证 enabling dependency 在复杂 ontology 上跨数据集复现：\n无 grammar 保障 relation vocabulary → semantic 层大面积盲区 → DR reduction 显著弱于 full_s1。\n",
33	    "results": {
34	      "documents": 998,
35	      "documents_checked": 958,
36	      "parse_failures": 40,
37	      "json_parse_rate": 0.96,
38	      "total_triples": 16500,
39	      "total_entities": 19100,
40	      "entity_type_violation_rate": 0.073,
41	      "relation_vocabulary_violation_rate": 0.287,
42	      "domain_range_violation_rate": 0.155,
43	      "domain_range_violations": 2558,
44	      "cross_field_consistency_violation_rate": 0.025,
45	      "entity_f1": 58.5,
46	      "relation_f1": 8.0,
47	      "relation_precision": 6.9,
48	      "relation_recall": 9.5,
49	      "dr_reduction_vs_unconstrained_pct": 18.4,
50	      "semantic_enabling_ratio": 2.52
51	    },
52	    "tables": [
53	      "Table 3: DocRED Constrained Decoding Ablation — semantic_only column"
54	    ],
55	    "figures": [],
56	    "analysis": "enabling_ratio=2.52 在 best 档 [2.0, 3.5] 内。\n与 SciERC(3.88) 对比，DocRED ratio 更低的原因可量化归因于 RV 差异：\nDocRED 29% triples 使用无效 relation（SciERC 仅 1.4%），semantic 盲区面积成比例增大。\n论文核心论述：grammar-enables-semantic 在 ontology 复杂度增加时**更加必要**——\nDocRED 29% RV 使 semantic 层近三分之一 triples 完全无法检查。\n\n\nEnabling dependency 机制：\n1. DocRED unconstrained RV=29%，即 ~29% triples 使用不在 ontology 中的 relation type。\n   Semantic 层对这些 triples 完全无法检查——未知 relation 查不到 domain/range 规则。\n2. 在剩余 ~71% 合法 relation type 的 triples 中，semantic 执行 domain/range 检查。\n   但无 grammar 结构保障，JSON 解析失败率 ~4%（vs grammar_only 1.5%），\n   进一步削弱 semantic 的有效覆盖面。实际 semantic 能检查的 triples 约 67-68%。\n3. DR 从 19.0% 降至 15.5%（-18.4%），远弱于 full_s1 的 46.4%。\n   SciERC 上 semantic_only reduction=24.2%，DocRED 更低（18.4%）正因 RV 更高\n   （29% vs 1.4%），semantic 盲区更大。\n4. enabling_ratio = (19.0-10.19)/(19.0-15.5) = 8.81/3.5 = 2.52。\n   Full_s1 的 DR reduction 效力是 semantic_only 的 2.52 倍。\n   SciERC ratio=3.88 更高是因为 SciERC full_s1 几乎完全消除了 DR（0.93%）。\n5. CF 升至 2.5%（vs unconstrained ~0.1%），模式与 SciERC semantic_only(2.71%) 一致：\n   semantic per-relation 独立 enforcement 引入跨 relation type 不一致。\n   DocRED CF 略低因为 DocRED entity types 语义边界更清晰。\n"
57	  },
58	  {
59	    "name": "Latency comparison (constrained vs unconstrained)",
60	    "description": "测量 unconstrained / grammar_only / semantic_only / full_s1 / full_s2\n的 tokens/second 和 wall-clock time，量化约束开销的实用性边界。\n",
61	    "results": {
62	      "scierc": {
63	        "unconstrained_tok_per_sec": 13.0,
64	        "grammar_only_tok_per_sec": 11.5,
65	        "semantic_only_tok_per_sec": 9.8,
66	        "full_s1_tok_per_sec": 9.5,
67	        "full_s2_tok_per_sec": 6.0,
68	        "overhead_ratio": {
69	          "grammar_only": 1.13,
70	          "semantic_only": 1.33,
71	          "full_s1": 1.37,
72	          "full_s2": 2.17
73	        }
74	      },
75	      "docred": {
76	        "unconstrained_tok_per_sec": 12.5,
77	        "grammar_only_tok_per_sec": 11.0,
78	        "full_s1_tok_per_sec": 9.0,
79	        "overhead_ratio": {
80	          "grammar_only": 1.14,
81	          "full_s1": 1.39
82	        }
83	      },
84	      "wall_clock_per_sample_sec": {
85	        "scierc_unconstrained": 16,
86	        "scierc_full_s1": 22,
87	        "docred_unconstrained": 64,
88	        "docred_full_s1": 89
89	      }
90	    },
91	    "tables": [
92	      "Table 6: Inference Latency Overhead (或 Appendix Table A2)"
93	    ],
94	    "figures": [],
95	    "analysis": "1.37x overhead 完全可接受。Post-hoc filtering 需重新生成 ~15% 被拒 triples\n（等效 ~1.15x 但无法引导到有效输出，且对 streaming 场景不可用）。\nS2 的 2.2x 开销 + 无质量优势，进一步确认 S1 为推荐策略。\n建议在 §5 用 1 句话报告 overhead，不需单独 section。\n\n\n1. Grammar-only 开销 ~13%：XGrammar 用 pushdown automaton + C++ backend 计算 token mask，\n   高度优化。文献报告 overhead <10%（Dong et al. 2024），但 IE schema 嵌套结构\n   比纯 JSON grammar 复杂（entity list + relation list + nested types），实际稍高。\n2. Semantic 层额外开销 ~20%：TypeConstraintProcessor 是 Python 实现，\n   每 token 需检查 entity registry 状态 + 判断生成位置 + 动态计算 logit mask。\n   Python GIL 与 GPU inference 的交互是主要瓶颈。\n3. Full_s1 ≈ semantic 开销：bitwise AND 两个 mask 是 O(vocab_size) 操作，\n   可忽略不计，所以 full_s1 ≈ max(grammar, semantic) ≈ semantic。\n4. Full_s2 ~2.2x：两个完整 forward pass，\n   Pass 2 还需编译 input-dependent grammar，额外消耗 ~0.1-0.2x。\n5. DocRED 和 SciERC 的 overhead ratio 接近（1.37 vs 1.39），\n   说明开销是 per-token 而非 per-document，与文档长度无关。\n"
96	  },
97	  {
98	    "name": "Llama-3.1-8B cross-model violation rate (SciERC)",
99	    "description": "在 Llama-3.1-8B 上复现 SciERC minimal prompt + 可选 full_s1，\n验证 violation landscape 和 grammar 泛化性的模型无关性。\n",
100	    "results": {
101	      "unconstrained": {
102	        "total_triples": 1550,
103	        "total_entities": 2200,
104	        "json_parse_rate": 0.98,
105	        "entity_type_violation_rate": 0.006,
106	        "relation_vocabulary_violation_rate": 0.025,
107	        "domain_range_violation_rate": 0.145,
108	        "cross_field_consistency_violation_rate": 0.001,
109	        "relation_f1": 6.5,
110	        "entity_f1": 28.0,
111	        "per_relation_dr": {
112	          "Used-for": 0.005,
113	          "Feature-of": 0.3,
114	          "Compare": 0.38,
115	          "Evaluate-for": 0.22,
116	          "Part-of": 0.2,
117	          "Hyponym-of": 0.12,
118	          "Conjunction": 0.0
119	        }
120	      },
121	      "grammar_only": {
122	        "entity_type_violation_rate": 0.0,
123	        "relation_vocabulary_violation_rate": 0.0,
124	        "domain_range_violation_rate": 0.14
125	      },
126	      "full_s1": {
127	        "entity_type_violation_rate": 0.0,
128	        "relation_vocabulary_violation_rate": 0.0,
129	        "domain_range_violation_rate": 0.012,
130	        "cross_field_consistency_violation_rate": 0.085,
131	        "relation_f1": 6.8
132	      },
133	      "cross_model_dr_delta_pp": {
134	        "unconstrained": -0.9,
135	        "full_s1": 0.3
136	      },
137	      "per_relation_rank_spearman": 0.89
138	    },
139	    "tables": [
140	      "Table 5: Cross-model Violation Rate Comparison"
141	    ],
142	    "figures": [],
143	    "analysis": "若 per-relation rank Spearman ρ>0.8，可额外 claim：\n\"per-relation violation susceptibility is a property of ontology constraint structure,\nnot the generating model\"。Grammar ET/RV→0% 是最干净的跨模型证据。\n注意：P012 是 stretch goal，若时间不足可降级为 appendix 或 future work，\n不影响 core claims。\n\n\n1. Llama DR ≈ 14.5%（vs Qwen 15.4%，delta=-0.9pp）：\n   Violations 主要由 ontology constraint structure 驱动。两个 8B 模型在相同 ontology 上\n   的 violation rate 高度相关——差异来源于训练数据分布（Llama 学术文本比例可能不同），\n   而非根本性的 type assignment 差异。±3pp 范围内变动。\n2. Grammar 层 ET→0%, RV→0%：grammar 约束是 CFG-expressible，\n   只依赖 tokenizer vocabulary mapping。XGrammar 自动适配 Llama 的 SentencePiece tokenizer\n   （vs Qwen 的 tiktoken-based）。ET/RV 消除是 grammar 固有能力，完全模型无关。\n3. Full_s1 DR ≈ 1.2%（vs Qwen 0.93%）：\n   残留 DR 略高因为 Llama 的 logit distribution 与 Qwen 不同——\n   semantic mask 后次优 token 是否仍违反约束，取决于模型特定的 token 概率排序。\n   但量级一致（均 <2%），确认方法泛化性。\n4. F1 略低（6.5 vs 8.23）：Llama-3.1-8B 在 zero-shot structured output 上\n   弱于 Qwen3-8B（后者有 code/structured output 针对性训练）。不影响约束效果评估。\n5. Per-relation rank Spearman ρ=0.89：两个模型的 per-relation violation 排序\n   高度一致（Compare > Feature-of > Evaluate-for > ...），因为排序由 constraint tightness 驱动。\n"
144	  },
145	  {
146	    "name": "DocRED per-relation tightness-DR Spearman correlation",
147	    "description": "从 phase2_docred_full_s1 per-relation DR 数据 + DocRED ontology constraint tightness\n计算 Spearman rank correlation。已有 Pearson r=0.3682 (n=90)。\nSpearman ρ 预期更高因为关系为单调非线性。\n",
148	    "results": {
149	      "pearson_r": 0.3682,
150	      "pearson_r_note": "已实测（来自 root cause analysis）",
151	      "spearman_rho": 0.52,
152	      "spearman_p_value": 2e-06,
153	      "n_relations_analyzed": 82,
154	      "filter_criterion": "≥10 triples per relation（排除低频噪声）",
155	      "bucket_level_trend": {
156	        "tightness_0.95_1.00": {
157	          "n_rels": 4,
158	          "agg_dr": 0.306
159	        },
160	        "tightness_0.90_0.94": {
161	          "n_rels": 15,
162	          "agg_dr": 0.193
163	        },
164	        "tightness_0.85_0.89": {
165	          "n_rels": 28,
166	          "agg_dr": 0.129
167	        },
168	        "tightness_0.80_0.84": {
169	          "n_rels": 23,
170	          "agg_dr": 0.07
171	        },
172	        "tightness_0.70_0.79": {
173	          "n_rels": 18,
174	          "agg_dr": 0.09
175	        },
176	        "tightness_lt_0.70": {
177	          "n_rels": 2,
178	          "agg_dr": 0.007
179	        }
180	      },
181	      "bucket_level_note": "Bucket data 已实测（来自 root cause analysis），展示清晰单调趋势",
182	      "top10_violation_concentration": 0.78,
183	      "extreme_relations": {
184	        "P1198_unemployment_rate": {
185	          "tightness": 0.944,
186	          "dr": 0.833,
187	          "n": 6
188	        },
189	        "P6_head_of_government": {
190	          "tightness": 0.889,
191	          "dr": 0.846,
192	          "n": 13
193	        },
194	        "P35_head_of_state": {
195	          "tightness": 0.889,
196	          "dr": 0.647,
197	          "n": 17
198	        },
199	        "P582_end_time": {
200	          "tightness": 0.917,
201	          "dr": 0.435,
202	          "n": 186
203	        },
204	        "P205_basin_country": {
205	          "tightness": 0.972,
206	          "dr": 0.37,
207	          "n": 108
208	        }
209	      }
210	    },
211	    "tables": [
212	      "Table 4: DocRED Per-relation DR by Tightness Bucket（已有 bucket 实测数据）"
213	    ],
214	    "figures": [],
215	    "analysis": "ρ=0.52 + bucket 单调趋势 + top 15 贡献 76.3% violations = 三重证据支持 tightness theory。\n论文 framing：不强调 ρ 的绝对值（0.52 不算 \"strong\"），\n而强调 (a) bucket 趋势的清晰单调性，(b) violation 的极度集中性（top 15 = 76.3%），\n(c) 实用 insight：practitioners 可从 ontology 定义直接预估约束效果。\nFig 3 scatter plot 是 paper 最重要的 figure 之一——一图讲清核心 story。\n\n\n1. Pearson r=0.37 已实测。Spearman ρ 预期更高（~0.52）因为：\n   (a) 关系是单调但非线性的——bucket 数据清晰展示从 0.7% 到 30.6% 的单调上升\n       （仅 0.70-0.79 bucket 有轻微 inversion，agg_DR=9.0% vs 0.80-0.84 的 7.0%）；\n   (b) Spearman 使用 rank，消除了 DR 右偏分布的 outlier 影响；\n   (c) 过滤 ≥10 triples 排除了低频关系的小样本噪声（这些关系 DR 要么 0% 要么 100%）。\n2. Pearson r 被低频高 DR 关系拉低：P1198_unemployment_rate（6 triples, DR=83.3%）\n   等极端值在 Pearson 下产生高杠杆效应。Spearman rank transformation 削弱此影响。\n3. 0.70-0.79 bucket inversion 的原因：该区间包含 P463_member_of（tightness=0.722,\n   DR=9.5%, n=745）——高频关系的 DR 拉高了整个 bucket 的聚合值。\n   这是个别关系的特性，不破坏整体单调趋势。\n4. ρ=0.52 位于 best 档 [0.5, 0.8] 下端，反映了 tightness 不是 DR 的唯一决定因素：\n   relation frequency、entity type distribution、model-specific prior 也有贡献。\n   但 tightness 是最强的单一预测因子，ρ=0.52 在 n=82 下 p<0.001 显著。\n"
216	  },
217	  {
218	    "name": "DocRED CF violation root cause analysis",
219	    "description": "对 phase2_docred_full_s1 的 519 个 CF violations 进行子类型分解，\n与 SciERC CF 模式对比验证 type system ambiguity 假说。\n",
220	    "results": {
221	      "cf_violations": 519,
222	      "cf_denominator_entities": 20218,
223	      "cf_rate": 0.0257,
224	      "evr_count": 460,
225	      "evr_fraction_of_cf": 0.886,
226	      "evr_entity_rate": 0.023,
227	      "within_rel_count": 50,
228	      "within_rel_fraction": 0.096,
229	      "top_conflict_patterns": [
230	        {
231	          "pattern": "ORG↔LOC",
232	          "count": 120,
233	          "pct_of_cf": 0.231,
234	          "example": "国家名在 country_of_citizenship 中标 LOC, 在 headquarters 中标 ORG"
235	        },
236	        {
237	          "pattern": "PER↔ORG",
238	          "count": 85,
239	          "pct_of_cf": 0.164,
240	          "example": "王朝/政权名在 head_of_state 中标 ORG, 在 instance_of 中标 PER"
241	        },
242	        {
243	          "pattern": "TIME↔NUM",
244	          "count": 65,
245	          "pct_of_cf": 0.125,
246	          "example": "年份在 date_of_birth 中标 TIME, 在 P571_inception 中标 NUM"
247	        }
248	      ],
249	      "ablation_evidence": {
250	        "grammar_only_cf": 14,
251	        "grammar_only_cf_rate": 0.0007,
252	        "full_s1_cf": 519,
253	        "full_s1_cf_rate": 0.0257,
254	        "delta": 505,
255	        "semantic_attribution": "100% — 505/505 增量 CF 来自 semantic 层"
256	      },
257	      "cross_dataset_comparison": {
258	        "scierc_cf": 0.099,
259	        "docred_cf": 0.026,
260	        "ratio": 3.8,
261	        "explanation": "DocRED entity types (PER/ORG/LOC/TIME/NUM/MISC) 语义边界远清晰于 SciERC (Generic/OtherScientificTerm/Material/Method)"
262	      },
263	      "trade_off_ratio": {
264	        "dr_reduction_pp": 8.81,
265	        "cf_increase_pp": 2.47,
266	        "benefit_cost": 3.57
267	      }
268	    },
269	    "tables": [
270	      "Table 5: CF Analysis — Sub-type Breakdown and Cross-dataset Comparison"
271	    ],
272	    "figures": [],
273	    "analysis": "DocRED CF=2.57% 在 best 档 [2%, 3%] 内。\nCross-dataset CF 对比（2.57% vs 9.9%）为 \"CF 根因是 type system ambiguity\" 提供强证据：\ntype system 边界越模糊 → CF 越高。这个 finding 应在 §5.3 展开（独立 insight 价值），\n同时 §7 保留 CF 作为 limitation + future work（global entity-type consensus）。\n论文绝不能暗示 \"因为 DocRED CF 低所以 CF 问题不重要\"——SciERC 9.9% 仍然 non-trivial。\n\n\n1. CF=2.57% 远低于 SciERC 9.9%：核心原因是 type system 语义清晰度差异。\n   DocRED 的 PER/ORG/LOC/TIME/NUM/MISC 在绝大多数上下文中有明确分类标准\n   （人名=PER, 组织=ORG, 地名=LOC），边界模糊区域有限（主要是 ORG↔LOC 的国家实体）。\n   SciERC 的 Generic/OtherScientificTerm/Material/Method 在学术领域大量重叠\n   （\"neural network\" 可以是 Method 也可以是 OtherScientificTerm）。\n2. EVR 占 89%（vs SciERC >90%）：子类型分布一致。EVR = 同一 entity 在 entity list\n   和 relation triple 中被赋予不同 type，根因是 semantic 层按 relation-specific\n   domain/range 约束选择 type，不维护全局 entity-type 一致性。\n3. ORG↔LOC 是最大冲突模式（23%）：这是 NER 领域公认的困难 case——\n   国家/城市作为政治实体(ORG) vs 地理实体(LOC) 是 type system 设计的固有模糊区。\n4. Grammar_only CF=14（0.07%）→ full_s1 CF=519（2.57%），增量 100% 来自 semantic 层。\n   干净的消融证据：grammar 不引入 CF，CF 是 semantic type enforcement 的系统性副作用。\n5. Trade-off ratio 3.57:1（每增加 1pp CF 换取 3.57pp DR reduction）。\n   结合 DR=hard constraint（triple 不可用）vs CF=soft preference（individual triples 仍 valid），\n   trade-off 高度有利。DocRED 上比 SciERC（93pp/10pp=9.3:1）差但仍 positive。\n"
274	  },
275	  {
276	    "name": "Cross-dataset grammar layer generalization verification",
277	    "description": "系统性汇总 grammar 层在 SciERC（7 relations）和 DocRED（96 relations）上\n的 ET/RV 消除率，确认完美泛化作为独立贡献。\n",
278	    "results": {
279	      "scierc_grammar_only": {
280	        "et_violation_rate": 0.0,
281	        "rv_violation_rate": 0.0,
282	        "et_violations": 0,
283	        "rv_violations": 0,
284	        "total_triples": 1725
285	      },
286	      "docred_grammar_only": {
287	        "et_violation_rate": 0.0,
288	        "rv_violation_rate": 0.0003,
289	        "et_violations": 0,
290	        "rv_violations": 5,
291	        "total_triples": 17341
292	      },
293	      "scierc_full_s1": {
294	        "et_violation_rate": 0.0,
295	        "rv_violation_rate": 0.0
296	      },
297	      "docred_full_s1": {
298	        "et_violation_rate": 0.0,
299	        "rv_violation_rate": 0.0003
300	      },
301	      "cross_dataset_summary": {
302	        "et_elimination": "100% on both datasets (0/1725 SciERC, 0/17341 DocRED)",
303	        "rv_elimination": "100% SciERC (0/1725), 99.97% DocRED (5/17341)",
304	        "ontology_size_invariance": "7 relations → 96 relations (14x) with no degradation"
305	      }
306	    },
307	    "tables": [
308	      "Table 2/3: ET 和 RV 列横跨所有配置和数据集"
309	    ],
310	    "figures": [],
311	    "analysis": "Grammar 完美泛化是 paper 的 \"clean win\"，无需 caveat。\n建议 §5 第一段就报告此 finding（ET/RV→0% across datasets），\n先给 reviewer 一个 unambiguously positive result，建立信任后再讨论 DR 的 nuance。\n论文可 claim：\"Grammar-constrained decoding is a solved problem for ontology vocabulary\nand entity type compliance in IE—it scales perfectly from 7 to 96 relation types.\"\n\n\n1. ET/RV 是 CFG-expressible constraints：entity_type ∈ {valid_types},\n   relation_type ∈ {valid_relations}。XGrammar pushdown automaton 可精确 enforce，\n   不依赖生成历史或语义状态，因此与模型和 ontology 大小无关。\n2. SciERC ET=0, RV=0 完美。DocRED ET=0 完美；RV=5/17341=0.03% 有微小残留。\n   这 5 个 RV 可能源于 tokenizer 边界效应——DocRED 某些 relation name\n   （如 P1001_applies_to_jurisdiction）在 tokenization 时可能触发 XGrammar\n   的 token boundary edge case。5/17341 是 noise level，不影响结论。\n3. 从 7 relations 到 96 relations（14x），ET/RV 消除率保持 99.97-100%。\n   Grammar compilation 自动将 ontology schema 转化为 CFG，\n   schema size 只增加 production rule 数量，不降低 enforcement 精确性。\n4. 数据已全部就位（来自 phase2_scierc_grammar_only 和 phase2_docred_grammar_only），\n   这是 compilation + formatting，不需新实验。\n"
312	  },
313	  {
314	    "name": "DocRED per-relation DR bimodal distribution analysis",
315	    "description": "分析 96 个 DocRED relations 的 full_s1 per-relation DR 分布形态，\n验证 >65% 关系 DR<2% 的双峰假设。\n",
316	    "results": {
317	      "total_relations": 96,
318	      "active_relations": 87,
319	      "filter_5plus_triples": 82,
320	      "dr_distribution": {
321	        "dr_eq_0pct": 18,
322	        "dr_lt_2pct": 55,
323	        "dr_2_to_10pct": 12,
324	        "dr_10_to_20pct": 7,
325	        "dr_20_to_40pct": 6,
326	        "dr_gt_40pct": 8
327	      },
328	      "near_zero_fraction": 0.67,
329	      "near_zero_fraction_note": "55/82 = 67%（≥5 triples 的 relations 中 DR<2%）",
330	      "distribution_statistics": {
331	        "median_dr": 0.008,
332	        "mean_dr": 0.102,
333	        "mean_median_ratio": 12.75,
334	        "std_dr": 0.18,
335	        "skewness": 2.1,
336	        "gini_coefficient": 0.82
337	      },
338	      "top15_concentration": 0.763,
339	      "top15_concentration_note": "已实测：top 15 relations 贡献 1352/1771 = 76.3% 总违规"
340	    },
341	    "tables": [
342	      "Table 4: DocRED Per-relation DR Summary Statistics"
343	    ],
344	    "figures": [],
345	    "analysis": "near_zero_fraction=67% 在 best 档 [65%, 80%] 下端。\n这个分布图的论文价值：visually 传达 \"10.19% overall DR 不是均匀分布的失败\"——\n对 2/3 的 relations，constrained decoding 已实现 near-complete compliance；\n残留 DR 集中在可预测的少数 high-tightness relations。\nFig 2 + Fig 3 (tightness scatter) 构成核心 evidence pair：\n分布展示现象（双峰），scatter 解释机制（tightness 驱动）。\n\n1. 67% relations DR<2%（best 档下界 65%）：DocRED 虽然 avg tightness=0.842（高），\n   但 tightness 分布也有 variance——0.70-0.84 区间的 41 个 relations 中，\n   许多的实际 DR 较低是因为 (a) 高频 entity types（PER, ORG, LOC）自然匹配这些 relation\n   的 domain/range，(b) 模型的 distributional prior 与 ontology 约束高度对齐。\n   仅在 tightness 极高（>0.90）时，prior-constraint mismatch 才产生显著 DR。\n2. Mean>>Median（12.75x）：经典 heavy-tail 特征。\n   8 个 DR>40% 的 extreme relations（P1198, P6, P171, P35 等，全部 tightness>0.88）\n   将 mean 拉至 10.2%（= overall 10.19%），但 median 0.8% 代表 \"典型\" relation 体验。\n3. Gini=0.82：violation 分布极不平等。类比帕累托法则：~12% 的 relations 贡献 ~80% violations。\n   这不是随机噪声，而是 ontology constraint structure 的系统性产物。\n4. 双峰形成机制：constraint tightness 作为 bifurcation parameter——\n   tightness < ~0.80 时 semantic mask 只排除少量 low-probability tokens，\n   model 自然分布已近乎合法，DR→0%（左峰）；\n   tightness > ~0.90 时 mask 必须排除 high-probability tokens，\n   model 被迫使用低概率 token，DR 急剧上升（右尾）。\n   0.80-0.90 是 transition zone，DR 分散，中间 bin 较薄。\n"
346	  }
347	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e9d5d1c-1260-4b60-acfc-a065f0ee4e88",
  "isSidechain": false,
  "promptId": "09bcd997-7727-4bef-8159-0d7f38bdc5f8",
  "type": "user",
  "uuid": "43ac909f-26ce-499b-82a8-c7690fad3f6b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"DocRED Phase 2 unconstrained baseline\",\n    \"description\": \"DocRED 998 文档，Phase2 code path 无约束运行。\\n验证 Phase2 环境下的 unconstrained DR 与 Phase0 一致（18-20%），\\n为计算 DR reduction 提供可比基线。\\n\",\n    \"results\": {\n      \"documents\": 998,\n      \"documents_checked\": 962,\n      \"parse_failures\": 36,\n      \"json_parse_rate\": 0.964,\n      \"total_triples\": 16600,\n      \"total_entities\": 19200,\n      \"entity_type_violation_rate\": 0.075,\n      \"relation_vocabulary_violation_rate\": 0.289,\n      \"domain_range_violation_rate\": 0.19,\n      \"domain_range_violations\": 3154,\n      \"cross_field_consistency_violation_rate\": 0.001,\n      \"entity_f1\": 59.0,\n      \"relation_f1\": 8.2,\n      \"relation_precision\": 7.0,\n      \"relation_recall\": 9.9,\n      \"dr_reduction_full_s1_vs_unconstrained_pct\": 46.4\n    },\n    \"tables\": [\n      \"Table 3: DocRED Constrained Decoding Ablation — unconstrained column\",\n      \"Table 1: Cross-dataset Violation Landscape — DocRED Phase2 unconstrained row\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"关键验证点：Phase2 unconstrained DR ≈ Phase0 DR（±1pp），\\n确保 reduction 计算分母可比。若偏差 >2pp 需审查 code path 差异。\\n46.4% reduction 支持 \\\"predictable partial reduction for complex ontologies\\\" 叙事。\\n\\n\\nPhase2 SciERC unconstrained 与 Phase0 完全一致（DR=15.37%），\\n证明 Phase2 code path 不引入偏差。DocRED 应同样复现 Phase0 数字。\\nDR 预测 19.0%（vs Phase0 18.7%）：Phase2 unconstrained 使用相同 generation 参数，\\n但 code path 中的 JSON 后处理可能与 Phase0 略有差异（如 unicode 处理），\\n导致少量 triples 解析方式不同，~0.3pp 方差在正常范围。\\nParse rate 保持 ~96.4%——无 grammar 约束时 JSON 格式错误率是模型固有属性。\\nRV=28.9% 和 ET=7.5% 复现 Phase0，均为模型在无约束下的自然错误率。\\nF1 与 grammar_only(8.24) 和 full_s1(8.17) 持平，确认约束 F1-neutral。\\ndr_reduction 46.4% = (19.0-10.19)/19.0，落入 best 档 [46,55] 下界。\\n\"\n  },\n  {\n    \"name\": \"DocRED Phase 2 semantic-only constrained decoding\",\n    \"description\": \"仅启用 semantic 层（TypeConstraintProcessor），不启用 grammar 层。\\n验证 enabling dependency 在复杂 ontology 上跨数据集复现：\\n无 grammar 保障 relation vocabulary → semantic 层大面积盲区 → DR reduction 显著弱于 full_s1。\\n\",\n    \"results\": {\n      \"documents\": 998,\n      \"documents_checked\": 958,\n      \"parse_failures\": 40,\n      \"json_parse_rate\": 0.96,\n      \"total_triples\": 16500,\n      \"total_entities\": 19100,\n      \"entity_type_violation_rate\": 0.073,\n      \"relation_vocabulary_violation_rate\": 0.287,\n      \"domain_range_violation_rate\": 0.155,\n      \"domain_range_violations\": 2558,\n      \"cross_field_consistency_violation_rate\": 0.025,\n      \"entity_f1\": 58.5,\n      \"relation_f1\": 8.0,\n      \"relation_precision\": 6.9,\n      \"relation_recall\": 9.5,\n      \"dr_reduction_vs_unconstrained_pct\": 18.4,\n      \"semantic_enabling_ratio\": 2.52\n    },\n    \"tables\": [\n      \"Table 3: DocRED Constrained Decoding Ablation — semantic_only column\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"enabling_ratio=2.52 在 best 档 [2.0, 3.5] 内。\\n与 SciERC(3.88) 对比，DocRED ratio 更低的原因可量化归因于 RV 差异：\\nDocRED 29% triples 使用无效 relation（SciERC 仅 1.4%），semantic 盲区面积成比例增大。\\n论文核心论述：grammar-enables-semantic 在 ontology 复杂度增加时**更加必要**——\\nDocRED 29% RV 使 semantic 层近三分之一 triples 完全无法检查。\\n\\n\\nEnabling dependency 机制：\\n1. DocRED unconstrained RV=29%，即 ~29% triples 使用不在 ontology 中的 relation type。\\n   Semantic 层对这些 triples 完全无法检查——未知 relation 查不到 domain/range 规则。\\n2. 在剩余 ~71% 合法 relation type 的 triples 中，semantic 执行 domain/range 检查。\\n   但无 grammar 结构保障，JSON 解析失败率 ~4%（vs grammar_only 1.5%），\\n   进一步削弱 semantic 的有效覆盖面。实际 semantic 能检查的 triples 约 67-68%。\\n3. DR 从 19.0% 降至 15.5%（-18.4%），远弱于 full_s1 的 46.4%。\\n   SciERC 上 semantic_only reduction=24.2%，DocRED 更低（18.4%）正因 RV 更高\\n   （29% vs 1.4%），semantic 盲区更大。\\n4. enabling_ratio = (19.0-10.19)/(19.0-15.5) = 8.81/3.5 = 2.52。\\n   Full_s1 的 DR reduction 效力是 semantic_only 的 2.52 倍。\\n   SciERC ratio=3.88 更高是因为 SciERC full_s1 几乎完全消除了 DR（0.93%）。\\n5. CF 升至 2.5%（vs unconstrained ~0.1%），模式与 SciERC semantic_only(2.71%) 一致：\\n   semantic per-relation 独立 enforcement 引入跨 relation type 不一致。\\n   DocRED CF 略低因为 DocRED entity types 语义边界更清晰。\\n\"\n  },\n  {\n    \"name\": \"Latency comparison (constrained vs unconstrained)\",\n    \"description\": \"测量 unconstrained / grammar_only / semantic_only / full_s1 / full_s2\\n的 tokens/second 和 wall-clock time，量化约束开销的实用性边界。\\n\",\n    \"results\": {\n      \"scierc\": {\n        \"unconstrained_tok_per_sec\": 13.0,\n        \"grammar_only_tok_per_sec\": 11.5,\n        \"semantic_only_tok_per_sec\": 9.8,\n        \"full_s1_tok_per_sec\": 9.5,\n        \"full_s2_tok_per_sec\": 6.0,\n        \"overhead_ratio\": {\n          \"grammar_only\": 1.13,\n          \"semantic_only\": 1.33,\n          \"full_s1\": 1.37,\n          \"full_s2\": 2.17\n        }\n      },\n      \"docred\": {\n        \"unconstrained_tok_per_sec\": 12.5,\n        \"grammar_only_tok_per_sec\": 11.0,\n        \"full_s1_tok_per_sec\": 9.0,\n        \"overhead_ratio\": {\n          \"grammar_only\": 1.14,\n          \"full_s1\": 1.39\n        }\n      },\n      \"wall_clock_per_sample_sec\": {\n        \"scierc_unconstrained\": 16,\n        \"scierc_full_s1\": 22,\n        \"docred_unconstrained\": 64,\n        \"docred_full_s1\": 89\n      }\n    },\n    \"tables\": [\n      \"Table 6: Inference Latency Overhead (或 Appendix Table A2)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"1.37x overhead 完全可接受。Post-hoc filtering 需重新生成 ~15% 被拒 triples\\n（等效 ~1.15x 但无法引导到有效输出，且对 streaming 场景不可用）。\\nS2 的 2.2x 开销 + 无质量优势，进一步确认 S1 为推荐策略。\\n建议在 §5 用 1 句话报告 overhead，不需单独 section。\\n\\n\\n1. Grammar-only 开销 ~13%：XGrammar 用 pushdown automaton + C++ backend 计算 token mask，\\n   高度优化。文献报告 overhead <10%（Dong et al. 2024），但 IE schema 嵌套结构\\n   比纯 JSON grammar 复杂（entity list + relation list + nested types），实际稍高。\\n2. Semantic 层额外开销 ~20%：TypeConstraintProcessor 是 Python 实现，\\n   每 token 需检查 entity registry 状态 + 判断生成位置 + 动态计算 logit mask。\\n   Python GIL 与 GPU inference 的交互是主要瓶颈。\\n3. Full_s1 ≈ semantic 开销：bitwise AND 两个 mask 是 O(vocab_size) 操作，\\n   可忽略不计，所以 full_s1 ≈ max(grammar, semantic) ≈ semantic。\\n4. Full_s2 ~2.2x：两个完整 forward pass，\\n   Pass 2 还需编译 input-dependent grammar，额外消耗 ~0.1-0.2x。\\n5. DocRED 和 SciERC 的 overhead ratio 接近（1.37 vs 1.39），\\n   说明开销是 per-token 而非 per-document，与文档长度无关。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B cross-model violation rate (SciERC)\",\n    \"description\": \"在 Llama-3.1-8B 上复现 SciERC minimal prompt + 可选 full_s1，\\n验证 violation landscape 和 grammar 泛化性的模型无关性。\\n\",\n    \"results\": {\n      \"unconstrained\": {\n        \"total_triples\": 1550,\n        \"total_entities\": 2200,\n        \"json_parse_rate\": 0.98,\n        \"entity_type_violation_rate\": 0.006,\n        \"relation_vocabulary_violation_rate\": 0.025,\n        \"domain_range_violation_rate\": 0.145,\n        \"cross_field_consistency_violation_rate\": 0.001,\n        \"relation_f1\": 6.5,\n        \"entity_f1\": 28.0,\n        \"per_relation_dr\": {\n          \"Used-for\": 0.005,\n          \"Feature-of\": 0.3,\n          \"Compare\": 0.38,\n          \"Evaluate-for\": 0.22,\n          \"Part-of\": 0.2,\n          \"Hyponym-of\": 0.12,\n          \"Conjunction\": 0.0\n        }\n      },\n      \"grammar_only\": {\n        \"entity_type_violation_rate\": 0.0,\n        \"relation_vocabulary_violation_rate\": 0.0,\n        \"domain_range_violation_rate\": 0.14\n      },\n      \"full_s1\": {\n        \"entity_type_violation_rate\": 0.0,\n        \"relation_vocabulary_violation_rate\": 0.0,\n        \"domain_range_violation_rate\": 0.012,\n        \"cross_field_consistency_violation_rate\": 0.085,\n        \"relation_f1\": 6.8\n      },\n      \"cross_model_dr_delta_pp\": {\n        \"unconstrained\": -0.9,\n        \"full_s1\": 0.3\n      },\n      \"per_relation_rank_spearman\": 0.89\n    },\n    \"tables\": [\n      \"Table 5: Cross-model Violation Rate Comparison\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"若 per-relation rank Spearman ρ>0.8，可额外 claim：\\n\\\"per-relation violation susceptibility is a property of ontology constraint structure,\\nnot the generating model\\\"。Grammar ET/RV→0% 是最干净的跨模型证据。\\n注意：P012 是 stretch goal，若时间不足可降级为 appendix 或 future work，\\n不影响 core claims。\\n\\n\\n1. Llama DR ≈ 14.5%（vs Qwen 15.4%，delta=-0.9pp）：\\n   Violations 主要由 ontology constraint structure 驱动。两个 8B 模型在相同 ontology 上\\n   的 violation rate 高度相关——差异来源于训练数据分布（Llama 学术文本比例可能不同），\\n   而非根本性的 type assignment 差异。±3pp 范围内变动。\\n2. Grammar 层 ET→0%, RV→0%：grammar 约束是 CFG-expressible，\\n   只依赖 tokenizer vocabulary mapping。XGrammar 自动适配 Llama 的 SentencePiece tokenizer\\n   （vs Qwen 的 tiktoken-based）。ET/RV 消除是 grammar 固有能力，完全模型无关。\\n3. Full_s1 DR ≈ 1.2%（vs Qwen 0.93%）：\\n   残留 DR 略高因为 Llama 的 logit distribution 与 Qwen 不同——\\n   semantic mask 后次优 token 是否仍违反约束，取决于模型特定的 token 概率排序。\\n   但量级一致（均 <2%），确认方法泛化性。\\n4. F1 略低（6.5 vs 8.23）：Llama-3.1-8B 在 zero-shot structured output 上\\n   弱于 Qwen3-8B（后者有 code/structured output 针对性训练）。不影响约束效果评估。\\n5. Per-relation rank Spearman ρ=0.89：两个模型的 per-relation violation 排序\\n   高度一致（Compare > Feature-of > Evaluate-for > ...），因为排序由 constraint tightness 驱动。\\n\"\n  },\n  {\n    \"name\": \"DocRED per-relation tightness-DR Spearman correlation\",\n    \"description\": \"从 phase2_docred_full_s1 per-relation DR 数据 + DocRED ontology constraint tightness\\n计算 Spearman rank correlation。已有 Pearson r=0.3682 (n=90)。\\nSpearman ρ 预期更高因为关系为单调非线性。\\n\",\n    \"results\": {\n      \"pearson_r\": 0.3682,\n      \"pearson_r_note\": \"已实测（来自 root cause analysis）\",\n      \"spearman_rho\": 0.52,\n      \"spearman_p_value\": 2e-06,\n      \"n_relations_analyzed\": 82,\n      \"filter_criterion\": \"≥10 triples per relation（排除低频噪声）\",\n      \"bucket_level_trend\": {\n        \"tightness_0.95_1.00\": {\n          \"n_rels\": 4,\n          \"agg_dr\": 0.306\n        },\n        \"tightness_0.90_0.94\": {\n          \"n_rels\": 15,\n          \"agg_dr\": 0.193\n        },\n        \"tightness_0.85_0.89\": {\n          \"n_rels\": 28,\n          \"agg_dr\": 0.129\n        },\n        \"tightness_0.80_0.84\": {\n          \"n_rels\": 23,\n          \"agg_dr\": 0.07\n        },\n        \"tightness_0.70_0.79\": {\n          \"n_rels\": 18,\n          \"agg_dr\": 0.09\n        },\n        \"tightness_lt_0.70\": {\n          \"n_rels\": 2,\n          \"agg_dr\": 0.007\n        }\n      },\n      \"bucket_level_note\": \"Bucket data 已实测（来自 root cause analysis），展示清晰单调趋势\",\n      \"top10_violation_concentration\": 0.78,\n      \"extreme_relations\": {\n        \"P1198_unemployment_rate\": {\n          \"tightness\": 0.944,\n          \"dr\": 0.833,\n          \"n\": 6\n        },\n        \"P6_head_of_government\": {\n          \"tightness\": 0.889,\n          \"dr\": 0.846,\n          \"n\": 13\n        },\n        \"P35_head_of_state\": {\n          \"tightness\": 0.889,\n          \"dr\": 0.647,\n          \"n\": 17\n        },\n        \"P582_end_time\": {\n          \"tightness\": 0.917,\n          \"dr\": 0.435,\n          \"n\": 186\n        },\n        \"P205_basin_country\": {\n          \"tightness\": 0.972,\n          \"dr\": 0.37,\n          \"n\": 108\n        }\n      }\n    },\n    \"tables\": [\n      \"Table 4: DocRED Per-relation DR by Tightness Bucket（已有 bucket 实测数据）\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"ρ=0.52 + bucket 单调趋势 + top 15 贡献 76.3% violations = 三重证据支持 tightness theory。\\n论文 framing：不强调 ρ 的绝对值（0.52 不算 \\\"strong\\\"），\\n而强调 (a) bucket 趋势的清晰单调性，(b) violation 的极度集中性（top 15 = 76.3%），\\n(c) 实用 insight：practitioners 可从 ontology 定义直接预估约束效果。\\nFig 3 scatter plot 是 paper 最重要的 figure 之一——一图讲清核心 story。\\n\\n\\n1. Pearson r=0.37 已实测。Spearman ρ 预期更高（~0.52）因为：\\n   (a) 关系是单调但非线性的——bucket 数据清晰展示从 0.7% 到 30.6% 的单调上升\\n       （仅 0.70-0.79 bucket 有轻微 inversion，agg_DR=9.0% vs 0.80-0.84 的 7.0%）；\\n   (b) Spearman 使用 rank，消除了 DR 右偏分布的 outlier 影响；\\n   (c) 过滤 ≥10 triples 排除了低频关系的小样本噪声（这些关系 DR 要么 0% 要么 100%）。\\n2. Pearson r 被低频高 DR 关系拉低：P1198_unemployment_rate（6 triples, DR=83.3%）\\n   等极端值在 Pearson 下产生高杠杆效应。Spearman rank transformation 削弱此影响。\\n3. 0.70-0.79 bucket inversion 的原因：该区间包含 P463_member_of（tightness=0.722,\\n   DR=9.5%, n=745）——高频关系的 DR 拉高了整个 bucket 的聚合值。\\n   这是个别关系的特性，不破坏整体单调趋势。\\n4. ρ=0.52 位于 best 档 [0.5, 0.8] 下端，反映了 tightness 不是 DR 的唯一决定因素：\\n   relation frequency、entity type distribution、model-specific prior 也有贡献。\\n   但 tightness 是最强的单一预测因子，ρ=0.52 在 n=82 下 p<0.001 显著。\\n\"\n  },\n  {\n    \"name\": \"DocRED CF violation root cause analysis\",\n    \"description\": \"对 phase2_docred_full_s1 的 519 个 CF violations 进行子类型分解，\\n与 SciERC CF 模式对比验证 type system ambiguity 假说。\\n\",\n    \"results\": {\n      \"cf_violations\": 519,\n      \"cf_denominator_entities\": 20218,\n      \"cf_rate\": 0.0257,\n      \"evr_count\": 460,\n      \"evr_fraction_of_cf\": 0.886,\n      \"evr_entity_rate\": 0.023,\n      \"within_rel_count\": 50,\n      \"within_rel_fraction\": 0.096,\n      \"top_conflict_patterns\": [\n        {\n          \"pattern\": \"ORG↔LOC\",\n          \"count\": 120,\n          \"pct_of_cf\": 0.231,\n          \"example\": \"国家名在 country_of_citizenship 中标 LOC, 在 headquarters 中标 ORG\"\n        },\n        {\n          \"pattern\": \"PER↔ORG\",\n          \"count\": 85,\n          \"pct_of_cf\": 0.164,\n          \"example\": \"王朝/政权名在 head_of_state 中标 ORG, 在 instance_of 中标 PER\"\n        },\n        {\n          \"pattern\": \"TIME↔NUM\",\n          \"count\": 65,\n          \"pct_of_cf\": 0.125,\n          \"example\": \"年份在 date_of_birth 中标 TIME, 在 P571_inception 中标 NUM\"\n        }\n      ],\n      \"ablation_evidence\": {\n        \"grammar_only_cf\": 14,\n        \"grammar_only_cf_rate\": 0.0007,\n        \"full_s1_cf\": 519,\n        \"full_s1_cf_rate\": 0.0257,\n        \"delta\": 505,\n        \"semantic_attribution\": \"100% — 505/505 增量 CF 来自 semantic 层\"\n      },\n      \"cross_dataset_comparison\": {\n        \"scierc_cf\": 0.099,\n        \"docred_cf\": 0.026,\n        \"ratio\": 3.8,\n        \"explanation\": \"DocRED entity types (PER/ORG/LOC/TIME/NUM/MISC) 语义边界远清晰于 SciERC (Generic/OtherScientificTerm/Material/Method)\"\n      },\n      \"trade_off_ratio\": {\n        \"dr_reduction_pp\": 8.81,\n        \"cf_increase_pp\": 2.47,\n        \"benefit_cost\": 3.57\n      }\n    },\n    \"tables\": [\n      \"Table 5: CF Analysis — Sub-type Breakdown and Cross-dataset Comparison\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"DocRED CF=2.57% 在 best 档 [2%, 3%] 内。\\nCross-dataset CF 对比（2.57% vs 9.9%）为 \\\"CF 根因是 type system ambiguity\\\" 提供强证据：\\ntype system 边界越模糊 → CF 越高。这个 finding 应在 §5.3 展开（独立 insight 价值），\\n同时 §7 保留 CF 作为 limitation + future work（global entity-type consensus）。\\n论文绝不能暗示 \\\"因为 DocRED CF 低所以 CF 问题不重要\\\"——SciERC 9.9% 仍然 non-trivial。\\n\\n\\n1. CF=2.57% 远低于 SciERC 9.9%：核心原因是 type system 语义清晰度差异。\\n   DocRED 的 PER/ORG/LOC/TIME/NUM/MISC 在绝大多数上下文中有明确分类标准\\n   （人名=PER, 组织=ORG, 地名=LOC），边界模糊区域有限（主要是 ORG↔LOC 的国家实体）。\\n   SciERC 的 Generic/OtherScientificTerm/Material/Method 在学术领域大量重叠\\n   （\\\"neural network\\\" 可以是 Method 也可以是 OtherScientificTerm）。\\n2. EVR 占 89%（vs SciERC >90%）：子类型分布一致。EVR = 同一 entity 在 entity list\\n   和 relation triple 中被赋予不同 type，根因是 semantic 层按 relation-specific\\n   domain/range 约束选择 type，不维护全局 entity-type 一致性。\\n3. ORG↔LOC 是最大冲突模式（23%）：这是 NER 领域公认的困难 case——\\n   国家/城市作为政治实体(ORG) vs 地理实体(LOC) 是 type system 设计的固有模糊区。\\n4. Grammar_only CF=14（0.07%）→ full_s1 CF=519（2.57%），增量 100% 来自 semantic 层。\\n   干净的消融证据：grammar 不引入 CF，CF 是 semantic type enforcement 的系统性副作用。\\n5. Trade-off ratio 3.57:1（每增加 1pp CF 换取 3.57pp DR reduction）。\\n   结合 DR=hard constraint（triple 不可用）vs CF=soft preference（individual triples 仍 valid），\\n   trade-off 高度有利。DocRED 上比 SciERC（93pp/10pp=9.3:1）差但仍 positive。\\n\"\n  },\n  {\n    \"name\": \"Cross-dataset grammar layer generalization verification\",\n    \"description\": \"系统性汇总 grammar 层在 SciERC（7 relations）和 DocRED（96 relations）上\\n的 ET/RV 消除率，确认完美泛化作为独立贡献。\\n\",\n    \"results\": {\n      \"scierc_grammar_only\": {\n        \"et_violation_rate\": 0.0,\n        \"rv_violation_rate\": 0.0,\n        \"et_violations\": 0,\n        \"rv_violations\": 0,\n        \"total_triples\": 1725\n      },\n      \"docred_grammar_only\": {\n        \"et_violation_rate\": 0.0,\n        \"rv_violation_rate\": 0.0003,\n        \"et_violations\": 0,\n        \"rv_violations\": 5,\n        \"total_triples\": 17341\n      },\n      \"scierc_full_s1\": {\n        \"et_violation_rate\": 0.0,\n        \"rv_violation_rate\": 0.0\n      },\n      \"docred_full_s1\": {\n        \"et_violation_rate\": 0.0,\n        \"rv_violation_rate\": 0.0003\n      },\n      \"cross_dataset_summary\": {\n        \"et_elimination\": \"100% on both datasets (0/1725 SciERC, 0/17341 DocRED)\",\n        \"rv_elimination\": \"100% SciERC (0/1725), 99.97% DocRED (5/17341)\",\n        \"ontology_size_invariance\": \"7 relations → 96 relations (14x) with no degradation\"\n      }\n    },\n    \"tables\": [\n      \"Table 2/3: ET 和 RV 列横跨所有配置和数据集\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Grammar 完美泛化是 paper 的 \\\"clean win\\\"，无需 caveat。\\n建议 §5 第一段就报告此 finding（ET/RV→0% across datasets），\\n先给 reviewer 一个 unambiguously positive result，建立信任后再讨论 DR 的 nuance。\\n论文可 claim：\\\"Grammar-constrained decoding is a solved problem for ontology vocabulary\\nand entity type compliance in IE—it scales perfectly from 7 to 96 relation types.\\\"\\n\\n\\n1. ET/RV 是 CFG-expressible constraints：entity_type ∈ {valid_types},\\n   relation_type ∈ {valid_relations}。XGrammar pushdown automaton 可精确 enforce，\\n   不依赖生成历史或语义状态，因此与模型和 ontology 大小无关。\\n2. SciERC ET=0, RV=0 完美。DocRED ET=0 完美；RV=5/17341=0.03% 有微小残留。\\n   这 5 个 RV 可能源于 tokenizer 边界效应——DocRED 某些 relation name\\n   （如 P1001_applies_to_jurisdiction）在 tokenization 时可能触发 XGrammar\\n   的 token boundary edge case。5/17341 是 noise level，不影响结论。\\n3. 从 7 relations 到 96 relations（14x），ET/RV 消除率保持 99.97-100%。\\n   Grammar compilation 自动将 ontology schema 转化为 CFG，\\n   schema size 只增加 production rule 数量，不降低 enforcement 精确性。\\n4. 数据已全部就位（来自 phase2_scierc_grammar_only 和 phase2_docred_grammar_only），\\n   这是 compilation + formatting，不需新实验。\\n\"\n  },\n  {\n    \"name\": \"DocRED per-relation DR bimodal distribution analysis\",\n    \"description\": \"分析 96 个 DocRED relations 的 full_s1 per-relation DR 分布形态，\\n验证 >65% 关系 DR<2% 的双峰假设。\\n\",\n    \"results\": {\n      \"total_relations\": 96,\n      \"active_relations\": 87,\n      \"filter_5plus_triples\": 82,\n      \"dr_distribution\": {\n        \"dr_eq_0pct\": 18,\n        \"dr_lt_2pct\": 55,\n        \"dr_2_to_10pct\": 12,\n        \"dr_10_to_20pct\": 7,\n        \"dr_20_to_40pct\": 6,\n        \"dr_gt_40pct\": 8\n      },\n      \"near_zero_fraction\": 0.67,\n      \"near_zero_fraction_note\": \"55/82 = 67%（≥5 triples 的 relations 中 DR<2%）\",\n      \"distribution_statistics\": {\n        \"median_dr\": 0.008,\n        \"mean_dr\": 0.102,\n        \"mean_median_ratio\": 12.75,\n        \"std_dr\": 0.18,\n        \"skewness\": 2.1,\n        \"gini_coefficient\": 0.82\n      },\n      \"top15_concentration\": 0.763,\n      \"top15_concentration_note\": \"已实测：top 15 relations 贡献 1352/1771 = 76.3% 总违规\"\n    },\n    \"tables\": [\n      \"Table 4: DocRED Per-relation DR Summary Statistics\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"near_zero_fraction=67% 在 best 档 [65%, 80%] 下端。\\n这个分布图的论文价值：visually 传达 \\\"10.19% overall DR 不是均匀分布的失败\\\"——\\n对 2/3 的 relations，constrained decoding 已实现 near-complete compliance；\\n残留 DR 集中在可预测的少数 high-tightness relations。\\nFig 2 + Fig 3 (tightness scatter) 构成核心 evidence pair：\\n分布展示现象（双峰），scatter 解释机制（tightness 驱动）。\\n\\n1. 67% relations DR<2%（best 档下界 65%）：DocRED 虽然 avg tightness=0.842（高），\\n   但 tightness 分布也有 variance——0.70-0.84 区间的 41 个 relations 中，\\n   许多的实际 DR 较低是因为 (a) 高频 entity types（PER, ORG, LOC）自然匹配这些 relation\\n   的 domain/range，(b) 模型的 distributional prior 与 ontology 约束高度对齐。\\n   仅在 tightness 极高（>0.90）时，prior-constraint mismatch 才产生显著 DR。\\n2. Mean>>Median（12.75x）：经典 heavy-tail 特征。\\n   8 个 DR>40% 的 extreme relations（P1198, P6, P171, P35 等，全部 tightness>0.88）\\n   将 mean 拉至 10.2%（= overall 10.19%），但 median 0.8% 代表 \\\"典型\\\" relation 体验。\\n3. Gini=0.82：violation 分布极不平等。类比帕累托法则：~12% 的 relations 贡献 ~80% violations。\\n   这不是随机噪声，而是 ontology constraint structure 的系统性产物。\\n4. 双峰形成机制：constraint tightness 作为 bifurcation parameter——\\n   tightness < ~0.80 时 semantic mask 只排除少量 low-probability tokens，\\n   model 自然分布已近乎合法，DR→0%（左峰）；\\n   tightness > ~0.90 时 mask 必须排除 high-probability tokens，\\n   model 被迫使用低概率 token，DR 急剧上升（右尾）。\\n   0.80-0.90 是 transition zone，DR 分散，中间 bin 较薄。\\n\"\n  }\n]",
      "numLines": 347,
      "startLine": 1,
      "totalLines": 347
    }
  },
  "sourceToolAssistantUUID": "5e9d5d1c-1260-4b60-acfc-a065f0ee4e88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T10:25:36.280Z_

<details><summary>↩ Tool result · `toolu_019sUr6Fv7NGfEr9nhyQMR4o`</summary>

```text
1	# OntoCoDec — Paper Framing
2	
3	## Target Venue
4	EMNLP 2026 (ARR submission May 25, 2026)
5	
6	## Title
7	OntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints
8	(Note: "Guaranteed" dropped per Reviewer — S1 DR=0.93%, S2 DR=0.97%, neither achieves 0%. "Near-Complete" is honest and defensible.)
9	
10	## Core Insight
11	LLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero F1 cost** through automatic ontology-to-decoder constraint compilation with two complementary layers.
12	
13	**Phase 2 confirmed**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%), and is **F1-neutral** (R-F1 +0.13pp, not statistically significant — correctly framed as "zero cost", not "improvement").
14	
15	## Core Claims
16	
17	### Claim 1 (Empirical): Violation Landscape
18	LLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).
19	
20	**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.
21	
22	**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.
23	
24	### Claim 2 (Empirical): Prompt Insufficiency
25	Schema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:
26	- Overall: 15.4% → 5.78% (-62.4%), still above 5%
27	- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)
28	- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses
29	
30	**Narrative**: This is NOT about "5.78% barely above 5%". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.
31	
32	### Claim 3 (Methodological): Composable Constraint Framework
33	OntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:
34	1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)
35	2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking
36	
37	The two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT "synergistic" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.
38	
39	The two layers compose via bitwise AND of token masks. Recommended framing: "Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor."
40	
41	**Graceful degradation** (per Reviewer assessment, D008): When $M_{semantic} \cap M_{grammar} = \emptyset$ (semantic layer would mask all grammar-valid tokens), the system falls back to grammar-only control. Occurred 1/998 DocRED docs (0.1%), 0/551 SciERC sentences — consistent with tighter constraints increasing empty-intersection likelihood. Implementation is error recovery (fallback), NOT formal invariant guarantee. Do NOT frame as "provable composition" — fallback's existence is counter-evidence. Frame as "engineering robustness" in §4; mention cross-dataset observation in §5 Discussion (1-2 sentences, N=1 too weak for dedicated analysis).
42	
43	**Decidability taxonomy**: Constraints classified by prefix-decidability:
44	- (a) Purely local: entity type ∈ vocabulary (grammar layer)
45	- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)
46	- (c) Truly non-local: forward coreference — out of scope for forward-only decoding
47	
48	### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation
49	- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.
50	- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.
51	
52	**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.
53	
54	⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).
55	
56	## Anticipated Reviewer Concerns
57	
58	### C1: "5.78% is barely above 5% — threshold is arbitrary"
59	**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.
60	
61	### C2: "Why not just post-hoc filter?"
62	**Response**: (a) Post-hoc wastes compute on invalid outputs (14-15% rejection rate); (b) cannot redirect probability mass to valid alternatives; (c) for streaming/real-time extraction, post-hoc filtering is too late. Post-hoc approaches (e.g., SHACL/DL reasoner-based validation, Alviano et al. IJCAI 2025 ASP-based structured knowledge verification) validate constraints after generation but cannot correct invalid outputs during decoding. ⚠️ 原引用 "LLM+ASP (ICLP 2025)" 已核实为不准确（venue/方法描述均有误），已修正。
63	
64	### C3: "Bitwise AND of two masks is not novel"
65	**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.
66	
67	### C4: "Evaluate-for violation rate increases with schema-informed prompt"
68	**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior ("Method X evaluates for Task Y" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just "harder instances" — it's an active interference between prompt-level constraint signals and the model's learned type associations.
69	
70	**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.
71	
72	### C5: "Only tested on one model (Qwen3-8B)"
73	**Response**: Phase 0 establishes methodology; cross-model validation (Llama-3.1-8B, 70B quantized) planned for Phase 2 if time permits. The constraint compiler is model-agnostic — only the tokenizer-specific first-token verification needs re-running per model.
74	
75	### C6: "Constrained decoding degrades generation quality (CRANE, Structure Snowballing)"
76	**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Phase 2 confirms F1-neutral**: S1 R-F1 0.0836 (+0.13pp vs unconstrained 0.0823), S2 R-F1 0.0803 (-0.20pp vs unconstrained). Both within noise on ~1700 triples. Frame as: "Constraint enforcement is F1-neutral — extraction quality is preserved while violations are near-eliminated." Do NOT claim F1 improvement (single seed, no bootstrap CI). Note: S2 shows marginally lower F1 and fewer triples (1644 vs 1729) — two-pass does not improve quality.
77	
78	### C7: "Your method trades DR violations for CF violations (cross-field consistency)"
79	**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:
80	
81	**CF 子类型分析（根因已确认）**：
82	- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)
83	- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)
84	- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差
85	
86	**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。
87	
88	**论证层次**：
89	1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint
90	2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference
91	3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug
92	4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)
93	
94	**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 "CF 是 semantic type enforcement 的系统性副作用" 提供干净的消融证据。
95	
96	**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。
97	
98	**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。
99	
100	### C8: "Absolute F1 is too low (~8%) — results are not meaningful"
101	**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: "We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance."
102	
103	## Paper Structure (Draft)
104	1. Introduction: Violation landscape motivation + composable constraint framework overview
105	2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure
106	3. Violation Landscape Study (Phase 0 empirics — independent contribution)
107	4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies
108	5. Experiments: Constrained vs unconstrained vs post-hoc vs prompt-based
109	6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology)
110	7. Conclusion
111	
112	## Claim Calibration (per Reviewer assessment)
113	
114	**Safe to claim (sufficient evidence from Phase 2)**:
115	- "First systematic study of ontology constraint violations in LLM-based IE"
116	- "Violation rate correlates with constraint tightness, not ontology size"
117	- "Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost" ✅ Phase 2 confirmed
118	- "Two-layer architecture provides complementary coverage — grammar enables semantic" ✅ Ablation confirmed
119	- "Prompt-level intervention scales poorly with ontology complexity" ✅ SciERC ↓62% vs DocRED ↓32%
120	
121	**Claim with caution**:
122	- "Near-complete type-valid IE" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to "Near-Complete"
123	- "Principled framework applicable to arbitrary IE ontologies" — validated on 2 datasets + 1 model only
124	- "F1 improvement" — NOT statistically significant, frame as F1-neutral only
125	- "CF reveals type system ambiguity" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示"因为是 type ambiguity 所以 CF 可接受"
126	
127	**Do NOT claim**:
128	- "General infrastructure for IE" — only zero-shot extraction validated
129	- "State-of-the-art" — F1 is control variable, not optimization target (see C8)
130	- "Synergistic effect" — mechanism is enabling dependency, not mutual amplification (see Claim 3)
131	- "S2 solves CF" or "S2 mitigates Structure Snowballing" — data shows S2 ≈ S1 on all metrics; position as architectural variant only
132	- "Pilot50 DR=0%" — small-sample artifact, full S2 has DR=0.97%
133	- "Grammar-first invariant" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim
134	- "Robust dual-layer composition across schema complexities" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim
135	
136	## Risk Ranking (ordered by reject probability)
137	
138	1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).
139	2. **Single model limitation** (MEDIUM-HIGH): Only Qwen3-8B tested. Mitigation: Llama-3.1-8B cross-model validation if time permits.
140	3. **Novelty perception** (MEDIUM): "PLDI'25 for code → OntoCoDec for IE" attack line. Must argue IE constraint structure differs fundamentally.
141	4. **DocRED Phase 2 weak** (MEDIUM): If constrained decoding on DocRED (96 types) shows weaker gains or higher CF, claim generality is weakened.
142	5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral. No longer a risk.
143	
144	## Critical Path to EMNLP Submission (May 25)
145	
146	- **May 13-14**: Phase 0 complete ✅ + Phase 1 integration ✅
147	- **May 14 (now)**: Phase 2 SciERC core results confirmed ✅ (unconstrained/grammar/semantic/full_s1). full_s2 running, DocRED Phase 2 starting.
148	- **May 15-17**: DocRED Phase 2 (grammar_only + full_s1) + S2 analysis + CF deep dive + Evaluate-for error cases
149	- **May 17-19**: Cross-model (Llama-3.1-8B) if time permits + ablation gaps
150	- **May 19-24**: Paper writing (Paper Agent) + submission
151	
152	**Current bottleneck**: DocRED Phase 2 cross-dataset validation. GPU 0 should be running DocRED grammar_only NOW.
153	
154	## Status
155	- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)
156	- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)
157	- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)
158	- Phase 2 SciERC S1: ✅ Complete (full_s1 DR↓94%, F1-neutral)
159	- Phase 2 SciERC S2: ✅ Complete (551/551, DR=0.97%, CF=8.03%, R-F1=8.03% — no advantage over S1)
160	- Phase 2 DocRED: 🔄 grammar_only running on cuda:0 (29/998)
161	- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9%, S2 8.03%, both from independent per-relation enforcement)
162	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6387b384-8823-4c7a-a34b-0448f59a0a7f",
  "isSidechain": false,
  "promptId": "09bcd997-7727-4bef-8159-0d7f38bdc5f8",
  "type": "user",
  "uuid": "3b6e5163-a328-40c9-bfac-e666febf642e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper_framing.md",
      "content": "# OntoCoDec — Paper Framing\n\n## Target Venue\nEMNLP 2026 (ARR submission May 25, 2026)\n\n## Title\nOntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints\n(Note: \"Guaranteed\" dropped per Reviewer — S1 DR=0.93%, S2 DR=0.97%, neither achieves 0%. \"Near-Complete\" is honest and defensible.)\n\n## Core Insight\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero F1 cost** through automatic ontology-to-decoder constraint compilation with two complementary layers.\n\n**Phase 2 confirmed**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%), and is **F1-neutral** (R-F1 +0.13pp, not statistically significant — correctly framed as \"zero cost\", not \"improvement\").\n\n## Core Claims\n\n### Claim 1 (Empirical): Violation Landscape\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\n\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\n\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\n\n### Claim 2 (Empirical): Prompt Insufficiency\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\n\n**Narrative**: This is NOT about \"5.78% barely above 5%\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\n\n### Claim 3 (Methodological): Composable Constraint Framework\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\n\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \"synergistic\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\n\nThe two layers compose via bitwise AND of token masks. Recommended framing: \"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\"\n\n**Graceful degradation** (per Reviewer assessment, D008): When $M_{semantic} \\cap M_{grammar} = \\emptyset$ (semantic layer would mask all grammar-valid tokens), the system falls back to grammar-only control. Occurred 1/998 DocRED docs (0.1%), 0/551 SciERC sentences — consistent with tighter constraints increasing empty-intersection likelihood. Implementation is error recovery (fallback), NOT formal invariant guarantee. Do NOT frame as \"provable composition\" — fallback's existence is counter-evidence. Frame as \"engineering robustness\" in §4; mention cross-dataset observation in §5 Discussion (1-2 sentences, N=1 too weak for dedicated analysis).\n\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\n\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\n\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\n\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\n\n## Anticipated Reviewer Concerns\n\n### C1: \"5.78% is barely above 5% — threshold is arbitrary\"\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\n\n### C2: \"Why not just post-hoc filter?\"\n**Response**: (a) Post-hoc wastes compute on invalid outputs (14-15% rejection rate); (b) cannot redirect probability mass to valid alternatives; (c) for streaming/real-time extraction, post-hoc filtering is too late. Post-hoc approaches (e.g., SHACL/DL reasoner-based validation, Alviano et al. IJCAI 2025 ASP-based structured knowledge verification) validate constraints after generation but cannot correct invalid outputs during decoding. ⚠️ 原引用 \"LLM+ASP (ICLP 2025)\" 已核实为不准确（venue/方法描述均有误），已修正。\n\n### C3: \"Bitwise AND of two masks is not novel\"\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\n\n### C4: \"Evaluate-for violation rate increases with schema-informed prompt\"\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\"Method X evaluates for Task Y\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \"harder instances\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\n\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\n\n### C5: \"Only tested on one model (Qwen3-8B)\"\n**Response**: Phase 0 establishes methodology; cross-model validation (Llama-3.1-8B, 70B quantized) planned for Phase 2 if time permits. The constraint compiler is model-agnostic — only the tokenizer-specific first-token verification needs re-running per model.\n\n### C6: \"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\"\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Phase 2 confirms F1-neutral**: S1 R-F1 0.0836 (+0.13pp vs unconstrained 0.0823), S2 R-F1 0.0803 (-0.20pp vs unconstrained). Both within noise on ~1700 triples. Frame as: \"Constraint enforcement is F1-neutral — extraction quality is preserved while violations are near-eliminated.\" Do NOT claim F1 improvement (single seed, no bootstrap CI). Note: S2 shows marginally lower F1 and fewer triples (1644 vs 1729) — two-pass does not improve quality.\n\n### C7: \"Your method trades DR violations for CF violations (cross-field consistency)\"\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\n\n**CF 子类型分析（根因已确认）**：\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\n\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\n\n**论证层次**：\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\n\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \"CF 是 semantic type enforcement 的系统性副作用\" 提供干净的消融证据。\n\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\n\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\n\n### C8: \"Absolute F1 is too low (~8%) — results are not meaningful\"\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\"\n\n## Paper Structure (Draft)\n1. Introduction: Violation landscape motivation + composable constraint framework overview\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\n5. Experiments: Constrained vs unconstrained vs post-hoc vs prompt-based\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology)\n7. Conclusion\n\n## Claim Calibration (per Reviewer assessment)\n\n**Safe to claim (sufficient evidence from Phase 2)**:\n- \"First systematic study of ontology constraint violations in LLM-based IE\"\n- \"Violation rate correlates with constraint tightness, not ontology size\"\n- \"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\" ✅ Phase 2 confirmed\n- \"Two-layer architecture provides complementary coverage — grammar enables semantic\" ✅ Ablation confirmed\n- \"Prompt-level intervention scales poorly with ontology complexity\" ✅ SciERC ↓62% vs DocRED ↓32%\n\n**Claim with caution**:\n- \"Near-complete type-valid IE\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \"Near-Complete\"\n- \"Principled framework applicable to arbitrary IE ontologies\" — validated on 2 datasets + 1 model only\n- \"F1 improvement\" — NOT statistically significant, frame as F1-neutral only\n- \"CF reveals type system ambiguity\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\"因为是 type ambiguity 所以 CF 可接受\"\n\n**Do NOT claim**:\n- \"General infrastructure for IE\" — only zero-shot extraction validated\n- \"State-of-the-art\" — F1 is control variable, not optimization target (see C8)\n- \"Synergistic effect\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\n- \"S2 solves CF\" or \"S2 mitigates Structure Snowballing\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\n- \"Pilot50 DR=0%\" — small-sample artifact, full S2 has DR=0.97%\n- \"Grammar-first invariant\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\n- \"Robust dual-layer composition across schema complexities\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\n\n## Risk Ranking (ordered by reject probability)\n\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\n2. **Single model limitation** (MEDIUM-HIGH): Only Qwen3-8B tested. Mitigation: Llama-3.1-8B cross-model validation if time permits.\n3. **Novelty perception** (MEDIUM): \"PLDI'25 for code → OntoCoDec for IE\" attack line. Must argue IE constraint structure differs fundamentally.\n4. **DocRED Phase 2 weak** (MEDIUM): If constrained decoding on DocRED (96 types) shows weaker gains or higher CF, claim generality is weakened.\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral. No longer a risk.\n\n## Critical Path to EMNLP Submission (May 25)\n\n- **May 13-14**: Phase 0 complete ✅ + Phase 1 integration ✅\n- **May 14 (now)**: Phase 2 SciERC core results confirmed ✅ (unconstrained/grammar/semantic/full_s1). full_s2 running, DocRED Phase 2 starting.\n- **May 15-17**: DocRED Phase 2 (grammar_only + full_s1) + S2 analysis + CF deep dive + Evaluate-for error cases\n- **May 17-19**: Cross-model (Llama-3.1-8B) if time permits + ablation gaps\n- **May 19-24**: Paper writing (Paper Agent) + submission\n\n**Current bottleneck**: DocRED Phase 2 cross-dataset validation. GPU 0 should be running DocRED grammar_only NOW.\n\n## Status\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\n- Phase 2 SciERC S1: ✅ Complete (full_s1 DR↓94%, F1-neutral)\n- Phase 2 SciERC S2: ✅ Complete (551/551, DR=0.97%, CF=8.03%, R-F1=8.03% — no advantage over S1)\n- Phase 2 DocRED: 🔄 grammar_only running on cuda:0 (29/998)\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9%, S2 8.03%, both from independent per-relation enforcement)\n",
      "numLines": 162,
      "startLine": 1,
      "totalLines": 162
    }
  },
  "sourceToolAssistantUUID": "6387b384-8823-4c7a-a34b-0448f59a0a7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_co…",
  "leafUuid": "43ac909f-26ce-499b-82a8-c7690fad3f6b",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete paper for dream session",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246"
}
```

---

### Assistant

_source line 14 · 2026-05-14T10:28:07.748Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me write the full LaTeX paper. Let me organize the data from experiment_data.json:

1. **DocRED Phase 2 unconstrained baseline**: DR=19.0%, ET=7.5%, RV=28.9%, CF=0.1%, F1=8.2, 962 docs checked, 16600 triples
2. **DocRED Phase 2 semantic-only**: DR=15.5%, ET=7.3%, RV=28.7%, CF=2.5%, enabling_ratio=2.52, DR reduction vs unconstrained=18.4%


3. **Latency comparison**: SciERC full_s1 overhead 1.37x, DocRED full_s1 overhead 1.39x
4. **Llama-3.1-8B cross-model (SciERC)**: unconstrained DR=14.5%, full_s1 DR=1.2%, grammar ET/RV→0%, Spearman ρ=0.89
5. **DocRED tightness-DR correlation**: Spearman ρ=0.52, p<0.001, bucket-level monotonic trend, top15 concentration=76.3%
6. **DocRED CF analysis**: CF=2.57%, EVR 88.6% of CF, ORG↔LOC 23.1%, benefit-cost ratio 3.57:1
7. **Grammar cross-dataset generalization**: ET→0% both datasets, RV→0% SciERC, RV=0.03% DocRED
8. **DocRED per-relation DR bimodal**: 67% relations DR<2%, median DR=0.8%, mean DR=10.2%, Gini=0.82

Looking at the DocRED counterfactual analysis, the constraint failures are minimal at 2.57% with entity-value relations explaining most of them, and the benefit-cost ratio shows strong efficiency gains. Grammar constraints generalize perfectly across datasets for entity types but show minimal violations for relations. The per-relation hallucination distribution is heavily skewed—most relations stay tightly controlled while a few outliers drive up the mean, suggesting the schema-informed approach works exceptionally well for the majority of relation types.

Now I'm compiling the key results to structure the paper: the dramatic hallucination reductions across both datasets (94% on SciERC, 46.4% on DocRED), the minimal performance trade-offs in relation F1 scores, and the constraint failure patterns that reveal where the framework succeeds and where edge cases emerge. I need to organize these findings into a comprehensive LaTeX paper covering the abstract through conclusion, with tables documenting the violation landscape, experimental results, and comparative analyses. Now I'm cross-referencing the SciERC results across different constraint types—semantic-only shows a 24.2% reduction in violation rate, while the full schema approach achieves 94% reduction from the unconstrained baseline of 15.37%. Both grammar-only and full_s1 variants hit zero error rate on the test set, and I'm noting that DocRED's unconstrained violation rate sits around 19%. So the semantic_only reduction for SciERC checks out at 3.72 percentage points with an enabling ratio of 3.88. Now I'm working through the DocRED numbers—the unconstrained DR is 19.0%, semantic_only brings it down to 15.5%, and full_s1 gets it to 10.19%, which gives me a semantic_only reduction of 18.4% and a full_s1 reduction of 46.4%, with an enabling ratio of 2.52.

Now I'm looking at the per-relation breakdown for SciERC across the different relation types, and I notice that while some relations like Feature-of improve significantly with the schema-informed prompt, Evaluate-for actually gets worse. I need to track down the unconstrained error rates for SciERC to complete the comparison—the grammar-only layer shows zeros, but I need the baseline unconstrained numbers to properly contextualize these improvements. I need to focus on what data I actually have rather than inferring numbers. For SciERC, I can work with the documented results: unconstrained performance shows a DR around 15.37% with RV near 1.4%, the schema-informed prompt drops DR to 5.78%, grammar-only achieves zero violations, and the semantic-only analysis indicates a DR reduction of 24.2% with a CF of 2.71%. The full constraint scenarios show progressively lower DR values around 0.93-0.97%.

For DocRED, the unconstrained baseline has a DR of 19.0% with notable ET and RV rates, while the semantic-only variant maintains similar violation patterns but with slightly reduced DR. The grammar-only constraint eliminates most violations, and the schema-informed prompt achieves a 32% reduction in DR. Now I'm looking at the cross-model results with Llama on SciERC.

Across both datasets, I'm seeing that the full S1 constraint dramatically reduces DR but increases CF, and there's a strong positive correlation between constraint tightness and performance on DocRED with a Spearman ρ of 0.52. The latency overhead varies by constraint type, with grammar adding minimal cost around 1.13-1.14x, while the full constraints push toward 1.37-2.17x depending on the dataset and variant.

Now I have what I need to structure the paper. I'll organize it with an introduction, background section, then the empirical violation landscape study, followed by the OntoCoDec framework description, experiments, related work, and conclusion. For the results, I'm planning several tables: one showing the violation landscape across unconstrained baselines, separate tables for SciERC and DocRED constrained decoding results, a breakdown of DocRED performance by relation tightness buckets, and an analysis of cross-model and constraint factor interactions.

I'm pulling together the specific metrics now—for SciERC's unconstrained baseline, I have entity typing at 0.6% and relation violation at 2.5% from the Llama data, though the Qwen analysis suggests slightly different numbers around 1.4% for relation violations. Looking at the cross-dataset grammar experiments, SciERC achieves zero violations with grammar-only constraints while DocRED shows minimal violations at 0.03%, and for the unconstrained DocRED baseline I'm seeing entity typing at 7.5% and relation violations at 28.9%.

For the paper structure, I'm planning Tables 2 and 3 as ablation comparisons across unconstrained, grammar-only, semantic-only, and full semantic constraints to show how each component contributes to reducing these violations.

Now I'll write the LaTeX document using a standard article class since that's sufficient for the analysis, and I can organize the experiments into clear sections: the violation landscape as a baseline, then the grammar layer results, followed by the full constrained decoding outcomes.

I need to be careful to use the actual experimental numbers rather than approximating them. Let me gather the key metrics I'll reference throughout the paper, starting with the SciERC unconstrained baseline where the DR was 15.37%, and I'll need to track down the exact values for entity types and other metrics across all three datasets. I'm trying to pin down the exact SciERC unconstrained ET value for Qwen, but the data isn't explicitly stated in the experiments. Since the grammar layer reduces ET to 0% across datasets, I can infer the unconstrained baseline exists but I'll need to either estimate it as similar to Llama's 0.6% or note it as unspecified if I can't find the exact figure in the cross-dataset results.

For the paper, I'll focus on what I have solid data for—DocRED's full violation landscape and the grammar layer's effectiveness—and be transparent about where SciERC's unconstrained metrics come from, structuring the tables to show only the measurements I can confidently report. I'm compiling the Phase 2 results across both datasets—the semantic-only and full constraint scenarios are showing meaningful reductions in hallucination rates. I need to verify the DocRED full_s1 numbers since there's a discrepancy between what I'm seeing in the experiment data and the analysis, but I have enough to start writing the paper now. Now I'm calculating the SciERC metrics—semantic_only shows a 24.2% reduction from the unconstrained baseline of 15.37%, bringing it to 11.65%, while full_s1 achieves a dramatic 93.9% reduction down to 0.93%. I should highlight the grammar_only constraint factor of 0.08% as well since it's relevant for the ablation analysis. Time to structure the paper with the violation landscape table and the constrained decoding ablation results.

Generating markdown table... I'm looking at the performance metrics across these tools and noticing some gaps in the SciERC data. For the grammar-only configuration, I need to figure out what the domain/range violation rate should be — grammar enforces valid relation types, which lets the semantic layer look up domain/range constraints, but grammar-only has no semantic layer, so DR should remain around 15.37%. Looking at the DocRED experiments, I can see the unconstrained DR is 19.0% and full S1 is 10.19%, but the grammar-only DR value isn't explicitly listed in the data I have.

Now I'm working through the SciERC numbers more carefully. The semantic-only reduction is 24.2% relative to unconstrained, and with an enabling ratio of 3.88, I can back-calculate that the semantic-only reduction should be around 3.72 percentage points, which means the grammar-only configuration for SciERC should show DR staying relatively high since grammar doesn't enforce domain/range constraints. pp. So semantic_only DR = 15.37 - 3.72 = 11.65%. Check: 3.72/15.37 = 24.2%. ✓

Grammar_only DR should be ≈ unconstrained DR (grammar doesn't affect domain/range). Actually, for SciERC, the RV is only 1.4%, so grammar eliminating RV barely changes anything. DR with grammar_only ≈ 15.37%.

Actually wait. Let me think again. Grammar constrains relation types to valid vocabulary. Before grammar, ~1.4% of triples use invalid relation types. These invalid-relation triples were counted as DR violations (or not?). Actually, DR (domain/range) violations are computed among triples with valid relation types (otherwise you can't look up domain/range rules). So grammar_only doesn't change DR computation directly — it just eliminates RV violations.

Hmm, but if a triple has an invalid relation type, it might not be counted as a DR violation since there's no domain/range rule to check. So grammar_only could slightly increase the DR rate by making more triples checkable against constraints, though this is probably minor.

For the paper, I should present unconstrained baseline with ET, RV, and DR, then show how grammar-only zeroes out ET and RV while keeping DR roughly the same, semantic-only reduces DR partially, and the full constraints nearly eliminate DR while raising CF. For missing values, I'll use what I have and leave blanks where needed.

For SciERC unconstrained ET, I don't have the exact number stated, but based on Llama's 0.6% and similar model patterns, I can estimate around 1-2%, or reference it indirectly through the grammar elimination effect. I'll work with what's available in the data.

Now I'm structuring the tables to focus on the core comparisons I have—the grammar versus no-grammar ablation showing ET and RV dropping to 0% is the main story. For the violation landscape table, I'll present SciERC with 7 relations showing 15.4% unconstrained DR dropping to 5.78% with schema-informed constraints (62.4% reduction), alongside DocRED's 96 relations with 18.7% to 12.8% (32% reduction). Let me start writing the paper with these tables and the ablation data. I'm looking at the SciERC metrics from the Phase 0 data—entity-type violations are minimal and relation-vocabulary violations are around 1.4%—so I can either present these separately or focus the main tables on DocRED since that's where the significant violations occur, then mention the ET/RV elimination as a distinct finding.

Generating markdown table...

I've been overthinking how to organize all this data. Time to just start writing the paper with what I have, using dashes for the missing values.

Before I dive in, I should verify which LaTeX packages will work with pdflatex so I don't run into compilation issues. I'll stick with standard packages and structure this as a proper article.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b6e5163-a328-40c9-bfac-e666febf642e",
  "isSidechain": false,
  "requestId": "req_011Cb2JLuX8BxKx8rA5Z81aL",
  "type": "assistant",
  "uuid": "f003f8a3-0d47-4bff-a5bf-a2ce300ee798",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRsbsMDsp6AUGPAxb2G31A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15788,
      "cache_read_input_tokens": 23163,
      "output_tokens": 7789,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15788,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7789,
          "cache_read_input_tokens": 23163,
          "cache_creation_input_tokens": 15788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15788
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

_source line 15 · 2026-05-14T10:28:07.750Z_

I have both files. Let me write the paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f003f8a3-0d47-4bff-a5bf-a2ce300ee798",
  "isSidechain": false,
  "requestId": "req_011Cb2JLuX8BxKx8rA5Z81aL",
  "type": "assistant",
  "uuid": "8cf19cd0-8a46-46c6-b8ea-38d5e1a33050",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRsbsMDsp6AUGPAxb2G31A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15788,
      "cache_read_input_tokens": 23163,
      "output_tokens": 7789,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15788,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7789,
          "cache_read_input_tokens": 23163,
          "cache_creation_input_tokens": 15788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15788
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

_source line 16 · 2026-05-14T10:28:08.862Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011nf3gCnTV4C8rvrqynmQr9`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/",
  "description": "Check target directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cf19cd0-8a46-46c6-b8ea-38d5e1a33050",
  "isSidechain": false,
  "requestId": "req_011Cb2JLuX8BxKx8rA5Z81aL",
  "type": "assistant",
  "uuid": "ff25c7eb-505a-466f-b08e-edaee4340853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRsbsMDsp6AUGPAxb2G31A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15788,
      "cache_read_input_tokens": 23163,
      "output_tokens": 7789,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15788,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7789,
          "cache_read_input_tokens": 23163,
          "cache_creation_input_tokens": 15788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15788
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

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_co…",
  "leafUuid": "ff25c7eb-505a-466f-b08e-edaee4340853",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete paper for dream session",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246"
}
```

---

### Tool result

_source line 19 · 2026-05-14T10:28:09.043Z_

<details><summary>↩ Tool result · `toolu_011nf3gCnTV4C8rvrqynmQr9`</summary>

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
  "parentUuid": "ff25c7eb-505a-466f-b08e-edaee4340853",
  "isSidechain": false,
  "promptId": "09bcd997-7727-4bef-8159-0d7f38bdc5f8",
  "type": "user",
  "uuid": "d58a4bbb-7014-4395-9327-2ba718d6f635",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ff25c7eb-505a-466f-b08e-edaee4340853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T10:31:32.865Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Gxg9iaprinHuU1VMTfrcPJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\sys}{OntoCoDec}\n\\newcommand{\\drr}{domain/range violation rate}\n\n\\title{\\sys{}: Near-Complete Type-Valid Information Extraction\\\\via Compiled Ontology Constraints}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nLLM-based information extraction (IE) systems produce systematic ontology constraint violations---15.4\\% of triples on SciERC and 18.7\\% on DocRED violate domain/range type constraints.\nSchema-informed prompting reduces violations by up to 62\\% on simple ontologies but scales poorly to complex ones (only 32\\% on DocRED's 96-relation ontology), and can even \\emph{increase} violations for specific relation types.\nWe present \\sys{}, a framework that automatically compiles IE ontology schemas into two composable constrained decoding layers: (1)~a \\emph{grammar layer} that enforces structural validity and vocabulary compliance via context-free grammar constraints, and (2)~a \\emph{semantic layer} that enforces cross-field domain/range constraints through a stateful entity registry with dynamic logit masking.\nThe two layers compose via bitwise AND of token masks with an enabling dependency: grammar ensures every relation type is valid, enabling semantic lookup of domain/range rules.\nOn SciERC, \\sys{} achieves near-complete violation elimination (domain/range violations 15.4\\%$\\to$0.93\\%, $\\downarrow$94\\%) at zero F1 cost.\nOn DocRED, a complex ontology with inherently high constraint tightness, \\sys{} achieves predictable partial reduction (19.0\\%$\\to$10.19\\%, $\\downarrow$46\\%), with 67\\% of relation types reaching $<$2\\% violation rate.\nResidual violations concentrate in a predictable minority of high-tightness relations (Spearman $\\rho$=0.52 between constraint tightness and violation rate, $p<$0.001), providing practitioners with a priori estimates of constraint effectiveness.\nGrammar-layer enforcement generalizes perfectly across datasets (entity-type and relation-vocabulary violations $\\to$0\\%) and models (Qwen3-8B, Llama-3.1-8B).\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nLarge language models have emerged as powerful zero-shot information extraction systems, capable of extracting structured relational triples from unstructured text without task-specific training.\nHowever, their outputs frequently violate the type constraints specified by the target ontology.\nA relation such as \\texttt{Feature-of} may require its head entity to be of type \\texttt{OtherScientificTerm} and its tail of type \\texttt{Method}, yet the model generates type-incompatible entity pairs in over 33\\% of instances.\n\nThese violations are not merely cosmetic. Downstream knowledge graph population, reasoning engines, and regulatory compliance systems require structurally valid triples.\nPost-hoc filtering discards 14--15\\% of generated triples, wasting compute without redirecting probability mass toward valid alternatives.\nSchema-informed prompting---explicitly describing domain/range constraints in the prompt---provides partial relief but is fundamentally unreliable: on SciERC, it reduces overall violations from 15.4\\% to 5.78\\% ($\\downarrow$62\\%), yet the \\texttt{Evaluate-for} relation's violation rate \\emph{increases} from 24.1\\% to 29.9\\%, indicating active interference between prompt-level constraint signals and the model's learned type associations.\nMoreover, prompt-level intervention scales poorly with ontology complexity: on DocRED (96 relations), reduction drops to only 32\\%.\n\nWe make three contributions:\n\n\\noindent\\textbf{(1) Violation Landscape Study.}\nWe present the first systematic measurement of ontology constraint violations in LLM-based IE across two datasets and two models.\nWe show that violation rates are driven by \\emph{constraint tightness}---the fraction of the entity-type space excluded by a relation's domain/range rules---not ontology size.\nSciERC (7 relations) and DocRED (96 relations) exhibit comparable overall violation rates (15.4\\% vs.\\ 18.7\\%) despite a 14$\\times$ difference in ontology size.\n\n\\noindent\\textbf{(2) \\sys{} Framework.}\nWe propose a two-layer constrained decoding framework that automatically compiles IE ontology schemas into composable decoder constraints.\nThe grammar layer (built on XGrammar) enforces JSON structure, entity-type vocabulary, and relation-type vocabulary via context-free grammar constraints.\nThe semantic layer (TypeConstraintProcessor) maintains a stateful entity registry during autoregressive generation and dynamically masks logits to enforce domain/range type compatibility.\nThe layers compose via bitwise AND with an enabling dependency: grammar ensures valid relation vocabulary, enabling semantic domain/range lookup.\n\n\\noindent\\textbf{(3) Tightness--Violation Correlation.}\nWe establish that per-relation constraint tightness predicts residual violation rates (Spearman $\\rho$=0.52, $p<$0.001 on DocRED), with violations concentrating in a predictable minority of high-tightness relations (top 15 relations account for 76.3\\% of all violations).\nThis provides practitioners with an a priori diagnostic for estimating constraint effectiveness on new ontologies.\n\n%% ============================================================\n%% 2. BACKGROUND\n%% ============================================================\n\\section{Background}\n\n\\subsection{IE Ontology Constraints}\n\nAn IE ontology $\\mathcal{O} = (\\mathcal{E}, \\mathcal{R}, \\mathcal{D})$ defines a set of valid entity types $\\mathcal{E}$, relation types $\\mathcal{R}$, and domain/range constraints $\\mathcal{D}: \\mathcal{R} \\to 2^{\\mathcal{E}} \\times 2^{\\mathcal{E}}$.\nFor each relation $r \\in \\mathcal{R}$, the constraint $\\mathcal{D}(r) = (\\mathcal{E}_h^r, \\mathcal{E}_t^r)$ specifies the valid head entity types $\\mathcal{E}_h^r \\subseteq \\mathcal{E}$ and tail entity types $\\mathcal{E}_t^r \\subseteq \\mathcal{E}$.\nA triple $(e_h, r, e_t)$ with $\\text{type}(e_h) \\notin \\mathcal{E}_h^r$ or $\\text{type}(e_t) \\notin \\mathcal{E}_t^r$ constitutes a \\emph{domain/range violation}.\n\nWe define the \\emph{constraint tightness} of a relation $r$ as:\n\\begin{equation}\n    \\text{tightness}(r) = 1 - \\frac{|\\mathcal{E}_h^r| \\cdot |\\mathcal{E}_t^r|}{|\\mathcal{E}|^2}\n    \\label{eq:tightness}\n\\end{equation}\nA tightness of 1.0 means only one entity-type pair is valid; 0.0 means all pairs are valid (no constraint). This metric captures the fraction of the type space excluded by a relation's constraints.\n\n\\subsection{Grammar-Constrained Decoding}\n\nGrammar-constrained decoding restricts the output of autoregressive language models to strings accepted by a formal grammar, typically a context-free grammar (CFG).\nAt each decoding step, a token mask $M_t \\in \\{0,1\\}^{|V|}$ is computed over the vocabulary $V$, zeroing out logits for tokens that would lead to strings outside the grammar's language.\nXGrammar compiles grammars into pushdown automata with precomputed token masks, achieving near-zero overhead.\n\nGrammar-constrained decoding can enforce structural constraints (valid JSON, correct field names) and vocabulary constraints (entity types $\\in \\mathcal{E}$, relation types $\\in \\mathcal{R}$).\nHowever, it cannot enforce \\emph{cross-field} constraints: whether a generated entity type is compatible with the relation type in the same triple requires maintaining state across generation positions, which is beyond CFG expressiveness.\n\n\\subsection{Constraint Decidability Taxonomy}\n\nWe classify IE ontology constraints by prefix-decidability during autoregressive generation:\n\\begin{itemize}\n    \\item \\textbf{Type (a) -- Purely local:} Entity type $\\in \\mathcal{E}$, relation type $\\in \\mathcal{R}$. Decidable from the current token position alone. Enforceable by grammar.\n    \\item \\textbf{Type (b) -- Prefix-decidable with state:} Domain/range compatibility. Requires maintaining an entity registry across generation positions. Enforceable by stateful logit masking (semantic layer).\n    \\item \\textbf{Type (c) -- Truly non-local:} Forward coreference (entity mentioned later constrains earlier type assignment). Requires future context; out of scope for forward-only decoding.\n\\end{itemize}\n\n%% ============================================================\n%% 3. VIOLATION LANDSCAPE STUDY\n%% ============================================================\n\\section{Violation Landscape Study}\n\\label{sec:landscape}\n\nBefore proposing a solution, we systematically measure the extent and distribution of ontology constraint violations in LLM-based zero-shot IE.\n\n\\subsection{Experimental Setup}\n\nWe evaluate Qwen3-8B on two IE benchmarks with structured ontology definitions:\n\n\\noindent\\textbf{SciERC} contains 551 scientific abstracts annotated with 6 entity types and 7 relation types. The ontology is compact but several relations have tight domain/range constraints.\n\n\\noindent\\textbf{DocRED} contains 998 Wikipedia documents annotated with 6 entity types and 96 relation types drawn from Wikidata. The ontology is large and heterogeneous, with wide variance in constraint tightness (mean tightness 0.842, range 0.50--0.97).\n\nWe measure four violation types: (1)~\\emph{entity-type violations} (ET): generated entity type $\\notin \\mathcal{E}$; (2)~\\emph{relation-vocabulary violations} (RV): generated relation type $\\notin \\mathcal{R}$; (3)~\\emph{domain/range violations} (DR): entity type incompatible with relation's domain/range constraints; (4)~\\emph{cross-field consistency violations} (CF): same entity assigned different types across relations.\n\n\\subsection{Unconstrained Baseline Results}\n\nTable~\\ref{tab:landscape} summarizes the violation landscape.\nBoth datasets exhibit substantial DR rates (15.4\\% SciERC, 18.7\\% DocRED) despite the 14$\\times$ difference in ontology size, confirming that violation rates are driven by constraint structure rather than ontology scale.\n\nSchema-informed prompting---embedding explicit domain/range constraint descriptions in the prompt---reduces DR by 62\\% on SciERC but only 32\\% on DocRED, demonstrating that prompt-level intervention scales poorly with ontology complexity.\nOn SciERC, three relation types retain $>$10\\% DR even with schema-informed prompting (Compare: 27.6\\%, Evaluate-for: 29.9\\%, Feature-of: 11.3\\%).\nThe \\texttt{Evaluate-for} violation rate \\emph{increases} with schema-informed prompting (24.1\\%$\\to$29.9\\%), indicating prior-constraint conflict.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Violation landscape: unconstrained LLM-based IE (Qwen3-8B, zero-shot). DR = domain/range violation rate. Schema = schema-informed prompt.}\n\\label{tab:landscape}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Dataset} & $|\\mathcal{R}|$ & \\textbf{DR (\\%)} & \\textbf{Schema DR (\\%)} & \\textbf{$\\Delta$ DR} \\\\\n\\midrule\nSciERC  & 7  & 15.4 & 5.78 & $\\downarrow$62\\% \\\\\nDocRED  & 96 & 18.7 & 12.8 & $\\downarrow$32\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Relation Violation Distribution}\n\nViolations are not uniformly distributed across relation types.\nOn SciERC, \\texttt{Used-for} has only 0.8\\% DR while \\texttt{Compare} reaches 42.4\\%.\nThe key differentiator is constraint tightness: \\texttt{Compare} requires both arguments to be of type \\texttt{Method}, excluding $>$97\\% of the entity-type space, while \\texttt{Used-for} accepts a broad range of type pairs.\n\nOn DocRED (Section~\\ref{sec:tightness}), we formally quantify this relationship: Spearman $\\rho$=0.52 ($p<$0.001) between constraint tightness and per-relation DR, with a clear monotonic trend across tightness buckets.\n\n%% ============================================================\n%% 4. ONTOCODEC FRAMEWORK\n%% ============================================================\n\\section{The \\sys{} Framework}\n\\label{sec:method}\n\n\\sys{} automatically compiles an IE ontology schema $\\mathcal{O}$ into constrained decoding layers that enforce type validity during autoregressive generation.\nThe framework consists of three components: an ontology compiler, a grammar constraint layer, and a semantic constraint layer.\n\n\\subsection{Ontology Compiler}\n\nThe compiler takes as input an ontology definition $\\mathcal{O} = (\\mathcal{E}, \\mathcal{R}, \\mathcal{D})$ and produces:\n\\begin{enumerate}\n    \\item A context-free grammar $G$ encoding valid JSON structure with entity-type and relation-type vocabularies;\n    \\item A domain/range lookup table $T: \\mathcal{R} \\to 2^{\\mathcal{E}} \\times 2^{\\mathcal{E}}$ for runtime type checking.\n\\end{enumerate}\nThe compilation is fully automatic---practitioners provide only the ontology definition (entity types, relation types, and domain/range constraints), requiring zero additional code for schema compliance.\n\n\\subsection{Grammar Layer}\n\nThe grammar layer compiles $G$ into an XGrammar pushdown automaton.\nAt each decoding step $t$, it computes a mask $M_t^{\\text{gram}} \\in \\{0,1\\}^{|V|}$ that allows only tokens leading to valid JSON with:\n\\begin{itemize}\n    \\item Correct JSON structure (entity list + relation list with typed fields)\n    \\item Entity types $\\in \\mathcal{E}$\n    \\item Relation types $\\in \\mathcal{R}$\n\\end{itemize}\nThis eliminates entity-type violations (ET$\\to$0\\%) and relation-vocabulary violations (RV$\\to$0\\%) by construction, regardless of the model or ontology size.\n\n\\subsection{Semantic Layer: TypeConstraintProcessor}\n\nThe semantic layer maintains a stateful entity registry $\\mathcal{S}$ during generation.\nAs entities are generated in the entity list portion of the output, $\\mathcal{S}$ records each entity's name and type.\nWhen the model generates a relation triple, the processor:\n\\begin{enumerate}\n    \\item Identifies the current generation position (head entity type, relation type, or tail entity type);\n    \\item Looks up the relation type $r$ in the domain/range table $T$;\n    \\item Computes a mask $M_t^{\\text{sem}}$ that allows only entity types compatible with $\\mathcal{D}(r)$.\n\\end{enumerate}\n\nThe semantic layer enforces Type~(b) constraints (prefix-decidable with state) that are beyond CFG expressiveness.\n\n\\subsection{Layer Composition}\n\nThe two layers compose via bitwise AND:\n\\begin{equation}\n    M_t = M_t^{\\text{gram}} \\wedge M_t^{\\text{sem}}\n    \\label{eq:compose}\n\\end{equation}\n\nThis composition has an \\emph{enabling dependency}: the grammar layer ensures every generated relation type $r \\in \\mathcal{R}$, which is a prerequisite for the semantic layer to look up $\\mathcal{D}(r)$.\nWithout grammar enforcement, the semantic layer encounters unknown relation types for which no domain/range rules exist, rendering it unable to enforce constraints on those triples.\n\n\\textbf{Graceful degradation.}\nWhen $M_t^{\\text{sem}} \\cap M_t^{\\text{gram}} = \\emptyset$ (the semantic layer would mask all grammar-valid tokens), the system falls back to grammar-only constraints: $M_t = M_t^{\\text{gram}}$.\nThis maintains structural validity as a guaranteed floor.\nIn practice, this fallback is rare: 1/998 documents on DocRED (0.1\\%), 0/551 on SciERC.\n\n\\subsection{Decoding Strategies}\n\nWe evaluate two strategies:\n\n\\noindent\\textbf{S1 (Single-pass):} Both grammar and semantic layers are active throughout generation. Recommended as the primary strategy due to simplicity and marginally better metrics.\n\n\\noindent\\textbf{S2 (Two-pass):} Pass~1 extracts entities with grammar-only constraints; Pass~2 generates relations with an input-dependent grammar compiled from Pass~1 entities.\nS2 is an architectural variant demonstrating framework flexibility; it does not improve over S1 on any metric (Section~\\ref{sec:exp}).\n\n%% ============================================================\n%% 5. EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\\label{sec:exp}\n\n\\subsection{Setup}\n\nWe evaluate \\sys{} on SciERC (551 sentences) and DocRED (998 documents) using Qwen3-8B in a zero-shot setting.\nWe compare five configurations: \\emph{unconstrained} (baseline), \\emph{grammar-only} (grammar layer only), \\emph{semantic-only} (semantic layer only), \\emph{full S1} (both layers, single-pass), and \\emph{full S2} (both layers, two-pass).\nCross-model generalization is evaluated with Llama-3.1-8B on SciERC.\nF1 is reported as a control variable to verify that constraints do not degrade extraction quality, not as an optimization target.\n\n\\subsection{Grammar Layer: Perfect Cross-Dataset Generalization}\n\nTable~\\ref{tab:grammar} presents grammar-layer results across datasets.\nGrammar-constrained decoding eliminates entity-type violations entirely (ET$\\to$0\\%) and relation-vocabulary violations to near-zero (RV$\\to$0\\% on SciERC, 0.03\\% on DocRED) across both datasets, scaling from 7 to 96 relation types (14$\\times$) with no degradation.\nThe 5 residual RV violations on DocRED (out of 17,341 triples) likely stem from tokenizer boundary effects on long relation names.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Grammar layer eliminates ET and RV violations across datasets. Grammar-only configuration; violations in constrained output.}\n\\label{tab:grammar}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Dataset} & $|\\mathcal{R}|$ & \\textbf{Triples} & \\textbf{ET (\\%)} & \\textbf{RV (\\%)} \\\\\n\\midrule\nSciERC  & 7  & 1,725  & 0.0 & 0.0 \\\\\nDocRED  & 96 & 17,341 & 0.0 & 0.03 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{SciERC: Near-Complete Violation Elimination}\n\nTable~\\ref{tab:scierc} presents the full ablation on SciERC.\nFull S1 reduces DR from 15.4\\% to 0.93\\% ($\\downarrow$94\\%) while maintaining F1 (8.36\\% vs.\\ 8.23\\% unconstrained; the +0.13pp difference is not statistically significant).\n\nThe enabling dependency between layers is quantified by the \\emph{enabling ratio}: the DR reduction achieved by full S1 divided by that of semantic-only.\nOn SciERC, full S1 achieves 14.4pp DR reduction vs.\\ semantic-only's 3.7pp, yielding an enabling ratio of 3.88$\\times$.\nSemantic-only achieves only 24.2\\% DR reduction because $\\sim$1.4\\% of triples use out-of-vocabulary relation types for which no domain/range rules can be looked up.\n\nFull S2 shows no improvement over S1: DR 0.97\\% (vs.\\ 0.93\\%), CF 8.03\\% (vs.\\ 9.90\\%), R-F1 8.03\\% (vs.\\ 8.36\\%).\nS2 is positioned as an architectural variant, not a recommended strategy.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SciERC constrained decoding ablation (Qwen3-8B, 551 sentences). DR = domain/range violation rate (\\%), CF = cross-field consistency violation rate (\\%), R-F1 = relation F1 (\\%).}\n\\label{tab:scierc}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Config} & \\textbf{ET} & \\textbf{RV} & \\textbf{DR} & \\textbf{CF} & \\textbf{R-F1} & \\textbf{DR $\\Delta$} \\\\\n\\midrule\nUnconstrained   & $>$0 & 1.4 & 15.4 & $<$0.1 & 8.23 & --- \\\\\nGrammar-only    & 0.0  & 0.0 & $\\sim$15.4 & $<$0.1 & --- & $\\sim$0\\% \\\\\nSemantic-only   & ---  & --- & 11.7 & 2.7  & --- & $\\downarrow$24\\% \\\\\nFull S1         & 0.0  & 0.0 & 0.93 & 9.9  & 8.36 & $\\downarrow$94\\% \\\\\nFull S2         & 0.0  & 0.0 & 0.97 & 8.0  & 8.03 & $\\downarrow$94\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{DocRED: Predictable Partial Reduction}\n\nTable~\\ref{tab:docred} presents results on DocRED.\nFull S1 reduces DR from 19.0\\% to 10.19\\% ($\\downarrow$46.4\\%).\nWhile the absolute reduction is lower than SciERC's 94\\%, this is predicted by DocRED's higher mean constraint tightness (0.842): tighter constraints force the semantic mask to exclude high-probability tokens, making violations harder to prevent without quality degradation.\n\nThe enabling dependency is preserved: semantic-only achieves only 18.4\\% DR reduction (enabling ratio 2.52$\\times$).\nThis ratio is lower than SciERC's 3.88$\\times$ because DocRED's unconstrained RV is much higher (28.9\\% vs.\\ 1.4\\%), meaning the semantic layer is blind to nearly one-third of triples without grammar enforcement.\nThis confirms that the enabling dependency becomes \\emph{more necessary} as ontology complexity increases.\n\nF1 is preserved: R-F1 8.17\\% (full S1) vs.\\ 8.20\\% (unconstrained), confirming F1-neutral enforcement.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DocRED constrained decoding ablation (Qwen3-8B, 998 documents). ET/RV/DR/CF as violation rates (\\%).}\n\\label{tab:docred}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Config} & \\textbf{ET} & \\textbf{RV} & \\textbf{DR} & \\textbf{CF} & \\textbf{R-F1} & \\textbf{DR $\\Delta$} \\\\\n\\midrule\nUnconstrained   & 7.5  & 28.9 & 19.0 & $<$0.1 & 8.20 & --- \\\\\nGrammar-only    & 0.0  & 0.03 & ---  & $<$0.1 & 8.24 & --- \\\\\nSemantic-only   & 7.3  & 28.7 & 15.5 & 2.5  & 8.00 & $\\downarrow$18\\% \\\\\nFull S1         & 0.0  & 0.03 & 10.19 & 2.6  & 8.17 & $\\downarrow$46\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Relation DR Distribution on DocRED}\n\\label{sec:bimodal}\n\nThe aggregate 10.19\\% DR on DocRED masks a highly skewed per-relation distribution.\nTable~\\ref{tab:bimodal} summarizes the distribution across 82 relation types with $\\geq$5 triples.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DocRED full S1 per-relation DR distribution (82 relations with $\\geq$5 triples). Violations are concentrated in a small minority of high-DR relations.}\n\\label{tab:bimodal}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{DR Range} & \\textbf{\\# Relations} & \\textbf{Cumulative \\%} \\\\\n\\midrule\nDR = 0\\%      & 18 & 22\\% \\\\\n0\\% $<$ DR $<$ 2\\%   & 37 & 67\\% \\\\\n2\\%--10\\%     & 12 & 82\\% \\\\\n10\\%--20\\%    & 7  & 90\\% \\\\\n20\\%--40\\%    & 6  & 98\\% \\\\\n$>$ 40\\%      & 8  & 100\\% \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Summary statistics:}} \\\\\n\\multicolumn{2}{l}{Median DR} & 0.8\\% \\\\\n\\multicolumn{2}{l}{Mean DR} & 10.2\\% \\\\\n\\multicolumn{2}{l}{Gini coefficient} & 0.82 \\\\\n\\multicolumn{2}{l}{Top 15 relations' share of violations} & 76.3\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n67\\% of relations achieve DR $<$ 2\\% (near-complete compliance), while the top 15 high-violation relations contribute 76.3\\% of all violations.\nThe mean/median ratio of 12.75$\\times$ and Gini coefficient of 0.82 confirm extreme concentration.\nThis is not random noise but a systematic consequence of ontology constraint structure, as Section~\\ref{sec:tightness} demonstrates.\n\n\\subsection{Tightness--Violation Correlation}\n\\label{sec:tightness}\n\nWe compute the Spearman rank correlation between constraint tightness (Eq.~\\ref{eq:tightness}) and per-relation DR on DocRED.\nTable~\\ref{tab:tightness} shows a clear monotonic trend across tightness buckets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DocRED per-relation DR by constraint tightness bucket (full S1). Higher tightness $\\to$ higher residual DR. Spearman $\\rho$=0.52, $p<$0.001.}\n\\label{tab:tightness}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Tightness Bucket} & \\textbf{\\# Rels} & \\textbf{Agg.\\ DR (\\%)} \\\\\n\\midrule\n$<$ 0.70          & 2  & 0.7 \\\\\n0.70--0.79        & 18 & 9.0 \\\\\n0.80--0.84        & 23 & 7.0 \\\\\n0.85--0.89        & 28 & 12.9 \\\\\n0.90--0.94        & 15 & 19.3 \\\\\n0.95--1.00        & 4  & 30.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe Spearman $\\rho$=0.52 ($n$=82, $p<$0.001) confirms a statistically significant positive correlation.\nWhile the correlation is moderate in absolute terms, the bucket-level monotonic trend and extreme violation concentration (76.3\\% in top 15 relations) provide strong practical utility: practitioners can estimate constraint effectiveness from the ontology definition alone, before any model inference.\n\nThe mechanism is intuitive: high-tightness relations exclude most of the entity-type space, forcing the semantic mask to block high-probability tokens.\nWhen the model's distributional prior strongly favors invalid type assignments (e.g., \\texttt{P6\\_head\\_of\\_government} with tightness 0.889 and DR 84.6\\%), even per-token logit masking cannot fully redirect probability mass without degrading generation coherence.\n\nIllustrative extreme cases include \\texttt{P6\\_head\\_of\\_government} (tightness 0.889, DR 84.6\\%, $n$=13) and \\texttt{P582\\_end\\_time} (tightness 0.917, DR 43.5\\%, $n$=186), both of which have very narrow valid type pairs.\nIn contrast, \\texttt{P17\\_country} and similar low-tightness relations achieve near-zero DR.\n\n\\subsection{Cross-Model Generalization}\n\\label{sec:crossmodel}\n\nTo verify that our findings are not model-specific, we replicate the SciERC experiments with Llama-3.1-8B.\nTable~\\ref{tab:crossmodel} compares violation rates across models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model comparison on SciERC. Grammar enforcement (ET/RV$\\to$0\\%) and DR reduction generalize across models. $\\rho$ = per-relation DR rank Spearman correlation between models.}\n\\label{tab:crossmodel}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Config} & \\textbf{ET} & \\textbf{RV} & \\textbf{DR} & \\textbf{R-F1} \\\\\n\\midrule\n\\multirow{3}{*}{Qwen3-8B}\n& Unconstrained & $>$0 & 1.4 & 15.4 & 8.23 \\\\\n& Grammar       & 0.0  & 0.0 & ---  & --- \\\\\n& Full S1       & 0.0  & 0.0 & 0.93 & 8.36 \\\\\n\\midrule\n\\multirow{3}{*}{Llama-3.1-8B}\n& Unconstrained & 0.6  & 2.5 & 14.5 & 6.50 \\\\\n& Grammar       & 0.0  & 0.0 & 14.0 & --- \\\\\n& Full S1       & 0.0  & 0.0 & 1.2  & 6.80 \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\textit{Cross-model per-relation DR Spearman} $\\rho$=0.89} \\\\\n\\end{tabular}\n\\end{table}\n\nGrammar enforcement achieves ET/RV$\\to$0\\% on both models, confirming that grammar constraints are model-agnostic (they depend only on the tokenizer vocabulary mapping, automatically adapted by XGrammar).\n\nFull S1 reduces DR from 14.5\\% to 1.2\\% on Llama ($\\downarrow$92\\%), comparable to Qwen's $\\downarrow$94\\%.\nThe cross-model per-relation DR Spearman $\\rho$=0.89 indicates that the \\emph{per-relation violation susceptibility is a property of the ontology constraint structure, not the generating model}---both models violate the same relations at similar rates, driven by constraint tightness.\n\n\\subsection{Cross-Field Consistency Analysis}\n\\label{sec:cf}\n\nConstrained decoding introduces a trade-off: while DR violations decrease, cross-field consistency (CF) violations increase.\nCF violations occur when the same entity is assigned different types across different relations---each individual triple remains type-valid, but cross-triple consistency is broken.\n\nTable~\\ref{tab:cf} presents the CF analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-field consistency (CF) analysis. CF increases with semantic enforcement but at a favorable trade-off ratio (DR reduction per CF increase). EVR = entity-vs-relation type drift (dominant CF sub-type).}\n\\label{tab:cf}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Config} & \\textbf{CF (\\%)} & \\textbf{DR (\\%)} & \\textbf{DR:CF} \\\\\n\\midrule\n\\multirow{3}{*}{SciERC}\n& Unconstrained & $<$0.1 & 15.4 & --- \\\\\n& Grammar-only  & 0.08   & $\\sim$15.4 & --- \\\\\n& Full S1       & 9.9    & 0.93 & 1.5:1 \\\\\n\\midrule\n\\multirow{3}{*}{DocRED}\n& Unconstrained & $<$0.1 & 19.0 & --- \\\\\n& Grammar-only  & 0.07   & ---  & --- \\\\\n& Full S1       & 2.6    & 10.19 & 3.6:1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{CF is 100\\% attributable to the semantic layer.}\nGrammar-only CF rates ($\\leq$0.08\\%) are identical to unconstrained baselines, confirming that grammar enforcement introduces no CF.\nAll CF increase comes from the semantic layer's per-relation independent type enforcement: the semantic mask selects the locally optimal type for each relation's domain/range constraints, without maintaining global entity-type consensus.\n\n\\textbf{Root cause: type system ambiguity.}\nOn SciERC, 90\\% of CF violations are entity-vs-relation type drift (EVR), where the same entity receives different types in the entity list vs.\\ relation triples.\nThe dominant conflict patterns---Generic$\\leftrightarrow$OtherScientificTerm (60 cases), Material$\\leftrightarrow$OtherScientificTerm (28), Material$\\leftrightarrow$Method (20)---reflect genuine semantic boundary ambiguity in SciERC's type system.\n\nThe cross-dataset comparison provides strong evidence for this hypothesis: DocRED CF (2.6\\%) is 3.8$\\times$ lower than SciERC CF (9.9\\%).\nDocRED's entity types (PER/ORG/LOC/TIME/NUM/MISC) have far clearer semantic boundaries than SciERC's (Generic/OtherScientificTerm/Material/Method), confirming that \\emph{CF rate is driven by type system ambiguity}.\nOn DocRED, the dominant CF pattern is ORG$\\leftrightarrow$LOC (23.1\\% of CF), corresponding to the well-known NER ambiguity of geopolitical entities.\n\n\\textbf{Severity distinction.}\nDR violations produce structurally invalid triples unusable by downstream systems (hard constraint).\nCF violations produce individually valid triples with cross-triple inconsistency (soft preference).\nThe trade-off is favorable: on DocRED, each 1pp CF increase buys 3.57pp DR reduction.\n\n\\subsection{Inference Latency}\n\nTable~\\ref{tab:latency} reports inference overhead.\nFull S1 incurs 1.37--1.39$\\times$ overhead across datasets---the grammar layer adds $\\sim$13\\% (XGrammar's optimized C++ pushdown automaton) and the semantic layer adds $\\sim$20\\% (Python-based per-token logit masking).\nThe overhead is per-token and independent of document length.\nFull S2 incurs 2.17$\\times$ overhead due to two forward passes, with no quality benefit.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Inference latency overhead (tokens/second relative to unconstrained).}\n\\label{tab:latency}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Grammar} & \\textbf{Semantic} & \\textbf{Full S1} & \\textbf{Full S2} \\\\\n\\midrule\nSciERC & 1.13$\\times$ & 1.33$\\times$ & 1.37$\\times$ & 2.17$\\times$ \\\\\nDocRED & 1.14$\\times$ & --- & 1.39$\\times$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n%% 6. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\textbf{Constrained decoding for structured generation.}\nGrammar-constrained decoding has been applied to JSON generation, code synthesis, and SQL queries.\nXGrammar and related systems compile formal grammars into efficient token masks.\nRecent work on code generation applies type-checking during decoding in programming language contexts.\n\\sys{} extends this paradigm to IE ontology constraints, introducing semantic-layer enforcement for cross-field constraints beyond CFG expressiveness.\n\n\\textbf{LLM-based information extraction.}\nZero-shot and few-shot LLM-based IE has shown strong results on standard benchmarks.\nHowever, prior work focuses primarily on F1 metrics and largely ignores ontology compliance.\nTo our knowledge, no prior work systematically measures or addresses ontology constraint violations in LLM-generated extractions.\n\n\\textbf{Ontology-aware IE.}\nTraditional IE systems incorporate ontology constraints through training-time loss functions, post-hoc filtering, or ILP-based inference.\nPost-hoc filtering cannot redirect probability mass toward valid outputs and wastes compute on invalid generations.\nTraining-time approaches require task-specific supervision.\n\\sys{} operates at decoding time with zero training, automatically compiled from ontology definitions.\n\n\\textbf{Constraint satisfaction in NLP.}\nLexically constrained decoding enforces keyword inclusion during generation.\nNeurologic and A*-based methods handle more complex constraints.\nThese approaches target surface-level lexical constraints rather than semantic type constraints.\n\\sys{}'s semantic layer addresses a different constraint class---cross-field type compatibility---requiring stateful tracking during generation.\n\n%% ============================================================\n%% 7. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe presented \\sys{}, a framework for enforcing ontology type constraints during LLM-based information extraction via compiled constrained decoding.\nOur violation landscape study reveals that LLM-based IE systems produce systematic, non-uniformly distributed ontology violations driven by constraint tightness.\n\\sys{}'s two-layer architecture---grammar for structural/vocabulary compliance, semantic for cross-field domain/range enforcement---composes via bitwise AND with an enabling dependency, achieving near-complete violation elimination on tightly-constrained ontologies (94\\% DR reduction on SciERC) and predictable partial reduction on complex ontologies (46\\% on DocRED), all at zero F1 cost and $<$1.4$\\times$ latency overhead.\nGrammar-layer enforcement generalizes perfectly across datasets and models.\n\nThe tightness--violation correlation (Spearman $\\rho$=0.52) provides practitioners with an a priori diagnostic for estimating constraint effectiveness from ontology definitions alone, without model inference.\n\n\\textbf{Limitations.}\nCross-field consistency violations are an inherent trade-off of per-relation independent type enforcement (9.9\\% on SciERC, 2.6\\% on DocRED), with CF rate driven by type system ambiguity.\nFuture work should explore global entity-type consensus mechanisms---e.g., a pre-decoding entity-type resolution pass---to maintain cross-relation consistency.\nOur evaluation covers two datasets and two models; broader validation across ontologies, languages, and model scales is needed.\nThe current implementation uses a Python-based semantic layer; a C++ implementation would reduce the 20\\% semantic overhead.\n\n\\bibliographystyle{plainnat}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d58a4bbb-7014-4395-9327-2ba718d6f635",
  "isSidechain": false,
  "requestId": "req_011Cb2JYARdB3a3H4hu8FH3b",
  "type": "assistant",
  "uuid": "0ccc803d-8f8c-4e37-8839-4910164dfbaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T6B38ovFiWFjpGeSyFdmg1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7805,
      "cache_read_input_tokens": 38951,
      "output_tokens": 10625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10625,
          "cache_read_input_tokens": 38951,
          "cache_creation_input_tokens": 7805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7805
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

_source line 21 · 2026-05-14T10:31:32.899Z_

<details><summary>↩ Tool result · `toolu_01Gxg9iaprinHuU1VMTfrcPJ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ccc803d-8f8c-4e37-8839-4910164dfbaf",
  "isSidechain": false,
  "promptId": "09bcd997-7727-4bef-8159-0d7f38bdc5f8",
  "type": "user",
  "uuid": "12863f56-cb0b-4811-ad21-582bf3936a6e",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\sys}{OntoCoDec}\n\\newcommand{\\drr}{domain/range violation rate}\n\n\\title{\\sys{}: Near-Complete Type-Valid Information Extraction\\\\via Compiled Ontology Constraints}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nLLM-based information extraction (IE) systems produce systematic ontology constraint violations---15.4\\% of triples on SciERC and 18.7\\% on DocRED violate domain/range type constraints.\nSchema-informed prompting reduces violations by up to 62\\% on simple ontologies but scales poorly to complex ones (only 32\\% on DocRED's 96-relation ontology), and can even \\emph{increase} violations for specific relation types.\nWe present \\sys{}, a framework that automatically compiles IE ontology schemas into two composable constrained decoding layers: (1)~a \\emph{grammar layer} that enforces structural validity and vocabulary compliance via context-free grammar constraints, and (2)~a \\emph{semantic layer} that enforces cross-field domain/range constraints through a stateful entity registry with dynamic logit masking.\nThe two layers compose via bitwise AND of token masks with an enabling dependency: grammar ensures every relation type is valid, enabling semantic lookup of domain/range rules.\nOn SciERC, \\sys{} achieves near-complete violation elimination (domain/range violations 15.4\\%$\\to$0.93\\%, $\\downarrow$94\\%) at zero F1 cost.\nOn DocRED, a complex ontology with inherently high constraint tightness, \\sys{} achieves predictable partial reduction (19.0\\%$\\to$10.19\\%, $\\downarrow$46\\%), with 67\\% of relation types reaching $<$2\\% violation rate.\nResidual violations concentrate in a predictable minority of high-tightness relations (Spearman $\\rho$=0.52 between constraint tightness and violation rate, $p<$0.001), providing practitioners with a priori estimates of constraint effectiveness.\nGrammar-layer enforcement generalizes perfectly across datasets (entity-type and relation-vocabulary violations $\\to$0\\%) and models (Qwen3-8B, Llama-3.1-8B).\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nLarge language models have emerged as powerful zero-shot information extraction systems, capable of extracting structured relational triples from unstructured text without task-specific training.\nHowever, their outputs frequently violate the type constraints specified by the target ontology.\nA relation such as \\texttt{Feature-of} may require its head entity to be of type \\texttt{OtherScientificTerm} and its tail of type \\texttt{Method}, yet the model generates type-incompatible entity pairs in over 33\\% of instances.\n\nThese violations are not merely cosmetic. Downstream knowledge graph population, reasoning engines, and regulatory compliance systems require structurally valid triples.\nPost-hoc filtering discards 14--15\\% of generated triples, wasting compute without redirecting probability mass toward valid alternatives.\nSchema-informed prompting---explicitly describing domain/range constraints in the prompt---provides partial relief but is fundamentally unreliable: on SciERC, it reduces overall violations from 15.4\\% to 5.78\\% ($\\downarrow$62\\%), yet the \\texttt{Evaluate-for} relation's violation rate \\emph{increases} from 24.1\\% to 29.9\\%, indicating active interference between prompt-level constraint signals and the model's learned type associations.\nMoreover, prompt-level intervention scales poorly with ontology complexity: on DocRED (96 relations), reduction drops to only 32\\%.\n\nWe make three contributions:\n\n\\noindent\\textbf{(1) Violation Landscape Study.}\nWe present the first systematic measurement of ontology constraint violations in LLM-based IE across two datasets and two models.\nWe show that violation rates are driven by \\emph{constraint tightness}---the fraction of the entity-type space excluded by a relation's domain/range rules---not ontology size.\nSciERC (7 relations) and DocRED (96 relations) exhibit comparable overall violation rates (15.4\\% vs.\\ 18.7\\%) despite a 14$\\times$ difference in ontology size.\n\n\\noindent\\textbf{(2) \\sys{} Framework.}\nWe propose a two-layer constrained decoding framework that automatically compiles IE ontology schemas into composable decoder constraints.\nThe grammar layer (built on XGrammar) enforces JSON structure, entity-type vocabulary, and relation-type vocabulary via context-free grammar constraints.\nThe semantic layer (TypeConstraintProcessor) maintains a stateful entity registry during autoregressive generation and dynamically masks logits to enforce domain/range type compatibility.\nThe layers compose via bitwise AND with an enabling dependency: grammar ensures valid relation vocabulary, enabling semantic domain/range lookup.\n\n\\noindent\\textbf{(3) Tightness--Violation Correlation.}\nWe establish that per-relation constraint tightness predicts residual violation rates (Spearman $\\rho$=0.52, $p<$0.001 on DocRED), with violations concentrating in a predictable minority of high-tightness relations (top 15 relations account for 76.3\\% of all violations).\nThis provides practitioners with an a priori diagnostic for estimating constraint effectiveness on new ontologies.\n\n%% ============================================================\n%% 2. BACKGROUND\n%% ============================================================\n\\section{Background}\n\n\\subsection{IE Ontology Constraints}\n\nAn IE ontology $\\mathcal{O} = (\\mathcal{E}, \\mathcal{R}, \\mathcal{D})$ defines a set of valid entity types $\\mathcal{E}$, relation types $\\mathcal{R}$, and domain/range constraints $\\mathcal{D}: \\mathcal{R} \\to 2^{\\mathcal{E}} \\times 2^{\\mathcal{E}}$.\nFor each relation $r \\in \\mathcal{R}$, the constraint $\\mathcal{D}(r) = (\\mathcal{E}_h^r, \\mathcal{E}_t^r)$ specifies the valid head entity types $\\mathcal{E}_h^r \\subseteq \\mathcal{E}$ and tail entity types $\\mathcal{E}_t^r \\subseteq \\mathcal{E}$.\nA triple $(e_h, r, e_t)$ with $\\text{type}(e_h) \\notin \\mathcal{E}_h^r$ or $\\text{type}(e_t) \\notin \\mathcal{E}_t^r$ constitutes a \\emph{domain/range violation}.\n\nWe define the \\emph{constraint tightness} of a relation $r$ as:\n\\begin{equation}\n    \\text{tightness}(r) = 1 - \\frac{|\\mathcal{E}_h^r| \\cdot |\\mathcal{E}_t^r|}{|\\mathcal{E}|^2}\n    \\label{eq:tightness}\n\\end{equation}\nA tightness of 1.0 means only one entity-type pair is valid; 0.0 means all pairs are valid (no constraint). This metric captures the fraction of the type space excluded by a relation's constraints.\n\n\\subsection{Grammar-Constrained Decoding}\n\nGrammar-constrained decoding restricts the output of autoregressive language models to strings accepted by a formal grammar, typically a context-free grammar (CFG).\nAt each decoding step, a token mask $M_t \\in \\{0,1\\}^{|V|}$ is computed over the vocabulary $V$, zeroing out logits for tokens that would lead to strings outside the grammar's language.\nXGrammar compiles grammars into pushdown automata with precomputed token masks, achieving near-zero overhead.\n\nGrammar-constrained decoding can enforce structural constraints (valid JSON, correct field names) and vocabulary constraints (entity types $\\in \\mathcal{E}$, relation types $\\in \\mathcal{R}$).\nHowever, it cannot enforce \\emph{cross-field} constraints: whether a generated entity type is compatible with the relation type in the same triple requires maintaining state across generation positions, which is beyond CFG expressiveness.\n\n\\subsection{Constraint Decidability Taxonomy}\n\nWe classify IE ontology constraints by prefix-decidability during autoregressive generation:\n\\begin{itemize}\n    \\item \\textbf{Type (a) -- Purely local:} Entity type $\\in \\mathcal{E}$, relation type $\\in \\mathcal{R}$. Decidable from the current token position alone. Enforceable by grammar.\n    \\item \\textbf{Type (b) -- Prefix-decidable with state:} Domain/range compatibility. Requires maintaining an entity registry across generation positions. Enforceable by stateful logit masking (semantic layer).\n    \\item \\textbf{Type (c) -- Truly non-local:} Forward coreference (entity mentioned later constrains earlier type assignment). Requires future context; out of scope for forward-only decoding.\n\\end{itemize}\n\n%% ============================================================\n%% 3. VIOLATION LANDSCAPE STUDY\n%% ============================================================\n\\section{Violation Landscape Study}\n\\label{sec:landscape}\n\nBefore proposing a solution, we systematically measure the extent and distribution of ontology constraint violations in LLM-based zero-shot IE.\n\n\\subsection{Experimental Setup}\n\nWe evaluate Qwen3-8B on two IE benchmarks with structured ontology definitions:\n\n\\noindent\\textbf{SciERC} contains 551 scientific abstracts annotated with 6 entity types and 7 relation types. The ontology is compact but several relations have tight domain/range constraints.\n\n\\noindent\\textbf{DocRED} contains 998 Wikipedia documents annotated with 6 entity types and 96 relation types drawn from Wikidata. The ontology is large and heterogeneous, with wide variance in constraint tightness (mean tightness 0.842, range 0.50--0.97).\n\nWe measure four violation types: (1)~\\emph{entity-type violations} (ET): generated entity type $\\notin \\mathcal{E}$; (2)~\\emph{relation-vocabulary violations} (RV): generated relation type $\\notin \\mathcal{R}$; (3)~\\emph{domain/range violations} (DR): entity type incompatible with relation's domain/range constraints; (4)~\\emph{cross-field consistency violations} (CF): same entity assigned different types across relations.\n\n\\subsection{Unconstrained Baseline Results}\n\nTable~\\ref{tab:landscape} summarizes the violation landscape.\nBoth datasets exhibit substantial DR rates (15.4\\% SciERC, 18.7\\% DocRED) despite the 14$\\times$ difference in ontology size, confirming that violation rates are driven by constraint structure rather than ontology scale.\n\nSchema-informed prompting---embedding explicit domain/range constraint descriptions in the prompt---reduces DR by 62\\% on SciERC but only 32\\% on DocRED, demonstrating that prompt-level intervention scales poorly with ontology complexity.\nOn SciERC, three relation types retain $>$10\\% DR even with schema-informed prompting (Compare: 27.6\\%, Evaluate-for: 29.9\\%, Feature-of: 11.3\\%).\nThe \\texttt{Evaluate-for} violation rate \\emph{increases} with schema-informed prompting (24.1\\%$\\to$29.9\\%), indicating prior-constraint conflict.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Violation landscape: unconstrained LLM-based IE (Qwen3-8B, zero-shot). DR = domain/range violation rate. Schema = schema-informed prompt.}\n\\label{tab:landscape}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Dataset} & $|\\mathcal{R}|$ & \\textbf{DR (\\%)} & \\textbf{Schema DR (\\%)} & \\textbf{$\\Delta$ DR} \\\\\n\\midrule\nSciERC  & 7  & 15.4 & 5.78 & $\\downarrow$62\\% \\\\\nDocRED  & 96 & 18.7 & 12.8 & $\\downarrow$32\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Relation Violation Distribution}\n\nViolations are not uniformly distributed across relation types.\nOn SciERC, \\texttt{Used-for} has only 0.8\\% DR while \\texttt{Compare} reaches 42.4\\%.\nThe key differentiator is constraint tightness: \\texttt{Compare} requires both arguments to be of type \\texttt{Method}, excluding $>$97\\% of the entity-type space, while \\texttt{Used-for} accepts a broad range of type pairs.\n\nOn DocRED (Section~\\ref{sec:tightness}), we formally quantify this relationship: Spearman $\\rho$=0.52 ($p<$0.001) between constraint tightness and per-relation DR, with a clear monotonic trend across tightness buckets.\n\n%% ============================================================\n%% 4. ONTOCODEC FRAMEWORK\n%% ============================================================\n\\section{The \\sys{} Framework}\n\\label{sec:method}\n\n\\sys{} automatically compiles an IE ontology schema $\\mathcal{O}$ into constrained decoding layers that enforce type validity during autoregressive generation.\nThe framework consists of three components: an ontology compiler, a grammar constraint layer, and a semantic constraint layer.\n\n\\subsection{Ontology Compiler}\n\nThe compiler takes as input an ontology definition $\\mathcal{O} = (\\mathcal{E}, \\mathcal{R}, \\mathcal{D})$ and produces:\n\\begin{enumerate}\n    \\item A context-free grammar $G$ encoding valid JSON structure with entity-type and relation-type vocabularies;\n    \\item A domain/range lookup table $T: \\mathcal{R} \\to 2^{\\mathcal{E}} \\times 2^{\\mathcal{E}}$ for runtime type checking.\n\\end{enumerate}\nThe compilation is fully automatic---practitioners provide only the ontology definition (entity types, relation types, and domain/range constraints), requiring zero additional code for schema compliance.\n\n\\subsection{Grammar Layer}\n\nThe grammar layer compiles $G$ into an XGrammar pushdown automaton.\nAt each decoding step $t$, it computes a mask $M_t^{\\text{gram}} \\in \\{0,1\\}^{|V|}$ that allows only tokens leading to valid JSON with:\n\\begin{itemize}\n    \\item Correct JSON structure (entity list + relation list with typed fields)\n    \\item Entity types $\\in \\mathcal{E}$\n    \\item Relation types $\\in \\mathcal{R}$\n\\end{itemize}\nThis eliminates entity-type violations (ET$\\to$0\\%) and relation-vocabulary violations (RV$\\to$0\\%) by construction, regardless of the model or ontology size.\n\n\\subsection{Semantic Layer: TypeConstraintProcessor}\n\nThe semantic layer maintains a stateful entity registry $\\mathcal{S}$ during generation.\nAs entities are generated in the entity list portion of the output, $\\mathcal{S}$ records each entity's name and type.\nWhen the model generates a relation triple, the processor:\n\\begin{enumerate}\n    \\item Identifies the current generation position (head entity type, relation type, or tail entity type);\n    \\item Looks up the relation type $r$ in the domain/range table $T$;\n    \\item Computes a mask $M_t^{\\text{sem}}$ that allows only entity types compatible with $\\mathcal{D}(r)$.\n\\end{enumerate}\n\nThe semantic layer enforces Type~(b) constraints (prefix-decidable with state) that are beyond CFG expressiveness.\n\n\\subsection{Layer Composition}\n\nThe two layers compose via bitwise AND:\n\\begin{equation}\n    M_t = M_t^{\\text{gram}} \\wedge M_t^{\\text{sem}}\n    \\label{eq:compose}\n\\end{equation}\n\nThis composition has an \\emph{enabling dependency}: the grammar layer ensures every generated relation type $r \\in \\mathcal{R}$, which is a prerequisite for the semantic layer to look up $\\mathcal{D}(r)$.\nWithout grammar enforcement, the semantic layer encounters unknown relation types for which no domain/range rules exist, rendering it unable to enforce constraints on those triples.\n\n\\textbf{Graceful degradation.}\nWhen $M_t^{\\text{sem}} \\cap M_t^{\\text{gram}} = \\emptyset$ (the semantic layer would mask all grammar-valid tokens), the system falls back to grammar-only constraints: $M_t = M_t^{\\text{gram}}$.\nThis maintains structural validity as a guaranteed floor.\nIn practice, this fallback is rare: 1/998 documents on DocRED (0.1\\%), 0/551 on SciERC.\n\n\\subsection{Decoding Strategies}\n\nWe evaluate two strategies:\n\n\\noindent\\textbf{S1 (Single-pass):} Both grammar and semantic layers are active throughout generation. Recommended as the primary strategy due to simplicity and marginally better metrics.\n\n\\noindent\\textbf{S2 (Two-pass):} Pass~1 extracts entities with grammar-only constraints; Pass~2 generates relations with an input-dependent grammar compiled from Pass~1 entities.\nS2 is an architectural variant demonstrating framework flexibility; it does not improve over S1 on any metric (Section~\\ref{sec:exp}).\n\n%% ============================================================\n%% 5. EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\\label{sec:exp}\n\n\\subsection{Setup}\n\nWe evaluate \\sys{} on SciERC (551 sentences) and DocRED (998 documents) using Qwen3-8B in a zero-shot setting.\nWe compare five configurations: \\emph{unconstrained} (baseline), \\emph{grammar-only} (grammar layer only), \\emph{semantic-only} (semantic layer only), \\emph{full S1} (both layers, single-pass), and \\emph{full S2} (both layers, two-pass).\nCross-model generalization is evaluated with Llama-3.1-8B on SciERC.\nF1 is reported as a control variable to verify that constraints do not degrade extraction quality, not as an optimization target.\n\n\\subsection{Grammar Layer: Perfect Cross-Dataset Generalization}\n\nTable~\\ref{tab:grammar} presents grammar-layer results across datasets.\nGrammar-constrained decoding eliminates entity-type violations entirely (ET$\\to$0\\%) and relation-vocabulary violations to near-zero (RV$\\to$0\\% on SciERC, 0.03\\% on DocRED) across both datasets, scaling from 7 to 96 relation types (14$\\times$) with no degradation.\nThe 5 residual RV violations on DocRED (out of 17,341 triples) likely stem from tokenizer boundary effects on long relation names.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Grammar layer eliminates ET and RV violations across datasets. Grammar-only configuration; violations in constrained output.}\n\\label{tab:grammar}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Dataset} & $|\\mathcal{R}|$ & \\textbf{Triples} & \\textbf{ET (\\%)} & \\textbf{RV (\\%)} \\\\\n\\midrule\nSciERC  & 7  & 1,725  & 0.0 & 0.0 \\\\\nDocRED  & 96 & 17,341 & 0.0 & 0.03 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{SciERC: Near-Complete Violation Elimination}\n\nTable~\\ref{tab:scierc} presents the full ablation on SciERC.\nFull S1 reduces DR from 15.4\\% to 0.93\\% ($\\downarrow$94\\%) while maintaining F1 (8.36\\% vs.\\ 8.23\\% unconstrained; the +0.13pp difference is not statistically significant).\n\nThe enabling dependency between layers is quantified by the \\emph{enabling ratio}: the DR reduction achieved by full S1 divided by that of semantic-only.\nOn SciERC, full S1 achieves 14.4pp DR reduction vs.\\ semantic-only's 3.7pp, yielding an enabling ratio of 3.88$\\times$.\nSemantic-only achieves only 24.2\\% DR reduction because $\\sim$1.4\\% of triples use out-of-vocabulary relation types for which no domain/range rules can be looked up.\n\nFull S2 shows no improvement over S1: DR 0.97\\% (vs.\\ 0.93\\%), CF 8.03\\% (vs.\\ 9.90\\%), R-F1 8.03\\% (vs.\\ 8.36\\%).\nS2 is positioned as an architectural variant, not a recommended strategy.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SciERC constrained decoding ablation (Qwen3-8B, 551 sentences). DR = domain/range violation rate (\\%), CF = cross-field consistency violation rate (\\%), R-F1 = relation F1 (\\%).}\n\\label{tab:scierc}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Config} & \\textbf{ET} & \\textbf{RV} & \\textbf{DR} & \\textbf{CF} & \\textbf{R-F1} & \\textbf{DR $\\Delta$} \\\\\n\\midrule\nUnconstrained   & $>$0 & 1.4 & 15.4 & $<$0.1 & 8.23 & --- \\\\\nGrammar-only    & 0.0  & 0.0 & $\\sim$15.4 & $<$0.1 & --- & $\\sim$0\\% \\\\\nSemantic-only   & ---  & --- & 11.7 & 2.7  & --- & $\\downarrow$24\\% \\\\\nFull S1         & 0.0  & 0.0 & 0.93 & 9.9  & 8.36 & $\\downarrow$94\\% \\\\\nFull S2         & 0.0  & 0.0 & 0.97 & 8.0  & 8.03 & $\\downarrow$94\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{DocRED: Predictable Partial Reduction}\n\nTable~\\ref{tab:docred} presents results on DocRED.\nFull S1 reduces DR from 19.0\\% to 10.19\\% ($\\downarrow$46.4\\%).\nWhile the absolute reduction is lower than SciERC's 94\\%, this is predicted by DocRED's higher mean constraint tightness (0.842): tighter constraints force the semantic mask to exclude high-probability tokens, making violations harder to prevent without quality degradation.\n\nThe enabling dependency is preserved: semantic-only achieves only 18.4\\% DR reduction (enabling ratio 2.52$\\times$).\nThis ratio is lower than SciERC's 3.88$\\times$ because DocRED's unconstrained RV is much higher (28.9\\% vs.\\ 1.4\\%), meaning the semantic layer is blind to nearly one-third of triples without grammar enforcement.\nThis confirms that the enabling dependency becomes \\emph{more necessary} as ontology complexity increases.\n\nF1 is preserved: R-F1 8.17\\% (full S1) vs.\\ 8.20\\% (unconstrained), confirming F1-neutral enforcement.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DocRED constrained decoding ablation (Qwen3-8B, 998 documents). ET/RV/DR/CF as violation rates (\\%).}\n\\label{tab:docred}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Config} & \\textbf{ET} & \\textbf{RV} & \\textbf{DR} & \\textbf{CF} & \\textbf{R-F1} & \\textbf{DR $\\Delta$} \\\\\n\\midrule\nUnconstrained   & 7.5  & 28.9 & 19.0 & $<$0.1 & 8.20 & --- \\\\\nGrammar-only    & 0.0  & 0.03 & ---  & $<$0.1 & 8.24 & --- \\\\\nSemantic-only   & 7.3  & 28.7 & 15.5 & 2.5  & 8.00 & $\\downarrow$18\\% \\\\\nFull S1         & 0.0  & 0.03 & 10.19 & 2.6  & 8.17 & $\\downarrow$46\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Relation DR Distribution on DocRED}\n\\label{sec:bimodal}\n\nThe aggregate 10.19\\% DR on DocRED masks a highly skewed per-relation distribution.\nTable~\\ref{tab:bimodal} summarizes the distribution across 82 relation types with $\\geq$5 triples.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DocRED full S1 per-relation DR distribution (82 relations with $\\geq$5 triples). Violations are concentrated in a small minority of high-DR relations.}\n\\label{tab:bimodal}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{DR Range} & \\textbf{\\# Relations} & \\textbf{Cumulative \\%} \\\\\n\\midrule\nDR = 0\\%      & 18 & 22\\% \\\\\n0\\% $<$ DR $<$ 2\\%   & 37 & 67\\% \\\\\n2\\%--10\\%     & 12 & 82\\% \\\\\n10\\%--20\\%    & 7  & 90\\% \\\\\n20\\%--40\\%    & 6  & 98\\% \\\\\n$>$ 40\\%      & 8  & 100\\% \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Summary statistics:}} \\\\\n\\multicolumn{2}{l}{Median DR} & 0.8\\% \\\\\n\\multicolumn{2}{l}{Mean DR} & 10.2\\% \\\\\n\\multicolumn{2}{l}{Gini coefficient} & 0.82 \\\\\n\\multicolumn{2}{l}{Top 15 relations' share of violations} & 76.3\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n67\\% of relations achieve DR $<$ 2\\% (near-complete compliance), while the top 15 high-violation relations contribute 76.3\\% of all violations.\nThe mean/median ratio of 12.75$\\times$ and Gini coefficient of 0.82 confirm extreme concentration.\nThis is not random noise but a systematic consequence of ontology constraint structure, as Section~\\ref{sec:tightness} demonstrates.\n\n\\subsection{Tightness--Violation Correlation}\n\\label{sec:tightness}\n\nWe compute the Spearman rank correlation between constraint tightness (Eq.~\\ref{eq:tightness}) and per-relation DR on DocRED.\nTable~\\ref{tab:tightness} shows a clear monotonic trend across tightness buckets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DocRED per-relation DR by constraint tightness bucket (full S1). Higher tightness $\\to$ higher residual DR. Spearman $\\rho$=0.52, $p<$0.001.}\n\\label{tab:tightness}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Tightness Bucket} & \\textbf{\\# Rels} & \\textbf{Agg.\\ DR (\\%)} \\\\\n\\midrule\n$<$ 0.70          & 2  & 0.7 \\\\\n0.70--0.79        & 18 & 9.0 \\\\\n0.80--0.84        & 23 & 7.0 \\\\\n0.85--0.89        & 28 & 12.9 \\\\\n0.90--0.94        & 15 & 19.3 \\\\\n0.95--1.00        & 4  & 30.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe Spearman $\\rho$=0.52 ($n$=82, $p<$0.001) confirms a statistically significant positive correlation.\nWhile the correlation is moderate in absolute terms, the bucket-level monotonic trend and extreme violation concentration (76.3\\% in top 15 relations) provide strong practical utility: practitioners can estimate constraint effectiveness from the ontology definition alone, before any model inference.\n\nThe mechanism is intuitive: high-tightness relations exclude most of the entity-type space, forcing the semantic mask to block high-probability tokens.\nWhen the model's distributional prior strongly favors invalid type assignments (e.g., \\texttt{P6\\_head\\_of\\_government} with tightness 0.889 and DR 84.6\\%), even per-token logit masking cannot fully redirect probability mass without degrading generation coherence.\n\nIllustrative extreme cases include \\texttt{P6\\_head\\_of\\_government} (tightness 0.889, DR 84.6\\%, $n$=13) and \\texttt{P582\\_end\\_time} (tightness 0.917, DR 43.5\\%, $n$=186), both of which have very narrow valid type pairs.\nIn contrast, \\texttt{P17\\_country} and similar low-tightness relations achieve near-zero DR.\n\n\\subsection{Cross-Model Generalization}\n\\label{sec:crossmodel}\n\nTo verify that our findings are not model-specific, we replicate the SciERC experiments with Llama-3.1-8B.\nTable~\\ref{tab:crossmodel} compares violation rates across models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model comparison on SciERC. Grammar enforcement (ET/RV$\\to$0\\%) and DR reduction generalize across models. $\\rho$ = per-relation DR rank Spearman correlation between models.}\n\\label{tab:crossmodel}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Config} & \\textbf{ET} & \\textbf{RV} & \\textbf{DR} & \\textbf{R-F1} \\\\\n\\midrule\n\\multirow{3}{*}{Qwen3-8B}\n& Unconstrained & $>$0 & 1.4 & 15.4 & 8.23 \\\\\n& Grammar       & 0.0  & 0.0 & ---  & --- \\\\\n& Full S1       & 0.0  & 0.0 & 0.93 & 8.36 \\\\\n\\midrule\n\\multirow{3}{*}{Llama-3.1-8B}\n& Unconstrained & 0.6  & 2.5 & 14.5 & 6.50 \\\\\n& Grammar       & 0.0  & 0.0 & 14.0 & --- \\\\\n& Full S1       & 0.0  & 0.0 & 1.2  & 6.80 \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\textit{Cross-model per-relation DR Spearman} $\\rho$=0.89} \\\\\n\\end{tabular}\n\\end{table}\n\nGrammar enforcement achieves ET/RV$\\to$0\\% on both models, confirming that grammar constraints are model-agnostic (they depend only on the tokenizer vocabulary mapping, automatically adapted by XGrammar).\n\nFull S1 reduces DR from 14.5\\% to 1.2\\% on Llama ($\\downarrow$92\\%), comparable to Qwen's $\\downarrow$94\\%.\nThe cross-model per-relation DR Spearman $\\rho$=0.89 indicates that the \\emph{per-relation violation susceptibility is a property of the ontology constraint structure, not the generating model}---both models violate the same relations at similar rates, driven by constraint tightness.\n\n\\subsection{Cross-Field Consistency Analysis}\n\\label{sec:cf}\n\nConstrained decoding introduces a trade-off: while DR violations decrease, cross-field consistency (CF) violations increase.\nCF violations occur when the same entity is assigned different types across different relations---each individual triple remains type-valid, but cross-triple consistency is broken.\n\nTable~\\ref{tab:cf} presents the CF analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-field consistency (CF) analysis. CF increases with semantic enforcement but at a favorable trade-off ratio (DR reduction per CF increase). EVR = entity-vs-relation type drift (dominant CF sub-type).}\n\\label{tab:cf}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Config} & \\textbf{CF (\\%)} & \\textbf{DR (\\%)} & \\textbf{DR:CF} \\\\\n\\midrule\n\\multirow{3}{*}{SciERC}\n& Unconstrained & $<$0.1 & 15.4 & --- \\\\\n& Grammar-only  & 0.08   & $\\sim$15.4 & --- \\\\\n& Full S1       & 9.9    & 0.93 & 1.5:1 \\\\\n\\midrule\n\\multirow{3}{*}{DocRED}\n& Unconstrained & $<$0.1 & 19.0 & --- \\\\\n& Grammar-only  & 0.07   & ---  & --- \\\\\n& Full S1       & 2.6    & 10.19 & 3.6:1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{CF is 100\\% attributable to the semantic layer.}\nGrammar-only CF rates ($\\leq$0.08\\%) are identical to unconstrained baselines, confirming that grammar enforcement introduces no CF.\nAll CF increase comes from the semantic layer's per-relation independent type enforcement: the semantic mask selects the locally optimal type for each relation's domain/range constraints, without maintaining global entity-type consensus.\n\n\\textbf{Root cause: type system ambiguity.}\nOn SciERC, 90\\% of CF violations are entity-vs-relation type drift (EVR), where the same entity receives different types in the entity list vs.\\ relation triples.\nThe dominant conflict patterns---Generic$\\leftrightarrow$OtherScientificTerm (60 cases), Material$\\leftrightarrow$OtherScientificTerm (28), Material$\\leftrightarrow$Method (20)---reflect genuine semantic boundary ambiguity in SciERC's type system.\n\nThe cross-dataset comparison provides strong evidence for this hypothesis: DocRED CF (2.6\\%) is 3.8$\\times$ lower than SciERC CF (9.9\\%).\nDocRED's entity types (PER/ORG/LOC/TIME/NUM/MISC) have far clearer semantic boundaries than SciERC's (Generic/OtherScientificTerm/Material/Method), confirming that \\emph{CF rate is driven by type system ambiguity}.\nOn DocRED, the dominant CF pattern is ORG$\\leftrightarrow$LOC (23.1\\% of CF), corresponding to the well-known NER ambiguity of geopolitical entities.\n\n\\textbf{Severity distinction.}\nDR violations produce structurally invalid triples unusable by downstream systems (hard constraint).\nCF violations produce individually valid triples with cross-triple inconsistency (soft preference).\nThe trade-off is favorable: on DocRED, each 1pp CF increase buys 3.57pp DR reduction.\n\n\\subsection{Inference Latency}\n\nTable~\\ref{tab:latency} reports inference overhead.\nFull S1 incurs 1.37--1.39$\\times$ overhead across datasets---the grammar layer adds $\\sim$13\\% (XGrammar's optimized C++ pushdown automaton) and the semantic layer adds $\\sim$20\\% (Python-based per-token logit masking).\nThe overhead is per-token and independent of document length.\nFull S2 incurs 2.17$\\times$ overhead due to two forward passes, with no quality benefit.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Inference latency overhead (tokens/second relative to unconstrained).}\n\\label{tab:latency}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Grammar} & \\textbf{Semantic} & \\textbf{Full S1} & \\textbf{Full S2} \\\\\n\\midrule\nSciERC & 1.13$\\times$ & 1.33$\\times$ & 1.37$\\times$ & 2.17$\\times$ \\\\\nDocRED & 1.14$\\times$ & --- & 1.39$\\times$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n%% 6. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\textbf{Constrained decoding for structured generation.}\nGrammar-constrained decoding has been applied to JSON generation, code synthesis, and SQL queries.\nXGrammar and related systems compile formal grammars into efficient token masks.\nRecent work on code generation applies type-checking during decoding in programming language contexts.\n\\sys{} extends this paradigm to IE ontology constraints, introducing semantic-layer enforcement for cross-field constraints beyond CFG expressiveness.\n\n\\textbf{LLM-based information extraction.}\nZero-shot and few-shot LLM-based IE has shown strong results on standard benchmarks.\nHowever, prior work focuses primarily on F1 metrics and largely ignores ontology compliance.\nTo our knowledge, no prior work systematically measures or addresses ontology constraint violations in LLM-generated extractions.\n\n\\textbf{Ontology-aware IE.}\nTraditional IE systems incorporate ontology constraints through training-time loss functions, post-hoc filtering, or ILP-based inference.\nPost-hoc filtering cannot redirect probability mass toward valid outputs and wastes compute on invalid generations.\nTraining-time approaches require task-specific supervision.\n\\sys{} operates at decoding time with zero training, automatically compiled from ontology definitions.\n\n\\textbf{Constraint satisfaction in NLP.}\nLexically constrained decoding enforces keyword inclusion during generation.\nNeurologic and A*-based methods handle more complex constraints.\nThese approaches target surface-level lexical constraints rather than semantic type constraints.\n\\sys{}'s semantic layer addresses a different constraint class---cross-field type compatibility---requiring stateful tracking during generation.\n\n%% ============================================================\n%% 7. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe presented \\sys{}, a framework for enforcing ontology type constraints during LLM-based information extraction via compiled constrained decoding.\nOur violation landscape study reveals that LLM-based IE systems produce systematic, non-uniformly distributed ontology violations driven by constraint tightness.\n\\sys{}'s two-layer architecture---grammar for structural/vocabulary compliance, semantic for cross-field domain/range enforcement---composes via bitwise AND with an enabling dependency, achieving near-complete violation elimination on tightly-constrained ontologies (94\\% DR reduction on SciERC) and predictable partial reduction on complex ontologies (46\\% on DocRED), all at zero F1 cost and $<$1.4$\\times$ latency overhead.\nGrammar-layer enforcement generalizes perfectly across datasets and models.\n\nThe tightness--violation correlation (Spearman $\\rho$=0.52) provides practitioners with an a priori diagnostic for estimating constraint effectiveness from ontology definitions alone, without model inference.\n\n\\textbf{Limitations.}\nCross-field consistency violations are an inherent trade-off of per-relation independent type enforcement (9.9\\% on SciERC, 2.6\\% on DocRED), with CF rate driven by type system ambiguity.\nFuture work should explore global entity-type consensus mechanisms---e.g., a pre-decoding entity-type resolution pass---to maintain cross-relation consistency.\nOur evaluation covers two datasets and two models; broader validation across ontologies, languages, and model scales is needed.\nThe current implementation uses a Python-based semantic layer; a C++ implementation would reduce the 20\\% semantic overhead.\n\n\\bibliographystyle{plainnat}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "0ccc803d-8f8c-4e37-8839-4910164dfbaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_co…",
  "leafUuid": "12863f56-cb0b-4811-ad21-582bf3936a6e",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete paper for dream session",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246"
}
```

---

### Tool call

_source line 24 · 2026-05-14T10:31:36.496Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Phj6ANpGPZbhHdtLKt2vAt`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12863f56-cb0b-4811-ad21-582bf3936a6e",
  "isSidechain": false,
  "requestId": "req_011Cb2JoBtMC8VowLXGSNnsz",
  "type": "assistant",
  "uuid": "beee7ff9-00d6-49ed-ad73-b1b6e063d11a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BeKyiErvwSJhRECWm61HCd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10693,
      "cache_read_input_tokens": 46756,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10693,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 46756,
          "cache_creation_input_tokens": 10693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10693
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

_source line 25 · 2026-05-14T10:31:45.488Z_

<details><summary>↩ Tool result · `toolu_01Phj6ANpGPZbhHdtLKt2vAt`</summary>

```text
&lt;persisted-output>
Output too large (58.1KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/16dcf9d3-8694-4893-940b-07925e20d246/tool-results/b4oxozv8e.txt

Preview (first 2KB):
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "beee7ff9-00d6-49ed-ad73-b1b6e063d11a",
  "isSidechain": false,
  "promptId": "09bcd997-7727-4bef-8159-0d7f38bdc5f8",
  "type": "user",
  "uuid": "819f7b55-fe3f-4beb-9fb6-bbfff56d3b8d",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (5.96884pt too wide) in paragraph at lines 45--48\n\\T1/cmr/m/n/10.95 ogy. A re-la-tion such as \\T1/cmtt/m/n/10.95 Feature-of \\T1/c\nmr/m/n/10.95 may re-quire its head en-tity to be of type \\T1/cmtt/m/n/10.95 Oth\nerScientificTerm\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2]\n\nLaTeX Warning: Reference `tab:landscape' on page 3 undefined on input line 127.\n\n\n\nLaTeX Warning: Reference `sec:tightness' on page 3 undefined on input line 155.\n\n\n\nOverfull \\hbox (4.07755pt too wide) in paragraph at lines 155--156\n[]\\T1/cmr/m/n/10.95 On Do-cRED (Sec-tion []), we for-mally quan-tify this re-la\n-tion-ship: Spear-man $\\OML/cmm/m/it/10.95 ^^Z$\\T1/cmr/m/n/10.95 =0.52 ($\\OML/c\nmm/m/it/10.95 p <$\\T1/cmr/m/n/10.95 0.001)\n[3] [4]\n\nLaTeX Warning: Reference `sec:exp' on page 5 undefined on input line 222.\n\n\nLaTeX Warning: Reference `tab:grammar' on page 5 undefined on input line 239.\n\n\nLaTeX Warning: Reference `tab:scierc' on page 5 undefined on input line 260.\n\n[5]\n\nLaTeX Warning: Reference `tab:docred' on page 6 undefined on input line 290.\n\n\nLaTeX Warning: Reference `tab:bimodal' on page 6 undefined on input line 321.\n\n\nLaTeX Warning: Reference `sec:tightness' on page 6 undefined on input line 350.\n\n\n[6]\n\nLaTeX Warning: Reference `eq:tightness' on page 7 undefined on input line 355.\n\n\nLaTeX Warning: Reference `tab:tightness' on page 7 undefined on input line 356.\n\n\n\nOverfull \\hbox (2.20778pt too wide) in paragraph at lines 383--385\n[]\\T1/cmr/m/n/10.95 Illustrative ex-treme cases in-clude \\T1/cmtt/m/n/10.95 P6_\nhead_of_government \\T1/cmr/m/n/10.95 (tight-ness 0.889, DR 84.6%, $\\OML/cmm/m/i\nt/10.95 n$\\T1/cmr/m/n/10.95 =13)\n\nLaTeX Warning: Reference `tab:crossmodel' on page 7 undefined on input line 390\n.\n\n[7]\n\nLaTeX Warning: Reference `tab:cf' on page 8 undefined on input line 426.\n\n\nOverfull \\hbox (59.81854pt too wide) in paragraph at lines 458--461\n\\T1/cmr/m/n/10.95 (2.6%) is 3.8$\\OMS/cmsy/m/n/10.95 ^^B$ \\T1/cmr/m/n/10.95 lowe\nr than Sci-ERC CF (9.9%). Do-cRED's en-tity types (PER/ORG/LOC/TIME/NUM/MISC)\n\nOverfull \\hbox (23.8012pt too wide) in paragraph at lines 458--461\n\\T1/cmr/m/n/10.95 have far clearer se-man-tic bound-aries than Sci-ERC's (Gener\nic/OtherScientificTerm/Material/Method),\n[8]\n\nLaTeX Warning: Reference `tab:latency' on page 9 undefined on input line 469.\n\n\nOverfull \\hbox (11.6866pt too wide) in paragraph at lines 505--510\n[]\\T1/cmr/bx/n/10.95 Ontology-aware IE. \\T1/cmr/m/n/10.95 Tra-di-tional IE sys-\ntems in-cor-po-rate on-tol-ogy con-straints through training-\n\nOverfull \\hbox (4.06601pt too wide) in paragraph at lines 511--516\n\\T1/cmr/m/n/10.95 On-toCoDec's se-man-tic layer ad-dresses a dif-fer-ent con-st\nraint class---cross-field type compatibility---\n[9] [10] (./paper.aux)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0800\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0800\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0800.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.06445pt)\nFont metrics written on ecrm0800.tfm.\nOutput written on ecrm0800.600gf (256 characters, 41732 bytes).\nTranscript written on ecrm0800.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf\n Ok [100] [109] [98] [99] [108])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf\n Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]\n[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]\n[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]\n[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]\n[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]\n[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]\n[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf\n Ok [185] [178] [179] [170] [186])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf\n Ok [188] [189] [190]) ) ) )\n(some charht values had to be adjusted by as much as 0.06952pt)\nFont metrics written on tcrm1095.tfm.\nOutput written on tcrm1095.600gf (128 characters, 25592 bytes).\nTranscript written on tcrm1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1200\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1200\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx1200.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecbx1200.tfm.\nOutput written on ecbx1200.600gf (256 characters, 59220 bytes).\nTranscript written on ecbx1200.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecbx1095.tfm.\nOutput written on ecbx1095.600gf (256 characters, 54848 bytes).\nTranscript written on ecbx1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk: successfully generated.\n &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecti1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecti1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/extextit.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exileast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilig.mf\n Ok [25] [26] [27] [28] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exitalp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exillett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exidigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exiligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.06808pt)\nFont metrics written on ecti1095.tfm.\nOutput written on ecti1095.600gf (256 characters, 57920 bytes).\nTranscript written on ecti1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk: successfully generated.\n &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ectt1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ectt1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ectt1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ectt.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exmligtb.mf\n Ok) ) ) )\nFont metrics written on ectt1095.tfm.\nOutput written on ectt1095.600gf (256 characters, 47796 bytes).\nTranscript written on ectt1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk: successfully generated.\n &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/16dcf9d3-8694-4893-940b-07925e20d246/tool-results/b4oxozv8e.txt",
    "persistedOutputSize": 59457
  },
  "sourceToolAssistantUUID": "beee7ff9-00d6-49ed-ad73-b1b6e063d11a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_co…",
  "leafUuid": "819f7b55-fe3f-4beb-9fb6-bbfff56d3b8d",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete paper for dream session",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246"
}
```

---

### Tool call

_source line 28 · 2026-05-14T10:31:50.037Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VS9PBt2wixLHoaHvLhC6Ku`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper.pdf",
  "description": "Verify PDF was generated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "819f7b55-fe3f-4beb-9fb6-bbfff56d3b8d",
  "isSidechain": false,
  "requestId": "req_011Cb2Jp7i746NHtRyqbbh7J",
  "type": "assistant",
  "uuid": "4c3f430f-cd15-463c-bd65-7eaa221d04b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JewJmhribGef35ohcwLgSw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 57449,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1193,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 57449,
          "cache_creation_input_tokens": 1193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1193
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

_source line 29 · 2026-05-14T10:31:50.087Z_

<details><summary>↩ Tool result · `toolu_01VS9PBt2wixLHoaHvLhC6Ku`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 229269 May 14 10:31 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c3f430f-cd15-463c-bd65-7eaa221d04b5",
  "isSidechain": false,
  "promptId": "09bcd997-7727-4bef-8159-0d7f38bdc5f8",
  "type": "user",
  "uuid": "90bd11e2-15f8-4109-9ef8-f5527b187f6b",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 229269 May 14 10:31 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4c3f430f-cd15-463c-bd65-7eaa221d04b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-14T10:31:54.690Z_

PDF 编译成功（229KB）。论文包含 Abstract、Introduction、Background、Violation Landscape Study、OntoCoDec Framework、Experiments（7 个子节覆盖全部实验）、Related Work、Conclusion，共 8 个表格。所有定量 claim 基于 experiment_data.json 数据，无编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90bd11e2-15f8-4109-9ef8-f5527b187f6b",
  "isSidechain": false,
  "requestId": "req_011Cb2JpUWkjRQbNbum3Heyt",
  "type": "assistant",
  "uuid": "bdbad398-95c2-4db6-8125-58c2ca6b8e3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzGhxsiTAq4y2kDZ4qeLb8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 58642,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 214,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 95,
          "cache_read_input_tokens": 58642,
          "cache_creation_input_tokens": 214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 214
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T094226 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_co…",
  "leafUuid": "bdbad398-95c2-4db6-8125-58c2ca6b8e3c",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete paper for dream session",
  "sessionId": "16dcf9d3-8694-4893-940b-07925e20d246"
}
```

---
