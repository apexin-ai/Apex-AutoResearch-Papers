# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190053 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/8e06f34f-0bcd-4993-862f-8b43ca07c11c.jsonl`
- **Structured JSON:** [`5d500fd068fc7c4607b2.json`](../../sessions/5d/5d500fd068fc7c4607b2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:26:40.652Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:26:40.652Z",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190053 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始framing不成立，但不降venue——reframe为\"variance structure is benchmark-conditional and model-conditional\"。新headline：evaluation variance的归因模式本身是unstable的， 不同benchmark/model组合产生qualitatively不同的方差结构，意味着没有universal reproducibility recipe。核心contribution转为：(1) G-theory framework作为diagnostic tool的方法论贡献；(2) 证明one-size-fits-all standardization策略无效（negative but important result）；(3) float32 engine confound的发现和修复本身是方法论贡献。 D-study从prescriptive budget转为diagnostic tool。启动exp-006对冲inference-only风险。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T19:26:40.655Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:26:40.655Z",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-20T19:26:40.682Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190053 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始framing不成立，但不降venue——reframe为"variance structure is benchmark-conditional and model-conditional"。新headline：evaluation variance的归因模式本身是unstable的， 不同benchmark/model组合产生qualitatively不同的方差结构，意味着没有universal reproducibility recipe。核心contribution转为：(1) G-theory framework作为diagnostic tool的方法论贡献；(2) 证明one-size-fits-all standardization策略无效（negative but important result）；(3) float32 engine confound的发现和修复本身是方法论贡献。 D-study从prescriptive budget转为diagnostic tool。启动exp-006对冲inference-only风险。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "79d32d62-820b-4400-ab38-6e7eddfdf334",
  "type": "user",
  "uuid": "a6a5cb3c-20d4-43a3-b18d-2dad77d7bd5d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:26:40.681Z_

```json
{
  "parentUuid": "a6a5cb3c-20d4-43a3-b18d-2dad77d7bd5d",
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
  "uuid": "020cdadb-6fe8-44bb-ac19-9893f29c724c",
  "timestamp": "2026-05-20T19:26:40.681Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:26:40.681Z_

```json
{
  "parentUuid": "020cdadb-6fe8-44bb-ac19-9893f29c724c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d76b14f2-997a-4d24-a5b2-6515bb0adca5",
  "timestamp": "2026-05-20T19:26:40.681Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
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
  "aiTitle": "Generate simulation paper for dream research",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c"
}
```

---

### Assistant

_source line 7 · 2026-05-20T19:26:44.660Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d76b14f2-997a-4d24-a5b2-6515bb0adca5",
  "isSidechain": false,
  "requestId": "req_011CbENTVA84V1Mvzh1R5aHJ",
  "type": "assistant",
  "uuid": "556decd3-f111-48a8-9409-7c1264e54ca3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019F6aAzemPvg6BT5nmX9UPH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11509,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11509
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

_source line 8 · 2026-05-20T19:26:45.616Z_

<details open><summary>🔧 Tool call — Read · `toolu_016uvFc6ZAHTyJfJd3y7dDcZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "556decd3-f111-48a8-9409-7c1264e54ca3",
  "isSidechain": false,
  "requestId": "req_011CbENTVA84V1Mvzh1R5aHJ",
  "type": "assistant",
  "uuid": "893b0698-7504-4fb4-b298-ec20a4a12d8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019F6aAzemPvg6BT5nmX9UPH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11509,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11509
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

_source line 9 · 2026-05-20T19:26:45.809Z_

<details open><summary>🔧 Tool call — Read · `toolu_011o9B5BhnSCqVCqcwrPbSZX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "893b0698-7504-4fb4-b298-ec20a4a12d8b",
  "isSidechain": false,
  "requestId": "req_011CbENTVA84V1Mvzh1R5aHJ",
  "type": "assistant",
  "uuid": "49d4b635-9dbe-4077-b941-1f5f018cf437",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019F6aAzemPvg6BT5nmX9UPH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11509,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11509
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

_source line 10 · 2026-05-20T19:26:45.814Z_

<details><summary>↩ Tool result · `toolu_011o9B5BhnSCqVCqcwrPbSZX`</summary>

```text
1	# Paper Framing — nlp_variance_gtheory
2	
3	## Target Venue
4	- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)
5	- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)
6	- Extended: TACL (rolling)
7	
8	## Title
9	Reproducibility Budgets for LLM Evaluation: Testing the Separability Assumption Between Infrastructure and Methodological Variance Sources via Generalizability Theory
10	
11	## Core Claims (3 条，可证伪)
12	
13	**Claim 1 — Item Dominance**: Item selection is the single largest uncontrolled variance source in LLM evaluation, contributing more than prompt phrasing, random seed, temperature, numerical precision, and hardware type combined. (MVP evidence: item_id = 58.4% of total variance vs all other factors combined < 25%)
14	
15	**Claim 2 — Conditional Separability**: Infrastructure factors (hardware type, numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level (direct interaction < 0.5% of total variance), but both interact substantially with item difficulty — their effects are item-conditional, not universal. This provides an empirical license for isolated-factor studies while warning that their conclusions are conditional on item selection.
16	
17	**Claim 3 — Reproducibility Budget**: G-theory D-study projections yield quantitative reproducibility budgets showing that increasing item sampling is orders of magnitude more cost-effective than increasing prompt/seed replication for achieving reliable model comparisons (G ≥ 0.90). Current common practices (1 prompt, 1 seed, ≤200 items) produce G < 0.40.
18	
19	## Story Spine
20	
21	**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability between infrastructure and methodology layers.
22	
23	**Existing approaches & gaps**: Mesting (2026) applied G-theory to 5 methodological facets but treated infrastructure as fixed background. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision but without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance but on fixed hardware. No study crosses both layers in a unified G-theory framework, and critically, no study has quantified the role of item selection relative to all other sources.
24	
25	**Our framing**: We conduct the first fully-crossed G-theory study spanning infrastructure (hardware type, numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors. The separability test has two equally publishable outcomes: if interactions are negligible, we grant an empirical license to isolated-factor studies; if substantial, we demonstrate that existing conclusions need hardware/prompt qualification. Our MVP reveals a third, unexpected finding: item selection dominates everything (58.4%), making it the overlooked key to evaluation reproducibility.
26	
27	**Headline result template**: "In a fully-crossed G-study of K conditions across M models and N benchmarks, item selection accounts for >50% of total evaluation variance, while direct infrastructure × methodology interactions contribute <0.5%. Current evaluation practices achieve G < 0.40; our D-study reproducibility budgets show that tripling item count is 10× more effective than tripling prompt count for reaching G ≥ 0.90."
28	
29	## Hook (Counter-Intuitive Quantified Claim)
30	"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs — item selection alone accounts for 58% of total evaluation variance, more than all other factors combined."
31	
32	## Narrative Strategy
33	- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Breaking limitations (separability assumption challenge)
34	- **Tension**: "Everyone's optimizing the wrong thing" — the field focuses on prompt/seed/hardware standardization while ignoring item selection
35	- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)
36	- **Signature visual**: Stacked-bar variance decomposition chart (field idiom from Mesting/Brittlebench)
37	- **Figure flow**: Problem illustration → G-theory facet diagram → Stacked-bar variance decomposition → D-study projection curves
38	
39	## Venue Fit Risks
40	- AAAI: Strong fit for "evaluation methodology" track. Risk: tight 9-week timeline requires overlapping experiments with writing.
41	- Reviewer concern 1: "Only open-weight models, not API models" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.
42	- Reviewer concern 2: "G-theory is borrowed methodology, not novel" — Frame as cross-domain transfer contribution. The novelty is the facet structure crossing infrastructure × methodology, not G-theory itself.
43	- Reviewer concern 3: "Item dominance is obvious — harder items have more variance" — Counter: (a) the magnitude (58%) was not previously quantified; (b) item×factor interactions (7% precision×item) are non-obvious; (c) the D-study implications for evaluation design are novel.
44	
45	## Anticipated Reviewer Concerns & Planned Responses
46	1. **"Only N GPU types"** → exp-003 (multi-hardware crossing) addresses this
47	2. **"float32 engine confound"** → exp-001 fixes with consistent vLLM engine settings (V0 enforce_eager for all)
48	3. **"Only MMLU"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag
49	4. **"Small item sample"** → exp-001 expands from 50 to 200 items
50	5. **"No training-time analysis"** → exp-006 (fine-tuning G-study with RoBERTa)
51	6. **"Missing scale validation"** → exp-005 (14B models)
52	7. **"G-theory may not be right framework"** → Compare with ANOVA and regression decomposition as sensitivity analysis
53	
54	## Design Decisions
55	- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.
56	- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.
57	- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.
58	- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support. Documented as hardware compatibility requirement.
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49d4b635-9dbe-4077-b941-1f5f018cf437",
  "isSidechain": false,
  "promptId": "79d32d62-820b-4400-ab38-6e7eddfdf334",
  "type": "user",
  "uuid": "da06fc6e-e75c-43df-97ce-da00a9a0b7a0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/paper_framing.md",
      "content": "# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: Testing the Separability Assumption Between Infrastructure and Methodological Variance Sources via Generalizability Theory\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Item Dominance**: Item selection is the single largest uncontrolled variance source in LLM evaluation, contributing more than prompt phrasing, random seed, temperature, numerical precision, and hardware type combined. (MVP evidence: item_id = 58.4% of total variance vs all other factors combined < 25%)\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (hardware type, numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level (direct interaction < 0.5% of total variance), but both interact substantially with item difficulty — their effects are item-conditional, not universal. This provides an empirical license for isolated-factor studies while warning that their conclusions are conditional on item selection.\n\n**Claim 3 — Reproducibility Budget**: G-theory D-study projections yield quantitative reproducibility budgets showing that increasing item sampling is orders of magnitude more cost-effective than increasing prompt/seed replication for achieving reliable model comparisons (G ≥ 0.90). Current common practices (1 prompt, 1 seed, ≤200 items) produce G < 0.40.\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability between infrastructure and methodology layers.\n\n**Existing approaches & gaps**: Mesting (2026) applied G-theory to 5 methodological facets but treated infrastructure as fixed background. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision but without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance but on fixed hardware. No study crosses both layers in a unified G-theory framework, and critically, no study has quantified the role of item selection relative to all other sources.\n\n**Our framing**: We conduct the first fully-crossed G-theory study spanning infrastructure (hardware type, numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors. The separability test has two equally publishable outcomes: if interactions are negligible, we grant an empirical license to isolated-factor studies; if substantial, we demonstrate that existing conclusions need hardware/prompt qualification. Our MVP reveals a third, unexpected finding: item selection dominates everything (58.4%), making it the overlooked key to evaluation reproducibility.\n\n**Headline result template**: \"In a fully-crossed G-study of K conditions across M models and N benchmarks, item selection accounts for >50% of total evaluation variance, while direct infrastructure × methodology interactions contribute <0.5%. Current evaluation practices achieve G < 0.40; our D-study reproducibility budgets show that tripling item count is 10× more effective than tripling prompt count for reaching G ≥ 0.90.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs — item selection alone accounts for 58% of total evaluation variance, more than all other factors combined.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Breaking limitations (separability assumption challenge)\n- **Tension**: \"Everyone's optimizing the wrong thing\" — the field focuses on prompt/seed/hardware standardization while ignoring item selection\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart (field idiom from Mesting/Brittlebench)\n- **Figure flow**: Problem illustration → G-theory facet diagram → Stacked-bar variance decomposition → D-study projection curves\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer contribution. The novelty is the facet structure crossing infrastructure × methodology, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious — harder items have more variance\" — Counter: (a) the magnitude (58%) was not previously quantified; (b) item×factor interactions (7% precision×item) are non-obvious; (c) the D-study implications for evaluation design are novel.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this\n2. **\"float32 engine confound\"** → exp-001 fixes with consistent vLLM engine settings (V0 enforce_eager for all)\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa)\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support. Documented as hardware compatibility requirement.\n",
      "numLines": 59,
      "startLine": 1,
      "totalLines": 59
    }
  },
  "sourceToolAssistantUUID": "49d4b635-9dbe-4077-b941-1f5f018cf437",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T19:26:45.904Z_

<details><summary>↩ Tool result · `toolu_016uvFc6ZAHTyJfJd3y7dDcZ`</summary>

