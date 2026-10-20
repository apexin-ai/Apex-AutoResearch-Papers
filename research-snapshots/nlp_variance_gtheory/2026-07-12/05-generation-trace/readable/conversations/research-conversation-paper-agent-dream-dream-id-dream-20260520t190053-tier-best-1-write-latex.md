# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190053 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/bbd31e6f-001a-4789-9145-d920d26ff65b.jsonl`
- **Structured JSON:** [`4a991d3bab8a07a75f4d.json`](../../sessions/4a/4a991d3bab8a07a75f4d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:16:44.254Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:16:44.254Z",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190053 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始framing完全成立。float32 confound修复后precision主效应坍缩至噪声水平，反而成为方法论贡献（展示engine配置对variance attribution的系统性影响）。 Item dominance在所有benchmark上复现为最大单一方差源，4个模型一致。Separability在aggregate level成立（direct interaction <0.5%）， 但item-conditional interactions提供nuanced story。D-study budget表给出clear actionable guidance，headline数字\"item selection >50%\"直接可用。 AAAI投稿节奏正常，三条claim原封不动。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T19:16:44.257Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:16:44.257Z",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b"
}
```

---

## Round 1

49 recorded events

### User

_source line 3 · 2026-05-20T19:16:44.282Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190053 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始framing完全成立。float32 confound修复后precision主效应坍缩至噪声水平，反而成为方法论贡献（展示engine配置对variance attribution的系统性影响）。 Item dominance在所有benchmark上复现为最大单一方差源，4个模型一致。Separability在aggregate level成立（direct interaction <0.5%）， 但item-conditional interactions提供nuanced story。D-study budget表给出clear actionable guidance，headline数字"item selection >50%"直接可用。 AAAI投稿节奏正常，三条claim原封不动。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ed6c6a04-3d46-4e11-bc8c-428049c69e9a",
  "type": "user",
  "uuid": "e03ac440-52ae-496a-84c3-7562b1984ac1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:16:44.281Z_

```json
{
  "parentUuid": "e03ac440-52ae-496a-84c3-7562b1984ac1",
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
  "uuid": "5431d85d-d868-4f1e-85bd-4c1bc8959ac5",
  "timestamp": "2026-05-20T19:16:44.281Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:16:44.281Z_

```json
{
  "parentUuid": "5431d85d-d868-4f1e-85bd-4c1bc8959ac5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "da53a940-28ac-4b04-a7cd-c63a614fcc41",
  "timestamp": "2026-05-20T19:16:44.281Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
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
  "aiTitle": "Generate NLP variance generalizability theory paper",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b"
}
```

---

### Assistant

_source line 7 · 2026-05-20T19:16:46.914Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da53a940-28ac-4b04-a7cd-c63a614fcc41",
  "isSidechain": false,
  "requestId": "req_011CbEMhXFenN3b2oNUtzsGM",
  "type": "assistant",
  "uuid": "fb775574-b5a3-4eee-b49b-f1238a0bf71f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2Cjx9PRNyhn65n841nbWe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11493,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11493,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11493
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

_source line 8 · 2026-05-20T19:16:47.961Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XPeCcAqQ8arKJfaJNXf4br`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb775574-b5a3-4eee-b49b-f1238a0bf71f",
  "isSidechain": false,
  "requestId": "req_011CbEMhXFenN3b2oNUtzsGM",
  "type": "assistant",
  "uuid": "aa1f1c3b-9afb-46b1-9abd-e76e3e1de214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2Cjx9PRNyhn65n841nbWe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11493,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11493,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11493
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

_source line 9 · 2026-05-20T19:16:48.073Z_

<details open><summary>🔧 Tool call — Read · `toolu_011hZuhcbTFif35Kap8tpeyZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa1f1c3b-9afb-46b1-9abd-e76e3e1de214",
  "isSidechain": false,
  "requestId": "req_011CbEMhXFenN3b2oNUtzsGM",
  "type": "assistant",
  "uuid": "6338de0f-fda1-4676-b756-dde9dc4eab5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2Cjx9PRNyhn65n841nbWe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11493,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11493,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11493
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

_source line 10 · 2026-05-20T19:16:48.078Z_

<details><summary>↩ Tool result · `toolu_011hZuhcbTFif35Kap8tpeyZ`</summary>

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
  "parentUuid": "6338de0f-fda1-4676-b756-dde9dc4eab5d",
  "isSidechain": false,
  "promptId": "ed6c6a04-3d46-4e11-bc8c-428049c69e9a",
  "type": "user",
  "uuid": "64e845cf-0984-4846-ac32-5ef9f39046a7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper_framing.md",
      "content": "# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: Testing the Separability Assumption Between Infrastructure and Methodological Variance Sources via Generalizability Theory\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Item Dominance**: Item selection is the single largest uncontrolled variance source in LLM evaluation, contributing more than prompt phrasing, random seed, temperature, numerical precision, and hardware type combined. (MVP evidence: item_id = 58.4% of total variance vs all other factors combined < 25%)\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (hardware type, numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level (direct interaction < 0.5% of total variance), but both interact substantially with item difficulty — their effects are item-conditional, not universal. This provides an empirical license for isolated-factor studies while warning that their conclusions are conditional on item selection.\n\n**Claim 3 — Reproducibility Budget**: G-theory D-study projections yield quantitative reproducibility budgets showing that increasing item sampling is orders of magnitude more cost-effective than increasing prompt/seed replication for achieving reliable model comparisons (G ≥ 0.90). Current common practices (1 prompt, 1 seed, ≤200 items) produce G < 0.40.\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability between infrastructure and methodology layers.\n\n**Existing approaches & gaps**: Mesting (2026) applied G-theory to 5 methodological facets but treated infrastructure as fixed background. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision but without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance but on fixed hardware. No study crosses both layers in a unified G-theory framework, and critically, no study has quantified the role of item selection relative to all other sources.\n\n**Our framing**: We conduct the first fully-crossed G-theory study spanning infrastructure (hardware type, numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors. The separability test has two equally publishable outcomes: if interactions are negligible, we grant an empirical license to isolated-factor studies; if substantial, we demonstrate that existing conclusions need hardware/prompt qualification. Our MVP reveals a third, unexpected finding: item selection dominates everything (58.4%), making it the overlooked key to evaluation reproducibility.\n\n**Headline result template**: \"In a fully-crossed G-study of K conditions across M models and N benchmarks, item selection accounts for >50% of total evaluation variance, while direct infrastructure × methodology interactions contribute <0.5%. Current evaluation practices achieve G < 0.40; our D-study reproducibility budgets show that tripling item count is 10× more effective than tripling prompt count for reaching G ≥ 0.90.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs — item selection alone accounts for 58% of total evaluation variance, more than all other factors combined.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Breaking limitations (separability assumption challenge)\n- **Tension**: \"Everyone's optimizing the wrong thing\" — the field focuses on prompt/seed/hardware standardization while ignoring item selection\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart (field idiom from Mesting/Brittlebench)\n- **Figure flow**: Problem illustration → G-theory facet diagram → Stacked-bar variance decomposition → D-study projection curves\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer contribution. The novelty is the facet structure crossing infrastructure × methodology, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious — harder items have more variance\" — Counter: (a) the magnitude (58%) was not previously quantified; (b) item×factor interactions (7% precision×item) are non-obvious; (c) the D-study implications for evaluation design are novel.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this\n2. **\"float32 engine confound\"** → exp-001 fixes with consistent vLLM engine settings (V0 enforce_eager for all)\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa)\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support. Documented as hardware compatibility requirement.\n",
      "numLines": 59,
      "startLine": 1,
      "totalLines": 59
    }
  },
  "sourceToolAssistantUUID": "6338de0f-fda1-4676-b756-dde9dc4eab5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T19:16:48.355Z_

<details><summary>↩ Tool result · `toolu_01XPeCcAqQ8arKJfaJNXf4br`</summary>

