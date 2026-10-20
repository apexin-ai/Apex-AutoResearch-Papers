# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T113743 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/98c6fb8b-38c3-4ff0-8816-78ed67c810e9.jsonl`
- **Structured JSON:** [`9006b17e3c6ff52d02e3.json`](../../sessions/90/9006b17e3c6ff52d02e3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T12:06:25.589Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T12:06:25.589Z",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T113743 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始 framing 完全成立。三条 claim 无需调整：pairwise confusability 跨 3 任务 2 模型独立预测退化， multi-channel 模型有 error taxonomy 支撑，SDGD-zero R2 修复后在 Few-NERD 和 MAVEN 上均显著优于 single-pass 和 random batching。 论文标题保持 \"analysis + method\" 双贡献定位。 Headline: \"Pairwise confusability predicts degradation (r=0.12–0.16) and SDGD yields +5.5 F1 on complex schemas.\" EMNLP Main 无需降级。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T12:06:25.592Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T12:06:25.592Z",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-15T12:06:25.613Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T113743 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始 framing 完全成立。三条 claim 无需调整：pairwise confusability 跨 3 任务 2 模型独立预测退化， multi-channel 模型有 error taxonomy 支撑，SDGD-zero R2 修复后在 Few-NERD 和 MAVEN 上均显著优于 single-pass 和 random batching。 论文标题保持 "analysis + method" 双贡献定位。 Headline: "Pairwise confusability predicts degradation (r=0.12–0.16) and SDGD yields +5.5 F1 on complex schemas." EMNLP Main 无需降级。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "cdf92f18-0400-4c4f-90e5-485ecb947e5a",
  "type": "user",
  "uuid": "7015aa13-43ba-4147-a7b6-6f00fefd3751",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T12:06:25.613Z_

```json
{
  "parentUuid": "7015aa13-43ba-4147-a7b6-6f00fefd3751",
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
  "uuid": "4f04e96c-51c8-4a1f-a8a9-682c48b548df",
  "timestamp": "2026-05-15T12:06:25.613Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T12:06:25.613Z_

```json
{
  "parentUuid": "4f04e96c-51c8-4a1f-a8a9-682c48b548df",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "edbd59c4-d097-437f-8069-ceacb75d27c1",
  "timestamp": "2026-05-15T12:06:25.613Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
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
  "aiTitle": "Generate research paper from dream experiment data",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9"
}
```

---

### Assistant

_source line 7 · 2026-05-15T12:06:30.772Z_

Let me start by reading the input files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edbd59c4-d097-437f-8069-ceacb75d27c1",
  "isSidechain": false,
  "requestId": "req_011Cb4KqjsdCcBJAxcqdXeyr",
  "type": "assistant",
  "uuid": "6f464e2b-380b-40d7-beff-e6e9b302c8e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDvHyfDEZHmdPujdT3KeiM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11214,
      "cache_read_input_tokens": 11841,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11214,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 199,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11214
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

_source line 8 · 2026-05-15T12:06:31.738Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R6rXLeWh9qih3XAFNj8GPu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f464e2b-380b-40d7-beff-e6e9b302c8e6",
  "isSidechain": false,
  "requestId": "req_011Cb4KqjsdCcBJAxcqdXeyr",
  "type": "assistant",
  "uuid": "c40a0890-b088-4462-9923-8187a9e53a1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDvHyfDEZHmdPujdT3KeiM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11214,
      "cache_read_input_tokens": 11841,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11214,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 199,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11214
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

_source line 9 · 2026-05-15T12:06:31.969Z_

<details open><summary>🔧 Tool call — Read · `toolu_0153f7UdAc4fDogeaXcJawSX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c40a0890-b088-4462-9923-8187a9e53a1c",
  "isSidechain": false,
  "requestId": "req_011Cb4KqjsdCcBJAxcqdXeyr",
  "type": "assistant",
  "uuid": "3268155e-b591-4018-bce2-4d0b0a7016df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDvHyfDEZHmdPujdT3KeiM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11214,
      "cache_read_input_tokens": 11841,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11214,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 199,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11214
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

_source line 10 · 2026-05-15T12:06:31.977Z_

<details><summary>↩ Tool result · `toolu_0153f7UdAc4fDogeaXcJawSX`</summary>

```text
1	# Paper Framing — schema-dag-extraction
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25 cycle)
5	- Commitment deadline: August 2, 2026
6	- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)
7	- Deadline: ARR May 25, 2026 (10 days from today)
8	
9	## Core Claims (3 conditions) — Revised per D012
10	
11	1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) extreme-batch accuracy gap on FewRel, (c) >=2 models.
12	
13	2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.
14	
15	3. **SDGD Effectiveness**: Confusability-aware schema decomposition (SDGD) -- partitioning types into low-confusability batches via graph coloring on the pairwise-similarity-thresholded graph -- yields significant F1 gains over single-pass and heuristic decomposition on complex schemas (>=30 types). SDGD directly leverages pairwise confusability (validated signal), avoiding per-type aggregation confounds. Evidence required: SDGD > single-pass, SDGD > random batching (same k), SDGD >= per-type splitting (with lower latency).
16	
17	## Story Spine — Revised per D012
18	
19	- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.
20	
21	- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.
22	
23	- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We operationalize pairwise confusability into SDGD, a principled framework for confusability-minimizing schema decomposition.
24	
25	- **Three-task validation**:
26	  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.156 (p<1e-11), per-type ρ=-0.293 (p=0.02), 10-28x confusion ratio
27	  - RE (FewRel, 80 relations, cross-domain): Extreme-batch accuracy gap Δ=21-50pp
28	  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)
29	
30	- **Headline result template**: "Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.12-0.16, p<1e-6), with 10-28x more type confusion errors in high-confusability batches. On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid. SDGD-zero, operating on pairwise similarity, improves F1 by X points over single-pass on Few-NERD."
31	
32	## Core Insight — Multi-Channel Degradation + Pairwise Robustness
33	
34	Schema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:
35	- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.
36	- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.
37	
38	These channels are orthogonal and independently addressable.
39	
40	**Pairwise vs Aggregated Confusability**:
41	- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.156) and MAVEN (MiniLM, r=0.120).
42	- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.
43	- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.
44	
45	## Evidence Hierarchy (D012)
46	
47	### Tier 1: PRIMARY — Pairwise SCS → Confusion
48	
49	The cleanest evidence. Directly measures: are semantically similar type pairs more often confused?
50	
51	**Few-NERD (NER)** — Qwen3 embeddings:
52	- Pearson r=0.156 (p=4.6e-12, n=1953 type pairs)
53	- Nonzero-only Spearman ρ=0.254 (p=1.1e-6)
54	- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)
55	- Immune to type frequency confound (operates at type-pair level)
56	
57	**MAVEN (ED)** — MiniLM embeddings:
58	- Pearson r=+0.120 (p≈0, n=11026 type pairs)
59	- Nonzero-only Spearman ρ=+0.191 (p<0.001)
60	- Cross-task replication on same-domain schema
61	- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas
62	
63	### Tier 2: STRONG SECONDARY — FewRel Extreme-Batch Comparison
64	
65	Large effect size, cross-task (RE), intuitive demonstration:
66	- count_4: low-BCS 91.7% vs high-BCS 70.8% (Δ=-20.9pp)
67	- count_8: low-BCS 100% vs high-BCS 50.0% (Δ=-50.0pp)
68	- count_16: low-BCS 91.7% vs high-BCS 43.1% (Δ=-48.6pp)
69	- Effect increases with count — consistent with multi-channel model
70	- MiniLM embeddings; pending: Qwen3 formal study
71	
72	### Tier 3: SUPPORTING — Few-NERD Per-type Analysis
73	
74	Bridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:
75	- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings
76	- Partial r=-0.200 (p=0.116) controlling for log-frequency
77	- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)
78	- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)
79	- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal
80	
81	### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound
82	
83	Methodological case study on when aggregated confusability measures fail:
84	- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction
85	- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation
86	- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure
87	- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)
88	- This is stronger than "domain boundary" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition
89	
90	### Tier 5: MECHANISTIC — Error Taxonomy
91	
92	Confusion rate differential demonstrates the mechanism:
93	- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS
94	- Random batches: 1.7-2.4x ratio (still significant, smaller effect)
95	- Type confusion errors increase with count AND with confusability (additive)
96	
97	## Embedding Ablation (D010)
98	
99	2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}
100	
101	### Per-type (Layer 2)
102	| | Few-NERD | FewRel | MAVEN |
103	|---|---|---|---|
104	| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |
105	| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |
106	
107	### Pairwise (Layer 1)
108	| | Few-NERD | MAVEN |
109	|---|---|---|
110	| Qwen3 | r=0.156 ✓ | r=-0.007 ✗ |
111	| MiniLM | — | r=+0.120 ✓ |
112	
113	**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.
114	
115	## Venue Fit Risks
116	
117	- **"Just an empirical study"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels "Lost in the Middle" (TACL 2024).
118	- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.
119	- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).
120	- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.
121	- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.
122	
123	## Anticipated Reviewer Concerns
124	
125	| Concern | Response Strategy | Experiment |
126	|---------|------------------|------------|
127	| Only one model | LLaMA-3.3-70B replication | exp-012 |
128	| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |
129	| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |
130	| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |
131	| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |
132	| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |
133	| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |
134	| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |
135	| Latency overhead | Report API calls and wall-clock time | exp-008 |
136	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3268155e-b591-4018-bce2-4d0b0a7016df",
  "isSidechain": false,
  "promptId": "cdf92f18-0400-4c4f-90e5-485ecb947e5a",
  "type": "user",
  "uuid": "1db502f8-683f-4615-bb26-1b9dbeba8fc6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/paper_framing.md",
      "content": "# Paper Framing — schema-dag-extraction\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\n- Commitment deadline: August 2, 2026\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\n- Deadline: ARR May 25, 2026 (10 days from today)\n\n## Core Claims (3 conditions) — Revised per D012\n\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) extreme-batch accuracy gap on FewRel, (c) >=2 models.\n\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\n\n3. **SDGD Effectiveness**: Confusability-aware schema decomposition (SDGD) -- partitioning types into low-confusability batches via graph coloring on the pairwise-similarity-thresholded graph -- yields significant F1 gains over single-pass and heuristic decomposition on complex schemas (>=30 types). SDGD directly leverages pairwise confusability (validated signal), avoiding per-type aggregation confounds. Evidence required: SDGD > single-pass, SDGD > random batching (same k), SDGD >= per-type splitting (with lower latency).\n\n## Story Spine — Revised per D012\n\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\n\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\n\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We operationalize pairwise confusability into SDGD, a principled framework for confusability-minimizing schema decomposition.\n\n- **Three-task validation**:\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.156 (p<1e-11), per-type ρ=-0.293 (p=0.02), 10-28x confusion ratio\n  - RE (FewRel, 80 relations, cross-domain): Extreme-batch accuracy gap Δ=21-50pp\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\n\n- **Headline result template**: \"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.12-0.16, p<1e-6), with 10-28x more type confusion errors in high-confusability batches. On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid. SDGD-zero, operating on pairwise similarity, improves F1 by X points over single-pass on Few-NERD.\"\n\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\n\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\n\nThese channels are orthogonal and independently addressable.\n\n**Pairwise vs Aggregated Confusability**:\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.156) and MAVEN (MiniLM, r=0.120).\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\n\n## Evidence Hierarchy (D012)\n\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\n\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\n\n**Few-NERD (NER)** — Qwen3 embeddings:\n- Pearson r=0.156 (p=4.6e-12, n=1953 type pairs)\n- Nonzero-only Spearman ρ=0.254 (p=1.1e-6)\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\n- Immune to type frequency confound (operates at type-pair level)\n\n**MAVEN (ED)** — MiniLM embeddings:\n- Pearson r=+0.120 (p≈0, n=11026 type pairs)\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\n- Cross-task replication on same-domain schema\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\n\n### Tier 2: STRONG SECONDARY — FewRel Extreme-Batch Comparison\n\nLarge effect size, cross-task (RE), intuitive demonstration:\n- count_4: low-BCS 91.7% vs high-BCS 70.8% (Δ=-20.9pp)\n- count_8: low-BCS 100% vs high-BCS 50.0% (Δ=-50.0pp)\n- count_16: low-BCS 91.7% vs high-BCS 43.1% (Δ=-48.6pp)\n- Effect increases with count — consistent with multi-channel model\n- MiniLM embeddings; pending: Qwen3 formal study\n\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\n\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\n\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\n\nMethodological case study on when aggregated confusability measures fail:\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\n- This is stronger than \"domain boundary\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\n\n### Tier 5: MECHANISTIC — Error Taxonomy\n\nConfusion rate differential demonstrates the mechanism:\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\n- Type confusion errors increase with count AND with confusability (additive)\n\n## Embedding Ablation (D010)\n\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\n\n### Per-type (Layer 2)\n| | Few-NERD | FewRel | MAVEN |\n|---|---|---|---|\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\n\n### Pairwise (Layer 1)\n| | Few-NERD | MAVEN |\n|---|---|---|\n| Qwen3 | r=0.156 ✓ | r=-0.007 ✗ |\n| MiniLM | — | r=+0.120 ✓ |\n\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \"Lost in the Middle\" (TACL 2024).\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response Strategy | Experiment |\n|---------|------------------|------------|\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\n",
      "numLines": 136,
      "startLine": 1,
      "totalLines": 136
    }
  },
  "sourceToolAssistantUUID": "3268155e-b591-4018-bce2-4d0b0a7016df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T12:06:32.039Z_

<details><summary>↩ Tool result · `toolu_01R6rXLeWh9qih3XAFNj8GPu`</summary>

```text
1	[
2	  {
3	    "name": "MAVEN Confusability Study (full)",
4	    "description": "在 MAVEN 168 event types 上运行 v2 prompt，500 sample，完成 count curve、 batch-level BCS 对照、pairwise SCS→confusion 相关、per-type 分析及 centrality confound 量化。\n",
5	    "results": {
6	      "count_curve_relaxed_f1": {
7	        "count_1": 0.118,
8	        "count_6": 0.142,
9	        "count_12": 0.178,
10	        "count_22": 0.21,
11	        "count_44": 0.248,
12	        "count_64": 0.261,
13	        "count_168": 0.272
14	      },
15	      "count_curve_exact_f1": {
16	        "count_1": 0.011,
17	        "count_6": 0.005,
18	        "count_12": 0.01,
19	        "count_22": 0.015,
20	        "count_44": 0.02,
21	        "count_64": 0.016,
22	        "count_168": 0.014
23	      },
24	      "pairwise_miniLM": {
25	        "n_pairs": 14028,
26	        "pearson_r": 0.12,
27	        "pearson_p": 1.2e-45,
28	        "spearman_rho": 0.135,
29	        "spearman_p": 3.8e-58,
30	        "nonzero_spearman_rho": 0.191,
31	        "nonzero_spearman_p": 0.00047
32	      },
33	      "pairwise_qwen3": {
34	        "pearson_r": -0.007,
35	        "pearson_p": 0.41,
36	        "verdict": "NOT_SIGNIFICANT — Qwen3 embeddings 无法在同质 schema 上捕获 pairwise signal"
37	      },
38	      "per_type_miniLM": {
39	        "n_types": 148,
40	        "filter": "freq>=10",
41	        "spearman_rho": 0.208,
42	        "spearman_p": 0.011,
43	        "direction": "positive",
44	        "verdict": "CENTRALITY CONFOUND — 方向与假设相反"
45	      },
46	      "per_type_qwen3": {
47	        "spearman_rho": 0.189,
48	        "spearman_p": 0.021,
49	        "direction": "positive",
50	        "verdict": "CENTRALITY CONFOUND — 两种 embedding 方向一致，排除 embedding 压缩假说"
51	      },
52	      "centrality_analysis": {
53	        "mean_bcs_vs_type_frequency_r": 0.34,
54	        "mean_bcs_vs_type_frequency_p": 2.1e-05,
55	        "interpretation": "高 mean BCS = 语义中心类型 = 高频/LLM 更熟悉 = 更高 F1"
56	      },
57	      "batch_level_extreme": {
58	        "count_6_high_bcs_relaxed_f1": 0.218,
59	        "count_6_low_bcs_relaxed_f1": 0.098,
60	        "count_12_high_bcs_relaxed_f1": 0.192,
61	        "count_12_low_bcs_relaxed_f1": 0.114,
62	        "confusion_rate_ratio_extreme_count6": 8.2,
63	        "confusion_rate_ratio_extreme_count12": 6.5
64	      }
65	    },
66	    "tables": [
67	      {
68	        "title": "MAVEN Count Curve (v2 prompt, 500 samples)",
69	        "columns": [
70	          "count",
71	          "relaxed_F1",
72	          "exact_F1",
73	          "recall",
74	          "precision",
75	          "pred_gold_ratio"
76	        ],
77	        "rows": [
78	          [
79	            1,
80	            0.118,
81	            0.011,
82	            0.21,
83	            0.082,
84	            2.56
85	          ],
86	          [
87	            6,
88	            0.142,
89	            0.005,
90	            0.185,
91	            0.115,
92	            1.61
93	          ],
94	          [
95	            12,
96	            0.178,
97	            0.01,
98	            0.21,
99	            0.154,
100	            1.36
101	          ],
102	          [
103	            22,
104	            0.21,
105	            0.015,
106	            0.238,
107	            0.188,
108	            1.27
109	          ],
110	          [
111	            44,
112	            0.248,
113	            0.02,
114	            0.268,
115	            0.231,
116	            1.16
117	          ],
118	          [
119	            64,
120	            0.261,
121	            0.016,
122	            0.275,
123	            0.249,
124	            1.1
125	          ]
126	        ]
127	      },
128	      {
129	        "title": "MAVEN Pairwise SCS → Confusion (2×2 embedding comparison)",
130	        "columns": [
131	          "embedding",
132	          "pearson_r",
133	          "p-value",
134	          "n_pairs",
135	          "verdict"
136	        ],
137	        "rows": [
138	          [
139	            "MiniLM",
140	            0.12,
141	            "1.2e-45",
142	            14028,
143	            "PASS"
144	          ],
145	          [
146	            "Qwen3",
147	            -0.007,
148	            0.41,
149	            14028,
150	            "FAIL"
151	          ]
152	        ]
153	      },
154	      {
155	        "title": "MAVEN Per-type BCS → F1 (centrality confound)",
156	        "columns": [
157	          "embedding",
158	          "spearman_ρ",
159	          "p-value",
160	          "direction",
161	          "verdict"
162	        ],
163	        "rows": [
164	          [
165	            "MiniLM",
166	            0.208,
167	            0.011,
168	            "positive",
169	            "CONFOUND"
170	          ],
171	          [
172	            "Qwen3",
173	            0.189,
174	            0.021,
175	            "positive",
176	            "CONFOUND"
177	          ]
178	        ]
179	      }
180	    ],
181	    "figures": [],
182	    "analysis": "MAVEN 结果完美支持论文的两层叙事：（1）pairwise confusability 在第三个任务（ED）上独立复现， 跨 NER→RE→ED 三任务验证 Claim 1；（2）per-type centrality confound 是方法论贡献—— 解释了为什么简单的 per-type 聚合（如直接用 mean BCS 排序类型）在同质 schema 上失效， 而 pairwise 分析和 SDGD 的 pairwise 操作策略绕过了这个问题。 Exact F1 极低（<0.02）是 event trigger 边界匹配问题，不影响 confusability 分析（使用 relaxed F1）。\n\n\nMAVEN 168 个 event types 来自同一语义域（FrameNet 层级结构），SCS 分布高度集中 （mean=0.216, std=0.103），不像 Few-NERD 有跨域分离。 Pairwise MiniLM 信号成立（r=0.120）因为 MiniLM 的通用语义空间在细粒度事件类型间保留了足够区分度， 而 Qwen3 指令调优后的表征空间过度压缩了语义邻近类型。 Per-type 正方向是 centrality confound 的典型表现：在同质 schema 中， mean BCS 高的类型恰好是语义网络的中心节点（如 \"Attack\", \"Meeting\"）， 这些类型在训练语料中高频出现，LLM 先验知识更强，F1 自然更高。 这不是假设失败，而是方法论贡献——揭示了 per-type 聚合何时失效。 Batch-level 极端组对照仍然显示 high-BCS 组更高（与 Few-NERD 方向相同）， 因为极端组构造直接操作 batch 内相似度，绕过了 centrality confound。\n"
183	  },
184	  {
185	    "name": "DocRED Confusability Study",
186	    "description": "在 DocRED 96 关系类型上进行 count curve + pairwise SCS→confusion 分析。 文档级 RE 任务，更长的上下文，测试 confusability 信号在复杂推理场景下的鲁棒性。\n",
187	    "results": {
188	      "count_curve_f1": {
189	        "count_1": 0.195,
190	        "count_6": 0.168,
191	        "count_12": 0.152,
192	        "count_24": 0.131,
193	        "count_48": 0.118,
194	        "count_96": 0.098
195	      },
196	      "pairwise_miniLM": {
197	        "n_pairs": 4560,
198	        "pearson_r": 0.108,
199	        "pearson_p": 3.5e-13,
200	        "spearman_rho": 0.122,
201	        "spearman_p": 1.8e-16
202	      },
203	      "per_type_qwen3": {
204	        "n_types": 82,
205	        "filter": "freq>=5",
206	        "spearman_rho": -0.231,
207	        "spearman_p": 0.037
208	      },
209	      "extreme_batch_comparison": {
210	        "count_12_high_bcs_f1": 0.105,
211	        "count_12_low_bcs_f1": 0.188,
212	        "delta_pp": -8.3,
213	        "confusion_rate_ratio": 5.8
214	      }
215	    },
216	    "tables": [
217	      {
218	        "title": "DocRED Pairwise Comparison Across Embeddings",
219	        "columns": [
220	          "embedding",
221	          "pearson_r",
222	          "p-value",
223	          "verdict"
224	        ],
225	        "rows": [
226	          [
227	            "MiniLM",
228	            0.108,
229	            "3.5e-13",
230	            "PASS"
231	          ],
232	          [
233	            "Qwen3",
234	            0.095,
235	            "2.1e-10",
236	            "PASS"
237	          ]
238	        ]
239	      }
240	    ],
241	    "figures": [],
242	    "analysis": "DocRED 作为第四个任务验证了 pairwise confusability 信号的跨任务泛化性。 效应量较小但 n_pairs 足够保证统计显著。文档级上下文的缓冲效应是合理的—— 更长的文档为模型提供了更多消歧证据。这一结果支持在论文中加入 DocRED 作为 supplementary evidence，但不改变三任务核心叙事。\n\n\nDocRED 关系类型语义分布介于 Few-NERD（跨域）和 MAVEN（同域）之间—— 96 个关系覆盖多个领域但部分关系高度相似（如 \"place of birth\" vs \"place of death\"）。 Pairwise 信号成立但效应略弱于 Few-NERD（r=0.108 vs 0.156），因为文档级 RE 中 更长的上下文提供了更多消歧信息，部分缓解了 confusability 效应。 Per-type 方向正确（负相关），因为 DocRED 跨域程度足够避免 MAVEN 的 centrality confound。 Extreme batch delta 较小（8.3pp vs Few-NERD 的 20-50pp），同样因为文档级上下文的缓冲效应。\n"
243	  },
244	  {
245	    "name": "Count × Confusability Interaction (2×2)",
246	    "description": "在 Few-NERD 上构造 {低 count=6, 高 count=22} × {低 BCS, 高 BCS} 四组， 每组 10 batches，测试 count 和 confusability 的加法/乘法交互效应。\n",
247	    "results": {
248	      "factorial_f1": {
249	        "low_count_low_bcs": 0.372,
250	        "low_count_high_bcs": 0.268,
251	        "high_count_low_bcs": 0.312,
252	        "high_count_high_bcs": 0.178
253	      },
254	      "factorial_recall": {
255	        "low_count_low_bcs": 0.468,
256	        "low_count_high_bcs": 0.415,
257	        "high_count_low_bcs": 0.33,
258	        "high_count_high_bcs": 0.265
259	      },
260	      "factorial_type_confusion_rate": {
261	        "low_count_low_bcs": 0.008,
262	        "low_count_high_bcs": 0.045,
263	        "high_count_low_bcs": 0.018,
264	        "high_count_high_bcs": 0.072
265	      },
266	      "two_way_anova": {
267	        "count_main_effect_F": 14.2,
268	        "count_main_effect_p": 0.0006,
269	        "bcs_main_effect_F": 22.8,
270	        "bcs_main_effect_p": 3.1e-05,
271	        "interaction_F": 3.1,
272	        "interaction_p": 0.087,
273	        "interaction_verdict": "边际显著，轻微超加性"
274	      },
275	      "effect_decomposition": {
276	        "count_delta_f1": -0.075,
277	        "bcs_delta_f1": -0.119,
278	        "interaction_delta_f1": -0.027,
279	        "additive_prediction_high_high": 0.197,
280	        "actual_high_high": 0.178,
281	        "super_additive_gap": -0.019
282	      }
283	    },
284	    "tables": [
285	      {
286	        "title": "2×2 Factorial F1 Results",
287	        "columns": [
288	          "",
289	          "Low BCS",
290	          "High BCS",
291	          "BCS effect"
292	        ],
293	        "rows": [
294	          [
295	            "Low count (6)",
296	            0.372,
297	            0.268,
298	            "-0.104"
299	          ],
300	          [
301	            "High count (22)",
302	            0.312,
303	            0.178,
304	            "-0.134"
305	          ],
306	          [
307	            "Count effect",
308	            "-0.060",
309	            "-0.090",
310	            "interaction: -0.027"
311	          ]
312	        ]
313	      },
314	      {
315	        "title": "2×2 Type Confusion Rate",
316	        "columns": [
317	          "",
318	          "Low BCS",
319	          "High BCS",
320	          "ratio"
321	        ],
322	        "rows": [
323	          [
324	            "Low count (6)",
325	            0.008,
326	            0.045,
327	            "5.6x"
328	          ],
329	          [
330	            "High count (22)",
331	            0.018,
332	            0.072,
333	            "4.0x"
334	          ]
335	        ]
336	      }
337	    ],
338	    "figures": [],
339	    "analysis": "2×2 结果核心支持 multi-channel 正交模型。BCS 主效应（F=22.8）大于 count 主效应（F=14.2）， 说明在 Few-NERD 上 confusability 是更强的降级因子。交互效应 p=0.087 表明实质上加法模型足够， 轻微超加性可在论文中讨论但不改变核心叙事。这一结果直接支持 SDGD 的设计原理： 单独优化 batch 内 confusability（而非同时优化 count）已经足够捕获大部分可分解的性能损失。\n\n\nCount 和 confusability 通过不同机制降低性能：count 稀释 attention → recall 下降， confusability 引起类型混淆 → precision 下降。两者理论上正交，但在 high-count high-BCS 条件下 存在轻微超加性——当 attention 已被稀释时，模型对类型区分的余量更小，confusability 的边际伤害更大。 交互效应统计上边际显著（p=0.087），不足以拒绝加法模型，这恰好支持论文的\"正交通道\"叙事： 两个通道基本独立，各自可寻址。超加性的微弱存在（1.9pp gap）在讨论中作为 nuance 提及。\n"
340	  },
341	  {
342	    "name": "Systematic Error Taxonomy",
343	    "description": "在 exp-002 数据上系统分类 FP 错误为四类：type_substitution、boundary_error、 false_negative、hallucination，按 BCS quartile 分 bin 统计分布。\n",
344	    "results": {
345	      "error_distribution_by_bcs_quartile": {
346	        "Q1_low_bcs": {
347	          "type_substitution_pct": 6.2,
348	          "boundary_error_pct": 14.8,
349	          "false_negative_pct": 58.3,
350	          "hallucination_pct": 20.7,
351	          "total_errors": 385
352	        },
353	        "Q2": {
354	          "type_substitution_pct": 12.5,
355	          "boundary_error_pct": 13.2,
356	          "false_negative_pct": 51.8,
357	          "hallucination_pct": 22.5,
358	          "total_errors": 412
359	        },
360	        "Q3": {
361	          "type_substitution_pct": 22.1,
362	          "boundary_error_pct": 11.9,
363	          "false_negative_pct": 44.6,
364	          "hallucination_pct": 21.4,
365	          "total_errors": 448
366	        },
367	        "Q4_high_bcs": {
368	          "type_substitution_pct": 38.4,
369	          "boundary_error_pct": 10.5,
370	          "false_negative_pct": 32.3,
371	          "hallucination_pct": 18.8,
372	          "total_errors": 521
373	        }
374	      },
375	      "monotonic_trends": {
376	        "type_substitution_vs_bcs": "单调递增 6.2→38.4%，Kendall τ=0.92",
377	        "false_negative_vs_bcs": "单调递减 58.3→32.3%，Kendall τ=-0.88",
378	        "boundary_error_vs_bcs": "微弱递减 14.8→10.5%，不显著",
379	        "hallucination_vs_bcs": "无趋势 20.7→18.8%，Kendall τ=-0.21"
380	      },
381	      "by_count_level": {
382	        "count_6": {
383	          "Q1_type_sub_pct": 4.8,
384	          "Q4_type_sub_pct": 31.2,
385	          "Q1_fn_pct": 61.5,
386	          "Q4_fn_pct": 38.1
387	        },
388	        "count_12": {
389	          "Q1_type_sub_pct": 7.9,
390	          "Q4_type_sub_pct": 44.7,
391	          "Q1_fn_pct": 54.2,
392	          "Q4_fn_pct": 27.8
393	        }
394	      },
395	      "chi_squared_bcs_vs_error_type": {
396	        "statistic": 89.4,
397	        "p": 1.2e-16,
398	        "df": 9
399	      }
400	    },
401	    "tables": [
402	      {
403	        "title": "Error Type Distribution by BCS Quartile (%)",
404	        "columns": [
405	          "BCS quartile",
406	          "Type sub.",
407	          "Boundary",
408	          "False neg.",
409	          "Halluc.",
410	          "Total"
411	        ],
412	        "rows": [
413	          [
414	            "Q1 (low)",
415	            6.2,
416	            14.8,
417	            58.3,
418	            20.7,
419	            385
420	          ],
421	          [
422	            "Q2",
423	            12.5,
424	            13.2,
425	            51.8,
426	            22.5,
427	            412
428	          ],
429	          [
430	            "Q3",
431	            22.1,
432	            11.9,
433	            44.6,
434	            21.4,
435	            448
436	          ],
437	          [
438	            "Q4 (high)",
439	            38.4,
440	            10.5,
441	            32.3,
442	            18.8,
443	            521
444	          ]
445	        ]
446	      }
447	    ],
448	    "figures": [],
449	    "analysis": "Error taxonomy 是 Claim 2（multi-channel degradation）最直接的机械证据。 Type substitution 从 Q1 的 6.2% 飙升到 Q4 的 38.4%（6.2x），而 false negative 反向变化， hallucination 稳定。这精确对应 multi-channel 模型的预测：confusability 通道选择性地增加 类型混淆错误，而非所有类型错误。count_12 条件下效应更强（Q4 type_sub=44.7%）， 因为更多类型在 prompt 中同时出现时，confusability 的累积效应更大。 Chi-squared 高度显著（p=1.2e-16）确认 BCS quartile 与错误类型分布非独立。\n\n\nType substitution 与 BCS 强单调递增是 Claim 2 的核心机械证据：高 confusability batch 中， 模型正确识别了 entity span 但将其标注为语义邻近的错误类型。这是 confusability 通道的签名错误。 False negative 与 BCS 递减是因为在高 BCS batch 中，模型更倾向于\"猜错类型\"而非\"完全遗漏\"—— 当多个相似类型在 prompt 中共现时，模型被激活去标注更多 span，但标注质量下降。 Hallucination 和 boundary error 与 BCS 无关，因为它们由其他因素驱动（幻觉=模型先验偏差， 边界=tokenization/span 识别问题），与类型相似度正交。 这一分解证实了 multi-channel 模型：count→omission(FN)，confusability→substitution。\n"
450	  },
451	  {
452	    "name": "SDGD-zero Few-NERD (R2 revision)",
453	    "description": "SDGD-zero R2：修复 R1 的阈值和合并策略问题。基于 Qwen3 embedding pairwise SCS， 构建 confusability graph（阈值 τ=0.82），图着色分组，每组独立推理后合并。 对比 single-pass full-schema baseline。\n",
454	    "results": {
455	      "r2_fixes": {
456	        "threshold": "τ=0.82 (R1 used 0.90, too aggressive → batches still confusable)",
457	        "merge_strategy": "span-level confidence dedup with type priority (R1 used naive union → duplicate spans)",
458	        "batch_config": "8 batches, avg 8.25 types/batch (range: 6-11)"
459	      },
460	      "sdgd_zero_results": {
461	        "f1": 0.469,
462	        "precision": 0.548,
463	        "recall": 0.41,
464	        "n_api_calls": 8,
465	        "wall_clock_minutes": 12.5
466	      },
467	      "single_pass_baseline": {
468	        "f1": 0.414,
469	        "precision": 0.648,
470	        "recall": 0.304,
471	        "n_api_calls": 1,
472	        "wall_clock_minutes": 2.8
473	      },
474	      "delta_vs_singlepass": {
475	        "delta_f1_pp": 5.5,
476	        "delta_recall_pp": 10.6,
477	        "delta_precision_pp": -10.0,
478	        "f1_p_value": 0.003,
479	        "verdict": "PASS — F1 显著提升，recall 大幅改善，precision 可控下降"
480	      },
481	      "per_batch_analysis": {
482	        "mean_batch_bcs": 0.762,
483	        "max_batch_bcs": 0.801,
484	        "min_batch_bcs": 0.718,
485	        "singlepass_bcs": 0.847,
486	        "bcs_reduction_pct": 10.0
487	      },
488	      "batch_level_breakdown": {
489	        "batch_1": {
490	          "n_types": 8,
491	          "bcs": 0.738,
492	          "f1": 0.385
493	        },
494	        "batch_2": {
495	          "n_types": 9,
496	          "bcs": 0.762,
497	          "f1": 0.352
498	        },
499	        "batch_3": {
500	          "n_types": 7,
501	          "bcs": 0.721,
502	          "f1": 0.401
503	        },
504	        "batch_4": {
505	          "n_types": 11,
506	          "bcs": 0.801,
507	          "f1": 0.312
508	        },
509	        "batch_5": {
510	          "n_types": 8,
511	          "bcs": 0.745,
512	          "f1": 0.378
513	        },
514	        "batch_6": {
515	          "n_types": 9,
516	          "bcs": 0.773,
517	          "f1": 0.345
518	        },
519	        "batch_7": {
520	          "n_types": 8,
521	          "bcs": 0.752,
522	          "f1": 0.368
523	        },
524	        "batch_8": {
525	          "n_types": 6,
526	          "bcs": 0.718,
527	          "f1": 0.415
528	        }
529	      },
530	      "type_confusion_rate": {
531	        "sdgd_zero": 0.021,
532	        "single_pass": 0.038,
533	        "reduction_pct": 44.7
534	      }
535	    },
536	    "tables": [
537	      {
538	        "title": "SDGD-zero R2 vs Single-pass on Few-NERD (66 types)",
539	        "columns": [
540	          "Method",
541	          "F1",
542	          "Precision",
543	          "Recall",
544	          "API calls",
545	          "Wall-clock (min)"
546	        ],
547	        "rows": [
548	          [
549	            "Single-pass",
550	            0.414,
551	            0.648,
552	            0.304,
553	            1,
554	            2.8
555	          ],
556	          [
557	            "SDGD-zero R2",
558	            0.469,
559	            0.548,
560	            0.41,
561	            8,
562	            12.5
563	          ],
564	          [
565	            "Δ",
566	            "+5.5pp",
567	            "-10.0pp",
568	            "+10.6pp",
569	            "+7",
570	            "+9.7"
571	          ]
572	        ]
573	      }
574	    ],
575	    "figures": [],
576	    "analysis": "SDGD-zero R2 的成功直接验证了 Claim 3：confusability-aware 分组本身有价值。 +5.5 F1 pp 中，约 2.2pp 来自 count reduction（见 exp-013），3.3pp 来自 confusability-aware grouping。 Per-batch 分析显示 batch 4（BCS=0.801, F1=0.312）vs batch 8（BCS=0.718, F1=0.415） 的对比直接体现了 SDGD 的内部一致性——即使在 SDGD 的优化分组内， 残余 confusability 差异仍然预测性能差异。 Type confusion rate 下降 44.7% 是机械证据：SDGD 通过分离 confusable pair 直接减少了 Channel 2 错误。\n\n\nR1 失败的根因是两个实现问题：（1）SCS 阈值 τ=0.90 过高，导致 confusability graph 过于稀疏， 图着色产生的分组仍包含大量高相似度对（0.82-0.90 范围被遗漏）； （2）naive union merge 在多个 batch 对同一 span 产生不同类型标注时直接取并集， 引入大量重复和矛盾预测。R2 将 τ 降至 0.82（基于 Few-NERD pairwise SCS 分布的 P90）， 确保 top-10% 相似度对被强制分离；merge 策略改为 span-level confidence dedup， 当多个 batch 对同一 text span 产生不同类型时取置信度最高者。 F1 从 0.414 提升至 0.469（+5.5pp）主要来自 recall 改善（+10.6pp）： 较小的 batch（8 types vs 66 types）显著减少了 attention dilution，模型遗漏更少的 entity。 Precision 下降（-10.0pp）因为 8 个 batch 的合并引入了少量 spurious predictions， 但 confidence-based merge 将其控制在可接受范围。 净 F1 收益 +5.5pp 在 [3, 8] 范围中部，合理反映了 zero-shot 图着色方法的局限—— embedding 相似度只是 empirical confusability 的代理，最优分组需要 calibration data（→ exp-010）。\n"
577	  },
578	  {
579	    "name": "SDGD-zero MAVEN",
580	    "description": "SDGD-zero 在 MAVEN 168 event types 上的 cross-task 验证。 基于 MiniLM embedding（MAVEN 上有效的 pairwise proxy），graph coloring 分组。\n",
581	    "results": {
582	      "sdgd_zero_results": {
583	        "relaxed_f1": 0.305,
584	        "exact_f1": 0.022,
585	        "n_batches": 14,
586	        "avg_types_per_batch": 12.0,
587	        "n_api_calls": 14,
588	        "wall_clock_minutes": 22.4
589	      },
590	      "single_pass_baseline": {
591	        "relaxed_f1": 0.272,
592	        "exact_f1": 0.014,
593	        "n_api_calls": 1,
594	        "wall_clock_minutes": 4.2
595	      },
596	      "random_batching_baseline": {
597	        "relaxed_f1": 0.282,
598	        "n_api_calls": 14
599	      },
600	      "delta_vs_singlepass": {
601	        "delta_relaxed_f1_pp": 3.3,
602	        "p_value": 0.012
603	      },
604	      "delta_vs_random": {
605	        "delta_relaxed_f1_pp": 2.3,
606	        "p_value": 0.038
607	      },
608	      "type_confusion_reduction": {
609	        "sdgd_zero_rate": 0.035,
610	        "single_pass_rate": 0.058,
611	        "reduction_pct": 39.7
612	      }
613	    },
614	    "tables": [
615	      {
616	        "title": "SDGD-zero on MAVEN (168 types, MiniLM embedding)",
617	        "columns": [
618	          "Method",
619	          "Relaxed F1",
620	          "Exact F1",
621	          "API calls",
622	          "Δ relaxed F1"
623	        ],
624	        "rows": [
625	          [
626	            "Single-pass (168 types)",
627	            0.272,
628	            0.014,
629	            1,
630	            "—"
631	          ],
632	          [
633	            "Random batching (k=14)",
634	            0.282,
635	            0.017,
636	            14,
637	            "+1.0pp"
638	          ],
639	          [
640	            "SDGD-zero (k=14)",
641	            0.305,
642	            0.022,
643	            14,
644	            "+3.3pp"
645	          ]
646	        ]
647	      }
648	    ],
649	    "figures": [],
650	    "analysis": "MAVEN 上的正向结果完成 SDGD 的 cross-task 验证（NER + ED）， 证明 confusability-aware 分组在不同任务和 schema 特征下均有效。 效应量较小但仍然显著（p=0.012 vs single-pass），足以支持 Claim 3。 值得注意的是 embedding 选择的重要性——在 MAVEN 上使用 Qwen3 embedding 的 SDGD 可能无效（因为 Qwen3 pairwise 信号不显著），这强化了论文中\"task-appropriate embedding\"的建议。\n\n\nMAVEN 上 SDGD 收益（+3.3pp relaxed F1）小于 Few-NERD（+5.5pp），原因有二： （1）MAVEN 的 SCS 分布更集中（mean=0.216, std=0.103），图着色的\"分离空间\"更小， 无法像 Few-NERD 那样找到明确的低相似度分组； （2）MAVEN F1 与 count 正相关（exp-004），batch 缩小到 12 types 会损失部分 count-context 效益， 部分抵消了 confusability reduction 的收益。 使用 MiniLM 而非 Qwen3 是正确选择，因为 MiniLM pairwise 信号在 MAVEN 上有效（r=0.120）而 Qwen3 无效。 vs random 的 +2.3pp 确认 confusability-aware 分组在同质 schema 上仍然有价值， 尽管收益小于跨域 schema。\n"
651	  },
652	  {
653	    "name": "SDGD-cal Few-NERD",
654	    "description": "SDGD-cal：使用 5-10 calibration examples 构建经验 confusion matrix， 替代 embedding SCS 作为 confusability proxy，再用 graph coloring 分组。 对比 SDGD-zero。\n",
655	    "results": {
656	      "calibration_cost": {
657	        "n_calibration_examples": 8,
658	        "n_calibration_api_calls": 8,
659	        "calibration_wall_clock_minutes": 4.5
660	      },
661	      "sdgd_cal_results": {
662	        "f1": 0.488,
663	        "precision": 0.556,
664	        "recall": 0.435,
665	        "n_api_calls": 9,
666	        "wall_clock_minutes": 14.2,
667	        "total_api_calls_incl_calibration": 17
668	      },
669	      "sdgd_zero_comparison": {
670	        "sdgd_zero_f1": 0.469,
671	        "delta_f1_pp": 1.9,
672	        "p_value": 0.042
673	      },
674	      "calibration_vs_embedding_correlation": {
675	        "empirical_vs_qwen3_scs_spearman": 0.58,
676	        "empirical_vs_miniLM_scs_spearman": 0.43,
677	        "verdict": "经验 confusability 与 embedding proxy 中等相关，但经验版更准确"
678	      },
679	      "confusion_matrix_properties": {
680	        "n_nonzero_pairs": 312,
681	        "n_total_pairs": 2145,
682	        "sparsity": 0.854,
683	        "top_empirical_pair": "person-other ↔ person-politician (confusion=23/8 examples)",
684	        "top_embedding_pair": "same pair (BCS=0.934)",
685	        "agreement_top_20": "85% overlap",
686	        "disagreement_examples": "building-library ↔ building-theater (high SCS=0.91, low empirical=0)"
687	      }
688	    },
689	    "tables": [
690	      {
691	        "title": "SDGD Variant Comparison on Few-NERD",
692	        "columns": [
693	          "Method",
694	          "F1",
695	          "P",
696	          "R",
697	          "API calls (total)",
698	          "Δ F1 vs single-pass"
699	        ],
700	        "rows": [
701	          [
702	            "Single-pass",
703	            0.414,
704	            0.648,
705	            0.304,
706	            1,
707	            "—"
708	          ],
709	          [
710	            "SDGD-zero",
711	            0.469,
712	            0.548,
713	            0.41,
714	            8,
715	            "+5.5pp"
716	          ],
717	          [
718	            "SDGD-cal",
719	            0.488,
720	            0.556,
721	            0.435,
722	            17,
723	            "+7.4pp"
724	          ]
725	        ]
726	      }
727	    ],
728	    "figures": [],
729	    "analysis": "SDGD-cal 的 +1.9pp 增量验证了 SDGD 框架的可扩展性——更好的 confusability 估计 直接转化为更好的分组和更高的 F1。这也为 SDGD-zero 的实用性提供了参照： 在无 calibration data 的冷启动场景下，SDGD-zero 已能获得大部分收益（5.5/7.4 = 74%）， calibration 的边际收益递减。论文中 SDGD-zero 作为默认推荐，SDGD-cal 作为高精度选项。\n\n\nSDGD-cal 比 SDGD-zero 高 1.9 F1 pp，因为经验 confusion matrix 直接捕获了 LLM 的实际混淆模式，而 embedding SCS 只是语义相似度的代理。 两者差距不大（1.9pp）因为 embedding proxy 已经相当好——top-20 confusable pairs 有 85% 重叠。 差异主要来自 edge cases：某些 embedding 上高相似但 LLM 实际不混淆的 pair （如 building-library ↔ building-theater，LLM 依靠上下文线索有效区分）， 以及 embedding 上不相似但 LLM 实际混淆的 pair（可能由于 training data 偏差）。 Calibration 的额外成本（8 API calls）使总 API calls 从 8 增至 17， 但仍远低于 per-type splitting（66 calls），且 F1 接近 per-type 水平。\n"
730	  },
731	  {
732	    "name": "SDGD-cal MAVEN",
733	    "description": "SDGD-cal 在 MAVEN 168 types 上的完整对比。 使用 MiniLM embedding 和 10 calibration examples。\n",
734	    "results": {
735	      "sdgd_cal_results": {
736	        "relaxed_f1": 0.318,
737	        "exact_f1": 0.025,
738	        "n_api_calls": 14,
739	        "total_api_calls_incl_calibration": 24
740	      },
741	      "full_comparison_table": {
742	        "single_pass": {
743	          "relaxed_f1": 0.272,
744	          "api_calls": 1
745	        },
746	        "random_k14": {
747	          "relaxed_f1": 0.282,
748	          "api_calls": 14
749	        },
750	        "sdgd_zero_miniLM": {
751	          "relaxed_f1": 0.305,
752	          "api_calls": 14
753	        },
754	        "sdgd_cal": {
755	          "relaxed_f1": 0.318,
756	          "api_calls": 24
757	        },
758	        "per_type": {
759	          "relaxed_f1": 0.325,
760	          "api_calls": 168
761	        }
762	      },
763	      "delta_sdgd_cal_vs_zero": "+1.3pp",
764	      "delta_sdgd_cal_vs_singlepass": "+4.6pp",
765	      "calibration_improvement_on_maven": {
766	        "empirical_vs_miniLM_spearman": 0.49,
767	        "verdict": "经验混淆信号在同质 schema 上增量更大，因为 embedding 信号更弱（MiniLM r=0.120）"
768	      }
769	    },
770	    "tables": [
771	      {
772	        "title": "Full Comparison Table: MAVEN (168 types)",
773	        "columns": [
774	          "Method",
775	          "Relaxed F1",
776	          "API calls",
777	          "Δ vs single-pass",
778	          "Latency ratio"
779	        ],
780	        "rows": [
781	          [
782	            "Single-pass",
783	            0.272,
784	            1,
785	            "—",
786	            "1.0x"
787	          ],
788	          [
789	            "Random (k=14)",
790	            0.282,
791	            14,
792	            "+1.0pp",
793	            "5.3x"
794	          ],
795	          [
796	            "SDGD-zero (MiniLM)",
797	            0.305,
798	            14,
799	            "+3.3pp",
800	            "5.3x"
801	          ],
802	          [
803	            "SDGD-cal",
804	            0.318,
805	            24,
806	            "+4.6pp",
807	            "8.5x"
808	          ],
809	          [
810	            "Per-type (k=168)",
811	            0.325,
812	            168,
813	            "+5.3pp",
814	            "40.0x"
815	          ]
816	        ]
817	      }
818	    ],
819	    "figures": [],
820	    "analysis": "MAVEN 完整对比表是论文 Table 3（或 4）的核心内容。SDGD-cal 在 Pareto 前沿上 明确优于 random 和 single-pass，接近 per-type 但成本大幅降低。 这完成了 Claim 3 的全部证据链：confusability-aware 分组在两个任务上均有效， 且 SDGD 框架提供了从 zero-shot 到 calibrated 的灵活选项。\n\n\nMAVEN 上 SDGD-cal vs SDGD-zero 的增量（1.3pp）与 Few-NERD 的（1.9pp）相近， 因为 calibration data 在同质 schema 上的价值更高——MiniLM embedding 在 MAVEN 上 虽然 pairwise 信号显著但效应较弱（r=0.120 vs Few-NERD Qwen3 r=0.156）， 经验数据能更精确地识别实际高混淆对。 SDGD-cal（0.318）接近 per-type splitting（0.325）但 API calls 少 7x（24 vs 168）， 完成 SDGD 框架在效率/质量 tradeoff 上的定位。\n"
821	  },
822	  {
823	    "name": "Multi-model Validation (LLaMA-3.3-70B)",
824	    "description": "用 LLaMA-3.3-70B-Instruct 在 Few-NERD 上复现 exp-002 协议： count curve + extreme/random batch + pairwise/per-type 分析。\n",
825	    "results": {
826	      "count_curve": {
827	        "count_1": {
828	          "f1": 0.298,
829	          "recall": 0.612,
830	          "precision": 0.198
831	        },
832	        "count_6": {
833	          "f1": 0.275,
834	          "recall": 0.445,
835	          "precision": 0.2
836	        },
837	        "count_12": {
838	          "f1": 0.318,
839	          "recall": 0.312,
840	          "precision": 0.324
841	        },
842	        "count_22": {
843	          "f1": 0.282,
844	          "recall": 0.258,
845	          "precision": 0.311
846	        },
847	        "count_44": {
848	          "f1": 0.405,
849	          "recall": 0.37,
850	          "precision": 0.447
851	        },
852	        "count_64": {
853	          "f1": 0.378,
854	          "recall": 0.288,
855	          "precision": 0.548
856	        }
857	      },
858	      "pairwise_analysis": {
859	        "qwen3_embedding": {
860	          "n_pairs": 1953,
861	          "pearson_r": 0.138,
862	          "pearson_p": 3.2e-09,
863	          "spearman_rho": 0.144,
864	          "spearman_p": 8.1e-10,
865	          "nonzero_spearman_rho": 0.228,
866	          "nonzero_spearman_p": 5.7e-05
867	        },
868	        "miniLM_embedding": {
869	          "pearson_r": 0.072,
870	          "pearson_p": 0.0015
871	        }
872	      },
873	      "per_type_analysis": {
874	        "n_types": 60,
875	        "filter": "freq>=5",
876	        "qwen3_spearman_rho": -0.265,
877	        "qwen3_spearman_p": 0.041,
878	        "miniLM_spearman_rho": -0.058,
879	        "miniLM_spearman_p": 0.66
880	      },
881	      "extreme_batch": {
882	        "count_6_high_bcs_f1": 0.195,
883	        "count_6_low_bcs_f1": 0.342,
884	        "count_12_high_bcs_f1": 0.215,
885	        "count_12_low_bcs_f1": 0.398,
886	        "confusion_rate_ratio_count6": 18.5,
887	        "confusion_rate_ratio_count12": 12.3
888	      },
889	      "cross_model_comparison": {
890	        "qwen3_pairwise_r": 0.156,
891	        "llama_pairwise_r": 0.138,
892	        "delta": -0.018,
893	        "both_significant": true,
894	        "fisher_z_test_p": 0.52,
895	        "verdict": "效应量无显著差异，two models 一致"
896	      }
897	    },
898	    "tables": [
899	      {
900	        "title": "Cross-model Pairwise Comparison on Few-NERD",
901	        "columns": [
902	          "Model",
903	          "Embedding",
904	          "Pearson r",
905	          "p-value",
906	          "Spearman ρ",
907	          "p-value"
908	        ],
909	        "rows": [
910	          [
911	            "Qwen3-32B",
912	            "Qwen3",
913	            0.156,
914	            "4.6e-12",
915	            0.16,
916	            "1.3e-12"
917	          ],
918	          [
919	            "LLaMA-3.3-70B",
920	            "Qwen3",
921	            0.138,
922	            "3.2e-9",
923	            0.144,
924	            "8.1e-10"
925	          ],
926	          [
927	            "Fisher z-test",
928	            "—",
929	            "Δ=0.018",
930	            "p=0.52",
931	            "—",
932	            "—"
933	          ]
934	        ]
935	      },
936	      {
937	        "title": "Cross-model Extreme Batch Confusion Rate",
938	        "columns": [
939	          "Model",
940	          "Count",
941	          "High-BCS rate",
942	          "Low-BCS rate",
943	          "Ratio"
944	        ],
945	        "rows": [
946	          [
947	            "Qwen3-32B",
948	            6,
949	            0.0728,
950	            0.0014,
951	            "27.5x"
952	          ],
953	          [
954	            "Qwen3-32B",
955	            12,
956	            0.048,
957	            0.0061,
958	            "9.9x"
959	          ],
960	          [
961	            "LLaMA-70B",
962	            6,
963	            0.0612,
964	            0.0033,
965	            "18.5x"
966	          ],
967	          [
968	            "LLaMA-70B",
969	            12,
970	            0.0445,
971	            0.0036,
972	            "12.3x"
973	          ]
974	        ]
975	      }
976	    ],
977	    "figures": [],
978	    "analysis": "Multi-model 验证完成 cross_model_significant: 2/2 的要求。两个差异显著的架构 （Qwen3-32B decoder vs LLaMA-3.3-70B decoder）在 pairwise confusability signal、 per-type direction、extreme batch effect 上全部一致，排除了单模型 artifact 的可能性。 Fisher z-test 的 p=0.52 确认两模型效应量无统计差异。 这是对 reviewer concern \"only one model\" 的完整回应。\n\n\nLLaMA-3.3-70B 的 pairwise r=0.138 略低于 Qwen3 的 0.156，因为不同模型的 confusability 敏感度略有差异——LLaMA 的指令遵从能力更强（70B 参数 + Instruct 调优）， 可能在部分高 confusability pair 上仍能正确区分。但差异不显著（Fisher z p=0.52）， 确认 confusability signal 是跨模型稳定的现象。 Per-type ρ=-0.265（p=0.041）方向和显著性与 Qwen3（ρ=-0.293, p=0.020）一致， 说明 Few-NERD 的跨域 schema 结构使 per-type 信号在不同提取模型上均稳定。 Extreme batch confusion rate ratio 12-18x 与 Qwen3 的 10-28x 范围一致。 LLaMA 整体 F1 略低于 Qwen3（count_64: 0.378 vs 0.414），可能因为 LLaMA 的 NER 提示模板适配度稍差，但不影响 confusability 信号的相对模式。\n"
979	  },
980	  {
981	    "name": "Random Batching Ablation",
982	    "description": "与 SDGD-zero 相同的 k=8 batch count，但 batch composition 完全随机。 5 次随机种子取平均。隔离 confusability-aware grouping 的贡献。\n",
983	    "results": {
984	      "random_batching_results": {
985	        "mean_f1": 0.436,
986	        "std_f1": 0.012,
987	        "mean_precision": 0.53,
988	        "mean_recall": 0.37,
989	        "n_api_calls": 8,
990	        "n_random_seeds": 5
991	      },
992	      "comparison": {
993	        "single_pass_f1": 0.414,
994	        "sdgd_zero_f1": 0.469,
995	        "random_f1": 0.436,
996	        "delta_random_vs_singlepass": "+2.2pp",
997	        "delta_sdgd_vs_random": "+3.3pp",
998	        "delta_sdgd_vs_singlepass": "+5.5pp"
999	      },
1000	      "decomposition": {
1001	        "count_reduction_contribution": "2.2pp (40% of total SDGD gain)",
1002	        "confusability_aware_contribution": "3.3pp (60% of total SDGD gain)"
1003	      },
1004	      "random_batch_bcs_stats": {
1005	        "mean_batch_bcs": 0.838,
1006	        "std_batch_bcs": 0.025,
1007	        "sdgd_mean_batch_bcs": 0.762,
1008	        "bcs_reduction_by_sdgd": "9.1%"
1009	      },
1010	      "type_confusion_rates": {
1011	        "random": 0.031,
1012	        "sdgd_zero": 0.021,
1013	        "single_pass": 0.038
1014	      }
1015	    },
1016	    "tables": [
1017	      {
1018	        "title": "Ablation: SDGD-zero vs Random Batching vs Single-pass",
1019	        "columns": [
1020	          "Method",
1021	          "F1",
1022	          "Recall",
1023	          "Type confusion rate",
1024	          "Mean batch BCS"
1025	        ],
1026	        "rows": [
1027	          [
1028	            "Single-pass (k=1)",
1029	            0.414,
1030	            0.304,
1031	            0.038,
1032	            0.847
1033	          ],
1034	          [
1035	            "Random (k=8)",
1036	            0.436,
1037	            0.37,
1038	            0.031,
1039	            0.838
1040	          ],
1041	          [
1042	            "SDGD-zero (k=8)",
1043	            0.469,
1044	            0.41,
1045	            0.021,
1046	            0.762
1047	          ]
1048	        ]
1049	      }
1050	    ],
1051	    "figures": [],
1052	    "analysis": "这是论文中最重要的 ablation。SDGD vs random（same k）的 +3.3pp gap（p < 0.01） 是 Claim 3 的充分必要证据——confusability-aware 分组本身有价值， SDGD 的收益不仅仅来自简单的 schema 分解。 5 次随机种子的 std=0.012 表明 random batching 的方差较小，SDGD-zero 的 0.469 显著高于随机分布的上界（0.436 + 2×0.012 = 0.460），排除了 lucky draw 的可能性。\n\n\nRandom batching 获得 +2.2pp 改善（vs single-pass）完全来自 count reduction： 从 66 types/batch 降到 ~8 types/batch 减少了 attention dilution，提升了 recall。 但 random batch 的 mean BCS（0.838）接近 single-pass（0.847）， 因为随机分组不会系统性地分离 confusable pair。 SDGD-zero 的额外 +3.3pp 来自 confusability-aware grouping：mean batch BCS 降至 0.762， type confusion rate 从 0.031 降至 0.021（32% 减少）。 60%/40% 的贡献分解表明 confusability-aware grouping 是 SDGD 价值的主要来源， 而非简单的 batch count reduction。这是 Claim 3 最关键的证据—— SDGD 优于 random batching（same k）直接证明了 confusability-aware 分组的独立价值。\n"
1053	  },
1054	  {
1055	    "name": "Per-type Splitting Ablation",
1056	    "description": "每个类型单独一个 batch（k=66），每次只提取一种类型。 UniNER-style 的上界实验。对比 SDGD 和 single-pass。\n",
1057	    "results": {
1058	      "per_type_results": {
1059	        "f1": 0.475,
1060	        "precision": 0.512,
1061	        "recall": 0.443,
1062	        "n_api_calls": 66,
1063	        "wall_clock_minutes": 68.5
1064	      },
1065	      "comparison": {
1066	        "single_pass": {
1067	          "f1": 0.414,
1068	          "api_calls": 1,
1069	          "wall_clock": 2.8
1070	        },
1071	        "random_k8": {
1072	          "f1": 0.436,
1073	          "api_calls": 8,
1074	          "wall_clock": 12.5
1075	        },
1076	        "sdgd_zero": {
1077	          "f1": 0.469,
1078	          "api_calls": 8,
1079	          "wall_clock": 12.5
1080	        },
1081	        "sdgd_cal": {
1082	          "f1": 0.488,
1083	          "api_calls": 17,
1084	          "wall_clock": 14.2
1085	        },
1086	        "per_type": {
1087	          "f1": 0.475,
1088	          "api_calls": 66,
1089	          "wall_clock": 68.5
1090	        }
1091	      },
1092	      "sdgd_zero_vs_per_type": {
1093	        "f1_gap": "-0.6pp",
1094	        "api_calls_ratio": "8.25x fewer",
1095	        "wall_clock_ratio": "5.5x faster",
1096	        "verdict": "SDGD-zero 达到 per-type 的 98.7% F1，但成本仅 12%"
1097	      },
1098	      "sdgd_cal_vs_per_type": {
1099	        "f1_gap": "+1.3pp (SDGD-cal 更高)",
1100	        "api_calls_ratio": "3.9x fewer",
1101	        "verdict": "SDGD-cal 超过 per-type，因为保留了部分 cross-type 上下文"
1102	      },
1103	      "per_type_error_analysis": {
1104	        "type_confusion_rate": 0.002,
1105	        "false_negative_rate": 0.31,
1106	        "hallucination_rate": 0.28,
1107	        "boundary_error_rate": 0.16,
1108	        "note": "type confusion 几乎消除，但 hallucination 上升——单类型 prompt 缺乏跨类型约束"
1109	      }
1110	    },
1111	    "tables": [
1112	      {
1113	        "title": "Full Method Comparison on Few-NERD (66 types)",
1114	        "columns": [
1115	          "Method",
1116	          "F1",
1117	          "P",
1118	          "R",
1119	          "API calls",
1120	          "Wall-clock",
1121	          "Efficiency"
1122	        ],
1123	        "rows": [
1124	          [
1125	            "Single-pass",
1126	            0.414,
1127	            0.648,
1128	            0.304,
1129	            1,
1130	            "2.8 min",
1131	            "baseline"
1132	          ],
1133	          [
1134	            "Random (k=8)",
1135	            0.436,
1136	            0.53,
1137	            0.37,
1138	            8,
1139	            "12.5 min",
1140	            "+2.2pp / 8 calls"
1141	          ],
1142	          [
1143	            "SDGD-zero (k=8)",
1144	            0.469,
1145	            0.548,
1146	            0.41,
1147	            8,
1148	            "12.5 min",
1149	            "+5.5pp / 8 calls"
1150	          ],
1151	          [
1152	            "Per-type (k=66)",
1153	            0.475,
1154	            0.512,
1155	            0.443,
1156	            66,
1157	            "68.5 min",
1158	            "+6.1pp / 66 calls"
1159	          ],
1160	          [
1161	            "SDGD-cal (k=9)",
1162	            0.488,
1163	            0.556,
1164	            0.435,
1165	            17,
1166	            "14.2 min",
1167	            "+7.4pp / 17 calls"
1168	          ]
1169	        ]
1170	      }
1171	    ],
1172	    "figures": [],
1173	    "analysis": "Per-type 实验揭示了一个反直觉的结果：最大分解≠最优分解。 SDGD-cal 超过 per-type 因为保留了 cross-type context 带来的消歧能力。 这使论文的 method 贡献更强——SDGD 不仅仅是\"把类型分开\"的简单策略， 而是在 confusability reduction 和 context preservation 之间的 principled tradeoff， graph coloring 框架正好 operationalize 了这个 tradeoff。 Pareto plot 是论文的核心 figure 之一：清晰展示 SDGD variants 在效率/质量空间的优势。\n\n\nPer-type splitting 几乎消除了 type confusion（rate=0.002 vs single-pass 0.038）， 验证了 confusability 是可通过分组解决的。但 F1 只有 0.475，低于预期的\"上界\"， 因为存在两个反向效应： （1）缺乏 cross-type context：当只有一个类型时，模型无法利用\"这个 span 更像 X 而非 Y\"的对比信息， 导致某些模糊 span 被遗漏或被 hallucinate（hallucination rate 上升至 0.28）； （2）recall 上升到 0.443（最高），因为 attention 完全集中在单一类型上。 SDGD-zero（0.469）接近 per-type（0.475）的原因是：SDGD 的 8-type batch 保留了 有限但有用的 cross-type context，同时移除了大部分 confusability。 SDGD-cal（0.488）超过 per-type（0.475）是关键发现——证明 optimal decomposition 不是\"最大分解\"而是\"最优 confusability/context tradeoff\"，SDGD 框架正好在此定位。\n"
1174	  },
1175	  {
1176	    "name": "SCS Proxy Validation",
1177	    "description": "用 exp-010 的经验 confusion matrix 作为 ground truth，验证 embedding SCS 作为 confusability proxy 的排序准确性。\n",
1178	    "results": {
1179	      "qwen3_scs_vs_empirical": {
1180	        "spearman_rho": 0.584,
1181	        "spearman_p": 2.3e-18,
1182	        "kendall_tau": 0.421,
1183	        "kendall_p": 8.1e-15,
1184	        "top_20_overlap": 0.85,
1185	        "top_50_overlap": 0.72
1186	      },
1187	      "miniLM_scs_vs_empirical": {
1188	        "spearman_rho": 0.432,
1189	        "spearman_p": 1.7e-10,
1190	        "kendall_tau": 0.312,
1191	        "kendall_p": 3.4e-08,
1192	        "top_20_overlap": 0.65,
1193	        "top_50_overlap": 0.54
1194	      },
1195	      "precision_at_k": {
1196	        "qwen3_p_at_10": 0.9,
1197	        "qwen3_p_at_20": 0.85,
1198	        "qwen3_p_at_50": 0.72,
1199	        "miniLM_p_at_10": 0.7,
1200	        "miniLM_p_at_20": 0.65,
1201	        "miniLM_p_at_50": 0.54
1202	      },
1203	      "failure_modes": {
1204	        "false_positive_scs": "embedding 高相似但不混淆：通常是共享 supertype 但 subtype 名称足够区分",
1205	        "false_negative_scs": "embedding 低相似但实际混淆：通常因共现频率或 prompt 位置效应"
1206	      }
1207	    },
1208	    "tables": [
1209	      {
1210	        "title": "SCS Proxy Validation",
1211	        "columns": [
1212	          "Embedding",
1213	          "Spearman ρ",
1214	          "Kendall τ",
1215	          "Top-20 overlap",
1216	          "P@10"
1217	        ],
1218	        "rows": [
1219	          [
1220	            "Qwen3",
1221	            0.584,
1222	            0.421,
1223	            "85%",
1224	            0.9
1225	          ],
1226	          [
1227	            "MiniLM",
1228	            0.432,
1229	            0.312,
1230	            "65%",
1231	            0.7
1232	          ]
1233	        ]
1234	      }
1235	    ],
1236	    "figures": [],
1237	    "analysis": "SCS validation 完成了 SDGD 框架的理论闭环：embedding SCS 是合理的 confusability proxy （ρ=0.58），但经验数据更好（SDGD-cal > SDGD-zero）。 论文的实用建议：cold-start 用 SDGD-zero（Qwen3 embedding）， 有少量 calibration data 后切换到 SDGD-cal。Qwen3 明显优于 MiniLM 作为 proxy 在 Few-NERD 上，但 MAVEN 上反转（→ 使用 task-appropriate embedding）。\n\nQwen3 SCS 与经验 confusability 的 Spearman ρ=0.584 表明 embedding 是合理但非完美的代理。 相关性显著但不为 1 的原因： （1）embedding 相似度捕获语义距离，而实际 confusion 还受 prompt 位置、类型名称字面相似性、 训练数据频率等非语义因素影响； （2）Qwen3 embedding 来自指令调优后的最后一层，保留了较多任务相关信息，因此优于 MiniLM。 Top-20 的 85% 重叠解释了为什么 SDGD-zero 已经很有效——最 confusable 的 pair 大多被正确识别。 SDGD-cal 的增量主要来自修正那 15% 的错误排序。 Precision@k 在 top-10 最高（0.90），说明 embedding proxy 在识别\"最危险\"pair 时最可靠。\n"
1238	  }
1239	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c40a0890-b088-4462-9923-8187a9e53a1c",
  "isSidechain": false,
  "promptId": "cdf92f18-0400-4c4f-90e5-485ecb947e5a",
  "type": "user",
  "uuid": "e56e4fb0-6209-4602-8be0-2c4eebba65db",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"MAVEN Confusability Study (full)\",\n    \"description\": \"在 MAVEN 168 event types 上运行 v2 prompt，500 sample，完成 count curve、 batch-level BCS 对照、pairwise SCS→confusion 相关、per-type 分析及 centrality confound 量化。\\n\",\n    \"results\": {\n      \"count_curve_relaxed_f1\": {\n        \"count_1\": 0.118,\n        \"count_6\": 0.142,\n        \"count_12\": 0.178,\n        \"count_22\": 0.21,\n        \"count_44\": 0.248,\n        \"count_64\": 0.261,\n        \"count_168\": 0.272\n      },\n      \"count_curve_exact_f1\": {\n        \"count_1\": 0.011,\n        \"count_6\": 0.005,\n        \"count_12\": 0.01,\n        \"count_22\": 0.015,\n        \"count_44\": 0.02,\n        \"count_64\": 0.016,\n        \"count_168\": 0.014\n      },\n      \"pairwise_miniLM\": {\n        \"n_pairs\": 14028,\n        \"pearson_r\": 0.12,\n        \"pearson_p\": 1.2e-45,\n        \"spearman_rho\": 0.135,\n        \"spearman_p\": 3.8e-58,\n        \"nonzero_spearman_rho\": 0.191,\n        \"nonzero_spearman_p\": 0.00047\n      },\n      \"pairwise_qwen3\": {\n        \"pearson_r\": -0.007,\n        \"pearson_p\": 0.41,\n        \"verdict\": \"NOT_SIGNIFICANT — Qwen3 embeddings 无法在同质 schema 上捕获 pairwise signal\"\n      },\n      \"per_type_miniLM\": {\n        \"n_types\": 148,\n        \"filter\": \"freq>=10\",\n        \"spearman_rho\": 0.208,\n        \"spearman_p\": 0.011,\n        \"direction\": \"positive\",\n        \"verdict\": \"CENTRALITY CONFOUND — 方向与假设相反\"\n      },\n      \"per_type_qwen3\": {\n        \"spearman_rho\": 0.189,\n        \"spearman_p\": 0.021,\n        \"direction\": \"positive\",\n        \"verdict\": \"CENTRALITY CONFOUND — 两种 embedding 方向一致，排除 embedding 压缩假说\"\n      },\n      \"centrality_analysis\": {\n        \"mean_bcs_vs_type_frequency_r\": 0.34,\n        \"mean_bcs_vs_type_frequency_p\": 2.1e-05,\n        \"interpretation\": \"高 mean BCS = 语义中心类型 = 高频/LLM 更熟悉 = 更高 F1\"\n      },\n      \"batch_level_extreme\": {\n        \"count_6_high_bcs_relaxed_f1\": 0.218,\n        \"count_6_low_bcs_relaxed_f1\": 0.098,\n        \"count_12_high_bcs_relaxed_f1\": 0.192,\n        \"count_12_low_bcs_relaxed_f1\": 0.114,\n        \"confusion_rate_ratio_extreme_count6\": 8.2,\n        \"confusion_rate_ratio_extreme_count12\": 6.5\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"MAVEN Count Curve (v2 prompt, 500 samples)\",\n        \"columns\": [\n          \"count\",\n          \"relaxed_F1\",\n          \"exact_F1\",\n          \"recall\",\n          \"precision\",\n          \"pred_gold_ratio\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.118,\n            0.011,\n            0.21,\n            0.082,\n            2.56\n          ],\n          [\n            6,\n            0.142,\n            0.005,\n            0.185,\n            0.115,\n            1.61\n          ],\n          [\n            12,\n            0.178,\n            0.01,\n            0.21,\n            0.154,\n            1.36\n          ],\n          [\n            22,\n            0.21,\n            0.015,\n            0.238,\n            0.188,\n            1.27\n          ],\n          [\n            44,\n            0.248,\n            0.02,\n            0.268,\n            0.231,\n            1.16\n          ],\n          [\n            64,\n            0.261,\n            0.016,\n            0.275,\n            0.249,\n            1.1\n          ]\n        ]\n      },\n      {\n        \"title\": \"MAVEN Pairwise SCS → Confusion (2×2 embedding comparison)\",\n        \"columns\": [\n          \"embedding\",\n          \"pearson_r\",\n          \"p-value\",\n          \"n_pairs\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"MiniLM\",\n            0.12,\n            \"1.2e-45\",\n            14028,\n            \"PASS\"\n          ],\n          [\n            \"Qwen3\",\n            -0.007,\n            0.41,\n            14028,\n            \"FAIL\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"MAVEN Per-type BCS → F1 (centrality confound)\",\n        \"columns\": [\n          \"embedding\",\n          \"spearman_ρ\",\n          \"p-value\",\n          \"direction\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"MiniLM\",\n            0.208,\n            0.011,\n            \"positive\",\n            \"CONFOUND\"\n          ],\n          [\n            \"Qwen3\",\n            0.189,\n            0.021,\n            \"positive\",\n            \"CONFOUND\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MAVEN 结果完美支持论文的两层叙事：（1）pairwise confusability 在第三个任务（ED）上独立复现， 跨 NER→RE→ED 三任务验证 Claim 1；（2）per-type centrality confound 是方法论贡献—— 解释了为什么简单的 per-type 聚合（如直接用 mean BCS 排序类型）在同质 schema 上失效， 而 pairwise 分析和 SDGD 的 pairwise 操作策略绕过了这个问题。 Exact F1 极低（<0.02）是 event trigger 边界匹配问题，不影响 confusability 分析（使用 relaxed F1）。\\n\\n\\nMAVEN 168 个 event types 来自同一语义域（FrameNet 层级结构），SCS 分布高度集中 （mean=0.216, std=0.103），不像 Few-NERD 有跨域分离。 Pairwise MiniLM 信号成立（r=0.120）因为 MiniLM 的通用语义空间在细粒度事件类型间保留了足够区分度， 而 Qwen3 指令调优后的表征空间过度压缩了语义邻近类型。 Per-type 正方向是 centrality confound 的典型表现：在同质 schema 中， mean BCS 高的类型恰好是语义网络的中心节点（如 \\\"Attack\\\", \\\"Meeting\\\"）， 这些类型在训练语料中高频出现，LLM 先验知识更强，F1 自然更高。 这不是假设失败，而是方法论贡献——揭示了 per-type 聚合何时失效。 Batch-level 极端组对照仍然显示 high-BCS 组更高（与 Few-NERD 方向相同）， 因为极端组构造直接操作 batch 内相似度，绕过了 centrality confound。\\n\"\n  },\n  {\n    \"name\": \"DocRED Confusability Study\",\n    \"description\": \"在 DocRED 96 关系类型上进行 count curve + pairwise SCS→confusion 分析。 文档级 RE 任务，更长的上下文，测试 confusability 信号在复杂推理场景下的鲁棒性。\\n\",\n    \"results\": {\n      \"count_curve_f1\": {\n        \"count_1\": 0.195,\n        \"count_6\": 0.168,\n        \"count_12\": 0.152,\n        \"count_24\": 0.131,\n        \"count_48\": 0.118,\n        \"count_96\": 0.098\n      },\n      \"pairwise_miniLM\": {\n        \"n_pairs\": 4560,\n        \"pearson_r\": 0.108,\n        \"pearson_p\": 3.5e-13,\n        \"spearman_rho\": 0.122,\n        \"spearman_p\": 1.8e-16\n      },\n      \"per_type_qwen3\": {\n        \"n_types\": 82,\n        \"filter\": \"freq>=5\",\n        \"spearman_rho\": -0.231,\n        \"spearman_p\": 0.037\n      },\n      \"extreme_batch_comparison\": {\n        \"count_12_high_bcs_f1\": 0.105,\n        \"count_12_low_bcs_f1\": 0.188,\n        \"delta_pp\": -8.3,\n        \"confusion_rate_ratio\": 5.8\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"DocRED Pairwise Comparison Across Embeddings\",\n        \"columns\": [\n          \"embedding\",\n          \"pearson_r\",\n          \"p-value\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"MiniLM\",\n            0.108,\n            \"3.5e-13\",\n            \"PASS\"\n          ],\n          [\n            \"Qwen3\",\n            0.095,\n            \"2.1e-10\",\n            \"PASS\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DocRED 作为第四个任务验证了 pairwise confusability 信号的跨任务泛化性。 效应量较小但 n_pairs 足够保证统计显著。文档级上下文的缓冲效应是合理的—— 更长的文档为模型提供了更多消歧证据。这一结果支持在论文中加入 DocRED 作为 supplementary evidence，但不改变三任务核心叙事。\\n\\n\\nDocRED 关系类型语义分布介于 Few-NERD（跨域）和 MAVEN（同域）之间—— 96 个关系覆盖多个领域但部分关系高度相似（如 \\\"place of birth\\\" vs \\\"place of death\\\"）。 Pairwise 信号成立但效应略弱于 Few-NERD（r=0.108 vs 0.156），因为文档级 RE 中 更长的上下文提供了更多消歧信息，部分缓解了 confusability 效应。 Per-type 方向正确（负相关），因为 DocRED 跨域程度足够避免 MAVEN 的 centrality confound。 Extreme batch delta 较小（8.3pp vs Few-NERD 的 20-50pp），同样因为文档级上下文的缓冲效应。\\n\"\n  },\n  {\n    \"name\": \"Count × Confusability Interaction (2×2)\",\n    \"description\": \"在 Few-NERD 上构造 {低 count=6, 高 count=22} × {低 BCS, 高 BCS} 四组， 每组 10 batches，测试 count 和 confusability 的加法/乘法交互效应。\\n\",\n    \"results\": {\n      \"factorial_f1\": {\n        \"low_count_low_bcs\": 0.372,\n        \"low_count_high_bcs\": 0.268,\n        \"high_count_low_bcs\": 0.312,\n        \"high_count_high_bcs\": 0.178\n      },\n      \"factorial_recall\": {\n        \"low_count_low_bcs\": 0.468,\n        \"low_count_high_bcs\": 0.415,\n        \"high_count_low_bcs\": 0.33,\n        \"high_count_high_bcs\": 0.265\n      },\n      \"factorial_type_confusion_rate\": {\n        \"low_count_low_bcs\": 0.008,\n        \"low_count_high_bcs\": 0.045,\n        \"high_count_low_bcs\": 0.018,\n        \"high_count_high_bcs\": 0.072\n      },\n      \"two_way_anova\": {\n        \"count_main_effect_F\": 14.2,\n        \"count_main_effect_p\": 0.0006,\n        \"bcs_main_effect_F\": 22.8,\n        \"bcs_main_effect_p\": 3.1e-05,\n        \"interaction_F\": 3.1,\n        \"interaction_p\": 0.087,\n        \"interaction_verdict\": \"边际显著，轻微超加性\"\n      },\n      \"effect_decomposition\": {\n        \"count_delta_f1\": -0.075,\n        \"bcs_delta_f1\": -0.119,\n        \"interaction_delta_f1\": -0.027,\n        \"additive_prediction_high_high\": 0.197,\n        \"actual_high_high\": 0.178,\n        \"super_additive_gap\": -0.019\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"2×2 Factorial F1 Results\",\n        \"columns\": [\n          \"\",\n          \"Low BCS\",\n          \"High BCS\",\n          \"BCS effect\"\n        ],\n        \"rows\": [\n          [\n            \"Low count (6)\",\n            0.372,\n            0.268,\n            \"-0.104\"\n          ],\n          [\n            \"High count (22)\",\n            0.312,\n            0.178,\n            \"-0.134\"\n          ],\n          [\n            \"Count effect\",\n            \"-0.060\",\n            \"-0.090\",\n            \"interaction: -0.027\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"2×2 Type Confusion Rate\",\n        \"columns\": [\n          \"\",\n          \"Low BCS\",\n          \"High BCS\",\n          \"ratio\"\n        ],\n        \"rows\": [\n          [\n            \"Low count (6)\",\n            0.008,\n            0.045,\n            \"5.6x\"\n          ],\n          [\n            \"High count (22)\",\n            0.018,\n            0.072,\n            \"4.0x\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"2×2 结果核心支持 multi-channel 正交模型。BCS 主效应（F=22.8）大于 count 主效应（F=14.2）， 说明在 Few-NERD 上 confusability 是更强的降级因子。交互效应 p=0.087 表明实质上加法模型足够， 轻微超加性可在论文中讨论但不改变核心叙事。这一结果直接支持 SDGD 的设计原理： 单独优化 batch 内 confusability（而非同时优化 count）已经足够捕获大部分可分解的性能损失。\\n\\n\\nCount 和 confusability 通过不同机制降低性能：count 稀释 attention → recall 下降， confusability 引起类型混淆 → precision 下降。两者理论上正交，但在 high-count high-BCS 条件下 存在轻微超加性——当 attention 已被稀释时，模型对类型区分的余量更小，confusability 的边际伤害更大。 交互效应统计上边际显著（p=0.087），不足以拒绝加法模型，这恰好支持论文的\\\"正交通道\\\"叙事： 两个通道基本独立，各自可寻址。超加性的微弱存在（1.9pp gap）在讨论中作为 nuance 提及。\\n\"\n  },\n  {\n    \"name\": \"Systematic Error Taxonomy\",\n    \"description\": \"在 exp-002 数据上系统分类 FP 错误为四类：type_substitution、boundary_error、 false_negative、hallucination，按 BCS quartile 分 bin 统计分布。\\n\",\n    \"results\": {\n      \"error_distribution_by_bcs_quartile\": {\n        \"Q1_low_bcs\": {\n          \"type_substitution_pct\": 6.2,\n          \"boundary_error_pct\": 14.8,\n          \"false_negative_pct\": 58.3,\n          \"hallucination_pct\": 20.7,\n          \"total_errors\": 385\n        },\n        \"Q2\": {\n          \"type_substitution_pct\": 12.5,\n          \"boundary_error_pct\": 13.2,\n          \"false_negative_pct\": 51.8,\n          \"hallucination_pct\": 22.5,\n          \"total_errors\": 412\n        },\n        \"Q3\": {\n          \"type_substitution_pct\": 22.1,\n          \"boundary_error_pct\": 11.9,\n          \"false_negative_pct\": 44.6,\n          \"hallucination_pct\": 21.4,\n          \"total_errors\": 448\n        },\n        \"Q4_high_bcs\": {\n          \"type_substitution_pct\": 38.4,\n          \"boundary_error_pct\": 10.5,\n          \"false_negative_pct\": 32.3,\n          \"hallucination_pct\": 18.8,\n          \"total_errors\": 521\n        }\n      },\n      \"monotonic_trends\": {\n        \"type_substitution_vs_bcs\": \"单调递增 6.2→38.4%，Kendall τ=0.92\",\n        \"false_negative_vs_bcs\": \"单调递减 58.3→32.3%，Kendall τ=-0.88\",\n        \"boundary_error_vs_bcs\": \"微弱递减 14.8→10.5%，不显著\",\n        \"hallucination_vs_bcs\": \"无趋势 20.7→18.8%，Kendall τ=-0.21\"\n      },\n      \"by_count_level\": {\n        \"count_6\": {\n          \"Q1_type_sub_pct\": 4.8,\n          \"Q4_type_sub_pct\": 31.2,\n          \"Q1_fn_pct\": 61.5,\n          \"Q4_fn_pct\": 38.1\n        },\n        \"count_12\": {\n          \"Q1_type_sub_pct\": 7.9,\n          \"Q4_type_sub_pct\": 44.7,\n          \"Q1_fn_pct\": 54.2,\n          \"Q4_fn_pct\": 27.8\n        }\n      },\n      \"chi_squared_bcs_vs_error_type\": {\n        \"statistic\": 89.4,\n        \"p\": 1.2e-16,\n        \"df\": 9\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"Error Type Distribution by BCS Quartile (%)\",\n        \"columns\": [\n          \"BCS quartile\",\n          \"Type sub.\",\n          \"Boundary\",\n          \"False neg.\",\n          \"Halluc.\",\n          \"Total\"\n        ],\n        \"rows\": [\n          [\n            \"Q1 (low)\",\n            6.2,\n            14.8,\n            58.3,\n            20.7,\n            385\n          ],\n          [\n            \"Q2\",\n            12.5,\n            13.2,\n            51.8,\n            22.5,\n            412\n          ],\n          [\n            \"Q3\",\n            22.1,\n            11.9,\n            44.6,\n            21.4,\n            448\n          ],\n          [\n            \"Q4 (high)\",\n            38.4,\n            10.5,\n            32.3,\n            18.8,\n            521\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Error taxonomy 是 Claim 2（multi-channel degradation）最直接的机械证据。 Type substitution 从 Q1 的 6.2% 飙升到 Q4 的 38.4%（6.2x），而 false negative 反向变化， hallucination 稳定。这精确对应 multi-channel 模型的预测：confusability 通道选择性地增加 类型混淆错误，而非所有类型错误。count_12 条件下效应更强（Q4 type_sub=44.7%）， 因为更多类型在 prompt 中同时出现时，confusability 的累积效应更大。 Chi-squared 高度显著（p=1.2e-16）确认 BCS quartile 与错误类型分布非独立。\\n\\n\\nType substitution 与 BCS 强单调递增是 Claim 2 的核心机械证据：高 confusability batch 中， 模型正确识别了 entity span 但将其标注为语义邻近的错误类型。这是 confusability 通道的签名错误。 False negative 与 BCS 递减是因为在高 BCS batch 中，模型更倾向于\\\"猜错类型\\\"而非\\\"完全遗漏\\\"—— 当多个相似类型在 prompt 中共现时，模型被激活去标注更多 span，但标注质量下降。 Hallucination 和 boundary error 与 BCS 无关，因为它们由其他因素驱动（幻觉=模型先验偏差， 边界=tokenization/span 识别问题），与类型相似度正交。 这一分解证实了 multi-channel 模型：count→omission(FN)，confusability→substitution。\\n\"\n  },\n  {\n    \"name\": \"SDGD-zero Few-NERD (R2 revision)\",\n    \"description\": \"SDGD-zero R2：修复 R1 的阈值和合并策略问题。基于 Qwen3 embedding pairwise SCS， 构建 confusability graph（阈值 τ=0.82），图着色分组，每组独立推理后合并。 对比 single-pass full-schema baseline。\\n\",\n    \"results\": {\n      \"r2_fixes\": {\n        \"threshold\": \"τ=0.82 (R1 used 0.90, too aggressive → batches still confusable)\",\n        \"merge_strategy\": \"span-level confidence dedup with type priority (R1 used naive union → duplicate spans)\",\n        \"batch_config\": \"8 batches, avg 8.25 types/batch (range: 6-11)\"\n      },\n      \"sdgd_zero_results\": {\n        \"f1\": 0.469,\n        \"precision\": 0.548,\n        \"recall\": 0.41,\n        \"n_api_calls\": 8,\n        \"wall_clock_minutes\": 12.5\n      },\n      \"single_pass_baseline\": {\n        \"f1\": 0.414,\n        \"precision\": 0.648,\n        \"recall\": 0.304,\n        \"n_api_calls\": 1,\n        \"wall_clock_minutes\": 2.8\n      },\n      \"delta_vs_singlepass\": {\n        \"delta_f1_pp\": 5.5,\n        \"delta_recall_pp\": 10.6,\n        \"delta_precision_pp\": -10.0,\n        \"f1_p_value\": 0.003,\n        \"verdict\": \"PASS — F1 显著提升，recall 大幅改善，precision 可控下降\"\n      },\n      \"per_batch_analysis\": {\n        \"mean_batch_bcs\": 0.762,\n        \"max_batch_bcs\": 0.801,\n        \"min_batch_bcs\": 0.718,\n        \"singlepass_bcs\": 0.847,\n        \"bcs_reduction_pct\": 10.0\n      },\n      \"batch_level_breakdown\": {\n        \"batch_1\": {\n          \"n_types\": 8,\n          \"bcs\": 0.738,\n          \"f1\": 0.385\n        },\n        \"batch_2\": {\n          \"n_types\": 9,\n          \"bcs\": 0.762,\n          \"f1\": 0.352\n        },\n        \"batch_3\": {\n          \"n_types\": 7,\n          \"bcs\": 0.721,\n          \"f1\": 0.401\n        },\n        \"batch_4\": {\n          \"n_types\": 11,\n          \"bcs\": 0.801,\n          \"f1\": 0.312\n        },\n        \"batch_5\": {\n          \"n_types\": 8,\n          \"bcs\": 0.745,\n          \"f1\": 0.378\n        },\n        \"batch_6\": {\n          \"n_types\": 9,\n          \"bcs\": 0.773,\n          \"f1\": 0.345\n        },\n        \"batch_7\": {\n          \"n_types\": 8,\n          \"bcs\": 0.752,\n          \"f1\": 0.368\n        },\n        \"batch_8\": {\n          \"n_types\": 6,\n          \"bcs\": 0.718,\n          \"f1\": 0.415\n        }\n      },\n      \"type_confusion_rate\": {\n        \"sdgd_zero\": 0.021,\n        \"single_pass\": 0.038,\n        \"reduction_pct\": 44.7\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"SDGD-zero R2 vs Single-pass on Few-NERD (66 types)\",\n        \"columns\": [\n          \"Method\",\n          \"F1\",\n          \"Precision\",\n          \"Recall\",\n          \"API calls\",\n          \"Wall-clock (min)\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass\",\n            0.414,\n            0.648,\n            0.304,\n            1,\n            2.8\n          ],\n          [\n            \"SDGD-zero R2\",\n            0.469,\n            0.548,\n            0.41,\n            8,\n            12.5\n          ],\n          [\n            \"Δ\",\n            \"+5.5pp\",\n            \"-10.0pp\",\n            \"+10.6pp\",\n            \"+7\",\n            \"+9.7\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SDGD-zero R2 的成功直接验证了 Claim 3：confusability-aware 分组本身有价值。 +5.5 F1 pp 中，约 2.2pp 来自 count reduction（见 exp-013），3.3pp 来自 confusability-aware grouping。 Per-batch 分析显示 batch 4（BCS=0.801, F1=0.312）vs batch 8（BCS=0.718, F1=0.415） 的对比直接体现了 SDGD 的内部一致性——即使在 SDGD 的优化分组内， 残余 confusability 差异仍然预测性能差异。 Type confusion rate 下降 44.7% 是机械证据：SDGD 通过分离 confusable pair 直接减少了 Channel 2 错误。\\n\\n\\nR1 失败的根因是两个实现问题：（1）SCS 阈值 τ=0.90 过高，导致 confusability graph 过于稀疏， 图着色产生的分组仍包含大量高相似度对（0.82-0.90 范围被遗漏）； （2）naive union merge 在多个 batch 对同一 span 产生不同类型标注时直接取并集， 引入大量重复和矛盾预测。R2 将 τ 降至 0.82（基于 Few-NERD pairwise SCS 分布的 P90）， 确保 top-10% 相似度对被强制分离；merge 策略改为 span-level confidence dedup， 当多个 batch 对同一 text span 产生不同类型时取置信度最高者。 F1 从 0.414 提升至 0.469（+5.5pp）主要来自 recall 改善（+10.6pp）： 较小的 batch（8 types vs 66 types）显著减少了 attention dilution，模型遗漏更少的 entity。 Precision 下降（-10.0pp）因为 8 个 batch 的合并引入了少量 spurious predictions， 但 confidence-based merge 将其控制在可接受范围。 净 F1 收益 +5.5pp 在 [3, 8] 范围中部，合理反映了 zero-shot 图着色方法的局限—— embedding 相似度只是 empirical confusability 的代理，最优分组需要 calibration data（→ exp-010）。\\n\"\n  },\n  {\n    \"name\": \"SDGD-zero MAVEN\",\n    \"description\": \"SDGD-zero 在 MAVEN 168 event types 上的 cross-task 验证。 基于 MiniLM embedding（MAVEN 上有效的 pairwise proxy），graph coloring 分组。\\n\",\n    \"results\": {\n      \"sdgd_zero_results\": {\n        \"relaxed_f1\": 0.305,\n        \"exact_f1\": 0.022,\n        \"n_batches\": 14,\n        \"avg_types_per_batch\": 12.0,\n        \"n_api_calls\": 14,\n        \"wall_clock_minutes\": 22.4\n      },\n      \"single_pass_baseline\": {\n        \"relaxed_f1\": 0.272,\n        \"exact_f1\": 0.014,\n        \"n_api_calls\": 1,\n        \"wall_clock_minutes\": 4.2\n      },\n      \"random_batching_baseline\": {\n        \"relaxed_f1\": 0.282,\n        \"n_api_calls\": 14\n      },\n      \"delta_vs_singlepass\": {\n        \"delta_relaxed_f1_pp\": 3.3,\n        \"p_value\": 0.012\n      },\n      \"delta_vs_random\": {\n        \"delta_relaxed_f1_pp\": 2.3,\n        \"p_value\": 0.038\n      },\n      \"type_confusion_reduction\": {\n        \"sdgd_zero_rate\": 0.035,\n        \"single_pass_rate\": 0.058,\n        \"reduction_pct\": 39.7\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"SDGD-zero on MAVEN (168 types, MiniLM embedding)\",\n        \"columns\": [\n          \"Method\",\n          \"Relaxed F1\",\n          \"Exact F1\",\n          \"API calls\",\n          \"Δ relaxed F1\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass (168 types)\",\n            0.272,\n            0.014,\n            1,\n            \"—\"\n          ],\n          [\n            \"Random batching (k=14)\",\n            0.282,\n            0.017,\n            14,\n            \"+1.0pp\"\n          ],\n          [\n            \"SDGD-zero (k=14)\",\n            0.305,\n            0.022,\n            14,\n            \"+3.3pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MAVEN 上的正向结果完成 SDGD 的 cross-task 验证（NER + ED）， 证明 confusability-aware 分组在不同任务和 schema 特征下均有效。 效应量较小但仍然显著（p=0.012 vs single-pass），足以支持 Claim 3。 值得注意的是 embedding 选择的重要性——在 MAVEN 上使用 Qwen3 embedding 的 SDGD 可能无效（因为 Qwen3 pairwise 信号不显著），这强化了论文中\\\"task-appropriate embedding\\\"的建议。\\n\\n\\nMAVEN 上 SDGD 收益（+3.3pp relaxed F1）小于 Few-NERD（+5.5pp），原因有二： （1）MAVEN 的 SCS 分布更集中（mean=0.216, std=0.103），图着色的\\\"分离空间\\\"更小， 无法像 Few-NERD 那样找到明确的低相似度分组； （2）MAVEN F1 与 count 正相关（exp-004），batch 缩小到 12 types 会损失部分 count-context 效益， 部分抵消了 confusability reduction 的收益。 使用 MiniLM 而非 Qwen3 是正确选择，因为 MiniLM pairwise 信号在 MAVEN 上有效（r=0.120）而 Qwen3 无效。 vs random 的 +2.3pp 确认 confusability-aware 分组在同质 schema 上仍然有价值， 尽管收益小于跨域 schema。\\n\"\n  },\n  {\n    \"name\": \"SDGD-cal Few-NERD\",\n    \"description\": \"SDGD-cal：使用 5-10 calibration examples 构建经验 confusion matrix， 替代 embedding SCS 作为 confusability proxy，再用 graph coloring 分组。 对比 SDGD-zero。\\n\",\n    \"results\": {\n      \"calibration_cost\": {\n        \"n_calibration_examples\": 8,\n        \"n_calibration_api_calls\": 8,\n        \"calibration_wall_clock_minutes\": 4.5\n      },\n      \"sdgd_cal_results\": {\n        \"f1\": 0.488,\n        \"precision\": 0.556,\n        \"recall\": 0.435,\n        \"n_api_calls\": 9,\n        \"wall_clock_minutes\": 14.2,\n        \"total_api_calls_incl_calibration\": 17\n      },\n      \"sdgd_zero_comparison\": {\n        \"sdgd_zero_f1\": 0.469,\n        \"delta_f1_pp\": 1.9,\n        \"p_value\": 0.042\n      },\n      \"calibration_vs_embedding_correlation\": {\n        \"empirical_vs_qwen3_scs_spearman\": 0.58,\n        \"empirical_vs_miniLM_scs_spearman\": 0.43,\n        \"verdict\": \"经验 confusability 与 embedding proxy 中等相关，但经验版更准确\"\n      },\n      \"confusion_matrix_properties\": {\n        \"n_nonzero_pairs\": 312,\n        \"n_total_pairs\": 2145,\n        \"sparsity\": 0.854,\n        \"top_empirical_pair\": \"person-other ↔ person-politician (confusion=23/8 examples)\",\n        \"top_embedding_pair\": \"same pair (BCS=0.934)\",\n        \"agreement_top_20\": \"85% overlap\",\n        \"disagreement_examples\": \"building-library ↔ building-theater (high SCS=0.91, low empirical=0)\"\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"SDGD Variant Comparison on Few-NERD\",\n        \"columns\": [\n          \"Method\",\n          \"F1\",\n          \"P\",\n          \"R\",\n          \"API calls (total)\",\n          \"Δ F1 vs single-pass\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass\",\n            0.414,\n            0.648,\n            0.304,\n            1,\n            \"—\"\n          ],\n          [\n            \"SDGD-zero\",\n            0.469,\n            0.548,\n            0.41,\n            8,\n            \"+5.5pp\"\n          ],\n          [\n            \"SDGD-cal\",\n            0.488,\n            0.556,\n            0.435,\n            17,\n            \"+7.4pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SDGD-cal 的 +1.9pp 增量验证了 SDGD 框架的可扩展性——更好的 confusability 估计 直接转化为更好的分组和更高的 F1。这也为 SDGD-zero 的实用性提供了参照： 在无 calibration data 的冷启动场景下，SDGD-zero 已能获得大部分收益（5.5/7.4 = 74%）， calibration 的边际收益递减。论文中 SDGD-zero 作为默认推荐，SDGD-cal 作为高精度选项。\\n\\n\\nSDGD-cal 比 SDGD-zero 高 1.9 F1 pp，因为经验 confusion matrix 直接捕获了 LLM 的实际混淆模式，而 embedding SCS 只是语义相似度的代理。 两者差距不大（1.9pp）因为 embedding proxy 已经相当好——top-20 confusable pairs 有 85% 重叠。 差异主要来自 edge cases：某些 embedding 上高相似但 LLM 实际不混淆的 pair （如 building-library ↔ building-theater，LLM 依靠上下文线索有效区分）， 以及 embedding 上不相似但 LLM 实际混淆的 pair（可能由于 training data 偏差）。 Calibration 的额外成本（8 API calls）使总 API calls 从 8 增至 17， 但仍远低于 per-type splitting（66 calls），且 F1 接近 per-type 水平。\\n\"\n  },\n  {\n    \"name\": \"SDGD-cal MAVEN\",\n    \"description\": \"SDGD-cal 在 MAVEN 168 types 上的完整对比。 使用 MiniLM embedding 和 10 calibration examples。\\n\",\n    \"results\": {\n      \"sdgd_cal_results\": {\n        \"relaxed_f1\": 0.318,\n        \"exact_f1\": 0.025,\n        \"n_api_calls\": 14,\n        \"total_api_calls_incl_calibration\": 24\n      },\n      \"full_comparison_table\": {\n        \"single_pass\": {\n          \"relaxed_f1\": 0.272,\n          \"api_calls\": 1\n        },\n        \"random_k14\": {\n          \"relaxed_f1\": 0.282,\n          \"api_calls\": 14\n        },\n        \"sdgd_zero_miniLM\": {\n          \"relaxed_f1\": 0.305,\n          \"api_calls\": 14\n        },\n        \"sdgd_cal\": {\n          \"relaxed_f1\": 0.318,\n          \"api_calls\": 24\n        },\n        \"per_type\": {\n          \"relaxed_f1\": 0.325,\n          \"api_calls\": 168\n        }\n      },\n      \"delta_sdgd_cal_vs_zero\": \"+1.3pp\",\n      \"delta_sdgd_cal_vs_singlepass\": \"+4.6pp\",\n      \"calibration_improvement_on_maven\": {\n        \"empirical_vs_miniLM_spearman\": 0.49,\n        \"verdict\": \"经验混淆信号在同质 schema 上增量更大，因为 embedding 信号更弱（MiniLM r=0.120）\"\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"Full Comparison Table: MAVEN (168 types)\",\n        \"columns\": [\n          \"Method\",\n          \"Relaxed F1\",\n          \"API calls\",\n          \"Δ vs single-pass\",\n          \"Latency ratio\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass\",\n            0.272,\n            1,\n            \"—\",\n            \"1.0x\"\n          ],\n          [\n            \"Random (k=14)\",\n            0.282,\n            14,\n            \"+1.0pp\",\n            \"5.3x\"\n          ],\n          [\n            \"SDGD-zero (MiniLM)\",\n            0.305,\n            14,\n            \"+3.3pp\",\n            \"5.3x\"\n          ],\n          [\n            \"SDGD-cal\",\n            0.318,\n            24,\n            \"+4.6pp\",\n            \"8.5x\"\n          ],\n          [\n            \"Per-type (k=168)\",\n            0.325,\n            168,\n            \"+5.3pp\",\n            \"40.0x\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MAVEN 完整对比表是论文 Table 3（或 4）的核心内容。SDGD-cal 在 Pareto 前沿上 明确优于 random 和 single-pass，接近 per-type 但成本大幅降低。 这完成了 Claim 3 的全部证据链：confusability-aware 分组在两个任务上均有效， 且 SDGD 框架提供了从 zero-shot 到 calibrated 的灵活选项。\\n\\n\\nMAVEN 上 SDGD-cal vs SDGD-zero 的增量（1.3pp）与 Few-NERD 的（1.9pp）相近， 因为 calibration data 在同质 schema 上的价值更高——MiniLM embedding 在 MAVEN 上 虽然 pairwise 信号显著但效应较弱（r=0.120 vs Few-NERD Qwen3 r=0.156）， 经验数据能更精确地识别实际高混淆对。 SDGD-cal（0.318）接近 per-type splitting（0.325）但 API calls 少 7x（24 vs 168）， 完成 SDGD 框架在效率/质量 tradeoff 上的定位。\\n\"\n  },\n  {\n    \"name\": \"Multi-model Validation (LLaMA-3.3-70B)\",\n    \"description\": \"用 LLaMA-3.3-70B-Instruct 在 Few-NERD 上复现 exp-002 协议： count curve + extreme/random batch + pairwise/per-type 分析。\\n\",\n    \"results\": {\n      \"count_curve\": {\n        \"count_1\": {\n          \"f1\": 0.298,\n          \"recall\": 0.612,\n          \"precision\": 0.198\n        },\n        \"count_6\": {\n          \"f1\": 0.275,\n          \"recall\": 0.445,\n          \"precision\": 0.2\n        },\n        \"count_12\": {\n          \"f1\": 0.318,\n          \"recall\": 0.312,\n          \"precision\": 0.324\n        },\n        \"count_22\": {\n          \"f1\": 0.282,\n          \"recall\": 0.258,\n          \"precision\": 0.311\n        },\n        \"count_44\": {\n          \"f1\": 0.405,\n          \"recall\": 0.37,\n          \"precision\": 0.447\n        },\n        \"count_64\": {\n          \"f1\": 0.378,\n          \"recall\": 0.288,\n          \"precision\": 0.548\n        }\n      },\n      \"pairwise_analysis\": {\n        \"qwen3_embedding\": {\n          \"n_pairs\": 1953,\n          \"pearson_r\": 0.138,\n          \"pearson_p\": 3.2e-09,\n          \"spearman_rho\": 0.144,\n          \"spearman_p\": 8.1e-10,\n          \"nonzero_spearman_rho\": 0.228,\n          \"nonzero_spearman_p\": 5.7e-05\n        },\n        \"miniLM_embedding\": {\n          \"pearson_r\": 0.072,\n          \"pearson_p\": 0.0015\n        }\n      },\n      \"per_type_analysis\": {\n        \"n_types\": 60,\n        \"filter\": \"freq>=5\",\n        \"qwen3_spearman_rho\": -0.265,\n        \"qwen3_spearman_p\": 0.041,\n        \"miniLM_spearman_rho\": -0.058,\n        \"miniLM_spearman_p\": 0.66\n      },\n      \"extreme_batch\": {\n        \"count_6_high_bcs_f1\": 0.195,\n        \"count_6_low_bcs_f1\": 0.342,\n        \"count_12_high_bcs_f1\": 0.215,\n        \"count_12_low_bcs_f1\": 0.398,\n        \"confusion_rate_ratio_count6\": 18.5,\n        \"confusion_rate_ratio_count12\": 12.3\n      },\n      \"cross_model_comparison\": {\n        \"qwen3_pairwise_r\": 0.156,\n        \"llama_pairwise_r\": 0.138,\n        \"delta\": -0.018,\n        \"both_significant\": true,\n        \"fisher_z_test_p\": 0.52,\n        \"verdict\": \"效应量无显著差异，two models 一致\"\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"Cross-model Pairwise Comparison on Few-NERD\",\n        \"columns\": [\n          \"Model\",\n          \"Embedding\",\n          \"Pearson r\",\n          \"p-value\",\n          \"Spearman ρ\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-32B\",\n            \"Qwen3\",\n            0.156,\n            \"4.6e-12\",\n            0.16,\n            \"1.3e-12\"\n          ],\n          [\n            \"LLaMA-3.3-70B\",\n            \"Qwen3\",\n            0.138,\n            \"3.2e-9\",\n            0.144,\n            \"8.1e-10\"\n          ],\n          [\n            \"Fisher z-test\",\n            \"—\",\n            \"Δ=0.018\",\n            \"p=0.52\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Cross-model Extreme Batch Confusion Rate\",\n        \"columns\": [\n          \"Model\",\n          \"Count\",\n          \"High-BCS rate\",\n          \"Low-BCS rate\",\n          \"Ratio\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-32B\",\n            6,\n            0.0728,\n            0.0014,\n            \"27.5x\"\n          ],\n          [\n            \"Qwen3-32B\",\n            12,\n            0.048,\n            0.0061,\n            \"9.9x\"\n          ],\n          [\n            \"LLaMA-70B\",\n            6,\n            0.0612,\n            0.0033,\n            \"18.5x\"\n          ],\n          [\n            \"LLaMA-70B\",\n            12,\n            0.0445,\n            0.0036,\n            \"12.3x\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Multi-model 验证完成 cross_model_significant: 2/2 的要求。两个差异显著的架构 （Qwen3-32B decoder vs LLaMA-3.3-70B decoder）在 pairwise confusability signal、 per-type direction、extreme batch effect 上全部一致，排除了单模型 artifact 的可能性。 Fisher z-test 的 p=0.52 确认两模型效应量无统计差异。 这是对 reviewer concern \\\"only one model\\\" 的完整回应。\\n\\n\\nLLaMA-3.3-70B 的 pairwise r=0.138 略低于 Qwen3 的 0.156，因为不同模型的 confusability 敏感度略有差异——LLaMA 的指令遵从能力更强（70B 参数 + Instruct 调优）， 可能在部分高 confusability pair 上仍能正确区分。但差异不显著（Fisher z p=0.52）， 确认 confusability signal 是跨模型稳定的现象。 Per-type ρ=-0.265（p=0.041）方向和显著性与 Qwen3（ρ=-0.293, p=0.020）一致， 说明 Few-NERD 的跨域 schema 结构使 per-type 信号在不同提取模型上均稳定。 Extreme batch confusion rate ratio 12-18x 与 Qwen3 的 10-28x 范围一致。 LLaMA 整体 F1 略低于 Qwen3（count_64: 0.378 vs 0.414），可能因为 LLaMA 的 NER 提示模板适配度稍差，但不影响 confusability 信号的相对模式。\\n\"\n  },\n  {\n    \"name\": \"Random Batching Ablation\",\n    \"description\": \"与 SDGD-zero 相同的 k=8 batch count，但 batch composition 完全随机。 5 次随机种子取平均。隔离 confusability-aware grouping 的贡献。\\n\",\n    \"results\": {\n      \"random_batching_results\": {\n        \"mean_f1\": 0.436,\n        \"std_f1\": 0.012,\n        \"mean_precision\": 0.53,\n        \"mean_recall\": 0.37,\n        \"n_api_calls\": 8,\n        \"n_random_seeds\": 5\n      },\n      \"comparison\": {\n        \"single_pass_f1\": 0.414,\n        \"sdgd_zero_f1\": 0.469,\n        \"random_f1\": 0.436,\n        \"delta_random_vs_singlepass\": \"+2.2pp\",\n        \"delta_sdgd_vs_random\": \"+3.3pp\",\n        \"delta_sdgd_vs_singlepass\": \"+5.5pp\"\n      },\n      \"decomposition\": {\n        \"count_reduction_contribution\": \"2.2pp (40% of total SDGD gain)\",\n        \"confusability_aware_contribution\": \"3.3pp (60% of total SDGD gain)\"\n      },\n      \"random_batch_bcs_stats\": {\n        \"mean_batch_bcs\": 0.838,\n        \"std_batch_bcs\": 0.025,\n        \"sdgd_mean_batch_bcs\": 0.762,\n        \"bcs_reduction_by_sdgd\": \"9.1%\"\n      },\n      \"type_confusion_rates\": {\n        \"random\": 0.031,\n        \"sdgd_zero\": 0.021,\n        \"single_pass\": 0.038\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"Ablation: SDGD-zero vs Random Batching vs Single-pass\",\n        \"columns\": [\n          \"Method\",\n          \"F1\",\n          \"Recall\",\n          \"Type confusion rate\",\n          \"Mean batch BCS\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass (k=1)\",\n            0.414,\n            0.304,\n            0.038,\n            0.847\n          ],\n          [\n            \"Random (k=8)\",\n            0.436,\n            0.37,\n            0.031,\n            0.838\n          ],\n          [\n            \"SDGD-zero (k=8)\",\n            0.469,\n            0.41,\n            0.021,\n            0.762\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是论文中最重要的 ablation。SDGD vs random（same k）的 +3.3pp gap（p < 0.01） 是 Claim 3 的充分必要证据——confusability-aware 分组本身有价值， SDGD 的收益不仅仅来自简单的 schema 分解。 5 次随机种子的 std=0.012 表明 random batching 的方差较小，SDGD-zero 的 0.469 显著高于随机分布的上界（0.436 + 2×0.012 = 0.460），排除了 lucky draw 的可能性。\\n\\n\\nRandom batching 获得 +2.2pp 改善（vs single-pass）完全来自 count reduction： 从 66 types/batch 降到 ~8 types/batch 减少了 attention dilution，提升了 recall。 但 random batch 的 mean BCS（0.838）接近 single-pass（0.847）， 因为随机分组不会系统性地分离 confusable pair。 SDGD-zero 的额外 +3.3pp 来自 confusability-aware grouping：mean batch BCS 降至 0.762， type confusion rate 从 0.031 降至 0.021（32% 减少）。 60%/40% 的贡献分解表明 confusability-aware grouping 是 SDGD 价值的主要来源， 而非简单的 batch count reduction。这是 Claim 3 最关键的证据—— SDGD 优于 random batching（same k）直接证明了 confusability-aware 分组的独立价值。\\n\"\n  },\n  {\n    \"name\": \"Per-type Splitting Ablation\",\n    \"description\": \"每个类型单独一个 batch（k=66），每次只提取一种类型。 UniNER-style 的上界实验。对比 SDGD 和 single-pass。\\n\",\n    \"results\": {\n      \"per_type_results\": {\n        \"f1\": 0.475,\n        \"precision\": 0.512,\n        \"recall\": 0.443,\n        \"n_api_calls\": 66,\n        \"wall_clock_minutes\": 68.5\n      },\n      \"comparison\": {\n        \"single_pass\": {\n          \"f1\": 0.414,\n          \"api_calls\": 1,\n          \"wall_clock\": 2.8\n        },\n        \"random_k8\": {\n          \"f1\": 0.436,\n          \"api_calls\": 8,\n          \"wall_clock\": 12.5\n        },\n        \"sdgd_zero\": {\n          \"f1\": 0.469,\n          \"api_calls\": 8,\n          \"wall_clock\": 12.5\n        },\n        \"sdgd_cal\": {\n          \"f1\": 0.488,\n          \"api_calls\": 17,\n          \"wall_clock\": 14.2\n        },\n        \"per_type\": {\n          \"f1\": 0.475,\n          \"api_calls\": 66,\n          \"wall_clock\": 68.5\n        }\n      },\n      \"sdgd_zero_vs_per_type\": {\n        \"f1_gap\": \"-0.6pp\",\n        \"api_calls_ratio\": \"8.25x fewer\",\n        \"wall_clock_ratio\": \"5.5x faster\",\n        \"verdict\": \"SDGD-zero 达到 per-type 的 98.7% F1，但成本仅 12%\"\n      },\n      \"sdgd_cal_vs_per_type\": {\n        \"f1_gap\": \"+1.3pp (SDGD-cal 更高)\",\n        \"api_calls_ratio\": \"3.9x fewer\",\n        \"verdict\": \"SDGD-cal 超过 per-type，因为保留了部分 cross-type 上下文\"\n      },\n      \"per_type_error_analysis\": {\n        \"type_confusion_rate\": 0.002,\n        \"false_negative_rate\": 0.31,\n        \"hallucination_rate\": 0.28,\n        \"boundary_error_rate\": 0.16,\n        \"note\": \"type confusion 几乎消除，但 hallucination 上升——单类型 prompt 缺乏跨类型约束\"\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"Full Method Comparison on Few-NERD (66 types)\",\n        \"columns\": [\n          \"Method\",\n          \"F1\",\n          \"P\",\n          \"R\",\n          \"API calls\",\n          \"Wall-clock\",\n          \"Efficiency\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass\",\n            0.414,\n            0.648,\n            0.304,\n            1,\n            \"2.8 min\",\n            \"baseline\"\n          ],\n          [\n            \"Random (k=8)\",\n            0.436,\n            0.53,\n            0.37,\n            8,\n            \"12.5 min\",\n            \"+2.2pp / 8 calls\"\n          ],\n          [\n            \"SDGD-zero (k=8)\",\n            0.469,\n            0.548,\n            0.41,\n            8,\n            \"12.5 min\",\n            \"+5.5pp / 8 calls\"\n          ],\n          [\n            \"Per-type (k=66)\",\n            0.475,\n            0.512,\n            0.443,\n            66,\n            \"68.5 min\",\n            \"+6.1pp / 66 calls\"\n          ],\n          [\n            \"SDGD-cal (k=9)\",\n            0.488,\n            0.556,\n            0.435,\n            17,\n            \"14.2 min\",\n            \"+7.4pp / 17 calls\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Per-type 实验揭示了一个反直觉的结果：最大分解≠最优分解。 SDGD-cal 超过 per-type 因为保留了 cross-type context 带来的消歧能力。 这使论文的 method 贡献更强——SDGD 不仅仅是\\\"把类型分开\\\"的简单策略， 而是在 confusability reduction 和 context preservation 之间的 principled tradeoff， graph coloring 框架正好 operationalize 了这个 tradeoff。 Pareto plot 是论文的核心 figure 之一：清晰展示 SDGD variants 在效率/质量空间的优势。\\n\\n\\nPer-type splitting 几乎消除了 type confusion（rate=0.002 vs single-pass 0.038）， 验证了 confusability 是可通过分组解决的。但 F1 只有 0.475，低于预期的\\\"上界\\\"， 因为存在两个反向效应： （1）缺乏 cross-type context：当只有一个类型时，模型无法利用\\\"这个 span 更像 X 而非 Y\\\"的对比信息， 导致某些模糊 span 被遗漏或被 hallucinate（hallucination rate 上升至 0.28）； （2）recall 上升到 0.443（最高），因为 attention 完全集中在单一类型上。 SDGD-zero（0.469）接近 per-type（0.475）的原因是：SDGD 的 8-type batch 保留了 有限但有用的 cross-type context，同时移除了大部分 confusability。 SDGD-cal（0.488）超过 per-type（0.475）是关键发现——证明 optimal decomposition 不是\\\"最大分解\\\"而是\\\"最优 confusability/context tradeoff\\\"，SDGD 框架正好在此定位。\\n\"\n  },\n  {\n    \"name\": \"SCS Proxy Validation\",\n    \"description\": \"用 exp-010 的经验 confusion matrix 作为 ground truth，验证 embedding SCS 作为 confusability proxy 的排序准确性。\\n\",\n    \"results\": {\n      \"qwen3_scs_vs_empirical\": {\n        \"spearman_rho\": 0.584,\n        \"spearman_p\": 2.3e-18,\n        \"kendall_tau\": 0.421,\n        \"kendall_p\": 8.1e-15,\n        \"top_20_overlap\": 0.85,\n        \"top_50_overlap\": 0.72\n      },\n      \"miniLM_scs_vs_empirical\": {\n        \"spearman_rho\": 0.432,\n        \"spearman_p\": 1.7e-10,\n        \"kendall_tau\": 0.312,\n        \"kendall_p\": 3.4e-08,\n        \"top_20_overlap\": 0.65,\n        \"top_50_overlap\": 0.54\n      },\n      \"precision_at_k\": {\n        \"qwen3_p_at_10\": 0.9,\n        \"qwen3_p_at_20\": 0.85,\n        \"qwen3_p_at_50\": 0.72,\n        \"miniLM_p_at_10\": 0.7,\n        \"miniLM_p_at_20\": 0.65,\n        \"miniLM_p_at_50\": 0.54\n      },\n      \"failure_modes\": {\n        \"false_positive_scs\": \"embedding 高相似但不混淆：通常是共享 supertype 但 subtype 名称足够区分\",\n        \"false_negative_scs\": \"embedding 低相似但实际混淆：通常因共现频率或 prompt 位置效应\"\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"SCS Proxy Validation\",\n        \"columns\": [\n          \"Embedding\",\n          \"Spearman ρ\",\n          \"Kendall τ\",\n          \"Top-20 overlap\",\n          \"P@10\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3\",\n            0.584,\n            0.421,\n            \"85%\",\n            0.9\n          ],\n          [\n            \"MiniLM\",\n            0.432,\n            0.312,\n            \"65%\",\n            0.7\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SCS validation 完成了 SDGD 框架的理论闭环：embedding SCS 是合理的 confusability proxy （ρ=0.58），但经验数据更好（SDGD-cal > SDGD-zero）。 论文的实用建议：cold-start 用 SDGD-zero（Qwen3 embedding）， 有少量 calibration data 后切换到 SDGD-cal。Qwen3 明显优于 MiniLM 作为 proxy 在 Few-NERD 上，但 MAVEN 上反转（→ 使用 task-appropriate embedding）。\\n\\nQwen3 SCS 与经验 confusability 的 Spearman ρ=0.584 表明 embedding 是合理但非完美的代理。 相关性显著但不为 1 的原因： （1）embedding 相似度捕获语义距离，而实际 confusion 还受 prompt 位置、类型名称字面相似性、 训练数据频率等非语义因素影响； （2）Qwen3 embedding 来自指令调优后的最后一层，保留了较多任务相关信息，因此优于 MiniLM。 Top-20 的 85% 重叠解释了为什么 SDGD-zero 已经很有效——最 confusable 的 pair 大多被正确识别。 SDGD-cal 的增量主要来自修正那 15% 的错误排序。 Precision@k 在 top-10 最高（0.90），说明 embedding proxy 在识别\\\"最危险\\\"pair 时最可靠。\\n\"\n  }\n]",
      "numLines": 1239,
      "startLine": 1,
      "totalLines": 1239
    }
  },
  "sourceToolAssistantUUID": "c40a0890-b088-4462-9923-8187a9e53a1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T113743 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extrac…",
  "leafUuid": "e56e4fb0-6209-4602-8be0-2c4eebba65db",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research paper from dream experiment data",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9"
}
```

---

### Assistant

_source line 14 · 2026-05-15T12:06:37.125Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both files. Let me also check if the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e56e4fb0-6209-4602-8be0-2c4eebba65db",
  "isSidechain": false,
  "requestId": "req_011Cb4KrDHtncAasxT4ct4zR",
  "type": "assistant",
  "uuid": "1deee48a-9359-4faa-949b-24d40ef8e0ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpuBE825TroV1W4LaJwTdB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3565,
      "cache_creation_input_tokens": 20300,
      "cache_read_input_tokens": 23055,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20300,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3565,
          "output_tokens": 168,
          "cache_read_input_tokens": 23055,
          "cache_creation_input_tokens": 20300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20300
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

_source line 15 · 2026-05-15T12:06:38.111Z_

I've read both input files. Let me check the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1deee48a-9359-4faa-949b-24d40ef8e0ed",
  "isSidechain": false,
  "requestId": "req_011Cb4KrDHtncAasxT4ct4zR",
  "type": "assistant",
  "uuid": "34c94b91-9bba-4224-bffa-cd877e8825fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpuBE825TroV1W4LaJwTdB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3565,
      "cache_creation_input_tokens": 20300,
      "cache_read_input_tokens": 23055,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20300,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3565,
          "output_tokens": 168,
          "cache_read_input_tokens": 23055,
          "cache_creation_input_tokens": 20300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20300
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

_source line 16 · 2026-05-15T12:06:40.170Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KgAFPUALdGbmF7f5zEmzf3`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/",
  "description": "List output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34c94b91-9bba-4224-bffa-cd877e8825fd",
  "isSidechain": false,
  "requestId": "req_011Cb4KrDHtncAasxT4ct4zR",
  "type": "assistant",
  "uuid": "27310550-d63d-403b-98cc-1f442be9b4a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpuBE825TroV1W4LaJwTdB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3565,
      "cache_creation_input_tokens": 20300,
      "cache_read_input_tokens": 23055,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20300,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3565,
          "output_tokens": 168,
          "cache_read_input_tokens": 23055,
          "cache_creation_input_tokens": 20300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20300
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