```text
1	[
2	  {
3	    "name": "Full-scale precision study (float32 confound fixed)",
4	    "description": "4 models × 3 precisions × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items，全部使用一致的vLLM V0 enforce_eager引擎消除float32 confound。\n",
5	    "results": {
6	      "item_variance_share_overall": 0.24,
7	      "item_variance_share_qwen3_8b": 0.28,
8	      "item_variance_share_llama31_8b": 0.26,
9	      "item_variance_share_gemma2_9b": 0.3,
10	      "item_variance_share_mistral_7b": 0.14,
11	      "residual_share_overall": 0.28,
12	      "residual_share_mistral": 0.38,
13	      "precision_main_effect": 0.015,
14	      "precision_item_interaction": 0.035,
15	      "prompt_item_interaction": 0.048,
16	      "temperature_item_interaction": 0.055,
17	      "seed_item_interaction": 0.018,
18	      "prompt_main_effect": 0.008,
19	      "temperature_main_effect": 0.012,
20	      "seed_main_effect": 0.003,
21	      "ordering_main_effect": 0.002,
22	      "ordering_item_interaction": 0.015,
23	      "accuracy_fp32": 0.67,
24	      "accuracy_bf16": 0.672,
25	      "accuracy_fp16": 0.671,
26	      "g_coefficient_overall": 0.42,
27	      "total_records": 172800,
28	      "models_showing_item_dominant_pattern": 2
29	    },
30	    "tables": [
31	      {
32	        "name": "Table 1: Variance Component Decomposition by Model (exp-001, MMLU)",
33	        "columns": [
34	          "Component",
35	          "Qwen3-8B",
36	          "Llama-3.1-8B",
37	          "Gemma-2-9B",
38	          "Mistral-7B",
39	          "Pooled"
40	        ],
41	        "rows": [
42	          [
43	            "item_id",
44	            "28.1%",
45	            "25.7%",
46	            "30.2%",
47	            "13.8%",
48	            "24.0%"
49	          ],
50	          [
51	            "residual",
52	            "23.4%",
53	            "26.1%",
54	            "21.8%",
55	            "38.2%",
56	            "27.9%"
57	          ],
58	          [
59	            "temperature:item",
60	            "6.2%",
61	            "5.8%",
62	            "4.8%",
63	            "5.1%",
64	            "5.5%"
65	          ],
66	          [
67	            "prompt:item",
68	            "5.4%",
69	            "5.1%",
70	            "4.2%",
71	            "3.6%",
72	            "4.8%"
73	          ],
74	          [
75	            "precision:item",
76	            "4.1%",
77	            "3.8%",
78	            "3.2%",
79	            "2.8%",
80	            "3.5%"
81	          ],
82	          [
83	            "seed:item",
84	            "2.1%",
85	            "1.9%",
86	            "1.6%",
87	            "1.4%",
88	            "1.8%"
89	          ],
90	          [
91	            "ordering:item",
92	            "1.8%",
93	            "1.6%",
94	            "1.2%",
95	            "1.1%",
96	            "1.5%"
97	          ],
98	          [
99	            "precision",
100	            "1.8%",
101	            "1.6%",
102	            "1.4%",
103	            "1.2%",
104	            "1.5%"
105	          ],
106	          [
107	            "temperature",
108	            "1.4%",
109	            "1.2%",
110	            "1.1%",
111	            "0.9%",
112	            "1.2%"
113	          ],
114	          [
115	            "prompt",
116	            "0.9%",
117	            "0.8%",
118	            "0.7%",
119	            "0.6%",
120	            "0.8%"
121	          ],
122	          [
123	            "all other",
124	            "24.8%",
125	            "26.4%",
126	            "29.8%",
127	            "31.3%",
128	            "26.5%"
129	          ]
130	        ]
131	      },
132	      {
133	        "name": "Table 2: Accuracy by Precision Condition (post-fix)",
134	        "columns": [
135	          "Model",
136	          "FP32",
137	          "BF16",
138	          "FP16",
139	          "Max Δ"
140	        ],
141	        "rows": [
142	          [
143	            "Qwen3-8B",
144	            "0.681",
145	            "0.683",
146	            "0.682",
147	            "0.002"
148	          ],
149	          [
150	            "Llama-3.1-8B",
151	            "0.664",
152	            "0.666",
153	            "0.665",
154	            "0.002"
155	          ],
156	          [
157	            "Gemma-2-9B",
158	            "0.708",
159	            "0.710",
160	            "0.709",
161	            "0.002"
162	          ],
163	          [
164	            "Mistral-7B",
165	            "0.613",
166	            "0.615",
167	            "0.614",
168	            "0.002"
169	          ]
170	        ]
171	      }
172	    ],
173	    "figures": [],
174	    "analysis": "这是worst档的核心打击——item dominance大幅缩水后Claim 1的\"58%\"headline不成立。 但reframe路径清晰：confound发现本身是贡献（prior work中有多少结论受类似confound 污染？），方差结构的model-conditional性质（Mistral vs others）成为新发现。residual 主导说明当前G-theory facet设计未能捕获全部系统性方差来源，这本身是diagnostic insight。 新叙事：item仍然是最大的可归因来源之一（24%），但不再是压倒性的——evaluation variance 的归因结构比之前认为的更碎片化。\n\n\nMVP中item_id=58.4%的大部分来自float32 engine confound的inflation——float32使用了 不同的vLLM backend（V1 vs V0），导致float32条件下accuracy系统性偏低（59.9% vs ~68.4%），这个precision主效应通过precision:item_id交互被分配到了item方差中。修复后 precision不再引入系统性偏差，三种精度的accuracy收敛到~67%，item_id的方差贡献大幅 缩水至~24%。residual上升到28%成为最大单一成分，因为：(1) item_id不再吸收confound inflation的方差；(2) CUDA非确定性、vLLM调度随机性等不可归因的噪声被暴露。Mistral-7B 特别异常（item仅14%、residual达38%），因为其architecture（sliding window attention + 不同的tokenizer覆盖率）对MMLU items的响应模式与其他三个模型质性不同——更多方差 落入不可解释的残差中。温度×item交互（5.5%）偏高是因为200个items中有约30%处于模型 决策边界，温度对这些borderline items的影响远大于确定性items。整体G=0.42仅略高于 MVP的0.357，因为residual主导意味着增加任何单一facet的level数都无法有效降低测量误差。\n"
175	  },
176	  {
177	    "name": "Multi-benchmark replication (GSM8K, ARC-Challenge, HellaSwag)",
178	    "description": "4 models × 2 precisions × 6 prompts × 6 seeds × 2 temperatures × 4 orderings on GSM8K/ARC-Challenge/HellaSwag各200 items。\n",
179	    "results": {
180	      "item_variance_share_gsm8k": 0.12,
181	      "item_variance_share_arc": 0.22,
182	      "item_variance_share_hellaswag": 0.18,
183	      "residual_share_gsm8k": 0.35,
184	      "residual_share_arc": 0.24,
185	      "residual_share_hellaswag": 0.2,
186	      "seed_item_interaction_gsm8k": 0.14,
187	      "temperature_item_interaction_gsm8k": 0.18,
188	      "temperature_main_effect_gsm8k": 0.08,
189	      "seed_main_effect_gsm8k": 0.05,
190	      "prompt_item_interaction_arc": 0.06,
191	      "prompt_item_interaction_hellaswag": 0.04,
192	      "g_coefficient_gsm8k": 0.38,
193	      "g_coefficient_arc": 0.48,
194	      "g_coefficient_hellaswag": 0.52,
195	      "cross_benchmark_item_dominance_replication": 0,
196	      "benchmarks_with_item_as_largest": 0,
197	      "benchmarks_with_consistent_top3_components": 0
198	    },
199	    "tables": [
200	      {
201	        "name": "Table 3: Variance Component Ranking by Benchmark",
202	        "columns": [
203	          "Rank",
204	          "MMLU (exp-001)",
205	          "GSM8K",
206	          "ARC-Challenge",
207	          "HellaSwag"
208	        ],
209	        "rows": [
210	          [
211	            "1st",
212	            "residual (28%)",
213	            "residual (35%)",
214	            "residual (24%)",
215	            "residual (20%)"
216	          ],
217	          [
218	            "2nd",
219	            "item_id (24%)",
220	            "temp:item (18%)",
221	            "item_id (22%)",
222	            "item_id (18%)"
223	          ],
224	          [
225	            "3rd",
226	            "temp:item (5.5%)",
227	            "seed:item (14%)",
228	            "prompt:item (6%)",
229	            "temp:item (8%)"
230	          ],
231	          [
232	            "4th",
233	            "prompt:item (4.8%)",
234	            "item_id (12%)",
235	            "temp:item (5%)",
236	            "prompt:item (4%)"
237	          ],
238	          [
239	            "5th",
240	            "precision:item (3.5%)",
241	            "temp (8%)",
242	            "seed:item (4%)",
243	            "seed:item (3%)"
244	          ]
245	        ]
246	      },
247	      {
248	        "name": "Table 4: Cross-benchmark Replication Summary",
249	        "columns": [
250	          "Pattern",
251	          "MMLU",
252	          "GSM8K",
253	          "ARC",
254	          "HellaSwag",
255	          "Replicated?"
256	        ],
257	        "rows": [
258	          [
259	            "item_id > all others combined",
260	            "No",
261	            "No",
262	            "No",
263	            "No",
264	            "0/4"
265	          ],
266	          [
267	            "item_id is largest component",
268	            "No",
269	            "No",
270	            "No",
271	            "No",
272	            "0/4"
273	          ],
274	          [
275	            "residual < 20%",
276	            "No",
277	            "No",
278	            "No",
279	            "No",
280	            "0/4"
281	          ],
282	          [
283	            "direct infra×method < 0.5%",
284	            "Yes",
285	            "Yes",
286	            "Yes",
287	            "Yes",
288	            "4/4"
289	          ],
290	          [
291	            "seed main effect < 1%",
292	            "Yes",
293	            "No",
294	            "Yes",
295	            "Yes",
296	            "3/4"
297	          ]
298	        ]
299	      }
300	    ],
301	    "figures": [],
302	    "analysis": "这是对Claim 1的致命打击：item dominance不仅在修复confound后缩水（exp-001）， 而且在MMLU以外的benchmark上根本不成立。GSM8K中seed和temperature的影响远超item selection。但这恰恰支撑了reframe后的核心论点：方差结构是benchmark-conditional的， 不存在universal reproducibility recipe。这个negative result在evaluation track 有价值——告诉社区\"固定prompt/seed\"在reasoning tasks上不够，而\"增加items\"在 reasoning tasks上可能比MMLU上更无效。\n\n\nGSM8K是reasoning task，生成chain-of-thought过程中seed和temperature的随机性被 放大——每个decoding step的采样噪声累积到最终答案。因此seed:item（14%）和 temperature:item（18%）远超MMLU，而item_id本身仅12%，因为reasoning tasks的难度 variance更多被seed/temperature的采样路径差异所遮蔽。residual在GSM8K上高达35%， 反映了CoT生成的内在不可控性。ARC-Challenge作为science reasoning有中等item dominance（22%），介于MMLU和GSM8K之间——多数题目是知识检索而非推理链，但部分 题目需要multi-step推理引入额外方差。HellaSwag的item=18%、residual=20%反映了 commonsense completion task中completion长度和ambiguity的中间特性。关键发现： 没有任何一个benchmark的方差结构能复制MMLU的pattern——方差hierarchy是 benchmark-conditional的。GSM8K的top component是residual（35%），ARC的是 residual（24%），HellaSwag的是residual（20%）——在worst档下residual几乎总是 最大或接近最大的成分，说明当前facet设计systematically遗漏了某些重要方差来源。\n"
303	  },
304	  {
305	    "name": "Multi-hardware G-study (BLOCKED)",
306	    "description": "4 models × 2+ GPU types × 2 precisions × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。测试hardware×methodology交互。\n",
307	    "results": {
308	      "status": "blocked_no_second_gpu",
309	      "hardware_main_effect": "N/A",
310	      "hardware_method_interaction": "N/A",
311	      "hardware_item_interaction": "N/A",
312	      "claim2_testable": false,
313	      "fallback_evidence": "single-GPU precision-only proxy"
314	    },
315	    "tables": [],
316	    "figures": [],
317	    "analysis": "这是structural blocker。paper必须在limitations中明确承认hardware crossing缺失， Claim 2的scope从\"infrastructure\"缩小到\"numerical precision\"。reviewer concern #1（\"Only N GPU types\"）变得无法回应。reframe策略：将single-GPU作为\"controlled baseline\"，承认hardware是open question，但argue precision已经是实践中最常见的 infrastructure变量。exp-006（fine-tuning）的hardware crossing（如果能在不同GPU上 跑RoBERTa）可能部分弥补。\n\n\n第二块GPU不可用——Manager无法在timeline内提供第二种GPU类型。这是worst档的核心 假设之一。没有hardware crossing，Claim 2的\"infrastructure vs methodology\" 分离无法实证，因为precision是infrastructure的一个proxy但不是全部。在单GPU上， 所有CUDA非确定性来自同一架构的同一driver stack，无法区分hardware-specific vs hardware-universal的方差。Claim 2必须降级为\"precision vs methodology separability\" 而非\"infrastructure vs methodology separability\"，scope显著缩小。\n"
318	  },
319	  {
320	    "name": "D-study projections",
321	    "description": "基于exp-001/002数据（exp-003 blocked）计算D-study optimal allocation projections。\n",
322	    "results": {
323	      "g_current_practice_mmlu": 0.48,
324	      "g_current_practice_gsm8k": 0.35,
325	      "g_current_practice_arc": 0.45,
326	      "g_current_practice_hellaswag": 0.5,
327	      "g_triple_items_mmlu": 0.62,
328	      "g_triple_items_gsm8k": 0.45,
329	      "g_triple_items_arc": 0.58,
330	      "g_triple_items_hellaswag": 0.64,
331	      "items_needed_g90_mmlu": 850,
332	      "items_needed_g90_gsm8k": 1400,
333	      "items_needed_g90_arc": 700,
334	      "items_needed_g90_hellaswag": 600,
335	      "items_needed_g90_average": 888,
336	      "optimal_allocation_varies_by_benchmark": true,
337	      "universal_budget_exists": false,
338	      "g_optimized_600items_3prompts_3seeds_mmlu": 0.72,
339	      "g_optimized_600items_3prompts_3seeds_gsm8k": 0.55
340	    },
341	    "tables": [
342	      {
343	        "name": "Table 5: D-study G-coefficient Projections",
344	        "columns": [
345	          "Scenario",
346	          "MMLU",
347	          "GSM8K",
348	          "ARC",
349	          "HellaSwag"
350	        ],
351	        "rows": [
352	          [
353	            "Current practice (200 items, 1 prompt, 1 seed)",
354	            "0.48",
355	            "0.35",
356	            "0.45",
357	            "0.50"
358	          ],
359	          [
360	            "Triple items (600)",
361	            "0.62",
362	            "0.45",
363	            "0.58",
364	            "0.64"
365	          ],
366	          [
367	            "Triple items + 3 prompts + 3 seeds",
368	            "0.72",
369	            "0.55",
370	            "0.68",
371	            "0.74"
372	          ],
373	          [
374	            "Items needed for G≥0.90 (optimal other facets)",
375	            "850",
376	            "1400",
377	            "700",
378	            "600"
379	          ],
380	          [
381	            "Items needed for G≥0.95",
382	            ">2000",
383	            ">3000",
384	            ">1500",
385	            ">1200"
386	          ]
387	        ]
388	      },
389	      {
390	        "name": "Table 6: Optimal Facet Allocation (budget=1000 total conditions)",
391	        "columns": [
392	          "Facet",
393	          "MMLU optimal",
394	          "GSM8K optimal",
395	          "Divergence"
396	        ],
397	        "rows": [
398	          [
399	            "items",
400	            "500",
401	            "250",
402	            "2× difference"
403	          ],
404	          [
405	            "prompts",
406	            "2",
407	            "4",
408	            "2× difference"
409	          ],
410	          [
411	            "seeds",
412	            "1",
413	            "4",
414	            "4× difference"
415	          ],
416	          [
417	            "temperatures",
418	            "1",
419	            "1 (fixed low)",
420	            "strategy differs"
421	          ]
422	        ]
423	      }
424	    ],
425	    "figures": [],
426	    "analysis": "Claim 3的prescriptive budget完全失效——不存在universal budget。但diagnostic framing仍有价值：D-study揭示了为什么GSM8K比MMLU更难达到可靠评估（residual floor更高），以及为什么不同benchmark需要不同的优化策略。这对practitioners仍然 有用，只是从\"照着这个budget做\"变成了\"你需要先诊断你的evaluation pipeline的 方差结构，然后制定针对性策略\"。这个reframe在evaluation track可以argue： 展示了为什么naive standardization（全部用同一个prompt/seed/item count）是 insufficient的。\n\n\n在worst档下，residual是最大方差成分（25-35%），而residual在G-theory中是不可 优化的——它代表未建模的交互和纯噪声。因此D-study projections的上限被压低。 即使增加所有facet的level数，residual的floor意味着G=0.90需要极大的item数量来 压缩其他可归因方差。MMLU上G≥0.90需要~850 items因为residual=28%设置了noise floor；GSM8K更差（1400 items）因为residual=35%加上seed/temperature的高交互 意味着需要同时增加items和seeds/temperatures。关键发现：optimal allocation strategy在不同benchmark上qualitatively不同——MMLU上增加items最有效，GSM8K上 增加seeds/降低temperature同样重要。这直接支撑\"no universal recipe\"的论点， 但摧毁了Claim 3的prescriptive budget叙事。D-study必须从\"这是你的budget\" 转为\"这是为什么你需要benchmark-specific的budget\"。\n"
427	  },
428	  {
429	    "name": "14B model extension (BLOCKED by exp-003)",
430	    "description": "Qwen3-14B和DeepSeek-R1-Distill-14B at BF16/FP16。测试模型规模对方差结构的影响。\n",
431	    "results": {
432	      "status": "blocked_by_exp003_and_hardware",
433	      "item_variance_share_qwen3_14b": 0.2,
434	      "item_variance_share_deepseek_r1_14b": 0.1,
435	      "residual_share_deepseek_r1_14b": 0.42,
436	      "reasoning_distilled_model_anomaly": true,
437	      "scale_effect_on_variance_structure": "inconclusive"
438	    },
439	    "tables": [
440	      {
441	        "name": "Table 7: 14B vs 8B Variance Structure Comparison (partial)",
442	        "columns": [
443	          "Component",
444	          "8B pooled (exp-001)",
445	          "Qwen3-14B",
446	          "DeepSeek-R1-14B"
447	        ],
448	        "rows": [
449	          [
450	            "item_id",
451	            "24.0%",
452	            "20.0%",
453	            "10.0%"
454	          ],
455	          [
456	            "residual",
457	            "27.9%",
458	            "30.0%",
459	            "42.0%"
460	          ],
461	          [
462	            "temp:item",
463	            "5.5%",
464	            "4.8%",
465	            "12.0%"
466	          ],
467	          [
468	            "seed:item",
469	            "1.8%",
470	            "1.5%",
471	            "8.5%"
472	          ]
473	        ]
474	      }
475	    ],
476	    "figures": [],
477	    "analysis": "即使partial执行，DeepSeek-R1-14B的异常方差结构（residual=42%）进一步瓦解了 universal item dominance叙事。但hardware confound无法排除（单GPU结果）， 且sample size=2个14B模型太少做scale-effect的causal claim。reframe中作为 supplementary evidence用，不作为独立contribution。\n\n\nexp-005依赖exp-003（需要multi-hardware数据），且需要≥48GB VRAM的GPU。在worst 档下即使能partial执行（单GPU、无hardware crossing），结果也problematic： DeepSeek-R1-Distill-14B作为reasoning-distilled模型会表现出极高的residual （~42%）和极低的item dominance（~10%），因为其内部的reasoning chain引入了 类似GSM8K上观察到的seed/temperature敏感性。Qwen3-14B的item=20%介于8B和 DeepSeek之间。两个模型的方差结构差异进一步支撑model-conditional论点，但 without hardware crossing，scale效应和architecture效应无法分离。\n"
478	  },
479	  {
480	    "name": "Fine-tuning G-study (RoBERTa)",
481	    "description": "RoBERTa-large on SST-2/MNLI/RTE/COPA。6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728 runs。\n",
482	    "results": {
483	      "item_variance_share_sst2": 0.15,
484	      "item_variance_share_mnli": 0.12,
485	      "item_variance_share_rte": 0.2,
486	      "item_variance_share_copa": 0.08,
487	      "learning_rate_main_effect_avg": 0.18,
488	      "seed_main_effect_avg": 0.08,
489	      "data_shuffle_main_effect_avg": 0.06,
490	      "precision_main_effect_avg": 0.02,
491	      "lr_seed_interaction_avg": 0.1,
492	      "residual_avg": 0.22,
493	      "g_coefficient_sst2": 0.55,
494	      "g_coefficient_rte": 0.48,
495	      "g_coefficient_copa": 0.35,
496	      "training_vs_inference_variance_correlation": 0.15
497	    },
498	    "tables": [
499	      {
500	        "name": "Table 8: Fine-tuning Variance Decomposition by Task",
501	        "columns": [
502	          "Component",
503	          "SST-2",
504	          "MNLI",
505	          "RTE",
506	          "COPA",
507	          "Average"
508	        ],
509	        "rows": [
510	          [
511	            "learning_rate",
512	            "16.0%",
513	            "20.0%",
514	            "18.0%",
515	            "17.0%",
516	            "17.8%"
517	          ],
518	          [
519	            "residual",
520	            "20.0%",
521	            "22.0%",
522	            "21.0%",
523	            "25.0%",
524	            "22.0%"
525	          ],
526	          [
527	            "item_id",
528	            "15.0%",
529	            "12.0%",
530	            "20.0%",
531	            "8.0%",
532	            "13.8%"
533	          ],
534	          [
535	            "lr:seed",
536	            "10.0%",
537	            "11.0%",
538	            "9.0%",
539	            "10.0%",
540	            "10.0%"
541	          ],
542	          [
543	            "seed",
544	            "8.0%",
545	            "7.0%",
546	            "9.0%",
547	            "8.0%",
548	            "8.0%"
549	          ],
550	          [
551	            "data_shuffle",
552	            "7.0%",
553	            "6.0%",
554	            "5.0%",
555	            "6.0%",
556	            "6.0%"
557	          ],
558	          [
559	            "seed:item",
560	            "5.0%",
561	            "4.0%",
562	            "4.0%",
563	            "6.0%",
564	            "4.8%"
565	          ],
566	          [
567	            "precision",
568	            "2.0%",
569	            "2.5%",
570	            "1.8%",
571	            "2.2%",
572	            "2.1%"
573	          ],
574	          [
575	            "lr:item",
576	            "8.0%",
577	            "7.0%",
578	            "6.0%",
579	            "9.0%",
580	            "7.5%"
581	          ],
582	          [
583	            "all other",
584	            "9.0%",
585	            "8.5%",
586	            "6.2%",
587	            "8.8%",
588	            "8.1%"
589	          ]
590	        ]
591	      },
592	      {
593	        "name": "Table 9: Inference vs Fine-tuning Variance Hierarchy",
594	        "columns": [
595	          "Rank",
596	          "Inference (MMLU)",
597	          "Fine-tuning (avg)"
598	        ],
599	        "rows": [
600	          [
601	            "1st",
602	            "residual (28%)",
603	            "residual (22%)"
604	          ],
605	          [
606	            "2nd",
607	            "item_id (24%)",
608	            "learning_rate (18%)"
609	          ],
610	          [
611	            "3rd",
612	            "temp:item (5.5%)",
613	            "item_id (14%)"
614	          ],
615	          [
616	            "4th",
617	            "prompt:item (4.8%)",
618	            "lr:seed (10%)"
619	          ],
620	          [
621	            "5th",
622	            "precision:item (3.5%)",
623	            "seed (8%)"
624	          ]
625	        ]
626	      }
627	    ],
628	    "figures": [],
629	    "analysis": "exp-006在worst档下是最有价值的hedge。即使inference story崩溃，fine-tuning的 方差归因是genuinely novel的——此前没有研究用G-theory分解fine-tuning的完整 facet structure。learning rate dominance（18%）、lr:seed交互（10%）、以及 inference-training方差结构的decorrelation（r=0.15）都是publishable findings。 这条线可以独立于inference story发展，在worst档下成为paper的saving grace。 potential title angle: \"What makes fine-tuning unreproducible? A G-theory decomposition reveals learning rate × seed interactions dominate.\"\n\n\nFine-tuning的方差结构与inference fundamentally不同。Learning rate是最大的 可归因方差来源（~18%），因为它直接控制模型converge到loss landscape的哪个 basin，不同basin对不同items的predictions质性不同。seed:lr交互高达10%因为 不同seed的weight initialization在不同lr下converge到不同local minima。 item_id在fine-tuning中方差占比更低（8-20%），因为fine-tuning本身改变了 model-item的关系——同一个item在不同training run中的难度会变（unlike inference where model weights are fixed）。COPA尤其低（8%）因为dataset 只有400 items，且causal reasoning tasks的learning dynamics更chaotic。 residual=22%反映了training过程中unmodeled的随机性（CUDA非确定性在训练中 比推理中更显著，因为每个gradient step都累积噪声）。与inference方差结构 的correlation极低（r=0.15），说明inference-based的D-study budget不能 指导training-time的reproducibility。这个发现独立于inference story，可以 作为separate contribution线——即使inference的item dominance不成立， fine-tuning的方差归因本身也是novel的。\n"
630	  },
631	  {
632	    "name": "LayerCast precision mitigation",
633	    "description": "LayerCast（FP16 storage + FP32 compute）作为额外precision条件测试方差减少量。\n",
634	    "results": {
635	      "layercast_accuracy": 0.672,
636	      "layercast_vs_bf16_accuracy_delta": 0.001,
637	      "variance_reduction_vs_fp16": 0.003,
638	      "precision_component_with_layercast": 0.012,
639	      "precision_item_interaction_with_layercast": 0.03,
640	      "practical_significance": "negligible"
641	    },
642	    "tables": [
643	      {
644	        "name": "Table 10: Precision Conditions Including LayerCast",
645	        "columns": [
646	          "Condition",
647	          "Accuracy",
648	          "Precision Variance Share",
649	          "Precision:Item Share"
650	        ],
651	        "rows": [
652	          [
653	            "FP32",
654	            "0.670",
655	            "1.5%",
656	            "3.5%"
657	          ],
658	          [
659	            "BF16",
660	            "0.672",
661	            "—",
662	            "—"
663	          ],
664	          [
665	            "FP16",
666	            "0.671",
667	            "—",
668	            "—"
669	          ],
670	          [
671	            "LayerCast (FP16+FP32)",
672	            "0.672",
673	            "1.2%",
674	            "3.0%"
675	          ]
676	        ]
677	      }
678	    ],
679	    "figures": [],
680	    "analysis": "exp-007在worst档下基本是negative/null result。可以用一句话mention作为 supplementary finding（\"LayerCast provides negligible additional benefit when the float32 engine confound is properly controlled\"），但不值得 dedicated space。主要价值是排除了precision作为重要方差来源的可能性。\n\n\n在worst档下，exp-001已经显示precision main effect仅1.5%（confound修复后）。 LayerCast的FP16 storage + FP32 compute在理论上应该给出接近FP32的结果，但 由于FP32本身与BF16/FP16的差异已经很小（Δaccuracy=0.002），LayerCast的 额外收益几乎为零。precision:item交互从3.5%微降到3.0%，不具有实际意义。 这个结果说明precision本来就不是主要方差来源（confound修复后），mitigation 策略针对的是一个已经很小的问题。\n"
681	  },
682	  {
683	    "name": "MATH benchmark extension",
684	    "description": "MATH benchmark 200 items，测试reasoning-heavy tasks中CoT引入的额外方差。\n",
685	    "results": {
686	      "item_variance_share_math": 0.1,
687	      "residual_share_math": 0.4,
688	      "seed_main_effect_math": 0.07,
689	      "seed_item_interaction_math": 0.12,
690	      "temperature_main_effect_math": 0.1,
691	      "temperature_item_interaction_math": 0.15,
692	      "prompt_item_interaction_math": 0.03,
693	      "g_coefficient_math": 0.3,
694	      "cot_length_variance_correlation": 0.65,
695	      "items_needed_g90_math": 2200
696	    },
697	    "tables": [
698	      {
699	        "name": "Table 11: MATH Variance Decomposition vs Other Benchmarks",
700	        "columns": [
701	          "Component",
702	          "MMLU",
703	          "GSM8K",
704	          "MATH"
705	        ],
706	        "rows": [
707	          [
708	            "residual",
709	            "28%",
710	            "35%",
711	            "40%"
712	          ],
713	          [
714	            "item_id",
715	            "24%",
716	            "12%",
717	            "10%"
718	          ],
719	          [
720	            "temp:item",
721	            "5.5%",
722	            "18%",
723	            "15%"
724	          ],
725	          [
726	            "seed:item",
727	            "1.8%",
728	            "14%",
729	            "12%"
730	          ],
731	          [
732	            "temperature",
733	            "1.2%",
734	            "8%",
735	            "10%"
736	          ],
737	          [
738	            "seed",
739	            "0.3%",
740	            "5%",
741	            "7%"
742	          ],
743	          [
744	            "G coefficient",
745	            "0.42",
746	            "0.38",
747	            "0.30"
748	          ],
749	          [
750	            "Items for G≥0.90",
751	            "850",
752	            "1400",
753	            "2200"
754	          ]
755	        ]
756	      }
757	    ],
758	    "figures": [],
759	    "analysis": "MATH是worst档叙事的exclamation mark。G=0.30意味着当前practice下MATH evaluation基本是noise-dominated的。结合exp-002的GSM8K结果，形成清晰的 gradient：knowledge-retrieval tasks（MMLU）→ moderate reasoning（ARC）→ generation-heavy reasoning（GSM8K/MATH）的方差结构systematically shifts from item-conditional to seed/temperature-conditional。这个gradient本身 是一个contribution——它解释了为什么reasoning benchmark的reproduction rates historically更低，并提供了mechanistic account（CoT length amplifies sampling noise）。\n\nMATH是最extreme的reasoning benchmark，CoT生成过程中的每个token都是一个 采样点，长推理链（avg 200+ tokens）意味着seed和temperature的随机性被200+ 次multiplicative放大。因此seed:item（12%）和temperature:item（15%）极高， temperature main effect达10%（在其他benchmark上<2%），因为temperature 直接控制采样diversity，在长chain中的累积效应是非线性的。item_id仅10%—— 比GSM8K更低——因为MATH problems的难度更多由解题路径的存在性决定，而非 item本身的知识内容，solution path的发现受seed/temperature强烈影响。 residual高达40%是worst档中最高的，反映了MATH推理过程中大量不可归因的 随机性（错误的推理链、self-correction失败、格式解析错误等）。G=0.30是 所有benchmark中最低的，G≥0.90需要2200 items，完全不切实际（MATH全集仅 5000题）。这个结果是\"no universal recipe\"论点的最强证据——如果连G≥0.90 的item threshold在不同benchmark间差3-4倍，prescriptive budget毫无意义。\n"
760	  }
761	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "893b0698-7504-4fb4-b298-ec20a4a12d8b",
  "isSidechain": false,
  "promptId": "79d32d62-820b-4400-ab38-6e7eddfdf334",
  "type": "user",
  "uuid": "eae953a7-8bf9-44cc-882b-22bf7a896a44",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full-scale precision study (float32 confound fixed)\",\n    \"description\": \"4 models × 3 precisions × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items，全部使用一致的vLLM V0 enforce_eager引擎消除float32 confound。\\n\",\n    \"results\": {\n      \"item_variance_share_overall\": 0.24,\n      \"item_variance_share_qwen3_8b\": 0.28,\n      \"item_variance_share_llama31_8b\": 0.26,\n      \"item_variance_share_gemma2_9b\": 0.3,\n      \"item_variance_share_mistral_7b\": 0.14,\n      \"residual_share_overall\": 0.28,\n      \"residual_share_mistral\": 0.38,\n      \"precision_main_effect\": 0.015,\n      \"precision_item_interaction\": 0.035,\n      \"prompt_item_interaction\": 0.048,\n      \"temperature_item_interaction\": 0.055,\n      \"seed_item_interaction\": 0.018,\n      \"prompt_main_effect\": 0.008,\n      \"temperature_main_effect\": 0.012,\n      \"seed_main_effect\": 0.003,\n      \"ordering_main_effect\": 0.002,\n      \"ordering_item_interaction\": 0.015,\n      \"accuracy_fp32\": 0.67,\n      \"accuracy_bf16\": 0.672,\n      \"accuracy_fp16\": 0.671,\n      \"g_coefficient_overall\": 0.42,\n      \"total_records\": 172800,\n      \"models_showing_item_dominant_pattern\": 2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Variance Component Decomposition by Model (exp-001, MMLU)\",\n        \"columns\": [\n          \"Component\",\n          \"Qwen3-8B\",\n          \"Llama-3.1-8B\",\n          \"Gemma-2-9B\",\n          \"Mistral-7B\",\n          \"Pooled\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"28.1%\",\n            \"25.7%\",\n            \"30.2%\",\n            \"13.8%\",\n            \"24.0%\"\n          ],\n          [\n            \"residual\",\n            \"23.4%\",\n            \"26.1%\",\n            \"21.8%\",\n            \"38.2%\",\n            \"27.9%\"\n          ],\n          [\n            \"temperature:item\",\n            \"6.2%\",\n            \"5.8%\",\n            \"4.8%\",\n            \"5.1%\",\n            \"5.5%\"\n          ],\n          [\n            \"prompt:item\",\n            \"5.4%\",\n            \"5.1%\",\n            \"4.2%\",\n            \"3.6%\",\n            \"4.8%\"\n          ],\n          [\n            \"precision:item\",\n            \"4.1%\",\n            \"3.8%\",\n            \"3.2%\",\n            \"2.8%\",\n            \"3.5%\"\n          ],\n          [\n            \"seed:item\",\n            \"2.1%\",\n            \"1.9%\",\n            \"1.6%\",\n            \"1.4%\",\n            \"1.8%\"\n          ],\n          [\n            \"ordering:item\",\n            \"1.8%\",\n            \"1.6%\",\n            \"1.2%\",\n            \"1.1%\",\n            \"1.5%\"\n          ],\n          [\n            \"precision\",\n            \"1.8%\",\n            \"1.6%\",\n            \"1.4%\",\n            \"1.2%\",\n            \"1.5%\"\n          ],\n          [\n            \"temperature\",\n            \"1.4%\",\n            \"1.2%\",\n            \"1.1%\",\n            \"0.9%\",\n            \"1.2%\"\n          ],\n          [\n            \"prompt\",\n            \"0.9%\",\n            \"0.8%\",\n            \"0.7%\",\n            \"0.6%\",\n            \"0.8%\"\n          ],\n          [\n            \"all other\",\n            \"24.8%\",\n            \"26.4%\",\n            \"29.8%\",\n            \"31.3%\",\n            \"26.5%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Accuracy by Precision Condition (post-fix)\",\n        \"columns\": [\n          \"Model\",\n          \"FP32\",\n          \"BF16\",\n          \"FP16\",\n          \"Max Δ\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            \"0.681\",\n            \"0.683\",\n            \"0.682\",\n            \"0.002\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"0.664\",\n            \"0.666\",\n            \"0.665\",\n            \"0.002\"\n          ],\n          [\n            \"Gemma-2-9B\",\n            \"0.708\",\n            \"0.710\",\n            \"0.709\",\n            \"0.002\"\n          ],\n          [\n            \"Mistral-7B\",\n            \"0.613\",\n            \"0.615\",\n            \"0.614\",\n            \"0.002\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是worst档的核心打击——item dominance大幅缩水后Claim 1的\\\"58%\\\"headline不成立。 但reframe路径清晰：confound发现本身是贡献（prior work中有多少结论受类似confound 污染？），方差结构的model-conditional性质（Mistral vs others）成为新发现。residual 主导说明当前G-theory facet设计未能捕获全部系统性方差来源，这本身是diagnostic insight。 新叙事：item仍然是最大的可归因来源之一（24%），但不再是压倒性的——evaluation variance 的归因结构比之前认为的更碎片化。\\n\\n\\nMVP中item_id=58.4%的大部分来自float32 engine confound的inflation——float32使用了 不同的vLLM backend（V1 vs V0），导致float32条件下accuracy系统性偏低（59.9% vs ~68.4%），这个precision主效应通过precision:item_id交互被分配到了item方差中。修复后 precision不再引入系统性偏差，三种精度的accuracy收敛到~67%，item_id的方差贡献大幅 缩水至~24%。residual上升到28%成为最大单一成分，因为：(1) item_id不再吸收confound inflation的方差；(2) CUDA非确定性、vLLM调度随机性等不可归因的噪声被暴露。Mistral-7B 特别异常（item仅14%、residual达38%），因为其architecture（sliding window attention + 不同的tokenizer覆盖率）对MMLU items的响应模式与其他三个模型质性不同——更多方差 落入不可解释的残差中。温度×item交互（5.5%）偏高是因为200个items中有约30%处于模型 决策边界，温度对这些borderline items的影响远大于确定性items。整体G=0.42仅略高于 MVP的0.357，因为residual主导意味着增加任何单一facet的level数都无法有效降低测量误差。\\n\"\n  },\n  {\n    \"name\": \"Multi-benchmark replication (GSM8K, ARC-Challenge, HellaSwag)\",\n    \"description\": \"4 models × 2 precisions × 6 prompts × 6 seeds × 2 temperatures × 4 orderings on GSM8K/ARC-Challenge/HellaSwag各200 items。\\n\",\n    \"results\": {\n      \"item_variance_share_gsm8k\": 0.12,\n      \"item_variance_share_arc\": 0.22,\n      \"item_variance_share_hellaswag\": 0.18,\n      \"residual_share_gsm8k\": 0.35,\n      \"residual_share_arc\": 0.24,\n      \"residual_share_hellaswag\": 0.2,\n      \"seed_item_interaction_gsm8k\": 0.14,\n      \"temperature_item_interaction_gsm8k\": 0.18,\n      \"temperature_main_effect_gsm8k\": 0.08,\n      \"seed_main_effect_gsm8k\": 0.05,\n      \"prompt_item_interaction_arc\": 0.06,\n      \"prompt_item_interaction_hellaswag\": 0.04,\n      \"g_coefficient_gsm8k\": 0.38,\n      \"g_coefficient_arc\": 0.48,\n      \"g_coefficient_hellaswag\": 0.52,\n      \"cross_benchmark_item_dominance_replication\": 0,\n      \"benchmarks_with_item_as_largest\": 0,\n      \"benchmarks_with_consistent_top3_components\": 0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Variance Component Ranking by Benchmark\",\n        \"columns\": [\n          \"Rank\",\n          \"MMLU (exp-001)\",\n          \"GSM8K\",\n          \"ARC-Challenge\",\n          \"HellaSwag\"\n        ],\n        \"rows\": [\n          [\n            \"1st\",\n            \"residual (28%)\",\n            \"residual (35%)\",\n            \"residual (24%)\",\n            \"residual (20%)\"\n          ],\n          [\n            \"2nd\",\n            \"item_id (24%)\",\n            \"temp:item (18%)\",\n            \"item_id (22%)\",\n            \"item_id (18%)\"\n          ],\n          [\n            \"3rd\",\n            \"temp:item (5.5%)\",\n            \"seed:item (14%)\",\n            \"prompt:item (6%)\",\n            \"temp:item (8%)\"\n          ],\n          [\n            \"4th\",\n            \"prompt:item (4.8%)\",\n            \"item_id (12%)\",\n            \"temp:item (5%)\",\n            \"prompt:item (4%)\"\n          ],\n          [\n            \"5th\",\n            \"precision:item (3.5%)\",\n            \"temp (8%)\",\n            \"seed:item (4%)\",\n            \"seed:item (3%)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: Cross-benchmark Replication Summary\",\n        \"columns\": [\n          \"Pattern\",\n          \"MMLU\",\n          \"GSM8K\",\n          \"ARC\",\n          \"HellaSwag\",\n          \"Replicated?\"\n        ],\n        \"rows\": [\n          [\n            \"item_id > all others combined\",\n            \"No\",\n            \"No\",\n            \"No\",\n            \"No\",\n            \"0/4\"\n          ],\n          [\n            \"item_id is largest component\",\n            \"No\",\n            \"No\",\n            \"No\",\n            \"No\",\n            \"0/4\"\n          ],\n          [\n            \"residual < 20%\",\n            \"No\",\n            \"No\",\n            \"No\",\n            \"No\",\n            \"0/4\"\n          ],\n          [\n            \"direct infra×method < 0.5%\",\n            \"Yes\",\n            \"Yes\",\n            \"Yes\",\n            \"Yes\",\n            \"4/4\"\n          ],\n          [\n            \"seed main effect < 1%\",\n            \"Yes\",\n            \"No\",\n            \"Yes\",\n            \"Yes\",\n            \"3/4\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是对Claim 1的致命打击：item dominance不仅在修复confound后缩水（exp-001）， 而且在MMLU以外的benchmark上根本不成立。GSM8K中seed和temperature的影响远超item selection。但这恰恰支撑了reframe后的核心论点：方差结构是benchmark-conditional的， 不存在universal reproducibility recipe。这个negative result在evaluation track 有价值——告诉社区\\\"固定prompt/seed\\\"在reasoning tasks上不够，而\\\"增加items\\\"在 reasoning tasks上可能比MMLU上更无效。\\n\\n\\nGSM8K是reasoning task，生成chain-of-thought过程中seed和temperature的随机性被 放大——每个decoding step的采样噪声累积到最终答案。因此seed:item（14%）和 temperature:item（18%）远超MMLU，而item_id本身仅12%，因为reasoning tasks的难度 variance更多被seed/temperature的采样路径差异所遮蔽。residual在GSM8K上高达35%， 反映了CoT生成的内在不可控性。ARC-Challenge作为science reasoning有中等item dominance（22%），介于MMLU和GSM8K之间——多数题目是知识检索而非推理链，但部分 题目需要multi-step推理引入额外方差。HellaSwag的item=18%、residual=20%反映了 commonsense completion task中completion长度和ambiguity的中间特性。关键发现： 没有任何一个benchmark的方差结构能复制MMLU的pattern——方差hierarchy是 benchmark-conditional的。GSM8K的top component是residual（35%），ARC的是 residual（24%），HellaSwag的是residual（20%）——在worst档下residual几乎总是 最大或接近最大的成分，说明当前facet设计systematically遗漏了某些重要方差来源。\\n\"\n  },\n  {\n    \"name\": \"Multi-hardware G-study (BLOCKED)\",\n    \"description\": \"4 models × 2+ GPU types × 2 precisions × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。测试hardware×methodology交互。\\n\",\n    \"results\": {\n      \"status\": \"blocked_no_second_gpu\",\n      \"hardware_main_effect\": \"N/A\",\n      \"hardware_method_interaction\": \"N/A\",\n      \"hardware_item_interaction\": \"N/A\",\n      \"claim2_testable\": false,\n      \"fallback_evidence\": \"single-GPU precision-only proxy\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"这是structural blocker。paper必须在limitations中明确承认hardware crossing缺失， Claim 2的scope从\\\"infrastructure\\\"缩小到\\\"numerical precision\\\"。reviewer concern #1（\\\"Only N GPU types\\\"）变得无法回应。reframe策略：将single-GPU作为\\\"controlled baseline\\\"，承认hardware是open question，但argue precision已经是实践中最常见的 infrastructure变量。exp-006（fine-tuning）的hardware crossing（如果能在不同GPU上 跑RoBERTa）可能部分弥补。\\n\\n\\n第二块GPU不可用——Manager无法在timeline内提供第二种GPU类型。这是worst档的核心 假设之一。没有hardware crossing，Claim 2的\\\"infrastructure vs methodology\\\" 分离无法实证，因为precision是infrastructure的一个proxy但不是全部。在单GPU上， 所有CUDA非确定性来自同一架构的同一driver stack，无法区分hardware-specific vs hardware-universal的方差。Claim 2必须降级为\\\"precision vs methodology separability\\\" 而非\\\"infrastructure vs methodology separability\\\"，scope显著缩小。\\n\"\n  },\n  {\n    \"name\": \"D-study projections\",\n    \"description\": \"基于exp-001/002数据（exp-003 blocked）计算D-study optimal allocation projections。\\n\",\n    \"results\": {\n      \"g_current_practice_mmlu\": 0.48,\n      \"g_current_practice_gsm8k\": 0.35,\n      \"g_current_practice_arc\": 0.45,\n      \"g_current_practice_hellaswag\": 0.5,\n      \"g_triple_items_mmlu\": 0.62,\n      \"g_triple_items_gsm8k\": 0.45,\n      \"g_triple_items_arc\": 0.58,\n      \"g_triple_items_hellaswag\": 0.64,\n      \"items_needed_g90_mmlu\": 850,\n      \"items_needed_g90_gsm8k\": 1400,\n      \"items_needed_g90_arc\": 700,\n      \"items_needed_g90_hellaswag\": 600,\n      \"items_needed_g90_average\": 888,\n      \"optimal_allocation_varies_by_benchmark\": true,\n      \"universal_budget_exists\": false,\n      \"g_optimized_600items_3prompts_3seeds_mmlu\": 0.72,\n      \"g_optimized_600items_3prompts_3seeds_gsm8k\": 0.55\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: D-study G-coefficient Projections\",\n        \"columns\": [\n          \"Scenario\",\n          \"MMLU\",\n          \"GSM8K\",\n          \"ARC\",\n          \"HellaSwag\"\n        ],\n        \"rows\": [\n          [\n            \"Current practice (200 items, 1 prompt, 1 seed)\",\n            \"0.48\",\n            \"0.35\",\n            \"0.45\",\n            \"0.50\"\n          ],\n          [\n            \"Triple items (600)\",\n            \"0.62\",\n            \"0.45\",\n            \"0.58\",\n            \"0.64\"\n          ],\n          [\n            \"Triple items + 3 prompts + 3 seeds\",\n            \"0.72\",\n            \"0.55\",\n            \"0.68\",\n            \"0.74\"\n          ],\n          [\n            \"Items needed for G≥0.90 (optimal other facets)\",\n            \"850\",\n            \"1400\",\n            \"700\",\n            \"600\"\n          ],\n          [\n            \"Items needed for G≥0.95\",\n            \">2000\",\n            \">3000\",\n            \">1500\",\n            \">1200\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: Optimal Facet Allocation (budget=1000 total conditions)\",\n        \"columns\": [\n          \"Facet\",\n          \"MMLU optimal\",\n          \"GSM8K optimal\",\n          \"Divergence\"\n        ],\n        \"rows\": [\n          [\n            \"items\",\n            \"500\",\n            \"250\",\n            \"2× difference\"\n          ],\n          [\n            \"prompts\",\n            \"2\",\n            \"4\",\n            \"2× difference\"\n          ],\n          [\n            \"seeds\",\n            \"1\",\n            \"4\",\n            \"4× difference\"\n          ],\n          [\n            \"temperatures\",\n            \"1\",\n            \"1 (fixed low)\",\n            \"strategy differs\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 3的prescriptive budget完全失效——不存在universal budget。但diagnostic framing仍有价值：D-study揭示了为什么GSM8K比MMLU更难达到可靠评估（residual floor更高），以及为什么不同benchmark需要不同的优化策略。这对practitioners仍然 有用，只是从\\\"照着这个budget做\\\"变成了\\\"你需要先诊断你的evaluation pipeline的 方差结构，然后制定针对性策略\\\"。这个reframe在evaluation track可以argue： 展示了为什么naive standardization（全部用同一个prompt/seed/item count）是 insufficient的。\\n\\n\\n在worst档下，residual是最大方差成分（25-35%），而residual在G-theory中是不可 优化的——它代表未建模的交互和纯噪声。因此D-study projections的上限被压低。 即使增加所有facet的level数，residual的floor意味着G=0.90需要极大的item数量来 压缩其他可归因方差。MMLU上G≥0.90需要~850 items因为residual=28%设置了noise floor；GSM8K更差（1400 items）因为residual=35%加上seed/temperature的高交互 意味着需要同时增加items和seeds/temperatures。关键发现：optimal allocation strategy在不同benchmark上qualitatively不同——MMLU上增加items最有效，GSM8K上 增加seeds/降低temperature同样重要。这直接支撑\\\"no universal recipe\\\"的论点， 但摧毁了Claim 3的prescriptive budget叙事。D-study必须从\\\"这是你的budget\\\" 转为\\\"这是为什么你需要benchmark-specific的budget\\\"。\\n\"\n  },\n  {\n    \"name\": \"14B model extension (BLOCKED by exp-003)\",\n    \"description\": \"Qwen3-14B和DeepSeek-R1-Distill-14B at BF16/FP16。测试模型规模对方差结构的影响。\\n\",\n    \"results\": {\n      \"status\": \"blocked_by_exp003_and_hardware\",\n      \"item_variance_share_qwen3_14b\": 0.2,\n      \"item_variance_share_deepseek_r1_14b\": 0.1,\n      \"residual_share_deepseek_r1_14b\": 0.42,\n      \"reasoning_distilled_model_anomaly\": true,\n      \"scale_effect_on_variance_structure\": \"inconclusive\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: 14B vs 8B Variance Structure Comparison (partial)\",\n        \"columns\": [\n          \"Component\",\n          \"8B pooled (exp-001)\",\n          \"Qwen3-14B\",\n          \"DeepSeek-R1-14B\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"24.0%\",\n            \"20.0%\",\n            \"10.0%\"\n          ],\n          [\n            \"residual\",\n            \"27.9%\",\n            \"30.0%\",\n            \"42.0%\"\n          ],\n          [\n            \"temp:item\",\n            \"5.5%\",\n            \"4.8%\",\n            \"12.0%\"\n          ],\n          [\n            \"seed:item\",\n            \"1.8%\",\n            \"1.5%\",\n            \"8.5%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"即使partial执行，DeepSeek-R1-14B的异常方差结构（residual=42%）进一步瓦解了 universal item dominance叙事。但hardware confound无法排除（单GPU结果）， 且sample size=2个14B模型太少做scale-effect的causal claim。reframe中作为 supplementary evidence用，不作为独立contribution。\\n\\n\\nexp-005依赖exp-003（需要multi-hardware数据），且需要≥48GB VRAM的GPU。在worst 档下即使能partial执行（单GPU、无hardware crossing），结果也problematic： DeepSeek-R1-Distill-14B作为reasoning-distilled模型会表现出极高的residual （~42%）和极低的item dominance（~10%），因为其内部的reasoning chain引入了 类似GSM8K上观察到的seed/temperature敏感性。Qwen3-14B的item=20%介于8B和 DeepSeek之间。两个模型的方差结构差异进一步支撑model-conditional论点，但 without hardware crossing，scale效应和architecture效应无法分离。\\n\"\n  },\n  {\n    \"name\": \"Fine-tuning G-study (RoBERTa)\",\n    \"description\": \"RoBERTa-large on SST-2/MNLI/RTE/COPA。6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728 runs。\\n\",\n    \"results\": {\n      \"item_variance_share_sst2\": 0.15,\n      \"item_variance_share_mnli\": 0.12,\n      \"item_variance_share_rte\": 0.2,\n      \"item_variance_share_copa\": 0.08,\n      \"learning_rate_main_effect_avg\": 0.18,\n      \"seed_main_effect_avg\": 0.08,\n      \"data_shuffle_main_effect_avg\": 0.06,\n      \"precision_main_effect_avg\": 0.02,\n      \"lr_seed_interaction_avg\": 0.1,\n      \"residual_avg\": 0.22,\n      \"g_coefficient_sst2\": 0.55,\n      \"g_coefficient_rte\": 0.48,\n      \"g_coefficient_copa\": 0.35,\n      \"training_vs_inference_variance_correlation\": 0.15\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Fine-tuning Variance Decomposition by Task\",\n        \"columns\": [\n          \"Component\",\n          \"SST-2\",\n          \"MNLI\",\n          \"RTE\",\n          \"COPA\",\n          \"Average\"\n        ],\n        \"rows\": [\n          [\n            \"learning_rate\",\n            \"16.0%\",\n            \"20.0%\",\n            \"18.0%\",\n            \"17.0%\",\n            \"17.8%\"\n          ],\n          [\n            \"residual\",\n            \"20.0%\",\n            \"22.0%\",\n            \"21.0%\",\n            \"25.0%\",\n            \"22.0%\"\n          ],\n          [\n            \"item_id\",\n            \"15.0%\",\n            \"12.0%\",\n            \"20.0%\",\n            \"8.0%\",\n            \"13.8%\"\n          ],\n          [\n            \"lr:seed\",\n            \"10.0%\",\n            \"11.0%\",\n            \"9.0%\",\n            \"10.0%\",\n            \"10.0%\"\n          ],\n          [\n            \"seed\",\n            \"8.0%\",\n            \"7.0%\",\n            \"9.0%\",\n            \"8.0%\",\n            \"8.0%\"\n          ],\n          [\n            \"data_shuffle\",\n            \"7.0%\",\n            \"6.0%\",\n            \"5.0%\",\n            \"6.0%\",\n            \"6.0%\"\n          ],\n          [\n            \"seed:item\",\n            \"5.0%\",\n            \"4.0%\",\n            \"4.0%\",\n            \"6.0%\",\n            \"4.8%\"\n          ],\n          [\n            \"precision\",\n            \"2.0%\",\n            \"2.5%\",\n            \"1.8%\",\n            \"2.2%\",\n            \"2.1%\"\n          ],\n          [\n            \"lr:item\",\n            \"8.0%\",\n            \"7.0%\",\n            \"6.0%\",\n            \"9.0%\",\n            \"7.5%\"\n          ],\n          [\n            \"all other\",\n            \"9.0%\",\n            \"8.5%\",\n            \"6.2%\",\n            \"8.8%\",\n            \"8.1%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: Inference vs Fine-tuning Variance Hierarchy\",\n        \"columns\": [\n          \"Rank\",\n          \"Inference (MMLU)\",\n          \"Fine-tuning (avg)\"\n        ],\n        \"rows\": [\n          [\n            \"1st\",\n            \"residual (28%)\",\n            \"residual (22%)\"\n          ],\n          [\n            \"2nd\",\n            \"item_id (24%)\",\n            \"learning_rate (18%)\"\n          ],\n          [\n            \"3rd\",\n            \"temp:item (5.5%)\",\n            \"item_id (14%)\"\n          ],\n          [\n            \"4th\",\n            \"prompt:item (4.8%)\",\n            \"lr:seed (10%)\"\n          ],\n          [\n            \"5th\",\n            \"precision:item (3.5%)\",\n            \"seed (8%)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-006在worst档下是最有价值的hedge。即使inference story崩溃，fine-tuning的 方差归因是genuinely novel的——此前没有研究用G-theory分解fine-tuning的完整 facet structure。learning rate dominance（18%）、lr:seed交互（10%）、以及 inference-training方差结构的decorrelation（r=0.15）都是publishable findings。 这条线可以独立于inference story发展，在worst档下成为paper的saving grace。 potential title angle: \\\"What makes fine-tuning unreproducible? A G-theory decomposition reveals learning rate × seed interactions dominate.\\\"\\n\\n\\nFine-tuning的方差结构与inference fundamentally不同。Learning rate是最大的 可归因方差来源（~18%），因为它直接控制模型converge到loss landscape的哪个 basin，不同basin对不同items的predictions质性不同。seed:lr交互高达10%因为 不同seed的weight initialization在不同lr下converge到不同local minima。 item_id在fine-tuning中方差占比更低（8-20%），因为fine-tuning本身改变了 model-item的关系——同一个item在不同training run中的难度会变（unlike inference where model weights are fixed）。COPA尤其低（8%）因为dataset 只有400 items，且causal reasoning tasks的learning dynamics更chaotic。 residual=22%反映了training过程中unmodeled的随机性（CUDA非确定性在训练中 比推理中更显著，因为每个gradient step都累积噪声）。与inference方差结构 的correlation极低（r=0.15），说明inference-based的D-study budget不能 指导training-time的reproducibility。这个发现独立于inference story，可以 作为separate contribution线——即使inference的item dominance不成立， fine-tuning的方差归因本身也是novel的。\\n\"\n  },\n  {\n    \"name\": \"LayerCast precision mitigation\",\n    \"description\": \"LayerCast（FP16 storage + FP32 compute）作为额外precision条件测试方差减少量。\\n\",\n    \"results\": {\n      \"layercast_accuracy\": 0.672,\n      \"layercast_vs_bf16_accuracy_delta\": 0.001,\n      \"variance_reduction_vs_fp16\": 0.003,\n      \"precision_component_with_layercast\": 0.012,\n      \"precision_item_interaction_with_layercast\": 0.03,\n      \"practical_significance\": \"negligible\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Precision Conditions Including LayerCast\",\n        \"columns\": [\n          \"Condition\",\n          \"Accuracy\",\n          \"Precision Variance Share\",\n          \"Precision:Item Share\"\n        ],\n        \"rows\": [\n          [\n            \"FP32\",\n            \"0.670\",\n            \"1.5%\",\n            \"3.5%\"\n          ],\n          [\n            \"BF16\",\n            \"0.672\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"FP16\",\n            \"0.671\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"LayerCast (FP16+FP32)\",\n            \"0.672\",\n            \"1.2%\",\n            \"3.0%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-007在worst档下基本是negative/null result。可以用一句话mention作为 supplementary finding（\\\"LayerCast provides negligible additional benefit when the float32 engine confound is properly controlled\\\"），但不值得 dedicated space。主要价值是排除了precision作为重要方差来源的可能性。\\n\\n\\n在worst档下，exp-001已经显示precision main effect仅1.5%（confound修复后）。 LayerCast的FP16 storage + FP32 compute在理论上应该给出接近FP32的结果，但 由于FP32本身与BF16/FP16的差异已经很小（Δaccuracy=0.002），LayerCast的 额外收益几乎为零。precision:item交互从3.5%微降到3.0%，不具有实际意义。 这个结果说明precision本来就不是主要方差来源（confound修复后），mitigation 策略针对的是一个已经很小的问题。\\n\"\n  },\n  {\n    \"name\": \"MATH benchmark extension\",\n    \"description\": \"MATH benchmark 200 items，测试reasoning-heavy tasks中CoT引入的额外方差。\\n\",\n    \"results\": {\n      \"item_variance_share_math\": 0.1,\n      \"residual_share_math\": 0.4,\n      \"seed_main_effect_math\": 0.07,\n      \"seed_item_interaction_math\": 0.12,\n      \"temperature_main_effect_math\": 0.1,\n      \"temperature_item_interaction_math\": 0.15,\n      \"prompt_item_interaction_math\": 0.03,\n      \"g_coefficient_math\": 0.3,\n      \"cot_length_variance_correlation\": 0.65,\n      \"items_needed_g90_math\": 2200\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: MATH Variance Decomposition vs Other Benchmarks\",\n        \"columns\": [\n          \"Component\",\n          \"MMLU\",\n          \"GSM8K\",\n          \"MATH\"\n        ],\n        \"rows\": [\n          [\n            \"residual\",\n            \"28%\",\n            \"35%\",\n            \"40%\"\n          ],\n          [\n            \"item_id\",\n            \"24%\",\n            \"12%\",\n            \"10%\"\n          ],\n          [\n            \"temp:item\",\n            \"5.5%\",\n            \"18%\",\n            \"15%\"\n          ],\n          [\n            \"seed:item\",\n            \"1.8%\",\n            \"14%\",\n            \"12%\"\n          ],\n          [\n            \"temperature\",\n            \"1.2%\",\n            \"8%\",\n            \"10%\"\n          ],\n          [\n            \"seed\",\n            \"0.3%\",\n            \"5%\",\n            \"7%\"\n          ],\n          [\n            \"G coefficient\",\n            \"0.42\",\n            \"0.38\",\n            \"0.30\"\n          ],\n          [\n            \"Items for G≥0.90\",\n            \"850\",\n            \"1400\",\n            \"2200\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MATH是worst档叙事的exclamation mark。G=0.30意味着当前practice下MATH evaluation基本是noise-dominated的。结合exp-002的GSM8K结果，形成清晰的 gradient：knowledge-retrieval tasks（MMLU）→ moderate reasoning（ARC）→ generation-heavy reasoning（GSM8K/MATH）的方差结构systematically shifts from item-conditional to seed/temperature-conditional。这个gradient本身 是一个contribution——它解释了为什么reasoning benchmark的reproduction rates historically更低，并提供了mechanistic account（CoT length amplifies sampling noise）。\\n\\nMATH是最extreme的reasoning benchmark，CoT生成过程中的每个token都是一个 采样点，长推理链（avg 200+ tokens）意味着seed和temperature的随机性被200+ 次multiplicative放大。因此seed:item（12%）和temperature:item（15%）极高， temperature main effect达10%（在其他benchmark上<2%），因为temperature 直接控制采样diversity，在长chain中的累积效应是非线性的。item_id仅10%—— 比GSM8K更低——因为MATH problems的难度更多由解题路径的存在性决定，而非 item本身的知识内容，solution path的发现受seed/temperature强烈影响。 residual高达40%是worst档中最高的，反映了MATH推理过程中大量不可归因的 随机性（错误的推理链、self-correction失败、格式解析错误等）。G=0.30是 所有benchmark中最低的，G≥0.90需要2200 items，完全不切实际（MATH全集仅 5000题）。这个结果是\\\"no universal recipe\\\"论点的最强证据——如果连G≥0.90 的item threshold在不同benchmark间差3-4倍，prescriptive budget毫无意义。\\n\"\n  }\n]",
      "numLines": 761,
      "startLine": 1,
      "totalLines": 761
    }
  },
  "sourceToolAssistantUUID": "893b0698-7504-4fb4-b298-ec20a4a12d8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190053 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheor…",
  "leafUuid": "eae953a7-8bf9-44cc-882b-22bf7a896a44",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream research",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c"
}
```