```text
1	[
2	  {
3	    "name": "Full-scale precision study with confound fix",
4	    "description": "4 models × 3 precisions (FP32/BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items, 全部使用vLLM V0 enforce_eager消除engine差异。总条件数 4×3×6×6×3×4=5184 per item, 总记录 5184×200=1,036,800。\n",
5	    "results": {
6	      "total_records": 1036800,
7	      "conditions_per_model": 1296,
8	      "overall_accuracy": 0.668,
9	      "accuracy_fp32": 0.666,
10	      "accuracy_bf16": 0.671,
11	      "accuracy_fp16": 0.669,
12	      "accuracy_spread_across_precisions": 0.005,
13	      "item_id": 0.584,
14	      "residual": 0.168,
15	      "prompt_template_x_item_id": 0.061,
16	      "temperature_x_item_id": 0.058,
17	      "seed_x_item_id": 0.029,
18	      "precision_x_item_id": 0.018,
19	      "ordering_x_item_id": 0.014,
20	      "prompt_template": 0.009,
21	      "temperature": 0.007,
22	      "ordering": 0.003,
23	      "precision": 0.003,
24	      "seed": 0.001,
25	      "models_with_item_id_rank1": 4,
26	      "item_id_range_across_models": [
27	        0.52,
28	        0.62
29	      ],
30	      "qwen3_8b_item_id": 0.598,
31	      "llama31_8b_item_id": 0.571,
32	      "gemma2_9b_item_id": 0.62,
33	      "mistral_7b_item_id": 0.547,
34	      "precision_main_effect_before_fix_mvp": 0.0087,
35	      "precision_main_effect_after_fix": 0.003,
36	      "precision_x_item_id_before_fix_mvp": 0.0724,
37	      "precision_x_item_id_after_fix": 0.018,
38	      "fp32_bf16_accuracy_gap_before_fix": 0.085,
39	      "fp32_bf16_accuracy_gap_after_fix": 0.005,
40	      "g_current_practice_1p1s200i": 0.34,
41	      "g_6p6s200i": 0.72,
42	      "g_6p6s200i_3t4o": 0.78
43	    },
44	    "tables": [
45	      {
46	        "name": "Table 1: Variance Component Estimates — MMLU 200 items, 4 models pooled",
47	        "columns": [
48	          "Component",
49	          "% Variance",
50	          "SE",
51	          "95% CI Lower",
52	          "95% CI Upper",
53	          "MVP (50 items)"
54	        ],
55	        "rows": [
56	          [
57	            "item_id",
58	            58.4,
59	            2.1,
60	            54.3,
61	            62.5,
62	            58.4
63	          ],
64	          [
65	            "residual",
66	            16.8,
67	            0.9,
68	            15.0,
69	            18.6,
70	            17.6
71	          ],
72	          [
73	            "prompt×item",
74	            6.1,
75	            0.7,
76	            4.7,
77	            7.5,
78	            5.7
79	          ],
80	          [
81	            "temp×item",
82	            5.8,
83	            0.6,
84	            4.6,
85	            7.0,
86	            6.9
87	          ],
88	          [
89	            "seed×item",
90	            2.9,
91	            0.4,
92	            2.1,
93	            3.7,
94	            2.7
95	          ],
96	          [
97	            "precision×item",
98	            1.8,
99	            0.3,
100	            1.2,
101	            2.4,
102	            "7.2*"
103	          ],
104	          [
105	            "ordering×item",
106	            1.4,
107	            0.3,
108	            0.8,
109	            2.0,
110	            "—"
111	          ],
112	          [
113	            "prompt",
114	            0.9,
115	            0.3,
116	            0.3,
117	            1.5,
118	            "—"
119	          ],
120	          [
121	            "temperature",
122	            0.7,
123	            0.2,
124	            0.3,
125	            1.1,
126	            "—"
127	          ],
128	          [
129	            "precision",
130	            0.3,
131	            0.1,
132	            0.1,
133	            0.5,
134	            "0.87*"
135	          ],
136	          [
137	            "ordering",
138	            0.3,
139	            0.1,
140	            0.1,
141	            0.5,
142	            "—"
143	          ],
144	          [
145	            "seed",
146	            0.1,
147	            0.05,
148	            0.0,
149	            0.2,
150	            "—"
151	          ]
152	        ]
153	      },
154	      {
155	        "name": "Table 2: Per-Model item_id Variance Share",
156	        "columns": [
157	          "Model",
158	          "item_id %",
159	          "Next Largest",
160	          "Next %"
161	        ],
162	        "rows": [
163	          [
164	            "Qwen3-8B",
165	            59.8,
166	            "residual",
167	            16.2
168	          ],
169	          [
170	            "Llama-3.1-8B",
171	            57.1,
172	            "residual",
173	            17.8
174	          ],
175	          [
176	            "Gemma-2-9B-IT",
177	            62.0,
178	            "residual",
179	            14.9
180	          ],
181	          [
182	            "Mistral-7B-v0.3",
183	            54.7,
184	            "residual",
185	            18.5
186	          ]
187	        ]
188	      }
189	    ],
190	    "figures": [],
191	    "analysis": "核心发现：engine confound修复后item dominance完全稳健，precision主效应从0.87%降至0.3%。 这同时验证了Claim 1（item dominance）和提供了方法论贡献（engine配置对variance attribution的影响）。 4个模型一致性消除了\"Qwen3特例\"的concern。200 items分层采样提供了足够的statistical power。 Ordering facet新增后占比很小（~1.7% total含interaction），说明item presentation order不是主要concern。\n\n\nMVP中precision主效应0.87%和precision×item交互7.24%主要来自float32使用不同vLLM engine路径（非V0时触发不同kernel）， 导致FP32准确率系统性偏低5.7pp。统一V0 enforce_eager后，三种精度走同一compute path， FP32/BF16/FP16准确率差收敛至0.5pp以内（纯numerical noise水平）。precision主效应从0.87%降至~0.3%， precision×item从7.24%降至~1.8%。这些被释放的方差份额主要回流到residual和item_id， 使item_id维持在~58%（与MVP一致，因为item difficulty本身是真实信号，不受engine confound影响）。 4个模型均以item_id为rank-1组分，因为MMLU的item difficulty分布（从trivial到expert-level） 在所有7-9B模型上产生类似的accuracy ceiling/floor效应。Gemma-2略高因其instruction-tuned特性 使其对easy items更稳定（floor更高），Mistral略低因其在部分domain上accuracy更平坦。 200 items（分层采样）比MVP的50 items提供更稳定的方差估计，置信区间收窄约50%。\n"
192	  },
193	  {
194	    "name": "Multi-benchmark replication",
195	    "description": "4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 items, 分别在GSM8K、ARC-Challenge、HellaSwag上运行。每benchmark总记录 4×2×6×6×2×4×200=230,400。\n",
196	    "results": {
197	      "gsm8k_overall_accuracy": 0.583,
198	      "gsm8k_item_id": 0.487,
199	      "gsm8k_residual": 0.214,
200	      "gsm8k_temperature_x_item_id": 0.089,
201	      "gsm8k_prompt_x_item_id": 0.072,
202	      "gsm8k_seed_x_item_id": 0.041,
203	      "gsm8k_precision_x_item_id": 0.012,
204	      "gsm8k_ordering_x_item_id": 0.018,
205	      "gsm8k_temperature": 0.024,
206	      "gsm8k_prompt": 0.015,
207	      "gsm8k_precision": 0.002,
208	      "gsm8k_g_current_practice": 0.29,
209	      "arc_overall_accuracy": 0.597,
210	      "arc_item_id": 0.551,
211	      "arc_residual": 0.182,
212	      "arc_prompt_x_item_id": 0.068,
213	      "arc_temperature_x_item_id": 0.054,
214	      "arc_seed_x_item_id": 0.031,
215	      "arc_precision_x_item_id": 0.014,
216	      "arc_ordering_x_item_id": 0.016,
217	      "arc_prompt": 0.011,
218	      "arc_temperature": 0.008,
219	      "arc_precision": 0.002,
220	      "arc_g_current_practice": 0.32,
221	      "hellaswag_overall_accuracy": 0.712,
222	      "hellaswag_item_id": 0.527,
223	      "hellaswag_residual": 0.195,
224	      "hellaswag_prompt_x_item_id": 0.058,
225	      "hellaswag_temperature_x_item_id": 0.062,
226	      "hellaswag_seed_x_item_id": 0.033,
227	      "hellaswag_precision_x_item_id": 0.011,
228	      "hellaswag_ordering_x_item_id": 0.019,
229	      "hellaswag_prompt": 0.008,
230	      "hellaswag_temperature": 0.006,
231	      "hellaswag_precision": 0.001,
232	      "hellaswag_g_current_practice": 0.36,
233	      "benchmarks_with_item_id_rank1": 4,
234	      "item_id_range_across_benchmarks": [
235	        0.487,
236	        0.584
237	      ],
238	      "cross_benchmark_replication_rate": 1.0,
239	      "models_showing_consistent_pattern": 4
240	    },
241	    "tables": [
242	      {
243	        "name": "Table 3: Cross-Benchmark Variance Decomposition Summary",
244	        "columns": [
245	          "Benchmark",
246	          "item_id %",
247	          "Residual %",
248	          "Item-Conditional Total %",
249	          "Precision Main %",
250	          "G (current)"
251	        ],
252	        "rows": [
253	          [
254	            "MMLU",
255	            58.4,
256	            16.8,
257	            16.1,
258	            0.3,
259	            0.34
260	          ],
261	          [
262	            "GSM8K",
263	            48.7,
264	            21.4,
265	            23.2,
266	            0.2,
267	            0.29
268	          ],
269	          [
270	            "ARC-Challenge",
271	            55.1,
272	            18.2,
273	            18.3,
274	            0.2,
275	            0.32
276	          ],
277	          [
278	            "HellaSwag",
279	            52.7,
280	            19.5,
281	            18.3,
282	            0.1,
283	            0.36
284	          ]
285	        ]
286	      },
287	      {
288	        "name": "Table 4: GSM8K Per-Model Breakdown",
289	        "columns": [
290	          "Model",
291	          "item_id %",
292	          "temp×item %",
293	          "prompt×item %",
294	          "residual %"
295	        ],
296	        "rows": [
297	          [
298	            "Qwen3-8B",
299	            51.2,
300	            8.1,
301	            6.8,
302	            19.8
303	          ],
304	          [
305	            "Llama-3.1-8B",
306	            47.3,
307	            9.4,
308	            7.6,
309	            22.1
310	          ],
311	          [
312	            "Gemma-2-9B-IT",
313	            50.8,
314	            8.5,
315	            6.9,
316	            20.3
317	          ],
318	          [
319	            "Mistral-7B-v0.3",
320	            43.4,
321	            10.5,
322	            8.3,
323	            23.5
324	          ]
325	        ]
326	      }
327	    ],
328	    "figures": [],
329	    "analysis": "Item dominance在4个benchmark上全部复现（range 48.7%-58.4%），但幅度因task type有系统性差异： generation-heavy tasks（GSM8K）因CoT随机性使residual膨胀，压缩item_id相对占比； classification-like tasks（MMLU, ARC）的item_id更高。这个gradient本身是有趣的发现， 可在Discussion中展开。关键是即使在\"worst case\"的GSM8K上，item_id仍是rank-1（48.7% > residual 21.4%）， headline claim成立。\n\n\nGSM8K的item_id占比略低于MMLU（48.7% vs 58.4%），因为数学推理任务引入更多chain-of-thought随机性， 使residual和temperature×item交互膨胀。GSM8K中温度效应更大（temperature×item 8.9%）， 因为CoT生成路径对sampling temperature更敏感——同一道数学题在不同温度下可能走完全不同的推理链。 但item_id仍然是rank-1组分，因为GSM8K的difficulty gradient极陡（从单步算术到多步word problem）， 这种item-level variance在所有条件下都主导。ARC-Challenge的item_id（55.1%）接近MMLU， 因为科学推理题的difficulty分布类似（从factual recall到multi-hop inference）。 HellaSwag的item_id（52.7%）也稳健，因为commonsense completion的item variance主要来自 distractor quality差异——有些items的wrong answers显而易见，有些几乎无法区分。 所有benchmark上precision主效应均<0.3%，确认engine confound fix的泛化性。 4/4 benchmark的item_id rank-1复现率为100%，支撑\"cross-benchmark replication rate = 1.0\"。\n"
330	  },
331	  {
332	    "name": "Multi-hardware G-study",
333	    "description": "4 models × 2 GPU types (RTX PRO 6000 + second GPU) × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。总记录 4×2×2×6×6×3×4×200=691,200。 核心目标：量化hardware主效应和hardware×methodology交互。\n",
334	    "results": {
335	      "total_records": 691200,
336	      "hardware_main_effect": 0.006,
337	      "hardware_x_precision": 0.002,
338	      "hardware_x_prompt": 0.001,
339	      "hardware_x_temperature": 0.001,
340	      "hardware_x_seed": 0.0005,
341	      "hardware_x_ordering": 0.0003,
342	      "hardware_x_item_id": 0.019,
343	      "precision_x_prompt": 0.0008,
344	      "precision_x_temperature": 0.0006,
345	      "precision_x_seed": 0.0003,
346	      "precision_x_ordering": 0.0002,
347	      "direct_infra_method_interaction_total": 0.005,
348	      "item_conditional_interactions_total": 0.142,
349	      "item_id": 0.561,
350	      "residual": 0.152,
351	      "prompt_x_item": 0.059,
352	      "temperature_x_item": 0.055,
353	      "seed_x_item": 0.028,
354	      "precision_x_item": 0.017,
355	      "ordering_x_item": 0.013,
356	      "hardware_x_item": 0.019,
357	      "separability_ratio": 0.035,
358	      "gpu1_gpu2_accuracy_correlation": 0.9987,
359	      "max_accuracy_difference_any_condition": 0.018,
360	      "mean_accuracy_difference": 0.004,
361	      "g_current_practice": 0.33,
362	      "g_full_design": 0.81
363	    },
364	    "tables": [
365	      {
366	        "name": "Table 5: Separability Test — Direct vs Item-Conditional Interactions",
367	        "columns": [
368	          "Interaction Type",
369	          "Components",
370	          "Total % Variance",
371	          "Interpretation"
372	        ],
373	        "rows": [
374	          [
375	            "Direct Infra×Method",
376	            "hw×prompt, hw×temp, hw×seed, hw×ord, prec×prompt, prec×temp, prec×seed, prec×ord",
377	            0.5,
378	            "Negligible — separability holds at aggregate"
379	          ],
380	          [
381	            "Infra×Item",
382	            "hw×item, prec×item",
383	            3.6,
384	            "Small but non-zero — hardware/precision effects are item-conditional"
385	          ],
386	          [
387	            "Method×Item",
388	            "prompt×item, temp×item, seed×item, ord×item",
389	            15.5,
390	            "Substantial — methodology effects are strongly item-conditional"
391	          ],
392	          [
393	            "Item Main",
394	            "item_id",
395	            56.1,
396	            "Dominant — item selection is the primary variance source"
397	          ]
398	        ]
399	      },
400	      {
401	        "name": "Table 6: Hardware Agreement Matrix (per-model mean accuracy)",
402	        "columns": [
403	          "Model",
404	          "GPU1",
405	          "GPU2",
406	          "Difference"
407	        ],
408	        "rows": [
409	          [
410	            "Qwen3-8B",
411	            0.671,
412	            0.668,
413	            0.003
414	          ],
415	          [
416	            "Llama-3.1-8B",
417	            0.654,
418	            0.65,
419	            0.004
420	          ],
421	          [
422	            "Gemma-2-9B-IT",
423	            0.689,
424	            0.684,
425	            0.005
426	          ],
427	          [
428	            "Mistral-7B-v0.3",
429	            0.638,
430	            0.634,
431	            0.004
432	          ]
433	        ]
434	      }
435	    ],
436	    "figures": [],
437	    "analysis": "Separability成立：direct infra×method交互总和0.5%，远低于1%阈值。但不是trivial null result—— item-conditional interactions（14.2%）提供了nuanced interpretation：infrastructure和methodology 不是完全独立的，而是通过item difficulty间接耦合。这比simple \"separable/not separable\"更有价值， 因为它解释了为什么isolated-factor studies的结论在某些items上不泛化。 这同时支撑了Claim 2的两半：\"empirical license for isolated-factor studies\"（direct <0.5%） 和 \"conclusions are conditional on item selection\"（item-conditional 14.2%）。\n\n\nHardware主效应0.6%反映两块GPU的微架构差异（不同SM count、memory bandwidth、kernel scheduling）， 但这些差异是系统性的（固定偏移），不是随机的，所以主效应很小。hardware×item交互1.9%比hardware主效应大， 因为特定items（如需要长sequence generation的items）在不同GPU上因kernel tiling差异产生不同的numerical path， 但这只影响边界case items。所有direct infra×method交互加总仅0.5%，因为infrastructure层（hardware type, precision） 和methodology层（prompt, seed, temperature, ordering）作用于不同的computation stages： precision/hardware影响numerical computation，prompt/seed/temperature影响token sampling， 两者的交叉点（sampling受precision影响的程度）在logit空间中被softmax压缩到negligible水平。 Item-conditional interactions总和14.2%远大于direct interactions 0.5%，验证了Claim 2的nuanced story： separability在aggregate成立，但两层都通过item difficulty调节其效应。 GPU间accuracy correlation 0.9987说明hardware几乎不改变model ranking，只在individual item level引入微小噪声。\n"
438	  },
439	  {
440	    "name": "D-study reproducibility budget projections",
441	    "description": "基于exp-001/002/003的合并variance component estimates，计算不同facet allocation下的G系数。 生成practitioner-facing budget tables和projection curves。纯计算，无GPU开销。\n",
442	    "results": {
443	      "g_1prompt_1seed_200items_mmlu": 0.34,
444	      "g_1prompt_1seed_200items_gsm8k": 0.29,
445	      "g_1prompt_1seed_200items_arc": 0.32,
446	      "g_1prompt_1seed_200items_hellaswag": 0.36,
447	      "g_1prompt_1seed_600items_mmlu": 0.71,
448	      "g_1prompt_1seed_1000items_mmlu": 0.82,
449	      "g_1prompt_1seed_2000items_mmlu": 0.9,
450	      "g_3prompt_1seed_200items_mmlu": 0.42,
451	      "g_6prompt_1seed_200items_mmlu": 0.49,
452	      "g_12prompt_1seed_200items_mmlu": 0.54,
453	      "g_1prompt_3seed_200items_mmlu": 0.36,
454	      "g_1prompt_6seed_200items_mmlu": 0.37,
455	      "optimal_g90_items": 600,
456	      "optimal_g90_prompts": 3,
457	      "optimal_g90_seeds": 2,
458	      "optimal_g90_total_conditions": 6,
459	      "optimal_g90_total_evaluations": 3600,
460	      "optimal_g95_items": 1200,
461	      "optimal_g95_prompts": 4,
462	      "optimal_g95_seeds": 3,
463	      "optimal_g95_total_conditions": 12,
464	      "optimal_g95_total_evaluations": 14400,
465	      "marginal_g_per_100_items": 0.038,
466	      "marginal_g_per_prompt": 0.025,
467	      "marginal_g_per_seed": 0.005,
468	      "items_vs_prompts_effectiveness_ratio": 10.2,
469	      "items_vs_seeds_effectiveness_ratio": 51.0,
470	      "gsm8k_optimal_g90_items": 800,
471	      "gsm8k_optimal_g90_prompts": 3,
472	      "gsm8k_optimal_g90_seeds": 2,
473	      "arc_optimal_g90_items": 650,
474	      "hellaswag_optimal_g90_items": 550
475	    },
476	    "tables": [
477	      {
478	        "name": "Table 7: Reproducibility Budget — MMLU (Items × Prompts × Seeds → G coefficient)",
479	        "columns": [
480	          "Items",
481	          "Prompts",
482	          "Seeds",
483	          "Total Evals",
484	          "G coeff",
485	          "Δ vs Current"
486	        ],
487	        "rows": [
488	          [
489	            200,
490	            1,
491	            1,
492	            200,
493	            0.34,
494	            "baseline"
495	          ],
496	          [
497	            200,
498	            3,
499	            1,
500	            600,
501	            0.42,
502	            "+0.08"
503	          ],
504	          [
505	            200,
506	            6,
507	            1,
508	            1200,
509	            0.49,
510	            "+0.15"
511	          ],
512	          [
513	            200,
514	            6,
515	            6,
516	            7200,
517	            0.54,
518	            "+0.20"
519	          ],
520	          [
521	            600,
522	            1,
523	            1,
524	            600,
525	            0.71,
526	            "+0.37"
527	          ],
528	          [
529	            600,
530	            3,
531	            1,
532	            1800,
533	            0.82,
534	            "+0.48"
535	          ],
536	          [
537	            600,
538	            3,
539	            2,
540	            3600,
541	            0.9,
542	            "+0.56"
543	          ],
544	          [
545	            1000,
546	            3,
547	            2,
548	            6000,
549	            0.93,
550	            "+0.59"
551	          ],
552	          [
553	            1200,
554	            4,
555	            3,
556	            14400,
557	            0.95,
558	            "+0.61"
559	          ],
560	          [
561	            2000,
562	            4,
563	            3,
564	            24000,
565	            0.97,
566	            "+0.63"
567	          ]
568	        ]
569	      },
570	      {
571	        "name": "Table 8: Cross-Benchmark Minimum Budget for G≥0.90",
572	        "columns": [
573	          "Benchmark",
574	          "Items",
575	          "Prompts",
576	          "Seeds",
577	          "Total Evals",
578	          "Cost Factor vs Current"
579	        ],
580	        "rows": [
581	          [
582	            "MMLU",
583	            600,
584	            3,
585	            2,
586	            3600,
587	            "18×"
588	          ],
589	          [
590	            "GSM8K",
591	            800,
592	            3,
593	            2,
594	            4800,
595	            "24×"
596	          ],
597	          [
598	            "ARC-Challenge",
599	            650,
600	            3,
601	            2,
602	            3900,
603	            "19.5×"
604	          ],
605	          [
606	            "HellaSwag",
607	            550,
608	            3,
609	            2,
610	            3300,
611	            "16.5×"
612	          ]
613	        ]
614	      }
615	    ],
616	    "figures": [],
617	    "analysis": "Claim 3的核心表格。Headline数字：\"tripling items is 10× more effective than tripling prompts\" 直接来自marginal effectiveness ratio 10.2:1。当前practice G<0.40的发现具有强policy implication—— 意味着现有leaderboard结果的measurement reliability低于社会科学中最低标准。 600 items + 3 prompts + 2 seeds的\"recommended minimum\"在计算成本上仅为full factorial的一小部分， 是actionable的建议。跨benchmark budget差异（550-800 items for G≥0.90）提供task-specific guidance。\n\n\nG系数由universe score variance与observed score variance的比值决定。因为item_id占总方差>50%， 增加item采样直接压缩最大的variance component，G提升最快。具体地，G ≈ σ²(τ) / [σ²(τ) + σ²(δ)/n_facets]， 当item_id是σ²(δ)的主要贡献者时，增加n_items的marginal return远超增加n_prompts或n_seeds。 数值上，从200到600 items（3×）使G从0.34升至0.71，而从1到3 prompts（3×）仅从0.34升至0.42。 这是因为prompt variance（含prompt×item）共计~7%，而item variance 58%。 Seed几乎无效（G从0.34到0.37 at 6 seeds），因为seed的总方差贡献<3%（主要通过seed×item）。 G≥0.90需要~600 items + 3 prompts + 2 seeds = 3,600 evaluations。 当前标准practice（1 prompt, 1 seed, 200 items）的G < 0.40意味着evaluation结果的reliability 低于社会科学中\"不可接受\"的阈值（通常G≥0.80）。 GSM8K需要更多items（800 vs 600）达到G≥0.90，因为其residual更大（CoT随机性）， 需要更多items来平均掉item-level noise。\n"
618	  },
619	  {
620	    "name": "14B model extension",
621	    "description": "Qwen3-14B和DeepSeek-R1-Distill-14B × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。每模型 2×6×6×3×4×200=172,800记录。\n",
622	    "results": {
623	      "qwen3_14b_accuracy": 0.728,
624	      "deepseek_r1_14b_accuracy": 0.714,
625	      "qwen3_14b_item_id": 0.574,
626	      "deepseek_r1_14b_item_id": 0.538,
627	      "qwen3_14b_residual": 0.162,
628	      "deepseek_r1_14b_residual": 0.198,
629	      "deepseek_r1_14b_temperature_x_item": 0.082,
630	      "scale_effect_on_item_id": "within 8B model range",
631	      "item_id_rank1_both_models": true,
632	      "variance_pattern_consistent_with_8b": true,
633	      "precision_main_effect_14b": 0.002
634	    },
635	    "tables": [
636	      {
637	        "name": "Table 9: 14B vs 8B Variance Pattern Comparison",
638	        "columns": [
639	          "Component",
640	          "8B Mean",
641	          "8B Range",
642	          "Qwen3-14B",
643	          "DS-R1-14B"
644	        ],
645	        "rows": [
646	          [
647	            "item_id",
648	            58.4,
649	            "54.7–62.0",
650	            57.4,
651	            53.8
652	          ],
653	          [
654	            "residual",
655	            16.8,
656	            "14.9–18.5",
657	            16.2,
658	            19.8
659	          ],
660	          [
661	            "temp×item",
662	            5.8,
663	            "4.6–7.0",
664	            5.3,
665	            8.2
666	          ],
667	          [
668	            "prompt×item",
669	            6.1,
670	            "4.7–7.5",
671	            5.8,
672	            5.4
673	          ],
674	          [
675	            "precision",
676	            0.3,
677	            "0.1–0.5",
678	            0.2,
679	            0.2
680	          ]
681	        ]
682	      }
683	    ],
684	    "figures": [],
685	    "analysis": "Scale invariance确认：item dominance不是小模型artifacts。DeepSeek-R1-Distill的slightly不同的profile （更高residual, 更高temp×item）提供了architecture effect的初步evidence， 但不改变core claim。这是P1实验，为paper增加robustness但非必需。\n\n\n14B模型的overall accuracy更高，但item difficulty的variance structure不会因scale改变—— easy items仍然easy，hard items仍然hard。Item_id占比略低于8B平均值（~55-57% vs ~58%）， 因为14B模型在medium-difficulty items上表现更一致（ceiling effect压缩了item variance的上端）， 但差异不大。DeepSeek-R1-Distill的reasoning-distilled特性使其在CoT-heavy items上产生更多 temperature×item交互（类似GSM8K的pattern），residual也略高，因为distillation引入的implicit CoT 增加了generation-level stochasticity。关键是item_id在两个14B模型上仍为rank-1， 确认pattern不随model scale改变。precision主效应在14B上同样negligible（0.2%）， 因为confound fix的原理（统一engine path）与model size无关。\n"
686	  },
687	  {
688	    "name": "Fine-tuning G-study",
689	    "description": "RoBERTa-large在SST-2/MNLI/RTE/COPA上fine-tuning。6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728 total。\n",
690	    "results": {
691	      "sst2_accuracy_mean": 0.948,
692	      "sst2_item_id": 0.412,
693	      "sst2_seed": 0.087,
694	      "sst2_learning_rate": 0.063,
695	      "sst2_data_shuffle": 0.042,
696	      "sst2_seed_x_item": 0.098,
697	      "sst2_lr_x_item": 0.074,
698	      "sst2_residual": 0.131,
699	      "sst2_gpu": 0.003,
700	      "sst2_precision": 0.002,
701	      "mnli_accuracy_mean": 0.876,
702	      "mnli_item_id": 0.445,
703	      "mnli_seed": 0.072,
704	      "mnli_learning_rate": 0.081,
705	      "mnli_data_shuffle": 0.038,
706	      "mnli_seed_x_item": 0.091,
707	      "mnli_residual": 0.142,
708	      "rte_accuracy_mean": 0.743,
709	      "rte_item_id": 0.368,
710	      "rte_seed": 0.124,
711	      "rte_learning_rate": 0.098,
712	      "rte_data_shuffle": 0.067,
713	      "rte_seed_x_item": 0.112,
714	      "rte_residual": 0.158,
715	      "copa_accuracy_mean": 0.682,
716	      "copa_item_id": 0.382,
717	      "copa_seed": 0.118,
718	      "copa_learning_rate": 0.091,
719	      "copa_residual": 0.167,
720	      "item_id_rank1_all_tasks": true,
721	      "seed_more_important_than_inference": true,
722	      "infra_effects_negligible": true,
723	      "fine_tuning_g_current_practice": 0.28
724	    },
725	    "tables": [
726	      {
727	        "name": "Table 10: Fine-tuning vs Inference Variance Hierarchy",
728	        "columns": [
729	          "Rank",
730	          "Inference (MMLU)",
731	          "Fine-tuning (SST-2)"
732	        ],
733	        "rows": [
734	          [
735	            1,
736	            "item_id (58.4%)",
737	            "item_id (41.2%)"
738	          ],
739	          [
740	            2,
741	            "residual (16.8%)",
742	            "residual (13.1%)"
743	          ],
744	          [
745	            3,
746	            "prompt×item (6.1%)",
747	            "seed×item (9.8%)"
748	          ],
749	          [
750	            4,
751	            "temp×item (5.8%)",
752	            "seed (8.7%)"
753	          ],
754	          [
755	            5,
756	            "seed×item (2.9%)",
757	            "lr×item (7.4%)"
758	          ],
759	          [
760	            6,
761	            "precision×item (1.8%)",
762	            "lr (6.3%)"
763	          ]
764	        ]
765	      }
766	    ],
767	    "figures": [],
768	    "analysis": "Fine-tuning G-study将paper从\"inference evaluation reproducibility\"扩展到\"ML reproducibility broadly\"。 核心takeaway：item dominance是跨paradigm的（inference和fine-tuning），但second-tier factors不同。 这是P1实验，为paper增加generality但AAAI投稿时可作为supplementary。\n\n\nFine-tuning与inference的关键区别：training seed和learning rate成为substantial variance sources （combined 10-22%），因为它们影响optimization trajectory，不仅仅是sampling randomness。 但item_id仍然是rank-1（37-45%），因为NLU tasks的item difficulty gradient—— 从\"I love this movie\"(trivially positive)到需要subtle pragmatic inference的examples—— 在所有training configurations下都产生consistent accuracy variation。 RTE的item_id最低（36.8%），因为小数据集（2.5K training examples）使fine-tuning对seed更敏感， seed主效应膨胀到12.4%。这为paper提供了\"inference vs fine-tuning\"的对比dimension： 两者都是item-dominant，但fine-tuning中training hyperparameters（seed, LR）取代了 inference中的generation parameters（temperature, prompt）成为第二梯队的variance sources。 GPU和precision主效应在fine-tuning中同样negligible（<0.5%），因为RoBERTa-large 对numerical precision不敏感（unlike large generative models的autoregressive error accumulation）。\n"
769	  },
770	  {
771	    "name": "LayerCast precision study",
772	    "description": "在MMLU上测试LayerCast（FP16 storage + FP32 compute）作为额外precision condition。 4 models × 1 precision mode × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 items = 172,800记录。\n",
773	    "results": {
774	      "layercast_accuracy_mean": 0.67,
775	      "layercast_vs_fp32_accuracy_diff": 0.004,
776	      "layercast_vs_bf16_accuracy_diff": -0.001,
777	      "layercast_item_agreement_with_fp32": 0.9991,
778	      "layercast_item_agreement_with_bf16": 0.9994,
779	      "layercast_added_variance_to_precision": 0.0004,
780	      "layercast_throughput_vs_fp32": 1.38,
781	      "layercast_throughput_vs_bf16": 0.91,
782	      "layercast_precision_x_item_contribution": 0.009
783	    },
784	    "tables": [
785	      {
786	        "name": "Table 11: Precision Mode Comparison",
787	        "columns": [
788	          "Mode",
789	          "Accuracy",
790	          "item Agreement w/ FP32",
791	          "Throughput (tokens/s)",
792	          "VRAM (GB)"
793	        ],
794	        "rows": [
795	          [
796	            "FP32",
797	            0.666,
798	            1.0,
799	            1820,
800	            31.2
801	          ],
802	          [
803	            "BF16",
804	            0.671,
805	            0.9985,
806	            2760,
807	            15.8
808	          ],
809	          [
810	            "FP16",
811	            0.669,
812	            0.9982,
813	            2810,
814	            15.6
815	          ],
816	          [
817	            "LayerCast",
818	            0.67,
819	            0.9991,
820	            2510,
821	            16.1
822	          ]
823	        ]
824	      }
825	    ],
826	    "figures": [],
827	    "analysis": "P2实验。LayerCast结果进一步support precision不是major concern（在engine confound fix后）。 可作为paper中\"practical recommendation\"段落的一条：对于追求最高reproducibility的场景， LayerCast提供了memory-efficient的FP32-equivalent选项。\n\n\nLayerCast在存储时用FP16减少memory footprint，在compute时cast to FP32， 因此其numerical behavior几乎等同于纯FP32（computation path一致）， accuracy差异仅来自storage时的precision loss（FP16 mantissa 10 bits vs FP32 23 bits）， 这对大部分weights来说negligible（在训练时weights就是从FP16/BF16来的）。 与BF16的差异更小（0.1pp），因为BF16的dynamic range与FP32一致（8-bit exponent）， 而FP16的range更窄但mantissa更宽，两者accuracy接近。 LayerCast对precision variance几乎没有增量贡献（0.04%），因为它本质上是FP32 compute的cheaper variant。 Throughput方面，LayerCast比FP32快38%（memory bandwidth节省），比BF16慢9%（需要cast操作）。 这个实验为paper提供了一个\"practical mitigation\"故事：如果practitioner担心precision影响， LayerCast以minimal overhead提供FP32-level behavior。\n"
828	  },
829	  {
830	    "name": "MATH benchmark extension",
831	    "description": "4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 MATH items。 总记录 4×2×6×6×2×4×200=230,400。测试reasoning-heavy task的variance structure。\n",
832	    "results": {
833	      "math_overall_accuracy": 0.342,
834	      "math_item_id": 0.421,
835	      "math_residual": 0.248,
836	      "math_temperature_x_item": 0.104,
837	      "math_prompt_x_item": 0.068,
838	      "math_seed_x_item": 0.052,
839	      "math_temperature": 0.038,
840	      "math_prompt": 0.021,
841	      "math_precision": 0.002,
842	      "math_precision_x_item": 0.008,
843	      "math_ordering_x_item": 0.015,
844	      "math_g_current_practice": 0.24,
845	      "math_item_id_rank1": true,
846	      "math_optimal_g90_items": 1100,
847	      "math_optimal_g90_prompts": 4,
848	      "math_optimal_g90_seeds": 3
849	    },
850	    "tables": [
851	      {
852	        "name": "Table 12: Full Cross-Benchmark Variance Summary (5 benchmarks)",
853	        "columns": [
854	          "Benchmark",
855	          "Accuracy",
856	          "item_id %",
857	          "Residual %",
858	          "Temp×Item %",
859	          "G (current)",
860	          "Items for G≥0.90"
861	        ],
862	        "rows": [
863	          [
864	            "MMLU",
865	            0.668,
866	            58.4,
867	            16.8,
868	            5.8,
869	            0.34,
870	            600
871	          ],
872	          [
873	            "ARC-Challenge",
874	            0.597,
875	            55.1,
876	            18.2,
877	            5.4,
878	            0.32,
879	            650
880	          ],
881	          [
882	            "HellaSwag",
883	            0.712,
884	            52.7,
885	            19.5,
886	            6.2,
887	            0.36,
888	            550
889	          ],
890	          [
891	            "GSM8K",
892	            0.583,
893	            48.7,
894	            21.4,
895	            8.9,
896	            0.29,
897	            800
898	          ],
899	          [
900	            "MATH",
901	            0.342,
902	            42.1,
903	            24.8,
904	            10.4,
905	            0.24,
906	            1100
907	          ]
908	        ]
909	      }
910	    ],
911	    "figures": [],
912	    "analysis": "MATH提供了variance structure的\"stress test\"。Item_id在最extreme条件下仍为rank-1（42.1%）， 但task difficulty明显调节了variance decomposition的profile。5个benchmark展现了清晰的gradient： task difficulty ↑ → item_id share ↓, residual ↑, temperature×item ↑, G current practice ↓。 这个gradient本身是publishable finding：它量化了为什么reasoning benchmark的evaluation更不稳定， 并给出了task-specific的reproducibility budget。\n\nMATH是所有benchmark中最challenging的（accuracy ~34%），其item difficulty分布极端—— 从Level 1（algebra basics）到Level 5（competition math），跨越巨大的difficulty range。 Item_id仍为rank-1（42.1%）但低于MMLU，因为：(1) lower overall accuracy增加了random guessing的比例， 膨胀residual到24.8%；(2) MATH的CoT generation比GSM8K更长更复杂（多步proof-like reasoning）， 使temperature×item interaction达到10.4%——在高temperature下，长推理链的任何一步都可能diverge， 且这种sensitivity是item-specific的（Level 5 problems的长推理链比Level 1的短计算更sensitive）。 Temperature主效应也最高（3.8%），因为MATH的generation length使sampling temperature的cumulative effect更显著。 G current practice仅0.24——所有benchmark中最低——意味着MATH evaluation的reproducibility最差。 达到G≥0.90需要1100 items + 4 prompts + 3 seeds，是MMLU所需的~3倍evaluation budget。 这个发现有strong policy implication：reasoning benchmark的evaluation标准需要比classification benchmark更严格。\n"
913	  }
914	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa1f1c3b-9afb-46b1-9abd-e76e3e1de214",
  "isSidechain": false,
  "promptId": "ed6c6a04-3d46-4e11-bc8c-428049c69e9a",
  "type": "user",
  "uuid": "18a0111c-0da2-4318-9f8b-7bf8b9001a9f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full-scale precision study with confound fix\",\n    \"description\": \"4 models × 3 precisions (FP32/BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items, 全部使用vLLM V0 enforce_eager消除engine差异。总条件数 4×3×6×6×3×4=5184 per item, 总记录 5184×200=1,036,800。\\n\",\n    \"results\": {\n      \"total_records\": 1036800,\n      \"conditions_per_model\": 1296,\n      \"overall_accuracy\": 0.668,\n      \"accuracy_fp32\": 0.666,\n      \"accuracy_bf16\": 0.671,\n      \"accuracy_fp16\": 0.669,\n      \"accuracy_spread_across_precisions\": 0.005,\n      \"item_id\": 0.584,\n      \"residual\": 0.168,\n      \"prompt_template_x_item_id\": 0.061,\n      \"temperature_x_item_id\": 0.058,\n      \"seed_x_item_id\": 0.029,\n      \"precision_x_item_id\": 0.018,\n      \"ordering_x_item_id\": 0.014,\n      \"prompt_template\": 0.009,\n      \"temperature\": 0.007,\n      \"ordering\": 0.003,\n      \"precision\": 0.003,\n      \"seed\": 0.001,\n      \"models_with_item_id_rank1\": 4,\n      \"item_id_range_across_models\": [\n        0.52,\n        0.62\n      ],\n      \"qwen3_8b_item_id\": 0.598,\n      \"llama31_8b_item_id\": 0.571,\n      \"gemma2_9b_item_id\": 0.62,\n      \"mistral_7b_item_id\": 0.547,\n      \"precision_main_effect_before_fix_mvp\": 0.0087,\n      \"precision_main_effect_after_fix\": 0.003,\n      \"precision_x_item_id_before_fix_mvp\": 0.0724,\n      \"precision_x_item_id_after_fix\": 0.018,\n      \"fp32_bf16_accuracy_gap_before_fix\": 0.085,\n      \"fp32_bf16_accuracy_gap_after_fix\": 0.005,\n      \"g_current_practice_1p1s200i\": 0.34,\n      \"g_6p6s200i\": 0.72,\n      \"g_6p6s200i_3t4o\": 0.78\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Variance Component Estimates — MMLU 200 items, 4 models pooled\",\n        \"columns\": [\n          \"Component\",\n          \"% Variance\",\n          \"SE\",\n          \"95% CI Lower\",\n          \"95% CI Upper\",\n          \"MVP (50 items)\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            58.4,\n            2.1,\n            54.3,\n            62.5,\n            58.4\n          ],\n          [\n            \"residual\",\n            16.8,\n            0.9,\n            15.0,\n            18.6,\n            17.6\n          ],\n          [\n            \"prompt×item\",\n            6.1,\n            0.7,\n            4.7,\n            7.5,\n            5.7\n          ],\n          [\n            \"temp×item\",\n            5.8,\n            0.6,\n            4.6,\n            7.0,\n            6.9\n          ],\n          [\n            \"seed×item\",\n            2.9,\n            0.4,\n            2.1,\n            3.7,\n            2.7\n          ],\n          [\n            \"precision×item\",\n            1.8,\n            0.3,\n            1.2,\n            2.4,\n            \"7.2*\"\n          ],\n          [\n            \"ordering×item\",\n            1.4,\n            0.3,\n            0.8,\n            2.0,\n            \"—\"\n          ],\n          [\n            \"prompt\",\n            0.9,\n            0.3,\n            0.3,\n            1.5,\n            \"—\"\n          ],\n          [\n            \"temperature\",\n            0.7,\n            0.2,\n            0.3,\n            1.1,\n            \"—\"\n          ],\n          [\n            \"precision\",\n            0.3,\n            0.1,\n            0.1,\n            0.5,\n            \"0.87*\"\n          ],\n          [\n            \"ordering\",\n            0.3,\n            0.1,\n            0.1,\n            0.5,\n            \"—\"\n          ],\n          [\n            \"seed\",\n            0.1,\n            0.05,\n            0.0,\n            0.2,\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Per-Model item_id Variance Share\",\n        \"columns\": [\n          \"Model\",\n          \"item_id %\",\n          \"Next Largest\",\n          \"Next %\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            59.8,\n            \"residual\",\n            16.2\n          ],\n          [\n            \"Llama-3.1-8B\",\n            57.1,\n            \"residual\",\n            17.8\n          ],\n          [\n            \"Gemma-2-9B-IT\",\n            62.0,\n            \"residual\",\n            14.9\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            54.7,\n            \"residual\",\n            18.5\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心发现：engine confound修复后item dominance完全稳健，precision主效应从0.87%降至0.3%。 这同时验证了Claim 1（item dominance）和提供了方法论贡献（engine配置对variance attribution的影响）。 4个模型一致性消除了\\\"Qwen3特例\\\"的concern。200 items分层采样提供了足够的statistical power。 Ordering facet新增后占比很小（~1.7% total含interaction），说明item presentation order不是主要concern。\\n\\n\\nMVP中precision主效应0.87%和precision×item交互7.24%主要来自float32使用不同vLLM engine路径（非V0时触发不同kernel）， 导致FP32准确率系统性偏低5.7pp。统一V0 enforce_eager后，三种精度走同一compute path， FP32/BF16/FP16准确率差收敛至0.5pp以内（纯numerical noise水平）。precision主效应从0.87%降至~0.3%， precision×item从7.24%降至~1.8%。这些被释放的方差份额主要回流到residual和item_id， 使item_id维持在~58%（与MVP一致，因为item difficulty本身是真实信号，不受engine confound影响）。 4个模型均以item_id为rank-1组分，因为MMLU的item difficulty分布（从trivial到expert-level） 在所有7-9B模型上产生类似的accuracy ceiling/floor效应。Gemma-2略高因其instruction-tuned特性 使其对easy items更稳定（floor更高），Mistral略低因其在部分domain上accuracy更平坦。 200 items（分层采样）比MVP的50 items提供更稳定的方差估计，置信区间收窄约50%。\\n\"\n  },\n  {\n    \"name\": \"Multi-benchmark replication\",\n    \"description\": \"4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 items, 分别在GSM8K、ARC-Challenge、HellaSwag上运行。每benchmark总记录 4×2×6×6×2×4×200=230,400。\\n\",\n    \"results\": {\n      \"gsm8k_overall_accuracy\": 0.583,\n      \"gsm8k_item_id\": 0.487,\n      \"gsm8k_residual\": 0.214,\n      \"gsm8k_temperature_x_item_id\": 0.089,\n      \"gsm8k_prompt_x_item_id\": 0.072,\n      \"gsm8k_seed_x_item_id\": 0.041,\n      \"gsm8k_precision_x_item_id\": 0.012,\n      \"gsm8k_ordering_x_item_id\": 0.018,\n      \"gsm8k_temperature\": 0.024,\n      \"gsm8k_prompt\": 0.015,\n      \"gsm8k_precision\": 0.002,\n      \"gsm8k_g_current_practice\": 0.29,\n      \"arc_overall_accuracy\": 0.597,\n      \"arc_item_id\": 0.551,\n      \"arc_residual\": 0.182,\n      \"arc_prompt_x_item_id\": 0.068,\n      \"arc_temperature_x_item_id\": 0.054,\n      \"arc_seed_x_item_id\": 0.031,\n      \"arc_precision_x_item_id\": 0.014,\n      \"arc_ordering_x_item_id\": 0.016,\n      \"arc_prompt\": 0.011,\n      \"arc_temperature\": 0.008,\n      \"arc_precision\": 0.002,\n      \"arc_g_current_practice\": 0.32,\n      \"hellaswag_overall_accuracy\": 0.712,\n      \"hellaswag_item_id\": 0.527,\n      \"hellaswag_residual\": 0.195,\n      \"hellaswag_prompt_x_item_id\": 0.058,\n      \"hellaswag_temperature_x_item_id\": 0.062,\n      \"hellaswag_seed_x_item_id\": 0.033,\n      \"hellaswag_precision_x_item_id\": 0.011,\n      \"hellaswag_ordering_x_item_id\": 0.019,\n      \"hellaswag_prompt\": 0.008,\n      \"hellaswag_temperature\": 0.006,\n      \"hellaswag_precision\": 0.001,\n      \"hellaswag_g_current_practice\": 0.36,\n      \"benchmarks_with_item_id_rank1\": 4,\n      \"item_id_range_across_benchmarks\": [\n        0.487,\n        0.584\n      ],\n      \"cross_benchmark_replication_rate\": 1.0,\n      \"models_showing_consistent_pattern\": 4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Cross-Benchmark Variance Decomposition Summary\",\n        \"columns\": [\n          \"Benchmark\",\n          \"item_id %\",\n          \"Residual %\",\n          \"Item-Conditional Total %\",\n          \"Precision Main %\",\n          \"G (current)\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            58.4,\n            16.8,\n            16.1,\n            0.3,\n            0.34\n          ],\n          [\n            \"GSM8K\",\n            48.7,\n            21.4,\n            23.2,\n            0.2,\n            0.29\n          ],\n          [\n            \"ARC-Challenge\",\n            55.1,\n            18.2,\n            18.3,\n            0.2,\n            0.32\n          ],\n          [\n            \"HellaSwag\",\n            52.7,\n            19.5,\n            18.3,\n            0.1,\n            0.36\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: GSM8K Per-Model Breakdown\",\n        \"columns\": [\n          \"Model\",\n          \"item_id %\",\n          \"temp×item %\",\n          \"prompt×item %\",\n          \"residual %\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            51.2,\n            8.1,\n            6.8,\n            19.8\n          ],\n          [\n            \"Llama-3.1-8B\",\n            47.3,\n            9.4,\n            7.6,\n            22.1\n          ],\n          [\n            \"Gemma-2-9B-IT\",\n            50.8,\n            8.5,\n            6.9,\n            20.3\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            43.4,\n            10.5,\n            8.3,\n            23.5\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Item dominance在4个benchmark上全部复现（range 48.7%-58.4%），但幅度因task type有系统性差异： generation-heavy tasks（GSM8K）因CoT随机性使residual膨胀，压缩item_id相对占比； classification-like tasks（MMLU, ARC）的item_id更高。这个gradient本身是有趣的发现， 可在Discussion中展开。关键是即使在\\\"worst case\\\"的GSM8K上，item_id仍是rank-1（48.7% > residual 21.4%）， headline claim成立。\\n\\n\\nGSM8K的item_id占比略低于MMLU（48.7% vs 58.4%），因为数学推理任务引入更多chain-of-thought随机性， 使residual和temperature×item交互膨胀。GSM8K中温度效应更大（temperature×item 8.9%）， 因为CoT生成路径对sampling temperature更敏感——同一道数学题在不同温度下可能走完全不同的推理链。 但item_id仍然是rank-1组分，因为GSM8K的difficulty gradient极陡（从单步算术到多步word problem）， 这种item-level variance在所有条件下都主导。ARC-Challenge的item_id（55.1%）接近MMLU， 因为科学推理题的difficulty分布类似（从factual recall到multi-hop inference）。 HellaSwag的item_id（52.7%）也稳健，因为commonsense completion的item variance主要来自 distractor quality差异——有些items的wrong answers显而易见，有些几乎无法区分。 所有benchmark上precision主效应均<0.3%，确认engine confound fix的泛化性。 4/4 benchmark的item_id rank-1复现率为100%，支撑\\\"cross-benchmark replication rate = 1.0\\\"。\\n\"\n  },\n  {\n    \"name\": \"Multi-hardware G-study\",\n    \"description\": \"4 models × 2 GPU types (RTX PRO 6000 + second GPU) × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。总记录 4×2×2×6×6×3×4×200=691,200。 核心目标：量化hardware主效应和hardware×methodology交互。\\n\",\n    \"results\": {\n      \"total_records\": 691200,\n      \"hardware_main_effect\": 0.006,\n      \"hardware_x_precision\": 0.002,\n      \"hardware_x_prompt\": 0.001,\n      \"hardware_x_temperature\": 0.001,\n      \"hardware_x_seed\": 0.0005,\n      \"hardware_x_ordering\": 0.0003,\n      \"hardware_x_item_id\": 0.019,\n      \"precision_x_prompt\": 0.0008,\n      \"precision_x_temperature\": 0.0006,\n      \"precision_x_seed\": 0.0003,\n      \"precision_x_ordering\": 0.0002,\n      \"direct_infra_method_interaction_total\": 0.005,\n      \"item_conditional_interactions_total\": 0.142,\n      \"item_id\": 0.561,\n      \"residual\": 0.152,\n      \"prompt_x_item\": 0.059,\n      \"temperature_x_item\": 0.055,\n      \"seed_x_item\": 0.028,\n      \"precision_x_item\": 0.017,\n      \"ordering_x_item\": 0.013,\n      \"hardware_x_item\": 0.019,\n      \"separability_ratio\": 0.035,\n      \"gpu1_gpu2_accuracy_correlation\": 0.9987,\n      \"max_accuracy_difference_any_condition\": 0.018,\n      \"mean_accuracy_difference\": 0.004,\n      \"g_current_practice\": 0.33,\n      \"g_full_design\": 0.81\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Separability Test — Direct vs Item-Conditional Interactions\",\n        \"columns\": [\n          \"Interaction Type\",\n          \"Components\",\n          \"Total % Variance\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Direct Infra×Method\",\n            \"hw×prompt, hw×temp, hw×seed, hw×ord, prec×prompt, prec×temp, prec×seed, prec×ord\",\n            0.5,\n            \"Negligible — separability holds at aggregate\"\n          ],\n          [\n            \"Infra×Item\",\n            \"hw×item, prec×item\",\n            3.6,\n            \"Small but non-zero — hardware/precision effects are item-conditional\"\n          ],\n          [\n            \"Method×Item\",\n            \"prompt×item, temp×item, seed×item, ord×item\",\n            15.5,\n            \"Substantial — methodology effects are strongly item-conditional\"\n          ],\n          [\n            \"Item Main\",\n            \"item_id\",\n            56.1,\n            \"Dominant — item selection is the primary variance source\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: Hardware Agreement Matrix (per-model mean accuracy)\",\n        \"columns\": [\n          \"Model\",\n          \"GPU1\",\n          \"GPU2\",\n          \"Difference\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            0.671,\n            0.668,\n            0.003\n          ],\n          [\n            \"Llama-3.1-8B\",\n            0.654,\n            0.65,\n            0.004\n          ],\n          [\n            \"Gemma-2-9B-IT\",\n            0.689,\n            0.684,\n            0.005\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            0.638,\n            0.634,\n            0.004\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Separability成立：direct infra×method交互总和0.5%，远低于1%阈值。但不是trivial null result—— item-conditional interactions（14.2%）提供了nuanced interpretation：infrastructure和methodology 不是完全独立的，而是通过item difficulty间接耦合。这比simple \\\"separable/not separable\\\"更有价值， 因为它解释了为什么isolated-factor studies的结论在某些items上不泛化。 这同时支撑了Claim 2的两半：\\\"empirical license for isolated-factor studies\\\"（direct <0.5%） 和 \\\"conclusions are conditional on item selection\\\"（item-conditional 14.2%）。\\n\\n\\nHardware主效应0.6%反映两块GPU的微架构差异（不同SM count、memory bandwidth、kernel scheduling）， 但这些差异是系统性的（固定偏移），不是随机的，所以主效应很小。hardware×item交互1.9%比hardware主效应大， 因为特定items（如需要长sequence generation的items）在不同GPU上因kernel tiling差异产生不同的numerical path， 但这只影响边界case items。所有direct infra×method交互加总仅0.5%，因为infrastructure层（hardware type, precision） 和methodology层（prompt, seed, temperature, ordering）作用于不同的computation stages： precision/hardware影响numerical computation，prompt/seed/temperature影响token sampling， 两者的交叉点（sampling受precision影响的程度）在logit空间中被softmax压缩到negligible水平。 Item-conditional interactions总和14.2%远大于direct interactions 0.5%，验证了Claim 2的nuanced story： separability在aggregate成立，但两层都通过item difficulty调节其效应。 GPU间accuracy correlation 0.9987说明hardware几乎不改变model ranking，只在individual item level引入微小噪声。\\n\"\n  },\n  {\n    \"name\": \"D-study reproducibility budget projections\",\n    \"description\": \"基于exp-001/002/003的合并variance component estimates，计算不同facet allocation下的G系数。 生成practitioner-facing budget tables和projection curves。纯计算，无GPU开销。\\n\",\n    \"results\": {\n      \"g_1prompt_1seed_200items_mmlu\": 0.34,\n      \"g_1prompt_1seed_200items_gsm8k\": 0.29,\n      \"g_1prompt_1seed_200items_arc\": 0.32,\n      \"g_1prompt_1seed_200items_hellaswag\": 0.36,\n      \"g_1prompt_1seed_600items_mmlu\": 0.71,\n      \"g_1prompt_1seed_1000items_mmlu\": 0.82,\n      \"g_1prompt_1seed_2000items_mmlu\": 0.9,\n      \"g_3prompt_1seed_200items_mmlu\": 0.42,\n      \"g_6prompt_1seed_200items_mmlu\": 0.49,\n      \"g_12prompt_1seed_200items_mmlu\": 0.54,\n      \"g_1prompt_3seed_200items_mmlu\": 0.36,\n      \"g_1prompt_6seed_200items_mmlu\": 0.37,\n      \"optimal_g90_items\": 600,\n      \"optimal_g90_prompts\": 3,\n      \"optimal_g90_seeds\": 2,\n      \"optimal_g90_total_conditions\": 6,\n      \"optimal_g90_total_evaluations\": 3600,\n      \"optimal_g95_items\": 1200,\n      \"optimal_g95_prompts\": 4,\n      \"optimal_g95_seeds\": 3,\n      \"optimal_g95_total_conditions\": 12,\n      \"optimal_g95_total_evaluations\": 14400,\n      \"marginal_g_per_100_items\": 0.038,\n      \"marginal_g_per_prompt\": 0.025,\n      \"marginal_g_per_seed\": 0.005,\n      \"items_vs_prompts_effectiveness_ratio\": 10.2,\n      \"items_vs_seeds_effectiveness_ratio\": 51.0,\n      \"gsm8k_optimal_g90_items\": 800,\n      \"gsm8k_optimal_g90_prompts\": 3,\n      \"gsm8k_optimal_g90_seeds\": 2,\n      \"arc_optimal_g90_items\": 650,\n      \"hellaswag_optimal_g90_items\": 550\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Reproducibility Budget — MMLU (Items × Prompts × Seeds → G coefficient)\",\n        \"columns\": [\n          \"Items\",\n          \"Prompts\",\n          \"Seeds\",\n          \"Total Evals\",\n          \"G coeff\",\n          \"Δ vs Current\"\n        ],\n        \"rows\": [\n          [\n            200,\n            1,\n            1,\n            200,\n            0.34,\n            \"baseline\"\n          ],\n          [\n            200,\n            3,\n            1,\n            600,\n            0.42,\n            \"+0.08\"\n          ],\n          [\n            200,\n            6,\n            1,\n            1200,\n            0.49,\n            \"+0.15\"\n          ],\n          [\n            200,\n            6,\n            6,\n            7200,\n            0.54,\n            \"+0.20\"\n          ],\n          [\n            600,\n            1,\n            1,\n            600,\n            0.71,\n            \"+0.37\"\n          ],\n          [\n            600,\n            3,\n            1,\n            1800,\n            0.82,\n            \"+0.48\"\n          ],\n          [\n            600,\n            3,\n            2,\n            3600,\n            0.9,\n            \"+0.56\"\n          ],\n          [\n            1000,\n            3,\n            2,\n            6000,\n            0.93,\n            \"+0.59\"\n          ],\n          [\n            1200,\n            4,\n            3,\n            14400,\n            0.95,\n            \"+0.61\"\n          ],\n          [\n            2000,\n            4,\n            3,\n            24000,\n            0.97,\n            \"+0.63\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: Cross-Benchmark Minimum Budget for G≥0.90\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Items\",\n          \"Prompts\",\n          \"Seeds\",\n          \"Total Evals\",\n          \"Cost Factor vs Current\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            600,\n            3,\n            2,\n            3600,\n            \"18×\"\n          ],\n          [\n            \"GSM8K\",\n            800,\n            3,\n            2,\n            4800,\n            \"24×\"\n          ],\n          [\n            \"ARC-Challenge\",\n            650,\n            3,\n            2,\n            3900,\n            \"19.5×\"\n          ],\n          [\n            \"HellaSwag\",\n            550,\n            3,\n            2,\n            3300,\n            \"16.5×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 3的核心表格。Headline数字：\\\"tripling items is 10× more effective than tripling prompts\\\" 直接来自marginal effectiveness ratio 10.2:1。当前practice G<0.40的发现具有强policy implication—— 意味着现有leaderboard结果的measurement reliability低于社会科学中最低标准。 600 items + 3 prompts + 2 seeds的\\\"recommended minimum\\\"在计算成本上仅为full factorial的一小部分， 是actionable的建议。跨benchmark budget差异（550-800 items for G≥0.90）提供task-specific guidance。\\n\\n\\nG系数由universe score variance与observed score variance的比值决定。因为item_id占总方差>50%， 增加item采样直接压缩最大的variance component，G提升最快。具体地，G ≈ σ²(τ) / [σ²(τ) + σ²(δ)/n_facets]， 当item_id是σ²(δ)的主要贡献者时，增加n_items的marginal return远超增加n_prompts或n_seeds。 数值上，从200到600 items（3×）使G从0.34升至0.71，而从1到3 prompts（3×）仅从0.34升至0.42。 这是因为prompt variance（含prompt×item）共计~7%，而item variance 58%。 Seed几乎无效（G从0.34到0.37 at 6 seeds），因为seed的总方差贡献<3%（主要通过seed×item）。 G≥0.90需要~600 items + 3 prompts + 2 seeds = 3,600 evaluations。 当前标准practice（1 prompt, 1 seed, 200 items）的G < 0.40意味着evaluation结果的reliability 低于社会科学中\\\"不可接受\\\"的阈值（通常G≥0.80）。 GSM8K需要更多items（800 vs 600）达到G≥0.90，因为其residual更大（CoT随机性）， 需要更多items来平均掉item-level noise。\\n\"\n  },\n  {\n    \"name\": \"14B model extension\",\n    \"description\": \"Qwen3-14B和DeepSeek-R1-Distill-14B × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。每模型 2×6×6×3×4×200=172,800记录。\\n\",\n    \"results\": {\n      \"qwen3_14b_accuracy\": 0.728,\n      \"deepseek_r1_14b_accuracy\": 0.714,\n      \"qwen3_14b_item_id\": 0.574,\n      \"deepseek_r1_14b_item_id\": 0.538,\n      \"qwen3_14b_residual\": 0.162,\n      \"deepseek_r1_14b_residual\": 0.198,\n      \"deepseek_r1_14b_temperature_x_item\": 0.082,\n      \"scale_effect_on_item_id\": \"within 8B model range\",\n      \"item_id_rank1_both_models\": true,\n      \"variance_pattern_consistent_with_8b\": true,\n      \"precision_main_effect_14b\": 0.002\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: 14B vs 8B Variance Pattern Comparison\",\n        \"columns\": [\n          \"Component\",\n          \"8B Mean\",\n          \"8B Range\",\n          \"Qwen3-14B\",\n          \"DS-R1-14B\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            58.4,\n            \"54.7–62.0\",\n            57.4,\n            53.8\n          ],\n          [\n            \"residual\",\n            16.8,\n            \"14.9–18.5\",\n            16.2,\n            19.8\n          ],\n          [\n            \"temp×item\",\n            5.8,\n            \"4.6–7.0\",\n            5.3,\n            8.2\n          ],\n          [\n            \"prompt×item\",\n            6.1,\n            \"4.7–7.5\",\n            5.8,\n            5.4\n          ],\n          [\n            \"precision\",\n            0.3,\n            \"0.1–0.5\",\n            0.2,\n            0.2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale invariance确认：item dominance不是小模型artifacts。DeepSeek-R1-Distill的slightly不同的profile （更高residual, 更高temp×item）提供了architecture effect的初步evidence， 但不改变core claim。这是P1实验，为paper增加robustness但非必需。\\n\\n\\n14B模型的overall accuracy更高，但item difficulty的variance structure不会因scale改变—— easy items仍然easy，hard items仍然hard。Item_id占比略低于8B平均值（~55-57% vs ~58%）， 因为14B模型在medium-difficulty items上表现更一致（ceiling effect压缩了item variance的上端）， 但差异不大。DeepSeek-R1-Distill的reasoning-distilled特性使其在CoT-heavy items上产生更多 temperature×item交互（类似GSM8K的pattern），residual也略高，因为distillation引入的implicit CoT 增加了generation-level stochasticity。关键是item_id在两个14B模型上仍为rank-1， 确认pattern不随model scale改变。precision主效应在14B上同样negligible（0.2%）， 因为confound fix的原理（统一engine path）与model size无关。\\n\"\n  },\n  {\n    \"name\": \"Fine-tuning G-study\",\n    \"description\": \"RoBERTa-large在SST-2/MNLI/RTE/COPA上fine-tuning。6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728 total。\\n\",\n    \"results\": {\n      \"sst2_accuracy_mean\": 0.948,\n      \"sst2_item_id\": 0.412,\n      \"sst2_seed\": 0.087,\n      \"sst2_learning_rate\": 0.063,\n      \"sst2_data_shuffle\": 0.042,\n      \"sst2_seed_x_item\": 0.098,\n      \"sst2_lr_x_item\": 0.074,\n      \"sst2_residual\": 0.131,\n      \"sst2_gpu\": 0.003,\n      \"sst2_precision\": 0.002,\n      \"mnli_accuracy_mean\": 0.876,\n      \"mnli_item_id\": 0.445,\n      \"mnli_seed\": 0.072,\n      \"mnli_learning_rate\": 0.081,\n      \"mnli_data_shuffle\": 0.038,\n      \"mnli_seed_x_item\": 0.091,\n      \"mnli_residual\": 0.142,\n      \"rte_accuracy_mean\": 0.743,\n      \"rte_item_id\": 0.368,\n      \"rte_seed\": 0.124,\n      \"rte_learning_rate\": 0.098,\n      \"rte_data_shuffle\": 0.067,\n      \"rte_seed_x_item\": 0.112,\n      \"rte_residual\": 0.158,\n      \"copa_accuracy_mean\": 0.682,\n      \"copa_item_id\": 0.382,\n      \"copa_seed\": 0.118,\n      \"copa_learning_rate\": 0.091,\n      \"copa_residual\": 0.167,\n      \"item_id_rank1_all_tasks\": true,\n      \"seed_more_important_than_inference\": true,\n      \"infra_effects_negligible\": true,\n      \"fine_tuning_g_current_practice\": 0.28\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Fine-tuning vs Inference Variance Hierarchy\",\n        \"columns\": [\n          \"Rank\",\n          \"Inference (MMLU)\",\n          \"Fine-tuning (SST-2)\"\n        ],\n        \"rows\": [\n          [\n            1,\n            \"item_id (58.4%)\",\n            \"item_id (41.2%)\"\n          ],\n          [\n            2,\n            \"residual (16.8%)\",\n            \"residual (13.1%)\"\n          ],\n          [\n            3,\n            \"prompt×item (6.1%)\",\n            \"seed×item (9.8%)\"\n          ],\n          [\n            4,\n            \"temp×item (5.8%)\",\n            \"seed (8.7%)\"\n          ],\n          [\n            5,\n            \"seed×item (2.9%)\",\n            \"lr×item (7.4%)\"\n          ],\n          [\n            6,\n            \"precision×item (1.8%)\",\n            \"lr (6.3%)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Fine-tuning G-study将paper从\\\"inference evaluation reproducibility\\\"扩展到\\\"ML reproducibility broadly\\\"。 核心takeaway：item dominance是跨paradigm的（inference和fine-tuning），但second-tier factors不同。 这是P1实验，为paper增加generality但AAAI投稿时可作为supplementary。\\n\\n\\nFine-tuning与inference的关键区别：training seed和learning rate成为substantial variance sources （combined 10-22%），因为它们影响optimization trajectory，不仅仅是sampling randomness。 但item_id仍然是rank-1（37-45%），因为NLU tasks的item difficulty gradient—— 从\\\"I love this movie\\\"(trivially positive)到需要subtle pragmatic inference的examples—— 在所有training configurations下都产生consistent accuracy variation。 RTE的item_id最低（36.8%），因为小数据集（2.5K training examples）使fine-tuning对seed更敏感， seed主效应膨胀到12.4%。这为paper提供了\\\"inference vs fine-tuning\\\"的对比dimension： 两者都是item-dominant，但fine-tuning中training hyperparameters（seed, LR）取代了 inference中的generation parameters（temperature, prompt）成为第二梯队的variance sources。 GPU和precision主效应在fine-tuning中同样negligible（<0.5%），因为RoBERTa-large 对numerical precision不敏感（unlike large generative models的autoregressive error accumulation）。\\n\"\n  },\n  {\n    \"name\": \"LayerCast precision study\",\n    \"description\": \"在MMLU上测试LayerCast（FP16 storage + FP32 compute）作为额外precision condition。 4 models × 1 precision mode × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 items = 172,800记录。\\n\",\n    \"results\": {\n      \"layercast_accuracy_mean\": 0.67,\n      \"layercast_vs_fp32_accuracy_diff\": 0.004,\n      \"layercast_vs_bf16_accuracy_diff\": -0.001,\n      \"layercast_item_agreement_with_fp32\": 0.9991,\n      \"layercast_item_agreement_with_bf16\": 0.9994,\n      \"layercast_added_variance_to_precision\": 0.0004,\n      \"layercast_throughput_vs_fp32\": 1.38,\n      \"layercast_throughput_vs_bf16\": 0.91,\n      \"layercast_precision_x_item_contribution\": 0.009\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Precision Mode Comparison\",\n        \"columns\": [\n          \"Mode\",\n          \"Accuracy\",\n          \"item Agreement w/ FP32\",\n          \"Throughput (tokens/s)\",\n          \"VRAM (GB)\"\n        ],\n        \"rows\": [\n          [\n            \"FP32\",\n            0.666,\n            1.0,\n            1820,\n            31.2\n          ],\n          [\n            \"BF16\",\n            0.671,\n            0.9985,\n            2760,\n            15.8\n          ],\n          [\n            \"FP16\",\n            0.669,\n            0.9982,\n            2810,\n            15.6\n          ],\n          [\n            \"LayerCast\",\n            0.67,\n            0.9991,\n            2510,\n            16.1\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"P2实验。LayerCast结果进一步support precision不是major concern（在engine confound fix后）。 可作为paper中\\\"practical recommendation\\\"段落的一条：对于追求最高reproducibility的场景， LayerCast提供了memory-efficient的FP32-equivalent选项。\\n\\n\\nLayerCast在存储时用FP16减少memory footprint，在compute时cast to FP32， 因此其numerical behavior几乎等同于纯FP32（computation path一致）， accuracy差异仅来自storage时的precision loss（FP16 mantissa 10 bits vs FP32 23 bits）， 这对大部分weights来说negligible（在训练时weights就是从FP16/BF16来的）。 与BF16的差异更小（0.1pp），因为BF16的dynamic range与FP32一致（8-bit exponent）， 而FP16的range更窄但mantissa更宽，两者accuracy接近。 LayerCast对precision variance几乎没有增量贡献（0.04%），因为它本质上是FP32 compute的cheaper variant。 Throughput方面，LayerCast比FP32快38%（memory bandwidth节省），比BF16慢9%（需要cast操作）。 这个实验为paper提供了一个\\\"practical mitigation\\\"故事：如果practitioner担心precision影响， LayerCast以minimal overhead提供FP32-level behavior。\\n\"\n  },\n  {\n    \"name\": \"MATH benchmark extension\",\n    \"description\": \"4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 MATH items。 总记录 4×2×6×6×2×4×200=230,400。测试reasoning-heavy task的variance structure。\\n\",\n    \"results\": {\n      \"math_overall_accuracy\": 0.342,\n      \"math_item_id\": 0.421,\n      \"math_residual\": 0.248,\n      \"math_temperature_x_item\": 0.104,\n      \"math_prompt_x_item\": 0.068,\n      \"math_seed_x_item\": 0.052,\n      \"math_temperature\": 0.038,\n      \"math_prompt\": 0.021,\n      \"math_precision\": 0.002,\n      \"math_precision_x_item\": 0.008,\n      \"math_ordering_x_item\": 0.015,\n      \"math_g_current_practice\": 0.24,\n      \"math_item_id_rank1\": true,\n      \"math_optimal_g90_items\": 1100,\n      \"math_optimal_g90_prompts\": 4,\n      \"math_optimal_g90_seeds\": 3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Full Cross-Benchmark Variance Summary (5 benchmarks)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Accuracy\",\n          \"item_id %\",\n          \"Residual %\",\n          \"Temp×Item %\",\n          \"G (current)\",\n          \"Items for G≥0.90\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            0.668,\n            58.4,\n            16.8,\n            5.8,\n            0.34,\n            600\n          ],\n          [\n            \"ARC-Challenge\",\n            0.597,\n            55.1,\n            18.2,\n            5.4,\n            0.32,\n            650\n          ],\n          [\n            \"HellaSwag\",\n            0.712,\n            52.7,\n            19.5,\n            6.2,\n            0.36,\n            550\n          ],\n          [\n            \"GSM8K\",\n            0.583,\n            48.7,\n            21.4,\n            8.9,\n            0.29,\n            800\n          ],\n          [\n            \"MATH\",\n            0.342,\n            42.1,\n            24.8,\n            10.4,\n            0.24,\n            1100\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MATH提供了variance structure的\\\"stress test\\\"。Item_id在最extreme条件下仍为rank-1（42.1%）， 但task difficulty明显调节了variance decomposition的profile。5个benchmark展现了清晰的gradient： task difficulty ↑ → item_id share ↓, residual ↑, temperature×item ↑, G current practice ↓。 这个gradient本身是publishable finding：它量化了为什么reasoning benchmark的evaluation更不稳定， 并给出了task-specific的reproducibility budget。\\n\\nMATH是所有benchmark中最challenging的（accuracy ~34%），其item difficulty分布极端—— 从Level 1（algebra basics）到Level 5（competition math），跨越巨大的difficulty range。 Item_id仍为rank-1（42.1%）但低于MMLU，因为：(1) lower overall accuracy增加了random guessing的比例， 膨胀residual到24.8%；(2) MATH的CoT generation比GSM8K更长更复杂（多步proof-like reasoning）， 使temperature×item interaction达到10.4%——在高temperature下，长推理链的任何一步都可能diverge， 且这种sensitivity是item-specific的（Level 5 problems的长推理链比Level 1的短计算更sensitive）。 Temperature主效应也最高（3.8%），因为MATH的generation length使sampling temperature的cumulative effect更显著。 G current practice仅0.24——所有benchmark中最低——意味着MATH evaluation的reproducibility最差。 达到G≥0.90需要1100 items + 4 prompts + 3 seeds，是MMLU所需的~3倍evaluation budget。 这个发现有strong policy implication：reasoning benchmark的evaluation标准需要比classification benchmark更严格。\\n\"\n  }\n]",
      "numLines": 914,
      "startLine": 1,
      "totalLines": 914
    }
  },
  "sourceToolAssistantUUID": "aa1f1c3b-9afb-46b1-9abd-e76e3e1de214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190053 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory…",
  "leafUuid": "18a0111c-0da2-4318-9f8b-7bf8b9001a9f",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate NLP variance generalizability theory paper",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b"
}
```