_source line 17 · 2026-05-15T12:06:40.336Z_

<details><summary>↩ Tool result · `toolu_01KgAFPUALdGbmF7f5zEmzf3`</summary>

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
  "parentUuid": "27310550-d63d-403b-98cc-1f442be9b4a9",
  "isSidechain": false,
  "promptId": "cdf92f18-0400-4c4f-90e5-485ecb947e5a",
  "type": "user",
  "uuid": "94989780-b352-4c66-90ae-50f74facfcda",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "27310550-d63d-403b-98cc-1f442be9b4a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-15T12:07:10.842Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to write a complete LaTeX paper. Let me carefully go through all the experiment data and paper framing to construct a coherent paper.

The paper has 3 core claims:
1. Confusability Independence - pairwise confusability predicts degradation across tasks/models
2. Multi-Channel Degradation - count→recall decline, confusability→type confusion (orthogonal)
3. SDGD Effectiveness - confusability-aware decomposition yields F1 gains

Experiments:
1. MAVEN Confusability Study - count curve + pairwise SCS→confusion


2. DocRED Confusability Study - count curve + pairwise analysis on RE
3. Count × Confusability Interaction (2×2) - factorial design on Few-NERD
4. Systematic Error Taxonomy - error type distribution by BCS quartile
5. SDGD-zero Few-NERD (R2) - SDGD vs single-pass
6. SDGD-zero MAVEN - cross-task validation
7. SDGD-cal Few-NERD - calibrated version
8. SDGD-cal MAVEN - calibrated cross-task
9. Multi-model Validation (LLaMA-3.3-70B) - cross-model replication
10. Random Batching Ablation - isolate confusability-aware grouping contribution
11. Per-type Splitting Ablation - upper bound comparison
12. SCS Proxy Validation - embedding vs empirical confusability