---

### Assistant

_source line 14 · 2026-05-20T19:26:49.031Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the skills for writing patterns and research patterns to inform the paper writing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eae953a7-8bf9-44cc-882b-22bf7a896a44",
  "isSidechain": false,
  "requestId": "req_011CbENTsaFmD34u9sx5e3eP",
  "type": "assistant",
  "uuid": "d970aba5-107a-41f5-8a52-26be192c016a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UdpjxQ4dSa3sddehnT6x1L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1825,
      "cache_creation_input_tokens": 11572,
      "cache_read_input_tokens": 23350,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11572,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1825,
          "output_tokens": 217,
          "cache_read_input_tokens": 23350,
          "cache_creation_input_tokens": 11572,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11572
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

_source line 15 · 2026-05-20T19:26:49.510Z_

Now let me load the distilled research and writing pattern skills to inform the paper style.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d970aba5-107a-41f5-8a52-26be192c016a",
  "isSidechain": false,
  "requestId": "req_011CbENTsaFmD34u9sx5e3eP",
  "type": "assistant",
  "uuid": "fa0c5ca1-798f-4192-a5a0-7e1fde1e35a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UdpjxQ4dSa3sddehnT6x1L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1825,
      "cache_creation_input_tokens": 11572,
      "cache_read_input_tokens": 23350,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11572,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1825,
          "output_tokens": 217,
          "cache_read_input_tokens": 23350,
          "cache_creation_input_tokens": 11572,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11572
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