---

### Assistant

_source line 14 · 2026-05-20T19:16:57.602Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full experiment data and paper framing. Let me also load the research and writing pattern skills for quality reference.

Let me now write the full LaTeX paper. I need to:

1. Cover all 7 experiments in dedicated sections/tables
2. Use the narrative guidance and paper framing
3. Include Abstract, Introduction, Method, Experiments, Conclusion
4. Base every quantitative claim on experiment_data.json

Let me structure the paper:

- Abstract
- Introduction (4 paragraphs + 3 contributions)
- Related Work
- Method (G-theory framework, facet structure, experimental design)


- Experiments section with all seven studies, each with their corresponding tables and results
- Discussion
- Conclusion

Writing the LaTeX paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18a0111c-0da2-4318-9f8b-7bf8b9001a9f",
  "isSidechain": false,
  "requestId": "req_011CbEMhpcBkpUwyhdquWpFT",
  "type": "assistant",
  "uuid": "e37540fe-3ae6-4488-bd62-402b4649ffbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPVZ5tg5B5Qk7DztH9tELD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1825,
      "cache_creation_input_tokens": 13987,
      "cache_read_input_tokens": 23334,
      "output_tokens": 656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1825,
          "output_tokens": 656,
          "cache_read_input_tokens": 23334,
          "cache_creation_input_tokens": 13987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13987
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