Now I'm mapping out the paper structure to organize these experiments into coherent sections. I'll group the confusability analysis work under one claim, then build toward the multi-channel degradation model, with ablations and validation studies supporting each major finding.

Writing the LaTeX paper now with the standard EMNLP format. I need to make sure I capture the key empirical results - the pairwise correlations from Few-NERD showing Qwen3 at r=0.156 and LLaMA at r=0.138, plus the MAVEN results with MiniLM at r=0.120 and Qwen3 near zero.

The factorial analysis shows strong effects with BCS at F=22.8 and count at F=14.2, and the error taxonomy reveals a dramatic shift in type substitution errors from 6.2% up to 38.4% across the BCS quartiles. For SDGD, the zero-shot results show solid improvements - Few-NERD jumping 5.5 percentage points to 0.469 and MAVEN gaining 3.3 points to 0.305 - while the calibrated version pushes even further with 7.4 and 4.6 point gains respectively. Random batching gives us a baseline of 0.436 to compare against.

Now I'm looking at the per-type performance where the calibrated SDGD at 0.488 exceeds the per-type baseline, and checking the multi-model correlation with LLaMA showing r=0.138 but no statistical significance at p=0.52. I'm going to write this up as a comprehensive paper using a standard article class with proper formatting.

Writing the paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94989780-b352-4c66-90ae-50f74facfcda",
  "isSidechain": false,
  "requestId": "req_011Cb4KrpiN626ZYHkdsNTxX",
  "type": "assistant",
  "uuid": "88d09cd7-8978-4a25-86a4-83a9af0c7b5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZdt4zzDPLKEgZxBadmda8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3763,
      "cache_read_input_tokens": 43355,
      "output_tokens": 12561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12561,
          "cache_read_input_tokens": 43355,
          "cache_creation_input_tokens": 3763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3763
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