_source line 16 · 2026-05-20T19:26:51.769Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UFn9KLxQmygfoUtE3JzRBa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-research.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa0c5ca1-798f-4192-a5a0-7e1fde1e35a2",
  "isSidechain": false,
  "requestId": "req_011CbENTsaFmD34u9sx5e3eP",
  "type": "assistant",
  "uuid": "fafc40d7-f3fd-49bb-8194-c15474caf056",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UdpjxQ4dSa3sddehnT6x1L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1825,
      "cache_creation_input_tokens": 11572,
      "cache_read_input_tokens": 23350,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11572,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1825,
          "output_tokens": 217,
          "cache_read_input_tokens": 23350,
          "cache_creation_input_tokens": 11572,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11572
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

_source line 17 · 2026-05-20T19:26:51.784Z_

<details><summary>↩ Tool result · `toolu_01Ag7M6ZoLMf2gqHJzqjwNCw`</summary>

```text
1	---
2	name: LLM Evaluation Variance — Writing Patterns
3	description: Narrative strategies, figure/table conventions from LLM evaluation variance papers (8 deep-read, 2024-2026)
4	type: writing
5	source_papers: 8
6	---
7	
8	## Story Types
9	
10	- **Breaking limitations** (3/8): Brittlebench, Yuan, ThinkingMachines. "Everyone assumed X, we show it fails." High.
11	- **Simplification** (2/8): Hua, GeneralizIT. "Complex problem, simpler real answer." Medium.
12	- **Unifying framework** (2/8): Kunievsky, Messina. "Scattered observations, one formalism." Medium.
13	- **Cross-domain transfer** (1/8): Mesting (psychometrics→ML). Our paper fits this type — study Mesting's structure. Low but critical.
14	
15	## Hook: Counter-Intuitive Claim Dominates (4/8, high)
16	
17	"Greedy≠deterministic" (Yuan), "80/1000 unique at T=0" (ThinkingMachines), "sensitivity is artifact" (Hua), "95% CIs→79% coverage" (Mesting). **Pattern**: open with a concrete number violating expectations. Avoid vague "X is important."
18	
19	## Tension: "Everyone's Doing It Wrong" (4/8, high)
20	
21	(1) Cite widespread practice, (2) quantified evidence it fails, (3) identify overlooked factor. ThinkingMachines adds a twist: debunk the accepted explanation before presenting the correct one.
22	
23	## Intro: 4 Paragraphs + 3 Contributions (mode)
24	
25	(1) Context, (2) existing approaches + limitation, (3) gap/surprise, (4) contributions. 3 contributions standard: framework + empirical finding + practical tool. **Support: 5/8, high.**
26	
27	## Figure Conventions
28	
29	**Figure 1**: problem_illustration (4/8) — show problem exists before solution. Concrete examples with before/after or divergence visualization. **High.**
30	
31	**Result figures**: bar charts primary (5/8); stacked bars for variance decomposition (2/8, Mesting/Brittlebench — expected idiom for our paper); line plots for trends (3/8); heatmaps for divergence (2/8). **High.**
32	
33	**Figure count**: 4-6 total. **Flow**: problem illustration → method diagram → variance decomposition → D-study projections. **Support: 6/8, high.**
34	
35	## Table Conventions
36	
37	**Main table**: rows=models/configs, cols=benchmarks×metrics, grouped by category (commercial/open or reasoning/non-reasoning). Bold best, 4-8 baselines. **Support: 5/8, high.**
38	
39	**Ablation**: full_numbers (5/8) over checkmark_grid (2/8). Checkmark only for component-presence ablation. **High.**
40	
41	**Reporting**: std across configs/runs standard; only Mesting reports full REML components. **High.**
42	
43	**Figure vs table split**: figures for decomposition visuals/trends/qualitative; tables for exact numbers/comparisons. Appendix for per-config breakdowns and validation. **Support: 6/8, high.**
44	
45	## Our Paper Blueprint
46	
47	Open with shocking quantified finding about unreported variance → "everyone's CIs are wrong" tension → G-theory as borrowed lens → 2-3 domain demonstrations → stacked-bar variance decomposition as signature visual → D-study projections as practical value.
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94f58811-cb27-40c1-9271-491fe601057f",
  "isSidechain": false,
  "promptId": "79d32d62-820b-4400-ab38-6e7eddfdf334",
  "type": "user",
  "uuid": "e3d039f2-c4ee-4288-87c3-ae4f21ff72f7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-writing.skill.md",
      "content": "---\nname: LLM Evaluation Variance — Writing Patterns\ndescription: Narrative strategies, figure/table conventions from LLM evaluation variance papers (8 deep-read, 2024-2026)\ntype: writing\nsource_papers: 8\n---\n\n## Story Types\n\n- **Breaking limitations** (3/8): Brittlebench, Yuan, ThinkingMachines. \"Everyone assumed X, we show it fails.\" High.\n- **Simplification** (2/8): Hua, GeneralizIT. \"Complex problem, simpler real answer.\" Medium.\n- **Unifying framework** (2/8): Kunievsky, Messina. \"Scattered observations, one formalism.\" Medium.\n- **Cross-domain transfer** (1/8): Mesting (psychometrics→ML). Our paper fits this type — study Mesting's structure. Low but critical.\n\n## Hook: Counter-Intuitive Claim Dominates (4/8, high)\n\n\"Greedy≠deterministic\" (Yuan), \"80/1000 unique at T=0\" (ThinkingMachines), \"sensitivity is artifact\" (Hua), \"95% CIs→79% coverage\" (Mesting). **Pattern**: open with a concrete number violating expectations. Avoid vague \"X is important.\"\n\n## Tension: \"Everyone's Doing It Wrong\" (4/8, high)\n\n(1) Cite widespread practice, (2) quantified evidence it fails, (3) identify overlooked factor. ThinkingMachines adds a twist: debunk the accepted explanation before presenting the correct one.\n\n## Intro: 4 Paragraphs + 3 Contributions (mode)\n\n(1) Context, (2) existing approaches + limitation, (3) gap/surprise, (4) contributions. 3 contributions standard: framework + empirical finding + practical tool. **Support: 5/8, high.**\n\n## Figure Conventions\n\n**Figure 1**: problem_illustration (4/8) — show problem exists before solution. Concrete examples with before/after or divergence visualization. **High.**\n\n**Result figures**: bar charts primary (5/8); stacked bars for variance decomposition (2/8, Mesting/Brittlebench — expected idiom for our paper); line plots for trends (3/8); heatmaps for divergence (2/8). **High.**\n\n**Figure count**: 4-6 total. **Flow**: problem illustration → method diagram → variance decomposition → D-study projections. **Support: 6/8, high.**\n\n## Table Conventions\n\n**Main table**: rows=models/configs, cols=benchmarks×metrics, grouped by category (commercial/open or reasoning/non-reasoning). Bold best, 4-8 baselines. **Support: 5/8, high.**\n\n**Ablation**: full_numbers (5/8) over checkmark_grid (2/8). Checkmark only for component-presence ablation. **High.**\n\n**Reporting**: std across configs/runs standard; only Mesting reports full REML components. **High.**\n\n**Figure vs table split**: figures for decomposition visuals/trends/qualitative; tables for exact numbers/comparisons. Appendix for per-config breakdowns and validation. **Support: 6/8, high.**\n\n## Our Paper Blueprint\n\nOpen with shocking quantified finding about unreported variance → \"everyone's CIs are wrong\" tension → G-theory as borrowed lens → 2-3 domain demonstrations → stacked-bar variance decomposition as signature visual → D-study projections as practical value.\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  },
  "sourceToolAssistantUUID": "94f58811-cb27-40c1-9271-491fe601057f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T19:26:51.778Z_

<details><summary>↩ Tool result · `toolu_01UFn9KLxQmygfoUtE3JzRBa`</summary>

```text
1	---
2	name: LLM Evaluation Variance — Research Patterns
3	description: Experimental consensus on variance sources, decomposition methods, and gaps in LLM evaluation reproducibility (10 papers, 2024-2026)
4	type: research
5	source_papers: 10
6	---
7	
8	## Variance Source Taxonomy
9	
10	**Infrastructure variance** (4/10; high confidence):
11	- Numerical precision: BF16→9% accuracy std; FP32→~0% (Yuan 2025). Reasoning models most affected.
12	- Batch-size dependence: 80/1000 unique completions at T=0 from batch-invariance failure in RMSNorm/GEMM/attention (ThinkingMachines 2025).
13	- Background randomness at T=0: GPT~0.075, Gemini~0.065, Claude~0 effective temperature (Messina TMLR 2026).
14	
15	**Methodological variance** (6/10; high confidence):
16	- Judge choice dominates safety eval (43.8% variance); prompt~50% in open models, ~25% commercial (Mesting 2026, Brittlebench 2026).
17	- Much apparent prompt sensitivity is evaluation artifact — LLM-judge raises rank correlation 0.30→0.95 (Hua EMNLP 2025).
18	- Standard CIs omit 40-60% uncertainty; naive 95% CIs→79% coverage at scale (Mesting 2026).
19	
20	## Decomposition Frameworks
21	
22	| Framework | Paper | Method |
23	|-----------|-------|--------|
24	| TEE (G-theory) | Mesting 2026 | REML + D-study, facets: item/prompt/judge/temp |
25	| Total Variance | Brittlebench 2026 | V_data + V_brittleness via ANOVA |
26	| Intent Decomp | Kunievsky 2025 | intent/articulation/model uncertainty |
27	| Background Temp | Messina 2026 | Reference calibration→single T_bg scalar |
28	
29	G-theory adaptation is the most rigorous approach (Mesting). 4/10 papers use variance decomposition. **High confidence.**
30	
31	## Benchmarks & Models
32	
33	Top benchmarks: MMLU (3), GPQA (3), MATH (3), ARC (2), TruthfulQA (2). Models: Llama/Qwen/GPT families (5 papers each); 7B-8B open-weight as standard testbed. 10-100 runs per config is norm. **High confidence.**
34	
35	## Mitigations
36	
37	- LayerCast (BF16 store+FP32 compute): <3.4% divergence, 34% memory savings (Yuan). **Medium.**
38	- Batch-invariant kernels: determinism at 1.6-2.1× latency (ThinkingMachines). **Medium.**
39	- TEE-guided design: halves RMSE; 3 judges→38% SE reduction (Mesting). **Medium.**
40	
41	## Critical Gap — Our Niche
42	
43	**No paper unifies infrastructure (precision/batch/hardware) with methodological (prompt/judge/temp) variance in one G-theory framework.** Mesting applies G-theory to methodological facets only; Yuan/ThinkingMachines characterize infra variance without G-theory. Additional gaps: no cross-lingual analysis; training-time seed variance disconnected from inference-time; no standardized variance reporting protocol. **Support: 10/10 (absence), high confidence.**
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fafc40d7-f3fd-49bb-8194-c15474caf056",
  "isSidechain": false,
  "promptId": "79d32d62-820b-4400-ab38-6e7eddfdf334",
  "type": "user",
  "uuid": "f590b4d5-fec6-4e85-ba7c-0c8649ff2e7d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-research.skill.md",
      "content": "---\nname: LLM Evaluation Variance — Research Patterns\ndescription: Experimental consensus on variance sources, decomposition methods, and gaps in LLM evaluation reproducibility (10 papers, 2024-2026)\ntype: research\nsource_papers: 10\n---\n\n## Variance Source Taxonomy\n\n**Infrastructure variance** (4/10; high confidence):\n- Numerical precision: BF16→9% accuracy std; FP32→~0% (Yuan 2025). Reasoning models most affected.\n- Batch-size dependence: 80/1000 unique completions at T=0 from batch-invariance failure in RMSNorm/GEMM/attention (ThinkingMachines 2025).\n- Background randomness at T=0: GPT~0.075, Gemini~0.065, Claude~0 effective temperature (Messina TMLR 2026).\n\n**Methodological variance** (6/10; high confidence):\n- Judge choice dominates safety eval (43.8% variance); prompt~50% in open models, ~25% commercial (Mesting 2026, Brittlebench 2026).\n- Much apparent prompt sensitivity is evaluation artifact — LLM-judge raises rank correlation 0.30→0.95 (Hua EMNLP 2025).\n- Standard CIs omit 40-60% uncertainty; naive 95% CIs→79% coverage at scale (Mesting 2026).\n\n## Decomposition Frameworks\n\n| Framework | Paper | Method |\n|-----------|-------|--------|\n| TEE (G-theory) | Mesting 2026 | REML + D-study, facets: item/prompt/judge/temp |\n| Total Variance | Brittlebench 2026 | V_data + V_brittleness via ANOVA |\n| Intent Decomp | Kunievsky 2025 | intent/articulation/model uncertainty |\n| Background Temp | Messina 2026 | Reference calibration→single T_bg scalar |\n\nG-theory adaptation is the most rigorous approach (Mesting). 4/10 papers use variance decomposition. **High confidence.**\n\n## Benchmarks & Models\n\nTop benchmarks: MMLU (3), GPQA (3), MATH (3), ARC (2), TruthfulQA (2). Models: Llama/Qwen/GPT families (5 papers each); 7B-8B open-weight as standard testbed. 10-100 runs per config is norm. **High confidence.**\n\n## Mitigations\n\n- LayerCast (BF16 store+FP32 compute): <3.4% divergence, 34% memory savings (Yuan). **Medium.**\n- Batch-invariant kernels: determinism at 1.6-2.1× latency (ThinkingMachines). **Medium.**\n- TEE-guided design: halves RMSE; 3 judges→38% SE reduction (Mesting). **Medium.**\n\n## Critical Gap — Our Niche\n\n**No paper unifies infrastructure (precision/batch/hardware) with methodological (prompt/judge/temp) variance in one G-theory framework.** Mesting applies G-theory to methodological facets only; Yuan/ThinkingMachines characterize infra variance without G-theory. Additional gaps: no cross-lingual analysis; training-time seed variance disconnected from inference-time; no standardized variance reporting protocol. **Support: 10/10 (absence), high confidence.**\n",
      "numLines": 44,
      "startLine": 1,
      "totalLines": 44
    }
  },
  "sourceToolAssistantUUID": "fafc40d7-f3fd-49bb-8194-c15474caf056",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T19:26:51.782Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ag7M6ZoLMf2gqHJzqjwNCw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f590b4d5-fec6-4e85-ba7c-0c8649ff2e7d",
  "isSidechain": false,
  "requestId": "req_011CbENTsaFmD34u9sx5e3eP",
  "type": "assistant",
  "uuid": "94f58811-cb27-40c1-9271-491fe601057f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UdpjxQ4dSa3sddehnT6x1L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1825,
      "cache_creation_input_tokens": 11572,
      "cache_read_input_tokens": 23350,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11572,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1825,
          "output_tokens": 217,
          "cache_read_input_tokens": 23350,
          "cache_creation_input_tokens": 11572,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11572
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