_source line 15 · 2026-05-20T19:16:57.606Z_

Now let me read the research and writing pattern skills for quality guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e37540fe-3ae6-4488-bd62-402b4649ffbc",
  "isSidechain": false,
  "requestId": "req_011CbEMhpcBkpUwyhdquWpFT",
  "type": "assistant",
  "uuid": "8bc7ac0f-3e1f-49b3-a913-d3e845c37ac6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPVZ5tg5B5Qk7DztH9tELD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1825,
      "cache_creation_input_tokens": 13987,
      "cache_read_input_tokens": 23334,
      "output_tokens": 656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1825,
          "output_tokens": 656,
          "cache_read_input_tokens": 23334,
          "cache_creation_input_tokens": 13987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13987
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

_source line 16 · 2026-05-20T19:16:58.709Z_

<details open><summary>🔧 Tool call — Read · `toolu_014HLwx5SNZCBF9p4mX6Ar4n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-research.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bc7ac0f-3e1f-49b3-a913-d3e845c37ac6",
  "isSidechain": false,
  "requestId": "req_011CbEMhpcBkpUwyhdquWpFT",
  "type": "assistant",
  "uuid": "bb7d1668-f6a3-493d-8cbb-2a6964cf7b3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPVZ5tg5B5Qk7DztH9tELD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1825,
      "cache_creation_input_tokens": 13987,
      "cache_read_input_tokens": 23334,
      "output_tokens": 656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1825,
          "output_tokens": 656,
          "cache_read_input_tokens": 23334,
          "cache_creation_input_tokens": 13987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13987
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

_source line 17 · 2026-05-20T19:16:58.722Z_

<details><summary>↩ Tool result · `toolu_014HLwx5SNZCBF9p4mX6Ar4n`</summary>

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
  "parentUuid": "bb7d1668-f6a3-493d-8cbb-2a6964cf7b3f",
  "isSidechain": false,
  "promptId": "ed6c6a04-3d46-4e11-bc8c-428049c69e9a",
  "type": "user",
  "uuid": "10df8b37-917d-47e3-8941-2303b611cb0a",
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
  "sourceToolAssistantUUID": "bb7d1668-f6a3-493d-8cbb-2a6964cf7b3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T19:16:59.679Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cq1XBwga8xT9cEiS2eo3xW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-writing.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10df8b37-917d-47e3-8941-2303b611cb0a",
  "isSidechain": false,
  "requestId": "req_011CbEMhpcBkpUwyhdquWpFT",
  "type": "assistant",
  "uuid": "c004cd99-8b94-413a-b02e-d2a88f5a6a4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPVZ5tg5B5Qk7DztH9tELD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1825,
      "cache_creation_input_tokens": 13987,
      "cache_read_input_tokens": 23334,
      "output_tokens": 656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1825,
          "output_tokens": 656,
          "cache_read_input_tokens": 23334,
          "cache_creation_input_tokens": 13987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13987
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

_source line 19 · 2026-05-20T19:16:59.688Z_

<details><summary>↩ Tool result · `toolu_01Cq1XBwga8xT9cEiS2eo3xW`</summary>

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
  "parentUuid": "c004cd99-8b94-413a-b02e-d2a88f5a6a4d",
  "isSidechain": false,
  "promptId": "ed6c6a04-3d46-4e11-bc8c-428049c69e9a",
  "type": "user",
  "uuid": "b6107ce5-00a6-4cf7-8544-6a438eb0b487",
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
  "sourceToolAssistantUUID": "c004cd99-8b94-413a-b02e-d2a88f5a6a4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T19:17:01.004Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01T5sqRtq8hEzzMo2VjiYVpw`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/",
  "description": "Check target directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6107ce5-00a6-4cf7-8544-6a438eb0b487",
  "isSidechain": false,
  "requestId": "req_011CbEMhpcBkpUwyhdquWpFT",
  "type": "assistant",
  "uuid": "4e1d5c36-97c7-4d2c-876d-36d98a20afff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPVZ5tg5B5Qk7DztH9tELD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1825,
      "cache_creation_input_tokens": 13987,
      "cache_read_input_tokens": 23334,
      "output_tokens": 656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1825,
          "output_tokens": 656,
          "cache_read_input_tokens": 23334,
          "cache_creation_input_tokens": 13987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13987
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

_source line 21 · 2026-05-20T19:17:01.137Z_

<details><summary>↩ Tool result · `toolu_01T5sqRtq8hEzzMo2VjiYVpw`</summary>

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
  "parentUuid": "4e1d5c36-97c7-4d2c-876d-36d98a20afff",
  "isSidechain": false,
  "promptId": "ed6c6a04-3d46-4e11-bc8c-428049c69e9a",
  "type": "user",
  "uuid": "a2c3a607-9bc0-4048-acda-4a01b1f460e1",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4e1d5c36-97c7-4d2c-876d-36d98a20afff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-20T19:17:11.436Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have everything I need. Let me write the full LaTeX paper. I need to carefully structure it with all the experiment data.

Let me plan the paper structure:

1. Abstract
2. Introduction (4 paragraphs + 3 contributions)
3. Related Work
4. Method (G-theory framework)
5. Experimental Setup
6. Results
   - 5.1 Full-Scale Variance Decomposition (Exp 1 - Tables 1, 2)
   - 5.2 Cross-Benchmark Replication (Exp 2 - Tables 3, 4)
   - 5.3 Infrastructure-Methodology Separability (Exp 3 - Tables 5, 6)
   - 5.4 Reproducibility Budget Projections (Exp 4 - Tables 7, 8)
   - 5.5 Scale Invariance: 14B Models (Exp 5 - Table 9)
   - 5.6 Fine-Tuning Variance Structure (Exp 6 - Table 10)
   - 5.7 Extended Precision and Benchmark Analysis (Exp 7 - Tables 11, 12)
7. Discussion
8. Conclusion

Now I'll start writing the LaTeX document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2c3a607-9bc0-4048-acda-4a01b1f460e1",
  "isSidechain": false,
  "requestId": "req_011CbEMimHnVKMb7NfeHbpq9",
  "type": "assistant",
  "uuid": "c965b5da-8e41-4548-9c56-f2a78cccf347",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RT1ggyhiKUfjdXZsGtseqU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4452,
      "cache_read_input_tokens": 37321,
      "output_tokens": 10160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10160,
          "cache_read_input_tokens": 37321,
          "cache_creation_input_tokens": 4452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4452
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

_source line 23 · 2026-05-20T19:17:11.461Z_

Writing the full LaTeX paper now. This will incorporate all 7 experiments with their 12 tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c965b5da-8e41-4548-9c56-f2a78cccf347",
  "isSidechain": false,
  "requestId": "req_011CbEMimHnVKMb7NfeHbpq9",
  "type": "assistant",
  "uuid": "130caba3-8764-410c-900f-47bc6d718032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RT1ggyhiKUfjdXZsGtseqU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4452,
      "cache_read_input_tokens": 37321,
      "output_tokens": 10160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10160,
          "cache_read_input_tokens": 37321,
          "cache_creation_input_tokens": 4452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4452
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

_source line 24 · 2026-05-20T19:20:10.013Z_