_source line 19 · 2026-05-15T12:07:10.844Z_

Now I'll write the complete LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88d09cd7-8978-4a25-86a4-83a9af0c7b5c",
  "isSidechain": false,
  "requestId": "req_011Cb4KrpiN626ZYHkdsNTxX",
  "type": "assistant",
  "uuid": "d9da4d0a-0bb4-487d-807a-77713fd2a6b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZdt4zzDPLKEgZxBadmda8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3763,
      "cache_read_input_tokens": 43355,
      "output_tokens": 12561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12561,
          "cache_read_input_tokens": 43355,
          "cache_creation_input_tokens": 3763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3763
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

_source line 20 · 2026-05-15T12:10:33.148Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Dxdu21NQmiLq2e2TvLitvc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{url}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\n\\title{Pairwise Type Confusability Predicts Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction:\\\\Analysis and a Graph-Coloring Decomposition Framework}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%----------------------------------------------------------------------\n\\begin{abstract}\nTraining-free LLM-based information extraction (IE) degrades severely on complex schemas, yet the mechanisms driving this degradation remain poorly understood.\nWe conduct the first controlled empirical study isolating \\emph{type confusability} from \\emph{type count} as independent degradation factors across three IE tasks---named entity recognition (Few-NERD, 66 types), event detection (MAVEN, 168 types), and document-level relation extraction (DocRED, 96 types)---with two LLMs (Qwen3-32B and LLaMA-3.3-70B).\nWe establish three findings.\nFirst, pairwise type confusability, measured by embedding-based semantic similarity, independently predicts extraction quality degradation ($r{=}0.12$--$0.16$, $p{<}10^{-9}$), with high-confusability batches exhibiting $10$--$28\\times$ more type confusion errors.\nSecond, count and confusability degrade performance through orthogonal channels: count causes entity omission (recall decline) while confusability causes type substitution errors, as confirmed by a $2{\\times}2$ factorial design and systematic error taxonomy.\nThird, we propose \\textbf{Schema Decomposition via Graph Disentanglement (SDGD)}, a graph-coloring framework that partitions types into low-confusability batches.\nSDGD-zero improves F1 by $+5.5$ points on Few-NERD and $+3.3$ points on MAVEN over single-pass extraction, significantly outperforming random batching with the same number of API calls.\nSDGD-cal, using 8 calibration examples, achieves $+7.4$ F1 on Few-NERD, surpassing even per-type splitting while using $3.9{\\times}$ fewer API calls.\n\\end{abstract}\n\n%----------------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models (LLMs) have demonstrated strong zero-shot and few-shot information extraction capabilities, enabling deployment in domains where labeled data is scarce or annotation is prohibitively expensive---clinical text, regulatory documents, and low-resource languages.\nHowever, a persistent challenge in training-free LLM IE is \\emph{schema complexity}: as the number of target types grows beyond a handful, extraction quality degrades dramatically.\nPrior work reports 20--60 F1 point gaps between training-free and supervised approaches on complex schemas.\n\nExisting decomposition strategies address this degradation through ad-hoc heuristics.\nUniNER~splits schemas into single-type batches, gaining modest improvements but losing valuable cross-type context.\nLLM-PEE~uses embedding similarity as an implicit grouping criterion but never validates whether similarity actually predicts confusion.\nNo prior work has conducted controlled experiments to isolate \\emph{what} makes schemas complex for LLMs---specifically, whether the degradation stems from the \\emph{number} of types, the \\emph{semantic similarity} between co-present types, or both.\n\nIn this paper, we present the first controlled empirical study of schema-induced degradation in training-free LLM IE.\nOur experimental design isolates two candidate degradation factors---\\emph{type count} (how many types appear in a single prompt) and \\emph{type confusability} (how semantically similar co-present types are)---and measures their independent and joint effects.\n\nOur contributions are threefold:\n\\begin{enumerate}\n\\item \\textbf{Confusability as an independent degradation factor.}\nWe show that pairwise type confusability, operationalized as embedding cosine similarity between type-name representations, independently predicts extraction quality degradation across NER (Few-NERD), event detection (MAVEN), and relation extraction (DocRED), validated on two LLMs (Qwen3-32B, LLaMA-3.3-70B).\nThe signal is robust at the type-pair level ($r{=}0.12$--$0.16$), though per-type aggregation introduces a centrality confound in semantically homogeneous schemas.\n\n\\item \\textbf{A multi-channel degradation model.}\nWe demonstrate that count and confusability degrade extraction through orthogonal channels: count causes entity omission (recall decline) while confusability causes type substitution (precision decline on confused types).\nA $2{\\times}2$ factorial analysis confirms near-additive effects, and a systematic error taxonomy shows monotonic increases in type substitution errors with confusability ($6.2\\%{\\to}38.4\\%$ across BCS quartiles, $\\chi^2{=}89.4$, $p{<}10^{-16}$).\n\n\\item \\textbf{SDGD: a principled decomposition framework.}\nWe operationalize pairwise confusability into Schema Decomposition via Graph Disentanglement (SDGD), which constructs a confusability graph from pairwise similarity scores and partitions types via graph coloring.\nSDGD-zero (embedding-only) achieves $+5.5$ F1 over single-pass on Few-NERD and $+3.3$ on MAVEN; SDGD-cal (with 8 calibration examples) reaches $+7.4$ F1, surpassing per-type splitting while using $3.9{\\times}$ fewer API calls.\n\\end{enumerate}\n\n\n%----------------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Training-free LLM IE.}\nRecent work has explored using LLMs for NER, RE, and event extraction in zero-shot and few-shot settings.\nWhile LLMs show promising results on simple schemas (5--15 types), performance degrades substantially on complex schemas.\nThis has motivated decomposition approaches that break complex schemas into manageable subsets.\n\n\\paragraph{Schema decomposition.}\nUniNER proposes per-type extraction, processing one entity type at a time.\nThis eliminates inter-type confusion but sacrifices cross-type context and incurs linear API cost.\nLLM-PEE groups semantically similar types together, implicitly assuming similarity aids extraction---the opposite of our finding that similarity \\emph{hurts} through type confusion.\nNeither approach validates its grouping criterion empirically.\n\n\\paragraph{Confusability in NLP.}\nLabel confusion has been studied in classification tasks, where confusable classes degrade performance.\nOur work extends this to structured prediction (IE) and provides the first quantitative link between type-pair semantic similarity and extraction confusion in LLMs.\n\n\n%----------------------------------------------------------------------\n\\section{Methodology}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\nWe study training-free LLM IE: given a text $x$ and a schema $\\mathcal{S} = \\{t_1, \\ldots, t_n\\}$ of $n$ target types, the LLM produces structured extractions via prompting.\nWe investigate how extraction quality varies as a function of (a)~the number of types $n$ presented simultaneously, and (b)~the pairwise semantic similarity among co-present types.\n\n\\subsection{Schema Confusability Score (SCS)}\n\nWe define the \\textbf{Schema Confusability Score (SCS)} between two types $t_i, t_j$ as the cosine similarity of their embedding representations:\n\\begin{equation}\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\mathbf{e}(t_i),\\; \\mathbf{e}(t_j)\\bigr)\n\\end{equation}\nwhere $\\mathbf{e}(\\cdot)$ denotes a text embedding of the type name (and optionally its description).\nWe experiment with two embedding models: Qwen3 (instruction-tuned, 2048-dim) and MiniLM (general-purpose, 384-dim).\n\nFor a batch of types $B \\subseteq \\mathcal{S}$, the \\textbf{Batch Confusability Score (BCS)} is the maximum pairwise SCS within the batch:\n\\begin{equation}\n\\text{BCS}(B) = \\max_{t_i, t_j \\in B,\\; i \\neq j} \\text{SCS}(t_i, t_j)\n\\end{equation}\n\n\\subsection{Experimental Protocol}\n\nWe construct controlled experiments by varying batch composition while holding other factors constant.\n\\textbf{Count curves} vary $|B|$ from 1 to $|\\mathcal{S}|$.\n\\textbf{Extreme-batch comparisons} fix $|B|$ and construct high-BCS vs.\\ low-BCS batches.\n\\textbf{Factorial designs} cross count $\\times$ confusability levels.\nAll experiments use 500 evaluation samples per condition unless otherwise noted.\n\n\\subsection{Datasets and Models}\n\n\\begin{itemize}\n\\item \\textbf{Few-NERD}: Fine-grained NER with 66 types across 8 coarse domains. Cross-domain schema.\n\\item \\textbf{MAVEN}: Event detection with 168 event types from FrameNet hierarchy. Same-domain (homogeneous) schema.\n\\item \\textbf{DocRED}: Document-level RE with 96 relation types. Mixed-domain schema.\n\\item \\textbf{Extraction models}: Qwen3-32B-Instruct (primary), LLaMA-3.3-70B-Instruct (validation).\n\\end{itemize}\n\n\n%----------------------------------------------------------------------\n\\section{Confusability Analysis}\n\\label{sec:analysis}\n\n\\subsection{Count Curves}\n\\label{sec:count-curves}\n\nTable~\\ref{tab:maven-count} shows the MAVEN count curve.\nAs type count increases from 1 to 168, relaxed F1 increases from $0.118$ to $0.272$---an \\emph{inverted} pattern compared to Few-NERD, where F1 decreases with count.\nThis inversion occurs because MAVEN's 168 same-domain types benefit from cross-type contextual cues at moderate counts, while Few-NERD's cross-domain types interfere.\nExact F1 remains extremely low ($<0.02$) due to event trigger boundary matching difficulty, which does not affect our confusability analysis (conducted on relaxed F1).\n\nDocRED shows the expected monotonic decline: F1 drops from $0.195$ (count 1) to $0.098$ (count 96), consistent with the attention dilution hypothesis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{MAVEN count curve (Qwen3-32B, 500 samples).}\n\\label{tab:maven-count}\n\\begin{tabular}{lcccccc}\n\\toprule\nCount & 1 & 6 & 12 & 22 & 44 & 64 \\\\\n\\midrule\nRelaxed F1 & .118 & .142 & .178 & .210 & .248 & .261 \\\\\nExact F1   & .011 & .005 & .010 & .015 & .020 & .016 \\\\\nRecall     & .210 & .185 & .210 & .238 & .268 & .275 \\\\\nPrecision  & .082 & .115 & .154 & .188 & .231 & .249 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Pairwise Confusability Predicts Confusion}\n\\label{sec:pairwise}\n\nOur central hypothesis is that semantically similar type pairs are more frequently confused by LLMs.\nTable~\\ref{tab:pairwise-cross} summarizes pairwise SCS--confusion correlations across datasets and embeddings.\n\nOn Few-NERD, Qwen3 embeddings yield $r{=}0.156$ ($p{=}4.6{\\times}10^{-12}$, $n{=}1{,}953$ pairs) for Qwen3-32B extraction, and $r{=}0.138$ ($p{=}3.2{\\times}10^{-9}$) for LLaMA-3.3-70B extraction.\nA Fisher $z$-test confirms no significant difference between models ($p{=}0.52$).\n\nOn MAVEN, MiniLM embeddings yield $r{=}0.120$ ($p{=}1.2{\\times}10^{-45}$, $n{=}14{,}028$ pairs), demonstrating cross-task replication on a same-domain schema.\nNotably, Qwen3 embeddings fail on MAVEN ($r{=}{-}0.007$, $p{=}0.41$), indicating that embedding choice is task-dependent.\n\nOn DocRED, MiniLM yields $r{=}0.108$ ($p{=}3.5{\\times}10^{-13}$, $n{=}4{,}560$ pairs) and Qwen3 yields $r{=}0.095$ ($p{=}2.1{\\times}10^{-10}$).\nThe weaker effect on DocRED is consistent with longer document contexts providing additional disambiguation cues.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pairwise SCS $\\to$ confusion correlation across tasks and embeddings. All correlations use Pearson $r$.}\n\\label{tab:pairwise-cross}\n\\begin{tabular}{llccc}\n\\toprule\nDataset & Embedding & $r$ & $p$-value & $n_{\\text{pairs}}$ \\\\\n\\midrule\n\\multirow{2}{*}{Few-NERD (Qwen3-32B)} & Qwen3  & 0.156 & $4.6{\\times}10^{-12}$ & 1,953 \\\\\n                                        & MiniLM & 0.072 & 0.0015 & 1,953 \\\\\n\\midrule\n\\multirow{2}{*}{Few-NERD (LLaMA-70B)}  & Qwen3  & 0.138 & $3.2{\\times}10^{-9}$ & 1,953 \\\\\n                                        & MiniLM & 0.072 & 0.0015 & 1,953 \\\\\n\\midrule\n\\multirow{2}{*}{MAVEN}                 & MiniLM & 0.120 & $1.2{\\times}10^{-45}$ & 14,028 \\\\\n                                        & Qwen3  & $-$0.007 & 0.41 & 14,028 \\\\\n\\midrule\n\\multirow{2}{*}{DocRED}                & MiniLM & 0.108 & $3.5{\\times}10^{-13}$ & 4,560 \\\\\n                                        & Qwen3  & 0.095 & $2.1{\\times}10^{-10}$ & 4,560 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Model Validation}\n\\label{sec:multimodel}\n\nTo rule out single-model artifacts, we replicate the full Few-NERD analysis protocol on LLaMA-3.3-70B-Instruct (Table~\\ref{tab:cross-model}).\nThe pairwise signal is consistent: $r{=}0.138$ (Qwen3 embedding) vs.\\ $r{=}0.156$ for Qwen3-32B (Fisher $z$-test $p{=}0.52$).\nExtreme-batch confusion rate ratios are $18.5\\times$ (count 6) and $12.3\\times$ (count 12) for LLaMA, compared to $27.5\\times$ and $9.9\\times$ for Qwen3-32B---same order of magnitude.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model pairwise comparison on Few-NERD (Qwen3 embeddings).}\n\\label{tab:cross-model}\n\\begin{tabular}{lcccc}\n\\toprule\nModel & Pearson $r$ & Spearman $\\rho$ & $p$-value & Fisher $z$ \\\\\n\\midrule\nQwen3-32B     & 0.156 & 0.160 & $1.3{\\times}10^{-12}$ & \\multirow{2}{*}{$p{=}0.52$} \\\\\nLLaMA-3.3-70B & 0.138 & 0.144 & $8.1{\\times}10^{-10}$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Centrality Confound in Homogeneous Schemas}\n\\label{sec:centrality}\n\nAn important methodological finding concerns the failure of \\emph{per-type aggregation} on semantically homogeneous schemas.\nOn MAVEN, per-type mean BCS correlates \\emph{positively} with F1 for both MiniLM ($\\rho{=}0.208$, $p{=}0.011$) and Qwen3 ($\\rho{=}0.189$, $p{=}0.021$)---opposite to the confusability hypothesis.\n\nWe identify the cause as a \\textbf{centrality confound}: in homogeneous schemas, types with high mean BCS are semantic network hubs (e.g., ``Attack'', ``Meeting'') that appear frequently in training data.\nThe LLM's stronger prior for these central types yields higher F1, masking the pairwise confusability effect.\nWe verify this by showing $r{=}0.34$ ($p{=}2.1{\\times}10^{-5}$) between mean BCS and type frequency.\n\nCrucially, pairwise confusability ($r{=}0.120$ with MiniLM) remains valid even when per-type aggregation fails, because pairwise analysis operates on individual type pairs rather than averaging over the neighborhood.\nThis finding motivates SDGD's pairwise design (Section~\\ref{sec:sdgd}).\n\n\n%----------------------------------------------------------------------\n\\section{Multi-Channel Degradation}\n\\label{sec:multichannel}\n\n\\subsection{Factorial Analysis}\n\\label{sec:factorial}\n\nWe construct a $2{\\times}2$ factorial design on Few-NERD crossing count ($\\{6, 22\\}$) with confusability ($\\{$low BCS, high BCS$\\}$), each cell containing 10 batches (Table~\\ref{tab:factorial}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$2{\\times}2$ factorial F1 results on Few-NERD. Interaction effect is marginally significant ($p{=}0.087$).}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Low BCS & High BCS & BCS effect \\\\\n\\midrule\nLow count (6)  & 0.372 & 0.268 & $-$0.104 \\\\\nHigh count (22) & 0.312 & 0.178 & $-$0.134 \\\\\n\\midrule\nCount effect & $-$0.060 & $-$0.090 & \\textit{int.: $-$0.027} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo-way ANOVA reveals significant main effects for both count ($F{=}14.2$, $p{=}0.0006$) and BCS ($F{=}22.8$, $p{=}3.1{\\times}10^{-5}$).\nThe interaction is marginally significant ($F{=}3.1$, $p{=}0.087$), with slight super-additivity: the observed F1 for high-count/high-BCS is $0.178$, compared to the additive prediction of $0.197$ (gap $= -0.019$).\nThe BCS main effect ($\\Delta{=}{-}0.119$) exceeds the count main effect ($\\Delta{=}{-}0.075$), indicating confusability is the stronger degradation factor on Few-NERD.\n\nType confusion rates reinforce this pattern: high-BCS batches show $4.0$--$5.6\\times$ more confusion errors regardless of count (Table~\\ref{tab:confusion-rate}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Type confusion rates in the $2{\\times}2$ factorial design.}\n\\label{tab:confusion-rate}\n\\begin{tabular}{lccc}\n\\toprule\n & Low BCS & High BCS & Ratio \\\\\n\\midrule\nLow count (6)  & 0.008 & 0.045 & 5.6$\\times$ \\\\\nHigh count (22) & 0.018 & 0.072 & 4.0$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Error Taxonomy}\n\\label{sec:taxonomy}\n\nTo characterize the degradation mechanism, we classify all false positive errors into four categories: \\emph{type substitution} (correct span, wrong type), \\emph{boundary error} (overlapping span, correct type), \\emph{false negative} (missed entity), and \\emph{hallucination} (fabricated entity).\nTable~\\ref{tab:error-taxonomy} shows the distribution across BCS quartiles on Few-NERD.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Error type distribution (\\%) by BCS quartile on Few-NERD. $\\chi^2{=}89.4$, $p{=}1.2{\\times}10^{-16}$, $df{=}9$.}\n\\label{tab:error-taxonomy}\n\\begin{tabular}{lcccc|c}\n\\toprule\nBCS quartile & Type sub. & Boundary & False neg. & Halluc. & Total \\\\\n\\midrule\nQ1 (low)  &  6.2 & 14.8 & 58.3 & 20.7 & 385 \\\\\nQ2        & 12.5 & 13.2 & 51.8 & 22.5 & 412 \\\\\nQ3        & 22.1 & 11.9 & 44.6 & 21.4 & 448 \\\\\nQ4 (high) & 38.4 & 10.5 & 32.3 & 18.8 & 521 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nType substitution increases monotonically from $6.2\\%$ (Q1) to $38.4\\%$ (Q4), a $6.2\\times$ ratio (Kendall $\\tau{=}0.92$).\nFalse negatives decrease monotonically from $58.3\\%$ to $32.3\\%$ ($\\tau{=}{-}0.88$).\nBoundary errors and hallucinations show no significant trend with BCS.\n\nThis pattern precisely matches the multi-channel model:\n\\begin{itemize}\n\\item \\textbf{Channel 1 (Count $\\to$ Omission)}: Higher type counts dilute attention, increasing false negatives.\n\\item \\textbf{Channel 2 (Confusability $\\to$ Substitution)}: Higher confusability increases type confusion---the model correctly identifies entity spans but assigns semantically neighboring types.\n\\end{itemize}\n\nThe monotonic trends are reinforced at different count levels: at count 12, Q4 type substitution reaches $44.7\\%$ (vs.\\ $31.2\\%$ at count 6), because more co-present confusable types amplify the cumulative interference.\n\n\n\\subsection{Extreme-Batch Confusability Effects}\n\\label{sec:extreme}\n\nOn MAVEN, extreme-batch comparisons (fixing count, varying BCS) show large performance gaps:\nat count 6, high-BCS batches achieve relaxed F1 $= 0.218$ vs.\\ low-BCS $= 0.098$;\nat count 12, high-BCS $= 0.192$ vs.\\ low-BCS $= 0.114$.\nThe confusion rate ratio between extreme groups reaches $8.2\\times$ (count 6) and $6.5\\times$ (count 12).\n\nOn Few-NERD with LLaMA-3.3-70B, the pattern replicates: low-BCS batches achieve F1 $= 0.342$ vs.\\ high-BCS $= 0.195$ at count 6 ($\\Delta{=}14.7$pp), and $0.398$ vs.\\ $0.215$ at count 12 ($\\Delta{=}18.3$pp).\n\nThese results demonstrate that confusability effects are large, consistent across tasks and models, and practically significant.\n\n%----------------------------------------------------------------------\n\\section{SDGD: Schema Decomposition via Graph Disentanglement}\n\\label{sec:sdgd}\n\n\\subsection{Method}\n\nHaving established that pairwise confusability independently degrades extraction and operates through a distinct channel (type substitution), we propose \\textbf{Schema Decomposition via Graph Disentanglement (SDGD)}.\n\n\\paragraph{Step 1: Confusability Graph Construction.}\nGiven schema $\\mathcal{S}$ and embedding function $\\mathbf{e}(\\cdot)$, construct an undirected graph $G = (\\mathcal{S}, E)$ where $(t_i, t_j) \\in E$ iff $\\text{SCS}(t_i, t_j) > \\tau$.\nThe threshold $\\tau$ is set to the 90th percentile of the pairwise SCS distribution.\n\n\\paragraph{Step 2: Graph Coloring.}\nApply greedy graph coloring to $G$, producing $k$ color classes $\\{B_1, \\ldots, B_k\\}$.\nTypes assigned the same color are guaranteed to have pairwise SCS $\\leq \\tau$, minimizing within-batch confusability.\n\n\\paragraph{Step 3: Batch Extraction \\& Merge.}\nRun independent LLM extraction on each batch $B_i$, then merge results via span-level confidence deduplication:\nwhen multiple batches produce predictions for the same text span, retain the highest-confidence prediction.\n\n\\paragraph{Variants.}\n\\textbf{SDGD-zero} uses embedding SCS directly as the confusability proxy.\n\\textbf{SDGD-cal} first runs a small number of calibration examples (e.g., 8) to build an empirical confusion matrix, replacing SCS with observed confusion rates.\n\n\n\\subsection{SCS Proxy Validation}\n\\label{sec:proxy}\n\nBefore evaluating SDGD, we validate whether embedding SCS is a reasonable proxy for empirical confusability.\nUsing the SDGD-cal confusion matrix as ground truth on Few-NERD (Table~\\ref{tab:proxy-valid}), Qwen3 SCS achieves Spearman $\\rho{=}0.584$ ($p{<}10^{-18}$) with empirical confusion, and $85\\%$ overlap in the top-20 most confusable pairs (P@10 $= 0.90$).\nMiniLM is weaker ($\\rho{=}0.432$, top-20 overlap $= 65\\%$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SCS proxy validation: embedding SCS vs.\\ empirical confusion matrix (Few-NERD).}\n\\label{tab:proxy-valid}\n\\begin{tabular}{lcccc}\n\\toprule\nEmbedding & Spearman $\\rho$ & Kendall $\\tau$ & Top-20 overlap & P@10 \\\\\n\\midrule\nQwen3  & 0.584 & 0.421 & 85\\% & 0.90 \\\\\nMiniLM & 0.432 & 0.312 & 65\\% & 0.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe imperfect correlation ($\\rho{<}1$) explains why SDGD-cal outperforms SDGD-zero: empirical confusion captures non-semantic factors (prompt position effects, training data frequency) that embeddings miss.\n\n\n\\subsection{SDGD Results on Few-NERD}\n\\label{sec:sdgd-fewnerd}\n\nTable~\\ref{tab:fewnerd-full} presents the full method comparison on Few-NERD (66 types).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Full method comparison on Few-NERD (66 types, Qwen3-32B).}\n\\label{tab:fewnerd-full}\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & F1 & P & R & API calls & Wall-clock \\\\\n\\midrule\nSingle-pass       & 0.414 & 0.648 & 0.304 & 1  & 2.8 min \\\\\nRandom ($k{=}8$)  & 0.436 & 0.530 & 0.370 & 8  & 12.5 min \\\\\nSDGD-zero ($k{=}8$) & 0.469 & 0.548 & 0.410 & 8  & 12.5 min \\\\\nPer-type ($k{=}66$)  & 0.475 & 0.512 & 0.443 & 66 & 68.5 min \\\\\nSDGD-cal ($k{=}9$)  & \\textbf{0.488} & 0.556 & 0.435 & 17 & 14.2 min \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKey observations:\n\\begin{itemize}\n\\item \\textbf{SDGD-zero vs.\\ single-pass}: $+5.5$ F1 pp ($p{=}0.003$), with $+10.6$pp recall improvement offset by $-10.0$pp precision decline. The recall gain reflects reduced attention dilution; the precision decline comes from merge artifacts across 8 batches.\n\\item \\textbf{SDGD-zero vs.\\ random batching}: $+3.3$ F1 pp at the same API cost ($k{=}8$). This gap isolates the value of confusability-aware grouping from simple schema decomposition.\n\\item \\textbf{SDGD-cal vs.\\ per-type}: $+1.3$ F1 pp with $3.9\\times$ fewer API calls. SDGD-cal \\emph{exceeds} per-type splitting because it preserves beneficial cross-type context while eliminating high-confusability co-occurrences.\n\\item \\textbf{Type confusion rate}: SDGD-zero reduces type confusion by $44.7\\%$ relative to single-pass ($0.021$ vs.\\ $0.038$), directly demonstrating Channel 2 mitigation.\n\\end{itemize}\n\n\n\\subsection{SDGD Results on MAVEN}\n\\label{sec:sdgd-maven}\n\nTable~\\ref{tab:maven-full} shows MAVEN results (168 types).\nSDGD uses MiniLM embeddings, which yield significant pairwise signal on MAVEN ($r{=}0.120$), unlike Qwen3 ($r{=}{-}0.007$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Full comparison on MAVEN (168 types, Qwen3-32B, MiniLM embeddings).}\n\\label{tab:maven-full}\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Rel.\\ F1 & Exact F1 & API calls & $\\Delta$ Rel.\\ F1 & Latency \\\\\n\\midrule\nSingle-pass         & 0.272 & 0.014 & 1   & ---     & 1.0$\\times$ \\\\\nRandom ($k{=}14$)   & 0.282 & 0.017 & 14  & +1.0pp  & 5.3$\\times$ \\\\\nSDGD-zero ($k{=}14$)& 0.305 & 0.022 & 14  & +3.3pp  & 5.3$\\times$ \\\\\nSDGD-cal            & 0.318 & 0.025 & 24  & +4.6pp  & 8.5$\\times$ \\\\\nPer-type ($k{=}168$) & 0.325 & ---   & 168 & +5.3pp  & 40.0$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSDGD-zero significantly outperforms both single-pass ($+3.3$pp, $p{=}0.012$) and random batching ($+2.3$pp, $p{=}0.038$).\nSDGD-cal approaches per-type performance ($0.318$ vs.\\ $0.325$) with $7\\times$ fewer API calls.\nType confusion reduction is $39.7\\%$ ($0.035$ vs.\\ $0.058$).\n\nThe smaller gains on MAVEN vs.\\ Few-NERD ($+3.3$ vs.\\ $+5.5$pp) are expected: MAVEN's concentrated SCS distribution offers less ``separation space'' for graph coloring, and some count-context benefit is lost when batches shrink from 168 to 12 types.\n\n\n\\subsection{Ablation: Random Batching}\n\\label{sec:ablation-random}\n\nThe random batching ablation (Table~\\ref{tab:ablation}) decomposes SDGD's total gain into count-reduction and confusability-aware contributions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ablation: SDGD-zero vs.\\ random batching vs.\\ single-pass on Few-NERD.}\n\\label{tab:ablation}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & F1 & Recall & Confusion rate & Mean BCS \\\\\n\\midrule\nSingle-pass ($k{=}1$) & 0.414 & 0.304 & 0.038 & 0.847 \\\\\nRandom ($k{=}8$)      & 0.436 & 0.370 & 0.031 & 0.838 \\\\\nSDGD-zero ($k{=}8$)   & 0.469 & 0.410 & 0.021 & 0.762 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOf SDGD-zero's total $+5.5$pp F1 gain over single-pass:\n\\begin{itemize}\n\\item $+2.2$pp ($40\\%$) comes from count reduction alone (random batching vs.\\ single-pass).\n\\item $+3.3$pp ($60\\%$) comes from confusability-aware grouping (SDGD-zero vs.\\ random).\n\\end{itemize}\n\nRandom batching barely reduces mean batch BCS ($0.838$ vs.\\ $0.847$), because random assignment does not systematically separate confusable pairs.\nSDGD-zero reduces BCS to $0.762$ ($-10\\%$), which translates to a $32\\%$ reduction in type confusion rate ($0.021$ vs.\\ $0.031$).\nSDGD-zero's F1 ($0.469$) exceeds the upper bound of random batching's distribution ($\\mu + 2\\sigma = 0.436 + 0.024 = 0.460$, over 5 seeds with $\\sigma{=}0.012$), confirming the result is not a ``lucky draw.''\n\n\n\\subsection{Ablation: Per-Type Splitting}\n\\label{sec:ablation-pertype}\n\nPer-type splitting ($k{=}66$) achieves F1 $= 0.475$---only $+0.6$pp above SDGD-zero ($0.469$) but at $8.25\\times$ the API cost.\nNotably, SDGD-cal ($0.488$) \\emph{surpasses} per-type splitting by $+1.3$pp.\n\nPer-type splitting nearly eliminates type confusion (rate $= 0.002$) but introduces new failure modes:\nhallucination rate increases to $28\\%$ (vs.\\ $\\sim\\!21\\%$ in batched conditions) because single-type prompts lack cross-type constraints that suppress spurious predictions.\nThis reveals that \\textbf{optimal decomposition $\\neq$ maximum decomposition}: the best strategy balances confusability reduction with context preservation.\nSDGD's graph coloring naturally achieves this balance---types are grouped if and only if they are below the confusability threshold.\n\n\n\\subsection{SDGD Variant Comparison}\n\\label{sec:sdgd-variants}\n\nTable~\\ref{tab:sdgd-variants} summarizes SDGD-zero vs.\\ SDGD-cal on both datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SDGD variant comparison across datasets.}\n\\label{tab:sdgd-variants}\n\\begin{tabular}{llccc}\n\\toprule\nDataset & Method & F1 & $\\Delta$ vs.\\ SP & API calls \\\\\n\\midrule\n\\multirow{2}{*}{Few-NERD} & SDGD-zero & 0.469 & +5.5pp & 8 \\\\\n                          & SDGD-cal  & 0.488 & +7.4pp & 17 \\\\\n\\midrule\n\\multirow{2}{*}{MAVEN}    & SDGD-zero & 0.305 & +3.3pp & 14 \\\\\n                          & SDGD-cal  & 0.318 & +4.6pp & 24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSDGD-cal's marginal improvement over SDGD-zero ($+1.9$pp on Few-NERD, $+1.3$pp on MAVEN) comes from replacing the embedding proxy with empirical confusion data.\nThe Spearman correlation between empirical confusability and Qwen3 SCS is $0.58$ (Few-NERD) and $0.49$ (MAVEN/MiniLM), explaining both why SDGD-zero is effective (the proxy captures most of the signal) and why SDGD-cal improves further (it corrects the $\\sim\\!15\\%$ of misordered pairs).\n\nSDGD-zero captures $74\\%$ of SDGD-cal's total gain on Few-NERD ($5.5/7.4$) and $72\\%$ on MAVEN ($3.3/4.6$), making it the recommended default for cold-start scenarios without calibration data.\n\n\n%----------------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Practical implications.}\nSDGD provides a practical, principled alternative to ad-hoc schema decomposition.\nFor schemas with ${\\geq}30$ types, SDGD-zero offers substantial F1 gains at moderate API cost ($k{=}8$--$14$ calls vs.\\ $66$--$168$ for per-type splitting).\nWhen even a handful of calibration examples are available, SDGD-cal further improves performance while remaining efficient.\n\n\\paragraph{Embedding selection.}\nNo single embedding universally captures confusability.\nOn cross-domain schemas (Few-NERD), instruction-tuned Qwen3 embeddings are superior (P@10 $= 0.90$).\nOn same-domain homogeneous schemas (MAVEN), generic MiniLM embeddings are more effective.\nSDGD-cal sidesteps this choice entirely by using empirical confusion data.\nWe recommend starting with SDGD-zero using the extraction model's own embeddings, falling back to generic embeddings if the pairwise signal is weak.\n\n\\paragraph{Limitations.}\nOur pairwise effect sizes are modest ($r{=}0.12$--$0.16$), reflecting the many non-confusability factors that influence extraction quality (prompt design, few-shot examples, input text difficulty).\nThe $2{\\times}2$ interaction effect is only marginally significant ($p{=}0.087$), preventing definitive conclusions about super-additivity.\nOur study covers three IE tasks but only two extraction models; further validation on encoder-based LLMs and multilingual settings is warranted.\nSDGD's latency overhead ($5$--$8\\times$ wall-clock time) may be prohibitive for latency-sensitive applications.\n\n\\paragraph{Centrality confound as a methodological contribution.}\nOur discovery that per-type confusability aggregation fails on homogeneous schemas due to centrality confounding has implications beyond this work.\nAny method that ranks types by average similarity to other types (a common heuristic) risks conflating type centrality with type confusability when the schema lacks clear domain boundaries.\nWe recommend that future work on schema complexity operate at the pairwise level.\n\n\n%----------------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first controlled study of schema-induced degradation in training-free LLM information extraction, establishing three findings:\n(1)~pairwise type confusability independently predicts extraction degradation across NER, event detection, and relation extraction ($r{=}0.12$--$0.16$);\n(2)~count and confusability degrade performance through orthogonal channels---omission and type substitution, respectively;\n(3)~SDGD, a graph-coloring decomposition framework operating on pairwise confusability, yields $+5.5$ F1 on Few-NERD and $+3.3$ on MAVEN over single-pass extraction, with $60\\%$ of the gain attributable to confusability-aware grouping rather than simple count reduction.\nOur analysis additionally reveals a centrality confound in per-type confusability aggregation on homogeneous schemas, motivating pairwise approaches.\n\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Ding et al.(2021)]{fewnerd}\nN.~Ding, G.~Xu, Y.~Chen, et al.\n\\newblock Few-NERD: A few-shot named entity recognition dataset.\n\\newblock In \\emph{Proc. ACL}, 2021.\n\n\\bibitem[Wang et al.(2023)]{maven}\nX.~Wang, Z.~Wang, et al.\n\\newblock MAVEN: A massive general domain event detection dataset.\n\\newblock In \\emph{Proc. EMNLP}, 2020.\n\n\\bibitem[Yao et al.(2019)]{docred}\nY.~Yao, D.~Ye, P.~Li, et al.\n\\newblock DocRED: A large-scale document-level relation extraction dataset.\n\\newblock In \\emph{Proc. ACL}, 2019.\n\n\\bibitem[Zhou et al.(2023)]{uniner}\nW.~Zhou, S.~Zhang, Y.~Gu, M.~Chen, and H.~Peng.\n\\newblock UniNER: Universal named entity recognition with instruction-following large language models.\n\\newblock \\emph{arXiv preprint arXiv:2308.03279}, 2023.\n\n\\bibitem[Liu et al.(2024)]{lost-middle}\nN.~F.~Liu, K.~Lin, J.~Hewitt, A.~Paranjape, M.~Bevilacqua, F.~Petroni, and P.~Liang.\n\\newblock Lost in the middle: How language models use long contexts.\n\\newblock \\emph{TACL}, 2024.\n\n\\bibitem[Wei et al.(2023)]{llmpee}\nX.~Wei, J.~Cui, N.~Cheng, et al.\n\\newblock Zero-shot information extraction via chatting with ChatGPT.\n\\newblock \\emph{arXiv preprint arXiv:2302.10205}, 2023.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9da4d0a-0bb4-487d-807a-77713fd2a6b4",
  "isSidechain": false,
  "requestId": "req_011Cb4KrpiN626ZYHkdsNTxX",
  "type": "assistant",
  "uuid": "eed1d72f-3a34-4dda-bf14-a749ded8d55d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZdt4zzDPLKEgZxBadmda8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3763,
      "cache_read_input_tokens": 43355,
      "output_tokens": 12561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12561,
          "cache_read_input_tokens": 43355,
          "cache_creation_input_tokens": 3763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3763
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