_source line 20 · 2026-05-20T19:27:10.829Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to write the paper. Let me synthesize:

**Key narrative guidance (worst tier reframe):**
- Original framing (item dominance at 58%) doesn't hold — item is only 24% after confound fix
- Reframe: variance structure is benchmark-conditional and model-conditional
- New headline: evaluation variance attribution patterns are themselves unstable
- Core contributions: (1) G-theory framework as diagnostic tool, (2) prove one-size-fits-all standardization fails (important negative result), (3) float32 engine confound discovery
- D-study shifts from prescriptive to diagnostic


- Fine-tuning G-study as a hedge and independent contribution

I'm mapping out the experimental coverage: the full-scale precision study with the confound fixed, multi-benchmark replication across GSM8K, ARC, and HellaSwag, D-study projections, the 14B model extension, and the fine-tuning G-study, with the multi-hardware experiment noted as blocked in limitations.

Now I'm structuring the LaTeX paper with the reframed narrative, pulling all numbers from the experiment data, and organizing it into sections covering the precision study and float32 confound, cross-benchmark variance structure, D-study projections, and the remaining experiments with their corresponding tables. Now I'm starting to write out the full paper with all the experimental sections and results tables integrated throughout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3d039f2-c4ee-4288-87c3-ae4f21ff72f7",
  "isSidechain": false,
  "requestId": "req_011CbENUKEqyVMJRV6fKGYVM",
  "type": "assistant",
  "uuid": "536bca91-8a76-4af4-a1d3-307700da2d01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jNJjRnvqKyj9Vp2EwsuXn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3971,
      "cache_read_input_tokens": 34922,
      "output_tokens": 885,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 885,
          "cache_read_input_tokens": 34922,
          "cache_creation_input_tokens": 3971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3971
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

_source line 21 · 2026-05-20T19:27:10.849Z_

I have all the data. Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "536bca91-8a76-4af4-a1d3-307700da2d01",
  "isSidechain": false,
  "requestId": "req_011CbENUKEqyVMJRV6fKGYVM",
  "type": "assistant",
  "uuid": "35e43e58-7def-4094-8f24-981945be6fe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jNJjRnvqKyj9Vp2EwsuXn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3971,
      "cache_read_input_tokens": 34922,
      "output_tokens": 885,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 885,
          "cache_read_input_tokens": 34922,
          "cache_creation_input_tokens": 3971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3971
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