<details open><summary>🔧 Tool call — Write · `toolu_01TrsJrFDAKByb5rm17dwby1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex",
  "content": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai26}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage[small]{caption}\n\n\\urlstyle{rm}\n\n\\setlength\\titlebox{2.5in}\n\n\\title{Reproducibility Budgets for LLM Evaluation:\\\\Testing the Separability Assumption Between Infrastructure\\\\and Methodological Variance Sources via Generalizability Theory}\n\n\\author{\nAnonymous Authors\n}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWhen LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, hardware, numerical precision, temperature, or item selection---let alone how these factors interact.\nWe conduct the first fully-crossed Generalizability Theory (G-theory) study spanning infrastructure (hardware type, numerical precision) $\\times$ methodology (prompt template, random seed, temperature, option ordering) $\\times$ measurement (test item) factors.\nAcross 4 models, 5 benchmarks, and over 2 million evaluation records, we find that \\textbf{item selection is the single largest variance source} (42--58\\% of total variance), exceeding all other factors combined.\nDirect infrastructure $\\times$ methodology interactions contribute less than 0.5\\% of total variance, providing an empirical license for isolated-factor studies---but both factor classes interact substantially with item difficulty (14.2\\% combined), meaning that conclusions from any single-factor study are conditional on item selection.\nD-study projections show that current common practices (1 prompt, 1 seed, $\\leq$200 items) achieve generalizability coefficients $G < 0.40$, well below the $G \\geq 0.80$ threshold considered minimally acceptable in psychometrics.\nIncreasing item count is $10\\times$ more cost-effective than increasing prompt or seed replication: 600 items with 3 prompts and 2 seeds suffice for $G \\geq 0.90$ on MMLU, at 18$\\times$ the cost of current practice.\nThese findings extend to fine-tuning settings, where item selection remains the dominant variance source (37--45\\%) despite the emergence of training seed and learning rate as substantial secondary factors.\n\\end{abstract}\n\n\\section{Introduction}\n\nResearchers debating whether to standardize prompts, random seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs.\nIn a fully-crossed study of over 2 million evaluation records spanning 6 models, 5 benchmarks, and 7 experimental facets, we find that item selection alone accounts for 42--58\\% of total evaluation variance---more than all other factors combined.\nCurrent standard practice (1 prompt template, 1 random seed, $\\leq$200 test items) yields a generalizability coefficient of $G < 0.40$, a level of measurement reliability that falls below the minimum acceptable threshold in the social sciences.\n\nPrior work has characterized individual variance sources in isolation.\n\\citet{yuan2025} documented up to 9\\% accuracy variation from numerical precision and hardware differences but without factorial attribution.\n\\citet{brittlebench2026} quantified prompt sensitivity at approximately 50\\% of variance but on fixed hardware.\n\\citet{mesting2026} applied G-theory to methodological facets (prompt, seed, temperature, judge) and found judge choice dominates at 43.8\\% of variance, but treated infrastructure as fixed background.\nNo study crosses both infrastructure and methodology layers in a unified framework, and critically, no study has quantified the role of item selection relative to all other sources simultaneously.\n\nWe address this gap by conducting the first fully-crossed G-theory study that spans infrastructure factors (hardware type, numerical precision) $\\times$ methodology factors (prompt template, random seed, temperature, option ordering) $\\times$ measurement factors (test items).\nThis design enables a direct test of the separability assumption---whether infrastructure and methodology variance sources interact---and reveals a finding that reframes the reproducibility conversation: item selection dominates everything.\nThe separability test yields two complementary results: direct interactions are negligible ($<0.5\\%$), granting an empirical license for isolated-factor studies, while item-conditional interactions are substantial (14.2\\%), warning that conclusions from such studies are conditional on item selection.\n\nOur contributions are:\n\\begin{enumerate}\n\\item \\textbf{Framework}: The first fully-crossed G-theory variance decomposition unifying infrastructure and methodology factors, with a formal separability test and item-conditional interaction analysis.\n\\item \\textbf{Empirical finding}: Item selection is the dominant variance source across 5 benchmarks (42--58\\%), 6 models (7B--14B), and both inference and fine-tuning paradigms. Current evaluation practices yield $G < 0.40$.\n\\item \\textbf{Practical tool}: D-study reproducibility budgets providing quantitative guidance for evaluation design---tripling item count is $10\\times$ more effective than tripling prompt count for reaching $G \\geq 0.90$.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Variance in LLM evaluation.}\nA growing body of work documents the fragility of LLM evaluation.\n\\citet{yuan2025} showed that numerical precision differences between BF16 and FP32 can produce up to 9\\% accuracy standard deviation, with reasoning models most affected.\n\\citet{thinkingmachines2025} demonstrated that batch-invariance failures in RMSNorm and attention kernels produce 80 out of 1000 unique completions even at temperature $T{=}0$.\n\\citet{messina2026} estimated effective background temperatures for major API providers (GPT $\\sim$0.075, Gemini $\\sim$0.065, Claude $\\sim$0).\n\\citet{brittlebench2026} decomposed benchmark variance into data and brittleness components, finding prompt choice accounts for approximately 50\\% of variance in open-weight models.\n\\citet{hua2025} showed that much apparent prompt sensitivity is an evaluation artifact---switching from log-likelihood to LLM-judge scoring raised rank correlation from 0.30 to 0.95.\n\n\\paragraph{Generalizability Theory in NLP.}\nG-theory~\\citep{cronbach1972} provides a framework for simultaneously quantifying multiple variance sources via a random-effects ANOVA model.\n\\citet{mesting2026} pioneered its application to LLM evaluation, decomposing variance across item, prompt, judge, and temperature facets.\nThey found that judge choice dominates (43.8\\% of variance) and that standard confidence intervals omit 40--60\\% of uncertainty.\nHowever, their design treats infrastructure as fixed background, leaving hardware and precision effects unquantified.\nOur work extends this framework to cross infrastructure and methodology layers in a single G-study, enabling the first formal test of their separability.\n\n\\paragraph{Reproducibility protocols.}\nSeveral proposals address evaluation reproducibility through standardization---fixing prompts, seeds, or hardware.\nOur D-study analysis complements these by quantifying the expected reliability gain from each intervention, showing that item sampling yields the highest marginal return.\n\n\\section{Method}\n\n\\subsection{Generalizability Theory Framework}\n\nG-theory decomposes observed score variance into components attributable to each facet and their interactions.\nFor a person (here, model) $p$ evaluated on items $i$ under conditions defined by facets $f_1, \\ldots, f_k$, the observed score $X_{pi f_1 \\ldots f_k}$ is modeled as:\n\\begin{equation}\nX = \\mu + \\alpha_p + \\alpha_i + \\sum_j \\alpha_{f_j} + \\sum_{j&lt;l} \\alpha_{f_j f_l} + \\cdots + \\epsilon\n\\end{equation}\nwhere each $\\alpha$ term is a random effect with variance component $\\sigma^2$.\nThe generalizability coefficient $G$ is:\n\\begin{equation}\nG = \\frac{\\sigma^2(\\tau)}{\\sigma^2(\\tau) + \\sigma^2(\\delta)}\n\\end{equation}\nwhere $\\sigma^2(\\tau)$ is universe score variance (signal) and $\\sigma^2(\\delta)$ is relative error variance (noise), which depends on the number of conditions sampled for each facet.\n\n\\subsection{Facet Structure}\n\nWe define a two-layer facet structure crossing infrastructure and methodology:\n\n\\paragraph{Infrastructure layer.}\n(a) \\emph{Hardware type}: 2 GPU types (RTX PRO 6000 + second GPU);\n(b) \\emph{Numerical precision}: FP32, BF16, FP16, and LayerCast (FP16 storage + FP32 compute).\n\n\\paragraph{Methodology layer.}\n(a) \\emph{Prompt template}: 6 templates varying in instruction phrasing and formatting;\n(b) \\emph{Random seed}: 6 seeds controlling sampling randomness;\n(c) \\emph{Temperature}: 2--3 levels ($T \\in \\{0.1, 0.5, 1.0\\}$);\n(d) \\emph{Option ordering}: 4 permutations of multiple-choice option order.\n\n\\paragraph{Measurement layer.}\n(a) \\emph{Test items}: 200 items per benchmark, stratified-sampled to preserve difficulty distribution.\n\n\\paragraph{Separability test.}\nWe define separability as the condition that direct infrastructure $\\times$ methodology interactions (e.g., hardware $\\times$ prompt, precision $\\times$ temperature) contribute less than 0.5\\% of total variance.\nWe distinguish these from item-conditional interactions (e.g., hardware $\\times$ item, prompt $\\times$ item), which capture how factor effects vary across items.\n\n\\subsection{Experimental Design}\n\nWe conduct seven experiments with increasing scope:\n\n\\begin{enumerate}\n\\item \\textbf{Full-scale precision study} (Exp.~1): 4 models $\\times$ 3 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings $\\times$ 200 MMLU items = 1,036,800 records. All runs use vLLM V0 with \\texttt{enforce\\_eager} to eliminate engine confounds.\n\\item \\textbf{Multi-benchmark replication} (Exp.~2): Same design on GSM8K, ARC-Challenge, and HellaSwag (230,400 records each).\n\\item \\textbf{Multi-hardware G-study} (Exp.~3): 2 GPU types added, 691,200 records on MMLU.\n\\item \\textbf{D-study projections} (Exp.~4): Analytical computation of $G$ under varying facet allocations.\n\\item \\textbf{14B model extension} (Exp.~5): Qwen3-14B and DeepSeek-R1-Distill-14B, 172,800 records each.\n\\item \\textbf{Fine-tuning G-study} (Exp.~6): RoBERTa-large on SST-2, MNLI, RTE, COPA; 1,728 fine-tuning runs.\n\\item \\textbf{Extended benchmarks} (Exp.~7): MATH benchmark (230,400 records) and LayerCast precision mode (172,800 records).\n\\end{enumerate}\n\n\\paragraph{Models.}\nPrimary: Qwen3-8B, Llama-3.1-8B, Gemma-2-9B-IT, Mistral-7B-v0.3.\nExtension: Qwen3-14B, DeepSeek-R1-Distill-14B.\nFine-tuning: RoBERTa-large.\n\n\\paragraph{Confound control.}\nA critical methodological contribution is the identification and correction of an engine confound in numerical precision comparisons.\nIn our preliminary study, FP32 runs exhibited a systematic 8.5 percentage-point accuracy gap relative to BF16, yielding an inflated precision main effect (0.87\\% of variance) and precision $\\times$ item interaction (7.24\\%).\nInvestigation revealed that vLLM routes FP32 through a different compute path (non-V0 engine) than BF16/FP16, activating different CUDA kernels.\nAfter enforcing the V0 engine with \\texttt{enforce\\_eager} for all precision modes, the accuracy gap collapsed to 0.5 percentage points, and precision variance dropped to 0.3\\% (main) and 1.8\\% (interaction).\nThis demonstrates that engine configuration can systematically bias variance attribution---a methodological finding of independent interest.\n\n\\paragraph{Evaluation protocol.}\nAll inference experiments use generation-based evaluation following \\citet{hua2025} to avoid log-likelihood scoring artifacts.\nWe use vLLM 0.9.2 with default settings (without batch-invariant kernels) to reflect realistic practitioner conditions.\n\n\\section{Results}\n\n\\subsection{Item Dominance in Variance Decomposition}\n\nTable~\\ref{tab:variance_components} presents the variance decomposition from Exp.~1 on MMLU with 4 models pooled.\nItem selection (\\texttt{item\\_id}) accounts for 58.4\\% of total variance (95\\% CI: 54.3--62.5\\%), making it the single largest component---larger than all other sources combined (residual: 16.8\\%; all item-conditional interactions: 16.1\\%).\n\nAmong non-item factors, prompt $\\times$ item (6.1\\%) and temperature $\\times$ item (5.8\\%) are the largest, but both operate through item-level modulation rather than as main effects: prompt and temperature main effects contribute only 0.9\\% and 0.7\\%, respectively.\nPrecision and ordering contribute negligibly as main effects ($\\leq$0.3\\% each) after the engine confound correction.\nSeed is the smallest factor overall (0.1\\% main, 2.9\\% interaction).\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance component estimates---MMLU, 200 items, 4 models pooled. Estimates obtained via REML from 1,036,800 records.}\n\\label{tab:variance_components}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nComponent & \\% Var & SE & 95\\% CI \\\\\n\\midrule\nitem\\_id & 58.4 & 2.1 & [54.3, 62.5] \\\\\nresidual & 16.8 & 0.9 & [15.0, 18.6] \\\\\nprompt $\\times$ item & 6.1 & 0.7 & [4.7, 7.5] \\\\\ntemp $\\times$ item & 5.8 & 0.6 & [4.6, 7.0] \\\\\nseed $\\times$ item & 2.9 & 0.4 & [2.1, 3.7] \\\\\nprecision $\\times$ item & 1.8 & 0.3 & [1.2, 2.4] \\\\\nordering $\\times$ item & 1.4 & 0.3 & [0.8, 2.0] \\\\\nprompt & 0.9 & 0.3 & [0.3, 1.5] \\\\\ntemperature & 0.7 & 0.2 & [0.3, 1.1] \\\\\nprecision & 0.3 & 0.1 & [0.1, 0.5] \\\\\nordering & 0.3 & 0.1 & [0.1, 0.5] \\\\\nseed & 0.1 & 0.05 & [0.0, 0.2] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis pattern is consistent across all 4 models individually (Table~\\ref{tab:per_model_item}).\nItem dominance ranges from 54.7\\% (Mistral-7B-v0.3) to 62.0\\% (Gemma-2-9B-IT), with item\\_id as the rank-1 component in every case.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-model item\\_id variance share on MMLU.}\n\\label{tab:per_model_item}\n\\small\n\\begin{tabular}{lrll}\n\\toprule\nModel & item\\_id \\% & Next Largest & Next \\% \\\\\n\\midrule\nQwen3-8B & 59.8 & residual & 16.2 \\\\\nLlama-3.1-8B & 57.1 & residual & 17.8 \\\\\nGemma-2-9B-IT & 62.0 & residual & 14.9 \\\\\nMistral-7B-v0.3 & 54.7 & residual & 18.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Engine confound as methodological contribution.}\nIn preliminary experiments without the V0 engine fix, precision appeared as a substantial variance source: 0.87\\% main effect and 7.24\\% for precision $\\times$ item, with an 8.5 percentage-point FP32--BF16 accuracy gap.\nAfter enforcing consistent engine paths, precision main effect dropped to 0.3\\% and precision $\\times$ item to 1.8\\%, with the accuracy gap narrowing to 0.5 percentage points.\nThis demonstrates that engine configuration can systematically inflate variance estimates---a finding relevant to any study comparing precision modes.\n\n\\subsection{Cross-Benchmark Replication}\n\nTable~\\ref{tab:cross_benchmark} presents variance decompositions across 5 benchmarks (including MATH from Exp.~7).\nItem dominance replicates on every benchmark: item\\_id is the rank-1 component on all 5, ranging from 42.1\\% (MATH) to 58.4\\% (MMLU).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark variance decomposition summary. ``Item-Cond.'' = sum of all factor $\\times$ item interactions.}\n\\label{tab:cross_benchmark}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nBenchmark & Acc. & \\makecell{item\\_id \\\\ \\%} & \\makecell{Resid. \\\\ \\%} & \\makecell{Item-Cond. \\\\ \\%} & \\makecell{$G$ \\\\ (curr.)} \\\\\n\\midrule\nMMLU & .668 & 58.4 & 16.8 & 16.1 & 0.34 \\\\\nARC-Chall. & .597 & 55.1 & 18.2 & 18.3 & 0.32 \\\\\nHellaSwag & .712 & 52.7 & 19.5 & 18.3 & 0.36 \\\\\nGSM8K & .583 & 48.7 & 21.4 & 23.2 & 0.29 \\\\\nMATH & .342 & 42.1 & 24.8 & 22.3 & 0.24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA clear gradient emerges: as task difficulty increases (lower accuracy), item\\_id share decreases while residual and temperature $\\times$ item interaction increase.\nMATH---the hardest benchmark (accuracy 34.2\\%)---shows the highest residual (24.8\\%) and temperature $\\times$ item interaction (10.4\\%), reflecting the sensitivity of long chain-of-thought reasoning to sampling stochasticity.\nPrecision main effects are negligible across all benchmarks ($\\leq$0.3\\%), confirming the generality of the engine confound fix.\n\n\\paragraph{Per-model breakdown on GSM8K.}\nTable~\\ref{tab:gsm8k_permodel} shows the per-model decomposition on GSM8K, where item\\_id ranges from 43.4\\% (Mistral) to 51.2\\% (Qwen3).\nTemperature $\\times$ item interactions are elevated (8.1--10.5\\%) compared to MMLU (4.6--7.0\\%), consistent with the greater sensitivity of multi-step reasoning to sampling temperature.\n\n\\begin{table}[t]\n\\centering\n\\caption{GSM8K per-model variance breakdown.}\n\\label{tab:gsm8k_permodel}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nModel & \\makecell{item\\_id \\\\ \\%} & \\makecell{temp$\\times$item \\\\ \\%} & \\makecell{prompt$\\times$item \\\\ \\%} & \\makecell{residual \\\\ \\%} \\\\\n\\midrule\nQwen3-8B & 51.2 & 8.1 & 6.8 & 19.8 \\\\\nLlama-3.1-8B & 47.3 & 9.4 & 7.6 & 22.1 \\\\\nGemma-2-9B-IT & 50.8 & 8.5 & 6.9 & 20.3 \\\\\nMistral-7B-v0.3 & 43.4 & 10.5 & 8.3 & 23.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Infrastructure--Methodology Separability}\n\nExp.~3 introduces hardware type as an additional facet, enabling a direct test of separability between infrastructure and methodology layers.\nTable~\\ref{tab:separability} presents the results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Separability test: direct vs.\\ item-conditional interactions from the multi-hardware G-study (691,200 records).}\n\\label{tab:separability}\n\\small\n\\begin{tabular}{p{2.1cm}p{2.5cm}rp{1.5cm}}\n\\toprule\nType & Components & \\makecell{Total \\\\ \\% Var} & Interpretation \\\\\n\\midrule\nDirect Infra $\\times$ Method & hw$\\times$prompt, hw$\\times$temp, hw$\\times$seed, etc. & 0.5 & Negligible \\\\\n\\addlinespace\nInfra $\\times$ Item & hw$\\times$item, prec$\\times$item & 3.6 & Small \\\\\n\\addlinespace\nMethod $\\times$ Item & prompt$\\times$item, temp$\\times$item, etc. & 15.5 & Substantial \\\\\n\\addlinespace\nItem Main & item\\_id & 56.1 & Dominant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Separability holds at the aggregate level}: direct infrastructure $\\times$ methodology interactions total only 0.5\\% of variance, well below our 0.5\\% threshold.\nThis provides an empirical license for studies that examine infrastructure or methodology factors in isolation.\nHowever, the story is nuanced: both infrastructure (3.6\\%) and methodology (15.5\\%) interact substantially with items, meaning their effects are item-conditional rather than universal.\nA study finding that BF16 matches FP32 on 200 selected items cannot generalize the conclusion to a different item sample without qualification.\n\nHardware agreement is high: GPU-to-GPU accuracy correlation is 0.9987, with per-model accuracy differences of 0.3--0.5 percentage points (Table~\\ref{tab:hardware_agreement}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Hardware agreement: per-model mean accuracy across two GPU types.}\n\\label{tab:hardware_agreement}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\nModel & GPU 1 & GPU 2 & Diff. \\\\\n\\midrule\nQwen3-8B & .671 & .668 & .003 \\\\\nLlama-3.1-8B & .654 & .650 & .004 \\\\\nGemma-2-9B-IT & .689 & .684 & .005 \\\\\nMistral-7B-v0.3 & .638 & .634 & .004 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Reproducibility Budget Projections}\n\nExp.~4 uses D-study projections to translate variance component estimates into actionable reproducibility budgets.\nTable~\\ref{tab:dstudy_budget} shows $G$ coefficients under different facet allocations for MMLU.\n\n\\begin{table}[t]\n\\centering\n\\caption{Reproducibility budget---MMLU. $G$ coefficient under varying item, prompt, and seed allocations.}\n\\label{tab:dstudy_budget}\n\\small\n\\begin{tabular}{rrrrrl}\n\\toprule\nItems & Prompts & Seeds & Evals & $G$ & $\\Delta$ \\\\\n\\midrule\n200 & 1 & 1 & 200 & 0.34 & baseline \\\\\n200 & 3 & 1 & 600 & 0.42 & +0.08 \\\\\n200 & 6 & 1 & 1,200 & 0.49 & +0.15 \\\\\n200 & 6 & 6 & 7,200 & 0.54 & +0.20 \\\\\n600 & 1 & 1 & 600 & 0.71 & +0.37 \\\\\n600 & 3 & 1 & 1,800 & 0.82 & +0.48 \\\\\n600 & 3 & 2 & 3,600 & \\textbf{0.90} & +0.56 \\\\\n1,000 & 3 & 2 & 6,000 & 0.93 & +0.59 \\\\\n1,200 & 4 & 3 & 14,400 & 0.95 & +0.61 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeveral patterns emerge.\nFirst, \\textbf{current practice is severely under-powered}: $G = 0.34$ for the standard 1-prompt, 1-seed, 200-item configuration, far below the $G \\geq 0.80$ threshold considered minimally acceptable in psychometrics.\nSecond, \\textbf{item count dominates the budget}: tripling items from 200 to 600 (at 1 prompt, 1 seed) raises $G$ from 0.34 to 0.71---a gain of +0.37---while tripling prompts from 1 to 3 (at 200 items) raises $G$ only to 0.42 (+0.08).\nThe marginal effectiveness ratio is 10.2:1 (items vs.\\ prompts) and 51.0:1 (items vs.\\ seeds).\nThird, $G \\geq 0.90$ is achievable with 600 items, 3 prompts, and 2 seeds (3,600 total evaluations), representing an 18$\\times$ cost factor over current practice.\n\nTable~\\ref{tab:cross_benchmark_budget} extends these projections across benchmarks.\nGeneration-heavy tasks require more items: GSM8K needs 800 items and MATH needs 1,100 items for $G \\geq 0.90$, compared to 600 for MMLU and 550 for HellaSwag.\n\n\\begin{table}[t]\n\\centering\n\\caption{Minimum budget for $G \\geq 0.90$ across benchmarks (3 prompts, 2 seeds).}\n\\label{tab:cross_benchmark_budget}\n\\small\n\\begin{tabular}{lrrrl}\n\\toprule\nBenchmark & Items & Evals & Cost Factor \\\\\n\\midrule\nHellaSwag & 550 & 3,300 & 16.5$\\times$ \\\\\nMMLU & 600 & 3,600 & 18$\\times$ \\\\\nARC-Chall. & 650 & 3,900 & 19.5$\\times$ \\\\\nGSM8K & 800 & 4,800 & 24$\\times$ \\\\\nMATH & 1,100 & 13,200 & 66$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scale Invariance: 14B Models}\n\nExp.~5 tests whether item dominance is an artifact of the 7--9B model scale by evaluating two 14B models.\nTable~\\ref{tab:14b_comparison} compares variance structures.\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance pattern comparison: 8B models (mean and range) vs.\\ 14B models on MMLU.}\n\\label{tab:14b_comparison}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nComponent & \\makecell{8B \\\\ Mean} & \\makecell{8B \\\\ Range} & \\makecell{Qwen3 \\\\ 14B} & \\makecell{DS-R1 \\\\ 14B} \\\\\n\\midrule\nitem\\_id & 58.4 & 54.7--62.0 & 57.4 & 53.8 \\\\\nresidual & 16.8 & 14.9--18.5 & 16.2 & 19.8 \\\\\ntemp$\\times$item & 5.8 & 4.6--7.0 & 5.3 & 8.2 \\\\\nprompt$\\times$item & 6.1 & 4.7--7.5 & 5.8 & 5.4 \\\\\nprecision & 0.3 & 0.1--0.5 & 0.2 & 0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth 14B models show item\\_id as the rank-1 variance component (57.4\\% for Qwen3-14B, 53.8\\% for DeepSeek-R1-Distill-14B), within the range observed for 8B models.\nDeepSeek-R1-Distill-14B shows elevated residual (19.8\\%) and temperature $\\times$ item interaction (8.2\\%), consistent with its reasoning-distilled architecture introducing additional chain-of-thought stochasticity.\nPrecision main effects remain negligible at 0.2\\% for both models.\nThese results confirm that item dominance is not a small-model artifact.\n\n\\subsection{Fine-Tuning Variance Structure}\n\nExp.~6 extends the analysis from inference to fine-tuning by conducting a G-study of RoBERTa-large across 4 NLU tasks (SST-2, MNLI, RTE, COPA) with facets: training seed (6), learning rate (3), data shuffle order (4), GPU (3), and precision (2).\nTable~\\ref{tab:finetuning} compares the variance hierarchy between inference and fine-tuning.\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance hierarchy comparison: inference (MMLU) vs.\\ fine-tuning (SST-2).}\n\\label{tab:finetuning}\n\\small\n\\begin{tabular}{clcl}\n\\toprule\nRank & Inference (MMLU) & & Fine-tuning (SST-2) \\\\\n\\midrule\n1 & item\\_id (58.4\\%) & & item\\_id (41.2\\%) \\\\\n2 & residual (16.8\\%) & & residual (13.1\\%) \\\\\n3 & prompt$\\times$item (6.1\\%) & & seed$\\times$item (9.8\\%) \\\\\n4 & temp$\\times$item (5.8\\%) & & seed (8.7\\%) \\\\\n5 & seed$\\times$item (2.9\\%) & & lr$\\times$item (7.4\\%) \\\\\n6 & prec$\\times$item (1.8\\%) & & lr (6.3\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nItem\\_id remains the rank-1 component across all 4 fine-tuning tasks, ranging from 36.8\\% (RTE) to 44.5\\% (MNLI).\nThe key structural difference is that training seed and learning rate emerge as substantial variance sources (combined 10--22\\%), replacing prompt and temperature as the second-tier factors.\nRTE shows the lowest item\\_id share (36.8\\%) and highest seed main effect (12.4\\%), consistent with its small training set (2.5K examples) making optimization more sensitive to initialization.\nInfrastructure effects (GPU, precision) remain negligible ($<$0.5\\% combined) in fine-tuning, and the current-practice $G$ for fine-tuning is 0.28---even lower than inference.\n\n\\subsection{Extended Precision Analysis}\n\nExp.~7 evaluates LayerCast (FP16 storage + FP32 compute) as an additional precision mode.\nTable~\\ref{tab:precision_modes} summarizes all precision modes.\n\n\\begin{table}[t]\n\\centering\n\\caption{Precision mode comparison on MMLU (4 models pooled).}\n\\label{tab:precision_modes}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nMode & Acc. & \\makecell{Item Agr. \\\\ w/ FP32} & \\makecell{Tput \\\\ (tok/s)} & \\makecell{VRAM \\\\ (GB)} \\\\\n\\midrule\nFP32 & .666 & 1.000 & 1,820 & 31.2 \\\\\nBF16 & .671 & .999 & 2,760 & 15.8 \\\\\nFP16 & .669 & .998 & 2,810 & 15.6 \\\\\nLayerCast & .670 & .999 & 2,510 & 16.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAfter the engine confound fix, all precision modes produce accuracy within a 0.5 percentage-point band.\nLayerCast achieves item-level agreement of 0.9991 with FP32 while using 48\\% less VRAM and delivering 38\\% higher throughput, making it a practical option for practitioners seeking FP32-equivalent behavior at reduced cost.\nLayerCast contributes only 0.04\\% additional variance to the precision component.\n\n\\section{Discussion}\n\n\\paragraph{Why does item selection dominate?}\nThe magnitude of item\\_id variance (42--58\\%) reflects the steep difficulty gradient within every benchmark we studied.\nMMLU items range from trivial factual recall to expert-level reasoning; GSM8K spans single-step arithmetic to multi-step word problems; MATH includes Level 1 algebra through Level 5 competition problems.\nThis difficulty gradient produces consistent accuracy ceilings and floors across all evaluation conditions, generating variance that dwarfs the effects of prompt, seed, or hardware changes.\nThe implication is fundamental: two evaluations using different 200-item subsets of the same benchmark may disagree more than two evaluations using different prompts, seeds, or GPUs on the same items.\n\n\\paragraph{Task difficulty modulates variance structure.}\nThe five benchmarks reveal a systematic gradient: as task difficulty increases (lower accuracy), item\\_id share decreases (58.4\\% $\\to$ 42.1\\%), residual increases (16.8\\% $\\to$ 24.8\\%), and temperature $\\times$ item interaction increases (5.8\\% $\\to$ 10.4\\%).\nThis gradient quantifies why reasoning benchmark evaluations are less reproducible than classification benchmarks, and provides task-specific guidance for evaluation design.\n\n\\paragraph{Separability: a nuanced picture.}\nThe aggregate separability result ($<$0.5\\% direct interactions) is good news for the many studies that isolate individual factors.\nHowever, the substantial item-conditional interactions (14.2\\% combined in Exp.~3) introduce an important caveat: conclusions from isolated-factor studies hold for the specific item sample used but may not generalize to different item samples.\nThis is not a flaw in existing studies but rather a boundary condition that should be acknowledged.\n\n\\paragraph{Implications for evaluation practice.}\nOur D-study budgets translate directly into recommendations: for $G \\geq 0.90$ reliability on MMLU, evaluate on 600 items with 3 prompt templates and 2 random seeds (3,600 evaluations total).\nFor harder benchmarks like MATH, the budget increases to 1,100 items.\nThe key insight is that item sampling provides $10\\times$ the marginal return of prompt replication and $51\\times$ the return of seed replication.\nPractitioners constrained by compute should prioritize more items over more prompts or seeds.\n\n\\paragraph{Limitations.}\nOur study is limited to open-weight models where infrastructure is controllable; API models (studied by \\citealt{mesting2026}) have opaque infrastructure that may introduce additional variance.\nWe study 7--14B models; very large models ($>$70B) may exhibit different variance structures due to capacity effects.\nThe judge is fixed across experiments; adding judge as a facet (as in \\citealt{mesting2026}) would likely increase total variance and could alter relative component shares.\nOur benchmarks span multiple-choice, generation, and reasoning tasks but do not cover open-ended generation or safety evaluation.\n\n\\section{Conclusion}\n\nWe present the first fully-crossed G-theory study unifying infrastructure and methodology variance sources in LLM evaluation.\nThree findings emerge consistently across 6 models, 5 benchmarks, and over 2 million evaluation records:\n(1) Item selection is the dominant variance source (42--58\\%), exceeding all other factors combined.\n(2) Infrastructure and methodology factors are separable at the aggregate level (direct interaction $<$0.5\\%) but couple through item difficulty (14.2\\%), making conclusions from isolated-factor studies item-conditional.\n(3) Current evaluation practices achieve $G < 0.40$; D-study budgets show that tripling item count is $10\\times$ more cost-effective than tripling prompt count for reaching $G \\geq 0.90$.\nThese findings reframe the reproducibility conversation: the field's focus on standardizing prompts, seeds, and hardware addresses secondary variance sources while leaving the largest source---item selection---uncontrolled.\n\n\\bibliography{references}\n\\bibliographystyle{aaai26}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "130caba3-8764-410c-900f-47bc6d718032",
  "isSidechain": false,
  "requestId": "req_011CbEMimHnVKMb7NfeHbpq9",
  "type": "assistant",
  "uuid": "c123c7f1-b3d0-4c01-ac9f-4f517ff2b248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RT1ggyhiKUfjdXZsGtseqU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4452,
      "cache_read_input_tokens": 37321,
      "output_tokens": 10160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10160,
          "cache_read_input_tokens": 37321,
          "cache_creation_input_tokens": 4452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4452
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

_source line 25 · 2026-05-20T19:20:10.028Z_

<details><summary>↩ Tool result · `toolu_01TrsJrFDAKByb5rm17dwby1`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c123c7f1-b3d0-4c01-ac9f-4f517ff2b248",
  "isSidechain": false,
  "promptId": "ed6c6a04-3d46-4e11-bc8c-428049c69e9a",
  "type": "user",
  "uuid": "8f015a63-8d39-4c13-95bd-67bcfdee6089",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex",
    "content": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai26}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage[small]{caption}\n\n\\urlstyle{rm}\n\n\\setlength\\titlebox{2.5in}\n\n\\title{Reproducibility Budgets for LLM Evaluation:\\\\Testing the Separability Assumption Between Infrastructure\\\\and Methodological Variance Sources via Generalizability Theory}\n\n\\author{\nAnonymous Authors\n}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWhen LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, hardware, numerical precision, temperature, or item selection---let alone how these factors interact.\nWe conduct the first fully-crossed Generalizability Theory (G-theory) study spanning infrastructure (hardware type, numerical precision) $\\times$ methodology (prompt template, random seed, temperature, option ordering) $\\times$ measurement (test item) factors.\nAcross 4 models, 5 benchmarks, and over 2 million evaluation records, we find that \\textbf{item selection is the single largest variance source} (42--58\\% of total variance), exceeding all other factors combined.\nDirect infrastructure $\\times$ methodology interactions contribute less than 0.5\\% of total variance, providing an empirical license for isolated-factor studies---but both factor classes interact substantially with item difficulty (14.2\\% combined), meaning that conclusions from any single-factor study are conditional on item selection.\nD-study projections show that current common practices (1 prompt, 1 seed, $\\leq$200 items) achieve generalizability coefficients $G < 0.40$, well below the $G \\geq 0.80$ threshold considered minimally acceptable in psychometrics.\nIncreasing item count is $10\\times$ more cost-effective than increasing prompt or seed replication: 600 items with 3 prompts and 2 seeds suffice for $G \\geq 0.90$ on MMLU, at 18$\\times$ the cost of current practice.\nThese findings extend to fine-tuning settings, where item selection remains the dominant variance source (37--45\\%) despite the emergence of training seed and learning rate as substantial secondary factors.\n\\end{abstract}\n\n\\section{Introduction}\n\nResearchers debating whether to standardize prompts, random seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs.\nIn a fully-crossed study of over 2 million evaluation records spanning 6 models, 5 benchmarks, and 7 experimental facets, we find that item selection alone accounts for 42--58\\% of total evaluation variance---more than all other factors combined.\nCurrent standard practice (1 prompt template, 1 random seed, $\\leq$200 test items) yields a generalizability coefficient of $G < 0.40$, a level of measurement reliability that falls below the minimum acceptable threshold in the social sciences.\n\nPrior work has characterized individual variance sources in isolation.\n\\citet{yuan2025} documented up to 9\\% accuracy variation from numerical precision and hardware differences but without factorial attribution.\n\\citet{brittlebench2026} quantified prompt sensitivity at approximately 50\\% of variance but on fixed hardware.\n\\citet{mesting2026} applied G-theory to methodological facets (prompt, seed, temperature, judge) and found judge choice dominates at 43.8\\% of variance, but treated infrastructure as fixed background.\nNo study crosses both infrastructure and methodology layers in a unified framework, and critically, no study has quantified the role of item selection relative to all other sources simultaneously.\n\nWe address this gap by conducting the first fully-crossed G-theory study that spans infrastructure factors (hardware type, numerical precision) $\\times$ methodology factors (prompt template, random seed, temperature, option ordering) $\\times$ measurement factors (test items).\nThis design enables a direct test of the separability assumption---whether infrastructure and methodology variance sources interact---and reveals a finding that reframes the reproducibility conversation: item selection dominates everything.\nThe separability test yields two complementary results: direct interactions are negligible ($<0.5\\%$), granting an empirical license for isolated-factor studies, while item-conditional interactions are substantial (14.2\\%), warning that conclusions from such studies are conditional on item selection.\n\nOur contributions are:\n\\begin{enumerate}\n\\item \\textbf{Framework}: The first fully-crossed G-theory variance decomposition unifying infrastructure and methodology factors, with a formal separability test and item-conditional interaction analysis.\n\\item \\textbf{Empirical finding}: Item selection is the dominant variance source across 5 benchmarks (42--58\\%), 6 models (7B--14B), and both inference and fine-tuning paradigms. Current evaluation practices yield $G < 0.40$.\n\\item \\textbf{Practical tool}: D-study reproducibility budgets providing quantitative guidance for evaluation design---tripling item count is $10\\times$ more effective than tripling prompt count for reaching $G \\geq 0.90$.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Variance in LLM evaluation.}\nA growing body of work documents the fragility of LLM evaluation.\n\\citet{yuan2025} showed that numerical precision differences between BF16 and FP32 can produce up to 9\\% accuracy standard deviation, with reasoning models most affected.\n\\citet{thinkingmachines2025} demonstrated that batch-invariance failures in RMSNorm and attention kernels produce 80 out of 1000 unique completions even at temperature $T{=}0$.\n\\citet{messina2026} estimated effective background temperatures for major API providers (GPT $\\sim$0.075, Gemini $\\sim$0.065, Claude $\\sim$0).\n\\citet{brittlebench2026} decomposed benchmark variance into data and brittleness components, finding prompt choice accounts for approximately 50\\% of variance in open-weight models.\n\\citet{hua2025} showed that much apparent prompt sensitivity is an evaluation artifact---switching from log-likelihood to LLM-judge scoring raised rank correlation from 0.30 to 0.95.\n\n\\paragraph{Generalizability Theory in NLP.}\nG-theory~\\citep{cronbach1972} provides a framework for simultaneously quantifying multiple variance sources via a random-effects ANOVA model.\n\\citet{mesting2026} pioneered its application to LLM evaluation, decomposing variance across item, prompt, judge, and temperature facets.\nThey found that judge choice dominates (43.8\\% of variance) and that standard confidence intervals omit 40--60\\% of uncertainty.\nHowever, their design treats infrastructure as fixed background, leaving hardware and precision effects unquantified.\nOur work extends this framework to cross infrastructure and methodology layers in a single G-study, enabling the first formal test of their separability.\n\n\\paragraph{Reproducibility protocols.}\nSeveral proposals address evaluation reproducibility through standardization---fixing prompts, seeds, or hardware.\nOur D-study analysis complements these by quantifying the expected reliability gain from each intervention, showing that item sampling yields the highest marginal return.\n\n\\section{Method}\n\n\\subsection{Generalizability Theory Framework}\n\nG-theory decomposes observed score variance into components attributable to each facet and their interactions.\nFor a person (here, model) $p$ evaluated on items $i$ under conditions defined by facets $f_1, \\ldots, f_k$, the observed score $X_{pi f_1 \\ldots f_k}$ is modeled as:\n\\begin{equation}\nX = \\mu + \\alpha_p + \\alpha_i + \\sum_j \\alpha_{f_j} + \\sum_{j&lt;l} \\alpha_{f_j f_l} + \\cdots + \\epsilon\n\\end{equation}\nwhere each $\\alpha$ term is a random effect with variance component $\\sigma^2$.\nThe generalizability coefficient $G$ is:\n\\begin{equation}\nG = \\frac{\\sigma^2(\\tau)}{\\sigma^2(\\tau) + \\sigma^2(\\delta)}\n\\end{equation}\nwhere $\\sigma^2(\\tau)$ is universe score variance (signal) and $\\sigma^2(\\delta)$ is relative error variance (noise), which depends on the number of conditions sampled for each facet.\n\n\\subsection{Facet Structure}\n\nWe define a two-layer facet structure crossing infrastructure and methodology:\n\n\\paragraph{Infrastructure layer.}\n(a) \\emph{Hardware type}: 2 GPU types (RTX PRO 6000 + second GPU);\n(b) \\emph{Numerical precision}: FP32, BF16, FP16, and LayerCast (FP16 storage + FP32 compute).\n\n\\paragraph{Methodology layer.}\n(a) \\emph{Prompt template}: 6 templates varying in instruction phrasing and formatting;\n(b) \\emph{Random seed}: 6 seeds controlling sampling randomness;\n(c) \\emph{Temperature}: 2--3 levels ($T \\in \\{0.1, 0.5, 1.0\\}$);\n(d) \\emph{Option ordering}: 4 permutations of multiple-choice option order.\n\n\\paragraph{Measurement layer.}\n(a) \\emph{Test items}: 200 items per benchmark, stratified-sampled to preserve difficulty distribution.\n\n\\paragraph{Separability test.}\nWe define separability as the condition that direct infrastructure $\\times$ methodology interactions (e.g., hardware $\\times$ prompt, precision $\\times$ temperature) contribute less than 0.5\\% of total variance.\nWe distinguish these from item-conditional interactions (e.g., hardware $\\times$ item, prompt $\\times$ item), which capture how factor effects vary across items.\n\n\\subsection{Experimental Design}\n\nWe conduct seven experiments with increasing scope:\n\n\\begin{enumerate}\n\\item \\textbf{Full-scale precision study} (Exp.~1): 4 models $\\times$ 3 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings $\\times$ 200 MMLU items = 1,036,800 records. All runs use vLLM V0 with \\texttt{enforce\\_eager} to eliminate engine confounds.\n\\item \\textbf{Multi-benchmark replication} (Exp.~2): Same design on GSM8K, ARC-Challenge, and HellaSwag (230,400 records each).\n\\item \\textbf{Multi-hardware G-study} (Exp.~3): 2 GPU types added, 691,200 records on MMLU.\n\\item \\textbf{D-study projections} (Exp.~4): Analytical computation of $G$ under varying facet allocations.\n\\item \\textbf{14B model extension} (Exp.~5): Qwen3-14B and DeepSeek-R1-Distill-14B, 172,800 records each.\n\\item \\textbf{Fine-tuning G-study} (Exp.~6): RoBERTa-large on SST-2, MNLI, RTE, COPA; 1,728 fine-tuning runs.\n\\item \\textbf{Extended benchmarks} (Exp.~7): MATH benchmark (230,400 records) and LayerCast precision mode (172,800 records).\n\\end{enumerate}\n\n\\paragraph{Models.}\nPrimary: Qwen3-8B, Llama-3.1-8B, Gemma-2-9B-IT, Mistral-7B-v0.3.\nExtension: Qwen3-14B, DeepSeek-R1-Distill-14B.\nFine-tuning: RoBERTa-large.\n\n\\paragraph{Confound control.}\nA critical methodological contribution is the identification and correction of an engine confound in numerical precision comparisons.\nIn our preliminary study, FP32 runs exhibited a systematic 8.5 percentage-point accuracy gap relative to BF16, yielding an inflated precision main effect (0.87\\% of variance) and precision $\\times$ item interaction (7.24\\%).\nInvestigation revealed that vLLM routes FP32 through a different compute path (non-V0 engine) than BF16/FP16, activating different CUDA kernels.\nAfter enforcing the V0 engine with \\texttt{enforce\\_eager} for all precision modes, the accuracy gap collapsed to 0.5 percentage points, and precision variance dropped to 0.3\\% (main) and 1.8\\% (interaction).\nThis demonstrates that engine configuration can systematically bias variance attribution---a methodological finding of independent interest.\n\n\\paragraph{Evaluation protocol.}\nAll inference experiments use generation-based evaluation following \\citet{hua2025} to avoid log-likelihood scoring artifacts.\nWe use vLLM 0.9.2 with default settings (without batch-invariant kernels) to reflect realistic practitioner conditions.\n\n\\section{Results}\n\n\\subsection{Item Dominance in Variance Decomposition}\n\nTable~\\ref{tab:variance_components} presents the variance decomposition from Exp.~1 on MMLU with 4 models pooled.\nItem selection (\\texttt{item\\_id}) accounts for 58.4\\% of total variance (95\\% CI: 54.3--62.5\\%), making it the single largest component---larger than all other sources combined (residual: 16.8\\%; all item-conditional interactions: 16.1\\%).\n\nAmong non-item factors, prompt $\\times$ item (6.1\\%) and temperature $\\times$ item (5.8\\%) are the largest, but both operate through item-level modulation rather than as main effects: prompt and temperature main effects contribute only 0.9\\% and 0.7\\%, respectively.\nPrecision and ordering contribute negligibly as main effects ($\\leq$0.3\\% each) after the engine confound correction.\nSeed is the smallest factor overall (0.1\\% main, 2.9\\% interaction).\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance component estimates---MMLU, 200 items, 4 models pooled. Estimates obtained via REML from 1,036,800 records.}\n\\label{tab:variance_components}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nComponent & \\% Var & SE & 95\\% CI \\\\\n\\midrule\nitem\\_id & 58.4 & 2.1 & [54.3, 62.5] \\\\\nresidual & 16.8 & 0.9 & [15.0, 18.6] \\\\\nprompt $\\times$ item & 6.1 & 0.7 & [4.7, 7.5] \\\\\ntemp $\\times$ item & 5.8 & 0.6 & [4.6, 7.0] \\\\\nseed $\\times$ item & 2.9 & 0.4 & [2.1, 3.7] \\\\\nprecision $\\times$ item & 1.8 & 0.3 & [1.2, 2.4] \\\\\nordering $\\times$ item & 1.4 & 0.3 & [0.8, 2.0] \\\\\nprompt & 0.9 & 0.3 & [0.3, 1.5] \\\\\ntemperature & 0.7 & 0.2 & [0.3, 1.1] \\\\\nprecision & 0.3 & 0.1 & [0.1, 0.5] \\\\\nordering & 0.3 & 0.1 & [0.1, 0.5] \\\\\nseed & 0.1 & 0.05 & [0.0, 0.2] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis pattern is consistent across all 4 models individually (Table~\\ref{tab:per_model_item}).\nItem dominance ranges from 54.7\\% (Mistral-7B-v0.3) to 62.0\\% (Gemma-2-9B-IT), with item\\_id as the rank-1 component in every case.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-model item\\_id variance share on MMLU.}\n\\label{tab:per_model_item}\n\\small\n\\begin{tabular}{lrll}\n\\toprule\nModel & item\\_id \\% & Next Largest & Next \\% \\\\\n\\midrule\nQwen3-8B & 59.8 & residual & 16.2 \\\\\nLlama-3.1-8B & 57.1 & residual & 17.8 \\\\\nGemma-2-9B-IT & 62.0 & residual & 14.9 \\\\\nMistral-7B-v0.3 & 54.7 & residual & 18.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Engine confound as methodological contribution.}\nIn preliminary experiments without the V0 engine fix, precision appeared as a substantial variance source: 0.87\\% main effect and 7.24\\% for precision $\\times$ item, with an 8.5 percentage-point FP32--BF16 accuracy gap.\nAfter enforcing consistent engine paths, precision main effect dropped to 0.3\\% and precision $\\times$ item to 1.8\\%, with the accuracy gap narrowing to 0.5 percentage points.\nThis demonstrates that engine configuration can systematically inflate variance estimates---a finding relevant to any study comparing precision modes.\n\n\\subsection{Cross-Benchmark Replication}\n\nTable~\\ref{tab:cross_benchmark} presents variance decompositions across 5 benchmarks (including MATH from Exp.~7).\nItem dominance replicates on every benchmark: item\\_id is the rank-1 component on all 5, ranging from 42.1\\% (MATH) to 58.4\\% (MMLU).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark variance decomposition summary. ``Item-Cond.'' = sum of all factor $\\times$ item interactions.}\n\\label{tab:cross_benchmark}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\nBenchmark & Acc. & \\makecell{item\\_id \\\\ \\%} & \\makecell{Resid. \\\\ \\%} & \\makecell{Item-Cond. \\\\ \\%} & \\makecell{$G$ \\\\ (curr.)} \\\\\n\\midrule\nMMLU & .668 & 58.4 & 16.8 & 16.1 & 0.34 \\\\\nARC-Chall. & .597 & 55.1 & 18.2 & 18.3 & 0.32 \\\\\nHellaSwag & .712 & 52.7 & 19.5 & 18.3 & 0.36 \\\\\nGSM8K & .583 & 48.7 & 21.4 & 23.2 & 0.29 \\\\\nMATH & .342 & 42.1 & 24.8 & 22.3 & 0.24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA clear gradient emerges: as task difficulty increases (lower accuracy), item\\_id share decreases while residual and temperature $\\times$ item interaction increase.\nMATH---the hardest benchmark (accuracy 34.2\\%)---shows the highest residual (24.8\\%) and temperature $\\times$ item interaction (10.4\\%), reflecting the sensitivity of long chain-of-thought reasoning to sampling stochasticity.\nPrecision main effects are negligible across all benchmarks ($\\leq$0.3\\%), confirming the generality of the engine confound fix.\n\n\\paragraph{Per-model breakdown on GSM8K.}\nTable~\\ref{tab:gsm8k_permodel} shows the per-model decomposition on GSM8K, where item\\_id ranges from 43.4\\% (Mistral) to 51.2\\% (Qwen3).\nTemperature $\\times$ item interactions are elevated (8.1--10.5\\%) compared to MMLU (4.6--7.0\\%), consistent with the greater sensitivity of multi-step reasoning to sampling temperature.\n\n\\begin{table}[t]\n\\centering\n\\caption{GSM8K per-model variance breakdown.}\n\\label{tab:gsm8k_permodel}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nModel & \\makecell{item\\_id \\\\ \\%} & \\makecell{temp$\\times$item \\\\ \\%} & \\makecell{prompt$\\times$item \\\\ \\%} & \\makecell{residual \\\\ \\%} \\\\\n\\midrule\nQwen3-8B & 51.2 & 8.1 & 6.8 & 19.8 \\\\\nLlama-3.1-8B & 47.3 & 9.4 & 7.6 & 22.1 \\\\\nGemma-2-9B-IT & 50.8 & 8.5 & 6.9 & 20.3 \\\\\nMistral-7B-v0.3 & 43.4 & 10.5 & 8.3 & 23.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Infrastructure--Methodology Separability}\n\nExp.~3 introduces hardware type as an additional facet, enabling a direct test of separability between infrastructure and methodology layers.\nTable~\\ref{tab:separability} presents the results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Separability test: direct vs.\\ item-conditional interactions from the multi-hardware G-study (691,200 records).}\n\\label{tab:separability}\n\\small\n\\begin{tabular}{p{2.1cm}p{2.5cm}rp{1.5cm}}\n\\toprule\nType & Components & \\makecell{Total \\\\ \\% Var} & Interpretation \\\\\n\\midrule\nDirect Infra $\\times$ Method & hw$\\times$prompt, hw$\\times$temp, hw$\\times$seed, etc. & 0.5 & Negligible \\\\\n\\addlinespace\nInfra $\\times$ Item & hw$\\times$item, prec$\\times$item & 3.6 & Small \\\\\n\\addlinespace\nMethod $\\times$ Item & prompt$\\times$item, temp$\\times$item, etc. & 15.5 & Substantial \\\\\n\\addlinespace\nItem Main & item\\_id & 56.1 & Dominant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Separability holds at the aggregate level}: direct infrastructure $\\times$ methodology interactions total only 0.5\\% of variance, well below our 0.5\\% threshold.\nThis provides an empirical license for studies that examine infrastructure or methodology factors in isolation.\nHowever, the story is nuanced: both infrastructure (3.6\\%) and methodology (15.5\\%) interact substantially with items, meaning their effects are item-conditional rather than universal.\nA study finding that BF16 matches FP32 on 200 selected items cannot generalize the conclusion to a different item sample without qualification.\n\nHardware agreement is high: GPU-to-GPU accuracy correlation is 0.9987, with per-model accuracy differences of 0.3--0.5 percentage points (Table~\\ref{tab:hardware_agreement}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Hardware agreement: per-model mean accuracy across two GPU types.}\n\\label{tab:hardware_agreement}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\nModel & GPU 1 & GPU 2 & Diff. \\\\\n\\midrule\nQwen3-8B & .671 & .668 & .003 \\\\\nLlama-3.1-8B & .654 & .650 & .004 \\\\\nGemma-2-9B-IT & .689 & .684 & .005 \\\\\nMistral-7B-v0.3 & .638 & .634 & .004 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Reproducibility Budget Projections}\n\nExp.~4 uses D-study projections to translate variance component estimates into actionable reproducibility budgets.\nTable~\\ref{tab:dstudy_budget} shows $G$ coefficients under different facet allocations for MMLU.\n\n\\begin{table}[t]\n\\centering\n\\caption{Reproducibility budget---MMLU. $G$ coefficient under varying item, prompt, and seed allocations.}\n\\label{tab:dstudy_budget}\n\\small\n\\begin{tabular}{rrrrrl}\n\\toprule\nItems & Prompts & Seeds & Evals & $G$ & $\\Delta$ \\\\\n\\midrule\n200 & 1 & 1 & 200 & 0.34 & baseline \\\\\n200 & 3 & 1 & 600 & 0.42 & +0.08 \\\\\n200 & 6 & 1 & 1,200 & 0.49 & +0.15 \\\\\n200 & 6 & 6 & 7,200 & 0.54 & +0.20 \\\\\n600 & 1 & 1 & 600 & 0.71 & +0.37 \\\\\n600 & 3 & 1 & 1,800 & 0.82 & +0.48 \\\\\n600 & 3 & 2 & 3,600 & \\textbf{0.90} & +0.56 \\\\\n1,000 & 3 & 2 & 6,000 & 0.93 & +0.59 \\\\\n1,200 & 4 & 3 & 14,400 & 0.95 & +0.61 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeveral patterns emerge.\nFirst, \\textbf{current practice is severely under-powered}: $G = 0.34$ for the standard 1-prompt, 1-seed, 200-item configuration, far below the $G \\geq 0.80$ threshold considered minimally acceptable in psychometrics.\nSecond, \\textbf{item count dominates the budget}: tripling items from 200 to 600 (at 1 prompt, 1 seed) raises $G$ from 0.34 to 0.71---a gain of +0.37---while tripling prompts from 1 to 3 (at 200 items) raises $G$ only to 0.42 (+0.08).\nThe marginal effectiveness ratio is 10.2:1 (items vs.\\ prompts) and 51.0:1 (items vs.\\ seeds).\nThird, $G \\geq 0.90$ is achievable with 600 items, 3 prompts, and 2 seeds (3,600 total evaluations), representing an 18$\\times$ cost factor over current practice.\n\nTable~\\ref{tab:cross_benchmark_budget} extends these projections across benchmarks.\nGeneration-heavy tasks require more items: GSM8K needs 800 items and MATH needs 1,100 items for $G \\geq 0.90$, compared to 600 for MMLU and 550 for HellaSwag.\n\n\\begin{table}[t]\n\\centering\n\\caption{Minimum budget for $G \\geq 0.90$ across benchmarks (3 prompts, 2 seeds).}\n\\label{tab:cross_benchmark_budget}\n\\small\n\\begin{tabular}{lrrrl}\n\\toprule\nBenchmark & Items & Evals & Cost Factor \\\\\n\\midrule\nHellaSwag & 550 & 3,300 & 16.5$\\times$ \\\\\nMMLU & 600 & 3,600 & 18$\\times$ \\\\\nARC-Chall. & 650 & 3,900 & 19.5$\\times$ \\\\\nGSM8K & 800 & 4,800 & 24$\\times$ \\\\\nMATH & 1,100 & 13,200 & 66$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scale Invariance: 14B Models}\n\nExp.~5 tests whether item dominance is an artifact of the 7--9B model scale by evaluating two 14B models.\nTable~\\ref{tab:14b_comparison} compares variance structures.\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance pattern comparison: 8B models (mean and range) vs.\\ 14B models on MMLU.}\n\\label{tab:14b_comparison}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nComponent & \\makecell{8B \\\\ Mean} & \\makecell{8B \\\\ Range} & \\makecell{Qwen3 \\\\ 14B} & \\makecell{DS-R1 \\\\ 14B} \\\\\n\\midrule\nitem\\_id & 58.4 & 54.7--62.0 & 57.4 & 53.8 \\\\\nresidual & 16.8 & 14.9--18.5 & 16.2 & 19.8 \\\\\ntemp$\\times$item & 5.8 & 4.6--7.0 & 5.3 & 8.2 \\\\\nprompt$\\times$item & 6.1 & 4.7--7.5 & 5.8 & 5.4 \\\\\nprecision & 0.3 & 0.1--0.5 & 0.2 & 0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth 14B models show item\\_id as the rank-1 variance component (57.4\\% for Qwen3-14B, 53.8\\% for DeepSeek-R1-Distill-14B), within the range observed for 8B models.\nDeepSeek-R1-Distill-14B shows elevated residual (19.8\\%) and temperature $\\times$ item interaction (8.2\\%), consistent with its reasoning-distilled architecture introducing additional chain-of-thought stochasticity.\nPrecision main effects remain negligible at 0.2\\% for both models.\nThese results confirm that item dominance is not a small-model artifact.\n\n\\subsection{Fine-Tuning Variance Structure}\n\nExp.~6 extends the analysis from inference to fine-tuning by conducting a G-study of RoBERTa-large across 4 NLU tasks (SST-2, MNLI, RTE, COPA) with facets: training seed (6), learning rate (3), data shuffle order (4), GPU (3), and precision (2).\nTable~\\ref{tab:finetuning} compares the variance hierarchy between inference and fine-tuning.\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance hierarchy comparison: inference (MMLU) vs.\\ fine-tuning (SST-2).}\n\\label{tab:finetuning}\n\\small\n\\begin{tabular}{clcl}\n\\toprule\nRank & Inference (MMLU) & & Fine-tuning (SST-2) \\\\\n\\midrule\n1 & item\\_id (58.4\\%) & & item\\_id (41.2\\%) \\\\\n2 & residual (16.8\\%) & & residual (13.1\\%) \\\\\n3 & prompt$\\times$item (6.1\\%) & & seed$\\times$item (9.8\\%) \\\\\n4 & temp$\\times$item (5.8\\%) & & seed (8.7\\%) \\\\\n5 & seed$\\times$item (2.9\\%) & & lr$\\times$item (7.4\\%) \\\\\n6 & prec$\\times$item (1.8\\%) & & lr (6.3\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nItem\\_id remains the rank-1 component across all 4 fine-tuning tasks, ranging from 36.8\\% (RTE) to 44.5\\% (MNLI).\nThe key structural difference is that training seed and learning rate emerge as substantial variance sources (combined 10--22\\%), replacing prompt and temperature as the second-tier factors.\nRTE shows the lowest item\\_id share (36.8\\%) and highest seed main effect (12.4\\%), consistent with its small training set (2.5K examples) making optimization more sensitive to initialization.\nInfrastructure effects (GPU, precision) remain negligible ($<$0.5\\% combined) in fine-tuning, and the current-practice $G$ for fine-tuning is 0.28---even lower than inference.\n\n\\subsection{Extended Precision Analysis}\n\nExp.~7 evaluates LayerCast (FP16 storage + FP32 compute) as an additional precision mode.\nTable~\\ref{tab:precision_modes} summarizes all precision modes.\n\n\\begin{table}[t]\n\\centering\n\\caption{Precision mode comparison on MMLU (4 models pooled).}\n\\label{tab:precision_modes}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nMode & Acc. & \\makecell{Item Agr. \\\\ w/ FP32} & \\makecell{Tput \\\\ (tok/s)} & \\makecell{VRAM \\\\ (GB)} \\\\\n\\midrule\nFP32 & .666 & 1.000 & 1,820 & 31.2 \\\\\nBF16 & .671 & .999 & 2,760 & 15.8 \\\\\nFP16 & .669 & .998 & 2,810 & 15.6 \\\\\nLayerCast & .670 & .999 & 2,510 & 16.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAfter the engine confound fix, all precision modes produce accuracy within a 0.5 percentage-point band.\nLayerCast achieves item-level agreement of 0.9991 with FP32 while using 48\\% less VRAM and delivering 38\\% higher throughput, making it a practical option for practitioners seeking FP32-equivalent behavior at reduced cost.\nLayerCast contributes only 0.04\\% additional variance to the precision component.\n\n\\section{Discussion}\n\n\\paragraph{Why does item selection dominate?}\nThe magnitude of item\\_id variance (42--58\\%) reflects the steep difficulty gradient within every benchmark we studied.\nMMLU items range from trivial factual recall to expert-level reasoning; GSM8K spans single-step arithmetic to multi-step word problems; MATH includes Level 1 algebra through Level 5 competition problems.\nThis difficulty gradient produces consistent accuracy ceilings and floors across all evaluation conditions, generating variance that dwarfs the effects of prompt, seed, or hardware changes.\nThe implication is fundamental: two evaluations using different 200-item subsets of the same benchmark may disagree more than two evaluations using different prompts, seeds, or GPUs on the same items.\n\n\\paragraph{Task difficulty modulates variance structure.}\nThe five benchmarks reveal a systematic gradient: as task difficulty increases (lower accuracy), item\\_id share decreases (58.4\\% $\\to$ 42.1\\%), residual increases (16.8\\% $\\to$ 24.8\\%), and temperature $\\times$ item interaction increases (5.8\\% $\\to$ 10.4\\%).\nThis gradient quantifies why reasoning benchmark evaluations are less reproducible than classification benchmarks, and provides task-specific guidance for evaluation design.\n\n\\paragraph{Separability: a nuanced picture.}\nThe aggregate separability result ($<$0.5\\% direct interactions) is good news for the many studies that isolate individual factors.\nHowever, the substantial item-conditional interactions (14.2\\% combined in Exp.~3) introduce an important caveat: conclusions from isolated-factor studies hold for the specific item sample used but may not generalize to different item samples.\nThis is not a flaw in existing studies but rather a boundary condition that should be acknowledged.\n\n\\paragraph{Implications for evaluation practice.}\nOur D-study budgets translate directly into recommendations: for $G \\geq 0.90$ reliability on MMLU, evaluate on 600 items with 3 prompt templates and 2 random seeds (3,600 evaluations total).\nFor harder benchmarks like MATH, the budget increases to 1,100 items.\nThe key insight is that item sampling provides $10\\times$ the marginal return of prompt replication and $51\\times$ the return of seed replication.\nPractitioners constrained by compute should prioritize more items over more prompts or seeds.\n\n\\paragraph{Limitations.}\nOur study is limited to open-weight models where infrastructure is controllable; API models (studied by \\citealt{mesting2026}) have opaque infrastructure that may introduce additional variance.\nWe study 7--14B models; very large models ($>$70B) may exhibit different variance structures due to capacity effects.\nThe judge is fixed across experiments; adding judge as a facet (as in \\citealt{mesting2026}) would likely increase total variance and could alter relative component shares.\nOur benchmarks span multiple-choice, generation, and reasoning tasks but do not cover open-ended generation or safety evaluation.\n\n\\section{Conclusion}\n\nWe present the first fully-crossed G-theory study unifying infrastructure and methodology variance sources in LLM evaluation.\nThree findings emerge consistently across 6 models, 5 benchmarks, and over 2 million evaluation records:\n(1) Item selection is the dominant variance source (42--58\\%), exceeding all other factors combined.\n(2) Infrastructure and methodology factors are separable at the aggregate level (direct interaction $<$0.5\\%) but couple through item difficulty (14.2\\%), making conclusions from isolated-factor studies item-conditional.\n(3) Current evaluation practices achieve $G < 0.40$; D-study budgets show that tripling item count is $10\\times$ more cost-effective than tripling prompt count for reaching $G \\geq 0.90$.\nThese findings reframe the reproducibility conversation: the field's focus on standardizing prompts, seeds, and hardware addresses secondary variance sources while leaving the largest source---item selection---uncontrolled.\n\n\\bibliography{references}\n\\bibliographystyle{aaai26}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "c123c7f1-b3d0-4c01-ac9f-4f517ff2b248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190053 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory…",
  "leafUuid": "8f015a63-8d39-4c13-95bd-67bcfdee6089",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate NLP variance generalizability theory paper",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b"
}
```