_source line 21 · 2026-05-15T12:10:33.167Z_

<details><summary>↩ Tool result · `toolu_01Dxdu21NQmiLq2e2TvLitvc`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eed1d72f-3a34-4dda-bf14-a749ded8d55d",
  "isSidechain": false,
  "promptId": "cdf92f18-0400-4c4f-90e5-485ecb947e5a",
  "type": "user",
  "uuid": "b40514be-e979-4254-b7a7-d56a0f10b887",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{url}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\n\\title{Pairwise Type Confusability Predicts Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction:\\\\Analysis and a Graph-Coloring Decomposition Framework}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%----------------------------------------------------------------------\n\\begin{abstract}\nTraining-free LLM-based information extraction (IE) degrades severely on complex schemas, yet the mechanisms driving this degradation remain poorly understood.\nWe conduct the first controlled empirical study isolating \\emph{type confusability} from \\emph{type count} as independent degradation factors across three IE tasks---named entity recognition (Few-NERD, 66 types), event detection (MAVEN, 168 types), and document-level relation extraction (DocRED, 96 types)---with two LLMs (Qwen3-32B and LLaMA-3.3-70B).\nWe establish three findings.\nFirst, pairwise type confusability, measured by embedding-based semantic similarity, independently predicts extraction quality degradation ($r{=}0.12$--$0.16$, $p{<}10^{-9}$), with high-confusability batches exhibiting $10$--$28\\times$ more type confusion errors.\nSecond, count and confusability degrade performance through orthogonal channels: count causes entity omission (recall decline) while confusability causes type substitution errors, as confirmed by a $2{\\times}2$ factorial design and systematic error taxonomy.\nThird, we propose \\textbf{Schema Decomposition via Graph Disentanglement (SDGD)}, a graph-coloring framework that partitions types into low-confusability batches.\nSDGD-zero improves F1 by $+5.5$ points on Few-NERD and $+3.3$ points on MAVEN over single-pass extraction, significantly outperforming random batching with the same number of API calls.\nSDGD-cal, using 8 calibration examples, achieves $+7.4$ F1 on Few-NERD, surpassing even per-type splitting while using $3.9{\\times}$ fewer API calls.\n\\end{abstract}\n\n%----------------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models (LLMs) have demonstrated strong zero-shot and few-shot information extraction capabilities, enabling deployment in domains where labeled data is scarce or annotation is prohibitively expensive---clinical text, regulatory documents, and low-resource languages.\nHowever, a persistent challenge in training-free LLM IE is \\emph{schema complexity}: as the number of target types grows beyond a handful, extraction quality degrades dramatically.\nPrior work reports 20--60 F1 point gaps between training-free and supervised approaches on complex schemas.\n\nExisting decomposition strategies address this degradation through ad-hoc heuristics.\nUniNER~splits schemas into single-type batches, gaining modest improvements but losing valuable cross-type context.\nLLM-PEE~uses embedding similarity as an implicit grouping criterion but never validates whether similarity actually predicts confusion.\nNo prior work has conducted controlled experiments to isolate \\emph{what} makes schemas complex for LLMs---specifically, whether the degradation stems from the \\emph{number} of types, the \\emph{semantic similarity} between co-present types, or both.\n\nIn this paper, we present the first controlled empirical study of schema-induced degradation in training-free LLM IE.\nOur experimental design isolates two candidate degradation factors---\\emph{type count} (how many types appear in a single prompt) and \\emph{type confusability} (how semantically similar co-present types are)---and measures their independent and joint effects.\n\nOur contributions are threefold:\n\\begin{enumerate}\n\\item \\textbf{Confusability as an independent degradation factor.}\nWe show that pairwise type confusability, operationalized as embedding cosine similarity between type-name representations, independently predicts extraction quality degradation across NER (Few-NERD), event detection (MAVEN), and relation extraction (DocRED), validated on two LLMs (Qwen3-32B, LLaMA-3.3-70B).\nThe signal is robust at the type-pair level ($r{=}0.12$--$0.16$), though per-type aggregation introduces a centrality confound in semantically homogeneous schemas.\n\n\\item \\textbf{A multi-channel degradation model.}\nWe demonstrate that count and confusability degrade extraction through orthogonal channels: count causes entity omission (recall decline) while confusability causes type substitution (precision decline on confused types).\nA $2{\\times}2$ factorial analysis confirms near-additive effects, and a systematic error taxonomy shows monotonic increases in type substitution errors with confusability ($6.2\\%{\\to}38.4\\%$ across BCS quartiles, $\\chi^2{=}89.4$, $p{<}10^{-16}$).\n\n\\item \\textbf{SDGD: a principled decomposition framework.}\nWe operationalize pairwise confusability into Schema Decomposition via Graph Disentanglement (SDGD), which constructs a confusability graph from pairwise similarity scores and partitions types via graph coloring.\nSDGD-zero (embedding-only) achieves $+5.5$ F1 over single-pass on Few-NERD and $+3.3$ on MAVEN; SDGD-cal (with 8 calibration examples) reaches $+7.4$ F1, surpassing per-type splitting while using $3.9{\\times}$ fewer API calls.\n\\end{enumerate}\n\n\n%----------------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Training-free LLM IE.}\nRecent work has explored using LLMs for NER, RE, and event extraction in zero-shot and few-shot settings.\nWhile LLMs show promising results on simple schemas (5--15 types), performance degrades substantially on complex schemas.\nThis has motivated decomposition approaches that break complex schemas into manageable subsets.\n\n\\paragraph{Schema decomposition.}\nUniNER proposes per-type extraction, processing one entity type at a time.\nThis eliminates inter-type confusion but sacrifices cross-type context and incurs linear API cost.\nLLM-PEE groups semantically similar types together, implicitly assuming similarity aids extraction---the opposite of our finding that similarity \\emph{hurts} through type confusion.\nNeither approach validates its grouping criterion empirically.\n\n\\paragraph{Confusability in NLP.}\nLabel confusion has been studied in classification tasks, where confusable classes degrade performance.\nOur work extends this to structured prediction (IE) and provides the first quantitative link between type-pair semantic similarity and extraction confusion in LLMs.\n\n\n%----------------------------------------------------------------------\n\\section{Methodology}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\nWe study training-free LLM IE: given a text $x$ and a schema $\\mathcal{S} = \\{t_1, \\ldots, t_n\\}$ of $n$ target types, the LLM produces structured extractions via prompting.\nWe investigate how extraction quality varies as a function of (a)~the number of types $n$ presented simultaneously, and (b)~the pairwise semantic similarity among co-present types.\n\n\\subsection{Schema Confusability Score (SCS)}\n\nWe define the \\textbf{Schema Confusability Score (SCS)} between two types $t_i, t_j$ as the cosine similarity of their embedding representations:\n\\begin{equation}\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\mathbf{e}(t_i),\\; \\mathbf{e}(t_j)\\bigr)\n\\end{equation}\nwhere $\\mathbf{e}(\\cdot)$ denotes a text embedding of the type name (and optionally its description).\nWe experiment with two embedding models: Qwen3 (instruction-tuned, 2048-dim) and MiniLM (general-purpose, 384-dim).\n\nFor a batch of types $B \\subseteq \\mathcal{S}$, the \\textbf{Batch Confusability Score (BCS)} is the maximum pairwise SCS within the batch:\n\\begin{equation}\n\\text{BCS}(B) = \\max_{t_i, t_j \\in B,\\; i \\neq j} \\text{SCS}(t_i, t_j)\n\\end{equation}\n\n\\subsection{Experimental Protocol}\n\nWe construct controlled experiments by varying batch composition while holding other factors constant.\n\\textbf{Count curves} vary $|B|$ from 1 to $|\\mathcal{S}|$.\n\\textbf{Extreme-batch comparisons} fix $|B|$ and construct high-BCS vs.\\ low-BCS batches.\n\\textbf{Factorial designs} cross count $\\times$ confusability levels.\nAll experiments use 500 evaluation samples per condition unless otherwise noted.\n\n\\subsection{Datasets and Models}\n\n\\begin{itemize}\n\\item \\textbf{Few-NERD}: Fine-grained NER with 66 types across 8 coarse domains. Cross-domain schema.\n\\item \\textbf{MAVEN}: Event detection with 168 event types from FrameNet hierarchy. Same-domain (homogeneous) schema.\n\\item \\textbf{DocRED}: Document-level RE with 96 relation types. Mixed-domain schema.\n\\item \\textbf{Extraction models}: Qwen3-32B-Instruct (primary), LLaMA-3.3-70B-Instruct (validation).\n\\end{itemize}\n\n\n%----------------------------------------------------------------------\n\\section{Confusability Analysis}\n\\label{sec:analysis}\n\n\\subsection{Count Curves}\n\\label{sec:count-curves}\n\nTable~\\ref{tab:maven-count} shows the MAVEN count curve.\nAs type count increases from 1 to 168, relaxed F1 increases from $0.118$ to $0.272$---an \\emph{inverted} pattern compared to Few-NERD, where F1 decreases with count.\nThis inversion occurs because MAVEN's 168 same-domain types benefit from cross-type contextual cues at moderate counts, while Few-NERD's cross-domain types interfere.\nExact F1 remains extremely low ($<0.02$) due to event trigger boundary matching difficulty, which does not affect our confusability analysis (conducted on relaxed F1).\n\nDocRED shows the expected monotonic decline: F1 drops from $0.195$ (count 1) to $0.098$ (count 96), consistent with the attention dilution hypothesis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{MAVEN count curve (Qwen3-32B, 500 samples).}\n\\label{tab:maven-count}\n\\begin{tabular}{lcccccc}\n\\toprule\nCount & 1 & 6 & 12 & 22 & 44 & 64 \\\\\n\\midrule\nRelaxed F1 & .118 & .142 & .178 & .210 & .248 & .261 \\\\\nExact F1   & .011 & .005 & .010 & .015 & .020 & .016 \\\\\nRecall     & .210 & .185 & .210 & .238 & .268 & .275 \\\\\nPrecision  & .082 & .115 & .154 & .188 & .231 & .249 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Pairwise Confusability Predicts Confusion}\n\\label{sec:pairwise}\n\nOur central hypothesis is that semantically similar type pairs are more frequently confused by LLMs.\nTable~\\ref{tab:pairwise-cross} summarizes pairwise SCS--confusion correlations across datasets and embeddings.\n\nOn Few-NERD, Qwen3 embeddings yield $r{=}0.156$ ($p{=}4.6{\\times}10^{-12}$, $n{=}1{,}953$ pairs) for Qwen3-32B extraction, and $r{=}0.138$ ($p{=}3.2{\\times}10^{-9}$) for LLaMA-3.3-70B extraction.\nA Fisher $z$-test confirms no significant difference between models ($p{=}0.52$).\n\nOn MAVEN, MiniLM embeddings yield $r{=}0.120$ ($p{=}1.2{\\times}10^{-45}$, $n{=}14{,}028$ pairs), demonstrating cross-task replication on a same-domain schema.\nNotably, Qwen3 embeddings fail on MAVEN ($r{=}{-}0.007$, $p{=}0.41$), indicating that embedding choice is task-dependent.\n\nOn DocRED, MiniLM yields $r{=}0.108$ ($p{=}3.5{\\times}10^{-13}$, $n{=}4{,}560$ pairs) and Qwen3 yields $r{=}0.095$ ($p{=}2.1{\\times}10^{-10}$).\nThe weaker effect on DocRED is consistent with longer document contexts providing additional disambiguation cues.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pairwise SCS $\\to$ confusion correlation across tasks and embeddings. All correlations use Pearson $r$.}\n\\label{tab:pairwise-cross}\n\\begin{tabular}{llccc}\n\\toprule\nDataset & Embedding & $r$ & $p$-value & $n_{\\text{pairs}}$ \\\\\n\\midrule\n\\multirow{2}{*}{Few-NERD (Qwen3-32B)} & Qwen3  & 0.156 & $4.6{\\times}10^{-12}$ & 1,953 \\\\\n                                        & MiniLM & 0.072 & 0.0015 & 1,953 \\\\\n\\midrule\n\\multirow{2}{*}{Few-NERD (LLaMA-70B)}  & Qwen3  & 0.138 & $3.2{\\times}10^{-9}$ & 1,953 \\\\\n                                        & MiniLM & 0.072 & 0.0015 & 1,953 \\\\\n\\midrule\n\\multirow{2}{*}{MAVEN}                 & MiniLM & 0.120 & $1.2{\\times}10^{-45}$ & 14,028 \\\\\n                                        & Qwen3  & $-$0.007 & 0.41 & 14,028 \\\\\n\\midrule\n\\multirow{2}{*}{DocRED}                & MiniLM & 0.108 & $3.5{\\times}10^{-13}$ & 4,560 \\\\\n                                        & Qwen3  & 0.095 & $2.1{\\times}10^{-10}$ & 4,560 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Model Validation}\n\\label{sec:multimodel}\n\nTo rule out single-model artifacts, we replicate the full Few-NERD analysis protocol on LLaMA-3.3-70B-Instruct (Table~\\ref{tab:cross-model}).\nThe pairwise signal is consistent: $r{=}0.138$ (Qwen3 embedding) vs.\\ $r{=}0.156$ for Qwen3-32B (Fisher $z$-test $p{=}0.52$).\nExtreme-batch confusion rate ratios are $18.5\\times$ (count 6) and $12.3\\times$ (count 12) for LLaMA, compared to $27.5\\times$ and $9.9\\times$ for Qwen3-32B---same order of magnitude.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model pairwise comparison on Few-NERD (Qwen3 embeddings).}\n\\label{tab:cross-model}\n\\begin{tabular}{lcccc}\n\\toprule\nModel & Pearson $r$ & Spearman $\\rho$ & $p$-value & Fisher $z$ \\\\\n\\midrule\nQwen3-32B     & 0.156 & 0.160 & $1.3{\\times}10^{-12}$ & \\multirow{2}{*}{$p{=}0.52$} \\\\\nLLaMA-3.3-70B & 0.138 & 0.144 & $8.1{\\times}10^{-10}$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Centrality Confound in Homogeneous Schemas}\n\\label{sec:centrality}\n\nAn important methodological finding concerns the failure of \\emph{per-type aggregation} on semantically homogeneous schemas.\nOn MAVEN, per-type mean BCS correlates \\emph{positively} with F1 for both MiniLM ($\\rho{=}0.208$, $p{=}0.011$) and Qwen3 ($\\rho{=}0.189$, $p{=}0.021$)---opposite to the confusability hypothesis.\n\nWe identify the cause as a \\textbf{centrality confound}: in homogeneous schemas, types with high mean BCS are semantic network hubs (e.g., ``Attack'', ``Meeting'') that appear frequently in training data.\nThe LLM's stronger prior for these central types yields higher F1, masking the pairwise confusability effect.\nWe verify this by showing $r{=}0.34$ ($p{=}2.1{\\times}10^{-5}$) between mean BCS and type frequency.\n\nCrucially, pairwise confusability ($r{=}0.120$ with MiniLM) remains valid even when per-type aggregation fails, because pairwise analysis operates on individual type pairs rather than averaging over the neighborhood.\nThis finding motivates SDGD's pairwise design (Section~\\ref{sec:sdgd}).\n\n\n%----------------------------------------------------------------------\n\\section{Multi-Channel Degradation}\n\\label{sec:multichannel}\n\n\\subsection{Factorial Analysis}\n\\label{sec:factorial}\n\nWe construct a $2{\\times}2$ factorial design on Few-NERD crossing count ($\\{6, 22\\}$) with confusability ($\\{$low BCS, high BCS$\\}$), each cell containing 10 batches (Table~\\ref{tab:factorial}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$2{\\times}2$ factorial F1 results on Few-NERD. Interaction effect is marginally significant ($p{=}0.087$).}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Low BCS & High BCS & BCS effect \\\\\n\\midrule\nLow count (6)  & 0.372 & 0.268 & $-$0.104 \\\\\nHigh count (22) & 0.312 & 0.178 & $-$0.134 \\\\\n\\midrule\nCount effect & $-$0.060 & $-$0.090 & \\textit{int.: $-$0.027} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo-way ANOVA reveals significant main effects for both count ($F{=}14.2$, $p{=}0.0006$) and BCS ($F{=}22.8$, $p{=}3.1{\\times}10^{-5}$).\nThe interaction is marginally significant ($F{=}3.1$, $p{=}0.087$), with slight super-additivity: the observed F1 for high-count/high-BCS is $0.178$, compared to the additive prediction of $0.197$ (gap $= -0.019$).\nThe BCS main effect ($\\Delta{=}{-}0.119$) exceeds the count main effect ($\\Delta{=}{-}0.075$), indicating confusability is the stronger degradation factor on Few-NERD.\n\nType confusion rates reinforce this pattern: high-BCS batches show $4.0$--$5.6\\times$ more confusion errors regardless of count (Table~\\ref{tab:confusion-rate}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Type confusion rates in the $2{\\times}2$ factorial design.}\n\\label{tab:confusion-rate}\n\\begin{tabular}{lccc}\n\\toprule\n & Low BCS & High BCS & Ratio \\\\\n\\midrule\nLow count (6)  & 0.008 & 0.045 & 5.6$\\times$ \\\\\nHigh count (22) & 0.018 & 0.072 & 4.0$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Error Taxonomy}\n\\label{sec:taxonomy}\n\nTo characterize the degradation mechanism, we classify all false positive errors into four categories: \\emph{type substitution} (correct span, wrong type), \\emph{boundary error} (overlapping span, correct type), \\emph{false negative} (missed entity), and \\emph{hallucination} (fabricated entity).\nTable~\\ref{tab:error-taxonomy} shows the distribution across BCS quartiles on Few-NERD.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Error type distribution (\\%) by BCS quartile on Few-NERD. $\\chi^2{=}89.4$, $p{=}1.2{\\times}10^{-16}$, $df{=}9$.}\n\\label{tab:error-taxonomy}\n\\begin{tabular}{lcccc|c}\n\\toprule\nBCS quartile & Type sub. & Boundary & False neg. & Halluc. & Total \\\\\n\\midrule\nQ1 (low)  &  6.2 & 14.8 & 58.3 & 20.7 & 385 \\\\\nQ2        & 12.5 & 13.2 & 51.8 & 22.5 & 412 \\\\\nQ3        & 22.1 & 11.9 & 44.6 & 21.4 & 448 \\\\\nQ4 (high) & 38.4 & 10.5 & 32.3 & 18.8 & 521 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nType substitution increases monotonically from $6.2\\%$ (Q1) to $38.4\\%$ (Q4), a $6.2\\times$ ratio (Kendall $\\tau{=}0.92$).\nFalse negatives decrease monotonically from $58.3\\%$ to $32.3\\%$ ($\\tau{=}{-}0.88$).\nBoundary errors and hallucinations show no significant trend with BCS.\n\nThis pattern precisely matches the multi-channel model:\n\\begin{itemize}\n\\item \\textbf{Channel 1 (Count $\\to$ Omission)}: Higher type counts dilute attention, increasing false negatives.\n\\item \\textbf{Channel 2 (Confusability $\\to$ Substitution)}: Higher confusability increases type confusion---the model correctly identifies entity spans but assigns semantically neighboring types.\n\\end{itemize}\n\nThe monotonic trends are reinforced at different count levels: at count 12, Q4 type substitution reaches $44.7\\%$ (vs.\\ $31.2\\%$ at count 6), because more co-present confusable types amplify the cumulative interference.\n\n\n\\subsection{Extreme-Batch Confusability Effects}\n\\label{sec:extreme}\n\nOn MAVEN, extreme-batch comparisons (fixing count, varying BCS) show large performance gaps:\nat count 6, high-BCS batches achieve relaxed F1 $= 0.218$ vs.\\ low-BCS $= 0.098$;\nat count 12, high-BCS $= 0.192$ vs.\\ low-BCS $= 0.114$.\nThe confusion rate ratio between extreme groups reaches $8.2\\times$ (count 6) and $6.5\\times$ (count 12).\n\nOn Few-NERD with LLaMA-3.3-70B, the pattern replicates: low-BCS batches achieve F1 $= 0.342$ vs.\\ high-BCS $= 0.195$ at count 6 ($\\Delta{=}14.7$pp), and $0.398$ vs.\\ $0.215$ at count 12 ($\\Delta{=}18.3$pp).\n\nThese results demonstrate that confusability effects are large, consistent across tasks and models, and practically significant.\n\n%----------------------------------------------------------------------\n\\section{SDGD: Schema Decomposition via Graph Disentanglement}\n\\label{sec:sdgd}\n\n\\subsection{Method}\n\nHaving established that pairwise confusability independently degrades extraction and operates through a distinct channel (type substitution), we propose \\textbf{Schema Decomposition via Graph Disentanglement (SDGD)}.\n\n\\paragraph{Step 1: Confusability Graph Construction.}\nGiven schema $\\mathcal{S}$ and embedding function $\\mathbf{e}(\\cdot)$, construct an undirected graph $G = (\\mathcal{S}, E)$ where $(t_i, t_j) \\in E$ iff $\\text{SCS}(t_i, t_j) > \\tau$.\nThe threshold $\\tau$ is set to the 90th percentile of the pairwise SCS distribution.\n\n\\paragraph{Step 2: Graph Coloring.}\nApply greedy graph coloring to $G$, producing $k$ color classes $\\{B_1, \\ldots, B_k\\}$.\nTypes assigned the same color are guaranteed to have pairwise SCS $\\leq \\tau$, minimizing within-batch confusability.\n\n\\paragraph{Step 3: Batch Extraction \\& Merge.}\nRun independent LLM extraction on each batch $B_i$, then merge results via span-level confidence deduplication:\nwhen multiple batches produce predictions for the same text span, retain the highest-confidence prediction.\n\n\\paragraph{Variants.}\n\\textbf{SDGD-zero} uses embedding SCS directly as the confusability proxy.\n\\textbf{SDGD-cal} first runs a small number of calibration examples (e.g., 8) to build an empirical confusion matrix, replacing SCS with observed confusion rates.\n\n\n\\subsection{SCS Proxy Validation}\n\\label{sec:proxy}\n\nBefore evaluating SDGD, we validate whether embedding SCS is a reasonable proxy for empirical confusability.\nUsing the SDGD-cal confusion matrix as ground truth on Few-NERD (Table~\\ref{tab:proxy-valid}), Qwen3 SCS achieves Spearman $\\rho{=}0.584$ ($p{<}10^{-18}$) with empirical confusion, and $85\\%$ overlap in the top-20 most confusable pairs (P@10 $= 0.90$).\nMiniLM is weaker ($\\rho{=}0.432$, top-20 overlap $= 65\\%$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SCS proxy validation: embedding SCS vs.\\ empirical confusion matrix (Few-NERD).}\n\\label{tab:proxy-valid}\n\\begin{tabular}{lcccc}\n\\toprule\nEmbedding & Spearman $\\rho$ & Kendall $\\tau$ & Top-20 overlap & P@10 \\\\\n\\midrule\nQwen3  & 0.584 & 0.421 & 85\\% & 0.90 \\\\\nMiniLM & 0.432 & 0.312 & 65\\% & 0.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe imperfect correlation ($\\rho{<}1$) explains why SDGD-cal outperforms SDGD-zero: empirical confusion captures non-semantic factors (prompt position effects, training data frequency) that embeddings miss.\n\n\n\\subsection{SDGD Results on Few-NERD}\n\\label{sec:sdgd-fewnerd}\n\nTable~\\ref{tab:fewnerd-full} presents the full method comparison on Few-NERD (66 types).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Full method comparison on Few-NERD (66 types, Qwen3-32B).}\n\\label{tab:fewnerd-full}\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & F1 & P & R & API calls & Wall-clock \\\\\n\\midrule\nSingle-pass       & 0.414 & 0.648 & 0.304 & 1  & 2.8 min \\\\\nRandom ($k{=}8$)  & 0.436 & 0.530 & 0.370 & 8  & 12.5 min \\\\\nSDGD-zero ($k{=}8$) & 0.469 & 0.548 & 0.410 & 8  & 12.5 min \\\\\nPer-type ($k{=}66$)  & 0.475 & 0.512 & 0.443 & 66 & 68.5 min \\\\\nSDGD-cal ($k{=}9$)  & \\textbf{0.488} & 0.556 & 0.435 & 17 & 14.2 min \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKey observations:\n\\begin{itemize}\n\\item \\textbf{SDGD-zero vs.\\ single-pass}: $+5.5$ F1 pp ($p{=}0.003$), with $+10.6$pp recall improvement offset by $-10.0$pp precision decline. The recall gain reflects reduced attention dilution; the precision decline comes from merge artifacts across 8 batches.\n\\item \\textbf{SDGD-zero vs.\\ random batching}: $+3.3$ F1 pp at the same API cost ($k{=}8$). This gap isolates the value of confusability-aware grouping from simple schema decomposition.\n\\item \\textbf{SDGD-cal vs.\\ per-type}: $+1.3$ F1 pp with $3.9\\times$ fewer API calls. SDGD-cal \\emph{exceeds} per-type splitting because it preserves beneficial cross-type context while eliminating high-confusability co-occurrences.\n\\item \\textbf{Type confusion rate}: SDGD-zero reduces type confusion by $44.7\\%$ relative to single-pass ($0.021$ vs.\\ $0.038$), directly demonstrating Channel 2 mitigation.\n\\end{itemize}\n\n\n\\subsection{SDGD Results on MAVEN}\n\\label{sec:sdgd-maven}\n\nTable~\\ref{tab:maven-full} shows MAVEN results (168 types).\nSDGD uses MiniLM embeddings, which yield significant pairwise signal on MAVEN ($r{=}0.120$), unlike Qwen3 ($r{=}{-}0.007$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Full comparison on MAVEN (168 types, Qwen3-32B, MiniLM embeddings).}\n\\label{tab:maven-full}\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Rel.\\ F1 & Exact F1 & API calls & $\\Delta$ Rel.\\ F1 & Latency \\\\\n\\midrule\nSingle-pass         & 0.272 & 0.014 & 1   & ---     & 1.0$\\times$ \\\\\nRandom ($k{=}14$)   & 0.282 & 0.017 & 14  & +1.0pp  & 5.3$\\times$ \\\\\nSDGD-zero ($k{=}14$)& 0.305 & 0.022 & 14  & +3.3pp  & 5.3$\\times$ \\\\\nSDGD-cal            & 0.318 & 0.025 & 24  & +4.6pp  & 8.5$\\times$ \\\\\nPer-type ($k{=}168$) & 0.325 & ---   & 168 & +5.3pp  & 40.0$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSDGD-zero significantly outperforms both single-pass ($+3.3$pp, $p{=}0.012$) and random batching ($+2.3$pp, $p{=}0.038$).\nSDGD-cal approaches per-type performance ($0.318$ vs.\\ $0.325$) with $7\\times$ fewer API calls.\nType confusion reduction is $39.7\\%$ ($0.035$ vs.\\ $0.058$).\n\nThe smaller gains on MAVEN vs.\\ Few-NERD ($+3.3$ vs.\\ $+5.5$pp) are expected: MAVEN's concentrated SCS distribution offers less ``separation space'' for graph coloring, and some count-context benefit is lost when batches shrink from 168 to 12 types.\n\n\n\\subsection{Ablation: Random Batching}\n\\label{sec:ablation-random}\n\nThe random batching ablation (Table~\\ref{tab:ablation}) decomposes SDGD's total gain into count-reduction and confusability-aware contributions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ablation: SDGD-zero vs.\\ random batching vs.\\ single-pass on Few-NERD.}\n\\label{tab:ablation}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & F1 & Recall & Confusion rate & Mean BCS \\\\\n\\midrule\nSingle-pass ($k{=}1$) & 0.414 & 0.304 & 0.038 & 0.847 \\\\\nRandom ($k{=}8$)      & 0.436 & 0.370 & 0.031 & 0.838 \\\\\nSDGD-zero ($k{=}8$)   & 0.469 & 0.410 & 0.021 & 0.762 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOf SDGD-zero's total $+5.5$pp F1 gain over single-pass:\n\\begin{itemize}\n\\item $+2.2$pp ($40\\%$) comes from count reduction alone (random batching vs.\\ single-pass).\n\\item $+3.3$pp ($60\\%$) comes from confusability-aware grouping (SDGD-zero vs.\\ random).\n\\end{itemize}\n\nRandom batching barely reduces mean batch BCS ($0.838$ vs.\\ $0.847$), because random assignment does not systematically separate confusable pairs.\nSDGD-zero reduces BCS to $0.762$ ($-10\\%$), which translates to a $32\\%$ reduction in type confusion rate ($0.021$ vs.\\ $0.031$).\nSDGD-zero's F1 ($0.469$) exceeds the upper bound of random batching's distribution ($\\mu + 2\\sigma = 0.436 + 0.024 = 0.460$, over 5 seeds with $\\sigma{=}0.012$), confirming the result is not a ``lucky draw.''\n\n\n\\subsection{Ablation: Per-Type Splitting}\n\\label{sec:ablation-pertype}\n\nPer-type splitting ($k{=}66$) achieves F1 $= 0.475$---only $+0.6$pp above SDGD-zero ($0.469$) but at $8.25\\times$ the API cost.\nNotably, SDGD-cal ($0.488$) \\emph{surpasses} per-type splitting by $+1.3$pp.\n\nPer-type splitting nearly eliminates type confusion (rate $= 0.002$) but introduces new failure modes:\nhallucination rate increases to $28\\%$ (vs.\\ $\\sim\\!21\\%$ in batched conditions) because single-type prompts lack cross-type constraints that suppress spurious predictions.\nThis reveals that \\textbf{optimal decomposition $\\neq$ maximum decomposition}: the best strategy balances confusability reduction with context preservation.\nSDGD's graph coloring naturally achieves this balance---types are grouped if and only if they are below the confusability threshold.\n\n\n\\subsection{SDGD Variant Comparison}\n\\label{sec:sdgd-variants}\n\nTable~\\ref{tab:sdgd-variants} summarizes SDGD-zero vs.\\ SDGD-cal on both datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SDGD variant comparison across datasets.}\n\\label{tab:sdgd-variants}\n\\begin{tabular}{llccc}\n\\toprule\nDataset & Method & F1 & $\\Delta$ vs.\\ SP & API calls \\\\\n\\midrule\n\\multirow{2}{*}{Few-NERD} & SDGD-zero & 0.469 & +5.5pp & 8 \\\\\n                          & SDGD-cal  & 0.488 & +7.4pp & 17 \\\\\n\\midrule\n\\multirow{2}{*}{MAVEN}    & SDGD-zero & 0.305 & +3.3pp & 14 \\\\\n                          & SDGD-cal  & 0.318 & +4.6pp & 24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSDGD-cal's marginal improvement over SDGD-zero ($+1.9$pp on Few-NERD, $+1.3$pp on MAVEN) comes from replacing the embedding proxy with empirical confusion data.\nThe Spearman correlation between empirical confusability and Qwen3 SCS is $0.58$ (Few-NERD) and $0.49$ (MAVEN/MiniLM), explaining both why SDGD-zero is effective (the proxy captures most of the signal) and why SDGD-cal improves further (it corrects the $\\sim\\!15\\%$ of misordered pairs).\n\nSDGD-zero captures $74\\%$ of SDGD-cal's total gain on Few-NERD ($5.5/7.4$) and $72\\%$ on MAVEN ($3.3/4.6$), making it the recommended default for cold-start scenarios without calibration data.\n\n\n%----------------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Practical implications.}\nSDGD provides a practical, principled alternative to ad-hoc schema decomposition.\nFor schemas with ${\\geq}30$ types, SDGD-zero offers substantial F1 gains at moderate API cost ($k{=}8$--$14$ calls vs.\\ $66$--$168$ for per-type splitting).\nWhen even a handful of calibration examples are available, SDGD-cal further improves performance while remaining efficient.\n\n\\paragraph{Embedding selection.}\nNo single embedding universally captures confusability.\nOn cross-domain schemas (Few-NERD), instruction-tuned Qwen3 embeddings are superior (P@10 $= 0.90$).\nOn same-domain homogeneous schemas (MAVEN), generic MiniLM embeddings are more effective.\nSDGD-cal sidesteps this choice entirely by using empirical confusion data.\nWe recommend starting with SDGD-zero using the extraction model's own embeddings, falling back to generic embeddings if the pairwise signal is weak.\n\n\\paragraph{Limitations.}\nOur pairwise effect sizes are modest ($r{=}0.12$--$0.16$), reflecting the many non-confusability factors that influence extraction quality (prompt design, few-shot examples, input text difficulty).\nThe $2{\\times}2$ interaction effect is only marginally significant ($p{=}0.087$), preventing definitive conclusions about super-additivity.\nOur study covers three IE tasks but only two extraction models; further validation on encoder-based LLMs and multilingual settings is warranted.\nSDGD's latency overhead ($5$--$8\\times$ wall-clock time) may be prohibitive for latency-sensitive applications.\n\n\\paragraph{Centrality confound as a methodological contribution.}\nOur discovery that per-type confusability aggregation fails on homogeneous schemas due to centrality confounding has implications beyond this work.\nAny method that ranks types by average similarity to other types (a common heuristic) risks conflating type centrality with type confusability when the schema lacks clear domain boundaries.\nWe recommend that future work on schema complexity operate at the pairwise level.\n\n\n%----------------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first controlled study of schema-induced degradation in training-free LLM information extraction, establishing three findings:\n(1)~pairwise type confusability independently predicts extraction degradation across NER, event detection, and relation extraction ($r{=}0.12$--$0.16$);\n(2)~count and confusability degrade performance through orthogonal channels---omission and type substitution, respectively;\n(3)~SDGD, a graph-coloring decomposition framework operating on pairwise confusability, yields $+5.5$ F1 on Few-NERD and $+3.3$ on MAVEN over single-pass extraction, with $60\\%$ of the gain attributable to confusability-aware grouping rather than simple count reduction.\nOur analysis additionally reveals a centrality confound in per-type confusability aggregation on homogeneous schemas, motivating pairwise approaches.\n\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Ding et al.(2021)]{fewnerd}\nN.~Ding, G.~Xu, Y.~Chen, et al.\n\\newblock Few-NERD: A few-shot named entity recognition dataset.\n\\newblock In \\emph{Proc. ACL}, 2021.\n\n\\bibitem[Wang et al.(2023)]{maven}\nX.~Wang, Z.~Wang, et al.\n\\newblock MAVEN: A massive general domain event detection dataset.\n\\newblock In \\emph{Proc. EMNLP}, 2020.\n\n\\bibitem[Yao et al.(2019)]{docred}\nY.~Yao, D.~Ye, P.~Li, et al.\n\\newblock DocRED: A large-scale document-level relation extraction dataset.\n\\newblock In \\emph{Proc. ACL}, 2019.\n\n\\bibitem[Zhou et al.(2023)]{uniner}\nW.~Zhou, S.~Zhang, Y.~Gu, M.~Chen, and H.~Peng.\n\\newblock UniNER: Universal named entity recognition with instruction-following large language models.\n\\newblock \\emph{arXiv preprint arXiv:2308.03279}, 2023.\n\n\\bibitem[Liu et al.(2024)]{lost-middle}\nN.~F.~Liu, K.~Lin, J.~Hewitt, A.~Paranjape, M.~Bevilacqua, F.~Petroni, and P.~Liang.\n\\newblock Lost in the middle: How language models use long contexts.\n\\newblock \\emph{TACL}, 2024.\n\n\\bibitem[Wei et al.(2023)]{llmpee}\nX.~Wei, J.~Cui, N.~Cheng, et al.\n\\newblock Zero-shot information extraction via chatting with ChatGPT.\n\\newblock \\emph{arXiv preprint arXiv:2302.10205}, 2023.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "eed1d72f-3a34-4dda-bf14-a749ded8d55d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T113743 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extrac…",
  "leafUuid": "b40514be-e979-4254-b7a7-d56a0f10b887",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research paper from dream experiment data",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9"
}
```

---

### Tool call

_source line 24 · 2026-05-15T12:10:37.832Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QcfHquM4D6PnRTh5yEV1y6`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b40514be-e979-4254-b7a7-d56a0f10b887",
  "isSidechain": false,
  "requestId": "req_011Cb4LA2FseGbSb18htKzk3",
  "type": "assistant",
  "uuid": "f7651d2f-ec72-47b7-93f8-c2824d7ef68a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112yeXnHPDL9LNFqLXDPAjb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12623,
      "cache_read_input_tokens": 47118,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12623,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 47118,
          "cache_creation_input_tokens": 12623,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12623
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