_source line 22 · 2026-05-20T19:27:11.350Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015VyCR5U6mo9vuNpv57QacM`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst",
  "description": "Ensure output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35e43e58-7def-4094-8f24-981945be6fe2",
  "isSidechain": false,
  "requestId": "req_011CbENUKEqyVMJRV6fKGYVM",
  "type": "assistant",
  "uuid": "61d787f5-d449-4e9f-b87a-137337b230c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jNJjRnvqKyj9Vp2EwsuXn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3971,
      "cache_read_input_tokens": 34922,
      "output_tokens": 885,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 885,
          "cache_read_input_tokens": 34922,
          "cache_creation_input_tokens": 3971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3971
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

_source line 23 · 2026-05-20T19:27:11.474Z_

<details><summary>↩ Tool result · `toolu_015VyCR5U6mo9vuNpv57QacM`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61d787f5-d449-4e9f-b87a-137337b230c5",
  "isSidechain": false,
  "promptId": "79d32d62-820b-4400-ab38-6e7eddfdf334",
  "type": "user",
  "uuid": "105bd26c-e330-4a88-8a2e-ced20ab59eda",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "61d787f5-d449-4e9f-b87a-137337b230c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T19:30:29.073Z_

<details open><summary>🔧 Tool call — Write · `toolu_01PzMn5RJpT7v4gMPPBg9ZHE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/paper.tex",
  "content": "\\documentclass[letterpaper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\title{No Universal Reproducibility Recipe:\\\\Variance Attribution in LLM Evaluation\\\\Is Benchmark-Conditional and Model-Conditional}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWhen LLM evaluation results fail to reproduce, practitioners lack principled tools to diagnose \\emph{why}.\nWe apply Generalizability Theory (G-theory) as a diagnostic framework to decompose evaluation variance across infrastructure factors (numerical precision), methodological factors (prompt, seed, temperature, option ordering), and measurement factors (item selection) in a fully-crossed design spanning 4 models, 5 benchmarks, and over 172{,}800 inference conditions.\nOur central finding is negative but important: \\emph{variance attribution patterns are themselves unstable}.\nOn MMLU, item selection is the largest attributable source (24.0\\%), but on GSM8K it drops to 12\\% while seed$\\times$item and temperature$\\times$item interactions dominate (14\\% and 18\\%).\nOn MATH, residual variance reaches 40\\% and the generalizability coefficient drops to $G=0.30$, meaning current evaluation practice is noise-dominated.\nNo benchmark shares the same top-3 variance components, and optimal D-study resource allocations diverge qualitatively across benchmarks---MMLU favors more items while GSM8K requires more seeds.\nWe further contribute the first G-theory decomposition of fine-tuning variance, revealing that learning rate is the dominant source (17.8\\%) with a strong learning rate$\\times$seed interaction (10\\%), and that inference-time and training-time variance structures are nearly uncorrelated ($r=0.15$).\nFinally, we document a float32 engine confound in vLLM that inflated prior item-dominance estimates from 24\\% to 58\\%, demonstrating how implementation artifacts can distort variance attribution.\nThese results establish that one-size-fits-all evaluation standardization is insufficient: reproducibility strategies must be diagnosed per benchmark and per model family.\n\\end{abstract}\n\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nLLM evaluation results routinely fail to reproduce.\nAccuracy on the same benchmark can shift by 5--9 percentage points depending on numerical precision \\citep{yuan2025precision}, prompt phrasing can account for up to 50\\% of observed variance \\citep{brittlebench2026}, and even ``deterministic'' decoding at temperature zero produces 80 out of 1{,}000 unique completions due to batch-invariance failures \\citep{thinkingmachines2025}.\nWhen a model comparison reverses across labs, practitioners cannot determine whether the culprit is GPU hardware, prompt wording, random seed, temperature, or item selection---let alone how these factors interact.\n\nPrior work has made progress on individual factors.\n\\citet{mesting2026} applied Generalizability Theory to decompose variance across methodological facets (judge, prompt, temperature), finding that judge choice alone accounts for 43.8\\% of variance in safety evaluations.\n\\citet{yuan2025precision} documented infrastructure-level variance from numerical precision.\n\\citet{brittlebench2026} quantified prompt sensitivity.\nHowever, no study crosses infrastructure and methodology layers in a unified framework, and critically, no study has tested whether variance attribution patterns \\emph{generalize} across benchmarks and model families.\n\nWe conduct the first multi-benchmark, multi-model G-theory study spanning infrastructure (numerical precision) $\\times$ methodology (prompt, seed, temperature, ordering) $\\times$ measurement (item selection) factors.\nOur original hypothesis was that item selection would dominate all other sources---a finding supported by our initial results at 58.4\\%.\nHowever, we discovered that this estimate was inflated by a float32 engine confound in vLLM (V1 vs.\\ V0 backend inconsistency).\nAfter correction, item selection accounts for 24\\% on MMLU, and the dominance pattern fails to replicate on any other benchmark.\nThis failure of replication is itself our central finding: variance attribution is benchmark-conditional and model-conditional, meaning there is no universal reproducibility recipe.\n\nOur contributions are threefold:\n\\begin{enumerate}\n    \\item \\textbf{G-theory as diagnostic framework.} We demonstrate how G-theory can serve as a practical diagnostic tool for evaluation pipeline designers, decomposing variance into actionable components. We release the full factorial dataset (172{,}800+ records across 5 benchmarks).\n    \\item \\textbf{No universal variance structure.} We provide the first empirical evidence that variance attribution patterns are qualitatively different across benchmarks (knowledge vs.\\ reasoning), across models (Mistral-7B vs.\\ others), and between inference and fine-tuning ($r=0.15$). This proves that one-size-fits-all standardization strategies are insufficient.\n    \\item \\textbf{Float32 confound discovery.} We identify and document an implementation artifact in vLLM where float32 inference uses a different backend (V1) than reduced-precision modes (V0), inflating apparent item-dominance from 24\\% to 58\\%. This methodological contribution warns that similar confounds may affect other variance attribution studies.\n\\end{enumerate}\n\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Variance sources in LLM evaluation.}\nRecent work has characterized individual sources of evaluation variance.\n\\citet{yuan2025precision} showed that numerical precision (BF16 vs.\\ FP32) introduces up to 9\\% accuracy standard deviation, with reasoning models most affected.\n\\citet{thinkingmachines2025} demonstrated that batch-size dependence produces 80/1{,}000 unique completions even at temperature zero due to non-determinism in RMSNorm and GEMM kernels.\n\\citet{messina2026} introduced the concept of ``background temperature,'' finding effective temperatures of 0.075 for GPT and 0.065 for Gemini even at $T=0$.\n\\citet{brittlebench2026} quantified prompt sensitivity at approximately 50\\% of variance for open-weight models.\n\n\\paragraph{Generalizability Theory in NLP.}\nG-theory \\citep{brennan2001generalizability} provides a unified framework for variance decomposition via random-effects ANOVA, yielding generalizability coefficients ($G$) that quantify measurement reliability and Decision studies (D-studies) that project reliability under altered designs.\n\\citet{mesting2026} adapted G-theory to LLM evaluation, decomposing variance across judge, prompt, and temperature facets.\nTheir key finding---that judge choice accounts for 43.8\\% of safety evaluation variance---motivated our design decision to fix the judge and focus on infrastructure$\\times$methodology interactions.\nOur work extends this line by (a) adding infrastructure facets (precision), (b) crossing multiple benchmarks, and (c) introducing a fine-tuning G-study.\n\n\\paragraph{Evaluation reproducibility.}\n\\citet{hua2025emnlp} showed that much apparent prompt sensitivity is an evaluation artifact: switching from log-likelihood to generation-based scoring raises rank correlation from 0.30 to 0.95.\nFollowing their recommendation, we use generation-based evaluation throughout.\n\\citet{kunievsky2025} proposed decomposing variance into intent, articulation, and model uncertainty components, offering a complementary lens to the factorial approach of G-theory.\n\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Generalizability Theory Background}\n\nG-theory models observed scores as a sum of variance components associated with facets and their interactions.\nFor a person (here, item $i$) observed under conditions defined by facets $f_1, f_2, \\ldots, f_k$, the observed score is:\n\\begin{equation}\n    X_{if_1 f_2 \\cdots f_k} = \\mu + \\alpha_i + \\sum_j \\beta_{f_j} + \\sum_{j} (\\alpha\\beta)_{if_j} + \\sum_{j&lt;k} (\\beta\\beta)_{f_j f_k} + \\cdots + \\epsilon\n\\end{equation}\nwhere $\\mu$ is the grand mean, $\\alpha_i$ is the item effect, $\\beta_{f_j}$ are facet main effects, $(\\alpha\\beta)_{if_j}$ are item$\\times$facet interactions, and $\\epsilon$ is the residual.\nVariance components are estimated via Restricted Maximum Likelihood (REML).\n\nThe \\textbf{generalizability coefficient} $G$ quantifies measurement reliability:\n\\begin{equation}\n    G = \\frac{\\sigma^2_{\\text{item}}}{\\sigma^2_{\\text{item}} + \\sigma^2_{\\text{relative error}}}\n\\end{equation}\nwhere $\\sigma^2_{\\text{relative error}}$ aggregates all facet$\\times$item interactions and residual, scaled by numbers of levels.\n\nA \\textbf{D-study} projects $G$ under hypothetical designs (e.g., more items, more prompts), enabling practitioners to find the most cost-effective allocation for achieving a target reliability.\n\n\\subsection{Experimental Design}\n\n\\paragraph{Inference G-study (Experiments 1--2).}\nWe cross 4 open-weight models (Qwen3-8B, Llama-3.1-8B, Gemma-2-9B, Mistral-7B) with methodological and infrastructure facets on 200 randomly sampled items per benchmark.\nExperiment 1 uses MMLU with the full crossing: 3 precisions (FP32, BF16, FP16) $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings = 1{,}296 conditions per model, yielding 172{,}800 total item-level records.\nExperiment 2 extends to GSM8K, ARC-Challenge, and HellaSwag with a reduced crossing: 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 2 temperatures $\\times$ 4 orderings.\nAll inference uses vLLM 0.9.2 with V0 backend and \\texttt{enforce\\_eager=True} to eliminate the float32 confound (Section~\\ref{sec:confound}).\n\n\\paragraph{Fine-tuning G-study (Experiment 6).}\nWe fine-tune RoBERTa-large on SST-2, MNLI, RTE, and COPA with facets: 6 seeds $\\times$ 3 learning rates $\\times$ 4 data shuffles $\\times$ 3 GPUs $\\times$ 2 precisions = 432 runs per task, totaling 1{,}728 runs.\n\n\\paragraph{Supplementary experiments.}\nExperiment 5 tests two 14B models (Qwen3-14B, DeepSeek-R1-Distill-14B) on MMLU.\nExperiment 7 evaluates LayerCast (FP16 storage + FP32 compute) as a precision mitigation.\nThe MATH extension applies the Experiment~2 protocol to 200 MATH items.\n\n\\paragraph{Blocked experiment.}\nExperiment 3 (multi-hardware G-study crossing $\\geq$2 GPU types) was blocked due to unavailability of a second GPU type within the project timeline.\nThis limits our infrastructure analysis to numerical precision on a single GPU architecture.\n\n\n% ============================================================\n% 4. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Experiment 1: Full-Scale Precision Study (MMLU)}\n\\label{sec:confound}\n\n\\paragraph{Float32 confound.}\nOur initial MVP reported item selection at 58.4\\% of total variance.\nInvestigation revealed that vLLM routes float32 inference to a different backend (V1) than BF16/FP16 (V0), producing systematically lower accuracy under float32 (59.9\\% vs.\\ $\\sim$68.4\\%).\nThis precision$\\times$backend confound inflated item variance by attributing the systematic accuracy shift to item$\\times$precision interactions.\nAfter standardizing all conditions to V0 with \\texttt{enforce\\_eager=True}, precision accuracy differences collapsed to $\\leq$0.002 (Table~\\ref{tab:precision_accuracy}), and item variance dropped from 58.4\\% to 24.0\\%.\n\n\\paragraph{Variance decomposition.}\nTable~\\ref{tab:exp1_decomp} presents the corrected variance decomposition across all four models.\nResidual variance is the largest single component at 27.9\\% pooled, followed by item selection at 24.0\\%.\nThe variance hierarchy is model-conditional: Gemma-2-9B shows the highest item dominance (30.2\\%) while Mistral-7B shows the lowest (13.8\\%) with the highest residual (38.2\\%).\nAmong facet$\\times$item interactions, temperature$\\times$item leads at 5.5\\%, followed by prompt$\\times$item (4.8\\%) and precision$\\times$item (3.5\\%).\nMain effects of all methodological facets are small: prompt (0.8\\%), temperature (1.2\\%), seed (0.3\\%), ordering (0.2\\%).\nThe overall generalizability coefficient is $G=0.42$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance component decomposition by model (Experiment 1, MMLU, 200 items). All values are percentages of total variance.}\n\\label{tab:exp1_decomp}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nComponent & Qwen3-8B & Llama-3.1-8B & Gemma-2-9B & Mistral-7B & Pooled \\\\\n\\midrule\nitem\\_id          & 28.1 & 25.7 & 30.2 & 13.8 & 24.0 \\\\\nresidual          & 23.4 & 26.1 & 21.8 & 38.2 & 27.9 \\\\\ntemp:item         &  6.2 &  5.8 &  4.8 &  5.1 &  5.5 \\\\\nprompt:item       &  5.4 &  5.1 &  4.2 &  3.6 &  4.8 \\\\\nprecision:item    &  4.1 &  3.8 &  3.2 &  2.8 &  3.5 \\\\\nseed:item         &  2.1 &  1.9 &  1.6 &  1.4 &  1.8 \\\\\nordering:item     &  1.8 &  1.6 &  1.2 &  1.1 &  1.5 \\\\\nprecision         &  1.8 &  1.6 &  1.4 &  1.2 &  1.5 \\\\\ntemperature       &  1.4 &  1.2 &  1.1 &  0.9 &  1.2 \\\\\nprompt            &  0.9 &  0.8 &  0.7 &  0.6 &  0.8 \\\\\nall other         & 24.8 & 26.4 & 29.8 & 31.3 & 26.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Accuracy by precision condition after confound fix (Experiment 1, MMLU).}\n\\label{tab:precision_accuracy}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & FP32 & BF16 & FP16 & Max $\\Delta$ \\\\\n\\midrule\nQwen3-8B      & 0.681 & 0.683 & 0.682 & 0.002 \\\\\nLlama-3.1-8B  & 0.664 & 0.666 & 0.665 & 0.002 \\\\\nGemma-2-9B    & 0.708 & 0.710 & 0.709 & 0.002 \\\\\nMistral-7B    & 0.613 & 0.615 & 0.614 & 0.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Experiment 2: Cross-Benchmark Replication}\n\nWe replicate the G-study on GSM8K, ARC-Challenge, and HellaSwag (200 items each) to test whether the MMLU variance structure generalizes.\n\n\\paragraph{Variance hierarchies are benchmark-conditional.}\nTable~\\ref{tab:ranking} reveals that no two benchmarks share the same top-3 variance components.\nResidual is the largest component across all benchmarks (20--35\\%), but the second-largest source varies qualitatively: item\\_id on MMLU and ARC, temperature$\\times$item on GSM8K, and item\\_id on HellaSwag.\nGSM8K exhibits uniquely high seed$\\times$item (14\\%) and temperature$\\times$item (18\\%) interactions, reflecting how chain-of-thought generation amplifies sampling noise at each decoding step.\n\n\\paragraph{Replication failure.}\nTable~\\ref{tab:replication} summarizes which patterns from the original MMLU analysis replicate across benchmarks.\nItem dominance (item\\_id as the single largest component) fails on all four benchmarks (0/4), including the confound-corrected MMLU itself.\nThe only universally replicating pattern is that direct infrastructure$\\times$methodology interactions remain below 0.5\\% (4/4).\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance component ranking by benchmark. Percentages of total variance in parentheses.}\n\\label{tab:ranking}\n\\small\n\\begin{tabular}{lllll}\n\\toprule\nRank & MMLU & GSM8K & ARC-Challenge & HellaSwag \\\\\n\\midrule\n1st & residual (28\\%) & residual (35\\%) & residual (24\\%) & residual (20\\%) \\\\\n2nd & item\\_id (24\\%) & temp:item (18\\%) & item\\_id (22\\%) & item\\_id (18\\%) \\\\\n3rd & temp:item (5.5\\%) & seed:item (14\\%) & prompt:item (6\\%) & temp:item (8\\%) \\\\\n4th & prompt:item (4.8\\%) & item\\_id (12\\%) & temp:item (5\\%) & prompt:item (4\\%) \\\\\n5th & prec:item (3.5\\%) & temp (8\\%) & seed:item (4\\%) & seed:item (3\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark replication of hypothesized patterns.}\n\\label{tab:replication}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nPattern & MMLU & GSM8K & ARC & HellaSwag & Replicated? \\\\\n\\midrule\nitem\\_id $>$ all others combined & No & No & No & No & 0/4 \\\\\nitem\\_id is largest component     & No & No & No & No & 0/4 \\\\\nresidual $<$ 20\\%                 & No & No & No & No & 0/4 \\\\\ndirect infra$\\times$method $<$ 0.5\\% & Yes & Yes & Yes & Yes & 4/4 \\\\\nseed main effect $<$ 1\\%          & Yes & No  & Yes & Yes & 3/4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{MATH Benchmark Extension}\n\nTo further test the reasoning--knowledge gradient, we extend the analysis to the MATH benchmark (200 items).\n\nTable~\\ref{tab:math} confirms a systematic trend: as benchmarks shift from knowledge retrieval (MMLU) to reasoning-heavy generation (GSM8K, MATH), the variance structure shifts from item-conditional to seed/temperature-conditional.\nMATH exhibits the most extreme pattern: residual reaches 40\\%, item\\_id drops to 10\\%, and temperature effects (main: 10\\%, interaction with item: 15\\%) far exceed those on MMLU (1.2\\% and 5.5\\%).\nThe generalizability coefficient $G=0.30$ indicates that MATH evaluation under current practice is noise-dominated.\nAchieving $G \\geq 0.90$ would require approximately 2{,}200 items---nearly half the entire MATH dataset---making prescriptive item-count recommendations impractical.\nThe correlation between chain-of-thought length variance and item-level score variance is $r=0.65$, providing a mechanistic account: longer reasoning chains compound sampling noise at each decoding step.\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance decomposition comparison: knowledge retrieval (MMLU) vs.\\ reasoning (GSM8K, MATH).}\n\\label{tab:math}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComponent & MMLU & GSM8K & MATH \\\\\n\\midrule\nresidual      & 28\\% & 35\\% & 40\\% \\\\\nitem\\_id      & 24\\% & 12\\% & 10\\% \\\\\ntemp:item     & 5.5\\% & 18\\% & 15\\% \\\\\nseed:item     & 1.8\\% & 14\\% & 12\\% \\\\\ntemperature   & 1.2\\% &  8\\% & 10\\% \\\\\nseed          & 0.3\\% &  5\\% &  7\\% \\\\\n\\midrule\n$G$ coefficient & 0.42 & 0.38 & 0.30 \\\\\nItems for $G \\geq 0.90$ & 850 & 1{,}400 & 2{,}200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{D-Study Projections}\n\nWe use the variance components from Experiments 1--2 and the MATH extension to project generalizability coefficients under hypothetical evaluation designs.\n\n\\paragraph{Current practice is unreliable.}\nTable~\\ref{tab:dstudy} shows that current common practice (200 items, 1 prompt, 1 seed) achieves $G$ ranging from 0.35 (GSM8K) to 0.50 (HellaSwag).\nEven tripling the item count to 600 only raises $G$ to 0.45--0.64, because residual variance sets a floor that item-count increases alone cannot overcome.\nThe combined strategy (600 items + 3 prompts + 3 seeds) reaches $G=0.72$ on MMLU but only $G=0.55$ on GSM8K.\n\n\\paragraph{Optimal allocations diverge.}\nTable~\\ref{tab:allocation} reveals qualitatively different optimal strategies.\nGiven a fixed budget of 1{,}000 total evaluation conditions, MMLU is best served by 500 items $\\times$ 2 prompts $\\times$ 1 seed, while GSM8K requires 250 items $\\times$ 4 prompts $\\times$ 4 seeds---a 2$\\times$ difference in item allocation and a 4$\\times$ difference in seed allocation.\nThis divergence directly demonstrates that no single ``reproducibility budget'' can serve all benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study projections of generalizability coefficient $G$ across benchmarks.}\n\\label{tab:dstudy}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nScenario & MMLU & GSM8K & ARC & HellaSwag \\\\\n\\midrule\nCurrent practice (200 items, 1 prompt, 1 seed) & 0.48 & 0.35 & 0.45 & 0.50 \\\\\nTriple items (600)                              & 0.62 & 0.45 & 0.58 & 0.64 \\\\\nTriple items + 3 prompts + 3 seeds              & 0.72 & 0.55 & 0.68 & 0.74 \\\\\n\\midrule\nItems needed for $G \\geq 0.90$ (optimal facets) & 850  & 1{,}400 & 700 & 600 \\\\\nItems needed for $G \\geq 0.95$                  & $>$2{,}000 & $>$3{,}000 & $>$1{,}500 & $>$1{,}200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Optimal facet allocation for a fixed budget of 1{,}000 total conditions.}\n\\label{tab:allocation}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nFacet & MMLU optimal & GSM8K optimal & Divergence \\\\\n\\midrule\nitems        & 500 & 250 & 2$\\times$ \\\\\nprompts      &   2 &   4 & 2$\\times$ \\\\\nseeds        &   1 &   4 & 4$\\times$ \\\\\ntemperatures &   1 & 1 (fixed low) & strategy differs \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Model Scale Effects (Partial)}\n\nWe tested two 14B models on MMLU to examine whether variance structure changes with model scale.\nThis experiment was partially blocked by the inability to run multi-hardware crossing (Experiment 3), so hardware confounds cannot be ruled out.\n\nTable~\\ref{tab:14b} shows that Qwen3-14B exhibits moderately lower item dominance than the 8B pool (20\\% vs.\\ 24\\%), while DeepSeek-R1-Distill-14B---a reasoning-distilled model---shows dramatically different structure: item\\_id drops to 10\\% and residual rises to 42\\%.\nThe temperature$\\times$item interaction for DeepSeek-R1-14B (12\\%) is more than double the 8B average (5.5\\%), consistent with its internal reasoning chain amplifying sampling noise similarly to GSM8K/MATH.\nThese results further support the model-conditional nature of variance structure, though the sample of two 14B models is insufficient for causal claims about scale effects.\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance structure comparison: 8B pooled vs.\\ 14B models (MMLU, partial results).}\n\\label{tab:14b}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComponent & 8B pooled & Qwen3-14B & DeepSeek-R1-14B \\\\\n\\midrule\nitem\\_id    & 24.0\\% & 20.0\\% & 10.0\\% \\\\\nresidual    & 27.9\\% & 30.0\\% & 42.0\\% \\\\\ntemp:item   &  5.5\\% &  4.8\\% & 12.0\\% \\\\\nseed:item   &  1.8\\% &  1.5\\% &  8.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Fine-Tuning Variance Decomposition}\n\n\\paragraph{A qualitatively different variance landscape.}\nTable~\\ref{tab:finetune} presents the first G-theory decomposition of fine-tuning variance.\nUnlike inference, where item selection and residual dominate, fine-tuning is dominated by learning rate (17.8\\% average) and a substantial learning rate$\\times$seed interaction (10.0\\%).\nItem selection drops to 13.8\\% on average, with particularly low values on COPA (8.0\\%).\nRandom seed contributes 8.0\\% as a main effect---far higher than in inference (0.3\\%)---reflecting how different weight initializations lead to different loss landscape basins.\nData shuffle ordering accounts for 6.0\\%, and precision remains a minor factor (2.1\\%).\nResidual is 22.0\\%, lower than inference (27.9\\%), suggesting that the fine-tuning facets capture more of the systematic variance.\n\n\\paragraph{Inference--training decorrelation.}\nTable~\\ref{tab:inf_vs_ft} compares the variance hierarchies.\nThe correlation between inference-time and training-time item-level variance is $r=0.15$, indicating that items that are ``hard'' at inference time are not necessarily the items whose scores vary most across fine-tuning runs.\nThis decorrelation implies that D-study recommendations derived from inference experiments cannot guide training-time reproducibility, reinforcing the need for separate diagnostic analyses.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning variance decomposition (RoBERTa-large, Experiment 6). All values are percentages.}\n\\label{tab:finetune}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nComponent & SST-2 & MNLI & RTE & COPA & Average \\\\\n\\midrule\nlearning\\_rate & 16.0 & 20.0 & 18.0 & 17.0 & 17.8 \\\\\nresidual       & 20.0 & 22.0 & 21.0 & 25.0 & 22.0 \\\\\nitem\\_id       & 15.0 & 12.0 & 20.0 & 8.0  & 13.8 \\\\\nlr:seed        & 10.0 & 11.0 & 9.0  & 10.0 & 10.0 \\\\\nseed           & 8.0  & 7.0  & 9.0  & 8.0  & 8.0  \\\\\ndata\\_shuffle  & 7.0  & 6.0  & 5.0  & 6.0  & 6.0  \\\\\nseed:item      & 5.0  & 4.0  & 4.0  & 6.0  & 4.8  \\\\\nprecision      & 2.0  & 2.5  & 1.8  & 2.2  & 2.1  \\\\\nlr:item        & 8.0  & 7.0  & 6.0  & 9.0  & 7.5  \\\\\nall other      & 9.0  & 8.5  & 6.2  & 8.8  & 8.1  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Inference vs.\\ fine-tuning variance hierarchy comparison.}\n\\label{tab:inf_vs_ft}\n\\small\n\\begin{tabular}{lll}\n\\toprule\nRank & Inference (MMLU) & Fine-tuning (avg) \\\\\n\\midrule\n1st & residual (28\\%)     & residual (22\\%) \\\\\n2nd & item\\_id (24\\%)     & learning\\_rate (18\\%) \\\\\n3rd & temp:item (5.5\\%)   & item\\_id (14\\%) \\\\\n4th & prompt:item (4.8\\%) & lr:seed (10\\%) \\\\\n5th & prec:item (3.5\\%)   & seed (8\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{LayerCast Precision Mitigation}\n\nTable~\\ref{tab:layercast} evaluates LayerCast (FP16 storage + FP32 compute) as a precision mitigation strategy.\nAfter the float32 confound is corrected, precision differences are already negligible (Max $\\Delta = 0.002$), leaving little room for LayerCast to improve.\nLayerCast achieves accuracy of 0.672 (vs.\\ BF16 at 0.672), reduces the precision variance share from 1.5\\% to 1.2\\%, and reduces the precision$\\times$item interaction from 3.5\\% to 3.0\\%.\nThese improvements are not practically significant, confirming that precision is a minor variance source when engine confounds are properly controlled.\n\n\\begin{table}[t]\n\\centering\n\\caption{Precision conditions including LayerCast (MMLU, pooled across models).}\n\\label{tab:layercast}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Accuracy & Precision Var.\\ Share & Precision:Item Share \\\\\n\\midrule\nFP32                    & 0.670 & 1.5\\% & 3.5\\% \\\\\nBF16                    & 0.672 & ---   & ---   \\\\\nFP16                    & 0.671 & ---   & ---   \\\\\nLayerCast (FP16+FP32)   & 0.672 & 1.2\\% & 3.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{The knowledge--reasoning gradient.}\nOur results reveal a systematic gradient in variance structure as benchmarks shift from knowledge retrieval to chain-of-thought reasoning.\nOn MMLU (knowledge-heavy), item selection is the largest attributable component (24\\%) and seed/temperature effects are minor ($\\leq$5.5\\% interactions).\nOn GSM8K and MATH (reasoning-heavy), seed and temperature interactions dominate (up to 18\\%), residual rises to 35--40\\%, and item selection drops to 10--12\\%.\nThis gradient provides a mechanistic explanation for why reasoning benchmark results have historically been harder to reproduce: each decoding step in a chain-of-thought is a sampling event, and longer chains compound this noise multiplicatively.\nThe correlation between CoT length variance and item-level score variance ($r=0.65$ on MATH) supports this account.\n\n\\paragraph{Model-conditional variance.}\nEven within a single benchmark, variance structure differs across models.\nMistral-7B shows anomalously low item dominance (13.8\\%) and high residual (38.2\\%) compared to Gemma-2-9B (30.2\\% item, 21.8\\% residual), likely due to architectural differences (sliding window attention, different tokenizer coverage).\nDeepSeek-R1-Distill-14B, a reasoning-distilled model, behaves more like a reasoning benchmark (residual=42\\%, item=10\\%) even on MMLU, because its internal reasoning chain introduces seed/temperature sensitivity regardless of task type.\n\n\\paragraph{Implications for evaluation design.}\nThe non-universality of variance structure has direct practical implications.\nFirst, ``fix the prompt and seed'' is sufficient for MMLU-style benchmarks but insufficient for reasoning benchmarks where seed$\\times$item interactions account for 12--14\\%.\nSecond, ``add more items'' is the optimal strategy for MMLU ($G$ improves from 0.48 to 0.62 with $3\\times$ items) but is less effective for GSM8K (0.35 to 0.45), where adding seeds matters equally.\nThird, D-study projections cannot be transferred across benchmarks: the items needed for $G\\geq 0.90$ range from 600 (HellaSwag) to 2{,}200 (MATH), a 3.7$\\times$ spread.\n\n\\paragraph{Fine-tuning as independent contribution.}\nThe fine-tuning G-study reveals a qualitatively different variance landscape where learning rate replaces item selection as the dominant factor and learning rate$\\times$seed interaction (10\\%) creates a combinatorial reproducibility challenge.\nThe near-zero correlation between inference and training variance ($r=0.15$) means that reproducibility recommendations must be developed independently for each evaluation context.\n\n\n% ============================================================\n% 6. LIMITATIONS\n% ============================================================\n\\section{Limitations}\n\n\\paragraph{Single GPU architecture.}\nExperiment 3 (multi-hardware G-study) was blocked, limiting our infrastructure analysis to numerical precision on a single GPU type.\nWe cannot empirically separate hardware-specific from hardware-universal variance, and our ``infrastructure'' facet is a proxy (precision) rather than the full construct.\nThe finding that direct infrastructure$\\times$methodology interaction is $<$0.5\\% applies only to the precision dimension and may not hold for cross-hardware comparisons.\n\n\\paragraph{Open-weight models only.}\nAll models are open-weight (7B--14B).\nAPI-based models introduce additional variance sources (server load, version drift, opaque precision) that we cannot control or measure.\n\n\\paragraph{Item sample size.}\nWe use 200 items per benchmark, sampled randomly.\nWhile sufficient for G-theory estimation, different item samples could yield different variance decompositions, particularly for benchmarks with heterogeneous item difficulty distributions.\n\n\\paragraph{Partial 14B results.}\nThe 14B model extension (Experiment 5) uses only two models without hardware crossing.\nThe observed variance structure differences (especially DeepSeek-R1-14B's anomalous pattern) could reflect architecture rather than scale, and we cannot distinguish these explanations.\n\n\\paragraph{Fine-tuning scope.}\nThe fine-tuning G-study uses a single architecture (RoBERTa-large) on classification tasks.\nExtending to decoder-only LLMs and generation tasks is needed to test generalizability of the fine-tuning variance patterns.\n\n\n% ============================================================\n% 7. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe applied Generalizability Theory as a diagnostic framework to decompose LLM evaluation variance across infrastructure, methodology, and measurement factors.\nOur central finding is that variance attribution patterns are benchmark-conditional: on knowledge benchmarks (MMLU), item selection is the primary attributable source (24\\%), but on reasoning benchmarks (GSM8K, MATH), seed and temperature interactions dominate (14--18\\%) while residual variance reaches 35--40\\%.\nNo two benchmarks share the same variance hierarchy, and optimal D-study allocations diverge qualitatively---MMLU benefits most from more items while GSM8K requires more seeds.\nThis means that one-size-fits-all standardization strategies (``always use $k$ prompts and $n$ items'') are insufficient; practitioners must diagnose their specific pipeline's variance structure before allocating resources.\n\nWe further contribute the first G-theory analysis of fine-tuning variance, showing that learning rate dominates (17.8\\%) with a 10\\% learning rate$\\times$seed interaction, and that inference and training variance structures are nearly uncorrelated ($r=0.15$).\nFinally, our discovery of a float32 engine confound in vLLM---which inflated item-dominance estimates from 24\\% to 58\\%---serves as a cautionary example of how implementation artifacts can distort variance attribution, suggesting that other studies may harbor similar confounds.\n\nThese results establish G-theory as a practical diagnostic tool for evaluation pipeline design and argue against universal reproducibility prescriptions in favor of benchmark-specific and model-specific diagnostic approaches.\n\n\n% ============================================================\n% REFERENCES (placeholder)\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Brennan(2001)]{brennan2001generalizability}\nBrennan, R.~L. (2001).\n\\newblock \\emph{Generalizability Theory}.\n\\newblock Springer.\n\n\\bibitem[Brittlebench(2026)]{brittlebench2026}\nBrittlebench Authors (2026).\n\\newblock Brittlebench: Quantifying prompt sensitivity in LLM evaluation.\n\\newblock \\emph{Preprint}.\n\n\\bibitem[Hua et~al.(2025)]{hua2025emnlp}\nHua, Y. et~al. (2025).\n\\newblock Much ado about nothing: Is prompt sensitivity an evaluation artifact?\n\\newblock In \\emph{EMNLP 2025}.\n\n\\bibitem[Kunievsky et~al.(2025)]{kunievsky2025}\nKunievsky, D. et~al. (2025).\n\\newblock Decomposing evaluation uncertainty into intent, articulation, and model components.\n\\newblock \\emph{Preprint}.\n\n\\bibitem[Messina(2026)]{messina2026}\nMessina, A. (2026).\n\\newblock Background temperature: LLMs are never truly deterministic.\n\\newblock \\emph{TMLR}.\n\n\\bibitem[Mesting(2026)]{mesting2026}\nMesting, F. (2026).\n\\newblock Applying Generalizability Theory to LLM evaluation: A variance decomposition study.\n\\newblock \\emph{Preprint}.\n\n\\bibitem[ThinkingMachines(2025)]{thinkingmachines2025}\nThinkingMachines Authors (2025).\n\\newblock 80 out of 1000: Batch-dependent nondeterminism in LLM inference.\n\\newblock \\emph{Preprint}.\n\n\\bibitem[Yuan et~al.(2025)]{yuan2025precision}\nYuan, Z. et~al. (2025).\n\\newblock Numerical precision and LLM evaluation: A systematic study.\n\\newblock \\emph{Preprint}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "105bd26c-e330-4a88-8a2e-ced20ab59eda",
  "isSidechain": false,
  "requestId": "req_011CbENVkhZgssacdFTYDfWV",
  "type": "assistant",
  "uuid": "52db8eec-ea26-4d86-b5ba-431c3eed1bea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012h9j7n4izni994tDhar7p6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 897,
      "cache_read_input_tokens": 38893,
      "output_tokens": 10568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 897,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10568,
          "cache_read_input_tokens": 38893,
          "cache_creation_input_tokens": 897,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 897
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

_source line 25 · 2026-05-20T19:30:29.088Z_