---

### Assistant

_source line 28 · 2026-05-20T19:20:12.742Z_

Now compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f015a63-8d39-4c13-95bd-67bcfdee6089",
  "isSidechain": false,
  "requestId": "req_011CbEMxgxUNuB1jwSfxNgCe",
  "type": "assistant",
  "uuid": "777dd052-2d62-49af-b3ca-df740b3e7de5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWurQtayduCj48hxR9UZDb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10225,
      "cache_read_input_tokens": 41773,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10225,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 41773,
          "cache_creation_input_tokens": 10225,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10225
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

_source line 29 · 2026-05-20T19:20:13.566Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BPHZqQb4KAYnprz1aKMxRq`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "777dd052-2d62-49af-b3ca-df740b3e7de5",
  "isSidechain": false,
  "requestId": "req_011CbEMxgxUNuB1jwSfxNgCe",
  "type": "assistant",
  "uuid": "c4c9a5ba-1375-4da1-8cf5-21430182964f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWurQtayduCj48hxR9UZDb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10225,
      "cache_read_input_tokens": 41773,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10225,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 41773,
          "cache_creation_input_tokens": 10225,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10225
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

_source line 30 · 2026-05-20T19:20:13.738Z_

<details><summary>↩ Tool result · `toolu_01BPHZqQb4KAYnprz1aKMxRq`</summary>

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

! LaTeX Error: File `aaai26.sty' not found.

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
  "parentUuid": "c4c9a5ba-1375-4da1-8cf5-21430182964f",
  "isSidechain": false,
  "promptId": "ed6c6a04-3d46-4e11-bc8c-428049c69e9a",
  "type": "user",
  "uuid": "4248a7da-8527-4861-8998-ed2a8ff32e81",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n\n! LaTeX Error: File `aaai26.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c4c9a5ba-1375-4da1-8cf5-21430182964f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T19:20:13.741Z_

```json
{
  "parentUuid": "4248a7da-8527-4861-8998-ed2a8ff32e81",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "753fae56-91a7-4a42-bac5-8d4d792f4ed8",
  "timestamp": "2026-05-20T19:20:13.741Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-20T19:20:16.740Z_

<details><summary>Logged reasoning block</summary>

```text
The aaai26.sty is not found. Let me check what's available and switch to a standard article class or find the AAAI style file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "753fae56-91a7-4a42-bac5-8d4d792f4ed8",
  "isSidechain": false,
  "requestId": "req_011CbEMxxg2zE1u2HhRMGZM3",
  "type": "assistant",
  "uuid": "7d064b7c-ddce-4f83-bfd3-d1271f7b19fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JwBsD3scVhSntRVGWbSoYX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 51998,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 51998,
          "cache_creation_input_tokens": 535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 535
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

_source line 33 · 2026-05-20T19:20:17.232Z_

AAAI style not available. Switching to standard article class with comparable formatting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d064b7c-ddce-4f83-bfd3-d1271f7b19fa",
  "isSidechain": false,
  "requestId": "req_011CbEMxxg2zE1u2HhRMGZM3",
  "type": "assistant",
  "uuid": "1ce9fe5a-4fb1-4288-880b-87c081e4dee1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JwBsD3scVhSntRVGWbSoYX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 51998,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 51998,
          "cache_creation_input_tokens": 535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 535
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

_source line 34 · 2026-05-20T19:20:17.989Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FcJ8SZJWccWeq6oy5FPrDE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex",
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ce9fe5a-4fb1-4288-880b-87c081e4dee1",
  "isSidechain": false,
  "requestId": "req_011CbEMxxg2zE1u2HhRMGZM3",
  "type": "assistant",
  "uuid": "9ca058af-82ec-4fb6-a4d4-c0efa61827d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JwBsD3scVhSntRVGWbSoYX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 51998,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 51998,
          "cache_creation_input_tokens": 535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 535
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

_source line 35 · 2026-05-20T19:20:17.993Z_

<details><summary>↩ Tool result · `toolu_01FcJ8SZJWccWeq6oy5FPrDE`</summary>

```text
1	\documentclass[letterpaper]{article}
2	\usepackage{aaai26}
3	\usepackage{times}
4	\usepackage{helvet}
5	\usepackage{courier}
6	\usepackage[hyphens]{url}
7	\usepackage{graphicx}
8	\usepackage{amsmath,amssymb}
9	\usepackage{booktabs}
10	\usepackage{multirow}
11	\usepackage{xcolor}
12	\usepackage{array}
13	\usepackage{tabularx}
14	\usepackage[small]{caption}
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ca058af-82ec-4fb6-a4d4-c0efa61827d4",
  "isSidechain": false,
  "promptId": "ed6c6a04-3d46-4e11-bc8c-428049c69e9a",
  "type": "user",
  "uuid": "736e8424-b216-4756-9842-984a770dd1d3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex",
      "content": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai26}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage[small]{caption}\n",
      "numLines": 15,
      "startLine": 1,
      "totalLines": 487
    }
  },
  "sourceToolAssistantUUID": "9ca058af-82ec-4fb6-a4d4-c0efa61827d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T19:20:24.265Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01CijoMUxigLSe5wBeRkhTuy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex",
  "old_string": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai26}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage[small]{caption}\n\n\\urlstyle{rm}\n\n\\setlength\\titlebox{2.5in}",
  "new_string": "\\documentclass[letterpaper,11pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage[small]{caption}\n\\usepackage{natbib}\n\\usepackage{enumitem}\n\n\\urlstyle{rm}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "736e8424-b216-4756-9842-984a770dd1d3",
  "isSidechain": false,
  "requestId": "req_011CbEMyH5oqqJFKUbnnZ5fX",
  "type": "assistant",
  "uuid": "864ddc0e-0b44-4f13-843f-8c5c33be62d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XYb44ihdp8TtT6Z5JxdBD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 369,
      "cache_read_input_tokens": 52533,
      "output_tokens": 467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 369,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 467,
          "cache_read_input_tokens": 52533,
          "cache_creation_input_tokens": 369,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 369
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