_source line 25 · 2026-05-15T12:10:38.860Z_

<details><summary>↩ Tool result · `toolu_01QcfHquM4D6PnRTh5yEV1y6`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (2.77704pt too wide) in paragraph at lines 25--33
\T1/ptm/m/n/10 embedding-based se-man-tic sim-i-lar-ity, in-de-pen-dently pre-d
icts ex-trac-tion qual-ity degra-da-tion ($\OML/cmm/m/it/10 r[]\OT1/cmr/m/n/10 
0\OML/cmm/m/it/10 :\OT1/cmr/m/n/10 12$\T1/ptm/m/n/10 --
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
Overfull \hbox (16.94765pt too wide) in paragraph at lines 61--64
\T1/ptm/m/n/10.95 graph from pair-wise sim-i-lar-ity scores and par-ti-tions ty
pes via graph col-or-ing. SDGD-zero (embedding-
[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)

LaTeX Warning: Reference `tab:maven-count' on page 3 undefined on input line 13
5.


LaTeX Warning: Reference `tab:pairwise-cross' on page 3 undefined on input line
 164.

[3]

LaTeX Warning: Reference `tab:cross-model' on page 4 undefined on input line 20
2.


LaTeX Warning: Reference `sec:sdgd' on page 4 undefined on input line 233.


LaTeX Warning: Reference `tab:factorial' on page 4 undefined on input line 243.


[4]

LaTeX Warning: Reference `tab:confusion-rate' on page 5 undefined on input line
 266.


LaTeX Warning: Reference `tab:error-taxonomy' on page 5 undefined on input line
 288.

[5]

LaTeX Warning: Reference `tab:proxy-valid' on page 6 undefined on input line 36
1.

[6]

LaTeX Warning: Reference `tab:fewnerd-full' on page 7 undefined on input line 3
85.


LaTeX Warning: Reference `tab:maven-full' on page 7 undefined on input line 417
.


LaTeX Warning: Reference `tab:ablation' on page 7 undefined on input line 448.


Overfull \hbox (29.48557pt too wide) in paragraph at lines 448--449
\T1/ptm/m/n/10.95 The ran-dom batch-ing ab-la-tion (Ta-ble []) de-com-poses SDG
D's to-tal gain into count-reduction and confusability-
[7]

LaTeX Warning: Reference `tab:sdgd-variants' on page 8 undefined on input line 
492.

[8]
Overfull \hbox (2.94582pt too wide) in paragraph at lines 535--539
 []\T1/ptm/b/n/10.95 Limitations.[] \T1/ptm/m/n/10.95 Our pair-wise ef-fect siz
es are mod-est ($\OML/cmm/m/it/10.95 r[]\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95
 :\OT1/cmr/m/n/10.95 12$\T1/ptm/m/n/10.95 --$\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/
10.95 :\OT1/cmr/m/n/10.95 16$\T1/ptm/m/n/10.95 ), re-flect-ing the many non-con
fusability
[9] [10] (./paper.aux

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
blic/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmri8a.pfb>
Output written on paper.pdf (10 pages, 187442 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (2.77704pt too wide) in paragraph at lines 25--33
\T1/ptm/m/n/10 embedding-based se-man-tic sim-i-lar-ity, in-de-pen-dently pre-d
icts ex-trac-tion qual-ity degra-da-tion ($\OML/cmm/m/it/10 r[]\OT1/cmr/m/n/10 
0\OML/cmm/m/it/10 :\OT1/cmr/m/n/10 12$\T1/ptm/m/n/10 --
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
Overfull \hbox (16.94765pt too wide) in paragraph at lines 61--64
\T1/ptm/m/n/10.95 graph from pair-wise sim-i-lar-ity scores and par-ti-tions ty
pes via graph col-or-ing. SDGD-zero (embedding-
[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [3] [4] [5]
[6]
Overfull \hbox (29.48557pt too wide) in paragraph at lines 448--449
\T1/ptm/m/n/10.95 The ran-dom batch-ing ab-la-tion (Ta-ble []10[]) de-com-poses
 SDGD's to-tal gain into count-reduction and confusability-
[7] [8]
Overfull \hbox (2.94582pt too wide) in paragraph at lines 535--539
 []\T1/ptm/b/n/10.95 Limitations.[] \T1/ptm/m/n/10.95 Our pair-wise ef-fect siz
es are mod-est ($\OML/cmm/m/it/10.95 r[]\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95
 :\OT1/cmr/m/n/10.95 12$\T1/ptm/m/n/10.95 --$\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/
10.95 :\OT1/cmr/m/n/10.95 16$\T1/ptm/m/n/10.95 ), re-flect-ing the many non-con
fusability
[9] [10] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmri8a.pfb>
Output written on paper.pdf (10 pages, 189706 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7651d2f-ec72-47b7-93f8-c2824d7ef68a",
  "isSidechain": false,
  "promptId": "cdf92f18-0400-4c4f-90e5-485ecb947e5a",
  "type": "user",
  "uuid": "8f39324f-51ab-4ca7-806a-d4545c3e19b8",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (2.77704pt too wide) in paragraph at lines 25--33\n\\T1/ptm/m/n/10 embedding-based se-man-tic sim-i-lar-ity, in-de-pen-dently pre-d\nicts ex-trac-tion qual-ity degra-da-tion ($\\OML/cmm/m/it/10 r[]\\OT1/cmr/m/n/10 \n0\\OML/cmm/m/it/10 :\\OT1/cmr/m/n/10 12$\\T1/ptm/m/n/10 --\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\nOverfull \\hbox (16.94765pt too wide) in paragraph at lines 61--64\n\\T1/ptm/m/n/10.95 graph from pair-wise sim-i-lar-ity scores and par-ti-tions ty\npes via graph col-or-ing. SDGD-zero (embedding-\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n\nLaTeX Warning: Reference `tab:maven-count' on page 3 undefined on input line 13\n5.\n\n\nLaTeX Warning: Reference `tab:pairwise-cross' on page 3 undefined on input line\n 164.\n\n[3]\n\nLaTeX Warning: Reference `tab:cross-model' on page 4 undefined on input line 20\n2.\n\n\nLaTeX Warning: Reference `sec:sdgd' on page 4 undefined on input line 233.\n\n\nLaTeX Warning: Reference `tab:factorial' on page 4 undefined on input line 243.\n\n\n[4]\n\nLaTeX Warning: Reference `tab:confusion-rate' on page 5 undefined on input line\n 266.\n\n\nLaTeX Warning: Reference `tab:error-taxonomy' on page 5 undefined on input line\n 288.\n\n[5]\n\nLaTeX Warning: Reference `tab:proxy-valid' on page 6 undefined on input line 36\n1.\n\n[6]\n\nLaTeX Warning: Reference `tab:fewnerd-full' on page 7 undefined on input line 3\n85.\n\n\nLaTeX Warning: Reference `tab:maven-full' on page 7 undefined on input line 417\n.\n\n\nLaTeX Warning: Reference `tab:ablation' on page 7 undefined on input line 448.\n\n\nOverfull \\hbox (29.48557pt too wide) in paragraph at lines 448--449\n\\T1/ptm/m/n/10.95 The ran-dom batch-ing ab-la-tion (Ta-ble []) de-com-poses SDG\nD's to-tal gain into count-reduction and confusability-\n[7]\n\nLaTeX Warning: Reference `tab:sdgd-variants' on page 8 undefined on input line \n492.\n\n[8]\nOverfull \\hbox (2.94582pt too wide) in paragraph at lines 535--539\n []\\T1/ptm/b/n/10.95 Limitations.[] \\T1/ptm/m/n/10.95 Our pair-wise ef-fect siz\nes are mod-est ($\\OML/cmm/m/it/10.95 r[]\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95\n :\\OT1/cmr/m/n/10.95 12$\\T1/ptm/m/n/10.95 --$\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/\n10.95 :\\OT1/cmr/m/n/10.95 16$\\T1/ptm/m/n/10.95 ), re-flect-ing the many non-con\nfusability\n[9] [10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmri8a.pfb>\nOutput written on paper.pdf (10 pages, 187442 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (2.77704pt too wide) in paragraph at lines 25--33\n\\T1/ptm/m/n/10 embedding-based se-man-tic sim-i-lar-ity, in-de-pen-dently pre-d\nicts ex-trac-tion qual-ity degra-da-tion ($\\OML/cmm/m/it/10 r[]\\OT1/cmr/m/n/10 \n0\\OML/cmm/m/it/10 :\\OT1/cmr/m/n/10 12$\\T1/ptm/m/n/10 --\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\nOverfull \\hbox (16.94765pt too wide) in paragraph at lines 61--64\n\\T1/ptm/m/n/10.95 graph from pair-wise sim-i-lar-ity scores and par-ti-tions ty\npes via graph col-or-ing. SDGD-zero (embedding-\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [3] [4] [5]\n[6]\nOverfull \\hbox (29.48557pt too wide) in paragraph at lines 448--449\n\\T1/ptm/m/n/10.95 The ran-dom batch-ing ab-la-tion (Ta-ble []10[]) de-com-poses\n SDGD's to-tal gain into count-reduction and confusability-\n[7] [8]\nOverfull \\hbox (2.94582pt too wide) in paragraph at lines 535--539\n []\\T1/ptm/b/n/10.95 Limitations.[] \\T1/ptm/m/n/10.95 Our pair-wise ef-fect siz\nes are mod-est ($\\OML/cmm/m/it/10.95 r[]\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95\n :\\OT1/cmr/m/n/10.95 12$\\T1/ptm/m/n/10.95 --$\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/\n10.95 :\\OT1/cmr/m/n/10.95 16$\\T1/ptm/m/n/10.95 ), re-flect-ing the many non-con\nfusability\n[9] [10] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmri8a.pfb>\nOutput written on paper.pdf (10 pages, 189706 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f7651d2f-ec72-47b7-93f8-c2824d7ef68a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-15T12:10:47.689Z_

编译成功，10 页 PDF，无错误。所有交叉引用已解析，仅有几个 overfull hbox 警告（不影响内容）。

论文覆盖了 `experiment_data.json` 中全部 10 个实验：
- MAVEN/DocRED confusability study → Section 4 (count curves + pairwise correlations)
- Multi-model validation (LLaMA) → Section 4.3
- Centrality confound → Section 4.4
- 2×2 factorial → Section 5.1
- Error taxonomy → Section 5.2
- Extreme-batch effects → Section 5.3
- SDGD-zero/cal on Few-NERD/MAVEN → Section 6.3--6.4
- Random batching ablation → Section 6.5
- Per-type splitting ablation → Section 6.6
- SCS proxy validation → Section 6.2

输出：`paper.pdf` 已写入指定目录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f39324f-51ab-4ca7-806a-d4545c3e19b8",
  "isSidechain": false,
  "requestId": "req_011Cb4LAQVqNe7d9SPWhQ6MM",
  "type": "assistant",
  "uuid": "cc1176b8-4b7e-4e37-b1dd-b47f53d8ee8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdVqy2wZYp6kDSKMYNDeYs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6950,
      "cache_read_input_tokens": 59741,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 259,
          "cache_read_input_tokens": 59741,
          "cache_creation_input_tokens": 6950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6950
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

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T113743 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extrac…",
  "leafUuid": "cc1176b8-4b7e-4e37-b1dd-b47f53d8ee8b",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research paper from dream experiment data",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T113743 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extrac…",
  "leafUuid": "cc1176b8-4b7e-4e37-b1dd-b47f53d8ee8b",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research paper from dream experiment data",
  "sessionId": "98c6fb8b-38c3-4ff0-8816-78ed67c810e9"
}
```

---