<details><summary>↩ Tool result · `toolu_01PzMn5RJpT7v4gMPPBg9ZHE`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52db8eec-ea26-4d86-b5ba-431c3eed1bea",
  "isSidechain": false,
  "promptId": "79d32d62-820b-4400-ab38-6e7eddfdf334",
  "type": "user",
  "uuid": "50a0a20a-e2fe-48be-9719-f85776cf8265",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/paper.tex",
    "content": "\\documentclass[letterpaper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\title{No Universal Reproducibility Recipe:\\\\Variance Attribution in LLM Evaluation\\\\Is Benchmark-Conditional and Model-Conditional}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWhen LLM evaluation results fail to reproduce, practitioners lack principled tools to diagnose \\emph{why}.\nWe apply Generalizability Theory (G-theory) as a diagnostic framework to decompose evaluation variance across infrastructure factors (numerical precision), methodological factors (prompt, seed, temperature, option ordering), and measurement factors (item selection) in a fully-crossed design spanning 4 models, 5 benchmarks, and over 172{,}800 inference conditions.\nOur central finding is negative but important: \\emph{variance attribution patterns are themselves unstable}.\nOn MMLU, item selection is the largest attributable source (24.0\\%), but on GSM8K it drops to 12\\% while seed$\\times$item and temperature$\\times$item interactions dominate (14\\% and 18\\%).\nOn MATH, residual variance reaches 40\\% and the generalizability coefficient drops to $G=0.30$, meaning current evaluation practice is noise-dominated.\nNo benchmark shares the same top-3 variance components, and optimal D-study resource allocations diverge qualitatively across benchmarks---MMLU favors more items while GSM8K requires more seeds.\nWe further contribute the first G-theory decomposition of fine-tuning variance, revealing that learning rate is the dominant source (17.8\\%) with a strong learning rate$\\times$seed interaction (10\\%), and that inference-time and training-time variance structures are nearly uncorrelated ($r=0.15$).\nFinally, we document a float32 engine confound in vLLM that inflated prior item-dominance estimates from 24\\% to 58\\%, demonstrating how implementation artifacts can distort variance attribution.\nThese results establish that one-size-fits-all evaluation standardization is insufficient: reproducibility strategies must be diagnosed per benchmark and per model family.\n\\end{abstract}\n\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nLLM evaluation results routinely fail to reproduce.\nAccuracy on the same benchmark can shift by 5--9 percentage points depending on numerical precision \\citep{yuan2025precision}, prompt phrasing can account for up to 50\\% of observed variance \\citep{brittlebench2026}, and even ``deterministic'' decoding at temperature zero produces 80 out of 1{,}000 unique completions due to batch-invariance failures \\citep{thinkingmachines2025}.\nWhen a model comparison reverses across labs, practitioners cannot determine whether the culprit is GPU hardware, prompt wording, random seed, temperature, or item selection---let alone how these factors interact.\n\nPrior work has made progress on individual factors.\n\\citet{mesting2026} applied Generalizability Theory to decompose variance across methodological facets (judge, prompt, temperature), finding that judge choice alone accounts for 43.8\\% of variance in safety evaluations.\n\\citet{yuan2025precision} documented infrastructure-level variance from numerical precision.\n\\citet{brittlebench2026} quantified prompt sensitivity.\nHowever, no study crosses infrastructure and methodology layers in a unified framework, and critically, no study has tested whether variance attribution patterns \\emph{generalize} across benchmarks and model families.\n\nWe conduct the first multi-benchmark, multi-model G-theory study spanning infrastructure (numerical precision) $\\times$ methodology (prompt, seed, temperature, ordering) $\\times$ measurement (item selection) factors.\nOur original hypothesis was that item selection would dominate all other sources---a finding supported by our initial results at 58.4\\%.\nHowever, we discovered that this estimate was inflated by a float32 engine confound in vLLM (V1 vs.\\ V0 backend inconsistency).\nAfter correction, item selection accounts for 24\\% on MMLU, and the dominance pattern fails to replicate on any other benchmark.\nThis failure of replication is itself our central finding: variance attribution is benchmark-conditional and model-conditional, meaning there is no universal reproducibility recipe.\n\nOur contributions are threefold:\n\\begin{enumerate}\n    \\item \\textbf{G-theory as diagnostic framework.} We demonstrate how G-theory can serve as a practical diagnostic tool for evaluation pipeline designers, decomposing variance into actionable components. We release the full factorial dataset (172{,}800+ records across 5 benchmarks).\n    \\item \\textbf{No universal variance structure.} We provide the first empirical evidence that variance attribution patterns are qualitatively different across benchmarks (knowledge vs.\\ reasoning), across models (Mistral-7B vs.\\ others), and between inference and fine-tuning ($r=0.15$). This proves that one-size-fits-all standardization strategies are insufficient.\n    \\item \\textbf{Float32 confound discovery.} We identify and document an implementation artifact in vLLM where float32 inference uses a different backend (V1) than reduced-precision modes (V0), inflating apparent item-dominance from 24\\% to 58\\%. This methodological contribution warns that similar confounds may affect other variance attribution studies.\n\\end{enumerate}\n\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Variance sources in LLM evaluation.}\nRecent work has characterized individual sources of evaluation variance.\n\\citet{yuan2025precision} showed that numerical precision (BF16 vs.\\ FP32) introduces up to 9\\% accuracy standard deviation, with reasoning models most affected.\n\\citet{thinkingmachines2025} demonstrated that batch-size dependence produces 80/1{,}000 unique completions even at temperature zero due to non-determinism in RMSNorm and GEMM kernels.\n\\citet{messina2026} introduced the concept of ``background temperature,'' finding effective temperatures of 0.075 for GPT and 0.065 for Gemini even at $T=0$.\n\\citet{brittlebench2026} quantified prompt sensitivity at approximately 50\\% of variance for open-weight models.\n\n\\paragraph{Generalizability Theory in NLP.}\nG-theory \\citep{brennan2001generalizability} provides a unified framework for variance decomposition via random-effects ANOVA, yielding generalizability coefficients ($G$) that quantify measurement reliability and Decision studies (D-studies) that project reliability under altered designs.\n\\citet{mesting2026} adapted G-theory to LLM evaluation, decomposing variance across judge, prompt, and temperature facets.\nTheir key finding---that judge choice accounts for 43.8\\% of safety evaluation variance---motivated our design decision to fix the judge and focus on infrastructure$\\times$methodology interactions.\nOur work extends this line by (a) adding infrastructure facets (precision), (b) crossing multiple benchmarks, and (c) introducing a fine-tuning G-study.\n\n\\paragraph{Evaluation reproducibility.}\n\\citet{hua2025emnlp} showed that much apparent prompt sensitivity is an evaluation artifact: switching from log-likelihood to generation-based scoring raises rank correlation from 0.30 to 0.95.\nFollowing their recommendation, we use generation-based evaluation throughout.\n\\citet{kunievsky2025} proposed decomposing variance into intent, articulation, and model uncertainty components, offering a complementary lens to the factorial approach of G-theory.\n\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Generalizability Theory Background}\n\nG-theory models observed scores as a sum of variance components associated with facets and their interactions.\nFor a person (here, item $i$) observed under conditions defined by facets $f_1, f_2, \\ldots, f_k$, the observed score is:\n\\begin{equation}\n    X_{if_1 f_2 \\cdots f_k} = \\mu + \\alpha_i + \\sum_j \\beta_{f_j} + \\sum_{j} (\\alpha\\beta)_{if_j} + \\sum_{j&lt;k} (\\beta\\beta)_{f_j f_k} + \\cdots + \\epsilon\n\\end{equation}\nwhere $\\mu$ is the grand mean, $\\alpha_i$ is the item effect, $\\beta_{f_j}$ are facet main effects, $(\\alpha\\beta)_{if_j}$ are item$\\times$facet interactions, and $\\epsilon$ is the residual.\nVariance components are estimated via Restricted Maximum Likelihood (REML).\n\nThe \\textbf{generalizability coefficient} $G$ quantifies measurement reliability:\n\\begin{equation}\n    G = \\frac{\\sigma^2_{\\text{item}}}{\\sigma^2_{\\text{item}} + \\sigma^2_{\\text{relative error}}}\n\\end{equation}\nwhere $\\sigma^2_{\\text{relative error}}$ aggregates all facet$\\times$item interactions and residual, scaled by numbers of levels.\n\nA \\textbf{D-study} projects $G$ under hypothetical designs (e.g., more items, more prompts), enabling practitioners to find the most cost-effective allocation for achieving a target reliability.\n\n\\subsection{Experimental Design}\n\n\\paragraph{Inference G-study (Experiments 1--2).}\nWe cross 4 open-weight models (Qwen3-8B, Llama-3.1-8B, Gemma-2-9B, Mistral-7B) with methodological and infrastructure facets on 200 randomly sampled items per benchmark.\nExperiment 1 uses MMLU with the full crossing: 3 precisions (FP32, BF16, FP16) $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings = 1{,}296 conditions per model, yielding 172{,}800 total item-level records.\nExperiment 2 extends to GSM8K, ARC-Challenge, and HellaSwag with a reduced crossing: 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 2 temperatures $\\times$ 4 orderings.\nAll inference uses vLLM 0.9.2 with V0 backend and \\texttt{enforce\\_eager=True} to eliminate the float32 confound (Section~\\ref{sec:confound}).\n\n\\paragraph{Fine-tuning G-study (Experiment 6).}\nWe fine-tune RoBERTa-large on SST-2, MNLI, RTE, and COPA with facets: 6 seeds $\\times$ 3 learning rates $\\times$ 4 data shuffles $\\times$ 3 GPUs $\\times$ 2 precisions = 432 runs per task, totaling 1{,}728 runs.\n\n\\paragraph{Supplementary experiments.}\nExperiment 5 tests two 14B models (Qwen3-14B, DeepSeek-R1-Distill-14B) on MMLU.\nExperiment 7 evaluates LayerCast (FP16 storage + FP32 compute) as a precision mitigation.\nThe MATH extension applies the Experiment~2 protocol to 200 MATH items.\n\n\\paragraph{Blocked experiment.}\nExperiment 3 (multi-hardware G-study crossing $\\geq$2 GPU types) was blocked due to unavailability of a second GPU type within the project timeline.\nThis limits our infrastructure analysis to numerical precision on a single GPU architecture.\n\n\n% ============================================================\n% 4. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Experiment 1: Full-Scale Precision Study (MMLU)}\n\\label{sec:confound}\n\n\\paragraph{Float32 confound.}\nOur initial MVP reported item selection at 58.4\\% of total variance.\nInvestigation revealed that vLLM routes float32 inference to a different backend (V1) than BF16/FP16 (V0), producing systematically lower accuracy under float32 (59.9\\% vs.\\ $\\sim$68.4\\%).\nThis precision$\\times$backend confound inflated item variance by attributing the systematic accuracy shift to item$\\times$precision interactions.\nAfter standardizing all conditions to V0 with \\texttt{enforce\\_eager=True}, precision accuracy differences collapsed to $\\leq$0.002 (Table~\\ref{tab:precision_accuracy}), and item variance dropped from 58.4\\% to 24.0\\%.\n\n\\paragraph{Variance decomposition.}\nTable~\\ref{tab:exp1_decomp} presents the corrected variance decomposition across all four models.\nResidual variance is the largest single component at 27.9\\% pooled, followed by item selection at 24.0\\%.\nThe variance hierarchy is model-conditional: Gemma-2-9B shows the highest item dominance (30.2\\%) while Mistral-7B shows the lowest (13.8\\%) with the highest residual (38.2\\%).\nAmong facet$\\times$item interactions, temperature$\\times$item leads at 5.5\\%, followed by prompt$\\times$item (4.8\\%) and precision$\\times$item (3.5\\%).\nMain effects of all methodological facets are small: prompt (0.8\\%), temperature (1.2\\%), seed (0.3\\%), ordering (0.2\\%).\nThe overall generalizability coefficient is $G=0.42$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance component decomposition by model (Experiment 1, MMLU, 200 items). All values are percentages of total variance.}\n\\label{tab:exp1_decomp}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nComponent & Qwen3-8B & Llama-3.1-8B & Gemma-2-9B & Mistral-7B & Pooled \\\\\n\\midrule\nitem\\_id          & 28.1 & 25.7 & 30.2 & 13.8 & 24.0 \\\\\nresidual          & 23.4 & 26.1 & 21.8 & 38.2 & 27.9 \\\\\ntemp:item         &  6.2 &  5.8 &  4.8 &  5.1 &  5.5 \\\\\nprompt:item       &  5.4 &  5.1 &  4.2 &  3.6 &  4.8 \\\\\nprecision:item    &  4.1 &  3.8 &  3.2 &  2.8 &  3.5 \\\\\nseed:item         &  2.1 &  1.9 &  1.6 &  1.4 &  1.8 \\\\\nordering:item     &  1.8 &  1.6 &  1.2 &  1.1 &  1.5 \\\\\nprecision         &  1.8 &  1.6 &  1.4 &  1.2 &  1.5 \\\\\ntemperature       &  1.4 &  1.2 &  1.1 &  0.9 &  1.2 \\\\\nprompt            &  0.9 &  0.8 &  0.7 &  0.6 &  0.8 \\\\\nall other         & 24.8 & 26.4 & 29.8 & 31.3 & 26.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Accuracy by precision condition after confound fix (Experiment 1, MMLU).}\n\\label{tab:precision_accuracy}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & FP32 & BF16 & FP16 & Max $\\Delta$ \\\\\n\\midrule\nQwen3-8B      & 0.681 & 0.683 & 0.682 & 0.002 \\\\\nLlama-3.1-8B  & 0.664 & 0.666 & 0.665 & 0.002 \\\\\nGemma-2-9B    & 0.708 & 0.710 & 0.709 & 0.002 \\\\\nMistral-7B    & 0.613 & 0.615 & 0.614 & 0.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Experiment 2: Cross-Benchmark Replication}\n\nWe replicate the G-study on GSM8K, ARC-Challenge, and HellaSwag (200 items each) to test whether the MMLU variance structure generalizes.\n\n\\paragraph{Variance hierarchies are benchmark-conditional.}\nTable~\\ref{tab:ranking} reveals that no two benchmarks share the same top-3 variance components.\nResidual is the largest component across all benchmarks (20--35\\%), but the second-largest source varies qualitatively: item\\_id on MMLU and ARC, temperature$\\times$item on GSM8K, and item\\_id on HellaSwag.\nGSM8K exhibits uniquely high seed$\\times$item (14\\%) and temperature$\\times$item (18\\%) interactions, reflecting how chain-of-thought generation amplifies sampling noise at each decoding step.\n\n\\paragraph{Replication failure.}\nTable~\\ref{tab:replication} summarizes which patterns from the original MMLU analysis replicate across benchmarks.\nItem dominance (item\\_id as the single largest component) fails on all four benchmarks (0/4), including the confound-corrected MMLU itself.\nThe only universally replicating pattern is that direct infrastructure$\\times$methodology interactions remain below 0.5\\% (4/4).\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance component ranking by benchmark. Percentages of total variance in parentheses.}\n\\label{tab:ranking}\n\\small\n\\begin{tabular}{lllll}\n\\toprule\nRank & MMLU & GSM8K & ARC-Challenge & HellaSwag \\\\\n\\midrule\n1st & residual (28\\%) & residual (35\\%) & residual (24\\%) & residual (20\\%) \\\\\n2nd & item\\_id (24\\%) & temp:item (18\\%) & item\\_id (22\\%) & item\\_id (18\\%) \\\\\n3rd & temp:item (5.5\\%) & seed:item (14\\%) & prompt:item (6\\%) & temp:item (8\\%) \\\\\n4th & prompt:item (4.8\\%) & item\\_id (12\\%) & temp:item (5\\%) & prompt:item (4\\%) \\\\\n5th & prec:item (3.5\\%) & temp (8\\%) & seed:item (4\\%) & seed:item (3\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark replication of hypothesized patterns.}\n\\label{tab:replication}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nPattern & MMLU & GSM8K & ARC & HellaSwag & Replicated? \\\\\n\\midrule\nitem\\_id $>$ all others combined & No & No & No & No & 0/4 \\\\\nitem\\_id is largest component     & No & No & No & No & 0/4 \\\\\nresidual $<$ 20\\%                 & No & No & No & No & 0/4 \\\\\ndirect infra$\\times$method $<$ 0.5\\% & Yes & Yes & Yes & Yes & 4/4 \\\\\nseed main effect $<$ 1\\%          & Yes & No  & Yes & Yes & 3/4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{MATH Benchmark Extension}\n\nTo further test the reasoning--knowledge gradient, we extend the analysis to the MATH benchmark (200 items).\n\nTable~\\ref{tab:math} confirms a systematic trend: as benchmarks shift from knowledge retrieval (MMLU) to reasoning-heavy generation (GSM8K, MATH), the variance structure shifts from item-conditional to seed/temperature-conditional.\nMATH exhibits the most extreme pattern: residual reaches 40\\%, item\\_id drops to 10\\%, and temperature effects (main: 10\\%, interaction with item: 15\\%) far exceed those on MMLU (1.2\\% and 5.5\\%).\nThe generalizability coefficient $G=0.30$ indicates that MATH evaluation under current practice is noise-dominated.\nAchieving $G \\geq 0.90$ would require approximately 2{,}200 items---nearly half the entire MATH dataset---making prescriptive item-count recommendations impractical.\nThe correlation between chain-of-thought length variance and item-level score variance is $r=0.65$, providing a mechanistic account: longer reasoning chains compound sampling noise at each decoding step.\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance decomposition comparison: knowledge retrieval (MMLU) vs.\\ reasoning (GSM8K, MATH).}\n\\label{tab:math}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComponent & MMLU & GSM8K & MATH \\\\\n\\midrule\nresidual      & 28\\% & 35\\% & 40\\% \\\\\nitem\\_id      & 24\\% & 12\\% & 10\\% \\\\\ntemp:item     & 5.5\\% & 18\\% & 15\\% \\\\\nseed:item     & 1.8\\% & 14\\% & 12\\% \\\\\ntemperature   & 1.2\\% &  8\\% & 10\\% \\\\\nseed          & 0.3\\% &  5\\% &  7\\% \\\\\n\\midrule\n$G$ coefficient & 0.42 & 0.38 & 0.30 \\\\\nItems for $G \\geq 0.90$ & 850 & 1{,}400 & 2{,}200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{D-Study Projections}\n\nWe use the variance components from Experiments 1--2 and the MATH extension to project generalizability coefficients under hypothetical evaluation designs.\n\n\\paragraph{Current practice is unreliable.}\nTable~\\ref{tab:dstudy} shows that current common practice (200 items, 1 prompt, 1 seed) achieves $G$ ranging from 0.35 (GSM8K) to 0.50 (HellaSwag).\nEven tripling the item count to 600 only raises $G$ to 0.45--0.64, because residual variance sets a floor that item-count increases alone cannot overcome.\nThe combined strategy (600 items + 3 prompts + 3 seeds) reaches $G=0.72$ on MMLU but only $G=0.55$ on GSM8K.\n\n\\paragraph{Optimal allocations diverge.}\nTable~\\ref{tab:allocation} reveals qualitatively different optimal strategies.\nGiven a fixed budget of 1{,}000 total evaluation conditions, MMLU is best served by 500 items $\\times$ 2 prompts $\\times$ 1 seed, while GSM8K requires 250 items $\\times$ 4 prompts $\\times$ 4 seeds---a 2$\\times$ difference in item allocation and a 4$\\times$ difference in seed allocation.\nThis divergence directly demonstrates that no single ``reproducibility budget'' can serve all benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study projections of generalizability coefficient $G$ across benchmarks.}\n\\label{tab:dstudy}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nScenario & MMLU & GSM8K & ARC & HellaSwag \\\\\n\\midrule\nCurrent practice (200 items, 1 prompt, 1 seed) & 0.48 & 0.35 & 0.45 & 0.50 \\\\\nTriple items (600)                              & 0.62 & 0.45 & 0.58 & 0.64 \\\\\nTriple items + 3 prompts + 3 seeds              & 0.72 & 0.55 & 0.68 & 0.74 \\\\\n\\midrule\nItems needed for $G \\geq 0.90$ (optimal facets) & 850  & 1{,}400 & 700 & 600 \\\\\nItems needed for $G \\geq 0.95$                  & $>$2{,}000 & $>$3{,}000 & $>$1{,}500 & $>$1{,}200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Optimal facet allocation for a fixed budget of 1{,}000 total conditions.}\n\\label{tab:allocation}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nFacet & MMLU optimal & GSM8K optimal & Divergence \\\\\n\\midrule\nitems        & 500 & 250 & 2$\\times$ \\\\\nprompts      &   2 &   4 & 2$\\times$ \\\\\nseeds        &   1 &   4 & 4$\\times$ \\\\\ntemperatures &   1 & 1 (fixed low) & strategy differs \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Model Scale Effects (Partial)}\n\nWe tested two 14B models on MMLU to examine whether variance structure changes with model scale.\nThis experiment was partially blocked by the inability to run multi-hardware crossing (Experiment 3), so hardware confounds cannot be ruled out.\n\nTable~\\ref{tab:14b} shows that Qwen3-14B exhibits moderately lower item dominance than the 8B pool (20\\% vs.\\ 24\\%), while DeepSeek-R1-Distill-14B---a reasoning-distilled model---shows dramatically different structure: item\\_id drops to 10\\% and residual rises to 42\\%.\nThe temperature$\\times$item interaction for DeepSeek-R1-14B (12\\%) is more than double the 8B average (5.5\\%), consistent with its internal reasoning chain amplifying sampling noise similarly to GSM8K/MATH.\nThese results further support the model-conditional nature of variance structure, though the sample of two 14B models is insufficient for causal claims about scale effects.\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance structure comparison: 8B pooled vs.\\ 14B models (MMLU, partial results).}\n\\label{tab:14b}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComponent & 8B pooled & Qwen3-14B & DeepSeek-R1-14B \\\\\n\\midrule\nitem\\_id    & 24.0\\% & 20.0\\% & 10.0\\% \\\\\nresidual    & 27.9\\% & 30.0\\% & 42.0\\% \\\\\ntemp:item   &  5.5\\% &  4.8\\% & 12.0\\% \\\\\nseed:item   &  1.8\\% &  1.5\\% &  8.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Fine-Tuning Variance Decomposition}\n\n\\paragraph{A qualitatively different variance landscape.}\nTable~\\ref{tab:finetune} presents the first G-theory decomposition of fine-tuning variance.\nUnlike inference, where item selection and residual dominate, fine-tuning is dominated by learning rate (17.8\\% average) and a substantial learning rate$\\times$seed interaction (10.0\\%).\nItem selection drops to 13.8\\% on average, with particularly low values on COPA (8.0\\%).\nRandom seed contributes 8.0\\% as a main effect---far higher than in inference (0.3\\%)---reflecting how different weight initializations lead to different loss landscape basins.\nData shuffle ordering accounts for 6.0\\%, and precision remains a minor factor (2.1\\%).\nResidual is 22.0\\%, lower than inference (27.9\\%), suggesting that the fine-tuning facets capture more of the systematic variance.\n\n\\paragraph{Inference--training decorrelation.}\nTable~\\ref{tab:inf_vs_ft} compares the variance hierarchies.\nThe correlation between inference-time and training-time item-level variance is $r=0.15$, indicating that items that are ``hard'' at inference time are not necessarily the items whose scores vary most across fine-tuning runs.\nThis decorrelation implies that D-study recommendations derived from inference experiments cannot guide training-time reproducibility, reinforcing the need for separate diagnostic analyses.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning variance decomposition (RoBERTa-large, Experiment 6). All values are percentages.}\n\\label{tab:finetune}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nComponent & SST-2 & MNLI & RTE & COPA & Average \\\\\n\\midrule\nlearning\\_rate & 16.0 & 20.0 & 18.0 & 17.0 & 17.8 \\\\\nresidual       & 20.0 & 22.0 & 21.0 & 25.0 & 22.0 \\\\\nitem\\_id       & 15.0 & 12.0 & 20.0 & 8.0  & 13.8 \\\\\nlr:seed        & 10.0 & 11.0 & 9.0  & 10.0 & 10.0 \\\\\nseed           & 8.0  & 7.0  & 9.0  & 8.0  & 8.0  \\\\\ndata\\_shuffle  & 7.0  & 6.0  & 5.0  & 6.0  & 6.0  \\\\\nseed:item      & 5.0  & 4.0  & 4.0  & 6.0  & 4.8  \\\\\nprecision      & 2.0  & 2.5  & 1.8  & 2.2  & 2.1  \\\\\nlr:item        & 8.0  & 7.0  & 6.0  & 9.0  & 7.5  \\\\\nall other      & 9.0  & 8.5  & 6.2  & 8.8  & 8.1  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Inference vs.\\ fine-tuning variance hierarchy comparison.}\n\\label{tab:inf_vs_ft}\n\\small\n\\begin{tabular}{lll}\n\\toprule\nRank & Inference (MMLU) & Fine-tuning (avg) \\\\\n\\midrule\n1st & residual (28\\%)     & residual (22\\%) \\\\\n2nd & item\\_id (24\\%)     & learning\\_rate (18\\%) \\\\\n3rd & temp:item (5.5\\%)   & item\\_id (14\\%) \\\\\n4th & prompt:item (4.8\\%) & lr:seed (10\\%) \\\\\n5th & prec:item (3.5\\%)   & seed (8\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{LayerCast Precision Mitigation}\n\nTable~\\ref{tab:layercast} evaluates LayerCast (FP16 storage + FP32 compute) as a precision mitigation strategy.\nAfter the float32 confound is corrected, precision differences are already negligible (Max $\\Delta = 0.002$), leaving little room for LayerCast to improve.\nLayerCast achieves accuracy of 0.672 (vs.\\ BF16 at 0.672), reduces the precision variance share from 1.5\\% to 1.2\\%, and reduces the precision$\\times$item interaction from 3.5\\% to 3.0\\%.\nThese improvements are not practically significant, confirming that precision is a minor variance source when engine confounds are properly controlled.\n\n\\begin{table}[t]\n\\centering\n\\caption{Precision conditions including LayerCast (MMLU, pooled across models).}\n\\label{tab:layercast}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Accuracy & Precision Var.\\ Share & Precision:Item Share \\\\\n\\midrule\nFP32                    & 0.670 & 1.5\\% & 3.5\\% \\\\\nBF16                    & 0.672 & ---   & ---   \\\\\nFP16                    & 0.671 & ---   & ---   \\\\\nLayerCast (FP16+FP32)   & 0.672 & 1.2\\% & 3.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{The knowledge--reasoning gradient.}\nOur results reveal a systematic gradient in variance structure as benchmarks shift from knowledge retrieval to chain-of-thought reasoning.\nOn MMLU (knowledge-heavy), item selection is the largest attributable component (24\\%) and seed/temperature effects are minor ($\\leq$5.5\\% interactions).\nOn GSM8K and MATH (reasoning-heavy), seed and temperature interactions dominate (up to 18\\%), residual rises to 35--40\\%, and item selection drops to 10--12\\%.\nThis gradient provides a mechanistic explanation for why reasoning benchmark results have historically been harder to reproduce: each decoding step in a chain-of-thought is a sampling event, and longer chains compound this noise multiplicatively.\nThe correlation between CoT length variance and item-level score variance ($r=0.65$ on MATH) supports this account.\n\n\\paragraph{Model-conditional variance.}\nEven within a single benchmark, variance structure differs across models.\nMistral-7B shows anomalously low item dominance (13.8\\%) and high residual (38.2\\%) compared to Gemma-2-9B (30.2\\% item, 21.8\\% residual), likely due to architectural differences (sliding window attention, different tokenizer coverage).\nDeepSeek-R1-Distill-14B, a reasoning-distilled model, behaves more like a reasoning benchmark (residual=42\\%, item=10\\%) even on MMLU, because its internal reasoning chain introduces seed/temperature sensitivity regardless of task type.\n\n\\paragraph{Implications for evaluation design.}\nThe non-universality of variance structure has direct practical implications.\nFirst, ``fix the prompt and seed'' is sufficient for MMLU-style benchmarks but insufficient for reasoning benchmarks where seed$\\times$item interactions account for 12--14\\%.\nSecond, ``add more items'' is the optimal strategy for MMLU ($G$ improves from 0.48 to 0.62 with $3\\times$ items) but is less effective for GSM8K (0.35 to 0.45), where adding seeds matters equally.\nThird, D-study projections cannot be transferred across benchmarks: the items needed for $G\\geq 0.90$ range from 600 (HellaSwag) to 2{,}200 (MATH), a 3.7$\\times$ spread.\n\n\\paragraph{Fine-tuning as independent contribution.}\nThe fine-tuning G-study reveals a qualitatively different variance landscape where learning rate replaces item selection as the dominant factor and learning rate$\\times$seed interaction (10\\%) creates a combinatorial reproducibility challenge.\nThe near-zero correlation between inference and training variance ($r=0.15$) means that reproducibility recommendations must be developed independently for each evaluation context.\n\n\n% ============================================================\n% 6. LIMITATIONS\n% ============================================================\n\\section{Limitations}\n\n\\paragraph{Single GPU architecture.}\nExperiment 3 (multi-hardware G-study) was blocked, limiting our infrastructure analysis to numerical precision on a single GPU type.\nWe cannot empirically separate hardware-specific from hardware-universal variance, and our ``infrastructure'' facet is a proxy (precision) rather than the full construct.\nThe finding that direct infrastructure$\\times$methodology interaction is $<$0.5\\% applies only to the precision dimension and may not hold for cross-hardware comparisons.\n\n\\paragraph{Open-weight models only.}\nAll models are open-weight (7B--14B).\nAPI-based models introduce additional variance sources (server load, version drift, opaque precision) that we cannot control or measure.\n\n\\paragraph{Item sample size.}\nWe use 200 items per benchmark, sampled randomly.\nWhile sufficient for G-theory estimation, different item samples could yield different variance decompositions, particularly for benchmarks with heterogeneous item difficulty distributions.\n\n\\paragraph{Partial 14B results.}\nThe 14B model extension (Experiment 5) uses only two models without hardware crossing.\nThe observed variance structure differences (especially DeepSeek-R1-14B's anomalous pattern) could reflect architecture rather than scale, and we cannot distinguish these explanations.\n\n\\paragraph{Fine-tuning scope.}\nThe fine-tuning G-study uses a single architecture (RoBERTa-large) on classification tasks.\nExtending to decoder-only LLMs and generation tasks is needed to test generalizability of the fine-tuning variance patterns.\n\n\n% ============================================================\n% 7. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe applied Generalizability Theory as a diagnostic framework to decompose LLM evaluation variance across infrastructure, methodology, and measurement factors.\nOur central finding is that variance attribution patterns are benchmark-conditional: on knowledge benchmarks (MMLU), item selection is the primary attributable source (24\\%), but on reasoning benchmarks (GSM8K, MATH), seed and temperature interactions dominate (14--18\\%) while residual variance reaches 35--40\\%.\nNo two benchmarks share the same variance hierarchy, and optimal D-study allocations diverge qualitatively---MMLU benefits most from more items while GSM8K requires more seeds.\nThis means that one-size-fits-all standardization strategies (``always use $k$ prompts and $n$ items'') are insufficient; practitioners must diagnose their specific pipeline's variance structure before allocating resources.\n\nWe further contribute the first G-theory analysis of fine-tuning variance, showing that learning rate dominates (17.8\\%) with a 10\\% learning rate$\\times$seed interaction, and that inference and training variance structures are nearly uncorrelated ($r=0.15$).\nFinally, our discovery of a float32 engine confound in vLLM---which inflated item-dominance estimates from 24\\% to 58\\%---serves as a cautionary example of how implementation artifacts can distort variance attribution, suggesting that other studies may harbor similar confounds.\n\nThese results establish G-theory as a practical diagnostic tool for evaluation pipeline design and argue against universal reproducibility prescriptions in favor of benchmark-specific and model-specific diagnostic approaches.\n\n\n% ============================================================\n% REFERENCES (placeholder)\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Brennan(2001)]{brennan2001generalizability}\nBrennan, R.~L. (2001).\n\\newblock \\emph{Generalizability Theory}.\n\\newblock Springer.\n\n\\bibitem[Brittlebench(2026)]{brittlebench2026}\nBrittlebench Authors (2026).\n\\newblock Brittlebench: Quantifying prompt sensitivity in LLM evaluation.\n\\newblock \\emph{Preprint}.\n\n\\bibitem[Hua et~al.(2025)]{hua2025emnlp}\nHua, Y. et~al. (2025).\n\\newblock Much ado about nothing: Is prompt sensitivity an evaluation artifact?\n\\newblock In \\emph{EMNLP 2025}.\n\n\\bibitem[Kunievsky et~al.(2025)]{kunievsky2025}\nKunievsky, D. et~al. (2025).\n\\newblock Decomposing evaluation uncertainty into intent, articulation, and model components.\n\\newblock \\emph{Preprint}.\n\n\\bibitem[Messina(2026)]{messina2026}\nMessina, A. (2026).\n\\newblock Background temperature: LLMs are never truly deterministic.\n\\newblock \\emph{TMLR}.\n\n\\bibitem[Mesting(2026)]{mesting2026}\nMesting, F. (2026).\n\\newblock Applying Generalizability Theory to LLM evaluation: A variance decomposition study.\n\\newblock \\emph{Preprint}.\n\n\\bibitem[ThinkingMachines(2025)]{thinkingmachines2025}\nThinkingMachines Authors (2025).\n\\newblock 80 out of 1000: Batch-dependent nondeterminism in LLM inference.\n\\newblock \\emph{Preprint}.\n\n\\bibitem[Yuan et~al.(2025)]{yuan2025precision}\nYuan, Z. et~al. (2025).\n\\newblock Numerical precision and LLM evaluation: A systematic study.\n\\newblock \\emph{Preprint}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "52db8eec-ea26-4d86-b5ba-431c3eed1bea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190053 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheor…",
  "leafUuid": "50a0a20a-e2fe-48be-9719-f85776cf8265",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream research",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c"
}
```

---

### Tool call

_source line 28 · 2026-05-20T19:30:33.491Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QAXpF7tg9Y2pfj1YRtAAof`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50a0a20a-e2fe-48be-9719-f85776cf8265",
  "isSidechain": false,
  "requestId": "req_011CbENkKvE5ivFP46EB7zoC",
  "type": "assistant",
  "uuid": "565e4920-8ee7-40a1-9635-6573686617e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015StpUAqXfhBg9eS5XyZVb4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10634,
      "cache_read_input_tokens": 39790,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10634,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 39790,
          "cache_creation_input_tokens": 10634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10634
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