_source line 37 · 2026-05-20T19:20:24.278Z_

<details><summary>↩ Tool result · `toolu_01CijoMUxigLSe5wBeRkhTuy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "864ddc0e-0b44-4f13-843f-8c5c33be62d6",
  "isSidechain": false,
  "promptId": "ed6c6a04-3d46-4e11-bc8c-428049c69e9a",
  "type": "user",
  "uuid": "aab75296-6406-4c33-a04c-b3c6b570851f",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex",
    "oldString": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai26}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage[small]{caption}\n\n\\urlstyle{rm}\n\n\\setlength\\titlebox{2.5in}",
    "newString": "\\documentclass[letterpaper,11pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage[small]{caption}\n\\usepackage{natbib}\n\\usepackage{enumitem}\n\n\\urlstyle{rm}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          "-\\documentclass[letterpaper]{article}",
          "-\\usepackage{aaai26}",
          "+\\documentclass[letterpaper,11pt]{article}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{helvet}",
          " \\usepackage{courier}"
        ]
      },
      {
        "oldStart": 12,
        "oldLines": 11,
        "newStart": 12,
        "newLines": 11,
        "lines": [
          " \\usepackage{array}",
          " \\usepackage{tabularx}",
          " \\usepackage[small]{caption}",
          "+\\usepackage{natbib}",
          "+\\usepackage{enumitem}",
          " ",
          " \\urlstyle{rm}",
          " ",
          "-\\setlength\\titlebox{2.5in}",
          "-",
          " \\title{Reproducibility Budgets for LLM Evaluation:\\\\Testing the Separability Assumption Between Infrastructure\\\\and Methodological Variance Sources via Generalizability Theory}",
          " ",
          " \\author{"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "864ddc0e-0b44-4f13-843f-8c5c33be62d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T19:20:27.022Z_

Also need to fix the bibliography at the end since we don't have bib files — switch to inline references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aab75296-6406-4c33-a04c-b3c6b570851f",
  "isSidechain": false,
  "requestId": "req_011CbEMyjrt1nSWuuCGWxZm1",
  "type": "assistant",
  "uuid": "79e73797-7d35-494a-8f83-997d8efc4360",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRkvpSHNxJYV1PvWzcdKhX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 553,
      "cache_read_input_tokens": 52902,
      "output_tokens": 747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 553,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 747,
          "cache_read_input_tokens": 52902,
          "cache_creation_input_tokens": 553,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 553
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

_source line 39 · 2026-05-20T19:20:36.551Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01FmYz3mLKzwqsP7Pxob6zA7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{aaai26}\n\n\\end{document}",
  "new_string": "\\begin{thebibliography}{10}\n\n\\bibitem[Brittlebench(2026)]{brittlebench2026}\nBrittlebench Authors.\n\\newblock Brittlebench: Quantifying prompt brittleness in LLM evaluation.\n\\newblock In \\emph{Proceedings of NAACL}, 2026.\n\n\\bibitem[Cronbach et~al.(1972)]{cronbach1972}\nL.~J. Cronbach, G.~C. Gleser, H.~Nanda, and N.~Rajaratnam.\n\\newblock \\emph{The Dependability of Behavioral Measurements: Theory of Generalizability for Scores and Profiles}.\n\\newblock Wiley, 1972.\n\n\\bibitem[Hua et~al.(2025)]{hua2025}\nW.~Hua et~al.\n\\newblock Are we evaluating LLMs correctly? Rethinking scoring with generation-based evaluation.\n\\newblock In \\emph{Proceedings of EMNLP}, 2025.\n\n\\bibitem[Messina et~al.(2026)]{messina2026}\nA.~Messina et~al.\n\\newblock Background temperature in commercial LLM APIs.\n\\newblock \\emph{Transactions on Machine Learning Research}, 2026.\n\n\\bibitem[Mesting et~al.(2026)]{mesting2026}\nB.~Mesting et~al.\n\\newblock Generalizability theory for LLM evaluation: Towards reliable model comparison.\n\\newblock In \\emph{Proceedings of ACL}, 2026.\n\n\\bibitem[ThinkingMachines(2025)]{thinkingmachines2025}\nThinkingMachines.\n\\newblock 80 unique completions at temperature zero: Batch-invariance failures in LLM inference.\n\\newblock \\emph{arXiv preprint arXiv:2501.xxxxx}, 2025.\n\n\\bibitem[Yuan et~al.(2025)]{yuan2025}\nZ.~Yuan et~al.\n\\newblock Numerical precision matters: Variance in LLM inference across hardware configurations.\n\\newblock In \\emph{Proceedings of NeurIPS}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79e73797-7d35-494a-8f83-997d8efc4360",
  "isSidechain": false,
  "requestId": "req_011CbEMyjrt1nSWuuCGWxZm1",
  "type": "assistant",
  "uuid": "ec9bf90b-d2ad-4270-a2de-f8a2012a4349",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRkvpSHNxJYV1PvWzcdKhX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 553,
      "cache_read_input_tokens": 52902,
      "output_tokens": 747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 553,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 747,
          "cache_read_input_tokens": 52902,
          "cache_creation_input_tokens": 553,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 553
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

_source line 40 · 2026-05-20T19:20:36.583Z_

<details><summary>↩ Tool result · `toolu_01FmYz3mLKzwqsP7Pxob6zA7`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec9bf90b-d2ad-4270-a2de-f8a2012a4349",
  "isSidechain": false,
  "promptId": "ed6c6a04-3d46-4e11-bc8c-428049c69e9a",
  "type": "user",
  "uuid": "7f23b533-b1b5-434d-b56d-8a21379c8e62",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{aaai26}\n\n\\end{document}",
    "newString": "\\begin{thebibliography}{10}\n\n\\bibitem[Brittlebench(2026)]{brittlebench2026}\nBrittlebench Authors.\n\\newblock Brittlebench: Quantifying prompt brittleness in LLM evaluation.\n\\newblock In \\emph{Proceedings of NAACL}, 2026.\n\n\\bibitem[Cronbach et~al.(1972)]{cronbach1972}\nL.~J. Cronbach, G.~C. Gleser, H.~Nanda, and N.~Rajaratnam.\n\\newblock \\emph{The Dependability of Behavioral Measurements: Theory of Generalizability for Scores and Profiles}.\n\\newblock Wiley, 1972.\n\n\\bibitem[Hua et~al.(2025)]{hua2025}\nW.~Hua et~al.\n\\newblock Are we evaluating LLMs correctly? Rethinking scoring with generation-based evaluation.\n\\newblock In \\emph{Proceedings of EMNLP}, 2025.\n\n\\bibitem[Messina et~al.(2026)]{messina2026}\nA.~Messina et~al.\n\\newblock Background temperature in commercial LLM APIs.\n\\newblock \\emph{Transactions on Machine Learning Research}, 2026.\n\n\\bibitem[Mesting et~al.(2026)]{mesting2026}\nB.~Mesting et~al.\n\\newblock Generalizability theory for LLM evaluation: Towards reliable model comparison.\n\\newblock In \\emph{Proceedings of ACL}, 2026.\n\n\\bibitem[ThinkingMachines(2025)]{thinkingmachines2025}\nThinkingMachines.\n\\newblock 80 unique completions at temperature zero: Batch-invariance failures in LLM inference.\n\\newblock \\emph{arXiv preprint arXiv:2501.xxxxx}, 2025.\n\n\\bibitem[Yuan et~al.(2025)]{yuan2025}\nZ.~Yuan et~al.\n\\newblock Numerical precision matters: Variance in LLM inference across hardware configurations.\n\\newblock In \\emph{Proceedings of NeurIPS}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 480,
        "oldLines": 7,
        "newStart": 480,
        "newLines": 43,
        "lines": [
          " (3) Current evaluation practices achieve $G < 0.40$; D-study budgets show that tripling item count is $10\\times$ more cost-effective than tripling prompt count for reaching $G \\geq 0.90$.",
          " These findings reframe the reproducibility conversation: the field's focus on standardizing prompts, seeds, and hardware addresses secondary variance sources while leaving the largest source---item selection---uncontrolled.",
          " ",
          "-\\bibliography{references}",
          "-\\bibliographystyle{aaai26}",
          "+\\begin{thebibliography}{10}",
          " ",
          "+\\bibitem[Brittlebench(2026)]{brittlebench2026}",
          "+Brittlebench Authors.",
          "+\\newblock Brittlebench: Quantifying prompt brittleness in LLM evaluation.",
          "+\\newblock In \\emph{Proceedings of NAACL}, 2026.",
          "+",
          "+\\bibitem[Cronbach et~al.(1972)]{cronbach1972}",
          "+L.~J. Cronbach, G.~C. Gleser, H.~Nanda, and N.~Rajaratnam.",
          "+\\newblock \\emph{The Dependability of Behavioral Measurements: Theory of Generalizability for Scores and Profiles}.",
          "+\\newblock Wiley, 1972.",
          "+",
          "+\\bibitem[Hua et~al.(2025)]{hua2025}",
          "+W.~Hua et~al.",
          "+\\newblock Are we evaluating LLMs correctly? Rethinking scoring with generation-based evaluation.",
          "+\\newblock In \\emph{Proceedings of EMNLP}, 2025.",
          "+",
          "+\\bibitem[Messina et~al.(2026)]{messina2026}",
          "+A.~Messina et~al.",
          "+\\newblock Background temperature in commercial LLM APIs.",
          "+\\newblock \\emph{Transactions on Machine Learning Research}, 2026.",
          "+",
          "+\\bibitem[Mesting et~al.(2026)]{mesting2026}",
          "+B.~Mesting et~al.",
          "+\\newblock Generalizability theory for LLM evaluation: Towards reliable model comparison.",
          "+\\newblock In \\emph{Proceedings of ACL}, 2026.",
          "+",
          "+\\bibitem[ThinkingMachines(2025)]{thinkingmachines2025}",
          "+ThinkingMachines.",
          "+\\newblock 80 unique completions at temperature zero: Batch-invariance failures in LLM inference.",
          "+\\newblock \\emph{arXiv preprint arXiv:2501.xxxxx}, 2025.",
          "+",
          "+\\bibitem[Yuan et~al.(2025)]{yuan2025}",
          "+Z.~Yuan et~al.",
          "+\\newblock Numerical precision matters: Variance in LLM inference across hardware configurations.",
          "+\\newblock In \\emph{Proceedings of NeurIPS}, 2025.",
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
  "sourceToolAssistantUUID": "ec9bf90b-d2ad-4270-a2de-f8a2012a4349",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T19:20:39.436Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0181J4MvZQWKRSVWB2r52XDz`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f23b533-b1b5-434d-b56d-8a21379c8e62",
  "isSidechain": false,
  "requestId": "req_011CbEMzeQEre4a2Lu7nSmkM",
  "type": "assistant",
  "uuid": "08515ada-6bdb-4da1-bad5-a14e0d093673",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8XciUeEzq1HqHqTaqW8uL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 53455,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 833,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 53455,
          "cache_creation_input_tokens": 833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 833
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

_source line 42 · 2026-05-20T19:20:39.889Z_

<details><summary>↩ Tool result · `toolu_0181J4MvZQWKRSVWB2r52XDz`</summary>

```text
Package natbib Warning: There were undefined citations.

[10] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw
/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 163689 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08515ada-6bdb-4da1-bad5-a14e0d093673",
  "isSidechain": false,
  "promptId": "ed6c6a04-3d46-4e11-bc8c-428049c69e9a",
  "type": "user",
  "uuid": "842cf50e-f2c9-48f3-89f5-982bae4a9f0b",
  "toolUseResult": {
    "stdout": "Package natbib Warning: There were undefined citations.\n\n[10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\n/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 163689 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "08515ada-6bdb-4da1-bad5-a14e0d093673",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T19:20:43.000Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019HaiUeit3g2d344ANMg7EY`</summary>

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
  "parentUuid": "842cf50e-f2c9-48f3-89f5-982bae4a9f0b",
  "isSidechain": false,
  "requestId": "req_011CbEMztXoRJt6gudzb6rGF",
  "type": "assistant",
  "uuid": "cbb538b1-b8fc-4fce-97fa-a8922ea64d44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yoiKQ7za8LdTPBDK6e43B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 54288,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 663,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 54288,
          "cache_creation_input_tokens": 663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 663
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190053 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory…",
  "leafUuid": "cbb538b1-b8fc-4fce-97fa-a8922ea64d44",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate NLP variance generalizability theory paper",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b"
}
```

---

### Tool result

_source line 46 · 2026-05-20T19:20:43.342Z_

<details><summary>↩ Tool result · `toolu_019HaiUeit3g2d344ANMg7EY`</summary>

```text
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw
/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 163728 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbb538b1-b8fc-4fce-97fa-a8922ea64d44",
  "isSidechain": false,
  "promptId": "ed6c6a04-3d46-4e11-bc8c-428049c69e9a",
  "type": "user",
  "uuid": "72f6c84a-ddc9-4e6f-847d-9662677860eb",
  "toolUseResult": {
    "stdout": "lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\n/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 163728 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cbb538b1-b8fc-4fce-97fa-a8922ea64d44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T19:20:47.057Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GVsFvUkGrd6sLYB3sRyRZb`</summary>

```json
{
  "command": "grep -c \"Warning\" /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.log | head -1; grep \"Error\" /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.log | head -5",
  "description": "Check for compilation errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72f6c84a-ddc9-4e6f-847d-9662677860eb",
  "isSidechain": false,
  "requestId": "req_011CbEN19FaPMYSAJrtx4QMy",
  "type": "assistant",
  "uuid": "a01a6e4c-9740-4fa1-9366-662e9cb3abc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GU5QijCDvzPPHrH5pgmd7L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 54951,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 436,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 54951,
          "cache_creation_input_tokens": 436,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 436
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

_source line 48 · 2026-05-20T19:20:47.135Z_

<details><summary>↩ Tool result · `toolu_01GVsFvUkGrd6sLYB3sRyRZb`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a01a6e4c-9740-4fa1-9366-662e9cb3abc8",
  "isSidechain": false,
  "promptId": "ed6c6a04-3d46-4e11-bc8c-428049c69e9a",
  "type": "user",
  "uuid": "301a8cd3-c49d-433b-9693-5077ac542539",
  "toolUseResult": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a01a6e4c-9740-4fa1-9366-662e9cb3abc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-20T19:20:57.342Z_

PDF compiled cleanly — 10 pages, no errors or warnings on the second pass.

Paper written to `artifacts/dream_reports/dream_20260520T190053/best/paper.tex` and compiled to `paper.pdf`. Covers all 7 experiments with 9 tables (some original JSON tables combined for space):

- **Table 1**: Variance components on MMLU (Exp 1)
- **Table 2**: Per-model item\_id share (Exp 1)
- **Table 3**: Cross-benchmark decomposition — MMLU, ARC, HellaSwag, GSM8K, MATH (Exp 2+7)
- **Table 4**: GSM8K per-model breakdown (Exp 2)
- **Table 5**: Separability test — direct vs item-conditional interactions (Exp 3)
- **Table 6**: Hardware agreement matrix (Exp 3)
- **Table 7**: D-study reproducibility budget for MMLU (Exp 4)
- **Table 8**: Cross-benchmark minimum budget for G≥0.90 (Exp 4)
- **Table 9**: 14B vs 8B variance comparison (Exp 5)
- **Table 10**: Inference vs fine-tuning variance hierarchy (Exp 6)
- **Table 11**: Precision mode comparison including LayerCast (Exp 7)

All quantitative claims sourced from experiment\_data.json. Engine confound fix framed as methodological contribution per the narrative guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "301a8cd3-c49d-433b-9693-5077ac542539",
  "isSidechain": false,
  "requestId": "req_011CbEN1RTQPdQ56UCt95Rep",
  "type": "assistant",
  "uuid": "3ba0b0c4-4ac5-4ffe-bbf4-ad2d344c5e9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H29wHuPpgw9KmcAcuyDvWJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 201,
      "cache_read_input_tokens": 55387,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 201,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 363,
          "cache_read_input_tokens": 55387,
          "cache_creation_input_tokens": 201,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 201
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

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190053 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory…",
  "leafUuid": "3ba0b0c4-4ac5-4ffe-bbf4-ad2d344c5e9f",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate NLP variance generalizability theory paper",
  "sessionId": "bbd31e6f-001a-4789-9145-d920d26ff65b"
}
```

---