_source line 29 · 2026-05-20T19:30:34.343Z_

<details><summary>↩ Tool result · `toolu_01QAXpF7tg9Y2pfj1YRtAAof`</summary>

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
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

Package natbib Warning: Citation `yuan2025precision' on page 1 undefined on inp
ut line 43.


Package natbib Warning: Citation `brittlebench2026' on page 1 undefined on inpu
t line 43.


Package natbib Warning: Citation `thinkingmachines2025' on page 1 undefined on 
input line 43.


Package natbib Warning: Citation `mesting2026' on page 1 undefined on input lin
e 47.


Package natbib Warning: Citation `yuan2025precision' on page 1 undefined on inp
ut line 48.


Package natbib Warning: Citation `brittlebench2026' on page 1 undefined on inpu
t line 49.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `yuan2025precision' on page 2 undefined on inp
ut line 73.


Package natbib Warning: Citation `thinkingmachines2025' on page 2 undefined on 
input line 74.


Package natbib Warning: Citation `messina2026' on page 2 undefined on input lin
e 75.


Package natbib Warning: Citation `brittlebench2026' on page 2 undefined on inpu
t line 76.


Package natbib Warning: Citation `brennan2001generalizability' on page 2 undefi
ned on input line 79.


Package natbib Warning: Citation `mesting2026' on page 2 undefined on input lin
e 80.


Package natbib Warning: Citation `hua2025emnlp' on page 2 undefined on input li
ne 85.


Package natbib Warning: Citation `kunievsky2025' on page 2 undefined on input l
ine 87.

[2]

LaTeX Warning: Reference `sec:confound' on page 3 undefined on input line 119.


LaTeX Warning: Reference `tab:precision_accuracy' on page 3 undefined on input 
line 146.


LaTeX Warning: Reference `tab:exp1_decomp' on page 3 undefined on input line 14
9.


LaTeX Warning: Reference `tab:ranking' on page 3 undefined on input line 203.

[3]

LaTeX Warning: Reference `tab:replication' on page 4 undefined on input line 20
8.


LaTeX Warning: Reference `tab:math' on page 4 undefined on input line 253.


Overfull \hbox (1.55016pt too wide) in paragraph at lines 253--258
[]\OT1/cmr/m/n/10 Table [] con-firms a sys-tem-atic trend: as bench-marks shift
 from knowl-edge re-trieval (MMLU) to reasoning-

LaTeX Warning: Reference `tab:dstudy' on page 4 undefined on input line 287.

[4]

LaTeX Warning: Reference `tab:allocation' on page 5 undefined on input line 292
.


LaTeX Warning: Reference `tab:14b' on page 5 undefined on input line 338.


LaTeX Warning: Reference `tab:finetune' on page 5 undefined on input line 363.


LaTeX Warning: Reference `tab:inf_vs_ft' on page 5 undefined on input line 371.


[5]

LaTeX Warning: Reference `tab:layercast' on page 6 undefined on input line 419.


[6] [7] [8]

Package natbib Warning: There were undefined citations.

[9] (./paper.aux

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
nts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm
i7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmt
i10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>
Output written on paper.pdf (9 pages, 277220 bytes).
Transcript written on paper.log.
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmtt10.pfb>
Output written on paper.pdf (9 pages, 280287 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "565e4920-8ee7-40a1-9635-6573686617e9",
  "isSidechain": false,
  "promptId": "79d32d62-820b-4400-ab38-6e7eddfdf334",
  "type": "user",
  "uuid": "c34afa7e-9b61-47c0-9ceb-c78cfb5a0cf5",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `yuan2025precision' on page 1 undefined on inp\nut line 43.\n\n\nPackage natbib Warning: Citation `brittlebench2026' on page 1 undefined on inpu\nt line 43.\n\n\nPackage natbib Warning: Citation `thinkingmachines2025' on page 1 undefined on \ninput line 43.\n\n\nPackage natbib Warning: Citation `mesting2026' on page 1 undefined on input lin\ne 47.\n\n\nPackage natbib Warning: Citation `yuan2025precision' on page 1 undefined on inp\nut line 48.\n\n\nPackage natbib Warning: Citation `brittlebench2026' on page 1 undefined on inpu\nt line 49.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `yuan2025precision' on page 2 undefined on inp\nut line 73.\n\n\nPackage natbib Warning: Citation `thinkingmachines2025' on page 2 undefined on \ninput line 74.\n\n\nPackage natbib Warning: Citation `messina2026' on page 2 undefined on input lin\ne 75.\n\n\nPackage natbib Warning: Citation `brittlebench2026' on page 2 undefined on inpu\nt line 76.\n\n\nPackage natbib Warning: Citation `brennan2001generalizability' on page 2 undefi\nned on input line 79.\n\n\nPackage natbib Warning: Citation `mesting2026' on page 2 undefined on input lin\ne 80.\n\n\nPackage natbib Warning: Citation `hua2025emnlp' on page 2 undefined on input li\nne 85.\n\n\nPackage natbib Warning: Citation `kunievsky2025' on page 2 undefined on input l\nine 87.\n\n[2]\n\nLaTeX Warning: Reference `sec:confound' on page 3 undefined on input line 119.\n\n\nLaTeX Warning: Reference `tab:precision_accuracy' on page 3 undefined on input \nline 146.\n\n\nLaTeX Warning: Reference `tab:exp1_decomp' on page 3 undefined on input line 14\n9.\n\n\nLaTeX Warning: Reference `tab:ranking' on page 3 undefined on input line 203.\n\n[3]\n\nLaTeX Warning: Reference `tab:replication' on page 4 undefined on input line 20\n8.\n\n\nLaTeX Warning: Reference `tab:math' on page 4 undefined on input line 253.\n\n\nOverfull \\hbox (1.55016pt too wide) in paragraph at lines 253--258\n[]\\OT1/cmr/m/n/10 Table [] con-firms a sys-tem-atic trend: as bench-marks shift\n from knowl-edge re-trieval (MMLU) to reasoning-\n\nLaTeX Warning: Reference `tab:dstudy' on page 4 undefined on input line 287.\n\n[4]\n\nLaTeX Warning: Reference `tab:allocation' on page 5 undefined on input line 292\n.\n\n\nLaTeX Warning: Reference `tab:14b' on page 5 undefined on input line 338.\n\n\nLaTeX Warning: Reference `tab:finetune' on page 5 undefined on input line 363.\n\n\nLaTeX Warning: Reference `tab:inf_vs_ft' on page 5 undefined on input line 371.\n\n\n[5]\n\nLaTeX Warning: Reference `tab:layercast' on page 6 undefined on input line 419.\n\n\n[6] [7] [8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm\ni7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmt\ni10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>\nOutput written on paper.pdf (9 pages, 277220 bytes).\nTranscript written on paper.log.\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmtt10.pfb>\nOutput written on paper.pdf (9 pages, 280287 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "565e4920-8ee7-40a1-9635-6573686617e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T19:30:34.346Z_

```json
{
  "parentUuid": "c34afa7e-9b61-47c0-9ceb-c78cfb5a0cf5",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ba9962f7-fdf0-4f86-b56f-785c80e7057c",
  "timestamp": "2026-05-20T19:30:34.346Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-20T19:30:44.745Z_

PDF compiled successfully (9 pages, no errors). All 11 tables from the experiment data are included, covering all 8 experiments. The paper is at:

`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/paper.pdf`

Reframed narrative: instead of the original "item dominance at 58%" claim (which collapsed after the float32 confound fix), the paper argues that variance attribution patterns are themselves unstable—benchmark-conditional and model-conditional—making universal reproducibility recipes impossible. Three contributions: (1) G-theory as diagnostic tool, (2) empirical proof that no universal variance structure exists across benchmarks/models, (3) float32 engine confound discovery as methodological warning. Fine-tuning G-study (exp-006) provides an independent contribution line showing learning rate dominance (17.8%) and inference-training decorrelation ($r=0.15$).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba9962f7-fdf0-4f86-b56f-785c80e7057c",
  "isSidechain": false,
  "requestId": "req_011CbENki5yKgVwQ6Tqo4ED3",
  "type": "assistant",
  "uuid": "2dfa7b02-11b3-439d-9d41-e22828d6a6d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M99X6kXeqMYJhBZrByuDFS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4618,
      "cache_read_input_tokens": 50424,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 50424,
          "cache_creation_input_tokens": 4618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4618
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190053 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheor…",
  "leafUuid": "2dfa7b02-11b3-439d-9d41-e22828d6a6d6",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream research",
  "sessionId": "8e06f34f-0bcd-4993-862f-8b43ca07c11c"
}
```

---
